from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
import re
from typing import Any

from audit_expository_readability import audit as audit_expository_readability
from verify_book_interpretive_role import verify as verify_book_interpretive_role
from verify_paper_release_requirements import verify_local as verify_paper_release_requirements
from verify_theorem_ownership import verify as verify_theorem_ownership


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
    book = verify_book_interpretive_role()
    release_requirements = verify_paper_release_requirements()
    readability_rows, forbidden_boilerplate = audit_expository_readability()
    assert not forbidden_boilerplate, forbidden_boilerplate
    theorem_results, global_duplicate_groups = verify_theorem_ownership()
    config = load_json(ROOT / "config" / "migration.json")
    catalog = load_json(ROOT / "catalog" / "papers.json")
    zenodo = load_json(ROOT / "catalog" / "zenodo-records.json")
    unmatched = load_json(ROOT / "catalog" / "unmatched-zenodo-records.json")
    report = load_json(ROOT / "catalog" / "migration-report.json")
    review_decisions = load_json(
        ROOT / "catalog" / "expository-review-decisions.json"
    )
    papers = catalog.get("papers") or []
    expected = int(config["expected_canonical_papers"])
    assert len(papers) == expected, (len(papers), expected)
    assert len(readability_rows) == expected, (
        len(readability_rows),
        expected,
    )
    assert (ROOT / "EXPOSITORY_READABILITY_POLICY.md").is_file()
    assert (ROOT / "PAPER_RELEASE_REQUIREMENTS.md").is_file()
    readability_report = load_json(
        ROOT / "catalog" / "expository-readability.json"
    )
    assert readability_report["papers"] == expected
    assert not readability_report["forbidden_boilerplate_hits"]
    replacement_result_refs = {
        str(row["selected_project"]): sorted(
            {str(item) for item in row.get("result_refs") or [] if str(item)}
        )
        for row in config["replacements"]
        if row.get("result_refs")
    }

    paper_root = ROOT / "papers"
    directories = sorted(path for path in paper_root.iterdir() if path.is_dir())
    assert len(directories) == expected, len(directories)
    identifiers = [paper["paper_id"] for paper in papers]
    assert len(identifiers) == len(set(identifiers))
    assert {path.name for path in directories} == set(identifiers)

    matched_record_ids: list[str] = []
    selected_revision_ids: set[str] = set()
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
        assert metadata["result_refs"] == paper["result_refs"]
        assert metadata["result_refs"] == sorted(set(metadata["result_refs"]))
        assert all(
            isinstance(result_id, str) and result_id
            for result_id in metadata["result_refs"]
        )
        assert metadata["main_tex_sha256"] == sha256_file(main_tex)
        assert metadata["paper_md_sha256"] == sha256_file(markdown)
        assert metadata["source_tree_sha256"] == canonical_hash(metadata["source_files"])
        assert metadata["source_provenance"]["legacy_source_path"]
        assert not Path(metadata["source_provenance"]["legacy_source_path"]).is_absolute()
        expected_replacement_refs = replacement_result_refs.get(
            metadata["source_provenance"]["legacy_source_path"]
        )
        if expected_replacement_refs is not None:
            assert metadata["result_refs"] == expected_replacement_refs

        for source_file in metadata["source_files"]:
            path = directory / source_file["path"]
            assert path.is_file(), path
            assert source_file["sha256"] == sha256_file(path)
            assert source_file["bytes"] == path.stat().st_size
            if path.suffix.lower() == ".tex":
                tex_files += 1

        revision = metadata["revision"]
        if revision["selected_revision"]:
            selected_revision_ids.add(paper_id)
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
    release_ready_ids = {
        str(paper_id)
        for paper_id, decision in (
            review_decisions.get("papers") or {}
        ).items()
        if str((decision or {}).get("status") or "")
        in {"reviewed", "reference_ready"}
    }
    assert selected_revision_ids == release_ready_ids, (
        sorted(selected_revision_ids - release_ready_ids),
        sorted(release_ready_ids - selected_revision_ids),
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
        "selected_revisions": len(selected_revision_ids),
        "tex_files": tex_files,
        "markdown_bytes": markdown_bytes,
        "zenodo_matched": len(matched_record_ids),
        "zenodo_unmatched": len(unmatched_ids),
        "theorem_results_in_release_scope": theorem_results,
        "global_duplicate_theorem_groups": global_duplicate_groups,
        "book_words": book["words"],
        "book_chapters": book["chapters"],
        "book_display_math": book["display_math"],
        "papers_in_expository_audit": len(readability_rows),
        "forbidden_series_boilerplate_hits": len(forbidden_boilerplate),
        "release_ready_papers": release_requirements["ready_papers"],
        "managed_evidence_blocks": release_requirements[
            "managed_evidence_blocks"
        ],
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
