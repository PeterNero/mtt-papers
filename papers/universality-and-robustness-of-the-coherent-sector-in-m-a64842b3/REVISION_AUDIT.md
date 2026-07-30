# Revision Audit: Local Coherent-Sector Robustness Across Model Families

Date: 2026-07-30

Paper id:
`universality-and-robustness-of-the-coherent-sector-in-m-a64842b3`

Selected revision:
Version 2

Superseded release:
Version 1.0, DOI `10.5281/zenodo.18260834`

## Revision purpose

Version 1 correctly asked whether the low coherent sector can be stable
across microscopic model choices, but it promoted local spectral language
to a global universality, physical-equivalence, and landscape-reduction
claim. It did not define a common comparison space, block domains,
spectral region, perturbation topology, error accumulation rule, state and
observable maps, or physical interpretation maps.

Version 2 is a standalone cross-model comparison paper. It imports rather
than duplicates the single-model Feshbach theorem and constructs the
transported-resolvent layer that was actually missing.

## Current authority lock

Kernel model at task start:
`45a790830b6947d8c330bb95d643113cbe6c0faa22d23ec8d050400bc290b45c`

Repository starting head:
`0b23772c29929f09156828c375cd1a18612e2027`

Controlling authority:

- `A10`, recorded, SHA-256
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.
  It requires explicit block-operator and resolvent assumptions,
  norm-specific robustness, local rather than global universality, and
  separation of projector stability, dynamics, and physical equivalence.

## Canonical ownership lock

Established operator theory owns:

- Riesz projections and perturbation theory;
- Davis-Kahan subspace-angle estimates;
- norm-resolvent, Mosco, and varying-Hilbert-space convergence; and
- Duhamel finite-time estimates.

The companion coherent-sector paper, DOI
`10.5281/zenodo.21710429`, owns:

- the exact-spectral-projector correction;
- the domain-explicit block operator;
- the Feshbach inverse formula and self-energy product; and
- the single-model operator-norm robustness theorem.

Version 2 of this paper owns only:

1. the transported cross-model record;
2. the common-region compressed-resolvent comparison;
3. chainwise error accumulation;
4. the state-observable transfer requirement;
5. the seven-layer robustness hierarchy; and
6. counterexamples separating local robustness from landscape reduction
   and physical equivalence.

## Current version delta

Version 2:

1. removes the legacy series style and mojibake;
2. replaces the untyped universality class by a controlled model record;
3. imports the single-model reduction rather than restating it as new;
4. requires a common full and eliminated-sector resolvent region;
5. transports retained resolvents to one declared comparison space;
6. proves the local comparison and chainwise accumulation bounds;
7. supplies a full-space Riesz-projector specialization;
8. records quasi-unitary and Mosco routes for genuinely varying spaces;
9. separates seven robustness layers;
10. proves a state-observable expectation bound;
11. gives a continuum counterexample to automatic landscape reduction;
12. gives an observable counterexample to spectral physical equivalence;
13. withdraws generic full-quantum and BRST/Borel claims;
14. replaces landscape reduction by a six-row completion contract;
15. reconciles the current Calabi-Yau, heterotic, string, M-theory, and
    quantum-gravity papers at their selected tiers; and
16. adds claim-status, numerical-certificate, completion, and
    falsifiability sections.

## Claim-by-claim audit

### All selected models form one coherent universality class

Version 1 claim:
The standing assumptions place a broad family of geometries and physical
theories in one class.

Decision:
Withdraw as a global statement.

Reason:
The models require explicit Hilbert-space identifications, common
resolvent regions, domain topology, and physical maps. None was supplied.

Version 2 resolution:
Define only a local tolerance-dependent class around one reference record.

### Projector norm below one proves physical equivalence

Version 1 claim:
Close projectors make microscopic differences physically irrelevant.

Decision:
Replace.

Reason:
Projector distance proves range isomorphism under its hypotheses, not
operator, state, observable, dynamical, or physical equivalence.

Version 2 resolution:
Separate seven robustness layers and require a certificate for each layer
claimed.

### Finite curvature correction preserves FCC

Version 1 claim:
Finiteness of an undefined curvature correction preserves the coherent
sector.

Decision:
Withdraw.

Reason:
Finiteness does not give smallness relative to a spectral or
contractivity margin, and the operator topology was not specified.

Version 2 resolution:
Require the curvature dependence to enter a declared operator or form
family with a quantitative perturbation and common-resolvent bound.

### RG compatible with FCC preserves the class

Version 1 claim:
Compatible RG flow preserves the coherent class.

Decision:
Withdraw as circular.

Reason:
Compatibility was defined by the property the theorem purported to
derive.

Version 2 resolution:
Any RG application must define the flow, transported domains, norm or
form topology, time or scale interval, and accumulated error.

### Full quantum dynamics is robust

Version 1 claim:
Borel, BRST, physical-Hilbert, scattering, and full quantum robustness
were already established.

Decision:
Withdraw.

Reason:
The current selected QG revision supports exact finite TT data,
conditional classical reduction, and fixed-order parity, while
nonperturbative ultraviolet completion remains open.

Version 2 resolution:
Use the QG paper only at its current declared tier.

### Calabi-Yau, heterotic, string, and M-theory are proved sublimits

Version 1 claim:
All listed branches are controlled members of one class.

Decision:
Replace by a status table.

Reason:
The current revisions are conditional realization records with distinct
open endpoints. They do not yet share one completed comparison record.

Version 2 resolution:
State each branch at its selected tier and list the missing common rows.

### Robustness reduces the landscape

Version 1 claim:
Gap and admissibility conditions make the landscape small, structured,
and often discrete.

Decision:
Disprove as an automatic inference.

Reason:
A continuum of microscopically distinct diagonal operators can have the
same retained resolvent and uniform gap.

Version 2 resolution:
Give the explicit counterexample and require a candidate set,
counting/measure convention, executable filter, and selector.

## External literature verification

The revision was checked against:

- Kato, DOI `10.1007/978-3-642-66282-9`;
- Davis and Kahan, DOI `10.1137/0707001`;
- Kuwae and Shioya, DOI `10.4310/CAG.2003.v11.n4.a1`;
- Post, DOI `10.1007/978-3-642-23840-6`;
- Ashok and Douglas, DOI `10.1088/1126-6708/2004/01/060`; and
- Douglas and Kachru, DOI `10.1103/RevModPhys.79.733`.

## Expository review

The revision:

- begins with the three distinct questions hidden by "universality";
- explains why a common gap is insufficient;
- imports the single-model theorem before defining the new layer;
- gives the transport record in both words and symbols;
- proves the central comparison result directly;
- explains chainwise error accumulation;
- uses a seven-row table to separate robustness notions;
- gives three elementary counterexamples;
- reconciles every named MTT branch against its current revision; and
- ends with executable, status, completion, and falsifiability contracts.

## Frontier delta

Before:
The paper asserted global coherent universality, full quantum robustness,
physical equivalence, and landscape reduction from untyped local spectral
conditions.

After:
The paper proves a bounded transported-resolvent comparison theorem,
chainwise error accumulation, and observable transfer on a declared local
class. It also proves by counterexample that these results do not imply a
finite landscape, unique selection, arbitrary-time dynamics, or physical
equivalence.

## Release verification

- `pdflatex`, `bibtex`, and two final `pdflatex` passes completed without
  LaTeX, citation, reference, overfull-box, or underfull-box warnings.
- All 14 PDF pages were rendered with Poppler and visually inspected,
  including the transported-resolvent theorem, accumulated-error bound,
  robustness-layer table, counterexamples, application table, and
  references.
- The expository, theorem-ownership, interpretive-book, paper-release, and
  canonical repository gates all passed.
- Zenodo Version 2 was published as DOI
  `10.5281/zenodo.21710653` under concept DOI
  `10.5281/zenodo.18260833`.
- The Zenodo record contains one file, `main.pdf`, 16 explicit
  references, two related identifiers, a plain-text abstract, and a
  repository link.
- Immutable source hashes:
  - `main.tex`:
    `1db283114f7c49319421b69075c3069e4c782160fdfed5b0abf99ef7a1058fb4`
  - `main.bib`:
    `f4c96ebf2328a499b8221fc88b5839a441e5e9d638ddc5d6cf31cc43f58872bf`
  - `main.pdf`:
    `127c0f141286f0a265083c0269ec6d1e48612d1c60fb7f907e2bb9bf7c7cdf61`
  - canonical source tree:
    `217bfdd16df05a6986e41a6d194f652e87c360784d3ccd4708f7157164f60612`
