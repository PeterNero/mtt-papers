"""Independent small editorial witnesses; frozen research certificates stay read-only."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import unittest

from test_cohesive_charge_editorial import add, eye, mm, scale, trace

ROOT = Path(__file__).resolve().parents[1]
PAPER = "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"
H = (0, 1, 2, 5, 6, 7)


def transpose(a):
    return [list(c) for c in zip(*a)]


def kron(a, b):
    return [[a[i][j]*b[r][s] for j in range(len(a[0])) for s in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def polynomial_add(a, b):
    return [sum(v[i] if i < len(v) else 0 for v in (a, b))
            for i in range(max(len(a), len(b)))]


def polynomial_mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def derivative(a):
    return [i*x for i, x in enumerate(a)][1:] or [F(0)]


def combine(a, b, factor=1):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0)+factor*value
    return {k: v for k, v in out.items() if v}


def wedge(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if i & j:
                continue
            inversions = sum(((j & ((1 << k)-1)).bit_count())
                             for k in range(3) if i & (1 << k))
            key = i | j
            out[key] = out.get(key, 0)+((-1)**inversions)*x*y
    return {k: v for k, v in out.items() if v}


def project(a):
    return {k: v for k, v in a.items() if k in H}


def homotopy(a):
    return {4: a[3]} if a.get(3) else {}


def m3(x, y, z, degree_x):
    return project(combine(wedge(homotopy(wedge(x, y)), z),
                           wedge(x, homotopy(wedge(y, z))), -(-1)**degree_x))


def trees(n):
    if n == 1:
        return [None]
    return [(left, right) for k in range(1, n)
            for left in trees(k) for right in trees(n-k)]


def tree_value(tree, leaves, root=True):
    if tree is None:
        return next(leaves)
    value = wedge(tree_value(tree[0], leaves, False),
                  tree_value(tree[1], leaves, False))
    return project(value) if root else homotopy(value)


class NestedEditorialTests(unittest.TestCase):
    def test_witten_formal_factorization_and_residual_hessian(self):
        phi = [F(1), F(0), F(1)]
        v = [x/2 for x in polynomial_mul(phi, phi)]
        vp, vpp = derivative(v), derivative(derivative(v))
        f = [F(1), F(-1), F(2), F(1)]
        def a(p):
            return polynomial_add(derivative(p), polynomial_mul(vp, p))
        def at(p):
            return polynomial_add([-x for x in derivative(p)], polynomial_mul(vp, p))
        kinetic = [-x for x in derivative(derivative(f))]
        common = polynomial_add(kinetic, polynomial_mul(polynomial_mul(vp, vp), f))
        corr = polynomial_mul(vpp, f)
        self.assertEqual(at(a(f)), polynomial_add(common, [-x for x in corr]))
        self.assertEqual(a(at(f)), polynomial_add(common, corr))
        self.assertEqual((derivative(phi)[0]**2, phi[0]*derivative(derivative(phi))[0],
                          vpp[0]), (0, 2, 2))

    def test_heisenberg_contraction_and_nonzero_m3(self):
        d = [[int(i == 3 and j == 4) for j in range(8)] for i in range(8)]
        h = transpose(d)
        p = [[int(i == j and i in H) for j in range(8)] for i in range(8)]
        self.assertEqual(add(mm(d, h), mm(h, d)), add(eye(8), scale(-1, p)))
        self.assertEqual(m3({1:1}, {1:1}, {2:1}, 1), {5:1})
        self.assertEqual(m3({1:1}, {2:1}, {2:1}, 1), {6:-1})
        self.assertEqual(m3({0:1}, {1:1}, {2:1}, 0), {})
        self.assertEqual(1+1+1, 1+2)

    def test_arity_four_heisenberg_trees_vanish(self):
        for masks in product(H, repeat=4):
            for tree in trees(4):
                self.assertEqual(tree_value(tree, iter({m:1} for m in masks)), {})

    def test_full_Q_is_not_self_adjoint_but_curvature_is_positive(self):
        d = [[int(i == 3 and j == 4) for j in range(8)] for i in range(8)]
        h = transpose(d)
        gamma = [[(-1)**i.bit_count() if i == j else 0 for j in range(8)] for i in range(8)]
        pi = [[int(i == j and i in H) for j in range(8)] for i in range(8)]
        for x in (F(0), F(2,3), F(2)):
            q = [[0,1,x], [1,0,0], [x,0,0]]
            f = mm(q, q)
            qa = add(kron(d, eye(3)), kron(gamma, q))
            self.assertEqual(q, transpose(q))
            self.assertNotEqual(qa, transpose(qa))
            self.assertEqual(add(qa, scale(-1, transpose(qa))),
                             kron(add(d, scale(-1, transpose(d))), eye(3)))
            self.assertEqual(mm(qa, qa), kron(eye(8), f))
            self.assertEqual(f, mm(transpose(q), q))
            hh = kron(h, eye(3))
            self.assertEqual(add(mm(qa, hh), mm(hh, qa)),
                             add(eye(24), scale(-1, kron(pi, eye(3)))))
            self.assertNotEqual(mm(qa, qa), mm(transpose(qa), qa))

    def test_normalized_cost_and_two_equal_hessian_terms(self):
        f0 = [[1,0,0], [0,1,0], [0,0,0]]
        fp = [[0,0,0], [0,0,1], [0,1,0]]
        fpp = [[2,0,0], [0,0,0], [0,0,2]]
        gram, residual = F(trace(mm(fp, fp)), 3), F(trace(mm(f0, fpp)), 3)
        self.assertEqual((gram, residual, gram+residual), (F(2,3), F(2,3), F(4,3)))
        for multiplicity in (8, 6):
            f = kron(eye(multiplicity), f0)
            self.assertEqual(F(trace(mm(f, f)), 2*3*multiplicity), F(1,3))

    def test_curvature_sign_in_curved_arity_one_identity(self):
        q, parity = [[0,1,0], [1,0,0], [0,0,0]], (0,1,1)
        f = mm(q, q)
        def dq(x, degree):
            return add(mm(q, x), scale(-(-1)**degree, mm(x, q)))
        for i, j in product(range(3), repeat=2):
            x = [[int(r == i and s == j) for s in range(3)] for r in range(3)]
            degree = (parity[i]+parity[j]) % 2
            square = dq(dq(x, degree), (degree+1) % 2)
            comm = add(mm(f, x), scale(-1, mm(x, f)))
            self.assertEqual(square, comm)
            m0 = scale(-1, f)
            self.assertEqual(add(square, add(mm(m0, x), scale(-1, mm(x, m0)))),
                             scale(0, eye(3)))

    def test_cyclic_top_form_is_not_invariant_scalar_norm(self):
        weights = (1, 1, 2)
        self.assertEqual(sum(weights), 4)
        self.assertNotEqual(sum(weights) % 3, 0)
        # The supertrace of the odd rank-one projection is negative.
        projection = [[0,0,0], [0,1,0], [0,0,0]]
        grading = [[1,0,0], [0,-1,0], [0,0,-1]]
        self.assertEqual(trace(mm(grading, mm(projection, projection))), -1)
        self.assertEqual(trace(mm(transpose(projection), projection)), 1)

    def test_paper_retains_distinct_carriers_and_domains(self):
        text = (ROOT / "papers" / PAPER / "main.tex").read_text()
        for anchor in ("sec:nested-witten", "sec:nil-minimal-model",
                       "sec:restricted-nested-arrow", "sec:noncentral-nested",
                       "sec:unital-curved-coefficients", "sec:response-retract",
                       "not the full module superconnection",
                       "different, nonminimal", "not domain certificates",
                       "\\mathbb Z_2", "inverse-character line"):
            self.assertTrue(anchor in text, f"missing contextual guard: {anchor}")


if __name__ == "__main__":
    unittest.main()
