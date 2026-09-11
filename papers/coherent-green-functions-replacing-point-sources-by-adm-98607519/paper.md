---
abstract: |
  The preceding paper identified Dirac delta functions as singular shadows of admissible projection: a delta is the zero-width limit of a bounded coherent projection kernel. The present paper develops the first worked sequel. We replace the standard point-source Green equation
  ``` math
  LG(x,y)=\delta(x-y)
  ```
  by the coherent Green equation
  ``` math
  LG_{\mathrm{coh}}(x,y)=K_{\mathrm{coh}}(x,y),
  ```
  where $`K_{\mathrm{coh}}`$ is a bounded admissible identity kernel on a retained coherent sector. The mathematical core is elementary but important: for a positive self-adjoint elliptic operator $`L`$, finite spectral projectors and heat-kernel filters produce smooth finite-width sources, smooth responses, finite diagonal values, and distributional convergence to the ordinary Green kernel only in the singular limit. A worked circle model with $`L_m=-\partial_\theta^2+m^2`$ displays the replacement explicitly: $`L_mG_N=K_N`$ and $`L_mG_\tau=H_\tau`$, with the point-source equation recovered only as $`N\to\infty`$ or $`\tau\downarrow0`$. Thus the standard Green function is recovered, but as an ideal endpoint rather than a primitive object.

  Within Modal Triplet Theory (MTT), these theorems provide a conditional downstream interface rather than a universal replacement rule. A selected physical realization must still supply $`L`$, the projector or filter, its width, and the map from an internal or Euclidean spectral problem to the claimed external source. It must also prove that covariance, gauge constraints, locality or causal support, and boundary conditions survive. Different finite kernels can share the same sharp limit while giving different finite predictions. The rigorous result is therefore the elliptic response theorem and its singular limit; physical kernel selection remains open.
author:
- Peter Nero
current_version: v2
date: September 2026, Version 2
generated_from_main_tex_sha256: f12bec1462e36962fa0f73f6c6bf0f13e8f2cb400d6f5a5a2a22cac1e81313c1
paper_id: coherent-green-functions-replacing-point-sources-by-adm-98607519
release_state: current_revised_tex
released_version: v1
title: |
  Coherent Green Functions from Declared Projection Kernels
  Elliptic Results and the MTT Source Boundary
zenodo_doi: 10.5281/zenodo.21703915
zenodo_record_id: 21703915
zenodo_url: "https://zenodo.org/records/21703915"
---

# Version 2 Revision Note

Supersedes
Version 1. The previous release remains public until a new release is approved.

Reason
Correct boundary-domain and Sobolev-norm claims for Green responses.

Resolution
Repairs both convergence theorems and distinguishes spectral from geometric Sobolev norms.

Retained result
Correctly scoped results and explanatory examples remain; no physical source-selection claim is promoted.

Remaining boundary
Realization hypotheses and physical source or apparatus bridges remain separate obligations. This is an unreleased authoring revision.

# Version 1 Revision Note

Supersedes
The unversioned manuscript *Coherent Green Functions: Replacing Point Sources by Admissible Kernels in Modal Triplet Theory*.

Reason
The earlier text correctly proved spectral and heat-kernel limits but treated a declared finite kernel as physically selected and extended compact elliptic conclusions to point particles, retarded propagators, contact interactions, and renormalization without the necessary source and symmetry theorems.

Resolution
This version retains the spectral mathematics, types the result as an elliptic or Euclidean construction, distinguishes a sector identity from the full identity, and makes covariance, gauge, locality, causal-support, and boundary compatibility explicit gates.

Retained result
For a supplied positive self-adjoint elliptic $`L`$, finite spectral and heat-filtered Green operators are smooth finite-source responses and converge distributionally to the ordinary Green kernel in the sharp limit.

Remaining boundary
No theorem here selects the finite kernel or its width from MTT geometry, and the hyperbolic, gauge, and interacting extensions remain separate constructions.

# Purpose and claim discipline

The previous paper established the following structural thesis:
``` math
\delta(x-y)=\text{singular limit of coherent projection kernels}.
```
The present paper asks for the first concrete physical construction that follows from that thesis.

The natural starting point is the Green equation. In standard continuum physics, the response of a linear operator $`L`$ to a point source is encoded by
``` math
\begin{equation}
LG(x,y)=\delta(x-y).
\end{equation}
```
This formula is mathematically powerful, but it builds in an idealization: the source has zero spatial width and exact point support.

The MTT replacement is:
``` math
\begin{equation}
LG_{\mathrm{coh}}(x,y)=K_{\mathrm{coh}}(x,y),
\end{equation}
```
where $`K_{\mathrm{coh}}`$ is the kernel of a bounded coherent projection or admissibility filter.

## Non-claims

This paper does not claim that ordinary Green functions are wrong. It does not claim that all point-source methods should be abandoned. It does not compute numerical finite-width corrections for a specific experimental system, select a physical kernel from MTT geometry, or derive a Lorentzian retarded replacement from the compact elliptic calculation. Its narrower claim is:

<div class="center">

</div>

This is proved in standard spectral settings and then interpreted inside MTT.

# Standard Green functions and the hidden delta

Let $`X`$ be a compact smooth Riemannian manifold without boundary, or a compact domain with self-adjoint elliptic boundary conditions. Let $`L`$ be a positive self-adjoint elliptic operator of order two on $`L^2(X)`$. For concreteness one may take
``` math
L=\Delta+m^2,\qquad m^2>0,
```
where $`\Delta\ge 0`$ is the nonnegative Laplacian.

Let $`\{ \phi_n\}_{n=0}^\infty`$ be an orthonormal eigenbasis:
``` math
L\phi_n=\mu_n\phi_n,\qquad 0<\mu_0\le \mu_1\le\cdots,\qquad \mu_n\to\infty.
```
The standard Green kernel is formally
``` math
\begin{equation}
G(x,y)=\sum_{n=0}^\infty \frac{\phi_n(x)\phi_n^*(y)}{\mu_n}.
\end{equation}
```
It satisfies
``` math
\begin{equation}
L_xG(x,y)=\delta(x-y)
\end{equation}
```
in the distributional sense.

The key point is that the singularity of $`G`$ is not only a property of $`L^{-1}`$. It is also a property of the source:
``` math
\delta(x-y).
```
If the source is replaced by a finite-width kernel, the response is correspondingly regularized.

# Coherent source kernels

<div class="definition">

**Definition 1** (Spectral coherent source kernel). For $`\Lambda>0`$, define the spectral projector
``` math
\Pi_\Lambda f=\sum_{\mu_n\le \Lambda}\langle \phi_n,f\rangle\phi_n.
```
Its kernel is
``` math
\begin{equation}
K_\Lambda(x,y)=\sum_{\mu_n\le \Lambda}\phi_n(x)\phi_n^*(y).
\end{equation}
```

</div>

For finite $`\Lambda`$, $`K_\Lambda`$ is a finite-rank smooth kernel. It is not the full identity kernel on $`L^2(X)`$. It is the identity kernel only on the retained spectral subspace
``` math
\operatorname{Ran}\Pi_\Lambda.
```

<div class="definition">

**Definition 2** (Heat coherent source kernel). For $`\tau>0`$, define the heat kernel of $`\Delta`$ by
``` math
H_\tau(x,y)=\sum_{n=0}^\infty e^{-\tau \lambda_n}\phi_n(x)\phi_n^*(y),
```
where $`\Delta\phi_n=\lambda_n\phi_n`$. This is a positive smoothing approximate identity.

</div>

The sharp spectral kernel $`K_\Lambda`$ and the heat kernel $`H_\tau`$ play different roles:
``` math
K_\Lambda=\text{band-limited identity kernel},
```
while
``` math
H_\tau=\text{positive smoothing identity kernel}.
```
Both converge to $`\delta(x-y)`$ in a singular limit, but only $`H_\tau`$ is automatically positive and smoothing in the probabilistic sense.

# Coherent Green functions

<div class="definition">

**Definition 3** (Spectral coherent Green function). The spectral coherent Green function is
``` math
\begin{equation}
G_\Lambda(x,y):=(L^{-1}\Pi_\Lambda)(x,y)
=\sum_{\mu_n\le \Lambda}\frac{\phi_n(x)\phi_n^*(y)}{\mu_n}.
\end{equation}
```

</div>

It satisfies the finite-source equation
``` math
\begin{equation}
L_xG_\Lambda(x,y)=K_\Lambda(x,y).
\end{equation}
```

<div class="definition">

**Definition 4** (Heat coherent Green function). For a heat source $`H_\tau`$, define
``` math
\begin{equation}
G_\tau(x,y):=(L^{-1}H_\tau)(x,y).
\end{equation}
```
If $`L=\Delta+m^2`$ and $`H_\tau=e^{-\tau\Delta}`$, then
``` math
\begin{equation}
G_\tau = L^{-1}e^{-\tau\Delta}.
\end{equation}
```
It satisfies
``` math
\begin{equation}
L_xG_\tau(x,y)=H_\tau(x,y).
\end{equation}
```

</div>

# Main theorem: coherent Green functions converge to the point-source Green function

<div class="theorem">

**Theorem 5** (Spectral coherent Green convergence). *Let $`L`$ be a positive self-adjoint elliptic operator of order two on a compact smooth domain as above. Let $`G_\Lambda=L^{-1}\Pi_\Lambda`$. Then:*

1.  *For each finite $`\Lambda`$, $`G_\Lambda(x,y)`$ is smooth on $`X\times X`$.*

2.  *$`L_xG_\Lambda(x,y)=K_\Lambda(x,y)`$.*

3.  *As $`\Lambda\to\infty`$, $`G_\Lambda\to G=L^{-1}`$ in the distributional kernel sense.*

4.  *For every $`f\in D_\infty(L):=\bigcap_{m\ge0}\operatorname{Dom}(L^m)`$,
    ``` math
    G_\Lambda f:=\int_XG_\Lambda(x,y)f(y)\,dy
    \longrightarrow
    Gf:=L^{-1}f
    ```
    in $`C^\infty(X)`$. On a closed manifold this includes every smooth input. With boundary, all powers of the selected elliptic realization impose compatibility; arbitrary smooth boundary data are not included. For every $`f\in L^2(X)`$, convergence still holds in $`L^2`$.*

</div>

<div class="proof">

*Proof.* Because $`L`$ is positive, self-adjoint, elliptic, and defined on a compact domain with self-adjoint boundary conditions, it has a complete orthonormal eigenbasis $`\{\phi_n\}`$ with eigenvalues $`\mu_n\to\infty`$. The finite spectral sum defining $`G_\Lambda`$ is smooth, proving (1).

Applying $`L_x`$ termwise gives
``` math
L_xG_\Lambda(x,y)
=
\sum_{\mu_n\le\Lambda}\phi_n(x)\phi_n^*(y)
=
K_\Lambda(x,y),
```
proving (2).

Let $`f=\sum f_n\phi_n`$. Then
``` math
G_\Lambda f=\sum_{\mu_n\le\Lambda}\frac{f_n}{\mu_n}\phi_n,
\qquad
Gf=\sum_{n=0}^\infty\frac{f_n}{\mu_n}\phi_n.
```
For $`s\ge0`$, define the spectral graph norm $`\|h\|_{\mathcal H_L^s}:=\|(I+L)^{s/2}h\|_2`$. Then exactly
``` math
\left\lVert Gf-G_\Lambda f \right\rVert_{\mathcal H_L^s}^2
=
\sum_{\mu_n>\Lambda}(1+\mu_n)^s \frac{|f_n|^2}{\mu_n^2}.
```
For $`f\in D_\infty(L)`$ this tail tends to zero at every order. Geometric Sobolev norms are compared by elliptic estimates; they are not identically the displayed spectral norm. Sobolev embedding gives the smooth limit. For general $`L^2`$ input use $`s=0`$ and boundedness of $`L^{-1}`$. The distributional kernel limit follows by testing against smoothing trace-class operators. This is the Green-response specialization of the joint sharp-limit theorem in , not an equivalence between smooth and distributional convergence. ◻

</div>

<div class="corollary">

**Corollary 6** (Coherent Green functions are regularized point-source responses). *For finite $`\Lambda`$, the equation
``` math
LG_\Lambda=K_\Lambda
```
is a smooth finite-source response. The ordinary point-source equation
``` math
LG=\delta
```
is recovered only in the singular limit $`\Lambda\to\infty`$.*

</div>

# Heat-kernel version

The spectral cutoff theorem is useful because it directly matches finite coherent subspaces. The heat-kernel version is often physically cleaner because the source is positive and localized.

<div class="theorem">

**Theorem 7** (Heat coherent Green convergence). *Let $`L=\Delta+m^2`$ with $`m^2>0`$ on a compact Riemannian manifold or compact domain with self-adjoint boundary conditions. Define
``` math
G_\tau=L^{-1}e^{-\tau\Delta}.
```
Then:*

1.  *$`G_\tau(x,y)`$ is smooth for every $`\tau>0`$;*

2.  *$`L_xG_\tau(x,y)=H_\tau(x,y)`$;*

3.  *as $`\tau\downarrow0`$, $`G_\tau\to G=L^{-1}`$ distributionally;*

4.  *for every $`f\in D_\infty(\Delta)`$, $`G_\tau f\to Gf`$ in $`C^\infty(X)`$; for every $`L^2`$ input, convergence holds in $`L^2`$. The all-powers domain uses the same boundary realization for $`\Delta`$ and $`L=\Delta+m^2`$.*

</div>

<div class="proof">

*Proof.* Since $`e^{-\tau\Delta}`$ is smoothing for $`\tau>0`$, $`G_\tau=L^{-1}e^{-\tau\Delta}`$ has a smooth kernel. The identity $`L_xG_\tau=H_\tau`$ follows from applying $`L`$ to $`L^{-1}H_\tau`$.

In the eigenbasis of $`\Delta`$, one has
``` math
G_\tau f=\sum_{n=0}^\infty \frac{e^{-\tau\lambda_n}}{\lambda_n+m^2} f_n\phi_n,
\qquad
Gf=\sum_{n=0}^\infty \frac{1}{\lambda_n+m^2} f_n\phi_n.
```
For $`f\in D_\infty(\Delta)`$, dominated convergence in each spectral graph norm followed by elliptic Sobolev comparison proves the smooth limit. The order-zero estimate proves the general $`L^2`$ limit and trace-class testing proves the distributional kernel assertion. ◻

</div>

# Finite diagonal values and coincidence singularities

One of the main reasons point-source Green functions create difficulties in QFT and classical field theory is the diagonal limit $`G(x,x)`$. For a genuine point-source Green function, this is often singular. For coherent Green functions it is finite.

<div class="proposition">

**Proposition 8** (Finite diagonal for finite spectral response). *For finite $`\Lambda`$,
``` math
\begin{equation}
G_\Lambda(x,x)=\sum_{\mu_n\le\Lambda}\frac{|\phi_n(x)|^2}{\mu_n}
\end{equation}
```
is finite for every $`x\in X`$.*

</div>

<div class="proof">

*Proof.* The sum contains only finitely many smooth terms. ◻

</div>

<div class="remark">

*Remark 9*. As $`\Lambda\to\infty`$, this diagonal may diverge depending on the dimension and the operator. The divergence is not mysterious in the present framework: it is the cost of driving a finite coherent response toward a zero-width point source.

</div>

This gives a precise version of the renormalization intuition introduced in the preceding paper:

<div class="center">

</div>

# Worked model on the circle

We now give an explicit model in which all objects can be written down. This section is not needed for the general theorem, but it makes the replacement rule concrete.

Let
``` math
X=S^1=\mathbb R/2\pi\mathbb Z
```
with coordinate $`\theta`$, and let
``` math
L_m=-\frac{d^2}{d\theta^2}+m^2,
\qquad m>0.
```
The normalized Fourier modes are
``` math
e_n(\theta)=\frac{1}{\sqrt{2\pi}}e^{in\theta},
\qquad n\in\mathbb Z,
```
and
``` math
L_m e_n=(n^2+m^2)e_n.
```

## Band-limited source kernel

For $`N\in\mathbb N`$, define the finite spectral projector
``` math
\Pi_N f=\sum_{|n|\le N}\langle e_n,f\rangle e_n.
```
Its kernel is the Dirichlet spectral kernel
``` math
K_N(\theta,\eta)
=
\frac{1}{2\pi}\sum_{|n|\le N}e^{in(\theta-\eta)}
=
\frac{\sin((N+\frac12)(\theta-\eta))}{2\pi\sin((\theta-\eta)/2)}
```
away from $`\theta=\eta`$, with the removable diagonal value
``` math
K_N(\theta,\theta)=\frac{2N+1}{2\pi}.
```
The ordinary identity kernel on $`S^1`$ is recovered only distributionally:
``` math
K_N(\theta,\eta)\to \delta(\theta-\eta)
```
as $`N\to\infty`$.

The associated coherent Green kernel is
``` math
G_N(\theta,\eta)
=
L_m^{-1}K_N(\theta,\eta)
=
\frac{1}{2\pi}\sum_{|n|\le N}
\frac{e^{in(\theta-\eta)}}{n^2+m^2}.
```
It satisfies the exact finite-source equation
``` math
L_mG_N(\theta,\eta)=K_N(\theta,\eta).
```
Thus $`G_N`$ is the response to a band-limited source, not to a point source.

## Limit to the ordinary Green function

The ordinary periodic massive Green kernel is
``` math
G(\theta,\eta)
=
\frac{1}{2\pi}\sum_{n\in\mathbb Z}
\frac{e^{in(\theta-\eta)}}{n^2+m^2}.
```
Equivalently, writing
``` math
r=d_{S^1}(\theta,\eta)\in[0,\pi],
```
one has
``` math
G(\theta,\eta)
=
\frac{\cosh(m(\pi-r))}{2m\sinh(\pi m)}.
```
The finite kernels converge to the ordinary Green kernel:
``` math
G_N(\theta,\eta)\to G(\theta,\eta)
```
uniformly in $`(\theta,\eta)`$, and distributionally after applying $`L_m`$:
``` math
L_mG_N=K_N\to\delta.
```

This gives a precise interpretation:
``` math
\boxed{
\text{point-source Green response}
=
\text{limit of band-limited coherent Green responses}.
}
```

## Heat-filtered positive source

The sharp spectral cutoff $`K_N`$ is finite-rank and smooth, but it is not positive and has oscillatory side-lobes. A smoother positive approximate identity is obtained from the heat kernel:
``` math
H_\tau(\theta,\eta)
=
\frac{1}{2\pi}\sum_{n\in\mathbb Z}e^{-\tau n^2}e^{in(\theta-\eta)},
\qquad \tau>0.
```
The corresponding heat-filtered Green kernel is
``` math
G_\tau(\theta,\eta)
=
\frac{1}{2\pi}\sum_{n\in\mathbb Z}
\frac{e^{-\tau n^2}e^{in(\theta-\eta)}}{n^2+m^2}.
```
It satisfies
``` math
L_mG_\tau(\theta,\eta)=H_\tau(\theta,\eta),
```
and
``` math
H_\tau\to\delta,
\qquad
G_\tau\to G
```
as $`\tau\downarrow0`$.

This explicitly displays the two versions of the replacement:
``` math
\delta
\quad\leadsto\quad
K_N
```
for a band-limited sector identity, and
``` math
\delta
\quad\leadsto\quad
H_\tau
```
for a positive finite-width source.

## What the example shows

The $`S^1`$ model illustrates the central claim in a completely explicit setting:
``` math
LG=\delta
```
is the singular endpoint of the family
``` math
LG_N=K_N
```
or
``` math
LG_\tau=H_\tau.
```

The finite kernels are not approximations in a vague philosophical sense. They are exact Green responses to exact finite-resolution sources. The usual point-source equation is recovered only after taking the singular limit.

In one dimension the massive Green function itself has a finite diagonal value, so this example should not be used as a model of coincident-point ultraviolet divergence. Its role is narrower and cleaner: it shows explicitly how the point source is replaced by a coherent finite source, and how the ordinary delta source is recovered as a limit. In higher dimensions, the same replacement also regularizes diagonal singularities before the limit is taken.

# MTT interpretation and source boundary

Within MTT, the coherent projector $`\Pi_{\mathrm{coh}}`$ is not normally an increasing full-space spectral cutoff. It is a sector projector: it selects the admissible coherent sector determined by the fixed-point regime, spectral gap, and admissibility conditions.

Thus $`K_{\mathrm{coh}}`$ should not be confused with a literal approximation to the identity on all of $`L^2(X)`$. It is an identity kernel only inside the retained coherent sector. Moreover, calling that sector physical requires a selected operator, projector, boundary condition, and intertwiner from the relevant MTT carrier.

<div class="definition">

**Definition 10** (MTT coherent Green equation). Given a coherent sector with projection kernel $`K_{\mathrm{coh}}`$, the MTT coherent Green function is defined by
``` math
\begin{equation}
LG_{\mathrm{coh}}(x,y)=K_{\mathrm{coh}}(x,y),
\end{equation}
```
or equivalently
``` math
\begin{equation}
G_{\mathrm{coh}}=L^{-1}\Pi_{\mathrm{coh}}
\end{equation}
```
whenever $`L^{-1}`$ is defined on the sector under consideration.

</div>

The ordinary point-source Green function is recovered only if one takes a family whose retained sectors exhaust the full domain and whose width tends to zero:
``` math
K_{\mathrm{coh}}(x,y)\leadsto \delta(x-y).
```

<div class="remark">

*Remark 11* (Sector identity versus full identity). The distinction is crucial. A coherent projector may erase many upstream distinctions and still act as the identity on the retained effective variables. Thus $`K_{\mathrm{coh}}`$ is not “almost the identity” on the full upstream space. It is the exact or approximate identity on the downstream admissible sector.

</div>

<div class="remark">

*Remark 12* (Physical compatibility gates). Even when $`K_{\mathrm{coh}}`$ is fixed mathematically, a physical substitution must preserve the structures used by the target theory. For a scalar elliptic problem these include covariance and boundary conditions. For gauge fields they also include the constraint complex and Ward or BRST identities. For Lorentzian propagation they include causal support and wavefront-set conditions. None of these follows from smoothness of the elliptic kernel alone.

</div>

# Point particles, point charges, and finite source kernels

A point particle or point charge is usually encoded as
``` math
\rho(x)=q\delta(x-x_0).
```
The coherent replacement is
``` math
\rho_{\mathrm{coh}}(x)=qK_{\mathrm{coh}}(x,x_0),
```
or, in the heat-kernel model,
``` math
\rho_\tau(x)=qH_\tau(x,x_0).
```

The field equation becomes
``` math
L\varphi_{\mathrm{coh}}=\rho_{\mathrm{coh}},
```
with solution
``` math
\varphi_{\mathrm{coh}}(x)=qG_{\mathrm{coh}}(x,x_0).
```

In the heat model:
``` math
\varphi_\tau(x)=qG_\tau(x,x_0).
```
As $`\tau\downarrow0`$, this converges to the standard point-source potential.

# Contact interactions as coherent overlaps

A local contact interaction is often modeled by a zero-range kernel:
``` math
V(x,y)=g\delta(x-y).
```
The coherent replacement is
``` math
V_{\mathrm{coh}}(x,y)=gK_{\mathrm{coh}}(x,y).
```
For a quartic field interaction, the point-local expression
``` math
\lambda\phi^4(x)
```
can be replaced by an overlap vertex
``` math
\lambda\int_{X^4}V_{\mathrm{coh}}(x_1,x_2,x_3,x_4)
\phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4)\,dx_1\cdots dx_4,
```
where a simple coherent model is
``` math
V_{\mathrm{coh}}(x_1,x_2,x_3,x_4)
=
\int_X K_{\mathrm{coh}}(z,x_1)K_{\mathrm{coh}}(z,x_2)
K_{\mathrm{coh}}(z,x_3)K_{\mathrm{coh}}(z,x_4)\,dz.
```

This is the vertex-level analogue of the Green-function replacement:
``` math
\delta \leadsto K_{\mathrm{coh}}.
```

# Retarded and causal Green functions

The preceding sections used elliptic Green functions because the spectral theory is clean. Hyperbolic propagation requires causal support. The corresponding replacement is not
``` math
G_{\mathrm{ret}}\delta
```
as a point impulse, but a finite-source retarded response:
``` math
L G_{\mathrm{ret,coh}} = K_{\mathrm{coh}}
```
with support controlled by the causal propagation of the finite source.

A basic model is
``` math
G_{\mathrm{ret,coh}} = G_{\mathrm{ret}}\circ \Pi_{\mathrm{coh}}.
```
If $`G_{\mathrm{ret}}`$ has future-lightcone support and $`\Pi_{\mathrm{coh}}`$ is spatial/internal on a fixed time slab, the causal response is the retarded propagation of an admissible source rather than an acausal point impulse.

<div class="remark">

*Remark 13* (Scope). A fully rigorous hyperbolic version requires specifying the spacetime function spaces, wavefront-set control, and causal support assumptions. This paper only records the structural replacement. The elliptic and heat-kernel theorems above are the rigorous core.

</div>

# Diagnostics and finite-width effects

The coherent Green-function replacement suggests several concrete diagnostics.

1.  **Finite-source models.** A supplied extended preparation or source can be represented by a finite kernel; point-source physics is not universally replaced.

2.  **Finite diagonal response.** Coincident-point quantities are finite before the delta limit is taken.

3.  **Modified contact scattering.** A declared nonlocal EFT interaction can acquire form factors determined by $`K_{\mathrm{coh}}`$; this is not implied by the free Green equation.

4.  **Resolution-dependent propagators.** Propagators become $`L^{-1}\Pi_{\mathrm{coh}}`$, not $`L^{-1}`$ on all modes.

5.  **Renormalization question.** A finite filter may soften selected integrals, but renormalization, Ward identities, reflection positivity, and Lorentzian unitarity require independent analysis.

# Relation to the delta/projection paper

The preceding paper established the general diagnostic:
``` math
\text{find the delta} \quad\Rightarrow\quad \text{identify the hidden projection}.
```
The present paper executes the first instance:
``` math
LG=\delta
\quad\Rightarrow\quad
LG_{\mathrm{coh}}=K_{\mathrm{coh}}.
```

Thus the Green function is not abandoned. It is reclassified:
``` math
\boxed{
\text{ordinary Green function}=\text{singular limit of coherent finite-source response}.
}
```

# Conclusion

The Dirac delta enters Green-function theory as the ideal point source. A declared finite kernel gives a legitimate alternative source model and a controlled sharp limit. The mathematics alone does not decide which source is physically realized.

The rigorous theorem is simple: finite spectral Green functions $`G_\Lambda=L^{-1}\Pi_\Lambda`$ and heat-filtered Green functions $`G_\tau=L^{-1}e^{-\tau\Delta}`$ are smooth finite-source responses that converge distributionally to the ordinary Green function only in the singular limit. Their diagonal values are finite before that limit is taken.

This provides a worked conditional interface for the delta/projection principle. It turns the mathematical relation
``` math
\delta=\text{singular shadow of projection}
```
into the operational replacement
``` math
LG=\delta
\quad\leadsto\quad
LG_{\mathrm{coh}}=K_{\mathrm{coh}}.
```

The next step is not automatic substitution in other theories. It is to derive a selected kernel and prove the required covariance, gauge, causal, and interacting consistency conditions in each target domain.

<div class="thebibliography">

9

P. Nero, *Projected Heat Kernels from MTT Fixed-Point Data*, version 2, 2026, joint sharp-limit theorem.

L. Hörmander, *The Analysis of Linear Partial Differential Operators*, Springer.

M. E. Taylor, *Partial Differential Equations I–III*, Springer.

J. Roe, *Elliptic Operators, Topology and Asymptotic Methods*, Chapman and Hall/CRC.

P. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, CRC Press.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics*, Academic Press.

P. Nero, *Dirac Delta Functions as Singular Shadows of Admissible Projection in Modal Triplet Theory*, 2026.

P. Nero, *Fixed Points over Multi-Bundle Manifolds* and related Fixed Points series papers, 2025–2026.

</div>
