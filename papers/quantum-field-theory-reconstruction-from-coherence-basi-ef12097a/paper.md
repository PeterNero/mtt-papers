---
abstract: |
  We show how quantum field theory arises as an effective statistical representation of coherence basin ensembles, under the same admissibility, regularity, and coarse-graining assumptions used elsewhere in the coherence-capacity framework. We show that quantum fields arise as collective variables encoding statistics of localized coherence basins, while quantum states correspond to ensemble distributions over admissible basins. Correlation functions, operators, and Hilbert-space structure emerge as bookkeeping devices for basin statistics, rather than fundamental ontological entities. This reconstruction explains the origin of operator algebras, superposition, and probabilistic measurement without postulating fundamental wave functions or fields.
author:
- Peter Nero
current_version: v2
date: January 2026
generated_from_main_tex_sha256: dd5d9aab4b0197e1f124b67fb7889c07c395820c54ac3dc92993bfb2bd1b4e4a
paper_id: quantum-field-theory-reconstruction-from-coherence-basi-ef12097a
release_state: zenodo_released
released_version: v2.0
title: |
  **Quantum Field Theory Reconstruction  
  from Coherence Basin Statistics**
zenodo_doi: 10.5281/zenodo.18322089
zenodo_record_id: 18322089
zenodo_url: "https://zenodo.org/records/18322089"
---

# Introduction

Quantum field theory (QFT) is the most successful predictive framework in physics, yet its conceptual foundations remain unsettled. Fields are treated as fundamental objects, operators act on abstract Hilbert spaces, and infinities are handled by renormalization procedures whose physical interpretation is often opaque.

In the preceding papers we showed that particles and forces arise from stable coherence basins and coherence-capacity transport. In this work we take the next step: we show that quantum field theory itself emerges as a *statistical effective theory of coherence basin ensembles*.

The central claim is:

> *Quantum fields do not describe fundamental physical substances; they encode statistical correlations among large ensembles of coherence basins.*

From this perspective, quantum superposition, operator algebras, and correlation functions are not mysterious axioms but inevitable bookkeeping tools.

#### Claim discipline.

All “reconstruction” statements in this paper are representation statements: they assert that basin-ensemble statistics admit standard QFT encodings under stated regularity and linearized assumptions. No claim is made that QFT emerges uniquely or globally outside admissible regimes.

# Framework and Assumptions

We adopt the minimal axioms used previously.

Axiom A1.  
Fundamental dynamics on a configuration space $`X`$ is invertible.

Axiom A2.  
Observable physics arises via a noninjective projection $`P:X\to Y`$.

Axiom A3.  
Effective descriptions are valid only within admissible basins characterized by positive coherence capacity.

Axiom A4.  
Coherence basins are stable, contractive regions of effective state space.

#### Scope note.

In this paper, coherence capacity is used only as an admissibility label imported from prior work; no independent capacity dynamics, transport, or flux assumptions are introduced here. No assumption of fundamental quantum fields, Hilbert spaces, or operator algebras is made.

# Coherence Basin Ensembles

## Single-basin description

A single coherence basin corresponds to what is ordinarily called a particle. Its centroid follows classical equations of motion, as shown previously.

However, experimental preparations rarely isolate a single basin. They produce ensembles of admissible basins with varying internal structure and trajectories.

## Ensembles as physical states

<div class="definition">

**Definition 1** (Basin ensemble). A basin ensemble is a normalized measure $`\mu`$ on the space of admissible coherence basins.

</div>

#### Measure-theoretic assumptions.

The basin ensemble measure $`\mu`$ is assumed to be a normalized Borel measure on the space of admissible coherence basins, equipped with the minimal $`\sigma`$-algebra required to define expectation values of basin observables. No claim is made that this space admits a canonical or unique measure; all results below are invariant under admissible reparameterizations of $`\mu`$ that preserve observable statistics.

Physically, $`\mu`$ encodes the preparation conditions of an experiment. Different microconfigurations projecting to the same effective description correspond to different points in the ensemble.

<div class="definition">

**Definition 2** (Effective state). An effective state is an equivalence class of basin ensembles yielding the same observable statistics.

</div>

<div class="lemma">

**Lemma 3** (Preservation of basin identity under ensemble statistics). *Within admissible regimes, ensemble statistics uniquely determine the identity of the underlying coherence basin up to admissible equivalence. Distinct coherence basins cannot yield identical ensemble statistics on overlapping admissible domains, except at merge–split boundaries where basin identity ceases to be well-defined.*

</div>

This replaces the notion of a fundamental wave function.

# Observables and Expectation Values

## Observables as basin functionals

An observable $`\mathcal O`$ is defined as a functional on coherence basins,
``` math
\mathcal O : B_\alpha \mapsto \mathbb R.
```

The expectation value of $`\mathcal O`$ in an ensemble $`\mu`$ is
``` math
\langle \mathcal O \rangle_\mu
= \int \mathcal O(B)\, d\mu(B).
```

This definition is purely classical at the ensemble level.

## Emergence of linearity

Linearity arises because expectation values depend linearly on $`\mu`$. Convex combinations of ensembles produce convex combinations of expectation values.

This is the origin of the linear structure of quantum states.

# Hilbert Space as Statistical Bookkeeping

## Representation theorem

We now show that ensemble statistics admit a Hilbert-space representation.

<div class="theorem">

**Theorem 4** (Hilbert representation under ensemble regularity). *There exists a Hilbert space $`\mathcal H`$ and a mapping
``` math
\mu \mapsto |\psi_\mu\rangle \in \mathcal H
```
such that expectation values can be written as
``` math
\langle \mathcal O \rangle_\mu
= \langle \psi_\mu | \hat{\mathcal O} | \psi_\mu \rangle
```
for a suitable operator $`\hat{\mathcal O}`$ associated with $`\mathcal O`$.*

</div>

<div class="proof">

*Proof.* Assume the algebra of basin observables admits a $`C^*`$-algebra completion and that the ensemble expectation $`\langle \cdot \rangle_\mu`$ defines a positive linear functional on this algebra. This follows from the Gelfand–Naimark–Segal construction applied to the commutative algebra of basin observables, extended to include noncommuting operators generated by incompatible basin partitions. ◻

</div>

Thus the Hilbert space is not fundamental; it is a representation of ensemble statistics.

# Field Operators from Basin Statistics

## Local observables

Local observables correspond to functionals of basin density in spacetime regions. Define the basin density operator
``` math
\hat{\phi}(x)
```
as the operator encoding fluctuations of basin density near $`x`$.

## Field interpretation

<div class="theorem">

**Theorem 5** (Emergent quantum fields in the linearized ensemble regime ). *Quantum fields arise as operator-valued distributions encoding correlations of basin ensembles.*

</div>

This representation holds in regimes where basin-density fluctuations admit a linearized, Gaussian description.

Field operators do not represent fundamental degrees of freedom but statistical correlations among many coherence basins.

# Superposition and Interference

Superposition arises because different basin ensembles may produce identical marginal statistics but differ in higher-order correlations. Interference reflects overlap of basin-support measures, not simultaneous existence of incompatible classical realities.

# Discussion

This reconstruction demystifies several features of quantum theory:

- Quantum states are statistical objects, not ontological waves.

- Operators encode ensemble correlations.

- Superposition reflects ensemble structure.

- Measurement collapse corresponds to capacity-induced basin selection.

Quantum field theory emerges as the optimal statistical language for describing coherence basin ensembles.

# Propagators as Basin Correlation Kernels

## Two-point correlations

In quantum field theory, propagators encode correlations between field values at different spacetime points. In the basin framework, these correlations arise naturally from statistics of basin ensembles.

Let $`\rho_B(x)`$ denote the basin density associated with a coherence basin $`B`$. For an ensemble $`\mu`$, define the two-point correlation function
``` math
G(x,y)
:= \int \rho_B(x)\,\rho_B(y)\, d\mu(B)
- \int \rho_B(x)\,d\mu(B)\int \rho_B(y)\,d\mu(B).
```

This quantity measures correlated support of coherence basins at $`x`$ and $`y`$.

<div class="theorem">

**Theorem 6** (Propagators as basin correlation kernels). *In the linearized ensemble regime, the two-point correlation function $`G(x,y)`$ admits a representation equivalent to the quantum field propagator associated with the corresponding effective field operator.*

</div>

<div class="proof">

*Proof.* In the Hilbert representation of ensemble statistics, $`G(x,y)`$ is represented by a state-dependent expectation value (e.g. vacuum in a chosen representation) of the time-ordered product of field operators. Its functional form is determined by the linearized dynamics of basin fluctuations. ◻

</div>

Thus propagators are not fundamental Green’s functions but correlation kernels encoding basin statistics.

# Path Integrals as Ensemble Generating Functionals

## Generating functionals

Consider the generating functional
``` math
Z[J] := \int \exp\!\left( i \int J(x)\,\rho_B(x)\,dx \right) d\mu(B),
```
where $`J(x)`$ is an external source.

<div class="theorem">

**Theorem 7** (Path integrals as ensemble generating functionals). *The functional $`Z[J]`$ serves as an effective generating functional for correlation functions, analogous to the quantum field theoretic path integral.*

</div>

<div class="proof">

*Proof.* The exponential weighting generates moments of basin density distributions. In the Hilbert representation, this reproduces the functional integral over field configurations weighted by the effective action, which encodes basin statistics. ◻

</div>

The path integral therefore serves as a compact encoding of ensemble statistics rather than a sum over ontological field histories.

# Renormalization as Capacity Coarse-Graining

## Scale dependence

Quantum field theories exhibit scale dependence and require renormalization. In the present framework, this arises from coarse-graining of coherence basins under limited capacity.

<div class="definition">

**Definition 8** (Capacity coarse-graining). Capacity coarse-graining is the systematic elimination of basin features that cannot be stably maintained under reduced coherence capacity at a given scale.

</div>

## Renormalization group flow

<div class="theorem">

**Theorem 9** (Renormalization from basin statistics, effective). *Renormalization group flow corresponds to evolution of effective ensemble descriptions under capacity coarse-graining.*

</div>

<div class="proof">

*Proof.* This correspondence holds at the level of effective descriptions under systematic coarse-graining of basin ensembles. As observational resolution decreases, fine basin distinctions are erased by projection. Coupling constants flow because they encode statistical properties of basin ensembles at different scales. ◻

</div>

This interpretation explains why renormalization is necessary and why physical predictions remain finite despite formal divergences.

# Perturbation Theory and Feynman Diagrams

## Perturbative expansion

Perturbation theory arises when interactions between basins are weak. Correlation functions can then be expanded in powers of interaction strength.

<div class="theorem">

**Theorem 10** (Diagrammatic expansion). *Feynman diagrams enumerate contributions to basin correlation functions under perturbative expansion of ensemble statistics.*

</div>

Vertices represent interaction-induced basin correlations; propagators represent basin correlation kernels.

This explains why diagrammatic perturbation theory is effective and why its combinatorial structure matches experimental observations.

# Breakdown of Quantum Field Theory

## Capacity exhaustion

Quantum field theory presumes that coherence capacity is sufficient to support arbitrarily fine-grained basin statistics. When capacity becomes limited, this assumption fails.

<div class="theorem">

**Theorem 11** (QFT breakdown at capacity exhaustion, effective). *Quantum field theory ceases to be valid when coherence capacity approaches zero, regardless of microscopic dynamics.*

</div>

<div class="proof">

*Proof.* At capacity exhaustion, effective projection becomes noninvertible and ensemble statistics can no longer be represented within a Hilbert-space encoding. ◻

</div>

This explains why QFT fails near singularities, horizons, and strong measurement contexts.

# Discussion

This reconstruction resolves several foundational puzzles:

- Why quantum theory is probabilistic: probabilities encode ensemble statistics.

- Why superposition exists: linearity reflects convexity of ensemble space.

- Why renormalization is necessary: finite capacity enforces coarse-graining.

- Why QFT is not fundamental: it presumes infinite capacity.

Quantum field theory is thus an effective statistical language, not a fundamental ontology.

# Conclusion

We have reconstructed quantum field theory as an emergent statistical description of coherence basin ensembles. Fields, operators, propagators, path integrals, and renormalization arise naturally from ensemble statistics under finite coherence capacity.

Together with the preceding papers, this completes a unified framework in which:

- coherence capacity functions as the fundamental admissibility resource,

- gravity is its geometric bookkeeping,

- particles and forces arise from basin dynamics,

- horizons and entropy reflect capacity bottlenecks,

- quantum field theory emerges as basin statistics.

The apparent mysteries of quantum theory thus reflect the deep structure of effective description rather than fundamental indeterminism.
