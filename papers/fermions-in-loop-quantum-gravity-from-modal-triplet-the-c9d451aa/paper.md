---
abstract: |
  This paper studies continuum-derived fermion operators on graph-labelled spaces in Modal Triplet Theory (MTT) and loop quantum gravity (LQG). For a self-adjoint continuum Dirac operator with compact resolvent, exact spectral compression preserves, without spectral pollution, every eigenvalue in the selected finite window. For a graded Dirac operator, a symmetric spectral window also preserves the chiral index. Any unitary presentation of that finite subspace on graph data inherits these facts. The construction avoids lattice doubling because it is continuum-derived and generally nonlocal; it does not yet construct a local graph Dirac operator or derive the continuum fermion source from MTT. Separately, a smooth constant-rank family of projectors carries the exact Kato–Berry connection, but such a family requires an explicit gapped band bundle. The paper therefore gives a rigorous no-spurious-spectrum benchmark and a finite source contract, not a completed chiral-fermion quantization in LQG.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: cc07402985587346fcdc9efbf2e042dee6b93eceeda3d6e8cab1f1fc0561f393
paper_id: fermions-in-loop-quantum-gravity-from-modal-triplet-the-c9d451aa
release_state: zenodo_released
released_version: v2
title: |
  Coherent Compression of Continuum Dirac Operators on LQG Graphs:
  A Conditional MTT Construction and the Doubling Boundary
zenodo_doi: 10.5281/zenodo.21665968
zenodo_record_id: 21665968
zenodo_url: "https://zenodo.org/records/21665968"
---

# Version 2 Revision Note

Supersedes:
The first coherent-compression and no-doubling release.

Reason:
The finite-element norm-resolvent estimate and edge-logarithm Berry construction did not establish their claimed conclusions.

Resolution:
They are replaced by exact sharp spectral compression, chiral-index inheritance, and the Kato–Berry connection for a supplied smooth projector bundle.

Retained result:
A continuum spectral window can be represented unitarily on finite graph data without spurious low-energy eigenvalues.

Remaining boundary:
The MTT-selected continuum Dirac source, geometric graph map, locality, refinement, anomaly control, and physical LQG dynamics remain open.

# Problem, correction, and scope

Fermion doubling is the appearance of unwanted low-energy fermion species when a chiral continuum theory is represented by certain local lattice operators. In lattice field theory this is not merely a numerical accident. The Nielsen–Ninomiya theorem ties it to a collection of assumptions, including a fixed translationally invariant momentum-space description, locality, Hermiticity, and exact chiral structure .

The issue also appears in semiclassical LQG treatments when matter is expanded on regular lattice-like graphs using naive local stencils . Other work studies whether graph superposition or refinement changes the conclusion . These are serious questions because the Standard Model is chiral.

The first edition of this paper proposed a different strategy: begin with a continuum Dirac operator and compress it to graph data. That strategy contains a valid idea, but the proof was too strong. This edition separates three questions:

1.  Can a finite representation inherit a chosen continuum spectral window without adding eigenvalues?

2.  Does that inheritance constitute a local, fundamental graph regularization of a chiral theory?

3.  Has MTT selected the continuum operator and the graph presentation from its own geometry?

The answer to the first question is yes for exact spectral compression. The answers to the second and third are not yet established.

## Relation to the LQG embedding paper

This paper assumes, rather than proves, the canonical bridge stated in *Modal Triplet Theory and Loop Quantum Gravity: A Conditional Holst/Canonical Embedding*. That bridge itself requires a selected normalized Holst action, a $`3+1`$ split, and time gauge. Fermions add further data: a spin or $`\mathrm{Spin}^c`$ bundle, gauge representation, continuum Dirac operator, domains and boundary conditions, and a map to graph variables.

# Continuum datum and three different finite operations

Let $`M`$ be a compact Riemannian spin or $`\mathrm{Spin}^c`$ manifold, or a compact domain with elliptic self-adjoint boundary conditions. Let $`S\otimes R\to M`$ be a Hermitian spinor bundle with a finite-rank internal bundle $`R`$, and set
``` math
\mathcal H=L^2(M,S\otimes R).
```
Let $`D`$ be a self-adjoint Dirac-type operator on $`\mathcal H`$ with compact resolvent. Compact resolvent ensures that its spectrum is discrete with finite multiplicities and has no finite accumulation point.

Three operations that were previously blended together must be distinguished:

1.  A *sharp spectral projector* $`P_\Lambda=\mathrm{Id}_{[-\Lambda,\Lambda]}(D)`$ is idempotent and finite rank.

2.  A *smooth filter*, such as $`F_h=e^{-h^2D^2}`$, is bounded and smoothing but is generally neither idempotent nor finite rank.

3.  A *finite-element or graph projector* $`Q_h`$ is finite rank, but need not commute with $`D`$ and can exhibit spectral pollution unless an approximation theorem excludes it.

Only the first operation gives the exact theorem below for free. An MTT “coherent projector” must be identified with one of these mathematical types before conclusions are transferred between them.

# Exact spectral compression

<div class="definition">

**Definition 1** (Selected spectral window). For $`\Lambda>0`$, define
``` math
P_\Lambda=\mathrm{Id}_{[-\Lambda,\Lambda]}(D),
 \qquad
 \mathcal H_\Lambda=P_\Lambda\mathcal H,
 \qquad
 D_\Lambda=D|_{\mathcal H_\Lambda}.
```
Since $`D`$ has compact resolvent, $`\mathcal H_\Lambda`$ is finite-dimensional.

</div>

<div id="thm:spectral" class="theorem">

**Theorem 2** (No spurious eigenvalues under exact spectral compression). *The operator $`D_\Lambda`$ is finite-dimensional and self-adjoint, and
``` math
\operatorname{spec}(D_\Lambda)
 =
 \operatorname{spec}(D)\cap[-\Lambda,\Lambda]
```
with exactly the same algebraic and geometric multiplicities. In particular, the compression introduces no additional zero or low-energy eigenvalues.*

</div>

<div class="proof">

*Proof.* The projector $`P_\Lambda`$ is obtained from the Borel functional calculus of the self-adjoint operator $`D`$, so it commutes with $`D`$. Its range is the orthogonal direct sum of precisely the eigenspaces whose eigenvalues lie in the chosen interval. Restricting $`D`$ to that invariant sum leaves the action on every included eigenspace unchanged and excludes every other eigenspace. Self-adjointness on the finite-dimensional invariant range is immediate. ◻

</div>

## What the theorem says in plain language

The finite matrix is made from the actual continuum eigenmodes in the window. It therefore cannot invent another low-energy species: its rows and columns already span exactly the modes one decided to retain. This is a useful benchmark for any approximate graph construction.

The conclusion is also limited. The projector depends on the full continuum operator and is generally nonlocal in position space. It does not provide a local graph stencil from which the continuum theory is recovered. It preserves a supplied spectrum rather than deriving that spectrum.

# Exact chiral-index inheritance

Assume now that $`\mathcal H=\mathcal H^+\oplus\mathcal H^-`$ has grading $`\Gamma=\Gamma^*=\Gamma^{-1}`$ and
``` math
\Gamma D+D\Gamma=0.
```
Then
``` math
D=
 \begin{pmatrix}
 0&D^-\\
 D^+&0
 \end{pmatrix},
\qquad
(D^+)^*=D^-.
```
The symmetric projector $`P_\Lambda`$ commutes with $`\Gamma`$, because $`\Gamma`$ maps the $`D`$-eigenspace at $`\lambda`$ to the eigenspace at $`-\lambda`$.

<div id="thm:index" class="theorem">

**Theorem 3** (Chiral index of a symmetric spectral window). *Let $`D^+`$ be Fredholm and let $`\Lambda>0`$. Define $`\mathcal H^\pm_\Lambda=P_\Lambda\mathcal H^\pm`$ and let $`D^+_\Lambda:\mathcal H^+_\Lambda\to\mathcal H^-_\Lambda`$ be the restricted map. Then
``` math
\operatorname{ind}D^+_\Lambda
 =
 \dim\ker D^+-\dim\ker D^-
 =
 \operatorname{ind}D^+.
```*

</div>

<div class="proof">

*Proof.* The kernel of $`D^+_\Lambda`$ is $`\ker D^+`$, because every zero mode lies in every positive spectral window. The kernel of its adjoint is $`\ker D^-`$. Equivalently, on every positive eigenspace of $`D^2`$, the map $`D`$ is an isomorphism between the positive- and negative-chirality subspaces, so nonzero modes contribute equally to both sides and cancel in the index. Only the chiral zero-mode difference remains. ◻

</div>

This is index inheritance, not a construction of an anomaly-free chiral gauge theory. Gauge covariance, anomaly cancellation, reflection or Lorentzian properties, and interactions must all be supplied separately.

# Presentation on a graph

Let $`\mathcal K_\Lambda`$ be a finite-dimensional Hilbert space whose basis is indexed by graph, node, edge, or intertwiner data, and let
``` math
U_\Lambda:\mathcal H_\Lambda\longrightarrow\mathcal K_\Lambda
```
be unitary. Define
``` math
D_{\Gamma,\Lambda}
 =
 U_\Lambda D_\Lambda U_\Lambda^*.
```

<div id="cor:graph" class="corollary">

**Corollary 4** (Unitary graph presentation). *The graph-presented operator $`D_{\Gamma,\Lambda}`$ has exactly the spectrum and chiral index stated in Theorems <a href="#thm:spectral" data-reference-type="ref" data-reference="thm:spectral">2</a> and <a href="#thm:index" data-reference-type="ref" data-reference="thm:index">3</a>.*

</div>

<div class="proof">

*Proof.* Spectrum, multiplicity, kernels, and index are invariant under unitary conjugation. ◻

</div>

The corollary is exact but does not make $`D_{\Gamma,\Lambda}`$ local on the graph. A generic unitary image is a dense matrix coupling distant graph labels. The unresolved physical theorem must construct $`U_\Lambda`$ from the LQG and MTT geometry and prove whichever locality, covariance, refinement, and semiclassical properties are required.

# The Nielsen–Ninomiya boundary

The exact spectral construction does not contradict the no-go theorem because it gives up at least the strict locality and fixed translationally invariant lattice-symbol assumptions. It begins with a continuum operator, uses its global spectral projector, and in a generic graph basis produces a nonlocal matrix.

<div class="proposition">

**Proposition 5** (What compression does and does not establish). *Exact spectral compression establishes absence of *spurious spectral copies relative to the supplied continuum operator*. It does not establish a doubler-free local lattice regularization satisfying all Nielsen–Ninomiya hypotheses.*

</div>

<div class="proof">

*Proof.* The first statement is Theorem <a href="#thm:spectral" data-reference-type="ref" data-reference="thm:spectral">2</a>. For the second, the spectral projector is a global function of $`D`$, and no finite-range graph kernel or translationally invariant lattice symbol has been constructed. Thus the construction lies outside the simultaneous hypothesis set of the no-go theorem rather than refuting its conclusion. ◻

</div>

If one later replaces $`D_{\Gamma,\Lambda}`$ by a strictly graph-local stencil, doubling must be checked again. One must state explicitly which condition is relaxed: exact chirality, ultralocality, translation invariance, a fixed lattice, or another assumption. “The graph is irregular” is not by itself a proof that the physical spectrum is correct.

# Why the old finite-element proof is withdrawn

The first edition set $`F_h=e^{-h^2D^2}`$, projected it into a finite-element space, and asserted an $`O(h)`$ norm-resolvent estimate. The displayed argument did not prove that estimate:

1.  for any proper finite-rank orthogonal projector $`Q_h`$ on an infinite-dimensional Hilbert space, $`\|\mathrm{Id}-Q_h\|=1`$, so operator-norm convergence to the identity is impossible;

2.  the cited $`L^2`$ approximation estimate contributes a factor $`h`$, while the smoothing bound used for the $`H^1`$ norm contributes $`h^{-1}`$, yielding $`O(1)`$, not the claimed $`O(h)`$;

3.  finite-dimensional resolvents and the continuum resolvent were compared without a fully specified embedding and complement action; and

4.  the proof acknowledged a constant defect and then asserted that it did not spoil convergence without establishing the required cancellation.

This does not prove that no Galerkin or finite-element approximation can work. A corrected theorem would need a stable family of domains, graph-norm approximation, a consistent embedding, resolvent estimates on the complement, and an explicit exclusion of spectral pollution. Those results must be proved for the actual Dirac discretization rather than inferred from smoothing alone.

# Berry transport: the exact statement

Berry terms require a family, not a single projector. Let $`X`$ be a smooth parameter manifold and let $`x\mapsto P(x)`$ be a $`C^1`$ family of finite-rank orthogonal projections on one fixed Hilbert space $`\mathcal H`$, with constant rank. The ranges form a Hermitian vector bundle
``` math
\mathcal E=\bigsqcup_{x\in X}\mathrm{Ran}P(x)\longrightarrow X.
```

<div id="thm:berry" class="theorem">

**Theorem 6** (Kato–Berry connection on a projector bundle). *For a $`C^1`$ section $`s`$ of $`\mathcal E`$, the rule
``` math
\nabla^{\mathrm B}s=P\,\mathrm ds
```
defines a metric-compatible connection. Its parallel transport is unitary, and where the family is $`C^2`$ its curvature is
``` math
F^{\mathrm B}
 =
 P\,(\mathrm dP\wedge\mathrm dP)\,P.
```*

</div>

<div class="proof">

*Proof.* Since $`Ps=s`$, differentiating gives $`\mathrm dP\,s+P\,\mathrm ds=\mathrm ds`$; projection therefore maps the ordinary derivative back into the range bundle and obeys the Leibniz rule. For two range sections $`s,t`$, orthogonality of $`P`$ gives
``` math
\mathrm d\langle s,t\rangle
 =
 \langle P\,\mathrm ds,t\rangle
 +\langle s,P\,\mathrm dt\rangle,
```
so the connection is metric-compatible and its parallel transport is unitary. Applying the projected derivative twice and using $`P\,\mathrm dP\,P=0`$, obtained by differentiating $`P^2=P`$, gives the curvature formula . ◻

</div>

An isolated spectral band of a smoothly varying self-adjoint operator can produce such projectors through a Riesz contour when a uniform gap and the required operator regularity hold. Current MTT/LQG data have not yet supplied that family for the physical fermion sector. Edge-overlap matrices and a matrix logarithm are therefore not enough; frames must arise from a common gapped bundle before their Berry interpretation is valid.

# What MTT must select

The proto-spinor and shared-circle papers provide promising source language: a conditional spinorial carrier, a common determinant-line interpretation, and finite internal operators. To turn that language into the $`D`$ used above, one branch must emit:

1.  a four-dimensional Lorentzian spin or $`\mathrm{Spin}^c`$ bundle and its relation to the shared circle;

2.  the tetrad, spin connection, gauge bundle, and fermion representation;

3.  a self-adjoint Euclidean continuation or a controlled Lorentzian operator with domains and boundary conditions;

4.  the complete mass/Yukawa contribution and chirality grading;

5.  a selected finite operation – sharp projector, smooth filter, or graph approximation – with its exact type declared;

6.  a geometric map $`U_\Lambda`$ to LQG graph data; and

7.  locality, covariance, refinement, anomaly, and semiclassical certificates appropriate to the intended physical claim.

The current finite $`27\times27`$ Standard-Model carrier and its declared profile/value results can constrain the internal matrix part. They do not by themselves construct the spacetime Dirac operator, graph map, or chiral gauge measure.

# Result ledger

<div class="center">

| Object | Status | Meaning |
|:---|:---|:---|
| Continuum $`D`$ with compact resolvent | Assumed | Source datum for the exact benchmark |
| Sharp spectral window $`P_\Lambda`$ | Constructed | Finite nonlocal continuum-derived projector |
| No-spurious-spectrum theorem | Proved | Exact relative to supplied $`D`$ |
| Chiral-index inheritance | Proved | Exact for symmetric graded window |
| Graph presentation | Conditional exact | Requires unitary $`U_\Lambda`$ |
| Graph locality and refinement | Open | Not implied by unitary presentation |
| Kato–Berry connection | Proved conditionally | Requires explicit smooth constant-rank projector bundle |
| Selected MTT fermion source | Open | Must emit bundle, operator, grading, and finite operation |
| Full chiral LQG theory | Open | Gauge, anomaly, constraints, dynamics, and physical inner product |

</div>

# Version 2 revision note

Version 2 withdraws the claimed finite-element norm-resolvent proof, the unqualified no-doubling theorem, and the edge-logarithm Berry construction. It replaces them with two exact results: spectral and chiral-index inheritance under a sharp continuum spectral projector, and the standard Kato–Berry connection for an explicit smooth projector bundle. It also states which Nielsen–Ninomiya hypotheses are relinquished and identifies the continuum fermion source and graph map as open MTT/LQG bridge objects.

# Conclusion

There is a rigorous way to place a finite portion of a continuum Dirac spectrum on graph-labelled data without creating extra low-energy modes: use the actual spectral subspace and transport it unitarily. This gives MTT a clean benchmark for a coherent fermion projector and preserves the chiral index exactly.

It is not yet a fundamental graph fermion theory. The construction is continuum-derived, generally nonlocal, and only as predictive as the operator fed into it. The next decisive result is therefore a same-source theorem from the q79/proto-spinor geometry that emits the physical four-dimensional Dirac operator and a geometrically selected graph map with declared locality and refinement properties.

<div class="thebibliography">

9

J. Barnett and L. Smolin, *Fermion doubling in loop quantum gravity*, Physical Review D **92**, 064022 (2015).

R. Gambini and J. Pullin, *No fermion doubling in quantum geometry*, International Journal of Modern Physics D **24**, 1542001 (2015).

J. Zhang, Y. Liu, and M. Han, *Fermion doubling and its suppression in loop quantum gravity*, arXiv:2205.12208 (2022).

H. B. Nielsen and M. Ninomiya, *A no-go theorem for regularizing chiral fermions*, Physics Letters B **105**, 219–223 (1981).

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1976.

</div>
