# Revision Audit: ETH and MBL Operational Bridge v2

## Scope

This audit records the replacement of the released v1 source by the
model-dependent v2 operational bridge. The correction authority is A10,
`MTT_Master_Corrigendum_and_Revision_Plan.md`, SHA-256
`78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.

## Disposition

The common-basin picture is retained only as an operational vocabulary
after the Hamiltonian, state class, observable family, map, metric, time
window, and uncertainty record have been declared.

| v1 claim | v2 resolution | Status |
|---|---|---|
| ETH is equivalent to a dominant contractive basin. | Uniform effective contraction is proved sufficient for observable convergence, but not necessary for ETH. | Universal equivalence withdrawn. |
| MBL is equivalent to exponentially many fragmented basins. | A quasi-LIOM commutator bound gives a quantitative finite-time memory criterion; integrability and symmetries show why memory alone is not equivalent to MBL. | Universal equivalence withdrawn. |
| Coarse evolve-project maps form reduced dynamics with a mixing rate. | The exact semigroup defect is derived. Markovianity requires the defect to vanish or be controlled. | Corrected by Theorem 4.1. |
| Unitary dynamics can contract an operational basin. | Microscopic unitary evolution is proved to preserve trace distance. Strict contraction belongs to the coarse channel. | Corrected by Proposition 4.3. |
| The ETH-MBL crossover has a Kramers/logistic knee. | Closed unitary dynamics supplies no stochastic barrier law. Finite data admit infinitely many smooth interpolants; a scaling model and held-out test are required. | Universal knee withdrawn. |
| ETH, MBL, and monitored transitions are the same mechanism. | They may share diagnostic vocabulary but have different state spaces, generators, ensembles, and limiting procedures. | Reclassified as an open typed comparison. |
| MTT's projector gap directly controls the many-body regime. | Hessian, Hamiltonian level-spacing, channel, and mobility gaps are distinguished. A source-and-intertwiner theorem is required. | Reclassified as an open MTT pullback. |

## New rigorous content

1. A complete finite random-field XXZ Hamiltonian and comparison capsule.
2. The exact reduced-semigroup defect formula.
3. Unitary trace-distance isometry and a sufficient contraction theorem.
4. The exact diagonal-bias plus temporal-fluctuation decomposition.
5. A quantitative quasi-LIOM memory bound.
6. A finite-data nonuniqueness theorem for crossover curves.
7. A typed conditional MTT diagnostic-transport theorem.
8. A finite-size, numerical, statistical, and held-out validation protocol.

## Claim tier

The paper is a finite-dimensional operational bridge. It does not prove
ETH or MBL for the XXZ family, a thermodynamic phase boundary, a universal
crossover law, or a selected MTT source for the many-body record.

## Verification obligations

- Build `main.tex` with BibTeX and inspect every rendered page.
- Run the expository readability, theorem ownership, book-role, release,
  and repository verifiers.
- Freeze the reviewed TeX, PDF, source-tree, and revision-audit hashes.
- Upload exactly one checksum-matching PDF to a Zenodo v2 record.
- Reconcile the release into the paper catalog and Kernel.
