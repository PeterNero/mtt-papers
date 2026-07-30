# Revision Audit: Born-Compatible Records and the Classical Limit

## Release Decision

- Current source: Version 2, July 2026.
- Supersedes: Version 1, January 2026.
- Review class: theorem separation and current-result promotion.
- Intended tier: exact canonical-domain q79 status plus exact finite concentration and persistence theorems.
- Not a universal Born theorem or an objective one-history selection theory.

## Defects Corrected

1. Version 1 claimed that the Born rule and the classical limit were the same problem.
2. It inferred squared-norm basin weights from non-injective projection without a source measure or basin-trace theorem.
3. It invoked Gleason-style reasoning without placing additivity, noncontextuality, dimension, and measurement-class assumptions in the logical chain.
4. It conflated decoherence, concentration, record stability, and outcome actualization.
5. It treated normalized basin weights as a physical origin of probability.
6. It described a unified resolution that exceeded the available MTT source theorem.

## Imported Quantum Framework

For a quantum instrument `{I_i}` with effects `E_i = I_i*(1)`, standard operational quantum mechanics gives

```text
p_i = Tr(rho E_i).
```

Gleason's theorem imports a trace representation for additive projection measures on real or complex Hilbert spaces of dimension greater than two. POVM-based extensions can include qubits. These results characterize a consistent probability assignment; they do not construct the selected MTT source law.

Primary references checked:

- A. M. Gleason, *Measures on the Closed Subspaces of a Hilbert Space*, Journal of Mathematics and Mechanics 6 (1957), 885-893, DOI 10.1512/iumj.1957.6.56050.
- C. M. Caves, C. A. Fuchs, K. Manne, and J. M. Renes, *Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements*, Foundations of Physics 34 (2004), 193-209, DOI 10.1023/B:FOOP.0000019581.00318.a5.
- W. H. Zurek, *Decoherence and the Transition from Quantum to Classical - Revisited*, arXiv:quant-ph/0306072.

## Current q79 Promotion

The current project ledger establishes the following on the canonical q79 binary one-anchor finite-symbol domain:

- selected Hilbert/state/observable data and reduced dynamics;
- a commuting nondemolition Fock output algebra;
- a stopped output measure emitted by the selected normal state;
- exact `SecondMomentCaptureDescent`;
- no separately added Born axiom, stochastic primitive, observed probability, or fit on that domain.

Controlling current objects:

- `ENC.QM.BORN`, level L3 controlled/profile, mixed proof tier.
- `B.QM.01`, open only beyond the canonical recorder for general apparatus contexts and additional semantic/actualization demands.

The paper does not reproduce the q79 theorem body. It reports the current status and builds a separate classical-limit interface.

## Exact Results Owned by Version 2

### Classical concentration

If one finite record has probability at least `1 - epsilon`, then

```text
d_TV(p, delta_i*) = 1 - p_i* <= epsilon
```

and every bounded record observable differs from its deterministic value by at most

```text
epsilon * oscillation(f).
```

### Finite-horizon persistence

If the initial dominant-record probability is at least `1 - epsilon` and every conditional per-step escape probability is at most `eta`, then

```text
P(record i* survives through step n)
  >= (1-epsilon)(1-eta)^n
  >= 1-epsilon-n eta.
```

No Markov assumption is required for this finite conditional bound.

### Decoherence guard

If the trace distance between a state and its pointer-dephased state is at most `delta`, every effect probability changes by at most `delta`. Exact decoherence still need not imply concentration.

## Correct Logical Chain

1. Instrument and record algebra identify alternatives.
2. A selected state/measure and capture map supply probabilities.
3. Additivity or effect noncontextuality can imply trace representation.
4. Decoherence suppresses operational interference.
5. Concentration controls deterministic approximation.
6. Persistence controls record stability.
7. Objective actualization, if demanded, remains separate.

The same record labels may occur in all seven rows, but this does not identify the rows as one theorem.

## Remaining MTT Gates

1. Extend exact second-moment capture descent to every allowed apparatus and preparation context.
2. Derive finite-bandwidth and non-Markov detector corrections with error bounds.
3. Select a physical scaling regime in which the concentration error tends to zero.
4. Derive a record-escape bound that remains small on the intended observation horizon.
5. State whether MTT is only an operational record theory or also supplies an objective one-history law.

## Claims Explicitly Not Made

- Projection alone does not derive the Born rule.
- Gleason's theorem is not an MTT source theorem.
- Decoherence does not select one outcome.
- Concentration does not derive general quantum probabilities.
- The canonical q79 binary result is not silently universalized.
- Operational record probabilities do not by themselves actualize one ontic history.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 2 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- External primary references checked.
- The current q79 result is referenced by status rather than duplicated as a theorem body.
- PDF must be visually inspected page by page before freezing.
