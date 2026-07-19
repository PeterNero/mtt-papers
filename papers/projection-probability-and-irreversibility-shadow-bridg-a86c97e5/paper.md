---
abstract: |
  We develop a unified framework within Modal Triplet Theory (MTT) connecting three apparently independent problems in 4D physics: quantum measurement collapse, black hole information loss, and the origin of probability in cosmology. In MTT, effective 4D physics arises as a shadow of deterministic dynamics on a higher configuration space under a noninvertible coherent projection. We introduce admissibility barriers—loci where the projection fails to be stably invertible due to gap closure, projector discontinuity, or basin rearrangement—and prove a general noninvertibility theorem: whenever trajectories cross such a barrier, the induced 4D shadow dynamics admits no global reconstruction map, despite invertibility of the upstairs evolution.

  We show that (i) quantum measurement collapse and (ii) black hole information loss are two instantiations of this same projection-induced noninvertibility, differing only in the physical realization of the barrier. We further show that Born probabilities, Hawking thermal weights, and cosmological initial-condition measures arise from a single basin-measure functional evaluated across different admissibility barriers, within the coherent universality class. Inflationary attractors and decoherence-based branching are identified as partial shadows that detect basin structure but cannot fix probability weights without access to the upstairs invariant measure.

  Finally, we incorporate results on computational irreducibility: there exist admissibility barriers for which basin membership is algorithmically undecidable, ruling out any uniform decoding protocol that would restore full information after barrier crossing. The framework clarifies the status of island constructions, POVM updates, and Everettian interpretations as partial inversions or refusals of projection rather than restorations of global 4D invertibility.
author:
- Peter Nero
current_version: v2
date: January, 2026
generated_from_main_tex_sha256: dccc393aba624bb65e240318ad4258bd98fe71e72e8f37faa7dbfa0ec11b6efc
paper_id: projection-probability-and-irreversibility-shadow-bridg-a86c97e5
release_state: zenodo_released
released_version: v1.0
title: |
  Projection, Probability, and Irreversibility:  
  Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.18262041
zenodo_record_id: 18262041
zenodo_url: "https://zenodo.org/records/18262041"
---

# Scope, Motivation, and Claim Discipline

This paper bridges three long-standing problems traditionally treated separately:

1.  **Quantum measurement collapse**: why deterministic unitary evolution yields definite outcomes with probabilistic weights.

2.  **Black hole information loss**: why semiclassical evaporation appears to map pure states to mixed thermal exterior states.

3.  **Cosmic initial conditions**: why the universe begins in a highly special state and why any probability measure on cosmic histories exists.

The central claim is structural: these are shadows of deterministic upstairs dynamics under a noninvertible projection across admissibility barriers.

## Claim discipline

We separate three layers:

1.  **Mathematical spine (proved):** deterministic invertible evolution $`\Phi_t`$ on a configuration space $`\mathcal X`$, a measurable shadow map $`P`$, and the consequence that barrier-crossing noninjectivity implies the shadow evolution admits no measurable right-inverse.

2.  **Structural identifications:** measurement, horizons, and early cosmology correspond to distinct physical realizations of admissibility barriers.

3.  **Phenomenological alignment:** mainstream “patches” (decoherence, POVMs, islands, inflationary measures) align with partial inversions/re-encodings on restricted algebras or partial basin detection.

We do not re-derive the Born rule or Hawking spectrum from microphysics here; we show they are instances of a common basin-measure mechanism, under stated identifications and within the coherent universality regime.

<div class="remark">

*Remark 1* (Unitarity vs invertibility). “Unitarity” in this paper means invertibility of the upstairs evolution. The central statement is that invertibility does not descend through noninvertible projection; the 4D shadow can be noninvertible even when the full theory is invertible.

</div>

# Upstairs Dynamics, Projection, and Admissibility Barriers

## Configuration space and invertible evolution

Let $`(\mathcal X,\mathcal B)`$ be a standard Borel space representing the full MTT configuration space on a bounded-geometry slab. Let
``` math
\Phi_t:\mathcal X\to\mathcal X
```
be a deterministic, invertible, measurable flow, with measurable inverse $`\Phi_{-t}`$.

## Coherent projector and observable map

Let $`\Pi:\mathcal X\to\mathcal X_{\mathrm{coh}}`$ be the coherent projector selecting dynamically stable configurations (spectral gap $`\lambda_*>0`$, FCC margins positive in the admissible regime). Let $`I:\mathcal X_{\mathrm{coh}}\to\mathcal Y`$ be the observable pushforward to an effective 4D state space $`\mathcal Y`$ (e.g. a Hilbert-state or algebraic state). Define
``` math
P := I\circ \Pi:\mathcal X\to\mathcal Y.
```

<div class="remark">

*Remark 2* (Boundary conditions). If the effective 4D description is realized on a slab/domain with boundary, we assume standard well-posed elliptic/hyperbolic boundary conditions are chosen so that the coherent projection and flow are defined and the slab-local analysis applies. This does not affect the measure-theoretic arguments below.

</div>

## Admissibility

We assume there exists an admissible subset $`\mathcal A\subset \mathcal X`$ where coherent evolution is well-controlled (bounded geometry, gap persists, projector regular, stability margins positive).

<div id="def:barrier" class="definition">

**Definition 3** (Admissibility barrier). A measurable set $`\mathcal B\subset\mathcal X`$ is an admissibility barrier if:

1.  $`\mathcal X\setminus\mathcal B = \mathcal U_+\sqcup \mathcal U_-`$ with $`\mathcal U_\pm`$ measurable and nonempty;

2.  $`\Pi`$ (or the admissibility constraints defining $`\mathcal U_\pm`$) is regular on each $`\mathcal U_\pm`$, but there is no globally measurable right-inverse for $`\Pi`$ across $`\mathcal U_+\cup\mathcal U_-`$;

3.  there exists $`y\in\mathcal Y`$ such that $`P^{-1}(y)`$ intersects both $`\mathcal U_+`$ and $`\mathcal U_-`$.

</div>

<div id="lem:barrier-operational" class="lemma">

**Lemma 4** (Operational sufficient conditions for an admissibility barrier). *Let $`P:\mathcal X\to\mathcal Y`$ be measurable and let $`\mathcal X\setminus\mathcal B=\mathcal U_+\sqcup\mathcal U_-`$ with $`\mathcal U_\pm`$ measurable and nonempty. If there exist $`x_+\in\mathcal U_+`$ and $`x_-\in\mathcal U_-`$, $`x_+\neq x_-`$, with
``` math
P(x_+)=P(x_-),
```
then Definition <a href="#def:barrier" data-reference-type="ref" data-reference="def:barrier">3</a>(B3) holds (fiber overlap). If additionally there is no globally measurable right-inverse for $`\Pi`$ across $`\mathcal U_+\cup\mathcal U_-`$, then $`\mathcal B`$ is an admissibility barrier and Theorem <a href="#thm:barrier" data-reference-type="ref" data-reference="thm:barrier">9</a> applies (for times $`t`$ for which $`\Phi_t(\mathcal U_\pm)`$ have positive measure).*

</div>

<div class="remark">

*Remark 5* (Physical sufficient conditions). Measurement: context change produces two distinct upstairs configurations with the same coarse pointer record under $`P`$, landing in different admissible regions. Black holes: distinct interior/exterior microstates project to the same exterior coarse algebra/state. Cosmology: distinct early-time admissible histories project to the same late-time coarse observables.

</div>

# Barrier Crossing Implies Shadow Noninvertibility

<div class="definition">

**Definition 6** (Shadow evolution map). Define the shadow map at time $`t`$ by
``` math
T_t := P\circ \Phi_t:\mathcal X\to\mathcal Y.
```

</div>

<div class="definition">

**Definition 7** (Right-invertibility (reconstruction)). We say $`T_t`$ admits a measurable right-inverse if there exists a measurable map $`S_t:\mathcal Y\to\mathcal X`$ such that
``` math
T_t\circ S_t=\mathrm{Id}_{\mathcal Y}.
```

</div>

<div class="remark">

*Remark 8* (Why right inverse?). A right inverse formalizes reconstruction: given a shadow state $`y\in\mathcal Y`$, $`S_t(y)`$ would produce an upstairs configuration whose shadow is $`y`$. A left inverse would require injectivity of $`T_t`$, which is exactly what fails at barrier crossing.

</div>

<div id="thm:barrier" class="theorem">

**Theorem 9** (Admissibility-barrier noninvertibility). *Assume:*

1.  *$`\Phi_t`$ is invertible and measurable;*

2.  *$`P`$ is measurable;*

3.  *$`\mathcal B`$ is an admissibility barrier with regions $`\mathcal U_\pm`$ as in Definition <a href="#def:barrier" data-reference-type="ref" data-reference="def:barrier">3</a>.*

*Then for any time $`t`$ such that $`\Phi_t(\mathcal U_+)`$ and $`\Phi_t(\mathcal U_-)`$ both have positive measure and Definition <a href="#def:barrier" data-reference-type="ref" data-reference="def:barrier">3</a>(B3) holds for some $`y\in\mathcal Y`$, the map $`T_t`$ admits no measurable right-inverse.*

</div>

<div class="proof">

*Proof.* By Definition <a href="#def:barrier" data-reference-type="ref" data-reference="def:barrier">3</a>(B3) there exist $`x_+\in\mathcal U_+`$ and $`x_-\in\mathcal U_-`$ with $`x_+\neq x_-`$ and $`P(x_+)=P(x_-)=y`$. Since $`\Phi_t`$ is invertible, $`\Phi_t(x_+)\neq\Phi_t(x_-)`$. But
``` math
T_t(x_+) = P(\Phi_t(x_+)),\qquad T_t(x_-) = P(\Phi_t(x_-)).
```
If $`T_t`$ had a measurable right-inverse $`S_t`$, then $`T_t(S_t(y))=y`$ would define a single-valued reconstruction for $`y`$. However, the existence of two distinct preimages across the barrier means no single-valued measurable map can act as a right-inverse on a set of positive measure while satisfying $`T_t\circ S_t=\mathrm{Id}_{\mathcal Y}`$. Therefore no measurable right-inverse exists. ◻

</div>

<div class="corollary">

**Corollary 10** (Upstairs invertibility does not descend). *Even if $`\Phi_t`$ is invertible/unitary upstairs, the induced 4D shadow dynamics $`T_t`$ is not globally reconstructible once barrier-crossing noninjectivity occurs.*

</div>

# Measurement Collapse as Barrier Crossing and Partial Inversion

## Measurement contexts and basin structure

A measurement context $`C`$ (instrument/POVM specification) restricts admissibility to a subset $`\mathcal A_C\subset\mathcal X`$ and induces outcome basins $`\{\mathcal A_i\}`$ corresponding to stable pointer sectors. A measurement interaction corresponds to a context change $`C\to C'`$ that may force trajectories across a measurement barrier $`\mathcal B_{\mathrm{meas}}`$.

<div class="definition">

**Definition 11** (Measurement barrier). $`\mathcal B_{\mathrm{meas}}`$ is an admissibility barrier whose crossing corresponds (in the shadow) to the onset of stable outcome basins for the post-context admissible set.

</div>

<div class="proposition">

**Proposition 12** (Collapse as shadow noninvertibility). *Measurement collapse is an instance of Theorem <a href="#thm:barrier" data-reference-type="ref" data-reference="thm:barrier">9</a>: after crossing $`\mathcal B_{\mathrm{meas}}`$, the shadow map admits no global reconstruction on $`\mathcal Y`$.*

</div>

## POVM update as partial right-inversion on restricted state spaces

Let $`\mathcal A(\mathcal Y)`$ denote the shadow observable algebra, and for outcome $`i`$ define the compatible subalgebra
``` math
\mathcal A_i := \{A\in\mathcal A(\mathcal Y)\mid [A,E_i]=0\},
```
where $`E_i`$ is the POVM element.

<div class="definition">

**Definition 13** (State restriction map). Let $`\mathrm{States}(\mathcal A_i)`$ denote the state space on $`\mathcal A_i`$. Define the restriction/evaluation map
``` math
F_{\mathcal A_i}:\mathcal X\to \mathrm{States}(\mathcal A_i),\qquad
F_{\mathcal A_i}(x) := \omega_{P(\Phi_t(x))}\big|_{\mathcal A_i},
```
where $`\omega_{P(\Phi_t(x))}`$ denotes the induced shadow state.

</div>

<div id="prop:povm-partial-inverse" class="proposition">

**Proposition 14** (POVM update as partial right-inversion on restricted algebras). *For each outcome $`i`$, there exists a map
``` math
S_i:\mathrm{States}(\mathcal A_i)\to\mathcal X
```
such that
``` math
F_{\mathcal A_i}\circ S_i = \mathrm{Id}_{\mathrm{States}(\mathcal A_i)}.
```
In general, no such right inverse exists for the full state map into $`\mathrm{States}(\mathcal A(\mathcal Y))`$ once barrier-crossing noninjectivity occurs.*

</div>

<div class="remark">

*Remark 15*. This is the measurement analogue of islands: reconstruction is possible only on a restricted state-space of observables, not pointwise on the full shadow description.

</div>

# Black Hole Horizons as Admissibility Barriers

We now apply the admissibility-barrier framework to gravitational collapse and black hole evaporation. The goal is not to model horizon microphysics, but to identify the structural mechanism by which information loss arises in the 4D shadow.

## Horizon-induced loss of admissibility

Consider a collapse–evaporation history on a bounded-geometry slab. In the MTT framework, degrees of freedom that become confined to the black hole interior are no longer admissible for the coherent 4D shadow once the horizon forms and persists through evaporation.

<div class="definition">

**Definition 16** (Horizon barrier). The horizon barrier $`\mathcal B_{\mathrm{hor}}`$ is an admissibility barrier separating configurations whose coherent projection yields only exterior-accessible degrees of freedom from configurations requiring interior (noncoherent) modes for reconstruction.

</div>

<div class="remark">

*Remark 17*. This definition abstracts from the details of quantum gravity. It encodes only the fact that interior degrees of freedom are not part of the admissible coherent sector available to exterior observers.

</div>

## Information loss as shadow noninvertibility

<div class="proposition">

**Proposition 18** (Black hole information loss). *Once trajectories cross $`\mathcal B_{\mathrm{hor}}`$, the shadow evolution map $`T_t`$ admits no global measurable right inverse. The apparent mapping of pure initial states to mixed exterior radiation states is therefore an instance of Theorem <a href="#thm:barrier" data-reference-type="ref" data-reference="thm:barrier">9</a>.*

</div>

<div class="remark">

*Remark 19*. This result does not deny invertibility of the upstairs evolution. It asserts that the coherent projection discards interior information in a way that forbids global reconstruction at the 4D level.

</div>

# Page Curve, Islands, and Partial Reconstruction

We now confront the modern Page-curve and island-program directly.

## What the island formula accomplishes

Island constructions modify the entropy computation for radiation by enlarging the region whose entanglement wedge is included. Operationally, this corresponds to redefining the observable algebra used to compute entropy.

Let $`\mathcal A(\mathcal Y)`$ denote the full shadow observable algebra, and let $`\mathcal A_{\mathrm{island}}\subset\mathcal A(\mathcal Y)`$ denote the restricted algebra selected by the island prescription.

## Islands as partial right inverses

<div class="proposition">

**Proposition 20** (Islands as partial inversion). *There exists a map
``` math
S_t^{(\mathrm{island})}:\mathrm{States}(\mathcal A_{\mathrm{island}})\to\mathcal X
```
such that
``` math
F_{\mathcal A_{\mathrm{island}}}\circ S_t^{(\mathrm{island})}
= \mathrm{Id}_{\mathrm{States}(\mathcal A_{\mathrm{island}})},
```
where $`F_{\mathcal A_{\mathrm{island}}}`$ is the restriction map defined analogously to $`F_{\mathcal A_i}`$ in Proposition <a href="#prop:povm-partial-inverse" data-reference-type="ref" data-reference="prop:povm-partial-inverse">14</a>.*

</div>

<div class="remark">

*Remark 21*. Islands restore effective reconstructability only on a restricted algebra. By Theorem <a href="#thm:barrier" data-reference-type="ref" data-reference="thm:barrier">9</a>, no global reconstruction map on $`\mathcal A(\mathcal Y)`$ can exist once horizon-induced fiber overlap occurs.

</div>

## Interpretation

Island constructions do not refute information loss in the shadow sense. They demonstrate that certain coarse-grained observables admit partial reconstruction. This is structurally identical to POVM updates in measurement theory.

# Basin Measures and Probability in the Coherent Universality Class

We now turn to probability.

## Invariant measure assumption

<div id="def:mu-coh" class="definition">

**Definition 22** (Coherent universality class invariant measure). We assume the existence of a $`\Phi_t`$-invariant probability measure $`\mu`$ on the admissible coherent sector $`\mathcal A`$, fixed either by uniqueness within the coherent universality class or by prior MTT $`\to`$ QM derivations identifying $`\mu`$ with squared-amplitude weights. The existence and uniqueness of $`\mu`$ are not re-derived here.

</div>

## Basin-measure functional

Let $`\mathcal B`$ be an admissibility barrier inducing a basin decomposition
``` math
\mathcal A = \bigsqcup_{i\in I}\mathcal A_i.
```

<div class="definition">

**Definition 23** (Basin-measure functional). Define
``` math
W_i := \frac{\mu(\mathcal A_i)}{\sum_{j\in I}\mu(\mathcal A_j)}.
```

</div>

## Born weights (structural identification)

<div class="proposition">

**Proposition 24** (Born weights as basin measures (structural identification)). *Under the measurement barrier $`\mathcal B_{\mathrm{meas}}`$, the observed Born weights $`p_i=\|\Pi_i\psi\|^2`$ coincide with the basin-measure functional $`W_i`$ when $`\mu`$ is identified with the squared-amplitude measure established in prior MTT$`\to`$QM results.*

</div>

<div class="remark">

*Remark 25*. This is a structural identification. No independent derivation of the Born rule is claimed here.

</div>

## Hawking weights (semiclassical identification)

<div class="proposition">

**Proposition 26** (Hawking weights as basin measures (semiclassical identification)). *Under the horizon barrier $`\mathcal B_{\mathrm{hor}}`$, the thermal weights $`p_\omega\propto e^{-\beta\omega}`$ observed in Hawking radiation coincide with the basin-measure functional $`W_\omega`$ when $`\mu`$ is identified with the invariant measure on exterior-admissible configurations in the standard semiclassical regime.*

</div>

<div class="remark">

*Remark 27*. No derivation of $`\beta`$ or of horizon microphysics is attempted here. The identification is made under the usual semiclassical correspondence.

</div>

## Basin-measure principle

<div id="thm:basin-measure" class="theorem">

**Theorem 28** (Basin-measure theorem in the coherent universality class). *Let $`(\mathcal X,\Phi_t)`$ be an MTT system with admissible coherent sector $`\mathcal A`$. Assume there exists a unique (up to equivalence) $`\Phi_t`$-invariant probability measure $`\mu`$ on $`\mathcal A`$ associated with the coherent universality class.*

*Let $`\mathcal B\subset\mathcal X`$ be an admissibility barrier satisfying hypotheses (H1)–(H3) of Definition <a href="#def:barrier" data-reference-type="ref" data-reference="def:barrier">3</a>, and suppose that:*

1.  *$`\mathcal B`$ induces a measurable basin decomposition
    ``` math
    \mathcal A = \bigsqcup_{i\in I} \mathcal A_i
    ```
    with $`\mu(\mathcal A_i)>0`$ for at least one $`i`$;*

2.  *the restriction of $`\mu`$ to $`\mathcal A\setminus\mathcal B`$ is invariant under $`\Phi_t`$ up to sets of measure zero;*

3.  *the shadow observables under consideration depend only on basin membership (i.e. are $`\mu`$-almost everywhere constant on each $`\mathcal A_i`$).*

**Then*, conditional on these assumptions, the probability weights observed in the 4D shadow dynamics after crossing $`\mathcal B`$ coincide with the basin-measure functional
``` math
W_i := \frac{\mu(\mathcal A_i)}{\sum_{j\in I}\mu(\mathcal A_j)}.
```*

</div>

<div class="remark">

*Remark 29*. The content of the theorem is an implication under explicit hypotheses, not a claim of universality over all possible measures or barriers.

</div>

<div class="corollary">

**Corollary 30**. *Quantum measurement probabilities and black hole thermal probabilities are shadows of the same upstairs invariant measure evaluated across different admissibility barriers.*

</div>

# Cosmic Initial Conditions and the Born Rule

We now complete the probability side of the shadow-bridge program by unifying quantum measurement probabilities and cosmological initial-condition measures.

## Two probability problems

Quantum theory and cosmology both contain unresolved probability problems:

- In quantum mechanics, probabilities enter via the Born rule, which is usually taken as an axiom or justified via symmetry, Gleason-type theorems, or decision-theoretic arguments.

- In cosmology, probabilities enter via measures on initial conditions or histories, often introduced ad hoc (inflationary measures, anthropic weighting, volume cutoffs).

Despite their different contexts, both problems concern the same question: why deterministic dynamics gives rise to probabilistic outcomes at all.

## Cosmic admissibility barrier

In the MTT framework, the earliest epoch at which a coherent four-dimensional description becomes valid defines a cosmological admissibility barrier $`\mathcal B_{\mathrm{cosmo}}`$. Crossing this barrier partitions the admissible configuration space into basins corresponding to macroscopically distinct cosmological histories.

<div class="proposition">

**Proposition 31** (Cosmic basin decomposition). *Crossing $`\mathcal B_{\mathrm{cosmo}}`$ induces a decomposition
``` math
\mathcal A = \bigsqcup_{i\in I}\mathcal A_i^{\mathrm{cosmo}},
```
where each basin corresponds to a distinct class of coherent cosmological histories.*

</div>

## Born rule as microscopic limit

At microscopic scales, measurement barriers induce analogous basin decompositions. The Born rule arises as the restriction of the same basin-measure functional to microscopic admissibility barriers.

<div id="thm:born-cosmic" class="theorem">

**Theorem 32** (Born–cosmic probability equivalence theorem). *Assume the hypotheses of Theorem <a href="#thm:basin-measure" data-reference-type="ref" data-reference="thm:basin-measure">28</a>. Assume further that:*

1.  *for microscopic admissibility barriers $`\mathcal B_{\mathrm{meas}}`$, the invariant measure $`\mu`$ induces squared-amplitude weights on outcome basins, as established in prior MTT$`\to`$QM results;*

2.  *for macroscopic cosmological admissibility barriers $`\mathcal B_{\mathrm{cosmo}}`$, the same measure $`\mu`$ restricts to a well-defined measure on coherent cosmic-history basins.*

*Then the Born rule probabilities in quantum measurement and the probability measures on cosmic initial conditions are restrictions of the same basin-measure functional $`W_i`$ associated with $`\mu`$, evaluated across $`\mathcal B_{\mathrm{meas}}`$ and $`\mathcal B_{\mathrm{cosmo}}`$ respectively.*

</div>

<div class="remark">

*Remark 33*. This theorem asserts a structural unification, not a new derivation of either probability rule. Any consistent modification of one must entail a modification of the other.

</div>

# Inflationary Attractors as Partial Basin Shadows

We now confront standard inflationary approaches to the cosmological measure problem.

## What inflation gets right

Inflationary dynamics correctly identifies:

1.  strong contraction of large regions of phase space;

2.  dominance of a subset of trajectories at late times;

3.  effective basin structure in reduced cosmological variables.

These features correspond to basin dominance in the shadow dynamics.

## What inflation cannot fix

However, inflationary dynamics alone cannot define a unique probability measure:

1.  no distinguished invariant measure is provided;

2.  regulator dependence persists (youngness paradox, Boltzmann brains);

3.  no admissibility barrier separating allowed from disallowed histories is identified.

## Shadow-bridge diagnosis

In MTT terms, inflationary attractors are partial shadows of the basin structure but lack access to the upstairs invariant measure $`\mu`$ and admissibility barrier $`\mathcal B_{\mathrm{cosmo}}`$.

<div class="theorem">

**Theorem 34** (Attractor–Born parallel). *Inflationary attractors and decoherence-based branching are structurally identical approximations: both detect basin dominance but cannot determine probability weights without reference to the upstairs invariant measure.*

</div>

<div class="remark">

*Remark 35*. This explains why inflationary measure problems persist despite attractor dynamics.

</div>

# Everettian Interpretations and the Shadow-Bridge

Everettian (many-worlds) interpretations maintain that the universal wavefunction evolves unitarily and that collapse is illusory.

## The Everettian refusal

From the shadow-bridge perspective, Everettian interpretations correspond to refusing the projection $`P`$ as physically operative, treating the upstairs state as the sole physical object.

## Consequences of refusing projection

This choice implies:

1.  no closed autonomous 4D effective theory exists;

2.  irreversibility and probabilities must be reconstructed branch-relatively;

3.  admissibility barriers are treated as epistemic rather than physical.

## Structural comparison

<div class="theorem">

**Theorem 36** (Everett–shadow dichotomy). *Everettian interpretations and the shadow-bridge framework differ by whether the projection $`P`$ is treated as physically operative. If $`P`$ is operative, barrier-crossing noninvertibility is unavoidable; if it is refused, 4D physics is not closed and remains branch-relative.*

</div>

<div class="remark">

*Remark 37*. This is a structural theory-choice criterion, not an empirical refutation of Everettian interpretations. This theorem characterizes a structural distinction between classes of effective descriptions; it does not constitute an empirical refutation of Everettian interpretations.

</div>

# Computational Irreducibility and Undecidability

The shadow-bridge framework is strengthened by results on computational irreducibility.

## Undecidability of basin membership

As shown in , there exist admissibility barriers for which basin membership of pre-barrier configurations is algorithmically undecidable.

<div class="proposition">

**Proposition 38** (Undecidability of reconstruction (existential)). *There exist admissibility barriers for which no uniform algorithm decides, in finite time, which basin a given pre-barrier configuration belongs to.*

</div>

<div class="remark">

*Remark 39* (Scope of undecidability). Undecidability here is existential: particular instances may be decidable, but no general decoding protocol can succeed uniformly across all admissibility-barrier crossings.

</div>

## Implications

This implies:

1.  information loss is principled, not merely practical;

2.  no general decoding protocol can restore full information after barrier crossing;

3.  partial inversions (POVM updates, islands) cannot be promoted to global reconstruction.

# Conclusion

We have shown that quantum measurement collapse, black hole information loss, and the origin of probability in cosmology are shadows of a single mechanism in Modal Triplet Theory: projection-induced noninvertibility across admissibility barriers.

Deterministic upstairs dynamics remains invertible, but the 4D shadow loses invertibility whenever basin structure rearranges. Measurement collapse, horizon formation, and cosmic initial-condition selection are distinct physical realizations of this same transition.

Born probabilities, Hawking thermal weights, and cosmological measures arise from a single basin-measure functional within the coherent universality class. Inflationary attractors and decoherence detect basin structure but cannot fix probability weights without access to the upstairs invariant measure. Everettian interpretations avoid collapse by refusing projection, at the cost of abandoning a closed 4D effective theory.

Finally, computational irreducibility establishes that information loss is not merely a practical limitation but a principled consequence of projection.

Together, these results position the shadow-bridge framework as a unifying explanation of probability and irreversibility across quantum mechanics, gravity, and cosmology.

<div class="thebibliography">

99

J. Barnett and L. Smolin, *Fermion doubling in loop quantum gravity*, Phys. Rev. D **92**, 064022 (2015).

R. Gambini and J. Pullin, *No fermion doubling in quantum geometry*, Int. J. Mod. Phys. D **24**, 1542001 (2015).

J. Zhang, Y. Liu, and M. Han, *Fermion doubling and its suppression in loop quantum gravity*, arXiv:2205.12208.

J. Lewandowski and C. Zhang, *Dirac field on loop quantum gravity*, Phys. Rev. D **105**, 124025 (2022).

H. B. Nielsen and M. Ninomiya, *No Go Theorem for Regularizing Chiral Fermions*, Phys. Lett. B **105**, 219–223 (1981).

P. Nero, *Computational Irreducibility from Projection: Undecidability of Selection Events in Coherent Quantum Dynamics*, arXiv:XXXX.YYYY.

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
