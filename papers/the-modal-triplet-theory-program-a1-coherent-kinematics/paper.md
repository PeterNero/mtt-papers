---
abstract: |
  We develop a kinematic framework for Modal Triplet Theory (MTT) that does not presuppose spacetime, geometry, or equations of motion. Kinematics is defined structurally, in terms of persistence of coherent structures across overlapping admissible encodings in the encoding atlas. Motion is identified with admissible continuation through chains of overlapping descriptions, while worldlines are equivalence classes of such continuations under re-encoding.

  We show that causal structure, horizon formation, and irreversibility arise as inevitable consequences of finite admissibility and obstruction to global description. Null and timelike distinctions are derived from admissible continuation properties rather than from a metric. No dynamical laws are assumed; the results apply to all realization classes compatible with the MTT structural core.

  This work provides the kinematic layer of the MTT program, bridging the abstract classification of reduced descriptions and the downstream encoding-class papers in which gravity, gauge structure, and quantization emerge as bookkeeping responses to structural obstructions.
author:
- Peter Nero
current_version: v1.0
date: January 2026
generated_from_main_tex_sha256: d52feeb32fe111cdd7cda9add7969feb470d6b68be6033d6926fd8fed7e921f8
paper_id: the-modal-triplet-theory-program-a1-coherent-kinematics
release_state: zenodo_released
released_version: v1.0
title: "The Modal Triplet Theory Program A1: Coherent Kinematics"
zenodo_doi: 10.5281/zenodo.18354943
zenodo_record_id: 18354943
zenodo_url: "https://zenodo.org/records/18354943"
---

# Introduction and Scope

The structural core of Modal Triplet Theory establishes when reduced descriptions exist, how they relate on overlaps, and why no single global description can exist. These results are deliberately pre-kinematic: they do not assume spacetime, trajectories, or equations of motion. Nevertheless, any theory that admits persistent reduced descriptions must address a basic question: *what does it mean for something to move, persist, or propagate when no global kinematic arena exists?*

The purpose of the present paper is to answer this question at the structural level. We develop a notion of kinematics that is intrinsic to the encoding atlas of Modal Triplet Theory. In this framework, kinematics is not defined by motion through a background space, but by persistence of coherent structure across admissible overlaps of local descriptions.

Specifically, we show that:

- *Position* is an encoding-relative notion defined by support of coherent structure within a local description.

- *Motion* corresponds to admissible continuation through chains of overlapping encodings.

- *Worldlines* are equivalence classes of admissible continuations under re-encoding.

- *Horizons* and *termination of motion* arise when admissible continuation fails (nil obstructions).

- *Irreversibility* follows from the absence of global sections and the terminal nature of nil.

Throughout this work, no metric, connection, or dynamical law is assumed. The results are purely structural and apply uniformly across all realization classes compatible with the MTT core. Geometry and dynamics, when they appear in later papers, are shown to encode and stabilize the kinematic structures identified here rather than to define them.

<div class="remark">

*Remark 1* (Relation to the series). This paper depends only on the structural core of Modal Triplet Theory and the encoding atlas it defines. It precedes the encoding-class papers on gravity, gauge structure, and quantization, and provides the kinematic interpretation required to understand those encodings as responses to structural obstructions rather than as fundamental postulates.

</div>

# Encoding-Relative Configuration and Position

We begin by defining the kinematic notions of configuration and position without reference to a background space. All definitions are relative to admissible encodings in the encoding atlas.

## Encoding-relative configuration

Let $`\mathcal E_\alpha = (A_\alpha, Z_\alpha, E_\alpha, \ldots)`$ be an admissible encoding on domain $`A_\alpha \subset X`$.

<div class="definition">

**Definition 2** (Encoding-relative configuration). The *configuration* of a coherent structure with respect to an encoding $`\mathcal E_\alpha`$ is its image in the reduced variable space $`Z_\alpha`$ under the encoding map $`E_\alpha`$.

</div>

Configurations are therefore encoding-dependent. There is no notion of a configuration independent of an encoding.

<div class="remark">

*Remark 3*. Different encodings may assign different configurations to the same coherent structure. Overlap consistency ensures that these configurations are related by admissible re-encoding on intersections of admissible domains.

</div>

## Support of coherent structure

The notion of position requires a notion of localization within an encoding.

<div class="definition">

**Definition 4** (Support). Let $`B \subset A_\alpha`$ be the subset of the admissible domain on which a given coherent structure is represented. The *support* of the structure in the encoding $`\mathcal E_\alpha`$ is the image
``` math
\mathrm{supp}_\alpha := E_\alpha(B) \subset Z_\alpha.
```

</div>

Support captures where, within the encoding-relative configuration space, the coherent structure is localized.

## Position as an encoding-relative diagnostic

We now define position in purely kinematic terms.

<div class="definition">

**Definition 5** (Position). A *position* in encoding $`\mathcal E_\alpha`$ is any admissible diagnostic functional
``` math
\mathrm{pos}_\alpha : \mathcal P(Z_\alpha) \to \mathcal Q_\alpha
```
that assigns to the support $`\mathrm{supp}_\alpha`$ a value in some diagnostic space $`\mathcal Q_\alpha`$ (for example, a coordinate tuple, region label, or coarse localization class).

</div>

Position is therefore:

- encoding-relative,

- diagnostic rather than fundamental,

- defined only where an encoding is admissible.

<div class="remark">

*Remark 6*. No assumption is made that $`\mathcal Q_\alpha`$ carries a metric, topology, or linear structure. Such structure may appear in particular realizations but is not required at the kinematic level.

</div>

## Consistency of position on overlaps

On overlaps of admissible domains, positions defined in different encodings must be mutually consistent.

<div class="definition">

**Definition 7** (Position compatibility). Let $`\mathcal E_\alpha`$ and $`\mathcal E_\beta`$ be admissible encodings with nonempty overlap $`A_{\alpha\beta}`$. Position diagnostics $`\mathrm{pos}_\alpha`$ and $`\mathrm{pos}_\beta`$ are *compatible* if there exists an admissible re-encoding map $`f_{\alpha\beta}`$ such that
``` math
\mathrm{pos}_\beta\bigl(E_\beta(B)\bigr)
\;\sim\;
\mathrm{pos}_\alpha\bigl(E_\alpha(B)\bigr)
```
for all coherent supports $`B \subset A_{\alpha\beta}`$, where $`\sim`$ denotes admissible equivalence.

</div>

This condition ensures that different local notions of position do not contradict one another on overlaps.

## Absence of global position

Finite admissibility implies that no single global notion of position exists.

<div class="theorem">

**Theorem 8** (No global position). *If the admissible domains do not admit a global encoding, then there exists no globally defined position diagnostic consistent with all admissible encodings.*

</div>

<div class="proof">

*Proof.* A globally defined position would require a global encoding whose restriction to each admissible domain reproduces the local position diagnostics. This contradicts finite admissibility. ◻

</div>

<div class="remark">

*Remark 9*. The absence of global position is not a deficiency of the theory but a structural feature. It reflects the impossibility of global reduced description established in the MTT core.

</div>

## Preview: from position to motion

Position as defined above is purely static and encoding-relative. In the next section we introduce *admissible continuation* across overlapping encodings and define motion as persistence of coherent structure along such continuations.

# Admissible Continuation and Motion

Having defined configuration and position relative to admissible encodings, we now introduce the central kinematic notion of *motion*. In Modal Triplet Theory, motion is not defined as change of position in a background space, but as persistence of coherent structure across chains of overlapping admissible encodings.

## Admissible continuation

Let $`\mathcal E_\alpha = (A_\alpha, Z_\alpha, E_\alpha, \ldots)`$ and $`\mathcal E_\beta = (A_\beta, Z_\beta, E_\beta, \ldots)`$ be admissible encodings with nonempty overlap $`A_{\alpha\beta}`$.

<div class="definition">

**Definition 10** (Admissible continuation). A coherent structure represented in $`\mathcal E_\alpha`$ is said to admit an *admissible continuation* to $`\mathcal E_\beta`$ if there exists a subset $`B \subset A_{\alpha\beta}`$ such that the representation in $`Z_\alpha`$ can be re-encoded consistently into $`Z_\beta`$ via the admissible re-encoding map $`f_{\alpha\beta}`$.

</div>

Admissible continuation is therefore a relation between encodings, not a map on a fixed configuration space.

## Chains of continuation

Motion arises when admissible continuation exists along a sequence of overlaps.

<div class="definition">

**Definition 11** (Continuation chain). A *continuation chain* is a finite or infinite sequence of admissible encodings
``` math
\mathcal E_{\alpha_1}, \mathcal E_{\alpha_2}, \ldots
```
such that admissible continuation exists from $`\mathcal E_{\alpha_i}`$ to $`\mathcal E_{\alpha_{i+1}}`$ for all $`i`$.

</div>

Continuation chains encode the possibility of persistent description without requiring a global kinematic arena.

## Motion as persistence

We now define motion itself.

<div class="definition">

**Definition 12** (Motion). A coherent structure is said to be *in motion* if it admits an admissible continuation along a nontrivial continuation chain of encodings.

</div>

Motion is thus:

- encoding-relative,

- local to admissible domains,

- defined by persistence of representation rather than by displacement.

<div class="remark">

*Remark 13*. A structure that admits continuation only within a single encoding but not across overlaps is stationary in that encoding, but may fail to be stationary globally due to the absence of global coherence.

</div>

## Directionality and ordering

Continuation chains naturally induce an ordering, but not a global time parameter.

<div class="definition">

**Definition 14** (Kinematic ordering). A *kinematic ordering* is the partial order on admissible encodings induced by admissible continuation: $`\mathcal E_\alpha \prec \mathcal E_\beta`$ if admissible continuation exists from $`\mathcal E_\alpha`$ to $`\mathcal E_\beta`$.

</div>

This ordering replaces external time in the kinematic description.

<div class="remark">

*Remark 15*. The kinematic ordering is generally not total. Branching, merging, and terminal chains are possible, reflecting the absence of global coherence.

</div>

## Reversibility and local symmetry

Admissible continuation need not be symmetric.

<div class="definition">

**Definition 16** (Local reversibility). A continuation from $`\mathcal E_\alpha`$ to $`\mathcal E_\beta`$ is *locally reversible* if admissible continuation also exists from $`\mathcal E_\beta`$ back to $`\mathcal E_\alpha`$.

</div>

<div class="remark">

*Remark 17*. Local reversibility may hold within restricted regions of the encoding atlas, but fails globally when nil obstructions or selection fronts are encountered. This asymmetry underlies the emergence of irreversibility.

</div>

## Motion without background space

We emphasize that no notion of distance, velocity, or trajectory in a background space has been assumed.

<div class="remark">

*Remark 18*. Motion as defined here is compatible with many downstream realizations, including geometric ones, but does not presuppose them. Any appearance of spacetime motion in later encoding classes arises as an interpretation of continuation structure, not as a primitive kinematic input.

</div>

## Preview: worldlines

Continuation chains are not unique: different chains may represent the same persistent structure under re-encoding. In the next section we define *worldlines* as equivalence classes of admissible continuation chains.

# Worldlines as Equivalence Classes of Continuation

In the absence of a global kinematic arena, the notion of a worldline must be reformulated. In Modal Triplet Theory, a worldline is not a curve in space or spacetime, but an equivalence class of admissible continuation chains representing the persistence of a coherent structure across overlapping descriptions.

## Non-uniqueness of continuation chains

Given a coherent structure represented in an admissible encoding $`\mathcal E_\alpha`$, there may exist multiple admissible continuation chains emanating from $`\mathcal E_\alpha`$ that track the same structure across different sequences of overlaps.

<div class="remark">

*Remark 19*. Distinct continuation chains may differ in:

- the choice of intermediate encodings;

- the order in which overlaps are traversed;

- the protocol or admissible re-encoding used on overlaps.

Despite these differences, the chains may represent the same persistent coherent structure.

</div>

This non-uniqueness reflects the absence of a preferred global parametrization.

## Equivalence of continuation chains

We now formalize when two continuation chains represent the same worldline.

<div class="definition">

**Definition 20** (Worldline equivalence). Two admissible continuation chains
``` math
\{\mathcal E_{\alpha_1}, \mathcal E_{\alpha_2}, \ldots\}
\quad \text{and} \quad
\{\mathcal E_{\beta_1}, \mathcal E_{\beta_2}, \ldots\}
```
are said to be *equivalent* if, for every finite segment of one chain, there exists a finite segment of the other such that the corresponding representations are related by admissible re-encoding on overlapping domains.

</div>

Equivalence is therefore defined by mutual representability rather than by pointwise identification.

## Definition of worldline

<div class="definition">

**Definition 21** (Worldline). A *worldline* is an equivalence class of admissible continuation chains under the equivalence relation defined above.

</div>

Worldlines encode kinematic identity without reference to background space, time, or parametrization.

## Worldlines and the atlas nerve

Continuation chains correspond naturally to paths in the atlas nerve.

<div class="remark">

*Remark 22*. A continuation chain defines a path in the $`1`$-skeleton of the atlas nerve. Worldline equivalence identifies paths that differ by homotopy through admissible re-encoding. In this sense, worldlines correspond to homotopy classes of admissible paths in the atlas nerve.

</div>

This interpretation makes clear that worldlines are global objects defined by the overlap structure of admissible descriptions.

## Branching and merging

Worldlines need not be unique or isolated.

<div class="definition">

**Definition 23** (Branching and merging). A worldline *branches* if there exist inequivalent continuation classes that coincide up to some encoding and then diverge. A worldline *merges* if distinct classes become equivalent after a common continuation.

</div>

<div class="remark">

*Remark 24*. Branching and merging reflect the partial nature of kinematic ordering and the absence of a total time parameter. They are generic features in the presence of finite admissibility.

</div>

## Terminal worldlines

Worldlines may terminate.

<div class="definition">

**Definition 25** (Terminal worldline). A worldline is *terminal* if it admits no admissible continuation beyond a finite chain. Equivalently, its continuation encounters a nil obstruction.

</div>

Terminal worldlines encode horizons, collapse, and termination of motion without requiring singular behavior of the underlying system.

## Irreversibility of worldlines

The absence of global coherence implies that worldline equivalence classes are generally not reversible.

<div class="theorem">

**Theorem 26** (Irreversibility of worldlines). *If a worldline is terminal or passes through a region of nil obstruction, then no admissible continuation exists that retraces the worldline beyond that point.*

</div>

<div class="proof">

*Proof.* By definition of nil obstruction, no admissible encoding exists beyond the terminal point. Therefore no continuation chain can be extended through or beyond that region, and reversal is impossible. ◻

</div>

<div class="remark">

*Remark 27*. Irreversibility here is kinematic rather than dynamical. It arises from the structure of admissible descriptions, not from time-asymmetric equations of motion.

</div>

## Preview: causal structure

Worldlines provide the foundation for defining causal relations among coherent structures. In the next section we show how admissible continuation induces a causal partial order and how null and timelike distinctions emerge from kinematic constraints.

# Causal Structure and Kinematic Classification

Having defined motion as admissible continuation and worldlines as equivalence classes of continuation chains, we now extract causal structure directly from the kinematic ordering induced by admissibility. No background time, metric, or dynamical law is assumed.

## Causal precedence

Admissible continuation induces a partial causal order.

<div class="definition">

**Definition 28** (Causal precedence). Given two admissible encodings $`\mathcal E_\alpha`$ and $`\mathcal E_\beta`$, we say that $`\mathcal E_\alpha`$ *causally precedes* $`\mathcal E_\beta`$, written
``` math
\mathcal E_\alpha \prec \mathcal E_\beta,
```
if there exists an admissible continuation chain from $`\mathcal E_\alpha`$ to $`\mathcal E_\beta`$.

</div>

This relation is reflexive and transitive but not necessarily antisymmetric, reflecting the absence of global coherence.

<div class="remark">

*Remark 29*. Causal precedence is defined on encodings, not on an external time parameter. It is therefore intrinsic to the structure of admissible descriptions.

</div>

## Causal relations between worldlines

Causal relations extend naturally to worldlines.

<div class="definition">

**Definition 30** (Worldline causality). A worldline $`W_1`$ causally precedes a worldline $`W_2`$ if there exist representatives $`\mathcal E_\alpha \in W_1`$ and $`\mathcal E_\beta \in W_2`$ such that $`\mathcal E_\alpha \prec \mathcal E_\beta`$.

</div>

This defines a partial order on worldlines modulo equivalence.

## Null and timelike continuation

We now distinguish different classes of admissible continuation.

<div class="definition">

**Definition 31** (Null continuation). An admissible continuation from $`\mathcal E_\alpha`$ to $`\mathcal E_\beta`$ is *null* if any admissible continuation chain between them is minimal, in the sense that no intermediate admissible encoding can be inserted without losing admissibility.

</div>

<div class="definition">

**Definition 32** (Timelike continuation). An admissible continuation from $`\mathcal E_\alpha`$ to $`\mathcal E_\beta`$ is *timelike* if there exists at least one admissible continuation chain between them containing intermediate encodings.

</div>

<div class="remark">

*Remark 33*. Null and timelike classifications are kinematic and encoding-relative. They do not presuppose a metric or causal cone, but arise from the structure of admissible continuation itself.

</div>

## Causal cones

The distinction between null and timelike continuation induces a cone-like structure.

<div class="definition">

**Definition 34** (Causal cone). The *causal cone* of an encoding $`\mathcal E_\alpha`$ is the set of encodings $`\mathcal E_\beta`$ such that $`\mathcal E_\alpha \prec \mathcal E_\beta`$.

</div>

Null continuations form the boundary of the causal cone, while timelike continuations form its interior.

<div class="remark">

*Remark 35*. This cone structure is purely order-theoretic and does not rely on any notion of distance or angle. Its resemblance to light cones is a derived feature that appears in suitable realizations.

</div>

## Horizons as kinematic boundaries

Finite admissibility implies that causal cones may be bounded.

<div class="definition">

**Definition 36** (Kinematic horizon). A *kinematic horizon* is a boundary in the causal cone of a worldline beyond which no admissible continuation exists.

</div>

<div class="remark">

*Remark 37*. Kinematic horizons arise when continuation chains terminate in nil obstructions. They are not assumed; they follow directly from finite admissibility.

</div>

## Global causal failure

The absence of a global encoding implies that causal structure is itself only locally defined.

<div class="theorem">

**Theorem 38** (No global causal ordering). *There exists no globally defined total causal order on all worldlines consistent with admissible continuation.*

</div>

<div class="proof">

*Proof.* A global total order would require a global encoding in which all admissible continuations could be embedded. This contradicts finite admissibility. ◻

</div>

## Irreversibility revisited

Causal structure provides an additional perspective on irreversibility.

<div class="remark">

*Remark 39*. Irreversibility arises because causal precedence is not invertible across kinematic horizons and nil obstructions. This is a structural property of the encoding atlas rather than a dynamical asymmetry.

</div>

## Preview: relation to geometry

The kinematic causal structure derived here will later be shown to require additional bookkeeping to remain consistent under refinement. In particular, the stabilization of causal cones and null boundaries motivates the emergence of geometric and gravitational encoding structures in subsequent papers.

# Horizons, Selection, and Termination

In this section we analyze the kinematic consequences of finite admissibility. We show how horizons, selection events, and termination of motion arise structurally from the encoding atlas, without invoking dynamics, measurement postulates, or external time.

## Finite admissibility and kinematic reach

Finite admissibility implies that admissible continuation cannot persist indefinitely along all directions.

<div class="definition">

**Definition 40** (Kinematic reach). The *kinematic reach* of an encoding $`\mathcal E_\alpha`$ is the set of encodings $`\mathcal E_\beta`$ such that $`\mathcal E_\alpha \prec \mathcal E_\beta`$ via admissible continuation.

</div>

Kinematic reach is generally bounded due to the presence of nil obstructions.

## Horizons as boundaries of continuation

We now formalize horizons purely kinematically.

<div class="definition">

**Definition 41** (Kinematic horizon). A *kinematic horizon* relative to an encoding $`\mathcal E_\alpha`$ is a boundary point of its kinematic reach such that:

1.  admissible continuation exists up to the boundary;

2.  no admissible continuation exists beyond the boundary.

</div>

<div class="remark">

*Remark 42*. Kinematic horizons are not defined by distances or metrics. They are defined by the termination of admissible continuation and therefore exist even in the absence of geometric structure.

</div>

## Selection fronts

Horizon formation is typically associated with abrupt changes in admissibility.

<div class="definition">

**Definition 43** (Selection front). A *selection front* is a codimension-one subset of the encoding atlas (or of its nerve) across which the admissibility of continuation changes discontinuously, forcing a transition between distinct admissible continuations or between admissible continuation and termination.

</div>

Selection fronts are the loci at which the system must “choose” among remaining admissible encodings.

## Selection events

We now define selection in kinematic terms.

<div class="definition">

**Definition 44** (Selection event). A *selection event* occurs when a continuation chain reaches a selection front and admissible continuation persists only along a strict subset of the previously available directions.

</div>

<div class="remark">

*Remark 45*. Selection does not introduce randomness or collapse by assumption. It reflects the structural loss of admissible continuation options.

</div>

## Termination and nil revisited

When no admissible continuation remains, termination occurs.

<div class="definition">

**Definition 46** (Termination). A continuation chain *terminates* if it encounters a nil obstruction, i.e., a region with no admissible encoding.

</div>

Termination is therefore the kinematic manifestation of nil.

## Irreversibility from selection and termination

Selection and termination together imply irreversibility.

<div class="theorem">

**Theorem 47** (Kinematic irreversibility). *Once a continuation chain crosses a selection front or terminates at a nil obstruction, there exists no admissible continuation that retraces the chain beyond that point.*

</div>

<div class="proof">

*Proof.* By definition of selection fronts, admissible continuation options are strictly reduced. By definition of nil, no continuation exists. In either case, the set of admissible continuations is not symmetric under reversal. ◻

</div>

<div class="remark">

*Remark 48*. Irreversibility here is kinematic and structural. It does not rely on entropy, coarse-graining, or time-asymmetric dynamics.

</div>

## Records as persistent kinematic traces

Selection and termination give rise to records.

<div class="definition">

**Definition 49** (Record). A *record* is a persistent feature of a continuation chain that remains invariant under all subsequent admissible continuations.

</div>

<div class="remark">

*Remark 50*. Records arise when admissible continuation options narrow. They encode past selection events structurally, not dynamically.

</div>

## Preview: predictive limits

Selection fronts and horizons place intrinsic limits on prediction.

<div class="remark">

*Remark 51*. The existence of selection fronts implies that there exist kinematically well-defined questions about future continuation that cannot be resolved within any admissible encoding. This observation underlies the computational and predictive limits analyzed in a subsequent paper.

</div>

# Summary and Relation to Downstream Encodings

In this paper we have developed a notion of kinematics intrinsic to the encoding atlas of Modal Triplet Theory. Without assuming spacetime, geometry, or equations of motion, we have shown how configuration, position, motion, causal structure, horizons, selection, and irreversibility arise as structural features of admissible continuation across overlapping reduced descriptions.

The central kinematic insight is that persistence replaces displacement as the primitive notion of motion. Coherent structures move insofar as their representation persists across chains of admissible encodings. Worldlines are equivalence classes of such continuation chains, and causal structure is induced by the partial ordering defined by admissibility. Null and timelike distinctions, horizons, and termination of motion follow directly from the structure of admissible continuation and finite admissibility.

These results are kinematic rather than dynamical. No metric, connection, or field equation has been introduced. Instead, kinematic structure is shown to be a consequence of the encoding atlas itself. Geometry and dynamics, when they appear in later papers, are not taken as defining kinematics but as encoding responses required to stabilize and organize the kinematic features identified here.

In particular:

- the stabilization of causal cones and null boundaries motivates the emergence of geometric and gravitational encoding structures;

- the organization of redundancy in admissible continuation motivates gauge encoding structures;

- the presence of selection fronts and horizons motivates discrete and quantized encoding constraints.

The present paper therefore occupies a precise position in the Modal Triplet Theory series. It depends only on the structural core and provides the kinematic interpretation necessary for understanding gravity, gauge structure, quantization, and unified encodings as downstream responses to structural obstructions rather than as fundamental postulates.

Together with the structural core and the obstruction classification developed elsewhere, this kinematic framework completes the pre-geometric layer of the theory.

<div class="remark">

*Remark 52* (Series progression). The logical progression of the series is as follows:

1.  the structural core establishes admissibility and the impossibility of global description;

2.  coherent kinematics defines motion, causality, and irreversibility without spacetime;

3.  obstruction classification explains why circle, lens, and nil are inevitable;

4.  encoding-class papers develop gravity, gauge structure, and quantization as bookkeeping responses;

5.  realization papers instantiate these encodings geometrically.

</div>
