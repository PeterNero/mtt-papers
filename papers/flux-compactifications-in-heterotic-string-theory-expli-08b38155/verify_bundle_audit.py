"""Exact standard-library checks for the Iwasawa bundle audit."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


class Laurent:
    """A Laurent polynomial in t with rational coefficients."""

    def __init__(self, terms=None):
        self.terms = {
            int(power): Fraction(value)
            for power, value in (terms or {}).items()
            if value
        }

    @classmethod
    def monomial(cls, coefficient=1, power=0):
        return cls({power: Fraction(coefficient)})

    def __add__(self, other):
        other = as_laurent(other)
        terms = dict(self.terms)
        for power, value in other.terms.items():
            terms[power] = terms.get(power, Fraction(0)) + value
        return Laurent(terms)

    def __neg__(self):
        return Laurent({power: -value for power, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-as_laurent(other))

    def __mul__(self, other):
        other = as_laurent(other)
        terms = {}
        for left_power, left_value in self.terms.items():
            for right_power, right_value in other.terms.items():
                power = left_power + right_power
                terms[power] = terms.get(power, Fraction(0)) + (
                    left_value * right_value
                )
        return Laurent(terms)

    def __eq__(self, other):
        return self.terms == as_laurent(other).terms

    def __repr__(self):
        return repr(self.terms)


def as_laurent(value):
    return value if isinstance(value, Laurent) else Laurent.monomial(value)


ZERO = Laurent()
ONE = Laurent.monomial()
T = Laurent.monomial(1, 1)
T2 = Laurent.monomial(1, 2)


def zero_matrix():
    return [[ZERO for _ in range(3)] for _ in range(3)]


def matrix_unit(row, column, coefficient=ONE):
    matrix = zero_matrix()
    matrix[row - 1][column - 1] = as_laurent(coefficient)
    return matrix


def matrix_add(left, right):
    return [
        [left[i][j] + right[i][j] for j in range(3)]
        for i in range(3)
    ]


def matrix_scale(value, matrix):
    return [
        [as_laurent(value) * matrix[i][j] for j in range(3)]
        for i in range(3)
    ]


def matrix_multiply(left, right):
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(3)),
                ZERO,
            )
            for j in range(3)
        ]
        for i in range(3)
    ]


def commutator(left, right):
    return matrix_add(
        matrix_multiply(left, right),
        matrix_scale(-1, matrix_multiply(right, left)),
    )


def diagonal(entries):
    matrix = zero_matrix()
    for index, entry in enumerate(entries):
        matrix[index][index] = as_laurent(entry)
    return matrix


def is_zero_matrix(matrix):
    return all(entry == ZERO for row in matrix for entry in row)


def matrix_equal(left, right):
    return all(
        left[i][j] == right[i][j]
        for i in range(3)
        for j in range(3)
    )


def rational_rank(rows):
    matrix = [
        [Fraction(value) for value in row]
        for row in rows
        if any(value for value in row)
    ]
    rank = 0
    column_count = len(matrix[0]) if matrix else 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                matrix[row][entry] - factor * matrix[rank][entry]
                for entry in range(column_count)
            ]
        rank += 1
    return rank


def commutant_nullity(generators):
    equations = []
    for generator in generators:
        for out_row in range(3):
            for out_column in range(3):
                equation = [Fraction(0) for _ in range(9)]
                for source in range(3):
                    equation[out_row * 3 + source] += generator[source][out_column]
                    equation[source * 3 + out_column] -= generator[out_row][source]
                equations.append(equation)
    return 9 - rational_rank(equations)


def integer_unit(row, column):
    matrix = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    matrix[row - 1][column - 1] = Fraction(1)
    return matrix


def main():
    e11 = matrix_unit(1, 1)
    e12 = matrix_unit(1, 2)
    e13 = matrix_unit(1, 3)
    e31 = matrix_unit(3, 1)
    e32 = matrix_unit(3, 2)
    e33 = matrix_unit(3, 3)

    old_b1 = matrix_scale(T, e13)
    old_b2 = matrix_scale(-T, e31)
    b3 = matrix_scale(T2, e12)
    old_residual = matrix_add(b3, commutator(old_b1, old_b2))
    expected_old = matrix_scale(
        T2,
        matrix_add(e12, matrix_add(matrix_scale(-1, e11), e33)),
    )

    repaired_b1 = matrix_scale(T, e13)
    repaired_b2 = matrix_scale(-T, e32)
    repaired_residual = matrix_add(
        b3,
        commutator(repaired_b1, repaired_b2),
    )

    g = diagonal([T, Laurent.monomial(1, -1), ONE])
    g_inverse = diagonal([Laurent.monomial(1, -1), T, ONE])
    base_b1 = e13
    base_b2 = matrix_scale(-1, e32)
    base_b3 = e12

    integer_generators = [
        integer_unit(1, 3),
        [[-value for value in row] for row in integer_unit(3, 2)],
        integer_unit(1, 2),
    ]
    nullity = commutant_nullity(integer_generators)

    checks = {
        "printed_residual_is_exact_expected_nonzero": (
            matrix_equal(old_residual, expected_old)
            and not is_zero_matrix(old_residual)
        ),
        "repaired_maurer_cartan_residual_vanishes": is_zero_matrix(
            repaired_residual
        ),
        "B1_complex_gauge_identity": matrix_equal(
            repaired_b1,
            matrix_multiply(matrix_multiply(g, base_b1), g_inverse),
        ),
        "B2_complex_gauge_identity": matrix_equal(
            repaired_b2,
            matrix_multiply(matrix_multiply(g, base_b2), g_inverse),
        ),
        "B3_complex_gauge_identity": matrix_equal(
            b3,
            matrix_multiply(matrix_multiply(g, base_b3), g_inverse),
        ),
        "holomorphic_commutant_dimension_is_two": nullity == 2,
    }
    report = {
        "schema": "mtt.paper.bundle-audit.v1",
        "arithmetic": "exact rational Laurent polynomials",
        "checks": checks,
        "commutant_dimension": nullity,
        "passed": all(checks.values()),
    }
    output_path = Path(__file__).with_name("bundle_audit_report.json")
    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
