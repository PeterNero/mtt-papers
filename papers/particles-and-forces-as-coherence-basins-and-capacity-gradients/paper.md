---
abstract: |
  We show how particles and forces arise as effective structures in admissible descriptions built from coherence basins and coherence-capacity transport, under the same stability, regularity, and closure assumptions used elsewhere in the coherence-capacity framework. Building on the transport theory developed in “Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion,” we show that localized, persistent excitations correspond to stable coherence basins, while forces arise from gradients and flows of coherence capacity. Newtonian motion, the Lorentz force, and confinement phenomena are obtained as basin-centroid and coherence-transport effects without introducing fundamental force carriers. Particle number nonconservation, charge conservation, and universality of gravity follow naturally from the basin framework.
author:
- Peter Nero
current_version: v2
date: January 2026
generated_from_main_tex_sha256: 3d3990ace558f14a54068fb5789d89c4f77aad91aa0cfa9c87cf433e6f4d8aef
paper_id: particles-and-forces-as-coherence-basins-and-capacity-gradients
release_state: zenodo_released
released_version: v2.0
title: |
  **Particles and Forces as Coherence Basins  
  and Capacity Gradients**
zenodo_doi: 10.5281/zenodo.18322084
zenodo_record_id: 18322084
zenodo_url: "https://zenodo.org/records/18322084"
---

# Introduction

In the preceding papers we identified coherence capacity as the fundamental resource governing effective physical descriptions and developed its transport, concentration, and exhaustion dynamics. In this work we show how the familiar ontology of particles and forces arises from that same structure.

The central claim of this paper is simple: *particles are stable coherence basins, and forces are the shadows of coherence-capacity gradients acting on those basins*.

This viewpoint eliminates the need to treat particles as fundamental point objects or forces as primitive interactions. Instead, particles and forces emerge from the same projection-based stability constraints that govern gravity, time, and irreversibility.

# Effective States and Coherence Basins

## Effective state space

Let $`Y`$ denote the space of effective (observable) states obtained by projection from the fundamental configuration space. Within admissible regions, effective dynamics is well-defined and predictive.

#### Effective description level.

The effective state space $`Y`$ should be understood as the image of an admissible projection from the coherent sector of the underlying state space, equipped with whatever minimal structure (topological, measure-theoretic, or differentiable) is required to support the effective equations used below. No claim is made that $`Y`$ exists globally or independently of the admissible regime.

## Coherence basins

<div class="definition">

**Definition 1** (Coherence basin). A coherence basin $`B_\alpha \subset Y`$ is a connected region of effective state space such that:

- projection stability holds throughout $`B_\alpha`$,

- trajectories entering $`B_\alpha`$ remain in $`B_\alpha`$ under admissible evolution,

- disturbances within $`B_\alpha`$ are contractively damped.

</div>

Coherence basins are the effective analogues of attractors or fixed-point regions in dynamical systems.

<div class="definition">

**Definition 2** (Particle). A particle is a localized, persistent coherence basin whose support in effective space remains bounded and identifiable over admissible evolution.

</div>

This definition makes no reference to point-like ontology or fundamental fields. Persistence and localization are properties of basin stability.

# Basin Density and Centroid Dynamics

## Effective density representation (assumption)

In admissible regimes where a smooth effective chart exists, we assume that the restriction of the coherence basin admits an absolutely continuous representation with respect to the effective spatial measure, yielding a basin density $`\rho_\alpha(x,t)`$. This representation is effective and slab-local; it does not assert a fundamental density or fluid ontology. All subsequent continuum equations are understood in this restricted, encoding-level sense.

<div class="lemma">

**Lemma 3** (Preservation of basin identity under effective representation). *Within admissible regimes, the effective density representation $`\rho_\alpha(x,t)`$ uniquely tracks the identity of the underlying coherence basin. Distinct coherence basins cannot yield identical effective density evolutions on overlapping admissible charts, except at admissibility barriers where basin merge–split occurs.*

</div>

## Basin density

To describe motion of a coherence basin, we introduce a basin density $`\rho_\alpha(x,t)`$ on an effective spatial slice $`\Sigma`$.

Normalization:
``` math
M_\alpha := \int_\Sigma \rho_\alpha(x,t)\,d^3x
```
is conserved within admissible regimes.

## Centroid definition

<div class="definition">

**Definition 4** (Basin centroid). The centroid of a coherence basin is
``` math
X^i(t) := \frac{1}{M_\alpha}\int_\Sigma x^i\,\rho_\alpha(x,t)\,d^3x.
```

</div>

The centroid is the effective worldline of the particle.

# Continuity and Momentum Balance

## Continuity equation

Within an admissible basin, the reduced dynamics yields a continuity equation:
``` math
\partial_t \rho_\alpha + \nabla\cdot(\rho_\alpha v) = 0,
```
where $`v`$ is the effective velocity field induced by the underlying dynamics and projection.

#### Constitutive closure.

The continuity and momentum-balance equations below are constitutive relations of the effective description. Their existence follows from the assumed regularity of the basin density representation and does not introduce new microscopic dynamics.

## Momentum balance

Assume the existence of an effective momentum flux tensor $`\Pi^{ij}`$ such that:
``` math
\partial_t(\rho_\alpha v^i) + \partial_j \Pi^{ij}
= \rho_\alpha a^i_{\mathrm{eff}},
```
where $`a^i_{\mathrm{eff}}`$ encodes bias induced by coherence-capacity gradients and internal connections.

# Newtonian Motion from Basin Centroids

<div class="theorem">

**Theorem 5** (Centroid equation of motion, effective). *If the basin is narrow compared to the scale of variation of $`a^i_{\mathrm{eff}}`$, then the centroid satisfies
``` math
M_\alpha \ddot X^i = F^i(X),
```
where
``` math
F^i(X) := M_\alpha a^i_{\mathrm{eff}}(X).
```*

</div>

<div class="proof">

*Proof.* The result holds in the narrow-basin, slowly varying limit of the effective continuum representation. Integrating the momentum balance equation over space and using localization of $`\rho_\alpha`$ yields the stated result. ◻

</div>

<div class="corollary">

**Corollary 6**. *Newton’s second law arises as the narrow-basin limit of coherence-basin dynamics.*

</div>

This law is not fundamental but emergent: the “force” reflects bias in capacity transport rather than interaction between point objects.

# Interpretation

The derivation above shows that classical particle motion emerges whenever coherence basins are sufficiently localized and capacity gradients vary slowly. Mass corresponds to the integrated coherence weight $`M_\alpha`$ of the basin; force corresponds to spatial variation of the effective capacity-induced acceleration field. This quantity encodes inertial resistance of the basin to chart reconfiguration, not a fundamental mass density; its appearance as an integral reflects the chosen effective representation.

No assumption of fundamental forces has been made.

# Electromagnetism as Phase-Coherence Transport

## Phase coherence and internal connections

In addition to spatial localization, coherence basins generally carry internal phase structure inherited from the projection of the fundamental configuration space. We model this by associating to each basin a complex amplitude
``` math
\psi(x) = \sqrt{\rho(x)}\,e^{i\theta(x)},
```
where $`\rho`$ is the basin density and $`\theta`$ is an internal phase.

Gauge freedom arises because only relative phase is physically meaningful. Accordingly, the effective description involves a connection $`A_\mu(x)`$, and physical phase gradients appear only in the gauge-covariant combination
``` math
p_\mu := \partial_\mu \theta - q A_\mu,
```
where $`q`$ labels the basin’s coupling to the internal phase connection.

## Phase-gradient transport

Assuming the Hamilton–Jacobi constraint obtained in the eikonal limit of coherent wave reconstruction, within an admissible basin, coherent evolution preserves the Hamilton–Jacobi constraint
``` math
g^{\mu\nu} p_\mu p_\nu = m^2,
```
which may be viewed as the eikonal limit of coherent wave dynamics.

Taking a covariant derivative along the basin centroid worldline $`X^\mu(\tau)`$ yields
``` math
\frac{D p_\mu}{D\tau}
= -q\,\partial_\mu A_\nu\,\dot X^\nu
+ q\,\partial_\nu A_\mu\,\dot X^\nu.
```

Introducing the field strength
``` math
F_{\mu\nu} := \partial_\mu A_\nu - \partial_\nu A_\mu,
```
we obtain the effective equation of motion
``` math
m\,\frac{D \dot X^\mu}{D\tau} = q\,F^\mu{}_{\nu}\,\dot X^\nu.
```

<div class="theorem">

**Theorem 7** (Lorentz force as effective coherence-transport law). *The Lorentz force arises as the condition that phase coherence be preserved under admissible transport of coherence basins.*

</div>

This result holds at the effective description level and presupposes the phase-coherent transport structure established in the underlying reconstruction.

Electromagnetism therefore does not represent a fundamental force carrier, but the bookkeeping of phase-coherence preservation during basin motion.

# Gauge Charge and Conservation Laws

## Charge as a basin invariant

The quantity $`q`$ appearing in the covariant phase gradient is an invariant label of the coherence basin. It characterizes how the basin transforms under internal phase rotations.

<div class="definition">

**Definition 8** (Gauge charge). Gauge charge is the representation label associated with internal phase-coherence transport of a coherence basin.

</div>

## Charge conservation

Because admissible evolution preserves basin identity except at barriers, gauge charge is conserved along admissible basin trajectories, except at admissibility barriers.

<div class="theorem">

**Theorem 9** (Charge conservation). *Within admissible regimes, gauge charge is conserved along coherence-basin trajectories.*

</div>

<div class="proof">

*Proof.* Charge labels are topological invariants of the basin structure and cannot change under continuous admissible evolution. ◻

</div>

In contrast, particle number is not protected: basins may merge, split, or dissolve at admissibility barriers, leading to particle creation and annihilation.

# Confinement as Coherence Protection

## Non-Abelian coherence strain

In sectors with non-Abelian internal structure, coherence transport imposes additional strain. Maintaining non-singlet coherence across extended regions requires preserving correlated internal orientations, which rapidly consumes coherence capacity.

## Area-law cost

Consider separating two coherence basins carrying non-Abelian charge. Maintaining admissibility requires preserving a coherent “string” of internal alignment between them. The capacity cost of this configuration grows with the area swept by the separation process.

<div class="theorem">

**Theorem 10** (Confinement from capacity exhaustion, conditional). *Assume bounded transport flux and persistent coherence strain under non-Abelian separation. Non-singlet coherence basins in non-Abelian sectors experience capacity exhaustion under separation, forcing recombination into singlet basins.*

</div>

<div class="proof">

*Proof.* Persistent capacity strain along the separation direction induces focusing of capacity flux and eventual formation of a bottleneck. The only admissible configuration that avoids capacity exhaustion is one in which net non-Abelian charge is neutralized locally. ◻

</div>

This reproduces confinement and the area-law behavior of Wilson loops as consequences of coherence protection rather than fundamental interaction potentials.

# Summary of Particle and Force Emergence

We summarize the emergent picture:

- Particles are stable coherence basins.

- Mass is the integrated coherence weight of a basin.

- Motion arises from capacity-gradient bias.

- Gravity appears as the universal response to total coherence-capacity distribution in effective geometric encodings.

- Electromagnetism preserves phase coherence under transport.

- Gauge charges are basin invariants.

- Confinement enforces coherence protection in non-Abelian sectors.

No fundamental point particles or force carriers are required.

# Discussion

Particles and forces emerge here as structural features of projection-based effective descriptions with finite coherence capacity. This framework explains why gravity is universal, why gauge interactions are quantized, and why particle number is not conserved, while charge is.

The derivations rely only on stability, projection, and capacity transport, and therefore apply broadly to any effective theory with similar structure.

# Conclusion

We have shown that particles and forces arise naturally from the dynamics of coherence capacity. Stable coherence basins behave as particles, while gradients and transport of coherence capacity generate the effective forces governing their motion.

This completes the coherence-capacity trilogy at the level of effective emergence:

- coherence capacity as the fundamental resource,

- its transport, concentration, and exhaustion,

- and the emergence of particles and forces.

Further work will address cosmology, entropy bounds, and quantum field theory reconstruction within this framework.
