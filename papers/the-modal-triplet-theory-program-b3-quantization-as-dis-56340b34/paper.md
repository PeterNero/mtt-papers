---
abstract: |
  We determine exactly what a nil-type termination of an admissible description does and does not imply. Failure of a declared chart or continuation map does not by itself collapse nearby admissible states to a discrete set. A finite survivor set follows, for example, when a smooth constraint map $`C:M^n\to\mathbb R^n`$ is transverse to zero and its zero set is compact. Discrete spectral values follow under a different hypothesis: a self-adjoint operator on a Hilbert space has discrete finite-multiplicity spectrum when its resolvent is compact. Neither conclusion follows from the nil label alone.

  These results define a useful MTT *discrete survivor filter*, but they do not uniquely characterize quantum mechanics. Finite classical state machines, Morse critical sets, symbolic labels, and topological winding sectors also give discrete survivors. Moreover, discreteness does not supply a noncommutative observable algebra, a complex Hilbert space, canonical commutation or anticommutation relations, dynamics, measurement instruments, or the Born rule. Indeed, exact finite-dimensional canonical commutation relations are impossible by the trace of a commutator.

  We therefore formulate quantum mechanics as a conditional reconstruction. Given a complex unital C\*-algebra, a positive normalized state, a representation or the associated GNS construction, a dynamical law, and effects or instruments, the standard operator and probability structures are available. Program B3 establishes the discrete-filter and compact-resolvent bridges and records the remaining same-source obligations; it does not derive complex quantum mechanics from nil termination.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 5e85579b4047b9d2d838573f039e5aaf72672d0a801675e8fc3bf84a8bbf949f
paper_id: the-modal-triplet-theory-program-b3-quantization-as-dis-56340b34
release_state: zenodo_released
released_version: v2
title: |
  The Modal Triplet Theory Program B3:
  Discrete Survivor Filters and Conditional Quantum Reconstruction
zenodo_doi: 10.5281/zenodo.21652653
zenodo_record_id: 21652653
zenodo_url: "https://zenodo.org/records/21652653"
---

# Revision note for version 2

<div class="description">

Version 1 of Program B3.

The first version inferred that a nil obstruction forces continuous families to collapse, treated discrete survivor structure as the unique content of quantization, and moved from discreteness to measurement language without independent algebraic, dynamical, or probabilistic inputs.

Version 2 separates chart-extension failure from a selected survivor constraint. It proves conditional finite-survivor and compact-resolvent theorems, gives nonquantum countermodels, proves the finite-dimensional canonical-commutator no-go, and states the extra data required for a genuine quantum reconstruction.

Nil-type termination can motivate a survivor filter; compact or topological constraints can produce robust discrete labels; and discreteness alone carries no intrinsic probability distribution.

No theorem here selects a complex C\*-algebra, Hilbert representation, quantum state, CCR/CAR representation, Hamiltonian, measurement instrument, Born weights, or physical outcome from the nil profile alone.

</div>

# How to Read Program B3

The word “quantization” is used for several mathematically different operations. A continuous model may acquire discrete labels because a constraint has isolated solutions, because a quotient has collapsed an orbit, because an operator has discrete spectrum, or because a quantum observable is represented on a Hilbert space. These mechanisms can coexist, but none of them is interchangeable with the others. The purpose of this paper is to separate them before asking whether MTT supplies a quantum theory.

## The four layers of the argument

The discussion is organized as a sequence of four gates.

1.  **Termination.** A declared chart or decoder ceases to extend. This is the nil-type statement. It concerns the description being used, not the cardinality of the underlying state space.

2.  **Survival.** A constraint, controlled domain, and equivalence relation select the states that remain admissible. Transversality and compactness can then make the reduced survivor set finite.

3.  **Spectrum.** A separately supplied operator can have discrete spectrum. Compact resolvent is one standard sufficient condition, but it already presupposes a Hilbert carrier and operator-domain data.

4.  **Quantum reconstruction.** A complex observable algebra, a state, a representation, dynamics, and measurement effects are supplied from one source. Only at this layer do Hilbert-space amplitudes and Born probabilities become available.

The main logical lesson is therefore
``` math
\text{nil termination}
 \;\not\Rightarrow\;
 \text{finite survivors}
 \;\not\Rightarrow\;
 \text{discrete spectrum}
 \;\not\Rightarrow\;
 \text{quantum mechanics}.
```
Each arrow can become valid only after the missing hypotheses displayed later in the paper are added.

## Object picture: a chart can end while states continue

Imagine describing a smooth road with a coordinate that becomes infinite at a particular marker. The coordinate description has failed there, but the road has not become a collection of isolated points. Definition <a href="#def:nil" data-reference-type="ref" data-reference="def:nil">1</a> formalizes exactly this relative kind of failure. To obtain isolated survivors one must add an actual selection rule, such as simultaneous constraints whose Jacobian has full rank.

This distinction is especially important in MTT. The circle, lens, and nil profiles describe how a chosen representation behaves. A nil profile may tell us where a continuation is unavailable, while a lens profile may identify many representatives of one reduced state. Neither profile, without a declared source map, chooses an observable algebra or a probability measure.

## What the reader should take from each theorem

The regular-value results explain when geometric constraints isolate survivors. The classical countermodels show that isolation is not uniquely quantum. The compact-resolvent theorem explains a different route to discreteness through operator theory. The commutator no-go prevents a finite matrix model from being mistaken for an exact bosonic canonical system. Finally, the GNS, Born-evaluation, and Stone results show precisely what standard quantum structure follows once the corresponding algebraic data have been supplied. They are reconstruction results, not claims that nil termination generated those data.

# Scope and Imported Data

Program A0 supplies typed reductions, admissible domains, exact factorization criteria, and controlled approximate descent . Program B0 treats circle, lens, and nil as coarse profiles rather than an exhaustive classification or a list of literal topological factors . In that usage, a nil profile records failure of a declared chart, decoder, transition, or continuation to extend. Programs B1 and B2 show how physical gravity and gauge theory arise only after their own geometric and dynamical data are supplied .

The present paper asks:

> Under which additional hypotheses does a nil-adjacent admissibility problem have discrete survivors, and what further structures are needed before those survivors constitute quantum mechanics?

The distinction is essential. The empty fiber of one reduction can coexist with a perfectly continuous upper evolution or with a different admissible chart. Even when the selected survivor set is finite, a finite set is not a Hilbert space, an observable algebra, a probability law, or a quantum measurement theory.

# Nil Profiles and Survivor Data

## Typed termination

<div id="def:nil" class="definition">

**Definition 1** (Nil-type profile). Let $`X`$ be an upper state space, let $`D\subseteq X`$ be the domain of a declared reduction or chart
``` math
\pi:D\longrightarrow Y,
```
and let $`\mathcal C`$ be a declared class of admissible extensions. A point $`x\in\overline D`$ has a *nil-type profile relative to $`(\pi,D,\mathcal C)`$* when $`\pi`$ has no extension in $`\mathcal C`$ to any allowed neighborhood of $`x`$.

</div>

This is a relative predicate. It depends on the map, its domain, the allowed category, and the extension class. It does not say that $`x`$ is absent from $`X`$, that upper dynamics terminates, or that every other chart fails.

<div id="prop:nil-not-discrete" class="proposition">

**Proposition 2** (Termination does not imply discreteness). *A nil-type profile in the sense of Definition <a href="#def:nil" data-reference-type="ref" data-reference="def:nil">1</a> does not imply that the admissible states in $`D`$, in $`\overline D`$, or in a neighboring chart form a discrete set.*

</div>

<div class="proof">

*Proof.* Let $`X=\mathbb R`$, $`D=(-\infty,0)`$, $`Y=\mathbb R`$, and
``` math
\pi(x)=\frac{1}{x}.
```
In the category of finite continuous real-valued maps, $`\pi`$ has no extension to a neighborhood of $`0`$, so $`0`$ has a nil-type profile. Nevertheless $`D`$ is a continuum. Failure of the selected decoder therefore does not collapse the upper or admissible domain to isolated points. ◻

</div>

<div class="remark">

*Remark 3*. The example is deliberately elementary. The same logical separation applies to singular coordinate systems, blow-up charts, finite-band decoders, and effective descriptions whose conditioning fails at a boundary.

</div>

## A separate survivor predicate

<div id="def:survivor" class="definition">

**Definition 4** (Survivor datum). A *survivor datum* is a tuple
``` math
(M,C,K,\sim),
```
where $`M`$ is a declared state or parameter space, $`C:M\to V`$ is a constraint map into a declared target, $`K\subseteq M`$ is the controlled domain, and $`\sim`$ is the declared equivalence relation. Its raw and reduced survivor sets are
``` math
\mathcal S_{\rm raw}=K\cap C^{-1}(0),
 \qquad
 \mathcal S=\mathcal S_{\rm raw}/\sim.
```

</div>

The nil profile can motivate the choice of $`C`$ or $`K`$, but it does not determine them. Discreteness is a theorem about this survivor datum.

<div class="definition">

**Definition 5** (Discrete survivor filter). A survivor datum is a *discrete survivor filter* when its reduced survivor set $`\mathcal S`$ is discrete in the declared quotient topology. It is a *finite survivor filter* when $`\mathcal S`$ is finite.

</div>

The quotient must be stated. A continuous gauge orbit can represent one reduced survivor, while an unquotiented presentation remains continuous.

# When Constraints Actually Give Discrete Survivors

## The transverse compact theorem

<div id="thm:regular-value" class="theorem">

**Theorem 6** (Regular survivor dimension). *Let $`M`$ be a smooth $`n`$-manifold, let $`C:M\to\mathbb R^r`$ be smooth, and suppose that $`0`$ is a regular value of $`C`$. Then
``` math
C^{-1}(0)
```
is either empty or a smooth submanifold of dimension $`n-r`$.*

</div>

<div class="proof">

*Proof.* This is the regular-value theorem: surjectivity of $`dC_x:T_xM\to\mathbb R^r`$ for every $`x\in C^{-1}(0)`$ supplies local coordinates in which $`C^{-1}(0)`$ is cut out by $`r`$ coordinate equations  . ◻

</div>

<div id="cor:finite" class="corollary">

**Corollary 7** (Compact transverse finite-survivor theorem). *Under the hypotheses of Theorem <a href="#thm:regular-value" data-reference-type="ref" data-reference="thm:regular-value">6</a>, if $`r=n`$ and $`C^{-1}(0)`$ is compact, then $`C^{-1}(0)`$ is finite.*

</div>

<div class="proof">

*Proof.* The regular-value theorem makes $`C^{-1}(0)`$ a zero-dimensional manifold, hence a discrete topological space. A compact discrete space is finite. ◻

</div>

<div class="remark">

*Remark 8* (What each hypothesis does). Transversality gives local isolation. Equal source and constraint dimensions give dimension zero. Compactness rules out infinitely many isolated solutions escaping to infinity. None of these properties is contained in the word “nil.”

</div>

## Why dimension counting alone is insufficient

If $`r<n`$, a regular survivor set has positive dimension $`n-r`$ and therefore retains continuous families. If $`r>n`$, transversality to zero forces an empty preimage. If zero is singular, the preimage can be discrete, continuous, stratified, or nonreduced. For example,
``` math
C(x,y)=x^2
```
has the continuous zero set $`\{0\}\times\mathbb R`$ even though one equation vanishes to higher order. Thus a count of equations is only informative when rank and domain hypotheses are certified.

## Quotient survivors

<div id="prop:quotient-finite" class="proposition">

**Proposition 9** (Finite raw set implies finite reduced set). *If $`\mathcal S_{\rm raw}`$ is finite, then $`\mathcal S_{\rm raw}/\sim`$ is finite for every equivalence relation $`\sim`$. The converse need not hold.*

</div>

<div class="proof">

*Proof.* A quotient map cannot create more equivalence classes than there are elements. For the converse, a nontrivial group can act transitively on an infinite or continuous raw set, producing a one-point quotient. ◻

</div>

This proposition prevents a common conflation: reduced discreteness can result from a quotient rather than from isolated upper states.

## Robustness under perturbation

<div id="prop:persistence" class="proposition">

**Proposition 10** (Local persistence of a transverse survivor). *Let $`C_\lambda:M^n\to\mathbb R^n`$ depend smoothly on a finite-dimensional parameter $`\lambda`$. If $`C_0(x_0)=0`$ and $`dC_0|_{x_0}`$ is invertible, then for all sufficiently small $`\lambda`$ there is a unique nearby smooth branch $`x(\lambda)`$ with $`C_\lambda(x(\lambda))=0`$.*

</div>

<div class="proof">

*Proof.* Apply the implicit-function theorem to $`(x,\lambda)\mapsto C_\lambda(x)`$ at $`(x_0,0)`$. ◻

</div>

The proposition gives a precise replacement for the former phrase “stable under arbitrary refinement.” Stability must be tied to a topology, perturbation class, and nonsingularity margin.

# Classical Sources of Discrete Survivors

Discrete labels are not unique to quantum theory.

## Finite deterministic systems

Let $`F:S\to S`$ be a deterministic map on a finite set. Its states, cycles, basins, and transition graph are all discrete. No complex amplitude, noncommutative observable algebra, or Born rule is present. This is already a counterexample to the implication
``` math
\text{discrete survivors}\Longrightarrow\text{quantum mechanics}.
```

## Morse critical points

Let $`M`$ be compact and let $`f:M\to\mathbb R`$ be a Morse function. Its critical points are isolated and therefore finite. They are the zeros of $`df`$, with nondegenerate Hessian, and are robust in the usual Morse-theoretic sense. This is a smooth classical realization of Corollary <a href="#cor:finite" data-reference-type="ref" data-reference="cor:finite">7</a>.

## Symbolic dynamics

A finite alphabet supplies discrete symbols and a finite directed graph supplies discrete admissibility rules. Bi-infinite symbolic trajectories can nevertheless form an uncountable compact space. Thus “discrete alphabet” does not even imply a discrete trajectory space. Symbolic dynamics illustrates both the usefulness and the limits of discrete encodings .

## Topological sectors

Maps $`S^1\to S^1`$ are classified up to homotopy by an integer degree. The sector label is discrete, although each sector contains continuous families of maps. Likewise, characteristic classes and winding numbers can label components without quantizing all local degrees of freedom .

<div class="remark">

*Remark 11* (Conclusion from the countermodels). A discrete survivor filter is a broad structural response available to classical, topological, combinatorial, and quantum models. It is canonical only at the level of the declared constraint problem, not as a unique identification with quantum mechanics.

</div>

Taken together, these examples explain why the survivor theorem should be read as a reusable geometric tool rather than as a definition of the quantum. The same theorem can organize classical equilibria, topological sectors, or candidate outcome labels. What those labels mean physically is decided only by the additional source and representation data attached to them.

# Spectral Discreteness Is a Separate Theorem

## Compact resolvent

<div class="definition">

**Definition 12** (Compact resolvent). Let $`A`$ be a densely defined closed operator on a Hilbert space $`\mathcal H`$ with nonempty resolvent set. It has *compact resolvent* if
``` math
(A-zI)^{-1}
```
is compact for one, and hence every, $`z`$ in the resolvent set.

</div>

<div id="thm:compact-resolvent" class="theorem">

**Theorem 13** (Self-adjoint compact-resolvent spectrum). *Let $`A`$ be self-adjoint on a complex Hilbert space and have compact resolvent. Then $`\operatorname{spec}(A)\subset\mathbb R`$ consists only of isolated eigenvalues of finite multiplicity, with no finite accumulation point. If $`\mathcal H`$ is infinite-dimensional, the eigenvalues can accumulate only at infinity  .*

</div>

<div class="proof">

*Proof.* For $`z\notin\mathbb R`$, the resolvent $`R_z=(A-zI)^{-1}`$ is compact and normal. The spectral theorem for compact normal operators gives nonzero eigenvalues of finite multiplicity whose only possible accumulation point is zero. The spectral mapping $`\mu=(\lambda-z)^{-1}`$ transfers these values to eigenvalues of $`A`$ and turns accumulation at zero into escape of $`|\lambda|`$ to infinity. ◻

</div>

## What the theorem imports

Theorem <a href="#thm:compact-resolvent" data-reference-type="ref" data-reference="thm:compact-resolvent">13</a> assumes:

1.  a Hilbert space;

2.  a densely defined operator and its domain;

3.  closedness and self-adjointness;

4.  a nonempty resolvent set; and

5.  compactness of the resolvent.

A nil-type chart failure supplies none of these. Conversely, a finite matrix has a finite spectrum for elementary algebraic reasons, even if it came from a classical discretization. A finite Galerkin truncation therefore cannot, by itself, prove compact resolvent or the spectrum of its continuum parent.

## Topological and spectral discreteness differ

A topological sector label classifies connected components or homotopy classes. A spectral value is an eigenvalue of a declared operator. Either can be discrete while the other is absent. Identifying them requires an explicit map from the topological or constraint data to the operator and a theorem that preserves the relevant spectrum.

# The Quantum Structures That Discreteness Does Not Supply

## Seven logically separate layers

For this paper, a quantum reconstruction distinguishes:

1.  a survivor or outcome label set;

2.  a complex linear state carrier;

3.  a noncommutative involutive observable algebra;

4.  a representation of that algebra;

5.  canonical relations, when relevant;

6.  dynamics; and

7.  states, effects, instruments, and probabilities.

No implication from item 1 to items 2–7 is valid without additional hypotheses.

## Commutativity is not decided by a set

For a finite set $`S`$, the algebra $`C(S)`$ of complex functions is commutative. The matrix algebra $`M_N(\mathbb C)`$ is noncommutative. Both may be built over the same number $`N`$ of labels. Therefore cardinality or discreteness cannot select the observable product.

## Complex amplitudes are not decided by a circle

A supplied Hermitian line bundle with $`U(1)`$ connection can carry phase and holonomy. It does not by itself select a complex Hilbert space of physical states, an inner product, linear superposition, or a representation of observables. Real and quaternionic quantum formalisms also show that the scalar field is an independent structural choice. A shared MTT circle may participate in a complex reconstruction only through a proved connection- preserving source map.

## Finite-dimensional CCR no-go

<div id="thm:ccr-no-go" class="theorem">

**Theorem 14** (No exact finite-dimensional canonical commutator). *Let $`Q,P\in M_N(\mathbb C)`$ and let $`\hbar\ne0`$. Then
``` math
[Q,P]=i\hbar I_N
```
is impossible.*

</div>

<div class="proof">

*Proof.* The cyclicity of the finite-dimensional trace gives
``` math
\operatorname{tr}[Q,P]
 =\operatorname{tr}(QP)-\operatorname{tr}(PQ)=0.
```
The proposed right-hand side has trace $`i\hbar N\ne0`$. ◻

</div>

Exact bosonic CCR representations therefore require an infinite-dimensional setting and careful unbounded-operator domains, or a Weyl-algebra formulation. A finite survivor matrix may approximate selected observables, but it is not an exact CCR representation merely because it has discrete states.

## CAR is also an input

For finitely many fermionic modes, the CAR algebra has finite-dimensional matrix representations. This possibility does not make CAR follow from finiteness. One must still supply generators $`a_j,a_j^*`$ and prove
``` math
\{a_j,a_k^*\}=\delta_{jk}I,
 \qquad
 \{a_j,a_k\}=0.
```
The distinction between the CCR no-go and finite-mode CAR representations is another reason to keep “discrete” and “quantum” separate.

# Conditional C\*-Algebraic Quantum Reconstruction

## Reconstruction datum

<div id="ass:quantum" class="assumption">

**Assumption 15** (Quantum reconstruction datum). Supply:

1.  a complex unital C\*-algebra $`\mathfrak A`$ of observables;

2.  a state $`\omega:\mathfrak A\to\mathbb C`$, meaning a positive linear functional with $`\omega(I)=1`$;

3.  a strongly continuous dynamical law, either a one-parameter group $`\alpha_t`$ of \*-automorphisms or a declared open-system evolution;

4.  a class of effects $`0\le E\le I`$ and, for sequential measurements, a specified instrument; and

5.  a source map relating the selected MTT survivor, bundle, or operator data to $`\mathfrak A`$, $`\omega`$, the dynamics, and the effects.

</div>

## GNS representation

<div id="thm:gns" class="theorem">

**Theorem 16** (Conditional Hilbert reconstruction). *Under the first two items of Assumption <a href="#ass:quantum" data-reference-type="ref" data-reference="ass:quantum">15</a>, there exist a complex Hilbert space $`\mathcal H_\omega`$, a unital \*-representation
``` math
\pi_\omega:\mathfrak A\longrightarrow B(\mathcal H_\omega),
```
and a cyclic unit vector $`\Omega_\omega`$ such that
``` math
\omega(A)
 =\langle\Omega_\omega,\pi_\omega(A)\Omega_\omega\rangle
 \qquad(A\in\mathfrak A).
```
The cyclic representation is unique up to unitary equivalence  .*

</div>

<div class="proof">

*Proof.* On $`\mathfrak A`$, define $`\langle A,B\rangle_\omega=\omega(A^*B)`$ and quotient by the null left ideal $`N_\omega=\{A:\omega(A^*A)=0\}`$. Complete the quotient to $`\mathcal H_\omega`$. Left multiplication defines $`\pi_\omega`$, and the class of $`I`$ defines $`\Omega_\omega`$. The standard cyclicity and uniqueness argument gives the result. ◻

</div>

<div class="remark">

*Remark 17*. The theorem reconstructs a representation from the supplied pair $`(\mathfrak A,\omega)`$. It does not select either member of that pair from a survivor set.

</div>

In practical terms, GNS is a translator. It turns algebraic expectation data into vectors and operators on a Hilbert space. It does not manufacture the expectation functional, decide which algebra describes the experiment, or identify one survivor with one physical outcome. Those are precisely the same-source tasks retained in Definition <a href="#def:certificate" data-reference-type="ref" data-reference="def:certificate">20</a>.

## Conditional Born probabilities

<div id="prop:born" class="proposition">

**Proposition 18** (Probabilities after state and effect are supplied). *For every effect $`E\in\mathfrak A`$,
``` math
p_\omega(E)=\omega(E)
```
lies in $`[0,1]`$. In the GNS representation,
``` math
p_\omega(E)
 =\langle\Omega_\omega,\pi_\omega(E)\Omega_\omega\rangle.
```
For a vector state and a projection, this is the usual Born expression.*

</div>

<div class="proof">

*Proof.* Positivity gives $`\omega(E)\ge0`$. Since $`I-E\ge0`$, $`1-\omega(E)=\omega(I-E)\ge0`$. The GNS identity gives the second formula. ◻

</div>

This is a probability evaluation theorem, not a probability source theorem. It does not derive $`\omega`$, the effect $`E`$, a detector, a capture process, or one realized outcome.

## Dynamics and Stone’s theorem

<div id="thm:stone" class="theorem">

**Theorem 19** (Conditional Hamiltonian generator). *Let $`U:\mathbb R\to\mathcal U(\mathcal H)`$ be a strongly continuous one-parameter unitary group. There is a unique self-adjoint operator $`H`$ such that
``` math
U(t)=e^{-itH}
```
 .*

</div>

A C\*-dynamical system $`(\mathfrak A,\alpha_t)`$ is unitarily implemented in the GNS representation of an invariant state under the standard construction. The existence of dynamics, invariance of the state, and the physical normalization of $`H`$ remain additional inputs; a discrete spectrum does not choose them.

## Measurement and records

An effect assigns a probability to one event. A quantum instrument additionally specifies outcome probabilities and state updates. Repeatability, decoherence, records, detector thresholds, and objective history selection are further dynamical statements. Nil termination alone proves none of them. In particular, “one survivor remains” is not a collapse theorem unless the physical instrument and state-update map have been derived.

# The MTT Quantum Source Contract

## Same-source requirement

An MTT realization reaches quantum-mechanical reconstruction only if one selected upper source emits compatible instances of all the structures in Assumption <a href="#ass:quantum" data-reference-type="ref" data-reference="ass:quantum">15</a>. Combining an independently chosen survivor set, an unrelated matrix algebra, an observed probability vector, and a fitted Hamiltonian is a profile replay, not a source theorem.

<div id="def:certificate" class="definition">

**Definition 20** (MTT quantum source certificate). An *MTT quantum source certificate* consists of:

1.  a hash-addressed upper carrier and admissibility domain;

2.  a survivor or constraint operator with a proved domain and quotient;

3.  a complex C\*-algebra and representation emitted from that carrier;

4.  selected CCR, CAR, or finite observable relations with exact or controlled-error certificates;

5.  selected dynamics with domain, self-adjointness or complete-positivity conditions, and normalization;

6.  a positive normalized state and selected effects or instruments;

7.  a commuting source map connecting the upper data to each lower object; and

8.  an independent verifier that distinguishes exact, controlled, profile-replay, and open rows.

</div>

## What current finite carriers can establish

A finite projected algebra can be an exact object when the theory explicitly selects that finite algebra. It can establish finite spectral data, noncommutative matrix products, finite-mode CAR, and exact finite traces. It cannot establish exact bosonic CCR by Theorem <a href="#thm:ccr-no-go" data-reference-type="ref" data-reference="thm:ccr-no-go">14</a>. Nor does an exact finite trace automatically become the physical quantum state or detector probability. Those identifications require the source certificate of Definition <a href="#def:certificate" data-reference-type="ref" data-reference="def:certificate">20</a>.

## Relation to circle and lens profiles

The profiles can coexist:

- circle-type transport can act as phase or connection data;

- lens-type quotienting can encode redundant representatives; and

- a nil-adjacent constraint can select a survivor sector.

Compatibility of these roles is not automatic commutativity. Their actions, domains, quotient order, and connection transport must be supplied and checked. No exhaustive “one profile, one physical theory” triad is asserted.

# Scoped B3 Theorem

<div id="thm:scoped" class="theorem">

**Theorem 21** (Discrete filters and conditional quantum reconstruction). *For the typed data and hypotheses of this paper:*

1.  *failure of a declared chart or decoder to extend does not by itself imply a discrete state or survivor set;*

2.  *a smooth constraint $`C:M^n\to\mathbb R^n`$ transverse to zero has isolated zeros, and a compact zero set is finite;*

3.  *classical finite-state, Morse, symbolic, and topological systems can produce discrete survivor labels;*

4.  *a self-adjoint operator with compact resolvent has discrete finite-multiplicity spectrum, but that conclusion imports a Hilbert space, operator domain, self-adjointness, and compactness;*

5.  *a discrete set selects neither a noncommutative algebra nor complex amplitudes;*

6.  *exact finite-dimensional bosonic CCR are impossible, while finite-mode CAR still require an independently supplied algebra;*

7.  *a complex C\*-algebra and state admit the GNS representation;*

8.  *Born probabilities follow for supplied effects and a supplied state; and*

9.  *a Hamiltonian generator follows from supplied strongly continuous unitary dynamics.*

*Consequently, a discrete survivor filter is a useful nil-type response but is not a derivation or unique characterization of complex quantum mechanics.*

</div>

<div class="proof">

*Proof.* Item 1 is Proposition <a href="#prop:nil-not-discrete" data-reference-type="ref" data-reference="prop:nil-not-discrete">2</a>. Item 2 is Theorem <a href="#thm:regular-value" data-reference-type="ref" data-reference="thm:regular-value">6</a> and Corollary <a href="#cor:finite" data-reference-type="ref" data-reference="cor:finite">7</a>. Item 3 is established by the countermodels above. Item 4 is Theorem <a href="#thm:compact-resolvent" data-reference-type="ref" data-reference="thm:compact-resolvent">13</a>. Item 5 follows from the commutative and matrix-algebra counterexamples and the independent scalar-field choice. Item 6 is Theorem <a href="#thm:ccr-no-go" data-reference-type="ref" data-reference="thm:ccr-no-go">14</a> and the subsequent CAR discussion. Items 7–9 are Theorem <a href="#thm:gns" data-reference-type="ref" data-reference="thm:gns">16</a>, Proposition <a href="#prop:born" data-reference-type="ref" data-reference="prop:born">18</a>, and Theorem <a href="#thm:stone" data-reference-type="ref" data-reference="thm:stone">19</a>. ◻

</div>

# Version Delta and Research Frontier

Relative to version 1, this revision:

- replaces the claimed collapse of every continuous family at a nil boundary by a counterexample and a typed extension-failure definition;

- introduces a separate survivor datum with explicit constraint, domain, and quotient;

- proves finite survivors only under transversality, equal constraint dimension, and compactness;

- replaces informal refinement stability by an implicit-function theorem with a declared perturbation class;

- records classical finite-state, Morse, symbolic, and topological countermodels;

- separates topological-sector discreteness from operator-spectrum discreteness;

- states the compact-resolvent spectral theorem with all imported hypotheses;

- separates outcome labels, complex state carriers, observable algebras, representations, canonical relations, dynamics, and probability;

- proves that exact finite-dimensional bosonic CCR are impossible;

- moves complex Hilbert, C\*-algebraic, CCR/CAR, dynamics, measurement, and Born claims into independent reconstruction theorems; and

- withdraws the claims that quantization is the unique response to nil or that the circle–lens–nil profiles exhaust physical gravity, gauge theory, and quantum mechanics.

The next source theorem must provide one selected MTT carrier satisfying Definition <a href="#def:certificate" data-reference-type="ref" data-reference="def:certificate">20</a>. In particular, it must emit the observable algebra, state, representation, dynamics, and effects from the same source as the survivor filter, with exact or controlled transport between them. A finite matrix or a discrete label set alone does not close this frontier.

# Conclusion

Nil-type termination remains a useful warning: a declared reduced description has reached the end of its admissible domain. It can motivate a search for robust survivor data. The revised mathematics shows, however, that the survivors become discrete only when an actual constraint or spectral theorem makes them discrete.

That distinction strengthens the MTT program. The compact transverse theorem gives an exact finite-survivor route, and the compact-resolvent theorem gives an exact spectral route. Their hypotheses can be tested. Classical countermodels then show where the quantum claim begins: complex linearity, noncommutative observables, canonical relations, dynamics, states, and measurement effects must all be sourced.

Program B3 therefore supplies a rigorous discrete-filter layer and a clear quantum reconstruction contract. It does not call every discrete structure quantum. A later selected-source theorem can now succeed by filling explicit mathematical slots rather than by relying on the ambiguity of the word “quantization.”

<div class="thebibliography">

99

P. Nero, *The Modal Triplet Theory Program A0: A Structural Theory of Reduced Description*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B0: Circle–Lens–Nil as an Obstruction Taxonomy and Its Minimal Curvature Realizations*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B1: Loop-Transport Consistency and the Conditional Gravity Realization*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B2: Gauge Redundancy, Global Sections, and the Conditional Yang–Mills Realization*, revised v2, 2026.

J. M. Lee, *Introduction to Smooth Manifolds*, second edition, Springer, 2013.

A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.

D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 1995.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, revised edition, Academic Press, 1980.

J. B. Conway, *A Course in Functional Analysis*, second edition, Springer, 1990.

G. J. Murphy, *C\*-Algebras and Operator Theory*, Academic Press, 1990.

O. Bratteli and D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics I*, second edition, Springer, 1987.

M. H. Stone, “On one-parameter unitary groups in Hilbert space,” *Annals of Mathematics* 33 (1932), 643–648.

</div>

# Computational Evidence and Reproducibility

The numerical and machine-verifiable claims used by this paper are archived in the curated repository, `https://github.com/PeterNero/mtt-results-repro`. The mapped authority/result identifiers are `no result rows mapped`. Claim tiers in that capsule distinguish exact derivation, certified numerics, profile replay, conditional results, and open obligations.
