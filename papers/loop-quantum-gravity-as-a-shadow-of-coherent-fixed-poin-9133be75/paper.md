---
abstract: |
  We show that the kinematical structure of loop quantum gravity (LQG) arises as a 4D shadow of coherent fixed-point dynamics in Modal Triplet Theory (MTT). In particular, the real SU(2) Ashtekar–Barbero connection, spin-network kinematics, and discrete area/volume spectra emerge as effective encodings of compact holonomy and gap-controlled truncation under noninvertible projection. We further prove that the Barbero–Immirzi parameter $`\gamma`$ is not a free quantization ambiguity within the coherent universality class: it is fixed by the same bottleneck data controlling coherent-sector symplectic normalization and admissibility. Black hole entropy matching is reinterpreted as a consistency condition on admissible coherent microstate counting, not parameter fitting. Finally, we formulate cross-sector closure and falsifiability: the same bottleneck vector $`\Theta`$ that fixes $`\gamma`$ also controls collapse thresholds and UV completion in independent shadow constructions. All results are slab-local and admissibility-conditioned.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 2f4bd16736c2cd32422731d4f3efc6abd17585e1477216a7631cf052db36cc60
paper_id: loop-quantum-gravity-as-a-shadow-of-coherent-fixed-poin-9133be75
release_state: zenodo_released
released_version: v1.0
title: |
  **Loop Quantum Gravity as a Shadow of Coherent Fixed-Point Dynamics**  
  Immirzi parameter, geometric discreteness, and spin-network kinematics from coherent-sector projection
zenodo_doi: 10.5281/zenodo.18261700
zenodo_record_id: 18261700
zenodo_url: "https://zenodo.org/records/18261700"
---

# Introduction

Canonical loop quantum gravity (LQG) provides a mathematically controlled kinematical quantization of general relativity using the real SU(2) Ashtekar–Barbero connection, spin-network states, and discrete spectra of geometric operators. Despite these successes, several foundational features remain ambiguous within LQG itself: the origin of the SU(2) structure, the interpretation of spin networks as fundamental states of geometry versus effective encodings, the apparent freedom of the Barbero–Immirzi parameter $`\gamma`$, and the precise relationship between kinematical discreteness and continuum semiclassical limits.

This paper provides a reduced-dynamical resolution of these points by showing that LQG kinematics emerges as a shadow of coherent fixed-point dynamics under noninvertible projection in a coherent universality class. In this framework, SU(2) compactness, discrete spectra, and spin-network labeling arise as effective encodings determined by spectral gap structure and symplectic normalization. Crucially, $`\gamma`$ is fixed by bottleneck data and is not independently tunable without leaving the coherent universality class.

We proceed in a PRD-style, slab-local and admissibility-conditioned manner: statements are made only on bounded-geometry time slabs where coherent projection is bounded and stability margins remain positive.

# Minimal Coherent-Sector Inputs and Claim Discipline

## Slab-locality and admissibility

<div id="ass:slab" class="assumption">

**Assumption 1** (Slab-local coherent regime). All results are asserted on bounded-geometry time slabs $`\Omega=[0,T]\times\Sigma`$ where:

1.  the reduced coherent projector exists and is bounded on the required domains;

2.  a uniform spectral gap separates coherent and noncoherent internal modes;

3.  stability margins defining admissible basins remain strictly positive away from boundaries.

</div>

## Bottleneck vector

<div id="def:Theta" class="definition">

**Definition 2** (Bottleneck vector). Let $`\Theta`$ denote the finite collection of coherent-sector parameters controlling:

1.  the uniform internal spectral gap $`\lambda_\ast`$;

2.  boundedness and norm data of the coherent projector;

3.  overlap and normalization data fixing reduced symplectic structure;

4.  admissibility and stability-margin parameters controlling basin dynamics.

</div>

<div class="remark">

*Remark 3*. The role of $`\Theta`$ is purely operational: it is the minimal data required to control projection, truncation, and stability on the slab. No global claims beyond slab-locality are made.

</div>

# Emergence of SU(2) Connection Variables

In this section we show that the real SU(2) Ashtekar–Barbero connection used in canonical LQG arises as a shadow variable of coherent-sector geometry under projection. No additional gauge principle is postulated.

## Coherent geometry and internal reuse

Let $`e^i_a`$ denote an emergent spatial triad on $`\Sigma`$ induced by the coherent fixed point, and let $`\omega^{ij}_a`$ be the associated spin connection. Coherent-sector projection selects a preferred compact stabilizer subgroup acting on internal rotational data.

<div id="ass:su2reuse" class="assumption">

**Assumption 4** (Compact rotational reuse channel). On each spatial slice $`\Sigma`$, the coherent-sector geometry admits a preferred compact rotational stabilizer acting on the projected internal tangent data. The stabilizer is connected and compact.

</div>

<div id="prop:ABshadow" class="proposition">

**Proposition 5** (Real compact connection as a shadow). *Under Assumption <a href="#ass:su2reuse" data-reference-type="ref" data-reference="ass:su2reuse">4</a> and slab-local admissibility (Assumption <a href="#ass:slab" data-reference-type="ref" data-reference="ass:slab">1</a>), the unique real compact connection compatible with coherent-sector projection and spatial admissibility is of Ashtekar–Barbero form
``` math
A^i_a \;=\; \Gamma^i_a + \gamma\,K^i_a,
```
where $`\Gamma^i_a`$ is the torsion-free spin connection compatible with $`e^i_a`$, $`K^i_a`$ is extrinsic curvature, and $`\gamma\in\mathbb{R}`$.*

</div>

<div class="proof">

*Proof.* Compactness of the stabilizer implies a real compact gauge group, hence an SU(2)-type connection. Compatibility with the induced symplectic structure on the reduced phase space requires a connection differing from $`\Gamma^i_a`$ by a term proportional to $`K^i_a`$. Reality of the reduced phase space fixes the proportionality to a real constant $`\gamma`$. ◻

</div>

<div class="remark">

*Remark 6*. This explains why SU(2) appears in canonical quantum gravity formulations that enforce reality and compactness: it is the compact shadow of coherent rotational reuse.

</div>

# Spin Networks as Effective Encodings

Spin networks arise naturally as effective encodings of coherent-sector data under spectral truncation and compact holonomy.

## Gap-controlled truncation and graph structure

<div id="ass:graph" class="assumption">

**Assumption 7** (Gap-controlled effective finiteness). On bounded regions of $`\Sigma`$, gap-controlled truncation implies only finitely many independent coherent degrees of freedom contribute to the reduced dynamics within the slab-local controlled domain.

</div>

This effective finiteness can be encoded combinatorially by graphs $`\Gamma\subset\Sigma`$, with edges representing coupling channels between coherent patches.

## Representation labels as overlap encodings

Edges carry labels in irreducible representations of the compact reuse group (SU(2)), encoding overlap and holonomy data.

<div id="thm:spinencoding" class="theorem">

**Theorem 8** (Spin networks as encoding states). *Under Assumptions <a href="#ass:slab" data-reference-type="ref" data-reference="ass:slab">1</a>, <a href="#ass:su2reuse" data-reference-type="ref" data-reference="ass:su2reuse">4</a>, and <a href="#ass:graph" data-reference-type="ref" data-reference="ass:graph">7</a>, spin network states form a faithful encoding of equivalence classes of coherent configurations under projection and spectral truncation. They are effective representatives of reduced coherent data, not fundamental geometric excitations.*

</div>

<div class="proof">

*Proof.* Noninvertible projection identifies microscopic configurations that differ below the truncation scale. Gap control implies only finitely many effective degrees of freedom per bounded region are distinguishable in the reduced theory. Compact holonomy decomposes these degrees into discrete SU(2) representations, yielding a discrete labeled basis. Graph connectivity encodes adjacency structure of coherent patches. ◻

</div>

# Discreteness of Area and Volume Operators

We derive discrete geometric spectra as consequences of compact holonomy and truncation.

<div id="thm:discretespectra" class="theorem">

**Theorem 9** (Discrete spectra as gap-controlled encodings). *Under compact SU(2) holonomy (Assumption <a href="#ass:su2reuse" data-reference-type="ref" data-reference="ass:su2reuse">4</a>) and gap-controlled truncation (Assumption <a href="#ass:graph" data-reference-type="ref" data-reference="ass:graph">7</a>), the spectra of area and volume operators constructed from fluxes of the densitized triad are discrete, with eigenvalues proportional to SU(2) representation labels.*

</div>

<div class="proof">

*Proof.* Flux operators generate the SU(2) Lie algebra on edges intersecting a surface or region. Quadratic geometric operators depend on the SU(2) Casimir eigenvalues, which are discrete and labeled by half-integers $`j`$. Truncation bounds the number of contributing edges/labels in bounded regions, preserving discreteness as an effective encoding. ◻

</div>

<div class="remark">

*Remark 10*. The result concerns discreteness of the reduced encoding spectra and does not assert a fundamental lattice ontology for spacetime.

</div>

# The Barbero–Immirzi Parameter Is Not Free

The Barbero–Immirzi parameter $`\gamma`$ is traditionally treated as a quantization ambiguity fixed a posteriori by black hole entropy matching. We show that within the coherent universality class it is fixed by bottleneck data $`\Theta`$.

## Normalization origin

In the reduced connection $`A^i_a = \Gamma^i_a + \gamma K^i_a,`$ $`\gamma`$ measures the relative normalization between extrinsic curvature and spin-connection contributions in the reduced symplectic structure.

<div id="thm:immirzi" class="theorem">

**Theorem 11** (Immirzi parameter as a bottleneck function). *Under Assumption <a href="#ass:slab" data-reference-type="ref" data-reference="ass:slab">1</a>, the Barbero–Immirzi parameter $`\gamma`$ is a derived quantity within the coherent universality class:
``` math
\gamma \;=\; \gamma(\Theta),
```
determined uniquely (up to controlled truncation error) by the ratio of coherent-sector symplectic normalization to compact reuse holonomy normalization.*

</div>

<div class="proof">

*Proof.* The reduced symplectic form on $`\Sigma`$ is obtained by projecting the coherent-sector action and restricting to the compact reuse channel. Both the normalization of the spin connection and the normalization of the extrinsic curvature term are fixed by coherent overlap data and projector norms encoded in $`\Theta`$. Therefore their ratio is fixed by $`\Theta`$, yielding $`\gamma=\gamma(\Theta)`$. Independently choosing $`\gamma`$ would modify this ratio and thus change $`\Theta`$, moving outside the universality class. ◻

</div>

<div id="cor:nofreegamma" class="corollary">

**Corollary 12** (No independent tuning of $`\gamma`$). *Any model requiring independent tuning of $`\gamma`$ relative to other coherent-sector bottleneck data does not correspond to a coherent universality completion.*

</div>

# Black Hole Entropy Revisited

We show that black hole entropy matching fixes $`\gamma`$ as a consistency condition on admissible coherent microstate counting rather than parameter fitting.

## Horizon admissibility and microstates

<div id="ass:horizon" class="assumption">

**Assumption 13** (Horizon admissibility). A horizon cross-section $`S\subset\Sigma`$ corresponds to a compact surface on which coherent-sector configurations are restricted by admissibility and stability compatible with the macroscopic geometry.

</div>

Let $`\mathcal{N}(A)`$ denote the number of admissible coherent equivalence classes projecting to horizon area $`A`$ within truncation tolerance.

<div id="prop:areacount" class="proposition">

**Proposition 14** (Area-proportional coherent microstate growth). *Under gap-controlled truncation and compact reuse holonomy, the number of admissible coherent equivalence classes satisfies
``` math
\log \mathcal{N}(A) = \alpha(\Theta)\,\frac{A}{\ell_P^2} + \mathcal{O}(\log A),
```
with $`\alpha(\Theta)`$ determined by bottleneck data.*

</div>

<div class="proof">

*Proof.* Gap control bounds the number of independent coherent degrees of freedom per unit area. Compact holonomy restricts overlap data to discrete representation classes. Hence microstate multiplicities grow exponentially with area, with density determined by coherent overlap and admissibility parameters in $`\Theta`$. Subleading logarithmic corrections arise from combinatorial and boundary effects. ◻

</div>

<div id="thm:gamma_entropy" class="theorem">

**Theorem 15** (Entropy consistency condition fixes $`\gamma`$). *Within the coherent universality class, matching the leading entropy $`\log\mathcal{N}(A)`$ to the Bekenstein–Hawking law $`S_{\mathrm{BH}}=A/(4\ell_P^2)`$ fixes $`\gamma`$ to the same value $`\gamma(\Theta)`$ as in Theorem <a href="#thm:immirzi" data-reference-type="ref" data-reference="thm:immirzi">11</a>.*

</div>

<div class="proof">

*Proof.* The area spectrum introduces a factor of $`\gamma`$ in the conversion from representation labels to geometric area. The microstate density per unit area is $`\alpha(\Theta)`$. Consistency with $`S_{\mathrm{BH}}`$ therefore fixes $`\gamma`$ uniquely as a function of $`\Theta`$. ◻

</div>

<div id="cor:notfit" class="corollary">

**Corollary 16** (Entropy matching is not parameter fitting). *The usual determination of $`\gamma`$ by entropy matching is a consistency constraint on admissible coherent microstate counting, not an independent tuning of a free parameter.*

</div>

# Relation to Ongoing LQG and Spin-Foam Research

We summarize alignment and contributions relative to current LQG/spin-foam programs.

## Origin of SU(2)

Proposition <a href="#prop:ABshadow" data-reference-type="ref" data-reference="prop:ABshadow">5</a> explains the SU(2) structure as the compact shadow of coherent rotational reuse, rather than a postulated fundamental gauge group.

## Spin networks and coarse-graining

Theorem <a href="#thm:spinencoding" data-reference-type="ref" data-reference="thm:spinencoding">8</a> interprets spin networks as encodings of coherent equivalence classes under projection, clarifying why graph refinement does not directly correspond to physical refinement and why coarse-graining requires additional structure.

## Spin foams

Spin foams may be interpreted as effective propagation kernels for encoded coherent data between slices, rather than as fundamental sums over microscopic spacetime histories. This accounts for universality of semiclassical limits and the necessity of renormalization/coarse-graining.

## Running of $`\gamma`$

Apparent running of $`\gamma`$ in effective descriptions indicates transitions between admissible regimes or changes in $`\Theta`$; within a fixed coherent universality class, $`\gamma`$ is fixed by Theorem <a href="#thm:immirzi" data-reference-type="ref" data-reference="thm:immirzi">11</a>.

# Cross-Sector Closure and Falsifiability

## Closure principle

<div id="thm:closure" class="theorem">

**Theorem 17** (Cross-sector closure). *Within the coherent universality class on bounded-geometry slabs, the following quantities are fixed functions of the same bottleneck vector $`\Theta`$:*

1.  *collapse and measurement-induced threshold scales (from independent shadow constructions);*

2.  *ultraviolet endpoint functional data and unstable-manifold dimension (from an independent AS/FRG shadow);*

3.  *the Barbero–Immirzi parameter and geometric spectra scales (this paper).*

*Consequently these quantities cannot be tuned independently without violating admissibility or leaving the coherent universality class.*

</div>

<div class="proof">

*Proof.* Each shadow construction depends only on projection-induced truncation control, spectral gaps, and stability margins, all encoded by $`\Theta`$. Therefore each derived quantity is a function of $`\Theta`$, and independent tuning would require changing $`\Theta`$, affecting all sectors simultaneously. ◻

</div>

## Falsifiability criteria

The closure yields falsifiability conditions:

1.  If the value of $`\gamma`$ required by black hole entropy or geometric spectra is incompatible with $`\Theta`$ as inferred from collapse thresholds or UV completion, the coherent universality hypothesis is ruled out.

2.  If consistent phenomenology requires independent adjustment of $`\gamma`$ apart from other $`\Theta`$-controlled quantities, closure fails.

3.  If a sector requires parameter ranges that invalidate admissibility in another, the framework is ruled out.

# Conclusions

We have shown that canonical LQG kinematics arises naturally as a shadow of coherent fixed-point dynamics under noninvertible projection: SU(2) connection variables emerge as compact reuse shadows, spin networks encode equivalence classes of coherent configurations, and discrete geometric spectra follow from compact holonomy and gap-controlled truncation. We proved that the Barbero–Immirzi parameter is not a free quantization ambiguity within the coherent universality class but is fixed by bottleneck data $`\Theta`$. Black hole entropy matching is reinterpreted as a consistency condition on admissible coherent microstate counting, not parameter fitting. Finally, cross-sector closure provides sharp falsifiability: $`\gamma`$ is linked to independently testable collapse and UV-completion shadow data through the same $`\Theta`$.

All results are slab-local and admissibility-conditioned: they hold only on bounded-geometry slabs where coherent projection is bounded and stability margins remain positive away from basin boundaries.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255621>

P. Nero, *Modal Triplet Theory: Foundation*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.16949762>

P. Nero, *Fixed Points I–VI: Complete Coherence Spine*, Zenodo preprints, August 2025. <https://doi.org/10.5281/zenodo.16948748>

P. Nero, *The Projection–Admissibility Principle: Structural Constraints on Effective Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255838>

P. Nero, *Closure and Inevitability in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255510>

P. Nero, *Coherence Capacity as the Fundamental Resource of Effective Physics*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255905>

P. Nero, *Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256048>

P. Nero, *Modal Triplet Theory: From MTT to Quantum Mechanics*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.17074246>

P. Nero, *From MTT to Quantum Field Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17068816>

P. Nero, *Modal Triplet Theory: From MTT to General Relativity*, Zenodo preprint, October 2025. <https://doi.org/10.5281/zenodo.16950597>

P. Nero, *Modal Triplet Theory: From MTT to a UV-Finite, Unitary Quantum Gravity*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17077671>

P. Nero, *Measurement as Disturbance and Stabilization in Modal Triplet Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17177404>

P. Nero, *Projection, Probability, and Irreversibility: Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256408>

P. Nero, *Modal Fixed Points, Bell’s Beables, and the Limits of Factorization*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17076300>

P. Nero, *Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory*, Zenodo preprint, August 2025. <https://doi.org/10.5281/zenodo.18208884>

P. Nero, *From Modal Triplet Theory to Indivisible Stochastic Processes: A First-Principles, Fully Rigorous Derivation*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18254862>

</div>
