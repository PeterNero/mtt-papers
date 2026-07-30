---
abstract: |
  This paper asks when Modal Triplet Theory (MTT) realizes a perturbative string background. A target metric, two-form, dilaton, and gauge connection are not yet a string theory: one must also supply a two-dimensional quantum field theory, its ghost and BRST systems, criticality, spin structures and GSO projection, modular amplitudes, sewing and factorization, anomaly and global $`B`$-field data, and an infrared prescription. We package these ingredients as a typed perturbative-string record and define a partial map from an upper MTT state to that record. The main theorem is conditional: if one selected MTT state emits every required row, the lower record is string-consistent at the declared order and genus, and the MTT observable map factors through the standard worldsheet amplitude map, then MTT realizes that perturbative string sector on the stated domain. The theorem is an exact encoding statement, not a derivation of string theory from saturation or projection alone. We also separate target-space beta-function equations from exact conformal invariance, cohomological anomaly cancellation from the differential Bianchi identity, central-charge arithmetic from model selection, and circle-spectrum symmetry from full quantum T-duality. The current selected $`q=79`$ heterotic program supplies five of twelve worldsheet rows and partially constructs two more. The physical non-pullback visible–hidden bundle, exact infrared $`(0,2)`$ SCFT, analytic GSO and modular characters, quantum BV data, tadpole control, and all-genus or nonperturbative completion remain open.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 67043e8ea77e1cbbab5458234cbd5c013ea9171c589ecfd2b9e680f81a20fc07
paper_id: modal-triplet-theory-from-mtt-to-string-theory-a-first-4b1100fc
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and Perturbative String Theory:
  A Conditional Encoding Contract and the $`q=79`$ Worldsheet Boundary
zenodo_doi: 10.5281/zenodo.21708018
zenodo_record_id: 21708018
zenodo_url: "https://zenodo.org/records/21708018"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1 and its claim that a bounded MTT projection had already produced the Polyakov/RNS theory, conformal consistency, Green–Schwarz anomaly cancellation, compactification, exact dualities, and ultraviolet finiteness.

The former argument moved directly from ten-dimensional target fields to a complete quantum worldsheet. It conflated bosonic and heterotic central-charge formulas, treated BRST nilpotence as synonymous with the leading target beta functions, replaced a differential Bianchi identity by equality of characteristic numbers, and assumed modular invariance in the very step where it was needed. It also imported withdrawn uniqueness and stabilization claims from adjacent MTT papers.

This revision defines the full lower string record and a typed MTT source map. It proves the resulting conditional realization theorem, states a fixed-order residual-transfer proposition, checks the standard heterotic central-charge arithmetic, and records the current twelve-row $`q=79`$ worldsheet cutset. T-duality, anomaly cancellation, fixed-genus ultraviolet inheritance, and target-space reduction are restricted to the hypotheses that actually support them.

The ten-dimensional fields $`(G,B,\Phi,A)`$, sigma-model pullbacks, fixed-order beta-function comparison, Green–Schwarz structure, heterotic compactification targets, and circle momentum–winding exchange remain useful parts of the proposed bridge when their missing quantum and global data are supplied.

MTT has not yet selected a complete perturbative worldsheet theory on the physical $`q=79`$ visible–hidden background. In the current research ledger, blocker B.QG.01 remains open and depends on the physical Hull–Strominger endpoint and the quantum BV/renormalized-transport layer.

</div>

# The corrected question

## Target fields are necessary but not sufficient

A conventional nonlinear sigma model starts with a map
``` math
X:\Sigma\longrightarrow M
```
and target couplings such as a metric $`G`$, a two-form $`B`$, and a dilaton $`\Phi`$. In a heterotic model one also needs left-moving gauge degrees of freedom and a gauge connection $`A`$. Pullback along $`X`$ then produces the familiar local couplings. This is an important bridge from target geometry to a worldsheet Lagrangian, but it does not determine the complete quantum theory.

The field content, chirality, current algebra, normalization, gauge fixing, ghost systems, physical state conditions, spin-structure sum, and renormalization prescription are additional choices. At higher genus one also needs a measure on moduli space, modular covariance, sewing and factorization, and treatment of degenerations. Global anomaly and gerbe data cannot be reconstructed from the local Lagrangian alone .

The corrected MTT question is therefore:

> Does one selected upper MTT state emit a complete, mutually compatible perturbative-string record, and does the MTT evaluation of observables factor through the standard worldsheet construction?

This question can be answered precisely. It is stronger than matching a few target fields and weaker than claiming a nonperturbative definition of string theory.

## Three claims that must not be merged

We distinguish the following levels.

<div class="description">

A map sends MTT variables or perturbations to worldsheet couplings. The companion proto-spinor paper owns a conditional quadratic version of this statement .

One complete, anomaly-free, modular and factorizing worldsheet record is emitted, and the declared MTT observables factor through its amplitude map. This is the conditional theorem of the present paper.

An MTT source, preparation, flow, or branch law chooses that record rather than another allowed record. Existence and consistency do not imply this selection step .

</div>

## Argument map

<a href="#sec:record" data-reference-type="ref+Label" data-reference="sec:record">2</a> defines the complete lower object. <a href="#sec:map" data-reference-type="ref+Label" data-reference="sec:map">3</a> states the typed MTT encoding contract. <a href="#sec:beta,sec:quantum-gates" data-reference-type="ref+Label" data-reference="sec:beta,sec:quantum-gates">[sec:beta,sec:quantum-gates]</a> separate target equations, central charge, BRST, anomaly, modularity, and duality. <a href="#sec:q79" data-reference-type="ref+Label" data-reference="sec:q79">7</a> audits the current selected $`q=79`$ branch. <a href="#sec:uv,sec:boundary" data-reference-type="ref+Label" data-reference="sec:uv,sec:boundary">[sec:uv,sec:boundary]</a> state exactly what fixed-genus ultraviolet inheritance would require and what remains open.

# The lower object to be realized

## Target and local worldsheet data

For definiteness, the main application is a closed oriented heterotic worldsheet. Other string theories require altered matter and projection rows, but the logical separation is the same.

<div id="def:string-record" class="definition">

**Definition 1** (Perturbative-string record). A perturbative-string record at a declared order $`N`$ in $`\alpha'`$, genus range $`\mathcal G`$, and external-state class $`\mathcal E`$ is a tuple
``` math
\mathfrak S=
(\mathfrak T,\mathfrak W,\mathfrak Q,\mathfrak P,
 \mathfrak A,\mathfrak M,\mathfrak I),
```
with the following typed rows.

1.  $`\mathfrak T`$ is target data: $`(M,G,B,\Phi,A,\nabla,\mathcal G_B)`$, including a global $`B`$-field or gerbe $`\mathcal G_B`$, a declared tangent connection $`\nabla`$, and all compactification and bundle data used by the model.

2.  $`\mathfrak W`$ specifies the two-dimensional fields, chiralities, current algebra, local action, couplings, boundary conditions, and normalization.

3.  $`\mathfrak Q`$ specifies gauge fixing, matter and ghost Hilbert or state spaces, the BRST operator, its domain, and the physical state cohomology.

4.  $`\mathfrak P`$ specifies spin structures, GSO or analogous projections, and any orbifold or discrete-torsion phases.

5.  $`\mathfrak A`$ certifies local and global gauge, gravitational, and worldsheet anomalies, the differential Bianchi identity, and the perturbative order of the target equations.

6.  $`\mathfrak M`$ supplies genus-$`g`$ integrands for $`g\in\mathcal G`$, their modular transformation law, the integration cycle or measure, and sewing and factorization on every relevant degeneration.

7.  $`\mathfrak I`$ supplies the tadpole, vacuum-shift, infrared, and soft prescription needed for the amplitudes in $`\mathcal E`$.

</div>

This definition does not demand an all-genus sum. A record may be complete for one fixed genus and multiplicity while an all-genus or nonperturbative completion remains open. The declared scope is part of the mathematical object.

## The local sigma-model row

For supplied target fields, the bosonic terms take the schematic form
``` math
\begin{align}
S_{\sigma}
={}&\frac{1}{4\pi\alpha'}\int_\Sigma
\sqrt{h}\,h^{ab}G_{MN}(X)\,
\partial_aX^M\partial_bX^N\,\mathrm d^2\sigma \nonumber\\
&+\frac{\mathrm i}{4\pi\alpha'}\int_\Sigma
\epsilon^{ab}B_{MN}(X)\,
\partial_aX^M\partial_bX^N\,\mathrm d^2\sigma
+\frac{1}{4\pi}\int_\Sigma
\sqrt{h}\,\Phi(X)R^{(2)}\,\mathrm d^2\sigma ,
\label{eq:sigma-action}
\end{align}
```
after choosing Euclidean conventions. A heterotic completion adds right-moving worldsheet fermions, left-moving gauge degrees of freedom, and their couplings. Gauge fixing adds the appropriate ghost systems.

Pullback explains how a supplied target tensor enters <a href="#eq:sigma-action" data-reference-type="ref+label" data-reference="eq:sigma-action">[eq:sigma-action]</a>. It does not select the worldsheet field content, prove quantum Weyl invariance, construct the GSO sum, or define the measure on moduli space. Consequently a bounded MTT projector can participate in an encoding map, but boundedness alone cannot produce the RNS or heterotic quantum theory.

## Compactification adds further rows

For a heterotic compactification on a complex threefold $`X`$, the target row must include visible and hidden holomorphic bundles and connections in one common stability chamber. In a torsional $`SU(3)`$-structure background, the Hull–Strominger equations include
``` math
\mathrm d(e^{-2\Phi}\omega^2)=0,\qquad
F^{0,2}=0,\qquad F\wedge\omega^2=0,\qquad
H=\mathrm i(\bar\partial-\partial)\omega,
```
together with a differential Green–Schwarz identity. Solving these target-space equations at first order in $`\alpha'`$ is not by itself an exact $`(0,2)`$ SCFT .

The companion Hull–Strominger paper gives the appropriate conditional fixed-point correspondence; the companion compactification audit records which older bundle examples fail . Those theorems are imported here rather than duplicated.

# The MTT encoding contract

## Typed source and evaluation maps

Let $`\mathcal U_{\mathrm{MTT}}`$ be a declared upper MTT configuration space. A string encoding is a partial typed map
``` math
\mathcal R_{\mathrm{str}}:
\mathcal U_{\mathrm{MTT}}\dashrightarrow\mathcal M_{\mathrm{str}},
```
where $`\mathcal M_{\mathrm{str}}`$ is the space of records in <a href="#def:string-record" data-reference-type="ref+label" data-reference="def:string-record">1</a>. “Typed” means that each lower field, bundle, connection, projection, character, and measure has an identified upper source and convention. Matching dimensions or abstractly isomorphic groups do not define this map.

For a selected scope $`(N,\mathcal G,\mathcal E)`$, let
``` math
\mathcal A_{\mathrm{ws}}:\mathcal M_{\mathrm{str}}\dashrightarrow\mathcal O_{\mathcal G,\mathcal E}
```
be the standard perturbative worldsheet evaluation map, and let
``` math
\mathcal A_{\mathrm{MTT}}:\mathcal U_{\mathrm{MTT}}\dashrightarrow\mathcal O_{\mathcal G,\mathcal E}
```
be the corresponding MTT evaluation. The required commuting relation is
``` math
\mathcal A_{\mathrm{MTT}}
=\mathcal A_{\mathrm{ws}}\circ\mathcal R_{\mathrm{str}}
\quad\text{on a declared domain }\mathcal U_0.
\label{eq:factorization}
```

<div id="def:mtt-realization" class="definition">

**Definition 2** (Complete MTT string realization). An upper state $`u_\ast\in\mathcal U_0`$ is a complete MTT realization of a perturbative string sector at scope $`(N,\mathcal G,\mathcal E)`$ if:

1.  $`\mathcal R_{\mathrm{str}}(u_\ast)`$ supplies every row of <a href="#def:string-record" data-reference-type="ref+label" data-reference="def:string-record">1</a>;

2.  those rows satisfy their standard compatibility, anomaly, BRST, modular, factorization, and infrared conditions at the declared scope;

3.  every approximation and field-redefinition convention is explicit; and

4.  <a href="#eq:factorization" data-reference-type="ref+label" data-reference="eq:factorization">[eq:factorization]</a> holds at $`u_\ast`$.

</div>

<div id="thm:string-realization" class="theorem">

**Theorem 3** (Conditional perturbative-string realization). *If $`u_\ast`$ satisfies <a href="#def:mtt-realization" data-reference-type="ref+label" data-reference="def:mtt-realization">2</a>, then $`\mathcal R_{\mathrm{str}}(u_\ast)`$ is a consistent perturbative-string record at scope $`(N,\mathcal G,\mathcal E)`$, and every observable in that scope obeys
``` math
\mathcal A_{\mathrm{MTT}}(u_\ast)
=\mathcal A_{\mathrm{ws}}\!\left(\mathcal R_{\mathrm{str}}(u_\ast)\right).
```*

</div>

<div class="proof">

*Proof.* The first three hypotheses put the emitted record in the domain of the standard amplitude map with a fixed approximation and infrared convention. The last hypothesis is exactly the displayed equality. The conclusion does not add an existence, uniqueness, selection, or all-genus assertion beyond the supplied record. ◻

</div>

<div class="remark">

*Remark 4* (Why a conditional theorem is useful). The theorem is not intended to hide the hard work in an assumption. It locates that work. A proposed MTT construction can now be tested row by row, and no target-space computation can silently stand in for a missing GSO, modular, BV, or infrared certificate.

</div>

## Relation to the proto-spinor bridge

The proto-spinor/worldsheet paper studies a different arrow. Its conditional quadratic bridge compares Hessians near one background:
``` math
L^\ast H_{\mathrm{ws}}L=H_{\mathrm{ps}}
```
on a selected tangent subspace, with a cubic remainder estimate . That theorem can provide a local component of $`\mathcal R_{\mathrm{str}}`$, but it does not emit the global record in <a href="#def:string-record" data-reference-type="ref+label" data-reference="def:string-record">1</a>. Conversely, the present theorem does not re-prove the local Hessian statement. The two papers have complementary ownership.

# Beta functions and target equations

## What the standard comparison says

Renormalization of a nonlinear sigma model produces beta functions on the space of target couplings. To leading order, in a common convention,
``` math
\begin{align}
\beta^G_{MN}
&=\alpha'\left(
R_{MN}-\frac14H_{MPQ}H_N{}^{PQ}
+2\nabla_M\nabla_N\Phi
\right)+O(\alpha'^2), \\
\beta^B_{MN}
&=\alpha'\left(
-\frac12\nabla^PH_{PMN}
+\nabla^P\Phi\,H_{PMN}
\right)+O(\alpha'^2),
\end{align}
```
with gauge and dilaton terms determined by the chosen string model and scheme. Vanishing Weyl-anomaly coefficients yields target field equations order by order, up to local field redefinitions .

This comparison has two important qualifications.

1.  A solution through order $`\alpha'^N`$ is not an all-orders fixed point and does not by itself construct an exact CFT.

2.  Beta functions, Weyl-anomaly coefficients, and target effective-action equations are related in a specified renormalization scheme; they are not literally the same coordinate-free object.

## Controlled residual transfer

<div id="prop:residual-transfer" class="proposition">

**Proposition 5** (Fixed-order residual transfer). *Let $`E_N(u)`$ be the vector of target effective-action residuals emitted by an MTT state $`u`$, and let $`\beta_N(u)`$ be the corresponding vector of worldsheet Weyl-anomaly coefficients through order $`\alpha'^N`$. Suppose on a neighborhood $`U`$ that
``` math
\beta_N(u)=K_N(u)E_N(u)+r_{N+1}(u),
```
where $`K_N(u)`$ is bounded by $`C_K`$ in the chosen norms and $`\|r_{N+1}(u)\|\le C_r|\alpha'|^{N+1}`$. Then
``` math
\|\beta_N(u)\|
\le C_K\|E_N(u)\|+C_r|\alpha'|^{N+1}
\qquad (u\in U).
```
In particular, an exact projected target solution through order $`N`$ implies only an $`O(\alpha'^{N+1})`$ Weyl-anomaly residual under these hypotheses.*

</div>

<div class="proof">

*Proof.* Take norms in the assumed relation and apply the operator-norm bound and the triangle inequality. ◻

</div>

The proposition is deliberately an error statement. To use it, MTT must emit the same target fields and scheme used by $`K_N`$, and the residual bound must include every active equation. It cannot promote a first-order Hull–Strominger solution to an exact infrared SCFT.

# Independent quantum consistency gates

## Criticality and ghosts

The central-charge check is exact for the standard free heterotic field content, but it is a consistency calculation rather than a derivation of that content.

<div id="lem:central-charge" class="lemma">

**Lemma 6** (Standard heterotic central-charge arithmetic). *For ten target coordinate bosons, sixteen units of left-moving gauge current central charge, ten right-moving Majorana fermions, and the standard reparametrization and superconformal ghosts,
``` math
c_L^{\mathrm{tot}}=(10+16)-26=0,\qquad
c_R^{\mathrm{tot}}=\left(10+\frac{10}{2}\right)-15=0.
```*

</div>

<div class="proof">

*Proof.* A free real boson contributes $`1`$, a free real Majorana fermion contributes $`1/2`$, the left-moving $`bc`$ ghosts contribute $`-26`$, and the combined right-moving $`bc`$ and $`\beta\gamma`$ ghosts contribute $`-15`$. Summing the stated standard field content gives the result . ◻

</div>

This calculation checks the critical bookkeeping once the heterotic matter and ghost systems have been chosen. It does not show that an MTT projection selects ten coordinates, the gauge current algebra, or the GSO projection.

## BRST and physical states

BRST nilpotence requires cancellation of the relevant quantum anomalies and a correctly defined operator on the gauge-fixed state space. Target beta-function equations are part of the consistency conditions for a background, but the slogan
``` math
\text{``BRST nilpotence''}\quad\Longleftrightarrow\quad\text{``leading
target beta functions vanish''}
```
is too coarse. One must specify the matter-plus-ghost theory, normal ordering, central charge, background, and perturbative order. The physical states are then identified by BRST cohomology, subject to the chosen projection and inner product.

## Spin structures and GSO

The GSO projection is not a sign appended after the target equations. It controls the physical spectrum, spacetime spin-statistics, tachyon removal, and modular consistency. At genus one and beyond, the spin-structure sum must transform correctly and be compatible with factorization. The original GSO construction supplies the standard supersymmetric example ; a selected $`q=79`$ model must still emit its own analytic characters and phases.

## Green–Schwarz and global B-field data

In a heterotic convention one writes
``` math
H=\mathrm dB-\frac{\alpha'}4
\bigl(\omega_3(A)-\omega_3(\nabla)\bigr),
\qquad
\mathrm dH=\frac{\alpha'}4
\left(\operatorname{tr}R_\nabla\wedge R_\nabla-\operatorname{tr}F\wedge F\right),
\label{eq:bianchi}
```
with any visible, hidden, and five-brane contributions made explicit. Green–Schwarz factorization is a ten-dimensional anomaly statement . A compactification additionally needs a differential representative satisfying <a href="#eq:bianchi" data-reference-type="ref+label" data-reference="eq:bianchi">[eq:bianchi]</a> and compatible global gerbe data.

Equality of integrals over all four-cycles establishes equality of the relevant de Rham cohomology classes under appropriate hypotheses. It does not make two chosen curvature four-forms equal pointwise, construct $`H`$, or trivialize a torsion differential-cohomology obstruction. Freed–Witten conditions and related global restrictions are likewise separate from local curvature arithmetic .

## Modularity and factorization

For a modular-invariant closed-string integrand, integration may be restricted to a fundamental domain of the torus modular group. The region that resembles arbitrarily short proper time in a point-particle representation is then identified with another region; the remaining boundary at large imaginary modulus is associated with degeneration and factorization, where infrared and tadpole issues can occur .

This mechanism cannot be invoked before modular invariance, the measure, spin-structure sum, and factorization have been established for the actual model. A finite set of modularly permuted labels is useful algebraic input, but it is not yet an analytic partition function.

# Duality: what the circle calculation proves

For a compact free boson on a circle, the zero-mode mass contribution is schematically
``` math
M^2_{\mathrm{zero}}
=\frac{n^2}{R^2}+\frac{w^2R^2}{\alpha'^2}.
```
It is invariant under
``` math
(n,w,R)\longmapsto(w,n,\alpha'/R).
```
This exact arithmetic is a valuable compatibility witness for momentum and winding exchange.

Full quantum T-duality contains more. In a nonlinear sigma model it requires an isometry or another specified duality structure, transformation of $`(G,B,\Phi)`$, the functional measure and dilaton shift, global and topological data, and compatibility with the projection and spectrum . Therefore an MTT shared-circle spectrum can encode the kinematic seed of T-duality without yet proving equality of two complete string backgrounds.

S-duality, holography, and an M-theory lift require additional nonperturbative or boundary data and are outside the theorem proved here. Their possible MTT encodings belong in separate papers with their own source maps; they are not consequences of <a href="#thm:string-realization" data-reference-type="ref+label" data-reference="thm:string-realization">3</a>.

# The selected q=79 worldsheet cutset

## Why this is the relevant branch

The current selected MTT route toward a heterotic string realization uses the time-oriented $`q=79/F`$ branch and a Fu–Yau-type non-Kähler compactification target. It is not the strict Calabi–Yau branch described in the companion paper . The exact finite arithmetic, Cech carrier, and projected HYM calculations give substantial support at their declared tiers, but only the worldsheet cutset decides whether they assemble into the record of <a href="#def:string-record" data-reference-type="ref+label" data-reference="def:string-record">1</a>.

<div id="tab:q79-available">

| Row | Required object | State | Current evidence or missing endpoint |
|:---|:---|:---|:---|
| W1 | Selected target branch | Available | Time-oriented $`q=79/F`$ representative. |
| W2 | Charge and Bianchi sector | Available | Fu–Yau/Mukai charge data and Green–Schwarz Bianchi sector at the declared topological and curvature tiers. |
| W3 | Visible local anomaly row | Available | Curvature-level visible Green–Schwarz cancellation. This is not the full global gerbe or physical visible–hidden bundle. |
| W4 | Critical central charge | Available | The universal heterotic arithmetic in <a href="#lem:central-charge" data-reference-type="ref+label" data-reference="lem:central-charge">6</a>. It checks standard field content rather than selecting it. |
| W5 | Low-energy limit | Available | The $`q=79`$ GR and quantum-EFT limit at the declared parity/controlled tier. It is not a worldsheet completion. |

Available rows in the current $`q=79`$ heterotic worldsheet contract. Availability is limited to the stated row and tier.

</div>

<div id="tab:q79-open">

| Row | Required object | State | Current evidence or missing endpoint |
|:---|:---|:---|:---|
| W6 | Global differential data | Open | Full Deligne gerbe, Freed–Witten restrictions, and differential class on the complete visible cycle set. |
| W7 | All-order target background | Open | The current flux construction is first order in $`\alpha'`$; an all-order background or a controlled exact alternative is absent. |
| W8 | Exact heterotic $`(0,2)`$ SCFT | Partial | K3 GLSM, local anomaly, topological clutching candidates, and related finite data exist. The physical non-pullback holomorphic visible–hidden bundle, HYM connection, differential Bianchi representative, GSO currents, and exact IR SCFT remain open. |
| W9 | Modular/GSO amplitudes | Partial | The finite $`F_3^2`$ torsion phase, seven modular seed orbits, and finite covariance are exact. Oscillator and gauge-current characters, spin-structure sum, multipliers, analytic GSO completion, and factorization are missing. |
| W10 | Quantum string-field/BV data | Open | No $`q=79`$-specific vertices and quantum BV master-action certificate have been emitted. |
| W11 | Tadpole and infrared control | Open | Vacuum shift, tadpole cancellation, massless soft behavior, and degeneration prescriptions remain to be supplied on the same branch. |
| W12 | Beyond fixed genus | Open | No all-genus summability or nonperturbative definition at finite string coupling is claimed. |

Partial and open rows in the current $`q=79`$ heterotic worldsheet contract.

</div>

The count is therefore
``` math
\boxed{5\ \text{available},\qquad 2\ \text{partial},\qquad 5\ \text{open}.}
```
Rows W8 and W9 are genuine advances: they reduce the unknown worldsheet data to a much sharper finite and analytic interface. They do not count as complete until their missing objects are constructed on the same physical background.

## The physical-bundle dependency

The principal geometric dependency is not another four-dimensional fit. It is one physical non-pullback visible–hidden Hull–Strominger endpoint with holomorphic bundles, a common positive HYM chamber, connections, and the differential anomaly identity. The current topological clutching data show that the required instanton and chirality targets are not excluded, but topological admissibility does not prove holomorphic existence or HYM.

This is why the $`q=79`$ worldsheet blocker depends on the physical Hull–Strominger endpoint. The quantum amplitude side independently depends on a renormalized BV/QME transport or an equivalent construction. Both dependencies must be discharged before the present conditional theorem can be instantiated.

## Finite modular data: exact but incomplete

The selected finite gerbe cocycle gives an exact discrete-torsion phase on 81 torus twist sectors. Their modular $`S,T`$ action reduces to seven seed blocks, and the associated twisted group algebra is $`\operatorname{Mat}_3(\mathbb C)`$. These are exact finite statements.

Analytic characters carry oscillator spectra, current algebras, spin structures, and multiplier systems. The finite permutation/cocycle layer constrains how such characters may transform, but it cannot supply their $`\tau`$-dependence or prove factorization. This distinction prevents a finite modular covariance certificate from being mistaken for a one-loop string partition function.

# Ultraviolet inheritance at fixed genus

The current q79 research corpus contains the following conditional result, which is imported rather than re-owned here:

> If one same-source $`q=79/F`$ background supplies an exact anomaly-free modular heterotic $`(0,2)`$ SCFT, a tachyon-free GSO projection, factorization, a heterotic quantum BV master action, and a tadpole/infrared prescription, then fixed-genus, fixed-multiplicity amplitudes have no local ultraviolet divergences.

The logic is standard string perturbation theory: local short-tube regions are controlled by modular equivalence, while boundaries of moduli space are handled through factorization and infrared prescriptions .

This result is not a permanent Gaussian damping of the physical graviton propagator. It is conditional inheritance from a complete worldsheet. Because W8–W11 are not closed, it is not yet an unconditional $`q=79`$ ultraviolet-completion theorem. Even after those fixed-genus rows close, convergence of the sum over genera and a nonperturbative definition remain the independent W12 boundary.

# Four-dimensional reduction and prediction

Once a complete compactification record is supplied, standard dimensional reduction can produce a four-dimensional effective action. Gauge couplings, Yukawa couplings, masses, and threshold corrections depend on normalized internal modes, moduli, bundle data, and a renormalization and matching scheme. For example, a holomorphic Yukawa is schematically an internal overlap integral, but its physical value also depends on kinetic normalization and transport to the comparison scale.

The finite $`27\times27`$ MTT carrier and the current Standard Model parity and profile calculations can be compatible with such a reduction. They do not become string-derived merely because the same finite ranks appear. Conversely, a future worldsheet construction would not turn measured profile inputs into source-selected predictions unless its normalized overlap kernels emit those values independently.

The factorization required for a genuine string origin is therefore a commuting chain
``` math
\begin{split}
u_\ast
&\xmapsto{\ \mathcal R_{\mathrm{str}}\ }
\mathfrak S_{q79}
\xmapsto{\ \text{compactification}\ }
\mathfrak E_4\\
&\xmapsto{\ \text{RG and matching}\ }
\mathcal O_{\mathrm{physical}},
\end{split}
```
with the same source, conventions, and uncertainty budget throughout. Each arrow is an independent theorem or certified computation.

# Claim audit and completion plan

## Disposition of Version 1 claims

<div class="center">

| Former claim | Status | Version 2 resolution |
|:---|:---|:---|
| Bounded projection produces Polyakov/RNS theory | Withdrawn | Pullback produces local couplings only after the worldsheet fields and action are supplied; quantum data remain separate. |
| An MTT fixed point implies $`\beta=0`$ | Conditional | Replaced by <a href="#prop:residual-transfer" data-reference-type="ref+label" data-reference="prop:residual-transfer">5</a> with scheme, order, completeness, and error hypotheses. |
| BRST nilpotence is equivalent to leading beta functions | Withdrawn | BRST requires the full matter-plus-ghost quantum system and anomaly cancellation. |
| Characteristic-number equality proves the Bianchi identity | Withdrawn | Cohomological equality is not a differential or global gerbe certificate. |
| The Hull–Strominger solution is the unique MTT minimizer | Withdrawn | The adjacent paper now proves only a conditional fixed-point correspondence. |
| Modular invariance is automatic in the compactification corner | Withdrawn | The actual characters, GSO sum, measure, sewing, and factorization must be constructed. |
| Circle spectral symmetry proves exact T-duality | Narrowed | It proves the momentum–winding seed; full Buscher and quantum data are additional. |
| MTT has a complete ultraviolet-finite string sector | Conditional | Fixed-genus UV inheritance follows only after the W8–W11 worldsheet contract is supplied. |
| Curvature-gap dynamics fix the four-dimensional potential | Withdrawn | Moduli stabilization and normalized reduction require an independent source and calculation. |
| S-duality, holography, and M-theory follow from this bridge | Out of scope | They require separate nonperturbative or boundary realization maps. |

</div>

## The shortest route to an instantiated theorem

The present theorem becomes a physical $`q=79`$ result only after the following same-source sequence is completed.

1.  Construct the non-pullback visible and hidden holomorphic bundles on the selected Fu–Yau carrier, their common HYM chamber and connections, and the differential/global anomaly data.

2.  Derive or construct the exact infrared $`(0,2)`$ SCFT and identify the target fields with the physical bundle rather than an aggregate local anomaly model.

3.  Emit the seven analytic seed characters, oscillator and current sectors, spin-structure and GSO sum, multipliers, modular mixing, and factorization.

4.  Construct the $`q=79`$-specific string-field vertices or an equivalent quantum BV/QME certificate.

5.  Supply the tadpole, vacuum-shift, soft, and infrared prescription.

6.  Evaluate the factorization $`\mathcal A_{\mathrm{MTT}}=\mathcal A_{\mathrm{ws}}\circ\mathcal R_{\mathrm{str}}`$ on a nontrivial held-out observable set.

All-genus summability or a nonperturbative definition is a subsequent question, not a hidden seventh item in the fixed-genus claim.

## Conclusion

String theory remains a serious and promising realization language for MTT, especially on the selected $`q=79`$ Fu–Yau branch. The corrected relation is now exact in its logic. MTT may supply an upper source and selection mechanism; standard worldsheet theory supplies the consistency and amplitude machinery; a typed source map and commuting evaluation diagram must connect them.

Five of the twelve $`q=79`$ worldsheet rows are available and two are partially constructed. This is meaningful progress, but it is not a complete string background. The remaining work is no longer summarized by the vague phrase “derive the worldsheet.” It is the concrete physical bundle, IR SCFT, analytic modular/GSO, BV, and infrared packet listed above. When those rows are emitted from one source, <a href="#thm:string-realization" data-reference-type="ref+label" data-reference="thm:string-realization">3</a> will turn the present conditional encoding into an instantiated perturbative-string result.

#### Corpus-state cross-checks.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*derived exact*).

  Literal 81-entry, 729-cocycle finite Cech witness.

- (*derived exact*).

  Executable q=79 exact-branch audit.

- (*derived exact*).

  CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The exact q79 arithmetic, finite rank-two Cech witness, and rank-two Wiener-contraction certificate are contextual evidence for the selected heterotic branch. They do not directly construct the physical non-pullback visible-hidden bundle, exact infrared (0,2) SCFT, analytic modular/GSO characters, quantum BV packet, tadpole prescription, all-genus completion, or the typed MTT-to-worldsheet evaluation factorization.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Corpus-state cross-checks

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A07/literal_cech_witness` (**DERIVED_EXACT**): Literal 81-entry, 729-cocycle finite Cech witness.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
