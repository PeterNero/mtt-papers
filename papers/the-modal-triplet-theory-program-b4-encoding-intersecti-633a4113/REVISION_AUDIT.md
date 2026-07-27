# Program B4 revision audit

## Selected revision

- Paper: `The Modal Triplet Theory Program B4`
- Superseded source: version 1.0
- Superseded source SHA-256: `498fbc58d177335a41210378439ffe333eca0ae3191cba6298ffd9decfdbd16c`
- Selected successor: version 2
- Controlling correction authority: `A10`
- A10 SHA-256: `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`

## Context audit

Version 1 was checked against the selected Program A0 and B0-B3 revisions,
standard intersection and deformation mathematics, standard anomaly theory,
and the current exact A46, A47, and A50 finite Standard Model packets. The old
paper correctly recognized that several constraints can narrow a realization
space and that the Standard Model is an important anomaly-free example. Its
rigidity theorem, however, did not define the candidate category, topology,
deformation class, independent constraint maps, or quotient by equivalence.

## Current exact result inputs

The revision uses the following current result objects only at their declared
scope:

- `typed_family_representation` (A46), SHA-256
  `528af6955b3b7207a9db178d14d95cb4078f895f946a7d204fa680bc5754f657`:
  exact 48-state family-diagonal chiral carrier and anomaly table.
- `native_gauge_group` (A47), SHA-256
  `eeb8c7bb501d151a53ba2df109654e34ea4735560338c86e978107c9b5678582`:
  exact native gauge action and faithful diagonal `Z6` kernel on the A46
  carrier.
- `neutral_summand_hypercharge` (A50), SHA-256
  `89a1bb179af408da9d1d8408a9063331d21c8e429bb7a9bb52976bbf857e172c`:
  exact one-dimensional anomaly-free phase nullspace in the selected completed
  finite algebra.

These packets prove a selected compatible branch and internal conditional
uniqueness statements. They do not classify every representation, topology,
finite algebra, or ultraviolet completion.

## Required corrections

### 1. Rigidity requires a typed space and deformation theory

**Prior claim:** Simultaneous circle/gravity, lens/gauge, and
nil/quantization constraints generically make their intersection rigid.

**Finding:** A set has no notion of isolation without a topology. Constraint
labels need not be independent, and equivalence or gauge-orbit directions must
be removed before a Jacobian can test rigidity.

**Resolution:** Version 2 defines an encoding-intersection datum with a
category, equivalence relation, topology or deformation functor, constraint
maps, regularity, and boundary conditions. Compatibility, local rigidity,
infinitesimal rigidity, persistence, and global uniqueness are defined
separately.

**Status:** Resolved.

### 2. A real rigidity criterion must replace dimension slogans

**Prior claim:** Several distinct compatibility requirements generically leave
an isolated intersection.

**Finding:** Repeated or dependent constraints can leave a continuum. Even
independent constraints can leave positive-dimensional moduli. Conversely,
singular equations can have isolated solutions without a full-rank derivative.

**Resolution:** Version 2 proves that an injective combined derivative on an
`n`-dimensional quotient moduli chart is sufficient for local isolation. It
also proves the standard transverse-intersection dimension formula and gives
both continuous-intersection and multiple-isolated-solution counterexamples.

**Status:** Resolved.

### 3. Consistency of one intersection is not uniqueness

**Prior claim:** The Standard Model's simultaneous compatibility explains its
exceptional rigidity and why only a narrow set of alternatives can exist.

**Finding:** Exhibiting one compatible point proves only nonemptiness.
Multiple isolated points can all be locally rigid. Global uniqueness requires
an exhaustive candidate category and proof that every alternative has been
classified and excluded or identified.

**Resolution:** Version 2 gives an exhaustive-selection certificate with
explicit candidate, equivalence, topology, anomaly, action, and quantum
requirements. The Standard Model theorem is narrowed to a selected
representation/anomaly compatibility result.

**Status:** Resolved.

### 4. Anomalies were defined too broadly

**Prior claim:** Any overlap or refinement failure in a combined encoding is
an anomaly, and anomaly cancellation is equivalent to admissibility.

**Finding:** Failure of a classical transition cocycle means that a bundle or
descent datum has not been constructed. A quantum anomaly is an obstruction to
the quantum Ward/BRST identity or a global determinant-line/phase obstruction.
These notions have different domains and tests.

**Resolution:** Version 2 separates classical overlap compatibility, local
quantum anomalies, and global anomalies. Anomaly cancellation is stated as
necessary for the declared chiral quantum gauge contract but not sufficient
for existence, locality, unitarity, ultraviolet completion, or uniqueness.

**Status:** Resolved.

### 5. Anomaly cancellation does not select all Standard Model data

**Prior claim:** Anomaly cancellation sharply constrains representations and
helps explain the Standard Model's isolated structure.

**Finding:** The abelian anomaly equations are homogeneous and cannot fix a
nonzero normalization. Vector-like pairs preserve all local perturbative
anomaly coefficients. Neutral singlets can leave the elementary anomaly table
unchanged. Additional global, algebraic, action, and source data are required.

**Resolution:** Version 2 proves the homogeneous hypercharge-scaling no-go and
the vector-like extension counterexample. It explains why A50's uniqueness is
stronger but conditional: the finite algebra, phase coordinates,
representation, and primitive lattice have already been fixed.

**Status:** Resolved.

## Additional mathematical corrections

- The intersection is formed from typed geometric, redundancy, quantum,
  anomaly, and overlap contracts rather than from three obstruction names.
- Orbit or automorphism directions must be quotiented or sliced before testing
  infinitesimal rigidity.
- Full-rank Jacobian is a sufficient local criterion, not a necessary one.
- Persistence under perturbation is separate from isolation.
- The word `generic` requires a topology and perturbation ensemble.
- Discrete representation labels can all be locally isolated while several
  inequivalent labels survive.
- The Standard Model anomaly sums are reproduced using one-family left-handed
  rows including `N^c`, and the three-family Witten count is twelve.
- The faithful global group is distinguished from its Lie algebra.
- Compatibility with a supplied curved spin background is not a derivation or
  quantization of gravity.
- A representation and anomaly packet does not replace the quantum field,
  renormalization, state, and observable constructions.

## Retained theorem content

The revision retains the useful core of Program B4:

1. intersecting independent constraints can narrow a realization space;
2. overlap and anomaly consistency are genuine obligations;
3. the Standard Model chiral representation is anomaly-free;
4. later selected MTT packets establish a nontrivial exact compatible finite
   branch; and
5. local rigidity, when proved, is valuable even without global uniqueness.

## Resulting scope

Program B4 v2 is a typed encoding-intersection and conditional rigidity paper.
It proves local rigidity under an explicit rank condition, gives the transverse
dimension theorem and countermodels, distinguishes anomaly notions, and
integrates the exact A46-A50 Standard Model representation results. It proves
one selected compatibility branch. It does not prove that the Standard Model
is the unique or inevitable intersection among all physical theories.
