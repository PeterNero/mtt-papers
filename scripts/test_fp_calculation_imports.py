"""Focused checks for manuscript imports, not a replacement for source replay."""
import json
import os
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import unittest

from consolidate_research_ownership import FP_CALC, owner

ROOT = Path(__file__).resolve().parents[1]
RESULTS = Path(os.environ.get(
    "MTT_RESULTS_REPO", str(ROOT.parent / "TEXPAPERS" / "mtt-results-repro")))


class FixedPointCalculationImports(unittest.TestCase):
    def test_companion_is_the_only_calculation_owner(self):
        for name in ("frontier_consolidation_20260911", "cubic_heat_trace_bound",
                     "l11_phase_channel", "finite_mode_recurrence_boundary"):
            self.assertEqual(owner({"id": "fixed_points_" + name,
                                    "repo_id": "fixed_points_frontier_20260911"})[0],
                             FP_CALC)
        fp = (ROOT / "papers/fixed-points-iii-disturbance-damping-balance-and-stability/main.tex").read_text()
        self.assertIn(r"\cite{NeroFiniteMode2026}", fp)
        self.assertNotIn("0.05568344585", fp)

    def test_outward_rounded_certificate_values(self):
        root = RESULTS / "release/results"
        equilibrium = json.loads((root / "fixed_points_frontier_consolidation_20260911/artifact.json").read_text())
        for row, upper in zip(equilibrium["equilibrium"]["rows"],
                              ("0.120292", "0.169007", "0.399192", "1.369221")):
            self.assertLessEqual(Decimal(row["full_trace_distance_upper"]), Decimal(upper))
        phase = json.loads((root / "fixed_points_l11_phase_channel/artifact.json").read_text())
        interval = phase["exact_boundary_model_transition_probability_enclosure"]
        self.assertLessEqual(Decimal("0.05568344585"), Decimal(interval["lower"]))
        self.assertGreaterEqual(Decimal("0.05936794417"), Decimal(interval["upper"]))
        self.assertLess(Decimal(phase["vector_error_bound"]["upper"]), Decimal("0.003840990"))
        self.assertLess(Decimal(phase["full_trace_error_upper"]), Decimal("0.015363959"))
        self.assertEqual((phase["dimension"], phase["outside_dimension"]), (489, 1149))
        self.assertFalse(phase["scope"]["all_worker_norm_columns_independently_recomputed"])

    def test_cubic_moment_and_degenerate_phase_bound(self):
        # A + B cos(theta): its square averages to A^2 + B^2/2.
        # A=q0^3+3q0*S and B^2=18*xa*xb*xr.
        q0, xa, xb, xr = map(Fraction, (2, 3, 5, 7))
        S = xa + xb + xr
        averaged = (q0**3 + 3*q0*S)**2 + 9*xa*xb*xr
        expanded = q0**6 + 6*q0**4*S + 9*q0**2*S**2 + 9*xa*xb*xr
        self.assertEqual(averaged, expanded)
        self.assertEqual(2**2+3**2+2*2*3*min(1, Fraction(2, 10)), Fraction(77, 5))
        self.assertEqual(2**2+3**2+2*2*3, 25)

    def test_model_boundaries_are_explicit(self):
        tex = (ROOT / "papers" / FP_CALC / "main.tex").read_text()
        for phrase in ("supplied quantization choices", "state approximability",
                       "not operator-norm recurrence", "every occupation",
                       "three norm columns were independently",
                       "pure-channel certificate does not upgrade"):
            self.assertIn(phrase, tex.replace("\n", " "))
        self.assertEqual(tex.count("% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE"), 1)
        self.assertEqual(tex.count("% END MTT MANAGED COMPUTATIONAL EVIDENCE"), 1)


if __name__ == "__main__":
    unittest.main()
