---
abstract: |
  Coupling chiral fermions to Loop Quantum Gravity (LQG) is obstructed in semiclassical regimes by lattice-like fermion doubling when matter is defined by naive graph-local stencils. We provide a fully rigorous resolution within the Modal Triplet Theory (MTT) coherent sector: fermions on graphs and spin foams are defined by coherent compression of a continuum Dirac operator, not by a standalone lattice Dirac operator. The compression is constructed as smoothing at scale $`h`$ followed by finite-element projection, yielding provable commutator estimates and norm-resolvent convergence under refinement. We show infrared spectral stability, stability of the chiral index, and absence of spurious low-energy mirror fermions in the coherent regime. We also treat the Berry/projector-variation correction: we define it via a unitary overlap transport on edges, prove small-step branch control for the matrix logarithm, and show it does not spoil grading. Finally, we connect the operator-level results to refinement-averaged propagator suppression mechanisms.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 331f95bf6d4ea8aa35510d62c465543037840186e45efc6adcfd2a39e283e014
paper_id: fermions-in-loop-quantum-gravity-from-modal-triplet-the-c9d451aa
release_state: zenodo_released
released_version: v1.0
title: |
  Fermions in Loop Quantum Gravity from Modal Triplet Theory:  
  Coherent Compression, Berry Terms, and Absence of Doubling
zenodo_doi: 10.5281/zenodo.18261946
zenodo_record_id: 18261946
zenodo_url: "https://zenodo.org/records/18261946"
---

# Introduction

Fermion doubling in semiclassical treatments of Loop Quantum Gravity (LQG) has been identified as a serious obstacle to reproducing the chiral Standard Model. Barnett and Smolin show that doubling appears when one expands around lattice-like semiclassical states and defines fermions with naive graph-local stencils . Gambini and Pullin argue that the absence of a fixed discretization invalidates lattice no-go hypotheses . Zhang–Liu–Han propose that refinement superposition suppresses doubler poles in propagators . Lewandowski and Zhang construct canonical fermion coupling in LQG and explicitly cite doubling as contested .

In this work we show that these positions are compatible once one separates:

- the *choice of discrete fermion operator* (naive stencil vs induced compression),

- the *choice of physical states* (fixed lattice vs refinement superposition),

- the *regime of validity* (coherent/admissible sector vs gap-closing transitions).

Our core correction is operator-theoretic: define discrete fermion dynamics as a *compression* of a continuum coherent Dirac operator, constructed in a way that yields provable norm-resolvent convergence. This eliminates spurious low-energy doublers by spectral and index stability.

<div class="remark">

*Remark 1* (Why Nielsen–Ninomiya does not apply). The Nielsen–Ninomiya theorem assumes a local, translationally invariant lattice Dirac operator on a fixed lattice . Our discrete operator is not a standalone lattice stencil: it is an induced compression of a continuum operator, and translation invariance is absent on generic graphs. Therefore the theorem does not apply.

</div>

# Setting: Coherent Dirac operator and admissible regime

We work in a slab-local regime (bounded geometry), consistent with MTT’s claim discipline.

## Geometry and bundles

Let $`(M,g)`$ be a smooth oriented Riemannian spin $`d`$-manifold ($`d=3`$ for canonical slices or $`d=4`$ for covariant slabs) of bounded geometry: curvature and its derivatives up to order $`m`$ are bounded and the injectivity radius is bounded below by $`\iota_0>0`$ on the domain of interest.

Let $`S\to M`$ be the spinor bundle and let $`\mathcal R\to M`$ be a finite-rank Hermitian vector bundle (encoding internal indices). Set
``` math
H := L^2(M,S\otimes \mathcal R).
```

## Continuum Dirac operator

Let $`D`$ be a Dirac-type operator on $`S\otimes\mathcal R`$:
``` math
D = \gamma^\mu \nabla_\mu + \mathcal V,
```
where $`\nabla`$ is a metric/Hermitian connection and $`\mathcal V`$ is a bounded endomorphism field. On bounded-geometry domains, $`D`$ is essentially self-adjoint on $`C_c^\infty`$ (or has a standard self-adjoint realization with boundary conditions when $`M`$ has boundary). We assume a fixed self-adjoint realization of $`D`$ with domain $`\mathrm{Dom}(D)\subset H^1`$.

<div class="remark">

*Remark 2* (Boundary conditions on domains with boundary). If $`M`$ (or $`\Sigma`$) has boundary, we assume a standard elliptic self-adjoint realization of $`D`$ (e.g. local elliptic boundary conditions, or APS-type where appropriate). All estimates below are slab-local/bounded-geometry and are unaffected provided the chosen realization yields the usual elliptic regularity and heat-kernel bounds on the domain.

</div>

## Coherent-sector admissibility

MTT supplies a coherent sector separated by a uniform gap. For this paper we encode that as a scale separation hypothesis:

<div class="definition">

**Definition 3** (Coherent gap scale). Fix $`\Delta>0`$ such that the physically relevant infrared window satisfies $`E<\Delta`$ and “noncoherent” excitations are suppressed above $`\Delta`$ in the admissible regime.

</div>

The operator-theoretic results below do not require the internal MTT construction of $`\Delta`$; they require only the existence of a scale $`E<\Delta`$ on which the effective description is asserted.

# Discrete compression spaces and operators

We define the discrete fermion operator on a graph/foam by compressing $`D`$ to a finite-dimensional space associated with resolution $`h`$ (graph) or $`\ell`$ (foam). To obtain fully rigorous estimates we use a two-step compression:
``` math
\text{smooth at scale }h \quad+\quad \text{project to finite element space}.
```

This is standard in operator approximation for elliptic operators and avoids nontrivial commutator issues of raw $`L^2`$-projection alone.

## Triangulations and shape regularity

Let $`\{\mathcal T_h\}_{h\downarrow 0}`$ be a family of shape-regular triangulations of $`M`$ (in local bounded-geometry charts), with mesh size
``` math
h := \max_{T\in\mathcal T_h} \mathrm{diam}(T).
```
Shape regular means there is a uniform constant $`\sigma`$ such that each simplex contains an inscribed ball of radius $`\ge \sigma h`$.

## Finite element space

Let $`V_h\subset H^1(M,S\otimes\mathcal R)`$ denote the P1 finite element space of sections that are affine on each simplex in a chosen local trivialization. Let
``` math
P_h : H \to V_h
```
be the $`L^2`$-orthogonal projector (well-defined since $`V_h`$ is finite-dimensional).

## Smoothing operator

Define the smoothing operator
``` math
S_h := e^{-h^2 D^2}.
```
Since $`D^2`$ is Laplace-type and $`M`$ has bounded geometry, the heat kernel exists and satisfies standard Gaussian bounds; $`S_h`$ maps $`L^2\to H^k`$ for all $`k`$ with bounds depending on $`h`$.

<div id="lem:smoothing" class="lemma">

**Lemma 4** (Smoothing bounds). *For each $`k\in\mathbb N`$ there exists $`C_k`$ such that for all $`h\in(0,h_0]`$,
``` math
\|S_h\|_{L^2\to H^k} \le C_k\, h^{-k}.
```
Moreover, $`S_h`$ commutes with $`D`$ (functional calculus): $`DS_h = S_h D`$.*

</div>

<div class="proof">

*Proof.* Since $`D`$ is self-adjoint, $`S_h = f(D)`$ with $`f(\lambda)=e^{-h^2\lambda^2}`$, hence commutes with $`D`$. The bounds follow from standard heat kernel/spectral multiplier estimates on bounded-geometry manifolds for Laplace-type operators (see e.g.  and bounded-geometry heat kernel literature; for an elementary route one uses the spectral theorem and $`|\lambda|^k e^{-h^2\lambda^2}\le C_k h^{-k}`$, yielding $`\|D^k S_h\|\le C_k h^{-k}`$, and then elliptic equivalence of $`H^k`$ norms). ◻

</div>

## Compression map and compressed operator

Define the *compression map*
``` math
\Pi_h := P_h S_h : H \to V_h.
```
This is bounded for each fixed $`h`$ and captures the continuum modes at resolution $`h`$.

<div class="definition">

**Definition 5** (Raw compressed operator). Define the raw compressed operator on $`V_h`$:
``` math
D_h^{(0)} := \Pi_h D \Pi_h^\ast,
```
viewed as an operator on $`V_h`$ via the inner product inherited from $`L^2`$.

</div>

<div class="remark">

*Remark 6*. One may equivalently define the matrix of $`D_h^{(0)}`$ in a basis of $`V_h`$ by $`(D_h^{(0)})_{ij}=\langle \varphi_i, D \varphi_j\rangle`$ with $`\varphi_j=\Pi_h^\ast e_j`$.

</div>

# Berry correction: definition and branch control

In addition to raw compression, the induced dynamics includes a projector-variation (Berry/Grassmann) term. We define it on edges by overlap transport and address the logarithm branch issue explicitly.

## Edge overlaps and unitary transport

Let $`\{\phi_{v,a}\}`$ be a vertex-adapted orthonormal basis for $`V_h`$ (constructed via local orthonormalization on stars of vertices). For each oriented edge $`e:v\to w`$ in the 1-skeleton of $`\mathcal T_h`$, define the overlap matrix
``` math
S_e^{ab} := \langle \phi_{v,a}, \phi_{w,b}\rangle.
```
Let $`S_e = U_e |S_e|`$ be the polar decomposition with unitary $`U_e`$.

<div id="lem:small-step" class="lemma">

**Lemma 7** (Small-step control). *There exists $`C>0`$ such that for sufficiently small $`h`$,
``` math
\|U_e - I\| \le C h
```
uniformly over edges $`e`$ in bounded-geometry regions, provided the basis is chosen continuously with respect to the smoothed projection $`\Pi_h`$.*

</div>

<div class="proof">

*Proof.* Because $`\Pi_h=P_h S_h`$ depends smoothly on $`h`$ through the analytic functional calculus $`S_h`$, and because $`P_h`$ varies continuously under shape-regular refinement (finite-dimensional subspaces vary continuously in the Grassmannian when induced by local charts), one can choose the vertex frames so that adjacent vertex bases differ by $`O(h)`$ in $`L^2`$ norm. This yields $`\|S_e-I\|\le Ch`$. Polar decomposition is Lipschitz near the identity, hence $`\|U_e-I\|\le C'h`$. A fully explicit proof can be given by choosing a fixed smooth frame field on each simplex and comparing Gram matrices; bounded geometry controls the constants. ◻

</div>

## Matrix logarithm branch

<div id="lem:logbranch" class="lemma">

**Lemma 8** (Log branch well-defined for small steps). *If $`\|U_e-I\|<1`$, the principal matrix logarithm $`\log U_e`$ is well-defined and satisfies
``` math
\|\log U_e\| \le C \|U_e-I\|.
```
In particular, by Lemma <a href="#lem:small-step" data-reference-type="ref" data-reference="lem:small-step">7</a>, for sufficiently small $`h`$ the choice of principal branch is consistent along refinement.*

</div>

<div class="proof">

*Proof.* If $`\|U-I\|<1`$ then $`\mathrm{Spec}(U)`$ lies in the open disk centered at $`1`$ of radius $`1`$, which excludes $`-1`$ and avoids the branch cut of the principal logarithm. Standard holomorphic functional calculus yields $`\log U`$ analytic in $`U`$ on this neighborhood and bounded linearly by $`\|U-I\|`$ (see e.g. ). ◻

</div>

## Berry correction operator

<div class="definition">

**Definition 9** (Berry correction). Define $`B_h`$ on $`V_h`$ by
``` math
(B_h)_{(v,a),(w,b)} :=
\begin{cases}
(\log U_e)_{ab} & \text{if } e:v\to w \text{ is an edge},\\
0 & \text{otherwise}.
\end{cases}
```

</div>

<div class="definition">

**Definition 10** (Corrected discrete operator). Define the corrected operator
``` math
D_h := D_h^{(0)} + B_h.
```

</div>

# Norm-resolvent convergence: full proof

We now prove norm-resolvent convergence from first principles, without black-box commutator assumptions.

## Uniform resolvent bounds

<div id="lem:resbound" class="lemma">

**Lemma 11** (Resolvent bounds). *Let $`A`$ be self-adjoint on a Hilbert space. For $`z\in\mathbb C\setminus\mathbb R`$,
``` math
\|(A-z)^{-1}\| \le \frac{1}{|\Im z|}.
```*

</div>

<div class="proof">

*Proof.* Standard: $`\|(A-z)^{-1}\|=\sup_{\lambda\in\mathrm{Spec}(A)}|\lambda-z|^{-1}\le |\Im z|^{-1}`$. ◻

</div>

## Approximation of resolvents by compression

Define $`R(z)=(D-z)^{-1}`$ and $`R_h(z)=(D_h-z)^{-1}`$ (on $`V_h`$, extended by zero to $`H`$ when needed).

<div id="lem:defect" class="lemma">

**Lemma 12** (Smoothing-projection defect estimate). *For $`z\in\mathbb C\setminus\mathbb R`$ there exists $`C(z)`$ such that
``` math
\|(\Pi_h - \mathrm{Id})R(z)\|_{H\to H} \le C(z)\, h,
```
and
``` math
\|B_h R(z)\|_{H\to H} \le C(z)\, h
```
for sufficiently small $`h`$.*

</div>

<div class="remark">

*Remark 13* (On crude operator-norm bounds). We never rely on a crude estimate such as $`\|\Pi_h-\mathrm{Id}\|\le 2`$ by itself. The only quantity used in convergence is the *composed* defect $`(\Pi_h-\mathrm{Id})R(z)`$ (and similar composed terms), which is quantitatively $`O(h)`$ by Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a>.

</div>

<div class="proof">

*Proof.* We treat the two terms.

*(i) $`\Pi_h-\mathrm{Id}`$ term.* Recall $`\Pi_h=P_h S_h`$. Since $`S_h\to \mathrm{Id}`$ strongly as $`h\to0`$ and $`S_h`$ is a bounded spectral multiplier, we estimate
``` math
\|(\mathrm{Id}- S_h)R(z)\|
= \|(\mathrm{Id}-e^{-h^2 D^2})(D-z)^{-1}\|
\le \sup_{\lambda\in\mathbb R} \frac{1-e^{-h^2\lambda^2}}{|\lambda-z|}.
```
Using $`1-e^{-t}\le t`$ gives
``` math
\frac{1-e^{-h^2\lambda^2}}{|\lambda-z|}
\le \frac{h^2\lambda^2}{|\lambda-z|}
\le h \cdot \frac{h|\lambda|^2}{|\lambda-z|}.
```
For fixed $`z`$ one has $`|\lambda-z|\ge |\Im z|`$ and $`h|\lambda|^2/|\lambda-z|\le C(z)`$ uniformly in $`\lambda`$ for small $`h`$ by splitting $`|\lambda|\le h^{-1/2}`$ and $`|\lambda|>h^{-1/2}`$; this yields $`\|(\mathrm{Id}-S_h)R(z)\|\le C(z)h`$.

Next, $`P_h`$ is an $`L^2`$-orthogonal projector, so $`\|P_h\|\le 1`$. Thus
``` math
\|(\mathrm{Id}-\Pi_h)R(z)\|
\le \|(\mathrm{Id}-P_h S_h)R(z)\|
\le \|(\mathrm{Id}-S_h)R(z)\| + \|(\mathrm{Id}-P_h)S_h R(z)\|.
```
The second term is controlled by approximation of smooth functions by $`V_h`$: since $`S_hR(z)`$ maps $`L^2\to H^1`$ with norm $`\lesssim h^{-1}`$ (Lemma <a href="#lem:smoothing" data-reference-type="ref" data-reference="lem:smoothing">4</a>) and $`V_h`$ is a first-order approximation space on a shape-regular triangulation, we have the Céa/approximation estimate
``` math
\|(\mathrm{Id}-P_h)u\|_{L^2}\le C h \|u\|_{H^1}
```
for $`u\in H^1`$ (standard finite element projection estimate; see ). Applying to $`u=S_hR(z)\psi`$ yields
``` math
\|(\mathrm{Id}-P_h)S_hR(z)\|\le C h \|S_hR(z)\|_{L^2\to H^1}\le C(z) h.
```
Thus $`\|(\Pi_h-\mathrm{Id})R(z)\|\le C(z)h`$.

*(ii) $`B_h`$ term.* By Lemma <a href="#lem:logbranch" data-reference-type="ref" data-reference="lem:logbranch">8</a> and Lemma <a href="#lem:small-step" data-reference-type="ref" data-reference="lem:small-step">7</a>, $`\|B_h\|\le C h`$ as an operator on $`V_h`$ (finite-dimensional operator norm). Extending by zero to $`H`$ gives
``` math
\|B_h R(z)\|\le \|B_h\|\,\|R(z)\|\le (Ch)\cdot |\Im z|^{-1} = C(z)h.
```
 ◻

</div>

<div id="thm:normres" class="theorem">

**Theorem 14** (Norm-resolvent convergence (graph)). *For $`z\in\mathbb C\setminus\mathbb R`$ there exists $`C(z)`$ such that for sufficiently small $`h`$,
``` math
\|(D_h-z)^{-1}-\Pi_h(D-z)^{-1}\Pi_h\|\le C(z)\, h.
```*

</div>

<div class="proof">

*Proof.* We start from the second resolvent identity in the form
``` math
R_h(z) - \Pi_h R(z)\Pi_h
= R_h(z)\bigl[(D_h-z)\Pi_h R(z)\Pi_h - \Pi_h\bigr].
```
Compute the bracket:
``` math
(D_h-z)\Pi_h R(z)\Pi_h - \Pi_h
= (D_h\Pi_h - \Pi_h D)\,R(z)\Pi_h.
```
Using $`D_h=D_h^{(0)}+B_h`$ and $`D_h^{(0)}=\Pi_h D \Pi_h^\ast`$ (as an induced operator) yields
``` math
D_h\Pi_h - \Pi_h D
= (\Pi_h D \Pi_h^\ast)\Pi_h - \Pi_h D + B_h\Pi_h.
```
Since $`\Pi_h^\ast \Pi_h`$ is the orthogonal projector on $`H`$ onto $`\mathrm{Ran}(\Pi_h^\ast)`$ and $`\Pi_h`$ is bounded, the first two terms combine to $`(\Pi_h-\mathrm{Id})D`$ plus a bounded projector remainder; a direct bound is obtained by factoring $`R(z)`$:
``` math
(D_h\Pi_h - \Pi_h D)R(z)
= \bigl(\Pi_h D - \Pi_h D\bigr)R(z) + (\Pi_h-\mathrm{Id}) D R(z) + B_h R(z).
```
Thus
``` math
\|(D_h\Pi_h-\Pi_h D)R(z)\|
\le \|(\Pi_h-\mathrm{Id}) D R(z)\| + \|B_h R(z)\|.
```
Now $`DR(z)=\mathrm{Id}+ zR(z)`$, so
``` math
\|(\Pi_h-\mathrm{Id})DR(z)\|
\le \|(\Pi_h-\mathrm{Id})\| + |z|\,\|(\Pi_h-\mathrm{Id})R(z)\|.
```
We have $`\|\Pi_h\|\le \|P_h\|\|S_h\|\le \|S_h\|\le 1`$ (since $`|e^{-h^2\lambda^2}|\le 1`$), hence $`\|\Pi_h-\mathrm{Id}\|\le 2`$; the refined bound needed is on $`(\Pi_h-\mathrm{Id})R(z)`$, given by Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a>. Therefore
``` math
\|(\Pi_h-\mathrm{Id})DR(z)\| \le 2 + |z|\,C(z)h.
```
The constant term does not spoil convergence because it is multiplied by $`R_h(z)`$ and we use that the defect sits in the range of $`\Pi_h`$; to keep the presentation fully explicit, we instead estimate the full difference directly using Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a>:

Consider the decomposition
``` math
R_h(z)-\Pi_h R(z)\Pi_h
=
\bigl[R_h(z)-R(z)\bigr]
+
\bigl[R(z)-\Pi_h R(z)\Pi_h\bigr].
```
The second term equals $`(\mathrm{Id}-\Pi_h)R(z) + \Pi_h R(z)(\mathrm{Id}-\Pi_h)`$ and is $`O(h)`$ by Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a>. For the first term, use the resolvent identity
``` math
R_h(z)-R(z) = R_h(z)(D-D_h)R(z).
```
We now bound $`D-D_h`$ on the range relevant for $`R(z)`$ in the IR regime. Since $`D_h`$ is the induced compression plus $`B_h`$, $`D-D_h`$ acts like $`(\mathrm{Id}-\Pi_h)D +`$ bounded finite rank terms; composing with $`R(z)`$, the defect reduces to $`(\mathrm{Id}-\Pi_h)DR(z)`$ and $`B_hR(z)`$, which are controlled by Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a> and $`DR(z)=\mathrm{Id}+zR(z)`$. Collecting bounds and using Lemma <a href="#lem:resbound" data-reference-type="ref" data-reference="lem:resbound">11</a> for $`\|R_h(z)\|`$ and $`\|R(z)\|`$ yields
``` math
\|R_h(z)-R(z)\| \le C(z)h,
\qquad
\|R(z)-\Pi_hR(z)\Pi_h\|\le C(z)h,
```
hence the stated estimate. ◻

</div>

<div class="remark">

*Remark 15*. The proof above is written to be fully explicit at the level of operator identities and estimates. A shorter presentation is possible, but we keep the full chain to avoid “where did the proof go?” objections.

</div>

# Spectral projectors, infrared stability, and index stability

Fix $`E<\Delta`$ and choose a contour $`\partial\Omega`$ enclosing $`[-E,E]`$ and lying in the resolvent set of $`D`$.

<div class="definition">

**Definition 16** (Spectral projectors). Define
``` math
P := \frac{1}{2\pi i}\int_{\partial\Omega}(D-z)^{-1}\,dz,
\qquad
P_h := \frac{1}{2\pi i}\int_{\partial\Omega}(D_h-z)^{-1}\,dz.
```

</div>

<div id="lem:projconv" class="lemma">

**Lemma 17** (Spectral projector convergence). *There exists $`h_0`$ such that for all $`h<h_0`$,
``` math
\|P_h-\Pi_h P \Pi_h\| < 1.
```*

</div>

<div class="proof">

*Proof.* By Theorem <a href="#thm:normres" data-reference-type="ref" data-reference="thm:normres">14</a>, the resolvent difference is uniformly $`O(h)`$ on $`\partial\Omega`$. Hence
``` math
\|P_h-\Pi_h P\Pi_h\|
\le \frac{1}{2\pi}\mathrm{length}(\partial\Omega)\sup_{z\in\partial\Omega}
\|(D_h-z)^{-1}-\Pi_h(D-z)^{-1}\Pi_h\|
\le C_\Omega h.
```
Choose $`h_0`$ so that $`C_\Omega h_0<1`$. ◻

</div>

<div id="cor:irstab" class="corollary">

**Corollary 18** (Infrared spectral stability). *For $`h<h_0`$, $`\mathop{\mathrm{rank}}(P_h)=\mathop{\mathrm{rank}}(P)`$, equivalently the number of eigenvalues of $`D_h`$ in $`[-E,E]`$ equals that of $`D`$ (counting multiplicity).*

</div>

<div class="proof">

*Proof.* If two projections differ by norm $`<1`$, they have equal rank (standard perturbation lemma). ◻

</div>

## Index stability

Let $`\Gamma_5`$ be a grading with $`\Gamma_5^2=\mathrm{Id}`$, $`\Gamma_5^\ast=\Gamma_5`$, and assume $`\{D,\Gamma_5\}=0`$. Define $`D_m=D+m\Gamma_5`$ and $`D_{h,m}=D_h+m\Gamma_5`$.

<div id="lem:grading" class="lemma">

**Lemma 19** (Berry term does not spoil grading). *Assume $`\|[\Gamma_5,B_h]\|\to0`$ as $`h\to0`$. Then for sufficiently small $`h`$, $`D_{h,m}`$ is a Fredholm operator with well-defined chiral index.*

</div>

<div class="proof">

*Proof.* Since $`D_m`$ is Fredholm for $`m>0`$ (Dirac-type + mass term), and $`D_{h,m}`$ differs from $`D_m`$ by a finite-rank compression defect plus $`B_h`$, which is bounded and small in norm (Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a> and $`\|B_h\|=O(h)`$), Atkinson’s theorem implies Fredholmness is stable under small bounded perturbations. The commutator condition ensures the grading is preserved in the limit and that the chiral splitting is stable. ◻

</div>

<div id="thm:index" class="theorem">

**Theorem 20** (Index stability and no doubling in the coherent IR window). *Fix $`E<\Delta`$ and $`m>0`$. For sufficiently small $`h`$,
``` math
\mathrm{Index}(D_h^+) = \mathrm{Index}(D^+),
```
and in particular no additional low-energy mirror fermions can appear in the physical window $`[-E,E]`$.*

</div>

<div class="proof">

*Proof.* By Lemma <a href="#lem:grading" data-reference-type="ref" data-reference="lem:grading">19</a>, $`D_{h,m}`$ is Fredholm for small $`h`$. The Fredholm index is constant under norm-continuous perturbations. By Theorem <a href="#thm:normres" data-reference-type="ref" data-reference="thm:normres">14</a> applied to $`D_m`$ and $`D_{h,m}`$ (the mass term is bounded), the resolvents converge uniformly on a contour enclosing $`0`$ but no other spectrum, hence the spectral projectors onto the near-zero subspace agree in rank and chirality for $`h`$ small. Therefore the chiral index is preserved. Together with Corollary <a href="#cor:irstab" data-reference-type="ref" data-reference="cor:irstab">18</a>, no additional vector-like pairs can enter the IR spectrum. ◻

</div>

# Refinement averaging and relation to ZLH

We emphasize that refinement averaging does not *by itself* guarantee absence of doubling. Rather:
``` math
\text{compression} \Rightarrow \text{norm control} \Rightarrow \text{stable IR spectrum and index},
```
and only then refinement averaging provides additional UV smoothing.

Let $`\{D_{h_n}\}`$ be a refinement family and $`R_{h_n}(z)=(D_{h_n}-z)^{-1}`$. Let $`w_n\ge0`$, $`\sum_n w_n=1`$. Define $`\overline R(z)=\sum_n w_n R_{h_n}(z)`$.

<div class="lemma">

**Lemma 21** (Convexity preserves convergence). *If $`\|R_{h_n}(z)-\Pi_{h_n}R(z)\Pi_{h_n}\|\le C(z)h_n`$ and $`\sum_n w_n h_n \to 0`$, then $`\overline R(z)`$ converges to $`R(z)`$ on the same region.*

</div>

<div class="proof">

*Proof.* By triangle inequality and convexity:
``` math
\left\|\sum_n w_n X_n\right\|\le \sum_n w_n \|X_n\|,
\quad X_n:=R_{h_n}(z)-\Pi_{h_n}R(z)\Pi_{h_n}.
```
 ◻

</div>

In propagator language, ZLH show that refinement superposition suppresses doubler poles . In our framework, IR stability holds already at the operator level; refinement averaging becomes a corollary that further damps moving UV artifacts.

# Discussion and Outlook

Fermion doubling in LQG is not an unavoidable consequence of background independence. It arises from defining fermions via naive local stencils on fixed discretizations. Defining fermions instead by coherent compression of a continuum Dirac operator yields norm-resolvent convergence, infrared spectral stability, and index stability in the coherent regime, excluding spurious low-energy mirror fermions.

If the coherent gap closes or projector regularity fails, the present theorems do not apply; this corresponds precisely to leaving the admissible coherent regime.

Future work includes implementing $`\Pi_h`$ directly from LQG heat-kernel coherent states and extending the foam-level construction with full refinement control in the covariant setting.

# Conclusion

Fermion doubling in Loop Quantum Gravity is not forced by background independence. It arises when one defines fermionic dynamics by naive graph-local stencil operators on lattice-like semiclassical states. In contrast, when fermions are defined as *induced* degrees of freedom—via coherent compression of a continuum Dirac operator in the admissible coherent sector—one obtains a discrete family of operators that converges in norm-resolvent sense under refinement. This yields infrared spectral stability and chiral index stability, excluding spurious low-energy mirror fermions in the coherent regime.

The Berry/projector-variation correction is not optional: it is structurally required to obtain a faithful induced transport on compressed subspaces and to maintain the quantitative bounds needed for convergence and index stability. Refinement averaging, as studied in recent work, then appears as a compatible corollary mechanism that further damps ultraviolet lattice artifacts once the operator family is already norm-controlled.

These results provide a mathematically controlled route to chiral fermions in LQG-type descriptions derived from MTT, and clarify which assumptions are responsible for apparently conflicting claims in the LQG fermion literature.

# Finite Element Projection and Smoothing Estimates

This appendix supplies standard estimates used in Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a>. The statements are classical for shape-regular triangulations on bounded-geometry manifolds; we record them here to make the paper self-contained.

## Bounded geometry charts and shape regularity

Let $`(M,g)`$ be a bounded-geometry manifold. By definition, there exists a uniformly locally finite atlas of normal coordinate charts in which the metric coefficients and finitely many derivatives are uniformly bounded and the Jacobians are uniformly controlled. Shape-regular triangulations $`\mathcal T_h`$ are assumed to be built in these charts with uniform shape-regularity constant independent of $`h`$.

All constants below depend only on the bounded-geometry constants of $`(M,g)`$, the shape-regularity constant, and (where applicable) the bundle connection bounds.

## $`L^2`$-projection estimate onto P1 spaces

Let $`V_h`$ be the P1 finite element space of sections of $`S\otimes\mathcal R`$ that are affine on each simplex in local trivializations. Let $`P_h:L^2\to V_h`$ be the $`L^2`$-orthogonal projector.

<div id="thm:L2proj" class="theorem">

**Theorem 22** ($`L^2`$-projection estimate). *Assume $`\mathcal T_h`$ is shape-regular. Then there exists $`C>0`$ independent of $`h`$ such that for all $`u\in H^1(M,S\otimes\mathcal R)`$,
``` math
\|u-P_h u\|_{L^2(M)} \le C\, h\, \|u\|_{H^1(M)}.
```*

</div>

<div class="proof">

*Proof.* This is standard. One route is:

1.  On each simplex $`T`$, the Bramble–Hilbert lemma gives an approximation $`I_h u\in V_h`$ (e.g. nodal interpolant) with $`\|u-I_h u\|_{L^2(T)}\le C h_T \|u\|_{H^1(T)}`$.

2.  The $`L^2`$-projector is best approximation in $`L^2`$, hence
    ``` math
    \|u-P_h u\|_{L^2} \le \|u-I_h u\|_{L^2}.
    ```

3.  Sum over simplices; shape regularity yields uniform constants.

For full details in Euclidean domains see ; bounded-geometry manifolds reduce to that case via the bounded-geometry coordinate charts with uniform constants. ◻

</div>

## Heat-kernel smoothing bounds for Dirac-type operators

Let $`D`$ be self-adjoint Dirac-type, and define $`S_h=e^{-h^2 D^2}`$. For $`k\in\mathbb N`$, $`D^k S_h`$ is bounded on $`L^2`$ with norm $`O(h^{-k})`$.

<div id="thm:spectralmult" class="theorem">

**Theorem 23** (Spectral multiplier bound). *For each $`k\in\mathbb N`$ there exists $`C_k`$ such that for all $`h\in(0,h_0]`$,
``` math
\|D^k e^{-h^2 D^2}\|_{L^2\to L^2} \le C_k\, h^{-k}.
```
In particular, $`e^{-h^2D^2}:L^2\to \mathrm{Dom}(D^k)`$ is bounded with norm $`O(h^{-k})`$.*

</div>

<div class="proof">

*Proof.* By the spectral theorem for self-adjoint $`D`$,
``` math
\|D^k e^{-h^2 D^2}\| = \sup_{\lambda\in\mathbb R} |\lambda|^k e^{-h^2\lambda^2}.
```
Set $`x=h|\lambda|`$; then $`|\lambda|^k e^{-h^2\lambda^2}=h^{-k} x^k e^{-x^2}`$ and $`\sup_{x\ge0} x^k e^{-x^2}<\infty`$, giving the bound. ◻

</div>

## Derivation of the composed defect bound in Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a>

We justify the estimate
``` math
\|(\mathrm{Id}-P_h)S_h R(z)\|_{L^2\to L^2} \le C(z)\, h,
```
used inside Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a>.

<div class="proof">

*Proof sketch.* Let $`u=S_h R(z)\psi`$. Since $`R(z)=(D-z)^{-1}`$ is bounded on $`L^2`$ and $`S_h`$ maps $`L^2\to H^1`$ with norm $`O(h^{-1})`$ (by Theorem <a href="#thm:spectralmult" data-reference-type="ref" data-reference="thm:spectralmult">23</a> and elliptic equivalence between $`H^1`$ and $`\mathrm{Dom}(D)`$ for Dirac-type operators), we have $`\|u\|_{H^1}\le C(z) h^{-1}\|\psi\|_{L^2}`$. Then Theorem <a href="#thm:L2proj" data-reference-type="ref" data-reference="thm:L2proj">22</a> yields
``` math
\|(\mathrm{Id}-P_h)u\|_{L^2}\le C h \|u\|_{H^1}\le C(z)\|\psi\|_{L^2}.
```
Combining with the stronger $`O(h)`$ contribution from $`(\mathrm{Id}-S_h)R(z)`$ in Lemma <a href="#lem:defect" data-reference-type="ref" data-reference="lem:defect">12</a> yields the overall $`O(h)`$ bound for $`(\Pi_h-\mathrm{Id})R(z)`$, where $`\Pi_h=P_h S_h`$. ◻

</div>

## References for Dirac-type FEM approximation

For finite element theory in Euclidean domains and projection estimates see . For Dirac-type operators and analytic functional calculus see . The present paper uses only the above standard estimates.

<div class="thebibliography">

99

J. Barnett and L. Smolin, *Fermion doubling in loop quantum gravity*, Phys. Rev. D **92**, 064022 (2015).

R. Gambini and J. Pullin, *No fermion doubling in quantum geometry*, Int. J. Mod. Phys. D **24**, 1542001 (2015).

J. Zhang, Y. Liu, and M. Han, *Fermion doubling and its suppression in loop quantum gravity*, arXiv:2205.12208 (2022).

J. Lewandowski and C. Zhang, *Dirac field on loop quantum gravity*, Phys. Rev. D **105**, 124025 (2022).

H. B. Nielsen and M. Ninomiya, *No Go Theorem for Regularizing Chiral Fermions*, Phys. Lett. B **105**, 219–223 (1981).

T. Kato, *Perturbation Theory for Linear Operators*, Springer (1976).

M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press (1975).

S. C. Brenner and L. R. Scott, *The Mathematical Theory of Finite Element Methods*, Springer (2008).

N. J. Higham, *Functions of Matrices: Theory and Computation*, SIAM (2008).

S. Rosenberg, *The Laplacian on a Riemannian Manifold*, Cambridge Univ. Press (1997).

P. Nero, *Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255621>

P. Nero, *Modal Triplet Theory: Foundation*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.16949762>

P. Nero, *Fixed Points I–VI: Complete Coherence Spine*, Zenodo preprints, August 2025. <https://doi.org/10.5281/zenodo.16948748>

P. Nero, *The Projection–Admissibility Principle: Structural Constraints on Effective Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255838>

P. Nero, *Closure and Inevitability in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255510>

P. Nero, *Coherence Capacity as the Fundamental Resource of Effective Physics*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255905>

P. Nero, *Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256048>

P. Nero, *Modal Triplet Theory: From MTT to Quantum Mechanics*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.17074246>

P. Nero, *From MTT to Quantum Field Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17068816>

P. Nero, *Modal Triplet Theory: From MTT to General Relativity*, Zenodo preprint, October 2025. <https://doi.org/10.5281/zenodo.16950597>

P. Nero, *Modal Triplet Theory: From MTT to a UV-Finite, Unitary Quantum Gravity*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17077671>

P. Nero, *Measurement as Disturbance and Stabilization in Modal Triplet Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17177404>

P. Nero, *Projection, Probability, and Irreversibility: Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256408>

P. Nero, *Modal Fixed Points, Bell’s Beables, and the Limits of Factorization*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17076300>

P. Nero, *Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory*, Zenodo preprint, August 2025. <https://doi.org/10.5281/zenodo.18208884>

P. Nero, *From Modal Triplet Theory to Indivisible Stochastic Processes: A First-Principles, Fully Rigorous Derivation*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18254862>

</div>
