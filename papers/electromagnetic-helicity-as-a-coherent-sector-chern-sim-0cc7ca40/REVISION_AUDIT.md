# Revision Audit: Electromagnetic Helicity from an Induced Line Connection

## Scope

This audit governs Version 3 of:

`electromagnetic-helicity-as-a-coherent-sector-chern-sim-0cc7ca40`

Supersedes:

- Version 2, DOI `10.5281/zenodo.18261452`.

Controlling authority:

- A10, consolidated paper reconciliation, source hash
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.

Source revision lock:

- Version 2 TeX SHA-256
  `306c66c45f22d84515b5261dac6d7811bc58ef55e80b1c86f1431ceac3882b42`.

Imported current MTT releases:

- Foundations v9, DOI `10.5281/zenodo.21655367`;
- Fixed Points I v7, DOI `10.5281/zenodo.21657157`; and
- Topological Phases v2, DOI `10.5281/zenodo.21711367`.

No numerical result packet is promoted by this paper.

## Version 2 claim audit

### MTT selects the physical coherent electromagnetic line

Decision: reclassify as a conditional source contract.

Reason: a rank-one coherent or harmonic projector supplies representation
data, not the physical identification of its range with the photon sector or
an intertwiner with electromagnetic dynamics.

Version 3 resolution: define source rows S1--S6 and identify the physical
line and dynamical rows as open.

### The electric field is obtained by contracting the spatial curvature

Decision: correct the type error.

Reason: contraction with the time vector must be performed on the spacetime
two-form before pullback to a spatial slice. A spatial two-form has no time
leg.

Version 3 resolution: define the full induced curvature `f`, then set
`b_t = i_t^* f` and `e_t = -i_t^*(i_{partial_t} f)`.

### Projector variation creates an extra balance-law remainder

Decision: withdraw and replace.

Reason: once the Berry term is included in the induced connection, its time
variation is already part of the total induced electric field. Adding it
again as a remainder double counts the same geometry.

Version 3 resolution: prove the exact induced-helicity balance with boundary
flux. Reinterpret the old remainder as the error made by replacing the full
induced field with the ambient Abelian surrogate, and prove an L2 comparison
bound.

### A local coherent connection form defines a global real helicity

Decision: narrow.

Reason: a nontrivial line bundle need not admit a global unit frame. On open
or multiply connected domains, ordinary helicity can be gauge dependent
unless a boundary or relative-helicity protocol is supplied.

Version 3 resolution: state a global trivialization and boundary contract for
absolute helicity, and distinguish relative or differential-character data.

### Rank one and coherence imply Hopf quantization

Decision: narrow to the Whitehead specialization.

Reason: integer Hopf charge requires an explicit map from the three-sphere to
the two-sphere and equality of the curvature with the pullback of the
normalized sphere area form.

Version 3 resolution: state both standard normalization conventions and make
the required pullback an explicit source row.

### The Riesz derivative scales as an unspecified constant over gap squared

Decision: replace with a dimensionally explicit theorem.

Reason: for the circle of radius half the gap, the contour length contributes
one power of the gap. For a bounded self-adjoint family, the resulting bound
is `2 ||partial L|| / lambda_*`. Unbounded Laplace-type families also require
common-domain or relative-resolvent hypotheses.

Version 3 resolution: prove the bounded-family estimate and state the
unbounded-domain obligation separately.

### Small projector derivatives imply approximate helicity conservation

Decision: withdraw.

Reason: projector derivatives control the Berry part, but the ambient
electric-magnetic pairing can remain nonzero.

Version 3 resolution: state the correct conservation criterion and a
separate ambient-surrogate error estimate.

## Theorem ownership

Version 3 owns:

- the typed MTT electromagnetic source contract;
- the conditional pullback theorem for the induced-line helicity dictionary;
  and
- the explicit organization of Berry-curvature omission as a surrogate error
  rather than an exact-balance remainder.

It derives or specializes, without claiming novelty:

- curvature of a projected or Grassmann connection;
- Abelian Chern--Simons and helicity gauge behavior;
- the helicity balance and boundary flux;
- Whitehead's integral formula for the Hopf invariant; and
- the contour derivative formula for an isolated spectral projector.

## External literature verification

The revision was checked against primary or standard records for:

- Chern--Simons transgression, DOI `10.2307/1971013`;
- Berry phase, DOI `10.1098/rspa.1984.0023`;
- Berry holonomy, DOI `10.1103/PhysRevLett.51.2167`;
- magnetic helicity and boundary data, DOI
  `10.1017/S0022112084002019`;
- relative helicity on multiply connected domains, DOI
  `10.48550/arXiv.2307.14159`;
- Whitehead's integral Hopf formula, DOI `10.1073/pnas.33.5.117`; and
- Kato perturbation theory, DOI `10.1007/978-3-642-66282-9`.

## Expository review

The revision:

- begins with the three hidden domain questions in the usual helicity formula;
- provides a type table before any physical interpretation;
- explains why the projector term belongs to the connection itself;
- separates exact identities, comparison estimates, and MTT source claims;
- gives the boundary flux rather than suppressing it rhetorically;
- displays both Hopf normalization conventions;
- explains the bounded versus unbounded Riesz-family distinction;
- provides a six-row completion contract for a physical MTT application; and
- ends with explicit achieved and non-achieved claims.

## Frontier delta

Before:
Version 2 claimed a selected MTT electromagnetic line, typed the electric
field incorrectly, and added projector variation as a separate remainder
after it had already been included in the induced connection.

After:
Version 3 establishes an exact induced-line connection and helicity
dictionary, including gauge and boundary domains, an exact balance law,
controlled ambient-surrogate error, correct Hopf normalization, and a
correctly scaled bounded-family Riesz estimate. The MTT physical
electromagnetic source and dynamical identification remain explicit open
rows.

## Release verification

Version 3 was released on Zenodo as
[`10.5281/zenodo.21713347`](https://doi.org/10.5281/zenodo.21713347),
under concept DOI
[`10.5281/zenodo.18261451`](https://doi.org/10.5281/zenodo.18261451).
The released record contains exactly one file, `main.pdf`, with:

- remote MD5 `5a839b88256c77d445b30cc2da3f2414`;
- local SHA-256
  `4c6b2fa1184e9dc2c6e79daffd91d6b6a158f622dd9833f4f24ccb038f0e4200`;
- size 346,309 bytes;
- 10 explicit references; and
- 2 related identifiers.

The final PDF has 10 pages. All 10 rendered pages were visually inspected
for clipping, overlap, equation placement, table layout, references, and
legibility. The final source hashes before release reconciliation were:

- `main.tex`:
  `e3d50561bc0fef5cb045401b572be80c5700106d999868c2c905f09894a54d53`;
- `main.bib`:
  `cbbbb49ad971a30ef01f4b614199f4079e6e48c9e4650a2335b74a46e59ecf14`;
- `paper.md`:
  `cf899b72df511ad6a9b99b0b8d521c7fdfc611922c4929416fe1f76923aa2be3`;
  and
- `metadata.json`:
  `c88c21fb46bb31453defa0c9910a560a2e77fb76752df538e2ccab151c727e09`.

The repository theorem-ownership, interpretive-book, release-requirement,
full paper, strict-boilerplate, and diff checks passed before publication.
The canonical artifact refresh and reviewed-artifact freeze were then rerun
after publication-ledger reconciliation.
