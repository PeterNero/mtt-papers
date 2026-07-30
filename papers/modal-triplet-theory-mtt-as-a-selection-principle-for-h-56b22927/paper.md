---
abstract: |
  Heterotic compactification papers often use the word “selection” for several different mathematical achievements: satisfying projected field equations, finding an isolated point in a finite ansatz, proving attraction under a specified flow, or assigning the realized vacuum. These implications are not equivalent. We formulate a selection ladder for Modal Triplet Theory (MTT) and the Hull–Strominger system. A finite invariant residual proves a full solution only when the tested residual is complete on the ansatz and every discarded equation vanishes. An isolated ansatz solution need not be unique in the full configuration space. Attraction requires an actual evolution and a basin estimate, while physical vacuum selection additionally requires a preparation law, branch rule, or equivalent source data. We apply this distinction to two former case studies. The diagonal Iwasawa geometry retains valid local balanced and torsion calculations, but the printed rank-three bundle, anomaly match, generation count, and normalized Yukawa do not survive the global bundle audit. The Lens–Nil model is non-integrable and therefore is not a Hull–Strominger compactification. The exact $`q=79`$ arithmetic branch, finite Cech data, and selected rank-two HYM certificates remain meaningful at their declared tiers, but they do not yet select a physical visible–hidden compactification. The result is a rigorous vocabulary and completion contract, not a claim that the heterotic landscape has already been uniquely selected.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 4501582a4a3483668d18eba74773813fc8d4e23e4863b271270f1454f2f9f4f6
paper_id: modal-triplet-theory-mtt-as-a-selection-principle-for-h-56b22927
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and Heterotic Vacuum Selection:
  What Finite Ansatz Calculations Prove, What Attraction Adds,
  and What Physical Selection Still Requires
zenodo_doi: 10.5281/zenodo.21707551
zenodo_record_id: 21707551
zenodo_url: "https://zenodo.org/records/21707551"
---

# Revision note: Version 2

#### Supersedes.

Version 1, DOI [10.5281/zenodo.17072927](https://doi.org/10.5281/zenodo.17072927).

#### Reason.

The former paper defined its fixed-point consistency condition by the compactification equations themselves and then called their componentwise solution a selection theorem. It also inherited invalid Iwasawa bundle and Yukawa claims and treated a non-integrable Lens–Nil structure as a heterotic compactification.

#### Resolution.

This version separates projected consistency, full equation closure, ansatz-local isolation, dynamical attraction, and physical selection. It proves the exact implication structure, imports the audited status of the two case studies, retains the current $`q=79`$ finite evidence at its stated tier, and identifies the remaining physical selection certificate. Revision history is kept here rather than in the abstract.

#### Retained content.

The diagonal Iwasawa balanced geometry and local torsion calculation, the usefulness of invariant residual tests, and the exact finite $`q=79`$, Cech, and rank-two HYM evidence are retained at their declared scope.

#### Remaining boundary.

A physical compactification-selection claim still requires the common rank-three visible–hidden Fu–Yau tuple, its differential Bianchi and gerbe data, the connection-preserving MTT bridge, an attraction domain, and a source or preparation rule.

# Why the word selection needs a type

The vacuum problem is not merely to solve a set of equations. A field configuration may solve the equations in a restricted family but fail an equation omitted by that family. It may be a genuine solution but be one among many disconnected branches. It may be isolated but dynamically unstable. It may be attracting but reached only from a small set of initial conditions. Finally, a theory may identify all basins without supplying a law that says which basin is realized.

These distinctions matter especially in heterotic compactification. The Hull–Strominger system couples complex geometry, a Hermitian form, a holomorphic volume form, visible and hidden holomorphic bundles, HYM connections, torsion, and the differential Green–Schwarz identity on one common compact complex threefold . Solving two scalar coefficients in a left-invariant truncation is useful, but it is not automatically a construction of that global tuple.

The first version of this paper obscured this point. Its “FCC” condition was defined to contain balance, primitivity, quantization, and the Bianchi identity. The statement that FCC was equivalent to those same componentwise equations was therefore a correct identity of definitions, not a mechanism selecting one physical vacuum. The purpose of the present version is to say exactly what each layer does prove.

# The lower target: one Hull–Strominger tuple

Let $`X`$ be a compact complex threefold with nowhere-vanishing holomorphic $`(3,0)`$-form $`\Omega`$. Let $`\omega`$ be a positive Hermitian form, let $`(V,A)`$ and $`(W,A_W)`$ be visible and hidden holomorphic bundles with HYM connections, and let $`\nabla`$ be the declared tangent-bundle connection. Suppressing conventional trace normalizations, the target equations include
``` math
\begin{align}
\mathrm{d}(\|\Omega\|_\omega\,\omega^2)&=0, \label{eq:balanced}\\
F_A^{0,2}=F_{A_W}^{0,2}&=0, \qquad
F_A\wedge\omega^2=F_{A_W}\wedge\omega^2=0, \label{eq:hym}\\
H&=\mathrm{i}(\bar\partial-\partial)\omega, \label{eq:torsion}\\
\mathrm{d}H&=\frac{\alpha'}{4}
\left(\mathrm{Tr}R_\nabla\wedge R_\nabla
-\mathrm{Tr}F_A\wedge F_A-\mathrm{Tr}F_{A_W}\wedge F_{A_W}\right).
\label{eq:bianchi}
\end{align}
```
Global flux, gerbe, stability, quantization, and worldsheet requirements add further data. Established solutions show that this target is mathematically nonempty, including Fu–Yau-type constructions and stable-bundle perturbations . Invariant solutions on complex Lie groups also exist, but their existence does not validate every proposed invariant bundle .

Write the full typed configuration space as
``` math
\mathcal{X}_{\mathrm{HS}}=\{(X,\Omega,\omega,V,A,W,A_W,\nabla,H,\ldots)\}/\mathcal{G},
```
where $`\mathcal{G}`$ contains the declared gauge and geometric equivalences. Let
``` math
\mathcal{R}_{\mathrm{HS}}:\mathcal{X}_{\mathrm{HS}}\longrightarrow\mathcal{Y}_{\mathrm{HS}}
```
collect all residuals, including <a href="#eq:balanced,eq:hym,eq:bianchi" data-reference-type="ref+label" data-reference="eq:balanced,eq:hym,eq:bianchi">[eq:balanced,eq:hym,eq:bianchi]</a> and the global conditions selected for the problem. The full solution set is
``` math
\mathcal{S}_{\mathrm{HS}}=\mathcal{R}_{\mathrm{HS}}^{-1}(0).
```
This definition is deliberately demanding: all entries refer to one carrier and one compatible collection of bundles and connections.

# The selection ladder

## Five distinct levels

<div class="definition">

**Definition 1** (Selection ladder). For a declared ansatz $`\iota:\mathcal{A}\hookrightarrow\mathcal{X}_{\mathrm{HS}}`$, a test map $`P:\mathcal{Y}_{\mathrm{HS}}\to\mathcal{E}`$, and a flow $`\Phi_t`$ when one is supplied, define:

1.  *projected consistency*: $`P\mathcal{R}_{\mathrm{HS}}(\iota(a))=0`$;

2.  *full equation closure*: $`\mathcal{R}_{\mathrm{HS}}(\iota(a))=0`$;

3.  *ansatz-local isolation*: $`a`$ is isolated among full solutions in $`\mathcal{A}`$, modulo the declared equivalences;

4.  *dynamical attraction*: $`\iota(a)`$ is an attracting fixed point of a specified evolution on a specified domain;

5.  *physical selection*: a source rule assigns the realized branch or a probability law on the relevant basins.

</div>

The ladder is not meant to devalue the lower levels. A projected calculation can reject an ansatz cheaply. Full closure can construct a genuine solution. Isolation can remove continuous moduli in the chosen family. Attraction can show robustness. The point is that the noun “selection” must say which level has been reached.

## Why component equations are not automatically complete

<div id="prop:projected" class="proposition">

**Proposition 2** (Projected residual criterion). *For $`a\in\mathcal{A}`$,
``` math
P\mathcal{R}_{\mathrm{HS}}(\iota(a))=0
\quad\Longrightarrow\quad
\mathcal{R}_{\mathrm{HS}}(\iota(a))\in\ker P.
```
Consequently, projected consistency implies full equation closure if and only if
``` math
\mathrm{im}(\mathcal{R}_{\mathrm{HS}}\circ\iota)\cap\ker P=\{0\}.
\tag{3.1}\label{eq:complete-test}
```*

</div>

<div class="proof">

*Proof.* The first statement is the definition of the kernel. The implication to a zero full residual holds precisely when the only residual both produced by the ansatz and invisible to $`P`$ is the zero residual. ◻

</div>

Condition <a href="#eq:complete-test" data-reference-type="ref+label" data-reference="eq:complete-test">[eq:complete-test]</a> is the algebraic form of a consistent truncation check. Expanding the Bianchi identity on a basis of invariant $`(2,2)`$-forms is complete for that residual only if the residual is known to lie entirely in the tested invariant space. It does not by itself prove the Dolbeault integrability of a printed connection, the existence of global bundle transition maps, stability, a global gerbe, or the discarded field equations.

<div class="example">

**Example 3**. Take $`\mathcal{Y}_{\mathrm{HS}}=\mathbb{R}^2`$, let $`P(x,y)=x`$, and let a proposed ansatz produce $`\mathcal{R}_{\mathrm{HS}}(\iota(a))=(0,1)`$. The tested coefficient vanishes, but the full residual does not. Heterotic analogues arise whenever one checks invariant Bianchi coefficients while leaving a nonzero Maurer–Cartan, HYM, global bundle, or non-invariant residual untested.

</div>

## Why isolated in an ansatz is not globally unique

<div id="thm:ansatz" class="theorem">

**Theorem 4** (Ansatz isolation theorem). *Assume $`a_\star\in\mathcal{A}`$ satisfies the full equations and that the derivative
``` math
D(\mathcal{R}_{\mathrm{HS}}\circ\iota)_{a_\star}:T_{a_\star}\mathcal{A}
\longrightarrow\mathcal{Y}_{\mathrm{HS}}
```
is injective with a bounded left inverse on its image. Then $`a_\star`$ is locally isolated in $`\mathcal{A}`$, modulo any quotient directions removed from $`T_{a_\star}\mathcal{A}`$. This conclusion does not imply local or global uniqueness in $`\mathcal{X}_{\mathrm{HS}}`$.*

</div>

<div class="proof">

*Proof.* The inverse or implicit function theorem gives local isolation on the declared finite-dimensional slice after quotient directions are removed. Directions transverse to $`\iota(\mathcal{A})`$ are absent from the derivative. Other full solutions may therefore lie arbitrarily near the slice, or on disconnected components not meeting it at all. ◻

</div>

To promote ansatz uniqueness to global uniqueness, one would at minimum need an exhaustion theorem showing that every admissible solution orbit meets the ansatz and a faithfulness theorem showing that distinct full orbits are not identified there. Such statements are rare and are not consequences of Nomizu reduction alone.

## What attraction and physical selection add

<div class="definition">

**Definition 5** (Dynamical and physical selection data). Dynamical attraction is typed by a semiflow $`\Phi_t:\mathcal{D}\to\mathcal{D}\subseteq\mathcal{X}_{\mathrm{HS}}`$, a fixed point $`x_\star`$, and a basin
``` math
\mathcal{B}(x_\star)=\{x\in\mathcal{D}:\Phi_t(x)\to x_\star\}.
```
Physical selection additionally requires a source object, for example an initial measure $`\mu_0`$, a deterministic branch functional, or an equivalent preparation law. With a measure, the basin weight is $`\mu_0(\mathcal{B}(x_\star))`$.

</div>

<div id="thm:no-selection" class="theorem">

**Theorem 6** (No selection from equations alone). *The zero set $`\mathcal{S}_{\mathrm{HS}}`$ determines neither a semiflow, its basins, nor a measure on those basins. Even a singleton zero set inside $`\mathcal{A}`$ supplies no physical-selection probability without additional source data.*

</div>

<div class="proof">

*Proof.* Distinct vector fields can share the same zero set while assigning a fixed point different stability types. For example, on $`\mathbb{R}`$, both $`\dot x=-x`$ and $`\dot x=x`$ have zero set $`\{0\}`$, but the first attracts and the second repels. Likewise, infinitely many mutually singular measures can be placed on a fixed family of basins. Neither object is determined by the equation $`x=0`$. ◻

</div>

# Where MTT enters

MTT aims to supply structure above the lower equations: an admissible upper carrier, a reduction map, an evolution, and fixed-point or continuation rules. That ambition is directly relevant to vacuum selection, but only after the upper and lower objects are connected.

Let $`\mathcal{M}`$ be an MTT configuration space with vector field $`V_{\mathrm{MTT}}`$, and let
``` math
\mathfrak{B}:\mathcal{M}\longrightarrow\mathcal{X}_{\mathrm{HS}}
```
be a typed bridge. If a lower Hull–Strominger evolution $`V_{\mathrm{HS}}`$ is declared, the essential compatibility equation is
``` math
D\mathfrak{B}_m\,V_{\mathrm{MTT}}(m)
=V_{\mathrm{HS}}(\mathfrak{B}(m)).
\tag{4.1}\label{eq:intertwine}
```
The adjacent MTT-to-Hull–Strominger paper owns the exact and residual fixed-point descent theorems based on this equation . We do not duplicate them here. Their lesson for selection is simple: an upper fixed point descends to a lower fixed point only after the bridge and the flow intertwining are supplied. A rank match, shared notation, or formal similarity of constraints is not enough.

There are nevertheless narrower senses in which MTT already selects data. The current finite program proves an exact $`q=79`$ arithmetic branch under its declared discrete assumptions, and it selects a retarded representative within a conjugate orientation orbit. Those are genuine finite branch selections. They do not by themselves select a smooth compactification, because the visible and hidden bundles, common HYM chamber, differential Bianchi representative, and continuum intertwiner remain separate objects.

# Re-auditing the two former case studies

## Iwasawa: valid local geometry, invalid physical chain

Let $`X=\Gamma\backslash H_3(\mathbb{C})`$ be the Iwasawa manifold with invariant $`(1,0)`$-forms
``` math
\mathrm{d}\omega^1=\mathrm{d}\omega^2=0,\qquad
\mathrm{d}\omega^3=\omega^1\wedge\omega^2.
```
For a diagonal Hermitian form
``` math
\omega=\frac{\mathrm{i}}{2}
\sum_{j=1}^{3}r_j^2\omega^j\wedge\overline{\omega^j},
```
the local complex-parallelizable and balanced calculations are legitimate. The torsion $`H=\mathrm{i}(\bar\partial-\partial)\omega`$ and its derivative can be computed exactly in the invariant frame.

The former paper then attached a rank-three visible-bundle construction, component anomaly match, generation count, and normalized cubic Yukawa. The current audited calculation shows why that chain fails :

1.  a form used as Chern data is not closed;

2.  the advertised monad lacks globally constructed line bundles and holomorphic maps;

3.  the printed Dolbeault matrix has a nonzero Maurer–Cartan residual;

4.  the unique one-entry repair in the stated matrix ansatz lies in one complex-gauge orbit and has a non-scalar holomorphic commutant, so it does not supply the claimed stable simple rank-three bundle;

5.  the stated trivial carrier forces $`c_3=0`$;

6.  the Bianchi, generation, and Yukawa conclusions depending on that bundle therefore do not follow.

This is not a no-go theorem for all invariant Iwasawa solutions. Such solutions exist in the literature for carefully chosen connections and bundles . It is a no-go for using the particular invalid bundle chain as the selection witness in this paper.

## Lens–Nil: an auxiliary real structure

The former second example used
``` math
L(3,1)\times(\Gamma\backslash\mathrm{Nil}_3)
```
with a balanced real $`\mathrm{SU}(3)`$-structure but explicitly found $`\mathrm{d}\Omega\neq0`$. The Hull–Strominger system requires a complex threefold with integrable complex structure and holomorphic volume form. Thus the displayed Lens–Nil object is not a point of $`\mathcal{X}_{\mathrm{HS}}`$, and solving two formal coefficient equations on it cannot select a heterotic vacuum.

Lens and Nil data may still be useful as auxiliary transport, filtration, spectral, or finite-carrier models inside MTT. That role is different from identifying their literal product with the selected global compactification. In particular, it is not the $`q=79`$ Fu–Yau-oriented carrier.

## Status table

<div class="center">

| Object | Current status | Meaning for selection |
|:---|:---|:---|
| Diagonal Iwasawa geometry and local torsion | retained | Valid lower geometric calculation; no physical bundle is selected. |
| Old Iwasawa visible bundle | withdrawn | Cannot source anomaly, index, or Yukawa conclusions. |
| Old normalized Iwasawa Yukawa | withdrawn | Normalization of $`\Omega`$ does not determine normalized matter wavefunctions or their physical overlap. |
| Lens–Nil compactification | retired as physical | Non-integrable auxiliary real $`\mathrm{SU}(3)`$-structure only. |
| $`q=79`$ arithmetic branch | exact at finite tier | Selects a discrete branch under stated assumptions, not a smooth vacuum. |
| Rank-two Cech/HYM packets | finite or rank-two certified | Useful ingredients; no automatic rank-three physical transfer. |
| Physical visible–hidden Fu–Yau tuple | open | Required before compactification selection can be claimed. |

</div>

# A correct theorem for finite ansatz calculations

The finite calculation can still support a rigorous theorem when its scope is stated honestly.

<div id="thm:finite" class="theorem">

**Theorem 7** (Finite-ansatz conclusion theorem). *Let $`\mathcal{A}`$ be a finite-dimensional ansatz and let $`a_\star\in\mathcal{A}`$. Assume:*

1.  *$`\iota(a)`$ defines global typed data in $`\mathcal{X}_{\mathrm{HS}}`$ for every $`a`$ in a neighborhood of $`a_\star`$;*

2.  *the tested residual map $`P`$ satisfies the completeness condition <a href="#eq:complete-test" data-reference-type="ref+label" data-reference="eq:complete-test">[eq:complete-test]</a>;*

3.  *quantization, stability, gauge quotient, and global bundle or gerbe conditions are included rather than inferred from local forms;*

4.  *$`P\mathcal{R}_{\mathrm{HS}}(\iota(a_\star))=0`$;*

5.  *the quotient derivative at $`a_\star`$ is injective with a bounded left inverse.*

*Then $`\iota(a_\star)`$ is a full Hull–Strominger solution locally isolated inside the declared ansatz, modulo the declared equivalences.*

*If, in addition, a flow preserving $`\iota(\mathcal{A})`$ is specified and its linearization has a certified spectral gap with nonlinear remainder controlled on a neighborhood, then $`a_\star`$ is locally attracting in that neighborhood. Neither conclusion establishes global uniqueness or physical selection without exhaustion and source hypotheses.*

</div>

<div class="proof">

*Proof.* By (F2) and (F4), <a href="#prop:projected" data-reference-type="ref+label" data-reference="prop:projected">2</a> gives full equation closure. Assumptions (F1) and (F3) ensure that this zero is a zero of the correctly typed global problem rather than a local symbolic surrogate. Assumption (F5) and <a href="#thm:ansatz" data-reference-type="ref+label" data-reference="thm:ansatz">4</a> give isolation in the quotient ansatz. The final claim is the standard linearized-stability conclusion once the flow, gap, domain invariance, and nonlinear bound are supplied. The missing global and source conclusions are excluded by <a href="#thm:ansatz,thm:no-selection" data-reference-type="ref+label" data-reference="thm:ansatz,thm:no-selection">[thm:ansatz,thm:no-selection]</a>. ◻

</div>

This theorem replaces the former “FCC equals component equations” statement. It is stronger because its hypotheses reveal exactly what a candidate must provide, and weaker in the necessary way because it does not rename consistency as selection.

# The current q79 compactification boundary

## What is already available

The selected $`q=79`$ program contains nontrivial and reusable ingredients:

- an exact arithmetic theorem selecting $`q=79`$ on the declared finite branch;

- a literal finite Cech witness;

- a certified finite projected HYM approximation;

- a selected rank-two continuum HYM witness with Fourier-tail and Wiener contraction control;

- a retarded orientation representative inside the finite conjugate branch pair.

These facts improve the search problem. They constrain which branch and which local analytic architecture should be used. They do not yet satisfy the same-carrier requirement of <a href="#eq:balanced,eq:hym,eq:bianchi" data-reference-type="ref+label" data-reference="eq:balanced,eq:hym,eq:bianchi">[eq:balanced,eq:hym,eq:bianchi]</a>.

## Physical compactification-selection certificate

A future claim that MTT selects one heterotic compactification should provide at least the following certificate:

1.  one global complex $`q=79`$ Fu–Yau-oriented carrier with its balanced metric and holomorphic volume form;

2.  explicit stable rank-three visible and compatible hidden holomorphic bundles in one positive Gauduchon/HYM chamber;

3.  HYM connections and the differential Green–Schwarz identity on that same tuple, together with global flux/gerbe data;

4.  a connection-preserving MTT bridge and the flow intertwining <a href="#eq:intertwine" data-reference-type="ref+label" data-reference="eq:intertwine">[eq:intertwine]</a>, or a certified residual theorem;

5.  a basin or contraction proof on a declared domain if dynamical attraction is claimed;

6.  an exhaustion theorem or an explicitly restricted candidate class if uniqueness is claimed;

7.  a preparation, branch, or measure rule if physical realization or probabilities are claimed;

8.  matter cohomology, normalized overlap data, and the worldsheet/IR endpoint for phenomenological claims.

The first three rows are the open physical Hull–Strominger endpoint. The fourth is the open geometry-to-operator naturality problem. Later rows should not be used to hide those earlier dependencies.

# Worldsheet and effective-field-theory boundaries

The first version claimed a succinct worldsheet verification, but the displayed beta functions mixed bosonic-string central-charge notation with a heterotic ten-dimensional target and treated the dilaton equation as automatic. That conclusion is withdrawn. Supersymmetry, anomaly cancellation, equations of motion, and worldsheet conformal invariance are related but convention- and order-dependent statements. The choice of tangent connection also participates in field redefinitions and the anomaly equation .

For a valid Hull–Strominger tuple, leading-order sigma-model reasoning provides an important consistency check. It does not repair a nonintegrable target or an undefined bundle, and it does not by itself prove an all-orders SCFT. Fu–Yau geometry and Anomaly-flow results provide established mathematical routes to lower fixed points ; they do not supply the missing MTT source map automatically.

The former EFT statements are narrowed for the same reason. A physical Yukawa coupling requires identified matter cohomology classes, normalized zero modes, bundle-valued products, a Hermitian inner product, and a four-dimensional normalization and matching convention. Rescaling $`\Omega`$ or choosing a basis in an invariant form space cannot set that physical coupling to one. Separate finite/profile Yukawa results elsewhere in the MTT corpus are unaffected, but they cannot be retroactively attributed to the invalid Iwasawa construction.

# Why the corrected result remains useful

The correction changes the role of finite invariant calculations without making them pointless.

#### They are efficient obstruction detectors.

A nonzero projected residual disproves a candidate immediately. Failure of integrability, closure, stability, or a characteristic-class condition can retire an entire branch before expensive continuum work.

#### They can produce candidate seeds.

When the global data exist and the truncation is complete, a finite solution can seed an implicit-function, perturbative, Galerkin, or flow construction. The literature on stable bundles, Fu–Yau geometry, and invariant solutions shows several ways in which such seeds can become genuine solutions.

#### They make the remaining assumptions visible.

The selection ladder prevents a common source of apparent progress: relabeling a solved constraint as an attractor or a finite branch as the realized universe. In MTT this is especially valuable because the theory is explicitly attempting to move upstream from lower equations to their carrier, evolution, and source.

#### They preserve narrower exact selections.

The exact $`q=79`$ arithmetic and retarded-orientation choices are not erased because the physical compactification is open. They are retained as properly typed finite selections and can constrain the eventual global construction.

# Conclusion

The corrected conclusion is precise. Componentwise left-invariant equations can establish projected consistency. With global typed data and a complete residual test they can establish a full solution. With a nonsingular quotient derivative they can establish isolation inside the ansatz. With a specified flow and certified stability bounds they can establish attraction. Only an exhaustion statement and a source or preparation rule can support a claim of physical vacuum selection.

The former Iwasawa and Lens–Nil examples do not reach those levels: the Iwasawa physical bundle chain fails, and Lens–Nil is not a complex Hull–Strominger target. The exact $`q=79`$ finite branch and rank-two Cech/HYM results remain real progress at narrower tiers. The next physical advance is therefore not another reformulation of the component equations. It is the common rank-three visible–hidden Fu–Yau tuple, followed by the connection-preserving MTT bridge, its attraction domain, and its source rule.

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

The q79 theorem and audit, literal finite rank-two Cech witness, and rank-two Wiener-contraction certificate are direct evidence only for the finite branch, topological witness, and declared rank-two analytic tier. They do not establish global exhaustion, a physical rank-three visible-hidden Hull-Strominger tuple, dynamical attraction of that tuple, or a source measure selecting one realized compactification.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A07/literal_cech_witness` (**DERIVED_EXACT**): Literal 81-entry, 729-cocycle finite Cech witness.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
