---
abstract: |
  This paper is the organizational roadmap for Modal Triplet Theory (MTT). It does not add a new physical derivation. It fixes the types, dependency order, and proof tiers needed to read the corpus without promoting analogies or target-compatible reconstructions into source theorems. A projection, a representative section, an exact upper decoder, autonomous reduced evolution, and effective-state merger solve different mathematical problems. Ordinary noninjectivity does not remove a right inverse; autonomous descent instead requires preservation of projection fibers.

  For physical ten-dimensional realizations we adopt the canonical convention $`\pi:M_{10}\to Y_4`$ with six-dimensional fiber $`X_6`$. The modal triplet is represented by typed vertical bundles, operators, and projectors. It is not three extra coordinate factors. A compact shared circle is line-bundle phase or holonomy data and is not Lorentzian time or a seventh internal coordinate. Circle-Lens-Nil is retained as a useful obstruction taxonomy, not an exhaustive theorem forcing unique gravity, gauge, and quantum responses. We prove the corresponding conditional $`4+6`$ realization statement and state the exact limits of that result.

  The roadmap classifies relations to quantum mechanics, quantum field theory, general relativity, the Standard Model, strings, quantum gravity, and AQFT by what is typed, reconstructed, selected, calibrated, or still open. Failure of one controlled chart means that chart has lost its certified domain; it does not imply that every mathematical or physical description has ceased to exist. Paper-level status is a dated snapshot, while the current A/B ledger and selected source hashes remain authoritative.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v12
date: July 2026
generated_from_main_tex_sha256: 698ec706e1d9ae9e1774e4901595d1dd9f60f407d9d3579de637f2d07f04784b
paper_id: modal-triplet-theory-admissibility-encodings-and-the-st-0867d9ed
release_state: zenodo_released
released_version: v11.0
title: |
  Modal Triplet Theory:  
  Admissibility, Encodings, and the Structure of Physical Description  
  A Typed and Tiered Corpus Roadmap
zenodo_doi: 10.5281/zenodo.19535807
zenodo_record_id: 19535807
zenodo_url: "https://zenodo.org/records/19535807"
---

# Purpose, Authority, and Scope

MTT studies reduced descriptions whose existence, continuation, and physical interpretation are conditional. The corpus contains foundational functional analysis, finite and continuum realizations, reconstructions of established formalisms, numerical packets, and interpretive proposals. These objects do not all have the same logical status.

This paper has four purposes:

1.  define a common typed dictionary;

2.  record the dependency order among structural, realization, and physical claims;

3.  classify the strength of relations to established physical frameworks;

4.  provide a stable reading guide while delegating live status to the curated A/B ledger.

<div class="remark">

*Remark 1* (Authority rule). A paper is evidence for the results it proves, but it is not automatically the current status authority for later work. When a selected successor, corrigendum, or current A/B row exists, its source path and hash control status. Corpus search is evidence discovery, not theorem promotion.

</div>

## Three distinct levels

Throughout the roadmap we distinguish:

1.  **Structural level:** typed spaces, maps, domains, margins, and conditional theorems about reduced description;

2.  **Realization level:** a geometry, bundle, connection, operator, or finite algebra implementing some structural data;

3.  **Physical level:** a selected action or dynamics, state or measure, observable map, uncertainties, and comparison with data.

Success at T1 does not imply T2, and success at T2 does not imply T3.

## What this paper does not claim

This roadmap does not derive spacetime, a probability law, the Born rule, Einstein dynamics, the Standard Model values, a string vacuum, or a nonperturbative quantum theory of gravity. It records which parts of those programs are typed or conditionally reconstructed and which source obligations remain.

# Reduced Description: The Core Dictionary

## Upper and reduced data

Let $`\mathcal X`$ be an upper configuration space, $`\mathcal Y`$ a reduced space, and
``` math
\Pi:\mathcal X\longrightarrow\mathcal Y
```
a declared reduction map. Let $`F:\mathcal X\to\mathcal X`$ be an upper evolution or update.

<div class="definition">

**Definition 2** (Representative section). A representative section is a map $`s:\mathcal Y\to\mathcal X`$ satisfying
``` math
\Pi\circ s=\operatorname{id}_{\mathcal Y}.
```
It chooses one upper representative from each reduced state in its domain.

</div>

<div class="definition">

**Definition 3** (Exact upper decoder). An exact upper decoder is a map $`D:\mathcal Y\to\mathcal X`$ satisfying
``` math
D\circ\Pi=\operatorname{id}_{\mathcal X}
```
on its declared upper domain. Such a decoder can exist only where $`\Pi`$ is injective.

</div>

<div class="definition">

**Definition 4** (Autonomous reduced evolution). An autonomous reduced evolution is a map $`G:\mathcal Y\to\mathcal Y`$ such that
``` math
\Pi\circ F=G\circ\Pi.
```

</div>

<div class="definition">

**Definition 5** (Effective merger). Two upper states merge effectively when $`x_1\ne x_2`$ but
``` math
\Pi(x_1)=\Pi(x_2).
```
This is a statement about reduced distinguishability, not automatically about microscopic destruction or probability.

</div>

These four notions must not be interchanged.

## The exact descent criterion

<div id="thm:descent" class="theorem">

**Theorem 6** (Factor-through criterion). *There exists a map $`G:\Pi(\mathcal X)\to\Pi(\mathcal X)`$ satisfying $`\Pi F=G\Pi`$ if and only if $`F`$ preserves the fibers of $`\Pi`$:
``` math
\Pi(x_1)=\Pi(x_2)
\quad\Longrightarrow\quad
\Pi(Fx_1)=\Pi(Fx_2).
```*

</div>

<div class="proof">

*Proof.* If $`G`$ exists, applying $`\Pi F=G\Pi`$ to $`x_1`$ and $`x_2`$ proves fiber preservation. Conversely, define
``` math
G(\Pi x):=\Pi(Fx).
```
Fiber preservation makes this definition independent of the chosen representative, and the factorization identity follows. ◻

</div>

<div id="prop:rightinverse" class="proposition">

**Proposition 7** (Noninjectivity does not remove a right inverse). *A noninjective surjection may have a representative section.*

</div>

<div class="proof">

*Proof.* The projection $`\Pi:\mathbb R^2\to\mathbb R`$, $`\Pi(x_1,x_2)=x_1`$, is noninjective and has the smooth section $`s(y)=(y,0)`$. Therefore noninjectivity alone cannot prove absence of a right inverse. Regular, global, equivariant, or stable sections require their own hypotheses. ◻

</div>

The corrected A0 program treats failure of descent, merger, failure of exact decoding, and ill-conditioning of representative continuation separately .

## Probability and irreversibility

A many-to-one reduction does not by itself define probabilities. To obtain a reduced Markov kernel or Born-type rule one must supply a measure or state and prove the relevant pushforward. Likewise, effective merger does not by itself select one ontic history, define entropy, or establish a physical arrow of time.

# Admissibility and Controlled Boundaries

## A declared control contract

An admissible chart must name the properties it controls. Typical margins include:

- a spectral gap $`\gamma>0`$;

- boundedness and regularity of a Riesz or coherent projector;

- a descent defect
  ``` math
  \delta_{\rm desc}
  =\sup_{\Pi x_1=\Pi x_2}
  d_{\mathcal Y}\!\left(\Pi Fx_1,\Pi Fx_2\right);
  ```

- conditioning of a representative section;

- invariance and completeness of a fixed-point basin;

- coherent stability or a Lyapunov margin;

- truncation, tail, or approximation error bounds.

<div class="definition">

**Definition 8** (Controlled encoding chart). A controlled encoding chart is a tuple
``` math
\mathfrak C=(U,\Pi,\mathcal O,F,\mathfrak m,\varepsilon)
```
where $`U\subseteq\mathcal X`$ is the declared domain, $`\mathcal O`$ is the observable family, $`\mathfrak m`$ is a list of named control margins, and $`\varepsilon`$ is the associated error budget.

</div>

<div class="definition">

**Definition 9** (Chart boundary). The boundary of a controlled chart is the locus at which at least one declared margin reaches its admissible threshold or its continuation theorem ceases to apply.

</div>

<div id="prop:boundary" class="proposition">

**Proposition 10** (Local loss of control is not universal nonexistence). *Failure of one chart contract proves only that this chart is no longer certified on the failed domain. It does not prove that every other mathematical or physical description is meaningless there.*

</div>

<div class="proof">

*Proof.* The premises concern the objects and margins of one chart. Another chart may use a different projection, domain, observable algebra, or stability theorem. Without a theorem excluding all such alternatives, universal nonexistence does not follow. ◻

</div>

## Selection fronts

A selection front is therefore a boundary-layer regime for a declared encoding. It may exhibit large condition numbers, closing gaps, metastability, or loss of robust section continuation. A transition, reset, detector instrument, or post-boundary branch must be supplied separately. Boundary crossing alone does not choose an outcome.

# Canonical Geometric Convention

## Physical ten-dimensional specialization

When a physical ten-dimensional realization is used, the canonical convention is a bundle or locally trivial fibration
``` math
\pi:M_{10}\longrightarrow Y_4
```
with a four-dimensional Lorentzian base $`Y_4`$ and a six-dimensional compact Riemannian fiber $`X_6`$. In a global product specialization,
``` math
M_{10}=Y_4\times X_6.
```
This is a selected realization convention, not a theorem that all MTT models must be ten-dimensional.

## Coordinate, bundle, and operator types

The following are distinct:

- coordinate factors of $`X_6`$;

- vector or principal bundles over $`X_6`$;

- a Hermitian shared line $`L_{\rm shared}`$ and its connection;

- vertical operators on sections of declared bundles;

- spectral projectors and their ranges;

- finite carrier modules and matrix representations.

A line bundle has rank one in each fiber but adds no coordinate dimension. An operator rank profile is not a manifold-dimension count.

## A conditional $`4+6`$ theorem

<div id="prop:fourplussix" class="proposition">

**Proposition 11** (Conditional transverse-curvature realization). *Assume:*

1.  *a four-dimensional base $`Y_4`$;*

2.  *a fiber
    ``` math
    X_6=F_1\times F_2\times F_3
    ```
    with each $`F_i`$ an oriented two-manifold;*

3.  *a line bundle with connection on each $`F_i`$ whose curvature $`\Omega_i`$ is a nonzero area form.*

*Then $`M=Y_4\times X_6`$ is ten-dimensional, and the pulled-back curvature forms $`p_i^\ast\Omega_i`$ are linearly independent.*

</div>

<div class="proof">

*Proof.* Dimensions add:
``` math
\dim M=4+2+2+2=10.
```
If $`\sum_i a_i p_i^\ast\Omega_i=0`$, restrict the equality to tangent vectors of $`F_j`$ while holding the other factors fixed. Every term except the $`j`$th vanishes, giving $`a_j\Omega_j=0`$. Since $`\Omega_j`$ is nonzero, $`a_j=0`$. This holds for each $`j`$. ◻

</div>

<div class="remark">

*Remark 12* (Limit of Proposition <a href="#prop:fourplussix" data-reference-type="ref" data-reference="prop:fourplussix">11</a>). The proposition proves a lawful ten-dimensional realization after its four-dimensional base, three transverse surfaces, and three nonzero curvature forms are assumed. It does not prove that MTT uniquely selects those assumptions, that ten dimensions are necessary, or that other realizations are excluded.

</div>

## The shared circle

The shared circle is represented by common $`U(1)`$ phase or holonomy data, typically through a Hermitian line bundle with connection. It is counted once. It is not identified with physical Lorentzian time. A flat connection can have nontrivial global holonomy, so circle response is not synonymous with nonzero curvature.

## Local $`3\times3`$ and global $`1+2+3`$ data

A rank-three comparison field belongs to
``` math
Q\in\Gamma(\operatorname{Hom}(TP,TI)).
```
Its nine components decompose locally into three orientation directions and six symmetric strain directions,
``` math
\operatorname{Mat}(3,\mathbb R)
=\mathfrak{so}(3)\oplus\operatorname{Sym}(3,\mathbb R),
\qquad
6=1+2+3
```
after a flag is selected. This is a representation decomposition, not manifold-dimension multiplication. The selected q79 finite carrier also has a $`1<2<3`$ rank profile, but rank agreement alone does not construct the connection-, operator-, or Hessian-preserving continuum intertwiner .

# Circle-Lens-Nil: Taxonomy, Not Exhaustiveness

## Recurring obstruction profiles

Circle-Lens-Nil (CLN) is retained as a useful vocabulary:

- **Circle:** loop, recurrence, phase, or holonomy consistency;

- **Lens:** quotient, redundancy, overlap, or multiple representatives;

- **Nil:** filtration, termination, nilpotent action, or a finite survivor sector.

Each use must declare its category and object type.

<div class="proposition">

**Proposition 13** (Taxonomy does not force a realization). *A CLN label does not by itself select a connection, gauge group, Hamiltonian, probability law, spacetime action, or quantum theory.*

</div>

<div class="proof">

*Proof.* The labels describe broad structural profiles. Inequivalent bundles, operators, actions, and observable maps can share those profiles. A selector or additional theorem is therefore required. ◻

</div>

## Corrected B-series interpretation

Program B0 no longer claims that CLN is exhaustive or that exactly three responses are forced. It gives a taxonomy and conditional minimal curvature realizations . Programs B1–B3 then study conditional gravity, gauge, and discrete-survivor realizations under explicit additional hypotheses .

Literal $`S^1\times\mathrm{Lens}_3\times\mathrm{Nil}_3`$ is seven-dimensional and is not the selected six-dimensional q79 compactification. Literal manifold nesting is not inferred from a rank flag. Lens and Nil may instead appear as parallel circle-bundle models, filtration labels, or operator profiles.

# The Corrected Structural Program A0–D1

## A-series: reduced description

- **A0** supplies the typed reduction dictionary, descent theorem, basin-local fixed-point control, and explicit admissibility margins.

- **A1** develops coherent kinematics conditionally from chart persistence and declared overlap data; it does not derive Lorentzian dynamics from projection alone.

- **A2** analyzes conditional computability and finite prediction depth; it does not prove universal undecidability at every boundary.

## B-series: conditional encoding responses

- **B0** gives the non-exhaustive CLN taxonomy.

- **B1** studies loop-transport consistency and a conditional gravity realization.

- **B2** separates gauge redundancy, global sections, and conditional Yang–Mills realization.

- **B3** proves discrete survivor-filter statements and records the additional assumptions needed for quantum reconstruction.

- **B4** distinguishes compatibility, local rigidity, persistence, and global uniqueness. Selected finite Standard Model packets establish a particular compatibility branch, not uniqueness across all realizations .

- **B5** treats saturation relative to a declared contract. Extended carriers, worldsheets, and dualities require explicit additional structures .

## C-series: typed realization

Program C is the realization dictionary. It distinguishes geometry, bundles, connections, operators, projectors, and finite carriers. It proves joint projector and compact-resolvent results under their stated hypotheses and proves that realization nonuniqueness limits prediction until a source law selects one realization .

## D1: interpretive hypothesis

Program D1 now treats E8/E9 dark-sector language as a projection-first hypothesis only. Encoding availability does not determine a stress tensor, equation of state, or acceleration. A covariant source or modified field equation and observational execution remain necessary .

# Proof Tiers for Relations to Established Physics

## Tier definitions

We use the following hierarchy:

<div class="center">

| Level | Meaning |
|:--:|:---|
| L0 | Interpretive analogy, diagnostic reframing, or conjecture. |
| L1 | Typed representation or compatibility map. |
| L2 | Conditional reconstruction after target-compatible structures are assumed. |
| L3 | Controlled calculation, profile replay, or certified result on a selected finite branch. |
| L4 | Selected physical source theorem with dynamics, state, observables, uncertainty, and held-out validation. |

</div>

<div class="remark">

*Remark 14*. The same research program may contain results at several levels. A finite L3 packet does not automatically promote the surrounding continuum theory to L4.

</div>

## Framework status map

The following table records the strongest defensible corpus-level interpretation, not a claim that every paper in a row is equally strong.

<div class="center">

| Framework | Current contribution | Remaining physical obligation |
|:---|:---|:---|
| Quantum mechanics | Complex Hilbert, operator, and selected finite recorder structures can be represented or conditionally reconstructed. | A general same-source Born theorem for all declared apparatus contexts remains open. |
| QFT and AQFT | Local nets, BV/BRST data, and perturbative structures exist under imported locality, state, and renormalization hypotheses. | A selected nonperturbative physical completion, state, RG matching, and observables remain open. |
| General relativity | Typed geometric and source/descent relations can recover Einstein-form dynamics conditionally. | Projection alone does not derive the Einstein action, matter source, or all GR phenomenology. |
| Standard Model | Selected finite representation, gauge-group, anomaly, and profile/parity packets establish substantial compatibility. | Zero-primitive electroweak normalization and held-out no-knob precision equivalence remain open. |
| Strings and flux geometry | q79 and Fu–Yau-type data provide a selected candidate branch and exact finite constraints. | Physical visible-hidden HYM endpoints, continuum naturality, action transfer, and the complete worldsheet contract remain open. |
| Quantum gravity | Several fixed-point, perturbative, Euclidean, BRST, and projection-first constructions are conditional or controlled. | UV-complete, positive, causal, nonperturbative physical dynamics are not established by the roadmap. |
| Dark sector | Availability profiles and their non-identifiability are typed. | A selected covariant source, cosmological solutions, perturbations, nonlinear tests, and likelihood remain open. |

</div>

## Why “MTT to X” is not one claim

A paper titled “MTT to X” may do one or more of the following:

- embed the notation of $`X`$ into an MTT carrier;

- show compatibility with an $`X`$-like constraint;

- reconstruct $`X`$ after importing its action or state space;

- calculate a selected finite profile;

- derive a source law and predict held-out observables.

Only the last item is a full physical derivation. Titles do not determine tiers; hypotheses and exit certificates do.

# Overlaps and Shadow Bridges

## A lawful overlap

An overlap between encodings $`\mathfrak C_1`$ and $`\mathfrak C_2`$ requires:

1.  a common source domain or an explicit comparison span;

2.  typed maps into both encodings;

3.  a commuting relation on the declared domain;

4.  preservation of the relevant dynamics or constraints;

5.  an observable comparison and an error budget.

For example, if $`J_i:\mathcal U\to\mathcal E_i`$ and the encoded evolutions are $`F_i`$, a dynamics-preserving overlap requires a source evolution $`F_{\mathcal
U}`$ such that
``` math
J_iF_{\mathcal U}=F_iJ_i
```
exactly or within a declared controlled error. Similar words in two papers do not supply this diagram.

## Duality and equivalence

A duality requires an invertible comparison on its declared physical quotient and preservation of dynamics and observables. A common rank count, shared circle, matching spectrum fragment, or common low-energy limit is weaker.

## Shadow-bridge status

A shadow bridge can be useful at L1 or L2 when it identifies a common constraint or diagnostic. It must be labeled accordingly. It becomes a physical equivalence only after its source, dynamics, state, observables, and inverse properties are proved.

# Fixed Points, Actions, and Physical Promotion

## Fixed points

The corrected fixed-point sequence distinguishes:

- a fixed point of an auxiliary stabilization map;

- a fixed point of a time-$`\tau`$ map;

- a stationary solution of a physical evolution;

- an attracting state under a Lyapunov or contractive law.

These are not equivalent without explicit hypotheses. Banach arguments require complete invariant basins; Schauder and Darbo give existence under different compactness or condensing conditions; uniqueness needs coercivity, strong monotonicity, or another declared mechanism.

## Action and source promotion

To promote a geometric or operator realization physically, supply:

1.  a selected action, Hamiltonian, generator, or covariant field equation;

2.  the state space, measure, or positive functional;

3.  gauge constraints and anomaly conditions;

4.  the observable map;

5.  parameter and normalization provenance;

6.  well-posedness and stability;

7.  approximation and numerical error certificates;

8.  comparison data separated into construction, calibration, and held-out sets.

<div class="proposition">

**Proposition 15** (Realization compatibility is not prediction). *If two inequivalent realizations satisfy the same stated premises but give different values for an observable, those premises do not predict that observable.*

</div>

<div class="proof">

*Proof.* Prediction requires the same value in every model of the premises, or a selector that removes the alternatives. Two admissible countermodels with different values disprove that implication. ◻

</div>

# Current Frontier Snapshot

## Closed control rows and open physical rows

As of July 2026, the curated ledger records important closed control results, including canonical-descent and GR-control rows, alongside open physical source rows. The principal open dependency chain includes:

- concrete eta9 meridian/period and flat Deligne values;

- selected visible-hidden Hull–Strominger endpoints;

- continuum q79 geometry-to-operator naturality;

- selected continuum operator execution;

- upper action and automorphism transfer;

- the general Born source theorem;

- nonperturbative QFT/BV completion;

- the complete q79 heterotic worldsheet contract;

- zero-primitive electroweak normalization;

- no-knob Standard Model values and precision equivalence.

This list is a dated snapshot. The live A/B rows, source hashes, and exit certificates supersede it when they change.

## What finite success currently means

Selected finite packets can establish exact arithmetic, representation, anomaly, group, or profile statements on their declared branch. They do not by themselves establish:

- a physical continuum compactification;

- an HYM source connection;

- a selected upper action;

- a general probability law;

- a nonperturbative QFT;

- held-out Standard Model precision.

# How to Read and Extend the Corpus

## Paper audit checklist

For every theorem or numerical claim, record:

1.  the selected source path, version, and hash;

2.  the exact premises and imported target structures;

3.  domains and codomains of every map;

4.  operator domains and commutation assumptions;

5.  the proof tier L0–L4;

6.  parameter provenance and units;

7.  verifier and artifact paths;

8.  open blockers and exit certificates;

9.  whether data are construction inputs, calibration, replay, or held out.

## Extension rule

New work should change a declared frontier truth value, discharge an exit certificate, prove a new conditional theorem, construct a missing typed map, or provide an independently verified calculation. Renaming an existing open packet, repeating a compatibility result, or replacing an old benchmark with another fitted replay is not frontier progress.

## Why the static paper index was removed

Version 11 contained a long paper-by-paper table with statuses such as “closed” and “mostly closed.” That table became stale as successor papers, corrigenda, and calculations changed. Version 12 replaces it with:

- stable conceptual classes in this paper;

- per-paper revision audits in the canonical paper repository;

- current A/B rows and source health in the research kernel;

- result references to the curated reproducibility repository where applicable.

This separates exposition from live authority.

# Version 12 Revision Record

Version 12 makes the following substantive corrections:

1.  ordinary noninjectivity no longer implies absence of a right inverse;

2.  descent, representative sections, exact decoding, merger, and stable continuation are typed separately;

3.  chart failure is expressed through named margins and means loss of control for that chart, not universal termination of description;

4.  the canonical physical convention is $`\pi:M_{10}\to Y_4`$ with six-dimensional fiber $`X_6`$;

5.  vertical triplet operators, line bundles, and coordinate factors are not conflated;

6.  the shared circle is phase/holonomy data, not time or an extra coordinate;

7.  CLN is a non-exhaustive taxonomy and does not force unique physical responses;

8.  the ten-dimensional statement is replaced by the conditional transverse-curvature Proposition <a href="#prop:fourplussix" data-reference-type="ref" data-reference="prop:fourplussix">11</a>;

9.  QM, QFT, GR, SM, strings, QG, AQFT, and dark-sector relations are classified by proof tier and remaining source obligations;

10. the stale static closure index is replaced by a stable reading guide and live-ledger authority rule.

# Conclusion

The coherent core of MTT is best understood as a typed research program about conditional reduced description. Its strongest general result is not that every familiar theory follows automatically, but that projection, descent, recovery, coherent continuation, and physical selection can be separated and tested with explicit contracts.

The canonical physical realization uses a four-dimensional Lorentzian base and a six-dimensional internal fiber when that specialization is chosen. Circle-Lens-Nil organizes recurring structures but neither exhausts all obstructions nor selects gravity, gauge theory, or quantum mechanics by name. Framework reconstructions are valuable at their proved tier; they become full physical derivations only when the selected source, dynamics, state, observables, uncertainty, and held-out tests are supplied.

This roadmap therefore offers a firmer unity than the old closure language: every paper can be located by its types, dependencies, proof tier, and exit certificate. That structure preserves genuine achievements while keeping the remaining frontier visible.
