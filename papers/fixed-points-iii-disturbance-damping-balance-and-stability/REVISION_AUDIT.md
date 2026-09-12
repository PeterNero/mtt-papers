# Fixed Points III v5 Release Audit

## v5 publication delta (July 2026)

- **Supersedes:** v4.
- **Reason:** deterministic force, stochastic power, invariant laws, and
  homogenized noise needed a clearer explanatory separation.
- **Resolution:** add a guided argument map without changing the estimates or
  their domains.
- **Retained:** every v4 theorem and correction.
- **Remaining:** coherent noise, general nonlinear invariant laws, and a
  physical stochastic source.

## Source lineage

- Source: `_work/Fixed_Points_III__Disturbance___Damping_Balance_and_Stability_v3`
- Revised: `revised_tex_vnext/Fixed_Points_III__Disturbance___Damping_Balance_and_Stability_v4`
- The v3 project remains untouched.

## Required corrections evaluated

| Finding | v3 evaluation | v4 action |
|---|---|---|
| Use a joint modal multi-index | Required; `(n,k)` separately counted overlapping structures | Uses the joint eigenindex `alpha`, all three eigenvalues, and multiplicity data |
| Use the unabsorbed equation and a one-sided remainder bound | Partly repaired in v3 | Uses `d_alpha` in the equation and defines `gamma_alpha=d_alpha-L_alpha` only in the one-sided energy estimate |
| Separate stochastic power from deterministic force amplitude | Not resolved | Introduces `q_alpha` and `f_alpha` with different units and different floors |
| Use `q/(2 gamma)` versus `f/gamma` | Not resolved | Proves separate stochastic second-moment and deterministic input-to-state theorems |
| Restrict "iff gamma>0" | Violated for general nonlinear/forced modes | Restricts it to exact scalar OU and robust worst-case deterministic stability |
| Do not call a nonlinear invariant law Gaussian | Violated by the "neglecting R or smallness" bridge | Gaussian law appears only in the exact linear Brownian OU theorem |
| State bundlewise stability for `Q Psi` | Incompletely scoped | Every bundlewise theorem is explicitly a noncoherent-sector theorem |
| Use stochastic trace or deterministic weighted series | Conflated in one `Sigma` | Defines separate `Sigma_q` and `Sigma_f`; correlated noise uses a weighted covariance trace |
| Correct fast-slow scaling so `bar g` appears | Inconsistent: `bar g` was absent from the scaled equation but present in the limit | Inserts `bar g` in the slow equation before taking the limit |
| Correct Green--Kubo normalization | v3 had an extra factor two | Uses `D=int_0^infty (R+R*) ds` |
| Add FCLT, tightness, and rough-path assumptions | Missing | Adds a uniform enhanced invariance principle, iterated-integral convergence, area-anomaly guard, and infinite-dimensional caveat |
| Distinguish deterministic fixed points from stochastic invariant measures | Partly stated | Gives separate deterministic-map and Markov-semigroup existence requirements |

## Additional corrections

- The joint Sobolev norm uses the joint spectral weight and does not sum the
  same physical mode once per vertical structure.
- Nonlinear bundlewise stochastic bounds are labelled sufficient; necessity is
  retained only for the independent exact OU product.
- Coherent forcing is explicitly outside the `Q`-sector trace theorem.
- The Weyl-law exponent is tied to the joint counting function and damping
  growth, not copied from a single-fiber estimate.
- A nonzero rough-path area anomaly is stated to generate an additional bracket
  drift rather than being silently identified with canonical Stratonovich
  noise.

## Resulting scope

FP III v4 proves deterministic input-to-state and stochastic second-moment
bounds for joint noncoherent modes under explicit one-sided damping. Exact
Gaussian invariant-law statements are confined to linear OU dynamics.
Homogenized stochastic coherent dynamics remain conditional on an enhanced
invariance principle; mixing alone is insufficient.

## Expository revision

The current paper now begins with a paper-specific reading guide. It explains
the disturbance--damping margin mode by mode, distinguishes deterministic
amplitude from stochastic power in plain language, and maps the route from
joint spectral data through modewise bounds, bundlewise summability, and
conditional homogenization. Additional discussion interprets the two
disturbance floors and explains why a rough-path limit needs more than ordinary
mixing. The conclusion now separates the robust result from the still-open
coherent-noise and physical-source questions. No theorem from another Fixed
Points paper is restated as new work.

## Validation

- FP I, FP II, and FP III permanent theorem audits all pass.
- The migration and verifier scripts pass Python syntax validation.
- TeX environment nesting passes.
- The current source compiles with `pdflatex` to a 9-page PDF.
- The final log has no undefined references, underfull boxes, overfull boxes,
  or LaTeX/package warnings.

## Corpus coherence reconciliation, 2026-08-02

The selected TeX now states the paper-specific `C.FP.01` boundary explicitly:
the damping generator, coherent projector, invariant domain, gap data, and
forcing/noise law are physical q79 inputs, not outputs of the abstract FP III
estimates. This is a scope clarification and does not change any theorem.
# Version 7: Finite-Mode Companion Bridge

September 2026. Supersedes authoring v6, not the unchanged released v5.
The scalar deterministic/stochastic bounds and conditional homogenization
theorems are retained without proof changes. A new explanatory paragraph
cites the standalone finite-mode calculation companion and distinguishes
its exact recurrence and certified transition from a mixing/Brownian limit.
No numerical proof blocks are duplicated here. The four curated calculation
results now belong to the companion rather than being counted as unexplained
additions to FP III. Abstract content and released Zenodo metadata are retained.
