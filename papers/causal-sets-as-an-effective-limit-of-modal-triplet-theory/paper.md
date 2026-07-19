---
abstract: |
  Causal Set Theory (CST) proposes that spacetime is fundamentally discrete and that its essential structure is encoded in a locally finite partial order representing causal relations. Modal Triplet Theory (MTT), by contrast, posits a continuous underlying modal field whose coherent sector gives rise to effective four–dimensional spacetime, causality, and quantum phenomena through stability and projection. In this work we show that causal sets can arise naturally as an effective, coarse–grained description of the emergent spacetime sector of MTT. In this construction, discreteness and causal order are not postulated at the fundamental level but appear as derived structures when the coherent spacetime is sampled at scales set by modal spectral gaps and admissibility constraints. We present two complementary routes to causal sets: (i) a kinematical construction based on Poisson sprinkling of the emergent MTT spacetime, and (ii) a dynamical construction in which causal set elements correspond to physically meaningful coherence–selection events. We argue that this perspective preserves the successes of CST while providing a deeper explanation for why causal order and discreteness arise at all.
author:
- Peter Nero
current_version: v1.0
date: January 2026
generated_from_main_tex_sha256: d864a54ac8e1155b40ea255663693d4ffe0df0f224743c22355f92035a1c31d9
paper_id: causal-sets-as-an-effective-limit-of-modal-triplet-theory
release_state: zenodo_released
released_version: v1.0
title: "**Causal Sets as an Effective Limit of Modal Triplet Theory**"
zenodo_doi: 10.5281/zenodo.18261498
zenodo_record_id: 18261498
zenodo_url: "https://zenodo.org/records/18261498"
---

# Introduction

Understanding the origin of spacetime structure remains a central challenge in quantum gravity. Causal Set Theory (CST) addresses this challenge by positing that spacetime is fundamentally discrete and that its essential content is captured by a locally finite partially ordered set, where the order relation encodes causal precedence and cardinality encodes spacetime volume. This approach achieves background independence and maintains Lorentz invariance in a statistical sense, but it does so by elevating causal order and discreteness to axiomatic status.

Modal Triplet Theory (MTT) approaches the same foundational problem from a different direction. Rather than assuming spacetime or causal structure as fundamental, MTT posits a continuous modal field defined on a higher–dimensional structured arena and identifies observable four–dimensional spacetime as a stable, coherent projection of that field. In MTT, causality, locality, and the arrow of time are emergent properties associated with stability, damping, and admissibility of coherent configurations.

At first glance, CST and MTT appear philosophically opposed: CST rejects the continuum at the fundamental level, while MTT recovers the continuum as an emergent structure. The aim of this paper is to show that this opposition is only apparent. We argue that CST can be understood as an effective description of the emergent spacetime sector of MTT, valid at scales where modal structure enforces an effective discreteness. In this sense, CST captures genuine features of physical spacetime, but those features need not be fundamental.

This paper does not attempt to derive the full dynamical growth models of CST from MTT. Rather, it establishes a principled route by which causal sets arise as coarse–grained encodings of MTT coherence, clarifying the conceptual status of causal order and discreteness.

# Minimal Overview of Modal Triplet Theory

Modal Triplet Theory posits a single underlying physical entity: a modal field defined on a ten–dimensional structured arena
``` math
M_{10} = Y^{4} \times X^{6},
```
where $`Y^{4}`$ is the effective spacetime manifold and $`X^{6}`$ is a finite, closed modal geometry associated with each spacetime point. The six modal directions are organized into three mutually commuting filter bundles, each equipped with a Laplace–type operator. The defining mathematical feature of this structure is that the corresponding spectral projectors commute, allowing a well–defined joint coherent projector $`\Pi_{\mathrm{coh}}`$.

The dynamics of the modal field consist of local evolution, including damping and disturbance, combined with projection onto the coherent sector. The latter retains only those configurations that are jointly harmonic with respect to all three modal filters. A central result of MTT is the *Fundamental Contractivity Condition* (FCC), which ensures that under suitable bounds on disturbance and damping, the combined evolve–project map is contractive on the admissible set. This yields a unique coherent regime toward which all admissible configurations relax.

Crucially, the coherent regime admits an effective four–dimensional description. In this projected sector, a Lorentzian spacetime metric emerges as an elastic response of the modal field, quantum phenomena arise from finite–width off–diagonal modal fluctuations, and causality appears as a property of retarded propagation in the effective spacetime. None of these structures are fundamental; all are consequences of stability and admissibility in the underlying modal dynamics.

# Minimal Overview of Causal Set Theory

Causal Set Theory is based on the proposal that spacetime is fundamentally a causal set $`(C,\prec)`$, where $`C`$ is a set of elementary events and $`\prec`$ is a partial order satisfying transitivity, acyclicity, and local finiteness. The order relation encodes causal precedence, while the number of elements in a region approximates its spacetime volume. In the continuum approximation, Lorentzian geometry is recovered from the combination of order and counting.

A key technical tool in CST is Poisson sprinkling: points are randomly selected in a Lorentzian manifold at a fixed density, and the induced causal relations define a causal set. This construction preserves Lorentz invariance statistically and provides a concrete link between causal sets and continuum spacetimes. Within CST, however, the discreteness scale and the sprinkling procedure are typically taken as fundamental inputs rather than derived quantities.

CST has achieved notable success in clarifying how causal structure can replace metric structure at the foundational level. Nonetheless, it leaves open the question of why spacetime should be discrete and why causal order should be fundamental rather than emergent.

# From Modal Coherence to Causal Order

A central conceptual difference between MTT and CST concerns the status of causality. In CST, causal order is fundamental: the partial order $`\prec`$ is taken as the primitive structure from which geometry is recovered. In MTT, causality is not assumed at the fundamental level but emerges as a property of the coherent sector after projection.

In MTT, the underlying modal field evolves on $`M_{10}`$ according to well–posed local dynamics that include damping and disturbance. When restricted to the coherent sector selected by the joint projector $`\Pi_{\mathrm{coh}}`$, the effective dynamics on the projected spacetime $`Y^{4}`$ are governed by hyperbolic (or hyperbolic–dominated) equations with retarded Green functions. As a result, influence propagates within light cones defined by the emergent metric $`g_{\mu\nu}`$. Causal structure is therefore induced by stability of the coherent projection rather than postulated.

Two consequences follow. First, causal order in MTT is contingent: it exists only insofar as the coherent spacetime description remains valid. In regions where admissibility fails, the effective causal description breaks down even though the underlying modal dynamics remain well defined. Second, causal order is directional: the arrow of time is determined by the direction of contractive flow guaranteed by the FCC.

From the perspective of CST, this suggests a reinterpretation of the partial order $`\prec`$ as encoding the retarded influence relations of a stable coherent spacetime that has already emerged from deeper modal dynamics.

# Kinematical Construction of a Causal Set from MTT

We now present a concrete construction by which a causal set arises as an effective description of an MTT coherent spacetime.

## Emergent spacetime and discreteness scale

Let $`(Y^{4}, g)`$ denote a spacetime arising as the coherent projection of an admissible MTT configuration. The coherent sector is characterized by finite spectral gaps associated with the modal filters. These gaps define a natural ultraviolet scale $`\ell`$, below which excitations are suppressed and above which the continuum description is valid.

We therefore identify $`\ell`$ as an effective discreteness scale, determined dynamically by modal spectral data rather than imposed by hand.

## Sprinkling and induced order

Given $`(Y^{4}, g)`$ and scale $`\ell`$, define a causal set $`(C,\prec)`$ by choosing a Poisson sprinkling of points in $`Y^{4}`$ with density $`\rho \sim \ell^{-4}`$. For any two sprinkled points $`x,y \in C`$, define
``` math
x \prec y \quad \text{if and only if} \quad x \in J^{-}(y),
```
where $`J^{-}(y)`$ is the causal past of $`y`$ with respect to the metric $`g`$.

This construction yields a locally finite partially ordered set. Counting elements approximates spacetime volume, while the partial order encodes the causal structure of $`(Y^{4}, g)`$. Thus the standard kinematical content of CST is recovered.

## Interpretation

Within MTT, this causal set is not fundamental. It is a discrete encoding of an already–emergent spacetime geometry, valid at scales where modal coherence suppresses finer structure. The randomness of the sprinkling reflects coarse–graining rather than intrinsic indeterminacy.

# Selection–Event Causal Sets

MTT also suggests a more intrinsic route to causal sets that does not rely on arbitrary sampling.

## Selection events

Physically significant changes in MTT occur when the system undergoes local coherence selection, such as measurement–like interactions, horizon crossings, or strong disturbances forcing re–projection into a new admissible basin. We refer to these occurrences as *selection events*. Selection events are localized in the emergent spacetime and associated with irreversible stabilization.

## Event–based causal sets

Define a causal set $`(C_{\mathrm{sel}},\prec)`$ by taking elements to be selection events and ordering them by causal precedence in the emergent spacetime. Local finiteness follows from admissibility: selection events cannot accumulate arbitrarily densely without violating stability margins.

This construction yields a causal set whose elements correspond to physically meaningful transitions rather than abstract spacetime points.

## Advantages

Selection–event causal sets provide a natural physical interpretation of causal set elements and suggest a direct link between causal structure and quantum measurement.

# Discreteness as a Derived Feature

In both constructions above, discreteness arises as a consequence of stability rather than as a primitive assumption. Closed modal fibers and spectral gaps enforce a finite resolution of spacetime structure. Causal sets therefore emerge as effective discrete encodings of a deeper continuous dynamics.

# Discussion and Outlook

We have shown that causal sets can arise naturally as effective descriptions of the emergent spacetime sector of Modal Triplet Theory. The kinematical content of CST is recovered by coarse–graining coherent spacetime at the modal gap scale, while a selection–event construction offers a physically grounded interpretation of causal set elements.

This work does not derive CST growth dynamics from MTT but clarifies the conceptual relationship between the two frameworks. CST captures genuine structural features of spacetime, while MTT explains why such features arise. Future work may explore whether specific classes of CST dynamics correspond to admissible modal evolutions.

From this perspective, Modal Triplet Theory does not compete with Causal Set Theory but subsumes it as an effective layer, with causal order and discreteness emerging because coherence demands them.

<div class="thebibliography">

9

L. Bombelli, J. Lee, D. Meyer, and R. D. Sorkin, Space–time as a causal set, , 59(5):521–524, 1987.

R. D. Sorkin, Causal sets: Discrete gravity, in *Lectures on Quantum Gravity*, Springer, 2003.

P. Nero, Modal Triplet Theory: Foundations and Fixed–Point Structure, preprint / manuscript, 2025.

</div>
