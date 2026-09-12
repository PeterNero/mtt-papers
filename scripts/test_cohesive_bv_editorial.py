"""Bounded exact BV editorial checks, independent of research-worker code."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import unittest

from test_cohesive_charge_editorial import add, eye, mm, scale
from test_cohesive_nested_editorial import combine
import test_cohesive_global_editorial as hirsch


ROOT = Path(__file__).resolve().parents[1]
PAPER = "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"


def transpose(a):
    return [list(row) for row in zip(*a)]


def block(a, b):
    return [row + [0]*len(b[0]) for row in a] + [[0]*len(a[0]) + row for row in b]


def symplectic(n):
    ident = eye(n)
    return [[0]*n + row for row in ident] + [[-x for x in row] + [0]*n for row in ident]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x/q for x in a[r]]
        for i in range(r+1, len(a)):
            q = a[i][c]
            if q:
                a[i] = [x-q*y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def tensor_map(a, operation, signed=False):
    out = {}
    for (e, k, u, v), c in a.items():
        sign = -1 if signed and e == 1 else 1
        for s, value in operation(hirsch.state(k, u, v)).items():
            out = combine(out, {(e, *s): c*sign*value})
    return out


def total_d(a):
    out = tensor_map(a, hirsch.differential, signed=True)
    for (e, k, u, v), c in a.items():
        if e == 0:
            out = combine(out, {(1, k, u, v): c})
    return out


# Polynomial variables: even x,z,c*; odd c,x*,z*. Left odd derivatives.
ODD = (3, 4, 5)
GHOST = (0, 0, -2, 1, -1, -1)


def variable(i):
    return {tuple(int(j == i) for j in range(6)): F(1)}


def poly_product(a, b):
    out = {}
    for p, x in a.items():
        for q, y in b.items():
            r = tuple(i+j for i, j in zip(p, q))
            if any(r[i] > 1 for i in ODD):
                continue
            inversions = sum(p[i]*q[j] for i in ODD for j in ODD if i > j)
            out = combine(out, {r: x*y*(-1)**inversions})
    return out


def derivative(a, i):
    out = {}
    for p, c in a.items():
        if p[i]:
            sign = (-1)**sum(p[j] for j in ODD if j < i) if i in ODD else 1
            r = list(p)
            r[i] -= 1
            out = combine(out, {tuple(r): c*p[i]*sign})
    return out


def orientation_reduce(a, density=True):
    out = {}
    for p, c in a.items():
        antifields = p[2]+p[4]+p[5]
        top_degree = antifields + int(antifields == 0 and density)
        if top_degree == 1:
            out[p] = c
    return out


class BVEditorialTests(unittest.TestCase):
    def test_euler_obstruction_is_not_a_numerical_gap_question(self):
        dimensions = [1,1,21,42,21,1,1]
        orientation = [1,0,0,0,0,0,1]
        euler = lambda a: sum((-1)**i*x for i,x in enumerate(a))
        self.assertEqual(euler(dimensions),0)
        self.assertEqual(euler(orientation),2)
        self.assertEqual(euler([a-b for a,b in zip(dimensions,orientation)]),-2)
        ranks = [0,1,20,20,1,0,0]
        cohomology = [n-ranks[i]-(ranks[i-1] if i else 0) for i,n in enumerate(dimensions)]
        self.assertEqual(cohomology,[1,0,0,2,0,0,1])
        self.assertEqual(sum(dimensions)-sum(cohomology),84)

    def test_sharp_cyclic_witness_on_actual_rational_pairing(self):
        b = hirsch.PERP
        gram = [[hirsch.multiply(a,c).get((23,0,0),F(0)) for c in b] for a in b]
        work = [row + [F(i==j) for j in range(21)] for i,row in enumerate(gram)]
        for j in range(21):
            pivot = next(i for i in range(j,21) if work[i][j])
            work[j],work[pivot] = work[pivot],work[j]
            divisor = work[j][j]
            work[j] = [x/divisor for x in work[j]]
            for i in range(21):
                if i != j:
                    q = work[i][j]
                    work[i] = [x-q*y for x,y in zip(work[i],work[j])]
        inverse = [row[21:] for row in work]
        dual = []
        for j in range(21):
            a = {}
            for i in range(21):
                a = combine(a,hirsch.vscale(inverse[i][j],b[i]))
            dual.append(a)
        basis = [hirsch.state(0),hirsch.state(0,0,1)] + b
        basis += [hirsch.lift(a,1,0) for a in b]
        basis += [hirsch.lift(a,0,1) for a in dual]
        basis += [hirsch.lift(a,1,1) for a in dual]
        basis += [hirsch.state(23,1,0),hirsch.state(23,1,1)]
        degrees = [hirsch.degree(next(iter(a))) for a in basis]
        pairing = [[hirsch.pairing(a,c) for c in basis] for a in basis]
        self.assertEqual(rank(pairing),88)
        arrows = {1:(2,F(1)),65:(86,F(-1))}
        arrows.update({2+i:(23+i-1,F(1)) for i in range(1,21)})
        arrows.update({44+j:(65+j+1,F(-1)) for j in range(20)})
        diagonal = [F(0)]*88
        for source,(target,q) in arrows.items():
            self.assertEqual(degrees[target],degrees[source]+1)
            self.assertNotIn(target,arrows)
            diagonal[source] += q*q
            diagonal[target] += q*q
        for i,j in product(range(88),repeat=2):
            da = arrows.get(i)
            db = arrows.get(j)
            lhs = (da[1]*pairing[da[0]][j] if da else 0)
            lhs += (-1)**degrees[i]*(db[1]*pairing[i][db[0]] if db else 0)
            self.assertEqual(lhs,0)
        self.assertEqual(diagonal.count(0),4)
        self.assertEqual(diagonal.count(1),84)
        self.assertEqual([i for i,x in enumerate(diagonal) if not x],[0,43,64,87])

    def test_cotangent_contraction_and_pairing(self):
        d, h = [[0]*4 for _ in range(4)], [[0]*4 for _ in range(4)]
        d[3][2], h[2][3] = 1, 1
        p = [[1,0,0,0], [0,1,0,0]]
        i = transpose(p)
        dhat = block(d, scale(-1, transpose(d)))
        hhat = block(h, scale(-1, transpose(h)))
        ihat, phat = block(i, transpose(p)), block(p, transpose(i))
        j, retained = symplectic(4), mm(ihat, phat)
        self.assertEqual(mm(phat, ihat), eye(4))
        self.assertEqual(add(mm(dhat,hhat), mm(hhat,dhat)), add(eye(8),scale(-1,retained)))
        self.assertEqual(mm(mm(transpose(ihat), j), ihat), symplectic(2))
        self.assertEqual(add(mm(transpose(dhat),j),mm(j,dhat)), [[0]*8 for _ in range(8)])
        self.assertEqual(mm(retained,retained),retained)
        self.assertEqual(mm(transpose(retained),j),mm(j,retained))
        self.assertEqual(mm(hhat,hhat), [[0]*8 for _ in range(8)])
        self.assertEqual(mm(phat,hhat), [[0]*8 for _ in range(4)])
        self.assertEqual(mm(hhat,ihat), [[0]*4 for _ in range(8)])

    def test_projection_is_not_full_symplectic_equivalence(self):
        p = [[1,0,0,0], [0,1,0,0]]
        phat = block(p,p)
        pulled = mm(mm(transpose(phat),symplectic(2)),phat)
        self.assertEqual(symplectic(4)[2][6],1)
        self.assertEqual(pulled[2][6],0)
        self.assertNotEqual(pulled,symplectic(4))

    def test_tensor_contraction_on_all_288_states_and_sign_control(self):
        failures_without_sign = 0
        for e, s in product(range(3),hirsch.STATES):
            a = {(e,*s): F(1)}
            p = tensor_map(a,hirsch.project)
            h = tensor_map(a,hirsch.homotopy,signed=True)
            self.assertEqual(total_d(total_d(a)),{})
            self.assertEqual(combine(total_d(h),tensor_map(total_d(a),hirsch.homotopy,signed=True)),
                             combine(a,p,-1))
            self.assertEqual(tensor_map(p,hirsch.project),p)
            self.assertEqual(total_d(p),tensor_map(total_d(a),hirsch.project))
            self.assertEqual(tensor_map(h,hirsch.project),{})
            self.assertEqual(tensor_map(p,hirsch.homotopy,signed=True),{})
            self.assertEqual(tensor_map(h,hirsch.homotopy,signed=True),{})
            wrong = combine(total_d(tensor_map(a,hirsch.homotopy)),
                            tensor_map(total_d(a),hirsch.homotopy))
            failures_without_sign += wrong != combine(a,p,-1)
        self.assertGreater(failures_without_sign,0)

    def test_orientation_pairing_complement_and_volume(self):
        unit, nu = hirsch.state(0), hirsch.state(23,1,1)
        complement = [a for a in hirsch.RETAINED if a not in (unit,nu)]
        b = [[hirsch.pairing(a,c) for c in (unit,nu)] for a in (unit,nu)]
        self.assertEqual(b,[[0,1],[1,0]])
        self.assertEqual(len(complement),86)
        self.assertTrue(all(hirsch.pairing(a,c)==0 for a,c in product((unit,nu),complement)))
        self.assertEqual(rank([[hirsch.pairing(a,c) for c in complement] for a in complement]),86)
        self.assertEqual(hirsch.multiply(nu,nu),{})
        for volume in (F(1),F(2),F(3,7)):
            star = [[0,1/volume],[volume,0]]
            self.assertEqual(mm(star,star),eye(2))
            self.assertEqual(mm(b,star),[[volume,0],[0,1/volume]])

    def test_orientation_projection_is_not_an_algebra_quotient(self):
        v, ut = hirsch.state(0,0,1), hirsch.state(23,1,0)
        nu = hirsch.state(23,1,1)
        self.assertEqual(hirsch.project(v),v)
        self.assertEqual(hirsch.project(ut),ut)
        self.assertEqual(hirsch.multiply(v,ut),hirsch.vscale(-1,nu))
        retain = lambda a: {s:c for s,c in a.items() if s in ((0,0,0),(23,1,1))}
        self.assertEqual(retain(v),{})
        self.assertEqual(retain(ut),{})
        self.assertNotEqual(retain(hirsch.multiply(v,ut)),hirsch.multiply(retain(v),retain(ut)))

    def test_graded_action_density_and_zero_section(self):
        x,z,cs,c,xs,zs = [variable(i) for i in range(6)]
        q = lambda a: poly_product(c,derivative(a,0))
        s0 = combine(hirsch.vscale(F(1,2),poly_product(z,z)),
                     hirsch.vscale(F(1,3),poly_product(poly_product(z,z),z)))
        s = combine(s0,poly_product(xs,c))
        self.assertEqual(poly_product(c,c),{})
        self.assertEqual(poly_product(c,xs),hirsch.vscale(-1,poly_product(xs,c)))
        self.assertEqual(q(x),c)
        for a in (x,z,cs,c,xs,zs,poly_product(x,x)):
            self.assertEqual(q(q(a)),{})
        self.assertEqual(q(s0),{})
        self.assertTrue(all(sum(a*b for a,b in zip(p,GHOST))==0 for p in s))
        # Each field/dual derivative product vanishes in this example, so
        # the classical master equation is independent of bracket sign convention.
        for field,dual in ((0,4),(1,5),(3,2)):
            self.assertEqual(poly_product(derivative(s,field),derivative(s,dual)),{})
        self.assertEqual(orientation_reduce(s),s)
        self.assertEqual(orientation_reduce(s,density=False),poly_product(xs,c))
        self.assertNotEqual(orientation_reduce(s,density=False),s)
        self.assertEqual({p:a for p,a in s.items() if not(p[2]+p[4]+p[5])},s0)
        self.assertEqual(orientation_reduce(poly_product(xs,zs)),{})
        self.assertNotEqual(poly_product(xs,zs),{})

    def test_neutrality_is_relative_to_the_declared_action(self):
        source_weights = [0]*3
        topology_weights = [0]*88
        self.assertEqual({a+b for a,b in product(source_weights,topology_weights)},{0})
        target = [1,-4,2,-3,6,0,3]
        self.assertEqual(sum(w==0 for w in target),1)
        # An adjoint restricted to a noncentral diagonal circle need not be neutral.
        self.assertEqual({a-b for a,b in product([1,-1],repeat=2)},{-2,0,2})
        self.assertEqual(6 + (-6),0)

    def test_manuscript_has_typed_bv_boundaries(self):
        tex = (ROOT / "papers" / PAPER / "main.tex").read_text(encoding="utf-8")
        for anchor in ("sec:bv-reduction","sec:bv-cotangent-retract","sec:bv-zero-section",
                       "sec:bv-orientation-profile","sec:bv-mode-completeness","sec:bv-physical-bridge",
                       "sec:bv-euler-lifting"):
            self.assertIn("\\label{"+anchor+"}",tex)
        for phrase in ("Grassmann variable","zero-section-preserving","antifield-linear",
                       "not an algebra quotient","physical Hodge star or volume",
                       "does not identify the shared differential line with hypercharge"):
            self.assertIn(phrase,tex)


if __name__ == "__main__":
    unittest.main()
