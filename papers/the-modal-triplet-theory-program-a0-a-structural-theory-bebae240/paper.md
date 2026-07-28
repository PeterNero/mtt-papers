---
abstract: |
  We give a typed, conditional formulation of Modal Triplet Theory (MTT) as a theory of reduced description. A representative section, an exact upper decoder, autonomous reduced evolution, and merger of effective states solve four different mathematical problems; none follows merely from noninjectivity of a projection. We prove the factor-through criterion for autonomous descent, a finite-diameter obstruction for a genuinely contractive reduced self-map, exact basin-local fixed-point results, and controlled approximate-orbit estimates. Admissibility boundaries are defined by explicit margins and section or projector conditioning rather than by assuming the desired obstruction. The encoding atlas and its relations are consequently local and conditional. Probability, irreversibility, physical time, and any concrete physical realization require their own measure, evolution, and source hypotheses.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 07c65fe7125f9565297ac63d3fb97298e351f01b394fcd18a81a5cd9556eea3a
paper_id: the-modal-triplet-theory-program-a0-a-structural-theory-bebae240
release_state: zenodo_released
released_version: v1.0
title: |
  The Modal Triplet Theory Program A0:  
  A Structural Theory of Reduced Description
zenodo_doi: 10.5281/zenodo.18354784
zenodo_record_id: 18354784
zenodo_url: "https://zenodo.org/records/18354784"
---

# Revision note for version 2

#### Supersedes.

Version 1 of Program A0.

#### Reason.

The former text conflated representative selection with microscopic recovery, treated an additive-error estimate as a Banach contraction, and promoted several conditional atlas statements to universal theorems.

#### Resolution.

Version 2 installs the projection–descent and recovery classification, exact basin-local FCC, the finite-diameter self-map obstruction, explicit margin barriers, and a typed distinction between physical evolution and auxiliary stabilization. It also corrects the direction of encoding factorization and scopes probability, records, selection, and global relations.

#### Retained content.

Finite admissibility, local encoding charts, coherence margins, and the total chart-of-charts remain the structural core.

#### Open boundary.

No physical measure, Born rule, arrow of time, reset law, spacetime dynamics, or concrete MTT realization is derived in A0.

# Part I: Abstract Framework

# Typed Data and Admissibility

This section fixes notation and logical order. All definitions are mathematical; physical interpretation is an additional assignment.

## Upper evolution and reductions

<div class="definition">

**Definition 1** (Typed projection system). A typed projection system at parameter $`t`$ consists of
``` math
(X_0,X_t,\Phi_t;\;Y_0,Y_t,P_0,P_t)
```
where:

- $`X_0`$ and $`X_t`$ are standard Borel spaces, equipped with metrics when metric estimates are used;

- $`\Phi_t:X_0\to X_t`$ is a measurable upper evolution map;

- $`P_0:X_0\to Y_0`$ and $`P_t:X_t\to Y_t`$ are measurable reductions, surjective onto their declared effective images.

The cross-level output map is
``` math
Q_t:=P_t\circ\Phi_t:X_0\longrightarrow Y_t.
```

</div>

<div class="remark">

*Remark 2* (Evolution semantics). No invertibility is needed for the typing results below. In an application, $`\Phi_t`$ must be declared either as physical evolution, with its own well-posedness, causal or hyperbolic hypotheses, or as an auxiliary stabilization map or semigroup. An auxiliary parameter is not physical time, and contraction of an auxiliary semigroup is not by itself physical irreversibility.

</div>

## Tolerance

<div class="definition">

**Definition 3** (Tolerance). Fix $`\varepsilon>0`$. Two points $`y_1,y_2`$ in a declared reduced metric space are $`\varepsilon`$-indistinguishable if
``` math
d_Y(y_1,y_2)\le \varepsilon,
```
where $`d_Y`$ is a chosen pseudometric.

</div>

## Representative selection, recovery, and descent

<div class="definition">

**Definition 4** (Representative section). A representative section for $`Q_t`$ is a map $`S_t:Y_t\to X_0`$ satisfying
``` math
Q_t\circ S_t=\operatorname{id}_{Y_t}.
```
It chooses one compatible upper representative. It does not recover the upper state that actually produced the reduced datum.

</div>

<div class="definition">

**Definition 5** (Exact upper decoder). An exact upper decoder is a map $`D_t:Q_t(X_0)\to X_0`$ satisfying
``` math
D_t\circ Q_t=\operatorname{id}_{X_0}.
```
It recovers the actual upper input.

</div>

<div class="definition">

**Definition 6** (Autonomous reduced evolution). An autonomous reduced evolution is a map $`F_t:Y_0\to Y_t`$ satisfying
``` math
F_t\circ P_0=P_t\circ\Phi_t.
```

</div>

<div class="definition">

**Definition 7** (Effective merger). If $`F_t`$ exists, an effective merger occurs when distinct $`y,y'\in Y_0`$ satisfy $`F_t(y)=F_t(y')`$.

</div>

<div id="thm:descent-recovery" class="theorem">

**Theorem 8** (Projection–descent and recovery). *For the typed data above:*

1.  *a set-theoretic representative section exists when $`Q_t`$ is surjective and the relevant choice principle is available; measurable, continuous, local, or Lipschitz sections require corresponding selection theorems;*

2.  *an exact decoder exists if and only if $`Q_t`$ is injective, in which case it is the inverse of $`Q_t`$ on its image;*

3.  *an autonomous reduced evolution exists if and only if
    ``` math
    \begin{equation}
    P_0(x)=P_0(x')
    \quad\Longrightarrow\quad
    P_t(\Phi_t x)=P_t(\Phi_t x')
    \label{eq:descent}
    \end{equation}
    ```
    for all $`x,x'\in X_0`$, and it is then unique;*

4.  *if <a href="#eq:descent" data-reference-type="eqref" data-reference="eq:descent">[eq:descent]</a> holds and two distinct initial effective states have the same final image, then $`F_t`$ is noninjective and the prior effective state cannot be decoded uniquely from the final one.*

</div>

<div class="proof">

*Proof.* The first item is the definition of a section of a surjection. If $`D_tQ_t=\operatorname{id}`$ and $`Q_t(x)=Q_t(x')`$, applying $`D_t`$ gives $`x=x'`$. Conversely, an injective map has an inverse on its image. For the third item, necessity follows by applying $`F_t`$ to equal $`P_0`$-images. Under <a href="#eq:descent" data-reference-type="eqref" data-reference="eq:descent">[eq:descent]</a>, define
``` math
F_t(P_0x):=P_t(\Phi_tx).
```
The implication makes this independent of the representative, and surjectivity of $`P_0`$ onto $`Y_0`$ gives existence and uniqueness. The final item is immediate from the definition of injectivity. ◻

</div>

<div class="corollary">

**Corollary 9** (Noninjectivity is not a right-section obstruction). *Noninjectivity of $`Q_t`$ rules out exact microscopic recovery, not representative selection. Surjectivity, together with the required regularity category, is the gate for a right section.*

</div>

## Admissible domains and explicit margins

<div class="definition">

**Definition 10** (Declared margins). Let $`m_1,\ldots,m_r`$ be continuous real-valued margins on a metric upper domain. They may encode such requirements as operator-domain control, spectral separation, bounded leakage, truncation error, section conditioning, or physical hyperbolicity. For $`\delta\ge0`$, set
``` math
A^\delta:=\{x:m_j(x)\ge\delta\text{ for every }j\}.
```

</div>

<div class="definition">

**Definition 11** (Admissible domain). A subset $`A\subset X_0`$ is admissible for a declared protocol family $`\Pi_A`$ if:

1.  $`A\subset A^\delta`$ for some $`\delta>0`$ and $`P_0|_A`$ is measurable;

2.  for each $`\pi\in\Pi_A`$ there is a representative section $`S_{A,\pi}:P_0(A)\to A`$ of $`P_0|_A`$ in the declared regularity category;

3.  a declared upper step $`R_{A,\pi}:A\to X_0`$ induces a well-typed section-dependent self-map
    ``` math
    T_{A,\pi}:=P_0\circ R_{A,\pi}\circ S_{A,\pi}
       :P_0(A)\longrightarrow P_0(A);
    ```

4.  the fixed-point, encoding, or approximation contract invoked on $`A`$ is stated explicitly and verified on its own invariant domain.

</div>

<div class="axiom">

**Axiom 1** (Finite admissibility). *For the declared theory class, there is no single domain $`A=X_0`$ and protocol family for which all required positive-margin, regularity, and closure contracts hold. Equivalently, no one globally valid admissible encoding exists at this adopted axiom tier.*

</div>

<div class="remark">

*Remark 12*. Finite admissibility excludes a single globally valid *admissible encoding* by definition. It does not, by itself, exclude a global relation, a set-theoretic section, or even an autonomous reduced map.

</div>

## Basin-local Fundamental Contractivity Condition

<div id="def:fcc" class="definition">

**Definition 13** (Exact basin-local FCC). Fix $`A`$, $`\pi`$, and $`T:=T_{A,\pi}`$. A basin contract is a nonempty complete metric subspace $`D_\alpha\subset P_0(A)`$ such that
``` math
T(D_\alpha)\subseteq D_\alpha,
\qquad
d_Y(Tu,Tv)\le q_\alpha d_Y(u,v)
```
for all $`u,v\in D_\alpha`$, where $`0\le q_\alpha<1`$. FCC means this exact, basin-local contract, not one contraction on a union of outcome basins.

</div>

<div id="thm:basin-fixed-point" class="theorem">

**Theorem 14** (Basin-local fixed point). *Every basin $`D_\alpha`$ satisfying Definition <a href="#def:fcc" data-reference-type="ref" data-reference="def:fcc">13</a> contains a unique fixed point $`y_\alpha^\ast`$, and
``` math
d_Y(T^ny,y_\alpha^\ast)\le
q_\alpha^n d_Y(y,y_\alpha^\ast)
\quad(y\in D_\alpha).
```*

</div>

<div class="proof">

*Proof.* This is Banach’s fixed-point theorem on the complete invariant domain $`D_\alpha`$. ◻

</div>

<div class="definition">

**Definition 15** (Approximate orbit contract). On an invariant domain $`D`$, an approximate orbit contract is
``` math
d_Y(Tu,Tv)\le\kappa d_Y(u,v)+c\varepsilon,
\qquad 0\le\kappa<1.
```

</div>

<div id="prop:approximate" class="proposition">

**Proposition 16** (Approximate pairwise estimate). *If two forward orbits remain in $`D`$, then
``` math
d_Y(T^nu,T^nv)
\le \kappa^n d_Y(u,v)
 \frac{1-\kappa^n}{1-\kappa}\,c\varepsilon.
```
This estimate alone neither makes $`T`$ a Banach contraction nor proves that $`T`$ has a fixed point.*

</div>

<div class="proof">

*Proof.* Iterate the affine recurrence for the distance. ◻

</div>

## Fixed points and basins

<div class="definition">

**Definition 17** (Basin). A basin is an invariant domain $`D_\alpha`$ equipped with either the exact FCC contract of Definition <a href="#def:fcc" data-reference-type="ref" data-reference="def:fcc">13</a>, or a separately stated stability theorem. Distinct outcome basins are not combined into one Banach domain.

</div>

## Coherence capacity

<div class="definition">

**Definition 18** (Coherence capacity). For declared margins $`m_j`$, define the diagnostic
``` math
C(x):=\min_j m_j(x).
```
Thus $`C(x)>0`$ records positive slack in every declared condition and $`C(x)=0`$ records saturation of at least one condition.

</div>

## Admissibility barriers

<div id="def:admissibility-barrier" class="definition">

**Definition 19** (Margin boundary and barrier). For a declared contract, let
``` math
X_{\rm adm}:=\{x:C(x)>0\},
\qquad
\partial X_{\rm adm}:=\overline{X_{\rm adm}}
   \setminus\operatorname{int}(X_{\rm adm}).
```
A pathwise admissibility barrier is a subset $`\mathcal B\subseteq\partial X_{\rm adm}`$ across which a specified positive margin cannot be continued. The failed margin must be named.

</div>

<div class="definition">

**Definition 20** (Section-conditioning diagnostic). For Lipschitz representative sections of $`Q_t`$, define
``` math
\kappa_{\rm sec}(t):=
\inf\{\operatorname{Lip}(S_t):Q_tS_t=\operatorname{id}_{Y_t}\},
```
with $`\kappa_{\rm sec}(t)=+\infty`$ if no Lipschitz section exists.

</div>

<div class="remark">

*Remark 21*. Blow-up of $`\kappa_{\rm sec}`$, loss of surjectivity, or failure of bounded Riesz-projector continuation can supply explicit barrier margins in a realization. None is assumed merely to manufacture an obstruction, and none alone is a physical singularity or state-selection law.

</div>

## Invariant measure (conditional)

<div class="assumption">

**Assumption 22** (Measure data, only when invoked). For probabilistic statements, supply either a preparation probability measure $`\mu`$ on the relevant upper domain or a stationary probability measure $`\nu`$ for a declared self-map. Invariance means $`R_\#\mu=\mu`$ for $`R:A\to A`$, or $`T_\#\nu=\nu`$ for $`T:Y_A\to Y_A`$; it is not meaningful without a same-space map.

</div>

## Encodings

<div class="definition">

**Definition 23** (Encoding). An encoding is a tuple
``` math
\mathcal E=(A,\;Z,\;E,\;F,\;\varepsilon)
```
where $`A`$ is admissible, $`Z`$ is a normed space, $`E:P_0(A)\to Z`$, and
``` math
E(T_{A,\pi}(y)) = F(E(y)) + \delta(y),
\quad \|\delta(y)\|\le c\,\varepsilon.
```

</div>

<div class="remark">

*Remark 24*. Coherence capacity $`C(x)`$ is not an observable, not a conserved quantity, and not a dynamical degree of freedom. It is a diagnostic margin (a stability/condition number) organizing when admissible encodings exist and when they fail.

</div>

## Interpretation postulate

<div class="postulate">

**Postulate 1**. *When an admissible encoding exists, its reduced structure may be interpreted as a physical description.*

</div>

<div class="remark">

*Remark 25*. Local sections $`S_{A,\pi}`$ may exist on admissible domains. Whether they extend is a separate selection and conditioning problem. Thus local representability does not imply stable global representability, but neither does it logically forbid a set-theoretic global section.

</div>

## Failure modes

The corresponding conclusions are unavailable if:

- no complete invariant basin satisfies FCC where a fixed point is claimed;

- no invariant measure exists where probability is claimed;

- no representative section exists in the required regularity category;

- the declared margins, factorization, or robustness estimates fail.

# Core Structural Results

Fix an admissible domain $`A`$, protocol $`\pi`$, and the well-typed self-map $`T:=T_{A,\pi}`$.

## Basin-local stability

<div class="theorem">

**Theorem 26** (Universality within one exact basin). *If $`D_\alpha`$ satisfies exact basin-local FCC, then every two orbits in $`D_\alpha`$ converge to the same unique fixed point:
``` math
\lim_{n\to\infty}d_Y(T^ny,T^ny')=0
\qquad(y,y'\in D_\alpha).
```*

</div>

<div class="proof">

*Proof.* Apply Theorem <a href="#thm:basin-fixed-point" data-reference-type="ref" data-reference="thm:basin-fixed-point">14</a> to both orbits, or use $`d_Y(T^ny,T^ny')\le q_\alpha^n d_Y(y,y')`$. ◻

</div>

<div class="remark">

*Remark 27* (No cross-basin conclusion). Separate invariant basins may contain separate fixed points. Neither exact FCC nor Proposition <a href="#prop:approximate" data-reference-type="ref" data-reference="prop:approximate">16</a> may be applied to their union unless that union independently satisfies the required complete invariant contract.

</div>

## Admissible prediction depth

<div class="definition">

**Definition 28** (Admissible prediction depth). Fix an admissible domain $`A`$ and protocol $`\pi\in\Pi_A`$. For $`x\in A`$, define the admissible prediction depth
``` math
\begin{aligned}
N_{\max}(x;A,\pi,\varepsilon)
:=\sup\big\{n\in\mathbb{N}\ \big|\ &
T_{A,\pi}^k(P_0(x))\in P_0(A)\\
&\text{for every }0\le k\le n\big\}.
\end{aligned}
```

</div>

<div class="remark">

*Remark 29*. $`N_{\max}`$ is an iteration-count diagnostic. Its relation to physical time or to the size of a margin must be proved in a realization.

</div>

## Computational limits (optional)

<div class="remark">

*Remark 30*. Finite, instance-dependent prediction depth does not imply undecidability. An undecidability result requires a specified input language and a reduction from a known undecidable problem to a declared reachability or admissibility question. A0 supplies no such reduction.

</div>

## Forgetting of incoherent distinctions

<div class="corollary">

**Corollary 31** (Basin-local metric forgetting). *For $`y,y'`$ in one exact FCC basin,
``` math
d_Y(T^ny,T^ny')\longrightarrow0.
```
Under only the approximate orbit contract,
``` math
\limsup_{n\to\infty}d_Y(T^ny,T^ny')
\le \frac{c\varepsilon}{1-\kappa},
```
provided both orbits remain in the same invariant domain. This is a metric statement; information or entropy claims require additional structures.*

</div>

## A valid reduced-self-map obstruction

<div id="thm:diameter-obstruction" class="theorem">

**Theorem 32** (Finite-diameter contraction obstruction). *Let $`(Y_A,d)`$ have finite positive diameter $`D`$, and let $`G:Y_A\to Y_A`$ satisfy
``` math
d(Gy,Gy')\le\kappa d(y,y')+c\varepsilon,
\qquad0\le\kappa<1.
```
Then
``` math
\operatorname{diam}G(Y_A)\le\kappa D+c\varepsilon.
```
If $`(1-\kappa)D>c\varepsilon`$, then $`G`$ is not surjective and has no right section $`S:Y_A\to Y_A`$ with $`G\circ S=\operatorname{id}_{Y_A}`$.*

</div>

<div class="proof">

*Proof.* Take the supremum of the displayed estimate over all pairs. Under the strict inequality, the image diameter is smaller than $`D`$, whereas a surjective image would be all of $`Y_A`$ and would have diameter $`D`$. ◻

</div>

<div class="remark">

*Remark 33*. Theorem <a href="#thm:diameter-obstruction" data-reference-type="ref" data-reference="thm:diameter-obstruction">32</a> concerns a self-map of one reduced space. It cannot be applied to a cross-level map merely because the latter is noninjective.

</div>

## Recovery and irreversibility are separate

<div class="proposition">

**Proposition 34** (Recovery classification). *For the typed maps of Theorem <a href="#thm:descent-recovery" data-reference-type="ref" data-reference="thm:descent-recovery">8</a>:*

1.  *noninjectivity of $`Q_t`$ obstructs exact upper recovery;*

2.  *noninjectivity of an existing $`F_t`$ obstructs recovery of the prior effective state;*

3.  *neither fact alone proves a physical arrow of time.*

*A physical arrow additionally needs oriented dynamics and an asymmetric property such as a noninvertible physical semigroup, a monotone Lyapunov or entropy functional, or a boundary condition.*

</div>

## Measure-dependent reduced probability

<div id="thm:reduced-kernel" class="theorem">

**Theorem 35** (Measure-dependent reduced kernel). *Let $`A`$ and $`P_0(A)`$ be standard Borel spaces, let $`\mu`$ be a probability measure on $`A`$, and let $`\{\mu_y\}`$ be a regular conditional distribution of $`x`$ given $`P_0(x)=y`$. For a measurable upper step $`R:A\to X_0`$, define
``` math
K(y,B):=\mu_y\{x:P_0(Rx)\in B\}.
```
Then $`K`$ is a Markov kernel, up to the usual $`(P_0)_\#\mu`$-null sets. If $`P_0R`$ descends to $`F`$ on $`P_0(A)`$, then $`K(y,\cdot)=\delta_{F(y)}`$ almost everywhere.*

</div>

<div class="proof">

*Proof.* Regular conditional distributions exist on standard Borel spaces. Measurability and countable additivity pass through the measurable preimage. Under autonomous descent, $`P_0(Rx)`$ is constant on each conditional fiber. ◻

</div>

<div class="definition">

**Definition 36** (Basin weights). Let $`\{B_i\}`$ be a measurable partition of $`P_0(A)`$ and let $`\mu`$ be a declared probability measure on $`A`$. Define
``` math
W_i :=
\mu\big(P_0^{-1}(B_i)\cap A\big),
```
or condition and renormalize this expression on a declared selection event.

</div>

<div class="remark">

*Remark 37*. The weights are probabilities because $`\mu`$ was supplied, not because the projection has fibers. Different upper measures can induce different weights and kernels. No Born rule is asserted.

</div>

## Re-encoding criterion on overlaps

<div id="thm:encoding-factor" class="theorem">

**Theorem 38** (Exact encoding factorization). *Let $`E_1:Y\to Z_1`$ and $`E_2:Y\to Z_2`$. A map $`f:E_1(Y)\to Z_2`$ satisfying $`E_2=f\circ E_1`$ exists if and only if
``` math
E_1(y)=E_1(y')\quad\Longrightarrow\quad E_2(y)=E_2(y')
```
for all $`y,y'\in Y`$. When it exists, $`f`$ is unique on $`E_1(Y)`$.*

</div>

<div class="proof">

*Proof.* Necessity is immediate. For sufficiency define $`f(E_1(y)):=E_2(y)`$; the implication makes this well-defined. ◻

</div>

<div class="remark">

*Remark 39*. Overlap of domains alone does not produce a re-encoding. Approximate factorization requires a quantitative fiber-consistency estimate and a controlled extension in the declared regularity class. A0 therefore makes no universal maximal-content claim.

</div>

## Finite admissibility and global scope

<div class="proposition">

**Proposition 40** (No global admissible encoding at the adopted axiom tier). *Under the finite-admissibility axiom, no object satisfying the definition of an admissible encoding has domain $`X_0`$.*

</div>

<div class="proof">

*Proof.* This is the direct content of the axiom and the definition of an encoding. ◻

</div>

<div class="remark">

*Remark 41*. This proposition does not prohibit a global relation or a global reduced map that fails one of the adopted admissibility margins.

</div>

# Part II: Encodings and Boundaries

# Encoding Atlas

This section lists admissible encodings as local charts on neighborhoods of stable basins. Fix $`A`$ and $`\pi`$ and write
``` math
Y_A:=P_0(A),
\qquad T_A:=T_{A,\pi}:Y_A\to Y_A .
```
Each encoding is specified by sufficient inequality contracts involving the contraction constant $`\kappa`$, tolerance $`\varepsilon`$, and coherence capacity $`C`$.

<div class="remark">

*Remark 42* (Contract nature of atlas inequalities). The inequalities in this atlas are *sufficient contracts* guaranteeing that an encoding closes to tolerance on the stated domain. They are not classification theorems: failure of a listed inequality does not imply that no encoding exists.

</div>

<div class="remark">

*Remark 43* (Status of numerical thresholds). Numerical coefficients displayed below are declared chart-design thresholds, not universal constants derived by A0. A physical realization must justify or replace them and verify every associated closure estimate.

</div>

## Chart-local control quantities

The following quantities are *chart-local*: they are defined only when the corresponding encoding supplies the structures needed to define them. They are not global invariants of the typed projection system.

- Basin separation scale (when a basin partition exists):
  ``` math
  \Delta_B := \inf_{i\neq j} d_Y(B_i,B_j).
  ```

- Capacity floor on the chart domain:
  ``` math
  C_{\min} := \inf_{x\in A} C(x).
  ```

- Contractivity slack:
  ``` math
  s_\kappa := 1-\kappa.
  ```

All inequalities below are sufficient but not necessary.

## Encoding E$`_1`$: Finite-Basin Operator Chart

#### Existence hypothesis

The reduced space $`Y_A`$ admits a finite or effectively finite collection of basins $`\{B_i\}`$ with well-defined separation.

#### Validity conditions

``` math
\begin{align}
\varepsilon &\le \tfrac{1}{10}\Delta_B, \\
\kappa &\le \tfrac{1}{2}, \\
C_{\min} &\ge C_1 > 0.
\end{align}
```

#### Closure contract

The chart is admitted only if a linear map $`F`$ on $`Z`$ is supplied and verified to satisfy
``` math
E(T_A(y)) = F(E(y)) + \delta(y),
\quad \|\delta(y)\|\le c_1\,\varepsilon .
```

#### Failure

This chart contract fails when basin separation is lost, $`\kappa\to 1`$, or $`C_{\min}\to 0`$; another encoding may still exist.

## Encoding E$`_2`$: Local Patch Algebra Chart

#### Existence hypothesis

The admissible domain admits a cover by overlapping admissible subdomains $`\{A_\alpha\}`$, but no global admissible section exists.

#### Validity conditions

``` math
\begin{align}
\inf_\alpha \inf_{x\in A_\alpha} C(x) &\ge C_2 > 0, \\
\sup_\alpha \kappa_\alpha &\le \kappa_2 < 1.
\end{align}
```

On overlaps $`A_{\alpha\beta}`$,
``` math
\|E_\beta(y) - f_{\alpha\beta}(E_\alpha(y))\|
\le c_2\,\varepsilon .
```

#### Obstruction contract

A claimed global obstruction must be exhibited by incompatible transition cocycles or a proved lower bound forcing every glue error above $`\varepsilon`$. Local overlap alone is not an obstruction.

#### Failure

Overlap incompatibility or capacity collapse.

## Encoding E$`_3`$: Two-Derivative Bookkeeping Chart

#### Existence hypothesis

Variations of basin representatives are slow enough that a second-order truncation is meaningful.

#### Validity conditions

``` math
\begin{align}
C_{\min} &\ge C_3 > 0, \\
q_\alpha &\le 1-s_3<1
\end{align}
```

Let $`\eta_3`$ denote the ratio of neglected higher-order terms to retained second-order terms. Require
``` math
\eta_3 \le c_3\,\varepsilon .
```

#### Closure contract

One must verify
``` math
E(T_A(y)) = E(y) + \mathcal{D}[E(y)] + \delta(y),
\quad \|\delta(y)\|\le c_3'\,\varepsilon .
```

#### Failure

Higher-order terms become unsuppressed or $`C\to 0`$.

## Encoding E$`_4`$: Scale-Step Truncation Chart

#### Existence hypothesis

There exists a hierarchy of reduced coordinates ordered by relevance.

#### Validity conditions

``` math
\begin{align}
C_{\min} &\ge C_4 > 0, \\
\rho_N &\le \varepsilon, \\
\kappa &\le 1 - c_4\,\varepsilon .
\end{align}
```

Here $`\rho_N`$ denotes a chart-local bound on the cumulative contribution of discarded coordinates.

#### Closure contract

One must verify
``` math
E(T_A(y)) = F(E(y)) + \delta(y),
\quad \|\delta(y)\|\le c_4'\,\varepsilon .
```

#### Failure

Discarded contributions exceed tolerance or $`\kappa\to 1`$.

## Encoding E$`_5`$: Auxiliary Fixed-Point Chart

#### Existence hypothesis

There exists an auxiliary representation $`Z_{\mathrm{aux}}`$ in which the reduced dynamics is near a stable fixed point.

#### Validity conditions

``` math
\begin{align}
\|\beta(E(y))\| &\le c_5\,\varepsilon, \\
\|D\beta\| &\le 1 - s_5, \\
C_{\min} &\ge C_5 > 0.
\end{align}
```

#### Closure contract

The auxiliary map must preserve a complete neighborhood and satisfy an exact contraction there, or a separate fixed-point existence theorem must be provided. A spectral-radius bound alone is insufficient for a nonnormal linearization.

#### Failure

Loss of auxiliary stability or capacity collapse.

## Encoding E$`_6`$: Spectral Operator Chart

#### Existence hypothesis

The encoding supplies operators whose spectra are meaningful on the admissible domain.

#### Validity conditions

``` math
\begin{align}
\varepsilon &\le \tfrac{1}{10}\Delta_D, \\
\|[D,a]\| &\le K_6, \\
C_{\min} &\ge C_6 > 0.
\end{align}
```

#### Closure contract

Dependence on spectral data only, with its error bound, must be verified for the declared operator domain.

#### Failure

Spectral gap closure or operator norm divergence.

## Encoding E$`_7`$: Boundary and Reset Chart

#### Existence hypothesis

Capacity reaches a declared boundary and an additional continuation or reset rule $`J_e`$ is supplied.

#### Validity conditions

``` math
\begin{align}
0 < C_{\min} &\le C_7, \\
\tau_e &\ge \tau_7 > 0.
\end{align}
```

Reset labels must be stable under $`\varepsilon`$-perturbations, $`J_e`$ must be measurable, and any required conservation law must be checked. Post-reset basins must satisfy FCC with positive slack. If probabilities are assigned, a measure or stochastic kernel must also be supplied.

#### Failure

Event clustering, unstable post-selection basins, or $`C<0`$.

## Encoding E$`_8`$: Relational Transition Chart

This encoding applies when no single-valued reduced evolution is admissible, but stable relational structure persists.

#### Existence hypothesis

- The descent criterion <a href="#eq:descent" data-reference-type="eqref" data-reference="eq:descent">[eq:descent]</a> fails on the neighborhood of interest, so no autonomous single-valued reduced map exists there.

- The typed reduced relation
  ``` math
  \mathcal{R}_t :=
  \{(P_0x,P_t\Phi_tx):x\in X_0\}\subseteq Y_0\times Y_t
  ```
  admits a stable restriction.

#### Variables

The reduced data are not points in a coordinate space, but *relations*:
``` math
Z_{\mathrm{rel}} \subseteq Y_0\times Y_t.
```

#### Chart map

``` math
E : Y_0 \to \mathcal{P}(Y_t),
\qquad
E(y) := \{y' \mid (y,y')\in\mathcal{R}_t\},
```
where $`\mathcal{P}(Y_t)`$ denotes the power set of $`Y_t`$.

#### Closure contract

For a declared semigroup $`\Phi_{s+t}=\Phi_s\Phi_t`$ with compatible time-indexed reductions, relational composition must be checked in the typed form
``` math
\mathcal{R}_s\circ\mathcal{R}_t
\subseteq \mathcal{R}_{s+t}
\quad\text{up to the declared tolerance}.
```
Transitivity of one fixed-time relation is not automatic.

#### Validity conditions

``` math
\begin{align}
C_{\min} &\ge C_8 > 0, \\
\text{Autonomous descent} &\text{ fails on the domain.}
\end{align}
```

#### Failure

- Relational structure becomes unstable or dense;

- No controlled restriction of $`\mathcal{R}_t`$ exists;

- Coherence capacity collapses globally.

#### Remarks

This encoding is one possible weak description when deterministic descent fails. It captures persistent constraints on allowed transitions without introducing local coordinates, states, or probabilities.

## Encoding E$`_9`$: Statistical Ensemble Chart

This encoding applies when local or pointwise reduced descriptions fail, but stable statistical structure persists without a well-defined invariant measure.

#### Existence hypothesis

- No admissible invariant or stationary measure exists on the admissible domain.

- Long-time empirical averages or ensemble summaries stabilize under reduced evolution.

- Single-trajectory descriptions do not close, but aggregate quantities do.

#### Variables

The reduced variables are ensemble summaries:
``` math
Z_{\mathrm{stat}} := \{\text{empirical distributions, moments, or coarse summaries}\}.
```

#### Chart map

``` math
E : Y_A \to Z_{\mathrm{stat}},
\qquad
E(y) := \lim_{N\to\infty} \frac{1}{N}\sum_{k=1}^N \mathcal{O}(T_A^k(y)),
```
whenever the limit exists for the chosen summary observable $`\mathcal{O}`$.

#### Closure contract

The chart is admitted only if ensemble evolution closes approximately:
``` math
E(T_A(y)) = F(E(y)) + \delta(y),
\qquad \|\delta(y)\|\le c_9\,\varepsilon,
```
even though no pointwise closure exists.

#### Validity conditions

``` math
\begin{align}
C_{\min} &\ge C_9 > 0, \\
\text{No invariant measure } \mu &\text{ exists on the domain.}
\end{align}
```

#### Failure

- Ensemble summaries fail to stabilize;

- Strong nonstationarity destroys aggregate closure;

- Capacity collapses and no admissible encoding remains.

#### Remarks

This empirical-summary encoding does not itself invoke probability, random variables, or stochastic dynamics. It is not universally ordered above or below the relational encoding; comparison requires a proved re-encoding.

## Atlas summary

Admissible encodings range from coordinate descriptions to relational and statistical summaries. In a particular realization one may observe a schematic transition
``` math
E_1 \;\to\; \cdots \;\to\; E_7 \;\to\; E_9 \;\to\; E_8,
```
but A0 does not prove this ordering. Each arrow requires an overlap factorization and a verified margin comparison.

# Admissibility Boundaries and Selection

This section analyzes the failure of admissible reduced descriptions. All notions refer to the definitions in Section 1 and are purely structural.

## Admissibility barriers

We recall the definition of an admissibility barrier from Definition <a href="#def:admissibility-barrier" data-reference-type="ref" data-reference="def:admissibility-barrier">19</a>. No additional structure is assumed here.

## Termination of encodings

<div class="proposition">

**Proposition 44** (Loss of an encoding certificate at a barrier). *Let $`\mathcal{E}=(A,Z,E,F,\varepsilon)`$ be an admissible encoding. If a trajectory reaches a barrier at which one of $`\mathcal E`$’s required margins vanishes, then the existing certificate for $`\mathcal E`$ ends there. Continuation requires a new proof restoring that margin, a different encoding, or an additional continuation law.*

</div>

<div class="proof">

*Proof.* Positive slack in every declared margin is part of admissibility. At the named zero margin, that hypothesis is no longer available. ◻

</div>

## Selection events

<div class="definition">

**Definition 45** (Declared selection or reset event). A selection event consists of a margin crossing together with a supplied continuation rule
``` math
J_e:\mathcal B_e\times\Lambda_e\longrightarrow
\bigcup_\alpha D_\alpha,
```
where $`\Lambda_e`$ contains any extra label or random input. The rule must be typed, measurable in probabilistic uses, and compatible with every claimed conservation law.

</div>

Margin saturation alone terminates a certificate; it does not choose an outcome or construct $`J_e`$.

## Irreversibility of selection

<div class="proposition">

**Proposition 46** (Conditional effective irreversibility). *A declared reset is irreversible at the effective level if its induced map from pre-event effective states to post-event effective states is noninjective. Exact upper recovery is impossible if the corresponding typed upper-to-output map is noninjective. Neither statement follows from loss of FCC alone, and neither establishes a physical arrow of time without an oriented asymmetric evolution law.*

</div>

## Boundary layers

<div class="definition">

**Definition 47** (Boundary layer). A $`\delta`$-boundary layer for the declared margins is
``` math
\mathcal L_\delta:=\{x:0<C(x)\le\delta\}.
```

</div>

<div class="remark">

*Remark 48*. Small margin identifies proximity to failure only for the declared contract. Sensitivity amplification, coordinate independence, or common scaling between encodings requires a comparison theorem for their margins.

</div>

## Records

<div class="definition">

**Definition 49** (Record). A record for $`T`$ is a measurable map $`R_{\rm rec}`$ on a forward-invariant post-event domain such that
``` math
R_{\rm rec}\circ T=R_{\rm rec}.
```

</div>

<div class="proposition">

**Proposition 50** (Record persistence). *Once such an $`R_{\rm rec}`$ is supplied, its value is constant along every forward orbit in its domain.*

</div>

<div class="proof">

*Proof.* Iterate the defining identity. ◻

</div>

FCC alone does not construct a nontrivial record. A partial order on events also requires an oriented event relation and record compatibility.

## Probability at boundaries (conditional)

Let $`\mu`$ be a declared upper probability measure and let $`\{B_i\}`$ be a measurable partition of the post-event reduced domain. The conditional numbers
``` math
W_i =
\frac{\mu(P_0^{-1}(B_i)\cap A_e)}
{\sum_j \mu(P_0^{-1}(B_j)\cap A_e)}
```
are probabilities when the denominator is positive. They describe the chosen measure and event domain $`A_e`$; they are not selected by the barrier and are not asserted to be Born weights.

## No global reversibility

<div class="remark">

*Remark 51*. Finite admissibility rules out one globally certified admissible encoding at the adopted axiom tier. It does not by itself rule out an invertible global relation, a reversible upper evolution, or a different reduced description whose hypotheses are not those of A0.

</div>

## Boundary summary

Admissibility barriers mark the limits of a named certificate. At such a limit one must stop, prove a continuation, switch to another verified encoding, or supply a reset law. Selection, probability, records, and irreversibility are separate gates.

# Part III: Structural Closure

# Exact and Controlled Relations Between Encodings

Category language is exact. We therefore define an exact category first and keep tolerance errors as explicit controlled data rather than silently quotienting by a relation that may fail to be a congruence.

## The exact local category

Fix one admissible domain $`A`$, protocol $`\pi`$, reduced space $`Y_A=P_0(A)`$, and self-map $`T_A`$.

<div class="definition">

**Definition 52** (Exact encoding object). An object of $`\mathbf{AdmEnc}_0(A,T_A)`$ is a triple
``` math
\mathcal E=(Z,E,F)
```
with $`E:Y_A\to Z`$, $`F:Z\to Z`$, and
``` math
E\circ T_A=F\circ E.
```

</div>

<div class="definition">

**Definition 53** (Exact re-encoding morphism). A morphism $`f:\mathcal E_1\to\mathcal E_2`$ is a map $`f:Z_1\to Z_2`$ satisfying
``` math
E_2=f\circ E_1,
\qquad
f\circ F_1=F_2\circ f
\quad\text{on }E_1(Y_A).
```

</div>

<div class="proposition">

**Proposition 54**. *Identity maps and ordinary composition make $`\mathbf{AdmEnc}_0(A,T_A)`$ a category.*

</div>

<div class="proof">

*Proof.* Both factorization identities are preserved by identity maps and by composition. ◻

</div>

## The correctly oriented universal object

<div class="definition">

**Definition 55** (Identity encoding).
``` math
\mathcal C_A:=(Y_A,\operatorname{id}_{Y_A},T_A).
```

</div>

<div id="thm:initiality" class="theorem">

**Theorem 56** (Local initiality). *$`\mathcal C_A`$ is initial in $`\mathbf{AdmEnc}_0(A,T_A)`$. For every exact encoding $`\mathcal E=(Z,E,F)`$, the unique morphism $`\mathcal C_A\to\mathcal E`$ is $`E`$.*

</div>

<div class="proof">

*Proof.* The object identity $`E\circ T_A=F\circ E`$ is exactly the dynamical intertwining condition. The equation $`E=f\circ\operatorname{id}`$ forces $`f=E`$. ◻

</div>

<div class="proposition">

**Proposition 57** (Recovery from an encoding). *A morphism $`\mathcal E\to\mathcal C_A`$ exists if and only if $`\operatorname{id}_{Y_A}`$ factors through $`E`$. Equivalently,
``` math
E(y)=E(y')\Longrightarrow y=y',
```
and a suitable inverse on $`E(Y_A)`$ exists in the declared regularity category.*

</div>

<div class="remark">

*Remark 58*. Version 1 reversed this arrow and called $`\mathcal C_A`$ terminal. A general encoding can discard reduced information, so recovery of $`Y_A`$ from its coordinates is an additional injectivity and regularity theorem.

</div>

## Controlled approximate re-encodings

For approximate encodings, retain an explicit defect
``` math
\|E\circ T_A-F\circ E\|\le\eta
```
on a declared domain. A controlled arrow $`f:\mathcal E_1\to\mathcal E_2`$ records both a factorization defect $`\|E_2-fE_1\|\le\eta_f`$ and a dynamical-intertwining defect. If $`g`$ is $`L_g`$-Lipschitz, then the factorization defect of $`g\circ f`$ is at most
``` math
\eta_g+L_g\eta_f.
```
Thus controlled arrows compose with an explicit error budget. A quotient category may be formed only after the proposed tolerance relation is proved to be an equivalence relation compatible with this composition; A0 does not assume such a quotient.

## Overlaps and global scope

For encodings on $`A_1`$ and $`A_2`$, first restrict to $`Y_{12}:=P_0(A_1\cap A_2)`$. Theorem <a href="#thm:encoding-factor" data-reference-type="ref" data-reference="thm:encoding-factor">38</a>, plus the declared regularity and error estimates, decides whether a transition map exists. Nonempty overlap alone is insufficient.

The finite-admissibility axiom excludes an exact or controlled *admissible* object whose domain is all of $`X_0`$. A particular pair of charts fails to glue only when a transition obstruction or incompatible margin is actually proved.

## Pushforward probability as an optional functor

Let $`\nu`$ be a declared probability measure on $`Y_A`$, and restrict to measurable exact encodings and measurable morphisms. Assign to $`\mathcal E=(Z,E,F)`$ the pushforward probability space $`(Z,E_\#\nu)`$, and to $`f:\mathcal E_1\to\mathcal E_2`$ the measurable pushforward map $`f`$. Since $`E_2=fE_1`$,
``` math
(E_2)_\#\nu=f_\#(E_1)_\#\nu,
```
so this assignment is a functor to probability spaces. The functor uses the supplied $`\nu`$; category structure does not create it.

## Category summary

The identity encoding is locally initial, not terminal. Arrows out of it are encodings; arrows back to it are recovery maps. Approximate arrows carry error budgets, and global gluing remains a separate descent problem.

# Part IV: Total Atlas

# Total Atlas: A Global Chart-of-Charts

This section introduces a global object that *contains* all admissible encodings without asserting the existence of any single globally valid encoding. It formalizes the idea of a *total chart* as a chart-of-charts.

## Local encoding fiber

<div class="definition">

**Definition 59** (Encoding fiber). For each $`x\in X_0`$, define
``` math
\mathrm{Enc}(x):=
\{\mathcal E:\mathcal E\text{ is a verified exact or controlled encoding
on some }A\ni x\}.
```

</div>

<div class="remark">

*Remark 60*. $`\mathrm{Enc}(x)`$ is the set of all reduced descriptions available at $`x`$. Finite admissibility says no single verified chart has domain $`X_0`$; it does not imply that any point is uncovered by the union of local charts.

</div>

## Total encoding family

<div class="definition">

**Definition 61** (Total encoding projection). Define the total encoding space
``` math
\mathbb{E} := \{(x,\mathcal{E}) \mid x\in X_0,\ \mathcal{E}\in \mathrm{Enc}(x)\},
```
with projection map
``` math
\pi:\mathbb{E}\to X_0,\qquad \pi(x,\mathcal{E})=x.
```

</div>

<div class="remark">

*Remark 62*. The fiber $`\pi^{-1}(x)`$ is canonically identified with $`\mathrm{Enc}(x)`$. Without a topology and local trivializations, $`\pi`$ is a set-theoretic fibered family, not a fiber bundle. It is not itself an encoding.

</div>

## Admissibility limits as fiber collapse

<div class="definition">

**Definition 63** (Encodability set). Define the encodable subset of $`X_0`$ by
``` math
X_{\mathrm{enc}} := \{x\in X_0 \mid \mathrm{Enc}(x)\neq\varnothing\}.
```

</div>

<div class="definition">

**Definition 64** (Encoding boundary set). Define the topological boundary as
``` math
\partial X_{\mathrm{enc}} :=
\overline{X_{\mathrm{enc}}}
\setminus\operatorname{int}(X_{\mathrm{enc}}).
```

</div>

<div class="remark">

*Remark 65*. Boundary points are accumulation points of both encodable and non-interior behavior. A claim that availability actually collapses there requires upper-semicontinuity or a specific margin theorem.

</div>

## Chart viability field

The atlas in Section 3 provides *sufficient contracts* in terms of local control quantities. We now compress those contracts into a single diagnostic.

<div class="definition">

**Definition 66** (Chart viability functional). For an encoding $`\mathcal{E}`$ and a point $`x\in X_0`$, define a chart viability score
``` math
\mathcal{V}_{\mathcal{E}}(x) \in \mathbb{R}
```
as any scalar functional such that:

1.  $`\mathcal{V}_{\mathcal{E}}(x)>0`$ implies $`x\in A_{\mathcal{E}}`$ and all stated inequality contracts of $`\mathcal{E}`$ hold at $`x`$;

2.  $`\mathcal{V}_{\mathcal{E}}(x)\le 0`$ implies at least one contract of $`\mathcal{E}`$ fails at $`x`$.

</div>

<div class="remark">

*Remark 67*. $`\mathcal{V}_{\mathcal{E}}`$ is not unique; it is a diagnostic that packages the inequality contracts of $`\mathcal{E}`$ into a single scalar. Scores for different encodings are comparable only after a common normalization is declared.

</div>

<div class="definition">

**Definition 68** (Maximal viability). Define the maximal viability at $`x`$ by
``` math
\mathcal{V}^\ast(x) := \sup_{\mathcal{E}\in \mathrm{Enc}(x)} \mathcal{V}_{\mathcal{E}}(x),
```
with the convention $`\mathcal{V}^\ast(x)=-\infty`$ if $`\mathrm{Enc}(x)=\varnothing`$.

</div>

<div class="remark">

*Remark 69*. With a common normalization, $`\mathcal{V}^\ast(x)`$ is a best-margin diagnostic. Relating its sign or continuity to $`\partial X_{\mathrm{enc}}`$ requires additional regularity of the encoding family.

</div>

## The overlap nerve of the atlas

We now define a global topological summary of chart overlap.

<div class="definition">

**Definition 70** (Overlap relation). Two encodings $`\mathcal{E}_i=(A_i,\dots)`$ and $`\mathcal{E}_j=(A_j,\dots)`$ overlap if
``` math
A_i\cap A_j \neq \varnothing
```
and there exists an exact re-encoding morphism or a controlled arrow with an explicit error budget on the overlap.

</div>

<div class="definition">

**Definition 71** (Atlas nerve). Let $`\{\mathcal{E}_\alpha\}`$ be a chosen family of encodings. The nerve $`\mathcal{N}`$ is the simplicial complex whose:

- vertices are encodings $`\mathcal{E}_\alpha`$;

- a $`k`$-simplex $`(\mathcal{E}_{\alpha_0},\dots,\mathcal{E}_{\alpha_k})`$ exists iff $`\bigcap_{i=0}^k A_{\alpha_i}\neq\varnothing`$ and transition morphisms are controlled on that intersection.

</div>

<div class="remark">

*Remark 72*. The nerve records the combinatorics of a chosen cover. A hole in the nerve is not automatically a gluing obstruction; that conclusion requires the appropriate good-cover hypotheses and a nontrivial transition cocycle or cohomology class.

</div>

## Universal reduced relation

Independently of whether deterministic descent holds, the typed data define a global relation.

<div class="definition">

**Definition 73** (Universal reduced relation). Define
``` math
\mathcal{R}_t:=
\{(P_0x,P_t\Phi_tx):x\in X_0\}\subseteq Y_0\times Y_t.
```

</div>

<div class="remark">

*Remark 74*. $`\mathcal{R}_t`$ is always well-defined. It is the graph of a single-valued map $`F_t:Y_0\to Y_t`$ exactly when the descent criterion <a href="#eq:descent" data-reference-type="eqref" data-reference="eq:descent">[eq:descent]</a> holds. A representative section chooses one value from compatible upper representatives; it does not make the full relation a graph when descent fails.

</div>

## Total-atlas summary

The total atlas consists of:

- the total encoding projection $`\pi:\mathbb{E}\to X_0`$;

- the normalized viability diagnostic $`\mathcal{V}^\ast`$, when a common normalization is supplied;

- the overlap nerve $`\mathcal{N}`$ recording the chosen cover and its controlled transition data;

- the typed relation $`\mathcal{R}_t\subseteq Y_0\times Y_t`$.

No single global admissible encoding is asserted. The chart-of-charts records local availability without converting local contracts into a global physical law.

# Conclusion

Modal Triplet Theory is presented here as a conditional, non-self-sealing framework. It asserts no ontology and no universal effective law. Instead, it gives checkable gates for representative selection, exact recovery, autonomous descent, basin-local stability, controlled re-encoding, and measure-dependent probability. Finite admissibility is a stated axiom about certified encodings, not a consequence of noninjectivity. Every stronger conclusion must identify the margin, measure, dynamics, or physical source theorem that supplies it.

Any physical interpretation is an external assignment layered atop the mathematical structure developed herein.
