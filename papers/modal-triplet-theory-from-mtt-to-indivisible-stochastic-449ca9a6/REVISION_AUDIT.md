# Indivisible stochastic-process paper revision audit

## 2026-09-12: v3 contextual revision

- The local `paper-markdown.lua` filter follows the repository's existing
  Pandoc pattern to retain all frozen-source citations, the built bibliography,
  revision notes, source labels and theorem reference numbers. It also preserves
  the managed computational-evidence markers and manifest filename; plain Pandoc
  omitted those citation/path details. This does not alter the PDF source.
- Supersedes v2, released as Zenodo record 21665996. The release identity and
  all previous revision notes remain unchanged.
- Integrates all 48 assigned BEQ frozen artifacts, including the full later
  candidate-audit refinements, at manifest commit
  `f141a20ea23c5c3ff19cc2161c0e226e29ade8a7`.
- Explains coherent history versus endpoint populations, all-ADO propagation,
  ideal dilation versus bounded bath-active readout, physical tangent domains,
  the D1-to-D4 chronology, charged lines and connection/holonomy, conditional
  scalar repair, metric-aware error transport, and held-out response tests.
- Preserves canonical operational q79 closure, finite/local compatibility,
  hidden projective and existential HYM conclusions, and ordinary measurement.
- Distinguishes the evolving audit's diagnostic D4 tangents/Hessians from a
  validated full-family numerical enclosure. No heavy calculation is rerun.
- Consumer correction: `sec:metric-qualification` names the missing
  common-norm contraction hypothesis in the BEQ semigroup estimate. General
  Duhamel comparison retains metric-distortion factors. Exact transported
  Hodge/cost identities and the source's diagonal example are retained.
  This correction is also escalated in the review fragment.
- Local lemma correction: `lem:action-kernel` now defines the Borel
  finite-normalization domain and a measurable extension outside it.
- `prop:sufficient` no longer calls an arbitrary standard Borel summary
  finite; finite memory claims must specify the admitted summary class.
- Kernel consumer/text queue C.FP.02 is addressed at
  `sec:recurrence-boundary`: closed pure-point unitary recurrence is distinct
  from mixing in a supplied finite Markov/Lindblad/bath model and from a
  controlled irreversible limit. B.ACTION.01 remains open.
- Verification records and exact source/manuscript/PDF hashes are in
  `editorial-reviews/2026-09-12/stochastic.json`. PDF and Markdown are generated
  locally; no global refresh, catalog change, publication or scientific replay
  is performed by this revision.

## Earlier v2 revision audit

## Release identity

- Paper ID: `modal-triplet-theory-from-mtt-to-indivisible-stochastic-449ca9a6`
- New version: `v2`
- Superseded release: `v1.0`, Zenodo record `18254863`
- Revision class: major theorem-boundary and interpretation correction

## Contextual corrections

### 1. Upper geometry

The former source called

`Y4 x B1 x B2 x B3`

a ten-dimensional manifold even though three independent three-dimensional
factors would give thirteen dimensions. Version 2 uses the reconciled
`Y4 x X6` branch notation. The `1<2<3` Circle-Lens-Nil lanes are operator or
rank data on a shared carrier, not three additional three-manifolds.

### 2. Probability source

The former source defined conditional probabilities in terms of a path measure
and then claimed to construct the path measure from those probabilities. It
also treated deterministic MTT dynamics and projection as sufficient to
generate probability.

Version 2 starts with one of two noncircular inputs:

1. a selected law on upper initial states, then pushes it forward; or
2. an initial law plus measurable conditional kernels, then applies the
   Ionescu-Tulcea theorem.

The selected MTT capture or preparation law remains open.

### 3. Memory and indivisibility

The former theorem "non-Markovianity implies indivisibility" was too broad.
Every classical path law factorizes sequentially through history-dependent
conditional kernels and becomes first-order Markovian when the complete
history is used as the state.

Version 2 defines the narrower phrase `fixed-Q indivisibility` as failure of
the Markov property on the selected observed state space. It separately
defines finite Markov order and proves history-state Markovization.

### 4. Finite sufficient states

The former source inferred infinite memory from dependence on complete-history
notation. This is invalid because the dependence may factor through a finite
or low-dimensional statistic.

Version 2 proves a sufficient-state compression proposition and gives an exact
binary example with infinite observed Markov order but a one-scalar posterior
state.

### 5. Action reconstruction

The former source converted an arbitrary target kernel to
`-hbar log(k)` and then claimed exact MTT realization. That operation is a
Gibbs parameterization of already supplied data. It demonstrates expressive
capacity, not prediction or source selection.

Version 2 retains the normalized action-kernel lemma and explicitly labels
the inverse-log construction as tautological. A physical result requires MTT
to derive the action, scale, reference measure, and equality to the projected
kernel before target probabilities are used.

### 6. Classical versus quantum probability

The former source treated refinement additivity on one classical sample space
as quantum measurement noncontextuality and treated the GNS representation of
a commutative event algebra as a derivation of POVMs and quantum instruments.

Version 2 proves that the represented algebra remains commutative. Born
probabilities, incompatible observables, process tensors, and CP instruments
require an additional noncommutative source theorem.

### 7. Measurement

The former source identified measurement entirely with conditioning and used
postselection to infer no-signaling.

Version 2 treats measurement as an ordinary physical intervention first.
Conditioning is the subsequent probability update after an outcome is known.
Operational no-signaling is a constraint on intervention-dependent marginals,
not a generic consequence of Bayesian conditioning.

## Results owned by version 2

This paper owns the MTT-specific synthesis of:

- the conditional projected-path theorem;
- the fixed-state indivisibility definition and its exact scope;
- the history-state Markovization correction;
- the finite sufficient-state completion test;
- the exact binary projection example;
- the classical-to-quantum boundary for the MTT stochastic shadow.

The Ionescu-Tulcea theorem and general complete-connection results are cited
standard mathematics, not claimed as new MTT theorems.

## Status after revision

The paper now proves a rigorous conditional stochastic-shadow result. It does
not claim a first-principles derivation of the source probability law or a
derivation of quantum mechanics from a classical path algebra.
