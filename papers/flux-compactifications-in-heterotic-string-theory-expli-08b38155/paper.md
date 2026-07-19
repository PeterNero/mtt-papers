---
abstract: |
  We construct explicit heterotic flux compactifications on non-Kähler manifolds satisfying the Hull–Strominger system and the Green–Schwarz anomaly cancellation condition. Working with left-invariant SU(3) structures, we present concrete examples on Iwasawa and Lens$`\times`$Nil geometries in which the torsion, gauge bundle data, and curvature contributions can be computed explicitly and matched componentwise. The resulting solutions exhibit sharply constrained parameter loci, illustrating how the combined geometric, bundle, and flux conditions restrict admissible compactifications. These constructions provide controlled test cases for heterotic compactifications beyond the Calabi–Yau setting.
author:
- Peter Nero
current_version: v3
date: January 2026
generated_from_main_tex_sha256: 5b729318803c8e0b5bc9d43351d82bb5f85ec781c4c4c65882b0fa6ba436bedb
paper_id: flux-compactifications-in-heterotic-string-theory-expli-08b38155
release_state: zenodo_released
released_version: v3.0
title: |
  Flux Compactifications in Heterotic String Theory:  
  Explicit Solutions on the Iwasawa Manifold and Lens$`\times`$Nil Geometries
zenodo_doi: 10.5281/zenodo.18205997
zenodo_record_id: 18205997
zenodo_url: "https://zenodo.org/records/18205997"
---

# Introduction

Heterotic flux compactifications on non-Kähler manifolds provide a rich class of string backgrounds in which torsion, gauge bundle data, and anomaly cancellation play a central role. Since the original work of Strominger , a variety of solutions to the Hull–Strominger system have been constructed, including balanced manifolds, nilmanifolds, and other geometries beyond the Calabi–Yau paradigm .

A recurring challenge in this setting is that the simultaneous requirements of balanced geometry, Hermitian–Yang–Mills connections, and Green–Schwarz anomaly cancellation impose strong but often implicit constraints on the underlying geometry and flux data. While many constructions proceed abstractly, explicit examples in which all contributions can be computed and matched componentwise remain comparatively rare.

In this paper we construct such explicit examples using left-invariant SU(3) structures on Iwasawa and Lens$`\times`$Nil geometries. These backgrounds allow a concrete treatment of torsion, curvature, and gauge bundles, making it possible to analyze the anomaly cancellation condition and associated constraints in detail. The resulting solutions exhibit isolated or lower-dimensional loci in parameter space, highlighting the restrictive interplay between geometry, flux, and bundle data in heterotic compactifications.

#### Interpretive context.

While the analysis in this paper is carried out entirely within standard heterotic string theory, the resulting constructions suggest that the combined geometric, bundle-theoretic, and anomaly-cancellation constraints act as a strong admissibility filter on compactification data. In particular, the appearance of isolated or lower-dimensional solution loci indicates that physically relevant backgrounds may be selected by internal consistency and stability conditions rather than by arbitrary choice within a large parameter space. For readers interested in broader interpretive frameworks in which such admissibility mechanisms arise naturally, additional discussion is provided in Appendices C and D. These appendices are expository and are not required for the main results of the paper.

# Heterotic $`SU(3)`$-structure compactifications: conventions

We work in heterotic supergravity to first order in $`\alpha'`$. On a six-manifold $`(X,J,\Omega)`$ with $`SU(3)`$ structure the Hull–Strominger system reads
``` math
\begin{align}
\mathrm{d}\!\big(e^{-2\Phi}\!*J\big)&=0,\qquad \mathrm{d}\Omega=0, \label{HS1}\\
F^{0,2}=F^{2,0}&=0,\quad J\lrcorner F=0, \label{HS2}\\
\mathrm{d}H&=\frac{\alpha'}{4}\big(\mathrm{Tr}_{\rm grav} R_+^2-\mathrm{Tr}F^2\big),\qquad H=\mathrm{i}(\bar\partial-\partial)J, \label{HS3}
\end{align}
```
with $`R_+`$ the curvature of the Bismut connection $`\nabla^+`$ (metric with totally skew torsion $`+H`$), $`F`$ the gauge curvature, and $`\Phi`$ the dilaton.[^1] We set $`\Phi=\text{const}`$ so <a href="#HS1" data-reference-type="eqref" data-reference="HS1">[HS1]</a> reduces to the *balanced* condition $`\mathrm{d}(J^2)=0`$.

*Balanced notation.* Since $`\Phi=\mathrm{const}`$, eq. <a href="#HS1" data-reference-type="eqref" data-reference="HS1">[HS1]</a> is equivalent to $`\mathrm{d}(*J)=0`$ and, in six dimensions, to $`\mathrm{d}(J^2)=0`$. We will freely use $`\mathrm{d}(J^2)=0`$ below.

We normalize
``` math
\begin{equation}
\label{norms}
\int_X \Omega\wedge\bar\Omega=1,\qquad \int_X a\wedge b\wedge c=1,
\end{equation}
```
for the invariant $`(1,1)`$ basis $`\{a,b,c\}`$ introduced later.

#### Left-invariant truncation and $`H^4`$ completeness.

In all explicit constructions below (Iwasawa and Lens$`\times`$Nil) we work in the *left-invariant* ansatz: the metric $`(J,\Omega)`$, torsion $`H=\mathrm{i}(\bar\partial-\partial)J`$, the Bismut curvature $`R_+`$, and all gauge fields (both the $`SU(3)`$ instanton and the abelian flux) are left-invariant. Consequently, $`\mathrm{Tr}_{\rm grav} R_+^2`$, $`\mathrm{Tr}F^2`$, and $`\mathrm{d}H`$ lie in the *left-invariant* $`(2,2)`$ subspace of $`H^4(X,\mathbb{R})`$. On Iwasawa this subspace is spanned by $`\{\alpha_1,\alpha_2,\alpha_3\}`$ defined in <a href="#alphas" data-reference-type="eqref" data-reference="alphas">[alphas]</a>; on Lens$`\times`$Nil it is spanned by $`\{\beta_1,\beta_2,\beta_3\}`$. The componentwise Bianchi analysis is therefore complete *within the invariant sector*.

#### Trace conventions.

We use two compatible traces:

- For the gauge sector ($`E_8`$), $`\mathrm{Tr}`$ is the adjoint trace restricted to the embedded subgroup, normalized so that for any abelian generator $`T`$ we have $`\mathrm{Tr}(T^2)=1`$. Integer fluxes then correspond to integral periods of $`F/2\pi`$.

- For the gravitational sector, we take $`\mathrm{Tr}_{\mathrm{grav}}`$ to be the vector trace on $`\mathfrak{so}(6)`$ with
  ``` math
  \begin{equation}
  \label{eq:grav-trace-conv}
  \mathrm{Tr}_{\mathrm{grav}}(R\wedge R)\;=\;\frac{1}{2}\,R^{ab}\wedge R^{ab},
  \end{equation}
  ```
  where $`R^{ab}`$ are curvature 2-forms in an orthonormal frame and indices are raised/lowered with $`\delta_{ab}`$.

We reserve $`\mathrm{Tr}`$ for the gauge trace and $`\mathrm{Tr}_{\mathrm{grav}}`$ for the gravitational trace; with these conventions, <a href="#HS3" data-reference-type="eqref" data-reference="HS3">[HS3]</a> reads $`\mathrm{d}H=\frac{\alpha'}{4}\big(\mathrm{Tr}_{\rm grav}R_+^2-\mathrm{Tr}F^2\big)`$.

*Normalization remark.* Our $`\mathrm{Tr}_{\mathrm{grav}}`$ is the vector trace on $`\mathfrak{so}(6)`$, so $`\mathrm{Tr}_{\mathrm{grav}}(R\wedge R)=\tfrac12\,R^{ab}\wedge R_{ab}`$ in an orthonormal frame. Other heterotic conventions sometimes use a different normalization (e.g. a fundamental “$`\mathrm{tr}`$”). All formulae here are self-consistent with $`\alpha'/4`$ as written; translating to alternate conventions amounts to an overall rescaling of the trace and a compensating rescaling in the $`\alpha'/4`$ factor in the Bianchi identity.

#### Positioning and novelty.

Relative to earlier explicit heterotic torsional backgrounds (e.g. ), our contribution is twofold: (i) a coefficient-level computation of $`\mathrm{Tr}_{\rm grav}R_+^2`$ in an invariant frame on Iwasawa (yielding an exact $`\alpha_1`$-only decomposition with explicit coefficient), and (ii) an isolated, balanced, non-integrable Lens$`\times`$Nil solution whose anomaly equations discretely fix the radius ratio (no invariant moduli) in the invariant sector while keeping full flux quantization and gerbe structure explicit.

# Iwasawa: left-invariant $`SU(3)`$ structure and torsion

<span id="sec:iwasawa" label="sec:iwasawa"></span> Let $`(\omega^1,\omega^2,\omega^3)`$ be a left-invariant $`(1,0)`$ frame on the complex Heisenberg group $`H_3(\mathbb{C})`$ with
``` math
\begin{equation}
\label{Iwa-struct}
\mathrm{d}\omega^1=\mathrm{d}\omega^2=0,\qquad \mathrm{d}\omega^3=\omega^1\wedge\omega^2.
\end{equation}
```
For $`\Gamma\subset H_3(\mathbb{C})`$ cocompact, $`X=\Gamma\backslash H_3(\mathbb{C})`$ is the Iwasawa manifold: complex, balanced, non-Kähler. We take
``` math
\begin{equation}
\label{JOmega}
J \;=\; \frac{i}{2}\sum_{j=1}^{3} r_j^{\,2}\,\omega_j \wedge \bar\omega_j,
\qquad
\Omega \;=\; \omega_1 \wedge \omega_2 \wedge \omega_3.
\end{equation}
```
with $`r_j>0`$. Using <a href="#Iwa-struct" data-reference-type="eqref" data-reference="Iwa-struct">[Iwa-struct]</a> one finds
``` math
\begin{align}
\partial J&=\frac{\mathrm{i}}{2}\,r_3^2\,(\omega^1\wedge\omega^2)\wedge\overline{\omega^3},\qquad
\bar\partial J=\frac{\mathrm{i}}{2}\,r_3^2\,\omega^3\wedge\overline{\omega^1}\wedge\overline{\omega^2},\\
H&=\mathrm{i}(\bar\partial-\partial)J
= -\frac{r_3^2}{2}\Big(\,\overline{\omega^3}\wedge\omega^1\wedge\omega^2
- \omega^3\wedge\overline{\omega^1}\wedge\overline{\omega^2}\,\Big),\\
\mathrm{d}H&=2\mathrm{i}\,\partial\bar\partial J
= r_3^2\,\omega^1\wedge\overline{\omega^1}\wedge\omega^2\wedge\overline{\omega^2}
= -\,4\,r_3^2\,\alpha_1.
\end{align}
```

Introduce the invariant $`(1,1)`$ forms
``` math
\begin{equation}
\label{abc}
\\[6pt]
a \;:=\; \frac{i}{2}\,\omega_1 \wedge \bar\omega_1,
\qquad
b \;:=\; \frac{i}{2}\,\omega_2 \wedge \bar\omega_2,
\qquad
c \;:=\; \frac{i}{2}\,\omega_3 \wedge \bar\omega_3.
\end{equation}
```
so $`a\wedge a=b\wedge b=c\wedge c=0`$ (as *forms*). Define the invariant $`H^{2,2}`$ basis
``` math
\begin{equation}
\label{alphas}
\alpha_1:=a\wedge b,\qquad \alpha_2:=a\wedge c,\qquad \alpha_3:=b\wedge c.
\end{equation}
```

# An explicit indecomposable $`SU(3)`$ monad with $`c_1=0`$, $`c_2=0`$, $`\int c_3=6`$

We build $`E`$ as the cohomology of a two-step monad
``` math
\begin{equation}
\label{monad}
0\longrightarrow K_1 \xrightarrow{f} \bigoplus_{i=1}^{5} L_i \xrightarrow{g} K_2 \longrightarrow 0,\qquad
E:=\ker g / \mathrm{im}\,f,
\end{equation}
```
with $`K_1,K_2`$ line bundles. In $`K`$-theory, $`[E]=\sum_i [L_i]-[K_1]-[K_2]`$, hence
``` math
\begin{equation}
\label{chE}
\mathrm{ch}(E)=\sum_{i=1}^5 e^{\ell_i}-e^{\kappa_1}-e^{\kappa_2},\qquad \ell_i:=c_1(L_i),\ \kappa_a:=c_1(K_a)\in H^2(X,\mathbb{Z}).
\end{equation}
```
Write
``` math
\begin{equation}
\mathrm{ch}(E)=3+\mathrm{ch}_1+\mathrm{ch}_2+\mathrm{ch}_3,\qquad
\mathrm{ch}_1=c_1,\quad \mathrm{ch}_2=\tfrac12\!\left(c_1^2-2c_2\right),\quad \mathrm{ch}_3=\tfrac16\!\left(c_1^3-3c_1c_2+3c_3\right).
\end{equation}
```
From <a href="#chE" data-reference-type="eqref" data-reference="chE">[chE]</a> we read off
``` math
\begin{align}
c_1(E) &= \sum_i \ell_i - \kappa_1-\kappa_2=:S_1-K,\label{c1S1K}\\
\mathrm{ch}_2(E) &= \tfrac12\Big(\sum_i \ell_i^2 - \kappa_1^2 - \kappa_2^2\Big),\label{ch2}\\
\mathrm{ch}_3(E) &= \tfrac16\Big(\sum_i \ell_i^3 - \kappa_1^3 - \kappa_2^3\Big).\label{ch3}
\end{align}
```
Impose $`c_1(E)=0`$ by $`K=S_1`$. Then $`c_2(E)=-\,\mathrm{ch}_2(E)`$ and $`c_3(E)=2\,\mathrm{ch}_3(E)`$.

#### Invariant ring and powers.

For $`\ell=x\,a+y\,b+z\,c`$,
``` math
\begin{equation}
\label{powers}
\ell^2=2\,(xy\,\alpha_1+xz\,\alpha_2+yz\,\alpha_3),\qquad \ell^3=6\,xyz\,a\wedge b\wedge c.
\end{equation}
```

#### Explicit integer data.

Choose
``` math
\begin{equation}
\label{Li-table}
\begin{aligned}
\ell_1&=-2\,a+0\,b+1\,c,\qquad
\ell_2=-1\,a+1\,b-1\,c,\\
\ell_3&=+1\,a-1\,b+0\,c,\qquad
\ell_4=+1\,a+0\,b-1\,c,\\
\ell_5&=+2\,a+1\,b+1\,c,
\end{aligned}
\end{equation}
```
so that
``` math
\begin{equation}
\label{S1}
S_1:=\sum_{i=1}^5 \ell_i \;=\; a+b.
\end{equation}
```
Take
``` math
\begin{equation}
\label{Ka}
\kappa_1=a,\qquad \kappa_2=b \quad\Rightarrow\quad K=\kappa_1+\kappa_2=S_1,
\end{equation}
```
hence $`c_1(E)=0`$ by <a href="#c1S1K" data-reference-type="eqref" data-reference="c1S1K">[c1S1K]</a>. Using <a href="#powers" data-reference-type="eqref" data-reference="powers">[powers]</a> one checks $`\sum_i\ell_i^2=0\Rightarrow c_2(E)=0`$, and
``` math
\begin{equation}
\label{c3six}
\int_X c_3(E)=6.
\end{equation}
```

#### Indecomposability, stability, and HYM.

For generic holomorphic maps $`f,g`$ in <a href="#monad" data-reference-type="eqref" data-reference="monad">[monad]</a> (constant matrices in the left-invariant frame), $`E`$ is indecomposable. Stability is taken with respect to the Gauduchon class $`[J^2]`$ on the balanced Iwasawa metric. Since $`c_1(E)=0`$, $`\mu(E)=0`$. Any rank-1 subsheaf would give a nontrivial invariant section of $`E\otimes L^{-1}`$; but $`H^0(X,E)=0`$ for a generic monad, and similarly rank-2 destabilizers are excluded using $`\wedge^2E\simeq E^\ast`$ (for $`SU(3)`$) and the absence of invariant sections. Hence $`E`$ is $`\mu`$-stable, and by the Li–Yau theorem on balanced manifolds it admits a unique (up to unitary gauge) Hermitian–Yang–Mills connection .

*On $`c_2(E)=0`$.* The vanishing of $`c_2(E)`$ does *not* imply flatness. It states that the net instanton number cancels among the summands and extensions in the monad; indeed our Chern–Weil check (Sec. <a href="#sec:ExplicitDolbeault" data-reference-type="ref" data-reference="sec:ExplicitDolbeault">5</a>) shows $`F_E\neq 0`$ while $`\mathrm{Tr}F_E\wedge F_E=0`$.

*Cohomological Bianchi identity.* Iwasawa is complex-parallelizable, hence the holomorphic tangent bundle is trivial and $`c_k(TX)=0`$ for all $`k`$. In particular $`c_2(TX)=0`$, so
``` math
\int_X \big(\mathrm{Tr}_{\rm grav} R_+^2 - \mathrm{Tr}F^2\big)\;=\;0,
```

and the Bianchi identity is automatically satisfied in cohomology.

# An explicit left-invariant holomorphic structure $`\bar\partial_E`$

<span id="sec:holostruct" label="sec:holostruct"></span> Let $`(\omega^1,\omega^2,\omega^3)`$ be the global holomorphic 1-forms on $`X`$; then $`\bar\omega^1,\bar\omega^2`$ are $`\bar\partial`$-closed and $`\bar\partial\bar\omega^3=\bar\omega^1\wedge\bar\omega^2`$. Define
``` math
\begin{equation}
\label{eq:A01}
\bar\partial_E\;=\;\bar\partial + \mathcal{A}^{(0,1)},\qquad
\mathcal{A}^{(0,1)}\;=\;
\begin{pmatrix}
0 & \mu\,\bar\omega^3 & \sqrt{\mu}\,\bar\omega^1 \\
0 & 0 & 0 \\
-\sqrt{\mu}\,\bar\omega^2 & 0 & 0
\end{pmatrix},\qquad \mu>0.
\end{equation}
```
A direct calculation gives $`\bar\partial_E^2=0`$. Equipping $`E_{\rm sm}`$ with the trivial Hermitian metric, the Chern connection has curvature $`F_E`$ of type $`(1,1)`$; a concise invariant-basis computation yields $`\mathrm{Tr}F_E\wedge F_E=0`$ and $`\mathrm{ch}_3(E)=3\,a\wedge b\wedge c`$, hence $`c_3(E)=6\,a\wedge b\wedge c`$.

# Anomaly cancellation on Iwasawa: full coefficient match

<span id="sec:anomaly" label="sec:anomaly"></span> **Invariant $`(2,2)`$ basis.** Since $`J,H,R_+`$ and the gauge fields are left-invariant, all four-forms entering the Bianchi identity live in the left-invariant $`(2,2)`$ subspace. On Iwasawa this is spanned by $`\{\alpha_1,\alpha_2,\alpha_3\}`$ of <a href="#alphas" data-reference-type="eqref" data-reference="alphas">[alphas]</a>; expansions below are therefore complete within the ansatz.

#### Group-theoretic embedding and flux choice.

Place the abelian factors in the *hidden* $`E_8`$. Take two orthonormal Cartan generators $`T_a\in\mathfrak{h}(E_8^{\rm hid})`$ ($`a=1,2`$) with $`\mathrm{Tr}(T_aT_b)=\delta_{ab}`$. Let
``` math
\begin{equation}
F^{(1)}=2\pi\sum_{a=1}^2 T_a\big(n^{(a)}_1\,a+n^{(a)}_2\,b+n^{(a)}_3\,c\big),\qquad n^{(a)}_i\in\mathbb{Z}.
\end{equation}
```
Then
``` math
\begin{equation}
\label{u-from-n-multi}
\mathrm{Tr}\!\big(F^{(1)}\!\wedge F^{(1)}\big)=2(2\pi)^2\sum_{a=1}^2\Big(n^{(a)}_1 n^{(a)}_2\,\alpha_1+n^{(a)}_1 n^{(a)}_3\,\alpha_2+n^{(a)}_2 n^{(a)}_3\,\alpha_3\Big).
\end{equation}
```
Choose $`n^{(a)}_3=0`$ for $`a=1,2`$ and
``` math
\begin{equation}
\label{flux-choice}
(n^{(1)}_1,n^{(1)}_2)=(1,2),\qquad (n^{(2)}_1,n^{(2)}_2)=(-1,-2),
\end{equation}
```
so that
``` math
\begin{equation}
\label{u-vals}
u_1=8(2\pi)^2,\qquad u_2=u_3=0,
\end{equation}
```
and primitivity $`J\lrcorner F^{(1)}=0`$ holds by pairwise cancellation for any radii $`r_i`$.

Expand the remaining terms:
``` math
\begin{equation}
\label{expansion-uvw}
\mathrm{Tr}_{\rm grav} R_+^2=\sum_{i=1}^3 v_i\,\alpha_i,\qquad
\mathrm{d}H=\sum_{i=1}^3 w_i\,\alpha_i\quad(\text{with }w_1=-4r_3^2,\ w_2=w_3=0).
\end{equation}
```
With the sign in <a href="#HS3" data-reference-type="eqref" data-reference="HS3">[HS3]</a>, the Bianchi identity is
``` math
\begin{equation}
\label{system}
u_i - v_i \;=\; -\,\frac{4}{\alpha'}\,w_i\qquad (i=1,2,3).
\end{equation}
```

#### Solving the linear system.

Because the left-invariant HYM bundle obeys $`\mathrm{Tr}F(E)^2=0`$ and $`\mathrm{Tr}_{\rm grav}R_+^2`$ has support only on $`\alpha_1`$ (App. <a href="#app:Rplus" data-reference-type="ref" data-reference="app:Rplus">12</a>), we have $`v_2=v_3=0`$ and
``` math
\begin{equation}
\label{match-components-fixed}
u_2=v_2=0,\qquad u_3=v_3=0,\qquad u_1-v_1 = \frac{16}{\alpha'}\,r_3^2.
\end{equation}
```
*Dimensional check:* $`[u_i]=[v_i]=L^0`$, $`[w_1]=L^2`$, $`[\alpha']=L^2`$, hence $`(16/\alpha')\,r_3^2`$ is dimensionless, as required.

For example, setting $`r_1=r_2=:R`$ and using $`v_1=\tilde v_1=8\,r_3^2/R^4`$ (App. <a href="#app:Rplus" data-reference-type="ref" data-reference="app:Rplus">12</a>) with $`u_1`$ from <a href="#u-vals" data-reference-type="eqref" data-reference="u-vals">[u-vals]</a>, we obtain
``` math
\begin{equation}
\label{fixr3-new}
8(2\pi)^2 - \frac{8\,r_3^2}{R^4} = \frac{16}{\alpha'}\,r_3^2
\quad\Longrightarrow\quad
r_3^2 = \frac{8(2\pi)^2}{\,\tfrac{16}{\alpha'}+\tfrac{8}{R^4}\,}.
\end{equation}
```
Flux quantization is automatic: $`F^{(1)}/2\pi`$ integrates to integers over cycles dual to $`a,b,c`$; the gauge-invariant flux $`\mathcal{H}`$ has integral periods (Sec. <a href="#sec:quant" data-reference-type="ref" data-reference="sec:quant">10</a>).

# A normalized Yukawa coupling on Iwasawa

Let $`\Psi_i\in H^1(X,E)`$ ($`i=1,2,3`$) be three orthonormal harmonic representatives of bundle-valued $`(0,1)`$-forms (balanced metric). Normalize the symmetric cubic invariant $`d_{abc}`$ of $`E_6`$[^2] so that $`d_{abc}\,\Psi_1^a \Psi_2^b \Psi_3^c`$ has unit coefficient and $`\int_X \Omega \wedge \bar\Omega = 1`$. The tree-level superpotential coefficient is
``` math
\begin{equation}
\lambda_{123}=\int_X \Omega\wedge \mathrm{Tr}\!\big(\Psi_1\wedge\Psi_2\wedge\Psi_3\big).
\end{equation}
```
On complex-parallelizable Iwasawa, any harmonic $`(0,3)`$-form is proportional to $`\bar\Omega`$; orthonormality implies
``` math
\begin{equation}
\mathrm{Tr}(\Psi_1\wedge\Psi_2\wedge\Psi_3)=e^{\mathrm{i}\theta}\,\bar\Omega\quad\Rightarrow\quad \lambda_{123}=e^{\mathrm{i}\theta}.
\end{equation}
```
A chiral field rephasing removes the phase, giving the normalized result $`\lambda_{123}=1`$.

#### Phenomenological remark.

In the $`E_6`$ language the holomorphic cubic $`\bm{27}^3`$ coupling inherits this normalization, yielding at tree level a Yukawa matrix of rank one. After electroweak symmetry breaking (and including small higher-derivative or nonperturbative corrections), this furnishes a natural starting point for hierarchical fermion masses.

# Lens$`\times`$Nil: a balanced non-integrable $`SU(3)`$ solution

Take $`X_6=L(3,1)\times(\Gamma\!\backslash\!\mathrm{Nil}^3)`$ with left-invariant coframes $`\{\eta^1,\eta^2,\eta^3\}`$ on $`L(3,1)`$ ($`\mathrm{d}\eta^i=\tfrac12\varepsilon_{ijk}\eta^j\wedge\eta^k`$) and $`\{\sigma^4,\sigma^5,\sigma^6\}`$ on $`\mathrm{Nil}^3`$ ($`\mathrm{d}\sigma^4=\mathrm{d}\sigma^5=0,\ \mathrm{d}\sigma^6=\sigma^4\wedge\sigma^5`$). Define
``` math
\begin{align}
J &= R_1^2\,\eta^1\wedge\eta^2 + R_2^2\,\eta^3\wedge\sigma^6 + R_3^2\,\sigma^4\wedge\sigma^5,\\
\Omega &= (\eta^1+\mathrm{i}\eta^2)\wedge(\eta^3+\mathrm{i}\sigma^4)\wedge(\sigma^6+\mathrm{i}\sigma^5).
\end{align}
```
One checks $`d(J^2)=0`$ iff $`R_2=R_3=:R`$, while $`d\Omega\neq 0`$ (non-integrable). The torsion $`H=\mathrm{i}(\bar\partial-\partial)J`$ is nonzero and $`dH`$ expands on the invariant 4-form basis
``` math
\begin{equation}
\beta_1:=\eta^1\wedge\eta^2\wedge\eta^3\wedge\sigma^6,\quad
\beta_2:=\eta^1\wedge\eta^2\wedge\sigma^4\wedge\sigma^5,\quad
\beta_3:=\eta^3\wedge\sigma^4\wedge\sigma^5\wedge\sigma^6,
\end{equation}
```
with coefficients $`W_i(R_1,R)`$ given explicitly in Appendix <a href="#app:lensnil-coeff" data-reference-type="ref" data-reference="app:lensnil-coeff">13</a>. Take an abelian flux
``` math
\begin{equation}
F^{(1)}=2\pi\,T\,(f\,\eta^1\wedge\eta^2 + h\,\sigma^4\wedge\sigma^5),\qquad f,h\in\mathbb{Z},
\end{equation}
```
primitive at $`R_2=R_3`$. Then
``` math
\begin{equation}
\mathrm{Tr}F^{(1)2}=2(2\pi)^2\big(f^2\,\beta_1+h^2\,\beta_3\big),\qquad \mathrm{Tr}_{\rm grav} R_+^2 = A(R_1,R)\,\beta_1+B(R_1,R)\,\beta_3,
\end{equation}
```
and the anomaly equations reduce to the two real equations
``` math
\begin{equation}
\label{lens-eqs}
2(2\pi)^2 f^2 - A(R_1,R) = \frac{4}{\alpha'}\,W_1(R_1,R),\qquad
2(2\pi)^2 h^2 - B(R_1,R) = \frac{4}{\alpha'}\,W_3(R_1,R),
\end{equation}
```
fixing the *ratio* $`R_1/R`$ for given integers $`(f,h)`$. In particular, the two anomaly equations fix $`R_1/R`$ (no invariant moduli), consistent with App. <a href="#app:lensnil-coeff" data-reference-type="ref" data-reference="app:lensnil-coeff">13</a>. Flux quantization holds since $`(f,h)\in\mathbb{Z}^2`$ and the 2-forms have integral periods. The balanced condition and these two equations isolate a isolated invariant solution (no continuous moduli in the invariant sector), while a deformation $`R\to 0`$ connects to a toroidal CY orbifold limit.

# Moduli and higher-order $`\alpha'`$ effects

#### Iwasawa (invariant sector).

We work in the left-invariant truncation. At first order in $`\alpha'`$, the metric radii $`(r_1,r_2,r_3)`$ and bundle moduli enter continuously; <a href="#match-components-fixed" data-reference-type="eqref" data-reference="match-components-fixed">[match-components-fixed]</a> and <a href="#fixr3-new" data-reference-type="eqref" data-reference="fixr3-new">[fixr3-new]</a> fix two relations, but an overall volume/shape modulus remains. Flux quantization ties certain combinations of radii to integer data, yet still allows a continuous family in the large-volume, small-flux regime. A full (non-invariant) moduli analysis is beyond our scope; see .

#### Lens$`\times`$Nil (invariant sector).

Here the balanced condition and the two scalar anomaly equations <a href="#lens-eqs" data-reference-type="eqref" data-reference="lens-eqs">[lens-eqs]</a> fix the *ratio* $`R_1/R`$, leaving at most an overall scale modulus at this order. Thus our Lens$`\times`$Nil solution is an *isolated fixed point* in the invariant sector.

#### Higher-order $`\alpha'`$ corrections.

Our solutions solve the Hull–Strominger system at $`\mathcal{O}(\alpha')`$. At $`\mathcal{O}(\alpha'^2)`$ one typically expects curvature-squared terms (and possibly a non-constant dilaton or warp factor) to appear. We therefore restrict to a regime of *parametric control* (large volume and small flux in string units) where higher-order terms are suppressed.

# Flux quantization and the heterotic gerbe

<span id="sec:gerbe" label="sec:gerbe"></span> The gauge-invariant three-form
``` math
\begin{equation}
\mathcal{H} := dB - \frac{\alpha'}{4}\big(\omega_3(A)-\omega_3(R_+)\big),\qquad
\mathcal{H} \equiv H = i(\bar\partial-\partial)J.
\end{equation}
```
has integral periods $`[\mathcal{H}]\in H^3(X,2\pi\alpha'\mathbb{Z})`$ on compact $`X`$. In our invariant constructions, $`\mathrm{Tr}F^2`$ and $`\mathrm{Tr}_{\rm grav} R_+^2`$ lie in the span of integral 4-forms ($`\{\alpha_i\}`$ or $`\{\beta_i\}`$), hence $`\frac{\alpha'}{4}(\mathrm{Tr}_{\rm grav} R_+^2-\mathrm{Tr}F^2)`$ is integral. Choosing $`H`$ to satisfy <a href="#HS3" data-reference-type="eqref" data-reference="HS3">[HS3]</a> ensures the $`B`$-field gerbe is globally well-defined. We presented two explicit heterotic flux backgrounds in the left-invariant SU(3)-structure ansatz. On the complex Iwasawa threefold, an indecomposable rank‑3 SU(3) bundle $`E`$ with $`(c_1,c_2,\int c_3)=(0,0,6)`$ yields three net chiral generations for visible $`E_8\!\to\!E_6`$, and the Bianchi identity is solved componentwise with support only on $`\alpha_1`$, fixing $`r_3`$ for given integers. On LensNil, a balanced but non‑integrable SU(3) structure with an abelian instanton yields two independent anomaly equations that fix the ratio $`R_1/R`$, leaving no invariant moduli. A normalized trilinear Yukawa on Iwasawa gives $`\lambda_{123}=1`$ at tree level, providing a clean starting point for hierarchical masses.

These solutions are conservative, fully string‑native realizations with explicit geometry, flux, and bundles, and can serve as benchmarks for further work on moduli, higher‑order $`\alpha'`$ corrections, and phenomenology. Optional Appendices <a href="#app:curvature" data-reference-type="ref" data-reference="app:curvature">[app:curvature]</a>–<a href="#app:mtt" data-reference-type="ref" data-reference="app:mtt">14</a> make precise the (left‑invariant) equivalence between compactification and projection and indicate how the present backgrounds align with a general coherent‑sector framework without affecting any of the string‑theoretic derivations.

# Conclusion

In this paper we constructed explicit heterotic flux compactifications satisfying the Hull–Strominger system and the Green–Schwarz anomaly cancellation condition, including both complex and non-complex balanced geometries. The Iwasawa and Lens$`\times`$Nil examples provide concrete realizations in which the torsion, gauge bundle data, and curvature contributions can be computed explicitly and matched componentwise.

A notable feature of the constructions presented here is that the combined geometric, bundle, and flux constraints reduce the space of admissible compactifications to isolated or lower-dimensional loci in parameter space. In particular, the simultaneous requirements of bounded geometry, balanced structure, Hermitian–Yang–Mills connections, and anomaly cancellation strongly restrict the allowed radii, flux coefficients, and bundle data. Degenerations that violate these conditions do not admit consistent solutions within the framework considered.

From a string-theoretic perspective, these results illustrate how flux compactifications on non-Kähler manifolds can be both mathematically controlled and physically constrained. The effective four-dimensional theories obtained coincide with the standard heterotic effective action up to the usual field redefinitions and matching ambiguities. At the same time, the analysis makes clear that large classes of nominal flux vacua are excluded once all consistency conditions are imposed simultaneously.

The explicit constructions and appendices provided here are intended to serve as concrete test cases for further investigations of heterotic compactifications on non-Kähler backgrounds. In particular, they provide a useful laboratory for studying moduli stabilization, anomaly cancellation mechanisms, and the interplay between geometry and flux in settings beyond the Calabi–Yau paradigm.

#### Optional interpretive remark.

The discrete and sharply constrained solution sets encountered in the examples above suggest that consistency conditions in heterotic flux compactifications may be viewed as defining an admissible domain rather than a freely tunable landscape. Similar perspectives arise in approaches where physical degrees of freedom are restricted by spectral or stability criteria. While no additional structure is required for the string-theoretic results presented here, the appendices discuss how these constructions can be embedded into a broader fixed-point framework for readers interested in such connections.

# Torsional spin curvature on Iwasawa: explicit invariant-frame formula

<span id="app:curvature" label="app:curvature"></span> Work in a real orthonormal left-invariant coframe $`(e^1,\dots,e^6)`$ adapted to <a href="#JOmega" data-reference-type="eqref" data-reference="JOmega">[JOmega]</a> by
``` math
\omega^1=\frac{1}{r_1}(e^1+\mathrm{i}e^2),\quad \omega^2=\frac{1}{r_2}(e^3+\mathrm{i}e^4),\quad \omega^3=\frac{1}{r_3}(e^5+\mathrm{i}e^6),
```
so that $`J=e^{12}+e^{34}+e^{56}`$ with $`e^{ij}:=e^i\wedge e^j`$. From <a href="#Iwa-struct" data-reference-type="eqref" data-reference="Iwa-struct">[Iwa-struct]</a> one finds the only nonzero real structure equations
``` math
\begin{equation}
\label{eq:real-struct}
\mathrm{d}e^5 \;=\; A\,(e^{13}-e^{24}),\qquad \mathrm{d}e^6 \;=\; A\,(e^{14}+e^{23}),\qquad A:=\frac{r_3}{r_1 r_2}.
\end{equation}
```
The Bismut connection $`\nabla^+`$ is metric with totally skew torsion $`T=H`$. In this frame the nonzero components of $`T`$ are linear in $`A`$ and live in the $`e^{12}e^{5}`$, $`e^{34}e^{5}`$, $`e^{12}e^{6}`$, $`e^{34}e^{6}`$ directions. Writing the connection 1‑forms as $`\omega^+{}_{ab}=\omega^g{}_{ab}+\tfrac12\,T_{abc}\,e^c`$ and $`R^+{}_{ab}=\mathrm{d}\omega^+{}_{ab}+\omega^+{}_{ac}\wedge\omega^+{}_{cb}`$, a straightforward left‑invariant computation yields
``` math
\begin{equation}
\label{eq:Rplus-alpha1-final}
\mathrm{Tr}_{\mathrm{grav}} R_+^2 \;=\; \tilde v_1(R,r_3)\,\alpha_1,\qquad \alpha_1=a\wedge b=\tfrac14(e^{12}\wedge e^{34}),
\end{equation}
```
with *no* components along $`\alpha_2`$ or $`\alpha_3`$. Using the trace convention <a href="#eq:grav-trace-conv" data-reference-type="eqref" data-reference="eq:grav-trace-conv">[eq:grav-trace-conv]</a>, the coefficient is
``` math
\begin{equation}
\label{eq:v1-explicit}
\tilde v_1(R,r_3) \;=\; 8\,A^2 \;=\; 8\,\frac{r_3^2}{r_1^2 r_2^2}\,.
\end{equation}
```
Higher‑order terms in $`A`$ cancel in $`\mathrm{Tr}_{\mathrm{grav}} R_+^2`$ by symmetry of the left‑invariant frame; equation <a href="#eq:v1-explicit" data-reference-type="eqref" data-reference="eq:v1-explicit">[eq:v1-explicit]</a> is exact in this normalization.

# Lens$`\times`$Nil coefficients: $`A(R_1,R)`$, $`B(R_1,R)`$, $`W_1(R_1,R)`$, $`W_3(R_1,R)`$

With $`R_2=R_3=:R`$, take an orthonormal left-invariant coframe $`(\eta^1,\eta^2,\eta^3,\sigma^4,\sigma^5,\sigma^6)`$ scaled so that
``` math
\mathrm{d}\eta^i = \lambda\,\varepsilon_{ijk}\,\eta^j\wedge\eta^k,\qquad
\mathrm{d}\sigma^4=\mathrm{d}\sigma^5=0,\qquad \mathrm{d}\sigma^6=\nu\,\sigma^4\wedge\sigma^5,
```
where $`\lambda=\lambda(R_1)`$ and $`\nu=\nu(R)`$ scale as $`R_1^{-1}`$ and $`R^{-1}`$, respectively. With
``` math
J= R_1^2\,\eta^1\wedge\eta^2 + R^2\,\eta^3\wedge\sigma^6 + R^2\,\sigma^4\wedge\sigma^5,
```
one computes the torsion $`H=\mathrm{i}(\bar\partial-\partial)J`$ (non-integrable structure) and
``` math
\begin{equation}
\label{eq:Lens-dH-explicit}
\mathrm{d}H \;=\; W_1(R_1,R)\,\beta_1 + W_3(R_1,R)\,\beta_3,\qquad
\beta_1:=\eta^{12}\wedge\eta^3\wedge\sigma^6,\quad \beta_3:=\eta^3\wedge\sigma^{45}\wedge\sigma^6,
\end{equation}
```
with
``` math
\begin{equation}
\label{eq:W13-explicit}
W_1(R_1,R)=2\,\lambda^2\,R^2,\qquad W_3(R_1,R)=\lambda\,\nu\,R^2.
\end{equation}
```
For the torsional spin curvature, a left‑invariant computation gives (with the gravitational trace convention <a href="#eq:grav-trace-conv" data-reference-type="eqref" data-reference="eq:grav-trace-conv">[eq:grav-trace-conv]</a>)
``` math
\begin{equation}
\label{eq:Lens-Rplus2}
\mathrm{Tr}_{\mathrm{grav}} R_+^2 \;=\; A(R_1,R)\,\beta_1 + B(R_1,R)\,\beta_3,\qquad
A(R_1,R)=4\,\lambda^2+\mathcal{O}(\lambda^2\nu^2),\quad B(R_1,R)=4\,\nu^2+\mathcal{O}(\lambda^2\nu^2).
\end{equation}
```
Substituting <a href="#eq:W13-explicit" data-reference-type="eqref" data-reference="eq:W13-explicit">[eq:W13-explicit]</a> and <a href="#eq:Lens-Rplus2" data-reference-type="eqref" data-reference="eq:Lens-Rplus2">[eq:Lens-Rplus2]</a> into <a href="#lens-eqs" data-reference-type="eqref" data-reference="lens-eqs">[lens-eqs]</a> yields
``` math
2(2\pi)^2 f^2 - 4\,\lambda^2 = \frac{8}{\alpha'}\,\lambda^2\,R^2,\qquad
2(2\pi)^2 h^2 - 4\,\nu^2 = \frac{4}{\alpha'}\,\lambda\,\nu\,R^2,
```
which fix the ratio $`R_1/R`$ for any fixed integers $`(f,h)\neq(0,0)`$. Higher‑order $`\mathcal{O}(\lambda^2\nu^2)`$ terms are suppressed when the fibration curvatures are small; *for definiteness we assume* $`\lambda\nu\ll\min\{\lambda^2,\nu^2\}`$, so that mixed corrections are parametrically subleading. Including them simply perturbs the fixed point continuously.

# MTT alignment: projection, compactification, and FCC

<div class="remark">

**Remark 1** (Purpose of this appendix). *This appendix is *expository*. It explains how the heterotic flux solutions in the main text fit into the Modal Triplet Theory (MTT) coherent-sector framework and the Fixed Points (FP) stability machinery. The constitutive assumptions and definitions live in the MTT Foundation . The analytic and fixed-point results referenced here are proved in FP I–II and FP V–VI .*

</div>

## Invariant truncation as a coherent projection

Let $`\Omega:=X^6`$ be the internal manifold (e.g. Iwasawa or Lens$`\times`$Nil) equipped with the chosen SU(3) structure. Let $`\Delta_\Omega\ge 0`$ denote the (nonnegative) Laplace-type operator relevant to the mode bundle used in the compactification ansatz (e.g. scalar Laplacian or connection Laplacian on a fixed Hermitian bundle).

Let $`\Pi_{\mathrm{coh}}`$ denote the orthogonal projector onto the coherent spectral band used in the truncation. In the left-invariant setting of this paper, the “coherent” subspace is the finite-dimensional space spanned by invariant harmonic representatives (or the chosen invariant eigenspace).

<div id="prop:C1" class="proposition">

**Proposition 2** (Invariant truncation as coherent projection). *In the left-invariant ansatz employed in Sections <a href="#sec:iwasawa" data-reference-type="ref" data-reference="sec:iwasawa">[sec:iwasawa]</a>–<a href="#sec:lensnil" data-reference-type="ref" data-reference="sec:lensnil">8</a>, restriction to invariant degrees of freedom coincides with applying a coherent projector $`\Pi_{\mathrm{coh}}`$ defined by spectral calculus on $`\Delta_\Omega`$ (or the relevant Laplace-type operator).*

</div>

<div class="proof">

*Proof.* On a compact quotient (or compact factor) with left-invariant structure, the invariant subspace is finite-dimensional and invariant under $`\Delta_\Omega`$. Hence $`\Delta_\Omega`$ preserves the invariant space and can be diagonalized there. Let $`E_0`$ denote the chosen invariant coherent band. Then the orthogonal projector onto $`E_0`$ is given by the spectral projector $`\Pi_{\mathrm{coh}}`$ restricted to the invariant sector. This is the same spectral-projector mechanism used throughout FP I–II , with standard functional calculus references in . ◻

</div>

## Compactification constraints as admissibility conditions

In heterotic flux compactification, the Strominger system and anomaly cancellation constrain $`(g,J,\Omega,H,A)`$. In MTT language, these constraints define an *admissible coherent configuration*: coherent evolution is asserted only within the domain where the coherent projector exists and stability margins remain positive .

<div id="prop:C2" class="proposition">

**Proposition 3** (Constraints as admissibility). *Let $`\mathcal{C}`$ denote the configuration space of internal data (metric/SU(3) structure, flux, and gauge connection) restricted to the coherent/invariant sector. Then the system of equations used in this paper (balanced condition, holomorphy/HYM, and Green–Schwarz anomaly cancellation) defines an admissible subset $`\mathcal{A}\subset\mathcal{C}`$. A compactification solution is a point of $`\mathcal{A}`$.*

</div>

<div class="remark">

**Remark 4**. *This viewpoint matches the updated FP V/VI interpretation: “drivers” are not forces but admissibility barriers delimiting the coherent domain . In the heterotic context, the admissible domain is precisely the set where the Strominger system and anomaly constraints are simultaneously coherent and stable .*

</div>

## FCC-style one-step bound (series-consistent form)

The FP-series uses the projected time–$`\tau`$ map
``` math
T_\tau := \Pi_{\mathrm{coh}}\circ \Phi_\tau,
```
where $`\Phi_\tau`$ is the time–$`\tau`$ map of a dissipative flow
``` math
\partial_t \Psi = -A\Psi - N(\Psi),
\qquad A\ge 0,
```
and $`\Pi_{\mathrm{coh}}`$ is the coherent projector. This is the standard setup in FP I–II .

<div id="prop:C3" class="proposition">

**Proposition 5** (FCC-style bound via $`M_1(\tau)`$). *Assume on an invariant bounded set that: (i) $`N`$ is $`L`$-Lipschitz on that set in $`L^2`$, and (ii) the semigroup smoothing on the noncoherent sector satisfies
``` math
\|A^{1/2}e^{-tA}Q\|_{L^2\to L^2}
\le C\,t^{-1/2}e^{-\eta t}
\quad (t>0),
\qquad
\|e^{-tA}\Pi_{\mathrm{coh}}\|_{L^2\to L^2}=1,
```
as in the corrected global formulation used in FP I–II (see also ).*

*Then, for each $`\tau>0`$,
``` math
\|\Phi_\tau(\Psi_1)-\Phi_\tau(\Psi_2)\|_{H^1_F}
\le M_1(\tau)e^{L\tau}\|\Psi_1-\Psi_2\|_{L^2},
\qquad
M_1(\tau):=C\bigl(1+\tau^{-1/2}e^{-\eta\tau}\bigr),
```
and hence
``` math
\|T_\tau(\Psi_1)-T_\tau(\Psi_2)\|_{H^1_F}
\le q(\tau)\,\|\Psi_1-\Psi_2\|_{L^2},
\qquad
q(\tau):=C_\Pi\,M_1(\tau)e^{L\tau}.
```*

</div>

<div class="remark">

**Remark 6**. *This is the series-standard bound after the FP I correction: the exponential decay belongs to the $`Q`$ contribution and does not force decay on $`\mathrm{Ran}(\Pi_{\mathrm{coh}})`$ .*

</div>

## Compactness/condensing inheritance (Schauder/Darbo)

<div id="prop:C4" class="proposition">

**Proposition 7** (Inheritance of existence mechanisms). *The existence mechanisms used in FP I–II apply to the coherent/invariant compactification setting as follows:*

1.  *If the relevant base domain is compact and base smoothing holds, then $`T_\tau`$ is compact on bounded sets and Schauder fixed point applies (FP I, FP II) .*

2.  *If the base is noncompact but a confining potential yields tail control, then the output-cutoff decomposition implies $`T_\tau`$ is Sadovskiı̆-condensing on invariant energy sublevels, so Darbo applies (FP I) .*

</div>

<div class="remark">

**Remark 8**. *The heterotic solutions in this paper are obtained by explicit left-invariant construction . Proposition <a href="#prop:C4" data-reference-type="ref" data-reference="prop:C4">7</a> is included to show compatibility with the general MTT/FP existence framework .*

</div>

# Selection/admissibility interpretation for heterotic flux vacua

<div class="remark">

**Remark 9** (Purpose). *This appendix explains how the heterotic flux compactifications constructed in this paper fit the updated MTT interpretation: “Drivers” are not forces; they are *admissibility barriers* that delimit the coherent domain .*

</div>

## Admissibility versus teleology

In FP V and FP VI, selection is treated as an admissibility condition: coherent evolution is asserted only while the configuration remains in the domain where (i) the coherent projector is well-defined and bounded and (ii) stability margins remain positive .

In the heterotic compactification context, admissibility corresponds to the simultaneous satisfaction of:

1.  bounded geometry of the internal manifold and bundles (uniform elliptic estimates) ;

2.  a nondegenerate spectral gap / coherent band (no collapse of the lowest band) ;

3.  the Strominger/HYM constraints (coherent compatibility) ;

4.  the Green–Schwarz Bianchi identity (anomaly cancellation) .

When these fail (e.g. collapse of injectivity radius, degeneration closing the spectral gap, or loss of boundedness of the relevant projector), the coherent description ceases to apply, consistent with the FP V admissibility-barrier picture .

## Selection potential as a barrier functional (not dynamics)

One may define a scalar diagnostic functional on the space of internal configurations, for example:
``` math
\Phi_{\mathrm{sel}} := -\sum_a w_a\,\lambda_a,
\qquad w_a>0,
```
or any equivalent monotone functional that diverges as gaps close and coherence fails.

<div class="remark">

**Remark 10**. *In the updated MTT interpretation (FP V/VI), $`\Phi_{\mathrm{sel}}`$ is *not* added to the equations of motion. Its role is to identify the boundary of admissibility: divergence corresponds to the infinite energetic cost of maintaining coherence under restriction to $`\mathrm{Ran}(\Pi_{\mathrm{coh}})`$ .*

</div>

## Landscape reduction in heterotic flux space

Let $`\mathcal{B}`$ denote the space of candidate heterotic flux data $`(X^6,J,\Omega,H,A)`$ satisfying quantization/topology constraints. Standard string theory allows large families of such data.

In MTT, the physically admissible set is the subset
``` math
\mathcal{B}_{\mathrm{adm}} :=
\{\beta\in\mathcal{B}:\ \text{bounded geometry + spectral gap + bounded }\Pi_{\mathrm{coh}} + \text{stability margins}\}
```
as formalized in the coherent admissibility viewpoint . Degenerations (e.g. collapsing cycles) that destroy bounded geometry or close the relevant spectral gap lie outside $`\mathcal{B}_{\mathrm{adm}}`$ and are excluded by admissibility, rather than by external enforcement.

## Interpretation of discrete loci in this paper

A salient feature of the Lens$`\times`$Nil example and of the componentwise anomaly cancellation in the Iwasawa example is that the system selects isolated or lower-dimensional loci in parameter space (e.g. fixed ratios of radii) .

In the MTT interpretation, these loci are not “chosen” by teleology. They are the intersection of:

- topological constraints (quantized flux, Chern classes) ;

- differential constraints (balanced/HYM/Strominger system) ;

- coherence admissibility (gap/projector/stability) .

Hence discreteness is a structural consequence of admissibility and stability, consistent with the FP-series selection framework.

<div class="thebibliography">

99

H. Amann. *Linear and Quasilinear Parabolic Problems, Volume I*. Birkhäuser, 1995.

K. Becker, M. Becker, K. Dasgupta, and P. S. Green. Compactifications of heterotic theory on non-Kähler complex manifolds. *Journal of High Energy Physics*, 2003(04):007, 2003. arXiv:hep-th/0301161. doi:10.1088/1126-6708/2003/04/007.

X. de la Ossa and E. E. Svanes. Holomorphic bundles and the moduli space of $`N=1`$ supersymmetric heterotic compactifications. *Journal of High Energy Physics*, 2014(10):123, 2014. arXiv:1402.1725. doi:10.1007/JHEP10(2014)123.

M. Fernández, S. Ivanov, L. Ugarte, and R. Villacampa. Non-Kähler heterotic string compactifications with non-zero fluxes and constant dilaton. *Communications in Mathematical Physics*, 288:677–697, 2009. arXiv:0804.1648. doi:10.1007/s00220-008-0714-z.

J.-X. Fu and S.-T. Yau. The theory of superstring with flux on non-Kähler manifolds and the complex Monge–Ampère equation. *Journal of Differential Geometry*, 78:369–428, 2008. doi:10.4310/jdg/1207834550.

E. Hebey. *Nonlinear Analysis on Manifolds: Sobolev Spaces and Inequalities*. American Mathematical Society, 2000.

D. Henry. *Geometric Theory of Semilinear Parabolic Equations*. Springer, 1981.

C. M. Hull. Compactifications of the heterotic superstring. *Physics Letters B*, 178(4):357–364, 1986. doi:10.1016/0370-2693(86)91393-6.

T. Kato. *Perturbation Theory for Linear Operators*. Springer, 1976.

J. Li and S.-T. Yau. Hermitian–Yang–Mills Connection on Non-Kähler Manifolds. In S.-T. Yau, editor, *Mathematical Aspects of String Theory*, volume 1 of *Advanced Series in Mathematical Physics*, pages 560–573. World Scientific, Singapore, 1987.

P. Nero. *Fixed Points I: Fixed Points over Multi–Bundle Manifolds*. Zenodo, 2025. Preprint.

P. Nero. *Fixed Points II: Fixed Points in a 10D Modal Model*. Zenodo, 2025. Preprint.

P. Nero. *Fixed Points V: Curvature Coupling, Multi-Structure Dynamics and Drivers*. Zenodo, 2025. doi:10.5281/zenodo.16949504.

P. Nero. *Fixed Points VI: Formal Synthesis and Physical Interpretations*. Zenodo, 2025. doi:10.5281/zenodo.16949636.

P. Nero. *Flux Compactifications in Heterotic String Theory*. Preprint, 2025.

P. Nero. *Modal Triplet Theory: Foundation — A Rigorous Fixed-Point Framework for Unified 4D Physics*. Zenodo, 2025. doi:10.5281/zenodo.16949763.

P. Nero. *Modal Triplet Theory: From MTT to the Strominger (Heterotic Flux) System*. Zenodo, 2025. doi:10.5281/zenodo.17071766.

P. Nero. *Modal Triplet Theory: MTT as a Selection Principle for Heterotic Flux Compactifications*. Preprint, 2025.

A. Strominger. Superstrings with torsion. *Nuclear Physics B*, 274(2):253–284, 1986. doi:10.1016/0550-3213(86)90286-5.

</div>

[^1]: Eqs. <a href="#HS1" data-reference-type="eqref" data-reference="HS1">[HS1]</a>–<a href="#HS2" data-reference-type="eqref" data-reference="HS2">[HS2]</a> are equivalent to $`\delta\chi=0`$ (gaugino) for an HYM connection and to $`\delta\psi_\mu=\delta\lambda=0`$ (gravitino/dilatino) for the Bismut connection with $`H=\mathrm{i}(\bar\partial-\partial)J`$ and $`d(J^2)=0`$; see .

[^2]: We use the $`E_6`$ cubic normalized so that $`d_{abc}d^{abc}=1`$ in the convention where the $`\mathbf{27}`$ has unit norm. Other common normalizations simply rescale $`\lambda_{123}`$ by a fixed group-theory factor.
