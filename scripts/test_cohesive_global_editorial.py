"""Small exact editorial checks; no worker code or archived outputs are imported."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import unittest

from test_cohesive_charge_editorial import add, eye, mm, scale, trace
from test_cohesive_nested_editorial import combine, kron

ROOT = Path(__file__).resolve().parents[1]
PAPER = "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"


@dataclass(frozen=True)
class Cyclotomic:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = coerce(other)
        return Cyclotomic(self.a+other.a, self.b+other.b)

    __radd__ = __add__

    def __neg__(self):
        return Cyclotomic(-self.a, -self.b)

    def __sub__(self, other):
        return self + -coerce(other)

    def __mul__(self, other):
        other = coerce(other)
        return Cyclotomic(self.a*other.a-self.b*other.b,
                          self.a*other.b+self.b*other.a-self.b*other.b)

    __rmul__ = __mul__

    def conjugate(self):
        return Cyclotomic(self.a-self.b, -self.b)


def coerce(x):
    return x if isinstance(x, Cyclotomic) else Cyclotomic(F(x))


def adjoint(a):
    return [[coerce(x).conjugate() for x in col] for col in zip(*a)]


def matrix(a):
    return [[coerce(x) for x in row] for row in a]


def unit(i, j, n):
    return matrix([[int(r == i and c == j) for c in range(n)] for r in range(n)])


def conjugate(g, a):
    return mm(mm(g, a), adjoint(g))


# A separate sparse implementation of the 24 x Lambda(u,v) rational model.
STATES = tuple(product(range(24), range(2), range(2)))
GRAM = [[F(0)]*22 for _ in range(22)]
for j in (0, 2, 4):
    GRAM[j][j+1] = GRAM[j+1][j] = F(1)
for offset in (6, 14):
    for j in range(8):
        GRAM[offset+j][offset+j] = F(-2)
    for a, b in [(i, i+1) for i in range(6)] + [(2, 7)]:
        GRAM[offset+a][offset+b] = GRAM[offset+b][offset+a] = F(1)


def state(k, u=0, v=0, value=1):
    return {} if not value else {(k, u, v): F(value)}


def vscale(q, a):
    return {k: q*x for k, x in a.items() if q*x}


def multiply(a, b):
    out = {}
    for (i, u, v), x in a.items():
        for (j, w, z), y in b.items():
            if u+w > 1 or v+z > 1:
                continue
            if i == 0 or j == 0:
                k, c = i+j, F(1)
            elif i < 23 and j < 23:
                k, c = 23, GRAM[i-1][j-1]
            else:
                continue
            out = combine(out, state(k, u+w, v+z, x*y*c*(-1)**(v*w)))
    return out


DELTA = combine(state(3), state(4, value=-2))
GAMMA = vscale(F(-1, 4), DELTA)
HCLASS = combine(state(1), state(2))
BASIS = [state(*s) for s in STATES]


def lift(a, u=0, v=0):
    return {(k, u, v): x for (k, _, _), x in a.items()}


def differential(a):
    out = {}
    for (k, u, v), x in a.items():
        if u:
            out = combine(out, vscale(x, multiply(state(k, 0, v), DELTA)))
    return out


def parallel(k):
    return (GRAM[2][k-1]-2*GRAM[3][k-1])/F(-4)


def project(a):
    out = {}
    for (k, u, v), x in a.items():
        if (k == 0 and u == 0) or (k == 23 and u == 1):
            out = combine(out, state(k, u, v, x))
        elif 0 < k < 23:
            out = combine(out, state(k, u, v, x))
            out = combine(out, vscale(-x*parallel(k), lift(DELTA, u, v)))
    return out


def homotopy(a):
    out = {}
    for (k, u, v), x in a.items():
        if not u and 0 < k < 23:
            out = combine(out, state(0, 1, v, x*parallel(k)))
        elif not u and k == 23:
            out = combine(out, vscale(x, lift(GAMMA, 1, v)))
    return out


PERP = [state(k) for k in (1, 2, *range(5, 23))]
PERP.append(combine(state(3), state(4, value=2)))
RETAINED = [state(0), state(0, v=1), state(23, u=1), state(23, u=1, v=1)]
RETAINED += [lift(x, u, v) for x in PERP for u, v in product(range(2), repeat=2)]


def degree(s):
    k, u, v = s
    return (0 if k == 0 else 4 if k == 23 else 2)+u+v


def pairing(a, b):
    return multiply(a, b).get((23, 1, 1), F(0))


class GlobalEditorialTests(unittest.TestCase):
    def test_projective_triple_and_positive_noncentral_cost(self):
        w = Cyclotomic(F(0), F(1))
        ident = matrix(eye(3))
        x = matrix([[0,0,1], [1,0,0], [0,1,0]])
        z = matrix([[1,0,0], [0,w,0], [0,0,w*w]])
        g01, g12 = kron(ident, x), kron(ident, z)
        g20 = scale(w, adjoint(mm(g01, g12)))
        triple = mm(mm(g01, g12), g20)
        self.assertEqual(triple, scale(w, matrix(eye(9))))
        q = add(kron(add(unit(0,1,3), unit(1,0,3)), ident),
                add(kron(unit(0,2,3), x), kron(unit(2,0,3), adjoint(x))))
        self.assertEqual(q, adjoint(q))
        self.assertNotEqual(q, conjugate(g12, q))
        curvature = mm(q, q)
        self.assertEqual(curvature, mm(adjoint(q), q))
        self.assertEqual(F(1,18)*trace(mm(curvature, curvature)), coerce(F(4,3)))
        self.assertNotEqual(mm(curvature, unit(3,6,9)), mm(unit(3,6,9), curvature))
        for i, j in product(range(9), repeat=2):
            e = unit(i,j,9)
            self.assertEqual(conjugate(triple, e), e)
        # Scalar changes of the chosen atlas are invisible under Ad.
        self.assertEqual(mm(mm(g01,g12), scale(w*w,g20)), matrix(eye(9)))
        self.assertEqual(conjugate(g20, q), conjugate(scale(w*w,g20), q))

    def test_cyclic_pairing_requires_character_compensation(self):
        w = Cyclotomic(F(0), F(1))
        # a times bc is the top form, whose weights add to four.
        transformed_pair = w * (w*w*w)
        self.assertEqual(transformed_pair, w)
        self.assertNotEqual(transformed_pair, coerce(1))
        self.assertEqual(transformed_pair*(w*w), coerce(1))

    def test_hirsch_contraction_and_betti_ranks(self):
        ranks = [F(0)]*7
        for s, a in zip(STATES, BASIS):
            self.assertEqual(differential(differential(a)), {})
            self.assertEqual(combine(differential(homotopy(a)), homotopy(differential(a))),
                             combine(a, project(a), -1))
            self.assertEqual(project(project(a)), project(a))
            self.assertEqual(homotopy(homotopy(a)), {})
            self.assertEqual(homotopy(project(a)), {})
            self.assertEqual(project(homotopy(a)), {})
            ranks[degree(s)] += project(a).get(s, 0)
        self.assertEqual(ranks, [1,1,21,42,21,1,1])
        self.assertEqual(sum(ranks), 88)
        self.assertEqual(multiply(DELTA, DELTA), state(23, value=-4))
        self.assertEqual(multiply(HCLASS, HCLASS), state(23, value=2))
        self.assertEqual(multiply(HCLASS, DELTA), {})

    def test_hirsch_strict_transfer_has_finite_structural_witness(self):
        possible = (lift(GAMMA, 1, 0), lift(GAMMA, 1, 1))
        nonzero_products = 0
        for a, b in product(RETAINED, repeat=2):
            ab = multiply(a, b)
            nonzero_products += bool(project(ab))
            hab = homotopy(ab)
            # Every first hidden pair lies in span(u gamma, u gamma v).
            for v in range(2):
                coeff = hab.get((3,1,v), 0)/F(-1,4)
                hab = combine(hab, vscale(coeff, possible[v]), -1)
            self.assertEqual(hab, {})
        self.assertEqual(nonzero_products, 555)
        for z, a in product(possible, RETAINED):
            self.assertEqual(project(multiply(z, a)), {})
            self.assertEqual(project(multiply(a, z)), {})
        all_hidden = (state(0,1), state(0,1,1), *possible)
        for z, a in product(all_hidden, BASIS):
            self.assertEqual(homotopy(multiply(z, a)), {})
        for a, b in product(all_hidden, repeat=2):
            self.assertEqual(multiply(a, b), {})
        # This verifies finite span conditions, not 88^3 individual triples.

    def test_hirsch_pairing_and_nonmultiplicative_representatives(self):
        for a, b in product(BASIS, repeat=2):
            self.assertEqual(pairing(project(a), b), pairing(a, project(b)))
        self.assertEqual(pairing(state(0), state(0)), 0)
        self.assertEqual(pairing(state(0), state(23,1,1)), 1)
        self.assertEqual(project(HCLASS), HCLASS)
        hh = multiply(HCLASS, HCLASS)
        self.assertEqual(hh, state(23, value=2))
        self.assertEqual(project(hh), {})
        self.assertEqual(homotopy(hh), vscale(2, lift(GAMMA, 1)))
        for a in RETAINED:
            self.assertEqual(differential(a), {})
            self.assertEqual(project(a), a)

    def test_intrinsic_compiler_uses_transported_normalization(self):
        u = [[1,0], [0,1], [0,0]]
        ut = [list(col) for col in zip(*u)]
        f = [[2,0], [0,1]]
        ff = mm(mm(u, f), ut)
        self.assertEqual(mm(mm(ut, ff), u), f)
        self.assertEqual(trace(mm(ff,ff)), trace(mm(f,f)))
        self.assertNotEqual(F(1,3)*trace(mm(ff,ff)), F(1,2)*trace(mm(f,f)))
        self.assertEqual(mm(u,ut), [[1,0,0], [0,1,0], [0,0,0]])

    def test_manuscript_keeps_topology_and_metric_boundaries(self):
        text = (ROOT / "papers" / PAPER / "main.tex").read_text()
        for anchor in ("sec:morita-curved-descent", "sec:morita-metric-boundary",
                       "sec:q79-hirsch-model", "sec:q79-hirsch-interactions",
                       "sec:morita-compiler-range", "not a positive Hilbert norm",
                       "not all scalar cyclic-pairing hypotheses",
                       "not proved formal", "not the physical 96-dimensional"):
            self.assertTrue(anchor in text, anchor)


if __name__ == "__main__":
    unittest.main()
