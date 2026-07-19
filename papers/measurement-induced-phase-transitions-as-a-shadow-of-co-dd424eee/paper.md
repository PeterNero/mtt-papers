---
abstract: |
  Measurement-induced phase transitions (MIPTs) in monitored many-body systems and collapse-like irreversibility in measurement contexts are typically treated as distinct phenomena. We show that they arise as two effective 4D shadows of the same reduced-dynamical mechanism: noninvertible projection onto an admissible coherent sector with basin stabilization. We formulate a general projected evolution map for reduced states, define admissible basins via contractivity margins, and prove that both MIPTs and collapse thresholds correspond to the same loss of contractivity at basin boundaries. We then establish a finite-strength nonanalytic crossover (“knee”) theorem via a local Ornstein–Uhlenbeck/Kramers reduction near basin boundaries, and prove protocol dependence and Zeno/anti-Zeno structure as unavoidable consequences of noncommutativity between probing and projection. Finally, we show that linear time-homogeneous measurement-only or decoherence-only models cannot reproduce the combined phenomena (knees, protocol dependence, and Zeno/anti-Zeno coexistence) without introducing state-dependent stabilization equivalent to basin dynamics. The results are slab-local and admissibility-conditioned: they apply on bounded-geometry time slabs where controlled truncation and positive stability margins hold. This provides a unifying reduced-dynamical bridge that aligns with, and contributes to, ongoing experimental and theoretical work on monitored circuits, continuous measurement, and irreversibility.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 43e4db0108d380c235d57caae1ae9a111f8c7137e931c3560809ac7c6f54ee18
paper_id: measurement-induced-phase-transitions-as-a-shadow-of-co-dd424eee
release_state: zenodo_released
released_version: v1.0
title: |
  **Measurement-Induced Phase Transitions as a Shadow of Coherence Basin Dynamics**  
  A projection-induced bridge between monitored-circuit transitions and collapse thresholds
zenodo_doi: 10.5281/zenodo.18261632
zenodo_record_id: 18261632
zenodo_url: "https://zenodo.org/records/18261632"
---

# Introduction

Two active research programs have developed largely independently: (i) measurement-induced phase transitions (MIPTs) in monitored many-body and circuit dynamics, diagnosed by changes in entanglement scaling as measurement rate is varied; and (ii) collapse-like irreversibility in measurement contexts, diagnosed by loss of reversibility, sharp threshold behavior, and stabilization into definite outcomes under monitoring.

Despite shared qualitative features—finite-strength transitions, protocol dependence, and Zeno/anti-Zeno effects—there is no generally accepted reduced-dynamical mechanism that unifies these phenomena without introducing model-specific assumptions. This paper provides such a mechanism: both MIPTs and collapse thresholds arise as shadows of a single projection-induced basin transition in reduced state space.

Our approach is strictly reduced-dynamical: no interpretational postulates are invoked. The key structural ingredient is a noninvertible projection onto observable degrees of freedom together with stabilization dynamics that yields admissible basins. Within this framework we identify a common transition mechanism, prove universal knee behavior, and derive protocol dependence and Zeno/anti-Zeno structure.

# Minimal Framework: Projected Dynamics with Admissible Basins

## Underlying and reduced spaces

<div class="definition">

**Definition 1** (Extended configuration space). Let $`\mathcal{H}_{\mathrm{ext}}`$ be a (possibly very large) Hilbert space supporting an “upstairs” description of dynamics. In applications this may be the Hilbert space of a system plus auxiliary degrees of freedom (environment, apparatus, discarded modes), or a higher-dimensional configuration space from which 4D observables are extracted.

</div>

<div class="definition">

**Definition 2** (Reduced observable Hilbert space). Let $`\mathcal H_{4}`$ be the Hilbert space supporting the reduced (observable) description, with reduced density operators $`\rho`$ acting on $`\mathcal H_{4}`$.

</div>

## Noninvertible projection and reduced map

<div id="ass:projection" class="assumption">

**Assumption 3** (Noninvertible projection). There exists a bounded linear map $`P:\mathcal{H}_{\mathrm{ext}}\to \mathcal H_{4}`$ that is generally many-to-one. We assume $`P`$ extends to density operators by the natural pushforward $`\rho \mapsto P \rho P^\dagger`$ on the controlled domain.

</div>

<div id="ass:Phi" class="assumption">

**Assumption 4** (Well-posed microscopic evolution). For each protocol strength parameter $`p`$ and time step $`\Delta t>0`$, there exists a well-posed microscopic evolution map $`\Phi^{(p)}_{\Delta t}`$ on density operators on $`\mathcal{H}_{\mathrm{ext}}`$, such that $`\Phi^{(p)}_{\Delta t}`$ depends continuously on $`p`$ in the operator topology on the slab of interest.

</div>

<div id="def:M" class="definition">

**Definition 5** (Protocol-cycle reduced map). For protocol parameters $`(p,\Delta t)`$, define the reduced protocol map
``` math
\begin{equation}
\label{eq:Mdef}
\mathcal{M}_{p,\Delta t}(\rho)
:=
P\,\Phi^{(p)}_{\Delta t}\!\big(P^\dagger \rho P\big)\,P^\dagger,
\end{equation}
```
whenever $`P^\dagger \rho P`$ lies in the domain of $`\Phi^{(p)}_{\Delta t}`$.

</div>

After $`n`$ cycles (total time $`t=n\Delta t`$),
``` math
\rho(t) = \big(\mathcal{M}_{p,\Delta t}\big)^n(\rho_0).
```

## Controlled truncation and slab-locality

<div id="ass:slab" class="assumption">

**Assumption 6** (Slab-local controlled reduction). All statements in this paper are asserted on bounded-geometry time slabs where: (i) the reduced map $`\mathcal{M}_{p,\Delta t}`$ is well-defined on the controlled domain, (ii) operator norms needed for continuity and contraction estimates are finite, and (iii) stability margins defining admissible basins remain strictly positive away from boundaries.

</div>

## Admissible basins

<div id="def:basin" class="definition">

**Definition 7** (Admissible basin). Fix protocol parameters $`(p,\Delta t)`$. An admissible basin $`\mathcal{B}\subset \mathcal{D}`$ (where $`\mathcal{D}`$ is a controlled domain of reduced states) is a set such that:

1.  **(Invariance)** $`\mathcal{M}_{p,\Delta t}(\mathcal{B})\subseteq \mathcal{B}`$.

2.  **(Contractivity)** There exists $`q(p,\Delta t)\in[0,1)`$ such that for all $`\rho,\sigma\in\mathcal{B}`$,
    ``` math
    d\!\left(\mathcal{M}_{p,\Delta t}(\rho),\mathcal{M}_{p,\Delta t}(\sigma)\right)
    \le q(p,\Delta t)\,d(\rho,\sigma),
    ```
    for a chosen metric $`d`$ on $`\mathcal{D}`$ compatible with the trace norm.

3.  **(Stability margin)** The contractivity factor satisfies $`1-q(p,\Delta t)\ge \epsilon`$ for some $`\epsilon>0`$ on the slab for the range of parameters considered.

</div>

<div class="remark">

*Remark 8*. The specific metric $`d`$ is not essential; any metric dominating the trace norm and compatible with the topology of trace-class operators suffices. The stability margin is the key ingredient for basin robustness and threshold analysis.

</div>

# Measurement-Induced Phase Transitions as a 4D Shadow

In monitored circuit and hybrid unitary-measurement dynamics, one varies a measurement rate (or strength) parameter $`p`$, and observes a sharp change in long-time entanglement scaling. In the present framework, this is captured by a change in invariant basin structure of $`\mathcal{M}_{p,\Delta t}`$ as $`p`$ is varied.

<div class="definition">

**Definition 9** (MIPT (reduced-dynamical formulation)). A measurement-induced phase transition occurs at $`p=p_\ast`$ if the set of admissible basins (or the stability margins of the dominant invariant basin) changes discontinuously in the sense that no single basin decomposition with uniformly positive margin persists across $`p_\ast`$.

</div>

The remainder of the paper does not require a specific many-body model; it only requires the existence of basins and continuity in $`p`$ on the slab (Assumptions <a href="#ass:Phi" data-reference-type="ref" data-reference="ass:Phi">4</a>, <a href="#ass:slab" data-reference-type="ref" data-reference="ass:slab">6</a>).

# Collapse and Irreversibility as a 4D Shadow

In collapse-like settings, one prepares an initial reduced state $`\rho_0`$ within an admissible basin and asks for the probability of exiting that basin and stabilizing elsewhere under monitoring.

<div class="definition">

**Definition 10** (Basin survival and exit probabilities). Let $`\mathcal{B}`$ be an admissible basin and $`\Pi_{\mathcal{B}}`$ a (possibly coarse) projector or indicator functional that detects membership in $`\mathcal{B}`$ within the controlled domain. Define:
``` math
P_{\mathrm{surv}}(p,t) := \mathop{\mathrm{Tr}}\!\left(\Pi_{\mathcal{B}}\,\rho(t)\right),
\qquad
P_{\mathrm{exit}}(p,t) := 1-P_{\mathrm{surv}}(p,t).
```
A collapse-like irreversibility event corresponds to basin exit followed by capture into a competing basin.

</div>

# Measurement–Collapse Shadow Bridge

## Control parameters and reduced dynamics

The protocol parameters $`(p,\Delta t)`$ appear both in monitored-circuit dynamics and in measurement-induced collapse experiments. In the present setting, both are encoded by the same reduced map $`\mathcal{M}_{p,\Delta t}`$ (Definition <a href="#def:M" data-reference-type="ref" data-reference="def:M">5</a>).

## Two shadows of the same basin structure

- **Shadow A (MIPT):** diagnosed by long-time entanglement scaling properties, which depend on the invariant basin structure as $`p`$ varies.

- **Shadow B (collapse/irreversibility):** diagnosed by basin survival and exit probabilities, i.e. whether the reduced state remains confined to the initial basin.

## Bridge theorem

<div id="thm:bridge" class="theorem">

**Theorem 11** (Measurement–Collapse Shadow Equivalence). *Assume:*

1.  *the reduced dynamics is given by $`\rho(t+\Delta t)=\mathcal{M}_{p,\Delta t}(\rho(t))`$ on a slab-local controlled domain $`\mathcal{D}`$;*

2.  *admissible basins exist for $`p`$ in an interval $`I\subset\mathbb{R}`$ except possibly at isolated transition values;*

3.  *$`\mathcal{M}_{p,\Delta t}`$ depends continuously on $`p`$ in operator topology on the slab.*

*Then:*

1.  *a measurement-induced phase transition at $`p=p_\ast`$ (defined as a change in admissible basin structure) is equivalent to loss of contractivity margin at a basin boundary at $`p=p_\ast`$;*

2.  *the same critical value $`p_\ast`$ governs collapse-like basin exit from any basin whose margin vanishes at that boundary.*

</div>

<div class="proof">

*Proof.* By Definition <a href="#def:basin" data-reference-type="ref" data-reference="def:basin">7</a>, an admissible basin requires a strictly positive contractivity margin. A measurement-induced phase transition in the reduced-dynamical sense occurs when no basin decomposition with uniform positive margin persists across $`p_\ast`$, i.e. when the margin vanishes for at least one dynamically relevant basin. This is precisely loss of contractivity at a basin boundary. Basin exit becomes non-negligible once the stability margin collapses, so the same $`p_\ast`$ also marks the onset of collapse-like irreversibility for states supported near that boundary. ◻

</div>

<div class="remark">

*Remark 12*. The theorem is slab-local and does not assume a particular microscopic measurement model. The only essential ingredients are noninvertible projection (Assumption <a href="#ass:projection" data-reference-type="ref" data-reference="ass:projection">3</a>), basin stabilization (Definition <a href="#def:basin" data-reference-type="ref" data-reference="def:basin">7</a>), and continuity in $`p`$ (Assumption <a href="#ass:Phi" data-reference-type="ref" data-reference="ass:Phi">4</a>).

</div>

# Finite-Strength Threshold (“Knee”) Structure

In this section we prove that the common basin transition of Theorem <a href="#thm:bridge" data-reference-type="ref" data-reference="thm:bridge">11</a> generically produces a finite-strength, nonanalytic crossover (“knee”) in basin exit probabilities, thereby explaining why both MIPTs and collapse thresholds are sharp in practice.

## Local reduction near a basin boundary

Fix a basin boundary point where a single direction becomes least stable. Introduce a local coordinate $`u\in\mathbb{R}`$ normal to the boundary such that $`u<0`$ lies inside the basin and $`u>0`$ corresponds to exit.

<div id="ass:OU" class="assumption">

**Assumption 13** (OU reduction near boundary). Near the boundary and on the slab, the effective dynamics of the least-stable coordinate admits the approximation
``` math
\begin{equation}
\label{eq:OU}
\dot u(t) = -\gamma(p)\,u(t) + \eta(t),
\end{equation}
```
where $`\gamma(p)`$ is continuous in $`p`$, and $`\eta(t)`$ is mean-zero Gaussian noise with covariance $`\mathbb{E}[\eta(t)\eta(t')]=2D\,\delta(t-t')`$ for some $`D>0`$.

</div>

<div id="lem:critical" class="lemma">

**Lemma 14** (Finite critical protocol strength). *Under Assumptions <a href="#ass:slab" data-reference-type="ref" data-reference="ass:slab">6</a> and <a href="#ass:OU" data-reference-type="ref" data-reference="ass:OU">13</a>, there exists $`p_\ast`$ such that
``` math
\gamma(p_\ast)=0,\qquad
\gamma(p)>0 \text{ for } p<p_\ast,\qquad
\gamma(p)<0 \text{ for } p>p_\ast.
```*

</div>

<div class="proof">

*Proof.* For sufficiently small $`p`$, admissibility implies contractivity in the least-stable direction, hence $`\gamma(p)>0`$. At the boundary associated with the MIPT/collapse transition, the contractivity margin vanishes, implying $`\gamma(p)\le 0`$ at criticality. Continuity of $`\gamma(p)`$ yields a finite crossing point $`p_\ast`$. ◻

</div>

## Knee theorem

<div id="thm:knee" class="theorem">

**Theorem 15** (Finite-strength knee). *Assume <a href="#ass:slab" data-reference-type="ref" data-reference="ass:slab">6</a> and <a href="#ass:OU" data-reference-type="ref" data-reference="ass:OU">13</a>. Let $`P_{\mathrm{exit}}(p,t)`$ denote the probability that $`u(t)`$ crosses from $`u<0`$ to $`u\ge 0`$ by time $`t`$, starting from an initial distribution supported in $`u<0`$. Then, on the slab time window where exponential survival approximation holds,
``` math
P_{\mathrm{exit}}(p,t) = 1-\exp\!\big(-\Gamma(p)\,t\big),
```
with an exit rate $`\Gamma(p)`$ exhibiting a finite-strength nonanalytic crossover at $`p=p_\ast`$. Moreover, $`\Gamma(p)`$ admits an interpolation of sigmoid form
``` math
\Gamma(p)\approx \Gamma_0\,
\frac{1}{1+\exp\!\left(\frac{p_\ast-p}{\delta p}\right)},
```
where $`\delta p`$ is controlled by $`D`$ and $`|\gamma'(p_\ast)|`$.*

</div>

<div class="proof">

*Proof.* For $`p<p_\ast`$, $`\gamma(p)>0`$ and the OU process is stable; first-passage across the boundary is noise-activated and exponentially suppressed (Kramers regime). For $`p>p_\ast`$, $`\gamma(p)<0`$ and drift expels trajectories, producing rapid exit on a timescale $`|\gamma(p)|^{-1}`$. Matching these regimes yields a sharp crossover of width set by diffusion scale $`D`$ and the slope at criticality. A detailed reduction is provided in Appendix <a href="#app:A" data-reference-type="ref" data-reference="app:A">10</a>. ◻

</div>

## No-go for linear measurement-only/decoherence-only models

<div id="prop:noknee" class="proposition">

**Proposition 16** (No knee without stabilization). *Consider any reduced dynamics generated by a linear time-homogeneous channel whose generator depends on $`p`$ only through a smooth rate prefactor and lacks state-dependent stabilization (i.e. does not admit basin boundaries characterized by loss of contractivity). Then $`P_{\mathrm{exit}}(p,t)`$ varies smoothly with $`p`$, and finite-strength knee behavior of the form in Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">15</a> cannot occur.*

</div>

<div class="proof">

*Proof.* A linear time-homogeneous generator with smooth dependence on $`p`$ produces a semigroup whose spectral decay rates vary smoothly with $`p`$. Knee behavior requires a sign change in an internal restoring rate and hence a qualitative change in local stability (Lemma <a href="#lem:critical" data-reference-type="ref" data-reference="lem:critical">14</a>), which is absent without basin stabilization. ◻

</div>

# Protocol Dependence and Zeno/Anti-Zeno Structure

## Protocol parameters and reduced evolution

We treat $`(p,\Delta t)`$ as independent protocol parameters. The reduced evolution is
``` math
\rho(t) = (\mathcal{M}_{p,\Delta t})^n(\rho_0),
\qquad t=n\Delta t.
```
Because $`P`$ is noninvertible, changes in $`(p,\Delta t)`$ generally alter which degrees of freedom are discarded and how stability margins renormalize; thus the effective generator is protocol-dependent.

## Effective generator dependence

<div id="ass:protocol-cont" class="assumption">

**Assumption 17** (Protocol continuity). The map $`(p,\Delta t)\mapsto \mathcal{M}_{p,\Delta t}`$ is continuous in operator topology on the slab, and admits a generator expansion
``` math
\mathcal{M}_{p,\Delta t} = \exp\!\big(\Delta t\,\mathcal{L}_{\mathrm{eff}}(p,\Delta t)\big) + \mathcal{O}(\Delta t^2)
```
on the controlled domain.

</div>

## Zeno/anti-Zeno theorem

<div id="thm:zeno" class="theorem">

**Theorem 18** (Zeno/anti-Zeno crossover). *Assume <a href="#ass:slab" data-reference-type="ref" data-reference="ass:slab">6</a>, <a href="#ass:protocol-cont" data-reference-type="ref" data-reference="ass:protocol-cont">17</a>, and the existence of a basin boundary with least-stable coordinate admitting the reduction in Assumption <a href="#ass:OU" data-reference-type="ref" data-reference="ass:OU">13</a>. Then there exist finite protocol scales $`p_Z`$ and $`\Delta t_Z`$ such that:*

1.  ***(Zeno regime)** For $`p\gg p_Z`$ and $`\Delta t\ll \Delta t_Z`$, basin exit is suppressed and $`\Gamma_{\mathrm{exit}}(p,\Delta t)\to 0`$.*

2.  ***(Anti-Zeno regime)** For intermediate $`(p,\Delta t)`$ near $`(p_Z,\Delta t_Z)`$, basin exit is enhanced: $`\Gamma_{\mathrm{exit}}(p,\Delta t)>\Gamma_{\mathrm{exit}}(0,\Delta t)`$.*

</div>

<div class="proof">

*Proof.* In the strong/frequent probing limit, repeated application of $`\mathcal{M}_{p,\Delta t}`$ confines trajectories to the most stable subspace within the basin, suppressing excursions along the least-stable direction (Zeno). At intermediate probing, the protocol injects fluctuations aligned with the least-stable coordinate and lowers the effective barrier governing exit (Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">15</a>), enhancing exit (anti-Zeno). Existence of finite crossover scales follows from continuity and the sign-change structure near the boundary (Lemma <a href="#lem:critical" data-reference-type="ref" data-reference="lem:critical">14</a>). ◻

</div>

## No-go for protocol dependence without stabilization

<div id="prop:noprotocol" class="proposition">

**Proposition 19** (Absence of protocol dependence without basin renormalization). *If the reduced dynamics is generated by a linear time-homogeneous channel whose generator depends only on $`p`$ through an overall smooth prefactor and does not depend on $`\Delta t`$ (beyond the trivial time-rescaling), then Zeno/anti-Zeno crossover behavior as in Theorem <a href="#thm:zeno" data-reference-type="ref" data-reference="thm:zeno">18</a> cannot occur. Any observed dependence on $`\Delta t`$ at fixed $`p`$ requires state-dependent stabilization or generator renormalization by the protocol.*

</div>

<div class="proof">

*Proof.* With a generator $`\mathcal{L}(p)=\alpha(p)\mathcal{L}_0`$, the evolution is $`e^{t\alpha(p)\mathcal{L}_0}`$, and protocol timing $`\Delta t`$ affects only the discretization of the same semigroup. There is no mechanism for intermediate enhancement relative to baseline beyond monotonic scaling in $`\alpha(p)`$. Zeno/anti-Zeno behavior requires protocol-dependent modification of stability margins and coupling to least-stable directions, which is absent without basin renormalization. ◻

</div>

# Relation to Ongoing Research and Validation Pathways

This section positions the derived structure relative to ongoing experimental and theoretical programs. The purpose is not to cite any one platform as definitive, but to show that multiple independent communities have identified facets of the same reduced-dynamical behavior.

## Monitored many-body systems and measurement-induced transitions

Hybrid unitary–measurement dynamics exhibits sharp changes in entanglement scaling as measurement rate varies. In the present framework these correspond to changes in admissible basin structure as $`p`$ crosses $`p_\ast`$ (Theorem <a href="#thm:bridge" data-reference-type="ref" data-reference="thm:bridge">11</a>). The knee theorem (Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">15</a>) explains why transitions can be sharp at finite measurement strength, rather than smooth decoherence crossovers.

## Continuous measurement and Zeno physics

Continuous measurement experiments display Zeno suppression at strong/frequent probing and anti-Zeno enhancement at intermediate probing. Theorem <a href="#thm:zeno" data-reference-type="ref" data-reference="thm:zeno">18</a> shows these are structural consequences of projection-induced basin dynamics, not artifacts of any particular measurement model.

## Weak measurement, reversibility, and echo protocols

Weak-measurement experiments combined with echo/reversal protocols observe a transition from reversible to irreversible behavior as measurement strength increases. In our framework this corresponds to confinement within a basin versus exit and capture across a basin boundary, with the finite-strength crossover quantified by Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">15</a>.

## Limitations of measurement-only and decoherence-only models

Propositions <a href="#prop:noknee" data-reference-type="ref" data-reference="prop:noknee">16</a> and <a href="#prop:noprotocol" data-reference-type="ref" data-reference="prop:noprotocol">19</a> formalize a common empirical challenge: linear time-homogeneous models reproduce smooth decay but do not generically yield finite-strength knees and full protocol dependence without introducing additional state-dependent stabilization. This clarifies why extensions with feedback, nonlinearities, or trajectory dependence are repeatedly required in practice.

## Unified predictions and validation channels

The framework yields validation channels that are largely platform-independent:

1.  **Universality of knees:** knee sharpness depends on stability margins and noise floors, not on microscopic circuit details.

2.  **Two-parameter protocol geometry:** behavior depends on both $`p`$ and $`\Delta t`$, not on a single effective rate.

3.  **Echo asymmetry near criticality:** forward/backward protocols exhibit asymmetry near basin boundaries due to capture dynamics.

These predictions are falsified if experiments show smooth, protocol-independent behavior across regimes where basin stability margins are demonstrably changing.

# Conclusions

We have constructed a reduced-dynamical bridge between measurement-induced phase transitions and collapse-like irreversibility by deriving both as shadows of projection-induced basin dynamics.

The principal results are:

1.  A unified reduced map $`\mathcal{M}_{p,\Delta t}`$ (Definition <a href="#def:M" data-reference-type="ref" data-reference="def:M">5</a>) encodes monitored dynamics and collapse contexts within a single projection framework.

2.  Measurement-induced phase transitions and collapse thresholds correspond to the same loss of contractivity at admissible basin boundaries (Theorem <a href="#thm:bridge" data-reference-type="ref" data-reference="thm:bridge">11</a>).

3.  Basin exit exhibits a finite-strength nonanalytic crossover (knee) at a critical monitoring strength (Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">15</a>), derived from a local OU/Kramers reduction.

4.  Protocol dependence and Zeno/anti-Zeno structure are unavoidable consequences of noninvertible projection with stabilization (Theorem <a href="#thm:zeno" data-reference-type="ref" data-reference="thm:zeno">18</a>).

5.  Linear time-homogeneous measurement-only or decoherence-only models cannot reproduce the combined set of features without introducing state-dependent stabilization equivalent to basin dynamics (Propositions <a href="#prop:noknee" data-reference-type="ref" data-reference="prop:noknee">16</a> and <a href="#prop:noprotocol" data-reference-type="ref" data-reference="prop:noprotocol">19</a>).

All statements are slab-local and admissibility-conditioned: the reduced map, contractivity margins, OU/Kramers reduction, and protocol-dependent generator structure are asserted only on bounded-geometry time slabs where the projection is bounded on the controlled domain and stability margins remain positive away from basin boundaries.

These results provide a unifying reduced-dynamical explanation for why finite-strength transitions, knees, and protocol dependence appear across diverse platforms and why additional state-dependent structure is repeatedly required beyond simple decoherence models. The bridge complements analogous shadow-bridge analyses linking collapse phenomena to other effective sectors; together, such bridges provide multiple independent validation channels for a common underlying projection-and-stabilization mechanism.

# OU/Kramers Reduction Near Basin Boundaries

This appendix provides the technical underpinning for Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">15</a>. Assume the OU reduction <a href="#eq:OU" data-reference-type="eqref" data-reference="eq:OU">[eq:OU]</a> holds on a slab time window.

## A.1 Stable regime $`p<p_\ast`$

If $`\gamma(p)>0`$, the OU process has stationary variance $`\mathbb{E}[u^2]=D/\gamma(p)`$. First-passage from $`u<0`$ to $`u\ge 0`$ is noise-activated; standard Kramers-type estimates imply an exponentially small exit rate in the small-noise or large-margin regime, with leading dependence controlled by $`\gamma(p)/D`$.

## A.2 Unstable regime $`p>p_\ast`$

If $`\gamma(p)<0`$, deterministic drift dominates and typical trajectories exit on a time scale $`\sim |\gamma(p)|^{-1}`$, yielding rapid basin exit.

## A.3 Crossover width

Near $`p_\ast`$, expand $`\gamma(p)\approx \gamma'(p_\ast)(p-p_\ast)`$. The crossover width in $`p`$ is controlled by the diffusion scale $`D`$ and $`|\gamma'(p_\ast)|`$, yielding the sigmoid interpolation stated in Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">15</a>.

# Generator Expansion and Protocol Dependence

This appendix records the minimal generator-level assumptions used in Section <a href="#sec:protocol" data-reference-type="ref" data-reference="sec:protocol">7</a>.

## B.1 Generator expansion

Assumption <a href="#ass:protocol-cont" data-reference-type="ref" data-reference="ass:protocol-cont">17</a> posits that, on the slab and on the controlled domain,
``` math
\mathcal{M}_{p,\Delta t} = \exp\!\big(\Delta t\,\mathcal{L}_{\mathrm{eff}}(p,\Delta t)\big)+\mathcal{O}(\Delta t^2).
```
Such expansions are standard when the microscopic dynamics is sufficiently regular and the reduced map is differentiable in $`\Delta t`$ at $`\Delta t=0`$.

## B.2 Noncommutativity of probing and projection

Protocol dependence arises because changing $`p`$ and $`\Delta t`$ changes the microscopic evolution $`\Phi^{(p)}_{\Delta t}`$ *before* projection. Since $`P`$ is noninvertible, the reduced generator cannot, in general, be written as a fixed generator multiplied by a scalar prefactor.

## B.3 Necessity for Zeno/anti-Zeno

Theorem <a href="#thm:zeno" data-reference-type="ref" data-reference="thm:zeno">18</a> requires that probing renormalizes stability margins near basin boundaries, which is exactly the content of the protocol dependence of $`\mathcal{L}_{\mathrm{eff}}(p,\Delta t)`$.

# Discrete-to-Continuous Limit in Monitored Dynamics

This appendix states a standard discrete-to-continuous connection used implicitly in Sections <a href="#sec:bridge" data-reference-type="ref" data-reference="sec:bridge">5</a>–<a href="#sec:protocol" data-reference-type="ref" data-reference="sec:protocol">7</a>.

Let $`\Delta t\to 0`$ with $`p=p(\Delta t)`$ chosen such that the combined effect of monitoring per unit time converges. Under regularity assumptions on $`\Phi^{(p)}_{\Delta t}`$, the reduced evolution converges to a continuous-time semigroup generated by $`\mathcal{L}_{\mathrm{eff}}`$. The present paper does not require a specific scaling law; it requires only that such a limit exists on the slab in the regimes where continuous-time language is used.

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
