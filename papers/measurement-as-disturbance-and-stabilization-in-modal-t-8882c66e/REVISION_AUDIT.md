# Revision Audit: Measurement as Disturbance, Completion, and Stabilization

## Release Decision

- Current source: Version 6, July 2026.
- Supersedes: Version 5, January 2026.
- Review class: mechanism separation, theorem correction, and current-result promotion.
- Intended tier: exact abstract kernel and contraction results, conditional linear-response model, and exact restricted q79 status.
- Not a universal measurement, Born-rule, uncertainty, or one-history theorem.

## Defects Corrected

1. Version 5 treated localized disturbance and later stabilization as a complete outcome-selection mechanism.
2. It imposed one global contraction while also requiring multiple stable outcome fixed points.
3. Its `Born rule from basin measures` proved only that a chosen measure assigns its own basin probabilities; it did not prove equality to quantum trace weights.
4. It inferred quantum uncertainty from an Ornstein-Uhlenbeck variance without deriving observables, commutators, source coefficients, or hbar normalization.
5. It called noninjective projection the absence of every right inverse, conflating unique decoding with representative selection.
6. It treated decoherence, outcome selection, and record stability as one process.
7. It included Bell, neutrino-mass, and landscape claims outside the paper's measurement remit.
8. It assumed a generic ten-dimensional product as the physical upper geometry rather than using a selected branch.

## Correct Measurement Chain

The revised paper distinguishes:

```text
apparatus coupling/disturbance
  -> outcome-resolved completion
  -> record stabilization.
```

The middle arrow is represented by a normalized transition-completion kernel or a quantum instrument. It supplies both the record probability and the state available to subsequent interactions.

## Exact Results Owned by Version 6

### Transition-completion law

For a preparation law `nu` on an exit space `E` and normalized outcome kernels `K_i`,

```text
p_i = integral_E K_i(x, D_i) dnu(x)
```

is a normalized probability distribution. For `p_i > 0`,

```text
nu_i'(A) = p_i^{-1} integral_E K_i(x, A) dnu(x)
```

is the conditional post-outcome law. This theorem does not derive `nu` or `K`.

### Basin-local stabilization

On each nonempty complete invariant basin `D_i`, a strict contraction `T_i` has one fixed record `r_i` and

```text
d(T_i^n x, r_i) <= q_i^n d(x, r_i).
```

A single contraction on one complete space has only one fixed point. Multiple records therefore require separate basins, a noncontractive transition region, context dependence, a completion kernel, or a combination of these.

### Decoder distinction

For noninjective `P: U -> X`, no map `D: X -> U` can satisfy

```text
D o P = id_U.
```

A section `s` with

```text
P o s = id_X
```

may exist but merely chooses representatives and does not recover the actual upper state.

### Guarded OU result

For

```text
da_t = -gamma a_t dt + sigma dW_t
```

with `gamma > 0` and an independent square-integrable initial state,

```text
Var_stationary(a) = sigma^2 / (2 gamma).
```

This is a conditional effective linear-response result. It is not identified with the Heisenberg uncertainty principle.

## Born Source Obligation

The exact bridge required for every allowed preparation, apparatus, and outcome is

```text
integral_E K_i(x, D_i) dnu_rho(x) = Tr(rho E_i).
```

The left side requires a selected upper preparation law and completion kernel. The right side is the standard quantum instrument probability. Contractivity and normalized basin volumes do not establish the equality.

## Current q79 Promotion

The canonical q79 binary one-anchor nondemolition Fock recorder currently supplies:

- selected finite state, observable, and output-algebra data;
- a commuting record algebra;
- a stopped-output measure from the selected normal state;
- exact second-moment capture descent;
- no added Born axiom, stochastic primitive, observed probability, or fit on that domain.

Controlling current objects:

- `B.QM.01`: exact canonical recorder result, open for arbitrary apparatus contexts and stronger source/actualization demands.
- `ENC.QM.BORN`: mixed L3 status with exactness only on the declared canonical domain.
- authority overlays `A03`, `A05`, `A10`, and `A18`, used only within their recorded scopes.

## Remaining MTT Gates

1. Derive the completion instrument for every intended apparatus context from the selected physical branch.
2. Prove the Born source equality on a nontrivial family of preparations and apparatuses.
3. Derive detector bandwidth, memory, and environmental corrections with error bounds.
4. Prove nondemolition repeatability or basin-local stabilization after completion.
5. Connect the instrument family to contextual and sequential protocols.
6. Decide whether MTT is operational only or derive an objective one-history selector.

## Claims Explicitly Not Made

- Measurement is not observer-created or metaphysically privileged.
- Disturbance alone does not select an outcome.
- Decoherence alone does not select an outcome.
- A global contraction does not provide multiple stable records.
- Projection alone does not create probability.
- Basin volume alone does not derive the Born rule.
- An OU variance does not derive a quantum commutator or hbar.
- Noninjectivity does not forbid every representative section.
- The restricted q79 binary result is not silently universalized.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 6 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- External primary references checked.
- Unrelated neutrino-mass, Bell, and landscape claims removed.
- The current q79 result is reported by tier rather than duplicated as a theorem body.
- LaTeX compiles without unresolved references, overfull boxes, or underfull boxes.
- PDF must be visually inspected page by page before freezing.
