---
abstract: |
  Modal Triplet Theory (MTT) selects physically viable effective descriptions through a coherent-sector admissibility constraint. A bounded projection with a finite spectral gap $`\lambda_\ast>0`$ and controlled truncation defines a coherent sector whose admissible configurations form a stability-selected fixed-point structure, referred to as the coherent spine. Effective physical laws arise only within this admissible sector, and their breakdown coincides with loss of admissibility.

  Previous work established that, within a string corner where a two-dimensional sigma-model encoding exists, perturbative string theory and infrared General Relativity arise as distinct but equivalent shadows of the same coherent admissibility constraint. In this paper we extend this correspondence by identifying a third encoding: functional renormalization-group asymptotic safety.

  Under explicit assumptions of controlled encoding and scheme conjugacy, we prove that coherent-spine fixed points, worldsheet renormalization-group fixed points, and functional renormalization-group ultraviolet fixed points are equivalent diagnostics of a single upstairs admissibility condition, up to controlled truncation error of order $`O(\lambda_\ast^{-1})`$. This establishes a triple-corner equivalence between perturbative string theory, asymptotic safety, and coherent-sector fixed points, and yields cross-framework predictions including matching spectra of leading irrelevant operators and correlated breakdown surfaces.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 0efc533c2bdce93117368279fefe7552bd914782518963086d6e48d7d06c24c3
paper_id: a-third-corner-shadow-bridge-asymptotic-safety-the-stri-37bbd5a2
release_state: zenodo_released
released_version: v1.0
title: |
  A Third-Corner Shadow Bridge:  
  Asymptotic Safety, the String Corner, and the Coherent Spine in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.18262056
zenodo_record_id: 18262056
zenodo_url: "https://zenodo.org/records/18262056"
---

# Motivation and Context

Quantum gravity research has produced several frameworks in which physical viability is enforced through fixed-point structure rather than through explicit microscopic dynamics. Perturbative string theory enforces consistency through quantum Weyl invariance of a two-dimensional worldsheet theory. Asymptotic safety enforces predictivity through the existence of a nontrivial ultraviolet fixed point of the functional renormalization-group flow. Modal Triplet Theory enforces viability through admissibility of a coherent sector selected by bounded projection and controlled truncation.

These frameworks are usually treated as mutually exclusive or competing ultraviolet completions. However, they share a structural feature: physical descriptions are selected by stability under coarse-graining, and break down precisely when this stability fails.

Within Modal Triplet Theory, admissibility is not a phenomenological criterion but a structural constraint imposed by the requirement that projection-based effective descriptions remain well-defined. The coherent sector is selected by spectral gaps, bounded projectors, and controlled truncation, and effective laws arise only within this sector.

Earlier work demonstrated that, within a string corner where a sigma-model encoding of coherent overlap data exists, the condition of worldsheet Weyl invariance and the infrared Einstein equations are equivalent shadows of the same coherent admissibility constraint. This result reframed the statement that “General Relativity falls out of string theory” as a shadow-bridge phenomenon rather than a hierarchical derivation.

The goal of the present paper is to demonstrate that asymptotic safety constitutes a third such shadow. We show that, within a common admissible universality class, the ultraviolet fixed point of the functional renormalization-group flow, the worldsheet renormalization- group fixed point of perturbative string theory, and the coherent-spine fixed point of Modal Triplet Theory are equivalent encodings of the same upstairs admissibility condition.

# Standing Assumptions and Scope

All results in this paper are slab-local and admissibility-conditioned. No claim is made that any of the encodings discussed are globally valid or exhaustive. The equivalences established here hold only within the overlap of their respective domains of validity.

We do not modify the microscopic unitary dynamics assumed in Modal Triplet Theory, the standard formulation of the worldsheet sigma model in perturbative string theory, or the functional renormalization-group formalism used in asymptotic safety. Where standard results from these frameworks are invoked, they are stated explicitly.

<div class="assumption">

**Assumption 1** (Coherent Sector and Spectral Gap). There exists an extended Hilbert space $`\mathcal{H}_{\mathrm{ext}}`$ supporting unitary microscopic evolution. There exists a closed coherent subspace $`\mathcal{H}_{\mathrm{coh}}\subset\mathcal{H}_{\mathrm{ext}}`$ selected by a bounded projector
``` math
\Pi_{\mathrm{coh}}:\mathcal{H}_{\mathrm{ext}}\rightarrow\mathcal{H}_{\mathrm{coh}},
```
constructed from joint Riesz projectors associated with a uniform spectral gap $`\lambda_\ast>0`$ separating coherent from noncoherent modes.

</div>

<div class="assumption">

**Assumption 2** (Controlled Truncation). There exists a slab-local admissible domain on which truncation errors induced by projection and by any reduced encoding are uniformly bounded by
``` math
\|\mathcal{E}\|\le C\,\lambda_\ast^{-1},
```
where $`\mathcal{E}`$ denotes the cumulative remainder and $`C`$ is bounded on the slab.

</div>

<div class="assumption">

**Assumption 3** (String Corner). Within the admissible slab, the coherent overlap data admit a two-dimensional sigma-model encoding whose induced scale-step map is scheme-conjugate to the standard worldsheet renormalization-group flow up to a controlled remainder of order $`O(\lambda_\ast^{-1})`$.

</div>

<div class="assumption">

**Assumption 4** (Asymptotic-Safety Corner). Within the admissible slab, the gravitational effective action admits a functional renormalization-group description with a nontrivial ultraviolet fixed point possessing finitely many relevant directions.

</div>

<div class="remark">

*Remark 5*. No assumption is made that the string corner or asymptotic-safety corner exhaust the space of admissible encodings. The results apply only where the respective encodings exist and are controlled.

</div>

# Projected Dynamics and Admissible Basins

<div class="definition">

**Definition 6** (Projected Step Map). Let $`\Phi_\tau`$ denote the invertible microscopic evolution map on $`\mathcal{H}_{\mathrm{ext}}`$. The coherent projected step map is defined by
``` math
T:=\Pi_{\mathrm{coh}}\circ\Phi_\tau .
```

</div>

<div class="definition">

**Definition 7** (Admissible Basin). A subset $`B\subset\mathcal{H}_{\mathrm{coh}}`$ is an admissible basin if it is forward-invariant under $`T`$ up to $`O(\lambda_\ast^{-1})`$ and if there exist constants $`0<\kappa<1`$ and $`C_B<\infty`$ such that
``` math
\|T(\psi_1)-T(\psi_2)\|
\le
\kappa\,\|\psi_1-\psi_2\| + C_B\,\lambda_\ast^{-1}
```
for all $`\psi_1,\psi_2\in B`$.

</div>

<div class="lemma">

**Lemma 8** (Existence of Approximate Fixed Points). *Every admissible basin contains at least one approximate fixed point $`\psi_\infty\in\overline{B}`$ satisfying
``` math
\|T(\psi_\infty)-\psi_\infty\|\le C\,\lambda_\ast^{-1},
```
with $`C`$ bounded on the slab.*

</div>

<div class="proof">

*Proof.* Iterating the contractive inequality yields convergence of the sequence $`\psi_{n+1}=T(\psi_n)`$ up to an error floor of order $`O(\lambda_\ast^{-1})`$ by standard Banach fixed-point arguments adapted to maps with controlled remainder. ◻

</div>

# The Coherent Spine as an Upstairs Fixed-Point Structure

We now formalize the notion of the coherent spine as it appears in Modal Triplet Theory. The coherent spine is not an effective object defined in a particular encoding; it is an upstairs structure selected by admissibility and stability of the projected dynamics.

<div class="definition">

**Definition 9** (Admissible Configuration). A coherent configuration $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ is admissible if it lies in an admissible basin and if the linearization of the projected step map $`T`$ about $`\psi`$ is bounded uniformly on the slab, up to controlled remainder of order $`O(\lambda_\ast^{-1})`$.

</div>

<div class="definition">

**Definition 10** (Coherent Spine). The coherent spine $`\mathfrak{S}`$ is defined as the set of all admissible configurations $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ that are approximate fixed points of $`T`$, i.e. satisfy
``` math
\|T(\psi)-\psi\|\le C_\psi\,\lambda_\ast^{-1},
```
with $`C_\psi`$ bounded on the slab, and whose admissible basin contains no directions of uncontrolled instability.

</div>

<div class="remark">

*Remark 11*. The coherent spine may consist of isolated fixed points or fixed-point manifolds, depending on residual symmetries and degeneracies of the admissibility condition. No assumption is made that the spine is unique or discrete.

</div>

<div class="lemma">

**Lemma 12** (Persistence of the Coherent Spine). *Let $`\psi\in\mathfrak{S}`$ and let $`\delta\psi`$ be an admissible perturbation satisfying $`\|\delta\psi\|=O(\lambda_\ast^{-1})`$. Then $`\psi+\delta\psi`$ remains within the same admissible basin and converges under iteration of $`T`$ back to $`\mathfrak{S}`$ up to $`O(\lambda_\ast^{-1})`$.*

</div>

<div class="proof">

*Proof.* By admissibility, the linearization of $`T`$ about $`\psi`$ is bounded with spectral radius strictly less than unity up to a controlled remainder. The contractive inequality defining the admissible basin therefore persists under perturbations of size $`O(\lambda_\ast^{-1})`$, and the remainder terms do not accumulate beyond the truncation scale. Iteration of $`T`$ thus returns $`\psi+\delta\psi`$ to the fixed-point neighborhood defined by $`\mathfrak{S}`$. ◻

</div>

<div class="remark">

*Remark 13*. This persistence property is the upstairs analogue of stability of fixed points in renormalization-group flows. It is an encoding-independent statement.

</div>

# Encoding I: Worldsheet Sigma-Model Description

We now recall the worldsheet encoding of coherent overlap data that defines the string corner. This encoding associates to an admissible coherent configuration a two-dimensional sigma model whose couplings encode the overlap structure of coherent modes.

<div class="definition">

**Definition 14** (Sigma-Model Encoding). Let $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ be admissible and lie within the string corner. The worldsheet encoding associates to $`\psi`$ a two-dimensional sigma model with coupling vector $`\mathbf{g}(\psi)`$, defined on a worldsheet $`\Sigma`$ with action
``` math
S_\Sigma[X;\mathbf{g}]
=
\frac{1}{4\pi\alpha'}
\int_\Sigma d^2\sigma\,\sqrt{h}\,
\left(
h^{ab}g_{\mu\nu}(X)\partial_a X^\mu\partial_b X^\nu
+
\epsilon^{ab}B_{\mu\nu}(X)\partial_a X^\mu\partial_b X^\nu
+
\alpha' R^{(2)}(h)\,\Phi(X)
\right),
```
where $`g_{\mu\nu}`$, $`B_{\mu\nu}`$, and $`\Phi`$ are effective fields determined by the coherent overlap data.

</div>

<div class="remark">

*Remark 15*. Within Modal Triplet Theory, the sigma-model fields are not fundamental but are effective parameters encoding overlap structure of coherent modes. Their admissibility is inherited from the admissibility of the underlying coherent configuration.

</div>

<div class="definition">

**Definition 16** (Worldsheet Renormalization-Group Flow). The worldsheet renormalization-group flow acts on the coupling vector $`\mathbf{g}`$ according to beta functions
``` math
\frac{d\mathbf{g}}{d\ln\mu}=\boldsymbol{\beta}(\mathbf{g}),
```
defined in a chosen renormalization scheme.

</div>

<div class="definition">

**Definition 17** (Worldsheet Fixed Point). A coupling vector $`\mathbf{g}_\ast`$ is a worldsheet fixed point if
``` math
\boldsymbol{\beta}(\mathbf{g}_\ast)=O(\lambda_\ast^{-1})
```
uniformly on the slab.

</div>

<div class="lemma">

**Lemma 18** (Weyl Invariance Criterion). *A worldsheet fixed point is equivalent to quantum Weyl invariance of the sigma model up to controlled truncation error.*

</div>

<div class="proof">

*Proof.* In two-dimensional quantum field theory, the trace of the renormalized worldsheet stress tensor is proportional to the beta functions of the couplings. Vanishing of the trace anomaly is therefore equivalent to vanishing beta functions, modulo scheme-dependent local counterterms. The controlled truncation error contributes corrections of order $`O(\lambda_\ast^{-1})`$, which are admissible within the slab. ◻

</div>

<div class="remark">

*Remark 19*. This establishes worldsheet Weyl invariance as a diagnostic of coherent admissibility in the string corner.

</div>

# Encoding II: Functional Renormalization-Group Description

We now turn to the functional renormalization-group encoding of the same admissible coherent configurations. This encoding underlies the asymptotic-safety approach to quantum gravity.

<div class="definition">

**Definition 20** (Effective Average Action). Let $`\Gamma_k[\varphi]`$ denote the effective average action at scale $`k`$, obtained by integrating out fluctuations with momenta $`p^2\gtrsim k^2`$ while suppressing infrared modes via a regulator $`R_k`$.

</div>

<div class="definition">

**Definition 21** (Functional Renormalization-Group Flow). The functional renormalization-group flow of $`\Gamma_k`$ is governed by the Wetterich equation
``` math
\partial_t\Gamma_k
=
\frac{1}{2}\operatorname{Tr}
\left[
\left(\Gamma_k^{(2)}+R_k\right)^{-1}\partial_t R_k
\right],
\qquad
t=\ln(k/k_0),
```
where $`\Gamma_k^{(2)}`$ denotes the second functional derivative of $`\Gamma_k`$ with respect to the fields.

</div>

<div class="assumption">

**Assumption 22** (Admissible Truncation Family). There exists a truncation family $`\Gamma_k^{(N)}`$ parameterized by a finite-dimensional coupling vector $`\mathbf{u}^{(N)}(k)`$ such that the exact beta functions are approximated by $`\boldsymbol{\beta}^{(N)}(\mathbf{u}^{(N)})`$ with controlled error
``` math
\|\boldsymbol{\beta}-\boldsymbol{\beta}^{(N)}\|\le C_N\,\lambda_\ast^{-1}
```
uniformly on the slab.

</div>

<div class="definition">

**Definition 23** (FRG Ultraviolet Fixed Point). A coupling vector $`\mathbf{u}^{(N)}_\ast`$ is a functional renormalization-group ultraviolet fixed point if
``` math
\boldsymbol{\beta}^{(N)}(\mathbf{u}^{(N)}_\ast)=O(\lambda_\ast^{-1})
```
and the linearized flow about $`\mathbf{u}^{(N)}_\ast`$ possesses only finitely many relevant directions.

</div>

<div class="remark">

*Remark 24*. The finiteness of relevant directions is essential for predictivity and corresponds, in the MTT interpretation, to bounded instability directions within an admissible basin.

</div>

<div class="lemma">

**Lemma 25** (Stability Under FRG Flow). *If $`\mathbf{u}^{(N)}_\ast`$ is an FRG ultraviolet fixed point, then perturbations along irrelevant directions decay under the renormalization-group flow up to controlled remainder $`O(\lambda_\ast^{-1})`$.*

</div>

<div class="proof">

*Proof.* This follows from linearization of the beta functions about $`\mathbf{u}^{(N)}_\ast`$ and the assumption that all but finitely many eigenvalues of the stability matrix have negative real parts, with corrections bounded by the truncation error. ◻

</div>

# Scheme Conjugacy Between Encodings

We now formalize the sense in which the different encodings introduced above represent the same upstairs admissibility constraint. The central technical notion is that of controlled conjugacy between scale-step maps.

<div class="definition">

**Definition 26** (Scale-Step Map). Let $`\mathcal{X}`$ denote a space of effective variables associated with a given encoding. A scale-step map is a map
``` math
\mathcal{R}:\mathcal{X}\rightarrow\mathcal{X}
```
representing the effect of a finite coarse-graining step on the encoding variables.

</div>

In the present context, three scale-step maps are relevant:

1.  the induced scale-step map on coherent overlap data, inherited from iteration of the projected map $`T`$;

2.  the worldsheet renormalization-group step acting on sigma-model couplings $`\mathbf{g}`$;

3.  the functional renormalization-group step acting on truncation couplings $`\mathbf{u}^{(N)}`$.

<div class="definition">

**Definition 27** (Controlled Conjugacy). Let $`\mathcal{R}_1`$ and $`\mathcal{R}_2`$ be scale-step maps on spaces $`\mathcal{X}_1`$ and $`\mathcal{X}_2`$, respectively. We say that $`\mathcal{R}_1`$ and $`\mathcal{R}_2`$ are controlled-conjugate on an admissible slab if there exists a bounded, invertible map $`U:\mathcal{X}_1\rightarrow\mathcal{X}_2`$ such that
``` math
\mathcal{R}_1
=
U^{-1}\circ \mathcal{R}_2\circ U
+
\mathcal{E},
```
where the remainder $`\mathcal{E}`$ satisfies
``` math
\|\mathcal{E}\|\le C\,\lambda_\ast^{-1}
```
uniformly on the slab.

</div>

<div class="remark">

*Remark 28*. Controlled conjugacy expresses the fact that two encodings differ only by a bounded change of variables and a controlled truncation error. It is weaker than exact conjugacy but sufficient to preserve fixed-point structure up to admissible error.

</div>

<div class="assumption">

**Assumption 29** (Worldsheet Conjugacy). Within the string corner, the induced scale-step map on coherent overlap data and the worldsheet renormalization-group step are controlled-conjugate.

</div>

<div class="assumption">

**Assumption 30** (FRG Conjugacy). Within the asymptotic-safety corner, the induced scale-step map on coherent overlap data and the functional renormalization-group step associated with the chosen truncation family are controlled-conjugate.

</div>

<div class="lemma">

**Lemma 31** (Propagation of Fixed Points Under Controlled Conjugacy). *Let $`\mathcal{R}_1`$ and $`\mathcal{R}_2`$ be controlled-conjugate scale-step maps. If $`\mathcal{R}_2`$ admits a fixed point $`x_\ast`$ with linearized stability bounded on the slab, then $`\mathcal{R}_1`$ admits an approximate fixed point $`y_\ast`$ satisfying
``` math
\|\mathcal{R}_1(y_\ast)-y_\ast\|\le C\,\lambda_\ast^{-1}.
```*

</div>

<div class="proof">

*Proof.* Let $`U`$ denote the conjugacy map. Set $`y_\ast:=U^{-1}(x_\ast)`$. Then
``` math
\mathcal{R}_1(y_\ast)-y_\ast
=
U^{-1}\mathcal{R}_2(x_\ast)-U^{-1}(x_\ast)+\mathcal{E}(y_\ast)
=
\mathcal{E}(y_\ast),
```
which is bounded by $`C\,\lambda_\ast^{-1}`$ by assumption. Linearized stability follows from boundedness of $`U`$ and stability of $`x_\ast`$, with corrections controlled by the same remainder. ◻

</div>

<div class="remark">

*Remark 32*. This lemma is the technical mechanism that allows fixed-point conditions to be transferred between encodings.

</div>

# Reconstruction of Admissibility from Each Encoding

We now show that admissibility of a coherent configuration can be reconstructed from fixed-point data in each encoding.

<div class="lemma">

**Lemma 33** (Worldsheet Fixed Point Implies Admissibility). *Let $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ lie within the string corner. If the associated sigma-model couplings $`\mathbf{g}(\psi)`$ admit a worldsheet fixed point, then $`\psi`$ is admissible and lies within an admissible basin of the projected map $`T`$.*

</div>

<div class="proof">

*Proof.* By the worldsheet conjugacy assumption, the worldsheet renormalization-group step is controlled-conjugate to the induced scale-step map on coherent overlap data. By the previous lemma, the existence of a worldsheet fixed point implies the existence of an approximate fixed point of the induced scale-step map, hence of $`T`$, up to $`O(\lambda_\ast^{-1})`$. Stability of the worldsheet fixed point implies bounded response under scale transformations, which pulls back to bounded projector regularity and persistence of the spectral gap. These conditions define admissibility. ◻

</div>

<div class="lemma">

**Lemma 34** (FRG Fixed Point Implies Admissibility). *Let $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ lie within the asymptotic-safety corner. If the associated truncation couplings $`\mathbf{u}^{(N)}(\psi)`$ admit a functional renormalization-group ultraviolet fixed point with finitely many relevant directions, then $`\psi`$ is admissible and lies within an admissible basin of $`T`$.*

</div>

<div class="proof">

*Proof.* By the FRG conjugacy assumption, the functional renormalization-group step is controlled-conjugate to the induced scale-step map on coherent overlap data. By propagation of fixed points under controlled conjugacy, the FRG fixed point yields an approximate fixed point of $`T`$. The finiteness of relevant directions ensures that no uncontrolled instability directions exist, implying bounded linearized dynamics within an admissible basin. This reconstructs admissibility of $`\psi`$. ◻

</div>

<div class="lemma">

**Lemma 35** (Coherent-Spine Membership Implies Fixed Points in All Encodings). *Let $`\psi\in\mathfrak{S}`$. Then $`\psi`$ induces both a worldsheet fixed point (within the string corner) and a functional renormalization-group ultraviolet fixed point (within the asymptotic-safety corner), up to controlled truncation error.*

</div>

<div class="proof">

*Proof.* If $`\psi\in\mathfrak{S}`$, then $`\psi`$ is an approximate fixed point of $`T`$ with bounded linearized stability. Controlled conjugacy between the induced scale-step map and each encoding implies, by propagation of fixed points, the existence of approximate fixed points in the worldsheet and functional renormalization-group encodings. ◻

</div>

# Conjugacy and Dimensional Reduction: A Controlled Commuting Diagram

This section makes precise the additional structural ingredient required when the string corner is naturally formulated in a ten-dimensional sigma-model background, while the asymptotic-safety corner is formulated as a four-dimensional functional renormalization-group (FRG) flow. The missing leg is an admissible $`10\mathrm{D}\to 4\mathrm{D}`$ reduction/encoding map. We formulate a controlled commuting diagram of scale-step maps and show that fixed-point structure and stability spectra match across all three corners up to controlled truncation error.

## Spaces of encodings

<div class="definition">

**Definition 36** (Upstairs overlap data space). Let $`\Theta`$ denote slab-local coherent overlap/bottleneck data (including, when applicable, compactification/moduli data sufficient to define a reduced effective description). Let $`\mathcal{U}_\Theta\subset \Theta`$ denote the admissible chart domain where the coherent projector is bounded and controlled truncation holds.

</div>

<div class="definition">

**Definition 37** (Worldsheet background space). Let $`\mathfrak{M}_{\mathrm{ws}}^{(10)}`$ denote the space of ten-dimensional sigma-model background data (e.g. tuples $`(g_{MN},B_{MN},\Phi,\ldots)`$ of specified regularity) modulo the usual admissible field redefinitions and scheme redundancies.

</div>

<div class="definition">

**Definition 38** (Four-dimensional effective-action space). Let $`\mathfrak{B}_{\mathrm{act}}^{(4)}`$ denote a Banach space of quasi-local four-dimensional effective actions (or effective average actions) equipped with a norm $`\|\cdot\|_{(4)}`$ on an admissible slab. Let $`\mathfrak{B}_{\mathrm{frg}}^{(4)}\subset \mathfrak{B}_{\mathrm{act}}^{(4)}`$ denote the domain where a chosen FRG step map is well-defined.

</div>

## Encoding maps

<div id="A:Uws" class="assumption">

**Assumption 39** (Worldsheet encoding chart and regularity). There exists a map (the string-corner chart)
``` math
U_{\mathrm{ws}}:\mathcal{U}_\Theta \to \mathfrak{M}_{\mathrm{ws}}^{(10)}
```
that is bounded and bi-Lipschitz onto its image. Moreover, the contribution of discarded noncoherent modes to the worldsheet encoding is controlled by the spectral gap: there exists $`C_{\mathrm{ws}}<\infty`$ such that encoding remainders are bounded by $`C_{\mathrm{ws}}\lambda_\ast^{-1}`$ on the slab.

</div>

<div id="A:U104" class="assumption">

**Assumption 40** ($`10\mathrm{D}\to 4\mathrm{D}`$ admissible reduction map). There exists a slab-local reduction/encoding map
``` math
U_{10\to 4}: \mathfrak{M}_{\mathrm{ws}}^{(10)} \supset \mathcal{U}_{10} \to \mathfrak{B}_{\mathrm{act}}^{(4)}
```
defined on an admissible subset $`\mathcal{U}_{10}`$ containing $`U_{\mathrm{ws}}(\mathcal{U}_\Theta)`$, such that:

1.  **(Well-defined reduction)** $`U_{10\to 4}`$ produces a four-dimensional effective action whose field content and operator expansion are consistent with a fixed truncation class on the slab.

2.  **(Controlled tower truncation)** the integrated-out Kaluza–Klein tower and heavy string modes contribute a remainder bounded by $`C_{10\to 4}\lambda_\ast^{-1}`$ in $`\|\cdot\|_{(4)}`$.

3.  **(Regularity)** $`U_{10\to 4}`$ is bounded and bi-Lipschitz onto its image (possibly after quotienting by admissible field redefinitions / scheme redundancies).

</div>

<div id="A:Ufrg" class="assumption">

**Assumption 41** (FRG encoding chart and regularity). There exists a map
``` math
U_{\mathrm{frg}}:\mathcal{U}_\Theta \to \mathfrak{B}_{\mathrm{frg}}^{(4)}
```
that is bounded and bi-Lipschitz onto its image and whose encoding remainder is bounded by $`C_{\mathrm{frg}}\lambda_\ast^{-1}`$ in $`\|\cdot\|_{(4)}`$.

</div>

<div class="remark">

*Remark 42*. Assumptions <a href="#A:Uws" data-reference-type="ref" data-reference="A:Uws">39</a> and <a href="#A:Ufrg" data-reference-type="ref" data-reference="A:Ufrg">41</a> are the worldsheet and FRG chart-regularity modules. Assumption <a href="#A:U104" data-reference-type="ref" data-reference="A:U104">40</a> is the additional ingredient required for a $`10\mathrm{D}\to 4\mathrm{D}`$ bridge. Each assumption is local to an admissible chart and is conditioned on the same coherent control parameter $`\lambda_\ast`$.

</div>

## Scale-step maps

<div class="definition">

**Definition 43** (Upstairs coarse-graining step). Let $`\mathcal{C}_b:\mathcal{U}_\Theta\to\mathcal{U}_\Theta`$ denote the induced slab-local coarse-graining step on overlap data associated with the coherent projected dynamics, for a fixed scale factor $`b>1`$.

</div>

<div class="definition">

**Definition 44** (Worldsheet RG step). Let $`\mathrm{RG}^{(10)}_{\mathrm{ws},b}:\mathfrak{M}_{\mathrm{ws}}^{(10)}\to \mathfrak{M}_{\mathrm{ws}}^{(10)}`$ denote the standard (scheme-fixed) worldsheet RG step map corresponding to $`b`$.

</div>

<div class="definition">

**Definition 45** (FRG step). Let $`\mathrm{RG}^{(4)}_{\mathrm{frg},b}:\mathfrak{B}_{\mathrm{frg}}^{(4)}\to\mathfrak{B}_{\mathrm{frg}}^{(4)}`$ denote the FRG step map (e.g. the time-$`\ln b`$ map of the Wetterich flow, on a chosen regulator and truncation class).

</div>

## Controlled commuting conditions

<div id="A:ws-step" class="assumption">

**Assumption 46** (Worldsheet conjugacy of steps). There exists a bounded reparametrization (scheme map) $`S_{\mathrm{ws}}`$ of $`\mathfrak{M}_{\mathrm{ws}}^{(10)}`$ such that the composed map $`\widetilde{U}_{\mathrm{ws}}:=S_{\mathrm{ws}}\circ U_{\mathrm{ws}}`$ satisfies
``` math
\widetilde{U}_{\mathrm{ws}}\circ \mathcal{C}_b
=
\mathrm{RG}^{(10)}_{\mathrm{ws},b}\circ \widetilde{U}_{\mathrm{ws}} + \mathcal{E}_{\mathrm{ws}},
\qquad
\|\mathcal{E}_{\mathrm{ws}}\|\le C_{\mathrm{ws}}\,\lambda_\ast^{-1}.
```

</div>

<div id="A:frg-step" class="assumption">

**Assumption 47** (FRG conjugacy of steps). The FRG chart satisfies
``` math
U_{\mathrm{frg}}\circ \mathcal{C}_b
=
\mathrm{RG}^{(4)}_{\mathrm{frg},b}\circ U_{\mathrm{frg}} + \mathcal{E}_{\mathrm{frg}},
\qquad
\|\mathcal{E}_{\mathrm{frg}}\|_{(4)}\le C_{\mathrm{frg}}\,\lambda_\ast^{-1}.
```

</div>

<div id="A:104-compat" class="assumption">

**Assumption 48** ($`10\mathrm{D}\to 4\mathrm{D}`$ RG-compatibility). On the admissible overlap, $`U_{10\to 4}`$ approximately intertwines the worldsheet and FRG steps:
``` math
U_{10\to 4}\circ \mathrm{RG}^{(10)}_{\mathrm{ws},b}
=
\mathrm{RG}^{(4)}_{\mathrm{frg},b}\circ U_{10\to 4} + \mathcal{E}_{10\to 4},
\qquad
\|\mathcal{E}_{10\to 4}\|_{(4)}\le C_{10\to 4}\,\lambda_\ast^{-1}.
```

</div>

<div class="remark">

*Remark 49*. Assumption <a href="#A:104-compat" data-reference-type="ref" data-reference="A:104-compat">48</a> is the precise mathematical expression of “the $`10\mathrm{D}\to 4\mathrm{D}`$ projection is admissible and commutes with coarse-graining up to controlled error.” It is the bridge-leg that makes the triple-corner result compatible with dimensional reduction.

</div>

## Main commuting-diagram theorem

<div id="T:commuting" class="theorem">

**Theorem 50** (Controlled Commuting Diagram and Conjugacy). *Assume <a href="#A:Uws" data-reference-type="ref" data-reference="A:Uws">39</a>, <a href="#A:U104" data-reference-type="ref" data-reference="A:U104">40</a>, <a href="#A:Ufrg" data-reference-type="ref" data-reference="A:Ufrg">41</a>, <a href="#A:ws-step" data-reference-type="ref" data-reference="A:ws-step">46</a>, <a href="#A:frg-step" data-reference-type="ref" data-reference="A:frg-step">47</a>, and <a href="#A:104-compat" data-reference-type="ref" data-reference="A:104-compat">48</a>. Then, on the admissible overlap $`\mathcal{U}_\Theta`$, the following controlled commuting relation holds:
``` math
U_{\mathrm{frg}}
=
U_{10\to 4}\circ \widetilde{U}_{\mathrm{ws}} + \mathcal{E}_{\mathrm{diag}},
\qquad
\|\mathcal{E}_{\mathrm{diag}}\|_{(4)}\le C_{\mathrm{diag}}\,\lambda_\ast^{-1},
```
for some bounded constant $`C_{\mathrm{diag}}`$ on the slab. Moreover, fixed points and their stable/unstable splittings correspond across the three corners up to $`O(\lambda_\ast^{-1})`$.*

</div>

<div class="proof">

*Proof.* Starting from Assumption <a href="#A:ws-step" data-reference-type="ref" data-reference="A:ws-step">46</a>, apply $`U_{10\to 4}`$ to both sides:
``` math
U_{10\to 4}\circ \widetilde{U}_{\mathrm{ws}}\circ \mathcal{C}_b
=
U_{10\to 4}\circ \mathrm{RG}^{(10)}_{\mathrm{ws},b}\circ \widetilde{U}_{\mathrm{ws}}
+ U_{10\to 4}\circ \mathcal{E}_{\mathrm{ws}}.
```
Using Assumption <a href="#A:104-compat" data-reference-type="ref" data-reference="A:104-compat">48</a> on the middle term,
``` math
U_{10\to 4}\circ \mathrm{RG}^{(10)}_{\mathrm{ws},b}
=
\mathrm{RG}^{(4)}_{\mathrm{frg},b}\circ U_{10\to 4} + \mathcal{E}_{10\to 4}.
```
Substituting gives
``` math
U_{10\to 4}\circ \widetilde{U}_{\mathrm{ws}}\circ \mathcal{C}_b
=
\mathrm{RG}^{(4)}_{\mathrm{frg},b}\circ U_{10\to 4}\circ \widetilde{U}_{\mathrm{ws}}
+
\mathcal{E}_{10\to 4}\circ \widetilde{U}_{\mathrm{ws}}
+
U_{10\to 4}\circ \mathcal{E}_{\mathrm{ws}}.
```
Compare this with Assumption <a href="#A:frg-step" data-reference-type="ref" data-reference="A:frg-step">47</a>:
``` math
U_{\mathrm{frg}}\circ \mathcal{C}_b
=
\mathrm{RG}^{(4)}_{\mathrm{frg},b}\circ U_{\mathrm{frg}} + \mathcal{E}_{\mathrm{frg}}.
```
Define $`\mathcal{E}_{\mathrm{diag}}:=U_{\mathrm{frg}}-U_{10\to 4}\circ \widetilde{U}_{\mathrm{ws}}`$. Rearranging and using boundedness of the charts, the triangle inequality, and the remainder bounds in Assumptions <a href="#A:ws-step" data-reference-type="ref" data-reference="A:ws-step">46</a>, <a href="#A:frg-step" data-reference-type="ref" data-reference="A:frg-step">47</a>, and <a href="#A:104-compat" data-reference-type="ref" data-reference="A:104-compat">48</a> yields
``` math
\|\mathcal{E}_{\mathrm{diag}}\|_{(4)}\le C_{\mathrm{diag}}\,\lambda_\ast^{-1}
```
for a slab-bounded $`C_{\mathrm{diag}}`$.

Fixed-point correspondence: if $`\Theta_\ast`$ is a fixed point of $`\mathcal{C}_b`$ up to $`O(\lambda_\ast^{-1})`$, then by <a href="#A:ws-step" data-reference-type="ref" data-reference="A:ws-step">46</a> and <a href="#A:frg-step" data-reference-type="ref" data-reference="A:frg-step">47</a> its images are fixed points of the worldsheet and FRG step maps up to $`O(\lambda_\ast^{-1})`$. The commuting relation then identifies the $`10\mathrm{D}\to 4\mathrm{D}`$ images of worldsheet fixed points with FRG fixed points to the same order. Stability splittings follow by linearizing the intertwining relations and applying standard bounded-perturbation estimates to the $`O(\lambda_\ast^{-1})`$ remainders. ◻

</div>

## Corollaries: fixed points and $`10\mathrm{D}\to 4\mathrm{D}`$ applicability

<div id="C:applicable" class="corollary">

**Corollary 51** (When the $`10\mathrm{D}\to 4\mathrm{D}`$ leg is applicable). *The $`10\mathrm{D}\to 4\mathrm{D}`$ leg is applicable precisely on the subset of the string corner where Assumption <a href="#A:U104" data-reference-type="ref" data-reference="A:U104">40</a> holds, i.e. where tower truncation and moduli reduction remain controlled with error $`O(\lambda_\ast^{-1})`$. Outside this subset, the worldsheet conjugacy and FRG conjugacy may still hold as separate encodings of $`\mathcal{C}_b`$, but the commuting diagram need not close.*

</div>

<div id="C:spectra104" class="corollary">

**Corollary 52** (Matching of leading irrelevant spectra across $`10\mathrm{D}`$ and $`4\mathrm{D}`$). *Under the hypotheses of Theorem <a href="#T:commuting" data-reference-type="ref" data-reference="T:commuting">50</a>, the leading irrelevant stability spectra at a hyperbolic worldsheet fixed point and at the corresponding FRG UV fixed point agree up to $`O(\lambda_\ast^{-1})`$, after admissible scheme reparametrization.*

</div>

# Triple-Corner Equivalence Theorem

We now state the central result of the paper.

<div class="theorem">

**Theorem 53** (Triple-Corner Shadow Bridge). *Let $`\psi\in\mathcal{H}_{\mathrm{coh}}`$ lie within the overlap of the admissible slab, the string corner, and the asymptotic-safety corner. Then the following statements are equivalent up to controlled truncation error of order $`O(\lambda_\ast^{-1})`$:*

1.  *$`\psi`$ lies on the coherent spine $`\mathfrak{S}`$.*

2.  *The associated sigma-model couplings $`\mathbf{g}(\psi)`$ admit a worldsheet renormalization-group fixed point.*

3.  *The associated truncation couplings $`\mathbf{u}^{(N)}(\psi)`$ admit a functional renormalization-group ultraviolet fixed point with finitely many relevant directions.*

</div>

<div class="proof">

*Proof.* The implication $`(1)\Rightarrow(2)`$ follows from coherent-spine membership and worldsheet conjugacy. The implication $`(1)\Rightarrow(3)`$ follows from coherent-spine membership and FRG conjugacy. The implication $`(2)\Rightarrow(1)`$ follows from reconstruction of admissibility from a worldsheet fixed point. The implication $`(3)\Rightarrow(1)`$ follows from reconstruction of admissibility from an FRG fixed point. Together, these establish the equivalence. ◻

</div>

# Matching Stability Spectra Across Encodings

We now derive concrete cross-framework consequences of the triple-corner equivalence. The first concerns the spectrum of linearized stability operators about fixed points in each encoding.

<div class="definition">

**Definition 54** (Linearized Stability Operators). Let $`\psi\in\mathfrak{S}`$ be a coherent-spine configuration. We define:

1.  the coherent-spine stability operator $`L_{\mathrm{coh}}`$ as the linearization of the projected map $`T`$ about $`\psi`$;

2.  the worldsheet stability operator $`L_{\mathrm{ws}}`$ as the linearization of the worldsheet renormalization-group flow about the fixed point $`\mathbf{g}(\psi)`$;

3.  the functional renormalization-group stability operator $`L_{\mathrm{frg}}`$ as the Jacobian of the beta functions $`\boldsymbol{\beta}^{(N)}`$ evaluated at $`\mathbf{u}^{(N)}(\psi)`$.

</div>

<div class="remark">

*Remark 55*. The operators $`L_{\mathrm{coh}}`$, $`L_{\mathrm{ws}}`$, and $`L_{\mathrm{frg}}`$ act on different spaces, but their spectra encode the response of the corresponding encoding to small perturbations.

</div>

<div class="proposition">

**Proposition 56** (Matching of Leading Irrelevant Spectra). *Let $`\theta_i^{\mathrm{coh}}`$, $`\theta_i^{\mathrm{ws}}`$, and $`\theta_i^{\mathrm{frg}}`$ denote the eigenvalues of $`L_{\mathrm{coh}}`$, $`L_{\mathrm{ws}}`$, and $`L_{\mathrm{frg}}`$ associated with irrelevant directions. Then, up to reordering and scheme reparametrization,
``` math
\theta_i^{\mathrm{coh}}
=
\theta_i^{\mathrm{ws}}
=
\theta_i^{\mathrm{frg}}
+
O(\lambda_\ast^{-1})
```
for the leading irrelevant modes.*

</div>

<div class="proof">

*Proof.* By controlled conjugacy, the scale-step maps underlying the three encodings are related by bounded conjugations plus remainders of order $`O(\lambda_\ast^{-1})`$. Linearization of conjugate maps yields operators related by similarity transformations up to controlled perturbations. Similarity transformations preserve spectra exactly, while bounded perturbations shift eigenvalues by at most $`O(\lambda_\ast^{-1})`$ by standard operator perturbation theory. Hence the leading irrelevant spectra coincide up to the truncation scale. ◻

</div>

<div class="remark">

*Remark 57*. This result yields a nontrivial, falsifiable prediction: critical exponents computed in worldsheet renormalization-group analyses and in functional renormalization-group studies of asymptotic safety must agree within controlled error when both lie in the admissible overlap.

</div>

# Correlated Breakdown Surfaces

We now analyze the consequences of admissibility failure. The triple-corner equivalence implies that breakdown of one encoding cannot occur independently of the others.

<div class="definition">

**Definition 58** (Admissibility Breakdown). Admissibility is said to break down at a configuration $`\psi`$ if the spectral gap $`\lambda_\ast`$ closes, the coherent-sector projector ceases to be bounded, or truncation errors become uncontrolled.

</div>

<div class="proposition">

**Proposition 59** (Correlated Breakdown of Encodings). *If admissibility breaks down at $`\psi`$, then:*

1.  *the worldsheet renormalization-group flow ceases to admit a fixed point near $`\mathbf{g}(\psi)`$;*

2.  *the functional renormalization-group flow ceases to admit a controlled ultraviolet fixed point near $`\mathbf{u}^{(N)}(\psi)`$.*

*Conversely, if either the worldsheet or functional renormalization-group fixed point condition fails beyond controlled error, admissibility must have broken down.*

</div>

<div class="proof">

*Proof.* If admissibility breaks down, controlled conjugacy between the induced scale-step map and each encoding fails. Without controlled conjugacy, the propagation of fixed points under bounded reparametrization no longer holds, and fixed points in the encodings cannot be maintained.

Conversely, suppose a worldsheet or functional renormalization-group fixed point persisted far beyond admissibility breakdown. Reconstruction lemmas established earlier would then imply bounded projector regularity and persistence of the spectral gap, contradicting the assumption of admissibility failure. Hence breakdown surfaces are correlated. ◻

</div>

<div class="remark">

*Remark 60*. This explains why perturbative string theory and asymptotic safety are observed to fail in similar regimes, such as near strong curvature or topology-changing configurations.

</div>

# Interpretation and Consequences

The triple-corner shadow bridge reframes long-standing debates in quantum gravity. Within the admissible universality class, perturbative string theory and asymptotic safety are not alternative ultraviolet completions but complementary diagnostics of the same upstairs fixed-point structure.

From the perspective of Modal Triplet Theory, neither worldsheet consistency nor functional renormalization-group fixed points are fundamental. Both are shadows of coherent-sector admissibility. Their apparent success arises from the fact that they test the same constraint using different variables and coarse-graining procedures.

This interpretation clarifies several puzzles. It explains why both string theory and asymptotic safety repeatedly recover Einstein gravity as the infrared attractor. It also explains why both frameworks encounter difficulties beyond certain regimes: those difficulties signal loss of admissibility rather than failure of a particular formalism.

# Conclusion

We have established a third-corner shadow bridge connecting perturbative string theory, functional renormalization-group asymptotic safety, and the coherent spine of Modal Triplet Theory. Under explicit and controlled assumptions, we proved that coherent-spine fixed points, worldsheet renormalization-group fixed points, and functional renormalization-group ultraviolet fixed points are equivalent encodings of a single upstairs admissibility constraint up to truncation error of order $`O(\lambda_\ast^{-1})`$.

This result reframes the apparent plurality of ultraviolet completions of gravity as an artifact of encoding choice. It yields concrete cross-framework predictions, including matching stability spectra and correlated breakdown surfaces, and provides a unifying structural explanation for the successes and limitations of existing approaches.

More broadly, the triple-corner shadow bridge reinforces the central lesson of Modal Triplet Theory: physically viable theories are selected by admissibility, and diverse mathematical formalisms arise as shadows of the same underlying fixed-point structure.

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
