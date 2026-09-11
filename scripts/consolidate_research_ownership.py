"""Assign current research a paper home without pretending it is already published."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

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


def build(manifest: dict, catalog: dict, result_root: Path) -> dict:
    papers = {p["paper_id"]: p for p in catalog["papers"]}
    rows = []
    for result in manifest["results"]:
        home, reason = owner(result)
        if home not in papers:
            raise ValueError(f"unknown owner paper: {home}")
        path = result_root / result["release_path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != result["sha256"]:
            raise ValueError(f"stale result: {result['id']}")
        tex = (ROOT / "papers" / home / "main.tex").read_text(encoding="utf-8-sig")
        refs = papers[home].get("result_refs", [])
        mentioned = result["id"] in tex or any(str(ref).split("/")[-1] == result["id"] for ref in refs)
        rows.append({
            "result_id": result["id"], "source_repository": result["repo_id"],
            "integration_owner": home, "source_theorem_owner": result.get("authority"),
            "tier": result["tier"], "sha256": result["sha256"],
            "artifact_url": "https://github.com/PeterNero/mtt-results-repro/blob/" + manifest["source_commit"] + "/" + result["release_path"],
            "description": result["description"], "scope": reason,
            "manuscript_integration": "explicit_reference_present_review_context" if mentioned else "contextual_integration_required",
        })
    if len({r["result_id"] for r in rows}) != len(rows):
        raise ValueError("duplicate result assignment")
    return {
        "schema": "mtt.research-paper-ownership.v1", "snapshot_date": "2026-09-11",
        "policy": "Exactly one integration owner per curated result. Source theorem ownership is retained. Assignment and sidecar coverage are not evidence that a theorem is in the TeX or released PDF. No Zenodo changes.",
        "results_commit": manifest["source_commit"],
        "summary": {"results": len(rows), "assigned": len(rows), "unassigned": 0,
                    "papers": len(papers), "owner_papers": len({r["integration_owner"] for r in rows}),
                    "manuscript_integration": dict(Counter(r["manuscript_integration"] for r in rows))},
        "results": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-repo", type=Path, required=True)
    parser.add_argument("--results-commit", required=True)
    args = parser.parse_args()
    manifest = json.loads((args.results_repo / "release/result_manifest.json").read_text())
    manifest["source_commit"] = args.results_commit
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
                          f"Manuscript check: `{row['manuscript_integration']}`. This is an exact-reference scan, not an expository-review verdict.", "",
                          f"[Frozen source artifact]({row['artifact_url']}); SHA-256 `{row['sha256']}`.", ""])
        (ROOT / "papers" / pid / "RESEARCH_INTEGRATION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
