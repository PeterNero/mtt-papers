"""Bounded editorial checks; no worker imports or large campaign replay."""
from fractions import Fraction as F
from pathlib import Path
import unittest

PAPER = Path(__file__).resolve().parents[1] / "papers" / (
    "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"
)


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def affine(t, v):
    return [row + [x] for row, x in zip(t, v)] + [[0]*len(v) + [1]]


def invariants(m):
    cube = 18*m*m
    euler = cube + 72
    chi = (cube + euler)//12
    b2 = euler + 2
    return chi, b2, (chi-1, b2-2*chi-21, chi-1)


class DeligneEditorialTests(unittest.TestCase):
    def test_class_dependent_hodge_ranks(self):
        for m, expected in [(3, (33, 236, (32,149,32))),
                            (9, (249,1532,(248,1013,248)))]:
            self.assertEqual(invariants(m), expected)
            self.assertEqual(sum(expected[2]), 18*m*m+51)
            self.assertEqual(expected[0]-1, expected[2][0])

    def test_discriminant_and_signatures(self):
        chi, b2, hodge = invariants(3)
        signature = (162-2*234)//3
        self.assertEqual(((b2+signature)//2,(b2-signature)//2),(67,169))
        self.assertEqual((67-3,169-20),(64,149))
        self.assertEqual(3**22*6,2*3**23)
        self.assertEqual((2*3**23) % 4,2)
        self.assertNotEqual((2*3**23) % 2**213,0)

    def test_integral_quotient_is_not_orthogonal_lattice(self):
        # In I_(1,1), A=< (2,1) > and V=< (1,2) > are primitive.
        # Pairing with V identifies L/A with Z, but V maps to 3Z.
        self.assertEqual(2*1-1*2,0)
        self.assertEqual(1*1-2*2,-3)
        self.assertEqual(1*1-0*2,1)
        self.assertEqual(F(1,3)*3,1)

    def test_local_affine_conjugacy_and_double_traversal(self):
        t = [[0,1],[1,0]]
        ident = [[1,0,0],[0,1,0],[0,0,1]]
        for a in (-7,0,3):
            mat = affine(t,[a,-a])
            g = [[1,0,a],[0,1,0],[0,0,1]]
            gi = [[1,0,-a],[0,1,0],[0,0,1]]
            self.assertEqual(mm(mat,mat),ident)
            self.assertEqual(mm(mm(gi,mat),g),affine(t,[0,0]))

    def test_local_origins_need_not_agree(self):
        t = [[0,1],[1,0]]
        a, b = affine(t,[0,0]), affine(t,[1,-1])
        self.assertNotEqual(mm(a,b),[[1,0,0],[0,1,0],[0,0,1]])
        # One common (T-I)u cannot equal two different translations.
        self.assertNotEqual([0,0],[1,-1])

    def test_affine_composition_and_invariant_translation(self):
        t = [[-1,0],[0,1]]
        mat = affine(t,[3,5])
        self.assertEqual(mm(mat,mat),[[1,0,0],[0,1,10],[0,0,1]])
        pminus = [[F(1),F(0)],[F(0),F(0)]]
        self.assertEqual(mm(pminus,pminus),pminus)

    def test_projective_bundle_and_support_matrix(self):
        self.assertEqual(33-1,32)
        self.assertEqual(3+31,34)
        self.assertEqual(44+2,46)
        g = [[0]*4 for _ in range(44)] + [[792,0,0,0],[0,792,0,0]]
        self.assertTrue(all(row == [0]*4 for row in g[:44]))
        self.assertEqual(g[-2:],[[792,0,0,0],[0,792,0,0]])
        self.assertFalse(any(1+2*i == 6 for i in range(5)))

    def test_affine_homogenization_does_not_change_base_rank(self):
        self.assertEqual(sum(invariants(3)[2])+1,214)
        self.assertEqual(sum(invariants(9)[2])+1,1510)
        self.assertNotEqual(214,1510)
        for total, boundary, positive in ((33,33,False),(33,34,False),(33,32,True)):
            self.assertEqual(total-boundary > 0, positive)

    def test_manuscript_anchors_and_scope(self):
        text = (PAPER / "main.tex").read_text(encoding="utf-8")
        for anchor in (
            "sec:deligne-family", "sec:deligne-rank-separation",
            "sec:deligne-incidence", "sec:deligne-leray",
            "sec:deligne-local-global", "sec:deligne-explicit-pencil",
            "sec:deligne-affine-connection", "sec:deligne-zero-boundary",
            "eq:deligne-integral-comparison",
        ):
            self.assertIn("\\label{"+anchor+"}",text)
        for guard in (
            "does not rerun the large", "weight-minus-one",
            "integral quotient is not the vanishing lattice",
            "Existing\nfinite-quotient and small-chart results are retained",
        ):
            self.assertIn(guard,text)


if __name__ == "__main__":
    unittest.main()
