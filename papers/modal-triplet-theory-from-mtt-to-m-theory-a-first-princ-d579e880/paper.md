---
abstract: |
  This paper asks when Modal Triplet Theory (MTT) realizes an eleven-dimensional low-energy sector of M-theory. Eleven-dimensional supergravity is not specified by a metric and a three-form alone: the full record includes an oriented Lorentzian spin manifold, vielbein, gravitino, shifted differential C-field, action and normalization, local supersymmetry, source and boundary data, and a declared quantum and derivative-order scope. M2- and M5-branes additionally require embeddings, normal bundles, worldvolume fields, kappa symmetry, self-duality data, and anomaly inflow. We package these ingredients as a typed eleven-dimensional record and define a partial map from an upper MTT state to that record. The main theorem is conditional: if one selected MTT state emits every required row, the lower record satisfies the standard consistency conditions at the declared order, and MTT evaluation factors through the eleven-dimensional effective theory, then MTT realizes that sector on the stated domain. We also prove that the axioms of a bounded projector or pullback alone do not select a unique spacetime, C-field, brane content, or action. The Cremmer–Julia–Scherk action, shifted flux law, supermembrane and five-brane systems, anomaly inflow, and type-IIA circle reduction are therefore used as standard lower targets, not re-derived from projection. Current q=79 arithmetic and heterotic Cech/Hermitian–Yang–Mills results are compatible contextual data, but they do not yet emit an eleven-dimensional spin geometry, M-theory circle, differential C-field, gravitino, brane sources, or connection-preserving action map. A nonperturbative definition of M-theory and four-dimensional phenomenological predictions remain outside the established result.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: fa72334c6f5c7edb1f947e216c170ce788db0f3452e744bc36317674f1f75f5a
paper_id: modal-triplet-theory-from-mtt-to-m-theory-a-first-princ-d579e880
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and the M-Theory Low-Energy Limit:
  A Conditional Eleven-Dimensional Encoding Contract
zenodo_doi: 10.5281/zenodo.21708348
zenodo_record_id: 21708348
zenodo_url: "https://zenodo.org/records/21708348"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1 and its claim that MTT projection had already derived the eleventh dimension, complete eleven-dimensional action, shifted flux quantization, M2/M5 worldvolume theories, anomaly inflow, type-IIA descent, moduli stabilization, three families, and low-energy observables.

The former argument placed standard M-theory and supergravity formulas after a projection symbol and treated that placement as a derivation. It omitted the gravitino from the claimed full field content, represented the global C-field only by an ordinary three-form, asked pullback to create rather than transport brane data, and promoted circle reduction and finite-dimensional residuals beyond their hypotheses. It also imported withdrawn compactification-selection and phenomenology claims from adjacent papers.

This revision defines the complete lower record and the typed MTT source map. It proves a conditional factorization theorem and a projector nonselection proposition. Standard action, flux, brane, anomaly, and reduction results are stated with their actual hypotheses and literature ownership. The q=79 heterotic branch is separated from a still-unconstructed eleven-dimensional lift.

Eleven-dimensional supergravity remains a valuable lower realization target. The CJS action, shifted C-field quantization, M2/M5 couplings, anomaly inflow, and massless type-IIA reduction remain in the paper as compatibility gates. MTT may still supply their common source, but that source has to be constructed and verified.

The current research ledger leaves blocker B.ACTION.01 open. Its exit requires one selected upper differential/action object whose automorphisms, zero modes, products, and finite operators reproduce the accepted lower structures through certified commuting maps.

</div>

# The corrected question

## M-theory and its low-energy limit are not the same claim

Eleven-dimensional supergravity is the classical low-energy effective theory associated with M-theory. Its massless multiplet contains the vielbein, gravitino, and three-form gauge potential. M-theory is the broader quantum framework whose different limits include eleven-dimensional supergravity and the strong-coupling type-IIA regime . No complete background-independent nonperturbative definition is presently available for arbitrary spacetime. Consequently, matching the classical supergravity action is not by itself a definition of full M-theory.

This paper therefore uses the phrase *M-theory low-energy limit* for a declared eleven-dimensional effective sector. The declaration must state the derivative order, loop order, source class, boundary conditions, and observables. A claim about the bosonic two-derivative truncation is narrower than a claim about local supersymmetry, and both are narrower than a quantum or nonperturbative statement.

## Three logically different achievements

The following levels must remain distinct.

<div class="description">

MTT variables are mapped to symbols with the tensor types of an eleven-dimensional metric, spinor, or C-field.

One complete lower record is emitted, satisfies the standard equations and global conditions at a declared order, and receives the MTT observables through a commuting evaluation map. This is the theorem proved here.

An MTT source, flow, preparation, or branch law chooses that record and its normalization rather than another allowed record. Representation and consistency do not supply this final step.

</div>

Version 1 moved directly from the first level to the third. The corrected paper makes the middle level exact and lists what the selection level still requires.

## Argument map

<a href="#sec:record" data-reference-type="ref+Label" data-reference="sec:record">2</a> defines the full lower object. <a href="#sec:map" data-reference-type="ref+Label" data-reference="sec:map">3</a> states the MTT encoding theorem and the nonselection result. <a href="#sec:cjs,sec:cfield,sec:branes" data-reference-type="ref+Label" data-reference="sec:cjs,sec:cfield,sec:branes">[sec:cjs,sec:cfield,sec:branes]</a> review the standard action, global C-field, and brane data that the map must emit. <a href="#sec:iia" data-reference-type="ref+Label" data-reference="sec:iia">7</a> describes the precise massless type-IIA reduction. <a href="#sec:q79" data-reference-type="ref+Label" data-reference="sec:q79">8</a> separates the existing q=79 heterotic work from a putative M-theory lift. <a href="#sec:four,sec:frontier" data-reference-type="ref+Label" data-reference="sec:four,sec:frontier">[sec:four,sec:frontier]</a> state the four-dimensional and research boundaries.

# The lower object to be realized

## Why a metric and three-form are insufficient

A local bosonic formula may be written using a Lorentzian metric $`g`$ and a three-form potential $`C_3`$. The complete theory needs more. Fermions require a spin structure and a choice of spinor bundle. Local supersymmetry requires the gravitino, transformation laws, gauge algebra, and domains. Nontrivial flux means that $`C_3`$ need not be a single global three-form. Magnetic five-branes change the Bianchi identity and require source regularization. Quantum phases and anomaly cancellation depend on global differential data, not only on the curvature $`G_4`$.

<div id="def:record" class="definition">

**Definition 1** (Eleven-dimensional low-energy record). Fix a derivative order $`r`$, loop order $`\ell`$, source class $`\mathcal B`$, and observable class $`\mathcal O`$. An eleven-dimensional low-energy record is a tuple
``` math
\mathfrak M_{11}=
(\mathfrak G,\mathfrak F,\mathfrak C,\mathfrak A,
 \mathfrak S,\mathfrak B,\mathfrak Q,\mathfrak D)
```
with the following typed rows.

1.  $`\mathfrak G`$ is an oriented time-oriented Lorentzian spin eleven-manifold $`Y^{10,1}`$, together with boundary, asymptotic, and regularity data.

2.  $`\mathfrak F=(e,\psi,\nabla)`$ contains the vielbein or metric, gravitino, compatible connection, spinor bundle, and field domains.

3.  $`\mathfrak C`$ is a shifted degree-four differential C-field $`\check C`$, including its local potentials, curvature $`G_4`$, characteristic class, gauge equivalences, and boundary trivializations.

4.  $`\mathfrak A`$ contains the effective action through $`(r,\ell)`$, its normalization, variational domain, gauge symmetries, local supersymmetry transformations, and equations of motion.

5.  $`\mathfrak S`$ contains electric and magnetic source currents and, when present, brane embeddings, normal bundles, worldvolume fields, kappa symmetry, self-duality, charges, and tensions.

6.  $`\mathfrak B`$ contains Bianchi identities, shifted quantization, local and global anomaly data, and inflow or boundary terms.

7.  $`\mathfrak Q`$ declares the quantum status: classical, semiclassical, perturbative to order $`\ell`$, or a specified nonperturbative construction, together with its state space, measure, and observables.

8.  $`\mathfrak D`$ contains any dimensional-reduction or duality map, including the circle bundle, radius, connection, spin structure, truncation, and lower-field dictionary.

</div>

The scope labels $`(r,\ell,\mathcal B,\mathcal O)`$ are part of the record. They prevent a two-derivative bosonic check from silently becoming a statement about fermions, branes, all loops, or full M-theory.

## Consistency gates

A record is *lower-consistent* on its declared domain when:

1.  its fields and sources satisfy the stated action principle and equations, including gauge and local-supersymmetry closure at the declared order;

2.  its C-field has the required shifted integral refinement and the source-modified Bianchi identities are compatible;

3.  all included branes have well-defined worldvolume theories and their local and global anomalies cancel;

4.  the variational and quantum constructions use compatible boundary conditions and domains; and

5.  every claimed reduction is a consistent truncation or a controlled effective reduction with a stated error.

These gates are ordinary supergravity, differential-cohomological, and brane mathematics. MTT enters in sourcing and selecting the complete record and in proving that its own evaluation agrees with the lower one.

# The MTT encoding contract

## Typed source and evaluation maps

Let $`\mathcal U_{\mathrm{MTT}}`$ be the upper MTT state domain. A candidate eleven-dimensional realization is a partial typed map
``` math
\mathcal R_{11}:\mathcal U_{\mathrm{MTT}}
\dashrightarrow
\operatorname{Rec}_{11}(r,\ell,\mathcal B,\mathcal O).
```
Partiality is essential. Most upper states need not determine a complete eleven-dimensional record. Even for a selected state $`u_\star`$, individual rows may be open.

Let $`\mathcal E_{\mathrm{MTT}}`$ denote the MTT observable evaluation and $`\mathcal E_{11}`$ the standard evaluation defined by the lower record. A map
``` math
\iota_{u_\star}:\mathcal O_{\mathrm{MTT}}
\longrightarrow
\mathcal O_{11}(\mathcal R_{11}(u_\star))
```
types the observables being compared. The decisive condition is the commuting relation
``` math
\begin{equation}
\mathcal E_{\mathrm{MTT}}(u_\star,O)
=
\mathcal E_{11}\!\left(\mathcal R_{11}(u_\star),\iota_{u_\star}(O)\right)
\label{eq:factor}
\end{equation}
```
for every $`O`$ in the declared class, with any approximation order and error bound written explicitly.

<div id="thm:realization" class="theorem">

**Theorem 2** (Conditional eleven-dimensional realization). *Let $`u_\star\in\mathcal U_{\mathrm{MTT}}`$. Suppose:*

1.  *$`\mathcal R_{11}(u_\star)`$ is a complete record in the sense of Definition <a href="#def:record" data-reference-type="ref" data-reference="def:record">1</a>;*

2.  *that record is lower-consistent at the declared $`(r,\ell,\mathcal B,\mathcal O)`$ scope;*

3.  *the MTT source map preserves every connection, differential, gauge action, source term, boundary condition, and normalization used by the lower evaluation; and*

4.  *<a href="#eq:factor" data-reference-type="ref+label" data-reference="eq:factor">[eq:factor]</a> holds on $`\mathcal O_{\mathrm{MTT}}`$, exactly or with the declared controlled error.*

*Then MTT realizes the specified eleven-dimensional low-energy sector on that domain. Exact factorization gives equality of the declared observables; controlled factorization gives only the corresponding error-bounded equivalence.*

</div>

<div class="proof">

*Proof.* The first two hypotheses produce a well-defined lower theory and evaluation map at the stated scope. The third hypothesis makes the source map structure-preserving rather than a comparison of untyped symbols. The fourth identifies each declared MTT evaluation with the lower evaluation. Thus all observables in the comparison class agree at exactly the stated order. No conclusion follows outside the specified source, derivative, loop, boundary, or observable domain. ◻

</div>

<div class="remark">

*Remark 3*. The theorem is intentionally stronger than a field dictionary and weaker than physical selection. It proves what follows once a complete selected source exists. It does not manufacture that source.

</div>

## What projection alone cannot determine

Pullback is a transport operation. Given an embedding $`X:\Sigma\to Y`$, it turns a supplied target field into a worldvolume field such as $`X^\ast g`$ or $`X^\ast C_3`$. It does not choose $`Y`$, construct $`X`$, or create the worldvolume gauge system. The same distinction applies to an abstract MTT projector.

<div id="prop:nonselection" class="proposition">

**Proposition 4** (Projector nonselection). *The axioms of a bounded projector $`P^2=P`$ on an upper state space, even together with the existence of pullbacks after target maps are supplied, do not logically determine a unique eleven-dimensional spin manifold, differential C-field, brane content, or action.*

</div>

<div class="proof">

*Proof.* Fix one Hilbert space $`\mathcal H`$ and one bounded projector $`P`$ on it. The projector identities remain unchanged if the same pair $`(\mathcal H,P)`$ is adjoined to either
``` math
\mathbb R_t\times T^{10}
\qquad\text{or}\qquad
\mathbb R_t\times S^4\times T^6,
```
with independently chosen spin structures and C-field classes. These eleven-manifolds are not equivalent as topological targets, and their degree-four data differ. On either target one may further vary the differential C-field while leaving $`P`$ fixed. Brane embeddings and their worldvolume fields can likewise be added or omitted without changing the projector axioms. Therefore two models satisfy the same projector premises and disagree on every claimed output. Additional source data or a structure-preserving construction is necessary to select among them. ◻

</div>

The proposition does not say that MTT can never select an eleven-dimensional record. It says that such selection must occur in the extra geometry, action, flow, or source law, not in idempotence or contractivity alone.

# The standard eleven-dimensional target

## The CJS multiplet

The classical massless multiplet of eleven-dimensional supergravity is
``` math
(e_M{}^A,\psi_M,C_{MNP}),
```
not merely $`(g,C_3)`$ . The vielbein describes the metric, $`\psi_M`$ is a Majorana vector-spinor, and $`C_3`$ is locally a three-form potential. Setting $`\psi_M=0`$ is a bosonic truncation. A claimed derivation of the full theory must also emit the spin bundle, gravitino kinetic and interaction terms, local supersymmetry transformations, and their closure conventions.

In a common bosonic convention, away from sources and global patching subtleties,
``` math
\begin{equation}
S_{\mathrm{CJS,bos}}
=\frac{1}{2\kappa_{11}^{2}}
\left[
\int_Y\left(R\star 1-\frac12 G_4\wedge\star G_4\right)
-\frac16\int_Y C_3\wedge G_4\wedge G_4
\right],
\qquad
G_4=\mathrm dC_3 .
\label{eq:cjs}
\end{equation}
```
The corresponding source-free form equations are
``` math
\begin{equation}
\mathrm dG_4=0,
\qquad
\mathrm d\star G_4+\frac12 G_4\wedge G_4=0,
\label{eq:form-eom}
\end{equation}
```
with the Einstein equation and fermionic equations completing the system. Signs vary with signature and orientation conventions, so the record must fix them rather than compare isolated coefficients.

## What this formula does and does not prove

<a href="#eq:cjs" data-reference-type="ref+Label" data-reference="eq:cjs">[eq:cjs]</a> is a standard lower target. To obtain it from MTT one needs:

1.  an actual eleven-dimensional integration domain and orientation;

2.  the metric, spin structure, gravitino, and C-field from one source;

3.  the exterior differential, Hodge star, wedge product, and trace or integration functional transported by commuting maps;

4.  the relative coefficients and $`\kappa_{11}`$ normalization selected before comparison; and

5.  a proof that the upper action or flow descends to <a href="#eq:cjs" data-reference-type="ref+label" data-reference="eq:cjs">[eq:cjs]</a>, including the local supersymmetry terms.

Writing MTT symbols with the same indices does not supply these items. Likewise, varying a copied lower action correctly proves its lower equations, not that the upper MTT dynamics selected the action.

## Higher-derivative and quantum terms

The two-derivative CJS action is not the whole effective action. The one-loop gravitational coupling customarily written using $`C_3\wedge X_8(R)`$, together with related higher-derivative terms, is important for global consistency and five-brane anomaly inflow . These terms belong to a higher declared order than <a href="#eq:cjs" data-reference-type="ref+label" data-reference="eq:cjs">[eq:cjs]</a>. A record must state whether they are included, which connection defines the characteristic forms, and how the global phase is defined. They cannot be inserted schematically and then used as evidence for a complete quantum theory.

# The C-field is global differential data

## Shifted quantization

Let
``` math
\lambda=\frac12 p_1(TY).
```
In the usual convention, the M-theory flux obeys the shifted quantization law
``` math
\begin{equation}
\left[\frac{G_4}{2\pi}\right]-\frac12\lambda
\in H^4(Y;\mathbb Z)
\label{eq:shift}
\end{equation}
```
. This statement is not the assertion that one global three-form $`C_3`$ exists. A nontrivial flux class obstructs such a global potential.

The appropriate global object is a shifted differential cocycle $`\check C`$. It carries:

1.  a characteristic integral class;

2.  the curvature $`G_4`$;

3.  local three-form potentials and their higher overlap data; and

4.  gauge equivalences and, when needed, boundary trivializations.

Differential cohomology is designed to retain these integral, differential, and holonomy layers simultaneously .

## Why cohomology arithmetic is not enough

Checking <a href="#eq:shift" data-reference-type="ref+label" data-reference="eq:shift">[eq:shift]</a> at the level of cohomology is necessary but does not construct the differential cocycle, its connection data, or its quantum phase. Conversely, a globally written $`C_3`$ may describe only the topologically trivial sector. A valid MTT source theorem must therefore emit the full differential object and prove compatibility with its metric, spin, source, and boundary rows.

The existing q=79 finite-gerbe and Cech calculations show that MTT research can work with finite patching data. They concern the selected heterotic branch and do not by themselves define the eleven-dimensional C-field. Their relevance is methodological and contextual, not an automatic lift.

# Branes, pullback, and anomaly inflow

## M2 data

An M2-brane begins with an embedding
``` math
X:\Sigma_3\longrightarrow Y^{10,1}.
```
Its bosonic action has the schematic form
``` math
\begin{equation}
S_{\mathrm{M2}}
=-T_{\mathrm{M2}}\int_{\Sigma_3}
\sqrt{-\det X^\ast g}
+T_{\mathrm{M2}}\int_{\Sigma_3}X^\ast C_3,
\label{eq:m2}
\end{equation}
```
with fermionic completion and kappa symmetry in a supersymmetric background . Pullback explains the two terms after $`X`$, $`g`$, and $`C_3`$ are supplied. It does not select the embedding, charge, tension, fermions, or kappa projector.

## M5 data

An M5-brane requires an embedding $`X:\Sigma_6\to Y`$, a chiral worldvolume two-form, and a self-dual three-form field strength coupled to $`X^\ast C_3`$. A covariant Pasti–Sorokin–Tonin formulation introduces an auxiliary scalar and extra gauge symmetry to implement self-duality . The complete supersymmetric theory also requires kappa symmetry and the appropriate background constraints.

These are independent rows of Definition <a href="#def:record" data-reference-type="ref" data-reference="def:record">1</a>. An MTT pullback can transport a supplied $`C`$-field to a supplied worldvolume. It cannot create the chiral two-form, its self-duality law, or the PST gauge system merely by being a projection.

## Sources and inflow

The M2 is electrically charged and the M5 magnetically charged under the C-field. In their presence the source-free equations <a href="#eq:form-eom" data-reference-type="ref+label" data-reference="eq:form-eom">[eq:form-eom]</a> are modified by distributional or regularized currents. The M5 worldvolume theory has a gravitational anomaly whose cancellation requires careful treatment of the bulk Chern–Simons coupling and normal bundle geometry . This is not captured by the numerical equality of integrated characteristic classes alone.

In common Planck-length conventions,
``` math
2\kappa_{11}^2=(2\pi)^8\ell_p^9,\qquad
T_{\mathrm{M2}}=\frac{1}{(2\pi)^2\ell_p^3},\qquad
T_{\mathrm{M5}}=\frac{1}{(2\pi)^5\ell_p^6}.
```
For MTT these relations are lower consistency checks. A no-knob claim would also have to source the unit convention or one dimensional scale from which they follow.

# Circle reduction to massless type IIA

## The field dictionary

Suppose $`Y^{10,1}`$ is a principal circle geometry over a ten-dimensional base and all retained fields are invariant along the circle. In string-frame conventions one writes
``` math
\begin{equation}
\mathrm ds_{11}^2
=e^{-2\phi/3}\mathrm ds_{10,s}^2
+e^{4\phi/3}(\mathrm dy+C_1)^2,
\label{eq:metric-reduction}
\end{equation}
```
and locally decomposes
``` math
\begin{equation}
C_3^{(11)}
=C_3^{(10)}+B_2\wedge(\mathrm dy+C_1),
\label{eq:c-reduction}
\end{equation}
```
with convention-dependent field redefinitions. Substitution into the eleven-dimensional equations and integration over the circle produce the massless type-IIA supergravity sector. The scale dictionary is
``` math
R_{11}=g_s\ell_s,\qquad
\ell_p^3=g_s\ell_s^3 .
```
These are standard reduction relations, not consequences of an unidentified shared phase circle .

## Brane descendants and one important exclusion

Under the standard reduction:

- an unwrapped M2 gives a D2 and a wrapped M2 gives the fundamental string;

- an unwrapped M5 gives the NS5 and a wrapped M5 gives the D4;

- Kaluza–Klein momentum gives D0 charge; and

- the Kaluza–Klein monopole gives the D6 sector.

The D8-brane and Romans mass do not arise from ordinary circle reduction of massless eleven-dimensional supergravity. Version 1 included D8 in the direct descendant list; that statement is withdrawn.

## What an MTT reduction proof must add

An MTT proof must select the principal circle bundle, its radius and connection, the spin structure, the invariant truncation, and the complete field dictionary. It must then show that the upper differential and action commute with reduction. Merely observing that MTT uses a circle does not establish any of these requirements.

# The q=79 branch and the shared-circle question

## What is already available

The selected q=79 program has exact finite arithmetic and branch data, literal finite Cech witnesses, a certified finite projected HYM solution, and a selected rank-two continuum HYM witness at their declared tiers. The current heterotic string paper further records a twelve-row worldsheet contract: five rows are available, two are partial, and five remain open .

These are genuine advances in a ten-dimensional heterotic/Fu–Yau branch. They are not an eleven-dimensional compactification record. In particular, they do not yet supply:

1.  an eleven-dimensional Lorentzian spin manifold;

2.  an M-theory principal circle with radius and connection;

3.  the shifted differential C-field;

4.  the gravitino and local-supersymmetry algebra;

5.  M2/M5 embeddings, worldvolume fields, and anomaly data; or

6.  an action-preserving map from the upper q=79 source.

## The shared circle is not automatically the M-theory circle

MTT uses a shared circle or line-bundle holonomy in several encodings. That common object may become part of an M-theory lift, but equality of names or isomorphism of abstract circles is insufficient. The required statement is a connection-preserving identification
``` math
(S^1_{\mathrm{MTT}},\nabla_{\mathrm{MTT}})
\longrightarrow
(S^1_{\mathrm{M}},\nabla_{\mathrm{KK}})
```
compatible with spin structure, radius, C-field reduction, holonomy, action, and every lower bundle in which the shared line is reused. Without that intertwiner, the MTT circle remains phase or holonomy data rather than an established spacetime dimension.

The proposed double traversal and branch-orientation ideas may help select a lift or time orientation. They do not themselves prove that the compact circle is physical time, nor that it is the Kaluza–Klein circle. Physical time remains the noncompact Lorentzian ordering direction in the lower record.

## Why the heterotic branch does not automatically lift

The q=79 compactification candidate is based on a six-dimensional non-Kahler torsional Fu–Yau/Hull–Strominger geometry. An ordinary M-theory-to-IIA circle reduction is a different route. Relating the two requires a specified duality chain or eleven-dimensional geometry and a proof that bundles, fluxes, differential cocycles, anomalies, and actions are transported consistently. The corrected perturbative-string, Hull–Strominger, Calabi–Yau, and flux-audit papers delimit those lower branches without asserting this missing lift .

# Compactification to four dimensions

## A seven-dimensional source is required

A direct M-theory compactification to four dimensions needs an eleven-dimensional geometry that is, at least locally and at an appropriate scale, organized as a four-dimensional spacetime with a seven-dimensional internal sector. The internal metric, topology, singularities, fluxes, and boundary data determine the lower spectrum and couplings. Smooth special holonomy can control supersymmetry, while chiral gauge sectors generally require additional singular, boundary, or brane structure .

The equality $`11=4+7`$ is dimensional bookkeeping, not a compactification theorem. The MTT rank flag $`1<2<3`$, the local $`3\times3`$ strain decomposition, and the q=79 six-dimensional heterotic geometry are useful structural clues, but none is presently a selected seven-dimensional M-theory internal space.

## Why stabilization and prediction do not follow from flux energy

After choosing an internal geometry, the four-dimensional action contains moduli, kinetic matrices, gauge couplings, superpotentials, threshold corrections, and normalized overlap integrals. A positive flux-energy term does not by itself make the potential proper on the full moduli space; runaway, decompactification, and boundary directions may remain. An isolated point in a finite ansatz is not automatically a globally selected vacuum.

Accordingly, Version 1’s claims of automatic coercivity, discrete vacuum selection, three families, normalized Yukawa couplings, soft terms, and cosmological predictions are removed. They may be reintroduced only after a selected eleven-dimensional source, complete reduction, normalized mode basis, and controlled effective action exist. Current MTT Standard Model profile results belong to their own declared lower tier and are not evidence for this missing M-theory derivation.

# Current status and completion contract

## Eleven-dimensional source rows

<div id="tab:status">

| Row | Required object | Current MTT status |
|:---|:---|:---|
| Spacetime | Oriented Lorentzian spin $`Y^{10,1}`$, boundary data, domains | Open: no selected q=79 eleven-dimensional manifold or lift. |
| Fields | Vielbein, gravitino, spin bundle, differential C-field | Open: finite carriers do not emit the full CJS multiplet. |
| Action | Normalized action, products, Hodge star, local supersymmetry | Open under B.ACTION.01. |
| Sources | M2/M5 embeddings, charges, tensions, worldvolume fields | Open: pullback transports but does not select these data. |
| Global consistency | Shifted quantization, Bianchi identities, anomalies, inflow | Standard lower results available; no same-source MTT certificate. |
| Circle reduction | Principal circle, radius, connection, spin structure, truncation | Open: the shared phase circle is not yet identified with $`S^1_{\rm M}`$. |
| Quantum status | Measure, state space, observables, renormalized or nonperturbative rule | Open beyond declared classical or conditional effective formulas. |
| Evaluation | Connection- and action-preserving commuting map | Open: no complete factorization certificate. |

The current eleven-dimensional completion cutset. “Standard lower results available” means the conventional mathematics is known; it does not mean MTT has selected its source.

</div>

## Relationship to the active research frontier

The current B.ACTION.01 blocker depends on two upstream constructions:

1.  a physical visible–hidden Hull–Strominger endpoint on the selected q=79 branch; and

2.  execution of the selected continuum operator rather than only its finite sparsity pattern.

Its exit certificate is one upper differential/action object whose automorphisms, zero modes, transferred products, and finite operators reproduce the accepted lower structures by certified commuting maps.

Closing those dependencies would not automatically prove M-theory. It would provide the right kind of upper action language from which the eleven-dimensional rows in <a href="#tab:status" data-reference-type="ref+label" data-reference="tab:status">1</a> could then be sourced. The paper’s contribution is to make that next test finite and typed.

## Minimal proof program

A credible MTT-to-M-theory result now has the following order.

1.  Construct one selected upper differential/action object and certify its products, automorphisms, domains, and normalization.

2.  Construct an eleven-dimensional Lorentzian spin target and a connection-preserving map from the shared MTT data.

3.  Emit the complete CJS multiplet and prove action and local supersymmetry factorization at a declared derivative order.

4.  Emit the shifted differential C-field, including global phase and source-modified Bianchi data.

5.  Add M2/M5 sources only after their embeddings, normal bundles, worldvolume fields, kappa symmetry, and anomaly inflow are sourced.

6.  Prove the chosen circle reduction or other duality chain, rather than identifying circles by dimension alone.

7.  Compute held-out lower observables and verify <a href="#eq:factor" data-reference-type="ref+label" data-reference="eq:factor">[eq:factor]</a> with a full convention and uncertainty ledger.

The first five steps would establish a selected eleven-dimensional low-energy realization. Full quantum M-theory and realistic four-dimensional phenomenology would remain further layers.

# Disposition of Version 1 claims

<div id="tab:disposition">

| Version 1 claim | Version 2 status | Reason |
|:---|:---|:---|
| Projection derives the eleventh dimension | Withdrawn | Projector axioms admit inequivalent targets; a selected spin circle geometry is additional data. |
| Full 11D field content is $`(g,C_3)`$ | Corrected | The CJS multiplet also contains the gravitino and local supersymmetry. |
| MTT derives the complete 11D action | Reclassified | The CJS action is a standard conditional lower target; action factorization remains open. |
| Shifted flux law follows automatically | Reclassified | <a href="#eq:shift" data-reference-type="ref+label" data-reference="eq:shift">[eq:shift]</a> is imported from standard M-theory and requires a global differential C-field. |
| Projection produces M2/M5 actions | Withdrawn | Embeddings, worldvolume fields, self-duality, kappa symmetry, charges, and tensions are independent rows. |
| M5 anomaly inflow is derived | Reclassified | Standard inflow is a lower consistency gate; no MTT same-source construction exists. |
| All IIA branes descend, including D8 | Corrected | Ordinary massless circle reduction supplies the standard M2/M5 and KK descendants, not Romans mass or D8. |
| Flux energy guarantees stabilization | Withdrawn | Positivity does not imply properness or global uniqueness on moduli space. |
| Three families, Yukawas, soft terms, cosmology | Removed | No selected seven-dimensional geometry or normalized four-dimensional reduction was constructed. |
| No continuous parameters remain | Withdrawn | Radius, volume, metric, flux, normalization, and moduli require a source or remain input data. |

Claim-by-claim resolution of the former first-principles language.

</div>

# Discussion

## What survives conceptually

The central MTT intuition survives in a sharper form. A common upper closure structure could, in principle, produce gravity, higher-form gauge data, branes, and lower effective theories as different projections of one source. Eleven-dimensional supergravity is especially useful because its field content and nonlinear couplings provide a demanding test of that idea. The test is now explicit: the same upper source must produce the metric, spinor, C-field, action, sources, global shifts, and reduction maps without changing normalization or importing observed lower data.

This is more informative than placing familiar equations after a projection. Failure of one row identifies the missing mathematical object. Success of all rows would establish a genuine common-source theorem rather than a dictionary.

## What the present paper achieves

The paper supplies three durable results.

1.  It defines the complete eleven-dimensional record against which MTT claims can be audited.

2.  It proves the conditional realization theorem as a commuting evaluation statement with declared scope.

3.  It proves that projector and pullback axioms alone cannot select the required spacetime, C-field, branes, or action.

It also corrects the M-theory/11D-supergravity distinction, restores the gravitino and differential C-field, removes the D8 descent error, and separates q=79 heterotic evidence from an unproved eleven-dimensional lift.

## What it does not achieve

No new eleven-dimensional background is constructed here. The CJS action, flux law, brane theories, and anomaly inflow are not re-proved as MTT theorems. The paper does not define nonperturbative M-theory, select a seven-dimensional compactification, stabilize its moduli, or predict four-dimensional masses and couplings. These limits are part of the result, not footnotes to it.

# Conclusion

MTT can claim an eleven-dimensional low-energy realization only when one selected upper state emits a complete spin, field, action, source, global, quantum-scope, and reduction record and when its observable evaluation factors through that lower theory. This paper proves that conditional statement and proves why projection alone is insufficient.

The standard mathematics remains fully useful. The CJS action fixes the classical lower target. Shifted differential cohomology fixes the global C-field requirement. M2/M5 theory and anomaly inflow fix the source gates. Circle reduction fixes the massless type-IIA dictionary. Existing q=79 and HYM results show that MTT has substantial finite and geometric structure, but they do not yet constitute this eleven-dimensional source.

The next meaningful advance is therefore not another formal rewriting of the 11D equations. It is the selected upper differential/action object required by B.ACTION.01, followed by a connection-preserving eleven-dimensional source map. If that construction succeeds, the contract developed here turns the claim into a finite sequence of verifiable commuting diagrams.

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

The exact q79 arithmetic, finite rank-two Cech witness, and rank-two Wiener-contraction certificate are contextual evidence for an adjacent selected heterotic branch. They do not directly construct an eleven-dimensional Lorentzian spin manifold, M-theory circle, shifted differential C-field, gravitino and local supersymmetry, M2/M5 source data, anomaly inflow, a selected seven-dimensional compactification, or the connection- and action-preserving MTT-to-eleven-dimensional evaluation map.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Corpus-state cross-checks

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A07/literal_cech_witness` (**DERIVED_EXACT**): Literal 81-entry, 729-cocycle finite Cech witness.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
