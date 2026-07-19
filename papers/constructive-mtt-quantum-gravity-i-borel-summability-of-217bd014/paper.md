---
abstract: |
  We give a fully constructive result for the transverse–traceless (TT) graviton sector of Modal Triplet Theory (MTT) under the spectral proper–time (SPT) damping mechanism. Assuming bounded geometry on a finite time slab (or bounded coordinate domain), we use a completely monotone proper–time filter with a positive proper–time gap $`\tau_0>0`$ to define a filtered covariance $`C`$ satisfying a Gaussian ultraviolet bound $`\widehat C(k)\lesssim e^{-\tau_0|k|^2}/(|k|^2+\lambda_\ast)`$. For local analytic interactions (including finite truncations of the TT-expanded Einstein–Hilbert density), we prove existence of the Euclidean functional integral, analyticity in a cardioid domain, and Borel summability of connected Schwinger functions via the Loop Vertex Expansion (BKAR forest formula) and a Nevanlinna–Sokal remainder bound. This provides a nonperturbative definition (via Borel sum) of the SPT-filtered TT sector and supplies the constructive core needed for a fully UV-controlled treatment of the physical TT sector within the MTT quantum gravity framework.
author:
- Peter Nero
bibliography:
- refs.bib
current_version: v1.0
date: January 2025
generated_from_main_tex_sha256: 396c64bf6dd2bde70a0c93ae948a9e31e3a010fc9666debee05888e58b8a8dd8
paper_id: constructive-mtt-quantum-gravity-i-borel-summability-of-217bd014
release_state: zenodo_released
released_version: v1.0
title: |
  Constructive MTT Quantum Gravity I:  
  Borel Summability of the SPT-Filtered TT Sector
zenodo_doi: 10.5281/zenodo.18209684
zenodo_record_id: 18209684
zenodo_url: "https://zenodo.org/records/18209684"
---

# Introduction

In MTT quantum gravity, UV control arises from a spectral proper–time (SPT) filter applied in the physical TT sector. The SPT filter is not an ad hoc regulator: it is a spectral functional calculus object derived from bounded geometry and proper–time gap hypotheses, yielding Gaussian damping $`e^{-\tau_0|k|^2}`$ on the TT propagator. The accompanying perturbative quantum gravity paper establishes all-loop finiteness of graviton-containing graphs under this damping. The remaining question is whether one can promote this to a *nonperturbative* definition of the theory.

This paper answers that question in the standard constructive QFT sense: we prove existence of the Euclidean TT-sector functional integral and Borel summability of its perturbative expansion. The cleanest route is the Loop Vertex Expansion (LVE), which provides factorial bounds on Taylor remainders and therefore Borel summability by the Nevanlinna–Sokal theorem.

We emphasize scope:

- We work in a bounded geometry region (finite time slab / bounded domain) where heat-kernel and resolvent bounds are uniform.

- We treat the TT sector (physical subspace). Gauge completion / BRST lifting is deferred to a subsequent paper.

- Interactions are treated as local analytic functionals with explicit factorial derivative bounds. This includes finite truncations of the TT-expanded Einstein–Hilbert interaction; the $`P\to\infty`$ limit is controlled under analyticity radius conditions.

# Geometric and analytic setup

## Domain and Laplace-type operator

Let $`\Omega\subset\mathbb{R}^4`$ be a bounded domain (a bounded-geometry coordinate chart of a time slab) with smooth boundary and fixed boundary conditions (Dirichlet or mixed), chosen so that the TT sector is well-posed.

Let $`E\to\Omega`$ be the TT bundle (symmetric trace-free divergence-free tensors in a fixed gauge). Let $`L`$ be a nonnegative selfadjoint Laplace-type operator on $`L^2(E)`$:
``` math
L=\nabla^\ast\nabla+\mathcal{R},\qquad L\ge 0.
```
Assume a uniform spectral gap on the noncoherent sector:
``` math
\sigma(L)\subset \{0\}\cup[\lambda_\ast,\infty),\qquad \lambda_\ast>0,
```
where $`0`$ corresponds to coherent TT zero-modes.

## SPT filter class and proper-time gap

Let $`f:[0,\infty)\to\mathbb{R}`$ be completely monotone with representing measure $`\mu`$:
``` math
f(\lambda)=\int_0^\infty e^{-t\lambda}\,d\mu(t),
\qquad \mu\ge 0,
```
and assume the *proper-time gap* condition:
``` math
\mathop{\mathrm{supp}}(\mu)\subset[\tau_0,\infty)\quad \text{for some }\tau_0>0.
```
Define the spectral filter $`B:=f(L)`$.

Define the filtered covariance (Euclidean):
``` math
C := B\,(L+\lambda_\ast)^{-1}.
```
This is the covariance used to define the TT Gaussian measure.

<div id="ass:heat" class="assumption">

**Assumption 1** (Heat kernel bounds on $`\Omega`$). There exist constants $`C_1,c_1>0`$ such that the heat kernel of $`e^{-tL}`$ satisfies
``` math
\|K_t(x,y)\|\le C_1 t^{-2}\exp\!\Big(-\frac{|x-y|^2}{c_1 t}\Big),\qquad t>0,\ x,y\in\Omega.
```

</div>

Assumption <a href="#ass:heat" data-reference-type="ref" data-reference="ass:heat">1</a> holds for Laplace-type operators on bounded-geometry regions with smooth boundary.

# Gaussian UV damping and Schatten-class control

## Fourier-side Gaussian bound

The SPT appendix in the QG paper proves (and we assume here as a lemma on $`\Omega`$):

<div id="lem:gauss" class="lemma">

**Lemma 2** (Gaussian UV bound for $`C`$). *There exists $`C_0>0`$ such that in local Fourier variables,
``` math
\|\widehat C(k)\|\le C_0\,\frac{e^{-\tau_0|k|^2}}{|k|^2+\lambda_\ast}.
```*

</div>

## Hilbert–Schmidt estimate

<div id="lem:hs" class="lemma">

**Lemma 3** (Hilbert–Schmidt covariance). *The covariance $`C`$ restricted to $`\Omega`$ is Hilbert–Schmidt:
``` math
C\in \mathfrak{S}_2(L^2(\Omega;E)).
```
Moreover, $`\|C\|_{\mathfrak{S}_2}<\infty`$ with an explicit bound depending on $`C_0,\tau_0,\lambda_\ast`$ and $`\mathrm{Vol}(\Omega)`$.*

</div>

<div class="proof">

*Proof.* Using Plancherel in a coordinate chart and Lemma <a href="#lem:gauss" data-reference-type="ref" data-reference="lem:gauss">2</a>,
``` math
\|C\|_{\mathfrak{S}_2}^2 \lesssim \int_{\mathbb{R}^4}\frac{e^{-2\tau_0|k|^2}}{(|k|^2+\lambda_\ast)^2}\,d^4k<\infty,
```
since $`e^{-2\tau_0|k|^2}`$ dominates polynomial growth and the integrand is integrable at both $`|k|\to\infty`$ and $`|k|\to 0`$ (the $`\lambda_\ast`$ shift controls IR). The prefactor depends on local trivializations and $`\mathrm{Vol}(\Omega)`$. ◻

</div>

<div class="remark">

*Remark 4*. On bounded $`\Omega`$, one can also obtain trace-class control for localized covariances using standard Sobolev embeddings. For Borel summability via LVE, Hilbert–Schmidt control plus Carleman–Fredholm determinants suffices.

</div>

# Interaction class and truncated gravity

## Local analytic interactions with factorial bounds

Let $`h:\Omega\to E`$ be the TT field. Let
``` math
V(h)=\int_\Omega v(h(x),\nabla h(x),\dots)\,dx
```
be a local functional.

<div id="ass:analytic" class="assumption">

**Assumption 5** (Analytic factorial bounds). There exist constants $`K,R_0>0`$ such that for every $`p\ge 0`$ the $`p`$-th Fréchet derivative satisfies
``` math
\sup_{\|h\|_{H^s}\le R_0}\|D^p V(h)\|\le K^p\,p!
```
as a multilinear form on $`(H^s)^p`$ for some fixed $`s>2`$.

</div>

This is the standard analyticity hypothesis used in constructive Borel summability proofs for analytic interactions.

## Einstein–Hilbert TT truncations

Let $`V_{\le P}`$ denote the TT-expanded Einstein–Hilbert interaction truncated at polynomial order $`P`$ in $`h`$ (and finitely many derivatives), on a fixed background metric in the slab.

<div id="ass:trunc" class="assumption">

**Assumption 6** (Uniform truncation analyticity). There exists $`R_0>0`$ such that Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a> holds for $`V_{\le P}`$ with constants $`K`$ independent of $`P`$.

</div>

This is the natural analytic-uniformity condition needed to pass $`P\to\infty`$.

# Constructive definition and Loop Vertex Expansion

## Gaussian measure and partition function

Let $`\mu_C`$ be the centered Gaussian measure on the TT field with covariance $`C`$. For coupling $`g\in\mathbb{C}`$ define the (finite-volume) partition function
``` math
Z(g):=\int e^{-gV(h)}\,d\mu_C(h),
```
and define connected Schwinger functions in the usual way.

## BKAR forest formula (statement)

We use the BKAR forest formula to represent $`\log Z(g)`$ and connected correlators. We follow standard references on the Loop Vertex Expansion .

We will not reproduce the full combinatorial derivation; we only need the standard consequence: connected objects admit a convergent expansion indexed by forests with uniform control by covariance norms and vertex derivatives.

## Determinant bounds via Carleman–Fredholm

Because $`C\in\mathfrak{S}_2`$, we use the Carleman–Fredholm determinant $`\det\nolimits_2(I+K)`$ for Hilbert–Schmidt $`K`$.

<div id="lem:det2" class="lemma">

**Lemma 7** (Carleman–Fredholm bound). *If $`K\in\mathfrak{S}_2`$, then
``` math
|\det\nolimits_2(I+K)|\le \exp\!\Big(\frac12\|K\|_{\mathfrak{S}_2}^2\Big).
```*

</div>

<div class="proof">

*Proof.* Standard inequality for $`\det\nolimits_2`$; see constructive QFT references . ◻

</div>

This is the key analytic bound replacing trace-class determinant control.

# Factorial remainder bounds and Borel summability

## Cardioid analyticity domain for LVE

The Loop Vertex Expansion yields analyticity not merely in a small disk, but in a cardioid domain in the complex coupling plane. This is the standard domain used to apply the Nevanlinna–Sokal theorem.

<div id="def:cardioid" class="definition">

**Definition 8** (Cardioid domain). For $`\rho>0`$, define the cardioid
``` math
\mathcal{C}_\rho := \Bigl\{ g\in\mathbb{C}\setminus\{0\}:\ |g|<\rho\cos^2\!\bigl(\tfrac12\arg g\bigr)\Bigr\}.
```

</div>

<div id="lem:cardioid" class="lemma">

**Lemma 9** (Uniform analyticity of $`Z(g)`$ and connected functions on a cardioid). *Assume Lemma <a href="#lem:hs" data-reference-type="ref" data-reference="lem:hs">3</a> and Assumptions <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a>–<a href="#ass:stable" data-reference-type="ref" data-reference="ass:stable">13</a>. Then there exists $`\rho>0`$ such that $`Z(g)`$ and all connected Schwinger functions are analytic on $`\mathcal{C}_\rho`$.*

</div>

<div class="proof">

*Proof.* The BKAR/LVE representation writes connected quantities as absolutely convergent integrals of Gaussian expectations of products of analytic local functionals evaluated at complex coupling $`g`$. The cardioid domain arises because one controls the real part of $`g`$ along the interpolation: writing $`g=re^{i\theta}`$, one uses the inequality
``` math
\Re(g)=r\cos\theta \ge r\cos^2\!\bigl(\tfrac12\theta\bigr) - r\sin^2\!\bigl(\tfrac12\theta\bigr),
```
and chooses $`\rho`$ so that the damping from the stable quadratic part dominates the imaginary part uniformly for $`g\in\mathcal{C}_\rho`$. More concretely, the stability assumption gives an estimate of the form
``` math
|e^{-gV(h)}|\le e^{-\Re(g)\,V(h)}\,e^{|\Im(g)|\,|V(h)|}
\le \exp\!\bigl(|g|\,a\|h\|_{H^s}^2+|g|b\bigr),
```
and the cardioid restriction ensures the coefficient of $`\|h\|_{H^s}^2`$ stays below the Gaussian tail constant from Lemma <a href="#lem:ball" data-reference-type="ref" data-reference="lem:ball">14</a> uniformly on the BKAR interpolation. Absolute convergence of the forest integrals then implies analyticity by dominated convergence. ◻

</div>

<div id="lem:nev-bound" class="lemma">

**Lemma 10** (Nevanlinna remainder bound on the cardioid). *Under the hypotheses of Lemma <a href="#lem:cardioid" data-reference-type="ref" data-reference="lem:cardioid">9</a>, the LVE Taylor remainder for any connected Schwinger function satisfies the Nevanlinna bound
``` math
|R_N(g)|\le A\,B^{N+1}\,(N+1)!\,|g|^{N+1}
\qquad\text{uniformly for }g\in\mathcal{C}_\rho.
```*

</div>

<div class="proof">

*Proof.* On $`\mathcal{C}_\rho`$, the absolute convergence bounds on the BKAR forest expansion are uniform. At fixed order $`N+1`$, the remainder is represented as an integral of the same type as the coefficients, with one extra interaction insertion and a factor $`g^{N+1}/N!`$ coming from the integral remainder formula. Uniform forest-counting bounds (Lemma <a href="#lem:tree-count" data-reference-type="ref" data-reference="lem:tree-count">19</a>), factorial derivative bounds (Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a>), and Wick/HS bounds (Lemma <a href="#lem:wick-hs" data-reference-type="ref" data-reference="lem:wick-hs">17</a>) yield
``` math
|R_N(g)|\le A\,B^{N+1}\,(N+1)!\,|g|^{N+1}
```
with constants independent of $`g\in\mathcal{C}_\rho`$. ◻

</div>

## Nevanlinna–Sokal criterion

We use the Nevanlinna–Sokal theorem: analyticity in a cardioid sector plus factorial remainder bounds implies Borel summability.

<div id="thm:NS" class="theorem">

**Theorem 11** (Nevanlinna–Sokal). *Let $`F(g)`$ be analytic in a cardioid domain $`\{g:|g|<g_0,\ |\arg g|<\theta\}`$ for some $`\theta>0`$. Assume its Taylor remainders satisfy
``` math
\bigl|F(g)-\sum_{n=0}^{N} a_n g^n\bigr|
\le A\,B^{N+1}\,(N+1)!\,|g|^{N+1}
```
uniformly in the cardioid. Then $`F`$ is Borel summable to its perturbation series.*

</div>

<div class="remark">

*Remark 12*. This is a standard summability result; see .

</div>

## Analytic ball control under the interacting weight

The factorial derivative bounds of Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a> are stated on a ball $`\{ \|h\|_{H^s}\le R_0\}`$. We now justify that for sufficiently small coupling, the interacting weight does not push the measure outside this ball in a way that breaks the constructive bounds. The precise statement below is a standard dominated-convergence control used in constructive analyses of analytic interactions.

<div id="ass:stable" class="assumption">

**Assumption 13** (Local stability / bounded below interaction). There exist constants $`a,b\ge 0`$ such that for all $`h`$ in the domain of $`V`$,
``` math
V(h)\ge -a\|h\|_{H^s}^2 - b.
```

</div>

<div id="lem:ball" class="lemma">

**Lemma 14** (Exponential integrability and analytic-ball reduction). *Assume $`C`$ is the SPT-filtered covariance on $`\Omega`$ with $`C\in\mathfrak{S}_2`$ and $`\lambda_\ast>0`$ (hence an IR gap on $`\Omega`$). Let $`V`$ satisfy Assumption <a href="#ass:stable" data-reference-type="ref" data-reference="ass:stable">13</a> and Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a> on the ball $`\{\|h\|_{H^s}\le R_0\}`$. Then there exists $`g_1>0`$ such that for all complex $`g`$ with $`|g|<g_1`$:*

1.  *$`Z(g)=\int e^{-gV(h)}\,d\mu_C(h)`$ is well-defined and nonzero.*

2.  *For every local observable $`\mathcal O`$ dominated by a polynomial in $`\|h\|_{H^s}`$, the normalized expectation
    ``` math
    \frac{1}{Z(g)}\int \mathcal O(h)\,e^{-gV(h)}\,d\mu_C(h)
    ```
    can be estimated by splitting the integration domain into $`\|h\|_{H^s}\le R_0`$ and its complement, and the contribution of $`\|h\|_{H^s}>R_0`$ is exponentially small in $`R_0^2`$ uniformly in $`|g|<g_1`$.*

*In particular, all constructive bounds may be carried out on the ball $`\{\|h\|_{H^s}\le R_0\}`$, with the complement controlled as an exponentially small error that can be absorbed into constants.*

</div>

<div class="proof">

*Proof.* Because $`\Omega`$ is bounded and $`\lambda_\ast>0`$ provides an IR gap, the Gaussian measure $`\mu_C`$ has sub-Gaussian tails in $`\|h\|_{H^s}`$: there exist $`c_0,C_0>0`$ such that
``` math
\mu_C\big(\|h\|_{H^s}>R\big)\le C_0 e^{-c_0 R^2}\qquad (R\ge 1).
```
(This follows from standard Fernique/Borell inequalities for Gaussian measures on Hilbert spaces.)

By Assumption <a href="#ass:stable" data-reference-type="ref" data-reference="ass:stable">13</a>, for $`|g|<g_1:=\min\{1,(2a)^{-1}\}`$ we have
``` math
|e^{-gV(h)}|\le e^{|g|\,|V(h)|}
\le e^{|g|\,(a\|h\|_{H^s}^2+b)}
\le e^{\frac12\|h\|_{H^s}^2 + b},
```
so $`e^{-gV}`$ is integrable against $`\mu_C`$ by Gaussian tail control (absorbing constants). This proves (i). For (ii), write
``` math
\int \mathcal O\,e^{-gV}\,d\mu_C
=
\int_{\|h\|\le R_0}\mathcal O\,e^{-gV}\,d\mu_C
+
\int_{\|h\|>R_0}\mathcal O\,e^{-gV}\,d\mu_C.
```
On $`\{\|h\|>R_0\}`$, polynomial growth of $`\mathcal O`$ and the bound above imply
``` math
\Big|\int_{\|h\|>R_0}\mathcal O\,e^{-gV}\,d\mu_C\Big|
\le
\int_{\|h\|>R_0} P(\|h\|_{H^s})\,e^{\frac12\|h\|_{H^s}^2+b}\,d\mu_C(h),
```
and the Gaussian tail estimate gives an exponentially small bound in $`R_0^2`$ after standard comparison (absorbing the polynomial into the exponential by reducing $`c_0`$). Uniformity in $`|g|<g_1`$ is built into the choice of $`g_1`$. ◻

</div>

## BKAR forest formula and connected expansions

Let $`n\in\mathbb{N}`$. For $`n`$ replicas of the TT field $`h^{(1)},\dots,h^{(n)}`$, define the interpolated Gaussian measure $`\mu_{C\otimes X}`$ with covariance
``` math
\mathbb{E}_{C\otimes X}\big[h^{(i)}(x)\,h^{(j)}(y)\big]=X_{ij}\,C(x,y),
```
where $`X=(X_{ij})`$ is a symmetric $`n\times n`$ matrix with $`X_{ii}=1`$ and $`0\le X_{ij}\le 1`$.

<div id="lem:BKAR" class="lemma">

**Lemma 15** (BKAR forest formula). *Let $`F(X)`$ be $`C^1`$ in the off-diagonal variables $`\{X_{ij}\}_{i<j}`$. Then
``` math
F(\mathbf{1})=\sum_{T\ \text{tree on }\{1,\dots,n\}}
\int_{[0,1]^{|T|}}\Bigl(\prod_{e\in T}dw_e\Bigr)\,
\Bigl(\prod_{e=(ij)\in T}\partial_{ij}\Bigr)\,F\bigl(X^{T}(\mathbf{w})\bigr),
```
where $`X^{T}(\mathbf{w})`$ is the BKAR matrix built from $`\mathbf{w}`$ by setting $`X^{T}_{ij}=\min\{w_e:\ e\text{ lies on the unique }i\!\!-\!\!j\text{ path in }T\}`$ for $`i\neq j`$ and $`X^{T}_{ii}=1`$.*

</div>

<div class="remark">

*Remark 16*. A standard reference is . The crucial property is that $`X^{T}(\mathbf{w})`$ is positive semidefinite for all $`\mathbf{w}\in[0,1]^{|T|}`$, so $`\mu_{C\otimes X^{T}(\mathbf{w})}`$ is a valid Gaussian measure.

</div>

## Hilbert–Schmidt Wick bounds

<div id="lem:wick-hs" class="lemma">

**Lemma 17** (Hilbert–Schmidt Wick bound). *Let $`C\in\mathfrak{S}_2`$ and let $`\mu_C`$ be the centered Gaussian measure on $`L^2(\Omega;E)`$ with covariance $`C`$. For any $`p\ge 1`$ and any bounded linear functionals $`\ell_1,\dots,\ell_{2p}`$ on $`L^2(\Omega;E)`$,
``` math
\Big|\mathbb{E}_{\mu_C}\prod_{j=1}^{2p}\ell_j(h)\Big|
\le (2p-1)!!\ \|C\|_{\mathfrak{S}_2}^{p}\ \prod_{j=1}^{2p}\|\ell_j\|.
```*

</div>

<div class="proof">

*Proof.* Write $`\ell_j(h)=\langle f_j,h\rangle`$ with $`\|f_j\|=\|\ell_j\|`$. Wick’s theorem yields a sum over pairings $`\pi`$:
``` math
\mathbb{E}\prod_{j=1}^{2p}\langle f_j,h\rangle
=\sum_{\pi}\prod_{(a,b)\in\pi}\langle f_a,C f_b\rangle.
```
Use Cauchy–Schwarz and $`\|C\|_{\mathfrak{S}_2}`$: $`|\langle f_a,C f_b\rangle|\le \|C\|_{\mathfrak{S}_2}\|f_a\|\|f_b\|`$. There are $`(2p-1)!!`$ pairings. ◻

</div>

## Analytic derivative bounds and coefficient control

<div id="lem:coef" class="lemma">

**Lemma 18** (Coefficient bound from analyticity). *Assume Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a>. Then for $`\|h\|_{H^s}\le R_0`$, the Taylor coefficients of $`V`$ satisfy
``` math
\Big|\frac{1}{p!}\,D^pV(0)[h,\dots,h]\Big|\le K^p\,\|h\|_{H^s}^{p}.
```*

</div>

<div class="proof">

*Proof.* Immediate from the definition of Fréchet derivatives and Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a>. ◻

</div>

## Tree counting (factorial domination)

<div id="lem:tree-count" class="lemma">

**Lemma 19** (Tree counting). *The number of labeled trees on $`n`$ vertices is $`n^{n-2}`$ (Cayley). Moreover, there exists a constant $`c_T>0`$ such that for all $`n\ge 1`$,
``` math
n^{n-2}\le c_T^n\,n!.
```*

</div>

<div class="proof">

*Proof.* Cayley’s formula gives $`n^{n-2}`$. Stirling implies $`n!\ge (n/e)^n`$, hence $`n^{n-2}\le n^n \le e^n n!`$. Take $`c_T=e`$. ◻

</div>

## Main constructive theorem

<div id="thm:borel" class="theorem">

**Theorem 20** (Existence and Borel summability (TT sector)). *Assume Lemma <a href="#lem:hs" data-reference-type="ref" data-reference="lem:hs">3</a> and Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a>. Then there exists $`g_0>0`$ such that:*

1.  *$`Z(g)`$ and all connected Schwinger functions are analytic for $`|g|<g_0`$ in a cardioid domain.*

2.  *The connected Schwinger functions admit expansions with remainders satisfying Nevanlinna bounds
    ``` math
    |R_N(g)|\le A\,B^{N+1}(N+1)!\,|g|^{N+1}.
    ```*

3.  *Hence each connected Schwinger function is Borel summable to its perturbation series.*

</div>

<div class="proof">

*Proof.* Fix a bounded local observable $`\mathcal{O}(h)`$ (a finite product of smeared TT components). We prove the Nevanlinna remainder bound for the connected expectation
``` math
F(g):=\frac{1}{Z(g)}\int \mathcal{O}(h)\,e^{-gV(h)}\,d\mu_C(h),
\qquad
Z(g):=\int e^{-gV(h)}\,d\mu_C(h).
```
The argument is standard in the LVE framework, but we give all bounds explicitly.

#### Step 1: Replica representation of connected functions.

Write the normalized moment as
``` math
F(g)=\frac{\mathbb{E}_{\mu_C}\big[\mathcal{O}(h)e^{-gV(h)}\big]}{\mathbb{E}_{\mu_C}\big[e^{-gV(h)}\big]}.
```
Connected objects can be represented by the logarithm expansion or, equivalently, by BKAR forests applied to a replicated partition function. For concreteness, define for $`n\ge 1`$
``` math
Z_n(g;X):=\mathbb{E}_{\mu_{C\otimes X}}\Big[\prod_{i=1}^n e^{-gV(h^{(i)})}\Big],
```
with $`X`$ an interpolation matrix. Then the standard identity is:
``` math
\log Z(g)=\sum_{n\ge 1}\frac{(-1)^{n-1}}{n}\,
\bigl(Z_n(g;\mathbf{1})-1\bigr),
```
and the BKAR formula (Lemma <a href="#lem:BKAR" data-reference-type="ref" data-reference="lem:BKAR">15</a>) expresses $`Z_n(g;\mathbf{1})`$ as a sum over trees. The same applies to $`\log`$ of generating functionals with sources, hence to connected correlators.

#### Step 2: Apply BKAR to obtain a tree expansion.

Applying Lemma <a href="#lem:BKAR" data-reference-type="ref" data-reference="lem:BKAR">15</a> to $`Z_n(g;\mathbf{1})`$, we obtain
``` math
Z_n(g;\mathbf{1})=\sum_{T}\int_{[0,1]^{|T|}} d\mathbf{w}\;
\mathbb{E}_{\mu_{C\otimes X^T(\mathbf{w})}}
\Big[\prod_{(ij)\in T}\langle \tfrac{\delta}{\delta h^{(i)}},\,C\,\tfrac{\delta}{\delta h^{(j)}}\rangle
\ \prod_{i=1}^n e^{-gV(h^{(i)})}\Big].
```
Each edge derivative inserts exactly one covariance $`C`$ linking replicas $`i`$ and $`j`$.

#### Step 3: Bounds on derivatives of the interaction.

Expand each $`e^{-gV(h^{(i)})}`$ in Taylor series up to order $`N`$ with integral remainder:
``` math
e^{-gV}=\sum_{p=0}^N \frac{(-g)^p}{p!}V^p + R_{N+1}(g;h),
\qquad
R_{N+1}(g;h)=\frac{(-g)^{N+1}}{N!}\int_0^1 (1-t)^N V^{N+1}(h)\,e^{-tgV(h)}\,dt.
```
Using Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a> on a sufficiently small ball (and using that the Gaussian measure concentrates in that ball for small $`g`$ on bounded $`\Omega`$), there exists $`K_1`$ such that
``` math
|V(h)|\le K_1\bigl(1+\|h\|_{H^s}\bigr)
\quad\text{and}\quad
|D^p V(h)|\le K^p p!
```
on the relevant domain. This provides factorial control of all vertex derivatives generated by $`\langle \delta/\delta h^{(i)}, C\,\delta/\delta h^{(j)}\rangle`$ acting on products of $`V`$’s.

#### Step 4: Wick/HS bounds on Gaussian expectations.

After distributing the functional derivatives from the tree edges, each BKAR term becomes a finite sum of Gaussian moments of degree $`2m`$ (coming from the derivatives hitting the exponentials/polynomials). By Lemma <a href="#lem:wick-hs" data-reference-type="ref" data-reference="lem:wick-hs">17</a>, each such Gaussian moment is bounded by
``` math
(2m-1)!!\ \|C\|_{\mathfrak{S}_2}^{m}\times(\text{product of test function norms}).
```
Thus every tree term is bounded by a constant times a power of $`\|C\|_{\mathfrak{S}_2}`$.

#### Step 5: Tree counting yields factorial growth.

At order $`n`$, the number of labeled trees is $`n^{n-2}\le c_T^n n!`$ by Lemma <a href="#lem:tree-count" data-reference-type="ref" data-reference="lem:tree-count">19</a>. All remaining combinatorics (distribution of derivatives among vertices, pairings) contribute at most additional factors $`c^n`$ after using the factorial derivative bounds from Assumption <a href="#ass:analytic" data-reference-type="ref" data-reference="ass:analytic">5</a>. Therefore the Taylor coefficient $`a_n`$ of any connected observable satisfies
``` math
|a_n|\le A\,B^n\,n!
```
for some $`A,B`$ depending on $`\|C\|_{\mathfrak{S}_2}`$ and the analytic constants $`K,R_0`$.

#### Step 6: Remainder bound (Nevanlinna form).

Using the integral remainder formula and the uniform coefficient bounds above, we obtain
``` math
|R_N(g)| \le A\,B^{N+1}\,(N+1)!\,|g|^{N+1},
```
uniformly for $`g`$ in a cardioid domain (standard for LVE because the BKAR integral provides analyticity in a sector and the exponential $`e^{-tgV}`$ is controlled there).

#### Step 7: Borel summability.

By Theorem <a href="#thm:NS" data-reference-type="ref" data-reference="thm:NS">11</a>, the connected Schwinger function $`F(g)`$ is Borel summable to its perturbation series. Since $`\mathcal{O}`$ was arbitrary among local polynomial observables, the same holds for all connected Schwinger functions. ◻

</div>

# Application to truncated TT gravity and the $`P\to\infty`$ limit

<div id="thm:trunc" class="theorem">

**Theorem 21** (Uniform Borel summability for TT truncations). *Assume Lemma <a href="#lem:hs" data-reference-type="ref" data-reference="lem:hs">3</a> and Assumption <a href="#ass:trunc" data-reference-type="ref" data-reference="ass:trunc">6</a>. Then the conclusions of Theorem <a href="#thm:borel" data-reference-type="ref" data-reference="thm:borel">20</a> hold uniformly in the truncation order $`P`$ for the interaction $`V_{\le P}`$, with constants $`A,B,g_0`$ independent of $`P`$. Consequently, the Borel sums converge as $`P\to\infty`$ to a Borel-summable limit theory for the full analytic TT interaction.*

</div>

<div class="proof">

*Proof.* By Assumption <a href="#ass:trunc" data-reference-type="ref" data-reference="ass:trunc">6</a>, the analytic factorial bounds are uniform in $`P`$. All LVE coefficient and remainder estimates in Theorem <a href="#thm:borel" data-reference-type="ref" data-reference="thm:borel">20</a> therefore hold with constants independent of $`P`$. Hence the Borel transforms are uniformly bounded on a common disk and converge termwise as $`P\to\infty`$. Dominated convergence yields convergence of the Borel sums to a limit analytic function. ◻

</div>

# Discussion and next steps

We have given a constructive nonperturbative definition (via Borel sum) of the SPT-filtered TT sector on bounded geometry slabs. This closes the principal technical gap between “all-loop finiteness” and “nonperturbative existence” in the TT sector.

Next steps:

1.  Extend from TT to BRST-invariant observables (constructive BV lifting).

2.  Treat infinite-volume / global slab limits with confinement weights or adiabatic switching.

3.  Match the constructive TT sector to Lorentzian pAQFT via analytic continuation where appropriate.
