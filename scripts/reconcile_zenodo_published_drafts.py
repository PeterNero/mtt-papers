from __future__ import annotations

import argparse
import json
from pathlib import Path
import time
import urllib.error
import urllib.request
from typing import Any

from migrate import (
    catalog_markdown,
    compact_zenodo_record,
    load_json,
    version_relation,
    write_json,
)
from refresh_paper_artifacts import catalog_row, refresh_one


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "papers.json"
ZENODO_PATH = ROOT / "catalog" / "zenodo-records.json"
UNMATCHED_PATH = ROOT / "catalog" / "unmatched-zenodo-records.json"
REPORT_PATH = ROOT / "catalog" / "migration-report.json"


def fetch_public_record(record_id: str) -> dict[str, Any] | None:
    value: Any = None
    for attempt in range(3):
        request = urllib.request.Request(
            f"https://zenodo.org/api/records/{record_id}",
            headers={
                "Accept": "application/json",
                "User-Agent": "mtt-papers-publication-reconciliation/1",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                value = json.load(response)
            break
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            if error.code not in {429, 500, 502, 503, 504}:
                raise
        except TimeoutError:
            pass
        if attempt < 2:
            time.sleep(1 + attempt)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError(f"Zenodo record {record_id} is not an object")
    return compact_zenodo_record(value)


def reconcile(
    ledger_path: Path,
    selected_papers: set[str] | None = None,
) -> dict[str, Any]:
    ledger = load_json(ledger_path)
    catalog = load_json(CATALOG_PATH)
    zenodo = load_json(ZENODO_PATH)
    unmatched = load_json(UNMATCHED_PATH)
    report = load_json(REPORT_PATH)

    catalog_by_id = {
        str(row["paper_id"]): row for row in catalog.get("papers") or []
    }
    records_by_id = {
        str(row["id"]): row for row in zenodo.get("records") or []
    }
    reconciled: list[str] = []
    still_unpublished: list[str] = []

    for paper_id, entry in sorted((ledger.get("papers") or {}).items()):
        if selected_papers and paper_id not in selected_papers:
            continue
        draft_id = str((entry or {}).get("draft_id") or "")
        if not draft_id or paper_id not in catalog_by_id:
            continue
        known_ids = {
            str(row.get("id") or "")
            for row in catalog_by_id[paper_id].get("zenodo_releases") or []
        }
        if draft_id in known_ids:
            continue
        record = fetch_public_record(draft_id)
        if record is None:
            still_unpublished.append(paper_id)
            continue

        record = {
            **record,
            "match_score": 1.0,
            "match_kind": "published_draft_reconciliation",
        }
        metadata_path = ROOT / "papers" / paper_id / "metadata.json"
        metadata = load_json(metadata_path)
        releases_by_id = {
            str(row.get("id") or ""): row
            for row in metadata.get("zenodo_releases") or []
        }
        releases_by_id[draft_id] = record
        releases = sorted(
            releases_by_id.values(),
            key=lambda row: (str(row.get("created") or ""), str(row.get("id") or "")),
            reverse=True,
        )
        latest = releases[0]
        metadata["zenodo_releases"] = releases
        metadata["latest_zenodo_release"] = latest
        metadata["release_state"] = "zenodo_released"
        metadata["version_relation"] = version_relation(
            str(metadata.get("current_version") or ""),
            str(latest.get("version") or ""),
        )
        write_json(metadata_path, metadata)
        refreshed = refresh_one(paper_id)
        catalog_by_id[paper_id] = catalog_row(refreshed["metadata"])
        records_by_id[draft_id] = record
        reconciled.append(paper_id)

    catalog["papers"] = sorted(
        catalog_by_id.values(), key=lambda row: str(row["title"]).lower()
    )
    matched_ids = {
        str(release["id"])
        for paper in catalog["papers"]
        for release in paper.get("zenodo_releases") or []
    }
    unmatched_rows = [
        row
        for row in unmatched.get("records") or []
        if str(row.get("id") or "") not in matched_ids
    ]
    all_records = sorted(
        records_by_id.values(),
        key=lambda row: (str(row.get("created") or ""), str(row.get("id") or "")),
        reverse=True,
    )

    report.update(
        {
            "canonical_papers": len(catalog["papers"]),
            "current_sources_newer_than_release": sum(
                row.get("version_relation") == "current_source_newer_than_release"
                for row in catalog["papers"]
            ),
            "papers_with_zenodo_release": sum(
                bool(row.get("latest_zenodo_release")) for row in catalog["papers"]
            ),
            "papers_without_zenodo_match": sum(
                not bool(row.get("latest_zenodo_release"))
                for row in catalog["papers"]
            ),
            "zenodo_records": len(all_records),
            "zenodo_records_matched": len(matched_ids),
            "zenodo_records_unmatched": len(unmatched_rows),
        }
    )
    catalog["counts"] = report
    write_json(CATALOG_PATH, catalog)
    write_json(
        ZENODO_PATH,
        {
            "schema": "mtt.zenodo-community-records.v1",
            "community": zenodo.get("community") or "mtt",
            "records": all_records,
        },
    )
    write_json(
        UNMATCHED_PATH,
        {
            "schema": "mtt.unmatched-zenodo-records.v1",
            "records": unmatched_rows,
        },
    )
    write_json(REPORT_PATH, report)
    (ROOT / "CATALOG.md").write_text(
        catalog_markdown(catalog["papers"], unmatched_rows),
        encoding="utf-8",
        newline="\n",
    )
    return {
        "reconciled": reconciled,
        "still_unpublished_or_unindexed": still_unpublished,
        "zenodo_records": len(all_records),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Reconcile tracked Zenodo draft ids that have become public records "
            "without rebuilding the canonical paper tree."
        )
    )
    parser.add_argument(
        "--publication-ledger",
        required=True,
        type=Path,
    )
    parser.add_argument("paper_ids", nargs="*")
    args = parser.parse_args()
    result = reconcile(
        args.publication_ledger.resolve(),
        set(args.paper_ids) or None,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
