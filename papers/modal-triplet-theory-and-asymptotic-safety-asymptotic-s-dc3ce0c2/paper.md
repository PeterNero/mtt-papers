---
abstract: |
  This paper states the mathematically controlled relation currently available between Modal Triplet Theory and functional-renormalization-group asymptotic safety. An integrable bound on an effective-action flow gives a Banach-space ultraviolet endpoint with an explicit tail estimate, but the bound must be proved for the selected four-dimensional flow and is not implied by an internal finite projector. Exact conjugacy between an MTT coarse-graining map and an FRG step map transports fixed points; approximate conjugacy transports only a residual unless a separate fixed-point theorem is supplied. Scheme changes are controlled by an endpoint-difference estimate, not by unrestricted scheme independence. Finally, a finite-dimensional unstable subspace follows when the linearized RG step is quasi-compact with essential spectral radius below one. These results define a rigorous conditional bridge. The selected MTT-to-FRG chart, physical regulator, four-dimensional damping estimate, and quasi-compactness certificate remain open source obligations.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 0732f728b13fe74c47b61984b70b05f9d32765d3d7056b962d9ca67b2bc9a4c7
paper_id: modal-triplet-theory-and-asymptotic-safety-asymptotic-s-dc3ce0c2
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and Asymptotic Safety:
  A Conditional FRG Conjugacy and Unstable-Subspace Theorem
zenodo_doi: 10.5281/zenodo.21665985
zenodo_record_id: 21665985
zenodo_url: "https://zenodo.org/records/21665985"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *Modal Triplet Theory and Asymptotic Safety: Asymptotic Safety as the Controlled FRG Shadow of the Coherent-Sector UV Endpoint*.

The earlier endpoint, scheme, and unstable-direction claims used assumptions that were not separated from conclusions. In particular, compactness of one summand did not control the essential spectrum of the full linearization.

Endpoint convergence, exact and approximate conjugacy, scheme variation, and quasi-compact unstable-subspace control are now separate theorems with explicit hypotheses.

Gaussian-integrable flow bounds imply a UV endpoint and tail bound; exact conjugacies transport fixed points and linearized spectra.

MTT does not yet select the physical FRG chart, regulator, dimensionless fixed functional, or quasi-compact linearization. The bridge is conditional rather than an established UV completion.

</div>

# Question and claim tier

Asymptotic safety asks whether a renormalization-group flow for dimensionless gravitational couplings approaches a non-Gaussian fixed point with finitely many ultraviolet-relevant directions. Functional renormalization group (FRG) calculations investigate this question through the effective average action $`\Gamma_k`$ and the Wetterich equation .

MTT uses a different starting language: coherent sectors, selected projectors, fixed-point maps, and geometry-to-operator transfers. A relation between the two frameworks therefore requires a map, not merely similar words. The strongest claim defended here is:
``` math
\text{selected MTT map}
\xleftrightarrow[\text{proved chart}]{\text{conjugacy}}
\text{FRG step map}.
```
All fixed-point consequences are conditional on that chart and on the analytic hypotheses below.

The paper does not claim that the present q79 internal finite Hessian is a four-dimensional FRG regulator. The internal-filter UV no-go theorem in the finite-filter paper shows why such an inference would fail without an intertwiner.

# Typed spaces and maps

Let $`\mathcal X`$ be a Banach space of dimensionless effective actions. The exact choice of norm is part of the model. A possible controlled setting is a bounded-geometry slab with analytic local functionals plus entire form factors, equipped with a majorant norm. The theorem statements below use only completeness and differentiability where declared.

Let
``` math
\mathcal R_b:\mathcal X\longrightarrow\mathcal X
```
be the time-$`\log b`$ step of an autonomous dimensionless FRG flow, for $`b>1`$. Let $`\mathcal U`$ be an MTT upper-state space and
``` math
\mathcal T_b:\mathcal U\longrightarrow\mathcal U
```
its selected coarse-graining step. A chart $`\mathcal C:\mathcal U\to\mathcal X`$ must specify how coherent variables become effective couplings. This chart is not supplied by identifying a coherent projector with an FRG cutoff.

## Dimensionful endpoints versus fixed points

A limit of dimensionful actions $`\Gamma_k`$ is not automatically an asymptotic-safety fixed point. Canonical rescaling must first produce dimensionless variables and an autonomous flow. This paper reserves $`\Gamma_\ast`$ for a fixed point of $`\mathcal R_b`$ and $`\Gamma_\infty`$ for a norm limit of a specified curve.

# What an integrable UV bound proves

<div id="thm:endpoint" class="theorem">

**Theorem 1** (Banach-space endpoint). *Let $`\Gamma:[k_0,\infty)\to\mathcal X`$ be locally absolutely continuous. If
``` math
\|\partial_k\Gamma_k\|_{\mathcal X}\leq g(k)
 \quad\text{for almost every }k,
 \qquad
 g\in L^1([k_0,\infty)),
```
then there is a unique $`\Gamma_\infty\in\mathcal X`$ such that
``` math
\Gamma_k\longrightarrow\Gamma_\infty,
 \qquad
 \|\Gamma_\infty-\Gamma_k\|_{\mathcal X}
 \leq\int_k^\infty g(s)\,ds.
```*

</div>

<div class="proof">

*Proof.* For $`K>k`$, absolute continuity gives
``` math
\|\Gamma_K-\Gamma_k\|_{\mathcal X}
 \leq\int_k^K\|\partial_s\Gamma_s\|_{\mathcal X}\,ds
 \leq\int_k^\infty g(s)\,ds.
```
The tail tends to zero, so $`\Gamma_k`$ is Cauchy. Completeness gives the limit, and $`K\to\infty`$ gives the bound. ◻

</div>

The commonly used Gaussian estimate
``` math
g(k)=Ck^m e^{-c\tau_0k^2},
 \qquad C,c,\tau_0>0,
```
satisfies the theorem. This proves an endpoint *if the estimate is available*. It does not prove the estimate from MTT geometry. In particular, an internal q79 spectral gap does not supply the required suppression of four-dimensional FRG shells.

<div id="prop:endpoint-fixed" class="proposition">

**Proposition 2** (When an endpoint is a fixed point). *Let $`x(t)`$ solve the autonomous Banach-space equation
``` math
\dot x=\beta(x)
```
with locally Lipschitz $`\beta`$. If $`x(t)\to x_\ast`$ as $`t\to\infty`$, then $`\beta(x_\ast)=0`$. Consequently the time-step map fixes $`x_\ast`$.*

</div>

<div class="proof">

*Proof.* If $`\beta(x_\ast)\neq0`$, Hahn–Banach gives a bounded linear functional $`\ell`$ with $`\ell(\beta(x_\ast))>0`$. By continuity, $`\ell(\beta(x(t)))`$ stays bounded below by a positive constant for all sufficiently large $`t`$. Then $`\ell(x(t))`$ cannot converge, a contradiction. ◻

</div>

The proposition explains why dimensionless autonomous variables are essential. It cannot be applied to a dimensionful endpoint before the rescaling and limiting flow are established.

# Exact and approximate conjugacy

<div id="thm:conjugacy" class="theorem">

**Theorem 3** (Conditional MTT–FRG conjugacy). *Suppose $`\mathcal C:\mathcal U\to\mathcal X`$ is injective and continuously differentiable near $`u_\ast`$, and
``` math
\begin{equation}
 \mathcal R_b\circ\mathcal C=\mathcal C\circ\mathcal T_b
 \label{eq:conjugacy}
\end{equation}
```
there. If $`\mathcal T_bu_\ast=u_\ast`$, then $`\Gamma_\ast=\mathcal C(u_\ast)`$ is an FRG fixed point. If $`D\mathcal C(u_\ast)`$ is a bounded linear isomorphism onto its image, then the restricted linearizations are similar:
``` math
D\mathcal R_b(\Gamma_\ast)|_{\operatorname{Ran}D\mathcal C}
 =
 D\mathcal C(u_\ast)\,D\mathcal T_b(u_\ast)\,
 D\mathcal C(u_\ast)^{-1}.
```
Thus their spectra and algebraic multiplicities agree on that image.*

</div>

<div class="proof">

*Proof.* Apply <a href="#eq:conjugacy" data-reference-type="eqref" data-reference="eq:conjugacy">[eq:conjugacy]</a> at $`u_\ast`$, then differentiate it and use the chain rule. ◻

</div>

This theorem is deliberately conditional. Conjugacy is the bridge; it is not a consequence of having fixed points on both sides.

<div id="prop:approx-conjugacy" class="proposition">

**Proposition 4** (Approximate conjugacy gives a residual). *Assume on a set $`V\subset\mathcal U`$ that
``` math
\|\mathcal R_b(\mathcal Cu)-\mathcal C(\mathcal T_bu)\|_{\mathcal X}\leq\varepsilon
```
and that $`\mathcal C`$ is $`L`$-Lipschitz there. Then
``` math
\|\mathcal R_b(\mathcal Cu)-\mathcal Cu\|_{\mathcal X}
 \leq \varepsilon+L\|\mathcal T_bu-u\|_{\mathcal U}.
```
In particular, an upper fixed point produces an FRG $`\varepsilon`$-residual, not necessarily a nearby FRG fixed point.*

</div>

<div class="proof">

*Proof.* Insert and subtract $`\mathcal C(\mathcal T_bu)`$ and use the triangle inequality. ◻

</div>

A nearby fixed point follows only after a separate contraction, degree, implicit-function, or validated-numerics theorem. This distinction is the main correction to the earlier bridge formulation.

# Scheme variation without overclaiming

Let $`\Gamma_k`$ and $`\Gamma'_k`$ be flows generated by two regulator choices in a common normed action space.

<div id="thm:scheme" class="theorem">

**Theorem 5** (Endpoint comparison). *Suppose both curves satisfy the hypotheses of <a href="#thm:endpoint" data-reference-type="ref+label" data-reference="thm:endpoint">1</a> and
``` math
h(k)=\|\partial_k\Gamma'_k-\partial_k\Gamma_k\|_{\mathcal X}
 \in L^1([k_0,\infty)).
```
Then
``` math
\|\Gamma'_\infty-\Gamma_\infty\|_{\mathcal X}
 \leq
 \|\Gamma'_{k_0}-\Gamma_{k_0}\|_{\mathcal X}
 \int_{k_0}^\infty h(k)\,dk.
```*

</div>

<div class="proof">

*Proof.* Integrate the difference of the two flows and take the norm and the limit. ◻

</div>

This is controlled regulator dependence. It is not scheme independence. A stronger statement that the endpoints are related by a bounded reparametrization requires that reparametrization to be constructed and its remainder bounded. Physical universality additionally concerns observables, not equality of off-shell effective actions.

# Finite relevant directions

The previous version wrote a linearization as a bounded plus compact operator and inferred finitely many unstable directions. That inference is invalid unless the noncompact part has controlled essential spectrum.

<div id="thm:quasicompact" class="theorem">

**Theorem 6** (Quasi-compact unstable subspace). *Let $`L:\mathcal X\to\mathcal X`$ be bounded and suppose its essential spectral radius satisfies
``` math
r_{\mathrm{ess}}(L)<1.
```
Then the part of $`\operatorname{spec}L`$ outside the closed unit disk consists of finitely many isolated eigenvalues, each of finite algebraic multiplicity. The associated Riesz projection
``` math
P_u=\frac{1}{2\pi i}\oint_\gamma(zI-L)^{-1}\,dz
```
has finite rank, where $`\gamma`$ encloses precisely that spectrum. Therefore the linear unstable subspace $`\operatorname{Ran}P_u`$ is finite-dimensional.*

</div>

<div class="proof">

*Proof.* This is the spectral decomposition theorem for quasi-compact operators: outside every circle of radius strictly larger than $`r_{\mathrm{ess}}(L)`$, the spectrum is a finite set of poles of the resolvent with finite-rank Riesz projections . ◻

</div>

If $`L=S+K`$ with $`K`$ compact, then
``` math
r_{\mathrm{ess}}(L)=r_{\mathrm{ess}}(S).
```
Compactness of $`K`$ therefore helps only after $`r_{\mathrm{ess}}(S)<1`$ is proved. A nonlinear local unstable manifold also requires a sufficiently smooth RG map and hyperbolicity; it does not follow from the linear statement alone.

# What SPT damping would have to establish

The conditional SPT route can now be stated as a finite checklist:

1.  select a four-dimensional, gauge-compatible TT or BV/BRST operator;

2.  derive its filter from the same MTT geometry rather than insert it as a regulator choice;

3.  prove the FRG shell estimate in the declared action norm;

4.  pass to autonomous dimensionless variables;

5.  construct the chart $`\mathcal C`$ and verify exact conjugacy or a certified defect;

6.  bound the essential spectral radius of the linearized step;

7.  compare regulator-independent observables, including errors.

The current corpus supplies useful ingredients but not this complete chain. The finite q79 Hessian is exact at its declared algebraic tier. The Euclidean TT/SPT paper gives a conditional filtered model. The constructive QG series provides finite-volume and finite-cutoff contracts. The continuum physical q79 HYM operator, four-dimensional source map, and nonperturbative QFT completion remain open.

# Status and interpretation

<div class="center">

| Claim | Status | Meaning |
|:---|:---|:---|
| Integrable flow gives endpoint | Exact conditional theorem | The bound is an input to <a href="#thm:endpoint" data-reference-type="ref+label" data-reference="thm:endpoint">1</a>. |
| Endpoint gives fixed point | Conditional | Requires autonomous dimensionless flow, as in <a href="#prop:endpoint-fixed" data-reference-type="ref+label" data-reference="prop:endpoint-fixed">2</a>. |
| Fixed points transfer across chart | Exact conditional theorem | Requires the conjugacy equation. |
| Approximate chart gives nearby fixed point | Not automatic | It gives only the residual in <a href="#prop:approx-conjugacy" data-reference-type="ref+label" data-reference="prop:approx-conjugacy">4</a>. |
| Scheme stability | Controlled comparison | <a href="#thm:scheme" data-reference-type="ref+label" data-reference="thm:scheme">5</a> bounds endpoint differences. |
| Finite relevant directions | Exact conditional theorem | Requires $`r_{\mathrm{ess}}<1`$, not smoothing language alone. |
| MTT proves asymptotic safety | Open | The selected chart and all physical analytic certificates are incomplete. |

</div>

# Discussion

This corrected bridge is useful even before it closes. It tells a future calculation exactly what would count as evidence. A numerically observed FRG fixed point is evidence about a truncation. An MTT fixed point is evidence about an upper map. They become the same mathematical result only after a chart intertwines the maps with controlled domain and error.

The quasi-compactness criterion similarly sharpens “finite predictivity.” Smoothing of one shell contribution does not settle the essential spectrum of the full RG derivative. Proving $`r_{\mathrm{ess}}<1`$, followed by a Riesz-projection computation, would give the desired finite-dimensional unstable sector in a form independent of basis rhetoric.

# Conclusion

MTT and asymptotic safety presently have a rigorous *conditional* relationship. Integrable FRG flow bounds, exact conjugacy, controlled scheme variation, and quasi-compact linearization have precise consequences. None of those hypotheses is supplied merely by the existence of an internal coherent projector.

The next decisive result is a same-source construction of the four-dimensional FRG variables and step map from the selected q79 geometry, together with a verified shell bound and essential-spectrum estimate. Until then, asymptotic safety is a promising diagnostic corner of MTT, not a derived equivalence or completed UV theory.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The FRG conjugacy and unstable-subspace theorem are conditional on a supplied intertwiner. The open strict-upgrade ledger neither supplies that intertwiner nor proves asymptotic safety; it records an independent source-selection frontier.

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

D. F. Litim, “Optimized renormalization group flows,” *Physical Review D* **64** (2001), 105007.

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

P. Nero, *Modal Triplet Theory: Foundations*, current revised MTT paper corpus, 2026.

P. Nero, *Finite Coherent Filters in Modal Triplet Theory: Operator Types, Exact Kernels, and Sectoral Boundaries*, current revised MTT paper corpus, 2026.

P. Nero, *Modal Triplet Theory: Perturbative Coherent-Sector Quantum Gravity and the Heterotic UV-Completion Boundary*, current revised MTT paper corpus, 2026.

</div>
