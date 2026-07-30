# Revision Audit: Deterministic Projection, Diffusive Limits, and Knee-Like Threshold Transitions

## Release Decision

- Current source: Version 2, July 2026.
- Supersedes: Version 1, January 2026.
- Review class: substantive mathematical correction.
- Intended tier: exact finite toy model plus an imported deterministic-homogenization theorem.
- Not an MTT source-selection theorem or a quantum-measurement derivation.

## Defects Corrected

1. The doubling map used in Version 1 is two-to-one almost everywhere, so it could not support the claim that the displayed full map was invertible.
2. For the old drift `-gamma(s) x` with `x < 0` and boundary `x = 0`, the stated stable and unstable crossing directions were reversed.
3. The paper changed models between sections: the early argument used a sign-changing stability coefficient, while the later exact formula used a fixed stable coefficient and an affine protocol force.
4. The exact Gaussian formula was for the endpoint event `X(t) >= 0`, not the first-passage event `sup_{u <= t} X(u) >= 0`.
5. Pointwise weak convergence did not justify the claimed convergence of first-passage knee locations and widths.
6. The fixed-Markov-generator comparison was tautological and did not establish a physical no-go result.
7. The probability space for deterministic hidden initial conditions was not stated clearly.
8. The Melbourne-Stuart bibliographic entry had the wrong title and journal.

## Version 2 Construction

The corrected source model is the smooth skew-product diffeomorphism

```text
F_epsilon,s(x,y)
  = ((1-epsilon gamma)x
     + epsilon alpha(s-s0)
     + sqrt(epsilon) sin(2 pi y1),
     A y mod Z^2),

A = [[2,1],[1,1]].
```

The hidden initial condition is sampled as `y0 ~ Lebesgue(T^2)` while every resulting trajectory remains deterministic.

## Exact Results Owned Here

- The displayed finite source map is a smooth diffeomorphism for `0 < epsilon < 1/gamma`.
- The retained map `P(x,y)=x` is non-injective.
- The Green-Kubo variance for `phi(y)=sin(2 pi y1)` is exactly `1/2`.
- The affine Ornstein-Uhlenbeck endpoint law has the stated mean, variance, midpoint, maximal slope, and exact quantile-width formula.
- The finite deterministic endpoint curves converge uniformly on compact protocol intervals.
- Finite-system quantiles converge to the unique limiting quantiles.

## Imported Result

The diffusion-limit theorem is imported from standard deterministic homogenization for discrete-time fast-slow systems. The paper specializes that theorem to the explicit hyperbolic toral source and computes its coefficient. It does not claim ownership of the general homogenization theorem.

Primary references checked:

- Melbourne and Stuart, *A Note on Diffusion Limits of Chaotic Skew-Product Flows*, Nonlinearity 24 (2011).
- Gottwald and Melbourne, *Homogenization for Deterministic Maps and Multiplicative Noise*, Proceedings of the Royal Society A 469 (2013).
- Chevyrev, Friz, Korepanov, Melbourne, and Zhang, *Deterministic Homogenization under Optimal Moment Assumptions for Fast-Slow Systems. Part 2*, Annales de l'Institut Henri Poincare B 58 (2022).

## Claims Explicitly Not Made

- No first-passage or metastable-exit theorem.
- No discontinuous phase transition.
- No claim that projection makes an individual trajectory intrinsically random.
- No no-go theorem for parameter-dependent Markov models.
- No Born-rule, collapse, or physical measurement derivation.
- No selection of `alpha`, `gamma`, `s0`, the threshold, or the invariant ensemble from MTT geometry.
- No empirical prediction.

## MTT Interface Boundary

Promotion to an MTT result would require:

1. a selected MTT source carrier and upper evolution;
2. an intertwiner to this source model or a native replacement;
3. a theorem selecting the retained outcome algebra;
4. geometric sources for the protocol and scale parameters; and
5. a physical record-forming instrument with derived probabilities.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 2 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- No duplicated MTT theorem body.
- PDF must be compiled with BibTeX and visually inspected page by page before freezing.
