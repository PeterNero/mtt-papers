---
abstract: |
  We formulate gauge redundancy as a precise lens-type realization rather than as the unique response to every nonfaithful description. For a declared group action $`\mathcal G\curvearrowright\mathcal A`$, the orbit map $`q:\mathcal A\to\mathcal A/\mathcal G`$ identifies gauge-related representatives. At the set level, every invariant map factors uniquely through this quotient. That universal property organizes redundancy but does not select the group, action, bundle, connection, observables, or dynamics.

  We separate two global-section questions that were conflated in the first version. A principal bundle $`P\to Y`$ is globally defined by its transition cocycle even when it has no global section; a global section exists precisely when $`P`$ is trivial. A field-space gauge fixing is instead a section of the orbit map on a specified regularity class and orbit stratum. Nonunique representatives alone do not obstruct such a section. A genuine global gauge-fixing obstruction must be proved in the chosen topological, smooth, or stacky category, as in Gribov–Singer phenomena.

  On a supplied principal bundle, a connection gives local gauge potentials and covariant curvature. Yang–Mills dynamics follows only after one supplies a base metric, structure group, invariant bilinear form, coupling, matter representation, boundary conditions, and local action. Other gauge-invariant actions exist, so lens-type redundancy does not prove uniqueness of Yang–Mills theory or select the Standard Model gauge group. Program B2 therefore establishes a typed redundancy and gauge-fixing framework plus a conditional Yang–Mills realization.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: e5f82dc6da68379853772da5e4256eaf274282ed9e1a2089c35a5172bbd304db
paper_id: the-modal-triplet-theory-program-b2-gauge-structure-as-4afd644a
release_state: zenodo_released
released_version: v2
title: |
  The Modal Triplet Theory Program B2:
  Gauge Redundancy, Global Sections, and the Conditional Yang–Mills Realization
zenodo_doi: 10.5281/zenodo.21652648
zenodo_record_id: 21652648
zenodo_url: "https://zenodo.org/records/21652648"
---

# Revision note for version 2

<div class="description">

Version 1 of Program B2.

The first version treated nonunique representatives as a failure of global description, asserted that every lens obstruction forces a unique gauge encoding, conflated a section of a spacetime principal bundle with a section of the field-space orbit map, and described connections and Yang–Mills structure as if they followed from redundancy alone.

Version 2 fixes the acting group and category, proves the quotient universal property, distinguishes the two section problems, and makes global gauge fixing a typed right-inverse question. Principal bundles and connections are canonical gauge realizations only after their geometric data are supplied. Yang–Mills equations are derived only from a declared local action.

Gauge transformations can organize redundant representatives; invariant quantities factor through gauge orbits; local potentials are related by bundle transition functions; and a connection compares local representatives without selecting a preferred gauge.

No theorem here selects the gauge group, principal bundle, global gauge fixing, Standard Model representation content, coupling constants, anomaly cancellation, or a unique Yang–Mills action from the lens profile.

</div>

# How to read Program B2

B2 begins with redundancy and asks how much extra structure is needed before that redundancy becomes gauge theory. The answer proceeds through a declared group action, its orbit quotient, a principal bundle, a connection, a field-space gauge-fixing problem, and finally a selected local action.

#### The central picture in plain language.

A gauge orbit is a family of different mathematical representatives assigned the same declared physical content. An invariant quantity has the same value on every member of that orbit, so it factors through the orbit space. This universal property organizes redundancy. It does not tell us which group acts, which orbits are physical, or which invariant quantities form a complete observable set.

#### Two different section problems.

A section of $`P\to Y`$ chooses one point in each principal-bundle fiber over spacetime and exists globally exactly when that bundle is trivial. A section of $`q:\mathcal A\to\mathcal A/\mathcal G`$ chooses one connection representative from each gauge orbit in a declared field-space domain. A bundle can be globally well-defined without the first section, and local gauge slices can exist without gluing to the second. Conflating these maps turns ordinary bundle topology into a false gauge-fixing conclusion.

#### A simple abelian case.

For a $`U(1)`$ potential, local representatives related by $`A\mapsto A+d\chi`$ lie on one gauge orbit after the allowed boundary behavior of $`\chi`$ is fixed. Curvature $`F=dA`$ is invariant under this transformation. This illustrates orbit redundancy and an invariant diagnostic, but it does not select $`U(1)`$, the base manifold, a coupling, or the Maxwell/Yang–Mills action.

#### Argument map.

Sections 1–2 define the group action, quotient, and invariant factorization. Section 3 separates principal-bundle topology from field-space gauge fixing. Sections 4–5 introduce connections, local potentials, stabilizers, slices, and genuine global obstructions. Section 6 derives Yang–Mills equations only from the supplied geometric and action data. Sections 7–9 separate gravity, quantization, and Standard Model claims and state the exact remaining source problem.

#### Scope boundary.

Lens-type nonfaithfulness is compatible with many groups, bundles, actions, and physical interpretations. B2 provides the typed gauge framework and a conditional Yang–Mills realization. It does not select the Standard Model gauge group, matter representations, anomalies, couplings, or quantization.

# Scope and Imported Data

Program A0 supplies typed reductions, admissible domains, and exact factorization criteria . Program B0 defines a lens profile as nonfaithfulness, redundancy, or multiple effective representatives under a declared reduction; it does not identify every lens profile with a lens space or gauge theory . Program B1 proves that smooth transport becomes a connection only on a supplied bundle and warns that internal gauge transport and frame transport are different physical types .

The present paper asks:

> When does descriptive redundancy have the mathematical form of gauge redundancy, when does a global gauge choice fail, and what additional data are required to obtain Yang–Mills dynamics?

The answer has four levels:

1.  a group action and its quotient;

2.  a principal bundle and its local sections;

3.  a connection and field-space gauge fixing; and

4.  a local gauge-invariant action.

Each level imports data not contained in the coarse predicate “more than one representative survives.”

# Typed Redundancy and the Orbit Quotient

## A declared action

<div id="def:gauge-datum" class="definition">

**Definition 1** (Gauge-redundancy datum). A *gauge-redundancy datum* consists of:

1.  a configuration object $`\mathcal A`$ in a declared category;

2.  a group or group object $`\mathcal G`$;

3.  an action $`\mathcal G\curvearrowright\mathcal A`$; and

4.  a declaration of which subgroup acts redundantly, including its boundary and asymptotic conditions.

At the set level, the orbit of $`A\in\mathcal A`$ is
``` math
[A]=\{u\cdot A:u\in\mathcal G\},
```
and the orbit map is
``` math
q:\mathcal A\longrightarrow\mathcal A/\mathcal G,\qquad q(A)=[A].
```

</div>

The category matters. A set-theoretic orbit space, a topological quotient, a smooth quotient, and the quotient stack $`[\mathcal A/\mathcal G]`$ retain different information. In particular, the stack remembers stabilizer groups that a coarse orbit space can discard.

<div id="def:lens" class="definition">

**Definition 2** (Gauge lens-type realization). The datum of Definition <a href="#def:gauge-datum" data-reference-type="ref" data-reference="def:gauge-datum">1</a> is a *gauge lens-type realization* when the orbit map is noninjective on the declared domain:
``` math
A\ne A'\quad\text{and}\quad q(A)=q(A')
```
for at least one pair. It is a *gauge-fixing obstruction* only when the orbit map has no section of the required regularity on the required domain or stratum.

</div>

This separates redundancy from obstruction. Redundancy says that an orbit contains several representatives. Obstruction says that no globally compatible representative can be selected in a specified category.

## The quotient universal property

<div id="thm:quotient" class="theorem">

**Theorem 3** (Set-level invariant factorization). *Let $`Z`$ be a set. A map $`F:\mathcal A\to Z`$ is gauge invariant,
``` math
F(u\cdot A)=F(A)
 \qquad
 (u\in\mathcal G,\ A\in\mathcal A),
```
if and only if there is a unique map $`\overline F:\mathcal A/\mathcal G\to Z`$ such that
``` math
F=\overline F\circ q.
```*

</div>

<div class="proof">

*Proof.* If $`F`$ is invariant, define $`\overline F([A])=F(A)`$. Invariance makes this well defined. Since $`q`$ is surjective, the factorization determines $`\overline F`$ uniquely. The converse is immediate because $`q(u\cdot A)=q(A)`$. ◻

</div>

<div class="corollary">

**Corollary 4** (What is universal). *The orbit quotient is universal for invariant set-valued diagnostics. This does not make one physical gauge theory universal or unique.*

</div>

In a topological or smooth category, the same conclusion requires the corresponding categorical quotient and continuity or smoothness of $`\overline F`$. Such a quotient may be singular or fail to be a manifold.

## Nonuniqueness is not failure

<div id="prop:redundancy" class="proposition">

**Proposition 5** (Redundancy alone is not a global obstruction). *Noninjectivity of $`q`$ neither implies that the underlying principal bundle is undefined nor proves that a global field-space gauge fixing fails.*

</div>

<div class="proof">

*Proof.* The trivial bundle $`Y\times G`$ is globally defined and has a global section, yet its connection space has many representatives related by nonconstant gauge transformations. Conversely, failure of a global section of a nontrivial principal bundle concerns $`P\to Y`$, while field-space gauge fixing concerns $`q:\mathcal A\to\mathcal A/\mathcal G`$. These are different maps. ◻

</div>

## Invariant versus complete observables

<div class="definition">

**Definition 6** (Separating invariant family). A family of invariant functions $`\{F_i:\mathcal A\to Z_i\}_{i\in I}`$ is *separating* on a domain if
``` math
F_i(A)=F_i(A')\text{ for all }i
 \quad\Longrightarrow\quad
 q(A)=q(A').
```

</div>

Gauge invariance alone does not imply separation of orbits. A selected observable family may be incomplete. Consequently, failure of chosen diagnostics to distinguish two configurations is not by itself proof that the configurations are gauge equivalent.

# Principal Bundles and the First Section Problem

## Global bundles from local data

Let $`Y`$ be a paracompact smooth manifold, $`G`$ a Lie group, and $`\{U_\alpha\}`$ an open cover. Smooth transition functions
``` math
g_{\beta\alpha}:U_\alpha\cap U_\beta\longrightarrow G
```
with
``` math
g_{\alpha\alpha}=e,\qquad
 g_{\alpha\beta}=g_{\beta\alpha}^{-1},\qquad
 g_{\gamma\beta}g_{\beta\alpha}=g_{\gamma\alpha}
```
on triple overlaps glue the local products $`U_\alpha\times G`$ into a globally defined principal $`G`$-bundle $`P\to Y`$ .

<div id="prop:no-section-required" class="proposition">

**Proposition 7** (No preferred section is required). *The bundle $`P`$ is globally defined by the transition cocycle. Its definition does not require a preferred global section.*

</div>

<div class="proof">

*Proof.* The quotient of the disjoint union $`\coprod_\alpha U_\alpha\times G`$ by
``` math
(x,h)_\alpha\sim(x,g_{\beta\alpha}(x)h)_\beta
```
is well defined and transitive precisely because of the cocycle equation. Local products supply the bundle charts. ◻

</div>

## When a spacetime section exists

<div id="thm:bundle-section" class="theorem">

**Theorem 8** (Principal-bundle section criterion). *A principal $`G`$-bundle $`P\to Y`$ admits a continuous global section if and only if it is continuously trivial. In the smooth category, it admits a smooth global section if and only if it is smoothly trivial.*

</div>

<div class="proof">

*Proof.* If $`s:Y\to P`$ is a section, the map
``` math
Y\times G\longrightarrow P,\qquad (x,h)\longmapsto s(x)h
```
is a principal-bundle isomorphism, with the corresponding regularity. The trivial bundle has the section $`x\mapsto(x,e)`$. ◻

</div>

Thus lack of a global section is a nontriviality statement about $`P\to Y`$. It is not a claim that the bundle lacks global meaning.

## Three section notions

The word “section” is used for three different maps:

Bundle section.
$`s:Y\to P`$, with $`\pi_P\circ s=\operatorname{id}_Y`$.

Associated-field section.
$`\phi:Y\to E=P\times_\rho V`$, describing a field in an associated bundle.

Orbit-map gauge fixing.
$`\sigma:\mathcal Q_0\to\mathcal A_0`$, with $`q\circ\sigma=\operatorname{id}_{\mathcal Q_0}`$ on a declared field-space domain or stratum.

Existence of one does not imply existence of the others.

# Gauge Transformations and Connections

## Vertical automorphisms

For a fixed principal bundle $`P\to Y`$, its gauge group is
``` math
\mathcal G(P)=\operatorname{Aut}_Y(P),
```
the $`G`$-equivariant bundle automorphisms covering $`\operatorname{id}_Y`$. Equivalently, under standard identifications,
``` math
\mathcal G(P)\cong\Gamma(\operatorname{Ad}P),
\qquad
\operatorname{Ad}P=P\times_{\operatorname{Ad}}G.
```

Let $`\mathcal A(P)`$ denote the affine space of principal connections on $`P`$. Locally, a connection is represented by a Lie-algebra-valued one-form $`A_\alpha`$. A local gauge transformation $`u_\alpha:U_\alpha\to G`$ acts by
``` math
A_\alpha\longmapsto A_\alpha^{u_\alpha}
 =u_\alpha^{-1}A_\alpha u_\alpha+u_\alpha^{-1}du_\alpha.
```
The curvature
``` math
F_{A_\alpha}=dA_\alpha+A_\alpha\wedge A_\alpha
```
transforms covariantly:
``` math
F_{A_\alpha^{u_\alpha}}
 =u_\alpha^{-1}F_{A_\alpha}u_\alpha.
```

<div id="prop:global-connection" class="proposition">

**Proposition 9** (Local potentials, global connection). *Local potentials satisfying the connection transition law on overlaps define one global principal connection. Distinct local potentials related by gauge transformations can therefore represent the same global connection data in different local sections.*

</div>

<div class="proof">

*Proof.* The overlap law is exactly the compatibility condition for local connection one-forms to arise as pullbacks of one principal connection by local sections. Changing a local section produces the displayed gauge-transformation law. ◻

</div>

## Redundant and physical transformations

The choice of $`\mathcal G`$ must include boundary conditions. Transformations that approach the identity at a boundary may be declared redundant, while large, asymptotic, or boundary-supported transformations can act on charges or edge degrees of freedom. Quotienting by the wrong group can erase physical data. Program B2 therefore does not identify every vertical-looking transformation with pure redundancy.

## Gauge and circle profiles may coexist

A gauge connection has holonomy around loops. Its orbit redundancy is a lens-type feature, while its return transport is a circle-type feature in the terminology of Program B0. The profiles can coexist in one realization. This is another reason not to identify one obstruction label with one unique physical sector.

# Field-Space Gauge Fixing: The Second Section Problem

## The orbit map

Fix a Sobolev or smooth completion $`\mathcal A_k(P)`$, a compatible gauge group $`\mathcal G_{k+1}(P)`$, boundary conditions, and a domain or orbit stratum $`\mathcal A_0\subseteq\mathcal A_k(P)`$. Let
``` math
\mathcal Q_0=q(\mathcal A_0).
```

<div id="def:gauge-fixing" class="definition">

**Definition 10** (Global field-space gauge fixing). A *global gauge fixing* in a declared category is a section
``` math
\sigma:\mathcal Q_0\longrightarrow\mathcal A_0,
\qquad
 q\circ\sigma=\operatorname{id}_{\mathcal Q_0},
```
with the required continuity, smoothness, locality, covariance, or other regularity.

</div>

<div id="thm:gauge-fixing" class="theorem">

**Theorem 11** (Typed gauge-fixing obstruction criterion). *The gauge lens-type realization has a global gauge-fixing obstruction in the declared category exactly when the orbit map $`q:\mathcal A_0\to\mathcal Q_0`$ has no section with the declared regularity.*

</div>

<div class="proof">

*Proof.* This is the right-inverse definition of a section. Its value is the typing: the domain, orbit stratum, quotient, boundary conditions, and regularity cannot be omitted. ◻

</div>

Noninjectivity of $`q`$ is necessary for nontrivial redundancy but does not decide Theorem <a href="#thm:gauge-fixing" data-reference-type="ref" data-reference="thm:gauge-fixing">11</a>. Some actions admit global slices; others do not.

## Stabilizers and singular strata

The stabilizer of $`A`$ is
``` math
\mathcal G_A=\{u\in\mathcal G:u\cdot A=A\}.
```
If stabilizers vary, the coarse quotient is generally stratified rather than a smooth manifold. On a free proper finite-dimensional action, the orbit map is a principal $`\mathcal G`$-bundle and a global section exists exactly when that bundle is trivial. Infinite-dimensional gauge theory requires analytic completions and slice theorems before this analogy may be used.

<div id="prop:local-global" class="proposition">

**Proposition 12** (Local slices do not imply a global slice). *Suppose a slice theorem supplies local sections of $`q`$ near every orbit in $`\mathcal Q_0`$. It does not follow that these local sections glue to one global section.*

</div>

<div class="proof">

*Proof.* On overlaps, two local slices differ by transition functions valued in the gauge group or residual stabilizer. A global slice requires these transitions to be a trivial cocycle in the chosen category. Local existence alone does not prove that. ◻

</div>

## Gribov–Singer phenomena

For important nonabelian gauge theories on compact bases, no single global continuous gauge choice covers the full configuration space under the usual hypotheses. This is the content of Gribov–Singer-type results  . They are examples of Theorem <a href="#thm:gauge-fixing" data-reference-type="ref" data-reference="thm:gauge-fixing">11</a>, not a theorem that every redundancy action has the same obstruction.

Practical gauge conditions such as Coulomb, Lorenz, or axial gauge must record:

1.  the function space and regularity;

2.  the allowed gauge group and boundary behavior;

3.  the orbit stratum and stabilizers;

4.  residual gauge transformations; and

5.  whether the condition is local, global, unique, or only perturbative.

# Conditional Yang–Mills Realization

## Required data

<div id="ass:ym" class="assumption">

**Assumption 13** (Yang–Mills realization). Supply:

1.  an oriented pseudo-Riemannian base $`(Y,g)`$;

2.  a principal $`G`$-bundle $`P\to Y`$;

3.  a connection $`A`$ with curvature $`F_A`$;

4.  an $`\operatorname{Ad}`$-invariant nondegenerate bilinear form $`B`$ on $`\mathfrak g=\operatorname{Lie}(G)`$;

5.  a coupling normalization $`g_{\rm YM}`$;

6.  boundary conditions and, if present, matter representations and a matter action.

</div>

The pure Yang–Mills action is
``` math
S_{\rm YM}[A]
 =-\frac{1}{2g_{\rm YM}^2}
 \int_Y B(F_A\wedge *F_A).
```

<div id="thm:ym" class="theorem">

**Theorem 14** (Gauge invariance and Yang–Mills equation). *Under Assumption <a href="#ass:ym" data-reference-type="ref" data-reference="ass:ym">13</a>, the action is invariant under gauge transformations preserving the declared boundary conditions. Its stationary points under compactly supported connection variations satisfy
``` math
d_A *F_A=0.
```
With a gauge-covariant matter action, the right-hand side is the corresponding covariantly conserved current.*

</div>

<div class="proof">

*Proof.* Curvature transforms by conjugation. $`\operatorname{Ad}`$-invariance of $`B`$ makes the integrand gauge invariant. For a variation $`A\mapsto A+ta`$,
``` math
\left.\frac{d}{dt}\right|_{t=0}F_{A+ta}=d_Aa.
```
Integration by parts, using the boundary conditions, gives
``` math
\delta S_{\rm YM}
 =-\frac{1}{g_{\rm YM}^2}
 \int_Y B(a\wedge d_A*F_A),
```
up to the dimension- and sign-dependent conventional placement of $`*`$. Arbitrariness of $`a`$ yields the equation. ◻

</div>

## Redundancy does not select the action

<div id="thm:no-unique-ym" class="theorem">

**Theorem 15** (No unique Yang–Mills theory from a lens profile). *The gauge lens-type data of Definition <a href="#def:lens" data-reference-type="ref" data-reference="def:lens">2</a> do not determine a unique gauge group, principal bundle, invariant pairing, coupling, matter representation, or local action.*

</div>

<div class="proof">

*Proof.* Different groups, including $`U(1)`$, $`SU(2)`$, and product groups, all act nontrivially on connection spaces. Even after $`(Y,G,P)`$ are fixed, distinct $`\operatorname{Ad}`$-invariant bilinear forms and coupling coefficients can be used. In four dimensions one may add the gauge-invariant topological term
``` math
\theta\int_Y B(F_A\wedge F_A),
```
and effective actions may include gauge-invariant higher-derivative operators. These choices leave the existence of gauge orbits unchanged while altering the action or quantum theory. Hence the coarse redundancy predicate cannot select them. ◻

</div>

For a compact simple Lie algebra, an invariant symmetric bilinear form is unique up to scale, but that statement already imports the group and simplicity. Product and abelian factors admit additional couplings or kinetic mixing. A uniqueness theorem for a particular Yang–Mills action must state its dimension, locality, derivative order, parity, field content, and equivalence relation.

# Relation to Gravity, Quantization, and the Standard Model

## Gauge versus gravitational connections

Program B1 and this paper both use connections because connections encode smooth parallel transport. The physical typing differs:

- a gravitational Levi–Civita or spin connection acts on tangent, frame, coframe, or spin geometry after a metric is supplied;

- an internal gauge connection acts on a declared internal principal bundle and its associated matter representations.

These may be combined in one product or extension bundle, but equality is not implied by shared formalism.

## Quantization is downstream

Gauge quotienting is a classical structural operation. BRST/BV complexes, ghosts, gauge-fixed propagators, Hilbert spaces, path integrals, anomalies, and quantum states require independent constructions. No Born probability or complex-Hilbert theorem follows from the orbit quotient.

## No Standard Model selection at B2

The Standard Model requires, among other data:

- the global form of the gauge group;

- representations and hypercharge normalization;

- anomaly cancellation;

- chiral family content;

- Higgs and Yukawa sectors;

- coupling values and scale transport; and

- an observable comparison map.

Program B2 supplies none of these from redundancy alone. Later finite-carrier and q79 results may provide compatible realizations at their declared tiers, but B2 cannot retroactively convert compatibility into uniqueness or no-parameter prediction.

# Scoped B2 Theorem

<div id="thm:scoped" class="theorem">

**Theorem 16** (Gauge redundancy with conditional Yang–Mills realization). *For the typed data declared in this paper:*

1.  *a gauge lens-type realization is a noninjective orbit map for a declared group action;*

2.  *invariant set-valued diagnostics factor uniquely through the orbit quotient;*

3.  *nonunique representatives do not imply failure of a global bundle or a global field-space gauge fixing;*

4.  *a principal bundle is globally defined by its cocycle and has a global section exactly when it is trivial;*

5.  *a field-space gauge fixing is a section of the orbit map on a declared domain, stratum, and regularity class;*

6.  *local slices do not by themselves provide a global slice;*

7.  *a supplied principal connection yields the standard local gauge potential and curvature laws; and*

8.  *Yang–Mills equations follow from the action of Assumption <a href="#ass:ym" data-reference-type="ref" data-reference="ass:ym">13</a>, while the lens profile alone selects neither that action nor the gauge group.*

</div>

<div class="proof">

*Proof.* Items 1–2 are Definition <a href="#def:lens" data-reference-type="ref" data-reference="def:lens">2</a> and Theorem <a href="#thm:quotient" data-reference-type="ref" data-reference="thm:quotient">3</a>. Item 3 is Proposition <a href="#prop:redundancy" data-reference-type="ref" data-reference="prop:redundancy">5</a>. Item 4 is Proposition <a href="#prop:no-section-required" data-reference-type="ref" data-reference="prop:no-section-required">7</a> and Theorem <a href="#thm:bundle-section" data-reference-type="ref" data-reference="thm:bundle-section">8</a>. Items 5–6 are Theorem <a href="#thm:gauge-fixing" data-reference-type="ref" data-reference="thm:gauge-fixing">11</a> and Proposition <a href="#prop:local-global" data-reference-type="ref" data-reference="prop:local-global">12</a>. Item 7 is Proposition <a href="#prop:global-connection" data-reference-type="ref" data-reference="prop:global-connection">9</a>. Item 8 is Theorems <a href="#thm:ym" data-reference-type="ref" data-reference="thm:ym">14</a> and <a href="#thm:no-unique-ym" data-reference-type="ref" data-reference="thm:no-unique-ym">15</a>. ◻

</div>

# Version Delta and Research Frontier

Relative to version 1, this revision:

- replaces “gauge is necessary and unique” by a typed group-action and quotient construction;

- retains the quotient universal property only in its stated category;

- separates multiple representatives from failure of a section;

- distinguishes sections of $`P\to Y`$, associated fields, and the field-space orbit map;

- states that a principal bundle is global even without a global section;

- makes gauge-fixing obstruction a right-inverse theorem on a specified domain and regularity class;

- treats Gribov–Singer results as realization-specific no-go theorems, not as consequences of redundancy alone;

- distinguishes redundant gauge transformations from boundary or asymptotic transformations that may carry physical charges;

- permits lens and circle profiles to coexist in one gauge connection; and

- derives Yang–Mills equations only from an explicit action while withdrawing uniqueness of the group and dynamics.

The next source theorem must start from one selected upper MTT carrier and emit:

1.  the internal structure group and its global form;

2.  the principal/associated bundles and transition cocycles;

3.  the physical redundancy subgroup including boundary conditions;

4.  the connection, invariant pairing, and action normalization;

5.  the chiral matter representations and anomaly certificate; and

6.  a commuting descent to the accepted finite operators and observables.

Until then, B2 is a rigorous gauge-redundancy framework and conditional Yang–Mills reconstruction, not a derivation of the Standard Model gauge sector.

# Conclusion

Gauge redundancy is a particularly clear realization of the lens profile once the acting group and quotient are declared. Its exact universal statement is the factorization of invariant diagnostics through the orbit space. That statement organizes representatives; it does not imply that a global bundle fails to exist or that no gauge fixing is possible.

The geometry becomes precise on a supplied principal bundle. Local sections give local potentials, a connection gives their compatible transport, and curvature transforms covariantly. A global spacetime section and a global field-space gauge fixing remain different questions. Yang–Mills dynamics then requires a metric, invariant pairing, coupling, boundary conditions, and action. This revised hierarchy retains the useful MTT insight that gauge freedom can encode redundancy while removing uniqueness and inevitability claims that the lens profile alone cannot prove.

<div class="thebibliography">

99

P. Nero, *The Modal Triplet Theory Program A0: A Structural Theory of Reduced Description*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B0: Circle–Lens–Nil as an Obstruction Taxonomy and Its Minimal Curvature Realizations*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B1: Loop-Transport Consistency and the Conditional Gravity Realization*, revised v2, 2026.

S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry*, volume I, Wiley, 1963.

N. Steenrod, *The Topology of Fibre Bundles*, Princeton University Press, 1951.

V. N. Gribov, “Quantization of non-Abelian gauge theories,” *Nuclear Physics B* 139 (1978), 1–19.

I. M. Singer, “Some remarks on the Gribov ambiguity,” *Communications in Mathematical Physics* 60 (1978), 7–12.

D. S. Freed and K. K. Uhlenbeck, *Instantons and Four-Manifolds*, Springer, 1984.

C. N. Yang and R. L. Mills, “Conservation of isotopic spin and isotopic gauge invariance,” *Physical Review* 96 (1954), 191–195.

</div>

# Computational Evidence and Reproducibility

The numerical and machine-verifiable claims used by this paper are archived in the curated repository, `https://github.com/PeterNero/mtt-results-repro`. The mapped authority/result identifiers are `no result rows mapped`. Claim tiers in that capsule distinguish exact derivation, certified numerics, profile replay, conditional results, and open obligations.
