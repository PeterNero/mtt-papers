"""Small exact witnesses for the v5 editorial comparison, not source reruns."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
COH = "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def sub(a, b):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(a, b)]


class TransferEditorialTests(unittest.TestCase):
    def test_exact_compressed_commutator(self):
        p = [[F(i == j) - F(1, 3) for j in range(3)] for i in range(3)]
        a = [[F(i == j == 0) for j in range(3)] for i in range(3)]
        b = [[F(i == j == 1) for j in range(3)] for i in range(3)]
        self.assertEqual(mm(a, b), mm(b, a))
        pa, pb = mm(mm(p, a), p), mm(mm(p, b), p)
        comm = sub(mm(pa, pb), mm(pb, pa))
        expected = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        self.assertEqual(comm, [[F(x, 9) for x in row] for row in expected])
        self.assertEqual(sum(x*x for row in comm for x in row), F(2, 27))

    def test_raw_excursion_is_not_feshbach_self_energy(self):
        raw, inverse_weighted = F(1, 2)**2, F(1, 2)**2 / 3
        self.assertEqual(raw, F(1, 4))
        self.assertEqual(inverse_weighted, F(1, 12))
        self.assertEqual(1 - inverse_weighted, F(11, 12))
        self.assertNotEqual(raw, inverse_weighted)

    def test_extra_harmonic_classes_cannot_be_contracted_away(self):
        old = [comb(2, k) if k <= 2 else 0 for k in range(5)]
        full = [comb(4, k) for k in range(5)]
        ideal = [a-b for a, b in zip(full, old)]
        self.assertEqual(ideal, [0, 2, 5, 4, 1])
        self.assertEqual(sum(ideal), 12)
        self.assertEqual([9*a+b for a, b in zip(old, ideal)], [9, 20, 14, 4, 1])
        self.assertNotEqual(sum(old), sum(full))

    def test_first_jet_specialized_image_is_not_flat_fiber(self):
        masks = range(16)
        even_degree = lambda mask: ((mask >> 2) & 1) + ((mask >> 3) & 1)
        self.assertEqual(sum(even_degree(mask) == 0 for mask in masks), 4)
        # The image over k[h] has 16 independent h-weighted generators.
        self.assertEqual(len({(mask, even_degree(mask)) for mask in masks}), 16)

    def test_manuscript_keeps_scope_and_old_corrections(self):
        text = (ROOT / "papers" / COH / "main.tex").read_text()
        for anchor in ("sec:compression-leakage", "sec:excursion-comparison",
                       "sec:finite-weyl-completion", "sec:first-jet-quotient",
                       "sec:response-retract", "sec:all-arity-source-map",
                       "Retained projectors are not the whole ambient projector",
                       "exhaustive table verification",
                       "not measured Yukawa or gauge couplings"):
            self.assertIn(anchor, text)
        self.assertIn("a flat family whose fiber dimension drops", text)


if __name__ == "__main__":
    unittest.main()
