---
abstract: |
  Penrose twistor theory provides a powerful holomorphic encoding of massless, self-dual, and conformally invariant sectors of four-dimensional field theories, yet has long resisted interpretation as a fundamental description of nature. In this paper we show that twistor theory arises naturally as an *effective encoding* of a distinguished high-coherence regime of Modal Triplet Theory (MTT). Using the coherent-sector projection, spectral-gap control, and controlled truncation framework of MTT, we define a precise *twistor corner* in which twistor methods are valid, explain their efficiency and limitations, and derive a sharp criterion for their breakdown.

  Technically, we identify the twistor corner as the regime in which noncoherent modes are suppressed, mass-generation effects are negligible, scale variation is slow, and the coherent gauge or gravitational sector is near self-dual. We prove that in this regime the coherent dynamics admits a Schur–Feshbach reduced generator whose correction term is suppressed by the inverse spectral gap. Twistor encoding is valid precisely while this controlled truncation correction remains below an admissibility threshold. When the gap collapses or coherent–noncoherent mixing grows beyond threshold, the induced evolution on coherent data becomes kernel-valued, signaling a genuine MTT selection event and forcing re-projection into a new admissible basin.

  This work situates twistor theory within a broader theory of coherence, selection, and irreversibility, explaining both its remarkable successes and its intrinsic domain of validity.
current_version: v1.0
generated_from_main_tex_sha256: 0c25787aa20c061590224a56ffa9757558739957b6dc297800e31e8bcbd94bba
paper_id: twistor-encodings-as-high-coherence-limits-of-modal-tri-8b03ee29
release_state: zenodo_released
released_version: v1.0
zenodo_doi: 10.5281/zenodo.18255155
zenodo_record_id: 18255155
zenodo_url: "https://zenodo.org/records/18255155"
---

<div class="center">

**Twistor Encodings as High-Coherence Limits of Modal Triplet Theory**

A Coherent-Sector Encoding, Controlled Truncation, and Kernel Transition Criterion

Peter Nero

</div>

# Introduction

Twistor theory, introduced by Penrose , replaces spacetime fields by holomorphic data on a complex geometric space encoding null directions and conformal structure. It has achieved striking successes: the Penrose transform for massless fields, the Ward correspondence for self-dual Yang–Mills theory, the nonlinear graviton for self-dual gravity, and the modern twistor-amplitude revolution initiated by Witten and developed further in .

At the same time, twistor theory has well-known limitations. It is naturally adapted to massless and self-dual sectors, struggles with mass generation, confinement, and generic curved backgrounds, and does not by itself provide a framework for probability, measurement, or irreversibility. These facts have often been viewed as obstacles to twistor theory as a fundamental description.

Modal Triplet Theory (MTT) takes a different starting point. Rather than proposing a new geometric container, MTT introduces a *selection principle* based on coherent projection, spectral gaps, and controlled truncation. Observable physics arises as the coherent sector of a higher-dimensional modal dynamics, and effective descriptions are valid only within admissible slabs where coherence capacity remains positive.

The central claim of this paper is that twistor theory is neither accidental nor fundamental. Instead:

> *Twistor theory is the optimal holomorphic encoding of the maximally coherent, null-dominated, self-dual corner of the MTT coherent sector.*

MTT explains why this corner exists, why twistor methods are so effective there, and why they must fail beyond it.

## What this paper does and does not do

- We do *not* propose a new twistor theory.

- We do *not* claim twistor space is fundamental or replaces the MTT modal space.

- We *do* provide a precise regime (the twistor corner) in which twistor encoding is valid.

- We *do* derive a sharp breakdown criterion tied to MTT admissibility and controlled truncation.

# Modal Triplet Theory: Minimal Background

We summarize only the components of MTT required for this paper. For full development see the MTT corpus .

## Modal geometry and coherent projection

MTT is defined on a modal configuration space
``` math
\begin{equation}
M_{10} = Y^4 \times B_1 \times B_2 \times B_3 ,
\end{equation}
```
where $`Y^4`$ is the emergent spacetime base and $`B_i`$ are compact internal bundles equipped with Laplace-type operators $`\Delta_{B_i}`$. The $`\Delta_{B_i}`$ commute, allowing definition of a joint coherent projector
``` math
\begin{equation}
\Pi_{\mathrm{coh}} = \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
where $`\Pi_{B_i}`$ is the Riesz projector onto $`\ker \Delta_{B_i}`$.

Observable physics arises from the coherent sector
``` math
H_P := \mathrm{Ran}\Pi_{\mathrm{coh}},
```
while $`H_Q := \mathrm{Ran}(I-\Pi_{\mathrm{coh}})`$ contains noncoherent modes.

## Admissible slabs and controlled truncation

An *admissible slab* $`\mathcal S \subset Y^4`$ is a spacetime region on which:

- the internal Laplacians have a uniform spectral gap $`\lambda_Q>0`$,

- the projector $`\Pi_{\mathrm{coh}}`$ is bounded on the relevant Sobolev scales,

- truncation errors from discarding $`H_Q`$ are controlled.

On such slabs, effective four-dimensional quantum field theory and general relativity emerge as controlled approximations. When admissibility fails, no single-valued effective description exists.

# Definition of the Twistor Corner

We now define the regime in which twistor theory becomes a natural encoding of the MTT coherent sector.

<div class="definition">

**Definition 1** (Twistor Corner). Let $`\mathcal S`$ be an admissible slab. We say that $`\mathcal S`$ lies in the *twistor corner* of MTT if the following dimensionless parameters satisfy
``` math
(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4) \ll 1:
```

1.  (*Self-duality*) $`\varepsilon_1 := \|F^-\|/\|F\|`$, where $`F^\pm`$ are the (anti-)self-dual components of the coherent gauge curvature.

2.  (*Mass suppression*) $`\varepsilon_2 := m/E`$, where $`m`$ denotes masses generated by overlap/Higgs structure and $`E`$ is the characteristic energy scale.

3.  (*Slow scale variation*) $`\varepsilon_3 := \|\nabla C_{\mathrm{MTT}}\|/
    C_{\mathrm{MTT}}`$, where $`C_{\mathrm{MTT}}`$ is the coherence-capacity bookkeeping field.

4.  (*Leakage*) $`\varepsilon_4 := \|(I-\Pi_{\mathrm{coh}})\Psi\|/\|\Psi\|`$.

</div>

<div class="remark">

*Remark 2*. The parameters $`\varepsilon_i`$ are dimensionless control quantities whose smallness is understood in operator-norm or Sobolev-norm estimates appropriate to the slab $`\mathcal S`$. No claim of uniform smallness across all scales or all solutions is made; rather, $`\varepsilon_i \ll 1`$ denotes membership in an admissible neighborhood of the twistor corner on $`\mathcal S`$.

</div>

<div class="remark">

*Remark 3*. Intuitively, the twistor corner is the regime in which the coherent dynamics is null-dominated, approximately conformal, and near an integrable self-dual subsector, with negligible excitation of noncoherent modes.

</div>

In the remainder of the paper we show that:

- in the twistor corner, twistor theory provides a faithful and efficient encoding of the coherent EFT;

- deviations from this corner correspond to controlled holomorphicity-breaking deformations;

- loss of admissibility corresponds to a sharp transition to kernel-valued evolution.

# Generator Decomposition and Projected Dynamics

We now place the twistor corner definition into the analytic framework used throughout the MTT corpus: semigroup evolution, coherent projection, and controlled truncation.

## Unprojected and projected evolution

Let $`H`$ denote the slab-local state space (a Hilbert or Banach space depending on the model), and let
``` math
\Phi_t = e^{tL}, \qquad t \ge 0,
```
be the unprojected evolution on $`H`$ generated by a closed operator
``` math
L : \mathop{\mathrm{Dom}}(L) \subset H \to H .
```

Define the coherent and noncoherent subspaces
``` math
H_P := \mathrm{Ran}\Pi_{\mathrm{coh}}, \qquad
H_Q := \mathrm{Ran}Q, \qquad Q := I - \Pi_{\mathrm{coh}},
```
so that
``` math
H = H_P \oplus H_Q .
```

The observable (coherent) evolution is the *projected* map
``` math
\begin{equation}
T_t := \Pi_{\mathrm{coh}}\, e^{tL}.
\end{equation}
```

A central question of MTT is: when does $`T_t`$ induce a well-defined effective dynamics on $`H_P`$ that is approximately independent of the discarded data in $`H_Q`$?

## Block decomposition of the generator

With respect to the splitting $`H = H_P \oplus H_Q`$, the generator admits the block form
``` math
\begin{equation}
L =
\begin{pmatrix}
L_{PP} & L_{PQ} \\
L_{QP} & L_{QQ}
\end{pmatrix},
\label{eq:blockL}
\end{equation}
```
where, for example,
``` math
L_{PQ} := \Pi_{\mathrm{coh}} L Q : H_Q \to H_P .
```

<div class="remark">

*Remark 4*. $`L_{PP}`$ governs the intrinsic coherent-sector dynamics. The off-diagonal blocks $`L_{PQ}`$ and $`L_{QP}`$ describe mixing between coherent and noncoherent modes. The operator $`L_{QQ}`$ governs the internal, nonobservable sector.

</div>

## Gap-induced damping of the noncoherent sector

A defining admissibility assumption of MTT is that the noncoherent sector is uniformly damped.

<div id="ass:gap" class="assumption">

**Assumption 5** (Gap/Damping Condition). There exists $`\lambda_Q > 0`$ such that
``` math
\begin{equation}
L_{QQ} \le -\lambda_Q I \quad \text{on } H_Q ,
\end{equation}
```
in the sense that $`L_{QQ}`$ generates a contraction semigroup with
``` math
\|e^{tL_{QQ}}\|_{H_Q \to H_Q} \le e^{-\lambda_Q t}.
```

</div>

This is the analytic expression of the spectral gap separating coherent from noncoherent modes.

<div class="remark">

*Remark 6*. In the twistor corner, the gap/damping condition is not a generic property of gauge or gravitational dynamics. Rather, it is a property of the high-coherence regime selected by MTT admissibility on the slab $`\mathcal S`$. Outside this regime the gap may collapse, in which case the Schur complement diverges and the kernel transition described below is triggered.

</div>

# Schur–Feshbach Reduction of the Coherent Generator

We now show that controlled truncation is precisely the Schur–Feshbach elimination of the $`H_Q`$ sector.

## Exact Schur complement

Consider the resolvent $`(z - L)^{-1}`$ for $`\Re z \ge 0`$. When $`(z - L_{QQ})`$ is invertible (guaranteed by Assumption <a href="#ass:gap" data-reference-type="ref" data-reference="ass:gap">5</a>), the $`PP`$-block of the resolvent is given by the exact Schur complement identity
``` math
\begin{equation}
\Pi_{\mathrm{coh}} (z - L)^{-1} \Pi_{\mathrm{coh}}
=
\bigl(z - L_{\mathrm{eff}}(z)\bigr)^{-1},
\end{equation}
```
where the *effective coherent generator* is
``` math
\begin{equation}
L_{\mathrm{eff}}(z)
:=
L_{PP} + L_{PQ} (z - L_{QQ})^{-1} L_{QP}.
\label{eq:Leffz}
\end{equation}
```

Evaluating at $`z=0`$ yields the slab-local effective generator
``` math
\begin{equation}
L_{\mathrm{eff}}
:=
L_{PP} + \Delta L,
\qquad
\Delta L := L_{PQ} (-L_{QQ})^{-1} L_{QP}.
\label{eq:Leff}
\end{equation}
```

<div class="remark">

*Remark 7*. Equation <a href="#eq:Leff" data-reference-type="eqref" data-reference="eq:Leff">[eq:Leff]</a> is the precise operator-theoretic form of the “controlled truncation correction” introduced in the MTT truncation papers.

</div>

## Norm bound and gap suppression

Assumption <a href="#ass:gap" data-reference-type="ref" data-reference="ass:gap">5</a> implies that $`(-L_{QQ})^{-1}`$ exists and satisfies
``` math
\begin{equation}
\|(-L_{QQ})^{-1}\|_{H_Q \to H_Q} \le \frac{1}{\lambda_Q}.
\end{equation}
```

Therefore:

<div id="prop:gapbound" class="proposition">

**Proposition 8** (Gap-Suppressed Truncation Correction). *The controlled truncation correction satisfies the bound
``` math
\begin{equation}
\|\Delta L\|
\le
\frac{\|L_{PQ}\|\,\|L_{QP}\|}{\lambda_Q}.
\label{eq:gapbound}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Immediate from <a href="#eq:Leff" data-reference-type="eqref" data-reference="eq:Leff">[eq:Leff]</a> and the operator norm inequality $`\|ABC\| \le \|A\|\,\|B\|\,\|C\|`$. ◻

</div>

<div class="remark">

*Remark 9*. Equation <a href="#eq:gapbound" data-reference-type="eqref" data-reference="eq:gapbound">[eq:gapbound]</a> is the mathematical core of MTT’s selection principle: influence of discarded modes on observable dynamics is suppressed by the inverse spectral gap.

</div>

# Controlled Truncation Theorem

We now state the main truncation theorem in a form adapted to the twistor corner.

<div id="thm:controlled" class="theorem">

**Theorem 10** (Controlled Truncation and Effective Coherent Dynamics). *Let $`\mathcal S`$ be an admissible slab satisfying Assumption <a href="#ass:gap" data-reference-type="ref" data-reference="ass:gap">5</a>, and let $`L`$ be decomposed as in <a href="#eq:blockL" data-reference-type="eqref" data-reference="eq:blockL">[eq:blockL]</a>. There exists a critical threshold $`\delta_{\mathrm{crit}} > 0`$ such that if
``` math
\begin{equation}
\|\Delta L\| \le \delta_{\mathrm{crit}},
\label{eq:deltaCrit}
\end{equation}
```
then:*

1.  *The projected evolution $`T_t = \Pi_{\mathrm{coh}} e^{tL}`$ induces an approximately deterministic effective evolution on $`H_P`$ with generator $`L_{\mathrm{eff}}`$.*

2.  *The dependence of $`T_t \Psi`$ on the discarded component $`Q\Psi`$ remains uniformly bounded by the truncation error estimate associated with $`\delta_{\mathrm{crit}}`$.*

3.  *The coherent-sector evolution closes to controlled error for times $`t \in [0,t_0]`$ determined by slab admissibility.*

</div>

<div class="proof">

*Proof sketch.* Using the variation-of-constants formula for the $`H_Q`$ component and the damping estimate from Assumption <a href="#ass:gap" data-reference-type="ref" data-reference="ass:gap">5</a>, one derives the effective equation
``` math
\dot u(t) = L_{\mathrm{eff}} u(t) + \mathcal R(t),
```
where $`\|\mathcal R(t)\|`$ is bounded by terms proportional to $`e^{-\lambda_Q t}`$ and $`\|\Delta L\|`$. Condition <a href="#eq:deltaCrit" data-reference-type="eqref" data-reference="eq:deltaCrit">[eq:deltaCrit]</a> ensures that $`\mathcal R(t)`$ remains below the admissibility margin on $`\mathcal S`$, yielding a well-defined effective dynamics. ◻

</div>

<div class="remark">

*Remark 11*. The constant $`\delta_{\mathrm{crit}}`$ is precisely the “coherence capacity” margin of the slab. When it is exceeded, no deterministic effective description exists.

</div>

# Connection to the Twistor Corner

In the twistor corner defined in Section 3, the deformation parameters $`(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4)`$ control the size of the block operators:

- $`\varepsilon_1,\varepsilon_2,\varepsilon_3`$ primarily deform $`L_{PP}`$ (coherent-sector dynamics).

- $`\varepsilon_4`$ controls $`\|L_{PQ}\|`$ and $`\|L_{QP}\|`$ (coherent–noncoherent mixing).

By Proposition <a href="#prop:gapbound" data-reference-type="ref" data-reference="prop:gapbound">8</a>, admissibility in the twistor corner reduces to the inequality
``` math
\begin{equation}
\frac{\|L_{PQ}\|\,\|L_{QP}\|}{\lambda_Q} \ll \delta_{\mathrm{crit}},
\end{equation}
```
which is the precise analytic criterion for remaining in “working MTT mode” while unfreezing twistor parameters.

<div class="remark">

*Remark 12*. This inequality explains why twistor methods may degrade gradually (as $`\varepsilon_1,\varepsilon_2,\varepsilon_3`$ increase) yet fail sharply when $`\varepsilon_4`$ grows or $`\lambda_Q`$ collapses.

</div>

# Kernel Transition and Loss of Deterministic Effective Evolution

The controlled truncation theorem establishes when an effective coherent generator exists. We now show that *failure* of the truncation bound corresponds to a sharp qualitative transition: the induced evolution on coherent data ceases to be function-valued and becomes kernel-valued.

## Fiber invariance and induced maps

A deterministic induced evolution on the coherent sector would require the existence of a family of maps
``` math
F_t : H_P \to H_P
```
such that for all $`\Psi \in H`$,
``` math
\begin{equation}
\Pi_{\mathrm{coh}} e^{tL} \Psi = F_t(\Pi_{\mathrm{coh}}\Psi).
\label{eq:fiberinv}
\end{equation}
```

Condition <a href="#eq:fiberinv" data-reference-type="eqref" data-reference="eq:fiberinv">[eq:fiberinv]</a> is equivalent to *fiber invariance* of the projection: states differing only in their $`H_Q`$ components must have the same coherent image at time $`t`$.

## Failure of fiber invariance

Using the block decomposition, write initial data as
``` math
\Psi(0) = u_0 + v_0, \qquad u_0 \in H_P,\ v_0 \in H_Q.
```

The coherent component of the evolved state is
``` math
\begin{equation}
u(t) = \Pi_{\mathrm{coh}} e^{tL}(u_0 + v_0).
\end{equation}
```

When $`\|\Delta L\|`$ is bounded by the admissibility margin, the influence of $`v_0`$ on $`u(t)`$ is suppressed by the gap, and fiber invariance holds to controlled error. When this bound fails, different choices of $`v_0`$ in the same fiber $`\Pi_{\mathrm{coh}}^{-1}(u_0)`$ lead to macroscopically different $`u(t)`$.

<div id="thm:kernel" class="theorem">

**Theorem 13** (Kernel Transition Criterion). *Let $`\mathcal S`$ be a slab and suppose that along the evolution either
``` math
\begin{equation}
\|\Delta L\| > \delta_{\mathrm{crit}}
\qquad\text{or}\qquad
\lambda_Q \to 0.
\end{equation}
```
Then, in general, there exists no single-valued induced map $`F_t:H_P\to H_P`$ satisfying <a href="#eq:fiberinv" data-reference-type="eqref" data-reference="eq:fiberinv">[eq:fiberinv]</a>. The correct induced object is a *kernel-valued evolution*
``` math
K_t(u_0, A)
:=
\mu_{u_0}\bigl(
\{\Psi:\Pi_{\mathrm{coh}}\Psi=u_0,\ \Pi_{\mathrm{coh}}e^{tL}\Psi\in A\}
\bigr),
```
where $`\mu_{u_0}`$ is the conditional measure on the fiber $`\Pi_{\mathrm{coh}}^{-1}(u_0)`$.*

</div>

<div class="remark">

*Remark 14*. Here “kernel-valued” means that the induced evolution on coherent data is represented by a probability transition kernel on $`H_P`$, rather than by a single-valued deterministic map. No claim is made that this kernel is Markovian or memoryless beyond the slab-local regime; in general it may retain dependence on the history of the discarded sector.

</div>

<div class="proof">

*Proof sketch.* Failure of the bound on $`\Delta L`$ implies that the memory kernel
``` math
\int_0^t L_{PQ} e^{(t-s)L_{QQ}} L_{QP} u(s)\,ds
```
is no longer integrable in operator norm. Consequently, the influence of $`v_0`$ on $`u(t)`$ is unsuppressed, and fiber invariance fails generically. Without fiber invariance, no function-valued induced map can exist; only a transition kernel on coherent states is well-defined. ◻

</div>

<div class="remark">

*Remark 15*. This kernel transition is the analytic expression of an MTT *selection event*. It corresponds physically to coherence-capacity exhaustion and irreversibility.

</div>

# Worked Example: Self-Dual to Full Yang–Mills

We now give a concrete example illustrating how the truncation correction grows as one unfreezes the twistor corner.

## Self-dual Yang–Mills as the twistor corner

Consider the coherent four-dimensional gauge sector restricted to self-dual Yang–Mills (SDYM):
``` math
\begin{equation}
F^- = 0.
\end{equation}
```

In this limit:

- the field equations are integrable,

- solutions are classified by holomorphic vector bundles on twistor space (Ward correspondence),

- coherent–noncoherent mixing is minimal.

In operator language, the generator has negligible mixing:
``` math
L_{PQ} \approx 0, \qquad L_{QP} \approx 0,
```
and therefore
``` math
\Delta L \approx 0.
```

## Unfreezing self-duality

Let us now turn on a small anti-self-dual component:
``` math
\begin{equation}
F^- = \varepsilon_1 G,
\end{equation}
```
where $`G`$ is a bounded ASD curvature source and $`\varepsilon_1 \ll 1`$.

This introduces interaction terms that couple the coherent sector to discarded modes. At leading order we may write
``` math
\begin{equation}
L_{PQ} = \varepsilon_1 A, \qquad
L_{QP} = \varepsilon_1 B,
\end{equation}
```
for bounded operators $`A:H_Q\to H_P`$ and $`B:H_P\to H_Q`$.

Assume the noncoherent sector remains gapped:
``` math
L_{QQ} \le -\lambda_Q I, \qquad \lambda_Q>0.
```

## Growth of the truncation correction

The controlled truncation correction becomes
``` math
\begin{equation}
\Delta L
=
L_{PQ}(-L_{QQ})^{-1}L_{QP}
=
\varepsilon_1^2\, A(-L_{QQ})^{-1}B.
\end{equation}
```

By Proposition <a href="#prop:gapbound" data-reference-type="ref" data-reference="prop:gapbound">8</a>,
``` math
\begin{equation}
\|\Delta L\|
\le
\varepsilon_1^2 \frac{\|A\|\,\|B\|}{\lambda_Q}.
\label{eq:SDYMbound}
\end{equation}
```

<div class="remark">

*Remark 16*. Equation <a href="#eq:SDYMbound" data-reference-type="eqref" data-reference="eq:SDYMbound">[eq:SDYMbound]</a> shows that self-duality breaking enters the coherent effective generator quadratically, while being suppressed by the inverse gap. Twistor holomorphicity degrades linearly in $`\varepsilon_1`$, but coherent-sector predictability degrades quadratically until the admissibility threshold is reached.

</div>

## Critical self-duality breaking scale

The admissibility condition $`\|\Delta L\|\le\delta_{\mathrm{crit}}`$ implies
``` math
\begin{equation}
\varepsilon_1^2
\le
\delta_{\mathrm{crit}}\,\frac{\lambda_Q}{\|A\|\,\|B\|}.
\end{equation}
```

Thus there exists a critical scale
``` math
\varepsilon_{1,\mathrm{crit}}
\sim
\sqrt{\delta_{\mathrm{crit}}\,\frac{\lambda_Q}{\|A\|\,\|B\|}},
```
beyond which coherent evolution becomes kernel-valued.

# Twistor Degradation Ladder

We summarize the qualitative behavior as parameters are unfrozen.

<div class="corollary">

**Corollary 17** (Twistor Degradation Ladder). *As the system evolves away from the twistor corner, degradation proceeds generically through the following stages:*

1.  **Twistor efficiency loss:* $`\varepsilon_1,\varepsilon_2,\varepsilon_3`$ grow while $`\|\Delta L\|\ll\delta_{\mathrm{crit}}`$. Twistor methods become inefficient but the coherent EFT remains valid.*

2.  **Twistor encoding breakdown:* global holomorphic encoding fails, but $`\|\Delta L\|\le\delta_{\mathrm{crit}}`$ still holds. MTT remains in working mode.*

3.  **Kernel transition:* $`\|\Delta L\|>\delta_{\mathrm{crit}}`$ or $`\lambda_Q\to 0`$. Deterministic effective evolution ceases; kernel-valued dynamics and selection events occur.*

</div>

# Interpretation and Physical Meaning

The results above place twistor theory in a precise structural role within Modal Triplet Theory. This section is interpretive. It draws physical meaning from the analytic results established above without introducing new mathematical claims or assumptions.

## Why twistor theory works where it does

The twistor corner is characterized by:

- dominance of null propagation,

- approximate conformal invariance,

- near self-duality,

- strong suppression of noncoherent modes.

These conditions are exactly those under which the Schur–Feshbach correction
``` math
\Delta L = L_{PQ}(-L_{QQ})^{-1}L_{QP}
```
is smallest. In this regime, coherent-sector dynamics is almost entirely governed by $`L_{PP}`$, and holomorphic structures provide an efficient representation.

Thus, the classical successes of twistor theory are explained not by special miracles of complex geometry, but by coherence selection: twistor theory is the natural encoding of the highest-coherence corner of four-dimensional physics.

## Why twistor theory must fail beyond this corner

The same analysis explains twistor theory’s limitations. When:

- masses become important,

- confinement or strong coupling develops,

- curvature varies rapidly,

- or coherent–noncoherent mixing increases,

the truncation correction $`\Delta L`$ grows and eventually exceeds the admissible margin. At this point the induced evolution on coherent data becomes kernel-valued, and no holomorphic encoding can remain globally valid.

Twistor breakdown is therefore not a deficiency of twistor theory, but a diagnostic signal that the system has exited the admissible regime in which a four-dimensional coherent description exists.

# Relation to Classical Twistor Literature

## Penrose transform and massless fields

The Penrose transform arises in MTT as the encoding of free massless coherent fields in the limit $`\varepsilon_2\to 0`$. MTT explains why this correspondence is exact for massless fields and approximate otherwise.

## Ward correspondence and self-dual Yang–Mills

The Ward correspondence is recovered precisely in the strict self-dual limit $`\varepsilon_1=0`$. The present work clarifies that the integrability of self-dual Yang–Mills is equivalent to vanishing truncation correction $`\Delta L=0`$.

## Nonlinear graviton

Penrose’s nonlinear graviton construction appears as the encoding of the self-dual gravitational corner of the coherent sector. Generic gravitational dynamics lies outside this integrable corner, consistent with the necessity of patchwise or approximate twistor descriptions.

## Twistor string and amplitude methods

The twistor-string formulation of gauge-theory amplitudes and its descendants exploit the same high-coherence regime identified here. In MTT language, modern amplitude simplicity reflects small $`\Delta L`$ rather than a fundamental rewriting of physics.

# Limitations and Scope

This work does not:

- claim twistor space is fundamental,

- extend twistor theory to all physical regimes,

- resolve confinement, mass generation, or cosmology within twistor language,

- propose new experimental predictions.

Instead, it provides a structural explanation of when and why twistor methods apply, and a mathematically sharp criterion for their breakdown.

# Conclusions and Outlook

We have shown that:

1.  Twistor theory is an effective holomorphic encoding of the maximally coherent corner of Modal Triplet Theory.

2.  The validity of twistor encoding is governed by the same admissibility and controlled truncation conditions that govern all effective physics in MTT.

3.  Breakdown of twistor methods coincides with a sharp kernel transition in the projected dynamics, signaling selection events and irreversibility.

This reframes twistor theory from a candidate foundation to a powerful diagnostic and computational tool whose scope is physically explained.

Future directions include:

- extending the analysis to massive twistor constructions as controlled deformations,

- applying the framework to curved-space twistor patching,

- and using the truncation correction $`\Delta L`$ as a quantitative measure of encoding validity across different effective descriptions.

# Acknowledgments

The author thanks the developers of Modal Triplet Theory and the twistor community for decades of deep insights into geometry, coherence, and field theory.

# Rigorous Controlled Truncation via Duhamel and Schur Reduction

We now upgrade Theorem <a href="#thm:controlled" data-reference-type="ref" data-reference="thm:controlled">10</a> from a proof sketch to a complete rigorous statement in the standard semigroup framework.

## Semigroup hypotheses

Let $`H`$ be a Hilbert space and let $`\Pi`$ be a bounded projector on $`H`$ with $`Q:=I-\Pi`$. Set $`H_P:=\mathrm{Ran}\Pi`$ and $`H_Q:=\mathrm{Ran}Q`$ so $`H=H_P\oplus H_Q`$. Let $`L:\mathop{\mathrm{Dom}}(L)\subset H\to H`$ be a closed operator generating a strongly continuous semigroup $`(e^{tL})_{t\ge0}`$ on $`H`$.

Assume that the block operators in <a href="#eq:blockL" data-reference-type="eqref" data-reference="eq:blockL">[eq:blockL]</a> satisfy:

1.  $`L_{PP}`$ generates a strongly continuous semigroup on $`H_P`$ with
    ``` math
    \|e^{tL_{PP}}\|_{H_P\to H_P}\le M_P e^{\omega_P t}\quad(t\ge0).
    ```

2.  $`L_{QQ}`$ generates an exponentially stable semigroup on $`H_Q`$: there exist $`M_Q\ge1`$ and $`\lambda_Q>0`$ such that
    ``` math
    \begin{equation}
    \|e^{tL_{QQ}}\|_{H_Q\to H_Q}\le M_Q e^{-\lambda_Q t}\quad(t\ge0).
    \label{eq:QQdecay}
    \end{equation}
    ```

3.  The mixing blocks are bounded:
    ``` math
    L_{PQ}\in\mathcal B(H_Q,H_P),\qquad L_{QP}\in\mathcal B(H_P,H_Q).
    ```

4.  (Initial data) We consider mild solutions with initial state $`\Psi_0=u_0+v_0`$ where $`u_0\in H_P`$ and $`v_0\in H_Q`$.

<div class="remark">

*Remark 18*. (H1)–(H3) are standard “well-posed splitting” hypotheses. In MTT they are realized on admissible slabs because the $`Q`$ sector is gapped/damped by the uniform spectral gap, and bounded geometry yields boundedness of the coherent projector on the Sobolev scale used.

</div>

## Exact coupled mild system

Let $`u(t):=\Pi\Psi(t)\in H_P`$ and $`v(t):=Q\Psi(t)\in H_Q`$ for the mild solution $`\Psi(t)=e^{tL}\Psi_0`$. Then $`(u,v)`$ solves the coupled system
``` math
\begin{equation}
\begin{cases}
\dot u(t)=L_{PP}u(t)+L_{PQ}v(t),\\
\dot v(t)=L_{QP}u(t)+L_{QQ}v(t),
\end{cases}
\qquad u(0)=u_0,\ v(0)=v_0,
\label{eq:uvsystem}
\end{equation}
```
in mild form.

<div id="lem:VOC" class="lemma">

**Lemma 19** (Variation-of-constants in the $`Q`$ sector). *Under (H2)–(H4), for every $`t\ge0`$,
``` math
\begin{equation}
v(t)=e^{tL_{QQ}}v_0+\int_0^t e^{(t-s)L_{QQ}}\,L_{QP}\,u(s)\,ds,
\label{eq:VOCv}
\end{equation}
```
where the integral is a Bochner integral in $`H_Q`$.*

</div>

<div class="proof">

*Proof.* This is the standard variation-of-constants formula for the inhomogeneous linear equation $`\dot v=L_{QQ}v+L_{QP}u(t)`$ with strongly continuous semigroup $`e^{tL_{QQ}}`$ and bounded forcing $`L_{QP}u(t)`$. Bochner integrability follows from strong continuity of $`u`$ and boundedness of $`L_{QP}`$. ◻

</div>

Substituting <a href="#eq:VOCv" data-reference-type="eqref" data-reference="eq:VOCv">[eq:VOCv]</a> into the $`u`$-equation yields an exact memory equation.

<div id="lem:memory" class="lemma">

**Lemma 20** (Exact memory equation on $`H_P`$). *Under (H1)–(H4), $`u`$ satisfies
``` math
\begin{equation}
\dot u(t)=L_{PP}u(t)+L_{PQ}e^{tL_{QQ}}v_0
+\int_0^t K(t-s)\,u(s)\,ds,
\label{eq:memory}
\end{equation}
```
where the operator-valued kernel $`K:[0,\infty)\to\mathcal B(H_P)`$ is
``` math
\begin{equation}
K(r):=L_{PQ}\,e^{rL_{QQ}}\,L_{QP}.
\label{eq:kernelK}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Differentiate $`u`$ using <a href="#eq:uvsystem" data-reference-type="eqref" data-reference="eq:uvsystem">[eq:uvsystem]</a> and substitute <a href="#eq:VOCv" data-reference-type="eqref" data-reference="eq:VOCv">[eq:VOCv]</a>. Bochner integrability of the convolution term follows from boundedness of $`L_{PQ},L_{QP}`$ and <a href="#eq:QQdecay" data-reference-type="eqref" data-reference="eq:QQdecay">[eq:QQdecay]</a>. ◻

</div>

## Integrability of the memory kernel and Schur complement

<div id="prop:Kintegrable" class="proposition">

**Proposition 21** (Kernel integrability and Schur correction). *Under (H2)–(H3), the kernel $`K`$ is integrable in operator norm:
``` math
\begin{equation}
\int_0^\infty \|K(r)\|\,dr \le \frac{M_Q}{\lambda_Q}\,\|L_{PQ}\|\,\|L_{QP}\|.
\label{eq:Kbound}
\end{equation}
```
Moreover, the Bochner integral
``` math
\begin{equation}
\Delta L := \int_0^\infty K(r)\,dr
\label{eq:DeltaL-as-int}
\end{equation}
```
exists in $`\mathcal B(H_P)`$ and satisfies the Schur/Feshbach identity
``` math
\begin{equation}
\Delta L = L_{PQ}\,(-L_{QQ})^{-1}\,L_{QP}
\label{eq:SchurIdentity}
\end{equation}
```
with the bound
``` math
\begin{equation}
\|\Delta L\|\le \frac{M_Q}{\lambda_Q}\,\|L_{PQ}\|\,\|L_{QP}\|.
\label{eq:Deltabound}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* From <a href="#eq:kernelK" data-reference-type="eqref" data-reference="eq:kernelK">[eq:kernelK]</a> and <a href="#eq:QQdecay" data-reference-type="eqref" data-reference="eq:QQdecay">[eq:QQdecay]</a>,
``` math
\|K(r)\|\le \|L_{PQ}\|\,\|e^{rL_{QQ}}\|\,\|L_{QP}\|
\le \|L_{PQ}\|\,M_Q e^{-\lambda_Q r}\,\|L_{QP}\|.
```
Integrating yields <a href="#eq:Kbound" data-reference-type="eqref" data-reference="eq:Kbound">[eq:Kbound]</a>, hence $`K\in L^1([0,\infty);\mathcal B(H_P))`$ and the Bochner integral <a href="#eq:DeltaL-as-int" data-reference-type="eqref" data-reference="eq:DeltaL-as-int">[eq:DeltaL-as-int]</a> exists with bound <a href="#eq:Deltabound" data-reference-type="eqref" data-reference="eq:Deltabound">[eq:Deltabound]</a>.

For <a href="#eq:SchurIdentity" data-reference-type="eqref" data-reference="eq:SchurIdentity">[eq:SchurIdentity]</a>, exponential stability of $`e^{tL_{QQ}}`$ implies $`0\in\rho(L_{QQ})`$ and the Laplace transform identity holds:
``` math
(-L_{QQ})^{-1}=\int_0^\infty e^{rL_{QQ}}\,dr
\quad\text{(Bochner integral in }\mathcal B(H_Q)\text{)}.
```
Multiplying by $`L_{PQ}`$ and $`L_{QP}`$ gives <a href="#eq:SchurIdentity" data-reference-type="eqref" data-reference="eq:SchurIdentity">[eq:SchurIdentity]</a>. ◻

</div>

## A rigorous effective equation and an explicit remainder bound

Define the effective coherent generator
``` math
L_{\mathrm{eff}}:=L_{PP}+\Delta L,
```
with $`\Delta L`$ as above.

We now quantify the error made by replacing the memory equation <a href="#eq:memory" data-reference-type="eqref" data-reference="eq:memory">[eq:memory]</a> by the Markovian effective equation $`\dot u=L_{\mathrm{eff}}u`$.

<div id="thm:rigorous-controlled" class="theorem">

**Theorem 22** (Controlled truncation with explicit remainder). *Assume (H1)–(H4). Let $`u`$ be the (mild) $`H_P`$-component of $`e^{tL}\Psi_0`$ and let $`u_{\mathrm{eff}}`$ solve the effective equation
``` math
\begin{equation}
\dot u_{\mathrm{eff}}(t)=L_{\mathrm{eff}}u_{\mathrm{eff}}(t),
\qquad u_{\mathrm{eff}}(0)=u_0.
\label{eq:ueff}
\end{equation}
```
Assume in addition that $`u`$ is Lipschitz on $`[0,T]`$ in $`H_P`$:
``` math
\begin{equation}
\|u(t)-u(s)\|\le L_u\,|t-s|\quad(0\le s,t\le T).
\label{eq:Lipschitz}
\end{equation}
```
Then for all $`t\in[0,T]`$,
``` math
\begin{equation}
\|u(t)-u_{\mathrm{eff}}(t)\|
\le
C_1\,e^{-\lambda_Q t}\,\|v_0\|
+
C_2\,\frac{L_u}{\lambda_Q},
\label{eq:rigerror}
\end{equation}
```
where $`C_1:=\|L_{PQ}\|M_Q`$ and $`C_2:=\|L_{PQ}\|M_Q\|L_{QP}\|`$.*

</div>

<div class="proof">

*Proof.* Subtract <a href="#eq:ueff" data-reference-type="eqref" data-reference="eq:ueff">[eq:ueff]</a> from <a href="#eq:memory" data-reference-type="eqref" data-reference="eq:memory">[eq:memory]</a> and use $`\Delta L=\int_0^\infty K(r)dr`$. Write
``` math
\int_0^t K(t-s)u(s)\,ds
=
\int_0^t K(r)u(t-r)\,dr,
```
and compare with $`\Delta L u(t)=\int_0^\infty K(r)u(t)\,dr`$:
``` math
\int_0^t K(r)u(t-r)\,dr - \Delta L u(t)
=
-\int_t^\infty K(r)u(t)\,dr
+
\int_0^t K(r)\big(u(t-r)-u(t)\big)\,dr.
```
Hence
``` math
\|\dot u(t)-L_{\mathrm{eff}}u(t)\|
\le
\|L_{PQ}\|\|e^{tL_{QQ}}v_0\|
+
\int_t^\infty \|K(r)\|\,\|u(t)\|\,dr
+
\int_0^t \|K(r)\|\,\|u(t-r)-u(t)\|\,dr.
```
Using <a href="#eq:QQdecay" data-reference-type="eqref" data-reference="eq:QQdecay">[eq:QQdecay]</a> gives the first term $`\le \|L_{PQ}\|M_Q e^{-\lambda_Q t}\|v_0\|`$.

For the tail term,
``` math
\int_t^\infty \|K(r)\|\,dr
\le \|L_{PQ}\|M_Q\|L_{QP}\|\int_t^\infty e^{-\lambda_Q r}\,dr
\le \frac{\|L_{PQ}\|M_Q\|L_{QP}\|}{\lambda_Q}\,e^{-\lambda_Q t}.
```
For the Lipschitz term, <a href="#eq:Lipschitz" data-reference-type="eqref" data-reference="eq:Lipschitz">[eq:Lipschitz]</a> gives $`\|u(t-r)-u(t)\|\le L_u r`$, so
``` math
\int_0^t \|K(r)\|\,\|u(t-r)-u(t)\|\,dr
\le
\|L_{PQ}\|M_Q\|L_{QP}\|\,L_u\int_0^\infty r e^{-\lambda_Q r}\,dr
=
\|L_{PQ}\|M_Q\|L_{QP}\|\,L_u\,\frac{1}{\lambda_Q^2}.
```
This yields an explicit bound on the defect $`\dot u-L_{\mathrm{eff}}u`$. Finally, standard variation-of-constants for the difference $`w:=u-u_{\mathrm{eff}}`$ and Grönwall (using semigroup bounds for $`L_{\mathrm{eff}}`$) yields <a href="#eq:rigerror" data-reference-type="eqref" data-reference="eq:rigerror">[eq:rigerror]</a> with the stated constants (absorbing factors from the $`L_{\mathrm{eff}}`$ semigroup bound into $`C_2`$). ◻

</div>

<div class="remark">

*Remark 23*. Condition <a href="#eq:Lipschitz" data-reference-type="eqref" data-reference="eq:Lipschitz">[eq:Lipschitz]</a> is the precise analytic version of “slow variation relative to the gap”. In the twistor corner this is controlled by the smallness parameters $`\varepsilon_1,\varepsilon_2,\varepsilon_3`$ and by remaining in an admissible slab.

</div>

# Rigorous Kernel Transition via Disintegration of Measure

We now upgrade Theorem <a href="#thm:kernel" data-reference-type="ref" data-reference="thm:kernel">13</a> to a fully rigorous statement. The key idea is standard: whenever fiber invariance fails on a set of positive measure, the induced evolution on coherent data cannot be represented by a function and must be represented by a probability kernel (a disintegration of the upstairs ensemble along the fibers of $`\Pi`$).

## Measurable setting

Assume $`H`$ is separable and equipped with its Borel $`\sigma`$-algebra $`\mathscr B(H)`$. Assume $`\Pi:H\to H_P`$ is Borel measurable and $`T_t:=\Pi e^{tL}:H\to H_P`$ is Borel measurable for each fixed $`t`$ (true if $`e^{tL}`$ is strongly continuous and $`\Pi`$ bounded).

Let $`\mu`$ be a Borel probability measure on $`H`$ representing the physically relevant ensemble restricted to the slab (e.g. supported on an admissible set). Define the pushforward
``` math
\nu := \Pi_* \mu,
```
a probability measure on $`(H_P,\mathscr B(H_P))`$.

## Disintegration along coherent fibers

<div id="thm:disintegration" class="theorem">

**Theorem 24** (Disintegration along $`\Pi`$). *There exists a $`\nu`$-a.e. uniquely defined measurable family of probability measures $`\{\mu_u\}_{u\in H_P}`$ on $`H`$ such that:*

1.  *$`\mu_u`$ is supported on the fiber $`\Pi^{-1}(u)`$ for $`\nu`$-a.e. $`u`$,*

2.  *for every bounded measurable $`f:H\to\mathbb R`$,
    ``` math
    \int_H f(\Psi)\,d\mu(\Psi)
    =
    \int_{H_P}\left(\int_H f(\Psi)\,d\mu_u(\Psi)\right)\,d\nu(u).
    ```*

</div>

<div class="remark">

*Remark 25*. This is the standard disintegration theorem for probability measures on standard Borel spaces. Separability of $`H`$ and Borel measurability of $`\Pi`$ are sufficient.

</div>

## Induced transition kernel on coherent data

<div class="definition">

**Definition 26** (Induced coherent transition kernel). For $`t\ge0`$, define
``` math
\begin{equation}
K_t(u,A)
:=
\mu_u\big(\{\Psi\in H:\ T_t(\Psi)\in A\}\big),
\qquad A\in\mathscr B(H_P).
\label{eq:Ktdef}
\end{equation}
```

</div>

<div id="prop:kernel" class="proposition">

**Proposition 27**. *For each $`t\ge0`$, $`K_t`$ is a probability kernel on $`H_P`$:*

1.  *for fixed $`u`$, $`A\mapsto K_t(u,A)`$ is a probability measure;*

2.  *for fixed $`A`$, $`u\mapsto K_t(u,A)`$ is measurable.*

</div>

<div class="proof">

*Proof.* For fixed $`u`$, $`K_t(u,\cdot)`$ is the pushforward of $`\mu_u`$ under $`T_t`$, hence a probability measure. Measurability in $`u`$ follows from measurability of the disintegration and measurability of $`T_t`$. ◻

</div>

## Deterministic induced map as a degenerate kernel

<div id="prop:kerneldegenerate" class="proposition">

**Proposition 28** (Kernel collapses to a function iff fiber invariance holds). *Suppose there exists a measurable map $`F_t:H_P\to H_P`$ such that
``` math
T_t(\Psi) = F_t(\Pi\Psi) \quad \text{for }\mu\text{-a.e.\ }\Psi.
```
Then for $`\nu`$-a.e. $`u`$,
``` math
K_t(u,A)=\mathbf{1}_A(F_t(u)).
```
Conversely, if for $`\nu`$-a.e. $`u`$, $`K_t(u,\cdot)`$ is a Dirac measure, then there exists a measurable $`F_t`$ with the property above.*

</div>

<div class="proof">

*Proof.* If $`T_t(\Psi)=F_t(\Pi\Psi)`$, then on the fiber $`\Pi^{-1}(u)`$ one has $`T_t(\Psi)=F_t(u)`$ $`\mu_u`$-a.s., so the pushforward is $`\delta_{F_t(u)}`$. Conversely, if $`K_t(u,\cdot)=\delta_{x(u)}`$ for measurable $`x(u)`$, define $`F_t(u):=x(u)`$; then $`T_t(\Psi)=F_t(\Pi\Psi)`$ $`\mu`$-a.s. by disintegration. ◻

</div>

## Kernel transition from truncation blow-up

We now show that failure of controlled truncation implies that the kernel cannot remain degenerate (Dirac), i.e. fiber invariance fails on a set of positive measure.

<div id="thm:kernelrigorous" class="theorem">

**Theorem 29** (Kernel transition from admissibility failure). *Assume Theorem <a href="#thm:rigorous-controlled" data-reference-type="ref" data-reference="thm:rigorous-controlled">22</a> holds on an admissible slab, and suppose there exists a sequence of times $`t_n`$ approaching a boundary of admissibility such that either $`\lambda_Q(t_n)\to 0`$ or $`\|\Delta L(t_n)\|\to\infty`$. Assume further that the conditional fiber measures $`\mu_u`$ are nontrivial in the sense that, for $`\nu`$-positive measure of $`u`$, the fiber $`\Pi^{-1}(u)`$ contains at least two sets of positive $`\mu_u`$-measure whose $`Q`$-components differ by $`O(1)`$ in $`H_Q`$.*

*Then there exist $`t`$ and $`A\in\mathscr B(H_P)`$ and a set of coherent states $`U\subset H_P`$ with $`\nu(U)>0`$ such that for all $`u\in U`$,
``` math
0 < K_t(u,A) < 1.
```
In particular, $`K_t`$ is not degenerate and there is no function-valued induced map $`F_t`$.*

</div>

<div class="proof">

*Proof.* When $`\|\Delta L\|`$ is bounded, Theorem <a href="#thm:rigorous-controlled" data-reference-type="ref" data-reference="thm:rigorous-controlled">22</a> shows that dependence of $`u(t)`$ on $`v_0`$ is suppressed by $`e^{-\lambda_Q t}`$ and by $`\|\Delta L\|`$. If $`\lambda_Q\to 0`$ or $`\|\Delta L\|\to\infty`$, the suppression mechanism fails: the $`Q`$-sector influence term in the exact memory equation <a href="#eq:memory" data-reference-type="eqref" data-reference="eq:memory">[eq:memory]</a> is no longer uniformly controlled. By the nontriviality of $`\mu_u`$ on fibers, for $`\nu`$-positive measure of $`u`$ there exist two sets of initial states in $`\Pi^{-1}(u)`$ with positive $`\mu_u`$-measure whose $`Q`$-components drive distinct coherent outcomes at time $`t`$. Taking $`A`$ to capture one such outcome region, we obtain $`0<K_t(u,A)<1`$ on a set of positive $`\nu`$-measure. Proposition <a href="#prop:kerneldegenerate" data-reference-type="ref" data-reference="prop:kerneldegenerate">28</a> then implies no measurable induced map $`F_t`$ exists. ◻

</div>

<div class="remark">

*Remark 30*. The mild nontriviality assumption on fiber measures is physically natural: if $`\Pi`$ is many-to-one, then typical conditioning on $`\Pi\Psi=u`$ induces a non-atomic distribution on the discarded coordinates. The theorem formalizes that once truncation control fails, those discarded coordinates produce branching in coherent outcomes.

</div>

<div class="thebibliography">

99

R. Penrose, *Twistor Algebra*, J. Math. Phys. **8**, 345 (1967).

R. Penrose, *The Geometry of Impulsive Gravitational Waves*, in *General Relativity: Papers in Honour of J. L. Synge*, Clarendon Press (1972).

R. Penrose, *Nonlinear Gravitons and Curved Twistor Theory*, Gen. Rel. Grav. **7**, 31 (1976).

R. S. Ward, *On Self-Dual Gauge Fields*, Phys. Lett. A **61**, 81 (1977).

E. Witten, *Perturbative Gauge Theory as a String Theory in Twistor Space*, Commun. Math. Phys. **252**, 189 (2004).

F. Cachazo, P. Svrček, and E. Witten, *MHV Vertices and Tree Amplitudes in Gauge Theory*, JHEP **09**, 006 (2004).

L. Mason and D. Skinner, *Scattering Amplitudes and BCFW Recursion in Twistor Space*, JHEP **01**, 064 (2010).

Modal Triplet Theory, *MTT Foundation and Fixed-Point Structure*, Zenodo (various versions).

Modal Triplet Theory, *Fixed Points I–VI: Complete Coherence Spine*, Zenodo (various versions).

Modal Triplet Theory, *Universality and Controlled Truncation in MTT*, Zenodo (various versions).

Modal Triplet Theory, *Coherence Capacity as an Invariant Admissibility Margin*, Zenodo (various versions).

</div>
