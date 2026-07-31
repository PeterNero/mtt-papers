---
author:
- Peter Nero
current_version: v2
date: July 2026, Version 2
generated_from_main_tex_sha256: 25b4b7e0707e660d25b4e57cc80d4d91004c23e8d2f59567bed316e5cb44574d
paper_id: why-general-relativity-and-string-theory-are-the-same-a-98920533
release_state: zenodo_released
released_version: v2
title: |
  **Worldsheet and Spacetime Consistency as a Conditional Diagnostic Square:**
  Sigma-model beta functions, target-space equations, and the MTT source contract
zenodo_doi: 10.5281/zenodo.21719524
zenodo_record_id: 21719524
zenodo_url: "https://zenodo.org/records/21719524"
---

<div class="center">

**Abstract**

</div>

> Perturbative string theory supplies a precise relation between two-dimensional Weyl consistency and target-space field equations. At leading order the metric beta function contains the Ricci tensor, but the complete statement also involves the antisymmetric tensor, dilaton, renormalization scheme, higher powers of alpha-prime, string loops, and the domain of the worldsheet theory. It is therefore inaccurate to identify General Relativity and string theory as theories, or to infer their equivalence merely because their consistency equations meet in a low-energy corner. This paper gives the correct technical bridge and states what Modal Triplet Theory (MTT) would have to add. We define a worldsheet diagnostic, a target-space Euler–Lagrange diagnostic, two source encodings, and an explicit comparison operator. A controlled diagnostic-square theorem proves exact and approximate transfer of solutions when these maps intertwine and the comparison operator has the required inverse estimate. A counterexample shows that coincident fixed points alone do not establish this bridge. The standard sigma-model result supplies a perturbative instance after field redefinitions; it does not supply an upstream MTT source. We finish with a twelve-row same-source contract and a separate error ledger. Current q79 work provides five rows, partially provides two, and leaves five open. Accordingly, the paper establishes a rigorous conditional comparison framework, not a derivation of string theory, pure Einstein gravity, or their ontological identity from MTT.

# Version 2 Revision Note

<div class="description">

Version 1.0, released in January 2026.

The previous version identified GR and string theory as the same constraint, assumed that an MTT proper-time flow was conjugate to worldsheet RG, identified $`\alpha'`$ with an inverse spectral gap, and treated common fixed points as a proof of equivalence.

Version 2 separates the established perturbative worldsheet-to-target result from the proposed MTT common-source explanation. It proves a typed conditional diagnostic-square theorem, gives a no-go counterexample, and records every approximation and source obligation.

The central intuition survives in narrower form: worldsheet and spacetime equations may be two controlled diagnostics of one selected background record.

MTT has not yet supplied one selected q79 physical visible–hidden worldsheet theory, upper action, and comparison map that closes the twelve-row contract.

</div>

# What the familiar statement actually means

The phrase “GR falls out of string theory” compresses several distinct claims. Perturbative string theory starts with a two-dimensional quantum field theory whose couplings are target-space fields. Quantum Weyl invariance constrains those couplings. In a perturbative scheme, the constraints agree with equations derived from a target-space effective action. In a further low-energy and field-content reduction, part of that action resembles Einstein gravity.

This chain is important, but it does not say that the theories are identical. Their variables, observables, dimensions, quantization data, and regimes are different. The careful statement is:
``` math
\begin{array}{c}
\text{worldsheet Weyl-anomaly coefficients: }\bar\beta^i=0\\[0.35em]
\Updownarrow\quad\text{at a declared order, scheme, and field content}\quad\\[0.35em]
\text{target-space equations: }\delta S_{\mathrm{eff}}/\delta\varphi^i=0 .
\end{array}
```
The arrow concerns diagnostics on a shared background-coupling space. It is not an identity between complete theories.

## Three levels that must not be conflated

<div class="description">

A perturbative equivalence between Weyl-anomaly coefficients and target effective equations, modulo field redefinitions and at a stated order.

A proof that both diagnostics are images of one declared upper source under explicit maps.

A proof that the upper source, branch, action, normalizations, and physical state are selected without importing the desired lower solution.

</div>

This paper formalizes the second level conditionally. It neither reproves all of the first nor claims the third.

# The standard worldsheet-to-target bridge

## Worldsheet data

For a bosonic background record
``` math
\varphi=(g_{\mu\nu},B_{\mu\nu},\Phi,\ldots)
```
on a target $`Y`$, the Euclidean sigma-model action contains
``` math
\begin{align}
S_\Sigma[X;\varphi]
={}&\frac{1}{4\pi\alpha'}\int_\Sigma
\sqrt{h}\,h^{ab}g_{\mu\nu}(X)
\partial_aX^\mu\partial_bX^\nu\,d^2\sigma \nonumber\\
&+\frac{i}{4\pi\alpha'}\int_\Sigma
\epsilon^{ab}B_{\mu\nu}(X)
\partial_aX^\mu\partial_bX^\nu\,d^2\sigma
+\frac{1}{4\pi}\int_\Sigma\sqrt h\,
R^{(2)}\Phi(X)\,d^2\sigma ,
\label{eq:sigma-action}
\end{align}
```
with convention-dependent normalizations. A complete superstring or heterotic model also needs worldsheet fermions, ghosts, spin structures, GSO data, gauge-bundle couplings, a measure, and global consistency.

At leading order in one common convention, the metric anomaly coefficient has the form
``` math
\begin{equation}
\bar\beta^g_{\mu\nu}
=\alpha'\left(
R_{\mu\nu}+2\nabla_\mu\nabla_\nu\Phi
-\frac14H_{\mu\rho\sigma}H_\nu{}^{\rho\sigma}
\right)+O(\alpha'^2),
\label{eq:metric-beta}
\end{equation}
```
where $`H=dB`$ is modified in heterotic theory by the appropriate Chern–Simons terms. The $`B`$-field and dilaton have their own anomaly coefficients. Thus $`\bar\beta^g=0`$ is not generally the vacuum Einstein equation.

## Target-space data

At string tree level and leading derivative order, the NS–NS part of a target effective action is schematically
``` math
\begin{equation}
S_{\mathrm{eff}}
=\frac{1}{2\kappa^2}\int_Y
\sqrt{-g}\,e^{-2\Phi}
\left[
R+4|\nabla\Phi|^2-\frac1{12}|H|^2+O(\alpha')
\right]d^Dx .
\label{eq:effective-action}
\end{equation}
```
Gauge, fermion, source, compactification, and loop terms must be added for the intended string. After compatible field redefinitions, the Euler–Lagrange equations of <a href="#eq:effective-action" data-reference-type="eqref" data-reference="eq:effective-action">[eq:effective-action]</a> agree with the worldsheet Weyl conditions at the calculated order .

Vacuum Einstein gravity appears only after further restrictions, for example constant dilaton, vanishing flux and sources, suitable dimension reduction, and neglect of higher-derivative and loop effects. These are hypotheses, not consequences of writing down <a href="#eq:sigma-action" data-reference-type="eqref" data-reference="eq:sigma-action">[eq:sigma-action]</a>.

## Scheme and field-redefinition dependence

Beta functions are coordinates on a space of couplings. Local field redefinitions change their components and change the representative effective action while preserving the appropriate on-shell physics. Accordingly, comparison must either fix a common scheme or include the field-redefinition map. Equality of two unlabelled formulae is not a scheme-independent theorem.

# A typed diagnostic square

## Objects and maps

Let $`\mathcal{U}`$ be a declared upper-source space. Let $`\mathcal{C}_{\mathrm{ws}}`$ be the space of complete worldsheet coupling records and $`\mathcal{C}_{\mathrm{st}}`$ the space of target effective-field records. Encoding maps
``` math
E_{\mathrm{ws}}:\mathcal{U}\to\mathcal{C}_{\mathrm{ws}},
\qquad
E_{\mathrm{st}}:\mathcal{U}\to\mathcal{C}_{\mathrm{st}}
```
must be independently defined. They are not names for fitting the same lower data twice.

Let
``` math
D_{\mathrm{ws}}:\mathcal{C}_{\mathrm{ws}}\to\mathcal{B}_{\mathrm{ws}},
\qquad
D_{\mathrm{st}}:\mathcal{C}_{\mathrm{st}}\to\mathcal{B}_{\mathrm{st}}
```
denote the full Weyl-anomaly and target Euler–Lagrange diagnostics. The spaces $`\mathcal{B}_{\mathrm{ws}}`$ and $`\mathcal{B}_{\mathrm{st}}`$ carry declared norms on a domain $`\mathcal{U}_0\subseteq\mathcal{U}`$. A comparison family
``` math
J_u:\mathcal{B}_{\mathrm{st}}\to\mathcal{B}_{\mathrm{ws}}
```
includes conventions, field redefinitions, gauge quotients, and any dimensional reduction used in the comparison.

<div class="definition">

**Definition 1** (Controlled diagnostic square). The data above form a controlled diagnostic square on $`\mathcal{U}_0`$ when
``` math
\begin{equation}
D_{\mathrm{ws}}(E_{\mathrm{ws}}u)
=J_uD_{\mathrm{st}}(E_{\mathrm{st}}u)+r(u),
\qquad
\|r(u)\|_{\mathrm{ws}}\leq\varepsilon(u),
\label{eq:square}
\end{equation}
```
and $`J_u`$ is injective on the compared diagnostic subspace with
``` math
\|v\|_{\mathrm{st}}\leq M(u)\|J_uv\|_{\mathrm{ws}}.
```
The square is exact when $`r=0`$.

</div>

The inverse estimate matters. Without it, a small worldsheet residual can hide a large target residual in a poorly conditioned or discarded direction.

<div id="thm:square" class="theorem">

**Theorem 2** (Controlled worldsheet–spacetime diagnostic transfer). *Let the controlled diagnostic square hold at $`u\in\mathcal{U}_0`$. Then
``` math
\begin{equation}
\|D_{\mathrm{st}}(E_{\mathrm{st}}u)\|_{\mathrm{st}}
\leq M(u)\left(
\|D_{\mathrm{ws}}(E_{\mathrm{ws}}u)\|_{\mathrm{ws}}
+\varepsilon(u)\right).
\label{eq:target-bound}
\end{equation}
```
If the square is exact and $`J_u`$ is injective on the compared subspace, worldsheet consistency implies the compared target equations. If $`J_u`$ is also surjective and boundedly invertible on the full diagnostic spaces, the two zero conditions are equivalent. None of these conclusions identifies the complete theories.*

</div>

<div class="proof">

*Proof.* Rearranging <a href="#eq:square" data-reference-type="eqref" data-reference="eq:square">[eq:square]</a> gives
``` math
J_uD_{\mathrm{st}}(E_{\mathrm{st}}u)
=D_{\mathrm{ws}}(E_{\mathrm{ws}}u)-r(u).
```
Apply the inverse estimate and the triangle inequality to obtain <a href="#eq:target-bound" data-reference-type="eqref" data-reference="eq:target-bound">[eq:target-bound]</a>. For $`r=0`$, injectivity transfers a worldsheet zero to a target zero. Surjectivity and bounded invertibility give the reverse implication on the declared spaces. The theorem compares diagnostic values only, so it makes no statement about equality of states, observables, or quantizations. ◻

</div>

<div class="corollary">

**Corollary 3** (Perturbative string instance). *Suppose a fixed string model, renormalization scheme, field-redefinition map, and perturbative order $`N`$ give
``` math
D_{\mathrm{ws}}=J D_{\mathrm{st}}+O(\alpha'^{N+1})
```
on a controlled background family. Then Theorem <a href="#thm:square" data-reference-type="ref" data-reference="thm:square">2</a> transfers the residual with $`\varepsilon=O(\alpha'^{N+1})`$, together with whatever string-loop, compactification, and analytic errors are separately present.*

</div>

This corollary organizes the standard result. It does not prove that an MTT source emitted the string model.

# Why matching fixed points is insufficient

<div id="prop:no-go" class="proposition">

**Proposition 4** (Common-zero no-go). *Equality of the zero sets of two diagnostics does not imply a controlled diagnostic square with a uniformly invertible linear comparison.*

</div>

<div class="proof">

*Proof.* On $`\mathbb{R}`$, let $`D_1(x)=x`$ and $`D_2(x)=x^3`$. Both have zero set $`\{0\}`$. Any pointwise scalar comparison satisfying $`D_2(x)=J_xD_1(x)`$ for $`x\neq0`$ has $`J_x=x^2`$. Its inverse norm diverges as $`x\to0`$. Thus common fixed points do not provide the stability or residual transfer required by Theorem <a href="#thm:square" data-reference-type="ref" data-reference="thm:square">2</a>. ◻

</div>

This elementary example exposes the defect in an argument of the form “both flows have the same fixed point, therefore they encode the same constraint.” A second circular argument is to assume a conjugacy $`F_{\mathrm{ws}}=U^{-1}F_{\mathrm{st}}U`$ and then advertise fixed-point transfer as a derivation. Conjugacy does transfer fixed points, but the research task is to construct and verify $`U`$. Naming it does not do so.

# What MTT would add

MTT proposes an explanation upstream of the standard bridge: both lower diagnostics may descend from one selected source. That proposal becomes mathematical only after the maps in <a href="#eq:square" data-reference-type="eqref" data-reference="eq:square">[eq:square]</a> are built from the same source, with provenance.

## The same-source contract

<div class="center">

<div class="tabularx">

@L0.07X L0.27@ Row & Required object & Current q79 status
W1 & Time-oriented q79 target branch & Available
W2 & Fu–Yau charge and Green–Schwarz/Bianchi sector & Available
W3 & Visible curvature-level Green–Schwarz cancellation & Available at curvature tier
W4 & Critical heterotic central-charge balance & Available universally
W5 & q79 low-energy GR and quantum-EFT parity limit & Available at its declared tier
W6 & Global differential gerbe and full visible-cycle consistency & Open; finite representative only

</div>

<div class="tabularx">

@L0.07X L0.27@ Row & Required object & Current q79 status
W7 & All-orders-in-$`\alpha'`$ q79 target background & Open; present background is first order
W8 & Exact q79 heterotic $`(0,2)`$ SCFT or complete beta functions & Partial; base GLSM and local/topological data exist, but the physical bundle and IR SCFT do not
W9 & Modular-invariant q79 GSO partition function and factorization & Partial; finite torsion data exist, while analytic characters and GSO remain open
W10 & q79-specific string-field vertices and BV master action & Open
W11 & Tadpole, vacuum-shift, infrared, and soft-state completion & Open
W12 & All-genus convergence or a nonperturbative definition & Open

</div>

</div>

The count is five available, two partial, and five open. In the live research ledger, $`B.\mathrm{QG}.01`$ asks for all twelve rows on the same physical nonpullback visible–hidden bundle. $`B.\mathrm{ACTION}.01`$ separately asks for the selected upper differential or action whose automorphisms and descendants reproduce the lower structures. Neither blocker is closed by the theorem in this paper.

## Why a projector and a gap are not enough

A coherent projector can select a subspace, and a spectral gap can control leakage from it. Neither object alone determines a target manifold, worldsheet measure, BRST complex, anomaly coefficients, effective action, comparison map, or renormalization scheme. Likewise, proper-time representations and worldsheet Wilsonian RG are not automatically the same flow. To identify them one needs a proved intertwiner with domain and error control.

The formerly asserted relation
``` math
\alpha'\sim\lambda_*^{-1}
```
is therefore not used as an identity. $`\alpha'`$ is the string tension scale in the sigma model; $`\lambda_*`$ may be a spectral control scale in an MTT reduction. A selected source theorem could relate them, but dimensional compatibility and matching of one asymptotic order would still not determine all coefficients.

# The complete error ledger

A useful bridge reports errors by origin rather than hiding them in one symbol.

<div class="center">

| Source | Typical control | What failure means |
|:---|:---|:---|
| $`\alpha'`$ expansion | curvature and derivative bounds in string units | higher-derivative terms are not small |
| String loops | powers of $`g_s=e^\Phi`$ and genus estimates | tree-level target action is insufficient |
| Worldsheet analysis | anomaly, modular, GSO, factorization, IR SCFT | no complete perturbative string background |
| Scheme/redefinition | explicit local map and Jacobian bounds | component beta functions cannot be compared directly |
| Compactification | Kaluza–Klein scale, moduli, warping, sources | the lower-dimensional GR truncation is uncontrolled |
| MTT projection | leakage, domain, spectral and truncation estimates | upper-to-lower descent is uncontrolled |
| Diagnostic comparison | residual $`r`$ and inverse bound $`M`$ | lower zeros or small residuals do not transfer |
| Quantum/observable match | state, BRST/BV, renormalization, uncertainty | equation-level parity is not physical equivalence |

</div>

These errors need not scale together. In particular, a small projection error says nothing by itself about string loops or modular consistency.

# Interpretation and consequences

## What is genuinely unified

The standard string result already unifies a set of worldsheet and target-space consistency equations within one perturbative construction. The MTT proposal is stronger in a different direction: it seeks one preprojection object from which the worldsheet and spacetime records descend. If the twelve-row contract and Theorem <a href="#thm:square" data-reference-type="ref" data-reference="thm:square">2</a>’s hypotheses are realized from one selected q79 source, then the two diagnostics would be certified views of that source. This would explain their agreement without claiming that a two-dimensional QFT and a spacetime effective theory are the same mathematical object.

## What is not yet unified

The present framework does not derive:

- a complete physical q79 heterotic worldsheet;

- an exact $`(0,2)`$ IR SCFT or modular-invariant GSO sum;

- the nonperturbative string theory or all-genus completion;

- a selected upper MTT action;

- pure four-dimensional Einstein gravity without reduction hypotheses;

- equality of worldsheet and spacetime observables; or

- a unique physical vacuum or branch.

It also does not prove that all quantum gravity theories are shadows of one constraint. That may be a research program, but each proposed diagnostic square needs its own maps and certificate.

## Falsifiability

Once source maps are explicit, the bridge can fail in informative ways. The worldsheet record may violate modular invariance; the target equations may contain a component outside the range controlled by $`J`$; the inverse bound may diverge; the $`\alpha'`$ or loop expansion may cease to be small; or two purported descendants may have incompatible source hashes. Any of these failures blocks promotion. Agreement obtained only after adjusting the source to the desired lower equations is reconstruction, not prediction.

# Research program

The shortest rigorous path is:

1.  construct the physical q79 visible and hidden holomorphic bundles in one positive HYM chamber;

2.  close the global differential Green–Schwarz and gerbe data;

3.  construct the heterotic $`(0,2)`$ worldsheet theory, analytic characters, GSO projection, and factorization;

4.  derive its anomaly coefficients in a declared scheme;

5.  derive the target effective equations from the same source and at the same order;

6.  emit $`J`$, $`r`$, $`\varepsilon`$, and the inverse estimate $`M`$;

7.  compare states and observables only after the equation-level square is closed; and

8.  keep the all-genus or nonperturbative completion as a separate tier.

This order prevents a familiar loop: proving a formal transfer theorem again while the physical source rows remain absent. The theorem is now owned here. Future progress must fill a row or improve a bound.

# Conclusion

General Relativity and perturbative string theory are not the same theory. The accurate mathematical relation is a controlled correspondence between worldsheet Weyl diagnostics and target-space effective equations on a shared background record, at a declared perturbative order and scheme. Pure Einstein gravity is a further low-energy corner.

MTT offers a potentially deeper explanation only if one selected upper source emits both records and the comparison square. Theorem <a href="#thm:square" data-reference-type="ref" data-reference="thm:square">2</a> states exactly what that would prove and Proposition <a href="#prop:no-go" data-reference-type="ref" data-reference="prop:no-go">4</a> shows why common fixed points do not suffice. With five of twelve q79 worldsheet rows available, two partial, and five open, the bridge is a serious, well-typed program rather than a completed equivalence.

<div class="thebibliography">

99

D. Friedan, “Nonlinear models in $`2+\epsilon`$ dimensions,” *Physical Review Letters* **45** (1980), 1057–1060. <https://doi.org/10.1103/PhysRevLett.45.1057>

C. G. Callan, D. Friedan, E. J. Martinec, and M. J. Perry, “Strings in background fields,” *Nuclear Physics B* **262** (1985), 593–609. <https://doi.org/10.1016/0550-3213(85)90506-1>

C. M. Hull and P. K. Townsend, “String effective actions from sigma-model conformal anomalies,” *Nuclear Physics B* **301** (1988), 197–223. <https://doi.org/10.1016/0550-3213(88)90692-5>

R. R. Metsaev and A. A. Tseytlin, “Order $`\alpha'`$ (two-loop) equivalence of the string equations of motion and the sigma-model Weyl invariance conditions,” *Nuclear Physics B* **293** (1987), 385–419. <https://doi.org/10.1016/0550-3213(87)90077-0>

P. Nero, *A Projection-First Reframing of String Theory: Conditional Encodings, Worldsheet Gates, and the q79 Boundary*, Version 2, 2026.

P. Nero, *Modal Triplet Theory to the Hull–Strominger System: A Conditional Fixed-Point Correspondence*, Version 2, 2026.

</div>
