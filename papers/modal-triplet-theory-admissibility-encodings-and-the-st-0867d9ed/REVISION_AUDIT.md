# Admissibility and Encodings roadmap v12 revision audit

## Selected revision

- Paper: `Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description`
- Superseded source: version 11
- Superseded source SHA-256:
  `05123cdde5dcea6de34752d82562c478958429d9b8ea5c4449ff021f64488de2`
- Selected successor: version 12
- Controlling correction authority: `A10`
- A10 SHA-256:
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`
- Durable research handoff:
  `e8073801-21e4-4a78-87e7-8882224978d8`

## Context audit

Version 11 was checked against selected Programs A0-A2, B0-B5, C, and D1;
Foundation v8; the corrected fixed-point and Theta papers; and current A/B
status rows.

The original purpose remains valuable: this paper should be the conceptual
roadmap for the MTT corpus. Its static index and several summaries, however,
predated the major theorem corrections now selected elsewhere. In particular,
it repeated the invalid right-inverse inference, treated Circle-Lens-Nil as
exhaustive, described ten dimensions as minimally necessary, interpreted
encoding failure as universal termination of physical description, and marked
multiple target-compatible reconstructions as closed derivations.

Version 12 is therefore a structural rewrite. It retains the roadmap function
while making the type system, dependency order, proof tiers, and current open
source obligations explicit.

## Required corrections and resolutions

### 1. Canonical physical geometry

**Prior state:** The roadmap referred to a high-dimensional modal space and a
ten-dimensional bundle with three geometric components without consistently
separating base, fiber, bundle, and operator data.

**Finding:** Coordinate dimensions, bundle ranks, line-bundle phase, and
operator sectors are different types.

**Resolution:** Version 12 adopts the canonical physical convention
`pi:M10 -> Y4` with six-dimensional compact fiber `X6`. The triplet is
represented by typed vertical bundles/operators/projectors. A line bundle does
not add a coordinate, and the shared circle is not physical time.

**Status:** Resolved.

### 2. Invalid right-inverse argument

**Prior claim:** At an admissibility boundary the coherent projection loses a
right inverse because it is noninjective.

**Finding:** A noninjective surjection may have a right inverse. Noninjectivity
instead obstructs a left inverse/exact upper decoder.

**Resolution:** Version 12 defines representative sections, exact upper
decoders, autonomous descent, and merger separately. It proves the
fiber-preservation criterion for descent and gives an explicit noninjective
projection with a smooth section.

**Status:** Resolved.

### 3. Circle-Lens-Nil exhaustiveness and forced responses

**Prior claim:** Every global coherence failure reduces to exactly Circle,
Lens, or Nil, which uniquely force gravity, gauge structure, and quantization.

**Finding:** The selected B-series no longer proves exhaustiveness or unique
physical response. The labels occur in several mathematical categories.

**Resolution:** Version 12 retains CLN as a typed, non-exhaustive taxonomy.
Each physical response is conditional on additional geometry, dynamics, state,
and observable assumptions. Literal `S1 x Lens3 x Nil3` and automatic manifold
nesting are excluded from the canonical physical geometry.

**Status:** Resolved.

### 4. Ten-dimensional necessity

**Prior claim:** A minimal realization is ten-dimensional.

**Finding:** The dimension count follows only after a four-dimensional base
and three transverse two-dimensional internal factors are assumed.

**Resolution:** Version 12 proves a conditional theorem: if
`X6=F1 x F2 x F3` and each surface carries a nonzero area curvature form, then
the total product is `4+2+2+2=10` and the three pulled-back curvatures are
independent. The paper explicitly denies uniqueness or necessity.

**Status:** Resolved.

### 5. Framework derivation and closure language

**Prior claim:** QM, QFT, GR, SM, strings, QG, AQFT, and related formalisms
were recovered or closed across broad domains.

**Finding:** Different papers provide typed embeddings, conditional
reconstructions, finite selected packets, profile replay, or interpretive
bridges. These are not one theorem tier.

**Resolution:** Version 12 introduces levels L0-L4 and gives a framework table
that states both current contributions and remaining physical obligations.
No target-compatible reconstruction is called a full derivation without a
selected source, dynamics, state, observables, uncertainty, and held-out test.

**Status:** Resolved.

### 6. Boundary language

**Prior claim:** Beyond an admissibility boundary physical description ceases
to exist in every meaningful sense.

**Finding:** Failure of a gap, projector, descent law, basin, or section
continuation proves loss of control for the declared chart. It does not exclude
all other charts.

**Resolution:** Version 12 defines controlled charts and named margins and
proves that local loss of control does not imply universal nonexistence. A
post-boundary reset, instrument, or branch rule remains additional data.

**Status:** Resolved.

### 7. Static status index

**Prior state:** A long paper-by-paper table used broad labels such as
`closed` and `mostly closed`.

**Finding:** The table became stale as successor papers and calculations
changed.

**Resolution:** Version 12 replaces it with stable conceptual classes, a dated
frontier snapshot, per-paper revision audits, and an explicit rule that live
A/B rows and selected source hashes control current status.

**Status:** Resolved.

## Current theorem content

Version 12 proves:

- the exact fiber-preservation criterion for autonomous descent;
- ordinary noninjectivity does not remove a representative section;
- one chart's control failure does not prove universal nonexistence;
- the conditional `4+6` transverse-curvature realization theorem;
- CLN labels do not select a unique physical realization;
- realization compatibility does not imply prediction in the presence of
  inequivalent countermodels.

## Frontier preserved

The roadmap does not close physical source rows. It explicitly retains:

- eta9 meridian/period and flat Deligne execution;
- selected visible-hidden Hull-Strominger endpoints;
- continuum q79 naturality and operator execution;
- upper action and automorphism transfer;
- the general Born source theorem;
- nonperturbative QFT/BV completion;
- the complete heterotic worldsheet contract;
- zero-primitive electroweak normalization;
- no-knob Standard Model precision equivalence.

## Publication delta

Version 12 is a major conceptual and theorem-status rewrite. It should be
uploaded as a new major Zenodo version with the generated PDF, canonical TeX,
Markdown conversion, and this revision audit.
