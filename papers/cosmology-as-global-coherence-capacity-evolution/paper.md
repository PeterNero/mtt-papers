---
abstract: |
  We show that cosmological expansion, acceleration, and horizon structure arise naturally as effective consequences of global coherence-capacity evolution under the same transport, closure, and regularity assumptions used elsewhere in the coherence-capacity framework. Building on the theory of coherence capacity and its transport, concentration, and exhaustion, we show that cosmology is not the dynamics of spacetime itself, but the global bookkeeping of how coherence capacity is redistributed and depleted over large scales. Under minimal axioms, we derive generalized Friedmann-type equations governing capacity flow, identify expansion as a relaxation process under spare capacity, and interpret cosmological horizons as global capacity bottlenecks. This framework requires no fundamental inflaton, vacuum energy, or initial singularity.
author:
- Peter Nero
current_version: v2
date: January 2026
generated_from_main_tex_sha256: 8bb44638d3e5c58da9ec842e549ea915e5d26760cb26e0502efebdf6639484d9
paper_id: cosmology-as-global-coherence-capacity-evolution
release_state: zenodo_released
released_version: v2.0
title: "**Cosmology as Global Coherence Capacity Evolution**"
zenodo_doi: 10.5281/zenodo.18322077
zenodo_record_id: 18322077
zenodo_url: "https://zenodo.org/records/18322077"
---

# Introduction

Cosmology traditionally describes the large-scale evolution of spacetime via dynamical equations for the metric. Observed expansion, acceleration, and horizon structure are attributed to energy content, vacuum energy, or initial conditions.

In this work we present a different perspective. We show that cosmology is the global manifestation of coherence capacity evolution. Expansion, acceleration, and horizons arise as necessary features of how a projection-based effective description redistributes its finite stability budget over increasingly large regions.

The central claim is simple: *cosmic expansion is a relaxation process driven by spare coherence capacity, while cosmic acceleration reflects capacity redistribution under global constraints*.

# Framework and Assumptions

We adopt the axioms introduced previously.

Axiom A1.  
Fundamental dynamics on a configuration space $`X`$ is invertible.

Axiom A2.  
Observable physics arises via a noninjective projection $`P:X\to Y`$.

Axiom A3.  
Effective descriptions are valid only on admissible regions characterized by positive coherence capacity $`\mathcal C(x)`$.

Axiom A4.  
Coherence capacity admits local transport, concentration, and exhaustion.

We further assume large-scale homogeneity and isotropy of the effective description.

#### Imported structural assumptions.

All results in this paper rely on the effective transport representation of coherence capacity developed previously, including the existence of a slab-local effective current, finite flux bounds arising from bounded projection and spectral separation, and constitutive closure governing admissible redistribution. No statement in this paper asserts a fundamental cosmological dynamics beyond these effective, encoding-level assumptions.

# Global Coherence Capacity

## Total capacity

Let $`\Sigma_t`$ denote a spatial hypersurface of the effective description. Define the total coherence capacity on $`\Sigma_t`$ by
``` math
\mathcal Q_{\mathcal C}(t) := \int_{\Sigma_t} n_\mu J^\mu_{\mathcal C}\, d^3x.
```

Inside admissible regimes, $`Q_C`$ is conserved in the effective transport representation, except where capacity is lost through global bottlenecks.

## Global capacity density

Under homogeneity, coherence capacity reduces to a scalar function of the cosmic scale parameter:
``` math
\mathcal C(x,t) \equiv \mathcal C(t).
```

This does not imply constancy in time; it implies spatial uniformity at fixed cosmic ordering.

# Cosmic Expansion as Capacity Relaxation

We now derive expansion from capacity dynamics.

## Spare capacity and relaxation

When coherence capacity is abundant relative to local strain, projection is strongly contractive. In such regimes, the effective description relaxes toward configurations that minimize gradients and strain.

<div class="theorem">

**Theorem 1** (Expansion from spare coherence capacity). *If the global coherence capacity density $`\mathcal C(t)`$ exceeds the minimum required for stability, then the effective spatial volume $`V(t)`$ increases monotonically under admissible evolution.*

</div>

<div class="proof">

*Proof.* Spare capacity enforces relaxation: gradients and inhomogeneities are damped. The only global relaxation channel compatible with homogeneity is uniform increase of spatial separation between degrees of freedom, corresponding to expansion of $`V(t)`$. ◻

</div>

Expansion is therefore not driven by repulsive forces but by the system relaxing under excess descriptive capacity.

# Generalized Friedmann Equation

We now derive the cosmological evolution equation.

## Capacity balance

Let $`a(t)`$ denote the scale factor, $`V(t)\propto a(t)^3`$. Capacity transport and conservation imply a balance equation of the form
``` math
\frac{d}{dt}\mathcal Q_{\mathcal C}(t)
=
- \Phi_{\mathcal C}^{\mathrm{out}}(t),
```
where $`\Phi_{\mathcal C}^{\mathrm{out}}`$ represents capacity loss through global bottlenecks (if any).

In the absence of such loss, $`\mathcal Q_{\mathcal C}`$ is conserved.

## Effective expansion law (encoding-level)

Dimensional consistency and isotropy imply
``` math
\left(\frac{\dot a}{a}\right)^2
=
\frac{1}{\mathcal C(t)}\,\rho_{\mathrm{eff}}(t),
```
where $`\rho_{\mathrm{eff}}`$ is the effective capacity strain density. The following relation should be understood as an effective encoding of global capacity balance under homogeneity and isotropy, not as a fundamental dynamical field equation.

<div class="theorem">

**Theorem 2** (Generalized Friedmann equation). *Cosmic expansion obeys a Friedmann-type equation with coherence capacity playing the role of inverse gravitational stiffness:
``` math
H^2 = \frac{\rho_{\mathrm{eff}}}{\mathcal C(t)}.
```*

</div>

<div class="proof">

*Proof.* This follows directly from the capacity-weighted Einstein response derived previously, specialized to homogeneous and isotropic geometry. ◻

</div>

Thus Newton’s constant is replaced by the inverse of global coherence capacity.

# Discussion

In this framework:

- Expansion occurs when spare capacity enforces relaxation.

- Deceleration occurs when capacity is strained by matter.

- Acceleration arises from redistribution of capacity under global constraints.

No new dynamical fields are required.

# Cosmic Acceleration and Apparent Dark Energy

We now address cosmic acceleration, often attributed to dark energy or a cosmological constant.

## Capacity redistribution versus vacuum energy

In the coherence-capacity framework, no additional energy component is required to produce acceleration. Instead, acceleration arises when coherence capacity is redistributed in such a way that the effective capacity density available to local regions increases over time.

<div class="definition">

**Definition 3** (Capacity redistribution). Capacity redistribution is the global rearrangement of coherence capacity that preserves total capacity while altering its local density.

</div>

Such redistribution may occur even when total capacity $`\mathcal Q_{\mathcal C}`$ is conserved.

<div class="theorem">

**Theorem 4** (Acceleration from capacity redistribution, conditional). *Assume the effective transport representation with constitutive closure and outward redistribution of coherence capacity under global constraints. If coherence capacity flows outward from regions of high strain toward regions of lower strain, then the scale factor $`a(t)`$ exhibits accelerated growth:
``` math
\ddot a > 0.
```*

</div>

<div class="proof">

*Proof.* Acceleration corresponds to decreasing effective stiffness $`1/\mathcal C(t)`$ in the generalized Friedmann equation. Outward flow of capacity increases $`\mathcal C(t)`$ in expanding regions, reducing gravitational resistance to expansion and producing $`\ddot a>0`$. ◻

</div>

Thus apparent dark energy is reinterpreted as a bookkeeping effect of capacity redistribution rather than a new physical substance.

# Cosmological Horizons as Global Capacity Bottlenecks

## Global bottleneck formation

As the universe expands, coherence capacity must be distributed across an increasingly large effective volume. If redistribution cannot keep pace with expansion, global bottlenecks form.

<div class="definition">

**Definition 5** (Cosmological capacity horizon). A cosmological capacity horizon is a codimension-one surface on which $`\mathcal C=0`$ due to insufficient capacity transport at global scales.

</div>

<div class="theorem">

**Theorem 6** (Horizon inevitability under finite transport). *Under sustained expansion with finite total coherence capacity, a cosmological capacity horizon must form.*

</div>

<div class="proof">

*Proof.* Under sustained expansion with finite total coherence capacity and bounded transport flux, redistribution fails and $`\mathcal C`$ vanishes on a bounding surface. ◻

</div>

Cosmological horizons are therefore global analogues of black hole horizons.

# Initial Conditions Without a Big Bang Singularity

Standard cosmology posits an initial singularity. In the present framework, no such singularity is required.

## Capacity-dominated initial regime

At early stages, coherence capacity is large relative to strain. Projection is strongly stable, and effective descriptions are highly relaxed.

<div class="theorem">

**Theorem 7** (Nonsingular origin). *If coherence capacity is sufficiently abundant, the effective description extends arbitrarily far in the past without encountering an admissibility barrier.*

</div>

<div class="proof">

*Proof.* Spare capacity ensures relaxation and prevents focusing to a bottleneck. Thus $`\mathcal C>0`$ at all early stages, avoiding singular behavior. ◻

</div>

The apparent Big Bang arises when tracing the effective description beyond its domain of applicability, not from a fundamental singularity.

# Arrow of Time at Cosmological Scale

We now connect global capacity evolution to the cosmic arrow of time.

<div class="theorem">

**Theorem 8** (Cosmic arrow from capacity exhaustion). *The global arrow of time aligns with the direction of net coherence capacity loss through cosmological bottlenecks.*

</div>

<div class="proof">

*Proof.* Capacity loss is irreversible and monotonically increases the total capacity entropy. The ordering of admissible descriptions therefore defines a preferred temporal direction, in the effective description ◻

</div>

This arrow is consistent with, but deeper than, thermodynamic time.

# Observational Consequences and Predictions

The coherence-capacity cosmology leads to distinct predictions:

- Apparent dark energy evolves with cosmic capacity redistribution, not as a true constant.

- Horizon entropy scales with area due to flux bounds.

- Early-universe smoothness reflects high initial capacity.

- Deviations from $`\Lambda`$CDM may appear at large scales where capacity redistribution becomes inefficient.

These predictions are testable in principle and do not require new microscopic fields.

# Discussion

Cosmology emerges here as the global bookkeeping of coherence capacity. Expansion, acceleration, and horizons arise from the same transport and bottleneck mechanisms that govern local gravity and black holes.

This unifies cosmology with the rest of effective physics and eliminates the need for separate explanations of inflation, dark energy, and initial singularities.

# Conclusion

We have shown that cosmological expansion and acceleration arise naturally from global coherence capacity evolution. Horizons, entropy, and the arrow of time are consequences of finite capacity transport and exhaustion.

Together with preceding papers, this completes a coherent framework in which:

- coherence capacity is the fundamental resource,

- gravity is its geometric bookkeeping,

- particles and forces emerge from basin dynamics,

- horizons and entropy arise from capacity bottlenecks,

- cosmology is global capacity evolution.

Effective physical laws persist precisely because coherence capacity is finite; their breakdown and global structure follow inevitably from its dynamics.
