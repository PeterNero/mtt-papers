# Revision Audit

## Paper

- ID: `quantum-field-theory-reconstruction-from-coherence-basi-ef12097a`
- Selected predecessor: Version 2, DOI `10.5281/zenodo.18322089`
- Revised version: Version 3
- Controlling authorities: `A03`, `A10`, and `A18`
- Current blockers: `B.QFT.01` closed; `B.QFT.02` open
- Mapped numerical results: none

## Why a rewrite was required

Version 2 began with a classical probability measure on coherence basins
and correctly obtained linear expectations. It then extended the
commutative GNS representation to noncommuting operators without defining
an algebra, state, or quantization functor. From that unsupported step it
claimed quantum fields, propagators, path integrals, renormalization,
Feynman rules, and a capacity-based QFT breakdown theorem.

The current corpus has a stronger but differently sourced result. The
selected q79 geometric branch now supplies a free twisted-Dirac even-CAR
local net through standard AQFT machinery. That theorem is owned by the
companion MTT-to-QFT paper and must not be duplicated here.

## Exact corrections

| Previous claim | Version 3 resolution |
|---|---|
| Basin ensembles generate the linear structure of quantum states. | Basin measures have an exact commutative multiplication representation on `L2`. Convexity gives mixtures, not coherent phase superposition. |
| A commutative GNS construction can be extended to incompatible noncommuting basin partitions. | Withdrawn. No such extension is selected by the classical data. CCR/CAR structure requires an independent algebra and dynamics. |
| Basin density fluctuations become operator-valued quantum fields. | Replaced by a typed interface: selected quantum states produce classical basin or record laws through commuting subalgebras, POVMs, or instruments. |
| A classical covariance is equivalent to a QFT propagator. | Replaced by a four-kernel distinction among classical covariance, advanced/retarded Green kernels, quantum two-point functions, and Feynman kernels. |
| A classical characteristic functional reproduces the path integral. | Restricted to classical moments. Quantum reconstruction requires additional algebraic, causal or Euclidean, positivity, and state hypotheses. |
| Capacity coarse-graining derives RG flow. | Withdrawn. Capacity can control a domain or error; beta functions require an action/algebra, scale prescription, regulator or subtraction scheme, and matching. |
| Feynman diagrams enumerate basin statistics. | Narrowed. Diagrammatics can occur in both settings, but QFT diagrams require the specified free propagator, interaction, grading, time ordering, and renormalization prescription. |
| QFT fails universally when capacity vanishes. | Withdrawn. A vanishing declared margin marks the end of that effective model's certified domain, not a universal theorem about QFT. |
| QFT is reconstructed from basin statistics. | Replaced by an exact state-restriction/state-extension interface and the separately selected free q79 CAR source. |

## New exact content

- Commutative basin representation theorem.
- Corollary that classical probability alone cannot supply CCR/CAR.
- Explicit two-level family with one fixed classical law and different
  quantum coherences.
- Classical-law nonselection proposition.
- State restriction and extension interface theorem for a commutative
  subalgebra of a unital C-star algebra.
- Local record-subalgebra and instrument interpretation.
- Typed separation of four different kernels.
- Generating-functional and renormalization boundaries.

## Theorem ownership

The selected free q79 twisted-Dirac even-CAR local-net construction remains
owned by:

> *Modal Triplet Theory and Quantum Field Theory on Curved Spacetime: A
> Selected Free CAR Net and the Interacting Reconstruction Boundary*,
> Version 4, DOI `10.5281/zenodo.21665998`.

The present paper imports that theorem and owns only the complementary
classical-statistics/interface results. It does not rename or reprove the
CAR theorem.

## Current MTT frontier

- `B.QM.02`: closed selected finite quantum model.
- `B.QFT.01`: closed selected local free-QFT source.
- `A03`: conditional perturbative observable functor; standard SM
  BRST/Faddeev-Popov quantization is imported.
- `A18`: conditional and constructive finite-domain quantization/QFT
  results with explicit remaining obligations.
- `B.QFT.02`: open geometry-selected nonperturbative interacting
  gauge-BRST C-star bridge, state selection, RG/matching, uncertainty, and
  observable comparison.

## Release

- Published version DOI: `10.5281/zenodo.21714936`
- Concept DOI: `10.5281/zenodo.18256429`
- Release date: 2026-07-31
- PDF: 13 pages, one canonical `main.pdf`
- Zenodo metadata: plain-text abstract, 13 explicit references, two
  repository relations, and no numerical-capsule claim
- Final TeX SHA-256:
  `54382b40794f6a0c0c77f151b4750262a84cc7c75d9089dc433f547e26fbdbf5`
- Final PDF SHA-256:
  `86becfcdb3c181d5b1b0de1f580695c2024efc5cf22ffdc298b51f620b34f0f5`
- Final source-tree SHA-256:
  `cf29ec96df63d92191ec0aa8490cc0e6c04f8c24db63f781b81b3c05e305abed`

The LaTeX/BibTeX build, complete PDF visual inspection, expository
readability gate, theorem-ownership gate, book-role gate, release
requirements, repository verifier, exact remote-draft verifier, and frozen
artifact check passed before publication. Kernel refresh and the full Kernel
test suite are recorded in the durable research handoff.
