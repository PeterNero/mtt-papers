---
abstract: |
  Modal Triplet Theory repeatedly uses fixed points, positive Hessians, heat kernels, coherent projectors, and perturbative graphs. These objects have often appeared as neighboring constructions without one theorem stating their exact common source. This paper supplies that theorem at the structural tier. Begin with a nonlinear defect section $`\Phi`$ on a metric configuration space and the positive repair cost $`\mathcal{C}=\frac12\left\lVert \Phi \right\rVert^{2}`$. Its negative gradient is closure repair. At a zero-defect fixed point the Hessian is exactly the normal operator $`D\Phi^{\dagger}D\Phi`$; its heat semigroup, Green operator, spectral projectors, local kernel, and complete finite repair-vertex jet are then different mathematical shadows of the same linearized source. At a nonzero-defect critical point an additional covariant residual term is present, so the normal-square formula cannot be used without qualification.

  The construction is extended to local Cech descent and to an $`\alpha`$-twisted cohesive module. The projective twist cancels in the endomorphism algebra, the Maurer–Cartan curvature $`F(a)=da+a^{2}`$ gives a canonical nonlinear repair residual, and a chosen Hermitian structure yields the Hodge operator and tangent heat flow. An exact stratified example shows simultaneously that the full cohesive operator may remain regular while every uniform fiberwise Green operator diverges across a cohomology-rank jump. Compatible isometric intertwiners transport the repair flow, functional calculus, projectors, kernels, and formal graph coefficients.

  The paper also proves the necessary boundary. A positive repair square is not a signed physical action. It loses first-order sign, phase, Morse index, causal support, and generally the physical interaction vertices. A direct action requires a variational anchor satisfying Helmholtz conditions; a universal multiplier lift always exists; and a cyclic Maurer–Cartan source admits a Chern–Simons-type signed action. For the q79 program, the cohesive Hartshorne–Serre benchmark closes the structural chain exactly after a Hermitian choice. Selection of the physical $`V_3/W_9`$ endpoint, its HYM metric, full Hull–Strominger action, Lorentzian domains, and the continuum-to-finite intertwiner remain open. Thus closure repair explains why the operator and kernel language should recur, without promoting that recurrence into a completed theory of dynamics or quantization.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: September 2026, Version 3
generated_from_main_tex_sha256: 8f4e04974e471ae5e731b898f96c0286a779a78c6f61c6cfcd31f497726a46d7
paper_id: cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows
release_state: current_revised_tex
title: |
  **Cohesive Closure Repair and Its Hodge, Kernel, and Projection Shadows:**
  From Nonlinear Defects to Tangent Semigroups, with the Physical-Action Boundary
---

# Version 3 Revision Note

Supersedes
The local Version 2 manuscript; no new public release is implied.

Reason
The physical residual had only a schematic description, and the projection statement did not distinguish a unitary equivalence from an isometric embedding with transverse coupling.

Resolution
Displays the six additional residuals, their derivatives and the corrected 25-block rank-102 support. States the extra adjoint condition for embedded Hessian transport, explains transported metrics, and organizes the physical endpoint contract into three structured source types.

Retained result
The residual-Hessian, cohesive, descent, repair-jet and action-boundary theorems remain at their stated tiers. Previously established local and finite results are not reopened.

Remaining boundary
A structural support mask is not a numerical matrix; symmetry reduction requires endpoint equivariance. Physical source selection, the common analytic domain and the four-dimensional action remain distinct.

# Version 2 Revision Note

Supersedes
Version 1. The previous release remains public until a new release is approved.

Reason
Connect strict-gradient repair to the finite-mode recurrence obstruction.

Resolution
Connects strict repair with the stationary-ensemble and finite-mode recurrence obstructions.

Retained result
Correctly scoped results and explanatory examples remain; no physical source-selection claim is promoted.

Remaining boundary
Realization hypotheses and physical source or apparatus bridges remain separate obligations. This is an unreleased authoring revision.

# Version 1 revision note

#### Supersedes.

No earlier paper. Version 1 establishes the baseline for this new theorem-owner paper.

#### Reason.

The Fixed Points, wave–particle, and diagrammatics papers each use a downstream part of the same mathematical chain, but none is the proper owner of the upstream derivation from nonlinear closure repair.

#### Resolution.

Version 1 proves and explains the structural chain
``` math
\begin{gathered}
\text{nonlinear closure defect}
\longrightarrow
\text{repair flow}
\longrightarrow
\text{linearized Hodge operator},\\
\text{linearized Hodge operator}
\longrightarrow
\text{kernel and projection shadows}.
\end{gathered}
```
It consolidates separately certified theorem packets, proves their composition in standalone form, includes the nonzero-defect correction, and separates the positive repair functional from a signed physical action.

#### Retained result.

The exact component theorems and their executable witnesses are retained at their established tiers. Their ownership is reorganized rather than weakened: this paper owns the composition, while the downstream papers retain their fixed-point, wave–particle, and graph theorems.

#### Remaining boundary.

No observed mass, coupling, mixing angle, cosmological datum, or fitted coefficient enters the theorems. The paper does not prove a Lorentzian action, interacting QFT, ultraviolet-complete quantum gravity, unique actualization, or selection of the physical q79 endpoint. The q79 cohesive application remains an exact structural benchmark rather than a physical promotion.

# The question before the operator

Many physical formalisms begin with an operator. One specifies a Hamiltonian, a Laplacian, a Dirac operator, a Hessian, or a propagator and then asks what it does. MTT begins one question earlier:

> What is being repaired, and why should its first observable shadow be an operator at all?

The answer developed here is deliberately modest. Suppose a state is admissible when a nonlinear defect vanishes. The squared size of the defect is then a natural nonnegative cost. Its gradient points in the direction in which inadmissibility grows most rapidly; its negative gradient therefore defines a repair flow. Linearizing that flow at an exact admissible state produces a positive normal operator. Once that operator exists, the heat semigroup, Green operator, spectral projectors, and local kernels belong to ordinary functional analysis.

This does not make every physical operator a theorem of MTT. It identifies one precise mechanism by which a large and important class of operators can arise. The mechanism has hypotheses, and several of them carry physical content: the configuration space, defect bundle, metric, connection, domain, background, and interpretation must all be selected. Hiding any one of these choices inside the word “closure” would merely relocate the input.

The central distinction of this paper is therefore:

> **The repair operator is derived from a selected defect and metric. The selected defect and metric are not derived by notation.**

## How to read the paper

Readers interested in the universal differential geometry may read <a href="#sec:residual-hessian,sec:dynamics" data-reference-type="ref+label" data-reference="sec:residual-hessian,sec:dynamics">[sec:residual-hessian,sec:dynamics]</a>. The cohesive and q79 construction is in <a href="#sec:cohesive,sec:q79" data-reference-type="ref+label" data-reference="sec:cohesive,sec:q79">[sec:cohesive,sec:q79]</a>. The operator, kernel, and projection chain is proved in <a href="#sec:hodge,sec:descent-projection" data-reference-type="ref+label" data-reference="sec:hodge,sec:descent-projection">[sec:hodge,sec:descent-projection]</a>. The relation to perturbative graphs is in <a href="#sec:graphs" data-reference-type="ref+label" data-reference="sec:graphs">7</a>. The crucial warning that repair is not automatically action appears in <a href="#sec:action-boundary" data-reference-type="ref+label" data-reference="sec:action-boundary">8</a>. The final status and theorem-ownership tables are in <a href="#sec:ownership,sec:frontier" data-reference-type="ref+label" data-reference="sec:ownership,sec:frontier">[sec:ownership,sec:frontier]</a>.

## Vocabulary of claim strength

We use four labels throughout.

1.  **Exact** means proved from the displayed assumptions.

2.  **Exact structural benchmark** means proved on the named q79 object, but not promoted to the selected physical endpoint.

3.  **Conditional transport** means the conclusion follows if the stated chain, metric, or transform intertwiner exists.

4.  **Open physical promotion** means that the required source object or comparison has not been constructed and certified.

These labels are part of the mathematics. They prevent a theorem about an available representation from being mistaken for a theorem selecting the representation realized in nature.

# Residual geometry and the repair Hessian

## The nonlinear source

Let $`(\mathcal{M},g)`$ be a finite-dimensional Riemannian manifold. The same formulas extend to a Hilbert manifold when the derivatives, adjoints, and domains used below exist. Let
``` math
(\mathcal{E},h,\nabla^{\mathcal{E}})\longrightarrow \mathcal{M}
```
be a real metric or complex Hermitian vector bundle with metric connection, and let
``` math
\Phi\in\Gamma(\mathcal{E})
```
be a twice differentiable defect section. In the complex case every scalar pairing below means its real part. Define
``` math
\begin{equation}
\mathcal{C}(p)=\frac12 h\bigl(\Phi(p),\Phi(p)\bigr).
\label{eq:repair-cost}
\end{equation}
```

At $`p\in\mathcal{M}`$, write
``` math
\begin{align}
r_p&=\Phi(p),\\
J_pX&=\nabla_X^{\mathcal{E}}\Phi,\\
B_p(X,Y)&=
\nabla_X^{\mathcal{E}}\nabla_Y^{\mathcal{E}}\Phi
-\nabla_{\nabla_X^{\mathcal{M}}Y}^{\mathcal{E}}\Phi.
\end{align}
```
The tensor $`B_p`$ is the covariant second derivative of the defect.

<div id="thm:residual-hessian" class="theorem">

**Theorem 1** (Covariant residual-Hessian identity). *For every $`X,Y\in T_p\mathcal{M}`$,
``` math
\begin{align}
\mathrm{d}\mathcal{C}_p(X)&=h(r_p,J_pX),
\label{eq:first-variation}\\
\mathop{\mathrm{Hess}}_p\mathcal{C}(X,Y)&=
h(J_pX,J_pY)+h(r_p,B_p(X,Y)).
\label{eq:full-hessian}
\end{align}
```
Equivalently,
``` math
\begin{equation}
\mathop{\mathrm{grad}}\mathcal{C}(p)=J_p^{\dagger}r_p,
\qquad
H_p=J_p^{\dagger}J_p+S_{r_p},
\label{eq:operator-hessian}
\end{equation}
```
where
``` math
g(S_{r_p}X,Y)=h(r_p,B_p(X,Y)).
```
The residual form is symmetric, including when $`\nabla^{\mathcal{E}}`$ has curvature.*

</div>

<div class="proof">

*Proof.* Metric compatibility gives
``` math
X[\mathcal{C}]=h(\nabla_X^{\mathcal{E}}\Phi,\Phi),
```
which proves <a href="#eq:first-variation" data-reference-type="eqref" data-reference="eq:first-variation">[eq:first-variation]</a>. Differentiate once more and subtract the Levi–Civita correction:
``` math
\begin{align*}
\mathop{\mathrm{Hess}}\mathcal{C}(X,Y)
&=X[\mathrm{d}\mathcal{C}(Y)]-\mathrm{d}\mathcal{C}(\nabla_X^{\mathcal{M}}Y)\\
&=h(\nabla_X^{\mathcal{E}}\Phi,\nabla_Y^{\mathcal{E}}\Phi)
+h\!\left(\Phi,
\nabla_X^{\mathcal{E}}\nabla_Y^{\mathcal{E}}\Phi
-\nabla_{\nabla_X^{\mathcal{M}}Y}^{\mathcal{E}}\Phi\right).
\end{align*}
```
This is <a href="#eq:full-hessian" data-reference-type="eqref" data-reference="eq:full-hessian">[eq:full-hessian]</a>. The antisymmetric part of $`B`$ is $`R^{\mathcal{E}}(X,Y)\Phi`$. Curvature of a metric or Hermitian connection is skew-adjoint, so $`\operatorname{Re}h(\Phi,R^{\mathcal{E}}(X,Y)\Phi)=0`$. The residual term is therefore symmetric. ◻

</div>

<div id="cor:zero-normal-square" class="corollary">

**Corollary 2** (Exact-zero normal square). *If $`p_*`$ is an exact closure state, $`\Phi(p_*)=0`$, then
``` math
\begin{equation}
\mathop{\mathrm{grad}}\mathcal{C}(p_*)=0,
\qquad
\mathop{\mathrm{Hess}}_{p_*}\mathcal{C}=J_*^{\dagger}J_*\geq0.
\label{eq:normal-square}
\end{equation}
```
Moreover,
``` math
\ker\mathop{\mathrm{Hess}}_{p_*}\mathcal{C}=\ker J_*.
```*

</div>

This is the exact source of the positive repair Hessian used later. It is also the point at which a common shortcut must stop. Equation <a href="#eq:normal-square" data-reference-type="eqref" data-reference="eq:normal-square">[eq:normal-square]</a> is not the general Hessian formula.

<div id="cor:nonzero-correction" class="corollary">

**Corollary 3** (Nonzero-defect correction). *A state $`p`$ is critical precisely when
``` math
J_p^{\dagger}r_p=0.
```
If $`r_p\neq0`$, the Hessian is
``` math
J_p^{\dagger}J_p+S_{r_p},
```
and the second term generally cannot be reconstructed from $`r_p`$ and $`J_p`$ alone. On $`\ker J_p`$, local stability is controlled entirely by $`S_{r_p}`$.*

</div>

<div id="ex:nonzero-witness" class="example">

**Example 4** (Why the correction cannot be dropped). Let $`\Phi_a:\mathbb{R}\to\mathbb{R}^2`$ be
``` math
\Phi_a(x)=(x,x^2+a),
\qquad a=1.
```
At $`x=0`$, the residual is $`(0,1)`$, the derivative is $`(1,0)`$, and $`J^{\dagger}r=0`$. Thus $`x=0`$ is critical although the defect is nonzero. The Gram term is $`J^{\dagger}J=1`$, the residual correction is $`2`$, and
``` math
\mathop{\mathrm{Hess}}_0\mathcal{C}=3.
```
Using only the normal square would give the wrong local stiffness by a factor of three.

</div>

## Symmetry and physical zero modes

Let a Lie group $`G`$ act isometrically on $`\mathcal{M}`$ and fiberwise isometrically on $`\mathcal{E}`$, and suppose $`\Phi`$ is equivariant.

<div id="prop:orbit-zero" class="proposition">

**Proposition 5** (Orbit zero modes). *If $`p`$ is critical and $`\xi_{\mathcal{M}}(p)`$ is tangent to its $`G`$-orbit, then
``` math
\mathop{\mathrm{Hess}}_p\mathcal{C}\bigl(\xi_{\mathcal{M}}(p),Y\bigr)=0
```
for every $`Y\in T_p\mathcal{M}`$.*

</div>

<div class="proof">

*Proof.* Invariance gives $`\mathrm{d}\mathcal{C}(\xi_{\mathcal{M}})=0`$ identically. Differentiate in the direction $`Y`$. The term containing $`\mathrm{d}\mathcal{C}(\nabla_Y\xi_{\mathcal{M}})`$ vanishes at a critical point, leaving the claimed Hessian identity. ◻

</div>

Consequently, positivity in a gauge or phase-symmetric system means positivity on a slice normal to the symmetry orbit. Requiring strict positivity on the unreduced space would incorrectly reject the zero modes that encode the symmetry.

# Repair as a flow

## Dissipative and reversible parts

Pure repair is the negative-gradient equation
``` math
\begin{equation}
\frac{\mathrm{d}u}{\mathrm{d}s}=-\mathop{\mathrm{grad}}\mathcal{C}(u).
\label{eq:gradient-repair}
\end{equation}
```
The parameter $`s`$ orders stabilization. It is not automatically Lorentzian time. A more general reversible–dissipative split is
``` math
\begin{equation}
\frac{\mathrm{d}u}{\mathrm{d}s}=(K-\Gamma)\mathop{\mathrm{grad}}\mathcal{C}(u),
\label{eq:reversible-dissipative}
\end{equation}
```
where $`K`$ is skew-adjoint and $`\Gamma`$ is self-adjoint and positive semidefinite.

<div id="thm:repair-flow" class="theorem">

**Theorem 6** (Repair monotonicity and tangent generator). *Along every solution of <a href="#eq:reversible-dissipative" data-reference-type="eqref" data-reference="eq:reversible-dissipative">[eq:reversible-dissipative]</a>,
``` math
\begin{equation}
\frac{\mathrm{d}}{\mathrm{d}s}\mathcal{C}(u(s))
=-g\bigl(\mathop{\mathrm{grad}}\mathcal{C},\Gamma\mathop{\mathrm{grad}}\mathcal{C}\bigr)\leq0.
\label{eq:energy-monotone}
\end{equation}
```
At a critical point $`p`$, the linearized generator is
``` math
\begin{equation}
D\bigl[(K-\Gamma)\mathop{\mathrm{grad}}\mathcal{C}\bigr]_p
=(K_p-\Gamma_p)H_p^{\sharp}.
\label{eq:linearized-general}
\end{equation}
```
At an exact-zero state and for pure repair, the tangent equation is
``` math
\begin{equation}
\partial_s v=-J_*^{\dagger}J_*v,
\qquad
v(s)=e^{-sJ_*^{\dagger}J_*}v(0).
\label{eq:tangent-heat}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Pair <a href="#eq:reversible-dissipative" data-reference-type="eqref" data-reference="eq:reversible-dissipative">[eq:reversible-dissipative]</a> with $`\mathop{\mathrm{grad}}\mathcal{C}`$. The $`K`$-term vanishes by skew-adjointness, and positivity of $`\Gamma`$ gives <a href="#eq:energy-monotone" data-reference-type="eqref" data-reference="eq:energy-monotone">[eq:energy-monotone]</a>. At a critical point the derivatives of $`K`$ and $`\Gamma`$ multiply $`\mathop{\mathrm{grad}}\mathcal{C}(p)=0`$, so only the Hessian term remains. The exact-zero specialization follows from <a href="#cor:zero-normal-square" data-reference-type="ref+label" data-reference="cor:zero-normal-square">2</a>. ◻

</div>

<div id="cor:circulation-no-go" class="corollary">

**Corollary 7** (Strict-dissipation circulation no-go). *If $`\Gamma`$ is positive definite along a periodic orbit of <a href="#eq:reversible-dissipative" data-reference-type="eqref" data-reference="eq:reversible-dissipative">[eq:reversible-dissipative]</a>, that orbit is constant. A persistent circulation therefore requires a null-dissipation sector, a conservative sector, a relative equilibrium generated by symmetry, or external driving.*

</div>

This small result matters conceptually. A particle-like phase circulation cannot be obtained merely by drawing a loop around a strictly dissipative minimum. Repair explains stabilization. Reversible phase transport requires additional selected structure.

This also separates repair from stationary noise. Fixed Points III owns the stationary-ensemble obstruction for strict Lyapunov repair: under its integrability and invariance hypotheses, a stationary ensemble has zero dissipation almost everywhere. A closed finite-spatial-mode unitary model with compact resolvent supplies a different obstruction, namely recurrence rather than irreversible mixing. Removing only an occupation-number cutoff does not remove that finite-spatial-mode recurrence.

Thus a stationary diffusion limit needs an independently justified recurrent fast driver and a mixing/scaling argument, a continuum or thermodynamic limit, or a declared open system. Toral-chaos examples remain valid examples of separately supplied drivers; they are not flows of a strictly decreasing repair cost. These distinctions preserve the repair Hessian theorem and locate the extra dynamical input precisely. The owning discussion and certificates are in Fixed Points III and the [curated reproduction repository](https://github.com/PeterNero/mtt-results-repro), under the finite-mode recurrence and fixed-point noise results; their proofs are not duplicated here.

## Fixed points and basins

The flow may possess many fixed points or many attraction basins. Their existence, uniqueness, regularity, and convergence require the familiar compactness, coercivity, analytic-semigroup, or Łojasiewicz–Simon hypotheses developed in Fixed Points I . The present paper does not duplicate those theorems. It supplies the upstream residual from which one eligible flow may be formed.

If a compact connected sector contains no zero of $`\Phi`$, the continuous cost $`\mathcal{C}`$ attains a positive minimum. Such a minimum is a mathematically precise persistent-defect candidate. It is not automatically a particle: its physical interpretation still depends on sector selection, stability modulo symmetry, reversible transport, and the map to observables.

# The cohesive source

## Why a complex rather than only a bundle

The q79 source program contains an $`\alpha`$-twisted Hartshorne–Serre object
``` math
\mathcal{S}_{\mathrm{HS}}\in D^b(J,\alpha)
```
with a bounded local perfect atlas. Its open-stratum contraction uses an inverse transverse coordinate and cannot pass through the exceptional stratum. Discarding the full complex would therefore erase precisely the place at which its cohomology rank changes.

Cohesive modules provide a lawful alternative. A bounded $`\alpha`$-twisted perfect atlas is represented by an $`\alpha`$-twisted graded smooth module $`E^\bullet`$ with an integrable antiholomorphic superconnection
``` math
\begin{equation}
\overline{\mathbb E}=\overline{\mathbb E}_0+\overline{\mathbb E}_1+\overline{\mathbb E}_2+\cdots,
\qquad
\overline{\mathbb E}^2=0.
\label{eq:cohesive-superconnection}
\end{equation}
```
This is standard cohesive and twisted-complex mathematics . The q79-specific statement is that the certified local atlas satisfies its hypotheses.

<div id="thm:end-untwist" class="theorem">

**Theorem 8** (Endomorphism untwisting). *Let the local projective transitions of $`E^\bullet`$ satisfy
``` math
G_{ij}G_{jk}G_{ki}=\alpha_{ijk}\mathrm{Id}.
```
Then $`\mathop{\mathrm{End}}(E^\bullet)`$ glues as an ordinary global graded algebra by conjugation. The commutator differential
``` math
\begin{equation}
d_{\mathop{\mathrm{End}}}(T)=[\overline{\mathbb E},T]
\label{eq:end-differential}
\end{equation}
```
satisfies $`d_{\mathop{\mathrm{End}}}^{2}=0`$.*

</div>

<div class="proof">

*Proof.* On a triple overlap,
``` math
\operatorname{ad}(G_{ij})\operatorname{ad}(G_{jk})\operatorname{ad}(G_{ki})
=\operatorname{ad}(\alpha_{ijk}\mathrm{Id})=\mathrm{Id}.
```
Thus the scalar gerbe cocycle disappears from the endomorphism transition. The graded Jacobi identity and $`\overline{\mathbb E}^2=0`$ give
``` math
d_{\mathop{\mathrm{End}}}^{2}(T)=[\overline{\mathbb E}^2,T]=0.
```
 ◻

</div>

The twist has not vanished from the object. It has become invisible to the adjoint algebra. This is exactly what is needed for a global deformation complex without falsely trivializing the original gerbe.

## The canonical nonlinear residual

Set
``` math
\mathcal{A}=\Omega^{0,*}(\mathop{\mathrm{End}}E),
\qquad d=[\overline{\mathbb E},-].
```
For a degree-one perturbation $`a\in\mathcal{A}^1`$, define
``` math
\begin{equation}
F(a)=da+a^2=(\overline{\mathbb E}+a)^2.
\label{eq:mc-residual}
\end{equation}
```
Then $`F(a)=0`$ precisely when the perturbed superconnection remains integrable. This is not an arbitrary polynomial chosen to resemble an interaction. It is the curvature of the perturbed cohesive source.

Choose a Hermitian structure and a gauge row. On degree one, let
``` math
\begin{equation}
\Phi_{\mathrm{MC}}(a)=\bigl(F(a),d_0^{\dagger}a\bigr),
\qquad
\mathcal{C}_{\mathrm{MC}}(a)=\frac12\left\lVert F(a) \right\rVert^2
+\frac12\left\lVert d_0^{\dagger}a \right\rVert^2.
\label{eq:mc-repair}
\end{equation}
```

<div id="thm:mc-repair" class="theorem">

**Theorem 9** (Cohesive Maurer–Cartan repair). *At the integrable background $`a=0`$,
``` math
\begin{equation}
D\Phi_{\mathrm{MC}}(0)=(d_1,d_0^{\dagger}),
\end{equation}
```
and
``` math
\begin{equation}
\mathop{\mathrm{Hess}}_0\mathcal{C}_{\mathrm{MC}}
=d_1^{\dagger}d_1+d_0d_0^{\dagger}
=\Delta_1.
\label{eq:mc-hodge}
\end{equation}
```
The tangent negative-gradient flow is
``` math
\partial_s a=-\Delta_1a,
\qquad
a(s)=e^{-s\Delta_1}a(0).
```
The nonlinear curvature also satisfies the Bianchi identity
``` math
d_aF(a)=0,
\qquad
d_a=d+[a,-].
```*

</div>

<div class="proof">

*Proof.* Differentiate <a href="#eq:mc-residual" data-reference-type="eqref" data-reference="eq:mc-residual">[eq:mc-residual]</a> at zero. The quadratic term has zero first derivative, so $`DF(0)=d_1`$. Apply <a href="#cor:zero-normal-square" data-reference-type="ref+label" data-reference="cor:zero-normal-square">2</a> to the two residual rows in <a href="#eq:mc-repair" data-reference-type="eqref" data-reference="eq:mc-repair">[eq:mc-repair]</a>. The Bianchi identity follows by expanding $`dF+[a,F]`$, using $`d^2=0`$ and the graded Leibniz rule. ◻

</div>

The algebraic residual is canonical once the cohesive object is fixed. The Hermitian metric, adjoint, normalization, and physical moment-map rows are not. In particular, $`d_0^{\dagger}a=0`$ is a gauge slice and must not be renamed the physical HYM equation.

# Hodge, Green, and kernel shadows

## The total-space Hodge package

Choose a smooth Hermitian metric on $`E^\bullet`$, a Hermitian metric on the compact boundaryless base $`J`$, and the associated density. Define
``` math
\begin{equation}
B_E=\overline{\mathbb E}+\overline{\mathbb E}^{\dagger},
\qquad
\Delta_E=B_E^2.
\label{eq:super-hodge}
\end{equation}
```
Its principal symbol is the Dolbeault symbol. Standard elliptic theory then gives a self-adjoint closure with compact resolvent .

<div id="thm:hodge-kernel" class="theorem">

**Theorem 10** (Hodge and kernel package). *Under the preceding compactness, ellipticity, metric, and domain hypotheses, there exist:*

1.  *a finite-dimensional harmonic space $`\ker\Delta_E`$ and orthogonal projector $`P_0`$;*

2.  *a smoothing heat semigroup $`e^{-s\Delta_E}`$ for $`s>0`$;*

3.  *a reduced Green operator
    ``` math
    \begin{equation}
    G_E=(\Delta_E|_{\ker\Delta_E^{\perp}})^{-1}(I-P_0)
    =\int_0^\infty\bigl(e^{-s\Delta_E}-P_0\bigr)\,\mathrm{d}s;
    \label{eq:green-heat}
    \end{equation}
    ```*

4.  *finite-rank spectral projectors $`\chi_I(\Delta_E)`$ for bounded spectral intervals $`I`$; and*

5.  *local Schwartz kernels for the smoothing functional calculus.*

*Every item is determined by the same selected $`\Delta_E`$.*

</div>

The word “shadow” is literal but not mystical. The spectral resolution is the wave-like normal-mode description. The local kernel
``` math
K_s(x,y)=\langle x|e^{-s\Delta_E}|y\rangle
```
is the localized propagation-of-repair description. They are two representations of one operator. Neither representation, by itself, makes the semigroup a physical quantum evolution.

## The wave–particle operator obtains a source candidate

The conditional wave–particle paper begins with a supplied positive operator $`A`$ and forms
``` math
B_{\mathrm{adm}}
=P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P
\cite{MTTWaveParticle2026}.
```
At the present structural tier, <a href="#thm:mc-repair,thm:hodge-kernel" data-reference-type="ref+label" data-reference="thm:mc-repair,thm:hodge-kernel">[thm:mc-repair,thm:hodge-kernel]</a> provide the exact candidate
``` math
\begin{equation}
A=\Delta_1=D\Phi_{\mathrm{MC}}(0)^{\dagger}D\Phi_{\mathrm{MC}}(0)
\label{eq:wave-source-candidate}
\end{equation}
```
on the cohesive benchmark. This closes the formerly missing mathematical arrow from nonlinear repair to the positive filtered operator on that benchmark.

It does not close the physical common-source theorem of the wave–particle paper. That stronger theorem must show that the state, Hamiltonian or generator, effects, instrument, damping channel, and selected MTT source all belong to one physical construction. Equation <a href="#eq:wave-source-candidate" data-reference-type="eqref" data-reference="eq:wave-source-candidate">[eq:wave-source-candidate]</a> supplies the positive repair operator, not the rest of quantum mechanics.

## A stratified warning

The existence of a regular total-space operator does not imply a uniform family of fiberwise inverses. The following exact example is the useful model.

<div id="prop:stratified-green" class="proposition">

**Proposition 11** (Regular complex, divergent fiberwise Green operator). *Let
``` math
d_r=\begin{bmatrix}
\operatorname{diag}(1,0,0)&rI_3
\end{bmatrix}:\mathbb{C}^6\longrightarrow\mathbb{C}^3
```
and let
``` math
B_r=\begin{bmatrix}0&d_r^{\dagger}\\d_r&0\end{bmatrix},
\qquad
\Delta_r=B_r^2.
```
The entries of $`B_r`$ and $`\Delta_r`$ are polynomial in $`r`$ and remain finite at $`r=0`$. For $`r\neq0`$,
``` math
\mathop{\mathrm{spec}}(\Delta_r)=
\{0^{(3)},(1+r^2)^{(2)},(r^2)^{(4)}\}.
```
At $`r=0`$,
``` math
\mathop{\mathrm{spec}}(\Delta_0)=\{0^{(7)},1^{(2)}\}.
```
Hence the smallest positive fiberwise eigenvalue is $`r^2`$ and the reduced fiberwise Green norm grows as $`r^{-2}`$.*

</div>

<div class="proof">

*Proof.* The three rows of $`d_r`$ are orthogonal with squared norms $`1+r^2,r^2,r^2`$. These are the nonzero eigenvalues of both $`d_rd_r^{\dagger}`$ and $`d_r^{\dagger}d_r`$, with each nonzero singular value appearing in both blocks of $`\Delta_r`$. The stated multiplicities and inverse norm follow directly. ◻

</div>

At $`r=2`$, the spectrum is $`\{0^{(3)},4^{(4)},5^{(2)}\}`$; at $`r=0`$, the kernel jumps from dimension three to seven. The full complex is regular while the open-stratum contraction using $`1/r`$ is not. This is why the cohesive object cannot be replaced globally by its rank-three open-stratum cohomology.

# Descent, holonomy, and compatible projection

## Nonlinear Cech descent

Let $`\{\mathcal{M}_i\}`$ be local Riemannian configuration charts with local defect spaces $`\mathcal{E}_i`$. Suppose the overlap maps
``` math
U_{ij}:\mathcal{M}_i\to\mathcal{M}_j,
\qquad
V_{ij}:\mathcal{E}_i\to\mathcal{E}_j
```
are respectively Riemannian isometries and unitary maps, and
``` math
\begin{equation}
\Phi_j\circ U_{ij}=V_{ij}\circ\Phi_i.
\label{eq:defect-descent}
\end{equation}
```

<div id="thm:repair-descent" class="theorem">

**Theorem 12** (Nonlinear repair descent). *The local costs $`\mathcal{C}_i=\frac12\left\lVert \Phi_i \right\rVert^2`$, negative-gradient fields $`X_i=-\mathop{\mathrm{grad}}\mathcal{C}_i`$, and their local flows $`R_i(s)`$ obey
``` math
\begin{align}
\mathcal{C}_j\circ U_{ij}&=\mathcal{C}_i,\\
TU_{ij}X_i&=X_j\circ U_{ij},\\
U_{ij}\circ R_i(s)&=R_j(s)\circ U_{ij}.
\end{align}
```
Therefore the nonlinear Cech equalizer
``` math
\Gamma(\mathcal{M})=
\{(x_i):x_j=U_{ij}x_i\text{ on every overlap}\}
```
is preserved. Compatible fixed points, basins, and existing asymptotic limits descend. A single-valued global basin label must lie in
``` math
\bigcap_{\gamma}\operatorname{Fix}(\operatorname{Hol}_{\gamma})
```
for the induced label local system.*

</div>

<div class="proof">

*Proof.* Equation <a href="#eq:defect-descent" data-reference-type="eqref" data-reference="eq:defect-descent">[eq:defect-descent]</a> and unitarity give equality of the local costs. Differentiating that equality and using that $`U_{ij}`$ is an isometry intertwines the gradient fields. Uniqueness for the local initial-value problem then intertwines the flows. Passing to an existing limit commutes with the continuous overlap maps. Transport around a cycle gives the holonomy-fixed condition on a global label. ◻

</div>

This theorem does not select one basin. It says exactly when local repair is one global process. Unique actualization requires an additional theorem that one allowed global basin is selected, or an explicit probability law when several remain. Measurement need not be a privileged primitive here; it is one physical process capable of changing the local defect map and its basins.

## Tangent and spectral projection

For a finite connected cover with unitary local-system transitions, the linear equalizer is concretely
``` math
\Gamma(\mathcal H)=\ker d_0,\qquad
(d_0\psi)_{ij}=\psi_j-U_{ij}\psi_i.
```
Transport along a spanning tree determines all components from one root vector; the remaining edges impose the cycle-holonomy fixed equations. Thus the global space is the intersection of those fixed spaces, not a tensor product over overlapping charts. Projectors descend only when $`U_{ij}P_i=P_jU_{ij}`$. These are the finite linear conclusions of the local Cech–Hilbert record cited in the evidence section.

Differentiate <a href="#eq:defect-descent" data-reference-type="eqref" data-reference="eq:defect-descent">[eq:defect-descent]</a> at a compatible zero-defect fixed point. The Jacobians and Hessians intertwine, so the tangent heat semigroup preserves the linear Cech equalizer. The Hilbert-space description is thus the linearization of nonlinear descent, not its replacement.

<div id="thm:projection-calculus" class="theorem">

**Theorem 13** (Compatible projection of the repair calculus). *Let $`H\geq0`$ be a self-adjoint repair Hessian on a Hilbert space and let $`P`$ be an orthogonal projector reducing $`H`$. Put $`H_P=H|_{\mathrm{Ran}P}`$. Then, on their declared domains,
``` math
\begin{equation}
Pe^{-sH}=e^{-sH_P}P,
\qquad
P\chi_I(H)=\chi_I(H_P)P,
\qquad
PG=G_PP,
\label{eq:functional-intertwining}
\end{equation}
```
where the Green identity is taken on the corresponding harmonic complements. A unitary equivalence $`T`$ of configuration spaces and a unitary equivalence $`U`$ of residual spaces, satisfying $`\Phi'(Ta)=U\Phi(a)`$, transport the nonlinear cost jet and the tangent functional calculus at compatible zero-defect backgrounds.*

*For an isometric embedding rather than an onto equivalence, the cost jet is transported only as a pullback. Full tangent transport additionally requires, on the common operator domains,
``` math
J'T=UJ,\qquad J'^\dagger U=TJ^\dagger.
```
These identities make the embedded tangent range reducing for the self-adjoint Hessian. Without the second identity only $`T^\dagger H'T=H`$ is implied, not $`H'T=TH`$.*

</div>

<div class="proof">

*Proof.* The first three identities are consequences of the spectral theorem for a reducing subspace. The residual identity gives the pullback equality $`\mathcal{C}'(Ta)=\mathcal{C}(a)`$ and hence equality of all pulled-back cost derivatives. At a zero-defect background the two displayed derivative identities give $`H'T=J'^\dagger J'T=J'^\dagger UJ=TJ^\dagger J=TH`$. For onto unitary maps the adjoint identity follows from the chain identity. For an embedding it is an extra hypothesis. The common-domain self-adjoint intertwining then gives the claimed functional calculus. ◻

</div>

For example, let $`\Phi(x)=x`$, $`\Phi'(x,y)=x+y`$, $`Tx=(x,0)`$, and $`U=1`$. The residual and cost pull back exactly, but
``` math
H=1,\qquad H'=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
H'Tx=(x,x)\ne(x,0)=THx .
```
The transverse response prevents reduction. This explains why a dimension match, an isometric compression or a compatible cost restricted to a subspace cannot replace a full operator intertwiner.

For a non-isometric Fourier–Mukai or BHT transform, derived equivalence alone is insufficient. It may preserve Ext groups, Yoneda products, and the formal Maurer–Cartan deformation problem after dg enhancement . It does not automatically preserve the Hermitian metric, adjoint, Hodge spectrum, or numerical kernel. Those require a transported metric theorem or a quantified comparison defect.

The transported-metric result makes the latter task concrete. For a bounded invertible chain/product map $`T`$, with domains also carried by $`T`$, set
``` math
g_{\rm tr}=(T^{-1})^\dagger g\,T^{-1}.
```
Then $`T`$ is unitary for this transported metric. If a separately selected physical metric is $`g_{\rm phys}(x,y)=g_{\rm tr}(x,Ey)`$, its positive distortion $`E`$ changes the degree-$`k`$ adjoint by
``` math
D_k^{\dagger_{\rm phys}}
 =E_k^{-1}D_k^{\dagger_{\rm tr}}E_{k+1},\qquad
C_k=E_{k+1}D_k-D_kE_k .
```
Thus $`C_k=0`$ is the metric-chain compatibility test. The exact witness in the transported-metric record has transported Hodge matrix $`I_2`$ but physical matrix $`\operatorname{diag}(4,1/9)`$. Polar normalization does not automatically repair the product: if $`T=US`$, its positive factor must itself respect the differential and product for $`U`$ to be a dg-algebra map. These are explicit comparison tests, not a construction of the physical BHT operator or its HYM metric.

# Higher repair jets and graph shadows

The operator is only the quadratic shadow of nonlinear repair. Higher derivatives of the same cost provide its formal interaction tensors.

Let $`E`$ and $`F`$ be finite-dimensional inner-product spaces, let $`\Phi:E\to F`$, and allow a positive residual metric field $`W(a)`$. At a background $`a_*`$, write
``` math
R_m=D^m\Phi(a_*),
\qquad
W_m=D^mW(a_*),
\qquad
V_n=D^n\mathcal{C}(a_*),
```
where
``` math
\mathcal{C}(a)=\frac12\left\langle \Phi(a),\,W(a)\Phi(a) \right\rangle.
```

<div id="thm:repair-jet" class="theorem">

**Theorem 14** (Complete repair-jet formula). *For every ordered three-color partition $`[n]=A\sqcup B\sqcup C`$, preserving the original argument order within each block,
``` math
\begin{equation}
V_n(v_1,\ldots,v_n)
=\frac12\sum_{A\sqcup B\sqcup C=[n]}
\left\langle R_{|A|}(v_A),\,W_{|B|}(v_B)R_{|C|}(v_C) \right\rangle.
\label{eq:three-color-jet}
\end{equation}
```
At a zero-defect background,
``` math
V_2(v,w)=\left\langle R_1(v),\,W_0R_1(w) \right\rangle.
```
If $`W`$ is constant and $`\Phi`$ is polynomial of degree $`r`$, then $`V_n=0`$ for $`n>2r`$.*

</div>

<div class="proof">

*Proof.* Apply the multivariable Leibniz rule to the three factors $`\Phi,W,\Phi`$. Each derivative label is assigned exactly once to the left residual, metric, or right residual. Summing over all assignments gives <a href="#eq:three-color-jet" data-reference-type="eqref" data-reference="eq:three-color-jet">[eq:three-color-jet]</a>. If $`R_0=0`$, the terms with an empty left or right residual block vanish at order two. Polynomial termination is immediate from the maximum derivative order of the two residual factors. ◻

</div>

For the Maurer–Cartan residual $`F(a)=da+a^2`$ with constant metric, the repair cost therefore has only quadratic, cubic, and quartic vertices. They are not independent knobs: they are derivatives of one residual and one metric.

Once the reduced inverse $`G`$ of $`V_2`$ is declared, Wick contraction organizes the formal coefficients by graphs . The modal diagrammatics paper proves this graph expansion and its compatible projection theorem . The present theorem adds the missing upstream arrow:
``` math
(\Phi,W,a_*)
\longmapsto
\bigl(V_2,G,\{V_n\}_{n\geq3}\bigr)
\longmapsto
\text{formal repair graphs}.
```

This explains why Gaussian and graph structures recur. Every sufficiently smooth local repair process has a quadratic tangent shadow, and every formal quadratic expansion admits Wick organization. What is universal is the grammar. A physical Feynman rule additionally needs a signed action, grading, gauge complex, state, causal prescription, and renormalization.

# Why repair is not automatically action

This section is not a caveat added after the fact. It is a theorem-level separation. Without it, the preceding construction would overclaim exactly where it becomes most physically interesting.

## The variational-anchor test

Let $`E,F`$ be finite-dimensional real Hilbert spaces and $`\Phi:E\to F`$. A constant variational anchor is a map $`A:F\to E^*`$ defining the one-form
``` math
\alpha_a(v)=(A\Phi(a))(v).
```

<div id="thm:helmholtz" class="theorem">

**Theorem 15** (Finite Helmholtz gate). *On a star-shaped domain, a scalar functional $`S_{\mathrm{var}}`$ with $`\mathrm{d}S_{\mathrm{var}}=\alpha`$ exists if and only if $`\alpha`$ is closed, equivalently
``` math
\begin{equation}
D(A\Phi)(a)=D(A\Phi)(a)^{T}
\label{eq:helmholtz}
\end{equation}
```
for every $`a`$. When it exists, one reconstruction is
``` math
\begin{equation}
S_{\mathrm{var}}(a)=S_{\mathrm{var}}(0)
+\int_0^1\alpha_{ta}(a)\,\mathrm{d}t.
\label{eq:radial-action}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Exact one-forms are closed. Conversely, <a href="#eq:radial-action" data-reference-type="eqref" data-reference="eq:radial-action">[eq:radial-action]</a> is the Poincare radial homotopy on a star-shaped domain; differentiation and $`\mathrm{d}\alpha=0`$ give $`\mathrm{d}S_{\mathrm{var}}=\alpha`$. The coordinate form of closedness is <a href="#eq:helmholtz" data-reference-type="eqref" data-reference="eq:helmholtz">[eq:helmholtz]</a>. ◻

</div>

In local field theory the same question becomes the graded formal-adjoint Helmholtz problem on jet bundles, with boundary terms and operator domains retained explicitly . A positive metric on residual space does not supply this anchor.

## The universal first-order lift

Even when a direct anchor is absent, introduce a multiplier $`\lambda\in F`$ and define
``` math
\begin{equation}
S_{\mathrm{mult}}(a,\lambda)=\left\langle \lambda,\,\Phi(a) \right\rangle.
\label{eq:multiplier-action}
\end{equation}
```

<div id="thm:multiplier" class="theorem">

**Theorem 16** (Multiplier lift and normal square). *Every exact closure state $`a_*`$ gives a lifted critical point $`(a_*,0)`$. If $`J=D\Phi(a_*)`$, the Hessian is
``` math
\begin{equation}
\mathcal{D}_J=
\begin{bmatrix}
0&J^{\dagger}\\
J&0
\end{bmatrix},
\qquad
\mathcal{D}_J^2=
\begin{bmatrix}
J^{\dagger}J&0\\
0&JJ^{\dagger}
\end{bmatrix}.
\label{eq:multiplier-square}
\end{equation}
```
Moreover,
``` math
\ker\mathcal{D}_J=\ker J\oplus\ker J^{\dagger}.
```*

</div>

<div class="proof">

*Proof.* Varying <a href="#eq:multiplier-action" data-reference-type="eqref" data-reference="eq:multiplier-action">[eq:multiplier-action]</a> gives $`\Phi(a)=0`$ and $`D\Phi(a)^{\dagger}\lambda=0`$. Differentiating again at $`(a_*,0)`$ gives the off-diagonal block operator. Direct multiplication gives its square and kernel. ◻

</div>

The multiplier lift is a genuine first-order square root of the repair normal operator. It does not decide whether the multiplier is an ordinary field, response field, antifield, or unphysical auxiliary variable. That typing belongs to a later physical construction, such as a selected BV complex .

## Information erased by the square

<div id="prop:square-no-go" class="proposition">

**Proposition 17** (Normal-square nonselection). *The positive operator $`J^{\dagger}J`$ does not determine the sign or phase of $`J`$, the signed action Hessian, a causal inverse, or the first-order response. In particular,
``` math
J_+=\operatorname{diag}(2,3),
\qquad
J_- =\operatorname{diag}(-2,3)
```
have the same normal square $`\operatorname{diag}(4,9)`$, but their inverse responses differ in the sign of the first channel.*

</div>

If a signed self-adjoint action Hessian $`H_{\mathrm{var}}`$ is identified with $`J`$, then the repair Hessian is $`H_{\mathrm{var}}^2`$ in the simplest equal-metric case. Squaring erases the Morse index. A saddle direction of the physical action becomes a positive repair direction.

The interaction vertices also differ. If
``` math
S_{\mathrm{var}}(x)=\frac m2x^2+\frac g6x^3,
\qquad
\Phi(x)=S_{\mathrm{var}}'(x)=mx+\frac g2x^2,
```
then
``` math
S_{\mathrm{rep}}(x)=\frac12\Phi(x)^2
=\frac{m^2}{2}x^2+\frac{mg}{2}x^3+\frac{g^2}{8}x^4.
```
The signed-action rows $`(V_2,V_3,V_4)=(m,g,0)`$ become the repair rows $`(m^2,3mg,3g^2)`$. Repair graphs are therefore not physical Feynman graphs unless a separate theorem identifies the physical perturbative datum with the repair functional.

## When a signed action does exist

Let $`\mathcal{A}`$ be a differential graded associative algebra with a degree-three cyclic trace $`\tau`$ satisfying
``` math
\tau(dx)=0,
\qquad
\tau(xy)=(-1)^{|x||y|}\tau(yx).
```
For $`a\in\mathcal{A}^1`$, define
``` math
\begin{equation}
S_{\mathrm{MC}}(a)=\frac12\tau(a\,da)+\frac13\tau(a^3).
\label{eq:mc-action}
\end{equation}
```

<div id="thm:cyclic-action" class="theorem">

**Theorem 18** (Cyclic Maurer–Cartan action). *For every degree-one variation $`u`$,
``` math
\begin{equation}
DS_{\mathrm{MC}}(a)[u]=\tau\bigl(u(da+a^2)\bigr).
\label{eq:mc-variation}
\end{equation}
```
If the pairing between degrees one and two is nondegenerate, the critical locus is exactly the Maurer–Cartan locus. The action is infinitesimally gauge invariant under $`\delta_\epsilon a=d\epsilon+[a,\epsilon]`$. It descends through even projective overlaps because the scalar cocycle cancels under conjugation and the cyclic trace is conjugation invariant.*

</div>

<div class="proof">

*Proof.* Differentiate the quadratic term. The Stokes identity moves $`d`$ from the variation to $`a`$, making the two contributions equal. Cyclicity makes the three cubic contributions equal. This gives <a href="#eq:mc-variation" data-reference-type="eqref" data-reference="eq:mc-variation">[eq:mc-variation]</a>. Pairing a gauge variation with the residual and integrating by parts yields the Bianchi identity. On overlaps, each monomial is conjugated by the same even transition, and the trace removes that conjugation. ◻

</div>

On a compact complex threefold with holomorphic volume form $`\Omega`$, the candidate trace is
``` math
\tau(x)=\int_X\Omega\wedge\mathop{\mathrm{Str}}(x),
```
and <a href="#eq:mc-action" data-reference-type="eqref" data-reference="eq:mc-action">[eq:mc-action]</a> becomes holomorphic Chern–Simons theory . This supplies a signed action for the integrability lane. It does not automatically supply nondegenerate cyclic pairings for the HYM, balanced, anomaly, coframe, and Lorentzian lanes.

# The cohesive closure-repair theorem

The preceding results can now be stated as one composition theorem.

<div id="thm:master" class="theorem">

**Theorem 19** (Cohesive closure-repair and shadow theorem). *Suppose the following data are supplied:*

1.  *a metric configuration space with a smooth defect section $`\Phi`$, smooth metric data and an exact-zero background $`p_*`$ (a $`C^N`$ source gives only the cost jet through the available order);*

2.  *compatible local isometric/unitary descent data;*

3.  *on the cohesive branch, an integrable possibly twisted superconnection whose endomorphism algebra realizes the defect complex;*

4.  *a Hermitian structure and self-adjoint elliptic domains; and*

5.  *any declared orthogonal projection or isometric transform reducing the linearized operator.*

*Then one and the same source determines, functorially:
``` math
\begin{equation}
\begin{gathered}
\mathcal{C}=\tfrac12\left\lVert \Phi \right\rVert^2,
\qquad
X=-\mathop{\mathrm{grad}}\mathcal{C},
\qquad
H=D\Phi(p_*)^{\dagger}D\Phi(p_*),\\
e^{-sH},
\qquad
P_0,
\qquad
G=H^{-1}(I-P_0),
\qquad
\chi_I(H),
\qquad
K_f(x,y)=\langle x|f(H)|y\rangle,\\
\{D^n\mathcal{C}(p_*)\}_{n\geq3}
\quad\text{and their finite formal repair graphs}.
\end{gathered}
\label{eq:master-chain}
\end{equation}
```
The nonlinear flow, tangent calculus, and existing basin limits descend through the compatible local chart equivalences. Reducing projections transport the tangent functional calculus. An onto unitary equivalence of the full residual and metric transports every object in <a href="#eq:master-chain" data-reference-type="eqref" data-reference="eq:master-chain">[eq:master-chain]</a>. An embedded nonlinear subsystem additionally needs invariance of its repair vector field; exact retained graph transport requires compatibility of the full typed vertex, grading and contraction data, as in the diagrammatics theorem. Reduction of the quadratic operator alone does not supply these nonlinear hypotheses.*

*The theorem does not identify $`\mathcal{C}`$ with a signed physical action. Such an identification requires a variational anchor or a separately typed multiplier/cyclic construction. Nor does the theorem select the original defect, metric, background, causal domain, state, or projection.*

</div>

<div class="proof">

*Proof.* The first variation, full Hessian, and exact-zero normal square are <a href="#thm:residual-hessian,cor:zero-normal-square" data-reference-type="ref+label" data-reference="thm:residual-hessian,cor:zero-normal-square">[thm:residual-hessian,cor:zero-normal-square]</a>. The repair flow and its tangent semigroup are <a href="#thm:repair-flow" data-reference-type="ref+label" data-reference="thm:repair-flow">6</a>. Cohesive realization and twist cancellation are <a href="#thm:end-untwist,thm:mc-repair" data-reference-type="ref+label" data-reference="thm:end-untwist,thm:mc-repair">[thm:end-untwist,thm:mc-repair]</a>. Elliptic Hodge theory supplies the functional calculus in <a href="#thm:hodge-kernel" data-reference-type="ref+label" data-reference="thm:hodge-kernel">10</a>. Nonlinear descent and compatible transport are <a href="#thm:repair-descent,thm:projection-calculus" data-reference-type="ref+label" data-reference="thm:repair-descent,thm:projection-calculus">[thm:repair-descent,thm:projection-calculus]</a>. The complete cost jet is <a href="#thm:repair-jet" data-reference-type="ref+label" data-reference="thm:repair-jet">14</a>; formal Wick contraction then produces its graph weights. The final nonidentification statement follows from <a href="#thm:helmholtz,thm:multiplier,prop:square-no-go,thm:cyclic-action" data-reference-type="ref+label" data-reference="thm:helmholtz,thm:multiplier,prop:square-no-go,thm:cyclic-action">[thm:helmholtz,thm:multiplier,prop:square-no-go,thm:cyclic-action]</a>. ◻

</div>

The theorem says something stronger than “an operator generates repair.” The nonlinear repair field exists first. Its derivative produces the operator. Yet it also says something more careful than “closure explains all operators.” Only the displayed class of positive tangent operators is obtained, and only after its source data are supplied.

# The q79 benchmark and its exact boundary

## What is already constructed

The current q79 research program provides a hash-bound $`\alpha`$-twisted cohesive benchmark $`\mathcal{S}_{\mathrm{HS}}`$ on $`J`$. On that object, the following are exact:

1.  the twisted cohesive representative and ordinary global endomorphism dg algebra;

2.  the canonical Maurer–Cartan curvature residual;

3.  the positive Hodge repair Hessian after a Hermitian choice;

4.  the tangent heat semigroup, harmonic projector, and reduced Green operator on the global total space;

5.  projective local descent of the finite coherent repair witness; and

6.  conditional transport of Ext, Yoneda, and formal Maurer–Cartan data through a dg-enhanced BHT/Fourier–Mukai equivalence.

The q79 result is not merely a finite analogy. It applies the general mathematics to one explicit twisted perfect-complex atlas. But it is a benchmark object, not yet the selected physical visible/hidden endpoint.

## The proposed full defect and why it remains proposed

The physical source program organizes the Hull–Strominger obligations into a multi-lane residual of the schematic form
``` math
\begin{equation}
\Phi_{\mathrm{phys}}=
(\Phi_0,\mu_{TX},\mu_V,\mu_W,
\Phi_{\mathrm{bal}},\Phi_{\mathrm{AB}},\Phi_{\mathrm{SU(3)}}).
\label{eq:seven-lane}
\end{equation}
```
Here $`\Phi_0`$ denotes integrability, the $`\mu`$-rows denote HYM moment maps, $`\Phi_{\mathrm{bal}}`$ balanced geometry, $`\Phi_{\mathrm{AB}}`$ anomaly/Bianchi closure, and the final row the declared $`\mathrm{SU}(3)`$ normalization or coordinate constraint.

If a selected endpoint $`s_*`$ satisfies $`\Phi_{\mathrm{phys}}(s_*)=0`$, then the positive physical repair Hessian is exactly
``` math
\begin{equation}
A_*=D\Phi_{\mathrm{phys}}(s_*)^{\dagger}
D\Phi_{\mathrm{phys}}(s_*).
\label{eq:physical-candidate}
\end{equation}
```
Writing the linearization as a deformation-complex block $`J_*`$ and additional physical rows $`K_*`$ gives
``` math
\begin{equation}
A_*=J_*^{\dagger}J_*+K_*^{\dagger}K_*.
\label{eq:augmented-hessian}
\end{equation}
```
This is an exact identity *if the same selected endpoint, metric, and domains supply every row*. The current corpus has not yet supplied that complete physical object. Equation <a href="#eq:augmented-hessian" data-reference-type="eqref" data-reference="eq:augmented-hessian">[eq:augmented-hessian]</a> is therefore the correct target theorem, not a declaration that the target has already been reached.

## The explicit residual and its block support

The full-residual record improves the schematic notation in <a href="#eq:seven-lane" data-reference-type="eqref" data-reference="eq:seven-lane">[eq:seven-lane]</a> to an explicit differential-operator compiler. Write $`\nu=\|\Omega\|_\omega`$, and reserve $`c_{\rm vol}`$ for the volume normalization constant, not a third Chern class. The six extra rows are
``` math
\begin{align}
\mu_{TX}&=R_\Theta\wedge\omega^2,&
\mu_V&=F_V\wedge\omega^2,&
\mu_W&=F_W\wedge\omega^2,\nonumber\\
\mathcal B&=d(\nu\omega^2),\nonumber\\
\mathcal A&=dH-\frac{\alpha'}4
 \bigl(\operatorname{tr}R_\Theta^2-\operatorname{tr}F_V^2
                         -\operatorname{tr}F_W^2\bigr),\nonumber\\
\mathcal N&=i\Omega\wedge\bar\Omega-c_{\rm vol}\omega^3.
\label{eq:explicit-six-rows}
\end{align}
```
Their target is the orthogonal sum of the six spaces
``` math
\begin{gathered}
\Omega^6(\operatorname{ad}TX),\quad\Omega^6(\operatorname{ad}V_3),\quad\Omega^6(\operatorname{ad}W_9^\tau),\\
\Omega^5,\quad\Omega^4,\quad\Omega^6 .
\end{gathered}
```
This is a choice of positive repair metric after a common scale is factored out. It is not an identification with a Lorentzian action.

At a fixed complex-structure chart, put $`a=(a_{TX},a_V,a_W)`$. Exterior differentiation and the covariant curvature variation give
``` math
\begin{align}
K_{TX}v&=d_\Theta a_{TX}\wedge\omega^2+
               2R_\Theta\wedge\omega\wedge\dot\omega,\nonumber\\
K_Vv&=d_{A_V}a_V\wedge\omega^2+
               2F_V\wedge\omega\wedge\dot\omega,\nonumber\\
K_Wv&=d_{A_W}a_W\wedge\omega^2+
               2F_W\wedge\omega\wedge\dot\omega,\nonumber\\
K_{\mathcal B}v&=d\{\nu(2\omega\wedge\dot\omega+
                                \dot{\log\nu}\,\omega^2)\},\nonumber\\
K_{\mathcal A}v&=d\dot H-\frac{\alpha'}2
  \{\operatorname{tr}(R_\Theta\wedge d_\Theta a_{TX})
       -\operatorname{tr}(F_V\wedge d_{A_V}a_V)
       -\operatorname{tr}(F_W\wedge d_{A_W}a_W)\},\nonumber\\
K_{\mathcal N}v&=i(\dot\Omega\wedge\bar\Omega+
                      \Omega\wedge\dot{\bar\Omega})
                      -3c_{\rm vol}\omega^2\wedge\dot\omega .
\label{eq:explicit-K}
\end{align}
```
Here $`\dot{\log\nu}=\operatorname{Re}\langle\dot\Omega,\Omega\rangle/
\|\Omega\|^2-\tfrac12\operatorname{tr}_g\dot g`$ in the packet’s fixed-chart metric convention. Varying complex structure requires the corresponding typed chart terms as well; these formulas do not supply their endpoint coefficients. In particular the factor $`\alpha'/2`$, rather than $`\alpha'/4`$, is forced by differentiating the curvature square.

The rank-102 complex fiber is
``` math
\mathcal Q=T^*X\oplus\operatorname{ad}(TX)\oplus\operatorname{ad}(V_3)
              \oplus\operatorname{ad}(W_9^\tau)\oplus TX,\qquad
\mathbf r=(3,8,8,80,3).
```
It is not the full form-augmented Hilbert space and not a finite discretization dimension. In this lane order the extra-row incidence is
``` math
I_K=\begin{pmatrix}
1&1&0&0&1\\
1&0&1&0&1\\
1&0&0&1&1\\
1&0&0&0&1\\
1&1&1&1&1\\
1&0&0&0&1
\end{pmatrix}.
```
A one means allowed dependence, not a certified nonzero coefficient. The anomaly row has a common target for all five lanes. Its Gram square therefore allows all 25 ordered blocks and $`102^2=10\,404`$ ordered fiber positions. Omitting it had allowed only 19 blocks and 7 716 positions. The six cross-gauge blocks contribute $`2(8\cdot8+8\cdot80+8\cdot80)=2\,688`$ positions. They must not be forced to zero before evaluating the same-source operator. Nor may the real Bianchi row be deleted as already contained in the complex without a same-domain isometry proving that exact redundancy.

This correction changes the possible coupling pattern, not the positivity identity. On the common closed form domain,
``` math
H_{\rm phys}=\Delta_{\mathcal Y,1}+K^\dagger K
 \ \geq\ \Delta_{\mathcal Y,1},\qquad
\ker H_{\rm phys}=\ker\Delta_{\mathcal Y,1}\cap\ker K .
```
The finite witness in the source has $`\Delta=\operatorname{diag}(0,0,1,2,4)`$ and $`K=(1,1,0,0,0)`$. It removes one of two harmonic directions and retains a positive gap of one. That example shows why neither the harmonic projector nor a scalar rescaling of the bare Hodge operator can be assumed.

There is also a lawful conditional sparsification. If the physical endpoint, residual, metric and Galerkin projection all respect the projective $`E[3]`$ action, character orthogonality removes unequal-character blocks. The hidden adjoint multiplicities are 8 for the trivial character and 9 for each of eight others. If, additionally, all 22 non-hidden modes are trivial, the count becomes
``` math
30^2+8\cdot9^2=1\,548 .
```
The general count is $`\sum_\chi(m_{{\rm ext},\chi}+m_{{\rm hid},\chi})^2`$. The value 1 548 is not a selected physical matrix count until these representation and invariance hypotheses are verified. It complements, and does not retract, the unconditioned 25-block support.

These are imported compiler results, not newly proved source existence. The earlier candidate audit in that record is historical. In particular, later hidden-carrier and existential HYM progress retained in the Flux paper is not undone by its old status fields. A common physical visible endpoint, all differential residual rows and their numerical coefficients are the stronger input needed here.

## The shared circle

The shared circle enters this construction as a differential line $`(L_{\mathrm{sh}},\nabla_{\mathrm{sh}})`$ and its equivariance, not as an extra coordinate and not as physical time. The finite q79 theorem already shows that one universal flat cyclic line acts compatibly on the selected finite carriers and commutes with their projectors and finite Hessian. The continuum promotion must prove the corresponding relation
``` math
[\nabla_{\mathrm{sh}},D\Phi_{\mathrm{phys}}]=0
```
in the appropriate equivariant sense. It would then follow that the repair Hessian and all its functional-calculus shadows preserve the shared charge sectors. This is a serious unification condition. It does not identify compact phase with Lorentzian time.

## Status table

<div class="center">

| Object or arrow | Status | Boundary |
|:---|:---|:---|
| General covariant residual Hessian | Exact here | Includes nonzero-defect correction |
| Exact-zero normal square and repair semigroup | Exact here | Requires selected metric and domain |
| Twisted cohesive endomorphism dg algebra on $`\mathcal{S}_{\mathrm{HS}}`$ | Exact structural benchmark | Scalar twist cancels in $`\mathop{\mathrm{End}}`$ |
| Maurer–Cartan repair and Hodge tangent on $`\mathcal{S}_{\mathrm{HS}}`$ | Exact structural benchmark | Hermitian metric exists but is not physically selected |
| Local nonlinear repair descent | Exact here | Does not select one basin |
| Isometric functional-calculus transport | Exact conditional | Arbitrary derived equivalence is not unitary |
| Repair jet to formal graph data | Exact finite/formal | Not a physical QFT action |
| Cyclic action for the integrability lane | Exact conditional | Requires cyclic trace and domain hypotheses |
| Selected physical $`V_3/W_9`$ cohesive or pure-bundle endpoint | Open | Current source-selection frontier |
| Full HYM/balanced/anomaly action and real slice | Open | Current action frontier |
| Lorentzian causal operator and state | Open | Cannot be inferred from the positive square |
| Continuum-to-finite product/Hodge intertwiner | Open | Current geometry frontier |

</div>

# What the theorem changes downstream

## Fixed points

The fixed-point theory keeps its existing theorem ownership. It proves existence, uniqueness under suitable hypotheses, smoothing, projection control, and convergence. The present paper supplies one principled source for the energy and tangent generator to which those theorems may be applied. It does not repeat their analytic hypotheses or promote a finite witness to an infinite-dimensional flow.

## Wave and particle representations

The positive filtered operator in the wave–particle paper no longer needs to be viewed as mathematically arbitrary on the cohesive benchmark. It can be the functional calculus of a repair Hessian. Its local and spectral descriptions then become the localized and normal-mode shadows of one tangent repair process. The quantum state, Born bridge, instrument, and physical time evolution remain separate obligations.

## Perturbative graphs

The graph paper begins with typed quadratic and higher tensors. The repair jet theorem derives one entire such tensor family from $`(\Phi,W)`$. This removes independent repair vertices as source inputs. It does not remove physical couplings from a QFT until the repair functional is proved to be the physical signed action or is related to it by a certified variational map.

## Quantum field theory

The existing selected free q79 CAR/AQFT result uses standard quantum-field machinery after its geometric input is supplied. The present paper does not rederive that machinery. It clarifies the upstream division of labor: positive repair controls stabilization and Euclidean/Hodge localization; the signed gauge-fixed action controls physical response and causal Green operators; the state and renormalization prescription complete the quantum theory.

## Gravity

If a gravitational defect system is selected, its positive repair Hessian and kernel follow by the same theorem. This supports the MTT intuition that geometry may respond to closure pressure. It does not prove that Einstein’s equations are the selected repair equation, that the stress tensor has the required normalization, or that the resulting theory is UV complete. The Lorentzian principal symbol and causal domains must be derived from the signed physical system, not guessed from a positive Hilbert-space metric.

# Theorem ownership and corpus placement

This paper is intended to prevent the same upstream theorem from being reproved in several downstream papers.

<div class="center">

| Result | Canonical owner | Use elsewhere |
|:---|:---|:---|
| Covariant residual Hessian and exact-zero normal square | This paper | Foundations, Fixed Points, QG may cite |
| Repair flow to tangent heat semigroup | This paper | Wave–particle and stabilization papers may cite |
| Cohesive q79 realization and twist cancellation | This paper as synthesis; executable theorem packet as evidence | Source and bundle papers may cite |
| Repair descent and compatible functional calculus | This paper | Projection papers may import conclusion |
| Repair jet to formal graph tensors | This paper | Modal diagrammatics retains graph theorem ownership |
| Finite graded Wick and graph-projection theorem | Modal diagrammatics | Imported here without proof duplication |
| Fixed-point existence and convergence | Fixed Points I and successors | Imported here |
| Conditional wave–particle operator encoding | Wave–particle paper | Receives a structural source candidate here |
| Physical q79 endpoint and action | No completed owner yet | Research frontier, not a theorem in this paper |

</div>

The new result should therefore be added to the related papers by a concise cross-reference and status update, not by copying the proofs. This keeps the corpus readable and makes later corrections local.

# Falsifiers and acceptance tests

The structural theorem is falsified in an application if any required map or domain fails. The physical interpretation fails if a stronger claim is made without its bridge. A candidate promotion should pass the following tests.

1.  **Defect source:** specify every residual row, bundle, connection, domain, and source hash.

2.  **Background:** prove whether the selected state has zero defect. If it does not, compute the residual Hessian correction.

3.  **Metric:** derive or explicitly declare the field and residual metrics; do not infer them from a categorical equivalence.

4.  **Descent:** verify the literal overlap maps, cocycles, and isometric/unitary compatibility.

5.  **Hodge domain:** prove self-adjointness, ellipticity or the appropriate hyperbolic replacement, and boundary conditions.

6.  **Projection:** verify reduction of the operator and preservation of the nonlinear residual jet, not only matching dimensions.

7.  **Action:** provide a Helmholtz/cyclic anchor or a fully typed multiplier/BV lift. Do not call the positive square the physical action.

8.  **Causality:** derive retarded, advanced, or Feynman prescriptions from the signed gauge-fixed operator and state.

9.  **Strata:** test Green and contraction bounds near every cohomology-rank jump.

10. **Numerics:** evaluate endpoint coefficients only after the same source has passed the structural tests.

These tests turn the paper into a research instrument. A failure identifies which arrow is missing; it does not send the program back to the beginning.

# Frontier theorem

The later endpoint-factorization record organizes seven acceptance rows into three structured sources:

1.  **GAS**, geometry and action: the physical endpoint and signed upper action;

2.  **SYN**, spectral synthesis: the analytic intertwiner and compatible chain/product contraction data;

3.  **BV4**, a BV-compatible four-dimensional compactification.

Shared-line functional calculus and the Galerkin/Feshbach execution are then consequences of compatible GAS and SYN data, rather than two more independent source objects. Three structured sources are not three scalar parameters. None of the three complete physical packages is accepted in the cited record. This dependency reduction preserves the exact finite constructions while preventing another round of inventing independent kernels for already derived arrows.

The decisive next theorem is not another abstract Hessian statement. That part is now complete. It is a selected-source theorem of the following form.

<div class="conjecture">

**Conjecture 20** (Selected physical cohesive-source theorem). There exists a selected q79 Hull–Strominger endpoint $`s_*`$, represented either by a stable pure-bundle source or by a physically admitted cohesive source, together with:

1.  the full defect section $`\Phi_{\mathrm{phys}}`$ and a common Hermitian metric;

2.  the shared differential line and equivariant connections;

3.  a cyclic or BV variational structure whose Euler–Lagrange rows agree with the selected physical residual on a declared gauge slice;

4.  Lorentzian externalization, real structure, and causal domains; and

5.  a continuum-to-finite chain, product, Hodge, and normalization intertwiner with an error certificate.

At an exact endpoint, the positive repair operator is $`A_*=D\Phi_{\mathrm{phys}}^{\dagger}D\Phi_{\mathrm{phys}}`$, while the signed physical operator is obtained from the certified variational structure rather than inferred from $`A_*`$.

</div>

Proving this conjecture would connect the upper bundle geometry, cohesive deformation theory, shared phase, fixed points, wave kernels, finite q79 operators, and the signed physical theory without conflating them. It is a sharp target because every required object has a declared type and every invalid shortcut has already been removed.

# Discussion

## What has genuinely been gained

The main gain is upstream organization. The heat kernel is no longer merely an attractive analogy for coherence. Under the theorem’s hypotheses it is the exact tangent propagator of nonlinear defect repair. The harmonic sector is the kernel of the same Hessian. The spectral projector and local kernel come from its functional calculus. The formal repair vertices are higher derivatives of the same cost. Compatible projection preserves the whole package.

This makes several previously separate papers part of one coherent story:
``` math
\begin{gathered}
\text{closure defect and metric}
\longrightarrow
\text{repair flow},\\
\text{repair flow}
\longrightarrow
\text{Hodge Hessian},\\
\text{Hodge Hessian}
\longrightarrow
\text{heat, Green, and spectral kernels},\\
\text{higher repair jet}
\longrightarrow
\text{formal graph grammar},\\
\text{compatible projection}
\longrightarrow
\text{retained shadows}.
\end{gathered}
```

## What has not been gained

The same clarity exposes the missing physics. A positive normal square cannot tell us which first-order sign or phase nature uses. It cannot choose a Lorentzian causal prescription. It cannot distinguish a physical saddle from a repair minimum. It cannot supply a quantum state, a Born rule, or a renormalization scheme. These are not small numerical corrections; they are different typed structures.

The result is therefore neither “only mathematics” nor a completed theory of everything. It is a rigorous mathematical bridge that narrows the physical frontier. It tells us which downstream constructions are already forced once a selected source exists, and which ones still require genuinely new input.

## Why the cohesive route matters

The cohesive route is especially useful because it remains regular where an open-stratum bundle contraction fails. It allows the full derived object to carry a global differential, deformation algebra, and Hodge calculus without first pretending that the cohomology rank is constant. This may be the right preprojection language for MTT. It may also turn out to be only an auxiliary resolution of a physical pure-bundle endpoint. The present theorem permits both outcomes and gives a concrete test between them.

# Conclusion

Closure is not represented here first as a static operator. It is represented by a nonlinear defect and the process that reduces its cost. The operator appears as the derivative of that process at an admissible state. Hodge theory, heat flow, Green response, spectral projection, local kernels, and formal repair graphs then follow as exact shadows of one source.

The result is strongest precisely because its boundary is explicit. At a nonzero-defect critical point the Hessian contains a residual correction. A derived equivalence is not automatically isometric. A global cohesive operator does not guarantee a uniform fiberwise Green family. A positive repair functional is not a signed action. A kernel is not automatically a quantum propagator. A descended basin map is not automatically unique actualization.

For q79, the cohesive Hartshorne–Serre benchmark now realizes the structural chain exactly after a Hermitian choice. The next leap is no longer to guess another operator. It is to select the physical endpoint, metric, cyclic or BV action, Lorentzian domains, and continuum-to-finite intertwiner from one source. If that is achieved, much of the downstream operator language will already be waiting as theorem rather than assumption.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The universal proofs in this paper are analytic or finite algebraic. Their MTT-specific instantiations are pinned in the curated [MTT Results Reproduction repository](https://github.com/PeterNero/mtt-results-repro). The principal result records are:

- the q79 cohesive-superconnection record;

- the q79 Maurer–Cartan repair record;

- the local Cech–Hilbert and nonlinear repair-descent records;

- the covariant residual-Hessian record and nonzero-defect witness;

- the reversible–dissipative repair record;

- the repair-jet graph-functor record;

- the variational-anchor and multiplier-lift record;

- the cyclic Maurer–Cartan action-descent record; and

- the q79 string cyclic-cotangent boundary record.

Version 3 additionally imports:

- the explicit six-row/25-block compiler: `q79_v3w9_full_residual`;

- its conditional character reduction: `q79_rank102_qutrit_reduction`;

- the bounded transported-metric record: `preprojection_bht_transported_metric`;

- the endpoint factorization record, listed under
  `causal_base_q79_seven_row_endpoint_factorization_packet`.

The local Cech equalizer, nonlinear descent, nonzero-defect example and phase-loss and damping witnesses are explicitly compared in the current contextual integration ledger. These imports use the frozen result manifest at [`f141a20ea23c`](https://github.com/PeterNero/mtt-results-repro/tree/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results); the integration companion gives each artifact hash and manuscript location. Each record declares its theorem tier, source artifacts, verifier, zero-fit status, and nonpromotion guards. The exact witnesses use rational or symbolic arithmetic where stated. They do not select the physical q79 endpoint or supply measured values. The source TeX, generated Markdown, compiled PDF, metadata hashes, and version-provenance audit accompany this paper in the public MTT papers repository. The evidence snapshot used for Version 1 is commit `ba0874012246bb930677ebfa6f0a6eb33a57a8f0`.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
