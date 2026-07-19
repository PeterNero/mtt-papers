---
abstract: |
  We present a clean, non-circular formulation of Modal Triplet Theory (MTT): a conditional framework governing when stable reduced descriptions exist, how they relate, and why no global reduced description is possible. The theory is formulated abstractly in terms of projection, admissibility, and contractive induced dynamics, with explicit realizations treated as non-axiomatic instantiations.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: January 2026
generated_from_main_tex_sha256: 5ba6c248295a7d530e6da6b4f64c9532574cd59fc7afb22df838e3c603c3628b
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

# Part I: Abstract Framework

# Definitions and Conventions

This section fixes notation and logical order. All definitions are purely mathematical. No physical interpretation is assumed.

## Abstract projection system

<div class="definition">

**Definition 1** (Abstract system). An abstract projection system is a triple
``` math
(X,\;\Phi,\;P)
```
where:

- $`X`$ is a standard measurable space,

- $`\Phi : X \to X`$ is an invertible measurable evolution (or flow $`\Phi_t`$),

- $`P : X \to Y`$ is a measurable, generally non-injective map into a reduced space $`Y`$.

</div>

## Tolerance

<div class="definition">

**Definition 2** (Tolerance). Fix $`\varepsilon>0`$. Two points $`y_1,y_2\in Y`$ are indistinguishable if
``` math
d_Y(y_1,y_2)\le \varepsilon,
```
where $`d_Y`$ is a chosen pseudometric.

</div>

## Admissible domains

<div class="definition">

**Definition 3** (Admissible domain). A subset $`A\subset X`$ is admissible if:

1.  $`P|_A`$ is measurable and locally regular;

2.  there exists a measurable section
    ``` math
    S_A : P(A)\to A
    ```
    such that $`P\circ S_A = \mathrm{id}`$ up to tolerance, and such that $`S_A`$ is *robust* on $`P(A)`$ (e.g. stable in measure under $`\varepsilon`$-perturbations of $`y\in P(A)`$);

3.  there exists a (possibly non-singleton) protocol index set $`\Pi_A`$ and, for each $`\pi\in\Pi_A`$, a measurable section
    ``` math
    S_{A,\pi}:P(A)\to A
    ```
    such that $`P\circ S_{A,\pi}=\mathrm{id}`$ up to tolerance, and an induced reduced map
    ``` math
    T_{A,\pi} := P\circ\Phi_{\tau(\pi)}\circ S_{A,\pi}:P(A)\to P(A)
    ```
    that is well-defined and stable.

</div>

<div class="axiom">

**Axiom 1** (Finite admissibility). *There exists no admissible domain $`A`$ with $`A=X`$.*

</div>

## Fundamental Contractivity Condition

<div class="definition">

**Definition 4** (FCC). An admissible domain $`A`$ satisfies FCC if for each $`\pi\in\Pi_A`$ there exist constants $`0<\kappa_\pi<1`$ and $`c_\pi<\infty`$ such that
``` math
d_Y\!\big(T_{A,\pi}(y),T_{A,\pi}(y')\big)
\le \kappa_\pi\, d_Y(y,y') + c_\pi\,\varepsilon
\quad \forall y,y'\in P(A).
```

</div>

<div class="remark">

*Remark 5*. Different $`\pi\in\Pi_A`$ represent distinct admissible protocol/context choices. All stability, basin, and encoding statements in this document apply pointwise in $`\pi`$.

</div>

<div class="remark">

*Remark 6*. FCC is a *local* property of an admissible domain $`A`$ together with a chosen section $`S_A`$, hence of the induced reduced map $`T_A`$. It is not assumed to hold globally on $`X`$.

</div>

## Fixed points and basins

<div class="definition">

**Definition 7** (Fixed-point set). A subset $`\mathfrak S\subset P(A)`$ is a fixed-point set if
``` math
\sup_{y\in\mathfrak S} d_Y\!\big(T_A(y),y\big)\le c_\ast\,\varepsilon.
```

</div>

<div class="theorem">

**Theorem 8** (Existence of fixed points). *If FCC holds on $`A`$, then $`T_A`$ admits at least one fixed-point set $`\mathfrak S\subset P(A)`$.*

</div>

<div class="definition">

**Definition 9** (Basin). A basin is a subset $`B\subset P(A)`$ such that
``` math
\limsup_{n\to\infty}
\mathrm{dist}_Y\!\big(T_A^n(y),\mathfrak S\big)\le c_B\,\varepsilon
\quad \forall y\in B.
```

</div>

## Coherence capacity

<div class="definition">

**Definition 10** (Admissibility modules). Let $`\{g_i(x)\}`$ measure violation of admissibility conditions, with $`g_i(x)\le 0`$ indicating validity.

</div>

<div class="definition">

**Definition 11** (Coherence capacity). Define
``` math
C(x) := \min_i (-g_i(x)).
```
Then $`C(x)>0`$ implies admissibility and $`C(x)=0`$ marks saturation.

</div>

## Admissibility barriers

<div class="definition">

**Definition 12** (Admissibility barrier). A measurable set $`\mathcal B\subset X`$ is an admissibility barrier if:

1.  $`X\setminus\mathcal B`$ contains at least two admissible regions $`A_+`$ and $`A_-`$;

2.  there exists $`y\in Y`$ with $`P^{-1}(y)\cap A_+\neq\varnothing`$ and $`P^{-1}(y)\cap A_-\neq\varnothing`$;

3.  no measurable section $`S:P(A_+\cup A_-)\to A_+\cup A_-`$ exists with $`P\circ S=\mathrm{id}`$ up to tolerance.

</div>

## Invariant measure (conditional)

<div class="assumption">

**Assumption 13** (Invariant measure). On an admissible domain $`A`$, there exists an invariant or stationary measure $`\mu`$ preserved by $`\Phi`$.

</div>

## Encodings

<div class="definition">

**Definition 14** (Encoding). An encoding is a tuple
``` math
\mathcal E=(A,\;Z,\;E,\;F,\;\varepsilon)
```
where $`A`$ is admissible and
``` math
E(T_A(y)) = F(E(y)) + \delta(y),
\quad \|\delta(y)\|\le c\,\varepsilon.
```

</div>

<div class="remark">

*Remark 15*. Coherence capacity $`C(x)`$ is not an observable, not a conserved quantity, and not a dynamical degree of freedom. It is a diagnostic margin (a stability/condition number) organizing when admissible encodings exist and when they fail.

</div>

## Interpretation postulate

<div class="postulate">

**Postulate 1**. *When an admissible encoding exists, its reduced structure may be interpreted as a physical description.*

</div>

<div class="remark">

*Remark 16*. Local sections $`S_{A,\pi}`$ may exist on admissible domains. Admissibility barriers assert the obstruction to extending such choices to a single global section across domains. Thus “local representability” does not imply global reconstructibility.

</div>

## Failure modes

The framework is silent if:

- no admissible domain satisfies FCC;

- no invariant measure exists where probability is claimed;

- no measurable section exists anywhere;

- basins are not robust under perturbations.

# Core Structural Results

All results in this section are conditional on the existence of an admissible domain $`A`$ with section $`S_A`$ and reduced map
``` math
T_A := P \circ \Phi_\tau \circ S_A .
```

## Universality under contractive projection

<div class="theorem">

**Theorem 17** (Universality under FCC). *Assume FCC holds on an admissible domain $`A`$. Then for all $`y,y'\in P(A)`$,
``` math
\limsup_{n\to\infty}
d_Y\!\big(T_A^n(y),T_A^n(y')\big)
\;\le\;
\frac{c}{1-\kappa}\,\varepsilon .
```*

</div>

<div class="remark">

*Remark 18*. This expresses convergence to a common fixed-point set up to a tolerance floor. No exact equality or limit point is assumed.

</div>

## Admissible prediction depth

<div class="definition">

**Definition 19** (Admissible prediction depth). Fix an admissible domain $`A`$ and protocol $`\pi\in\Pi_A`$. For $`x\in A`$, define the admissible prediction depth
``` math
N_{\max}(x;A,\pi,\varepsilon)
:=
\sup\Big\{n\in\mathbb{N}\ \Big|\ \text{the reduced iterates }
T_{A,\pi}^k(P(x)) \text{ remain within } P(A) \text{ for all } k\le n\Big\}.
```

</div>

<div class="remark">

*Remark 20*. $`N_{\max}`$ provides a regime-intrinsic notion of finite predictivity without invoking external time. In boundary layers ($`0<C\ll 1`$), $`N_{\max}`$ is typically small; deep in stable basins it may be large.

</div>

## Computational limits (optional)

<div class="proposition">

**Proposition 21** (Conditional undecidability of selection questions). *In regimes where admissibility depends on protocol choice and where prediction depth $`N_{\max}(x;A,\pi,\varepsilon)`$ is finite but instance-dependent, there exist well-posed decision problems about reduced evolution and selection (e.g. whether a specified basin is entered before admissibility is lost) that are not decidable by any uniform algorithm from finite descriptions of initial reduced data and protocol parameters.*

</div>

<div class="remark">

*Remark 22*. This proposition is included as an optional structural consequence layer. Its role is to record that finite admissibility and protocol-dependent projection can imply limits of computability beyond practical complexity.

</div>

## Forgetting of incoherent distinctions

<div class="corollary">

**Corollary 23** (Forgetting). *Let $`y,y'\in P(A)`$ belong to the same basin. Then all distinctions between $`y`$ and $`y'`$ not preserved by the fixed-point set $`\mathfrak S`$ are suppressed under iteration of $`T_A`$ up to tolerance.*

</div>

## Projection–admissibility obstruction

<div class="theorem">

**Theorem 24** (Projection–admissibility obstruction). *Let $`\mathcal B\subset X`$ be an admissibility barrier. There exists no measurable section
``` math
S : P(A_+\cup A_-)\to A_+\cup A_-
```
satisfying $`P\circ S=\mathrm{id}`$ up to tolerance, where $`A_+`$ and $`A_-`$ are admissible regions separated by $`\mathcal B`$.*

</div>

<div class="proof">

*Sketch.* Existence of such a section would contradict the definition of $`\mathcal B`$ as an admissibility barrier. ◻

</div>

## Irreversibility of reduced dynamics

<div class="theorem">

**Theorem 25** (Irreversibility). *On any admissible domain $`A`$ satisfying FCC, the reduced map $`T_A`$ is not invertible up to tolerance on $`P(A)`$.*

</div>

<div class="proof">

*Sketch.* Non-injectivity of $`P`$ implies that multiple points in $`A`$ map to the same $`y\in P(A)`$. FCC ensures contraction of their images under $`T_A`$, preventing reconstruction of preimages. ◻

</div>

Irreversibility is therefore structural, not dynamical.

## Probability from basin structure (conditional)

Assume the existence of an invariant measure $`\mu`$ on $`A`$.

<div class="remark">

*Remark 26*. Assume the basin sets $`B_i\subset P(A)`$ are measurable with respect to the $`\sigma`$-algebra induced on $`P(A)`$ by $`P`$.

</div>

<div class="definition">

**Definition 27** (Basin weights). Let $`\{B_i\}`$ be the basin partition of $`P(A)`$. Define
``` math
W_i :=
\frac{\mu\big(P^{-1}(B_i)\cap A\big)}
{\sum_j \mu\big(P^{-1}(B_j)\cap A\big)} .
```

</div>

<div class="theorem">

**Theorem 28** (Conditional probability theorem). *If a selection event forces choice among basins $`\{B_i\}`$, the weights $`W_i`$ define consistent outcome probabilities.*

</div>

If no invariant measure exists, no canonical basin weighting is asserted; only basin structure and record/selection ordering remain meaningful at the reduced level.

## Maximality of admissible content

<div class="theorem">

**Theorem 29** (Maximality on overlaps). *Let $`\mathcal E_1`$ and $`\mathcal E_2`$ be admissible encodings with overlapping domains. Then on the overlap there exists a controlled re-encoding relating their reduced descriptions up to tolerance.*

</div>

<div class="corollary">

**Corollary 30** (No stronger reduced description). *There exists no admissible encoding whose reduced variables contain strictly more stable descriptive content than that induced by $`P`$.*

</div>

## No global reduced description

<div class="theorem">

**Theorem 31** (No global encoding). *There exists no encoding defined on all of $`X`$.*

</div>

<div class="proof">

*Sketch.* By finite admissibility, no admissible domain covers $`X`$. ◻

</div>

## Interpretive remark

All results above concern reduced descriptions as mathematical objects. Any physical interpretation is an external assignment.

# Part II: Encodings and Boundaries

# Encoding Atlas

This section lists admissible encodings as local charts on neighborhoods of stable basins of the reduced map
``` math
T_A := P \circ \Phi_\tau \circ S_A .
```
Each encoding is specified by sufficient inequality contracts involving the contraction constant $`\kappa`$, tolerance $`\varepsilon`$, and coherence capacity $`C`$.

<div class="remark">

*Remark 32* (Contract nature of atlas inequalities). The inequalities in this atlas are *sufficient contracts* guaranteeing that an encoding closes to tolerance on the stated domain. They are not classification theorems: failure of a listed inequality does not imply that no encoding exists.

</div>

## Chart-local control quantities

The following quantities are *chart-local*: they are defined only when the corresponding encoding supplies the structures needed to define them. They are not global invariants of $`(X,\Phi,P)`$.

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

The reduced space $`P(A)`$ admits a finite or effectively finite collection of basins $`\{B_i\}`$ with well-defined separation.

#### Validity conditions

``` math
\begin{align}
\varepsilon &\le \tfrac{1}{10}\Delta_B, \\
\kappa &\le \tfrac{1}{2}, \\
C_{\min} &\ge C_1 > 0.
\end{align}
```

#### Closure

There exists a linear map $`F`$ on $`Z`$ such that
``` math
E(T_A(y)) = F(E(y)) + \delta(y),
\quad \|\delta(y)\|\le c_1\,\varepsilon .
```

#### Failure

Occurs when basin separation is lost, $`\kappa\to 1`$, or $`C_{\min}\to 0`$.

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

#### Obstruction

Any attempted global choice of coordinates yields a glue error exceeding $`\varepsilon`$.

#### Failure

Overlap incompatibility or capacity collapse.

## Encoding E$`_3`$: Two-Derivative Bookkeeping Chart

#### Existence hypothesis

Variations of basin representatives are slow enough that a second-order truncation is meaningful.

#### Validity conditions

``` math
\begin{align}
C_{\min} &\ge C_3 > 0, \\
0.2 \le \kappa &\le 0.9.
\end{align}
```

Let $`\eta_3`$ denote the ratio of neglected higher-order terms to retained second-order terms. Require
``` math
\eta_3 \le c_3\,\varepsilon .
```

#### Closure

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

#### Closure

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
\rho(D\beta) &\le 1 - s_5, \\
C_{\min} &\ge C_5 > 0.
\end{align}
```

#### Closure

Auxiliary flow remains within tolerance of a fixed point.

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

#### Closure

Dynamics depend only on spectral data up to tolerance.

#### Failure

Spectral gap closure or operator norm divergence.

## Encoding E$`_7`$: Event-Selection Chart

#### Existence hypothesis

Capacity varies sharply enough that isolated selection events occur.

#### Validity conditions

``` math
\begin{align}
0 < C_{\min} &\le C_7, \\
\tau_e &\ge \tau_7 > 0.
\end{align}
```

Selection labels must be stable under $`\varepsilon`$-perturbations, and post-selection basins must satisfy FCC with positive slack.

#### Failure

Event clustering, unstable post-selection basins, or $`C<0`$.

## Encoding E$`_8`$: Relational Transition Chart

This encoding applies when no single-valued reduced evolution is admissible, but stable relational structure persists.

#### Existence hypothesis

- No admissible section $`S_A`$ exists that yields a single-valued reduced map on any neighborhood of interest.

- The universal reduced relation
  ``` math
  \mathcal{R} := \{(y,y')\in Y\times Y \mid \exists x\in X:\ y=P(x),\ y'=P(\Phi_\tau(x))\}
  ```
  admits a stable restriction on a subset of $`Y\times Y`$.

#### Variables

The reduced data are not points in a coordinate space, but *relations*:
``` math
Z_{\mathrm{rel}} \subset Y\times Y.
```

#### Chart map

``` math
E : P(A) \to \mathcal{P}(Y),
\qquad
E(y) := \{y' \mid (y,y')\in\mathcal{R}\},
```
where $`\mathcal{P}(Y)`$ denotes the power set of $`Y`$.

#### Closure

Relational composition closes up to tolerance:
``` math
(y,y')\in Z_{\mathrm{rel}},\ (y',y'')\in Z_{\mathrm{rel}}
\;\Rightarrow\;
(y,y'')\in Z_{\mathrm{rel}} \ \text{up to } \varepsilon.
```

#### Validity conditions

``` math
\begin{align}
C_{\min} &\ge C_8 > 0, \\
\text{No admissible single-valued } T_A &\text{ exists on the domain.}
\end{align}
```

#### Failure

- Relational structure becomes unstable or dense;

- No controlled restriction of $`\mathcal{R}`$ exists;

- Coherence capacity collapses globally.

#### Remarks

This encoding represents the weakest admissible description short of total loss of describability. It captures persistent constraints on allowed transitions without introducing local coordinates, states, or probabilities.

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
E : P(A) \to Z_{\mathrm{stat}},
\qquad
E(y) := \lim_{N\to\infty} \frac{1}{N}\sum_{k=1}^N \mathcal{O}(T_A^k(y)),
```
whenever the limit exists for the chosen summary observable $`\mathcal{O}`$.

#### Closure

Ensemble evolution closes approximately:
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

This encoding is strictly weaker than probabilistic encodings. It captures stable statistical structure without invoking probability, random variables, or stochastic dynamics.

<div class="remark">

*Remark 33* (Interpretive correspondence (non-axiomatic)). In phenomenological applications, regimes dominated by Encoding E$`_9`$ (statistical ensemble structure without local realization) correspond to effects commonly attributed to unseen clustering sources, while regimes dominated by Encoding E$`_8`$ (pure relational transition structure) correspond to uniform large-scale drift without localized sources. No new degrees of freedom are introduced by either encoding.

</div>

## Atlas summary

Admissible encodings range from strong coordinate descriptions to purely relational and statistical encodings. As coherence capacity decreases, admissible encodings weaken in the order
``` math
E_1 \;\to\; \cdots \;\to\; E_7 \;\to\; E_9 \;\to\; E_8,
```
with $`E_8`$ representing the final admissible relational structure before total loss of describability.

# Admissibility Boundaries and Selection

This section analyzes the failure of admissible reduced descriptions. All notions refer to the definitions in Section 1 and are purely structural.

## Admissibility barriers

We recall the definition of an admissibility barrier from Definition <a href="#def:admissibility-barrier" data-reference-type="ref" data-reference="def:admissibility-barrier">[def:admissibility-barrier]</a>. No additional structure is assumed here.

## Termination of encodings

<div class="theorem">

**Theorem 34** (Termination at barriers). *Let $`\mathcal{E}=(A,Z,E,F,\varepsilon)`$ be an admissible encoding. If a trajectory intersects an admissibility barrier $`\mathcal{B}`$, then $`\mathcal{E}`$ cannot be extended across $`\mathcal{B}`$.*

</div>

<div class="proof">

*Sketch.* Extension would require a measurable section of $`P`$ across the barrier, contradicting the defining property of $`\mathcal{B}`$. ◻

</div>

## Selection events

<div class="definition">

**Definition 35** (Selection event). A selection event is a transition of a trajectory from one admissible basin to another when admissibility modules saturate and FCC no longer holds uniformly along the trajectory.

</div>

Selection is defined without reference to outcomes or measurement.

## Irreversibility of selection

<div class="theorem">

**Theorem 36** (Irreversibility of selection). *Selection events are irreversible for all admissible reduced descriptions.*

</div>

<div class="proof">

*Sketch.* Non-injectivity of $`P`$ combined with loss of FCC prevents reconstruction of pre-selection basin membership from post-selection reduced data. ◻

</div>

## Boundary layers

<div class="definition">

**Definition 37** (Boundary layer). A boundary layer is a region where admissibility holds but
``` math
0 < C(x) \ll 1 .
```

</div>

<div class="theorem">

**Theorem 38** (Universality in boundary layers). *All admissible encodings exhibit qualitatively similar behavior in boundary layers, independent of coordinate choice.*

</div>

Such behavior includes sensitivity amplification and loss of global closure.

## Records

<div class="definition">

**Definition 39** (Record). A record is a reduced structure that remains invariant under subsequent admissible reduced evolution after a selection event.

</div>

<div class="theorem">

**Theorem 40** (Record formation). *If the post-selection basin satisfies FCC with positive slack, then records necessarily form.*

</div>

Records induce a partial order on selection events.

## Probability at boundaries (conditional)

Assume the existence of an invariant measure $`\mu`$ on an admissible domain $`A`$.

<div class="theorem">

**Theorem 41** (Boundary probability). *When a selection event forces a choice among basins $`\{B_i\}`$, the basin weights
``` math
W_i =
\frac{\mu(P^{-1}(B_i)\cap A)}
{\sum_j \mu(P^{-1}(B_j)\cap A)}
```
define consistent selection probabilities.*

</div>

If no invariant measure exists, no probabilistic statement is made.

## No global reversibility

<div class="theorem">

**Theorem 42** (No global reversibility). *There exists no reduced description that is reversible across all admissibility barriers.*

</div>

## Boundary summary

Admissibility barriers mark the limits of reduced description. At such limits, encodings must either terminate or be replaced by distinct encodings on other admissible domains.

# Part III: Structural Closure

# Category of Admissible Encodings

This section formalizes relations between admissible encodings using category-theoretic language. All constructions are local to admissible domains and respect tolerance.

## Objects

<div class="definition">

**Definition 43** (Encoding object). An object $`\mathcal{E}`$ of the category $`\mathbf{AdmEnc}`$ is a tuple
``` math
\mathcal{E} = (A,\;Z,\;E,\;F,\;\varepsilon)
```
where:

- $`A\subset X`$ is an admissible domain satisfying FCC;

- $`Z`$ is a reduced coordinate space;

- $`E : P(A)\to Z`$ is a chart map;

- $`F : Z\to Z`$ is a closure map satisfying
  ``` math
  E(T_A(y)) = F(E(y)) + \delta(y),
  \quad \|\delta(y)\|\le c\,\varepsilon;
  ```

- $`\varepsilon>0`$ is the tolerance.

</div>

Objects are local coordinate charts on neighborhoods of stable basins.

## Morphisms

<div class="definition">

**Definition 44** (Re-encoding morphism). Let $`\mathcal{E}_1=(A_1,Z_1,E_1,F_1,\varepsilon)`$ and $`\mathcal{E}_2=(A_2,Z_2,E_2,F_2,\varepsilon)`$.

A morphism
``` math
f:\mathcal{E}_1 \to \mathcal{E}_2
```
exists if $`A_{12}:=A_1\cap A_2\neq\varnothing`$ and there is a map $`f:Z_1\to Z_2`$ such that
``` math
E_2(y) = f(E_1(y)) + \delta_{12}(y),
\quad \|\delta_{12}(y)\|\le c_{12}\,\varepsilon
```
for all $`y\in P(A_{12})`$.

</div>

Morphisms represent controlled re-encodings on overlaps.

## Composition

Morphisms compose by ordinary composition of maps on reduced spaces. Composition is defined only on triple overlaps $`A_1\cap A_2\cap A_3`$ and accumulated error must remain bounded by a constant multiple of $`\varepsilon`$.

## Quotient by tolerance

<div class="definition">

**Definition 45** (Tolerance equivalence). Two morphisms $`f,g:\mathcal{E}_1\to\mathcal{E}_2`$ are equivalent if
``` math
\sup_{y\in P(A_{12})}\|f(E_1(y)) - g(E_1(y))\|
\le c\,\varepsilon .
```

</div>

Let $`\mathbf{AdmEnc}/\!\sim`$ denote the quotient category.

## Coherent encoding on a domain

<div class="definition">

**Definition 46** (Coherent encoding). Given an admissible domain $`A`$ with section $`S_A`$ and reduced map $`T_A`$, define the coherent encoding
``` math
\mathcal{C}_A := (A,\;P(A),\;\mathrm{id},\;T_A,\;\varepsilon).
```

</div>

## Local universal factorization

<div class="theorem">

**Theorem 47** (Local factorization). *Let $`\mathcal{E}`$ be an encoding defined on an admissible domain $`A`$. Then there exists a unique morphism
``` math
f_{\mathcal{E}}:\mathcal{E}\to\mathcal{C}_A
```
in $`\mathbf{AdmEnc}/\!\sim`$.*

</div>

This expresses that all admissible encodings on $`A`$ reduce to the same coherent content on $`P(A)`$.

## Local terminality

<div class="theorem">

**Theorem 48** (Local terminality). *For a fixed admissible domain $`A`$, the coherent encoding $`\mathcal{C}_A`$ is terminal in the full subcategory of $`\mathbf{AdmEnc}/\!\sim`$ consisting of encodings defined on $`A`$.*

</div>

<div class="remark">

*Remark 49*. Terminality is local in $`A`$. No claim of global terminality is made.

</div>

## Obstruction to global objects

<div class="theorem">

**Theorem 50** (No extension across barriers). *Let $`\mathcal{E}_+`$ and $`\mathcal{E}_-`$ be encodings defined on admissible domains $`A_+`$ and $`A_-`$ separated by an admissibility barrier. There exists no encoding defined on $`A_+\cup A_-`$ that restricts to both.*

</div>

<div class="corollary">

**Corollary 51** (No global encoding). *There exists no object of $`\mathbf{AdmEnc}`$ whose domain is all of $`X`$.*

</div>

## Probability as a functor (conditional)

Assume the existence of an invariant measure $`\mu`$ on an admissible domain $`A`$.

<div class="definition">

**Definition 52** (Selection functor). Define a functor
``` math
\mathsf{Sel} : \mathbf{AdmEnc} \to \mathbf{Prob}
```
mapping encodings on $`A`$ to probability spaces whose weights are given by basin measures, and morphisms to pushforward maps.

</div>

<div class="theorem">

**Theorem 53** (Functorial probability). *Probability assignments are functorial images of basin partitions under $`\mathsf{Sel}`$.*

</div>

If no invariant measure exists, $`\mathsf{Sel}`$ is undefined.

## Category summary

The category $`\mathbf{AdmEnc}`$ formalizes local reduced descriptions and their relations. Its quotient by tolerance admits local terminal objects but no global object.

# Part IV: Total Atlas

# Total Atlas: A Global Chart-of-Charts

This section introduces a global object that *contains* all admissible encodings without asserting the existence of any single globally valid encoding. It formalizes the idea of a *total chart* as a chart-of-charts.

## Local encoding fiber

<div class="definition">

**Definition 54** (Encoding fiber). Let $`(X,\Phi,P)`$ be an abstract projection system with tolerance $`\varepsilon`$. For each $`x\in X`$, define the encoding fiber
``` math
\mathrm{Enc}(x) := \{\mathcal{E}=(A,Z,E,F,\varepsilon)\in \mathbf{AdmEnc} \mid x\in A\}.
```

</div>

<div class="remark">

*Remark 55*. $`\mathrm{Enc}(x)`$ is the set of all reduced descriptions available at $`x`$. Finite admissibility implies $`\mathrm{Enc}(x)`$ may be empty for some $`x`$.

</div>

## Encoding fibration

<div class="definition">

**Definition 56** (Encoding fibration). Define the total encoding space
``` math
\mathbb{E} := \{(x,\mathcal{E}) \mid x\in X,\ \mathcal{E}\in \mathrm{Enc}(x)\},
```
with projection map
``` math
\pi:\mathbb{E}\to X,\qquad \pi(x,\mathcal{E})=x.
```

</div>

<div class="remark">

*Remark 57*. The fiber $`\pi^{-1}(x)`$ is canonically identified with $`\mathrm{Enc}(x)`$. The object $`\pi:\mathbb{E}\to X`$ is not itself an encoding; it is a *bundle of encodings*.

</div>

## Admissibility limits as fiber collapse

<div class="definition">

**Definition 58** (Encodability set). Define the encodable subset of $`X`$ by
``` math
X_{\mathrm{enc}} := \{x\in X \mid \mathrm{Enc}(x)\neq\varnothing\}.
```

</div>

<div class="definition">

**Definition 59** (Encoding boundary set). Define the encoding boundary set as
``` math
\partial X_{\mathrm{enc}} := \overline{X_{\mathrm{enc}}}\setminus X_{\mathrm{enc}}.
```

</div>

<div class="remark">

*Remark 60*. Points in $`\partial X_{\mathrm{enc}}`$ are precisely those at which encoding availability collapses. This notion is global and does not presuppose a codimension-one geometric boundary.

</div>

## Chart viability field

The atlas in Section 3 provides *sufficient contracts* in terms of local control quantities. We now compress those contracts into a single diagnostic.

<div class="definition">

**Definition 61** (Chart viability functional). For an encoding $`\mathcal{E}`$ and a point $`x\in X`$, define a chart viability score
``` math
\mathcal{V}_{\mathcal{E}}(x) \in \mathbb{R}
```
as any scalar functional such that:

1.  $`\mathcal{V}_{\mathcal{E}}(x)>0`$ implies $`x\in A_{\mathcal{E}}`$ and all stated inequality contracts of $`\mathcal{E}`$ hold at $`x`$;

2.  $`\mathcal{V}_{\mathcal{E}}(x)\le 0`$ implies at least one contract of $`\mathcal{E}`$ fails at $`x`$.

</div>

<div class="remark">

*Remark 62*. $`\mathcal{V}_{\mathcal{E}}`$ is not unique; it is a diagnostic that packages the inequality contracts of $`\mathcal{E}`$ into a single scalar.

</div>

<div class="definition">

**Definition 63** (Maximal viability). Define the maximal viability at $`x`$ by
``` math
\mathcal{V}^\ast(x) := \sup_{\mathcal{E}\in \mathrm{Enc}(x)} \mathcal{V}_{\mathcal{E}}(x),
```
with the convention $`\mathcal{V}^\ast(x)=-\infty`$ if $`\mathrm{Enc}(x)=\varnothing`$.

</div>

<div class="remark">

*Remark 64*. $`\mathcal{V}^\ast(x)`$ measures the best available reduced description at $`x`$. The encoding boundary set $`\partial X_{\mathrm{enc}}`$ corresponds to collapse of $`\mathcal{V}^\ast`$ to nonpositivity in any neighborhood representation.

</div>

## The overlap nerve of the atlas

We now define a global topological summary of chart overlap.

<div class="definition">

**Definition 65** (Overlap relation). Two encodings $`\mathcal{E}_i=(A_i,\dots)`$ and $`\mathcal{E}_j=(A_j,\dots)`$ overlap if
``` math
A_i\cap A_j \neq \varnothing
```
and there exists a re-encoding morphism on the overlap in $`\mathbf{AdmEnc}/\!\sim`$.

</div>

<div class="definition">

**Definition 66** (Atlas nerve). Let $`\{\mathcal{E}_\alpha\}`$ be a chosen family of encodings. The nerve $`\mathcal{N}`$ is the simplicial complex whose:

- vertices are encodings $`\mathcal{E}_\alpha`$;

- a $`k`$-simplex $`(\mathcal{E}_{\alpha_0},\dots,\mathcal{E}_{\alpha_k})`$ exists iff $`\bigcap_{i=0}^k A_{\alpha_i}\neq\varnothing`$ and transition morphisms are controlled on that intersection.

</div>

<div class="remark">

*Remark 67*. Holes or obstruction cycles in $`\mathcal{N}`$ represent failures of global gluing and encode barrier structure at the atlas level.

</div>

## Universal reduced relation

Finite admissibility forbids a global single-valued reduced evolution on $`Y`$. The correct global object is a relation.

<div class="definition">

**Definition 68** (Universal reduced relation). Define the universal reduced relation $`\mathcal{R}\subset Y\times Y`$ by
``` math
\mathcal{R} := \{(y,y')\in Y\times Y \mid \exists x\in X \text{ such that } y=P(x),\ y'=P(\Phi_\tau(x))\}.
```

</div>

<div class="remark">

*Remark 69*. $`\mathcal{R}`$ is always well-defined and global, even when no global reduced map exists. On an admissible domain $`A`$ with section $`S_A`$, $`\mathcal{R}`$ restricts to the graph of the single-valued reduced map $`T_A`$ on $`P(A)`$.

</div>

## Total-atlas summary

The total atlas consists of:

- the encoding fibration $`\pi:\mathbb{E}\to X`$ capturing all admissible encodings as fibers;

- the maximal viability field $`\mathcal{V}^\ast`$ diagnosing where any encoding is possible;

- the overlap nerve $`\mathcal{N}`$ summarizing gluing and obstruction structure;

- the universal reduced relation $`\mathcal{R}\subset Y\times Y`$ capturing global reduced transitions.

No single global encoding is asserted; instead the theory provides a global *chart-of-charts* object that makes admissibility limits explicit.

# Conclusion

Modal Triplet Theory is presented here as a conditional, non-self-sealing framework. It asserts no ontology and no universal effective law. Instead, it classifies when reduced descriptions exist, how they must relate, and why they necessarily fail beyond finite admissibility. All claims are local, tolerance-bounded, and structurally enforced by projection and contractive dynamics.

Any physical interpretation is an external assignment layered atop the mathematical structure developed herein.
