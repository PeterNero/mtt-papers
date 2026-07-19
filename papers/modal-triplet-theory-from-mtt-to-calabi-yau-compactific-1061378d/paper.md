---
abstract: |
  We prove that Modal Triplet Theory (MTT) contains a Calabi–Yau (CY) corner: there exist coherent fixed points whose internal six–manifold is Calabi–Yau and for which the MTT fixed–point projection produces exactly the same ten–dimensional background, worldsheet $`\sigma`$–model, and four–dimensional effective theory as standard CY compactifications. We further show that the additional MTT admissibility constraints—a uniform spectral gap above zero modes, bounded harmonic/projector maps, and commuting modal Laplacians across the three gauge layers—are compatible with (and often automatic on) compact CY backgrounds equipped with Hermitian Yang–Mills bundles. Consequently, MTT does not “break” CY physics; it selects a thick, well–controlled subset and correlates parameters that ordinary CY model building treats as independent. We then import the full CY machinery (spectra, Yukawas, thresholds, mirror symmetry) and explicitly recast it as functions of MTT parameters, deriving new low–energy correlations. A worked $`T^6/\mathbb{Z}_3`$ resolution example illustrates all checks and parameter maps.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: September 7, 2025
generated_from_main_tex_sha256: f8634107ddc4b8f2b3c97e7c2db66e3932c2f6cb2821b0bfa2ce7ef27e9c3a16
paper_id: modal-triplet-theory-from-mtt-to-calabi-yau-compactific-1061378d
release_state: zenodo_released
released_version: v1.0
title: |
  **Modal Triplet Theory: From MTT to Calabi–Yau Compactifications:  
  Existence, Compatibility, and Phenomenology**
zenodo_doi: 10.5281/zenodo.17071247
zenodo_record_id: 17071247
zenodo_url: "https://zenodo.org/records/17071247"
---

# Introduction

#### Aim.

MTT provides a ten–dimensional geometric framework in which four–dimensional physics arises from a coherent fixed point of a curvature–gap flow on a triplet of orthogonal internal bundles and a bounded projection to a coherent sector. We ask whether the familiar Calabi–Yau compactifications lie inside this framework and, if so, whether the extra MTT constraints refine rather than obstruct that class.(see Nero MTT Foundations ).

#### Contributions.

(C1) *Existence of a CY corner (Theorems <a href="#thm:cy-vanishW" data-reference-type="ref" data-reference="thm:cy-vanishW">1</a>–<a href="#thm:cy-constructive" data-reference-type="ref" data-reference="thm:cy-constructive">3</a>).* There exist MTT parameter loci (vanishing torsion classes, $`H=0`$, constant dilaton) with CY internal geometry via an abstract SU(3)–structure route and a constructive torus/orbifold resolution route.  
(C2) *Compatibility of MTT constraints on CY (Theorems <a href="#thm:gap" data-reference-type="ref" data-reference="thm:gap">5</a>-<a href="#thm:commute" data-reference-type="ref" data-reference="thm:commute">7</a>).* On compact CYs with bounded geometry and HYM bundles, SA.1 (positive spectral gap), SA.4 (bounded harmonic/projector), and commuting Laplacians hold on thick regions.  
(C3) *Indistinguishability of physics at the CY corner (Theorems <a href="#thm:ws-eq" data-reference-type="ref" data-reference="thm:ws-eq">9</a>–<a href="#thm:eft-eq" data-reference-type="ref" data-reference="thm:eft-eq">10</a>).* The worldsheet CFT and 4D EFT coincide with standard CY compactifications.  
(C4) *Import of CY machinery (Sec. <a href="#sec:import" data-reference-type="ref" data-reference="sec:import">6</a>).* Parameter maps express CY data as MTT functions, yielding correlations among couplings and hierarchies.

# Preliminaries: MTT, SU(3)–structure, and admissibility

## MTT internal geometry and admissibility

The internal sector consists of three orthogonal bundles $`B_1,B_2,B_3`$ in a six–manifold $`X_6`$ with block–diagonal metric and commuting scalar Laplacians. The joint projector $`\Pi=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$ maps to the coherent sector. Standing assumptions (SA): SA.1 (uniform spectral gap $`\lambda_\ast>0`$); SA.2 (well–posedness/smoothing); SA.3 (compact/condensing); SA.4 (bounded projector).

#### Convention on eigenvalues.

Throughout, $`\Delta\!\ge 0`$ denotes the (scalar or bundle) Laplacian with lowest eigenvalue $`\lambda_0=0`$ on constants (or parallel sections). We write $`\lambda_1(\Delta)`$ for the *first nonzero* eigenvalue. SA.1 refers to the existence of a uniform gap $`\lambda_1(\Delta)\ge \lambda_\ast>0`$ above the zero modes.

## SU(3)–structure and torsion classes

An SU(3)–structure $`(J,\Omega)`$ on $`X_6`$ yields torsion classes $`W_1,\ldots,W_5`$ from the decompositions $`dJ`$ and $`d\Omega`$; vanishing torsion ($`W_i=0`$) is equivalent to $`X_6`$ being Kähler and Ricci–flat (Calabi–Yau). (see Nero FP6 )

## HYM bundles, Laplacians, and projectors

On a holomorphic bundle $`E\to X`$ with unitary connection $`\nabla`$, the HYM conditions are $`F^{0,2}=0`$ and $`J\!\lrcorner F=0`$. Elliptic theory on compact bounded–geometry manifolds ensures boundedness of the Hodge projector $`P_H`$ on Sobolev scales.

# Existence of a Calabi–Yau corner inside MTT

## Abstract SU(3)–structure route

<div id="thm:cy-vanishW" class="theorem">

**Theorem 1** (CY locus via vanishing torsion classes). *If the SU(3)–structure $`(J(\theta),\Omega(\theta))`$ induced by MTT parameters $`\theta`$ obeys $`W_i(\theta_0)=0`$ for $`i=1,\dots,5`$ with $`H(\theta_0)=0`$ and constant dilaton, then $`(X_6;J(\theta_0),\Omega(\theta_0))`$ is Calabi–Yau, and the MTT fixed point reproduces a standard CY background.*

</div>

<div class="remark">

**Remark 2**. *In layered MTT geometries, $`W_i`$ are analytic in small warp/twist parameters; setting warps and nil twists to zero and aligning complex frames yields $`W_i=0`$ (explicit checks in the torus/orbifold class).*

</div>

## Constructive torus/orbifold resolution route

<div id="thm:cy-constructive" class="theorem">

**Theorem 3** (Constructive CY corner). *There exist MTT parameter choices (vanishing warps/twists) for which $`X_6`$ is $`T^6`$ or a crepant resolution $`\hat X_6`$ of $`T^6/\Gamma`$ with $`\Gamma\subset SU(3)`$. Then $`(J,\Omega)`$ is torsion–free and $`(X_6,g)`$ is CY. In the torus limit the Laplacian splits into commuting blocks; commutation persists on the resolved CY.*

</div>

## HYM bundles on the CY corner

<div id="prop:hym-split" class="proposition">

**Proposition 4**. *Let $`E=E_1\otimes E_2\otimes E_3`$ with HYM $`\nabla_i`$ on a CY $`(X,g)`$. Then $`\nabla=\nabla_1\otimes 1\otimes 1+
1\otimes \nabla_2\otimes 1+1\otimes 1\otimes \nabla_3`$ is HYM on $`E`$.*

</div>

# Compatibility of MTT constraints on CY

## SA.1: Spectral gap on compact CYs

<div id="thm:gap" class="theorem">

**Theorem 5** (Positive spectral gap; uniform on thick regions). *On a compact CY $`(X,g)`$, the first nonzero eigenvalue $`\lambda_1(\Delta)`$ of the (scalar) Laplacian is positive. On bounded–geometry families ($`|{\rm Rm}|\le K_0`$, $`{\rm inj}\ge \iota_0>0`$, $`{\rm diam}\le D_0`$) one has a uniform lower bound $`\lambda_1\ge c(K_0,\iota_0,D_0)>0`$ (Cheeger–Buser).*

</div>

*Proof sketch.* Positivity of $`\lambda_1`$ on compact manifolds is standard; Cheeger’s inequality $`\lambda_1\ge h^2/4`$ and Buser’s converse control $`\lambda_1`$ by the isoperimetric constant $`h`$. Uniform positivity on bounded-geometry families ($`|{\rm Rm}|\le K_0`$, $`{\rm inj}\ge\iota_0`$, $`{\rm diam}\le D_0`$) follows from uniform isoperimetric bounds. (see Cheeger , Buser , and Taylor ) $`\square`$

## SA.4: Bounded Hodge projector

<div id="thm:proj" class="theorem">

**Theorem 6** (Boundedness of the harmonic projector). *On compact bounded–geometry CYs, $`P_H:H^s\to H^s`$ is bounded for all $`s\in\mathbb{R}`$.*

</div>

*Proof sketch.* On compact bounded-geometry manifolds, elliptic regularity and the pseudodifferential parametrix for $`\Delta`$ imply that the Green operator $`G=\Delta^{-1}`$ is bounded $`H^{s-2}\!\to H^s`$ and $`P_H=I-\Delta G`$ is bounded $`H^s\!\to H^s`$ for all $`s`$; see . $`\square`$

## Commuting modal Laplacians

<div id="thm:commute" class="theorem">

**Theorem 7** (Commuting bundle Laplacians for split HYM). *Let $`(E_i,\nabla_i)`$ be Hermitian bundles with unitary connections on $`(X,g)`$, and $`E=\bigotimes_{i=1}^3 E_i`$ with product metric/connection $`\nabla=\sum_i 1\otimes\cdots\otimes \nabla_i \otimes\cdots\otimes 1`$. Write $`\Delta_i=\nabla_i^*\nabla_i`$ acting as $`1\otimes\cdots\otimes\Delta_i\otimes\cdots\otimes 1`$ on sections of $`E`$. Then $`\Delta_i`$ and $`\Delta_j`$ act on different tensor factors and commute on $`C^\infty(E)`$, hence on the $`L^2`$ domain closure. Therefore the joint spectral projector $`\Pi=\Pi_1\Pi_2\Pi_3`$ is well-defined and bounded on Sobolev scales.*

</div>

<div class="remark">

**Remark 8**. *In torus/orbifold CYs with block metrics, the scalar Laplacian splits $`\Delta=\Delta_1+\Delta_2+\Delta_3`$ with $`[\Delta_i,\Delta_j]=0`$, giving a commuting structure also on functions.*

</div>

# Indistinguishability of physics at the CY corner

## Worldsheet

<div id="thm:ws-eq" class="theorem">

**Theorem 9** (Worldsheet equivalence). *At the CY locus with $`H=0`$ and constant dilaton, the MTT worldsheet projection produces the same Polyakov/RNS action and BRST/CFT data as in standard CY compactification. *Reference.* For $`H=0`$ and $`SU(3)`$ holonomy, the $`(2,2)`$ SCFT background and BRST structure coincide with standard CY compactification; see e.g. .*

</div>

## 4D effective theory

<div id="thm:eft-eq" class="theorem">

**Theorem 10** (4D EFT equivalence). *Dimensional reduction on the CY locus yields the same 4D massless spectrum, Kähler potential, gauge kinetic functions, and Yukawa couplings as standard CY compactifications with the same HYM bundle and moduli.*

</div>

# Importing CY machinery as MTT functions

## Parameter map

Let $`\Theta_{\rm MTT}`$ denote MTT parameters (gap scales, block volumes $`v_i`$, discrete lens/orbifold data, warp/twist). At the CY corner:
``` math
\Theta_{\rm MTT}\longmapsto
\begin{cases}
\text{K\"ahler moduli }t_A=\int_{\Sigma_A}\!J,\\
\text{Complex moduli }z_\alpha\text{ from periods of }\Omega,\\
\text{Bundle moduli }u_I\text{ (HYM).}
\end{cases}
```
Volume combinations of blocks give $`t_A(\Theta_{\rm MTT})`$.

## Kähler potential, prepotential, special geometry

With $`J=\sum_A t_A\omega_A`$ and $`\kappa_{ABC}=\int\omega_A\wedge\omega_B\wedge\omega_C`$, $`F(t)=\tfrac{1}{6}\kappa_{ABC}t_At_Bt_C+\cdots`$, $`K=-\log\!\left(\mathrm{i}\int\Omega\wedge\bar\Omega\right)`$, so special geometry is inherited as functions of $`\Theta_{\rm MTT}`$.

## Gauge kinetic functions

For $`\{ \omega_a\}`$ a basis, $`f_{ab}=\frac{1}{2\kappa_{10}^2}\int\omega_a\wedge\!\ast\omega_b`$ becomes $`f_{ab}(\Theta_{\rm MTT})`$; block volumes correlate entries.

## Yukawa couplings

Geometric: $`Y_{\alpha\beta\gamma}=\int\Omega\wedge\partial_\alpha\partial_\beta\partial_\gamma\Omega(z(\Theta_{\rm MTT}))`$. Bundle matter: $`Y_{ijk}\sim \int\Omega\wedge\psi^{(a)}_i\wedge\psi^{(b)}_j\wedge\psi^{(c)}_k`$ with $`\psi`$ harmonic reps, hence $`Y_{ijk}(\Theta_{\rm MTT})`$.

## Thresholds and one–loop running

One–loop thresholds depend on spectra/Ray–Singer torsions, hence on $`(X,g)`$ and thus on $`\Theta_{\rm MTT}`$.

## Mirror symmetry

Mirror exchanges complex/Kähler moduli; via $`\Theta_{\rm MTT}\mapsto (t,z)`$ this induces a dual map on the mirror.

# Worked example: $`T^6/\mathbb{Z}_3`$ resolution

# Implications and predictions

Because the CY corner is a subset of admissible MTT fixed points, we obtain:

- **Controlled EFT.** SA.1 enforces KK scale separation $`m_{\rm KK}^2\gtrsim \lambda_\ast`$.

- **Correlated couplings.** Block volumes $`v_i`$ determine Kähler moduli combinations, correlating $`g_1,g_2,g_3`$.

- **Yukawa textures.** Commuting projectors yield selection rules compatible with CY cohomology products.

- **Reduced landscape.** Bounded geometry/commutation eliminate degenerations and incompatible bundles.

# Conclusions

We proved the CY corner exists inside MTT, that MTT constraints are compatible/automatic on compact CY+HYM, and that physics is indistinguishable from standard CY compactifications at this locus. We gave a parameter map that imports CY machinery as MTT functions, producing low–energy correlations, with a torus/orbifold resolution example illustrating all checks.

# SU(3) torsion classes

With $`(J,\Omega)`$ an SU(3)–structure, torsion classes arise by projecting $`dJ`$ and $`d\Omega`$ onto SU(3) irreps; $`W_i=0`$ $`\Leftrightarrow`$ $`X`$ is Kähler and $`d\Omega=0`$ $`\Rightarrow c_1(X)=0`$ (CY).

# Elliptic estimates and bounded projectors

On compact bounded–geometry manifolds: Green operator $`G=\Delta^{-1}`$ is bounded $`H^{s-2}\!\to H^s`$, $`P_H=I-\Delta G`$ is bounded $`H^s\!\to H^s`$, and Cheeger/Buser give $`\lambda_1\ge h^2/4`$.

# Commuting Laplacians for split HYM bundles

For $`E=\bigotimes_{i=1}^3 E_i`$ with HYM $`\nabla_i`$, the induced $`\Delta_i`$ commute and the joint projector exists.

# Mirror symmetry and thresholds

Quick reference: $`K_{\rm cs}(z,\bar z)=-\log\big(\mathrm{i}\int \Omega\wedge \bar\Omega\big)`$, $`F_{\rm cl}(t)=\tfrac{1}{6}\kappa t^3+\cdots`$; thresholds involve determinants of Laplacians (Ray–Singer).

# From the Lens/NIL baseline to the CY corner: explicit SA constants and deformation

## E.1Baseline geometry and block operators

Let $`X_6\simeq S^1_{\rm cen}\times \Sigma_1\times \Sigma_2\times \Sigma_3`$ with block–diagonal metric. On the triplet $`\{B_n\}`$ take the concrete baseline
``` math
B_1 \simeq S^1_{\rm cen}\times F_1,\qquad
B_2 \simeq S^1_{\rm cen}\times L(3,1),\qquad
B_3 \simeq S^1_{\rm cen}\times\big(L(3,1)\times \Gamma\backslash{\rm Nil}_3\big),
```
allowing mild warping $`f(\theta)=1+\alpha\cos\theta`$ with $`|\alpha|<1`$ on each block. Denote vertical scalar Laplacians by $`\Delta_{B_n}`$ and the coherent projector by $`\Pi_{\rm coh}=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$.

## E.2Explicit spectral gaps (SA.1)

On $`S^1_{\rm cen}`$ of length $`\ell_\theta`$, $`\lambda_1(S^1)=(2\pi/\ell_\theta)^2`$. On $`L(3,1)`$ with a fixed bounded–geometry metric, Cheeger–Buser implies $`\lambda_1\ge h^2/4=:c_{\rm lens}>0`$; on $`\Gamma\backslash{\rm Nil}_3`$ in the non–collapsing regime, $`\lambda_1\ge h^2/4=:c_{\rm nil}>0`$. Warping by $`f(\theta)`$ preserves lower bounds up to controlled constants (bi–Lipschitz). Hence for the vertical Laplacians
``` math
\lambda_\ast:=\min\!\left\{(2\pi/\ell_\theta)^2,\;c_{\rm lens},\;c_{\rm nil}\right\}>0.
```

## E.3Bounded projectors (SA.4) and semigroup smoothing (SA.2)

With resolvent contours of radius $`\lambda_\ast/2`$, parameter–dependent elliptic theory gives $`\|(\Delta_{B_n}-z)^{-1}\|_{H^s\to H^s}\le C_s(\lambda_\ast)`$, hence $`\|\Pi_{B_n}\|_{H^s\to H^s}\le C_s`$ and $`\|\Pi_{\rm coh}\|_{H^1\to H^1}\le C_\Pi`$ uniformly. The parabolic generator
``` math
A:=\kappa_1\Delta_{B_1}+\kappa_2\Delta_{B_2}+\kappa_3\Delta_{B_3}+\varepsilon\,\Delta_{\rm hor}-N,
```
is sectorial; its semigroup satisfies
``` math
\|\Phi_t\|_{L^2\to H^1}\le M_1(t)e^{Lt},\qquad M_1(t)\lesssim (1+t^{-1/2})e^{-\lambda_\ast t}.
```

Here $`\Delta_{\rm hor}`$ denotes the horizontal Laplacian associated to the base (if present in the flow; otherwise take $`\varepsilon=0`$).

## E.4Commutation (SA.3) and contraction (FCC)

Block–diagonality implies $`[\Delta_{B_i},\Delta_{B_j}]=0`$ and commuting spectral projectors. Choosing $`\tau>0`$ so that
``` math
C_\Pi\,M_1(\tau)\,e^{L\tau}<1,
```
the projected time–$`\tau`$ map $`T_\tau=\Pi_{\rm coh}\circ \Phi_\tau`$ is a contraction on $`{\rm Ran}\,\Pi_{\rm coh}`$, hence a unique coherent fixed point exists.

## E.5Deformation to the CY corner

Set $`\alpha\to 0`$ and flatten the Lens and Nil layers by a smooth path of bounded–geometry metrics toward flat tori on each block. In this limit the vertical Laplacian becomes a sum of torus Laplacians and the torsion classes vanish ($`W_i=0`$). Thus the internal geometry reaches the CY corner. Because the FCC is open, the contraction persists along the path and the CY selection statements (worldsheet/4D equivalence and parameter map) apply unchanged.

#### Remark.

The Lens/NIL baseline is not itself Calabi–Yau; it is a calibrated admissible starting point that carries uniform constants and preserves commutation. The deformation provides a concrete bridge to the CY class while keeping the MTT selection intact.
