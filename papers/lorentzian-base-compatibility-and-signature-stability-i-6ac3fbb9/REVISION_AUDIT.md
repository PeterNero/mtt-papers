# Lorentzian Base Compatibility and Signature Stability v2 Revision Audit

## Source lineage

- Source: `_work/Signature_Selection_and_Exclusion_in_Modal_Triplet_Theory`
- Revised: `revised_tex_vnext/Lorentzian_Base_Compatibility_and_Signature_Stability_in_the_MTT_Fixed_Point_Realization_v2`
- The original project remains untouched.

## Withdrawn central construction

The former effective-signature construction used

`K_{mu nu} = <D_mu Psi, D_nu Psi>`

with a positive Hilbert inner product. This is necessarily a
positive-semidefinite Gram matrix and cannot have Lorentzian inertia. All
signature-selection and exclusion claims derived from assigning negative
eigenvalues to that tensor are withdrawn.

## Replacement results

| Finding | Original status | v2 replacement |
|---|---|---|
| Positive Gram tensor used as causal metric | Mathematically impossible | Proves the positive Gram obstruction and retains the tensor only as a possible positive kinetic/information metric |
| Signature said to emerge without background causal data | Unsupported | Locates physical signature in the gauge-fixed principal symbol of a selected local physical equation |
| Stabilization direction used as physical time | Type conflation | Separates `R_tau` from physical propagation `U(t_2,t_1)` |
| Euclidean signature universally excluded | Unsupported control-flow argument | Proves that a definite quadratic metric symbol is elliptic rather than hyperbolic for the standard Cauchy problem; preserves Euclidean boundary-value/Wick-rotated uses |
| `(2,2)` and multiple times universally excluded | Unsupported instability claim | Proves that nondegenerate quadratic forms with both inertia indices at least two have no hyperbolicity covector; scopes this to metric-type standard Cauchy evolution |
| Higher spatial dimensions excluded by the internal gap | False | Proves that `(1,n)` is hyperbolic for every `n >= 1`; each dimensional exclusion needs an independent theorem |
| `3+1` called selected and conditionally inevitable | Not proved | States `3+1` as part of the canonical MTT/FP realization pending a dimension-selection theorem |
| Signature robustness asserted informally | Missing quantitative margin | Proves uniform inertia stability under perturbations smaller than the minimum absolute eigenvalue margin |
| Signature change treated as an admissibility failure | Under-specified | Proves only that continuous inertia change crosses degeneracy; system hyperbolicity needs further symmetrizer and constraint control |
| Coherent projection said to generate spacetime signature | Unsupported | Proves principal-symbol descent when the upper principal coefficient is scalar internally and the projector is smooth/fiberwise |

## Independent gates retained

The revised paper keeps these logically separate:

1. Internal spectral gap and coherent projector.
2. Stabilization-flow contraction or damping.
3. Physical hyperbolicity and causal propagation.
4. Base dimension and topology.

Fixed Points results control the first two and support coherent compression.
They do not select the principal symbol or base dimension.

## Resulting scope

The paper now proves compatibility and perturbative stability of a supplied
Lorentzian physical completion. It conditionally rules out Euclidean and
multi-time quadratic metric symbols from the same standard one-time hyperbolic
Cauchy problem. It does not derive Lorentzian signature, three spatial
dimensions, physical time, or a causal metric from Hilbert geometry.

## Validation

- Signature Stability v2 permanent theorem audit passes.
- Foundation v7, Projection-Admissibility v2, and all six Fixed Points audits
  continue to pass.
- Migration and verifier scripts pass Python syntax validation.
- TeX environment nesting and ASCII/tab guards pass.
- The current source compiles successfully with two `pdflatex` passes.
- The six-page PDF was rendered in full and visually inspected on 2026-07-29.
