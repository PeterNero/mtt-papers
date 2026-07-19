---
abstract: |
  Feynman diagrams and their associated rules appear across a wide range of physical theories, including relativistic quantum field theory, classical statistical field theory, condensed–matter systems, and effective descriptions of gravity. Their ubiquity is often attributed to the quantization of fields, yet closely related diagrammatic structures arise in contexts with no intrinsic quantum interpretation. This raises a conceptual question: why does the same perturbative grammar recur so universally?

  In this paper we propose and develop an explanatory viewpoint based on Modal Triplet Theory (MTT). Building on recent results that derive algebraic quantum field theory (AQFT) and perturbative amplitudes rigorously from coherent modal geometry, we show that the essential structure underlying Feynman rules already exists at the level of coherent modal fluctuations around stable fixed points. Propagator– and vertex–like objects arise as the inverse of the quadratic form governing coherent fluctuations and as higher variations of the modal action, respectively. Diagrammatic expansions then follow inevitably from Gaussian combinatorics, independently of quantization prescriptions, Hilbert spaces, or path integrals.

  This “modal diagrammatics” perspective does not replace the AQFT or pAQFT constructions, which remain essential for causal locality, renormalization control, and global consistency. Rather, it explains why those rigorous frameworks necessarily reproduce the familiar diagrammatic rules when projected to four–dimensional spacetime. We further show how internal overlap integrals, selection rules, and curvature–gap thresholds emerge naturally as vertex factors and propagator spectra in the projected theory.

  Finally, we discuss broader implications of this viewpoint. It clarifies why classical statistical field theories also admit Feynman diagrams, suggests an interpretation of “quantumness” as a particular coherence regime rather than a fundamental ontology, and offers a coherent way to understand the limited domain of validity of perturbative quantum gravity. The result is a unifying conceptual account of diagrammatics as the universal perturbative language of coherent systems.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: c901d892106dffe861c3e26b5f71e656f39ba709b7272572543adca0911e39ce
paper_id: modal-diagrammatics-the-origin-of-feynman-rules-from-co-79b757d8
release_state: zenodo_released
released_version: v1.0
title: "**Modal Diagrammatics: The Origin of Feynman Rules from Coherent Modal Geometry**"
zenodo_doi: 10.5281/zenodo.18330804
zenodo_record_id: 18330804
zenodo_url: "https://zenodo.org/records/18330804"
---

# Introduction: why Feynman rules are puzzling

Feynman diagrams occupy a central place in modern theoretical physics. They provide a compact and efficient computational language for perturbative quantum field theory and underlie much of contemporary particle phenomenology. Yet closely related diagrammatic structures also appear in contexts that are not intrinsically quantum, including classical statistical field theory, critical phenomena, polymer physics, and condensed matter systems. Even in gravity, perturbative expansions around fixed backgrounds are often organized diagrammatically despite the absence of a fundamental quantum theory of spacetime.

This universality raises a basic conceptual question. If Feynman rules are taken to be a direct consequence of field quantization, why do essentially identical diagrammatic structures arise in theories governed by classical probability measures or thermal ensembles? Conversely, if diagrammatics is merely a calculational artifact, why does it emerge so robustly across such disparate physical domains?

In conventional presentations of quantum field theory, Feynman rules are introduced as primitive prescriptions derived from a path integral or canonical quantization procedure. From this perspective, diagrams appear tied to specifically quantum notions such as operator commutators, Hilbert spaces, and measurement postulates. While algebraic quantum field theory (AQFT) and its perturbative extension (pAQFT) provide a more rigorous and conceptually clean foundation, they still reproduce the same diagrammatic structures when perturbative expansions are performed.

Recent developments in Modal Triplet Theory (MTT) offer an opportunity to revisit this issue from a different angle. In the MTT framework, four–dimensional quantum field theory is not assumed as fundamental but is derived from a higher–dimensional modal geometry via coherent projection. Building on this foundation, it has been shown that algebraic quantum field theory on curved spacetime and perturbative scattering amplitudes can be obtained from first principles, with Feynman rules emerging as a derived consequence of the algebraic construction rather than as axioms.

The present paper asks a complementary and more explanatory question: *why must those derived rules take the particular propagator–and–vertex form familiar from Feynman diagrammatics?* In other words, what structural features of the underlying theory force diagrammatic perturbation theory to appear once a suitable effective description exists?

Our central claim is that diagrammatics is not fundamentally quantum. Rather, it is the universal perturbative grammar of systems that admit a stable background, a dominant quadratic sector, and controlled interactions within a truncated or projected space of degrees of freedom. Whenever these conditions are met, Gaussian fluctuations dominate, Wick’s theorem applies, and perturbative expansions organize themselves into diagrams. The specific physical interpretation—quantum, thermal, or otherwise—enters only through the choice of weight and projection, not through the combinatorial structure itself.

Within Modal Triplet Theory, these conditions are realized in a particularly transparent way. Coherent fixed points define stable backgrounds in modal configuration space, bounded projectors select admissible fluctuation sectors, and gap conditions ensure truncation control. Expanding the modal action around such a fixed point yields a quadratic core and higher–order interaction terms. The inverse of the quadratic form plays the role of a propagator for coherent modal fluctuations, while higher variations define interaction vertices. A diagrammatic expansion then follows inevitably at the modal level, before any projection to four–dimensional spacetime or invocation of quantum field theoretic structures.

This “modal diagrammatics” viewpoint is not intended as an alternative foundation to AQFT or pAQFT. Those frameworks remain essential for ensuring causal locality, renormalization control, and global consistency of the projected theory. Instead, the aim here is explanatory: to show why the rigorous algebraic derivations necessarily reproduce diagrammatic rules, and to demystify the appearance of Feynman diagrams as a consequence of coherence and stability rather than quantization per se.

The implications of this perspective extend beyond perturbative quantum field theory. It offers a natural explanation for the presence of diagrams in classical statistical field theory, suggests that “quantumness” itself may be understood as a particular coherence regime of effective descriptions, and provides a coherent way to think about the limited domain of validity of perturbative quantum gravity. Experimental observations of wave–like behavior in composite systems, such as positronium interference, fit naturally into this picture as manifestations of coherence rather than as evidence of fundamental quantum ontology.

The structure of the paper is as follows. In Section 2 we summarize the relevant results from Modal Triplet Theory and clarify the relationship of the present work to the existing AQFT and pAQFT derivations. Sections 3 through 7 develop the modal diagrammatics framework, identifying the quadratic core, modal propagator, interaction vertices, and diagrammatic expansion. Section 8 explains how familiar four–dimensional Feynman rules emerge upon projection and why overlap integrals appear as coupling constants. Subsequent sections explore connections to classical statistical field theory, implications for quantum gravity, and the interpretation of quantumness as a coherence regime. We conclude with a discussion of scope, limitations, and possible extensions.

# Context and prior results

The purpose of this section is to situate the present work within the broader Modal Triplet Theory (MTT) program and to clarify precisely what has already been established. This paper does not introduce new foundational axioms or replace existing derivations. Instead, it builds on results that have been obtained rigorously elsewhere and asks a distinct explanatory question concerning the origin of diagrammatic perturbation theory.

## Modal Triplet Theory and coherent sectors

Modal Triplet Theory describes physical systems as dynamics on a high–dimensional modal configuration space, equipped with a fixed–point structure and spectral gaps separating coherent sectors from noncoherent excitations. On admissible spacetime slabs, the coherent sector is selected by a bounded projector $`\Pi_{\mathrm{coh}}`$ whose existence and stability follow from contractivity and gap conditions.

Coherent fixed points define stable backgrounds around which controlled perturbative expansions may be performed. The admissibility conditions of MTT ensure that truncation to the coherent sector is well defined and that higher excitations do not destabilize the effective description. All constructions in the present paper are implicitly restricted to such admissible domains.

## AQFT nets from admissible charts

In companion work, algebraic quantum field theory (AQFT) nets have been derived directly from the overlap structure of admissible charts in Modal Triplet Theory. In that construction, locality, isotony, and the absence of a global section arise from the impossibility of extending admissible descriptions beyond controlled overlaps.

When a spacetime encoding exists, these admissibility–indexed nets reduce to standard Haag–Kastler nets indexed by spacetime regions. This result provides a rigorous foundational explanation for locality and causal structure without assuming spacetime or quantum fields as primitive objects.

## Quantum field theory on curved spacetime

Building on the net construction, a projection $`\Pi_{\mathrm{QFT}}`$ has been shown to map coherent modal configurations to algebraic quantum field theory on globally hyperbolic curved spacetimes. The image of this projection consists of:

- a locally covariant field algebra defined by CCR or CAR relations,

- a Hadamard state ensuring well–defined local observables and renormalization,

- a slab–local notion of propagation encoded by the time–slice axiom.

Within this framework, perturbative algebraic quantum field theory (pAQFT) provides a rigorous construction of interacting fields, renormalized time–ordered products, and causally well behaved observables.

## Derivation of perturbative amplitudes

Most recently, perturbative scattering amplitudes and phenomenology have been derived from Modal Triplet Theory using AQFT and pAQFT. In that work, Feynman rules, loop corrections, and renormalization group flow are obtained as consequences of the algebraic construction, with all effective couplings determined by internal overlap integrals and curvature–gap data.

Crucially, that derivation makes explicit the conditions under which scattering amplitudes exist, distinguishing asymptotically flat or stationary regimes from generic curved or time–dependent backgrounds where only local or in–in observables are meaningful.

## Scope of the present work

Given these results, the mathematical necessity of diagrammatic perturbation theory within the projected quantum field theory is no longer in question. The present paper therefore does *not* attempt to rederive amplitudes or to provide an alternative to the AQFT or pAQFT frameworks.

Instead, we ask a different question: why does the algebraic construction inevitably reproduce a perturbative grammar organized in terms of propagators, vertices, and diagrams? What structural features of the underlying modal theory force this familiar form?

The aim of this paper is to show that diagrammatics is already implicit at the level of coherent modal fluctuations, prior to projection to four–dimensional spacetime or the introduction of quantum field theoretic notions. The AQFT and pAQFT frameworks then serve to make this structure precise, local, and renormalizable, rather than to create it.

## Interpretive stance

Throughout this paper we adopt the following stance:

- AQFT and pAQFT provide the correct rigorous framework for quantum field theory.

- Modal diagrammatics is an explanatory viewpoint that clarifies why those frameworks yield diagrammatic perturbation theory.

- No claim is made that modal diagrammatics alone suffices to define a complete quantum field theory.

With this context in place, we now turn to the general structural conditions under which diagrammatic perturbation theory arises, independent of any specifically quantum interpretation.

# Coherence, stability, and perturbation: the universal setup

Before specializing to modal geometry, it is useful to identify the minimal structural ingredients that give rise to diagrammatic perturbation theory in any context. This section abstracts away from quantum mechanics, spacetime locality, and modal details in order to isolate the universal mechanism underlying Feynman–type diagrammatics.

## Stable backgrounds and quadratic cores

Consider a system described by a functional $`S[\Phi]`$ on some space of configurations $`\Phi`$. Suppose that $`S`$ admits a stable background configuration $`\Phi_{\ast}`$, in the sense that $`\Phi_{\ast}`$ is a stationary point and that fluctuations around $`\Phi_{\ast}`$ are controlled by a nondegenerate quadratic form. Writing
``` math
\Phi = \Phi_{\ast} + \varphi,
```
one may expand
``` math
S[\Phi_{\ast} + \varphi]
=
S[\Phi_{\ast}]
+
\frac{1}{2}\langle \varphi, K \varphi\rangle
+
S_{\mathrm{int}}[\varphi],
```
where $`K`$ is the Hessian of $`S`$ at $`\Phi_{\ast}`$ and $`S_{\mathrm{int}}`$ collects all higher–order terms.

The operator $`K`$ defines the *quadratic core* of the theory. Its inverse, when it exists on an appropriate subspace, governs linear response and dominates the behavior of small fluctuations. The existence of such a quadratic core is the essential prerequisite for any perturbative expansion.

## Projection and truncation

In many physical systems, not all fluctuation directions are dynamically relevant. Stability often requires that fluctuations be restricted to a subspace selected by a projection operator $`\Pi`$, which removes unstable, rapidly growing, or otherwise inadmissible modes.

We therefore consider fluctuations of the form
``` math
\varphi_{\mathrm{eff}} := \Pi \varphi,
```
and replace $`K`$ by its restriction $`K_{\mathrm{eff}} := \Pi K \Pi`$. A perturbative description is meaningful only if:

- the projection $`\Pi`$ is bounded on the domain of interest,

- the restricted quadratic form $`K_{\mathrm{eff}}`$ is invertible on the projected subspace,

- higher–order terms $`S_{\mathrm{int}}`$ remain controlled under this truncation.

These conditions formalize the notion of an *admissible perturbative sector*. They are independent of whether the underlying theory is classical or quantum.

## Gaussian dominance and Wick expansion

Given a stable quadratic core, perturbative expansions are dominated by Gaussian fluctuations. Formally, one considers a generating functional of the form
``` math
Z[J] = \int \mathcal{D}\varphi_{\mathrm{eff}}\;
\exp\!\left(
W_0[\varphi_{\mathrm{eff}}] + W_{\mathrm{int}}[\varphi_{\mathrm{eff}}] + \langle J,
\varphi_{\mathrm{eff}}\rangle
\right),
```
where $`W_0`$ is quadratic and $`W_{\mathrm{int}}`$ contains higher–order interactions. The precise interpretation of the exponential (oscillatory, probabilistic, or otherwise) is not relevant at this stage.

The crucial fact is that expectation values with respect to the quadratic part $`W_0`$ satisfy Wick’s theorem: all higher moments are determined by pairwise contractions defined by the inverse of $`K_{\mathrm{eff}}`$. As a result, perturbative expansions of $`Z[J]`$ organize themselves into sums over pairings and higher–order interaction insertions.

This combinatorial structure is universal. It depends only on the existence of a Gaussian core and not on the interpretation of the underlying measure. The resulting bookkeeping is precisely what is encoded by diagrammatic perturbation theory.

## Propagators and vertices as universal objects

From this perspective, the fundamental objects of diagrammatics have a purely structural origin:

- the *propagator* is the inverse of the restricted quadratic form $`K_{\mathrm{eff}}`$,

- the *vertices* are given by higher functional derivatives of $`S_{\mathrm{int}}`$,

- diagrams enumerate the combinatorics of Wick contractions and interaction insertions.

No reference has been made to quantization, canonical commutation relations, Hilbert spaces, or spacetime locality. Diagrammatic perturbation theory is thus not a specifically quantum construction, but the natural perturbative language of any system with a stable, projected quadratic core.

## Universality across physical theories

The same structure appears in a wide range of contexts:

- in relativistic quantum field theory, with oscillatory weights $`e^{iS}`$,

- in classical statistical field theory, with probabilistic weights $`e^{-S_E}`$,

- in condensed matter systems near critical points,

- in effective theories obtained by integrating out fast degrees of freedom.

What distinguishes these cases is not the combinatorial structure of the expansion, but the physical interpretation of the propagator and the meaning of the underlying measure. The diagrammatic grammar itself is universal.

## Implications for the present work

The discussion above shows that the appearance of propagators, vertices, and diagrams is forced by coherence, stability, and truncation, rather than by any intrinsically quantum principle. In the remainder of this paper, we apply this universal reasoning to the specific case of Modal Triplet Theory.

We will show that coherent modal fluctuations around stable fixed points satisfy the conditions outlined above, and that a well–defined diagrammatic expansion already exists at the modal level. Projection to four–dimensional spacetime then produces the familiar Feynman rules of perturbative quantum field theory as a derived shadow of this more primitive structure.

# Modal configuration space and coherent fluctuations

We now specialize the universal perturbative structure described in Section 3 to the modal framework of Modal Triplet Theory (MTT). The goal of this section is to identify the precise modal objects that play the roles of background configuration, admissible fluctuations, and effective degrees of freedom. No quantum field theoretic structure is introduced here; the discussion remains entirely at the level of modal geometry and coherent dynamics.

## Modal configuration space

The fundamental configuration space of Modal Triplet Theory is a product manifold
``` math
M_{10} = Y_4 \times B_1 \times B_2 \times B_3 ,
```
where $`Y_4`$ is a four–dimensional Lorentzian spacetime and the $`B_n`$ are compact internal modal bundles. Fields on $`M_{10}`$ represent complete modal configurations, encoding both spacetime behavior and internal structure.

Dynamics on $`M_{10}`$ are governed by an action functional $`S_{10}[\Psi]`$ together with selection and stability principles that restrict attention to dynamically meaningful sectors. In particular, admissible configurations are those for which coherent projection and truncation control are available.

## Coherent fixed points

A central role is played by coherent fixed points $`\Psi_{\ast}`$ of the modal dynamics. These are configurations satisfying:

- stationarity of the modal action,

- spectral gap conditions separating a finite–dimensional coherent sector from higher excitations,

- contractivity of the induced flow on admissible spacetime slabs.

Such fixed points define stable modal backgrounds around which controlled perturbative expansions may be performed. Physically, they correspond to persistent macroscopic structures admitting effective lower–dimensional descriptions.

## Coherent projection and admissible slabs

Let $`\Pi_{\mathrm{coh}}`$ denote the bounded projector onto the coherent sector associated with a given fixed point $`\Psi_{\ast}`$. The existence and boundedness of $`\Pi_{\mathrm{coh}}`$ are guaranteed only on restricted spacetime regions, referred to as *admissible slabs*. On these slabs:

- coherent and noncoherent modes are spectrally separated,

- truncation to the coherent sector is dynamically stable,

- perturbative control is preserved under evolution.

All subsequent constructions in this paper are implicitly restricted to such admissible slabs. No claim is made that coherent projection exists globally or indefinitely.

## Coherent fluctuations

Given a coherent fixed point $`\Psi_{\ast}`$, we consider fluctuations of the form
``` math
\Psi = \Psi_{\ast} + \eta .
```
Only the coherent component of $`\eta`$ is retained:
``` math
\eta_{\mathrm{coh}} := \Pi_{\mathrm{coh}} \eta .
```
Noncoherent components correspond to rapidly decaying or unstable modes and are discarded from the effective description.

The space of coherent fluctuations thus defines the effective configuration space for perturbation theory. Importantly, this restriction is not an approximation but a dynamically enforced truncation arising from the stability structure of the modal system.

## Modal action expanded about a fixed point

Restricting the modal action to coherent fluctuations yields
``` math
S_{\mathrm{coh}}[\eta_{\mathrm{coh}}]
=
S_{10}[\Psi_{\ast} + \eta_{\mathrm{coh}}] .
```
Expanding about $`\eta_{\mathrm{coh}} = 0`$ gives
``` math
S_{\mathrm{coh}}[\eta]
=
S_{10}[\Psi_{\ast}]
+
\frac{1}{2}\langle \eta, \mathcal{K}\eta\rangle
+
S_{\mathrm{int}}[\eta],
```
where $`\mathcal{K}`$ is the Hessian of the action at $`\Psi_{\ast}`$, restricted to the coherent sector, and $`S_{\mathrm{int}}`$ collects all cubic and higher–order terms.

This decomposition realizes explicitly the general structure discussed in Section 3: a stable quadratic core plus controlled interactions, defined entirely within the coherent modal subspace.

## Interpretation

At this stage, no spacetime fields, propagators, vertices, or diagrams have been introduced. Nevertheless, all ingredients required for a diagrammatic perturbative expansion are already present:

- a stable background configuration $`\Psi_{\ast}`$,

- a bounded projection selecting admissible fluctuations,

- a quadratic form governing linear response,

- higher–order interaction terms encoding mode coupling.

In the next section we show that the inverse of the restricted quadratic operator $`\mathcal{K}`$ defines a natural propagator for coherent modal fluctuations, and that this object plays the structural role of a propagator in diagrammatic perturbation theory.

# The modal quadratic core and the modal propagator

In this section we identify the modal analog of the propagator. As emphasized earlier, this object is not introduced as a spacetime Green’s function or as a quantum expectation value. Instead, it arises as the controlled inverse of the quadratic form governing coherent modal fluctuations around a stable fixed point.

## The coherent Hessian

Let $`\Psi_{\ast}`$ be a coherent fixed point on an admissible slab, and let $`\mathcal{K}`$ denote the Hessian of the modal action evaluated at $`\Psi_{\ast}`$, restricted to the coherent sector:
``` math
\mathcal{K}
:=
\left.
\frac{\delta^2 S_{10}}{\delta \Psi^2}
\right|_{\Psi=\Psi_{\ast}}
\quad\text{with domain restricted by }\Pi_{\mathrm{coh}} .
```

By construction, $`\mathcal{K}`$ is a self–adjoint operator on the coherent fluctuation space, with spectrum bounded away from zero by the modal gap. The gap condition ensures that $`\mathcal{K}`$ is invertible on admissible slabs, up to boundary and gauge degeneracies that will be addressed separately.

Physically, $`\mathcal{K}`$ governs linear response of the coherent background to small perturbations. It plays the same structural role as the kinetic operator in ordinary field theory, but it acts on fields defined over the full modal space $`M_{10}`$.

## Admissible inversion

Because coherent projection and stability are only guaranteed on finite spacetime regions, the inverse of $`\mathcal{K}`$ must be defined with care. We therefore define an *admissible inverse* as an operator $`G`$ satisfying
``` math
\mathcal{K} G = G \mathcal{K} = \Pi_{\mathrm{coh}}
```
on the admissible slab, together with boundary conditions compatible with truncation control and modal stability.

The precise choice of boundary conditions (retarded, advanced, symmetric, or otherwise) is not fixed at the modal level. Different choices correspond to different effective propagators after projection and are selected downstream when causal structure and state choice are imposed via algebraic quantum field theory.

## Definition of the modal propagator

We define the *modal propagator* to be any admissible inverse of the coherent Hessian:
``` math
G := \mathcal{K}^{-1}_{\mathrm{admissible}} .
```

This object carries:

- dependence on spacetime coordinates in $`Y_4`$,

- dependence on internal coordinates in $`B_1\times B_2\times B_3`$,

- indices associated with internal bundle structure and representation content,

- selection rules inherited from the coherent sector.

At this stage, $`G`$ is a purely modal object. It does not yet encode microcausality, positive frequency, or vacuum structure. Those properties emerge only after projection to four–dimensional quantum field theory.

## Comparison with spacetime propagators

Despite these differences, the analogy with ordinary propagators is exact at the structural level. In any perturbative expansion governed by a quadratic core, pairwise contractions of fluctuations are weighted by the inverse of the quadratic operator. The modal propagator $`G`$ therefore plays precisely the role required for diagrammatic perturbation theory.

The familiar spacetime propagators of quantum field theory arise when:

- the modal propagator is projected onto a basis of coherent modes,

- internal degrees of freedom are integrated out,

- causal boundary conditions are selected by the choice of state.

This projection will be made explicit in later sections.

## Gauge and constraint directions

In gauge theories and constrained systems, the operator $`\mathcal{K}`$ may possess zero modes associated with gauge redundancies. At the modal level, these are handled by restricting $`\mathcal{K}`$ to the physical coherent subspace and, if necessary, by introducing gauge–fixing terms compatible with coherent projection.

The treatment of gauge symmetry and the role of BRST structure are discussed separately after projection, where algebraic control of constraints is available. For the purposes of modal diagrammatics, it suffices that $`\mathcal{K}`$ admits a bounded inverse on the relevant coherent degrees of freedom.

## Interpretation

The modal propagator is not a quantum object, nor does it presuppose probabilistic interpretation. It is the linear response kernel of a stable coherent modal system. Its appearance is forced by the existence of a quadratic core and controlled truncation.

In the next section we show that higher variations of the modal action define interaction vertices, and that together with the modal propagator they generate a full diagrammatic expansion at the modal level.

# Modal vertices and internal selection rules

Having identified the modal propagator as the inverse of the coherent quadratic core, we now turn to the interaction terms. In this section we show that higher–order variations of the modal action define natural interaction vertices, and that the familiar selection rules and overlap integrals of the effective four–dimensional theory arise directly from their internal structure.

## Higher variations of the modal action

Let $`S_{\mathrm{int}}[\eta]`$ denote the interaction part of the coherent–restricted modal action introduced in Section 4. For $`n \ge 3`$, we define the $`n`$–point modal vertex by
``` math
V_n(\eta_1,\ldots,\eta_n)
:=
\left.
\frac{\delta^n S_{\mathrm{int}}}{\delta\eta^n}
\right|_{\eta=0}
(\eta_1,\ldots,\eta_n).
```

Each $`V_n`$ is a multilinear functional acting on coherent fluctuations. It encodes all nonlinear couplings permitted by the modal geometry, including spacetime dependence, internal bundle structure, and symmetry constraints. No additional assumptions are introduced at this stage.

## Locality and structure of modal vertices

The modal action $`S_{10}`$ is local on the full configuration space $`M_{10}`$. As a result, the vertices $`V_n`$ inherit a locality property in both spacetime and internal directions: they couple only fluctuations evaluated at the same point of $`Y_4`$ and at coincident internal coordinates, modulo derivatives appearing in the action.

Structurally, a modal vertex may be written schematically as
``` math
V_n \sim \int_{Y_4} d^4x \int_{B_1\times B_2\times B_3} d\mu\;
\mathcal{V}_n(x,y)\,
\eta(x,y)^n,
```
where $`\mathcal{V}_n`$ encodes tensorial, spinorial, and gauge structure determined by the modal geometry.

## Internal mode expansion and overlap integrals

To connect with effective lower–dimensional descriptions, we expand coherent fluctuations in a basis of internal modes:
``` math
\eta(x,y) = \sum_{\alpha} \phi_\alpha(x)\,\chi_\alpha(y),
```
where $`\{\chi_\alpha\}`$ are orthonormal eigenmodes on $`B_1\times B_2\times B_3`$ compatible with the coherent projection.

Inserting this expansion into the vertex functional yields
``` math
V_n \;\sim\; \sum_{\alpha_1,\ldots,\alpha_n}
\left(
\int_{B_1\times B_2\times B_3}
\chi_{\alpha_1}(y)\cdots \chi_{\alpha_n}(y)\, d\mu
\right)
\int_{Y_4} \phi_{\alpha_1}(x)\cdots \phi_{\alpha_n}(x)\, d^4x .
```

The internal integral appearing here is precisely an *overlap integral*. Its value determines the strength of the corresponding interaction in the effective theory. In this way, overlap integrals arise automatically as vertex coefficients, rather than being introduced by hand.

## Selection rules and modal constraints

Not all combinations of internal modes contribute to $`V_n`$. The structure of the modal geometry imposes selection rules that restrict which overlaps are nonzero. These include:

- symmetry constraints from internal isometries and bundle structure,

- representation constraints associated with gauge and spinor indices,

- the “two–of–three” selection mechanism characteristic of Modal Triplet Theory.

These selection rules ensure that only dynamically admissible interactions appear in the effective description. From the modal viewpoint, they are simply statements about which multilinear contractions of coherent modes are allowed by geometry and stability.

## Comparison with effective field theory vertices

In conventional effective field theory, interaction vertices and coupling constants are specified as part of the Lagrangian. In the modal framework, the same data emerge from the evaluation of $`V_n`$ on coherent mode expansions. The apparent arbitrariness of effective couplings is replaced by concrete geometric integrals.

This observation explains why the couplings appearing in the effective four–dimensional theory are finite, bounded, and correlated: they are projections of a single underlying modal interaction functional.

## Interpretation

Modal vertices provide the second essential ingredient of diagrammatic perturbation theory. Together with the modal propagator identified in Section 5, they define a complete set of building blocks for a diagrammatic expansion at the modal level.

In the next section we show that these ingredients combine with Gaussian combinatorics to produce a full Wick–type expansion of coherent modal fluctuations, yielding a genuine diagrammatic perturbation theory “upstairs” before any reference to quantum fields or spacetime propagators.

# Modal diagrammatics: Wick expansion upstairs

With the modal propagator and interaction vertices in hand, we now show how a full diagrammatic perturbation theory arises directly at the level of coherent modal fluctuations. The construction in this section mirrors the familiar Wick expansion of quantum field theory, but it is formulated entirely on modal configuration space and does not presuppose quantization, Hilbert spaces, or operator algebras.

## Formal generating functional

Consider a formal generating functional for coherent fluctuations on an admissible slab,
``` math
Z[J] :=
\int_{\mathrm{coh}} \mathcal{D}\eta\;
\exp\!\left(
i S_{\mathrm{coh}}[\eta] + i\langle J,\eta\rangle
\right),
```
where $`S_{\mathrm{coh}}[\eta]`$ is the coherent–restricted modal action defined in Section 4, and $`J`$ is a source coupled linearly to the coherent fluctuation $`\eta`$.

Here and throughout, $`Z[J]`$ is used purely as a formal device for organizing the Wick expansion of coherent fluctuations around a stable quadratic core; no claim is made that it defines a fundamental path integral or a globally well–defined measure, and all rigorous notions of causality, positivity, and renormalization are supplied only after projection by AQFT and pAQFT.

The measure $`\mathcal{D}\eta`$ is not assumed to define a fundamental path integral. It is used here as a compact notation for the perturbative expansion of correlation functionals around the coherent fixed point. All statements below are understood as formal expansions valid within the admissible, truncated sector.

## Gaussian core and contractions

Separating the quadratic and interaction parts of the action,
``` math
S_{\mathrm{coh}}[\eta]
=
\frac{1}{2}\langle \eta,\mathcal{K}\eta\rangle
+
S_{\mathrm{int}}[\eta],
```
the leading contribution to $`Z[J]`$ is Gaussian. Expectation values with respect to the quadratic part are therefore determined entirely by pairwise contractions defined by the modal propagator $`G=\mathcal{K}^{-1}`$:
``` math
\langle \eta(x_1,y_1)\,\eta(x_2,y_2)\rangle_0
=
G\bigl((x_1,y_1),(x_2,y_2)\bigr).
```

This contraction rule is the sole combinatorial input required for diagrammatic perturbation theory.

## Wick expansion

Expanding the interaction exponential,
``` math
\exp\!\bigl(i S_{\mathrm{int}}[\eta]\bigr)
=
\sum_{n=0}^\infty \frac{i^n}{n!} S_{\mathrm{int}}[\eta]^n,
```
and evaluating expectation values term by term with respect to the Gaussian core yields a Wick expansion. Each term is expressed as a sum over all possible pairings of fluctuation fields, with contractions weighted by the modal propagator $`G`$ and interaction insertions weighted by the modal vertices $`V_n`$.

The resulting expansion may be represented graphically by diagrams with:

- lines corresponding to modal propagators,

- vertices corresponding to $`V_n`$,

- integration over spacetime and internal coordinates at each vertex.

These diagrams are *modal diagrams*. They encode the perturbative structure of coherent modal fluctuations.

## Universality of the diagrammatic grammar

The appearance of diagrams at this stage is entirely independent of any quantum interpretation. It follows solely from:

- the existence of a stable quadratic core,

- the restriction to an admissible fluctuation sector,

- the locality of interaction terms,

- Gaussian combinatorics.

No reference has been made to operator ordering, commutation relations, or probability amplitudes. Diagrammatics is thus seen to be a universal perturbative grammar for coherent systems, rather than a distinctive feature of quantum mechanics.

## Relation to perturbative expansions in other contexts

The same Wick expansion appears in a wide range of physical theories:

- in classical statistical field theory, where $`S_{\mathrm{coh}}`$ plays the role of a free energy functional,

- in condensed matter systems near critical points,

- in effective theories obtained by integrating out fast degrees of freedom.

The modal diagrammatic expansion unifies these cases by identifying the common structural origin of diagrammatics in coherence and stability.

## Interpretation

Modal diagrammatics should be understood as a bookkeeping device for perturbative coherent fluctuations. It is not a complete physical theory and does not by itself encode causal structure, positivity, or renormalization constraints. Those features emerge only after projection to algebraic quantum field theory.

Nevertheless, the existence of a well–defined diagrammatic expansion at the modal level explains why any rigorous downstream construction that permits perturbation theory must reproduce the familiar diagrammatic rules. In the next section we show how projection to four–dimensional spacetime converts modal diagrammatics into the standard Feynman rules of perturbative quantum field theory.

# Projection to four dimensions: why Feynman rules look familiar

In the previous sections we have established the existence of a complete diagrammatic perturbation theory defined directly on modal configuration space. In this section we show how this “upstairs” diagrammatics projects to an effective four–dimensional description, and why the resulting rules coincide with the familiar Feynman rules of perturbative quantum field theory.

## Mode decomposition and effective fields

Let $`\eta(x,y)`$ denote a coherent modal fluctuation, with $`x\in Y_4`$ and $`y\in B_1\times B_2\times B_3`$. On an admissible slab, coherent fluctuations admit an expansion in a basis of internal modes,
``` math
\eta(x,y) = \sum_{\alpha} \phi_\alpha(x)\,\chi_\alpha(y),
```
where the $`\chi_\alpha`$ form an orthonormal set of internal eigenmodes compatible with the coherent projection, and the $`\phi_\alpha(x)`$ are effective four–dimensional fields.

The index $`\alpha`$ labels both representation content and internal excitation level. Modes with large internal eigenvalues lie outside the coherent sector and are suppressed by the gap, while a finite set of low–lying modes survives as effective degrees of freedom.

## Projection of the modal propagator

Inserting the mode expansion into the modal propagator yields
``` math
G\bigl((x,y),(x',y')\bigr)
=
\sum_{\alpha,\beta}
G_{\alpha\beta}(x,x')\,
\chi_\alpha(y)\chi_\beta(y'),
```
where
``` math
G_{\alpha\beta}(x,x')
=
\int d\mu(y)\,d\mu(y')\;
\chi_\alpha(y)\,
G\bigl((x,y),(x',y')\bigr)\,
\chi_\beta(y').
```

Orthogonality and symmetry of the internal modes imply that $`G_{\alpha\beta}`$ is diagonal to leading order in the coherent sector. The diagonal components $`G_{\alpha\alpha}(x,x')`$ play the role of spacetime propagators for the effective fields $`\phi_\alpha(x)`$, with masses determined by the internal spectrum and curvature–gap corrections.

Thus, the familiar spacetime propagator arises as the projection of the modal propagator onto a single coherent mode.

## Projection of modal vertices

A similar projection occurs for interaction vertices. Inserting the mode expansion into the $`n`$–point modal vertex $`V_n`$ gives
``` math
V_n
\;\sim\;
\sum_{\alpha_1,\ldots,\alpha_n}
\left(
\int_{B_1\times B_2\times B_3}
\chi_{\alpha_1}(y)\cdots\chi_{\alpha_n}(y)\,d\mu
\right)
\int_{Y_4}
\phi_{\alpha_1}(x)\cdots\phi_{\alpha_n}(x)\,d^4x .
```

The internal integral defines an effective coupling constant,
``` math
g_{\alpha_1\cdots\alpha_n}
:=
\int_{B_1\times B_2\times B_3}
\chi_{\alpha_1}(y)\cdots\chi_{\alpha_n}(y)\,d\mu,
```
which is precisely the overlap integral appearing in the effective four–dimensional theory.

Selection rules inherited from the modal geometry ensure that only a restricted set of such couplings is nonzero, reproducing gauge invariance, representation constraints, and the characteristic “two–of–three” structure of Modal Triplet Theory.

## Diagrammatic correspondence

Combining the projected propagators and vertices yields a diagrammatic expansion entirely in terms of four–dimensional fields $`\phi_\alpha(x)`$, with:

- lines weighted by spacetime propagators $`G_{\alpha\alpha}(x,x')`$,

- vertices weighted by overlap–defined couplings $`g_{\alpha_1\cdots\alpha_n}`$,

- integration over spacetime coordinates at each vertex.

This is exactly the structure of standard Feynman rules. The only difference lies in the interpretation: propagators and vertices are not fundamental postulates, but projections of modal objects.

## Masses, thresholds, and curvature effects

The internal spectrum associated with the modal operator $`\mathcal{K}`$ determines the effective mass parameters of the four–dimensional fields. Curvature–dependent shifts in the modal spectrum translate directly into curvature–gap mass corrections, which appear as thresholds in the effective theory.

In perturbative calculations, these thresholds control decoupling and renormalization group flow, in agreement with standard effective field theory expectations.

## Why the rules must look familiar

The preceding analysis shows that the familiar form of Feynman rules is not accidental. Once a coherent modal sector exists and admits a stable quadratic core, projection to a lower–dimensional effective description necessarily produces:

- propagators as inverses of quadratic operators,

- vertices as overlap integrals of internal modes,

- diagrammatic expansions organized by Wick contractions.

Any effective theory derived from such a projection must therefore employ a perturbative grammar that is indistinguishable from standard Feynman diagrammatics.

## Interpretation

Feynman rules are thus best understood as the *projected shadow* of a more primitive diagrammatic structure defined on modal configuration space. Their universality across quantum field theory, classical statistical field theory, and effective descriptions of gravity reflects the universality of coherence–based perturbative expansions, rather than a special feature of quantization.

In the next sections we explore the broader implications of this viewpoint, including its relation to classical statistical field theory, its interpretation of quantumness as a coherence regime, and its consequences for perturbative quantum gravity.

# Why classical statistical field theory also has diagrams

One of the most striking facts about Feynman diagrammatics is that it appears in theories that are not intrinsically quantum. Diagrammatic expansions play a central role in classical statistical field theory, critical phenomena, polymer physics, and equilibrium and nonequilibrium statistical mechanics. This section explains why this is not an accidental resemblance, but a direct consequence of the universal perturbative structure identified earlier.

## Gaussian measures and perturbation theory

Consider a classical statistical field theory defined by a Hamiltonian or free energy functional $`H[\phi]`$. The corresponding partition function takes the form
``` math
Z = \int \mathcal{D}\phi\; e^{-\beta H[\phi]},
```
where $`\beta`$ is the inverse temperature. If $`H`$ admits a stable configuration $`\phi_{\ast}`$, one may expand
``` math
H[\phi_{\ast}+\varphi]
=
H[\phi_{\ast}]
+
\frac{1}{2}\langle \varphi, K \varphi\rangle
+
H_{\mathrm{int}}[\varphi],
```
with $`K`$ the Hessian at $`\phi_{\ast}`$.

As in the modal and quantum cases, the quadratic term defines a Gaussian measure, and the interaction term can be treated perturbatively. Expectation values with respect to the Gaussian part satisfy Wick’s theorem, and perturbative corrections organize themselves into diagrams with propagators given by $`K^{-1}`$ and vertices determined by higher derivatives of $`H_{\mathrm{int}}`$.

## Comparison with quantum field theory

The formal similarity between classical statistical field theory and quantum field theory is well known. In Euclidean quantum field theory, correlation functions are defined by weights of the form $`e^{-S_E[\phi]}`$, which are indistinguishable from statistical partition functions at the level of perturbative expansion.

From the perspective developed here, this similarity is not surprising. In both cases:

- a stable background defines a quadratic core,

- perturbative control requires truncation to an admissible fluctuation sector,

- Gaussian dominance leads to Wick expansion,

- diagrams encode the combinatorics of contractions.

The difference between classical and quantum theories lies in interpretation, not in the diagrammatic grammar. Quantum theories typically involve oscillatory weights and additional structure related to causality and unitarity, while classical statistical theories involve probabilistic weights and equilibrium interpretation. The underlying perturbative combinatorics is identical.

## Diagrammatics without quantization

The existence of Feynman diagrams in classical statistical systems demonstrates that diagrammatics does not require quantization in the sense of operator algebras or canonical commutation relations. It requires only:

- a well–defined quadratic form governing fluctuations,

- a notion of admissible perturbative sector,

- controlled interactions.

This observation reinforces the central thesis of this paper: diagrammatics is the perturbative language of coherent systems, not a uniquely quantum construction.

## Interpretation in the modal framework

Within the modal framework, both quantum field theory and classical statistical field theory arise as effective descriptions of coherent modal sectors under different projections and interpretations. The same modal diagrammatics underlies both, with the difference between “quantum” and “classical” behavior determined by how the coherent sector is probed, coupled to an environment, or coarse–grained.

In particular, the appearance of diagrams in classical statistical field theory is naturally explained as the projection of modal diagrammatics onto a regime where the effective description is probabilistic rather than oscillatory.

## Summary

The presence of Feynman diagrams in classical statistical field theory is not an anomaly but a confirmation of their universal origin. Diagrammatic perturbation theory reflects the combinatorics of Gaussian fluctuations around stable backgrounds and therefore arises whenever coherence and stability permit a perturbative expansion.

This universality strongly supports the interpretation of Feynman rules as a general feature of coherent systems, rather than as an intrinsic marker of quantization.

# Quantumness as a coherence regime

The modal diagrammatics developed in the preceding sections suggests a reinterpretation of what is commonly referred to as “quantumness.” Rather than viewing quantum behavior as a fundamental ontological property of matter, we propose that it be understood as a particular regime of coherent, projected description. In this section we make this claim precise and show how familiar quantum features arise naturally within this framework.

## Projected coherence and effective linearity

A defining feature of quantum systems is the apparent linearity of their state space and the superposition principle. In the modal framework, this linear structure does not reflect the full underlying configuration space, which is highly nonlinear and constrained. Instead, it emerges as an effective property of the coherent sector selected by $`\Pi_{\mathrm{coh}}`$.

Within an admissible slab, coherent fluctuations form a dynamically stable subspace on which the quadratic core of the modal action dominates. To leading order, dynamics in this sector is linear, and superposition holds as an approximation. Nonlinearities appear only through controlled interaction terms and are suppressed by gap and stability conditions.

Thus, superposition is not a universal property of physical states, but a consequence of restricted access to a coherent subspace where linearization is valid.

## Probabilities and coarse–grained selection

Quantum mechanics assigns probabilistic outcomes to measurement events via the Born rule. From the modal perspective, probabilities arise not from intrinsic randomness but from coarse–grained selection among multiple underlying coherent configurations that project to the same effective description.

When an effective observable fails to distinguish between distinct modal microstates, outcomes must be described statistically. The resulting probabilities reflect the geometry and measure of basins in modal configuration space, conditioned on admissibility and stability constraints. In this sense, quantum probabilities encode ignorance induced by projection, not fundamental indeterminism.

This viewpoint is compatible with the algebraic formulation of quantum field theory, where states are positive linear functionals on an algebra of observables rather than ontological wavefunctions.

## Noncommutativity and incompatible projections

Another hallmark of quantum theory is the noncommutativity of observables. In the modal framework, noncommutativity arises when different effective observables correspond to incompatible projections of the underlying modal space.

Two observables fail to commute when there exists no admissible chart in which both can be represented sharply and simultaneously. This mirrors the net–theoretic interpretation of locality and contextuality, where noncommutativity reflects the impossibility of joint representability rather than an abstract algebraic postulate.

Noncommutativity is thus a structural feature of projected descriptions, not a fundamental property of the underlying modal dynamics.

## Wave behavior of composite systems

The interpretation of quantumness as a coherence regime provides a natural explanation for the wave–like behavior of composite systems, including large molecules, neutrons, and positronium. Such systems exhibit interference only when:

- internal degrees of freedom remain dynamically slaved,

- environmental coupling does not resolve path information,

- a coherent center–of–mass sector admits a stable quadratic description.

Under these conditions, the composite system occupies a single coherent basin whose effective description is governed by modal diagrammatics. When these conditions fail, coherence is lost and wave behavior disappears. The modal framework therefore predicts quantum interference as a conditional phenomenon, consistent with experimental observations.

## Classical limit and decoherence

The classical limit corresponds to regimes in which coherent projections become sharp and dominant, overlaps between admissible charts are large, and fluctuations are strongly suppressed by gaps. In such regimes, effective observables commute approximately and dynamics becomes deterministic.

Decoherence, in this view, is not a fundamental collapse process but a transition between coherence regimes: interactions with an environment reduce the admissible overlap of coherent charts and force a change in effective description.

## Summary

Quantumness emerges as a regime of coherent, projected dynamics characterized by:

- dominance of a quadratic core,

- stability under truncation,

- limited representability of observables,

- statistical description induced by projection.

Within this regime, diagrammatic perturbation theory, probabilistic outcomes, and noncommutativity arise naturally. Outside it, classical or nonperturbative descriptions become appropriate. This interpretation aligns quantum theory with a broader framework of coherence and stability rather than elevating it to a fundamental ontological status.

# Implications for quantum gravity

The interpretation of diagrammatics and quantumness developed in this paper has direct implications for the long–standing problem of quantum gravity. Rather than asking how to quantize spacetime globally, the modal framework reframes the question in terms of coherence, stability, and admissible perturbative sectors. In this section we show how this perspective clarifies both the successes and the limitations of perturbative quantum gravity.

## Gravity as an emergent coherent sector

In Modal Triplet Theory, spacetime geometry is not fundamental but emerges as a coherent sector of the modal configuration space. The metric on $`Y_4`$ represents a collective, low–energy description of underlying modal degrees of freedom that admit a stable fixed point and a spectral gap.

From this viewpoint, gravitational degrees of freedom are intrinsically composite. The “graviton,” when it exists, corresponds to a coherent fluctuation mode of the emergent geometric sector, rather than to a fundamental particle. As with other composite systems, a perturbative description is meaningful only when coherence and truncation conditions are satisfied.

## Modal quadratic core for geometry

Expanding the modal action about a coherent geometric fixed point yields a quadratic core governing small fluctuations of the emergent metric. The corresponding Hessian defines a modal kinetic operator for geometric fluctuations, whose admissible inverse plays the role of a graviton propagator in perturbative calculations.

In regimes where curvature is weak and the modal gap remains open, this quadratic core is stable and admits a controlled inverse. Modal diagrammatics then produces a perturbative expansion for gravitational fluctuations that coincides, after projection, with the standard Feynman diagram expansion of perturbative quantum gravity.

## Why perturbative quantum gravity works locally

Perturbative quantum gravity is known to be predictive as an effective field theory at low energies and weak curvature. In the modal framework, this success is explained by the existence of local admissible slabs on which:

- the coherent geometric sector is spectrally isolated,

- truncation to low–lying modes is stable,

- the quadratic core dominates over interactions.

On such slabs, modal diagrammatics is well defined and projects to the familiar graviton propagators and interaction vertices. Higher–order divergences reflect the breakdown of the effective description at scales where the modal gap closes or new coherent sectors enter.

## Why perturbative quantum gravity fails globally

The difficulties of quantum gravity—nonrenormalizability, background dependence, and breakdown near horizons or singularities—are often interpreted as failures of quantization. The modal framework offers a different explanation.

Globally, spacetime does not admit a single admissible coherent chart. Horizons, strong curvature regions, and topological obstructions correspond to failures of coherent projection and truncation control. In such regions:

- the modal gap may close,

- coherent and noncoherent modes mix,

- no stable quadratic core exists.

Under these conditions, modal diagrammatics itself ceases to be valid. The failure of perturbative quantum gravity is therefore not mysterious, but a direct consequence of the loss of coherence and admissibility.

## Relation to renormalization and effective field theory

From the modal perspective, the nonrenormalizability of perturbative quantum gravity reflects the necessity of introducing an infinite tower of counterterms once the projection to a single coherent sector becomes inadequate. This is precisely what one expects when truncation control is lost.

Conversely, the success of effective field theory treatments of gravity at low energies is explained by the persistence of a coherent geometric sector over a wide range of scales. Renormalization group flow describes how effective couplings evolve within this sector, but does not extend the domain of validity of the perturbative expansion.

## Quantum gravity without global quantization

The modal framework suggests that a fully global quantization of spacetime is neither necessary nor meaningful. Quantum gravitational behavior should instead be understood as a patchwork of locally coherent perturbative expansions, each valid on its own admissible domain and glued together where overlaps exist.

This picture aligns naturally with the absence of a global section in the net–theoretic description of spacetime and with the emergence of irreversibility at horizons. It also provides a principled explanation for why different approaches to quantum gravity succeed in complementary regimes without yielding a single universal framework.

## Summary

Within the modal diagrammatics viewpoint, quantum gravity is not the quantization of geometry as a whole, but the perturbative fluctuation theory of emergent coherent geometric sectors. Diagrammatic expansions are valid precisely where coherence, stability, and truncation permit them, and they fail where those conditions break down.

This interpretation demystifies both the partial success and the ultimate limitations of perturbative quantum gravity, and situates gravitational diagrammatics within the same coherence–based framework that underlies quantum field theory and classical statistical physics.

# Experimental resonances: composite interference and coherence

The interpretation of diagrammatics and quantumness developed in the preceding sections finds strong support in experimental observations of wave–like behavior in composite systems. Interference phenomena have now been observed not only for elementary particles, but also for neutrons, atoms, large molecules, and most recently for positronium. These experiments provide direct empirical evidence that wave behavior is a conditional feature of coherence rather than a marker of fundamental quantization.

## Wave behavior beyond elementary particles

Interference experiments with increasingly complex systems have demonstrated that wave–like behavior persists far beyond the scale of elementary particles. Notable examples include:

- neutron interferometry,

- atomic and molecular beam interference,

- interference of large organic molecules,

- recent demonstrations of center–of–mass wave behavior in positronium.

These systems differ widely in mass, internal structure, and stability. Yet under carefully controlled conditions they all exhibit interference patterns characteristic of a single coherent wave.

## Conditions for composite interference

From the modal perspective, these experiments share a common structural feature. Wave behavior appears only when:

- internal degrees of freedom remain dynamically slaved or gapped,

- environmental interactions do not resolve which–path information,

- a coherent center–of–mass sector admits a stable quadratic description.

Under these conditions, the full composite system occupies a single coherent basin in modal configuration space. The effective description of that basin is governed by the quadratic core and modal diagrammatics developed earlier.

If any of these conditions fail, coherence is lost and interference disappears. The transition from wave–like to particle–like behavior is therefore a transition between coherence regimes, not a change in underlying ontology.

## Positronium as a diagnostic example

Positronium provides a particularly illuminating example. As a bound state of an electron and a positron, positronium is:

- internally structured,

- unstable to annihilation,

- strongly coupled to electromagnetic fields.

Nevertheless, recent experiments have demonstrated interference of its center–of–mass motion when coherence time exceeds the transit time and environmental decoherence is suppressed. In the modal framework, this means that the internal relative coordinate and annihilation channels remain effectively frozen, allowing a coherent projection onto a single effective degree of freedom.

The observation of positronium interference therefore does not merely confirm a generic quantum prediction. It confirms that even fragile, composite systems can enter a coherent regime where a quadratic effective description applies and modal diagrammatics governs the observed behavior.

## Interpretation of interference patterns

In the coherence–based interpretation, interference patterns do not indicate that an object is “both wave and particle.” Rather, they indicate that the effective description of the system is constrained to a coherent sector in which:

- linear superposition is valid,

- fluctuations are governed by a Gaussian core,

- diagrammatic propagation applies.

Which–path detection, environmental coupling, or internal excitation corresponds to a loss of admissible overlap between coherent charts, forcing a change in effective description and destroying interference.

## Relation to decoherence and classical emergence

Decoherence experiments are often interpreted as demonstrating a transition from quantum to classical behavior. In the modal framework, decoherence is more precisely understood as a transition between coherence regimes. Increasing coupling to an environment reduces the size of admissible coherent sectors and suppresses the quadratic core responsible for diagrammatic behavior.

The classical limit is reached when a single effective description dominates and interference between alternative coherent histories becomes negligible. This transition is continuous and dynamical, not fundamental.

## Summary

Experimental observations of interference in composite systems provide direct empirical support for the interpretation of quantumness as a coherence regime. Wave behavior appears whenever a system admits a stable, projected quadratic description, and disappears when coherence is lost.

From this perspective, experiments such as positronium interference are not merely tests of quantum mechanics, but probes of the coherence structure underlying effective physical descriptions. They confirm that diagrammatic perturbation theory and wave behavior are features of coherent regimes, not intrinsic properties of matter.

# Relation to AQFT and pAQFT

The modal diagrammatics developed in this paper is intended as an explanatory framework, not as a replacement for algebraic quantum field theory (AQFT) or its perturbative extension (pAQFT). In this section we clarify the precise relationship between these approaches and delineate their respective roles within the broader Modal Triplet Theory program.

## Distinct roles of modal diagrammatics and AQFT

Modal diagrammatics addresses the question of *why* perturbative expansions organize themselves into propagators, vertices, and diagrams. It operates at the level of modal configuration space and relies on coherence, stability, and truncation to define a quadratic core and interaction structure.

AQFT, by contrast, addresses the question of *how* a consistent quantum field theory should be formulated once an effective spacetime description exists. It provides:

- a precise notion of locality via nets of algebras,

- causal propagation via the time–slice axiom,

- a state–independent formulation of observables,

- control over positivity, causality, and global consistency.

These two frameworks therefore operate at different conceptual levels. Modal diagrammatics explains the origin of diagrammatic perturbation theory, while AQFT ensures that the projected theory is mathematically well defined and physically meaningful.

## Why AQFT remains essential

Although modal diagrammatics produces a diagrammatic expansion at the level of coherent fluctuations, it does not by itself encode:

- microcausality or spacetime locality,

- positivity of states,

- renormalization locality and covariance,

- global consistency across overlapping regions.

These properties are guaranteed only after projection to AQFT. In particular, the choice of admissible propagators, boundary conditions, and states is fixed downstream by AQFT and pAQFT, not at the modal level. Modal diagrammatics therefore cannot replace AQFT as a foundation for quantum field theory.

## Compatibility with perturbative AQFT

Perturbative algebraic quantum field theory provides a rigorous framework for interacting quantum fields on curved spacetime. Within pAQFT:

- interacting observables are defined via time–ordered products,

- renormalization ambiguities are classified and controlled,

- perturbative expansions are guaranteed to respect locality and covariance.

The diagrammatic expansions arising in pAQFT coincide precisely with those obtained by projecting modal diagrammatics to four–dimensional spacetime. In this sense, modal diagrammatics may be viewed as the *upstream source* of the combinatorial structure that pAQFT makes rigorous.

## Interpretive clarity

A potential misunderstanding would be to view modal diagrammatics as an alternative quantization scheme or as a shortcut to defining quantum field theory without algebraic control. This is not the case. The present framework should be interpreted as follows:

- modal diagrammatics explains the inevitability of diagrammatic perturbation theory,

- AQFT and pAQFT provide the correct mathematical setting for its application,

- the two are complementary rather than competing.

This separation of explanatory and foundational roles allows one to retain the full rigor of AQFT while gaining conceptual insight into the origin of its perturbative structures.

## Relation to other approaches

The modal diagrammatics viewpoint is compatible with a wide range of approaches to quantum field theory and quantum gravity, including effective field theory, semiclassical gravity, and background–dependent perturbative quantization. What it adds is a unifying interpretation of diagrammatics as a consequence of coherence rather than as a postulate.

In particular, it aligns naturally with:

- the use of Gaussian fixed points in renormalization group analyses,

- the appearance of diagrams in statistical and condensed matter physics,

- the patchwise validity of perturbative quantum gravity.

## Summary

Modal diagrammatics does not undermine or bypass AQFT and pAQFT. Instead, it provides a conceptual explanation for why those rigorous frameworks necessarily give rise to diagrammatic perturbation theory when coherent, stable sectors exist.

By cleanly separating explanatory insight from mathematical foundation, the combined framework preserves rigor while deepening understanding.

# Limitations and scope

While the modal diagrammatics framework developed in this paper provides a unifying and explanatory account of the origin of Feynman rules, it is essential to delineate clearly its scope and limitations. This section specifies the domain of validity of the present analysis and identifies questions that lie beyond its intended reach.

## Local and slab–restricted validity

All constructions in this paper are implicitly restricted to *admissible slabs* in modal configuration space, where coherent projection is bounded and truncation control is maintained. The existence of a stable quadratic core, modal propagator, and controlled interaction vertices depends on these conditions.

No claim is made that modal diagrammatics is globally valid across all spacetime regions or modal configurations. In particular, near strong curvature, singularities, or topological obstructions where admissibility fails, the diagrammatic expansion ceases to be meaningful.

## Heuristic status of modal generating functionals

The formal generating functionals introduced in Sections 7 and 8 are not intended as fundamental path integrals. They serve as compact notation for perturbative expansions around coherent fixed points and rely on the existence of a well–defined Gaussian core.

Issues of measure definition, convergence, and global existence are addressed rigorously only after projection to algebraic quantum field theory. Modal diagrammatics should therefore be understood as a structural and combinatorial analysis, not as a standalone quantization procedure.

## Causality and positivity

Modal diagrammatics by itself does not encode microcausality, positivity of states, or unitarity. These properties are guaranteed only after projection to AQFT and pAQFT, where the choice of admissible propagators, boundary conditions, and states is fixed by algebraic criteria.

As a result, modal diagrammatics cannot be used in isolation to define physical amplitudes or probabilities. Its role is explanatory rather than foundational.

## Renormalization and ultraviolet control

Although the modal framework incorporates gap conditions and truncation control, it does not by itself provide a complete treatment of ultraviolet divergences or renormalization locality. The rigorous classification and control of counterterms is achieved only in the algebraic quantum field theory setting.

Modal diagrammatics explains why renormalization must take the form it does, but it does not replace the technical machinery required to implement it consistently.

## Nonperturbative phenomena

The present work is perturbative in nature. Phenomena such as confinement, mass gaps, topological transitions, and strong–coupling dynamics are not derived here. Where such effects are discussed, they are treated qualitatively or as consistency constraints rather than as theorems.

Any extension of modal diagrammatics to nonperturbative regimes would require additional structure beyond the scope of this paper.

## Interpretive boundaries

Finally, while the interpretation of quantumness as a coherence regime provides a compelling conceptual framework, it does not settle foundational questions about ontology, measurement, or the ultimate nature of physical reality. The present analysis is concerned with explanatory structure and mathematical inevitability, not with metaphysical claims.

## Summary

Modal diagrammatics offers a coherent and unifying explanation for the ubiquity of Feynman–type diagrammatics across physical theories. Its validity is restricted to coherent, stable, perturbative regimes and relies on downstream algebraic frameworks for full physical consistency.

Within these limits, it provides genuine insight into why perturbative quantum field theory takes the form it does, without claiming to supersede or replace established rigorous foundations.

# Conclusions

Feynman diagrams and their associated rules are among the most recognizable and effective tools in theoretical physics. Yet their ubiquity across quantum field theory, classical statistical field theory, condensed matter systems, and effective descriptions of gravity has long suggested that they are not tied exclusively to any single physical ontology. This paper has provided a unified explanation for that ubiquity.

Building on Modal Triplet Theory, we have shown that the essential structure underlying Feynman rules already exists at the level of coherent modal fluctuations around stable fixed points. Once a system admits:

- a coherent background configuration,

- a bounded projection selecting admissible fluctuations,

- a dominant quadratic core governing linear response,

- and controlled higher–order interactions,

a diagrammatic perturbation theory is inevitable. Propagators arise as admissible inverses of the quadratic core, vertices arise as higher variations of the action, and diagrams encode the combinatorics of Gaussian fluctuations via Wick expansion.

Within this framework, quantization is no longer the origin of diagrammatics. Rather, quantum field theory inherits a universal perturbative grammar that is already present whenever coherence and stability permit a truncated effective description. The role of algebraic quantum field theory and its perturbative extension is to make this structure rigorous by enforcing locality, causality, renormalization control, and positivity after projection to four–dimensional spacetime.

This perspective clarifies several longstanding puzzles. It explains why classical statistical field theories employ the same diagrammatic techniques as quantum field theories, why composite systems such as large molecules or positronium can exhibit wave–like behavior under appropriate conditions, and why perturbative quantum gravity is both locally successful and globally limited. In each case, diagrammatics signals the presence of a coherent perturbative regime rather than a fundamental quantum ontology.

The interpretation of quantumness that emerges from this analysis is therefore conditional and structural. Quantum behavior corresponds to a regime in which projected coherent dynamics is well approximated by a linear quadratic core with controlled interactions. Outside this regime, classical or nonperturbative descriptions become appropriate, and the diagrammatic expansion ceases to apply.

The results presented here do not replace existing rigorous frameworks. Instead, they provide an explanatory layer that unifies a wide range of perturbative techniques under a single coherence–based principle. Modal diagrammatics explains why algebraic quantum field theory, perturbative expansions, and Feynman rules take the form they do, without elevating any of them to fundamental status.

More broadly, this work suggests that many of the most familiar structures of theoretical physics arise not from quantization itself, but from the universal mathematics of stable systems subjected to controlled perturbation and projection. In this sense, Feynman rules are not axioms of nature, but the natural language spoken by coherent systems when they are probed gently enough.

<div class="thebibliography">

99

P. Nero, *The Book on Modal Triplet Theory: How Spacetime, Particles, Forces, and Quantum Theory Emerge from One Field*, Zenodo preprint (September 2025), <https://doi.org/10.5281/zenodo.17162671>.

P. Nero, *Modal Triplet Theory: Foundation*, Zenodo preprint (September 2025), <https://doi.org/10.5281/zenodo.16949762>.

P. Nero, *Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description*, Zenodo preprint (January 2026), <https://doi.org/10.5281/zenodo.18262454>.

P. Nero, *Universality and Robustness of the Coherent Sector in Modal Triplet Theory*, Zenodo preprint (2025), <https://doi.org/10.5281/zenodo.18260833>.

P. Nero, *Coherent Universality and the Inevitability of Projection-Based Quantum Theories*, Zenodo preprint (January 2026), <https://doi.org/10.5281/zenodo.18261806>.

P. Nero, *Closure and Inevitability in Modal Triplet Theory*, Zenodo preprint (January 2026), <https://doi.org/10.5281/zenodo.18255510>.

P. Nero, *From MTT to Quantum Field Theory on Curved Spacetime*, Zenodo preprint (2025), <https://doi.org/10.5281/zenodo.16950915>.

P. Nero, *Quantum Amplitudes from Modal Geometry*, Zenodo preprint (September 2025), <https://doi.org/10.5281/zenodo.17076216>.

P. Nero, *Effective Field Theory as a Shadow of Projection–Admissible Dynamics*, Zenodo preprint (January 2026), <https://doi.org/10.5281/zenodo.18262360>.

R. Haag, *Local Quantum Physics*, Springer, Berlin (1996).

R. Haag and D. Kastler, “An Algebraic Approach to Quantum Field Theory,” *J. Math. Phys.* **5**, 848 (1964).

R. Brunetti, K. Fredenhagen, and R. Verch, “The Generally Covariant Locality Principle,” *Commun. Math. Phys.* **237**, 31 (2003).

S. Hollands and R. M. Wald, “Local Wick Polynomials and Time Ordered Products of Quantum Fields in Curved Spacetime,” *Commun. Math. Phys.* **223**, 289 (2001).

K. Rejzner, *Perturbative Algebraic Quantum Field Theory*, Springer, Heidelberg (2016).

G. C. Wick, “The Evaluation of the Collision Matrix,” *Phys. Rev.* **80**, 268 (1950).

J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena*, Oxford University Press (2002).

G. Parisi, *Statistical Field Theory*, Addison–Wesley (1988).

N. Goldenfeld, *Lectures on Phase Transitions and the Renormalization Group*, Addison–Wesley (1992).

M. Arndt et al., “Wave–Particle Duality of C$`_{60}`$ Molecules,” *Nature* **401**, 680 (1999).

A. D. Cronin, J. Schmiedmayer, and D. E. Pritchard, “Optics and Interferometry with Atoms and Molecules,” *Rev. Mod. Phys.* **81**, 1051 (2009).

Experimental Collaboration, “Observation of Center–of–Mass Interference in Positronium,” *Nature Physics* (2024).

</div>
