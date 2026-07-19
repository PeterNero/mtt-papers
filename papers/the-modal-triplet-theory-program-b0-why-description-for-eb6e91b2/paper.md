---
abstract: |
  We classify the possible ways in which global coherence can fail in any theory that admits local reduced descriptions with overlap consistency and identity persistence. Working purely at the structural level and without assuming geometry, bundles, dynamics, or dimensionality, we show that there exist exactly three and only three obstruction types: loop inconsistency (circle), redundancy of representation (lens), and failure of representability (nil). These obstructions are exhaustive and mutually irreducible.

  We further demonstrate that any realization capable of supporting all three obstruction types simultaneously in a stable and non-degenerate manner must exhibit a tri-layer overlap structure. When combined with continuity and kinematic persistence requirements, the minimal such realization is equivalent, up to admissible re-encoding, to a ten-dimensional configuration space composed of a four-dimensional effective base and three independent internal layers. Geometry and bundle structure are shown to arise as the minimal bookkeeping framework required to encode circle, lens, and nil consistently, rather than as fundamental axioms.

  This work provides the missing classification link between the structural core of Modal Triplet Theory and its encoding-class and realization papers, explaining why gravity, gauge redundancy, and termination of description are inevitable structural responses to local describability and global obstruction.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 59d38668889be0238e068f7b2f021792f5be47a83a2aaf596748c21864fe96b4
paper_id: the-modal-triplet-theory-program-b0-why-description-for-eb6e91b2
release_state: zenodo_released
released_version: v1.0
title: |
  The Modal Triplet Theory Program B0:  
  Why Description Forces Circle, Lens, and Nil  
  and Why the Minimal Continuous Realization Is Ten-Dimensional
zenodo_doi: 10.5281/zenodo.18354990
zenodo_record_id: 18354990
zenodo_url: "https://zenodo.org/records/18354990"
---

# Introduction and Scope

The structural core of Modal Triplet Theory establishes general conditions under which reduced descriptions exist, how such descriptions relate on overlaps, and why no single global reduced description can exist. These results are formulated abstractly, in terms of projection, admissibility, and identity persistence, and make no assumptions about geometry, spacetime, bundles, gauge structure, or dimensionality.

However, once local describability and global obstruction are taken seriously, a natural question arises: *what forms of failure of global coherence are actually possible, and why do the same geometric and gauge-like structures appear so universally across effective physical theories?* The purpose of the present paper is to answer this question at the level of structural classification.

We show that the failure of global coherence in a locally describable system admits an exhaustive and minimal classification. Any such failure must appear as one of three distinct types: inconsistency detected only around closed overlap chains (circle), non-uniqueness of local representation without contradiction (lens), or complete loss of representability (nil). No fourth obstruction type is possible under the assumptions of local describability and overlap consistency.

Having classified the obstruction types, we then address the question of realization. We ask: *what minimal kind of structure can support all three obstructions simultaneously, without degenerating one into another?* We show that a tri-layer overlap architecture is the minimal solution. Furthermore, when continuity and kinematic persistence are required, this tri-layer structure admits a minimal continuous realization equivalent, up to admissible re-encoding, to a ten-dimensional configuration space.

Throughout this work, geometry and bundle structure are treated not as fundamental inputs but as emergent bookkeeping frameworks forced by the need to encode overlap consistency, redundancy, and termination of description. The results of this paper therefore do not postulate gravity, gauge symmetry, or dimensionality; instead, they explain why these structures arise inevitably once local description and global obstruction are both present.

<div class="remark">

*Remark 1* (Relation to the series). This paper depends only on the structural core of Modal Triplet Theory and its kinematic interpretation of persistence across admissible overlaps. It precedes and motivates the encoding-class papers on gravity, gauge structure, quantization, and unified encodings, as well as the realization paper on geometric and bundle models. No realization-specific assumptions are used in the classification arguments presented here.

</div>

# Structural Assumptions and Global Coherence

In this section we state explicitly the structural assumptions imported from the core of Modal Triplet Theory and clarify what is meant by global coherence and its failure. No geometric, topological, or dynamical assumptions are introduced.

## Local describability

<div class="assumption">

**Assumption 2** (Local describability). There exists a collection of admissible domains $`\{A_\alpha\}`$ covering the region of interest such that on each $`A_\alpha`$ a reduced description is well-defined. Equivalently, there exist local encodings
``` math
\mathcal E_\alpha = (A_\alpha, Z_\alpha, E_\alpha, \ldots)
```
with associated local sections selecting representatives of coherent structure.

</div>

Local describability asserts only that reduced descriptions exist *locally*; it does not assume the existence of any globally valid reduced description.

## Overlap consistency

<div class="assumption">

**Assumption 3** (Overlap consistency). On any nonempty overlap $`A_{\alpha\beta} := A_\alpha \cap A_\beta`$, the corresponding local encodings are related by admissible re-encoding maps
``` math
f_{\alpha\beta} : Z_\alpha \to Z_\beta
```
that preserve coherent content up to admissible equivalence.

</div>

Overlap consistency ensures that different local descriptions of the same underlying coherent structure do not contradict one another on shared domains.

## Identity persistence

<div class="assumption">

**Assumption 4** (Identity persistence). If a coherent structure is representable on a chain of overlapping admissible domains, then its identity can be tracked consistently across that chain, up to admissible re-encoding equivalence.

</div>

This assumption underlies the kinematic notion of persistence developed in the coherent kinematics paper. It does not assume trajectories, spacetime, or equations of motion; it requires only that “being the same” is a meaningful notion locally.

## Finite admissibility and global obstruction

<div class="assumption">

**Assumption 5** (Finite admissibility). There exists no single admissible domain that covers the entire region of interest. Equivalently, no global section of the reduced description exists.

</div>

Finite admissibility is the structural statement that global coherence is generically obstructed. It is not a statement about experimental limitation or lack of information, but a property of the reduced description itself.

## Global coherence

We now formalize the notion whose failure we seek to classify.

<div class="definition">

**Definition 6** (Global coherence). A system is said to admit global coherence if there exists a single reduced encoding $`\mathcal E = (A, Z, E, \ldots)`$ with $`A`$ equal to the entire region of interest, such that all local descriptions arise as restrictions of $`\mathcal E`$.

</div>

Global coherence therefore requires the existence of a global section compatible with all local encodings and all overlap relations.

<div class="definition">

**Definition 7** (Failure of global coherence). Failure of global coherence occurs when local describability and overlap consistency hold, but no such global encoding exists.

</div>

## The classification problem

Given the assumptions above, the central question addressed in this paper is:

> *In a system that is locally describable, overlap-consistent, and admits identity persistence but fails to be globally coherent, what distinct structural modes of failure are possible?*

The remainder of this work shows that this question has a sharp and exhaustive answer. Under the stated assumptions, failure of global coherence must take one of exactly three forms, which we classify in the following sections.

# Obstruction Types as Invariants of the Encoding Atlas

In this section we formalize what is meant by an “obstruction type” and show that failure of global coherence admits an exhaustive classification into exactly three inequivalent classes. The classification is stated in terms of invariants of the encoding atlas and is therefore stable under admissible refinement and re-encoding.

## The encoding atlas and its nerve

We briefly recall the structural objects introduced in the Modal Triplet Theory core.

Let $`\{A_\alpha\}`$ be an admissible cover of the region of interest, with associated local encodings
``` math
\mathcal E_\alpha = (A_\alpha, Z_\alpha, E_\alpha, \ldots).
```
On nonempty overlaps $`A_{\alpha\beta}`$ there exist admissible re-encoding maps
``` math
f_{\alpha\beta} : Z_\alpha \to Z_\beta,
```
defined up to admissible equivalence.

These data define a groupoid of encodings and a simplicial object, the *atlas nerve* $`N`$, whose $`k`$-simplices correspond to nonempty $`(k+1)`$-fold overlaps of admissible domains.

## Global coherence and descent

Global coherence is equivalent to the existence of a global object descending from the local encodings.

<div class="definition">

**Definition 8** (Global object). A *global object* is a choice of representatives in each $`Z_\alpha`$ together with compatibility on all overlaps such that all re-encoding maps compose consistently on the atlas nerve.

</div>

Failure of global coherence is therefore a failure of descent: local data exist, but cannot be glued into a global object.

## Obstruction types as atlas invariants

We now define precisely what is meant by an obstruction *type*.

<div class="definition">

**Definition 9** (Obstruction type). An *obstruction type* is an equivalence class of failures of global descent that:

1.  is invariant under admissible refinement of the cover;

2.  is invariant under admissible re-encoding;

3.  cannot be eliminated by local modification of representatives;

4.  corresponds to a distinct failure mode of the descent problem.

</div>

Two failures of global coherence are of the same obstruction type if they define the same invariant class on the atlas nerve or encoding fibration.

## Three invariant failure modes

Under the assumptions of local describability, overlap consistency, identity persistence, and finite admissibility, exactly three inequivalent obstruction types can arise.

<div class="theorem">

**Theorem 10** (Exhaustive obstruction classification). *Any obstruction to global coherence is equivalent, under admissible refinement and re-encoding, to exactly one of the following:*

1.  ***Circle:** a nontrivial holonomy class on a $`1`$-cycle of the atlas nerve, corresponding to path-dependent inconsistency of transport;*

2.  ***Lens:** a nontrivial isotropy or automorphism class of encoding fibers, corresponding to non-unique but consistent local lifts;*

3.  ***Nil:** a nontrivial complement of the encodable set $`X_{\mathrm{enc}} \subset X`$, corresponding to empty encoding fibers.*

*No fourth inequivalent obstruction type exists.*

</div>

## Interpretation of the three types

The three obstruction types correspond to distinct descent failures:

- Circle obstructs descent by path dependence on loops in the nerve.

- Lens obstructs descent by non-uniqueness of lifts even when compatibility holds.

- Nil obstructs descent by failure of existence of local lifts.

These failure modes are mutually irreducible: circle cannot be absorbed into lens, lens cannot be absorbed into nil, and nil cannot be resolved by refinement.

<div class="remark">

*Remark 11*. Formulated in this way, the classification is a theorem about the descent problem for the encoding atlas. It does not rely on logical case-splitting, but on the structure of the atlas nerve and the encoding fibration.

</div>

## Classification theorem

<div class="theorem">

**Theorem 12** (Exhaustive obstruction classification). *Under the assumptions of local describability, overlap consistency, identity persistence, and finite admissibility, any obstruction to global coherence must be of exactly one of the following three types:*

1.  ***Circle**: loop inconsistency detected only on closed chains of overlapping admissible domains;*

2.  ***Lens**: non-uniqueness of admissible local representation without contradiction;*

3.  ***Nil**: failure of representability, i.e. absence of any admissible encoding on a region.*

*No fourth obstruction type is possible.*

</div>

## Proof sketch

We sketch the argument, emphasizing structural necessity rather than construction.

Consider an attempt to extend local descriptions to a global encoding. Failure of this attempt must manifest in one of the following ways:

#### Case 1: Path-dependent inconsistency.

Suppose that for every point there exists at least one admissible local description, and that pairwise overlaps are consistent, but transporting a coherent structure along two distinct chains of overlapping domains yields inequivalent results. By identity persistence, such inconsistency can only be detected when the two chains form a closed loop. This defines an obstruction visible only on closed overlap chains, which we call a *circle*.

#### Case 2: Redundant but consistent descriptions.

Suppose that for every point there exist admissible local descriptions, and that all overlap relations are consistent, but that the local description is not unique. If multiple admissible sections represent the same coherent structure with no canonical global choice, then global coherence fails by non-uniqueness rather than contradiction. This defines a *lens* obstruction.

#### Case 3: Failure of representability.

Finally, suppose that there exist regions on which no admissible local description applies. In this case, global coherence fails because the reduced description ceases to exist. This defines a *nil* obstruction.

These cases are mutually exclusive and collectively exhaustive. Any apparent alternative failure mode reduces to one of them: path dependence reduces to circle, non-canonical choice reduces to lens, and absence of description reduces to nil. Therefore no fourth obstruction type exists. $`\square`$

## Irreducibility of the three types

It is important to note that the three obstruction types are irreducible to one another under admissible re-encoding.

<div class="remark">

*Remark 13*. A circle obstruction cannot be removed by choosing a different local representative, and therefore cannot be reduced to a lens. A lens obstruction does not involve contradiction and therefore cannot be reduced to nil. Nil represents the absence of description and therefore cannot be reduced to either circle or lens. Each obstruction type represents a distinct structural failure mode.

</div>

## Interpretive note

The terminology *circle*, *lens*, and *nil* is descriptive rather than metaphorical. Each name refers to the minimal structural pattern by which the corresponding obstruction is detected: closed overlap chains, asymmetric projection–reconstruction pairs, and empty encoding fibers, respectively.

# Circle: Loop Inconsistency and Holonomy

We now analyze the first obstruction type identified in the classification theorem: *circle*. This obstruction captures the failure of identity persistence detected only on closed chains of overlapping admissible domains.

## Closed overlap chains

Let $`\{A_\alpha\}`$ be an admissible cover, and consider a finite sequence of domains
``` math
A_{\alpha_1}, A_{\alpha_2}, \ldots, A_{\alpha_n}
```
such that each consecutive overlap $`A_{\alpha_i\alpha_{i+1}}`$ is nonempty, and $`A_{\alpha_n\alpha_1}`$ is also nonempty. Such a sequence defines a *closed overlap chain*.

On each overlap $`A_{\alpha_i\alpha_{i+1}}`$ there exists an admissible re-encoding map
``` math
f_{\alpha_i\alpha_{i+1}} : Z_{\alpha_i} \to Z_{\alpha_{i+1}}
```
relating the local descriptions.

## Definition of circle

<div class="definition">

**Definition 14** (Circle obstruction). A *circle* obstruction exists if there is a closed overlap chain such that the composition of admissible re-encoding maps around the loop satisfies
``` math
f_{\alpha_n\alpha_1} \circ f_{\alpha_{n-1}\alpha_n} \circ \cdots \circ
f_{\alpha_1\alpha_2}
\;\not\sim\;
\mathrm{id}_{Z_{\alpha_1}},
```
where $`\sim`$ denotes admissible equivalence.

</div>

Thus, although each pairwise overlap is consistent, identity persistence fails when descriptions are transported around the loop.

## Minimality of triple overlaps

The circle obstruction cannot be detected on pairwise overlaps alone. At least three overlapping domains are required.

<div class="lemma">

**Lemma 15**. *If all admissible overlap chains have length at most two, then any apparent loop inconsistency can be removed by admissible re-encoding, and no genuine circle obstruction exists.*

</div>

<div class="proof">

*Sketch.* With only pairwise overlaps, any composition of re-encoding maps can be reduced to a single transition between two charts. Any nontrivial effect can therefore be absorbed into a redefinition of the local representative, reducing the obstruction to a lens rather than a circle. ◻

</div>

This establishes that circle obstructions are intrinsically associated with *triple overlap structure*.

## Circle as shared obstruction

A crucial feature of the circle obstruction is that it is not localized within any single chart or encoding. Instead, it resides entirely in the compatibility data between encodings.

<div class="remark">

*Remark 16*. The circle obstruction is *shared*: it cannot be attributed to the base description alone or to any internal layer alone. It arises from the failure of simultaneous consistency of all overlap relations around a loop.

</div>

This shared character is what later forces any bookkeeping structure to couple base and internal descriptions universally.

## Circle and holonomy

Although no geometric structure has been assumed, the formal pattern exhibited by a circle obstruction is that of *holonomy*: the outcome of transporting identity around a loop depends on the path taken.

<div class="remark">

*Remark 17*. The appearance of holonomy-like behavior here is purely structural. It arises from local describability and overlap consistency together with global obstruction, and does not presuppose a connection, curvature, or manifold.

</div>

In later papers, this structure will be shown to necessitate connection- and curvature-like bookkeeping when one attempts to stabilize identity persistence under refinement.

## Relation to other obstruction types

It is important to distinguish circle from the other obstruction types.

- A circle obstruction involves contradiction detected only on closed chains; it cannot be removed by choosing a different local representative.

- A lens obstruction involves non-uniqueness without contradiction; no loop is required.

- A nil obstruction involves absence of any admissible description.

<div class="remark">

*Remark 18*. If a purported loop inconsistency can be eliminated by a redefinition of local representatives, then the obstruction is not a circle but a lens. Genuine circle obstructions are therefore precisely those that survive all admissible re-encodings.

</div>

## Preview of consequences

The existence of circle obstructions has two immediate consequences that will be developed in subsequent sections:

1.  it forces any stable realization to include additional bookkeeping structure to track loop-dependent inconsistency;

2.  it couples base and internal descriptions, preventing their independent global specification.

These consequences underpin the later emergence of geometric and gravitational encoding structures.

# Lens: Redundancy and Non-Unique Representation

We now analyze the second obstruction type identified in the classification theorem: *lens*. Unlike circle, which involves contradiction detected on closed overlap chains, lens captures failure of global coherence through non-uniqueness of local representation without inconsistency.

## Non-unique local sections

Consider an admissible domain $`A_\alpha`$ with local encoding
``` math
\mathcal E_\alpha = (A_\alpha, Z_\alpha, E_\alpha, \ldots).
```
Local describability requires the existence of at least one admissible section selecting a representative of coherent structure. However, admissibility does not require this section to be unique.

<div class="definition">

**Definition 19** (Lens obstruction). A *lens* obstruction exists if there are multiple admissible local sections or encodings representing the same coherent structure on a domain, such that:

1.  all representations are mutually consistent on overlaps;

2.  no canonical global choice of representative exists;

3.  any two choices are related by admissible re-encoding.

</div>

Thus, lens represents redundancy of description rather than contradiction.

## Projection–reconstruction asymmetry

The defining structural feature of lens is an asymmetry between projection and reconstruction.

<div class="remark">

*Remark 20*. Lens obstructions arise whenever the reduced description involves a projection that forgets information, together with a reconstruction (section) that is not unique. Projection maps may be canonical, while reconstruction maps are necessarily choice-dependent.

</div>

This asymmetry ensures that multiple admissible representations coexist, all equally valid, but none privileged.

## Lens as descriptive redundancy

A lens obstruction does not indicate a failure of consistency. Instead, it indicates that the same coherent structure admits multiple internal representations.

<div class="remark">

*Remark 21*. Lens obstructions encode redundancy of description, not multiplicity of underlying entities. They therefore represent a structural symmetry of the encoding rather than a symmetry of the system being described.

</div>

This distinction will later be essential for understanding gauge structure as an encoding phenomenon rather than a fundamental physical symmetry.

## Minimality of lens

Lens obstructions can occur already on pairwise overlaps and do not require closed overlap chains.

<div class="lemma">

**Lemma 22**. *Lens obstructions can exist in the absence of circle obstructions.*

</div>

<div class="proof">

*Sketch.* Non-unique local sections may exist even when all overlap transition maps are path-independent. In this case, redundancy persists but no loop inconsistency arises. ◻

</div>

This distinguishes lens sharply from circle.

## Lens and irreducibility

Lens obstructions are irreducible to the other obstruction types.

- A lens obstruction does not involve contradiction and therefore cannot be reduced to a circle.

- A lens obstruction does not involve absence of description and therefore cannot be reduced to nil.

<div class="remark">

*Remark 23*. If redundancy can be removed by a single admissible global choice, then the obstruction is not a genuine lens. A genuine lens exists precisely when redundancy is unavoidable.

</div>

## Preview of consequences

The existence of lens obstructions has two key consequences that will be developed later:

1.  it necessitates bookkeeping of descriptive redundancy across overlaps;

2.  it gives rise to gauge-like encoding structures when realizations are introduced.

Lens therefore captures the structural origin of gauge freedom without invoking fields, connections, or group actions.

# Nil: Termination of Describability

We now analyze the third and final obstruction type identified in the classification theorem: *nil*. Unlike circle and lens, which arise from inconsistencies or redundancies among admissible descriptions, nil represents the complete failure of local describability itself.

## Absence of admissible encodings

Nil arises when the conditions for admissibility fail entirely.

<div class="definition">

**Definition 24** (Nil obstruction). A *nil* obstruction exists on a region if there is no admissible local encoding applicable to that region. Equivalently, the encoding fiber over that region is empty.

</div>

Nil therefore represents not inconsistency of description, nor multiplicity of representation, but the absence of any reduced description.

## Nil versus non-existence

It is essential to distinguish nil from ontological non-existence.

<div class="remark">

*Remark 25*. Nil does not assert that the underlying system ceases to exist. It asserts only that no admissible reduced description applies. The obstruction is descriptive, not ontological.

</div>

This distinction is crucial for later interpretation of horizons, collapse, and singular behavior.

## Structural origin of nil

Nil obstructions arise whenever the admissibility conditions themselves are violated, for example when:

- no local section exists;

- overlap consistency fails irreparably;

- contractivity or stability conditions break down;

- truncation or projection errors exceed tolerance.

These failures cannot be repaired by re-encoding or refinement.

## Nil as a boundary object

Nil plays the role of a boundary in the space of admissible descriptions.

<div class="remark">

*Remark 26*. Nil corresponds to the boundary of the encoding atlas: it is the locus at which the atlas fails to admit any chart. In categorical terms, it acts as a zero object for admissible encodings.

</div>

This boundary character underlies the irreversibility associated with nil.

## Irreversibility and termination

Once a nil obstruction is encountered, no continuation of the reduced description is possible across that region.

<div class="lemma">

**Lemma 27**. *Nil obstructions are terminal: once encountered along a chain of admissible descriptions, they cannot be passed through or undone by admissible re-encoding.*

</div>

<div class="proof">

*Sketch.* By definition, no admissible encoding exists in a nil region. Any attempt to extend a reduced description across such a region would therefore violate local describability. ◻

</div>

This terminal character distinguishes nil sharply from circle and lens.

## Nil and kinematic termination

In the kinematic interpretation of persistence across admissible overlaps, nil corresponds to termination of motion or history.

<div class="remark">

*Remark 28*. In coherent kinematics, nil appears as the endpoint of worldlines, horizons of representability, or collapse of record persistence. These interpretations are derived, not assumed.

</div>

## Nil and irreducibility

Nil obstructions are irreducible to the other obstruction types.

- Nil is not redundancy and therefore cannot be reduced to lens.

- Nil is not contradiction and therefore cannot be reduced to circle.

<div class="remark">

*Remark 29*. If an apparent absence of description can be removed by refining the admissible cover or choosing a different encoding, then the obstruction is not nil. A genuine nil obstruction exists only when all admissible descriptions fail.

</div>

## Preview of consequences

Nil obstructions complete the classification of failure modes of global coherence. Together with circle and lens, they will determine the minimal architectural requirements for any realization capable of supporting local describability, redundancy, and termination simultaneously.

# Minimal Coexistence: Why Three Layers Are Required

Having classified the three obstruction types—circle, lens, and nil—as inequivalent invariants of the encoding atlas, we now address the question of *coexistence*. Specifically, we ask what minimal architectural structure is capable of supporting all three obstruction types simultaneously, in a stable and non-degenerate manner.

## Structural meaning of a layer

We begin by making precise what is meant by a *layer* in this context.

<div class="definition">

**Definition 30** (Independent layer). A *layer* is an independent structural carrier of encoding data such that:

1.  it admits local sections and overlap re-encodings;

2.  its local automorphism group (lens redundancy) acts nontrivially on its encoding data;

3.  its transition data cannot be absorbed into the automorphism group of any other single layer under admissible re-encoding.

</div>

The third condition expresses independence: loop or overlap defects associated with one layer cannot be reinterpreted purely as redundancy in another.

## Single-layer degeneracy

We first consider the possibility that all obstruction types could be supported within a single layer.

<div class="lemma">

**Lemma 31**. *A single-layer architecture cannot support non-degenerate coexistence of circle, lens, and nil obstructions.*

</div>

<div class="proof">

*Sketch.* In a single layer, any loop-dependent inconsistency detected on closed overlap chains can always be absorbed into a redefinition of local representatives, because the full transition structure acts within a single automorphism group. Thus circle obstructions reduce to lens obstructions. Alternatively, failure of representability collapses directly to nil. No independent circle obstruction can persist. ◻

</div>

This shows that one layer is insufficient.

## Two-layer architectures and gauge-removability

We next consider architectures with two independent layers.

<div class="lemma">

**Lemma 32**. *In a two-layer architecture satisfying the independence conditions above, any loop obstruction is admissibly equivalent to a lens obstruction.*

</div>

<div class="proof">

*Sketch.* With two layers, transition data live in a product of two automorphism groups. Any loop defect detected on a closed overlap chain can be decomposed into a pair of layer-wise transformations. Because there are only two layers, the resulting defect can always be absorbed into a redefinition of representatives in one layer relative to the other. Equivalently, the loop holonomy lies entirely within the combined isotropy group of the encoding fibers. Under admissible re-encoding, such defects reduce to non-uniqueness of representation rather than genuine path-dependent inconsistency. ◻

</div>

<div class="remark">

*Remark 33*. This result does not assert that two-layer systems cannot exhibit holonomy in an abstract groupoid sense. It asserts that, under the MTT notion of admissible re-encoding and layer independence, such holonomy is not an invariant obstruction type and therefore does not constitute a genuine circle.

</div>

Thus, two layers are insufficient to stabilize circle as an independent obstruction.

## Tri-layer necessity

We now show that three layers suffice and are minimal.

<div class="theorem">

**Theorem 34** (Tri-layer minimality). *Three independent layers are the minimal structural architecture capable of supporting non-degenerate coexistence of circle, lens, and nil obstructions.*

</div>

<div class="proof">

*Sketch.* With three independent layers, pairwise overlaps support lens obstructions via layer-wise redundancy, while triple overlaps support genuine cocycle data that cannot be absorbed into the automorphism group of any single layer. Loop defects detected on three-layer overlap chains therefore survive admissible re-encoding as invariant circle obstructions. Nil remains possible through simultaneous failure of all layers. Minimality follows from the preceding lemmas. ◻

</div>

## Shared obstruction and universal coupling

A key feature of the tri-layer architecture is that the circle obstruction is *shared* across all layers.

<div class="remark">

*Remark 35*. In a tri-layer system, the circle obstruction resides in the compatibility data among all three layers simultaneously. It cannot be attributed to any single layer and therefore couples all layers and the base description universally. This shared character underlies the later emergence of geometric and gravitational encoding structures.

</div>

## Stability under refinement

Finally, we note that the tri-layer architecture is stable under admissible refinement.

<div class="remark">

*Remark 36*. Architectures with fewer layers fail to stabilize all three obstruction types under refinement, while architectures with additional layers introduce redundancy without generating new obstruction classes. Three layers therefore represent the minimal stable architecture.

</div>

# From Tri-Layer Structure to Minimal Continuous Realization

In this section we pass from the purely structural tri-layer result to a rigorous statement about minimal *continuous representability*. To obtain a fully rigorous argument, we specify a realization class in which: (i) encodings are modeled by smooth local trivializations, (ii) overlap data defines Čech cocycles, (iii) circle obstructions correspond to nontrivial holonomy (curvature) classes.

No claim of ontological dimensionality is made; the conclusion is a statement of representability up to admissible re-encoding.

## Realization class and precise meaning of “circle”

We fix a realization class sufficient to make the obstruction invariants geometric (bundle-theoretic) objects.

<div id="ass:smooth-atlas" class="assumption">

**Assumption 37** (Smooth atlas realization). Let $`A\subset X`$ be an admissible domain. Assume that on $`P(A)`$ there exists a finite or locally finite admissible cover $`\{U_\alpha\}`$ such that:

1.  each $`U_\alpha`$ is a smooth manifold (or smooth submanifold of a common ambient manifold);

2.  each encoding chart on $`U_\alpha`$ is a smooth local trivialization with transition maps $`g_{\alpha\beta}`$ on overlaps $`U_{\alpha\beta}`$;

3.  the transition maps form a Čech 1-cocycle with values in a structure group $`G`$ (possibly protocol-indexed), i.e.
    ``` math
    g_{\alpha\beta} g_{\beta\gamma} g_{\gamma\alpha} = e
    \quad \text{on } U_{\alpha\beta\gamma},
    ```
    up to admissible equivalence.

</div>

<div id="ass:circle-holonomy" class="assumption">

**Assumption 38** (Circle realized as nontrivial holonomy). Assume that, in this realization class, a circle obstruction corresponds to a nontrivial holonomy/curvature class of a $`G`$-bundle with connection on $`P(A)`$. Equivalently: there exists a principal $`G`$-bundle $`P_G\to P(A)`$ with a connection whose curvature is not identically zero on $`P(A)`$.

</div>

<div class="remark">

*Remark 39*. Assumption <a href="#ass:circle-holonomy" data-reference-type="ref" data-reference="ass:circle-holonomy">38</a> is a realization hypothesis: it specifies how the abstract circle invariant is represented in the smooth realization class. It is the minimal standard way to make “circle” rigorous as a stable invariant under refinement.

</div>

## Why each independent layer requires at least two continuous coordinates

We now prove a lower bound on the continuous coordinate dimension required per independent layer to support a stable circle obstruction in the realization class above.

<div class="definition">

**Definition 40** (Layer carrier). A *layer carrier* is the minimal smooth manifold factor $`B`$ (in a local product-type representation) on which one independent layer of transition data acts nontrivially.

</div>

<div id="thm:no-circle-1d" class="theorem">

**Theorem 41** (No stable circle on one-dimensional layer carriers). *Under Assumptions <a href="#ass:smooth-atlas" data-reference-type="ref" data-reference="ass:smooth-atlas">37</a>–<a href="#ass:circle-holonomy" data-reference-type="ref" data-reference="ass:circle-holonomy">38</a>, a one-dimensional layer carrier cannot support a stable circle obstruction. Consequently, any independent layer carrier must satisfy $`\dim B \ge 2`$.*

</div>

<div class="proof">

*Proof.* Let $`B`$ be a connected smooth 1-manifold (possibly with boundary). In the realization class, the circle obstruction is represented by a principal $`G`$-bundle with connection whose curvature is nonzero somewhere on the domain. Curvature is a horizontal $`\mathfrak{g}`$-valued 2-form $`F\in \Omega^2(\cdot;\mathfrak g)`$. However, on a 1-manifold $`B`$ one has
``` math
\Omega^2(B) = \{0\},
```
since there are no nonzero differential 2-forms on a 1-dimensional manifold. Therefore any connection restricted to a 1D carrier has identically vanishing curvature. In particular, no nontrivial curvature/holonomy class can be supported *as a local, stable, infinitesimal invariant*. Any apparent loop effect on a 1D carrier is necessarily global and can be absorbed into representative choice, hence reduces to a lens-type redundancy rather than a circle invariant in the sense of Assumption <a href="#ass:circle-holonomy" data-reference-type="ref" data-reference="ass:circle-holonomy">38</a>.

Thus a one-dimensional carrier cannot realize the circle invariant as a stable curvature class. Therefore $`\dim B\ge 2`$ is necessary for an independent layer. ◻

</div>

<div class="remark">

*Remark 42*. This argument is fully rigorous and uses only the standard fact that curvature is a 2-form and 2-forms vanish on 1D manifolds. It does not assume any specific dynamics.

</div>

## Internal dimensional lower bound for tri-layer coexistence

We now combine tri-layer minimality (Section <a href="#sec:sec7" data-reference-type="ref" data-reference="sec:sec7">7</a>) with Theorem <a href="#thm:no-circle-1d" data-reference-type="ref" data-reference="thm:no-circle-1d">41</a>.

<div id="thm:internal6" class="theorem">

**Theorem 43** (Six-dimensional internal lower bound). *Assume tri-layer minimality holds (Section <a href="#sec:sec7" data-reference-type="ref" data-reference="sec:sec7">7</a>) and that each layer admits a smooth realization satisfying Assumptions <a href="#ass:smooth-atlas" data-reference-type="ref" data-reference="ass:smooth-atlas">37</a>–<a href="#ass:circle-holonomy" data-reference-type="ref" data-reference="ass:circle-holonomy">38</a>. Then any continuous realization supporting non-degenerate coexistence of circle, lens, and nil requires internal dimension at least six:
``` math
\dim B_{\mathrm{internal}} \ge 3 \cdot 2 = 6.
```*

</div>

<div class="proof">

*Proof.* By tri-layer minimality, three independent layers are required. By Theorem <a href="#thm:no-circle-1d" data-reference-type="ref" data-reference="thm:no-circle-1d">41</a>, each independent layer carrier has dimension at least 2. Independence implies these carriers contribute additively to the internal coordinate dimension. Hence
``` math
\dim B_{\mathrm{internal}} \ge 2 + 2 + 2 = 6.
```
 ◻

</div>

## Base dimension requirement as an explicit realization axiom

The minimal base dimension depends on what class of kinematic persistence one requires. To keep this section fully rigorous without importing a separate dimension-selection theorem, we state the base requirement as an explicit realization assumption.

<div id="ass:base4" class="assumption">

**Assumption 44** (Four-dimensional kinematic base). In the realization class considered in this paper, kinematic persistence is required in the sense of the coherent kinematics layer, and the effective base manifold supporting that kinematics has dimension
``` math
\dim Y = 4.
```

</div>

<div class="remark">

*Remark 45*. Assumption <a href="#ass:base4" data-reference-type="ref" data-reference="ass:base4">44</a> packages the kinematic dimension-selection content of the kinematics program into the present paper. If a separate theorem-level derivation of $`\dim Y=4`$ is supplied elsewhere, this assumption can be replaced by a reference.

</div>

## Minimal continuous representability: the ten-dimensional bound

We now state and prove the dimensional representability bound.

<div id="thm:tenD" class="theorem">

**Theorem 46** (Minimal continuous representability by a ten-dimensional space). *Assume:*

1.  *tri-layer minimality (Section <a href="#sec:sec7" data-reference-type="ref" data-reference="sec:sec7">7</a>);*

2.  *the smooth atlas realization and circle-as-holonomy assumptions (Assumptions <a href="#ass:smooth-atlas" data-reference-type="ref" data-reference="ass:smooth-atlas">37</a>–<a href="#ass:circle-holonomy" data-reference-type="ref" data-reference="ass:circle-holonomy">38</a>);*

3.  *the four-dimensional kinematic base assumption (Assumption <a href="#ass:base4" data-reference-type="ref" data-reference="ass:base4">44</a>).*

*Then any continuous realization supporting non-degenerate coexistence of circle, lens, and nil obstructions is *representable*, up to admissible re-encoding, by a configuration space of dimension at least ten:
``` math
\dim M \;\ge\; \dim Y + \dim B_{\mathrm{internal}} \;\ge\; 4 + 6 \;=\; 10.
```
Moreover, the bound is sharp in the realization class: it is achieved by a product-type representation
``` math
M \simeq Y_4 \times B_1 \times B_2 \times B_3,
\qquad \dim B_i = 2.
```*

</div>

<div class="proof">

*Proof.* By Assumption <a href="#ass:base4" data-reference-type="ref" data-reference="ass:base4">44</a>, $`\dim Y = 4`$. By Theorem <a href="#thm:internal6" data-reference-type="ref" data-reference="thm:internal6">43</a>, $`\dim B_{\mathrm{internal}}\ge 6`$. Therefore any product-type representative has dimension at least $`4+6=10`$.

Sharpness: choose three independent layer carriers $`B_i`$ each of dimension 2. Then $`\dim(B_1\times B_2\times B_3)=6`$ and hence $`\dim M = 4+6=10`$. Such a representation is admissible in the realization class by construction, and supports the required tri-layer obstruction structure. ◻

</div>

<div class="remark">

*Remark 47* (Representability, not ontology). Theorem <a href="#thm:tenD" data-reference-type="ref" data-reference="thm:tenD">46</a> asserts representability up to admissible re-encoding within the stated realization class. It does not assert that the physical world is fundamentally ten-dimensional.

</div>

## Bundle geometry as bookkeeping (consequence, not assumption)

Finally, we record the rigorous sense in which bundle geometry is selected as a bookkeeping framework.

<div id="cor:bundle-bookkeeping" class="corollary">

**Corollary 48** (Bundle geometry is the minimal bookkeeping framework). *Under Assumptions <a href="#ass:smooth-atlas" data-reference-type="ref" data-reference="ass:smooth-atlas">37</a>–<a href="#ass:circle-holonomy" data-reference-type="ref" data-reference="ass:circle-holonomy">38</a>, the data of local charts, overlap maps, and circle holonomy define a principal bundle with connection on $`P(A)`$, unique up to admissible equivalence on the domain.*

</div>

<div class="proof">

*Proof.* By Assumption <a href="#ass:smooth-atlas" data-reference-type="ref" data-reference="ass:smooth-atlas">37</a>, the transition maps form a cocycle defining a principal $`G`$-bundle (standard Čech construction). By Assumption <a href="#ass:circle-holonomy" data-reference-type="ref" data-reference="ass:circle-holonomy">38</a>, the circle invariant is represented by a nontrivial connection curvature, so a connection exists on that bundle. Uniqueness up to admissible equivalence follows from standard gauge equivalence of cocycles and connections on overlaps. ◻

</div>

<div class="remark">

*Remark 49*. This corollary makes precise that bundle geometry is not postulated: it is the canonical mathematical packaging of overlap consistency, redundancy, and holonomy once a smooth realization class is chosen.

</div>

# Consequences for Encoding Classes

The results obtained in this work are structural and realizational, not phenomenological. Their significance lies in constraining the possible *encoding classes* that can exist downstream in Modal Triplet Theory. In this section we summarize how the circle–lens–nil classification and the tri-layer minimality result determine the form of all subsequent encoding-class papers.

## Encoding classes versus realizations

An encoding class specifies a *form of description*—a language in which reduced structures may be expressed—while a realization specifies a concrete implementation of that language.

<div class="remark">

*Remark 50*. The present paper constrains encoding classes but does not select particular realizations. Bundle geometry, manifolds, connections, and spectral operators appear only when encoding classes are realized concretely.

</div>

The obstruction classification therefore precedes and constrains all encoding papers, regardless of how they are later realized.

## Gravity as kinematic consistency encoding

The circle obstruction represents loop-dependent inconsistency in identity persistence. Any encoding class that stabilizes identity across closed overlap chains must therefore introduce additional bookkeeping structure.

<div class="remark">

*Remark 51*. The encoding class commonly identified as gravity arises as the unique encoding that resolves circle obstructions by enforcing consistency of kinematic persistence across overlapping descriptions.

</div>

This result does not assume geometry or field equations. It asserts only that some encoding of consistency is unavoidable once circle obstructions exist. Geometric and gravitational structures are realizations of this encoding class.

## Gauge structure as redundancy encoding

Lens obstructions represent unavoidable redundancy of description.

<div class="remark">

*Remark 52*. Gauge structure arises as the encoding class that organizes and compensates for lens obstructions. Gauge freedom is therefore redundancy of encoding, not a symmetry of underlying reality.

</div>

This explains the universality and unobservability of gauge degrees of freedom across physical theories.

## Quantization as discrete constraint encoding

Nil obstructions represent termination of describability.

<div class="remark">

*Remark 53*. Discrete spectra and quantization arise as encoding responses to nil obstructions, in which continuous descriptions fail and only discrete, topologically protected structures remain admissible.

</div>

Quantization is therefore an encoding constraint, not an independent postulate.

## Unified and maximal encodings

Encoding classes need not exist independently. In some regimes, multiple obstruction types may be active simultaneously.

<div class="remark">

*Remark 54*. Encoding frameworks that simultaneously resolve circle, lens, and nil obstructions represent maximal or saturated encodings. Such encodings naturally exhibit features associated with unified frameworks, including coupled gravity, gauge redundancy, and quantization constraints.

</div>

The existence of such encodings is constrained by the tri-layer and minimal dimensionality results derived above.

## Relation to dark sector interpretations

The dark sector phenomena addressed elsewhere in the series are interpreted as regimes in which only weaker encoding classes remain admissible.

- Statistical encoding classes dominate when local representability fails but aggregate structure persists.

- Relational encoding classes dominate when even statistical descriptions fail and only transition constraints remain.

These interpretations rely directly on the obstruction classification and do not introduce new structure.

## Position in the series

This paper completes the structural classification required to motivate all subsequent encoding-class papers in the Modal Triplet Theory program.

<div class="remark">

*Remark 55*. The logical sequence is as follows:

1.  structural core establishes local describability and global obstruction;

2.  coherent kinematics defines persistence and motion;

3.  the present work classifies obstruction types and minimal coexistence;

4.  encoding-class papers address gravity, gauge, quantization, and unification;

5.  realization papers instantiate these encodings concretely.

</div>

## Outlook

By showing that exactly three obstruction types exist and that their stable coexistence forces a tri-layer architecture with a minimal continuous realization, this work removes arbitrariness from the appearance of geometric, gauge, and quantum structures in effective physical theories.

The remaining papers in the series build upon this classification to explore specific encoding classes and their realizations, without revisiting the structural inevitabilities established here.

# Compatibility with the Modal Triplet Theory Core

We briefly summarize how the obstruction classification developed in this work maps directly onto the structural objects introduced in the core of Modal Triplet Theory.

## Encoding atlas and obstruction types

In the MTT core, admissible descriptions are organized into an encoding atlas, with fibers
``` math
\mathrm{Enc}(x)
```
over points $`x \in X`$, and overlap relations encoded by admissible re-encodings. Failure of global coherence corresponds to failure of descent in this atlas.

The three obstruction types classified here correspond to distinct invariant features of this structure:

- **Circle** corresponds to a nontrivial holonomy class on $`1`$-cycles of the atlas nerve $`N`$, detected as path dependence of admissible transport around closed overlap chains.

- **Lens** corresponds to nontrivial isotropy of encoding fibers $`\mathrm{Enc}(x)`$, i.e. multiple admissible local sections related by re-encoding automorphisms.

- **Nil** corresponds to empty encoding fibers, defining the boundary of the encodable region $`X_{\mathrm{enc}} \subset X`$.

These three invariants exhaust the possible failures of global descent in the encoding atlas.

## Relation to the universal reduced relation

The universal reduced relation
``` math
\mathcal R \subset Y \times Y
```
introduced in the MTT core provides a global object encoding admissible reduced transitions. Circle obstructions correspond to nontrivial composition of $`\mathcal R`$ along loops in the atlas nerve, lens obstructions correspond to non-unique lifts of $`\mathcal R`$ to encoding fibers, and nil obstructions correspond to regions where $`\mathcal R`$ admits no admissible lift at all.

## Role in the series

The present paper refines the core statement that no global reduced encoding exists by classifying *how* such failure can occur. Subsequent papers in the series treat gravity, gauge structure, and quantization as encoding responses to circle, lens, and nil obstructions respectively, while realization papers construct explicit geometric models satisfying the representability conditions identified here.

No additional structural assumptions beyond those of the MTT core are introduced in this classification.

# Conclusion

In this work we have addressed a single structural question: given local describability, overlap consistency, identity persistence, and the absence of a global reduced description, what forms of failure of global coherence are possible, and what minimal architectures can support them simultaneously?

We have shown that the answer is sharp. Exactly three and only three obstruction types exist: loop inconsistency detected on closed overlap chains (circle), redundancy of local representation without contradiction (lens), and termination of describability (nil). These obstruction types are exhaustive and mutually irreducible; no fourth mode of failure is compatible with the stated structural assumptions.

We further demonstrated that non-degenerate coexistence of circle, lens, and nil requires a tri-layer architectural structure. Architectures with fewer layers collapse one obstruction type into another, while architectures with additional layers introduce redundancy without increasing structural capacity. When continuity and kinematic persistence are imposed as realization requirements, this tri-layer structure admits a minimal continuous realization equivalent, up to admissible re-encoding, to a ten-dimensional configuration space composed of a four-dimensional effective base and three independent internal layers.

Throughout, geometry, bundle structure, and dimensionality have not been assumed. Instead, they appear as minimal bookkeeping frameworks selected by the need to encode shared loop obstructions, redundancy, and termination consistently. The results therefore explain why geometric, gauge, and quantum structures arise so universally in effective physical theories, without postulating them as fundamental.

This paper completes the structural classification required to motivate the encoding-class papers that follow in the Modal Triplet Theory series. Those works develop gravity as a kinematic consistency encoding, gauge structure as a redundancy encoding, quantization as a discrete constraint encoding, and unified frameworks as saturated encodings, as well as concrete geometric and bundle realizations. No additional structural assumptions are introduced downstream.

The classification presented here establishes that the familiar architectures of modern theoretical physics are not arbitrary constructions, but inevitable responses to the coexistence of local describability and global obstruction.
