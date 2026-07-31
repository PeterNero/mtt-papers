# Revision Audit: Coherence-Capacity Cosmology v3

## Scope

This audit records the replacement of the released v2 source by the
covariant v3 effective-model paper. The correction authority is A10,
`MTT_Master_Corrigendum_and_Revision_Plan.md`, SHA-256
`78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.

## Disposition

The original cosmological interpretation is retained only as a candidate
interpretation of a declared effective scalar. Claims that expansion,
acceleration, horizons, nonsingularity, or a time arrow follow from
capacity positivity or exhaustion are withdrawn.

| v2 claim | v3 resolution | Status |
|---|---|---|
| Spare capacity forces spatial expansion. | Capacity positivity is kinematically independent of the metric. Expansion is decided by a covariant action and initial data. | Withdrawn and replaced by Proposition 4.3. |
| Isotropy and dimensions imply `H^2 = rho_eff / C`. | A Jordan-frame scalar-tensor action is declared and varied. Its exact Friedmann equations include kinetic, potential, and Planck-mass-running terms. | Replaced by Theorem 3.1 and equations (4.1)-(4.4). |
| Capacity redistribution implies acceleration. | The exact necessary-and-sufficient acceleration inequality is derived. Redistribution alone does not fix its sign. | Replaced by Theorem 4.1. |
| Finite transport inevitably creates a cosmological horizon at `C=0`. | Causal horizons are defined from Lorentzian causal structure. Capacity zero is proved neither necessary nor sufficient. | Replaced by Proposition 7.1. |
| Positive early capacity removes the initial singularity. | A positive-capacity dust FLRW counterexample retains divergent curvature. Completeness requires a separate spacetime theorem. | Replaced by Proposition 7.2. |
| Capacity exhaustion selects the cosmic arrow. | The covariant action is reversible. An arrow requires a state, boundary condition, entropy current, or irreversible generator. | Reclassified as conditional. |
| The framework removes the need for dark energy, inflation, and an initial singularity. | The action contains LambdaCDM as a nested limit. Nontrivial alternatives require selected functions, complete solutions, and data comparison. | Withdrawn. |
| Cosmological observations were predicted. | Background observables, perturbation obligations, likelihood inputs, parameter accounting, and falsifiers are now explicit. No fit is claimed. | Reclassified as an open comparison contract. |

## New rigorous content

1. A covariant scalar-tensor effective action and its metric and scalar
   Euler-Lagrange equations.
2. The exact spatially flat FLRW reduction.
3. A necessary-and-sufficient acceleration criterion.
4. A background reconstruction-degeneracy theorem showing why freely
   chosen coupling functions can replay expansion data without predicting
   them.
5. A precise LambdaCDM nested limit.
6. Counterexamples separating capacity level sets from causal horizons
   and capacity positivity from past completeness.
7. A reproducible observational comparison contract and explicit
   falsification conditions.

## Claim tier

The paper is a conditional covariant effective realization. It does not
derive the source map or coupling functions from selected MTT geometry,
does not fit cosmological data, and does not establish a new cosmological
model as observationally viable.

## Verification obligations

- Build `main.tex` with BibTeX and inspect every rendered page.
- Run the expository readability, theorem ownership, book-role, release,
  and repository verifiers.
- Freeze the reviewed TeX, PDF, source-tree, and revision-audit hashes.
- Upload exactly one checksum-matching PDF to a Zenodo v3 record.
- Reconcile the release into the paper catalog and Kernel.
