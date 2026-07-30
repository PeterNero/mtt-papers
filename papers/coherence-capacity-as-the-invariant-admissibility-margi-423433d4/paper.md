---
abstract: |
  Modal Triplet Theory (MTT) uses several independent control conditions: spectral separation, projector and resolvent bounds, complementary stability, leakage control, contraction, truncation accuracy, descent, and domain or hyperbolicity requirements. A quantitative compression of these conditions must preserve their units, logical independence, and source provenance. A common zero set alone is insufficient because an arbitrary reparameterization can change gradients, rates, magnitudes, and any proposed physical coupling.

  This paper defines a *coherence-capacity record*. Each declared admissibility condition has a signed slack, a provenance, a tolerance, and a positive scale with the same units. Division by those scales produces a dimensionless reserve vector. Its minimum is the bottleneck capacity, while a separately declared metric gives a geometric clearance from the inadmissible set. We prove four elementary but useful facts: positivity of the bottleneck is exactly simultaneous satisfaction of the declared conditions; its value gives a quantitative perturbation certificate; uniform positive capacity is equivalent to a uniform reserve on a region; and controlled changes of margin coordinates or bi-Lipschitz metrics preserve a capacity *class* up to explicit comparison constants. Distance and slack definitions agree quantitatively only when an error-bound or transversality estimate is supplied.

  The scalar is therefore a normalized diagnostic compression, not a new field, conserved charge, probability, force, entropy, or gravitational coupling. Capacity exhaustion means that at least one declared certificate has reached its boundary. It does not by itself imply failure of the upper dynamics, nonexistence of a measurable section, irreversible evolution, collapse, a horizon, or an arrow of time. Those conclusions require separate dynamics, constitutive laws, instruments, or geometric theorems. The MTT Foundation remains the owner of the complete admissibility ledger and continuation alternatives; this paper supplies the metric and normalization layer needed to compare and transport that ledger without conflating quantities of different units.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v4
date: Version 4, July 2026
generated_from_main_tex_sha256: bea319301088e16a96b3e701a5a575123f6b194019d9cae9ba10e92edbdf4553
paper_id: coherence-capacity-as-the-invariant-admissibility-margi-423433d4
release_state: zenodo_released
released_version: v4
title: |
  Coherence Capacity in Modal Triplet Theory:
  Normalized Margins, Metric Clearance, and the Invariance Class
zenodo_doi: 10.5281/zenodo.21709472
zenodo_record_id: 21709472
zenodo_url: "https://zenodo.org/records/21709472"
---

# Revision note: Version 4

<div class="description">

Version 4 supersedes Version 3.0, DOI [10.5281/zenodo.18322057](https://doi.org/10.5281/zenodo.18322057).

Version 3 allowed any positive scalar with the desired zero set, asserted that all MTT controls fail simultaneously, and inferred from scalar exhaustion the absence of a global section, structural irreversibility, Einstein gravity, an arrow of time, entropy, measurement collapse, and undecidability. A common zero set cannot support those conclusions. Moreover, noninjectivity does not rule out a right inverse: an orthogonal projection has the inclusion of its range as a bounded section.

The primary object is now a sourced, dimensionless reserve vector. The scalar capacity is its declared bottleneck compression, or a normalized metric distance to the inadmissible set. The metric, norms, tolerances, scales, domain, and provenance are part of the definition. “Invariant” now means equivalence up to explicit positive comparison constants under a controlled change of record, not numerical uniqueness under arbitrary reparameterization.

The paper retains the useful idea that many independent MTT control conditions can be summarized by their weakest remaining reserve. It also retains capacity exhaustion as a precise diagnostic first-exit event.

No universal choice of metric, normalization, or margin list is selected for every MTT realization. No transport, reset, probability, force, thermodynamic, gravitational, or cosmological law is derived here.

</div>

# Introduction: the question in its correct form

An effective construction is rarely valid everywhere. A spectral cluster may cease to be isolated, a complementary resolvent may grow too large, a contraction constant may reach one, or a truncation remainder may exceed its tolerance. These are different failures measured in different units. Calling all of them “loss of closure” can be helpful prose, but it is not yet a quantitative definition.

The corrected MTT Foundation records such conditions as separate margins . It also emphasizes that the entries can fail independently and that a first exit from an admissible chart does not choose what happens next. Fixed Points I supplies the canonical conditional spectral-projector and fixed-point framework on which several of those margins are based . This paper asks the narrower question:

> How can heterogeneous admissibility margins be compressed into one useful number without erasing their units, provenance, or logical independence?

There are two sensible answers.

1.  Normalize every signed slack and retain the resulting vector. Its least component is the active bottleneck.

2.  Equip the state-and-control space with a declared metric and measure distance to the inadmissible set.

Neither answer is canonical until its scales or metric are supplied. Their numerical agreement is a theorem obligation, not a definition.

## What this paper does not attempt

The present construction is a control diagnostic. It does not derive the underlying operator, action, state, physical geometry, or continuation law. It does not turn a list of hypotheses into a new physical substance. In particular, a small reserve says that a declared approximation is fragile; it does not say that nature exerts a force in the direction of increasing reserve.

This distinction is familiar outside MTT. Spectral perturbation theory relates gaps to stability of invariant subspaces ; Feshbach–Schur analysis relates block operators and complementary resolvents to controlled effective operators . A condition or error margin organizes those estimates. It does not replace the operator theorem that produced them.

# The admissibility record

The capacity definition begins with a typed record, not with a scalar.

<div id="def:record" class="definition">

**Definition 1** (Admissibility-margin record). An admissibility-margin record on a region $`U`$ is
``` math
\mathcal R_{\rm adm}
 =
 \bigl(
 U,d,\mathcal I,\{s_i,\sigma_i,\mathcal D_i,\pi_i\}_{i\in\mathcal I}
 \bigr),
```
where:

1.  $`U`$ is the state-and-control region on which all declared quantities can be compared.

2.  $`d`$ is a specified metric or extended metric on $`U`$. In an operator problem this may be an operator norm, graph norm, form metric, or a product metric, but the choice must be stated.

3.  $`\mathcal I`$ is a finite set of required control rows.

4.  $`s_i:\mathcal D_i\to\mathbb R`$ is a continuous signed slack on its declared domain $`\mathcal D_i\subseteq U`$. Positive means that row $`i`$ passes, zero is its boundary, and negative means that it fails.

5.  $`\sigma_i>0`$ is a declared reference scale with the same units as $`s_i`$. It is fixed independently of the point being certified, or its allowed state dependence and bounds are stated explicitly.

6.  $`\pi_i`$ is the provenance record for $`s_i`$, its tolerance, norm, source theorem or assumption, uncertainty, and evaluation procedure.

The common record domain is $`\mathcal D=\bigcap_{i\in\mathcal I}\mathcal D_i`$, and the declared admissible set is
``` math
\mathcal A
 =
 \{x\in\mathcal D:s_i(x)>0\text{ for every }i\in\mathcal I\}.
```

</div>

The strict inequality is useful when capacity is intended to measure interior reserve. A particular theorem may use nonnegative inequalities and include part of the boundary; that convention must be recorded rather than hidden in notation.

## Typical rows

The complete Foundation ledger is longer than the following table, and it remains the canonical source. The table only shows how representative conditions become signed slacks.

<div class="center">

<div class="tabularx">

@L0.20Y Y@ Row & Supplied control statement & Example signed slack
Internal gap & A selected spectral cluster has separation $`\gamma(x)>\gamma_{\min}`$. & $`s_{\rm gap}=\gamma-\gamma_{\min}`$.
Resolvent or projector & A declared contour or complementary resolvent obeys $`K(x)<K_{\max}`$. & $`s_{\rm res}=K_{\max}-K`$.
Complementary stability & The complementary semigroup has residual decay $`\omega_Q(x)>0`$. & $`s_Q=\omega_Q`$.
Leakage or descent & A leakage or commutator defect is below its certified tolerance: $`\ell(x)<\ell_{\max}`$. & $`s_{\rm leak}=\ell_{\max}-\ell`$.
Contraction & A map has a proved contraction factor $`q(x)<1`$ on a declared invariant set and norm. & $`s_{\rm ctr}=1-q`$.
Truncation & The complete remainder bound obeys $`E(x)<E_{\max}`$. & $`s_{\rm tr}=E_{\max}-E`$.
Hyperbolicity or positivity & A selected principal-symbol, Hessian, or Gram eigenvalue satisfies $`h(x)>h_{\min}`$. & $`s_{\rm hyp}=h-h_{\min}`$.
Numerical certificate & An interval inclusion, majorant, or residual test has a strict certified reserve $`\rho(x)>0`$. & $`s_{\rm cert}=\rho`$.

</div>

</div>

The rows are not interchangeable. A spectral gap does not prove invariance; a contraction factor says nothing before its norm and invariant set are fixed; and a small numerical residual is not an existence theorem without the corresponding certification inequality.

## Why normalization is indispensable

Suppose a gap is measured in inverse-length squared, an operator defect in operator norm, and a truncation error in a dimensionless observable norm. Taking their raw minimum is meaningless. The positive scales $`\sigma_i`$ turn each slack into a dimensionless reserve
``` math
r_i(x)=\frac{s_i(x)}{\sigma_i}.
```
The vector
``` math
r(x)=\bigl(r_i(x)\bigr)_{i\in\mathcal I}
```
is the primary capacity object. It preserves which condition is limiting and how each entry was normalized.

Scales can come from a theorem tolerance, a certified reference gap, an instrument resolution, or a predeclared design budget. Choosing a scale after seeing which candidate one wishes to accept is target-dependent selection, not an invariant definition.

# Bottleneck coherence capacity

<div id="def:capacity" class="definition">

**Definition 2** (Signed bottleneck and coherence capacity). For a record as in Definition <a href="#def:record" data-reference-type="ref" data-reference="def:record">1</a>, define
``` math
D_{\mathcal R}(x)=\min_{i\in\mathcal I}r_i(x),
 \qquad
 C_{\mathcal R}(x)=\min\{1,\max\{0,D_{\mathcal R}(x)\}\}.
```
The active set is
``` math
I_{\rm act}(x)
 =
 \{i\in\mathcal I:r_i(x)=D_{\mathcal R}(x)\}.
```

</div>

The signed quantity $`D_{\mathcal R}`$ distinguishes interior, boundary, and failure. The clipped quantity $`C_{\mathcal R}\in[0,1]`$ is convenient for comparison and visualization. Clipping at one says only that reserves larger than one declared scale are not distinguished by this summary. The full vector should be retained in every archival calculation.

<div id="prop:logical" class="proposition">

**Proposition 3** (Exact logical content of the bottleneck). *For every $`x\in\mathcal D`$:
``` math
x\in\mathcal A
 \quad\Longleftrightarrow\quad
 D_{\mathcal R}(x)>0
 \quad\Longleftrightarrow\quad
 C_{\mathcal R}(x)>0.
```
Moreover, $`D_{\mathcal R}(x)=0`$ means that at least one declared row is on its boundary and none is negative. It does not imply that every row vanishes.*

</div>

<div class="proof">

*Proof.* The minimum of finitely many real numbers is positive exactly when every number is positive. Since every $`\sigma_i`$ is positive, $`r_i`$ and $`s_i`$ have the same sign. The statement about the boundary follows from the definition of a finite minimum. ◻

</div>

This small proposition corrects an important overstatement in Version 3. The point of a bottleneck is precisely that one control may be exhausted while the others retain large reserves.

<div id="prop:perturb" class="proposition">

**Proposition 4** (Perturbation certificate). *Let $`x\in\mathcal A`$, and suppose $`y\in\mathcal D`$ satisfies
``` math
\|r(y)-r(x)\|_{\infty}<D_{\mathcal R}(x).
```
Then $`y\in\mathcal A`$. More concretely, if every $`r_i`$ is Lipschitz on a neighborhood of $`x`$ with constant $`L_i`$, and $`L=\max_iL_i`$, then
``` math
d(x,y)<\frac{D_{\mathcal R}(x)}{L}
 \quad\Longrightarrow\quad
 y\in\mathcal A
```
whenever $`L>0`$ and the connecting neighborhood remains in $`\mathcal D`$.*

</div>

<div class="proof">

*Proof.* For each $`i`$,
``` math
r_i(y)
 >
 r_i(x)-D_{\mathcal R}(x)
 \ge 0.
```
The strict norm inequality makes every final inequality strict. Under the Lipschitz assumption, $`\|r(y)-r(x)\|_\infty\le Ld(x,y)`$, so the second statement follows. ◻

</div>

The proposition is the operational meaning of capacity: it is a certified reserve in the chosen normalized coordinates. It is not a statement about energy or available work.

<div class="definition">

**Definition 5** (Regional capacity). For $`K\subseteq\mathcal D`$, define
``` math
C_{\mathcal R}(K)=\inf_{x\in K}C_{\mathcal R}(x),
 \qquad
 D_{\mathcal R}(K)=\inf_{x\in K}D_{\mathcal R}(x).
```

</div>

<div id="prop:uniform" class="proposition">

**Proposition 6** (Uniform reserve). *If $`D_{\mathcal R}(K)>0`$, then every declared margin has a uniform positive normalized reserve on $`K`$. Conversely, if each row has a uniform lower bound $`r_i(x)\ge\varepsilon_i>0`$ on $`K`$, then
``` math
D_{\mathcal R}(K)\ge\min_i\varepsilon_i>0.
```*

</div>

<div class="proof">

*Proof.* The first implication follows from $`r_i(x)\ge D_{\mathcal R}(x)\ge D_{\mathcal R}(K)`$. The converse follows by taking the minimum first over $`i`$ and then over $`x\in K`$. ◻

</div>

Regional capacity is the correct quantity when a proof requires a *uniform* gap, resolvent, or contraction estimate. A positive value at one state does not certify an entire trajectory, slab, or parameter family.

# Metric clearance and distance to failure

The bottleneck construction uses chosen constraint coordinates. A coordinate-free-looking alternative is distance to the complement, but it still depends on a metric.

<div id="def:clearance" class="definition">

**Definition 7** (Metric clearance). Assume $`\mathcal A`$ is open in the metric space $`(\mathcal D,d)`$, and choose a positive reference length $`L_d`$ in the units of $`d`$. For $`x\in\mathcal D`$, define
``` math
\delta_d(x)=\operatorname{dist}_d(x,\mathcal D\setminus\mathcal A),
 \qquad
 C_d(x)=\min\left\{1,\frac{\delta_d(x)}{L_d}\right\}.
```

</div>

If the complement is empty, one may set $`\delta_d=+\infty`$, but that degenerate case contains no admissibility boundary and should be stated separately.

<div id="prop:distance" class="proposition">

**Proposition 8** (Basic metric properties). *The clearance $`\delta_d`$ is $`1`$-Lipschitz:
``` math
|\delta_d(x)-\delta_d(y)|\le d(x,y).
```
It is positive on $`\mathcal A`$ and zero on $`\overline{\mathcal D\setminus\mathcal A}`$. If two metrics satisfy
``` math
a\,d(x,y)\le d'(x,y)\le b\,d(x,y)
```
on the region of interest for constants $`0<a\le b<\infty`$, then their clearances satisfy
``` math
a\,\delta_d(x)\le\delta_{d'}(x)\le b\,\delta_d(x).
```*

</div>

<div class="proof">

*Proof.* For every $`z\in\mathcal D\setminus\mathcal A`$, the triangle inequality gives $`d(x,z)\le d(x,y)+d(y,z)`$. Taking infima over $`z`$ yields $`\delta_d(x)\le d(x,y)+\delta_d(y)`$; exchanging $`x`$ and $`y`$ proves the Lipschitz bound. Openness gives positive distance locally only when the point has a nonzero metric ball contained in $`\mathcal A`$, which is exactly the definition. The comparison statement follows by taking infima in the two metric inequalities. ◻

</div>

<div class="remark">

*Remark 9* (Infinite-dimensional caution). An open set guarantees that each interior point contains some metric ball, so its pointwise clearance is positive. It does not guarantee a positive uniform clearance on a noncompact set. Nor are an operator norm, graph norm, strong topology, and weak topology interchangeable. The topology and metric used by the source theorem must be the ones used by the capacity record.

</div>

## When do slack and distance capacities agree?

The two definitions have the same positive set by construction, but they need not have comparable numerical values. A flat margin such as $`s(x)=\delta_d(x)^3`$ and a steep margin such as $`s(x)=\sqrt{\delta_d(x)}`$ share a zero set while encoding very different rates.

<div id="ass:errorbound" class="assumption">

**Assumption 10** (Local error bound). On a region $`V\subseteq\mathcal A`$, suppose there are constants $`0<\alpha\le\beta<\infty`$ such that
``` math
\alpha\,\frac{\delta_d(x)}{L_d}
 \le
 D_{\mathcal R}(x)
 \le
 \beta\,\frac{\delta_d(x)}{L_d}
 \qquad (x\in V).
```

</div>

<div id="prop:comparison" class="proposition">

**Proposition 11** (Slack–distance comparability). *Under Assumption <a href="#ass:errorbound" data-reference-type="ref" data-reference="ass:errorbound">10</a>, the clipped capacities obey
``` math
\alpha C_d(x)
 \le C_{\mathcal R}(x)
 \le \beta C_d(x)
```
on every subregion where both $`\delta_d(x)/L_d\le1`$ and $`D_{\mathcal R}(x)\le1`$. More generally, the same inequalities hold locally after keeping the unclipped signed bottleneck.*

</div>

<div class="proof">

*Proof.* On the stated subregion no clipping occurs, so the claim is exactly Assumption <a href="#ass:errorbound" data-reference-type="ref" data-reference="ass:errorbound">10</a>. The unclipped statement is the same comparison without the subregion restriction. ◻

</div>

The hypothesis is substantial. For affine inequalities, classical error bounds give precisely this kind of comparison under suitable feasibility conditions . For nonlinear operator constraints one needs a model-specific regularity, transversality, or metric-subregularity estimate. Sharing a boundary is not enough.

# What “invariant” can honestly mean

The word *invariant* is useful only after the allowed transformations are stated.

<div id="def:equiv" class="definition">

**Definition 12** (Capacity-equivalent records). Two records $`\mathcal R`$ and $`\mathcal R'`$ on a region $`V`$ are capacity-equivalent if they define the same admissible set on $`V`$ and there exist constants $`0<a\le b<\infty`$ such that
``` math
aD_{\mathcal R}(x)\le D_{\mathcal R'}(x)\le bD_{\mathcal R}(x)
 \qquad
 \text{for every }x\in V\cap\mathcal A.
```

</div>

This relation preserves positivity, exhaustion, and uniform-reserve statements. It does not assert that the numerical values are identical.

<div id="thm:reparam" class="theorem">

**Theorem 13** (Controlled reparameterization). *Let $`r:V\to(0,\infty)^n`$ be one normalized reserve vector and let $`r'=F\circ r`$ be another. Suppose $`F`$ preserves the positive cone and there are constants $`0<a\le b<\infty`$ such that
``` math
a\min_i u_i
 \le
 \min_jF_j(u)
 \le
 b\min_i u_i
```
for every $`u\in r(V\cap\mathcal A)`$. Then the two bottleneck records are capacity-equivalent on $`V`$.*

</div>

<div class="proof">

*Proof.* Apply the displayed comparison to $`u=r(x)`$. The two minima are exactly the two signed bottleneck capacities on the admissible region. ◻

</div>

Positive diagonal changes of normalization with scales bounded above and below satisfy the theorem. So do uniformly bi-Lipschitz changes of margin coordinates that preserve the positive cone. An arbitrary function $`C'=f(C)`$ need not. For example, $`f(C)=C^3`$ preserves the zero set but has no positive linear lower comparison near zero. It changes boundary rates and makes $`\nabla C'`$ vanish more rapidly.

<div class="remark">

*Remark 14* (The actual invariant). The robust object is the equivalence class
``` math
[\mathcal R]_{\rm cap}
```
of records under controlled comparisons. The positivity domain and exhaustion boundary are qualitative invariants. A numerical scalar is a representative chosen by a metric and normalization convention.

</div>

# Operator-theoretic examples

The definitions become useful when the slacks come from real estimates. The examples below illustrate the bookkeeping; they do not claim that one universal list applies to every MTT model.

## A spectral projector

Let $`A(x)`$ be a self-adjoint operator family with a selected spectral cluster separated from the rest of the spectrum by $`\gamma(x)`$. Let $`P(x)`$ be the corresponding Riesz projector. Perturbation theory relates a nonzero gap and resolvent control to stability of the selected subspace .

A legitimate record could contain
``` math
s_{\rm gap}(x)=\gamma(x)-\gamma_{\min},
```
and, for a declared contour $`\Gamma`$,
``` math
K_\Gamma(x)
 =
 \sup_{z\in\Gamma}\|(z-A(x))^{-1}\|,
 \qquad
 s_{\rm res}(x)=K_{\max}-K_\Gamma(x).
```
The record must state the operator domain, perturbation topology, contour, target cluster, thresholds, and Sobolev or graph norm in which $`P(x)`$ is controlled. The scalar capacity then reports which reserve is smaller. It does not prove the Riesz formula or projector bound; those remain the source theorem.

## A Schur–Feshbach truncation

Let $`\mathcal H=P\mathcal H\oplus Q\mathcal H`$, $`Q=\operatorname{Id}-P`$, and write a closed operator $`T`$ in blocks. At a spectral parameter $`z`$ for which $`QTQ-z`$ is invertible on its declared domain, the complementary correction has the form
``` math
R_F(z)
 =
 PTQ\,(QTQ-z)^{-1}QTP.
```
If the effective construction requires $`\|R_F(z)\|<\eta_{\max}`$, the normalized truncation reserve may be
``` math
r_F(z)
 =
 1-
 \frac{
 \|PTQ\|\,
 \|(QTQ-z)^{-1}\|\,
 \|QTP\|
 }{\eta_{\max}}.
```
This uses the actual three-factor control product. The slogan “mixing squared divided by a gap” is only a special symmetric estimate and must not replace the domain, resolvent, and block norms .

## A contraction argument

Suppose $`F_x:K_x\to K_x`$ is a contraction in a declared norm with factor $`q(x)<1`$. One row may be
``` math
r_{\rm ctr}(x)=1-q(x).
```
Another row must record whether $`F_x`$ actually maps the chosen set into itself, for example through a separately proved invariance reserve. A positive $`r_{\rm ctr}`$ without a complete domain and invariant-set statement is not a fixed-point certificate. Conversely, once those hypotheses are supplied, the Banach fixed-point theorem, not the word “capacity”, proves existence and uniqueness. Fixed Points I owns the corresponding MTT framework .

## A numerical toy record

Consider four already normalized rows at one point:
``` math
r(x)=(0.62,\;0.31,\;0.08,\;0.44).
```
Then
``` math
D_{\mathcal R}(x)=C_{\mathcal R}(x)=0.08,
\qquad
 I_{\rm act}(x)=\{3\}.
```
The record is admissible, but its third certificate is fragile. Any perturbation changing every normalized row by less than $`0.08`$ preserves admissibility by Proposition <a href="#prop:perturb" data-reference-type="ref" data-reference="prop:perturb">4</a>. Nothing in these four numbers says whether row 3 is a spectral gap, a truncation error, or a detector threshold. That meaning lives in the provenance $`\pi_3`$.

# Capacity along an evolution

Capacity can be evaluated along a trajectory without becoming the generator of that trajectory. Let $`x:[0,T]\to\mathcal D`$ be supplied by an upper or effective evolution, and suppose the normalized rows $`r_i(x(t))`$ are absolutely continuous.

<div id="prop:path" class="proposition">

**Proposition 15** (First-exit reserve bound). *If
``` math
\left|\frac{d}{dt}r_i(x(t))\right|\le v_i(t)
```
for almost every $`t`$, and $`v(t)=\max_i v_i(t)`$, then
``` math
D_{\mathcal R}(x(t))
 \ge
 D_{\mathcal R}(x(0))-\int_0^t v(s)\,ds.
```
Consequently, no declared margin can be exhausted before the integral of the worst normalized rate reaches the initial bottleneck reserve.*

</div>

<div class="proof">

*Proof.* For every $`i`$,
``` math
r_i(x(t))
 \ge
 r_i(x(0))-\int_0^t v_i(s)\,ds
 \ge
 D_{\mathcal R}(x(0))-\int_0^t v(s)\,ds.
```
Taking the minimum over $`i`$ proves the result. ◻

</div>

This is a useful monitoring bound. It is not a conservation law. A law such as
``` math
\partial_t C+\nabla\cdot J_C=S_C
```
requires a separately defined field, flux, source, regularity class, and constitutive or variational principle. Likewise, a barrier $`-\log(\varepsilon+C)`$ explicitly introduces a penalty into an algorithm; its negative gradient is a chosen force in that model, not a consequence of the capacity definition.

## What happens at zero?

At a first time $`t_\ast`$ with $`D_{\mathcal R}(x(t_\ast))=0`$, the record says only which certificate has reached its declared boundary. The corrected Foundation distinguishes three possibilities:

1.  stop the reduced description;

2.  continue the upper dynamics and derive another reduced chart; or

3.  add a reset map or reset kernel and thereby define a hybrid system.

The boundary does not select among them. If a reset has several outputs, the boundary also does not provide their probabilities.

# Why the former physical deductions do not follow

The corrected definition is intentionally less dramatic than Version 3. That is a gain in rigor: downstream physical claims can now be tested against the exact additional data they require.

## A projection may have a section

Let $`P:\mathcal H\to P\mathcal H`$ be an orthogonal projection. It is noninjective when $`\ker P\ne\{0\}`$, yet the inclusion
``` math
\iota:P\mathcal H\hookrightarrow\mathcal H
```
is a bounded measurable map satisfying
``` math
P\circ\iota=\operatorname{Id}_{P\mathcal H}.
```
Thus noninjectivity, gap closure, or identification of upper states does not by itself prove that no right inverse or measurable section exists.

A section selects one representative of each lower state. It does not recover the actual original upper state. The impossible object for a noninjective map is a *left* inverse recovering every upper state:
``` math
L\circ P=\operatorname{Id}_{\mathcal H}.
```
The physically relevant questions are therefore whether a selected decoder exists, whether it commutes with the dynamics on its domain, and whether it recovers the information one claims. Capacity exhaustion alone decides none of these.

## Irreversibility and time

The reduced chart can lose a certificate while the upper evolution remains invertible. It can also cross into another valid chart and later return. Irreversibility requires a noninvertible lower semigroup, a coarse-graining theorem, a reset rule, a record-stability mechanism, or a thermodynamic limit. A sequence of zero crossings is not, by itself, an arrow of time.

## Gravity

One may postulate an effective action containing
``` math
\int\sqrt{-g}\,f(C)R,
```
but this is extra dynamics. Its variation generally contains derivatives of $`f(C)`$ and resembles a scalar-tensor coupling unless $`f(C)`$ is fixed and constant. The capacity definition neither selects the action nor derives the normalization $`1/(16\pi G)`$. Identifying $`G^{-1}`$ with an arbitrary representative of a capacity class is especially ill-defined because $`C\mapsto C^3`$ preserves the zero set while changing the proposed coupling.

## Horizons, entropy, and measurement

A horizon requires a Lorentzian geometry, causal structure, and field equations. An area law requires a state-counting, algebraic, or entanglement argument and an independently derived coefficient. A measurement requires a system–apparatus interaction, pointer records, and an outcome instrument. Capacity can enter such models as one certified control row, but it does not supply their missing structures.

## Probability and undecidability

The location of a boundary does not define a probability measure over possible continuations. Nor does it imply undecidability. An undecidability theorem needs an explicit robust embedding of a universal machine and a proof that its storage and operations remain admissible for the required run. Computational cost, unpredictability, first-exit sensitivity, and formal undecidability are different claims.

# Relation to the MTT paper sequence

This revision gives the capacity sequence a coherent division of labor.

<div class="center">

<div class="tabularx">

@L0.28Y@ Document or topic & Correct role after this revision
MTT Foundation & Canonical owner of the complete admissibility ledger, independent hypotheses, and stop/continue/reset alternatives .
Fixed Points I–VI & Canonical owners of their conditional projector, existence, stability, covariance, and synthesis results. Capacity may summarize proved reserves but does not reproach or re-prove those theorems .
This paper & Owner of the normalized reserve record, bottleneck compression, metric clearance, comparison conditions, and capacity-equivalence language.
Controlled truncation & Must emit the actual block-domain, resolvent, mixing, remainder, and error rows before capacity can summarize them.
Capacity dynamics & May study a declared constitutive model, but conservation and transport do not follow from the margin definition.
Particles and forces & May use capacity in an action or Hamiltonian if that coupling is sourced; $`\nabla C`$ is not automatically a force.
Horizons and cosmology & Require covariant dynamics, causal and state data, normalization, and comparison with observations. Capacity language alone is interpretive.
Capacity-gated algorithms & Are hybrid constrained systems. Their flow domains, guards, reset maps or kernels, and invariants must be specified explicitly.

</div>

</div>

This order prevents circular reasoning. A downstream paper may not choose a scalar capacity to obtain a desired force, use that force to define the dynamics, and then claim the resulting trajectory proves the original capacity law.

# Source discipline and falsifiability

A capacity value is only as strong as its rows. Every published value should include:

1.  the exact state, parameter point, and domain;

2.  the finite list of required margins;

3.  the norm, topology, tolerance, and units for each margin;

4.  the normalization scale and why it was fixed;

5.  the theorem, assumption, numerical certificate, or measured input sourcing each row;

6.  interval or uncertainty bounds;

7.  the active constraint set;

8.  whether the claim is pointwise, local, regional, or trajectory-wide;

9.  a hash-addressed calculation when numerical values are used; and

10. a continuation statement that is separate from the boundary test.

The thresholds must be fixed before they are used to exclude data or select a branch. Otherwise the capacity is an after-the-fact score. A held-out failure of a claimed positive reserve falsifies that certificate or one of its source assumptions. It does not by itself falsify every MTT encoding.

## A minimal archival packet

For machine-readable work, one capacity packet should contain at least the fields

<div class="center">

<div class="tabularx">

0.94@L0.29Y@ `record_id`, `source_commit` & Identity and immutable source provenance.
`domain`, `metric` & The common evaluation region and quantitative topology.
`rows`, `scales`, `intervals` & Signed slacks, normalization choices, and certified uncertainty.
`active_set`, `capacity`, `scope` & The limiting rows, scalar compression, and claim domain.
`continuation_policy` & Stop, upper continuation, or a separately sourced reset rule.

</div>

</div>

The scalar should never be stored without the row vector. This makes a future change of normalization auditable and prevents one paper’s diagnostic from silently becoming another paper’s physical parameter.

# Limitations and open work

The current construction closes a definitional problem, not a physical source theorem.

1.  There is no universal metric on the space of all MTT realizations.

2.  Different operator problems naturally use different norms and domains.

3.  Slack–distance equivalence needs a model-specific error bound.

4.  A finite margin list is only complete relative to a declared theorem or calculation contract.

5.  The capacity class does not select a preferred scalar representative.

6.  No dynamics, probability, entropy, force, or geometry follows from the scalar without additional structure.

These limits are productive. They turn the word “capacity” into a checklist of explicit obligations. A future model can strengthen the construction by selecting its metric and scales from the same upper source as its operators, and then proving that the resulting record descends naturally through the relevant projections.

# Conclusion

Coherence capacity is best understood as the normalized clearance of a declared effective construction from its nearest certified failure. The full reserve vector is primary. Its minimum is a useful bottleneck summary, and metric distance is a useful geometric alternative. Both are quantitative only after their scales, metric, norms, and provenance are fixed.

This corrected formulation preserves the original intuition while removing claims the scalar could not support. Capacity exhaustion identifies a first failed certificate; it does not decide the fate of the upper state or manufacture a new physical law. The reward is a definition that can be used consistently across spectral projectors, fixed-point arguments, controlled truncations, numerical certificates, and future MTT realizations.

# Reproducibility statement

This paper proves structural statements from the displayed definitions and inequalities. It reports no fitted parameter, numerical prediction, or calculation-derived physical value. The source TeX, bibliography, revision audit, and generated PDF are versioned in the MTT papers repository. Papers that publish numerical capacity values must additionally provide the machine-readable packet described in Section <a href="#sec:source" data-reference-type="ref" data-reference="sec:source">10</a>.
