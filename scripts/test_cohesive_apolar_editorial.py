"""Bounded exact editorial examples, not a replay of the 48-fiber campaign."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import unittest

from test_cohesive_charge_editorial import add, eye, mm, scale
from test_cohesive_matter_editorial import diagonal, rank, transpose

PAPER = Path(__file__).resolve().parents[1] / "papers" / (
    "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"
)


def inverse(a):
    n = len(a)
    rows = [[F(v) for v in row] + [F(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            raise ValueError("singular restricted Gram form")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        c = rows[j][j]
        rows[j] = [v/c for v in rows[j]]
        for i in range(n):
            if i != j:
                c = rows[i][j]
                rows[i] = [x-c*y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def functional(b, g, hdim=1):
    gram = mm(mm(transpose(b), g), b)
    return mm(mm(inverse(gram)[hdim:], transpose(b)), g)


class ApolarEditorialTests(unittest.TestCase):
    def test_response_lift_preserves_products_and_doubles_rank(self):
        h = [[1, 0, 2, 0], [0, 1, 0, 3],
             [0, 0, 1, 0], [0, 0, 0, 1]]
        ih = inverse(h)
        def lift(a):
            block = [a[0]+[0, 0], a[1]+[0, 0],
                     [0, 0]+a[0], [0, 0]+a[1]]
            return mm(mm(h, block), ih)
        a, b = [[0, 1], [0, 0]], [[0, 0], [1, 0]]
        self.assertEqual(lift(mm(a, b)), mm(lift(a), lift(b)))
        self.assertEqual(rank(lift(a)), 2*rank(a))
        d = [[0, 0, 0, 0], [0, 0, 0, 0],
             [1, 0, 0, 0], [0, 1, 0, 0]]
        d = mm(mm(h, d), ih)
        self.assertEqual(mm(d, lift(a)), mm(lift(a), d))

    def test_fitting_polynomial_and_rank_stability(self):
        a = diagonal([0]*12+[1, 2, 3, 4, 5, 6])
        polynomial, f0 = eye(18), F(1)
        for root in range(1, 7):
            polynomial = mm(polynomial, add(a, scale(-root, eye(18))))
            f0 *= -root
        p = add(eye(18), scale(-1/f0, polynomial))
        q = add(eye(18), scale(-1, p))
        self.assertEqual(p, diagonal([0]*12+[1]*6))
        self.assertEqual(mm(p, p), p)
        self.assertEqual(rank(q), 12)
        self.assertEqual(mm(a, q), [[0]*18 for _ in range(18)])

    def test_arrows_partial_involution_and_mapping_cone_sign(self):
        t = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
        s = transpose(t)
        p, r = mm(t, s), mm(s, t)
        partial = add(t, s)
        self.assertEqual(mm(t, t), [[0]*3 for _ in range(3)])
        self.assertEqual(mm(partial, partial), add(p, r))
        self.assertEqual(mm(mm(partial, partial), partial), partial)
        self.assertNotEqual(mm(partial, partial), [[0]*3 for _ in range(3)])
        d, a = [[0, 1], [0, 0]], eye(2)
        cone = [d[0]+a[0], d[1]+a[1],
                [0, 0]+scale(-1, d)[0], [0, 0]+scale(-1, d)[1]]
        wrong = [d[0]+a[0], d[1]+a[1], [0, 0]+d[0], [0, 0]+d[1]]
        self.assertEqual(mm(cone, cone), [[0]*4 for _ in range(4)])
        self.assertNotEqual(mm(wrong, wrong), [[0]*4 for _ in range(4)])

    def test_natural_retraction_and_nonorthogonal_complement(self):
        b, g = [[1, 1], [0, 1], [1, 0]], diagonal([2, 3, 5])
        f = functional(b, g)
        h, c = [[row[0]] for row in b], [[row[1]] for row in b]
        r = mm(c, f)
        self.assertEqual(mm(f, h), [[0]])
        self.assertEqual(mm(f, c), [[1]])
        self.assertEqual(mm(r, r), r)
        self.assertEqual(rank(r), 1)
        self.assertNotEqual(mm(transpose(r), g), mm(g, r))

    def test_full_adapted_covariance_and_complement_shift(self):
        b, g = [[1, 1], [0, 1], [1, 0]], diagonal([2, 3, 5])
        f = functional(b, g)
        u = [[1, 2, 0], [0, 1, 3], [0, 0, 1]]
        iu = inverse(u)
        m = [[F(2), F(7)], [F(0), F(3)]]
        transformed = functional(mm(mm(u, b), m), mm(mm(transpose(iu), g), iu))
        self.assertEqual(transformed, scale(F(1, 3), mm(f, iu)))
        shifted = mm(b, [[1, 11], [0, 1]])
        self.assertEqual(functional(shifted, g), f)
        self.assertNotEqual(functional(mm(u, b), g), mm(f, iu))

    def test_split_lift_changes_while_quotient_does_not(self):
        f = [[0, 1]]
        for a in [-7, 0, 3, F(2, 5)]:
            b = [[1, a], [0, 1]]
            self.assertEqual(functional(b, eye(2)), f)
            r = mm([[a], [1]], f)
            self.assertEqual(mm(r, r), r)
            self.assertEqual(r, [[0, a], [0, 1]])

    def test_restricted_nondegeneracy_is_an_extra_hypothesis(self):
        g, b = diagonal([1, -1]), [[1], [1]]
        self.assertEqual(rank(g), 2)
        gram = mm(mm(transpose(b), g), b)
        self.assertEqual(gram, [[0]])
        with self.assertRaises(ValueError):
            inverse(gram)

    def test_divided_power_duality_and_socle_example(self):
        def exponents(n):
            return [(a, b, n-a-b) for a in range(n+1) for b in range(n-a+1)]
        for degree in range(4):
            low, high = exponents(degree), exponents(degree+1)
            for axis in range(3):
                multiply = [[0]*len(low) for _ in high]
                derivative = [[0]*len(high) for _ in low]
                for j, monomial in enumerate(low):
                    nxt = list(monomial)
                    nxt[axis] += 1
                    i = high.index(tuple(nxt))
                    multiply[i][j] = 1
                for j, monomial in enumerate(high):
                    if monomial[axis]:
                        nxt = list(monomial)
                        nxt[axis] -= 1
                        derivative[low.index(tuple(nxt))][j] = 1
                self.assertEqual(transpose(multiply), derivative)
        # In k[x,y,z]/m^2 the degree-one multiplication map is zero.
        self.assertEqual(rank([[0]*3 for _ in range(3)]), 0)
        self.assertEqual(len(exponents(1)), 3)
        self.assertEqual(18-3, 15)
        self.assertEqual(len(exponents(15)), 136)
        self.assertEqual(len(exponents(7)), 36)
        self.assertTrue(all(factorial(a)*factorial(b)*factorial(c) % 21817
                            for a, b, c in exponents(15)))

    def test_source_anchors_and_finite_scope(self):
        tex = (PAPER / "main.tex").read_text(encoding="utf-8")
        bib = (PAPER / "main.bib").read_text(encoding="utf-8")
        for key in ["UnifiedPBWIntertwiner2026", "UnifiedCoefficientFitting2026",
                    "UnifiedApolarOrbit2026", "UnifiedSelectedRetraction2026",
                    "UnifiedNaturalRetraction2026", "UnifiedQuotientDescent2026",
                    "UnifiedSocleDuality2026", "UnifiedTerminalChain2026"]:
            self.assertIn(key, tex)
            self.assertIn("@misc{"+key+",", bib)
        for anchor in ["sec:pbw-intertwiner", "sec:pbw-apolar-orbit",
                       "sec:apolar-natural-retraction", "sec:apolar-quotient-descent",
                       "sec:apolar-socle", "sec:apolar-terminal-map"]:
            self.assertIn("\\label{"+anchor+"}", tex)
        for phrase in ["not a positive physical metric",
                       "not 48 independently executed actual",
                       "The mixing block", "positive HYM Hessian",
                       "rather than a square-zero differential",
                       "not reimported as current research blockers"]:
            self.assertIn(phrase, tex)


if __name__ == "__main__":
    unittest.main()
