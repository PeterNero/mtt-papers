# Fixed Points VI v4 Revision Audit

## Source lineage

- Source: `_work/Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v3`
- Revised: `revised_tex_vnext/Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v4`
- The v3 project remains untouched.

## Synthesis-level corrections

| Finding | v3 evaluation | v4 action |
|---|---|---|
| Do not claim a unified covariant field theory from FP I–V | The abstract promoted the control framework directly to a field theory | Introduces explicit statuses: inherited theorem, conditional completion, and physical interpretation |
| Use the joint projector correctly | The product `Pi_1 Pi_2 Pi_3` was declared an orthogonal projector without strong commutation | Uses the FP II joint spectral projector and permits a product only under strong commutation |
| Separate projected recurrence from equilibrium | A fixed point of the projected time-step map was treated as a steady solution | Restates the FP I existence alternatives and requires FP II’s strict Lyapunov argument for equilibrium promotion |
| Scope uniqueness to an actual inverse | The vertical gap was used as an inverse bound without excluding kernels or proving the operator estimate | Gives a conditional contraction theorem requiring the declared inverse and its norm |
| Preserve FP III disturbance distinctions | A shared loss/disturbance quantity reappeared | Separates deterministic amplitude, stochastic power, and their different floors |
| Preserve FP IV curvature structure | Curvature was inserted as a selected affine mass/gap formula | Uses the full curved operator, Riesz projector, and explicit old-projector leakage; affine response is not promoted |
| Correct centroid dynamics | Relativistic/Newtonian motion was inferred from the control framework | Retains intrinsic first-order modulation and requires a separate inertial/Lorentzian completion |
| Correct overlap conclusions | Persistence of overlap was made a merger rule and gap failure a collapse rule | Retains only absolute/sign-qualified interaction statements; merger and collapse require a dynamical theorem |
| Replace the FP V selection potential | The superseded `Phi_sel/Phi_crit` construction and shared threshold returned | Uses the exact margin deficit score and separates exit, force, energy, and post-exit selection |

## Independent mathematical corrections

| Finding | v3 evaluation | v4 action |
|---|---|---|
| Correct the continuous Lyapunov equation | With `d zeta=A zeta dt+B dW`, v3 wrote `A Sigma+Sigma A^T=Q` | Uses `A Sigma+Sigma A^T+Q=0` |
| Correct nonnormal matrix estimates | Spectral abscissa alone was used to bound the inverse and covariance | Assumes `||exp(tA)||<=M exp(-omega t)` and obtains the required `M` and `M^2` factors |
| Separate classical and quantum covariance | A classical Langevin covariance was immediately given quantum/PPT meaning | Requires CCR, `hbar`, uncertainty, and complete-positive quantum dynamics as additional data |
| Restrict PPT scope | The previous wording was broader than needed | States exactness for the two-mode `1 x 1` case and only the safe general multimode implication |
| Account for curvature-dependent mass variation | v3 retained a minimal Einstein equation after inserting `R |phi|^2` | States that metric variation produces nonminimal gravitational terms |
| Do not infer a Lorentz force from covariance | Gauge covariance was promoted directly to point-particle motion | Requires a controlled localized-solution limit |
| Correct bilocal causality | Equal-time spatial nonlocality was called microcausal because the principal symbol was unchanged | Proves the instantaneous domain-of-dependence obstruction |
| Supply a causal alternative | “Integrating out a mediator” was treated as equivalent to an equal-time symmetric kernel | Uses a local hyperbolic mediator and notes that elimination gives a retarded memory kernel |
| Avoid an unsupported local well-posedness theorem | `K in L1` and `s>2` were insufficient for the full Einstein–Yang–Mills–Dirac–scalar claim | Removes the theorem; keeps only the limited statement that `L1` may aid estimates but cannot prove causality |

## Physical-claim corrections

- Three internal structures do not by themselves select three gauge groups,
  representations, particle statistics, bifundamental matter, or the Standard
  Model.
- The Lorentzian action is retained only as a schematic conditional
  completion; all fields and couplings remain additional data.
- Decoherence, measurement, entropy production, emergent time, inflation,
  horizons, and cosmological arrows are not conclusions of the FP theorems.
- A local/open-quantum completion can make some of those topics mathematically
  investigable, but the bridge must be proved separately.

## Resulting series-level achievement

FP VI v4 consolidates, without reopening, the corrected achievements of FP
I–V: projected fixed-point existence under explicit compactness hypotheses,
strict-Lyapunov equilibrium promotion, joint-mode stability and disturbance
floors, curved-cluster persistence and leakage, intrinsic modulation, frozen
linear covariance/correlation, and admissibility exit diagnostics. It gives a
precise list of the constructive bridges still required for a physical theory.

## Validation

- FP I through FP VI permanent theorem audits pass.
- The FP VI migration and verifier scripts pass Python syntax validation.
- TeX environment nesting passes.
- PDF compilation remains blocked by the previously identified local MiKTeX
  dependency `amsthm.sty`; this is an environment issue rather than a detected
  FP VI source error.
