# Proto-Spinor v7 Release Audit

## v7 publication delta

- **Supersedes:** v6.
- **Reason:** loop memory, double covering, finite q79 return, and physical
  fermions needed to be separated into four readable layers.
- **Resolution:** add the rotation-lift picture and explicit finite-return
  calculation without changing theorem status.
- **Retained:** every v6 shared-line and SpinC-return result.
- **Remaining:** global Spin, nonflat FM/HYM, continuum intertwining, and
  Lorentzian particle dynamics.

**Date:** 2026-07-22  
**Selected source:** `The_Proto_Spinor__Conditional_Spinorial_Closure_and_q79_Interface_v6/main.tex`  
**Supersedes:** Proto-Spinor v5

## Current status

Version 6 upgrades the q79 proto-spinor interface from a local binary-dihedral
lift to an exact flat differential-line and finite SpinC-Fourier return
theorem. The strict global Spin obstruction, physical nonflat FM/HYM lift,
world-in-world continuum intertwiner and Lorentzian particle theory remain
open and are not inferred from the finite result.

## Changes in this version

1. Added the universal `Z64` line and exact determinant/CLN/root-plane/Hessian
   pullback theorem.
2. Derived the common BHT-Hori operator `J_FM`, including
   `J_FM^T J_FM=I` and `J_FM^2=-I`.
3. Added the rank-two complex polarizations `(I minus/plus i J_FM)/2`.
4. Proved the `S3 -> Z64` quarter-root no-go and moved the lift to the correct
   binary sheet group `Dic3`.
5. Added the exactly two conjugate phase-root maps, producing
   `(plus/minus i J_FM)^2=I` with no fitted selector.
6. Added the Boothby-Wang interpretation of Lens and Nil as parallel, not
   nested, circle-bundle geometries.

## Evidence used

- `Q79_UNIVERSAL_SHARED_DIFFERENTIAL_LINE_AND_FINITE_OPERATOR_INTERTWINER_v1.md`
- `Q79_BHT_HORI_CLIFFORD_POLARIZATION_AND_DOUBLE_RETURN_v1.md`
- `Q79_BINARY_SHEET_FM_SHARED_ROOT_AND_SPINC_RETURN_v1.md`
- their executable JSON certificates and builders

## Nonpromotion guards

- SpinC cancellation is not a strict global Spin lift.
- The two conjugate `plus/minus i` lifts are orientations of one determinant
  structure, not proof of two observable universes.
- Double return is a finite representation theorem, not periodic physical
  time, flat spacetime, or zero gravity.
- The physical continuum HYM connection and Hessian still require a separate
  same-source comparison.

## Expository revision, 2026-07-28

The v6 theorem set and nonpromotion guards are unchanged. The paper now opens
with a four-layer reading guide separating the local comparison field,
conditional spin lift, selected q79 finite carrier, and downstream physical
fermion theory. A continuous `2 pi`/`4 pi` frame-lift explanation makes the
double-cover theorem concrete without importing a Dirac action or particle
ontology.

The exact finite return is explained directly from
`J_FM^2 = -I` and the conjugate `+i/-i` roots. Further discussion clarifies
that the rank `1+2+3` entries are algebraic carrier roles rather than particle
assignments, and that SpinC phase compensation does not close the independent
global Spin obstruction. No open continuum or Lorentzian gate was promoted.
