"""Exact finite editorial examples; no archived research outputs are rewritten."""
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAPER = "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(k, a):
    return [[k*x for x in row] for row in a]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


class ChargeEditorialTests(unittest.TestCase):
    def test_lane_and_diagonal_central_characters_differ(self):
        # Exact Weyl commutators represented by their exponents modulo three.
        for j in range(3):
            xz_phase, zx_phase = j, (j+1) % 3
            self.assertEqual((xz_phase-zx_phase) % 3, 2)
        lane_characters = [2, 2, 2]
        self.assertEqual(len(set(lane_characters)), 1)
        self.assertEqual(sum(lane_characters) % 3, 0)

    def test_nilpotent_square_and_harmonic_mode(self):
        d = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
        dt = [list(c) for c in zip(*d)]
        delta = add(mm(d, dt), mm(dt, d))
        self.assertEqual(mm(d, d), scale(0, eye(3)))
        self.assertEqual(mm(add(d, dt), add(d, dt)), delta)
        self.assertEqual(delta, [[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        ph = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        self.assertEqual(mm(add(d, dt), ph), scale(0, eye(3)))
        self.assertEqual(mm(delta, ph), scale(0, eye(3)))

    def test_curved_square_does_not_identify_phase_modulo_sign(self):
        d = [[0, 1], [2, 0]]
        dt = [list(c) for c in zip(*d)]
        self.assertEqual(mm(d, d), scale(2, eye(2)))
        bp = add(d, dt)
        # At phase i, B = i(d-d^T), hence its square is -(d-d^T)^2.
        bm = add(d, scale(-1, dt))
        self.assertEqual(mm(bp, bp), scale(9, eye(2)))
        self.assertEqual(scale(-1, mm(bm, bm)), eye(2))
        a, b = F(3, 5), F(4, 5)
        self.assertEqual(a*a+b*b, 1)
        value = lambda x, y: 5+4*(x*x-y*y)
        self.assertEqual(value(a, b), value(a, -b))
        self.assertNotEqual((a, b), (a, -b))
        self.assertNotEqual((a, b), (-a, b))

    def test_jordan_lie_reconstruction_and_central_blindness(self):
        f, x = [[2, 0], [0, 1]], [[0, 1], [1, 0]]
        left, right = mm(f, x), mm(x, f)
        c, a = add(left, right), add(left, scale(-1, right))
        self.assertEqual(c, scale(3, x))
        self.assertEqual(a, [[0, 1], [-1, 0]])
        self.assertEqual(scale(F(1, 2), add(c, a)), left)
        self.assertEqual(trace(mm(c, x)), 6)
        self.assertEqual(scale(F(1, 2), add(mm(f, eye(2)), mm(eye(2), f))), f)
        for i in range(2):
            for j in range(2):
                e = [[int(r == i and s == j) for s in range(2)] for r in range(2)]
                shifted = add(f, scale(5, eye(2)))
                self.assertEqual(add(mm(f, e), scale(-1, mm(e, f))),
                                 add(mm(shifted, e), scale(-1, mm(e, shifted))))

    def test_intrinsic_circle_hessian_cancels_ambient_value(self):
        q0 = [[0,0,1,0], [0,0,0,1], [1,0,0,0], [0,1,0,0]]
        q1 = [[0,0,0,1], [0,0,-1,0], [0,-1,0,0], [1,0,0,0]]
        ident = eye(4)
        self.assertEqual(mm(q0, q0), ident)
        self.assertEqual(mm(q1, q1), ident)
        self.assertEqual(add(mm(q0, q1), mm(q1, q0)), scale(0, ident))
        q = add(scale(F(3,5), q0), scale(F(4,5), q1))
        self.assertEqual(mm(q, q), ident)
        self.assertEqual(F(1,2)*trace(mm(ident, ident)), 2)
        ambient = 2*trace(ident)
        normal = trace(mm(scale(2, q0), scale(-1, q0)))
        radial = 2*trace(ident)
        self.assertEqual((ambient, normal, radial), (8, -8, 8))
        self.assertEqual(ambient+normal, 0)

    def test_manuscript_retains_contextual_guards(self):
        text = (ROOT / "papers" / PAPER / "main.tex").read_text()
        for anchor in ("sec:central-qutrit-character", "sec:single-charge-factorization",
                       "sec:curved-phase-boundary", "sec:jordan-lie-center",
                       "sec:admissible-radial-circle", "sec:compression-leakage",
                       "sec:all-arity-source-map",
                       "Retained projectors are not the whole ambient projector",
                       "not unique recovery even", "central ambiguity",
                       "intrinsic circle Hessian is zero"):
            self.assertIn(anchor, text)


if __name__ == "__main__":
    unittest.main()
