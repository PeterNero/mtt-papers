---
abstract: |
  We show that gauge structure arises as a necessary encoding class once local describability and overlap consistency coexist with lens obstructions, i.e. with non-unique but consistent local representations. In the Modal Triplet Theory (MTT) framework, gauge is not postulated as a symmetry of underlying reality and is not introduced as a field-theoretic axiom. Rather, it is identified as bookkeeping of descriptive redundancy: the unique encoding that organizes and compensates for the non-uniqueness of admissible local sections while preserving overlap consistency and kinematic persistence.

  We define gauge transformations as admissible automorphisms of encoding fibers, and show that gauge freedom is unavoidable whenever lens obstructions are present and global canonical representatives do not exist. We further show that in smooth realization classes, redundancy bookkeeping is realized by bundle structure with a connection-like object implementing consistent comparison of redundant representatives. This connection is distinct in role from the kinematic consistency encoding identified with gravity: gravity resolves circle obstructions (loop inconsistency), while gauge resolves lens obstructions (non-unique lifts). The analysis clarifies the structural origin of gauge universality and prepares the ground for quantization as the encoding response to nil obstructions.
author:
- Peter Nero
current_version: v1.0
date: January 2026
generated_from_main_tex_sha256: 72d198f4e94ee37ec4e5339ee001451746a4deb9305994285f071b04df1dd7ba
paper_id: the-modal-triplet-theory-program-b2-gauge-structure-as-4afd644a
release_state: zenodo_released
released_version: v1.0
title: |
  The Modal Triplet Theory Program B2:  
  Gauge Structure as Redundancy Encoding  
  in the Modal Triplet Theory Program
zenodo_doi: 10.5281/zenodo.18355037
zenodo_record_id: 18355037
zenodo_url: "https://zenodo.org/records/18355037"
---

# Introduction and Scope

The structural core of Modal Triplet Theory establishes that reduced descriptions exist only locally on admissible domains, that such descriptions must be related by controlled re-encoding on overlaps, and that no single global reduced encoding exists. Coherent kinematics then defines motion and causal structure as persistence across overlapping admissible encodings, without assuming spacetime or dynamical laws. A subsequent classification identifies three and only three obstruction types to global coherence: circle, lens, and nil.

The purpose of the present paper is to analyze the structural consequences of *lens* obstructions. A lens obstruction is the failure of global coherence by *redundancy*: multiple admissible local representatives exist that are mutually consistent on overlaps, but no canonical global choice exists. In such regimes, kinematic persistence and overlap consistency remain intact, but the reduced description is not unique. This non-uniqueness is neither contradiction (circle) nor termination of description (nil). It is an independent obstruction type and therefore demands its own encoding response.

We show that lens obstructions force the introduction of an additional encoding class whose sole role is to organize descriptive redundancy. This encoding class is what is conventionally identified as gauge structure. In MTT terms, gauge is not a fundamental physical symmetry; it is the unique bookkeeping structure that compensates for the non-uniqueness of admissible local sections while preserving consistent reduced description.

Throughout this paper we adhere to three principles:

- Gauge is an *encoding* of redundancy, not a postulated interaction or field.

- Gauge transformations are *automorphisms of representation*, not transformations of underlying reality.

- Geometric objects commonly associated with gauge theory (bundles, connections) appear only as *realizations* of the redundancy encoding, not as axioms of the structural theory.

We emphasize the separation between gauge and gravity in the MTT program. Gravity, treated elsewhere, arises as kinematic consistency bookkeeping required to resolve circle obstructions (loop-dependent inconsistency). Gauge arises here as redundancy bookkeeping required to resolve lens obstructions (non-unique but consistent representation). The two encodings are structurally distinct, though they may couple in particular realizations.

<div class="remark">

*Remark 1* (Position in the series). This paper depends only on the structural core, coherent kinematics, and the circle–lens–nil obstruction classification. It follows the gravity-as-encoding paper and precedes the quantization paper, in which nil obstructions are shown to force discrete constraint encodings. Realization-specific constructions of gauge bundles and connections are deferred to the geometric realization papers.

</div>

# Lens Obstructions as Non-Unique Local Lifts

In this section we formalize lens obstructions in a manner suitable for defining gauge structure as an encoding class. The key idea is that lens obstructions correspond to non-uniqueness of admissible local lifts of coherent structure, without contradiction or failure of representability.

## Local lifts and redundancy

Let $`\mathcal E_\alpha = (A_\alpha, Z_\alpha, E_\alpha, \ldots)`$ be an admissible encoding on domain $`A_\alpha`$.

<div class="definition">

**Definition 2** (Local lift). A *local lift* of a coherent structure on $`A_\alpha`$ is a choice of representative in the encoding fiber $`Z_\alpha`$ consistent with admissibility and overlap constraints.

</div>

Local describability requires the existence of at least one admissible local lift on each admissible domain. Lens obstructions arise when such lifts are not unique.

## Definition of lens obstruction (refined)

We now restate lens obstructions in terms appropriate for gauge structure.

<div class="definition">

**Definition 3** (Lens obstruction (structural)). A *lens obstruction* exists on an admissible domain if the encoding fibers admit a nontrivial automorphism (isotropy) group acting on local lifts such that:

1.  multiple admissible local lifts of the same coherent structure exist;

2.  these lifts are related by admissible fiber automorphisms;

3.  the automorphism structure persists under admissible refinement and cannot be absorbed into overlap re-encoding.

</div>

Thus, lens obstructions represent redundancy of representation without inconsistency.

<div class="remark">

*Remark 4* (Lens versus gauge). A lens obstruction is a *structural condition*: the existence of non-unique but admissible local lifts related by persistent isotropy of encoding fibers. Gauge structure is not identified with the lens obstruction itself, but with the *encoding response* required to organize and compensate for that redundancy. Thus, lens denotes the obstruction, while gauge denotes the encoding that resolves it. This distinction is structural and holds independently of any particular physical realization.

</div>

## Lens versus circle and nil

It is important to distinguish lens obstructions sharply from the other two obstruction types.

- Lens obstructions do not involve path dependence; transporting different lifts along admissible continuation chains yields equivalent results.

- Lens obstructions do not involve termination; admissible descriptions exist everywhere in the domain.

<div class="remark">

*Remark 5*. If non-uniqueness of lifts could be eliminated by refining the admissible cover or by admissible re-encoding, then the obstruction would not be a genuine lens. Lens obstructions are precisely those redundancies that persist under all such operations.

</div>

## Fiberwise characterization

Lens obstructions are fiberwise in nature.

<div class="lemma">

**Lemma 6**. *Lens obstructions correspond to nontrivial automorphism structure of encoding fibers.*

</div>

<div class="proof">

*Proof.* Multiple admissible local lifts correspond to distinct points in the same encoding fiber that are related by admissible re-encoding and produce identical coherent content. The set of such transformations forms a nontrivial automorphism group acting on the fiber. ◻

</div>

This automorphism structure is the structural origin of gauge freedom.

## Absence of global lift

Lens obstructions prevent the existence of a global lift.

<div class="theorem">

**Theorem 7** (Non-existence of a global lift). *If a lens obstruction exists on an admissible domain, then no globally defined admissible lift exists that is compatible with all local encodings.*

</div>

<div class="proof">

*Proof.* A global lift would select a single representative in each encoding fiber. However, the existence of a persistent nontrivial automorphism group implies that any such choice can be transformed into an inequivalent admissible lift. Therefore no choice is invariant under admissible re-encoding, and no global lift can exist. ◻

</div>

## Interpretation

We emphasize that lens obstructions do not indicate ambiguity or incompleteness of the underlying system.

<div class="remark">

*Remark 8*. Lens obstructions encode descriptive redundancy, not physical indeterminacy. They indicate that multiple representations are equally valid descriptions of the same coherent structure.

</div>

This redundancy must be organized to preserve overlap consistency and kinematic persistence. In the next section we show that this organization uniquely defines gauge transformations as admissible automorphisms of encoding fibers.

# Gauge Transformations as Fiber Automorphisms

We now formalize gauge transformations in the Modal Triplet Theory framework. Gauge transformations are not postulated as symmetries of an underlying physical space; they arise as the natural automorphisms associated with lens obstructions, i.e. with non-unique but admissible local lifts of coherent structure.

## Automorphisms of encoding fibers

Let $`\mathcal E_\alpha = (A_\alpha, Z_\alpha, E_\alpha, \ldots)`$ be an admissible encoding, and let $`z \in Z_\alpha`$ be a local lift of a coherent structure.

<div class="definition">

**Definition 9** (Fiber automorphism). A *fiber automorphism* at $`\mathcal E_\alpha`$ is an admissible map
``` math
g_\alpha : Z_\alpha \to Z_\alpha
```
such that:

1.  $`g_\alpha`$ preserves coherent content, i.e. $`E_\alpha^{-1}(z)`$ and $`E_\alpha^{-1}(g_\alpha(z))`$ represent the same coherent structure;

2.  $`g_\alpha`$ is compatible with admissible re-encoding on overlaps;

3.  $`g_\alpha`$ is invertible up to admissible equivalence.

</div>

The set of all such automorphisms forms a group under composition.

## Gauge transformations

We now identify gauge transformations with fiber automorphisms.

<div class="definition">

**Definition 10** (Gauge transformation). A *gauge transformation* is a fiber automorphism arising from a lens obstruction, i.e. an admissible transformation that maps one local lift of a coherent structure to another equally admissible lift without altering any observable or kinematic content.

</div>

Gauge transformations therefore act on representations, not on the underlying coherent structures themselves.

## Gauge encoding versus physical realizations

Gauge structure, as defined in this paper, is an encoding class that resolves lens obstructions by organizing redundancy of representation. It does not correspond to any particular physical interaction.

<div class="remark">

*Remark 11*. Electromagnetism, weak interactions, and strong interactions are *distinct realizations* of gauge encoding, characterized by different gauge groups, representations, and dynamics. The existence of gauge encoding does not imply the existence of any particular force; it implies only that some redundancy bookkeeping must exist wherever lens obstructions are present.

</div>

<div class="remark">

*Remark 12*. Different coherent structures may admit different local isotropy groups, and there is no requirement that a single gauge group act universally on all structures. Universality of gauge encoding refers to the inevitability of redundancy bookkeeping when lens obstructions exist, not to universality of a specific gauge interaction.

</div>

## Local nature of gauge freedom

Gauge transformations are defined locally on admissible domains.

<div class="remark">

*Remark 13*. Gauge freedom is local because lens obstructions are local: redundancy of lifts is detected within encoding fibers on admissible domains. Global gauge transformations exist only when compatible local automorphisms can be chosen on all domains, which is generically obstructed.

</div>

This locality is structural, not imposed.

## Gauge equivalence

Gauge transformations induce an equivalence relation on local lifts.

<div class="definition">

**Definition 14** (Gauge equivalence). Two local lifts $`z_1, z_2 \in Z_\alpha`$ are *gauge equivalent* if there exists a gauge transformation $`g_\alpha`$ such that $`z_2 = g_\alpha(z_1)`$.

</div>

Physical (coherent) content is invariant under gauge equivalence.

## Gauge invariants

Because gauge transformations encode redundancy, only gauge-invariant quantities are meaningful descriptors of coherent structure.

<div class="definition">

**Definition 15** (Gauge-invariant quantity). A *gauge-invariant quantity* is a function or diagnostic on encoding fibers that is constant on gauge-equivalence classes.

</div>

<div class="remark">

*Remark 16*. Gauge invariants arise naturally as those features of the encoding that descend to the quotient by fiber automorphisms. This quotient is the maximal reduced description compatible with lens obstructions.

</div>

## Distinction from gravity

We emphasize the distinction between gauge and gravity encodings.

<div class="remark">

*Remark 17*. Gauge transformations resolve redundancy of representation (lens obstructions). They do not resolve path-dependent inconsistency of continuation (circle obstructions). Conversely, the kinematic consistency encoding identified as gravity resolves circle obstructions but does not eliminate redundancy of local lifts. The two encodings address distinct structural problems and must not be conflated.

</div>

## Uniqueness of gauge encoding

We now show that gauge structure is the unique encoding response to lens obstructions.

<div class="theorem">

**Theorem 18** (Universality of redundancy encoding). *Any admissible resolution of lens obstructions must factor through the quotient groupoid obtained by modding encoding fibers by their isotropy (automorphism) action. Consequently, any such resolution is equivalent, up to admissible re-encoding, to a redundancy encoding implemented by fiber automorphisms.*

</div>

<div class="proof">

*Proof.* Any admissible redundancy-resolution functor must identify all gauge-equivalent lifts while preserving overlap consistency. This is precisely the universal property of the quotient groupoid defined by fiber isotropy. Therefore any such resolution factors uniquely through this quotient and is equivalent to the gauge (redundancy) encoding. ◻

</div>

<div class="remark">

*Remark 19* (Universality of gauge revisited). Universality of gauge structure in this context means that whenever lens obstructions exist, some redundancy encoding must be present locally. It does not mean that a single gauge group acts on all coherent structures. Different lens obstructions may induce different local isotropy groups in different encodings.

</div>

<div class="theorem">

**Theorem 20** (Uniqueness of gauge encoding). *Any admissible encoding that resolves lens obstructions while preserving overlap consistency and kinematic persistence is equivalent, up to admissible re-encoding, to a redundancy encoding implemented by fiber automorphisms.*

</div>

<div class="proof">

*Proof.* Let $`\mathcal G`$ be an encoding resolving lens obstructions. By definition, it must identify all admissible local lifts as equivalent representations of the same coherent structure. This identification defines an equivalence relation on encoding fibers generated by admissible automorphisms. Any alternative encoding that preserves coherent content and overlap consistency must factor through this equivalence. Therefore $`\mathcal G`$ is equivalent, up to admissible re-encoding, to a redundancy encoding realized by fiber automorphisms. ◻

</div>

## Preview: gauge fixing and connections

While gauge transformations encode redundancy, one may choose specific representatives for calculational or practical purposes.

<div class="remark">

*Remark 21*. Gauge fixing corresponds to a non-canonical choice of local section within a gauge-equivalence class. Such choices do not alter the underlying encoding structure and may fail globally due to lens obstructions.

</div>

In the next section we analyze gauge fixing and show how, in smooth realization classes, gauge redundancy is organized by bundle structure and connection-like objects distinct from gravitational connections.

# Gauge Fixing and Redundancy Bookkeeping

In this section we analyze gauge fixing within the redundancy encoding framework and show how bookkeeping of redundancy gives rise to connection-like structures in smooth realization classes. We emphasize throughout that these structures are not gravitational: they resolve redundancy (lens obstructions), not kinematic path dependence (circle obstructions).

## Gauge fixing as section selection

Gauge fixing corresponds to selecting a representative from each gauge-equivalence class.

<div class="definition">

**Definition 22** (Gauge fixing). A *gauge fixing* on an admissible domain $`A_\alpha`$ is a choice of local section
``` math
s_\alpha : A_\alpha \to Z_\alpha
```
such that $`s_\alpha(x)`$ selects a single representative from each gauge-equivalence class in the encoding fiber over $`x`$.

</div>

Gauge fixing is therefore a choice of description, not a structural operation.

## Non-canonicity of gauge fixing

We now show that gauge fixing is generically non-canonical.

<div class="theorem">

**Theorem 23** (Non-existence of global gauge fixing). *If a lens obstruction exists, then no globally admissible gauge fixing exists.*

</div>

<div class="proof">

*Proof.* A global gauge fixing is a global section selecting one representative per gauge-equivalence class. Such a section would be invariant under all fiber automorphisms. This contradicts the existence of a nontrivial isotropy group acting on the fibers. Hence no global gauge fixing exists. ◻

</div>

<div class="remark">

*Remark 24*. Local gauge fixing may exist on individual admissible domains, but cannot be extended consistently across the entire atlas.

</div>

## Gauge transitions on overlaps

On overlaps of admissible domains, different gauge fixings are related by gauge transformations.

<div class="definition">

**Definition 25** (Gauge transition). Let $`s_\alpha`$ and $`s_\beta`$ be gauge fixings on overlapping admissible domains $`A_\alpha`$ and $`A_\beta`$. The *gauge transition* on $`A_{\alpha\beta}`$ is the gauge transformation $`g_{\alpha\beta}`$ such that
``` math
s_\beta(x) = g_{\alpha\beta}(x)\, s_\alpha(x)
```
for all $`x \in A_{\alpha\beta}`$.

</div>

Gauge transitions encode how different local gauge choices are related.

## Redundancy bookkeeping

Because gauge fixing is non-canonical, redundancy must be tracked explicitly.

<div class="remark">

*Remark 26*. Redundancy bookkeeping assigns data to overlaps that records how local gauge choices differ. This bookkeeping ensures consistency of reduced descriptions without privileging any particular gauge.

</div>

This bookkeeping role is the defining function of gauge structure in MTT.

## Smooth realizations and gauge connections

We now show how redundancy bookkeeping is realized geometrically in smooth settings.

<div class="theorem">

**Theorem 27** (Gauge connection realization). *In smooth realization classes, redundancy bookkeeping is realized by a connection-like object on a principal bundle whose structure group is the gauge automorphism group of encoding fibers.*

</div>

<div class="proof">

*Proof.* Gauge transitions $`g_{\alpha\beta}(x)`$ define smooth maps on overlaps. Consistency of these transitions under refinement and composition requires infinitesimal control of how gauge choices vary. The unique structure implementing such control is a connection on the associated principal bundle. This connection records how to compare gauge choices infinitesimally without selecting a preferred global representative. ◻

</div>

<div class="remark">

*Remark 28* (Electromagnetism as a mixed realization). Electromagnetism provides an important example in which lens and circle obstructions coexist within a single realization. The U(1) phase redundancy of electromagnetism realizes a lens obstruction resolved by gauge encoding, while the associated holonomy around closed loops realizes a circle obstruction. The present separation of gauge and gravity reflects a distinction of structural roles, not a claim that physical theories realize only one obstruction type at a time.

</div>

## Distinction from gravitational connection

We stress the distinction between gauge connections and gravitational connections.

<div class="remark">

*Remark 29*. Gauge connections arise to track redundancy of representation (lens obstructions). Gravitational connections arise to resolve kinematic path dependence (circle obstructions). Although both are realized geometrically as connections, they encode distinct structural roles and should not be conflated.

</div>

This distinction is structural and persists independently of particular realization choices.

## Gauge invariance revisited

Gauge invariance is now seen as invariance under redundancy bookkeeping.

<div class="remark">

*Remark 30*. Gauge invariance expresses the fact that physical (coherent) content is invariant under changes of representative within a gauge-equivalence class. It is not a symmetry of the underlying system, but a statement about redundancy of description.

</div>

## Preview: coupling to other encodings

Gauge structure may interact with other encoding classes in particular realizations.

<div class="remark">

*Remark 31*. In unified or saturated encodings, gauge redundancy bookkeeping may couple to kinematic consistency bookkeeping (gravity) or to discrete constraint encodings (quantization). Such couplings are realization-dependent and do not alter the structural separation of encoding roles established here.

</div>

<div class="remark">

*Remark 32* (Circle realizations and gravity). Circle obstructions denote loop-dependent failure of global coherence. Different encodings may realize this obstruction in different regimes. When circle affects internal or phase transport, electromagnetism provides a minimal realization. When circle affects kinematic persistence itself—worldlines, causal cones, and horizons—a gravity-like kinematic consistency encoding is forced. These are distinct realizations of the same structural invariant.

</div>

# Summary and Outlook

In this paper we have identified gauge structure as a necessary encoding class arising from lens obstructions in the Modal Triplet Theory framework. Lens obstructions correspond to non-unique but admissible local representations of coherent structure, with full overlap consistency and kinematic persistence. Such redundancy cannot be eliminated by refinement or admissible re-encoding and therefore requires explicit bookkeeping.

We showed that this bookkeeping is uniquely implemented by a redundancy encoding whose transformations act as automorphisms of encoding fibers. Gauge transformations are thus not symmetries of an underlying physical arena, but automorphisms of representation that relate equally valid local lifts. Gauge equivalence expresses invariance of coherent content under changes of representative, and gauge fixing corresponds to a non-canonical choice of local section that cannot be extended globally in the presence of lens obstructions.

In smooth realization classes, redundancy bookkeeping is realized geometrically by principal bundles equipped with connection-like objects that track transitions between local gauge choices. These gauge connections are structurally distinct from the gravitational connections introduced to resolve circle obstructions. Although both appear as connections in geometric realizations, they encode different kinds of bookkeeping: gauge resolves redundancy of representation, while gravity resolves path-dependent kinematic inconsistency.

The results of this paper complete the identification of gauge structure within the Modal Triplet Theory Program. Together with the gravity-as-encoding paper, they establish that two of the three fundamental obstruction types—circle and lens—require distinct and unavoidable encoding responses. The remaining obstruction type, nil, corresponds to termination of describability and motivates a discrete constraint encoding, treated in the subsequent paper on quantization.

More broadly, this analysis clarifies why gauge structure is universal yet unobservable directly, why gauge fixing is inherently non-canonical, and why gauge symmetry appears as a freedom of description rather than as a property of underlying reality. These features are not postulated; they are forced by the structure of local describability and overlap consistency.

Subsequent papers in the series develop the encoding response to nil obstructions (quantization), analyze the intersection and saturation of multiple encoding classes (including the Standard Model and string-theoretic frameworks), and construct explicit realizations in geometric and bundle-based models. No additional structural assumptions are introduced downstream.

In this way, gauge structure emerges as an inevitable component of any coherent descriptive framework once redundancy of representation is present, completing the lens branch of the circle–lens–nil triad.

<div class="remark">

*Remark 33* (Universality clarified). Universality of gauge structure in the Modal Triplet Theory framework means that whenever lens obstructions exist, some redundancy encoding must exist locally. It does not mean that a single gauge group, interaction, or coupling acts on all coherent structures. Different realizations may exhibit different gauge groups, or none at all, depending on the presence and nature of lens obstructions.

</div>
