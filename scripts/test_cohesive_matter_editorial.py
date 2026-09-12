"""Bounded editorial checks; no research worker is imported or modified."""
from fractions import Fraction as F
from pathlib import Path
import unittest

from test_cohesive_charge_editorial import add, eye, mm, scale

PAPER = Path(__file__).resolve().parents[1] / "papers" / (
    "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"
)


def transpose(a):
    return [list(c) for c in zip(*a)]


def diagonal(values):
    return [[v if i == j else 0 for j in range(len(values))]
            for i, v in enumerate(values)]


def rank(a):
    work = [list(map(F, row)) for row in a]
    r = 0
    for c in range(len(work[0])):
        pivot = next((i for i in range(r, len(work)) if work[i][c]), None)
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        divisor = work[r][c]
        work[r] = [x / divisor for x in work[r]]
        for i in range(r + 1, len(work)):
            factor = work[i][c]
            if factor:
                work[i] = [x - factor*y for x, y in zip(work[i], work[r])]
        r += 1
        if r == len(work):
            break
    return r


class MatterEditorialTests(unittest.TestCase):
    def test_index_sign_needs_grading(self):
        d = [[1, 0, 0, 0]]
        hp, hm = mm(transpose(d), d), mm(d, transpose(d))
        forward = [hp[i][i] for i in range(4)] + [hm[0][0]]
        reverse = [hm[0][0]] + [hp[i][i] for i in range(4)]
        self.assertEqual((4-rank(d))-(1-rank(d)), 3)
        self.assertEqual((1-rank(transpose(d)))-(4-rank(transpose(d))), -3)
        self.assertEqual([forward[i] for i in [0, 4, 1, 2, 3]], reverse)
        self.assertEqual(sorted(forward), sorted(reverse))
        for value in [F(1, 5), F(1, 2), F(7, 9), F(0), F(1)]:
            f = lambda x: value if x else 1
            self.assertEqual(sum(s*f(x) for s, x in zip([1]*4+[-1], forward)), 3)
            self.assertEqual(sum(s*f(x) for s, x in zip([1]+[-1]*4, reverse)), -3)

    def test_equivariant_duality_requires_canonical_character(self):
        # Synthetic degree-zero/degree-three pair with canonical character 1 mod 3.
        index = {0: 1, 1: 0, 2: -1}
        for chi in range(3):
            self.assertEqual(index[(-chi-1) % 3], -index[chi])
        self.assertNotEqual(index[0], -index[0])
        # Invariant-volume witness, duality pairs inverse characters.
        inverse_pair = {0: 0, 1: 3, 2: -3}
        for chi in range(3):
            self.assertEqual(inverse_pair[(-chi) % 3], -inverse_pair[chi])

    def test_hrr_and_adjoint_index_rows(self):
        for c3 in [-6, 0, 6]:
            ch = [F(3), F(0), F(-2), F(c3, 2)]
            dual = [(-1)**i*x for i, x in enumerate(ch)]
            end_top = sum(ch[i]*dual[3-i] for i in range(4))
            self.assertEqual(end_top, 0)
            self.assertEqual(dual[3], -ch[3])
        self.assertEqual(F(6, 2), 3)
        self.assertEqual(sum([3, 8, 8, 80, 3]), 102)

    def test_projector_resolution_and_chain_lift(self):
        charges = [F(1)]*16 + [F(-2)]*10 + [F(4)]
        projectors = [
            [-(q+2)*(q-4)/9 for q in charges],
            [(q-1)*(q-4)/18 for q in charges],
            [(q-1)*(q+2)/18 for q in charges],
        ]
        self.assertEqual([sum(p) for p in projectors], [16, 10, 1])
        for j in range(27):
            self.assertEqual(sum(p[j] for p in projectors), 1)
            for a in range(3):
                self.assertEqual(projectors[a][j]**2, projectors[a][j])
                for b in range(a):
                    self.assertEqual(projectors[a][j]*projectors[b][j], 0)
        # D_base=(1,0,0,0), tensored with all 27 representation directions.
        d = [[int(col == row) for col in range(108)] for row in range(27)]
        for p in projectors:
            for row in range(27):
                for col in range(108):
                    self.assertEqual(d[row][col]*p[col % 27], p[row]*d[row][col])
        # Mixing the 16 and 10 directions violates this chain condition.
        self.assertNotEqual(projectors[0][0], projectors[0][16])

    def test_net_actual_counts_and_rank_deficiency(self):
        for mirrors in range(83):
            kplus, kminus = mirrors+3, mirrors
            self.assertEqual(kplus-kminus, 3)
            self.assertEqual(16*(kplus+kminus), 48+32*mirrors)
            self.assertEqual(16*(kplus+kminus) == 48, mirrors == 0)
            r = 82-mirrors
            self.assertEqual(16*((82-r)+(85-r)), 48+32*mirrors)

    def test_equivariant_higgs_rank_and_scalar_obstruction(self):
        dimensions = [3, 3, 2, 2, 1]
        family_diagonals = [[1, 1, 1], [1, 1, 1], [0, 1, 1],
                            [1, 1, 1], [1, 1, 1]]
        full = [x for m, n in zip(family_diagonals, dimensions) for x in m for _ in range(n)]
        self.assertEqual((len(full), sum(full), full.count(0)), (33, 31, 2))
        for m, n in zip(family_diagonals, dimensions):
            h = diagonal([x for x in m for _ in range(n)])
            for a in range(n):
                for b in range(n):
                    g = [[int(i//n == j//n and i % n == a and j % n == b)
                          for j in range(3*n)] for i in range(3*n)]
                    self.assertEqual(mm(h, g), mm(g, h))
        for scalar in [F(0), F(1), F(2), F(1, 3)]:
            self.assertIn(3-rank(scale(scalar, eye(3))), [0, 3])

    def test_single_conjugate_mass_map_has_equal_normal_ranks(self):
        for b in [[[0, 0, 0], [0, 1, 2], [0, 0, 1]],
                  [[1, 2, 0], [0, 1, 0], [0, 0, 3]],
                  [[0, 0, 0]]*3]:
            left, right = mm(transpose(b), b), mm(b, transpose(b))
            self.assertEqual(rank(left), rank(right))
            self.assertEqual(rank(left), rank(b))
            self.assertNotEqual((rank(left), rank(right)), (2, 3))

    def test_k3_matter_curve_and_ordinary_section_bound(self):
        h2, eta, line_multiple = 2, 9, 5
        genus = 1 + eta*eta*h2//2
        degree_h = eta*h2
        zlength = sum([3, 3, 6])
        degree = line_multiple*degree_h-zlength
        sections = 2+line_multiple**2*h2//2
        self.assertEqual((genus, degree_h, zlength, degree, sections), (82, 18, 12, 78, 27))
        lower_h0 = sections-zlength
        chi = degree+1-genus
        lower_h1 = lower_h0-chi
        self.assertEqual((chi, lower_h0, lower_h1), (-3, 15, 18))
        self.assertEqual(16*(lower_h0+lower_h1), 528)
        self.assertEqual(genus-degree, 4)

    def test_evaluation_map_rank_and_explicit_nonselection(self):
        # Auxiliary rational witnesses, never selected geometric evaluations.
        good = eye(82) + [[F(1)]*82, [F(j) for j in range(82)], [F(j*j) for j in range(82)]]
        bad = [row[:81]+[F(0)] for row in good]
        for matrix, expected_rank in [(good, 82), (bad, 81)]:
            r = rank(matrix)
            self.assertEqual(r, expected_rank)
            self.assertEqual((len(matrix), len(matrix[0])), (85, 82))
            self.assertEqual((82-r)-(85-r), -3)
            self.assertEqual(16*((82-r)+(85-r)), 48+32*(82-r))
        self.assertEqual(rank(good[:82]), 82)
        self.assertEqual(rank(bad[:82]), 81)
        self.assertEqual((78+85, 2*82-2, 78+85+1-82), (163, 162, 82))

    def test_cartier_intersection_and_derived_shift(self):
        # Degree-bounded source and one-higher target, not an Artinian quotient.
        multiplication = [[int(i == j+1) for j in range(6)] for i in range(7)]
        self.assertEqual(rank(multiplication), 6)
        self.assertEqual((6-rank(multiplication), 7-rank(multiplication)), (0, 1))
        at_origin = [[0]]
        self.assertEqual((1-rank(at_origin), 1-rank(at_origin)), (1, 1))
        for a, b in [(0, 3), (15, 18), (1, 4)]:
            shifted = [0, a, b, 0]
            self.assertEqual(sum((-1)**i*h for i, h in enumerate(shifted)), -(a-b))
            self.assertEqual(shifted[2]-shifted[1], 3)

    def test_contextual_scope_is_in_manuscript(self):
        text = (PAPER / "main.tex").read_text(encoding="utf-8")
        for anchor in ["matter-index-theta", "matter-index-first", "matter-projector-lift",
                       "matter-exotic-ranks", "matter-bht-localization",
                       "matter-graph-prym", "matter-theta-test"]:
            self.assertIn(r"\label{sec:"+anchor+"}", text)
        for phrase in ["invariant holomorphic volume form", "equal rank",
                       "right-handed-neutrino slot", "not a weak-angle",
                       "uncorrected ordinary representative", "not a new selection of a time arrow"]:
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
