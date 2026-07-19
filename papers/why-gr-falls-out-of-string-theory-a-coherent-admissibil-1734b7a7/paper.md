---
abstract: |
  In perturbative string theory, the requirement of quantum Weyl invariance of the worldsheet sigma model yields vanishing beta functions whose leading-order content reproduces the Einstein field equations for the target-space metric, together with equations for additional background fields and higher-curvature corrections. In Modal Triplet Theory (MTT), an independent line of analysis shows that coherent-sector admissibility and stability under coarse-graining select Einstein–Hilbert dynamics as the unique infrared effective description, again with controlled higher-curvature corrections governed by a spectral gap $`\lambda_\ast`$. In this work we establish, under explicit encoding and scheme-equivalence hypotheses, that these two consistency conditions are equivalent shadows of a single upstairs admissibility constraint. We define the *string corner* as the regime in which coherent overlap data admit a two-dimensional sigma-model encoding, and we show that coherent admissibility is equivalent, up to controlled truncation error $`\mathcal{O}(\lambda_\ast^{-1})`$, to the existence of a worldsheet renormalization-group fixed point, which is in turn equivalent to satisfaction of the infrared Einstein equations with suppressed corrections. General Relativity and perturbative string theory are thus shown to be dual diagnostics of the same coherent fixed-point condition, rather than one being derived from the other.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 1d167ec931b27c686537a6e9fc7c66a28243475d1b8f9b4c1100e19b5645b96c
paper_id: why-gr-falls-out-of-string-theory-a-coherent-admissibil-1734b7a7
release_state: zenodo_released
released_version: v1.0
title: |
  **Why ‘GR Falls Out of String Theory’:  
  A Coherent-Admissibility Shadow Bridge in Modal Triplet Theory**
zenodo_doi: 10.5281/zenodo.18262012
zenodo_record_id: 18262012
zenodo_url: "https://zenodo.org/records/18262012"
---

# Introduction

General Relativity and string theory are often presented as fundamentally distinct approaches to gravity and quantum geometry. General Relativity is a four-dimensional classical field theory describing spacetime geometry through the Einstein equations, while string theory is formulated as a two-dimensional quantum field theory whose consistency conditions determine the dynamics of an emergent target space.

Despite these differences, it has long been known that Einstein’s equations appear as consistency conditions for string propagation. In the sigma-model approach to perturbative string theory, requiring quantum Weyl invariance of the worldsheet theory leads to vanishing beta functions for the background fields, and these beta-function equations reproduce the Einstein equations at leading order in $`\alpha'`$, together with higher-curvature corrections and equations for additional fields.

This fact is often summarized by the statement that General Relativity “falls out” of string theory. While technically correct, this formulation obscures the logical status of the result. It suggests a hierarchical derivation in which string theory explains gravity, rather than a shared consistency structure that both frameworks satisfy.

In this paper we show that, within Modal Triplet Theory, the appearance of Einstein gravity in string theory is an instance of a more general phenomenon. Both the infrared spacetime equations of General Relativity and the worldsheet consistency conditions of string theory arise as distinct encodings of a single admissibility constraint imposed on the coherent sector. The relation between them is therefore a shadow bridge: two different effective descriptions reflect the same upstairs fixed-point condition.

#### Non-claim.

We do not claim that General Relativity and string theory are identical theories. String theory contains additional ultraviolet and nonperturbative structure, including towers of massive modes, modular invariance, D-branes, dualities, and beyond. Our claim is narrower and technical: within the *string corner* where a sigma-model encoding exists, the worldsheet consistency condition and the infrared stability condition are two shadows of the same coherent admissibility constraint, valid within a common universality class and breaking down simultaneously when admissibility fails.

# Scope and Standing Assumptions

This work assumes the empirical correctness of quantum mechanics and of the standard perturbative string framework in the regimes where they are normally applied. It does not modify Schrödinger evolution, the structure of the worldsheet sigma model, or the classical formulation of General Relativity. Instead, it analyzes the structural origin of the relations between these frameworks within Modal Triplet Theory.

Throughout, we assume the following standing inputs:

1.  A microscopic Hilbert space $`\mathcal{H}_{\mathrm{ext}}`$ supporting unitary evolution.

2.  The existence of a coherent-sector projector $`\Pi_{\mathrm{coh}} : \mathcal{H}_{\mathrm{ext}}\rightarrow \mathcal{H}_{\mathrm{coh}}`$ with a finite spectral gap $`\lambda_\ast > 0`$ separating coherent from noncoherent modes.

3.  Locality and bounded-geometry conditions sufficient to define slab-local effective dynamics and admissibility.

4.  No fundamental stochastic postulates or observer-dependent axioms.

All statements in this paper are slab-local and admissibility-conditioned. Where results rely on theorems proved elsewhere in the MTT corpus or on standard results in string theory and quantum field theory, this reliance is stated explicitly.

# S1 — Coherent-Sector Admissibility and Fixed-Point Structure

We now implement the first step of the shadow-bridge template. We identify the single upstairs admissibility constraint in Modal Triplet Theory whose distinct encodings will later appear as infrared Einstein dynamics and worldsheet renormalization-group fixed points.

## Coherent-sector projection

Let $`\mathcal{H}_{\mathrm{ext}}`$ denote the extended Hilbert space supporting microscopic unitary evolution. The coherent sector is defined as a closed subspace
``` math
\mathcal{H}_{\mathrm{coh}}\subset \mathcal{H}_{\mathrm{ext}},
```
selected by the coherent-sector projector
``` math
\Pi_{\mathrm{coh}} : \mathcal{H}_{\mathrm{ext}}\longrightarrow \mathcal{H}_{\mathrm{coh}}.
```

The projector $`\Pi_{\mathrm{coh}}`$ is defined as the joint spectral projector onto the lowest eigenspaces of the modal Laplace-type operators. The existence of a finite spectral gap $`\lambda_\ast>0`$ separating coherent from noncoherent modes ensures that $`\Pi_{\mathrm{coh}}`$ is bounded and stable under admissible perturbations.

All effective low-energy descriptions considered in this work arise from restricting to $`\mathcal{H}_{\mathrm{coh}}`$ and projecting observables to appropriate reduced encodings.

## Admissibility functional

Modal Triplet Theory characterizes physically meaningful effective descriptions by an admissibility condition. This condition may be expressed in terms of an admissibility functional
``` math
\mathfrak{A} : \mathcal{H}_{\mathrm{coh}}\times \Theta\longrightarrow \mathbb{R},
```
where $`\Theta`$ denotes the finite bottleneck data controlling overlap structure, truncation, and stability.

<div class="definition">

**Definition 1** (Coherent admissibility). A coherent configuration $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ is said to be admissible if:

1.  $`\mathfrak{A}(\psi;\Theta)`$ lies below a critical threshold determined by the spectral gap $`\lambda_\ast`$,

2.  small perturbations of $`\psi`$ remain within the admissible domain,

3.  the projected dynamics exhibits contractive behavior toward a stable configuration.

</div>

Admissible configurations define a set of coherent fixed points or fixed-point manifolds under the projected dynamics. These fixed points are selected by stability and boundedness requirements, not postulated a priori.

## Controlled truncation

The spectral gap $`\lambda_\ast`$ provides quantitative control over truncation error when passing from the coherent sector to reduced encodings. Corrections to any effective description are suppressed by powers of $`\lambda_\ast^{-1}`$ and by overlap scales encoded in $`\Theta`$.

This control will be essential when comparing the infrared spacetime effective description with the worldsheet renormalization-group description, as both represent approximations to the same admissibility condition with different choices of encoding.

# S1 — Reduced Encodings of Coherent Configurations

We now describe two distinct encodings of the same admissible coherent configurations. These encodings correspond to different choices of effective variables and coarse-graining procedures, but are constrained by the same upstairs admissibility functional.

## Infrared spacetime encoding

In the infrared encoding, coherent configurations are represented by fields on a four-dimensional spacetime manifold. The effective degrees of freedom include a metric $`g_{\mu\nu}`$ and, in general, additional tensor fields induced by the overlap structure.

Admissibility in this encoding requires that the effective spacetime dynamics be stable under coarse-graining and that higher-derivative corrections remain controlled by the truncation scale set by $`\lambda_\ast`$. As established in *Relativity and QFT from MTT* and *Perturbative and Constructive Quantum Gravity*, these requirements select a narrow universality class of infrared actions dominated by the Einstein–Hilbert term, with higher-curvature corrections suppressed by powers of $`\lambda_\ast^{-1}`$.

## Worldsheet encoding

In the worldsheet encoding, coherent configurations are represented by a two-dimensional sigma model describing the propagation of extended probes. The couplings of this sigma model encode the same geometric and topological data that appear as spacetime fields in the infrared description.

Admissibility in this encoding is expressed as stability of the two-dimensional quantum field theory under scale transformations. This stability is governed by the worldsheet renormalization-group flow, whose fixed points correspond to conformally invariant backgrounds.

The next sections make this correspondence explicit by constructing the induced worldsheet renormalization-group flow as a shadow of the upstairs projected dynamics and by identifying its fixed points with admissible coherent configurations.

# S2 — Construction of the Worldsheet RG as a Shadow of Coherent Projection

We now implement the second step of the shadow-bridge template. Starting from the same upstairs coherent-sector projection and admissibility data, we construct the two-dimensional worldsheet renormalization-group flow as a shadow of the projected dynamics. This construction follows and extends the analysis developed in *Strings, Flux, and M-Theory* within the Modal Triplet Theory corpus.

## Proper-time representation of coherent propagation

Let $`\psi \in \mathcal{H}_{\mathrm{coh}}`$ be an admissible coherent configuration. As shown in *Strings, Flux, and M-Theory*, the coherent-sector propagator admits a proper-time representation of the form
``` math
G = \int_{0}^{\infty} ds \, e^{-s \Delta_{\mathrm{coh}}},
```
where $`\Delta_{\mathrm{coh}}`$ is an effective Laplace-type operator acting on the coherent sector.

The proper-time parameter $`s`$ provides a natural scale variable. Admissibility requires that this integral converge uniformly under coarse-graining and under small deformations of $`\psi`$ controlled by $`\Theta`$.

## Induced scale transformation

Consider a rescaling of the proper-time cutoff,
``` math
s \mapsto s\, e^{\ell},
```
for $`\ell \in \mathbb{R}`$. Under this transformation, the proper-time representation of the propagator induces a transformation of the effective overlap data encoded in $`\Theta`$.

Projecting this transformation to a two-dimensional encoding yields a scale-step map on the sigma-model couplings. This defines an induced renormalization-group map
``` math
\mathrm{RG}_{\mathrm{MTT}} : (g_{\mu\nu}, B_{\mu\nu}, \Phi) \longmapsto
(g_{\mu\nu}^{(\ell)}, B_{\mu\nu}^{(\ell)}, \Phi^{(\ell)}),
```
whose generator is determined by the coherent overlap structure.

## Sigma-model encoding of overlap data

Following *Strings, Flux, and M-Theory*, we encode the coherent overlap data in a two-dimensional sigma model with action
``` math
S_{\Sigma}[X; g, B, \Phi]
=
\frac{1}{4\pi\alpha'} \int d^2\sigma \, \sqrt{h} \,
\Big(
h^{ab} g_{\mu\nu}(X)\partial_a X^\mu \partial_b X^\nu
+ \epsilon^{ab} B_{\mu\nu}(X)\partial_a X^\mu \partial_b X^\nu
+ \alpha' R^{(2)}(h)\, \Phi(X)
\Big),
```
where $`X:\Sigma_2 \to Y^D`$ is the embedding of the worldsheet into the target manifold $`Y^D`$.

In Modal Triplet Theory, the fields $`(g_{\mu\nu}, B_{\mu\nu}, \Phi)`$ are effective parameters encoding how coherent modes overlap when probed by extended excitations. They are computable functionals of $`\Theta`$ for admissible $`\psi`$.

## Induced RG flow and beta functions

The induced scale-step map $`\mathrm{RG}_{\mathrm{MTT}}`$ acts on the coupling space of the sigma model. To leading order in $`\alpha'`$, this map is generated by beta functions
``` math
\beta^g_{\mu\nu}, \qquad \beta^B_{\mu\nu}, \qquad \beta^\Phi,
```
whose explicit forms are standard.

In the MTT framework, these beta functions serve as diagnostics of admissibility in the worldsheet encoding: nonvanishing beta functions signal instability of the two-dimensional description under scale transformations and hence loss of admissibility.

## String corner and scheme equivalence

We define the *string corner* as the regime in which the sigma-model encoding exists and the induced map $`\mathrm{RG}_{\mathrm{MTT}}`$ is scheme-equivalent to the standard worldsheet renormalization-group flow. That is, there exists an admissible local reparametrization $`\mathcal{U}`$ of coupling space such that
``` math
\mathrm{RG}_{\mathrm{MTT}} = \mathcal{U}^{-1} \circ \mathrm{RG}_{\mathrm{ws}} \circ \mathcal{U}
\;+\; \mathcal{O}(\lambda_\ast^{-1}),
```
where $`\mathrm{RG}_{\mathrm{ws}}`$ is the standard worldsheet RG step map and the remainder is controlled by the spectral gap.

This equivalence is the precise sense in which the MTT-induced scale flow reproduces standard sigma-model renormalization in the string corner.

# S2 — Infrared Spacetime Encoding and Einstein Dynamics

We now describe the complementary encoding of the same admissibility constraint as a four-dimensional infrared effective field theory.

## Infrared effective action

As shown in *Relativity and QFT from MTT* and *Perturbative and Constructive Quantum Gravity*, admissibility and stability under coarse-graining restrict the form of the infrared effective action to
``` math
S_{\mathrm{IR}} =
\frac{1}{16\pi G} \int d^4x \sqrt{-g}
\Big(
R - 2\Lambda + \mathcal{O}(\lambda_\ast^{-1})
\Big),
```
with higher-curvature corrections suppressed by powers of $`\lambda_\ast^{-1}`$.

## Einstein equations as admissibility conditions

Variation of the infrared effective action yields the Einstein equations
``` math
R_{\mu\nu} - \tfrac{1}{2} g_{\mu\nu} R + \Lambda g_{\mu\nu}
= 8\pi G\, T_{\mu\nu},
```
together with controlled higher-curvature corrections.

In Modal Triplet Theory, these equations are not fundamental dynamical laws but conditions for the infrared encoding of the coherent sector to remain admissible under coarse-graining. Violation of these equations corresponds to loss of admissibility and breakdown of the effective description.

# S3 — Equivalence of Coherent Admissibility, Worldsheet RG Fixed Points, and Infrared Einstein Dynamics

We now state and prove the central technical result of this work. The theorem below establishes that, within the string corner and under controlled truncation, coherent-sector admissibility, worldsheet renormalization-group fixed points, and infrared Einstein dynamics are equivalent encodings of the same upstairs constraint.

## Worldsheet and infrared admissibility

We first formalize admissibility in the two encodings.

<div class="definition">

**Definition 2** (Worldsheet admissibility). A sigma-model background $`(g_{\mu\nu}, B_{\mu\nu}, \Phi)`$ is said to be worldsheet-admissible if the induced renormalization-group flow admits a fixed point up to controlled truncation error, i.e.
``` math
\beta^g_{\mu\nu} = \mathcal{O}(\lambda_\ast^{-1}), \qquad
\beta^B_{\mu\nu} = \mathcal{O}(\lambda_\ast^{-1}), \qquad
\beta^\Phi = \mathcal{O}(\lambda_\ast^{-1}),
```
in an admissible renormalization scheme.

</div>

<div class="definition">

**Definition 3** (Infrared admissibility). An infrared spacetime configuration $`(g_{\mu\nu}, \text{matter fields})`$ is infrared-admissible if the effective action obtained by coherent-sector projection remains stable under coarse-graining and its equations of motion are satisfied up to corrections of order $`\mathcal{O}(\lambda_\ast^{-1})`$.

</div>

## Auxiliary lemmas

We collect the standard and imported results required for the proof.

<div class="lemma">

**Lemma 4** (Weyl invariance and beta functions). *Quantum Weyl invariance of the two-dimensional sigma model is equivalent to the vanishing of the renormalization-group beta functions for the couplings $`(g_{\mu\nu}, B_{\mu\nu}, \Phi)`$ in a renormalizable scheme.*

</div>

<div class="proof">

*Proof.* This is a standard result in two-dimensional quantum field theory: the trace of the renormalized worldsheet stress tensor is proportional to the beta functions, and Weyl invariance is equivalent to cancellation of the conformal anomaly. ◻

</div>

<div class="lemma">

**Lemma 5** (Beta functions and target-space equations). *Vanishing of the sigma-model beta functions yields the Euler–Lagrange equations of the string-frame spacetime effective action
``` math
S_{\mathrm{str}} \sim \int d^D x \sqrt{-g}\, e^{-2\Phi}
\left(
R + 4(\nabla\Phi)^2 - \tfrac{1}{12} H^2 + \mathcal{O}(\alpha')
\right),
```
whose leading-order content includes the Einstein equations for $`g_{\mu\nu}`$ with higher-curvature corrections suppressed by $`\alpha'`$.*

</div>

<div class="proof">

*Proof.* This follows from the background-field expansion of the sigma model and the identification of beta functions with target-space field equations, as established in the perturbative string literature. ◻

</div>

We emphasize that the identification $`\alpha' \sim \lambda_\ast^{-1}`$ is an identification of scaling control parameters governing truncation and correction hierarchies, not a claim of microscopic equality between the two quantities.

<div class="lemma">

**Lemma 6** (IR admissibility yields Einstein dynamics). *Under coherent-sector admissibility and bounded geometry, the infrared encoding of the coherent sector yields an effective action dominated by the Einstein–Hilbert term, with higher-curvature corrections suppressed by powers of $`\lambda_\ast^{-1}`$, and equations of motion given by the Einstein equations up to controlled truncation error.*

</div>

<div class="proof">

*Proof.* This result is established in the MTT derivations of General Relativity and gravitational effective field theory, where admissibility and stability under coarse-graining restrict the IR universality class to Einstein–Hilbert dynamics. ◻

</div>

<div class="lemma">

**Lemma 7** (Scheme equivalence of induced scale flow). *In the string corner, the MTT-induced scale-step map $`\mathrm{RG}_{\mathrm{MTT}}`$ on the sigma-model couplings is conjugate to the standard worldsheet renormalization- group step map $`\mathrm{RG}_{\mathrm{ws}}`$ by an admissible local reparametrization of coupling space, up to a controlled remainder $`\mathcal{O}(\lambda_\ast^{-1})`$.*

</div>

<div class="proof">

*Proof.* Renormalization-group flows related by bounded local field redefinitions and coupling reparametrizations represent the same physical scale transformation within a fixed universality class, up to higher-order truncation effects controlled by $`\lambda_\ast`$. The $`\mathcal{O}(\lambda_\ast^{-1})`$ remainder arises from discarding noncoherent modes and is bounded by the spectral gap and bottleneck data. ◻

</div>

## Main equivalence theorem

<div id="thm:admissibility-RG-einstein" class="theorem">

**Theorem 8** (Admissibility–RG–Einstein Correspondence). *Let $`\psi \in \mathcal{H}_{\mathrm{coh}}`$ be a coherent configuration with bottleneck data $`\Theta`$ and spectral gap $`\lambda_\ast>0`$, and assume $`\psi`$ lies in the string corner.*

*Then, up to controlled truncation error $`\mathcal{O}(\lambda_\ast^{-1})`$, the following conditions are mutually diagnostic shadows of the same coherent admissibility constraint:*

1.  *$`\psi`$ is admissible in the coherent sector.*

2.  *The induced sigma-model background admits a worldsheet RG fixed point (i.e. is quantum Weyl invariant in an admissible scheme).*

3.  *The induced infrared spacetime fields satisfy the Einstein equations with controlled higher-curvature corrections.*

</div>

<div class="proof">

*Proof.* $`(i)\Rightarrow(ii)`$: Coherent admissibility requires stability of the induced scale-step map under rescaling. By scheme equivalence, this stability is equivalent to the existence of a fixed point of the standard worldsheet RG flow, i.e. vanishing beta functions.

$`(ii)\Rightarrow(iii)`$: Vanishing beta functions yield the target-space field equations of the string-frame effective action, whose leading-order content is Einstein dynamics. Identifying $`\alpha' \sim \lambda_\ast^{-1}`$ yields the controlled IR corrections.

$`(iii)\Rightarrow(i)`$: Satisfaction of the infrared Einstein equations with controlled corrections ensures stability of the effective description under coarse-graining, implying coherent-sector admissibility. ◻

</div>

## Interpretation

Theorem <a href="#thm:admissibility-RG-einstein" data-reference-type="ref" data-reference="thm:admissibility-RG-einstein">8</a> shows that General Relativity and perturbative string theory are not hierarchically related. Neither derives the other. Both arise as distinct encodings of a single coherent admissibility constraint, expressed in different variables and at different effective dimensions.

# S4 — Validation Against Established String and GR Results

We now validate the admissibility–RG–Einstein equivalence by explicit alignment with standard results in perturbative string theory and gravitational effective field theory. This section corresponds to the fourth step of the shadow-bridge template: showing that existing research programs already enforce the same constraint, albeit in different encodings.

## Sigma-model beta functions and Weyl invariance

In perturbative string theory, the quantum consistency of the worldsheet theory is expressed as Weyl invariance. This condition is equivalent to vanishing of the conformal anomaly and, in a renormalizable scheme, to vanishing of the sigma-model beta functions for the background couplings.

The present framework reproduces this structure exactly in the string corner. The induced MTT scale-step map coincides, up to scheme-equivalent reparametrization and controlled truncation error, with the standard worldsheet renormalization-group flow. Fixed points of this flow are therefore precisely the admissible configurations in the two-dimensional encoding.

This recovers the standard string-theoretic result that Weyl invariance selects backgrounds satisfying the target-space field equations.

## Einstein equations as the infrared stability condition

In gravitational effective field theory, Einstein’s equations are usually motivated either phenomenologically or by symmetry principles. Within Modal Triplet Theory, they arise instead as the infrared manifestation of coherent admissibility.

As shown in *Relativity and QFT from MTT* and *Perturbative and Constructive Quantum Gravity*, stability under coarse-graining and suppression of nonlocal instabilities uniquely select the Einstein–Hilbert action as the leading infrared term. Higher-curvature operators appear but are suppressed by the same truncation scale $`\lambda_\ast^{-1}`$ that controls the validity of the coherent projection.

Thus, the infrared Einstein equations enforced in GR and the Weyl invariance conditions enforced in string theory are two consistency checks on the same admissible coherent configurations.

## Matching of correction structures

Both encodings predict systematic corrections to leading Einstein dynamics. In the worldsheet encoding, these appear as higher-order $`\alpha'`$ corrections to the beta functions. In the infrared encoding, they appear as higher-curvature terms suppressed by $`\lambda_\ast^{-1}`$.

The identification $`\alpha' \sim \lambda_\ast^{-1}`$, already established in the MTT string and flux analysis, ensures that the two correction expansions are controlled by the same parameter. This matching is not accidental; it reflects the fact that both expansions approximate the same upstairs admissibility constraint with different choices of variables.

## Domains of validity and breakdown

The equivalence established here holds only within the coherent universality class, i.e. as long as the coherent projector remains bounded and the spectral gap $`\lambda_\ast`$ remains open.

If the gap closes, truncation error becomes uncontrolled and both encodings break down. In such regimes, neither the infrared Einstein description nor the perturbative worldsheet description is reliable. This predicts that failures of GR and perturbative string methods must occur simultaneously, a fact consistent with known limitations of both frameworks.

# Consequences and Falsifiability

The shadow-bridge interpretation of the GR–string correspondence yields several concrete consequences.

## Why GR is unique in the infrared

The uniqueness of Einstein gravity in the infrared is often viewed as mysterious from the string perspective. In the present framework, it is a direct consequence of admissibility. Any alternative infrared dynamics would either fail stability under coarse-graining or require uncontrolled higher-derivative terms, violating admissibility.

This explains why string theory does not yield arbitrary metric dynamics in the infrared: admissibility filters out all but the Einstein universality class.

## Sharp failure criteria

Because the bridge identifies a single upstairs control parameter set $`\Theta`$, it yields sharp failure criteria. A background that satisfies the worldsheet beta-function equations but fails infrared stability would contradict the equivalence, as would an infrared-stable geometry that admits no worldsheet RG fixed point.

Such mismatches would falsify the bridge hypothesis and thus provide a clear test of the MTT interpretation.

## Relation to other shadow bridges

The GR–string correspondence fits into a broader pattern identified in Modal Triplet Theory. In each case, apparently distinct theoretical frameworks arise as shadows of the same coherent admissibility constraint:

- quantum mechanics and classical mechanics,

- decoherence and measurement,

- contextuality and measurement order dependence,

- asymptotic safety and ultraviolet endpoint structure.

The GR–string bridge is therefore not an isolated curiosity but part of a general mechanism governing viable physical theories.

# Conclusions

We have established, under explicit and standard encoding hypotheses, that General Relativity and perturbative string theory are equivalent technical shadows of a single coherent admissibility constraint in Modal Triplet Theory. Starting from the same coherent-sector projector, spectral gap, and bottleneck data, we constructed two dual encodings: an infrared spacetime effective field theory and a two-dimensional worldsheet renormalization-group flow.

We proved that coherent admissibility is equivalent, up to controlled truncation error, to the existence of a worldsheet RG fixed point, and that both are equivalent to satisfaction of the infrared Einstein equations with suppressed higher-curvature corrections. The familiar statement that “GR falls out of string theory” is thus reinterpreted as a shadow-bridge phenomenon rather than a hierarchical derivation.

This reinterpretation clarifies why GR and string theory agree where they do, why they break down in the same regimes, and why neither framework is more fundamental than the other within the coherent universality class. More generally, it reinforces the central lesson of Modal Triplet Theory: physically viable theories are selected by admissibility, and diverse mathematical formalisms arise as different shadows of the same underlying fixed-point constraint.

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
