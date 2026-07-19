---
abstract: |
  We derive pilot–wave (de Broglie–Bohm) dynamics as an effective, intra–basin description of Modal Triplet Theory (MTT). Starting from the deterministic modal flow on the full configuration space $`X = Y^4 \times B_1 \times B_2 \times B_3`$, we show that the coherent projection and observable pushforward induce (i) a Schrödinger evolution on the reduced observable Hilbert space, (ii) a conserved probability current on configuration space, and (iii) a canonical characteristic flow whose integral curves coincide with Bohmian guidance equations. No additional hidden variables, stochastic postulates, or ontological assumptions are introduced.

  We further prove that pilot–wave dynamics are valid only within admissible coherence basins where the coherent projection is stable. At admissibility boundaries—including measurement, horizon formation, and cosmological selection events—the pilot–wave description necessarily breaks down, while the underlying MTT dynamics remain deterministic and well-defined. Pilot–wave theory is therefore shown to be a regime–limited shadow of MTT rather than a fundamental theory.

  This establishes Bohmian mechanics as a semiclassical gauge of MTT, clarifies its domain of validity, and resolves its foundational tensions with probability, measurement, and relativistic causality.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: caf50c330af256c69d1dae3fba2aa66565f635c9d804efdf4666f17ad13bdf7d
paper_id: modal-triplet-theory-from-mtt-to-pilot-wave-dynamics
release_state: zenodo_released
released_version: v1.0
title: "Modal Triplet Theory: From MTT to Pilot–Wave Dynamics"
zenodo_doi: 10.5281/zenodo.18262378
zenodo_record_id: 18262378
zenodo_url: "https://zenodo.org/records/18262378"
---

# Introduction and Scope

Pilot–wave theory (also known as de Broglie–Bohm theory) provides a deterministic reformulation of nonrelativistic quantum mechanics by supplementing the Schrödinger wavefunction with configuration–space trajectories guided by the wave phase. While mathematically consistent, pilot–wave theory is widely regarded as ontologically ad hoc, probabilistically incomplete, and difficult to extend beyond nonrelativistic quantum mechanics.

Modal Triplet Theory (MTT), by contrast, derives quantum mechanics as an effective four–dimensional shadow of deterministic dynamics on a higher–dimensional modal configuration space. In MTT, quantum states, probabilities, and measurement outcomes arise from coherent projection and admissibility constraints rather than from fundamental indeterminism or added hidden variables.

The purpose of this paper is to show that pilot–wave dynamics are not an independent alternative to standard quantum mechanics, but rather an *effective characteristic description* of MTT in regimes where:

- the coherent projector is stable,

- the effective Schrödinger evolution is valid,

- and no admissibility barrier is crossed.

Within this regime, Bohmian guidance equations arise canonically from the conserved probability current associated with the MTT–derived Schrödinger evolution. Outside this regime, pilot–wave theory necessarily fails, while MTT remains consistent and deterministic.

## Claim Discipline

We distinguish three layers of statements:

1.  **Proved (MTT-native):** deterministic modal flow, coherent projection, existence of Schrödinger evolution, Born measure, and admissibility constraints.

2.  **Derived (this paper):** emergence of pilot–wave guidance equations as characteristic flows of the MTT Schrödinger layer.

3.  **Excluded claims:** pilot–wave ontology as fundamental, global validity across selection events, or replacement of MTT by Bohmian mechanics.

All derivations are valid *only within admissible coherence basins*, as emphasized throughout the MTT corpus.

# MTT Framework and Notation

## Modal Configuration Space

Modal Triplet Theory posits a configuration space
``` math
X \;=\; Y^4 \times B_1 \times B_2 \times B_3,
```
where:

- $`Y^4`$ is the emergent spacetime manifold,

- each $`B_i`$ is a compact modal fiber equipped with a Laplace–type operator.

Let $`\Phi_\tau : X \to X`$ denote the deterministic modal evolution, assumed invertible and well-posed on admissible domains.

## Coherent Projection and Observable Pushforward

Define the joint harmonic projector
``` math
\Pi := \Pi_{B_1} \Pi_{B_2} \Pi_{B_3},
```
where $`\Pi_{B_i}`$ projects onto $`\ker \Delta_{B_i}`$. The coherent sector is
``` math
\mathcal{H}_{\mathrm{coh}} := \mathrm{Ran}(\Pi).
```

Observable states are obtained via the pushforward
``` math
P := I \circ \Pi,
```
where $`I`$ integrates over the internal modal fibers.

The effective (shadow) evolution is
``` math
T_\tau := P \circ \Phi_\tau.
```

## Admissibility

An admissible domain $`\mathcal{A} \subset X`$ is one on which:

1.  the spectral gaps defining $`\Pi`$ remain open,

2.  $`\Pi`$ is bounded and regular,

3.  truncation errors remain controlled under iteration of $`T_\tau`$.

Admissibility is *not global*. Crossing its boundary produces selection events and effective irreversibility.

## Reduced Hilbert Space and Schrödinger Layer

On each admissible basin, the observable sector admits:

- a Hilbert space $`\mathcal{H}_{\mathrm{obs}}`$,

- a self-adjoint Hamiltonian $`H_{\mathrm{obs}}`$,

- unitary evolution $`U(t)=e^{-iH_{\mathrm{obs}}t/\hbar}`$.

This construction is reviewed in detail in the MTT$`\to`$QM derivation and will be taken as established here.

**In the next section**, we derive the configuration–space probability current and show how Bohmian guidance equations arise as characteristic flows.

# Configuration–Space Schrödinger Dynamics

We now specialize to the standard nonrelativistic regime of the MTT–derived observable theory. All statements in this section are valid *within a fixed admissible coherence basin*.

## Configuration Observables

Let $`q \in \mathbb{R}^{3N}`$ denote a configuration observable (e.g. particle positions in the nonrelativistic limit). The observable Hilbert space takes the form
``` math
\mathcal{H}_{\mathrm{obs}} \;\simeq\; L^2(\mathbb{R}^{3N}, dq).
```

The MTT–derived Hamiltonian has the standard Schrödinger form
``` math
\begin{equation}
H_{\mathrm{obs}}
\;=\;
\sum_{k=1}^N
\left(
-\frac{\hbar^2}{2m_k}\nabla_k^2
\right)
\;+\;
V(q,t),
\label{eq:Hobs}
\end{equation}
```
where $`V`$ may include external, interaction, and effective potentials arising from modal truncation.

## Unitary Evolution

The observable state $`\psi(q,t)`$ evolves according to
``` math
\begin{equation}
i\hbar\,\partial_t \psi(q,t)
\;=\;
H_{\mathrm{obs}}\,\psi(q,t),
\label{eq:Schrodinger}
\end{equation}
```
with $`\|\psi(t)\|_{L^2}`$ conserved for all $`t`$ such that the trajectory remains in the admissible basin.

<div class="remark">

*Remark 1*. This evolution is exact only *between* selection events. MTT makes no claim that a single global Schrödinger equation governs all times.

</div>

# Probability Density and Continuity

## Born Density

Define the configuration–space density
``` math
\begin{equation}
\rho(q,t) := |\psi(q,t)|^2.
\end{equation}
```

In MTT, $`\rho`$ is not postulated but arises as the unique noncontextual measure compatible with modal re–coherence and projection. Within an admissible basin, $`\rho`$ is conserved by unitary evolution.

## Probability Current

For each configuration component $`x_k \in \mathbb{R}^3`$, define the probability current
``` math
\begin{equation}
j_k(q,t)
:=
\frac{\hbar}{m_k}
\operatorname{Im}\!\left(
\psi^*(q,t)\,\nabla_k \psi(q,t)
\right).
\label{eq:current}
\end{equation}
```

## Continuity Equation

<div class="theorem">

**Theorem 2** (Continuity Equation). *Within an admissible coherence basin, the density $`\rho`$ and currents $`\{j_k\}`$ satisfy
``` math
\begin{equation}
\partial_t \rho(q,t)
+
\sum_{k=1}^N \nabla_k \cdot j_k(q,t)
\;=\;
0.
\label{eq:continuity}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Equation <a href="#eq:continuity" data-reference-type="eqref" data-reference="eq:continuity">[eq:continuity]</a> follows from the self–adjointness of $`H_{\mathrm{obs}}`$ and the unitarity of the evolution <a href="#eq:Schrodinger" data-reference-type="eqref" data-reference="eq:Schrodinger">[eq:Schrodinger]</a>. The proof is standard and relies only on integration by parts. ◻

</div>

<div class="remark">

*Remark 3*. Global probability conservation across all times is *not* asserted. At admissibility boundaries, the effective description changes and <a href="#eq:continuity" data-reference-type="eqref" data-reference="eq:continuity">[eq:continuity]</a> need not hold.

</div>

# Polar Decomposition and Hamilton–Jacobi Form

## Polar Representation

Write the wavefunction in polar form
``` math
\begin{equation}
\psi(q,t) = R(q,t)\,e^{iS(q,t)/\hbar},
\qquad
R \ge 0.
\label{eq:polar}
\end{equation}
```

Then $`\rho = R^2`$ and the current becomes
``` math
\begin{equation}
j_k(q,t)
=
\rho(q,t)\,
\frac{\nabla_k S(q,t)}{m_k}.
\label{eq:currentS}
\end{equation}
```

## Quantum Hamilton–Jacobi Equation

Substituting <a href="#eq:polar" data-reference-type="eqref" data-reference="eq:polar">[eq:polar]</a> into the Schrödinger equation and separating real and imaginary parts yields:
``` math
\begin{align}
\partial_t \rho
+
\sum_{k=1}^N \nabla_k \cdot
\left(
\rho\,\frac{\nabla_k S}{m_k}
\right)
&= 0,
\\[0.5em]
\partial_t S
+
\sum_{k=1}^N
\frac{(\nabla_k S)^2}{2m_k}
+
V(q,t)
+
Q(q,t)
&= 0,
\label{eq:HJ}
\end{align}
```
where the quantum potential is
``` math
\begin{equation}
Q(q,t)
:=
-
\sum_{k=1}^N
\frac{\hbar^2}{2m_k}
\frac{\nabla_k^2 R}{R}.
\label{eq:Q}
\end{equation}
```

<div class="remark">

*Remark 4*. In MTT, $`Q`$ is not interpreted as a new fundamental force. It encodes projection–induced curvature of the effective description.

</div>

# Pilot–Wave Guidance as Characteristic Flow

We now arrive at the central result.

## Velocity Field on Configuration Space

Define the configuration–space velocity field
``` math
\begin{equation}
v_k(q,t)
:=
\frac{j_k(q,t)}{\rho(q,t)}
=
\frac{\nabla_k S(q,t)}{m_k}.
\label{eq:velocity}
\end{equation}
```

This object is well-defined wherever $`\rho>0`$.

## Characteristic Curves

Let $`q(t) = (x_1(t),\dots,x_N(t))`$ be an integral curve of $`v`$:
``` math
\begin{equation}
\dot x_k(t) = v_k(q(t),t).
\label{eq:guidance}
\end{equation}
```

## Main Theorem

<div class="theorem">

**Theorem 5** (Emergent Pilot–Wave Dynamics). *Within an admissible coherence basin of Modal Triplet Theory, the integral curves of the configuration–space velocity field <a href="#eq:velocity" data-reference-type="eqref" data-reference="eq:velocity">[eq:velocity]</a> satisfy the de Broglie–Bohm guidance equations <a href="#eq:guidance" data-reference-type="eqref" data-reference="eq:guidance">[eq:guidance]</a>.*

*These curves provide a deterministic characteristic description of the MTT–derived Schrödinger evolution.*

</div>

<div class="proof">

*Proof.* Equation <a href="#eq:guidance" data-reference-type="eqref" data-reference="eq:guidance">[eq:guidance]</a> follows identically from definitions <a href="#eq:current" data-reference-type="eqref" data-reference="eq:current">[eq:current]</a> and <a href="#eq:velocity" data-reference-type="eqref" data-reference="eq:velocity">[eq:velocity]</a>. No additional assumptions are introduced. ◻

</div>

<div class="remark">

*Remark 6* (Interpretive Status). MTT does *not* postulate particles or trajectories as fundamental. The guidance equations arise as a *derived kinematic structure* once a configuration observable is chosen.

</div>

<div class="remark">

*Remark 7* (Domain of Validity). The guidance law is valid only while the effective Schrödinger description holds. At admissibility boundaries, the characteristic flow need not extend smoothly and pilot–wave dynamics may fail.

</div>

# Equivariance and Born Measure

## Equivariance

<div class="theorem">

**Theorem 8** (Equivariance). *If initial configurations are distributed according to $`\rho(q,t_0)=|\psi(q,t_0)|^2`$, then under the guidance flow <a href="#eq:guidance" data-reference-type="eqref" data-reference="eq:guidance">[eq:guidance]</a>,
``` math
\rho(q,t)=|\psi(q,t)|^2
```
for all $`t`$ within the admissible basin.*

</div>

<div class="proof">

*Proof.* Equivariance follows directly from the continuity equation <a href="#eq:continuity" data-reference-type="eqref" data-reference="eq:continuity">[eq:continuity]</a> and the definition of the velocity field <a href="#eq:velocity" data-reference-type="eqref" data-reference="eq:velocity">[eq:velocity]</a>. ◻

</div>

<div class="remark">

*Remark 9*. In pilot–wave theory, equivariance is often invoked to justify the Born rule. In MTT, the Born measure is derived independently; equivariance appears as a consistency check rather than a postulate.

</div>

**In Part III**, we will:

- extend the derivation to entangled and nonlocal systems,

- analyze measurement and admissibility breakdown,

- and relate pilot–wave trajectories to MTT’s indivisible stochastic processes.

# Entanglement and Configuration–Space Nonlocality

## Entangled States

Let $`\psi(q,t)`$ be an $`N`$–particle wavefunction on $`\mathbb{R}^{3N}`$ that does not factorize:
``` math
\psi(q,t) \neq \prod_{k=1}^N \psi_k(x_k,t).
```

In such cases, the configuration–space current <a href="#eq:current" data-reference-type="eqref" data-reference="eq:current">[eq:current]</a> and velocity field <a href="#eq:velocity" data-reference-type="eqref" data-reference="eq:velocity">[eq:velocity]</a> are intrinsically nonlocal in physical space.

## Nonlocal Guidance

For entangled $`\psi`$, the velocity of particle $`k`$ is
``` math
\begin{equation}
\dot x_k(t)
=
\frac{1}{m_k}
\nabla_k S(x_1,\dots,x_N,t),
\end{equation}
```
which depends instantaneously on the full configuration $`q=(x_1,\dots,x_N)`$.

This is the familiar nonlocality of pilot–wave theory.

## MTT Interpretation

In MTT, this nonlocality is not attributed to superluminal forces or signals. Instead, it reflects the fact that the coherent projector $`\Pi`$ acts globally on the modal configuration space.

Observable locality is preserved at the level of operator algebras on $`Y^4`$; nonlocal correlations arise from projection constraints rather than from causal influence.

<div class="remark">

*Remark 10*. MTT therefore accommodates Bell–inequality violations without violating microcausality or relativistic consistency.

</div>

# Measurement as Admissibility Breakdown

## Limits of the Schrödinger Layer

The Schrödinger evolution <a href="#eq:Schrodinger" data-reference-type="eqref" data-reference="eq:Schrodinger">[eq:Schrodinger]</a> and its associated guidance equations are valid only within a fixed admissible coherence basin.

When the system–apparatus interaction drives the modal configuration toward the boundary of admissibility, the coherent projector ceases to be stably invertible.

## Admissibility Barriers

<div class="definition">

**Definition 11** (Admissibility Barrier). A subset $`\mathcal{B}\subset X`$ is an admissibility barrier if:

1.  the spectral gap defining $`\Pi`$ closes or becomes unstable,

2.  $`\Pi`$ ceases to admit a measurable right inverse,

3.  multiple modal states project to the same observable state.

</div>

Crossing $`\mathcal{B}`$ induces effective irreversibility in the projected dynamics.

## Measurement Event

A measurement corresponds to a trajectory $`\Phi_\tau(x)`$ crossing an admissibility barrier. After this crossing:

- the prior Schrödinger evolution no longer applies globally,

- the guidance field $`v(q,t)`$ may cease to exist,

- the observable state must be reinitialized in a new basin.

<div class="remark">

*Remark 12*. This replaces the notion of “collapse” with a precise structural mechanism: loss of admissibility.

</div>

# Failure of Global Pilot–Wave Dynamics

## Why Bohmian Mechanics Cannot Be Global

Pilot–wave theory assumes:

- a single global wavefunction $`\psi(q,t)`$,

- continuous guidance trajectories for all times.

MTT shows that these assumptions fail generically:

- Schrödinger evolution is basin–scoped,

- admissibility breakdown forces re–projection,

- no global measurable inverse of $`P`$ exists.

<div class="theorem">

**Theorem 13** (No Global Guidance Law). *There exists no globally defined guidance field $`v(q,t)`$ whose integral curves describe all observable dynamics across admissibility barriers.*

</div>

<div class="proof">

*Proof.* At admissibility barriers, multiple modal states map to the same observable state under $`P`$. A globally defined $`v(q,t)`$ would require a measurable right inverse of $`P`$, which does not exist. ◻

</div>

<div class="remark">

*Remark 14*. This is not a deficiency of MTT but a theorem. It explains why pilot–wave theory must be regime–limited.

</div>

# Relation to Indivisible Stochastic Processes

## History–Dependent Kernels

MTT induces a probability measure on histories
``` math
(q_0,q_1,\dots)\in (\mathbb{R}^{3N})^{\mathbb{N}}
```
with conditional kernels
``` math
K_{\Delta\tau}(q_{k+1}\mid q_0,\dots,q_k)
\propto
\exp\!\left(
-\frac{\Delta A(q_{k+1}\mid q_0,\dots,q_k)}{\hbar}
\right),
```
where $`\Delta A`$ is the modal action increment.

These kernels are generically non–Markovian.

## Bohmian Limit

In regimes where:

- the action increment is sharply peaked,

- admissibility is stable,

- internal moduli decouple,

the kernels concentrate on the characteristic flow:
``` math
K_{\Delta\tau}(\cdot\mid q_0,\dots,q_k)
\;\to\;
\delta\!\left(
q_{k+1} - \Phi^{(v)}_{\Delta\tau}(q_k)
\right),
```
where $`\Phi^{(v)}`$ is the flow generated by $`v=j/\rho`$.

<div class="theorem">

**Theorem 15** (Pilot–Wave as Zero–Noise Limit). *Pilot–wave dynamics arise as the zero–noise, peaked–kernel limit of the MTT indivisible stochastic process within an admissible basin.*

</div>

<div class="remark">

*Remark 16*. Outside this limit, deterministic Bohmian trajectories are replaced by history–dependent stochastic evolution, even though the underlying modal dynamics remain deterministic.

</div>

# Summary of the MTT–to–Pilot–Wave Mapping

<div class="center">

| **Pilot–Wave Concept**    | **MTT Origin**                               |
|:--------------------------|:---------------------------------------------|
| Wavefunction $`\psi`$     | Coherent–sector state under $`P=\Pi\circ I`$ |
| Born density $`|\psi|^2`$ | Derived basin measure                        |
| Probability current $`j`$ | Unitarity of $`H_{\mathrm{obs}}`$            |
| Guidance equation         | Characteristic flow of $`j/\rho`$            |
| Nonlocality               | Global action of coherent projector          |
| Collapse                  | Admissibility barrier crossing               |
| Quantum equilibrium       | Consistency, not postulate                   |
| Global trajectories       | *Forbidden* by noninvertibility              |

</div>

**In Part IV (final)**, we will:

- synthesize the results,

- contrast MTT, pilot–wave, and Everett interpretations,

- state precise conclusions and limits of applicability.

# Comparison with Interpretations of Quantum Mechanics

We briefly situate the present derivation relative to other major interpretations of quantum mechanics.

## Copenhagen-Type Interpretations

Copenhagen interpretations treat the Schrödinger equation as fundamental but supplement it with axiomatic measurement postulates. Collapse is taken as primitive and non-unitary.

By contrast, in MTT:

- the Schrödinger equation is derived rather than postulated,

- collapse is replaced by admissibility breakdown,

- no additional axioms beyond deterministic modal evolution are required.

## Everett / Many-Worlds

Everettian interpretations retain universal unitary evolution and deny physical collapse. However, they require an additional interpretation of branching and a nontrivial justification of the Born rule.

In MTT:

- unitary evolution is only intra-basin,

- branching corresponds to admissibility basin structure,

- probabilities arise from basin measures, not branch counting.

Thus MTT agrees with Everett that collapse is not fundamental, but rejects the claim of globally valid unitary evolution.

## Pilot–Wave Theory

Pilot–wave theory restores determinism by introducing configuration trajectories guided by the wavefunction.

The present paper shows that:

- pilot–wave guidance equations are *derived* in MTT,

- they require no additional ontological postulates,

- and they are valid only within admissible coherence basins.

MTT therefore subsumes pilot–wave theory as an effective description, while explaining its scope limitations.

# Main Results

We summarize the principal results of this paper.

1.  Modal Triplet Theory admits a deterministic modal flow on the full configuration space $`X`$.

2.  Coherent projection and observable pushforward induce an effective Schrödinger evolution on admissible coherence basins.

3.  The associated probability current defines a canonical configuration–space velocity field.

4.  The integral curves of this velocity field coincide with de Broglie–Bohm guidance equations.

5.  No hidden variables, stochastic postulates, or additional ontology are introduced.

6.  Pilot–wave dynamics are valid only intra–basin; they necessarily fail at admissibility barriers.

7.  Measurement corresponds to admissibility breakdown, not to physical collapse or branching.

8.  Outside the pilot–wave regime, MTT induces indivisible stochastic processes on observable histories.

# Interpretive Statement

The derivation presented here establishes the following:

> *Pilot–wave theory is not a fundamental alternative to quantum mechanics, but an emergent characteristic description of Modal Triplet Theory valid only within admissible coherence basins.*

From the MTT perspective:

- determinism is fundamental,

- probability is structural,

- nonlocal correlations arise from projection,

- and irreversibility is unavoidable at admissibility boundaries.

Pilot–wave mechanics correctly captures the semiclassical, deterministic limit of this structure, but cannot be globally extended without contradiction.

# Outlook

Several directions follow naturally from this work.

- **Relativistic extension:** Pilot–wave dynamics for relativistic fields arise from the same MTT framework without preferred foliations.

- **Quantum field theory:** Particle creation and annihilation correspond to basin transitions rather than trajectory endpoints.

- **Quantum gravity:** Horizon formation and evaporation are admissibility events, explaining information loss without violating determinism.

- **Cosmology:** Initial condition selection and probability measures are unified with quantum measurement under the same mechanism.

In this sense, Modal Triplet Theory provides a unifying framework in which the successes of pilot–wave theory are retained, its foundational problems are resolved, and its limitations are rendered unavoidable and precise.

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
