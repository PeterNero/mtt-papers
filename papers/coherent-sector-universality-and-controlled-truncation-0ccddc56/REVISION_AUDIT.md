# Revision Audit: Coherent-Sector Reduction in MTT

Date: 2026-07-30

Paper id:
`coherent-sector-universality-and-controlled-truncation-0ccddc56`

Selected revision:
Version 2

Superseded release:
Version 1.0, DOI `10.5281/zenodo.18261354`

## Revision purpose

Version 1 contained the right methods-level target but did not define the
operator problem tightly enough for its central theorem. It left block
domains and the spectral parameter implicit, used an inverse at zero
without proving zero was in the eliminated-block resolvent, replaced the
actual Feshbach product by a schematic perturbation-squared-over-gap
expression, and promoted local spectral stability to broad universality
and emergent time.

Version 2 is a standalone operator-reduction paper. It distinguishes an
exact spectral projector from a reference-selected projector and makes
every domain, resolvent, norm, perturbation, and interpretation boundary
explicit.

## Current authority lock

Kernel model at task start:
`d7ec6749eeba3d8acfe5f2ced480120c60dede3c07ab0bffec2a4a9c64e6bbee`

Repository starting head:
`6dc3ea8e431544ccb255505fd363997e29cc52f1`

Controlling authority:

- `A10`, recorded, SHA-256
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.
  The master corrigendum requires explicit block domains and spectral
  parameters; the actual
  `||PTQ|| ||(QTQ-z)^-1|| ||QTP||` product; a precise analytic meaning
  instead of generic "bounded geometry"; universality only in a class
  preserving the declared gap, rank, projector, and domain rows; and a
  model-specific theorem before internal modular flow is called physical
  time.

## Canonical ownership lock

Classical operator theory owns:

- spectral functional calculus and Riesz projectors;
- the Feshbach--Schur map and inverse formula;
- bounded perturbation and resolvent identities;
- Davis--Kahan subspace-angle theory;
- Stone's theorem and Duhamel's formula; and
- Schrieffer--Wolff and adiabatic refinements under their hypotheses.

The MTT Foundation owns the general admissibility ledger and status
semantics:

- `papers/modal-triplet-theory-foundations/main.tex`
- DOI `10.5281/zenodo.21655367`

The normalized-capacity paper owns signed row normalization, provenance,
and bottleneck conventions:

- `papers/coherence-capacity-as-the-invariant-admissibility-margi-423433d4/main.tex`
- DOI `10.5281/zenodo.21709472`

Version 2 of this paper owns only:

1. the exact-spectral-projector correction for coherent reduction;
2. the domain-explicit bounded-coupling specialization;
3. the actual self-energy product and its declared-region interpretation;
4. the explicit block-variation robustness estimate;
5. the reduced-resolvent local comparison metric;
6. the resolvent-versus-long-time-dynamics boundary; and
7. the controlled coherent-sector certificate and completion contract.

## Current version delta

Version 2:

1. removes the legacy series style and mojibake;
2. distinguishes reference operator `G`, selected projector `P`, and full
   operator `T`;
3. proves that an exact spectral projector of `T` makes the off-diagonal
   blocks vanish;
4. states self-adjoint diagonal domains and bounded off-diagonal maps;
5. introduces the declared spectral parameter and resolvent region;
6. proves the exact Feshbach inverse formula;
7. replaces the schematic error by the exact product;
8. gives a transparent two-mode example;
9. derives Riesz-projector stability from a contour and Neumann margin;
10. removes generic "bounded geometry" language;
11. derives an all-block local operator-norm robustness estimate;
12. defines a bounded reduced-resolvent comparison functional and treats
    approximate universality as tolerance- and metric-dependent;
13. proves a finite-time Duhamel bound and gives a long-time
    counterexample;
14. separates internal unitary parameter from physical time;
15. gives a finite/numerical execution checklist; and
16. adds claim-status, falsifiability, and completion tables.

## Claim-by-claim audit

### The exact spectral projector has an omitted-sector correction

Version 1 claim:
`P` is the spectral projector of `T`, while `PTQ` and `QTP` generate a
nonzero correction.

Decision:
Correct.

Reason:
An exact spectral projector reduces its self-adjoint operator, so both
off-diagonal blocks vanish.

Version 2 resolution:
Prove the reducing-projector proposition. Nontrivial reduction uses a
projector selected from a reference operator, symmetry, Galerkin space, or
approximate criterion.

### The correction is `||delta T||^2/Delta`

Version 1 claim:
The truncation error universally has that schematic form.

Decision:
Replace.

Reason:
The exact object is energy dependent and contains separately typed
coupling and resolvent factors.

Version 2 resolution:
Use
`B(D-z)^-1 C` and its exact norm product. The squared form is a corollary
only when `C=B*` and one bounded perturbation controls both couplings.

### Zero can be used as the spectral parameter

Version 1 claim:
`(QTQ)^-1` exists because a low/high gap exists.

Decision:
Withdraw without an extra location assumption.

Reason:
A gap between clusters does not imply that zero lies outside the high
block spectrum.

Version 2 resolution:
Declare `z` and require `z in rho(D)`, or certify a common region
`Omega` at positive distance from `spec(D)`.

### Bounded commutators are bounded geometry

Version 1 claim:
Generic commutator and structure-constant bounds define bounded geometry.

Decision:
Withdraw terminology.

Reason:
Geometric boundedness and operator commutator conditions are distinct
analytic notions.

Version 2 resolution:
List self-adjointness, domains, bounded couplings, resolvent margins,
contours, and perturbation norms directly.

### Small perturbations preserve everything

Version 1 claim:
Small perturbations preserve the gap, projector, and effective dynamics.

Decision:
Replace by norm-specific theorems.

Reason:
"Small" depends on topology. Operator-norm, graph-norm, form, strong
resolvent, and semigroup stability are not interchangeable.

Version 2 resolution:
Prove bounded operator-norm projector and block-map bounds. State all
other topologies as separate obligations.

### The Riesz contour formula has no orientation-dependent sign

Version 1 claim:
The spectral projector can be written with `(G-z)^-1` and a positive
counterclockwise contour factor.

Decision:
Correct the sign and declare the orientation.

Reason:
For a positively oriented contour,
`(2 pi i)^-1 integral (z-G)^-1 dz` is the projector. With the paper's
`(G-z)^-1` convention, the formula requires a leading minus sign.

Version 2 resolution:
Declare the contour positively oriented and use
`-(2 pi i)^-1 integral (G-z)^-1 dz` for both projectors.

### Coherent-sector agreement defines global universality

Version 1 claim:
Different internal geometries with close reduced generators form a
universal physical class.

Decision:
Narrow.

Reason:
A unitary identification, spectral region, norm, tolerance, observables,
and accumulation rule are needed. Reduced closeness is not microscopic or
physical equivalence.

Version 2 resolution:
Define a reduced-resolvent comparison functional from the bounded inverses
`F_T(z)^-1`, on a region contained in both the full and eliminated-block
resolvent sets. No metric axioms are asserted without closure conditions
on the allowed unitary identifications. Use only local
epsilon-neighborhood language.

### The modular generator is physical time

Version 1 claim:
Robust coherent-sector dynamics establishes structural stability of
emergent time.

Decision:
Withdraw.

Reason:
Stone's theorem supplies a mathematical group parameter. Physical time
requires a state, clock protocol, Hamiltonian, decoder, and controlled
intertwining relation.

Version 2 resolution:
Publish that physical-time record as an explicit open application
contract.

## External literature verification

The revision was checked against primary or authoritative sources for:

- the original projection formalism:
  Feshbach, DOI `10.1016/0003-4916(62)90221-X`;
- the smooth Feshbach--Schur map:
  Griesemer and Hasler, DOI `10.1016/j.jfa.2008.01.015`;
- closed operators, resolvents, Riesz projectors, and perturbations:
  Kato, DOI `10.1007/978-3-642-66282-9`;
- spectral-subspace rotation:
  Davis and Kahan, DOI `10.1137/0707001`;
- functional analysis and Stone's theorem:
  Reed and Simon, ISBN `978-0-12-585050-6`; and
- gap-improved effective Hamiltonians:
  Bravyi, DiVincenzo, and Loss,
  DOI `10.1016/j.aop.2011.06.004`.

## Expository review

The revision:

- starts from the corrected six-object question;
- explains the exact-projector issue before introducing formulas;
- gives one complete two-mode example;
- proves each central estimate with its domain and norm visible;
- separates imported operator theory from the paper's integration work;
- compares six distinct meanings of universality;
- explains why long times require a separate theorem;
- provides a physical-time checklist;
- gives a finite numerical certificate format; and
- closes with claim-status and falsifiability tables.

## Frontier delta

Before:
The paper contained a useful intuition but an ill-typed central theorem
and broad universality/time interpretations.

After:
The paper supplies an exact, domain-explicit, norm-specific
Feshbach/projector certificate, a new correction exposing when the
off-diagonal blocks must vanish, and strict boundaries between spectral
reduction, local robustness, long-time dynamics, continuum transfer, and
physical time.

## Release verification

- `pdflatex`, `bibtex`, and two final `pdflatex` passes completed without
  LaTeX, citation, reference, overfull-box, or underfull-box warnings.
- All 14 PDF pages were rendered with Poppler and visually inspected,
  including the block-domain theorem, corrected Riesz contour formula,
  reduced-resolvent comparison functional, status table, and references.
- The expository, theorem-ownership, interpretive-book, paper-release, and
  canonical repository gates all passed.
- Zenodo Version 2 was published as DOI
  `10.5281/zenodo.21710429` under concept DOI
  `10.5281/zenodo.18261353`.
- The Zenodo record contains one file, `main.pdf`, eight explicit
  references, two related identifiers, a plain-text abstract, and a
  repository link.
- Immutable source hashes:
  - `main.tex`:
    `a64dbb79461e71fbafa2b1f902a357f07595615f3d78f52c48292b8af40aa048`
  - `main.bib`:
    `f822bfa74fdbfd80020a2c1a410accc48d2a771bb36436ab2d3096fb08ceea54`
  - `main.pdf`:
    `05283cb1cabeb634624eb2fdcc8098cc70715b35dc49b373d2e107792ef53a45`
  - canonical source tree:
    `0827309394230fab4c0fc78e2c77d61bb9c26b754b0cfbcf2fd265ad609fa843`
