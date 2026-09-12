# Fixed Points V v7 Release Audit

## v7 publication delta (July 2026)

- **Supersedes:** v6.
- **Reason:** covariance and deficit diagnostics could still be mistaken for
  dynamics or selection.
- **Resolution:** add the covariance-cloud and diagnostic-only explanations;
  preserve FP III ownership of the scalar OU baseline.
- **Retained:** all v6 covariance and exit bounds.
- **Remaining:** nonlinear dynamics, causal propagation, and post-exit
  selection.

## Source lineage

- Source: `_work/Fixed_Points_V__Curvature_Coupling__Multi_Structure_Dynamics_and_Drivers_v5`
- Revised: `revised_tex_vnext/Fixed_Points_V__Curvature_Coupling__Multi_Structure_Dynamics_and_Drivers_v6`
- The v5 project remains untouched.

## Required corrections evaluated

| Finding | v5 evaluation | v6 action |
|---|---|---|
| Use the FP IV curved operator | Curvature was encoded by an unproved affine eigenvalue shift | Uses `L_x=nabla_x* nabla_x+R_x` and the curved Riesz projector; labels an affine response as an additional approximation |
| Use joint modal labels | Separate `(n,omega)` labels could repeat the FP II counting error | Uses one joint label `alpha`, including multiplicity |
| Separate stochastic and deterministic disturbances | The retired shared `delta` threshold remained in admissibility | Uses stochastic power `q_alpha`, deterministic amplitude `f_alpha`, and their distinct FP III floors |
| Write white noise as an SDE | The formal derivative `xi(t)` was used as if pointwise noise | Writes the Ito equation and proves its invariant variance by Ito isometry |
| State sufficient matrix hypotheses | `Gamma >= gamma_0 I` was used without specifying symmetry | Assumes self-adjoint positive damping for the displayed operator-norm bound |
| Derive the cross block from the block Lyapunov equation | The cross-covariance estimate was asserted without the needed block-damping structure | Assumes block-diagonal damping, writes the Sylvester equation, and proves the semigroup integral bound |
| Correct canonical-correlation normalization | v5 divided by the square root of the largest covariance eigenvalues, which does not control pseudoinverse normalization | Uses the smallest positive covariance eigenvalues on the two supports |
| Control modal sums | The selection sum had no finiteness or summability condition | Restricts to a finite constraint family or states the additional uniform/compact control needed for an infinite family |
| Do not call a diagnostic sum physical energy | The selection potential was interpreted as infinite energetic cost without a source theorem | Replaces it with an exact deficit score and explicitly denies force, energy, and selection status absent an independent theorem |
| Do not infer Gaussianity through a nonlinear map | A Lipschitz function of Gaussian centroid data was declared Gaussian | Requires exact affine Gaussian margin observables and states why Lipschitz regularity alone is insufficient |
| Repair the exit probability threshold | The previous Borell expression omitted the observable mean/margin and positivity condition | Uses positive affine margins and requires each margin to exceed the expected supremum |
| Supply continuous-time regularity | Extreme-value scaling was invoked without entropy control | Assumes separability, continuous paths, finite expected supremum, and identifies metric entropy as a sufficient route |
| Restrict localization claims | Equal-time correlation was promoted to localized, non-propagating exits | Proves a fixed-time/finite-grid simultaneous-exit bound and states that propagation requires cross-time dynamics |
| Remove probabilistic censorship | The corollary claimed nonadmissibility was non-generic and isolated without adequate hypotheses | Deletes the claim and replaces it with a no-propagation theorem from covariance alone |
| Separate exit from post-exit selection | Barrier exceedance was close to being read as a transition mechanism | Proves only first exit from declared constraints and explicitly withholds force and basin-selection conclusions |

## Additional corrections

- The stationary covariance is represented by its convergent semigroup
  integral, making existence, uniqueness, and the norm bound transparent.
- Zero cross-noise implies zero stationary cross-covariance only under the
  declared block-diagonal frozen damping hypothesis.
- Spectral separation, one-sided damping, deterministic response tolerance,
  and stochastic variance tolerance are distinct admissibility margins.
- The finite-grid exit estimate uses only Gaussian tails and a union bound, so
  it does not silently assume temporal independence.
- The simultaneous-exit estimate is a scalar observable theorem; canonical
  block correlation supplies bounds on such observables but is not itself a
  causal statement.

## Theorem ownership correction

FP III owns the exact scalar OU variance theorem. FP V imports that scalar
baseline and owns the genuinely multi-structure layer: the stable-semigroup
covariance and resolvent theorem, its symmetric-damping corollary,
cross-covariance and canonical-correlation bounds, and the admissibility-exit
results. The stronger nonnormal semigroup theorem formerly repeated in FP VI
has been placed here, where covariance belongs.

## Resulting scope

FP V v6 proves exact covariance and correlation estimates for a frozen linear
OU model and rigorous exit estimates for affine Gaussian margin observables.
It also gives an exact scalar diagnostic for a declared admissible domain. It
does not derive a physical Driver, energetic barrier, causal propagation law,
or post-exit state from covariance or spectral diagnostics alone.

## Expository revision

The current paper now uses the covariance-ellipsoid and admissibility-boundary
picture to connect its formal blocks. A paper-specific reader guide explains
the inherited role of FP III and FP IV, the diagnostic meaning of the deficit
score, and the path from stable linearization to covariance, affine margins,
and exit bounds. New discussions explain transient amplification in the
Lyapunov estimate, normalize cross-correlation conceptually, separate
finite-grid from continuous-path claims, and identify the exact point at which
covariance ceases to support causal conclusions. No theorem owned by FP III is
reclaimed as an FP V result.

## Validation

- FP I through FP V permanent theorem audits pass.
- The FP V migration and verifier scripts pass Python syntax validation.
- TeX environment nesting passes.
- The current source compiles with `pdflatex` to an 8-page PDF.
- The final log has no undefined references, underfull boxes, overfull boxes,
  or LaTeX/package warnings.

## Corpus coherence reconciliation, 2026-08-02

The selected TeX now states the paper-specific `C.FP.01` boundary explicitly:
the coupled generator, projector, covariance source, invariant domain, and any
post-exit transition kernel must be selected by the physical q79 model. FP V
diagnoses supplied data and does not emit those physical operators. No theorem
or estimate is changed.

## Foundational dependency repair: version 9 (2026-09-12)

Removes misleading generic numerical-evidence boilerplate, explicitly cites earlier FP editions and preserves every covariance/correlation/exit theorem and proof. No later MTT research is a premise.

Only local arguments, earlier numbered FP installments and standard mathematics are proof sources. Prior revision and validation entries above are historical, not current application-status assertions. Original Zenodo release metadata is preserved; this is an unreleased authoring revision. See FP_FOUNDATIONAL_DEPENDENCY_REPAIR_2026-09-12.md for the full review and verification record.
