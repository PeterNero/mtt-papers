from __future__ import annotations

import argparse
from pathlib import Path
import re

from migrate import (
    build_markdown,
    canonical_hash,
    catalog_markdown,
    load_json,
    pandoc_metadata,
    sha256_file,
    write_json,
)


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
CATALOG_PATH = ROOT / "catalog" / "papers.json"
UNMATCHED_PATH = ROOT / "catalog" / "unmatched-zenodo-records.json"
ZENODO_PATH = ROOT / "catalog" / "zenodo-records.json"
REPORT_PATH = ROOT / "catalog" / "migration-report.json"
CONFIG_PATH = ROOT / "config" / "migration.json"
TEX_MANAGED_BEGIN = "% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE"
MD_MANAGED_BEGIN = "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->"
MD_MANAGED_END = "<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->"
EVIDENCE_HEADING_RE = re.compile(
    r"^(#{1,6}) (?:Computational Evidence and Reproducibility|Reproducibility and Result Ownership)\s*$",
    re.MULTILINE,
)
NEXT_HEADING_RE = re.compile(r"^#{1,6} \S", re.MULTILINE)


def catalog_row(metadata: dict) -> dict:
    return {
        key: value
        for key, value in metadata.items()
        if key not in {"schema", "source_files"}
    }


def restore_managed_markdown_markers(directory: Path, main_tex: Path) -> None:
    tex_text = main_tex.read_text(encoding="utf-8-sig", errors="replace")
    if TEX_MANAGED_BEGIN not in tex_text:
        return
    markdown_path = directory / "paper.md"
    markdown = markdown_path.read_text(encoding="utf-8-sig", errors="replace")
    if MD_MANAGED_BEGIN in markdown:
        return
    heading = EVIDENCE_HEADING_RE.search(markdown)
    if heading is None:
        raise ValueError(
            f"{directory.name}: TeX has managed computational evidence but "
            "the generated Markdown lacks its section"
        )
    next_heading = NEXT_HEADING_RE.search(markdown, heading.end())
    section_end = next_heading.start() if next_heading is not None else len(markdown)
    prefix = markdown[: heading.start()].rstrip()
    section = markdown[heading.start() : section_end].strip()
    suffix = markdown[section_end:].lstrip()
    rebuilt = (
        f"{prefix}\n\n{MD_MANAGED_BEGIN}\n{section}\n{MD_MANAGED_END}\n"
        + (f"\n{suffix}" if suffix else "")
    )
    markdown_path.write_text(rebuilt, encoding="utf-8", newline="\n")


def refresh_one(paper_id: str, *, sync_descriptive_metadata: bool = False) -> dict:
    directory = PAPERS / paper_id
    metadata_path = directory / "metadata.json"
    if not metadata_path.is_file():
        raise FileNotFoundError(f"paper metadata not found: {paper_id}")
    metadata = load_json(metadata_path)
    if sync_descriptive_metadata:
        title, authors, paper_date, abstract = pandoc_metadata(directory)
        if title:
            metadata["title"] = title
        if authors:
            metadata["authors"] = authors
        if paper_date:
            metadata["date"] = paper_date
        if abstract:
            metadata["abstract"] = abstract
    main_tex = directory / str(metadata["canonical_tex"])
    main_hash = sha256_file(main_tex)
    latest = metadata.get("latest_zenodo_release")

    paper_md_hash, warning = build_markdown(
        directory,
        paper_id,
        str(metadata.get("current_version") or ""),
        str(metadata.get("release_state") or ""),
        main_hash,
        latest if isinstance(latest, dict) else None,
        str(metadata.get("date") or ""),
    )
    restore_managed_markdown_markers(directory, main_tex)
    paper_md_hash = sha256_file(directory / "paper.md")

    source_files = []
    for row in metadata["source_files"]:
        relative = Path(str(row["path"]))
        path = directory / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        source_files.append(
            {
                "path": relative.as_posix(),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
        )

    metadata["main_tex_sha256"] = main_hash
    metadata["paper_md_sha256"] = paper_md_hash
    metadata["source_files"] = source_files
    metadata["source_tree_sha256"] = canonical_hash(source_files)
    revision = metadata.get("revision") or {}
    if revision.get("selected_revision"):
        audit = directory / "REVISION_AUDIT.md"
        if not audit.is_file():
            raise FileNotFoundError(audit)
        revision["revision_evidence_sha256"] = sha256_file(audit)
        metadata["revision"] = revision
    write_json(metadata_path, metadata)
    return {
        "paper_id": paper_id,
        "metadata": metadata,
        "pandoc_warning": warning,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Refresh Markdown and canonical hashes without remigrating TeX."
    )
    parser.add_argument("paper_ids", nargs="*")
    parser.add_argument("--all", action="store_true")
    parser.add_argument(
        "--prune-missing",
        action="store_true",
        help="remove catalog rows whose canonical paper directory no longer exists",
    )
    parser.add_argument("--sync-descriptive-metadata", action="store_true")
    args = parser.parse_args()

    if args.all and args.paper_ids:
        parser.error("use either --all or explicit paper ids")
    if args.all:
        paper_ids = sorted(
            path.name
            for path in PAPERS.iterdir()
            if path.is_dir() and (path / "metadata.json").is_file()
        )
    else:
        paper_ids = args.paper_ids
    if not paper_ids and not args.prune_missing:
        parser.error("provide at least one paper id or --all")

    catalog = load_json(CATALOG_PATH)
    catalog_by_id = {
        str(row["paper_id"]): row for row in catalog.get("papers") or []
    }
    removed_release_ids: set[str] = set()
    if args.prune_missing:
        missing_ids = {
            paper_id
            for paper_id in catalog_by_id
            if not (PAPERS / paper_id / "metadata.json").is_file()
        }
        for paper_id in missing_ids:
            row = catalog_by_id.pop(paper_id)
            removed_release_ids.update(
                str(release["id"])
                for release in row.get("zenodo_releases") or []
                if release.get("id") is not None
            )
    warnings = []
    for paper_id in paper_ids:
        result = refresh_one(
            paper_id,
            sync_descriptive_metadata=args.sync_descriptive_metadata,
        )
        catalog_by_id[paper_id] = catalog_row(result["metadata"])
        if result["pandoc_warning"]:
            warnings.append(
                {
                    "paper_id": paper_id,
                    "warning": result["pandoc_warning"],
                }
            )

    catalog["papers"] = sorted(
        catalog_by_id.values(), key=lambda row: str(row["title"]).lower()
    )
    matched_ids = {
        str(release["id"])
        for paper in catalog["papers"]
        for release in paper.get("zenodo_releases") or []
    }
    unmatched_payload = load_json(UNMATCHED_PATH)
    unmatched = [
        row
        for row in unmatched_payload.get("records") or []
        if str(row.get("id") or "") not in matched_ids
        and str(row.get("id") or "") not in removed_release_ids
    ]
    write_json(
        UNMATCHED_PATH,
        {
            "schema": unmatched_payload.get("schema")
            or "mtt.unmatched-zenodo-records.v1",
            "records": unmatched,
        },
    )

    zenodo_payload = load_json(ZENODO_PATH)
    zenodo_records = [
        row
        for row in zenodo_payload.get("records") or []
        if str(row.get("id") or "") not in removed_release_ids
    ]
    write_json(
        ZENODO_PATH,
        {
            **zenodo_payload,
            "records": zenodo_records,
        },
    )
    zenodo_ids = {str(row["id"]) for row in zenodo_records}
    config = load_json(CONFIG_PATH)
    report = load_json(REPORT_PATH)
    report.update(
        {
            "canonical_papers": len(catalog["papers"]),
            "superseded_projects_excluded": len(
                config.get("replacements") or []
            )
            + sum(
                bool(row.get("superseded_project"))
                for row in config.get("native_projects") or []
            ),
            "current_sources_newer_than_release": sum(
                row.get("version_relation") == "current_source_newer_than_release"
                for row in catalog["papers"]
            ),
            "papers_with_zenodo_release": sum(
                bool(row.get("latest_zenodo_release"))
                for row in catalog["papers"]
            ),
            "papers_without_zenodo_match": sum(
                not bool(row.get("latest_zenodo_release"))
                for row in catalog["papers"]
            ),
            "zenodo_records": len(zenodo_ids),
            "zenodo_records_matched": len(matched_ids),
            "zenodo_records_unmatched": len(unmatched),
        }
    )
    catalog["counts"] = report
    write_json(CATALOG_PATH, catalog)
    write_json(REPORT_PATH, report)
    (ROOT / "CATALOG.md").write_text(
        catalog_markdown(catalog["papers"], unmatched),
        encoding="utf-8",
        newline="\n",
    )

    print(f"refreshed {len(paper_ids)} paper artifact sets")
    if warnings:
        print(f"pandoc emitted warnings for {len(warnings)} papers")
        for row in warnings:
            print(f"{row['paper_id']}: {row['warning']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
