---
abstract: |
  The Hull–Strominger system couples a conformally balanced Hermitian metric, holomorphic gauge bundles, Hermitian–Yang–Mills connections, torsion, and the differential Green–Schwarz identity on one compact complex threefold. This paper asks a precise question: when does a fixed point of a Modal Triplet Theory evolution determine a solution of that system? We define a typed bridge from an upstairs MTT configuration space to Hull–Strominger data and prove exact and residual fixed-point descent theorems. Exact descent requires the bridge to intertwine the selected MTT flow with a lower geometric flow, such as the Anomaly flow together with the required bundle evolutions. Approximate intertwining yields only a quantified equation residual. These results establish a conditional correspondence, not compactification selection. The former selection-potential, global-convexity, and automatic Fu–Yau claims are withdrawn. Established Fu–Yau and Anomaly-flow results provide a mathematically appropriate lower target, while the selected $`q=79`$ program still lacks one common rank-three visible–hidden Hull–Strominger tuple and a connection-preserving intertwiner from the MTT carrier.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: c7cbe4cc0ebe987609ae16a2520b6df9bf18aff70c503657b6a356a7ba2cba2d
paper_id: modal-triplet-theory-from-mtt-to-the-strominger-heterot-b2789a83
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and the Hull–Strominger System:
  A Conditional Fixed-Point Correspondence and the $`q=79`$ Completion Boundary
zenodo_doi: 10.5281/zenodo.21707236
zenodo_record_id: 21707236
zenodo_url: "https://zenodo.org/records/21707236"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1 and its claim that MTT had uniquely selected a non-Kähler heterotic compactification.

The earlier argument used a “twisted differential” even though the anomaly equation generally gives $`\mathrm dH\ne0`$, inferred a contraction without a verified contraction constant, and treated an indefinite constrained functional as a coercive strictly convex selection potential. It also assembled Fu–Yau, Iwasawa, bundle, and MTT ingredients that had not been constructed on one common carrier.

This version removes the invalid selection functional and replaces it with a typed flow-intertwining contract. It proves exactly what follows from an intertwiner, gives the corresponding residual estimate, and separates lower Hull–Strominger existence from MTT source selection.

The Hull–Strominger equations, the use of conformally balanced geometry and Hermitian–Yang–Mills data, fixed-point methods as a possible bridge, and Fu–Yau geometry as the strongest established lower-space target are retained.

MTT must still construct one selected $`q=79`$ physical visible–hidden background and prove that its upper evolution descends to the required geometric and bundle flows with the same connections, traces, and global flux data.

</div>

# The question and the answer

## Why a fixed-point bridge is attractive

The Hull–Strominger system is not one equation. It is an assembly of complex geometry, gauge theory, a differential anomaly equation, and global flux data. MTT, in turn, is organized around admissible carriers, projected sectors, and fixed-point evolution. It is therefore natural to ask whether an MTT fixed point can be transported into a heterotic fixed point.

The attraction of this idea should not obscure the logical order. A fixed point in one space is not automatically a fixed point in another. One needs a map between the spaces, and that map must respect the evolutions. This paper supplies that missing mathematical sentence:
``` math
\begin{CD}
\mathcal U_{\mathrm{MTT}} @>{R_\tau}>> \mathcal U_{\mathrm{MTT}}\\
@V{\mathfrak B}VV @VV{\mathfrak B}V\\
\mathcal Y_{\mathrm{HS}} @>{S_\tau}>> \mathcal Y_{\mathrm{HS}} .
\end{CD}
```
Here $`R_\tau`$ is a selected MTT stabilization evolution, $`S_\tau`$ is a declared lower geometric evolution, and $`\mathfrak B`$ is a typed bridge. The commuting square is an assumption until its rows are derived from one source.

## What is proved

The paper owns three limited results.

1.  Exact flow intertwining sends an MTT fixed point to a lower fixed point.

2.  A bounded intertwining defect sends an MTT fixed point only to a lower approximate solution, with the same explicit defect bound.

3.  Local uniqueness or selection requires an invariant contraction basin and cannot be inferred from fixed-point correspondence alone.

These are mathematical bridge theorems. They do not prove that MTT already provides the hypotheses.

## Dependency map

The argument has five layers:
``` math
\begin{split}
\text{one Hull--Strominger carrier}
&\longrightarrow \text{lower residuals and lower flow}\\
&\longrightarrow \text{typed MTT-to-lower bridge}\\
&\longrightarrow \text{intertwining certificate}\\
&\longrightarrow \text{fixed-point descent}\\
&\longrightarrow \text{physical completion tests}.
\end{split}
```
Sections <a href="#sec:hs" data-reference-type="ref" data-reference="sec:hs">2</a> and <a href="#sec:flow" data-reference-type="ref" data-reference="sec:flow">3</a> explain the first two layers. Sections <a href="#sec:bridge" data-reference-type="ref" data-reference="sec:bridge">4</a>–<a href="#sec:selection" data-reference-type="ref" data-reference="sec:selection">6</a> prove the bridge results. Sections <a href="#sec:audit" data-reference-type="ref" data-reference="sec:audit">7</a>–<a href="#sec:frontier" data-reference-type="ref" data-reference="sec:frontier">10</a> state what survives physically.

# One Hull–Strominger object

## Fields and convention

Fix a compact complex threefold $`X`$ with nowhere-vanishing holomorphic $`(3,0)`$-form $`\Omega`$. Let $`\omega`$ be a positive Hermitian form, $`\Phi`$ a dilaton, and $`V_{\mathrm{vis}},V_{\mathrm{hid}}`$ holomorphic Hermitian bundles with unitary connections $`A_{\mathrm{vis}},A_{\mathrm{hid}}`$. Fix also a metric connection $`\nabla`$ on $`TX`$. Its choice is part of the data, not a notation that may be changed between equations.

We use
``` math
\mathrm d^c=\mathrm i\partial\bar\partial,\qquad
H=\mathrm d^c\omega
```
as a convention for the torsion equation. Numerical factors in $`\mathrm d^c`$ and trace normalizations vary in the literature; every comparison below presupposes one convention fixed throughout.

In this convention the first-order equations include
``` math
\begin{align}
\mathrm d\!\left(\|\Omega\|_\omega\omega^2\right)&=0,
\label{eq:balanced}\\
F_a^{0,2}=0,\qquad F_a\wedge\omega^2&=0,
\quad a\in\{\mathrm{vis},\mathrm{hid}\},
\label{eq:gauge-hym}\\
R_\nabla^{0,2}=0,\qquad R_\nabla\wedge\omega^2&=0,
\label{eq:tangent-instanton}\\
\mathrm dH&=\frac{\alpha'}4\left(
\operatorname{tr}R_\nabla\wedge R_\nabla
-\operatorname{tr}F_{\mathrm{vis}}\wedge F_{\mathrm{vis}}
-\operatorname{tr}F_{\mathrm{hid}}\wedge F_{\mathrm{hid}}\right).
\label{eq:bianchi}
\end{align}
```
The tangent-instanton row is included when required by the chosen first-order equations-of-motion convention .

## Global data are a separate row

Writing $`H=\mathrm dB+`$ Chern–Simons terms is local notation. Globally, the $`B`$-field is gerbe data and the Green–Schwarz condition is differential cohomological. A topological equality of second Chern classes is necessary in common settings but does not identify the differential four-form representatives in <a href="#eq:bianchi" data-reference-type="ref+label" data-reference="eq:bianchi">[eq:bianchi]</a>. Likewise, a smooth vector bundle with the desired Chern classes is not yet a holomorphic stable bundle with an HYM connection.

<div id="def:lower" class="definition">

**Definition 1** (Complete lower datum). A point $`y\in\mathcal Y_{\mathrm{HS}}`$ is a tuple
``` math
y=(X,\Omega,\omega,\Phi,V_{\mathrm{vis}},V_{\mathrm{hid}},
A_{\mathrm{vis}},A_{\mathrm{hid}},\nabla,H,\mathfrak g_H)
```
in which all objects live on the same $`X`$, use one trace convention, and $`\mathfrak g_H`$ denotes the global gerbe or differential-cohomological flux datum. Gauge-equivalent tuples represent the same point.

</div>

<div id="def:residual" class="definition">

**Definition 2** (Hull–Strominger residual). After gauge fixing and choosing Sobolev completions, let $`\mathcal R_{\mathrm{HS}}(y)`$ be the vector consisting of the left-hand sides of <a href="#eq:balanced,eq:gauge-hym,eq:tangent-instanton,eq:bianchi" data-reference-type="ref+label" data-reference="eq:balanced,eq:gauge-hym,eq:tangent-instanton,eq:bianchi">[eq:balanced,eq:gauge-hym,eq:tangent-instanton,eq:bianchi]</a>, together with the global patching defect. Thus
``` math
\mathcal R_{\mathrm{HS}}(y)=0
```
means that every declared lower row is satisfied on one common tuple.

</div>

The residual formulation is intentionally unforgiving. It prevents a metric from one construction, a bundle from another, and a topological identity from a third from being advertised as one solution.

# The appropriate lower flow

## Anomaly flow

There is an established geometric flow designed for this setting. In a fixed holomorphic and bundle ansatz, the Anomaly flow evolves the positive $`(2,2)`$-form $`\|\Omega\|_\omega\omega^2`$ by an equation of the form
``` math
\begin{equation}
\partial_\tau\!\left(\|\Omega\|_\omega\omega^2\right)
=\mathrm i\partial\bar\partial\omega
-\frac{\alpha'}4\left(
\operatorname{tr}R_\nabla\wedge R_\nabla
-\operatorname{tr}F_{\mathrm{vis}}\wedge F_{\mathrm{vis}}
-\operatorname{tr}F_{\mathrm{hid}}\wedge F_{\mathrm{hid}}\right).
\label{eq:anomaly-flow}
\end{equation}
```
The exact analytic formulation depends on the selected tangent connection and on whether bundle metrics are fixed or evolved. The flow preserves the conformally balanced condition under its hypotheses, and its stationary points solve the anomaly equation. Short-time existence is known in the original setting, and convergence is known in important Fu–Yau ansatz classes .

The existence of <a href="#eq:anomaly-flow" data-reference-type="ref+label" data-reference="eq:anomaly-flow">[eq:anomaly-flow]</a> is important for MTT because it gives a genuine lower repair dynamics. It does not prove that an MTT flow equals it. Nor does the metric flow by itself construct the holomorphic bundles or their HYM metrics. Those rows must be fixed consistently or coupled to appropriate bundle heat flows.

## A lower semigroup is local to its domain

Let $`\mathcal D_{\mathrm{HS}}\subset\mathcal Y_{\mathrm{HS}}`$ be a gauge-fixed domain on which a lower evolution $`S_\tau`$ is well posed. Depending on the theorem being imported, $`S_\tau`$ may be a local semiflow rather than a global semigroup. We require only
``` math
S_0=\operatorname{id},\qquad
S_{\tau+\sigma}=S_\tau S_\sigma
```
whenever both sides are defined.

<div id="ass:stationary" class="assumption">

**Assumption 3** (Stationary-point identification). On a declared invariant domain $`\mathcal D_0\subset\mathcal D_{\mathrm{HS}}`$,
``` math
\operatorname{Fix}(S)=\{y\in\mathcal D_0:\mathcal R_{\mathrm{HS}}(y)=0\}.
```

</div>

This assumption packages the bundle and global rows that a metric-only Anomaly flow does not automatically enforce. In a Fu–Yau ansatz with fixed valid HYM data, it can be discharged by the corresponding existence and flow theorems. It is not currently discharged on the selected physical $`q=79`$ tuple.

## Why the old twisted complex cannot be used

<div id="lem:twisted" class="lemma">

**Lemma 4** (Anomaly obstruction to the naive twisted differential). *Let $`H`$ be a real three-form and define $`d_H=\mathrm d+H\wedge`$ on differential forms. Then
``` math
d_H^2=(\mathrm dH)\wedge.
```
Consequently $`d_H`$ is not a cochain differential on a generic heterotic background with nonzero Green–Schwarz four-form.*

</div>

<div class="proof">

*Proof.* The graded Leibniz rule gives
``` math
(\mathrm d+H\wedge)^2
=\mathrm dH\wedge+H\wedge H\wedge.
```
Because $`H`$ has odd degree, $`H\wedge H=0`$. The stated identity follows. ◻

</div>

Thus the earlier “twisted harmonic projector” cannot be justified by twisted de Rham cohomology unless $`\mathrm dH=0`$. A corrected operator must instead come from a specified Bismut/Hull covariant Laplacian, an elliptic deformation complex, or the gauge-fixed Hessian of a selected action. Its domain, kernel removal, and spectral gap must be proved for that operator.

# The typed MTT bridge

## Upper data

Let $`\mathcal U_{\mathrm{MTT}}`$ denote an MTT configuration space after quotienting or fixing its declared redundancies. A point $`u`$ may contain the common circle line, local $`1<2<3`$ filtration, global $`q=79`$ carrier data, projectors, connections, and upper fields. Let $`R_\tau`$ be a selected MTT stabilization flow on a domain $`\mathcal D_{\mathrm{MTT}}`$.

This notation does not assume that such a physical continuum flow has already been constructed. It identifies exactly where that future result enters.

<div id="def:bridge" class="definition">

**Definition 5** (Typed bridge). A typed MTT-to-Hull–Strominger bridge is a map
``` math
\mathfrak B:\mathcal D_{\mathrm{MTT}}\longrightarrow\mathcal D_0
```
whose output is a complete lower datum in the sense of Definition <a href="#def:lower" data-reference-type="ref" data-reference="def:lower">1</a>. It must provide the following rows without changing carrier or source:

<div class="center">

| Row | Required image under $`\mathfrak B`$ |
|:---|:---|
| Carrier | one complex threefold $`X`$, complex structure, and $`\Omega`$ |
| Metric | positive $`\omega`$ and dilaton $`\Phi`$ |
| Visible sector | rank-three physical holomorphic bundle and connection |
| Hidden sector | compatible hidden bundle or sheaf and connection |
| Tangent sector | one declared connection $`\nabla`$ and curvature |
| Flux | $`H`$, trace convention, gerbe patching, and quantization |
| Dynamics | tangent map carrying the upper vector field to the lower one |

</div>

</div>

The shared circle can enter this bridge as common line-bundle phase or holonomy data, counted once. That role does not identify it with Lorentzian time and does not by itself construct $`X`$, $`V_{\mathrm{vis}}`$, or the Green–Schwarz class.

## Exact intertwining

<div id="def:intertwiner" class="definition">

**Definition 6** (Flow intertwiner). The bridge $`\mathfrak B`$ intertwines the flows on a common interval $`I`$ if
``` math
\begin{equation}
\mathfrak B\circ R_\tau=S_\tau\circ\mathfrak B,
\qquad \tau\in I,
\label{eq:intertwine}
\end{equation}
```
where both sides are defined.

</div>

Infinitesimally, if the two flows have differentiable vector fields $`\mathcal F_{\mathrm{MTT}}`$ and $`\mathcal F_{\mathrm{HS}}`$, exact intertwining requires
``` math
\begin{equation}
D\mathfrak B_u\,\mathcal F_{\mathrm{MTT}}(u)
=\mathcal F_{\mathrm{HS}}(\mathfrak B(u)).
\label{eq:generator-intertwine}
\end{equation}
```
Equation <a href="#eq:generator-intertwine" data-reference-type="eqref" data-reference="eq:generator-intertwine">[eq:generator-intertwine]</a> is the continuum operator source obligation. Matching only fixed-point labels or dimensions does not prove it.

# Fixed-point descent

<div id="thm:descent" class="theorem">

**Theorem 7** (Conditional fixed-point descent). *Let $`R_\tau`$, $`S_\tau`$, and $`\mathfrak B`$ be as above. Suppose $`\mathfrak B`$ satisfies <a href="#eq:intertwine" data-reference-type="ref+label" data-reference="eq:intertwine">[eq:intertwine]</a> and $`u_\ast\in\mathcal D_{\mathrm{MTT}}`$ is fixed by $`R_\tau`$ for every $`\tau\in I`$. Then $`\mathfrak B(u_\ast)`$ is fixed by $`S_\tau`$ for every $`\tau\in I`$. If Assumption <a href="#ass:stationary" data-reference-type="ref" data-reference="ass:stationary">3</a> holds, then
``` math
\mathcal R_{\mathrm{HS}}(\mathfrak B(u_\ast))=0.
```*

</div>

<div class="proof">

*Proof.* For every permitted $`\tau`$,
``` math
S_\tau(\mathfrak B(u_\ast))
=\mathfrak B(R_\tau u_\ast)
=\mathfrak B(u_\ast).
```
The residual conclusion is exactly Assumption <a href="#ass:stationary" data-reference-type="ref" data-reference="ass:stationary">3</a>. ◻

</div>

<div class="remark">

*Remark 8* (One-way character). The theorem is descent, not equivalence. A lower solution $`y_\ast`$ lifts to an MTT fixed point only if $`y_\ast\in\operatorname{Ran}(\mathfrak B)`$ and an upper preimage is fixed. Uniqueness of the lift additionally requires control of the fibers of $`\mathfrak B`$.

</div>

## Residual descent

Exact commuting diagrams are demanding. A numerical or perturbative bridge usually supplies a defect.

<div id="prop:defect" class="proposition">

**Proposition 9** (Generator-defect bound). *Suppose $`\mathfrak B`$ is differentiable and, on a domain $`\mathcal V`$,
``` math
\left\|
D\mathfrak B_u\,\mathcal F_{\mathrm{MTT}}(u)
-\mathcal F_{\mathrm{HS}}(\mathfrak B(u))
\right\|_{\mathcal Y}
\le \varepsilon .
```
If $`\mathcal F_{\mathrm{MTT}}(u_\ast)=0`$, then
``` math
\left\|\mathcal F_{\mathrm{HS}}(\mathfrak B(u_\ast))\right\|_{\mathcal Y}
\le\varepsilon .
```*

</div>

<div class="proof">

*Proof.* Insert $`\mathcal F_{\mathrm{MTT}}(u_\ast)=0`$ into the defect inequality. ◻

</div>

This proposition is deliberately modest. A small flow residual is not an exact background. To infer a nearby exact solution one needs a separate inverse-function, Newton–Kantorovich, or a posteriori theorem with a gauge-fixed derivative, inverse bound, nonlinear remainder estimate, and a verified radius.

# What selection would additionally require

<div id="prop:contraction" class="proposition">

**Proposition 10** (Contraction-basin criterion). *Let $`(\mathcal B,d)`$ be a nonempty complete invariant subset of $`\mathcal D_{\mathrm{HS}}`$. If for some $`\tau_0>0`$
``` math
d(S_{\tau_0}y,S_{\tau_0}z)\le q\,d(y,z),
\qquad y,z\in\mathcal B,\qquad 0\le q<1,
```
then $`S_{\tau_0}`$ has exactly one fixed point in $`\mathcal B`$, and its Picard iterates converge geometrically to that point.*

</div>

<div class="proof">

*Proof.* This is the Banach fixed-point theorem on $`\mathcal B`$. ◻

</div>

The content lies in proving the invariant complete basin and the number $`q<1`$. Parabolic smoothing alone does not do this. A schematic estimate of the form $`C_\Pi M(\tau)e^{L\tau}`$ proves contraction only after one establishes that it is strictly below one for a specified $`\tau`$ on a specified domain.

<div id="prop:no-selection" class="proposition">

**Proposition 11** (Correspondence does not imply selection). *Suppose $`\mathfrak B`$ intertwines two flows. If the lower flow has two fixed points in $`\mathfrak B(\mathcal D_{\mathrm{MTT}})`$, intertwining alone cannot select one of them.*

</div>

<div class="proof">

*Proof.* The identity map on a space with a flow having two fixed points is already an intertwiner and selects neither. Additional basin, initial-data, variational, or source information is necessary. ◻

</div>

Consequently the phrase “MTT selects the compactification” requires more than <a href="#thm:descent" data-reference-type="ref+label" data-reference="thm:descent">7</a>. It requires a selected upper initial condition or branch, a complete invariant basin, uniqueness within the physically relevant quotient, and a proof that no other admissible basin realizes the same observables.

# Audit of the former selection argument

## The functional was not a selection theorem

The previous version introduced a functional $`\Xi`$ containing the string-frame curvature term, $`H`$- and Yang–Mills terms, Lagrange multipliers, and a spectral variance term. It then claimed:
``` math
\operatorname{Crit}(\Xi)
\Longleftrightarrow
\{\text{Hull--Strominger{} solutions}\},
\qquad
D^2\Xi>0.
```
Neither implication was established.

First-order supersymmetry equations are not generally identical to the Euler–Lagrange equations of the ten-dimensional action. Under additional instanton and perturbative assumptions, solutions of the supersymmetry and Bianchi equations can imply the equations of motion, but that is not a variational equivalence . Second, scalar curvature and multiplier terms do not give an evidently bounded-below functional. Third, positivity of a principal elliptic block does not control all lower-order couplings or moduli. Finally, a spectral scalar cannot be asserted to lift every geometric and bundle modulus without its actual second variation.

Accordingly, this version does not use $`\Xi`$, does not claim global attraction, and does not identify an MTT fixed point with a unique minimizer. An action-derived repair flow remains a valuable future target, but it must be constructed before its Hessian or Lyapunov properties are quoted.

## Connection and torsion bookkeeping

The gauge-invariant three-form should satisfy both the local Chern–Simons description and the global differential-cohomological patching law. Once $`H`$ is used for that gauge-invariant object, the supersymmetry torsion equation is $`H=\mathrm d^c\omega`$ in the chosen convention. Subtracting the Chern–Simons terms a second time from the torsion equation double counts them.

The tangent connection $`\nabla`$ also cannot be changed silently between the torsion equation, Bianchi identity, anomaly flow, and equations-of-motion claim. Different choices may define different Hull–Strominger systems .

# Fu–Yau, Iwasawa, and the current MTT evidence

## What established mathematics supplies

Fu and Yau constructed solutions on non-Kähler torus bundles over K3 under specific topological, bundle, and analytic hypotheses . Later work extended and reorganized these constructions, including solutions with torus symmetry and tangent HYM connections . The Anomaly flow is known to converge in a Fu–Yau ansatz for controlled initial data .

These results prove that the lower target is mathematically inhabited. They do not show that the selected MTT $`q=79`$ carrier is one of those solutions, nor that its upper flow descends to the Anomaly flow.

## The q79 rows must not be merged

The current MTT corpus contains several nontrivial but separate results:

1.  exact finite arithmetic selecting the $`q=79`$ branch;

2.  smooth rank-three topological candidates with index $`\pm3`$;

3.  an exact finite rank-two Cech witness;

4.  a certified finite rank-two HYM approximation; and

5.  a rank-two Wiener-algebra existence and local-uniqueness certificate.

The packets and verifiers are curated in Ref. . The rank-two analytic theorem does not change its bundle rank, Chern classes, or carrier. The topological rank-three candidate is not yet a stable holomorphic visible bundle with an HYM connection.

The physical completion therefore still needs, on one $`X_{79}`$:

<div class="center">

| Gate | Required object | Current state |
|:---|:---|:---|
| G1 | complex $`X_{79}`$, $`\Omega`$, and positive balanced Fu–Yau metric | candidate/partial |
| V1 | rank-three visible holomorphic stable bundle with index $`\pm3`$ | open |
| V2 | compatible hidden holomorphic data | open |
| H1 | visible, hidden, and tangent instantons in one chamber | rank-two evidence |
| A1 | differential Green–Schwarz identity with fixed traces | open |
| Q1 | global gerbe and flux quantization | open |
| B1 | connection-preserving MTT bridge and flow intertwiner | open |

</div>

This is the physical content of the open blockers $`B.\mathrm{HS}.01`$ and $`B.\mathrm{GEO}.01`$.

## The corrected role of Iwasawa and Lens–Nil

The Iwasawa manifold remains a useful source of explicit balanced $`SU(3)`$-structure calculations. The companion bundle audit shows, however, that the earlier printed rank-three bundle, Bianchi match, and selected-background conclusion do not survive. Other valid Iwasawa Hull–Strominger solutions exist in the literature; their existence does not repair that specific MTT construction.

Likewise,
``` math
\text{local Circle--Lens--Nil filtration}
\not\equiv L(3,1)\times\mathrm{Nil}_3
\not\equiv X_{79}.
```
Lens and Nil may remain auxiliary finite, spectral, or transport labels. They are not a substitute for the integrable complex geometry and global bundle data in Definition <a href="#def:lower" data-reference-type="ref" data-reference="def:lower">1</a>.

# Worldsheet and physical interpretation

A first-order Hull–Strominger background is an important string-theoretic object, but it is not by itself a complete four-dimensional model. A worldsheet completion requires the relevant anomaly, conformal, modular, factorization, and GSO data. Four-dimensional physics additionally requires the massless cohomology, representation embedding, normalized kinetic terms, overlap integrals, moduli treatment, and quantum corrections.

The fixed-point bridge therefore has a precise interpretation:

- it can explain how an upper MTT equilibrium becomes a lower geometric equilibrium;

- it can transport a certified residual and its error budget;

- it cannot create missing bundles or flux data;

- it cannot turn a conditional encoding into source selection; and

- it does not derive low-energy masses or couplings without additional normalized overlap and transport maps.

# A concrete completion program

The revised bridge suggests an efficient order of work.

1.  Construct the physical rank-three visible bundle on the selected Fu–Yau-oriented $`q=79`$ carrier and prove stability.

2.  Construct compatible hidden and tangent instantons in the same metric chamber.

3.  Solve the differential Green–Schwarz equation with fixed traces and provide global gerbe data.

4.  Define the MTT configuration space and its selected continuum vector field on that same tuple.

5.  Define every row of $`\mathfrak B`$, including connection and domain maps.

6.  Prove <a href="#eq:generator-intertwine" data-reference-type="ref+label" data-reference="eq:generator-intertwine">[eq:generator-intertwine]</a>, or emit a certified defect bound.

7.  Use <a href="#thm:descent" data-reference-type="ref+label" data-reference="thm:descent">7</a> or <a href="#prop:defect" data-reference-type="ref+label" data-reference="prop:defect">9</a>; if selection is claimed, independently prove the contraction-basin hypotheses of <a href="#prop:contraction" data-reference-type="ref+label" data-reference="prop:contraction">10</a>.

This program is stricter than the previous selection-potential route, but it also uses more of the mathematics that already exists. In particular, the Anomaly flow supplies the correct lower fixed-point language instead of inventing a second unverified flow.

# Conclusion

The viable relationship between MTT and the Hull–Strominger system is a conditional fixed-point correspondence. Its central object is not an assumed selection potential but a typed, connection-preserving flow intertwiner. If that intertwiner and one upper fixed point are supplied, fixed-point descent is exact. If only a defect estimate is supplied, the result is an approximate lower solution until an a posteriori theorem closes the residual.

Fu–Yau geometry and the Anomaly flow make this route mathematically credible. The current $`q=79`$ finite, topological, and rank-two results make it nonempty as an MTT research program. They do not yet provide the common rank-three visible–hidden background or the intertwiner. Those two objects, not another reformulation of the old potential, are the present frontier.

#### Rows used directly in this paper.

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

The q79 arithmetic theorem and audit, literal finite rank-two Cech witness, and rank-two Wiener-contraction certificate provide direct evidence only at their declared finite, topological, or rank-two analytic tiers. They do not construct the common physical rank-three visible-hidden Hull-Strominger background, differential Green-Schwarz representative, flux gerbe, worldsheet endpoint, or the typed MTT-to-Anomaly-flow intertwiner required by the conditional fixed-point theorem.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A07/literal_cech_witness` (**DERIVED_EXACT**): Literal 81-entry, 729-cocycle finite Cech witness.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
