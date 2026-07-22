"""Exact finite checks for the Penrose--Schoenberg completion theorem.

The paper contains the general proof.  This verifier checks its algebraic core on
an exact finite Poisson model and then stress-tests the resulting Schur kernels.
No measured masses, collapse rates, Newton constant, or smearing length are used.
"""

from __future__ import annotations

import math

import numpy as np
import sympy as sp


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return a * b - b * a


def exact_poisson_energy_check() -> tuple[sp.Matrix, list[sp.Matrix]]:
    # A positive finite Laplacian analogue.  K=L^{-1} is the Green kernel.
    laplacian = sp.Matrix(
        [
            [3, -1, 0],
            [-1, 3, -1],
            [0, -1, 2],
        ]
    )
    assert laplacian.is_positive_definite
    green = laplacian.inv()

    densities = [
        sp.Matrix([0, 0, 0]),
        sp.Matrix([1, 0, 0]),
        sp.Matrix([0, 2, 0]),
        sp.Matrix([1, -1, 2]),
    ]
    potentials = [green * mu for mu in densities]

    for a in range(len(densities)):
        for b in range(len(densities)):
            delta_mu = densities[a] - densities[b]
            delta_u = potentials[a] - potentials[b]
            source_energy = (delta_mu.T * green * delta_mu)[0] / 2
            field_energy = (delta_u.T * laplacian * delta_u)[0] / 2
            assert sp.simplify(source_energy - field_energy) == 0
            assert source_energy >= 0

    return green, densities


def energy_matrix(green: sp.Matrix, densities: list[sp.Matrix]) -> sp.Matrix:
    n = len(densities)
    return sp.Matrix(
        n,
        n,
        lambda a, b: sp.simplify(
            ((densities[a] - densities[b]).T
             * green
             * (densities[a] - densities[b]))[0]
            / 2
        ),
    )


def exact_cnd_check(energy: sp.Matrix, green: sp.Matrix, densities: list[sp.Matrix]) -> None:
    c1, c2, c3 = sp.symbols("c1 c2 c3", real=True)
    coeffs = sp.Matrix([-(c1 + c2 + c3), c1, c2, c3])
    weighted_density = sum(
        (coeffs[a] * densities[a] for a in range(len(densities))),
        sp.zeros(densities[0].rows, 1),
    )

    cnd_form = (coeffs.T * energy * coeffs)[0]
    squared_norm = (weighted_density.T * green * weighted_density)[0]
    assert sp.simplify(cnd_form + squared_norm) == 0

    # Independent symbolic identity for arbitrary points in a two-dimensional
    # Hilbert space.  This guards against the numerical example doing the work.
    x = sp.symbols("x0:6", real=True)
    r = [sp.Matrix(x[0:2]), sp.Matrix(x[2:4]), sp.Matrix(x[4:6])]
    q1, q2 = sp.symbols("q1 q2", real=True)
    q = sp.Matrix([-(q1 + q2), q1, q2])
    distances = sp.Matrix(
        3,
        3,
        lambda a, b: ((r[a] - r[b]).dot(r[a] - r[b])) / 2,
    )
    weighted_r = sum((q[a] * r[a] for a in range(3)), sp.zeros(2, 1))
    assert sp.expand((q.T * distances * q)[0] + weighted_r.dot(weighted_r)) == 0


def exact_dp_generator_check(energy: sp.Matrix, green: sp.Matrix, densities: list[sp.Matrix]) -> None:
    n = len(densities)
    rho_symbols = sp.symbols(f"rho0:{n*n}")
    rho = sp.Matrix(n, n, rho_symbols)
    mass_operators = [
        sp.diag(*(densities[a][j] for a in range(n)))
        for j in range(densities[0].rows)
    ]

    generator = sp.zeros(n)
    for i, mass_i in enumerate(mass_operators):
        for j, mass_j in enumerate(mass_operators):
            generator -= green[i, j] * commutator(
                mass_i, commutator(mass_j, rho)
            ) / 2

    expected = sp.Matrix(
        n,
        n,
        lambda a, b: -energy[a, b] * rho[a, b],
    )
    assert all(sp.simplify(v) == 0 for v in generator - expected)


def numerical_schur_stress_check(energy: sp.Matrix) -> float:
    e = np.array(energy.tolist(), dtype=float)
    minimum_eigenvalue = math.inf
    for time in (0.0, 1e-6, 0.01, 0.1, 1.0, 10.0, 100.0):
        damping = np.exp(-time * e)
        eigenvalues = np.linalg.eigvalsh(damping)
        minimum_eigenvalue = min(minimum_eigenvalue, float(eigenvalues[0]))
        assert eigenvalues[0] >= -1e-12
        assert np.allclose(np.diag(damping), 1.0)

    for t, s in ((0.2, 0.7), (1.0, 3.0), (0.0, 2.0)):
        assert np.allclose(np.exp(-(t + s) * e), np.exp(-t * e) * np.exp(-s * e))

    return minimum_eigenvalue


def main() -> None:
    green, densities = exact_poisson_energy_check()
    energy = energy_matrix(green, densities)
    exact_cnd_check(energy, green, densities)
    exact_dp_generator_check(energy, green, densities)
    minimum_eigenvalue = numerical_schur_stress_check(energy)

    print("PASS exact finite Poisson field/source energy identity")
    print("PASS Penrose energy is one-half a squared Green-Hilbert distance")
    print("PASS exact conditional-negative-definiteness identity")
    print("PASS DP double commutator equals the Schur decay generator")
    print("PASS CPTP Schur-kernel stress test and semigroup law")
    print(f"minimum sampled damping eigenvalue: {minimum_eigenvalue:.3e}")


if __name__ == "__main__":
    main()
