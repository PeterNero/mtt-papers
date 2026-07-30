# Projected Heat Kernels v1 Revision Audit

## Current version delta

The unversioned source contained correct compact elliptic functional-calculus
results, but promoted them to a universal physical delta-replacement rule.
Version 1 retains the projected heat operator and all valid spectral
estimates while correcting the inference layer.

The revision:

- declares that the operator acts on a specified compact Riemannian internal
  space, Euclidean problem, or spatial Cauchy-slice Hilbert space;
- proves explicitly that `AP = 0` implies
  `P exp(-tau A) P = P`, so harmonic projection receives no additional
  proper-time smoothing;
- separates exact removal by the projected operator from spectral-gap
  damping by `exp(-tau A) Q`;
- replaces the universal delta rule by a same-domain eligibility contract;
- treats a kernel-valued CCR as a changed symplectic algebra requiring an
  independent microcausality and covariance proof;
- treats finite contact vertices as nonlocal EFT candidates unless a local
  parent and gauge/BRST consistency are supplied; and
- adds normalization and instrument obligations for measurement effects.

## Retained result

For declared compatible data `(A,P,tau)`, functional calculus uniquely
determines `P exp(-tau A) P`. In the compact elliptic spectral setting it has
the displayed regularity and coherent-band error estimates, and suitable
families approach the full identity distribution in the joint sharp limit.

## Remaining boundary

Current MTT fixed-point results do not select one operator domain, projector,
and proper-time scale for every physical sector. They also do not prove that
substitution into a spacetime source, CCR, gauge constraint, local vertex,
measurement instrument, or noise law preserves the target theory.

## Validation

The paper must compile without undefined references or layout warnings. Its
PDF, TeX, Markdown, revision audit, and explanatory discussion are frozen
only after visual review and the repository release verifier pass.
