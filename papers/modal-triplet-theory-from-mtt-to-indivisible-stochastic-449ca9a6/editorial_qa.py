"""Bounded editorial checks and PDF contact sheets; no scientific replay."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
SLUG = Path(__file__).resolve().parent.name
WAVE = "wave-particle-duality-as-projection-duality-in-modal-tr-785c9af8"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--papers-repo", type=Path,
        default=os.environ.get("MTT_PAPERS_REPO", ROOT),
        help="Papers repository (MTT_PAPERS_REPO; defaults to this helper's repository).",
    )
    parser.add_argument(
        "--results-repo", type=Path, default=os.environ.get("MTT_RESULTS_REPO"),
        help="Frozen results repository (MTT_RESULTS_REPO; defaults to ../mtt-results-repro relative to the papers repository).",
    )
    parser.add_argument(
        "--pdftoppm", default=os.environ.get("PDFTOPPM"),
        help="Poppler pdftoppm executable (PDFTOPPM; otherwise discovered on PATH).",
    )
    return parser.parse_args(argv)


def resolve_paths(args: argparse.Namespace) -> tuple[Path, Path, str]:
    root = args.papers_repo.expanduser().resolve()
    results_repo = (args.results_repo or root.parent / "mtt-results-repro").expanduser().resolve()
    if not (root / "catalog/research-ownership.json").is_file():
        raise ValueError("Papers repository lacks catalog/research-ownership.json; set --papers-repo or MTT_PAPERS_REPO.")
    results = results_repo / "release/results"
    if not results.is_dir():
        raise ValueError("Frozen results repository lacks release/results; set --results-repo or MTT_RESULTS_REPO.")
    pdftoppm = shutil.which(args.pdftoppm or "pdftoppm")
    if pdftoppm is None:
        raise ValueError("pdftoppm was not found; install Poppler on PATH or set --pdftoppm / PDFTOPPM to its executable.")
    return root, results, pdftoppm


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bounded_checks() -> dict:
    b = np.array([[-1, -1, 0], [0, 1, -1], [1, 0, 1]], dtype=object)
    c = np.array([-1, 1, 1], dtype=object)
    p = np.outer(c, c) * F(1, 3)
    checks = {
        "route_cycle_annihilated": bool(np.all(b @ c == 0)),
        "route_projector_idempotent": bool(np.all(p @ p == p)),
        "normalized_route_hodge": bool(np.all((b.T @ b) * F(1, 3) == np.eye(3, dtype=int) - p)),
        "cycle_witness_one": (c @ p @ c) * F(1, 3) == 1,
        "incoherent_witness_one_third": sum(p[i, i] for i in range(3)) * F(1, 3) == F(1, 3),
        "all_plus_witness_one_ninth": sum(p.flat) * F(1, 3) == F(1, 9),
        "canonical_output_normalization": F(1, 448) + F(149, 448) + F(149, 224) == 1,
        "phase_holonomy_intersection": {F(k, 7) for k in range(7)} & {F(k, 64) for k in range(64)} == {F(0)},
        "external_anchor_not_z64": F(18, 360) * 64 == F(16, 5),
    }
    rates = [F(1, 4), F(1, 2), F(3, 4)]
    amps = [F(1), F(1), -F(1, 5)]
    y = [sum(a * r**n for a, r in zip(amps, rates)) for n in range(5)]
    h = [[y[i + j] for j in range(3)] for i in range(3)]
    det = sum(h[0][i] * (h[1][(i + 1) % 3] * h[2][(i + 2) % 3] - h[1][(i + 2) % 3] * h[2][(i + 1) % 3]) for i in range(3))
    checks["signed_hankel_small_minor_zero"] = y[0] * y[2] == y[1] ** 2
    checks["signed_hankel_rank_three_witness"] = det == -F(1, 5120)
    # A physical-metric Hodge semigroup need not contract in transported norm.
    e = np.array([[1.0, 1.0], [1.0, 2.0]])
    lap = np.array([[1.0, 1.0], [0.0, 0.0]])
    heat = np.eye(2) + (np.exp(-1.0) - 1.0) * lap
    norm = float(np.linalg.norm(heat, 2))
    checks["different_metric_not_common_contraction"] = norm > 1.0 and np.allclose(e @ lap, lap.T @ e)
    checks["metric_distortion_bounds_heat"] = norm <= float(np.sqrt(np.linalg.cond(e)))
    if not all(checks.values()):
        raise AssertionError(checks)
    return {"checks": checks, "count": len(checks), "different_metric_heat_norm": norm,
            "scope": "Small exact rational examples and one 2x2 norm check; no source scientific reruns."}


def inspect_paper(paper_id: str, ownership: dict, root: Path, results: Path, pdftoppm: str) -> dict:
    directory = root / "papers" / paper_id
    qa = directory / "editorial-qa"
    render = qa / "pages"
    render.mkdir(parents=True, exist_ok=True)
    tex = (directory / "main.tex").read_text(encoding="utf-8")
    meta = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
    refs = {r["result_id"]: r for r in ownership["results"]}
    for result_id in meta["result_refs"]:
        row = refs[result_id]
        suffix = row["artifact_url"].rsplit("/", 1)[-1]
        assert digest((results / result_id / suffix).read_bytes()) == row["sha256"], result_id
    cited = {k.strip() for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", tex) for k in group.split(",")}
    bib = (directory / "main.bib").read_text(encoding="utf-8") if (directory / "main.bib").exists() else ""
    defined = set(re.findall(r"@\w+\{([^,]+),", bib)) | set(re.findall(r"\\bibitem\{([^}]+)\}", tex))
    assert not (cited - defined), cited - defined
    if paper_id == SLUG:
        assert {f"beq{i:02d}" for i in range(1, 49)} <= cited
    pdf = directory / "main.pdf"
    reader = PdfReader(pdf)
    page_texts = [page.extract_text() or "" for page in reader.pages]
    assert all(t.strip() for t in page_texts), "Empty PDF page"
    assert "Foundations of X" not in str(reader.metadata.title), "Inherited wrong PDF title"
    subprocess.run([pdftoppm, "-r", "100", "-png", str(pdf), str(render / "page")], check=True)
    images = sorted(render.glob("page-*.png"))
    assert len(images) == len(reader.pages)
    sheets = []
    for offset in range(0, len(images), 4):
        sheet = Image.new("RGB", (1200, 1740), "#c9c9c9")
        draw = ImageDraw.Draw(sheet)
        for j, image_path in enumerate(images[offset:offset + 4]):
            with Image.open(image_path) as source:
                page = source.convert("RGB")
            page.thumbnail((584, 828))
            x, y0 = 8 + (j % 2) * 600, 25 + (j // 2) * 870
            sheet.paste(page, (x, y0))
            draw.text((x, y0 - 18), f"Page {offset + j + 1}", fill="black")
        sheet_path = qa / f"contact-{offset // 4 + 1:02d}.png"
        sheet.save(sheet_path)
        sheets.append(str(sheet_path))
    report = {
        "paper_id": paper_id, "pdf_pages": len(reader.pages), "pdf_sha256": digest(pdf.read_bytes()),
        "main_tex_lf_sha256": digest(tex.replace("\r\n", "\n").encode()),
        "source_refs_hash_checked": len(meta["result_refs"]), "defined_citations": len(cited),
        "all_pages_rendered": True, "all_pages_have_text": True, "contact_sheets": sheets,
        "page_headings": [{"page": i + 1, "text": t[:160]} for i, t in enumerate(page_texts)],
        "visual_inspection": "Pending human/assistant image inspection; rendering is not visual approval."
    }
    (qa / "qa-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return {k: report[k] for k in ["paper_id", "pdf_pages", "source_refs_hash_checked", "defined_citations"]}


if __name__ == "__main__":
    try:
        root, results, pdftoppm = resolve_paths(parse_args())
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    ownership = json.loads((root / "catalog/research-ownership.json").read_text(encoding="utf-8-sig"))
    checks = bounded_checks()
    target = root / "papers" / SLUG / "editorial-qa" / "bounded-checks.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"bounded": checks, "papers": [inspect_paper(p, ownership, root, results, pdftoppm) for p in [SLUG, WAVE]]}, indent=2))
