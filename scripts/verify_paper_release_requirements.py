from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
DECISIONS = ROOT / "catalog" / "expository-review-decisions.json"

READY_STATES = {"reviewed", "reference_ready"}
EDITORIAL_ABSTRACT_RE = re.compile(
    r"\bcorrected\b|"
    r"\bsupersedes?\b|"
    r"\brevision note\b|"
    r"\bthis edition\b|"
    r"\bearlier version\b|"
    r"\bversion\s+\d+(?:\.\d+)?\b",
    re.IGNORECASE,
)
EDITORIAL_TITLE_RE = re.compile(
    r"\bcorrected\b|\bedition\b|\brevised version\b",
    re.IGNORECASE,
)
TEX_METADATA_RE = re.compile(
    r"\\[A-Za-z@]+|"
    r"\\[()[\]]|"
    r"(?<!\\)\$|"
    r"\\[{}%#&_^~]",
)
HTML_TAG_RE = re.compile(r"<[^>]+>")
FORBIDDEN_FIXED_POINT_SERIES_TEXT = (
    "As both the cornerstone of the Modal Triplet Theory",
    "the series is intended to function simultaneously as a basis",
    "Each paper in the series builds upon its predecessors",
)
ABSTRACT_RE = re.compile(
    r"\\begin\{abstract\}(.*?)\\end\{abstract\}",
    re.DOTALL,
)
REVISION_HEADING_RE = re.compile(
    r"\\(?:section|chapter)\*\{"
    r"(?:Revision note[^}]*|Version\s+\d+(?:\.\d+)?\s+Revision Note)"
    r"\}",
    re.IGNORECASE,
)
TEX_MANAGED_BEGIN = "% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE"
TEX_MANAGED_END = "% END MTT MANAGED COMPUTATIONAL EVIDENCE"
MD_MANAGED_BEGIN = "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->"
MD_MANAGED_END = "<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->"


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object: {path}")
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def ready_papers() -> list[tuple[str, dict[str, Any]]]:
    decisions = read_json(DECISIONS).get("papers") or {}
    return sorted(
        (paper_id, decision)
        for paper_id, decision in decisions.items()
        if str(decision.get("status") or "") in READY_STATES
    )


def require_revision_note(paper_id: str, tex: str) -> None:
    abstract_match = ABSTRACT_RE.search(tex)
    assert abstract_match, f"{paper_id}: abstract is missing"
    revision_match = REVISION_HEADING_RE.search(tex)
    assert revision_match, f"{paper_id}: separate revision note is missing"
    assert revision_match.start() > abstract_match.end(), (
        f"{paper_id}: revision note must follow the abstract"
    )

    revision_text = tex[revision_match.start() :]
    labels = re.findall(r"\\item\[([^\]]+)\]", revision_text)
    labels.extend(re.findall(r"\\paragraph\{([^}]+)\}", revision_text))
    normalized = {re.sub(r"[^a-z]+", " ", label.lower()).strip() for label in labels}
    assert any(label.startswith("supersedes") for label in normalized), (
        f"{paper_id}: revision note lacks Supersedes"
    )
    assert any(label.startswith("reason") for label in normalized), (
        f"{paper_id}: revision note lacks Reason"
    )
    assert any(label.startswith("resolution") for label in normalized), (
        f"{paper_id}: revision note lacks Resolution"
    )
    assert any(
        label.startswith("retained result") or label.startswith("retained content")
        for label in normalized
    ), f"{paper_id}: revision note lacks Retained result/content"
    assert any(
        label.startswith("remaining boundary") or label.startswith("open boundary")
        for label in normalized
    ), f"{paper_id}: revision note lacks Remaining/Open boundary"


def require_managed_block_pair(
    paper_id: str,
    text: str,
    begin: str,
    end: str,
    abstract_end: int | None = None,
) -> None:
    begin_count = text.count(begin)
    end_count = text.count(end)
    assert begin_count == end_count, (
        f"{paper_id}: managed evidence markers are unpaired"
    )
    assert begin_count <= 1, (
        f"{paper_id}: managed evidence block is duplicated"
    )
    if begin_count and abstract_end is not None:
        assert text.index(begin) > abstract_end, (
            f"{paper_id}: managed evidence block is inside the abstract"
        )


def require_plain_publication_text(
    paper_id: str,
    field: str,
    value: str,
) -> None:
    assert not TEX_METADATA_RE.search(value), (
        f"{paper_id}: {field} contains TeX markup"
    )
    assert not HTML_TAG_RE.search(value), (
        f"{paper_id}: {field} contains HTML rather than plain text"
    )
    assert not any(
        phrase.casefold() in value.casefold()
        for phrase in FORBIDDEN_FIXED_POINT_SERIES_TEXT
    ), f"{paper_id}: {field} contains forbidden Fixed Points series boilerplate"


def verify_local() -> dict[str, int]:
    ready = ready_papers()
    assert ready, "no papers have a human release review"
    managed_blocks = 0

    for paper_id, decision in ready:
        directory = PAPERS / paper_id
        metadata = read_json(directory / "metadata.json")
        tex_path = directory / str(metadata.get("canonical_tex") or "main.tex")
        md_path = directory / str(metadata.get("canonical_markdown") or "paper.md")
        pdf_path = directory / "main.pdf"
        tex = tex_path.read_text(encoding="utf-8-sig")
        markdown = md_path.read_text(encoding="utf-8-sig")
        abstract_match = ABSTRACT_RE.search(tex)

        title = str(metadata.get("title") or "").strip()
        abstract = str(metadata.get("abstract") or "").strip()
        assert title, f"{paper_id}: metadata title is empty"
        assert abstract, f"{paper_id}: metadata abstract is empty"
        assert not EDITORIAL_TITLE_RE.search(title), (
            f"{paper_id}: edition/correction language is mixed into the title"
        )
        assert not EDITORIAL_ABSTRACT_RE.search(abstract), (
            f"{paper_id}: correction history is mixed into the abstract"
        )
        require_plain_publication_text(
            paper_id,
            "metadata abstract",
            abstract,
        )
        assert abstract_match, f"{paper_id}: TeX abstract is missing"
        assert not EDITORIAL_ABSTRACT_RE.search(abstract_match.group(1)), (
            f"{paper_id}: correction history is mixed into the TeX abstract"
        )
        for phrase in FORBIDDEN_FIXED_POINT_SERIES_TEXT:
            assert phrase.casefold() not in tex.casefold(), (
                f"{paper_id}: paper contains forbidden Fixed Points series boilerplate"
            )
        assert str(metadata.get("current_version") or "").startswith("v"), (
            f"{paper_id}: current version is missing"
        )

        require_revision_note(paper_id, tex)
        require_managed_block_pair(
            paper_id,
            tex,
            TEX_MANAGED_BEGIN,
            TEX_MANAGED_END,
            abstract_match.end(),
        )
        require_managed_block_pair(
            paper_id,
            markdown,
            MD_MANAGED_BEGIN,
            MD_MANAGED_END,
        )
        if TEX_MANAGED_BEGIN in tex:
            managed_blocks += 1

        assert pdf_path.is_file() and pdf_path.stat().st_size > 10_000, (
            f"{paper_id}: canonical PDF is missing or empty"
        )
        source_inputs = [
            path
            for pattern in ("*.tex", "*.sty", "*.bib")
            for path in directory.glob(pattern)
        ]
        newest_source = max(path.stat().st_mtime_ns for path in source_inputs)
        assert pdf_path.stat().st_mtime_ns >= newest_source, (
            f"{paper_id}: PDF is older than a TeX/style/bibliography input"
        )
        assert str(decision.get("reviewed_on") or ""), (
            f"{paper_id}: human review date is missing"
        )
        assert str(decision.get("note") or ""), (
            f"{paper_id}: human review note is missing"
        )
        assert str(decision.get("reviewed_main_tex_sha256") or "") == sha256(
            tex_path
        ), f"{paper_id}: canonical TeX differs from the reviewed artifact"
        assert str(decision.get("reviewed_pdf_sha256") or "") == sha256(
            pdf_path
        ), f"{paper_id}: canonical PDF differs from the reviewed artifact"
        assert (
            str(decision.get("reviewed_source_tree_sha256") or "")
            == str(metadata.get("source_tree_sha256") or "")
        ), f"{paper_id}: source tree differs from the reviewed artifact"

    return {
        "ready_papers": len(ready),
        "managed_evidence_blocks": managed_blocks,
    }


def request_json(
    method: str,
    url: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            value = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise AssertionError(f"{url}: HTTP {error.code}: {detail}") from error
    if not isinstance(value, dict):
        raise AssertionError(f"{url}: expected JSON object")
    return value


def verify_publication_api(base_url: str) -> dict[str, int]:
    base = base_url.rstrip("/")
    ready = ready_papers()
    drafts = 0
    released = 0
    for paper_id, _decision in ready:
        encoded = urllib.parse.quote(paper_id)
        status = request_json(
            "GET",
            f"{base}/api/publications/papers/{encoded}",
        )
        state = str(status.get("publication_state") or "")
        assert state in {"zenodo_draft", "released"}, (
            f"{paper_id}: publication state is {state!r}"
        )
        linked_results = status.get("linked_results") or []
        if linked_results:
            assert status.get("reference_state") == "current", (
                f"{paper_id}: mapped computational results are not "
                "referenced in both TeX and Markdown"
            )
            assert status.get("tex_reference_managed") is True, (
                f"{paper_id}: managed TeX evidence reference is missing"
            )
            assert status.get("markdown_reference_managed") is True, (
                f"{paper_id}: managed Markdown evidence reference is missing"
            )
        if state == "zenodo_draft":
            assert str(status.get("draft_id") or ""), (
                f"{paper_id}: tracked Zenodo draft id is missing"
            )
            drafts += 1
        else:
            released += 1

        metadata = read_json(PAPERS / paper_id / "metadata.json")
        preview = request_json(
            "POST",
            f"{base}/api/publications/papers/{encoded}/preview",
            {
                "calculation_identifier": "",
                "calculation_repository_url": (
                    "https://github.com/PeterNero/mtt-results-repro"
                ),
                "source_repository_url": (
                    "https://github.com/PeterNero/mtt-papers/tree/main/papers/"
                    f"{paper_id}"
                ),
                "title": metadata["title"],
                "description": metadata["abstract"],
                "apply_references": True,
                "upload_pdf": True,
            },
        )
        assert not (preview.get("warnings") or []), (
            f"{paper_id}: Zenodo preview warnings: {preview.get('warnings')}"
        )
        proposed = preview.get("metadata") or {}
        assert not EDITORIAL_TITLE_RE.search(str(proposed.get("title") or "")), (
            f"{paper_id}: Zenodo title mixes correction history"
        )
        assert not EDITORIAL_ABSTRACT_RE.search(
            str(proposed.get("description") or "")
        ), f"{paper_id}: Zenodo description mixes correction history"
        require_plain_publication_text(
            paper_id,
            "Zenodo description",
            str(proposed.get("description") or ""),
        )

    return {
        "zenodo_drafts": drafts,
        "released_current": released,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publication-api", default="")
    args = parser.parse_args()
    try:
        result = verify_local()
        if args.publication_api:
            result.update(verify_publication_api(args.publication_api))
    except Exception as error:
        print(f"paper release verification failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
