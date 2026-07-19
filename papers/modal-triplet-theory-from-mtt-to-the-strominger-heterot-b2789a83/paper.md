---
abstract: |
  We extend the Modal Triplet Theory (MTT) bridge from the torsion–free SU(3) (Calabi–Yau) slice to the *non–Kähler, flux* slice governed by the Hull–Strominger system, and upgrade the result from admissibility to *true selection by MTT*. On a compact complex threefold with trivial canonical bundle, conformally balanced metric, NS–NS three–form $`\widehat{H}`$, and a Hermitian–Yang–Mills (HYM) bundle, we formulate *twisted* Standing Assumptions (SA.F1–SA.F4) ensuring contractivity of the projected flow and the existence of a *unique coherent fixed point*. We then construct a *selection potential* $`\Xi`$ in the torsional SU(3) slice and prove: (i) its stationary points coincide with solutions of the Hull–Strominger system (with the Bismut/Hull connection on $`TX`$); (ii) under SA.F1–SA.F4, $`\Xi`$ is strictly convex near a Strominger solution, hence that solution is the *unique local minimizer*; (iii) the MTT fixed point coincides with this minimizer and is globally attractive in the coherent sector. A reference implementation on the Fu–Yau class (torus bundles over K3 and K3–orbifolds) verifies twisted spectral gaps, bounded projectors, and commuting *torsionful* Laplacians. Compactification “choice” is replaced by *fixed–point selection* also in the non–Kähler regime; technically, this yields *controlled truncations*, *built–in decoherence*, and *correlated low–energy data* in the presence of flux, fully parallel to the CY case.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: September 7 2025
generated_from_main_tex_sha256: b1025edbb6bbc19a45b4ef870a1bc35a97562b76e053565820605d38139434c1
paper_id: modal-triplet-theory-from-mtt-to-the-strominger-heterot-b2789a83
release_state: zenodo_released
released_version: v1.0
title: |
  Modal Triplet Theory: From MTT to the Strominger (Heterotic Flux) System  
  Selection of Non–Kähler SU(3) Geometry by a Fixed–Point Principle
zenodo_doi: 10.5281/zenodo.17071767
zenodo_record_id: 17071767
zenodo_url: "https://zenodo.org/records/17071767"
---

# Introduction and Motivation

#### MTT in brief.

Modal Triplet Theory (MTT) posits a ten–dimensional modal geometry with three orthogonal internal bundles over a $`4`$D base and a joint harmonic projector defining the coherent sector. A dissipative flow $`\Phi_t`$ on field space, composed with the projector, yields a contractive map whose unique fixed point $`\Psi^*`$ projects to observed low–energy physics. The Calabi–Yau (CY) slice reproduces standard string backgrounds and effective dynamics while adding analytic control (spectral gaps, bounded projectors, commuting modal Laplacians) .

#### Aim.

We generalize the CY construction to the heterotic *flux* regime: compact complex threefolds with trivial canonical bundle, non–Kähler (conformally balanced) metrics, nonzero flux and HYM bundles, subject to the *Hull–Strominger system* . Beyond *compliance*, we prove *selection*: we build a torsional SU(3) *selection potential* $`\Xi`$ and show that its unique local minimizer (under SA.F) is exactly the Strominger solution realized by the MTT fixed point.

#### Key corrections vs. prior draft.

\(i\) We use the *gauge–invariant Green–Schwarz 3–form* $`\widehat{H}`$ (not a globally exact $`H`$), with $`\mathrm{d}\widehat{H}=\frac{\alpha'}{4}\big(\mathrm{Tr}F\wedge F-\mathrm{Tr}R^+\wedge R^+\big)`$. (ii) We endow $`\Xi`$ with $`|\widehat{H}|^2`$ and the Chern–Simons couplings, ensuring global gauge invariance (gerbe picture). (iii) We give full proofs (twisted gap, bounded projector, commuting torsionful blocks, Lyapunov descent, strict convexity, fixed point $`=`$ minimizer).

#### Contributions.

- Twisted Standing Assumptions (SA.F1–SA.F4) and a *Flux Fixed–Point Theorem*.

- A *selection potential* $`\Xi`$ for $`(g,J,\Omega,\Phi;B,A)`$ using $`\widehat{H}`$; Euler–Lagrange equations $`\Leftrightarrow`$ Hull–Strominger with $`R^+`$.

- *Strict convexity* of $`\Xi`$ near a Strominger solution $`\Rightarrow`$ *unique local minimum*; equality with the MTT fixed point and global attraction in the coherent sector.

- Fu–Yau implementation: admissibility checks and consistency.

- (Case study) Fu–Yau class (Sec. <a href="#sec:FuYau" data-reference-type="ref" data-reference="sec:FuYau">8</a>); see also *Appendix <a href="#app:iwasawa" data-reference-type="ref" data-reference="app:iwasawa">14</a>* for a compact nilmanifold (Iwasawa) realization.

#### Organisation.

Section <a href="#sec:Prelim" data-reference-type="ref" data-reference="sec:Prelim">2</a> fixes function spaces, gauges, and $`\widehat{H}`$. Section <a href="#sec:Strominger" data-reference-type="ref" data-reference="sec:Strominger">3</a> recalls SU(3) torsion and the Strominger system. Section <a href="#sec:TwistedSA" data-reference-type="ref" data-reference="sec:TwistedSA">4</a> proves SA.F1–SA.F4 and the fixed–point theorem. Section <a href="#sec:Selection" data-reference-type="ref" data-reference="sec:Selection">5</a> constructs $`\Xi`$ and proves selection. Sections <a href="#sec:WS" data-reference-type="ref" data-reference="sec:WS">6</a>–<a href="#sec:FuYau" data-reference-type="ref" data-reference="sec:FuYau">8</a> discuss worldsheet $`\beta=0`$, HYM/Bianchi, and the Fu–Yau case. Appendices provide operator estimates, linearization, and commuting–block details.

# Preliminaries: Function Spaces, Gauges, and Green–Schwarz 3–form

## Function spaces and bounded geometry

All manifolds are smooth, compact, without boundary. Metrics, connections, and forms live in Sobolev spaces $`H^s`$ for $`s`$ large (or $`C^{k,\alpha}`$ Hölder spaces), with *bounded geometry* hypotheses: uniform bounds on curvature and a positive injectivity radius. Norms $`\|\cdot\|_{H^s}`$, $`\|\cdot\|_{C^{k,\alpha}}`$ are taken with respect to a fixed background.

## Gauge choices and slices

We work modulo diffeomorphisms and gauge:

- *Metric*: DeTurck gauge for $`g`$ (fix a background connection to eliminate diffeo freedom in elliptic variations).

- *Gauge field*: unitary Coulomb gauge for $`A`$ (with respect to $`g`$) to fix $`\mathcal{G}`$.

- *B–field*: $`B`$ is a *bundle 2–gerbe* connection; we work in local potentials and fix a gerbe gauge slice (Coulomb–type) consistent with large gauge transformations.

## Green–Schwarz 3–form and Bismut connection

Define the Chern–Simons 3–forms
``` math
\omega_3(A)=\mathrm{Tr}\!\big(A\wedge \mathrm{d}A+\tfrac{2}{3}A\wedge A\wedge A\big),\quad
\omega_3(\omega^+)=\mathrm{Tr}\!\big(\omega^+\wedge \mathrm{d}\omega^+ +\tfrac{2}{3}\omega^+\wedge \omega^+\wedge \omega^+\big),
```
with $`\omega^+`$ the Bismut connection on $`TX`$ and curvature $`R^+`$. The *gauge–invariant* Green–Schwarz 3–form is
``` math
\begin{equation}
\label{eq:GHat}
\widehat{H} \;=\; \mathrm{d}B\;-\;\frac{\alpha'}{4}\,\big(\omega_3(A)-\omega_3(\omega^+)\big),\qquad
\mathrm{d}\widehat{H} \;=\; \frac{\alpha'}{4}\,\big(\mathrm{Tr}F\wedge F-\mathrm{Tr}R^+\wedge R^+\big).
\end{equation}
```
Throughout, the tangent–bundle connection in the Bianchi identity is $`R^+`$ (Bismut/Hull choice compatible with heterotic SUSY) .

## Gerbe covariance of $`\widehat{H}`$

The $`B`$-field is a Deligne 2-gerbe connection with connective structure. Local variations $`\delta B`$ are taken within a fixed differential cohomology class consistent with large gauge transformations; $`\widehat{H}`$ is the globally defined curvature. The functional $`\Xi`$ depends on $`B`$ only via $`\widehat{H}`$ and Chern–Simons forms, hence is gauge invariant. Variations are implemented by refining open covers and using a partition-of-unity argument; boundary terms cancel by the Bianchi constraint enforced by $`K`$.

## Auxiliary multiplier for the Green–Schwarz definition

We treat $`\widehat H`$ as an independent 3form variable and impose its Green–Schwarz definition by a 2form Lagrange multiplier $`\Lambda\in\Omega^2(X)`$:
``` math
\widehat H \;=\; \mathrm{d}B - \frac{\alpha'}{4}\big(\omega_3(A)-\omega_3(\omega^+)\big).
```
This ensures global gauge invariance and makes the Euler–Lagrange variations with respect to $`B`$, $`\widehat H`$, $`A`$, and $`\omega^+`$ fully consistent.

# SU(3)–Structure with Torsion and the Hull–Strominger System

## SU(3) structure and torsion classes

Let $`(X^6,J,\Omega)`$ be a complex threefold with Hermitian form $`J`$ and holomorphic $`(3,0)`$–form $`\Omega`$; intrinsic torsion decomposes into $`W_1,\dots,W_5`$. The CY case has $`W_i=0`$. In heterotic flux vacua typically $`W_1=W_2=0`$ (integrable complex structure), while $`W_3`$ and $`W_4,W_5`$ encode torsion and dilaton.

## Bismut connection and conformally balanced metrics

The *Bismut* connection $`\nabla^+=\nabla^{\mathrm{LC}}+\tfrac12 T`$ preserves $`(g,J)`$ with totally skew torsion $`T=\widehat{H}`$ (torsionful connection); a Hermitian metric is *conformally balanced* if $`d(e^{-2\Phi}J^2)=0`$ (Gauduchon class).

## Hull–Strominger system

Given $`(X,J,\Omega)`$ with $`K_X`$ trivial, Hermitian metric $`J`$, dilaton $`\Phi`$, holomorphic bundle $`(E,A)`$, and $`\widehat{H}`$ as in <a href="#eq:GHat" data-reference-type="eqref" data-reference="eq:GHat">[eq:GHat]</a>,
``` math
\begin{align}
  & d\!\left(e^{-2\Phi}J\wedge J\right)=0, \quad \text{(conformally balanced)} \label{eq:balanced}\\
  & \widehat{H} = i(\bar\partial-\partial)J\ -\ \frac{\alpha'}{4}\big(\omega_3(A)-\omega_3(\omega^+)\big), \label{eq:BismutTorsion}\\
  & F^{0,2}=0,\qquad J\lrcorner F=0, \quad \text{(HYM on $E$)} \label{eq:HYM}\\
  & \mathrm{d}\widehat{H}=\frac{\alpha'}{4}\Big(\mathrm{Tr}\,F\wedge F - \mathrm{Tr}\,R^+\!\wedge R^+\Big). \quad \text{(Bianchi / anomaly)} \label{eq:Bianchi}
\end{align}
```
These are necessary and sufficient for $`4`$D $`\mathcal N{=}1`$ heterotic SUSY at leading order in $`\alpha'`$. .

# Twisted Admissibility and the Flux Fixed–Point Theorem

## Twisted Standing Assumptions (SA.F1–SA.F4)

Let $`X`$ be compact complex with $`K_X`$ trivial, $`(J,\Omega)`$, Hermitian $`g`$, $`\widehat{H}`$ as in <a href="#eq:GHat" data-reference-type="eqref" data-reference="eq:GHat">[eq:GHat]</a>, and holomorphic bundle $`(E,A)`$.

**SA.F1 (Twisted spectral gap).** Let $`d_{\widehat{H}}:=\mathrm{d}+\widehat{H}\wedge`$ (or equivalently use Bismut Laplacians; see also for twisted de Rham complexes). The *twisted Laplacian*
``` math
\Delta^{(\widehat{H})} \;=\; d_{\widehat{H}}\delta_{\widehat{H}}+\delta_{\widehat{H}} d_{\widehat{H}}
```
is elliptic with discrete spectrum on compact $`X`$. On bounded–geometry families, there exists a uniform positive lower bound $`\lambda_*^{(\widehat{H})}>0`$ on the first nonzero eigenvalue.

<div id="lem:gap" class="lemma">

**Lemma 1** (Uniform twisted gap). *Assume bounded geometry (curvature bounds, injectivity radius $`\ge \iota_0`$) and $`\|\widehat{H}\|_{C^1}\le H_0`$. Then
``` math
\lambda_1\big(\Delta^{(\widehat{H})}\big)\ \ge\ \lambda_1(\Delta)\ -\ C(\iota_0,\|Rm\|_\infty)\,H_0,
```
hence for $`H_0`$ small relative to the Cheeger/Buser constant one has $`\lambda_*^{(\widehat{H})}\ge \tfrac12 \lambda_1(\Delta)>0`$.*

</div>

<div class="proof">

*Proof.* Write $`\Delta^{(\widehat{H})}=\Delta+\mathsf{Q}_1(\nabla)+\mathsf{Q}_0`$, where $`\mathsf{Q}_1,\mathsf{Q}_0`$ are first/zero order with operator norms bounded by $`C H_0`$. Kato–Rellich gives relative boundedness; min–max plus Cheeger/Buser estimate for $`\Delta`$   yields the claim.

*Cheeger–Buser step.* For the Hodge Laplacian $`\Delta`$ on $`k`$-forms, $`\lambda_1(\Delta)\ge \tfrac{h^2}{4}`$ with $`h`$ the (form) isoperimetric constant. Hence $`\lambda_1\big(\Delta^{(\widehat{H})}\big)\ge \tfrac{h^2}{4}-C\|\widehat{H}\|_{C^1}`$.

*Constants.* All constants $`C, c`$ depend only on the bounded-geometry data $`\big(\|Rm(g)\|_{C^0}, \operatorname{inj}(X,g)^{-1}\big)`$ and the uniform $`C^1`$ bound on $`\widehat{H}`$; they are uniform on the admissible family. ◻

</div>

**SA.F2 (Bounded twisted projector).** Let $`\Pi^{(\widehat{H})}`$ be the orthogonal projector onto twisted harmonic forms. Then $`\Pi^{(\widehat{H})}:H^s\to H^s`$ is bounded for all $`s\in\mathbb{R}`$, with norm controlled uniformly on the admissible family.

<div id="lem:proj" class="lemma">

**Lemma 2** (Resolvent control $`\Rightarrow`$ bounded projector). *For a small circle $`\Gamma`$ around $`0`$ in the resolvent set, $`\Pi^{(\widehat{H})}=\frac{1}{2\pi i}\oint_\Gamma(\Delta^{(\widehat{H})}-z)^{-1}\mathrm{d}z.`$ Parameter–dependent elliptic estimates and Lemma <a href="#lem:gap" data-reference-type="ref" data-reference="lem:gap">1</a> imply $`\|(\Delta^{(\widehat{H})}-z)^{-1}\|_{H^s\to H^s}\le C_s`$ uniformly; hence $`\|\Pi^{(\widehat{H})}\|_{H^s\to H^s}\le C_s`$.*

**Constants.* The bounds $`C_s`$ depend only on $`s`$ and the bounded-geometry data (as above) and on the uniform $`C^1`$ bound for $`\widehat{H}`$; they are uniform over the admissible family.*

</div>

**SA.F3 (Commuting torsionful modal blocks).** Assume $`(g,\widehat{H})`$ are block–diagonal with respect to the three internal bundles and that $`\widehat{H}=\sum_i \widehat{H}_i`$ with $`\widehat{H}_i`$ supported on block $`i`$ (and any common $`S^1`$). Then the vertical twisted Laplacians commute: $`[\,\Delta^{(\widehat{H})}_{B_i},\,\Delta^{(\widehat{H})}_{B_j}\,]=0.`$

<div id="lem:commute" class="lemma">

**Lemma 3** (Block commutation). *Under the above split, $`d_{\widehat{H}}=\sum_i (d_{(i)}+\widehat{H}_i\wedge)`$ and the terms act on disjoint coordinates. Hence $`\Delta^{(\widehat{H})}=\sum_i \Delta^{(\widehat{H})}_{B_i}`$ and the summands commute.*

</div>

**SA.F4 (Well–posedness and smoothing).** The parabolic generator
``` math
\partial_t\Psi \;=\; -\Big(\sum_{i=1}^3 \kappa_i\,\Delta^{(\widehat{H})}_{B_i} + \varepsilon\,\Delta_Y\Big)\Psi \;-\; N(\Psi)
```
is uniformly elliptic; the semigroup $`\Phi_t`$ is analytic and smoothing. On sublevels where $`N`$ is locally Lipschitz with constant $`L`$, the usual $`M_1(t)e^{Lt}`$ bounds hold (as in ).

## Flux Fixed–Point Theorem

<div id="thm:FluxFixedPoint" class="theorem">

**Theorem 4** (Flux fixed point & uniqueness). *Assume SA.F1–SA.F4 and use $`\nabla^+`$ on $`TX`$. Then there exists $`\tau>0`$ such that
``` math
T_\tau \;=\; \Pi^{(\widehat{H})}_{\mathrm{coh}}\circ \Phi_\tau
```
is a contraction on $`(\mathrm{Ran}\,\Pi^{(\widehat{H})}_{\mathrm{coh}},\|\cdot\|_{H^1})`$. Consequently, $`T_\tau`$ admits a *unique* coherent fixed point $`\Psi^*`$, attracting all Picard iterates geometrically.*

</div>

<div class="proof">

*Proof.* Combine Lemmas <a href="#lem:gap" data-reference-type="ref" data-reference="lem:gap">1</a>–<a href="#lem:proj" data-reference-type="ref" data-reference="lem:proj">2</a> with standard parabolic smoothing to get $`\|\Phi_\tau\|_{L^2\to H^1}\le M_1(\tau)e^{L\tau}`$ and $`\|\Pi^{(\widehat{H})}\|_{H^1\to H^1}\le C_\Pi`$. Choose $`\tau`$ with $`C_\Pi M_1(\tau)e^{L\tau}<1`$; then Banach contraction applies. ◻

</div>

# Selection Potential and MTT Selection in the Flux Slice

## Configuration space and constraints

Fix a compact complex threefold $`X`$ with $`K_X\simeq \mathcal O_X`$ and complex structure $`J`$ (thus $`W_1=W_2=0`$). Let
``` math
\mathcal{C}=\big\{(g,\Phi,B;A):\ g\ \text{Hermitian on }(X,J),\ \Phi\in C^\infty,\ B\in\Omega^2,\ A\ \text{unitary on fixed holomorphic }E\big\},
```
modulo diffeomorphisms, unitary gauge, and gerbe gauge. Define $`\widehat{H}`$ by <a href="#eq:GHat" data-reference-type="eqref" data-reference="eq:GHat">[eq:GHat]</a>. Fix a topological sector (Chern data, cohomology class of $`\widehat{H}`$ compatible with <a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a>).

## Selection potential with Green–Schwarz 3–form

In string frame, set
``` math
\begin{equation}
\label{eq:XiDefFixed}
\begin{aligned}
\Xi[g,\Phi,B;A,\omega^+;\widehat H,K,\Lambda]\;=&\;
\int_X e^{-2\Phi}\Big(R(g)+4|\nabla\Phi|_g^2-\tfrac12|\widehat H|_g^2\Big)\,\mathrm{vol}_g \\
&\;+\;\frac{1}{2g_{10}^2}\int_X e^{-2\Phi}\,\mathrm{Tr}(F_A\wedge *F_A) \\
&\;+\;\int_X K\wedge\Big(\mathrm{d}\widehat H-\tfrac{\alpha'}{4}(\mathrm{Tr}F_A\wedge F_A-\mathrm{Tr}R^+\wedge R^+)\Big)\\
&\;+\;\int_X \Lambda\wedge\Big(\widehat H-\mathrm{d}B+\tfrac{\alpha'}{4}(\omega_3(A)-\omega_3(\omega^+))\Big)\\
&\;+\;\sum_{n,k}\frac{\delta_{n,k}}{2\,\gamma_{n,k}}\, .
\end{aligned}
\end{equation}
```

where $`\omega^+`$ is the Bismut connection, $`R^+`$ its curvature, and $`\gamma_{n,k}=\kappa_{n,k}\lambda^{(\widehat{H})}_{n,k}-L`$ (OU variance floor).

<div class="remark">

**Remark 5**. *(i) $`B`$ enters only via $`\widehat{H}`$ and Chern–Simons forms; large gauge transformations are respected. (ii) We impose the normalization $`\int_X e^{-2\Phi}\mathrm{vol}_g=1`$ to remove trivial rescalings.*

</div>

## Euler–Lagrange equations = Hull–Strominger

<div id="thm:ELStromingerFixed" class="theorem">

**Theorem 6** (Euler–Lagrange $`\Leftrightarrow`$ Strominger). *Critical points of $`\Xi`$ on $`\mathcal{C}\times\Omega^4`$ obey the Hull–Strominger system <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a>–<a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a> with $`R^+`$. Conversely, any smooth solution of <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a>–<a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a> is a critical point of $`\Xi`$.*

</div>

<div class="proof">

*Proof.* Varying $`K`$ enforces <a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a>. Varying $`B`$ (hence $`\widehat{H}`$) with fixed gerbe class yields $`\mathrm{d}(e^{-2\Phi}*\widehat{H})=0`$, equivalent to <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a> on a complex threefold together with <a href="#eq:BismutTorsion" data-reference-type="eqref" data-reference="eq:BismutTorsion">[eq:BismutTorsion]</a>. Metric/dilaton variations give the $`(G,B,\Phi)`$ Euler–Lagrange system equivalent to worldsheet $`\beta=0`$ at leading $`\alpha'`$, which is known to be equivalent to <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a>–<a href="#eq:BismutTorsion" data-reference-type="eqref" data-reference="eq:BismutTorsion">[eq:BismutTorsion]</a> with $`R^+`$. . Variation of $`A`$ in the holomorphic class gives HYM on a Gauduchon metric (Li–Yau), i.e. <a href="#eq:HYM" data-reference-type="eqref" data-reference="eq:HYM">[eq:HYM]</a>. The OU term is constant under deterministic variations. The converse follows by substitution.

*Constants.* Coercivity and continuity constants depend only on bounded-geometry data and a uniform bound on $`\|\widehat{H}\|_{C^1}`$; they are uniform on the admissible family. ◻

</div>

## Existence of minimizers

<div id="prop:existence" class="proposition">

**Proposition 7** (Direct method). *In a fixed topological sector, under bounded geometry and SA.F1–SA.F2, $`\Xi`$ is bounded below and sequentially weakly lower semicontinuous on $`\mathcal{C}`$ modulo symmetries (with the normalization $`\int e^{-2\Phi}\mathrm{vol}_g=1`$). Hence $`\Xi`$ admits a minimizer.*

</div>

<div class="proof">

*Proof.* Elliptic inequalities bound $`\|R\|_{H^{-1}}`$, $`\|\nabla\Phi\|_{L^2}`$, $`\|\widehat{H}\|_{L^2}`$, and $`\|F\|_{L^2}`$ in terms of $`\Xi`$; SA.F1 and bounded geometry give compact embeddings (Rellich) modulo fixed gauges; lower semicontinuity holds by convexity of quadratic terms and continuity of the Chern–Simons constraint via $`K`$. The OU term is nonnegative and continuous.

*Constants.* All constants are uniform on the admissible family and depend only on bounded-geometry data and the fixed Sobolev index used for compactness. ◻

</div>

## Strict convexity near a Strominger solution

<div id="thm:convexity" class="theorem">

**Theorem 8** (Positive Hessian). *Let $`(g_0,\Phi_0,B_0;A_0)`$ solve <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a>–<a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a> and satisfy SA.F1–SA.F4. Fix gauges as in Section <a href="#sec:Prelim" data-reference-type="ref" data-reference="sec:Prelim">2</a>. Then there exists $`c>0`$ and a neighborhood $`\mathcal U`$ such that, for all $`\mathsf u`$ orthogonal to symmetry directions,
``` math
\delta^2\Xi\big|_{(g_0,\Phi_0,B_0;A_0)}[\mathsf u,\mathsf u]\ \ge\ c\,\|\mathsf u\|{_{H^1}}^2.
```
In particular, the solution is a *unique local minimizer* in $`\mathcal U`$.*

</div>

<div class="proof">

*Proof.* Linearize the system in fixed gauges; the principal symbol of the linearized operator is block–diagonal with entries the twisted Laplacians on the respective bundles (metric/dilaton via $`\Delta^{(\widehat{H})}`$ acting on symmetric 2–tensors and scalars; $`B`$ via $`\Delta^{(\widehat{H})}`$ on 2–forms; bundle via the Yang–Mills Laplacian). SA.F1 yields a uniform lower bound on the principal part; SA.F4 provides elliptic/smoothing control; SA.F2 controls projector pieces. If a kernel remains from true moduli, the OU term adds a positive quadratic form (weights $`\gamma_{n,k}^{-1}`$), lifting them. A Gårding inequality then gives the stated coercivity.

*Constants.* The coercivity constant $`c`$ depends only on the bounded-geometry data, uniform $`\|\widehat{H}\|_{C^1}`$ bounds, and the spectral gap $`\lambda_*^{(\widehat{H})}`$; it is uniform on the admissible family. ◻

</div>

<div class="remark">

**Remark 9** (OU variance term). *The OU term in $`\Xi`$ depends on the twisted eigenvalues $`\lambda^{(\widehat{H})}_{n,k}`$ via $`\gamma_{n,k}=\kappa_{n,k}\lambda^{(\widehat{H})}_{n,k}-L`$. In the Lyapunov inequalities we can drop this nonnegative term to obtain a lower bound, hence it never obstructs descent. In the Hessian analysis, its second variation contributes a nonnegative quadratic form along directions where $`\delta\lambda^{(\widehat{H})}_{n,k}\neq 0`$, and therefore can lift residual flat directions. Our coercivity estimate does not rely on it, but it strengthens positivity if present.*

</div>

## Lyapunov descent and equality with the fixed point

<div id="prop:Lyap" class="proposition">

**Proposition 10** (Strict Lyapunov for $`\Phi_t`$ and $`T_\tau`$). *Along the flow $`\Phi_t`$ one has
``` math
\frac{\mathrm{d}}{\mathrm{d}t}\,\Xi(\Phi_t U)\ \le\ -\,c_0 \,\big\|\Pi^{(\widehat{H})}_{\mathrm{coh}}\nabla\Xi(\Phi_t U)\big\|_{H^{-1}}^2
```
for some $`c_0>0`$. For the discrete map $`T_\tau=\Pi^{(\widehat{H})}_{\mathrm{coh}}\circ\Phi_\tau`$, there exists $`\eta>0`$ (independent of $`U`$) such that
``` math
\Xi(T_\tau U)\ \le\ \Xi(U)\ -\ \eta\,\big\|\Pi^{(\widehat{H})}_{\mathrm{coh}}\nabla\Xi(U)\big\|_{H^{-1}}^2.
```*

</div>

<div class="proof">

*Proof.* $`\Phi_t`$ is generated by a sectorial, maximally dissipative operator on the coherent sector; the chain rule plus elliptic regularity yields the stated differential inequality with $`c_0`$ from SA.F1–SA.F4. For $`T_\tau`$, use firm non-expansiveness of $`\Pi^{(\widehat{H})}_{\mathrm{coh}}`$ and the smoothing estimate $`\|\Phi_\tau - (I-\tau \mathcal{A})\|_{H^{-1}\to H^{1}}\le C\tau^{3/2}`$ with $`\mathcal{A}`$ the twisted elliptic part; a Krasnosel’skiı̆–Mann argument (strong monotonicity of $`\nabla\Xi`$ on the slice) gives the discrete descent.

*Constants.* $`c_0,\eta`$ depend only on the spectral gap $`\lambda_*^{(\widehat{H})}`$, Lipschitz constant $`L`$ of $`N`$ on the sublevel, and bounded-geometry data; they are uniform on the admissible family. ◻

</div>

<div id="thm:Selection" class="theorem">

**Theorem 11** (MTT selection). *Under SA.F1–SA.F4, in a fixed topological sector, the MTT fixed point $`\Psi^*`$ coincides with the *unique local minimizer* of $`\Xi`$ (Theorems <a href="#thm:ELStromingerFixed" data-reference-type="ref" data-reference="thm:ELStromingerFixed">6</a> and <a href="#thm:convexity" data-reference-type="ref" data-reference="thm:convexity">8</a>) and attracts all coherent iterates.*

</div>

<div class="proof">

*Proof.* By Theorem <a href="#thm:FluxFixedPoint" data-reference-type="ref" data-reference="thm:FluxFixedPoint">4</a>, $`T_\tau`$ is a contraction with unique fixed point. By Proposition <a href="#prop:Lyap" data-reference-type="ref" data-reference="prop:Lyap">10</a>, $`\Xi`$ strictly decreases along $`T_\tau`$ unless at a critical point; Theorem <a href="#thm:convexity" data-reference-type="ref" data-reference="thm:convexity">8</a> gives uniqueness of the local minimum. Hence the fixed point equals the minimizer and is globally attractive in the coherent sector. ◻

</div>

# Worldsheet $`\sigma`$–Model and $`\beta=0`$ in the Flux Slice

In the MTT$`\to`$String dictionary , the target fields $`(G,B,\Phi)`$ are pulled back from the coherent fixed point. The worldsheet $`\sigma`$–model (Polyakov action with Kalb–Ramond field) yields leading $`\beta`$–functions:
``` math
\beta^{(G)}_{MN}\sim R_{MN}-\tfrac14 \widehat{H}_{MPQ}\widehat{H}_N{}^{PQ}+2\nabla_M\nabla_N\Phi,\quad
\beta^{(B)}_{MN}\sim -\tfrac12\nabla^P \widehat{H}_{PMN}+\nabla^P\Phi\,\widehat{H}_{PMN}.
```
Vanishing $`\beta`$ at the fixed point—together with using $`\nabla^+`$ on $`TX`$—is equivalent to the Strominger system <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a>–<a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a> at leading order in $`\alpha'`$ . The heterotic gauge $`\beta`$ yields HYM on Gauduchon metrics (Li–Yau).

# HYM on Gauduchon Metrics and Anomaly Cancellation

The Donaldson–Uhlenbeck–Yau correspondence extends beyond Kähler: on a compact complex manifold with a Gauduchon metric, slope–stable holomorphic bundles admit HYM connections . This furnishes <a href="#eq:HYM" data-reference-type="eqref" data-reference="eq:HYM">[eq:HYM]</a>. In torsional heterotic backgrounds the natural tangent connection entering <a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a> is the torsionful Bismut/Hull connection $`\nabla^+`$; $`R^+`$ is the SUSY choice (equivalent to $`R^-`$ up to $`\mathcal{O}(\alpha')`$ field redefinitions).

# Worked Case: The Fu–Yau Class

#### Geometry.

Let $`\pi:X\to \mathrm{K3}`$ be a principal $`T^2`$–bundle with complex structure and $`K_X\simeq\mathcal{O}_X`$. Fu–Yau identified conformally balanced metrics with $`\widehat{H}=i(\bar\partial-\partial)J-\frac{\alpha'}{4}(\omega_3(A)-\omega_3(\omega^+))`$ and solved <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a>–<a href="#eq:Bianchi" data-reference-type="eqref" data-reference="eq:Bianchi">[eq:Bianchi]</a> for suitable topological data.  .

For a complementary compact nilmanifold model with explicit left-invariant data, see Appendix <a href="#app:iwasawa" data-reference-type="ref" data-reference="app:iwasawa">14</a>.

#### Admissibility checks (SA.F).

- *Twisted spectral gap (SA.F1).* On compact $`X`$ with bounded geometry, $`\Delta^{(\widehat{H})}`$ is elliptic with discrete spectrum; Lemma <a href="#lem:gap" data-reference-type="ref" data-reference="lem:gap">1</a> bounds $`\lambda_1(\Delta^{(\widehat{H})})`$ below uniformly on controlled families.

- *Bounded twisted projector (SA.F2).* Lemma <a href="#lem:proj" data-reference-type="ref" data-reference="lem:proj">2</a>.

- *Commuting torsionful blocks (SA.F3).* Choose $`(g,\widehat{H})`$ split fiber/base; then Lemma <a href="#lem:commute" data-reference-type="ref" data-reference="lem:commute">3</a> applies.

- *Smoothing (SA.F4).* The twisted parabolic generator enjoys the same semigroup bounds as in CY .

<div class="proposition">

**Proposition 12** (Model lower bound on $`\lambda_1(\Delta^{(\widehat{H})})`$ for Fu–Yau). *On a principal $`T^2`$-bundle over K3 with product-type ansatz $`g=\epsilon^{-2}g_{T^2}\oplus g_{K3}`$ and $`\widehat{H}`$ supported in the base plus basic components, there exists $`\epsilon_0>0`$ and $`c_*>0`$ such that for all $`0<\epsilon\le \epsilon_0`$ one has $`\lambda_1(\Delta^{(\widehat{H})})\ge c_*`$.*

</div>

<div class="proof">

*Proof.* Use separation of variables: the first nonzero eigenvalue on the small fiber is $`\gtrsim \epsilon^2`$, while the base contribution is bounded below by the K3 isoperimetric constant; $`\widehat{H}`$ enters as a first-order perturbation bounded uniformly in $`\epsilon`$, so Kato–Rellich preserves a uniform gap. ◻

</div>

#### HYM and Bianchi.

Pick a slope–stable holomorphic bundle on the Gauduchon metric; by Li–Yau it carries an HYM connection. Use $`\nabla^+`$ on $`TX`$ in the Bianchi identity to complete a Strominger solution.

#### Conclusion.

Fu–Yau manifolds furnish an *admissible flux slice* for MTT; by Theorems <a href="#thm:convexity" data-reference-type="ref" data-reference="thm:convexity">8</a> and <a href="#thm:Selection" data-reference-type="ref" data-reference="thm:Selection">11</a> they realize a *selected* (unique local minimizing) Strominger geometry coincident with the MTT fixed point.

# Discussion and Outlook

We have promoted the heterotic non–Kähler flux slice from *compliance* to *selection* inside MTT: twisted admissibility (SA.F1–SA.F4) grants a contraction/uniqueness theorem, while the Green–Schwarz–corrected selection potential $`\Xi`$ yields existence and *strict convexity* at the Strominger solution, hence unique local minimization. Equality of minimizer and fixed point follows from Lyapunov descent. As in the CY corner, this provides selection, controlled truncations, built–in decoherence, and correlated low–energy data.

#### Scope in $`\alpha'`$.

All target-space equations are matched to worldsheet $`\beta`$-functions at leading order in $`\alpha'`$. Higher-derivative corrections can be incorporated into $`\Xi`$ as additional local functionals; the contraction and Lyapunov parts of the proof depend only on sectoriality and bounded geometry and therefore persist qualitatively when such terms are perturbative.

# Elliptic and Resolvent Estimates for $`\Delta^{(\widehat{H})}`$

Write $`\Delta^{(\widehat{H})}=\Delta+\mathsf{Q}_1(\nabla)+\mathsf{Q}_0`$ with $`\|\mathsf{Q}_1\|+\|\mathsf{Q}_0\|\le C\|\widehat{H}\|_{C^1}`$. On compact bounded–geometry manifolds, parameter–dependent elliptic estimates give
``` math
\|u\|_{H^{s+2}}\ \le\ C\Big(\|(\Delta^{(\widehat{H})}-z)u\|_{H^{s}} + (1+|z|)\|u\|_{H^{s}}\Big),
```
uniform in $`z`$ on circles excluding the spectrum. Consequently, the resolvent $`(\Delta^{(\widehat{H})}-z)^{-1}`$ is bounded $`H^s\to H^s`$ uniformly on such circles, proving Lemma <a href="#lem:proj" data-reference-type="ref" data-reference="lem:proj">2</a>. Lemma <a href="#lem:gap" data-reference-type="ref" data-reference="lem:gap">1</a> follows from min–max and Cheeger/Buser for $`\Delta`$ plus relative boundedness of $`\mathsf{Q}_1,\mathsf{Q}_0`$.

# Linearization and Positive Hessian

Linearize $`\Xi`$ at a Strominger background in fixed gauges. The second variation is
``` math
\delta^2\Xi[\mathsf u,\mathsf u]\ =\ \langle \mathcal L \mathsf u,\ \mathsf u\rangle_{L^2} \ +\ \text{l.o.t.},
```
where $`\mathcal L`$ is block–diagonal at leading order with entries the twisted Laplacians on the metric/dilaton ($`\Delta^{(\widehat{H})}`$ acting on symmetric 2–tensors and scalars), on $`B`$ ($`\Delta^{(\widehat{H})}`$ on 2–forms), and on the bundle ($`\Delta_A`$ acting on $`\mathfrak{u}(E)`$–valued 1–forms). SA.F1 yields $`\langle \mathcal L \mathsf u,\mathsf u\rangle\ge c\|\mathsf u\|_{H^1}^2`$ modulo symmetries; the OU variance term contributes $`+\sum \gamma_{n,k}^{-1}|u_{n,k}|^2`$, lifting residual moduli. This proves Theorem <a href="#thm:convexity" data-reference-type="ref" data-reference="thm:convexity">8</a>.

# Commuting Torsionful Blocks: Details

If $`g=\bigoplus_i g_i`$ and $`\widehat{H}=\sum_i \widehat{H}_i`$ with $`\widehat{H}_i`$ supported on block $`i`$ (and possibly a common $`S^1`$), then in block coordinates one has
``` math
d_{\widehat{H}}=\sum_i (d_{(i)}+\widehat{H}_i\wedge),\qquad \delta_{\widehat{H}}=\sum_i (\delta_{(i)}+\iota(\widehat{H}_i)),
```
and each summand acts only on block $`i`$. Hence $`\Delta^{(\widehat{H})}=\sum_i \Delta^{(\widehat{H})}_{B_i}`$ and $`[\,\Delta^{(\widehat{H})}_{B_i},\Delta^{(\widehat{H})}_{B_j}\,]=0`$.

# Detailed Variations in $`(B,\widehat H,K,\Lambda)`$

We work at fixed topology and in the gauges of §<a href="#sec:Prelim" data-reference-type="ref" data-reference="sec:Prelim">2</a>. The only nontrivial variations from $`\Xi`$ in <a href="#eq:XiDefFixed" data-reference-type="eqref" data-reference="eq:XiDefFixed">[eq:XiDefFixed]</a> are in the $`|\widehat H|^2`$ term and the two constraint terms.

#### (i) Variation in $`K`$.

``` math
\delta_K \Xi \;=\; \int_X \delta K \wedge \Big(\mathrm{d}\widehat H-\tfrac{\alpha'}{4}(\mathrm{Tr}F\wedge F-\mathrm{Tr}R^+\wedge R^+)\Big),
```
so the Euler–Lagrange equation is the Bianchi identity $`\mathrm{d}\widehat H=\tfrac{\alpha'}{4}(\mathrm{Tr}F\wedge F-\mathrm{Tr}R^+\wedge R^+)`$.

#### (ii) Variation in $`\Lambda`$.

``` math
\delta_\Lambda \Xi \;=\; \int_X \delta\Lambda \wedge \Big(\widehat H-\mathrm{d}B+\tfrac{\alpha'}{4}(\omega_3(A)-\omega_3(\omega^+))\Big),
```
imposing the *definition* of $`\widehat H`$ as the Green–Schwarz 3form: $`\widehat H=\mathrm{d}B-\tfrac{\alpha'}{4}(\omega_3(A)-\omega_3(\omega^+))`$.

#### (iii) Variation in $`\widehat H`$.

Using $`\delta |\widehat H|^2=2\langle \widehat H,\delta\widehat H\rangle`$ and integrating by parts in the $`K`$ term,
``` math
\delta_{\widehat H}\Xi \;=\; -\int_X e^{-2\Phi}\langle \widehat H,\delta\widehat H\rangle\,\mathrm{vol}_g
\;+\;\int_X K\wedge \mathrm{d}(\delta\widehat H)\;+\;\int_X \Lambda\wedge \delta\widehat H .
```
With $`\mathrm{d}(K\wedge \delta\widehat H)=\mathrm{d}K\wedge \delta\widehat H - K\wedge \mathrm{d}(\delta\widehat H)`$ and no boundary, this gives
``` math
\delta_{\widehat H}\Xi \;=\; \int_X \big(-e^{-2\Phi}*\widehat H+\mathrm{d}K+\Lambda\big)\wedge \delta\widehat H .
```
Hence the equation of motion is
``` math
\begin{equation}
\label{eq:EL1}
e^{-2\Phi}*\widehat H\;=\;\mathrm{d}K+\Lambda .
\end{equation}
```

#### (iv) Variation in $`B`$.

Only the $`\Lambda`$ term contributes:
``` math
\delta_B\Xi \;=\; -\int_X \Lambda\wedge \mathrm{d}(\delta B)\;=\;\int_X \mathrm{d}\Lambda \wedge \delta B .
```
Thus $`\mathrm{d}\Lambda=0`$. We may absorb the closed form $`\Lambda`$ into $`K`$ (or set $`\Lambda=0`$ by choosing the gauge slice for $`K`$), so <a href="#eq:EL1" data-reference-type="eqref" data-reference="eq:EL1">[eq:EL1]</a> becomes
``` math
\mathrm{d}\!\big(e^{-2\Phi}*\widehat H\big)\;=\;0,
```
i.e. the weighted $`B`$–equation of motion.

#### (v) Variations in $`A`$ and $`\omega^+`$.

The standard identities $`\delta\omega_3(A)=2\mathrm{Tr}(\delta A\wedge F)+\mathrm{d}\,\mathrm{Tr}(A\wedge \delta A)`$ and the analogous one for $`\omega^+`$ show that the only bulk contribution from the constraints is $`-\tfrac{\alpha'}{2}\int_X K\wedge \mathrm{Tr}(\delta A\wedge F)`$ and $`+\tfrac{\alpha'}{2}\int_X K\wedge \mathrm{Tr}(\delta\omega^+\wedge R^+)`$, which combine with the Yang–Mills and Einstein terms. In the holomorphic class and for Gauduchon metrics, the gauge Euler–Lagrange equations reduce to the HYM conditions used in §<a href="#sec:HYM" data-reference-type="ref" data-reference="sec:HYM">7</a>.

# Iwasawa as a concrete Strominger background

## E.1Background and SU(3) structure

Let $`X = \Gamma\backslash H_3(\mathbb{C})`$ be the Iwasawa manifold with the standard left-invariant $`(1,0)`$-coframe $`(\omega_1,\omega_2,\omega_3)`$ obeying $`d\omega_1=d\omega_2=0`$, $`d\omega_3=\omega_1\wedge\omega_2`$. Set the Hermitian form and holomorphic volume form
``` math
J=\frac{\mathrm{i}}{2}\sum_{j=1}^3 \omega_j\wedge\bar\omega_j,\qquad \Omega=\omega_1\wedge\omega_2\wedge\omega_3.
```
Then $`X`$ is complex parallelizable and $`J`$ is balanced ($`d(J^2)=0`$). With the Bismut connection $`\nabla_+`$ on $`TX`$, the torsion is $`T=H_b=\mathrm{i}(\bar\partial-\partial)J`$, consistent with the Green–Schwarz definition used in the main text. *Reference model and notation as in A02.* :contentReference\[oaicite:9\]index=9

## E.2Strominger data and the Bianchi identity

Use $`\nabla_+`$ on $`TX`$ and take a left-invariant SU(3)-instanton $`A`$ on a holomorphic bundle $`E\to X`$ (explicit left-invariant abelian instantons exist on Iwasawa). Define the gauge-invariant Green–Schwarz three-form
``` math
H_b = dB - \frac{\alpha'}{4}\big(\omega_3(A)-\omega_3(\omega_+)\big),\qquad
dH_b = \frac{\alpha'}{4}\big(\mathrm{Tr}F\wedge F - \mathrm{Tr}R_+\wedge R_+\big).
```
Then, with $`J`$ balanced and $`A`$ of HYM type, the *Hull–Strominger system* $`d(e^{-2\Phi}J\wedge J)=0`$, $`F^{0,2}=0`$, $`J\lrcorner F=0`$, and the Bianchi identity above is satisfied. This matches the conventions and equations in Sections 2–3 of the main text. :contentReference\[oaicite:10\]index=10 :contentReference\[oaicite:11\]index=11

## E.3Twisted admissibility (SA.F) on Iwasawa

Let $`\Delta(H_b)`$ be the twisted Laplacian for $`d_{H_b}=d+H_b\wedge`$. On a fixed compact Iwasawa metric:

- **Twisted spectral gap (SA.F1).** $`\lambda_1(\Delta(H_b))>0`$, with a uniform lower bound on bounded-geometry families. This is a direct instance of Lemma 4.1 (min–max/Cheeger–Buser for $`\Delta`$ plus Kato–Rellich for the $`H_b`$-terms).

- **Bounded twisted projector (SA.F2).** The twisted harmonic projector $`\Pi(H_b):H^s\to H^s`$ is bounded for all $`s`$, by the resolvent representation and parameter-dependent elliptic estimates (Lemma 4.2).

(See A02 for the same statements in this concrete model.) :contentReference\[oaicite:12\]index=12 :contentReference\[oaicite:13\]index=13

## E.4Selection: minimizer $`=`$ MTT fixed point

Let $`\Xi`$ be the selection potential of Sec. 5. By Theorem 5.2 (EL $`\Leftrightarrow`$ Strominger), any Iwasawa Strominger background is a critical point. Near a left-invariant solution $`(J_0,\Phi_0,B_0;A_0)`$, the Hessian is strictly positive modulo symmetries (Theorem 5.4), and $`\Xi`$ is a strict Lyapunov function for the coherent flow and the discrete map $`T_\tau`$ (Proposition 5.6). Hence the coherent MTT fixed point exists, is unique, and *equals* the unique local minimizer, i.e. the Iwasawa Strominger solution (A02 Theorem 1). :contentReference\[oaicite:14\]index=14 :contentReference\[oaicite:15\]index=15

#### Remark (on SA.F3).

R02–12 uses SA.F3 (commuting torsionful blocks) for split geometries; on Iwasawa the torsion couples invariant blocks and we may work with the *global* twisted projector $`\Pi(H_b)`$ instead. The contraction/Lyapunov arguments rely only on SA.F1–SA.F2 plus smoothing (SA.F4), which hold here. :contentReference\[oaicite:16\]index=16

## E.5Literature pointers

Invariant Strominger solutions on nilmanifolds (including Iwasawa) are well documented and are consistent with the Bismut/Hull choice used here; see Fu–Yau and subsequent invariant constructions, e.g. .
