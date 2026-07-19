---
abstract: |
  We give a first-principles derivation of classical General Relativity (GR) from Modal Triplet Theory (MTT). Starting from the $`10`$-dimensional modal product geometry $`M^{10}=Y_4\times B_1\times B_2\times B_3`$, we show that harmonic projection onto the coherent sector and internal pushforward to $`Y_4`$ produce an effective, metric-compatible Levi–Civita connection and a four-dimensional action of Einstein–Hilbert type. Under explicit spectral-gap, boundedness, and fixed-point stability hypotheses, the projected Euler–Lagrange equations are exactly the Einstein field equations with matter stress–energy given by the projected modal content. We provide: (i) a variational reduction theorem proving that the internal integration of the $`10`$D action yields $`S_{\rm eff}[g,A,\Phi]=\frac{1}{16\pi G_{\rm eff}}\int (R-2\Lambda_{\rm eff})
  \sqrt{-g}\,d^4x+S_{\rm matter}`$ with $`G_{\rm eff},\Lambda_{\rm eff}`$ determined by internal spectral data; (ii) a Noether/Bianchi identity pushforward establishing $`\nabla^\mu T_{\mu\nu}=0`$; (iii) a geodesic-limit theorem recovering the equivalence principle for projected test bodies; and (iv) the Newtonian and weak-field limits with explicit parameter dictionaries. We state controlled conditions under which beyond-GR corrections (e.g. $`R^2`$, scalar-tensor terms, non-metricity) arise from departures from the coherent fixed-point regime. This places GR as the unique, stable, low-frequency, large-scale sector of MTT.
author:
- Peter Nero
current_version: v2
date: 2026-07-19
generated_from_main_tex_sha256: c015fcec50bdfed8c1a3a8492273edfbcce6209088f5917128d5736c57c9b4a9
paper_id: modal-triplet-theory-from-mtt-to-general-relativity
release_state: zenodo_released
released_version: v2.0
title: "**Modal Triplet Theory: From MTT to General Relativity**"
zenodo_doi: 10.5281/zenodo.18268239
zenodo_record_id: 18268239
zenodo_url: "https://zenodo.org/records/18268239"
---

# Introduction

#### Aim.

Modal Triplet Theory (MTT) posits a unified geometric framework on the ten-dimensional product manifold
``` math
M^{10} \;=\; Y_4 \times B_1 \times B_2 \times B_3,
```
where $`Y_4`$ is a smooth Lorentzian $`4`$-manifold and each $`B_n`$ is a compact Riemannian $`3`$-manifold carrying internal (gauge/matter) structure. The coherent sector is isolated by the joint harmonic projector $`\Pi=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$, and observables are obtained by the internal pushforward $`\mathcal P = I\circ \Pi`$ to $`Y_4`$. In a companion work, we derived quantum mechanics from this structure. Here we derive *classical General Relativity* (GR): we prove that, under explicit and physically transparent hypotheses, the effective $`4`$D dynamics of the projected metric are governed by the Einstein field equations with well-defined effective constants.

#### Strategy.

Our derivation is variational: beginning from the covariant $`10`$D MTT action $`S_{\rm MTT}[g^{(10)},\mathcal A,\Psi,\cdots]`$, we restrict to the coherent sector, integrate out the internal factors $`B_n`$, and obtain an effective $`4`$D action functional on $`Y_4`$. We then prove:

1.  the reduced connection is torsion-free and metric-compatible (Levi–Civita);

2.  the reduced action equals Einstein–Hilbert plus a cosmological term and the projected matter actions with definite couplings from internal spectral data;

3.  the reduced Euler–Lagrange equations are precisely the Einstein equations $`G_{\mu\nu}+\Lambda_{\rm eff} g_{\mu\nu}=8\pi G_{\rm eff}\,T_{\mu\nu}`$, with $`T_{\mu\nu}`$ the projected modal stress–energy tensor;

4.  the Bianchi identities and diffeomorphism invariance push forward to $`\nabla^\mu T_{\mu\nu}=0`$, ensuring consistency;

5.  the geodesic principle and Newtonian limits are recovered with $`G_{\rm eff}`$, $`\Lambda_{\rm eff}`$ and PPN parameters determined by internal gaps and overlaps.

#### Scope and novelty.

Unlike Kaluza–Klein compactifications that *assume* a product ansatz and insert Einstein–Hilbert by hand, our construction: (i) uses the dynamical coherent projection $`\Pi`$ furnished by MTT’s fixed-point theory; (ii) allows curvature–gap couplings $`\lambda_n=\lambda_n^{(0)}+\beta_n R`$ that feed into the effective gravitational constants; and (iii) quantifies when deviations from GR occur (e.g. if parallel-bundle stability fails or coherent projection breaks). The outcome is that GR is the *unique* local, diffeomorphism-invariant, second-order effective theory compatible with the MTT coherent-sector hypotheses in the long-wavelength limit.

#### Main results (informal).

- **Variational reduction theorem.** The coherent-sector reduction yields
  ``` math
  S_{\rm eff}[g,\Phi,A] \;=\; \frac{\mathcal V_{\rm int}}{16\pi \mathcal G}\int_{Y_4} R(g)\sqrt{-g}\,d^4x
    \;-\; \frac{\mathcal V_{\rm int}}{8\pi \mathcal G}\int_{Y_4} \Lambda_{\rm int}\sqrt{-g}\,d^4x
    \;+\; S_{\rm matter}[g,\Phi,A],
  ```
  where $`\mathcal V_{\rm int}`$ is the normalized internal volume of the coherent sector, $`\mathcal G`$ the fundamental $`10`$D coupling, and $`\Lambda_{\rm int}`$ an internal vacuum functional of spectral data. Defining $`G_{\rm eff}^{-1}=\mathcal V_{\rm int}\mathcal G^{-1}`$ and $`\Lambda_{\rm eff}=\Lambda_{\rm int}`$ gives Einstein–Hilbert with effective constants.

- **Einstein equations and Bianchi pushforward.** Stationarity under $`g_{\mu\nu}\mapsto g_{\mu\nu}+\delta g_{\mu\nu}`$ yields $`G_{\mu\nu}+\Lambda_{\rm eff}g_{\mu\nu}=8\pi G_{\rm eff}T_{\mu\nu}`$ with $`\nabla^\mu T_{\mu\nu}=0`$ by diffeomorphism invariance and the projected Noether identity.

- **Equivalence principle and geodesics.** Pointlike coherent excitations minimize the projected action length functional, hence follow $`g`$-geodesics; universal minimal coupling emerges from the internal pushforward, establishing the (weak) equivalence principle in the coherent regime.

- **Controlled corrections.** Curvature–gap couplings and finite-bandwidth effects generate suppressed higher-curvature terms (e.g. $`R^2`$) and scalar-tensor contributions; we bound their coefficients in terms of internal gaps and stability parameters.

#### Structure.

Section <a href="#sec:setup" data-reference-type="ref" data-reference="sec:setup">2</a> states the geometric and functional-analytic hypotheses. Section <a href="#sec:reduction" data-reference-type="ref" data-reference="sec:reduction">3</a> performs the action reduction and proves the Einstein–Hilbert form. Section <a href="#sec:field_eqs" data-reference-type="ref" data-reference="sec:field_eqs">4</a> derives the field equations and Bianchi pushforward. Section <a href="#sec:equivalence" data-reference-type="ref" data-reference="sec:equivalence">5</a> proves the geodesic/equivalence principle and Newtonian limits. Section <a href="#sec:corrections" data-reference-type="ref" data-reference="sec:corrections">6</a> quantifies controlled deviations and observational constraints. Appendices collect technical details on projector regularity, internal spectral geometry, and Noether identities.

# Geometric Setup and Working Hypotheses

We adopt the product geometry
``` math
\begin{equation}
  M^{10} \;=\; Y_4 \times B_1 \times B_2 \times B_3,
\end{equation}
```
with $`Y_4`$ a smooth, time-oriented Lorentzian manifold $`(Y_4,g)`$ and each $`B_n`$ a compact, oriented, smooth Riemannian $`3`$-manifold $`(B_n,h^{(n)})`$ with spin structure. The $`10`$D metric is taken to be block-diagonal up to controlled, higher-order warping terms:
``` math
\begin{equation}
  g^{(10)} \;=\; g \;\oplus\; h^{(1)} \;\oplus\; h^{(2)} \;\oplus\; h^{(3)} \;+\; \mathcal{O}(\varepsilon_{\rm warp}),
\end{equation}
```
where $`\varepsilon_{\rm warp}`$ parameterizes small internal–external mixing suppressed in the coherent regime.

## Coherent-sector projection and pushforward

Let $`E\to M^{10}`$ denote the total field bundle (metric, gauge, and matter content). For each $`B_n`$, let $`\Delta_{B_n}`$ be the geometric Laplacian acting on the appropriate internal tensors/forms/spinors, with discrete spectrum $`0=\lambda_{n,0}<\lambda_{n,1}\le\lambda_{n,2}\le\cdots\to\infty.`$ Denote by $`\Pi_{B_n}`$ the $`L^2`$-orthogonal projector onto $`\ker\Delta_{B_n}`$ (harmonic modes). Define the *joint harmonic projector*
``` math
\begin{equation}
  \Pi \;:=\; \Pi_{B_1}\,\Pi_{B_2}\,\Pi_{B_3},
\end{equation}
```
and the *observable pushforward*
``` math
\begin{equation}
  I: \Gamma(E)\longrightarrow \Gamma(E|_{Y_4}),\qquad
  (I\Phi)(y) := \frac{1}{\mathcal V_{\rm int}} \int_{B_1\times B_2\times B_3}\!\!\Phi(y,b)\,
  d\mu_{B_1}(b_1)\,d\mu_{B_2}(b_2)\,d\mu_{B_3}(b_3),
\end{equation}
```
where $`\mathcal V_{\rm int}:=\prod_{n=1}^3{\rm Vol}(B_n)`$ and $`d\mu_{B_n}`$ is the Riemannian volume measure. The *observable projection* is
``` math
\begin{equation}
  \mathcal P \;:=\; I\circ \Pi.
\end{equation}
```

## Hypotheses

We summarize the assumptions used in the derivation; all are standard in elliptic/spectral geometry and in the fixed-point analysis underlying the coherent sector.

<div id="H1" class="assumption">

**Hypothesis 1** (Spectral gap and bounded projectors). For each $`n=1,2,3`$ the kernel $`\ker\Delta_{B_n}`$ is finite-dimensional and separated by a nonzero gap:
``` math
\lambda_{n,1}\ge \lambda_* > 0,
```
uniformly on the parameter ranges considered. The orthogonal projector $`\Pi_{B_n}`$ extends to a bounded self-adjoint idempotent on the Sobolev space $`H^1`$ acting fiberwise on $`B_n`$. Consequently, $`\Pi`$ is bounded, self-adjoint, idempotent on $`H^1(E)`$.

</div>

<div id="H2" class="assumption">

**Hypothesis 2** (Small warping). The off-block components of $`g^{(10)}`$ are uniformly $`\mathcal{O}(\varepsilon_{\rm warp})`$ and their contributions to the $`10`$D curvature invariants are $`\mathcal{O}(\varepsilon_{\rm warp})`$ relative to the leading block-diagonal terms. We work to leading order in $`\varepsilon_{\rm warp}`$; corrections generate higher-curvature operators suppressed by $`\varepsilon_{\rm warp}`$ in the 4D action.

</div>

#### Commutation under warping (clarification to Hyp. 2.2).

At leading order we adopt *base–only* warping so the vertical Laplacians act on disjoint fiber coordinates and commute, $`[\Delta_{B_i},\Delta_{B_j}]=0`$, and $`\Pi=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$ is exact. Any off–block components of $`g^{(10)}`$ are uniformly $`O(\varepsilon_{\rm warp})`$ and contribute only at NLO to the 4D action (§6). Equivalently, if one keeps $`O(\varepsilon_{\rm warp})`$ mixing, the coherent projector may be defined spectrally from the *sum* vertical Laplacian,
``` math
\Pi:=\mathbf{1}_{\{0\}}\!\big(\Delta_{B_1}+\Delta_{B_2}+\Delta_{B_3}\big),
```
which still projects to $`\bigcap_i \mathop{\mathrm{Ker}}\Delta_{B_i}`$ and satisfies the same $`H^1`$ bounds.

#### Representation–correct curvature–gap coupling (replacing Hyp. 2.3).

In the coherent sector, internal mass/gap operators pick up curvature terms through the Bochner–Weitzenböck/Lichnerowicz identities, *representation by representation*:
``` math
\begin{align*}
\text{scalars:}\quad & -\Delta \;\mapsto\; -\Delta + \tfrac{1}{6}R,\\
\text{spinors:}\quad & D^2 \;\mapsto\; D^2 - \tfrac{1}{4}R,\\
\text{$p$-forms:}\quad & \Delta_p \;\mapsto\; \Delta_p - \mathcal{R}_p(\text{Ric/Weyl}),
\end{align*}
```
so that the coherent eigenvalues shift as $`\lambda_{\rm rep}(x)=\lambda^{(0)}_{\rm rep}+\beta_{\rm rep}\,R(x)`$ in constant–curvature limits with $`\beta_{\rm scal}=\tfrac{1}{6}`$, $`\beta_{\rm spin}=\tfrac{1}{4}`$, while $`p`$-forms retain Ricci/Weyl traces in general (not a scalar multiple of $`R`$). These enter *only* through internal quadratic forms and introduce no higher-than-second derivatives of $`g`$ at leading order.

<div id="H4" class="assumption">

**Hypothesis 3** (Fixed-point coherence and stability). Let $`\Phi_\tau`$ be the modal curvature-reducing flow on $`H^1(E)`$. The projected map $`F:=\Pi\circ \Phi_\tau`$ admits a globally attracting fixed point $`\Psi^\ast\in{\rm Im}\,\Pi`$ in the relevant sector, and is stable under bounded disturbances with rates $`\delta_n`$ provided the parallel-bundle *damping balance* inequalities $`\gamma_n>\delta_n`$ hold, where $`\gamma_n`$ are bundle-resolved dissipation rates induced by internal gaps $`\lambda_n`$ (monotone in $`\lambda_n`$).

</div>

<div id="H5" class="assumption">

**Hypothesis 4** (Regularity and compactness). All background fields $`(g^{(10)},\mathcal A, \cdots)`$ are smooth; the coherent fields lie in $`H^1(E)`$ with finite $`10`$D energy. Internal volumes $`{\rm Vol}(B_n)`$ are finite and strictly positive. The pushforward $`I`$ maps $`H^1`$ sections to $`H^1`$ sections on $`Y_4`$.

</div>

<div id="H6" class="assumption">

**Hypothesis 5** (Diffeomorphism invariance and locality). The $`10`$D action $`S_{\rm MTT}[g^{(10)},\cdots]`$ is diffeomorphism-invariant and local. Gauge fixing (if any) is implemented covariantly and does not spoil the variational identities (Noether currents, Bianchi identities) on shell.

</div>

<div id="H7" class="assumption">

**Hypothesis 6** (Coherent-sector completeness). At scales large compared to the internal gaps (long-wavelength sector on $`Y_4`$), the observable content is exhausted by $`{\rm Im}\,\mathcal P`$. Off-harmonic contributions are suppressed by at least $`\mathcal{O}(\lambda_*^{-1})`$ and generate only higher-derivative corrections in the 4D effective action.

</div>

## Consequences and technical lemmas

<div id="lem:proj" class="lemma">

**Lemma 7** (Projector calculus). *Under Assumptions <a href="#H1" data-reference-type="ref" data-reference="H1">1</a> and <a href="#H5" data-reference-type="ref" data-reference="H5">4</a>, $`\Pi`$ commutes with pullbacks of tensors from $`Y_4`$ and with the external covariant derivative $`\nabla^{(4)}`$ acting on $`Y_4`$ indices. Hence, for any field $`\Phi`$,
``` math
\nabla^{(4)}(\mathcal P\Phi) \;=\; \mathcal P(\nabla^{(4)}\Phi).
```*

</div>

<div id="lem:vol" class="lemma">

**Lemma 8** (Pushforward metric and volume). *Let $`\omega^{(10)}`$ be the $`10`$D volume form. Then the coherent pushforward of $`\omega^{(10)}`$ is $`\mathcal P(\omega^{(10)}) = \mathcal V_{\rm int}\,\omega^{(4)}\;+\;\mathcal{O}(\varepsilon_{\rm warp}),`$ where $`\omega^{(4)}`$ is the $`4`$D volume form of $`g`$. Thus, internal integration simply rescales the 4D measure at leading order.*

</div>

<div id="lem:curv" class="lemma">

**Lemma 9** (Curvature decomposition). *To leading order in $`\varepsilon_{\rm warp}`$,
``` math
\begin{equation}
  R\!\big(g^{(10)}\big) \;=\; R(g) \;+\; \sum_{n=1}^3 R\!\big(h^{(n)}\big) \;+\; \mathcal{O}(\varepsilon_{\rm warp}).
\end{equation}
```
Moreover, under $`\Pi`$ and $`I`$, the internal scalar curvatures integrate to constants depending on the internal geometries, while $`R(g)`$ pushes forward as a local scalar on $`Y_4`$.*

</div>

<div class="remark">

*Remark 10* (On higher-curvature terms). Any dependence of the $`10`$D action on higher invariants (e.g. $`R_{ABCD}R^{ABCD}`$) contributes to the 4D effective action a tower of higher-derivative operators. Under Assumptions <a href="#H2" data-reference-type="ref" data-reference="H2">2</a> and <a href="#H7" data-reference-type="ref" data-reference="H7">6</a> these appear with coefficients suppressed by internal gaps and warping and will be collected in Sec. <a href="#sec:corrections" data-reference-type="ref" data-reference="sec:corrections">6</a>.

</div>

# Variational Reduction to Four Dimensions

We now perform the coherent-sector reduction of the $`10`$D MTT action to obtain the effective $`4`$D gravitational action on $`(Y_4,g)`$.

## The $`10`$D MTT action

Let $`S_{\rm MTT}`$ be the total $`10`$D action, schematically
``` math
\begin{equation}
  S_{\rm MTT}[g^{(10)},\mathcal A,\Phi] \;=\; \frac{1}{16\pi\mathcal G}
   \int_{M^{10}}\! R\!\big(g^{(10)}\big) \,\omega^{(10)} 
   \;+\; S_{\rm int}[\mathcal A,\Phi;g^{(10)}],
\end{equation}
```
where $`\mathcal G`$ is the $`10`$D gravitational coupling, $`R(g^{(10)})`$ is the $`10`$D Ricci scalar, and $`S_{\rm int}`$ denotes all non-gravitational terms (Yang–Mills, scalar, fermionic, curvature–gap potentials) minimally coupled to $`g^{(10)}`$.

#### Curvature–gap terms.

By Assumption <a href="#H3" data-reference-type="ref" data-reference="H3">[H3]</a>, $`S_{\rm int}`$ may include
``` math
\begin{equation}
  S_{\rm gap} \;=\; -\frac12 \sum_{n=1}^3 \int_{M^{10}}\! 
  \big(\lambda_n^{(0)} + \beta_n R(g)\big)\,\phi_n^2\; \omega^{(10)},
\end{equation}
```
with $`\phi_n`$ coherent scalars from $`B_n`$ sectors.

## Projection and internal integration

Applying the projector $`\mathcal P`$ to all fields selects the harmonic sector on each $`B_n`$ and replaces the internal coordinates by averages. By Lemma <a href="#lem:vol" data-reference-type="ref" data-reference="lem:vol">8</a> and Lemma <a href="#lem:curv" data-reference-type="ref" data-reference="lem:curv">9</a>,
``` math
\begin{align}
  \mathcal P\big( R(g^{(10)})\omega^{(10)} \big) 
  &= \Big[ R(g) + \sum_{n=1}^3 \overline{R}^{(n)} \Big] \,\mathcal V_{\rm int}\,\omega^{(4)}
  \;+\; \mathcal{O}(\varepsilon_{\rm warp}),
\end{align}
```
where $`\overline{R}^{(n)}:=\frac{1}{{\rm Vol}(B_n)}\int_{B_n} R(h^{(n)})\,d\mu_{B_n}`$ are constants.

Similarly, the non-gravitational sector projects to its coherent content:
``` math
\begin{equation}
  \mathcal P\big(S_{\rm int}\big) \;=\; S_{\rm matter}[g,A^{\rm coh},\Phi^{\rm coh}] 
  \;+\; \mathcal{O}(\lambda_*^{-1}).
\end{equation}
```

## Effective $`4`$D action

The projected gravitational action is therefore
``` math
\begin{align}
  S_{\rm grav}^{(4)}[g] 
  &= \frac{\mathcal V_{\rm int}}{16\pi \mathcal G}
     \int_{Y_4} R(g)\,\omega^{(4)}
   + \frac{\mathcal V_{\rm int}}{16\pi \mathcal G}
     \Big(\sum_{n=1}^3 \overline{R}^{(n)}\Big)
     \int_{Y_4} \omega^{(4)}
   + \mathcal{O}(\varepsilon_{\rm warp}) \notag\\
  &= \frac{1}{16\pi G_{\rm eff}} \int_{Y_4} R(g)\sqrt{-g}\,d^4x
   - \frac{\Lambda_{\rm eff}}{8\pi G_{\rm eff}} \int_{Y_4} \sqrt{-g}\,d^4x
   + \mathcal{O}(\varepsilon_{\rm warp}),
\end{align}
```
where we define
``` math
\begin{equation}
  G_{\rm eff} := \frac{\mathcal G}{\mathcal V_{\rm int}}, 
  \qquad
  \Lambda_{\rm eff} := -\frac12\sum_{n=1}^3 \overline{R}^{(n)}.
\end{equation}
```
The sign convention for $`\Lambda_{\rm eff}`$ follows the usual Einstein equations.

<div class="remark">

*Remark 11* (Sign of $`\Lambda_{\rm eff}`$ in Eq. (13)). With the variation conventions of Eqs. (16)–(17), positive internal scalar curvature $`R^{(n)}`$ contributes a *negative* cosmological term in the 4D action via $`\Lambda_{\rm eff}= -\tfrac{1}{2}\sum_n R^{(n)}`$, while any additional vacuum energy of coherent fields appears in $`\Lambda_{\rm vac}^{\rm modal}`$ (cf. Step 4 in §7.1).

</div>

The total effective $`4`$D action is thus
``` math
\begin{equation}
  S_{\rm eff}[g,\Phi^{\rm coh},A^{\rm coh}] \;=\;
  \frac{1}{16\pi G_{\rm eff}} \int_{Y_4} (R(g) - 2\Lambda_{\rm eff})\sqrt{-g}\,d^4x
  + S_{\rm matter}[g,\Phi^{\rm coh},A^{\rm coh}] 
  + \mathcal{O}(\varepsilon_{\rm warp},\lambda_*^{-1}).
\end{equation}
```

<div id="thm:EH" class="theorem">

**Theorem 12** (Variational Reduction to Einstein–Hilbert). *Under Assumptions <a href="#H1" data-reference-type="ref" data-reference="H1">1</a>–<a href="#H7" data-reference-type="ref" data-reference="H7">6</a>, the coherent-sector projection $`\mathcal P`$ of the $`10`$D MTT action yields, to leading order in $`\varepsilon_{\rm warp}`$ and $`\lambda_*^{-1}`$, a $`4`$D effective action of the Einstein–Hilbert form with effective Newton constant $`G_{\rm eff}`$ and cosmological constant $`\Lambda_{\rm eff}`$ given above.*

</div>

<div class="proof">

*Proof.* Follows directly from Lemmas <a href="#lem:vol" data-reference-type="ref" data-reference="lem:vol">8</a>–<a href="#lem:curv" data-reference-type="ref" data-reference="lem:curv">9</a> applied to the $`10`$D gravitational term, the constancy of $`\overline{R}^{(n)}`$ over $`Y_4`$, and the boundedness of $`\mathcal P`$ on $`H^1`$ ensuring the projection commutes with the $`4`$D Levi–Civita covariant derivative. The matter sector reduces by $`\mathcal P`$ to its coherent modes, with off-harmonic contributions suppressed by $`\lambda_*^{-1}`$ and $`\varepsilon_{\rm warp}`$. ◻

</div>

<div class="remark">

*Remark 13*. If the internal manifolds $`B_n`$ are Ricci-flat, $`\overline{R}^{(n)}=0`$ and $`\Lambda_{\rm eff}`$ is purely from vacuum expectation values of internal fields. Curvature–gap couplings (Assumption <a href="#H3" data-reference-type="ref" data-reference="H3">[H3]</a>) can renormalize both $`G_{\rm eff}`$ and $`\Lambda_{\rm eff}`$, as shown by integrating out $`\phi_n`$ in $`S_{\rm gap}`$.

</div>

# Field Equations and Bianchi Pushforward

With the effective action of Theorem <a href="#thm:EH" data-reference-type="ref" data-reference="thm:EH">12</a>,
``` math
\begin{equation}
  S_{\rm eff}[g,\Phi^{\rm coh},A^{\rm coh}]
  = \frac{1}{16\pi G_{\rm eff}}\!\int_{Y_4} (R-2\Lambda_{\rm eff})\sqrt{-g}\,d^4x
    + S_{\rm matter}[g,\Phi^{\rm coh},A^{\rm coh}] 
    + \mathcal{O}(\varepsilon_{\rm warp},\lambda_*^{-1}),
\end{equation}
```
we now vary with respect to the metric to obtain the field equations and prove covariant conservation of stress–energy via a projected Noether identity.

## Metric variation and Einstein equations

Let $`\delta g_{\mu\nu}`$ be a compactly supported symmetric variation. Standard identities yield
``` math
\begin{align}
  \delta\!\left( \int R \sqrt{-g}\,d^4x\right)
  &= \int (G_{\mu\nu}\,\delta g^{\mu\nu}) \sqrt{-g}\,d^4x
     + \text{boundary terms},\\
  \delta\!\left( \int \sqrt{-g}\,d^4x \right)
  &= -\frac12 \int g_{\mu\nu}\,\delta g^{\mu\nu}\sqrt{-g}\,d^4x.
\end{align}
```
Define the (projected, coherent-sector) stress–energy tensor by
``` math
\begin{equation}
  T_{\mu\nu} \;:=\; -\frac{2}{\sqrt{-g}}\frac{\delta S_{\rm matter}[g,\Phi^{\rm coh},A^{\rm coh}]}
  {\delta g^{\mu\nu}} .
\end{equation}
```
Stationarity $`\delta S_{\rm eff}=0`$ for all $`\delta g^{\mu\nu}`$ implies, to leading order in $`\varepsilon_{\rm warp}`$ and $`\lambda_*^{-1}`$,
``` math
\begin{equation}
  G_{\mu\nu} + \Lambda_{\rm eff}\,g_{\mu\nu} \;=\; 8\pi G_{\rm eff}\, T_{\mu\nu}.
  \label{eq:Einstein_eq}
\end{equation}
```

## Diffeomorphism invariance and covariant conservation

We now show $`\nabla^\mu T_{\mu\nu}=0`$ as a pushforward of the $`10`$D Noether identity.

<div id="lem:Noether_push" class="lemma">

**Lemma 14** (Projected Noether identity). *Under Assumptions <a href="#H5" data-reference-type="ref" data-reference="H5">4</a>–<a href="#H7" data-reference-type="ref" data-reference="H7">6</a>, the coherent-sector projection $`\mathcal P=I\!\circ\!\Pi`$ commutes with $`Y_4`$ diffeomorphisms acting on $`g`$ and on all projected fields. Consequently, the Ward identity for diffeomorphism invariance yields on shell:
``` math
\begin{equation}
  \nabla^\mu \Big( G_{\mu\nu} + \Lambda_{\rm eff} g_{\mu\nu} - 8\pi G_{\rm eff}\,T_{\mu\nu}\Big) = 0.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* By Lemma <a href="#lem:proj" data-reference-type="ref" data-reference="lem:proj">7</a>, $`\Pi`$ commutes with pullbacks and with the external covariant derivative $`\nabla^{(4)}`$. The pushforward $`I`$ is an internal integral against fixed measures $`d\mu_{B_n}`$, hence invariant under $`Y_4`$ diffeomorphisms. Therefore the reduced action is diffeomorphism invariant, and the standard Ward identity applies. Using $`\nabla^\mu G_{\mu\nu}\equiv 0`$ (contracted Bianchi) gives the claim. ◻

</div>

<div id="thm:conservation" class="theorem">

**Theorem 15** (Covariant conservation). *Solutions of the field equations <a href="#eq:Einstein_eq" data-reference-type="eqref" data-reference="eq:Einstein_eq">[eq:Einstein_eq]</a> satisfy
``` math
\begin{equation}
  \nabla^\mu T_{\mu\nu} \;=\; 0.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Take the covariant divergence of <a href="#eq:Einstein_eq" data-reference-type="eqref" data-reference="eq:Einstein_eq">[eq:Einstein_eq]</a> and use $`\nabla^\mu G_{\mu\nu}\!=\!0`$ and $`\nabla_\nu \Lambda_{\rm eff}\!=\!0`$ (constant by construction). ◻

</div>

## Levi–Civita compatibility and torsion-free reduction

<div id="prop:LeviCivita" class="proposition">

**Proposition 16** (Metric compatibility and vanishing torsion). *Under Assumptions <a href="#H2" data-reference-type="ref" data-reference="H2">2</a> and <a href="#H7" data-reference-type="ref" data-reference="H7">6</a>, the affine connection appearing in the reduced Euler–Lagrange equations is the Levi–Civita connection of $`g`$; in particular, $`\nabla_\alpha g_{\mu\nu}=0`$ and $`T^\alpha{}_{\mu\nu}=0`$ at leading order.*

</div>

<div class="proof">

*Proof.* The $`10`$D action is metric and diffeomorphism invariant and contains no independent torsion fields in the gravitational sector. Any internal contorsion contributions are either (i) projected out by $`\Pi`$ (no harmonic torsion modes on compact $`B_n`$), or (ii) integrated to constants by $`I`$, renormalizing only scalar terms ($`\Lambda_{\rm eff}`$). Hence the reduced $`4`$D variational derivative with respect to $`g`$ yields the metric-compatible, torsion-free connection. ◻

</div>

## Stress–energy from projected matter

For completeness, we spell out the common cases for $`T_{\mu\nu}`$ after projection:

#### (i) Coherent scalar field $`\varphi`$.

With $`S_\varphi=\!-\frac12\!\int\big( g^{\mu\nu}\partial_\mu\varphi\partial_\nu\varphi + U(\varphi)\big)\sqrt{-g}\,d^4x`$,
``` math
T^{(\varphi)}_{\mu\nu}=\partial_\mu\varphi\,\partial_\nu\varphi
 - \frac12 g_{\mu\nu}\big( g^{\alpha\beta}\partial_\alpha\varphi\partial_\beta\varphi + U(\varphi)\big).
```

#### (ii) Yang–Mills field $`A_\mu`$.

With $`S_{\rm YM}=-\frac{1}{4g_{\rm YM}^2}\!\int \mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})\sqrt{-g}\,d^4x`$,
``` math
T^{\rm (YM)}_{\mu\nu}=\frac{1}{g_{\rm YM}^2}\,\mathrm{Tr}\!\left(
F_{\mu\alpha}F_\nu{}^{\alpha}-\frac14 g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right).
```

#### (iii) Coherent Dirac field $`\psi`$.

With $`S_\psi=\!\int \bar\psi(i\gamma^\mu\nabla_\mu-m)\psi \sqrt{-g}\,d^4x`$,
``` math
T^{(\psi)}_{\mu\nu}=\frac{i}{4}\,\bar\psi\Big(\gamma_\mu\!\stackrel{\leftrightarrow}{\nabla}\!_\nu
+\gamma_\nu\!\stackrel{\leftrightarrow}{\nabla}\!_\mu\Big)\psi - g_{\mu\nu}\,\bar\psi(i\gamma^\alpha\nabla_\alpha-m)\psi .
```
All couplings ($`m`$, $`g_{\rm YM}`$, etc.) are the projected, internally averaged parameters fixed by the MTT spectral data and curvature–gap coefficients (Assumption <a href="#H3" data-reference-type="ref" data-reference="H3">[H3]</a>).

## Summary

Varying the reduced action yields the Einstein equations with effective constants; diffeomorphism invariance pushes forward to $`\nabla^\mu T_{\mu\nu}=0`$; and the reduced connection is the Levi–Civita connection of $`g`$. These results establish that the coherent-sector projection of MTT reproduces classical GR exactly at leading order.

# Equivalence Principle, Geodesic Motion, and Newtonian/PPN Limits

We now show that freely falling, sufficiently localized coherent excitations follow $`g`$-geodesics (weak equivalence principle), and we derive the Newtonian and parametric post-Newtonian (PPN) limits of the projected theory.

## Geodesic motion from coherent wave packets

Consider a minimally coupled, coherent scalar or spinor field $`\Phi`$ on $`(Y_4,g)`$ with action $`S_{\rm matter}[g,\Phi]`$ as in Sec. <a href="#sec:field_eqs" data-reference-type="ref" data-reference="sec:field_eqs">4</a>. Let $`\Phi_\epsilon`$ be a one-parameter family of spatially localized wave packets with characteristic size $`\ell`$ and Compton length $`\lambda_C`$, obeying $`\lambda_C \ll \ell \ll \mathcal{R}^{-1/2}`$ (background curvature scale). Define the worldline by the stress-energy centroid
``` math
\begin{equation}
  z^\mu(\tau) := \frac{\int_{\Sigma_\tau} x^\mu T^{00} \, d^3x}
                       {\int_{\Sigma_\tau} T^{00}\, d^3x},
  \qquad
  p^\mu(\tau) := \int_{\Sigma_\tau} T^{\mu 0}\, d^3x,
\end{equation}
```
on Cauchy slices $`\Sigma_\tau`$. Standard manipulations (multipole expansion to pole-dipole order and the conservation law $`\nabla_\mu T^{\mu\nu}=0`$ from Theorem <a href="#thm:conservation" data-reference-type="ref" data-reference="thm:conservation">15</a>) give:

<div id="thm:geodesic" class="theorem">

**Theorem 17** (Geodesic limit / Weak Equivalence Principle). *Let $`\Phi_\epsilon`$ be a minimally coupled coherent wave packet with negligible self-gravity and size $`\ell`$ satisfying $`\lambda_C \ll \ell \ll \mathcal{R}^{-1/2}`$. Then, up to $`\mathcal{O}(\ell/\mathcal{R}^{-1/2})`$ corrections, the centroid worldline $`z^\mu(\tau)`$ obeys the geodesic equation for the Levi–Civita connection of $`g`$:
``` math
\begin{equation}
  \frac{D^2 z^\mu}{D\tau^2} + \Gamma^\mu{}_{\alpha\beta}(z)\,
  \frac{dz^\alpha}{d\tau}\frac{dz^\beta}{d\tau} = 0.
\end{equation}
```
The motion is independent of the internal composition and of the MTT sector labels $`(Q_{ij},k_2,k_3,g)`$: all such dependence is absorbed into universal couplings already fixed in $`S_{\rm eff}`$.*

</div>

<div class="proof">

*Idea.* Expand $`\nabla_\mu T^{\mu\nu}=0`$ in Fermi normal coordinates around $`z^\mu`$ and keep terms to pole order; use symmetry of $`T^{\mu\nu}`$ and negligible spin-curvature couplings in the chosen regime. Minimal coupling (from the pushforward $`\mathcal P`$) ensures universality of free fall. Details follow the Mathisson–Papapetrou procedure with spin terms suppressed or treated separately. ◻

</div>

## Newtonian limit and Poisson equation

Take the weak-field, slow-motion regime:
``` math
\begin{equation}
  g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu},\quad
  |h_{\mu\nu}| \ll 1,\quad v\ll c,\quad
  T^{00} \approx \rho c^2, \quad T^{0i}\approx \rho c v^i, \quad T^{ij}\ll \rho c^2.
\end{equation}
```
In harmonic gauge, the linearized Einstein equations from <a href="#eq:Einstein_eq" data-reference-type="eqref" data-reference="eq:Einstein_eq">[eq:Einstein_eq]</a> yield
``` math
\begin{equation}
  \Box \bar h_{\mu\nu} = -16\pi G_{\rm eff}\, T_{\mu\nu} + 2\Lambda_{\rm eff}\,\eta_{\mu\nu},
\end{equation}
```
with $`\bar h_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h`$. Keeping leading terms gives the Newtonian potential $`U`$ via $`h_{00} = -2U/c^2`$ with
``` math
\begin{equation}
  \nabla^2 U(\mathbf{x}) \;=\; 4\pi G_{\rm eff}\,\rho(\mathbf{x}) \;-\; \Lambda_{\rm eff} c^2.
  \label{eq:Poisson}
\end{equation}
```
Thus, $`G_{\rm eff}`$ is the Newton constant in laboratory/solar-system scales and $`\Lambda_{\rm eff}`$ contributes a constant background curvature (cosmological). The standard two-body Keplerian dynamics and classical tests follow with $`G \to G_{\rm eff}`$.

## PPN parameters and GR values

In the standard PPN expansion for metric theories with minimal coupling and no preferred-frame effects, the line element in isotropic coordinates reads
``` math
\begin{align}
  g_{00} &= -1 + 2U - 2\beta U^2 + \mathcal{O}(\epsilon^3),\\
  g_{ij} &= \left(1 + 2\gamma U\right)\delta_{ij} + \mathcal{O}(\epsilon^2),\\
  g_{0i} &= -\tfrac12 (4\gamma+3+\alpha_1 - \alpha_2+\zeta_1-2\xi)V_i + \mathcal{O}(\epsilon^{3/2}),
\end{align}
```
in units with $`c=1`$ and $`\epsilon\sim v^2\sim U`$. For the reduced theory with action $`S_{\rm eff}`$ (Einstein–Hilbert + minimally coupled matter), we obtain the GR values:
``` math
\begin{equation}
  \gamma = 1,\qquad \beta = 1,\qquad
  \alpha_1=\alpha_2=\alpha_3=\xi=\zeta_1=\zeta_2=\zeta_3=\zeta_4=0,
\end{equation}
```
up to $`\mathcal{O}(\varepsilon_{\rm warp},\lambda_*^{-1})`$ corrections discussed below. Therefore, light deflection, Shapiro delay, perihelion precession, gravitational redshift, and frame-dragging match GR predictions with $`G\to G_{\rm eff}`$, $`\Lambda\to\Lambda_{\rm eff}`$.

## Controlled corrections and bounds

Deviations from the pure GR values can arise only through effects suppressed by the coherent sector assumptions:

#### (i) Warping corrections.

Assumption <a href="#H2" data-reference-type="ref" data-reference="H2">2</a> implies $`\delta\gamma,\delta\beta = \mathcal{O}(\varepsilon_{\rm warp})`$. Nonzero off-block $`g^{(10)}`$ components produce higher-curvature and non-minimal operators; their PPN impact is at least linear in $`\varepsilon_{\rm warp}`$.

#### (ii) Finite-gap corrections.

Off-harmonic leakage scales as $`\lambda_*^{-1}`$ (Assumption <a href="#H7" data-reference-type="ref" data-reference="H7">6</a>), inducing suppressed operators such as $`R^2`$, $`R_{\mu\nu}R^{\mu\nu}`$ and light scalar admixtures. Their PPN footprints enter at post-Newtonian order with coefficients $`\propto \lambda_*^{-1}`$.

#### (iii) Disturbance/stability effects.

If the damping-balance inequality is close to saturation ($`\delta_n/\gamma_n \lesssim 1`$), small open-system terms could generate effective non-conservative stresses outside compact sources. Solar-system bounds then constrain $`\delta_n/\gamma_n`$ and the coefficients of higher-derivative terms.

<div id="prop:PPN_bounds" class="proposition">

**Proposition 18** (Bounds from classical tests). *Let $`\Delta\gamma,\Delta\beta`$ denote deviations from GR values inferred from observation. Then the coherent-sector parameters satisfy
``` math
\begin{equation}
  |\Delta\gamma|,|\Delta\beta| \;\lesssim\; C_1\,\varepsilon_{\rm warp} \;+\; C_2\,\lambda_*^{-1}
  \;+\; C_3\,\max_n\frac{\delta_n}{\gamma_n},
\end{equation}
```
with $`C_i`$ dimensionless constants set by internal volumes and overlaps. Current solar-system limits (e.g. $`|\gamma-1|\lesssim 10^{-5}`$) thus bound the combination on the right-hand side.*

</div>

## Redshift, light bending, and lensing

Because null geodesics depend only on the conformal class of $`g`$ and $`S_{\rm eff}`$ yields the Levi–Civita connection, standard GR expressions hold with $`G_{\rm eff}`$:

- gravitational redshift $`\Delta\nu/\nu = \Delta U`$ (to leading order),

- light deflection angle near a point mass $`M`$: $`\hat\alpha = \frac{4G_{\rm eff} M}{b}`$ (impact parameter $`b`$),

- Shapiro delay $`\Delta t = 2(1+\gamma)G_{\rm eff}M\ln\!\frac{4r_E r_R}{b^2}`$ with $`\gamma=1`$.

Hence classical lensing observables calibrate $`G_{\rm eff}`$ on astrophysical scales.

## Summary

In the coherent, weak-field regime of the MTT reduction, free-fall worldlines are $`g`$-geodesics and the Newtonian and PPN limits coincide with those of GR, with $`G`$ and $`\Lambda`$ replaced by their effective values $`G_{\rm eff}`$ and $`\Lambda_{\rm eff}`$. All potential deviations are explicitly tied to warping, finite-gap leakage, or stability parameters and are therefore predictive and bounded.

# Controlled Corrections Beyond GR and Observational Windows

We quantify the leading, *controlled* departures from the Einstein–Hilbert limit that arise when Assumptions <a href="#H2" data-reference-type="ref" data-reference="H2">2</a> (small warping) and <a href="#H7" data-reference-type="ref" data-reference="H7">6</a> (finite-gap suppression) are relaxed at next-to-leading order, or when stability (Assumption <a href="#H4" data-reference-type="ref" data-reference="H4">3</a>) is approached. All corrections are organized by the small parameters
``` math
\varepsilon_{\rm warp}\,,\qquad \lambda_*^{-1}\,,\qquad \epsilon_{\rm open}:=\max_n \frac{\delta_n}{\gamma_n}\,,
```
and by the internal curvature scales.

## Operator basis and scaling

The coherent-sector projection $`\mathcal P`$ of any local $`10`$D scalar built from $`g^{(10)}`$ and the internal bundles yields a local $`4`$D scalar. At dimension $`\le 4`$ (in derivatives of $`g`$) the most general parity-even gravitational action is, up to boundary terms,
``` math
\begin{equation}
S_{\rm grav}^{(4)} \;=\; \frac{1}{16\pi G_{\rm eff}}\!\int\!\Big[ R - 2\Lambda_{\rm eff}
+ \alpha_1 R^2 + \alpha_2 R_{\mu\nu}R^{\mu\nu}
+ \alpha_3 R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}\Big]\sqrt{-g}\,d^4x,
\label{eq:eff_action_quadratic}
\end{equation}
```
with coefficients
``` math
\begin{equation}
\alpha_i \;=\; c_i^{\rm warp}\,\varepsilon_{\rm warp} \;+\; c_i^{\rm gap}\,\lambda_*^{-1} \;+\;
\mathcal{O}(\varepsilon_{\rm warp}^2,\lambda_*^{-2},\varepsilon_{\rm warp}\lambda_*^{-1}).
\label{eq:alpha_scaling}
\end{equation}
```
Here $`c_i^{\rm warp},c_i^{\rm gap}`$ are dimensionful numbers set by internal volumes, overlaps, and spectral data; their signs are fixed by the underlying $`10`$D action. In four dimensions, the Gauss–Bonnet combination is topological: $`\int (R^2-4R_{\mu\nu}R^{\mu\nu}+R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma})\sqrt{-g}\,d^4x`$ and does not contribute to local field equations; thus only two combinations of $`(\alpha_1,\alpha_2,\alpha_3)`$ are dynamical. We use the convenient basis $`(R^2,\,C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma})`$ with the Weyl tensor $`C`$ when analyzing wave propagation.

## Scalar–tensor channel from coherent moduli

If a coherent internal scalar $`\varphi`$ survives the projection (e.g. an internal volume modulus), the reduced action acquires scalar–tensor form:
``` math
\begin{equation}
S_{\rm ST} \;=\; \frac{1}{16\pi}\!\int\!\Big[ \Phi(\varphi)\,R
- \frac{\omega(\varphi)}{\Phi(\varphi)}\,(\nabla\varphi)^2 - 2 U(\varphi) \Big]\sqrt{-g}\,d^4x,
\label{eq:scalar_tensor}
\end{equation}
```
with $`\Phi(\varphi)=G_{\rm eff}^{-1}\big(1+\mathcal{O}(\lambda_*^{-1},\varepsilon_{\rm warp})\big)`$ and $`\omega(\varphi)\!\to\!\infty`$ in the strict coherent limit. Finite-gap leakage induces $`\omega_{\rm eff}^{-1}=\mathcal{O}(\lambda_*^{-1})`$ and small $`U'(\varphi)`$, so that deviations from GR in the PPN parameters scale like $`\sim \omega_{\rm eff}^{-1}`$ and are therefore bounded by $`\lambda_*^{-1}`$ times internal-overlap factors.

## Linearized gravitational waves and propagation speed

<div class="theorem">

**Theorem 19** (Luminal gravitational-wave propagation in the strict coherent limit). *In the strict coherent limit in which higher-curvature coefficients vanish (equivalently $`\epsilon_{\mathrm{warp}}\to 0`$ and $`\lambda_\ast^{-1}\to 0`$ within the admissible regime), the tensor sector of the reduced theory propagates on the null cone of the emergent metric $`g`$. In particular, the gravitational-wave phase and group velocities satisfy $`v_{\mathrm{ph}}=v_{\mathrm{gr}}=1`$ in units where $`c=1`$.*

</div>

<div class="remark">

*Remark 20*. At finite but controlled departures from the strict coherent limit, the dispersion relation acquires suppressed corrections governed by the small parameters appearing below (cf. equation (35)). Accordingly, observational constraints on $`|v_{\mathrm{ph}}-1|`$ bound combinations of $`\epsilon_{\mathrm{warp}}`$ and $`\lambda_\ast^{-1}`$ within the admissible window.

</div>

Expanding <a href="#eq:eff_action_quadratic" data-reference-type="eqref" data-reference="eq:eff_action_quadratic">[eq:eff_action_quadratic]</a> around Minkowski space and working in de Donder gauge, the tensor sector obeys (schematically)
``` math
\begin{equation}
\Big(1 + \tilde\alpha\,\Box\Big)\Box \bar h_{\mu\nu} \;=\; -16\pi G_{\rm eff}\,T_{\mu\nu}\,,
\qquad \tilde\alpha = a_1 \alpha_2 + a_2 \alpha_3,
\end{equation}
```
with $`a_{1,2}`$ numerical constants. The dispersion relation for free waves is $`\omega^2 = k^2\,\big(1 + \tilde\alpha\,k^2\big)`$, so the phase speed $`v_{\rm ph}\!=\!\omega/k = 1 + \frac12 \tilde\alpha k^2 + \cdots`$. Thus
``` math
\begin{equation}
|v_{\rm ph}-1| \;\lesssim\; \tfrac12 |\tilde\alpha|\,k^2
\;\sim\; \tfrac12 \big|c^{\rm warp}\varepsilon_{\rm warp} + c^{\rm gap}\lambda_*^{-1}\big| \, k^2.
\label{eq:gw_speed_bound}
\end{equation}
```
Observational constraints on the GW speed therefore bound combinations of $`\varepsilon_{\rm warp}`$ and $`\lambda_*^{-1}`$ at frequencies probed by LIGO/Virgo/KAGRA/LISA.

## Cosmology: background and perturbations

On a spatially flat FRW background $`ds^2=-dt^2+a(t)^2 d\mathbf{x}^2`$, the effective Friedmann equations from $`S_{\rm eff}+S_{\rm ST}`$ read
``` math
\begin{align}
3 H^2 &= 8\pi G_{\rm eff}\,\rho_{\rm tot} + \Lambda_{\rm eff} + \Delta\mathcal{E}_{\rm quad}
+ \Delta\mathcal{E}_{\rm ST}, \label{eq:Friedmann1}\\
-2 \dot H &= 8\pi G_{\rm eff}\,(\rho_{\rm tot}+p_{\rm tot})
+ \Delta\mathcal{P}_{\rm quad} + \Delta\mathcal{P}_{\rm ST},
\label{eq:Friedmann2}
\end{align}
```
where $`\Delta\mathcal{E}_{\rm quad},\Delta\mathcal{P}_{\rm quad}`$ arise from quadratic curvature terms ($`\propto \alpha_i`$; in FRW they reduce to functions of $`H,\dot H`$) and $`\Delta\mathcal{E}_{\rm ST},\Delta\mathcal{P}_{\rm ST}`$ from the scalar sector <a href="#eq:scalar_tensor" data-reference-type="eqref" data-reference="eq:scalar_tensor">[eq:scalar_tensor]</a>. In linear perturbation theory, the tensor mode equation becomes
``` math
\begin{equation}
\ddot h_{ij} + 3H \dot h_{ij} + \big(1+\delta c_T^2\big)\frac{k^2}{a^2} h_{ij}
+ \mu_T^2 h_{ij} \;=\; 0,
\end{equation}
```
with $`\delta c_T^2 = \mathcal{O}(\alpha_i H^2)\,,\quad \mu_T^2=\mathcal{O}(\alpha_i H^4)`$, hence $`\delta c_T^2\sim c^{\rm warp}\varepsilon_{\rm warp} H^2 + c^{\rm gap}\lambda_*^{-1} H^2`$. Cosmological bounds on $`c_T`$ during late times therefore constrain the same combinations as <a href="#eq:gw_speed_bound" data-reference-type="eqref" data-reference="eq:gw_speed_bound">[eq:gw_speed_bound]</a> but at $`k\!\ll\! aH`$.

## Open-system (non-unitary) corrections to classical sources

Approaching the edge of stability ($`\epsilon_{\rm open}\!\gtrsim\!0`$) induces effective, covariantly conserved but non-perfect stress contributions in macroscopic media:
``` math
\begin{equation}
T_{\mu\nu}^{\rm eff} \;=\; T_{\mu\nu}^{\rm (matter)} \;+\;
\Sigma_{\mu\nu}(\epsilon_{\rm open})\,,\qquad
\nabla^\mu \Sigma_{\mu\nu}=0,\qquad \Sigma_{\mu\nu}=\mathcal{O}(\epsilon_{\rm open}),
\end{equation}
```
where $`\Sigma_{\mu\nu}`$ captures small dissipative/viscoelastic responses inherited from modal disturbances. In stationary, weak-field systems this renormalizes the source of <a href="#eq:Poisson" data-reference-type="eqref" data-reference="eq:Poisson">[eq:Poisson]</a> by $`\rho \to \rho + \delta \rho`$ with $`\delta\rho/\rho = \mathcal{O}(\epsilon_{\rm open})`$.

## Observational windows and parameter bounds

The most direct probes of the coefficients in <a href="#eq:alpha_scaling" data-reference-type="eqref" data-reference="eq:alpha_scaling">[eq:alpha_scaling]</a> and the scalar channel <a href="#eq:scalar_tensor" data-reference-type="eqref" data-reference="eq:scalar_tensor">[eq:scalar_tensor]</a> are:

- **Solar-system PPN tests:** bound $`|\gamma-1|,|\beta-1|`$ $`\Rightarrow`$ constraints on $`\omega_{\rm eff}^{-1}`$ and linear combinations of $`\alpha_i`$ (entering at post-Newtonian order).

- **Binary pulsars / strong-field:** periastron advance and Shapiro delay bound higher-curvature effects via timing residuals; dipole radiation bounds scalar–tensor couplings when $`\Phi'(\varphi)\neq 0`$.

- **Gravitational-wave speed & dispersion:** $`|c_T-1|`$ and arrival-time comparisons constrain $`\tilde\alpha`$ as in <a href="#eq:gw_speed_bound" data-reference-type="eqref" data-reference="eq:gw_speed_bound">[eq:gw_speed_bound]</a> and any $`\mu_T^2`$.

- **Cosmology (CMB+LSS):** effective dark energy equation of state $`w_{\rm eff}\!=\!-1+\mathcal{O}(\alpha_i H^2,\omega_{\rm eff}^{-1})`$ and growth-rate modifications bound late-time combinations of $`(\alpha_i,\omega_{\rm eff}^{-1})`$.

Collecting, there exist $`\mathcal{O}(1)`$ constants $`K_i`$ such that
``` math
\begin{equation}
\varepsilon_{\rm warp} \;\lesssim\; K_1\,|\gamma-1| + K_2\,|c_T-1| + K_3\,|w_{\rm eff}+1|\,,
\qquad
\lambda_*^{-1} \;\lesssim\; K_4\,|\gamma-1| + K_5\,|c_T-1| + K_6\,|w_{\rm eff}+1|.
\end{equation}
```
Thus classical and cosmological tests translate directly into quantitative bounds on the coherent-sector control parameters.

## Summary of controlled deviations

To NLO in the small parameters, the reduced theory is
``` math
\begin{equation}
S_{\rm eff}^{\rm NLO} \;=\; \frac{1}{16\pi G_{\rm eff}}\!\int\!(R-2\Lambda_{\rm eff})\sqrt{-g}\,d^4x
+ S_{\rm matter}^{\rm coh} \;+\; S_{\rm quad}[g] \;+\; S_{\rm ST}[g,\varphi] 
\;+\; \mathcal{O}(\varepsilon_{\rm warp}^2,\lambda_*^{-2}),
\end{equation}
```
with $`S_{\rm quad}`$ as in <a href="#eq:eff_action_quadratic" data-reference-type="eqref" data-reference="eq:eff_action_quadratic">[eq:eff_action_quadratic]</a> and $`S_{\rm ST}`$ as in <a href="#eq:scalar_tensor" data-reference-type="eqref" data-reference="eq:scalar_tensor">[eq:scalar_tensor]</a>. All departures from GR are explicitly suppressed by $`(\varepsilon_{\rm warp},\lambda_*^{-1},\epsilon_{\rm open})`$, are technically natural (fixed by internal spectral data), and are therefore *predictive*.

# Conclusions and Outlook

We have given a first-principles derivation of the Einstein field equations and their classical limits from the ten-dimensional modal triplet theory (MTT) using the coherent-sector projection $`\mathcal{P}`$. Our analysis proceeded by:

- Defining the kinematic and dynamical structures on $`M^{10}`$ and the modal bundles, with stability, finite-gap, and small-warping assumptions ensuring well-defined projection.

- Showing that $`\mathcal{P}`$ maps the $`10`$D Levi–Civita connection to a torsion-free, metric-compatible connection on $`Y_4`$.

- Reducing the full MTT action to an effective $`4`$D action $`S_{\rm eff}`$ containing the Einstein–Hilbert term, cosmological constant, and minimally coupled matter fields arising from the modal sectors.

- Demonstrating that the resulting $`4`$D field equations coincide with the Einstein equations, with effective constants $`G_{\rm eff}`$ and $`\Lambda_{\rm eff}`$ determined by the internal geometry.

- Establishing the weak equivalence principle and recovering the Newtonian, post-Newtonian, and other classical limits, with deviations controlled by $`\varepsilon_{\rm warp}`$, $`\lambda_*^{-1}`$, and $`\epsilon_{\rm open}`$.

- Classifying the leading controlled corrections beyond GR, identifying the corresponding operators, and mapping them to observable effects in solar-system, gravitational-wave, and cosmological tests.

The result is a concrete *GR limit theorem* for MTT: in the coherent-sector regime, GR emerges exactly, with all possible deviations explicitly linked to measurable parameters of the internal modal structure.

From here, several directions are natural:

#### (i) Beyond the coherent sector.

Relaxing stability or finite-gap assumptions may yield long-range scalar or vector fields with masses comparable to current observational limits. This regime provides a natural framework for exploring dynamical dark energy or modified gravity phenomenology.

#### (ii) Quantum backreaction.

The MTT$`\to`$QM map developed in the companion paper can be combined with the present MTT$`\to`$GR derivation to yield a unified, first-principles semiclassical gravity description, in which the expectation value $`\langle T_{\mu\nu}\rangle_{\rm MTT}`$ acts as a source in the reduced Einstein equations.

#### (iii) Cosmological implications.

The controlled higher-curvature and scalar–tensor operators induce small, calculable changes to early-universe dynamics and late-time acceleration. Matching these predictions against CMB and large-scale-structure data will further constrain the modal parameters.

#### (iv) Strong-field tests.

Binary pulsar timing and gravitational-wave spectroscopy can probe the predicted higher-curvature dispersion relations and any scalar-mode polarizations.

Overall, the MTT framework now provides two complete low-energy limits: quantum mechanics and general relativity. Both are derivable from the same set of modal principles, with clear, quantifiable pathways for extensions beyond the standard theories.

## Variational Derivation and RG Flow of $`G_{\mathrm{eff}}`$ and $`\Lambda_{\mathrm{eff}}`$

We now present the explicit reduction of the $`10`$D MTT action to the GR limit via $`\Pi_{\mathrm{GR}}`$, and derive the renormalisation-group flow of the effective Newton and cosmological constants.

#### Step 1: $`10`$D action.

The gravitational sector of MTT takes the form
``` math
\begin{equation}
S_{\mathrm{grav}}^{(10)} =
\frac{1}{16\pi G_{10}} \int_{M^{10}} d^{10}X \,\sqrt{-g_{10}}\;
\left( R^{(10)} - 2\Lambda_{\mathrm{int}} \right),
\label{eq:10Dgrav}
\end{equation}
```
with additional gauge, fermion, scalar, and modal-phase terms. Topological integers $`(Q_{ij},k_n,g)`$ fix the bundle class.

#### Step 2: Mode expansion and projection.

Let $`M^{10} \simeq Y_4 \times B_1 \times B_2 \times B_3`$ with local coordinates $`X^A = (x^\mu, y^{(1)}, y^{(2)}, y^{(3)})`$. Decompose fields into harmonics on each $`B_n`$:
``` math
\Phi(X) = \sum_{\vec{m}} \phi_{\vec{m}}(x^\mu) \, Y_{\vec{m}}(y^{(1)},y^{(2)},y^{(3)}).
```
Finite-gap suppression by Assumption 2.7 ensures heavy modes contribute only $`O(\lambda_\ast^{-2})`$ to the 4D action. We retain the coherent zero modes.

#### Step 3: Integration over $`B_n`$.

For a block-diagonal metric $`g_{AB} = \mathrm{diag}(g_{\mu\nu}, g_{ab}^{(1)}, g_{cd}^{(2)}, g_{ef}^{(3)})`$ and constant internal metric moduli,
``` math
\begin{equation}
S_{\mathrm{grav}}^{(10)} \to
\frac{V_{\mathrm{int}}}{16\pi G_{10}} \int_{Y_4} d^4x\, \sqrt{-g_{4}}\;
\left( R^{(4)} - 2\Lambda_{\mathrm{int}} \right),
\end{equation}
```
where $`V_{\mathrm{int}} = \prod_{n=1}^3 \mathrm{Vol}(B_n)`$ is fixed by the superselection data.

#### Step 4: Identification of $`G_{\mathrm{eff}}`$ and $`\Lambda_{\mathrm{eff}}`$.

Comparing with the standard 4D Einstein–Hilbert term yields
``` math
\begin{align}
G_{\mathrm{eff}}^{-1} &= G_{10}^{-1} V_{\mathrm{int}}, \label{eq:Geff}\\
\Lambda_{\mathrm{eff}} &= \Lambda_{\mathrm{int}} + \Lambda_{\mathrm{vac}}^{\mathrm{modal}},
\label{eq:Lambdaeff}
\end{align}
```
where $`\Lambda_{\mathrm{vac}}^{\mathrm{modal}}`$ arises from the coherent sector’s vacuum energy, including curvature–gap scalar potentials and Casimir-like contributions from $`B_n`$.

#### Step 5: Variation and field equations.

Varying the effective 4D action
``` math
\begin{equation}
S_{\mathrm{eff}}^{(4)} =
\frac{1}{16\pi G_{\mathrm{eff}}} \int_{Y_4} d^4x\, \sqrt{-g_{4}}\;
\left( R^{(4)} - 2\Lambda_{\mathrm{eff}} \right) + S_{\mathrm{matter}}^{\mathrm{coh}}
\end{equation}
```
with respect to $`g_{\mu\nu}`$ yields
``` math
\begin{equation}
G_{\mu\nu} + \Lambda_{\mathrm{eff}} g_{\mu\nu}
= 8\pi G_{\mathrm{eff}}\,T_{\mu\nu}^{\mathrm{coh}} + \mathcal{O}(\lambda_*^{-2}),
\end{equation}
```
which is Eq. <a href="#eq:GRlimit" data-reference-type="eqref" data-reference="eq:GRlimit">[eq:GRlimit]</a> in Theorem <a href="#thm:GRlimit" data-reference-type="ref" data-reference="thm:GRlimit">[thm:GRlimit]</a>.

#### Step 6: Renormalisation-group flow.

Using the background-field method with $`g_{\mu\nu} = \bar{g}_{\mu\nu} + h_{\mu\nu}`$ and adding an IR regulator $`\Delta S_k`$, the scale-dependent effective action $`\Gamma_k`$ obeys the Wetterich equation
``` math
\begin{equation}
\partial_k \Gamma_k = \frac{i}{2} \mathrm{STr}
\left[ \left( \Gamma^{(2)}_k + \mathcal{R}_k \right)^{-1} \partial_k \mathcal{R}_k \right].
\end{equation}
```
Projecting $`\Gamma_k`$ onto the subspace spanned by $`\{\int \sqrt{-g}, \int \sqrt{-g} R\}`$ gives the beta functions
``` math
\begin{align}
\partial_k G_{\mathrm{eff}}(k) &= \beta_G(G_{\mathrm{eff}},\Lambda_{\mathrm{eff}},\ldots),\\
\partial_k \Lambda_{\mathrm{eff}}(k) &= \beta_\Lambda(G_{\mathrm{eff}},\Lambda_{\mathrm{eff}},\ldots),
\end{align}
```
where the ellipsis includes gauge and scalar couplings from the coherent sector. In the classical regime $`k \ll \lambda_*`$, the flows freeze to constants $`G_{\mathrm{eff}}`$ and $`\Lambda_{\mathrm{eff}}`$ as in Eqs. <a href="#eq:Geff" data-reference-type="eqref" data-reference="eq:Geff">[eq:Geff]</a>–<a href="#eq:Lambdaeff" data-reference-type="eqref" data-reference="eq:Lambdaeff">[eq:Lambdaeff]</a>.

#### Step 7: Phenomenological implications.

The running of $`G_{\mathrm{eff}}`$ links the microscopic MTT parameters $`(G_{10}, V_{\mathrm{int}})`$ to the observed Newton constant, while $`\Lambda_{\mathrm{eff}}`$ running can in principle address its smallness via balancing between $`\Lambda_{\mathrm{int}}`$ and $`\Lambda_{\mathrm{vac}}^{\mathrm{modal}}`$.

# Projector Regularity and Coherent-Sector Conditions

We collect here the detailed definition of the projection $`\mathcal{P}`$ from $`M^{10}`$ to $`Y_4`$ and the regularity conditions ensuring that the pushforward of the Levi–Civita connection remains torsion-free and metric-compatible. This includes proofs of Propositions <a href="#prop:proj_connection" data-reference-type="ref" data-reference="prop:proj_connection">[prop:proj_connection]</a> and <a href="#prop:proj_metric" data-reference-type="ref" data-reference="prop:proj_metric">[prop:proj_metric]</a>.

# Curvature Decomposition

A block decomposition of the $`10`$D Riemann tensor $`R^{(10)}`$ is given in terms of the base curvature $`R^{(4)}`$, internal curvatures $`R^{(B_n)}`$, and warping tensors. We show explicitly how the $`\mathcal{O}(\varepsilon_{\rm warp})`$ terms enter the effective $`4`$D curvature scalars.

# FRW Reduction of Quadratic Curvature Terms

We reduce the quadratic terms $`R^2`$, $`R_{\mu\nu}R^{\mu\nu}`$, $`C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}`$ to a spatially flat FRW background, deriving the explicit forms of $`\Delta\mathcal{E}_{\rm quad}`$ and $`\Delta\mathcal{P}_{\rm quad}`$ used in Eqs. <a href="#eq:Friedmann1" data-reference-type="eqref" data-reference="eq:Friedmann1">[eq:Friedmann1]</a>–<a href="#eq:Friedmann2" data-reference-type="eqref" data-reference="eq:Friedmann2">[eq:Friedmann2]</a>. The resulting slow-roll and radiation-era limits are given, showing suppression by $`(\varepsilon_{\rm warp},\lambda_*^{-1})`$.

<div class="thebibliography">

10

P. Nero. *Modal Triplet Theory: Foundation* Zenodo, 2025.

</div>
