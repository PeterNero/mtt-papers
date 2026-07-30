from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import urllib.parse
import urllib.request
from contextlib import contextmanager
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "migration.json"
ZENODO_API = "https://zenodo.org/api/records"
PAPER_ID_MAX_LENGTH = 64
BUILD_SUFFIXES = {
    ".aux",
    ".bbl",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".nav",
    ".out",
    ".snm",
    ".synctex.gz",
    ".toc",
    ".vrb",
}
TEXT_SUFFIXES = {
    ".bib",
    ".bst",
    ".cls",
    ".csv",
    ".json",
    ".md",
    ".sty",
    ".tex",
    ".txt",
    ".tsv",
    ".yaml",
    ".yml",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(rows: Any) -> str:
    payload = json.dumps(
        rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def relative_posix(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def safe_remove_tree(path: Path, parent: Path) -> None:
    resolved = path.resolve()
    root = parent.resolve()
    relative = resolved.relative_to(root)
    if not relative.parts:
        raise ValueError(f"refusing to remove root directory: {resolved}")
    if resolved.exists():
        shutil.rmtree(resolved)


def sync_staged_tree(source: Path, destination: Path, parent: Path) -> None:
    """Mirror a staged tree without replacing the destination directory handle."""
    source_resolved = source.resolve()
    destination_resolved = destination.resolve()
    root = parent.resolve()
    source_resolved.relative_to(root)
    destination_resolved.relative_to(root)
    if source_resolved == root or destination_resolved == root:
        raise ValueError("refusing to synchronize a repository root")

    destination.mkdir(parents=True, exist_ok=True)
    source_files = {
        path.relative_to(source)
        for path in source.rglob("*")
        if path.is_file()
    }
    source_directories = {
        path.relative_to(source)
        for path in source.rglob("*")
        if path.is_dir()
    }

    for destination_file in sorted(destination.rglob("*"), reverse=True):
        if not destination_file.is_file():
            continue
        if destination_file.relative_to(destination) not in source_files:
            destination_file.unlink()

    for destination_directory in sorted(destination.rglob("*"), reverse=True):
        if not destination_directory.is_dir():
            continue
        if destination_directory.relative_to(destination) not in source_directories:
            destination_directory.rmdir()

    for source_directory in sorted(source_directories):
        (destination / source_directory).mkdir(parents=True, exist_ok=True)
    for relative in sorted(source_files):
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, target)

    safe_remove_tree(source, parent)


def install_staging(staging: Path) -> None:
    sync_staged_tree(staging / "papers", REPO_ROOT / "papers", REPO_ROOT)
    destination = REPO_ROOT / "catalog"
    safe_remove_tree(destination, REPO_ROOT)
    (staging / "catalog").replace(destination)
    catalog_destination = REPO_ROOT / "CATALOG.md"
    if catalog_destination.exists():
        catalog_destination.unlink()
    (staging / "CATALOG.md").replace(catalog_destination)
    safe_remove_tree(staging, REPO_ROOT)


def native_projects(config: dict[str, Any]) -> dict[Path, dict[str, Any]]:
    rows: dict[Path, dict[str, Any]] = {}
    for entry in config.get("native_projects") or []:
        project = (REPO_ROOT / entry["path"]).resolve()
        if project in rows:
            raise ValueError(f"duplicate native project path: {project}")
        if not (project / "main.tex").is_file():
            raise FileNotFoundError(f"native project lacks main.tex: {project}")
        rows[project] = entry
    return rows


def discover_projects(source_root: Path, config: dict[str, Any]) -> list[Path]:
    projects: list[Path] = []
    for source_name in config["source_roots"]:
        root = source_root / source_name
        if not root.is_dir():
            raise FileNotFoundError(f"missing configured source root: {root}")
        for lane in ("_work", "revised_tex_vnext"):
            lane_root = root / lane
            if not lane_root.is_dir():
                continue
            projects.extend(
                main.parent for main in sorted(lane_root.glob("*/main.tex"))
            )

    discovered = {relative_posix(path, source_root): path for path in projects}
    replacements = config["replacements"]
    native_rows = list((config.get("native_projects") or []))
    native_superseded = {
        row["superseded_project"]
        for row in native_rows
        if row.get("superseded_project")
    }
    replacement_superseded = {row["superseded_project"] for row in replacements}
    duplicate_superseded = replacement_superseded & native_superseded
    if duplicate_superseded:
        raise ValueError(
            "projects cannot be superseded by both replacement mechanisms: "
            + ", ".join(sorted(duplicate_superseded))
        )
    superseded = replacement_superseded | native_superseded
    selected = {row["selected_project"] for row in replacements}

    missing_old = sorted(superseded - set(discovered))
    missing_new = sorted(selected - set(discovered))
    if missing_old or missing_new:
        raise ValueError(
            "replacement map does not match discovered projects: "
            f"missing_old={missing_old}, missing_new={missing_new}"
        )

    revised_discovered = {
        relative
        for relative in discovered
        if "/revised_tex_vnext/" in f"/{relative}/"
    }
    unregistered_revisions = sorted(revised_discovered - selected)
    if unregistered_revisions:
        raise ValueError(
            "revised projects require explicit lineage entries: "
            + ", ".join(unregistered_revisions)
        )

    canonical = [path for relative, path in discovered.items() if relative not in superseded]
    canonical.extend(native_projects(config))
    expected = int(config["expected_canonical_papers"])
    if len(canonical) != expected:
        raise ValueError(f"expected {expected} canonical papers, found {len(canonical)}")
    native_by_path = native_projects(config)

    def source_key(path: Path) -> str:
        native = native_by_path.get(path.resolve())
        if native:
            return str(native["source_provenance"]).lower()
        return relative_posix(path, source_root).lower()

    return sorted(canonical, key=source_key)


def render_inlines(items: Iterable[dict[str, Any]]) -> str:
    parts: list[str] = []
    for item in items:
        kind = item.get("t")
        content = item.get("c")
        if kind == "Str":
            parts.append(str(content))
        elif kind in {"Space", "SoftBreak", "LineBreak"}:
            parts.append(" ")
        elif kind in {"Emph", "Strong", "Strikeout", "SmallCaps", "Underline"}:
            parts.append(render_inlines(content or []))
        elif kind in {"Superscript", "Subscript"}:
            parts.append(render_inlines(content or []))
        elif kind in {"Code", "Math", "RawInline"} and isinstance(content, list):
            parts.append(str(content[-1]))
        elif kind == "Quoted" and isinstance(content, list):
            parts.append(render_inlines(content[-1]))
        elif kind in {"Link", "Image", "Span"} and isinstance(content, list):
            parts.append(render_inlines(content[-2] if kind in {"Link", "Image"} else content[-1]))
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def render_meta_text(value: dict[str, Any] | None) -> str:
    if not value:
        return ""
    kind = value.get("t")
    content = value.get("c")
    if kind == "MetaString":
        return str(content)
    if kind == "MetaInlines":
        return render_inlines(content or [])
    if kind == "MetaBlocks":
        text_parts: list[str] = []
        for block in content or []:
            block_content = block.get("c")
            if block.get("t") in {"Para", "Plain"}:
                text_parts.append(render_inlines(block_content or []))
        return re.sub(r"\s+", " ", " ".join(text_parts)).strip()
    return ""


def pandoc_source(project: Path) -> str:
    text = (project / "main.tex").read_text(encoding="utf-8-sig", errors="replace")
    lines = []
    for line in text.splitlines():
        if re.match(r"^\s*\\newcolumntype\b", line):
            lines.append("% Conversion-only omission: unsupported Pandoc column declaration.")
        else:
            lines.append(line)
    return "\n".join(lines) + "\n"


@contextmanager
def pandoc_input(project: Path) -> Iterable[str]:
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        suffix=".tex",
        prefix=".mtt-pandoc-",
        dir=project,
        delete=False,
    ) as handle:
        handle.write(pandoc_source(project))
        temporary = Path(handle.name)
    try:
        yield temporary.name
    finally:
        temporary.unlink(missing_ok=True)


def pandoc_metadata(project: Path) -> tuple[str, list[str], str, str]:
    with pandoc_input(project) as source:
        completed = subprocess.run(
            ["pandoc", "--from=latex", "--to=json", source],
            cwd=project,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=90,
            check=False,
        )
    if completed.returncode != 0:
        raise RuntimeError(f"Pandoc metadata failed for {project}: {completed.stderr}")
    payload = json.loads(completed.stdout)
    metadata = payload.get("meta") or {}
    title = render_meta_text(metadata.get("title"))
    date = render_meta_text(metadata.get("date"))
    abstract = render_meta_text(metadata.get("abstract"))
    author_meta = metadata.get("author") or {}
    if author_meta.get("t") == "MetaList":
        authors = [render_meta_text(item) for item in author_meta.get("c") or []]
    else:
        authors = [render_meta_text(author_meta)] if author_meta else []
    return title, [author for author in authors if author], date, abstract


def fallback_title(project_name: str) -> str:
    value = re.sub(r"\s*\(\d+\)\s*$", "", project_name)
    value = re.sub(r"_v\d+(?:[._]\d+)*$", "", value, flags=re.IGNORECASE)
    value = value.replace("___", " - ").replace("__", ": ").replace("_", " ")
    return re.sub(r"\s+", " ", value).strip()


def project_version(project_name: str) -> str:
    matches = re.findall(r"(?:^|_)v(\d+(?:[._]\d+)*)", project_name, re.IGNORECASE)
    if not matches:
        return ""
    return "v" + matches[-1].replace("_", ".")


def version_tuple(value: str) -> tuple[int, ...] | None:
    numbers = re.findall(r"\d+", value or "")
    if not numbers:
        return None
    parsed = [int(number) for number in numbers]
    while len(parsed) > 1 and parsed[-1] == 0:
        parsed.pop()
    return tuple(parsed)


def version_relation(current: str, released: str) -> str:
    current_value = version_tuple(current)
    released_value = version_tuple(released)
    if not current_value or not released_value:
        return "unknown"
    width = max(len(current_value), len(released_value))
    left = current_value + (0,) * (width - len(current_value))
    right = released_value + (0,) * (width - len(released_value))
    if left == right:
        return "matches_latest_release"
    if left > right:
        return "current_source_newer_than_release"
    return "release_newer_than_current_source"


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title)
    ascii_title = "".join(character for character in normalized if not unicodedata.combining(character))
    value = re.sub(r"[^A-Za-z0-9]+", "-", ascii_title).strip("-").lower()
    if not value:
        value = "paper"
    if len(value) > PAPER_ID_MAX_LENGTH:
        suffix = hashlib.sha1(title.encode("utf-8")).hexdigest()[:8]
        prefix_length = PAPER_ID_MAX_LENGTH - len(suffix) - 1
        value = value[:prefix_length].rstrip("-") + "-" + suffix
    return value


def normalize_title(value: str) -> str:
    value = html.unescape(value or "")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(character for character in value if not unicodedata.combining(character))
    value = value.lower().replace("–", "-").replace("—", "-")
    value = re.sub(r"\s+v\d+(?:\.\d+)*\s*$", "", value)
    value = re.sub(r"\s*\(\d+\)\s*$", "", value)
    return " ".join(re.findall(r"[a-z0-9]+", value))


def compact_zenodo_record(record: dict[str, Any]) -> dict[str, Any]:
    metadata = record.get("metadata") or {}
    creators = []
    for creator in metadata.get("creators") or []:
        person = creator.get("person_or_org") or creator
        name = person.get("name") or creator.get("name")
        if name:
            creators.append(name)
    files = []
    for item in record.get("files") or []:
        links = item.get("links") or {}
        files.append(
            {
                "key": item.get("key") or "",
                "size": item.get("size") or 0,
                "content_url": links.get("content") or links.get("self") or "",
                "checksum": item.get("checksum") or "",
            }
        )
    record_id = str(record.get("id") or "")
    links = record.get("links") or {}
    return {
        "id": record_id,
        "title": metadata.get("title") or "",
        "version": metadata.get("version") or "",
        "doi": record.get("doi") or metadata.get("doi") or "",
        "concept_doi": record.get("conceptdoi") or "",
        "publication_date": metadata.get("publication_date") or "",
        "created": record.get("created") or "",
        "updated": record.get("updated") or "",
        "resource_type": (metadata.get("resource_type") or {}).get("type") or "",
        "creators": creators,
        "record_url": links.get("self_html") or f"https://zenodo.org/records/{record_id}",
        "files": files,
    }


def fetch_zenodo_records(community: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    page = 1
    total = None
    while total is None or len(rows) < total:
        query = urllib.parse.urlencode(
            {
                "q": f"communities:{community}",
                "sort": "mostrecent",
                "size": 25,
                "page": page,
            }
        )
        request = urllib.request.Request(
            f"{ZENODO_API}?{query}",
            headers={"Accept": "application/json", "User-Agent": "mtt-papers-migration/1"},
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.load(response)
        hits = payload.get("hits") or {}
        total_value = hits.get("total")
        if isinstance(total_value, dict):
            total_value = total_value.get("value")
        total = int(total_value or 0)
        page_rows = hits.get("hits") or []
        if not page_rows:
            break
        rows.extend(compact_zenodo_record(row) for row in page_rows)
        page += 1
    return sorted(rows, key=lambda row: (row["created"], row["id"]), reverse=True)


def zenodo_aliases(record: dict[str, Any]) -> list[str]:
    values = [record["title"]]
    for item in record.get("files") or []:
        key = Path(item.get("key") or "").stem
        key = re.sub(r"_v\d+(?:[._]\d+)*\s*(?:\(\d+\))?$", "", key, flags=re.IGNORECASE)
        values.append(key.replace("_", " "))
    return [normalized for value in values if (normalized := normalize_title(value))]


def alias_score(left: str, right: str) -> float:
    if left == right:
        return 1.0
    sequence = SequenceMatcher(None, left, right).ratio()
    left_tokens = set(left.split())
    right_tokens = set(right.split())
    union = left_tokens | right_tokens
    jaccard = len(left_tokens & right_tokens) / len(union) if union else 0.0
    return max(sequence, jaccard)


def match_zenodo_records(
    papers: list[dict[str, Any]],
    records: list[dict[str, Any]],
    overrides: dict[str, str],
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    by_id = {paper["paper_id"]: paper for paper in papers}
    by_source = {paper["legacy_source_path"]: paper for paper in papers}
    matches: dict[str, list[dict[str, Any]]] = {paper["paper_id"]: [] for paper in papers}
    unmatched: list[dict[str, Any]] = []

    for record in records:
        override = overrides.get(str(record["id"]))
        if override:
            paper = by_id.get(override) or by_source.get(override)
            if not paper:
                raise ValueError(f"unknown Zenodo override target {override} for {record['id']}")
            matches[paper["paper_id"]].append({**record, "match_score": 1.0, "match_kind": "override"})
            continue

        record_names = zenodo_aliases(record)
        ranked: list[tuple[float, dict[str, Any]]] = []
        for paper in papers:
            score = max(
                alias_score(record_name, paper_alias)
                for record_name in record_names
                for paper_alias in paper["normalized_aliases"]
            )
            ranked.append((score, paper))
        ranked.sort(key=lambda item: (item[0], item[1]["paper_id"]), reverse=True)
        best_score, best_paper = ranked[0]
        second_score = ranked[1][0]
        exact = best_score == 1.0
        if best_score >= 0.88 and (exact or best_score - second_score >= 0.025):
            matches[best_paper["paper_id"]].append(
                {**record, "match_score": round(best_score, 6), "match_kind": "title_or_file"}
            )
        else:
            unmatched.append(
                {
                    **record,
                    "best_candidate": best_paper["paper_id"],
                    "best_score": round(best_score, 6),
                    "second_score": round(second_score, 6),
                }
            )

    for rows in matches.values():
        rows.sort(key=lambda row: (row["created"], row["id"]), reverse=True)
    return matches, unmatched


def should_copy(path: Path) -> bool:
    if any(part in {".git", "__pycache__"} or part.startswith("_minted-") for part in path.parts):
        return False
    lower_name = path.name.lower()
    return not any(lower_name.endswith(suffix) for suffix in BUILD_SUFFIXES)


def copy_canonical_file(source: Path, destination: Path) -> None:
    payload = source.read_bytes()
    if source.suffix.lower() in TEXT_SUFFIXES:
        payload = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    destination.write_bytes(payload)


def copy_project(
    source: Path, target: Path, *, exclude_generated: bool = False
) -> list[dict[str, Any]]:
    target.mkdir(parents=True, exist_ok=True)
    files: list[dict[str, Any]] = []
    for source_file in sorted(source.rglob("*")):
        if not source_file.is_file():
            continue
        relative = source_file.relative_to(source)
        if exclude_generated and relative.as_posix() in {
            "metadata.json",
            "paper.md",
        }:
            continue
        if not should_copy(relative):
            continue
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        copy_canonical_file(source_file, destination)
        files.append(
            {
                "path": relative.as_posix(),
                "sha256": sha256_file(destination),
                "bytes": destination.stat().st_size,
            }
        )
    if not (target / "main.tex").is_file():
        raise FileNotFoundError(f"copied project lacks main.tex: {target}")
    return files


def build_markdown(
    project: Path,
    paper_id: str,
    current_version: str,
    release_state: str,
    main_hash: str,
    latest_release: dict[str, Any] | None,
    date_override: str = "",
) -> tuple[str, str]:
    command = [
        "pandoc",
        "--from=latex",
        "--to=gfm",
        "--standalone",
        "--wrap=none",
        "-M",
        f"paper_id={paper_id}",
        "-M",
        f"current_version={current_version}",
        "-M",
        f"release_state={release_state}",
        "-M",
        f"generated_from_main_tex_sha256={main_hash}",
    ]
    if date_override:
        command.extend(["-M", f"date={date_override}"])
    if latest_release:
        command.extend(
            [
                "-M",
                f"zenodo_record_id={latest_release['id']}",
                "-M",
                f"zenodo_doi={latest_release['doi']}",
                "-M",
                f"released_version={latest_release['version']}",
                "-M",
                f"zenodo_url={latest_release['record_url']}",
            ]
        )
    with pandoc_input(project) as source:
        completed = subprocess.run(
            [*command, source],
            cwd=project,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            check=False,
        )
    if completed.returncode != 0:
        raise RuntimeError(f"Pandoc Markdown failed for {project}: {completed.stderr}")
    if len(completed.stdout.strip()) < 200:
        raise ValueError(f"implausibly short Markdown conversion: {project}")
    markdown = "\n".join(
        line.rstrip() for line in completed.stdout.splitlines()
    ) + "\n"
    (project / "paper.md").write_text(
        markdown, encoding="utf-8", newline="\n"
    )
    return sha256_file(project / "paper.md"), completed.stderr.strip()


def prepare_paper_records(
    projects: list[Path],
    source_root: Path,
    config: dict[str, Any],
    prior_papers: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    replacement_by_selected = {
        row["selected_project"]: row for row in config["replacements"]
    }
    papers: list[dict[str, Any]] = []
    used_ids: set[str] = set()
    native_by_path = native_projects(config)
    prior_by_id = {str(row.get("paper_id") or ""): row for row in prior_papers}
    for project in projects:
        native = native_by_path.get(project.resolve())
        source_path = (
            str(native["source_provenance"])
            if native
            else relative_posix(project, source_root)
        )
        title, authors, date, abstract = pandoc_metadata(project)
        title = str(native.get("title") or title) if native else title
        title = title or fallback_title(project.name)
        authors = list(native.get("authors") or authors) if native else authors
        date = str(native.get("date") or date) if native else date
        abstract = str(native.get("abstract") or abstract) if native else abstract
        replacement = replacement_by_selected.get(source_path) if not native else None
        result_source = native if native else (replacement or {})
        result_refs = sorted(
            {
                str(item)
                for item in result_source.get("result_refs") or []
                if str(item)
            }
        )
        configured_paper_id = replacement.get("paper_id") if replacement else None
        paper_id = (
            str(native.get("paper_id") or slugify(title))
            if native
            else str(configured_paper_id or slugify(title))
        )
        if paper_id in used_ids:
            suffix = hashlib.sha1(source_path.encode("utf-8")).hexdigest()[:8]
            prefix_length = PAPER_ID_MAX_LENGTH - len(suffix) - 1
            paper_id = paper_id[:prefix_length].rstrip("-") + "-" + suffix
        used_ids.add(paper_id)

        source_text = (project / "main.tex").read_text(
            encoding="utf-8-sig", errors="replace"
        )
        dynamic_date = bool(
            re.search(r"\\date\s*\{\s*\\today\s*\}", source_text)
        )
        if dynamic_date:
            prior = prior_by_id.get(paper_id)
            if prior and prior.get("date"):
                date = str(prior["date"])

        aliases = [title, fallback_title(project.name)]
        if native and native.get("superseded_project"):
            replacement = {
                "superseded_project": native["superseded_project"],
                "revision_evidence": str(
                    native.get("revision_evidence") or "REVISION_AUDIT.md"
                ),
                "native_successor": True,
            }
        if replacement:
            old_project = source_root / replacement["superseded_project"]
            old_title, _, _, _ = pandoc_metadata(old_project)
            aliases.extend([old_title, fallback_title(old_project.name)])

        normalized_aliases = sorted(
            {normalized for alias in aliases if alias and (normalized := normalize_title(alias))}
        )
        papers.append(
            {
                "paper_id": paper_id,
                "title": title,
                "authors": authors,
                "date": date,
                "abstract": abstract,
                "result_refs": result_refs,
                "current_version": (
                    str(native.get("current_version") or project_version(project.name))
                    if native
                    else project_version(project.name)
                ),
                "legacy_source_path": source_path,
                "normalized_aliases": normalized_aliases,
                "replacement": replacement,
                "project": project,
                "native": bool(native),
                "dynamic_date": dynamic_date,
            }
        )
    return papers


def catalog_markdown(
    papers: list[dict[str, Any]], unmatched_zenodo: list[dict[str, Any]]
) -> str:
    released = sum(paper["release_state"] == "zenodo_released" for paper in papers)
    newer = sum(
        paper["version_relation"] == "current_source_newer_than_release"
        for paper in papers
    )
    lines = [
        "# MTT Paper Catalog",
        "",
        f"Canonical papers: **{len(papers)}**. Zenodo-linked papers: **{released}**. "
        f"Current sources newer than their latest release: **{newer}**.",
        "",
        "The list is alphabetical and intentionally has no topical grouping.",
        "",
        "| Paper | Current | Public release | Sources |",
        "| --- | --- | --- | --- |",
    ]
    for paper in sorted(papers, key=lambda row: row["title"].lower()):
        title = paper["title"].replace("|", "\\|")
        current = paper["current_version"] or "unversioned"
        latest = paper.get("latest_zenodo_release")
        if latest:
            release = f"[{latest['version'] or 'released'}]({latest['record_url']})"
        else:
            release = "not matched"
        paper_id = paper["paper_id"]
        lines.append(
            f"| {title} | {current} | {release} | "
            f"[TeX](papers/{paper_id}/main.tex) / [Markdown](papers/{paper_id}/paper.md) |"
        )
    if unmatched_zenodo:
        lines.extend(
            [
                "",
                "## Zenodo-only records",
                "",
                "These public records have no matching local TeX project and are not "
                "represented as canonical source papers:",
                "",
            ]
        )
        for record in sorted(unmatched_zenodo, key=lambda row: row["title"].lower()):
            version = record["version"] or "released"
            lines.append(
                f"- [{record['title']}]({record['record_url']}) ({version}, DOI {record['doi']})"
            )
    return "\n".join(lines) + "\n"


def migrate(args: argparse.Namespace) -> dict[str, Any]:
    source_root = args.source_root.resolve()
    config = load_json(CONFIG_PATH)
    projects = discover_projects(source_root, config)
    prior_catalog_path = REPO_ROOT / "catalog" / "papers.json"
    prior_papers = (
        load_json(prior_catalog_path).get("papers") or []
        if prior_catalog_path.is_file()
        else []
    )
    papers = prepare_paper_records(projects, source_root, config, prior_papers)

    zenodo_cache = REPO_ROOT / "catalog" / "zenodo-records.json"
    if args.refresh_zenodo or not zenodo_cache.is_file():
        zenodo_records = fetch_zenodo_records(args.zenodo_community)
    else:
        zenodo_records = load_json(zenodo_cache).get("records") or []
    matches, unmatched_zenodo = match_zenodo_records(
        papers,
        zenodo_records,
        {str(key): value for key, value in (config.get("zenodo_record_overrides") or {}).items()},
    )

    staging = REPO_ROOT / ".import-staging"
    safe_remove_tree(staging, REPO_ROOT)
    staged_papers = staging / "papers"
    staged_catalog = staging / "catalog"
    staged_papers.mkdir(parents=True)
    staged_catalog.mkdir(parents=True)

    output_papers: list[dict[str, Any]] = []
    pandoc_warnings: list[dict[str, str]] = []
    for paper in papers:
        paper_id = paper["paper_id"]
        target = staged_papers / paper_id
        source_files = copy_project(
            paper["project"], target, exclude_generated=paper["native"]
        )
        main_hash = sha256_file(target / "main.tex")
        releases = matches[paper_id]
        latest = releases[0] if releases else None
        current_version = (
            paper["current_version"]
            or (latest["version"] if latest else "")
            or "unversioned"
        )
        release_state = "zenodo_released" if latest else "not_matched_to_zenodo"

        replacement = paper["replacement"]
        revision: dict[str, Any] = {"selected_revision": bool(replacement)}
        if replacement:
            if replacement.get("native_successor"):
                evidence = paper["project"] / replacement["revision_evidence"]
                evidence_path = (
                    Path("papers") / paper_id / replacement["revision_evidence"]
                ).as_posix()
            else:
                evidence = source_root / replacement["revision_evidence"]
                evidence_path = replacement["revision_evidence"]
            revision_target = target / "REVISION_AUDIT.md"
            copy_canonical_file(evidence, revision_target)
            revision.update(
                {
                    "superseded_source_path": replacement["superseded_project"],
                    "revision_evidence_path": evidence_path,
                    "revision_evidence_sha256": sha256_file(revision_target),
                }
            )

        markdown_hash, warnings = build_markdown(
            target,
            paper_id,
            current_version,
            release_state,
            main_hash,
            latest,
            paper["date"] if paper["dynamic_date"] else "",
        )
        if warnings:
            pandoc_warnings.append({"paper_id": paper_id, "warnings": warnings})

        release_relation = version_relation(
            current_version, latest["version"] if latest else ""
        )
        metadata = {
            "schema": "mtt.paper.v1",
            "paper_id": paper_id,
            "title": paper["title"],
            "authors": paper["authors"],
            "date": paper["date"],
            "abstract": paper["abstract"],
            "result_refs": paper["result_refs"],
            "current_version": current_version,
            "canonical_tex": "main.tex",
            "canonical_markdown": "paper.md",
            "main_tex_sha256": main_hash,
            "paper_md_sha256": markdown_hash,
            "source_tree_sha256": canonical_hash(source_files),
            "source_files": source_files,
            "source_provenance": {
                "legacy_source_path": paper["legacy_source_path"]
            },
            "revision": revision,
            "release_state": release_state,
            "version_relation": release_relation,
            "latest_zenodo_release": latest,
            "zenodo_releases": releases,
        }
        write_json(target / "metadata.json", metadata)
        output_papers.append(
            {
                key: metadata[key]
                for key in (
                    "paper_id",
                    "title",
                    "authors",
                    "date",
                    "abstract",
                    "result_refs",
                    "current_version",
                    "canonical_tex",
                    "canonical_markdown",
                    "main_tex_sha256",
                    "paper_md_sha256",
                    "source_tree_sha256",
                    "source_provenance",
                    "revision",
                    "release_state",
                    "version_relation",
                    "latest_zenodo_release",
                    "zenodo_releases",
                )
            }
        )

    output_papers.sort(key=lambda row: row["title"].lower())
    matched_record_ids = {
        release["id"]
        for paper in output_papers
        for release in paper["zenodo_releases"]
    }
    report = {
        "schema": "mtt.paper-migration-report.v1",
        "canonical_papers": len(output_papers),
        "superseded_projects_excluded": len(config["replacements"])
        + sum(
            bool(row.get("superseded_project"))
            for row in (config.get("native_projects") or [])
        ),
        "zenodo_records": len(zenodo_records),
        "zenodo_records_matched": len(matched_record_ids),
        "zenodo_records_unmatched": len(unmatched_zenodo),
        "papers_with_zenodo_release": sum(
            paper["release_state"] == "zenodo_released" for paper in output_papers
        ),
        "papers_without_zenodo_match": sum(
            paper["release_state"] != "zenodo_released" for paper in output_papers
        ),
        "current_sources_newer_than_release": sum(
            paper["version_relation"] == "current_source_newer_than_release"
            for paper in output_papers
        ),
        "pandoc_warning_papers": len(pandoc_warnings),
    }
    write_json(
        staged_catalog / "papers.json",
        {
            "schema": "mtt.paper-catalog.v1",
            "counts": report,
            "papers": output_papers,
        },
    )
    write_json(
        staged_catalog / "zenodo-records.json",
        {
            "schema": "mtt.zenodo-community-records.v1",
            "community": args.zenodo_community,
            "records": zenodo_records,
        },
    )
    write_json(
        staged_catalog / "unmatched-zenodo-records.json",
        {
            "schema": "mtt.unmatched-zenodo-records.v1",
            "records": unmatched_zenodo,
        },
    )
    write_json(staged_catalog / "migration-report.json", report)
    write_json(
        staged_catalog / "pandoc-warnings.json",
        {"schema": "mtt.pandoc-warnings.v1", "papers": pandoc_warnings},
    )
    (staging / "CATALOG.md").write_text(
        catalog_markdown(output_papers, unmatched_zenodo),
        encoding="utf-8",
        newline="\n",
    )

    install_staging(staging)
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the flat canonical MTT paper store")
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--zenodo-community", default="mtt")
    parser.add_argument("--refresh-zenodo", action="store_true")
    return parser.parse_args()


def main() -> int:
    try:
        report = migrate(parse_args())
    except Exception as error:
        print(f"migration failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
