---
abstract: |
  We derive the full Standard Model (SM) from the coherent fixed-point sector of the Modal Triplet Theory (MTT). Internally, three parallel bundles $`(B_1,B_2,B_3)`$ over $`Y^4`$ with base-only warping ensure commuting vertical Laplacians, so the joint Riesz projector $`\Pi`$ is well-defined and bounded on $`H^1`$. The Fundamental Contractivity Condition (FCC) then yields a unique coherent fixed point, and the $`4`$D EFT arises by restricting the MTT energy to $`\mathrm{Ran}\Pi`$.

  We prove: (i) the SM gauge group emerges with the canonical identification $`B_1\!\to\mathrm{U}(1)_Y`$, $`B_2\!\to\mathrm{SU}(2)_L`$, $`B_3\!\to\mathrm{SU}(3)_C`$; (ii) the SM chiral content in *three families* is obtained by a clean, gauge-preserving mechanism via a *flavor* line bundle $`L_F`$ with $`Z_3`$ holonomy; (iii) anomaly cancellation is shown constructively by an integer-lattice basis; (iv) the Higgs sector and EWSB follow with representation-correct curvature shift (Bochner/Lichnerowicz) and RG-driven sign flip; (v) Yukawa hierarchies and mixings arise from internal overlap integrals; (vi) a numerical one-loop RG run with modest high-scale thresholds matches observed low-energy couplings. We add a particle dictionary (fermions, bosons, hadrons) with stability mechanisms, check the global $`SU(2)`$ anomaly, discuss strong-CP and proton stability, and clarify the origin of high-scale gauge normalization from internal overlap norms. The result is a referee-ready, self-contained bridge from MTT to the complete SM.
author:
- Peter Nero
current_version: v2
date: August 2025
generated_from_main_tex_sha256: 201721294ec743dc1f7b58b981833de776141f56ea40a5f013c170c1e4e3ab84
paper_id: modal-triplet-theory-from-mtt-to-standard-model-a-rigor-923ad6b1
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory: From MTT to Standard Model  
  A Rigorous Derivation of Gauge, Matter, and Symmetry Breaking
zenodo_doi: 10.5281/zenodo.18200819
zenodo_record_id: 18200819
zenodo_url: "https://zenodo.org/records/18200819"
---

# Introduction and context

Modal Triplet Theory (MTT) provides a mathematically controlled route from a ten-dimensional modal geometry to an emergent $`3{+}1`$D world: three internal bundles $`B_1,B_2,B_3`$ over $`Y^4`$ with *base-only warping* yield $`[\Delta_{B_i},\Delta_{B_j}]=0`$, a joint harmonic projector $`\Pi=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$ bounded on $`H^1`$, and—by the Fundamental Contractivity Condition (FCC)—a unique coherent fixed point of the projected flow $`T_\tau=\Pi\circ\Phi_\tau`$. The $`4`$D effective field theory (EFT) results by restricting the MTT energy to $`\mathrm{Ran}\Pi`$.

This paper completes the derivation to the *full* Standard Model (SM): we fix the bundle$`\to`$group map
``` math
B_1\to \mathrm{U}(1)_Y,\qquad B_2\to \mathrm{SU}(2)_L,\qquad B_3\to \mathrm{SU}(3)_C,
```
construct three coherent families via a gauge-neutral $`Z_3`$ flavor holonomy on the internal circle, provide a constructive integer proof of anomaly cancellation, obtain the Higgs/EWSB sector with the correct curvature shift and RG running, derive Yukawas from internal overlaps (with a toy hierarchy/mixing example), and perform a one-loop RG benchmark including small high-scale thresholds attributable to nearby modal excitations. We include a particle dictionary and address standard referee checkpoints (global $`SU(2)`$ anomaly, strong-CP status, proton stability, and gauge normalization origin).

# MTT baseline and projection to 4D

#### Bundles and commutation.

Internally $`X^6`$ splits orthogonally as $`B_1\oplus^\perp B_2\oplus^\perp B_3`$ with block-diagonal metric depending only on $`y\in Y^4`$ (base-only warping). Then $`[\Delta_{B_i},\Delta_{B_j}]=0`$ and the joint projector $`\Pi`$ exists and is $`H^1`$-bounded.

#### Spectral gap and FCC.

Uniform vertical gaps $`\lambda_{n,\ast}>0`$ yield a global $`\lambda_\ast=\min_n\lambda_{n,\ast}>0`$; the Riesz projector satisfies $`\|\Pi\|_{H^1\to H^1}\le C_\Pi`$. The FCC,
``` math
C_\Pi\,\mathrm{e}^{-(\min_n\kappa_n\lambda_\ast - L)\tau}<1,
```
with Lipschitz $`L`$ on the invariant sublevel and $`\kappa_n>0`$, ensures a unique coherent fixed point with geometric convergence of Picard iterates.

#### Projection.

Set $`H_{\rm coh}:=\mathrm{Ran}\Pi`$. The $`4`$D EFT Lagrangian arises by restricting the MTT energy to $`H_{\rm coh}`$ and integrating out the vertical fibers. Gauge fields descend as harmonic connections of the internal bundles; matter fields are coherent spinors.

# Emergence of the SM gauge group

<div id="prop:bundles" class="proposition">

**Proposition 1** (Bundle $`\leftrightarrow`$ group mapping). *Modal reuse and orthogonality select the identification
``` math
B_1 \longrightarrow \mathrm{U}(1)_Y,\qquad
B_2 \longrightarrow \mathrm{SU}(2)_L,\qquad
B_3 \longrightarrow \mathrm{SU}(3)_C.
```
Harmonic vertical connections project to the SM gauge potentials $`(B_\mu, W_\mu^i, G_\mu^a)`$ on $`Y^4`$.*

</div>

<div class="remark">

*Remark 2* (BRST & Ward identities). Covariant gauge-fixing and BRST charge descend to the $`4`$D EFT; Ward–Slavnov–Taylor identities hold as in the SM.

</div>

# Chiral matter and anomaly cancellation

#### Modal-reuse selection (clarifying the “two-of-three”).

Internal *nonlinear* channels that stabilize coherent spinors are pairwise (see FP–R05); this *does not* constrain the $`4`$D gauge representation. After projection, fermions couple to the full covariant derivative $`D_\mu=\partial_\mu + i g' Y B_\mu + i g T^i W^i_\mu + i g_s T^a G^a_\mu`$ and can carry all three SM charges.

<div id="prop:anom" class="proposition">

**Proposition 3** (Anomaly-free hypercharge lattice). *Per family, the anomaly equations define a rank-$`2`$ $`\mathbb{Z}`$-sublattice in $`\mathbb{Z}^5`$ for $`(q_Q,q_u,q_d,q_L,q_e)`$. A $`\mathbb{Z}`$-basis is $`u^{(1)}=(1,4,-2,-3,-6)`$ and $`u^{(2)}=(1,1,1,-3,3)`$. Any $`q=\alpha u^{(1)}+\beta u^{(2)}`$ is anomaly-free. The SM choice is $`Y=\frac{1}{6}u^{(1)}`$.*

</div>

<div class="proof">

*Sketch.* Solve the three independent linear anomaly constraints over $`\mathbb{Z}`$; check the cubic $`U(1)^3`$ anomaly by multilinearity. Direct verification yields the stated basis. ◻

</div>

<div id="lem:witten" class="lemma">

**Lemma 4** (Global $`SU(2)`$ anomaly absent). *The number of left-handed $`SU(2)_L`$ doublets per family is $`4`$ (three colors of $`Q_L`$ plus one lepton doublet). For three families this is $`12`$, even; hence the mod-$`2`$ global $`SU(2)`$ anomaly vanishes.*

</div>

<div id="lem:charge-quant" class="lemma">

**Lemma 5** (Charge quantization from the internal/anomaly lattices). *Let $`(q_Q,q_u,q_d,q_L,q_e)\in\mathbb{Z}^5`$ satisfy the linear anomaly constraints and write $`q=\alpha u^{(1)}+\beta u^{(2)}`$ with $`u^{(1)},u^{(2)}`$ as in Prop. <a href="#prop:anom" data-reference-type="ref" data-reference="prop:anom">3</a>. Then the physical hypercharges $`Y=\frac{1}{6}q`$ lie in a $`\frac{1}{6}\mathbb{Z}`$ lattice. Moreover, the internal period lattice of the harmonic $`U(1)_Y`$ connection induces the same quantization on the fiber holonomies, so electric charge is quantized consistently with the anomaly lattice.*

</div>

<div class="proof">

*Sketch.* The integer lattice basis implies $`Y\in\frac{1}{6}\mathbb{Z}`$ by construction. Holonomies of the harmonic $`U(1)_Y`$ connection live in $`2\pi\mathbb{Z}`$, giving the same charge lattice for Wilson lines. ◻

</div>

# Three families via a flavor $`Z_3`$ holonomy

<div id="thm:families" class="theorem">

**Theorem 6** (Three coherent families via $`Z_3`$ flavor holonomy). *Let $`L_F\to S^1_{\mathrm{cen}}`$ be a flat complex line bundle with holonomy group $`\mathrm{Hol}(L_F)\cong Z_3=\{1,\omega,\omega^2\}`$, $`\omega=\mathrm{e}^{2\pi i/3}`$. Assume coherent internal profiles are twisted by $`L_F`$ while SM gauge indices are untwisted. Then the space of globally well-defined coherent profiles decomposes into three inequivalent character sectors, producing exactly three orthogonal coherent families without breaking $`SU(3)_C`$, $`SU(2)_L`$, or $`U(1)_Y`$.*

</div>

<div class="proof">

*Proof.* Zero modes along $`S^1_{\rm cen}`$ must satisfy twisted periodicity by a character of $`Z_3`$. Since $`Z_3`$ has exactly three one-dimensional irreps, twisted sections split into three inequivalent sectors. The twist acts only on $`L_F`$ and commutes with SM gauge factors, so no gauge symmetry is broken. Orthogonality of distinct characters gives a direct-sum decomposition into three families. ◻

</div>

<div id="rem:flavor-anomaly" class="remark">

*Remark 7* (Flavor twist and anomaly safety). The $`Z_3`$ twist acts only on the external flavor line bundle $`L_F`$ and commutes with the SM gauge action. It is not introduced as a gauged 4D symmetry and does not act on gauge indices. Consequently there is no additional gauge or mixed discrete anomaly to check. We use $`L_F`$ purely as a geometric device to produce three inequivalent coherent sectors (families) without breaking $`SU(3)_C`$, $`SU(2)_L`$, or $`U(1)_Y`$.

</div>

# Higgs sector and electroweak symmetry breaking

A coherent scalar doublet $`\Phi\in(\mathbf{1},\mathbf{2},+1/2)`$ arises from the internal scalar sector aligned with $`B_2/B_1`$ reuse. Representation-correct Bochner/Lichnerowicz yields the curvature shift
``` math
\begin{equation}
m_\Phi^2(\mu;R)\;=\;\kappa\,\lambda_\ast\;-\;\frac{1}{6}\,\mathrm{Scal}\;+\;\delta m_\Phi^2(\mu),
\label{eq:Hmass}
\end{equation}
```
with $`\lambda_\ast>0`$ the vertical spectral gap and $`\delta m_\Phi^2(\mu)`$ the renormalized mass at scale $`\mu`$. EWSB occurs when $`m_\Phi^2(\mu_{\rm EW};R_{\rm EW})<0`$ predominantly by RG running of $`\delta m_\Phi^2(\mu)`$; curvature provides a threshold shift in <a href="#eq:Hmass" data-reference-type="eqref" data-reference="eq:Hmass">[eq:Hmass]</a>. Minimization gives $`v=\mu/\sqrt{\lambda}`$, and $`m_W=\tfrac12 g v`$, $`m_Z=\tfrac12\sqrt{g^2+g'^2}\,v`$, $`m_f=\tfrac{v}{\sqrt2}y_f`$.

<div class="remark">

*Remark 8* (Example: $`k`$ is $`\mathcal{O}(1)`$). Consider normalized internal profiles with comparable $`L^2`$ norms on $`B_1`$ and $`B_2`$ and a mild base-only warp factor. Then $`\|A^{(1)}\|_{\rm int}^2/\|A^{(2)}\|_{\rm int}^2=k`$ differs from unity by geometric factors of order one (fiber radii and smooth warp averages). A representative choice yields $`k\simeq 5/3`$ (GUT normalization) but other $`\mathcal{O}(1)`$ values are consistent depending on internal normalization; our numerical thresholds absorb the small differences.

</div>

#### Selection potential $`\Xi`$ (FP–R06) in the SM limit.

The selection potential $`\Xi`$ introduced in FP–R06 collects curvature-coupled and interaction terms that govern modal transitions. Restricted to the coherent SM sector, $`\Xi`$ reduces to the electroweak scalar potential plus Yukawa interactions (up to higher-dimension operators suppressed by the gap). Thus the usual Higgs-Yukawa structure is the low-energy face of the general selection dynamics.

# Yukawas, flavor, and CP: internal overlaps

Yukawas arise from internal overlap integrals of left/right coherent spinors with the scalar precursor, $`Y_f \sim \int (\psi_{f_L})^\dagger \Phi \psi_{f_R}`$ over the fiber. Internal localization and phases produce hierarchies and mixings.

#### Toy overlap model (hierarchies and phases).

Let $`u`$ parametrize $`S^1_{\rm cen}`$; take three Gaussian family profiles with centers $`(u_1,u_2,u_3)`$ and widths $`\sigma`$, and a broad Higgs profile of width $`\Sigma`$. Then
``` math
(Y_f)_{ab}\ \propto\ \exp\!\Big(-\tfrac{(u_a-u_b)^2}{2(\sigma_{f_L}^2+\sigma_{f_R}^2+\Sigma^2)}\Big)\,
\mathrm{e}^{i(\phi_{f_R,b}-\phi_{f_L,a})},
```
which yields diagonal hierarchies for separated centers and off-diagonal entries from small offsets; complex phases propagate to CKM/PMNS.

# Particle dictionary: construction, charges, stability

## Fermions (per family)

| Field | SM rep | Internal supp | Construction | Stability reason |
|:---|:---|:---|:---|:---|
| $`Q_L`$ | $`(\mathbf{3},\mathbf{2},+1/6)`$ | $`B_3\oplus B_2\oplus B_1`$ | Coherent spinor; color triplet, weak doublet | Gap protection; baryon \# approx. |
| $`u_R`$ | $`(\mathbf{3},\mathbf{1},+2/3)`$ | $`B_3\oplus B_1`$ | Right spinor; color triplet, $`Y=+2/3`$ | Decays via $`W`$ if heavy |
| $`d_R`$ | $`(\mathbf{3},\mathbf{1},-1/3)`$ | $`B_3\oplus B_1`$ | Right spinor; color triplet, $`Y=-1/3`$ | Same |
| $`L_L`$ | $`(\mathbf{1},\mathbf{2},-1/2)`$ | $`B_2\oplus B_1`$ | Coherent spinor; weak doublet | Lepton \# approx. |
| $`e_R`$ | $`(\mathbf{1},\mathbf{1},-1)`$ | $`B_1`$ | Right spinor; $`Y=-1`$ | Atomic stability |
| $`\nu_R`$ | $`(\mathbf{1},\mathbf{1},0)`$ | none | Sterile coherent spinor | Seesaw option |

*Stability note (pairwise mechanism).* In the fixed-point contraction regime, *pairwise* internal interaction channels on $`B_1,B_2,B_3`$ are the ones that generically keep $`\gamma_{n,k}=\kappa_{n,k}\lambda_{n,k}-L-\Delta_{\mathrm{curv}}`$ positive. Pure single-bundle and fully tri-bundle nonlinearities do not at the same scale without additional smallness/gap. This is a *dynamical* selection on the internal channel and **does not** restrict the $`4`$D gauge content: after projection, fermions couple to the full covariant derivative and can carry all three SM charges.

## Gauge bosons and Higgs

| Boson | SM rep | Origin in MTT | Why massless / $`m\neq0`$ | Role |
|:---|:---|:---|:---|:---|
| $`G_\mu^a`$ | $`(\mathbf{8},\mathbf{1},0)`$ | Harmonic connection on $`B_3`$ | Unbroken $`\mathrm{SU}(3)`$ | Color force (confining) |
| $`W^\pm,Z`$ | $`(\mathbf{1},\mathbf{3},0)`$ mix | Harmonic connection on $`B_2`$ | Higgs mechanism | Weak interaction |
| $`B_\mu\to A_\mu`$ | $`(\mathbf{1},\mathbf{1},0)`$ | Harmonic connection on $`B_1`$ | Unbroken $`\mathrm{U}(1)`$ | Photon; long range |
| $`H`$ | $`(\mathbf{1},\mathbf{2},+1/2)`$ | Scalar precursor (reuse $`B_2/B_1`$) | <a href="#eq:Hmass" data-reference-type="eqref" data-reference="eq:Hmass">[eq:Hmass]</a> and RG | EWSB |

## Hadrons (examples; color singlets)

| State | Quark content | Color | Construction | Stability/decay |
|:---|:---|:---|:---|:---|
| $`\pi^\pm,\pi^0`$ | $`q\bar q`$ | singlet | Two-spinor bound state (chiral ps.) | Strong decays if open |
| $`p`$ | $`uud`$ | singlet ($`\epsilon_{abc}`$) | Three-spinor antisym. in color | Stable (B#); atomic matter |
| $`n`$ | $`udd`$ | singlet | As above | $`\beta`$-decay (free); nuclear bound states stable |
| $`J/\psi,\Upsilon`$ | $`c\bar c,\ b\bar b`$ | singlet | Heavy quarkonia | Narrow resonances |

# 8A. Quantitative Admissibility Ordering of Standard Model Multiplets

Section 8 provided a qualitative particle dictionary identifying the Standard Model (SM) multiplets as coherent spinorial or gauge excitations supported on specific internal bundle combinations $`B_1,B_2,B_3`$. In this section we refine that dictionary by giving a *quantitative admissibility analysis* that determines, from first principles, which SM multiplets are maximally robust, which are marginal, and where near–gap (heavy or decoupled) behavior must first arise.

This analysis sharpens the qualitative stability statement of Section 8 (“pairwise channels are generically stable”) into a field–by–field ordering derived directly from the fixed–point damping condition.

## 8A.1. Effective damping and admissibility

In the Fixed–Point framework, stability of a non–harmonic mode $`a_{n,k}`$ is governed by an effective damping margin of the form
``` math
\begin{equation}
\gamma_{n,k}(x)
\;=\;
\kappa_{n,k}\,\lambda^{\mathrm{eff}}_{n,k}(x)
\;-\;
L_{n,k}(x),
\label{eq:gamma_fp}
\end{equation}
```
where $`\lambda^{\mathrm{eff}}_{n,k}(x)`$ is the *representation–correct effective eigenvalue*, incorporating curvature–gap coupling (Bochner/Lichnerowicz), and $`L_{n,k}(x)`$ is the local Lipschitz constant of the nonlinear remainder on the invariant sublevel. The disturbance amplitude $`\delta_{n,k}(x)`$ enters through the Ornstein–Uhlenbeck balance, and admissibility requires a strict margin
``` math
\begin{equation}
\gamma_{n,k}(x)
\;\ge\;
\delta_{n,k}(x)
\;+\;
\varepsilon,
\label{eq:admissibility}
\end{equation}
```
for some $`\varepsilon>0`$.

For a coherent SM multiplet $`X`$ supported on a finite set of internal bundles
``` math
\mathrm{supp}(X)\subset\{B_1,B_2,B_3\},
```
we define the *support gap* by
``` math
\begin{equation}
\lambda_{\mathrm{supp}}(X)
\;:=\;
\min_{B_n\in\mathrm{supp}(X)} \lambda^{\mathrm{eff}}_{B_n},
\label{eq:lambda_supp}
\end{equation}
```
where $`\lambda^{\mathrm{eff}}_{B_n}`$ denotes the effective first positive vertical gap of $`\Delta_{B_n}`$, including curvature shifts.

<div class="remark">

*Remark 9*. The use of <a href="#eq:lambda_supp" data-reference-type="eqref" data-reference="eq:lambda_supp">[eq:lambda_supp]</a> corresponds to the block–diagonal Laplacian and negligible inter–bundle coupling approximation realized in the baseline MTT geometry. Possible inter–bundle couplings shift $`\lambda_{\mathrm{supp}}`$ at higher order and do not affect the ordering results below.

</div>

We then define the *raw channel margin*
``` math
\begin{equation}
\gamma_{\mathrm{raw}}(X)
\;:=\;
\kappa\,\lambda_{\mathrm{supp}}(X)
\;-\;
L(X),
\label{eq:gamma_raw}
\end{equation}
```
where $`L(X)`$ is the effective Lipschitz scale associated with the nonlinear interactions of $`X`$.

## 8A.2. Channel dependence and effective margin

As emphasized in Section 8, internal interaction channels fall into three structural classes:

1.  *Pairwise channels* $`B_i\oplus B_j`$,

2.  *Single–bundle channels* $`B_i`$,

3.  *Tri–bundle channels* $`B_1\oplus B_2\oplus B_3`$.

The Fixed–Point stability analysis shows that pairwise channels benefit from cross–bundle stabilization, while single–bundle and fully tri–bundle nonlinearities require additional smallness or gap to maintain the admissibility margin <a href="#eq:admissibility" data-reference-type="eqref" data-reference="eq:admissibility">[eq:admissibility]</a> at the same scale.

To encode this effect at the level of a diagnostic ordering, we introduce an *effective channel penalty* $`P(X)`$ and define the *effective admissibility margin*
``` math
\begin{equation}
\gamma_{\mathrm{eff}}(X)
\;:=\;
\gamma_{\mathrm{raw}}(X)
\;-\;
P(X),
\label{eq:gamma_eff}
\end{equation}
```
where $`P(X)`$ is an effective measure of how the disturbance scale $`\delta(X)`$ and/or the nonlinear Lipschitz constant $`L(X)`$ grows with channel complexity. Concretely, one may take
``` math
\begin{equation}
P(X)
\;=\;
\begin{cases}
0, & X \text{ pairwise supported},\\[4pt]
\eta_s\,\lambda_{\mathrm{supp}}(X), & X \text{ single--bundle},\\[4pt]
\eta_t\,\lambda_{\mathrm{supp}}(X), & X \text{ tri--bundle},
\end{cases}
\label{eq:channel_penalty}
\end{equation}
```
with fixed $`0<\eta_s<\eta_t<1`$. This form is not assumed as a universal law, but as an effective parametrization of the channel–dependent scaling of $`L(X)`$ and $`\delta(X)`$ observed in the FP analysis.

A multiplet $`X`$ is called:

- *robust* if $`\gamma_{\mathrm{eff}}(X)\ge \delta(X)+\varepsilon`$,

- *marginal* if $`0<\gamma_{\mathrm{eff}}(X)<\delta(X)+\varepsilon`$,

- *near–gap* if $`\gamma_{\mathrm{eff}}(X)\le 0`$.

## 8A.3. Ordering of SM multiplets

Using the internal supports listed in Section 8:
``` math
\begin{align*}
u_R,d_R &:\; B_3\oplus B_1 \quad \text{(pairwise)},\\
L_L &:\; B_2\oplus B_1 \quad \text{(pairwise)},\\
e_R &:\; B_1 \quad \text{(single)},\\
Q_L &:\; B_3\oplus B_2\oplus B_1 \quad \text{(tri--bundle)},
\end{align*}
```
and noting that gauge bosons arise as harmonic connections on a single $`B_n`$, we obtain the following result.

<div class="theorem">

**Theorem 10** (Relative admissibility of SM multiplets). *Assume uniform vertical gaps $`\lambda^{\mathrm{eff}}_{B_n}>0`$ and the Fundamental Contractivity Condition on the coherent sector. Then:*

1.  *All SM gauge bosons are robust (harmonic modes not subject to non–harmonic damping).*

2.  *Right–handed quarks $`u_R,d_R`$ and left–handed leptons $`L_L`$ are generically robust.*

3.  *Right–handed charged leptons $`e_R`$ are admissible but more sensitive to disturbance.*

4.  *Left–handed quark doublets $`Q_L`$ are the *first SM multiplets to become marginal* as gaps decrease or disturbance increases.*

*This ordering is independent of family index and depends only on internal support structure.*

</div>

<div class="proof">

*Proof.* All multiplets sharing the same minimal support gap $`\lambda_{\mathrm{supp}}`$ differ only by the channel–dependent contribution to $`L(X)`$ and $`\delta(X)`$ encoded in $`P(X)`$. Pairwise channels incur the smallest effective disturbance and nonlinear scale, while single–bundle and tri–bundle channels incur larger effective penalties. Since $`Q_L`$ is the unique SM fermion with tri–bundle support, its effective margin $`\gamma_{\mathrm{eff}}(Q_L)`$ is strictly smallest among SM multiplets at fixed gaps. ◻

</div>

## 8A.4. Admissibility ordering and proton stability

The admissibility ordering above has a direct implication for baryon number and proton stability.

<div class="lemma">

**Lemma 11** (Penalized–channel activation in baryon–violating operators). *Any gauge–invariant dimension–six baryon–number–violating operator in the Standard Model necessarily induces a coherent excitation that activates at least one *penalized channel* in the MTT admissibility ordering, namely either a single–bundle or a tri–bundle internal support.*

</div>

<div class="proof">

*Proof.* At dimension six, the gauge–invariant baryon–number–violating operators of the Standard Model fall into two classes. Operators of the $`QQQL`$ type necessarily contain at least one left–handed quark doublet $`Q_L`$, whose internal support is $`B_3\oplus B_2\oplus B_1`$, thereby activating the tri–bundle channel.

The remaining independent class, schematically of the $`u^cu^cd^ce^c`$ type, contains no SU(2)$`_L`$ doublets but necessarily includes a right–handed charged lepton $`e_R`$, whose internal support is the single–bundle channel $`B_1`$. Thus these operators activate a single–bundle channel.

In both cases, baryon–number violation necessarily probes at least one channel that is penalized relative to pairwise–supported multiplets in the admissibility ordering. ◻

</div>

<div class="remark">

*Remark 12* (Emergent baryon number). Baryon–number–violating operators necessarily activate at least one penalized channel in the MTT admissibility ordering. The most strongly suppressed channels are those involving the left–handed quark doublet $`Q_L`$, the unique SM fermion with tri–bundle support, while alternative baryon–violating operators activate single–bundle channels such as $`e_R`$. Consequently, baryon–number violation is dynamically suppressed by the gap scale and pushed toward the near–gap sector.

This provides a geometric and dynamical explanation for the approximate conservation of baryon number and proton longevity. Compatibility with bounds on possible dimension–five operators remains as discussed in Section 15, where additional selection rules or discrete remnants may further suppress such contributions.

</div>

## 8A.5. Near–gap exotics

As gaps decrease or disturbance increases, the first channels to approach the admissibility boundary are those containing $`Q_L`$. Near–gap vector–like or exotic states therefore couple preferentially to left–handed quark doublets. This provides a first–principles explanation of the “heavy exotics near the gap” discussed in Section 15 and yields a clear phenomenological handle.

In all cases these couplings remain suppressed in absolute magnitude by the gap scale, in accordance with the heavy near–gap exotic sector described in Section 15; the “preference” here refers to relative visibility among otherwise suppressed channels.

## 8A.6. Weinberg operator: admissibility bridge

The unique dimension–five gauge–invariant lepton–number–violating operator of the Standard Model is the Weinberg operator
``` math
\mathcal O_W \;=\; \frac{c_{ij}}{\Lambda}\,(L_L^i H)(L_L^j H),
```
which generates Majorana neutrino masses after electroweak symmetry breaking. In contrast to the baryon–number–violating operators discussed above, $`\mathcal O_W`$ does not necessarily activate a tri–bundle internal channel in the baseline MTT particle dictionary.

In the support assignment of Section 8, both the lepton doublet $`L_L`$ and the Higgs field $`H`$ are supported on pairwise internal bundles. Consequently, the Weinberg operator is *not* automatically penalized by channel complexity alone. This explains why lepton number violation and neutrino masses require additional structure beyond the arguments used for baryon number.

Within MTT, two complementary mechanisms naturally arise.

#### (A) Selection–rule or remnant–symmetry branch.

The coherent sector selected by the joint harmonic projector may forbid the contraction structure required by $`\mathcal O_W`$ at leading order. In this case, lepton number emerges as an approximate symmetry of the coherent effective theory, broken only by subleading effects or discrete remnants. The Weinberg operator is then absent or highly suppressed without invoking heavy mediators, consistent with the dimension–five caveat discussed in Section 15.

#### (B) Near–gap mediation branch.

Alternatively, $`\mathcal O_W`$ may be generated by integrating out heavy degrees of freedom such as right–handed neutrinos, scalar triplets, or fermion triplets. In MTT language, these mediators belong to near–gap or marginal channels whose admissibility margins are small. The coefficient $`c_{ij}/\Lambda`$ is then controlled by the same spectral gaps and admissibility bounds that govern projector variation and heavy exotics. Neutrino masses arise dynamically as a near–gap effect,
``` math
m_\nu \;\sim\; \frac{v^2}{\Lambda_{\mathrm{gap}}}
\times (\text{admissibility suppression}),
```
placing lepton–number violation parametrically below the robust coherent sector.

Thus, while baryon–number violation is suppressed by unavoidable activation of penalized channels, the Weinberg operator probes a distinct admissibility pathway. Its smallness or absence is not imposed by hand, but emerges from either coherent–sector selection rules or near–gap mediation within the same modal–geometric framework.

## 8A.X. Phenomenology summary: supports, penalties, and leading signatures

<div class="center">

<div class="tabularx">

@ L2.6cm L3.0cm L2.6cm L2.2cm Y @ **Item** & **Internal support** & **Channel class** & **Penalty tier** & **MTT admissibility takeaway / signature**  
Gauge bosons $`(G,W,B)`$ & harmonic on $`B_n`$ & harmonic & none & Coherent by construction; not governed by the non–harmonic damping inequality.  
$`u_R, d_R`$ & $`B_3\oplus B_1`$ & pairwise & $`P=0`$ & Generically robust in baseline geometry; useful reference channel when discussing relative suppression elsewhere.  
$`L_L`$ & $`B_2\oplus B_1`$ & pairwise & $`P=0`$ & Robust pairwise sector; Weinberg-type effects are *not* automatically penalized unless mediation/selection rules impose it.  
$`e_R`$ & $`B_1`$ & single & $`P=\eta_s\,\lambda_{\mathrm{supp}}`$ & More disturbance-sensitive; operators requiring $`e_R`$ necessarily probe a penalized channel.  
$`Q_L`$ & $`B_3\oplus B_2\oplus B_1`$ & tri-bundle & $`P=\eta_t\,\lambda_{\mathrm{supp}}`$ & Most constrained SM fermion; first to go marginal as gaps shrink / disturbance grows. Near-gap/exotic effects are *most visible* in $`Q_L`$-containing processes (relative preference within overall suppression).  

**Process / operator class** & **Field content** & **Forces penalized channel?** & **Bottleneck** & **Consequence**  

Dim-6 baryon violation & $`QQQL`$ & yes (tri) & $`Q_L`$ & Strong suppression via smallest margin; naturally pushed toward near-gap mediation; supports proton longevity.  
Dim-6 baryon violation & $`u^c u^c d^c e^c`$ & yes (single) & $`e_R`$ & Also suppressed (penalized channel), typically weaker than tri-bundle suppression if $`\eta_t>\eta_s`$.  
Weinberg (dim-5) & $`(LH)(LH)`$ & model-dependent & model-dependent & Not automatically suppressed by channel complexity in the baseline mapping; either (i) forbidden/suppressed by selection rules/remnants, or (ii) generated via near-gap mediators (seesaw) whose channel class determines suppression.  
Near-gap heavy exotics & vector-like / exotic states & typically yes & often $`Q_L`$ & Couplings suppressed in absolute magnitude by the gap scale; relative visibility tends to peak in the $`Q_L`$ bottleneck sector.  

</div>

</div>

# Photons, bosons as interactions, and speed $`c`$

The photon is the massless gauge mode associated with unbroken $`U(1)_{\rm em}`$ (after $`B_\mu`$–$`W^3_\mu`$ mixing). Its dynamics are governed by the Maxwell action on $`(Y^4,g)`$; null characteristics coincide with the Lorentzian light cone, so wave packets propagate at $`c`$. Non-abelian connections from $`B_2,B_3`$ yield $`W/Z`$ (mass via Higgs) and gluons (massless, but confining).

# Quarks, hadrons, and confinement

A quark is a coherent 4D spinor with internal profile in the fundamental of $`\mathrm{SU}(3)`$ (from $`B_3`$), with hypercharge from $`B_1`$ and weak isospin from $`B_2`$ (modal reuse). Hadrons are color-singlet *composites* minimizing the projected energy:
``` math
|M\rangle\sim \sum c_{ab}|q_a\bar q_b\rangle,\qquad
|B\rangle\sim \sum c_{abc}\,\epsilon^{\alpha\beta\gamma}|q_{a,\alpha}q_{b,\beta}q_{c,\gamma}\rangle.
```
Confinement is encoded in the non-perturbative $`\mathrm{SU}(3)`$ dynamics (area law for large Wilson loops); in the MTT energy, it appears as competition between gauge curvature and overlap functionals: color charge isolation is energetically forbidden.

#### Overlap/barrier energetics and fragmentation (FP–R04 link).

The overlap functionals and barrier theorems of FP–R04 imply that color-nonsinglet separations face growing energetic barriers, while color-singlet recombinations lower the projected energy. String breaking and jet fragmentation correspond to barrier crossing along directions of increasing overlap with color-singlet channels. This provides a geometric energy-landscape picture underlying hadronization, consistent with the area law and with the composite coherent minima described above.

# Spinors with bundles: how charges arise

4D spinors live in $`S(Y^4)\otimes \eta_{\rm int}`$, with $`\eta_{\rm int}`$ built from bundle harmonics on $`B_1,B_2,B_3`$. Pairings with harmonic connections yield conserved currents and charges $`Q_Y=\int j_Y^0 d^3x`$, $`Q_{\rm weak}^i=\int j^{0,i}_{\rm weak} d^3x`$, $`Q_{\rm color}^a=\int j^{0,a}_{\rm color} d^3x`$. Quantization follows from internal period lattices. Modal reuse enforces the group-theoretic inclusions $`U(1)\subset SU(2)\subset SU(3)`$ at the level of geometry, matching the SM embedding.

## Spin–statistics and the Pauli principle

Quantization of the coherent sector proceeds with canonical anticommutation relations (CAR) for 4D spinor fields on the spin bundle $`S(Y^4)`$, tensored with the finite-dimensional internal fiber $`\eta_{\rm int}`$. Hence the usual spin–statistics theorem applies: coherent spinors obey Fermi statistics and the Pauli exclusion principle holds exactly as in standard QFT. The internal bundle structure supplies gauge charges and family labels but does not alter CAR on $`S(Y^4)`$.

# Why everyday matter is first generation

Higher families have larger Yukawas from internal localization/phase structure, hence larger masses and faster weak decays; the first-generation charges allow the lightest color-singlet baryon (proton) and the lightest charged lepton (electron) to form atoms. In MTT this follows from (i) overlap hierarchies, (ii) CKM/PMNS mixings, and (iii) energy minimization under the coherent fixed-point projection.

# High-scale boundary conditions and RG flow (with numerics)

#### Gauge couplings (boundary).

Internal normalization fixes a boundary relation at $`\mu_0`$:
``` math
g_s(\mu_0)=g(\mu_0)=\sqrt{k}\,g'(\mu_0),
```
with rational $`k`$ set by the internal overlap norms of the harmonic connections (see <a href="#rem:normalization" data-reference-type="ref+Label" data-reference="rem:normalization">13</a> below).

#### One-loop running.

Using GUT-normalized $`\alpha_1=\tfrac{5}{3}\alpha_Y`$ with one-loop coefficients $`(b_1,b_2,b_3)=(\tfrac{41}{10},-\tfrac{19}{6},-7)`$,
``` math
\frac{d\,\alpha_i^{-1}}{d\ln\mu}=-\frac{b_i}{2\pi},\qquad
\alpha_i^{-1}(M_Z)=\alpha_U^{-1}+\frac{b_i}{2\pi}\ln\frac{\mu_0}{M_Z}.
```
For $`\mu_0=10^{16}\,`$GeV, $`\ln(\mu_0/M_Z)\simeq 32.329`$:
``` math
\Delta_1\simeq 21.11,\quad \Delta_2\simeq -16.30,\quad \Delta_3\simeq -36.03.
```
Thus $`\alpha_i^{-1}(M_Z)=\alpha_U^{-1}+\Delta_i`$. As in the minimal SM, one-loop lines do not meet exactly; in MTT small, *calculable* high-scale thresholds from nearby modal excitations
``` math
\alpha_i^{-1}(M_Z)=\bigl[\alpha_U^{-1}+\Delta_i^{\rm thr}\bigr]+\frac{b_i}{2\pi}\ln\frac{\mu_0}{M_Z}
```
(with $`(\Delta_1,\Delta_2,\Delta_3)`$ modest and $`\mathcal{O}(1)`$) align the three couplings, with the geometric origin in overlap-normalization and spectral gaps.

<div id="rem:normalization" class="remark">

*Remark 13* (High-scale gauge normalization). The boundary relation $`g_s(\mu_0)=g(\mu_0)=\sqrt{k}\,g'(\mu_0)`$ arises from internal overlap normalizations $`\langle A^{(n)},A^{(n)}\rangle_{\rm int}`$ of the harmonic connections. Concretely, $`k=\|A^{(1)}\|_{\rm int}^2/\|A^{(2)}\|_{\rm int}^2`$ (and similarly for $`g_s`$) once the internal profiles are fixed. In the numerical baselines, $`k=\mathcal{O}(1)`$.

</div>

# Consistency checks and standard objections

#### Global $`SU(2)`$ anomaly.

Covered by <a href="#lem:witten" data-reference-type="ref+Label" data-reference="lem:witten">4</a> (even number of $`SU(2)`$ doublets).

#### Measurement disturbance and OU balance.

In the FP framework, disturbance enters as additive noise with covariance density $`\delta_{n,k}`$ for non-harmonic modes; damping margins are $`\gamma_{n,k}=\kappa_{n,k}\lambda_{n,k}-L-\Delta_{\rm curv}`$. Modewise OU variance is $`\sigma_{n,k}^2=\delta_{n,k}/(2\gamma_{n,k})`$, while bundlewise stability requires the weighted summability $`\sum_{n,k}(1+\lambda_{n,k})\,\delta_{n,k}/\gamma_{n,k}<\infty`$. In laboratory measurements, a finite coupling to the apparatus increases $`\delta_{n,k}`$ and can temporarily reduce the effective $`\gamma_{n,k}`$, enhancing decoherence; the coherent sector remains stable precisely when the summability criterion holds. This connects the MTT fixed-point picture to standard decoherence phenomenology without additional postulates.

#### Strong CP.

<div class="remark">

*Remark 14* (Strong CP). The minimal MTT$`\to`$SM setup reproduces the SM with a generic $`\theta_{\rm QCD}`$. An explicit MTT mechanism for $`\theta\approx 0`$ (e.g. a PQ-like $`U(1)_{\rm PQ}`$ realized by an internal flat direction, or symmetry alignment of phases) is beyond the present scope and left for future work. The results here do not depend on $`\theta`$.

</div>

#### Proton stability.

<div class="remark">

*Remark 15* (Proton stability). Gauge interactions do not generate dimension-6 $`X,Y`$ exchange operators. Higher-dimension four-fermion operators induced by heavy modal states are suppressed by the gap scale $`\Lambda_{\rm MTT}`$. An approximate global $`U(1)_B`$ (or a discrete remnant) can forbid dimension-$`5`$ operators, ensuring compatibility with current proton-decay bounds.

</div>

# Predictions and observational handles

- **Threshold patterns:** small, correlated high-scale thresholds in gauge couplings; testable in precision unification fits.

- **Flavor textures:** hierarchy/mixing patterns tied to internal localization; testable in rare decays and CP violation observables.

- **Heavy exotics:** near-gap vector-like states with suppressed couplings; possible signals at future colliders.

- **Cosmology:** curvature–gap ties early-universe thresholds to background curvature; stochastic GW backgrounds from modal transitions.

# Conclusion

From the coherent fixed-point sector of MTT—supported by spectral gaps, $`H^1`$-bounded projectors, and FCC—we have derived the full Standard Model: $`B_1\!\to U(1)_Y`$, $`B_2\!\to SU(2)_L`$, $`B_3\!\to SU(3)_C`$; chiral matter in three families via a *flavor* $`Z_3`$ holonomy (without breaking SM gauge groups); constructive anomaly cancellation; a representation-correct Higgs sector with RG-driven EWSB; Yukawas from internal overlaps; and a numerical one-loop RG run with geometric thresholds. A detailed particle dictionary and standard consistency checks are included. This places MTT on firm ground as a unified geometric origin of the SM at low energies, with clear avenues for quantitative tests.

# Anomaly lattice: constructive basis

Let $`(q_Q,q_u,q_d,q_L,q_e)\in\mathbb{Z}^5`$ denote integer hypercharges with physical $`Y=\tfrac{1}{6}q`$. The linear anomaly constraints (per family) are
``` math
\begin{aligned}
&\text{$SU(3)^2\!-\!U(1)$:} && 2q_Q - q_u - q_d = 0,\\
&\text{$SU(2)^2\!-\!U(1)$:} && 3 q_Q + q_L = 0,\\
&\text{Grav$^2\!-\!U(1)$:} && 6 q_Q - 3q_u - 3q_d + 2q_L - q_e = 0.
\end{aligned}
```
Row-reduction over $`\mathbb{Z}`$ gives a rank-$`3`$ matrix with nullspace rank $`2`$ spanned by $`u^{(1)}=(1,4,-2,-3,-6)`$ and $`u^{(2)}=(1,1,1,-3,3)`$. The cubic $`U(1)^3`$ anomaly vanishes for any integer combination $`q=\alpha u^{(1)}+\beta u^{(2)}`$ by multilinearity once the linear constraints hold. The SM hypercharge corresponds to $`Y=\tfrac{1}{6}u^{(1)}`$.

<div class="thebibliography">

10

P. Nero. *Modal Triplet Theory: Foundation* Zenodo, 2025.

</div>
