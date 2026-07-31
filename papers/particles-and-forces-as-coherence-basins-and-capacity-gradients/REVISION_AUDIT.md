# Particles and Forces Paper v3 Release Audit

## Selected revision

- Paper: `Particles and Forces as Conditional Coherence-Basin Encodings`
- Superseded version: v2.0
- Prior release DOI: `10.5281/zenodo.18322084`
- Selected successor: v3
- Controlling correction authority: A10
- Live blocker: B.ACTION.01, upper action and automorphism transfer

## Context audit

Version 2 was checked against the corrected Version 3 capacity-dynamics paper,
the current MTT action frontier, and the consolidated corpus reconciliation.
The useful idea is retained: stable localized sectors can be represented by
basin-like effective records. The prior paper conflated persistence,
localization, density, mass, force, charge, confinement, and gravity.

Version 3 rebuilds the proposal as a typed conditional encoding and gives an
exact centroid theorem. It does not map curated numerical result packets
because no packet currently supplies the selected action or physical basin
coefficients used by this paper.

## Required corrections and resolutions

### 1. Basin identity and spatial density

**Prior claim:** A basin density uniquely tracks the underlying basin.

**Finding:** The observation map may forget internal labels. Distinct
invariant basins can have identical density and current histories.

**Resolution:** Version 3 proves an explicit product-space counterexample and
defines a complete particle record containing basin, observation map, spatial
data, stresses, action, internal representation, and errors.

### 2. Capacity gradient as force

**Prior claim:** Spatial variation of coherence capacity is an effective force.

**Finding:** A diagnostic margin has no automatic energy dimension or
dynamical coupling. Monotone reparameterizations preserve admissibility but
rescale its gradient.

**Resolution:** Version 3 proves the reparameterization obstruction and
requires a selected capacity-to-potential, action, Hamiltonian, stress, or
mobility law.

### 3. Newtonian motion

**Prior claim:** Newton's second law was derived by defining
`F = M a_eff` after assuming a momentum equation containing `a_eff`.

**Finding:** This renamed an assumed acceleration field and omitted boundary
traction and localization error.

**Resolution:** Version 3 derives the exact centroid balance from continuity
and momentum equations, including boundary stress, and proves a Lipschitz
error bound for the point-particle approximation.

### 4. Integrated density as mass

**Prior claim:** Mass is the integrated basin coherence weight.

**Finding:** Density normalization, inertial kinetic coefficient, spectral
rest mass, and gravitational mass are distinct.

**Resolution:** Version 3 proves a scaling counterexample and states the
additional normalization theorem needed to identify them.

### 5. Lorentz force

**Prior claim:** The Lorentz force follows from preservation of phase
coherence.

**Finding:** The displayed derivation assumed the Hamilton-Jacobi constraint,
gauge connection, charge, and momentum-velocity relation that contain the
desired effective dynamics.

**Resolution:** Version 3 derives the Lorentz term from a declared
gauge-covariant effective action and keeps MTT source selection of that action
open.

### 6. Charge conservation

**Prior claim:** Basin persistence conserves gauge charge.

**Finding:** Persistence alone does not imply a Noether identity or
topological invariance.

**Resolution:** Version 3 gives the conditional gauge-symmetry and current
conservation theorem and distinguishes it from basin persistence.

### 7. Confinement

**Prior claim:** Qualitative non-Abelian coherence strain reproduces
confinement and the Wilson-loop area law.

**Finding:** No gauge-invariant energy, measure, Wilson loop, or coercive
separation estimate was supplied.

**Resolution:** Version 3 proves a conditional finite-energy separation bound
from `V(R) >= sigma R - c` and lists the additional Yang-Mills data required
for a physical confinement claim.

### 8. Gravity and particle-number change

**Prior claim:** Universal gravity and particle-number nonconservation follow
naturally from the basin framework.

**Finding:** Both require dynamics: a common metric action and worldline limit
for gravity, and a transition or field law for merge, split, creation, and
annihilation.

**Resolution:** These are retained as model interpretations and explicit
source obligations, not derived results.

## Frontier after revision

The paper-level correctness blocker is resolved. Stable basins are now scoped
as one component of an effective particle record, and every force statement is
derived from declared dynamics. B.ACTION.01 remains open: one selected upper
MTT action must still source the spatial observation map, kinetic
normalization, physical mass, gauge coupling, stress law, capacity coupling,
transition dynamics, and gravitational response.
