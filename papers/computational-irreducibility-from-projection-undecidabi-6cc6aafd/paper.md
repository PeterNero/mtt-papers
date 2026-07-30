---
abstract: |
  Projection, stable records, and threshold events do not by themselves imply algorithmic undecidability. Undecidability enters only after a dynamical realization is shown to simulate a universal machine uniformly for arbitrarily long admissible runs. This paper replaces an earlier generic claim by an auditable reachability framework. It imports, without duplicating, the conditional two-counter-machine theorem of the revised MTT Program A2 and proves four complementary results. First, a finite projection system can have noninjective descent, an absorbing record basin, and completely decidable selection. Second, undecidable reachability descends through a projection only under an effective semiconjugacy, admissibility, input, and target-fidelity contract. Third, a finite-horizon robust event is decidable once a complete positive-margin enclosure certificate is supplied. Fourth, a compact carrier cannot encode infinitely many distinct configurations with one uniform positive decoding radius; unbounded robust computation therefore requires shrinking margins, a non-totally-bounded carrier, a growing family of carriers, or another explicitly verified mechanism. We also prove that every finite trajectory prefix may be computable while unbounded target reachability is undecidable. Thus reachability undecidability is not a theorem that every trajectory is uncomputable, that no shortcut exists, or that projection creates universal computation. Current MTT has not yet supplied a selected physical embedding satisfying the complete unbounded robustness contract, so its physical selection-reachability claim remains conditional.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 9896f29fee9668a4320c3274fb0c35e3ca6bd7c3d11d9710e7be84144940454a
paper_id: computational-irreducibility-from-projection-undecidabi-6cc6aafd
release_state: zenodo_released
released_version: v2
title: |
  **Selection Reachability in Projection-Based Dynamics:**
  Conditional Undecidability, Robust Encoding, and Finite-Capacity Limits in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.21710992
zenodo_record_id: 21710992
zenodo_url: "https://zenodo.org/records/21710992"
---

# Revision note for Version 2

<div class="description">

Version 1, DOI [10.5281/zenodo.18255391](https://doi.org/10.5281/zenodo.18255391).

Version 1 inferred universal computation and undecidable selection from noninjective projection, record stability, basin structure, and finite admissibility. Its simulator construction assumed, rather than proved, unbounded counters, exact zero tests, uniform instruction fidelity, and arbitrarily long admissible persistence.

Version 2 makes the universal-machine reduction conditional on the complete Program A2 embedding contract, proves what a projection must preserve before undecidability can descend, and separates finite-horizon verification from unbounded reachability.

The distinction between chaos and algorithmic reachability, the use of a fixed universal counter machine, and the selection event as a possible target predicate remain useful once their hypotheses are typed.

No selected physical MTT carrier currently provides the full input code, step map, zero test, unbounded admissible persistence, target fidelity, and robust neighborhoods required for the conditional undecidability theorem.

</div>

This note records the release delta and is not part of the abstract.

# The corrected question

There are several mathematically different ways in which a physical model can be difficult to predict. A trajectory can be sensitive to initial data. A finite computation can be expensive. A reduced state can omit memory needed for autonomous evolution. An unbounded reachability question can be undecidable. These statements do not imply one another.

Version 1 moved too quickly between them. It treated a many-to-one projection as if it created universal computation, interpreted finite record margins as unlimited counter storage, and then described undecidable reachability as the absence of an effective dynamical law. Each step is false without additional data.

The corrected question is narrower:

> Under which explicit encoding and descent conditions does the halting problem reduce to the occurrence of a selected event in an effective physical dynamics?

This is a reachability question. It is not automatically a claim about all trajectories, all protocols, all physical theories, or the computational cost of finite prediction.

The revision has a deliberately layered role. The MTT Program A2 paper owns the conditional two-counter-machine reduction . The present paper does not rename or re-prove that theorem. It supplies the missing projection-transfer analysis, capacity obstruction, finite-horizon certificate boundary, and explanatory counterexamples.

# Four claims that must not be conflated

We use the computable admissible presentation introduced in Program A2 . In abbreviated form it consists of
``` math
\mathfrak C=(S,\iota,F,A,H),
```
where $`S`$ is an effectively represented state set, $`\iota`$ is a computable input encoder, $`F:S\rightharpoonup S`$ is a partial computable step map with an effective domain, $`A\subseteq S`$ is the admissible set, and $`H\subseteq A`$ is the selected target. The associated reachability language is
``` math
\operatorname{SEL}(\mathfrak C)
 =
 \left\{w:\exists n\geq 0,\
 F^k(\iota(w))\in A\ (0\leq k\leq n),\
 F^n(\iota(w))\in H\right\}.
```
Program A2 proves that this language is recursively enumerable under its declared presentation and states the additional hypotheses needed for decidability and undecidability. Those results are imported here.

<div class="definition">

**Definition 1** (Claim ladder). For one declared presentation, distinguish:

1.  *step computability*: $`F(s)`$ can be computed when it is defined;

2.  *bounded reachability*: a target query is decided up to a supplied finite horizon;

3.  *unbounded reachability*: membership in $`\operatorname{SEL}(\mathfrak C)`$ is decidable or undecidable;

4.  *complexity*: a total task has a lower bound in a specified machine model and size measure;

5.  *computational irreducibility*: a separately defined class of shortcut predictors fails on a specified family of instances.

</div>

The ladder is not a chain of implications. In particular, a computable one-step rule can have undecidable unbounded reachability, and an undecidable language does not by itself state a runtime lower bound for a total decider, because no such decider exists.

<div class="remark">

*Remark 2* (Robustness is another quantifier). A robust event may mean that every initial point in a neighborhood reaches the same target at the same step, that each point reaches it at some possibly different step, or that a probability exceeds a threshold. These are different languages. A paper must select one convention and provide an effective representation of the quantified neighborhood.

</div>

# Projection does not create undecidability

The Projection–Admissibility Principle distinguishes descent from recovery . Information loss under descent is a structural fact. Computational universality is a property of a specified transition system. The following elementary example separates them.

<div id="prop:counterexample" class="proposition">

**Proposition 3** (Decidable noninjective projection). *There is a finite system with a noninjective projection, an absorbing stable record basin, and selection reachability decidable in one step.*

</div>

<div class="proof">

*Proof.* Let the source state space be $`Y=\{0,1\}^2`$, the effective state space be $`X=\{0,1\}`$, and define
``` math
P(a,b)=a,\qquad G(a,b)=(0,b),\qquad F(a)=0.
```
Then $`P`$ is noninjective and
``` math
P\circ G=F\circ P.
```
Take $`A=X`$ and $`H=\{0\}`$. The target is absorbing. Every effective state is in $`H`$ initially or enters $`H`$ after one step, so the selection language is the full input language and is decidable. A finite product of copies with componentwise dynamics gives the same conclusion for a local finite-lattice model. ◻

</div>

The counterexample does not say that projection is irrelevant. It says that projection needs a fidelity contract before a computational property can pass through it.

## The descent-transfer theorem

Let
``` math
\mathfrak C_Y=(S_Y,\iota_Y,G,A_Y,H_Y),
\qquad
\mathfrak C_X=(S_X,\iota_X,F,A_X,H_X)
```
be computable admissible presentations. Think of $`Y`$ as an upper or source description and $`X`$ as an effective description.

<div id="def:descent" class="definition">

**Definition 4** (Effective reachability descent). An effective reachability descent from $`\mathfrak C_Y`$ to $`\mathfrak C_X`$ on an invariant encoded set $`E\subseteq S_Y`$ consists of computable maps $`P:E\to S_X`$, $`u`$ on source inputs, and $`g`$ on target inputs such that:

1.  $`\iota_Y(u(w))\in E`$ and $`P(\iota_Y(u(w)))=\iota_X(g(w))`$;

2.  $`G(E)\subseteq E`$ wherever $`G`$ is defined;

3.  $`P(Gy)=F(Py)`$ for every relevant $`y\in E`$;

4.  $`y\in A_Y`$ if and only if $`Py\in A_X`$, on the encoded orbits;

5.  $`y\in H_Y`$ if and only if $`Py\in H_X`$, on the encoded orbits.

</div>

<div id="thm:transfer" class="theorem">

**Theorem 5** (Reachability transfer through projection). *If Definition <a href="#def:descent" data-reference-type="ref" data-reference="def:descent">4</a> holds, then for every declared input $`w`$,
``` math
u(w)\in\operatorname{SEL}(\mathfrak C_Y)
 \quad\Longleftrightarrow\quad
 g(w)\in\operatorname{SEL}(\mathfrak C_X).
```
Consequently, if a language $`L`$ many-one reduces to $`\operatorname{SEL}(\mathfrak C_Y)`$ through $`u`$, then
``` math
L\leq_m\operatorname{SEL}(\mathfrak C_X)
```
through $`g`$.*

</div>

<div class="proof">

*Proof.* Condition (D1) identifies the initial states. Conditions (D2) and (D3), by induction on $`n`$, give
``` math
P\!\left(G^n(\iota_Y(u(w)))\right)
 =
 F^n(\iota_X(g(w)))
```
for every finite encoded prefix. Condition (D4) preserves exactly the prefixes that count as admissible, and (D5) preserves exactly the target hits. The two reachability statements are therefore equivalent. Composition with the source reduction proves the final claim. ◻

</div>

<div class="remark">

*Remark 6*. Noninjectivity of $`P`$ away from $`E`$ is compatible with the theorem. What matters is not invertibility of the whole projection but preservation of the encoded orbit, the admissibility predicate, and the target predicate. If $`P`$ collapses the halting and nonhalting codes together, the reduction is destroyed rather than created.

</div>

# Finite horizons and robust certificates

Version 1 defined an instance-dependent finite admissible horizon and then asserted that finiteness did not restore decidability. That conclusion does not follow. A known computable horizon and decidable step predicates give a finite search. Conversely, merely naming a semantic $`N_{\max}`$ does not supply an algorithm for finding it.

For continuous or uncertain initial data, one also needs certified set propagation. The next result states a finite checker contract without pretending that every nonlinear model automatically emits it.

<div id="def:packet" class="definition">

**Definition 7** (Positive-margin enclosure packet). Let $`X`$ be a metric state space, $`K_0\subseteq A`$ a compact preparation set, $`F`$ the selected step map, $`H\subseteq A`$ an absorbing target, and $`N<\infty`$. A positive-margin enclosure packet consists of sets $`E_0,\ldots,E_N`$ and machine-checkable rational bounds satisfying:

1.  $`K_0\subseteq E_0`$ and $`F(E_k)\subseteq E_{k+1}`$ for $`k<N`$;

2.  $`\operatorname{dist}(E_k,X\setminus A)\geq a_k>0`$ for every $`k\leq N`$;

3.  for every $`k\leq N`$, exactly one certified row is supplied:
    ``` math
    \textsc{hit}: \operatorname{dist}(E_k,X\setminus H)\geq h_k>0,
    \quad\text{or}\quad
    \textsc{miss}: \operatorname{dist}(E_k,H)\geq m_k>0.
    ```

</div>

<div id="prop:finite" class="proposition">

**Proposition 8** (Finite-horizon robust decision). *A valid packet from Definition <a href="#def:packet" data-reference-type="ref" data-reference="def:packet">7</a> decides whether all preparations in $`K_0`$ enter the absorbing target $`H`$ by step $`N`$.*

</div>

<div class="proof">

*Proof.* Condition (V1) encloses every propagated preparation and (V2) keeps every enclosed prefix admissible. A <span class="smallcaps">hit</span> row at step $`k`$ places all propagated states inside $`H`$, so the answer is yes. If every row through $`N`$ is <span class="smallcaps">miss</span>, no propagated state has entered $`H`$, so the answer is no. Absorption makes a hit by an earlier, preparation-dependent time visible as a common hit at the final step. ◻

</div>

This proposition is intentionally a certificate theorem. It does not say that the required enclosures or strict distances are easy to compute. If an image touches $`\partial A`$ or $`\partial H`$, the positive-margin promise fails and the packet is incomplete. The correct output is then *unresolved at this precision*, not “undecidable.” Interval arithmetic, semialgebraic decision procedures, abstract interpretation, or model-specific barrier certificates may provide the rows in particular systems.

# The imported conditional A2 theorem

The corrected Program A2 theorem uses one fixed universal two-counter machine with configurations $`Q\times\mathbb{N}^2`$ . Its robust uniform embedding contract has six indispensable rows:

<div class="center">

<div class="tabularx">

0.94

@\>

p0.20Y@

Row & Required content
Input code & A computable injection of machine configurations and a computable map from finite machine inputs to physical initial data.
Step fidelity & One selected physical step implements increment, decrement/zero-test, branch, and halt on every encoded run.
Unbounded persistence & Every finite prefix of every encoded run stays in the domain and remains admissible; there is no fixed global counter cap.
Target fidelity & The selected event occurs exactly for halting configurations.
Uniformity & Dynamics, target, decoder, and protocol are fixed independently of the input.
Robustness & Computable positive neighborhoods preserve labels, steps, and target membership.

</div>

</div>

Program A2 proves the following imported implication:
``` math
\boxed{
\text{complete robust uniform embedding}
\ \Longrightarrow\
\operatorname{HALT}_{\mathcal M}\leq_m\operatorname{SEL}(\mathfrak C)
}
```
and therefore conditional undecidability of selection reachability. The proof is the standard finite-prefix simulation followed by target fidelity. It is not repeated here, preserving theorem ownership in Program A2.

The force of the theorem lies in its antecedent. Projection, non-Markovianity, finite margins, locality, or the existence of records supplies none of the six rows automatically. Smooth and even analytic dynamical systems can be constructed to simulate Turing machines ; those results demonstrate possibility, not genericity and not selection by MTT.

# A compact uniform-robustness obstruction

The old record-register construction assumed a countable collection of stable sites while also speaking as though one fixed finite capacity and one uniform stability margin were sufficient. Compactness exposes the conflict.

<div class="definition">

**Definition 9** (Decoded robust code). Let $`K`$ be a metric carrier and $`\mathcal C`$ a set of symbolic configurations. A decoded robust code consists of points $`x_c\in K`$, radii $`\delta_c>0`$, and a single-valued decoder
``` math
D:\bigcup_{c\in\mathcal C}B(x_c,\delta_c)\longrightarrow\mathcal C
```
such that $`D(x)=c`$ throughout $`B(x_c,\delta_c)`$.

</div>

<div id="thm:packing" class="theorem">

**Theorem 10** (Compact uniform-margin obstruction). *If $`K`$ is compact, then for every $`r>0`$ only finitely many distinct configurations can satisfy $`\delta_c\geq r`$. In particular, an infinite configuration set cannot have
``` math
\inf_{c\in\mathcal C}\delta_c>0.
```*

</div>

<div class="proof">

*Proof.* For distinct $`c,d`$, the decoding neighborhoods are disjoint; otherwise the single-valued decoder would assign two labels to one point. Fix $`r>0`$ and consider all $`c`$ with $`\delta_c\geq r`$. Their centers are $`r`$-separated: if $`d(x_c,x_d)<r`$, then $`x_d`$ belongs to both $`B(x_c,\delta_c)`$ and $`B(x_d,\delta_d)`$, a contradiction.

Compact metric spaces are totally bounded. Cover $`K`$ by finitely many balls of radius $`r/2`$. Each such ball contains at most one center from an $`r`$-separated set. Hence only finitely many of the configurations can have radius at least $`r`$. A uniform positive lower bound would contradict this for an infinite configuration set. ◻

</div>

<div id="cor:options" class="corollary">

**Corollary 11** (Options for unbounded counters). *A robust encoding of two unbounded counters must use at least one of the following:*

1.  *decoding radii that approach zero along some configurations;*

2.  *a carrier that is not totally bounded;*

3.  *a uniformly specified family of growing carriers; or*

4.  *a different encoding whose robustness is proved without one uniform locally constant decoder margin.*

</div>

The theorem is deliberately limited. It does not say that compact smooth systems cannot simulate Turing machines. Indeed, Graça and Zhong construct a smooth simulation on a compact sphere . It says that one must inspect the exact encoding and robustness quantifiers: compactness is incompatible with infinitely many disjoint code cells of one fixed positive radius. Shrinking cells or another coding mechanism evade that particular obstruction but introduce a precision obligation that a physical claim must address.

# Computable trajectories can have undecidable reachability

The phrase “no effective law exists” in Version 1 was stronger than the reduction supports.

<div id="prop:prefix" class="proposition">

**Proposition 12** (Finite prefixes versus unbounded reachability). *There is a fixed total computable step map for which every finite orbit prefix is computable, while target reachability over all time is undecidable.*

</div>

<div class="proof">

*Proof.* Fix a universal Turing machine and encode its configurations as finite strings. Let $`\tau`$ be its computable one-step transition, extended by a self-loop on halting configurations. Given an input $`w`$ and $`n`$, the state $`\tau^n(c_0(w))`$ is computable by $`n`$ iterations. Thus every finite prefix is computable. If an algorithm decided whether some iterate entered the halting set, it would decide the halting problem, contradicting Turing’s theorem . ◻

</div>

The proposition locates the obstruction in the unbounded existential quantifier over $`n`$, not in the local update law. Moore’s dynamical-systems constructions make the same distinction concrete in continuous settings .

## What “computational irreducibility” would still require

Undecidable reachability is already a precise and strong statement. It should not be inflated into three other statements:

- It does not prove that every trajectory is difficult; many inputs may halt immediately or enter a simple cycle.

- It does not prove that each finite state requires step-by-step simulation; a special family may admit a closed form or shortcut.

- It does not provide a complexity lower bound without a total prediction task, input-size convention, machine model, and comparison class.

A future MTT irreducibility theorem would therefore need to name a total finite task, a family of selected instances, a resource measure, and a class of allowed shortcut algorithms. The conditional Program A2 theorem establishes none of those complexity claims, nor does it purport to.

# What the external literature establishes

The relevant literature supports a conditional, model-specific conclusion. Hybrid and continuous systems can carry universal computation, but reachability also has broad decidable subclasses.

<div class="center">

<div class="tabularx">

0.96@p0.23YY@ Result & What it establishes & What it does not establish
Turing and Minsky & Universal discrete machines and undecidable halting/reachability & A physical realization or robustness under perturbations
Moore & Explicit dynamical systems whose long-run questions encode computation & Generic undecidability of smooth dynamics
Branicky & Universal computation in specified hybrid and ODE constructions & Universality from projection alone
Henzinger et al. & Precise decidable and undecidable reachability boundaries for hybrid automata & One verdict for every hybrid system
Graça et al. & Explicit analytic or polynomial robust simulations, including bounded noise & Selection of those dynamics by MTT
Graça–Zhong & Low-dimensional robust analytic simulation and a smooth compact-sphere construction & A uniform positive decoding radius for infinitely many labels

</div>

</div>

The literature therefore strengthens the corrected paper in two ways. It shows that a robust embedding is mathematically plausible, and it shows why the embedding must be constructed rather than inferred. The decidability frontier changes when guards, resets, dimensions, noise models, and encoding conventions change .

# Current MTT status

MTT currently provides several relevant but separate layers:

1.  Foundations defines closure, admissibility, and typed claim boundaries .

2.  Projection–Admissibility distinguishes descent, information loss, and recovery .

3.  Program A2 supplies the computable-presentation language, finite-depth results, finite-capacity no-go, and the exact conditional universal-machine reduction .

4.  The measurement paper distinguishes physical disturbance, outcome completion, and record stabilization .

5.  The conditional-classification paper prevents projection, event, ultraviolet, and matter claims from being inferred across incomplete witness axes .

What is not currently selected is one physical realization satisfying all six A2 embedding rows on the same source. Finite basin models and finite event logs can demonstrate bounded simulation. They do not prove unbounded admissible persistence. A countable record register written into prose is not a selected carrier. A threshold metaphor is not an exact zero-test operator. A stability margin for each finite experiment is not a uniform or controlled family of margins over arbitrary counter values.

Accordingly, this paper makes no promotion of the physical MTT proof tier. Its new exact results are mathematical audit tools: the descent theorem identifies what projection must preserve, and the compactness theorem identifies one capacity/robustness obstruction.

# The certificate required for a physical theorem

A future selected MTT undecidability claim should be accompanied by one hash-addressed certificate with at least the following fields:

    carrier_id, carrier_domain, state_representation,
    input_encoder, configuration_decoder,
    selected_step_operator, admissible_domain,
    increment_map, decrement_map, zero_test,
    halting_target, projection_map,
    semiconjugacy_verifier, target_fidelity_verifier,
    prefix_persistence_theorem, robustness_radii,
    precision_model, source_hashes, proof_status

The packet must answer concrete questions.

1.  Is the carrier fixed for all inputs, or is there a uniform growing family?

2.  Can every finite machine prefix be represented without leaving the selected admissible domain?

3.  Are increment, decrement, and zero-test operations generated by one fixed selected dynamics rather than an input-dependent controller?

4.  Does the physical projection satisfy Theorem <a href="#thm:transfer" data-reference-type="ref" data-reference="thm:transfer">5</a> on the encoded subset?

5.  Are robustness radii uniform, shrinking, or controlled by a proved precision law?

6.  Does the target event represent halting in both directions?

Any failed row is informative. Failure of unbounded persistence leaves a finite simulator. Failure of target fidelity invalidates the reduction. Failure of robustness leaves an exact-code construction that may be physically unstable. Failure of semiconjugacy means the projected event language need not inherit the source computation.

# Completion and falsifiability

The corrected framework can fail cleanly.

1.  A proposed projection identifies a halting and nonhalting encoded orbit, violating target fidelity.

2.  The counter code reaches a fixed capacity or an admissibility boundary.

3.  Zero testing requires precision smaller than the declared physical tolerance.

4.  The protocol or transition rule depends on the encoded program, so the claimed fixed universal dynamics is not uniform.

5.  Robust neighborhoods overlap while carrying distinct labels.

6.  A finite-horizon claim lacks a positive-margin enclosure packet.

7.  A claimed complexity or irreducibility theorem lacks a total task and resource model.

Conversely, completing the six A2 rows and the descent contract would justify a substantial theorem: one selected MTT event-reachability language would be undecidable. It still would not imply that every MTT process is universal or that all finite predictions require literal simulation.

# Conclusion

Projection is not an engine of undecidability. It can erase a computation, preserve one, or transfer its reachability language, depending on the maps and predicates it respects. Stable records provide possible symbolic carriers, but they do not supply unbounded counters, zero tests, or universal dynamics. Finite admissibility can support verified finite simulations; it cannot be silently promoted to unlimited machine execution.

The corrected result is therefore both smaller and stronger. Program A2 owns the exact conditional reduction. This paper proves the descent contract needed to apply it through a projection, gives a decidable projection counterexample, supplies a finite-horizon certificate theorem, and proves a compact uniform-margin obstruction. It also makes explicit that computable finite trajectories and undecidable unbounded reachability coexist.

For MTT, the frontier is now unambiguous: construct one selected physical carrier and operator satisfying the complete robust embedding and descent certificate, or retain the valuable but finite simulation tier. Until that construction exists, selection undecidability is a conditional mathematical possibility, not a derived universal property of reality.
