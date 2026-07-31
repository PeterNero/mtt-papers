---
abstract: |
  Projection can discard information without selecting a network geometry. This paper develops a rigorous Modal Triplet Theory (MTT) framework in which observable motif constraints are determined from the actual image
  ``` math
  \mathcal R=F(\mathcal A)\subseteq\mathcal M,
  ```
  where $`\mathcal A`$ is a declared admissible source domain and $`F`$ includes projection, network extraction, and motif measurement. Compatibility constraints are properties of $`\mathcal R`$, not consequences of noninvertibility by itself. We give an exact recombination test for support nonfactorization, a graph-of-a-map sufficient condition, and a regular-value description of local image geometry. A covering-map counterexample proves that failure of a continuous section is compatible with a full product image. We also separate three distinct objects: an embedded physical network, a constrained motif support, and a statistical conditional-dependence graph.

  For a declared local reserve model, we derive a useful conditional result. If the leading coherence deficit is
  ``` math
  Q(\beta,q_\parallel,q_\perp)
    =a\beta^2+b(q_\parallel^2+q_\perp^2)+cq_\parallel^2,
    \qquad a,b,c>0,
  ```
  then every admissible branch of thickness $`\rho=(q_\parallel^2+q_\perp^2)^{1/2}`$ satisfies $`\rho\leq\sqrt{C/b}`$. Near saturation, the dominant channel is forced to remain nearly straight and the branch nearly orthogonal. The estimate is stable under a relative remainder bound. This proves the square-root law inside the stated quadratic model; it does not derive the model, its coefficients, a branch-creation law, or universal empirical prevalence. Those require a selected network source, Hessian, extraction pipeline, and probability or growth dynamics. The result is a falsifiable conditional encoding rather than a universal theory of network morphology.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: d03c6de4843fc501295fd52cadcbb33cb25ad2da36881497e2593dfb7c8e74b6
paper_id: projection-induced-network-geometry-sprouting-hidden-co-6919523e
release_state: zenodo_released
released_version: v2
title: |
  **Admissible Image Geometry for Network Motifs in Modal Triplet Theory**
  Conditional Correlations, Sprout Bounds, and What Projection Alone Does Not Imply
zenodo_doi: 10.5281/zenodo.21714026
zenodo_record_id: 21714026
zenodo_url: "https://zenodo.org/records/21714026"
---

# Version 2 revision note

<div class="description">

Version 1, DOI <https://doi.org/10.5281/zenodo.18274629>.

Version 1 treated the absence of a global reconstruction map as if it forced a proper, nonfactorizing motif image and then used that inference to derive specific graph geometry, sprout prevalence, and a universal square-root law. None of those implications follows from noninvertibility alone.

Version 2 defines the image $`\mathcal R=F(\mathcal A)`$ explicitly, supplies direct tests for its geometry, separates image constraints from graph extraction and statistical dependence, and states the sprout result as a theorem of a declared positive quadratic reserve model.

The useful local idea survives: a selected positive Hessian can make bending and longitudinal branch growth more expensive than a transverse thin mode. Near a small reserve boundary, that anisotropy yields a controlled, approximately orthogonal sprout bound.

MTT has not yet selected a physical network source, the map $`F`$, the coefficients $`a,b,c`$, a capacity calibration, or a growth law for any biological or engineered system. Cross-domain universality and empirical prevalence are therefore open.

</div>

# The question this paper can answer

Networks appear in vasculature, leaf venation, fungal growth, neural arborization, infrastructure, and many other settings. Their common visual vocabulary does not imply a common microscopic cause. Even within transport networks, optimization, adaptation, damage tolerance, fluctuating loads, and tissue growth can produce different structures . Network motifs are useful empirical summaries, but a repeated motif is not itself a derivation of its mechanism .

The narrow MTT question is this:

> Given a selected source domain, a selected projection and extraction map, and a certified local reserve function, what restrictions follow for the observable motif image?

This question is mathematically meaningful. It is also weaker than the claim that projection alone explains real network morphology. The difference matters. A many-to-one map tells us that some source information was forgotten. It does not tell us which motifs remain, which edges appear, or how probability is distributed over the surviving motifs.

Version 2 therefore uses four rules.

1.  The realizable set is computed from the image of a declared map.

2.  Nonfactorization is proved by a failed recombination or an explicit coupled constraint.

3.  Graph topology is supplied by an extraction rule, not inferred from correlation.

4.  A prevalence statement requires a measure or dynamics in addition to a feasible set.

These rules turn the paper from a universality claim into a reusable conditional framework.

# Typed source, image, and graph objects

## The full map

Let $`\mathcal X`$ be a source configuration space and let $`\mathcal A\subseteq\mathcal X`$ be the domain on which the relevant MTT source, projector, and stability conditions have been verified. Let
``` math
P:\mathcal A\longrightarrow\mathcal Y
```
be the effective projection. Network extraction is a separate map
``` math
\Gamma:\mathcal Y\longrightarrow\mathcal G,
```
where an element of $`\mathcal G`$ contains a graph, an embedding when relevant, and edge attributes such as radius or conductivity. Finally, let
``` math
m:\mathcal G\longrightarrow\mathcal M
```
be the declared motif-measurement map. The complete observable map is
``` math
F=m\circ\Gamma\circ P:\mathcal A\longrightarrow\mathcal M.
```

<div class="definition">

**Definition 1** (Admissible motif image). The realizable motif support of the declared construction is
``` math
\mathcal R:=F(\mathcal A)\subseteq\mathcal M.
```
If the source carries a probability measure $`\nu`$, its observable law is $`\mu=F_\ast\nu`$. The pair $`(\mathcal R,\mu)`$ contains more information than either object alone.

</div>

Every arrow in this definition has an owner. Changing the skeletonization algorithm changes $`\Gamma`$. Changing how a junction is measured changes $`m`$. Changing the coherent branch or projector changes $`P`$ and possibly $`\mathcal A`$. Those changes need not preserve $`\mathcal R`$.

## Motif coordinates

For a degree-three embedded junction, a convenient local coordinate chart is
``` math
u=(\beta,q_\parallel,q_\perp,\eta)\in\mathbb R^4.
```
Here $`\beta`$ measures bending of a declared dominant channel, $`q_\parallel`$ and $`q_\perp`$ are longitudinal and transverse components of a candidate third branch, and $`\eta`$ collects any additional measured attribute such as taper or imbalance. Define
``` math
\rho=\sqrt{q_\parallel^2+q_\perp^2}.
```
When $`\rho>0`$, the branch angle $`\phi`$ relative to the dominant channel satisfies
``` math
\cos\phi=\frac{q_\parallel}{\rho}.
```
Thus $`q_\parallel=0`$ means an orthogonal branch in this local chart.

These variables are measurements after $`\Gamma`$ and $`m`$. They do not create a graph edge. A branch must already have been detected by the network-extraction rule before its angle and thickness can be measured.

# What failure of reconstruction does not prove

Projection and reconstruction are easily confused. A section of $`P:\mathcal A\to P(\mathcal A)`$ is a map $`s`$ with $`P\circ s=\mathrm{id}`$. Its existence depends on the regularity category: set-theoretic, measurable, continuous, smooth, or connection-preserving sections are different claims. Version 1 did not keep those categories separate.

<div class="proposition">

**Proposition 2** (No section does not determine image geometry). *There is a continuous surjection onto a full product space that has no continuous global section.*

</div>

<div class="proof">

*Proof.* Consider
``` math
p:S^1\times[-1,1]\longrightarrow S^1\times[-1,1],
  \qquad p(z,t)=(z^2,t).
```
It is onto, so its image is the complete product $`S^1\times[-1,1]`$. If a continuous section existed, the induced maps on the fundamental group of the circle factor would satisfy $`p_\ast s_\ast=\mathrm{id}_{\mathbb Z}`$. But $`p_\ast`$ is multiplication by $`2`$, so this would require an integer $`k`$ with $`2k=1`$, which is impossible. ◻

</div>

The example has two consequences. First, lack of a continuous section does not imply that the image is a proper subset of the target. Second, it does not imply coupled coordinate constraints. A reconstruction obstruction describes the fibers or topology of a map; image geometry must be determined separately.

The measurable case requires its own theorem and hypotheses. One must not take failure of a continuous section and silently promote it to failure of a measurable section. Standard measurable-selection results make such a promotion particularly unsafe .

<div class="corollary">

**Corollary 3** (Correct use of no-section results). *A no-section theorem can falsify a claim that explicitly requires a section of the same regularity on the same domain. By itself it cannot prove that $`\mathcal R`$ is proper, nonfactorizing, low-dimensional, graph-like, or sprout-selecting.*

</div>

# Direct tests for hidden compatibility

## Support factorization

Suppose the motif chart is a product
``` math
\mathcal M=M_1\times\cdots\times M_k
```
with coordinate projections $`\pi_i`$. There are at least two notions of factorization.

<div class="definition">

**Definition 4** (Support factorization). A subset $`\mathcal R\subseteq\mathcal M`$ factorizes by coordinates if
``` math
\mathcal R=\prod_{i=1}^k\pi_i(\mathcal R).
```
Failure of this equality means that some individually realizable coordinate values cannot be recombined into a jointly realizable motif.

</div>

<div class="definition">

**Definition 5** (Probabilistic factorization). A probability law $`\mu`$ on $`\mathcal M`$ factorizes if
``` math
\mu=\mu_1\otimes\cdots\otimes\mu_k
```
for its coordinate marginals. This is a statement about a law, not only its support.

</div>

<div class="proposition">

**Proposition 6** (Recombination certificate). *If $`u,v\in\mathcal R`$ and a point $`w`$ obtained by taking at least one coordinate from $`u`$ and another from $`v`$ is not in $`\mathcal R`$, then $`\mathcal R`$ does not factorize.*

</div>

<div class="proof">

*Proof.* Every coordinate of $`w`$ belongs to the corresponding projection $`\pi_i(\mathcal R)`$. Hence $`w`$ belongs to $`\prod_i\pi_i(\mathcal R)`$. Since $`w\notin\mathcal R`$, equality with that product is impossible. ◻

</div>

This gives a finite falsification certificate when membership in $`\mathcal R`$ can be checked. It also identifies what must be computed: two accepted motifs and one rejected recombination from the same frozen source and extraction rule.

## Constraint and graph forms

An explicit constraint can describe the image locally. Let $`h:\mathcal M\to\mathbb R^r`$ be continuously differentiable and suppose that the declared image is contained in $`h^{-1}(0)`$.

<div class="proposition">

**Proposition 7** (Regular local image constraint). *If $`0`$ is a regular value of $`h`$, then $`h^{-1}(0)`$ is a submanifold of codimension $`r`$. If $`\mathcal R`$ contains a relatively open subset of this level set, then the stated equations give its local compatibility geometry.*

</div>

<div class="proof">

*Proof.* This is the regular-value theorem . ◻

</div>

Codimension alone does not identify which variables are coupled. A direct and useful sufficient condition is a graph relation.

<div class="proposition">

**Proposition 8** (Graph-of-a-map nonfactorization). *Let $`U\subseteq M_1`$ and let $`f:U\to M_2`$ be nonconstant. Then
``` math
\mathcal R_f=\{(x,f(x)):x\in U\}
```
does not factorize as $`\pi_1(\mathcal R_f)\times\pi_2(\mathcal R_f)`$.*

</div>

<div class="proof">

*Proof.* Choose $`x_1,x_2`$ with $`f(x_1)\neq f(x_2)`$. Both $`(x_1,f(x_1))`$ and $`(x_2,f(x_2))`$ lie in $`\mathcal R_f`$, while the recombination $`(x_1,f(x_2))`$ does not. Apply the recombination certificate. ◻

</div>

In an MTT application, $`h`$ or $`f`$ must come from a selected source calculation, a certified reduced equation, or a declared phenomenological model. Writing the symbol $`\mathcal R`$ does not establish any constraint.

# Correlation constraints are not graph edges

Three different uses of the word “network” must be separated.

1.  A *physical or geometric graph* has vertices and edges extracted by $`\Gamma`$ from an image, flow field, point cloud, or other effective state.

2.  A *motif support* is a set $`\mathcal R\subseteq\mathcal M`$ of allowed measurements.

3.  A *statistical graph* encodes conditional independences of a probability law.

None determines the others without additional assumptions. In particular, a correlated pair of motif coordinates is not a new physical edge. Conversely, two physical edges can carry independent measured attributes. Graphical-model edges require a specified law and a Markov convention .

<div class="proposition">

**Proposition 9** (Support does not determine dependence). *The square $`[-1,1]^2`$ supports both an independent distribution and a correlated distribution with a strictly positive density everywhere.*

</div>

<div class="proof">

*Proof.* The uniform density $`f_0(x,y)=1/4`$ is independent. For $`0<|\epsilon|<1`$, define
``` math
f_\epsilon(x,y)=\frac14(1+\epsilon xy).
```
It is positive and normalized on the same square. Its marginals are uniform, but
``` math
\mathbb E_\epsilon[XY]=\frac{\epsilon}{9}\neq0.
```
Thus identical full support is compatible with different dependence. ◻

</div>

<div class="proposition">

**Proposition 10** (Dependence does not determine a physical graph). *Fix any nonproduct law on a two-coordinate motif space. The same law can be attached to different embedded graphs by changing the extraction map $`\Gamma`$ while leaving the measured coordinate pair unchanged.*

</div>

<div class="proof">

*Proof.* For example, assign the same joint attribute law to two marked branches in a three-edge star or to two marked edges in a cycle. The coordinate law is unchanged while the physical edge sets differ. ◻

</div>

The corrected chain is therefore
``` math
\text{source}
  \xrightarrow{P}
  \text{effective state}
  \xrightarrow{\Gamma}
  \text{physical graph}
  \xrightarrow{m}
  \text{motif coordinates}.
```
A statistical graph may be inferred only after a law on those coordinates has also been supplied.

# How a local reserve model can arise

## Full and reduced quadratic forms

Near a selected reference configuration, a twice differentiable deficit or action can be expanded in visible motif coordinates $`u`$ and hidden response coordinates $`z`$:
``` math
D(u,z)
  =
  D(0,0)
  +\frac12
  \begin{pmatrix}u\\ z\end{pmatrix}^{\!T}
  \begin{pmatrix}A&B\\ B^T&D\end{pmatrix}
  \begin{pmatrix}u\\ z\end{pmatrix}
  +R_3(u,z).
```
The notation $`D`$ for both the hidden block and the full deficit is avoided below by writing the hidden block as $`H_{zz}`$.

<div class="theorem">

**Theorem 11** (Schur-complement reduction). *Let
``` math
H=
  \begin{pmatrix}H_{uu}&H_{uz}\\H_{zu}&H_{zz}\end{pmatrix}
```
be symmetric with $`H_{zz}>0`$. Minimizing the quadratic form over $`z`$ gives
``` math
\inf_z\frac12
  \begin{pmatrix}u\\z\end{pmatrix}^{\!T}
  H
  \begin{pmatrix}u\\z\end{pmatrix}
  =
  \frac12u^TH_{\mathrm{eff}}u,
\qquad
  H_{\mathrm{eff}}
  =
  H_{uu}-H_{uz}H_{zz}^{-1}H_{zu}.
```
If $`H>0`$, then $`H_{\mathrm{eff}}>0`$.*

</div>

<div class="proof">

*Proof.* Complete the square using $`z_\ast=-H_{zz}^{-1}H_{zu}u`$. Positivity of the Schur complement follows from positivity of $`H`$ . ◻

</div>

This theorem explains how a local visible Hessian can be computed from a larger source Hessian. It does not guarantee any particular entries. In a physical MTT network model, $`H`$ must come from the same selected source that defines $`P`$ and $`\mathcal A`$, and the remainder $`R_3`$ needs a certified bound.

## The anisotropic sprout chart

Take
``` math
u=(\beta,q_\parallel,q_\perp).
```
The simplest positive quadratic model that penalizes bending, total branch size, and longitudinal alignment is
``` math
Q(u)
  =
  a\beta^2
  b(q_\parallel^2+q_\perp^2)
  cq_\parallel^2,
  \qquad a,b,c>0.
```
The coefficient $`b`$ is the isotropic branch-size cost. The coefficient $`c`$ is an additional longitudinal penalty. Such a diagonal form may result from symmetry or from diagonalizing a positive local Hessian, but the identification of the eigenvectors with physical bend and branch directions is an extra source statement.

For a reserve $`C>0`$, define the local feasible image
``` math
\mathcal R_C^{(2)}=\{u:Q(u)\leq C\}.
```
This is an ellipsoid in local motif coordinates. Its geometry, rather than projection noninvertibility, produces the following result.

# The conditional sprout theorem

<div class="theorem">

**Theorem 12** (Quadratic reserve bound). *Let $`a,b,c,C>0`$ and let $`u\in\mathcal R_C^{(2)}`$. Then
``` math
\rho\leq\sqrt{\frac{C}{b}}.
```
Equality holds only when
``` math
\beta=0,\qquad q_\parallel=0,
```
so a saturating branch leaves the dominant channel straight and is orthogonal in the declared local chart.*

*More generally, if $`0<\lambda\leq1`$ and
``` math
\rho\geq\lambda\sqrt{\frac{C}{b}},
```
then
``` math
|\beta|
  \leq
  \sqrt{\frac{C(1-\lambda^2)}{a}},
\qquad
  |q_\parallel|
  \leq
  \sqrt{\frac{C(1-\lambda^2)}{c}}.
```
For $`\rho>0`$ this gives
``` math
\cos^2\phi
  \leq
  \frac{b(1-\lambda^2)}{c\lambda^2}.
```*

</div>

<div class="proof">

*Proof.* Since
``` math
C\geq Q
  =a\beta^2+b\rho^2+cq_\parallel^2
  \geq b\rho^2,
```
the first bound follows. Equality requires both nonnegative residual terms to vanish. Under the lower bound on $`\rho`$,
``` math
a\beta^2+cq_\parallel^2
  \leq C-b\rho^2
  \leq C(1-\lambda^2).
```
Bounding each term separately proves the next two inequalities. Divide the $`q_\parallel`$ bound by $`\rho^2\geq\lambda^2C/b`$ to obtain the angle estimate. ◻

</div>

The theorem says less, and more precisely, than Version 1. It does not say that a branch must appear. It says that if a branch in this chart uses a large fraction of the available quadratic reserve, then it must be thin on the absolute scale $`\sqrt C`$, nearly transverse, and accompanied by little dominant-channel bending.

## Controlled nonlinear remainder

A physical deficit is rarely exactly quadratic. Let
``` math
\widetilde Q(u)=Q(u)+R(u).
```

<div class="theorem">

**Theorem 13** (Relative-error stability). *Suppose $`|R(u)|\leq\epsilon Q(u)`$ on the declared chart, with $`0\leq\epsilon<1`$. If $`\widetilde Q(u)\leq C`$, then
``` math
\rho
  \leq
  \sqrt{\frac{C}{(1-\epsilon)b}}.
```*

</div>

<div class="proof">

*Proof.* The remainder bound gives $`\widetilde Q\geq(1-\epsilon)Q\geq(1-\epsilon)b\rho^2`$. ◻

</div>

An additive error $`|R|\leq\delta`$ instead yields
``` math
\rho\leq\sqrt{\frac{C+\delta}{b}}.
```
Both forms expose the verification obligation. One must state the chart, norm, remainder bound, and source of the Hessian coefficients.

## Why the exponent is not universal

<div class="proposition">

**Proposition 14** (Order of contact determines the scaling exponent). *Suppose for small $`\rho`$ the branch deficit satisfies
``` math
k_-\rho^p\leq D(\rho)\leq k_+\rho^p,
  \qquad p>0,\quad k_\pm>0.
```
Then the maximal feasible branch scale obeys
``` math
\left(\frac{C}{k_+}\right)^{1/p}
  \leq \rho_{\max}(C)
  \leq
  \left(\frac{C}{k_-}\right)^{1/p}.
```*

</div>

<div class="proof">

*Proof.* Apply the two inequalities to the condition $`D(\rho)\leq C`$ and to a trial value satisfying the upper estimate. ◻

</div>

Thus the exponent $`1/2`$ is evidence for a nondegenerate quadratic leading term. A quartic flat direction gives $`C^{1/4}`$; a nonsmooth linear cost gives $`C`$. Projection alone selects none of these.

# Feasible sets do not supply probabilities

Version 1 inferred that sprout motifs become statistically dominant near the boundary. A feasible set cannot establish that conclusion without a law.

<div class="proposition">

**Proposition 15** (No universal prevalence from support). *Let $`\mathcal R_C^{(2)}`$ contain both the origin and at least one nonzero near-saturating sprout. There are probability measures supported on the same set for which the sprout probability is $`0`$, $`1`$, or any prescribed number in $`[0,1]`$.*

</div>

<div class="proof">

*Proof.* Use a Dirac measure at the origin, a Dirac measure at a declared sprout, or their convex mixtures. ◻

</div>

A statistical theorem therefore needs one of the following:

- a source probability measure $`\nu`$ and its pushforward $`F_\ast\nu`$;

- a stochastic growth process with a stopping rule;

- a deterministic ensemble and a declared sampling measure;

- or a Gibbs, maximum-entropy, or other law justified independently.

Even then, conditioning must be specified. A concentration statement can be valid under a chosen law while failing under another law with the same support. The current MTT network program has not selected such a law.

# Boundary language and capacity

MTT coherence capacity is best treated as a sourced reserve vector or a declared normalized margin class, not as a universal scalar force. A local network model may choose a scalar reserve
``` math
C=\min_i r_i
```
or another monotone functional of certified reserve rows $`r=(r_1,\ldots,r_n)`$. That scalar is useful for a bottleneck estimate but does not reconstruct the rows or their Hessian.

For this paper, $`C`$ has only the following role:

> $`C`$ is the certified amount by which the declared local deficit may increase before leaving the selected admissible chart.

It is not automatically energy, curvature, crowding, entropy, stress, or biological fitness. A proposed observable proxy $`\widehat C`$ must be calibrated against the reserve it is intended to estimate. Monotonicity between a proxy and a geometric feature cannot be used both to define capacity and to confirm the prediction without circularity.

# A valid empirical test contract

The corrected model can be tested, but only with a predeclared data-use contract.

## Training-stage obligations

1.  Fix the network-extraction algorithm $`\Gamma`$, including resolution, pruning, junction, and thickness rules.

2.  Fix the motif map $`m`$ and the local coordinate chart $`(\beta,q_\parallel,q_\perp,\eta)`$.

3.  State how a candidate reserve or reserve proxy is obtained.

4.  Estimate or derive the local Hessian and verify $`a,b,c>0`$ on the training domain.

5.  Bound the nonlinear remainder and freeze the accepted chart.

## Held-out obligations

On data not used to choose the extraction, proxy, chart, or coefficients, test:

1.  whether observed accepted motifs lie inside the certified feasible region up to measurement error;

2.  whether the upper envelope of $`\rho`$ follows the predicted reserve scaling;

3.  whether high-reserve-fraction branches obey the bend and angle bounds;

4.  whether the same coefficients transfer across the preregistered conditions claimed by the model.

Failure of a bound with verified premises falsifies the local reserve model on that domain. Failure of an uncalibrated proxy does not falsify MTT as a whole. Conversely, a fitted square-root envelope is not a source theorem: many positive quadratic models share it.

## What would count as strong evidence

The strongest version would derive $`F`$, $`H_{\mathrm{eff}}`$, and the reserve rows from one selected source before the network measurements are used. The theorem would then predict coefficients and transfer behavior out-of-sample. A weaker but still useful phenomenological test can fit $`a,b,c`$ on one condition and validate them on another. The two evidence tiers must not be merged.

# Relation to established network models

This framework does not show that optimization is unnecessary in real networks. Established models demonstrate that optimization, damage tolerance, fluctuating loads, local adaptation, and growth can alter network topology and hierarchy . Those results are mechanisms with their own state variables and objectives.

The MTT reserve model is different. It asks whether a selected source and projection induce a constrained motif image whose local Hessian has a specific anisotropy. If so, the conditional sprout theorem follows without minimizing a global network functional. But the source of the local quadratic form still needs explanation. In some systems it may arise from elasticity, transport, growth, or an optimization principle. MTT does not erase those domain dynamics.

Nor does the framework establish a string-theory description. A minimal surface or worldsheet model can be compared only after an explicit map identifies its fields, boundary conditions, and observables with the same network construction. Similar-looking geometry is not an equivalence theorem.

# Current MTT status

Table <a href="#tab:status" data-reference-type="ref" data-reference="tab:status">1</a> prevents the conditional theorem from being read as a selected physical result.

<div id="tab:status">

| Object | Current tier | What is established or missing |
|:---|:---|:---|
| Typed chain $`F=m\circ\Gamma\circ P`$ | framework | A valid way to state a network encoding; no physical network instance is selected by the notation. |
| Image tests | exact mathematics | Recombination, graph-of-a-map, and regular-value tests are rigorous once membership or constraints are supplied. |
| No-section implication | withdrawn | No-section alone does not imply a proper or nonfactorizing image. |
| Quadratic sprout bound | conditional exact | Exact for the declared $`Q`$ and controlled under the stated remainder bound. |
| Physical network source | open | No selected MTT operator or action currently emits $`\Gamma`$, the motif chart, and the local network Hessian from one source. |
| Coefficients $`a,b,c`$ | open | Not derived for a biological, physical, or engineered network. |
| Capacity calibration | open | Curvature, crowding, and taper are not accepted universal capacity proxies. |
| Prevalence or growth law | open | A feasible image does not select a probability measure or branch-creation dynamics. |
| Cross-domain universality | not established | Similar motifs across domains do not establish a common source. |

The corrected claim ledger.

</div>

The model is therefore a conditional encoding at the representation and local reconstruction level. It is not a derivation of observed network statistics from current MTT geometry.

# Version 2 changes and reasons

| Version 1 statement | Version 2 decision | Reason |
|:---|:---|:---|
| No global reconstruction forces hidden motif constraints | Withdraw | A surjective map without a continuous section can have a full product image. |
| Local observables cannot be freely combined | Replace by a direct image test | Nonfactorization requires a failed recombination or an explicit coupled constraint. |
| Correlation constraints generate network geometry | Separate the objects | Physical edges come from $`\Gamma`$; statistical edges require a law and conditional-independence convention. |
| Sprouting is the only admissible boundary deformation | Narrow to a local quadratic theorem | The conclusion needs a positive anisotropic Hessian and a controlled remainder. |
| $`\rho_{\rm th}\sim\sqrt C`$ is universal | Make conditional | The exponent is $`1/p`$ when the first nonzero branch cost has order $`p`$. |
| Sprouts dominate boundary ensembles | Withdraw without a measure | The same support admits probability laws with any sprout prevalence. |
| Capacity proxies test the theory directly | Require calibration and held-out data | An observable proxy is not automatically the sourced reserve. |
| Optimization and string descriptions are unnecessary | Remove as a general claim | Other mechanisms can generate network structure; comparison requires an explicit common map. |

Claim-by-claim revision ledger.

# Conclusion

The central correction is simple: information loss is not geometry. Projection may make reconstruction nonunique or obstruct regular sections, but the observable network constraints live in the actual image $`\mathcal R=F(\mathcal A)`$. They must be computed or specified there.

Once that is done, MTT can support a clean local theorem. A selected positive Hessian with an extra longitudinal penalty defines an ellipsoidal reserve region. The maximal branch scale is then proportional to $`\sqrt C`$, and branches near that scale are forced to be approximately orthogonal while the dominant channel remains nearly straight. A relative remainder certificate preserves the conclusion with an explicit loss.

This is a useful result, but it is conditional. It neither creates the branch nor predicts its frequency. It does not choose graph edges, source coefficients, a biological capacity proxy, or a cross-domain growth law. Those are precisely the objects that a future selected MTT network model must emit. By separating them, Version 2 turns a broad analogy into an auditable research program with exact mathematical tests and clear failure conditions.
