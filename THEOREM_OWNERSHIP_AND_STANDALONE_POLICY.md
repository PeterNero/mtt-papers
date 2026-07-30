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
