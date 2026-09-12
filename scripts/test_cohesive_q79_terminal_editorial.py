"""Small independent editorial checks, not a replay of worker research."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import unittest

import sympy as s

PAPER = Path(__file__).resolve().parents[1] / "papers" / (
    "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"
)


class Q79TerminalEditorialTests(unittest.TestCase):
    def test_fitting_ladder_after_unit_elimination(self):
        a, r, t = s.symbols("a r t")
        m = s.diag(s.Matrix([[a, r], [-t, 0]]), r*t, r*t)
        for size, expected in [(4, [r**3*t**3]), (3, [r*r*t*t]),
                               (2, [r*t]), (1, [a, r, t])]:
            minors = [s.expand(m.extract(rows, cols).det())
                      for rows in combinations(range(4), size)
                      for cols in combinations(range(4), size)]
            actual = s.groebner([x for x in minors if x != 0], a, r, t)
            target = s.groebner(expected, a, r, t)
            self.assertEqual(list(actual), list(target))

    def test_presentation_ranks_and_divisor_class(self):
        def matrix(a, r, t):
            return s.diag(*[s.Matrix([[c, r], [-t, 0]]) for c in (a, 1, 1)])
        for args, rank in [((2, 1, 1), 6), ((2, 0, 1), 3),
                           ((2, 1, 0), 3), ((2, 0, 0), 3), ((0, 0, 0), 2)]:
            self.assertEqual(matrix(*args).rank(), rank)
        self.assertEqual(tuple(3*x for x in (1, 1)), (3, 3))
        self.assertNotEqual((3, 3), (9, 3))

    def test_real_topology_excludes_resonance_extremes(self):
        pairs = []
        for euler in (-4, -2, 0, 2, 4, 6):
            plus = (22+euler-2)//2
            pairs.append((plus, 22-plus-2))
        self.assertEqual(pairs, [(8, 12), (9, 11), (10, 10),
                                 (11, 9), (12, 8), (13, 7)])
        self.assertNotIn((1, 19), pairs)
        self.assertNotIn((19, 1), pairs)
        self.assertEqual(21-(2-1), 20)
        for delta_pairing in (-7, 0, 5):
            self.assertEqual((4*F(delta_pairing, 4)).denominator, 1)

    def test_repair_and_variance_basin_are_different(self):
        x = s.symbols("x", positive=True)
        self.assertEqual(s.limit(1/(1+2*x*x), x, 0), 1)
        p = s.symbols("p")
        flow = 4*p*(1-p)*(2*p-1)
        self.assertLess(flow.subs(p, s.Rational(1, 3)), 0)
        self.assertEqual(s.integrate(2*(1-p), (p, s.Rational(1, 2), 1)),
                         s.Rational(1, 4))
        self.assertNotEqual(F(1, 4), F(1, 3))

    def test_first_count_instrument_and_exact_state(self):
        p = s.ones(3)/3
        q = s.eye(3)-p
        rho = s.diag(1, 0, 0)
        self.assertEqual(p*p, p)
        self.assertEqual(q*q, q)
        self.assertEqual(p*q, s.zeros(3))
        branches = [rho/448, s.Rational(447, 448)*p*rho*p,
                    s.Rational(447, 448)*q*rho*q]
        self.assertEqual([s.trace(x) for x in branches],
                         [s.Rational(1, 448), s.Rational(149, 448),
                          s.Rational(149, 224)])
        expected = s.Matrix([[748, -149, -149], [-149, 298, 298],
                             [-149, 298, 298]])/1344
        self.assertEqual(sum(branches, s.zeros(3)), expected)
        self.assertEqual(s.trace(expected), 1)
        self.assertTrue(all(value >= 0 for value in expected.eigenvals()))

    def test_conditionals_have_their_correct_domains(self):
        p = s.ones(3)/3
        q = s.eye(3)-p
        mixed = s.eye(3)/3
        self.assertEqual((q*mixed*q/s.trace(q*mixed)).rank(), 2)
        self.assertEqual(s.trace(p*q/2), 0)
        root = s.diag(1, 0, 0)
        self.assertEqual(s.trace((s.eye(3)-root)*root), 0)

    def test_projective_conjugation_preserves_path_map(self):
        p = s.ones(3)/3
        rho = s.diag(1, 0, 0)
        u = s.diag(1, s.I, -1)
        pu, ru = u*p*u.adjoint(), u*rho*u.adjoint()
        self.assertEqual(s.trace(ru*pu), s.trace(rho*p))
        self.assertEqual(pu*ru*pu, u*(p*rho*p)*u.adjoint())
        self.assertEqual((s.I*u)*rho*(s.I*u).adjoint(), ru)

    def test_manuscript_anchors_and_limits(self):
        text = (PAPER/"main.tex").read_text(encoding="utf-8")
        for anchor in ("sec:q79-fitting-descent", "eq:q79-fitting-ladder",
                       "sec:q79-bk3-kernel", "eq:q79-bk3-dense",
                       "sec:q79-pathwise-repair", "eq:q79-record-state"):
            self.assertIn("\\label{"+anchor+"}", text)
        for guard in ("not an\nembedding with the subspace topology",
                      "does not remove\nthe two continuous coordinates",
                      "zero-weight mark has zero probability",
                      "un-stopped counting process", "ordinary coupled physical system",
                      "not a general impossibility theorem for deterministic MTT"):
            self.assertIn(guard, text)


if __name__ == "__main__":
    unittest.main()

