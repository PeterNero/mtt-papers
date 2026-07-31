# Revision Audit: Topological Phases as Bundle and Index Data

## Scope

This audit governs Version 2 of:

`topological-phases-of-matter-as-admissible-overlap-stru-837dec46`

Supersedes:

- Version 1, DOI `10.5281/zenodo.18261859`.

Controlling authority:

- A10, consolidated paper reconciliation, source hash
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.

Source revision lock:

- Version 1 TeX SHA-256
  `82c2bdfbe0379a4ff08385b67f1393f95256251bf18545d22d1898c34033fc1d`.

Imported current MTT releases:

- Foundations v9, DOI `10.5281/zenodo.21655367`;
- Projection--Admissibility v2, DOI `10.5281/zenodo.21652659`;
- Local Coherent-Sector Robustness v2, DOI
  `10.5281/zenodo.21710653`;
- Noncommutative Geometry v5, DOI `10.5281/zenodo.21665974`; and
- Topological Consistency Conditions v2, DOI
  `10.5281/zenodo.21666014`.

No numerical result packet is promoted by this paper.

## Version 1 claim audit

### A valid cocycle is a globally trivial completion

Decision: withdraw.

Reason: the cocycle condition is the consistency condition used to construct
a bundle. A bundle is trivial only when the cocycle is a coboundary, or
equivalently when it admits a global frame.

Version 2 resolution: prove the gluing-versus-trivialization proposition and
give the degree-one line bundle over the sphere as an explicit
counterexample.

### A topological phase is precisely failure of global gluing

Decision: withdraw and replace.

Reason: ordinary Chern and K-theory phases are represented by valid global
bundles or projective modules. Their nontriviality lies in the equivalence
class, not in failed transitivity of the gluing relation.

Version 2 resolution: define a typed topological-phase record and locate
topology in its declared bundle, projector, symmetry-protected, many-body,
or operator-algebraic invariant.

### Projection assumptions force phase basins

Decision: withdraw.

Reason: Version 1 argued from observed macroscopic stability, which assumes
the phenomenon it claimed to derive. A phase decomposition requires a
specified state space, equivalence/deformation relation, and stability or
thermodynamic theorem.

Version 2 resolution: no generic phase-basin theorem is claimed.

### Topological obstruction classes are automatically quantized

Decision: narrow to specified invariants.

Reason: discreteness follows only after an actual cohomology, K-theory,
index, or other invariant and its domain have been supplied.

Version 2 resolution: state and prove homotopy invariance for the occupied
bundle Chern number, and identify the separate hypotheses used in free,
disordered, and interacting settings.

### Robustness under all local gap-preserving perturbations

Decision: narrow.

Reason: allowed perturbations must also preserve the relevant algebra,
locality/covariance domain, and protecting symmetry. A mobility gap requires
localization hypotheses different from an empty spectral interval.

Version 2 resolution: prove an explicit norm-gap certificate for a
finite-band class-A family and state the distinct noncommutative disorder
requirements.

### Bulk--boundary correspondence follows from compensation

Decision: withdraw as a theorem and replace with a conditional index result.

Reason: a bulk class does not identify a boundary operator. Standard
bulk--edge results require an interface/Toeplitz extension, Fredholmness,
locality, a gap or mobility gap, symmetry when relevant, and an index
pairing theorem.

Version 2 resolution: state the connecting-map/index theorem with all
required rows. Explain that nonzero index protects spectral flow or
transport on that domain, not necessarily a zero mode at every momentum.

### A trivial bulk forbids boundary modes

Decision: withdraw.

Reason: topologically trivial bulks can have accidental boundary states.
Topology distinguishes protected from removable features under the allowed
deformations.

### One overlap formalism covers free, disordered, interacting, and
superconducting phases equally

Decision: withdraw.

Reason: these settings use different physical algebras, projectors,
symmetries, gap notions, deformation categories, and invariants.
Interactions can reduce free classifications, and intrinsic topological
order requires data not present in a one-particle bundle.

Version 2 resolution: separate the tenfold-way table, noncommutative
mobility-gap construction, many-body flux-torus projector, SPT order, and
intrinsic order.

### MTT generic overlap syntax derives topological phases

Decision: reclassify as a conditional encoding.

Reason: current MTT supplies projector, admissibility, spectral-stability,
finite noncommutative, and topological-consistency language. It does not
select every condensed-matter Hamiltonian, protecting symmetry, physical
projector, invariant, or boundary index construction.

Version 2 resolution: define a seven-row MTT encoding certificate and prove
exact and error-controlled pullback of established invariants after those
source rows are supplied.

## Theorem ownership

Version 2 owns:

- the MTT-specific typed topological-phase record;
- the MTT topological-phase encoding certificate; and
- the exact and controlled MTT invariant-pullback theorem.

It specializes or explains, without claiming novelty:

- cocycle gluing versus coboundary trivialization;
- occupied-bundle Chern number and gap-preserving homotopy invariance;
- the elementary norm-gap perturbation bound;
- tenfold-way free-fermion classifications;
- noncommutative Hall invariants in localized regimes;
- many-body flux-torus Chern constructions; and
- Toeplitz/Fredholm bulk--edge index pairing.

## External literature verification

The revision was checked against primary records for:

- TKNN Hall quantization, DOI `10.1103/PhysRevLett.49.405`;
- Kane--Mele Z2 order, DOI `10.1103/PhysRevLett.95.146802`;
- the Schnyder--Ryu--Furusaki--Ludwig 3D classification, DOI
  `10.1103/PhysRevB.78.195125`;
- Kitaev's periodic table, DOI `10.1063/1.3149495`;
- the tenfold way and dimensional hierarchy, DOI
  `10.1088/1367-2630/12/6/065010`;
- interaction reduction of the BDI classification, DOI
  `10.1103/PhysRevB.81.134509`;
- noncommutative quantum Hall geometry, DOI `10.1063/1.530758`;
- the many-body Hall invariant, DOI `10.1103/PhysRevB.31.3372`;
- interacting Hall quantization, DOI `10.1007/s00220-014-2167-x`;
- Chern/edge correspondence, DOI `10.1103/PhysRevLett.71.3697`;
- the disordered Toeplitz bulk--edge theorem, DOI
  `10.1142/S0129055X02001107`;
- interacting bosonic SPT order, DOI `10.1103/PhysRevB.87.155114`; and
- topological entanglement entropy, DOIs
  `10.1103/PhysRevLett.96.110404` and
  `10.1103/PhysRevLett.96.110405`.

## Expository review

The revision:

- begins by separating six claims conflated in Version 1;
- defines every row needed for a physical topological-phase claim;
- explains the cocycle error before introducing physical classification;
- gives a concrete nontrivial line-bundle counterexample;
- works through the class-A Chern phase and its robustness proof;
- supplies a scoped symmetry-class table;
- explains why disorder, interactions, SPT order, and intrinsic order need
  different records;
- states bulk--boundary correspondence as an index theorem;
- distinguishes MTT coherent, Fermi, and many-body projectors;
- gives a quantitative exact/approximate MTT bridge; and
- ends with a falsifiability and completion checklist.

## Frontier delta

Before:
Version 1 treated failed cocycle gluing as the definition of topology and
claimed generic robustness and bulk--boundary correspondence across free,
interacting, disordered, and superconducting systems.

After:
Version 2 identifies valid cocycle classes, typed physical phase records,
gap- and symmetry-preserving homotopies, and interface index theorems as the
correct objects. MTT is retained as a conditional encoding language with an
explicit source/intertwiner/error certificate. No universal classification
or selected condensed-matter realization is promoted.

## Release verification

Version 2 was published on 31 July 2026:

- record DOI: `10.5281/zenodo.21711367`;
- concept DOI: `10.5281/zenodo.18261858`;
- Zenodo record: `21711367`;
- version: `v2`;
- canonical file: one `main.pdf`, 352564 bytes;
- remote MD5: `064a0daa7a663e743cabcb492ca13bf3`;
- local PDF SHA-256:
  `1af929ca51731548b5969892e120565360a2067d66f3f4c123af4e35f5311bf3`;
- canonical TeX SHA-256:
  `cb16cd6d384633e46ae9df5ea4dc9c6a4cb807a13f1f5591c8993eb1b6751f6f`;
- canonical source-tree SHA-256:
  `64ed569b03d149c9a8938634535e23d0cd4b15997c172d3583d82587da5a3da5`;
- 20 explicit references and 2 related repository identifiers; and
- all 12 rendered pages visually inspected, with no clipping, overlap,
  unresolved references, or layout warnings.

The published PDF checksum is identical to the reviewed local artifact. The
publication ledger was reconciled after publication and identifies Version 2
as the current release under the existing concept record.
