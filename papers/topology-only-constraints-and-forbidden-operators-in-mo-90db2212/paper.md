---
abstract: |
  We derive a Tier–1 layer of predictions in Modal Triplet Theory (MTT) using topology and admissibility alone, without invoking renormalization group flow, collapse dynamics, or spectral actions. Matter fields are modeled as globally admissible sections of overlap bundles formed from three internal bundles. This immediately quantizes hypercharge on a discrete lattice determined by integral cohomology, forbids anomalous representations as topological obstructions in determinant line bundles, and excludes broad classes of baryon- and lepton-number violating operators (including leading proton decay operators) as globally inadmissible bundle products. We also obtain topological constraints on neutrino mass terms: Majorana masses require a global real structure on the relevant overlap bundle. These results supply early falsifiability criteria independent of Planck-scale dynamics. All statements are slab-local and admissibility-conditioned, but require no dynamics beyond global definability of overlap sections.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 6b499ecf6a39c5ab945542e7ca01cf2863157ebcd20d8c5d3dd9761923c7823b
paper_id: topology-only-constraints-and-forbidden-operators-in-mo-90db2212
release_state: zenodo_released
released_version: v1.0
title: |
  **Topology-Only Constraints and Forbidden Operators in Modal Triplet Theory**  
  Anomaly cancellation, hypercharge quantization, and early falsifiability from overlap bundles
zenodo_doi: 10.5281/zenodo.18261774
zenodo_record_id: 18261774
zenodo_url: "https://zenodo.org/records/18261774"
---

# Introduction

A fundamental theory should exclude inconsistent effective descriptions as early as possible. In practice, many constraints in particle physics are often presented as dynamical results or as consequences of postulated symmetries (e.g. GUT symmetries or discrete parities). This paper isolates a stricter layer: *topology-only* constraints that arise before dynamics, renormalization, or collapse physics enter.

In Modal Triplet Theory (MTT), observable matter degrees of freedom arise in the coherent sector as admissible overlap channels between three internal bundles. The requirement that these overlaps be globally well-defined immediately constrains charges, representations, and operators. We show that:

- Hypercharge is quantized on a discrete lattice fixed by integral cohomology classes of overlap bundles (Sec. <a href="#sec:hypercharge" data-reference-type="ref" data-reference="sec:hypercharge">3</a>);

- Anomalous representations are forbidden because anomaly bundles fail to trivialize globally (Sec. <a href="#sec:anomalies" data-reference-type="ref" data-reference="sec:anomalies">4</a>);

- Many baryon/lepton violating operators are forbidden by global bundle inconsistency independently of coupling strength (Sec. <a href="#sec:forbidden_ops" data-reference-type="ref" data-reference="sec:forbidden_ops">5</a>);

- Majorana masses are allowed only when a global real structure exists on the relevant overlap bundle (Sec. <a href="#sec:neutrino" data-reference-type="ref" data-reference="sec:neutrino">6</a>).

These constitute early falsifiability conditions: if an observed charge assignment or operator requires a globally inadmissible bundle, the coherent-sector framework is ruled out, independently of Planck-scale physics.

# Minimal Topological Inputs and Admissibility

## Slab-locality

<div id="ass:slab" class="assumption">

**Assumption 1** (Slab-local admissible regime). All statements are made on bounded-geometry slabs $`\Omega=[0,T]\times\Sigma`$ where coherent projection is defined and bounded. Topological statements refer to the topology of the spatial slice $`\Sigma`$ (or of regions of $`\Sigma`$) and to globally defined bundles on it.

</div>

## Internal bundles and overlap bundles

We assume three internal bundles $`B_1,B_2,B_3`$ over $`Y_4`$, and consider the induced bundle data restricted to spatial slices $`\Sigma`$. The only structure used here is that matter fields correspond to globally admissible overlap sections constructed from $`B_i`$ and their duals.

<div id="ass:global_overlap" class="assumption">

**Assumption 2** (Globally admissible overlaps). Admissible matter fields correspond to globally defined sections of overlap bundles formed from tensor products of $`B_1,B_2,B_3`$ and their duals. Local patching without a global section is not admissible.

</div>

<div class="definition">

**Definition 3** (Overlap bundle). An *overlap bundle* is any bundle of the form
``` math
\mathcal{E}=\bigotimes_{i=1}^3 B_i^{\otimes n_i}\otimes (B_i^\ast)^{\otimes m_i},
```
for integers $`n_i,m_i\ge 0`$, equipped with the induced connection. A matter field is admissible only if it is a globally defined section of $`\mathcal{E}`$.

</div>

<div class="remark">

*Remark 4*. This paper treats the overlap-bundle picture as an abstract admissibility principle. No specific internal geometry is needed; only global definability and integral cohomology.

</div>

# Hypercharge Quantization from Bundle Topology

In this section we show that hypercharge assignments are quantized by topology alone.

## U(1) charges as line-bundle holonomy weights

Hypercharge is modeled as a U(1) weight associated with a complex line bundle $`L_Y`$ whose connection defines holonomy phases on closed loops.

<div class="definition">

**Definition 5** (Hypercharge weight). Let $`L_Y\to \Sigma`$ be the U(1) line bundle associated with hypercharge. A field of hypercharge $`q_Y\in\mathbb{Q}`$ transforms by the representation
``` math
\mathrm{Hol}_{L_Y}(\gamma)\mapsto \exp(i q_Y \theta(\gamma))
```
for loops $`\gamma`$ with holonomy angle $`\theta(\gamma)`$.

</div>

## Quantization theorem

<div id="thm:hypercharge" class="theorem">

**Theorem 6** (Hypercharge quantization). *Assume <a href="#ass:global_overlap" data-reference-type="ref" data-reference="ass:global_overlap">2</a>. Then admissible hypercharge assignments lie in a discrete lattice $`\Lambda_Y\subset\mathbb{Q}`$ determined by integral cohomology:
``` math
q_Y \in \Lambda_Y \quad\text{where}\quad \Lambda_Y = \left\{\frac{n}{N_0}: n\in\mathbb{Z}\right\}
```
for some integer $`N_0\ge 1`$ determined by the primitive generator(s) of $`H^2(\Sigma,\mathbb{Z})`$ and by the overlap-bundle construction. Charges outside $`\Lambda_Y`$ are topologically inadmissible.*

</div>

<div class="proof">

*Proof.* A U(1) gauge field on $`\Sigma`$ is a connection on a line bundle $`L_Y`$ with $`c_1(L_Y)\in H^2(\Sigma,\mathbb{Z})`$. For a field of charge $`q_Y`$, the associated bundle is $`L_Y^{\otimes q_Y}`$. Global definability requires that the holonomy around any loop be single-valued, equivalently that the Chern class of the charged bundle be integral. Thus $`q_Y c_1(L_Y)\in H^2(\Sigma,\mathbb{Z})`$. If $`c_1(L_Y)`$ is primitive, this forces $`q_Y\in \frac{1}{N_0}\mathbb{Z}`$ for some $`N_0`$. Overlap bundles built from $`B_i`$ restrict $`N_0`$ further but cannot make $`\Lambda_Y`$ dense. ◻

</div>

<div class="remark">

*Remark 7*. This yields hypercharge quantization without invoking grand unification or anomaly cancellation. Anomaly cancellation becomes an additional consistency condition (Sec. <a href="#sec:anomalies" data-reference-type="ref" data-reference="sec:anomalies">4</a>), but the lattice already exists pre-dynamically.

</div>

# Anomaly Cancellation as a Pre-Dynamical Constraint

Gauge and mixed anomalies correspond to obstructions to defining fermion determinants as globally consistent sections of determinant line bundles.

## Determinant line bundles and obstructions

<div class="definition">

**Definition 8** (Determinant line bundle). Given a chiral fermion bundle $`\mathcal{E}\to\Sigma`$, the determinant line bundle $`\det \mathcal{E}`$ is the line bundle whose local trivializations encode the fermion measure phase. A gauge anomaly corresponds to the nontriviality of $`\det \mathcal{E}`$ as a gauge-equivariant line bundle.

</div>

<div class="definition">

**Definition 9** (Anomalous representation). A representation is *anomalous* if the associated determinant line bundle fails to admit a global trivialization compatible with gauge transformations.

</div>

## Topological anomaly forbiddance

<div id="thm:anomaly" class="theorem">

**Theorem 10** (Topology-forbidden anomalies). *Assume <a href="#ass:global_overlap" data-reference-type="ref" data-reference="ass:global_overlap">2</a>. Any gauge, mixed, or gravitational anomaly corresponds to a nontrivial obstruction class in a determinant line bundle built from overlap bundles and is therefore topologically inadmissible. Hence anomalous representations are excluded before dynamics is specified.*

</div>

<div class="proof">

*Proof.* By Assumption <a href="#ass:global_overlap" data-reference-type="ref" data-reference="ass:global_overlap">2</a>, admissible fermions must be globally defined overlap sections. The fermion measure is a section of the corresponding determinant line bundle. If the determinant bundle is nontrivial (or not trivialisable gauge-equivariantly), there is no globally consistent measure, contradicting admissibility. Thus representations that would generate anomalies are excluded by the absence of a global trivialization. ◻

</div>

<div class="remark">

*Remark 11*. This reinterprets anomaly cancellation as an admissibility filter: the Standard Model’s anomaly cancellation is a reflection of topological consistency, not a dynamical coincidence.

</div>

# Topology-Forbidden Operators

Effective field theory allows many operators compatible with local gauge symmetry. In the overlap-bundle framework, operators must correspond to globally defined sections of the tensor product bundle formed from their constituent fields.

## Operator admissibility

<div class="definition">

**Definition 12** (Admissible operator). Let fields $`\psi_a`$ be sections of overlap bundles $`\mathcal{E}_a`$. An operator $`\mathcal{O}=\prod_a \psi_a`$ is *admissible* only if the tensor product bundle $`\bigotimes_a \mathcal{E}_a`$ admits a global section (equivalently is globally consistent with the overlap admissibility constraints).

</div>

## Baryon/lepton violating operators

Consider standard dimension-5 proton decay operators schematically
``` math
QQQL,\qquad u^c u^c d^c e^c,
```
whose existence in generic EFTs leads to rapid proton decay unless suppressed.

<div id="thm:proton" class="theorem">

**Theorem 13** (Topology-forbidden B/L violation). *Assume <a href="#ass:global_overlap" data-reference-type="ref" data-reference="ass:global_overlap">2</a> and Theorem <a href="#thm:hypercharge" data-reference-type="ref" data-reference="thm:hypercharge">6</a>. Operators whose constituent bundles combine into a tensor product carrying a nontrivial obstruction class (e.g. nonintegral hypercharge, incompatible overlap holonomy, or nontrivial determinant obstruction) are inadmissible. In particular, the leading baryon- and lepton-number violating operators are forbidden whenever their bundle product fails to admit a global section, independently of coupling strength.*

</div>

<div class="proof">

*Proof.* Each fermion field is a section of an overlap bundle whose U(1) charge lies in the lattice $`\Lambda_Y`$. The operator $`\mathcal{O}`$ corresponds to a section of the product bundle $`\bigotimes_a \mathcal{E}_a`$. For $`QQQL`$ and $`u^c u^c d^c e^c`$, the hypercharge and nonabelian representation content require the product bundle to be gauge-trivial and globally defined. If the corresponding Chern classes or obstruction classes are nontrivial, no global section exists and the operator is inadmissible by definition. This forbiddance is topological and does not depend on any dynamical suppression. ◻

</div>

<div class="remark">

*Remark 14*. This provides a pre-dynamical explanation for proton stability: forbidden operators are excluded by global consistency rather than by fine-tuned small coefficients.

</div>

# Neutrino Mass Structure

Neutrino masses are sensitive probes of admissibility because Majorana masses require a global real structure on the relevant bundle.

## Majorana admissibility

<div class="definition">

**Definition 15** (Majorana admissibility). A Majorana mass term is admissible only if the overlap bundle supporting the neutrino field admits a global real (or pseudo-real) structure compatible with the coherent projector, allowing a gauge-invariant identification of the field with its charge conjugate.

</div>

<div id="prop:neutrino" class="proposition">

**Proposition 16** (Topology-constrained neutrino masses). *Assume <a href="#ass:global_overlap" data-reference-type="ref" data-reference="ass:global_overlap">2</a>. Majorana mass terms are admissible only if the relevant overlap bundle admits a global real structure; otherwise Majorana bilinears fail to define global sections and are inadmissible. In that case neutrino masses must be Dirac or arise from higher-order admissible operators.*

</div>

<div class="proof">

*Proof.* A Majorana bilinear is a section of $`\mathcal{E}\otimes \mathcal{E}`$, identified with a scalar only if $`\mathcal{E}`$ admits a real structure compatible with charge conjugation. If no such structure exists globally, the bilinear cannot be made gauge-invariant and globally defined. By Assumption <a href="#ass:global_overlap" data-reference-type="ref" data-reference="ass:global_overlap">2</a>, such a term is inadmissible. ◻

</div>

<div class="remark">

*Remark 17*. This provides an early discriminator between neutrino mass models without using RG or dynamics: Majorana masses require a topological condition, not merely the absence of a symmetry.

</div>

# Comparison with EFT and GUT Approaches

Effective field theory allows all operators compatible with local gauge symmetry, typically suppressing unwanted terms by high scales or additional symmetries. Grand unification forbids operators by embedding the Standard Model into a larger symmetry group.

By contrast, the overlap-bundle admissibility principle forbids operators by global consistency: if the corresponding bundle product has no global section, the operator is absent regardless of scale. This mechanism can reproduce many selection-rule effects often attributed to GUT symmetries without requiring a larger gauge group.

# Early Falsifiability Criteria

Topology-only constraints provide early falsifiability channels:

1.  **Hypercharge lattice violation:** any observed charge outside $`\Lambda_Y`$ falsifies the overlap-bundle admissibility framework.

2.  **Anomalous representation:** any required anomalous representation violates Theorem <a href="#thm:anomaly" data-reference-type="ref" data-reference="thm:anomaly">10</a>.

3.  **Observed forbidden operator:** observation of an operator whose associated bundle product lacks a global section falsifies the framework.

4.  **Neutrino mass inconsistency:** evidence requiring a Majorana mass term when no global real structure exists falsifies admissibility.

These criteria are independent of Planck-scale dynamics and apply in any slab-local coherent regime.

# Relation to Other Shadow Papers

This topology-only paper sits beneath all shadow-bridge papers in the program: collapse/measurement thresholds, causal-set event structure, AS/FRG UV endpoints, LQG kinematics, and NCG spectral action all presuppose admissible overlap-bundle consistency. Therefore any failure of the topology-only layer rules out the later shadow constructions automatically.

Conversely, agreement of later shadow constructions across sectors (cross-sector closure) provides additional indirect validation of the same topological admissibility constraints.

# Conclusions

We have derived a Tier–1 layer of constraints in Modal Triplet Theory using topology and admissibility alone. Hypercharge quantization follows from integral cohomology of overlap line bundles. Anomalous representations are excluded as determinant-bundle obstructions. Broad classes of baryon- and lepton-number violating operators are forbidden by global inconsistency of the associated bundle products. Neutrino mass terms are topologically constrained: Majorana masses require a global real structure on the relevant overlap bundle.

These results provide early falsifiability criteria independent of Planck-scale dynamics and independent of the specific details of coherent-sector evolution. All statements are slab-local and admissibility-conditioned, but require no dynamical inputs beyond global definability.

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
