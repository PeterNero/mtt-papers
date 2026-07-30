# Revision Audit: Finite-Memory Noise and the White-Noise/Markov Limit

## Release Decision

- Current source: Version 1, July 2026.
- Supersedes: the unversioned April 2026 manuscript.
- Review class: scaling-limit correction, process-level completion, and MTT scope control.
- Intended tier: exact analysis for the stated approximate identities and colored Ornstein-Uhlenbeck model; conditional for a general deterministic or geometric MTT source.
- Not a derivation of fundamental randomness, universal Markov closure, or sector-specific physical noise coefficients.

## Defects Corrected

1. The earlier manuscript moved from covariance convergence to an Ornstein-Uhlenbeck process and Markov dynamics without a law-level convergence theorem.
2. Pointwise nonnegativity and normalization were treated as sufficient for a physical stationary covariance, omitting positive type.
3. Gaussianity, finite-dimensional convergence, path-space tightness, and closure of the resolved state were not separated.
4. A finite-memory correction was discussed without first constructing an explicit finite-memory process.
5. The response variance was allowed to suggest a quantum uncertainty floor without deriving observables, commutators, or hbar normalization.
6. Projection was allowed to suggest stochasticity without a preparation measure, invariant state, coarse-graining rule, or functional limit theorem.
7. Additive and multiplicative noise limits were not distinguished, leaving the Ito/Stratonovich issue underspecified.

## Exact Results Owned by Version 1

### Approximate-identity limit

If nonnegative kernels `C_tau` have total mass `2D` and concentrate at zero, then

```text
C_tau -> 2D delta_0
```

in the distributional sense. This is a kernel theorem only.

### Positive-type guard

A stationary covariance must be of positive type, equivalently represented under the standard continuity assumptions by a nonnegative spectral measure. Pointwise nonnegativity alone is insufficient.

### Covariance-law separation

The constant Gaussian process and the constant Rademacher process have identical means and covariances but different laws. Covariance convergence therefore does not imply process convergence unless additional law-level information, such as Gaussianity, is supplied.

### Exact colored-OU functional limit

For

```text
d xi_tau = -(1/tau) xi_tau dt + sqrt(2D)/tau dW
```

in its stationary law, the integrated source

```text
B_tau(t) = integral_0^t xi_tau(s) ds
```

converges weakly in `C([0,T])` to `sqrt(2D) W`. The proof gives explicit covariance convergence and a fourth-moment tightness bound.

### Damped-response limit

For

```text
dot a_tau = -gamma a_tau + xi_tau,
```

the continuous solution map and the functional limit imply convergence to

```text
da = -gamma a dt + sqrt(2D) dW.
```

### Exact finite-memory floor

The stationary augmented system obeys

```text
Var(xi_tau) = D/tau
Cov(a_tau, xi_tau) = D/(1 + gamma tau)
Var(a_tau) = D/[gamma(1 + gamma tau)].
```

The last expression tends to `D/gamma`. It is an effective response width, not a derivation of a Heisenberg uncertainty relation.

## Markov Status

At finite memory time, the augmented state `(a_tau, xi_tau)` is Markov. The resolved coordinate `a_tau` is generally not closed because its derivative depends on the hidden memory coordinate. The limiting OU coordinate is a closed Markov diffusion. Thus the exact chain is:

```text
finite Markov augmentation
  -> nonclosed resolved memory
  -> closed Markov limit.
```

## Current MTT Interpretation

Projection can hide upper-state information and, after an ensemble or invariant state is supplied, induce effective unresolved forcing. Projection alone does not create a probability measure or a diffusion.

A strict MTT source theorem still needs:

1. a selected preparation measure or invariant state;
2. a centered finite-memory observable;
3. positivity and normalization of its covariance;
4. quantitative mixing, martingale approximation, or another functional limit theorem;
5. tightness in a declared path topology;
6. closure of the intended resolved variables;
7. source derivations of `D`, `tau`, and `gamma`; and
8. an observable finite-memory error test.

## Claims Explicitly Not Made

- Delta-like covariance alone does not establish Gaussian white noise.
- Covariance convergence alone does not establish path convergence.
- Determinism alone does not establish a diffusive limit.
- Projection alone does not establish probability.
- A finite-memory source need not yield a Markov reduced state.
- The colored-OU example is not claimed to be the selected q79 physical source.
- The response variance is not identified with a quantum uncertainty principle.
- For multiplicative forcing, the stochastic calculus is not selected without the approximation scheme and its hypotheses.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 1 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- Primary references checked for Ornstein-Uhlenbeck and Wong-Zakai results.
- Kernel, covariance, finite-dimensional, path-space, and Markov claims are explicitly separated.
- LaTeX compiles without unresolved references, overfull boxes, or underfull boxes.
- All eight PDF pages were visually inspected after the final compile; no clipping, overlap, broken tables, or unreadable equations were found.
