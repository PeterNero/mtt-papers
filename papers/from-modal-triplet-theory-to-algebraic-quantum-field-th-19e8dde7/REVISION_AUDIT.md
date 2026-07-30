# Admissibility Precosheaves and Conditional AQFT Nets in MTT v2 Revision Audit

## Source lineage

- Superseded title: `From Modal Triplet Theory to Algebraic Quantum Field Theory: Local Nets from Admissible Charts and Coherent Basin Persistence`
- Superseded source: `7 Quantum Field Theory/_work/From_Modal_Triplet_Theory_to_Algebraic_Quantum_Field_Theory`
- Public v1 record: Zenodo `10.5281/zenodo.18330770`
- Selected successor: `mtt-papers/papers/from-modal-triplet-theory-to-algebraic-quantum-field-th-19e8dde7/main.tex`
- Successor title: `Admissibility Precosheaves and Conditional AQFT Nets in Modal Triplet Theory`
- Successor version: `v2`
- Governing correction authority: A10, `MTT_Master_Corrigendum_and_Revision_Plan.md`

The stable paper ID is retained. The v2 source is authored directly in the flat
canonical paper store and supersedes the grouped v1 source without recreating
that authoring tree.

## Disposition of the v1 construction

The v1 chart-only derivation of an AQFT net is withdrawn. Three central
implications were not valid:

1. inclusion of admissible chart domains does not automatically extend every
   smaller-chart observable;
2. absence of a common representability chart does not imply that two
   observables commute; and
3. absence of one global chart does not prevent an abstract quasilocal algebra
   or categorical colimit.

The first implication lacked a selected algebra homomorphism. The second tried
to assign zero to a commutator whose operands had not been placed in a common
algebra. The third confused an object in the indexing category with a
universal object constructed from the whole diagram.

## Required corrections and their resolution

| A10 requirement | v2 resolution |
| --- | --- |
| Base the physical net on the FP VI upper local route and locality descent | FP VI's local-hyperbolic-parent requirement is separated from Projection v2's exact coherent-compression theorem |
| Do not infer commutation from failure of joint representability | A typed non-comparability proposition proves that the commutator is undefined until a common realization is supplied |
| Do not assume automatic observable extension | The admissibility precosheaf requires explicit unital injective star-homomorphisms and functoriality |
| Inherit isotony from upper inclusions and reduction | The physical-net theorem proves inclusion after restricting to the common `P`-compatible upper subalgebra |
| Preserve abstract global algebra possibilities | The quasilocal inductive limit and more general colimit are explicitly restored |
| Narrow the global obstruction | Only a single global admissible chart is excluded by the chart statement; selected compatible states or admissible physical representations need separate obstructions |
| Separate pregeometry from Haag--Kastler AQFT | Distinct sections define the admissibility precosheaf, Lorentzian physical net, and the natural chart-to-region interface |

## Corrected theorem chain

### Pregeometric level

An admissibility-indexed precosheaf is a conditional functor

```text
B : C_adm -> Alg.
```

Its algebra objects and extension morphisms are data or theorem outputs. Raw
domain overlap does not determine them. Without a causal base, this functor is
not a physical Haag--Kastler net and has no spacelike-commutation statement.

### Physical level

The physical theorem assumes:

```text
selected globally hyperbolic Lorentzian base (Y,g)
bundle pi : M -> Y
upper isotonic local net A_U(pi^-1 O)
decomposable orthogonal coherent projector P
P-compatible upper observable subalgebras.
```

It defines

```text
A_P(O) = { P A P restricted to P H_U : A in A_U^P(O) }.
```

Compression is a star-homomorphism on the compatible subalgebra. Upper
inclusion therefore gives isotony, and upper spacelike commutation gives

```text
[PAP, PBP] = P[A,B]P = 0.
```

The theorem inherits locality; it does not create locality from chart
non-comparability.

### Interface level

A selected region-to-context functor `L` and component maps

```text
rho_O : B(L(O)) -> A_P(O)
```

must satisfy

```text
rho_O2 o j_12 = iota_12 o rho_O1.
```

Only componentwise isomorphisms establish equivalence of the pregeometric and
physical nets. This naturality condition is the precise remaining
chart-to-region intertwiner.

## Global algebra, state and representation correction

- A directed local C-star net can possess a quasilocal inductive-limit algebra
  even without a largest indexing region.
- A compatible family of local states defines a state on that inductive limit.
- Every abstract C-star algebra has a faithful Hilbert-space representation.
- What may fail is a selected single-chart state or representation satisfying
  all MTT admissibility and physical-selection requirements.

The v2 paper therefore makes no unqualified no-global-algebra, no-state or
no-faithful-representation claim.

## Horizon and irreversibility correction

An AQFT net may assign algebras on both sides of a horizon. Observer access,
thermal/modular behavior and information statements require a spacetime, net
and state. An MTT admissibility boundary is not a physical horizon until the
chart-to-region interface and causal theorem identify it as one.

Likewise, failure of chart continuation does not prove a temporal arrow.
Oriented dynamics plus a semigroup, monotone functional or asymmetric boundary
condition remains necessary.

## Current-corpus status incorporated

- FP VI v4: an instantaneous equal-time bilocal kernel is not microcausal; a
  local hyperbolic parent is the valid conditional route.
- Projection--Admissibility v2: compatible fiberwise compression preserves
  isotony and spacelike commutation.
- q79 gravity frontier: a Lorentzian coframe and causal representative are
  conditionally available after `A_QG + A_causal`; this does not create a QFT
  net.
- A18: finite-domain SPT-filtered TT/BRST constructive results are partial;
  infinite volume, full chiral SM, Lorentzian reconstruction and the complete
  nonperturbative BRST Hilbert space remain open.
- A03: the selected perturbative SM observable functor imports standard
  BRST/Faddeev--Popov quantization rather than deriving it from MTT.

The later selected-QFT result is incorporated at its declared tier: a
globally hyperbolic framed q79 representative and twisted massless Dirac
source compose with standard CAR/AQFT results to give a closed even free
observable net with locality, covariance, time slice, and nonempty positive
Hadamard state space. This does not close the chart-to-region naturality map
or the interacting physical C-star completion.

## External standard checked

The rewrite follows the standard distinction between:

- a Haag--Kastler net on regions of a fixed causal spacetime;
- a locally covariant functor on globally hyperbolic spacetimes and causal
  embeddings; and
- an abstract quasilocal/inductive-limit algebra assembled from local
  algebras.

Primary anchors are Haag--Kastler (1964), Brunetti--Fredenhagen--Verch
(`math-ph/0112041`) and Chilian--Fredenhagen (`0802.1642`).

## Edition delta

This is a structural rewrite. The abstract, central construction, isotony
proof, locality proof, global-algebra claim, horizon interpretation and
conclusion have all been replaced. The useful retained idea is limited to the
following: admissible contexts can index partial algebraic descriptions, and
an already local upper theory can retain locality after a compatible coherent
compression.

## Validation record

- A10 requirements: mapped one by one above.
- FP VI and Projection v2 interfaces: checked at their selected scopes.
- Current A03/A18 QFT status: retained as conditional/partial.
- The current source compiles successfully with two `pdflatex` passes.
- The complete PDF is rendered and visually inspected before release freeze.
