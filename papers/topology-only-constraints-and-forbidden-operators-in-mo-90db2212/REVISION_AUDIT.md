# Revision Audit: Bundle Selection Rules, Anomaly Lines, and Charge Lattices

## Scope

This audit governs Version 2 of:

`topology-only-constraints-and-forbidden-operators-in-mo-90db2212`

Supersedes:

- Version 1, DOI `10.5281/zenodo.18261774`.

Controlling correction authority:

- A10, consolidated paper reconciliation, source hash
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.

Current finite-result authorities:

- A46, typed family representation, source hash
  `7413bbfac4fd741ab024a056d31f21a3faa6a959101253e8f41df8afd4358226`;
- A47, native gauge group and parameter audit, source hash
  `21934c068f22a25419b09627a5512aa563556bbf8d95eb23e9d6885c01658de1`;
- A50, neutral summand and hypercharge reduction, source hash
  `327fa5b3468908fef396f4d76dc3e0d98f993d570510d08765dc1bb157be2fd1`;
- A22, selected E6 central-generator anomaly audit, source hash
  `3cfac133dc08f234947772981705cebc432fd4103a783a24a9e6531ca10e3cc3`;
- A04, declared twelve-obligation SM profile closure, source hash
  `0eb2875f60127d2a780812a1f1af7baf2daab090f1a1c780541aeaab17f48899`;
  and
- A05, strict no-knob upgrade ledger, source hash
  `ced380228f057c089181a779aba9b9ad15799031e4475ed09d4d34e91032cda7`.

Source revision lock:

- Version 1 TeX SHA-256
  `6b499ecf6a39c5ab945542e7ca01cf2863157ebcd20d8c5d3dd9761923c7823b`.

## Version 1 claim audit

### Rational hypercharges are tensor powers of one line bundle

Decision: withdraw and replace.

Reason: the continuous characters of `U(1)` are integer powers. A rational
power of a line bundle is not defined until compatible root and
normalization data are supplied.

Version 2 resolution: prove the integer-character lattice theorem, add the
central-quotient descent condition, and treat `Y=n/N` as an explicit
normalization.

### Integral cohomology alone selects the observed hypercharges

Decision: withdraw as a universal theorem.

Reason: an integral charge lattice determines allowed labels, not the matter
spectrum or its primitive normalization.

Version 2 resolution: distinguish the abstract lattice from A50's exact
finite-profile null-vector calculation, which yields
`6Y=(1,-4,2,-3,6,0)` inside the selected finite completion.

### The anomaly line is the determinant of the matter bundle on a spatial
slice

Decision: correct the type.

Reason: the fermionic anomaly is represented by the determinant or Pfaffian
line of a family of chiral Dirac operators over background-field or
configuration space.

Version 2 resolution: state local anomaly as curvature and global anomaly as
holonomy, with gauge compatibility, locality, counterterms, and inflow
included in the cancellation contract.

### A bundle admits an operator exactly when it has a global section

Decision: withdraw and replace.

Reason: nontrivial bundles can have sections with zeros. A four-dimensional
coupling requires a gauge-invariant contraction, an allowed dual coefficient,
selected zero modes, and a nonzero multilinear functional.

Version 2 resolution: define the operator completion record and prove the
typed bundle-selection theorem.

### QQQL and u-c u-c d-c e-c are dimension-five operators forbidden by
hypercharge topology

Decision: correct and narrow.

Reason: in nonsupersymmetric SMEFT these are dimension-six four-fermion
operators, and both are Standard Model gauge singlets.

Version 2 resolution: emit the exact extra Picard classes
`3 ell_Q + ell_L` and `2 ell_u + ell_d + ell_e`. Exclusion now requires one
of those classes, an allowed-coefficient space, or the actual overlap
functional to provide a realization-specific obstruction.

### Majorana mass universally requires a real structure

Decision: narrow.

Reason: the precise condition is an invariant bilinear in the correct
symmetry component together with an allowed coefficient. Real structure is
one sufficient route; pseudoreal representations, flavor multiplicity,
Higgs insertions, and higher operators require separate treatment.

Version 2 resolution: distinguish a sterile bare mass from the
dimension-five Weinberg operator and give both internal line classes.

### Topology alone explains proton stability

Decision: withdraw at the physical MTT tier.

Reason: current MTT does not yet emit the selected physical internal bundle
classes and coefficient functionals for the proton-decay rows.

Version 2 resolution: provide the exact two-row completion certificate and
state what observation would falsify a realization after that certificate is
declared.

## Theorem ownership

Version 2 owns:

- the typed MTT operator completion record;
- the realization-scoped bundle-selection theorem;
- the explicit operator-class table for the declared MTT line notation; and
- the synthesis of current exact finite MTT gauge/anomaly results with the
  still-open physical bundle endpoint.

It derives or specializes, without claiming novelty:

- integer `U(1)` character lattices and central-quotient descent;
- determinant/Pfaffian-line anomaly geometry;
- the conventional one-family Standard Model anomaly arithmetic;
- SMEFT operator dimensions and gauge invariance; and
- the Weinberg-operator Majorana condition.

## External literature verification

The revision was checked against primary records for:

- determinant-line curvature and holonomy, arXiv `dg-ga/9505002`;
- anomalies as invertible field theories, arXiv `1404.7224`;
- global gauge-group effects on hypercharge quantization, arXiv `1302.0669`;
- the dimension-six SMEFT operator basis, DOI
  `10.1007/JHEP10(2010)085`;
- the dimension-five Weinberg operator, DOI
  `10.1103/PhysRevLett.43.1566`; and
- realization-specific heterotic line-bundle selection rules, DOI
  `10.1007/JHEP06(2012)113`.

## Expository review

The revision:

- begins by separating four meanings of "forbidden by topology";
- identifies the base space and type of every bundle;
- explains coefficient spaces and overlap functionals before stating a
  selection theorem;
- gives a concrete section/trivialization/connection distinction;
- proves the charge-lattice theorem before discussing observed hypercharge;
- places anomaly geometry over background-field space;
- checks the conventional anomaly sums explicitly;
- gives one readable operator table containing dimensions, hypercharge sums,
  Picard classes, and exact remaining tests;
- explains why the two proton-decay examples are not removed by Standard
  Model gauge topology;
- integrates current exact A22/A46/A47/A50 results without obscuring the
  A04 profile and A05 no-knob boundaries; and
- ends with falsifiability and an operator-level completion target.

## Frontier delta

Before:
Version 1 claimed broad topology-only hypercharge selection, anomaly
exclusion, proton stability, and Majorana constraints using objects on the
wrong bases and incomplete operator tests.

After:
Version 2 establishes a typed realization-by-realization framework. It
proves the allowed charge lattice and sufficient bundle-selection theorem,
corrects anomaly-line geometry, emits exact classes for seven representative
operators, and records current exact finite MTT gauge/anomaly achievements.
Universal dangerous-operator exclusion and physical compactification
selection remain explicitly open.

## Release verification

Version 2 was released on Zenodo as
[`10.5281/zenodo.21713543`](https://doi.org/10.5281/zenodo.21713543),
under concept DOI
[`10.5281/zenodo.18261773`](https://doi.org/10.5281/zenodo.18261773).
The released record contains exactly one file, `main.pdf`, with:

- remote MD5 `31a8bdc9267f9865c4ec3b497296f2c4`;
- local SHA-256
  `c039abd076bb1b4171777d93ad3883a6f6e3b1dbcbd02a71e055b5b09ab836b6`;
- size 367,630 bytes;
- 9 explicit references; and
- 2 related identifiers.

The final PDF has 11 pages. All 11 rendered pages were visually inspected
for clipping, overlap, equation placement, table layout, references, and
legibility. The final canonical hashes are:

- `main.tex`:
  `02ba3c274b8b0eacf86b79e26a278706bc335a881780a3f04db60be22f5f0c24`;
- `main.bib`:
  `c236b0b7af8e25e9c36e18f990a87ed91495b3340ecc5134b05111f2845a9745`;
- `main.pdf`:
  `c039abd076bb1b4171777d93ad3883a6f6e3b1dbcbd02a71e055b5b09ab836b6`;
  and
- source tree:
  `14b4626c2f56e52d5404c3452563a987104e64d2506abff44cd433a4f76a8ebb`.

The theorem-ownership, interpretive-book, release-requirement, full paper,
strict-boilerplate, and diff checks passed before publication. The canonical
artifact refresh and reviewed-artifact freeze were rerun after
publication-ledger reconciliation.
