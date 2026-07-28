---
abstract: |
  We apply the corrected FP–I machinery to a ten-dimensional control setting $`\ensuremath{M_{10}}=\ensuremath{Y^{4}}\times\ensuremath{X^{6}}`$. The compact six-manifold $`\ensuremath{X^{6}}`$ carries three compatible vertical structures represented by strongly commuting nonnegative self-adjoint operators. Overlap is allowed; nesting requires supplied inclusion maps and is not inferred from ranks $`1<2<3`$. In the q79 realization the $`1<2<3`$ flag acts on a separate lane tensor factor, not inside an irreducible HYM gauge bundle, while the shared circle is a separate flat line factor and is not counted as a seventh internal product dimension. We prove existence of projected time–$`\tau`$ fixed points by Schauder/Darbo and coherent uniqueness under base coercivity or strong monotonicity. A projected fixed point is promoted to a full equilibrium only under a strict Lyapunov identity. Fiber gaps control only the noncoherent $`Q`$ sector and are never used as coherent damping.
author:
- Peter Nero
bibliography:
- references.bib
current_version: v4
date: July 2026
generated_from_main_tex_sha256: 886337d171ca309ebce8913f4515e23ecd3aae126d87d0ea029bd5a143bdcf00
paper_id: fixed-points-ii-projected-fixed-points-and-equilibria-i-e079d534
release_state: zenodo_released
released_version: v2.0
title: "Fixed Points II: Projected Fixed Points and Equilibria in a 10D Modal Model"
zenodo_doi: 10.5281/zenodo.18202914
zenodo_record_id: 18202914
zenodo_url: "https://zenodo.org/records/18202914"
---

*Part II of VI in the Fixed Point series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

# Revision note for this edition

Supersedes.  
*Fixed Points II: Projected Fixed Points and Equilibria in a 10D Modal Model*, version 3.

Reason.  
The version 3 correction fixed the ten-dimensional control geometry but still described the q79 $`1<2<3`$ carrier too loosely. The exact projective-module theorem excludes placing a nontrivial parallel flag inside an irreducible stable HYM factor and distinguishes post-projection finite algebra from a physical Galerkin subspace.

Resolution.  
Version 4 retains the corrected FP theorem and places the rank flag on an external lane tensor factor, with the shared differential line as a separate flat scalar factor. It also records that the 27-state algebra is post-projection data and that the six-coordinate strain carrier is a nonlinear quotient shadow rather than a linear subspace of the physical HYM carrier.

Retained result.  
Schauder/Darbo existence and conditional coherent uniqueness survive in the corrected ten-dimensional control realization.

Remaining boundary.  
The selected visible/hidden q79 HYM endpoints, physical action and Hessian, finite invariant subspace or Feshbach execution, physical time, and Lorentzian dynamics require independent source and completion theorems.

# Introduction and scope

We consider $`\ensuremath{M_{10}}=\ensuremath{Y^{4}}\times\ensuremath{X^{6}}`$, where $`(\ensuremath{Y^{4}},g_Y)`$ is a complete Riemannian analytic/control manifold and $`\ensuremath{X^{6}}`$ is compact. The Riemannian base may model a Cauchy-slice control geometry or Euclideanized problem, but is not identified here with physical Lorentzian spacetime. The internal space carries three vertical structures indexed by $`n=1,2,3`$, each equipped with a *nonnegative* self-adjoint vertical operator and a uniform spectral gap. We adopt throughout the corrected FP–I series conventions:

- Laplacians are *nonnegative* ($`\Delta\ge 0`$), and dissipative flows are written $`\partial_t\Psi=-A\Psi-N(\Psi)`$.

- The coherent projector $`\Pi_{\mathrm{coh}}`$ is the joint fiber-harmonic projector, and $`Q:=\mathrm{Id}-\Pi_{\mathrm{coh}}`$.

- Semigroup smoothing is recorded in the global safe form $`\|A^{1/2}e^{-tA}Q\|\lesssim (1+t^{-1/2})e^{-\lambda t}`$ (cf. analytic semigroup bounds in ).

This alignment is what allows FP–III and later papers to reuse damping/smoothing constants without sign drift.

The parameter $`t`$ in the parabolic flow and the step $`\tau`$ below are stabilization parameters. A physical Lorentzian evolution $`U(t_2,t_1)`$ and any relation to this control flow require a separate theorem.

Our goals are: (i) existence of coherent fixed points via Schauder (compact base) or Darbo (noncompact base with confinement); (ii) uniqueness via a Fundamental Contractivity Condition (FCC) on the coherent sector; (iii) explicit constants in standard geometries. General dynamical-systems context may be compared with .

We also cite here FP–I as the foundational reference for the projection/fixed-point strategy: see .

# Geometry and functional setup

## Internal bundles and harmonic alignment

Let $`\ensuremath{X^{6}}`$ be a compact six-manifold. On the common internal Hilbert space $`L^2(\ensuremath{X^{6}})`$ let $`A_n(y)`$, $`n=1,2,3`$, denote the nonnegative self-adjoint operators associated with the selected vertical structures. These structures may overlap. They are nested only if a concrete realization supplies bundle injections or operator intertwiners; rank labels alone do not do so. No product decomposition into three disjoint fibers is assumed. The shared central circle is encoded by a common circle cycle, foliation, or $`U(1)`$ line-bundle connection on $`\ensuremath{X^{6}}`$. Its line-bundle data do not add the dimension of the bundle total space to $`\dim\ensuremath{X^{6}}`$.

<div class="remark">

*Remark 1* (Current q79 carrier and type boundary). The current q79 preprojection architecture is
``` math
\mathcal E_{\rm pre}
=\Gamma(E_{\rm HYM})\widehat\otimes H_{\rm lane}
\widehat\otimes L_{\rm shared}.
```
The projectors $`p_1=\operatorname{diag}(1,0,0)`$, $`p_2=\operatorname{diag}(1,1,0)`$, and $`p_3=I_3`$ act only on $`H_{\rm lane}`$. They encode the relative $`1<2<3`$ lanes without reducing the holonomy of an irreducible stable HYM gauge factor. The common differential line $`L_{\rm shared}`$ is a separate flat scalar factor and is not identified with the curved HYM bundle. This placement is forced by the scalar commutant of an irreducible stable HYM factor .

Two further type distinctions are essential. The accepted 27-state finite algebra is post-projection source data, not a rank-27 Galerkin subspace of the rank-102 physical deformation carrier. Likewise, the six real strain coordinates are an orientation-forgetting nonlinear quotient shadow of spectral data; there is no corresponding equivariant linear rank-six subspace of $`\operatorname{Herm}(3)`$. The fixed-point theorems below use only the declared operators and do not promote either finite object to the physical continuum Hessian.

</div>

We assume bounded internal geometry and smooth bounded dependence on $`y\in\ensuremath{Y^{4}}`$ as in FP–I. A concrete MTT realization must specify $`\ensuremath{X^{6}}`$, the three operators, their domains, and the shared-circle action.

<div id="ass:strong-comm" class="assumption">

**Assumption 2** (Strong commutation of vertical operators). For every $`y`$, the spectral measures of $`A_1(y),A_2(y),A_3(y)`$ commute. Their common domain is dense, their weighted form sum is closed, and the commutation and domain bounds are uniform in $`y`$. Equivalently, the three operators admit a joint spectral calculus on the common internal Hilbert space.

</div>

## Fiber Laplacians and gaps

Write $`A_n(y)`$ for the *nonnegative* vertical Laplace-type operator (or the vertical part of the spinor Laplacian in the spinor option). Each $`A_n(y)`$ has discrete spectrum with $`0`$ the harmonic eigenvalue. We assume a uniform gap
``` math
\begin{equation}
\label{eq:gap}
\ensuremath{\lambda^{\ast}}:= \inf_{y\in \ensuremath{Y^{4}}}\ \min_{1\le n\le 3}\ \lambda_1\!\big(A_n(y)\big) \;>\;0,
\end{equation}
```
and constant harmonic rank in $`y`$.

#### Explicit gaps in standard fibers.

For $`S^1_\ell`$ (length $`\ell`$), $`\lambda_1=(2\pi/\ell)^2`$. For a flat torus $`T^m`$ with side lengths $`L_j`$, $`\lambda_1=(2\pi)^2\min_j L_j^{-2}`$. For the round $`S^3`$ (radius $`1`$), $`\lambda_1=3`$ (see, e.g., ). Nilmanifold factors with bounded geometry admit a uniform positive lower bound on $`\lambda_1`$ once the metric class is fixed (bounded geometry prevents collapse).

## Fields, norms, and (optional) spinors

We work with complex scalar fields by default; all results extend to sections of a fixed Hermitian bundle with compatible connection.

#### Anisotropic norm.

Let
``` math
\ensuremath{H^{1}_{F}}:= \bigcap_{n=1}^3\mathrm{dom}(A_n^{1/2}),
\qquad
\|\Psi\|_{\ensuremath{H^{1}_{F}}}^{2}:=\|\Psi\|_{\ensuremath{L^{2}}}^{2}
+\sum_{n=1}^3\|A_n^{1/2}\Psi\|_{\ensuremath{L^{2}}}^{2},
```
with the natural common form domain. This is the joint vertical anisotropic norm for the possibly overlapping structures. Under strong commutation it is equivalent to the form norm of the weighted vertical sum when the weights $`\kappa_n`$ are bounded above and below away from zero.

## Joint harmonic projector

Let $`\Pi_n(y)`$ be the $`\ensuremath{L^{2}}`$–orthogonal projector onto $`\ker A_n(y)`$ and define the joint projector fiberwise by
``` math
\Pi_{\mathrm{coh}}(y) := \Pi_1(y)\,\Pi_2(y)\,\Pi_3(y).
```
We view $`\Pi_{\mathrm{coh}}`$ as the induced projector on $`\ensuremath{L^{2}}(\ensuremath{M_{10}})`$ acting fiberwise.

<div id="lem:comm-range" class="lemma">

**Lemma 3** (Commutation and range). *Under Assumption <a href="#ass:strong-comm" data-reference-type="ref" data-reference="ass:strong-comm">2</a>, the spectral projectors commute. Hence
``` math
\Pi_{\mathrm{coh}}(y)=\Pi_1(y)\Pi_2(y)\Pi_3(y),
\qquad
\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}(y)=\bigcap_{n=1}^{3}\ker A_n(y).
```*

</div>

<div id="lem:Pcoh-H1" class="lemma">

**Lemma 4** (Boundedness on $`H^1`$). *Under the gap condition <a href="#eq:gap" data-reference-type="eqref" data-reference="eq:gap">[eq:gap]</a> and bounded fiber geometry, the joint projector $`\Pi_{\mathrm{coh}}:H^{1}\to H^{1}`$ is bounded with
``` math
\|\Pi_{\mathrm{coh}}\|_{H^{1}\to H^{1}}\le C_{\Pi},
```
and $`\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$ is closed in $`H^{1}`$.*

</div>

<div class="remark">

*Remark 5* (Reference for Riesz projector bounds). Uniform control of fiberwise Riesz projectors on Sobolev scales follows from the Riesz–Dunford formula and parameter-dependent elliptic regularity; see .

</div>

# Flow, projection, and fixed points

## Parabolic generator and smoothing

Let $`\Delta_Y\ge0`$ be the Riemannian Laplacian of the base control geometry (or the Laplacian on a selected Riemannian Cauchy slice with declared boundary conditions). It is not the Lorentzian d’Alembertian. We study
``` math
\begin{equation}
\label{eq:flow}
\partial_t\Psi
= -\Bigl(\sum_{n=1}^{3}\kappa_n A_n + \varepsilon \Delta_{Y}\Bigr)\Psi
- N(\Psi),
\qquad
\kappa_n>0,\ \varepsilon\in[0,1].
\end{equation}
```
Denote the time–$`\tau`$ map by $`\Phi_\tau`$ and set
``` math
Q:= \mathrm{Id}-\Pi_{\mathrm{coh}},
\qquad
A:= \sum_{n=1}^{3}\kappa_n A_n + \varepsilon \Delta_Y .
```
Define rates
``` math
\lambda_n := \inf_{y\in\ensuremath{Y^{4}}}\lambda_1\!\big(A_n(y)\big)>0,
\qquad
\lambda_{A} := \min_{1\le n\le 3}\kappa_n \lambda_n.
```
Under strong commutation, $`\lambda_{A}`$ is a lower bound for the vertical form sum on $`\mathop{\mathrm{Ran}}Q`$.

<div id="ass:projector-comm" class="assumption">

**Assumption 6** (Projector commutation for the base-regularized model). The common domain is preserved by $`\Pi_{\mathrm{coh}}`$ and $`[A,\Pi_{\mathrm{coh}}]=0`$. If the vertical operators depend on $`y`$, this includes control of the commutator $`[\Delta_Y,\Pi_{\mathrm{coh}}]`$; it is not automatic from strong commutation of the $`A_n`$. Models with nonzero commutator require explicit leakage terms and are outside the exact invariant-sector theorem below.

</div>

By analytic semigroup theory (e.g. ) and Assumption <a href="#ass:projector-comm" data-reference-type="ref" data-reference="ass:projector-comm">6</a>, for $`t>0`$ one has
``` math
\begin{equation}
\label{eq:semigroup}
\|A^{1/2}e^{-tA}Q\|_{\ensuremath{L^{2}}\to\ensuremath{L^{2}}}
\le C\,(1+t^{-1/2})e^{-\lambda_{A}t},
\qquad
\|e^{-tA}\Pi_{\mathrm{coh}}\|_{\ensuremath{L^{2}}\to\ensuremath{L^{2}}}\le 1.
\end{equation}
```
For two solutions let $`w=\Psi_1-\Psi_2`$. Duhamel’s formula gives the sector-correct estimate
``` math
\begin{align}
\|Qw(t)\|_{\ensuremath{H^{1}_{F}}}
&\le C(1+t^{-1/2})e^{-\lambda_{A}t}
\|Qw(0)\|_{\ensuremath{L^{2}}}\nonumber\\
&\quad+C\int_0^t(1+(t-s)^{-1/2})e^{-\lambda_{A}(t-s)}
\|Q(N(\Psi_1(s))-N(\Psi_2(s)))\|_{\ensuremath{L^{2}}}\,\mathrm{d}s.
\label{eq:Q-duhamel}
\end{align}
```
No factor $`e^{-\lambda_{A}t}`$ is asserted for $`\Pi_{\mathrm{coh}}w`$. On the invariant coherent sector its dynamics are instead
``` math
\begin{equation}
\partial_t u=-\varepsilon\Delta_Yu-\Pi_{\mathrm{coh}}N(u),
\qquad u=\Pi_{\mathrm{coh}}u,
\label{eq:P-flow}
\end{equation}
```
and require base coercivity or coherent monotonicity for contraction.

<div class="remark">

*Remark 7* (Base lower-order terms). If the $`Q`$ equation includes first/zero-order terms with relative bound $`C_Y\ge0`$, replace the noncoherent decay margin by $`\lambda_{A}-C_Y`$. This modification remains a $`Q`$-sector statement.

</div>

## Coherence invariance and the projected map

<div id="ass:coh-inv" class="assumption">

**Assumption 8** (Coherence invariance). We assume Assumption <a href="#ass:projector-comm" data-reference-type="ref" data-reference="ass:projector-comm">6</a> and $`N(\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}})\subset \mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$.

</div>

We apply fixed-point principles to
``` math
T_\tau := \Pi_{\mathrm{coh}}\circ \Phi_\tau:\ D\to \mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}\cap \ensuremath{L^{2}},
```
where $`D\subset \mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}\cap \ensuremath{L^{2}}`$ is a closed bounded set (specified in §<a href="#subsec:exist" data-reference-type="ref" data-reference="subsec:exist">3.4</a>).

<div id="ass:lyapunov" class="assumption">

**Assumption 9** (Strict Lyapunov identity). There is a functional $`\mathcal E`$ bounded below on the invariant set such that every sufficiently regular trajectory satisfies
``` math
\mathcal E(\Phi_tu)+c\int_0^t\|\partial_s\Phi_su\|_{\ensuremath{L^{2}}}^2\,\mathrm{d}s
=\mathcal E(u),\qquad c>0.
```
For a gradient flow this follows from $`N=\nabla V`$ with the required domain and regularity. It is not implied by semilinearity alone.

</div>

<div id="prop:proj-eq" class="proposition">

**Proposition 10** (Projected step fixed point and equilibrium promotion). *Under Assumption <a href="#ass:coh-inv" data-reference-type="ref" data-reference="ass:coh-inv">8</a>, a point $`\Psi^\ast\in\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$ with $`T_\tau(\Psi^\ast)=\Psi^\ast`$ is a fixed point of the time–$`\tau`$ stabilization map. If Assumption <a href="#ass:lyapunov" data-reference-type="ref" data-reference="ass:lyapunov">9</a> also holds, then it is a genuine equilibrium: $`\Phi_t(\Psi^\ast)=\Psi^\ast`$ for all $`t\ge0`$.*

</div>

<div class="proof">

*Proof.* Coherence invariance gives $`T_\tau(\Psi^\ast)=\Phi_\tau(\Psi^\ast)=\Psi^\ast`$. The Lyapunov identity on $`[0,\tau]`$ then has equal endpoint energies, so its nonnegative dissipation integral vanishes. Hence $`\partial_t\Phi_t(\Psi^\ast)=0`$ and the orbit is stationary. Without the Lyapunov identity, a time–$`\tau`$ fixed point could be a nonstationary periodic point. ◻

</div>

## Uniqueness via the FCC (anisotropic norm)

<div id="thm:FCC" class="theorem">

**Theorem 11** (Fundamental contractivity on the coherent sector). *Let
``` math
L_{\mathrm{coh}}:= \mathrm{Lip}\bigl(\Pi_{\mathrm{coh}}N|_{\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}}\bigr).
```
Then for $`\Psi_1,\Psi_2\in\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$,
``` math
\|\Phi_\tau(\Psi_1)-\Phi_\tau(\Psi_2)\|_{\ensuremath{L^{2}}}
\le e^{L_{\mathrm{coh}}\tau}\|\Psi_1-\Psi_2\|_{\ensuremath{L^{2}}},
```
and since $`\|\cdot\|_{\ensuremath{H^{1}_{F}}}=\|\cdot\|_{\ensuremath{L^{2}}}`$ on $`\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$, the same holds in $`\ensuremath{H^{1}_{F}}`$. Moreover, $`T_\tau=\Pi_{\mathrm{coh}}\Phi_\tau`$ is a Banach contraction on the declared coherent phase space provided either:*

1.  ***Base diffusion:** $`\varepsilon>0`$ and the nonnegative $`\Delta_Y`$ has a PoincarÃ© gap $`\mu_Y>0`$ on a specified invariant subspace (for example mean-zero functions or Dirichlet boundary data), with $`\varepsilon\mu_Y>L_{\mathrm{coh}}`$; then
    ``` math
    \|T_\tau(\Psi_1)-T_\tau(\Psi_2)\|_{\ensuremath{L^{2}}}\le e^{-(\varepsilon\mu_Y-L_{\mathrm{coh}})\tau}\|\Psi_1-\Psi_2\|_{\ensuremath{L^{2}}}.
    ```*

2.  ***Strong monotonicity:** there exists $`\mu>0`$ such that $`\langle \Pi_{\mathrm{coh}}N(u)-\Pi_{\mathrm{coh}}N(v),u-v\rangle_{\ensuremath{L^{2}}}\ge \mu\|u-v\|_{\ensuremath{L^{2}}}^2`$ for all $`u,v\in\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$; then
    ``` math
    \|T_\tau(\Psi_1)-T_\tau(\Psi_2)\|_{\ensuremath{L^{2}}}\le e^{-\mu\tau}\|\Psi_1-\Psi_2\|_{\ensuremath{L^{2}}}.
    ```*

</div>

<div class="remark">

*Remark 12* (Base zero mode). On a compact boundaryless connected base, scalar constants lie in $`\ker\Delta_Y`$. Therefore base diffusion gives no coherent contraction on the full scalar space. One must remove/fix the mean, impose boundary conditions, or use coherent strong monotonicity.

</div>

<div class="remark">

*Remark 13* (Why fiber smoothing does not contract on $`\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$). On $`\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$ one has $`\nabla_F\Psi=0`$, hence $`\|\Psi\|_{\ensuremath{H^{1}_{F}}}=\|\Psi\|_{\ensuremath{L^{2}}}`$ and $`Q=0`$. Thus contraction must come from *base* dissipation (case (a)) or coherent monotonicity (case (b)), not from the fiber semigroup estimate <a href="#eq:semigroup" data-reference-type="eqref" data-reference="eq:semigroup">[eq:semigroup]</a>.

</div>

## Existence without contraction: Schauder and Darbo

<div id="ass:conf" class="assumption">

**Assumption 14** (Confinement for noncompact bases). If $`\ensuremath{Y^{4}}`$ is noncompact, assume the energy includes a confining base potential $`V(y)\to\infty`$ as $`r(y):=\mathop{\mathrm{dist}}_Y(y,y_0)\to\infty`$, yielding uniform tail control on energy sublevels (as in FP–I’s confinement hypothesis).

</div>

<div id="ass:base-smooth" class="assumption">

**Assumption 15** (Base smoothing for compactness). For the Schauder/Darbo existence routes we assume *base smoothing* is present, e.g. $`\varepsilon>0`$ in <a href="#eq:flow" data-reference-type="eqref" data-reference="eq:flow">[eq:flow]</a> (or one works with a base-regularized generator as in FP–I). This ensures $`\Phi_\tau`$ maps bounded sets in $`\ensuremath{L^{2}}`$ into sets bounded in $`H^1`$ on compact base regions, so Rellich compactness applies.

</div>

<div id="lem:affine" class="lemma">

**Lemma 16** (Coherent affine bound). *Assume one of the two contraction hypotheses in Theorem <a href="#thm:FCC" data-reference-type="ref" data-reference="thm:FCC">11</a>, with coherent contraction rate
``` math
\rho_{\mathrm{coh}}=
\begin{cases}
\varepsilon\mu_Y-L_{\mathrm{coh}},&\text{base-gap case},\\
\mu,&\text{strong-monotonicity case}.
\end{cases}
```
Set $`q_{\mathrm{coh}}(\tau)=e^{-\rho_{\mathrm{coh}}\tau}`$ and $`B_{\mathrm{coh}}(\tau)=\|T_\tau(0)\|_{\ensuremath{L^{2}}}`$. Then
``` math
\|T_\tau(\Psi)\|_{\ensuremath{L^{2}}}
\le q_{\mathrm{coh}}(\tau)\|\Psi\|_{\ensuremath{L^{2}}}+B_{\mathrm{coh}}(\tau)
```
for coherent $`\Psi`$. No $`Q`$-sector gap enters this estimate.*

</div>

<div id="cor:ball" class="corollary">

**Corollary 17** (Invariant/absorbing ball). *If $`q_{\mathrm{coh}}(\tau)<1`$ in Lemma <a href="#lem:affine" data-reference-type="ref" data-reference="lem:affine">16</a>, then
``` math
D_R := \{\Psi\in \mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}\cap \ensuremath{L^{2}}:\ \|\Psi\|_{\ensuremath{L^{2}}}\le R\},
\qquad
R\ge \frac{B_{\mathrm{coh}}(\tau)}{1-q_{\mathrm{coh}}(\tau)},
```
is forward invariant for $`T_\tau`$ and absorbing in the coherent $`\ensuremath{L^{2}}`$ metric.*

</div>

<div id="thm:schauder" class="theorem">

**Theorem 18** (Schauder: compact base). *Assume $`\ensuremath{Y^{4}}`$ is compact and Assumption <a href="#ass:base-smooth" data-reference-type="ref" data-reference="ass:base-smooth">15</a> holds. Then $`T_\tau=\Pi_{\mathrm{coh}}\Phi_\tau`$ maps bounded $`L^2`$ sets into sets relatively compact in $`L^2`$. If a nonempty $`D\subset\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}\cap\ensuremath{L^{2}}`$ is $`L^2`$-closed, bounded, convex, and satisfies $`T_\tau(D)\subset D`$, then $`T_\tau`$ has a fixed point in $`D`$.*

</div>

<div id="lem:condensing" class="lemma">

**Lemma 19** (Condensing via compact-local/small-tail decomposition). *Assume Assumptions <a href="#ass:base-smooth" data-reference-type="ref" data-reference="ass:base-smooth">15</a> and <a href="#ass:conf" data-reference-type="ref" data-reference="ass:conf">14</a>. Let $`D_M`$ be a forward-invariant energy sublevel that is bounded in $`H^1`$ and has the uniform tail control of Assumption <a href="#ass:conf" data-reference-type="ref" data-reference="ass:conf">14</a>. Let $`\alpha(\cdot)`$ be the Kuratowski measure of noncompactness in $`\ensuremath{L^{2}}`$. Then $`\Phi_\tau`$ is *Sadovskiı̆-condensing* on $`D_M`$: for every bounded $`E\subset D_M`$ with $`\alpha(E)>0`$,
``` math
\alpha(\Phi_\tau(E))<\alpha(E).
```*

</div>

<div class="proof">

*Proof sketch (same mechanism as FP–I, but adapted).* Fix a bounded set $`E`$ in a forward-invariant energy sublevel. Let $`\chi_R\in C_c^\infty(\ensuremath{Y^{4}})`$ be a cutoff equal to $`1`$ on $`\{r\le R\}`$ and supported on $`\{r\le 2R\}`$, and extend $`\chi_R`$ to $`\ensuremath{M_{10}}`$ by $`\chi_R\circ\pi`$. Define the output decomposition
``` math
K_R(\Psi_0):=(\chi_R\circ\pi)\,\Phi_\tau(\Psi_0),
\qquad
S_R(\Psi_0):=(1-\chi_R\circ\pi)\,\Phi_\tau(\Psi_0).
```
Confinement gives uniform small tails: $`\sup_{\Psi_0\in E}\|S_R(\Psi_0)\|_{\ensuremath{L^{2}}}\to 0`$ as $`R\to\infty`$. Base smoothing (Assumption <a href="#ass:base-smooth" data-reference-type="ref" data-reference="ass:base-smooth">15</a>) implies that for each fixed $`R`$, the set $`K_R(E)`$ is relatively compact in $`\ensuremath{L^{2}}`$ (Rellich on the compact base region $`\{r\le 2R\}`$ plus smoothing in $`H^1`$). Hence $`\alpha(K_R(E))=0`$, and by standard properties of $`\alpha`$,
``` math
\alpha(\Phi_\tau(E))=\alpha(K_R(E)+S_R(E))\le \alpha(K_R(E)) + 2\sup_{\Psi_0\in E}\|S_R(\Psi_0)\|_{\ensuremath{L^{2}}}
=2\sup_{\Psi_0\in E}\|S_R(\Psi_0)\|_{\ensuremath{L^{2}}}.
```
Choose $`R`$ so large that the right-hand side is $`<\alpha(E)`$, giving $`\alpha(\Phi_\tau(E))<\alpha(E)`$. ◻

</div>

<div id="thm:darbo" class="theorem">

**Theorem 20** (Darbo–Sadovskiı̆: noncompact base with confinement). *Assume $`\ensuremath{Y^{4}}`$ is noncompact and Assumptions <a href="#ass:conf" data-reference-type="ref" data-reference="ass:conf">14</a> and <a href="#ass:base-smooth" data-reference-type="ref" data-reference="ass:base-smooth">15</a> hold. Let $`D\subset \mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}\cap\ensuremath{L^{2}}`$ be nonempty, $`L^2`$-closed, bounded, convex, and invariant under $`T_\tau`$. Since $`\Pi_{\mathrm{coh}}`$ is an $`L^2`$-orthogonal projection of norm one, Lemma <a href="#lem:condensing" data-reference-type="ref" data-reference="lem:condensing">19</a> implies that $`T_\tau`$ is condensing on $`D`$. Hence $`T_\tau`$ has a fixed point in $`D`$.*

</div>

<div class="remark">

*Remark 21* (No full-map decay from the fiber gap). The margin $`\lambda_{A}-C_Y-L_{\mathrm{Lip}}`$ can sharpen estimates for the $`Q`$ component. It cannot imply $`\alpha(\Phi_\tau(E))\le\theta(\tau)\alpha(E)`$ with $`\theta(\tau)\to0`$ for the full map unless the coherent component has its own base or monotonicity contraction.

</div>

## Damping estimates and effective rates

Let $`\Psi=\Pi_{\mathrm{coh}}\Psi+Q\Psi`$ and write $`\Psi^\perp:=Q\Psi`$. Assuming coherence invariance and that $`N`$ is $`L_{\mathrm{Lip}}`$–Lipschitz on the invariant set considered, compare $`\Psi`$ with $`\Pi_{\mathrm{coh}}\Psi`$ to obtain
``` math
\frac{d}{dt}\|\Psi^\perp\|_{\ensuremath{L^{2}}}^{2}
\le -2\lambda_{A}\|\Psi^\perp\|_{\ensuremath{L^{2}}}^{2} + 2C_Y\|\Psi^\perp\|_{\ensuremath{L^{2}}}^{2} + 2L_{\mathrm{Lip}}\|\Psi^\perp\|_{\ensuremath{L^{2}}}^{2}.
```
Hence the effective decay rate satisfies
``` math
\begin{equation}
\label{eq:eta}
\eta \ge \lambda_{A}-C_Y-L_{\mathrm{Lip}}.
\end{equation}
```
This governs noncoherent $`\ensuremath{L^{2}}`$ decay only. Higher-norm control follows from the sector-correct Duhamel estimate <a href="#eq:Q-duhamel" data-reference-type="eqref" data-reference="eq:Q-duhamel">[eq:Q-duhamel]</a> under its regularity hypotheses. It does not imply coherent or full $`H^1`$ decay.

# Examples

## Product of circles and tori

Let $`\ensuremath{X^{6}}=T^2_1\times T^2_2\times T^2_3`$. Let $`A_n`$ contain the nonnegative Laplacian in the $`T_n^2`$ directions, and let a common $`U(1)`$ connection encode the selected central-circle holonomy without adding another product factor. For rectangular tori,
``` math
\lambda_n
=\min\Bigl\{(2\pi/\ell_{u_n})^2,\ (2\pi/\ell_{v_n})^2\Bigr\}
>0,
```
for the first nonconstant mode of that factor. These gaps control $`Q`$; the FCC margin still requires base coercivity or coherent monotonicity.

## Sphere case ($`S^3`$)

If one selected vertical operator has round-$`S^3`$ leaves of radius one, its first positive eigenvalue is $`3`$ (see ). This is an operator-level gap example, not a claim that three disjoint $`S^3`$ factors fit inside $`\ensuremath{X^{6}}`$ or that the coherent sector contracts.

## Nilmanifold auxiliary model

On a compact six-manifold carrying a nilmanifold foliation or on an auxiliary Lens–Nil model carrying a nilpotent vertical operator, a noncollapsing bounded-geometry family has a uniform positive first nonzero eigenvalue once its metric class is fixed. The actual embedding, shared-circle action, and commutation with the other two operators must be checked in the concrete model. This example does not identify $`L(3,1)\times\mathrm{Nil}_{3}`$ with the selected q79/Fu–Yau compactification.

## Toward Physical Interpretation (programmatic note)

While this paper is purely mathematical, the following schematic links guide later work:

- The three strongly commuting operators encode compatible, possibly overlapping modal structures on the same internal space.

- The coherent sector $`\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$ consists of fiberwise zero modes (only base dependence remains).

- Spectral gaps $`\lambda_n`$ set decay rates of nonzero fiber modes; in KK heuristics this corresponds to mass scales $`m_n\sim \lambda_n^{1/2}`$ for excitations.

- A projected step fixed point is an equilibrium only when the strict Lyapunov hypothesis of Proposition <a href="#prop:proj-eq" data-reference-type="ref" data-reference="prop:proj-eq">10</a> is verified.

# Concluding remarks

We established conditional existence and uniqueness results for projected stabilization-step fixed points on $`\ensuremath{M_{10}}=\ensuremath{Y^{4}}\times\ensuremath{X^{6}}`$ with three strongly commuting vertical operators. Equilibrium promotion requires a strict Lyapunov identity. The analysis is a Riemannian control model; physical interpretations and Lorentzian dynamics are deferred.

# Contraction on the coherent sector: details

Throughout, let $`T_\tau=\Pi_{\mathrm{coh}}\Phi_\tau`$ act on the declared coherent phase space and write $`L_{\mathrm{coh}}:=\mathrm{Lip}(\Pi_{\mathrm{coh}}N|_{\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}})`$. Coherence invariance means $`[A,\Pi_{\mathrm{coh}}]=0`$ and $`\Pi_{\mathrm{coh}}N(\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}})\subset\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$.

<div class="proof">

*Proof of Theorem <a href="#thm:FCC" data-reference-type="ref" data-reference="thm:FCC">11</a> (baseline).* If $`\Psi_i(0)\in\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$, then $`\Phi_t(\Psi_i)\in\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$ for all $`t\ge 0`$. Set $`u(t):=\Phi_t(\Psi_1)-\Phi_t(\Psi_2)\in\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$. Then $`\partial_t u = -\Pi_{\mathrm{coh}}\bigl(N(\Phi_t(\Psi_1))-N(\Phi_t(\Psi_2))\bigr)`$, hence $`\frac{d}{dt}\|u\|_{\ensuremath{L^{2}}}\le L_{\mathrm{coh}}\|u\|_{\ensuremath{L^{2}}}`$ and Grönwall yields the bound. ◻

</div>

<div class="proof">

*Proof of Theorem <a href="#thm:FCC" data-reference-type="ref" data-reference="thm:FCC">11</a>(a) (base diffusion).* Assume $`\varepsilon>0`$ and the nonnegative $`\Delta_Y`$ has a PoincarÃ© gap $`\mu_Y>0`$ on the declared mean-zero or boundary-conditioned coherent subspace. On that subspace the linear generator is $`-\varepsilon\Delta_Y`$, so for $`u(t)`$ as above,
``` math
\frac{d}{dt}\|u\|_{\ensuremath{L^{2}}}^2 \le -2(\varepsilon\mu_Y-L_{\mathrm{coh}})\|u\|_{\ensuremath{L^{2}}}^2,
```
and Grönwall gives the stated contraction. ◻

</div>

<div class="proof">

*Proof of Theorem <a href="#thm:FCC" data-reference-type="ref" data-reference="thm:FCC">11</a>(b) (strong monotonicity).* Assume $`\langle \Pi_{\mathrm{coh}}N(u)-\Pi_{\mathrm{coh}}N(v),u-v\rangle_{\ensuremath{L^{2}}}\ge \mu\|u-v\|_{\ensuremath{L^{2}}}^2`$ on $`\mathop{\mathrm{Ran}}\Pi_{\mathrm{coh}}`$. Then $`\frac{d}{dt}\|u\|_{\ensuremath{L^{2}}}^2\le -2\mu\|u\|_{\ensuremath{L^{2}}}^2`$ and Grönwall yields the contraction. ◻

</div>

# Spectral gap and damping inequality

Let $`\Psi=\Pi_{\mathrm{coh}}\Psi+Q\Psi`$ and $`\Psi^\perp:=Q\Psi`$. For solutions of <a href="#eq:flow" data-reference-type="eqref" data-reference="eq:flow">[eq:flow]</a>, using that $`A\ge \lambda_{A}I`$ on $`\mathop{\mathrm{Ran}}Q`$ and that $`N`$ is $`L_{\mathrm{Lip}}`$–Lipschitz on the invariant set, one obtains
``` math
\frac{d}{dt}\|\Psi^\perp(t)\|_{\ensuremath{L^{2}}}^2
\le -2(\lambda_{A}-C_Y-L_{\mathrm{Lip}})\|\Psi^\perp(t)\|_{\ensuremath{L^{2}}}^2,
```
which integrates to the exponential estimate consistent with <a href="#eq:eta" data-reference-type="eqref" data-reference="eq:eta">[eq:eta]</a>.

# Riesz projector bounds and base potentials

For each $`n`$, let $`A_n(y)\ge0`$ be the nonnegative vertical operator defined in Section 2 and fix a circle $`\Gamma`$ of radius $`\ensuremath{\lambda^{\ast}}/2`$ centered at $`0`$ inside the spectral gap (uniform in $`y`$). The fiberwise Riesz projector is
``` math
\Pi_n(y) = \frac{1}{2\pi i}\int_\Gamma (z-A_n(y))^{-1}\,dz.
```
Strong commutation gives the joint projector
``` math
\Pi_{\mathrm{coh}}(y)=\Pi_1(y)\Pi_2(y)\Pi_3(y),
\qquad
\|\Pi_{\mathrm{coh}}\|_{\ensuremath{L^{2}}\to\ensuremath{L^{2}}}\le 1.
```
Differentiating with respect to a base coordinate $`y^\alpha`$ gives
``` math
\partial_\alpha \Pi_n(y)
=\frac{1}{2\pi i}\int_\Gamma (z-A_n(y))^{-1}\,(\partial_\alpha A_n(y))\,(z-A_n(y))^{-1}\,dz,
```
hence
``` math
\|\partial_\alpha \Pi_n(y)\|_{\ensuremath{L^{2}}\to\ensuremath{L^{2}}}
\le \frac{C}{(\ensuremath{\lambda^{\ast}})^2}\|\partial_\alpha A_n(y)\|_{H^2\to \ensuremath{L^{2}}}.
```
Under bounded internal geometry and $`C^m`$ base dependence, $`\|\partial_\alpha A_n(y)\|_{H^2\to \ensuremath{L^{2}}}`$ is uniformly bounded, so $`\|\partial_\alpha \Pi_{\mathrm{coh}}(y)\|_{\ensuremath{L^{2}}\to\ensuremath{L^{2}}}\le C'_\Pi`$ and
``` math
\|\Pi_{\mathrm{coh}}\Psi\|_{H^1}\le (1+C'_\Pi)\|\Psi\|_{H^1}.
```
This is the standard mechanism behind Lemma <a href="#lem:Pcoh-H1" data-reference-type="ref" data-reference="lem:Pcoh-H1">4</a>; see .

#### Base potentials.

Adding a nonnegative confining potential $`V(y)`$ improves tail coercivity on $`\ensuremath{Y^{4}}`$ and underlies Darbo on noncompact bases, but does not change the fiber operators $`A_n(y)`$ and hence does not change $`\ensuremath{\lambda^{\ast}}`$ or $`\lambda_{A}`$.
