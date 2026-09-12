"""Small exact examples only; this is not independent source-theorem verification."""

from fractions import Fraction as F
from itertools import permutations, product
import math
import unittest


def transpose(a):
    return list(map(list, zip(*a)))


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


class EditorialExamples(unittest.TestCase):
    def test_projector_ranks(self):
        p = [[F(1, 3) if i // 3 == j // 3 else F(0) for j in range(6)] for i in range(6)]
        self.assertEqual(mul(p, p), p)
        self.assertEqual(sum(p[i][i] for i in range(6)), 2)
        self.assertEqual(6 - sum(p[i][i] for i in range(6)), 4)

    def test_checkpoint_normalization(self):
        weights = [F(n, 448) for n in (1, 149, 298)]
        self.assertEqual(sum(weights), 1)
        self.assertEqual(weights[1] / (1 - weights[0]), F(1, 3))
        self.assertEqual(weights[2] / (1 - weights[0]), F(2, 3))

    def test_no_count_amplitude_effect(self):
        gamma = math.log(448)
        self.assertAlmostEqual(math.exp(-gamma / 2) ** 2, 1 / 448)
        self.assertNotAlmostEqual(math.exp(-gamma) ** 2, 1 / 448)

    def test_grid_semigroup(self):
        c2 = F(7, 25)
        self.assertEqual(c2 ** 3 * c2 ** 2, c2 ** 5)
        self.assertEqual(c2 + (1 - c2) * F(1, 3) + (1 - c2) * F(2, 3), 1)

    def test_hessian_projector_square_root(self):
        p = [[F(1, 3)] * 3 for _ in range(3)]
        q = [[F(i == j) - p[i][j] for j in range(3)] for i in range(3)]
        self.assertEqual(mul(q, q), q)
        self.assertEqual(mul([[3 * x for x in row] for row in q],
                             [[3 * x for x in row] for row in q]),
                         [[9 * x for x in row] for row in q])

    def test_equal_clock_condition(self):
        p_rate, q_rate = F(2), F(3)
        self.assertNotEqual(p_rate * 1 + q_rate * 0, p_rate * 0 + q_rate * 1)

    def test_fourth_moment_is_not_output_effect(self):
        self.assertEqual((F(1) + F(0)) / 2, F(1, 2))
        self.assertEqual((F(1, 2) + F(1, 2)) / 2, F(1, 2))
        self.assertNotEqual((F(1) ** 2 + F(0) ** 2) / 2, F(1, 2) ** 2)

    def test_nonselective_purity(self):
        self.assertEqual(F(1, 3) ** 2 + F(2, 3) ** 2, F(5, 9))
        self.assertLess(F(2, 3), 1)

    def test_fourier_cutoff_loss(self):
        self.assertEqual(F(3, 5) ** 2 + F(4, 5) ** 2, 1)
        self.assertEqual(1 - F(3, 5) ** 2, F(16, 25))

    def test_feshbach_coefficient(self):
        self.assertEqual(1 - F(1, 2) ** 2 / 3, F(11, 12))

    def test_support_ranks(self):
        ranks = [3 + sum(mask) for mask in product((0, 1), repeat=3)]
        self.assertEqual([ranks.count(i) for i in range(3, 7)], [1, 3, 3, 1])

    def test_boundary_linear_cost(self):
        t = F(2, 3)
        r = t * t
        self.assertEqual(t * t / 2, r / 2)
        self.assertNotEqual(t * t / 2, r * r / 2)

    def test_s3_deck_centralizer(self):
        group = list(permutations(range(3)))
        comp = lambda a, b: tuple(a[b[i]] for i in range(3))
        centralizer = [g for g in group if all(comp(g, h) == comp(h, g) for h in group)]
        self.assertEqual(centralizer, [(0, 1, 2)])

    def test_shared_root_restriction(self):
        self.assertEqual([(33 * x - x) % 64 for x in (0, 16, 32, 48)], [0] * 4)

    def test_c4_covariance_condition(self):
        j = [[0, -1], [1, 0]]
        for a, b, c in product(range(-2, 3), repeat=3):
            m = [[a, c], [c, b]]
            self.assertEqual(mul(m, j) == mul(j, m), a == b and c == 0)

    def test_quasifree_mixture_counterexample(self):
        occupations = [(F(1, 2), 0, 0), (F(1, 2), 1, 1)]
        n1 = sum(p * a for p, a, b in occupations)
        n2 = sum(p * b for p, a, b in occupations)
        joint = sum(p * a * b for p, a, b in occupations)
        self.assertEqual(joint, F(1, 2))
        self.assertEqual(n1 * n2, F(1, 4))
        self.assertNotEqual(joint, n1 * n2)

    def test_flat_completion_at_one(self):
        self.assertEqual(F(1, 2), F(1, 2) * F(math.exp(0)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
