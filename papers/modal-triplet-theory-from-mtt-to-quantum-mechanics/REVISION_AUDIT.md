# Revision Audit: MTT and Nonrelativistic Quantum Mechanics

Date: 2026-07-30

Paper id:
`modal-triplet-theory-from-mtt-to-quantum-mechanics`

Selected revision:
Version 4

Superseded release:
Version 3, DOI `10.5281/zenodo.18261329`

## Revision purpose

Version 3 mixed standard quantum/operator mathematics with MTT source claims.
Version 4 reclassifies the general result as a coherent-sector
reconstruction, preserves the exact selected q79 binary-recorder result at
its current domain, and leaves the universal Born-source theorem open.

The paper remains a standalone explanatory bridge from MTT to
nonrelativistic quantum mechanics. It is not a correction list and does not
transfer ownership of standard theorems or the q79 source theorem.

## Current authority lock

Kernel model:
`a78e96e00159bbac534dd421ef2427fabb34b0fbcf57a92b2087a410e7eb7c20`

Repository starting head:
`bacd13201708380824630260f2494af1864d9583`

Controlling authorities:

- `A03`, conditional:
  `d42e7eb590fe1caa8f51affd6e27745af1ed9564a690d1bb39ffe0f05ad049b2`.
  Standard SM BRST/Faddeev-Popov quantization is imported, not derived from
  MTT.
- `A05`, open:
  `ced380228f057c089181a779aba9b9ad15799031e4475ed09d4d34e91032cda7`.
  The strict upgrade ledger is not zero-knob global closure.
- `A10`, recorded:
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.
  The master corrigendum applies subject to successor decisions.
- `A18`, conditional/open:
  `7287df306cc3832fb1cccbed43f8794eaa44576799f46fe526f882df2463a1a3`.
  Six conditional quantization and four finite-domain constructive QFT
  results do not close capture measure, general BRST, continuum, or full
  four-dimensional obligations.

Controlling blocker:

- `B.QM.01`, P0, open globally.
  The canonical q79 binary one-anchor recorder has an exact stopped
  operational output measure and exact second-moment capture descent on its
  selected commuting Fock output algebra. Arbitrary apparatus contexts,
  finite-bandwidth/non-Markov control, pre-quantum probability semantics,
  and objective one-history selection remain open.

## Selected q79 source lock

Repository:
`https://github.com/PeterNero/mtt-qm-source-proof`

Commit:
`1615da7e1b2c917556fe04a44d073b905644071e`

Source theorem:

`proof_corpus/Canonical_q79_Fock_Output_Measure_and_Second_Moment_Capture_Descent_Theorem_v1.md`

SHA-256:
`3d22a3be695cffa9f1366dd173b1cd544a9d0e3764722a2a3187919364175978`

Certificate:

`certificates/canonical_q79_fock_output_measure.certificate.json`

SHA-256:
`483404470854e6a888f890ad129160b52d3ca38c6a471b73947da5e78d34496e`

Assessment:

`reports/QM01_CANONICAL_OUTPUT_MEASURE_ASSESSMENT_2026-07-23.md`

SHA-256:
`4a2adf6ab52f081f90bc2e863639e9d5756835b2eb35258dac283ce21b280f11`

## Claim-by-claim audit

### Complete first-principles derivation

Version 3 claim:
MTT completely derives nonrelativistic quantum mechanics.

Decision:
Withdraw.

Version 4 resolution:
Define the complete lower quantum record and prove a conditional
reconstruction theorem. General source selection is not claimed.

### Literal ten-dimensional tri-product

Version 3 claim:
The lower theory begins from a literal product
`Y4 x B1 x B2 x B3`.

Decision:
Retire as canonical geometry.

Version 4 resolution:
Use the current MTT ten-dimensional bundle over a four-dimensional
Lorentzian base with compact six-dimensional fiber. No old three-factor
internal product is used as a proof source.

### Hilbert and symplectic structure

Version 3 claim:
Projection constructs the reduced Hilbert and symplectic structure.

Decision:
Narrow.

Reason:
An orthogonal projector does not supply multiplication by `i`, a compatible
complex structure, or a symplectic form.

Version 4 resolution:
The source record must emit a complex Hilbert space, or a real Hilbert space
with a compatible complex structure. The relation among the real metric,
complex structure, and symplectic form is explained explicitly.

### Noncommutativity

Version 3 claim:
Compression to the coherent sector yields quantum noncommutativity.

Decision:
Withdraw as an implication of projection.

Version 4 resolution:
The observable algebra is an independent source row. Compression preserves
an algebra only under suitable invariance conditions.

### Quadratic-form Hamiltonian

Version 3 claim:
A bounded pullback of a closed semibounded form is closed and gives the
reduced self-adjoint Hamiltonian.

Decision:
Correct.

Reason:
Bounded pullback alone does not preserve the completeness needed for
closedness, and a nonreducing coherent range can remain coupled to discarded
modes.

Version 4 resolution:
Prove a sufficient closed reducing-pullback proposition using an isometric
closed range, form-domain invariance, form reduction, and a dense lower
domain. Explain the Schur-Feshbach correction when the sector is not
reducing.

### Unitary evolution

Version 3 claim:
Unitary evolution follows automatically after projection.

Decision:
Narrow.

Version 4 resolution:
Stone's theorem gives unitary evolution after a self-adjoint Hamiltonian and
evolution parameter have been supplied. Time-dependent propagation remains
conditional on the relevant Kato hypotheses.

### Arbitrary Schrodinger operators

Version 3 claim:
Exact realization of any broad Kato-Rellich Schrodinger operator is an MTT
derivation.

Decision:
Reclassify as exact representability.

Reason:
The construction chooses upper data containing the same target potential.

Version 4 resolution:
Prove an exact direct-sum target-embedding proposition and state explicitly
that it tests expressiveness and the decoder, not parameter selection or
prediction.

### Time-energy uncertainty

Version 3 claim:
A self-adjoint time generator and Robertson inequality yield a universal
`Delta t Delta E` relation.

Decision:
Withdraw.

Version 4 resolution:
Treat time as an evolution parameter or a supplied physical clock/clock
POVM. Use the operational Mandelstam-Tamm relation for a chosen observable.

### Gleason, Busch, and the Born rule

Version 3 claim:
Re-coherence weights plus a functional equation and Gleason-Busch derive the
Born rule without postulates.

Decision:
Withdraw globally.

Reason:
Gleason- and Busch-type results characterize probability assignments after
Hilbert/effect structure and additivity or noncontextuality assumptions are
supplied. They do not source a detector or the physical probability
semantics.

Version 4 resolution:
Separate probability characterization, operational instrument sourcing, and
pre-quantum/ontic actualization.

### Selected q79 output measure

Current source result:
The q79 binary one-anchor recorder emits the effects

```text
F_u(r_u)   = exp(-gamma u) I
F_u(ds,a)  = gamma exp(-gamma s) P_a ds
gamma      = log 448
```

and hence the stopped output law

```text
mu(r_u)    = exp(-gamma u)
mu(ds,a)   = gamma exp(-gamma s) Tr(rho P_a) ds.
```

Decision:
Retain exactly at the selected canonical binary operational tier.

Version 4 resolution:
Explain the theorem, cite its owner and immutable commit, and state that it
uses standard normal-state operational semantics. Do not promote it to
arbitrary apparatuses, pre-quantum probability semantics, or objective
single-history selection.

### POVMs and dilation

Version 3 claim:
Naimark/Stinespring automatically realizes all POVMs inside MTT.

Decision:
Narrow.

Version 4 resolution:
Treat dilation as standard representation mathematics. The ancilla,
isometry, coupling, pointer algebra, and apparatus context remain source
rows.

### Measurement

Version 3 tendency:
Measurement is treated as a special completion event.

Decision:
Clarify.

Version 4 resolution:
Measurement is an ordinary physical interaction plus a record, represented
by an instrument. No consciousness or privileged observer boundary is
introduced.

### Entanglement and locality

Version 3 claim:
Entanglement is the preferred generic MTT encoding and its propagation and
force mediation follow from the upper construction.

Decision:
Narrow substantially.

Version 4 resolution:
Entanglement follows once a physical tensor-product composition rule is
supplied. Standard local CP maps imply operational no-signalling.
Upper-local explanations of Bell correlations require a separate map that
preserves settings, local algebras, and independence assumptions.

### Open systems

Version 3 claim:
Modal disturbances generically yield Lindblad dynamics.

Decision:
Reclassify as conditional.

Version 4 resolution:
Use GKSL and Davies results only under their standard Markov,
weak-coupling, spectral, and correlation hypotheses. Retain non-Markov
effects as an open detector-control obligation.

### Path integrals and semiclassics

Version 3 claim:
The path integral and stationary-phase kernel are independently derived from
MTT.

Decision:
Narrow.

Version 4 resolution:
Treat them as alternative or asymptotic representations after the
Hamiltonian, action, measure/regularization, and boundary data are supplied.

### Algorithmic irreducibility

Version 3 content:
A broad discussion of limits of predictability and algorithmic
irreducibility.

Decision:
Remove from this paper.

Reason:
It is not needed for the QM reconstruction theorem and has independent
computability obligations.

## Local theorem ownership

Version 4 owns only:

1. the definition of the complete QM reconstruction record;
2. the conditional MTT-QM reconstruction theorem;
3. the sufficient closed reducing-pullback proposition; and
4. the exact target-embedding proposition and its interpretation.

Stone, Kato, representation, Gleason, Busch, Naimark, Stinespring, GKSL,
Davies, and Mandelstam-Tamm results retain literature ownership.

The q79 output-measure theorem remains owned by the source-proof repository.
This paper explains its hypotheses, formulas, domain, and implication without
copying its proof block.

## Expository review

The revision:

- states the problem, contribution, claim tier, and limitations in the
  abstract and introduction;
- defines every central lower structure and explains why it is independent;
- gives the dependency chain from source record to reconstruction;
- interprets every local formal result;
- contains a two-level recorder example and a harmonic-oscillator embedding
  example;
- relates the result to current MTT geometry and quantization status;
- distinguishes exact, conditional, imported, and open claims; and
- gives a ten-row completion contract.

## Frontier delta

Before:
The released paper claimed a universal first-principles QM and Born-rule
derivation using several unproved or incorrect implications.

After:
The paper now gives a correct general coherent-sector reconstruction
contract, a valid form/compression analysis, and the exact selected q79
binary output-measure result at its declared tier. `B.QM.01` remains open
globally, exactly as required by the current Kernel row.

## Release verification

Completed on 2026-07-30:

- `pdflatex`, `bibtex`, and two final `pdflatex` passes completed
  successfully;
- the final log contains no unresolved citations, references, overfull
  boxes, or LaTeX warnings;
- all 18 PDF pages were rendered and visually inspected;
- Markdown, descriptive metadata, source hashes, and the managed
  reproducibility section were regenerated and verified;
- theorem ownership passed with 528 scoped formal results and zero known
  duplicate-body groups;
- strict boilerplate, Book-role, local release, and canonical repository
  verifiers passed;
- Zenodo metadata contains a content-only abstract, separate revision notes,
  18 explicit references, and two repository identifiers;
- the published record contains exactly one file, `main.pdf`, with SHA-256
  `11d3c508932549006540c512b4db81ebe0f70bcbf7ade04928996ef7c4367f0c`;
- version 4 was published as DOI `10.5281/zenodo.21708961`, preserving concept
  DOI `10.5281/zenodo.17074246`; and
- the publication ledger and canonical paper metadata were reconciled to
  the published record.

The final Git heads and Kernel refresh are recorded in the durable research
handoff.
