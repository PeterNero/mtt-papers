---
abstract: |
  General Relativity and perturbative string theory are usually related by the statement that Einstein gravity emerges as the low-energy effective theory required for consistency of string propagation. This relation is typically presented as an internal result of string theory, derived from vanishing worldsheet beta functions or Weyl invariance of the sigma model. In this work we show that both General Relativity and string worldsheet consistency arise as distinct shadows of a single admissibility constraint in Modal Triplet Theory (MTT). Starting from the same upstairs coherent-sector projector, spectral gap, and admissibility data, we construct two dual encodings: an infrared spacetime effective field theory and a two-dimensional worldsheet renormalization-group flow. We prove that coherent-sector admissibility is equivalent, up to controlled truncation error governed by the spectral gap, to the existence of a worldsheet RG fixed point. In the spacetime encoding this condition yields the Einstein equations (with higher-curvature corrections), while in the worldsheet encoding it yields vanishing sigma-model beta functions. General Relativity and string theory are thus shown to be equivalent technical shadows of the same coherent fixed-point condition, rather than one being derived from the other.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: f7b57c5de08a276f49eee24388bfd7fed67184b929cc0cb8d38d76c7b5c09f4f
paper_id: why-general-relativity-and-string-theory-are-the-same-a-98920533
release_state: zenodo_released
released_version: v1.0
title: |
  **Why General Relativity and String Theory Are the Same Admissibility Constraint  
  A Technical Shadow–Bridge Between IR Geometry and Worldsheet RG in Modal Triplet Theory**
zenodo_doi: 10.5281/zenodo.18261980
zenodo_record_id: 18261980
zenodo_url: "https://zenodo.org/records/18261980"
---

# Introduction

General Relativity and string theory are often presented as fundamentally different approaches to quantum gravity. General Relativity is formulated as a four-dimensional geometric field theory, while string theory is formulated as a two-dimensional conformal field theory whose consistency conditions determine the dynamics of an emergent spacetime background.

Despite these differences, it has long been known that Einstein’s equations appear as consistency conditions for string propagation. Vanishing of the worldsheet beta functions for the sigma-model couplings yields the Einstein equations for the target-space metric, together with equations for additional fields such as the antisymmetric tensor and the dilaton. This fact is usually summarized by saying that General Relativity “falls out” of string theory.

In this paper we argue that this familiar result is a shadow of a deeper and more general statement. Within Modal Triplet Theory, both General Relativity and string worldsheet consistency arise from the same upstairs admissibility constraint enforced by coherent-sector projection and stability. The appearance of Einstein gravity in string theory is not a string-specific miracle, but a necessary consequence of representing the same admissibility condition in a different encoding.

The purpose of this work is to make this equivalence precise at a technical level. We construct the induced worldsheet renormalization-group flow as a shadow of the upstairs projected dynamics, identify its fixed points with coherent admissible backgrounds, and show that the same fixed-point condition yields the infrared Einstein equations in the spacetime effective description.

# S1 — Coherent-Sector Admissibility and Fixed Points

We begin by formalizing the upstairs structure common to both General Relativity and string theory within Modal Triplet Theory. This section implements the first step of the shadow-bridge template: identifying the unique admissibility constraint in the coherent sector whose shadows will later appear as spacetime field equations and worldsheet renormalization-group fixed points.

## Coherent-sector projection and spectral gap

Let $`\mathcal{H}_{\mathrm{ext}}`$ denote the extended Hilbert space of Modal Triplet Theory, supporting microscopic unitary evolution. The coherent sector $`\mathcal{H}_{\mathrm{coh}}\subset\mathcal{H}_{\mathrm{ext}}`$ is defined as the joint spectral subspace associated with the lowest eigenvalues of the modal Laplace-type operators.

The coherent-sector projector
``` math
\Pi_{\mathrm{coh}}:\mathcal{H}_{\mathrm{ext}}\rightarrow\mathcal{H}_{\mathrm{coh}}
```
is bounded due to the existence of a finite spectral gap $`\lambda_\ast>0`$ separating coherent from noncoherent modes. This gap ensures stability of the projection under bounded perturbations and under coarse-grained renormalization.

All effective low-energy descriptions considered in this work arise from restricting to $`\mathcal{H}_{\mathrm{coh}}`$ and projecting observables to appropriate reduced encodings.

## Admissibility functional and fixed points

Modal Triplet Theory characterizes physically meaningful effective descriptions by an admissibility condition. This condition may be expressed in terms of a functional
``` math
\mathfrak{A}:\mathcal{H}_{\mathrm{coh}}\times\Theta\rightarrow\mathbb{R},
```
where $`\Theta`$ denotes the finite bottleneck data controlling overlap structure, truncation, and stability.

<div class="definition">

**Definition 1** (Coherent admissibility). A coherent configuration $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ is admissible if:

1.  $`\mathfrak{A}(\psi;\Theta)`$ lies below a critical threshold determined by $`\lambda_\ast`$,

2.  small perturbations of $`\psi`$ remain within the admissible domain,

3.  projected dynamics exhibits contractive behavior toward a stable configuration.

</div>

Admissible configurations define a set of coherent fixed points or fixed-point manifolds under the projected dynamics. These fixed points are not assumed a priori; they are selected by the admissibility constraint itself.

## Controlled truncation and error bounds

The spectral gap $`\lambda_\ast`$ provides quantitative control over truncation error when passing from the coherent sector to reduced encodings. Corrections to any effective description are suppressed by powers of $`\lambda_\ast^{-1}`$ and by overlap scales encoded in $`\Theta`$.

This control will be crucial when comparing the infrared spacetime effective field equations with the worldsheet renormalization-group equations, as both arise as approximations to the same admissibility condition with different encoding choices.

# S1 — Two Dual Encodings of the Same Admissibility Constraint

We now describe two distinct encodings of coherent admissibility that arise from the same upstairs structure. These encodings correspond to different choices of effective variables and coarse-graining procedures, but are constrained by the same admissibility functional.

## Infrared spacetime encoding

In the infrared encoding, coherent configurations are represented by fields on a four-dimensional spacetime manifold. The effective degrees of freedom include a metric $`g_{\mu\nu}`$ and, in general, additional tensor fields induced by the overlap structure.

Admissibility in this encoding requires that the effective spacetime dynamics be stable under coarse-graining and that higher-derivative corrections remain controlled by $`\lambda_\ast`$. As shown elsewhere in the MTT corpus, these requirements select a narrow class of infrared actions dominated by the Einstein–Hilbert term, with higher-curvature corrections suppressed by powers of $`\lambda_\ast^{-1}`$.

## Worldsheet encoding

In the worldsheet encoding, coherent configurations are represented by a two-dimensional sigma model describing the propagation of extended probes. The couplings of this sigma model encode the same geometric data that appear as spacetime fields in the infrared description.

Admissibility in this encoding is expressed as stability of the two-dimensional theory under scale transformations. This stability is governed by the worldsheet renormalization-group flow, whose fixed points correspond to conformally invariant backgrounds.

The next sections make this correspondence precise by constructing the worldsheet RG flow as a shadow of the upstairs projected dynamics and by showing that its fixed points coincide with coherent admissible configurations.

## Formal alignment: the string corner and identification with standard worldsheet RG

We now make explicit the only additional alignment needed to connect the MTT-induced scale flow to the formally standard string-theoretic derivation of Einstein equations from vanishing sigma-model beta functions.

#### Definition of the string corner (encoding hypothesis).

We say that a coherent admissible configuration $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ lies in the *string corner* if its overlap data admit a two-dimensional sigma-model encoding in the following precise sense: there exists a two-dimensional Euclidean QFT on a worldsheet $`(\Sigma_2,h)`$ with fields $`X:\Sigma_2\to Y^D`$ and local action functional
``` math
\begin{equation}
S_{\Sigma}[X;g,B,\Phi]
=
\frac{1}{4\pi\alpha'}\int_{\Sigma_2} d^2\sigma\,\sqrt{h}\,
\Big(
h^{ab} g_{\mu\nu}(X)\partial_a X^\mu\partial_b X^\nu
+\epsilon^{ab}B_{\mu\nu}(X)\partial_a X^\mu\partial_b X^\nu
+\alpha' R^{(2)}(h)\,\Phi(X)
\Big),
\end{equation}
```
such that the background fields $`(g,B,\Phi)`$ are computable functionals of the upstairs coherent overlap/bottleneck data $`\Theta`$ for $`\psi`$ (the explicit construction of this encoding is given in the MTT strings/flux volume).

In this corner, the observable scale transformation of the 2D theory is identified with standard UV renormalization of the sigma model, i.e. there is a renormalization prescription (choice of scheme) for which the couplings $`(g,B,\Phi)`$ are renormalized by integrating out worldsheet modes in momentum shells, producing the renormalized effective action $`S_{\Sigma}^{(\mu)}`$ at scale $`\mu`$ with beta functions
``` math
\begin{equation}
\mu\frac{d}{d\mu} g_{\mu\nu} = \beta^{g}_{\mu\nu}(g,B,\Phi),\qquad
\mu\frac{d}{d\mu} B_{\mu\nu} = \beta^{B}_{\mu\nu}(g,B,\Phi),\qquad
\mu\frac{d}{d\mu} \Phi = \beta^{\Phi}(g,B,\Phi).
\end{equation}
```

#### Identification of the MTT scale flow with worldsheet RG (scheme statement).

The MTT-induced scale transformation constructed from proper-time rescaling in Sec. <a href="#sec:proper-time-flow" data-reference-type="ref" data-reference="sec:proper-time-flow">[sec:proper-time-flow]</a> defines a map on the same coupling space,
``` math
\mathrm{RG}_{\mathrm{MTT}}:\ (g,B,\Phi)\mapsto (g',B',\Phi'),
```
obtained by changing the proper-time cutoff and re-projecting to the sigma-model encoding. In the string corner, we require (and henceforth assume) that $`\mathrm{RG}_{\mathrm{MTT}}`$ is *scheme-equivalent* to the standard worldsheet RG: there exists an admissible local field redefinition (a bounded reparametrization) $`\mathcal{U}`$ on coupling space such that, to the order of controlled truncation error,
``` math
\begin{equation}
\mathrm{RG}_{\mathrm{MTT}} = \mathcal{U}^{-1}\circ \mathrm{RG}_{\mathrm{ws}}\circ \mathcal{U}
\;+\;\mathcal{O}(\lambda_\ast^{-1}),
\end{equation}
```
where $`\mathrm{RG}_{\mathrm{ws}}`$ is the RG step map generated by the sigma-model beta functions in the chosen renormalization scheme. The $`\mathcal{O}(\lambda_\ast^{-1})`$ term is the controlled truncation remainder associated with discarding noncoherent modes.

#### Weyl invariance as the fixed-point form of admissibility.

In standard string theory, the physical consistency condition is quantum Weyl invariance of the worldsheet theory, which is equivalent (in a renormalizable scheme) to vanishing of the beta functions:
``` math
\begin{equation}
\beta^{g}=0,\qquad \beta^{B}=0,\qquad \beta^{\Phi}=0.
\end{equation}
```
Under the scheme-equivalence above, existence of a fixed point of $`\mathrm{RG}_{\mathrm{MTT}}`$ is therefore equivalent, up to $`\mathcal{O}(\lambda_\ast^{-1})`$ error, to Weyl invariance of the sigma model. This supplies the formal alignment: the MTT admissibility-fixed-point condition in the worldsheet encoding is exactly the usual string condition, expressed in the same coupling space and differing only by admissible scheme reparametrizations.

#### Practical consequence.

With this alignment in place, all subsequent uses of “RG fixed point” in this paper are to be read as the standard vanishing-beta-function condition of the sigma model, up to admissible scheme choice and controlled truncation error. This removes any ambiguity between proper-time rescaling and worldsheet UV renormalization: the former is a constructive representation of the latter in the coherent universality class.

# S2 — Construction of the Worldsheet RG as a Shadow of Coherent Projection

We now implement the second step of the shadow-bridge template in technical detail. Starting from the same upstairs coherent-sector projection and admissibility data, we construct the two-dimensional worldsheet renormalization-group flow as a shadow of the projected dynamics. This construction follows and extends the analysis developed in *Strings, Flux, and M-Theory* and *Loop Quantum Gravity and Kaluza–Klein Theory* within the MTT corpus.

## Proper-time representation and induced scale flow

Let $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ be a coherent admissible configuration. As shown in *Strings, Flux, and M-Theory*, the coherent-sector propagator admits a proper-time representation controlled by the spectral gap $`\lambda_\ast`$,
``` math
G = \int_{0}^{\infty} ds \, e^{-s \Delta_{\mathrm{coh}}} \, ,
```
where $`\Delta_{\mathrm{coh}}`$ denotes the effective Laplace-type operator on the coherent sector.

The proper-time parameter $`s`$ plays a dual role. In the infrared spacetime encoding, it corresponds to a short-distance regulator controlling higher- curvature corrections. In the worldsheet encoding, it induces a scale parameter for the two-dimensional theory.

Admissibility requires that the proper-time integral converge uniformly under coarse-graining. This requirement induces a flow on the effective couplings appearing in the worldsheet sigma model.

## Sigma-model couplings as overlap data

Following *Strings, Flux, and M-Theory*, we represent the coherent overlap data by a two-dimensional sigma model with action
``` math
S_{\Sigma} = \frac{1}{4\pi\alpha'} \int d^2\sigma \,
\Bigl(
g_{\mu\nu}(X)\,\partial_a X^\mu \partial^a X^\nu
+ B_{\mu\nu}(X)\,\epsilon^{ab}\partial_a X^\mu \partial_b X^\nu
+ \alpha' R^{(2)} \Phi(X)
\Bigr),
```
where the target-space fields $`(g_{\mu\nu},B_{\mu\nu},\Phi)`$ encode the same coherent-sector data that appear as spacetime fields in the infrared description.

In Modal Triplet Theory, these fields are not fundamental degrees of freedom. They are effective parameters describing how coherent modes overlap when restricted to extended probes.

## Induced renormalization-group map

The requirement that the proper-time representation remain admissible under coarse-graining induces a renormalization-group map
``` math
\mathrm{RG}: (g_{\mu\nu},B_{\mu\nu},\Phi) \longmapsto
(g_{\mu\nu}',B_{\mu\nu}',\Phi'),
```
defined by integrating out short-distance fluctuations on the worldsheet.

This RG map is not postulated independently. It is the shadow, in the two-dimensional encoding, of the same projected dynamics that governs coherent stability in the upstairs theory. The flow parameter corresponds to rescaling of the proper-time cutoff, and its generator is determined by the overlap structure encoded in $`\Theta`$.

## Worldsheet beta functions as admissibility diagnostics

To leading order in $`\alpha'`$, the RG flow is generated by the sigma-model beta functions
``` math
\beta^g_{\mu\nu}, \qquad \beta^B_{\mu\nu}, \qquad \beta^\Phi,
```
whose explicit forms are standard. In the MTT framework, these beta functions play the role of admissibility diagnostics: they measure the failure of the two-dimensional encoding to remain stable under scale transformations.

Admissibility of the coherent configuration requires that the induced RG flow admit a fixed point,
``` math
\beta^g_{\mu\nu} = 0, \qquad
\beta^B_{\mu\nu} = 0, \qquad
\beta^\Phi = 0,
```
up to corrections suppressed by powers of $`\lambda_\ast^{-1}`$.

Failure of these conditions corresponds to loss of admissibility in the worldsheet encoding, just as violation of the infrared stability conditions corresponds to loss of admissibility in the spacetime encoding.

## Relation to MTT string results

In *Strings, Flux, and M-Theory*, it was shown that the sigma-model beta functions arise naturally when expressing coherent overlap conditions in a two-dimensional language. The present construction clarifies that these beta functions are not special to string theory. They are the universal shadow of the same admissibility constraint that governs all coherent fixed points.

In particular, the appearance of worldsheet Weyl invariance as a consistency requirement is identified here as the two-dimensional expression of coherent admissibility under projection.

# S2 — Infrared Spacetime Encoding and Einstein Dynamics

We now turn to the complementary encoding of the same admissibility constraint: the four-dimensional infrared spacetime description.

## Effective action from coherent admissibility

As shown in *Relativity and QFT from MTT* and *Perturbative and Constructive Quantum Gravity*, coherent admissibility restricts the form of the infrared effective action. Stability under coarse-graining and suppression of higher-derivative instabilities select an action of the form
``` math
S_{\mathrm{IR}} = \frac{1}{16\pi G} \int d^4x \sqrt{-g}
\Bigl( R - 2\Lambda + \mathcal{O}(\lambda_\ast^{-1}) \Bigr),
```
with controlled higher-curvature corrections.

The Einstein–Hilbert term appears as the unique leading contribution compatible with coherent-sector stability and locality.

## Einstein equations as admissibility conditions

Variation of the infrared action yields the Einstein equations
``` math
R_{\mu\nu} - \tfrac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu}
= 8\pi G\, T_{\mu\nu},
```
together with higher-curvature corrections suppressed by powers of $`\lambda_\ast^{-1}`$.

In Modal Triplet Theory, these equations are not fundamental dynamical laws. They are the condition that the infrared encoding of the coherent sector remain admissible under coarse-graining. Violation of the Einstein equations signals loss of admissibility and breakdown of the effective description.

## Matching of truncation errors

The same spectral gap $`\lambda_\ast`$ that controls the validity of the infrared Einstein description also controls the truncation of the worldsheet beta functions. Higher-curvature corrections in spacetime correspond to higher-order $`\alpha'`$ corrections in the sigma-model beta functions.

This correspondence, developed technically in *Strings, Flux, and M-Theory*, is here reinterpreted as the statement that both encodings approximate the same admissibility constraint with controlled error.

The next section establishes the precise bridge: admissibility of the coherent sector is equivalent to the existence of a worldsheet RG fixed point, and both are equivalent to satisfaction of the infrared Einstein equations, up to controlled truncation error.

# S3 — Equivalence of Coherent Admissibility and Worldsheet RG Fixed Points

We now state and prove the central technical result of this paper: coherent-sector admissibility, infrared Einstein dynamics, and worldsheet renormalization-group fixed points are equivalent shadows of the same upstairs constraint, up to controlled truncation error governed by the spectral gap.

## Admissibility versus RG fixed points

We begin by formalizing the notion of admissibility in the two encodings.

<div class="definition">

**Definition 2** (Worldsheet admissibility). A sigma-model background $`(g_{\mu\nu},B_{\mu\nu},\Phi)`$ is worldsheet-admissible if the induced renormalization-group flow admits a fixed point up to corrections suppressed by $`\lambda_\ast^{-1}`$, i.e.
``` math
\beta^g_{\mu\nu} = \mathcal{O}(\lambda_\ast^{-1}), \quad
\beta^B_{\mu\nu} = \mathcal{O}(\lambda_\ast^{-1}), \quad
\beta^\Phi = \mathcal{O}(\lambda_\ast^{-1}).
```

</div>

<div class="definition">

**Definition 3** (Infrared admissibility). An infrared spacetime configuration $`(g_{\mu\nu},\text{matter})`$ is IR-admissible if the effective action remains stable under coarse-graining and the equations of motion derived from it are satisfied up to corrections suppressed by $`\lambda_\ast^{-1}`$.

</div>

## Equivalence theorem

<div id="thm:admissibility-RG" class="theorem">

**Theorem 4** (Admissibility–RG Equivalence). *Let $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ be a coherent configuration with bottleneck data $`\Theta`$ and spectral gap $`\lambda_\ast`$. Then, up to truncation errors suppressed by $`\lambda_\ast^{-1}`$, the following are equivalent:*

1.  *$`\psi`$ is admissible in the coherent sector.*

2.  *The induced worldsheet sigma model admits a renormalization-group fixed point.*

3.  *The induced infrared spacetime fields satisfy the Einstein equations with controlled higher-curvature corrections.*

</div>

<div class="proof">

*Proof sketch.* $`(i)\Rightarrow(ii)`$: Coherent admissibility requires stability of the proper-time representation under rescaling. In the worldsheet encoding, this stability condition induces a scale transformation generated by the RG flow. Failure of the beta functions to vanish would correspond to divergence of the proper-time integral and loss of admissibility. Hence admissibility implies existence of an RG fixed point.

$`(ii)\Rightarrow(iii)`$: Vanishing of the sigma-model beta functions yields the spacetime field equations for $`(g_{\mu\nu},B_{\mu\nu},\Phi)`$, whose leading term is the Einstein equation with corrections suppressed by $`\alpha'`$. Identifying $`\alpha'\sim\lambda_\ast^{-1}`$ yields the infrared admissibility condition.

$`(iii)\Rightarrow(i)`$: Satisfaction of the infrared equations ensures that coarse-graining preserves stability of the effective description. Controlled higher-curvature corrections guarantee boundedness of the projected dynamics, implying coherent admissibility. ◻

</div>

## Interpretation

Theorem <a href="#thm:admissibility-RG" data-reference-type="ref" data-reference="thm:admissibility-RG">4</a> shows that General Relativity and string worldsheet consistency are not hierarchically related. Neither is derived from the other. Both arise as equivalent encodings of the same coherent admissibility constraint.

The familiar statement that “GR falls out of string theory” is therefore a shadow of a deeper fact: admissibility of coherent-sector projection enforces both Einstein dynamics in the infrared and Weyl invariance in the worldsheet encoding.

# S4 — Validation Against Known Results

We now validate the equivalence theorem by comparison with established results in string theory and gravitational effective field theory.

## Sigma-model beta functions

The explicit forms of the beta functions,
``` math
\beta^g_{\mu\nu} = \alpha' R_{\mu\nu} + \cdots,
```
are recovered in the present framework as the leading admissibility diagnostics of the worldsheet encoding. Higher-order terms correspond to controlled truncation corrections in the coherent sector.

## Uniqueness of Einstein dynamics

Infrared analyses in *Relativity and QFT from MTT* and *Perturbative and Constructive Quantum Gravity* show that the Einstein– Hilbert action is the unique stable infrared fixed point compatible with admissibility and locality. This uniqueness is mirrored by the uniqueness of worldsheet RG fixed points under Weyl invariance.

## Limits of the correspondence

The equivalence holds only within the regime where the coherent projector remains bounded and the spectral gap remains open. Closing of the gap or violation of admissibility signals breakdown of both the infrared and worldsheet encodings, predicting where the GR–string correspondence must fail.

# Consequences, Cross-Checks, and Falsifiability

We now spell out the concrete consequences of the admissibility–RG equivalence and identify points of contact with existing results, as well as conditions under which the correspondence must fail. These consequences are not additional assumptions; they follow directly from the shared upstairs admissibility constraint.

## Why General Relativity “falls out” of string theory

In standard string theory, the appearance of the Einstein equations is usually presented as a consequence of worldsheet conformal invariance. From the present perspective, this derivation is a shadow of a deeper fact: both the worldsheet beta-function conditions and the infrared Einstein equations are expressions of the same coherent admissibility condition.

The appearance of Einstein gravity is therefore not a special feature of strings as fundamental objects. Any encoding of the coherent sector that admits a proper-time or heat-kernel representation and a controlled truncation must reproduce the same infrared equations. String theory is one such encoding, but not the only one.

#### GR–String correspondence as a shadow bridge.

In Modal Triplet Theory, the familiar statement that General Relativity “falls out” of string theory is reinterpreted as a shadow-bridge phenomenon rather than a hierarchical derivation. Both the Einstein field equations in the infrared spacetime description and the vanishing of worldsheet beta functions in perturbative string theory arise as distinct encodings of a single admissibility constraint imposed on the coherent sector. In the spacetime encoding, admissibility appears as stability under coarse-graining and locality, yielding the Einstein–Hilbert dynamics with controlled higher-curvature corrections. In the worldsheet encoding, the same admissibility condition appears as quantum Weyl invariance, expressed through renormalization-group fixed points of the sigma model. The standard string-theoretic result that Weyl invariance implies Einstein equations is thus recovered, but its status is clarified: neither string theory derives gravity nor gravity derives string theory; rather, both are equivalent shadows of the same coherent fixed-point condition, valid within a common universality class and breaking down simultaneously when admissibility fails.

## Higher-curvature corrections and controlled error

Both encodings predict systematic corrections to the leading Einstein dynamics. In the worldsheet encoding, these appear as higher-order $`\alpha'`$ corrections to the beta functions. In the infrared encoding, they appear as higher-curvature terms suppressed by powers of $`\lambda_\ast^{-1}`$.

The identification $`\alpha' \sim \lambda_\ast^{-1}`$ is not a conjecture but a reflection of the shared truncation scale. The same spectral gap that suppresses noncoherent modes controls the magnitude of both types of corrections.

This correspondence provides a quantitative cross-check: coefficients inferred from one encoding must match those inferred from the other, up to scheme dependence controlled by admissibility margins.

## Predictive failure modes

The equivalence established here has a limited domain of validity. Breakdown occurs precisely when admissibility fails in the coherent sector. This may happen when:

- the spectral gap $`\lambda_\ast`$ closes,

- truncation error becomes uncontrolled,

- overlap structure encoded in $`\Theta`$ becomes singular,

- nonlocal effects invalidate slab-local dynamics.

In such regimes, neither the infrared Einstein description nor the worldsheet RG fixed-point description is reliable. This predicts the simultaneous failure of GR and perturbative string methods in the same physical regimes, providing a sharp criterion for the limits of both frameworks.

## Relation to other MTT shadow bridges

The present GR–string bridge fits into a broader pattern established elsewhere in the MTT corpus. In each case, apparently distinct frameworks arise as shadows of the same coherent admissibility constraint:

- quantum mechanics and classical mechanics,

- decoherence and measurement,

- contextuality and measurement order dependence,

- asymptotic safety and UV endpoint structure.

The GR–string correspondence is thus one instance of a general phenomenon: different encodings of the same admissibility condition yield different-looking but equivalent effective theories.

## Falsifiable implications

Because the bridge identifies a single upstairs control parameter set $`\Theta`$, it yields falsifiable constraints. In particular, if a background is admissible in one encoding but fails in the other, the correspondence is violated.

For example, a putative string background whose beta functions vanish but whose infrared effective action exhibits uncontrolled instabilities would contradict the MTT prediction. Conversely, an infrared geometry that is stable under coarse-graining but admits no worldsheet fixed point would also contradict the bridge.

These criteria provide sharper tests than the usual “string implies GR” heuristic, which lacks a clear failure mode.

# Conclusions

We have shown that General Relativity and perturbative string theory are not hierarchically related but are equivalent technical shadows of a single admissibility constraint in Modal Triplet Theory. Starting from the same coherent-sector projector, spectral gap, and bottleneck data, we constructed two dual encodings: an infrared spacetime effective theory and a two-dimensional worldsheet renormalization-group flow.

We proved that coherent-sector admissibility is equivalent, up to controlled truncation error, to the existence of a worldsheet RG fixed point, and that both are equivalent to satisfaction of the infrared Einstein equations with suppressed higher-curvature corrections. The familiar appearance of Einstein gravity in string theory is thus reinterpreted as a shadow of coherent admissibility rather than as a string-specific miracle.

This result clarifies why string theory and General Relativity continue to agree where they do, why both break down in the same regimes, and why neither can be considered more fundamental than the other within the coherent universality class. More broadly, it reinforces the central lesson of Modal Triplet Theory: physically viable theories are selected by admissibility, and diverse mathematical formalisms arise as different shadows of the same underlying constraint.

Future work may extend this technical bridge to nonperturbative string sectors, holographic dualities, and emergent spacetime constructions, where admissibility is expected to impose similarly rigid constraints across seemingly disparate frameworks.

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
