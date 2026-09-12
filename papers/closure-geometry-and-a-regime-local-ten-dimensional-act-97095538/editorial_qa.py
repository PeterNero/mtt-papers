"""Scoped PDF rendering and bounded arithmetic checks for this editorial review."""

from pathlib import Path
import argparse
import hashlib
import json
import os
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
DEFAULT_FROZEN = ROOT.parent / "mtt-results-repro" / "release" / "results"
QA = ROOT / "papers" / SLUGS[0] / "tmp" / "editorial-qa-20260912"


def write_json(path, value):
    resolved = path.resolve()
    assert resolved.is_relative_to(QA.resolve())
    resolved.parent.mkdir(parents=True, exist_ok=True)
    resolved.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def render():
    from PIL import Image, ImageDraw
    from pypdf import PdfReader

    result = []
    for slug in SLUGS:
        pdf = ROOT / "papers" / slug / "main.pdf"
        out = QA / slug
        out.mkdir(parents=True, exist_ok=True)
        reader = PdfReader(pdf)
        subprocess.run(["pdftoppm", "-r", "120", "-png", str(pdf), str(out / "page")], check=True)
        pages = sorted(out.glob("page-*.png"))
        assert len(pages) == len(reader.pages)
        for start in range(0, len(pages), 4):
            sheet = Image.new("RGB", (1500, 2180), "#e4e4e4")
            draw = ImageDraw.Draw(sheet)
            for offset, page in enumerate(pages[start:start + 4]):
                im = Image.open(page).convert("RGB")
                im.thumbnail((735, 1040))
                x, y = (offset % 2) * 750, (offset // 2) * 1090
                draw.text((x + 12, y + 8), f"{slug[:38]} | page {start + offset + 1}", fill="black")
                sheet.paste(im, (x + 8, y + 32))
            sheet.save(out / f"contact-{start // 4 + 1:02}.png")
        texts = [(p.extract_text() or "") for p in reader.pages]
        write_json(out / "pages.json", [{"page": i + 1, "characters": len(t), "text": t} for i, t in enumerate(texts)])
        result.append({"paper_id": slug, "pdfpages": len(pages), "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(), "render_dpi": 120, "pages_nonempty": all(len(t.strip()) > 15 for t in texts), "contact_sheets": (len(pages) + 3) // 4})
        print(slug, len(pages), "pages rendered", flush=True)
    write_json(QA / "render.json", result)


def bounded_checks(frozen):
    import sympy as s

    checks = {}
    x, y, r = s.symbols("x y r", real=True)
    E = (x*x + (y + y*y)**2) / 2
    jets = [s.diff(E, y, n).subs({x: 0, y: 0}) for n in (2, 3, 4)]
    checks["repair_jets_1_6_12"] = jets == [1, 6, 12]
    Ew = (1 + y + y*y)*E
    checks["joint_metric_jets_9_48"] = [s.diff(Ew, y, n).subs({x: 0, y: 0}) for n in (3, 4)] == [9, 48]
    signed = x*x + x**3 / 2
    repair = s.diff(signed, x)**2 / 2
    checks["signed_vs_normal_vertices"] = [s.diff(signed, x, n).subs(x, 0) for n in (2, 3, 4)] == [2, 3, 0] and [s.diff(repair, x, n).subs(x, 0) for n in (2, 3, 4)] == [4, 18, 27]
    checks["quartic_Wick_coefficient"] = -s.Rational(12, 24)*3 == -s.Rational(3, 2)
    checks["two_cubic_Wick_coefficient"] = s.Rational(6**2, 2*6**2)*15 == s.Rational(15, 2)
    d = s.Matrix([[1]])
    dp = s.Matrix([[1, 1]])
    u0, u1 = s.Matrix([1, 0]), s.eye(1)
    checks["isometric_cochain_adjoint_counterexample"] = dp*u0 == u1*d and u0.T*u0 == s.eye(1) and dp.T*u1 != u0*d.T
    f = json.loads((frozen / "q79_family_source_cutset/artifact.json").read_text())
    w = f["exact_finite_nonpromotion_witness"]
    matrix = lambda a: s.Matrix([[s.sympify(v) for v in row] for row in a])
    P, a = matrix(w["low_projector"]), matrix(w["connection_hidden"])
    checks["frozen_finite_projection_kernel"] = P*P == P and P.T == P and P.rank() == 4 and P*a == s.zeros(8, 1) and a != s.zeros(8, 1)
    checks["frozen_distinct_lifts_distinct_normals"] = matrix(w["Dirac_hidden"]).T*matrix(w["Dirac_hidden"]) == matrix(w["Hessian_hidden"]) and matrix(w["Hessian_hidden"]) != matrix(w["Hessian_zero"])
    k = f["exact_Kato_family_witness"]
    U, P = matrix(k["Cayley_transport_at_one_half"]), matrix(k["projector_at_one_half"])
    H = matrix(k["Hessian_at_one_half"])
    checks["frozen_Kato_rotation_and_gap"] = U.T*U == s.eye(2) and P*P == P and H == P + 4*(s.eye(2)-P) and H.eigenvals() == {1: 1, 4: 1}
    f = json.loads((frozen / "causal_base_q79_seven_row_endpoint_factorization_packet/artifact.json").read_text())
    w = f["exact_feshbach_and_symmetry_witness"]
    K = matrix(w["hessian_K"])
    F = K[:2,:2] - K[:2,2:]*K[2:,2:].inv()*K[2:,:2]
    checks["frozen_Feshbach_9_over_5_and_det81"] = F == s.Rational(9,5)*s.eye(2) and K.det() == 81
    f = json.loads((frozen / "eta9_gate1_campaign/artifact.json").read_text())
    groups = f["groups_in_selected_order"]
    checks["gate1_row_accounting_not_Macaulay_replay"] = len(groups) == 30 and sum(g["target_count"] for g in groups) == 225 and len(set(g["group_index"] for g in groups)) == 30
    f = json.loads((frozen / "eta9_three_cycle_b96_nondetection/artifact.json").read_text())
    gram = matrix(f["B96_three_cycle_decision"]["Gram_matrix"])
    checks["B96_Gram_only_not_transport_replay"] = gram == -2*s.eye(3) and gram.det() == -8 and gram.rank() == 3
    checks["scale_stationarity_p4"] = s.simplify(s.diff(x**-4 + x*x/s.Integer(30), x).subs(x, s.Integer(60)**s.Rational(1,6))) == 0
    f = json.loads((frozen / "q79_cohesive_superconnection/artifact.json").read_text())
    w = f["exact_stratified_Hodge_witness"]
    Q, B, delta = matrix(w["Q_r"]), matrix(w["B_r"]), matrix(w["Delta_r"])
    checks["cohesive_Hodge_square_only"] = Q*Q == s.zeros(9) and B == Q+Q.T and B*B == delta
    write_json(QA / "bounded-checks.json", {"scope": "Small exact arithmetic and matrix checks, not independent scientific packet or continuum verification.", "checks": {k: bool(v) for k,v in checks.items()}, "passed": sum(bool(v) for v in checks.values()), "total": len(checks)})
    print(json.dumps({k: bool(v) for k,v in checks.items()}, indent=2))
    assert all(checks.values())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["render", "checks"])
    parser.add_argument("--frozen-results", type=Path,
                        default=os.environ.get("MTT_FROZEN_RESULTS", DEFAULT_FROZEN),
                        help="Frozen results directory; defaults to MTT_FROZEN_RESULTS or sibling mtt-results-repro/release/results.")
    args = parser.parse_args()
    frozen = args.frozen_results.expanduser().resolve()
    if args.mode == "checks" and not frozen.is_dir():
        parser.error(f"Frozen results directory does not exist: {frozen}")
    render() if args.mode == "render" else bounded_checks(frozen)
