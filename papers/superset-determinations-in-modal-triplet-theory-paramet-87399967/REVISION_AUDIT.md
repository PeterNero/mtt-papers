# Revision Audit: Superset Determinations v3

Date: 2026-07-29

## Purpose

This paper owns the parameter-identifiability interpretation of the MTT
superset strategy. It does not own the imported gauge, finite-triple, Yukawa,
Higgs, or spectrum theorem bodies.

## Current Ledger

The paper was checked against the current parameter and authority state.

| Class | Count | Status |
|---|---:|---|
| Construction-side continuous primitives | 1 | Shared `P_EW`, counted once |
| Measured SM profile coordinates | 15 | Empirical inputs with declared covariance policy |
| Neutral extension profile coordinates | 2 | Outside the 12/12 SM baseline |
| Higgs-specific construction parameters | 0 | No separate Higgs knob |
| Transported SMDR output rows | 8 | Outputs, not new independent inputs |
| Charged Yukawa magnitude rows | 9 | Outputs at finite-replay/profile tier |
| Finite Dirac dimension | 96 | Structural dimension, not a parameter count |

The current authority explicitly forbids three misleading interpretations:

- one shared construction primitive does not mean one total empirical input;
- measured profile inputs are not derived no-knob predictions;
- no strict parameter reduction relative to the Standard Model is claimed.

## Contextual Corrections

- The title now says profile-standard SM closure rather than unqualified
  true-SM closure.
- The abstract contains only the current scientific content.
- The mandatory version-delta fields are present.
- The old one-loop crossing, fitted zeta, minimum-norm threshold, common-scale,
  and alpha-s cross-prediction chain remains retired.
- The nine charged Yukawa rows are explicitly retained as closed at the
  finite-replay/profile standard; the separate zero-primitive source theorem
  remains open.
- A46-A50 native gauge, chiral carrier, and finite-triple results are included.
- A51 one-Higgs projection and A61-A62 10/10 finite spectrum rows are included.
- The universal normalized spectrum no-go is stated: finite spectra alone do
  not emit the observed gauge-coupling ratios.

## Scope Decision

The superset is a common representation and constraint architecture. It can
reduce duplicated sector constructions and expose cross-sector consistency
conditions. It does not currently reduce the strict empirical continuous
input count relative to the Standard Model.

## Verification Required

- compile `main.tex`;
- render and visually inspect every PDF page;
- refresh `paper.md` and metadata;
- preserve a plain-text Zenodo abstract;
- run release and theorem-ownership verifiers;
- freeze reviewed hashes only after all checks pass.
