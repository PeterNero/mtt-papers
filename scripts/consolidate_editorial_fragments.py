"""Consolidate explicitly reviewed editorial fragments without changing result bytes."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from consolidate_research_ownership import lf_hash, reviewed_results

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def write(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

def consolidate(fragment_paths, rebind_papers, result_repo, root=ROOT):
    registry_path = root / "catalog/research-integration-reviews.json"
    registry = read(registry_path)
    manifest = read(result_repo / "release/result_manifest.json")
    fragments = [read(path) for path in fragment_paths]
    new = [row for doc in fragments for row in doc.get("reviews", [])]
    seen = set()
    for row in new:
        for rid in row["result_ids"]:
            if rid in seen:
                raise ValueError(f"overlapping fragment owner review: {rid}")
            seen.add(rid)
    retained, rebound = [], []
    for row in registry["reviews"]:
        ids = [rid for rid in row["result_ids"] if rid not in seen]
        if not ids:
            continue
        row = dict(row, result_ids=ids, result_hashes={rid: row["result_hashes"][rid] for rid in ids})
        actual = lf_hash(root / "papers" / row["paper_id"] / "main.tex")
        if actual != row["main_tex_lf_sha256"]:
            if row["paper_id"] not in rebind_papers:
                raise ValueError(f"prior contextual review needs explicit rebind approval: {row['id']}")
            rebound.append({"review_id": row["id"], "paper_id": row["paper_id"],
                            "previous_hash": row["main_tex_lf_sha256"], "current_hash": actual})
            row["main_tex_lf_sha256"] = actual
            row["context_rechecked_in"] = "editorial-reviews/2026-09-12"
        retained.append(row)
    registry["reviews"] = retained + new
    decisions = reviewed_results(registry, manifest["results"], root)
    if len(decisions) != len(manifest["results"]):
        missing = {r["id"] for r in manifest["results"]} - set(decisions)
        raise ValueError(f"missing contextual owner reviews: {sorted(missing)}")
    bad = {rid: r["stale_reasons"] for rid, r in decisions.items() if r["stale_reasons"]}
    if bad:
        raise ValueError(f"stale fragment reviews: {bad}")
    # The parent-reviewed map is an allowlist; papers may import different
    # explicitly bound subresults from one aggregate Kernel result family.
    source_map = read(root / 'editorial-reviews/2026-09-12/parent-consumers.json')['result_source_map']
    consumers = []
    pairs = set()
    for doc in fragments:
        for key, value in doc.get("result_source_map", doc.get("kernel_result_sources", {})).items():
            value = [value] if isinstance(value, str) else value
            if key not in source_map or not set(value) <= set(source_map[key]):
                raise ValueError(f"conflicting Kernel source mapping: {key}")
        for row in doc.get("consumer_reviews", []):
            for key, value in row.get("kernel_result_sources", {}).items():
                if key not in source_map or not set(value) <= set(source_map[key]):
                    raise ValueError(f"conflicting consumer source mapping: {key}")
            for rid in row["result_ids"]:
                pair = (row["paper_id"], rid)
                if pair in pairs:
                    raise ValueError(f"duplicate consumer placement: {pair}")
                pairs.add(pair)
            consumers.append(row)
    report = {"schema": "mtt.editorial-consolidation.v1", "reviewed_at": "2026-09-12",
              "fragments": [p.relative_to(root).as_posix() for p in fragment_paths],
              "source_snapshot": "f141a20ea23c5c3ff19cc2161c0e226e29ade8a7",
              "owner_results": len(decisions), "consumer_review_groups": len(consumers),
              "consumer_placements": len(pairs), "rebound_prior_reviews": rebound,
              "release_authorized": False, "research_promotion": False}
    write(registry_path, registry)
    write(root / "catalog/research-consumer-reviews.json", {
        "schema": "mtt.research-consumer-reviews.v1",
        "policy": "Per-paper contextual import decisions; not theorem ownership or scientific promotion.",
        "result_source_map": source_map, "reviews": consumers})
    write(root / "editorial-reviews/2026-09-12/consolidation.json", report)
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fragment", action="append", required=True)
    parser.add_argument("--rebind-reviewed-paper", action="append", default=[])
    parser.add_argument("--results-repo", type=Path, required=True)
    args = parser.parse_args()
    report = consolidate([ROOT / p for p in args.fragment], set(args.rebind_reviewed_paper), args.results_repo)
    print(json.dumps({k: v for k, v in report.items() if k != "rebound_prior_reviews"}, indent=2))

if __name__ == "__main__":
    main()
