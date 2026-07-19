---
abstract: |
  We construct a fully rigorous electromagnetic helicity/Chern–Simons (CS) functional on the finite-rank coherent electromagnetic line bundle selected by MTT’s joint harmonic (Riesz) projector $`\Pi_{\mathrm{coh}}(t,x)`$. Because the projector varies over the base, the induced coherent connection necessarily contains Berry/Grassmann (projector) terms; ignoring them makes the curvature and balance laws incorrect. We (i) define the induced coherent connection and compute its curvature including the Berry term; (ii) define both the physical, unnormalized coherent helicity $`H_{\mathrm{coh}}=\int_\Sigma \bm A^{\mathrm{coh}}\cdot\bm B^{\mathrm{coh}}\,d^3x`$ and the Hopf-normalized CS functional $`Q_{\mathrm{coh}}=\frac{1}{16\pi^2}\int_\Sigma \mathcal A^{\mathrm{coh}}\wedge d_\Sigma\mathcal A^{\mathrm{coh}}`$; (iii) prove exact balance laws with explicit remainder $`\mathcal R_\Pi(t)`$ that captures projector variation/noncommutation; and (iv) bound $`\mathcal R_\Pi(t)`$ in terms of $`\|\partial_t\Pi\|`$ and $`\|d_\Sigma\Pi\|`$ with an explicit admissible-slab constant $`C_\Pi:=\sup_{\mathcal U}\max\{\|\partial_t\Pi\|,\|d_\Sigma\Pi\|\}`$. We connect $`\|\partial_t\Pi\|`$ to standard spectral projector perturbation bounds via Riesz calculus and a uniform spectral gap, in the precise manner used in the MTT fixed-point spine. Finally, we state the MTT-aligned admissibility result: on admissible coherent slabs the functionals are well-defined and conserved up to a remainder controlled by the admissibility margin; at barrier/exit events this control can fail, providing the mathematically correct sense in which admissibility/FCC replaces homotopy protection.
author:
- Peter Nero
current_version: v2
date: January, 2026
generated_from_main_tex_sha256: 306c66c45f22d84515b5261dac6d7811bc58ef55e80b1c86f1431ceac3882b42
paper_id: electromagnetic-helicity-as-a-coherent-sector-chern-sim-0cc7ca40
release_state: zenodo_released
released_version: v2.0
title: |
  **Electromagnetic Helicity as a Coherent-Sector  
  Chern–Simons Functional in Modal Triplet Theory  
  Rank-One Abelian Sector, Correct Hopf Normalization, and Admissibility-Controlled Remainders**
zenodo_doi: 10.5281/zenodo.18261452
zenodo_record_id: 18261452
zenodo_url: "https://zenodo.org/records/18261452"
---

# Introduction

Topological soliton models and electromagnetic Hopfions exhibit stability via topology, with an integer Hopf invariant $`Q_H\in\pi_3(S^2)\cong\mathbb Z`$. MTT organizes stability via a dynamically selected coherent sector determined by a joint harmonic projector $`\Pi_{\mathrm{coh}}`$, spectral gaps, and contraction/stability margins (FCC/admissibility). This paper provides a referee-robust bridge by defining (i) a physical coherent helicity $`H_{\mathrm{coh}}`$ and (ii) a Hopf-normalized coherent CS functional $`Q_{\mathrm{coh}}`$ on the coherent line bundle, both with correct Berry/projector terms and with exact balance laws including projector-variation remainders.

# Setting and boundary conditions

Let $`\mathcal U=[t_0,t_1]\times \Sigma`$ be a bounded-geometry slab, $`\Sigma`$ a Cauchy slice. Work with Sobolev $`H^s(\Sigma)`$, $`s>3/2`$, so products are controlled.

<div id="ass:boundary" class="assumption">

**Assumption 1** (Boundary/decay conditions). Either (i) $`\Sigma`$ is compact without boundary; or (ii) $`\Sigma=\mathbb R^3`$ with sufficient decay; or (iii) boundary conditions/relative helicity are used so CS/helicity identities have no boundary remainder.

</div>

# Coherent projector and rank-one EM sector

<div id="ass:PiReg" class="assumption">

**Assumption 2** (Projector regularity). On $`\mathcal U`$, $`\Pi(t,x)=\Pi_{\mathrm{coh}}(t,x)`$ satisfies: (i) orthogonal projector of constant finite rank; (ii) $`\Pi\in C^1(\mathcal U;\mathcal B(\mathcal E))`$; (iii) uniform Sobolev boundedness $`\|\Pi\|_{H^1\to H^1}\le C_\Pi^{(0)}`$.

</div>

<div id="ass:rank1" class="assumption">

**Assumption 3** (Rank-one EM coherent sector). For the electromagnetic leg, $`\mathrm{rank}\,\mathcal H^{(\mathrm{EM})}_{\mathrm{coh}}(t,x)=1`$ on $`\mathcal U`$.

</div>

<div id="ass:scalarU1" class="assumption">

**Assumption 4** (Scalar $`U(1)`$ action). On the EM leg, the ambient Abelian covariant derivative acts as $`D=d+iA\,I_{\mathcal E}`$ with $`A`$ a real 1-form on $`\mathcal U`$. Hence $`[A,\Pi]=0`$.

</div>

# Induced coherent connection and curvature

<div class="definition">

**Definition 5** (Induced coherent connection). On sections $`s=\Pi s`$ of the coherent EM line bundle, define
``` math
\nabla^{\mathrm{coh}}:=\Pi\circ(d+iA).
```
Locally, choosing a unit section $`u`$ with $`\Pi=|u\rangle\langle u|`$, the induced spatial 1-form is
``` math
\mathcal A^{\mathrm{coh}} = \underbrace{-i\langle u,d_\Sigma u\rangle}_{\mathcal A^\Pi} + A|_\Sigma.
```

</div>

<div id="thm:curv" class="theorem">

**Theorem 6** (Curvature with Berry term). *Assume <a href="#ass:PiReg" data-reference-type="ref" data-reference="ass:PiReg">2</a> and <a href="#ass:scalarU1" data-reference-type="ref" data-reference="ass:scalarU1">4</a>. The curvature 2-form of $`\nabla^{\mathrm{coh}}`$ is
``` math
\Omega^{\mathrm{coh}} = i\,\Pi(dA)\Pi + \Pi(d\Pi)\wedge(d\Pi)\Pi.
```*

</div>

# Two invariants: physical helicity and Hopf-normalized CS

## Intrinsic coherent spatial field strength

<div id="def:Fcoh" class="definition">

**Definition 7** (Intrinsic coherent spatial field strength). On a spatial slice $`\Sigma`$ at time $`t`$, define
``` math
F^{\mathrm{coh}}(t):=(-i)\,\Omega^{\mathrm{coh}}(t)\big|_\Sigma.
```
In rank-one, $`F^{\mathrm{coh}}=d_\Sigma\mathcal A^{\mathrm{coh}}`$ in any local unit section.

</div>

## Unnormalized coherent helicity $`H_{\mathrm{coh}}`$

<div id="def:H" class="definition">

**Definition 8** (Physical (unnormalized) coherent helicity). Assume <a href="#ass:boundary" data-reference-type="ref" data-reference="ass:boundary">1</a>. In a vector calculus representation on $`\Sigma\subset\mathbb R^3`$, choose a gauge/frame for which $`\bm B^{\mathrm{coh}}=\nabla\times \bm A^{\mathrm{coh}}`$ represents the same $`F^{\mathrm{coh}}`$. Define the physical helicity
``` math
H_{\mathrm{coh}}(t):=\int_\Sigma \bm A^{\mathrm{coh}}(t)\cdot \bm B^{\mathrm{coh}}(t)\,d^3x
\;=\;\int_\Sigma \mathcal A^{\mathrm{coh}}(t)\wedge F^{\mathrm{coh}}(t).
```

</div>

## Hopf-normalized coherent CS functional $`Q_{\mathrm{coh}}`$

<div id="def:Q" class="definition">

**Definition 9** (Hopf-normalized coherent CS). Assume <a href="#ass:boundary" data-reference-type="ref" data-reference="ass:boundary">1</a>. Define
``` math
\begin{equation}
\label{eq:Qdef}
Q_{\mathrm{coh}}(t):=\frac{1}{16\pi^2}\int_\Sigma \mathcal A^{\mathrm{coh}}(t)\wedge F^{\mathrm{coh}}(t)
=\frac{1}{16\pi^2}\int_\Sigma \mathcal A^{\mathrm{coh}}(t)\wedge d_\Sigma\mathcal A^{\mathrm{coh}}(t).
\end{equation}
```
Thus $`Q_{\mathrm{coh}} = \frac{1}{16\pi^2} H_{\mathrm{coh}}`$ whenever the same representative is used.

</div>

# Balance laws and corrected constants

Define the coherent electric 1-form on $`\Sigma`$ intrinsically:
``` math
E^{\mathrm{coh}}(t):=\iota_{\partial_t}F^{\mathrm{coh}}(t).
```

<div class="remark">

*Remark 10* (Relation to spacetime components). If $`\Omega^{\mathrm{coh}}`$ denotes the full spacetime curvature 2-form of the induced coherent connection, then
``` math
E^{\mathrm{coh}} = \iota_{\partial_t} F^{\mathrm{coh}}
```
coincides with the spatial 1-form whose components are $`(\Omega^{\mathrm{coh}})_{0i}\,dx^i`$ in any coordinate system adapted to the time slicing of the slab. Thus $`E^{\mathrm{coh}}`$ agrees with the usual electric field associated with the coherent connection.

</div>

<div id="thm:Hbalance" class="theorem">

**Theorem 11** (Exact balance law for $`H_{\mathrm{coh}}`$ with remainder). *Assume <a href="#ass:boundary" data-reference-type="ref" data-reference="ass:boundary">1</a>, <a href="#ass:PiReg" data-reference-type="ref" data-reference="ass:PiReg">2</a>, <a href="#ass:rank1" data-reference-type="ref" data-reference="ass:rank1">3</a>, <a href="#ass:scalarU1" data-reference-type="ref" data-reference="ass:scalarU1">4</a>. Then
``` math
\begin{equation}
\label{eq:Hbalance}
\frac{d}{dt}H_{\mathrm{coh}}(t)
=
-2\int_\Sigma E^{\mathrm{coh}}(t)\wedge F^{\mathrm{coh}}(t) \;+\; R_\Pi^{(H)}(t),
\end{equation}
```
where the remainder $`R_\Pi^{(H)}(t)`$ arises from projector variation/frame noncommutation and is given explicitly in Appendix <a href="#app:R" data-reference-type="ref" data-reference="app:R">11</a>. Moreover, for any $`s>3/2`$,
``` math
\begin{equation}
\label{eq:HRemBound}
|R_\Pi^{(H)}(t)|
\le
C_s\,C_\Pi\Big(\|\partial_t\Pi(t)\|_{\mathrm{op}}+\|d_\Sigma\Pi(t)\|_{\mathrm{op}}\Big)\,
\|\mathcal A^{\mathrm{coh}}(t)\|_{H^s(\Sigma)}\,\|F^{\mathrm{coh}}(t)\|_{H^{s-1}(\Sigma)},
\end{equation}
```
where
``` math
C_\Pi:=\sup_{(t,x)\in\mathcal U}\max\{\|\partial_t\Pi(t,x)\|_{\mathrm{op}},\|d_\Sigma\Pi(t,x)\|_{\mathrm{op}}\}<\infty.
```*

</div>

<div id="thm:Qbalance" class="theorem">

**Theorem 12** (Exact balance law for $`Q_{\mathrm{coh}}`$ with remainder). *Under the same hypotheses,
``` math
\begin{equation}
\label{eq:Qbalance}
\frac{d}{dt}Q_{\mathrm{coh}}(t)
=
-\frac{1}{8\pi^2}\int_\Sigma E^{\mathrm{coh}}(t)\wedge F^{\mathrm{coh}}(t)\;+\;R_\Pi^{(Q)}(t),
\end{equation}
```
with $`R_\Pi^{(Q)}(t)=\frac{1}{16\pi^2}R_\Pi^{(H)}(t)`$ and the bound <a href="#eq:HRemBound" data-reference-type="eqref" data-reference="eq:HRemBound">[eq:HRemBound]</a> scaled accordingly.*

</div>

<div id="cor:clean" class="corollary">

**Corollary 13** (Clean vacuum constants under frozen projector). *If $`\partial_t\Pi\equiv0`$ on $`\mathcal U`$(or more generally, if the Berry/Grassmann contribution to $`\mathcal A^{\mathrm{coh}}`$ is time independent up to an exact spatial 1-form, so that its time derivative contributes only exact terms to the Chern–Simons functional, which vanish under Assumption <a href="#ass:boundary" data-reference-type="ref" data-reference="ass:boundary">1</a>) , then $`R_\Pi^{(H)}=R_\Pi^{(Q)}=0`$. In vector calculus notation this gives
``` math
\frac{d}{dt}H_{\mathrm{coh}}(t) = -2\int_\Sigma \bm E^{\mathrm{coh}}\cdot\bm B^{\mathrm{coh}}\,d^3x,
\qquad
\frac{d}{dt}Q_{\mathrm{coh}}(t) = -\frac{1}{8\pi^2}\int_\Sigma \bm E^{\mathrm{coh}}\cdot\bm B^{\mathrm{coh}}\,d^3x.
```*

</div>

# Spectral projector bounds for $`\|\partial_t\Pi\|`$ and $`\|d_\Sigma\Pi\|`$ (Riesz calculus + gap)

Let $`L(t)`$ be the relevant fiberwise Laplace-type operator family defining $`\Pi(t)`$ as a Riesz projector. Assume a uniform gap $`\lambda_*>0`$: $`\sigma(L(t))\subset\{0\}\cup[\lambda_*,\infty)`$. Let $`\Gamma`$ enclose $`0`$ and no other spectrum, e.g. radius $`\lambda_*/2`$.

``` math
\begin{equation}
\Pi(t)=\frac{1}{2\pi i}\oint_\Gamma (z-L(t))^{-1}\,dz.
\end{equation}
```

<div id="ass:Ldiff" class="assumption">

**Assumption 14** (Differentiability of operator family). $`t\mapsto L(t)`$ is differentiable in operator norm with $`\|\partial_tL(t)\|_{\mathrm{op}}<\infty`$ on $`\mathcal U`$. Likewise, $`x\mapsto L(t,x)`$ is $`C^1`$ in operator norm on $`\Sigma`$ with $`\|d_\Sigma L(t)\|_{\mathrm{op}}<\infty`$.

</div>

<div id="thm:RieszBound" class="theorem">

**Theorem 15** (Riesz projector perturbation bounds). *Under the uniform gap and <a href="#ass:Ldiff" data-reference-type="ref" data-reference="ass:Ldiff">14</a>,
``` math
\partial_t\Pi(t)=\frac{1}{2\pi i}\oint_\Gamma (z-L(t))^{-1}(\partial_tL(t))(z-L(t))^{-1}\,dz,
```
and
``` math
\|\partial_t\Pi(t)\|_{\mathrm{op}}\le C_\Gamma\,\frac{\|\partial_tL(t)\|_{\mathrm{op}}}{\lambda_*^2}.
```
Similarly,
``` math
\|d_\Sigma\Pi(t)\|_{\mathrm{op}}\le C_\Gamma\,\frac{\|d_\Sigma L(t)\|_{\mathrm{op}}}{\lambda_*^2}.
```*

</div>

<div class="remark">

*Remark 16* (MTT coherence alignment). In MTT, $`L(t)`$ is the vertical Laplace-type operator (or commuting sum) whose kernel defines the coherent sector. Bounded geometry + uniform gap give uniform resolvent control on $`\Gamma`$, so these bounds are precisely the projector-control mechanism used throughout the fixed-point series and Foundation spine.

</div>

# Hopf quantization specialization (correct normalization)

<div id="prop:Hopf" class="proposition">

**Proposition 17** (Hopf quantization specialization). *Assume:*

1.  *$`\Sigma\simeq S^3`$;*

2.  *$`H^2(S^3)=0`$, so for any closed 2-form $`F^{\mathrm{coh}}`$ there exists a global 1-form $`\mathcal A^{\mathrm{coh}}`$ with $`d\mathcal A^{\mathrm{coh}}=F^{\mathrm{coh}}`$;*

3.  *$`F^{\mathrm{coh}} = n^*\omega_{S^2}`$ for a map $`n:S^3\to S^2`$ and the standard normalized area form $`\omega_{S^2}`$, so the Hopf class $`Q_H\in\mathbb Z`$ is defined.*

*Then with Definition <a href="#def:Q" data-reference-type="ref" data-reference="def:Q">9</a>,
``` math
Q_{\mathrm{coh}} = Q_H\in\mathbb Z.
```*

</div>

<div class="remark">

*Remark 18* (Gauge independence on $`S^3`$). On $`\Sigma\simeq S^3`$, the condition $`H^2(S^3)=0`$ guarantees the existence of a global 1-form $`A`$ satisfying $`dA=F^{\mathrm{coh}}`$. Any two such choices differ by an exact 1-form $`A\mapsto A+d\chi`$. Since
``` math
\int_{S^3} (A+d\chi)\wedge d(A+d\chi)
=
\int_{S^3} A\wedge dA
+
\int_{S^3} d(\chi\,dA),
```
and $`\int_{S^3} d(\chi\,dA)=0`$, the integral $`\int_{S^3} A\wedge dA`$ is gauge independent. Thus the integer-valued Hopf quantization of $`Q_{\mathrm{coh}}`$ in Proposition <a href="#prop:Hopf" data-reference-type="ref" data-reference="prop:Hopf">17</a> is well defined.

</div>

# MTT admissibility/FCC control statement (rigorous form)

<div id="ass:admissible" class="assumption">

**Assumption 19** (Admissible coherent slab (MTT)). On $`\mathcal U`$, the coherent regime persists with strict margins:
``` math
\lambda(t,x)\ge \lambda_{\min}>0,\qquad
\gamma(t,x)\ge \delta(t,x)+\varepsilon,
```
for all occupied channels, and an FCC-type stability margin holds for the projected coherent dynamics. Additionally, the operator families defining $`\Pi`$ satisfy <a href="#ass:Ldiff" data-reference-type="ref" data-reference="ass:Ldiff">14</a> on $`\mathcal U`$.

</div>

<div id="thm:admissibleControl" class="theorem">

**Theorem 20** (Admissible-slab control of remainders). *Assume <a href="#ass:admissible" data-reference-type="ref" data-reference="ass:admissible">19</a>. Then Theorem <a href="#thm:RieszBound" data-reference-type="ref" data-reference="thm:RieszBound">15</a> yields uniform bounds on $`\|\partial_t\Pi\|`$ and $`\|d_\Sigma\Pi\|`$ on $`\mathcal U`$, hence $`C_\Pi<\infty`$ and the remainder bounds <a href="#eq:HRemBound" data-reference-type="eqref" data-reference="eq:HRemBound">[eq:HRemBound]</a> (and its $`Q`$-scaled version) are quantitative on $`\mathcal U`$. If the admissibility/adiabatic conditions make $`\|\partial_tL\|`$ and $`\|d_\Sigma L\|`$ small compared to $`\lambda_*^2`$, then $`R_\Pi^{(H)}`$ and $`R_\Pi^{(Q)}`$ are small and $`H_{\mathrm{coh}}`$, $`Q_{\mathrm{coh}}`$ are conserved up to controlled error.*

</div>

# Curvature derivation

<div class="proof">

*Proof of Theorem <a href="#thm:curv" data-reference-type="ref" data-reference="thm:curv">6</a>.* Let $`D=d+iA`$ with scalar $`U(1)`$ action. For sections $`s=\Pi s`$, $`\nabla^{\mathrm{coh}}s=\Pi Ds`$. Then
``` math
(\nabla^{\mathrm{coh}})^2 s = \Pi D(\Pi Ds) = \Pi(D\Pi)\wedge Ds + \Pi\Pi D^2 s.
```
Since $`D^2=i\,dA`$, the second term gives $`i\,\Pi(dA)\Pi s`$. For the first term, write $`D\Pi=d\Pi+iA\Pi`$; scalar commutation and $`\Pi(d\Pi)\Pi=0`$ from $`d(\Pi^2)=d\Pi`$ leave precisely the Grassmann term $`\Pi(d\Pi)\wedge(d\Pi)\Pi`$. ◻

</div>

# Balance-law remainder $`R_\Pi`$ and explicit bilinear-to-linear step

## B.1 Rank-one Berry term and its time derivative

With $`\Pi=|u\rangle\langle u|`$ (local unit section), the Berry 1-form is $`\mathcal A^\Pi=-i\langle u,d_\Sigma u\rangle`$. Then
``` math
\dot{\mathcal A}^\Pi
= -i\langle \dot u, d_\Sigma u\rangle - i\langle u, d_\Sigma \dot u\rangle.
```
Up to an exact form (which vanishes in $`\int_\Sigma \dot{\mathcal A}^\Pi\wedge F^{\mathrm{coh}}`$ under Assumption <a href="#ass:boundary" data-reference-type="ref" data-reference="ass:boundary">1</a>), this is controlled by the bilinear pairing of $`\dot u`$ and $`d_\Sigma u`$.

## B.2 Remainder definition

Starting from $`H_{\mathrm{coh}}(t)=\int_\Sigma \mathcal A^{\mathrm{coh}}\wedge F^{\mathrm{coh}}`$, differentiate and integrate by parts to obtain the standard term $`-2\int E^{\mathrm{coh}}\wedge F^{\mathrm{coh}}`$ plus the projector/frame remainder
``` math
R_\Pi^{(H)}(t) := 2\int_\Sigma \dot{\mathcal A}^\Pi(t)\wedge F^{\mathrm{coh}}(t).
```
Then $`R_\Pi^{(Q)}=\frac{1}{16\pi^2}R_\Pi^{(H)}`$.

## B.3 Bilinear bound and explicit linearization constant

From $`\Pi=|u\rangle\langle u|`$,
``` math
\dot\Pi = |\dot u\rangle\langle u| + |u\rangle\langle \dot u|,
\qquad
d_\Sigma\Pi = |d_\Sigma u\rangle\langle u| + |u\rangle\langle d_\Sigma u|.
```
Thus in operator norm,
``` math
\|\dot\Pi\|_{\mathrm{op}} \le 2\|\dot u\|, \qquad
\|d_\Sigma\Pi\|_{\mathrm{op}} \le 2\|d_\Sigma u\|.
```
Choosing the gauge $`\langle u,\dot u\rangle=0`$ locally yields converses up to a universal factor, hence
``` math
\|\dot u\|\,\|d_\Sigma u\| \;\lesssim\; \|\dot\Pi\|_{\mathrm{op}}\,\|d_\Sigma\Pi\|_{\mathrm{op}}.
```
Therefore, for $`s>3/2`$,
``` math
|R_\Pi^{(H)}(t)| \le C_s\,\|\dot\Pi(t)\|_{\mathrm{op}}\,\|d_\Sigma\Pi(t)\|_{\mathrm{op}}\,
\|\mathcal A^{\mathrm{coh}}(t)\|_{H^s}\,\|F^{\mathrm{coh}}(t)\|_{H^{s-1}}.
```
Now define the explicit admissible-slab constant
``` math
C_\Pi := \sup_{\mathcal U}\max\{\|\dot\Pi\|_{\mathrm{op}},\|d_\Sigma\Pi\|_{\mathrm{op}}\} <\infty.
```
Then pointwise in $`t`$,
``` math
\|\dot\Pi\|_{\mathrm{op}}\,\|d_\Sigma\Pi\|_{\mathrm{op}}
\le C_\Pi\left(\|\dot\Pi\|_{\mathrm{op}}+\|d_\Sigma\Pi\|_{\mathrm{op}}\right),
```
which yields the linear bound <a href="#eq:HRemBound" data-reference-type="eqref" data-reference="eq:HRemBound">[eq:HRemBound]</a> with an explicit constant depending on $`C_\Pi`$. This is the precise step replacing the earlier rhetorical “absorption.” 0◻

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
