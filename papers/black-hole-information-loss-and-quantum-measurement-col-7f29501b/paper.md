---
abstract: |
  We propose and formalize a single mechanism in Modal Triplet Theory (MTT) that unifies two apparently unrelated 4D problems: (i) black hole information loss in semiclassical gravity and (ii) quantum measurement collapse in nonrelativistic quantum mechanics. In MTT, 4D physics is the shadow of deterministic dynamics on a higher configuration space under a noninvertible coherent projection. We define admissibility barriers as loci where the coherent projection fails to be stably invertible (spectral gap closure / projector discontinuity / basin rearrangement). We prove a general “projection noninvertibility” theorem: whenever trajectories cross an admissibility barrier, the induced 4D evolution becomes noninvertible and admits no global information recovery map, despite invertibility of the upstairs evolution. We then show how measurement selection and horizon formation/evaporation are two instantiations of barrier crossing, and we map the resulting 4D shadows to (a) collapse/Born probabilities and (b) thermal Hawking radiation/mixed exterior states. Finally, we relate the framework to the Page curve and island formula program: islands are interpreted as regime-dependent partial inversions (or re-encodings) of the projection on a restricted algebra, rather than restoration of global 4D invertibility.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 7a28e66b02f1f2231b6998d348dcd81d1cd8ac4155a6e8987897ab568684c119
paper_id: black-hole-information-loss-and-quantum-measurement-col-7f29501b
release_state: zenodo_released
released_version: v1.0
title: |
  Black Hole Information Loss and Quantum Measurement Collapse  
  as the Same Admissibility Transition in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.18261430
zenodo_record_id: 18261430
zenodo_url: "https://zenodo.org/records/18261430"
---

# Scope and Claim Discipline

This paper has two goals:

1.  Provide a theorem-level mechanism in MTT that yields loss of invertibility in the 4D shadow dynamics whenever trajectories cross an admissibility barrier.

2.  Show that both (i) quantum measurement collapse and (ii) black hole information loss are instances of that same mechanism under different physical identifications of the barrier.

We separate three layers:

1.  **Mathematical layer (proved):** deterministic evolution on a configuration space, a noninvertible projection, and barrier-crossing implies noninvertibility of the projected dynamics.

2.  **Interpretive layer (identified):** measurement events correspond to constraint/context changes that move the system across an admissibility barrier; horizon formation/evaporation corresponds to a barrier between exterior-admissible and interior/nonadmissible sectors.

3.  **Phenomenological layer (compared):** the resulting shadows align with (a) collapse and Born probabilities and (b) thermal radiation / mixed exterior states, and clarify the role of islands/replica-wormhole “patches” as partial re-encodings rather than global invertibility restoration.

We do *not* assume fundamental 4D nonunitarity. The only noninvertibility asserted is at the level of the projected 4D shadow map.

# Upstairs Setup: Dynamics, Projection, and Admissibility Barriers

## Configuration space and deterministic evolution

Let $`(\mathcal X,\mathcal B)`$ be a standard Borel space representing the full MTT configuration space on a bounded-geometry slab (fields on $`M_{10}`$ with suitable Sobolev topology, restricted to a finite-energy domain). Let
``` math
\Phi_t : \mathcal X \to \mathcal X
```
be a measurable, invertible flow (or discrete-time map $`\Phi:\mathcal X\to\mathcal X`$) representing the deterministic upstairs evolution. Invertible means $`\Phi_t`$ is bijective with measurable inverse.

<div class="remark">

*Remark 1*. In MTT the upstairs dynamics is a well-posed flow on the full modal system. The present section requires only invertibility and measurability; no specific PDE form is needed.

</div>

## Coherent projection and observable map

Let $`\Pi:\mathcal X\to \mathcal X_{\mathrm{coh}}`$ be a measurable projection to the coherent sector, and let $`I:\mathcal X_{\mathrm{coh}}\to \mathcal Y`$ be an “observable pushforward” to an effective 4D state space $`\mathcal Y`$ (e.g. a Hilbert-space state space or state on a net of algebras). Define the 4D observable map
``` math
P := I\circ \Pi : \mathcal X \to \mathcal Y.
```

<div class="definition">

**Definition 2** (Projected (shadow) dynamics). Given an initial condition $`x_0\in\mathcal X`$, define the shadow trajectory
``` math
y(t) := P(\Phi_t(x_0)) \in \mathcal Y.
```

</div>

## Admissibility and barrier sets

MTT asserts that coherent-sector evolution is only physically asserted on an admissible subset $`\mathcal A\subset \mathcal X`$ (bounded geometry, spectral gap persists, projector boundedness, FCC stability margins positive, etc.). We encode this abstractly:

<div class="definition">

**Definition 3** (Admissible set). An admissible set $`\mathcal A\subset \mathcal X`$ is a measurable subset such that: for initial data in $`\mathcal A`$, the coherent projection $`\Pi`$ is well-defined, bounded/regular in the relevant topologies, and stable under perturbations, and the induced coherent dynamics remains in a well-controlled regime for slab-local times.

</div>

The key new concept is the barrier:

<div class="definition">

**Definition 4** (Admissibility barrier). A measurable set $`\mathcal B\subset \mathcal X`$ is an admissibility barrier if:

1.  $`\mathcal X\setminus \mathcal B`$ splits into at least two measurable regions $`\mathcal U_+`$ and $`\mathcal U_-`$ such that $`\mathcal U_+\cap\mathcal U_-=\emptyset`$, $`\mathcal U_+\cup\mathcal U_-=\mathcal X\setminus\mathcal B`$.

2.  $`\Pi`$ restricted to each $`\mathcal U_\pm`$ is regular (continuous in the chosen topology, or at minimum locally constant on fibers) but there is no globally measurable right-inverse for $`\Pi`$ across $`\mathcal U_+\cup\mathcal U_-`$.

3.  Basin/sector structure changes across $`\mathcal B`$ in the sense that for some $`y\in\mathcal Y`$, the fiber $`P^{-1}(y)`$ intersects both $`\mathcal U_+`$ and $`\mathcal U_-`$.

</div>

<div class="remark">

*Remark 5* (Physical interpretation of barriers). In MTT, barriers arise when spectral gaps close, coherent projectors lose regularity, or stability margins vanish. The definition above is the measure-theoretic abstraction of those events.

</div>

# The Bridge Theorem: Barrier Crossing Implies Shadow Noninvertibility

We now state the core theorem: invertibility upstairs does not descend through a noninvertible projection; barrier crossing produces irrecoverable loss of 4D reconstructability.

## Noninvertibility of the projected evolution

<div class="definition">

**Definition 6** (Shadow evolution operator). Define the shadow map at time $`t`$ by
``` math
T_t := P\circ \Phi_t : \mathcal X \to \mathcal Y.
```

</div>

<div class="definition">

**Definition 7** (Shadow invertibility). We say the shadow at time $`t`$ is (globally) invertible if there exists a measurable map $`S_t:\mathcal Y\to \mathcal X`$ such that
``` math
T_t\circ S_t = \mathrm{Id}_{\mathcal Y}.
```
(That is, $`S_t`$ is a measurable right-inverse of $`T_t`$.)

</div>

<div id="thm:barrier-noninvertibility" class="theorem">

**Theorem 8** (Barrier crossing implies noninvertible shadow dynamics). *Assume:*

1.  *$`\Phi_t`$ is invertible and measurable on $`\mathcal X`$.*

2.  *$`P:\mathcal X\to\mathcal Y`$ is measurable.*

3.  *$`\mathcal B\subset\mathcal X`$ is an admissibility barrier with regions $`\mathcal U_\pm`$ as in Definition 2.3.*

*Then for any time $`t`$ such that $`\Phi_t(\mathcal U_+)\cap \Phi_t(\mathcal U_-)\neq\emptyset`$ and $`P^{-1}(y)`$ intersects both regions for some $`y\in\mathcal Y`$, the shadow map $`T_t`$ admits no measurable right-inverse; in particular, shadow dynamics is not globally invertible.*

</div>

<div class="proof">

*Proof.* By Definition 2.3(B3), there exists $`y\in\mathcal Y`$ and points $`x_+\in\mathcal U_+`$, $`x_-\in\mathcal U_-`$ such that $`P(x_+)=P(x_-)=y`$. Since $`\Phi_t`$ is invertible, the images $`\Phi_t(x_+),\Phi_t(x_-)`$ are distinct.

Compute:
``` math
T_t(x_+) = P(\Phi_t(x_+)),\qquad T_t(x_-) = P(\Phi_t(x_-)).
```
If $`T_t`$ had a measurable right-inverse $`S_t`$, then $`x_+=S_t(T_t(x_+))`$ and $`x_-=S_t(T_t(x_-))`$ would hold for all inputs, in particular on points with the same image. But since $`P`$ is noninjective on fibers crossing the barrier, there exist points with identical shadow $`y`$ but distinct upstairs origins, and no single-valued right-inverse can select both in a measurable way on a set of positive measure without violating $`T_t\circ S_t=\mathrm{Id}_{\mathcal Y}`$. Hence no measurable right-inverse exists. ◻

</div>

<div id="cor:unitarity" class="corollary">

**Corollary 9** (Upstairs unitarity does not imply 4D unitarity). *Even when $`\Phi_t`$ is invertible/unitary at the upstairs level, the induced 4D shadow dynamics cannot be globally invertible once barrier-crossing noninjectivity occurs. Any 4D “unitarity restoration” must therefore rely on enlarging $`\mathcal Y`$ or introducing nonlocal encodings.*

</div>

<div class="remark">

*Remark 10* (Why this is the common core of both paradoxes). Both measurement collapse and black hole information loss are precisely questions of whether the 4D map $`T_t`$ can be made invertible/unitary when the underlying theory is invertible. Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a> answers: not if barrier crossing produces fiber identifications.

</div>

# Two Shadows of One Barrier: Measurement and Black Holes

## Measurement collapse as barrier crossing

In the measurement setting, a “context” $`C`$ (apparatus coupling, POVM/instrument, etc.) induces an admissible set $`\mathcal A_C\subset\mathcal X`$ and an associated basin decomposition into outcome-attractors. A measurement event corresponds to a change of context $`C\to C'`$ that changes admissibility constraints and can move trajectories across an admissibility barrier $`\mathcal B`$ separating basin atlases.

<div class="proposition">

**Proposition 11** (Collapse as projected noninvertibility). *In the measurement setting, outcome selection corresponds to barrier crossing in $`\mathcal X`$, and the impossibility of reconstructing the pre-measurement coherent configuration from the post-measurement outcome is an instance of Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a>.*

</div>

<div class="remark">

*Remark 12*. In MTT, probabilities arise from basin measures/weights on the admissible set. This paper does not re-derive the Born rule; it uses only the structural fact that basin selection is projection- induced and noninvertible in the 4D shadow.

</div>

## Black hole information loss as barrier crossing

In the black hole setting, consider a collapse+evaporation history on a slab that includes horizon formation. The relevant claim is not that upstairs information is destroyed, but that the 4D shadow map discards degrees of freedom that become nonadmissible (or noncoherent) once the system crosses a horizon barrier.

<div class="definition">

**Definition 13** (Horizon barrier (shadow-level identification)). A horizon barrier is an admissibility barrier $`\mathcal B_{\mathrm{hor}}\subset\mathcal X`$ such that crossing it corresponds, in the shadow $`\mathcal Y`$, to formation of a trapped region and subsequent evaporation in which interior degrees of freedom no longer remain in the admissible coherent sector as seen by external observables.

</div>

<div class="proposition">

**Proposition 14** (Information loss as projected noninvertibility). *Under the horizon barrier identification, the nonexistence of a global 4D recovery map for the pre-collapse state from late-time Hawking radiation is an instance of Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a>.*

</div>

## Mapping to Page curve and islands

The island formula program restores an effective Page curve by modifying how entanglement entropy of radiation is computed, effectively including additional regions (islands) in the entanglement wedge. This can be interpreted as enlarging or re-encoding the shadow algebra of observables.

<div class="remark">

*Remark 15* (Islands as partial inverse / re-encoding). In the present framework, islands correspond to regime-dependent partial right-inverses on a *restricted* algebra or coarse-grained sector of $`\mathcal Y`$, not a global right-inverse of $`T_t`$ on all of $`\mathcal Y`$. That is, islands can restore invertibility for selected observables within a universality regime, while Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a> forbids global invertibility once barrier-crossing fiber identifications occur.

</div>

<div class="remark">

*Remark 16* (Mainstream patches predicted by the bridge). Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a> predicts that any attempt to restore full 4D unitarity/invertibility must either:

1.  enlarge the observable algebra/state space (nonlocal encoding), or

2.  introduce explicit final-state projections, or

3.  rely on regime-dependent effective inversions (islands) that cannot be global.

This aligns structurally with the emergence of islands/replica-wormhole methods and with final-state projection proposals.

</div>

# Confrontation with the Page Curve and Island Formula

In this section we confront the present framework directly with the modern “island” resolution of the black hole information problem. Our goal is not to re-derive the island formula or replica trick, but to clarify—at the level of operator structure and invertibility—what such constructions can and cannot accomplish in light of Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a>.

## What the island formula actually restores

The island formula modifies the computation of von Neumann entropy for radiation subsystems by enlarging the region whose entanglement wedge is included in the entropy calculation. Schematically, one replaces
``` math
S(\rho_{\mathrm{rad}}) \;\longrightarrow\;
\min_{\mathcal I}
\left\{
\frac{\mathrm{Area}(\partial \mathcal I)}{4G_N}
+
S_{\mathrm{bulk}}(\rho_{\mathrm{rad}\cup \mathcal I})
\right\}.
```

Operationally, this corresponds to enlarging the effective algebra of observables used to compute entropy, so that certain interior degrees of freedom are treated as if they were encoded in the radiation sector.

From the perspective of the present framework, this amounts to the following:

- The observable shadow space $`\mathcal Y`$ is *effectively enlarged or re-encoded* for a restricted class of observables (those entering the entropy functional).

- The projection $`P:\mathcal X\to\mathcal Y`$ is *not inverted globally*, but is partially inverted or redefined on a chosen subalgebra.

Thus the island prescription restores *effective invertibility* for specific coarse-grained diagnostics (entanglement entropy), but does not provide a global right-inverse for the shadow evolution map $`T_t=P\circ\Phi_t`$.

## Islands as partial inverses on restricted algebras

Let $`\mathcal A(\mathcal Y)`$ denote the full algebra of 4D observables, and let $`\mathcal A_{\mathrm{island}}\subset \mathcal A(\mathcal Y)`$ denote the restricted subalgebra for which the island prescription applies.

In the present language, the island construction defines a map
``` math
S_t^{(\mathcal A_{\mathrm{island}})} :
\mathcal A_{\mathrm{island}} \;\to\; \mathcal X
```
such that
``` math
T_t \circ S_t^{(\mathcal A_{\mathrm{island}})}
=
\mathrm{Id}
\quad \text{on } \mathcal A_{\mathrm{island}}.
```

Crucially, no such map exists on the full algebra $`\mathcal A(\mathcal Y)`$ once barrier-crossing noninjectivity has occurred.

<div class="remark">

*Remark 17*. This distinction is often blurred in informal discussions of “information recovery.” Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a> forbids a global inverse on $`\mathcal Y`$, but does not forbid partial inverses on restricted algebras or coarse-grained observables.

</div>

## Why islands do not restore global unitarity

Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a> implies that once the shadow map $`T_t`$ identifies distinct upstairs configurations across an admissibility barrier, no measurable global right-inverse can exist.

Island constructions evade this only by:

1.  restricting attention to specific observables (entropy functionals), and

2.  allowing state-dependent or regime-dependent re-encodings of degrees of freedom.

Neither step restores global invertibility of the shadow dynamics. Instead, islands implement a *contextual partial reconstruction*—exactly analogous, in structure, to context-dependent recovery of pre-measurement information in quantum measurement theory.

## Predictions of the MTT shadow-bridge

The present framework makes sharp structural predictions that go beyond the island literature:

1.  **No protocol can reconstruct full pre-collapse data.** Any procedure claiming full information recovery must either enlarge the observable algebra beyond $`\mathcal Y`$ or introduce nonlocal degrees of freedom not present in the original shadow theory.

2.  **Page-curve unitarity is effective, not fundamental.** The recovery of a Page curve reflects a reorganization of basin measures and partial re-encodings, not restoration of global invertibility.

3.  **Breakdown occurs at admissibility barriers, not entropy thresholds.** The fundamental transition is controlled by gap closure / loss of projector regularity, not by the entanglement entropy reaching a maximum.

These predictions distinguish the MTT shadow-bridge from interpretations that treat the island formula as evidence for exact 4D unitarity.

## Relation to final-state projection and nonlocal encodings

Other proposed resolutions—final-state projection at the singularity, ER=EPR-style nonlocal encoding, or state-dependent interior operators—can be classified in the same way. Each introduces, implicitly or explicitly, a modification of the observable map $`P`$ or an enlargement of $`\mathcal Y`$ that allows partial inversion on selected sectors.

The shadow-bridge framework predicts that all such constructions are *patches* for the same underlying fact: projection across an admissibility barrier is noninvertible, and any restoration of information must therefore be either partial, contextual, or nonlocal.

## Summary

The island formula does not contradict the present framework. Rather, it fits naturally as a regime-dependent partial inversion of the shadow map on restricted observables. What it cannot do—by Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a>—is restore global invertibility of the 4D shadow dynamics once admissibility-barrier crossing has occurred.

In this sense, black hole information loss and quantum measurement collapse share not only a common origin, but also a common pattern of attempted resolution: effective recovery on restricted algebras, without global reconstruction.

# Born Weights and Hawking Weights from a Single Basin-Measure Functional

We now show that the probability weights appearing in quantum measurement (Born rule) and the thermal weights appearing in Hawking radiation arise from the same mathematical object in the MTT framework: a basin-measure functional on the full configuration space, evaluated across different admissibility barriers.

## Basin measures in the full configuration space

Let $`(\mathcal X,\mu)`$ be the MTT configuration space equipped with its natural invariant measure $`\mu`$ (Liouville-type, or stationary measure induced by the deterministic flow $`\Phi_t`$). Let $`\mathcal B\subset\mathcal X`$ be an admissibility barrier, and suppose that crossing $`\mathcal B`$ induces a decomposition of the admissible set into disjoint basins
``` math
\mathcal A \;\longrightarrow\; \bigsqcup_{i\in I} \mathcal A_i,
```
where each $`\mathcal A_i`$ flows under $`\Phi_t`$ to a distinct coherent attractor or sector.

<div class="definition">

**Definition 18** (Basin-measure functional). Define the basin-measure functional
``` math
W_i := \frac{\mu(\mathcal A_i)}{\sum_{j\in I} \mu(\mathcal A_j)}.
```

</div>

By construction, $`\{W_i\}`$ defines a probability distribution over admissible outcomes after barrier crossing.

## Measurement barrier and Born weights

In the measurement setting, the admissibility barrier $`\mathcal B_{\mathrm{meas}}`$ corresponds to a change of context or coupling to an apparatus, producing a set of outcome basins $`\{\mathcal A_i\}`$ associated with stable pointer states.

<div class="proposition">

**Proposition 19** (Born weights as basin measures (structural identification)). *Under the measurement admissibility barrier $`\mathcal B_{\mathrm{meas}}`$, the Born weights $`p_i = \|\Pi_i \psi\|^2`$ coincide with the basin-measure functional $`W_i`$ induced by $`\mu`$, up to normalization. This identification relies on the existence and invariance of the upstairs measure $`\mu`$ and on the correspondence between $`\mu`$ and squared amplitudes established in earlier MTT $`\to`$ QM derivations; it is not re-derived here.*

</div>

<div class="remark">

*Remark 20*. This identification does not require postulating the Born rule. It follows from the invariance of $`\mu`$ under $`\Phi_t`$ and the fact that projection-induced basin capture is the only source of stochasticity in the shadow dynamics.

</div>

## Horizon barrier and Hawking weights

In the black hole setting, the admissibility barrier $`\mathcal B_{\mathrm{hor}}`$ corresponds to horizon formation and evaporation, which renders interior degrees of freedom nonadmissible in the coherent shadow. The admissible exterior sector decomposes into basins labeled by asymptotic radiation modes.

<div class="proposition">

**Proposition 21** (Hawking weights as basin measures under semiclassical identification). *Under the horizon admissibility barrier $`\mathcal B_{\mathrm{hor}}`$, the thermal Hawking weights
``` math
p_\omega \propto e^{-\beta \omega}
```
arise as the basin-measure functional $`W_\omega`$ induced by $`\mu`$, evaluated on radiation basins labeled by asymptotic frequency $`\omega`$. Here $`\beta`$ is identified with the inverse Hawking temperature in the standard semiclassical regime; no derivation of $`\beta`$ or of horizon microphysics is attempted in this work.*

</div>

<div class="remark">

*Remark 22*. The appearance of a thermal spectrum reflects the fact that the invariant measure $`\mu`$, when restricted to the exterior-admissible basins, is weighted by the same exponential action factors that control stability and admissibility in the coherent sector.

</div>

## Unified theorem

We can now state the unifying result.

<div id="thm:born-hawking" class="theorem">

**Theorem 23** (Unifying structural principle). *Let $`\mathcal B`$ be an admissibility barrier in an MTT system, inducing basin decomposition $`\{\mathcal A_i\}`$ of the admissible set. Then the probability weights observed in the 4D shadow dynamics after crossing $`\mathcal B`$ are given universally by the basin-measure functional $`W_i`$.*

*In particular:*

1.  *for $`\mathcal B=\mathcal B_{\mathrm{meas}}`$, $`W_i`$ yields Born probabilities;*

2.  *for $`\mathcal B=\mathcal B_{\mathrm{hor}}`$, $`W_i`$ yields Hawking thermal weights.*

</div>

<div class="corollary">

**Corollary 24** (No fundamental distinction between quantum and thermal probabilities). *In the MTT framework, quantum measurement probabilities and black hole thermal radiation probabilities are not fundamentally different objects. Both are shadows of the same upstairs basin-measure functional evaluated across different admissibility barriers.*

</div>

<div class="remark">

*Remark 25* (Why this is not “everything is thermal”). The distinction between “quantum” and “thermal” statistics lies not in the measure functional itself, but in the geometry of the barrier and the labeling of the basins. Measurement barriers produce discrete outcome basins; horizon barriers produce continuum-labeled radiation basins.

</div>

# Quantum Measurement Collapse as Partial Inversion on Restricted Algebras

We now complete the shadow-bridge by showing that quantum measurement collapse is structurally identical to the island construction discussed in the black hole setting. In both cases, apparent information loss is resolved by a partial inversion of the shadow map on a restricted algebra of observables.

## Measurement update as a noninvertible shadow map

Let $`\mathcal A(\mathcal Y)`$ denote the algebra of 4D observables. A measurement context $`C`$ (specified by an instrument or POVM $`\{E_i\}`$) induces a restriction of admissibility and hence a change of the effective observable map $`P`$.

After a measurement, the shadow dynamics is described by
``` math
\rho \;\longrightarrow\; \rho_i
= \frac{\sqrt{E_i}\,\rho\,\sqrt{E_i}}{\Tr(E_i\rho)},
```
which is manifestly noninvertible on $`\mathcal A(\mathcal Y)`$.

## Restricted algebra and partial inverse

Define the post-measurement algebra
``` math
\mathcal A_i := \{ A \in \mathcal A(\mathcal Y) \mid [A,E_i]=0 \},
```
the algebra of observables compatible with outcome $`i`$.

<div class="proposition">

**Proposition 26** (Partial inversion after measurement). *For each outcome $`i`$, there exists a map
``` math
S_i : \mathcal A_i \;\to\; \mathcal X
```
such that
``` math
P \circ \Phi_t \circ S_i = \mathrm{Id}
\quad \text{on } \mathcal A_i.
```
No such map exists on the full algebra $`\mathcal A(\mathcal Y)`$.*

</div>

<div class="remark">

*Remark 27*. This is the measurement analogue of the island construction: invertibility is restored only on a restricted algebra selected by the context and outcome.

</div>

## Collapse vs. Everett vs. islands

From this perspective:

- “Collapse” is the statement that the shadow map is noninvertible on the full algebra.

- “Many worlds” corresponds to keeping the full upstairs state in $`\mathcal X`$ and refusing to project.

- “Decoherence” corresponds to suppressing off-diagonal sectors without selecting a basin.

- “POVM update” is a partial inversion on $`\mathcal A_i`$, analogous to an island.

## Unified picture

<div id="thm:measurement-island" class="theorem">

**Theorem 28** (Measurement–island equivalence). *Quantum measurement collapse and black hole island constructions are instances of the same structural mechanism: partial inversion of a noninvertible shadow map on a restricted observable algebra, following admissibility-barrier crossing.*

</div>

<div class="remark">

*Remark 29*. The difference between measurement and black holes lies in the physical realization of the barrier and in the algebra selected for partial inversion, not in the underlying mechanism.

</div>

# Direct Comparison with Everettian Interpretations

Everettian (“many-worlds”) interpretations propose that the appearance of collapse is an illusion arising from unitary evolution and branching of the universal wavefunction, with no fundamental projection or loss of information. In this section we confront that claim directly within the shadow-bridge framework. This distinction should be understood as a theory-choice criterion about what counts as an autonomous effective description of 4D physics, not as an empirical refutation of Everettian interpretations.

## The Everettian move

The Everettian position may be summarized as follows:

1.  The fundamental state (wavefunction) evolves unitarily at all times.

2.  Measurement corresponds to entanglement and branching, not projection.

3.  Apparent collapse reflects an observer’s restriction to a branch, not a physical process.

From the present perspective, this corresponds to *refusing to apply the projection* $`P=I\circ\Pi`$ and insisting that the physically relevant description remains the upstairs state in $`\mathcal X`$ (or its Hilbert-space analogue) at all times.

## What Everett must deny

Theorem <a href="#thm:barrier-noninvertibility" data-reference-type="ref" data-reference="thm:barrier-noninvertibility">8</a> isolates the precise point of disagreement. The Everettian position requires that:

- the full upstairs state remains physically meaningful at the 4D level, and

- no admissibility barrier produces noninvertibility of the observable map.

In other words, Everett denies that $`P`$ is a physically enforced map, treating it instead as an optional epistemic restriction.

## Structural consequences of refusing projection

If one refuses the projection $`P`$ as physically operative, two consequences follow:

1.  The effective 4D theory is no longer complete: observers must be described as parts of the upstairs configuration space $`\mathcal X`$, with no autonomous 4D description.

2.  All apparent irreversibility (collapse, thermalization, horizon loss) must be reconstructed from branch-relative bookkeeping rather than from dynamical selection.

This position is internally consistent, but it abandons the goal of deriving a closed, autonomous 4D effective theory.

## Everett and black holes

The same structural choice appears in the black hole context. An Everettian stance would treat the full interior–exterior entangled state as physically real and deny any loss of information, regardless of the inability of 4D observers to reconstruct it.

In the shadow-bridge framework, this corresponds to refusing the projection across the horizon barrier and insisting that interior degrees of freedom remain part of the physical state, even when they are nonadmissible in the coherent sector.

## Why Everett reintroduces shadows implicitly

In practice, Everettian treatments inevitably reintroduce shadow-like structures:

- Branch weights obey the Born rule.

- Observers experience definite outcomes.

- Decoherence defines effective pointer sectors.

These are precisely the signatures of basin selection and partial inversion on restricted algebras described earlier. From the shadow-bridge perspective, Everett retains the upstairs state but relies on emergent shadow structure to recover phenomenology.

<div class="remark">

*Remark 30* (Everett as a refusal, not a refutation). The present framework does not refute Everettian interpretations. Rather, it clarifies their commitment: Everett denies that projection-induced noninvertibility is physically operative. In exchange, it gives up a closed 4D effective description and must treat all observed definiteness as branch-relative.

</div>

## Shadow-bridge position

The shadow-bridge framework makes the opposite choice:

- The upstairs evolution is deterministic and invertible.

- The projection $`P`$ is physically enforced by admissibility and stability.

- Noninvertibility of the 4D shadow is real and generative, not illusory.

From this standpoint, collapse and black hole information loss are not interpretational artifacts but structural features of effective physics under projection.

<div id="thm:everett-shadow" class="theorem">

**Theorem 31** (Everett–shadow dichotomy). *Everettian interpretations and the shadow-bridge framework are distinguished by a single structural choice: whether the projection $`P`$ is treated as physically operative. If $`P`$ is operative, barrier-crossing noninvertibility is unavoidable and collapse/information loss are real in the 4D shadow. If $`P`$ is refused, 4D physics is not closed and must be understood as branch-relative.*

</div>

<div class="remark">

*Remark 32*. This dichotomy is not empirical at the level of the upstairs theory, but it is decisive at the level of what counts as an autonomous effective description of 4D physics.

</div>

# Outlook

This paper isolates the common mathematical core of two crises: black hole information loss and quantum measurement collapse. The next step is to instantiate the barrier structure in concrete MTT models: identify the spectral-gap/contractivity conditions corresponding to measurement context changes and to horizon formation, and compute the induced shadow entropy diagnostics in each case. A direct comparison with Page-curve/island formula computations would then locate precisely which observables admit partial inversion and where the coherent regime must fail.

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
