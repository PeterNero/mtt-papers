"""Finite examples for the ontology companion, not MTT source promotion.

Run with: python -B check_ontology_examples_v1.py
Reuses only the adjacent explanatory matrix helpers. No network or simulation
jobs. Rational circuit examples are exact; the Fourier and exponential
examples are floating-point checks, not symbolic proofs of general theorems.
"""

from collections import Counter
import cmath
from fractions import Fraction as F
from math import exp, isclose, pi, sqrt
import unittest

from check_explanatory_examples_v2 import (
    I, PL, PLUS, MINUS, MIX, W, add, apply, kron, matmul, outer, scale,
    trace, trace_out_a, trace_out_b,
)


CNOT = ((1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0))
BELL = scale(F(1, 2), outer((1, 0, 0, 1)))
RECORD_MIX = ((F(1, 2), 0, 0, 0),
              (0, 0, 0, 0),
              (0, 0, 0, 0),
              (0, 0, 0, F(1, 2)))


def cnot_gate(qubits, control, target):
    """Exact basis permutation; qubit zero is the most significant bit."""
    n = 2 ** qubits
    c, t = 1 << (qubits - control - 1), 1 << (qubits - target - 1)
    permutation = [j ^ t if j & c else j for j in range(n)]
    return tuple(tuple(int(i == permutation[j]) for j in range(n))
                 for i in range(n))


def discard_last_qubit(rho):
    n = len(rho) // 2
    return tuple(tuple(sum(rho[2 * i + b][2 * j + b] for b in range(2))
                       for j in range(n)) for i in range(n))


class OntologyExamples(unittest.TestCase):
    def test_01_reversible_memory_coupling(self):
        self.assertEqual(matmul(CNOT, CNOT), kron(I, I))
        self.assertEqual(apply(CNOT, kron(PLUS, PL)), BELL)

    def test_02_identical_pointer_marginals_not_identical_states(self):
        self.assertEqual(trace_out_a(BELL), MIX)
        self.assertEqual(trace_out_a(RECORD_MIX), MIX)
        self.assertEqual(trace(matmul(kron(PL, PL), BELL)), F(1, 2))
        self.assertEqual(trace(matmul(kron(PL, PL), RECORD_MIX)), F(1, 2))
        self.assertNotEqual(BELL, RECORD_MIX)

    def test_03_wigner_coherence_distinguishes_mixture(self):
        self.assertEqual(trace(matmul(BELL, BELL)), 1)
        self.assertEqual(trace(matmul(BELL, RECORD_MIX)), F(1, 2))

    def test_04_readout_and_coherence_projectors_incompatible(self):
        pointer_zero = kron(I, PL)
        self.assertNotEqual(matmul(pointer_zero, BELL),
                            matmul(BELL, pointer_zero))

    def test_05_undo_without_external_copy(self):
        restored = apply(CNOT, BELL)
        self.assertEqual(restored, kron(PLUS, PL))
        self.assertEqual(trace_out_a(restored), PL)
        self.assertEqual(trace(matmul(kron(PLUS, I), restored)), 1)
        collapsed_restored = apply(CNOT, RECORD_MIX)
        self.assertEqual(trace(matmul(kron(PLUS, I), collapsed_restored)),
                         F(1, 2))

    def test_06_external_record_removes_reduced_coherence(self):
        copy_record = cnot_gate(3, 1, 2)
        state = apply(copy_record, kron(BELL, PL))
        self.assertEqual(discard_last_qubit(state), RECORD_MIX)
        self.assertEqual(trace(matmul(kron(BELL, I), state)), F(1, 2))

    def test_07_undo_sf_alone_does_not_erase_external_record(self):
        copy_record = cnot_gate(3, 1, 2)
        undo_sf = cnot_gate(3, 0, 1)
        state = apply(copy_record, kron(BELL, PL))
        reversed_sf = apply(undo_sf, state)
        self.assertEqual(trace(matmul(kron(kron(PLUS, I), I), reversed_sf)),
                         F(1, 2))
        # The friend's bit is reset, but the external record still correlates
        # with S, so S alone remains maximally mixed.
        self.assertEqual(discard_last_qubit(reversed_sf), kron(MIX, PL))
        self.assertEqual(trace(matmul(kron(kron(PL, I), PL), reversed_sf)),
                         F(1, 2))

    def test_08_reversing_all_copies_restores_interference(self):
        copy_record = cnot_gate(3, 1, 2)
        undo_sf = cnot_gate(3, 0, 1)
        initial = kron(kron(PLUS, PL), PL)
        measured = apply(undo_sf, initial)
        copied = apply(copy_record, measured)
        restored = apply(undo_sf, apply(copy_record, copied))
        self.assertEqual(restored, initial)
        self.assertEqual(trace(matmul(kron(kron(PLUS, I), I), restored)), 1)

    def test_09_partial_record_overlap_visibility(self):
        for overlap, orthogonal in ((F(0), F(1)), (F(4, 5), F(3, 5)),
                                    (F(-4, 5), F(3, 5)),
                                    (F(1), F(0)), (F(-1), F(0))):
            # Equal SF branches; E0=|0>, E1=overlap|0>+orthogonal|1>.
            vector = (1, 0, 0, 0, 0, 0, overlap, orthogonal)
            state = scale(F(1, 2), outer(vector))
            self.assertEqual(trace(state), 1)
            reduced = discard_last_qubit(state)
            self.assertEqual(trace(matmul(BELL, reduced)), (1 + overlap) / 2)

    def test_10_canonical_checkpoint_single_label_partition(self):
        labels = ["ready" if atom == 0 else "P" if atom <= 149 else "Q"
                  for atom in range(448)]
        counts = Counter(labels)
        self.assertEqual(counts, {"ready": 1, "P": 149, "Q": 298})
        probabilities = {label: F(n, 448) for label, n in counts.items()}
        self.assertEqual(sum(probabilities.values()), 1)
        self.assertEqual(probabilities["Q"], F(149, 224))
        self.assertEqual(F(counts["P"], counts["P"] + counts["Q"]), F(1, 3))

    def test_11_world_count_from_coefficients_is_basis_dependent(self):
        root = cmath.exp(2j * pi / 3)
        dft = tuple(tuple(root ** (j * k) / sqrt(3) for k in range(3))
                    for j in range(3))
        column = [row[0] for row in dft]
        self.assertEqual(sum(abs(x) > 1e-12 for x in (1, 0, 0)), 1)
        self.assertEqual(sum(abs(x) > 1e-12 for x in column), 3)
        self.assertTrue(isclose(sum(abs(x) ** 2 for x in column), 1))
        identity = matmul(tuple(tuple(dft[j][i].conjugate() for j in range(3))
                                for i in range(3)), dft)
        for i in range(3):
            for j in range(3):
                self.assertLess(abs(identity[i][j] - int(i == j)), 1e-12)

    def test_12_same_density_has_different_ensemble_descriptions(self):
        self.assertEqual(scale(F(1, 2), add(PLUS, MINUS)), MIX)
        self.assertEqual(scale(F(1, 2), add(PL, ((0, 0), (0, 1)))), MIX)
        self.assertEqual(scale(F(1, 2), apply(W, MIX)), MIX)

    def test_13_poisson_race_normalization_given_primitive(self):
        weights = (F(1, 6), F(1, 3), F(1, 2))
        for total_rate in (F(3), F(12), F(15)):
            rates = tuple(total_rate * r for r in weights)
            self.assertEqual(sum(rates), total_rate)
            self.assertEqual(tuple(rate / sum(rates) for rate in rates),
                             weights)
        gamma, t = 2, 3
        survival = exp(-gamma * t)
        masses = [(1 - survival) * r for r in weights]
        self.assertAlmostEqual(survival + sum(masses), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
