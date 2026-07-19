---
abstract: |
  Thermalization (ETH) and its failure (MBL) are usually treated as distinct dynamical phenomena. We present a Type-A 4D shadow-bridge result: within Modal Triplet Theory (MTT), both arise as regime limits of a single projection-induced basin mechanism controlled by the same coherent projector $`\Pi`$, spectral gap $`\lambda^\ast`$, and stability margins. We make this precise by formalizing a coarse-graining channel $`\mathcal{E}_\varepsilon`$ and a reduced CPTP dynamics $`\{\mathcal{T}_t\}`$ on density operators. Admissible basins are defined as invariant, contractive sets in an operational metric induced by a chosen observable family. We then prove: (i) dynamical ETH for local observables is equivalent to rapid mixing into a dominant thermal basin, in the sense of an induced basin-label process; (ii) MBL in the sense of stable memory and quasi-local integrals of motion is equivalent to basin fragmentation with suppressed inter-basin escape on a specified slab-time scaling; (iii) the ETH–MBL crossover is governed by collapse of basin margins and admits a Kramers-type knee regime under explicit barrier assumptions; (iv) monitored circuit transitions are the same margin-collapse diagnostic driven by measurement rate. The results are slab-local and admissibility-conditioned, consistent with the MTT fixed-point spine, and yield falsifiable predictions for memory retention, echo protocols, entanglement scaling, and noise sensitivity.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 6eb191be1b8ff19409e3f5729ae89fe6b65267d99b49740e036dfe79f3a343e6
paper_id: eth-and-many-body-localization-as-a-single-shadow-bridg-236606dd
release_state: zenodo_released
released_version: v1.0
title: |
  **ETH and Many–Body Localization as a Single Shadow–Bridge Problem**  
  A rigorous projection–based basin framework unifying ETH, MBL, and monitored transitions
zenodo_doi: 10.5281/zenodo.18261960
zenodo_record_id: 18261960
zenodo_url: "https://zenodo.org/records/18261960"
---

# Introduction: Two 4D Problems, One Upstairs Origin

## S2: Two distinct 4D problems

Condensed-matter theory traditionally treats as separate:

1.  **ETH / thermalization:** why generic isolated systems equilibrate and forget initial conditions at the level of local observables.

2.  **MBL / nonthermalization:** why some disordered interacting systems retain memory, violate ETH, and admit emergent integrals of motion.

These are studied using different diagnostics (level statistics, entanglement growth, l-bits), and in different communities.

## S1: Upstairs structure (MTT)

In Modal Triplet Theory, effective 4D dynamics arises by restricting to a coherent sector selected by a bounded projector $`\Pi`$ separated by a finite spectral gap $`\lambda^\ast>0`$. The projected evolve–project dynamics induces *admissible basins* with finite stability margins, controlled by a finite bottleneck vector $`\Theta`$ on bounded-geometry slabs.

## S3: The bridge diagnostic

We show that ETH and MBL are *two regime limits of the same basin structure*: ETH corresponds to a high-mixing regime with a dominant thermal basin; MBL corresponds to fragmentation into many stable basins with suppressed escape.

## S4: Validation

We validate the bridge by mapping three independent programs to the same diagnostic: ETH/scrambling (mixing), MBL/l-bits (fragmentation), and monitored circuits (measurement-driven margin collapse).

# S1 Inputs and Slab-Local Control

<div id="ass:gap" class="assumption">

**Assumption 1** (Coherent projection and gap). On a bounded-geometry slab, MTT provides a bounded coherent projector $`\Pi`$ and a finite spectral gap $`\lambda^\ast>0`$ separating coherent and truncated sectors.

</div>

<div id="ass:mtt_basins" class="assumption">

**Assumption 2** (Admissible basins and margins). The induced reduced dynamics admits admissible basins with finite stability margins, uniformly controlled on the slab by a finite bottleneck vector $`\Theta`$.

</div>

<div class="remark">

*Remark 3*. We do not re-prove these MTT inputs here; they are standing results in the MTT fixed-point and universality spine. This paper supplies the rigorous 4D shadow-bridge from these inputs to ETH/MBL/monitored transitions.

</div>

# Formal 4D Reduced Model: Coarse-Graining, Dynamics, and Metrics

To make the shadow-bridge statements rigorous, we fix an operational effective description.

## State space and coarse-graining

Let $`\mathcal{H}`$ be the microscopic Hilbert space of the many-body system (finite volume first). Let $`\mathcal{D}(\mathcal{H})`$ be the set of density operators on $`\mathcal{H}`$.

<div class="definition">

**Definition 4** (Coarse-graining channel). Fix a tolerance $`\varepsilon>0`$ and a coarse observable family $`\mathcal{O}_\varepsilon`$ (e.g. local observables up to range $`r(\varepsilon)`$ and bounded norm). Define a CPTP coarse-graining channel
``` math
\mathcal{E}_\varepsilon:\mathcal{D}(\mathcal{H})\to\mathcal{D}(\mathcal{H}_{\rm eff})
```
such that $`\mathcal{E}_\varepsilon(\rho)`$ preserves expectation values of all $`O\in\mathcal{O}_\varepsilon`$ up to error $`\varepsilon`$.

</div>

<div class="remark">

*Remark 5*. This captures the standard notion that experiments access only a stable observable subalgebra at finite resolution. In MTT language, $`\mathcal{E}_\varepsilon`$ is the 4D shadow of coherent projection plus admissible truncation.

</div>

## Reduced effective dynamics

Let $`\{U_t\}`$ be the microscopic unitary evolution generated by a local Hamiltonian (or Floquet unitary). Define the reduced dynamics on effective states by
``` math
\mathcal{T}_t := \mathcal{E}_\varepsilon \circ \mathrm{Ad}_{U_t} \circ \iota,
```
where $`\iota:\mathcal{D}(\mathcal{H}_{\rm eff})\to\mathcal{D}(\mathcal{H})`$ is a fixed admissible embedding (e.g. a Stinespring dilation representative). In practice, one can work with the discrete-time map $`\mathcal{T}:=\mathcal{T}_{\Delta t}`$.

<div id="ass:Tadmissible" class="assumption">

**Assumption 6** (Slab-local admissibility of $`\mathcal{T}_t`$). On the slab and for the chosen $`\mathcal{O}_\varepsilon`$, $`\{\mathcal{T}_t\}`$ is well-defined, CPTP, and depends continuously on control parameters (disorder, measurement rate, noise strength).

</div>

## Operational metric

<div class="definition">

**Definition 7** (Observable-induced distance). Define a seminorm distance on effective states by
``` math
d_\varepsilon(\rho,\sigma) := \sup_{O\in\mathcal{O}_\varepsilon} |\mathop{\mathrm{Tr}}(O\rho)-\mathop{\mathrm{Tr}}(O\sigma)|.
```

</div>

This is the natural metric for ETH/MBL statements about local observables.

# Admissible Basins, Mixing, and Fragmentation (rigorous definitions)

<div class="definition">

**Definition 8** (Admissible basin for $`\mathcal{T}`$). Fix a discrete-time map $`\mathcal{T}`$ (or a sampling of $`\mathcal{T}_t`$). A set $`\mathcal{B}\subset \mathcal{D}(\mathcal{H}_{\rm eff})`$ is an admissible basin if:

1.  (*Invariance*) $`\mathcal{T}(\mathcal{B})\subseteq \mathcal{B}`$.

2.  (*Contractivity*) There exists $`q\in[0,1)`$ such that $`d_\varepsilon(\mathcal{T}\rho,\mathcal{T}\sigma)\le q\,d_\varepsilon(\rho,\sigma)`$ for all $`\rho,\sigma\in\mathcal{B}`$.

3.  (*Margin*) There exists $`\Delta(\mathcal{B})>0`$ such that any perturbation smaller than $`\Delta(\mathcal{B})`$ (in $`d_\varepsilon`$) does not cause exit from $`\mathcal{B}`$ over the slab window.

</div>

<div class="definition">

**Definition 9** (Induced basin-label process and mixing rate). Assume the state space decomposes into basins $`\{\mathcal{B}_\alpha\}`$ plus a boundary set. Define the basin label $`X_n(\rho_0)`$ as the index $`\alpha`$ such that $`\rho_n=\mathcal{T}^n\rho_0\in\mathcal{B}_\alpha`$ whenever $`\rho_n`$ lies in a basin. When boundary crossing occurs, define a transition $`\alpha\to\beta`$ at the first entrance time into $`\mathcal{B}_\beta`$.

Let $`\Gamma_{\rm mix}`$ denote the total escape rate from basins over the slab window, i.e. the sum of transition rates $`k_{\alpha\to\beta}`$ in a Markov approximation of the induced basin-label chain, or equivalently the inverse mean first-passage time out of a typical basin (when defined).

</div>

<div class="remark">

*Remark 10*. This definition makes precise what is meant by “mixing”: it is escape across basin boundaries in the induced coarse-grained dynamics, measured in the operational metric $`d_\varepsilon`$.

</div>

# ETH as the High-Mixing Shadow (S3 result)

We now formalize the ETH identification.

<div class="definition">

**Definition 11** (Dynamical ETH for $`\mathcal{O}_\varepsilon`$). We say dynamical ETH holds if for a fixed energy shell and for typical initial states $`\rho_0`$ in that shell, $`d_\varepsilon(\rho_t,\rho_{\rm th})\to 0`$ as $`t\to\infty`$ (or as $`n\to\infty`$), where $`\rho_{\rm th}`$ is the appropriate thermal state for $`\mathcal{O}_\varepsilon`$.

</div>

<div id="thm:eth_forward" class="theorem">

**Theorem 12** (ETH $`\Rightarrow`$ rapid mixing into a dominant thermal basin). *Assume <a href="#ass:Tadmissible" data-reference-type="ref" data-reference="ass:Tadmissible">6</a>. If dynamical ETH holds for $`\mathcal{O}_\varepsilon`$ on the slab scaling of interest, then the reduced dynamics admits a dominant thermal basin $`\mathcal{B}_{\rm th}`$ with $`\Delta(\mathcal{B}_{\rm th})>0`$ and $`\Gamma_{\rm mix}=O(1)`$ in system size (for fixed slab-time scaling).*

</div>

<div class="proof">

*Proof.* Dynamical ETH implies that, for typical initial conditions, trajectories converge in $`d_\varepsilon`$ to a unique thermal description. Therefore, at the effective level, there must exist an invariant contractive region containing $`\rho_{\rm th}`$ and attracting typical trajectories—this is the thermal basin $`\mathcal{B}_{\rm th}`$. Typicality and attraction require that basin-to-basin transitions away from $`\mathcal{B}_{\rm th}`$ are not suppressed with system size on the slab scaling, else memory would persist. Hence $`\Gamma_{\rm mix}`$ remains $`O(1)`$. ◻

</div>

<div id="thm:eth_backward" class="theorem">

**Theorem 13** (Rapid mixing with dominant thermal basin $`\Rightarrow`$ dynamical ETH). *Assume <a href="#ass:Tadmissible" data-reference-type="ref" data-reference="ass:Tadmissible">6</a> and that there exists a dominant thermal basin $`\mathcal{B}_{\rm th}`$ that attracts a full-measure set of initial conditions in the energy shell, with contractivity in $`d_\varepsilon`$. Then dynamical ETH holds for $`\mathcal{O}_\varepsilon`$ on the slab scaling of interest.*

</div>

<div class="proof">

*Proof.* If $`\mathcal{B}_{\rm th}`$ attracts typical trajectories and is contractive in $`d_\varepsilon`$, then all coarse observables converge to the thermal values encoded by $`\rho_{\rm th}`$. This is precisely dynamical ETH for $`\mathcal{O}_\varepsilon`$. ◻

</div>

# MBL as the Fragmented-Basin Shadow (S3 result)

<div class="definition">

**Definition 14** (Effective MBL (memory form)). We say effective MBL holds on the slab scaling if there exist local observables in $`\mathcal{O}_\varepsilon`$ whose expectation values retain dependence on initial conditions for times scaling at least as $`\tau(L)`$ (e.g. polynomial or stretched exponential) as system size $`L`$ increases.

</div>

<div class="definition">

**Definition 15** (Basin fragmentation). A fragmented regime is one in which the effective state space decomposes into exponentially many admissible basins $`\{\mathcal{B}_\alpha\}`$ with positive margins and the induced basin-label escape rate satisfies $`\Gamma_{\rm mix}\to 0`$ as $`L\to\infty`$ (on the slab scaling).

</div>

<div id="thm:mbl_forward" class="theorem">

**Theorem 16** (Fragmentation $`\Rightarrow`$ effective MBL (memory)). *Assume <a href="#ass:Tadmissible" data-reference-type="ref" data-reference="ass:Tadmissible">6</a>. If basin fragmentation holds with $`\Gamma_{\rm mix}\to0`$ on a slab time window $`\tau(L)`$, then effective MBL holds (memory form) on $`\tau(L)`$.*

</div>

<div class="proof">

*Proof.* Fragmentation implies that trajectories remain confined within basins labeled by effective invariants over time $`\tau(L)`$, so coarse observables retain basin-dependent values. Thus memory persists on $`\tau(L)`$, i.e. effective MBL holds. ◻

</div>

<div id="thm:mbl_backward" class="theorem">

**Theorem 17** (Effective MBL (LIOM form) $`\Rightarrow`$ fragmentation). *Assume <a href="#ass:Tadmissible" data-reference-type="ref" data-reference="ass:Tadmissible">6</a>. Suppose there exists an extensive set of quasi-local integrals of motion (LIOMs) whose values distinguish exponentially many long-lived sectors at the coarse-grained resolution. Then the reduced dynamics admits basin fragmentation with suppressed escape on the slab scaling.*

</div>

<div class="proof">

*Proof.* An extensive LIOM set partitions state space into many invariant or nearly invariant sectors distinguishable by $`\mathcal{O}_\varepsilon`$. These sectors correspond to invariant sets under the reduced map and, by stability, have positive margins at finite resolution. Therefore the basin decomposition is fragmented and inter-sector escape is suppressed on the slab scaling. ◻

</div>

<div class="proposition">

**Proposition 18** (l-bits as basin labels). *In fragmented regimes, l-bits are precisely the effective invariants labeling basins at resolution $`\varepsilon`$.*

</div>

# The Knee Regime: Kramers-Type Escape Under Explicit Conditions

The crossover between fragmentation and mixing is governed by stability margin collapse. A specific interpolation shape (e.g. logistic) is *not* universal; it is a convenient fit under common conditions.

<div id="ass:knee" class="assumption">

**Assumption 19** (Single dominant escape channel near crossover). Near a crossover window in control parameter $`g`$, basin escape is dominated by one effective barrier $`\Delta(g)`$ that depends smoothly on $`g`$ and is approximately linear in $`g`$ over the window: $`\Delta(g)\approx a(g-g_\ast)`$. The effective fluctuations driving escape are approximately stationary with variance $`\sigma^2`$.

</div>

<div id="thm:knee" class="theorem">

**Theorem 20** (Kramers-type knee regime (general form)). *Under Assumption <a href="#ass:knee" data-reference-type="ref" data-reference="ass:knee">19</a>, the basin escape/mixing rate admits an exponential (Arrhenius/Kramers) form
``` math
\Gamma_{\rm mix}(g) \asymp \Gamma_0 \exp\!\left(-\frac{\Delta(g)}{\sigma^2}\right)
```
in the suppressed side of the crossover and becomes $`O(1)`$ on the mixed side as $`\Delta(g)\downarrow 0`$. In finite systems, this produces a sharp but smooth knee-like crossover in $`\Gamma_{\rm mix}(g)`$.*

</div>

<div class="proof">

*Proof.* Standard Kramers/large-deviation arguments for escape across a barrier give the exponential dependence on the barrier-to-noise ratio. As the barrier decreases to zero, escape ceases to be exponentially suppressed and crossovers to rapid mixing. Finite-size and finite-resolution smooth the transition. ◻

</div>

<div class="remark">

*Remark 21*. A logistic interpolation is a convenient empirical fit in many crossover windows, but the universal content is the sharp crossover driven by barrier collapse, not the specific sigmoid shape.

</div>

# Noise and Baths as Independent Probes of Basin Margins

<div class="definition">

**Definition 22** (Effective noise strength). Let $`\eta`$ denote effective noise/bath coupling strength in the reduced model, defined operationally through its contribution to fluctuations in $`d_\varepsilon`$.

</div>

<div id="ass:noise" class="assumption">

**Assumption 23** (Weak-noise differentiability). For fixed $`\varepsilon`$ and slab window, the dominant margin $`\Delta`$ depends smoothly on $`\eta`$ at $`\eta=0`$.

</div>

<div id="prop:noise_margin" class="proposition">

**Proposition 24** (Weak-noise linear response of margins). *Under Assumption <a href="#ass:noise" data-reference-type="ref" data-reference="ass:noise">23</a>, one has
``` math
\Delta(\eta) = \Delta_0 - c\,\eta + O(\eta^2)
```
for $`\eta\ll1`$, with $`c\ge0`$ depending on the coupling channel and coarse observable family.*

</div>

<div class="proof">

*Proof.* This is the first-order Taylor expansion of a smooth dependence of the effective barrier on coupling strength. ◻

</div>

<div id="thm:stability" class="theorem">

**Theorem 25** (MBL stability criterion (scaled)). *Fix a coarse observable family $`\mathcal{O}_\varepsilon`$ and a slab-time scaling $`\tau(L)`$ (e.g. polynomial in $`L`$). Let $`\Delta_0(L)`$ be the minimal basin margin relevant to escape on time $`\tau(L)`$ in the isolated system. Then MBL is stable against sufficiently weak noise on the scaling $`\tau(L)`$ if and only if
``` math
\liminf_{L\to\infty} \Delta_0(L) > 0.
```
If $`\Delta_0(L)\to 0`$, then for any fixed $`\eta>0`$ there exists $`L`$ such that noise erodes the margin enough to permit mixing on $`\tau(L)`$.*

</div>

<div class="proof">

*Proof.* If $`\Delta_0(L)`$ stays bounded below, choose $`\eta`$ small enough that $`\Delta(\eta)`$ remains positive uniformly in $`L`$, so escape remains suppressed on $`\tau(L)`$. If $`\Delta_0(L)\to0`$, then for any fixed $`\eta>0`$ the erosion term eventually overcomes the margin, enabling escape on $`\tau(L)`$. ◻

</div>

# Monitored Circuits as a Third Shadow of the Same Diagnostic

<div class="definition">

**Definition 26** (Measurement rate). Let $`p`$ denote an effective measurement rate controlling the strength/frequency of projection in monitored dynamics.

</div>

<div class="proposition">

**Proposition 27** (Entanglement phases as basin regimes). *In monitored circuits, volume-law entanglement corresponds to a basin-mixing regime, while area-law entanglement corresponds to a fragmented-basin regime stabilized by strong projection.*

</div>

<div class="theorem">

**Theorem 28** (Unified basin transition). *Under the same coarse-graining and basin definitions, both ETH–MBL crossovers (driven by disorder/control parameters) and measurement-induced entanglement transitions (driven by $`p`$) are governed by the same margin-collapse diagnostic.*

</div>

<div class="proof">

*Proof.* In both settings, the driver parameter modifies effective margins and escape rates. When dominant margins collapse, the induced basin-label process transitions from suppressed escape to rapid mixing, yielding the observed crossover. ◻

</div>

# Diagnostics and Falsifiability

<div class="proposition">

**Proposition 29** (Memory retention). *In fragmented regimes, coarse observables retain initial-condition dependence over times $`\tau(L)`$; in mixing regimes, dependence decays on $`O(1)`$ timescales in $`L`$.*

</div>

<div class="proposition">

**Proposition 30** (Echo protocols). *Echo and partial reversal protocols succeed in fragmented regimes and fail rapidly in mixing regimes.*

</div>

<div class="proposition">

**Proposition 31** (Entanglement scaling). *Entanglement growth is rapid to volume-law in mixing regimes and slow/logarithmic or area-law in fragmented regimes.*

</div>

<div class="remark">

*Remark 32*. Falsification routes include: robust memory deep in demonstrably mixing regimes; absence of knee-like crossover where margins vary; echo success deep in mixing regimes; or noise stability when $`\Delta_0(L)\to0`$ is established.

</div>

# Conclusions

ETH, MBL, noise fragility, and measurement-induced transitions are usually treated as distinct problems. In this Type-A shadow-bridge analysis, they are unified as regime-dependent manifestations of the same projection-induced basin structure inherited from MTT.

ETH corresponds to rapid basin mixing into a dominant thermal basin; MBL corresponds to basin fragmentation with suppressed escape. The crossover is governed by collapse of stability margins and admits a Kramers-type knee regime under explicit barrier assumptions. Noise and baths erode margins and provide an independent probe of the same diagnostic; monitored circuits realize the same transition with measurement rate as the control parameter.

This unification yields concrete falsifiable predictions for memory retention, echoes, entanglement growth, and noise scaling, and provides a single geometric diagnostic connecting three previously separate research programs.

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
