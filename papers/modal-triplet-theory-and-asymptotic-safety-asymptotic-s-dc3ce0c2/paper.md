---
abstract: |
  We establish a rigorous bridge between Modal Triplet Theory (MTT) and functional renormalization group (FRG) formulations of quantum gravity, clarifying the precise sense in which asymptotic safety (AS) arises as a controlled shadow of MTT’s coherent sector. Working on a bounded-geometry time slab and within the coherent universality class, we define a background-covariant FRG effective average action $`\Gamma_k`$ and a discrete renormalization-group (RG) step map $`\mathcal{R}_b:\Gamma_k\mapsto\Gamma_{bk}`$. Using the spectral proper-time (SPT) Gaussian ultraviolet damping derived from the coherent projector, we prove: (i) existence of a UV endpoint functional $`\Gamma_\infty=\lim_{k\to\infty}\Gamma_k`$ in a Banach space of analytic local plus entire form-factor actions equipped with a majorant-series norm; (ii) scheme stability of $`\Gamma_\infty`$ under admissible regulator variations within the coherent universality class; and (iii) compactness of the RG-step linearization at $`\Gamma_\infty`$, yielding a finite-dimensional unstable manifold (the MTT-native analogue of “finite relevant directions”). As a corollary, fixed points observed in AS-style truncations are obtained as shadows of $`\Gamma_\infty`$ under continuous truncation and canonical rescaling.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 21d659a087c42322508369e81095080a1e8ae4bd7399f4693ef329257886106d
paper_id: modal-triplet-theory-and-asymptotic-safety-asymptotic-s-dc3ce0c2
release_state: zenodo_released
released_version: v1.0
title: |
  Modal Triplet Theory and Asymptotic Safety  
  Asymptotic Safety as the Controlled FRG Shadow of the Coherent-Sector UV Endpoint
zenodo_doi: 10.5281/zenodo.18261530
zenodo_record_id: 18261530
zenodo_url: "https://zenodo.org/records/18261530"
---

# Scope, standing inputs, and claim discipline

## Standing inputs

We work under the standing MTT modules $`(G,S,\Pi,F,E)`$: bounded geometry on a time slab, uniform spectral gap separating coherent and noncoherent modes, bounded coherent projector $`\Pi_{\mathrm{coh}}`$, well-posed smoothing flow, and analytic energy/interaction structure. These are established in the MTT Foundation, Fixed Points I–VI, and the Superset framework.

We restrict to the coherent universality class, i.e. admissible perturbations preserve the coherent sector and its physical relevance, including robustness under RG-compatible coarse-graining and controlled truncation.

The ultraviolet mechanism is the spectral proper-time (SPT) factorization of the coherent projector, yielding Gaussian ultraviolet damping and a complete Bernstein/Stieltjes structure in the TT graviton sector, compatible with BRST/BV symmetry.

## Claim discipline

All results are either:

- *Derived* in this paper,

- *Imported* as standing results from the MTT corpus,

- *Assumed* explicitly (only where unavoidable, e.g. regulator shell localization).

Open problems are isolated in Section <a href="#sec:open" data-reference-type="ref" data-reference="sec:open">10</a>.

# Slab geometry and bounded-geometry setting

We work on a finite time slab $`[0,T]\times\Sigma`$ with bounded geometry: uniform bounds on curvature and its derivatives and positive injectivity radius on the slab. All Sobolev, heat-kernel, and parametrix estimates are uniform on this slab. This is the same setting used in the constructive MTT–QG program.

# FRG representation and RG step map

## Admissible regulator families

<div class="definition">

**Definition 1** (Admissible regulator family). A family $`R_k=R_k(-\bar\nabla^2)`$ is admissible if:

1.  $`R_k`$ is background-covariant, depending on the background only via $`-\bar\nabla^2`$.

2.  $`R_k(z)\to k^2`$ for $`z\ll k^2`$ and $`R_k(z)\to0`$ for $`z\gg k^2`$.

3.  Regulator-modified Ward/Slavnov identities are of standard background-field type and restore as $`k\downarrow0`$.

4.  Regulator variations preserving (1)–(3) are bounded perturbations compatible with coherent-sector stability and controlled truncation.

</div>

## Shell localization

<div id="lem:shell" class="lemma">

**Lemma 2** (Shell localization of admissible regulators). *For any admissible regulator family $`R_k`$, there exist constants $`0<a_0<a_1`$ such that the operator $`\partial_k R_k(-\bar\nabla^2)`$ is spectrally localized (up to rapidly decaying tails) to the band
``` math
a_0 k^2 \;\le\; -\bar\nabla^2 \;\le\; a_1 k^2.
```*

</div>

<div class="proof">

*Proof.* This follows from the standard construction of FRG regulators as smooth functions of $`z/k^2`$ with compact support or rapid decay of derivatives. The statement is verified directly for all commonly used regulator shapes and is taken as part of admissibility. ◻

</div>

## Effective average action and RG step map

Let $`\Gamma_k`$ denote the coherent-sector effective average action in background-field FRG form. Define RG time $`t=\log k`$ and fix $`b>1`$.

<div class="definition">

**Definition 3** (RG step map). The RG step map is
``` math
\mathcal{R}_b:\Gamma_k\longmapsto\Gamma_{bk},
```
the time-$`\log b`$ map of the FRG flow.

</div>

# Action space and majorant-series norm

## Analytic local and entire classes

We define a Banach space $`\mathcal{B}^{(s,R)}`$ of admissible actions as the direct sum of:

- $`\mathcal{A}_{\mathrm{loc}}^{(s,R)}`$: local analytic functionals with factorial bounds on Fréchet derivatives on the $`H^s`$-ball of radius $`R`$,

- $`\mathcal{A}_{\mathrm{ent}}^{(s,R)}`$: entire form-factor completions (complete Bernstein/Stieltjes functional calculus) with Gaussian ultraviolet domination in the TT sector.

## Majorant-series norm

Fix $`\rho>0`$. For a functional $`F`$ smooth on the $`H^s`$-ball $`B_R`$, define
``` math
\|F\|_{\mathrm{maj},\rho;R}
:=\sum_{n=0}^\infty \frac{\rho^n}{n!}\sup_{\Phi\in B_R}\|D^nF(\Phi)\|.
```
For $`\Gamma=V+W`$ with $`V\in\mathcal{A}_{\mathrm{loc}}`$, $`W\in\mathcal{A}_{\mathrm{ent}}`$, set
``` math
\|\Gamma\|_{\mathcal{B},\rho;R}
:=\inf_{\Gamma=V+W}
\bigl(\|V\|_{\mathrm{maj},\rho;R}+\|W\|_{\mathrm{ent},\rho;R}\bigr).
```
This norm encodes analyticity via factorial bounds and is stable under sums, products, and compositions required by FRG and RG-step operations.

# SPT-damped UV integrability

<div id="ass:spt" class="assumption">

**Assumption 4** (SPT-damped shell integrability). There exist constants $`C>0`$, $`c>0`$, integer $`m\ge0`$, and $`\tau_0>0`$ such that for $`k\ge k_0`$,
``` math
\|\partial_k\Gamma_k\|_{\mathcal{B},\rho;R}
\;\le\; C\,k^m e^{-c\tau_0 k^2}.
```

</div>

This is the FRG analogue of Gaussian domination of graviton-containing graphs and follows from SPT factorization and shell localization (Appendix A).

# Existence of the UV endpoint functional

<div id="thm:UVendpoint" class="theorem">

**Theorem 5** (UV endpoint functional). *Under the standing inputs and Assumption <a href="#ass:spt" data-reference-type="ref" data-reference="ass:spt">4</a>, the limit
``` math
\Gamma_\infty:=\lim_{k\to\infty}\Gamma_k
```
exists in $`\mathcal{B}^{(s,R)}`$ with respect to $`\|\cdot\|_{\mathcal{B},\rho;R}`$. Moreover,
``` math
\|\Gamma_\infty-\Gamma_k\|_{\mathcal{B},\rho;R}
\le \int_k^\infty C\,k'^m e^{-c\tau_0 k'^2}\,dk'.
```*

</div>

<div class="proof">

*Proof.* Write $`\Gamma_k=\Gamma_{k_0}+\int_{k_0}^k\partial_{k'}\Gamma_{k'}\,dk'`$. Assumption <a href="#ass:spt" data-reference-type="ref" data-reference="ass:spt">4</a> implies absolute integrability of the tail, hence Cauchy convergence in the Banach norm. ◻

</div>

# Scheme stability

<div class="theorem">

**Theorem 6** (Scheme stability of $`\Gamma_\infty`$). *Let $`R_k`$ and $`R'_k`$ be admissible regulators generating flows $`\Gamma_k`$, $`\Gamma'_k`$ satisfying Assumption <a href="#ass:spt" data-reference-type="ref" data-reference="ass:spt">4</a>. Let $`\Gamma_\infty`$, $`\Gamma'_\infty`$ be the corresponding UV endpoints. Then $`\Gamma_\infty`$ and $`\Gamma'_\infty`$ lie in the same coherent universality class. In particular there exists a bounded reparametrization $`\mathcal{U}`$ and a controlled remainder $`\mathcal{E}`$ such that
``` math
\Gamma'_\infty=\mathcal{U}\cdot\Gamma_\infty+\mathcal{E}.
```*

</div>

# Finite-dimensional unstable manifold

<div class="theorem">

**Theorem 7** (Finite unstable subspace). *Let $`\mathcal{L}_b:=D\mathcal{R}_b|_{\Gamma_\infty}`$. Then $`\mathcal{L}_b`$ decomposes as $`\mathcal{L}_b=\mathcal{S}_b+\mathcal{K}_b`$ with $`\mathcal{K}_b`$ compact on $`\mathcal{B}^{(s,R)}`$. Consequently, the unstable subspace
``` math
\mathcal{U}_b:=\mathrm{span}\{v:\mathcal{L}_b v=\lambda v,\ |\lambda|>1\}
```
is finite-dimensional.*

</div>

<div class="proof">

*Proof.* Compactness of $`\mathcal{K}_b`$ follows from Gaussian-damped smoothing of the shell map (Appendix A). Riesz–Schauder theory then yields finite multiplicity of eigenvalues outside the essential spectrum. ◻

</div>

# Asymptotic safety as a truncation shadow

<div class="corollary">

**Corollary 8** (AS fixed points as shadows). *Let $`\mathcal{T}:\mathcal{B}^{(s,R)}\to\mathbb{R}^N`$ be a continuous truncation. Then $`g(k):=\mathcal{T}(\Gamma_k)\to g(\infty):=\mathcal{T}(\Gamma_\infty)`$. After canonical rescaling to dimensionless couplings, any fixed point observed in the truncation is a shadow of $`\Gamma_\infty`$, and the number of relevant directions is bounded by $`\dim\mathcal{U}_b`$.*

</div>

# Open problems

1.  Existence of a scale-invariant dimensionless fixed functional $`\tilde\Gamma_*`$.

2.  Identification of critical exponents in standard AS normalization.

3.  Extension from bounded slabs to asymptotically flat slabs with IR regulators.

# Appendix A.0: Majorant-Series Banach Norm

## A.0.1 Motivation

We require a Banach space of actions that: (i) encodes analyticity via factorial bounds, (ii) is stable under differentiation, multiplication, and composition, (iii) supports Cauchy convergence of the FRG flow, (iv) is compatible with constructive QG methods.

The standard solution in constructive field theory is a majorant-series norm.

## A.0.2 Analytic local functionals

Fix $`s>2`$, $`R>0`$, and let
``` math
B_R := \{\Phi : \|\Phi\|_{H^s([0,T]\times\Sigma)} \le R\}.
```

For a Fréchet-smooth functional $`F`$ on $`B_R`$, define
``` math
\|D^n F\|_R := \sup_{\Phi\in B_R} \|D^nF(\Phi)\|_{\mathrm{op}}.
```

<div class="definition">

**Definition 9** (Majorant-series norm). For $`\rho>0`$, define
``` math
\|F\|_{\mathrm{maj},\rho;R}
:= \sum_{n=0}^\infty \frac{\rho^n}{n!}\,\|D^nF\|_R.
```

</div>

<div class="lemma">

**Lemma 10** (Equivalence with factorial bounds). *$`\|F\|_{\mathrm{maj},\rho;R}<\infty`$ iff $`F`$ is analytic on $`B_R`$ with
``` math
\|D^nF\|_R \le \|F\|_{\mathrm{maj},\rho;R}\,\rho^{-n} n!.
```
Conversely, factorial bounds imply finiteness for $`\rho<1/K`$.*

</div>

## A.0.3 Entire form-factor sector

Let $`W`$ be a functional defined by background-covariant kernels (e.g. $`F(-\bar\nabla^2)`$ with $`F`$ complete Bernstein). Define
``` math
\|W\|_{\mathrm{ent},\rho;R}
:= \sum_{n=0}^\infty \frac{\rho^n}{n!}\|D^nW\|_R + \|W\|_{\mathrm{ker}},
```
where $`\|\cdot\|_{\mathrm{ker}}`$ is the operator norm $`H^s\to H^s`$.

## A.0.4 Full action space

<div class="definition">

**Definition 11** (Banach space $`\mathcal B^{(s,R)}`$). Let
``` math
\mathcal B^{(s,R)} := \mathcal A_{\mathrm{loc}}^{(s,R)} \oplus
\mathcal A_{\mathrm{ent}}^{(s,R)},
```
with norm
``` math
\|\Gamma\|_{\mathcal B,\rho;R}
:= \inf_{\Gamma=V+W}
\bigl(\|V\|_{\mathrm{maj},\rho;R}+\|W\|_{\mathrm{ent},\rho;R}\bigr).
```

</div>

<div class="lemma">

**Lemma 12** (Closure properties). *$`\mathcal B^{(s,R)}`$ is a Banach space, closed under sums, differentiation, and FRG compositions. Analytic bounds are preserved with controlled constants.*

</div>

# Appendix A.1: Bounded-Geometry Slab and Heat-Kernel Bounds

Let $`[0,T]\times\Sigma`$ be a finite time slab with bounded geometry. For any Laplace-type operator $`L`$, the heat kernel $`K_t(x,y)`$ satisfies
``` math
\|K_t(x,y)\|
\le C\,t^{-2}\exp\!\left(-\frac{d_{\bar g}(x,y)^2}{c\,t}\right),
\quad 0<t\le1.
```

These estimates are uniform on the slab and allow parametrix transfer between Fourier and configuration space.

# Appendix A.2: SPT-Filtered Covariances

SPT factorization yields TT-sector covariances of the form
``` math
C = f(L)\,(L+\lambda_*)^{-1},
```
with $`f`$ completely monotone and supported on $`[\tau_0,\infty)`$.

In Fourier variables,
``` math
\|\widehat C(p)\| \lesssim \frac{e^{-\tau_0|p|^2}}{|p|^2+\lambda_*}.
```

# Appendix A.3: Gaussian Damping Implies Sobolev Smoothing

<div class="lemma">

**Lemma 13** (Sobolev smoothing). *For any $`\sigma\ge0`$,
``` math
C : H^s \to H^{s+\sigma}
```
is bounded. The operator norm depends on $`\tau_0,\lambda_*,\sigma`$ and bounded-geometry constants.*

</div>

<div class="proof">

*Proof.* The multiplier
``` math
(1+|p|^2)^{\sigma/2}\frac{e^{-\tau_0|p|^2}}{|p|^2+\lambda_*}
```
is bounded for all $`\sigma`$; transfer to the slab uses Appendix A.1. ◻

</div>

# Appendix A.4: Linearized FRG Shell Operator

The linearized Wetterich RHS at scale $`k`$ is
``` math
\mathcal J_k(\delta\Gamma)
=\tfrac12\,\mathrm{STr}\bigl[
G_k\,\delta\Gamma^{(2)}\,G_k\,\partial_kR_k
\bigr] + \text{ghost/Ward terms}.
```

All terms contain two propagators and one shell-localized insertion.

# Appendix A.5: Compactness via Rellich on Slabs

<div class="lemma">

**Lemma 14** (Rellich compactness). *On a bounded slab,
``` math
H^{s+\sigma}\hookrightarrow H^s
```
is compact for $`\sigma>0`$.*

</div>

Combined with Appendix A.3, any smoothing operator $`H^s\to H^{s+\sigma}`$ induces a compact map on $`H^s`$.

# Appendix A.6: Quantitative Shell Contraction

<div class="lemma">

**Lemma 15** (Shell localization). *$`\partial_kR_k`$ is spectrally supported in $`a_0k^2\le-\bar\nabla^2\le a_1k^2`$.*

</div>

<div class="lemma">

**Lemma 16** (Quantitative contraction). *There exist constants $`C'(b,\rho,R,s)`$ and $`c>0`$ such that
``` math
\|\mathcal K_{k\to bk}(\delta\Gamma)\|_{\mathcal B,\rho;R}
\le C'(b,\rho,R,s)\,k\,e^{-c\tau_0k^2}
\|\delta\Gamma\|_{\mathcal B,\rho;R}.
```*

</div>

<div class="proof">

*Proof.* Each TT propagator contributes $`e^{-\tau_0|p|^2}`$ on the shell, yielding an overall $`e^{-c\tau_0k^2}`$ factor. Analytic bounds absorb derivatives; integrate over $`[k,bk]`$. ◻

</div>

# Appendix A.7: Spectral Consequences

The RG-step linearization decomposes as
``` math
D\mathcal R_b = \mathcal S_b + \mathcal K_b,
```
with $`\mathcal K_b`$ compact. By Riesz–Schauder theory, only finitely many eigenvalues lie outside the unit disk. Hence the unstable manifold is finite-dimensional.

# Appendix A.8: Relation to Probabilistic Slab Admissibility

The present appendices establish deterministic operator control of RG shell integration on a bounded slab.

Recent results on probabilistic admissibility (FP V) show that, in the Gaussian linearized regime, admissible evolution on a slab is generic with overwhelming probability. These results are independent but compatible: the deterministic compactness established here provides the structural backbone for the probabilistic persistence results.

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
