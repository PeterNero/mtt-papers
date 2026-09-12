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
from verify_fp_foundational_dependencies import verify as verify_fp_foundational_dependencies
from consolidate_research_ownership import reviewed_results
from research_consumer_reviews import reviewed_consumers


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_PUBLICATION_TITLES = {
    "the universe has a bad memory",
    "the universe had a bad memory",
}
FORBIDDEN_PUBLIC_PATH_TOKENS = {
    "bad-memory-book",
    "humanvoicepass",
    "the-universe-has-a-bad-memory",
    "the-universe-had-a-bad-memory",
}
TEXT_HASH_SUFFIXES = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".md",
    ".py",
    ".sty",
    ".tex",
    ".txt",
    ".yaml",
    ".yml",
}


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


def sha256_matches(path: Path, expected: str) -> bool:
    raw = path.read_bytes()
    variants = {hashlib.sha256(raw).hexdigest()}
    if path.suffix.lower() in TEXT_HASH_SUFFIXES and b"\x00" not in raw:
        lf = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        crlf = lf.replace(b"\n", b"\r\n")
        variants.add(hashlib.sha256(lf).hexdigest())
        variants.add(hashlib.sha256(crlf).hexdigest())
    return expected in variants


def byte_size_matches(path: Path, expected: int) -> bool:
    raw = path.read_bytes()
    variants = {len(raw)}
    if path.suffix.lower() in TEXT_HASH_SUFFIXES and b"\x00" not in raw:
        lf = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        variants.add(len(lf))
        variants.add(len(lf.replace(b"\n", b"\r\n")))
    return expected in variants


def portable_text_matches(path: Path, portable_files: dict[str, Any]) -> bool:
    relative = path.relative_to(ROOT).as_posix()
    row = portable_files.get(relative)
    if not isinstance(row, dict):
        return False
    raw = path.read_bytes()
    canonical = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return (
        len(canonical) == int(row.get("bytes_lf") or -1)
        and hashlib.sha256(canonical).hexdigest() == row.get("sha256_lf")
    )


def md5_file(path: Path) -> str:
    digest = hashlib.md5()
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
    verify_fp_foundational_dependencies()
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
    portable_hashes = load_json(ROOT / "catalog" / "portable-text-hashes.json")
    assert portable_hashes["schema"] == "mtt.portable-text-hashes.v1"
    portable_files = portable_hashes.get("files") or {}
    papers = catalog.get("papers") or []
    ownership = load_json(ROOT / "catalog/research-ownership.json")
    reviews = load_json(ROOT / "catalog/research-integration-reviews.json")
    result_rows = [{"id": r["result_id"], "repo_id": r["source_repository"], "sha256": r["sha256"]}
                   for r in ownership["results"]]
    decisions = reviewed_results(reviews, result_rows, ROOT)
    consumers = reviewed_consumers(ROOT, ownership)
    for row in ownership["results"]:
        review = decisions.get(row["result_id"])
        assert row.get("contextual_review") == review, f"regenerate ownership: {row['result_id']}"
        assert row["manuscript_integration"] == (review["state"] if review else "unreviewed")
        assert not review or not review["stale_reasons"], f"stale contextual review: {row['result_id']}"
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
    released_pdf_matches = 0
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
        assert metadata["title"].strip().lower() not in FORBIDDEN_PUBLICATION_TITLES
        assert not any(
            token in paper_id.lower() for token in FORBIDDEN_PUBLIC_PATH_TOKENS
        ), paper_id
        assert metadata["result_refs"] == paper["result_refs"]
        assert metadata["result_refs"] == sorted(set(metadata["result_refs"]))
        assert all(
            isinstance(result_id, str) and result_id
            for result_id in metadata["result_refs"]
        )
        assert sha256_matches(
            main_tex, metadata["main_tex_sha256"]
        ) or portable_text_matches(main_tex, portable_files)
        assert sha256_matches(
            markdown, metadata["paper_md_sha256"]
        ) or portable_text_matches(markdown, portable_files)
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
            legacy_identity = sha256_matches(
                path, source_file["sha256"]
            ) and byte_size_matches(path, int(source_file["bytes"]))
            assert legacy_identity or portable_text_matches(path, portable_files)
            if path.suffix.lower() == ".tex":
                tex_files += 1

        revision = metadata["revision"]
        if revision["selected_revision"]:
            selected_revision_ids.add(paper_id)
            audit = directory / "REVISION_AUDIT.md"
            assert audit.is_file(), audit
            assert sha256_matches(
                audit, revision["revision_evidence_sha256"]
            ) or portable_text_matches(audit, portable_files)

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

        latest = paper.get("latest_zenodo_release") or {}
        if paper.get("version_relation") == "matches_latest_release":
            assert latest, paper_id
            pdf_rows = [
                row
                for row in latest.get("files") or []
                if str(row.get("key") or "").lower().endswith(".pdf")
            ]
            assert len(pdf_rows) == 1, (paper_id, pdf_rows)
            local_pdf = directory / "main.pdf"
            assert local_pdf.is_file(), local_pdf
            checksum = str(pdf_rows[0].get("checksum") or "")
            assert checksum.startswith("md5:"), (paper_id, checksum)
            assert md5_file(local_pdf) == checksum.removeprefix("md5:"), paper_id
            assert local_pdf.stat().st_size == int(pdf_rows[0]["size"]), paper_id
            released_pdf_matches += 1

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
    assert not any(
        str(record.get("title") or "").strip().lower()
        in FORBIDDEN_PUBLICATION_TITLES
        for record in zenodo["records"]
    )
    forbidden_paths = [
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and any(token in path.as_posix().lower() for token in FORBIDDEN_PUBLIC_PATH_TOKENS)
    ]
    assert not forbidden_paths, forbidden_paths
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
        "contextual_consumer_reviews": len(consumers),
        "selected_revisions": len(selected_revision_ids),
        "tex_files": tex_files,
        "markdown_bytes": markdown_bytes,
        "zenodo_matched": len(matched_record_ids),
        "zenodo_unmatched": len(unmatched_ids),
        "released_pdf_matches": released_pdf_matches,
        "commercial_book_artifacts": 0,
        "portable_text_hashes": len(portable_files),
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
