# MTT Theorem Ownership and Standalone-Paper Policy

Date: 2026-07-28

## Rule

Every formal result has one canonical paper. A second paper may restate the
hypotheses, conclusion, and role of that result for standalone readability,
but it must identify the owner and must not reproduce the same formal
theorem/proof block.

Standalone therefore means:

- all local notation and assumptions needed to understand the argument are
  present;
- imported results are stated clearly enough to follow the dependency chain;
- the canonical source is cited; and
- genuinely paper-specific deductions remain formal results in that paper.

Standalone does not mean that the same proof is published repeatedly.

## Current Canonical Owners

| Result family | Canonical owner | Treatment elsewhere |
|---|---|---|
| Projection descent, recovery, finite-diameter obstruction, reduced kernel | *The Projection--Admissibility Principle* | Imported contracts in Program A0 and Foundation |
| Chart gluing, encoding regularity, conditional finite propagation, physical bridge | *Coherent Kinematics in Modal Triplet Theory* | Imported contracts in Program A1 |
| Generic projected existence, equilibrium promotion, Banach uniqueness, compact/noncompact fixed-point gates | Fixed Points I | Application corollaries in FP II; imported contracts in Foundation and FP VI |
| Ten-dimensional joint projector and coherent-sector application | Fixed Points II | Summarized in FP VI |
| Scalar deterministic/stochastic disturbance and scalar OU baseline | Fixed Points III | Imported baseline in FP V and FP VI |
| Supplied radial finite-mode coercivity/recurrence, cubic heat-trace and phase-channel calculation | Finite-Mode Closure Dynamics | Downstream application of FP III; no reverse import into the foundational series |
| Curved cluster, leakage, and intrinsic centroid modulation | Fixed Points IV | Summarized in FP VI |
| Vector/nonnormal covariance, correlation, and admissibility exit | Fixed Points V | Summarized in FP VI |
| Instantaneous bilocal obstruction and local-mediator completion | Fixed Points VI | Not duplicated |
| Shared-line/Hessian, Foundation-specific reduction and robustness spine | *Modal Triplet Theory: Foundations* | Interpreted, not reproved, in the Book |
| Three-time LGI bound and conditional no-retro-signaling | Temporal Bell paper | Not promoted to general MTT projection theorems |

## Narrative Papers

*The Book on Modal Triplet Theory* owns no formal theorem. It is the
low-mathematics interpretive map of the corpus and must cite the focused
source for every proved result. Zero theorem environments are necessary but
not sufficient: the Book must remain intuition-first, avoid reproducing
technical ledgers or derivations in its main narrative, and use short
technical boundaries only where the interpretation could otherwise outrun
the owning papers.

The Temporal Bell paper owns only its LGI theorem and conditional
no-retro-signaling proposition. Its projection comparison is a nonselection
check, its qubit calculation is an imported benchmark, and its MTT bridge is a
completion contract.

## Fixed-Point Series

Each fixed-point paper is independently readable and has a distinct role:

1. FP I: generic functional-analytic fixed-point machinery.
2. FP II: ten-dimensional projected-control specialization.
3. FP III: disturbance/damping and scalar stochastic baseline.
4. FP IV: curvature, leakage, and modulation.
5. FP V: multi-structure covariance and admissibility exits.
6. FP VI: synthesis, interpretation boundaries, and two new causality results.

Later papers may summarize earlier results but do not become alternate theorem
sources.

### Foundational dependency direction (2026-09-12)

The general standalone/import policy above is deliberately stricter for this
series. FP n may depend only on results established locally, earlier numbered
FP installments, and standard external mathematical literature. "Earlier"
means the installment number, not an earlier edition of a downstream paper.
All needed notation and the hypotheses of earlier-FP imports must be stated
locally. Cite an explicit edition and the relevant result where possible.

Other MTT papers, research repositories, packets and numerical results are
consumers of the FP foundation, never its proof authorities. Place their
applications, realization contracts and changing progress counts in their
own papers or the Kernel, not in the six foundational manuscripts. This also
avoids a bibliographic two-way dependency disguised as an optional example.
Keep generic examples and scope limits in the FP papers themselves.

A correction learned from later work may still repair an FP argument. Supply
its local derivation or an appropriate standard mathematical citation; do not
make the correction depend on the later MTT source. Historical revision notes
record what changed and are not mathematical premises. Do not erase valid
analytic corrections to recover the intended dependency order.

Run `python scripts/verify_fp_foundational_dependencies.py`. Its reviewed
citation allowlist rejects later-FP and non-FP MTT sources and reports the
per-paper dependency graph. It is a regression guard, not a semantic proof
checker; contextual review of uncited assumptions remains mandatory.

## Repository Enforcement

Run:

```powershell
python scripts/verify_theorem_ownership.py
```

The verifier checks the ownership-sensitive papers, expected formal-result
counts and labels, prohibited duplicate theorem titles, and exact duplicate
formal bodies across every paper currently marked reviewed or
reference-ready for release.

The full-corpus diagnostic also reports exact duplicates outside that release
scope. At the date of this policy, the remaining exact duplicate-body set is
confined to two unreleased QFT/QG manuscripts:

- *Modal Triplet Theory: From MTT to a UV-Finite Unitary Quantum Field
  Theory...*
- *Modal Triplet Theory: Perturbative Coherent-Sector Quantum...*

The focused perturbative coherent-sector paper is the intended owner. The
broader manuscript is not release-ready until its copied theorem blocks are
converted to attributed synthesis. This known nonrelease blocker is not
silently accepted as theorem ownership.
