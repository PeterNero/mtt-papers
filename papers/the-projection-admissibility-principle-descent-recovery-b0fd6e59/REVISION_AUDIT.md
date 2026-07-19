# Projection–Admissibility v2 Revision Audit

## Source lineage

- Source: `_work/The_Projection__Admissibility_Principle__Structural_Constraints_on_Effective_Physical_Description (1)`
- Revised: `revised_tex_vnext/The_Projection__Admissibility_Principle__Descent__Recovery__and_Structural_Constraints_v2`
- The original project remains untouched.

## Disposition of the former central theorem

The original Projection–Admissibility Obstruction is withdrawn. Its proof used
noninjectivity of a cross-level map to forbid a right inverse. This is false:
a noninjective surjection can have a right section. The proof also substituted
unstated continuity, locality, and predictive-stability requirements for the
set-theoretic equation defining a section.

Every corollary that depended only on that obstruction has therefore been
withdrawn or rebuilt: probability from degeneracy, automatic irreversibility,
an arrow of time, universality, entropy/information loss, measurement collapse,
horizon entropy, and MTT constructive closure.

## Replacement theorem chain

| Object | Correct equation | Gate established in v2 |
|---|---|---|
| Representative section | `T_t S_t = id` | Set-theoretically requires surjectivity; regular sections need category-specific theorems |
| Exact upper decoder | `D_t T_t = id_A` | Exists on the attained image exactly when `T_t` is injective |
| Autonomous reduced evolution | `F_t P_0 = P_t Phi_t` | Exists exactly when upper evolution preserves initial reduction fibers |
| Effective merger | `F_t(y)=F_t(y')` for `y != y'` | Noninjectivity of an already descended reduced map |
| Valid no-right-section obstruction | `G:Y_A -> Y_A` has image diameter below `diam(Y_A)` | Proves nonsurjectivity for the reduced self-map, not for a cross-level projection |
| Stable representative continuation | Uniformly bounded Lipschitz section | Diagnosed by best section condition number; blow-up is not automatically physical |
| Stochastic reduction | Conditional upper measure pushed through evolution and projection | Requires standard Borel spaces, an upper measure, and disintegration |
| Locality descent | Compression of the `P`-compatible upper local net | Preserves isotony and spacelike commutation |

## Application corrections

- **Open systems:** Partial trace is noninjective but has product-state
  representative sections. These do not recover actual correlations.
  Autonomous reduced channels require assignment/compatibility assumptions.
- **Wilsonian reduction:** IR data generally do not decode a unique UV input.
  A selected UV completion is a section; autonomous RG flow and universality
  require theory-space closure and basin stability.
- **Exterior gravity:** Exterior restriction may admit compatible extensions,
  but these do not recover the actual interior. Exterior autonomy requires
  boundary and flux data. Horizon entropy is not a map-theoretic corollary.
- **MTT:** The coherent projector and FP stabilization flow instantiate the
  typed framework only where the descent, stability, and continuation gates
  are independently verified. Gap and projection do not create Born weights,
  entropy, QFT, gravity, or cosmology.

## Resulting scope

The revised paper proves a projection/descent/recovery classification, a valid
finite-diameter nonsurjectivity theorem, a measure-dependent reduced kernel,
and locality descent for compatible coherent observables. It explicitly does
not derive probability, entropy production, temporal direction, universality,
geometry, or Hilbert structure from noninjectivity alone.

## Validation

- Projection–Admissibility v2 permanent theorem audit passes.
- Foundation v7 and all six Fixed Points permanent theorem audits still pass.
- Migration and verifier scripts pass Python syntax validation.
- TeX environment nesting and ASCII/tab guards pass.
- PDF compilation remains blocked by the previously identified local MiKTeX
  dependency `amsthm.sty`; this is an environment issue rather than a detected
  source error.
