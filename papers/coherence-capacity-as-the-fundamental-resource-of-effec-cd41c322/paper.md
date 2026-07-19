---
abstract: |
  We identify a single structural resource underlying effective physical descriptions: a finite *coherence capacity*, defined as the stability margin that allows a projection-based description to remain predictive under disturbance. We consider a general class of theories in which observable physics arises via a noninvertible projection from a higher-dimensional configuration space with invertible dynamics. Under minimal axioms, we prove that exhaustion of coherence capacity necessarily induces noninvertibility of the effective evolution, forcing irreversibility in the observable description despite invertibility of the underlying dynamics. Measurement collapse, thermalization, and black hole information loss are shown to be instances of the same admissibility transition. We further show that spatial variation of coherence capacity induces a geometric response identical in form to Einstein gravity, with Newton’s constant emerging as a conversion factor between coherence capacity and curvature units. The framework is independent of any specific microscopic model; Modal Triplet Theory is cited only as a concrete realization of the axioms.
author:
- Peter Nero
current_version: v3
date: January 2026
generated_from_main_tex_sha256: a9645bdd5aa97068c0263d6ad23e16c10def6fe68b569c62d3d07cd85d2ea0f4
paper_id: coherence-capacity-as-the-fundamental-resource-of-effec-cd41c322
release_state: zenodo_released
released_version: v3.0
title: "**Coherence Capacity as the Fundamental Resource of Effective Physics**"
zenodo_doi: 10.5281/zenodo.18322036
zenodo_record_id: 18322036
zenodo_url: "https://zenodo.org/records/18322036"
---

# Introduction

Modern physics is built from effective descriptions: quantum mechanics, quantum field theory, and general relativity each apply only within domains where their assumptions remain valid. Outside those domains, familiar laws break down. Measurement yields irreversible outcomes, thermalization erases memory, and black holes appear to destroy information. These phenomena are usually treated as distinct puzzles.

In this work we argue that they share a single structural origin: the exhaustion of a finite *coherence capacity*, the margin that allows a projection-based effective description to remain stable.

We do not modify fundamental dynamics, introduce new degrees of freedom, or postulate stochastic collapse. Instead, we analyze the unavoidable consequences of describing physics via noninvertible projection from a higher-dimensional configuration space. Our results apply to any theory satisfying a small set of axioms stated explicitly below.

#### Scope.

This paper establishes *inevitability results*, not existence results. We do not prove that a theory satisfying the axioms exists; rather, we show what must follow if it does. Modal Triplet Theory provides one explicit realization, but no use is made of its specific constructions.

# Levels of Description

We distinguish three levels.

## Upstairs configuration space

Let $`(X,\mathcal{B})`$ be a standard measurable space representing the full configuration space of a physical system. We assume:

- A deterministic, invertible evolution $`\Phi : X \to X`$ (or a flow $`\Phi_t`$).

- No fundamental time parameter; $`\Phi`$ provides only an ordering of configurations.

## Projection and observables

Observable physics is defined via a measurable projection
``` math
P : X \to Y,
```
where $`Y`$ is the space of effective (observable) states. The projection is generally noninjective.

## Effective shadow

The induced observable evolution is
``` math
T := P \circ \Phi : X \to Y.
```
All effective laws (dynamics, geometry, probabilities) refer to this shadow level.

# Core Definitions

This section fixes the primitive objects used throughout the paper. All subsequent results depend only on these definitions and the axioms already stated.

## Coherence Capacity

<div class="definition">

**Definition 1** (Upstairs coherence capacity). Let $`x\in X`$. The upstairs coherence capacity $`\mathcal C_X(x)`$ is defined as the maximal disturbance amplitude for which the projection-based description remains stable in a neighborhood of $`x`$.

</div>

<div class="definition">

**Definition 2** (Effective coherence capacity). For $`y\in Y`$, define the effective coherence capacity
``` math
\mathcal C_Y(y) := \inf_{x\in P^{-1}(y)} \mathcal C_X(x).
```
When an effective spacetime description exists, we write $`\mathcal C(x^\mu)`$ for $`\mathcal C_Y(y(x^\mu))`$.

</div>

Thus coherence capacity is fundamentally defined on $`X`$ and pushed forward to the effective description. All statements of $`\mathcal C>0`$ refer to the effective capacity unless stated otherwise.

#### Capacity as a collected invariant.

Coherence capacity is not a primitive postulate of the framework. It is a unifying name for a collection of structural constraints that must hold simultaneously for a projection-based effective description to remain admissible. These include bounded projector regularity, spectral separation, finite truncation error, and dynamical stability margins. Any scalar functional that vanishes precisely when these constraints fail may serve as a capacity parameter. The results of this paper are therefore invariant under redefinitions of $`C`$ that preserve its zero set and positivity domain.

## Admissibility

<div class="definition">

**Definition 3** (Admissible region). A region $`A\subset X`$ is admissible if and only if:

- the projection $`P`$ is well-defined and regular on $`A`$,

- truncation or coarse-graining errors remain below fixed tolerance,

- the induced effective dynamics is contractive on $`P(A)`$.

</div>

Equivalently, admissibility holds precisely where $`\mathcal C_X(x)>0`$.

## Coherence Basins

<div class="definition">

**Definition 4** (Coherence basin). A coherence basin $`B_\alpha\subset Y`$ is a forward-invariant subset of effective state space such that there exists $`0<\lambda<1`$ with
``` math
\|T(y_1)-T(y_2)\|\le\lambda\|y_1-y_2\| \quad \forall y_1,y_2\in B_\alpha.
```

</div>

Coherence basins are stable regions of effective description; disturbances within a basin are damped rather than amplified.

# Axioms

We now state the axioms required for all subsequent results.

Axiom A1 (Invertible fundamental dynamics).  
The upstairs evolution $`\Phi`$ is invertible.

Axiom A2 (Noninjective projection).  
The observable map $`P`$ is noninjective on $`X`$.

Axiom A3 (Admissible domain).  
There exists a subset $`A \subset X`$ on which the projection-based description is stable and predictive. Outside $`A`$, the effective description ceases to be valid.

Axiom A4 (Finite stability margin).  
Stability of the effective description on $`A`$ is controlled by a finite margin that can be exhausted under disturbance.

No further structure is assumed.

#### Scope clarification.

This paper does not establish the existence of a physical theory satisfying Axioms A1–A4. Rather, it establishes structural consequences that follow if such a theory exists. No claim is made that coherence capacity is unique or fundamental in all possible formulations; the results apply to any projection-based effective description with finite stability margins.

# Coherence Capacity

## Definition

<div class="definition">

**Definition 5** (Coherence capacity). Let $`x \in A`$. The *coherence capacity* $`\mathcal{C}(x)`$ is a nonnegative scalar functional measuring the maximal disturbance amplitude that preserves validity of the effective description near $`x`$.

</div>

Operationally, $`\mathcal{C}(x) > 0`$ means the projection $`P`$ remains stable and predictive; $`\mathcal{C}(x) = 0`$ marks the boundary of admissibility.

#### Interpretive clarification.

Coherence capacity is not introduced here as a new dynamical field, degree of freedom, or fundamental scalar quantity. Writing $`C(x)`$ reflects the spatial dependence of the *admissibility margin* in regimes where an effective spacetime description exists and a derivative expansion is meaningful. The capacity field is therefore a descriptive encoding of how boundedness, spectral separation, and stability margins vary across an effective description, not an additional component of the microscopic dynamics.

## Basic properties

<div class="lemma">

**Lemma 6**. *$`\mathcal{C}(x) > 0`$ for all $`x \in A`$.*

</div>

<div class="lemma">

**Lemma 7**. *If $`x_n \to x`$ with $`x_n \in A`$ and $`x \notin A`$, then $`\mathcal{C}(x_n) \to 0`$.*

</div>

# Projection Noninvertibility Theorem

We now state the central result.

<div class="definition">

**Definition 8**. The shadow evolution $`T`$ is *globally invertible* if there exists a measurable map $`S : Y \to X`$ such that
``` math
T \circ S = \mathrm{Id}_Y.
```

</div>

<div class="theorem">

**Theorem 9** (Coherence Capacity Collapse Implies Shadow Noninvertibility). *Assume Axioms A1–A4. If a trajectory $`\{x, \Phi(x), \Phi^2(x), \dots\}`$ crosses a point where $`\mathcal{C}=0`$, then the induced shadow evolution $`T`$ admits no global measurable right inverse.*

</div>

<div class="proof">

*Proof.* At a point where $`\mathcal{C}=0`$, the projection $`P`$ identifies distinct configurations $`x_1 \neq x_2`$ in $`X`$ with the same image in $`Y`$, and stability of the effective description fails. Since $`\Phi`$ is invertible, $`\Phi(x_1)`$ and $`\Phi(x_2)`$ remain distinct. Any putative inverse $`S`$ would be required to select a unique preimage for identical shadow states, which is impossible on a set of nonzero measure. Hence no global right inverse exists. ◻

</div>

<div class="corollary">

**Corollary 10**. *Irreversibility in the effective description is unavoidable once coherence capacity is exhausted, even though the fundamental dynamics remains invertible.*

</div>

# Gravity as the Geometric Bookkeeping of Coherence Capacity

Within an admissible regime, the effective description admits a local four-dimensional geometric representation. The role of geometry in this framework is not to mediate forces, but to encode where and how a projection-based description remains stable.

The central observation is that coherence capacity may vary across the effective description. Such variation must be tracked consistently and locally. The only available structure capable of doing this—while preserving locality and diffeomorphism invariance—is geometry.

Accordingly, coherence capacity enters the effective action as a curvature stiffness. The minimal local, diffeomorphism-invariant action consistent with this interpretation is
``` math
S_{\mathrm{eff}} = \int \sqrt{-g}\,\frac{\mathcal C(x)}{16\pi} R
+ \mathcal L_m + \mathcal O(R^2).
```

Varying with respect to the metric yields
``` math
\mathcal C\,G_{\mu\nu}
+ (g_{\mu\nu}\Box - \nabla_\mu\nabla_\nu)\mathcal C
= 8\pi T_{\mu\nu} + \cdots.
```

This equation should not be read as introducing a new gravitational degree of freedom. Rather, it states that geometry is the bookkeeping device that tracks how much coherence capacity remains available to support a spacetime description. When $`\mathcal C`$ is constant, Einstein gravity is recovered with
``` math
G_{\mathrm{eff}} = \frac{1}{\mathcal C}.
```

Gravity is therefore not fundamental interaction but the structural response of the effective description to capacity gradients. This statement concerns the effective description only and does not assert that microscopic gravitational dynamics are generated by capacity.

# Emergence of Time and the Arrow of Irreversibility

The upstairs dynamics admits no fundamental time parameter. It provides only an ordering of configurations. The notion of time arises only at the level of effective description, where successive admissible projections can be parametrized.

Within a single admissible basin, projection remains invertible and the effective evolution may be reversed. In this regime, time behaves as a coordinate parametrizing reversible ordering.

Irreversibility enters only at admissibility barriers. When coherence capacity collapses ($`\mathcal C \to 0`$), the effective description must be reset to a new admissible basin. The shadow evolution becomes noninvertible, and no effective inverse exists.

<div class="definition">

**Definition 11** (Arrow of time). The arrow of time is defined as the ordering induced by the sequence of coherence capacity exhaustion events.

</div>

This arrow is structural, not statistical. It does not require entropy maximization or probabilistic assumptions. Entropy increase is a consequence of capacity loss, not its cause.

# Measurement, Black Holes, and Thermalization as a Single Mechanism

We now show that three traditionally distinct phenomena—measurement collapse, black hole information loss, and thermalization—are instances of the same structural transition.

## Measurement

Measurement introduces additional constraints on admissibility by coupling the system to an apparatus. This coupling reduces coherence capacity locally. When $`\mathcal C \to 0`$, projection becomes noninvertible and the system is forced into a new admissible basin. This is what is observed as collapse.

## Black holes

In gravitational settings, inward capacity flux may exceed outward redistribution. When this occurs, coherence capacity collapses on a codimension-one surface. The resulting bottleneck is a horizon. Exterior observers cannot invert the effective evolution across it.

## Thermalization

In high-capacity regimes, basins mix and memory is erased. In low-capacity or fragmented regimes, memory persists. Thermalization is therefore not a universal tendency but a capacity-dependent phenomenon.

All three cases correspond to the same event: exhaustion of coherence capacity forcing projection noninvertibility.

# Simulability and the Necessity of Undecidability

If capacity exhaustion events were decidable in advance, effective evolution would require global foresight over exponentially many counterfactual futures. This would render physical evolution computationally inconsistent.

The undecidability of capacity exhaustion localizes irreducibility to the boundary itself. The system evolves deterministically until admissibility fails, at which point projection enforces selection.

This guarantees that physical evolution remains simulable in real time by itself. Undecidability is therefore not a defect but a consistency requirement.

# Relation to Modal Triplet Theory

Modal Triplet Theory provides an explicit realization of the axioms used here, with coherence capacity constructed from spectral gaps, projector regularity, and dynamical margins. The present analysis does not rely on those constructions and applies to any projection-based effective theory with finite stability margins.

The capacity framework may therefore be viewed either as a reparameterized description of the MTT admissibility structure or as a reparameterization of the same admissibility structure expressed in different descriptive variables.

# Conclusion

We have shown that coherence capacity is the fundamental resource governing effective physical descriptions. Its conservation within admissible regimes and exhaustion at boundaries unify gravity, time, measurement, thermalization, and information loss as structural necessities.

Effective laws persist precisely because coherence capacity is finite. Their breakdown is not a failure of fundamental dynamics, but the price paid for stability, locality, and predictability.
