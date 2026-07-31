# Revision Audit: Admissible Image Geometry for Network Motifs

## Identity

- Paper ID:
  `projection-induced-network-geometry-sprouting-hidden-co-6919523e`
- Superseded release: Version 1,
  DOI `10.5281/zenodo.18274629`
- Selected revision: Version 2, July 2026
- Controlling current authority: `A10`
- Current Kernel disposition before revision:
  `REVISE / RECLASSIFY`, moderate

## Why Version 1 required correction

Version 1 repeatedly used the following implication:

```text
no global reconstruction or section
    -> proper nonfactorizing motif image
    -> hidden correlations
    -> graph geometry
    -> universal sprouting
```

The first arrow is false without additional hypotheses. A surjective
covering map can lack a continuous section while its image is the entire
target product. The later arrows also conflate support constraints,
probability laws, physical graph edges, and statistical dependence graphs.

The claimed square-root threshold had a legitimate mathematical core, but
only after a positive quadratic local reserve model is supplied. Projection
alone does not select the quadratic order, its coefficients, its physical
coordinates, a branch-creation process, or an ensemble law.

## Version 2 replacement

Version 2 introduces the typed chain

```text
source domain A
    -> effective projection P
    -> network extraction Gamma
    -> motif map m
    -> image R = (m o Gamma o P)(A).
```

It then:

1. proves by a covering-map counterexample that no-section does not
   determine image geometry;
2. defines support and probabilistic factorization separately;
3. gives a failed-recombination certificate for support
   nonfactorization;
4. gives graph-of-a-map and regular-value local image tests;
5. proves that common support need not determine correlation;
6. separates physical graph edges from conditional-dependence graphs;
7. derives the visible quadratic form by Schur complement only under a
   declared positive full Hessian;
8. proves the square-root, bend, and angle bounds for the explicit
   anisotropic quadratic reserve;
9. gives a relative-remainder robustness theorem;
10. proves that a leading order `p` produces exponent `1/p`, so the
    square-root exponent is not universal;
11. proves that a feasible support alone allows any sprout prevalence;
12. states a training/held-out empirical test contract.

## Claim decisions

| Version 1 claim | Decision | Version 2 replacement |
|---|---|---|
| No reconstruction forces hidden constraints | Withdraw | Compute `R` and use a direct image test |
| Network observables cannot be freely recombined | Conditional | Failed-recombination certificate |
| Correlations generate graph geometry | Withdraw | Graph extraction and dependence are separate maps |
| Sprouts are the only boundary deformation | Narrow | High-reserve-fraction theorem in one quadratic chart |
| `rho_th ~ sqrt(C)` is universal | Withdraw as universal | Exact for a nondegenerate quadratic branch cost |
| Boundary ensembles are sprout dominated | Withdraw without a law | Requires a selected measure or growth dynamics |
| Curvature/crowding/taper are capacity proxies | Open | Require independent calibration |
| Optimization or string theory is unnecessary | Withdraw as general | Alternative mechanisms require explicit comparison maps |

## External source check

The revision was checked against standard or primary sources for:

- network motifs, DOI `10.1126/science.298.5594.824`;
- damage and load fluctuations in transport networks,
  DOI `10.1103/PhysRevLett.104.048704`;
- fluctuations and redundancy,
  DOI `10.1103/PhysRevLett.104.048703`;
- growth and adaptive network optimization,
  DOI `10.1103/PhysRevLett.117.138301`;
- graphical models, measurable selection, smooth regular-value
  geometry, and Schur-complement matrix analysis.

These references provide context and standard mathematics. They do not
promote the MTT network model to a selected physical result.

## Current frontier after the mathematical rewrite

Closed inside this paper:

- typed image geometry;
- no-section counterexample;
- support nonfactorization tests;
- distinction between motif support, physical graph, and statistical
  graph;
- exact quadratic reserve theorem;
- controlled relative-error version;
- order-of-contact scaling law;
- no-prevalence-from-support theorem.

Still open:

- selected MTT physical network source;
- selected projection and extraction map for a concrete system;
- same-source Hessian coefficients;
- calibrated reserve proxy;
- branch-creation or ensemble law;
- held-out cross-domain validation.

## Release verification

- Final PDF: 14 pages; all pages visually inspected, with the image and
  revision ledgers checked at full size.
- Local PDF SHA-256:
  `4f93cdbf38b0f29d04b0c490d6799444eceb2581e9faf122034e1c12bb23575f`.
- Published successor DOI: `10.5281/zenodo.21714026`.
- Concept DOI: `10.5281/zenodo.18274628`.
- Remote file: exactly one `main.pdf`, 356708 bytes, MD5
  `be27de246dce5da5eadef34919c18a48`.
- Zenodo metadata: version `v2`, plain-text present-paper abstract, nine
  explicit references, and two related identifiers.
- Theorem ownership, interpretive-book, expository, local release, and
  repository-wide verification gates passed before publication.
- Publication-ledger reconciliation completed against Zenodo record
  `21714026`.
- Kernel refresh and cross-repository release verification are recorded in
  the durable research handoff for this revision.
