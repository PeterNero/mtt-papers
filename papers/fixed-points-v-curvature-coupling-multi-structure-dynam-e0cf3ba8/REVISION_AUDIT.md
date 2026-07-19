# Fixed Points V v6 Revision Audit

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

## Resulting scope

FP V v6 proves exact covariance and correlation estimates for a frozen linear
OU model and rigorous exit estimates for affine Gaussian margin observables.
It also gives an exact scalar diagnostic for a declared admissible domain. It
does not derive a physical Driver, energetic barrier, causal propagation law,
or post-exit state from covariance or spectral diagnostics alone.

## Validation

- FP I through FP V permanent theorem audits pass.
- The FP V migration and verifier scripts pass Python syntax validation.
- TeX environment nesting passes.
- PDF compilation remains blocked by the previously identified local MiKTeX
  dependency `amsthm.sty`; this is an environment issue rather than a detected
  FP V source error.
