# Fixed Points II v3 Revision Audit

## Source lineage

- Source: `_work/Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v2`
- Revised project: `revised_tex_vnext/Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v3`
- The v2 project remains untouched.

## Required corrections evaluated

| Finding | v2 evaluation | v3 action |
|---|---|---|
| Replace the seven-dimensional `S1 x T2 x T2 x T2` example | Required | Uses one compact `X6`; the torus example is `T2 x T2 x T2`, with shared-circle data encoded by a common `U(1)` connection rather than an extra factor |
| State strong commutation of unbounded vertical operators | Missing | Added commuting spectral measures, common dense domain, closed form sum, and joint spectral calculus |
| Treat the triplet as vertical structures on `M10=Y4 x X6` | Partly present but implemented as disjoint product fibers | Replaced by three possibly overlapping/nested operators on the common `L2(X6)` space |
| Use a Riemannian base control operator, not a Lorentzian d'Alembertian | Implicit but not scoped | Declared a complete Riemannian control base and nonnegative base Laplacian/Cauchy-slice operator |
| Separate physical time from stabilization time | Missing | Declared `t` and `tau` as stabilization parameters and reserved `U(t2,t1)` for separate physical evolution |
| Do not apply the Q-gap decay factor to estimates containing coherent modes | Violated by the global nonlinear smoothing estimate | Replaced it with a Q-sector Duhamel estimate and an independent P-sector equation |
| Do not construct a coherent invariant ball from the Q gap | Violated by the old `q(tau)` bound | Rebuilt the affine bound from base Poincare coercivity or coherent strong monotonicity only |
| Add a strict Lyapunov identity before identifying a time-step fixed point with equilibrium | Missing | Added a strict Lyapunov assumption, promotion theorem, and proof; otherwise the result remains a projected step fixed point |
| Remove/lift the scalar base zero mode for base-diffusion FCC | Missing | Restricted the Poincare gap to a mean-zero or boundary-conditioned invariant subspace and added a zero-mode warning |
| State enough smoothing and topology for Schauder compactness | Ambiguous | Uses bounded `L2 -> H1` smoothing and Rellich compactness into `L2`; Schauder phase space is explicitly `L2` |

## Additional issues found

| Issue | v3 resolution |
|---|---|
| A base-dependent projector need not commute with the base Laplacian | Added an explicit `[A,P]=0`/commutator-control assumption and deferred leakage models |
| The old fiber-gradient norm presupposed disjoint fibers | Replaced it with the joint form norm `sum ||A_n^(1/2) Psi||^2` |
| Projection of a condensing map needed justification | Uses the norm-one `L2` orthogonal projector and an `L2`-closed invariant set |
| The optional full-map condensing rate again imported the Q gap | Removed; the revision states that a full-map rate also needs coherent contraction |
| Sphere and nil examples could be read as incompatible product decompositions | Rewritten as operator/foliation examples on a selected six-manifold |

## Resulting scope

FP II v3 is a conditional Riemannian control-model specialization of FP I. It
proves projected stabilization-step fixed-point existence and coherent
uniqueness under explicit hypotheses. Equilibrium promotion requires the strict
Lyapunov identity. It does not select the physical MTT topology, prove
Lorentzian dynamics, or derive coherent contraction from internal gaps.

