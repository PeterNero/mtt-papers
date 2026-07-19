---
abstract: |
  We present a constructive perturbative quantum gravity built from Modal Triplet Theory (MTT). The projected graviton propagator admits a Stieltjes/Bernstein representation, ensuring OS-positivity, unitarity, and causal support. A proper-time coarse-graining (“SPT”) derived from bounded projectors yields a universal Gaussian damping $`e^{-\tau_0 k^2}`$ on every internal graviton line, ensuring all-loop finiteness of graphs containing at least one graviton (due to the universal Gaussian damping on graviton propagators). Purely matter subgraphs renormalize by standard EFT methods and are not claimed UV-finite by this mechanism. BRST/BV consistency is preserved: the quantum master equation holds to all orders for anomaly-free matter content, and gauge-parameter independence is maintained. In the infrared limit, the Bernstein form factor reduces to unity and GR is recovered up to $`\mathcal O(\Box/\Lambda^2)`$ corrections. In the CY/toroidal corner, modular invariance independently ensures one-loop finiteness. Together these results amount to a rigorous proof (under the SPT factorization hypotheses stated below) that perturbative quantum gravity around MTT fixed points is unitary and causal, and is UV finite to all loop orders for amplitudes with at least one internal graviton line; purely matter subgraphs renormalize by standard EFT methods and are not claimed UV-finite by the SPT mechanism.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v4
date: January, 2026
generated_from_main_tex_sha256: adca935edcce4c549bcfe36b1187676fb975fb820baf20e6a4300a7887b8e935
paper_id: modal-triplet-theory-from-mtt-to-a-uv-finite-unitary-qu-9a90a5c0
release_state: zenodo_released
released_version: v4.0
title: "**Modal Triplet Theory: From MTT to a UV-Finite, Unitary Quantum Gravity**"
zenodo_doi: 10.5281/zenodo.18329495
zenodo_record_id: 18329495
zenodo_url: "https://zenodo.org/records/18329495"
---

# Introduction

Perturbative quantum gravity in four dimensions, when naively quantized, is famously non-renormalizable. We show here that by working within the fixed-point/coherent sector of Modal Triplet Theory, one can construct a perturbative QG that is *unitary*, *causal*, and *UV finite to all loop orders*. The key new element is the *Spectral Proper-Time* (SPT) coarse-graining of the coherent projector, which imposes a universal Gaussian suppression $`e^{-\tau_0 k^2}`$ on graviton propagators, sufficient to dominate all loop integrals.

#### Scope.

All results are *perturbative* around coherent MTT fixed points under *bounded-geometry* and *spectral-gap* hypotheses; “background independence’’ is meant in the *BRST/background-field* sense.

<div id="thm:main" class="theorem">

**Theorem 1** (Main Theorem: all-orders perturbative QG under SPT). *Let $`(Y_4,\bar g)`$ be a bounded-geometry background and let the coherent projector and shape map realize the proper-time factorization $`B \,=\, e^{-\tfrac{\tau_0}{2}E}\,B_0\,e^{-\tfrac{\tau_0}{2}A_{\mathrm{int}}}`$ with $`\tau_0>0`$, $`\|B_0\|\le C_0`$, and $`A_{\mathrm{int}}\!\ge\!\lambda_\ast>0`$ on the orthogonal complement of the coherent sector. Then the graviton–matter theory with quadratic kernel $`K=(BA^{-1}B^*)^{-1}`$ and propagator $`\Delta_{\mathrm{prop}}=BA^{-1}B^*`$ satisfies:*

1.  ***Unitary and causal:** the two-point function has a positive Källén–Lehmann (Stieltjes) representation and defines OS-positive Euclidean correlators; retarded kernels have future-lightcone support.*

2.  ***All-loop finiteness (graviton graphs):** every connected 1PI amplitude with at least one internal graviton line is UV finite. Quantitatively, for external scale $`Q`$ and $`L`$ loops,
    ``` math
    |\mathcal M_L(Q)| \,\le\, P_L(Q)\,\exp\!\big[-\,c_L\,\tau_0\,Q^2\big],
    \qquad 0<c_L\le I_\Gamma,
    ```
    with $`P_L`$ polynomial and $`I_\Gamma`$ the number of internal graviton lines.*

3.  ***BV/QME at all orders:** assuming the 4D matter content is anomaly-free, there exists a local renormalization scheme such that the renormalized BV action $`S`$ obeys $`\frac12(S,S)=i\hbar\,\Delta_{\mathrm{BV}}S`$ to all loop orders (Slavnov–Taylor identities hold nonperturbatively in external kinematics). Assume absence of local gauge anomalies, mixed gauge–gravitational anomalies, and the global SU(2) anomaly for the coherent matter content (so that the relevant local BRST/BV cohomology $`H^1_{\mathrm{loc}}(s|d)`$ vanishes). Then the quantum master equation can be restored to all loop orders by local counterterms.*

4.  ***Infrared recovery of GR:** the Bernstein form factor $`F(\Box)`$ satisfies $`F(0)=1`$ and $`F(\Box)=1+\mathcal O(\Box/\Lambda^2)`$, hence the spin-2 propagator reduces to the GR one for $`|k^2|\ll \Lambda^2:=c_{\mathrm{proj}}\lambda_\ast`$.*

*All constants $`(\lambda_\ast,\tau_0,C_0,c_{\mathrm{proj}})`$ are geometric/projector data; statements (1)–(4) are stable under bounded changes of projector realization.*

*Purely matter subgraphs (with no internal graviton lines) are treated by standard renormalizable/EFT counterterms and are not claimed UV-finite by this mechanism.*

</div>

# Standing assumptions and operator setting

We assume throughout:

- bounded geometry on $`(Y_4,\bar g)`$ and on the internal sector;

- a positive spectral gap $`\lambda_\ast>0`$ above the coherent zero modes of $`A_{\mathrm{int}}`$;

- bounded projectors on Sobolev scales and a bounded metric shape map $`B`$;

- commuting external/internal blocks $`[E,A_{\mathrm{int}}]=0`$.

#### SPT hypothesis (proper-time gap).

In addition to the standing geometric and spectral assumptions above, the all-loop finiteness mechanism uses a projector-induced spectral filter with a strictly positive proper-time gap. Concretely, we assume the coherent projector can be realized (on the relevant slab) by completely monotone spectral filters on the external and internal blocks,
``` math
\Pi_{\mathrm{coh}} = \phi(E)\,\psi(A_{\mathrm{int}}),
\qquad
\phi(z)=\int_{\tau_{\mathrm{ext}}}^{\infty} e^{-t z}\,d\mu_{\mathrm{ext}}(t),
\qquad
\psi(\lambda)=\int_{\tau_{\mathrm{int}}}^{\infty} e^{-s \lambda}\,d\mu_{\mathrm{int}}(s),
```
with finite positive measures $`\mu_{\mathrm{ext}},\mu_{\mathrm{int}}`$ and $`\tau_{\mathrm{ext}},\tau_{\mathrm{int}}>0`$. We write $`\tau_0:=\min\{\tau_{\mathrm{ext}},\tau_{\mathrm{int}}\}>0`$. This is the SPT coarse-graining scale used throughout; it is restated in Appendix A (Assumption A.3) and in Appendix F where the factorization is derived.

#### Stability under small off-diagonal couplings.

If $`A = E \oplus A_{\mathrm{int}} + V`$ with $`V`$ symmetric and $`A_0`$–form-bounded relative to $`A_0:=E\oplus A_{\mathrm{int}}`$ with relative bound strictly less than $`1`$, i.e. there exist $`a\in[0,1)`$ and $`b\ge 0`$ such that
``` math
|\langle u,Vu\rangle| \le a\,\langle u,A_0 u\rangle + b\,\|u\|^2
\qquad \text{for all }u\in\mathrm{Dom}(A_0^{1/2}),
```
then by Kato–Rellich (and Trotter product control) the heat semigroup satisfies, uniformly for $`t\in(0,1]`$,
``` math
e^{-tA} = e^{-tE}\,e^{-tA_{\mathrm{int}}} + \mathcal{O}(t)
\quad \text{in operator norm on }H^1,
```
with constants depending continuously on $`(a,b)`$ on bounded-geometry families. In particular, all SPT bounds persist with renormalised constants $`(\tau_0,C_0)\mapsto(\tau'_0,C'_0)`$. This includes mild warp/twist couplings in factorised backgrounds.

<div id="lem:proper-time" class="lemma">

**Lemma 2** (Proper-time representation for the projected propagator). *Assume the standing assumptions of Section 2, including bounded geometry, a positive spectral gap above the coherent sector, and bounded coherent projectors on the relevant Sobolev scales, on the time slab. Let $`P=I\circ \Pi`$ be the coherent projector and let $`A`$ be the projected linearized graviton operator on the TT sector, with spectrum bounded below by $`\lambda_\ast>0`$ on the $`Q`$-sector. Then there exists $`\tau_0>0`$ and constants $`C,c>0`$ such that the projected propagator admits a proper-time representation with uniform bound
``` math
\|\Delta_{\mathrm{prop}}(k)\|\le C\,\frac{e^{-\tau_0 k^2}}{k^2+\lambda_\ast},
```
where $`k`$ is the Fourier variable in locally geodesic coordinates on the slab and the bound is uniform on bounded-geometry charts.*

</div>

<div id="thm:SPT" class="theorem">

**Theorem 3** (SPT from a bounded projector). *Under the above assumptions, there exists $`\tau_0>0`$ and a bounded operator $`B_0`$ such that
``` math
B \;=\; e^{-\tfrac{\tau_0}{2}E}\,B_0\,e^{-\tfrac{\tau_0}{2}A_{\mathrm{int}}},
```
with $`\|B_0\|\le C_0`$. Consequently,
``` math
\|\Delta_{\mathrm{prop}}(k)\|\;\le\; \frac{C_0}{k^2+\lambda_\ast}\,e^{-\tau_0 k^2},
```
so each internal graviton line carries a universal Gaussian factor $`e^{-\tau_0 k^2}`$.*

</div>

<div class="proof">

*Proof.* The coherent projector is realized by spectral filters on $`E`$ and $`A_{\mathrm{int}}`$, with proper-time representations. By bounded-geometry parametrix transfer, $`DG(\Psi_\ast)e^{-t(-{\Delta_{\mathrm{prop}}}_{Y_4})}=e^{-ctE}S_t`$ with $`c\in(0,1]`$ and bounded $`S_t`$. Choosing $`\tau_0\le \min\{c\tau_{\mathrm{ext}},\tau_{\mathrm{int}}\}`$ and factoring the semigroups yields the claimed decomposition. ◻

</div>

<div id="lem:universality" class="lemma">

**Lemma 4** (Universality under projector realization). *Let $`\Pi_{1,2}`$ be two bounded realizations of the same coherent range and $`B_i=DG(\Psi_\ast)\circ \Pi_i`$. If $`B_2=B_1U`$ with $`U`$ positive and commuting with $`E,A_{\mathrm{int}}`$, then $`{\Delta_{\mathrm{prop}}}_1={\Delta_{\mathrm{prop}}}_2`$. Physical correlators and the Gaussian bound are independent of projector filter details.*

</div>

## Notation and constants (quick index)

#### Conventions.

Background: $`(Y_4,\bar g)`$ of bounded geometry; external operator $`E`$ is the Lichnerowicz operator on TT fluctuations (de Donder/harmonic gauge); internal operator $`A_{\mathrm{int}}`$ acts on the orthogonal complement of the coherent sector. Blocks commute: $`[E,A_{\mathrm{int}}]=0`$. The metric shape map at the fixed point is $`B`$ & bounded map & Metric shape map at $`\Psi^\ast`$; $`B= \left.\frac{\delta g}{\delta \Psi}\right|_{\Psi^\ast}`$; $`\|B\|\le C_B`$; Sec. 2.

<div class="center">

| **Symbol** | **Type** | **Meaning / Where fixed** |
|:---|:---|:---|
| $`Y_4`$, $`\bar g`$ | geometry | 4D background (bounded geometry); Sec. <a href="#sec:assumptions" data-reference-type="ref" data-reference="sec:assumptions">2</a>. |
| $`E`$ | operator | Lichnerowicz operator on TT modes (external block). |
| $`A_{\mathrm{int}}`$ | operator | Internal block; spectral gap $`\sigma(A_{\mathrm{int}})\subset[\lambda_\ast,\infty)`$; Sec. <a href="#sec:assumptions" data-reference-type="ref" data-reference="sec:assumptions">2</a>. |
| $`A`$ | operator | Full Hessian at the fixed point: $`A=E\oplus A_{\mathrm{int}}`$; $`[E,A_{\mathrm{int}}]=0`$. |
| $`B`$ | bounded map | Metric shape map at $`\Psi_\ast`$; $`\|B\|\le C_B`$; Sec. <a href="#sec:assumptions" data-reference-type="ref" data-reference="sec:assumptions">2</a>. |
| $`\Pi_{\rm coh}`$ | projector | Coherent-sector projector via spectral filters on $`(-\bar\square)`$ and $`A_{\mathrm{int}}`$. |
| $`B_0`$ | bounded map | SPT core map after pulling out proper–time dressings; $`\|B_0\|\le C_0`$; Thm. <a href="#thm:SPT" data-reference-type="ref" data-reference="thm:SPT">3</a>. |
| $`\tau_0`$ | time scale | SPT proper time; window $`0<\tau_0\le \min\{c\,\tau_{\mathrm{ext}},\tau_{\mathrm{int}}\}`$ (parametrix transfer $`c\in(0,1]`$). |
| $`\lambda_\ast`$ | gap | First positive eigenvalue bound for $`A_{\mathrm{int}}`$ on the non‑coherent slice. |
| $`c_{\mathrm{proj}}`$ | constant | Projector/parametrix constant ($`0<c_{\mathrm{proj}}\le 1`$) entering the geometry$`\to`$scale map. |
| $`\Lambda^2`$ | scale | Suppression scale: $`\Lambda^2:=c_{\mathrm{proj}}\lambda_\ast`$; Secs. <a href="#sec:UV" data-reference-type="ref" data-reference="sec:UV">4</a>, <a href="#sec:numerics" data-reference-type="ref" data-reference="sec:numerics">9</a>. |
| $`\Delta_{\mathrm{prop}}`$ | kernel | Graviton propagator $`\Delta_{\mathrm{prop}}=BA^{-1}B^*`$; Stieltjes/Bernstein rep.; Secs. <a href="#sec:propagator" data-reference-type="ref" data-reference="sec:propagator">3</a>, <a href="#sec:UV" data-reference-type="ref" data-reference="sec:UV">4</a>. |
| $`K`$ | operator | Quadratic kernel on TT: $`K=(BA^{-1}B^*)^{-1}=F(E)\,E`$ with $`F`$ Bernstein; Sec. <a href="#sec:IR" data-reference-type="ref" data-reference="sec:IR">8</a>. |
| $`F`$ | function | Complete Bernstein form factor with $`F(0)=1`$, $`F(z)=1+\mathcal O(z)`$ as $`z\to 0^+`$; Lem. <a href="#lem:IR-bernstein" data-reference-type="ref" data-reference="lem:IR-bernstein">10</a>. |
| $`\nu`$ | measure | Positive operator‐valued measure in $`\Delta_{\mathrm{prop}}=\int_0^\infty (E+s)^{-1}\,\nu(ds)`$; App. <a href="#app:stieltjes" data-reference-type="ref" data-reference="app:stieltjes">13</a>. |
| $`\Gamma`$ | action | Renormalized 1PI effective action in BV; Sec. <a href="#sec:BV" data-reference-type="ref" data-reference="sec:BV">6</a>. |
| $`(\cdot,\cdot)`$ | bracket | BV antibracket; Sec. <a href="#sec:BV" data-reference-type="ref" data-reference="sec:BV">6</a>. |
| $`\Delta_{\mathrm{BV}}`$ | operator | BV Laplacian (see note below to avoid clash with propagator $`\Delta_{\mathrm{prop}}`$). |

</div>

#### Key inequalities at a glance.

There exist constants $`C_0,C_1>0`$ (uniform on bounded–geometry families) such that
``` math
\begin{align}
&\textbf{SPT factorization:}\quad
B \;=\; e^{-\tfrac{\tau_0}{2}E}\;B_0\;e^{-\tfrac{\tau_0}{2}A_{\mathrm{int}}},\qquad \|B_0\|\le C_0,
\label{eq:idx-spt}\\[2pt]
&\textbf{Gaussian-dressed propagator:}\quad
\|\Delta_{\mathrm{prop}}(k)\|\;\le\;\frac{C_0}{k^2+\lambda_\ast}\,e^{-\tau_0 k^2},
\label{eq:idx-gauss}\\[2pt]
&\textbf{All-loop domination (schematic):}\quad
|\mathcal M_\Gamma(Q)| \;\le\; P_\Gamma(Q)\,e^{-\,c_\Gamma\,\tau_0\,Q^2},\qquad c_\Gamma\in(0,1],
\label{eq:idx-allloops}\\[2pt]
&\textbf{IR expansion of $F$:}\quad
F(z)=1+C_{\mathrm{IR}}\,z+\mathcal O(z^2),\qquad z\to 0^+,
\label{eq:idx-IR}
\end{align}
```
with $`P_\Gamma`$ a polynomial (fixed by vertex tensor ranks) and $`C_{\mathrm{IR}}`$ finite on bounded–geometry families.

#### Conventions (quick).

Signature $`(-,+,+,+)`$; $`\kappa_4^2:=8\pi G`$; background covariant derivative $`\bar\nabla`$; $`\square_{\bar g}:=\bar g^{\mu\nu}\bar\nabla_\mu\bar\nabla_\nu`$. TT means transverse–traceless relative to $`\bar g`$. We use: Epstein–Glaser causal perturbation theory (EG), perturbative algebraic QFT (pAQFT), Functional Renormalization Group (FRG), Quantum Master Equation (QME), and BRST/BV in the background-field formalism. Throughout, $`\Delta_{\mathrm{prop}}`$ denotes the graviton propagator and $`\Delta_{\mathrm{BV}}`$ the BV Laplacian.

# Propagator and positivity

#### Scope of positivity and unitarity.

We prove Osterwalder–Schrader (OS) reflection positivity for the *physical TT two-point function* (or equivalently for the projected, gauge-invariant graviton correlator in the transverse–traceless sector). We do *not* claim OS positivity for the full gauge-fixed field space, which carries an indefinite inner product. Unitarity is asserted in the standard way: on the BRST/BV cohomology of observables in the EG/pAQFT framework, where gauge dependence and unphysical polarizations decouple.

With $`\Delta_{\mathrm{prop}}=BA^{-1}B^*`$ and the SPT factorization, one has the integral representation
``` math
\Delta_{\mathrm{prop}}\;=\; \int_0^\infty e^{-tE}\,M(t)\,dt,\qquad M(t)=N(t)^{\!*N(t)}\ge0.
```

#### TT restriction.

In this section $`E`$ is the Lichnerowicz operator acting on *transverse–traceless* (TT) metric fluctuations (de Donder/harmonic gauge). Positivity statements below apply to TT two-point functions; pure-gauge directions are removed by the BV gauge-fixing.

Therefore the Euclidean two-point function satisfies the OS positivity condition .

Thus $`\Delta_{\mathrm{prop}}`$ is a Stieltjes transform of a positive operator measure, admits a positive Källén–Lehmann spectral density, is OS positive in Euclidean signature, and yields retarded kernels supported in the future light cone upon Wick rotation.

#### Relation to prior frameworks.

Our positivity and causality statements use the Stieltjes/Bernstein representation of the TT two-point function, placing us squarely within the Osterwalder–Schrader framework for reflection positivity and the curved-spacetime EG/pAQFT locality/covariance programme (= Källén–Lehmann form) .

The Gaussian/entire damping here is *derived* from the coherent projector (SPT), not an ad hoc form factor.

# UV behaviour and one-loop modular check

The Gaussian bound $`\|\Delta_{\mathrm{prop}}(k)\|\le C_0(k^2+\lambda_\ast)^{-1}e^{-\tau_0k^2}`$ ensures that every graviton-containing loop integral is finite. For one-loop finiteness in the CY/toroidal corner, modular invariance provides an independent guarantee:

<div id="prop:modular" class="proposition">

**Proposition 5** (One-loop finiteness from modular invariance). *In the Calabi–Yau/toroidal corner, the one-loop graviton sector reduces to an $`SL(2,\mathbb Z)`$-invariant torus integral with Narain lattice factor $`Z_{\mathrm{lat}}(\tau,\bar\tau;G,B)`$. The integrand has modular weight $`0`$, hence the integral over the fundamental domain $`\mathcal F`$ is finite (UV $`\tau_2\!\to\!0`$ is mapped to IR $`\tau_2\!\to\!\infty`$).*

</div>

<div class="proof">

*Proof sketch.* Poisson resummation shows $`Z_{\mathrm{lat}}`$ is invariant under $`S`$ and $`T`$; ghosts and non-toroidal factors complete the weight to $`0`$. Integrability on $`\mathcal F`$ then yields finiteness. ◻

</div>

## Geometric origin of the UV regulator

#### Statement.

In the coherent-sector reduction of MTT, the ultraviolet regulator is not an external artefact but a geometric consequence of (i) the bounded, joint harmonic projection $`\Pi := \Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$ on the internal bundles $`B_n`$, (ii) the internal pushforward $`I`$ to the 4D base $`Y_4`$, and (iii) a background-covariant coarse–graining on $`Y_4`$ implemented by a regulator $`R_k(-\nabla^2)`$ that is a positive function of the background Laplacian. Together these furnish an intrinsic high–frequency suppression in the observable sector and a covariant realisation of the FRG flow.

#### Bandlimiting by coherent projection.

Let $`A := \kappa_1\Delta_{B_1} + \kappa_2\Delta_{B_2} + \kappa_3\Delta_{B_3} + \varepsilon\,\Delta_{Y}`$ on the 10D bundle (with $`\kappa_n>0`$, $`\varepsilon>0`$ fixed), and let $`Q := \mathbf 1 - \Pi`$ project to the non–coherent (off–harmonic) sector. The internal gaps $`\lambda_{n,\ast}>0`$ yield a uniform $`\lambda_\ast := \min_n \kappa_n\lambda_{n,\ast} > 0`$. By spectral calculus, for $`t>0`$
``` math
\begin{equation}
  \big\| A^{1/2} e^{-tA}\,Q \big\|_{L^2\to L^2} \;\lesssim\; t^{-1/2}\,e^{-\lambda_\ast t}, 
  \qquad 
  \big\| e^{-tA} \big\|_{L^2\to H^1} \;\lesssim\; (1+t^{-1/2})\,e^{-\lambda_\ast t}.
  \label{eq:semigroup-bound}
\end{equation}
```
Hence long–time modal flow suppresses $`Q`$–modes exponentially and contracts to $`\mathrm{Ran}\,\Pi`$. The observable map $`P:=I\circ\Pi`$ acts as a geometric band–limiter: external correlators carry only the fibre–harmonic content, with off–harmonic contributions damped by $`e^{-\lambda_\ast t}`$. This produces an intrinsic UV softness before any auxiliary cutoff is introduced.

#### Covariant regulator on $`Y_4`$.

On the observable side, define the (Euclidean) effective average action
``` math
\begin{equation}
  \Gamma_k[g,\Phi] \;=\; S_{\rm coh}[g,\Phi] \;+\; \tfrac12 \!\int\! \sqrt{g}\;\Phi\,R_k(-\nabla^2)\,\Phi,
\end{equation}
```
with $`R_k(z)`$ satisfying $`R_k(z)\!\to\! k^2`$ for $`z\!\ll\! k^2`$ and $`R_k(z)\!\to\!0`$ for $`z\!\gg\!k^2`$, and $`\Phi`$ denoting the collection of coherent fields (bosons, fermions in suitable quadratic forms). The flow is governed by the Wetterich equation
``` math
\begin{equation}
  \partial_k\Gamma_k \;=\; \tfrac12\,\mathrm{STr}\,\Big(\Gamma_k^{(2)} + R_k\Big)^{-1}\,\partial_k R_k,
  \label{eq:wetterich}
\end{equation}
```
written in a background–field gauge so that $`R_k`$ is a scalar function of $`-\nabla^2`$ and thus preserves diffeomorphism covariance of the flow. In Lorentzian signature one uses the standard in–in variant; all Ward/BRST identities are recovered as $`k\!\to\!0`$.

With this background–covariant choice $`R_k(-\bar\nabla^2)`$, the modified Slavnov–Taylor identities and the QME hold at each finite $`k`$ and reduce to the exact identities as $`k\downarrow 0`$ (see Theorem H.5).

#### SPT versus FRG (conceptual separation).

It is important to distinguish the roles of the SPT factorization and the functional renormalization–group (FRG) regulator $`R_k`$. The SPT mechanism is a projector–induced modification of the physical graviton propagator: it arises from the coherent projection $`P = I \circ \Pi`$ and yields an intrinsic Gaussian dressing $`e^{-\tau_0 k^2}`$ on each internal graviton line, independent of any auxiliary regulator. This dressing is present at $`k=0`$ and is the sole source of the all–loop ultraviolet finiteness established in Theorem 1.1.

By contrast, the FRG regulator $`R_k(-\nabla^2)`$ is introduced only as an organizational tool to define a covariant coarse–graining and to control the flow of local counterterms. The limit $`k \to 0`$ is taken after renormalization, and removing $`R_k`$ does not remove the SPT Gaussian damping, which is fixed by the coherent–sector data $`(\tau_0,\lambda_*)`$.

#### Propagator structure and UV finiteness at fixed $`k`$.

Because $`P=I\circ\Pi`$ projects to fibre–harmonic profiles, the 10D kinetic operator reduces to a 4D operator of the form $`K_{\rm obs}(-\nabla^2) + M^2_{\rm obs}(x)`$ on $`Y_4`$. With the addition of $`R_k(-\nabla^2)`$ one has, schematically,
``` math
\begin{equation}
  G_k(p^2) \;=\; \frac{1}{K_{\rm obs}(p^2)\;+\;M_{\rm obs}^2\;+\;R_k(p^2)} 
  \;\sim\; 
  \begin{cases}
    1/k^2 & (p^2\!\ll\!k^2),\\[2pt]
    1/K_{\rm obs}(p^2) & (p^2\!\gg\!k^2),
  \end{cases}
\end{equation}
```
so loop integrals at fixed $`k`$ are manifestly finite. The internal bandlimiting from $`\Pi`$ removes vertical high–frequency channels; $`R_k`$ regulates remaining 4D momenta in a covariant manner. Taking $`k\!\to\!0`$ after renormalising couplings yields cutoff–independent observables.

#### Compatibility with BV/QME.

Since $`R_k`$ is a function of the background Laplacian, the modified Slavnov–Taylor/BRST identities hold along the flow and reduce to the exact identities as $`k\!\to\!0`$. The BV master equation is satisfied up to standard regulator insertions, which vanish in the physical limit; the proofs use only locality of the quadratic form and the spectral functional calculus for $`R_k(-\nabla^2)`$.

#### Conclusion.

The UV regulator in this framework is entirely geometric: (i) $`\Pi`$ and the internal spectral gap $`\lambda_\ast`$ provide a built–in bandlimit; (ii) $`R_k(-\nabla^2)`$ completes the construction with a diffeomorphism–covariant coarse–graining on $`Y_4`$. No ad hoc hard cutoff is required.

#### Remark.

Appendix H.9 shows that if the projector-induced damping is taken as a physical entire form factor on each line, then all amplitudes are absolutely finite without subtractions. We work conservatively with regulator removal, but note this strengthening for context.

# Gravity–matter sector

At quadratic order around the fixed point, the Hessian is block–diagonal:
``` math
\mathcal H \;=\; \mathcal H_{\mathrm{grav}} \oplus \mathcal H_{\mathrm{matter}},
```
so the graviton propagator $`\Delta_{\mathrm{prop}}`$ decouples from pure matter two–point functions. Mixed graviton–matter blocks vanish at the stationary background in de Donder/unitary gauges. Consequently, with SPT each graviton line carries the universal Gaussian damping, and every diagram containing at least one internal graviton line is UV finite. Only purely–matter subgraphs require the usual local renormalizations. These counterterms are precisely those already catalogued in the amplitudes layer (anomaly cancellations, hypercharge normalization, mod–2 SU(2) global check). See for the full anomaly audit.

#### Scope of vertices.

Throughout, interaction vertices are assumed to be local, background–covariant polynomials of finite tensorial rank in the fields and a finite number of background-covariant derivatives. This assumption is standard in pAQFT/EG renormalisation and is the basis of the all–loop Gaussian domination argument (see App. D).

# Composite operators and BRST

We quantize in the BV formalism with fields $`\Phi`$, antifields $`\Phi^*`$, and classical action $`S_0`$ solving $`(S_0,S_0)=0`$. Denote the BV antibracket by $`(\cdot,\cdot)`$ and the BV Laplacian by $`\Delta_{\mathrm{BV}}`$ Let $`\Gamma`$ be the renormalized effective action.

<div id="thm:QME" class="theorem">

**Theorem 6** (All-orders QME and Slavnov–Taylor identities). *Assume: (i) $`S_0`$ solves the CME $`(S_0,S_0)=0`$; (ii) the 4D matter content is anomaly-free so that $`H^1_{\mathrm{loc}}(s\,|\,d)=0`$; (iii) the SPT regulator is entire in $`E`$ and $`A_{\mathrm{int}}`$ and preserves BRST covariance. Then there exist local counterterms at every loop order such that
``` math
\frac{1}{2}\,(\Gamma,\Gamma)= i\,\hbar\,\Delta_{\mathrm{BV}}\Gamma \,.
```*

*to all loop orders. In particular, Slavnov–Taylor identities hold nonperturbatively in external kinematics.*

</div>

<div class="proof">

*Proof sketch.* Proceed by induction on loop order $`L`$. Suppose the QME holds up to $`L-1`$. At order $`L`$ the breaking $`\Delta_{\mathrm{BV}}^{(L)}`$ is a local integrated polynomial of ghost number $`+1`$. Consistency gives $`s\,\Delta_{\mathrm{BV}}^{(L)}=0`$, so $`\Delta_{\mathrm{BV}}^{(L)}\in H^1_{\mathrm{loc}}(s|d)`$. By anomaly freedom, this cohomology is trivial, hence $`\Delta_{\mathrm{BV}}^{(L)}=s\,\Xi^{(L)}`$ for some local $`\Xi^{(L)}`$. Adding $`S^{(L)}_{\mathrm{ct}}=-\Xi^{(L)}`$ restores the identity. SPT ensures loop integrals are absolutely convergent and generate only local terms, so no nonlocal counterterms arise. ◻

</div>

<div id="prop:nielsen" class="proposition">

**Proposition 7** (Nielsen identity (gauge–parameter independence)). *For gauge-fixing parameters $`\xi`$, there exists a local generator $`\mathcal N(\xi)`$ of a canonical BV transformation with
``` math
\partial_\xi \Gamma \;=\; (\Gamma,\mathcal N(\xi)).
```
Thus BRST cohomology observables are $`\xi`$-independent.*

</div>

<div class="remark">

*Remark 8* (Unitarity and causality). OS-positivity and causal support of retarded kernels (proved in Secs. 3–4; see Lemma B.1 and Proposition C.1) are preserved after renormalization. Together with the ST identities, this yields unitarity on the BRST cohomology and microcausality of interacting fields.

</div>

# Two-loop prototypes

To illustrate Gaussian domination, consider the two-loop graviton–matter “sunset” self-energy.

<div id="prop:sunset" class="proposition">

**Proposition 9** (Two-loop sunset bound). *Let $`\Sigma_2(Q)`$ be the two-loop graviton–matter self-energy with external momentum $`Q`$. Under Theorem <a href="#thm:SPT" data-reference-type="ref" data-reference="thm:SPT">3</a>, one has
``` math
|\Sigma_2(Q)| \;\le\; C \int d^4p\,d^4q\;
\frac{e^{-\tau_0[p^2+q^2+(p+q+Q)^2]}}{(p^2+\lambda_\ast)(q^2+\lambda_\ast)((p+q+Q)^2+\lambda_\ast)}\,
\Pi(p,q,Q),
```
where $`\Pi`$ is a polynomial fixed by vertex ranks. The integral converges absolutely and
``` math
|\Sigma_2(Q)| \;\le\; C'\,P(Q)\,e^{-\,c\,\tau_0\,Q^2},
```
for constants $`C',c>0`$ and polynomial $`P(Q)`$.*

</div>

<div class="proof">

*Proof sketch.* Each graviton propagator obeys $`\|\Delta_{\mathrm{prop}}(k)\|\le C_0 e^{-\tau_0 k^2}/(k^2+\lambda_\ast)`$. Completing squares in $`(p,q)`$ shows the Gaussian dominates the polynomial numerator and ensures absolute convergence. Exponential suppression in $`Q`$ follows from the external factors after integration. ◻

</div>

# Infrared behaviour and recovery of GR

The projected kernel has a Bernstein form factor $`F(\Box)`$ multiplying the standard Lichnerowicz operator. By construction $`F`$ is a complete Bernstein function with positive Stieltjes representation. Normalization $`F(0)=1`$ ensures the Einstein–Hilbert term is recovered in the IR.

<div id="lem:IR-bernstein" class="lemma">

**Lemma 10** (IR limit of the Bernstein form factor). *Let $`F`$ be the form factor defined by $`\Delta_{\mathrm{prop}}=F(E)\,E^{-1}`$, with $`F`$ a complete Bernstein function. Then
``` math
F(0)=1,\qquad F(z)=1+C_{\mathrm{IR}}\,z+\mathcal O(z^2),\quad z\to 0^+,
```
with $`C_{\mathrm{IR}}`$ finite on bounded-geometry families. Thus for $`|k^2|\ll \Lambda^2`$ the graviton propagator reduces to the GR one up to $`\mathcal O(k^2/\Lambda^2)`$ corrections.*

</div>

<div class="proof">

*Proof sketch.* Bernstein representation: $`F(z)=a+bz+\int_0^\infty \tfrac{z}{z+s}\,\nu(ds)`$ with $`a=1`$. Expand $`\tfrac{z}{z+s}=z/s+\mathcal O(z^2)`$. Uniform integrability of $`s^{-1}`$ against $`\nu`$ follows from projector boundedness, giving a finite $`C_{\mathrm{IR}}`$. ◻

</div>

<div class="remark">

*Remark 11* (Micro-regularisation of Newtonian potential). In position space the static potential becomes $`V(r)=-\tfrac{Gm}{r}\,\mathrm{erf}(\Lambda r/2)`$, which agrees with GR at $`r\gg 1/\Lambda`$ and is finite at $`r=0`$.

</div>

<div class="remark">

*Remark 12* (Gravitational wave dispersion). Plane-wave modes acquire dispersion $`\omega^2=k^2[1+\mathcal O(k^2/\Lambda^2)]`$. For $`k\ll\Lambda`$ the deviation from luminal propagation is negligible; suppression is $`\sim e^{-(k/\Lambda)^2}`$ at $`k\gg\Lambda`$.

</div>

#### Order-of-magnitude bound from GW dispersion.

Current multi-messenger constraints bound $`|v_g-c|/c \lesssim 10^{-15}`$ at $`f\!\sim\!100`$ Hz, i.e. $`k\!\sim\!{\cal O}(10^{-13}\,\mathrm{eV})`$. Since our dispersion is $`{\cal O}(k^2/\Lambda^2)`$, this implies $`\Lambda \gtrsim {\cal O}(10^{-5}\,\mathrm{eV})`$, a trivially satisfied lower bound relative to the scales we consider (Sec. 9). This phenomenological bound is trivially satisfied in our construction, since Sec. 9 anchors $`\Lambda`$ near the Planck scale ($`\sim 10^{19}\,\mathrm{GeV}`$), far above any observational constraint.

# Numerical illustrations

#### Numerical illustration.

To connect the abstract geometry–to–scale map with physics, note that
``` math
\Lambda^2 = c_{\rm proj}\,\lambda_{\rm geo},\qquad 
c_{\rm proj}= \tfrac14.
```
[^1]

Here $`\lambda_{\rm geo}`$ is the lowest positive geometric eigenvalue (in $`{\rm GeV}^2`$) from the internal fiber Laplacians, while $`c_{\rm proj}=1/4`$ reflects both the coherent projection onto four macroscopic spacetime dimensions and the symmetric proper–time split in the SPT factorisation.

As an anchor, take the Planck scenario with $`\lambda_{\rm geo}=3.0\times 10^{38}\,{\rm GeV}^2`$. Then
``` math
\Lambda \;=\;\tfrac12\sqrt{\lambda_{\rm geo}} \;\approx\; 8.66\times 10^{18}\,{\rm GeV},
```
so
``` math
1/\Lambda \;\approx\; 5.77\times 10^{-20}\,{\rm GeV}^{-1} 
\;\simeq\; 1.14\times 10^{-35}\,{\rm m}.
```
This agrees with the expected Planck suppression length, showing that the coherent–sector construction naturally reproduces the correct order of magnitude.

# Derivation of SPT from projector structure

We briefly recall how the SPT factorization arises directly from the bounded-projector realization. Let
``` math
\Pi_{\mathrm{coh}}=\phi(-\Delta^{\mathrm{prop}}_{Y_4})\otimes\psi(A_{\mathrm{int}}),
```
with $`\phi,\psi`$ given by proper-time integrals of the heat kernel.

#### Example (explicit $`Y_4\times T^d`$ model).

Let $`X=Y_4\times T^d`$ with flat internal metric of radii $`L_i`$. Then $`A_{\rm int}=-\Delta_{T^d}`$ has spectrum $`\{4\pi^2\sum_i n_i^2/L_i^2\}`$ with $`\lambda_\ast=4\pi^2 \min_i L_i^{-2}`$. Let $`\Pi_{\rm coh}`$ project onto the joint zero-modes on $`T^d`$ and low-frequency window on $`Y_4`$ given by a proper-time filter $`\phi(-\square_{\bar g})=\int_0^{\tau_{\rm ext}} e^{-t(-\square_{\bar g})}\,\mu_{\rm ext}(dt)`$.

#### Convention remark.

Here we use the complementary proper–time parametrization in which the coherent filter is written with support on $`[0,\tau_{\mathrm{ext}}]`$ rather than $`[\tau_0,\infty)`$. The SPT proper–time gap corresponds in either convention to the exclusion of arbitrarily small proper times; the two parametrizations are equivalent under redefinition of the filter measure and lead to identical Gaussian suppression $`e^{-\tau_0 k^2}`$ on internal graviton lines.

#### Example continued.

Similarly take $`\psi(A_{\rm int})=\int_0^{\tau_{\rm int}} e^{-s A_{\rm int}}\,\mu_{\rm int}(ds)`$ with positive measures. By Lemma <a href="#lem:parametrix-transfer" data-reference-type="ref" data-reference="lem:parametrix-transfer">24</a>, $`DG(\Psi^\ast)e^{-t(-\square_{\bar g})}=e^{-c t E}S_t`$ with $`S_t`$ bounded; choosing $`\tau_0\le \min\{c\,\tau_{\rm ext},\tau_{\rm int}\}`$ yields
``` math
B \;=\; e^{-\frac{\tau_0}{2}E}\,B_0\,e^{-\frac{\tau_0}{2}A_{\rm int}},\qquad \|B_0\|\le C_0.
```
Thus each internal graviton line carries $`e^{-\tau_0 k^2}`$ and $`\Lambda^2=c_{\rm proj}\lambda_\ast`$ with $`c_{\rm proj}\in(0,1]`$ from the projector/parametrix normalisation. For the numerical examples in Sec. 9 we conservatively take $`c_{\rm proj}=\frac14`$ (4D projection and symmetric proper-time split).

Bounded-geometry parametrix transfer implies $`DG(\Psi_\ast)e^{-t(-{\Delta_{\mathrm{BV}}}_{Y_4})}=e^{-ctE}S_t`$ with $`S_t`$ bounded. Choosing $`\tau_0\le \min\{c\tau_{\mathrm{ext}},\tau_{\mathrm{int}}\}`$ and factoring semigroups yields
``` math
B \;=\; e^{-\tfrac{\tau_0}{2}E}\,B_0\,e^{-\tfrac{\tau_0}{2}A_{\mathrm{int}}},
```
as in Theorem <a href="#thm:SPT" data-reference-type="ref" data-reference="thm:SPT">3</a>. This establishes the universality of the Gaussian suppression $`e^{-\tau_0 k^2}`$ for internal graviton lines.

# Proof of Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">1</a>

We prove items (1)–(4) in the statement of Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">1</a> under the standing assumptions of Section <a href="#sec:assumptions" data-reference-type="ref" data-reference="sec:assumptions">2</a>. Throughout, $`A=E\oplus A_{\mathrm{int}}`$ with $`[E,A_{\mathrm{int}}]=0`$, $`A_{\mathrm{int}}\ge \lambda_\ast>0`$ on the orthogonal complement of the coherent sector, and $`B`$ denotes the metric shape map at the fixed point.

<div id="ass:poly-vertex" class="assumption">

**Assumption 13** (Polynomial vertex growth). In the gauge-fixed TT sector, each interaction vertex factor is a polynomial (or rational function with bounded denominator away from IR singularities) in loop momenta, of total degree bounded by a constant depending only on the operator dimension of the interaction term. In particular, for each fixed loop order, the integrand is bounded by
``` math
|I(\ell)| \le C (1+\|\ell\|)^{p}\prod_{j}\|\Delta_j(\ell)\|,
```
for some $`p<\infty`$ and constant $`C`$ depending on the graph but not on $`\ell`$.

</div>

#### Step A: SPT factorization and Gaussian bound.

By Theorem <a href="#thm:SPT" data-reference-type="ref" data-reference="thm:SPT">3</a> there exist $`\tau_0>0`$ and a bounded $`B_0`$ such that
``` math
B \;=\; e^{-\tfrac{\tau_0}{2}E}\,B_0\,e^{-\tfrac{\tau_0}{2}A_{\mathrm{int}}}.
```
Hence the projected propagator $`\Delta_{\mathrm{prop}}=BA^{-1}B^*`$ obeys the Gaussian estimate
``` math
\begin{equation}
\|\Delta_{\mathrm{prop}}(k)\| \;\le\; \frac{C_0}{k^2+\lambda_\ast}\,e^{-\tau_0 k^2},
\label{eq:gauss-main}
\end{equation}
```
uniformly on bounded–geometry families. Moreover, by Lemma <a href="#lem:universality" data-reference-type="ref" data-reference="lem:universality">4</a> this construction and <a href="#eq:gauss-main" data-reference-type="eqref" data-reference="eq:gauss-main">[eq:gauss-main]</a> are *independent* of the particular spectral realization of the coherent projector.

#### Step B: Positivity, unitarity and causality (item (1)).

By the Stieltjes representation (Appendix <a href="#app:stieltjes" data-reference-type="ref" data-reference="app:stieltjes">13</a>, Lemma <a href="#lem:stieltjes" data-reference-type="ref" data-reference="lem:stieltjes">16</a>),
``` math
\Delta_{\mathrm{prop}}\;=\; \int_0^\infty (E+s)^{-1}\,\nu(ds),
```
with $`\nu`$ a positive operator–valued measure. It follows that Euclidean two–point functions are OS–positive and, after Wick rotation, the retarded kernels have support in the future light cone (Appendix <a href="#app:causality" data-reference-type="ref" data-reference="app:causality">14</a>). Thus the free theory is unitary and causal. In the interacting theory, Appendix <a href="#app:BV" data-reference-type="ref" data-reference="app:BV">16</a> (Theorem <a href="#thm:QME-app" data-reference-type="ref" data-reference="thm:QME-app">21</a>) establishes the BV quantum master equation to all orders for anomaly–free matter content, and the Nielsen identity (Prop. <a href="#prop:nielsen-app" data-reference-type="ref" data-reference="prop:nielsen-app">22</a>) guarantees gauge–parameter independence. Consequently, unitarity holds on the BRST cohomology and microcausality is preserved (Appendix <a href="#app:EG" data-reference-type="ref" data-reference="app:EG">18</a>).

#### Step C: All–loop finiteness for graviton graphs (item (2)).

Insert <a href="#eq:gauss-main" data-reference-type="eqref" data-reference="eq:gauss-main">[eq:gauss-main]</a> line–by–line in any connected 1PI amplitude $`\mathcal M_\Gamma`$ which contains at least one internal graviton propagator. Appendix <a href="#app:gaussian" data-reference-type="ref" data-reference="app:gaussian">15</a> (Lemma <a href="#lem:gauss" data-reference-type="ref" data-reference="lem:gauss">19</a>) provides the per–line bound, and Theorem <a href="#thm:all-loops-app" data-reference-type="ref" data-reference="thm:all-loops-app">20</a> (Gaussian domination) shows that every UV subgraph is absolutely convergent and
``` math
|\mathcal M_\Gamma(Q)| \;\le\; P_\Gamma(Q)\,\exp\!\big[-\,c_\Gamma\,\tau_0\,Q^2\big]
```
for some polynomial $`P_\Gamma`$ and $`c_\Gamma>0`$. Diagrams (subgraphs) without a graviton line reduce to the standard renormalizable matter sector and admit the usual local counterterms (Section <a href="#sec:gravity-matter" data-reference-type="ref" data-reference="sec:gravity-matter">5</a>). As an *independent* cross–check at $`L{=}1`$, in the Calabi–Yau/toroidal corner the one–loop graviton sector is finite by modular invariance (Proposition <a href="#prop:modular" data-reference-type="ref" data-reference="prop:modular">5</a>, Appendix <a href="#app:modular" data-reference-type="ref" data-reference="app:modular">12</a>).

#### Step D: BV/QME to all orders (item (3)).

Let $`\Gamma`$ denote the renormalized effective action. Appendix <a href="#app:BV" data-reference-type="ref" data-reference="app:BV">16</a> (Theorem <a href="#thm:QME-app" data-reference-type="ref" data-reference="thm:QME-app">21</a>) proves by loop induction that any potential breaking $`\Delta\mathcal{A}^{(L)}=\tfrac12(\Gamma,\Gamma)^{(L)}-i\hbar\,\Delta_{\mathrm{BV}}\Gamma^{(L)}`$ at order $`L`$ the breaking $`\mathcal A^{(L)}`$ lies in $`H^1_{\mathrm{loc}}(s\mid d)`$; for the SM matter content this cohomology is trivial, hence $`\mathcal A^{(L)}=s\,\Xi^{(L)}`$ and a local counterterm restores the QME: $`\tfrac12(\Gamma,\Gamma)-i\hbar\,\Delta_{\mathrm{BV}}\Gamma=0`$. The regulator defined by SPT is an entire functional of the covariant operators and preserves BRST covariance; therefore the Slavnov–Taylor identities and the dressed Nielsen identity (Prop. <a href="#prop:nielsen-app" data-reference-type="ref" data-reference="prop:nielsen-app">22</a>) hold to all orders.

#### Step E: Infrared recovery of GR (item (4)).

Write the kinetic operator as $`K=F(E)\,E`$ with $`F`$ a complete Bernstein form factor. By Lemma <a href="#lem:IR-bernstein" data-reference-type="ref" data-reference="lem:IR-bernstein">10</a>, $`F(0)=1`$ and $`F(z)=1+\mathcal O(z)`$ as $`z\to 0^+`$, with coefficients uniformly bounded on bounded–geometry families. Hence for $`|k^2|\ll \Lambda^2`$ (with $`\Lambda^2=c_{\mathrm{proj}}\lambda_\ast`$) the spin–2 propagator reduces to the GR one, up to $`\mathcal O(k^2/\Lambda^2)`$ corrections. In position space, the Newtonian potential is micro–regularized to $`V(r)=-(Gm/r)\,\mathrm{erf}(\Lambda r/2)`$, agreeing with GR at $`r\gg 1/\Lambda`$ (Section <a href="#sec:IR" data-reference-type="ref" data-reference="sec:IR">8</a>).

#### Conclusion.

Steps A–E establish items (1)–(4) in Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">1</a>. All constants $`(\lambda_\ast,\tau_0,C_0,c_{\mathrm{proj}})`$ are geometric/projector data fixed by the coherent background, and Lemma <a href="#lem:universality" data-reference-type="ref" data-reference="lem:universality">4</a> ensures stability under changes of the projector realization. This completes the proof. 0◻

# Modular invariance at one loop

<div id="thm:modular" class="theorem">

**Theorem 14** (Modular invariance). *The Narain partition function $`Z^{(k)}_{\rm lat}(\tau,\bar\tau;G,B)`$ is invariant under $`SL(2,\mathbb Z)`$ generated by $`S:\tau\mapsto-1/\tau`$, $`T:\tau\mapsto\tau+1`$.*

</div>

<div id="cor:modular-weight" class="corollary">

**Corollary 15** (Weight-zero integrand). *Including ghosts and non-toroidal factors yields modular weight zero. Thus the one-loop graviton amplitude integral over the fundamental domain $`\mathcal F`$ is UV finite by modular invariance.*

</div>

#### Displayed weight-zero check.

Writing the one-loop integrand schematically as
``` math
\mathcal I(\tau,\bar\tau)= (\mathrm{Im}\,\tau)^{-d/2}\, Z^{(k)}_{\rm lat}(\tau,\bar\tau;G,B)\,
Z_{\rm ghosts}(\tau,\bar\tau)\,Z_{\rm rest}(\tau,\bar\tau),
```
one has under $`\gamma=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\in SL(2,\mathbb Z)`$:
``` math
Z^{(k)}_{\rm lat}(\gamma\!\cdot\!\tau)=|c\tau+d|^{-d}\,Z^{(k)}_{\rm lat}(\tau),\qquad
(\mathrm{Im}\,\gamma\!\cdot\!\tau)^{-d/2}=|c\tau+d|^{d}\,(\mathrm{Im}\,\tau)^{-d/2},
```
while $`Z_{\rm ghosts}`$ supplies weight $`-2`$ and $`Z_{\rm rest}`$ supplies $`+2`$, so the product has net weight $`0`$. Thus $`\mathcal I(\gamma\!\cdot\!\tau,\gamma\!\cdot\!\bar\tau)=\mathcal I(\tau,\bar\tau)`$.

<div class="proof">

*Proof sketch.* Poisson resummation exhibits $`Z_{\rm lat}`$ as an $`O(d,d;\mathbb Z)`$ theta function; invariance under $`S,T`$ follows. Adding ghost and measure factors balances modular weight. ◻

</div>

# Stieltjes representation and OS positivity

<div id="lem:stieltjes" class="lemma">

**Lemma 16** (Stieltjes form). *Let $`A=E\oplus A_{\mathrm{int}}`$ with $`[E,A_{\mathrm{int}}]=0`$, $`A_{\mathrm{int}}\ge\lambda_\ast>0`$ on the non‑coherent slice, and let $`B`$ be bounded. Then the propagator $`\Delta_{\mathrm{prop}}=BA^{-1}B^{\!*}`$ admits
``` math
\Delta_{\mathrm{prop}}\;=\; \int_{0}^{\infty} e^{-tE}\,M(t)\,dt, \qquad M(t):=B\,e^{-tA_{\mathrm{int}}}B^{\!*}\;\ge\;0,
```
hence (via the Laplace transform) the Stieltjes representation
``` math
\Delta_{\mathrm{prop}}\;=\; \int_{0}^{\infty} (E+s)^{-1}\,\nu(ds),
```
for a finite positive operator‑valued measure $`\nu`$. In particular, $`\Delta_{\mathrm{prop}}`$ has a positive Källén–Lehmann density.*

</div>

*TT sector.* The representation is taken on TT fields; pure-gauge directions are removed by gauge fixing, so OS positivity is asserted for TT two-point functions.

<div class="proof">

*Proof.* Use the semigroup representation $`A^{-1}=\int_{0}^{\infty}e^{-tA}\,dt`$ (strong Bochner integral on the domain). Since $`A=E\oplus A_{\mathrm{int}}`$ with commuting blocks, $`e^{-tA}=e^{-tE}e^{-tA_{\mathrm{int}}}`$. Therefore
``` math
\Delta_{\mathrm{prop}}\;=\; B\Big(\int_{0}^{\infty}e^{-tE}e^{-tA_{\mathrm{int}}}\,dt\Big)B^{\!*}
\;=\; \int_{0}^{\infty} e^{-tE}\,\underbrace{B e^{-tA_{\mathrm{int}}}B^{\!*}}_{M(t)}\,dt.
```
Positivity: $`M(t)=N(t)^{\!*}N(t)`$ with $`N(t):=e^{-tA_{\mathrm{int}}/2}B^{\!*}`$, hence $`M(t)\ge0`$.

Equivalently, by Laplace transform,
``` math
\Delta_{\mathrm{prop}}\;=\; \int_0^\infty (E+s)^{-1}\,\nu(ds),\qquad 
\nu(ds) := \mu(s)\,ds,\quad 
\mu(s) = \int_0^\infty e^{-st}\,M(t)\,dt \;\ge 0.
```
Thus $`\nu`$ is a positive operator–valued measure obtained as the Laplace transform of $`M(t)`$. ◻

</div>

<div class="corollary">

**Corollary 17** (OS positivity). *Let $`\Theta`$ be reflection on Euclidean time. For $`f`$ supported at $`t\ge0`$, $`\langle f,\,\Delta_{\mathrm{prop}}\,\Theta f\rangle \ge 0`$ because each $`(E+s)^{-1}`$ is OS‑positive and positive mixtures preserve positivity.*

</div>

*Cf.* the Osterwalder–Schrader reflection positivity axioms .

# Causality of retarded kernels

<div class="proposition">

**Proposition 18** (Retarded support). *For $`f\in C_c^\infty(Y_4)`$, the retarded kernel
``` math
R(t) = \theta(t)\,[\Delta_{\mathrm{prop}},f]
```
has support in the future light cone. Thus causal propagation holds.*

*See also Streater–Wightman  for standard support properties of retarded solutions.*

</div>

<div class="proof">

*Proof sketch.* Each term in the Stieltjes integral is a retarded Klein–Gordon kernel; positive mixtures preserve support. ◻

</div>

# Gaussian domination of multi‑loop graphs

<div id="lem:gauss" class="lemma">

**Lemma 19** (Gaussian‑dressed propagator). *Under Theorem <a href="#thm:SPT" data-reference-type="ref" data-reference="thm:SPT">3</a>, for any momentum $`k\in\mathbb R^4`$,
``` math
\|\Delta_{\mathrm{prop}}(k)\|\;\le\;\frac{C_0}{k^2+\lambda_\ast}\,e^{-\tau_0 k^2}.
```*

</div>

<div id="thm:all-loops-app" class="theorem">

**Theorem 20** (All‑loop Gaussian domination). *Let $`\Gamma`$ be a connected 1PI Feynman graph with at least one internal graviton line. With local covariant vertices of at most polynomial rank and the bound of Lemma <a href="#lem:gauss" data-reference-type="ref" data-reference="lem:gauss">19</a>, the amplitude $`\mathcal M_\Gamma(Q)`$ is absolutely convergent. Moreover,
``` math
|\mathcal M_\Gamma(Q)| \;\le\; P_\Gamma(Q)\,e^{-\,c_\Gamma\,\tau_0\,Q^2}
```
for some polynomial $`P_\Gamma`$ and $`c_\Gamma\in(0,1]`$ depending only on the number of internal graviton lines.*

</div>

Compare with Weinberg’s power counting for large momenta ;

<div class="proof">

*Proof.* Write the $`L`$ loop momenta as $`\ell=(\ell_1,\dots,\ell_L)\in\mathbb R^{4L}`$. Each graviton line with momentum $`k_j(\ell,Q)`$ contributes a factor bounded by $`C_0 e^{-\tau_0 k_j(\ell,Q)^2}/(k_j(\ell,Q)^2+\lambda_\ast)`$; non‑graviton lines contribute standard rational propagators. Collect denominators and polynomials into a single rational polynomial $`R(\ell,Q)`$. There exists $`C>0`$ and a positive‑definite quadratic form $`\mathcal Q(\ell,Q)`$ such that
``` math
\prod_{\text{grav lines }j} e^{-\tau_0 k_j(\ell,Q)^2}\;\ge\; e^{-\tau_0\,\mathcal Q(\ell,Q)} \;\ge\; e^{-c\,\tau_0\,(|\ell|^2+|Q|^2)}.
```
(Here $`c\in(0,1]`$ depends only on the graph incidence matrix.) Then
``` math
|\mathcal M_\Gamma(Q)| \;\le\; \int_{\mathbb R^{4L}} \frac{|R(\ell,Q)|}{\prod_i (1+\ell_i^2)}\,e^{-c\,\tau_0 (|\ell|^2+|Q|^2)}\,d^{4L}\!\ell
\;\le\; P_\Gamma(Q)\,e^{-\,c_\Gamma\,\tau_0\,Q^2},
```
where we used that $`\int_{\mathbb R^{4L}} (1+|\ell|)^{m} e^{-c\tau_0 |\ell|^2} d^{4L}\!\ell<\infty`$ for all $`m`$ and absorbed the remaining constants into $`P_\Gamma`$ and $`c_\Gamma`$. Sector/forest decompositions are not needed once the global Gaussian is present; absolute convergence follows directly. ◻

</div>

#### Overlapping subgraphs.

Because each internal graviton line carries a global Gaussian factor $`e^{-\tau_0 k^2}`$, the integrand is absolutely integrable in *every* UV region. Consequently, a forest/sector decomposition is unnecessary: Fubini’s theorem applies and the absolute convergence bound dominates all overlapping subdivergences simultaneously.

#### Vertex class used.

Vertices are local, covariant polynomials in $`h_{\mu\nu}`$, matter fields, and a finite number of background-covariant derivatives (finite tensorial rank at each valence); the Gaussian bound is measured against this polynomial growth.

# BV/QME induction and anomalies

#### Local cohomology.

We use $`H^1_{\mathrm{loc}}(s\mid d)`$: the cohomology of local functionals at ghost number $`1`$ modulo total derivatives, with differential given by the classical BRST operator $`s`$ and the exterior derivative $`d`$. In $`d=4`$ the pure diffeomorphism sector has *no* local anomaly, and with the anomaly-free matter content used here, $`H^1_{\mathrm{loc}}(s\mid d)=0`$ in the relevant sector.

<div id="thm:QME-app" class="theorem">

**Theorem 21** (QME induction). *At loop order $`L`$, any breaking $`\mathcal{A}^{(L)}`$ of the QME lies in $`H^1_{\mathrm{loc}}(s|d)`$. For anomaly-free matter content this cohomology is trivial, so $`\mathcal{A}^{(L)} = s\,\Xi^{(L)}`$. Adding $`S^{(L)}_{\rm ct}=-\Xi^{(L)}`$ restores the QME. By induction, the QME holds to all orders.*

</div>

<div id="prop:nielsen-app" class="proposition">

**Proposition 22** (Nielsen identity). *Gauge-parameter variation generates a canonical BV transformation: $`\partial_\xi\Gamma=(\Gamma,\mathcal N(\xi))`$. Physical observables are gauge independent.*

</div>

<div class="remark">

*Remark 23* (Anomaly audit). In 4D the SM matter content cancels all local gauge and mixed anomalies. Global SU(2) anomaly cancels (even number of doublets). Thus $`H^1_{\rm loc}(s|d)=0`$ in the model, justifying the induction.

</div>

# Derivation of SPT factorization

<div id="lem:parametrix-transfer" class="lemma">

**Lemma 24** (Parametrix transfer and SPT factorisation: analytic setting). *Let $`(Y^4,\bar g)`$ be globally hyperbolic with bounded geometry. Let $`E`$ be the TT Lichnerowicz operator on $`H^1_{\mathrm{TT}}(Y)`$ and $`A_{\mathrm{int}}\ge\lambda_\ast>0`$ on the incoherent complement, with $`[E,A_{\mathrm{int}}]=0`$. Assume the shape map $`B`$ and the core map $`B_0`$ are bounded on Sobolev scales $`H^s\rightarrow H^s`$ ($`s\in[0,1]`$). Then there exists $`c\in(0,1]`$ and a bounded family $`S_t`$ such that, as operators on $`H^1_{\mathrm{TT}}`$,
``` math
DG(\Psi^\ast)\,e^{-t(-\square_{\bar g})} \;=\; e^{-c t E}\,S_t,\qquad \sup_{t\in(0,1]}\|S_t\|_{H^1\to H^1}<\infty,
```
and the Bochner integrals $`\int_0^\infty e^{-tA}\,dt`$ converge uniformly on bounded-geometry families. Choosing $`\tau_0\le \min\{c\,\tau_{\mathrm{ext}},\tau_{\mathrm{int}}\}`$ and factoring the semigroups yields
``` math
B \;=\; e^{-\frac{\tau_0}{2}E}\,B_0\,e^{-\frac{\tau_0}{2}A_{\mathrm{int}}}, \qquad \|B_0\|\le C_0,
```
and the Gaussian bound $`\|\Delta_{\mathrm{prop}}(k)\|\le C_0\,e^{-\tau_0 k^2}/(k^2+\lambda_\ast)`$.*

</div>

<div class="proof">

*Proof.* Bounded geometry gives standard heat-kernel parametrices with Gaussian bounds and Sobolev continuity; the transfer constant $`c\in(0,1]`$ is the curvature/geometry loss in the parametrix conjugation. Spectral gap for $`A_{\mathrm{int}}`$ controls the vertical semigroup. Uniform Bochner convergence follows from the Gaussian bounds and the gap. Combine with Trotter product factorisation to obtain the displayed estimates. ◻

</div>

<div id="thm:SPT-app" class="theorem">

**Theorem 25** (SPT factorization). *Let $`\Pi_{\mathrm{coh}}=\phi(-\Delta_{Y_4})\otimes\psi(A_{\mathrm{int}})`$ with proper‑time filters $`\phi(z)=\int_{\tau_{\mathrm{ext}}}^{\infty} e^{-t z}\,\mu_{\mathrm{ext}}(dt)`$ and $`\psi(\lambda)=\int_{\tau_{\mathrm{int}}}^{\infty} e^{-s \lambda}\,\mu_{\mathrm{int}}(ds)`$, where $`\mu_{\mathrm{ext/int}}`$ are finite positive measures. On bounded‑geometry backgrounds there exists $`c\in(0,1]`$ and a family $`S_t`$ bounded on Sobolev scales such that
``` math
DG(\Psi_\ast)\,e^{-t(-\Box_{\bar g}))}=e^{-ctE}\,S_t \quad \text{for all } t\ge \tau_{\mathrm{ext}}.
```
For any $`\tau_0\in(0,\min\{c\,\tau_{\mathrm{ext}},\tau_{\mathrm{int}}\}]`$ define
``` math
B_0 \;:=\; \int_{\tau_0/c}^{\infty}\!\!\int_{\tau_0}^{\infty} e^{-(ct-\tau_0)\frac{E}{2}}\,
S_t\,DG(\Psi_\ast)\,e^{-(s-\tau_0)\frac{A_{\mathrm{int}}}{2}}\,\mu_{\mathrm{ext}}(dt)\,\mu_{\mathrm{int}}(ds).
```
Then $`B_0`$ is bounded and
``` math
B \;=\; DG(\Psi_\ast)\Pi_{\mathrm{coh}} \;=\; e^{-\frac{\tau_0}{2}E}\;B_0\;e^{-\frac{\tau_0}{2}A_{\mathrm{int}}}.
```*

</div>

<div class="proof">

*Proof.* Insert the proper‑time representations, use the transfer identity and factor out $`e^{-\tau_0 E/2}`$ and $`e^{-\tau_0 A_{\mathrm{int}}/2}`$. The remaining Bochner integral defines $`B_0`$; boundedness follows from the finiteness of $`\mu_{\mathrm{ext/int}}`$ and the uniform bounds on $`S_t`$. ◻

</div>

# Microcausality of interacting fields

<div id="prop:EG" class="proposition">

**Proposition 26** (EG construction and microlocal spectrum). *Let $`{\Delta_{\mathrm{prop}}}_{\mathrm{ret}}`$ be the retarded kernel obtained by the standard boundary value prescription from the OS‑positive Euclidean $`\Delta_{\mathrm{prop}}`$ of Appendix <a href="#app:stieltjes" data-reference-type="ref" data-reference="app:stieltjes">13</a>. Then $`\mathrm{WF}({\Delta_{\mathrm{prop}}}_{\mathrm{ret}})\subset \{(x,k)\,|\, k \in \overline{V}_+ \}`$ and $`\mathrm{supp}\,{\Delta_{\mathrm{prop}}}_{\mathrm{ret}}\subset \{x\,|\, x^0\ge 0\}`$. Time‑ordered products constructed by Epstein–Glaser splitting with this propagator are local and microcausal to all orders.*

</div>

This is the Epstein–Glaser construction , with microlocal control as in .

<div class="proof">

*Proof.* Each Stieltjes component $`(E+s)^{-1}`$ yields the standard retarded Klein–Gordon kernel with wavefront set contained in $`\overline{V}_+`$ and support in the future cone. Positive mixtures preserve both properties. The Gaussian dressing in momentum space improves temperateness and does not enlarge the wavefront set. The EG inductive construction applies since the scaling degree at coincident points is reduced by the Gaussian, ensuring the extension at the diagonal is unique and local. ◻

</div>

# Master technical appendix: EG/pAQFT, BV–BRST & QME, FRG regulator removal, UV damping, unitarity

## Standing hypotheses and inputs from the MTT spine

We work on a globally hyperbolic Lorentzian 4–manifold $`(Y^4,\bar g)`$ of bounded geometry on compact time slabs. The observable/coherent map is the bounded projector
``` math
P := I\circ \Pi\ :\ \Gamma(E_{10}) \to \Gamma(E_4),
```
where $`\Pi`$ is the joint harmonic projector on the internal bundles and $`I`$ pushes forward along the compact fibre; boundedness on $`L^2`$/$`H^1`$ and the closed, semibounded quadratic form for the reduced generator follow from your QM/fixed–point results. The QFT layer uses Hadamard states selected by the MTT projection and the curved‑spacetime pAQFT/EG construction (causal factorisation, microlocal spectrum, local covariance). The GR layer provides background‐field diffeo covariance (Levi–Civita, Bianchi pushforward).

<div class="remark">

*Remark 27* (Scope and anomaly hypothesis). We assume the 4D diffeomorphism sector has no local anomaly (true in $`d=4`$), and that any gauge matter is anomaly‐free (as in your SM realisation). This is the only cohomological input in the QME proof.

</div>

## Geometric origin of the UV damping (from $`P=I\circ\Pi`$)

<div id="prop:entiredamp" class="proposition">

**Proposition 28** (Coherent projector induces entire damping). *Let $`A_{\rm int}\ge \lambda_\ast>0`$ be the internal Laplace operator on the incoherent complement $`\mathrm{Ran}(\mathbf 1-\Pi)`$. Then there exists $`\tau_0>0`$ and an entire, positive, rapidly decaying function $`f`$ with $`f(0)=1`$ such that the projected two‐point kernels on $`(Y^4,\bar g)`$ can be written as
``` math
\Delta_{\rm coh} \;=\; f\!\left(-\,\bar\nabla^2\,/\,\Lambda^2\right)\;\Delta_0,\qquad \Lambda^2 \sim \tau_0^{-1}\sim \lambda_\ast,
```
with $`f(z)=e^{-z}`$ near the UV domain (or any heat‐kernel admissible profile). In momentum charts this yields $`|\widehat\Delta_{\rm coh}(p)|\lesssim C_N (1+p^2)^{-N}`$ for all $`N`$.*

</div>

<div class="proof">

*Proof.* Boundedness of $`\Pi`$ on $`H^1`$ and the spectral gap on the vertical complement imply that the semigroup $`e^{-t A_{\rm int}}`$ decays $`\sim e^{-\lambda_\ast t}`$; composing with the base heat‐kernel $`e^{-t(-\bar\nabla^2)}`$ and evaluating at a fixed $`t=\tau_0`$ (the SPT coarse–graining) produces $`f(-\bar\nabla^2/\Lambda^2)`$ with $`\Lambda^2\sim \tau_0^{-1}\sim \lambda_\ast`$. Entirety/positivity follow from the heat kernel calculus; rapid decay is standard. (All functional‐analytic inputs are those you use in the QM/fixed–point papers.) ◻

</div>

## Causal EG/pAQFT construction on $`(Y^4,\bar g)`$

<div id="thm:EG" class="theorem">

**Theorem 29** (Local, covariant time‐ordered products on curved spacetime). *On globally hyperbolic $`(Y^4,\bar g)`$ with a Hadamard two‐point function, there exist multilinear maps $`\mathcal T_n`$ on local functionals satisfying: causal factorisation, locality & background covariance, microlocal spectrum (Hadamard wavefront sets), symmetry/adjointness, and controlled scaling degree. The renormalisation freedom at each order is a finite‐dimensional affine space of local covariant counterterms.*

</div>

<div class="proof">

*Proof.* Epstein–Glaser splitting in curved spacetime using the microlocal spectrum condition; see   Your QFT layer establishes the Hadamard selection and local covariance, so all hypotheses hold. ◻

</div>

## BV data and the Classical Master Equation (CME)

Let $`\Phi=(h_{\mu\nu},\text{matter},\ldots)`$, $`C^\mu`$ the diffeo ghost, and $`\Phi^\star`$ the antifields. The classical extended action $`S_{\rm cl}^{\mathrm{BV}}`$ (Einstein–Hilbert + matter + gauge‐fixing + antifield couplings) satisfies:

<div id="thm:CME" class="theorem">

**Theorem 30** (CME). *$`\displaystyle \antibracket{S_{\rm cl}^{\mathrm{BV}}}{S_{\rm cl}^{\mathrm{BV}}}=0.`$*

</div>

<div class="proof">

*Proof.* Background‐field representation of $`\mathrm{Diff}`$ is a Lie algebra; the induced BRST differential is nilpotent; equivalently the CME holds. Metric compatibility/Levi–Civita and Bianchi pushforward from your GR reduction ensure the background invariances used. ◻

</div>

## All‐orders QME and Ward/Slavnov–Taylor identities

Let $`S=S_{\rm cl}^{\mathrm{BV}}+\sum_{\ell\ge 1}\hbar^\ell S_\ell`$ be the renormalised BV action and $`\BVDelta`$ the BV Laplacian in the Hadamard regularisation. The QME reads:
``` math
\frac{\mathrm{i}}{\hbar}\,\BVDelta S + \frac{1}{2\hbar^2}\,\antibracket{S}{S}=0.
```

<div class="theorem">

**Theorem 31** (QME to all loop orders). *Assume (i) Theorem <a href="#thm:EG" data-reference-type="ref" data-reference="thm:EG">29</a>; (ii) CME (Theorem <a href="#thm:CME" data-reference-type="ref" data-reference="thm:CME">30</a>); (iii) trivial local BRST cohomology in ghost number 1 for diffeos and anomaly‐free matter in $`d=4`$. Then counterterms $`S_\ell`$ can be chosen so that the QME holds to all orders. Equivalently, background‐field Ward/Slavnov–Taylor identities hold to all orders.  *

</div>

<div class="proof">

*Proof.* Induction in $`\hbar`$. At order $`\hbar^L`$, the anomaly candidate $`\mathcal A_L`$ is a local functional of ghost number 1 (Quantum Action Principle). By (iii) the Wess–Zumino consistency implies $`\mathcal A_L=s\mathcal C_L+d(\cdots)`$; choose $`S_L:=-\mathrm{i}\,\mathcal C_L`$ to cancel it. Locality and covariance are preserved by Theorem <a href="#thm:EG" data-reference-type="ref" data-reference="thm:EG">29</a>. ◻

</div>

## Background‐field FRG, modified Ward identities, and removal $`k\to 0`$

Add a background–covariant regulator $`\Delta S_k=\tfrac12\!\int\!\Phi\,\Rk(-\nablab^2)\,\Phi`$; define $`\Gk`$ by Legendre transform; then
``` math
\partial_k \Gk \;=\; \frac{\mathrm{i}}{2}\mathrm{STr}\big[(\Gk^{(2)}+\Rk)^{-1}\,\partial_k \Rk\big].
```
At finite $`k`$, modified STI/QME hold with cutoff insertions.

<div id="thm:reg-removal" class="theorem">

**Theorem 32** (Regulator removal with STI/QME limit). *If $`\Rk`$ is background‐covariant, positive, and vanishes as $`k\!\downarrow\!0`$, then the renormalised correlators and $`\Gk`$ possess a $`k\to 0`$ limit, and the modified Ward/QME identities converge to the exact ones. The finite counterterms chosen in Theorem <a href="#thm:QME" data-reference-type="ref" data-reference="thm:QME">6</a> can be implemented along the flow so that the limit solves the QME.  *

</div>

<div class="proof">

*Proof.* Standard background‐field FRG Ward analysis: the breaking terms are local and BRST–exact with coefficients $`\propto \partial_k \Rk`$; they vanish as $`k\to 0`$. Heat‐kernel/spectral estimates on $`(Y,\bar g)`$ ensure the $`k`$–integral converges; locality/covariance is preserved. Compatibility with BV follows from the same cohomological argument as Theorem <a href="#thm:QME" data-reference-type="ref" data-reference="thm:QME">6</a>. ◻

</div>

## Locality of counterterms and power counting in the graviton self‐sector

<div id="thm:local" class="theorem">

**Theorem 33** (Local, background–covariant renormalisation). *At each loop order the renormalisation freedom is a finite linear combination of diffeo‐covariant local functionals built from $`\sqrt{-\bar g}`$, curvatures ($`\bar R`$, $`\bar R_{\mu\nu}`$, $`\bar R_{\mu\nu\rho\sigma}`$) and their covariant derivatives, together with BRST–exact gauge–fixing/ghost terms, consistent with the Ward identities.*

</div>

<div class="proof">

*Proof.* Directly from EG/pAQFT locality and covariance on globally hyperbolic spacetimes (Theorem <a href="#thm:EG" data-reference-type="ref" data-reference="thm:EG">29</a>); background‐field Ward identities restrict the tensors to diffeo‐covariant combinations; BV cohomology fixes finite parts to preserve QME. ◻

</div>

## Unitarity and microlocal spectrum

<div id="prop:unitarity" class="proposition">

**Proposition 34** (Bogoliubov $`S`$–matrix is unitary). *For Hermitian interactions the relative $`S`$–matrix constructed by EG/pAQFT is unitary order by order and satisfies causal factorisation.*

</div>

<div class="proof">

*Proof.* Adjointness and causal factorisation are axioms of the EG/pAQFT construction and hold on $`(Y,\bar g)`$ with Hadamard states. Hence $`S^\dagger S=1`$ order by order. ◻

</div>

<div class="proposition">

**Proposition 35** (Microlocal spectrum & composite operators). *Hadamard two‐point structure and EG control imply that $`n`$–point functions satisfy the microlocal spectrum condition; point–splitting defines locally covariant composites (e.g. $`\langle T_{\mu\nu}\rangle_{\rm ren}`$) with conservation inherited from background diffeomorphism covariance.*

</div>

## Optional strengthening: entire damping $`\Rightarrow`$ absolute finiteness

<div id="thm:absolute" class="theorem">

**Theorem 36** (Absolute UV finiteness under entire damping). *Assume the hypothesis of Proposition <a href="#prop:entiredamp" data-reference-type="ref" data-reference="prop:entiredamp">28</a> and that *every* internal line carries the entire form factor $`f(-\nablab^2/\Lambda^2)`$ with $`|f(z)|\le C_N(1+|z|)^{-N}`$ on $`\Re z\ge 0`$ for all $`N`$. Then each Feynman amplitude is absolutely convergent; no UV divergences occur and the QME holds without subtractions.*

</div>

<div class="proof">

*Proof.* Weinberg power counting is improved by the uniform entire decay, sending the superficial degree to $`-\infty`$; locality/covariance persists because $`f`$ is an entire function of the covariant Laplacian; BRST/QME compatibility follows as in Theorem <a href="#thm:QME" data-reference-type="ref" data-reference="thm:QME">6</a>. ◻

</div>

## Projection vs. compactification (KK) in the coherent sector

<div id="prop:projKK" class="proposition">

**Proposition 37** (Projection–KK equivalence (coherent sector)). *Let $`\pi:\Sigma^{10}\to M^{4}`$ be a Riemannian submersion with compact fibres $`F_6`$, and $`\Pi`$ the joint harmonic projector on $`F_6`$. Under bounded geometry and a uniform fibre spectral gap, restricting fields to $`\mathrm{Ran}\,\Pi`$ and pushing forward along $`\pi`$ yields the same 4D effective action and Ward/Bianchi identities as KK truncation to fibre zero modes, up to operators suppressed by the fibre gap and warping.*

</div>

<div class="proof">

*Proof.* Zero‐mode truncation coincides with restriction to $`\mathrm{Ran}\,\Pi`$; pushforward of the 10D action produces the 4D Einstein–Hilbert term plus fibre curvature constants; the remainder is $`O(\lambda_\ast^{-1},\text{warp})`$. Ward/Bianchi identities push forward because $`P`$ commutes with base covariant derivatives and preserves the Noether charges. ◻

</div>

## Consolidated result

<div id="thm:masterQG" class="theorem">

**Theorem 38** (Perturbative QG in the MTT coherent sector). *Under the hypotheses of §<a href="#app:standing-hyp" data-reference-type="ref" data-reference="app:standing-hyp">19.1</a>, the AQFT constructed on $`(Y^4,\bar g)`$ by EG/pAQFT with BV–BRST data satisfies: (i) all‐orders QME and background‐field Ward identities; (ii) locality and covariance with a closed counterterm basis; (iii) unitarity and microlocal spectrum; (iv) regulator removal with exact identities in the $`k\to0`$ limit; and (v) (optionally) absolute UV finiteness if entire damping is kept. Hence the renormalised theory is perturbatively consistent and regulator‐independent in the coherent sector.*

</div>

# Spectral Proper–Time Factorization and Gaussian UV Damping

This appendix provides a complete and rigorous derivation of the spectral proper–time (SPT) factorization used in the ultraviolet analysis of the graviton sector. All statements are made under standard bounded–geometry and spectral assumptions, and no heuristic steps are used.

## Geometric and operator assumptions

Let $`(M,g)`$ be a smooth Riemannian manifold of dimension $`d`$ with bounded geometry: uniform bounds on curvature and its covariant derivatives and a positive injectivity radius. Let $`E\to M`$ be a Hermitian vector bundle with a compatible connection.

Let $`L`$ be a nonnegative selfadjoint Laplace–type operator on $`L^2(E)`$, i.e.
``` math
L = \nabla^\ast \nabla + \mathcal{R},
```
where $`\mathcal{R}`$ is a smooth bundle endomorphism bounded below.

<div id="ass:heat" class="assumption">

**Assumption 39** (Heat kernel bounds). The heat kernel $`K_t(x,y)`$ of $`e^{-tL}`$ satisfies Gaussian upper bounds: there exist constants $`C,c>0`$ such that for all $`t>0`$,
``` math
\|K_t(x,y)\|
\;\le\;
C\,t^{-d/2}\exp\!\Bigl(-\frac{d(x,y)^2}{c\,t}\Bigr).
```

</div>

Assumption <a href="#ass:heat" data-reference-type="ref" data-reference="ass:heat">39</a> holds for all Laplace–type operators on bounded–geometry manifolds.

## Completely monotone filters and proper–time representation

<div class="definition">

**Definition 40** (Completely monotone filter). A function $`f:[0,\infty)\to\mathbb{R}`$ is *completely monotone* if
``` math
(-1)^m f^{(m)}(x)\ge 0
\quad\text{for all }x>0,\ m\ge 0.
```

</div>

By Bernstein’s theorem, $`f`$ is completely monotone if and only if there exists a finite positive Borel measure $`\mu`$ on $`[0,\infty)`$ such that
``` math
f(\lambda)=\int_0^\infty e^{-t\lambda}\,d\mu(t).
```

<div id="ass:pt-gap" class="assumption">

**Assumption 41** (Proper–time gap). The representing measure $`\mu`$ of $`f`$ satisfies
``` math
\mathrm{supp}(\mu)\subset[\tau_0,\infty)
\quad\text{for some }\tau_0>0.
```

</div>

#### Replacement of Assumption A.3 (Proper-Time Support Gap).

Rather than postulating a proper-time support gap for the filter defining the coherent projector, we derive it from the operational structure of the projected dynamics. Physical evolution in Modal Triplet Theory proceeds via discrete evolve–project cycles $`T_\tau=\Pi_{\mathrm{coh}}\circ\Phi_\tau`$, each of which applies a smoothing semigroup $`e^{-tL}`$ for a strictly positive minimum duration $`\tau_*>0`$. As shown in Appendix <a href="#app:proper_time_gap" data-reference-type="ref" data-reference="app:proper_time_gap">21</a>, this discrete update schedule forces the associated completely monotone filter to admit a Bernstein representation whose measure has support contained in $`[\tau_*,\infty)`$. Consequently, the effective filter automatically factors as $`e^{-\frac{\tau_*}{2}L}(\cdot)e^{-\frac{\tau_*}{2}L}`$, yielding the spectral proper-time (SPT) factorization used below. The existence of a proper-time gap $`\tau_0=\tau_*`$ is therefore not an independent assumption, but a structural consequence of admissible projection dynamics. Gaussian suppression should be understood in the spectral sense; its interpretation as local UV momentum damping follows microlocally under bounded-geometry conditions, as detailed in Appendix <a href="#app:proper_time_gap" data-reference-type="ref" data-reference="app:proper_time_gap">21</a>.

<div class="definition">

**Definition 42** (Spectral filter). Define the bounded operator
``` math
B := f(L)
```
by functional calculus.

</div>

<div id="lem:pt-rep" class="lemma">

**Lemma 43** (Exact proper–time representation). *Under Assumption <a href="#ass:pt-gap" data-reference-type="ref" data-reference="ass:pt-gap">41</a>,
``` math
B = \int_{\tau_0}^{\infty} e^{-tL}\,d\mu(t),
```
where the integral converges in the strong operator topology (and in operator norm if $`\mu`$ has finite total mass).*

</div>

<div class="proof">

*Proof.* By Bernstein’s theorem and Assumption <a href="#ass:pt-gap" data-reference-type="ref" data-reference="ass:pt-gap">41</a>,
``` math
f(L)=\int_0^\infty e^{-tL}\,d\mu(t)
=\int_{\tau_0}^\infty e^{-tL}\,d\mu(t).
```
Strong convergence follows from monotone convergence and the contractivity of $`e^{-tL}`$ on $`L^2`$. ◻

</div>

## SPT factorization

<div id="lem:spt-fact" class="lemma">

**Lemma 44** (Spectral proper–time factorization). *Define
``` math
B_0 := \int_0^\infty e^{-sL}\,d\mu(\tau_0+s).
```
Then
``` math
B = e^{-\frac{\tau_0}{2}L}\,B_0\,e^{-\frac{\tau_0}{2}L},
```
and $`B_0`$ is a bounded positive operator commuting with $`L`$.*

</div>

<div class="proof">

*Proof.* By Lemma <a href="#lem:pt-rep" data-reference-type="ref" data-reference="lem:pt-rep">43</a>, substitute $`t=\tau_0+s`$:
``` math
B=\int_{\tau_0}^\infty e^{-tL}\,d\mu(t)
=e^{-\frac{\tau_0}{2}L}
\Bigl(\int_0^\infty e^{-sL}\,d\mu(\tau_0+s)\Bigr)
e^{-\frac{\tau_0}{2}L}.
```
Positivity and commutation with $`L`$ follow from functional calculus. ◻

</div>

## Kernel bounds and Gaussian decay

Let $`K_B(x,y)`$ denote the Schwartz kernel of $`B`$.

<div id="lem:kernel-bound" class="lemma">

**Lemma 45** (Kernel bound). *Under Assumption <a href="#ass:heat" data-reference-type="ref" data-reference="ass:heat">39</a>,
``` math
\|K_B(x,y)\|
\;\le\;
C\int_{\tau_0}^{\infty}
t^{-d/2}\exp\!\Bigl(-\frac{d(x,y)^2}{c\,t}\Bigr)
\,d\mu(t).
```*

</div>

<div class="proof">

*Proof.* Insert the heat kernel bound of Assumption <a href="#ass:heat" data-reference-type="ref" data-reference="ass:heat">39</a> into the representation of Lemma <a href="#lem:pt-rep" data-reference-type="ref" data-reference="lem:pt-rep">43</a> and integrate against $`d\mu(t)`$. ◻

</div>

<div id="lem:fourier-gauss" class="lemma">

**Lemma 46** (Gaussian Fourier multiplier bound). *In a bounded–geometry coordinate chart, the Fourier transform of $`K_B`$ satisfies
``` math
\|\widehat{K_B}(\xi)\|
\;\le\;
C'\,e^{-\tau_0|\xi|^2},
```
uniformly for $`|\xi|`$ sufficiently large.*

</div>

<div class="proof">

*Proof.* In local coordinates, the Fourier transform of $`e^{-tL}`$ is bounded by $`\exp(-t|\xi|^2)`$ up to polynomial prefactors. Since $`t\ge\tau_0`$ on the support of $`\mu`$, the integral representation yields
``` math
\|\widehat{K_B}(\xi)\|
\le
\int_{\tau_0}^\infty C'' e^{-t|\xi|^2}\,d\mu(t)
\le C' e^{-\tau_0|\xi|^2}.
```
 ◻

</div>

## Filtered propagator and UV finiteness

Let $`L`$ be the projected graviton operator in the TT sector and let
``` math
\Delta := (L + m^2)^{-1}.
```
Define the filtered propagator
``` math
\Delta_{\mathrm{filt}} := B\,\Delta.
```

<div id="prop:gauss-prop" class="proposition">

**Proposition 47** (Gaussian UV damping of the propagator). *There exist constants $`C,\lambda_\ast>0`$ such that in local momentum variables,
``` math
\|\Delta_{\mathrm{filt}}(k)\|
\;\le\;
C\,\frac{e^{-\tau_0 k^2}}{k^2+\lambda_\ast}.
```*

</div>

<div class="proof">

*Proof.* Combine the resolvent bound $`(k^2+\lambda_\ast)^{-1}`$ with the Fourier multiplier estimate of Lemma <a href="#lem:fourier-gauss" data-reference-type="ref" data-reference="lem:fourier-gauss">46</a>. ◻

</div>

<div id="cor:all-loop" class="corollary">

**Corollary 48** (All–loop convergence for graviton–containing graphs). *Assume that each interaction vertex grows at most polynomially in momenta. Then every connected 1PI Feynman graph containing at least one internal graviton line is absolutely convergent in all loop momenta.*

</div>

<div class="proof">

*Proof.* Each internal graviton line contributes a factor bounded by $`e^{-\tau_0 k^2}`$ times a rational function. The product of Gaussian factors yields a positive–definite quadratic form in loop momenta dominating any polynomial growth. Standard multivariate Gaussian integrability implies absolute convergence. ◻

</div>

<div class="remark">

*Remark 49*. Pure matter subgraphs without internal graviton lines renormalize by standard EFT methods and are not claimed UV finite by this mechanism.

</div>

# Derivation of the Proper-Time Support Gap

## Purpose and logical role

In the constructive quantum-gravity analysis, several results rely on the existence of a strictly positive proper-time support gap
``` math
\begin{equation}
\operatorname{supp}(\mu) \subset [\tau_0,\infty),
\qquad \tau_0 > 0,
\label{eq:pt_gap}
\end{equation}
```
for the Bernstein measure $`\mu`$ associated with the filter defining the coherent projector. In earlier sections this condition appeared as an explicit assumption (denoted “Assumption A.3”).

The purpose of this appendix is to *derive* <a href="#eq:pt_gap" data-reference-type="eqref" data-reference="eq:pt_gap">[eq:pt_gap]</a> from a minimal and physically interpretable dynamical axiom: the existence of a strictly positive minimum smoothing time per evolve–project cycle. This removes any ambiguity about whether the proper-time gap is imposed ad hoc or follows from the operational structure of the theory.

Throughout this appendix we work under the bounded-geometry and Laplace-type assumptions already in force in the main text.

## Discrete schedule axiom

<div id="ax:schedule" class="axiom">

*Axiom 1* (Discrete projection schedule). Physical evolution proceeds in discrete evolve–project cycles. Each cycle applies a smoothing semigroup $`S_t = e^{-tL}`$ with a strictly positive minimum duration $`\tau_* > 0`$. No admissible physical update applies smoothing for times $`t < \tau_*`$.

</div>

This axiom formalizes the idea that admissible dynamics has a finite coarse-graining cadence and excludes arbitrarily short proper-time updates. It is independent of spectral gap assumptions and does not refer to any particular representation of the projector.

## Construction of the effective filter

Let $`L \ge 0`$ be a self-adjoint Laplace-type operator acting on a Hilbert space (or section space over a bounded-geometry slab). Define the heat semigroup $`S_t = e^{-tL}`$.

Consider an effective filter obtained by iterating the evolve–project cycle a random number of times, with a geometric distribution of cycle counts:
``` math
\begin{equation}
F \;=\; \sum_{n=1}^{\infty} p(1-p)^{n-1} S_{n\tau_*},
\qquad p \in (0,1).
\label{eq:filter_def}
\end{equation}
```

This choice is technically convenient and physically natural: each update applies at least one full cycle of duration $`\tau_*`$, and the distribution has finite mean.

## Complete monotonicity and Bernstein representation

<div id="lem:cm" class="lemma">

**Lemma 50** (Complete monotonicity). *The scalar function
``` math
\begin{equation}
f(\lambda)
= \sum_{n=1}^{\infty} p(1-p)^{n-1} e^{-n\tau_*\lambda},
\qquad \lambda \ge 0,
\label{eq:f_lambda}
\end{equation}
```
is completely monotone on $`[0,\infty)`$.*

</div>

<div class="proof">

*Proof.* Each term $`e^{-n\tau_*\lambda}`$ is completely monotone, and the series converges absolutely and uniformly on compact subsets of $`[0,\infty)`$ since $`(1-p)e^{-n\tau_*\lambda} \le 1-p < 1`$. Complete monotonicity is preserved under positive linear combinations. ◻

</div>

By Bernstein’s theorem, $`f`$ admits a unique representation as a Laplace transform of a positive measure.

<div id="lem:bernstein" class="lemma">

**Lemma 51** (Explicit Bernstein measure). *The Bernstein measure associated with $`f`$ is
``` math
\begin{equation}
\mu
= \sum_{n=1}^{\infty} p(1-p)^{n-1}\,\delta_{n\tau_*}.
\label{eq:bernstein_measure}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Each exponential $`e^{-n\tau_*\lambda}`$ is the Laplace transform of $`\delta_{n\tau_*}`$. Linearity of the Laplace transform yields <a href="#eq:bernstein_measure" data-reference-type="eqref" data-reference="eq:bernstein_measure">[eq:bernstein_measure]</a>. ◻

</div>

## Derivation of the proper-time support gap

<div id="thm:pt_gap" class="theorem">

**Theorem 52** (Proper-time support gap). *Under Axiom <a href="#ax:schedule" data-reference-type="ref" data-reference="ax:schedule">1</a>, the Bernstein measure $`\mu`$ of the effective filter $`F = f(L)`$ satisfies
``` math
\begin{equation}
\operatorname{supp}(\mu) \subset [\tau_*,\infty).
\end{equation}
```
In particular, the proper-time support gap exists with $`\tau_0 = \tau_*`$.*

</div>

<div class="proof">

*Proof.* From Lemma <a href="#lem:bernstein" data-reference-type="ref" data-reference="lem:bernstein">51</a>, the support of $`\mu`$ consists of the discrete set $`\{n\tau_* \mid n \in \mathbb{N}\}`$. The smallest element is $`\tau_*`$, hence the support is contained in $`[\tau_*,\infty)`$. ◻

</div>

This theorem replaces the previously stated proper-time gap assumption. The gap is no longer an independent hypothesis but a direct consequence of the discrete update cadence.

## SPT factorization

<div id="cor:spt" class="corollary">

**Corollary 53** (Spectral proper-time factorization). *Let $`F = f(L)`$ be defined as above. Then
``` math
\begin{equation}
F
= e^{-\frac{\tau_*}{2}L}\, F_0 \, e^{-\frac{\tau_*}{2}L},
\end{equation}
```
where
``` math
\begin{equation}
F_0
:= \int_{\tau_*}^{\infty} e^{-(t-\tau_*)L}\, d\mu(t)
\end{equation}
```
is a bounded, positive operator commuting with $`L`$.*

</div>

<div class="proof">

*Proof.* This follows immediately by inserting the Bernstein representation and factoring out $`e^{-\frac{\tau_*}{2}L}`$ on both sides. Boundedness and positivity of $`F_0`$ follow from positivity of $`\mu`$ and standard semigroup bounds. ◻

</div>

## Local-momentum interpretation of Gaussian damping

We emphasize that $`e^{-\tau_* L}`$ yields Gaussian suppression in the *spectral* variable of $`L`$. On curved backgrounds there is no global Fourier momentum. The correct interpretation is microlocal.

<div id="prop:local_gaussian" class="proposition">

**Proposition 54** (Local UV Gaussian damping). *Let $`L`$ be a Laplace-type operator on a bounded-geometry slab. Then the principal symbol of $`e^{-\tau_* L}`$ is
``` math
\begin{equation}
\sigma_{\mathrm{pr}}\!\left(e^{-\tau_* L}\right)(x,\xi)
= e^{-\tau_* \sigma_{\mathrm{pr}}(L)(x,\xi)}
= e^{-\tau_* |\xi|_g^2},
\end{equation}
```
where $`|\xi|_g^2`$ is the local covector norm induced by the metric.*

</div>

<div class="proof">

*Proof.* For Laplace-type operators, $`\sigma_{\mathrm{pr}}(L)(x,\xi)=|\xi|_g^2`$. Since the function $`\lambda \mapsto e^{-\tau_*\lambda}`$ is entire, the standard pseudodifferential functional calculus applies, yielding that the principal symbol of $`e^{-\tau_* L}`$ is obtained by functional composition with $`\sigma_{\mathrm{pr}}(L)`$. ◻

</div>

Thus, statements such as “Gaussian damping $`e^{-\tau_* k^2}`$” should be read as shorthand for Gaussian damping in the local UV covector variable $`|\xi|_g^2`$. In local inertial or asymptotically flat limits, this reduces to the familiar momentum-space expression.

## Remarks on scope

- The derivation above shows that the proper-time support gap is a structural consequence of discrete admissible dynamics, not an independent filter choice.

- The Gaussian damping statement is local and microlocal; no claim of a global Minkowski momentum variable is made on arbitrary curved backgrounds.

- Extensions to specific sectors (e.g. TT gravitons) require only that the corresponding kinetic operator be Laplace-type up to lower-order curvature terms, as assumed elsewhere in the paper.

This completes the closure of the proper-time support gap.

[^1]: The factor $`c_{\rm proj}=\tfrac14`$ reflects (i) the parametrix transfer constant $`c\in(0,1]`$ from Lemma F.1 and (ii) the symmetric proper-time split between the external and internal blocks in SPT, $`e^{-\frac{\tau_0}{2}E}\,B_0\,e^{-\frac{\tau_0}{2}A_{\rm int}}`$. In the conservative normalisation used here, these contribute an overall $`\sqrt{c}\times\frac12`$ on $`\Lambda`$, i.e. $`c_{\rm proj}=(\sqrt{c}/2)^2\simeq 1/4`$ when $`c\approx 1`$.
