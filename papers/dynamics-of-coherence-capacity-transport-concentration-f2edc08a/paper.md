---
abstract: |
  We develop the dynamical theory of coherence capacity introduced in “Coherence Capacity as the Fundamental Resource of Effective Physics.” Coherence capacity is defined as the finite stability margin that allows a projection-based effective description to remain predictive. Under minimal axioms, we show that coherence capacity admits a local transport law and behaves as a conserved resource within admissible regimes. We prove that capacity transport generically exhibits focusing, leading to concentration, bottleneck formation, and exhaustion on codimension-one surfaces. These results provide the dynamical substrate for gravitational attraction, horizon formation, thermalization, and irreversibility, without modifying fundamental dynamics or introducing new degrees of freedom. All transport statements are effective/encoding-level, slab-local, and conditional on regularity and constitutive closure assumptions stated explicitly below.
author:
- Peter Nero
current_version: v2
date: January 2026
generated_from_main_tex_sha256: c919040c692d60f6e438afbe8a443d7fd3aa0a8740fcf110e1fc88f5fef605bc
paper_id: dynamics-of-coherence-capacity-transport-concentration-f2edc08a
release_state: zenodo_released
released_version: v2.0
title: |
  **Dynamics of Coherence Capacity:  
  Transport, Concentration, and Exhaustion**
zenodo_doi: 10.5281/zenodo.18322062
zenodo_record_id: 18322062
zenodo_url: "https://zenodo.org/records/18322062"
---

# Introduction

In the preceding work we identified coherence capacity as the structural resource governing the validity of effective physical descriptions. Exhaustion of coherence capacity forces noninvertibility of the effective evolution, producing irreversibility even when the underlying dynamics is deterministic and invertible.

The present paper extends that analysis from kinematics to dynamics. Specifically, we address the question: how does coherence capacity move, redistribute, concentrate, and fail?

We show that coherence capacity is not merely a diagnostic but a physical resource admitting local transport and conservation laws. Within admissible regimes, capacity is conserved and redistributed; under persistent strain it concentrates and forms bottlenecks where effective descriptions necessarily break down.

This transport picture provides the missing dynamical link between capacity exhaustion and familiar physical phenomena such as gravitational attraction, horizon formation, and loss of memory.

# Levels of Description

We distinguish three levels.

## Upstairs configuration space

Let $`(X,\mathcal B)`$ be a measurable configuration space equipped with an invertible evolution $`\Phi:X\to X`$ (or a flow $`\Phi_t`$). No fundamental time parameter is assumed; $`\Phi`$ defines only an ordering of configurations.

## Projection and observables

Observable physics is defined by a measurable projection
``` math
P:X\to Y,
```
where $`Y`$ is the space of effective states. The projection is generally noninjective.

## Effective shadow

The induced observable evolution is
``` math
T := P\circ \Phi : X \to Y.
```
All effective laws refer to this shadow level.

# Axioms

The results of this paper rest on the following minimal axioms.

Axiom A1 (Invertible fundamental dynamics).  
The evolution $`\Phi`$ is invertible on $`X`$.

Axiom A2 (Projection).  
The observable map $`P:X\to Y`$ is measurable and noninjective.

Axiom A3 (Admissibility).  
There exists a subset $`A\subset X`$ on which the projection-based description is stable and predictive.

Axiom A4 (Finite coherence capacity).  
Stability of the effective description on $`A`$ is controlled by a finite margin that can be exhausted under disturbance.

No assumption of fundamental stochasticity, collapse, or time asymmetry is made.

# Coherence Capacity

## Definition

<div class="definition">

**Definition 1** (Coherence capacity). For $`x\in A`$, the coherence capacity $`\mathcal C(x)`$ is the maximal disturbance amplitude such that the projection-based effective description remains stable in a neighborhood of $`x`$.

</div>

$`\mathcal C(x)>0`$ characterizes admissible regions; $`\mathcal C(x)=0`$ marks admissibility barriers.

## Basic properties

<div class="lemma">

**Lemma 2**. *$`\mathcal C(x)>0`$ for all $`x\in A`$.*

</div>

<div class="lemma">

**Lemma 3**. *If $`x_n\in A`$ converges to $`x\notin A`$, then $`\mathcal C(x_n)\to 0`$.*

</div>

These properties follow directly from the definition of admissibility.

# Capacity as a Physical Resource

We now elevate coherence capacity from a diagnostic to a physical resource.

<div class="definition">

**Definition 4** (Coherence capacity resource). Coherence capacity is a locally defined scalar resource whose preservation is necessary and sufficient for the continued validity of a projection- based effective description.

</div>

This resource can be redistributed, concentrated, and exhausted, but not created from nothing within admissible regimes.

#### Interpretive clarification.

Referring to coherence capacity as a “resource” is a descriptive choice, not an ontological claim. Coherence capacity is not a new degree of freedom, field, or conserved charge. The resource language encodes the fact that admissibility margins can be redistributed, depleted, or concentrated within an effective description, even though the underlying dynamics on $`X`$ remains invertible. All statements in this section concern the structure of effective description, not additional microscopic physics.

# Capacity Transport and Currents

## Existence of a capacity current

<div class="theorem">

**Theorem 5** (Existence of a coherence-capacity current). *Within any admissible basin, there exists a locally defined effective current $`J^\mu_{\mathcal C}`$ on $`Y`$, defined up to coarse-graining, such that
``` math
\nabla_\mu J^\mu_{\mathcal C} = 0
```
holds pointwise inside the basin. Concretely, take any admissibility margin functional $`C`$ defined on the coherent basin and consider its pushforward density under the projection map $`P`$ restricted to that basin; under the stated absolute continuity and regularity assumptions, this pushforward admits a local representation by an effective current.*

</div>

<div class="proof">

*Proof.* Inside an admissible basin the projection remains stable and the effective description is predictive. The invertibility of $`\Phi`$ ensures that admissibility-defining structure is preserved under evolution. Pushing forward this structure defines a local flow of coherence capacity on $`Y`$, yielding a divergence-free current $`J^\mu_{\mathcal C}`$. Here “current” refers to an effective representation of admissibility transport under the assumption that Y admits a smooth local chart and that the pushforward of admissibility- preserving structure is absolutely continuous. ◻

</div>

## Continuity equation

The local conservation law
``` math
\boxed{
\nabla_\mu J^\mu_{\mathcal C} = 0 \qquad (\mathcal C>0)
}
```
expresses conservation of coherence capacity within admissible regimes.

# Capacity Nonconservation at Admissibility Barriers

Conservation of coherence capacity holds only within admissible regions. At admissibility barriers, the defining inequalities of stability fail and capacity is no longer preserved.

<div class="theorem">

**Theorem 6** (Capacity exhaustion at admissibility barriers). *Let $`B\subset Y`$ be the projection of an admissibility barrier. Then the capacity current satisfies
``` math
\nabla_\mu J^\mu_{\mathcal C} = \mathcal S_B,
```
where $`\mathcal S_B`$ is a distribution supported on $`B`$.*

</div>

<div class="proof">

*Proof.* At an admissibility barrier $`\mathcal C\to 0`$ and the projection $`P`$ loses regularity. The pushforward flow defining $`J^\mu_{\mathcal C}`$ ceases to be well-defined across $`B`$. As a result, the local conservation law acquires a source term supported on the barrier. ◻

</div>

<div class="corollary">

**Corollary 7**. *All irreversible changes in the effective description correspond to flux of coherence capacity through admissibility barriers.*

</div>

This establishes irreversibility as a structural necessity rather than a dynamical assumption.

# Capacity Flux Direction and Strain

The continuity equation alone does not determine the direction of capacity transport. Physical interpretation requires identifying what drives capacity redistribution.

## Capacity strain

<div class="definition">

**Definition 8** (Capacity strain). Let $`\mathcal L(x)`$ denote the local load imposed on the effective description by interactions, curvature, entanglement growth, measurement coupling, or environmental noise. Capacity strain is the tendency of $`\mathcal C`$ to decrease in regions where $`\mathcal L`$ is large.

</div>

<div class="assumption">

**Assumption 9** (Downhill transport principle). Coherence capacity is transported so as to oppose capacity strain: capacity flows away from regions of lower effective stability toward regions of higher effective stability.

</div>

This assumption is a constitutive choice describing how admissibility margins are encoded at the effective level; it does not introduce new microscopic dynamics.

# Capacity Focusing and Concentration

We now show that capacity transport generically leads to concentration.

<div class="definition">

**Definition 10** (Flow direction and expansion). Where $`J_C^\mu \neq 0`$, define the unit flow direction $`u^\mu := J_C^\mu / \|J_C\|`$ (with $`\|\cdot\|`$ taken with respect to the effective metric on $`Y`$ when such a chart exists). Define the expansion of the capacity flow by
``` math
\theta := \nabla_\mu u^\mu .
```
Inside admissible basins, $`\nabla_\mu J_C^\mu = 0`$ expresses conservation of the effective capacity current, but $`\theta`$ need not vanish; instead, it encodes the focusing or defocusing of the integral curves of the normalized flow $`u^\mu`$.

</div>

<div class="theorem">

**Theorem 11** (Capacity focusing). *Assume persistent capacity strain along integral curves of $`u^\mu`$. Then there exists $`\kappa>0`$ such that
``` math
\frac{d\theta}{d\tau} \le -\kappa\,\theta^2
```
along the flow.*

</div>

<div class="proof">

*Proof.* Capacity strain induces gradients in $`\mathcal C`$ that bias the flux according to the downhill transport principle. Contractivity of projection ensures that deviations from uniform flux amplify concentration rather than dispersion, producing a quadratic suppression term analogous to Raychaudhuri focusing. ◻

</div>

<div class="corollary">

**Corollary 12**. *If capacity strain persists for sufficient duration, coherence capacity concentrates and $`\theta`$ becomes negative in finite parameter distance.*

</div>

# Bottleneck and Boundary Formation

Capacity concentration has a sharp endpoint.

<div class="theorem">

**Theorem 13** (Bottleneck formation). *If inward coherence-capacity flux into a compact region exceeds outward transport for sufficient duration, then $`\mathcal C\to 0`$ on a codimension-one hypersurface surrounding the region.*

</div>

<div class="proof">

*Proof.* By the focusing theorem, persistent negative expansion drives capacity to zero in finite parameter distance. Conservation forbids disappearance of capacity elsewhere, so depletion localizes on a bounding hypersurface in the effective transport representation. ◻

</div>

<div class="definition">

**Definition 14** (Capacity bottleneck). A capacity bottleneck is a connected hypersurface on which $`\mathcal C=0`$ and across which the effective description is noninvertible.

</div>

Capacity bottlenecks are the structural origin of horizons and collapse boundaries.

# Sources of Capacity Strain

The following processes contribute to capacity strain:

- **Interaction strength:** strong coupling increases projection load.

- **Curvature:** geometric distortion raises the cost of maintaining stability.

- **Entanglement growth:** rapid correlation buildup strains coherent truncation.

- **Measurement coupling:** external apparatus imposes additional projection constraints.

- **Noise and environment:** uncontrolled coupling drains capacity through noncoherent channels.

Any combination of these can drive $`\mathcal C\to 0`$.

# A Minimal Illustrative Model

The following model is purely illustrative and does not represent a proposed fundamental dynamical law for coherence capacity; it serves only to visualize focusing, relaxation, and barrier formation under admissibility-preserving transport.

Consider a one-dimensional effective space with coordinate $`x`$, coherence capacity $`\mathcal C(x,t)`$, and current
``` math
J_{\mathcal C} = -D\,\partial_x \mathcal C + v(x)\,\mathcal C,
```
where $`v(x)`$ represents capacity strain and $`D>0`$ is a contractivity constant.

The continuity equation becomes
``` math
\partial_t \mathcal C
= D\,\partial_x^2 \mathcal C - \partial_x(v\,\mathcal C).
```

If $`v(x)`$ is inward-directed and sufficiently strong, solutions develop a finite-time zero of $`\mathcal C`$, signaling breakdown of the effective description at a moving boundary.

This toy model captures relaxation when capacity is abundant, focusing under strain, and barrier formation without singular dynamics.

# Discussion

Coherence capacity behaves as a genuine physical resource: it is conserved within admissible regimes, transported and concentrated by interaction and geometry, and exhausted at moving boundaries. These properties are independent of microscopic details and follow solely from projection-based effective description with finite stability margins.

In subsequent work we will show that capacity concentration produces gravitational attraction, capacity bottlenecks generate horizons and area laws, and competing transport regimes yield thermalization or persistent memory.

# Conclusion

We have developed a dynamical theory of coherence capacity. By introducing capacity currents, transport laws, and focusing theorems, we have shown that coherence capacity flows, concentrates, and exhausts in a manner analogous to conserved physical resources.

This dynamical picture completes the structural framework begun in the preceding work. Gravity, irreversibility, and breakdown of effective laws emerge not as separate postulates, but as unavoidable consequences of capacity transport and exhaustion.
