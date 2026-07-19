---
abstract: |
  Topological phases of matter exhibit robustness, quantized response, and protected boundary modes that are not explained by local symmetry breaking or microscopic Hamiltonian details. We present a structural account of topological phases based on coarse–grained projection and global admissibility of local effective descriptions. We show that phases correspond to admissible basins of coarse–grained dynamics, and that topological phases arise precisely when locally well–defined effective descriptions fail to admit a globally consistent completion. Topological invariants appear as obstruction classes of overlap structures, explaining quantization and robustness. Bulk–boundary correspondence follows inevitably: boundary modes arise as compensating degrees of freedom required to restore local consistency at interfaces. The framework applies equally to interacting and disordered systems with a spectral gap or mobility gap and does not rely on band topology or free–fermion assumptions.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 82c2bdfbe0379a4ff08385b67f1393f95256251bf18545d22d1898c34033fc1d
paper_id: topological-phases-of-matter-as-admissible-overlap-stru-837dec46
release_state: zenodo_released
released_version: v1.0
title: |
  **Topological Phases of Matter as Admissible Overlap Structures**  
  A projection–based account of robustness and bulk–boundary correspondence
zenodo_doi: 10.5281/zenodo.18261859
zenodo_record_id: 18261859
zenodo_url: "https://zenodo.org/records/18261859"
---

# Introduction

Topological phases of matter are distinguished by properties that are insensitive to local perturbations, disorder, and microscopic details. These include quantized transport coefficients, robust degeneracies, and protected edge or surface modes. Unlike conventional phases, these features do not arise from symmetry breaking or local order parameters.

Standard explanations invoke band topology, Berry curvature, or long–range entanglement. While powerful, these descriptions are often model–specific and do not clearly explain *why* topological protection is inevitable or why bulk and boundary phenomena are universally linked.

In this work we provide a structural explanation. We show that topological phases arise because only certain global overlap structures of coarse–grained effective descriptions are admissible. Topological invariants encode global consistency constraints, and protected boundary modes appear when these constraints fail at interfaces.

# Minimal Structural Assumptions

We work entirely at the level of effective condensed–matter descriptions.

<div id="ass:locality" class="assumption">

**Assumption 1** (Locality and stability). The system admits a local description and possesses either a spectral gap or a mobility gap ensuring stability under small local perturbations.

</div>

<div id="ass:projection" class="assumption">

**Assumption 2** (Coarse–grained projection). There exists a coarse–grained projection from microscopic degrees of freedom to effective degrees of freedom capturing stable low–energy physics.

</div>

<div id="ass:local_eff" class="assumption">

**Assumption 3** (Local effective descriptions). On sufficiently small regions of space, the projected system admits a consistent local effective description stable under perturbations.

</div>

No assumption is made about noninteracting particles, translational symmetry, or specific lattice Hamiltonians.

# Phases as Admissible Basins

<div class="definition">

**Definition 1** (Admissible basin). An admissible basin is a region of the effective state space that is stable under the projected dynamics and under small local perturbations.

</div>

<div id="thm:phases" class="theorem">

**Theorem 1** (Phase inevitability). *Any system satisfying Assumptions <a href="#ass:locality" data-reference-type="ref" data-reference="ass:locality">1</a>–<a href="#ass:local_eff" data-reference-type="ref" data-reference="ass:local_eff">3</a> decomposes into admissible basins corresponding to phases of matter.*

</div>

<div class="proof">

*Proof.* Without such basins, arbitrarily small perturbations would destabilize macroscopic properties, contradicting observed phase stability. Coarse–grained projection selects stable regions of effective state space, which define phases. ◻

</div>

Conventional symmetry–breaking phases correspond to basins related by symmetry. Topological phases correspond to basins distinguished by global constraints.

# Topological Phases as Global Admissibility Constraints

We now give a structural characterization of topological phases.

## Local effective descriptions and overlaps

Let $`\Sigma`$ be the spatial manifold. Cover $`\Sigma`$ by overlapping regions $`\{U_\alpha\}`$. On each $`U_\alpha`$, the system admits a local effective Hilbert space $`\mathcal{H}_\alpha`$ and observable algebra $`\mathcal{A}_\alpha`$.

<div class="definition">

**Definition 2** (Overlap maps). On overlaps $`U_\alpha\cap U_\beta`$, an overlap map
``` math
\phi_{\alpha\beta} : \mathcal{H}_\alpha|_{U_\alpha\cap U_\beta}
\longrightarrow
\mathcal{H}_\beta|_{U_\alpha\cap U_\beta}
```
identifies the two local descriptions. The overlap maps are required to preserve the local observable algebra and its adjoint structure up to admissible equivalence.

</div>

## Global admissibility

<div id="def:global_admissibility" class="definition">

**Definition 3** (Global admissibility). A collection $`\{\mathcal{H}_\alpha,\phi_{\alpha\beta}\}`$ is globally admissible if the overlap maps satisfy the cocycle condition
``` math
\phi_{\alpha\beta}\circ\phi_{\beta\gamma}\circ\phi_{\gamma\alpha}=\mathrm{Id}
```
on all triple overlaps.

</div>

## Topological obstruction

<div id="thm:topo_phase" class="theorem">

**Theorem 2** (Topological phase criterion). *A phase is topological if and only if, under the locality and gap assumptions stated in Section 2, its locally admissible effective descriptions fail to admit a globally admissible completion, with the failure classified by a nontrivial topological obstruction.*

</div>

<div class="proof">

*Proof.* If a globally admissible completion exists, the phase can be continuously deformed to a trivial phase without closing the gap. If no such completion exists, the failure is measured by a topological obstruction class that cannot change under continuous local perturbations. ◻

</div>

<div class="proposition">

**Proposition 1** (Quantization of invariants). *Topological obstruction classes take values in discrete sets determined by the topology of $`\Sigma`$ and the structure of overlap maps.*

</div>

<div class="proof">

*Proof.* Obstruction classes live in integral cohomology or K–theory groups, which are discrete. Continuous perturbations cannot change them without violating local admissibility. ◻

</div>

# Robustness Under Disorder and Perturbations

<div class="proposition">

**Proposition 2** (Robustness of topological phases). *Topological phases are robust under all local perturbations that preserve local admissibility and the gap or mobility gap.*

</div>

<div class="proof">

*Proof.* Local perturbations deform overlap maps locally but cannot remove a global obstruction without closing the gap or violating admissibility. ◻

</div>

This explains robustness to disorder and interactions.

# Bulk–Boundary Correspondence

Let $`\Sigma_{\mathrm{bulk}}\subset\Sigma`$ support a topological phase and let $`\partial\Sigma_{\mathrm{bulk}}`$ denote its boundary with a trivial phase.

<div id="thm:bulk_boundary" class="theorem">

**Theorem 3** (Bulk–boundary correspondence). *If the bulk phase carries a nontrivial global admissibility obstruction, then there necessarily exist boundary–localized modes whose role is to restore local overlap consistency at $`\partial\Sigma_{\mathrm{bulk}}`$. These modes are protected against all perturbations preserving locality and the bulk gap or mobility gap.*

</div>

<div class="proof">

*Proof.* The bulk obstruction prevents global gluing of overlap maps. At the boundary, local admissibility must still hold. This requires additional boundary degrees of freedom to compensate for the obstruction. Because the obstruction is topological, these modes cannot be removed without closing the gap. ◻

</div>

<div class="corollary">

**Corollary 1**. *If the bulk phase is globally admissible (topologically trivial), no protected boundary modes are required.*

</div>

<div class="remark">

*Remark 1*. This formulation applies equally to interacting, disordered, and superconducting systems and does not rely on single–particle band topology.

</div>

# Relation to Known Topological Phases

The framework recovers known results:

- Chern insulators: obstruction is the first Chern class.

- $`\mathbb{Z}_2`$ topological insulators: time–reversal–protected obstruction.

- Topological superconductors: real–structure obstruction yields Majorana modes.

- Interacting topological order: the obstruction no longer resides in single-particle bundles but in the global consistency data of the emergent operator algebra, generalizing overlap maps to tensor-categorical fusion and braiding structures.

The unifying feature is global admissibility, not microscopic detail.

# Scope and Limitations

The analysis applies to systems with a spectral gap or mobility gap. Gap closing corresponds to basin boundary crossing and signals phase transitions. The framework does not claim to classify all possible exotic phases, but explains the structural origin of topological protection where it exists.

# Conclusions

We have shown that topological phases of matter arise as admissible overlap structures of coarse–grained effective descriptions. Topological invariants measure global consistency obstructions, explaining quantization and robustness. Bulk–boundary correspondence follows inevitably: protected boundary modes arise to restore local consistency at interfaces.

This perspective unifies band topology, interacting topological order, disorder robustness, and bulk–boundary correspondence within a single structural framework and clarifies why topological phases are both rare and exceptionally stable.

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
