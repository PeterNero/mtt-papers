# Revision Audit: Wilsonian Coarse-Graining and Projection-Admissible Description

## Scope

This audit governs Version 2 of:

`effective-field-theory-as-a-shadow-of-projection-admiss-ec123406`

Supersedes:

- Version 1, DOI `10.5281/zenodo.18262361`.

Controlling authority:

- A10, consolidated paper reconciliation, source hash
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.

Imported current MTT releases:

- Foundations v9, DOI `10.5281/zenodo.21655367`;
- Projection--Admissibility v2, DOI `10.5281/zenodo.21652659`;
- Coherent-Sector Reduction v2, DOI `10.5281/zenodo.21710429`; and
- Conditional Classification v3, DOI `10.5281/zenodo.21710806`.

No numerical result packet is promoted by this paper.

## Version 1 claim audit

### Noninjectivity rules out a right inverse

Decision: withdraw.

Reason: a noninjective surjection can have a right section. Noninjectivity
rules out a left inverse that decodes the actual input.

Version 2 resolution: import the current Projection--Admissibility inverse
taxonomy and demonstrate it in an exact Gaussian mode-elimination example.

### RG flow is generically irreversible

Decision: split into two typed claims.

Reason: exact coarse-graining can form a noninvertible semigroup on source
descriptions, while a locally Lipschitz beta-function ODE can have a locally
invertible two-sided flow on a selected coupling chart.

Version 2 resolution: prove the separate semigroup and coupling-flow
statements and exhibit both in one example.

### Projection produces universality and fixed points

Decision: withdraw as a generic implication.

Reason: noninjectivity identifies at least one source pair; universality
requires basin attraction or an equivalent observable-convergence theorem.
A fixed point is defined by the RG map, not by an admissibility superlative.

Version 2 resolution: give a finite counterexample, define observable
universality, and prove a contraction criterion.

### Every cutoff is the admissibility boundary

Decision: withdraw.

Reason: regulator, renormalization, matching, threshold, power-counting, and
breakdown scales have different roles. Their values can depend on scheme,
observable, truncation, and target precision.

Version 2 resolution: define an observable-specific validity certificate and
its margin. Its zero set is a boundary for that certificate only. Physical
identification with an MTT boundary requires a same-source theorem.

### Strong coupling means the projection collapsed

Decision: withdraw as a generic claim.

Reason: perturbation theory can fail while a nonperturbative formulation of
the same EFT remains predictive.

Version 2 resolution: separate seven meanings of EFT breakdown and reserve
MTT admissibility exit for cases with a proved margin correspondence.

### MTT is an explicit generic realization of EFT

Decision: narrow to a conditional model bridge.

Reason: current MTT supplies typed projection and local
Feshbach--resolvent control, but no selected certificate identifying a
Wilsonian reduction for arbitrary interacting QFTs.

Version 2 resolution: prove an approximate intertwining theorem and list the
minimum source, scale, encoding, observable, error, boundary, and scheme rows
needed for a physical realization.

## Theorem ownership

Version 2 owns:

- the specialized semigroup-versus-group proposition;
- the local coupling-flow proposition in the declared RG comparison;
- the finite noninjective counterexample to generic universality;
- the observable contraction criterion;
- local stability of the EFT validity certificate; and
- the approximate MTT--Wilsonian observable-transfer theorem.

It imports without re-proving:

- the section, decoder, descent, and merger taxonomy from
  Projection--Admissibility;
- local Feshbach--Schur and resolvent control from Coherent-Sector Reduction;
- current MTT foundational typing; and
- the seven-axis witness discipline from Conditional Classification.

The ordinary differential equation uniqueness result, triangle inequality,
and contraction iteration are standard mathematics and are not claimed as
novel.

## External literature verification

The revision was checked against primary publication records for:

- Kadanoff scaling, DOI
  `10.1103/PhysicsPhysiqueFizika.2.263`;
- Wilson momentum-cell coarse-graining, DOI
  `10.1103/PhysRevB.4.3184`;
- Wilson--Kogut RG review, DOI
  `10.1016/0370-1573(74)90023-4`;
- Wilson's RG review, DOI `10.1103/RevModPhys.47.773`;
- Appelquist--Carazzone decoupling, DOI
  `10.1103/PhysRevD.11.2856`;
- Weinberg's phenomenological Lagrangians, DOI
  `10.1016/0378-4371(79)90223-1`;
- Polchinski's exact RG construction, DOI
  `10.1016/0550-3213(84)90287-6`;
- Wetterich's exact effective-action flow, DOI
  `10.1016/0370-2693(93)90726-X`;
- Georgi's EFT review, DOI
  `10.1146/annurev.ns.43.120193.001233`;
- Burgess's EFT review, DOI
  `10.1146/annurev.nucl.56.080805.140508`; and
- Rosten's exact RG review, DOI
  `10.1016/j.physrep.2011.12.003`.

## Expository review

The revision:

- opens with five distinct claims that Version 1 conflated;
- explains exact coarse-graining, finite truncation, and observable
  evaluation before formal comparison;
- gives a complete Gaussian mode-elimination example;
- distinguishes scale semigroups from reversible coupling ODEs;
- supplies a finite counterexample and a positive contraction theorem for
  universality;
- tabulates six distinct scale roles and seven breakdown meanings;
- defines a quantitative EFT validity certificate;
- states current MTT support without promoting QFT or UV-completion status;
- compares the result with the primary RG and EFT literature; and
- ends with a concrete failure and completion checklist.

## Frontier delta

Before:
Version 1 claimed that EFT, irreversible RG flow, universality, fixed points,
and cutoff breakdown are inevitable consequences of projection under finite
admissibility.

After:
Version 2 establishes a conditional structural comparison. It identifies the
precise inverse-map correction, separates exact coarse-graining from
coupling-coordinate flow, requires basin stability for universality, defines
observable-specific validity margins, and proves the error bound required for
a selected MTT--Wilsonian bridge.

## Release verification

Version 2 was published on 30 July 2026:

- record DOI: `10.5281/zenodo.21711197`;
- concept DOI: `10.5281/zenodo.18262360`;
- Zenodo record: `21711197`;
- version: `v2`;
- canonical file: one `main.pdf`, 342269 bytes;
- remote MD5: `31bbc47f23889417f1e3287718b6e1ba`;
- local PDF SHA-256:
  `2878f2b6dc4b53c8b1f438c8e4d1a46554152aa7280e0cad25eb8a41d02084ba`;
- canonical TeX SHA-256:
  `fd382717b5422739071d0562322aabe7367081044798010496fe09519b6b79ed`;
- canonical source-tree SHA-256:
  `a4f8e46689e10b107f6ce5a133a18c4acfe2abaa707e88db8fe3807fd26ff8b2`;
- 15 explicit references and 2 related repository identifiers; and
- all 12 rendered pages visually inspected, with no clipping, overlap,
  unresolved references, or layout warnings.

The published PDF checksum is identical to the reviewed local artifact. The
publication ledger was reconciled after publication and identifies Version 2
as the current release under the existing concept record.
