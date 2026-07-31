---
abstract: |
  We replace an absolute notion of “encoding saturation” by a typed and testable relative notion. A saturation contract specifies a category of candidate realizations, its equivalences, a complete list of constraints and boundary data, and a class of allowed factorizations. A realization is saturated relative to that contract when it satisfies every declared constraint and admits no nontrivial allowed factorization. Saturation can therefore change when the candidate class, constraint inventory, equivalence, or factorization class changes.

  For a finite-dimensional local model with declared variable and constraint blocks, we prove that first-order factorization is exactly detected by the connected components of the bipartite derivative-incidence graph. A connected active graph gives infinitesimal indecomposability; together with an injective combined derivative, it gives a locally isolated, infinitesimally indecomposable realization. This is a genuine conditional saturation theorem.

  The stronger claims in the first version do not follow from saturation alone. We give explicit countermodels showing that a complete, rigid, indecomposable constraint system need not contain extended carriers, a critical dimension, or a nontrivial duality. A one-dimensional carrier is minimal only after one requires a nonconstant continuous loop or nontrivial holonomy. Critical dimensions require an explicit anomaly or central-charge defect. Duality requires an explicit invertible comparison preserving the declared dynamics and observables. String-like and brane-like structures are consequently realization classes, not inevitable consequences of three obstruction labels.

  We also separate existence, local rigidity, uniqueness within a declared candidate class, physical selection, and empirical adequacy. The current selected q=79 arithmetic theorem supplies an exact finite branch, but the physical visible-hidden Hull–Strominger endpoints, the remaining seven rows of the twelve-row worldsheet contract, and an all-scale nonperturbative completion remain open. Program B5 therefore provides a rigorous language and a finite indecomposability test for unified encodings. It does not derive string theory, a numerical critical dimension, or the physical selection of a saturated universe.
author:
- Peter Nero
current_version: v4
date: July 2026 Version 4
generated_from_main_tex_sha256: 295ecec094f2b6a5d02b3049aebb6dbf8d7dd775ccb01ea0d3e0912a2be64254
paper_id: the-modal-triplet-theory-program-b5-saturated-and-unifi-b0579f7f
release_state: zenodo_released
released_version: v4
title: |
  The Modal Triplet Theory Program B5:
  Relative Saturation, Conditional Extended Carriers,
  and String-Like Realizations
zenodo_doi: 10.5281/zenodo.21718246
zenodo_record_id: 21718246
zenodo_url: "https://zenodo.org/records/21718246"
---

# Revision note for version 4

<div class="description">

Version 3 of Program B5.

Version 3 already supplied the reviewed relative-saturation theorem, countermodels, and explanatory wiring-diagram presentation. Its managed reproducibility block nevertheless reported that no result row was mapped, although the paper uses the exact selected q=79 arithmetic packet.

Version 4 maps the A11 q=79 theorem explicitly in both canonical sources and pins the curated repository revision. The in-paper release note now records only the current version delta; the complete revision history remains in the accompanying audit. No theorem or physical-selection claim changes.

The relative saturation contract, derivative-incidence criterion, countermodels, and conditional status of extended carriers, dimensions, anomalies, and dualities are unchanged.

An exhaustive realization category, physical string background, completed q79 worldsheet, nonperturbative completion, and physical selection theorem remain open.

</div>

# How to Read Program B5

Program B5 asks whether a successful collection of constraints is genuinely one coupled construction or merely several independent theories written next to one another. The paper calls the first situation *saturated*, but only relative to a declared contract. This qualification is essential: changing which variables are primitive, which constraints count, or which factorizations are allowed can change the answer.

## The central picture: a wiring diagram

At a solution, linearize every declared constraint. Place the variable blocks on one side of a bipartite graph and the constraint blocks on the other. Draw an edge whenever changing a variable block changes a constraint block to first order. If this graph falls into two pieces, the linearized problem also falls into two independent subsystems. If it is connected, every variable block is tied into one first-order network.

This wiring picture gives the paper’s exact finite test. It does not say that the full nonlinear theory cannot be separated by a clever change of variables, nor that the solution is globally unique. Those stronger claims need their own certificates. The injective-derivative condition supplies one additional fact: the same solution is locally isolated.

## Five questions kept separate

The argument proceeds through five questions.

1.  Is the candidate complete with respect to the displayed constraint inventory?

2.  Is the displayed system indecomposable with respect to the allowed factorizations?

3.  Does a separate carrier requirement force positive dimension or a worldsheet-like sweep?

4.  Do explicit anomaly, criticality, and duality data make that sweep a string-like physical realization?

5.  Is one realization selected by a source law and empirically adequate?

The derivative-incidence theorem answers the second question locally. The loop theorem answers a narrow version of the third. The anomaly, duality, and string packages state what must be added for the fourth. Nothing in the word “saturation” answers the fifth.

## Suggested reading routes

Readers interested in the exact mathematical contribution can move from the contract definitions to the derivative-incidence theorem and its finite example. Readers interested in the string interpretation should then read the countermodels before the worldsheet, anomaly, and duality sections; those countermodels prevent conditional realization mechanisms from being mistaken for consequences of saturation. The final theorem ledger and reusable audit collect the result and every remaining boundary.

# Scope and Dependencies

Program B5 begins after the typed intersection theory of Program B4. It does not infer a unified theory directly from the words circle, lens, and nil. Program A0 supplies typed reductions, quotient relations, and factorization criteria . Program B0 treats circle, lens, and nil as useful but nonexhaustive obstruction profiles . Programs B1–B3 state the additional geometric, gauge, and quantum data needed before those profiles become physical theories . Program B4 defines a common realization locus and separates compatibility, local rigidity, persistence, and global uniqueness .

The question addressed here is narrower:

> Given a fully declared intersection contract, when do its constraint blocks fail to split into independent subsystems, and what additional assumptions are needed before that indecomposability can be realized by strings, worldsheets, critical dimensions, anomalies, or dualities?

## Terminology boundary

The word *saturation* has several standard mathematical meanings. Ideal saturation $`I:f^\infty`$, saturation of a sublattice, a saturated subsheaf, and the contract-relative notion introduced below are different constructions. An exact computation involving one of the first three does not prove descriptive saturation unless a map between the two notions is supplied.

## Current q=79 evidence

One later selected result is relevant as a boundary marker. The exact q=79 packet proves, on its stated finite branch, that
``` math
q\equiv 15\pmod {64},
 \qquad
 q\equiv 2\pmod 7,
 \qquad
 q\equiv 79\pmod {448}.
```
This is an exact finite arithmetic result . The integer $`79`$ is not a spacetime dimension, a worldsheet central charge, or a proof of string criticality.

The current physical string branch remains conditional:

1.  the selected visible and hidden non-pullback holomorphic bundles and their common positive HYM chamber are not yet constructed;

2.  the q=79 worldsheet contract is complete in five of twelve declared rows; and

3.  all-genus or other nonperturbative completion, positivity, and asymptotic control remain open.

Those open rows are not assumptions silently imported into the theorems below.

# A Relative Saturation Contract

## Typed data

<div id="def:contract" class="definition">

**Definition 1** (Saturation contract). A *saturation contract* is a tuple
``` math
\mathfrak C
 =
 \bigl(
 \mathcal C,\sim,\mathcal M,\{F_\alpha\}_{\alpha\in A},
 \mathcal B,\mathcal D,\mathcal R
 \bigr)
```
with the following data:

1.  a category or structured class $`\mathcal C`$ of candidate realizations;

2.  an equivalence relation or groupoid $`\sim`$ of admissible re-encodings;

3.  a moduli object $`\mathcal M`$, or a local slice after quotienting the declared equivalences;

4.  a finite or otherwise controlled inventory of constraint maps $`F_\alpha:\mathcal M\to W_\alpha`$;

5.  declared variable and constraint blocks $`\mathcal B`$;

6.  a class $`\mathcal D`$ of factorizations that count as a genuine separation of responsibilities; and

7.  regularity, source, boundary, and domain data $`\mathcal R`$.

</div>

The index set $`A`$ may contain geometric transport, bundle cocycle, gauge, quantum, anomaly, overlap, boundary, and refinement constraints. The labels are bookkeeping devices. Their equations need not be independent.

<div class="definition">

**Definition 2** (Contract-complete realization). The common realization locus is
``` math
\mathcal Z_{\mathfrak C}
 =
 \left\{
 [x]\in\mathcal M/{\sim}:
 F_\alpha(x)=0\ \text{for every }\alpha\in A,
 \ \text{and }\mathcal R\text{ holds}
 \right\}.
```
A point $`[x]\in\mathcal Z_{\mathfrak C}`$ is *contract complete*.

</div>

Completeness is relative to the declared inventory. The phrase “all constraints” means every row in $`A`$, not every obstruction that could be invented in a larger theory.

## Allowed factorization

<div id="def:factorization" class="definition">

**Definition 3** (Local contract factorization). Let $`[x]\in\mathcal Z_{\mathfrak C}`$. A nontrivial local factorization in the class $`\mathcal D`$ consists of:

1.  a neighborhood $`U`$ of $`[x]`$ and an allowed equivalence $`U\simeq U_1\times U_2`$, with both factors nontrivial;

2.  a partition $`A=A_1\sqcup A_2`$; and

3.  maps $`\widetilde F_\alpha`$ such that, under the equivalence,
    ``` math
    F_\alpha=
     \begin{cases}
     \widetilde F_\alpha\circ\pi_1,&\alpha\in A_1,\\
     \widetilde F_\alpha\circ\pi_2,&\alpha\in A_2.
     \end{cases}
    ```

Boundary data, sources, and equivalences must factor in the same declared sense.

</div>

<div id="def:saturation" class="definition">

**Definition 4** (Relative saturation). A contract-complete realization is *$`\mathcal D`$-saturated* when it admits no nontrivial local factorization from Definition <a href="#def:factorization" data-reference-type="ref" data-reference="def:factorization">3</a>. It is *globally $`\mathcal D`$-saturated* when no such factorization exists on its full connected component.

</div>

This definition says what is inseparable and which splittings were tested. It does not build a carrier, action, anomaly theory, or physical selector.

<div id="prop:relative" class="proposition">

**Proposition 5** (Saturation is contract relative). *Relative saturation is not an intrinsic predicate of an untyped object. Changing the constraint inventory, candidate category, equivalence, block decomposition, or allowed factorization class can change its truth value.*

</div>

<div class="proof">

*Proof.* Adding a constraint can remove a point from $`\mathcal Z_{\mathfrak C}`$. Enlarging $`\mathcal D`$ can admit a previously forbidden factorization. Refining a variable block can expose a splitting hidden by a coarse block, while quotienting by a larger equivalence can identify factors that were previously distinct. Therefore the predicate depends on the displayed contract data. ◻

</div>

# The Derivative-Incidence Criterion

## Blocked linearization

Let $`\mathcal M`$ be a smooth finite-dimensional local slice near a contract-complete point $`x`$. Write
``` math
V=T_x\mathcal M=\bigoplus_{i\in I}V_i,
 \qquad
 W=\bigoplus_{j\in J}W_j,
 \qquad
 L=DF_x:V\longrightarrow W,
```
where $`F=(F_j)_{j\in J}`$. Discard constraint blocks with zero derivative. If a variable block has no incident derivative, it is a free first-order factor and is retained as an isolated vertex.

<div class="definition">

**Definition 6** (Derivative-incidence graph). The bipartite graph $`G_x`$ has variable vertices $`I`$, constraint vertices $`J`$, and an edge $`i\!-\!j`$ exactly when
``` math
L_j|_{V_i}\ne 0.
```

</div>

<div class="definition">

**Definition 7** (First-order block factorization). A *first-order block factorization* is a pair of nonempty partitions
``` math
I=I_1\sqcup I_2,
 \qquad
 J=J_1\sqcup J_2
```
such that
``` math
L_j|_{V_i}=0
 \quad\text{whenever}\quad
 (i,j)\in(I_1\times J_2)\cup(I_2\times J_1).
```

</div>

<div id="thm:incidence" class="theorem">

**Theorem 8** (Incidence criterion for infinitesimal indecomposability). *After deleting zero constraint blocks, $`L`$ has a nontrivial first-order block factorization if and only if the derivative-incidence graph $`G_x`$ is disconnected with a partition containing variable vertices on both sides. Consequently, a connected $`G_x`$ proves first-order indecomposability relative to the declared blocks.*

</div>

<div class="proof">

*Proof.* Suppose the displayed partitions give a first-order factorization. Every nonzero derivative entry joins $`I_1`$ only to $`J_1`$ or $`I_2`$ only to $`J_2`$. There is no edge crossing between the two vertex sets, so $`G_x`$ is disconnected.

Conversely, let $`G_x=G_1\sqcup G_2`$ be a disconnection with variable vertices in both components. Put $`I_k=I\cap G_k`$ and $`J_k=J\cap G_k`$. No edge joins $`I_1`$ to $`J_2`$ or $`I_2`$ to $`J_1`$, which is exactly the vanishing condition for a first-order block factorization. More than two components can be grouped into two nonempty collections. ◻

</div>

<div id="cor:rigid-saturation" class="corollary">

**Corollary 9** (Locally rigid infinitesimal saturation). *Assume $`F(x)=0`$, $`G_x`$ is connected, and $`DF_x`$ is injective. Then $`x`$ is locally isolated in $`F^{-1}(0)`$ and first-order indecomposable relative to the declared blocks.*

</div>

<div class="proof">

*Proof.* Theorem <a href="#thm:incidence" data-reference-type="ref" data-reference="thm:incidence">8</a> gives first-order indecomposability. If $`n=\dim V`$, injectivity supplies an $`n\times n`$ nonzero minor after choosing $`n`$ target coordinates. The inverse function theorem applied to those components makes their common zero locally unique. Hence the full zero set is locally $`\{x\}`$. ◻

</div>

<div class="remark">

*Remark 10* (Exact scope). Connected incidence is a statement about the displayed linearized blocks. It does not exclude a nonlinear change of variables that factors the contract, nor does it establish global uniqueness. Injectivity is sufficient for local isolation, not necessary: singular equations can also have isolated zeros.

</div>

## A finite exact example

Let $`\mathcal M=\mathbb R^3`$ with scalar variable blocks and define
``` math
F(x_1,x_2,x_3)
 =
 \begin{pmatrix}
 x_1+x_2\\
 x_2+x_3\\
 x_3+x_1
 \end{pmatrix}.
```
The derivative matrix is
``` math
L=
 \begin{pmatrix}
 1&1&0\\
 0&1&1\\
 1&0&1
 \end{pmatrix},
 \qquad
 \det L=2.
```
Its incidence graph is a six-cycle, hence connected, and $`L`$ is invertible. The origin is therefore locally rigid and first-order indecomposable.

This example is deliberately point-valued. It contains no extended carrier, worldsheet, critical dimension, anomaly polynomial, or duality. It proves that even the conjunction of completeness, rigidity, and first-order indecomposability does not imply any of those additional structures.

The matrix also makes the two tests visibly different. Its nonzero pattern connects all six graph vertices, which certifies coupling. Its determinant certifies local isolation. A connected singular matrix could pass the first test and fail the second, while an invertible block-diagonal matrix could be locally isolated yet split into independent sectors. Saturation and rigidity therefore measure different properties.

# What Saturation Does Not Force

## Pointlike data remain possible

A pointwise field is not the same as a collection of independent points. Sections of a bundle are evaluated pointwise while their derivatives, connections, boundary conditions, and gauge transformations couple values across the base. Conversely, a finite-dimensional or zero-dimensional model can have a connected constraint graph, as the preceding example shows.

Therefore the old implication
``` math
\text{saturation}\Longrightarrow
 \text{failure of all pointlike encodings}
```
is false without a separate definition of pointlike locality and a theorem showing that every allowed local model violates a named constraint.

## The conditional carrier-minimality theorem

There is a valid narrower statement behind the earlier intuition.

<div id="thm:loop-dimension" class="theorem">

**Theorem 11** (Minimal dimension for continuous loop support). *Let $`K`$ be a compact metric carrier required to contain a nonconstant continuous loop. Then its covering dimension satisfies
``` math
\dim K\ge 1.
```
The bound is sharp because $`S^1`$ has covering dimension one and supports a non-nullhomotopic loop.*

</div>

<div class="proof">

*Proof.* A compact metric space of covering dimension zero is totally disconnected. The image of $`S^1`$ under a continuous map is connected. If the map is nonconstant, its image contains more than one point, contradicting total disconnectedness. The circle supplies the sharp example. ◻

</div>

<div class="remark">

*Remark 12*. The theorem is conditional on continuous loop support. An interval is one-dimensional but has trivial fundamental group. A circle supports holonomy but does not by itself supply a gauge group, a nil/refinement law, a worldsheet action, a quantum measure, or anomaly cancellation.

</div>

## Worldsheet-like sweeps

Suppose a one-dimensional carrier $`K`$ is propagated through an additional parameter $`t\in I`$ by a sufficiently regular family of maps $`\gamma_t:K\to X`$. The evaluation map
``` math
\Gamma:K\times I\longrightarrow X,
 \qquad
 \Gamma(k,t)=\gamma_t(k),
```
has a two-dimensional parameter domain when $`K`$ is one-dimensional. This is a *worldsheet-like sweep*. Calling it a physical worldsheet additionally requires at least:

1.  a target geometry and field space;

2.  an action and boundary conditions;

3.  gauge fixing and a quantum measure or operator construction;

4.  local and global anomaly control; and

5.  observables and a physical interpretation.

The product $`K\times I`$ alone proves none of these rows.

# Anomaly Completeness and Critical Dimensions

## The anomaly inventory must be declared

<div id="def:anomaly-contract" class="definition">

**Definition 13** (Anomaly contract). An *anomaly contract* consists of:

1.  a field and symmetry content;

2.  a quantum construction and regularization domain;

3.  a list $`\mathcal A=\{\alpha_r\}_{r\in R}`$ of local, global, mixed, gravitational, or worldsheet anomaly classes that are defined for that model;

4.  the cohomology, determinant-line, cobordism, BRST, or Ward-identity groups in which those classes live; and

5.  an allowed mechanism class $`\mathcal K`$ of counterterms, inflow, Green–Schwarz terms, or additional sectors.

</div>

<div class="definition">

**Definition 14** (Anomaly complete). A model is *$`(\mathcal A,\mathcal K)`$-anomaly complete* when every declared class is zero or is trivialized by a displayed mechanism in $`\mathcal K`$, with the compatibility equations checked.

</div>

The phrase “all potential anomalies cancel” has no invariant meaning without Definition <a href="#def:anomaly-contract" data-reference-type="ref" data-reference="def:anomaly-contract">13</a>. Classical failure of a bundle cocycle is also not automatically a quantum anomaly.

In established string constructions, criticality and anomaly cancellation are obtained from explicit worldsheet central-charge, gauge, gravitational, and inflow equations . Their existence supports string-like realizations of a sufficiently rich contract. It does not show that abstract indecomposability creates those equations.

## A conditional criticality theorem

<div id="thm:critical" class="theorem">

**Theorem 15** (Analytic anomaly-zero criterion). *Fix all realization data except a real dimension parameter $`d`$ in an open interval $`U`$. Suppose the net anomaly or central-charge defect
``` math
a:U\longrightarrow\mathbb R
```
is real analytic and not identically zero. Then the admissible set
``` math
\{d\in U:a(d)=0\}
```
is discrete. It is finite on every compact subinterval whose neighborhood is contained in $`U`$.*

</div>

<div class="proof">

*Proof.* Zeros of a nonzero real-analytic function are isolated. An infinite set of zeros in such a compact subinterval would have an accumulation point, forcing $`a`$ to vanish identically by the identity theorem, a contradiction  . ◻

</div>

<div class="remark">

*Remark 16* (Why the hypothesis matters). If $`a\equiv0`$, every $`d`$ is allowed. If $`a(d)=(d-10)(d-26)`$, two values survive. If $`a(d)=\sin(\pi d)`$, infinitely many isolated values survive. The word “anomaly” alone selects none of these functions. Moreover, ordinary spacetime dimension is already integer-valued; merely observing discreteness does not derive a critical dimension.

</div>

For several continuous moduli, one equation generally leaves a positive-dimensional zero locus. A discrete solution then requires the appropriate rank, transversality, compactness, or arithmetic hypotheses, as in Program B4.

# Duality Requires a Certificate

## Typed duality data

<div id="def:duality" class="definition">

**Definition 17** (Duality certificate). A duality between two realization descriptions $`X`$ and $`Y`$ consists of:

1.  typed source and target state or configuration spaces;

2.  maps or functors $`D:X\to Y`$ and $`E:Y\to X`$;

3.  inverse or natural-equivalence identities on the declared domains;

4.  preservation of actions, equations, symplectic or operator structures, and boundary conditions as applicable;

5.  an observable correspondence, including normalization and uncertainty; and

6.  matching anomaly and quantum-consistency data.

</div>

Different theories use different subsets of this list, but an identification cannot be inferred merely because two descriptions address similar obstructions. Standard examples such as target-space T-duality are supported by explicit transformations and quantum consistency checks  .

<div id="prop:duality" class="proposition">

**Proposition 18** (Quotienting does not manufacture duality). *If a certified duality is included in the equivalence relation $`\sim`$, then the quotient $`\mathcal M/{\sim}`$ identifies the dual descriptions. The existence of a saturated point in $`\mathcal M/{\sim}`$ does not, conversely, construct a duality certificate.*

</div>

<div class="proof">

*Proof.* The first statement is the definition of a quotient by a declared equivalence. For the converse, take a contract whose moduli space is one point and whose category has only its identity morphism. The point is contract complete and admits no nontrivial factorization, but there are no two distinct descriptions and no nontrivial duality. Alternatively, two isolated saturated points can be placed in a discrete category with no morphism between them. ◻

</div>

Thus duality webs are possible and important features of particular saturated realizations. They are not forced by relative saturation itself.

# String-Like Realizations

## Realization package

<div id="def:string-package" class="definition">

**Definition 19** (String-like realization package). A *string-like realization package* for a saturation contract contains:

1.  a one-dimensional carrier $`K`$, its allowed topologies and labels;

2.  a worldsheet or swept domain $`\Sigma`$ and target data $`X`$;

3.  a field/configuration space and an action $`S`$ with boundary conditions;

4.  a gauge and quantum construction, including its state or measure data;

5.  a declared anomaly contract and explicit trivializations;

6.  overlap, refinement, and compactification maps;

7.  every claimed duality certificate; and

8.  a map from this package into the variables and constraints of $`\mathfrak C`$.

</div>

<div id="prop:string" class="proposition">

**Proposition 20** (Conditional realization criterion). *If the map in Definition <a href="#def:string-package" data-reference-type="ref" data-reference="def:string-package">19</a> is type preserving, sends every declared equation and boundary condition of the package to the corresponding row of $`\mathfrak C`$, and its image is contract complete and $`\mathcal D`$-indecomposable, then the package realizes a saturated encoding.*

</div>

<div class="proof">

*Proof.* Type preservation makes the image a candidate in $`\mathcal C`$. Vanishing of every constraint and satisfaction of the boundary data place it in $`\mathcal Z_{\mathfrak C}`$. The assumed absence of an allowed factorization is exactly Definition <a href="#def:saturation" data-reference-type="ref" data-reference="def:saturation">4</a>. ◻

</div>

The proposition is a certificate template, not a proof that such a package exists. It also does not make its carrier ontologically fundamental.

## Branes and higher carriers

Higher-dimensional carriers can be included by replacing $`K`$ with a $`p`$-dimensional object and giving the corresponding action, gauge symmetries, charges, anomalies, and dualities. The loop-minimality theorem does not exclude them. It says only that dimension one is the smallest possible continuous carrier dimension under a nonconstant-loop requirement. It does not order physical models by plausibility.

## A useful but limited interpretation

String-like frameworks are natural *examples* to test against a rich saturation contract because they combine extended carriers, gauge data, gravity-sensitive consistency conditions, anomaly equations, and explicit dualities. The logical direction is
``` math
\text{complete string package}
 \Longrightarrow
 \text{candidate saturated realization},
```
after the map and indecomposability test are proved. The reverse implication is invalid.

This direction preserves the useful connection to string theory without turning it into a definition. Established string constructions provide rich packages that may satisfy an MTT contract. The MTT contract can then compare which rows are shared, which are stronger, and which remain open. It cannot replace the worldsheet action, quantum measure, anomaly calculation, or duality map by declaring the finished package saturated.

# Existence Is Not Physical Selection

## Four different claims

For clarity, the following statements must remain separate:

<div class="description">

$`\mathcal Z_{\mathfrak C}\ne\varnothing`$.

A point is isolated in the declared quotient topology.

Exactly one equivalence class survives in the fully enumerated candidate class.

A common source law, initial/boundary condition, or independently justified selection functional chooses that class and yields observables.

</div>

Empirical adequacy is a fifth statement: the resulting observables must agree with held-out measurements with a convention map and uncertainty budget.

<div class="proposition">

**Proposition 21** (No selection from existence alone). *If a contract has two inequivalent complete saturated realizations and no selection functional or source law distinguishing them, neither is physically selected by the contract.*

</div>

<div class="proof">

*Proof.* Both realizations satisfy exactly the predicates encoded by the contract. Any rule choosing one must therefore use information not present in those predicates. Without such additional data, the choice is underdetermined. ◻

</div>

This remains true when each point is locally rigid. Local isolation does not compare separated components.

# Current Theorem Ledger

## Results proved in this revision

1.  Saturation is a contract-relative conjunction of completeness and indecomposability.

2.  The connected components of the derivative-incidence graph exactly detect first-order block factorization relative to declared finite blocks.

3.  Connected incidence plus injective combined derivative gives local rigidity and infinitesimal indecomposability.

4.  Continuous nonconstant-loop support requires carrier dimension at least one, and $`S^1`$ makes the bound sharp.

5.  A nonzero analytic anomaly defect has isolated dimension zeros.

6.  Quotienting by a duality identifies a duality only after that duality has been constructed.

7.  Explicit countermodels show that relative saturation alone forces none of extended carriers, critical dimensions, worldsheets, anomalies, or nontrivial dualities.

## Conditional realization statements

1.  A one-dimensional carrier is minimal only for a declared continuous-loop requirement.

2.  A worldsheet-like sweep follows from a one-dimensional carrier plus an independent continuation parameter; a physical worldsheet requires the remaining action and quantum rows.

3.  Critical dimensions follow only from an explicit nontrivial anomaly or central-charge equation.

4.  A string-like package realizes saturation only after all contract maps, equations, anomalies, domains, and the indecomposability test are supplied.

## Claims not proved

This paper does not prove:

- that circle, lens, and nil exhaust all obstruction types;

- that unified descriptions must be saturated;

- that saturated descriptions must be extended or string-like;

- that one-dimensional carriers are physically preferred;

- that a numerical critical dimension is selected;

- that anomaly cancellation or duality follows automatically;

- that the q=79 finite branch is a complete string vacuum;

- that a physical branch is uniquely selected; or

- that an all-scale quantum-gravity theory has been constructed.

# A Reusable Saturation Audit

A future paper claiming a saturated or unified encoding should provide the following finite audit.

1.  **Candidate class:** objects, morphisms, regularity, topology, and boundary conditions.

2.  **Equivalence:** every quotient or gauge identification.

3.  **Constraint inventory:** explicit maps, targets, and source data.

4.  **Factorization class:** which decompositions count as separate layers.

5.  **Local test:** blocked derivative, incidence graph, rank, and kernel after quotienting.

6.  **Global test:** components, nonlinear changes of variables, and global decompositions.

7.  **Carrier test:** topology and the exact property requiring extension.

8.  **Anomaly test:** fields, anomaly classes, mechanisms, and checked trivializations.

9.  **Dimension test:** the actual equation whose zero set is claimed to be critical.

10. **Duality test:** maps, inverses, domains, dynamics, and observables.

11. **Selection test:** source law or independent selector.

12. **Empirical test:** observables, conventions, uncertainties, and held-out comparisons.

Failure of one row identifies the missing theorem. It does not invalidate the rows already proved.

# Conclusion

The useful content of saturation is not that maximal consistency mysteriously creates strings. It is that a declared family of constraints can become genuinely coupled and nonfactorizable. The derivative-incidence graph gives a finite exact test of that coupling at first order, and the rank criterion from Program B4 can simultaneously establish local isolation.

Extended carriers, worldsheets, anomaly equations, critical dimensions, and dualities remain powerful realization mechanisms. Their hypotheses must be shown, not hidden inside the word saturation. Likewise, the existence or rigidity of one realization does not select it physically. This corrected formulation preserves the unification program while turning its strongest claims into explicit mathematical obligations.

<div class="thebibliography">

99

P. Nero, *The Modal Triplet Theory Program A0: Typed Reduction, Admissibility, and Conditional Reconstruction*, MTT paper series, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program B0: Obstruction Profiles and Conditional Encoding Responses*, MTT paper series, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program B1: Conditional Geometric Reconstruction and the Gravity Encoding*, MTT paper series, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program B2: Conditional Gauge Reconstruction from Principal-Bundle Data*, MTT paper series, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program B3: Discrete Survivor Filters and Conditional Quantum Reconstruction*, MTT paper series, version 2, 2026.

P. Nero, *The Modal Triplet Theory Program B4: Typed Encoding Intersections, Conditional Rigidity, and Standard Model Compatibility*, MTT paper series, version 2, 2026.

P. Nero, *Consolidated Exact $`\mathbb Z_{64}`$ to $`q=79`$ Closure Theorem*, current selected result packet, SHA-256 prefix `ccacd5227f91ab08`, 2026.

A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.

S. G. Krantz and H. R. Parks, *A Primer of Real Analytic Functions*, second edition, Birkhauser, 2002.

L. Alvarez-Gaume and E. Witten, Gravitational anomalies, *Nuclear Physics B* **234** (1984), 269–330.

M. B. Green and J. H. Schwarz, Anomaly cancellations in supersymmetric $`D=10`$ gauge theory and superstring theory, *Physics Letters B* **149** (1984), 117–122.

T. H. Buscher, Path-integral derivation of quantum duality in nonlinear sigma-models, *Physics Letters B* **201** (1988), 466–472.

J. Polchinski, *String Theory, Volume I: An Introduction to the Bosonic String*, Cambridge University Press, 1998.

</div>

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The finite arithmetic claim used by this paper is archived in the [curated results repository at commit `31247ebb5c22`](https://github.com/PeterNero/mtt-results-repro/tree/31247ebb5c22f3fbb5443024365433c6ee0bff4a). The mapped authority/result identifier is `A11/q79_exact_theorem`. It is an exact result on the selected finite arithmetic and charge branch. It does not supply a critical dimension, a completed worldsheet, physical Hull–Strominger endpoints, or a selection theorem for a saturated universe.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
