# Coherent Green Functions v1 Revision Audit

## September 2026 Current-Version Delta (v2)

- Supersedes: v1; no Zenodo record changed.
- Reason: Correct boundary-domain and Sobolev-norm claims for Green responses.
- Resolution: Repairs both convergence theorems and distinguishes spectral from geometric Sobolev norms.
- Ownership: Own the Green-response specialization while importing the common sharp-limit result.
- Retained: valid scoped results and examples, without physical promotion.
- Remaining: future source integration and author release approval.


## Current version delta

Version 1 retains the finite spectral and heat-filtered elliptic Green
operators, their smooth kernels, finite diagonal values in the stated compact
setting, and their sharp distributional limits. It withdraws the inference
that these standard theorems select one physical MTT source kernel.

The revision:

- retitles the paper around declared projection kernels rather than universal
  point-source replacement;
- distinguishes a retained-sector identity from the full identity;
- states that the operator, projector or filter, width, boundary conditions,
  and MTT-to-source intertwiner are realization inputs until derived;
- makes covariance, gauge/BRST, locality, causal support, and wavefront-set
  compatibility explicit gates;
- confines the proved core to compact elliptic or Euclidean problems; and
- reclassifies contact, retarded, and renormalization applications as
  conditional models.

## Retained result

For a supplied positive self-adjoint elliptic operator, finite spectral and
heat-filtered Green operators are smooth finite-source responses and converge
distributionally to the ordinary Green kernel in the appropriate sharp
limit.

## Remaining boundary

The paper does not select the finite source or its width from MTT geometry,
derive a Lorentzian retarded kernel, or prove gauge and interacting
consistency.

## Validation

The paper must compile cleanly, pass repository release verification, and
receive a complete PDF visual review before publication.
