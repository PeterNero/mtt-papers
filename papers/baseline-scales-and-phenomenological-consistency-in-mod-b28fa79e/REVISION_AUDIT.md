# Baseline Scales v2 Revision Audit

## Source lineage

- Source: `_work/Baseline_Scales_and_Phenomenological_Consistency_in_Modal_Triplet_Theory`
- Revised: `revised_tex_vnext/Baseline_Scales_and_Phenomenological_Consistency_in_Modal_Triplet_Theory_v2`
- The original project remains untouched.

## Required scope corrections

| Finding | Original status | v2 action |
|---|---|---|
| Internal gap identified with the effective cutoff | Unsupported identification | Defines `lambda_*^int` as an internal mass/truncation scale and `Lambda_4D` as a separate physical EFT cutoff |
| Eigenvalues quoted without a physical normalization | Units under-specified | Requires `A_int^phys=M_int^2 Ahat_int` when the geometric operator is dimensionless |
| Vertical gap said to damp high four-dimensional energy | False without a base operator | Explains that each internal mode carries arbitrary base momentum unless an external damping/form-factor/EFT theorem is supplied |
| Internal gap automatically made all unwanted fields heavy | Missing physical action and mixing calculation | Gives a conditional product-action mass theorem and lists warping, mixing, boundary, and interaction corrections |
| Q-sector decay equated directly with the gap | Missing generator sign and nonnormal control | Uses `||exp(tau L_QQ)||<=M_Q exp(-omega_Q tau)` and derives a gap relation only for the bounded-perturbation generator |
| Coherent contraction tied to the internal gap | Independent gates conflated | Separates `q_coh` or `mu_coh` from `lambda_*^int` |
| Curvature correction inferred from a schematic ratio | Dimensional analysis promoted to prediction | Treats higher-curvature coefficients as physical-action matching data |
| Planck scale treated as emergent from generic coherent data | No selected gravitational action | Gives the higher-dimensional volume relation only as a model-dependent example |
| Fifth-force safety inferred from a large gap | Coupling omitted | Requires both mediator mass and matter coupling/charge response |
| Lorentz and equivalence-principle safety inferred structurally | Principal symbol and species couplings omitted | Requires explicit observable response maps |
| GW/GR/cosmological agreement declared automatically | No common physical model or numerical execution | Lists the required responses and explicitly marks them unevaluated |
| “No fine tuning” asserted without a measure | Undefined claim | Requires a prior, sensitivity, condition number, or naturalness criterion |
| Separate parameter choices treated as simultaneous consistency | No common witness | Defines one consistency set over one parameter/branch space |
| Numerical agreement risked being called prediction | Provenance missing | Distinguishes calibration, consistency witness, and held-out prediction |

## Retained constructive result

Under a selected product action with quadratic operator

`-Box_4 + A_int + m_0^2`,

compatible domains, product measure, and an orthonormal internal eigenbasis,
the four-dimensional masses satisfy `m_k^2=m_0^2+lambda_k`. This is a
conditional physical bridge, not a consequence of projection alone.

## Formal consistency protocol

The revised paper requires each empirical row to provide:

1. A response map from the same selected physical completion.
2. Its parameter domain.
3. Theory uncertainty.
4. Experimental acceptance set.
5. Data and branch-selection provenance.

Joint consistency means the intersection of all rows with the structural
domain is nonempty. A displayed point in that intersection is a consistency
witness; it becomes a held-out prediction only for data not used anywhere in
construction or selection.

## Current status

The paper records the structural scales supplied by Foundation and Fixed
Points, but no common physical response system for particle, fifth-force,
Lorentz, GR, GW, and cosmological observations. It therefore neither proves
empirical viability nor identifies an empirical contradiction. Its declared
status is “not evaluated by this ledger.”

## Validation

- Baseline Scales v2 permanent theorem audit passes.
- Foundation v7, Projection-Admissibility v2, Signature Stability v2, and all
  six Fixed Points audits continue to pass.
- Migration and verifier scripts pass Python syntax validation.
- TeX environment nesting and ASCII/tab guards pass.
- PDF compilation remains blocked by the previously identified local MiKTeX
  dependency `amsthm.sty`; this is an environment issue rather than a detected
  source error.
