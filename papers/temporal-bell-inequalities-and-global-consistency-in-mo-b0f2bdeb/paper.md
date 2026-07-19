---
abstract: |
  We give a proof-forward account of temporal Bell inequalities (Leggett–Garg) in Modal Triplet Theory (MTT). We show: (i) any temporally factorized realist model satisfies the Leggett–Garg bound; (ii) MTT generically violates temporal factorization because coherent histories are globally constrained by the coherence projector and fixed-point selection; (iii) nevertheless, operational no-retro-signaling holds (later measurement choices do not change earlier observable marginals); and (iv) therefore MTT reproduces the standard quantum Leggett–Garg violations without retrocausal signaling and without abandoning realism of the underlying modal configuration. Spatial Bell nonlocality and temporal Bell violations are identified as two projections of the same global-consistency mechanism.
author:
- Peter Nero
current_version: v1.0
date: January 2026
generated_from_main_tex_sha256: fbf9cb11f14918c433eb9a8ea778e4e27ff908ab7e99d3002bf9dbddd06f12ea
paper_id: temporal-bell-inequalities-and-global-consistency-in-mo-b0f2bdeb
release_state: zenodo_released
released_version: v1.0
title: Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.18208885
zenodo_record_id: 18208885
zenodo_url: "https://zenodo.org/records/18208885"
---

# Introduction

Temporal Bell inequalities test whether a single system can admit a time-local realist description. Leggett–Garg inequalities constrain correlations of a dichotomic observable measured at different times. Quantum mechanics violates these inequalities. We show that MTT predicts the same violations for the same structural reason as in spatial Bell: failure of factorization due to global constraints, while preserving operational causality.

# Leggett–Garg setup and temporal factorization

## Measurement schedule and correlations

Fix times $`t_1 < t_2 < t_3`$. Let $`Q_k \in \{+1,-1\}`$ denote the outcome of measuring a dichotomic observable at time $`t_k`$. Denote two-time correlators
``` math
C_{ij} := \mathbb{E}[Q_i Q_j], \qquad 1 \le i < j \le 3.
```
The (three-time) Leggett–Garg combination is
``` math
\begin{equation}
K := C_{12} + C_{23} - C_{13}.
\label{eq:LGI}
\end{equation}
```

## Assumptions behind the LGI

We separate what is tested by Leggett–Garg from what is observed in practice.

<div class="definition">

**Definition 1** (Temporal factorization model). A temporal factorization (TF) model for $`(Q_1,Q_2,Q_3)`$ consists of a probability space $`(\Omega,\mathcal{F},\mathbb{P})`$ with a hidden variable $`\lambda : \Omega \to \Lambda`$ and conditional response functions $`q_k : \Lambda \to \{\pm 1\}`$ such that
``` math
\begin{equation}
Q_k = q_k(\lambda) \quad \text{a.s.},
\label{eq:TFresp}
\end{equation}
```
and the joint distribution satisfies
``` math
\begin{equation}
\mathbb{P}(Q_1 = a, Q_2 = b, Q_3 = c)
= \int_\Lambda \rho(\lambda)
\mathbf{1}\{q_1(\lambda)=a\}
\mathbf{1}\{q_2(\lambda)=b\}
\mathbf{1}\{q_3(\lambda)=c\}
\,d\lambda.
\label{eq:TFjoint}
\end{equation}
```
Equivalently, conditional on $`\lambda`$, the outcomes are jointly deterministic and time-local.

</div>

<div class="remark">

*Remark 1*. Definition 1 abstracts the macrorealism+noninvasiveness assumptions in the form used for Bell-type derivations: a single underlying variable fixes all outcomes at all times. This is stronger than needed for many experimental protocols, but it is the standard form in which LGI bounds are derived and compared to quantum predictions.

</div>

# The Leggett–Garg inequality: factorization implies the bound

<div class="theorem">

**Theorem 1** (LGI under temporal factorization). *If $`(Q_1,Q_2,Q_3)`$ admit a temporal factorization model, then
``` math
K \le 1.
```*

</div>

<div class="proof">

*Proof.* Under temporal factorization, for each $`\lambda`$ define $`q_k = q_k(\lambda) \in \{\pm 1\}`$. Then
``` math
K(\lambda) := q_1 q_2 + q_2 q_3 - q_1 q_3
= q_2(q_1 + q_3) - q_1 q_3.
```
Since $`q_1,q_3 \in \{\pm 1\}`$, either $`q_1 = q_3`$ or $`q_1 = -q_3`$.

If $`q_1 = q_3`$, then $`q_1 + q_3 = \pm 2`$ and $`q_1 q_3 = 1`$, so
``` math
K(\lambda) = q_2(\pm 2) - 1 \in \{+1,-3\} \le 1.
```
If $`q_1 = -q_3`$, then $`q_1 + q_3 = 0`$ and $`q_1 q_3 = -1`$, so
``` math
K(\lambda) = 0 - (-1) = 1.
```
Hence for all $`\lambda`$, $`K(\lambda) \le 1`$. Taking expectation yields $`K = \mathbb{E}[K(\lambda)] \le 1`$. ◻

</div>

<div class="corollary">

**Corollary 1**. *If an experiment yields $`K > 1`$, then no temporal factorization model can reproduce the observed temporal correlations.*

</div>

# Global Consistency and Coherent Histories in MTT

Modal Triplet Theory does not define physical evolution as a purely initial-value problem. Instead, admissible physical histories are selected by global coherence constraints acting on entire spacetime trajectories. The fundamental object is a coherent modal configuration satisfying the coherence projector $`\Pi_{\mathrm{coh}}`$ and the Fundamental Contractivity Condition (FCC).

The effective notion of a “state at time $`t`$” arises only after projection onto a lower-dimensional description. Intermediate-time states are therefore contextual and need not be independent of later measurement conditions.

## New: Boundary-value interpretation (intuition)

A useful physical analogy is that of a vibrating string. The normal modes of a guitar string are not determined by initial displacement alone, but by boundary conditions imposed at both ends (the bridge and the nut). The string does not “know the future”; it simply satisfies a global boundary-value constraint.

In the same sense, a modal trajectory in MTT is defined by admissibility conditions imposed over its full temporal extent. The appearance that later measurements influence earlier properties arises from describing a globally constrained solution using time-local slices, not from retrocausal signaling.

## New: Probability space of coherent histories

We now make explicit the probabilistic structure implicit in the preceding discussion.

<div class="definition">

**Definition 2** (History probability space). Let $`\Omega`$ denote the set of globally admissible coherent histories on a time interval $`I=[t_1,t_3]`$ for a fixed experimental arrangement. Let $`\mathcal{F}`$ be the $`\sigma`$-algebra generated by cylinder sets corresponding to pointer records in localized spacetime regions. Let $`\mathbb{P}`$ be the probability measure induced by conditioning the coherent-sector fixed-point ensemble on the experimental setup.

</div>

Measurement choices correspond to conditioning $`\mathbb{P}`$ on sub-$`\sigma`$-algebras of $`\mathcal{F}`$. Time-slice probabilities are obtained by marginalization and conditional expectation with respect to $`\mathbb{P}`$. Because admissible histories are selected globally, these time-slice distributions need not factorize across time.

# Operational Causality and No-Retro-Signaling

The violation of temporal Bell inequalities is often taken to suggest retrocausal influence. We now show that this conclusion is unwarranted in MTT. Although intermediate-time descriptions are contextual, MTT preserves operational causality: later measurement choices do not alter earlier observable marginals.

<div class="definition">

**Definition 3** (No-retro-signaling). A theory satisfies no-retro-signaling if the marginal probability distribution of outcomes at time $`t_i`$ is independent of measurement choices made at later times.

</div>

## New: Formal statement and proof

<div class="lemma">

**Lemma 1** (No-retro-signaling in Modal Triplet Theory). *Modal Triplet Theory satisfies no-retro-signaling.*

</div>

<div class="proof">

*Proof.* Let $`M_2`$ denote the choice of measurement performed at time $`t_2`$, including the choice to perform no measurement. In the history probability space $`(\Omega,\mathcal{F},\mathbb{P})`$, conditioning on $`M_2`$ corresponds to restricting $`\mathbb{P}`$ to a sub-$`\sigma`$-algebra $`\mathcal{F}_{\le t_2}`$ that encodes the experimental arrangement.

Pointer records at time $`t_1`$ are elements of a sub-$`\sigma`$-algebra $`\mathcal{F}_{t_1}\subset \mathcal{F}_{\le t_2}`$. Because the underlying dynamics on the spacetime base is retarded and measurement couplings are localized, the marginal distribution on $`\mathcal{F}_{t_1}`$ is independent of which sub-$`\sigma`$-algebra $`\mathcal{F}_{\le t_2}`$ is conditioned upon.

Thus, for all measurement choices $`M_2`$ and $`M_2'`$,
``` math
\mathbb{P}(Q_1=+1\mid M_2)
=
\mathbb{P}(Q_1=+1\mid M_2').
```
An identical argument applies to $`Q_2`$ with respect to choices made at $`t_3`$. Hence no-retro-signaling holds. ◻

</div>

<div class="remark">

*Remark 2*. The above lemma is the temporal analogue of the no-signaling condition in spatial Bell experiments. In both cases, global conditioning may alter joint or conditional correlations while leaving individual marginals invariant.

</div>

# Failure of Temporal Factorization

We now identify the precise assumption violated by MTT in temporal Bell experiments. The failure is not operational causality, but temporal factorization: the assumption that outcomes at different times can be assigned independently of later measurement context.

In MTT, coherent histories are selected globally. Conditioning on measurement outcomes at later times refines the admissible set of histories and therefore alters the effective description of earlier segments. This refinement does not correspond to a signal or influence propagating backward in time; it reflects the non-factorizability of globally constrained solutions when described using time-local variables.

## New: Formal statement of temporal contextuality

<div class="proposition">

**Proposition 1** (Temporal contextuality in MTT). *In Modal Triplet Theory, temporal factorization generally fails. That is, there do not exist functions $`q_k(\lambda)`$ such that
``` math
Q(t_k)=q_k(\lambda)
```
for all $`k`$ and all admissible histories, with a joint distribution of the form
``` math
\mathbb{P}(Q_1,Q_2,Q_3)
=
\int_\Lambda \rho(\lambda)
\prod_{k=1}^3
\mathbf{1}\{q_k(\lambda)=Q_k\}\,d\lambda.
```*

</div>

<div class="proof">

*Proof.* Let $`\Omega`$ denote the set of globally admissible coherent histories under a fixed experimental arrangement. Changing whether a measurement is performed at time $`t_2`$, or altering its coupling, changes the boundary conditions defining admissibility and therefore changes the conditional measure on $`\Omega`$.

Because the admissible history ensemble itself depends on later measurement context, there is in general no single hidden variable $`\lambda`$ whose value fixes outcomes at all times independently of that context. Hence temporal factorization fails. ◻

</div>

## Connection to Leggett–Garg violation

By Theorem 1, temporal factorization implies the Leggett–Garg bound $`K\le 1`$. By Proposition 1, temporal factorization fails in MTT. Therefore, MTT permits violations of the Leggett–Garg inequality while preserving no-retro-signaling.

# Explicit Leggett–Garg Violations

To make the discussion concrete, we now exhibit explicit temporal correlations that violate the Leggett–Garg bound. These correlations are standard in quantum mechanics and are reproduced by MTT whenever the coherent-sector projection matches the quantum boundary dictionary.

## Standard quantum benchmark

Consider a two-level system with Hamiltonian
``` math
H = \frac{\hbar \omega}{2}\,\sigma_x,
```
and a dichotomic observable
``` math
Q = \sigma_z.
```
Let measurements be performed at times $`t_1<t_2<t_3`$, with ideal projective readout at each time.

Quantum mechanics predicts the two-time correlators
``` math
C_{ij} = \langle \sigma_z(t_i)\sigma_z(t_j)\rangle
       = \cos\bigl(\omega (t_j-t_i)\bigr).
```

## Violation of the LGI

Choose equal time separations
``` math
\Delta := t_2-t_1 = t_3-t_2,
\qquad
t_3-t_1 = 2\Delta.
```
Then the Leggett–Garg combination becomes
``` math
K = 2\cos(\omega\Delta) - \cos(2\omega\Delta)
  = 1 + 2\cos(\omega\Delta)\bigl(1-\cos(\omega\Delta)\bigr).
```

For $`0 < \cos(\omega\Delta) < 1`$, one has $`K>1`$. For example, taking $`\omega\Delta=\pi/3`$ yields $`\cos(\omega\Delta)=1/2`$ and
``` math
K = \frac{3}{2} > 1.
```

Thus the Leggett–Garg inequality is violated.

## Interpretation within MTT

Within MTT, this violation reflects the failure of temporal factorization under global coherence constraints. The underlying modal configuration is realist, but the effective time-local description cannot assign independent values to $`Q(t_1),Q(t_2),Q(t_3)`$ without reference to the full measurement context.

# Interpretation: Apparent Retrocausality as Projection

Temporal Bell violations are often described using the language of retrocausality: later measurements appear to influence earlier properties. In MTT this appearance is a projection artifact.

The fundamental object is a globally coherent history selected by admissibility and stability constraints. Conditioning on later measurement outcomes refines the admissible set of histories and thereby alters the effective description of earlier segments. No signal propagates backward in time, and no causal paradox arises.

## New: Jarrett-in-Time Decomposition

We now make precise which assumptions fail and which are preserved in temporal Bell violations, following the logic of Jarrett’s decomposition in the spatial Bell case.

<div class="definition">

**Definition 4** (Temporal Parameter and Outcome Independence). Temporal Parameter Independence (TPI) holds if the marginal distribution of outcomes at time $`t_i`$ is independent of measurement choices made at later times. Temporal Outcome Independence (TOI) holds if, conditioned on the hidden variable $`\lambda`$, the joint outcomes factorize:
``` math
\mathbb{P}(Q_i,Q_j\mid \lambda)
=
\mathbb{P}(Q_i\mid \lambda)\,
\mathbb{P}(Q_j\mid \lambda),
\qquad i<j.
```

</div>

<div class="proposition">

**Proposition 2** (Jarrett-in-time structure of MTT). *Modal Triplet Theory satisfies Temporal Parameter Independence but violates Temporal Outcome Independence.*

</div>

<div class="proof">

*Proof.* Temporal Parameter Independence is equivalent to no-retro-signaling, which holds by Lemma 2. Temporal Outcome Independence fails because intermediate outcomes depend on the global boundary conditions defining the admissible coherent history. Thus factorization conditioned on a single hidden variable $`\lambda`$ is not possible. ◻

</div>

<div class="remark">

*Remark 3*. This decomposition mirrors the spatial Bell case: MTT preserves the analogue of no-signaling while violating outcome independence due to global constraints, not due to nonlocal or retrocausal dynamics.

</div>

# Relation to Spatial Bell Nonlocality

Violations of Bell inequalities in spatially separated systems are now well understood as ruling out local hidden-variable models based on statistical factorization, while preserving no-signaling. Temporal Bell violations present an analogous challenge in the time domain.

In Modal Triplet Theory, these two phenomena share a common origin. Both arise from the projection of a globally constrained coherent configuration onto a reduced description. Spatial separation and temporal separation are treated symmetrically at the level of global admissibility.

## New: Formal unification

<div class="proposition">

**Proposition 3** (Spatial–temporal Bell unification). *Spatial Bell violations and temporal Bell violations arise from the same structural failure of factorization under global consistency constraints. In both cases, operational causality is preserved while outcome independence fails.*

</div>

<div class="proof">

*Proof.* In the spatial case, no-superluminal-signaling holds while factorization $`P(A,B\mid a,b,\lambda)=P(A\mid a,\lambda)P(B\mid b,\lambda)`$ fails due to global coherence constraints. In the temporal case, no-retro- signaling holds while temporal factorization fails for the same reason. Both are projections of a single globally admissible configuration. ◻

</div>

<div class="remark">

*Remark 4*. The distinction between “space” and “time” is therefore secondary to the underlying global-consistency structure. Nonlocal correlations in space and contextual correlations in time are dual manifestations of the same mechanism.

</div>

# Conclusions

We have shown that temporal Bell violations (Leggett–Garg violations) arise naturally in Modal Triplet Theory as a consequence of global consistency. The failure of temporal factorization does not signal retrocausal dynamics or a breakdown of realism, but reflects the inadequacy of describing globally constrained coherent histories using time-local hidden variables.

MTT preserves operational causality: later measurement choices do not alter earlier observable marginals. Temporal contextuality arises because conditioning on later boundary conditions refines the set of admissible histories. This mechanism is precisely analogous to the origin of spatial Bell nonlocality in MTT.

Taken together with previous results on measurement and spatial Bell violations, the present work completes the foundations triad of Modal Triplet Theory: space, process, and time are unified as projections of a single global-consistency structure.

# Temporal CHSH and Network Generalizations

The Leggett–Garg inequality is the simplest temporal Bell inequality, involving three measurement times. More general temporal inequalities can be constructed in direct analogy with the CHSH inequality and with network Bell inequalities.

Consider four measurement times $`t_1<t_2<t_3<t_4`$ and dichotomic observables $`Q(t_i)\in\{\pm1\}`$. Under temporal factorization, the CHSH-type combination
``` math
S := C_{12}+C_{23}+C_{34}-C_{14}
```
satisfies the bound $`|S|\le 2`$.

As in the three-time case, any model admitting a temporally factorized hidden-variable description obeys this bound. Whenever the coherent- sector projection in MTT reproduces standard quantum correlators, these bounds are generically violated for suitable choices of time separations.

More generally, one may consider temporal networks in which measurement choices and outcomes are arranged in directed acyclic graphs with time ordering. In all such cases, temporal factorization implies a family of linear inequalities analogous to spatial Bell network inequalities. Modal Triplet Theory generically violates these inequalities while preserving no-retro-signaling, by the same global-consistency mechanism identified in the main text.

<div class="remark">

*Remark 5*. The temporal CHSH and network generalizations introduce no new physical assumptions beyond those already required for the Leggett–Garg case. They further illustrate that temporal nonclassicality in MTT is not an isolated phenomenon but a structural consequence of global coherence.

</div>

<div class="thebibliography">

99 ...

</div>

<div class="thebibliography">

99

J. S. Bell, “On the Einstein Podolsky Rosen Paradox,” *Physics* **1**, 195–200 (1964).

J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, “Proposed experiment to test local hidden-variable theories,” *Phys. Rev. Lett.* **23**, 880–884 (1969).

A. J. Leggett and A. Garg, “Quantum mechanics versus macroscopic realism: Is the flux there when nobody looks?,” *Phys. Rev. Lett.* **54**, 857–860 (1985).

C. Emary, N. Lambert, and F. Nori, “Leggett–Garg inequalities,” *Rep. Prog. Phys.* **77**, 016001 (2014).

J. Kofler and Č. Brukner, “Condition for macroscopic realism beyond the Leggett–Garg inequalities,” *Phys. Rev. A* **87**, 052115 (2013).

A. Fine, “Hidden variables, joint probability, and the Bell inequalities,” *Phys. Rev. Lett.* **48**, 291–295 (1982).

J. P. Jarrett, “On the physical significance of the locality conditions in the Bell arguments,” *Noûs* **18**, 569–589 (1984).

A. Shimony, “Events and processes in the quantum world,” in *Quantum Concepts in Space and Time*, ed. R. Penrose and C. J. Isham, Oxford University Press (1986).

Y. Aharonov and L. Vaidman, “The two-state vector formalism: An updated review,” in *Time in Quantum Mechanics*, Vol. 1, Springer Lecture Notes in Physics (2008).

H. Price and K. Wharton, “Disentangling the quantum world,” *Entropy* **17**, 7752–7767 (2015).

O. Oreshkov, F. Costa, and Č. Brukner, “Quantum correlations with no causal order,” *Nat. Commun.* **3**, 1092 (2012).

L. Hardy, “Towards quantum gravity: A framework for probabilistic theories with non-fixed causal structure,” *J. Phys. A* **40**, 3081–3099 (2007).

M. S. Leifer and M. F. Pusey, “Is a time-symmetric interpretation of quantum theory possible without retrocausality?,” *Proc. Roy. Soc. A* **473**, 20160607 (2017).

P. Nero, “Bell’s Beables, Modal Fixed Points, and the Limits of Factorization,” *Zenodo* (2024).

P. Nero, “Measurement as Global Consistency in Modal Triplet Theory,” *Zenodo* (2024).

</div>
