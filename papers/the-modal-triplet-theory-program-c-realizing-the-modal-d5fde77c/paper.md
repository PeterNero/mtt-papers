---
abstract: |
  This paper gives a typed realization dictionary for the Modal Triplet Theory (MTT) program. In the canonical physical specialization,
  ``` math
  M_{10}=Y_4\times X_6,
  ```
  where $`Y_4`$ is the four-dimensional Lorentzian spacetime and $`X_6`$ is the compact Riemannian internal space. Coordinate factors of $`X_6`$, vector bundles over $`X_6`$, Hermitian line bundles, vertical operators, and spectral projectors are distinct objects and cannot be interchanged by notation. A modal lane is therefore represented by a typed triple $`(\mathcal E_i,A_i,P_i)`$, not by an additional coordinate manifold.

  We prove the conditional operator statements needed by this dictionary. Strongly commuting self-adjoint vertical operators have a well-defined joint spectral projector, while compact resolvent, not the mere presence of discrete labels, is what gives a discrete spectrum. We also record the exact local spatial-triplet decomposition
  ``` math
  \operatorname{Mat}(3,\mathbb R)
   =
   \mathfrak{so}(3)\oplus
   \mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O,
   \qquad 9=3+(1+2+3),
  ```
  for a comparison field $`Q_{\mathrm{WW}}\in\Gamma(\operatorname{Hom}(TP,TI))`$. This is a component decomposition after a flag is chosen; it is not a multiplication of manifold dimensions.

  On the selected q=79 degree-three carrier, the global rank profile $`1+2+3`$ is realized by
  ``` math
  L_{\mathrm{shared}}\otimes
   (\mathcal O\oplus\mathcal A_0\oplus\mathcal A).
  ```
  The shared circle is line-bundle phase and holonomy data, counted once and not identified with physical time. Equality of the local and global rank profiles does not construct their connection-preserving intertwiner. The physical visible-hidden HYM endpoints, the continuum geometry-to-operator intertwiner, the selected continuum Hessian, the upper action, the general Born source theorem, and the complete worldsheet contract remain open.

  The resulting conclusion is deliberately typed: realizations can establish mathematical existence and compatibility, but nonuniqueness prevents physical prediction until a source law selects one realization and supplies its dynamics and observable map.
author:
- Peter Nero
current_version: v3
date: July 2026 Version 3
generated_from_main_tex_sha256: 31842b7410ca6dfc982f6d7cf0f3fcf24ecba94b85fa886250bd4bdc1a173524
paper_id: the-modal-triplet-theory-program-c-realizing-the-modal-d5fde77c
release_state: zenodo_released
released_version: v3
title: |
  The Modal Triplet Theory Program C:
  A Typed Dictionary for Geometric, Bundle,
  and Operator Realizations
zenodo_doi: 10.5281/zenodo.21655387
zenodo_record_id: 21655387
zenodo_url: "https://zenodo.org/records/21655387"
---

# Revision note for version 3

<div class="description">

Version 2 of Program C.

The version 2 type dictionary was correct, but its many distinctions between coordinates, bundles, operators, projectors, local strain components, and the q79 carrier were still easy to collapse when read as a theorem list.

Version 3 adds a concrete modal-lane example, a translation workflow, and plain-language explanations of the local $`3\times3`$ decomposition and global $`1+2+3`$ carrier. It sharpens the open connection-preserving intertwiner contract without claiming that the matching ranks construct it.

The joint-projector, compact-resolvent, local decomposition, shared-line, and nonselection statements remain at their version 2 tiers.

The physical realization, action, visible-hidden HYM pair, continuum intertwiner and Hessian, Born source, and complete worldsheet remain open.

</div>

# Revision note for version 2

<div class="description">

Version 1.0 of Program C.

The first version did not distinguish coordinate factors, bundles, line bundles, operators, and projectors. It also inferred the absence of global charts, purely discrete spectra, one-dimensional carriers, worldsheets, and dualities from premises that do not imply those conclusions.

Version 2 supplies the authoritative type dictionary, fixes the canonical physical product $`M_{10}=Y_4\times X_6`$, proves the valid conditional geometric and spectral statements, adds counterexamples to the withdrawn claims, and connects the local spatial-triplet representation to the selected q=79 carrier only through an explicitly open intertwiner contract.

Geometry, bundles, and operators remain useful realization languages. Different mathematical realizations can instantiate the same abstract constraint pattern, and their nonuniqueness is an important fact.

This paper does not select a physical realization, derive an action or Born rule, construct the physical visible-hidden HYM pair, execute the continuum q=79 Hessian, or complete a worldsheet theory.

</div>

# How to Use Program C

Program C is a translation manual. It should be used whenever an abstract MTT role is assigned a geometric or operator-theoretic realization. The first question is not whether the proposed object has the right informal shape, but whether it has the right mathematical type and whether every required map is defined.

## A concrete modal lane

Take a compact internal space $`X_6`$, a Hermitian vector bundle $`\mathcal E\to X_6`$, and a compatible connection $`\nabla`$. The connection Laplacian
``` math
A=\nabla^*\nabla
```
is an operator on sections of $`\mathcal E`$, once its domain is declared. If an isolated spectral cluster lies in an interval $`I`$, functional calculus defines the projector
``` math
P=\mathbf 1_I(A).
```
These three objects play different roles:

- $`\mathcal E`$ says what kind of internal field is carried;

- $`A`$ tests or evolves sections according to geometric data; and

- $`P`$ selects the modes satisfying the declared spectral criterion.

Calling all three “the lens lane” would hide the composition laws needed to combine them. The typed notation $`(\mathcal E,A,P)`$ keeps the carrier, test, and selection operation visible.

## The realization pipeline

A complete use of the dictionary proceeds in five steps.

1.  Choose the physical base and internal coordinate space.

2.  Specify the bundles, transition functions, metrics, and connections.

3.  Define closed operators on stated domains and prove the spectral properties used by the projectors.

4.  Construct the maps that compare local MTT decompositions with the selected global carrier, preserving the structures actually used.

5.  Add source selection, dynamics, states, observables, and empirical conventions before making a physical prediction.

The first three steps give a mathematical representation. The fourth gives a same-object or same-source bridge. Only the fifth can turn that bridge into a physical completion.

## Argument map

Sections 2–4 fix the status hierarchy, physical carrier, and type dictionary. Section 5 develops the operator layer. Sections 6 and 7 compare the local $`3\times3`$ strain decomposition with the selected q=79 global rank profile and state the missing intertwiner. Section 8 keeps spacetime, gauge, and HYM connections distinct. Sections 9–12 explain selection, compare standard physical formalisms, quarantine invalid older realizations, and record the current frontier.

# Scope and Logical Status

Program C begins after the typed structural and intersection results of Programs A0–B5. Its task is not to prove that a familiar physical theory is inevitable. Its task is to answer a narrower question:

> What mathematical data must be supplied for an MTT constraint pattern to be realized by a spacetime, an internal geometry, bundles, line bundles, operators, and selected spectral sectors?

A *realization* in this paper means a typed map from declared abstract data into a mathematical model that preserves the specified relations. Calling two objects “circle-like,” “lens-like,” or “nil-like” is not such a map. A realization certificate must identify domains, codomains, equivalences, connections, equations, boundary conditions, and any source data used in its construction.

## Five statuses that must remain separate

We use the following hierarchy.

Representation.
Abstract data are mapped into mathematical objects with the required types.

Conditional reconstruction.
A known formalism is recovered after its additional hypotheses are supplied.

Selected source realization.
One candidate is selected by a declared source law independent of the target observable.

Physical completion.
The selected realization has a state space, dynamics, observables, probability rule where required, and a convention map.

Empirical adequacy.
Held-out observables agree within a declared uncertainty model.

No status follows merely from the one above it. In particular, an elegant representation is not yet a source theorem, and a source theorem is not yet a quantum or phenomenological completion.

# Canonical Physical Carrier

## Product specialization

<div id="def:product" class="definition">

**Definition 1** (Canonical product realization). The canonical physical product realization used in this paper is
``` math
M_{10}=Y_4\times X_6,
```
where $`Y_4`$ is a four-dimensional globally hyperbolic Lorentzian manifold and $`X_6`$ is a compact six-dimensional Riemannian manifold. Physical causal propagation is carried by $`Y_4`$. Positive elliptic internal operators act vertically on $`X_6`$.

</div>

A nontrivial bundle $`\pi:M_{10}\to Y_4`$ may replace the global product in a more general realization, with local trivializations $`\pi^{-1}(U)\simeq U\times X_6`$. Whenever the product notation is used below, however, it means Definition <a href="#def:product" data-reference-type="ref" data-reference="def:product">1</a>; it never means three independent three-manifolds or a compact time circle.

## Coordinate factors

<div class="definition">

**Definition 2** (Coordinate factor). A *coordinate factor* $`F_i`$ is a manifold occurring in a proved product decomposition
``` math
X_6\simeq F_1\times\cdots\times F_r.
```
Its dimension contributes to $`\dim X_6`$.

</div>

<div id="prop:dimension" class="proposition">

**Proposition 3** (Dimension bookkeeping). *If $`X_6\simeq F_1\times F_2\times F_3`$, then
``` math
\dim F_1+\dim F_2+\dim F_3=6.
```
If the factors have equal dimension, each has dimension two.*

</div>

<div class="proof">

*Proof.* Dimension is additive under finite products of manifolds. The equal-factor statement follows from $`3\dim F_i=6`$. ◻

</div>

A principal $`U(1)`$ bundle or Hermitian line bundle over $`X_6`$ is not a fourth coordinate factor. Consequently
``` math
S^1_{\mathrm{shared}}\times F_1\times F_2\times F_3
```
is seven-dimensional when each $`F_i`$ is two-dimensional and cannot be used as $`X_6`$.

# The Authoritative Type Dictionary

## Objects and their roles

<div class="tabularx">

@P0.15P0.28Y@ Symbol & Type & Meaning and exclusion
$`Y_4`$ & Lorentzian manifold & Physical spacetime. It carries causal evolution; it is not a compact phase circle.
$`X_6`$ & Compact Riemannian manifold & Internal coordinate space in $`M_{10}=Y_4\times X_6`$.
$`F_i`$ & Manifold factor of $`X_6`$ & An actual coordinate factor only after a product decomposition is proved.
$`\mathcal E_i`$ & Hermitian vector bundle over $`X_6`$ & Internal representation or field carrier. Its rank is not a coordinate dimension.
$`L_{\mathrm{shared}}`$ & Hermitian line bundle with connection & Common phase or holonomy data. It is counted once and is not physical time.
$`A_i`$ & Self-adjoint vertical operator on sections of $`\mathcal E_i`$ & An operator with a stated domain; it is neither a coordinate nor a bundle.
$`P_i`$ & Spectral projector of $`A_i`$ & A bounded idempotent selecting a declared spectral cluster.
$`P_{\mathrm{coh}}`$ & Joint coherent projector & The product $`P_1P_2P_3`$ only under strong commutation, or a spectral projector of one total internal operator.
$`Q_{\mathrm{WW}}`$ & Section of $`\operatorname{Hom}(TP,TI)`$ & Local world-in-world comparison field between rank-three bundles; never a projector.
$`\mathcal O\oplus\mathcal A_0\oplus\mathcal A`$ & Rank $`1+2+3`$ q=79 carrier & Selected global trace-split representation. Matching ranks do not identify it with the local strain bundle.

</div>

<div id="prop:types" class="proposition">

**Proposition 4** (Type noninterchangeability). *A coordinate factor, a vector bundle, a line bundle, an unbounded operator, and a spectral projector cannot be identified solely because they are assigned the same modal label.*

</div>

<div class="proof">

*Proof.* A coordinate factor is an object in a manifold category. A vector or line bundle has a projection to a base and transition functions. An unbounded operator has a domain in a space of sections. A projector is a bounded idempotent endomorphism. These objects have different domains, codomains, composition laws, and invariants. An identification therefore requires explicit functors or intertwining maps preserving those structures. ◻

</div>

Unqualified notation such as $`B_i`$ is deprecated when it could mean a base, bundle, factor, boundary, or filter. The symbols in Table <a href="#tab:dictionary" data-reference-type="ref" data-reference="tab:dictionary">[tab:dictionary]</a> are used throughout the corrected corpus.

<div class="example">

**Example 5** (Equal rank does not identify the object). The trivial complex line over $`S^2`$ and the Hopf line bundle both have rank one, but their first Chern classes differ, so they are not isomorphic. Even on one fixed trivial line bundle, two connections can have different holonomy and need not be related by a permitted gauge transformation. Consequently, rank agreement is only a bookkeeping prerequisite for an intertwiner; it is not evidence that transition functions, connections, or operators agree.

</div>

# Modal Lanes and Vertical Operators

## The typed modal triple

<div class="definition">

**Definition 6** (Vertical modal lane). A vertical modal lane on $`X_6`$ is a triple
``` math
(\mathcal E_i,A_i,P_i),\qquad i=1,2,3,
```
where $`\mathcal E_i\to X_6`$ is a Hermitian bundle, $`A_i`$ is a nonnegative self-adjoint operator on a declared dense domain in $`L^2(X_6;\mathcal E_i)`$, and
``` math
P_i=\mathbf 1_{I_i}(A_i)
```
is the spectral projector for a declared isolated Borel set $`I_i`$.

</div>

If the three bundles differ, a common Hilbert bundle or specified embeddings must be supplied before the operators can be multiplied. Writing three operator symbols side by side does not create a common domain.

## Joint spectral selection

<div id="ass:strong" class="assumption">

**Assumption 7** (Strong commutation). After transport to one Hilbert space, the spectral measures of $`A_1,A_2,A_3`$ commute. Equivalently, the operators admit a joint functional calculus. Their quadratic forms have a common dense domain.

</div>

<div id="thm:joint" class="theorem">

**Theorem 8** (Joint coherent projector). *Under Assumption <a href="#ass:strong" data-reference-type="ref" data-reference="ass:strong">7</a>,
``` math
P_{\mathrm{coh}}=P_1P_2P_3
```
is an orthogonal projector independent of the order of the factors, and
``` math
\operatorname{Ran}P_{\mathrm{coh}}
 =
 \bigcap_{i=1}^3\operatorname{Ran}P_i.
```*

</div>

<div class="proof">

*Proof.* Strong commutation makes the spectral projectors pairwise commuting. The product of finitely many commuting orthogonal projectors is an orthogonal projector. Its range is their range intersection. ◻

</div>

The theorem says that three tests can be imposed simultaneously without an order ambiguity. It does not say that the three tests are independent or that their common range is nonzero. Both properties must be checked in the selected realization. This is why strong commutation is a compatibility certificate rather than a physical selection rule.

<div id="cor:sum" class="corollary">

**Corollary 9** (Single total operator). *Suppose the nonnegative quadratic-form sum $`A_{\mathrm{int}}=A_1+A_2+A_3`$ is closed. Then
``` math
\ker A_{\mathrm{int}}=\bigcap_{i=1}^3\ker A_i.
```
Thus the zero spectral projector of $`A_{\mathrm{int}}`$ may be used as $`P_{\mathrm{coh}}`$ without separately multiplying the $`P_i`$.*

</div>

<div class="proof">

*Proof.* For $`u`$ in the common form domain,
``` math
\langle u,A_{\mathrm{int}}u\rangle
 =
 \sum_i\langle u,A_i u\rangle.
```
All summands are nonnegative, so the sum vanishes exactly when every summand vanishes. ◻

</div>

## When discreteness is valid

<div id="thm:compact" class="theorem">

**Theorem 10** (Compact-resolvent discreteness). *Let $`A`$ be self-adjoint, bounded below, and have compact resolvent on a separable Hilbert space. Then its spectrum consists of eigenvalues of finite multiplicity with no finite accumulation point, apart from the standard possibility of accumulation at infinity.*

</div>

<div class="proof">

*Proof.* For $`z`$ in the resolvent set, $`(A-z)^{-1}`$ is compact and normal. The spectral theorem for compact normal operators gives a discrete nonzero spectrum with finite-dimensional eigenspaces. Applying $`\lambda\mapsto(\lambda-z)^{-1}`$ transfers this statement to $`A`$. ◻

</div>

The compact-resolvent hypothesis is essential. Multiplication by $`x`$ on $`L^2([0,1])`$ is bounded and self-adjoint with spectrum $`[0,1]`$. It is an operator realization with continuous spectrum. Therefore the version 1 claim that every admissible observable has purely discrete spectrum is withdrawn.

## Measurement and probability boundary

A spectral projector supplies a mathematical event or selected subspace. It does not by itself supply a state, a probability measure, a detector model, or an objective history. The selected q=79 one-anchor recorder closes an exact restricted capture statement on its declared commuting output algebra, but the general Born-source problem remains open. Program C therefore makes no universal measurement or probability claim.

# The Local Spatial-Triplet Representation

## World-in-world comparison field

Let $`TP`$ and $`TI`$ be oriented rank-three Euclidean vector bundles over a common base $`B`$. A local comparison field is
``` math
Q_{\mathrm{WW}}\in\Gamma\!\left(\operatorname{Hom}(TP,TI)\right).
```
After choosing local orthonormal frames, $`Q_{\mathrm{WW}}`$ is a $`3\times3`$ matrix. Its nine entries are components of one linear map, not nine coordinate dimensions.

<div id="thm:spatial" class="theorem">

**Theorem 11** (Orientation-strain and $`1+2+3`$ split). *At a nonsingular comparison background,
``` math
\operatorname{Mat}(3,\mathbb R)
 =
 \mathfrak{so}(3)\oplus\operatorname{Sym}(3,\mathbb R).
```
After an orthonormal flag is selected,
``` math
\operatorname{Sym}(3,\mathbb R)
 =
 \mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O,
```
where $`\mathcal D_0`$ is the traceless diagonal subspace and $`\mathcal O`$ is the symmetric off-diagonal subspace. Their dimensions are
``` math
3,\qquad 1,\qquad 2,\qquad 3.
```*

</div>

<div class="proof">

*Proof.* Every real matrix has the unique orthogonal decomposition
``` math
Q=\tfrac12(Q-Q^\mathsf T)+\tfrac12(Q+Q^\mathsf T).
```
The first summand is antisymmetric and has dimension three. Relative to the selected flag, a symmetric matrix decomposes uniquely into its scalar trace, traceless diagonal part, and symmetric off-diagonal part. These spaces have dimensions one, two, and three and are mutually orthogonal for the Frobenius inner product. ◻

</div>

With one separate ordering scalar, the exact component identity is
``` math
1+3\times3=(1+3)+(1+2+3)=4+6=10.
```
It does not prove $`TM_{10}\simeq TY_4\oplus TX_6`$, choose Lorentzian signature, or select the q=79 global topology. Those require transition functions, metrics, connections, and a physical source law.

## Why the old no-global-chart theorem fails

Version 1 claimed that the absence of a global reduced description forbids a global coordinate chart. The implication is not valid without an additional faithfulness axiom equating reduced descriptions with coordinate charts. Coordinate coverage is a property of a manifold and its atlas; descriptive admissibility is extra model data. A manifold diffeomorphic to $`\mathbb R^n`$ has a global chart while one may still impose context-dependent or non-global reduced descriptions on fields over it. Conversely, $`S^n`$ lacks a single global chart for topological reasons unrelated to MTT admissibility. Atlas structure is therefore a permitted realization, not a derived necessity of reduced-description failure.

# The Selected q=79 Global Carrier

## Trace-split rank profile

Let $`\pi_C:C\to B`$ be the selected degree-three spectral cover and put
``` math
\mathcal A=(\pi_C)_*\mathcal O_C,\qquad
 \mathcal A_0=\ker\!\left(\operatorname{Tr}:\mathcal A\to\mathcal O_B\right).
```
Then
``` math
\operatorname{rank}\mathcal O_B=1,\qquad
 \operatorname{rank}\mathcal A_0=2,\qquad
 \operatorname{rank}\mathcal A=3.
```
The selected global carrier is
``` math
\mathcal H_{\mathrm{CLN}}
 =
 L_{\mathrm{shared}}\otimes
 \left(\mathcal O_B\oplus\mathcal A_0\oplus\mathcal A\right),
 \qquad
 \operatorname{rank}\mathcal H_{\mathrm{CLN}}=1+2+3=6.
```

The exact arithmetic selector on the declared finite branch is
``` math
q\equiv15\pmod{64},\qquad
 q\equiv2\pmod7,\qquad
 q\equiv79\pmod{448}.
```
This proves the selected finite residue class, not a spacetime dimension or a critical worldsheet dimension.

## The shared line

The corrected Foundation constructs one universal flat $`\mathbb Z_{64}`$ differential line whose declared pullbacks give the q=79 SpinC determinant sign line, the finite $`1+2+3`$ carrier phase, the root-plane complex structure, and the finite Reynolds-Hessian square. This is stronger than saying that several isomorphic circles happen to occur: the connection and holonomy are part of the comparison.

The result is finite and flat. It does not identify the nonzero-Chern physical HYM connection, and the compact phase circle is not the noncompact ordering variable of physical time.

## The missing local-to-global intertwiner

<div id="def:intertwiner" class="definition">

**Definition 12** (Continuum realization intertwiner). A continuum realization intertwiner is a bundle map
``` math
\mathfrak I:
 \mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O
 \longrightarrow
 L_{\mathrm{shared}}\otimes
 \left(\mathcal O_B\oplus\mathcal A_0\oplus\mathcal A\right)
```
over a declared base map, together with:

1.  compatible transition functions and an isometric fiber map;

2.  preservation of the $`1+2+3`$ filtrations;

3.  equality or controlled conjugacy of the relevant connections;

4.  intertwining of covariant derivatives and vertical operators; and

5.  equality or a certified comparison of the physical Hessians.

</div>

<div class="proposition">

**Proposition 13** (Rank matching is insufficient). *The equality $`1+2+3=1+2+3`$ does not imply the existence of $`\mathfrak I`$.*

</div>

<div class="proof">

*Proof.* Equal-rank bundles can have different characteristic classes, holonomies, or connections and need not be isomorphic. Even isomorphic bundles can carry operators that are not conjugate. Each row in Definition <a href="#def:intertwiner" data-reference-type="ref" data-reference="def:intertwiner">12</a> is therefore independent of rank equality. ◻

</div>

Constructing this same-source map on the physical q=79 HYM complex is the current continuum geometry-to-operator blocker. It is not closed by the finite shared-line theorem.

The local theorem and the global carrier are therefore two verified ends of a proposed bridge. The local side explains how six strain components arise after quotienting the three orientation directions of a $`3\times3`$ comparison field. The global side supplies a selected rank-six trace-split carrier with a shared line. Definition <a href="#def:intertwiner" data-reference-type="ref" data-reference="def:intertwiner">12</a> is the load-bearing middle: without it, equality of the two dimension lists remains a structural clue rather than a derivation of the global degrees of freedom from the local comparison field.

# Bundles, Line Bundles, and Connections

## Three connection types

The following connection data must be kept typed.

1.  A spacetime connection acts on $`TY_4`$, its frame bundle, or a spin bundle and participates in the Lorentzian field equations.

2.  A gauge connection acts on a principal or associated internal bundle over $`Y_4`$ or $`M_{10}`$.

3.  A vertical HYM connection acts on a holomorphic bundle over $`X_6`$ and satisfies the declared complex and stability equations.

These connections may interact in one action or anomaly equation. They are not equal merely because each admits parallel transport.

<div class="proposition">

**Proposition 14** (Typed connection comparison). *An identification of two connection realizations requires a bundle map $`U:E\to E'`$ satisfying
``` math
U\circ\nabla=\nabla'\circ U
```
on a common declared domain. Similar holonomy language alone does not give such an identification.*

</div>

<div class="proof">

*Proof.* A connection is a differential operator obeying a Leibniz rule on sections of a particular bundle. Conjugacy by $`U`$ is exactly the condition that parallel transport and covariant differentiation agree under the comparison. ◻

</div>

## Curvature is not the whole circle story

Nonzero curvature can produce infinitesimal loop holonomy, but flat connections can also have nontrivial global holonomy on a non-simply-connected base. Thus a circle or loop response may be represented by curvature, flat monodromy, or both. Version 1’s identification of circle obstruction with nonzero curvature is replaced by this connection-and-holonomy contract.

## Current physical bundle boundary

Reference Fu–Yau and Hull–Strominger geometries establish relevant mathematical existence results. The selected MTT branch still requires an explicit visible $`U_{\eta=9}`$ bundle and a genuine hidden twisted-holomorphic locally free carrier in one positive Gauduchon/HYM chamber, with anomaly and Bianchi compatibility. Until those endpoints are constructed from the selected source, no reference geometry is the physical MTT compactification.

# Realization Contracts and Physical Selection

<div id="def:contract" class="definition">

**Definition 15** (Realization contract). A realization contract is a tuple
``` math
\mathfrak R=
 \left(
 \mathcal S,\mathcal C,\sim,\Phi,
 \mathcal E_{\mathrm{eq}},
 \mathcal B_{\partial},
 \mathcal D_{\mathrm{dyn}},
 \mathcal O_{\mathrm{obs}}
 \right),
```
where $`\mathcal S`$ is the typed abstract source, $`\mathcal C`$ is the candidate category, $`\sim`$ is the declared equivalence, $`\Phi`$ is the realization map, $`\mathcal E_{\mathrm{eq}}`$ is the equation inventory, $`\mathcal B_{\partial}`$ is the boundary/domain inventory, $`\mathcal D_{\mathrm{dyn}}`$ is the dynamics, and $`\mathcal O_{\mathrm{obs}}`$ is the observable map.

</div>

A purely mathematical realization may omit the final two rows, but then it must not be called a physical completion.

<div id="thm:nonunique" class="theorem">

**Theorem 16** (Nonuniqueness limits prediction). *Suppose two inequivalent realizations $`R_1,R_2\in\mathcal C/{\sim}`$ satisfy the same structural source data and all declared mathematical equations, but an observable has different values,
``` math
\mathcal O(R_1)\ne\mathcal O(R_2).
```
Then the structural source data do not predict $`\mathcal O`$.*

</div>

<div class="proof">

*Proof.* Both values are compatible with all premises. If the premises determined a unique value, the two values would have to agree. A selector, probability measure on realizations, or stronger source law is therefore required. ◻

</div>

This theorem states the principal limitation of the C-layer. Demonstrating many compatible realizations is useful for consistency and model discovery, but increases, rather than removes, underdetermination unless an independent selection law is supplied.

## A minimum realization certificate

Every claimed physical realization should report:

1.  source objects and source hashes;

2.  candidate category and equivalence relation;

3.  base, fibers, bundles, ranks, and transition functions;

4.  connections, domains, operator closures, and spectral assumptions;

5.  equations, boundary conditions, and anomaly inventory;

6.  the selector and every continuous or discrete primitive;

7.  dynamics, state space, probability law, and observable map;

8.  approximation errors, uncertainty transport, and held-out tests.

Missing rows define the theorem boundary; they are not filled by analogy.

# Relations to Standard Physical Formalisms

<div class="tabularx">

@P0.14P0.33Y@ Framework & Realization data that MTT can organize & Data not supplied by the dictionary alone
General relativity & Lorentzian base, frame/spin bundles, connection, curvature, local comparison field & Einstein–Hilbert or alternative action, stress tensor, field equations, hyperbolicity, normalization, and empirical solution.
Gauge theory and SM & Principal and associated bundles, representations, connections, finite projectors, anomaly tables & Selected continuum action, couplings, masses, RG transport, quantum state, and no-knob source values.
Quantum mechanics & Hilbert spaces, self-adjoint operators, spectral projectors, finite recorder models & General state preparation, Born source theorem, dynamics, detector model, and ontic-history rule.
Quantum field theory & Field bundles, local operators, classical BV complexes, finite representations & Selected renormalized quantum measure, nonperturbative completion, positivity, RG matching, and scattering/observable comparison.
String theory & Internal complex geometry, bundles, extended-carrier candidates, anomaly and duality contracts & Complete worldsheet action, GSO and analytic data, IR SCFT, selected physical bundle pair, and all-scale completion.

</div>

The current q=79 worldsheet contract is complete in five of twelve declared rows. A two-parameter sweep of a one-dimensional carrier is only a surface; it is not a quantum worldsheet until the missing target, action, gauge, boundary, anomaly, quantization, and observable data are supplied.

# Quarantined and Retired Realizations

## Old explicit Iwasawa construction

The Iwasawa manifold is a valid and useful complex non-Kahler manifold. What is withdrawn is the older MTT-specific construction that asserted a selected stable bundle, coefficient-level physical anomaly cancellation, and normalized Yukawa output without the required source, stability, and same-branch certificates. Those old values are not evidence for the selected q=79 physical branch. Iwasawa may be used as an auxiliary mathematical test geometry only when every theorem is restated and verified on its own hypotheses.

## Literal Circle–Lens–Nil products

The literal manifold $`S^1\times L(3,1)\times\mathrm{Nil}_3`$ is seven-dimensional. It is not the six-dimensional $`X_6`$ in Definition <a href="#def:product" data-reference-type="ref" data-reference="def:product">1</a>. The six-manifold $`L(3,1)\times\mathrm{Nil}_3`$ is also not the selected q=79 Fu–Yau topology; their global invariants differ. Circle–Lens–Nil remains useful as a filtration, operator profile, or parallel bundle schema, not as an automatic literal nesting of manifolds.

## Claims withdrawn from version 1

The following implications are explicitly withdrawn:

1.  no global reduced description $`\Rightarrow`$ no global coordinate chart;

2.  discrete survivors $`\Rightarrow`$ every observable has discrete spectrum;

3.  nil selection $`\Rightarrow`$ Hilbert space, projection measurement, or Born probability;

4.  saturation $`\Rightarrow`$ point carriers fail;

5.  saturation $`\Rightarrow`$ a one-dimensional carrier or worldsheet is forced;

6.  equivalent explanatory purpose $`\Rightarrow`$ a physical duality;

7.  circle, lens, and nil labels $`\Rightarrow`$ GR, QFT, or string theory is explained or selected.

Programs B4 and B5 provide the correct typed intersection and contract-relative saturation replacements.

# Current Realization Ledger

<div class="tabularx">

@Y P0.19P0.35@ Object & Status & Exact boundary
Canonical $`M_{10}=Y_4\times X_6`$ notation & Declared physical specialization & Not derived by the abstract triplet or the $`3\times3`$ component count.
Coordinate/bundle/operator/projector dictionary & Closed in this paper & Types and required comparison maps are explicit.
Joint coherent projector & Conditional theorem & Requires a common Hilbert space and strong commutation, or one total operator.
Discrete vertical spectrum & Conditional theorem & Requires compact resolvent or another explicit discreteness theorem.
Local spatial $`3+(1+2+3)`$ split & Exact & Flag-dependent component theorem; not global geometry.
Selected q=79 rank-$`1+2+3`$ carrier & Exact on selected finite carrier & Does not identify the local strain bundle.
Universal flat shared line and finite Hessian square & Exact finite theorem & Does not produce the physical nonzero-Chern HYM connection.
Physical visible-hidden bundle pair & Open: B.HS.01 & Explicit common HYM chamber and anomaly/Bianchi certificate required.
Continuum local-to-q79 intertwiner & Open: B.GEO.01 & Transition, metric, connection, derivative, operator, and Hessian rows required.
Selected rank-102 continuum execution & Open: B.OP.01 & Nineteen physical blocks, kernel removal, inverse and radii bounds required.
Upper action and automorphism transfer & Open: B.ACTION.01 & One selected upper differential/action must reproduce the lower structures.
General Born source theorem & Open: B.QM.01 & The restricted one-anchor result does not cover every apparatus context.
Complete q=79 worldsheet contract & Open: B.QG.01 & Currently five of twelve declared rows.

</div>

# Conclusion

Program C now has one precise job: to prevent category mistakes while turning abstract MTT data into mathematical models. The canonical physical specialization is $`M_{10}=Y_4\times X_6`$. Coordinate factors contribute to the dimension of $`X_6`$; bundles carry representations; line bundles carry phase and holonomy; vertical operators act on sections; spectral projectors select modes; and the local spatial triplet is a representation-theoretic $`1+2+3`$ split of strain components.

Several concrete advances survive this discipline. The local $`3+(1+2+3)`$ decomposition is exact. Joint projectors and discrete spectra follow under standard, explicit operator hypotheses. The selected q=79 carrier has an exact global $`1+2+3`$ rank profile, and one universal flat shared line controls several finite pullbacks with their connection and holonomy retained.

The remaining difficulty is no longer hidden by notation. The same-source continuum intertwiner, physical HYM endpoints, executed continuum operator, upper action, general Born source, and complete worldsheet theory are independent obligations. Until a source law selects one full realization, nonuniqueness is a limit on physical predictivity, not evidence that every realization is physically equivalent.

<div class="thebibliography">

99

P. Nero, *The Modal Triplet Theory Program A0: Typed Reduction and Structural Scope*, revised edition, 2026.

P. Nero, *The Modal Triplet Theory Program B4: Typed Encoding Intersections and Conditional Rigidity*, revised edition, 2026.

P. Nero, *The Modal Triplet Theory Program B5: Relative Saturation, Conditional Extended Carriers, and String-Like Realizations*, version 2, 2026.

P. Nero, *Modal Triplet Theory: Foundations*, version 8, 2026.

P. Nero, *World-in-World Genesis: Local Comparison Geometry and a Globalization Program*, corrected fifth edition, 2026.

P. Nero, *Consolidated Exact $`\mathbb Z_{64}`$-to-$`q=79`$ Closure Theorem*, current exact authority packet, 2026.

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators*, Academic Press, 1978.

D. Husemoller, *Fibre Bundles*, Springer, third edition, 1994.

S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry, Volume I*, Wiley, 1963.

J.-X. Fu and S.-T. Yau, The theory of superstring with flux on non-Kahler manifolds and the complex Monge–Ampere equation, *Journal of Differential Geometry* 78 (2008), 369–428.

</div>

# Computational Evidence and Reproducibility

The numerical and machine-verifiable claims used by this paper are archived in the curated repository, `https://github.com/PeterNero/mtt-results-repro`. The mapped authority/result identifiers are `no result rows mapped`. Claim tiers in that capsule distinguish exact derivation, certified numerics, profile replay, conditional results, and open obligations.
