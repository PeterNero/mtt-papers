---
abstract: |
  We formulate circle, lens, and nil (CLN) as three coarse, typed profiles of an encoding atlas rather than as an exhaustive list of all possible descent obstructions. Circle records nontrivial return transport around a composable loop; lens records nonfaithfulness or redundancy of a reduction; nil records failure of a declared chart or transition to extend. These predicates concern different mathematical data, can occur independently or together, and are invariant under suitably compatible re-encoding. They do not by themselves imply a literal circle, lens-space, or nilmanifold factor. We distinguish holonomy from curvature by exhibiting a flat connection on $`S^1`$ with nontrivial holonomy. A six-dimensional lower bound follows only in the restricted realization class where three profiles are represented by nonzero curvature two-forms on independent transverse coordinate factors: each factor then has dimension at least two, giving $`2+2+2=6`$. If a separate four-dimensional physical base is supplied and dimensions add, the familiar $`4+6=10`$ realization follows; neither the four-dimensional base nor ten-dimensional necessity is selected by B0. The shared circle is common phase or holonomy data and is counted once.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 906eba951ecbdde54f1efc4636294bf6dd8397535a4987384ada88a178589ade
paper_id: the-modal-triplet-theory-program-b0-why-description-for-eb6e91b2
release_state: zenodo_released
released_version: v1.0
title: |
  The Modal Triplet Theory Program B0:  
  Circle–Lens–Nil as an Obstruction Taxonomy  
  and Its Minimal Curvature Realizations
zenodo_doi: 10.5281/zenodo.18354990
zenodo_record_id: 18354990
zenodo_url: "https://zenodo.org/records/18354990"
---

# Revision note for version 2

#### Supersedes.

Version 1 of Program B0.

#### Reason.

The former paper claimed an exhaustive, mutually irreducible three-type classification without fixing a category or higher descent problem. It also identified nontrivial holonomy with nonzero curvature and promoted a four-dimensional input plus a conditional six-dimensional construction to a forced ten-dimensional conclusion.

#### Resolution.

Version 2 replaces the exclusivity theorem by a typed coarse taxonomy, proves re-encoding invariance only under explicit compatibility, separates flat holonomy from curvature, and confines the $`2+2+2`$ lower bound to independent transverse nonzero-curvature realizations. Dimension addition and the four-dimensional base are stated as hypotheses.

#### Retained content.

Return memory, descriptive redundancy, and chart termination remain useful CLN diagnostics, and geometric circle-bundle models remain important examples.

#### Open boundary.

No theorem here proves that CLN exhausts higher descent, that a lens space or nilmanifold is physically selected, that the three roles are globally nested, that physical time is a compact circle, or that spacetime must be ten-dimensional.

# Scope and Imported Data

Program A0 supplies typed reductions, representative sections, exact recovery, autonomous descent, and admissibility domains . Program A1 supplies chart transitions and encoding trajectories, with physical causality entering only after a Lorentzian and hyperbolic bridge . Program A2 separates chart partiality and branch underdetermination from algorithmic undecidability . B0 classifies three recurring *diagnostics* of these structures.

The word “obstruction” is used in a broad encoding sense. It does not assert a specific cohomology class unless a coefficient object, cover, cocycle degree, and equivalence relation are declared.

<div id="def:atlas" class="definition">

**Definition 1** (Typed encoding atlas). A typed encoding atlas consists of:

- upper domains $`U_\alpha\subseteq X`$;

- effective images $`Z_\alpha`$ and reductions $`P_\alpha:U_\alpha\to Z_\alpha`$;

- declared overlap domains $`D_{\beta\alpha}\subseteq Z_\alpha`$;

- partial transition maps or relations $`f_{\beta\alpha}:D_{\beta\alpha}\rightharpoonup Z_\beta`$; and

- equivalence relations $`\simeq_\alpha`$ specifying when two effective representatives carry the same declared content.

All composites below are restricted to their actual domains.

</div>

<div class="remark">

*Remark 2*. A representative section of a surjective reduction may exist even when the reduction is noninjective. Redundancy, exact upper recovery, and descent are therefore separate questions, as proved in Program A0.

</div>

# Three Coarse Obstruction Profiles

## Circle: return memory

<div id="def:circle" class="definition">

**Definition 3** (Circle profile). Let
``` math
\gamma=(\alpha_0,\alpha_1,\ldots,\alpha_n=\alpha_0)
```
be a closed composable chain. On the common domain of definition, let
``` math
h_\gamma
:=
f_{\alpha_0\alpha_{n-1}}\circ\cdots\circ
f_{\alpha_2\alpha_1}\circ f_{\alpha_1\alpha_0}.
```
The chain has a *circle profile* if $`h_\gamma`$ is not equivalent to the identity under the declared chart equivalence.

</div>

Circle therefore means return memory, monodromy, or holonomy. Whether it is an inconsistency, a gauge transformation, or a lawful local-system action depends on the target category.

## Lens: redundancy

<div id="def:lens" class="definition">

**Definition 4** (Lens profile). A reduction $`P_\alpha:U_\alpha\to Z_\alpha`$ has a *lens profile* on a set $`V\subseteq Z_\alpha`$ if some $`z\in V`$ has two distinct upper representatives,
``` math
x\neq x',
\qquad
P_\alpha(x)=P_\alpha(x')=z,
```
or, more generally, if the declared representation functor is not faithful on the relevant objects or arrows.

</div>

Lens therefore means quotient, projective, finite-sheet, or other redundancy. It does not imply that a representative section is absent, that reduced dynamics fails to descend, or that the global topology is a lens space.

## Nil: partiality or extension failure

<div id="def:nil" class="definition">

**Definition 5** (Nil profile). A chart system has a *nil profile* at a boundary datum $`z`$ if a declared continuation or transition required by the encoding problem has no value at $`z`$, and no extension in the declared atlas satisfies the stated compatibility conditions.

</div>

Nil therefore means termination or anchoring of the chosen encoding problem. It does not imply that the upper object or upper evolution ceases to exist. Nor does it imply a nilpotent Lie algebra without an additional triangular realization.

# Independence, Coexistence, and Invariance

<div id="prop:independence" class="proposition">

**Proposition 6** (Logical independence). *None of the predicates in Definitions <a href="#def:circle" data-reference-type="ref" data-reference="def:circle">3</a>–<a href="#def:nil" data-reference-type="ref" data-reference="def:nil">5</a> implies either of the other two without additional hypotheses.*

</div>

<div class="proof">

*Proof.* A flat complex line over $`S^1`$ with nontrivial monodromy has a circle profile but can use injective local state descriptions and a globally defined transport, so lens and nil need not occur. The set map $`\{a,b\}\to\{\ast\}`$ has a lens profile but no nontrivial loop or extension boundary. A partial identity map on $`[0,1)`$ that is not extended at $`1`$ has a nil profile but is injective and has no loop. These examples separate the three predicates. ◻

</div>

<div class="remark">

*Remark 7* (Coexistence). The profiles are not mutually exclusive. A partial many-to-one chart system may also carry nontrivial return transport. A primary CLN label can be assigned by a diagnostic decision tree, but the ordering of that tree is a convention, not a theorem of irreducibility.

</div>

<div id="prop:firstorder" class="proposition">

**Proposition 8** (First-order diagnostic completeness). *Fix a finite chart query and test only:*

1.  *existence of every required transition;*

2.  *uniqueness or faithfulness of the required representation; and*

3.  *identity of every required closed-chain return.*

*If a test fails, it is diagnosed respectively by nil, lens, or circle after any earlier failures have been recorded. If no test fails, this diagnostic detects no CLN profile.*

</div>

<div class="proof">

*Proof.* This is the exhaustive decision tree for the three declared predicates. ◻

</div>

<div class="remark">

*Remark 9* (No universal exhaustiveness). Proposition <a href="#prop:firstorder" data-reference-type="ref" data-reference="prop:firstorder">8</a> is not a classification of all mathematical obstructions. Higher Cech or gerbe descent, nonabelian coherence, analytic blow-up, spectral-domain failure, non-Hausdorff quotients, and other realization-specific phenomena require their own objects and equivalences. An exhaustive theorem would have to specify a category or higher category of encodings, its morphisms and refinements, and the full descent problem.

</div>

<div class="definition">

**Definition 10** (Compatible re-encoding). Two typed atlases are compatibly re-encoded if there are chartwise isomorphisms $`g_\alpha:Z_\alpha\to Z'_\alpha`$ and corresponding upper isomorphisms that preserve reductions, equivalence relations, transition domains, and transition maps:
``` math
g_\beta\circ f_{\beta\alpha}
=
f'_{\beta\alpha}\circ g_\alpha
```
where both sides are defined.

</div>

<div id="thm:invariance" class="theorem">

**Theorem 11** (Profile invariance under compatible re-encoding). *Under a compatible re-encoding:*

1.  *a return map changes by conjugation, $`h'_\gamma=g_{\alpha_0}h_\gamma g_{\alpha_0}^{-1}`$;*

2.  *reduction-fiber multiplicity and faithfulness are preserved; and*

3.  *the existence or nonexistence of a compatible transition extension is preserved.*

*Hence the three profile predicates are invariant.*

</div>

<div class="proof">

*Proof.* The transition intertwining identities telescope around a closed chain and give the conjugation formula. Bijective upper and lower re-encodings preserve equality and inequality within reduction fibers. The same commuting squares transport an extension in either direction, so extension existence is preserved. ◻

</div>

# Holonomy Is Not Curvature

Let $`\theta`$ be the angular coordinate on $`S^1=\mathbb R/2\pi\mathbb Z`$ and consider the trivial complex line with connection
``` math
\nabla=d+\mathrm i a\,d\theta,
\qquad a\in\mathbb R.
```
Its curvature is
``` math
F_\nabla=d(\mathrm i a\,d\theta)=0,
```
but its holonomy around the positively oriented circle is
``` math
\operatorname{Hol}_{S^1}(\nabla)
=
\exp(-2\pi\mathrm i a),
```
which is nontrivial when $`a\notin\mathbb Z`$.

<div id="thm:flat" class="theorem">

**Theorem 12** (Flat circle profile). *A one-dimensional carrier can support nontrivial return holonomy with zero curvature. Therefore nontrivial circle-profile data does not imply a nonzero curvature two-form or a two-dimensional carrier.*

</div>

<div class="proof">

*Proof.* The connection above is flat and has the displayed nontrivial holonomy. ◻

</div>

More generally, flat bundles encode representations of the fundamental group, while curvature controls infinitesimal holonomy . Global monodromy can therefore survive when curvature vanishes identically.

<div class="corollary">

**Corollary 13** (When two dimensions are required). *If a realization explicitly requires a nonzero differential two-form $`F\in\Omega^2(B)`$, then $`\dim B\geq2`$.*

</div>

<div class="proof">

*Proof.* The exterior square of a vector space of dimension zero or one is zero. ◻

</div>

This corollary applies to a *nonzero-curvature realization class*; it does not apply to the general circle profile of Definition <a href="#def:circle" data-reference-type="ref" data-reference="def:circle">3</a>.

# Lens and Nil as Geometric Examples, Not Consequences

The names lens and nil have useful geometric models.

## Lens-space model

The lens space $`L(p,1)`$ is the quotient $`S^3/\mathbb Z_p`$. Up to orientation, it is also the unit-circle bundle of a complex line bundle over $`S^2\cong\mathbb{CP}^1`$ with first Chern number $`p`$ . Its finite quotient and projective structure make it a natural *example* of lens-profile bookkeeping. A many-to-one reduction does not, however, select $`p`$, a Chern class, or a lens-space total space.

## Nilmanifold model

Let $`H_3(\mathbb R)`$ be the upper-unitriangular Heisenberg group,
``` math
n(x,y,z)=
\begin{pmatrix}
1&x&z\\
0&1&y\\
0&0&1
\end{pmatrix}.
```
Its multiplication contains the triangular cross-term
``` math
n(x,y,z)n(x',y',z')
=
n(x+x',y+y',z+z'+xy').
```
Quotient by the integer lattice gives the compact Heisenberg nilmanifold $`\mathrm{Nil}_3`$, a circle bundle over $`T^2`$ . This is a natural model of triangular transport or anchoring. Chart termination alone does not select this group, its lattice, or its metric.

<div class="remark">

*Remark 14* (Parallel circle bundles). $`L(p,1)`$ and $`\mathrm{Nil}_3`$ are circle-bundle total spaces over different bases and with different topology. They are not literally nested. A string such as
``` math
S^1\subset L(p,1)\subset\mathrm{Nil}_3
```
is therefore not a general manifold construction. The lawful recursive object is a filtration of carrier or operator data, with any global circle-bundle realizations supplied separately.

</div>

# The Conditional 2+2+2 Curvature Realization

<div id="def:curvatureclass" class="definition">

**Definition 15** (Independent transverse curvature realization). An independent transverse three-profile curvature realization consists of a smooth internal base $`B`$, subbundles $`H_C,H_L,H_N\subseteq TB`$, three declared line or principal bundles with connections $`\nabla_C,\nabla_L,\nabla_N`$, and their curvature two-forms $`F_C,F_L,F_N`$ such that:

1.  $`H_C\oplus H_L\oplus H_N`$ injects as a direct subbundle of $`TB`$;

2.  $`F_i|_{\Lambda^2H_i}`$ is nonzero somewhere for $`i\in\{C,L,N\}`$; and

3.  the three factors are independent coordinate channels rather than three labels on one reused tangent plane.

</div>

<div id="thm:six" class="theorem">

**Theorem 16** (Minimal nonzero-curvature realization). *Every realization satisfying Definition <a href="#def:curvatureclass" data-reference-type="ref" data-reference="def:curvatureclass">15</a> obeys
``` math
\dim B
\geq
\operatorname{rank}H_C+
\operatorname{rank}H_L+
\operatorname{rank}H_N
\geq 2+2+2=6.
```
The lower bound is sharp within this realization class.*

</div>

<div class="proof">

*Proof.* A nonzero alternating two-form on $`H_i`$ requires $`\operatorname{rank}H_i\geq2`$. Direct-sum transversality adds the three ranks, proving the lower bound. For sharpness, take $`B=S^2_C\times S^2_L\times S^2_N`$. On each factor use the Hopf circle bundle with its standard connection, and let $`F_i`$ be the pullback of its nonzero curvature form to $`B`$. Then $`\dim B=6`$ and all three conditions hold. ◻

</div>

<div class="remark">

*Remark 17* (What the theorem does not say). The theorem does not show that every CLN profile needs curvature, that the three channels must be transverse in nature, or that the realizing six-manifold is unique. Without (R1)–(R3), dimensions need not add. Reused, overlapping, quotient, or discrete data can occupy fewer independent coordinate directions.

</div>

# Dimension Bookkeeping and the 4+6 Branch

<div id="prop:additivity" class="proposition">

**Proposition 18** (Conditional dimension additivity). *If a physical realization is supplied as a product
``` math
M=Y\times X
```
of smooth manifolds, or as a smooth fiber bundle with base $`Y`$ and fiber $`X`$, then
``` math
\dim M=\dim Y+\dim X.
```
If $`\dim Y=4`$ and $`\dim X=6`$, then $`\dim M=10`$.*

</div>

<div class="proof">

*Proof.* For a product, $`T_{(y,x)}M\cong T_yY\oplus T_xX`$. For a smooth fiber bundle, local trivializations give the same dimension sum. ◻

</div>

<div class="remark">

*Remark 19* (The four-dimensional base is input). B0 does not select $`\dim Y=4`$, Lorentzian signature, three spatial directions, or a physical time variable. These are supplied by a later physical realization or selection theorem. Consequently B0 proves no unconditional ten-dimensional necessity.

</div>

## The world-in-world component count

Let $`P`$ and $`I`$ have rank-three tangent spaces and let
``` math
Q_x\in\operatorname{Hom}(T_xP,T_xI)\cong\operatorname{Mat}(3,\mathbb R).
```
The number $`3\times3=9`$ counts components of $`Q_x`$, not dimensions of a manifold product. With inner products and positive determinant, polar decomposition gives locally
``` math
\operatorname{Mat}(3,\mathbb R)
=
\mathfrak{so}(3)\oplus\operatorname{Sym}(3,\mathbb R),
\qquad
9=3+6.
```
Further,
``` math
\operatorname{Sym}(3,\mathbb R)
=
\mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O,
\qquad
6=1+2+3.
```
Thus the component census
``` math
1+3\times3=(1+3)+(1+2+3)=4+6
```
is exact as local linear algebra after the ordering component is supplied. It is not, by itself, a globalization to $`Y^4\times X^6`$.

## The shared circle

A common $`U(1)`$ phase or holonomy line may be pulled through all three carrier lanes. If it is the same line, it is counted once. Treating that line as a bundle fiber and then adding another Cartesian circle double-counts it. Physical time is not identified with the compact phase circle without a separate noncompact lift and dynamical bridge.

# Current MTT Interpretation

The corrected structural reading is:

Circle.  
Shared phase, return memory, or holonomy.

Lens.  
Finite, projective, signed-sheet, or quotient transport.

Nil.  
Triangular transport, anchoring, or termination in a selected operator filtration.

This taxonomy can be represented by a rank pattern such as $`1+2+3`$ without asserting three nested manifolds. In the current q79 program, the trace line, trace-zero plane, and reused rank-three carrier are a later selected carrier construction. Equality of ranks does not identify that carrier with the local world-in-world strain space; a same-source connection and Hessian intertwiner is still required.

The smooth model $`L(3,1)\times\mathrm{Nil}_3`$ remains a lawful auxiliary six-manifold. It is not thereby the selected q79 Fu–Yau compactification. B0 supplies no theorem identifying those global spaces.

# Consequences for Downstream Papers

1.  A gravity paper may use circle-profile holonomy only after it supplies a connection, metric, and field equation. Holonomy alone is not Einstein gravity.

2.  A gauge paper may use lens-profile redundancy only after it supplies a group action, principal or associated bundle, connection, and dynamics.

3.  A quantization paper may use nil-profile termination only after it supplies an algebra, representation, spectral or integral condition, and physical observable map.

4.  A proto-spinor paper may use CLN as typed carrier roles. Spinorial, particle, mass, and statistics claims need their separate structures.

5.  A ten-dimensional action may use $`Y^4\times X^6`$ as a declared realization. B0 does not derive that action or its base dimension.

# Scoped B0 Theorem

<div id="thm:scope" class="theorem">

**Theorem 20** (Circle–lens–nil taxonomy with conditional curvature bound). *For a typed encoding atlas:*

1.  *Definitions <a href="#def:circle" data-reference-type="ref" data-reference="def:circle">3</a>–<a href="#def:nil" data-reference-type="ref" data-reference="def:nil">5</a> give three distinct coarse profiles: return memory, reduction redundancy, and extension failure;*

2.  *the profiles are logically independent, may coexist, and are invariant under compatible re-encoding;*

3.  *the three-predicate decision tree is exhaustive only for its declared first-order diagnostic, not for arbitrary higher descent;*

4.  *nontrivial holonomy can be flat and one-dimensional;*

5.  *if all three profiles are separately represented by nonzero curvature two-forms on independent transverse factors, the internal carrier has dimension at least six, and $`2+2+2=6`$ is sharp in that class; and*

6.  *a ten-dimensional $`4+6`$ realization follows only after a separate four-dimensional base and dimension-additive product or fiber-bundle structure are supplied.*

</div>

<div class="proof">

*Proof.* Items 1–3 are Definitions <a href="#def:circle" data-reference-type="ref" data-reference="def:circle">3</a>–<a href="#def:nil" data-reference-type="ref" data-reference="def:nil">5</a>, Propositions <a href="#prop:independence" data-reference-type="ref" data-reference="prop:independence">6</a>–<a href="#prop:firstorder" data-reference-type="ref" data-reference="prop:firstorder">8</a>, and Theorem <a href="#thm:invariance" data-reference-type="ref" data-reference="thm:invariance">11</a>. Item 4 is Theorem <a href="#thm:flat" data-reference-type="ref" data-reference="thm:flat">12</a>. Item 5 is Theorem <a href="#thm:six" data-reference-type="ref" data-reference="thm:six">16</a>. Item 6 is Proposition <a href="#prop:additivity" data-reference-type="ref" data-reference="prop:additivity">18</a> and its stated hypotheses. ◻

</div>

# Version Delta and Research Frontier

Relative to version 1, this revision:

- replaces “exactly three and only three” by a nonexhaustive typed taxonomy plus an explicitly bounded first-order decision tree;

- withdraws mutual irreducibility and tri-layer necessity as universal theorems;

- distinguishes flat monodromy from curvature and gives an explicit flat $`S^1`$ example;

- makes dimension additivity depend on independent transverse coordinate factors;

- retains $`2+2+2=6`$ only as the sharp minimum of the declared nonzero-curvature realization class;

- states that the four-dimensional base is imported, not selected;

- removes unconditional ten-dimensional necessity; and

- separates CLN carrier roles from literal lens-space, nilmanifold, product, or nesting claims.

The next theorem target is not another dimension count. It is a same-source global intertwiner from the local $`1+2+3`$ strain decomposition to the selected q79 carrier, preserving transitions, the shared line, connections, inner products, Hessians, and the operators used downstream.

# Conclusion

Circle, lens, and nil remain useful because they ask three different questions: what returns after a loop, how many representatives survive a reduction, and where a chosen encoding stops. Their usefulness does not require an unsupported exhaustiveness theorem.

The dimensional conclusion is likewise precise. Three independent nonzero-curvature channels require at least six transverse dimensions, and this bound is attained. Flat return memory can require less. Ten dimensions arise when a four-dimensional physical base is separately supplied and paired with a six-dimensional internal realization. This scoped result is strong enough to organize the later MTT program without treating taxonomy as topology or an input base as a derived theorem.

<div class="thebibliography">

9

P. Nero, *The Modal Triplet Theory Program A0: A Structural Theory of Reduced Description*, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program A1: Coherent Kinematics*, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program A2: Conditional Computability and Finite Prediction Depth*, version 2, 2026.

S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry*, volume I, Wiley, 1963.

W. M. Boothby and H. C. Wang, “On contact manifolds,” *Annals of Mathematics* 68 (1958), 721–734.

W. P. Thurston, *Three-Dimensional Geometry and Topology*, volume 1, Princeton University Press, 1997.

</div>
