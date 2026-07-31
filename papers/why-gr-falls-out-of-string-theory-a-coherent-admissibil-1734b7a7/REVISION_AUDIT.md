# Why General Relativity Appears in Perturbative String Theory v2 Release Audit

## Selected revision

- Paper: `Why General Relativity Appears in Perturbative String Theory`
- Superseded version: v1.0
- Prior release DOI: `10.5281/zenodo.18262012`
- Selected successor: v2
- Controlling correction authorities: A10 and A13
- Live blockers: B.QG.01 and B.ACTION.01

## Editorial role

This paper is the explanatory companion to
`Worldsheet and Spacetime Consistency as a Conditional Diagnostic Square`.
The technical companion uniquely owns the controlled comparison theorem and
common-zero no-go result. This paper contains no formal theorem environment
and does not reproduce either proof.

## Context audit

Version 1 was checked against the revised projection-first string paper,
Hull--Strominger paper, technical diagnostic-square paper, and current q79
worldsheet contract. It was also checked against the standard primary
sigma-model and string effective-action literature.

The intended educational idea is retained: string worldsheet consistency
constrains target geometry and explains why Einstein dynamics occurs in the
low-energy metric sector. The previous claim that the two theories are
equivalent MTT shadows is not retained as an established result.

## Required corrections and resolutions

### 1. Explanatory versus theorem-owning role

**Prior problem:** The paper repeated substantially the same equivalence
theorem as its technical companion.

**Resolution:** Version 2 explains the physical chain and cites the technical
owner. It adds no competing formal theorem.

### 2. The standard result

**Prior claim:** Vanishing metric beta function directly reproduces the
Einstein equation.

**Finding:** The leading metric coefficient is coupled to the dilaton and
three-form, while other fields have their own equations. The target action is
scheme- and field-redefinition-aware.

**Resolution:** Version 2 prints the coupled leading coefficient, explains the
target effective action, and treats pure GR as a further restricted
low-energy corner.

### 3. Error control

**Prior claim:** One inverse spectral-gap error controlled worldsheet,
spacetime, and higher-curvature corrections together.

**Finding:** Alpha-prime, string loops, worldsheet completion,
compactification, field redefinitions, and MTT projection are independent
controls.

**Resolution:** Version 2 separates all of them and withdraws the automatic
identification of alpha-prime with an inverse MTT gap.

### 4. Assumed flow equivalence

**Prior claim:** MTT proper-time rescaling and worldsheet RG were
scheme-equivalent, yielding common fixed points.

**Finding:** The comparison map was assumed rather than built.

**Resolution:** The paper now presents the common-source diagram as a research
question. It explains that every arrow, residual, inverse estimate, and source
hash must be supplied.

### 5. q79 status

**Prior claim:** The string corner and infrared GR shadow were already
realized from one source.

**Finding:** The q79 worldsheet contract is five available, two partial, and
five open. The physical visible--hidden bundle, exact infrared conformal
theory, GSO/modular completion, and upper action remain open.

**Resolution:** Version 2 states that count in prose and table form and points
to B.QG.01 and B.ACTION.01 without promoting them.

### 6. Measurement language

**Requirement:** Measurement must not be granted a special ontological role.

**Resolution:** The worldsheet is described as an ordinary physical quantum
system, and detection as another physical interaction. The bridge concerns
quantum consistency, not an observer completing reality.

## Visual and build audit

- `pdflatex` completed through stable cross-references without undefined
  citations, warnings, or overfull boxes.
- All eight pages of `main.pdf` were rendered with Poppler and visually
  inspected.
- The title, abstract, revision note, tables, equations, source diagram,
  contents, references, and page transitions are legible and unclipped.

## Frontier after revision

The final moderate paper-level upgrade is resolved. The paper is now a
standalone explanatory account with a clear theorem-ownership boundary.

The physical frontier is unchanged. B.QG.01 and B.ACTION.01 remain open, and
the next progress must construct a missing source object or improve a
controlled comparison certificate rather than restate the bridge.
