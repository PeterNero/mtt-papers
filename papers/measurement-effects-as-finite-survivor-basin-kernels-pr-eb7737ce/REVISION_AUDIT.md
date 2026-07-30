# Revision Audit: Finite-Resolution Position Measurements

## Release Decision

- Current source: Version 1, July 2026.
- Supersedes: the unversioned April 2026 manuscript.
- Review class: measurement-object correction, exact detector-smearing theorem, and outcome-completion scope control.
- Intended tier: exact POVM, instrument, convergence, error-bound, Gaussian, and qubit results for the stated models; conditional as an MTT detector source.
- Not a derivation of the Born rule, a universal apparatus model, or a one-history theorem.

## Defects Corrected

1. The earlier source described the formal density `|x><x|` as though it were the position PVM itself.
2. It called projective measurement in general a distributional singular limit, which is false for ordinary discrete spectral projections.
3. It defined finite effects but allowed them to stand in for the post-measurement update, realized outcome, and stabilized record.
4. It did not emphasize that one POVM admits multiple instruments with different sequential predictions.
5. It gave only pointwise approximate-identity convergence under continuity rather than the stronger natural `L1` and total-variation result.
6. It supplied no explicit finite-resolution error certificate.
7. It treated a conditional Ornstein-Uhlenbeck variance as a lower bound on detector width without deriving a calibration map.
8. It suggested that basin stabilization softens or solves outcome selection, although stabilization acts only after an outcome-completion step.

## Correct Measurement Chain

The revised paper keeps the following objects distinct:

```text
physical coupling and detector response
  -> outcome-resolved instrument
  -> completion into one record
  -> amplification or basin-local stabilization.
```

A POVM gives outcome probabilities. An instrument also gives conditional output states. Neither object alone supplies an ontic one-history selector.

## Exact Results Owned by Version 1

### Sharp position PVM

On `L2(R^d)`, sharp position is the PVM

```text
(Q(B) psi)(y) = 1_B(y) psi(y).
```

Its formal density uses generalized vectors, but every set-valued projection `Q(B)` is a bounded operator.

### Detector smearing theorem

For a normalized response profile `g_epsilon`, the classical response channel

```text
kappa_epsilon(B | y) = integral_B g_epsilon(x-y) dx
```

defines the commutative POVM

```text
E_epsilon(B) = integral kappa_epsilon(B | y) Q(dy).
```

It is exactly a classical post-processing of sharp position.

### Total-variation sharp limit

For every normalized `psi` in `L2`,

```text
p_epsilon = g_epsilon * |psi|^2
```

converges to `|psi|^2` in `L1`. The corresponding outcome measures converge in total variation.

### Finite-resolution error certificate

If `f = |psi|^2` is in `W^{1,1}` and the detector profile has finite first absolute moment,

```text
||p_epsilon - f||_1
  <= epsilon m_1(g) ||grad f||_1.
```

The total-variation error is half this bound.

### Square-root detector instrument

For bounded response density, multiplication by `sqrt(g_epsilon(x-y))` supplies a normalized completely positive instrument whose associated effects are exactly `E_epsilon`. This is one compatible instrument, not a uniquely selected update.

### Gaussian broadening

For centered isotropic Gaussian blur,

```text
X_epsilon = Y + epsilon Z,
Cov(X_epsilon) = Cov(Y) + epsilon^2 I_d.
```

The statement assumes finite second moments.

### Discrete qubit limit

For

```text
E_plus/minus(eta) = (I plus/minus eta sigma_z)/2,
```

the norm error from the sharp projection is `(1-eta)/2`. This regular operator limit demonstrates that not every PVM limit is distributional.

## Standard Input and MTT Boundary

The finite outcome density is evaluated with the standard quantum trace rule. The paper does not derive that rule.

The current q79 binary one-anchor recorder supplies exact selected state, observable, output-algebra, and stopped-record data on its declared domain. It does not yet emit arbitrary continuous detector kernels or a universal apparatus instrument.

A strict MTT detector theorem still needs:

1. selected system-apparatus dynamics;
2. derivation of the response profile or effect kernel;
3. derivation of the compatible instrument;
4. a preparation source for every intended context;
5. any one-history completion rule demanded by the ontology;
6. repeatability or basin-local record stabilization; and
7. a calibration theorem connecting selected dynamics to detector width.

## Claims Explicitly Not Made

- Measurement is not observer-created or metaphysically privileged.
- A POVM does not determine a unique instrument.
- An instrument does not by itself prove one-history actualization.
- Basin contraction does not select which basin is entered.
- Decoherence does not select one instrument element.
- The trace rule is used rather than rederived.
- A detector-smearing theorem is not a universal MTT source theorem.
- The parameter `epsilon` is not identified with an OU or coherence floor.
- Discrete projective measurements are not distributional point projectors.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 1 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- Primary Davies-Lewis instrument reference checked; Holevo's statistical-structure reference supplied for context.
- Measurement interaction, effect, instrument, outcome completion, and stabilization are separated.
- LaTeX compiles without unresolved references, overfull boxes, or underfull boxes.
- All nine PDF pages were visually inspected after the final compile; no clipping, overlap, broken tables, or unreadable equations were found.
