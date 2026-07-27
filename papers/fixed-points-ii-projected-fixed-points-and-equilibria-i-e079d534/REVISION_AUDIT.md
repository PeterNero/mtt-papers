# Fixed Points II v4 Revision Audit

## v4 delta (July 2026)

The v4 update consumes the canonically verified
`mtt-qm-source-proof` head `1615da7` without changing the FP II existence,
uniqueness, or equilibrium-promotion theorem.

| New result | v4 action |
|---|---|
| A nontrivial parallel `1<2<3` flag cannot lie inside an irreducible stable HYM gauge factor | Places `p1 < p2 < p3` on the external lane tensor factor |
| The shared differential line is a separate flat scalar factor | Separates it from both the curved HYM bundle and dimension counting |
| The accepted 27-state algebra is post-projection source data | Explicitly excludes interpreting it as a rank-27 physical Galerkin subspace |
| The six-coordinate strain carrier is a nonlinear orientation-forgetting quotient shadow | Explicitly excludes a linear rank-six subspace of `Herm(3)` |
| Universal projective/quotient constructions pass, while the physical q79 rows remain `0/3` | Records the open endpoint, action, Hessian, finite-reduction, and Lorentzian bridges without promoting them |
| Two latent TeX defects blocked compilation | Removes nested math around an ordinary-text `S^3` and avoids a double superscript on `\lamstar` |

No FP II fixed-point hypothesis was weakened or replaced. This is a type and
scope correction at the q79 realization boundary.

## Prior v3 correction retained

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

FP II v4 is a conditional Riemannian control-model specialization of FP I. It
proves projected stabilization-step fixed-point existence and coherent
uniqueness under explicit hypotheses. Equilibrium promotion requires the strict
Lyapunov identity. Its q79 realization now places the `1<2<3` flag on an
external lane factor and keeps the shared flat line, post-projection 27-state
algebra, and nonlinear strain quotient correctly typed. It does not select the
physical HYM endpoints or action, prove Lorentzian dynamics, or derive coherent
contraction from internal gaps.

## Validation

- The canonical `mtt-qm-source-proof` verifier passes at commit `1615da7`.
- The 139-paper repository verifier passes after Markdown and hash regeneration.
- `pdflatex`, `bibtex`, and two final `pdflatex` passes compile FP II v4 with
  resolved citations and references.
