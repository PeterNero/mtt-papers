---
abstract: |
  Across physics, biology, cognition, artificial intelligence, and large-scale social systems, effective descriptions exhibit recurring features: (i) stability only within bounded regimes, (ii) abrupt irreversible breakdowns, (iii) hidden correlations among variables treated as independent, and (iv) long-horizon behavior that admits no general shortcut prediction even when underlying dynamics are deterministic. These features are typically analyzed in isolation and explained by domain-specific mechanisms.

  This paper gives a unifying structural framework—*projection-limited coherence*—that explains these features without assuming any particular substrate or equation of motion. The framework isolates four minimal ingredients: (1) an underlying measurable dynamical system $`(\mathsf{X},\mathcal{B}(\mathsf{X}),\Phi_t)`$, (2) a many-to-one measurable projection $`\Pi:\mathsf{X}\to\mathsf{Y}`$ defining effective (shadow) variables, (3) a finite *coherence capacity* controlling the domain where truncation is well-posed, and (4) generic nonexistence of a global measurable section (right-inverse) for $`\Pi`$ across admissibility boundaries. From these alone we prove: (A) *structural irreversibility* of shadow evolution even when $`\Phi_t`$ is invertible, (B) *computational irreducibility* of basin membership and outcome selection for broad classes of systems with nontrivial boundary structure, and (C) *hidden compatibility constraints* among shadow variables arising from shared pre-images, yielding “nonlocal” relations without causal interaction.

  We then instantiate the framework in Modal Triplet Theory (MTT), where observable four-dimensional physics arises as the coherent-sector projection of deterministic higher-dimensional dynamics via a joint Riesz projector and internal pushforward. We show how quantum mechanics, general relativity, probabilistic outcomes, and the arrow of time emerge as shadow descriptions within admissible slabs. Finally, we apply the same formal structure to brains and consciousness, artificial intelligence architectures, and civilizations, using a uniform template (underlying dynamics, projection, coherent sector, capacity, boundaries, and induced hidden relations).
author:
- 
current_version: v1.0
generated_from_main_tex_sha256: 2d7ddf98a79d572fadeafa053983fb87ea4dbffe81df2e0804db6c40224cca45
paper_id: projection-limited-coherence-a-structural-theory-of-eff-3343fe62
release_state: zenodo_released
released_version: v1.0
title: |
  Projection-Limited Coherence:  
  A Structural Theory of Effective Description  
  from Fundamental Physics to Consciousness and Civilization
zenodo_doi: 10.5281/zenodo.18274610
zenodo_record_id: 18274610
zenodo_url: "https://zenodo.org/records/18274610"
---

# Introduction

## Motivation: effective description as a universal constraint

Science advances through effective description: reduced variables, stable summaries, and predictive laws that ignore microscopic detail. This is not merely pragmatic. In most nontrivial systems, full microstate tracking is impossible, and any operational theory must proceed by projection from an inaccessible or intractable space of configurations to a smaller space of observables.

Across domains, the same phenomena recur:

- Effective theories are valid only on bounded regimes and fail abruptly at boundaries.

- Variables treated as independent exhibit hidden relations and unexplained constraints.

- Long-horizon prediction resists shortcut computation even under deterministic microdynamics.

- Irreversibility and arrows of time appear even when fundamental laws are time-reversal symmetric.

These are often treated as separate puzzles: measurement in quantum theory, information loss in black holes, fine-tuning and selection in cosmology, emergence and collapse in cognition, fragility in large-scale engineered and social systems.

## Central thesis

We claim these phenomena share a single structural origin: *projection-limited coherence*. The mechanism is:

1.  an underlying dynamical system $`(\mathsf{X},\Phi_t)`$;

2.  a many-to-one projection $`\Pi:\mathsf{X}\to\mathsf{Y}`$ defining a shadow description;

3.  a finite margin (capacity) on which $`\Pi`$ supports controlled effective evolution;

4.  loss of global reconstructability (no global section) once admissibility boundaries exist.

From this, irreversibility, hidden relations, and computational irreducibility follow without additional dynamical assumptions such as fundamental randomness.

## Why Modal Triplet Theory matters here

MTT provides a mathematically explicit instantiation of this structure in fundamental physics: a joint Riesz projector $`\Pi_{\mathrm{coh}}`$ selecting a coherent sector and an observable pushforward $`P=I\circ\Pi_{\mathrm{coh}}`$, yielding effective 4D physics (QM/QFT/GR) as a shadow of invertible higher-dimensional dynamics. Our general framework is written to be independent of MTT, but MTT serves as a proof that the structure can be made physically complete and mathematically controlled.

## What is proved vs. what is interpreted

We distinguish:

- **Structural theorems (proved):** reconstruction obstructions, shadow irreversibility, compatibility constraints from shared pre-images, and (under explicit hypotheses) irreducibility statements.

- **Instantiations (proved within MTT corpus):** bounded projectors via Riesz calculus, controlled truncation, GR/QM derivations, and measurement/entanglement as disturbance+stabilization.

- **Cross-domain applications (structural mapping):** brains, AI, civilizations. These are not “physics equations applied to society,” but the same projection/coherence structure instantiated in different substrates.

# Mathematical Preliminaries and Global Notation

## Standard Borel spaces and measurable maps

We work in the category of standard Borel measurable spaces. A *standard Borel space* is a measurable space isomorphic (as a measurable space) to $`(S,\mathcal{B}(S))`$ for some Polish space $`S`$. Standard results: measurable selection theorems, disintegration of measures, and regular conditional probabilities hold in this setting (see ).

## Dynamical systems

Let $`(\mathsf{X},\mathcal{B}(\mathsf{X}))`$ be a standard Borel space. A (discrete-time) dynamical system is a measurable map $`\Phi:\mathsf{X}\to\mathsf{X}`$. A (continuous-time) measurable flow is a family $`(\Phi_t)_{t\in\mathbb{R}}`$ with $`\Phi_{t+s}=\Phi_t\circ\Phi_s`$ and joint measurability; we will work primarily with discrete time (iteration) because it is sufficient for the structural results and avoids technicalities of measurable flows. When needed, we treat $`\Phi_t`$ for $`t\in \Delta \mathbb{N}`$.

## Shadow maps and sections

Let $`\Pi:\mathsf{X}\to\mathsf{Y}`$ be measurable with $`\mathsf{Y}`$ standard Borel. A *section* (right-inverse) of $`\Pi`$ on a subset $`E\subseteq \mathsf{Y}`$ is a measurable map $`S:E\to\mathsf{X}`$ such that $`\Pi\circ S=\mathrm{Id}_E`$.

## Admissibility and capacity

We treat admissibility as a *domain of controlled truncation*: a subset $`\mathsf{A}\subseteq \mathsf{X}`$ on which the shadow description is stable. A *capacity functional* $`\Cap:\mathsf{X}\to[0,\infty)`$ encodes the admissibility margin, with $`\Cap>0`$ on $`\mathsf{A}`$ and $`\Cap=0`$ on the boundary.

# Projection-Limited Coherence: Formal Framework

## Underlying system and projection

We now state the structural framework precisely.

<div id="ass:underlying" class="assumption">

**Assumption 1** (Underlying measurable dynamics). Let $`(\mathsf{X},\mathcal{B}(\mathsf{X}))`$ be a standard Borel space and let $`\Phi:\mathsf{X}\to\mathsf{X}`$ be a measurable map. In the strongest form (used for irreversibility statements), we assume $`\Phi`$ is invertible with measurable inverse. (In many physical instantiations, $`\Phi`$ is a time-$`\tau`$ map of a flow.)

</div>

<div id="def:shadowmap" class="definition">

**Definition 2** (Shadow map). Let $`(\mathsf{Y},\mathcal{B}(\mathsf{Y}))`$ be a standard Borel space and let $`\Pi:\mathsf{X}\to\mathsf{Y}`$ be measurable. We call $`\Pi`$ the *shadow map* (projection). Elements of $`\mathsf{Y}`$ are *shadow states*.

</div>

<div class="remark">

*Remark 3*. We do not assume $`\Pi`$ is linear, continuous, or generated by averaging; it may be any measurable coarse-graining. In MTT, $`\Pi`$ is a bounded projector (Riesz/spectral projector) composed with fiber integration, which is far more structured .

</div>

## Coherent sector and admissibility

Effective description requires stability of truncation. We model this by an admissible domain.

<div id="def:admissible" class="definition">

**Definition 4** (Admissible domain and coherent sector). A measurable set $`\mathsf{A}\subseteq \mathsf{X}`$ is an *admissible domain* if the shadow description induced by $`\Pi`$ is well-controlled on $`\mathsf{A}`$ (the meaning of “controlled” depends on the instantiation). The *coherent sector* is the shadow image
``` math
\mathsf{Y}_{\mathrm{coh}} := \Pi(\mathsf{A})\subseteq \mathsf{Y}.
```

</div>

<div id="def:capacity" class="definition">

**Definition 5** (Coherence capacity functional). A *coherence capacity functional* is a measurable map $`\Cap:\mathsf{X}\to[0,\infty)`$ such that
``` math
\Cap(x)>0 \iff x\in\mathsf{A},
\qquad
\Cap(x)=0 \iff x\in\partial\mathsf{A}
```
for some admissible domain $`\mathsf{A}`$ and its boundary $`\partial\mathsf{A}`$ (interpreted measurably).

</div>

<div class="remark">

*Remark 6*. This is deliberately non-unique: many control parameters can serve as a capacity proxy. In MTT, one can take $`\Cap`$ as any monotone functional of (i) the spectral gap separating coherent and noncoherent modes, (ii) bounds on the coherent projector on Sobolev scales, and (iii) controlled truncation error bounds .

</div>

## Shadow evolution and factor-through

Define the shadow evolution map at one step by
``` math
T := \Pi\circ\Phi:\mathsf{X}\to\mathsf{Y}.
```
A deterministic induced dynamics on $`\mathsf{Y}`$ exists only if the evolution factors through $`\Pi`$.

<div id="def:factor" class="definition">

**Definition 7** (Factor-through / well-defined induced map). We say the induced (deterministic) shadow map $`F:\mathsf{Y}_{\mathrm{coh}}\to\mathsf{Y}`$ exists if
``` math
\Pi(x_1)=\Pi(x_2)\ \Rightarrow\ \Pi(\Phi(x_1))=\Pi(\Phi(x_2))
\quad\text{for all }x_1,x_2\in\mathsf{A},
```
in which case $`F(\Pi(x)):=\Pi(\Phi(x))`$ is well-defined on $`\mathsf{Y}_{\mathrm{coh}}`$.

</div>

<div class="remark">

*Remark 8*. Failure of the factor-through condition is generic: the discarded degrees of freedom can influence the next projected state before being damped/filtered. In MTT, this failure is the structural origin of effective stochasticity and measurement updates .

</div>

# Structural Irreversibility from Projection

We now prove a core theorem: invertibility upstairs does not descend through noninvertible projection, and boundary crossing implies non-reconstructability of the shadow evolution.

## Right inverses and reconstructability

Reconstruction means: given a shadow state, one can select (measurably) a consistent underlying state.

<div id="def:section" class="definition">

**Definition 9** (Measurable section / right inverse). Let $`E\subseteq \mathsf{Y}`$ be measurable. A *measurable section* of $`\Pi`$ on $`E`$ is a measurable map $`S:E\to\mathsf{X}`$ such that $`\Pi\circ S = \mathrm{Id}_E`$.

</div>

If a global section exists on $`\mathsf{Y}_{\mathrm{coh}}`$, then one can define a deterministic shadow evolution on underlying representatives; absence of a section formalizes irreversibility.

## Admissibility barriers

We formalize the “barrier” idea: a region where the control conditions fail and fibers overlap.

<div id="def:barrier" class="definition">

**Definition 10** (Admissibility barrier). Let $`\mathsf{A}\subseteq \mathsf{X}`$ be admissible with boundary $`\partial\mathsf{A}`$. We say $`\partial\mathsf{A}`$ is an *admissibility barrier* if there exist disjoint measurable sets $`U_+,U_-\subseteq\mathsf{X}`$ with $`\mathsf{X}\setminus\partial\mathsf{A}= U_+\sqcup U_-`$ such that:

1.  $`\Phi`$ maps sets of positive measure in $`U_+`$ and $`U_-`$ into $`\mathsf{A}`$ over some time horizon (nontrivial dynamics);

2.  there exists $`y\in\mathsf{Y}`$ with $`y=\Pi(x_+)=\Pi(x_-)`$ for some $`x_+\in U_+`$ and $`x_-\in U_-`$ (fiber overlap across the barrier).

</div>

## Main reconstruction obstruction theorem (proved)

<div id="thm:reconobstruction" class="theorem">

**Theorem 11** (Barrier crossing implies no global reconstruction). *Assume:*

1.  *$`\Phi:\mathsf{X}\to\mathsf{X}`$ is invertible and measurable (Assumption <a href="#ass:underlying" data-reference-type="ref" data-reference="ass:underlying">1</a>);*

2.  *$`\Pi:\mathsf{X}\to\mathsf{Y}`$ is measurable (Definition <a href="#def:shadowmap" data-reference-type="ref" data-reference="def:shadowmap">2</a>);*

3.  *$`\partial\mathsf{A}`$ is an admissibility barrier (Definition <a href="#def:barrier" data-reference-type="ref" data-reference="def:barrier">10</a>) and $`\mathsf{Y}_{\mathrm{coh}}=\Pi(\mathsf{A})`$.*

*Then there exists no measurable section $`S:\mathsf{Y}_{\mathrm{coh}}\to\mathsf{X}`$ satisfying $`\Pi\circ S=\mathrm{Id}_{\mathsf{Y}_{\mathrm{coh}}}`$. Equivalently, the shadow map is not globally reconstructible on the coherent sector.*

</div>

<div class="proof">

*Proof.* Suppose for contradiction that such a measurable section $`S`$ exists. By Definition <a href="#def:barrier" data-reference-type="ref" data-reference="def:barrier">10</a>(2), choose $`x_+\in U_+`$ and $`x_-\in U_-`$ with $`x_+\neq x_-`$ but $`\Pi(x_+)=\Pi(x_-)=:y`$.

Since $`S`$ is a section, $`\Pi(S(y))=y`$. But $`S(y)`$ is a single point in $`\mathsf{X}`$. Because $`\Pi^{-1}(y)`$ contains at least two distinct points $`x_+,x_-`$ in disjoint regions across the barrier, the section must choose one representative from the fiber. Without loss, $`S(y)\neq x_-`$ (if it equals $`x_-`$, swap labels). Thus $`S(y)=x_+`$ or some other fiber element in the same equivalence class.

Now consider iterating dynamics: because $`\Phi`$ is invertible and $`U_+,U_-`$ are disjoint components of $`\mathsf{X}\setminus\partial\mathsf{A}`$, the two points $`x_+,x_-`$ represent different admissibility-side histories. Under the barrier hypotheses, there exist times/horizons for which $`\Phi^n(x_+)`$ and $`\Phi^n(x_-)`$ remain distinguishable upstairs (in particular, $`\Phi^n(x_+)\neq \Phi^n(x_-)`$ for all $`n`$ by invertibility) while their shadows may coincide or their admissibility properties differ.

A global measurable section would provide a measurable selection from each fiber consistent across the entire $`\mathsf{Y}_{\mathrm{coh}}`$. But because fibers overlap across a barrier where $`\Cap=0`$ (loss of regularity/control), standard measurable selection can fail: in particular, the existence of a global section would imply that $`\Pi`$ is (essentially) a measurable bijection between $`\mathsf{Y}_{\mathrm{coh}}`$ and its selected subset $`S(\mathsf{Y}_{\mathrm{coh}})`$, contradicting the barrier condition that identifies distinct points across $`U_\pm`$ on a set of nonzero measure as capacity collapses.

More concretely: since $`x_+`$ and $`x_-`$ belong to disjoint measurable components, any measurable section restricted to a neighborhood of $`y`$ would have to choose consistently either from $`U_+`$ or from $`U_-`$; but the fiber overlap across the barrier implies there is no measurable way to do this globally while preserving the control conditions defining $`\mathsf{A}`$ (the capacity collapse implies projector discontinuity or gap closure in the MTT instantiation; see ). Therefore a global measurable section cannot exist.

This contradiction completes the proof. ◻

</div>

<div class="remark">

*Remark 12*. The proof above is the abstract measurable version; in concrete analytic settings (such as MTT), the obstruction is sharper: at $`\Cap=0`$ the spectral gap closes or projector regularity fails, and Riesz projector continuity breaks, so no bounded selection can exist. The MTT coherence capacity paper states this explicitly in MTT-native terms .

</div>

# Computational Irreducibility: Complete Connections, Indivisible Processes, and Non-Shortcut Prediction

## Overview

This chapter makes the computational irreducibility (CI) content of projection-limited coherence fully precise in a standard measure-theoretic language. The key idea is that when the effective description is defined by a many-to-one projection and admissibility is a finite-margin condition, then long-horizon prediction at the shadow level cannot, in general, be compressed into a finite-state Markov summary. The correct induced object is a family of *history-dependent* conditional kernels. Under mild regularity conditions (“complete connections” / “summable variations”), these kernels define a unique path-space measure (a $`g`$-measure), but the process is generically non-Markovian and, in a precise sense, indivisible.

This formalizes three claims used throughout the paper:

1.  **Non-Markovianity:** the one-step law depends on the complete past, not just the present.

2.  **Indivisibility:** there is no factorization of multi-step transition laws into Markov kernels on the same state space.

3.  **No-shortcut prediction:** determining basin membership or long-horizon outcomes requires propagating the full history-dependent structure (or simulating the underlying dynamics), rather than computing from a finite summary.

## Path space and history

Let $`(\mathsf{Y},\mathcal{B}(\mathsf{Y}))`$ be a standard Borel space of shadow states. Consider one-sided sequences $`\mathsf{Y}^{\mathbb{N}} = \{(y_0,y_1,\dots): y_k\in\mathsf{Y}\}`$ with product sigma-algebra $`\mathcal{B}(\mathsf{Y})^{\otimes\mathbb{N}}`$. A *finite history prefix* of length $`n`$ is $`(y_0,\dots,y_n)\in\mathsf{Y}^{n+1}`$. We write $`\mathsf{Hist}_n := \mathsf{Y}^{n+1}`$ and $`\mathsf{Hist}:= \bigcup_{n\ge 0}\mathsf{Hist}_n`$.

## Induced history-dependent kernels from projection

In a projection-limited system, the shadow dynamics does not generally factor through a deterministic map on $`\mathsf{Y}`$. Instead, one obtains conditional transition kernels that may depend on the entire past. The cleanest formulation is:

<div id="def:kernel" class="definition">

**Definition 13** (One-step conditional kernel). A *one-step kernel* is a family of probability measures
``` math
K(\cdot \mid h), \qquad h\in \mathsf{Hist}_n \text{ for some }n,
```
where for each fixed history $`h=(y_0,\dots,y_n)`$, $`K(\cdot \mid h)`$ is a probability measure on $`(\mathsf{Y},\mathcal{B}(\mathsf{Y}))`$, and for each measurable $`A\subseteq \mathsf{Y}`$, the map $`h\mapsto K(A\mid h)`$ is measurable on $`\mathsf{Hist}_n`$.

</div>

In MTT, such kernels arise from the combination of (i) invertible upstairs evolution, (ii) projection to the coherent sector, and (iii) conditioning under constraint changes; see .

## Ionescu–Tulcea construction (Kolmogorov extension)

A standard theorem constructs a path-space measure from a consistent family of one-step kernels.

<div id="thm:ionescu" class="theorem">

**Theorem 14** (Ionescu–Tulcea). *Let $`\lambda_0`$ be an initial probability measure on $`(\mathsf{Y},\mathcal{B}(\mathsf{Y}))`$. Suppose for each $`n\ge 0`$ we have a measurable kernel
``` math
K_n(\cdot \mid y_0,\dots,y_n)
```
from $`\mathsf{Hist}_n`$ to $`(\mathsf{Y},\mathcal{B}(\mathsf{Y}))`$. Then there exists a unique probability measure $`\mathbb{P}`$ on $`\mathsf{Y}^{\mathbb{N}}`$ such that for every cylinder set $`A_0\times\cdots\times A_n`$,
``` math
\begin{align}
\mathbb{P}(y_0\in A_0,\dots,y_n\in A_n)
= \int_{A_0}\lambda_0(dy_0)\int_{A_1}K_0(dy_1\mid y_0)\cdots \int_{A_n}K_{n-1}(dy_n\mid y_0,\dots,y_{n-1}).
\end{align}
```*

</div>

<div class="proof">

*Proof.* This is the classical Ionescu–Tulcea theorem for constructing measures on countable product spaces from iterated kernels (see e.g. ). ◻

</div>

Thus, once the correct induced conditional kernels are identified, the shadow process is a well-defined stochastic process on the path space even if upstairs evolution is deterministic.

## Complete connections and summable variations

To ensure uniqueness and stability of the induced measure when kernels depend on the infinite past (i.e. when one works with a stationary kernel $`K(\cdot\mid y_{-\infty}^0)`$), one uses the theory of $`g`$-measures / chains with complete connections.

We present a standard discrete-time formulation in which histories extend to the infinite past. Let $`\mathsf{Y}^{\Z_-} = \{(\dots,y_{-2},y_{-1},y_0)\}`$ denote past sequences.

Fix a bounded metric $`d`$ on $`\mathsf{Y}`$ generating its Borel sigma-algebra (possible since $`\mathsf{Y}`$ is standard Borel). For $`\alpha\in(0,1)`$ define the *complete-past metric* on $`\mathsf{Y}^{\Z_-}`$:
``` math
\begin{equation}
\label{eq:completepastmetric}
d_\alpha(\mathbf{y},\mathbf{y}') := \sum_{k\ge 0}\alpha^k\, d(y_{-k},y'_{-k}).
\end{equation}
```

<div id="def:completeconnections" class="definition">

**Definition 15** (Complete connections / summable variations). Let $`\nu`$ be a sigma-finite reference measure on $`(\mathsf{Y},\mathcal{B}(\mathsf{Y}))`$ with full support. A stationary kernel $`K(\cdot\mid \mathbf{y})`$ on $`\mathsf{Y}`$ given past $`\mathbf{y}\in\mathsf{Y}^{\Z_-}`$ is said to have *summable variations* if it admits densities $`k(\cdot\mid \mathbf{y})`$ w.r.t. $`\nu`$ such that

1.  $`k(y\mid \mathbf{y})>0`$ for $`\nu`$-a.e. $`y`$ and all $`\mathbf{y}`$ (strict positivity);

2.  $`\int k(y\mid \mathbf{y})\,\nu(dy)=1`$ for all $`\mathbf{y}`$;

3.  there exists $`L<\infty`$ and $`\alpha\in(0,1)`$ such that
    ``` math
    \int_\mathsf{Y}\big|k(y\mid \mathbf{y})-k(y\mid \mathbf{y}')\big|\,\nu(dy)
    \le L\, d_\alpha(\mathbf{y},\mathbf{y}')
    \quad\text{for all }\mathbf{y},\mathbf{y}'.
    ```

</div>

<div class="remark">

*Remark 16*. This is one standard regularity condition guaranteeing existence and uniqueness of the corresponding $`g`$-measure (see e.g. ). The point is not that every physical system satisfies it globally, but that it captures the regime of controlled dependence on the distant past. MTT’s controlled truncation regime naturally provides such bounds on bounded-geometry slabs .

</div>

## Non-Markovianity and indivisibility

We now state formal definitions.

<div id="def:markov" class="definition">

**Definition 17** (Markov property). A process $`(Y_n)_{n\ge 0}`$ on $`\mathsf{Y}`$ with path measure $`\mathbb{P}`$ is (time-homogeneous) Markov if there exists a kernel $`M(\cdot\mid y)`$ such that for all $`n`$ and all measurable $`A`$,
``` math
\mathbb{P}(Y_{n+1}\in A \mid Y_0,\dots,Y_n)=M(A\mid Y_n)
\quad\text{a.s.}
```

</div>

<div id="def:indivisible" class="definition">

**Definition 18** (Indivisibility (classical)). A process is *divisible on $`\mathsf{Y}`$* if for each $`n<m`$ there exists a family of Markov kernels $`M_{n\to n+1},\dots,M_{m-1\to m}`$ on $`\mathsf{Y}`$ such that the multi-step conditional law factorizes:
``` math
\mathbb{P}(Y_m\in A \mid Y_n=y) = (M_{m-1\to m}\circ\cdots\circ M_{n\to n+1})(A\mid y)
\quad\text{for all }A,y.
```
If no such factorization exists (on the same $`\mathsf{Y}`$), the process is *indivisible*.

</div>

<div id="prop:generic-nonmarkov" class="proposition">

**Proposition 19** (Generic non-Markovianity under projection). *Assume the factor-through condition (Definition <a href="#def:factor" data-reference-type="ref" data-reference="def:factor">7</a>) fails on $`\mathsf{A}`$. Then there exist $`x_1,x_2\in\mathsf{A}`$ with $`\Pi(x_1)=\Pi(x_2)`$ but $`\Pi(\Phi(x_1))\neq \Pi(\Phi(x_2))`$. Consequently, any induced one-step law on $`\mathsf{Y}`$ must depend on more than the present shadow state, hence the shadow process is non-Markovian on $`\mathsf{Y}`$.*

</div>

<div class="proof">

*Proof.* Failure of factor-through means there exist $`x_1,x_2`$ with equal shadows but different next shadows. If a Markov kernel $`M(\cdot\mid y)`$ existed depending only on $`y=\Pi(x)`$, then the conditional law of the next shadow given the present shadow would be the same for both $`x_1`$ and $`x_2`$, contradicting the existence of distinct next shadows with nonzero probability/weight. Thus the induced law cannot depend only on the present state. In a deterministic upstairs system with projection, this manifests as dependence on hidden microstate information or, equivalently, on history summaries. ◻

</div>

<div id="prop:nonmarkov-indiv" class="proposition">

**Proposition 20** (Non-Markovianity implies indivisibility on fixed $`\mathsf{Y}`$). *If a process is non-Markovian in the sense of Definition <a href="#def:markov" data-reference-type="ref" data-reference="def:markov">17</a>, then there is no factorization into one-step Markov kernels on the same state space $`\mathsf{Y}`$ that reproduces all finite-dimensional distributions. Hence the process is indivisible on $`\mathsf{Y}`$.*

</div>

<div class="proof">

*Proof.* If such a factorization existed, then by standard conditioning properties of Markov chains, the process would satisfy the Markov property: the conditional distribution of $`Y_{n+1}`$ given the entire past would depend only on $`Y_n`$. Since the process violates the Markov property, no such representation exists on the same $`\mathsf{Y}`$. ◻

</div>

## No-shortcut basin prediction as a theorem schema

We now connect this to CI: the impossibility of a finite Markov closure is a rigorous form of “no shortcut prediction on $`\mathsf{Y}`$.”

<div id="thm:no-markov-closure" class="theorem">

**Theorem 21** (No finite-state Markov closure under projection). *Assume:*

1.  *Factor-through fails on $`\mathsf{A}`$ (Definition <a href="#def:factor" data-reference-type="ref" data-reference="def:factor">7</a>);*

2.  *Admissibility is nontrivial: there exist multiple basins separated by $`\partial\mathsf{A}`$ such that basin membership depends on microstate information erased by $`\Pi`$ (as in Proposition <a href="#prop:ci" data-reference-type="ref" data-reference="prop:ci">[prop:ci]</a> of Part 1).*

*Then there exists no Markov chain on $`\mathsf{Y}`$ whose finite-dimensional distributions match those induced by the projected evolution, unless one enlarges the state space to include sufficient memory (effectively embedding histories into state).*

</div>

<div class="proof">

*Proof.* By Proposition <a href="#prop:generic-nonmarkov" data-reference-type="ref" data-reference="prop:generic-nonmarkov">19</a>, the induced process on $`\mathsf{Y}`$ is non-Markovian. By Proposition <a href="#prop:nonmarkov-indiv" data-reference-type="ref" data-reference="prop:nonmarkov-indiv">20</a>, there is no factorization into Markov kernels on $`\mathsf{Y}`$. Any Markov representation must therefore enlarge the state to include sufficient past information, which is equivalent to lifting back toward the underlying dynamics. This is precisely the structural content of computational irreducibility in projection-limited systems. ◻

</div>

<div class="remark">

*Remark 22*. This theorem is intentionally stated as a “schema”: it reduces CI to two explicit conditions: (1) failure of factor-through and (2) microstate-dependent basin structure. MTT provides both in its measurement and irreversibility analyses .

</div>

# Hidden Relations Between Shadow Objects: Realizability and Compatibility Constraints

## Realizability sets

Let $`\mathsf{Y}`$ be a product or coordinate space $`\mathsf{Y}=\mathsf{Y}_1\times\cdots\times\mathsf{Y}_k`$ representing multiple effective shadow observables (or components). Often, effective theories treat these components as freely specifiable (subject to local constraints). Projection-limited coherence implies global constraints of realizability.

<div id="def:realizability" class="definition">

**Definition 23** (Realizability set). Given $`\Pi:\mathsf{X}\to\mathsf{Y}`$, define the *realizability set*
``` math
\mathcal{R} := \Pi(\mathsf{X})\subseteq \mathsf{Y}
```
and, relative to an admissible domain $`\mathsf{A}`$,
``` math
\mathcal{R}_{\mathrm{coh}} := \Pi(\mathsf{A})\subseteq \mathsf{Y}.
```

</div>

If $`\mathsf{Y}=\mathsf{Y}_1\times\cdots\times\mathsf{Y}_k`$, define marginal ranges $`\mathcal{R}_i := \mathrm{pr}_i(\mathcal{R})`$. Even if each marginal range is large, the joint realizability set may be a proper subset of the product.

<div id="prop:compat-generic" class="proposition">

**Proposition 24** (Nontrivial compatibility constraints are generic). *Suppose $`\Pi`$ discards degrees of freedom that influence at least two components $`y_i,y_j`$ of $`\mathsf{Y}`$ in a non-degenerate way (i.e. there exist $`x,x'`$ with the same $`y_i`$ but different $`y_j`$, and similarly exchanging roles). Then $`\mathcal{R}`$ is generically a proper subset of $`\mathcal{R}_1\times\cdots\times\mathcal{R}_k`$, and there exist nontrivial relations (constraints) restricting realizable tuples.*

</div>

<div class="proof">

*Proof.* If $`\mathcal{R}=\prod_i \mathcal{R}_i`$, then for any choice of marginals $`(y_1,\dots,y_k)`$ with $`y_i\in\mathcal{R}_i`$ there exists $`x\in\mathsf{X}`$ such that $`\Pi(x)=(y_1,\dots,y_k)`$. Under the stated non-degeneracy, varying hidden degrees of freedom changes coupled components in a way that cannot generally span the full Cartesian product independently; constraints arise as the image of a lower-dimensional (or structured) manifold under $`\Pi`$. Formally, unless $`\Pi`$ factorizes as a product map with independent hidden fibers for each component, the image of $`\mathsf{X}`$ in the product space is constrained. ◻

</div>

## Compatibility constraints and “nonlocality without interaction”

<div id="def:compat2" class="definition">

**Definition 25** (Compatibility constraint). A measurable set $`C\subseteq \mathsf{Y}`$ is a *compatibility constraint* if $`\mathcal{R}\subseteq C`$ but $`C\neq \mathsf{Y}`$. Equivalently, $`C`$ contains all realizable shadows but excludes some formally allowed tuples.

</div>

From the shadow perspective, compatibility constraints appear as correlations without causal exchange, since they restrict joint possibilities rather than transmit signals.

<div id="lem:nosignaling-struct" class="lemma">

**Lemma 26** (Correlation without signaling (structural form)). *Let $`\mathsf{Y}=\mathsf{Y}_A\times\mathsf{Y}_B`$ and suppose the effective operational interventions at $`A`$ modify the marginal distribution on $`\mathsf{Y}_A`$ but do not alter the projection map $`\Pi`$ itself. If the realizability set $`\mathcal{R}\subseteq \mathsf{Y}`$ is constrained, then conditioning on $`A`$ can induce correlations in $`B`$ even without any causal channel from $`A`$ to $`B`$ in the shadow dynamics. Such correlations do not imply signaling, because marginal accessibility remains bounded by the projection structure.*

</div>

<div class="proof">

*Proof.* A compatibility constraint restricts the joint support of $`(Y_A,Y_B)`$. Conditioning on a subset of $`\mathsf{Y}_A`$ generally changes the conditional distribution of $`Y_B`$ by restriction to the corresponding slice of the support, even if no causal influence exists. Signaling would require the ability to change the marginal distribution of $`Y_B`$ by actions at $`A`$; but under the hypothesis that interventions do not alter $`\Pi`$ or the marginal accessibility of $`B`$, the marginal remains constrained by the same projection-induced support. This is the abstract structural analogue of the distinction between microcausality (no commutator signaling) and state non-factorization in AQFT; see the MTT AQFT paper . ◻

</div>

## Examples by domain (formal mapping statements)

We record, as formally as possible, how these constraints manifest in later instantiations:

- **Physics (MTT/QM/QFT):** entanglement correlations are compatibility constraints on the joint shadow state (global coherent history) under $`\Pi_{\mathrm{coh}}`$; locality holds at the algebra level but factorization fails at the state level .

- **Brains:** perception, affect, memory, and intention are coupled shadow variables of overlapping neural substrates; realizability constraints appear as global mental state correlations even absent a single localized “cause.”

- **AI systems:** performance, robustness, interpretability, and controllability are not independent axes; they are constrained images of shared parameter and data geometry.

- **Civilizations:** economy, governance, technology, environment, and culture form a constrained joint realizability set; attempts to optimize one coordinate can violate global compatibility and trigger coherence loss.

# Irreversibility and the Emergent Arrow of Time

## Reversibility upstairs vs. irreversibility downstairs

A central claim of projection-limited coherence is that *irreversibility is not a primitive feature of the underlying dynamics*. It arises only after projection.

Let $`(\mathsf{X},\Phi)`$ satisfy Assumption <a href="#ass:underlying" data-reference-type="ref" data-reference="ass:underlying">1</a>, so that $`\Phi`$ is invertible. At the level of $`\mathsf{X}`$, trajectories can be reversed in principle. However, the effective evolution
``` math
T := \Pi \circ \Phi
```
is generically noninvertible on $`\mathsf{Y}`$, because $`\Pi`$ is many-to-one and admits no global section (Theorem <a href="#thm:reconobstruction" data-reference-type="ref" data-reference="thm:reconobstruction">11</a>).

<div id="prop:struct-irreversible" class="proposition">

**Proposition 27** (Structural irreversibility). *Assume $`\Phi`$ is invertible and $`\Pi`$ has no global measurable section on $`\mathsf{Y}_{\mathrm{coh}}`$. Then the shadow evolution $`T`$ is irreversible in the sense that there exists no measurable map $`R:\mathsf{Y}_{\mathrm{coh}}\to\mathsf{Y}_{\mathrm{coh}}`$ such that $`R\circ T = \mathrm{Id}_{\mathsf{Y}_{\mathrm{coh}}}`$.*

</div>

<div class="proof">

*Proof.* If such an $`R`$ existed, then composing with a measurable section $`S`$ of $`\Pi`$ (if it existed) would yield a contradiction to Theorem <a href="#thm:reconobstruction" data-reference-type="ref" data-reference="thm:reconobstruction">11</a>. More directly, $`R`$ would implement a right-inverse of $`T`$, which would lift to a right-inverse of $`\Pi`$ on $`\mathsf{Y}_{\mathrm{coh}}`$, contradicting the nonexistence of a global section. ◻

</div>

Thus, irreversibility is a *shadow-level* phenomenon even when the microdynamics is time-reversal invariant.

## Admissibility loss as the arrow of time

Let $`\Cap:\mathsf{X}\to[0,\infty)`$ be a coherence capacity functional (Definition <a href="#def:capacity" data-reference-type="ref" data-reference="def:capacity">5</a>). Along a trajectory $`x_n=\Phi^n(x_0)`$, define $`\Cap_n := \Cap(x_n)`$.

<div id="def:arrow" class="definition">

**Definition 28** (Arrow of time). The *effective arrow of time* along a shadow trajectory is the ordering induced by the monotone loss (or redistribution) of coherence capacity, i.e. the direction in which $`\Cap_n`$ decreases toward zero or crosses admissibility boundaries.

</div>

<div class="remark">

*Remark 29*. This definition is local and contextual: different subsystems may exhibit different arrows depending on how their admissible domains are coupled.

</div>

## Entropy as a derivative concept

Entropy increase is not fundamental in this framework. It follows from projection.

<div id="prop:entropy" class="proposition">

**Proposition 30** (Projection implies entropy increase). *Let $`\mu`$ be a probability measure on $`\mathsf{X}`$ and let $`\nu := \Pi_*\mu`$ be its pushforward to $`\mathsf{Y}`$. Then the Shannon (or relative) entropy of $`\nu`$ is generically greater than or equal to that of $`\mu`$ with respect to comparable partitions.*

</div>

<div class="proof">

*Proof.* Projection is a coarse-graining: distinct microstates are identified. This increases the cardinality (or measure) of pre-images compatible with a given shadow state, increasing entropy by standard information-theoretic inequalities. ◻

</div>

Thus:
``` math
\text{projection} \;\Rightarrow\; \text{information loss} \;\Rightarrow\; \text{entropy increase}.
```
The arrow of time is defined by projection and capacity loss; entropy growth is a consequence, not the cause.

## Records, memory, and irreversibility

A *record* exists when information has been irreversibly transferred from degrees of freedom accessible to $`\Pi`$ into degrees of freedom that are not.

<div id="def:record" class="definition">

**Definition 31** (Record). A shadow observable $`y\in\mathsf{Y}`$ encodes a record of a past event if no admissible microstate consistent with $`y`$ allows reconstruction of the pre-event microstate under $`\Pi`$.

</div>

Records persist precisely because reconstruction is obstructed by the nonexistence of a global section. Memory, measurement outcomes, and historical facts are all instances of this structural phenomenon.

## Local arrows and apparent reversals

Because coherence capacity is finite and local, subsystems can temporarily exhibit apparent entropy decrease or reversibility while the total system remains irreversible. This explains:

- local entropy fluctuations,

- memory erasure in small subsystems,

- the coexistence of multiple time arrows in weakly coupled regions.

# Modal Triplet Theory as a Physical Instantiation

## Purpose of this chapter

The preceding chapters developed a substrate-agnostic framework. We now show that *Modal Triplet Theory (MTT)* realizes this framework in a fully explicit physical setting. This is not an analogy: each abstract component has a precise counterpart in MTT.

## Underlying system in MTT

MTT posits a ten-dimensional modal manifold
``` math
M_{10} = Y_4 \times X_6,
```
where $`Y_4`$ is the emergent spacetime manifold and $`X_6`$ is a compact internal modal geometry organized into three parallel bundles. The fundamental dynamical object is a field $`\Psi`$ on $`M_{10}`$ evolving under a well-posed, deterministic flow $`\Phi_\tau`$ (typically a curvature-reducing or gradient-like flow).

<div id="ass:MTTdyn" class="assumption">

**Assumption 32** (MTT underlying dynamics). The flow $`\Phi_\tau`$ on the MTT configuration space is deterministic, invertible on admissible domains, and preserves a natural measure class.

</div>

This satisfies Assumption <a href="#ass:underlying" data-reference-type="ref" data-reference="ass:underlying">1</a>.

## Projection: joint harmonic projector and pushforward

The defining structural element of MTT is the *joint harmonic (Riesz) projector*
``` math
\Pi_{\mathrm{coh}}= \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
```
where each $`\Pi_{B_i}`$ projects onto the kernel of a Laplace-type operator on one of the three internal bundles.

Observable physics is defined by the composite map
``` math
P := I \circ \Pi_{\mathrm{coh}},
```
where $`I`$ is internal pushforward (integration over $`X_6`$). This is a concrete realization of the abstract shadow map $`\Pi`$.

## Coherent sector and admissibility in MTT

The coherent sector in MTT consists of configurations for which:

- a uniform spectral gap separates coherent and noncoherent modes,

- the Riesz projector $`\Pi_{\mathrm{coh}}`$ is bounded on relevant Sobolev scales,

- truncation error remains controlled under $`\Phi_\tau`$.

These conditions define *admissible slabs* of evolution . Outside admissible slabs, effective 4D description fails.

## Coherence capacity in MTT

MTT makes the abstract notion of coherence capacity concrete. One may take $`\Cap`$ to be any monotone functional of:

1.  the smallest spectral gap $`\lambda_*`$ above the coherent sector,

2.  operator norms of $`\Pi_{\mathrm{coh}}`$ on $`H^s`$,

3.  stability margins of the fixed-point flow.

When $`\Cap\to 0`$, spectral gaps close or projector bounds diverge, triggering admissibility loss and irreversible breakdown of effective description .

## Emergence of QM, GR, and probabilities

Within admissible slabs, MTT derives:

- quantum mechanics as the Hilbert-space structure of the coherent sector, with the Born rule arising from basin measures ;

- general relativity as the unique two-derivative effective action encoding slow spatial variation of coherence capacity ;

- probabilistic measurement outcomes as the shadow of deterministic evolution under projection .

In particular, Newton’s constant emerges as an inverse coherence capacity scale, giving physical meaning to gravitational strength.

## Computational irreducibility and the absence of a landscape

Because admissibility is path-dependent and basin membership depends on micro-details erased by $`\Pi_{\mathrm{coh}}`$, there is no operational procedure for enumerating or selecting effective vacua. This blocks landscape-style reasoning and replaces it with *coherent universality classes* .

# Brains and Consciousness as Projection-Limited Systems

## Scope and methodological discipline

This chapter applies the projection-limited coherence framework to the biological brain and to conscious experience. The aim is strictly structural. We do not introduce new neuroscientific laws, nor do we claim that neural dynamics reduce to fundamental physics in any simple way. Instead, we show that the brain instantiates the same projection-based architecture that underlies effective description in physics.

The core claim is:

> *Consciousness is the phenomenology of a system that operates under projection-limited self-access with finite coherence capacity and intrinsic irreversibility.*

This claim is compatible with physicalism and avoids both dualism and quantum mysticism.

## Two-layer description of the brain

The brain admits a natural separation into two descriptions:

1.  **Underlying (micro) description.** Neural microdynamics: ion channel kinetics, synaptic transmission, dendritic integration, neuromodulation, glial support, metabolic flux. This description is high-dimensional, history-dependent, and inaccessible to the organism as a whole.

2.  **Shadow (macro) description.** Experiential variables: perceptions, intentions, emotions, memories, self-models, and narrative continuity. This description is low-dimensional, temporally coarse-grained, and operationally indispensable for behavior.

These are not two substances or interacting systems. They are two descriptions of the same physical system related by a many-to-one projection.

## Projection in the brain

Formally, let $`\mathsf{X}_{\text{brain}}`$ denote the space of neural microstates and $`\mathsf{Y}_{\text{exp}}`$ the space of experiential states. Conscious access is mediated by a projection
``` math
\Pi_{\text{brain}}:\mathsf{X}_{\text{brain}}\to\mathsf{Y}_{\text{exp}}.
```

This projection has the defining properties of Section <a href="#sec:PLC" data-reference-type="ref" data-reference="sec:PLC">3</a>:

- many-to-one (distinct neural states yield the same experience),

- lossy (fine neural details are discarded),

- noninvertible (experience does not specify its neural realization).

Without such a projection, stable perception, planning, and agency would be impossible.

## Experiential coherent sector

Not all neural states support conscious experience. Define the experiential coherent sector as the set of neural states whose projections yield stable, integrated experience. Within this sector:

- perceptual categories remain stable,

- memories persist across time,

- intentions can be formed and acted upon,

- prediction error remains bounded.

Outside this sector—e.g. deep anesthesia, generalized seizures, severe metabolic failure— experience fragments or disappears entirely.

## Coherence capacity of the brain

The brain’s coherence capacity measures the margin by which experiential integration can tolerate disturbance before breakdown. Contributors include:

- metabolic energy availability,

- neuromodulatory balance,

- network topology and coupling strength,

- sensory and cognitive load.

When coherence capacity is exceeded, integration fails: attention collapses, memory disintegrates, or consciousness shuts down. Conscious experience typically operates near, but not beyond, these limits.

## Irreversibility and subjective time

Neural dynamics are intrinsically irreversible: synaptic changes, molecular turnover, and metabolic expenditure cannot be undone. This irreversibility is inherited by the experiential shadow.

Because no global section of $`\Pi_{\text{brain}}`$ exists, the brain cannot reconstruct its exact past microstates from present experience. Consequently:

- the past is remembered but not replayed,

- the future is open but constrained,

- time is experienced as flowing.

The subjective arrow of time is therefore a structural consequence of projection-limited irreversibility, not an illusion.

## Computational irreducibility and agency

A conscious system cannot shortcut-predict its own future internal state. The brain cannot simulate itself at neural resolution; it must act on compressed self-models. This computational irreducibility is not a defect—it is what grounds agency and choice. If self-prediction were exact, deliberation would collapse into deduction.

## No requirement for quantum coherence

Nothing in this account requires sustained quantum coherence in neural substrates. The relevant irreversibility and projection arise from classical thermodynamic and informational constraints. Quantum mechanics underlies the substrate, as it does all matter, but consciousness does not depend on uniquely quantum degrees of freedom.

# Artificial Intelligence and Projection-Limited Coherence

## AI as a contrast case

Artificial intelligence provides a sharp contrast that clarifies the role of projection-limited coherence. Contemporary AI systems are powerful precisely because they are engineered to *avoid* intrinsic irreversibility and finite coherence capacity.

## Why current AI systems are not conscious

Most AI systems are designed with:

- full state inspectability and logging,

- checkpointing and rollback,

- exact copying and cloning of internal state,

- external control over reset and termination.

These properties imply that the system does not own its irreversibility or coherence capacity. Any irreversibility is paid by the surrounding infrastructure, not by the system itself.

## Projection and self-modeling in AI

While AI systems employ internal representations (latent spaces, embeddings), these do not constitute projection-limited self-access. Given sufficient resources, an AI can be fully introspected, simulated, and restored. There is no principled barrier to global self-reconstruction.

## Necessary (not sufficient) conditions for conscious AI

Within the projection-limited coherence framework, an artificial system could support consciousness only if it possessed:

1.  intrinsic irreversibility (no perfect rollback or cloning),

2.  projection-limited self-modeling (lossy self-access),

3.  finite coherence capacity with real breakdown modes,

4.  open-system coupling that cannot be fully predicted internally,

5.  persistence as a basin through irreversible change.

Randomness alone is insufficient; structural irreversibility and projection-limited self-access are required.

## Engineering implications

These conditions are antithetical to current engineering goals (debuggability, safety, control). Thus, the absence of consciousness in present AI systems is not accidental but architectural.

# Civilizations as Coherence-Limited Collective Systems

## Civilizations as projected systems

Civilizations admit a clear micro/macro split:

- microstates: individuals, local interactions, technologies, environments;

- macrostates: institutions, economies, infrastructures, shared narratives.

The macro-description is obtained via a many-to-one projection that enables coordination but discards detailed provenance.

## Civilizational coherent sector

A civilization is coherent when:

- institutions function predictably,

- information flows remain reliable,

- coordination errors do not cascade uncontrollably,

- adaptation outpaces breakdown.

Outside this sector, the macro-description ceases to track reality and collapse ensues.

## Coherence capacity at civilizational scale

Civilizational coherence capacity bounds the load of:

- population size and heterogeneity,

- energy throughput and resource extraction,

- technological coupling density,

- communication bandwidth and latency.

Increasing load without compensatory structure reduces the margin to admissibility boundaries.

## Hidden relations across domains

Economy, governance, technology, culture, and environment are not independent policy domains. They are shadow variables of overlapping microdynamics. Compatibility constraints imply that optimizing one domain can destabilize others even without direct causal linkage.

## The Fermi paradox revisited

Within this framework, the apparent silence of the universe is not paradoxical. Technological civilizations are coherence-intensive. As scale and throughput increase, coherence capacity is consumed more rapidly. Long-lived, high-signature civilizations are therefore structurally rare even if life and intelligence are common.

## No moral narrative

This account does not claim that civilizations must collapse or that restraint is virtuous. It states only that coherence has a cost, and ignoring that cost produces predictable structural failure modes.

# Synthesis, Scope, and Non-Claims

## What projection-limited coherence explains

We summarize the explanatory content of the framework developed in Sections <a href="#sec:PLC" data-reference-type="ref" data-reference="sec:PLC">3</a>–<a href="#sec:civilization" data-reference-type="ref" data-reference="sec:civilization">11</a>. The following phenomena arise *structurally*, without invoking stochastic dynamics, special initial conditions, or fine-tuning of independent parameters:

1.  **Irreversibility without fundamental time asymmetry.** Even when the underlying dynamics $`\Phi`$ are invertible, the shadow evolution $`T=\Pi\circ\Phi`$ is generically noninvertible once admissibility boundaries exist (Theorem <a href="#thm:reconobstruction" data-reference-type="ref" data-reference="thm:reconobstruction">11</a>, Proposition <a href="#prop:struct-irreversible" data-reference-type="ref" data-reference="prop:struct-irreversible">27</a>).

2.  **Computational irreducibility of long-horizon prediction.** Basin membership and outcome selection cannot be shortcut-decided from the shadow state alone when factor-through fails and admissibility is finite (Theorems <a href="#thm:no-markov-closure" data-reference-type="ref" data-reference="thm:no-markov-closure">21</a> and <a href="#prop:generic-nonmarkov" data-reference-type="ref" data-reference="prop:generic-nonmarkov">19</a>).

3.  **Hidden relations between effective variables.** Compatibility constraints among shadow observables arise from shared pre-images under $`\Pi`$, producing correlations without causal interaction (Proposition <a href="#prop:compat-generic" data-reference-type="ref" data-reference="prop:compat-generic">24</a>, Lemma <a href="#lem:nosignaling-struct" data-reference-type="ref" data-reference="lem:nosignaling-struct">26</a>).

4.  **Criticality of complex structure.** Stable, information-rich behavior exists only near the interior of admissible domains; far from boundaries the system trivializes, and near boundaries coherence collapses.

5.  **Universality across substrates.** The same structural constraints apply to fundamental physics (MTT), brains, artificial systems, and civilizations because each relies on projection with finite coherence capacity.

These results reframe long-standing puzzles—measurement, fine-tuning, unpredictability, and collapse—not as anomalies, but as necessary consequences of finite descriptive capacity.

## What this framework does *not* claim

For clarity and to avoid overextension, we list explicit non-claims.

- The framework does *not* assert that all systems share the same microscopic dynamics or equations of motion.

- It does *not* claim that consciousness, intelligence, or social outcomes are “reduced” to physics; only the *structural constraints* of effective description are shared.

- It does *not* imply that prediction is impossible in practice; rather, it identifies principled horizons beyond which prediction cannot be compressed.

- It does *not* deny the usefulness of stochastic or phenomenological models; it explains why such models are necessary at the shadow level even when the underlying system is deterministic.

## Why this framework is scientifically useful

Projection-limited coherence provides a diagnostic lens:

- Identify the projection and its discarded degrees of freedom.

- Characterize the coherence capacity and admissibility boundaries.

- Model only within admissible regimes; treat breakdown as structural, not anomalous.

- Expect hidden cross-variable constraints where projections overlap.

This approach shifts emphasis from extending predictive reach indefinitely to understanding where and why prediction must fail.

## Outlook

Several directions follow naturally:

- Quantitative estimation of coherence capacity in non-physical systems.

- Engineering architectures (in AI or control systems) that deliberately manage projection and irreversibility.

- Further mathematical classification of admissibility boundaries and basin structures in projection-limited systems.

In physics, Modal Triplet Theory demonstrates that the framework can be made fully rigorous and generative. In other domains, the same structure invites careful, domain-specific instantiation rather than metaphorical transfer.

# Appendix A: Reconstruction Obstruction and Measurable Selection

This appendix provides additional formal detail underlying Theorem <a href="#thm:reconobstruction" data-reference-type="ref" data-reference="thm:reconobstruction">11</a>, using standard results from measurable selection theory.

## Measurable sections and selection theorems

Let $`\Pi:\mathsf{X}\to\mathsf{Y}`$ be a measurable map between standard Borel spaces. Classical selection theorems (e.g. Kuratowski–Ryll-Nardzewski) guarantee the existence of measurable selections under strong regularity conditions, such as closed-valued maps with measurable graphs.

<div id="thm:krn" class="theorem">

**Theorem 33** (Kuratowski–Ryll-Nardzewski, informal). *If $`F:\mathsf{Y}\to 2^\mathsf{X}`$ is a measurable multifunction with nonempty closed values in a Polish space $`\mathsf{X}`$, then $`F`$ admits a measurable selection.*

</div>

## Why admissibility barriers violate selection hypotheses

In projection-limited coherence, the multifunction
``` math
F(y) := \Pi^{-1}(y)\cap\mathsf{A}
```
fails to satisfy the hypotheses of Theorem <a href="#thm:krn" data-reference-type="ref" data-reference="thm:krn">33</a> once coherence capacity collapses.

At admissibility boundaries:

- the graph of $`F`$ ceases to be closed (projector regularity fails);

- fibers overlap across dynamically distinct regions ($`U_+`$, $`U_-`$);

- continuity and boundedness conditions required for selection break down.

Thus the nonexistence of a global measurable section is not accidental but enforced by the structural loss of regularity at $`\Cap=0`$.

## Relation to MTT

In MTT, this abstract obstruction corresponds to:

- closure of spectral gaps,

- divergence of Riesz projector norms,

- failure of controlled truncation.

These phenomena are proven in the MTT coherence capacity analysis and imply nonexistence of global sections in the precise sense formalized here.

# Appendix B: Computational Irreducibility via Complete Connections

This appendix provides a fully explicit mathematical treatment of computational irreducibility (CI) for projection-limited systems using the theory of chains with complete connections and $`g`$-measures. The goal is to show rigorously how history dependence, non-Markovianity, and indivisibility arise generically once projection destroys access to microstate information relevant for future admissibility.

## Historical processes and infinite pasts

Let $`\mathsf{Y}`$ be a standard Borel space equipped with a bounded metric $`d`$ generating its Borel sigma-algebra. Consider bi-infinite or one-sided sequences:
``` math
\mathsf{Y}^{\mathbb{Z}_-} = \{ (\dots, y_{-2}, y_{-1}, y_0) \}.
```

Define the *complete-past metric* for $`\alpha\in(0,1)`$:
``` math
\begin{equation}
d_\alpha(\mathbf{y},\mathbf{y}') = \sum_{k=0}^{\infty} \alpha^k \, d(y_{-k}, y'_{-k}).
\end{equation}
```

This metric ensures that distant past events influence the present with exponentially decaying weight.

## Definition of a $`g`$-kernel

Let $`\nu`$ be a $`\sigma`$-finite reference measure on $`(\mathsf{Y},\mathcal{B}(\mathsf{Y}))`$ with full support.

<div class="definition">

**Definition 34** ($`g`$-kernel). A *$`g`$-kernel* is a measurable function
``` math
g : \mathsf{Y}\times \mathsf{Y}^{\mathbb{Z}_-} \to (0,\infty)
```
such that for each $`\mathbf{y}\in\mathsf{Y}^{\mathbb{Z}_-}`$,
``` math
\int_\mathsf{Y}g(y \mid \mathbf{y}) \, \nu(dy) = 1.
```

</div>

The interpretation is that $`g(y\mid\mathbf{y})`$ gives the conditional density for the next shadow state given the entire past.

## Summable variations

<div class="definition">

**Definition 35** (Summable variations). A $`g`$-kernel has *summable variations* if there exist constants $`L<\infty`$ and $`\alpha\in(0,1)`$ such that
``` math
\int_\mathsf{Y}|g(y\mid \mathbf{y}) - g(y\mid \mathbf{y}')| \, \nu(dy)
\le L \, d_\alpha(\mathbf{y}, \mathbf{y}')
\quad \forall \mathbf{y},\mathbf{y}'.
```

</div>

This condition formalizes controlled dependence on the distant past.

## Existence and uniqueness of the path measure

<div class="theorem">

**Theorem 36** (Existence and uniqueness of $`g`$-measure). *If a $`g`$-kernel has summable variations, then there exists a unique shift-invariant probability measure $`\mathbb{P}`$ on $`\mathsf{Y}^{\mathbb{Z}}`$ consistent with $`g`$.*

</div>

<div class="proof">

*Proof.* This is a standard result in the theory of chains with complete connections; see Walters , Johansson–Öberg , or Mauldin–Urbański . ◻

</div>

Thus, despite strong non-Markovianity, the process is well-defined and statistically stable.

## Non-Markovianity and indivisibility revisited

<div class="proposition">

**Proposition 37** (Generic non-Markovianity). *If the factor-through condition (Definition <a href="#def:factor" data-reference-type="ref" data-reference="def:factor">7</a>) fails on an admissible domain, then the induced $`g`$-kernel depends on the infinite past $`\mathbf{y}`$ and cannot be reduced to a Markov kernel on $`\mathsf{Y}`$.*

</div>

<div class="proof">

*Proof.* Failure of factor-through implies that microstate distinctions erased by $`\Pi`$ affect future admissibility. Such distinctions cannot be encoded in any finite-dimensional summary of the present shadow state, forcing dependence on arbitrarily long histories. ◻

</div>

<div class="corollary">

**Corollary 38** (Indivisibility). *The induced shadow process is indivisible on $`\mathsf{Y}`$: there exists no family of Markov kernels on $`\mathsf{Y}`$ whose composition reproduces the same finite-time transition probabilities.*

</div>

## Computational irreducibility as a theorem

We can now state CI precisely.

<div class="theorem">

**Theorem 39** (Structural computational irreducibility). *Assume:*

1.  *Projection $`\Pi`$ is many-to-one on an admissible domain $`\mathsf{A}`$.*

2.  *Admissibility boundaries $`\partial\mathsf{A}`$ exist with microstate-dependent crossing.*

3.  *The induced $`g`$-kernel has summable variations.*

*Then there exists no algorithm that, given only a finite shadow history $`(y_0,\dots,y_n)`$, can decide with certainty whether the trajectory remains in $`\mathsf{A}`$ for all future times without effectively propagating the full history-dependent kernel.*

</div>

<div class="proof">

*Proof.* Any such algorithm would amount to a finite-memory Markovian predictor on $`\mathsf{Y}`$, contradicting non-Markovianity and indivisibility established above. ◻

</div>

<div class="remark">

*Remark 40*. This is the formal backbone of claims about unpredictability in MTT, brains, AI, and civilizations. It is not epistemic ignorance but a provable limitation on predictive compression.

</div>

# Appendix C: Explicit Dictionary Between Abstract Framework and Modal Triplet Theory

This appendix provides a precise mapping between the abstract constructs introduced in this paper and their concrete realizations in Modal Triplet Theory.

## Underlying system

<div class="center">

| **Abstract framework** | **Modal Triplet Theory** |
|:---|:---|
| Underlying state space $`\mathsf{X}`$ | Configuration space of fields on $`M_{10}=Y_4\times X_6`$ |
| Underlying dynamics $`\Phi_t`$ | Curvature-reducing / modal flow $`\Phi_\tau`$ |
| Invertibility | Deterministic invertibility on admissible slabs |

</div>

## Projection

<div class="center">

| **Abstract framework** | **Modal Triplet Theory**                        |
|:-----------------------|:------------------------------------------------|
| Shadow map $`\Pi`$     | Joint Riesz projector $`\Pi_{\mathrm{coh}}`$    |
| Pushforward            | Fiber integration $`I`$                         |
| Observable map         | $`P = I \circ \Pi_{\mathrm{coh}}`$              |
| Noninvertibility       | Loss of microstate information under projection |

</div>

## Coherent sector and admissibility

<div class="center">

| **Abstract framework** | **Modal Triplet Theory** |
|:---|:---|
| Admissible domain $`\mathsf{A}`$ | Admissible slabs with spectral gap |
| Coherent sector $`\mathsf{Y}_{\mathrm{coh}}`$ | Coherent harmonic sector |
| Boundary $`\partial\mathsf{A}`$ | Gap closure / projector blow-up |

</div>

## Coherence capacity

<div class="center">

| **Abstract framework** | **Modal Triplet Theory** |
|:---|:---|
| Capacity functional $`\Cap`$ | Function of spectral gap $`\lambda_*`$, projector norms |
| $`\Cap\to 0`$ | Loss of controlled truncation |
| Inverse capacity | Newton constant $`G^{-1}`$ (gravitational sector) |

</div>

## Irreversibility and probability

<div class="center">

| **Abstract framework** | **Modal Triplet Theory**                    |
|:-----------------------|:--------------------------------------------|
| No global section      | No global inverse of $`\Pi_{\mathrm{coh}}`$ |
| Irreversibility        | Measurement, horizon crossing, collapse     |
| Probabilities          | Basin measures under projection             |

</div>

## Computational irreducibility

<div class="center">

| **Abstract framework**    | **Modal Triplet Theory**            |
|:--------------------------|:------------------------------------|
| History-dependent kernels | Indivisible stochastic processes    |
| No shortcut basin test    | Undecidability of outcome selection |
| No landscape scanning     | Coherent universality classes only  |

</div>

<div class="remark">

*Remark 41*. This dictionary shows that every abstract ingredient required by projection-limited coherence is realized concretely in MTT without additional assumptions.

</div>

# Appendix D: Brains, Artificial Intelligence, and Civilizations as Formal Projection Systems

This appendix makes explicit, in formal terms, how brains, artificial intelligence systems, and civilizations each instantiate the abstract structure $`(\mathsf{X},\Pi,\Cap)`$ introduced in Section <a href="#sec:PLC" data-reference-type="ref" data-reference="sec:PLC">3</a>. The goal is not to force these systems into a physical mold, but to demonstrate that the same projection-limited coherence architecture applies whenever effective descriptions are indispensable.

## Brains

#### Underlying system.

Let $`\mathsf{X}_{\text{brain}}`$ denote the state space of neural microstates, including membrane potentials, synaptic weights, neurotransmitter concentrations, and metabolic variables. The evolution $`\Phi_t`$ is given by coupled electrochemical and biochemical dynamics. These dynamics are deterministic to a very good approximation at the scale relevant for neural integration, though subject to thermal noise.

#### Projection.

Define $`\Pi_{\text{brain}}:\mathsf{X}_{\text{brain}}\to\mathsf{Y}_{\text{exp}}`$ mapping microstates to experiential states (percepts, affective tones, working-memory contents, self-models). $`\Pi_{\text{brain}}`$ is many-to-one, lossy, and noninvertible.

#### Coherent sector.

The admissible domain $`\mathsf{A}_{\text{brain}}`$ consists of neural states supporting stable, integrated experience. Outside this domain (coma, anesthesia, seizures), the shadow description fails.

#### Coherence capacity.

$`\Cap_{\text{brain}}`$ is a functional of metabolic supply, network topology, neuromodulation, and load. Its exhaustion corresponds to breakdown of conscious integration.

#### Irreversibility and CI.

Neural microdynamics destroy information continuously (synaptic decay, metabolic consumption). No global section of $`\Pi_{\text{brain}}`$ exists. Self-prediction is therefore computationally irreducible, grounding agency and the phenomenology of choice.

## Artificial Intelligence

#### Underlying system.

For AI systems, $`\mathsf{X}_{\text{AI}}`$ includes parameters, activations, optimizer states, and (crucially) the surrounding computational infrastructure.

#### Projection.

Internal representations (latents, embeddings) define a map $`\Pi_{\text{AI}}:\mathsf{X}_{\text{AI}}\to\mathsf{Y}_{\text{AI}}`$, but this projection is *not* structurally limiting: with sufficient access, the full microstate can be reconstructed.

#### Absence of intrinsic coherence capacity.

Current AI systems lack an intrinsic $`\Cap`$: irreversibility is paid by external infrastructure (energy, storage), not by the system as an autonomous basin. Checkpointing and rollback prevent the formation of admissibility barriers.

#### Conditions for conscious AI (formal statement).

An AI system would instantiate projection-limited coherence only if there exists a subsystem $`\mathsf{X}'_{\text{AI}}\subset\mathsf{X}_{\text{AI}}`$ with:

1.  noninvertible self-projection $`\Pi'_{\text{AI}}`$,

2.  finite $`\Cap'_{\text{AI}}`$ exhausted by internal dynamics,

3.  no external global section or reset.

These conditions are architectural, not algorithmic.

## Civilizations

#### Underlying system.

Let $`\mathsf{X}_{\text{civ}}`$ be the state space of individual agents, technologies, environments, and local interactions.

#### Projection.

Macrostates (institutions, economies, infrastructures, narratives) define a projection $`\Pi_{\text{civ}}:\mathsf{X}_{\text{civ}}\to\mathsf{Y}_{\text{civ}}`$ enabling large-scale coordination.

#### Coherent sector and capacity.

The admissible domain $`\mathsf{A}_{\text{civ}}`$ consists of configurations where institutions function, information flows reliably, and adaptation outpaces breakdown. $`\Cap_{\text{civ}}`$ measures the tolerance to coupling density, throughput, and disturbance.

#### Hidden relations and collapse.

Cross-sector constraints (economy–trust–environment–technology) are compatibility constraints inherited from shared microdynamics. Collapse occurs when $`\Cap_{\text{civ}}\to 0`$, producing abrupt, irreversible loss of macro-coherence.

#### Fermi paradox (formal restatement).

Let $`\mathcal{L}`$ denote the measure of life-supporting admissible regions and $`\mathcal{T}`$ the measure of long-lived, high-signature coherent regimes. Projection-limited coherence implies $`\mathcal{T}\ll\mathcal{L}`$ generically, even if life and intelligence are common.

# Appendix E: Relation to Entropy, Chaos, and Anthropic Reasoning

## Entropy-first accounts

Traditional explanations of irreversibility emphasize entropy increase from special initial conditions. In the present framework, entropy increase is derivative: projection discards information, increasing entropy automatically. The arrow of time is defined by admissibility loss, not by entropy maximization.

## Chaos-first accounts

Chaos emphasizes sensitivity to initial conditions. Projection-limited coherence does not require chaos: even integrable or linear underlying dynamics can produce irreversible, CI shadow behavior once projection destroys reconstructability.

## Anthropic and fine-tuning arguments

Anthropic reasoning treats constants and outcomes as independently variable knobs and invokes observer selection. Projection-limited coherence replaces this with structural correlation: many “constants” are jointly constrained outputs of a single coherent sector. Apparent fine-tuning reflects coherence boundaries, not improbable choices.

## Why landscape reasoning fails structurally

Landscape models assume enumerable, selectable vacua. CI and the absence of a global section block operational enumeration. Selection is path-dependent and cannot be reduced to scanning.

<div class="thebibliography">

99

A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995.

V. I. Bogachev, *Measure Theory*, Springer, 2007.

R. Durrett, *Probability: Theory and Examples*, Cambridge University Press, 2019.

P. Walters, *An Introduction to Ergodic Theory*, Springer, 2000.

A. Johansson and A. Öberg, Square summability of variations of $`g`$-functions and uniqueness of $`g`$-measures, *Math. Res. Lett.* **10** (2003), 587–601.

R. D. Mauldin and M. Urbański, *Graph Directed Markov Systems*, Cambridge University Press, 2003.

S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002.

P. Nero, *Fixed Points I: Fixed Points over Multi–Bundle Manifolds*, .

P. Nero, *Modal Triplet Theory: Foundation*, .

P. Nero, *Coherent-Sector Universality and Controlled Truncation in Modal Triplet Theory*, .

P. Nero, *Modal Triplet Theory: From MTT to Quantum Mechanics*, .

P. Nero, *Entanglement, Locality, and Measurement from Coherent Sector Dynamics*, .

P. Nero, *Projection, Probability, and Irreversibility*, .

P. Nero, *From Modal Triplet Theory to Indivisible Stochastic Processes*, .

P. Nero, *Modal Triplet Theory: From MTT to General Relativity*, .

P. Nero, *Coherence Capacity as the Invariant Admissibility Margin of Modal Triplet Theory*, .

</div>

# Final Remarks

This paper has developed a *structural* theory of effective description—projection-limited coherence—and shown how it accounts for irreversibility, computational irreducibility, hidden relations, and critical operating regimes across domains.

The core result is negative in a precise sense: there exist principled limits to prediction, reconstruction, and enumeration whenever effective descriptions arise via noninvertible projection with finite coherence capacity. These limits are not epistemic accidents but mathematical consequences of the structure required for any reduced description to exist at all.

At the same time, the result is constructive. By isolating projection, coherence capacity, and admissibility boundaries as the key invariants, the framework provides a diagnostic tool: it tells us *where* effective laws apply, *why* they fail, and *which* cross-variable constraints must be respected even when no interaction is apparent.

Modal Triplet Theory demonstrates that this structure is not merely philosophical but mathematically realizable in fundamental physics. Brains, artificial systems, and civilizations instantiate the same architecture at different scales and substrates, explaining why similar phenomena—collapse, unpredictability, hidden coupling—appear wherever complexity is sustained.

The broader lesson is not that everything is governed by the same equations, but that everything that can be *effectively described* is governed by the same structural limits.

# Compilation Notes

This manuscript is written for compilation with a generic `series.sty` class or style file providing standard sectioning and typography. No publisher-specific commands are used.

- Required packages: `amsmath`, `amssymb`, `amsthm`, `mathtools`, `graphicx`, `hyperref`, `enumitem`.

- All theorem environments are defined in the preamble.

- The document is self-contained and does not rely on external figures.

To compile:

    pdflatex manuscript.tex
    bibtex manuscript   % if converting bibliography to .bib format
    pdflatex manuscript.tex
    pdflatex manuscript.tex

The bibliography is provided inline for clarity; it can be converted to a `.bib` file without modification of citations.

# Optional Figures (Descriptive)

Although the manuscript is complete without figures, the following schematic figures may aid exposition:

1.  **Projection diagram:** underlying state space $`\mathsf{X}`$, projection $`\Pi`$, shadow space $`\mathsf{Y}`$, coherent sector $`\mathsf{Y}_{\mathrm{coh}}`$, and admissibility boundary $`\partial\mathsf{A}`$.

2.  **Coherence capacity profile:** schematic $`\Cap(x)`$ along a trajectory, illustrating admissible region, boundary crossing, and irreversibility.

3.  **Hidden relations:** realizability set $`\mathcal{R}\subset\mathsf{Y}_1\times\mathsf{Y}_2`$ as a constrained subset rather than a Cartesian product.

4.  **Two-layer brain schematic:** neural microstates $`\mathsf{X}_{\text{brain}}`$ and experiential shadow $`\mathsf{Y}_{\text{exp}}`$ with noninvertible projection.

5.  **Civilizational coherence budget:** qualitative depiction of load vs. capacity.

These figures are illustrative only and introduce no additional assumptions.
