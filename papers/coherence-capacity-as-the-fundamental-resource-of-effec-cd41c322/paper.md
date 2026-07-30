---
abstract: |
  Coherence capacity is a normalized summary of how far a declared effective construction lies from failure of one of its control conditions. This paper asks when that diagnostic can also be called a *resource*. The answer requires additional operational data. One must specify an allowed perturbation family, a cost, an action of perturbations on states, a composition rule, and, for a genuine resource theory, a class of free operations and a conversion preorder.

  Given those data, we define the control budget as the least perturbation cost that exits the admissible set. In a metric perturbation model this is exactly the distance to inadmissibility and hence the largest guaranteed open perturbation ball. We prove a cumulative-consumption theorem for normalized reserve vectors, a parallel-composition bottleneck law, and controlled transport bounds between models. These results make capacity operationally useful as a robustness budget. They also show why it is generally neither additive nor conserved: repair, feedback, redundancy, and changes of metric can alter the budget.

  A capacity value alone is not a probability measure, force, entropy, thermodynamic monotone, gravitational coupling, reset law, or arrow of time. Noninjectivity also does not rule out a right inverse; an orthogonal projection has the inclusion of its range as a bounded section. Any physical use therefore needs a separate action, channel, constitutive law, instrument, state count, or causal geometry. Within MTT, the normalized margin paper supplies the capacity record and the Foundation supplies the complete admissibility ledger. The present paper contributes the model-specific control-budget and resource-completion layer. It does not promote coherence capacity to a universal substance underlying all effective physics.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v4
date: Version 4, July 2026
generated_from_main_tex_sha256: b7af07348d7463fbf17042c67a84b792eb9ab8b3c152fb9155565f27eba212b2
paper_id: coherence-capacity-as-the-fundamental-resource-of-effec-cd41c322
release_state: zenodo_released
released_version: v4
title: |
  Coherence Capacity as a Control Budget
  for Effective Descriptions:
  Robustness, Composition, and the Limits of Resource Language
zenodo_doi: 10.5281/zenodo.21709596
zenodo_record_id: 21709596
zenodo_url: "https://zenodo.org/records/21709596"
---

# Revision note: Version 4

<div class="description">

Version 4 supersedes Version 3.0, DOI [10.5281/zenodo.18322036](https://doi.org/10.5281/zenodo.18322036).

Version 3 called an arbitrary positive margin the fundamental resource of effective physics. It then used the same scalar to infer a missing right inverse, irreversible shadow dynamics, gravity, time, entropy, measurement collapse, horizons, thermalization, and undecidability. None of those conclusions follows from a zero set or stability margin alone.

The title and central theorem have been replaced. Capacity becomes an operational control budget only after a perturbation class and cost are specified. A full resource interpretation additionally requires free operations, composition, and conversion rules. The paper proves robust-radius, cumulative-consumption, composition, and transport results, while assigning probability, force, entropy, gravity, and continuation laws to separate source theorems.

The physically useful intuition survives: a controlled effective description has a finite tolerance to disturbance, and its weakest reserve can organize robustness calculations.

MTT does not yet select one universal perturbation metric, cost, free operation class, or conservation law for every encoding. This paper therefore establishes a reusable conditional framework, not a universal physical resource theory.

</div>

# Introduction and roadmap

The word *resource* has several meanings in physics and mathematics. Energy is a conserved or exchanged dynamical quantity. Entanglement is a resource only relative to a specified class of free operations. A robust control margin is a budget because it measures the smallest allowed perturbation that destroys stability. These meanings cannot be exchanged by analogy.

The corrected capacity paper defines a sourced, dimensionless reserve vector, a bottleneck scalar, and a metric distance to inadmissibility . The MTT Foundation owns the complete ledger of conditions being summarized . Those constructions answer:

> How close is this declared effective description to failure?

This paper addresses the next question:

> Under what additional assumptions does that clearance become a usable control budget or a resource monotone?

The answer is deliberately layered.

1.  Section <a href="#sec:levels" data-reference-type="ref" data-reference="sec:levels">2</a> distinguishes a diagnostic margin, an operational budget, a resource theory, and a physical field or charge.

2.  Sections <a href="#sec:budget" data-reference-type="ref" data-reference="sec:budget">3</a>–<a href="#sec:composition" data-reference-type="ref" data-reference="sec:composition">5</a> define perturbation budgets and prove their robustness, consumption, and composition properties.

3.  Section <a href="#sec:resource" data-reference-type="ref" data-reference="sec:resource">6</a> states what is still required for a genuine resource theory.

4.  Section <a href="#sec:examples" data-reference-type="ref" data-reference="sec:examples">7</a> gives concrete operator and algorithmic examples.

5.  Section <a href="#sec:limits" data-reference-type="ref" data-reference="sec:limits">8</a> identifies the former deductions that do not follow.

6.  Sections <a href="#sec:mtt" data-reference-type="ref" data-reference="sec:mtt">9</a>–<a href="#sec:contract" data-reference-type="ref" data-reference="sec:contract">10</a> locate the framework within MTT and give a falsifiable completion contract.

# Four levels that must not be conflated

<div class="definition">

**Definition 1** (Diagnostic capacity). A diagnostic capacity record consists of normalized signed slacks
``` math
r(x)=\bigl(r_i(x)\bigr)_{i\in\mathcal I}
```
for a finite list of sourced admissibility conditions. Its signed bottleneck and clipped scalar are
``` math
D(x)=\min_i r_i(x),
 \qquad
 C(x)=\min\{1,\max\{0,D(x)\}\}.
```

</div>

This level says which certificate is closest to failure. It is defined by the normalized-margin paper . A value of $`C=0.2`$ has no operational meaning until the normalization and perturbations are stated.

<div class="definition">

**Definition 2** (Operational control budget). An operational control budget specifies what disturbances are allowed, how they act, and how much they cost. Its value at $`x`$ is the least cost of a disturbance that takes $`x`$ outside the declared admissible set.

</div>

This is analogous to a stability radius in robust control, where distance to instability is defined relative to a structured perturbation class . Different uncertainty structures can give different radii for the same unperturbed system.

<div class="definition">

**Definition 3** (Resource theory). A resource theory specifies objects, allowed compositions, a distinguished class of free objects or free operations, and a conversion preorder. A resource monotone is a function whose allowed direction under free operations is fixed by that theory.

</div>

This usage follows the general mathematical theory of resources . Quantum resource theories likewise begin with operational restrictions rather than with a scalar alone .

<div class="definition">

**Definition 4** (Dynamical or physical resource). A dynamical resource is a quantity entering a supplied action, Hamiltonian, continuity equation, balance law, channel capacity, or constitutive relation. Its units, exchange law, sources, and observables are part of the model.

</div>

The implications run only downward after extra data are supplied. A diagnostic margin can become an operational budget. A budget can be placed inside a resource theory. A resource monotone can enter a physical model. None of those promotions is automatic.

<div class="center">

<div class="tabularx">

@L0.23Y Y@ Level & Required data & What is not yet supplied
Diagnostic margin & Slacks, units, scales, norms, tolerances, provenance & Perturbation meaning and cost
Operational budget & Allowed perturbations, action, cost, failure set & Free operations and conversion order
Resource theory & Objects, free operations, composition, monotones & A physical conservation or exchange law
Physical resource & Action or constitutive law, units, sources, observables & Nothing further only if the complete physical model is supplied

</div>

</div>

# Perturbation models and the robust budget

<div id="def:perturbation" class="definition">

**Definition 5** (Perturbation model). A perturbation model is a tuple
``` math
\mathcal R_{\rm ctrl}
 =
 \bigl(
 \mathcal X,\mathcal A,\mathcal P,\odot,c,\mathcal D,\pi
 \bigr),
```
where:

1.  $`\mathcal X`$ is the state-and-control space and $`\mathcal A\subseteq\mathcal X`$ the declared admissible set;

2.  $`\mathcal P_x`$ is the set of perturbations allowed at $`x`$;

3.  $`p\odot x`$ is the perturbed state when defined;

4.  $`c_x(p)\in[0,\infty]`$ is its cost;

5.  $`\mathcal D`$ records domains, regularity, and composition conventions; and

6.  $`\pi`$ records the source and units of all these choices.

</div>

<div id="def:exitbudget" class="definition">

**Definition 6** (Exit budget). For $`x\in\mathcal A`$, define
``` math
B_{\mathcal R}(x)
 =
 \inf\bigl\{
 c_x(p):p\in\mathcal P_x,\ p\odot x\notin\mathcal A
 \bigr\}.
```
If no allowed perturbation exits $`\mathcal A`$, set $`B_{\mathcal R}(x)=+\infty`$.

</div>

The budget is relative to $`\mathcal P`$ and $`c`$. Restricting perturbations can increase it; changing the cost units rescales it. These are not defects. They are why the perturbation model belongs in every statement.

## Metric perturbations

Suppose $`(\mathcal X,d)`$ is a metric space, every $`y\in\mathcal X`$ can be treated as the endpoint of an allowed perturbation from $`x`$, and its cost is $`c_x(y)=d(x,y)`$. Then Definition <a href="#def:exitbudget" data-reference-type="ref" data-reference="def:exitbudget">6</a> becomes
``` math
B_d(x)=\operatorname{dist}_d(x,\mathcal X\setminus\mathcal A).
```

<div id="thm:ball" class="theorem">

**Theorem 7** (Maximal guaranteed perturbation ball). *Let $`\mathcal A`$ be open in $`(\mathcal X,d)`$, and let $`x\in\mathcal A`$. Then:*

1.  *every $`y`$ with $`d(x,y)<B_d(x)`$ lies in $`\mathcal A`$;*

2.  *for every $`\varepsilon>0`$, there exists $`z\in\mathcal X\setminus\mathcal A`$ with $`d(x,z)<B_d(x)+\varepsilon`$, unless the complement is empty.*

*Thus $`B_d(x)`$ is exactly the supremal radius of an open metric ball around $`x`$ guaranteed to remain admissible.*

</div>

<div class="proof">

*Proof.* If $`d(x,y)<B_d(x)`$ and $`y\notin\mathcal A`$, then $`y`$ belongs to the set over which the defining infimum is taken, contradicting $`B_d(x)\le d(x,y)`$. The second statement is the defining approximation property of an infimum. ◻

</div>

This theorem supplies a precise sense in which capacity is a resource: it is a tolerance budget for a declared class of perturbations. It does not say that the budget is carried by a new physical field.

## Controlled transport between equivalent models

A coordinate or representation change need not preserve a numerical budget exactly. It does preserve the budget up to explicit constants when the change controls distances in both directions.

<div id="thm:transport" class="theorem">

**Theorem 8** (Bi-Lipschitz transport of exit budgets). *Let $`(\mathcal X,d_X)`$ and $`(\mathcal Y,d_Y)`$ be metric spaces with admissible sets $`\mathcal A_X\subseteq\mathcal X`$ and $`\mathcal A_Y\subseteq\mathcal Y`$. Suppose $`F:\mathcal X\to\mathcal Y`$ is a bijection satisfying
``` math
F(\mathcal A_X)=\mathcal A_Y
```
and, for constants $`0<m\le M<\infty`$,
``` math
m\,d_X(x,z)
 \le
 d_Y(Fx,Fz)
 \le
 M\,d_X(x,z)
 \qquad(x,z\in\mathcal X).
```
Then the metric exit budgets obey
``` math
m\,B_X(x)
 \le
 B_Y(Fx)
 \le
 M\,B_X(x)
 \qquad(x\in\mathcal A_X).
```*

</div>

<div class="proof">

*Proof.* Bijectivity and $`F(\mathcal A_X)=\mathcal A_Y`$ imply $`F(\mathcal X\setminus\mathcal A_X)=\mathcal Y\setminus\mathcal A_Y`$. Therefore
``` math
B_Y(Fx)
 =
 \inf_{z\notin\mathcal A_X}d_Y(Fx,Fz).
```
Applying the two metric-comparison inequalities inside the infimum gives the result. ◻

</div>

Exact invariance is the special case $`m=M=1`$. A one-sided Lipschitz map, a nonbijective projection, or a map that does not carry the complete failure set to the complete failure set does not satisfy this theorem. Those cases require their own decoder or quotient analysis.

## Connecting the budget to normalized margins

Let $`D(x)=\min_i r_i(x)>0`$ be a normalized bottleneck. Suppose the margin map is $`L`$-Lipschitz in the sup norm:
``` math
\|r(y)-r(x)\|_\infty\le Ld(x,y).
```
Then the perturbation proposition in the capacity paper gives
``` math
B_d(x)\ge\frac{D(x)}{L}.
```
The margin value is therefore a certified *lower bound* on the true metric exit budget. Equality needs an active perturbation reaching the boundary at that cost. It cannot be inferred from Lipschitz continuity alone.

# Cumulative consumption and repair

An operational budget becomes especially useful for sequences of controlled transformations.

<div id="ass:consumption" class="assumption">

**Assumption 9** (Rowwise consumption bound). Let $`x_0,x_1,\ldots,x_N\in\mathcal X`$, and let $`r_i(x)`$ be normalized signed reserves. For every step $`k`$, suppose a nonnegative consumption vector
``` math
a^{(k)}=\bigl(a_i^{(k)}\bigr)_{i\in\mathcal I}
```
is certified such that
``` math
r_i(x_{k+1})
 \ge
 r_i(x_k)-a_i^{(k)}
 \qquad
 \text{for all }i.
```

</div>

<div id="thm:cumulative" class="theorem">

**Theorem 10** (Cumulative budget certificate). *Under Assumption <a href="#ass:consumption" data-reference-type="ref" data-reference="ass:consumption">9</a>,
``` math
r_i(x_N)
 \ge
 r_i(x_0)-\sum_{k=0}^{N-1}a_i^{(k)}
 \qquad
 \text{for every }i.
```
Hence the complete sequence remains admissible whenever
``` math
\sum_{k=0}^{N-1}a_i^{(k)}<r_i(x_0)
 \qquad
 \text{for every }i.
```
A simpler sufficient condition is
``` math
\sum_{k=0}^{N-1}\|a^{(k)}\|_\infty<D(x_0).
```*

</div>

<div class="proof">

*Proof.* Iterating the rowwise inequality gives the first display. If each final lower bound is positive, every final reserve is positive. For the scalar condition,
``` math
\sum_k a_i^{(k)}
 \le
 \sum_k\|a^{(k)}\|_\infty
 <
 D(x_0)
 \le r_i(x_0)
```
for every row $`i`$. ◻

</div>

The vector condition is sharper than the scalar one because different operations may consume different rows. An operation that spends spectral gap need not spend the same amount of truncation reserve.

## Repair and feedback

The inequality in Assumption <a href="#ass:consumption" data-reference-type="ref" data-reference="ass:consumption">9</a> is one-sided. A repair or feedback operation can increase some $`r_i`$. Redundancy can move the effective state farther from a failure set. Re-estimating an operator in a better norm can improve a certified lower bound without changing the physical state.

Therefore capacity is not generally conserved. A balance equation would need to distinguish:
``` math
\text{consumption},\qquad
 \text{repair},\qquad
 \text{exchange},\qquad
 \text{reclassification}.
```
The capacity definition supplies none of those rates.

# Composition laws

Resource language is incomplete without composition. Even in the simplest independent case, the natural law is a bottleneck rather than a sum.

<div id="thm:parallel" class="theorem">

**Theorem 11** (Independent parallel bottleneck). *Let $`(\mathcal X_A,d_A)`$ and $`(\mathcal X_B,d_B)`$ have open admissible sets $`\mathcal A_A`$ and $`\mathcal A_B`$. Equip $`\mathcal X_A\times\mathcal X_B`$ with the max-product metric
``` math
d_\infty\bigl((x_A,x_B),(y_A,y_B)\bigr)
 =
 \max\{d_A(x_A,y_A),d_B(x_B,y_B)\},
```
and let the product admissible set be $`\mathcal A_A\times\mathcal A_B`$. Then
``` math
B_\infty(x_A,x_B)
 =
 \min\{B_A(x_A),B_B(x_B)\}.
```*

</div>

<div class="proof">

*Proof.* The complement of the product admissible set is
``` math
\bigl((\mathcal X_A\setminus\mathcal A_A)\times\mathcal X_B\bigr)
 \cup
 \bigl(\mathcal X_A\times(\mathcal X_B\setminus\mathcal A_B)\bigr).
```
The distance to the first set is $`B_A(x_A)`$, because the second coordinate may remain fixed; the distance to the second is $`B_B(x_B)`$. Distance to their union is the minimum of the two distances. ◻

</div>

Parallel capacity is therefore limited by the weaker subsystem. This is not an extensive thermodynamic law.

## Coupled and redundant systems

If the admissible set is not a Cartesian product, Theorem <a href="#thm:parallel" data-reference-type="ref" data-reference="thm:parallel">11</a> does not apply. Coupling can introduce new joint failure surfaces. Conversely, an error-correcting code can make the logical admissible set larger than the naive product. A legitimate composition theorem must specify:

1.  the joint state space and metric;

2.  the joint admissible set;

3.  correlations in the perturbation family;

4.  encoding and decoding maps;

5.  resources consumed by repair; and

6.  whether the reported budget is component, logical, or end-to-end.

There is no universal formula $`B_{AB}=B_A+B_B`$. Additivity, subadditivity, or superadditivity is a model result.

# When does this become a resource theory?

Let $`\mathcal S`$ be a class of states and $`\mathcal F`$ a class of operations closed under identity and composition. Define a convertibility preorder by
``` math
x\succeq_{\mathcal F} y
 \quad\Longleftrightarrow\quad
 y=F(x)\text{ for some }F\in\mathcal F.
```
A conventional resource monotone $`M`$ satisfies
``` math
M(F(x))\le M(x)
 \qquad(F\in\mathcal F).
```
Whether larger or smaller numerical values mean “more resource” is a convention, but the allowed direction must be consistent.

<div id="prop:notmonotone" class="proposition">

**Proposition 12** (Capacity is not automatically a monotone). *An exit budget $`B`$ need not be monotone under an arbitrary admissibility- preserving operation. In particular, a repair operation can map $`x`$ to a state $`F(x)`$ with $`B(F(x))>B(x)`$, while a degrading operation can produce $`B(F(x))<B(x)`$.*

</div>

<div class="proof">

*Proof.* Take $`\mathcal X=\mathbb R`$, $`\mathcal A=(-1,1)`$, and $`B(x)=1-|x|`$. On the admissible subdomain $`(0,1)`$, the map $`F_{\rm repair}(x)=x/2`$ satisfies
``` math
B(F_{\rm repair}(x))=1-\frac{x}{2}>1-x=B(x),
```
whereas $`F_{\rm degrade}(x)=(x+1)/2`$ satisfies
``` math
B(F_{\rm degrade}(x))
 =
 \frac{1-x}{2}
 <
 1-x
 =
 B(x).
```
Both maps take $`(0,1)`$ into $`(0,1)`$. ◻

</div>

The example is elementary, but the lesson is general. If repair is free, capacity can be created for free and is not a resource monotone in the usual direction. If repair consumes ancillas, work, communication, or control authority, those inputs must be included in the resource ledger.

## A valid model-specific monotone

One can still define a resource theory by choosing free operations that obey a declared comparison. For example, suppose every $`F\in\mathcal F`$ has a certified constant $`\alpha_F>0`$ such that
``` math
B(F(x))\ge\alpha_F B(x).
```
This is a robustness-preservation guarantee, not a monotonicity theorem. Alternatively, choose operations satisfying $`B(F(x))\le B(x)`$ and use $`B`$ as a consumable monotone. The choice depends on the operational task.

<div class="definition">

**Definition 13** (Capacity-resource completion). A capacity record is promoted to a capacity resource theory only when the following are supplied:
``` math
\bigl(
 \mathcal S,\mathcal F,\otimes,\succeq_{\mathcal F},
 B,\text{conversion rates},\text{catalysts},
 \text{error convention}
 \bigr).
```

</div>

This is the same discipline used in established resource theories: the restriction on operations gives the resource its meaning .

# Concrete conditional examples

## Spectral-gap robustness

Let $`A`$ be a Hermitian matrix with a selected spectral cluster separated from the remainder by a gap $`\gamma>0`$. Let $`E`$ be a Hermitian perturbation. Standard spectral perturbation theory bounds eigenvalue motion by $`\|E\|`$ and invariant-subspace rotation in terms of the gap .

If the two sides of the selected gap can each move by at most $`\|E\|`$, then
``` math
\operatorname{gap}(A+E)
 \ge
 \gamma-2\|E\|.
```
Thus
``` math
\|E\|<\frac{\gamma}{2}
```
is a sufficient robustness budget for preserving positive separation. It may not be the exact structured stability radius. Restrictions on the allowed perturbation matrix can increase the true budget.

This example makes every ingredient visible:

1.  the state is the operator $`A`$;

2.  the perturbations are Hermitian matrices $`E`$;

3.  the cost is the chosen operator norm;

4.  failure is closure of the selected gap; and

5.  $`\gamma/2`$ is a certified lower bound, not a new energy.

## A contraction budget

Suppose a family of maps has contraction factors $`q(x)<1`$ in a declared norm and invariant set. The normalized reserve $`1-q(x)`$ can bound how much a perturbation may increase the Lipschitz constant before contraction is lost. But the invariant-set reserve, domain, and fixed-point theorem remain separate rows. Fixed Points I owns the corresponding conditional MTT framework .

## A guarded numerical algorithm

Let an algorithm evolve while $`C(x)>0`$. Introducing
``` math
U_\varepsilon(x)=-\log\bigl(\varepsilon+C(x)\bigr)
```
and following $`-\nabla U_\varepsilon`$ makes capacity a penalty potential by explicit design. The resulting force depends on the representative $`C`$, its metric, and $`\varepsilon`$. Replacing $`C`$ by $`C^3`$ changes the trajectory even though the admissible set is unchanged.

At $`C=0`$, the algorithm still needs a guard and one of:
``` math
\text{stop},\qquad
 \text{continue in another chart},\qquad
 \text{apply a reset map or kernel}.
```
The capacity boundary does not choose the reset or its probabilities.

## A channel or experimental tolerance

An experiment may define the budget as the largest calibration error, noise strength, or control drift for which an output guarantee remains inside tolerance. This can be directly useful. It is still not the probability of an outcome. Probabilities require a state and an instrument; the budget only certifies the domain on which their predictions are controlled.

# What the budget does not derive

## No right-inverse theorem

Let $`P:\mathcal H\to P\mathcal H`$ be an orthogonal projection. If $`\ker P\ne\{0\}`$, then $`P`$ is noninjective. Nevertheless the inclusion
``` math
\iota:P\mathcal H\hookrightarrow\mathcal H
```
satisfies
``` math
P\circ\iota=\operatorname{Id}_{P\mathcal H}.
```
It is a bounded measurable right inverse. Noninjectivity prevents a left inverse that recovers every original upper state; it does not prevent a section selecting one representative.

Capacity exhaustion may invalidate a particular decoder or commuting diagram, but that requires a decoder theorem. It does not follow from noninjectivity.

## No automatic irreversibility or reset

A first exit says that one lower certificate has ended. The upper evolution may remain invertible, another lower chart may exist, or the description may simply stop. A reset law defines a hybrid system and must separately prove existence, measurability, conservation, and outcome probabilities.

## No probability

A positive scalar and a boundary do not define a normalized measure. Quadratic quantum probabilities require a state, observable algebra, and instrument or a same-source probability theorem. Capacity can restrict the domain of such a theorem but cannot replace it.

## No force or equation of motion

A gradient becomes a force only after it appears in an action, Hamiltonian, or constitutive law with declared units and sign. Arbitrary reparameterization of the same zero set changes the gradient, so a same-zero-set capacity class cannot select a unique force.

## No entropy or thermodynamics

Entropy requires a state count, measure, density operator, coarse-graining, or thermodynamic potential. A control budget can constrain accessible states without being their entropy. A conservation or balance law requires a symmetry or constitutive postulate.

## No gravity or Newton constant

Postulating
``` math
S[g,C]=\int\sqrt{-g}\,f(C)R
```
adds a scalar-tensor coupling unless $`f(C)`$ is fixed and constant. The capacity record does not select $`f`$, the Einstein-Hilbert normalization, or the observed value of $`G`$. Identifying $`G^{-1}=C`$ is also incompatible with arbitrary allowed changes of capacity representative.

## No horizon, collapse, or arrow of time

Horizons require Lorentzian causal geometry and field equations. Measurement requires a system-apparatus interaction and outcome records. An arrow of time requires asymmetric dynamics, boundary conditions, record stability, or thermodynamic structure. A list of first-exit events does not supply those ingredients.

# Role within Modal Triplet Theory

The capacity papers now have distinct roles.

<div class="center">

<div class="tabularx">

@L0.28Y@ Source & Canonical responsibility
MTT Foundation & Complete admissibility ledger, independent control rows, and the stop/continue/reset alternatives .
Coherence Capacity: normalized margins & Signed slacks, normalization scales, reserve vector, bottleneck scalar, metric clearance, active rows, and capacity-equivalence class .
This paper & Perturbation model, exit budget, maximal guaranteed ball, cumulative consumption, independent composition, and resource-completion contract.
Fixed Points I & Conditional spectral-projector, invariant-set, existence, contraction, and stability gates .
Future dynamics papers & Any transport, repair, exchange, conservation, force, entropy, or geometric response law.

</div>

</div>

This hierarchy prevents a loop. One first proves the control rows, then normalizes them, then defines an operational perturbation budget, and only then asks whether a task-specific resource theory or physical law exists.

# Completion contract and falsifiability

A claim that coherence capacity is a resource for a particular model must publish at least the following rows.

<div class="center">

<div class="tabularx">

@L0.25Y@ Row & Required content
State and domain & State space, operator domains, boundary conditions, and admissible set.
Capacity source & Full normalized reserve vector, scales, tolerances, provenance, and active row; never the scalar alone.
Perturbations & Allowed structured disturbances and their action on states.
Cost & Metric or cost functional, units, uncertainty, and normalization.
Budget theorem & Exact radius or certified lower and upper bounds with error control.
Composition & Parallel, sequential, correlated, and redundant composition rules.
Free operations & Operations regarded as costless and proof that they preserve the required closure properties.
Monotone direction & Whether capacity must increase, decrease, or remain comparable under free operations.
Repair ledger & Ancillas, work, communication, feedback, or other resources consumed by stabilization.
Physical promotion & Separate action, instrument, measure, entropy, or geometry theorem if a physical interpretation is claimed.
Provenance & Source-independent inputs, fitted inputs, held-out outputs, intervals, code, commit, and hashes for numerical values.

</div>

</div>

The framework is falsifiable at several levels. A claimed radius fails if an allowed cheaper perturbation exits the admissible set. A claimed composition law fails if a joint perturbation violates its bound. A resource monotone fails if a declared free operation moves it in the forbidden direction. A physical promotion fails if the predicted observable or held-out comparison fails. These are stronger tests than asking whether a scalar happened to vanish at a chosen boundary.

# Conclusion

Coherence capacity can be a genuine *control budget*: after the perturbations and their cost are fixed, it measures the least disturbance that destroys a declared effective description. That interpretation gives precise robustness, cumulative-consumption, and composition theorems.

It is not, by definition, the fundamental resource of all effective physics. A resource theory needs operational restrictions and conversion rules. A physical resource needs dynamics, units, sources, and observables. Keeping those levels separate makes the capacity idea more useful, because each proposed application now has an exact completion contract and an observable failure mode.

# Reproducibility statement

This paper reports structural definitions and proofs, not a fitted parameter or numerical physical prediction. The source TeX, bibliography, revision audit, and generated PDF are versioned in the MTT papers repository. A future numerical control-budget result must additionally archive its perturbation family, cost, full reserve vector, active rows, interval bounds, code commit, and verification hashes.
