# Program A0 v2 Revision Audit

## Scope

- Paper: *The Modal Triplet Theory Program A0: A Structural Theory of Reduced Description*
- Superseded authoring edition: v1.0
- Selected authoring edition: v2
- Controlling correction authority: A10, *MTT Master Corrigendum and Revision Plan*
- Supporting corrected theorem source: *The Projection--Admissibility Principle: Descent, Recovery, and Structural Constraints on Effective Description*, v2

This is a substantive theorem revision. It is not a boundary-only erratum.

## Required corrections

1. **Invalid right-inverse inference: resolved.**
   The v1 argument from noninjectivity to absence of a right inverse is
   removed. A representative section is separated from an exact upper
   decoder.
2. **Projection--Descent and Recovery Theorem: resolved.**
   The paper now types the upper evolution, initial and final reductions,
   cross-level output map, representative section, exact decoder, autonomous
   reduced evolution, and effective merger. The fiber-preservation criterion
   is proved as necessary and sufficient for deterministic descent.
3. **Distinct failure notions: resolved.**
   Failure of autonomous descent, effective-state merger, failure of exact
   microscopic recovery, and blow-up of stable representative continuation
   are stated as separate conditions.
4. **Valid no-right-section theorem: resolved.**
   The finite-diameter estimate is applied only to a reduced self-map. The
   strict inequality `(1-kappa)D > c epsilon` is required before
   nonsurjectivity and absence of a right section are concluded.
5. **Explicit admissibility margins: resolved.**
   Barriers are defined from named continuous margins and their boundary.
   Section conditioning, loss of surjectivity, and Riesz-projector
   continuation are possible realization-specific margins, not assumed
   obstructions.
6. **Basin-local FCC: resolved.**
   Banach contraction is imposed on each complete invariant basin. An
   additive-error orbit estimate is retained separately and is explicitly
   denied fixed-point-existence force.
7. **Evolution semantics: resolved.**
   Physical evolution and auxiliary stabilization are typed separately.
   Auxiliary contraction is not identified with physical time or a physical
   arrow.

## Additional repairs found in context

- Removed the unsupported undecidability proposition.
- Replaced blanket irreversibility with a typed recovery classification.
- Added a measure-dependent reduced Markov-kernel theorem; projection alone
  no longer creates probabilities or Born weights.
- Replaced the unsupported maximal-content theorem with an exact
  factorization criterion.
- Corrected the encoding-category arrow: the identity encoding is initial,
  not terminal. Recovery arrows require injectivity and regularity.
- Kept approximate arrows out of an unproved quotient category and attached
  explicit composition error budgets.
- Replaced automatic selection at a margin crossing with a separately typed
  reset or continuation rule.
- Removed the claims that FCC necessarily creates records and that all
  boundary layers are universal.
- Corrected the topological boundary to `closure minus interior`.
- Downgraded the encoding "fibration" to a set-theoretic total family unless
  topology and local triviality are supplied.
- Corrected the universal relation: it is the graph of a reduced map exactly
  when the descent criterion holds, not merely when a section is chosen.
- Marked atlas constants and ordering arrows as declared contracts rather
  than universal MTT deductions.

## Retained result

A0 remains a conditional structural framework for finite admissibility,
local encoding charts, explicit coherence margins, basin-local fixed-point
control, re-encoding, and a global chart-of-charts inventory.

## Explicitly not claimed

The revision does not derive a physical measure, Born rule, selection
instrument, entropy law, arrow of time, spacetime dynamics, quantum theory,
gravity, or a concrete MTT realization from projection alone.

## Verification

Run from the paper directory:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run from the repository root after migration metadata is regenerated:

```powershell
python scripts/migrate.py --source-root C:\Users\nero_\Downloads\TEXPAPERS
python scripts/verify.py
```
