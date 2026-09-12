"""Assign current research a paper home without pretending it is already published."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SM = "modal-triplet-theory-from-mtt-to-standard-model-a-rigor-923ad6b1"
FLUX = "flux-compactifications-in-heterotic-string-theory-expli-08b38155"
HS = "modal-triplet-theory-from-mtt-to-the-strominger-heterot-b2789a83"
COH = "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"
QM = "modal-triplet-theory-from-mtt-to-quantum-mechanics"
QG = "modal-triplet-theory-perturbative-coherent-sector-quant-eb63e01d"
FP3 = "fixed-points-iii-disturbance-damping-balance-and-stability"
PROTO = "the-proto-spinor-conditional-spinorial-closure-and-the-973217d8"
PARAM = "modal-triplet-theory-parameters-closure-and-structural-ae734bf0"
ACTION = "closure-geometry-and-a-regime-local-ten-dimensional-act-97095538"
STOCH = "modal-triplet-theory-from-mtt-to-indivisible-stochastic-449ca9a6"
GRAPHS = "modal-diagrammatics-the-origin-of-feynman-rules-from-co-79b757d8"

FAMILY_OWNER = {
    "sm_closure": SM, "q79": FLUX, "qa_su3": HS,
    "constants": PARAM, "individual_constants": PARAM,
    "protospinor_gr": "closure-strain-geometry-local-normal-forms-and-conditio-b62ade60",
    "protospinor_sim": PROTO, "qm_source": QM, "qg_current": QG,
    "math_closure": COH, "eta9_current": FLUX, "eta9_source_lock": FLUX,
    "unified_source": HS, "preprojection_repair": COH,
    "beq_external": STOCH, "q79_total_superconnection": PROTO,
    "q79_mirror_current": QG, "unified_source_g3gms": COH,
    "causal_base_constraint_fiber": COH, "eta9_three_cycle_current": FLUX,
    "fixed_points_frontier_20260911": FP3,
}

REVIEW_STATES = {"integrated", "summary_present", "addition_needed", "historical_context"}


def lf_hash(path: Path) -> str:
    raw = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(raw).hexdigest()


def reviewed_results(document: dict, results: list[dict], root: Path) -> dict:
    """A text hit is discovery; only a source-bound contextual review is a decision."""
    sources = {r["id"]: r for r in results}
    reviewed = {}
    for group in document.get("reviews", []):
        if group["state"] not in REVIEW_STATES or not group.get("assessment"):
            raise ValueError(f"invalid contextual review: {group['id']}")
        if not group.get("reviewed_at") or not group.get("reviewer"):
            raise ValueError(f"unattributed contextual review: {group['id']}")
        path = root / "papers" / group["paper_id"] / "main.tex"
        raw = path.read_text(encoding="utf-8-sig")
        stale = []
        if lf_hash(path) != group.get("main_tex_lf_sha256"):
            stale.append("manuscript changed")
        anchors = group.get("anchors", [])
        if not anchors or any(anchor not in raw for anchor in anchors):
            stale.append("review location missing")
        locations = [{"source_ref": path.relative_to(root).as_posix(),
                      "line_start": raw[:raw.index(anchor)].count("\n") + 1,
                      "anchor": anchor} for anchor in anchors if anchor in raw]
        for key in group["result_ids"]:
            if key not in sources or key in reviewed:
                raise ValueError(f"unknown or duplicate reviewed result: {key}")
            if owner(sources[key])[0] != group["paper_id"]:
                raise ValueError(f"review is not for integration owner: {key}")
            reasons = list(stale)
            if sources[key]["sha256"] != group.get("result_hashes", {}).get(key):
                reasons.append("result artifact changed")
            reviewed[key] = {
                "id": group["id"], "state": "review_stale" if reasons else group["state"],
                "reviewed_at": group["reviewed_at"], "reviewer": group["reviewer"],
                "assessment": group["assessment"], "locations": locations,
                "remaining_action": group.get("remaining_action", ""),
                "main_tex_lf_sha256": group.get("main_tex_lf_sha256"),
                "result_sha256": group.get("result_hashes", {}).get(key),
                "stale_reasons": reasons,
            }
    return reviewed


def owner(result: dict) -> tuple[str, str]:
    key, repo = result["id"], result["repo_id"]
    if "eta9" in key and repo not in {"fixed_points_frontier_20260911"}:
        return FLUX, "Selected-source topology and transport; finite-fiber and global classes remain distinct."
    if any(word in key for word in ("recorder", "record_descent", "fock_output")):
        return "why-the-born-rule-and-the-classical-limit-are-the-same-a68ca872", "Operational record measure at its declared apparatus tier."
    if "ontology" in key:
        return "locality-coherent-alternatives-and-records-in-mtt", "Interpretive consumer of the source non-entailment theorem, not a new ontology proof."
    if any(word in key for word in ("graph_functor", "repair_jet")):
        return GRAPHS, "Repair jets supply conditional perturbative data, not interacting continuum existence."
    if any(word in key for word in ("cyclic", "multiplier_lift", "variational_anchor")) and repo != "beq_external":
        return ACTION, "Action construction and normalization contract; physical action selection remains separate."
    if "hidden" in key or "hym_chamber" in key:
        return HS, "Preserve closed hidden existence/stability tiers; do not infer the common physical endpoint."
    if repo not in FAMILY_OWNER:
        raise ValueError(f"unassigned result family: {repo}/{key}")
    return FAMILY_OWNER[repo], "Preserve the artifact's exact tier and guards; paper ownership does not promote a source claim."


def build(manifest: dict, catalog: dict, result_root: Path, *, root: Path = ROOT,
          reviews: dict | None = None) -> dict:
    papers = {p["paper_id"]: p for p in catalog["papers"]}
    if reviews is None:
        review_path = root / "catalog/research-integration-reviews.json"
        reviews = json.loads(review_path.read_text()) if review_path.is_file() else {}
    decisions = reviewed_results(reviews, manifest["results"], root)
    rows = []
    for result in manifest["results"]:
        home, reason = owner(result)
        if home not in papers:
            raise ValueError(f"unknown owner paper: {home}")
        path = result_root / result["release_path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != result["sha256"]:
            raise ValueError(f"stale result: {result['id']}")
        tex = (root / "papers" / home / "main.tex").read_text(encoding="utf-8-sig")
        refs = papers[home].get("result_refs", [])
        in_tex = result["id"] in tex
        in_metadata = any(str(ref).split("/")[-1] == result["id"] for ref in refs)
        review = decisions.get(result["id"])
        rows.append({
            "result_id": result["id"], "source_repository": result["repo_id"],
            "integration_owner": home, "source_theorem_owner": result.get("authority"),
            "tier": result["tier"], "sha256": result["sha256"],
            "artifact_url": "https://github.com/PeterNero/mtt-results-repro/blob/" + manifest["source_commit"] + "/" + result["release_path"],
            "description": result["description"], "scope": reason,
            "reference_scan": {"tex": in_tex, "metadata": in_metadata},
            "manuscript_integration": review["state"] if review else "unreviewed",
            "contextual_review": review,
        })
    if len({r["result_id"] for r in rows}) != len(rows):
        raise ValueError("duplicate result assignment")
    return {
        "schema": "mtt.research-paper-ownership.v2", "snapshot_date": "2026-09-12",
        "policy": "Exactly one integration owner per curated result. Unreviewed is not missing. An ID hit is not contextual integration. Reviewed decisions bind the manuscript and result hashes and become stale on change. Integration at the declared tier is not physical-source promotion or release approval.",
        "results_commit": manifest["source_commit"],
        "summary": {"results": len(rows), "assigned": len(rows), "unassigned": 0,
                    "papers": len(papers), "owner_papers": len({r["integration_owner"] for r in rows}),
                    "manuscript_integration": dict(Counter(r["manuscript_integration"] for r in rows)),
                    "reference_scan": {"tex_hits": sum(r["reference_scan"]["tex"] for r in rows),
                                       "metadata_hits": sum(r["reference_scan"]["metadata"] for r in rows)}},
        "results": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-repo", type=Path, required=True)
    parser.add_argument("--results-commit", required=True)
    args = parser.parse_args()
    commit = subprocess.check_output(
        ["git", "-C", str(args.results_repo), "rev-parse", f"{args.results_commit}^{{commit}}"], text=True
    ).strip()
    manifest = json.loads(subprocess.check_output(
        ["git", "-C", str(args.results_repo), "show", f"{commit}:release/result_manifest.json"]
    ))
    manifest["source_commit"] = commit
    catalog = json.loads((ROOT / "catalog/papers.json").read_text(encoding="utf-8-sig"))
    payload = build(manifest, catalog, args.results_repo)
    (ROOT / "catalog/research-ownership.json").write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    for paper in catalog["papers"]:
        pid = paper["paper_id"]
        selected = [r for r in payload["results"] if r["integration_owner"] == pid]
        lines = ["# Research Integration Record", "", paper["title"], "",
                 "This companion records the current research assigned to this paper. It is not part of the released PDF, not a new theorem, and not a release approval.", "",
                 "Read the canonical TeX, REVISION_AUDIT.md and the Kernel completion ledger together. Retain each result's assumptions; cite its original theorem rather than duplicating proofs.", ""]
        if not selected:
            lines.append("No additional primary result is assigned in this curated snapshot. Existing references and the paper-specific completion ledger still apply; this does not certify universal completeness.")
        for row in selected:
            lines.extend([f"## {row['result_id']}", "", f"Tier: `{row['tier']}`.", "", row["description"], "", row["scope"], "",
                          f"Contextual integration: `{row['manuscript_integration']}`.", "",
                          f"Literal identifier scan: TeX={row['reference_scan']['tex']}, metadata={row['reference_scan']['metadata']}. A missing identifier is not proof of missing mathematics.", "",
                          f"[Frozen source artifact]({row['artifact_url']}); SHA-256 `{row['sha256']}`.", ""])
            review = row.get("contextual_review")
            if review:
                lines.extend([f"Reviewed {review['reviewed_at']}: {review['assessment']}", ""])
                for location in review["locations"]:
                    lines.append(f"- `main.tex:{location['line_start']}`: `{location['anchor']}`")
                lines.extend(["", f"Remaining: {review['remaining_action'] or 'Preserve the reviewed scope; no new integration action.'}", ""])
                if review["stale_reasons"]:
                    lines.extend(["Review invalidated: " + "; ".join(review["stale_reasons"]), ""])
        (ROOT / "papers" / pid / "RESEARCH_INTEGRATION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
