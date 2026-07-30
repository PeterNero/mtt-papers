---
abstract: |
  A Calabi–Yau compactification is not specified by a six-dimensional metric alone. It also requires topology, complex and Kähler data, gauge bundles and connections, anomaly cancellation, a supersymmetry convention, and a declared worldsheet or effective-field-theory approximation. This paper asks what Modal Triplet Theory (MTT) presently establishes about that complete object. We define a typed realization map from an upper MTT configuration to a lower Calabi–Yau compactification record and prove the corresponding conditional realization theorem: if one MTT source emits every required row and its reduction factors through the standard compactification functional, then both descriptions give the same declared lower data. This is an exact embedding statement, not a derivation or selection of a unique Calabi–Yau vacuum. We also isolate the analytic conditions under which spectral gaps, harmonic projectors, and commuting modal operators are available. A positive gap and bounded harmonic projector hold for each fixed compact elliptic problem; uniformity over moduli and operator commutation require additional non-collapsing or product hypotheses. A flat six-torus gives an elementary compatibility witness but not realistic four-dimensional phenomenology. The selected $`q=79`$ Fu–Yau program is a distinct non-Kähler torsional branch and cannot serve as a proof of a strict Calabi–Yau corner. The outcome is a precise and reusable realization contract, with unique-vacuum selection, moduli stabilization, and phenomenological prediction retained as independent open problems.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 5490709d5571e2621bca3b483faac66dec52cbc36ad7375b68f76d1e4ad47e8c
paper_id: modal-triplet-theory-from-mtt-to-calabi-yau-compactific-1061378d
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and Calabi–Yau Compactification:
  A Conditional Realization Map and Its Selection Boundary
zenodo_doi: 10.5281/zenodo.21707791
zenodo_record_id: 21707791
zenodo_url: "https://zenodo.org/records/21707791"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1 and its assertion that MTT had already proved and selected a Calabi–Yau corner with the same worldsheet theory and four-dimensional phenomenology as a standard compactification.

The former paper treated vanishing torsion classes as though MTT had derived them, inferred a unique compactification from compatibility conditions, and used a smooth metric path to change Lens–Nil topology into torus topology. It also asserted generic commutation of bundle Laplacians, imported worldsheet and low-energy data without their source assumptions, and described an omitted $`T^6/\mathbb Z_3`$ calculation as a worked example.

This revision replaces those claims with a typed realization contract. It separates lower Calabi–Yau existence, heterotic bundle and anomaly data, worldsheet completion, four-dimensional reduction, moduli stabilization, and MTT source selection. The spectral statements are restricted to their valid fixed-background or uniformly controlled-family forms, and operator commutation is proved only for a genuine product factorization.

Calabi–Yau geometry is retained as a legitimate lower realization target. Standard Ricci-flat, HYM, spectral, cohomological, and dimensional-reduction machinery remains available once its full hypotheses are supplied.

No current MTT theorem selects a unique Calabi–Yau topology, complex structure, Kähler class, stable visible–hidden bundle pair, worldsheet CFT, or stabilized four-dimensional vacuum. The selected $`q=79`$ physical Hull–Strominger endpoint remains a separate open construction.

</div>

# The question and the corrected answer

## Why Calabi–Yau geometry is a natural target

Compact Calabi–Yau threefolds organize a large and mathematically controlled class of ten-to-four-dimensional string compactifications. Their complex geometry supports holomorphic bundles and cohomological spectrum calculations; Yau’s theorem supplies a Ricci-flat Kähler metric in each chosen Kähler class; and dimensional reduction turns the chosen geometric record into a four-dimensional effective theory .

MTT is organized differently. It begins with an upper carrier, admissibility conditions, projection or decoding maps, and fixed-point dynamics. The natural question is therefore not whether the word “Calabi–Yau” can be attached to an MTT parameter limit. It is whether one selected upper object emits the complete lower record needed by a compactification and whether the declared reduction respects that record.

## What this paper establishes

This paper owns three limited results.

1.  It defines the complete lower record that an MTT-to-Calabi–Yau map must emit.

2.  It proves the conditional realization statement obtained when every row of that record and the reduction factorization are supplied.

3.  It identifies which common MTT analytic requirements are automatic for a fixed compact elliptic problem and which require extra uniformity or product assumptions.

The result is a compatibility and bookkeeping theorem. It does not construct the missing MTT source or choose one point in the Calabi–Yau landscape.

## Logical dependency map

The corrected order is
``` math
\begin{split}
\text{selected upper MTT state}
&\longrightarrow \text{typed lower geometric record}\\
&\longrightarrow \text{Calabi--Yau and bundle equations}\\
&\longrightarrow \text{worldsheet completion at a declared order}\\
&\longrightarrow \text{four-dimensional reduction}\\
&\longrightarrow \text{stabilized vacuum and observables}.
\end{split}
```
An implication may be used only after its own hypotheses have been checked. In particular, a Ricci-flat metric does not choose a bundle, a bundle does not by itself define an exact conformal field theory, and a massless four-dimensional spectrum does not stabilize its moduli.

# The lower object that must be realized

## Geometric Calabi–Yau datum

<div id="def:cy-record" class="definition">

**Definition 1** (Geometric Calabi–Yau record). A geometric Calabi–Yau record in complex dimension three is
``` math
\mathcal C_{\mathrm{geom}}
  =(X,I,\Omega,[\omega],g),
```
where $`X`$ is a compact connected smooth six-manifold, $`I`$ is an integrable complex structure, $`\Omega`$ is a nowhere-vanishing holomorphic $`(3,0)`$-form, $`[\omega]`$ is a Kähler class, and $`g`$ is the Ricci-flat Kähler metric in that class. We use “Calabi–Yau” in the inclusive sense $`\operatorname{Hol}(g)\subseteq SU(3)`$; exact $`SU(3)`$-holonomy is a separate condition when four-dimensional $`N=1`$ supersymmetry rather than an enhanced theory is intended.

</div>

For a fixed compact Kähler manifold with $`c_1(X)=0`$, Yau’s theorem gives a unique Ricci-flat Kähler metric in each fixed Kähler class . This is not uniqueness of the manifold, complex structure, or Kähler class. Those choices vary in families and can change the resulting physics.

An equivalent differential-geometric presentation uses an $`SU(3)`$ structure $`(\omega,\Omega)`$. If
``` math
\mathrm d\omega=0,\qquad \mathrm d\Omega=0,
```
with the usual algebraic compatibility and positivity conditions, then the structure is torsion-free and the metric has holonomy contained in $`SU(3)`$. The vanishing of intrinsic torsion is a test on a supplied structure; it does not show that MTT has emitted such a structure.

## Heterotic data are additional

For the heterotic interpretation emphasized in the MTT corpus, the lower record must be enlarged to
``` math
\mathcal C_{\mathrm{het}}=
(X,I,\Omega,\omega,g;
 V_{\mathrm{vis}},A_{\mathrm{vis}};
 V_{\mathrm{hid}},A_{\mathrm{hid}};
 \nabla,H,\Phi,\mathcal G_B).
```
Here $`V_{\mathrm{vis}}`$ and $`V_{\mathrm{hid}}`$ are holomorphic gauge bundles, $`A_{\mathrm{vis}}`$ and $`A_{\mathrm{hid}}`$ are unitary connections, $`\nabla`$ is a declared connection on $`TX`$, $`H`$ is the three-form flux, $`\Phi`$ is the dilaton, and $`\mathcal G_B`$ denotes the global $`B`$-field or gerbe data.

In the strict unwarped Calabi–Yau limit one normally imposes
``` math
H=0,\qquad \mathrm d\Phi=0,\qquad
F_a^{0,2}=0,\qquad F_a\wedge\omega^2=0
\quad(a=\mathrm{vis},\mathrm{hid}),
```
together with the anomaly condition
``` math
0=\mathrm dH=\frac{\alpha'}4
\left(\operatorname{tr}R_\nabla\wedge R_\nabla
-\operatorname{tr}F_{\mathrm{vis}}\wedge F_{\mathrm{vis}}
-\operatorname{tr}F_{\mathrm{hid}}\wedge F_{\mathrm{hid}}\right)
```
in one fixed trace convention, possibly modified by a declared five-brane class. A topological equality of second Chern classes is necessary in the usual setting but does not automatically identify the differential four-form representatives.

The Donaldson–Uhlenbeck–Yau correspondence supplies HYM connections on slope-polystable holomorphic bundles; it does not turn an arbitrary smooth bundle into a supersymmetric gauge background . The visible and hidden bundles, their stability chambers, and the tangent-connection convention must therefore be part of the input or of a separate derivation.

## Worldsheet and effective-theory rows

Target-space supergravity equations are not identical to an exact worldsheet construction. A heterotic model must additionally specify the sigma-model field content, gauge bundle, anomaly cancellation, GSO projection, modular invariance, and the perturbative order at which conformal invariance is claimed. The standard embedding has a familiar $`(2,2)`$ description; general stable bundles lead instead to $`(0,2)`$ models. Equality of target metrics alone does not prove equality of the complete CFT.

Likewise, a four-dimensional theory requires a declared reduction scheme, normalizations, quantum corrections, and an energy range. Its massless spectrum depends on bundle-valued cohomology, not only on the Hodge numbers of $`X`$. Its couplings depend on normalized modes and moduli. Stabilizing those moduli is a further dynamical problem .

<div id="tab:rows">

| Row | Data or certificate required |
|:---|:---|
| Topology | Compact complex threefold, canonical bundle and global quotient or resolution data. |
| Metric | Kähler class and its Ricci-flat representative; exact holonomy if required. |
| Gauge | Holomorphic visible and hidden bundles, stability chamber, HYM connections and structure-group embedding. |
| Anomaly | One trace convention, tangent connection, differential Bianchi identity and global $`B`$-field data. |
| Supersymmetry | Declared ten-dimensional theory, spinors, flux/dilaton regime and perturbative order. |
| Worldsheet | CFT or sigma-model completion, anomalies, GSO and modular data. |
| Four dimensions | Reduction functional, normalized zero modes, corrections and validity scale. |
| Stabilization | Potential or dynamics fixing the relevant geometric and bundle moduli. |
| MTT source | One selected upper carrier that emits all preceding rows and preserves their connections under reduction. |

The rows that were conflated in Version 1.

</div>

# The MTT realization contract

## Typed source and reduction maps

Let $`\mathcal U_{\mathrm{MTT}}`$ be a declared upper configuration space and let
``` math
\mathcal R_{\mathrm{CY}}:\mathcal U_{\mathrm{MTT}}\dashrightarrow
\mathcal M_{\mathrm{CY}}
```
be a possibly partial map into the space of records listed in <a href="#tab:rows" data-reference-type="ref+label" data-reference="tab:rows">1</a>. The map is typed: it must say which upper fields produce the complex structure, Kähler form, bundles, connections, flux, dilaton, and global data. Isomorphic bundles without an identified connection-preserving map are not yet the same physical row.

Let $`\mathcal D_{\mathrm{std}}`$ denote a standard compactification or dimensional-reduction functional on its domain, and let $`\mathcal D_{\mathrm{MTT}}`$ be the lower description assigned by MTT. The factorization condition is
``` math
\mathcal D_{\mathrm{MTT}}
=\mathcal D_{\mathrm{std}}\circ\mathcal R_{\mathrm{CY}}
\quad\text{on a declared domain } \mathcal U_0\subseteq\mathcal U_{\mathrm{MTT}}.
```
This equation is the precise replacement for the old phrase “MTT produces exactly the same physics.”

<div id="def:complete-realization" class="definition">

**Definition 2** (Complete MTT–CY realization). An upper state $`u_\ast\in\mathcal U_0`$ is a complete MTT–CY realization at a declared perturbative order if:

1.  $`\mathcal R_{\mathrm{CY}}(u_\ast)`$ is defined and supplies every required row of <a href="#tab:rows" data-reference-type="ref+label" data-reference="tab:rows">1</a>;

2.  the geometric, HYM, anomaly, and supersymmetry equations hold in one common convention on that one record;

3.  the worldsheet and effective-theory claims are restricted to the orders for which their completion data have been supplied; and

4.  the factorization equation for $`\mathcal D_{\mathrm{MTT}}`$ holds at $`u_\ast`$.

</div>

<div id="thm:conditional-realization" class="theorem">

**Theorem 3** (Conditional Calabi–Yau realization). *If $`u_\ast`$ satisfies <a href="#def:complete-realization" data-reference-type="ref+label" data-reference="def:complete-realization">2</a>, then $`\mathcal R_{\mathrm{CY}}(u_\ast)`$ is a Calabi–Yau compactification record at the declared order, and every observable in the domain of $`\mathcal D_{\mathrm{std}}`$ satisfies
``` math
\mathcal D_{\mathrm{MTT}}(u_\ast)
=\mathcal D_{\mathrm{std}}\!\left(\mathcal R_{\mathrm{CY}}(u_\ast)\right).
```*

</div>

<div class="proof">

*Proof.* The first two hypotheses place the lower record in the domain of the standard compactification functional. The third fixes the approximation level and prevents a target-space solution from being promoted to an exact worldsheet statement. The fourth hypothesis is precisely the displayed identity. No existence or uniqueness assertion beyond the supplied record is used. ◻

</div>

<div class="remark">

*Remark 4* (Why the theorem matters). The theorem is intentionally conditional. Its value is that it identifies the exact upstream construction that would turn compatibility into a derivation. Merely finding parameters for which a written torsion class vanishes does not satisfy the source-map or factorization rows.

</div>

## What realization does not imply

Even a complete realization does not by itself show:

- that the realized topology or bundle is unique;

- that the corresponding fixed point attracts generic initial data;

- that a preparation or branch law selects it physically;

- that all moduli are stabilized; or

- that its low-energy parameters agree with experiment.

These are higher rungs of the selection ladder developed in the companion heterotic-selection paper . They are not reproved here.

# Analytic compatibility: what is automatic and what is not

## A fixed compact background

<div id="prop:fixed-spectrum" class="proposition">

**Proposition 5** (Fixed-background spectral admissibility). *Let $`L`$ be a nonnegative self-adjoint elliptic operator of Laplace type on a Hermitian vector bundle over a fixed compact manifold. Then $`L`$ has discrete spectrum with finite-dimensional kernel,
``` math
\lambda_\ast
=\min\bigl(\operatorname{Spec}(L)\setminus\{0\}\bigr)>0,
```
and the orthogonal projector $`P_{\operatorname{Ker}L}`$ extends boundedly on every Sobolev space $`H^s`$.*

</div>

<div class="proof">

*Proof.* Compact resolvent gives a discrete spectrum of finite multiplicity with no finite accumulation point. Elliptic regularity makes the kernel smooth and finite dimensional. The spectral projector is therefore smoothing of finite rank and is bounded on all Sobolev scales. ◻

</div>

This proposition supports a fixed-background MTT gap and projector check. It does not supply one numerical gap uniformly over all complex structures, Kähler classes, bundle moduli, or degenerating metrics.

## Uniformity over a family

For a parameter family $`L_t`$, a uniform bound $`\inf_t\lambda_\ast(L_t)>0`$ requires a controlled parameter domain. Typical sufficient hypotheses include precompact bounded geometry, uniformly elliptic coefficients, fixed operator domain, and no jump in kernel dimension. Degeneration, collapse, or an eigenvalue crossing zero destroys the claimed uniform constant. Thus a “thick region” must be specified and certified; compactness of each fiber separately is not enough.

## When modal Laplacians commute

<div id="lem:product-commutation" class="lemma">

**Lemma 6** (Exact product commutation). *Let
``` math
X=X_1\times X_2\times X_3,\qquad
E=E_1\boxtimes E_2\boxtimes E_3
```
carry product metrics and product connections. On the Hilbert tensor product, define
``` math
L_1=L_{E_1}\otimes I\otimes I,\quad
L_2=I\otimes L_{E_2}\otimes I,\quad
L_3=I\otimes I\otimes L_{E_3}.
```
Then the self-adjoint closures of $`L_i`$ strongly commute, their spectral projectors commute, and the product Laplacian is
``` math
L_E=L_1+L_2+L_3.
```*

</div>

<div class="proof">

*Proof.* Each operator acts on a different tensor factor. Their spectral measures are tensor products with the identity measures on the other factors, so the spectral projections commute. The product formula follows on the algebraic tensor core and extends to the self-adjoint closure. ◻

</div>

This lemma does not apply to three arbitrary connections over the same base. For a tensor-product bundle on one manifold, covariant derivatives act along the same tangent directions and the rough Laplacian generally contains mixed terms. Commutation must then be calculated, not inferred from notation. Moreover, resolving an orbifold usually destroys exact product factorization even when a torus limit had it.

## HYM compatibility is conditional

If holomorphic bundles $`E_i`$ are HYM in one Kähler chamber, their tensor product connection has curvature
``` math
F_{E_1\otimes E_2}
=F_{E_1}\otimes I+I\otimes F_{E_2}.
```
Its contracted curvature is the sum of the two central HYM constants. This is a useful construction, but it does not establish stability, the desired structure group, anomaly cancellation, or a visible-sector index. Those remain separate rows.

# An exact compatibility witness and its limits

## The flat six-torus

Let
``` math
X=T^2_1\times T^2_2\times T^2_3
```
with complex coordinates $`z^1,z^2,z^3`$,
``` math
\omega=\frac{\mathrm i}{2}\sum_{a=1}^3\mathrm dz^a\wedge\mathrm d\bar z^a,
\qquad
\Omega=\mathrm dz^1\wedge\mathrm dz^2\wedge\mathrm dz^3.
```
Then $`\mathrm d\omega=\mathrm d\Omega=0`$, the product metric is flat, and the scalar Laplacian splits into three strongly commuting factors. With trivial flat visible, hidden, and tangent connections and $`H=0`$, the differential Bianchi identity vanishes term by term. This gives a completely explicit lower compatibility witness for the geometric, spectral, product, and leading-order anomaly rows.

The witness is deliberately modest. The torus has holonomy strictly smaller than $`SU(3)`$, produces enhanced supersymmetry, and the trivial gauge choice does not yield a chiral Standard-Model-like spectrum. It also does not prove that an MTT source emits the record. It shows only that the lower target class is nonempty and that MTT-style analytic conditions are not mutually inconsistent with a simple Calabi–Yau background.

## Why the former orbifold example is withdrawn

The previous version named a $`T^6/\mathbb Z_3`$ resolution but omitted the promised construction. A valid orbifold model would have to specify the group action, fixed loci, crepant resolution, Kähler chamber, gauge shift or bundle, twisted sectors, anomaly constraints, and the relation between orbifold and resolved descriptions . Exact product commutation need not persist after resolution. Without those rows there is no worked compactification and no parameter map to audit.

# What Calabi–Yau machinery may be inherited

## Massless fields

Once $`X`$ and a holomorphic bundle $`V`$ are supplied, candidate massless fields are organized by bundle-valued cohomology groups. For example, the multiplicity of a representation associated with a bundle $`U`$ is computed from groups such as $`H^1(X,U)`$, subject to the chosen embedding and conventions. This is a conditional calculation on $`(X,V)`$; Hodge numbers of $`X`$ alone do not determine the charged spectrum.

## Yukawa couplings

For normalized harmonic representatives $`\psi_i`$, a holomorphic Yukawa coupling has the schematic form
``` math
Y_{ijk}\sim
\int_X\Omega\wedge
\psi_i\wedge\psi_j\wedge\psi_k,
```
with bundle contractions and normalization factors fixed by the model. Writing $`Y_{ijk}=Y_{ijk}(\Theta_{\mathrm{MTT}})`$ is justified only after the source map derives $`X,\Omega,V,\psi_i`$ and their normalization from $`\Theta_{\mathrm{MTT}}`$. Otherwise the equation is a change of variables, not a prediction.

## Gauge and gravitational couplings

Dimensional reduction similarly yields volume- and dilaton-dependent gauge and gravitational couplings. Such formulas become MTT predictions only if the relevant volume, dilaton, normalization, and threshold data are selected upstream. A spectral gap can control a Kaluza–Klein scale on a fixed background, but it does not by itself fix the overall compactification scale.

## Moduli and stabilization

Yau’s theorem leaves the complex and Kähler moduli unspecified. Bundle holomorphy can obstruct some complex-structure deformations through the Atiyah map, and explicit models can stabilize subsets of moduli . Other moduli require additional perturbative or nonperturbative effects. Therefore “the MTT fixed point is stable” and “all compactification moduli are stabilized” are different statements about different operators.

## Mirror symmetry and thresholds

Mirror symmetry, threshold corrections, and special geometry may be studied after a model and approximation scheme are fixed. They are not automatic consequences of a three-block notation. In particular, an MTT duality map must be constructed and shown to intertwine the relevant period, bundle, and quantum data before it can be identified with a mirror map.

# Relation to the $`q=79`$ and Lens–Nil programs

## Three geometries that must not be identified

<div class="center">

| Object | Geometric type | Correct role |
|:---|:---|:---|
| Strict CY branch | Compact Ricci-flat Kähler threefold, normally $`H=0`$ in the unwarped heterotic limit | A possible lower realization target for the contract in <a href="#sec:contract" data-reference-type="ref+label" data-reference="sec:contract">3</a>. |
| $`q=79`$ Fu–Yau branch | Non-Kähler complex threefold with torsion and nonzero flux | The strongest current target for the selected heterotic program; it belongs to the Hull–Strominger problem, not to a strict Calabi–Yau corner . |
| Lens–Nil construction | Auxiliary balanced or rank/operator comparison model; the audited almost-complex model is non-integrable | Useful for local calculations or filtration intuition, but not a physical CY or Hull–Strominger proof source . |

</div>

A smooth family of metrics on one fixed manifold cannot change its diffeomorphism type. Consequently, “flattening” Lens and Nil factors does not turn their manifold into a torus or a Calabi–Yau threefold. A topology change, surgery, quotient, resolution, or entirely new carrier would have to be constructed explicitly.

## What the current repository results contribute

The current MTT program has exact finite $`q=79`$ arithmetic, a literal finite rank-two Cech witness, a certified finite projected HYM approximation, and a selected rank-two continuum HYM witness with a Wiener contraction certificate. These are substantial results at their declared tiers. They do not provide a Calabi–Yau topology, a rank-three visible bundle, a hidden bundle, or an MTT-to-CY source map. They therefore appear here as contextual evidence and reusable tools, not as direct proof of <a href="#thm:conditional-realization" data-reference-type="ref+label" data-reference="thm:conditional-realization">3</a>.

The companion Hull–Strominger paper states the required flow-intertwining bridge . The physical visible–hidden endpoint still requires one common carrier with the required bundles, HYM connections, anomaly identity, and global flux data.

# Selection and completion boundary

## Compatibility, existence, and selection

Three claims must remain distinct.

<div class="description">

The lower equations and MTT analytic requirements can hold simultaneously. The torus witness establishes this in a simple non-phenomenological case.

One selected upper state emits a complete lower record and the MTT reduction factors through the standard compactification. This is the hypothesis of <a href="#thm:conditional-realization" data-reference-type="ref+label" data-reference="thm:conditional-realization">3</a>; it has not yet been constructed.

An MTT preparation, evolution, or branch law chooses that realization among alternatives. This requires more than equation solving or local isolation.

</div>

## A completion contract

To promote the present paper from a conditional map to a physical Calabi–Yau result, a future construction must provide:

1.  a selected compact complex threefold $`X`$, not merely a local $`SU(3)`$-structure ansatz;

2.  an MTT-derived complex structure, Kähler class, holomorphic volume form, and Ricci-flat metric;

3.  explicit visible and hidden holomorphic bundles in a common stability chamber, with HYM connections;

4.  the differential anomaly identity and global $`B`$-field data in one convention;

5.  a source map preserving the relevant connections and holonomies;

6.  the worldsheet completion and perturbative order actually claimed;

7.  a dimensional-reduction factorization with normalized modes; and

8.  a stabilization and selection mechanism if a unique physical vacuum is claimed.

These rows are deliberately stronger than a list of matching dimensions or isomorphic abstract groups. They identify the actual object on which the calculation is performed.

# Claim audit and conclusion

## Disposition of Version 1 claims

<div class="center">

| Former claim | Status | Version 2 resolution |
|:---|:---|:---|
| MTT proves a Calabi–Yau corner | Withdrawn | Replaced by a conditional typed realization theorem. |
| Vanishing torsion selects a unique CY | Withdrawn | It tests a supplied structure; Yau uniqueness is only within a fixed Kähler class. |
| MTT and standard worldsheet theories coincide | Conditional | Requires the full sigma-model/CFT, anomaly, GSO and modular rows. |
| The four-dimensional EFT is automatically identical | Conditional | Holds only under the explicit reduction factorization. |
| Compactness gives a uniform spectral gap over moduli | Corrected | A fixed background has a gap; a family needs uniform control. |
| Three bundle Laplacians commute generically | Withdrawn | Exact commutation is proved for a genuine product carrier. |
| Lens–Nil deforms smoothly to a CY torus | Withdrawn | Metric deformation cannot change topology. |
| $`T^6/\mathbb Z_3`$ is a worked phenomenological example | Withdrawn | The required resolution, bundle and spectrum data were absent. |
| CY formulas give new MTT predictions | Withdrawn | They are conditional evaluation formulas until their inputs are selected upstream. |

</div>

## Conclusion

Calabi–Yau geometry remains a valuable realization target for MTT, but the correct relation is now precise. Standard geometry can certify a lower record once topology, metric, bundle, anomaly, worldsheet, and reduction data are supplied. MTT contributes a proposed upper origin and selection mechanism. The bridge between them is the typed source map and reduction factorization of <a href="#sec:contract" data-reference-type="ref+label" data-reference="sec:contract">3</a>.

This reformulation preserves the useful mathematical content while removing an unsupported claim of uniqueness. It also clarifies the research choice: a strict Calabi–Yau branch would require a new selected source record, whereas the current $`q=79`$ program is pursuing the different, non-Kähler Fu–Yau/Hull–Strominger route. Neither branch should borrow the other’s topology as a proof shortcut.

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

The exact q79 arithmetic, finite rank-two Cech witness, and rank-two Wiener-contraction certificate are contextual evidence for adjacent non-Kahler heterotic work. They do not directly prove a strict Calabi-Yau topology, metric, stable visible-hidden bundle pair, MTT-to-CY source map, worldsheet completion, or stabilized four-dimensional vacuum.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Corpus-state cross-checks

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A07/literal_cech_witness` (**DERIVED_EXACT**): Literal 81-entry, 729-cocycle finite Cech witness.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
