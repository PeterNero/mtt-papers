---
abstract: |
  We give a typed formulation of encoding intersections and determine when such an intersection is actually rigid. Compatibility means that a declared set of geometric, redundancy, quantum, anomaly, and overlap constraints has at least one common realization. Local rigidity means that a realization is isolated after the declared equivalences have been quotiented. Infinitesimal rigidity, persistence, and global uniqueness are different properties.

  On a finite-dimensional moduli chart, if the combined constraint map has injective derivative at a solution, that solution is locally isolated. For clean transverse constraint submanifolds, the intersection dimension is the ambient dimension minus the sum of codimensions. These theorems make rigidity conditional on the category, representation class, topology, overlap maps, anomaly equations, and deformation notion. Mere coexistence of three labels does not imply rigidity: a compatible intersection can contain a continuum, and several isolated realizations can all be locally rigid.

  We distinguish classical bundle-cocycle consistency from quantum gauge anomalies. Anomaly cancellation is necessary for a declared chiral quantum gauge realization but does not select a unique group or representation. Within the fixed selected finite MTT carrier, later exact packets establish a 48-state family-diagonal chiral representation, the faithful global group $`(SU(3)\times SU(2)\times U(1))/\mathbb Z_6`$, and a unique anomaly-free hypercharge line for the completed finite algebra. We reproduce the relevant anomaly cancellations and state their exact scope. They prove one selected compatibility branch, not an exhaustive classification of alternative representations, topologies, actions, or ultraviolet completions. Program B4 therefore supplies a conditional rigidity theorem and a Standard Model compatibility certificate, not a uniqueness theorem for the observed theory.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: cd29276ede02f9971e2782edcaff830a40c2ff9f7917a25c6d26fc485d5088f9
paper_id: the-modal-triplet-theory-program-b4-encoding-intersecti-633a4113
release_state: zenodo_released
released_version: v2
title: |
  The Modal Triplet Theory Program B4:
  Typed Encoding Intersections, Conditional Rigidity,
  and Standard Model Compatibility
zenodo_doi: 10.5281/zenodo.21652656
zenodo_record_id: 21652656
zenodo_url: "https://zenodo.org/records/21652656"
---

# Revision note for version 2

<div class="description">

Version 1 of Program B4.

The first version called triple intersections generically rigid without specifying a topology, deformation class, independent constraint equations, or quotient by equivalence. It also conflated classical overlap failure with quantum anomaly and moved from Standard Model consistency to an informal explanation of its exceptional selection.

Version 2 defines compatibility, local rigidity, infinitesimal rigidity, persistence, and global uniqueness separately. It proves a full-rank local rigidity criterion and a transverse intersection dimension theorem, states the required representation/anomaly/overlap contract, and gives explicit nonuniqueness countermodels.

Combining independently meaningful constraints can narrow a realization space; anomaly equations can remove candidate chiral representations; and the Standard Model furnishes an important compatible realization.

No theorem here exhausts all gauge groups, global quotients, representations, bundle topologies, anomaly mechanisms, actions, quantum completions, or beyond-Standard-Model branches. Consequently no global uniqueness or inevitability claim is made.

</div>

# How to Read Program B4

This paper studies a question that is easy to phrase too strongly: if several encodings agree on one realization, has that realization been selected uniquely? The answer depends on what kind of agreement has been proved. Program B4 therefore uses four distinct levels of claim:

1.  **Compatibility:** at least one candidate satisfies all declared constraints.

2.  **Local rigidity:** a particular candidate has no nearby inequivalent deformation that also satisfies them.

3.  **Conditional uniqueness:** a datum such as the hypercharge line is unique inside an already fixed carrier and representation class.

4.  **Global selection:** every allowed candidate has been classified and exactly one equivalence class survives.

Most of the constructive Standard Model evidence used here reaches the first level and selected instances of the third. The Jacobian and transversality results explain how the second can be certified. The fourth remains a classification problem and cannot be obtained merely by strengthening the description of one successful branch.

## Object picture: filters on a candidate landscape

Think of $`\mathcal M`$ as a landscape whose points encode complete candidate realizations, not just numerical parameter values. One point may include a global gauge group, a bundle, matter representations, overlap maps, a quantum algebra, and an action. Each constraint locus removes the candidates that fail one part of the contract. Their intersection $`\mathcal Z`$ is what remains after all declared filters have been applied.

Three geometrically different outcomes are possible. The filters may leave a curve, so compatible theories still deform continuously. They may leave several isolated points, so every survivor is locally rigid but no survivor is globally preferred. Or they may leave one point in the declared candidate class. Only the last case proves uniqueness, and even then the declaration of the candidate class is part of the theorem.

## Argument map

Sections 3 and 4 define the candidate space, its quotient, and the local rank tests. Sections 5 and 6 separate classical gluing from quantum anomaly cancellation. Section 7 then inserts the selected A46–A50 finite-carrier data and checks that they form one coherent Standard Model compatibility packet. Section 8 explains why this successful packet is not yet an exhaustive selection theorem. This order is deliberate: the local mathematics first tells us exactly what the later computational packets do and do not establish.

# Scope, Dependencies, and Current Evidence

Program A0 supplies typed reductions, equivalence relations, admissible domains, and exact factorization criteria . Program B0 treats circle, lens, and nil as nonexhaustive profiles rather than literal factors or unique physical theories . Program B1 obtains gravitational geometry only after a Lorentzian metric, physical carrier, and action are supplied  . Program B2 obtains gauge theory only after a group action, principal bundle, connection, invariant pairing, and action are supplied  . Program B3 separates a discrete survivor filter from a complex quantum reconstruction .

Program B4 therefore does not intersect three words. It intersects explicitly typed realization classes whose data have already been declared.

## Later selected-branch results

Three later results are directly relevant:

A46.
A 48-state, three-family chiral carrier $`\mathbb C^3_{\rm family}\otimes\mathcal H_{16}`$ with family-diagonal gauge action and an exact anomaly table .

A47.
Native unitary automorphisms $`U(1)`$, $`SU(2)`$, and $`SU(3)`$ on the selected rank carriers, with faithful kernel $`\mathbb Z_6`$ on the A46 matter rows  .

A50.
For the completed fixed finite algebra and the A46 spectrum, a one-dimensional anomaly-free abelian phase nullspace with primitive hypercharge vector .

All three are derived-exact at their declared finite selected-branch tier. They strengthen the existence side of this paper. Their own claim boundaries exclude exhaustive ultraviolet selection, full no-knob Standard Model values, and classification of all alternative carriers.

In the landscape picture, these packets specify and verify one distinguished point together with several coordinates internal to that point. A46 fixes the matter carrier and its anomaly rows, A47 identifies the kernel of the group action, and A50 fixes the primitive abelian direction in the chosen phase space. They are mutually reinforcing because they act on the same carrier. They do not, by themselves, enumerate every other landscape on which a different carrier or global group could live.

# Typed Encoding-Intersection Data

## The category must be fixed

<div id="def:intersection-datum" class="definition">

**Definition 1** (Intersection datum). An *encoding-intersection datum* consists of:

1.  a category or structured class $`\mathcal E`$ of candidate realizations;

2.  an equivalence relation or groupoid of admissible re-encodings;

3.  a topology, smooth structure, or deformation functor when rigidity is to be discussed;

4.  constraint predicates or maps for geometric transport, redundancy, quantum reconstruction, anomalies, and overlap compatibility; and

5.  declared boundary conditions, regularity, and source data.

</div>

Examples of data hidden by an untyped “encoding space” include spacetime dimension and signature, spin or $`\mathrm{Spin}^c`$ structure, the global form of a gauge group, principal-bundle topology, matter representations, the observable algebra, and the class of allowed deformations.

## Constraint loci

After quotienting or choosing a local slice for the declared equivalences, let $`\mathcal M`$ denote a moduli object of candidate realizations. Write
``` math
\mathcal C_{\mathrm{geo}},\quad \mathcal C_{\mathrm{red}},\quad \mathcal C_{\mathrm{qm}},\quad \mathcal C_{\mathrm{an}},\quad \mathcal C_{\mathrm{ov}}
 \subseteq \mathcal M
```
for the loci satisfying the supplied geometric, redundancy, quantum, anomaly, and overlap contracts. The common solution locus is
``` math
\mathcal Z
 =
 \mathcal C_{\mathrm{geo}}\cap\mathcal C_{\mathrm{red}}\cap\mathcal C_{\mathrm{qm}}\cap\mathcal C_{\mathrm{an}}\cap\mathcal C_{\mathrm{ov}}.
```
The five labels are organizational. They need not be independent, smooth, or nonempty.

<div class="definition">

**Definition 2** (Compatibility and realization). The datum is *compatible* when $`\mathcal Z\ne\varnothing`$. A *realization* is an equivalence class $`[e]\in\mathcal Z`$.

</div>

Compatibility is an existence statement. Exhibiting one realization proves nonemptiness and nothing about the number of other realizations.

## Four different rigidity predicates

<div id="def:local-rigidity" class="definition">

**Definition 3** (Local rigidity). A realization $`[e]\in\mathcal Z`$ is *locally rigid* if it is isolated in $`\mathcal Z`$ with the declared quotient topology.

</div>

<div id="def:inf-rigidity" class="definition">

**Definition 4** (Infinitesimal rigidity). On a smooth local moduli chart where the constraints are represented by a map $`F`$, a solution $`e`$ is *infinitesimally rigid* if
``` math
\ker dF_e=\{0\}.
```

</div>

<div class="definition">

**Definition 5** (Global uniqueness). The datum is *globally unique* if $`\mathcal Z`$ contains exactly one equivalence class.

</div>

<div class="definition">

**Definition 6** (Persistence). A solution *persists* under a declared parameter perturbation if a nearby solution exists for every sufficiently small allowed parameter, with the declared regularity.

</div>

Local rigidity, infinitesimal rigidity, persistence, and global uniqueness do not imply one another without additional hypotheses. In particular, an overdetermined isolated solution can disappear under a small perturbation.

# Conditional Rigidity Theorems

## A full-rank criterion

<div id="thm:jacobian" class="theorem">

**Theorem 7** (Injective-Jacobian local rigidity). *Let $`\mathcal M`$ be a smooth $`n`$-manifold, let $`F:\mathcal M\to\mathbb R^m`$ be smooth with $`m\ge n`$, and let $`e\in F^{-1}(0)`$. If
``` math
\mathop{\mathrm{rank}}dF_e=n,
```
then $`e`$ is locally isolated in $`F^{-1}(0)`$.*

</div>

<div class="proof">

*Proof.* Since $`dF_e`$ is injective, there is a linear projection $`L:\mathbb R^m\to\mathbb R^n`$ such that $`d(L\circ F)_e`$ is invertible. By the inverse-function theorem, $`L\circ F`$ is a diffeomorphism from a neighborhood of $`e`$ onto a neighborhood of zero. In that neighborhood, $`F(x)=0`$ implies $`(L\circ F)(x)=0`$, hence $`x=e`$. ◻

</div>

<div class="remark">

*Remark 8* (Quotient directions). If a group acts by equivalences, orbit directions normally lie in the kernel of the unquotiented derivative. Theorem <a href="#thm:jacobian" data-reference-type="ref" data-reference="thm:jacobian">7</a> must be applied on a valid local slice or to the deformation complex modulo infinitesimal automorphisms.

</div>

## Transverse intersections

<div id="thm:transverse" class="theorem">

**Theorem 9** (Dimension of a transverse compatibility locus). *Let $`\mathcal M`$ be an $`n`$-manifold and let $`C_1,\ldots,C_k\subseteq\mathcal M`$ be embedded submanifolds of codimensions $`c_1,\ldots,c_k`$. If they meet transversely at every point of their common intersection, then that intersection is a submanifold of dimension
``` math
n-\sum_{j=1}^k c_j.
```
In particular, dimension zero gives local discreteness; positive dimension gives continuous compatible deformations .*

</div>

<div class="proof">

*Proof.* Locally represent each $`C_j`$ as the regular zero set of a submersion. Transversality says that the combined derivative is surjective. The regular-value theorem applied to the combined map gives the stated dimension. ◻

</div>

<div class="corollary">

**Corollary 10** (What a rigidity certificate must show). *A finite-dimensional local rigidity claim is certified by an explicit constraint map and a rank or equivalent deformation-complex calculation after all equivalence directions are removed. Merely listing several requirements does not establish their independence.*

</div>

This criterion also explains why adding more named principles need not make a theory more rigid. If two principles impose the same local equation, their derivative rows are dependent and no new direction is removed. What matters is the rank of the combined constraint operator on the quotient tangent space, not the number of labels attached to it.

## Three counterexamples

<div id="prop:continuum" class="proposition">

**Proposition 11** (Compatibility need not be rigid). *Three compatible constraint labels can have a continuous common solution set.*

</div>

<div class="proof">

*Proof.* Take $`\mathcal M=\mathbb R^2`$ and let all three constraint loci be
``` math
C_1=C_2=C_3=\{(x,y):y=0\}.
```
Their common intersection is a line. Repeating one condition under three names adds no codimension. ◻

</div>

<div id="prop:two-points" class="proposition">

**Proposition 12** (Local rigidity need not give uniqueness). *Every point of a compatibility locus can be locally rigid while the datum has more than one realization.*

</div>

<div class="proof">

*Proof.* Take $`\mathcal M=\mathbb R`$ and $`F(x)=x^2-1`$. The solution locus is $`\{-1,+1\}`$. Both points are isolated and have nonzero derivative, but neither is globally selected. ◻

</div>

<div class="remark">

*Remark 13* (Full rank is sufficient, not necessary). The equation $`F(x)=x^2=0`$ has an isolated solution at $`0`$, although $`dF_0=0`$. Singular methods may prove rigidity where Theorem <a href="#thm:jacobian" data-reference-type="ref" data-reference="thm:jacobian">7</a> does not apply.

</div>

## The word “generic”

A genericity theorem requires a topology or measure on the space of constraint maps, a perturbation class, and a transversality or prevalence theorem. Even then, it answers a question inside that chosen ensemble. Program B4 makes no unqualified claim that geometric, gauge, and quantum compatibility is generically empty, finite, or rigid.

# Representation, Overlap, and Quantum Contracts

## Representation class

A gauge-representation constraint is meaningful only after fixing:

1.  the local Lie algebra and global group;

2.  the base dimension, signature, and spin structure;

3.  the allowed principal bundles and topological sectors;

4.  the matter and scalar representation category;

5.  chirality, reality, and family assumptions;

6.  boundary conditions and allowed large transformations; and

7.  the equivalence relation on representations.

A discrete list of irreducible representations can make every list entry isolated in the discrete topology. This does not make one entry globally unique. Conversely, continuous coupling or moduli directions can remain after the representation labels are fixed.

## Overlap contract

Let $`P\to X`$ be a principal $`G`$-bundle with local transition functions $`g_{\alpha\beta}`$. The classical bundle-gluing condition is
``` math
g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=e
```
on triple overlaps. A connection, associated matter bundle, and any survivor or quantum source map must transform compatibly with this cocycle.

<div class="definition">

**Definition 14** (Typed overlap compatibility). A candidate intersection is *overlap compatible* when all declared transition maps satisfy their cocycle laws and every structure map in the intersection commutes with those transitions on its stated domain.

</div>

Failure of this classical cocycle condition means that the proposed bundle or descent datum was not constructed. It is not, by itself, a quantum gauge anomaly.

## Quantum contract

By Program B3, a quantum layer requires at least a complex observable algebra, a positive state, a representation, dynamics, and effects or instruments. Gauge symmetry must act by the declared automorphisms and be compatible with the physical state or constraint construction. A finite representation table and anomaly cancellation do not alone supply this quantum contract.

# Anomalies: Necessary Constraints, Not a Selection Theorem

## Classical and quantum obstructions

A local quantum gauge anomaly is an obstruction to preserving the gauge Ward or BRST identities after quantization. In perturbative chiral gauge theory it is represented by local cohomological descent data and group-theoretic anomaly coefficients. A global anomaly is a possible nontrivial phase or determinant- line obstruction under a large gauge transformation. These depend on the dimension, global group, representations, base topology, and spin data  .

<div id="prop:anomaly-necessary" class="proposition">

**Proposition 15** (Anomaly cancellation is necessary but not sufficient). *For a declared chiral quantum gauge realization, cancellation of every anomaly included in its consistency contract is necessary for gauge invariance. Cancellation alone does not prove existence, locality, unitarity, ultraviolet completion, or uniqueness of the theory.*

</div>

<div class="proof">

*Proof.* A nonzero anomaly obstructs the declared gauge identity, so the candidate fails that contract. For the converse limitation, anomaly coefficients depend only on part of the theory’s data. Distinct actions, couplings, global groups, matter sectors, and vector-like extensions can have the same vanishing coefficients. ◻

</div>

## Anomaly equations do not fix abelian normalization

<div id="thm:scaling" class="theorem">

**Theorem 16** (Homogeneous hypercharge-scaling no-go). *Fix the nonabelian representations of a four-dimensional chiral gauge theory. Suppose a nonzero hypercharge vector $`Y`$ cancels the mixed $`G^2U(1)`$, mixed gravitational-$`U(1)`$, and $`U(1)^3`$ anomalies. Then $`cY`$ also cancels them for every real $`c`$. Thus anomaly cancellation alone cannot isolate a nonzero abelian normalization.*

</div>

<div class="proof">

*Proof.* The mixed nonabelian and gravitational coefficients are homogeneous linear functions of $`Y`$, while the cubic coefficient is homogeneous of degree three. Their zero sets are invariant under $`Y\mapsto cY`$. ◻

</div>

A primitive charge lattice, global $`U(1)`$ group, coupling convention, or other normalization condition must therefore be fixed. A50 does precisely more than solve homogeneous anomaly equations: it works inside a selected finite algebra, fixes the phase coordinates, and selects the primitive null vector in that declared representation.

## Anomaly-free extensions

<div id="prop:vectorlike" class="proposition">

**Proposition 17** (Vector-like extension counterexample). *Let a four-dimensional chiral gauge representation be perturbatively anomaly-free. Adding a left-handed representation $`R_y`$ together with its conjugate $`\overline R_{-y}`$ leaves all local perturbative gauge and mixed gravitational anomaly coefficients unchanged.*

</div>

<div class="proof">

*Proof.* The two members contribute opposite cubic nonabelian indices, opposite $`G^2U(1)`$ and gravitational-$`U(1)`$ coefficients, and opposite $`U(1)^3`$ coefficients. Their sum vanishes. ◻

</div>

Global anomalies and the rest of the physical contract must still be checked. Nevertheless, Proposition <a href="#prop:vectorlike" data-reference-type="ref" data-reference="prop:vectorlike">17</a> gives infinitely many representation categories in which anomaly cancellation cannot by itself select the Standard Model.

# A Standard Model Compatibility Packet

## Declared chiral carrier

Use left-handed Weyl fields and one neutral singlet per family:
``` math
\begin{array}{c|c|c|c|c}
\text{field} & SU(3) & SU(2) & Y & \text{multiplicity}\\
\hline
Q     & \mathbf 3             & \mathbf 2 & 1/6  & 6\\
u^c   & \overline{\mathbf 3}  & \mathbf 1 & -2/3 & 3\\
d^c   & \overline{\mathbf 3}  & \mathbf 1 & 1/3  & 3\\
L     & \mathbf 1             & \mathbf 2 & -1/2 & 2\\
e^c   & \mathbf 1             & \mathbf 1 & 1    & 1\\
N^c   & \mathbf 1             & \mathbf 1 & 0    & 1
\end{array}
```
This is the one-family $`\mathcal H_{16}`$ used by A46. Three family copies give the 48-state chiral carrier.

The table should be read as the concrete common object on which the following certificates meet. The anomaly sums test its local quantum consistency, the center calculation tests which global group acts faithfully, and the A50 nullspace calculation tests which abelian phase direction survives inside the completed finite algebra. Agreement of all three calculations on these same rows is the substantive compatibility result.

## Exact local anomaly sums

Using the fundamental quadratic index $`T(\mathbf 3)=T(\mathbf 2)=1/2`$, the one-family mixed anomalies are
``` math
\begin{aligned}
\mathcal A_{SU(3)^2U(1)}
 &=2\left(\frac12\right)\left(\frac16\right)
   +\left(\frac12\right)\left(-\frac23\right)
   +\left(\frac12\right)\left(\frac13\right)=0,\\
\mathcal A_{SU(2)^2U(1)}
 &=3\left(\frac12\right)\left(\frac16\right)
   +\left(\frac12\right)\left(-\frac12\right)=0.
\end{aligned}
```
The abelian and mixed gravitational coefficients are
``` math
\begin{aligned}
\mathcal A_{U(1)^3}
 &=6\left(\frac16\right)^3
  +3\left(-\frac23\right)^3
  +3\left(\frac13\right)^3
  +2\left(-\frac12\right)^3+1^3+0^3=0,\\
\mathcal A_{\mathrm{grav}^2U(1)}
 &=6\left(\frac16\right)
  +3\left(-\frac23\right)
  +3\left(\frac13\right)
  +2\left(-\frac12\right)+1+0=0.
\end{aligned}
```
For the cubic $`SU(3)`$ anomaly, $`Q`$ contributes two fundamentals and $`u^c,d^c`$ contribute two antifundamentals, so
``` math
\mathcal A_{SU(3)^3}=2-1-1=0.
```
There is no perturbative cubic $`SU(2)`$ anomaly for these pseudoreal representations. The Witten global anomaly cancels because one family has three color copies of the $`Q`$ doublet plus one $`L`$ doublet, hence four weak doublets; three families have twelve . These are exactly the rows certified in A46.

## Faithful global group

The direct product $`SU(3)\times SU(2)\times U(1)`$ does not act faithfully on the displayed matter rows. A47 enumerates the centers and obtains the diagonal kernel $`\mathbb Z_6`$. On that selected carrier the faithful global group is
``` math
G_{\mathrm{SM}}
 =
 \frac{SU(3)\times SU(2)\times U(1)_Y}{\mathbb Z_6}.
```
This is stronger than specifying the Lie algebra $`\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1)`$, because it records the global action on the matter representation.

## The selected hypercharge line

In A50 the abelian phase coordinates $`(\alpha_{\mathbb C},\mu_{M_3},\nu_{\mathbb C_N})`$ satisfy two independent linear anomaly equations,
``` math
\alpha_{\mathbb C}+3\mu_{M_3}=0,
 \qquad
 \alpha_{\mathbb C}-\nu_{\mathbb C_N}=0.
```
Their nullspace is one-dimensional with primitive vector
``` math
(3,-1,3),
```
which emits
``` math
6Y=(1,-4,2,-3,6,0)
```
on $`(Q,u^c,d^c,L,e^c,N^c)`$. The cubic anomaly then vanishes. The word “unique” here means one anomaly-free phase line inside the fixed completed finite algebra and A46 edge representation. It does not quantify over other algebras, particle lists, global groups, or ultraviolet mechanisms.

## Geometric and quantum scope

On a supplied four-dimensional Lorentzian spin background, these matter representations can be coupled covariantly to the corresponding gauge bundle. That establishes compatibility with background geometry; it does not derive Einstein gravity or quantize gravity. Likewise, a quantum Standard Model requires a gauge-fixed or gauge-invariant quantum field construction, states, renormalization, and observables. The representation and anomaly packet is necessary input to that construction, not its replacement.

<div id="thm:sm" class="theorem">

**Theorem 18** (Scoped Standard Model compatibility). *Fix:*

1.  *a four-dimensional Lorentzian spin background and admissible gauge bundles;*

2.  *the A46 three-family chiral carrier;*

3.  *the A47 faithful global group $`G_{\mathrm{SM}}`$; and*

4.  *the A50 selected hypercharge line.*

*Then the displayed local gauge and mixed gravitational anomaly coefficients vanish, the $`SU(2)`$ Witten parity obstruction vanishes, and the gauge action is compatible with the declared family-diagonal representation. This proves a nonempty selected representation/anomaly intersection.*

</div>

<div class="proof">

*Proof.* The local and global anomaly calculations are given above and are multiplied, without changing zero or even parity, by the three family copies. A47 identifies the faithful kernel of the action, and A50 identifies the primitive abelian phase line on the same finite carrier. ◻

</div>

# Why This Does Not Select the Standard Model Globally

## Existence is not exhaustiveness

Theorem <a href="#thm:sm" data-reference-type="ref" data-reference="thm:sm">18</a> exhibits one point in a declared compatibility locus. It does not prove that:

- every other global gauge group or quotient has been classified;

- every anomaly-free chiral or vector-like representation has been excluded;

- every bundle topology or spin background has been considered;

- every Green–Schwarz, inflow, or ultraviolet cancellation mechanism has been excluded;

- the Higgs, Yukawa, flavor, neutrino, or symmetry-breaking sectors are uniquely selected; or

- the measured couplings and masses follow from the same source.

The neutral singlet $`N^c`$ itself illustrates the role of the representation class: because it has $`Y=0`$ and is nonabelian-neutral, adding or removing it does not change the elementary gauge anomaly sums above, although it changes the finite geometry and neutrino sector. A49-A50 select it through additional finite-geometry axioms, not through the anomaly table alone.

## Local versus global uniqueness

A46-A50 can establish uniqueness statements inside a fixed carrier: the faithful kernel of one action, the minimal completion under declared finite-geometry axioms, and the abelian null line in one phase space. These are valuable local or conditional selection results. Proposition  <a href="#prop:two-points" data-reference-type="ref" data-reference="prop:two-points">12</a> shows why they cannot be promoted to global uniqueness without a proof that the candidate class itself is exhaustive.

## Required exhaustive-selection certificate

<div id="def:selection" class="definition">

**Definition 19** (Exhaustive selection certificate). An *exhaustive selection certificate* for the observed Standard Model must:

1.  specify the candidate category and equivalence relation;

2.  fix the dimension, signature, spin data, global gauge-group class, bundle topologies, and representation bounds;

3.  state all overlap, locality, anomaly, quantum, and action constraints;

4.  prove that every candidate is represented in the classification;

5.  decide every candidate against the same constraints;

6.  prove that the surviving quotient has exactly one element, or report all survivors; and

7.  independently verify any computational enumeration and exactness bounds.

</div>

Without items 1–4, failure to find an alternative is only a search result. Without item 5, constraints may have been applied asymmetrically. Without item 6, local rigidity has been mistaken for uniqueness.

# Scoped B4 Theorem

<div id="thm:scoped" class="theorem">

**Theorem 20** (Typed intersections and conditional rigidity). *For the declared data of this paper:*

1.  *compatibility is nonemptiness of a common typed constraint locus;*

2.  *one compatible realization does not imply local rigidity or uniqueness;*

3.  *an injective combined Jacobian on a quotient moduli chart is sufficient for local rigidity;*

4.  *a clean transverse intersection has the dimension stated in Theorem <a href="#thm:transverse" data-reference-type="ref" data-reference="thm:transverse">9</a>;*

5.  *anomaly cancellation is necessary for the corresponding chiral quantum gauge contract but is not sufficient for a unique theory;*

6.  *homogeneous anomaly equations do not fix nonzero abelian normalization;*

7.  *vector-like pairs preserve local perturbative anomaly cancellation;*

8.  *A46-A50 prove one exact selected finite representation/anomaly branch and the conditional uniqueness statements internal to that branch; and*

9.  *global Standard Model uniqueness would require the exhaustive certificate of Definition <a href="#def:selection" data-reference-type="ref" data-reference="def:selection">19</a>.*

</div>

<div class="proof">

*Proof.* Items 1–2 follow from the definitions and Propositions <a href="#prop:continuum" data-reference-type="ref" data-reference="prop:continuum">11</a>–<a href="#prop:two-points" data-reference-type="ref" data-reference="prop:two-points">12</a>. Item 3 is Theorem <a href="#thm:jacobian" data-reference-type="ref" data-reference="thm:jacobian">7</a>; item 4 is Theorem <a href="#thm:transverse" data-reference-type="ref" data-reference="thm:transverse">9</a>. Item 5 is Proposition <a href="#prop:anomaly-necessary" data-reference-type="ref" data-reference="prop:anomaly-necessary">15</a>; item 6 is Theorem <a href="#thm:scaling" data-reference-type="ref" data-reference="thm:scaling">16</a>; item 7 is Proposition <a href="#prop:vectorlike" data-reference-type="ref" data-reference="prop:vectorlike">17</a>. Item 8 is the scoped content of Theorem <a href="#thm:sm" data-reference-type="ref" data-reference="thm:sm">18</a> and the cited exact packets. Item 9 is the distinction between one selected branch and quantification over the candidate category. ◻

</div>

# Version Delta and Research Frontier

Relative to version 1, this revision:

- withdraws the untyped claim that triple intersections are generically rigid;

- makes the category, equivalence relation, topology, deformation class, and constraint maps explicit;

- separates compatibility, local rigidity, infinitesimal rigidity, persistence, and global uniqueness;

- proves a full-rank local rigidity theorem and a transverse dimension theorem;

- supplies continuum-compatible and multiple-isolated-solution counterexamples;

- makes representation rigidity conditional on a fixed global group, topology, representation class, and quotient;

- distinguishes classical bundle-cocycle failure from local and global quantum anomalies;

- proves that anomaly cancellation alone cannot fix abelian normalization or exclude vector-like extensions;

- replaces the old “Standard Model resolves circle, lens, and nil” theorem by a typed representation/anomaly compatibility theorem;

- incorporates the exact A46, A47, and A50 selected finite-branch results at their declared scope; and

- states the exhaustive classification certificate required for any global Standard Model selection claim.

The next rigidity frontier is not another qualitative intersection argument. It is an explicit deformation complex or finite candidate classifier for a declared upper MTT source. The source must emit the geometry, global gauge group, representations, anomaly complex, quantum action, and overlap maps. After quotienting automorphisms, its tangent cohomology or Jacobian must be computed. Global selection then requires an exhaustive classification of all allowed disconnected branches.

# Conclusion

Intersections can be powerful. Independent constraints can reduce a large candidate space to isolated realizations, and the rank and transversality theorems state exactly when that happens locally. But the narrowing is a property of specified equations in a specified category, not a consequence of counting the words circle, lens, and nil.

The Standard Model provides a concrete compatibility success. In the selected finite MTT branch, the chiral carrier, anomaly table, faithful $`\mathbb Z_6`$ quotient, and shared hypercharge line are exact and mutually consistent. This is stronger than an analogy. Its honest meaning is also narrower than inevitability: it establishes one selected branch and several conditional uniqueness statements inside that branch.

Program B4 now provides the missing logical bridge. Compatibility proves existence, a Jacobian or deformation complex proves local rigidity, and an exhaustive classification proves global uniqueness. Keeping those three certificates separate allows later MTT results to strengthen the Standard Model case without repeatedly turning a successful realization into an unsupported theorem that no alternative exists.

<div class="thebibliography">

99

P. Nero, *The Modal Triplet Theory Program A0: A Structural Theory of Reduced Description*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B0: Circle–Lens–Nil as an Obstruction Taxonomy and Its Minimal Curvature Realizations*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B1: Loop-Transport Consistency and the Conditional Gravity Realization*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B2: Gauge Redundancy, Global Sections, and the Conditional Yang–Mills Realization*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B3: Discrete Survivor Filters and Conditional Quantum Reconstruction*, revised v2, 2026.

P. Nero, *Typed Family-Diagonal Chiral Standard Model Representation and Anomaly Table*, MTT results reproducibility capsule, result `typed_family_representation`, SHA-256 `528af6955b3b7207a9db178d14d95cb4078f895f946a7d204fa680bc5754f657`, 2026.

P. Nero, *Native Bundle-Automorphism Gauge Group and $`\mathbb Z_6`$ Kernel*, MTT results reproducibility capsule, result `native_gauge_group`, SHA-256 `eeb8c7bb501d151a53ba2df109654e34ea4735560338c86e978107c9b5678582`, 2026.

P. Nero, *Selected Neutral Summand and Unique Anomaly-Free Shared Hypercharge Line*, MTT results reproducibility capsule, result `neutral_summand_hypercharge`, SHA-256 `89a1bb179af408da9d1d8408a9063331d21c8e429bb7a9bb52976bbf857e172c`, 2026.

V. Guillemin and A. Pollack, *Differential Topology*, Prentice–Hall, 1974.

J. M. Lee, *Introduction to Smooth Manifolds*, second edition, Springer, 2013.

R. A. Bertlmann, *Anomalies in Quantum Field Theory*, Oxford University Press, 1996.

A. Bilal, “Lectures on anomalies,” arXiv:0802.0634, 2008.

E. Witten, “An $`SU(2)`$ anomaly,” *Physics Letters B* 117 (1982), 324–328.

</div>

# Computational Evidence and Reproducibility

The numerical and machine-verifiable claims used by this paper are archived in the curated repository, `https://github.com/PeterNero/mtt-results-repro`. The mapped authority/result identifiers are `no result rows mapped`. Claim tiers in that capsule distinguish exact derivation, certified numerics, profile replay, conditional results, and open obligations.
