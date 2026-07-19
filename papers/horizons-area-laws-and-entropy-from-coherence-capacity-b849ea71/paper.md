---
abstract: |
  We derive horizon formation, area laws, and entropy bounds as necessary consequences of coherence-capacity bottlenecks in projection-based effective descriptions. Building on the theory of coherence capacity and its transport developed in preceding work, we show that whenever inward capacity flux exceeds outward transport, admissibility fails on a codimension-one surface. Such surfaces act as horizons: effective descriptions become noninvertible across them, and global information recovery is impossible. We demonstrate that entropy arises as the bookkeeping of coherence capacity loss and that area laws follow from geometric bounds on capacity flux. The results are independent of microscopic dynamics and apply to any effective theory with finite stability margins.
author:
- Peter Nero
current_version: v2
date: January 2026
generated_from_main_tex_sha256: 5c23ace35477bc30b6c0452d7a94ac980a8499d0a0bfffeae65fe26cda9923d2
paper_id: horizons-area-laws-and-entropy-from-coherence-capacity-b849ea71
release_state: zenodo_released
released_version: v2.0
title: |
  **Horizons, Area Laws, and Entropy  
  from Coherence Capacity Bottlenecks**
zenodo_doi: 10.5281/zenodo.18322069
zenodo_record_id: 18322069
zenodo_url: "https://zenodo.org/records/18322069"
---

# Introduction

Horizons and entropy occupy a central place in modern physics. Black holes possess entropy proportional to horizon area; quantum systems thermalize and lose memory; effective descriptions exhibit irreversible behavior. These phenomena are traditionally treated using separate conceptual frameworks.

In this work we show that horizons and entropy arise from a single structural mechanism: the formation of *coherence capacity bottlenecks*. When the transport of coherence capacity into a region exceeds its ability to redistribute that capacity, the effective description necessarily fails on a bounding surface. This surface acts as a horizon for the effective description.

Entropy is then identified as the measure of coherence capacity that has been irreversibly shed at such bottlenecks. Area laws follow from geometric bounds on capacity flux through codimension-one surfaces.

No assumptions of fundamental information destruction, singular dynamics, or microscopic entropy are required.

# Review of Coherence Capacity and Transport

We briefly summarize the framework established previously.

## Coherence capacity

Coherence capacity $`\mathcal C(x)`$ is the local stability margin that allows a projection-based effective description to remain predictive. It is positive inside admissible regions and vanishes at admissibility barriers.

## Capacity transport

Within admissible basins, coherence capacity admits a conserved current $`J^\mu_{\mathcal C}`$ satisfying
``` math
\nabla_\mu J^\mu_{\mathcal C} = 0 \qquad (\mathcal C > 0).
```

Capacity is redistributed by interactions, curvature, and coupling, and may concentrate under persistent strain.

## Capacity exhaustion

At admissibility barriers $`\mathcal C\to 0`$ and capacity conservation fails:
``` math
\nabla_\mu J^\mu_{\mathcal C} = \mathcal S_B.
```

Such barriers are associated with noninvertibility of the effective description.

#### Scope of transport statements.

All transport statements in this paper are formulated at the level of an effective representation of admissibility, as introduced in the capacity transport framework. They are slab-local and conditional on the existence of an admissible chart with controlled projection, absolute continuity, and constitutive closure. No statement in this section asserts the existence of a fundamental or global transport law.

# Capacity Bottlenecks as Horizons

We now formalize the connection between capacity bottlenecks and horizons.

<div class="definition">

**Definition 1** (Capacity bottleneck). A capacity bottleneck is a connected codimension-one hypersurface $`H`$ defined by $`\mathcal C=0`$, across which the effective description is noninvertible.

</div>

<div class="theorem">

**Theorem 2** (Horizon formation from capacity imbalance). *If the inward flux of coherence capacity into a compact region exceeds the maximum outward transport permitted by admissible dynamics, then a capacity bottleneck forms on a hypersurface bounding the region.*

</div>

<div class="proof">

*Proof.* By applying the focusing and bottleneck results established in Theorem 9.2 and Theorem 10.1 of *Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion* to the effective current representation, persistent negative expansion along integral curves drives $`C`$ to zero on a codimension-one hypersurface. ◻

</div>

<div class="corollary">

**Corollary 3**. *Capacity bottlenecks act as horizons: effective evolution cannot be globally inverted across them.*

</div>

This definition of a horizon is purely structural and does not rely on light cones or causal structure. Causal horizons in geometric encodings arise as a special case of capacity bottlenecks when the effective description admits a Lorentzian structure.

# Irreversibility and Loss of Global Description

The presence of a capacity bottleneck has immediate consequences.

<div class="theorem">

**Theorem 4** (No global recovery across horizons). *Across a capacity bottleneck, there exists no global inverse of the effective evolution mapping.*

</div>

<div class="proof">

*Proof.* This follows directly from projection noninvertibility at $`\mathcal C=0`$. Distinct configurations on opposite sides of the bottleneck share identical effective images. ◻

</div>

Thus information loss at horizons is not a failure of fundamental dynamics, but a structural limitation of effective description.

# Entropy as Capacity Accounting

We now define entropy in this framework.

<div class="definition">

**Definition 5** (Capacity entropy). The entropy associated with a region is defined as the cumulative coherence capacity irreversibly shed at admissibility barriers enclosing that region.

</div>

Entropy is therefore not a measure of microscopic disorder, but a measure of lost descriptive capacity.

<div class="lemma">

**Lemma 6**. *Capacity entropy is nondecreasing under admissible evolution.*

</div>

<div class="proof">

*Proof.* Capacity is conserved inside admissible regions and can only be lost at barriers. Once lost, capacity cannot be recovered by the effective description. ◻

</div>

This establishes a generalized second law without invoking probabilistic assumptions.

# Area Laws from Capacity Flux Bounds

We now show that capacity bottlenecks imply entropy bounds proportional to the area of the bottleneck surface. This result is purely geometric and does not depend on microscopic dynamics.

## Capacity flux through hypersurfaces

Let $`H`$ be a capacity bottleneck hypersurface with unit normal $`n_\mu`$. Define the capacity flux through $`H`$ by
``` math
\Phi_{\mathcal C}(H) := \int_H n_\mu J^\mu_{\mathcal C}\, dA,
```
where $`dA`$ is the induced area element on $`H`$.

Since capacity transport is local and finite-bandwidth, the flux density $`|n_\mu J^\mu_{\mathcal C}|`$ admits a universal upper bound $`\sigma_{\max}`$ determined by admissibility constraints.

<div class="assumption">

**Assumption 7** (Flux bound). There exists a constant $`\sigma_{\max}`$ such that
``` math
|n_\mu J^\mu_{\mathcal C}| \le \sigma_{\max}
```
for all admissible configurations.

</div>

This assumption expresses the finite rate at which coherence capacity can be transported across a surface.

#### Justification.

Such a bound is the transport-level encoding of bounded projector regularity and finite spectral separation. In admissible domains, updates of coherent structure occur at finite effective bandwidth, which limits the rate at which admissibility can be transported across any codimension-one interface. The flux bound therefore reflects existing MTT control data rather than an independent physical postulate.

## Area law

<div class="theorem">

**Theorem 8** (Area bound on capacity loss). *Let $`H`$ be a capacity bottleneck. Then the total coherence capacity shed across $`H`$ satisfies
``` math
\Delta \mathcal Q_{\mathcal C}(H) \le \sigma_{\max}\, \mathrm{Area}(H).
```*

</div>

<div class="proof">

*Proof.* By definition,
``` math
\Delta \mathcal Q_{\mathcal C}(H) = \int_H |n_\mu J^\mu_{\mathcal C}|\, dA.
```
Applying the flux bound yields the stated inequality. ◻

</div>

<div class="corollary">

**Corollary 9** (Entropy area law). *The entropy associated with a capacity bottleneck is bounded by the area of the bottleneck surface.*

</div>

Thus area laws arise as direct consequences of finite capacity flux, independent of any holographic hypothesis.

# Black Hole Entropy as Capacity Saturation

We now specialize the preceding results to black hole horizons.

## Horizons as maximal bottlenecks

A black hole horizon corresponds to a capacity bottleneck for exterior observables.

#### Assumption 7.1 (Stationary saturation).

In stationary bottleneck configurations, the effective capacity flux saturates the bound, i.e. $`|n_\mu J_C^\mu| = \sigma_{\max}`$ on the horizon hypersurface.

<div class="theorem">

**Theorem 10** (Black hole entropy). *The entropy associated with a black hole horizon is
``` math
S = \sigma_{\max}\, \mathrm{Area}(H),
```
up to universal normalization.*

</div>

<div class="proof">

*Proof.* For stationary horizons, capacity transport is extremal. Substituting the saturated flux into the area bound yields the stated result. ◻

</div>

This reproduces the Bekenstein–Hawking scaling without reference to microscopic degrees of freedom or state counting.

# Partial Recovery and Restricted Algebras

Although global recovery across a capacity bottleneck is impossible, restricted recovery may remain feasible.

## Restricted observables

Let $`\mathcal A_{\mathrm{ext}}`$ denote the algebra of observables supported outside the bottleneck. Within $`\mathcal A_{\mathrm{ext}}`$, effective evolution may admit a partial inverse.

<div class="theorem">

**Theorem 11** (Restricted recovery). *There exists a right-inverse of the effective evolution on $`\mathcal A_{\mathrm{ext}}`$ if and only if coherence capacity remains positive for the restriction of the coherent projection to $`A_{\mathrm{ext}}`$ remains bounded and admits a measurable right inverse on the corresponding effective algebra.*

</div>

<div class="proof">

*Proof.* Restricted observables probe only a subset of the configuration space. If capacity is exhausted only for complementary degrees of freedom, the projection remains invertible on the restricted sector. ◻

</div>

This explains why information recovery schemes based on restricted observables (e.g., “islands”) succeed without restoring global invertibility.

# Relation to Holography and the Page Curve

The coherence-capacity framework clarifies several features of modern holographic approaches.

## Page curve

The Page curve describes the entropy of radiation as a function of time. In the present framework, it reflects redistribution of coherence capacity between interior and exterior observables.

Early-time growth corresponds to capacity being shed across the horizon. Late-time saturation reflects reorganization of capacity among restricted algebras, not restoration of global coherence.

## No paradox

There is no contradiction between unitary fundamental dynamics and effective information loss. Global unitarity holds upstairs; effective irreversibility is enforced by capacity bottlenecks.

# Discussion

The results of this paper show that horizons, entropy, and area laws are not special features of gravity but generic consequences of projection- based effective descriptions with finite coherence capacity.

This framework explains:

- why entropy scales with area rather than volume,

- why horizons imply information loss for effective observers,

- why recovery is possible only on restricted algebras,

- why singularities are unnecessary for horizon formation.

All results follow from finite capacity transport and do not depend on microscopic details.

# Conclusion

We have shown that coherence capacity bottlenecks give rise to horizons, entropy, and area laws as structural necessities. Entropy measures the coherence capacity irreversibly shed at admissibility barriers, and area laws reflect universal bounds on capacity flux.

Together with preceding work, this completes a unified framework in which:

- coherence capacity is the fundamental resource,

- gravity is its geometric bookkeeping,

- particles and forces emerge from basin dynamics,

- horizons and entropy arise from capacity exhaustion.

Effective physical laws persist precisely because coherence capacity is finite; their breakdown is the price paid for stability and predictability.
