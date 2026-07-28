# Decoherence and measurement paper v2 revision audit

## Selected revision

- Paper: `Why Decoherence Cannot Replace Measurement`
- Superseded source: version 1.0
- Superseded source SHA-256:
  `9128b63a8527d106a5df6a6cdb84697dc22dc17ab6a84996fa1d56923bdb4402`
- Selected successor: version 2
- Controlling authorities: `A03`, `A05`, `A10`, `A18`
- A10 SHA-256:
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`
- Current blocker boundary: `B.QM.01`
- Durable research handoff:
  `78dc7d4d-3289-40c8-8681-d562992b825f`

## Verdict

The central negative thesis survives: decoherence suppresses interference and
stabilizes records but does not, by itself, select an outcome. The prior paper
did not consistently respect that thesis. It repeatedly replaced the missing
selection law with assertions that noninvertible projection, admissibility
loss, or a basin boundary enforces capture.

Version 2 makes the distinction exact without giving measurement fundamental
status. Measurement is an ordinary system--apparatus--environment interaction
described with its record retained. A decoherence channel is the
record-discarded, nonselective completely positive trace-preserving
description. An outcome-resolved description is an instrument or normalized
continuation kernel. The former does not determine the latter.

## Required corrections

### 1. Retain intra-basin suppression versus inter-basin selection

**Prior state:** The conceptual distinction was useful, but basin membership,
pointer structure, and projection-enforced transitions were treated as already
derived.

**Resolution:** Version 2 states a conditional typed basin theorem. If a
selected source emits basins, basin-preserving channels, record algebra, and a
completion instrument, then decoherence and measurement can be represented as
intra- and inter-basin resolutions of the same ordinary physical process.

**Status:** Resolved.

### 2. Add the missing selection-completion map or kernel

**Prior state:** A trajectory reached a boundary and was said to be captured,
but no normalized outcome map, conditional update, or continuation law was
defined.

**Resolution:** Version 2 defines:

- a quantum instrument of completely positive trace-nonincreasing outcome maps;
- its outcome probabilities and conditional states;
- a normalized boundary completion kernel with successor-basin support; and
- the corresponding nonselective barycenter.

It proves that boundary membership does not select this kernel.

**Status:** Resolved.

### 3. Do not infer outcomes or probabilities from decoherence or chart exit

**Prior state:** The paper correctly said decoherence is insufficient, then
asserted that projection supplies single outcomes, Born weights,
irreversibility, and structural undecidability.

**Resolution:** Version 2 gives an exact counterexample. One qubit dephasing
channel is the nonselective sum of instruments with different probability laws
and conditional states. It separately constructs two incompatible
continuation kernels satisfying the same chart-exit data. Born weights,
objective outcomes, an entropy arrow, and undecidability are therefore listed
as independent source obligations.

**Status:** Resolved.

## Exact theorem content

Version 2 proves:

1. complete positivity, trace preservation, coherence suppression, and
   population preservation for finite pointer dephasing;
2. underdetermination of an outcome instrument by its nonselective channel;
3. non-selection of outcomes and probabilities by decoherence;
4. non-selection of a continuation kernel by chart exit;
5. a conditional suppression-selection bridge for typed MTT basin models.

## Current MTT frontier preserved

The paper records, without enlarging, the current canonical-domain result:

- the q79 binary one-anchor Fock recorder has an exact stopped-output law and
  SecondMomentCaptureDescent on its declared finite-symbol domain;
- no observed probability or fitted stochastic primitive is added there.

It does not claim:

- a universal apparatus source map;
- finite-bandwidth or non-Markov completion;
- objective actualization of one ontic history;
- a universal Born-source theorem;
- selection from every MTT admissibility boundary.

Those are the stronger open rows in `B.QM.01`.

## Additional contextual repairs

- Measurement is explicitly treated as ordinary record-forming physics, not a
  privileged act, observer intervention, or separate dynamical law.
- The completion map completes the effective description; it is not an extra
  operation performed by nature.
- Noninjectivity is no longer called the source of irreversibility or
  selection.
- Quantum Darwinism is discussed as record redundancy, not as a theory that
  secretly presupposes MTT basin capture.
- Continuous trajectories are treated as outcome-resolved unravellings, not
  proof of an MTT structural origin.
- Collapse-like behavior is not asserted to follow from reduced margins.
- Algorithmic undecidability now requires an explicit computable reduction.
- The statement that probability follows from undecidability is withdrawn.
- A universal promotion contract makes every future measurement claim
  testable.

## Context checked

- corrected projection/probability/irreversibility version 3;
- gravitationally induced collapse version 3;
- current `ENC.QM.BORN` and `B.QM.01` status;
- Davies--Lewis quantum instruments;
- Zurek and Schlosshauer decoherence analyses.

## Publication delta

Version 2 is a minor-scope but substantive theorem-status correction. It should
be uploaded as a new Zenodo version with the generated PDF, canonical TeX,
Markdown conversion, and this revision audit.
