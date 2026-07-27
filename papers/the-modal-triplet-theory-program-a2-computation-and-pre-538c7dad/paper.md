---
abstract: |
  We separate four notions that were conflated in the first version of Program A2: finite admissible prediction depth, underdetermination at a branching relation, algorithmic undecidability, and computational lower bounds. Prediction depth is a chart- and protocol-relative iteration diagnostic. It is finite only under a certified finite barrier along the declared continuations; finite depth alone does not imply undecidability. A selection reachability problem becomes algorithmically undecidable if a selected MTT realization robustly and uniformly embeds a universal two-counter machine, preserves every finite machine prefix, and identifies halting with a selected target event. We prove this conditional transfer theorem and also prove the complementary finite-capacity result: a fixed finite carrier with computable transitions has decidable reachability and therefore cannot satisfy the unbounded embedding contract. Neither non-Markovianity, noninjective projection, branching, nor nil termination supplies that contract by itself. Computational irreducibility additionally requires a specified computation model and a lower-bound theorem. Probability, quantization, physical time, and universal limits of control remain separate source obligations.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: ec74c511a8291103777f6b9da9f88eeed9e23300922d04c09ae7aa533f4f46dd
paper_id: the-modal-triplet-theory-program-a2-computation-and-pre-538c7dad
release_state: zenodo_released
released_version: v1.0
title: |
  The Modal Triplet Theory Program A2:  
  Conditional Computability and Finite Prediction Depth
zenodo_doi: 10.5281/zenodo.18354966
zenodo_record_id: 18354966
zenodo_url: "https://zenodo.org/records/18354966"
---

# Revision note for version 2

#### Supersedes.

Version 1 of Program A2.

#### Reason.

The former paper used “undecidable” for several different failures of prediction and inferred algorithmic undecidability from finite admissibility, branching, and nil termination without a declared input language or reduction. It also combined unbounded counter storage with a finite admissibility horizon.

#### Resolution.

Version 2 introduces a computable reachability presentation, states the exact robust two-counter embedding contract, proves undecidability only conditional on that contract, and proves that a fixed finite carrier cannot realize it. It also gives correctly scoped prediction-depth and control statements.

#### Retained content.

Prediction as admissible continuation, protocol-relative prediction depth, and the distinction between local prediction and a global effective description remain useful.

#### Open boundary.

No selected MTT realization is presently proved to implement unbounded, robust counter storage and operations. No complexity lower bound, Born measure, quantization theorem, physical time variable, or universal controller no-go follows from A2 alone.

# Scope and Logical Separation

Program A0 supplies typed upper evolution, reductions, admissible domains, and an iteration-count prediction-depth diagnostic . Program A1 supplies chart-persistence kinematics and only a conditional bridge to physical spacetime propagation . The present paper adds a computability layer. It does not turn descriptive order into physical time or a chart obstruction into a theorem of mathematical logic.

## Four different questions

Let a finite string describe an initial state and a protocol. The following questions are distinct.

1.  *Semantic determinacy:* does the selected data define one continuation, several continuations, or no continuation?

2.  *Decidability:* is there an algorithm that returns the correct yes/no answer on every input in a declared language?

3.  *Complexity:* among algorithms that decide the language, what resources are required as a function of input length?

4.  *Simulation cost:* for a specified trajectory, how much work is required to reproduce a chosen number of steps?

Branching may make an actual branch underdetermined while existential or universal reachability remains decidable. A long simulation may be expensive without being undecidable. Conversely, undecidability is a uniform statement over an infinite input family, not a claim that every instance is hard.

<div class="remark">

*Remark 1* (Terminology). In this paper, “undecidable” has its standard algorithmic meaning. A question outside the domain of an encoding is *undefined* there. A question with several admissible answers is *underdetermined* until a selector is added. Neither condition is renamed undecidability.

</div>

# Computable Admissible Presentations

Computability requires more structure than a topological atlas.

<div id="def:presentation" class="definition">

**Definition 2** (Computable admissible presentation). A computable admissible presentation is a tuple
``` math
\mathfrak C=(\Sigma,S,\iota,F,A,H)
```
with the following data.

- $`\Sigma`$ is a finite alphabet and $`S\subseteq\Sigma^\ast`$ is a decidable set of finite state descriptions, equipped with a computable rational-valued metric $`d_S`$ when robustness is claimed.

- $`\iota:\Sigma^\ast\to S`$ is a total computable input encoder on the declared input language.

- $`F:S\rightharpoonup S`$ is a partial computable one-step map for one fixed protocol, with decidable domain.

- $`A\subseteq S`$ is a decidable admissible set.

- $`H\subseteq A`$ is a decidable target or selection-event set.

An orbit is followed only while $`F`$ is defined and remains in $`A`$.

</div>

The deterministic definition is sufficient for the reduction below. A branching system instead uses a computably presented relation $`R\subseteq S\times S`$ and must declare whether reachability means “there exists a branch” or “every branch.”

<div id="def:sel" class="definition">

**Definition 3** (Selection reachability language). For a presentation $`\mathfrak C`$, define
``` math
\operatorname{SEL}(\mathfrak C)
:=
\left\{
w\in\Sigma^\ast:
\begin{array}{l}
\text{for some }n\geq0,\ F^k(\iota(w))\text{ is defined and in }A\\
\text{for }0\leq k\leq n,\text{ and }F^n(\iota(w))\in H
\end{array}
\right\}.
```

</div>

Because a target hit has a finite witness, this language is recursively enumerable under Definition <a href="#def:presentation" data-reference-type="ref" data-reference="def:presentation">2</a>. Decidability requires more: a decision procedure must also halt on every nonmember.

## Finite recognizable horizons

<div id="prop:recognizable" class="proposition">

**Proposition 4** (Decidability with recognizable termination). *Suppose every orbit of $`\mathfrak C`$ reaches $`H`$, leaves $`A`$, or repeats a previous state after finitely many steps, and each of these events is recognizable from the finite state description. Then $`\operatorname{SEL}(\mathfrak C)`$ is decidable.*

</div>

<div class="proof">

*Proof.* Simulate the orbit while storing visited states. Accept on entering $`H`$. Reject on leaving $`A`$, on an undefined transition, or on the first repeated state. By hypothesis one of these cases occurs after finitely many steps. ◻

</div>

<div class="remark">

*Remark 5*. A finite horizon is not enough if its endpoint is only a semantic statement that the chosen encoding no longer represents the intended upper object and there is no effective test for that loss. Conversely, an instance-dependent horizon need not be known in advance if exit is effectively recognizable. The algorithm may simply simulate until the recognizable exit.

</div>

# Admissible Prediction Depth

We now retain the useful A2 diagnostic in a form compatible with A0.

<div class="definition">

**Definition 6** (Protocol-relative prediction depth). Let $`T_{A,\pi}:P_0(A)\rightharpoonup P_0(A)`$ be a declared reduced step map for an admissible domain $`A`$ and protocol $`\pi`$. For $`x\in A`$, set
``` math
N_{\max}(x;A,\pi)
:=
\sup\left\{
n\in\mathbb N:
T_{A,\pi}^{k}(P_0x)\text{ is defined and in }P_0(A)
\text{ for }0\leq k\leq n
\right\}.
```

</div>

This number counts iterations. A conversion to elapsed time, proper time, distance, energy, or an information budget requires a realization-specific bridge.

<div id="thm:depth" class="theorem">

**Theorem 7** (Certified finite depth). *If there is an integer $`d<\infty`$ such that every declared continuation from $`P_0x`$ either leaves $`P_0(A)`$, becomes undefined, or reaches a separately declared branch ambiguity by step $`d`$, then
``` math
N_{\max}(x;A,\pi)\leq d
```
for the corresponding continuation convention.*

</div>

<div class="proof">

*Proof.* No continuation satisfying the defining conditions can contain more than $`d`$ admissible, unambiguous steps. ◻

</div>

<div class="remark">

*Remark 8* (What does not prove finite depth). The mere existence of a selection front or nil boundary somewhere in a reachable graph does not give a uniform bound on every path. One must prove that the declared paths meet the barrier in finite depth, or supply a coercive margin or ranking function that yields such a bound.

</div>

<div id="prop:refinement" class="proposition">

**Proposition 9** (Refinement monotonicity under a projection contract). *Let a refined transition system project stepwise to a coarse one, let every refined admissible path project to a coarse admissible path, and let the refined determinacy criterion imply the coarse criterion. Then refined prediction depth cannot exceed coarse prediction depth.*

</div>

<div class="proof">

*Proof.* Every refined path counted at depth $`n`$ produces a coarse path counted at depth $`n`$. Taking suprema gives the claim. ◻

</div>

Without this path-projection contract, refinement can expose an obstruction, remove a spurious obstruction, or change the protocol, so monotonicity is not automatic.

# Branching, Nil Boundaries, and Algorithms

<div id="prop:branch" class="proposition">

**Proposition 10** (Branching is not undecidability). *Suppose a computable, finitely branching relation $`R`$ returns an effective finite successor list for each state. For a fixed finite depth $`d`$, both
``` math
\exists\text{ a branch reaching }H\text{ by }d
\quad\text{and}\quad
\forall\text{ branches, }H\text{ is reached by }d
```
are decidable.*

</div>

<div class="proof">

*Proof.* Enumerate the finite computation tree to depth $`d`$ and inspect its leaves. ◻

</div>

Thus a branch selector may be absent even though reachability questions are algorithmically decidable. Conversely, an infinite computable transition system can have an undecidable reachability language even when each state has only one successor.

<div id="prop:nil" class="proposition">

**Proposition 11** (Nil boundary semantics). *If a chart continuation is undefined beyond a certified nil boundary, then a question whose semantics requires that continuation is undefined in that chart system. It becomes a yes/no decision problem only after a total extension, rejection convention, or alternative chart relation is specified.*

</div>

<div class="proof">

*Proof.* A partial map has no value outside its domain. Algorithmic decidability is a property of a total Boolean-valued decision problem, so the missing semantic value must first be completed by declared data. ◻

</div>

# Two-Counter Machines and the Missing MTT Contract

A deterministic two-counter machine has a finite control set $`Q`$, two registers in $`\mathbb N`$, and instructions <span class="smallcaps">inc</span>, <span class="smallcaps">decjz</span>, and <span class="smallcaps">halt</span>. A fixed universal machine can receive its program and input through the initial register values. Its halting language is undecidable .

<div id="def:embedding" class="definition">

**Definition 12** (Robust uniform MTT embedding). Let $`\mathcal M`$ be a fixed universal two-counter machine with configuration set
``` math
\operatorname{Conf}(\mathcal M)=Q\times\mathbb N^2
```
and partial step map $`\tau`$. A robust uniform embedding of $`\mathcal M`$ into an MTT presentation consists of:

1.  a computable injective code $`J:\operatorname{Conf}(\mathcal M)\to A`$ and a total computable reduction map $`g`$ from machine inputs to presentation inputs such that
    ``` math
    \iota(g(w))=J(c_0(w));
    ```

2.  *step fidelity*,
    ``` math
    F(J(c))=J(\tau(c))
    ```
    for every nonhalting configuration on every encoded run;

3.  *unbounded admissible persistence*: every finite prefix of every encoded machine run remains in the domain of $`F`$ and in $`A`$;

4.  *target fidelity*: $`J(c)\in H`$ if and only if $`c`$ is a halting configuration;

5.  *uniformity*: $`F,A,H`$, and the decoding convention are fixed independently of the input;

6.  *robustness*: there is a computable positive rational radius $`\delta(c)`$ such that
    ``` math
    U_c:=\{s\in S:d_S(s,J(c))<\delta(c)\}
    ```
    is nonempty, lies in $`A`$, has constant target membership, and, when $`\tau(c)`$ is defined,
    ``` math
    F(U_c)\subseteq U_{\tau(c)}.
    ```

</div>

Condition (E3) does not require an infinite amount of storage at any finite step. It requires a system with no fixed global counter cap across the entire input family and all finite run prefixes. This is precisely the condition missing from a construction that supplies only a finite admissible horizon.

<div id="thm:undecidable" class="theorem">

**Theorem 13** (Conditional selection-reachability undecidability). *If a selected MTT realization satisfies Definition <a href="#def:embedding" data-reference-type="ref" data-reference="def:embedding">12</a>, then its selection reachability language is undecidable. More precisely,
``` math
\operatorname{HALT}_{\mathcal M}
\leq_m
\operatorname{SEL}(\mathfrak C).
```*

</div>

<div class="proof">

*Proof.* Given a machine input $`w`$, compute $`g(w)`$ and hence the corresponding initial MTT code $`\iota(g(w))=J(c_0(w))`$. Conditions (E2) and (E3) identify every finite MTT prefix with the corresponding machine prefix. By (E4), the MTT orbit reaches $`H`$ if and only if $`\mathcal M`$ halts on $`w`$. Therefore an algorithm deciding $`\operatorname{SEL}(\mathfrak C)`$ would decide the halting language of the fixed universal two-counter machine, a contradiction. Conditions (E5) and (E6) ensure that the reduction is not hidden in an input-dependent controller and is stable on the declared neighborhoods. ◻

</div>

<div class="remark">

*Remark 14* (Current MTT status). The theorem is exact and conditional. Projection, non-Markovianity, stable records, locality, or basin language alone does not construct $`J`$, $`F`$, the zero test, an unbounded admissible register, or the neighborhoods $`U_c`$. The current corpus has not supplied all six embedding clauses for a selected physical MTT realization.

</div>

# Finite Capacity Is a No-Go for the Strong Claim

<div id="thm:finite" class="theorem">

**Theorem 15** (Fixed-capacity reachability). *Let $`Q`$ be finite and suppose each of two counters is bounded by a fixed $`C<\infty`$. For any deterministic transition rule on
``` math
Q\times\{0,\ldots,C\}^2,
```
halting reachability is decidable.*

</div>

<div class="proof">

*Proof.* There are at most $`|Q|(C+1)^2`$ configurations. Simulate from the initial configuration. Accept on halting. If a configuration repeats before halting, determinism makes the subsequent orbit periodic, so reject. ◻

</div>

<div class="corollary">

**Corollary 16** (Capacity obstruction). *A selected realization with one fixed finite state carrier and computable transition table cannot satisfy Definition <a href="#def:embedding" data-reference-type="ref" data-reference="def:embedding">12</a>. A family of larger finite truncations is not enough unless the passage to arbitrarily large admissible prefixes is itself uniform and proved.*

</div>

<div class="proof">

*Proof.* Finite-state reachability is decidable by the same repeated-state argument, whereas Theorem <a href="#thm:undecidable" data-reference-type="ref" data-reference="thm:undecidable">13</a> would make the embedded halting language undecidable. ◻

</div>

There are two coherent research targets:

1.  prove a genuinely unbounded selected MTT carrier with robust operations and no premature admissibility exit; or

2.  retain a finite carrier and state only finite-horizon simulation and verification results.

The second target can still be physically and computationally valuable, but it does not establish universal undecidability.

# Complexity and “Full Simulation”

<div class="definition">

**Definition 17** (Decision-time complexity). Fix an encoding of inputs, a machine model, and a size function $`|w|`$. A decision-time lower bound for a language $`L`$ is a theorem that every deciding algorithm in the declared model uses at least the stated resources on an infinite family of inputs .

</div>

<div class="remark">

*Remark 18*. Non-Markovianity says that a chosen reduced state is not sufficient for autonomous one-step prediction. Enlarging the state by memory variables may restore Markovian evolution. This fact neither proves undecidability nor a complexity lower bound.

</div>

<div class="remark">

*Remark 19*. Finite capacity usually makes a fixed model easier to decide by exhaustive state exploration, though the state count can be large. It does not by itself imply computational irreducibility.

</div>

The phrase “prediction requires full simulation” can mean at least three different things:

1.  no closed-form shortcut is presently known;

2.  a particular prediction algorithm follows every step;

3.  every correct algorithm requires resources comparable to stepwise simulation.

Only the third is a lower-bound claim, and it requires a formal computation model and proof. Theorem <a href="#thm:undecidable" data-reference-type="ref" data-reference="thm:undecidable">13</a> establishes no such bound for decidable instances and no claim about all MTT trajectories.

# Conditional Consequences for Control

<div class="definition">

**Definition 20** (Universal intervention verifier). Let $`\mathcal U`$ be an effectively presented family of admissible interventions containing a no-intervention element $`u_0`$. A universal intervention verifier is a total algorithm $`V(w,u)`$ that returns “yes” if the orbit obtained from input $`w`$ under intervention $`u`$ reaches $`H`$, and “no” otherwise.

</div>

<div id="prop:control" class="proposition">

**Proposition 21** (Conditional intervention-verifier obstruction). *On a realization satisfying Definition <a href="#def:embedding" data-reference-type="ref" data-reference="def:embedding">12</a>, no universal intervention verifier exists for a family containing the no-intervention element $`u_0`$.*

</div>

<div class="proof">

*Proof.* The map $`w\mapsto V(g(w),u_0)`$ would decide whether the uncontrolled encoded orbit reaches $`H`$. It would therefore decide $`\operatorname{HALT}_{\mathcal M}`$, contradicting Theorem <a href="#thm:undecidable" data-reference-type="ref" data-reference="thm:undecidable">13</a>. ◻

</div>

This result does not forbid local feedback control, control on a decidable subclass, probabilistic control, controller synthesis without a complete verifier, or a verifier that sometimes returns “unknown.” Branching also does not imply that interventions cannot alter branch weights or admissible successors; that is a dynamical question.

# What A2 Does Not Derive

## Probability

An algorithmic no-go does not select a probability measure. A probability statement needs a measurable space, a normalized state or measure, and an outcome map. Undecidability is compatible with deterministic, stochastic, or set-valued dynamics and therefore does not imply the Born rule.

## Quantization

A finite survivor set may be discrete, but discreteness at one truncation is not a quantization theorem. Quantization requires a selected algebra, representation, spectrum or integral condition, and a source relation to the physical observables.

## Time, horizons, and irreversibility

$`N_{\max}`$ is an iteration count. It is not a physical time or a spacetime horizon. A noncompact ordering variable, a Lorentzian metric, and a hyperbolic propagation law require their own bridge. Likewise, a partial or noninjective reduced map does not by itself prove thermodynamic irreversibility.

## Upper dynamics

Encoding termination says that the declared chart no longer supplies a compatible representation. It does not prove that upper evolution terminates. A different chart, extension, or upper description may remain available.

# Scoped A2 Theorem

<div id="thm:scope" class="theorem">

**Theorem 22** (Conditional computability and prediction-depth package). *For a declared MTT chart-transition system:*

1.  *prediction depth is a chart- and protocol-relative iteration diagnostic;*

2.  *it is finite under the certified barrier hypothesis of Theorem <a href="#thm:depth" data-reference-type="ref" data-reference="thm:depth">7</a>;*

3.  *refinement monotonicity holds under the projection contract of Proposition <a href="#prop:refinement" data-reference-type="ref" data-reference="prop:refinement">9</a>;*

4.  *finite-depth branching and nil boundaries represent underdetermination or partial semantics, not algorithmic undecidability by themselves;*

5.  *a robust uniform universal two-counter embedding implies undecidable selection reachability by Theorem <a href="#thm:undecidable" data-reference-type="ref" data-reference="thm:undecidable">13</a>;*

6.  *a fixed finite carrier has decidable reachability and cannot satisfy that unbounded embedding contract; and*

7.  *complexity, full-simulation, probability, quantization, physical time, and universal control claims require additional hypotheses.*

</div>

<div class="proof">

*Proof.* Items 1–3 follow from the definitions and Theorem <a href="#thm:depth" data-reference-type="ref" data-reference="thm:depth">7</a>–Proposition <a href="#prop:refinement" data-reference-type="ref" data-reference="prop:refinement">9</a>. Item 4 is Propositions <a href="#prop:branch" data-reference-type="ref" data-reference="prop:branch">10</a> and <a href="#prop:nil" data-reference-type="ref" data-reference="prop:nil">11</a>. Items 5 and 6 are Theorems <a href="#thm:undecidable" data-reference-type="ref" data-reference="thm:undecidable">13</a> and <a href="#thm:finite" data-reference-type="ref" data-reference="thm:finite">15</a>. Item 7 records the missing structures identified in the preceding sections. ◻

</div>

# Version Delta and Research Frontier

Relative to version 1, this revision:

- withdraws the unsupported no-global-predictive-map theorem;

- replaces generic structural undecidability by a conditional many-one reduction;

- states the six-clause robust embedding contract explicitly;

- corrects the conflict between unbounded counters and fixed finite admissibility capacity;

- distinguishes branching, undefined continuation, undecidability, complexity lower bounds, and simulation cost;

- narrows the control result to an intervention-verifier consequence of the same reduction; and

- removes the claimed derivation of quantization, measurement probabilities, horizons, and irreversibility from prediction depth.

The decisive constructive frontier is now precise: exhibit, in one selected MTT realization, a computable carrier and step map satisfying (E1)–(E6), especially unbounded admissible persistence and a robust zero test. Until then, the corpus supports finite prediction-depth diagnostics and finite simulations, but not a universal MTT undecidability theorem.

# Conclusion

Finite admissibility can limit the range of a chosen description without making its reachability language undecidable. Branching can leave an outcome unselected without making existential or universal reachability uncomputable. A nil boundary can make continuation undefined without supplying a Boolean decision problem. These distinctions do not weaken the MTT program; they isolate the missing theorem.

If a selected realization robustly embeds a universal two-counter machine and preserves every finite run prefix, undecidable selection reachability follows immediately and rigorously. If the realization instead has one fixed finite capacity, reachability is decidable. Program A2 therefore converts a broad claim into a clean fork between an explicit universality construction and an honest finite-horizon computational model.

<div class="thebibliography">

9

P. Nero, *The Modal Triplet Theory Program A0: A Structural Theory of Reduced Description*, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program A1: Coherent Kinematics*, version 2, 2026.

M. Minsky, *Computation: Finite and Infinite Machines*, Prentice-Hall, 1967.

A. M. Turing, “On computable numbers, with an application to the Entscheidungsproblem,” *Proceedings of the London Mathematical Society* 42 (1936), 230–265.

J. Hartmanis and R. E. Stearns, “On the computational complexity of algorithms,” *Transactions of the American Mathematical Society* 117 (1965), 285–306.

C. Moore, “Unpredictability and undecidability in dynamical systems,” *Physical Review Letters* 64 (1990), 2354–2357.

</div>
