# Spatial Bell/beables paper v2 revision audit

## Identity

- Paper: `Modal Fixed Points, Bell's Beables, and the Limits of Factorization`
- New version: `v2`
- Superseded release: `v1.0`, Zenodo record `17076301`
- Revision class: interpretation and theorem-boundary correction

## Central result retained

The paper retains the useful upper-world interpretation:

```text
upper-local dynamics
+ microcausal/base-local descent
+ local instruments
+ a globally nonseparable admissible state
```

This package can violate Bell factorization without a controllable
superluminal signal. It is not a Bell-local hidden-variable completion.

## Corrections

### 1. Bell locality was distinguished from no-signaling

The prior text called the upper ontology local while also claiming quantum
CHSH agreement. Version 2 states explicitly that measurement independence and
CHSH violation force failure of conditional Bell factorization. Algebraic
microcausality and operational no-signaling remain compatible with that
failure.

### 2. The hidden-state contract was repaired

The former fixed point `Psi*(a,b,xi)` depended on both settings while `xi` was
treated as a complete measurement-independent seed. Version 2 instead uses a
preparation-selected state independent of the later settings. A
setting-dependent alternative must be declared as an atemporal global
boundary-value, retrocausal, contextual, incomplete-state, or
measurement-dependent branch.

### 3. Projection was no longer credited with creating the correlations

Projection does not by itself select a nonseparable state, probability rule,
instrument, or Bell correlator. The revised interpretation is descent of
upper nonseparability: the global state carries the correlation and a
base-local descent exposes it without transmitting a spacelike signal.

### 4. Locality descent received an explicit hypothesis and proof

The new locality-descent lemma requires a fiberwise projector/integral that
preserves support in the causal base. A generic global or spatially nonlocal
projector does not satisfy this condition automatically.

### 5. No-signaling no longer imports an unproved MTT Born theorem

No-signaling is proved conditionally from standard local completely positive
instruments on a normal state. The selected MTT probability source, detector
instruments, and singlet state remain rows of the completion contract.

### 6. The Kaluza--Klein comparison was corrected

The former proposition inferred Bell factorization from local
Kaluza--Klein/zero-mode dynamics. This is false: local quantum field theories
can have nonseparable states while spacelike algebras commute. Version 2
removes that proposition and identifies state selection, rather than locality
alone, as the possible MTT contribution.

### 7. Quantum and network examples were reclassified

The singlet value `2 sqrt(2)` is a standard benchmark. It becomes an MTT
result only when one selected MTT source emits the state, descent,
instruments, and probability functional. Claims that arbitrary network
quantum bounds are already realized were removed.

### 8. Spatial and temporal Bell papers were separated

The spatial paper concerns Bell factorization and two-way no-signaling.
Temporal Leggett--Garg experiments permit forward disturbance and are owned by
the separate temporal Bell paper. A common interpretation is possible, but a
unification theorem requires explicit intertwiners and probability
preservation.

## Theorem ownership

This version owns:

1. the base-local internal locality-descent lemma;
2. the conditional MTT Bell completion proposition.

It imports:

1. CHSH under measurement independence and factorization;
2. the standard local-instrument no-signaling argument;
3. the singlet/Tsirelson benchmark.

## Status after revision

The paper is a rigorous conditional reconstruction and interpretive
clarification. It proves that the proposed package is logically consistent
with no-signaling and Bell violation. It does not yet prove that selected MTT
geometry emits the required nonseparable state, probability source, or
detector instruments.
