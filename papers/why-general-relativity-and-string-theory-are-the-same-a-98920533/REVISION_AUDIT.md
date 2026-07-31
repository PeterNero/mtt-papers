# Worldsheet--Spacetime Diagnostic Square v2 Release Audit

## Selected revision

- Paper: `Worldsheet and Spacetime Consistency as a Conditional Diagnostic Square`
- Superseded version: v1.0
- Prior release DOI: `10.5281/zenodo.18261980`
- Selected successor: v2
- Controlling correction authorities: A10 and A13
- Live blockers: B.QG.01 and B.ACTION.01

## Context audit

Version 1 was checked against the revised Foundation, projection-first string,
Hull--Strominger, General Relativity, controlled-truncation, and upper-action
papers. It was also checked against the standard nonlinear sigma-model,
background-field, Weyl-anomaly, and target effective-action literature.

The useful idea survives only in a typed form. Worldsheet Weyl conditions and
target effective equations can be compared as diagnostics of one background
record. They are not identical theories, and an MTT common-source explanation
requires independently constructed source maps.

## Required corrections and resolutions

### 1. Identity of theories

**Prior claim:** General Relativity and perturbative string theory are the
same admissibility constraint.

**Finding:** The standard result compares anomaly coefficients and target
effective equations at a specified order, field content, and scheme. Pure
Einstein gravity is a further restricted low-energy corner.

**Resolution:** Version 2 replaces theory identity by a controlled diagnostic
square and states explicitly what is and is not compared.

### 2. Missing fields and orders

**Prior claim:** Vanishing of the metric beta function yields the Einstein
equations, with a generic controlled correction.

**Finding:** The leading condition also contains the dilaton and three-form;
heterotic models add gauge and anomaly data. Higher alpha-prime terms, string
loops, compactification, and field redefinitions are independent controls.

**Resolution:** Version 2 prints the leading coupled beta function and
tree-level NS--NS action, then gives an eight-source error ledger.

### 3. Assumed conjugacy

**Prior claim:** The MTT proper-time flow is scheme-equivalent to worldsheet
RG, and fixed-point transfer proves the bridge.

**Finding:** The conjugacy was assumed. Proper time and Wilsonian worldsheet
RG are not automatically the same flow.

**Resolution:** The revised theorem requires an explicit comparison map,
residual, and inverse estimate. A stated conjugacy is treated as a hypothesis
to be constructed, not a derivation.

### 4. Common fixed points

**Prior claim:** Coincident admissible fixed points imply equivalence.

**Finding:** Common zero sets do not control residuals or stability.

**Resolution:** Version 2 proves the counterexample D1(x)=x, D2(x)=x^3.
Their zero sets agree, but the comparison inverse diverges near the fixed
point.

### 5. Spectral scale and string scale

**Prior claim:** alpha-prime is the inverse MTT spectral gap.

**Finding:** The two scales have different definitions. A relation requires a
selected source theorem, dimensional conventions, and coefficient matching.

**Resolution:** The relation is retained only as a possible future bridge,
not an identity.

### 6. q79 status

**Prior claim:** The common-source bridge was constructed.

**Finding:** The current q79 worldsheet contract has five available rows, two
partial rows, and five open rows. The physical visible--hidden worldsheet and
upper action remain open.

**Resolution:** Version 2 reproduces the authoritative twelve-row contract
and keeps B.QG.01 and B.ACTION.01 open.

### 7. Theorem ownership

**Prior problem:** Two neighboring GR/string papers asserted substantially
the same bridge theorem.

**Resolution:** This paper now owns the formal controlled diagnostic-square
theorem. The companion `Why GR Falls Out of String Theory` paper is to be
revised as an expository interpretation that cites this theorem without
duplicating it.

## External references checked

- Friedan, `Nonlinear models in 2+epsilon dimensions`, 1980.
- Callan, Friedan, Martinec, and Perry, `Strings in background fields`, 1985.
- Metsaev and Tseytlin, two-loop equivalence and scheme dependence, 1987.
- Hull and Townsend, sigma-model conformal anomalies and string effective
  actions, 1988.

## Visual and build audit

- `pdflatex` completed twice without undefined references or overfull boxes.
- All nine pages of `main.pdf` were rendered with Poppler and visually
  inspected.
- Equations, tables, references, headings, margins, and page numbers are
  legible and free of overlap or clipping.

## Frontier after revision

The paper-level correctness blocker is resolved. The result is now a rigorous
conditional theorem for exact or controlled transport between two diagnostics,
plus a no-go result showing why common fixed points are insufficient.

The physical frontier is unchanged: B.QG.01 requires the complete twelve-row
q79 worldsheet contract on the same selected background, and B.ACTION.01
requires the selected upper action and automorphism transfer. No new
calculation result or source selection is claimed.
