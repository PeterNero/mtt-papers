# Revision Audit: Born and Inflationary Probabilities

## Release Decision

- Current source: Version 2, July 2026.
- Supersedes: Version 1, January 2026.
- Review class: major claim reclassification with retained conditional mathematics.
- Intended tier: exact measure-theoretic framework plus a conditional e-fold model.
- Not a completed common-source theorem, Born derivation, or cosmological-measure solution.

## Defects Corrected

1. Version 1 treated a schematic basin functional as a selected MTT probability measure.
2. It inferred the Born rule from normalized basin weights without proving that those weights equal squared quantum amplitudes for the declared instruments.
3. It claimed that Born and inflationary probabilities were already projections of the same physical source without specifying one source measure, typed maps, context dependence, or pushforward equalities.
4. It treated non-injective projection as though it generated probability.
5. It presented `C(N) = kappa(Nc-N)`, `Delta A / hbar = lambda/C(N)^2`, and `exp(3N)` volume weighting as derived rather than assumed.
6. It inferred regulator-independent normalizability and avoidance of eternal inflation from normalizability of one chosen one-dimensional density.
7. It treated ordinary observational compatibility of plateau inflation and tension of simple monomial models as validation of the proposed weight.
8. It drew unsupported conclusions about time, entropy, basin entry, collapse, and the beginning of the universe.

## Exact Results Owned by Version 2

### Projection guardrail

A measurable non-injective map does not determine a probability law. In particular, a point measure pushes forward to another point measure.

### Trivial common realization

For arbitrary target laws `nu_Q` and `nu_C`, the product source

```text
U = Omega_Q x Omega_C,
mu = nu_Q tensor nu_C
```

has the two laws as coordinate marginals. Bare common-source existence is therefore non-explanatory. Physical content requires prior selection of the source and maps.

### Conditional e-fold theorem

For positive `alpha`, `beta`, and `p`, and real `Nc`,

```text
w(N) = exp(beta N - alpha/(Nc-N)^p),  N < Nc
```

is integrable, has finite polynomial moments in `Nc-N`, and has the unique mode

```text
N_mode = Nc - (alpha p / beta)^(1/(p+1)).
```

The old model is the special case `beta = 3`, `p = 2`, and `alpha = lambda/kappa^2`.

### Curvature pushforward

Under the separately assumed relation `Omega = Omega_star exp(-2N)`, the paper computes the exact transformed density and its domain. This is a change-of-variables theorem, not a derivation of the curvature relation.

## Current MTT Interface

The current q79 program has advanced beyond Version 1 on one restricted quantum domain:

- the canonical binary one-anchor recorder emits its stopped output measure from the selected normal state on the commuting Fock output algebra;
- second-moment capture descent is exact on that domain;
- no observed probability is used as a fit input there.

The general Born source theorem remains open for arbitrary allowed apparatus contexts, finite-bandwidth or non-Markov control, and objective selection of one ontic history.

The common-measure bridge remains open because there is no selected:

1. inflationary history space and physical quotient;
2. gauge- and slicing-invariant event sigma-algebra;
3. normalized cosmological source law;
4. cosmological observable pushforward;
5. same-source map connecting that construction to the q79 recorder.

Controlling current objects:

- `ENC.BOUND.MEASURE`, level L0 interpretive, proof tier open.
- `B.MEASURE.01`, common physical measure and pushforwards, open.
- `B.QM.01`, general Born source theorem, open with the canonical q79 recorder closed on its restricted domain.

## Parameter Ledger for the Illustrative Model

- `Nc`: proposed front location, not selected.
- `beta`: exponential history/volume weight; `beta = 3` assumes three-dimensional physical-volume weighting.
- `p`: barrier exponent; `p = 2` is an ansatz.
- `alpha`: barrier scale; in the old parametrization it combines `lambda` and `kappa`.
- `Omega_star`: additional scale required for the curvature proxy.

Normalization removes only an overall multiplicative constant. It does not select these inputs.

## External Checks

- Ben Freivogel, *Making predictions in the multiverse*, Classical and Quantum Gravity 28 (2011) 204007, DOI 10.1088/0264-9381/28/20/204007.
- Planck Collaboration, *Planck 2018 results. X. Constraints on inflation*, Astronomy and Astrophysics 641 (2020) A10, DOI 10.1051/0004-6361/201833887.
- BICEP/Keck Collaboration, *BICEP/Keck XIII*, Physical Review Letters 127 (2021) 151301, DOI 10.1103/PhysRevLett.127.151301.

The observational values are explicitly historical reference points, not claimed as a latest-data likelihood and not used to fit the illustrative density.

## Claims Explicitly Not Made

- No claim that projection creates probability.
- No universal Born-rule derivation.
- No physical solution of the eternal-inflation measure problem.
- No MTT prediction of the e-fold parameters.
- No claim that plateau-model compatibility validates the proposed measure.
- No derivation of low initial entropy, the arrow of time, the Big Bang, or quantum collapse from basin entry.
- No identification of the shared compact phase circle with physical time.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 2 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- External primary references verified.
- No duplicated MTT theorem body.
- PDF must be visually inspected page by page before freezing.
