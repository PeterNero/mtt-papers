# Revision Audit: Dirac Delta Limits and the MTT Finite-Kernel Diagnostic

## Release Decision

- Current source: Version 1, July 2026.
- Supersedes: the unversioned April 2026 manuscript.
- Review class: distribution-role separation, kernel regularity correction, fixed-point correction, gauge-scope repair, and quantitative exactness completion.
- Intended tier: exact spectral-projector, heat-kernel, coarea-tube, compressed-CCR, and deterministic-pushforward results; conditional physical and MTT source interpretation.
- Not a universal origin theorem for delta distributions, a global gauge-fixing theorem, a measurement-completion theorem, or an ultraviolet-completion theorem.

## Defects Corrected

1. The earlier manuscript treated every physical delta as a zero-width admissible projection.
2. It did not distinguish identity kernels, sources, constraints, conservation distributions, PVM densities, and gauge-slice selectors.
3. It assumed that any bounded projection has a smooth or bounded pointwise kernel.
4. It inferred finite physical width from a spectral gap without a source or calibration theorem.
5. It blurred the difference between an idempotent spectral projector and a nonidempotent heat semigroup.
6. It claimed that a deterministic fixed-point basin produces finite-width concentration, although deterministic attraction can push an entire ensemble to a point mass.
7. Its Gaussian constraint filter lacked the normalization and coarea Jacobian required for the correct limit.
8. It promoted a local finite-dimensional Faddeev-Popov change of variables to global functional gauge fixing.
9. It treated ghosts and BRST language as evidence for a selected MTT quotient without proving that source.
10. It let a finite detector kernel stand in for the measurement instrument, outcome completion, and record stabilization.
11. It treated exact momentum-conservation deltas as finite overlap effects rather than Fourier consequences of translation invariance.
12. It suggested that finite smoothing generally repairs renormalization without proving symmetry preservation, matching, unitarity, or cutoff selection.
13. It assigned delta roles to circle, lens, and nil layers without an intertwining or source theorem.

## Exact Results Owned by Version 1

### Diagonal identity distribution

On a compact Riemannian manifold, the diagonal distribution

```text
<delta_diag, Psi> = integral_X Psi(x,x) dV(x)
```

is the Schwartz kernel of the identity.

### Spectral projector kernel limit

For a nonnegative self-adjoint Laplace-type operator in the declared compact elliptic setting, the finite-rank kernels

```text
K_Lambda(x,y)
  = sum_{lambda_j <= Lambda} phi_j(x) conjugate(phi_j(y))
```

converge to `delta_diag` in distributions.

### Quantitative spectral truncation

For `r >= 0`,

```text
||(I - Pi_Lambda)f||_{H^s}
  <= (1 + Lambda)^(-r/2) ||f||_{H^(s+r)}.
```

This is the exact finite-cutoff certificate. It does not select `Lambda`.

### Heat-kernel approximate identity

For `0 <= r <= 2`,

```text
||(exp(-tau Delta) - I)f||_{H^s}
  <= tau^(r/2) ||f||_{H^(s+r)}.
```

The heat kernel approaches the same identity distribution but is not a projection.

### Gaussian constraint-tube limit

For a smooth submersion `C:R^n -> R^m` near the compact support of the test function, the normalized Gaussian

```text
g_epsilon(z)
  = (2 pi epsilon^2)^(-m/2)
    exp(-|z|^2/(2 epsilon^2))
```

satisfies

```text
integral f(x) g_epsilon(C(x)) dx
  -> integral_{C^(-1)(0)} f(x)/J_C(x) dH^(n-m)(x).
```

The normalization and normal Jacobian are mandatory.

### Compressed canonical commutation relation

For an orthogonal one-particle projection `P`,

```text
[a(Pf), a_dagger(Pg)]
  = <Pf,Pg> I
  = <f,Pg> I.
```

If `P` has a sufficiently regular kernel, that kernel represents the compressed inner product exactly. This statement belongs only to the declared compressed theory.

### Deterministic fixed-point concentration

If every point in the support of an initial probability measure converges under iteration to one attractor, the pushforward measures converge weakly to the Dirac mass at that attractor. A nonzero stationary width requires continuing disturbance or another broadening mechanism.

## Correct Gauge Boundary

For a finite-dimensional local group action, an invertible orbit-to-gauge-condition derivative and a neighborhood containing exactly one root yield a local delta change-of-variables identity. The Faddeev-Popov determinant is the corresponding Jacobian.

This does not establish:

- a global slice;
- absence of Gribov copies;
- an infinite-dimensional functional measure;
- a regulator-independent determinant; or
- a selected MTT quotient kernel.

Primary references checked:

- Faddeev and Popov, *Feynman Diagrams for the Yang-Mills Field*, 1967, DOI `10.1016/0370-2693(67)90067-6`.
- Gribov, *Quantization of Non-Abelian Gauge Theories*, 1978, DOI `10.1016/0550-3213(78)90175-X`.

## Correct Measurement Boundary

The paper imports, without duplicating, the companion finite-resolution measurement result:

```text
normalized detector response
  -> smeared position POVM
  -> L1/total-variation sharp-statistics limit
  -> one compatible square-root instrument.
```

The detector effect does not by itself derive the physical coupling, choose an instrument uniquely, complete one outcome, or stabilize its record. A discrete finite-dimensional PVM need not involve a Dirac distribution.

## MTT Diagnostic and Completion Obligations

For each downstream delta:

1. classify its mathematical role;
2. identify a role-appropriate finite object;
3. derive that object and its scale from selected upstream geometry;
4. declare the convergence topology;
5. provide a quantitative error or exactness certificate; and
6. verify the required symmetry and operator identities at finite resolution.

The current paper supplies several reusable analytic bridges. It does not derive the upstream source.

## Claims Explicitly Not Made

- Not every delta is a hidden projection.
- A spectral gap does not select a physical resolution width.
- An arbitrary bounded projector need not have a smooth kernel.
- Heat smoothing is not orthogonal projection.
- Deterministic attraction does not preserve a finite ensemble width.
- A local Faddeev-Popov identity is not global gauge fixing.
- Finite smearing does not select a measurement outcome.
- Translation-invariant conservation deltas are not necessarily finite-overlap artifacts.
- A finite kernel is not automatically a renormalized or ultraviolet-complete theory.
- Circle, lens, and nil do not yet select the finite kernels or their scales in this paper.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 1 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- LaTeX compiles without unresolved references, overfull boxes, or underfull boxes.
- All twelve PDF pages were visually inspected after the final compile; no clipping, overlap, broken tables, unreadable equations, or malformed references were found.
