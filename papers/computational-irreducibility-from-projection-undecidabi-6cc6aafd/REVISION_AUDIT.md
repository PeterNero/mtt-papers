# Revision Audit: Selection Reachability in Projection-Based Dynamics

## Scope

This audit governs Version 2 of:

`computational-irreducibility-from-projection-undecidabi-6cc6aafd`

Supersedes:

- Version 1, DOI `10.5281/zenodo.18255391`.

Controlling current authority:

- A10, consolidated paper reconciliation, source hash
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.

Imported current MTT releases:

- Foundations v9, DOI `10.5281/zenodo.21655367`;
- Projection--Admissibility v2, DOI `10.5281/zenodo.21652659`;
- Program A2 v2, DOI `10.5281/zenodo.21652637`;
- Measurement v6, DOI `10.5281/zenodo.21665982`; and
- Conditional Classification v3, DOI `10.5281/zenodo.21710806`.

No numerical result packet is promoted by this paper.

## Version 1 claim audit

### Projection forces universal computation

Version 1 claim:
Noninjective projection, stable basins, record formation, locality, and finite
predictivity force a physical dynamics to support universal computation.

Decision:
Withdraw.

Reason:
These properties do not construct a universal transition rule, counter
registers, a zero test, or unbounded memory. A finite counterexample has all
the listed projection and stability features but decidable reachability.

Version 2 resolution:
Prove the explicit decidable counterexample and state that projection may
erase, preserve, or transfer computation depending on a typed fidelity
contract.

### The simulator was constructed from basin language

Version 1 claim:
A proof block constructed a universal two-counter-machine simulator from
control basins, countably many record sites, knee transitions, and a fixed
protocol alphabet.

Decision:
Withdraw the construction.

Reason:
The proof assumed every missing object: the countable physical carrier,
exact increment and decrement, exact zero testing, step fidelity, target
fidelity, uniformity, robust decoding, and admissibility for arbitrary run
length. Basin terminology does not establish those objects.

Version 2 resolution:
Import the exact conditional theorem and six-row embedding contract from
Program A2 without duplicating its theorem. State the present MTT status as
conditional because no selected physical realization supplies all rows.

### Finite horizons do not restore decidability

Version 1 claim:
An instance-dependent finite admissible horizon remains undecidable because
the event predicate is robust over a neighborhood.

Decision:
Withdraw as a generic statement.

Reason:
A known computable horizon and effectively decidable robust predicates yield a
finite search. Merely naming a semantic horizon or quantifying over a
continuum does not provide such a decision procedure, but its absence is not a
proof of undecidability.

Version 2 resolution:
Prove a positive-margin enclosure-packet theorem for finite-horizon robust
events. Boundary contact or a missing enclosure is classified as unresolved,
not automatically undecidable.

### Finite margins support unbounded robust counters

Version 1 claim:
Finite stability margins and countably many persistent record sites suffice
for arbitrarily long robust counter-machine execution.

Decision:
Withdraw.

Reason:
No selected carrier or capacity theorem was supplied. On a compact metric
carrier, infinitely many distinct decoded configurations cannot have one
uniform positive decoding radius.

Version 2 resolution:
Prove the compact uniform-margin obstruction. An unbounded encoding must use
shrinking margins, a non-totally-bounded carrier, a growing family, or another
explicitly verified mechanism. The paper notes that compact smooth universal
simulations in the literature do not contradict this narrower packing result.

### Undecidable reachability means no effective law exists

Version 1 claim:
Undecidable event reachability implies the absence of a globally effective
dynamical law and establishes computational irreducibility of physical
trajectories.

Decision:
Withdraw.

Reason:
A fixed computable transition map can generate every finite trajectory prefix
while unbounded target reachability remains undecidable. Undecidability of one
language is not a complexity lower bound or a theorem about every trajectory.

Version 2 resolution:
Prove finite-prefix computability with undecidable unbounded reachability and
state the additional task, size, machine, and shortcut definitions required
for a future computational-irreducibility theorem.

### Gravity sets the coherence budget for undecidability

Version 1 claim:
Gravity determines the coherence budget and therefore the resource bound for
universal selection computation.

Decision:
Withdraw.

Reason:
No selected gravity-to-capacity map or universal-machine embedding was
provided. A model-specific geometric margin may bound a finite experiment, but
that does not establish arbitrary machine prefixes.

Version 2 resolution:
No gravity claim is made.

## Theorem ownership

Version 2 owns:

- the finite noninjective-projection counterexample;
- the effective reachability-descent definition and transfer theorem;
- the positive-margin finite-horizon enclosure theorem;
- the compact uniform-margin obstruction and its encoding corollary; and
- the finite-prefix-computability versus unbounded-reachability proposition.

It imports without re-proving:

- the computable admissible presentation and selection language from Program
  A2;
- the six-row robust uniform two-counter-machine embedding contract;
- the conditional many-one reduction from machine halting to MTT selection
  reachability;
- the finite-capacity reachability result from Program A2;
- the Projection--Admissibility distinction between descent and recovery; and
- the current measurement-process decomposition.

The Turing and Minsky undecidability results and the compactness/total
boundedness fact are standard mathematics and are not claimed as novel.

## External literature verification

The revision was checked against primary publication records for:

- Turing's computability theorem, DOI
  `10.1112/plms/s2-42.1.230`;
- Minsky's two-counter-machine reference, *Computation: Finite and Infinite
  Machines*, Prentice-Hall, 1967;
- Moore's dynamical undecidability papers, DOI
  `10.1103/PhysRevLett.64.2354` and
  `10.1088/0951-7715/4/2/002`;
- Branicky's hybrid/continuous universal computation, DOI
  `10.1016/0304-3975(94)00147-B`;
- Henzinger--Kopke--Puri--Varaiya's hybrid reachability boundary, DOI
  `10.1145/225058.225162`;
- robust analytic simulation, DOI `10.1007/11494645_21`;
- robust polynomial-ODE simulation, DOI
  `10.1016/j.aam.2007.02.003`; and
- low-dimensional and compact-sphere simulation, DOI
  `10.3233/COM-210381`.

## Expository review

The revision:

- begins by separating five different computability claims;
- gives a concrete two-bit counterexample before abstract theorems;
- explains why a projection needs a semiconjugacy and predicate-fidelity
  contract;
- states finite-horizon robust verification as a checkable certificate;
- presents the six imported A2 rows in a table;
- proves the compactness obstruction and explains its exact limitation;
- compares the result with primary hybrid and analog-computation literature;
- states current MTT support and missing source objects explicitly; and
- ends with a machine-readable certificate schema and falsifiability list.

## Frontier delta

Before:
Version 1 asserted that viable projection-based physical theories necessarily
have undecidable observable dynamics and computationally irreducible
trajectories.

After:
Version 2 proves only that undecidability can transfer through an effective
projection contract and imports the Program A2 conditional reduction. It
proves finite and compact-capacity boundaries and leaves physical MTT
undecidability open until a selected robust unbounded embedding is supplied.

## Release verification

Version 2 was published on Zenodo as:

- version DOI `10.5281/zenodo.21710992`;
- concept DOI `10.5281/zenodo.18255388`; and
- record `https://zenodo.org/records/21710992`.

The published record was verified to contain exactly one file, `main.pdf`,
with 14 explicit references, two related identifiers, a plain-text
description, and version label `v2`.

Immutable reviewed artifacts:

- `main.tex` SHA-256:
  `9896f29fee9668a4320c3274fb0c35e3ca6bd7c3d11d9710e7be84144940454a`;
- `main.pdf` SHA-256:
  `7d74461ec42884ca4cff0bb929100e34667d6d315cc26349bdf09d483631ac17`;
- `paper.md` SHA-256:
  `f70edb422d8978badfb7006639d5d61e66a5fa17331c53a19ceb5c09152d96d9`;
  and
- source-tree SHA-256:
  `2ee50240ec59b61639bd6b997f32f68bebc382ebf44017d9f1737224865ff388`.

The PDF was built with `pdflatex`, `bibtex`, and two final `pdflatex`
passes. All 11 pages were rendered with Poppler and visually inspected.
The canonical repository verifier, theorem-ownership verifier, interpretive
book-role verifier, strict expository audit, and paper-release verifier all
passed before publication.
