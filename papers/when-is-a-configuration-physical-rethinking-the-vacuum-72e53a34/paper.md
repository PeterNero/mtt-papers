---
abstract: |
  Vacuum selection involves several logically different questions that are often compressed into one. A configuration can exist as a mathematical solution, admit a controlled effective chart, satisfy a chosen set of stability and consistency tests, be reached with nonzero weight under a dynamics or measure, and agree with observations. None of these statements implies all the others.

  This paper gives an admissibility-first account of the problem while correcting two overly strong inferences. First, failure of one chart or one certificate does not prove that the underlying mathematical configuration does not exist. Global exclusion requires either a chart-independent obstruction or a transition-compatible exhaustion of the allowed atlas. Second, exclusion is not selection. If two configurations remain admissible, the admissibility predicate alone supplies neither a unique outcome nor a probability distribution. Selection additionally requires a declared dynamics, initial law, measure, conditioning rule, optimization principle, or other source of relative weight.

  We formalize these distinctions with a typed vacuum-selection record that contains the candidate space and equivalence relation, admissibility rows, chart transitions, dynamics or ensemble, initial data, stopping and reset semantics, observation map, conditioning event, and normalization certificate. We also show why disconnected admissible components do not by themselves imply physical inaccessibility: that conclusion depends on whether the selected evolution is continuous, permits jumps or tunneling, or changes charts.

  The resulting framework preserves the useful core of the admissibility-first proposal. It turns consistency, stability, and controlled-description tests into a provenance-aware filter before statistical or dynamical selection is attempted. Current finite Modal Triplet Theory calculations provide examples of such certificates at explicitly limited tiers. They do not yet define a global vacuum measure, prove exhaustion of all branches, or select one observed universe.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 09e9d317a083fde3e014121b005c249bbf0d11f79098c9c79065f9d7bb59b2f7
paper_id: when-is-a-configuration-physical-rethinking-the-vacuum-72e53a34
release_state: zenodo_released
released_version: v2
title: |
  When Is a Configuration Physical?
  Admissibility, Chart Failure, and the Logic of Vacuum Selection
zenodo_doi: 10.5281/zenodo.21710258
zenodo_record_id: 21710258
zenodo_url: "https://zenodo.org/records/21710258"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1.0, DOI [10.5281/zenodo.18255208](https://doi.org/10.5281/zenodo.18255208).

Version 1 treated failure of an admissible description as if it established nonexistence of a physical configuration. It also described admissibility as selection by exclusion, inferred physical inaccessibility from disconnected admissible regions, and attributed the lack of convergence in landscape research to those claims without supplying an atlas-exhaustion theorem, dynamics, transition law, measure, observation map, or normalization.

The revision separates mathematical existence, chart validity, kinematic admissibility, dynamical or statistical realization, and empirical identification. It proves elementary no-go propositions for the two invalid implications, specifies the data required for a genuine vacuum-selection statement, and compares this role with landscape statistics, tunneling, effective field theory, and swampland-style consistency filters.

The central methodological idea survives: one should not compare or weight candidate configurations before stating which mathematical and physical structures are controlled on them. Admissibility can sharply reduce a candidate set and expose missing assumptions.

The paper does not identify the realized vacuum. Current Modal Triplet Theory results do not yet provide a global exhaustion theorem, a complete visible–hidden physical compactification, a universal transition dynamics, a normalized measure on all allowed branches, or a derivation of observed four-dimensional data from that selection problem.

</div>

# The question in its corrected form

The phrase “Which vacuum is physical?” can hide several distinct questions:

1.  Does a candidate exist as a mathematical solution of the stated equations and constraints?

2.  Is there a chart or representation in which the quantities used in the argument are defined and controlled?

3.  Does the candidate satisfy a declared set of consistency, stability, and approximation tests?

4.  Is it reached, occupied, or weighted by a specified dynamics, ensemble, measure, or variational rule?

5.  Does an observation map send it to data compatible with experiment?

The old paper treated these questions as different descriptions of one boundary. They are instead different layers of a complete inference.

The corrected admissibility-first thesis is modest but useful:

> Before assigning weights or drawing physical conclusions, state the candidate space, the chart in which each test is meaningful, and the certificate that each test passes. Then state separately what selects among the surviving candidates.

This is not a rejection of landscape counting, vacuum transitions, anthropic conditioning, or effective field theory. It is an ordering rule. The relevant objects must be typed before they can be combined.

## Five meanings of “physical”

<div class="tabularx">

L0.18YY Layer & Question & Typical certificate
Formal existence & Does the object solve the declared mathematical equations? & Exact construction, existence theorem, or certified numerical solution.
Chart validity & Are the coordinates, operators, and approximations used here defined? & Domain theorem, transition map, operator-domain statement, or error bound.
Admissibility & Does the candidate pass the selected consistency and control rows? & Signed reserves for topology, anomaly, positivity, spectral, descent, stability, and truncation conditions.
Realization & Why is this admissible candidate reached or weighted rather than another? & Initial law and dynamics, invariant measure, transition rates, optimization principle, or explicit selection axiom.
Empirical identification & What observations does the realized candidate predict? & Observation map, matching conventions, uncertainty budget, and held-out comparison.

</div>

A candidate can pass an earlier layer and fail a later one. A formal solution may lack a controlled low-energy chart. An admissible candidate may have zero weight under a declared cosmological dynamics. A dynamically preferred candidate may disagree with observation. Conversely, failure of one representation need not imply failure of all representations.

## What this paper does not assume

The argument does not assume that every useful Hilbert-space description has a spectral gap. Hilbert spaces and gap conditions are different objects. Nor does it assume that every effective field theory breaks down at one universal threshold. Each model has its own domain, scales, and error estimates. Finally, it does not assume that configuration space comes with a canonical probability measure. A measure is additional data, not a consequence of naming a set.

# Candidate spaces, charts, and admissibility

## The candidate space

Let $`\mathcal C`$ denote a class of candidate configurations and let $`\sim`$ identify descriptions that are regarded as physically or mathematically equivalent. Depending on the problem, an element of $`\mathcal C`$ might be:

- a stationary point of a scalar potential;

- a solution of field equations modulo gauge equivalence;

- a compactification together with metric, flux, bundle, and source data;

- a quantum state or representation of an observable algebra; or

- an effective theory with declared cutoff and matching data.

These are not interchangeable notions of vacuum. The type of $`\mathcal C`$ must be stated before selection is discussed.

An atlas is a family of partial descriptions
``` math
\{(U_\alpha,\varphi_\alpha)\}_{\alpha\in I},
  \qquad U_\alpha\subseteq \mathcal C,
```
with transition maps on overlaps whenever the descriptions are intended to represent the same underlying object. Here “chart” is used broadly: it may be a coordinate patch, gauge fixing, perturbative expansion, effective theory, numerical parametrization, or finite projected model.

## Admissibility rows

Within a chart $`U_\alpha`$, suppose the declared tests are represented by signed normalized reserves
``` math
r_{\alpha j}:U_\alpha\longrightarrow \mathbb R,
  \qquad j=1,\ldots,m_\alpha.
```
The convention is that positive reserve means the corresponding condition is certified. The chart-relative admissible set is
``` math
\mathcal A_\alpha
  =
  \bigl\{x\in U_\alpha:
  r_{\alpha j}(x)>0\ \text{for every required }j\bigr\}.
```
The rows can encode exact algebraic constraints, strict positivity, operator-domain control, numerical residual bounds, truncation errors, or other conditions. Their provenance and logical status matter. A numerically positive surrogate is not an exact theorem unless its error certificate controls the relevant implication.

<div class="definition">

**Definition 1** (Chart-relative admissibility record). A chart-relative admissibility record is
``` math
\mathfrak A_\alpha
  =
  \bigl(U_\alpha,\varphi_\alpha,
        \{(r_{\alpha j},s_{\alpha j},\pi_{\alpha j})\}_{j=1}^{m_\alpha}\bigr),
```
where $`s_{\alpha j}`$ states the semantics of row $`j`$ and $`\pi_{\alpha j}`$ identifies its proof, computation, assumptions, and source version. The record is *complete for a declared claim* only if every premise needed by that claim appears as a row or an explicit assumption.

</div>

This definition prevents a common ambiguity. The failure of a row says that one declared certificate has failed. What follows depends on its semantics. Failure of an error bound can mean only that the approximation is no longer certified; it need not mean that the exact solution has ceased to exist.

## Local failure and global exclusion

<div id="prop:chart" class="proposition">

**Proposition 2** (One-chart failure is not nonexistence). *Let $`x\in\mathcal C`$ and let $`\mathfrak A_\alpha`$ be one chart-relative admissibility record. Either
``` math
x\notin U_\alpha
  \quad\text{or}\quad
  x\in U_\alpha\setminus\mathcal A_\alpha
```
is insufficient, by itself, to prove that $`x`$ does not exist in $`\mathcal C`$, or that no admissible description of $`x`$ exists.*

</div>

<div class="proof">

*Proof.* The first statement is immediate because chart domains are partial: $`x\notin U_\alpha`$ is compatible with $`x\in U_\beta`$ for another chart. For the second, a failed row can be chart dependent. It is consistent with the stated data that another record $`\mathfrak A_\beta`$ contains $`x`$ and all of its required rows are positive. Therefore global nonexistence or exclusion does not follow without an additional theorem relating all allowed charts or establishing a chart-independent obstruction. ◻

</div>

A familiar analogy is a coordinate singularity. The failure of longitude at a pole does not remove the pole from the sphere. In a physical calculation the situation can be subtler, but the logic is the same: breakdown of coordinates, perturbation theory, gauge choice, or finite truncation must not be relabeled as breakdown of the underlying object.

<div id="cor:global" class="corollary">

**Corollary 3** (Requirements for global exclusion). *A valid global exclusion statement needs at least one of:*

1.  *a chart-independent obstruction evaluated on $`x`$;*

2.  *an atlas-exhaustion theorem plus transition-compatible admissibility rows showing that every allowed chart excludes $`x`$; or*

3.  *a definition of the candidate class under which failure of the row is itself logically equivalent to nonexistence.*

</div>

The second route is demanding. On overlaps $`U_\alpha\cap U_\beta`$, one must know whether the two records test the same invariant statement or only different sufficient conditions. If they are merely sufficient, failure in both charts can still leave the underlying property undecided.

# Exclusion is not selection

An admissibility filter can reduce a candidate class dramatically. That is already valuable. But a filter does not generally choose one surviving element.

<div id="prop:noselect" class="proposition">

**Proposition 4** (Admissibility alone does not select). *Let
``` math
\mathcal A=\{x\in\mathcal C:P(x)=1\}
```
be the set selected by an admissibility predicate. If $`\mathcal A`$ contains two inequivalent elements $`x_1\not\sim x_2`$, then $`P`$ alone determines neither a unique realized configuration nor a unique probability measure on $`\mathcal A/\!\sim`$.*

</div>

<div class="proof">

*Proof.* Both $`x_1`$ and $`x_2`$ satisfy exactly the information supplied by $`P`$, so that information does not distinguish them. Moreover, the Dirac measures $`\delta_{[x_1]}`$ and $`\delta_{[x_2]}`$, as well as every convex combination
``` math
p\,\delta_{[x_1]}+(1-p)\,\delta_{[x_2]},
  \qquad 0\leq p\leq1,
```
are normalized probability measures supported on the admissible quotient. No value of $`p`$ is determined by the predicate. ◻

</div>

> Admissibility answers “which candidates survive these tests?” Selection answers “why this survivor, or this distribution over survivors?”

Selection can be supplied in several inequivalent ways:

- deterministic evolution from selected initial data;

- stochastic dynamics with specified transition law;

- an invariant or equilibrium measure, together with a proof of existence and normalization;

- a variational principle with a unique optimizer;

- cosmological nucleation and expansion rates;

- conditioning on an observation or observer model; or

- an explicit branch axiom.

Each option changes the claim. None is silently contained in the word “admissible.”

## Why this distinction matters

Suppose a finite scan begins with $`10^6`$ candidates and exact consistency conditions leave only three. The reduction from $`10^6`$ to three is a strong result. It can expose correlations, rule out broad mechanisms, and make later calculations feasible. Yet it has not selected one of the three. Reporting “three admissible candidates remain” is more rigorous and more informative than hiding the remaining ambiguity behind a selection label.

Conversely, a probability distribution can be defined before all admissibility questions are settled, but then its support and physical interpretation are conditional. The order advocated here is therefore a discipline of inference, not a claim that only one research strategy is mathematically possible.

# A typed vacuum-selection record

To turn an admissibility filter into a selection model, the missing data should be visible in one record.

<div id="def:record" class="definition">

**Definition 5** (Vacuum-selection record). A typed vacuum-selection record is
``` math
\mathfrak V=
\bigl(
\mathcal C,\sim,\{\mathfrak A_\alpha\},
\mathcal D,\mu_0,\mathcal T,\mathcal R,
\mathcal O,E_{\rm obs},\mathcal N
\bigr),
```
where:

1.  $`\mathcal C`$ and $`\sim`$ define candidates and equivalence;

2.  $`\{\mathfrak A_\alpha\}`$ is the admissibility atlas;

3.  $`\mathcal D`$ is a deterministic generator, stochastic transition law, path measure, or declared ensemble;

4.  $`\mu_0`$ is initial data or an initial law when required;

5.  $`\mathcal T`$ gives stopping, terminal, or observation-time semantics;

6.  $`\mathcal R`$ gives post-exit continuation, chart transition, or reset semantics;

7.  $`\mathcal O`$ maps selected states or histories to observables;

8.  $`E_{\rm obs}`$ is the conditioning or comparison event; and

9.  $`\mathcal N`$ proves normalization, well-posedness, and the error or uncertainty statement needed for the final claim.

</div>

The record is deliberately broad enough to cover deterministic, stochastic, quantum, and statistical proposals. It does not pretend that these proposals are equivalent. Instead, it forces the author to state which one is being used.

## Three common specializations

#### Deterministic selection.

Let $`X_t=\Phi_t(X_0)`$ be a well-posed flow. If $`X_0`$ is fixed and $`\Phi_t(X_0)`$ converges to a unique equivalence class in $`\mathcal A`$, the limit can define a selection. The convergence basin and dependence on initial data remain part of the theorem.

#### Stochastic selection.

Let $`X_t`$ have a transition kernel $`K_t(x,\mathrm dy)`$. An outcome law might take the form
``` math
\nu(B)
  =
  \mathbb P_{\mu_0}
  \bigl(\mathcal O(X_T)\in B\mid E_{\rm obs}\bigr).
```
This expression is meaningful only if the process, stopping time $`T`$, conditioning event, and denominator $`\mathbb P_{\mu_0}(E_{\rm obs})>0`$ are defined. A different initial law or transition kernel can produce a different $`\nu`$ on the same admissible set.

#### Ensemble or counting selection.

For a finite or regulated class, one may assign weights $`w(x)`$ and define
``` math
\nu([x])
  =
  \frac{w([x])\,\mathbf 1_{\mathcal A}([x])}
       {\sum_{[y]\in\mathcal C/\sim}w([y])\,\mathbf 1_{\mathcal A}([y])}.
```
The denominator, regulator, equivalence classes, and origin of $`w`$ are part of the result. Admissibility supplies the indicator, not the weight.

## A release checklist for selection claims

<div class="tabularx">

L0.24YY Object & Required question & Failure mode if omitted
Candidate type & What exactly counts as a vacuum? & Stationary points, compactifications, states, and EFTs are conflated.
Equivalence & Which descriptions represent the same candidate? & Gauge copies or dual presentations are overcounted.
Admissibility atlas & Where is each test valid and how do charts overlap? & Local certificate failure is promoted to global exclusion.
Dynamics or weight & What distinguishes surviving candidates? & Exclusion is mislabeled as unique selection.
Initial law & From what state or distribution does evolution begin? & Outcome weights are underdetermined.
Exit semantics & What happens when a chart or reserve fails? & A stopping condition is mistaken for a new state.
Observation map & How are model variables compared with data? & Internal coordinates are mistaken for observables.
Normalization and error & Is the law finite, normalized, stable, and accurate enough? & Formal weights are treated as probabilities.

</div>

# Disconnected regions and physical accessibility

Version 1 inferred that disconnected admissible regions could not be related physically. Topology alone does not support that conclusion.

<div id="prop:disconnect" class="proposition">

**Proposition 6** (Disconnectedness is not inaccessibility). *If an admissible subset $`\mathcal A\subset\mathcal C`$ is disconnected, then no continuous path lying entirely in $`\mathcal A`$ joins different connected components. This does not imply that a selected physical evolution cannot move between the components.*

</div>

<div class="proof">

*Proof.* The first statement is the definition of disconnected components. For the second, consider a continuous-time Markov chain on two states $`\{a,b\}`$ with positive jump rates in both directions. The state space is disconnected in its discrete topology, yet the process reaches either state from the other with positive probability. More generally, an evolution may leave $`\mathcal A`$, use another chart, tunnel, jump, or apply a reset map. Whether any such mechanism is physically allowed is extra data in $`\mathcal D`$ and $`\mathcal R`$. ◻

</div>

Even when the microscopic evolution is continuous, an effective description can represent a transition as a jump after unresolved degrees of freedom are integrated out. Conversely, a formal instanton or nucleation solution does not by itself establish an observationally relevant transition rate. Coleman–De Luccia vacuum decay is an example of a theory in which transition data are computed from more than the topology of the vacuum set .

## What a boundary can establish

An admissibility boundary can establish that a particular certificate or chart has reached its declared limit. It can support a first-exit problem after a generator is supplied. It does not independently decide among:

1.  termination of the underlying history;

2.  continuation in another chart;

3.  deterministic reset to a new state;

4.  stochastic reset according to a kernel;

5.  tunneling through a region not represented by the chart; or

6.  failure only of the approximation while the exact system remains regular.

These alternatives are developed at the process level in the capacity-gated and selection-front papers . The present paper owns the logical distinction as it applies specifically to vacuum selection.

# Relation to landscape and consistency programs

## Landscape counting is not one uniform assumption

The string-vacuum literature contains several different projects. Bousso and Polchinski showed how quantized four-form fluxes can generate a dense discretuum and included a membrane-nucleation dynamics . Douglas framed systematic vacuum classification in terms of ensembles of effective Lagrangians . Denef and Douglas computed distributions and counts for classes of flux vacua . These works do not simply assume that every formal point is equally realized. They specify particular candidate classes, constraints, approximations, and weights.

The admissibility-first framework should therefore not be advertised as an explanation of why landscape research “failed to converge.” It instead offers a bookkeeping discipline that can be applied inside such programs: which constraints define the counted class, where are the approximations valid, what supplies the weight, and what observational conditioning is used?

## Consistency filters and the swampland

The landscape/swampland distinction emphasizes that apparently consistent low-energy theories need not admit ultraviolet completion in quantum gravity . This is close in logical form to an admissibility filter: both distinguish a broad formal class from a smaller class passing additional consistency conditions. The criteria are not automatically the same. An Modal Triplet Theory reserve row becomes relevant to a string or quantum gravity claim only after a theorem identifies its domain and proves the corresponding physical implication.

The comparison yields a useful division:

- a *consistency filter* asks whether a candidate belongs to the intended theory;

- a *control filter* asks whether a chosen approximation or chart is reliable;

- a *stability filter* asks whether specified perturbations remain controlled; and

- a *selection law* assigns realization or observational weight among the survivors.

A single condition can play more than one role, but the implication must be proved rather than inferred from terminology.

## Anthropic conditioning

Anthropic arguments add an observation or observer condition rather than an admissibility theorem. Weinberg’s cosmological-constant bound, for example, conditions on the formation of gravitationally bound structures . One may accept or reject a particular conditioning model, but its logical role is clear: it supplies $`E_{\rm obs}`$ in <a href="#def:record" data-reference-type="ref+label" data-reference="def:record">5</a>. It does not follow from positivity of a local reserve.

# Effective descriptions and chart boundaries

Effective field theory provides a concrete reason to distinguish an object from one description of it. An EFT is specified with degrees of freedom, symmetries, a cutoff or expansion regime, matching data, and an error organization. Its breakdown can indicate that omitted operators, thresholds, or new degrees of freedom matter. It need not imply that the underlying theory or state is nonexistent. The modern EFT viewpoint grew from precisely this attention to scale and controlled expansions .

In the notation of <a href="#sec:charts" data-reference-type="ref+label" data-reference="sec:charts">2</a>, an EFT can be represented as one chart $`U_\alpha`$ with rows for scale separation, truncation error, positivity, and other model-specific conditions. A neighboring EFT or a more complete description may provide $`U_\beta`$. To continue a physical prediction across their overlap one needs:

1.  a matching map between variables and observables;

2.  overlapping error control;

3.  agreement to the declared order or norm; and

4.  a statement about which quantities are invariant under the change of description.

This is the kind of transition-compatible theorem required by <a href="#cor:global" data-reference-type="ref+label" data-reference="cor:global">3</a>. Calling every EFT breakdown “inadmissible physics” would erase exactly the multiscale structure that makes EFT useful.

# The MTT implementation and its present limit

## What MTT contributes

Modal Triplet Theory organizes a physical claim around a finite ledger of typed conditions. In the corrected Foundation, the ledger distinguishes formal data, domain conditions, control reserves, exit semantics, and claim status . The normalized capacity paper makes otherwise incomparable inequalities explicit by recording a slack, scale, norm, provenance, and active-row information for each condition .

For vacuum questions, this contributes three practical tools:

1.  *provenance*: every admissibility row points to the theorem or computation that supports it;

2.  *typing*: topology, anomaly cancellation, spectral control, finite projection, and numerical residuals are not treated as one scalar fact; and

3.  *anti-promotion boundaries*: a finite or rank-restricted certificate remains at that tier until a transfer theorem is proved.

The heterotic-vacuum paper applies this distinction directly: finite ansatz calculations, attraction in a chosen reduced flow, and physical selection are separate claims . The Hull–Strominger paper similarly keeps its fixed-point correspondence conditional on the geometric and analytic data named in its hypotheses .

## Current finite certificates

Current repository results include:

- an exact arithmetic selection of $`q=79`$ on a declared branch;

- a literal finite rank-two Cech witness with its cocycle checks;

- a certified finite projected HYM solution; and

- a rank-two weighted-theta/Wiener contraction certificate.

These are substantive examples of exact, topological, finite-projection, and analytic admissibility rows. They show how a candidate branch can accumulate auditable certificates instead of relying on one qualitative label.

They do not yet prove:

- exhaustion of every allowed global branch;

- a unique physical rank-three visible–hidden bundle pair;

- a complete physical Hull–Strominger or worldsheet endpoint;

- a normalized measure or transition dynamics on all candidate compactifications;

- a unique realized vacuum; or

- the observed four-dimensional theory from vacuum selection alone.

The reproducibility section below identifies the frozen repository commit and result manifests. Their role in this paper is contextual: they illustrate the structure of certified admissibility, not a completed vacuum-selection theorem.

## The theorem still needed

A strong Modal Triplet Theory vacuum-selection result would require a chain of the form
``` math
\begin{aligned}
\text{candidate atlas}
&\longrightarrow
\text{transition-compatible admissibility rows}\\
&\longrightarrow
\text{exhaustion or declared candidate boundary}\\
&\longrightarrow
\text{selected dynamics or normalized measure}\\
&\longrightarrow
\text{unique class or outcome law}\\
&\longrightarrow
\text{four-dimensional observation map}.
\end{aligned}
```
Every arrow needs a domain and a verifier. The current results occupy important parts of the second line. They do not yet supply the entire chain.

# A worked logical example

Consider three inequivalent candidate compactifications $`\mathcal C/\!\sim=\{v_1,v_2,v_3\}`$. Suppose exact topology and anomaly tests exclude $`v_3`$, while certified analytic rows retain $`v_1`$ and $`v_2`$:
``` math
\mathcal A/\!\sim=\{v_1,v_2\}.
```
This establishes a two-thirds reduction and an exact exclusion of $`v_3`$. It does not choose between $`v_1`$ and $`v_2`$.

Now add a continuous-time transition generator on the two survivors,
``` math
Q=
  \begin{pmatrix}
    -k_{12} & k_{12}\\
    k_{21} & -k_{21}
  \end{pmatrix},
  \qquad k_{12},k_{21}>0.
```
Its stationary law is
``` math
\pi_1=\frac{k_{21}}{k_{12}+k_{21}},
  \qquad
  \pi_2=\frac{k_{12}}{k_{12}+k_{21}}.
```
The admissibility calculation determines the support $`\{v_1,v_2\}`$. The rates determine the stationary weights. An observation map may then condition those weights further.

This elementary example displays the full separation:

1.  changing the admissibility rows can change the support;

2.  changing the rates can change the weights without changing support;

3.  changing the initial law matters before stationarity;

4.  changing the observation condition can change the posterior law; and

5.  none of these changes alters the mathematical existence of the three original candidates.

The same distinctions remain necessary in an infinite-dimensional or quantum model, where proving that each object exists is much harder.

# What would count as progress

The framework gives several meaningful intermediate achievements. A research program need not leap directly to a unique universe.

<div class="description">

Prove that a named candidate or family violates a chart-independent condition.

Reduce a finite or regulated candidate class while reporting all surviving classes and the completeness of the scan.

Prove that the relevant rows and observables agree on chart overlaps, so a certificate is not tied to one presentation.

Given a declared generator and initial law, compute transition, capture, or stationary probabilities with error control.

Prove uniqueness, or derive a normalized outcome law, on an exhausted candidate class.

Map the selected result to observables with conventions, renormalization and threshold transport, uncertainties, and held-out tests.

</div>

Each item is independently valuable. The labels also prevent an exact finite certificate from being advertised as empirical closure.

# Falsifiability and completion contract

The admissibility-first proposal becomes scientifically stronger when it states how it could fail or remain incomplete.

## Failure modes

The proposal would fail as a useful vacuum-selection framework if:

1.  its rows cannot be made invariant or transition compatible across the descriptions required by the physical problem;

2.  its filters merely restate known equations without producing new exclusions, error control, or computational compression;

3.  the candidate class cannot be bounded or exhausted enough for the selection claim being made;

4.  no dynamics, measure, or variational rule can be sourced without importing the desired outcome;

5.  different equally admissible row choices produce incompatible predictions with no higher-level criterion; or

6.  the eventual observation map fails held-out empirical tests.

## Completion certificate

A future claim of completed vacuum selection should publish:

1.  the candidate class and equivalence relation;

2.  the atlas and transition maps;

3.  every admissibility row with proof status and source hash;

4.  an exhaustion statement or an explicit limitation of scope;

5.  the dynamics, measure, or optimization principle;

6.  initial, boundary, stopping, and reset data;

7.  the resulting unique class or normalized outcome law;

8.  the observation and matching map;

9.  an uncertainty and approximation budget; and

10. independent verification that observed values were not used as hidden construction inputs where prediction is claimed.

Without items 4–7, the result is a filter rather than a completed selection theorem. Without items 8–10, it is not empirical closure.

# Conclusion

The useful insight in an admissibility-first approach is not that non-admissible configurations cease to exist in every mathematical sense. It is that physical inference should not outrun its domain certificates. A formal solution, a controlled chart, an admissible candidate, a realized history, and an observed world are different objects.

Two corrections follow. Failure of one chart cannot establish global nonexistence without an invariant obstruction or atlas-exhaustion theorem. And admissibility cannot uniquely select when more than one inequivalent candidate survives. Dynamics, measures, conditioning, or another source of relative weight must enter explicitly.

With these corrections, admissibility remains a promising organizing principle. It can turn vague appeals to consistency or stability into auditable rows, prevent finite calculations from being promoted beyond their domains, and show exactly which object is missing from a proposed selection chain. Current Modal Triplet Theory results provide nontrivial examples of this method. They narrow and certify parts of a candidate branch. The global measure, branch exhaustion, physical compactification, and empirical observation map remain separate research targets.

# Reproducibility statement

The no-go propositions in this paper are elementary consequences of the typed definitions and require no numerical input. The finite Modal Triplet Theory examples cited as contextual evidence are maintained in the public results repository identified below, with immutable commit and manifest hashes. No measured Standard Model or cosmological value is used to prove the logical results of this paper.

#### Corpus-state cross-checks.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*derived exact*).

  Literal 81-entry, 729-cocycle finite Cech witness.

- (*derived exact*).

  Executable q=79 exact-branch audit.

- (*derived exact*).

  CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The q79 arithmetic theorem and audit, literal finite rank-two Cech witness, and rank-two Wiener-contraction certificate are contextual examples of finite, topological, and analytic admissibility certificates. They do not construct a complete physical visible-hidden Hull-Strominger vacuum, select a unique realized branch, supply a global measure or dynamics, or derive observed four-dimensional physics.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Corpus-state cross-checks

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A07/literal_cech_witness` (**DERIVED_EXACT**): Literal 81-entry, 729-cocycle finite Cech witness.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
