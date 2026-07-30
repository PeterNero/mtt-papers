# Revision Audit: Deterministic Microdynamics and the Superdeterminism Boundary

## Release Decision

- Current source: Version 3, July 2026.
- Supersedes: Version 2, January 2026.
- Review class: conditional-kernel correction, Markov-closure correction, Bell-boundary repair, and coupled-stabilization completion.
- Intended tier: exact descent, conditional-law, finite counterexample, and coupled-contraction results; imported deterministic homogenization; conditional MTT and Bell source promotion.
- Not a universal stochasticity, Born-rule, one-history, or superdeterminism no-go theorem.

## Defects Corrected

1. Version 2 treated a Dirac conditional kernel as equivalent to constancy at every point of every projection fiber.
2. It described noninjective projection as generating stochasticity, although a preparation or invariant measure is required.
3. It promoted a one-step conditional law to a Markov process without proving history independence or time homogeneity.
4. Its Gaussian OU forcing was an assumed stochastic source, not a derivation from deterministic microdynamics.
5. Its selection-potential tail claim omitted process-level Gaussian concentration hypotheses needed for slab-exit control.
6. It called structured stochasticity “non-random” and a third logical category, which is not standard probability terminology.
7. Its cascading-stabilization corollary had no coupled map, influence bounds, or contraction estimate.
8. It let stabilization stand in for outcome completion.
9. It characterized superdeterminism as conspiracy rather than testing measurement independence in a specified joint law.
10. It did not distinguish Bell factorization, operational no-signaling, base locality, and measurement independence.

## Exact Results Owned by Version 3

### Global fiber-factorization criterion

For complete evolution `Phi` and retained map `P`, a reduced map `F` satisfying

```text
P o Phi = F o P
```

exists exactly when `P o Phi` is constant on every fiber of `P`.

### Almost-sure deterministic descent

On standard Borel spaces with preparation `mu`, the following are equivalent:

1. the next reduced state is a measurable function of the current reduced state almost surely;
2. it is measurable with respect to the current reduced sigma-algebra;
3. its regular conditional law given the current reduced state is Dirac almost everywhere.

This is weaker than global fiber constancy because conditional null sets are ignored.

### Preparation-dependence counterexample

One fixed projection and one fixed deterministic microscopic map admit two preparations with the same current reduced marginal but opposite deterministic next-state kernels. Projection and microdynamics therefore do not select the conditional law.

### Non-Markov projection counterexample

The invertible four-cycle with observed word

```text
0, 0, 1, 1, ...
```

under its invariant uniform preparation is stationary but not first-order Markov. The current observed value leaves hidden phase information in the history.

### Coupled-basin contraction theorem

If component distances obey a nonnegative influence matrix `L` with spectral radius below one, a weighted maximum metric makes the coupled basin map a strict contraction. The declared basin has one fixed record and all basin orbits converge geometrically.

This theorem begins after basin entry. It does not select an outcome basin.

## Imported Deterministic Limit

The companion deterministic-projection paper supplies a smooth invertible toral skew-product source with a selected initial ensemble, exact Green-Kubo variance `1/2`, and a rigorously controlled diffusion limit under an imported deterministic-homogenization theorem.

The general homogenization input is not owned here. The primary current reference is:

- Chevyrev, Friz, Korepanov, Melbourne, and Zhang, *Deterministic Homogenization under Optimal Moment Assumptions for Fast-Slow Systems. Part 2*, Annales de l'Institut Henri Poincare B 58 (2022), DOI `10.1214/21-AIHP1203`.

## Correct Bell Boundary

The revised paper distinguishes:

```text
measurement independence:
  P(dlambda | a,b) = P(dlambda)

Bell factorization:
  P(r,s | a,b,lambda)
    = P(r | a,lambda) P(s | b,lambda)

operational no-signaling:
  local outcome marginals do not depend on remote settings.
```

Determinism alone implies none of these statistical relations.

The corrected MTT Bell package is:

```text
preparation-selected nonseparable state independent of later settings
  + base-local descent
  + local completely positive instruments.
```

It can violate Bell factorization while preserving measurement independence and operational no-signaling. It is not a Bell-local hidden-variable completion. Selected MTT state, probability, and instrument sources remain open.

Primary Bell references checked:

- Bell, *On the Einstein Podolsky Rosen Paradox*, 1964, DOI `10.1103/PhysicsPhysiqueFizika.1.195`.
- Hall, *Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence*, 2010, DOI `10.1103/PhysRevLett.105.250404`.

## MTT Completion Obligations

1. Select the complete physical carrier and evolution.
2. Select the retained algebra or projection.
3. Derive the preparation or invariant state before evaluating projected probabilities.
4. Test exact, almost-sure, and approximate fiber factorization.
5. Prove a sufficient-state, memory-kernel, or homogenization theorem.
6. Derive its coefficients and approximation error from the same source.
7. Derive the outcome-resolved apparatus instrument.
8. Prove coupled basin-local stabilization after completion.
9. Verify measurement independence, base locality, local instruments, and no-signaling separately in Bell protocols.

## Claims Explicitly Not Made

- Projection alone does not create probability.
- Failure of deterministic descent does not by itself produce a stochastic law.
- A one-step conditional kernel is not automatically Markov.
- Structured probability is still probability, not a third logical category.
- An assumed OU forcing is not a deterministic-source theorem.
- Basin contraction does not select a basin.
- Determinism is not synonymous with superdeterminism.
- Upper/base locality is not Bell factorization.
- The conditional MTT Bell package is not yet selected from one physical source.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 3 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- The old malformed Unicode quotation text and bloated stale self-reference list were removed.
- LaTeX compiles without unresolved references, overfull boxes, or underfull boxes.
- All eight PDF pages were visually inspected after the final compile; no clipping, overlap, broken tables, or unreadable equations were found.
