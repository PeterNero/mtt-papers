# Revision Audit

## Supersedes

`Fermions in Loop Quantum Gravity from Modal Triplet Theory: Coherent
Compression, Berry Terms, and Absence of Doubling`, version 1.0.

## Reason

The first edition's finite-element norm-resolvent estimate was not proved.
Its own bounds produced an order-one term where order `h` was claimed, and a
finite-rank projector cannot converge to the identity in operator norm on an
infinite-dimensional Hilbert space. The paper also treated compression as a
general resolution of Nielsen--Ninomiya and introduced Berry transport
without first constructing a smooth gapped projector bundle.

## Resolution

Version 2:

- distinguishes a sharp projector, smooth filter, and finite-element/graph
  projector;
- proves exact spectrum preservation for sharp spectral compression;
- proves exact chiral-index inheritance for a symmetric graded window;
- proves unitary inheritance for a graph presentation while identifying its
  generic nonlocality;
- states explicitly which Nielsen--Ninomiya hypotheses are not retained;
- withdraws the defective norm-resolvent proof;
- replaces edge-logarithm assertions by the exact Kato--Berry connection on a
  supplied smooth constant-rank projector bundle; and
- lists the continuum Dirac source and geometric graph map still required
  from MTT.

## Retained Result

A finite, continuum-derived spectral window can be represented on graph data
without introducing spurious low-energy eigenvalues, and it preserves the
chiral index exactly under the stated grading hypotheses.

## Remaining Boundary

MTT must still select the four-dimensional fermion bundle, continuum Dirac
operator, chirality and gauge data, finite-operation type, and graph map.
Graph locality, refinement convergence, anomaly control, dynamics, and the
physical LQG fermion Hilbert space remain open.

## Evidence

- `main.tex`
- `main.pdf`
- `The Proto-Spinor: Conditional Spinorial Closure and the Current Operator
  Frontier`
- `Modal Triplet Theory and Loop Quantum Gravity: A Conditional
  Holst/Canonical Embedding`
- Current q79 and Standard-Model carrier results
