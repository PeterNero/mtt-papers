---
abstract: |
  Finite functional-renormalization-group truncations can reveal fixed-point structure, but a truncation fixed point is not automatically the shadow of an exact ultraviolet completion. This paper gives a validation framework for that inference. A contraction residual bounds the distance to an exact fixed point when the exact map is already known to be contractive. A finite truncation has its own fixed point only when an independent existence condition, such as invariant contraction or a verified degree argument, is supplied. If a lifted truncation fixed point has a certified defect relative to the exact map, its distance from the exact fixed point is bounded by that defect divided by the contraction margin. An additive-error Lipschitz inequality alone proves none of these conclusions. Applied to Modal Triplet Theory, the framework identifies the missing data: a selected map from coherent variables to FRG couplings, a physical regulator and scheme, and certified truncation defects. The paper therefore supplies a rigorous truncation diagnostic, not a proof that current asymptotic-safety truncations are MTT predictions.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: fc31e2c07d246f0217150f78a00aba3f45f492d7970a28741c26b04b585bb9d6
paper_id: asymptotic-safety-as-a-truncation-shadow-of-a-coherent-05df2176
release_state: zenodo_released
released_version: v2
title: |
  Asymptotic-Safety Truncations as Conditional Shadows:
  Fixed-Point Residuals, Error Bounds, and Scheme Dependence
zenodo_doi: 10.5281/zenodo.21665946
zenodo_record_id: 21665946
zenodo_url: "https://zenodo.org/records/21665946"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *Asymptotic Safety as a Truncation Shadow of a Coherent-Sector UV Endpoint*.

The previous argument inferred approximate fixed points from an additive-error contraction and treated truncation convergence as if an exact fixed point and coupling map had already been established.

The paper now separates exact-map contraction, finite-map existence, lifted residuals, and scheme/truncation error. A counterexample records why the former inference fails.

Under a genuine contraction and a certified lifted defect, truncation fixed points obey an explicit a posteriori error bound.

No selected MTT-to-FRG coupling chart or certified physical truncation defect is currently available. Numerical FRG fixed points remain external diagnostics at this tier.

</div>

# Why a separate truncation paper is needed

The technical MTT–asymptotic-safety paper owns the conditional conjugacy and quasi-compact unstable-subspace theorems. This companion paper addresses a narrower question:
``` math
\begin{gathered}
\text{When does a fixed point of a finite FRG truncation}\\
\text{approximate a fixed point of an exact map?}
\end{gathered}
```

This question matters because practical asymptotic-safety calculations replace an infinite-dimensional effective action by finitely many couplings. Stability across larger truncations and regulator choices is valuable evidence , but the logical implication to an exact fixed functional requires error control.

# Exact map, truncation, and lift

Let $`\mathcal X`$ be a Banach space, $`\mathcal K\subset\mathcal X`$ a nonempty closed set, and
``` math
\mathcal T:\mathcal K\to\mathcal K
```
the exact dimensionless RG step. For each $`N`$, let $`X_N`$ be a finite-dimensional coupling space, with
``` math
\pi_N:\mathcal X\to X_N,\qquad
 \iota_N:X_N\to\mathcal X.
```
The finite map
``` math
\mathcal T_N:K_N\to K_N
```
need not equal $`\pi_N\mathcal T\iota_N`$. Gauge fixing, regulator choice, projection, closure assumptions, and numerical discretization can all contribute to the defect.

<div class="definition">

**Definition 1** (Lifted defect). For $`y\in K_N`$, define
``` math
d_N(y)=\|\mathcal T(\iota_Ny)-\iota_N\mathcal T_N(y)\|_{\mathcal X}.
```
This is the error relevant to fixed-point transfer.

</div>

Convergence of individual couplings or visual stability of a plot is not a substitute for a bound on $`d_N`$ in a declared norm.

# Residual validation

<div id="thm:residual" class="theorem">

**Theorem 2** (A posteriori fixed-point bound). *Suppose $`\mathcal T:\mathcal K\to\mathcal K`$ is a contraction with constant $`0\leq q<1`$, and let $`x_\ast`$ be its unique fixed point. Then every $`x\in\mathcal K`$ satisfies
``` math
\|x-x_\ast\|_{\mathcal X}
 \leq
 \frac{\|\mathcal Tx-x\|_{\mathcal X}}{1-q}.
```*

</div>

<div class="proof">

*Proof.* Using $`\mathcal Tx_\ast=x_\ast`$,
``` math
\|x-x_\ast\|
 \leq\|x-\mathcal Tx\|+\|\mathcal Tx-\mathcal Tx_\ast\|
 \leq\|\mathcal Tx-x\|+q\|x-x_\ast\|.
```
Rearrange. ◻

</div>

The theorem is a validation result, not an existence result from a small residual. Existence and uniqueness came from the exact contraction hypothesis.

<div id="cor:shadow" class="corollary">

**Corollary 3** (Certified truncation shadow). *Assume the hypotheses of <a href="#thm:residual" data-reference-type="ref+label" data-reference="thm:residual">2</a>. If $`\mathcal T_Ny_N=y_N`$, $`\iota_Ny_N\in\mathcal K`$, and
``` math
d_N(y_N)\leq\varepsilon_N,
```
then
``` math
\|\iota_Ny_N-x_\ast\|_{\mathcal X}
 \leq\frac{\varepsilon_N}{1-q}.
```
Consequently, $`\varepsilon_N\to0`$ implies convergence of the lifted truncation fixed points to $`x_\ast`$.*

</div>

<div class="proof">

*Proof.* At a truncation fixed point,
``` math
\|\mathcal T(\iota_Ny_N)-\iota_Ny_N\|
 =
 \|\mathcal T(\iota_Ny_N)-\iota_N\mathcal T_Ny_N\|
 =d_N(y_N).
```
Apply <a href="#thm:residual" data-reference-type="ref+label" data-reference="thm:residual">2</a>. ◻

</div>

# The finite fixed point needs its own theorem

<div id="prop:finite-existence" class="proposition">

**Proposition 4** (Finite-map existence by contraction). *If $`K_N`$ is complete and $`\mathcal T_N:K_N\to K_N`$ is a contraction with constant $`q_N<1`$, then $`\mathcal T_N`$ has a unique fixed point $`y_N`$.*

</div>

This is one available route. In finite dimension, an invariant compact convex set and continuity permit Brouwer existence, but not uniqueness or the a posteriori error bound above. Interval Newton, Krawczyk, degree, or Conley-index methods can provide stronger computer-assisted certificates.

## Why additive-error contraction is insufficient

The inequality
``` math
\begin{equation}
 \|\mathcal T_Nx-\mathcal T_Ny\|
 \leq q\|x-y\|+\varepsilon,
 \qquad q<1,\quad\varepsilon>0,
 \label{eq:additive}
\end{equation}
```
does not make $`\mathcal T_N`$ a contraction.

<div class="example">

**Example 5** (No existence from <a href="#eq:additive" data-reference-type="eqref" data-reference="eq:additive">[eq:additive]</a>). Let $`K=\{0,1\}`$ with its usual metric and let $`T`$ exchange the two points. Then $`K`$ is complete, $`T:K\to K`$ has no fixed point, and
``` math
|Tx-Ty|\leq0\,|x-y|+1
```
for all $`x,y\in K`$. Thus <a href="#eq:additive" data-reference-type="eqref" data-reference="eq:additive">[eq:additive]</a> can hold with $`q=0`$ without a fixed point.

</div>

This is the precise failure in the earlier version. An additive defect can be useful after an exact or finite fixed point has been established, but it cannot replace the existence theorem.

# Perturbing an exact contraction

<div id="thm:perturbation" class="theorem">

**Theorem 6** (Fixed-point perturbation). *Let $`T,S:\mathcal K\to\mathcal K`$ be contractions, with $`T`$ having constant $`q<1`$, and fixed points $`x_T,x_S`$. If
``` math
\sup_{x\in\mathcal K}\|Sx-Tx\|\leq\varepsilon,
```
then
``` math
\|x_S-x_T\|\leq\frac{\varepsilon}{1-q}.
```*

</div>

<div class="proof">

*Proof.*
``` math
\|x_S-x_T\|
 \leq\|Sx_S-Tx_S\|+\|Tx_S-Tx_T\|
 \leq\varepsilon+q\|x_S-x_T\|.
```
 ◻

</div>

The theorem requires $`S`$ to possess a fixed point, here guaranteed by its own contraction property. Closeness to $`T`$ alone is not enough.

# Scheme and regulator dependence

An FRG truncation is specified by more than a list of operators. It includes:

- field parametrization and background split;

- gauge fixing and ghost sector;

- regulator shape $`R_k`$;

- projection prescriptions for beta functions;

- truncation basis and normalization conditions;

- spacetime domain and boundary conditions.

Two calculations can be compared by treating one step map as a perturbation of the other and applying <a href="#thm:perturbation" data-reference-type="ref+label" data-reference="thm:perturbation">6</a> when a common invariant domain and contraction estimate exist. Without those data, “scheme stability” means empirical robustness across the tested schemes, not a theorem of universal equality.

# Relevant directions and spectral error

Let $`L=D\mathcal T(x_\ast)`$ and $`L_N=D(\iota_N\mathcal T_N\pi_N)`$ at compatible points. Convergence of fixed points does not alone imply convergence of critical exponents. One needs an operator-norm or resolvent estimate and a spectral separation condition. For an isolated spectral cluster enclosed by a contour $`\gamma`$, the relevant comparison is between Riesz projectors
``` math
P=\frac{1}{2\pi i}\oint_\gamma(z-L)^{-1}\,dz,
 \qquad
 P_N=\frac{1}{2\pi i}\oint_\gamma(z-L_N)^{-1}\,dz.
```
If the resolvent perturbation is small uniformly on $`\gamma`$, standard spectral perturbation theory controls the cluster and its total algebraic multiplicity . Counting positive critical exponents in a finite matrix without such control does not prove the exact number of relevant directions.

# Application contract for MTT

For an MTT truncation to qualify under <a href="#cor:shadow" data-reference-type="ref+label" data-reference="cor:shadow">3</a>, the following objects must be emitted from one selected branch:

1.  an exact or controlled upper RG map $`\mathcal T`$;

2.  a chart from coherent geometric variables to FRG actions and couplings;

3.  a compatible finite basis and lift $`(\pi_N,\iota_N)`$;

4.  an invariant domain and a contraction or other existence certificate;

5.  a computable lifted defect $`d_N`$;

6.  a regulator, gauge, and normalization convention;

7.  a spectral error certificate for claimed relevant directions.

The present MTT corpus does not yet provide this packet. It has exact finite internal operators, conditional four-dimensional filters, and several finite-domain constructive results. Those are ingredients, not the selected FRG coupling map or truncation certificate.

# Status table

<div class="center">

| Statement | Status | Required input |
|:---|:---|:---|
| Residual-to-distance bound | Exact | Exact contraction and a residual. |
| Lifted truncation convergence | Exact conditional | Fixed points plus $`d_N\to0`$. |
| Finite fixed-point existence | Separate | Contraction, degree, or validated numerical theorem. |
| Additive-error contraction implies a fixed point | False | Counterexample given above. |
| Critical-exponent convergence | Conditional | Resolvent bound and isolated spectral cluster. |
| Current FRG fixed points are MTT shadows | Open | Selected coupling chart and defect certificate. |

</div>

# Discussion and conclusion

The phrase “truncation shadow” is justified only when there is something precise casting the shadow: an exact map, a lift, and a controlled defect. Under those conditions, <a href="#cor:shadow" data-reference-type="ref+label" data-reference="cor:shadow">3</a> gives a clean quantitative statement. Without them, a stable truncation fixed point remains meaningful FRG evidence but not an MTT derivation.

This correction does not weaken the research program. It turns a broad correspondence into a reproducible target. The next useful computation is not another unconstrained search for fixed-point coordinates. It is a same-source construction of the MTT-to-FRG chart and a certified residual for one explicitly declared truncation.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The truncation-residual and scheme-dependence results in this paper are analytic statements under displayed hypotheses. The mapped strict-upgrade ledger does not prove an exact ultraviolet completion; it records a separate open source-selection obligation.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

C. Wetterich, “Exact evolution equation for the effective potential,” *Physics Letters B* **301** (1993), 90–94.

M. Reuter, “Nonperturbative evolution equation for quantum gravity,” *Physical Review D* **57** (1998), 971–985.

M. Reuter and F. Saueressig, *Quantum Gravity and the Functional Renormalization Group*, Cambridge University Press, 2019.

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

P. Nero, *Modal Triplet Theory and Asymptotic Safety: A Conditional FRG Conjugacy and Unstable-Subspace Theorem*, current revised MTT paper corpus, 2026.

</div>
