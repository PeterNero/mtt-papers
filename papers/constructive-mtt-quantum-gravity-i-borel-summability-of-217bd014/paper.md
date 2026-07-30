---
abstract: |
  This paper separates three constructive questions: existence of the filtered Gaussian measure, Borel summability at a finite spectral cutoff, and removal of that cutoff for a selected gravitational interaction. On a bounded-geometry Euclidean domain, a positive proper-time gap makes the spectral proper-time (SPT) covariance trace class, not merely Hilbert–Schmidt. It therefore defines a centered Borel Gaussian measure on the stated TT Hilbert space and has almost-sure Sobolev regularity of every finite order. We then prove ordinary Borel summability for finite-dimensional nonnegative quartic interactions and give an exact Borel–Laplace representation on the positive coupling ray. Finally, we prove a sufficient weighted-Borel convergence criterion for cutoff removal. These results do not establish Borel summability of the TT-expanded Einstein–Hilbert action: its sectorial stability, a selected interaction and filter, cutoff-uniform constructive bounds, and convergence of the Borel transforms remain separate obligations. The result is a rigorous finite-volume constructive core and a precise input contract for the BRST/BV successor, rather than a nonperturbative construction of MTT gravity.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 4717ea70ea72ae3ccae251b0b40452eb4c110548e717d214ef4b34fd52d6bdff
paper_id: constructive-mtt-quantum-gravity-i-borel-summability-of-217bd014
release_state: zenodo_released
released_version: v2
title: |
  Constructive MTT Quantum Gravity I:
  Finite-Volume SPT Gaussian Control and a Conditional Borel-Summability Contract
zenodo_doi: 10.5281/zenodo.21665952
zenodo_record_id: 21665952
zenodo_url: "https://zenodo.org/records/21665952"
---

# Version 2 Revision Note

Supersedes:
Constructive MTT Quantum Gravity I, first release.

Reason:
The Gaussian measure, finite-cutoff Borel theorem, and continuum interacting-gravity limit had been conflated.

Resolution:
The three levels are separated and each theorem is stated with its own cutoff, positivity, and convergence hypotheses.

Retained result:
The finite-volume SPT covariance is trace class, the finite-dimensional nonnegative quartic model is Borel summable, and a weighted criterion controls a possible cutoff limit.

Remaining boundary:
The selected gravity interaction, sectorial stability, cutoff-uniform bounds, and continuum Borel transform remain open.

# Correction and scope

The first version claimed a full constructive definition of an SPT-filtered TT gravitational sector. Its smoothing estimate was useful, but the proof crossed four logical gaps. Hilbert–Schmidt covariance was used as though it automatically defined a Gaussian measure on the same Hilbert space; a lower stability bound was used as an upper bound on the complex interaction; a loop-vertex expansion (LVE) was invoked without constructing the required intermediate-field/resolvent representation; and uniform estimates were treated as convergence when the spectral cutoff was removed.

This version proves only what follows from declared hypotheses. Its hierarchy is
``` math
\begin{align*}
\boxed{\text{SPT trace class}}
&\Longrightarrow \boxed{\text{Gaussian TT model}}\\
&\Longrightarrow \boxed{\text{finite-cutoff Borel theorem for a stable class}}\\
&\Longrightarrow \boxed{\text{conditional cutoff-removal contract}}.
\end{align*}
```
The final arrow to a physical gravitational theory is not asserted. In particular, an SPT filter is treated here as a regulator/model datum until MTT geometry selects its spectral function and proper-time scale.

## Reader orientation and the central picture

The paper studies three different limits, and they should not be blended. The first is an infinite-dimensional Gaussian measure at fixed bounded volume. The second is an interacting integral after only finitely many eigenmodes have been retained. The third is the limit in which that spectral cutoff is removed. Sections 2 and 3 close the first problem, Section 4 closes a deliberately restricted version of the second, and Section 5 states a sufficient condition for the third. Section 6 then lists the extra gates needed before any of this becomes a quantum-gravity construction.

In plain language, the SPT factor acts like a very strong high-frequency sieve. If $`L e_j=\lambda_j e_j`$, the variance of the $`j`$th Gaussian coordinate is
``` math
c_j=\frac{f(\lambda_j)}{\lambda_j+m^2}
 \leq
 \frac{\mu([\tau_0,\infty))e^{-\tau_0\lambda_j}}
      {\lambda_j+m^2}.
```
The exponential tail makes the sum of all coordinate variances finite on bounded volume. That fact constructs the free Gaussian measure. It does not decide which nonlinear gravitational interaction to integrate, whether that interaction is stable, or whether the cutoff sequence converges.

# Finite-volume spectral setting

Let $`\Omega`$ be a compact four-dimensional Riemannian manifold with boundary, or a bounded smooth domain equipped with fixed elliptic boundary conditions. Let $`E_{\mathrm{TT}}\to\Omega`$ be a finite-rank real bundle and let
``` math
L:D(L)\subset\mathcal{H}\longrightarrow\mathcal{H},\qquad
 \mathcal{H}=L^2(\Omega;E_{\mathrm{TT}}),
```
be nonnegative, self-adjoint, elliptic and of Laplace type. Thus $`L`$ has compact resolvent. Write its eigenvalues with multiplicity as $`0\leq\lambda_1\leq\lambda_2\leq\cdots`$ and assume the heat trace is finite for every $`t>0`$.

Let $`\mu`$ be a finite positive Borel measure supported in $`[\tau_0,\infty)`$ for some $`\tau_0>0`$, and put
``` math
f(\lambda)=\int_{\tau_0}^{\infty}e^{-t\lambda}\,d\mu(t),
 \qquad
 C=f(L)(L+m^2)^{-1},\qquad m^2>0.
```
The mass parameter is an infrared shift for this Euclidean finite-volume model. It is not identified here with a physical graviton mass.

<div id="lem:spt-bound" class="lemma">

**Lemma 1** (SPT spectral bound). *For every $`\lambda\geq0`$,
``` math
0\leq f(\lambda)\leq \mu([\tau_0,\infty))e^{-\tau_0\lambda}.
```
Consequently $`C`$ is positive, self-adjoint and bounded.*

</div>

<div class="proof">

*Proof.* Positivity follows from the positive representing measure. On its support, $`e^{-t\lambda}\leq e^{-\tau_0\lambda}`$, and integration gives the estimate. Functional calculus gives the operator assertions. ◻

</div>

# The corrected Gaussian theorem

<div id="thm:trace" class="theorem">

**Theorem 2** (Trace-class SPT covariance). *The covariance $`C`$ is trace class on $`\mathcal{H}`$, with
``` math
\operatorname{Tr}C\leq
 \frac{\mu([\tau_0,\infty))}{m^2}\operatorname{Tr}(e^{-\tau_0L})<\infty.
```
It therefore determines a unique centered Borel Gaussian probability measure $`\gamma_C`$ on $`\mathcal{H}`$.*

</div>

<div class="proof">

*Proof.* In the eigenbasis of $`L`$, the eigenvalues of $`C`$ are $`c_j=f(\lambda_j)/(\lambda_j+m^2)`$. Lemma <a href="#lem:spt-bound" data-reference-type="ref" data-reference="lem:spt-bound">1</a> gives
``` math
\sum_jc_j\leq
 \frac{\mu([\tau_0,\infty))}{m^2}\sum_je^{-\tau_0\lambda_j}<\infty.
```
Thus $`C`$ is positive trace class. The standard Hilbert-space Gaussian-measure criterion then gives the centered Borel measure with covariance $`C`$; the abstract-Wiener alternative is due to Gross . ◻

</div>

<div class="remark">

*Remark 3* (Why the correction matters). A positive Hilbert–Schmidt operator need not be trace class, so Hilbert–Schmidt control alone does not justify a Gaussian probability measure supported on $`\mathcal{H}`$. One may instead construct an abstract Wiener space, but its Banach support and the domain of the interaction must then be stated. The positive SPT gap avoids that ambiguity in the present bounded-domain model by giving trace class directly.

</div>

<div id="thm:sobolev" class="theorem">

**Theorem 4** (All finite Sobolev moments). *For every $`s\geq0`$,
``` math
\operatorname{Tr}\bigl((1+L)^sC\bigr)<\infty,\qquad
 \mathbb{E}_{\gamma_C}\|h\|_{H_L^s}^2
 =\operatorname{Tr}\bigl((1+L)^sC\bigr).
```
Hence $`\gamma_C(H_L^s)=1`$ for every finite $`s`$, and a sample belongs almost surely to $`\bigcap_{n\in\mathbb N}H_L^n`$.*

</div>

<div class="proof">

*Proof.* The trace is bounded by a constant times $`\sum_j(1+\lambda_j)^se^{-\tau_0\lambda_j}`$, which is finite because exponential decay dominates every power and the heat trace is finite. The Gaussian second-moment identity gives the equality. Intersecting the resulting full-measure sets over integer $`s`$ proves the last statement. ◻

</div>

This regularity makes many local polynomial functionals well-defined on the measure support. It does not prove that a particular gauge-fixed gravitational functional is stable, selected, or compatible with the constraints.

# Finite spectral cutoff

Let $`P_N`$ be the spectral projection onto the first $`N`$ eigenmodes of $`L`$ and set $`\mathcal{H}_N=P_N\mathcal{H}`$. The pushforward $`\gamma_N=(P_N)_*\gamma_C`$ is an ordinary $`N`$-dimensional Gaussian measure. Let $`V_N:\mathcal{H}_N\to[0,\infty)`$ be a real quartic polynomial satisfying
``` math
\begin{equation}
\label{eq:quartic-growth}
 0\leq V_N(x)\leq a_N(1+\|x\|^4).
\end{equation}
```
For a polynomial observable $`\mathcal O_N`$ define
``` math
Z_N(g)=\int e^{-gV_N(x)}\,d\gamma_N(x),\qquad
 G_{N,\mathcal O}(g)=\int \mathcal O_N(x)e^{-gV_N(x)}\,d\gamma_N(x).
```

<div id="lem:moments" class="lemma">

**Lemma 5** (Quartic Gaussian moment bound). *For each fixed $`N`$ and polynomial observable $`\mathcal O_N`$, there are constants $`A_N,K_N>0`$ such that for all $`n\geq0`$,
``` math
\int |\mathcal O_N(x)|V_N(x)^n\,d\gamma_N(x)
 \leq A_NK_N^n(2n)!.
```*

</div>

<div class="proof">

*Proof.* After a linear change of variables the finite-dimensional Gaussian is bounded by a constant times $`e^{-b_N\|x\|^2}dx`$. Equation <a href="#eq:quartic-growth" data-reference-type="eqref" data-reference="eq:quartic-growth">[eq:quartic-growth]</a> and the polynomial growth of $`\mathcal O_N`$ reduce the integral to radial Gaussian moments. Those moments are Gamma functions of $`2n`$ plus a fixed shift. Absorbing the fixed shift and low orders into $`A_N,K_N`$ gives the stated bound. ◻

</div>

<div id="thm:finite-borel" class="theorem">

**Theorem 6** (Finite-cutoff ordinary Borel summability). *For every fixed $`N`$, $`Z_N`$ and each $`G_{N,\mathcal O}`$ are analytic for $`\Re g>0`$ and have their formal perturbation series as Gevrey-one asymptotic expansions there. More precisely, the remainder after order $`n-1`$ obeys
``` math
|R_{N,n}(g)|\leq A_N(4K_N)^n n!\,|g|^n,
 \qquad \Re g\geq0.
```
They are therefore Borel summable in the Nevanlinna–Sokal sense on the positive coupling ray.*

</div>

<div class="proof">

*Proof.* For $`v\geq0`$, Taylor’s formula with integral remainder gives, when $`\Re g\geq0`$,
``` math
\left|e^{-gv}-\sum_{k=0}^{n-1}\frac{(-gv)^k}{k!}\right|
 \leq \frac{|g|^nv^n}{n!}.
```
Integrating this estimate and applying Lemma <a href="#lem:moments" data-reference-type="ref" data-reference="lem:moments">5</a> yields
``` math
|R_{N,n}(g)|\leq A_NK_N^n\frac{(2n)!}{n!}|g|^n
 \leq A_N(4K_N)^nn!|g|^n,
```
because $`(2n)!/(n!)^2\leq4^n`$. Dominated differentiation on compact subsets of $`\Re g>0`$ gives analyticity. The factorial remainder estimate on a Sokal disk is the Nevanlinna–Sokal criterion . ◻

</div>

<div id="cor:bessel" class="corollary">

**Corollary 7** (Exact positive-ray Borel–Laplace formula). *For $`g>0`$ the Borel transform of $`Z_N`$ may be represented by
``` math
\mathcal B_N(t)=
 \int J_0\!\left(2\sqrt{tV_N(x)}\right)d\gamma_N(x),\qquad t\geq0,
```
and
``` math
Z_N(g)=\frac1g\int_0^\infty e^{-t/g}\mathcal B_N(t)\,dt.
```*

</div>

<div class="proof">

*Proof.* Expanding $`J_0(2\sqrt{tv})=\sum_{n\geq0}(-tv)^n/(n!)^2`$ gives the Borel transform near the origin. For $`t,v\geq0`$, $`|J_0(2\sqrt{tv})|\leq1`$. Fubini’s theorem and the elementary Laplace identity
``` math
\frac1g\int_0^\infty e^{-t/g}J_0(2\sqrt{tv})\,dt=e^{-gv}
```
then prove the formula. ◻

</div>

The theorem deliberately uses a nonnegative quartic class. Generic finite truncations of the Einstein–Hilbert expansion need not be nonnegative, and higher polynomial degree generally changes the Gevrey order. They are therefore not included by the phrase local analytic interaction.

# What is needed to remove the cutoff

Let $`\mathcal B_N`$ denote Borel transforms on a common positive ray. Uniform factorial bounds alone do not imply that $`N\to\infty`$ exists: for example, $`F_N(g)=(-1)^Ng`$ has uniform Gevrey bounds but no pointwise limit.

<div id="thm:removal" class="theorem">

**Theorem 8** (Weighted-Borel cutoff removal). *Fix $`g_0>0`$. Suppose measurable Borel transforms $`\mathcal B_N`$ satisfy
``` math
\int_0^\infty e^{-t/g_0}|\mathcal B_N(t)-\mathcal B(t)|\,dt
 \longrightarrow0
```
for some $`\mathcal B`$. Then for every $`0<g\leq g_0`$,
``` math
F_N(g)=\frac1g\int_0^\infty e^{-t/g}\mathcal B_N(t)\,dt
 \longrightarrow
 F(g)=\frac1g\int_0^\infty e^{-t/g}\mathcal B(t)\,dt.
```
The convergence is uniform on each compact subinterval of $`(0,g_0]`$.*

</div>

<div class="proof">

*Proof.* For $`g\leq g_0`$, $`e^{-t/g}\leq e^{-t/g_0}`$. Hence
``` math
|F_N(g)-F(g)|\leq
 \frac1g\int_0^\infty e^{-t/g_0}
 |\mathcal B_N(t)-\mathcal B(t)|\,dt.
```
On $`g\in[g_1,g_0]`$ the prefactor is bounded by $`1/g_1`$, proving both claims. ◻

</div>

This theorem identifies the missing object. One must construct a common Borel plane and prove weighted convergence, or a stronger sufficient condition, for the actual cutoff sequence. Termwise convergence on a small disk plus uniform local bounds is not by itself enough to control the Laplace tail.

# Constructive gravity contract

For an SPT-filtered TT model to qualify as a nonperturbative gravitational construction, the following gates must all be discharged:

1.  **Measure gate.** A trace-class covariance on the declared Hilbert space, or a fully specified abstract Wiener support. Theorem <a href="#thm:trace" data-reference-type="ref" data-reference="thm:trace">2</a> closes this gate for the bounded-domain SPT covariance used here.

2.  **Interaction gate.** A selected gauge-fixed or reduced interaction that is measurable on that support. The finite quartic class is a model class, not the Einstein–Hilbert interaction.

3.  **Stability gate.** Sectorial coercivity or a valid contour deformation for the selected interaction. A real lower bound cannot be reused as a complex upper bound.

4.  **Constructive gate.** An actual forest/LVE, cluster expansion, or another method producing the required uniform remainder estimates. Naming BKAR   does not construct the corresponding resolvents and determinant bounds.

5.  **Removal gate.** Cutoff-uniform control strong enough to imply convergence, such as Theorem <a href="#thm:removal" data-reference-type="ref" data-reference="thm:removal">8</a>.

6.  **Physical gate.** BRST/BV compatibility, a physical-state construction, Lorentzian interpretation, and agreement with the selected low-energy gravitational action.

Constructive MTT Quantum Gravity II now begins at the last gate: it gives exact finite-cutoff BRST chain criteria and conditional Ward and reconstruction theorems, but it does not manufacture the measure, quantum master equation, or cutoff removal left open here.

# Relation to current MTT results

The present theorems are compatible with, but logically distinct from, the current MTT gravity ledger. The finite $`q=79`$ TT operator and the conditional two-derivative TEGR/Einstein tensor shape concern the selected classical/effective operator. Standard low-energy quantum-GR amplitudes may be imported at EFT parity once their assumptions are declared. None of those results selects the SPT proper-time measure $`\mu`$, proves that the full gravitational interaction lies in the stable quartic class, or supplies the weighted Borel limit in Theorem <a href="#thm:removal" data-reference-type="ref" data-reference="thm:removal">8</a>.

The Gaussian damping also must not be read as a positive Källén–Lehmann representation in the same momentum variable. A nonzero positive spectral measure has a $`1/p^2`$-type large-momentum tail and cannot simultaneously produce permanent Gaussian decay. Here the damping is explicitly a Euclidean spectral regulator/model datum, not a proof of spectral positivity or UV-complete quantum gravity.

# Version delta

Relative to version 1, this successor:

- replaces the insufficient Hilbert–Schmidt measure claim by the trace-class theorem and states the abstract-Wiener alternative;

- removes the unsupported generic LVE and full TT-gravity Borel theorem;

- proves a finite-cutoff theorem for an explicit stable quartic class;

- removes the false assertion that small coupling changes concentration of the fixed base Gaussian measure;

- replaces the claim that uniform estimates imply a limit by the weighted-Borel convergence criterion of Theorem <a href="#thm:removal" data-reference-type="ref" data-reference="thm:removal">8</a>;

- distinguishes a useful SPT regulator from a filter selected by MTT geometry; and

- records the exact interface to the corrected BRST/BV successor.

# Conclusion

The positive proper-time gap yields a strong and rigorous result: on bounded volume, the SPT covariance is trace class and defines a smooth Gaussian TT model. Stable quartic finite-mode interactions have ordinary Borel-summable expansions, with an explicit positive-ray Borel transform. What remains is no longer hidden inside the word constructive: one must select the gravitational interaction and filter, prove sectorial stability and cutoff-uniform constructive estimates, establish a convergent Borel limit, and then pass the BRST/BV physical-state gates. Until those steps are supplied, this paper is a finite-volume constructive foundation and test contract, not a completed nonperturbative theory of gravity.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The finite-volume Gaussian construction and conditional Borel contract are local analytic results. The open strict-upgrade ledger neither proves cutoff removal nor selects a gravitational interaction; it records an independent source-level frontier.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99 L. Gross, *Abstract Wiener spaces*, in *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability*, vol. 2, 31–42 (1967).

A. D. Sokal, *An improvement of Watson’s theorem on Borel summability*, *Journal of Mathematical Physics* **21**, 261–263 (1980), doi:10.1063/1.524408.

D. C. Brydges and T. Kennedy, *Mayer expansions and the Hamilton–Jacobi equation*, *Journal of Statistical Physics* **48**, 19–49 (1987).

A. Abdesselam and V. Rivasseau, *Trees, forests and jungles: a botanical garden for cluster expansions*, in *Constructive Physics*, Lecture Notes in Physics **446**, 7–36 (1995).

K. Osterwalder and R. Schrader, *Axioms for Euclidean Green’s functions*, *Communications in Mathematical Physics* **31**, 83–112 (1973).

</div>
