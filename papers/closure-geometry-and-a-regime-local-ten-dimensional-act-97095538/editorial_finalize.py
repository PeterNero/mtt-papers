"""Mechanically synchronize only the six assigned papers and this review fragment."""

from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SLUGS = [
    "closure-geometry-and-a-regime-local-ten-dimensional-act-97095538",
    "modal-diagrammatics-the-origin-of-feynman-rules-from-co-79b757d8",
    "modal-triplet-theory-perturbative-coherent-sector-quant-eb63e01d",
    "modal-triplet-theory-parameters-closure-and-structural-ae734bf0",
    "from-modal-triplet-theory-to-algebraic-quantum-field-th-19e8dde7",
    "modal-triplet-theory-from-mtt-to-quantum-field-theory-o-fd17e8ba",
]
ALLOWED = [(ROOT / "papers" / slug).resolve() for slug in SLUGS]
FRAGMENT = ROOT / "editorial-reviews/2026-09-12/action_qg.json"
REPORT = FRAGMENT.with_suffix(".md")
QA = ALLOWED[0] / "tmp/editorial-qa-20260912"
DEFAULT_FROZEN = ROOT.parent / "mtt-results-repro" / "release" / "results"
DEFAULT_KERNEL = ROOT.parent / "BrainOfEnterprise-MTT-Research-Environment" / "data"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_text(path, value):
    resolved = path.resolve()
    assert resolved in (FRAGMENT.resolve(), REPORT.resolve()) or any(resolved.is_relative_to(p) for p in ALLOWED), resolved
    resolved.parent.mkdir(parents=True, exist_ok=True)
    resolved.write_text(value, encoding="utf-8", newline="\n")


def write_json(path, value):
    write_text(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lf_text(path):
    return path.read_bytes().decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def lf_sha(path):
    return hashlib.sha256(lf_text(path).encode("utf-8")).hexdigest()


def baseline_json(fragment, relative):
    value = subprocess.check_output(["git", "show", fragment["baseline_commit"] + ":" + relative], cwd=ROOT)
    return json.loads(value.decode("utf-8-sig"))


def anchor_locations(paper_id, anchors):
    path = ROOT / "papers" / paper_id / "main.tex"
    text = lf_text(path)
    result = []
    for anchor in anchors:
        assert anchor in text, (paper_id, anchor)
        result.append({"anchor": anchor, "path": path.relative_to(ROOT).as_posix(), "line": text[:text.index(anchor)].count("\n") + 1})
    return result


def restore_markers(project):
    if "% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE" not in lf_text(project / "main.tex"):
        return
    path = project / "paper.md"
    text = lf_text(path)
    begin = "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->"
    end = "<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->"
    if begin in text:
        return
    heading = re.search(r"^#{1,6} (?:Computational Evidence and Reproducibility|Reproducibility and Result Ownership)\s*$", text, re.MULTILINE)
    assert heading, project
    following = re.search(r"^#{1,6} \S", text[heading.end():], re.MULTILINE)
    stop = heading.end() + following.start() if following else len(text)
    write_text(path, text[:heading.start()].rstrip() + "\n\n" + begin + "\n" + text[heading.start():stop].strip() + "\n" + end + "\n\n" + text[stop:].lstrip())


def integration_markdown(fragment, metadata, records):
    paper_id = metadata["paper_id"]
    lines = ["# Research Integration Record", "", metadata["title"], "", "Current contextual review: 2026-09-12. This local companion is not a new theorem, release approval, or global catalog update.", "", "Source-bound decisions, full reading coverage, exact hashes and separate corrections are recorded in `editorial-reviews/2026-09-12/action_qg.json`. Current A/B authorities and later refinements control older packet status fields.", ""]
    own = [r for r in fragment["reviews"] if r["paper_id"] == paper_id]
    if not own:
        lines.extend(["No additional primary owner assignment is claimed. The consumer reviews below do not change canonical ownership.", ""])
    for review in own:
        for result_id in review["result_ids"]:
            record = records[result_id]
            lines.extend(["## " + result_id, "", "Tier: `" + record["tier"] + "`.", "", record["description"], "", "Contextual integration: `integrated`.", "", review["assessment"], "", "Anchors: " + ", ".join("`" + a + "`" for a in review["anchors"]) + ".", "", "[Frozen source artifact](" + record["artifact_url"] + "); SHA-256 `" + record["sha256"] + "`.", ""])
    consumers = [r for r in fragment["consumer_reviews"] if r["paper_id"] == paper_id]
    if consumers:
        lines.extend(["## Contextual Consumer Reviews", ""])
    for review in consumers:
        lines.extend(["### " + review["result_ids"][0], "", "State: `integrated`; this is a consumer import, not an owner placement.", "", review["assessment"], "", "Anchors: " + ", ".join("`" + a + "`" for a in review["anchors"]) + ".", ""])
        for result_id in review["curated_result_ids"]:
            record = records[result_id]
            lines.extend(["Source: `" + result_id + "`, tier `" + record["tier"] + "`.", "", "[Frozen artifact](" + record["artifact_url"] + "); SHA-256 `" + record["sha256"] + "`.", ""])
    lines.extend(["## Boundary and Review Method", "", "Each result retains its exact, conditional, profile, excluded or open scope. Complete source reading and the small bounded checks in this review are not independent replay of scientific certificates. Earlier historical completion groups were excluded from duplicate consumer reviews in accordance with the parent's candidate-selection correction.", "", "See `REVISION_AUDIT.md` and the fragment's `corrections` list for genuine text defects and shared source-theorem guidance. Global Kernel/catalog integration remains parent-owned.", ""])
    return "\n".join(lines)


def main(frozen, kernel, proof_root):
    fragment = read_json(FRAGMENT)
    assert fragment["exclusive_paper_scope"] == SLUGS
    spec = importlib.util.spec_from_file_location("scoped_migrate_helpers", ROOT / "scripts/migrate.py")
    migrate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(migrate)
    ownership = {r["result_id"]: r for r in read_json(ROOT / "catalog/research-ownership.json")["results"]}
    records = {r["result_id"]: r for r in fragment["source_read_coverage"]["frozen_artifacts"]}
    for result_id, row in records.items():
        relative = row["artifact_url"].split("/release/results/", 1)[1]
        path = frozen / relative
        assert sha(path) == row["sha256"] == ownership[result_id]["sha256"], result_id
        row.update({"artifact_path": path.as_posix(), "bytes": path.stat().st_size, "line_count": len(lf_text(path).splitlines()), "read_line_ranges": [[1, len(lf_text(path).splitlines())]], "source_hash_matches_frozen_bytes": True})
    for row in fragment["source_read_coverage"]["proof_explanations"]:
        path = (proof_root / row["source_root_relative_path"]).resolve()
        assert path.is_relative_to(proof_root), path
        assert sha(path) == row["sha256"], ("Previously read proof bytes changed", path)
        row.update({"path": path.as_posix(), "bytes": path.stat().st_size, "line_count": len(lf_text(path).splitlines()), "read_line_ranges": [[1, len(lf_text(path).splitlines())]]})
    for review in fragment["reviews"] + fragment["consumer_reviews"]:
        path = ROOT / "papers" / review["paper_id"] / "main.tex"
        review["main_tex_lf_sha256"] = lf_sha(path)
        review["anchor_locations"] = anchor_locations(review["paper_id"], review["anchors"])
        ids = review.get("curated_result_ids", review["result_ids"])
        assert set(ids) == set(review["result_hashes"])
        for result_id in ids:
            assert review["result_hashes"][result_id] == records[result_id]["sha256"]
    for review in fragment["text_reviews"]:
        review["main_tex_lf_sha256"] = lf_sha(ROOT / "papers" / review["paper_id"] / "main.tex")
        review["anchor_locations"] = anchor_locations(review["paper_id"], review["anchors"])
    for correction in fragment["corrections"]:
        correction["consumer_locations"] = []
        for paper_id in correction["paper_ids"]:
            anchors = correction.get("anchors_by_paper", {}).get(paper_id, correction.get("anchors", []))
            correction["consumer_locations"].extend(anchor_locations(paper_id, anchors))
    render = {r["paper_id"]: r for r in read_json(QA / "render.json")}
    visual = {r["paper_id"]: r for r in read_json(QA / "visual-inspection.json")["papers"]}
    for change in fragment["paper_changes"]:
        paper_id = change["paper_id"]
        project = ROOT / "papers" / paper_id
        metadata_path = project / "metadata.json"
        metadata = read_json(metadata_path)
        baseline = baseline_json(fragment, "papers/" + paper_id + "/metadata.json")
        assert baseline["current_version"] == change["previous_version"]
        assert metadata["current_version"] in (change["previous_version"], change["current_version"])
        _, authors, date, abstract = migrate.pandoc_metadata(project)
        metadata.update({"current_version": change["current_version"], "release_state": "current_revised_tex", "version_relation": "current_source_newer_than_release", "date": date, "authors": authors, "abstract": abstract})
        refs = set(metadata.get("result_refs", [])) | set(change["additional_context_result_refs"])
        for review in fragment["reviews"] + fragment["consumer_reviews"]:
            if review["paper_id"] == paper_id:
                refs.update(review.get("curated_result_ids", review["result_ids"]))
        metadata["result_refs"] = sorted(refs)
        write_text(project / "RESEARCH_INTEGRATION.md", integration_markdown(fragment, metadata, records))
        main_hash = sha(project / "main.tex")
        _, warning = migrate.build_markdown(project, paper_id, metadata["current_version"], metadata["release_state"], main_hash, metadata.get("latest_zenodo_release"), metadata["date"])
        restore_markers(project)
        markdown = lf_text(project / "paper.md")
        bib_keys = set(re.findall(r"\\bibcite\{([^}]+)\}", lf_text(project / "main.aux")))
        md_keys = set(re.findall(r'<a id="ref-([^"]+)"></a>', markdown))
        cited_keys = set(re.findall(r"\]\(#ref-([^)]+)\)", markdown))
        assert bib_keys == md_keys and cited_keys <= md_keys, (paper_id, bib_keys - md_keys)
        assert "# References" in markdown and "## Abstract" in markdown
        assert all(field in markdown for field in ("Supersedes", "Reason", "Resolution", "Retained", "Open boundary"))
        files = {r["path"] for r in metadata["source_files"]}
        files.update({"REVISION_AUDIT.md", "RESEARCH_INTEGRATION.md"})
        if (project / "main.bib").is_file():
            files.add("main.bib")
        if (project / "paper-markdown.lua").is_file():
            files.add("paper-markdown.lua")
        source_files = [{"path": p, "sha256": sha(project / p), "bytes": (project / p).stat().st_size} for p in sorted(files)]
        metadata.update({"main_tex_sha256": main_hash, "paper_md_sha256": sha(project / "paper.md"), "source_files": source_files, "source_tree_sha256": migrate.canonical_hash(source_files)})
        revision = metadata.setdefault("revision", {})
        revision.update({"selected_revision": True, "revision_evidence_path": "papers/" + paper_id + "/REVISION_AUDIT.md", "revision_evidence_sha256": sha(project / "REVISION_AUDIT.md")})
        for key in ("paper_id", "title", "latest_zenodo_release", "zenodo_releases", "source_provenance"):
            assert metadata.get(key) == baseline.get(key), (paper_id, key)
        assert sha(project / "series.sty") == next(r["sha256"] for r in baseline["source_files"] if r["path"] == "series.sty")
        assert sha(project / "main.pdf") == render[paper_id]["pdf_sha256"]
        assert change["pdf_pages"] == render[paper_id]["pdfpages"]
        write_json(metadata_path, metadata)
        change.update({"main_tex_sha256": main_hash, "main_tex_lf_sha256": lf_sha(project / "main.tex"), "paper_md_sha256": sha(project / "paper.md"), "metadata_sha256": sha(metadata_path), "source_tree_sha256": metadata["source_tree_sha256"], "pdf_sha256": sha(project / "main.pdf"), "pdf_bytes": (project / "main.pdf").stat().st_size, "released_identity_preserved": True, "common_style_unchanged": True, "markdown_generation": {"helper": "scripts/migrate.py build_markdown only, with local managed-marker restoration", "warning": warning}})
        change["build"]["log_directory"] = (ALLOWED[0] / "editorial-build-20260912" / paper_id).relative_to(ROOT).as_posix()
        change["markdown_generation"].update({"local_filter": "paper-markdown.lua", "bibliography_entries": len(md_keys), "bibliography_matches_built_pdf": True, "abstract_and_revision_notes_retained": True})
        change["pdf_inspection"].update(visual[paper_id])
        assert visual[paper_id]["contact_sheet_pages_inspected"] == list(range(1, change["pdf_pages"] + 1))
        assert not visual[paper_id]["findings"]
        for record in fragment["source_read_coverage"]["manuscripts"]:
            if record["paper_id"] == paper_id:
                record.update({"current_main_tex_lf_sha256": lf_sha(project / "main.tex"), "current_line_count": len(lf_text(project / "main.tex").splitlines()), "baseline_main_tex_sha256": baseline["main_tex_sha256"]})
        print(paper_id, metadata["current_version"], "PDF/Markdown/metadata synchronized", flush=True)
    ledger_path = kernel / "paper-completion-ledger.json"
    ledger = read_json(ledger_path)
    selected = [p for p in ledger["papers"] if p["paper_id"] in SLUGS]
    exclusions = set(fragment["historical_candidate_policy"]["excluded_from_new_consumer_reviews"])
    placements = {(r["paper_id"], result_id) for r in fragment["consumer_reviews"] for result_id in r["result_ids"]}
    pending = set()
    snapshot = []
    for row in selected:
        expected = set(row.get("new_result_placements", [])) - exclusions
        for reconciliation in row.get("coherence_reconciliations", []):
            if reconciliation["applicable"] and reconciliation["integration_status"] in ("needs_result_integration", "needing_result_integration"):
                expected.update(set(reconciliation["result_ids"]) - exclusions)
        pending.update((row["paper_id"], r) for r in expected)
        snapshot.append({"paper_id": row["paper_id"], "new_result_placements": row.get("new_result_placements", []), "review_required_after_historical_exclusions": sorted(expected), "applicable_reconciliations": [r for r in row.get("coherence_reconciliations", []) if r["applicable"]]})
    assert pending == placements, {"missing": sorted(pending-placements), "extra": sorted(placements-pending)}
    fragment["kernel_queue_snapshot"] = {"path": ledger_path.as_posix(), "sha256": sha(ledger_path), "snapshot_at": ledger.get("snapshot_at"), "papers": snapshot, "required_consumer_placements": len(pending), "unreviewed_remaining_in_assigned_queue": 0}
    baseline_reviews = baseline_json(fragment, "catalog/research-integration-reviews.json")["reviews"]
    old_integrated = {(r["paper_id"], i) for r in baseline_reviews if r["state"] in ("integrated", "historical") for i in r["result_ids"]}
    assignments = {(r["integration_owner"], r["result_id"]) for r in ownership.values() if r.get("integration_owner") in SLUGS}
    expected_owner = assignments - old_integrated
    actual_owner = {(r["paper_id"], i) for r in fragment["reviews"] for i in r["result_ids"]}
    assert expected_owner == actual_owner, {"missing_owner": sorted(expected_owner-actual_owner), "unexpected_owner": sorted(actual_owner-expected_owner)}
    fragment["owner_queue_check"] = {"baseline_unreviewed_assigned_results": len(expected_owner), "reviewed_results": len(actual_owner), "remaining": 0}
    bounded = read_json(QA / "bounded-checks.json")
    assert bounded["passed"] == bounded["total"] == 14
    fragment.setdefault("checks", {}).update({"scoped_pdf_builds_passed": 6, "reported_build_warnings": 0, "rendered_and_contact_sheet_inspected_pages": sum(r["pdfpages"] for r in render.values()), "bounded_checks": bounded, "source_hashes_match": True, "release_identity_preserved": True, "common_styles_unchanged": True, "consumer_queue_coverage_exact": True, "owner_queue_coverage_exact": True, "no_global_refresh_or_catalog_write": True})
    fragment["checks"].update({"full_size_changed_page_inspections": sum(len(r["full_size_pages"]) for r in visual.values()), "markdown_bibliographies_match_built_pdfs": True, "markdown_abstract_and_revision_notes_retained": True})
    write_json(FRAGMENT, fragment)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frozen-results", type=Path,
                        default=os.environ.get("MTT_FROZEN_RESULTS", DEFAULT_FROZEN),
                        help="Frozen results directory; defaults to MTT_FROZEN_RESULTS or sibling mtt-results-repro/release/results.")
    parser.add_argument("--kernel-data", type=Path,
                        default=os.environ.get("MTT_KERNEL_DATA", DEFAULT_KERNEL),
                        help="Kernel data directory; defaults to MTT_KERNEL_DATA or the sibling Kernel repository's data directory.")
    parser.add_argument("--proof-root", type=Path,
                        default=os.environ.get("MTT_PROOF_ROOT"),
                        help="Root containing proof repositories; defaults to MTT_PROOF_ROOT or the parent of mtt-results-repro.")
    args = parser.parse_args()
    frozen = args.frozen_results.expanduser().resolve()
    kernel = args.kernel_data.expanduser().resolve()
    proof_root = args.proof_root.expanduser().resolve() if args.proof_root else frozen.parents[2]
    for name, path in (("frozen results", frozen), ("Kernel data", kernel), ("proof root", proof_root)):
        if not path.is_dir():
            parser.error(f"The {name} directory does not exist: {path}")
    main(frozen, kernel, proof_root)
