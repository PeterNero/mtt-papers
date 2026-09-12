"""Exact local editorial witnesses; never imports the research worker."""
from fractions import Fraction as F
from pathlib import Path
import unittest

from test_cohesive_charge_editorial import add, eye, mm, scale
from test_cohesive_matter_editorial import diagonal, rank, transpose

PAPER = Path(__file__).resolve().parents[1] / "papers" / (
    "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"
)


def vecadd(a, b):
    return tuple(x+y for x, y in zip(a, b))


def vecscale(c, a):
    return tuple(c*x for x in a)


def basis(n):
    return [tuple(int(i == j) for i in range(n)) for j in range(n)]


# Ordered degrees (1,1,1,2,2): e,b,z,c,v.
DEGREES = (1, 1, 1, 2, 2)


def d(x):
    return (0, 0, 0, x[0], -2*x[0]+x[1])


def bracket(x, y):
    return (0, 0, 0, 2*x[0]*y[0], -2*x[0]*y[0])


def mc(x):
    return vecadd(d(x), vecscale(F(1, 2), bracket(x, x)))


def section(x, closed=0):
    return (x, 2*x+x*x, closed, 0, 0)


class StringEditorialTests(unittest.TestCase):
    def test_rank_and_central_adjoint(self):
        self.assertEqual(sum([3, 3**2-1, 3**2-1, 9**2-1, 3]), 102)
        for n in [3, 9]:
            scalar, inverse = scale(F(2, 3), eye(n)), scale(F(3, 2), eye(n))
            for i in range(n):
                for j in range(n):
                    x = [[int(a == i and b == j) for b in range(n)]
                         for a in range(n)]
                    self.assertEqual(mm(mm(scalar, x), inverse), x)

    def test_double_complex_and_anomaly_sign(self):
        # tau,h,k,v plus three closed curvature labels.
        p = [[0]*7 for _ in range(7)]
        b = [[0]*7 for _ in range(7)]
        p[1][0], p[3][2] = 1, 1
        b[2][0], b[3][1] = 1, -1
        zero = [[0]*7 for _ in range(7)]
        self.assertEqual(mm(p, p), zero)
        self.assertEqual(mm(b, b), zero)
        self.assertEqual(add(mm(p, b), mm(b, p)), zero)
        weights = (F(3, 2), F(-1, 2), F(-1, 2))
        xi = sum(2*w for w in weights)
        self.assertEqual(xi, 1)
        self.assertEqual(add(p, b)[3][1]+xi, 0)
        for i in (4, 5, 6):
            self.assertTrue(all(p[j][i] == b[j][i] == 0 for j in range(7)))

    def test_chern_weil_deformation_and_form_sign(self):
        # Commuting scalar curvature witness, not a continuum connection.
        for f in [F(-2), F(1, 3), F(3)]:
            for a in [F(-3, 2), F(0), F(5)]:
                delta = (f+a)**2-f**2
                self.assertEqual(delta, 2*f*a+a*a)
                self.assertEqual(-f*f-delta+(f+a)**2, 0)
                if delta:
                    self.assertNotEqual(-f*f+delta+(f+a)**2, 0)

    def test_finite_dg_lie_axioms_on_all_basis_elements(self):
        zero = (0,)*5
        for i, x in enumerate(basis(5)):
            self.assertEqual(d(d(x)), zero)
            for j, y in enumerate(basis(5)):
                sign = (-1)**(DEGREES[i]*DEGREES[j])
                self.assertEqual(bracket(x, y), vecscale(-sign, bracket(y, x)))
                self.assertEqual(d(bracket(x, y)), vecadd(
                    bracket(d(x), y), vecscale((-1)**DEGREES[i], bracket(x, d(y)))))
                for k, z in enumerate(basis(5)):
                    terms = [
                        vecscale((-1)**(DEGREES[i]*DEGREES[k]), bracket(x, bracket(y, z))),
                        vecscale((-1)**(DEGREES[j]*DEGREES[i]), bracket(y, bracket(z, x))),
                        vecscale((-1)**(DEGREES[k]*DEGREES[j]), bracket(z, bracket(x, y))),
                    ]
                    self.assertEqual(vecadd(vecadd(terms[0], terms[1]), terms[2]), zero)

    def test_mc_lift_closed_fiber_and_nonlinearity(self):
        roots = []
        for x in map(F, range(-4, 5)):
            for lam in [F(-2, 3), F(0), F(7)]:
                self.assertEqual(mc(section(x, lam)), (0, 0, 0, x+x*x, 0))
                self.assertEqual(section(x, lam)[0], x)
                self.assertEqual(d((0, 0, lam, 0, 0)), (0,)*5)
            if mc(section(x)) == (0,)*5:
                roots.append(x)
        self.assertEqual(roots, [-1, 0])
        self.assertEqual(vecadd(section(2), vecscale(-2, section(1))), (0, 2, 0, 0, 0))
        # pi(e,b,z,c,v)=(e,c) is a strict quotient; form lane is its kernel.
        pi = lambda x: (x[0], x[3])
        for x in basis(5):
            self.assertEqual(pi(d(x)), (0, x[0]))
            for y in basis(5):
                self.assertEqual(pi(bracket(x, y)), (0, 2*x[0]*y[0]))
        self.assertEqual([i for i, x in enumerate(basis(5)) if pi(x) == (0, 0)], [1, 2, 4])

    def test_lie_embedding_is_not_associative(self):
        e12, e21 = [[0, 1], [0, 0]], [[0, 0], [1, 0]]
        product = mm(e12, e21)
        commutator = add(product, scale(-1, mm(e21, e12)))
        self.assertEqual(sum(commutator[i][i] for i in range(2)), 0)
        self.assertEqual(sum(product[i][i] for i in range(2)), 1)

    def test_moment_map_anchor_and_pseudo_metric(self):
        n = 4
        omega = [[int(j == i+n)-int(i == j+n) for j in range(2*n)]
                 for i in range(2*n)]
        complex_i = scale(-1, omega)
        self.assertEqual(mm(omega, complex_i), eye(8))
        for i in range(n):
            rho = [[-int(j == i+n)] for j in range(2*n)]
            dmu = mm(transpose(rho), omega)
            gradient = mm(complex_i, rho)
            self.assertEqual(dmu, transpose(gradient))
            self.assertEqual(gradient, [[int(j == i)] for j in range(2*n)])
        # A compatible nondegenerate pseudo-Kahler metric need not be positive.
        metric = diagonal([1, -1, 1, -1, 1, -1, 1, -1])
        pseudo_omega = mm(metric, omega)
        self.assertEqual(mm(pseudo_omega, complex_i), metric)
        self.assertEqual(transpose(pseudo_omega), scale(-1, pseudo_omega))
        self.assertEqual(rank(metric), 8)
        self.assertEqual(metric[1][1], -1)

    def test_restricted_gram_with_target_cross_terms(self):
        jfull = [row+[0]*4 for row in eye(7)]
        retained = [2, 3, 4, 5, 7, 8, 9, 10]
        inclusion = [[int(i == j) for j in retained] for i in range(11)]
        gram = mm(transpose(jfull), jfull)
        reduced = mm(mm(transpose(inclusion), gram), inclusion)
        self.assertEqual(rank(gram), 7)
        self.assertEqual(reduced, diagonal([1]*4+[0]*4))
        q = [[F((i+1)*(j+1), 7) for j in range(7)] for i in range(7)]
        weight = add(eye(7), mm(transpose(q), q))
        jj = mm(jfull, inclusion)
        self.assertTrue(all(jj[i] == [0]*8 for i in [0, 1, 6]))
        weighted = mm(mm(transpose(jj), weight), jj)
        wmu = [[weight[i][j] for j in [2, 3, 4, 5]] for i in [2, 3, 4, 5]]
        mu = [row+[0]*4 for row in eye(4)]
        self.assertEqual(weighted, mm(mm(transpose(mu), wmu), mu))
        # With cross terms the inclusion need not be a reducing intertwiner.
        ambient = mm(mm(transpose(jfull), weight), jfull)
        self.assertNotEqual(mm(ambient, inclusion), mm(inclusion, weighted))

    def test_volume_roles_and_tangent_identity(self):
        mu, scale_r = F(1), F(2)
        dmu, dr = F(3, 5), F(-2, 7)
        volume = scale_r**2*mu
        dvolume = 2*scale_r*dr*mu+scale_r**2*dmu
        self.assertEqual(volume, 4)
        self.assertEqual(2*scale_r*dr*mu+scale_r**2*dmu-dvolume, 0)
        self.assertNotEqual(mu-volume, 0)
        # A nonconstant real scaling has a nonzero (0,1) derivative in general.
        # In the exterior basis dz1,dz2,dz3,dbarz1 it survives wedging with Omega.
        indices = [3, 0, 1, 2]
        inversions = sum(indices[i] > indices[j] for i in range(4) for j in range(i+1, 4))
        self.assertEqual((-1)**inversions, -1)

    def test_manuscript_source_and_boundary_anchors(self):
        tex = (PAPER / "main.tex").read_text(encoding="utf-8")
        bib = (PAPER / "main.bib").read_text(encoding="utf-8")
        for anchor in ["sec:string-constructor", "sec:string-mc-lift", "sec:string-calabi",
                       "sec:string-constrained-hessian", "sec:string-positivity"]:
            self.assertIn("\\label{"+anchor+"}", tex)
        for key in ["PreprojectionStringConstructor2026", "PreprojectionBCLift2026",
                    "PreprojectionCalabiRoles2026"]:
            self.assertIn(key, tex)
            self.assertIn("@misc{"+key+",", bib)
        for boundary in ["pseudo-Kahler", "not an associative dg subalgebra",
                         "25-block support", "constant-norm condition",
                         "current", "Lorentzian"]:
            self.assertIn(boundary, tex)
        self.assertIn("\\mathcal N&=i\\Psi\\wedge\\bar\\Psi", tex)


if __name__ == "__main__":
    unittest.main()
