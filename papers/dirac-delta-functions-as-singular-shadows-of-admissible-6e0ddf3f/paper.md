---
abstract: |
  Dirac delta distributions play several mathematically different roles in physics. They are identity kernels, point sources, hard constraints, conservation distributions, formal densities of continuous observables, and local gauge-slice selectors. This paper separates those roles before asking which admit finite-resolution representatives. On a compact elliptic background, spectral projector kernels converge to the diagonal delta distribution, with the Sobolev truncation estimate
  ``` math
  \|(I-\Pi_\Lambda)f\|_{H^s}
  \leq (1+\Lambda)^{-r/2}\|f\|_{H^{s+r}}.
  ```
  Heat kernels give a different, nonprojective approximate identity and obey
  ``` math
  \|(e^{-\tau\Delta}-I)f\|_{H^s}
  \leq \tau^{r/2}\|f\|_{H^{s+r}},
  \qquad 0\leq r\leq2.
  ```
  For a smooth submersion $`C:\mathbb R^n\to\mathbb R^m`$, normalized Gaussian tubes converge by the coarea formula to the correctly Jacobian-weighted constraint distribution on $`C^{-1}(0)`$. Compression of the canonical commutation relations by an orthogonal projection replaces the full inner product kernel by the projected kernel exactly, but only in that declared compressed theory. These results support a restricted Modal Triplet Theory (MTT) diagnostic: when a delta occurs in a downstream model, one should ask whether selected upstream geometry emits a finite projector, smoothing kernel, source profile, detector response, or constraint tube, and in which topology the sharp limit is controlled. They do not imply that every delta is a hidden projection, that a spectral gap fixes a physical width, or that finite smearing by itself solves gauge fixing, measurement, ultraviolet renormalization, or outcome selection.
author:
- Peter Nero
current_version: v1
date: July 2026, Version 1
generated_from_main_tex_sha256: d90f0bbd4956b4f64433c2a3171d9820a74c76f497df56116fe1519668c63ad5
paper_id: dirac-delta-functions-as-singular-shadows-of-admissible-6e0ddf3f
release_state: zenodo_released
released_version: v1
title: |
  Dirac Delta Limits, Spectral Kernels, and the MTT Finite-Kernel Diagnostic
  Exact Approximate Identities, Constraint Tubes, and Scope Boundaries
zenodo_doi: 10.5281/zenodo.21665962
zenodo_record_id: 21665962
zenodo_url: "https://zenodo.org/records/21665962"
---

# Version 1 Revision Note

Supersedes
The unversioned April 2026 manuscript *Dirac Delta Functions as Singular Shadows of Admissible Projection: A Fixed-Point and Gauge-Theoretic Formulation in Modal Triplet Theory*.

Reason
The earlier manuscript treated all physical delta distributions as zero-width projections, inferred finite physical width from a spectral gap, assigned a delta outcome to every deterministic fixed-point basin, and extended a local Faddeev–Popov Jacobian argument to global functional gauge fixing. It also used an unnormalized Gaussian constraint filter and suggested that replacing deltas by finite kernels generally resolves renormalization.

Resolution
This version classifies the distinct uses of the delta, proves separate spectral, heat-kernel, constraint-tube, and compressed-CCR statements with explicit hypotheses and error topologies, corrects the fixed-point claim, and limits the gauge argument to a local finite-dimensional model. Measurement and field-theory applications are stated at their actual tiers.

Retained result
Spectral projectors and heat kernels provide rigorous finite kernels approaching the identity distribution, normalized constraint tubes converge by coarea, and finite-sector compression yields an exact projected commutator kernel.

Remaining boundary
No theorem here derives a particular cutoff, detector width, source profile, gauge slice, or regularization scale from the selected MTT carrier. Global non-Abelian gauge fixing, arbitrary measurement contexts, one-history completion, and symmetry-preserving ultraviolet completion remain separate problems.

# Why the uses of $`\delta`$ must be separated

The Dirac delta is a distribution, not an ordinary function. On $`\mathbb R^d`$, its defining property is
``` math
\langle\delta_{x_0},f\rangle=f(x_0),
\qquad f\in C_c^\infty(\mathbb R^d).
```
That single definition supports several constructions whose physical meanings are not interchangeable. A delta may represent an exact identity operator, an ideal point source, a constraint surface with a Jacobian, or the Fourier expression of an exact symmetry. In other settings it is only a formal density for an operator-valued measure.

The earlier projection reading noticed something useful: many sharp distributional objects can be approached by finite kernels. The mistake was to turn that useful construction into a universal origin claim. The corrected question is narrower:

> For this particular occurrence of a delta, is there a selected finite object whose controlled limit gives the distribution, and does replacing the delta preserve the mathematical and physical structure that matters?

<div class="center">

| Use | Exact object | Possible finite representative |
|:---|:---|:---|
| Identity kernel | Diagonal delta distribution | Spectral projector or heat kernel |
| Point source | Distributional forcing term | Extended source density |
| Hard constraint | Level-set distribution with Jacobian | Normalized constraint tube |
| Momentum conservation | Fourier distribution from translation invariance | Finite spacetime-window transform |
| PVM density | Formal density of a PVM | Detector-smeared POVM |
| Gauge slice | Local constraint and orbit Jacobian | Finite gauge tube, locally |

</div>

The third column is not automatic. Each proposed finite representative needs a normalization, a convergence topology, and a source theorem if it is to be a prediction rather than a regulator chosen by hand.

# The diagonal delta is the identity kernel

Let $`X`$ be a compact smooth Riemannian manifold with volume form $`\mathrm{d}V`$. The diagonal delta distribution $`\delta_{\mathrm{diag}}\in\mathcal D'(X\times X)`$ is defined by
``` math
\langle\delta_{\mathrm{diag}},\Psi\rangle
=\int_X\Psi(x,x)\,\mathrm{d}V(x),
\qquad \Psi\in C^\infty(X\times X).
```
With the usual kernel convention, it represents the identity:
``` math
f(x)=\int_X\delta_{\mathrm{diag}}(x,y)f(y)\,\mathrm{d}V(y).
```
This statement is exact. It does not assert that a finite physical process has generated the identity operator.

An orthogonal projection $`P:\mathcal H\to\mathcal H`$ is also an exact bounded operator. If it has a kernel $`K_P`$, that kernel represents the identity only on $`\mathrm{Ran}(P)`$:
``` math
Pf=f\qquad\text{for }f\in\mathrm{Ran}(P).
```
An arbitrary bounded projection need not possess a pointwise smooth or bounded kernel. Kernel regularity follows only after additional hypotheses such as finite rank, Hilbert–Schmidt regularity, or smoothing. This qualification is essential whenever a finite coherent projector is presented as a physical profile.

# Spectral projectors approach the identity

<div id="ass:elliptic" class="assumption">

**Assumption 1** (Compact elliptic setting). Let $`\Delta\geq0`$ be a nonnegative self-adjoint Laplace-type operator on $`L^2(X)`$, where $`X`$ is compact and has either no boundary or a fixed self-adjoint elliptic boundary condition. Let
``` math
\Delta\phi_j=\lambda_j\phi_j,
\qquad
0\leq\lambda_0\leq\lambda_1\leq\cdots,
```
where $`\{\phi_j\}`$ is a complete orthonormal eigenbasis.

</div>

For $`\Lambda\geq0`$, define
``` math
\Pi_\Lambda f
=\sum_{\lambda_j\leq\Lambda}
\langle\phi_j,f\rangle\phi_j
```
and
``` math
K_\Lambda(x,y)
=\sum_{\lambda_j\leq\Lambda}
\phi_j(x)\overline{\phi_j(y)}.
```
Each $`\Pi_\Lambda`$ is a finite-rank orthogonal projection and $`K_\Lambda`$ is smooth.

<div id="thm:spectral-kernel" class="theorem">

**Theorem 2** (Spectral projector kernel limit). *Under Assumption <a href="#ass:elliptic" data-reference-type="ref" data-reference="ass:elliptic">1</a>,
``` math
K_\Lambda\longrightarrow\delta_{\mathrm{diag}}
\quad\text{in }\mathcal D'(X\times X)
```
as $`\Lambda\to\infty`$. Equivalently, $`\Pi_\Lambda f\to f`$ in $`C^\infty(X)`$ for every $`f\in C^\infty(X)`$.*

</div>

<div class="proof">

*Proof.* For $`s\in\mathbb R`$, use the spectral Sobolev norm
``` math
\|f\|_{H^s}^2
=\sum_j(1+\lambda_j)^s
|\langle\phi_j,f\rangle|^2.
```
If $`f`$ is smooth, then $`f\in H^s`$ for every $`s`$, and the spectral tail converges to zero in every Sobolev norm. Sobolev embedding therefore gives $`\Pi_\Lambda f\to f`$ in $`C^k(X)`$ for every $`k`$.

The Schwartz kernel theorem identifies continuous operators $`C^\infty(X)\to\mathcal D'(X)`$ with distributions on $`X\times X`$. The preceding convergence, together with the uniform Sobolev tail estimates below, implies convergence of the corresponding kernels in the distribution topology. The kernel of the limiting identity operator is $`\delta_{\mathrm{diag}}`$. ◻

</div>

<div id="thm:spectral-error" class="theorem">

**Theorem 3** (Quantitative spectral truncation). *For $`r\geq0`$, $`s\in\mathbb R`$, and $`f\in H^{s+r}(X)`$,
``` math
\|(I-\Pi_\Lambda)f\|_{H^s}
\leq
(1+\Lambda)^{-r/2}\|f\|_{H^{s+r}}.
```*

</div>

<div class="proof">

*Proof.* Writing $`f_j=\langle\phi_j,f\rangle`$,
``` math
\begin{align*}
\|(I-\Pi_\Lambda)f\|_{H^s}^2
&=
\sum_{\lambda_j>\Lambda}
(1+\lambda_j)^s|f_j|^2\\
&\leq
(1+\Lambda)^{-r}
\sum_{\lambda_j>\Lambda}
(1+\lambda_j)^{s+r}|f_j|^2.
\end{align*}
```
Taking square roots gives the claim. ◻

</div>

The theorem says exactly what is finite and what is limiting. At finite $`\Lambda`$, $`K_\Lambda`$ is the identity on the selected spectral subspace and suppresses its orthogonal complement. The full delta appears only as the subspaces exhaust $`L^2(X)`$. Nothing in this theorem selects a physical value of $`\Lambda`$.

# Heat kernels are smoothing, not projections

The heat semigroup gives another approximation to the identity:
``` math
e^{-\tau\Delta}f
=\sum_j e^{-\tau\lambda_j}
\langle\phi_j,f\rangle\phi_j,
\qquad \tau>0.
```
Its kernel is
``` math
H_\tau(x,y)
=\sum_j e^{-\tau\lambda_j}
\phi_j(x)\overline{\phi_j(y)}.
```

<div id="thm:heat" class="theorem">

**Theorem 4** (Heat-kernel approximate identity). *Under Assumption <a href="#ass:elliptic" data-reference-type="ref" data-reference="ass:elliptic">1</a>,
``` math
H_\tau\longrightarrow\delta_{\mathrm{diag}}
\quad\text{in }\mathcal D'(X\times X)
```
as $`\tau\downarrow0`$. Moreover, for $`0\leq r\leq2`$, $`s\in\mathbb R`$, and $`f\in H^{s+r}(X)`$,
``` math
\|(e^{-\tau\Delta}-I)f\|_{H^s}
\leq
\tau^{r/2}\|f\|_{H^{s+r}}.
```*

</div>

<div class="proof">

*Proof.* For $`u\geq0`$ and $`0\leq\alpha\leq1`$,
``` math
0\leq1-e^{-u}\leq u^\alpha.
```
Taking $`\alpha=r/2`$ gives
``` math
\begin{align*}
\|(e^{-\tau\Delta}-I)f\|_{H^s}^2
&=
\sum_j(1+\lambda_j)^s
|1-e^{-\tau\lambda_j}|^2|f_j|^2\\
&\leq
\tau^r
\sum_j(1+\lambda_j)^s\lambda_j^r|f_j|^2\\
&\leq
\tau^r\|f\|_{H^{s+r}}^2.
\end{align*}
```
The operator convergence on smooth functions and the Schwartz kernel theorem then give the distributional kernel limit. ◻

</div>

For small time and away from global complications, the familiar local asymptotic form is
``` math
H_\tau(x,y)
\sim
(4\pi\tau)^{-d/2}
\exp\!\left[-\frac{\mathop{\mathrm{dist}}(x,y)^2}{4\tau}\right]
\sum_{k\geq0}a_k(x,y)\tau^k.
```
This explains the finite-width appearance of the heat kernel. It must not be confused with spectral projection: $`e^{-\tau\Delta}`$ has weights strictly between zero and one on positive eigenspaces and is generally not idempotent. The two constructions approach the same identity distribution through different operator families.

# Normalized tubes around a constraint surface

A hard constraint
``` math
\delta(C(x))
```
is not generally an identity kernel. It localizes an integral to a level set and carries a geometric Jacobian.

Let
``` math
g_\epsilon(z)
=(2\pi\epsilon^2)^{-m/2}
\exp\!\left(-\frac{|z|^2}{2\epsilon^2}\right),
\qquad z\in\mathbb R^m.
```
The normalization is indispensable: $`\int_{\mathbb R^m}g_\epsilon(z)\,\mathrm{d}z=1`$.

<div id="thm:constraint-tube" class="theorem">

**Theorem 5** (Gaussian constraint-tube limit). *Let $`C:\mathbb R^n\to\mathbb R^m`$, $`m\leq n`$, be smooth, and let $`f\in C_c(\mathbb R^n)`$. Assume $`DC(x)`$ has rank $`m`$ on a neighborhood of $`\mathop{\mathrm{supp}}(f)`$. Define the normal Jacobian
``` math
\mathcal J_C(x)
=\sqrt{\det\!\bigl(DC(x)DC(x)^{\mathsf T}\bigr)}.
```
Then
``` math
\lim_{\epsilon\downarrow0}
\int_{\mathbb R^n}f(x)g_\epsilon(C(x))\,\mathrm{d}x
=
\int_{C^{-1}(0)}
\frac{f(x)}{\mathcal J_C(x)}
\,\mathrm{d}\mathcal H^{n-m}(x).
```*

</div>

<div class="proof">

*Proof.* The coarea formula gives
``` math
\int_{\mathbb R^n}f(x)g_\epsilon(C(x))\,\mathrm{d}x
=
\int_{\mathbb R^m}g_\epsilon(z)F(z)\,\mathrm{d}z,
```
where
``` math
F(z)
=
\int_{C^{-1}(z)}
\frac{f(x)}{\mathcal J_C(x)}
\,\mathrm{d}\mathcal H^{n-m}(x).
```
Because $`C`$ is a submersion near the compact support of $`f`$, local submersion coordinates and a finite partition of unity show that $`F`$ is continuous near $`z=0`$. It is compactly supported. The family $`\{g_\epsilon\}`$ is an approximate identity on $`\mathbb R^m`$, so the last integral converges to $`F(0)`$. ◻

</div>

This theorem gives a rigorous version of a finite admissibility tube. It also shows why writing only $`\exp[-|C|^2/(2\epsilon^2)]`$ is incomplete: without the Gaussian normalization, the integral generally tends to zero, and without the normal Jacobian the limiting surface measure is wrong.

The result is local in constraint geometry. If zero is not a regular value, the level set is singular and a different analysis is needed. If the configuration space is infinite-dimensional, neither Lebesgue measure nor the functional determinant follows from this finite-dimensional theorem.

# An exact projected commutator

The identity kernel enters canonical field commutators. There is one precise setting in which replacing the full identity by a projected kernel is exact.

<div id="thm:compressed-ccr" class="theorem">

**Theorem 6** (Compressed canonical commutation relation). *Let $`\mathcal H`$ be a complex one-particle Hilbert space, let $`\mathcal F_s(\mathcal H)`$ be its bosonic Fock space, and let $`P`$ be an orthogonal projection on $`\mathcal H`$. On the usual finite-particle domain,
``` math
[a(Pf),a^\dagger(Pg)]
=\langle Pf,Pg\rangle I
=\langle f,Pg\rangle I.
```
If $`P`$ is represented by a sufficiently regular integral kernel $`K_P`$, then
``` math
\langle f,Pg\rangle
=
\int_{X\times X}
\overline{f(x)}K_P(x,y)g(y)
\,\mathrm{d}V(x)\mathrm{d}V(y).
```*

</div>

<div class="proof">

*Proof.* The canonical commutation relation on $`\mathcal H`$ is
``` math
[a(u),a^\dagger(v)]=\langle u,v\rangle I.
```
Set $`u=Pf`$ and $`v=Pg`$. Since $`P=P^\ast=P^2`$,
``` math
\langle Pf,Pg\rangle=\langle f,Pg\rangle.
```
The kernel expression is the definition of $`P`$ as an integral operator. ◻

</div>

This is not a license to replace every $`\delta(x-y)`$ in a field theory by an arbitrary kernel. It says that if the theory is explicitly compressed to $`\mathrm{Ran}(P)`$, then the compressed creation and annihilation operators satisfy the projected relation. Dynamics, locality, covariance, positivity, and gauge symmetry must still be checked in the compressed model.

# Fixed points: concentration and finite spread

Fixed-point dynamics does not by itself force finite width. In fact, a deterministic attracting fixed point naturally produces a delta limit.

<div id="prop:fixed-point-delta" class="proposition">

**Proposition 7** (Pushforward toward a deterministic attractor). *Let $`S`$ be a metric space, $`T:S\to S`$ a measurable map, and $`x_\ast\in S`$. Suppose $`T^n x\to x_\ast`$ for every $`x`$ in a measurable basin $`B`$. If $`\mu`$ is a probability measure supported in $`B`$, then
``` math
(T^n)_\#\mu\Longrightarrow\delta_{x_\ast}
```
weakly.*

</div>

<div class="proof">

*Proof.* For every bounded continuous $`h:S\to\mathbb R`$,
``` math
\int_S h\,\mathrm{d}((T^n)_\#\mu)
=
\int_B h(T^n x)\,\mathrm{d}\mu(x)
\longrightarrow
h(x_\ast)
```
by bounded convergence. ◻

</div>

The width of the basin is irrelevant to this conclusion. If there are several attracting basins, an initial ensemble can instead converge to a mixture of point masses, with weights inherited from the initial measure. Neither case selects a unique realized history from the limiting ensemble.

A nonzero stationary spread requires another ingredient. For example, the declared stochastic equation
``` math
\mathrm{d}X_t=-\gamma X_t\,\mathrm{d}t+\sqrt{2D}\,\mathrm{d}W_t
```
has stationary variance $`D/\gamma`$ when $`\gamma,D>0`$. That variance comes from the balance between damping and continuing disturbance. It does not follow from the fixed point or spectral gap alone, and it is not automatically a detector width, coherence length, or MTT-selected constant. Finite-memory driving changes the response again and must be analyzed in the declared colored-noise model.

# Gauge fixing: what the Jacobian argument proves

The Faddeev–Popov construction is often written schematically as
``` math
1=
\int_{\mathcal G}
\delta\!\bigl(F(A^g)\bigr)
\det M_F(A^g)\,\mathrm{d}g.
```
Its finite-dimensional local content is a change-of-variables statement. Let a Lie group $`G`$ of dimension $`m`$ act smoothly on a configuration manifold $`\mathcal A`$, and let $`F:\mathcal A\to\mathbb R^m`$ be a gauge condition. For fixed $`A`$, consider the orbit map
``` math
\Phi_A(g)=F(g\cdot A).
```
If $`D_e\Phi_A`$ is invertible and the chosen neighborhood contains exactly one root of $`\Phi_A`$, then the inverse function theorem and the ordinary delta change-of-variables formula give a local identity of the form
``` math
\int_G
\delta\!\bigl(\Phi_A(g)\bigr)
\left|\det D_g\Phi_A\right|
\,\mathrm{d}g
=1.
```
The determinant is the orbit-to-slice Jacobian. The normalized Gaussian tube from Theorem <a href="#thm:constraint-tube" data-reference-type="ref" data-reference="thm:constraint-tube">5</a> supplies a finite local approximation to the slice constraint.

This local model explains the geometry but does not settle global gauge fixing. In non-Abelian theories, one gauge condition can meet an orbit more than once; these Gribov copies invalidate a naive global one-root identity . Infinite-dimensional path-integral measures and determinants also require regularization. Ghost fields are a representation of the determinant in the perturbative functional formalism, not proof that a selected MTT kernel has supplied a global quotient.

# Measurement: a physical process with distinct layers

For position on $`L^2(\mathbb R^d)`$, the sharp observable is the projection-valued measure
``` math
(Q(B)\psi)(x)=\mathbf 1_B(x)\psi(x).
```
The notation
``` math
Q(\mathrm{d}x)=|x\rangle\langle x|\,\mathrm{d}x
```
uses a distributional density. The generalized $`|x\rangle`$ is not a vector in $`L^2`$, but every $`Q(B)`$ is a bounded projection.

A normalized detector response $`g_\epsilon`$ produces the smeared POVM
``` math
E_\epsilon(B)
=
\int_{\mathbb R^d}
\left(\int_B g_\epsilon(y-x)\,\mathrm{d}y\right)Q(\mathrm{d}x).
```
For a state $`\psi`$, the outcome density is
``` math
p_\epsilon=g_\epsilon*|\psi|^2.
```
Normalized approximate identities give
``` math
\|p_\epsilon-|\psi|^2\|_{L^1}\longrightarrow0,
```
and the companion finite-resolution measurement paper proves a quantitative $`W^{1,1}`$ bound and constructs one compatible square-root instrument.

This example is a genuine finite-kernel bridge, but measurement contains more than the POVM. The physical coupling, conditional state update, completion into one outcome-bearing record, and later stabilization are distinct layers. A detector-smearing theorem does not select one history. Conversely, a discrete finite-dimensional PVM can be an ordinary bounded operator family with no Dirac distribution at all .

# Point sources, contacts, and conservation laws

## Point sources

An equation such as
``` math
Lu=\delta_{x_0}
```
defines a Green function or an ideal point-source response. Replacing the source by a normalized profile $`\rho_\epsilon`$ may be physically appropriate when the source has finite extent:
``` math
Lu_\epsilon=\rho_\epsilon,
\qquad
\rho_\epsilon\longrightarrow\delta_{x_0}.
```
That is a source regularization, not necessarily a projection. The theory must specify whether the point source is an exact mathematical probe, an effective limit, or a claim about a physical emitter.

## Contact interactions

A contact term such as $`\delta(x-y)`$ idealizes a zero-range interaction. Finite-range potentials can converge to contact models in declared scaling limits, but the coupling may need dimension-dependent renormalization and the operator domain can change. Merely substituting a smooth kernel does not prove equivalence to the original contact theory.

## Momentum conservation

Translation invariance gives the exact tempered-distribution identity
``` math
\int_{\mathbb R^d}e^{iq\cdot x}\,\mathrm{d}x
=(2\pi)^d\delta(q).
```
Here the delta expresses exact Fourier orthogonality and conservation in an infinite translation-invariant model. It is not evidence by itself for a finite survivor basin.

If the interaction is restricted to a finite spacetime window $`W`$, the factor becomes
``` math
\widehat{\mathbf 1_W}(q)
=
\int_W e^{iq\cdot x}\,\mathrm{d}x.
```
For rectangular windows this is a product of sinc profiles, and expanding windows recover the conservation delta distributionally. The finite profile therefore follows from a changed finite-window model. Whether the physical system selects such a window is a separate question.

# Finite kernels do not automatically renormalize a theory

A smoothing or finite-rank kernel can suppress high-frequency modes. It may therefore be useful as a regulator or as the exact observable algebra of a finite projected model. That observation is weaker than ultraviolet completion.

An admissible replacement must address at least:

1.  whether the kernel is selected or fitted;

2.  whether gauge and Ward identities are preserved;

3.  whether Lorentz covariance, causality, and unitarity survive;

4.  whether the finite theory matches observed low-energy amplitudes;

5.  whether the cutoff can be removed, or instead belongs to the exact physical model; and

6.  whether regulator dependence is controlled.

Renormalization is not generally a repair of “over-sharp projection.” It is a structured relation between bare descriptions, observables, scales, and counterterms. A finite spectral algebra can make traces exact at its declared cutoff, but connecting that algebra to a continuum QFT remains an additional theorem.

# The MTT finite-kernel diagnostic

The results above support a disciplined diagnostic rather than a universal replacement rule.

<div class="definition">

**Definition 8** (Finite-kernel diagnostic). For a downstream occurrence of a Dirac delta, the MTT finite-kernel diagnostic asks:

1.  Which mathematical role does the delta play?

2.  Is there a finite projector, semigroup kernel, source profile, detector response, constraint tube, or spacetime window appropriate to that role?

3.  Which selected upstream object emits that finite representative?

4.  In which topology does the representative converge to the delta?

5.  What quantitative error certificate is available?

6.  Which symmetries and operator identities survive at finite resolution?

</div>

This formulation is compatible with the projection-first program. The common circle, lens filtration, nil/shear data, fixed-point maps, and finite q79 operators may help select particular finite objects. But those geometric ingredients do not become a source theorem merely because a Gaussian or spectral cutoff can be written down.

## What the present mathematics already supplies

The current paper establishes four exact bridges:

1.  finite spectral projectors converge to the diagonal identity distribution with a Sobolev error;

2.  heat kernels converge through a distinct smoothing family with a Sobolev error;

3.  normalized Gaussian constraint tubes converge to the coarea-weighted surface distribution; and

4.  compression to a declared one-particle subspace gives an exact projected canonical commutator.

These are reusable interfaces. A later MTT source theorem can point to one of them and provide the missing finite object and scale without reproving the analytic bridge.

## What remains open

The selected MTT carrier has not yet been shown here to emit:

1.  a universal spectral threshold $`\Lambda`$ or heat time $`\tau`$;

2.  a detector response for arbitrary apparatus contexts;

3.  a global non-Abelian gauge slice free of copy ambiguities;

4.  a symmetry-preserving finite kernel for every QFT sector; or

5.  a one-history completion law.

The circle–lens–nil interpretation can organize candidate sources, but the assignment of individual delta roles to those layers remains a research proposal. In particular, there is no theorem here identifying a compact phase circle with physical time or deriving a physical resolution scale from a spectral gap.

# Status ledger

<div class="center">

| Status | Result |
|:---|:---|
| Exact | The diagonal delta is the Schwartz kernel of the identity |
| Exact | Spectral projector kernels converge distributionally to the diagonal delta |
| Exact | Spectral truncation has the stated $`H^{s+r}\to H^s`$ error |
| Exact | Heat kernels form a nonprojective approximate identity with the stated error |
| Exact | Normalized Gaussian constraint tubes converge by the coarea formula |
| Exact | Orthogonal compression gives the projected CCR kernel |
| Exact | A deterministic attracting fixed point can concentrate an ensemble to a delta |
| Standard input | Detector POVMs, local Faddeev–Popov formalism, and distributional Fourier conservation |
| Conditional | Replacing a physical sharp object by a finite source, detector, window, or kernel |
| Open | Selected MTT scales, global gauge fixing, general instrument source, one-history completion, and ultraviolet completion |

</div>

# Conclusion

Dirac deltas are not all shadows of one hidden process. Their shared distributional notation conceals several operator, source, constraint, symmetry, and measurement roles. Once those roles are separated, a useful projection-first insight survives in a rigorous form.

Spectral projector kernels and heat kernels both approach the identity distribution, but one family is projective and the other is smoothing. Normalized Gaussian tubes approach regular constraint surfaces with the coarea Jacobian. Compressed field operators obey an exact projected commutator. Finite detector responses and finite spacetime windows provide further role-specific approximations.

For MTT, the productive question is therefore not “which projection is every delta hiding?” It is “which finite object does the selected geometry emit for this role, and what proves the sharp limit without losing the required physics?” The analytic interfaces are now explicit. Selecting their physical inputs remains the frontier.

<div class="thebibliography">

99

N. Berline, E. Getzler, and M. Vergne, *Heat Kernels and Dirac Operators*, Springer, Berlin, 1992, doi:10.1007/978-3-642-58088-8.

E. B. Davies and J. T. Lewis, *An Operational Approach to Quantum Probability*, Communications in Mathematical Physics **17** (1970) 239–260, doi:10.1007/BF01647093.

L. C. Evans and R. F. Gariepy, *Measure Theory and Fine Properties of Functions*, revised edition, CRC Press, Boca Raton, 2015, doi:10.1201/b18333.

L. D. Faddeev and V. N. Popov, *Feynman Diagrams for the Yang–Mills Field*, Physics Letters B **25** (1967) 29–30, doi:10.1016/0370-2693(67)90067-6.

V. N. Gribov, *Quantization of Non-Abelian Gauge Theories*, Nuclear Physics B **139** (1978) 1–19, doi:10.1016/0550-3213(78)90175-X.

A. S. Holevo, *Statistical Structure of Quantum Theory*, Lecture Notes in Physics Monographs, vol. 67, Springer, Berlin, 2001, doi:10.1007/3-540-44998-1.

</div>
