"""Bounded exact checks for the atlas's diagnostic interpretation."""
from pathlib import Path
import unittest
import sympy as s


class AtlasEditorialTests(unittest.TestCase):
    def test_cycle_kernel_projector_and_gap(self):
        d = s.Matrix([[-1, 1, 0], [0, -1, 1], [1, 0, -1]])
        lap = d.T*d
        proj = s.eye(3)-d.T*(d*d.T).pinv()*d
        self.assertEqual(lap, 3*s.eye(3)-s.ones(3))
        self.assertEqual(proj, s.ones(3)/3)
        self.assertEqual(proj*proj, proj)
        self.assertEqual(d*proj, s.zeros(3))
        self.assertEqual(lap.eigenvals(), {0: 1, 3: 2})
        self.assertEqual(lap, 3*(s.eye(3)-proj))

    def test_positive_weights_preserve_kernel_not_gap(self):
        d = s.Matrix([[-1, 1]])
        self.assertEqual((d.T*7*d).nullspace(), d.nullspace())
        self.assertEqual((d.T*7*d).eigenvals(), {0: 1, 14: 1})
        self.assertNotEqual((d.T*0*d).nullspace(), d.nullspace())

    def test_obstructed_tangent_is_not_a_modulus(self):
        x = s.symbols('x', real=True)
        self.assertEqual(s.diff(x*x, x).subs(x, 0), 0)
        self.assertEqual(s.solveset(x*x, x, domain=s.S.Reals), s.FiniteSet(0))

    def test_affine_residual_requires_cokernel_certificate(self):
        d = s.Matrix([[1], [1]])
        b = s.Matrix([1, -1])
        self.assertEqual(d.T*b, s.zeros(1, 1))
        self.assertEqual((b.T*b)[0], 2)
        x = s.symbols('x', real=True)
        self.assertEqual(s.expand(((d*x-b).T*(d*x-b))[0]), 2*x*x+2)

    def test_cox_grading_is_not_uniform_flat_character(self):
        from itertools import product
        basis = [a for a in product(range(3), repeat=3) if sum(a) < 3]
        self.assertEqual([sum(sum(a) == n for a in basis) for n in range(3)], [1,3,6])
        self.assertEqual([sum(sum(a) == 2 and a[2] == n for a in basis)
                          for n in (2,1,0)], [1,2,3])
        self.assertEqual({(-1)**sum(a) for a in basis}, {-1,1})

    def test_manuscript_has_scoped_explanation(self):
        root = Path(__file__).resolve().parents[1]
        tex = (root/'papers/cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows/main.tex').read_text(encoding='utf-8')
        for anchor in ('sec:atlas-reference', 'eq:atlas-compatibility', 'eq:atlas-gap',
                       'sec:atlas-tangent', 'sec:atlas-arrows', 'sec:atlas-chronology'):
            self.assertIn(anchor, tex)
        self.assertIn('foundational Fixed Points stay independent', tex)
        self.assertNotIn('Foundations, Fixed Points, QG may cite', tex)


if __name__ == '__main__':
    unittest.main()
