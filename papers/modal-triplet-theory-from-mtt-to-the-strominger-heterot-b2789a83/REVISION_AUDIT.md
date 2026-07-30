# Revision Audit: MTT and the Hull-Strominger System

## Current revision

- Version: v2
- Date: July 2026
- Supersedes: v1.0, DOI 10.5281/zenodo.17071767
- Disposition: conditional fixed-point correspondence; selection claim withdrawn

## Reason

Version 1 claimed that a Green-Schwarz-corrected functional selected a unique
Hull-Strominger compactification and that the selected MTT fixed point was its
globally attractive minimizer. That chain does not satisfy its analytic or
geometric proof obligations.

The decisive defects are:

1. For a three-form \(H\), the proposed operator
   \(d_H=d+H\wedge\) satisfies \(d_H^2=(dH)\wedge\). It is therefore not a
   twisted cochain differential on a generic heterotic anomaly background
   with \(dH\ne0\).
2. Parabolic smoothing and a spectral gap do not by themselves produce a
   verified contraction constant below one on an invariant complete basin.
3. The former constrained functional contains indefinite curvature and
   multiplier terms. Boundedness below, lower semicontinuity, and strict
   Hessian positivity were not established.
4. First-order supersymmetry equations are not automatically the
   Euler-Lagrange equations of that functional.
5. Fu-Yau geometry, Iwasawa calculations, finite q79 data, and rank-two HYM
   results were not assembled on one common physical rank-three carrier.

## Resolution

Version 2 removes the selection potential and replaces it with a typed bridge
between an upper MTT flow and a lower Hull-Strominger flow. It proves:

1. exact fixed-point descent under a commuting flow diagram;
2. a quantitative lower residual bound under a bounded generator defect; and
3. a separate contraction-basin criterion for any future uniqueness claim.

The lower dynamics is anchored to the established Anomaly flow, with bundle
flows or fixed HYM data included as separate hypotheses. The paper explicitly
distinguishes descent, lifting, local uniqueness, and physical selection.

## Retained content

- The Hull-Strominger equations and their one-carrier assembly requirement.
- Conformally balanced geometry, HYM connections, torsion, and the
  Green-Schwarz differential identity as distinct typed rows.
- Fixed-point methods as a possible MTT-to-heterotic bridge.
- Fu-Yau geometry and the Anomaly flow as the strongest established lower
  target for the q79 program.
- The exact finite q79, rank-three topological, rank-two Cech, finite-HYM, and
  Wiener-contraction results at their declared tiers.

## Current evidence incorporated

- A07: literal finite rank-two Cech witness.
- A11: exact q79 arithmetic theorem and audit.
- A15: certified finite rank-two HYM approximation.
- A19: rank-two Wiener-contraction existence and local-uniqueness theorem.
- The audited heterotic-flux companion paper, v4, DOI
  10.5281/zenodo.21705964.
- B.HS.01: the physical visible-hidden Hull-Strominger endpoint remains open.
- B.GEO.01: the connection-preserving continuum intertwiner remains open.

## Remaining boundary

The selected q79 branch still needs one common physical tuple: a global
Fu-Yau complex threefold, stable rank-three visible bundle with the required
index, compatible hidden and tangent instantons, the differential
Green-Schwarz identity, global gerbe data, and a connection-preserving MTT
flow intertwiner. Exact descent becomes applicable only after those hypotheses
are constructed on the same source.
