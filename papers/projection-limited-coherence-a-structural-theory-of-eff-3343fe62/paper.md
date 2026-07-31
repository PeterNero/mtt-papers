---
abstract: |
  Many sciences replace a detailed state by a smaller set of effective variables. This paper develops a substrate-neutral framework for asking what such a projection does and does not imply. For a measurable source space $`\mathsf X`$, dynamics $`\Phi`$, observation map $`\Pi:\mathsf X\to\mathsf Y`$, admissible domain $`\mathcal A`$, and declared margin $`\mathcal C`$, we separate five questions: whether deterministic dynamics descends to $`\mathsf Y`$, whether the descended map is invertible, whether a projected stochastic process is Markov, whether source information can be recovered, and whether the realizable image $`\mathcal R=\Pi(\mathcal A)`$ obeys compatibility constraints. Each question has its own criterion.

  We prove the exact fiber criterion for deterministic descent and the corresponding lumpability criterion for stochastic kernels. We show by counterexample that a many-to-one projection, or even the absence of a continuous section, need not make the effective dynamics irreversible. Conversely, failure of the fiber criterion produces history dependence but does not by itself prove computational irreducibility. Information loss is expressed by conditional entropy and data processing; monotone physical entropy requires an additional dynamics and entropy-production law. Likewise, a capacity is a control margin until a constitutive equation, conservation law, or source term is supplied.

  The resulting framework is useful precisely because it is selective. It organizes current Modal Triplet Theory constructions and provides a template for models in physics, biology, cognition, artificial intelligence, and collective systems. The mathematical template transfers across domains; physical conservation laws, entropy laws, selection principles, and claims about consciousness or civilization do not. Such applications are stated as hypotheses with explicit validation obligations.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: a9852de96917d666ae7f305a732a38c2c603dc91c45884c8e3c430b2153d11bd
paper_id: projection-limited-coherence-a-structural-theory-of-eff-3343fe62
release_state: zenodo_released
released_version: v2
title: |
  **Projection-Limited Coherence**
  Exact Criteria for Effective Dynamics and a Cross-Domain Research Program
zenodo_doi: 10.5281/zenodo.21714517
zenodo_record_id: 21714517
zenodo_url: "https://zenodo.org/records/21714517"
---

# Version 2 revision note

<div class="description">

Version 1, DOI <https://doi.org/10.5281/zenodo.18274610>.

Version 1 treated many-to-one projection, finite capacity, and failure of a global section as sufficient for irreversibility, entropy increase, computational irreducibility, and cross-domain hidden relations. Those implications require different hypotheses and are false in that generality.

Version 2 replaces the universal chain by exact descent, lumpability, recovery, image-geometry, information, and first-exit criteria. Explicit counterexamples mark the logical boundaries. Capacity is kept separate from conservation and entropy, and all nonphysical applications are reclassified as model-building programs.

The central organizing idea survives: an effective description is governed jointly by a source dynamics, a projection, a realizable image, and a declared validity margin. These data can generate loss of source information, memory, compatibility constraints, and finite validity windows, but only when the corresponding criterion is met.

No universal domain-independent law selects $`\Pi`$, $`\mathcal C`$, an entropy functional, a probability measure, or a capacity dynamics. Each physical or empirical application must supply and test those objects.

</div>

# Why the distinctions matter

An effective variable is not the same thing as a complete state. A fluid velocity field omits molecular coordinates; a detector record omits most of the apparatus microstate; a summary statistic omits most of a data set. This observation is elementary, but several different consequences are often compressed into the phrase “information was projected out.”

The compression is dangerous because the following statements are not equivalent:

1.  two source states have the same observed value;

2.  the source dynamics induces an autonomous observed dynamics;

3.  the induced observed dynamics is not invertible;

4.  the observed stochastic process has memory;

5.  the original source state cannot be recovered from the observation;

6.  the observation has larger entropy at later times;

7.  prediction has no computational shortcut.

This paper gives each statement its own mathematical test. The purpose is not to deny that projection can contribute to irreversibility, memory, or hidden constraints. It is to identify the extra structure that turns that possibility into a theorem.

The phrase *projection-limited coherence* will mean the following research pattern:
``` math
\text{source dynamics}
  \;+\;\text{observation map}
  \;+\;\text{realizable image}
  \;+\;\text{validity margin}.
```
It is a template, not a substrate-independent equation of motion.

# Typed framework

## Source, observation, and admissibility

Let $`(\mathsf X,\mathcal B(\mathsf X))`$ and $`(\mathsf Y,\mathcal B(\mathsf Y))`$ be standard Borel spaces. Let
``` math
\Phi:\mathsf X\longrightarrow\mathsf X
  \qquad\text{and}\qquad
  \Pi:\mathsf X\longrightarrow\mathsf Y
```
be measurable. The source dynamics may be discrete, or it may be the time-$`\Delta t`$ map of a flow. The observation map $`\Pi`$ need not be linear or idempotent. It may represent a quotient, a coarse-graining, a measurement record, a feature map, or a projection followed by a pushforward.

<div class="definition">

**Definition 1** (Admissible source and realizable image). An *admissible source domain* is a declared measurable subset $`\mathcal A\subseteq\mathsf X`$. Its realizable effective image is
``` math
\mathcal R_\Pi(\mathcal A):=\Pi(\mathcal A)\subseteq\mathsf Y.
```
All effective constraints in this paper refer to this image or to a probability measure supported on it.

</div>

The distinction between $`\mathsf Y`$ and $`\mathcal R_\Pi(\mathcal A)`$ is essential. Coordinates on $`\mathsf Y`$ may look independent while the realizable image is a proper coupled subset. Equally, a many-to-one map can have $`\mathcal R_\Pi(\mathcal A)=\mathsf Y`$, in which case no image constraint follows.

## Capacity as a declared margin

<div class="definition">

**Definition 2** (Control margin). A *capacity* or *control margin* is a function
``` math
\mathcal C:\mathcal A\longrightarrow[0,\infty)
```
whose operational meaning is fixed by a stated estimate. Typical examples are a spectral gap, distance to a failure set, inverse-condition margin, coercivity constant, or certified truncation reserve.

</div>

A nonnegative function called capacity is not automatically conserved, extensive, additive, entropic, or physical. Those properties are additional claims. Recent MTT capacity papers make this separation explicit by distinguishing normalized margins, metric clearance, constitutive transport, and first exit .

## Five maps that should not be conflated

For later use, we name five distinct objects:

<div class="center">

| **Object** | Question answered |
|:---|:---|
| **$`\Pi:\mathsf X\to\mathsf Y`$** | What source information is retained? |
| **$`T:\mathcal R\to\mathcal R`$** | Does source dynamics descend to an autonomous effective map? |
| **$`S:\mathcal R\to\mathsf X`$** | Can one choose a representative source state? |
| **$`D:\mathcal R\to\mathsf X`$** | Can one recover the actual source state on a declared class? |
| **$`\mathsf K(x,\cdot)`$** | Does projected stochastic evolution depend only on the present effective state? |

</div>

A section $`S`$ chooses one point in each fiber. It does not recover which point in that fiber actually occurred. This simple distinction removes several apparent paradoxes.

# When deterministic dynamics descends

## The exact fiber criterion

<div id="thm:fiber" class="theorem">

**Theorem 3** (Effective-dynamics fiber criterion). *Let $`\Phi:\mathcal A\to\mathcal A`$ and $`\Pi:\mathcal A\to\mathcal R:=\Pi(\mathcal A)`$ be maps. There exists a unique map $`T:\mathcal R\to\mathcal R`$ satisfying
``` math
T\circ\Pi=\Pi\circ\Phi
  \quad\text{on }\mathcal A
```
if and only if
``` math
\Pi(x)=\Pi(x')
  \quad\Longrightarrow\quad
  \Pi(\Phi x)=\Pi(\Phi x')
  \qquad (x,x'\in\mathcal A).
```
If the spaces and maps are measurable and the quotient is equipped with a measurable structure for which the resulting $`T`$ is measurable, then this is an autonomous measurable effective dynamics.*

</div>

<div class="proof">

*Proof.* If $`T`$ exists, equal observed states have equal images after one step: $`\Pi(\Phi x)=T(\Pi x)=T(\Pi x')=\Pi(\Phi x')`$. Conversely, define $`T(y)=\Pi(\Phi x)`$ for any $`x`$ with $`\Pi(x)=y`$. The fiber condition makes this independent of the chosen representative. Uniqueness follows because every $`y\in\mathcal R`$ has such a representative. ◻

</div>

This is the deterministic analogue of a sufficient statistic for evolution. It says exactly when hidden coordinates can be forgotten without creating state-dependent ambiguity.

## Three boundary examples

<div id="ex:product" class="example">

**Example 4** (Many-to-one projection with invertible shadow). Let $`\mathsf X=\mathsf Y\times F`$, let $`\Pi(y,f)=y`$, and let
``` math
\Phi(y,f)=(Ty,Rf)
```
with $`T`$ and $`R`$ bijective. Then $`\Pi`$ is many-to-one whenever $`F`$ has more than one point, but the effective map is precisely the invertible map $`T`$. Loss of source coordinates therefore does not imply irreversible effective dynamics.

</div>

<div id="ex:cover" class="example">

**Example 5** (No continuous section, yet invertible shadow). Let $`\mathsf X=\mathsf Y=S^1`$, $`\Pi(z)=z^2`$, and $`\Phi(z)=e^{i\alpha/2}z`$. Then
``` math
\Pi(\Phi z)=e^{i\alpha}\Pi(z),
```
so the shadow map is the invertible rotation $`T(y)=e^{i\alpha}y`$. The double covering $`\Pi`$ has no continuous global section, but this does not obstruct invertible shadow dynamics. The regularity class of a proposed section and the autonomy of the shadow are different questions.

</div>

<div id="ex:no-descent" class="example">

**Example 6** (Projection without autonomous descent). Let $`\mathsf X=\{0,1\}^2`$, let $`\Pi(y,h)=y`$, and let $`\Phi(y,h)=(h,y)`$. The source states $`(0,0)`$ and $`(0,1)`$ have the same observation but evolve to observations $`0`$ and $`1`$. The fiber criterion fails, so no one-step map on $`\mathsf Y`$ represents the source dynamics.

</div>

Examples <a href="#ex:product" data-reference-type="ref" data-reference="ex:product">4</a>–<a href="#ex:no-descent" data-reference-type="ref" data-reference="ex:no-descent">6</a> are not pathologies. They show that projection supplies a question, while the source dynamics supplies the answer.

## Sections, decoders, and actual recovery

<div class="proposition">

**Proposition 7** (Representative selection is not source recovery). *Suppose $`S:\mathcal R\to\mathcal A`$ is a right inverse of $`\Pi`$, so $`\Pi\circ S=\operatorname{Id}_{\mathcal R}`$. Then $`S`$ recovers every actual source state $`x\in\mathcal A`$ from $`\Pi(x)`$ if and only if $`\Pi`$ is injective on $`\mathcal A`$ and $`S=\Pi^{-1}`$ there.*

</div>

<div class="proof">

*Proof.* Actual recovery requires $`S(\Pi x)=x`$ for every $`x\in\mathcal A`$, which makes $`S`$ a left inverse as well as a right inverse. A map with a left inverse is injective. The converse is immediate. ◻

</div>

Thus failure of a section can matter for a chosen category or regularity class, but existence of a section does not undo information loss inside a fiber. The appropriate recovery question must specify:

1.  the source subset to be recovered;

2.  the allowed decoder class;

3.  exact or approximate recovery;

4.  the norm, loss, or statistical risk;

5.  whether side information is available.

This is the same discipline used in statistics and information theory when comparing experiments or sufficient representations .

# Stochastic reduction and memory

## The projected-kernel criterion

Let $`\mathsf K(x,\cdot)`$ be a Markov kernel on $`\mathsf X`$. Write $`\Pi^{-1}B=\{x:\Pi(x)\in B\}`$ for $`B\in\mathcal B(\mathsf Y)`$.

<div id="thm:lump" class="theorem">

**Theorem 8** (Projected Markov-kernel criterion). *There exists a Markov kernel $`\overline{\mathsf K}`$ on $`\mathcal R=\Pi(\mathsf X)`$ such that
``` math
\overline{\mathsf K}(\Pi x,B)
  =\mathsf K(x,\Pi^{-1}B)
```
for every source state $`x`$ and measurable $`B\subseteq\mathcal R`$ if and only if
``` math
\Pi(x)=\Pi(x')
  \quad\Longrightarrow\quad
  \mathsf K(x,\Pi^{-1}B)=\mathsf K(x',\Pi^{-1}B)
```
for every measurable $`B`$.*

</div>

<div class="proof">

*Proof.* Necessity follows because the right side must depend only on $`\Pi x`$. Under the stated fiber constancy, the displayed formula defines $`\overline{\mathsf K}(y,B)`$ independently of the representative $`x`$. ◻

</div>

For finite-state chains this is the familiar strong lumpability condition. The general lesson is again exact: a projected process is Markov when the transition probabilities of observable events are constant on observation fibers. Many-to-one projection neither guarantees nor forbids this .

## History dependence

When Theorem <a href="#thm:lump" data-reference-type="ref" data-reference="thm:lump">8</a> fails, a useful model may enlarge the state:
``` math
Y_n
  \quad\leadsto\quad
  (Y_n,Y_{n-1},\ldots,Y_{n-r+1})
```
or introduce a predictive state inferred from the past. A process has finite Markov order $`r`$ only if its conditional law given the full past equals the conditional law given the last $`r`$ observations. Complete connections and predictive-state constructions provide rigorous tools when no small $`r`$ suffices .

<div class="remark">

*Remark 9* (What memory does not prove). Failure of a one-step Markov representation on a chosen state space does not prove that no finite augmentation exists, that simulation must follow every microscopic step, or that prediction is computationally irreducible. Those are complexity claims about a specified representation and algorithmic task.

</div>

# Realizable images and hidden compatibility

Suppose an effective state has components $`\mathsf Y=\mathsf Y_1\times\cdots\times\mathsf Y_m`$. Define
``` math
\mathcal R=\Pi(\mathcal A),
  \qquad
  \mathcal R_j=\operatorname{pr}_j(\mathcal R).
```

<div class="definition">

**Definition 10** (Support compatibility). The effective variables obey a nontrivial *support compatibility constraint* when
``` math
\mathcal R\subsetneq\mathcal R_1\times\cdots\times\mathcal R_m.
```

</div>

<div class="proposition">

**Proposition 11** (Recombination test). *The realizable image factors as $`\mathcal R=\prod_j\mathcal R_j`$ if and only if every coordinatewise recombination of values occurring in $`\mathcal R`$ also belongs to $`\mathcal R`$.*

</div>

<div class="proof">

*Proof.* If $`\mathcal R`$ is the product of its coordinate projections, every recombination lies in it. Conversely, the recombination property places every element of $`\prod_j\mathcal R_j`$ in $`\mathcal R`$. ◻

</div>

This proposition supplies a direct test. Projection alone does not decide its outcome. Nor does support nonfactorization determine a probability law. If $`\mu`$ is a source measure and $`\nu=\Pi_\#\mu`$, statistical independence requires
``` math
\nu=\nu_1\otimes\cdots\otimes\nu_m,
```
which is a statement about the measure, not only its support. Likewise, a conditional-dependence graph is not automatically a physical interaction graph. These distinctions are developed in the companion image-geometry paper .

# Capacity, transport, and first exit

## A margin becomes useful through an estimate

Let $`\mathcal C:\mathcal A\to[0,\infty)`$ and define the valid region
``` math
\mathcal A_+=\{x\in\mathcal A:\mathcal C(x)>0\}.
```
The first-exit time of a trajectory $`x(t)`$ is
``` math
\tau_\partial
  :=\inf\{t\geq0:\mathcal C(x(t))=0\}.
```
Without an evolution law for $`\mathcal C(x(t))`$, this definition has no predicted time scale.

<div id="prop:exit" class="proposition">

**Proposition 12** (Elementary first-exit lower bound). *Suppose $`t\mapsto\mathcal C(x(t))`$ is absolutely continuous before first exit and
``` math
\left|\frac{d}{dt}\mathcal C(x(t))\right|\leq L
```
almost everywhere, with $`\mathcal C(x(0))=c_0>0`$. If $`L>0`$, then
``` math
\tau_\partial\geq\frac{c_0}{L}.
```
If $`L=0`$, no finite exit occurs through this margin.*

</div>

<div class="proof">

*Proof.* Absolute continuity gives $`\mathcal C(x(t))\geq c_0-Lt`$. Reaching zero therefore requires $`t\geq c_0/L`$. ◻

</div>

The proposition is modest but representative. A capacity claim becomes predictive only after a bound, balance law, transport equation, or constitutive model connects the margin to dynamics.

## What is not automatic

None of the following follows from the word “capacity”:

- conservation of $`\int\mathcal C`$;

- a continuity equation;

- monotone depletion;

- additivity across subsystems;

- equivalence to thermodynamic entropy;

- a universal threshold shared by unrelated domains.

These may be imposed, derived, or tested in a particular model. They cannot be transferred from a physical theory to a biological or social model by analogy alone.

# Information loss, entropy, and arrows of time

## The exact information statement

Let $`X`$ be a discrete source random variable and $`Y=\Pi(X)`$. Then
``` math
H(X)=H(Y)+H(X\mid Y),
  \qquad
  H(Y)\leq H(X).
```
The lost source information is the conditional entropy $`H(X\mid Y)`$. For a stochastic channel $`K`$, the data-processing inequality gives
``` math
I(U;Y)\leq I(U;X)
```
whenever $`U\to X\to Y`$ is a Markov chain . Relative entropy also contracts under a Markov kernel.

These statements compare information before and after a channel. They do not say that the marginal entropy of an observed system must increase with physical time. A deterministic coarse-graining of a discrete state actually satisfies $`H(\Pi(X))\leq H(X)`$ at the instant of projection. Thermodynamic entropy production requires additional ingredients such as a dynamics, reference measure, coarse-grained equilibration, detailed-balance structure, or fluctuation relation.

## Three notions of irreversibility

<div class="definition">

**Definition 13** (Three irreversibility questions). For a projected model, distinguish:

1.  *source loss*: $`\Pi`$ is noninjective on the relevant source set;

2.  *dynamical noninvertibility*: the descended map $`T`$ exists but is not invertible;

3.  *predictive irreversibility*: retrodiction from available records has a declared nonzero risk or entropy.

</div>

These notions can coincide in a model, but none is a synonym for the others. Example <a href="#ex:product" data-reference-type="ref" data-reference="ex:product">4</a> has source loss and invertible effective dynamics. A bijective observed map can still be hard to retrodict in the presence of noise. A stochastic process can be statistically time-asymmetric even when its state transition matrix is invertible as a linear operator.

## Records and an arrow

A record is a physical variable whose present value is statistically or functionally coupled to a past event. To derive an arrow of time from records, a model must state:

1.  the recording interaction;

2.  the stable record algebra or state variables;

3.  the preparation or boundary condition;

4.  the direction in which record mutual information is generated;

5.  the recovery or erasure protocol.

MTT may supply a retarded branch orientation in a selected physical construction, but projection alone does not select that orientation.

# Computational irreducibility needs a computational theorem

A system is not computationally irreducible merely because its effective process has memory. A non-Markov process may have a compact predictive state; a high-dimensional deterministic system may have an exactly soluble observable; and a finite-state process can always be advanced by matrix powers, although the cost may still be large.

<div class="definition">

**Definition 14** (Task-relative shortcut). Fix an input encoding, an observable $`f`$, a time horizon $`n`$, an accuracy $`\varepsilon`$, and a computational model. A shortcut is an algorithm that computes or approximates $`f(\Phi^n x)`$ with asymptotic cost smaller than the declared step-by-step baseline.

</div>

A no-shortcut theorem must therefore be a lower bound, reduction, undecidability result, or complexity-theoretic statement for this typed task. Projection can motivate the search for such a theorem by exposing hidden-state dependence. It does not supply the theorem.

Predictive-state methods provide a constructive middle ground. They ask whether histories with the same conditional future distribution can be merged into a smaller state. The resulting causal states can reveal finite or infinite predictive complexity without equating memory with undecidability .

# How the framework applies to MTT

## A typed instantiation

Within MTT, the abstract symbols can be assigned more structure:

<div class="center">

| **Framework object** | MTT role at the current declared tier |
|:---|:---|
| **$`\mathsf X`$** | An upper configuration, bundle, field, or finite operator domain specified by the paper using it. |
| **$`\Pi`$** | A selected coherent-sector projector, pushforward, truncation, or observable map; these are not interchangeable without a commuting diagram. |
| **$`\mathcal A`$** | The domain on which spectral, analytic, algebraic, or numerical hypotheses have actually been verified. |
| **$`\mathcal R=\Pi(\mathcal A)`$** | The set of effective data emitted by that selected map, not all formally writable lower variables. |
| **$`\mathcal C`$** | A normalized margin, metric clearance, coercivity reserve, spectral gap, or first-exit control quantity with its own estimate. |
| **$`T`$ or $`\overline{\mathsf K}`$** | A descended deterministic or stochastic dynamics only after the fiber or lumpability condition has been established. |

</div>

This paper does not derive a universal MTT projector or a universal capacity dynamics. It provides the checklist by which a proposed MTT encoding can be audited. The current foundation supplies typed upper, coherent, and effective layers . Current capacity work supplies separate definitions for invariant margins and transport . Current stochastic work distinguishes history dependence from quantum algebra .

## Current claims and non-claims

<div class="center">

| **Statement** | Status in this paper |
|:---|:---|
| **Fiber criterion for deterministic descent** | Exact theorem. |
| **Kernel criterion for Markov projection** | Exact theorem. |
| **Source information can be lost under a many-to-one map** | Exact, relative to a declared source set. |
| **Projected dynamics is necessarily irreversible** | False without further hypotheses. |
| **Projection necessarily increases physical entropy** | False without an entropy-production model. |
| **Finite capacity obeys a universal conservation law** | Not claimed. |
| **MTT derives all effective physics from one universal projection** | Not claimed here. |
| **Cross-domain systems instantiate the same physical law** | Not claimed. |

</div>

# Cross-domain use: analogy first, model second

## What transfers

The following abstract questions can be asked in any domain:

1.  What is the source state?

2.  What is observed or retained by $`\Pi`$?

3.  What is the realizable image $`\mathcal R`$?

4.  What estimate gives operational meaning to $`\mathcal C`$?

5.  Does the fiber or lumpability criterion hold?

6.  Which prediction is made before examining the test data?

This common syntax can be scientifically useful. It can reveal that two fields face structurally similar model-reduction problems.

## What does not transfer

The following objects remain domain specific:

- conserved quantities and constitutive laws;

- thermodynamic entropy and temperature;

- biological fitness and metabolic cost;

- cognitive reports and behavioral observables;

- engineering failure criteria;

- social institutions, incentives, and historical interventions.

Using the same word for two margins does not establish that they have the same units, dynamics, or causal role.

## Domain-model ledger

<div class="center">

| **Domain** | Candidate source | Candidate projection | Required evidence |
|:---|:---|:---|:---|
| **Physics** | A specified state, field, bundle, or operator model | A declared measurement, quotient, or effective-field map | Commuting map, controlled error, dynamics, units, and comparison with observables |
| **Biology** | Molecular, cellular, or population state | A phenotype, network, or functional summary | Mechanistic model, perturbation data, uncertainty, and held-out prediction |
| **Cognition** | Neural and bodily variables under an experimental protocol | Reports or task-level latent variables | Operational definitions, identifiability, intervention, and competing-model comparison |
| **Artificial intelligence** | Model state, training history, and environment | Representations, outputs, or self-model variables | Reproducible benchmark, ablation, distribution shift, and causal test |
| **Collective systems** | Agents, institutions, resources, and communication | Macroscopic indicators or network summaries | Historical data, counterfactual design, confound control, and domain-specific dynamics |

</div>

## Consciousness and civilization

Projection-limited coherence does not by itself define consciousness, subjective time, agency, civilizational stability, or a solution to the Fermi paradox. Those topics can motivate candidate models, but each would need operational variables and discriminating evidence. In particular:

- a compressed self-model is not sufficient for consciousness;

- memory in an observed process is not sufficient for agency;

- a finite organizational margin is not a thermodynamic capacity;

- failure of a social system is not a universal admissibility boundary;

- absence of an observed extraterrestrial signal is not derived from the abstract projection formalism.

The value of the framework here is methodological. It says what would have to be built before an analogy becomes a scientific model.

# Validation and falsification

A projection-limited model should be accompanied by a seven-part certificate:

1.  **Source specification:** state space, units, and dynamics.

2.  **Observation specification:** the map $`\Pi`$ and its uncertainty.

3.  **Image test:** direct characterization of $`\mathcal R=\Pi(\mathcal A)`$ or a certified approximation.

4.  **Dynamics test:** fiber criterion, lumpability test, or an explicit history-dependent alternative.

5.  **Margin certificate:** definition of $`\mathcal C`$ and the estimate it controls.

6.  **Prediction:** an observable not used to choose the model.

7.  **Comparison:** uncertainty budget and performance against plausible alternatives.

The framework is falsified in an application when its declared map or margin fails its own certificate, when an alleged image constraint admits observed recombinations, when a claimed memory effect disappears under a sufficient state augmentation, or when a domain-specific prediction fails. The abstract mathematics itself is not evidence for any particular empirical instantiation.

# Discussion

## A useful change of emphasis

The strongest part of projection-limited coherence is not the claim that projection explains everything. It is the insistence that an effective theory has an upstream source, a map, an image, and a validity domain. Writing these objects explicitly often exposes where a proposed explanation has skipped a step.

For example, if a projected process appears irreversible, one should first ask whether an autonomous effective map exists. If it does, test its invertibility. If it does not, model the hidden-state dependence rather than calling the process fundamentally random. If entropy is invoked, identify the probability law and reference dynamics. If capacity is invoked, identify the norm or estimate it controls. If two variables are said to have a hidden relation, characterize the realizable image or the joint measure.

## Why the corrected framework is stronger

Removing universal implications does not make the framework empty. It makes it modular:
``` math
\begin{array}{c}
\text{fiber test} \longrightarrow \text{autonomous deterministic shadow},\\
\text{lumpability test} \longrightarrow \text{autonomous Markov shadow},\\
\text{image test} \longrightarrow \text{compatibility constraints},\\
\text{information test} \longrightarrow \text{recoverability limits},\\
\text{margin estimate} \longrightarrow \text{controlled validity window}.
\end{array}
```
Different applications may satisfy different rows. The framework records that fact without forcing all systems into one physical mechanism.

## Relationship to reduction and emergence

The formalism is compatible with several established viewpoints. Sufficient statistics and Blackwell comparison describe what information a channel preserves . Lumpability describes when a Markov chain descends to a partition . Information theory quantifies channel loss . Predictive-state methods ask which histories have the same future law . Projection-limited coherence does not replace these theories. It provides a common typed ledger in which their distinct obligations can be combined with MTT’s source, admissibility, and margin language.

# Conclusion

Projection is not a universal generator of irreversibility, entropy, complexity, or cross-domain law. It is one component of an effective description. Exact consequences arise only after the source dynamics, observation fibers, realizable image, probability law, and validity margin are specified.

Version 2 establishes a corrected core:

1.  deterministic descent is governed by fiber invariance;

2.  stochastic descent is governed by kernel lumpability;

3.  a section selects a representative but does not recover an unknown source point in a nontrivial fiber;

4.  compatibility is a property of the actual image or joint measure;

5.  information loss does not by itself supply thermodynamic entropy production;

6.  memory does not by itself supply a no-shortcut theorem;

7.  capacity is a control margin until a domain-specific law gives it more structure.

This is the defensible unifying statement. MTT and other theories may instantiate the template in multiple ways. Biology, cognition, artificial intelligence, and collective systems may also use it, but only through independently specified and tested domain models.
