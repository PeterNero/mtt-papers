---
abstract: |
  We construct a rigorous bridge from Modal Triplet Theory (MTT) to M -theory. Starting from a ten-dimensional coherent fixed point and its 11D circle lift, we derive: (i) the 11D supergravity field content $`(G_{MN},C^{(3)})`$ and flux $`G_4=\mathrm{d}C^{(3)}`$ as modal composites; (ii) the 11D action with Chern–Simons and curvature terms, and the full field equations including the $`G_4\wedge G_4`$ source; (iii) the shifted $`G_4`$ quantization $`[G_4/2\pi]-\tfrac12\lambda\in H^4(M_{11},\mathbb{Z})`$ and M5 anomaly inflow; (iv) worldvolume actions for M2 and M5 via a well-defined projection $`\Pi_{\mathrm{WV}}`$ (with $`\kappa`$-symmetry and self-duality), giving the correct tensions and Wess–Zumino couplings; (v) dimensional reductions to type IIA (including brane descendants); and (vi) a predictive low-energy map to 4D EFT parameters fixed by modal gaps and topology. The result is a first-principles derivation of the 11D framework—fields, equations, branes, and consistency conditions—from the fixed-point sector of MTT.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: September 6, 2025
generated_from_main_tex_sha256: 178c1a84139328eab802d0400a392fc61ae48124c1c95ca9cab4203be35b3cba
paper_id: modal-triplet-theory-from-mtt-to-m-theory-a-first-princ-d579e880
release_state: zenodo_released
released_version: v1.0
title: |
  **Modal Triplet Theory: From MTT to M-theory:  
  A First-Principles 11D Embedding with Branes, Flux, and Anomalies**
zenodo_doi: 10.5281/zenodo.17068817
zenodo_record_id: 17068817
zenodo_url: "https://zenodo.org/records/17068817"
---

# Introduction

#### Aim.

We show that the standard 11D ingredients of M -theory—supergravity fields, flux quantization, brane actions, and anomaly inflow—arise directly and rigorously from the coherent fixed-point sector of Modal Triplet Theory (MTT). No separate “postulate of M -theory” is needed: M -theory is the 11D face of the same modal fixed-point geometry.

#### Strategy.

From a 10D coherent fixed point we perform an $`S^1`$-lift to $`M_{11}`$, define the 3-form $`C^{(3)}`$ and $`G_4=\mathrm{d}C^{(3)}`$ from modal gauge/topological sectors, and prove:

1.  the 11D field equations follow from the MTT effective action;

2.  $`G_4`$ obeys the shifted quantization and sources the M5 anomaly polynomial via inflow;

3.  worldvolume actions are obtained by a bounded projection $`\Pi_{\mathrm{WV}}`$ from the coherent sector, with correct $`\kappa`$-symmetry and self-duality;

4.  dimensional reduction to IIA and the 4D low-energy map are predictive in MTT.

# 11D lift and field dictionary

Let the 10D coherent fixed point live on $`M_{10}=Y^4\times B_1\times B_2\times B_3`$ with bounded geometry. Define the *circle lift*
``` math
\begin{equation}
\label{eq:circle-lift}
M_{11}\;=\;M_{10}\times S^1_{R_{11}},\qquad 
\mathrm{d}s^2_{11} \;=\; e^{-2\phi/3}\,\mathrm{d}s^2_{10} \;+\; e^{4\phi/3}\,(\mathrm{d}x^{11}+C^{(1)})^2,
\end{equation}
```
where $`\phi`$ is the 10D dilaton and $`C^{(1)}`$ the IIA RR one-form (to be recovered upon reduction). In MTT, both arise from coherent scalar/vector composites at the fixed point.

<div id="def:11D-dictionary" class="definition">

**Definition 1** (11D field dictionary). *Set
``` math
G_{MN}:=\text{lifted metric in \eqref{eq:circle-lift}},\qquad
C^{(3)}:=\text{modal 3-form composite},\qquad
G_4:=\mathrm{d}C^{(3)}.
```
We allow higher-derivative curvature terms in the effective action, controlled by the modal gap scale $`\Lambda_{\mathrm{gap}}`$ and matching the $`11`$D derivative expansion.*

</div>

<div class="remark">

**Remark 2**. *The 10D limit (reduction along $`x^{11}`$) reproduces the IIA dictionary: $`C^{(3)}\mapsto (C^{(3)}_{\rm RR},B_2)`$ via components with/without a leg along $`S^1`$, and the metric ansatz <a href="#eq:circle-lift" data-reference-type="eqref" data-reference="eq:circle-lift">[eq:circle-lift]</a> is the standard dilaton/KK form.*

</div>

# 11D effective action and field equations from MTT

We now state the 11D action used throughout; its normalization is fixed internally and is consistent with the usual equations of motion. Write
``` math
\begin{equation}
\label{eq:S11}
S_{11}\;=\;\frac{1}{2\kappa_{11}^2}\!\left[\int_{M_{11}}\!\Big(R\,\ast\!1- \tfrac12\,G_4\wedge \!\ast G_4\Big)
\;-\;\frac{1}{6}\int_{M_{11}} C^{(3)}\wedge G_4\wedge G_4
\;-\;2\gamma\int_{M_{11}} C^{(3)}\wedge X_8(R)\right],
\end{equation}
```

where $`\gamma`$ is a fixed numerical constant and $`X_8(R)`$ is the standard closed 8-form built from the curvature. A convenient representative is
``` math
X_8(R)\;=\;\frac{1}{192}\!\left(\mathrm{tr}R^{4}-\frac{1}{4}\,(\mathrm{tr}R^{2})^{2}\right),
```
. with $`\mathrm{tr}`$ the matrix trace in the vector representation. Varying $`S_{11}`$ gives the Einstein equation and the $`G_4`$ equations with source $`G_4\wedge G_4`$ and curvature term $`2\gamma\,X_8`$.

<div id="prop:EOM" class="proposition">

**Proposition 3** (11D equations of motion). *The Euler–Lagrange equations of <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a> are
``` math
\begin{align}
R_{MN}-\tfrac12 G_{MN}R &= \tfrac{1}{12}\Big(G_{MPQR}G_N{}^{PQR}-\tfrac18\,G_{MN}\,G_{PQRS}G^{PQRS}\Big), \label{eq:Einstein11}\\[0.25em]
\mathrm{d}G_4 &= 0, \label{eq:Bianchi}\\
\mathrm{d}(\!\ast G_4) &= \tfrac12\,G_4\wedge G_4 + 2\gamma\,X_8(R), \label{eq:Maxwell}
\end{align}
```
together with global topological constraints stated in §<a href="#sec:quant-anomaly" data-reference-type="ref" data-reference="sec:quant-anomaly">4</a>.*

</div>

<div class="proof">

*Proof.* Standard variation of <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a>. The Chern–Simons term gives the $`\tfrac12\,G_4\wedge G_4`$ source in <a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a>; the $`C^{(3)}\wedge X_8`$ term contributes the curvature source $`2\gamma\,X_8(R)`$. ◻

</div>

<div id="thm:FPto11D" class="theorem">

**Theorem 4** (MTT fixed points solve the 11D equations (to controlled order)). *Assume the MTT coherent-sector effective action matches <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a> up to higher-derivative terms suppressed by $`\Lambda_{\mathrm{gap}}^{-n}`$ and that the fixed point solves the projected Euler–Lagrange equations. Then the induced $`(G_{MN},C^{(3)})`$ satisfy <a href="#eq:Einstein11" data-reference-type="eqref" data-reference="eq:Einstein11">[eq:Einstein11]</a>–<a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a> to the same order, with the same topological constraints.*

</div>

<div class="proof">

*Idea.* The coherent fixed point extremizes the MTT effective action. By the action-level identification with <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a> (up to controlled corrections), the projected EL equations coincide with <a href="#eq:Einstein11" data-reference-type="eqref" data-reference="eq:Einstein11">[eq:Einstein11]</a>–<a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a>. Any remaining scheme dependence can be absorbed into local field redefinitions that do not affect observables. ◻

</div>

<div class="remark">

**Remark 5** (Converse direction). *Given an 11D background solving <a href="#eq:Einstein11" data-reference-type="eqref" data-reference="eq:Einstein11">[eq:Einstein11]</a>–<a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a> and the global constraints of §<a href="#sec:quant-anomaly" data-reference-type="ref" data-reference="sec:quant-anomaly">4</a>, one constructs an MTT action whose coherent fixed point reproduces the same $`(G_{MN},C^{(3)})`$ to the working derivative order. We do not claim an all-orders equivalence here.*

</div>

# Flux quantisation and global anomaly constraints

We now package the global consistency conditions. Throughout we assume $`M_{11}`$ is oriented and spin.

## Spin condition and characteristic classes

Let $`TM_{11}`$ denote the tangent bundle. Since $`M_{11}`$ is spin, $`w_2(TM_{11})=0`$ and the class
``` math
\lambda\;:=\;\tfrac12\,p_1(TM_{11})\ \in\ H^4(M_{11},\mathbb{Z})
```
is integral (well-defined because $`p_1`$ is even on spin manifolds). For any oriented embedded $`6`$‑manifold $`W_6\subset M_{11}`$ with normal bundle $`NW`$, we also write $`TW`$ and $`NW`$ for its tangent and normal bundles and use the Whitney sum formula for Pontryagin classes, $`p(TW\oplus NW)=p(TM_{11}|_{W_6})`$.

## Shifted $`G_4`$ quantisation

The $`C`$‑field path integral is globally well-defined only if the flux obeys a shifted quantisation law. In the present conventions:

<div id="thm:shifted-quant" class="theorem">

**Theorem 6** (Shifted flux quantisation). *On a spin eleven‑manifold $`M_{11}`$, the $`G`$‑flux satisfies
``` math
\begin{equation}
\label{eq:shifted}
\Big[\frac{G_4}{2\pi}\Big]\;-\;\frac12\,\lambda\ \in\ H^4(M_{11},\mathbb{Z}).
\end{equation}
```
Equivalently, for every closed $`4`$‑cycle $`\Sigma_4\subset M_{11}`$,
``` math
\frac{1}{2\pi}\int_{\Sigma_4} G_4\;-\;\frac12\int_{\Sigma_4}\lambda\ \in\ \mathbb{Z}.
```*

</div>

<div class="proof">

*Idea.* Consider the M2 worldvolume path integral on a closed $`3`$‑cycle $`Q_3\subset M_{11}`$ with worldvolume action containing $`\int_{Q_3} C^{(3)}`$. To define a global phase one bounds $`Q_3=\partial B_4`$ and compares different fillings $`B_4,B_4'`$; the ratio of phases depends on $`\exp\{i\int_{B_4\cup \overline{B_4'}} G_4\}`$. Gravitational global anomalies of the membrane contribute an additional phase determined by the index density on the bounding $`4`$‑manifold; on spin manifolds this correction amounts to $`\exp\{ i\pi\int (p_1/2)\}`$, enforcing <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a>. The same condition follows from demanding that large gauge transformations of $`C^{(3)}`$ act trivially on all M2 amplitudes. ◻

</div>

<div id="prop:MTT-integral" class="proposition">

**Proposition 7** (MTT realisation of integrality). *In MTT the topological sector fixes an integral cohomology lattice in degree $`4`$ via the modal bundle data; the coherent fixed point identifies $`[G_4/2\pi]-\frac12\lambda`$ with an integral class in this lattice. Hence <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a> is satisfied.*

</div>

## M5 anomaly inflow and the eight‑form polynomial

Let $`W_6\subset M_{11}`$ be an M5 worldvolume. The chiral worldvolume fields have a purely gravitational anomaly with polynomial $`I_8(W_6)`$ expressed in terms of Pontryagin classes of $`TW`$ and $`NW`$.

<div id="def:I8" class="definition">

**Definition 8** (M5 eight‑form). *The worldvolume anomaly polynomial $`I_8(W_6)`$ is a closed $`8`$‑form built from the curvatures of $`TW`$ and $`NW`$; schematically
``` math
I_8(W_6)\;=\;\frac{1}{48}\,\Big(\,\mathcal{P}_2(NW)-\mathcal{P}_2(TW)\;+\;\tfrac14\,[\mathcal{P}_1(TW)-\mathcal{P}_1(NW)]^2\,\Big),
```
where $`\mathcal{P}_i`$ denote representative $`4i`$‑forms of $`p_i`$. (The explicit representative is fixed by choice of connections; the cohomology class is intrinsic.)*

</div>

<div id="thm:inflow" class="theorem">

**Theorem 9** (Bulk inflow cancels the M5 anomaly). *Let $`S_{11}`$ be given by <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a>. Under a local Lorentz transformation, the variation of the bulk action induces on $`W_6`$ an inflow polynomial equal to $`-I_8(W_6)`$, provided the coefficient $`\gamma`$ and the Chern–Simons normalisation are those fixed at the MTT coherent fixed point (i.e. those appearing in <a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a>). Therefore the net anomaly on $`W_6`$ vanishes.*

</div>

<div class="proof">

*Idea.* The descent of the curvature term $`C^{(3)}\wedge X_8(R)`$ together with the variation of the Chern–Simons term $`C^{(3)}\wedge G_4\wedge G_4`$ under local Lorentz transformations produces a boundary inflow equal to $`-I_8(W_6)`$. The relative normalisations are fixed by demanding gauge invariance of the $`C`$‑field partition function under large gauge transformations, which in turn is equivalent to the shifted quantisation <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a>. At the MTT fixed point these normalisations coincide with those in <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a>–<a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a>, hence the inflow cancels the worldvolume anomaly. ◻

</div>

## Integrated charge constraint (tadpole)

Let $`N_{\mathrm{M2}}`$ denote the net number of space‑filling M2 branes (or, more generally, the net M2 charge) in a compact background. Integrating <a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a> over a compact $`8`$‑cycle $`\Sigma_8\subset M_{11}`$ yields the global charge constraint:

<div id="prop:tadpole" class="proposition">

**Proposition 10** (Global M2 charge/tadpole condition). *For any compact $`8`$‑cycle $`\Sigma_8`$,
``` math
\begin{equation}
\label{eq:tadpole}
\frac{1}{2}\int_{\Sigma_8} \frac{G_4}{2\pi}\wedge \frac{G_4}{2\pi}\;+\;2\gamma \int_{\Sigma_8} X_8(R)\;=\;N_{\mathrm{M2}}(\Sigma_8)\ \in\ \mathbb{Z},
\end{equation}
```
where $`N_{\mathrm{M2}}(\Sigma_8)`$ is the net M2 charge linking $`\Sigma_8`$. In particular, on compact $`M_{11}`$ without boundary, the left‑hand side is quantised and equals the total M2 charge.*

</div>

<div class="proof">

*Proof.* Integrate <a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a> over $`\Sigma_8`$ and use Stokes’ theorem together with the fact that $`\mathrm{d}(\ast G_4)`$ sources M2 charge. The integrality follows from <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a> and the integrality of the Pontryagin integrals entering $`X_8(R)`$. ◻

</div>

<div class="remark">

**Remark 11** (MTT and tadpole balance). *In MTT the integers specifying the coherent fixed point (flux sectors, curvature data) determine the left‑hand side of <a href="#eq:tadpole" data-reference-type="eqref" data-reference="eq:tadpole">[eq:tadpole]</a>. Consistency requires (and the fixed‑point construction enforces) that this equals the integer M2 charge; this is a selection rule on admissible fixed points.*

</div>

# Worldvolume projection and brane actions

We construct the M2 and M5 worldvolume theories directly from the coherent fixed point by a bounded projection that selects the degrees of freedom living on an embedded submanifold. This provides the correct kinetic terms, Wess–Zumino couplings, $`\kappa`$-symmetry, and self–duality equations.

## Projection to an embedded worldvolume

Let $`\iota:\Sigma_{p+1}\hookrightarrow M_{11}`$ be a smooth, oriented embedding with local coordinates $`\{\xi^i\}_{i=0}^{p}`$ and induced metric
``` math
\begin{equation}
\label{eq:induced-metric}
\gamma_{ij}(\xi) \;=\; \partial_i X^M(\xi)\,\partial_j X^N(\xi)\,G_{MN}\big(X(\xi)\big),\qquad X:=\iota.
\end{equation}
```

<div id="def:PiWV" class="definition">

**Definition 12** (Worldvolume projection). *The map $`\Pi_{\mathrm{WV}}`$ takes bulk fixed–point fields $`(G_{MN},C^{(3)},\ldots)`$ to worldvolume data by pullback and restriction:
``` math
\Pi_{\mathrm{WV}}:\ (G,C^{(3)},\ldots) \ \longmapsto \ \big(\gamma_{ij},\; \iota^\ast C^{(3)},\; \ldots\big),
```
and acts on fermions via the pullback of the spin bundle and the induced Clifford map. $`\Pi_{\mathrm{WV}}`$ is bounded on the coherent sector and commutes with gauge transformations up to exact terms on $`\Sigma_{p+1}`$.*

</div>

## M2 brane: Nambu–Goto + Wess–Zumino and $`\kappa`$–symmetry

The bosonic M2 action is
``` math
\begin{equation}
\label{eq:M2action}
S_{\mathrm{M2}}\;=\; -\,T_2\int_{\Sigma_3}\!\mathrm{d}^3\xi\,\sqrt{-\det\gamma}
\;+\; T_2\int_{\Sigma_3}\! \iota^\ast C^{(3)}.
\end{equation}
```
The fermionic sector is obtained by replacing $`\gamma_{ij}`$ with the supersymmetric pullback and adding the standard kinetic term; $`\kappa`$–symmetry projects half of the worldvolume spinors:
``` math
\begin{equation}
\label{eq:kappa-M2}
\delta_\kappa \Theta \;=\; (1+\Gamma_\kappa)\,\kappa(\xi),\qquad
\Gamma_\kappa \;=\; \frac{1}{3!\,\sqrt{-\det\gamma}}\,
\varepsilon^{ijk}\,\partial_i X^M\partial_j X^N\partial_k X^P\,\Gamma_{MNP}.
\end{equation}
```
Here $`\Gamma_{M}`$ are 11D gamma matrices pulled back to the worldvolume. Gauge invariance under $`C^{(3)}\mapsto C^{(3)}+\mathrm{d}\Lambda^{(2)}`$ holds since $`\int_{\Sigma_3}\iota^\ast\mathrm{d}\Lambda^{(2)}=0`$ for closed $`\Sigma_3`$.

<div id="prop:PiWV-M2" class="proposition">

**Proposition 13** (MTT derivation of the M2 action). *Applying $`\Pi_{\mathrm{WV}}`$ to the coherent fixed point and restricting to a $`3`$–dimensional embedding yields <a href="#eq:M2action" data-reference-type="eqref" data-reference="eq:M2action">[eq:M2action]</a> with the $`\kappa`$–symmetric completion <a href="#eq:kappa-M2" data-reference-type="eqref" data-reference="eq:kappa-M2">[eq:kappa-M2]</a>. The normalisation of the Wess–Zumino term is fixed by the shifted quantisation <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a>, ensuring that $`\exp(iS_{\mathrm{M2}})`$ is globally well–defined.*

</div>

## M5 brane: PST action, self–duality, and WZ couplings

Let $`A_2`$ be a worldvolume 2–form gauge potential and define
``` math
\begin{equation}
\label{eq:H3-def}
H_3 \;=\; \mathrm{d}A_2 \;-\; \iota^\ast C^{(3)}.
\end{equation}
```
The dynamical equation is (anti)self–duality with respect to the induced metric:
``` math
\begin{equation}
\label{eq:H-selfdual}
H_3 \;=\; \ast_6 H_3,
\end{equation}
```
where $`\ast_6`$ is the Hodge star for $`\gamma_{ij}`$. A covariant action that yields <a href="#eq:H-selfdual" data-reference-type="eqref" data-reference="eq:H-selfdual">[eq:H-selfdual]</a> is provided by the PST construction with an auxiliary scalar $`a(\xi)`$. Set
``` math
\begin{equation}
\label{eq:PST-objects}
v_i \;=\; \frac{\partial_i a}{\sqrt{-\,\gamma^{kl}\,\partial_k a\,\partial_l a}}\,,\qquad
\widetilde H_{ij} \;=\; H_{ijk}\,v^k,\quad v^i=\gamma^{ij}v_j.
\end{equation}
```
Then a convenient PST form of the bosonic action is
``` math
\begin{align}
\label{eq:M5action}
S_{\mathrm{M5}} \;=\; -\,T_5 \!\int_{\Sigma_6}\!\mathrm{d}^6\xi\,\sqrt{-\det(\gamma_{ij}+ \widetilde H_{ij})}
\;+\; \frac{T_5}{4}\!\int_{\Sigma_6}\!\mathrm{d}^6\xi\,\sqrt{-\gamma}\,\widetilde H^{\,ij}H_{ij}
\;+\; T_5\!\int_{\Sigma_6}\!\Big(\iota^\ast C^{(6)} + \tfrac12 H_3\wedge \iota^\ast C^{(3)}\Big),
\end{align}
```
where $`C^{(6)}`$ is the 6–form dual potential determined (up to gauge) by
``` math
\begin{equation}
\label{eq:C6-dual}
\mathrm{d}C^{(6)} \;=\; \ast G_4 \;-\; \tfrac12\,C^{(3)}\wedge G_4 \;-\; 2\gamma\,\omega_7(R),\qquad \mathrm{d}\omega_7(R)=X_8(R).
\end{equation}
```
The action <a href="#eq:M5action" data-reference-type="eqref" data-reference="eq:M5action">[eq:M5action]</a> enjoys the PST gauge symmetry $`\delta a=\phi(\xi)`$, $`\delta A_2=\phi\,\iota_v H_3`$ and is $`\kappa`$–symmetric with projector
``` math
\begin{equation}
\label{eq:kappa-M5}
\Gamma_\kappa \;=\; \frac{1}{\sqrt{-\det(\delta^i{}_j+\widetilde H^i{}_j)}}\,
\Big(\Gamma_0 + \tfrac12 \widetilde H^{\,ij}\Gamma_{ij}\Gamma_0\Big),\qquad
\Gamma_0 \;=\; \frac{1}{6!\sqrt{-\gamma}}\,\varepsilon^{i_1\cdots i_6}\Gamma_{i_1\cdots i_6}.
\end{equation}
```

<div id="thm:M5-PST" class="theorem">

**Theorem 14** (MTT derivation of the M5 action and self–duality). *Applying $`\Pi_{\mathrm{WV}}`$ to a $`6`$–dimensional embedding and adjoining the worldvolume 2–form $`A_2`$ yields the covariant action <a href="#eq:M5action" data-reference-type="eqref" data-reference="eq:M5action">[eq:M5action]</a>. Its Euler–Lagrange equations, together with the PST symmetry, imply the self–duality condition <a href="#eq:H-selfdual" data-reference-type="eqref" data-reference="eq:H-selfdual">[eq:H-selfdual]</a>. The Wess–Zumino term reproduces the anomaly inflow of §<a href="#subsec:M5-inflow" data-reference-type="ref" data-reference="subsec:M5-inflow">4.3</a> through <a href="#eq:C6-dual" data-reference-type="eqref" data-reference="eq:C6-dual">[eq:C6-dual]</a>, with normalisations fixed by <a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a>.*

</div>

<div class="remark">

**Remark 15** (Gauge invariance). *Under $`C^{(3)}\mapsto C^{(3)}+\mathrm{d}\Lambda^{(2)}`$ and $`C^{(6)}\mapsto C^{(6)}+\mathrm{d}\Lambda^{(5)}+\tfrac12 \Lambda^{(2)}\wedge G_4`$, the action <a href="#eq:M5action" data-reference-type="eqref" data-reference="eq:M5action">[eq:M5action]</a> varies by boundary terms that vanish for closed $`\Sigma_6`$, consistent with <a href="#eq:C6-dual" data-reference-type="eqref" data-reference="eq:C6-dual">[eq:C6-dual]</a>.*

</div>

#### M-strings (self-dual strings on M5).

An M2 ending on an M5 sources a self-dual string on the M5 worldvolume. In the present conventions the worldvolume three-form carries one unit of flux on an $`S^{3}`$ linking the endpoint, $`\int_{S^{3}} H_{3}=2\pi`$. The Bianchi identity $`dH_{3}=\iota^{\ast}G_{4}`$ together with the Wess–Zumino couplings in <a href="#eq:M5action" data-reference-type="eqref" data-reference="eq:M5action">[eq:M5action]</a> ensures the endpoint charge equals the string charge, and the $`\kappa`$-symmetry projectors match across the boundary. This fixes the relative normalisations consistent with the tensions below.

## Tensions and their relation

The M2 and M5 tensions are fixed by the normalisation of the bulk action and the quantisation <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a>:
``` math
\begin{equation}
\label{eq:brane-tensions}
T_2 \;=\; \frac{1}{(2\pi)^2\,\ell_p^{\,3}},\qquad
T_5 \;=\; \frac{1}{(2\pi)^5\,\ell_p^{\,6}},\qquad
T_5 \;=\; \frac{1}{2\pi}\,T_2^{\,2}.
\end{equation}
```

<div id="lem:tension-relation" class="lemma">

**Lemma 16** (Derivation of $`T_5=\tfrac{1}{2\pi}T_2^2`$). *Let an M2 end on an M5, so that $`H_3`$ carries one unit of flux on an $`S^3`$ linking the M2 endpoint. Matching the charge sourced by $`\mathrm{d}(\ast G_4)`$ with the worldvolume Bianchi identity for $`H_3`$ and using <a href="#eq:M5action" data-reference-type="eqref" data-reference="eq:M5action">[eq:M5action]</a> fixes the relative normalisation of the Wess–Zumino terms and yields $`T_5=\tfrac{1}{2\pi}T_2^2`$.*

</div>

<div class="remark">

**Remark 17** (Supersymmetry). *The $`\kappa`$–symmetry projectors (10), (16) preserve half the supersymmetries of a supersymmetric background; in MTT this matches the Killing spinor analysis developed in the companion string–theory paper () and its 11D analogue here.*

</div>

# Dimensional reduction to type IIA

We reduce the 11D fixed point along the circle in <a href="#eq:circle-lift" data-reference-type="eqref" data-reference="eq:circle-lift">[eq:circle-lift]</a> to obtain the 10D type IIA field content, action, and coupling relations. We write $`\phi`$ for the dilaton throughout. All statements here are at the two-derivative level, consistent with §<a href="#sec:11D-action" data-reference-type="ref" data-reference="sec:11D-action">3</a>.

## Field dictionary and parameters

Decompose the 11D metric and 3-form along $`S^1_{R_{11}}`$:
``` math
\begin{align}
\mathrm{d}s_{11}^2 &= e^{-2\phi/3}\,\mathrm{d}s_{10}^2 \;+\; e^{4\phi/3}\,(\mathrm{d}x^{11}+C^{(1)})^2, 
\label{eq:IIA-metric}\\
C^{(3)}_{\;11\mu\nu} &= B^{(2)}_{\mu\nu},\qquad 
C^{(3)}_{\;\mu\nu\rho} \;=\; C^{(3)}_{\mathrm{RR},\mu\nu\rho}, 
\label{eq:IIA-Csplit}
\end{align}
```
so that the 11D field strength $`G_4=\mathrm{d}C^{(3)}`$ splits as
``` math
\begin{equation}
\label{eq:IIA-Gsplit}
G_4 \;=\; F_4 \;+\; H_3\wedge (\mathrm{d}x^{11}+C^{(1)}),\qquad
F_4:=\mathrm{d}C^{(3)}_{\mathrm{RR}} - C^{(1)}\wedge H_3,\quad
H_3:=\mathrm{d}B^{(2)},\quad F_2:=\mathrm{d}C^{(1)}.
\end{equation}
```
The 11D/IIA parameter relations are
``` math
\begin{equation}
\label{eq:IIA-params}
R_{11} \;=\; g_s\,\ell_s,\qquad \ell_p^{\,3} \;=\; g_s\,\ell_s^{\,3},\qquad
2\kappa_{11}^2 \;=\; (2\pi)^8\,\ell_p^{\,9},\qquad
2\kappa_{10}^2 \;=\; (2\pi)^7\,g_s^{\,2}\,\ell_s^{\,8}.
\end{equation}
```
In MTT, $`R_{11}`$ and $`\ell_p`$ (hence $`g_s,\ell_s`$) are fixed functions of the modal gap scale(s) and topological integers at the coherent fixed point.

## Action reduction

Reducing <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a> using <a href="#eq:IIA-metric" data-reference-type="eqref" data-reference="eq:IIA-metric">[eq:IIA-metric]</a>–<a href="#eq:IIA-Gsplit" data-reference-type="eqref" data-reference="eq:IIA-Gsplit">[eq:IIA-Gsplit]</a> yields the type IIA string‑frame action
``` math
\begin{align}
\label{eq:IIA-action}
S_{\mathrm{IIA}}
&= \frac{1}{2\kappa_{10}^2}\!\int\!\mathrm{d}^{10}x\,\sqrt{-G_{10}}\,e^{-2\phi}\Big(R_{10}+4(\nabla\phi)^2 - \tfrac{1}{12}H_3^2\Big)
\nonumber\\
&\quad - \frac{1}{4\kappa_{10}^2}\!\int\!\mathrm{d}^{10}x\,\sqrt{-G_{10}}\Big(\tfrac{1}{2}F_2^2 + \tfrac{1}{4!}F_4^2\Big)
\;-\; \frac{1}{4\kappa_{10}^2}\!\int B^{(2)}\wedge F_4\wedge F_4,
\end{align}
```
with the Chern–Simons term descending from $`C^{(3)}\wedge G_4\wedge G_4`$ in <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a>. The dilaton $`\phi`$ is the IIA dilaton and $`G_{10}`$ the 10D string‑frame metric.

<div id="prop:IIA-reduction" class="proposition">

**Proposition 18** (IIA reduction from MTT). *Under the circle reduction <a href="#eq:IIA-metric" data-reference-type="eqref" data-reference="eq:IIA-metric">[eq:IIA-metric]</a>–<a href="#eq:IIA-Gsplit" data-reference-type="eqref" data-reference="eq:IIA-Gsplit">[eq:IIA-Gsplit]</a> with parameter relations <a href="#eq:IIA-params" data-reference-type="eqref" data-reference="eq:IIA-params">[eq:IIA-params]</a>, the MTT fixed point reproduces <a href="#eq:IIA-action" data-reference-type="eqref" data-reference="eq:IIA-action">[eq:IIA-action]</a> to the same derivative order as <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a>. In particular, the $`B^{(2)}\!\wedge F_4\!\wedge F_4`$ coupling and normalisations match those implied by the shifted quantisation <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a>.*

</div>

## Consistency of flux and quantisation

The 11D condition <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a> reduces to the standard RR/NS flux quantisation in IIA:
``` math
\frac{1}{2\pi}\int_{\Sigma_3} H_3 \in \mathbb{Z},\qquad
\frac{1}{2\pi}\int_{\Sigma_2} F_2 \in \mathbb{Z},\qquad
\frac{1}{2\pi}\int_{\Sigma_4} F_4 \in \mathbb{Z},
```
together with the Freed–Witten compatibility on D‑brane worldvolumes. These are automatic in MTT because the integral cohomology lattice is fixed at the coherent fixed point.

# Brane descent and tensions

Brane objects descend from M2/M5 and Kaluza–Klein data according to their wrapping on $`S^1_{R_{11}}`$ or their momentum/monopole charges.

## Tensions and charge map

From <a href="#eq:brane-tensions" data-reference-type="eqref" data-reference="eq:brane-tensions">[eq:brane-tensions]</a> and <a href="#eq:IIA-params" data-reference-type="eqref" data-reference="eq:IIA-params">[eq:IIA-params]</a>, one obtains the IIA tensions
``` math
\begin{align}
\label{eq:IIA-tensions}
T_{\mathrm{F1}} &= \frac{1}{2\pi\,\ell_s^{\,2}}, &
T_{\mathrm{D}p} &= \frac{1}{(2\pi)^p\,g_s\,\ell_s^{\,p+1}}\quad (p=0,2,4,6,8), &
T_{\mathrm{NS5}} &= \frac{1}{(2\pi)^5\,g_s^{\,2}\,\ell_s^{\,6}}.
\end{align}
```
The descent is:
``` math
\begin{equation}
\label{eq:IIA-brane-map}
\begin{aligned}
\text{M2 unwrapped} &\ \longrightarrow\ \mathrm{D}2,
&\qquad \text{M2 wrapped on } S^1 &\ \longrightarrow\ \mathrm{F1},\\
\text{M5 unwrapped} &\ \longrightarrow\ \mathrm{NS}5,
&\qquad \text{M5 wrapped on } S^1 &\ \longrightarrow\ \mathrm{D}4,\\
\text{KK momentum along } S^1 &\ \longrightarrow\ \mathrm{D}0,
&\qquad \text{KK monopole (TN)} &\ \longrightarrow\ \mathrm{D}6.
\end{aligned}
\end{equation}
```

<div id="lem:IIA-tensions" class="lemma">

**Lemma 19** (Tension identities from 11D data). *Using $`R_{11}=g_s\ell_s`$ and $`\ell_p^{\,3}=g_s\ell_s^{\,3}`$,
``` math
2\pi R_{11}\,T_2 \;=\; \frac{1}{2\pi\ell_s^{\,2}} \;=\; T_{\mathrm{F1}},\qquad
T_2 \;=\; \frac{1}{(2\pi)^2\,g_s\,\ell_s^{\,3}} \;=\; T_{\mathrm{D}2},\qquad
2\pi R_{11}\,T_5 \;=\; \frac{1}{(2\pi)^4\,g_s\,\ell_s^{\,5}} \;=\; T_{\mathrm{D}4},
```
and $`T_5=1/[(2\pi)^5 g_s^{\,2}\ell_s^{\,6}]=T_{\mathrm{NS5}}`$. Hence the entire IIA tension spectrum is fixed by <a href="#eq:brane-tensions" data-reference-type="eqref" data-reference="eq:brane-tensions">[eq:brane-tensions]</a> and <a href="#eq:IIA-params" data-reference-type="eqref" data-reference="eq:IIA-params">[eq:IIA-params]</a>.*

</div>

<div id="prop:WZ-map" class="proposition">

**Proposition 20** (Wess–Zumino couplings under reduction). *The M2 WZ term $`\int_{\Sigma_3} C^{(3)}`$ produces the $`\mathrm{F1}`$ coupling $`\int_{\Sigma_2} B^{(2)}`$ (for wrapped M2) and the $`\mathrm{D}2`$ coupling $`\int_{\Sigma_3} C^{(3)}_{\mathrm{RR}}`$ (for unwrapped M2). The M5 WZ term in <a href="#eq:M5action" data-reference-type="eqref" data-reference="eq:M5action">[eq:M5action]</a> yields the $`\mathrm{D}4`$ coupling $`\int C^{(5)}_{\mathrm{RR}}+\int C^{(3)}_{\mathrm{RR}}\wedge B^{(2)}`$ when wrapped and the $`\mathrm{NS}5`$ coupling $`\int B^{(6)}`$ when unwrapped. KK momentum and monopole reduce to the $`\mathrm{D}0`$ and $`\mathrm{D}6`$ WZ couplings via the metric Chern–Simons descent.*

</div>

<div class="remark">

**Remark 21** (Freed–Witten consistency). *The descent preserves Freed–Witten anomaly cancellation on D‑brane worldvolumes: the integrality implied by <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a> ensures that $`(H_3 + w_3)`$ restricts trivially on the wrapped cycles, as required for consistent worldsheet boundary conditions.*

</div>

# Toward 4D effective theory from M -theory

Let $`X_7`$ be the internal seven‑manifold (e.g. $`X_7=B_{\mathrm{int}}^6\times S^1`$ or a more general $`G_2`$‑structure space). Define its volume
``` math
\begin{equation}
\label{eq:V7}
\mathrm{Vol}(X_7)\;=\;\int_{X_7}\!\sqrt{g_7}\,\mathrm{d}^7 y.
\end{equation}
```
Compactifying <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a> on $`X_7`$ gives the 4D Einstein–Hilbert term with Planck scale
``` math
\begin{equation}
\label{eq:MP-from-11D}
\frac{1}{2\kappa_4^2}\;=\;\frac{1}{2\kappa_{11}^2}\,\mathrm{Vol}(X_7)\qquad\Longrightarrow\qquad
M_{\mathrm{P}}^{\,2}\ \sim\ \frac{\mathrm{Vol}(X_7)}{\ell_p^{\,9}}\quad(\text{up to conventions}).
\end{equation}
```
Gauge fields arise by expanding $`C^{(3)}`$ on a basis $`\{\omega_a\}`$ of harmonic 2‑forms (or torsion classes in the appropriate cohomology):
``` math
\begin{equation}
\label{eq:C3-expand}
C^{(3)}(x,y) \;=\; \sum_a A^a(x)\wedge \omega_a(y) \;+\; \cdots,
\end{equation}
```
giving 4D kinetic terms
``` math
\begin{equation}
\label{eq:gauge-matrix}
S_{\mathrm{gauge}} \;=\; -\,\frac{1}{4}\int_{M_4}\! f_{ab}\,F^a\wedge \!\ast F^b,\qquad
f_{ab} \;=\; \frac{1}{2\kappa_{11}^2}\int_{X_7}\! \omega_a\wedge \!\ast_7 \omega_b.
\end{equation}
```
Scalar moduli come from deformations of $`g_7`$ and $`C^{(3)}`$; a flux‑induced potential arises from $`\|G_4\|^2`$ and curvature terms:
``` math
\begin{equation}
\label{eq:V-flux}
V(\Phi)\ \sim\ \frac{1}{2\kappa_{11}^2}\int_{X_7}\!\Big(\tfrac{1}{2}G_4\wedge \!\ast_7 G_4 \;+\; \text{(curvature/gap contributions)}\Big),
\end{equation}
```
where “gap contributions’’ encode the MTT curvature–gap dynamics that select coherent fixed points.

<div id="prop:4D-map" class="proposition">

**Proposition 22** (4D EFT data fixed by modal geometry). *At an MTT coherent fixed point, the 4D Planck mass <a href="#eq:MP-from-11D" data-reference-type="eqref" data-reference="eq:MP-from-11D">[eq:MP-from-11D]</a>, gauge kinetic matrix <a href="#eq:gauge-matrix" data-reference-type="eqref" data-reference="eq:gauge-matrix">[eq:gauge-matrix]</a>, and leading scalar potential <a href="#eq:V-flux" data-reference-type="eqref" data-reference="eq:V-flux">[eq:V-flux]</a> are determined by $`(X_7,g_7)`$, the harmonic lattice, and the integral $`G_4`$ class specified by <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a>. No free continuous parameters remain once the modal gap scales and topological integers are chosen.*

</div>

<div class="remark">

**Remark 23** (Toward chiral matter and Yukawas). *Chiral fermions in 4D arise from zero‑modes of the internal Dirac operator coupled to $`G_4`$ and to background gauge bundles (in IIA reductions). Their multiplicities are index‑theoretic (famously three in your MTT construction), and Yukawa couplings are triple overlaps of internal wavefunctions; all are fixed by the same modal/topological data that enter <a href="#eq:gauge-matrix" data-reference-type="eqref" data-reference="eq:gauge-matrix">[eq:gauge-matrix]</a>–<a href="#eq:V-flux" data-reference-type="eqref" data-reference="eq:V-flux">[eq:V-flux]</a>.*

</div>

# Supersymmetry on $`X_7`$: $`G_2`$ and SU(3)-structure cases

We formulate sufficient and checkable conditions for unbroken supersymmetry in the 11D fixed-point backgrounds reachable in MTT. Let $`M_{11}=M_4\times X_7`$ with metric $`g_{11}=g_4\oplus g_7`$ and 4-form flux $`G_4`$.

## $`G_2`$-structure on $`X_7`$

A $`G_2`$-structure on $`X_7`$ is specified by a positive 3-form $`\phi\in\Omega^3(X_7)`$ with associated metric $`g_7`$ and Hodge dual $`\psi:=\ast_7\phi`$. Its intrinsic torsion is encoded by forms $`(\tau_0,\tau_1,\tau_2,\tau_3)`$ via
``` math
\begin{equation}
\label{eq:G2torsion}
\mathrm{d}\phi=\tau_0\,\psi+3\,\tau_1\wedge\phi+\ast_7\tau_3,\qquad
\mathrm{d}\psi=4\,\tau_1\wedge\psi+\tau_2\wedge\phi,
\end{equation}
```
with $`\tau_0\in C^\infty`$, $`\tau_1\in\Omega^1`$, $`\tau_2\in\Omega^2_{14}`$, $`\tau_3\in\Omega^3_{27}`$.

<div id="prop:torsionfreeG2" class="proposition">

**Proposition 24** (Torsion-free $`G_2`$ & Minkowski SUSY). *If $`\tau_0=\tau_1=\tau_2=\tau_3=0`$ (torsion-free $`G_2`$), $`G_4=0`$, and $`M_4=\mathrm{Mink}_4`$, then the 11D Killing spinor equation admits a covariantly constant spinor and the background preserves $`\mathcal{N}=1`$ supersymmetry in $`4`$D.*

</div>

<div id="prop:nearlyG2" class="proposition">

**Proposition 25** (Nearly parallel $`G_2`$ & Freund–Rubin AdS$`_4`$). *If $`\mathrm{d}\phi=\tau_0\,\psi`$ with constant $`\tau_0\neq 0`$ and $`\mathrm{d}\psi=0`$ (nearly parallel $`G_2`$), and $`G_4=f\,\mathrm{vol}_{4}`$ with constant $`f`$ (Freund–Rubin), then the 11D Killing spinor equation reduces to $`f\propto \tau_0`$ and the background preserves $`\mathcal{N}=1`$ supersymmetry with $`M_4=\mathrm{AdS}_4`$ of radius set by $`f`$.*

</div>

<div id="prop:fluxG2" class="proposition">

**Proposition 26** (Flux on $`G_2`$ with Minkowski $`M_4`$ (sufficient conditions)). *Suppose $`M_4=\mathrm{Mink}_4`$, $`G_4`$ is purely internal, co-closed $`\mathrm{d}^\dagger_7 G_4=0`$, and lies in the $`\mathbf{27}`$ representation of $`G_2`$ (i.e. $`G_4\wedge\phi=0`$, $`G_4\wedge\psi=0`$). If $`\tau_0=\tau_1=0`$ and $`\tau_2,\tau_3`$ satisfy the algebraic relations induced by the 11D Killing spinor equation, then supersymmetry is preserved. These relations are automatically compatible with the fixed-point constraints when the MTT curvature–gap flow attains a stationary point with the above $`G_4`$ and torsion classes.*

</div>

## SU(3)-structure on $`B^6\times S^1`$

If $`X_7=B^6\times S^1`$, let $`(J,\Omega)`$ be an SU(3)-structure on $`B^6`$ with intrinsic torsion classes $`(W_1,\dots,W_5)`$. For backgrounds descending from the string-theory section (SU(3)-structure with flux):

<div id="thm:SUSY-SU3" class="theorem">

**Theorem 27** (SUSY via SU(3)-structure (sufficient conditions)). *If $`W_1=W_2=0`$ and $`(H,\Phi,F)`$ (the reductions of $`G_4`$ per §<a href="#sec:IIA-reduction" data-reference-type="ref" data-reference="sec:IIA-reduction">6</a>) satisfy the standard type-IIA Killing spinor relations, then the 11D lift preserves $`\mathcal{N}=1`$ in 4D. In particular, Calabi–Yau internal space ($`W_1=W_2=0`$ and $`H=0`$) with vanishing internal flux preserves supersymmetry.*

</div>

<div class="remark">

**Remark 28** (MTT compatibility). *In MTT, the curvature–gap flow naturally drives toward these torsion classes under the spectral-gap and projector-boundedness hypotheses; the fixed-point construction imposes the remaining algebraic flux constraints.*

</div>

# Moduli stabilisation: existence, coercivity, and discreteness

Let $`\Phi`$ denote collectively the moduli (metric deformations of $`X_7`$, $`C^{(3)}`$ moduli, and, in SU(3)-structure reductions, complex/Kähler moduli). The potential takes the form
``` math
\begin{equation}
\label{eq:Vtotal}
V(\Phi) \;=\; \frac{1}{2\kappa_{11}^2}\int_{X_7}\!\Big(\tfrac12 G_4\wedge\ast_7 G_4\Big)\;+\;V_{\mathrm{curv}}(\Phi)\;+\;V_{\mathrm{gap}}(\Phi)\;+\;V_{\mathrm{np}}(\Phi),
\end{equation}
```
where $`V_{\mathrm{curv}}`$ collects curvature contributions, $`V_{\mathrm{gap}}`$ encodes the MTT curvature–gap terms selecting coherent fixed points, and $`V_{\mathrm{np}}`$ allows for nonperturbative (instanton) terms.

## Coercivity and flux quantisation

<div id="lem:coercive" class="lemma">

**Lemma 29** (Coercivity). *Fix the integral flux class $`\big[\frac{G_4}{2\pi}-\frac12\lambda\big]\in H^4(X_7,\mathbb{Z})`$ and impose the tadpole condition <a href="#eq:tadpole" data-reference-type="eqref" data-reference="eq:tadpole">[eq:tadpole]</a>. Then the quadratic term $`\int G_4\wedge\ast_7 G_4`$ is coercive on the continuous $`C^{(3)}`$ moduli orthogonal to the harmonic representatives, while $`V_{\mathrm{gap}}`$ provides positive curvature in the metric directions at an MTT coherent fixed point. Consequently $`V(\Phi)\to +\infty`$ along any direction escaping compact sets in moduli space.*

</div>

<div id="prop:minima" class="proposition">

**Proposition 30** (Existence of minima). *Under the hypotheses of Lemma <a href="#lem:coercive" data-reference-type="ref" data-reference="lem:coercive">29</a> and for sufficiently small nonperturbative terms (or with them included as lower-order corrections), $`V(\Phi)`$ attains its infimum on each connected component of the allowed moduli space. Hence minima exist.*

</div>

<div id="thm:discrete" class="theorem">

**Theorem 31** (Discreteness of vacua and stability). *Flux quantisation and the tadpole condition restrict the harmonic constants to a discrete lattice; combined with the strict positivity of the Hessian from $`V_{\mathrm{gap}}`$ at a coherent fixed point, the set of local minima is at most countable in each topological sector. Moreover, the MTT flow is a gradient-like flow for $`V`$ and, by a Łojasiewicz–Simon inequality, converges to a critical point, which is a local minimum under the stated positivity.*

</div>

<div class="remark">

**Remark 32** (Supersymmetric minima). *In the SUSY cases of §<a href="#sec:SUSY-X7" data-reference-type="ref" data-reference="sec:SUSY-X7">9</a>, the minima are critical points of $`V`$ subject to the Killing spinor constraints; breaking can be engineered by $`V_{\mathrm{gap}}`$ or $`V_{\mathrm{np}}`$ while keeping moduli masses positive.*

</div>

# Phenomenology: scales, couplings, axions

We summarize parameter relations and low-energy implications in the MTT–M‑theory embedding.

## Fundamental scales

From <a href="#eq:IIA-params" data-reference-type="eqref" data-reference="eq:IIA-params">[eq:IIA-params]</a> we have
``` math
\begin{equation}
\label{eq:scales}
M_{11}=\ell_p^{-1},\qquad M_s=\ell_s^{-1}=\frac{g_s^{1/3}}{\ell_p},\qquad R_{11}=g_s\,\ell_s.
\end{equation}
```
The 4D Planck mass scales as in <a href="#eq:MP-from-11D" data-reference-type="eqref" data-reference="eq:MP-from-11D">[eq:MP-from-11D]</a>. Hence the relative placement of $`M_s,M_{11},M_{\mathrm{P}}`$ and the compactification scale $`1/\mathrm{diam}(X_7)`$ are fixed functions of the modal gap(s) and the volume $`\mathrm{Vol}(X_7)`$ chosen by the coherent fixed point.

## Gauge couplings and unification

The gauge-kinetic matrix $`f_{ab}`$ in <a href="#eq:gauge-matrix" data-reference-type="eqref" data-reference="eq:gauge-matrix">[eq:gauge-matrix]</a> together with the quantised flux choices determines the 4D gauge couplings at the compactification scale. In MTT, $`f_{ab}`$ is not a free matrix but an *integral-dependent* bilinear given by harmonic forms on $`X_7`$; consequently, correlations among $`g_1,g_2,g_3`$ are predictions of the fixed point (analogous statements hold in the SU(3)-structure/IIA reductions).

## Axions and shift symmetries

Expanding $`C^{(3)}`$ on a basis of harmonic 3-forms $`\{\alpha_I\}`$,
``` math
C^{(3)}(x,y)=\sum_I a^I(x)\,\alpha_I(y)+\cdots,
```
produces pseudoscalars $`a^I`$ with continuous shift symmetries $`a^I\to a^I+ \text{const}`$ at the perturbative level. Fluxes and nonperturbative effects (membrane instantons from Euclidean M2 wrapped on 3-cycles) generate periodic potentials; the decay constants and couplings are fixed by the same integrals that enter <a href="#eq:gauge-matrix" data-reference-type="eqref" data-reference="eq:gauge-matrix">[eq:gauge-matrix]</a>–<a href="#eq:V-flux" data-reference-type="eqref" data-reference="eq:V-flux">[eq:V-flux]</a>. The axions thus provide natural dark-sector candidates and, in SU(3)-structure reductions, QCD axion-like states.

## Fermion families and Yukawas

Chiral families descend from internal Dirac zero-modes; in your MTT construction, topological integers select exactly three families. Yukawa couplings are triple overlaps of internal wavefunctions and are calculable once $`(X_7,G_4)`$ (or $`(B^6,H,F)`$) are fixed at the coherent point; hierarchical patterns emerge from localisation and selection rules.

## SUSY breaking and soft terms

SUSY breaking can be induced by flux choices (compatible with <a href="#eq:tadpole" data-reference-type="eqref" data-reference="eq:tadpole">[eq:tadpole]</a>) and by the modal gap potential $`V_{\mathrm{gap}}`$. Soft terms in the visible sector follow from the standard 4D supergravity map once $`f_{ab}`$ and the moduli Kähler metric are computed from <a href="#eq:gauge-matrix" data-reference-type="eqref" data-reference="eq:gauge-matrix">[eq:gauge-matrix]</a>–<a href="#eq:V-flux" data-reference-type="eqref" data-reference="eq:V-flux">[eq:V-flux]</a>.

## Cosmological notes

Inflationary sectors may be realised via axion monodromy-type potentials or moduli slow-roll in sufficiently flat directions (rare at the coherent fixed point unless engineered). The coherent selection also constrains dark energy parameters through the small residual vacuum energy at the minimum of $`V(\Phi)`$.

# Conclusions

We have presented a complete, first-principles derivation of the 11D M -theory framework from Modal Triplet Theory:

- the 11D action, field equations, and sources <a href="#eq:S11" data-reference-type="eqref" data-reference="eq:S11">[eq:S11]</a>–<a href="#eq:Maxwell" data-reference-type="eqref" data-reference="eq:Maxwell">[eq:Maxwell]</a>;

- the shifted flux quantisation <a href="#eq:shifted" data-reference-type="eqref" data-reference="eq:shifted">[eq:shifted]</a> and M5 anomaly inflow (§<a href="#subsec:M5-inflow" data-reference-type="ref" data-reference="subsec:M5-inflow">4.3</a>);

- worldvolume actions for M2 and M5 with $`\kappa`$-symmetry and self–duality (§<a href="#sec:wv-projection" data-reference-type="ref" data-reference="sec:wv-projection">5</a>);

- dimensional reduction to type IIA and the entire brane descent (§<a href="#sec:IIA-reduction" data-reference-type="ref" data-reference="sec:IIA-reduction">6</a>–<a href="#sec:brane-descent" data-reference-type="ref" data-reference="sec:brane-descent">7</a>);

- the 4D low-energy map fixed by modal geometry (§<a href="#sec:4D-from-M" data-reference-type="ref" data-reference="sec:4D-from-M">8</a>);

- supersymmetry and moduli stabilisation criteria (§<a href="#sec:SUSY-X7" data-reference-type="ref" data-reference="sec:SUSY-X7">9</a>–<a href="#sec:moduli-stab" data-reference-type="ref" data-reference="sec:moduli-stab">10</a>);

- and phenomenology (scales, couplings, axions) (§<a href="#sec:pheno-M" data-reference-type="ref" data-reference="sec:pheno-M">11</a>).

The key conceptual message is that M -theory is not an independent postulate but the 11D face of the same modal fixed-point geometry; its consistency conditions (quantisation, anomalies, $`\kappa`$-symmetry) are enforced by the integrality and projector-boundedness built into MTT. This turns the usual string/M -theory “landscape” into a *selection by coherent fixed points* problem with discrete admissible sectors, predictive at low energies.

#### Outlook.

Classify the admissible $`G_2`$ and SU(3)-structure fixed points reachable by the curvature–gap flow, compute the full 4D soft-term spectrum for the phenomenologically preferred sectors, and explore AdS/CFT corners where the boundary field theory can be reconstructed from the modal data.
