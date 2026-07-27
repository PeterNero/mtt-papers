from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object: {path}")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def verify() -> dict[str, int]:
    config = load_json(ROOT / "config" / "migration.json")
    catalog = load_json(ROOT / "catalog" / "papers.json")
    zenodo = load_json(ROOT / "catalog" / "zenodo-records.json")
    unmatched = load_json(ROOT / "catalog" / "unmatched-zenodo-records.json")
    report = load_json(ROOT / "catalog" / "migration-report.json")
    papers = catalog.get("papers") or []
    expected = int(config["expected_canonical_papers"])
    assert len(papers) == expected, (len(papers), expected)

    paper_root = ROOT / "papers"
    directories = sorted(path for path in paper_root.iterdir() if path.is_dir())
    assert len(directories) == expected, len(directories)
    identifiers = [paper["paper_id"] for paper in papers]
    assert len(identifiers) == len(set(identifiers))
    assert {path.name for path in directories} == set(identifiers)

    matched_record_ids: list[str] = []
    selected_revisions = 0
    markdown_bytes = 0
    tex_files = 0
    for paper in papers:
        assert "group" not in paper
        paper_id = paper["paper_id"]
        directory = paper_root / paper_id
        main_tex = directory / paper["canonical_tex"]
        markdown = directory / paper["canonical_markdown"]
        metadata_path = directory / "metadata.json"
        assert main_tex.is_file(), main_tex
        assert markdown.is_file(), markdown
        assert metadata_path.is_file(), metadata_path

        metadata = load_json(metadata_path)
        assert metadata["paper_id"] == paper_id
        assert metadata["title"] == paper["title"]
        assert metadata["main_tex_sha256"] == sha256_file(main_tex)
        assert metadata["paper_md_sha256"] == sha256_file(markdown)
        assert metadata["source_tree_sha256"] == canonical_hash(metadata["source_files"])
        assert metadata["source_provenance"]["legacy_source_path"]
        assert not Path(metadata["source_provenance"]["legacy_source_path"]).is_absolute()

        for source_file in metadata["source_files"]:
            path = directory / source_file["path"]
            assert path.is_file(), path
            assert source_file["sha256"] == sha256_file(path)
            assert source_file["bytes"] == path.stat().st_size
            if path.suffix.lower() == ".tex":
                tex_files += 1

        revision = metadata["revision"]
        if revision["selected_revision"]:
            selected_revisions += 1
            audit = directory / "REVISION_AUDIT.md"
            assert audit.is_file(), audit
            assert revision["revision_evidence_sha256"] == sha256_file(audit)

        markdown_text = markdown.read_text(encoding="utf-8")
        tex_text = main_tex.read_text(encoding="utf-8-sig", errors="replace")
        markdown_bytes += len(markdown_text.encode("utf-8"))
        assert markdown_text.startswith("---\n"), markdown
        assert f"paper_id: {paper_id}" in markdown_text, markdown
        assert "generated_from_main_tex_sha256:" in markdown_text, markdown
        assert len(markdown_text) > 200, markdown
        assert len(markdown_text) / max(1, len(tex_text)) >= 0.45, markdown
        tex_sections = len(
            re.findall(r"\\(?:part|chapter|section|subsection|subsubsection)\*?\{", tex_text)
        )
        markdown_headings = len(re.findall(r"(?m)^#{1,6}\s", markdown_text))
        assert markdown_headings > 0, markdown
        if tex_sections > 3:
            assert markdown_headings >= int(tex_sections * 0.7), (
                paper_id,
                tex_sections,
                markdown_headings,
            )

        for release in paper["zenodo_releases"]:
            matched_record_ids.append(str(release["id"]))
            assert release["record_url"].startswith("https://zenodo.org/records/")

    native_successors = [
        row
        for row in (config.get("native_projects") or [])
        if row.get("superseded_project")
    ]
    native_superseded = {
        str(row["superseded_project"]) for row in native_successors
    }
    terminal_replacements = [
        row
        for row in config["replacements"]
        if str(row["selected_project"]) not in native_superseded
    ]
    expected_selected_revisions = len(terminal_replacements) + len(native_successors)
    assert selected_revisions == expected_selected_revisions, (
        selected_revisions,
        expected_selected_revisions,
    )
    assert len(matched_record_ids) == len(set(matched_record_ids))
    zenodo_ids = {str(record["id"]) for record in zenodo["records"]}
    unmatched_ids = {str(record["id"]) for record in unmatched["records"]}
    assert set(matched_record_ids).isdisjoint(unmatched_ids)
    assert set(matched_record_ids) | unmatched_ids == zenodo_ids
    assert report["canonical_papers"] == expected
    assert report["zenodo_records"] == len(zenodo_ids)
    assert report["zenodo_records_matched"] == len(matched_record_ids)
    assert report["zenodo_records_unmatched"] == len(unmatched_ids)
    expected_lineage_edges = len(config["replacements"]) + len(native_successors)
    assert report["superseded_projects_excluded"] == expected_lineage_edges, (
        report["superseded_projects_excluded"],
        expected_lineage_edges,
    )

    serialized = json.dumps(catalog) + json.dumps(report)
    assert "C:\\\\Users\\\\" not in serialized
    assert "C:/Users/" not in serialized
    assert (ROOT / "CATALOG.md").read_text(encoding="utf-8").count("| [TeX]") == expected
    if unmatched_ids:
        assert "## Zenodo-only records" in (ROOT / "CATALOG.md").read_text(encoding="utf-8")

    return {
        "papers": expected,
        "selected_revisions": selected_revisions,
        "tex_files": tex_files,
        "markdown_bytes": markdown_bytes,
        "zenodo_matched": len(matched_record_ids),
        "zenodo_unmatched": len(unmatched_ids),
    }


def main() -> int:
    try:
        result = verify()
    except Exception as error:
        print(f"verification failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
