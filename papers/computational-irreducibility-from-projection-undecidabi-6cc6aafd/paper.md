---
abstract: |
  We prove that any effective physical description in the coherent universality class capable of reproducing irreversible measurement, stable classical records, relativistic locality, and finite predictivity necessarily exhibits algorithmic undecidability at the level of observable dynamics. Within the coherent universality class realized explicitly by Modal Triplet Theory (MTT), noninvertible projection together with admissible basin structure forces the existence of well-posed physical decision problems that no algorithm can decide. The result is formulated without reference to external time: the relevant bound is instead a coherence budget determined by basin geometry, spectral gaps, stability margins, and gravity. The proof constructs a uniform many-one reduction from the halting problem for universal two-counter machines to robust selection-event occurrence under admissibility. Computational irreducibility is thus shown to be a structural consequence of viable physical theories, distinct from chaos or stochasticity, and explains the absence of globally valid effective laws across measurement, spacetime, and ultraviolet completion.
author:
- |
  Peter Nero  
  Independent Researcher
current_version: v1.0
generated_from_main_tex_sha256: 7da3fd5ca3ca14aa5ffbfba172b70b61101f68babf8c3994306561d9e83fe4f7
paper_id: computational-irreducibility-from-projection-undecidabi-6cc6aafd
release_state: zenodo_released
released_version: v1.0
title: |
  **Computational Irreducibility from Projection:  
  Undecidability of Selection Events in Coherent Quantum Dynamics**
zenodo_doi: 10.5281/zenodo.18255391
zenodo_record_id: 18255391
zenodo_url: "https://zenodo.org/records/18255391"
---

# Introduction

A widespread assumption in fundamental physics is that, although prediction may be practically difficult, the effective laws governing observable phenomena are in principle computable. Classical chaos, quantum uncertainty, and statistical mechanics are typically understood as limits of prediction, not as failures of computability itself.

In this paper we show that this assumption is false for any theory that successfully accounts for irreversible measurement, stable macroscopic records, relativistic locality, and finite predictivity. The obstruction is not merely complexity but *undecidability*: there exist well-defined physical questions whose answers cannot be decided by any algorithm.

The result follows from three structural features that recur across successful approaches to measurement and quantum gravity:

1.  effective noninvertible projection,

2.  dynamically stable admissible basins with finite margins,

3.  truncation enforced by spectral gaps and admissibility.

These features define what we call the *coherent universality class*. Modal Triplet Theory provides a minimal explicit realization of this class, but the undecidability result does not depend on MTT-specific constructions.

# Effective Projection and Admissibility

## Reduced description

Let $`\mathcal{H}_{\mathrm{ext}}`$ denote an extended Hilbert space describing microscopic degrees of freedom, and let $`\mathcal{H}_4`$ denote the reduced Hilbert space supporting observable degrees of freedom. Effective states are trace-class operators $`\rho \in \mathcal{T}_1(\mathcal{H}_4)`$.

<div class="definition">

**Definition 1** (Noninvertible projection). A projection $`\mathcal{P}:\mathcal{H}_{\mathrm{ext}}\to\mathcal{H}_4`$ is *noninvertible* if distinct microscopic configurations map to the same reduced state and no physically admissible operation reconstructs the preimage.

</div>

Effective evolution is described by protocol-dependent maps
``` math
\begin{equation}
\rho_{n+1} = M_{\pi(n)}(\rho_n),
\end{equation}
```
where $`\pi`$ labels a protocol cycle. No global, state-independent generator is assumed.

## Admissible basins

<div class="definition">

**Definition 2** (Admissible basin). A subset $`\mathcal{B}_\alpha \subset \mathcal{T}_1(\mathcal{H}_4)`$ is an admissible basin if:

1.  it is invariant under $`M_\pi`$,

2.  it is contractive with a finite stability margin,

3.  stability persists under admissible protocol variations.

</div>

Admissible basins represent dynamically stable macrostates such as measurement outcomes, classical records, or geometric encodings.

# Selection Events and Records

<div class="definition">

**Definition 3** (Selection event). A *selection event* is an irreversible transition
``` math
e_{\alpha\to\beta}:\ \rho\in\mathcal{B}_\alpha \longrightarrow \rho'\in\mathcal{B}_\beta,
```
occurring when admissibility fails at a basin boundary and the trajectory is captured into a new stable basin.

</div>

Selection events write persistent information into a record $`\mathcal{R}= (\mathcal{R}^{(1)},\mathcal{R}^{(2)},\mathcal{R}^{(\mathrm{aux})})`$.

<div class="remark">

*Remark 4*. Selection events unify measurement outcomes, collapse transitions, and causal-set events as the same physical process viewed through different diagnostics.

</div>

# Coherence Budget and Admissible Horizon

## Selection potential and stability margins

Let $`\Xi(\rho)`$ denote a scalar admissibility or selection functional on $`\mathcal{T}_1(\mathcal{H}_4)`$ whose value controls basin stability. For each admissible basin $`\mathcal{B}_\alpha`$ there exists a critical value $`\Xi_{\mathrm{crit}}`$ such that $`\rho\in\mathcal{B}_\alpha`$ is stable if and only if $`\Xi(\rho)<\Xi_{\mathrm{crit}}`$.

Define the initial margin
``` math
\begin{equation}
m(\rho_0) := \Xi_{\mathrm{crit}} - \Xi(\rho_0)\,.
\end{equation}
```

The evolution of $`\Xi(\rho_n)`$ along admissible trajectories is influenced by disturbance, protocol-dependent driving, and discarded degrees of freedom. On bounded-geometry slabs, these effects admit uniform control in terms of the bottleneck data $`\Theta`$ (spectral gap $`\lambda_*`$, projector norm, Lipschitz constants, damping rates).

## Coherence budget

<div class="definition">

**Definition 5** (Coherence budget). Let $`\sigma^2(\Theta,\pi)`$ be a variance proxy bounding fluctuations of $`\Xi(\rho_n)`$ along admissible trajectories for protocol $`\pi`$. The *coherence budget* is defined as
``` math
\begin{equation}
\mathcal{B}(\rho_0;\Theta,\pi) :=
\frac{m(\rho_0)^2}{\sigma^2(\Theta,\pi)}\,.
\end{equation}
```

</div>

Large $`\mathcal{B}`$ corresponds to exponentially stable evolution with negligible probability of basin exit, while $`\mathcal{B}\sim O(1)`$ marks near-critical regimes exhibiting threshold (“knee”) behavior.

## Admissible horizon

The validity of the reduced description is limited not by an external time parameter but by admissibility itself.

<div class="definition">

**Definition 6** (Admissible horizon). Fix a truncation tolerance $`\varepsilon>0`$. The *admissible horizon* $`N_{\max}(\rho_0;\Theta,\pi,\varepsilon)`$ is the largest integer such that for all $`n\le N_{\max}`$ the reduced trajectory
``` math
\rho_{n+1} = M_{\pi(n)}(\rho_n)
```
remains within the admissible domain at tolerance $`\varepsilon`$.

</div>

The horizon $`N_{\max}`$ is determined by basin geometry and gravity-dependent stability encoded in $`\Theta`$; it is not an externally chosen clock time. The spectral gap $`\lambda_*`$ enters only by setting the encoding resolution and step granularity.

# Effective Encodings and Physical Decision Problems

## Finite encodings

All undecidability statements are made with respect to finite descriptions.

<div class="definition">

**Definition 7** (Effective instance). An effective instance is specified by a finite string encoding:

- an initial reduced state $`\rho_0`$ to tolerance $`\varepsilon`$ (e.g. a rational density matrix in a fixed basis),

- bottleneck data $`\Theta`$ given by finite rational approximations,

- a protocol schedule $`\pi`$, specified as a finite word over a fixed finite alphabet of admissible protocol primitives,

- a designated selection event $`e_\star`$ (e.g. entry into a specified basin).

</div>

No noncomputable real numbers or infinite precision inputs are assumed.

## Robust selection language

Because physical admissibility requires robustness under small preparation errors, event occurrence must be formulated robustly.

<div class="definition">

**Definition 8** (Robust selection language). Define
``` math
\mathrm{SEL}^{\mathrm{rob}}_\varepsilon:=
\Big\{(\rho_0,\Theta,\pi,\varepsilon,e_\star)\ \Big|\ 
\exists n\le N_{\max}(\rho_0;\Theta,\pi,\varepsilon)\ \text{s.t. } e_\star \text{ occurs for all }
\tilde\rho_0\in B_\varepsilon(\rho_0)\Big\},
```
where $`B_\varepsilon(\rho_0)`$ is the trace-norm $`\varepsilon`$-ball around $`\rho_0`$.

</div>

<div class="remark">

*Remark 9*. $`\mathrm{SEL}^{\mathrm{rob}}_\varepsilon`$ asks whether a selection event occurs *before admissibility is lost*, independently of small preparation errors. This matches the operational meaning of events in MTT.

</div>

## Bounded horizon and decidability

Although $`N_{\max}`$ is finite for each instance, it is instance-dependent, not known a priori, and determined by basin geometry rather than by an external clock.

Moreover, membership in $`\mathrm{SEL}^{\mathrm{rob}}_\varepsilon`$ is not a simple pointwise reachability question. It requires event occurrence for all perturbations within $`B_\varepsilon(\rho_0)`$, a robust reachability property that is strictly stronger than simulating a single trajectory. Finite horizons therefore do not restore decidability.

# Encoding Universal Computation in Event Logs

## Two-counter machines

A two-counter (Minsky) machine $`\mathcal{M}`$ consists of:

- a finite set of control states $`Q`$,

- two nonnegative integer counters $`c_1,c_2`$,

- instructions of the form <span class="smallcaps">INC</span>$`(i)`$, <span class="smallcaps">DECJZ</span>$`(i)`$, and <span class="smallcaps">HALT</span>.

Two-counter machines are computationally universal; the halting problem for such machines is undecidable.

## Encoding into basins and records

Each control state $`q\in Q`$ is associated with a basin $`\mathcal{B}_q`$. Two counters are encoded by persistent record registers $`\mathcal{R}^{(1)},\mathcal{R}^{(2)}`$.

Define the token-count functionals
``` math
\begin{equation}
\mathsf{N}_i(\rho) := |\mathcal{R}^{(i)}|,\qquad i=1,2,
\end{equation}
```
measured at tolerance $`\varepsilon`$.

An encoding of a machine configuration $`(q,c_1,c_2)`$ is any $`\rho\in\mathcal{B}_q`$ satisfying $`\mathsf{N}_1(\rho)=c_1`$ and $`\mathsf{N}_2(\rho)=c_2`$.

# Uniform Instruction Simulation

We now show that admissible projection dynamics can simulate a universal two-counter machine using selection events as irreversible computational tokens, without embedding computation in the control protocol itself.

## Uniform protocol family

Fix once and for all a finite set of admissible protocol primitives
``` math
\mathcal{P}=\{\Pi_1,\ldots,\Pi_k\},
```
each corresponding to a physically admissible protocol cycle (e.g. fixed measurement strength, probing duration, and control configuration). The protocol alphabet $`\mathcal{P}`$ is independent of the encoded program and input.

The protocol schedule $`\pi`$ is universal: at each step the choice of primitive depends only on the current basin label, not on the encoded machine or input. Thus all program and input data are encoded solely in the initial reduced state $`\rho_0`$.

## Instruction simulation lemma

<div class="proof">

*Proof.* We give an explicit construction.

#### Control basins.

Fix a universal two-counter machine $`\mathcal{M}`$ with control states $`Q=\{q_1,\dots,q_m\}`$ and a distinguished halting state $`q_{\mathrm{halt}}`$. By admissibility, there exists a finite family of dynamically stable basins $`\{\mathcal{B}_q\}_{q\in Q\cup\{q_{\mathrm{halt}}\}}`$ such that: (i) each $`\mathcal{B}_q`$ is invariant under admissible intra-basin dynamics, (ii) each basin has a finite stability margin, (iii) $`\mathcal{B}_{q_{\mathrm{halt}}}`$ is absorbing on the slab.

Membership in $`\mathcal{B}_q`$ encodes the current control state.

#### Record registers.

Let $`\mathcal{R}^{(1)}`$ and $`\mathcal{R}^{(2)}`$ be persistent record registers, each consisting of a countable collection of stable record sites. Define the token-count functionals
``` math
\mathsf{N}_i(\rho) := |\mathcal{R}^{(i)}| , \qquad i=1,2,
```
measured at truncation tolerance $`\varepsilon`$. By record stability, tokens cannot be erased by any admissible operation on the slab.

#### Encoding.

A machine configuration $`(q,c_1,c_2)`$ is encoded by any reduced state $`\rho\in\mathcal{B}_q`$ such that $`\mathsf{N}_1(\rho)=c_1`$ and $`\mathsf{N}_2(\rho)=c_2`$. Finite stability margins guarantee robustness of this encoding under perturbations of size $`\varepsilon`$.

#### Protocol primitives.

Fix once and for all a finite protocol alphabet $`\mathcal{P}=\{\Pi_1,\dots,\Pi_k\}`$, independent of $`\mathcal{M}`$ and its input. Each primitive $`\Pi_j`$ corresponds to a physically admissible protocol cycle (measurement strength, probing duration, and control configuration fixed).

The interpreter rule is as follows: when the reduced state lies in basin $`\mathcal{B}_q`$, apply the unique protocol primitive $`\Pi(q)\in\mathcal{P}`$ assigned to $`q`$. This rule depends only on the basin label and is fixed globally.

#### Increment.

If the instruction at $`q`$ is $`\textsc{INC}(i)`$ with next state $`q'`$, the protocol primitive $`\Pi(q)`$ is chosen so that the reduced dynamics induces a selection event appending exactly one new stable token to $`\mathcal{R}^{(i)}`$, followed by capture into $`\mathcal{B}_{q'}`$. This is realized by a controlled basin exit whose post-capture record includes the new token. Irreversibility follows from basin capture.

#### Conditional decrement and branch.

If the instruction at $`q`$ is $`\textsc{DECJZ}(i)`$ with targets $`q_0,q_1`$, the protocol primitive $`\Pi(q)`$ is chosen so that its effect depends on the stability margin associated with $`\mathcal{R}^{(i)}`$:

- If $`\mathsf{N}_i(\rho)=0`$, the basin boundary corresponding to token presence is absent, and the trajectory is captured into $`\mathcal{B}_{q_0}`$.

- If $`\mathsf{N}_i(\rho)>0`$, the presence of a token shifts the admissibility functional $`\Xi`$ so that a knee transition occurs, inducing a selection event that marks one token inactive (reducing the effective count by one) and captures the trajectory into $`\mathcal{B}_{q_1}`$.

This branching uses only basin geometry and finite stability margins.

#### Halting.

If the instruction at $`q`$ is $`\textsc{HALT}`$, the corresponding protocol primitive induces capture into the absorbing basin $`\mathcal{B}_{q_{\mathrm{halt}}}`$, producing a distinguished selection event $`e_{\mathrm{halt}}`$. By admissibility, return from $`\mathcal{B}_{q_{\mathrm{halt}}}`$ is excluded on the slab.

#### Uniformity.

The protocol alphabet $`\mathcal{P}`$ and interpreter rule $`\Pi(q)`$ are fixed independently of the machine $`\mathcal{M}`$ and input $`w`$. All program and input information is encoded solely in the initial reduced state $`\rho_0`$ via basin membership and record tokens. Thus the construction is uniform.

#### Correctness.

By induction on the number of protocol cycles, the reduced dynamics simulates the step-by-step evolution of $`\mathcal{M}`$. Each instruction is faithfully realized, and halting occurs if and only if the reduced trajectory enters $`\mathcal{B}_{q_{\mathrm{halt}}}`$.

This completes the construction. ◻

</div>

<div class="proof">

*Proof.* Increment operations correspond to controlled selection events that append a stable token to the appropriate record register. Conditional decrement-and-branch operations are realized by threshold (knee) behavior at basin boundaries: the presence of a token shifts the stability margin so that the same protocol primitive induces capture into different basins. Halting corresponds to capture into a designated absorbing basin. Uniformity follows because the protocol family and interpreter rule are fixed once and for all. ◻

</div>

<div class="remark">

*Remark 10*. No computation is hidden in the controller. Universality arises from basin structure and record encoding under noninvertible projection.

</div>

# Undecidability of Selection under Coherence Bounds

We now state and prove the main result.

<div class="theorem">

**Theorem 11** (Undecidability of robust selection). *The protocol alphabet $`\mathcal{P}`$ and the interpreter rule are fixed independently of the machine $`\mathcal{M}`$ and input $`w`$; universality arises solely from state encoding and basin dynamics under projection.*

*``` math
\mathrm{HALT} \;\le_m\; \mathrm{SEL}^{\mathrm{rob}}_\varepsilon.
```
Consequently, there exists no algorithm that decides membership in $`\mathrm{SEL}^{\mathrm{rob}}_\varepsilon`$.*

</div>

<div class="proof">

*Proof.* Let $`\mathcal{M}`$ be a two-counter machine and $`w`$ an input. Define a computable mapping
``` math
F:(\mathcal{M},w)\mapsto(\rho_0,\Theta,\pi,\varepsilon,e_\star),
```
where:

- $`\rho_0`$ encodes the initial control state and counter values via basin membership and record tokens;

- $`\Theta`$ is fixed bottleneck data ensuring admissibility;

- $`\pi`$ is the fixed universal protocol schedule;

- $`e_\star`$ denotes entry into the halting basin $`\mathcal{B}_{\mathrm{halt}}`$.

By Lemma 7.1, the reduced dynamics simulates $`\mathcal{M}`$ step by step. Finite stability margins ensure robustness: the occurrence or non-occurrence of $`e_\star`$ is invariant under all perturbations in $`B_\varepsilon(\rho_0)`$. Therefore,
``` math
\mathcal{M}\ \text{halts on } w
\iff
(\rho_0,\Theta,\pi,\varepsilon,e_\star)\in\mathrm{SEL}^{\mathrm{rob}}_\varepsilon.
```
Since the halting problem is undecidable, so is $`\mathrm{SEL}^{\mathrm{rob}}_\varepsilon`$. ◻

</div>

<div class="corollary">

**Corollary 12** (Computability limitation). *There exists no algorithm that decides robust selection-event occurrence uniformly over all admissible instances $`(\rho_0,\Theta,\pi,\varepsilon,e_\star)`$.*

</div>

# Gravity, Measurement, and the Origin of Irreducibility

Undecidability in this framework is not an artifact of exotic microscopic dynamics but a consequence of projection and admissibility.

## Role of gravity

Gravity enters through the bottleneck vector $`\Theta`$. Curvature and geometry control stability margins, damping rates, and thus the coherence budget $`\mathcal{B}`$. Gravity therefore sets the *resource bound* for effective predictability: how long a configuration remains admissible and whether selection events can occur.

## Measurement and records

Selection events coincide with irreversible measurement outcomes. The existence of stable records requires finite stability margins, which in turn force noninvertible projection. Computational irreducibility thus arises directly from the physical requirements of measurement and record stability.

## Beyond chaos

Chaos concerns sensitivity to initial conditions under a fixed effective law. Here the obstruction is stronger: no single effective law exists that applies across admissible regimes. The unpredictability is therefore algorithmic, not merely practical or probabilistic.

# Ornstein–Uhlenbeck and Kramers Bounds

The coherence budget introduced in Sec. 4 is justified by standard Ornstein–Uhlenbeck and Kramers-type estimates for barrier crossing in stochastic systems with drift and damping.

Let $`u_n`$ denote the least-stable coordinate normal to a basin boundary, with effective evolution
``` math
\begin{equation}
u_{n+1} = (1-\gamma)u_n + \eta_n ,
\end{equation}
```
where $`\gamma>0`$ is the stability margin and $`\eta_n`$ is a disturbance term with bounded variance determined by $`\Theta`$ and the protocol $`\pi`$. Standard results imply
``` math
\begin{equation}
\mathrm{Var}[u_n] \le \frac{\sigma^2(\Theta,\pi)}{2\gamma},
\end{equation}
```
uniformly on admissible slabs.

Barrier crossing probabilities admit exponential bounds of the form
``` math
\begin{equation}
\mathbb{P}(\text{exit}) \;\lesssim\;
\exp\!\left(-\frac{m(\rho_0)^2}{\sigma^2(\Theta,\pi)}\right)
= \exp(-\mathcal{B}),
\end{equation}
```
justifying the interpretation of $`\mathcal{B}`$ as a physical coherence budget and $`N_{\max}`$ as a stability-limited horizon.

# Two-Counter Machines and Universality

Two-counter (Minsky) machines consist of a finite control and two unbounded nonnegative integer registers with instructions <span class="smallcaps">INC</span>, <span class="smallcaps">DECJZ</span>, and <span class="smallcaps">HALT</span>. It is a classical result that such machines are computationally universal and that their halting problem is undecidable.

The use of two counters is minimal: one-counter machines are decidable, while two counters suffice to simulate arbitrary Turing machines. This minimality aligns with the present construction, which uses only two record registers $`\mathcal{R}^{(1)},\mathcal{R}^{(2)}`$ and a finite basin structure.

# Chaos versus Undecidability

It is important to distinguish chaos from undecidability.

Chaotic systems exhibit sensitive dependence on initial conditions but are governed by a fixed, computable evolution law. In contrast, the undecidability established here concerns the absence of any algorithmic law that decides selection-event occurrence across admissible regimes. The obstruction is structural and persists even when individual trajectories are computable.

# Relation to Undecidability in Hybrid Systems

Undecidability is known to arise in robust reachability problems for hybrid systems combining continuous dynamics with discrete transitions and threshold guards. Classic results show that requiring correctness under perturbations can render reachability undecidable even for systems with computable local flows.

The present work is not a reformulation of those results. Instead, it identifies a physical mechanism—noninvertible projection with admissibility and basin structure—that forces effective dynamics into a similar undecidable class. The robustness condition in $`\mathrm{SEL}^{\mathrm{rob}}_\varepsilon`$ is not a technical convenience but a physical requirement reflecting stability of records under small preparation errors.

Thus, while consonant with known results on hybrid systems, the undecidability here arises from empirical requirements alone, without assuming infinite precision, exotic real parameters, or ad hoc discrete control.

# Relation to Other Shadow Constructions

The undecidability result integrates naturally with other shadow constructions within the coherent universality class:

- collapse and measurement-induced thresholds arise from basin exits;

- causal-set event structure corresponds to the log of selection events;

- asymptotic safety fixed points appear as truncation shadows of a UV endpoint;

- loop quantum gravity discreteness arises as an encoding artifact;

- noncommutative geometry and the spectral action encode admissible overlap structure.

Computational irreducibility explains why these distinct frameworks capture consistent partial shadows without yielding a single globally computable effective law.

<div class="thebibliography">

Minsky, M. (1967). . Prentice-Hall.

Alur, R., Courcoubetis, C., Henzinger, T. A., & Ho, P.-H. (1995). Hybrid automata: An algorithmic approach to the specification and verification of hybrid systems. , 138, 3–34.

Henzinger, T. A. (1996). The theory of hybrid automata. .

Branicky, M. S. (1995). Universal computation and other capabilities of hybrid and continuous dynamical systems. , 138, 67–100.

Asarin, E., & Maler, O. (2000). As soon as possible: Time optimal control for timed automata. .

</div>
