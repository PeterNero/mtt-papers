# Program B5 v4 Release Audit

## v4 reproducibility delta

Version 4 preserves the complete Version 3 scientific revision. It replaces
the stale managed statement `no result rows mapped` by the exact result object
already used in the paper:

- `q79_exact_theorem` (A11), at the `DERIVED_EXACT` selected finite-branch
  tier.

Both canonical sources point to curated-results commit
`31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The in-paper release note now
contains only the Version 4 delta; this audit retains the earlier history.
This is a provenance and presentation correction, not a critical-dimension,
worldsheet-completion, or physical-selection theorem.

## v3 publication delta

- **Supersedes:** v2.
- **Reason:** the relative saturation theorem needed an intuitive
  wiring-diagram explanation and a clearer selection boundary.
- **Resolution:** add a guided dependency map without changing the
  derivative-incidence theorem or countermodels.
- **Retained:** all v2 mathematical conclusions.
- **Remaining:** exhaustive realization, physical string background,
  worldsheet completion, and selection.

## Selected revision

- Paper: `The Modal Triplet Theory Program B5`
- Superseded source: version 1.0
- Superseded source SHA-256:
  `08f278d8d7c681eb7e7bf0dd9e5679fd9b731727033c28111f994cae940dfb95`
- Selected successor: version 4
- Controlling correction authority: `A10`
- A10 SHA-256:
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`
- Current finite q=79 boundary authority: `A11`
- A11 SHA-256:
  `ccacd5227f91ab08fa3cb961c395d8abc07ff861a1fcbbd583095f6809bdcecc`

## Context audit

Version 1 was checked against the selected Program A0 and B0-B4 revisions,
the current string/flux encoding status, the exact finite q=79 authority, and
the live `B.HS.01`, `B.QG.01`, and `B.QG.02` blockers. The old paper correctly
recognized that constraints supplied by one common source can become strongly
coupled and that string theory is an important example of a framework combining
extended carriers, anomaly conditions, gravity-sensitive structure, and
dualities.

Its central implication chain was not established. Saturation was defined as
inseparability and then used to assert the failure of pointlike descriptions,
the necessity of one-dimensional carriers, discrete critical dimensions,
internal cancellation of every anomaly, and forced dualities. The category,
factorization class, carrier topology, anomaly groups, dimension equations,
duality maps, and physical selector needed for those claims were absent.

## Current result input

The revision cites one current calculation object:

- `q79_exact_theorem` (A11), SHA-256
  `ccacd5227f91ab08fa3cb961c395d8abc07ff861a1fcbbd583095f6809bdcecc`:
  on the selected exact finite branch,
  `q = 15 mod 64`, `q = 2 mod 7`, and therefore `q = 79 mod 448`.

The revision uses this packet only to mark the current finite arithmetic
boundary. It explicitly states that `79` is not a spacetime dimension,
worldsheet central charge, or critical-dimension theorem.

## Required corrections

### 1. Saturation was absolute and circular

**Prior claim:** A saturated encoding implements circle, lens, and nil
responses inseparably, so no decomposition into independent layers exists.

**Finding:** The conclusion was included in the definition. No category,
equivalence relation, constraint inventory, block structure, or class of
allowed factorizations was specified.

**Resolution:** Version 2 defines a saturation contract containing all of
those data. A realization is saturated only relative to the displayed
contract. A theorem proves that changing the contract can change the
saturation predicate.

**Status:** Resolved.

### 2. A real indecomposability test was missing

**Prior claim:** Simultaneous obstruction responses amplify one another and
make the encoding exceptionally rigid.

**Finding:** No test distinguished genuine coupling from relabeled independent
constraints.

**Resolution:** Version 2 introduces the bipartite derivative-incidence graph.
It proves that graph disconnection is equivalent to a first-order block
factorization relative to the declared blocks. Connected incidence proves
first-order indecomposability. Combined with an injective derivative, it proves
local isolation as well.

**Status:** Resolved.

### 3. Saturation does not exclude pointlike models

**Prior claim:** Pointlike carriers cannot simultaneously maintain kinematic,
gauge, and discrete consistency.

**Finding:** Pointwise fields can be globally coupled by derivatives,
connections, and boundary conditions. A finite constraint system can also be
complete, rigid, and indecomposable without any base-space carrier.

**Resolution:** Version 2 gives the exact matrix countermodel

```text
[[1,1,0],
 [0,1,1],
 [1,0,1]]
```

whose determinant is `2` and whose incidence graph is connected. Its unique
solution is rigid and first-order indecomposable, yet the model has no extended
carrier.

**Status:** Resolved by counterexample and claim withdrawal.

### 4. One-dimensional carriers require an extra hypothesis

**Prior claim:** One-dimensional carriers are the minimal objects capable of
supporting saturation.

**Finding:** Saturation itself has no carrier-dimension predicate. A
one-dimensional interval also has no nontrivial loop.

**Resolution:** Version 2 proves the correct conditional theorem: a compact
metric carrier supporting a nonconstant continuous loop has covering dimension
at least one, and `S1` makes the bound sharp. The paper states explicitly that
this does not supply gauge, nil, action, worldsheet, or anomaly data.

**Status:** Resolved.

### 5. Worldsheet language was promoted too early

**Prior claim:** Continued one-dimensional carriers naturally generate
worldsheets.

**Finding:** A two-parameter sweep is not yet a physical worldsheet theory.

**Resolution:** Version 2 derives only the parameter domain `K x I` from a
family of carriers. It lists the additional target, action, boundary, gauge,
quantum, anomaly, and observable rows required for a physical worldsheet.

**Status:** Resolved.

### 6. Critical dimensions were asserted without an equation

**Prior claim:** Saturation and anomaly cancellation force a discrete set of
ambient dimensions.

**Finding:** No anomaly polynomial, central-charge defect, field content, or
regularization was supplied. Integer-valued dimension is already discrete and
does not constitute a critical-dimension derivation.

**Resolution:** Version 2 proves a conditional analytic theorem. If the
fully specified net defect `a(d)` is real analytic and not identically zero,
its zeros are isolated and finite on compact subintervals. Counterexamples
`a = 0`, `a = (d-10)(d-26)`, and `a = sin(pi d)` show why the function must be
provided.

**Status:** Resolved.

### 7. "Anomaly saturation" lacked a typed inventory

**Prior claim:** Saturated encodings internally cancel gauge, gravitational,
mixed, and higher anomalies in the strongest possible sense.

**Finding:** Different anomalies live in different cohomological,
determinant-line, cobordism, BRST, or Ward-identity settings. The allowed
counterterms, inflow, Green-Schwarz mechanisms, and added sectors also change
the test.

**Resolution:** Version 2 defines an anomaly contract with field content,
quantum domain, anomaly classes, target obstruction groups, and allowed
trivialization mechanisms. "Anomaly complete" now means that every row in that
declared inventory is explicitly trivialized.

**Status:** Resolved.

### 8. Duality was inferred rather than constructed

**Prior claim:** Saturation forces descriptions with redistributed
responsibilities to be identified by duality.

**Finding:** Similar purpose does not construct an invertible map, preserve an
action, or match observables. Quotienting by a duality presupposes that the
duality has already been proved.

**Resolution:** Version 2 defines a duality certificate with source and target,
maps and inverses, dynamics, boundaries, observables, and anomaly data. It
proves by counterexample that a saturated contract can have no nontrivial
duality.

**Status:** Resolved.

### 9. String-like realization was conflated with inevitability

**Prior claim:** String-like structures arise as the minimal realization of
maximal simultaneous obstruction resolution.

**Finding:** The implication requires the carrier, worldsheet, action,
quantization, anomaly, overlap, duality, and contract maps to be supplied.

**Resolution:** Version 2 gives a string-like realization package and a
conditional certificate: if every typed row maps into the saturation contract,
all constraints vanish, and the image passes the indecomposability test, the
package is a saturated realization. The converse is explicitly rejected.

**Status:** Resolved.

### 10. Existence was not physical selection

**Prior claim:** Saturated encodings explain why string-like frameworks arise
naturally in unification attempts.

**Finding:** Existence or rigidity does not select one realization from several
inequivalent survivors.

**Resolution:** Version 2 separates existence, local rigidity,
class-relative uniqueness, physical selection, and empirical adequacy. A
proposition proves that two equally complete saturated points remain
underdetermined without an additional source law or selector.

**Status:** Resolved.

### 11. The live q=79 string frontier had to be preserved

**Prior risk:** The structural paper could be read as closing a physical
string or quantum-gravity branch.

**Finding:** `A11` closes a finite arithmetic branch only. The selected
visible-hidden HYM endpoints remain open (`B.HS.01`), the worldsheet contract
is currently `5/12` (`B.QG.01`), and the all-scale completion remains open
(`B.QG.02`).

**Resolution:** Version 2 states all three boundaries in the abstract, body,
theorem ledger, and conclusion. No open blocker is promoted.

**Status:** Resolved.

## Additional mathematical corrections

- Contract saturation is distinguished from ideal, lattice, and sheaf
  saturation.
- Constraint completeness refers to a displayed inventory, not unknowable
  "all constraints."
- First-order indecomposability is distinguished from nonlinear and global
  indecomposability.
- Connected incidence is relative to declared primitive blocks.
- Injective derivative is sufficient, not necessary, for local isolation.
- A worldsheet-like sweep is distinguished from a worldsheet quantum theory.
- Anomaly classes are distinguished from classical bundle-cocycle failure.
- A quotient records an established equivalence; it does not generate one.
- Higher-dimensional carriers are not ranked as physically inferior.
- Local rigidity does not compare disconnected solution components.
- q=79 arithmetic is not dimension counting.

## Retained theorem content

The revision preserves the useful core of Program B5:

1. one common source can couple otherwise distinct constraint blocks;
2. such coupling can produce genuine indecomposability and local rigidity;
3. extended-carrier, worldsheet, anomaly, and duality structures are valuable
   realization mechanisms;
4. string theory is an important test class for a rich saturation contract;
   and
5. mathematical consistency must remain separate from physical necessity.

## Resulting scope

Program B5 v2 is a rigorous relative-saturation and realization paper. It
proves an exact finite-dimensional first-order indecomposability criterion,
combines it with the B4 local-rigidity criterion, proves a conditional
loop-carrier lower bound and analytic criticality theorem, and supplies
countermodels to the former unconditional claims. It gives reusable anomaly,
duality, string-package, selection, and publication audit contracts. It does
not derive string theory, a numerical critical dimension, a duality web, a
complete q=79 worldsheet, or physical selection of one saturated universe.

## Expository revision, 2026-07-28

The theorem inventory and ownership are unchanged. A new paper-specific
reading guide explains saturation through the derivative-incidence graph as a
wiring diagram and separates contract completeness, indecomposability,
extended-carrier requirements, string-like realization, and physical
selection. Separate reading routes now guide mathematically focused and
interpretively focused readers through the argument.

The finite matrix example now explains why graph connectivity and determinant
nonvanishing test different properties. The string-like realization section
also states in plain language how established string packages can be tested
against an MTT contract without treating saturation as a substitute for their
actions, quantum measures, anomaly calculations, or duality maps. No new
necessity claim was added.
