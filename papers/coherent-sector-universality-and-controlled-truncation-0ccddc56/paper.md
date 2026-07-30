---
abstract: |
  A coherent-sector truncation is controlled only after the retained subspace, the full closed operator, its block domains, the spectral parameter, the eliminated-sector resolvent, and the comparison norm have all been specified. A spectral gap by itself is not a complete truncation theorem.

  This paper gives a domain-explicit coherent-sector reduction for a self-adjoint block operator on $`\mathcal H=\mathcal H_P\oplus\mathcal H_Q`$. It first resolves a basic ambiguity: if $`P`$ is the exact spectral projector of the same operator $`T`$, then $`P`$ reduces $`T`$, the off-diagonal blocks vanish, and the truncation is exact. A nonzero Feshbach correction therefore requires a projector selected from a reference operator, symmetry, Galerkin space, or approximate coherent criterion.

  For such a reference-selected projector, write
  ``` math
  T=
   \begin{pmatrix}A&B\\ C&D\end{pmatrix}.
  ```
  At every declared $`z\in\rho(D)`$, the exact reduced operator is the Feshbach–Schur map
  ``` math
  F_T(z)=A-z-B(D-z)^{-1}C.
  ```
  The omitted-sector self-energy obeys the actual product estimate
  ``` math
  \|B(D-z)^{-1}C\|
   \leq
   \|B\|\,\|(D-z)^{-1}\|\,\|C\|,
  ```
  and, for self-adjoint $`D`$, the middle factor is $`\operatorname{dist}(z,\operatorname{spec}D)^{-1}`$. We prove the corresponding inverse formula, give a two-mode example, derive Riesz-projector stability under bounded perturbations, and establish a local operator-norm robustness bound with all block variations shown explicitly.

  These results define a controlled local class, not a global universality theorem. Resolvent closeness does not imply uniform-in-time dynamical closeness, graph-norm or form robustness requires separate hypotheses, and an internal one-parameter unitary is not physical time without a model-specific clock and intertwining theorem. The result is a rigorous methods paper and an executable certificate format for future Modal Triplet Theory reductions.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: a64dbb79461e71fbafa2b1f902a357f07595615f3d78f52c48292b8af40aa048
paper_id: coherent-sector-universality-and-controlled-truncation-0ccddc56
release_state: zenodo_released
released_version: v2
title: |
  Coherent-Sector Reduction in Modal Triplet Theory:
  Feshbach Control, Projector Stability, and Local Universality
zenodo_doi: 10.5281/zenodo.21710429
zenodo_record_id: 21710429
zenodo_url: "https://zenodo.org/records/21710429"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1.0, DOI [10.5281/zenodo.18261354](https://doi.org/10.5281/zenodo.18261354).

Version 1 left the block domains and spectral parameter implicit, used $`(QTQ)^{-1}`$ without a stated resolvent condition, replaced the exact off-diagonal resolvent product by a schematic $`\|\delta T\|^2/\Delta`$, called generic commutator bounds “bounded geometry,” and promoted local projector stability to broad physical universality and emergent time.

The revision distinguishes an exact spectral projector from a reference-selected projector; defines a closed block-operator problem; states and proves the Feshbach inverse formula at $`z\in\rho(D)`$; derives the exact product, resolvent-distance, Riesz-projector, and block-variation bounds; identifies the norm in every robustness statement; and separates spectral reduction from time-domain dynamics and physical clock interpretation.

The useful claim survives locally: a selected low sector can be a controlled effective description when the eliminated block has a certified resolvent region and the off-diagonal couplings are quantitatively small there.

Modal Triplet Theory does not yet provide one universal continuum operator, coherent projector, physical clock, or connection-preserving transfer theorem to which this abstract certificate applies across all encodings. Those are model-specific source obligations.

</div>

# The corrected question

The original question was:

> When may the full internal description be replaced by a smaller coherent sector without losing the behavior relevant to a declared calculation?

The answer depends on what “behavior” means. A resolvent, a spectral cluster, a finite-time unitary, a semigroup, a quadratic form, and a list of observables require different estimates. No single gap statement controls all of them automatically.

This paper treats the resolvent and spectral-projector problem first. It uses standard Feshbach–Schur and perturbation theory . The Modal Triplet Theory contribution is a typed certificate that records exactly which version of this standard mathematics is being used and prevents a local reduction from being promoted to a universal physical claim.

## The six objects that must be distinguished

1.  A *reference operator* $`G`$ may be used to identify a candidate coherent subspace.

2.  An orthogonal projector $`P`$ selects that subspace; $`Q=\mathbf 1-P`$.

3.  The *full operator* $`T`$ is the object actually being reduced.

4.  A spectral parameter $`z`$ specifies the resolvent problem.

5.  A comparison norm states the sense in which the reduction is controlled.

6.  A physical interpretation map states whether the reduced parameter describes energy, modular flow, Euclidean evolution, or physical time.

If $`G=T`$ and $`P`$ is an exact spectral projector of $`T`$, the reduction has no off-diagonal correction. If $`P`$ is selected from $`G\neq T`$, a finite basis, or another coherent criterion, the coupling to $`Q\mathcal H`$ must be measured.

## What is not claimed

The paper does not prove that:

- every Modal Triplet Theory encoding has a common coherent projector;

- a finite projected operator converges to a selected continuum operator;

- operator-norm robustness implies graph-norm, form, or semigroup robustness;

- a resolvent approximation is uniformly accurate for arbitrary evolution times;

- the internal generator is a physical Hamiltonian; or

- distinct compactifications or microscopic theories are physically equivalent merely because one reduced block is close.

# Why an exact spectral projector gives no correction

Let $`T`$ be self-adjoint on a dense domain $`\mathcal D(T)\subset\mathcal H`$. Its spectral measure is denoted by $`E_T(\cdot)`$.

<div id="prop:reducing" class="proposition">

**Proposition 1** (Exact spectral projectors reduce their operator). *For every Borel set $`I\subset\mathbb R`$, the projector $`P=E_T(I)`$ preserves $`\mathcal D(T)`$, commutes with $`T`$ on $`\mathcal D(T)`$, and satisfies
``` math
PTQ=0,
  \qquad
  QTP=0,
  \qquad Q=\mathbf 1-P.
```
Consequently
``` math
T=T_P\oplus T_Q
```
on $`P\mathcal H\oplus Q\mathcal H`$, and truncation to the exact spectral subspace has zero Feshbach self-energy.*

</div>

<div class="proof">

*Proof.* The spectral functional calculus gives $`E_T(I)E_T(J)=E_T(I\cap J)`$ and
``` math
T=\int_{\mathbb R}\lambda\,\mathrm dE_T(\lambda).
```
Hence $`P`$ commutes with every bounded spectral function and preserves the domain defined by $`\int\lambda^2\,\mathrm d\langle E_T(\lambda)x,x\rangle<\infty`$. Thus $`PTx=TPx`$ for $`x\in\mathcal D(T)`$. Since $`PQ=0`$, $`PTQ=TPQ=0`$, and similarly $`QTP=0`$. The direct-sum statement follows. ◻

</div>

This proposition exposes a hidden circularity in many informal reduction arguments. One cannot simultaneously define $`P`$ as the exact spectral projector of $`T`$ and then estimate a nonzero coupling $`PTQ`$. To obtain a nontrivial reduction, at least one of the following must be true:

1.  $`P`$ is spectral for a reference operator $`G`$, while $`T=G+V`$;

2.  $`P`$ is a Galerkin or finite-element projector;

3.  $`P`$ is selected by symmetry, topology, localization, or another criterion not reducing $`T`$; or

4.  $`P`$ approximates, rather than equals, the target spectral projector.

The source and status of $`P`$ are therefore part of every truncation certificate.

# The closed block-operator problem

Fix an orthogonal decomposition
``` math
\mathcal H=\mathcal H_P\oplus\mathcal H_Q,
  \qquad
  \mathcal H_P=P\mathcal H,\quad \mathcal H_Q=Q\mathcal H.
```
The following assumptions give a clean theorem while still allowing unbounded diagonal blocks.

<div id="ass:block" class="assumption">

**Assumption 2** (Block domain and bounded coupling). The operators
``` math
A:\mathcal D(A)\subset\mathcal H_P\to\mathcal H_P,
 \qquad
 D:\mathcal D(D)\subset\mathcal H_Q\to\mathcal H_Q
```
are self-adjoint. The off-diagonal maps
``` math
B:\mathcal H_Q\to\mathcal H_P,
 \qquad
 C:\mathcal H_P\to\mathcal H_Q
```
are bounded and satisfy $`C=B^*`$. The full operator is
``` math
T=
 \begin{pmatrix}
 A&B\\ C&D
 \end{pmatrix},
 \qquad
 \mathcal D(T)=\mathcal D(A)\oplus\mathcal D(D).
```

</div>

By the bounded-perturbation theorem, $`T`$ is self-adjoint. This setup is not the most general Feshbach framework, but its domains and norms are unambiguous. Unbounded off-diagonal couplings require relative-bound, quadratic-form, or graph-norm hypotheses and are outside the theorem below.

<div class="definition">

**Definition 3** (Declared resolvent region). A set $`\Omega\subset\mathbb C`$ is an eliminated-sector resolvent region if
``` math
\Omega\subset\rho(D)
  \quad\text{and}\quad
  r_\Omega:=
  \sup_{z\in\Omega}\|(D-z)^{-1}\|<\infty.
```
For self-adjoint $`D`$,
``` math
\|(D-z)^{-1}\|
  =
  \frac{1}{\operatorname{dist}(z,\operatorname{spec}D)}
```
for $`z\notin\operatorname{spec}D`$.

</div>

A real gap $`\Delta`$ is useful only after the location of $`z`$ is declared. For example, if $`\operatorname{dist}(\Omega,\operatorname{spec}D)\geq g>0`$, then $`r_\Omega\leq g^{-1}`$. Writing only $`1/\Delta`$ hides this dependence.

# Exact Feshbach reduction

<div class="definition">

**Definition 4** (Feshbach–Schur map). For $`z\in\rho(D)`$, define
``` math
R_D(z)=(D-z)^{-1},
  \qquad
  \Sigma_T(z)=BR_D(z)C,
```
and
``` math
F_T(z)=A-z-\Sigma_T(z)
```
on $`\mathcal D(A)\subset\mathcal H_P`$.

</div>

The operator $`\Sigma_T(z)`$ is the eliminated-sector self-energy. It is bounded under <a href="#ass:block" data-reference-type="ref+label" data-reference="ass:block">2</a>; the reduced operator $`F_T(z)`$ remains closed on $`\mathcal D(A)`$.

<div id="thm:feshbach" class="theorem">

**Theorem 5** (Feshbach inverse formula). *Assume <a href="#ass:block" data-reference-type="ref+label" data-reference="ass:block">2</a> and let $`z\in\rho(D)`$. Then
``` math
z\in\rho(T)
 \quad\Longleftrightarrow\quad
 0\in\rho(F_T(z)).
```
When these equivalent conditions hold,
``` math
(T-z)^{-1}
=
\begin{pmatrix}
F_T(z)^{-1}
&
-F_T(z)^{-1}BR_D(z)
\\[0.3em]
-R_D(z)CF_T(z)^{-1}
&
R_D(z)+R_D(z)CF_T(z)^{-1}BR_D(z)
\end{pmatrix}.
```
In particular,
``` math
P(T-z)^{-1}P=F_T(z)^{-1}
```
on $`\mathcal H_P`$.*

</div>

<div class="proof">

*Proof.* On $`\mathcal D(A)\oplus\mathcal D(D)`$, factor
``` math
T-z
=
\begin{pmatrix}
\mathbf 1&BR_D(z)\\ 0&\mathbf 1
\end{pmatrix}
\begin{pmatrix}
F_T(z)&0\\ C&D-z
\end{pmatrix}.
```
The first factor is boundedly invertible. The second is invertible exactly when $`F_T(z)`$ is invertible, because $`D-z`$ is already invertible. The inverse of the two triangular factors gives the displayed block formula. Domain compatibility follows from $`\operatorname{ran}R_D(z)\subset\mathcal D(D)`$. ◻

</div>

The theorem is exact. It does not say that $`A`$ alone is an accurate replacement. That approximation is controlled by $`\Sigma_T(z)`$.

<div id="cor:product" class="corollary">

**Corollary 6** (Actual truncation-error product). *For every $`z\in\rho(D)`$,
``` math
\|\Sigma_T(z)\|
  \leq
  \|B\|\,\|R_D(z)\|\,\|C\|.
```
If $`D`$ is self-adjoint, then
``` math
\|\Sigma_T(z)\|
  \leq
  \frac{\|B\|\,\|C\|}
       {\operatorname{dist}(z,\operatorname{spec}D)}.
```
Under $`C=B^*`$, this becomes
``` math
\|\Sigma_T(z)\|
  \leq
  \frac{\|B\|^2}
       {\operatorname{dist}(z,\operatorname{spec}D)}.
```*

</div>

<div class="proof">

*Proof.* The first inequality is submultiplicativity of the operator norm. The second uses the self-adjoint resolvent identity $`\|R_D(z)\|=\operatorname{dist}(z,\operatorname{spec}D)^{-1}`$; the last uses $`\|B^*\|=\|B\|`$. ◻

</div>

The schematic expression $`\|\delta T\|^2/\Delta`$ is therefore valid only after proving that the same bounded perturbation supplies both off-diagonal blocks and that the declared spectral region remains at distance at least $`\Delta`$ from $`\operatorname{spec}D`$. The product form is the general statement.

## A two-mode example

<div class="example">

**Example 7** (One retained and one eliminated mode). Let
``` math
T=
  \begin{pmatrix}
    a&b\\ \overline b&d
  \end{pmatrix},
  \qquad a,d\in\mathbb R,
```
and let $`P`$ retain the first coordinate. For $`z\neq d`$,
``` math
F_T(z)
  =
  a-z-\frac{|b|^2}{d-z}.
```
Moreover,
``` math
\det(T-z)=(d-z)F_T(z).
```
Thus the self-energy has exact magnitude
``` math
|\Sigma_T(z)|=\frac{|b|^2}{|d-z|}.
```
The numerator measures coupling to the omitted mode; the denominator measures spectral distance from it. If $`P`$ were instead the exact spectral projector of $`T`$, the matrix in the corresponding eigenbasis would be diagonal and $`b=0`$.

</div>

This example contains the whole mechanism. A large gap cannot compensate for an unspecified or unbounded coupling, and a small coupling does not help at a pole of the eliminated resolvent.

# Projector selection and stability

Let $`G`$ be a self-adjoint reference operator and let a positively oriented closed contour $`\Gamma\subset\rho(G)`$ surround an isolated spectral cluster. With the resolvent convention used in this paper, the Riesz projector is
``` math
P
  =
  -\frac{1}{2\pi i}
  \oint_\Gamma (G-z)^{-1}\,\mathrm dz.
```
For self-adjoint $`G`$, this agrees with the corresponding spectral projector.

<div id="thm:riesz" class="theorem">

**Theorem 8** (Riesz-projector stability). *Let $`V=V^*`$ be bounded and set $`G_V=G+V`$. Define
``` math
M_0=\sup_{z\in\Gamma}\|(G-z)^{-1}\|.
```
If $`M_0\|V\|<1`$, then $`\Gamma\subset\rho(G_V)`$, the perturbed projector
``` math
P_V
  =
  -\frac{1}{2\pi i}
  \oint_\Gamma(G_V-z)^{-1}\,\mathrm dz
```
is well defined, and
``` math
\|P_V-P\|
\leq
\frac{\operatorname{length}(\Gamma)}{2\pi}
\frac{M_0^2\|V\|}{1-M_0\|V\|}.
```
If the right-hand side is less than one and $`P`$ has finite rank, then $`\operatorname{rank}P_V=\operatorname{rank}P`$.*

</div>

<div class="proof">

*Proof.* For $`z\in\Gamma`$,
``` math
G_V-z
=
\bigl[\mathbf 1+V(G-z)^{-1}\bigr](G-z).
```
The Neumann series gives
``` math
\|(G_V-z)^{-1}\|
\leq
\frac{M_0}{1-M_0\|V\|}.
```
The second resolvent identity gives
``` math
(G_V-z)^{-1}-(G-z)^{-1}
=
-(G_V-z)^{-1}V(G-z)^{-1}.
```
Integrating its norm around $`\Gamma`$ yields the displayed bound. Two orthogonal projections at distance less than one have isomorphic ranges; for finite rank their ranks agree. ◻

</div>

This theorem makes projector regularity a conclusion under explicit conditions, not an independent slogan. Davis–Kahan subspace-angle estimates provide related sharp bounds for self-adjoint spectral subspaces .

## What “bounded geometry” does not mean here

In differential geometry, bounded geometry normally includes precise metric conditions such as a positive injectivity-radius bound and curvature-derivative bounds. Bounded commutators in an operator representation are not, by themselves, equivalent to that notion.

This paper therefore avoids using “bounded geometry” as a catch-all hypothesis. Its analytic inputs are instead listed directly:

- self-adjointness and domains of $`A`$ and $`D`$;

- boundedness of $`B`$ and $`C`$;

- a declared common resolvent region;

- operator-norm perturbations where operator-norm conclusions are claimed; and

- a contour and Neumann margin where projector stability is claimed.

If an application uses geometric boundedness to prove these rows, that geometric theorem belongs in the application.

# Local robustness with all blocks visible

Consider two block operators $`T_0`$ and $`T_1`$ on the same decomposition and domains:
``` math
T_j=
\begin{pmatrix}
A_j&B_j\\ C_j&D_j
\end{pmatrix},
\qquad j=0,1.
```
Let
``` math
R_j(z)=(D_j-z)^{-1},
 \qquad
 \Sigma_j(z)=B_jR_j(z)C_j.
```

<div id="thm:robust" class="theorem">

**Theorem 9** (Operator-norm block robustness). *Suppose $`z\in\rho(D_0)\cap\rho(D_1)`$ and
``` math
\|R_j(z)\|\leq r,\qquad
\|B_j\|\leq b,\qquad
\|C_j\|\leq c.
```
Set
``` math
\alpha=\|A_1-A_0\|,\quad
\beta=\|B_1-B_0\|,\quad
\gamma=\|C_1-C_0\|,\quad
\delta=\|D_1-D_0\|.
```
Here the differences are bounded operators on the indicated fixed spaces. Then
``` math
\|\Sigma_1(z)-\Sigma_0(z)\|
\leq
\beta r c
+b r^2\delta c
+b r\gamma,
```
and
``` math
\|F_{T_1}(z)-F_{T_0}(z)\|
\leq
\alpha+\beta r c+b r^2\delta c+b r\gamma.
```*

</div>

<div class="proof">

*Proof.* Insert and subtract intermediate products:
``` math
\begin{aligned}
\Sigma_1-\Sigma_0
={}&(B_1-B_0)R_1C_1\\
&+B_0(R_1-R_0)C_1\\
&+B_0R_0(C_1-C_0).
\end{aligned}
```
The resolvent identity gives
``` math
R_1-R_0=-R_1(D_1-D_0)R_0,
```
so $`\|R_1-R_0\|\leq r^2\delta`$. Submultiplicativity gives the self-energy bound. Since
``` math
F_{T_1}(z)-F_{T_0}(z)
=(A_1-A_0)-(\Sigma_1-\Sigma_0),
```
the final estimate follows. ◻

</div>

<div id="cor:neumann" class="corollary">

**Corollary 10** (Common resolvent region from one reference). *If $`z\in\rho(D_0)`$ and
``` math
\|(D_0-z)^{-1}\|\,\|D_1-D_0\|<1,
```
then $`z\in\rho(D_1)`$ and
``` math
\|(D_1-z)^{-1}\|
\leq
\frac{\|(D_0-z)^{-1}\|}
 {1-\|(D_0-z)^{-1}\|\,\|D_1-D_0\|}.
```*

</div>

This is the precise local content of robustness in the present paper. It does not cover changing domains, relatively bounded unbounded perturbations, form convergence, strong-resolvent convergence, or semigroup convergence. Those are different topologies with different theorems .

# What “universality” can mean

Version 1 called two microscopic geometries universal when their effective generators agreed up to controlled error. Approximate agreement at one tolerance is not automatically an equivalence relation: errors accumulate under composition.

<div class="definition">

**Definition 11** (Reduced-resolvent comparison functional). Let two controlled records have retained spaces $`\mathcal H_{P,0}`$ and $`\mathcal H_{P,1}`$ of equal Hilbert dimension and a common region
``` math
\Omega\subset
  \rho(T_0)\cap\rho(D_0)\cap\rho(T_1)\cap\rho(D_1).
```
Define
``` math
d_\Omega(T_0,T_1)
=
\inf_U\;
\sup_{z\in\Omega}
\left\|
 U F_{T_0}(z)^{-1}U^*-F_{T_1}(z)^{-1}
\right\|,
```
where the infimum is over declared unitaries $`U:\mathcal H_{P,0}\to\mathcal H_{P,1}`$. If no such identification is supplied, set $`d_\Omega=\infty`$.

</div>

The inverse formula identifies each bounded term in this definition with the compressed resolvent $`P_j(T_j-z)^{-1}P_j`$. We call $`d_\Omega`$ a comparison functional rather than a metric: an application may restrict the allowed unitaries, and metric axioms then require separate closure conditions on that class. An $`\varepsilon`$-neighborhood under $`d_\Omega`$ is a useful local comparison class. Exact zero comparison can define a reduced equivalence after quotienting declared presentation redundancies. Finite $`\varepsilon`$-closeness is tolerance dependent and should be reported as such.

<div class="tabularx">

L0.23YY Statement & Data required & What it does not imply
Same retained rank & Stable Riesz projectors and rank certificate & Same reduced operator or physics
Close reduced resolvents & Common $`\Omega`$, unitary identification, operator norm & Uniform long-time dynamics
Close spectra & Spectral metric and multiplicity control & Close eigenvectors or observables
Close projectors & Gap/contour and perturbation norm & Dynamical stability
Same effective observables & Observation maps and error budget & Same microscopic theory
Physical equivalence & Full state, observable, dynamics, and comparison functor & Follows from no single row above

</div>

The paper therefore uses *local universality* only for a declared neighborhood in a declared reduced metric. It makes no claim that all viable quantum, gravitational, or compactification models occupy one class.

# Resolvent control is not uniform dynamical control

The Feshbach map is naturally an energy- or spectral-parameter-dependent object. Additional work is required to turn it into a statement about $`e^{-itT}`$.

<div id="prop:duhamel" class="proposition">

**Proposition 12** (A finite-time Duhamel bound). *Let $`T=T_{\rm diag}+W`$ be bounded and self-adjoint, where
``` math
T_{\rm diag}=A\oplus D
```
and $`W`$ contains the off-diagonal blocks. Then
``` math
\|e^{-itT}-e^{-itT_{\rm diag}}\|
\leq |t|\,\|W\|.
```
Consequently
``` math
\|Pe^{-itT}P-e^{-itA}P\|
\leq |t|\,\|W\|.
```*

</div>

<div class="proof">

*Proof.* Duhamel’s formula gives
``` math
e^{-itT}-e^{-itT_{\rm diag}}
=
-i\int_0^t
e^{-i(t-s)T}W e^{-isT_{\rm diag}}\,\mathrm ds.
```
Both unitary factors have norm one, so integration gives the bound. Compression by $`P`$ cannot increase the norm. ◻

</div>

This estimate is first order in the coupling and grows with the time horizon. Gap-improved adiabatic, Schrieffer–Wolff, or superadiabatic estimates are possible under additional hypotheses , but they are not consequences of <a href="#cor:product" data-reference-type="ref+label" data-reference="cor:product">6</a> alone.

<div class="example">

**Example 13** (No uniform-in-time conclusion from a small generator error). On the one-dimensional Hilbert space let $`H_0=0`$ and $`H_\varepsilon=\varepsilon`$. Their generators differ by $`\varepsilon`$, and their resolvents are close on compact sets away from zero. Yet at $`t=\pi/\varepsilon`$,
``` math
\|e^{-itH_\varepsilon}-e^{-itH_0}\|=2.
```
Thus small operator or resolvent error does not imply uniform closeness for arbitrarily long times.

</div>

# An internal generator is not automatically physical time

Every self-adjoint $`T`$ generates a strongly continuous unitary group
``` math
U_T(s)=e^{-isT}
```
by Stone’s theorem . This mathematical parameter $`s`$ need not be the time read by a physical clock. It might label a modular flow, an internal phase, a Euclidean interpolation, or an auxiliary spectral transformation.

A physical-time claim requires additional data such as:

1.  a physical state and observable algebra;

2.  a clock or operational time protocol;

3.  a physical Hamiltonian $`H_{\rm phys}`$;

4.  an embedding or decoding map $`J:\mathcal H_{\rm phys}\to\mathcal H_P`$; and

5.  an exact or controlled intertwining relation, for example
    ``` math
    J e^{-itH_{\rm phys}}
      =
      e^{-i\theta(t)A_{\rm eff}}J
      +E(t),
      \qquad
      \|E(t)\|\leq\varepsilon(t),
    ```
    on a declared interval and domain.

Without these rows, this paper establishes spectral reduction, not the emergence of observed time.

# A complete controlled-reduction certificate

<div class="definition">

**Definition 14** (Controlled coherent-sector certificate). A controlled coherent-sector certificate on $`\Omega`$ contains:
``` math
\mathfrak C_{\rm red}
=
\bigl(
\mathcal H,G,T,P,Q,
\mathcal D(A),\mathcal D(D),
A,B,C,D,
\Omega,r_\Omega,
\mathfrak n,\varepsilon,
\pi
\bigr),
```
where $`\mathfrak n`$ names the comparison norm, $`\varepsilon`$ is the proved error budget, and $`\pi`$ records the provenance and status of every input.

</div>

At minimum, the certificate should answer:

1.  What selected $`P`$, and is it exact, approximate, or finite?

2.  Which operator is being reduced?

3.  Are the block domains fixed and dense?

4.  Is each off-diagonal block bounded, relatively bounded, or only form bounded?

5.  What is the spectral region $`\Omega`$?

6.  How is $`\Omega\subset\rho(D)`$ certified?

7.  Which norm or topology is controlled?

8.  Is the approximation $`A`$, $`F_T(z)`$, or a further energy-independent operator?

9.  What parameter range preserves the projector rank and resolvent margin?

10. What observable or physical interpretation is attached afterward?

## Finite and numerical execution

For a finite matrix or Galerkin truncation, an executable certificate can report:

- exact dimensions and basis hashes;

- Hermiticity residuals and interval enclosures;

- the projector source and $`\|(I-P)GP\|`$;

- interval bounds for $`\operatorname{spec}D`$ or singular values of $`D-z`$;

- certified norms of $`B`$, $`C`$, and $`R_D(z)`$;

- the self-energy product and the resulting reduced resolvent error;

- projector-angle or contour bounds under perturbation; and

- roundoff, discretization, and continuum-transfer errors as separate rows.

The finite calculation is exact for the finite object if performed with exact or interval-certified arithmetic. It becomes a continuum theorem only after a convergence and domain-transfer result is supplied.

# Relation to MTT and established mathematics

## Established operator theory

The Schur complement and Feshbach map are standard tools. Their isospectral and inverse properties are established in operator-theoretic forms, including smooth variants . Spectral projections, closed operators, bounded perturbations, and resolvent convergence belong to classical perturbation theory . Davis–Kahan theory controls rotations of self-adjoint spectral subspaces .

Accordingly, this paper does not claim the Feshbach formula or Riesz projection as new Modal Triplet Theory mathematics. Its contribution is the correction and integration:

- exact spectral projectors are separated from reference-selected projectors;

- the actual product bound replaces a proxy slogan;

- every theorem states its domain, parameter, norm, and perturbation class;

- local reduction is not relabeled as global universality; and

- spectral flow is not relabeled as physical time.

## MTT ownership and use

The Modal Triplet Theory Foundation owns the general admissibility ledger and status semantics . The normalized-capacity paper owns the rowwise slack, scale, provenance, and bottleneck conventions . This paper owns only the coherent-sector operator certificate, the exact-projector correction, the domain-explicit Feshbach specialization, the local block-robustness estimate, and the resolvent-versus-time boundary.

Later Modal Triplet Theory papers may cite this certificate, but they must still construct their own $`G,T,P`$, prove the relevant domain and resolvent rows, and attach a physical interpretation map. Citation does not fill those objects.

# Claim status and limitations

<div class="tabularx">

L0.29L0.18Y Statement & Status here & Boundary
Exact spectral $`P`$ reduces $`T`$ & Proved & Self-adjoint spectral calculus
Feshbach inverse formula & Imported and specialized & Assumption <a href="#ass:block" data-reference-type="ref" data-reference="ass:block">2</a>, $`z\in\rho(D)`$
Self-energy product bound & Proved & Operator norm and bounded off-diagonal blocks
Riesz-projector stability & Proved & Bounded perturbation and fixed contour
Block robustness & Proved & Fixed domains and bounded operator differences
Finite-time Duhamel control & Proved & Bounded self-adjoint generators
Graph/form/semigroup robustness & Open per application & Requires different hypotheses
Continuum transfer & Open per application & Requires convergence and domain control
Physical-time emergence & Not established & Requires clock and intertwining theorem
Global MTT universality & Not claimed & Requires common source and physical equivalence maps

</div>

# Completion and falsifiability contract

A model-specific Modal Triplet Theory application is complete at the controlled resolvent-reduction tier only if it supplies:

1.  a selected, reproducible reference operator $`G`$;

2.  a projector $`P`$ with rank and stability certificate;

3.  the full operator $`T`$ and all block domains;

4.  verified off-diagonal maps $`B`$ and $`C`$;

5.  a nonempty spectral region $`\Omega\subset\rho(D)`$;

6.  a certified resolvent margin and self-energy product;

7.  a reduced operator and declared comparison norm;

8.  a numerical or analytic error budget;

9.  a continuum-transfer theorem if the source is finite; and

10. a physical observation or time map if physical dynamics is claimed.

The reduction fails in its declared regime if the selected rank changes, the contour meets the spectrum, the eliminated resolvent loses its bound, the off-diagonal product exceeds the tolerance, the domain assumptions fail, or a held-out observable lies outside the certified error budget. Those failure modes make the framework testable rather than merely descriptive.

# Conclusion

Coherent-sector reduction is a precise operator problem, not a consequence of the word “coherence.” If the retained projector is exactly spectral for the full operator, the sector already reduces the operator and there is no self-energy. If the projector comes from a reference or approximation, the omitted sector contributes the exact Feshbach–Schur term $`B(D-z)^{-1}C`$.

The resulting control has three visible ingredients: coupling into the omitted sector, resolvent distance within that sector, and coupling back. Projector stability follows from a separate contour and perturbation margin. Robustness is local to the norm, domains, region, and block variations actually bounded.

This corrected formulation gives Modal Triplet Theory a reusable and rigorous reduction certificate. It does not yet identify a universal coherent projector, derive physical time, or prove equivalence of different microscopic theories. Those stronger statements require model-specific source, continuum, dynamics, and observation maps.

# Reproducibility statement

All displayed estimates can be checked directly from the block factorization, resolvent identity, Neumann series, Riesz contour, and Duhamel formula printed in the paper. No numerical result or measured physical constant is used. A model-specific application should publish its matrices or closed-operator data and the certificate listed in <a href="#sec:certificate" data-reference-type="ref+label" data-reference="sec:certificate">10</a>.
