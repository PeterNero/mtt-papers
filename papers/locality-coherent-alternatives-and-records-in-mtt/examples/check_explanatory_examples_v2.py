"""Small quantum examples for the v2 explanatory note, not MTT source proofs.

Uses only the standard library. Rational examples use Fraction; the complex
phase, rotation and Zeno examples use floating-point checks at stated tolerance.
No network, file writes, jobs, random sampling or research-repository imports.
"""

import cmath
from fractions import Fraction as F
from itertools import product
from math import cos, pi, sin, sqrt
import unittest


def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(*matrices):
    return tuple(tuple(sum(a[i][j] for a in matrices)
                       for j in range(len(matrices[0][0])))
                 for i in range(len(matrices[0])))


def scale(c, a):
    return tuple(tuple(c * v for v in row) for row in a)


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def outer(v):
    return tuple(tuple(x * y.conjugate() for y in v) for x in v)


def apply(k, rho):
    return matmul(matmul(k, rho), dagger(k))


def channel(kraus, rho):
    return add(*(apply(k, rho) for k in kraus))


def kron(a, b):
    return tuple(tuple(a[i][j] * b[k][l]
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def trace_out_a(rho):
    return tuple(tuple(sum(rho[2 * a + i][2 * a + j] for a in range(2))
                       for j in range(2)) for i in range(2))


def trace_out_b(rho):
    return tuple(tuple(sum(rho[2 * i + b][2 * j + b] for b in range(2))
                       for j in range(2)) for i in range(2))


I = ((1, 0), (0, 1))
PL = ((1, 0), (0, 0))
PR = ((0, 0), (0, 1))
PLUS = ((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)))
MINUS = ((F(1, 2), F(-1, 2)), (F(-1, 2), F(1, 2)))
MIX = scale(F(1, 2), I)
W = ((1, 1), (1, -1))
MARKERS = ((F(0), F(1)), (F(4, 5), F(3, 5)), (F(1), F(0)))


def marker(r, click_amplitude):
    return (((r, 0), (0, 1)), scale(click_amplitude, PL))


def recombine(rho):
    # H = W/sqrt(2), so H rho H* is rational for rational rho.
    return scale(F(1, 2), apply(W, rho))


def rotate(rho, angle):
    c, s = cos(angle / 2), sin(angle / 2)
    return apply(((c, -s), (s, c)), rho)


class ExplanatoryExamples(unittest.TestCase):
    def assertMatrixClose(self, actual, expected):
        self.assertEqual((len(actual), len(actual[0])),
                         (len(expected), len(expected[0])))
        for row, wanted in zip(actual, expected):
            for value, target in zip(row, wanted):
                self.assertLessEqual(abs(value - target), 1e-12)

    def test_01_monitor_completeness(self):
        for r, c in MARKERS:
            self.assertEqual(r * r + c * c, 1)
            self.assertEqual(add(*(matmul(dagger(k), k)
                                   for k in marker(r, c))), I)

    def test_02_populations_preserved_coherence_reduced(self):
        for rho in (PL, PR, PLUS, outer((F(3, 5), F(4, 5)))):
            for r, c in MARKERS:
                out = channel(marker(r, c), rho)
                self.assertEqual(out, ((rho[0][0], r * rho[0][1]),
                                       (r * rho[1][0], rho[1][1])))

    def test_03_right_only_state_unchanged(self):
        for r, c in MARKERS:
            self.assertEqual(channel(marker(r, c), PR), PR)
            self.assertEqual(apply(marker(r, c)[0], PR), PR)

    def test_04_balanced_output_table(self):
        self.assertEqual(recombine(PLUS), PL)
        self.assertEqual(recombine(channel(marker(F(0), F(1)), PLUS)), MIX)
        self.assertEqual(recombine(PR)[0][0], F(1, 2))
        self.assertEqual(recombine(PR)[1][1], F(1, 2))

    def test_05_partial_and_perfect_null_records(self):
        null = apply(marker(F(4, 5), F(3, 5))[0], PLUS)
        self.assertEqual(trace(null), F(41, 50))
        conditioned = scale(1 / trace(null), null)
        self.assertEqual(conditioned[0][0], F(16, 41))
        self.assertEqual(conditioned[1][1], F(25, 41))
        self.assertEqual(recombine(conditioned)[0][0], F(81, 82))
        perfect = apply(PR, PLUS)
        self.assertEqual(trace(perfect), F(1, 2))
        self.assertEqual(scale(1 / trace(perfect), perfect), PR)

    def test_06_absorption_and_qnd_differ(self):
        rho3 = tuple(tuple(PLUS[i][j] if i < 2 and j < 2 else 0
                           for j in range(3)) for i in range(3))
        for r, c in MARKERS:
            no_absorption = ((r, 0, 0), (0, 1, 0), (0, 0, 1))
            absorption = ((0, 0, 0), (0, 0, 0), (c, 0, 0))
            out = channel((no_absorption, absorption), rho3)
            self.assertEqual(trace(out), 1)
            self.assertEqual(out[2][2], c * c / 2)
            surviving = tuple(tuple(out[i][j] for j in range(2))
                              for i in range(2))
            ports = recombine(surviving)
            self.assertEqual(ports[0][0], (1 + r) ** 2 / 4)
            self.assertEqual(ports[1][1], (1 - r) ** 2 / 4)
            qnd = recombine(channel(marker(r, c), PLUS))
            self.assertEqual(qnd[0][0] - ports[0][0], c * c / 4)
            self.assertEqual(qnd[1][1] - ports[1][1], c * c / 4)

    def test_07_eraser_subsets_sum_to_mixture(self):
        self.assertEqual(scale(F(1, 2), add(PLUS, MINUS)), MIX)
        self.assertEqual(recombine(PLUS), PL)
        self.assertEqual(recombine(MINUS), PR)
        self.assertEqual(recombine(MIX), MIX)

    def test_08_complex_marker_overlap_convention(self):
        alpha, beta, phi = 3 / 5, 4 / 5, 0.7
        gamma = 0.3 + 0.4j
        phased_beta = beta * cmath.exp(1j * phi)
        joint = outer((alpha, 0, phased_beta * gamma,
                       phased_beta * sqrt(1 - abs(gamma) ** 2)))
        path = trace_out_b(joint)
        expected = alpha * phased_beta.conjugate() * gamma.conjugate()
        self.assertAlmostEqual(abs(path[0][1] - expected), 0, places=12)
        p_plus = trace(matmul(PLUS, path)).real
        self.assertAlmostEqual(p_plus, 0.5 + (alpha * phased_beta * gamma).real)

    def test_09_independent_system_conditioning(self):
        rho_b = outer((F(3, 5), F(4, 5)))
        joint = kron(PLUS, rho_b)
        for k in marker(F(4, 5), F(3, 5)):
            branch = apply(kron(k, I), joint)
            self.assertEqual(scale(1 / trace(branch), trace_out_a(branch)),
                             rho_b)

    def test_10_entangled_remote_marginal(self):
        singlet = ((0, 0, 0, 0),
                   (0, F(1, 2), F(-1, 2), 0),
                   (0, F(-1, 2), F(1, 2), 0),
                   (0, 0, 0, 0))
        for r, c in MARKERS:
            out = channel(tuple(kron(k, I) for k in marker(r, c)), singlet)
            self.assertEqual(trace_out_a(out), MIX)
        conditional = apply(kron(PL, I), singlet)
        self.assertEqual(scale(1 / trace(conditional),
                               trace_out_a(conditional)), PR)

    def test_11_forward_x_disturbance(self):
        self.assertEqual(channel((PLUS, MINUS), PL), MIX)
        self.assertEqual(trace(matmul(PL, PL)), 1)
        self.assertEqual(trace(matmul(PL, MIX)), F(1, 2))

    def test_12_future_instrument_does_not_change_past_marginal(self):
        rho = outer((F(3, 5), F(4, 5)))
        future_instruments = ((PL, PR), (PLUS, MINUS),
                              marker(F(4, 5), F(3, 5)))
        for earlier in marker(F(4, 5), F(3, 5)):
            branch = apply(earlier, rho)
            propagated = recombine(branch)
            for future in future_instruments:
                self.assertEqual(trace(channel(future, propagated)),
                                 trace(branch))

    def test_13_lg_common_joint_bound(self):
        values = {a * b + b * c - a * c for a, b, c in
                  product((-1, 1), repeat=3)}
        self.assertEqual(values, {-3, 1})

    def test_14_lg_pair_and_triple_protocols(self):
        projectors = (PL, PR)
        labels = (1, -1)
        theta = pi / 3

        def pair_correlation(angle):
            return sum(a * b * trace(apply(pb, rotate(apply(pa, MIX), angle)))
                       for a, pa in zip(labels, projectors)
                       for b, pb in zip(labels, projectors))

        c12 = pair_correlation(theta)
        c13_without_middle = pair_correlation(2 * theta)
        self.assertAlmostEqual(2 * c12 - c13_without_middle, 1.5)
        c13_with_middle = 0
        total = 0
        for a, pa in zip(labels, projectors):
            for pb in projectors:
                for c, pc in zip(labels, projectors):
                    after_b = apply(pb, rotate(apply(pa, MIX), theta))
                    probability = trace(apply(pc, rotate(after_b, theta)))
                    total += probability
                    c13_with_middle += a * c * probability
        self.assertAlmostEqual(total, 1)
        self.assertAlmostEqual(c13_with_middle, 0.25)
        self.assertAlmostEqual(2 * c12 - c13_with_middle, 0.75)

    def test_15_independent_bin_count(self):
        n, p = 8, F(2, 5)
        mean = variance = F(0)
        for outcomes in product((0, 1), repeat=n):
            count = sum(outcomes)
            probability = p ** count * (1 - p) ** (n - count)
            mean += count * probability
            variance += (count - n * p) ** 2 * probability
        self.assertEqual(mean, n * p)
        self.assertEqual(variance, n * p * (1 - p))

    def test_16_number_state_second_order_correlation(self):
        for n in range(1, 10):
            self.assertEqual(F(n * (n - 1), n * n), 1 - F(1, n))

    def test_17_zeno_example(self):
        omega_t = pi
        survival = lambda n: cos(omega_t / (2 * n)) ** (2 * n)
        self.assertAlmostEqual(survival(1), 0)
        self.assertGreater(survival(1000), survival(10))
        self.assertGreater(survival(1000), 0.997)

    def test_18_classical_chsh_bound(self):
        values = {a0 * (b0 + b1) + a1 * (b0 - b1)
                  for a0, a1, b0, b1 in product((-1, 1), repeat=4)}
        self.assertEqual(values, {-2, 2})


if __name__ == "__main__":
    unittest.main(verbosity=2)
