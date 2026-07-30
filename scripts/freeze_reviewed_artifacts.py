from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
DECISIONS = ROOT / "catalog" / "expository-review-decisions.json"
READY_STATES = {"reviewed", "reference_ready"}


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Freeze the exact TeX, PDF, and source-tree hashes already "
            "approved by an expository review decision."
        )
    )
    parser.add_argument("--paper-id", action="append", default=[])
    args = parser.parse_args()

    document = read_json(DECISIONS)
    decisions = document.get("papers") or {}
    selected = set(args.paper_id)
    if selected:
        missing = sorted(selected - set(decisions))
        if missing:
            raise ValueError(
                "paper lacks an expository review decision: "
                + ", ".join(missing)
            )

    frozen = 0
    for paper_id, decision in decisions.items():
        if str((decision or {}).get("status") or "") not in READY_STATES:
            continue
        if selected and paper_id not in selected:
            continue
        directory = PAPERS / paper_id
        metadata = read_json(directory / "metadata.json")
        tex = directory / str(metadata.get("canonical_tex") or "main.tex")
        pdf = directory / "main.pdf"
        if not tex.is_file() or not pdf.is_file():
            raise FileNotFoundError(f"{paper_id}: TeX or PDF is missing")
        source_inputs = [
            path
            for pattern in ("*.tex", "*.sty", "*.bib")
            for path in directory.glob(pattern)
        ]
        if pdf.stat().st_mtime_ns < max(
            path.stat().st_mtime_ns for path in source_inputs
        ):
            raise ValueError(f"{paper_id}: PDF is older than a source input")
        source_tree = str(metadata.get("source_tree_sha256") or "")
        if not source_tree:
            raise ValueError(f"{paper_id}: source-tree hash is missing")
        decision["reviewed_main_tex_sha256"] = sha256(tex)
        decision["reviewed_pdf_sha256"] = sha256(pdf)
        decision["reviewed_source_tree_sha256"] = source_tree
        frozen += 1

    DECISIONS.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"frozen_reviewed_papers": frozen}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
