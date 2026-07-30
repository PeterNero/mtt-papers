from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any

from verify_paper_release_requirements import (
    EDITORIAL_ABSTRACT_RE,
    EDITORIAL_TITLE_RE,
    require_plain_publication_text,
)


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
DECISIONS = ROOT / "catalog" / "expository-review-decisions.json"
DEFAULT_LEDGER = (
    Path.home()
    / "Downloads"
    / "BrainOfEnterprise-MTT-Research-Environment"
    / "data"
    / "publication-ledger.json"
)
DEFAULT_TOKEN_FILE = (
    Path.home()
    / "Downloads"
    / "BrainOfEnterprise-MTT-Research-Environment"
    / ".runtime"
    / "zenodo.token"
)
DEFAULT_BASE_URL = "https://zenodo.org/api"
RETRYABLE_HTTP = {408, 425, 429, 500, 502, 503, 504}
REQUEST_TIMEOUT_SECONDS = 180
UPLOAD_TIMEOUT_SECONDS = 120
READY_STATES = {"reviewed", "reference_ready"}
SOURCE_REPOSITORY_BASE = (
    "https://github.com/PeterNero/mtt-papers/tree/main/papers"
)
RESULTS_REPOSITORY_URL = (
    "https://github.com/PeterNero/mtt-results-repro/tree/"
    "31247ebb5c22f3fbb5443024365433c6ee0bff4a"
)
CREATOR = {
    "name": "Nero, Peter",
    "orcid": "0009-0007-1670-874X",
}
DEFAULT_KEYWORDS = [
    "Modal Triplet Theory",
    "MTT",
    "mathematical physics",
    "reproducible research",
]
THEBIBLIOGRAPHY_RE = re.compile(
    r"\\begin\{thebibliography\}\{[^}]*\}"
    r".*?"
    r"\\end\{thebibliography\}",
    re.DOTALL,
)
REFERENCES_SECTION_RE = re.compile(
    r"\\(?:section|chapter)\*?\{References\}"
    r".*?"
    r"(?=\\end\{document\}|\Z)",
    re.DOTALL | re.IGNORECASE,
)


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def file_digest(path: Path, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_reference_key(value: str) -> str:
    return re.sub(r"\W+", "", value).casefold()


def pandoc_plain_references(source: str, cwd: Path) -> list[str]:
    completed = subprocess.run(
        ["pandoc", "--from=latex", "--to=plain", "--wrap=none"],
        cwd=cwd,
        input=source,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip().splitlines()
        suffix = detail[-1] if detail else f"exit {completed.returncode}"
        raise RuntimeError(f"bibliography conversion failed: {suffix}")
    references = []
    for paragraph in re.split(r"\n\s*\n", completed.stdout.strip()):
        value = " ".join(paragraph.replace("\u00a0", " ").split())
        value = re.sub(r"^\d+\.\s+", "", value)
        if (
            value
            and value.casefold() != "references"
            and not value.isdigit()
        ):
            references.append(value)
    return references


def format_csl_reference(row: dict[str, Any]) -> str:
    names = []
    for author in row.get("author") or []:
        if not isinstance(author, dict):
            continue
        family = str(author.get("family") or "").strip()
        given = str(author.get("given") or "").strip()
        literal = str(author.get("literal") or "").strip()
        name = " ".join(part for part in (given, family) if part) or literal
        if name:
            names.append(name)

    date_parts = ((row.get("issued") or {}).get("date-parts") or [[]])
    year = str(date_parts[0][0]) if date_parts and date_parts[0] else ""
    title = str(row.get("title") or "").strip().rstrip(".")
    parts = []
    if names:
        parts.append("; ".join(names))
    if year:
        parts.append(f"({year})")
    if title:
        parts.append(f"{title}.")

    container = str(row.get("container-title") or "").strip()
    volume = str(row.get("volume") or "").strip()
    issue = str(row.get("issue") or "").strip()
    pages = str(row.get("page") or "").strip()
    publisher = str(row.get("publisher") or "").strip()
    edition = str(row.get("edition") or "").strip()
    if container:
        journal = container
        if volume:
            journal += f", {volume}"
        if issue:
            journal += f"({issue})"
        if pages:
            journal += f", {pages}"
        parts.append(journal + ".")
    elif publisher:
        book = publisher
        if edition:
            book += f", edition {edition}"
        parts.append(book + ".")

    doi = str(row.get("DOI") or row.get("doi") or "").strip()
    url = str(row.get("URL") or row.get("url") or "").strip()
    if doi:
        parts.append(f"https://doi.org/{doi}")
    elif url.startswith(("http://", "https://")):
        parts.append(url)
    return " ".join(parts).strip()


def bib_file_references(paper_dir: Path) -> list[str]:
    bibliographies = sorted(paper_dir.glob("*.bib"))
    if not bibliographies:
        return []
    completed = subprocess.run(
        [
            "pandoc",
            *(str(path) for path in bibliographies),
            "--from=biblatex",
            "--to=csljson",
        ],
        cwd=paper_dir,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip().splitlines()
        suffix = detail[-1] if detail else f"exit {completed.returncode}"
        raise RuntimeError(f"bibliography extraction failed: {suffix}")
    try:
        rows = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"bibliography extraction returned invalid JSON: {error}"
        ) from error
    return [
        value
        for value in (
            format_csl_reference(row)
            for row in rows
            if isinstance(row, dict)
        )
        if value
    ]


def source_references(paper_id: str) -> list[str]:
    paper_dir = PAPERS / paper_id
    tex_path = paper_dir / "main.tex"
    source = tex_path.read_text(encoding="utf-8-sig", errors="replace")
    references = []
    for match in THEBIBLIOGRAPHY_RE.finditer(source):
        references.extend(
            pandoc_plain_references(match.group(0), paper_dir)
        )
    if not references:
        match = REFERENCES_SECTION_RE.search(source)
        if match:
            references.extend(
                pandoc_plain_references(match.group(0), paper_dir)
            )
    if not references:
        references.extend(bib_file_references(paper_dir))

    unique = []
    seen = set()
    for reference in references:
        key = normalize_reference_key(reference)
        if key and key not in seen:
            seen.add(key)
            unique.append(reference)
    if not unique:
        raise RuntimeError(
            f"{paper_id}: no external references could be extracted"
        )
    return unique


def required_related_identifiers(
    paper_id: str,
    existing: list[dict[str, Any]],
) -> list[dict[str, str]]:
    selected = []
    for row in existing:
        if not isinstance(row, dict):
            continue
        identifier = str(row.get("identifier") or "").strip()
        relation = str(row.get("relation") or "").strip()
        if not identifier or not relation:
            continue
        if (
            "github.com/PeterNero/mtt-papers" in identifier
            or "github.com/PeterNero/mtt-results-repro" in identifier
        ):
            continue
        selected.append(
            {
                "identifier": identifier,
                "relation": relation,
            }
        )
    selected.extend(
        [
            {
                "identifier": (
                    f"{SOURCE_REPOSITORY_BASE}/{paper_id}"
                ),
                "relation": "isDocumentedBy",
            },
            {
                "identifier": RESULTS_REPOSITORY_URL,
                "relation": "isDocumentedBy",
            },
        ]
    )
    return list(
        {
            (row["identifier"], row["relation"]): row
            for row in selected
        }.values()
    )


def remote_filename(row: dict[str, Any]) -> str:
    return str(
        row.get("filename")
        or row.get("key")
        or row.get("id")
        or ""
    )


def remote_md5(row: dict[str, Any]) -> str:
    value = str(row.get("checksum") or "").strip().lower()
    return value.removeprefix("md5:")


class ZenodoClient:
    def __init__(self, token: str, base_url: str) -> None:
        if not token:
            raise ValueError("Zenodo token is empty")
        self.token = token
        self.base_url = base_url.rstrip("/")

    def _url(self, path_or_url: str) -> str:
        if path_or_url.startswith(("http://", "https://")):
            return path_or_url
        return f"{self.base_url}/{path_or_url.lstrip('/')}"

    def request(
        self,
        method: str,
        path_or_url: str,
        payload: Any | None = None,
        *,
        timeout: int = REQUEST_TIMEOUT_SECONDS,
    ) -> dict[str, Any]:
        body = (
            json.dumps(payload).encode("utf-8")
            if payload is not None
            else None
        )
        url = self._url(path_or_url)
        for attempt in range(3):
            request = urllib.request.Request(
                url,
                data=body,
                method=method,
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/json",
                    "User-Agent": "mtt-papers-release-readiness/1",
                },
            )
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    raw = response.read()
                if not raw:
                    return {}
                value = json.loads(raw.decode("utf-8"))
                if not isinstance(value, dict):
                    raise RuntimeError(f"{url}: expected a JSON object")
                return value
            except urllib.error.HTTPError as error:
                detail = error.read().decode(
                    "utf-8",
                    errors="replace",
                )[:2000]
                if error.code not in RETRYABLE_HTTP or attempt == 2:
                    raise RuntimeError(
                        f"{method} {url}: HTTP {error.code}: {detail}"
                    ) from error
            except (TimeoutError, urllib.error.URLError) as error:
                if attempt == 2:
                    raise RuntimeError(f"{method} {url}: {error}") from error
            time.sleep(min(2**attempt, 12))
        raise AssertionError("unreachable")

    def request_list(
        self,
        method: str,
        path_or_url: str,
        payload: Any | None = None,
        *,
        timeout: int = REQUEST_TIMEOUT_SECONDS,
    ) -> list[dict[str, Any]]:
        body = (
            json.dumps(payload).encode("utf-8")
            if payload is not None
            else None
        )
        url = self._url(path_or_url)
        for attempt in range(3):
            request = urllib.request.Request(
                url,
                data=body,
                method=method,
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/json",
                    "User-Agent": "mtt-papers-release-readiness/1",
                },
            )
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    raw = response.read()
                if not raw:
                    return []
                value = json.loads(raw.decode("utf-8"))
                if not isinstance(value, list) or not all(
                    isinstance(row, dict) for row in value
                ):
                    raise RuntimeError(
                        f"{url}: expected a JSON array of objects"
                    )
                return value
            except urllib.error.HTTPError as error:
                detail = error.read().decode(
                    "utf-8",
                    errors="replace",
                )[:2000]
                if error.code not in RETRYABLE_HTTP or attempt == 2:
                    raise RuntimeError(
                        f"{method} {url}: HTTP {error.code}: {detail}"
                    ) from error
            except (TimeoutError, urllib.error.URLError) as error:
                if attempt == 2:
                    raise RuntimeError(f"{method} {url}: {error}") from error
            time.sleep(min(2**attempt, 12))
        raise AssertionError("unreachable")

    def upload_invenio(
        self,
        deposition_id: str,
        filename: str,
        path: Path,
    ) -> dict[str, Any]:
        encoded = urllib.parse.quote(filename, safe="")
        listing = self.request(
            "GET",
            f"records/{deposition_id}/draft/files",
        )
        entries = listing.get("entries") or []
        existing = [
            row
            for row in entries
            if str((row or {}).get("key") or "") == filename
        ]
        expected_md5 = file_digest(path, "md5")
        if any(remote_md5(row) == expected_md5 for row in existing):
            return existing[0]
        if not existing:
            self.request(
                "POST",
                f"records/{deposition_id}/draft/files",
                [{"key": filename}],
            )
        content_url = self._url(
            f"records/{deposition_id}/draft/files/{encoded}/content"
        )
        data = path.read_bytes()
        for attempt in range(2):
            request = urllib.request.Request(
                content_url,
                data=data,
                method="PUT",
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/octet-stream",
                    "Content-Length": str(len(data)),
                    "User-Agent": "mtt-papers-release-readiness/1",
                },
            )
            try:
                with urllib.request.urlopen(
                    request,
                    timeout=UPLOAD_TIMEOUT_SECONDS,
                ) as response:
                    value = json.loads(response.read().decode("utf-8"))
                if not isinstance(value, dict):
                    raise RuntimeError(
                        f"{content_url}: expected a JSON object"
                    )
                break
            except urllib.error.HTTPError as error:
                detail = error.read().decode(
                    "utf-8",
                    errors="replace",
                )[:2000]
                if error.code not in RETRYABLE_HTTP or attempt == 1:
                    raise RuntimeError(
                        f"PUT {content_url}: HTTP {error.code}: {detail}"
                    ) from error
            except (TimeoutError, urllib.error.URLError) as error:
                if attempt == 1:
                    raise RuntimeError(
                        f"PUT {content_url}: {error}"
                    ) from error
            time.sleep(min(2**attempt, 12))
        return self.request(
            "POST",
            (
                f"records/{deposition_id}/draft/files/"
                f"{encoded}/commit"
            ),
        )

    def upload(self, bucket_url: str, filename: str, path: Path) -> dict[str, Any]:
        url = (
            f"{bucket_url.rstrip('/')}/"
            f"{urllib.parse.quote(filename, safe='')}"
        )
        data = path.read_bytes()
        for attempt in range(2):
            request = urllib.request.Request(
                url,
                data=data,
                method="PUT",
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/octet-stream",
                    "User-Agent": "mtt-papers-release-readiness/1",
                },
            )
            try:
                with urllib.request.urlopen(
                    request,
                    timeout=UPLOAD_TIMEOUT_SECONDS,
                ) as response:
                    value = json.loads(response.read().decode("utf-8"))
                if not isinstance(value, dict):
                    raise RuntimeError(f"{url}: expected a JSON object")
                return value
            except urllib.error.HTTPError as error:
                detail = error.read().decode(
                    "utf-8",
                    errors="replace",
                )[:2000]
                if error.code not in RETRYABLE_HTTP or attempt == 1:
                    raise RuntimeError(
                        f"PUT {url}: HTTP {error.code}: {detail}"
                    ) from error
            except (TimeoutError, urllib.error.URLError) as error:
                if attempt == 1:
                    raise RuntimeError(f"PUT {url}: {error}") from error
            time.sleep(min(2**attempt, 12))
        raise AssertionError("unreachable")

    def upload_legacy(
        self,
        deposition_id: str,
        filename: str,
        path: Path,
    ) -> dict[str, Any]:
        boundary = f"----mtt-zenodo-{uuid.uuid4().hex}"
        marker = boundary.encode("ascii")
        body = b"".join(
            (
                b"--" + marker + b"\r\n",
                b'Content-Disposition: form-data; name="name"\r\n\r\n',
                filename.encode("utf-8"),
                b"\r\n--" + marker + b"\r\n",
                (
                    b'Content-Disposition: form-data; name="file"; '
                    b'filename="' + filename.encode("utf-8") + b'"\r\n'
                ),
                b"Content-Type: application/pdf\r\n\r\n",
                path.read_bytes(),
                b"\r\n--" + marker + b"--\r\n",
            )
        )
        url = self._url(
            f"deposit/depositions/{deposition_id}/files"
        )
        for attempt in range(2):
            request = urllib.request.Request(
                url,
                data=body,
                method="POST",
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": (
                        f"multipart/form-data; boundary={boundary}"
                    ),
                    "User-Agent": "mtt-papers-release-readiness/1",
                },
            )
            try:
                with urllib.request.urlopen(
                    request,
                    timeout=UPLOAD_TIMEOUT_SECONDS,
                ) as response:
                    value = json.loads(response.read().decode("utf-8"))
                if not isinstance(value, dict):
                    raise RuntimeError(f"{url}: expected a JSON object")
                return value
            except urllib.error.HTTPError as error:
                detail = error.read().decode(
                    "utf-8",
                    errors="replace",
                )[:2000]
                retryable_transfer_failure = (
                    error.code == 400
                    and "upload transfer failed" in detail.casefold()
                )
                if (
                    error.code not in RETRYABLE_HTTP
                    and not retryable_transfer_failure
                ) or attempt == 1:
                    raise RuntimeError(
                        f"POST {url}: HTTP {error.code}: {detail}"
                    ) from error
            except (TimeoutError, urllib.error.URLError) as error:
                if attempt == 1:
                    raise RuntimeError(f"POST {url}: {error}") from error
            time.sleep(min(2**attempt, 12))
        raise AssertionError("unreachable")

    def delete_file(self, row: dict[str, Any]) -> None:
        url = str((row.get("links") or {}).get("self") or "").strip()
        if not url:
            raise RuntimeError(
                f"{remote_filename(row)}: draft file lacks a deletion URL"
            )
        self.request("DELETE", url)


def ready_paper_ids(selected: set[str] | None) -> list[str]:
    decisions = read_json(DECISIONS).get("papers") or {}
    ids = sorted(
        str(paper_id)
        for paper_id, decision in decisions.items()
        if str((decision or {}).get("status") or "") in READY_STATES
    )
    if selected:
        missing = sorted(selected - set(ids))
        if missing:
            raise ValueError(
                "selected paper is not release-reviewed: "
                + ", ".join(missing)
            )
        ids = [paper_id for paper_id in ids if paper_id in selected]
    return ids


def validate_local_metadata(paper_id: str, metadata: dict[str, Any]) -> None:
    title = str(metadata.get("title") or "").strip()
    description = str(metadata.get("abstract") or "").strip()
    version = str(metadata.get("current_version") or "").strip()
    if not title or not description or not version:
        raise ValueError(f"{paper_id}: title, abstract, or version is empty")
    if EDITORIAL_TITLE_RE.search(title):
        raise ValueError(f"{paper_id}: title contains correction history")
    if EDITORIAL_ABSTRACT_RE.search(description):
        raise ValueError(f"{paper_id}: abstract contains correction history")
    require_plain_publication_text(paper_id, "metadata abstract", description)


def is_editable(draft: dict[str, Any]) -> bool:
    state = str(draft.get("state") or "").casefold()
    return not bool(draft.get("submitted")) and state not in {
        "done",
        "published",
    }


def get_deposition(
    client: ZenodoClient,
    deposition_id: str,
) -> dict[str, Any]:
    return client.request(
        "GET",
        f"deposit/depositions/{deposition_id}",
    )


def find_editable_concept_draft(
    client: ZenodoClient,
    source: dict[str, Any],
) -> dict[str, Any] | None:
    concept_id = str(
        source.get("conceptrecid")
        or source.get("conceptrecord_id")
        or ""
    ).strip()
    source_id = str(source.get("id") or "").strip()
    if not concept_id:
        return None
    query = urllib.parse.urlencode(
        {
            "size": 100,
            "q": f"conceptrecid:{concept_id}",
        }
    )
    candidates = [
        row
        for row in client.request_list(
            "GET",
            f"deposit/depositions?{query}",
        )
        if str(row.get("id") or "").strip() != source_id
        and is_editable(row)
    ]
    if not candidates:
        return None
    candidates.sort(
        key=lambda row: (
            str(row.get("modified") or row.get("created") or ""),
            int(row.get("id") or 0),
        )
    )
    return candidates[-1]


def recover_or_create_draft(
    client: ZenodoClient,
    paper_id: str,
    metadata: dict[str, Any],
    entry: dict[str, Any],
) -> tuple[dict[str, Any], str]:
    tracked_id = str(entry.get("draft_id") or "").strip()
    if tracked_id:
        tracked = get_deposition(client, tracked_id)
        if is_editable(tracked):
            return tracked, "update_existing_draft"

    latest = metadata.get("latest_zenodo_release") or {}
    latest_id = str(latest.get("id") or "").strip()
    if not latest_id:
        created = client.request("POST", "deposit/depositions", {})
        return created, "create_new_draft"

    source = get_deposition(client, latest_id)
    latest_draft_url = str(
        (source.get("links") or {}).get("latest_draft") or ""
    ).strip()
    if latest_draft_url:
        candidate = client.request("GET", latest_draft_url)
        if (
            str(candidate.get("id") or "") != latest_id
            and is_editable(candidate)
        ):
            return candidate, "recover_existing_new_version_draft"
    candidate = find_editable_concept_draft(client, source)
    if candidate is not None:
        return candidate, "recover_existing_concept_draft"

    try:
        response = client.request(
            "POST",
            f"deposit/depositions/{latest_id}/actions/newversion",
            {},
        )
    except RuntimeError as error:
        if (
            "files.enabled" not in str(error)
            and "Please remove all files first" not in str(error)
        ):
            raise
        modern = client.request(
            "POST",
            f"records/{latest_id}/versions",
        )
        modern_id = str(modern.get("id") or "").strip()
        if not modern_id:
            raise RuntimeError(
                f"{paper_id}: modern new-version response lacks id"
            ) from error
        return (
            get_deposition(client, modern_id),
            "create_new_version_draft_modern_api",
        )
    latest_draft_url = str(
        (response.get("links") or {}).get("latest_draft") or ""
    ).strip()
    if not latest_draft_url:
        raise RuntimeError(
            f"{paper_id}: new-version response lacks latest_draft"
        )
    candidate = client.request("GET", latest_draft_url)
    if (
        str(candidate.get("id") or "") != latest_id
        and is_editable(candidate)
    ):
        return candidate, "create_new_version_draft"
    candidate = find_editable_concept_draft(client, source)
    if candidate is not None:
        return candidate, "create_new_version_draft_recovered_by_concept"
    raise RuntimeError(
        f"{paper_id}: Zenodo created no recoverable editable new-version draft"
    )


def clean_metadata(
    paper_id: str,
    canonical: dict[str, Any],
    draft: dict[str, Any],
    entry: dict[str, Any],
) -> dict[str, Any]:
    existing = dict(draft.get("metadata") or {})
    overrides = dict(entry.get("metadata_overrides") or {})
    title = str(canonical["title"]).strip()
    description = str(canonical["abstract"]).strip()
    version = str(canonical["current_version"]).strip()
    notes = str(overrides.get("notes") or existing.get("notes") or "").strip()
    if not notes:
        notes = (
            "Revision history and rationale are documented separately in the "
            "paper's revision note and repository revision audit."
        )
    configured_references = overrides.get("external_references")
    if isinstance(configured_references, list):
        references = [
            str(value).strip()
            for value in configured_references
            if str(value).strip()
        ]
    else:
        references = [
            str(value).strip()
            for value in existing.get("references") or []
            if str(value).strip()
        ]
    if not references:
        references = source_references(paper_id)

    configured_keywords = overrides.get("keywords")
    if isinstance(configured_keywords, list):
        keywords = [
            str(value).strip()
            for value in configured_keywords
            if str(value).strip()
        ]
    else:
        keywords = [
            str(value).strip()
            for value in existing.get("keywords") or []
            if str(value).strip()
        ]
    if not keywords:
        keywords = list(DEFAULT_KEYWORDS)

    communities = [
        dict(row)
        for row in existing.get("communities") or []
        if isinstance(row, dict)
        and str(row.get("identifier") or "").strip()
    ]
    if not any(
        str(row.get("identifier") or "").strip() == "mtt"
        for row in communities
    ):
        communities.append({"identifier": "mtt"})

    existing_related = [
        row
        for row in existing.get("related_identifiers") or []
        if isinstance(row, dict)
    ]
    configured_related = overrides.get("related_identifiers")
    if isinstance(configured_related, list):
        existing_related.extend(
            row
            for row in configured_related
            if isinstance(row, dict)
        )
    existing.update(
        {
            "title": title,
            "description": description,
            "version": version,
            "notes": notes,
            "upload_type": "publication",
            "publication_type": "preprint",
            "creators": [dict(CREATOR)],
            "keywords": keywords,
            "related_identifiers": required_related_identifiers(
                paper_id,
                existing_related,
            ),
            "references": references,
            "access_right": "open",
            "license": "cc-by-4.0",
            "language": "eng",
            "communities": communities,
        }
    )
    require_plain_publication_text(
        paper_id,
        "Zenodo description",
        description,
    )
    return existing


def verify_remote(
    paper_id: str,
    canonical: dict[str, Any],
    entry: dict[str, Any],
    draft: dict[str, Any],
) -> dict[str, Any]:
    failures = verify_remote_metadata(paper_id, canonical, draft)
    local_pdf = PAPERS / paper_id / "main.pdf"
    local_md5 = file_digest(local_pdf, "md5")
    local_sha256 = file_digest(local_pdf, "sha256")
    metadata = draft.get("metadata") or {}
    description = str(metadata.get("description") or "").strip()
    title = str(metadata.get("title") or "").strip()
    version = str(metadata.get("version") or "").strip()

    if not is_editable(draft):
        failures.append("record is not an editable unsubmitted draft")
    if title != str(canonical.get("title") or "").strip():
        failures.append("remote title differs from canonical title")
    if version != str(canonical.get("current_version") or "").strip():
        failures.append("remote version differs from canonical version")
    if description != str(canonical.get("abstract") or "").strip():
        failures.append("remote description differs from canonical abstract")
    if EDITORIAL_TITLE_RE.search(title):
        failures.append("remote title contains correction history")
    if EDITORIAL_ABSTRACT_RE.search(description):
        failures.append("remote description contains correction history")
    try:
        require_plain_publication_text(
            paper_id,
            "remote Zenodo description",
            description,
        )
    except AssertionError as error:
        failures.append(str(error))

    pdfs = [
        row
        for row in draft.get("files") or []
        if remote_filename(row).lower().endswith(".pdf")
    ]
    exact = [row for row in pdfs if remote_md5(row) == local_md5]
    if len(exact) != 1:
        failures.append(
            f"expected one exact current PDF, found {len(exact)}"
        )
    if len(pdfs) != 1:
        failures.append(
            f"expected no stale PDF files, found {len(pdfs)} total PDFs"
        )

    reviewed_pdf = str(entry.get("reviewed_pdf_sha256") or "")
    if reviewed_pdf and reviewed_pdf != local_sha256:
        failures.append("local PDF differs from recorded reviewed PDF hash")

    return {
        "paper_id": paper_id,
        "draft_id": str(draft.get("id") or ""),
        "version": version,
        "local_pdf_md5": local_md5,
        "local_pdf_sha256": local_sha256,
        "remote_pdf": remote_filename(exact[0]) if len(exact) == 1 else "",
        "remote_pdf_count": len(pdfs),
        "exact_remote_pdf_count": len(exact),
        "failures": failures,
        "ready": not failures,
    }


def verify_remote_metadata(
    paper_id: str,
    canonical: dict[str, Any],
    draft: dict[str, Any],
) -> list[str]:
    failures: list[str] = []
    metadata = draft.get("metadata") or {}
    title = str(metadata.get("title") or "").strip()
    description = str(metadata.get("description") or "").strip()
    version = str(metadata.get("version") or "").strip()
    if not is_editable(draft):
        failures.append("record is not an editable unsubmitted draft")
    if title != str(canonical.get("title") or "").strip():
        failures.append("remote title differs from canonical title")
    if version != str(canonical.get("current_version") or "").strip():
        failures.append("remote version differs from canonical version")
    if description != str(canonical.get("abstract") or "").strip():
        failures.append("remote description differs from canonical abstract")
    if EDITORIAL_TITLE_RE.search(title):
        failures.append("remote title contains correction history")
    if EDITORIAL_ABSTRACT_RE.search(description):
        failures.append("remote description contains correction history")
    try:
        require_plain_publication_text(
            paper_id,
            "remote Zenodo description",
            description,
        )
    except AssertionError as error:
        failures.append(str(error))

    references = [
        str(value).strip()
        for value in metadata.get("references") or []
        if str(value).strip()
    ]
    if not references:
        failures.append("remote Zenodo references are empty")

    related = [
        row
        for row in metadata.get("related_identifiers") or []
        if isinstance(row, dict)
    ]
    identifiers = {
        str(row.get("identifier") or "").strip()
        for row in related
    }
    if not any(
        "github.com/PeterNero/mtt-papers" in value
        for value in identifiers
    ):
        failures.append("canonical paper repository relation is missing")
    if not any(
        "github.com/PeterNero/mtt-results-repro" in value
        for value in identifiers
    ):
        failures.append("curated results repository relation is missing")

    creators = [
        row
        for row in metadata.get("creators") or []
        if isinstance(row, dict)
    ]
    if not any(
        str(row.get("name") or "").strip() == CREATOR["name"]
        and str(row.get("orcid") or "").strip() == CREATOR["orcid"]
        for row in creators
    ):
        failures.append("canonical creator or ORCID is missing")
    if str(metadata.get("upload_type") or "") != "publication":
        failures.append("upload type is not publication")
    if str(metadata.get("publication_type") or "") != "preprint":
        failures.append("publication type is not preprint")
    if str(metadata.get("access_right") or "") != "open":
        failures.append("access right is not open")
    if str(metadata.get("license") or "") != "cc-by-4.0":
        failures.append("license is not cc-by-4.0")
    if str(metadata.get("language") or "") != "eng":
        failures.append("language is not eng")
    if not (metadata.get("keywords") or []):
        failures.append("keywords are missing")
    communities = {
        str(row.get("identifier") or "").strip()
        for row in metadata.get("communities") or []
        if isinstance(row, dict)
    }
    if "mtt" not in communities:
        failures.append("MTT community is missing")
    if not str(metadata.get("notes") or "").strip():
        failures.append("separate revision notes are missing")
    return failures


def sync_metadata_one(
    client: ZenodoClient,
    paper_id: str,
    canonical: dict[str, Any],
    ledger: dict[str, Any],
    ledger_path: Path,
) -> dict[str, Any]:
    papers = ledger.setdefault("papers", {})
    entry = dict(papers.get(paper_id) or {})
    draft, strategy = recover_or_create_draft(
        client,
        paper_id,
        canonical,
        entry,
    )
    draft_id = str(draft["id"])
    selected_metadata = clean_metadata(
        paper_id,
        canonical,
        draft,
        entry,
    )
    draft = client.request(
        "PUT",
        f"deposit/depositions/{draft_id}",
        {"metadata": selected_metadata},
    )
    failures = verify_remote_metadata(paper_id, canonical, draft)
    if failures:
        raise RuntimeError("; ".join(failures))
    local_pdf = PAPERS / paper_id / "main.pdf"
    local_md5 = file_digest(local_pdf, "md5")
    papers[paper_id] = {
        **entry,
        "draft_id": draft_id,
        "draft_doi": str(
            ((draft.get("metadata") or {}).get("prereserve_doi") or {}).get(
                "doi"
            )
            or draft.get("doi")
            or ""
        ),
        "last_synced_at": datetime.now(timezone.utc).isoformat(
            timespec="seconds"
        ),
        "calculation_repository_url": RESULTS_REPOSITORY_URL,
        "pdf_uploaded": any(
            remote_filename(row).lower().endswith(".pdf")
            and remote_md5(row) == local_md5
            for row in draft.get("files") or []
        ),
        "strategy": strategy,
        "zenodo_references_applied": True,
        "metadata_overrides": {
            **dict(entry.get("metadata_overrides") or {}),
            "title": str(canonical["title"]).strip(),
            "description": str(canonical["abstract"]).strip(),
            "notes": str(selected_metadata.get("notes") or "").strip(),
            "creators": selected_metadata["creators"],
            "keywords": selected_metadata["keywords"],
            "external_references": selected_metadata["references"],
            "related_identifiers": selected_metadata[
                "related_identifiers"
            ],
            "source_repository_url": (
                f"{SOURCE_REPOSITORY_BASE}/{paper_id}"
            ),
            "access_right": "open",
            "license": "cc-by-4.0",
            "language": "eng",
            "publication_type": "preprint",
        },
    }
    write_json_atomic(ledger_path, ledger)
    return {
        "paper_id": paper_id,
        "draft_id": draft_id,
        "version": str(canonical["current_version"]),
        "remote_pdf": "",
        "strategy": strategy,
        "ready": True,
        "failures": [],
    }


def sync_one(
    client: ZenodoClient,
    paper_id: str,
    canonical: dict[str, Any],
    ledger: dict[str, Any],
    ledger_path: Path,
) -> dict[str, Any]:
    papers = ledger.setdefault("papers", {})
    entry = dict(papers.get(paper_id) or {})
    draft, strategy = recover_or_create_draft(
        client,
        paper_id,
        canonical,
        entry,
    )
    draft_id = str(draft["id"])
    selected_metadata = clean_metadata(
        paper_id,
        canonical,
        draft,
        entry,
    )
    draft = client.request(
        "PUT",
        f"deposit/depositions/{draft_id}",
        {"metadata": selected_metadata},
    )

    local_pdf = PAPERS / paper_id / "main.pdf"
    local_md5 = file_digest(local_pdf, "md5")
    local_sha256 = file_digest(local_pdf, "sha256")
    pdfs = [
        row
        for row in draft.get("files") or []
        if remote_filename(row).lower().endswith(".pdf")
    ]
    exact = [row for row in pdfs if remote_md5(row) == local_md5]
    if not exact:
        bucket = str((draft.get("links") or {}).get("bucket") or "").strip()
        if not bucket:
            raise RuntimeError(f"{paper_id}: draft lacks a file bucket")
        # Match the kernel publication service exactly: every revision is
        # uploaded under the stable artifact name and identified by checksum.
        upload_name = "main.pdf"
        try:
            client.upload(bucket, upload_name, local_pdf)
        except RuntimeError as bucket_error:
            draft = get_deposition(client, draft_id)
            already_exact = [
                row
                for row in draft.get("files") or []
                if (
                    remote_filename(row).lower().endswith(".pdf")
                    and remote_md5(row) == local_md5
                )
            ]
            if not already_exact:
                print(
                    "  bucket upload failed; trying the draft-file "
                    f"content/commit API ({bucket_error})",
                    flush=True,
                )
                try:
                    client.upload_invenio(
                        draft_id,
                        upload_name,
                        local_pdf,
                    )
                except RuntimeError as draft_file_error:
                    print(
                        "  draft-file upload failed; trying the "
                        "documented legacy deposition-file API "
                        f"({draft_file_error})",
                        flush=True,
                    )
                    client.upload_legacy(
                        draft_id,
                        upload_name,
                        local_pdf,
                    )
        draft = get_deposition(client, draft_id)
        pdfs = [
            row
            for row in draft.get("files") or []
            if remote_filename(row).lower().endswith(".pdf")
        ]
        exact = [row for row in pdfs if remote_md5(row) == local_md5]
        if len(exact) != 1:
            raise RuntimeError(
                f"{paper_id}: uploaded PDF checksum was not confirmed"
            )

    keep_name = remote_filename(exact[0])
    for row in list(pdfs):
        if remote_filename(row) != keep_name:
            client.delete_file(row)

    draft = get_deposition(client, draft_id)
    verification_entry = {
        **entry,
        "draft_id": draft_id,
        "draft_doi": str(
            ((draft.get("metadata") or {}).get("prereserve_doi") or {}).get(
                "doi"
            )
            or draft.get("doi")
            or ""
        ),
        "last_synced_at": datetime.now(timezone.utc).isoformat(
            timespec="seconds"
        ),
        "calculation_repository_url": RESULTS_REPOSITORY_URL,
        "strategy": strategy,
        "pdf_uploaded": True,
        "pdf_filename": keep_name,
        "pdf_md5": local_md5,
        "pdf_sha256": local_sha256,
        "zenodo_references_applied": True,
        "metadata_overrides": {
            **dict(entry.get("metadata_overrides") or {}),
            "title": str(canonical["title"]).strip(),
            "description": str(canonical["abstract"]).strip(),
            "notes": str(selected_metadata.get("notes") or "").strip(),
            "creators": selected_metadata["creators"],
            "keywords": selected_metadata["keywords"],
            "external_references": selected_metadata["references"],
            "related_identifiers": selected_metadata[
                "related_identifiers"
            ],
            "source_repository_url": (
                f"{SOURCE_REPOSITORY_BASE}/{paper_id}"
            ),
            "access_right": "open",
            "license": "cc-by-4.0",
            "language": "eng",
            "publication_type": "preprint",
        },
    }
    papers[paper_id] = verification_entry
    write_json_atomic(ledger_path, ledger)
    result = verify_remote(
        paper_id,
        canonical,
        verification_entry,
        draft,
    )
    if not result["ready"]:
        raise RuntimeError(
            f"{paper_id}: post-sync verification failed: "
            + "; ".join(result["failures"])
        )
    result["strategy"] = strategy
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Synchronize or verify reviewed MTT Zenodo drafts without "
            "publishing them."
        )
    )
    parser.add_argument(
        "mode",
        choices=("metadata", "sync", "verify"),
    )
    parser.add_argument(
        "--paper-id",
        action="append",
        default=[],
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        default=DEFAULT_LEDGER,
    )
    parser.add_argument(
        "--token-file",
        type=Path,
        default=DEFAULT_TOKEN_FILE,
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
    )
    args = parser.parse_args()

    try:
        token = os.environ.get("ZENODO_ACCESS_TOKEN", "").strip()
        if not token:
            token = args.token_file.read_text(encoding="utf-8").strip()
        client = ZenodoClient(token, args.base_url)
        ledger_path = args.ledger.resolve()
        ledger = read_json(ledger_path)
        selected = set(args.paper_id) or None
        paper_ids = ready_paper_ids(selected)
        results: list[dict[str, Any]] = []
        failures: list[dict[str, str]] = []
        for index, paper_id in enumerate(paper_ids, start=1):
            canonical = read_json(PAPERS / paper_id / "metadata.json")
            validate_local_metadata(paper_id, canonical)
            print(
                f"[{index}/{len(paper_ids)}] {args.mode} {paper_id}",
                flush=True,
            )
            try:
                if args.mode == "sync":
                    result = sync_one(
                        client,
                        paper_id,
                        canonical,
                        ledger,
                        ledger_path,
                    )
                elif args.mode == "metadata":
                    result = sync_metadata_one(
                        client,
                        paper_id,
                        canonical,
                        ledger,
                        ledger_path,
                    )
                else:
                    entry = (
                        (ledger.get("papers") or {}).get(paper_id) or {}
                    )
                    draft_id = str(entry.get("draft_id") or "").strip()
                    if not draft_id:
                        raise RuntimeError("publication ledger lacks draft id")
                    draft = get_deposition(client, draft_id)
                    result = verify_remote(
                        paper_id,
                        canonical,
                        entry,
                        draft,
                    )
                    if not result["ready"]:
                        results.append(result)
                        error = "; ".join(result["failures"])
                        failures.append(
                            {
                                "paper_id": paper_id,
                                "error": error,
                            }
                        )
                        print(f"  FAILED {error}", flush=True)
                        continue
                results.append(result)
                if args.mode == "metadata":
                    print(
                        f"  METADATA READY draft {result['draft_id']}",
                        flush=True,
                    )
                else:
                    print(
                        f"  READY draft {result['draft_id']} "
                        f"{result['remote_pdf']}",
                        flush=True,
                    )
            except Exception as error:
                failures.append(
                    {
                        "paper_id": paper_id,
                        "error": str(error),
                    }
                )
                print(f"  FAILED {error}", flush=True)

        summary = {
            "generated_at": datetime.now(timezone.utc).isoformat(
                timespec="seconds"
            ),
            "mode": args.mode,
            "papers": len(paper_ids),
            "ready": sum(bool(row.get("ready")) for row in results),
            "failed": len(failures),
            "failures": failures,
            "results": results,
        }
        if args.report is not None:
            write_json_atomic(args.report.resolve(), summary)
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 1 if failures else 0
    except Exception as error:
        print(f"Zenodo draft readiness failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
