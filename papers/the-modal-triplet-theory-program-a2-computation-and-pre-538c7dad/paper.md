---
abstract: |
  We analyze limits of computation, prediction, and control that arise as structural consequences of admissible description in the Modal Triplet Theory (MTT) framework. Without invoking complexity theory, algorithmic randomness, or resource constraints, we show that finite admissibility, kinematic persistence, and selection fronts impose intrinsic limits on what can be predicted or decided within any admissible encoding.

  We introduce the notion of admissible prediction depth and show that, in the presence of selection fronts and nil obstructions, well-posed questions about future kinematic continuation can be undecidable within the theory. These limits are structural rather than epistemic: they persist even with infinite computational power and perfect local information.

  The results clarify the relationship between physical prediction, computation, and description. They show that undecidability and loss of predictability arise from the same structural sources as irreversibility, horizons, and quantization, and do not require additional postulates about information or observers.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 4b72d576a13c75e79f613ce8c74eaefc8f37ee216397389ad622ac931ca82fb4
paper_id: the-modal-triplet-theory-program-a2-computation-and-pre-538c7dad
release_state: zenodo_released
released_version: v1.0
title: |
  The Modal Triplet Theory Program A2:  
  Computation and Predictive Limits  
  in the Modal Triplet Theory Program
zenodo_doi: 10.5281/zenodo.18354966
zenodo_record_id: 18354966
zenodo_url: "https://zenodo.org/records/18354966"
---

# Introduction and Scope

The structural core of Modal Triplet Theory establishes that reduced descriptions are local, that global coherence is generically obstructed, and that admissible descriptions are constrained by overlap consistency and refinement stability. Coherent kinematics then defines motion, causality, horizons, and irreversibility without assuming spacetime or dynamics. Subsequent papers identify gravity, gauge structure, and quantization as encoding responses forced by specific obstruction types.

The purpose of the present paper is to analyze the consequences of these structural features for computation and prediction. We ask a simple but fundamental question:

> *What can be predicted, computed, or decided within a framework in which descriptions are local, admissibility is finite, and kinematic continuation may terminate?*

We show that the answer is: *not everything that is well-defined*. Even questions that are sharply posed in the kinematic framework may lack definite answers within any admissible encoding. These limitations arise not from lack of data, computational resources, or noise, but from the structure of admissible description itself.

The analysis in this paper relies only on:

- the structural core of Modal Triplet Theory;

- coherent kinematics and admissible continuation;

- the existence of selection fronts and nil obstructions.

No assumptions are made about:

- algorithmic complexity;

- probabilistic computation;

- observers or measurement postulates;

- computational resources.

The resulting limits are therefore intrinsic to the theory and apply to all realization classes compatible with the MTT framework.

<div class="remark">

*Remark 1* (Position in the series). This paper belongs to the A-layer of the Modal Triplet Theory Program. It derives structural consequences of admissibility and kinematics, but introduces no new encoding classes. It precedes and motivates interpretive papers on the dark sector and complements the encoding-class papers on gravity, gauge, and quantization.

</div>

# Prediction as Admissible Continuation

In the Modal Triplet Theory framework, prediction is not defined as extrapolation of a state in time, but as determination of admissible continuation of coherent structure across overlapping encodings. In this section we formalize prediction accordingly.

## Predictive questions

A predictive question concerns the future continuation of a coherent structure.

<div class="definition">

**Definition 2** (Predictive question). A *predictive question* is a well-posed query of the form:

> Given a coherent structure represented in an admissible encoding $`\mathcal E_\alpha`$, does admissible continuation exist to a specified set of encodings $`\{\mathcal E_\beta\}`$?

</div>

Predictive questions are therefore questions about the existence and properties of continuation chains, not about numerical values at future times.

## Prediction without global time

Because there is no global time parameter in the kinematic framework, prediction is inherently relational.

<div class="remark">

*Remark 3*. Prediction does not require an external notion of time. The ordering relevant to prediction is the kinematic ordering induced by admissible continuation, as defined in coherent kinematics.

</div>

This distinguishes prediction from time-evolution in classical dynamical systems.

## Admissible prediction

We now define prediction formally.

<div class="definition">

**Definition 4** (Admissible prediction). An *admissible prediction* is the determination, within an admissible encoding, of whether a given predictive question has a definite answer under all admissible refinements of the encoding atlas.

</div>

An admissible prediction must be stable under refinement; otherwise it does not constitute a well-defined prediction in the MTT sense.

## Prediction versus simulation

Simulation is not prediction in this framework.

<div class="remark">

*Remark 5*. A simulation may generate particular continuation chains under specific choices of encoding or gauge, but such results are not admissible predictions unless they are invariant under all admissible refinements. Prediction is therefore strictly stronger than simulation.

</div>

This distinction will be crucial when discussing undecidability.

## Determinacy and indeterminacy

We now distinguish deterministic from indeterminate predictive questions.

<div class="definition">

**Definition 6** (Determinately predictable question). A predictive question is *determinately predictable* if all admissible continuation chains compatible with the initial encoding yield the same answer.

</div>

<div class="definition">

**Definition 7** (Indeterminate predictive question). A predictive question is *indeterminate* if admissible continuation chains yield different answers, or if admissible continuation terminates before the question can be resolved.

</div>

Indeterminacy here is structural and does not imply randomness.

## Sources of predictive indeterminacy

There are two primary sources of indeterminacy.

- **Branching at selection fronts:** multiple admissible continuations exist, leading to different outcomes.

- **Termination at nil obstructions:** continuation ceases before the question can be resolved.

Both sources arise from admissibility constraints, not from lack of information.

## No global predictive map

We now state a basic limitation.

<div class="theorem">

**Theorem 8** (No global predictive map). *There exists no globally defined map assigning definite answers to all predictive questions consistent with admissible continuation.*

</div>

<div class="proof">

*Proof.* A global predictive map would require a global encoding capable of resolving all continuation questions. This contradicts finite admissibility and the existence of nil obstructions. ◻

</div>

## Preview: prediction depth

Prediction may be possible locally even when global prediction fails.

<div class="remark">

*Remark 9*. The extent to which prediction remains possible before encountering branching or termination is quantified by admissible prediction depth, introduced in the next section.

</div>

# Admissible Prediction Depth

In this section we quantify the extent to which prediction remains possible within the Modal Triplet Theory framework. We introduce the notion of admissible prediction depth, which measures how far admissible continuation can proceed before encountering branching or termination that renders prediction indeterminate.

## Local versus global predictability

Although global prediction is impossible, local prediction may remain viable for finite extents.

<div class="remark">

*Remark 10*. The absence of a global predictive map does not imply that all predictive questions are indeterminate. Rather, predictability is local and bounded, and its limits are determined by admissibility structure.

</div>

This motivates a quantitative notion of predictive reach.

## Definition of prediction depth

We now define prediction depth intrinsically.

<div class="definition">

**Definition 11** (Admissible prediction depth). Let $`\mathcal E_\alpha`$ be an admissible encoding representing a coherent structure. The *admissible prediction depth* $`D(\mathcal E_\alpha)`$ is the supremum of lengths of admissible continuation chains starting at $`\mathcal E_\alpha`$ such that all predictive questions along those chains are determinately predictable.

</div>

The length of a continuation chain is measured by the number of admissible continuation steps, not by time or distance.

## Finite prediction depth

Finite admissibility implies that prediction depth is generically finite.

<div class="theorem">

**Theorem 12** (Finite prediction depth). *For any admissible encoding $`\mathcal E_\alpha`$, the admissible prediction depth $`D(\mathcal E_\alpha)`$ is finite whenever selection fronts or nil obstructions exist in its kinematic reach.*

</div>

<div class="proof">

*Proof.* Selection fronts introduce branching of admissible continuation, rendering predictive questions indeterminate beyond the front. Nil obstructions terminate continuation entirely. In either case, continuation chains of arbitrary length cannot remain determinately predictable. Therefore $`D(\mathcal E_\alpha)`$ is finite. ◻

</div>

## Dependence on initial encoding

Prediction depth depends on where one starts in the encoding atlas.

<div class="remark">

*Remark 13*. Different admissible encodings may have different prediction depths, even when representing the same underlying coherent structure. Prediction depth is thus an encoding-relative quantity.

</div>

This dependence reflects the absence of a privileged global encoding.

## Refinement stability

Prediction depth is stable under admissible refinement.

<div class="lemma">

**Lemma 14**. *Admissible refinement of the encoding atlas does not increase prediction depth.*

</div>

<div class="proof">

*Proof.* Refinement may reveal additional selection fronts or nil obstructions, but cannot eliminate existing ones. Therefore refinement can only decrease or preserve prediction depth, not increase it. ◻

</div>

This monotonicity is essential for the structural nature of prediction limits.

## Prediction depth versus computational power

Prediction depth is not a resource limitation.

<div class="remark">

*Remark 15*. Finite prediction depth persists even with unlimited computational resources and perfect local information. It reflects structural limits on admissible continuation, not algorithmic complexity or computational cost.

</div>

## Local predictability regions

Despite finite depth, extended regions of predictability may exist.

<div class="definition">

**Definition 16** (Predictability region). A *predictability region* is a subset of the encoding atlas in which admissible prediction depth exceeds a specified threshold.

</div>

Such regions correspond to regimes in which effective theories appear deterministic over extended extents.

## Preview: undecidability

Finite prediction depth implies that certain predictive questions cannot be decided within the theory.

<div class="remark">

*Remark 17*. In the next section we show that, in the presence of branching and termination, there exist well-posed predictive questions that are undecidable within any admissible encoding, independently of computational power.

</div>

# Undecidability of Kinematic Questions

In this section we show that finite admissible prediction depth implies the existence of well-posed predictive questions that are undecidable within the Modal Triplet Theory framework. This undecidability is structural rather than computational: it persists even with unlimited computational resources and perfect local information.

## Well-posed kinematic questions

We begin by clarifying what is meant by undecidability in this context.

<div class="definition">

**Definition 18** (Well-posed kinematic question). A *well-posed kinematic question* is a predictive question whose statement is invariant under admissible re-encoding and refinement of the encoding atlas.

</div>

Such questions are unambiguous and meaningful within the theory.

## Decidability within an admissible encoding

Decidability is defined relative to admissible encodings.

<div class="definition">

**Definition 19** (Decidable predictive question). A well-posed kinematic question is *decidable* if there exists an admissible procedure, definable within the encoding framework, that yields a definite answer in finite admissible continuation steps.

</div>

A question that fails this criterion is undecidable.

## Undecidability from branching

Selection fronts induce branching of admissible continuation.

<div class="lemma">

**Lemma 20**. *If a predictive question depends on which branch of a selection front is taken, then it is undecidable.*

</div>

<div class="proof">

*Proof.* At a selection front, multiple admissible continuation chains exist, yielding different outcomes. No admissible refinement can select a unique continuation without violating admissibility. Therefore no admissible procedure can determine the outcome uniquely. ◻

</div>

## Undecidability from termination

Nil obstructions induce termination of continuation.

<div class="lemma">

**Lemma 21**. *If a predictive question requires continuation beyond a nil obstruction to be resolved, then it is undecidable.*

</div>

<div class="proof">

*Proof.* By definition, no admissible continuation exists beyond a nil obstruction. Therefore no admissible procedure can evaluate the question. ◻

</div>

## Existence of undecidable questions

We now state the main result of this section.

<div class="theorem">

**Theorem 22** (Structural undecidability). *In the presence of selection fronts or nil obstructions, there exist well-posed kinematic questions that are undecidable within any admissible encoding.*

</div>

<div class="proof">

*Proof.* By finite prediction depth, there exists a bound beyond which determinately predictable continuation fails. Construct a question whose resolution requires continuation beyond this bound. By the preceding lemmas, such a question is undecidable. ◻

</div>

## Independence from computational power

We emphasize the nature of this undecidability.

<div class="remark">

*Remark 23*. The undecidability established here does not arise from computational complexity or algorithmic limitations. It persists even if the computational agent has unlimited resources and perfect access to local encoding data. The obstruction lies in admissibility, not in computation.

</div>

## Relation to classical undecidability

This structural undecidability is distinct from, but compatible with, classical notions.

<div class="remark">

*Remark 24*. Classical undecidability results (e.g. Turing undecidability) concern limits of formal computation. The present result concerns limits of physical prediction imposed by admissible description. The two notions may coincide in specific realizations, but neither reduces to the other.

</div>

## Scope of undecidable questions

Not all predictive questions are undecidable.

<div class="remark">

*Remark 25*. Undecidability arises only for questions whose resolution depends on continuation across selection fronts or nil obstructions. Many local questions remain decidable within finite predictability regions.

</div>

## Preview: limits of control

Undecidability has direct implications for control and intervention.

<div class="remark">

*Remark 26*. In the next section we show that structural undecidability also limits the extent to which coherent structures can be controlled or steered by admissible interventions.

</div>

# Limits of Control and Intervention

In this section we analyze the consequences of finite admissible prediction depth and structural undecidability for control and intervention. We show that limits on prediction imply corresponding limits on the ability to steer, regulate, or force outcomes within the Modal Triplet Theory framework.

## Control as constrained intervention

We first define what is meant by control in an encoding-relative setting.

<div class="definition">

**Definition 27** (Admissible intervention). An *admissible intervention* is a modification of the encoding conditions or initial representation that is itself admissible and preserves overlap consistency and refinement stability.

</div>

Interventions are therefore subject to the same admissibility constraints as descriptions.

<div class="definition">

**Definition 28** (Control problem). A *control problem* is a specification of a desired property of future admissible continuation, together with a proposed admissible intervention intended to enforce that property.

</div>

Control is meaningful only insofar as the outcome of the intervention is predictable.

## Dependence of control on prediction

We now establish the dependence of control on prediction.

<div class="lemma">

**Lemma 29**. *If a predictive question associated with a control problem is undecidable, then the control problem is not solvable within any admissible encoding.*

</div>

<div class="proof">

*Proof.* A control problem requires determining whether an intervention will enforce a desired outcome. If the corresponding predictive question is undecidable, no admissible procedure can establish that the intervention succeeds. Therefore the control problem is unsolvable within the theory. ◻

</div>

Thus, undecidability directly limits control.

## Control failure at selection fronts

Selection fronts introduce intrinsic limits on intervention.

<div class="lemma">

**Lemma 30**. *No admissible intervention can deterministically select a unique branch at a selection front without violating admissibility.*

</div>

<div class="proof">

*Proof.* At a selection front, multiple admissible continuation branches exist. Any intervention that forces one branch while excluding others would render the excluded branches inadmissible, contradicting admissibility constraints. Hence no admissible intervention can enforce deterministic selection. ◻

</div>

This establishes that branching cannot be controlled away.

## Control failure at nil obstructions

Nil obstructions impose even stronger limits.

<div class="lemma">

**Lemma 31**. *No admissible intervention can enforce continuation beyond a nil obstruction.*

</div>

<div class="proof">

*Proof.* By definition of nil obstruction, no admissible encoding exists beyond the obstruction. Any intervention attempting to enforce continuation would require introducing an inadmissible description. Therefore such intervention is forbidden. ◻

</div>

Thus termination is uncontrollable.

## Local versus global control

Control may remain possible in restricted regimes.

<div class="remark">

*Remark 32*. Within predictability regions of finite but nonzero prediction depth, admissible interventions may influence outcomes locally. However, such control is always bounded by the nearest selection front or nil obstruction.

</div>

This explains why effective control appears possible in many physical systems despite fundamental limits.

## No universal control strategy

We now state the global limitation.

<div class="theorem">

**Theorem 33** (No universal control strategy). *There exists no admissible intervention strategy that can enforce arbitrary desired outcomes across all admissible continuation chains.*

</div>

<div class="proof">

*Proof.* A universal control strategy would require resolving all predictive questions and overriding all branching and termination behavior. This contradicts the existence of undecidable predictive questions and nil obstructions established earlier. ◻

</div>

## Control versus determinism

The limits of control do not imply lack of determinism.

<div class="remark">

*Remark 34*. Failure of control does not imply indeterministic dynamics. It reflects limits on what can be enforced or steered within admissible description. Deterministic behavior may exist locally even where control fails globally.

</div>

## Implications

The structural limits on control have broad implications.

<div class="remark">

*Remark 35*. These results imply that no observer, agent, or apparatus—regardless of capability—can bypass admissibility constraints to enforce outcomes beyond prediction depth. Limits of control are therefore as fundamental as limits of prediction.

</div>

## Preview: relation to quantization and horizons

Limits of control are closely related to other structural features.

<div class="remark">

*Remark 36*. Selection fronts, horizons, and quantization boundaries represent points at which control necessarily fails. These features are unified by the admissibility structure of the theory.

</div>

# Relation to Quantization and Probability

In this section we relate the limits of prediction and control derived above to the discrete constraint encoding identified as quantization and to the conditional notion of probability developed in the Modal Triplet Theory framework. We show that predictive limits, undecidability, and quantization are not independent phenomena, but manifestations of the same admissibility structure.

## Prediction depth and discrete survivors

Finite admissible prediction depth implies that continuation eventually encounters selection fronts or nil obstructions.

<div class="remark">

*Remark 37*. When admissible prediction depth is exhausted due to a nil obstruction, only discrete survivors remain admissible. Thus the boundary of predictability coincides with the boundary at which quantization becomes structurally relevant.

</div>

Prediction therefore transitions from deterministic continuation to discrete classification.

## Undecidability and quantization

Undecidable predictive questions are closely tied to discrete constraint encoding.

<div class="lemma">

**Lemma 38**. *If a predictive question is undecidable due to termination at a nil obstruction, then its resolution, if any, must be expressed in terms of discrete survivors.*

</div>

<div class="proof">

*Proof.* Termination of admissible continuation implies that no further continuous description is possible. Any remaining descriptive content must therefore be drawn from discrete survivors selected by stability under refinement. ◻

</div>

This shows that undecidability and quantization share a common structural origin.

## Probability as a secondary structure

Probability does not resolve undecidability.

<div class="remark">

*Remark 39*. The introduction of probability does not convert undecidable predictive questions into decidable ones. Probability assigns weights to discrete survivors when invariant measures exist, but it does not extend admissible prediction depth or restore lost continuation.

</div>

Thus probability is subordinate to admissibility and quantization.

## Conditional probabilistic prediction

Probabilistic prediction is possible only under additional conditions.

<div class="definition">

**Definition 40** (Probabilistic predictive question). A predictive question is *probabilistically predictive* if:

1.  admissible continuation terminates at a discrete survivor set $`\mathcal S`$;

2.  an invariant measure exists on $`\mathcal S`$.

</div>

In this case, prediction yields a probability distribution rather than a deterministic outcome.

## No probabilistic control beyond nil

Probability does not restore control.

<div class="lemma">

**Lemma 41**. *Probabilistic weighting of discrete survivors does not permit admissible control beyond selection fronts or nil obstructions.*

</div>

<div class="proof">

*Proof.* Probabilistic weighting assigns likelihoods to outcomes but does not alter which outcomes are admissible. Therefore it cannot enforce or exclude specific continuations beyond the admissibility boundary. ◻

</div>

This reinforces the structural nature of control limits.

## Relation to measurement

Measurement outcomes are discrete and terminal.

<div class="remark">

*Remark 42*. Measurement, understood as selection among discrete survivors, coincides with the exhaustion of admissible prediction depth. The unpredictability of outcomes reflects undecidability of continuation, not lack of information.

</div>

## Unified perspective

We now summarize the unified picture.

<div class="remark">

*Remark 43*. Finite admissibility implies finite prediction depth. Finite prediction depth implies undecidability of certain kinematic questions. Termination of predictability implies collapse to discrete survivors. Discrete survivors are organized by quantization. Probability appears only conditionally when invariant measures exist. These are not separate assumptions but consequences of the same structural constraints.

</div>

# Summary and Outlook

In this paper we have analyzed limits of computation, prediction, and control as structural consequences of admissible description in the Modal Triplet Theory framework. Without invoking complexity theory, algorithmic randomness, or resource constraints, we showed that finite admissibility, coherent kinematics, and selection fronts impose intrinsic limits on what can be predicted or decided within any admissible encoding.

Prediction was defined as determination of admissible continuation rather than as time evolution. We showed that although local prediction may be possible within restricted regions of the encoding atlas, admissible prediction depth is generically finite. Selection fronts induce branching of admissible continuation, while nil obstructions terminate continuation entirely. Both mechanisms render certain well-posed kinematic questions undecidable within the theory.

We further demonstrated that undecidability implies corresponding limits on control and intervention. No admissible intervention can deterministically select among branches at a selection front or enforce continuation beyond a nil obstruction. These limits are structural rather than epistemic: they persist even with unlimited computational power and perfect local information.

The results clarify the relationship between predictive limits, quantization, and probability. Exhaustion of admissible prediction depth coincides with collapse of continuous description and the emergence of discrete survivors organized by the discrete constraint encoding identified as quantization. Probability appears only conditionally, when invariant measures exist on discrete survivor sets, and does not restore lost predictability or control.

Together with the structural core and coherent kinematics, the present analysis completes the A-layer of the Modal Triplet Theory Program. It shows that limits of prediction, undecidability, irreversibility, and quantization boundaries arise from the same admissibility structure that forbids global reduced description. These limits are not failures of theory or computation, but unavoidable features of any framework that admits local description and global obstruction.

Subsequent papers in the series build on these results. Encoding-class papers show how gravity, gauge structure, and quantization arise as forced responses to specific obstruction types, while realization papers construct explicit models that instantiate these encodings. Interpretive papers explore how these structural limits manifest phenomenologically, including in cosmology and the dark sector.

In this way, Modal Triplet Theory provides a unified explanation for why prediction, control, and computation are fundamentally limited in physical theories, and why those limits are inseparable from the structures we identify as gravity, gauge symmetry, and quantization.
