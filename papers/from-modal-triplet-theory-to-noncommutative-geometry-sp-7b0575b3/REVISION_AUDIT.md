# MTT to Noncommutative Geometry v4 Revision Audit

Date: 2026-07-28

Status: implemented as a new TeX successor; v3 preserved

## Source and disposition

- Superseded source:
  `15 Discrete & Spectral & Operator Geometric Theories/_work/Modal_Triplet_Theory__From_MTT_to_Noncommutative_Geometry_v3`
- Superseded `main.tex` SHA-256:
  `7e5f37f5a59ddce8e293d5feaf817a7f6f7aa4c0321dff7259daa5bd985e0d7f`
- Successor:
  `15 Discrete & Spectral & Operator Geometric Theories/revised_tex_vnext/Modal_Triplet_Theory__From_MTT_to_Noncommutative_Geometry_v4`
- Disposition:
  retain as a typed almost-commutative encoding; withdraw the first-principles
  derivation and unique-normalization claims.

## Controlling current authorities

The current-status decisions use the curated authority rows, not historical
corpus wording:

| Authority | SHA-256 | Use in v4 |
|---|---|---|
| A10 | `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e` | Master correction specification |
| A44 | `2a3a4345f1ddc4fe2d1a8ad838abdb02c832701fae02fed57c7b8f2902fab721` | Qutrit/SM algebra no-go and conditional corner bridge |
| A45 | `23ff816d6b04789f479dca6c8bf70f790832c7ef1cbb995115ff458d0388f633` | Family/gauge-factor correction and selected rank flag |
| A46 | `7413bbfac4fd741ab024a056d31f21a3faa6a959101253e8f41df8afd4358226` | Three-family chiral representation and anomaly table |
| A47 | `21934c068f22a25419b09627a5512aa563556bbf8d95eb23e9d6885c01658de1` | Native gauge group and global Z6 quotient |
| A48 | `75412a0ee97081196e2cd3b331fdf53a2346c6bd96bb2d209e357abbbd01d054` | Explicit finite bimodule |
| A49 | `221241fe49f9390ad1be6d75320a0c6cbe565914860b2e723a5e0e09a04c1e59` | Profile finite Dirac operator and three-summand no-go |
| A50 | `327fa5b3468908fef396f4d76dc3e0d98f993d570510d08765dc1bb157be2fd1` | Neutral completion and anomaly-free shared circle |
| A51 | `423e3ae86dd8b5abee19e38d53f0bb003fb53fc0e5adc872076cab546934e893` | Finite one-forms, one-Higgs projector, and profile traces |
| A52 | `cd5c4a0af557470a6687a71241228432e4c9d94b216c69a37aec6fbf6823f99e` | Product-triple scope, normalization no-go, and moment ambiguity |

## Evaluation of the three recorded corrections

### 1. The Standard Model finite algebra was assumed

The correction remains applicable, but current results permit a stronger
replacement.

- v3 began with `C + H + M3(C)` and called the result an MTT derivation.
- A44 proves that the selected qutrit algebra `M3(C)^3` is not isomorphic to
  that algebra by real dimension and center dimension.
- A45 proves that the `C^3` factor is the family/character factor, not the
  three gauge-rank lanes.
- A46-A50 then construct the separate gauge representation, native group,
  finite bimodule, necessary neutral summand, orientation/intersection data,
  and unique anomaly-free hypercharge line.

Version 4 therefore states an executed finite profile construction rather
than either an assumed algebra or a direct renaming of the qutrit algebra.

### 2. The Wick dictionary was absent

The correction remains fully applicable.

Version 4:

- declares the product spectral triple to be Euclidean;
- lists the minimum Lorentzian-to-Euclidean data needed for a physical Wick
  contract;
- states that the compact shared phase circle is not physical time; and
- cites the primary NCG literature on Wick rotation and fermion doubling.

No MTT theorem currently supplies this physical Wick contract.

### 3. Spectral-action assumptions were conflated with fixed-point projection

The correction remains applicable.

Version 4 adds a reducing-projector theorem. A fixed-point projector preserves
an existing real even spectral triple only when it reduces the algebra
representation and Dirac operator, commutes with the real structure and
grading, remains faithful, and separately preserves the finite orientation
and pairing data. This proves exactly what projection can do without claiming
that projection constructs the spectral input.

## Additional current-result corrections

Version 4 also makes the following changes required by post-audit results:

1. Records the A49 no-go for the uncompleted three-summand finite triple.
2. Uses the selected additional neutral complex summand from A50.
3. Records that raw A51 inner fluctuations contain three Higgs doublets.
4. Uses the selected rank-four projector for the one-Higgs profile sector.
5. Labels the finite Dirac entries and Yukawa traces as profile replay.
6. Records the A52 no-go for universal gauge normalization on the selected
   pure-SM running branch.
7. Records the exact scaling degeneracy of the cutoff scale and moments.
8. Replaces FRG/pAQFT/QG "matching" by a typed compatibility statement.
9. Adds explicit curated result identifiers and repository provenance.

## Retained theorem content

The following content survives:

- the standard product-triple theorem after its Euclidean and finite inputs
  are supplied;
- compact resolvent and bounded commutators under the standard product
  hypotheses;
- the standard spectral-action heat-kernel expansion;
- generation of gauge and scalar operator content by inner fluctuations; and
- compatibility of the selected finite profile triple with that standard NCG
  machinery.

## Remaining boundary

The successor does not claim:

- a physical nonpullback q79 HYM realization;
- a connection/Hessian-preserving continuum intertwiner;
- an MTT derivation of Lorentzian spacetime or Wick rotation;
- source-derived finite Dirac/Yukawa values;
- source-derived overlap kinetic metric or proper-time measure;
- unique spectral cutoff moments;
- no-knob Standard Model values; or
- a renormalized nonperturbative quantum field theory.

These boundaries agree with the current B.GEO.01, B.OP.01, B.ACTION.01,
B.QFT.02, B.SM.01, and B.SM.02 frontier.
