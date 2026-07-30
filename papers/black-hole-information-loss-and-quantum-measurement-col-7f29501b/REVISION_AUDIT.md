# Black-Hole Information and Measurement Paper v2 Revision Audit

## Overall verdict

Version 1 contained a useful coarse-graining intuition but its bridge theorem
was false. It confused noninjective projection with noninvertible effective
dynamics, used a right inverse as though it recovered every microscopic state,
and imposed overlap of images of disjoint sets under an invertible flow.

Version 2 withdraws the claim that measurement collapse and black-hole
information loss are the same physical transition. It replaces it with an
exact quotient-dynamics theorem and a typed channel analogy.

## Claim-by-claim disposition

| Version 1 claim | Finding | Version 2 action |
| --- | --- | --- |
| Barrier crossing forces noninvertible shadow dynamics | Not proved; noninjective projection can support a reversible quotient | Replaced by the necessary-and-sufficient fiber-factorization theorem |
| An invertible flow can map disjoint barrier sectors to overlapping sets | Contradicts injectivity | Added an exact disjointness proposition |
| A right inverse recovers the microscopic state | A right inverse only selects one preimage | Recovery is defined as a left inverse on a declared code |
| Measurement and black-hole loss are the same transition | Physical channels were not constructed | Reclassified as a structural analogy |
| Measurement collapse is a special fundamental process | Unnecessary and contrary to the ordinary instrument description | Measurement is treated as a physical system-apparatus interaction plus record conditioning or loss |
| A horizon is an MTT admissibility barrier | Was asserted, not derived | Retained only as a model assumption pending a selected geometry and channel |
| Islands are partial inverses of projection | Wrong type and domain | Replaced by recovery on a code subspace or observable algebra |
| Born and Hawking weights arise from one basin measure | No common measure or pushforwards were supplied | Withdrawn pending an explicit source theorem |

## New exact results

1. Projected-dynamics factorization through a surjective observation map.
2. Necessary and sufficient criterion for invertibility of the induced
   quotient dynamics.
3. Counterexample showing that a noninjective projection can have reversible
   observable dynamics.
4. Preservation of disjointness by an injective flow.
5. Collision obstruction to exact channel recovery on a code.

## Theorem ownership and scope

The fiber-factorization, disjointness, and collision results are owned by this
paper. Standard quantum-instrument theory and island/entanglement-wedge
reconstruction are imported from their primary literature. No fixed-point,
SPT, or q79 theorem is duplicated here.

## Current MTT boundary

The paper uses MTT projection language as an abstract carrier. It does not
claim a selected black-hole background, horizon channel, measurement
instrument, common Born/Hawking measure, or microscopic evaporation dynamics.
Those are the explicit exit objects.

## Release consequence

The public v1 record at `10.5281/zenodo.18261430` should receive v2 as a major
corrected successor. The scientific abstract is plain and does not contain
the correction history; the version history belongs in the paper and Zenodo
version notes.
