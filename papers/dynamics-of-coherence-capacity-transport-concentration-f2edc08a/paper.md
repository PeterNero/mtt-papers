---
abstract: |
  Coherence capacity is a sourced diagnostic of the remaining validity of an effective description. A diagnostic does not move merely because it has been named. To discuss transport one must additionally choose a base space, an ordering variable, a fixed normalized capacity representative, a velocity or flux, source and repair terms, boundary conditions, and a solution concept. This paper supplies that missing model-level framework.

  We distinguish three inequivalent equations: material transport of a scalar reserve, a balance law for an additive density, and advection–diffusion–reaction of a field. We derive the corresponding integral balance, show exactly how nonlinear reparameterization changes a continuity equation, and extend the rowwise capacity budget to continuous trajectories. The bottleneck is the minimum of the reserve rows and is generally nonsmooth when the active row changes. Under a unique active row and a regular-value hypothesis, its first-exit set is a moving codimension-one hypersurface with an explicit normal-velocity formula.

  Two no-go results correct the former transport picture. Source-free passive transport preserves a positive reserve along characteristics. Source-free continuity transport preserves a positive density for every finite interval on which the flow has finite integrated divergence. Compression increases such a density; it does not by itself exhaust a reserve. A focusing inequality, finite-time zero, conservation law, or capacity bottleneck therefore requires additional dynamics or a declared constitutive relation. We give one explicit conditional model in which a compressing carrier lowers a reserve through a fixed decreasing constitutive map. No gravity, horizon, entropy, probability, collapse, irreversibility, or arrow of time is derived from transport alone.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: Version 3, July 2026
generated_from_main_tex_sha256: bfc1ef9fb8d75ae4baa729496c47e831cae6425a0afab90963053dd1623dea8f
paper_id: dynamics-of-coherence-capacity-transport-concentration-f2edc08a
release_state: zenodo_released
released_version: v3
title: |
  Dynamics of Coherence Capacity:
  Constitutive Transport, Balance Laws, and First Exit
zenodo_doi: 10.5281/zenodo.21709740
zenodo_record_id: 21709740
zenodo_url: "https://zenodo.org/records/21709740"
---

# Revision note: Version 3

<div class="description">

Version 3 supersedes Version 2.0, DOI [10.5281/zenodo.18322062](https://doi.org/10.5281/zenodo.18322062).

Version 2 inferred a divergence-free capacity current, generic focusing, codimension-one exhaustion, irreversibility, gravity, and horizons from projection and a finite stability margin. Neither a current nor its conservation follows from those assumptions. The proposed focusing inequality also lacked an evolution equation for the velocity field.

The paper now treats every transport equation as constitutive or action-derived model data. It fixes the normalized capacity representative before taking gradients or fluxes, separates scalar transport from density conservation, proves conditional balance and first-exit results, and gives counterexamples to generic focusing and generic finite-time exhaustion.

The useful question survives: once a particular effective model supplies dynamics for its reserve rows, how can those rows be transported, consumed, repaired, concentrated, and monitored for first exit?

MTT does not yet select one universal capacity evolution law. Any application must derive or postulate its velocity, diffusion, source, repair, boundary, and reset data and then validate them against the underlying operator dynamics.

</div>

# Introduction and roadmap

The two preceding capacity papers answer static and operational questions. The normalized-margin paper defines signed reserve rows, their scales, a bottleneck scalar, and a metric clearance . The control-budget paper defines the least cost of an allowed perturbation that leaves the admissible set . Neither definition contains a velocity field, a flux, a diffusion tensor, or a source.

This distinction matters. A temperature field can be advected, diffuse, or react, but those verbs come from a heat or transport model, not from the definition of temperature. A stability margin is similar. It can change along an evolving state, yet its change law must be calculated from that state evolution or supplied as a reduced constitutive equation.

The paper proceeds in five stages:

1.  Section <a href="#sec:promotion" data-reference-type="ref" data-reference="sec:promotion">2</a> lists the data needed to promote a static capacity record to a dynamical model.

2.  Section <a href="#sec:pathwise" data-reference-type="ref" data-reference="sec:pathwise">3</a> derives continuous-time rowwise budget and first-exit bounds without assuming a local conservation law.

3.  Sections <a href="#sec:balance" data-reference-type="ref" data-reference="sec:balance">4</a>–<a href="#sec:pde" data-reference-type="ref" data-reference="sec:pde">5</a> distinguish scalar transport, density balance, and advection–diffusion–reaction.

4.  Sections <a href="#sec:nogo" data-reference-type="ref" data-reference="sec:nogo">6</a>–<a href="#sec:boundary" data-reference-type="ref" data-reference="sec:boundary">7</a> prove the no-go and regular-boundary results that replace the former generic focusing argument.

5.  Sections <a href="#sec:models" data-reference-type="ref" data-reference="sec:models">9</a>–<a href="#sec:contract" data-reference-type="ref" data-reference="sec:contract">12</a> give conditional models, locate theorem ownership, and state the completion contract for a physical application.

# From a static record to a dynamical model

## The static input

Let $`\mathcal I=\{1,\ldots,m\}`$ index a finite list of sourced admissibility conditions. Their normalized signed reserves are
``` math
r(t,x)=\bigl(r_i(t,x)\bigr)_{i\in\mathcal I},
```
and the signed bottleneck is
``` math
D(t,x)=\min_{i\in\mathcal I}r_i(t,x).
```
The state is admissible exactly when every declared row is positive. The clipped display scalar
``` math
C(t,x)=\min\{1,\max\{0,D(t,x)\}\}
```
is useful for plots but loses information outside the interval $`[0,1]`$. Dynamics should therefore be stated first for the full row vector or for the signed bottleneck $`D`$, not only for $`C`$.

The symbol $`x`$ can denote an effective spatial coordinate, a point in a configuration manifold, or a control parameter. Those interpretations are not interchangeable.

## The dynamical promotion record

<div id="def:record" class="definition">

**Definition 1** (Capacity-dynamics record). A capacity-dynamics record is
``` math
\mathcal D_{\rm cap}
 =
 \bigl(
 I,\mathcal M,g,\mu,r,v,K,s,\mathcal B,\mathcal S,\pi
 \bigr),
```
where:

1.  $`I=[0,T]`$ is an ordering interval;

2.  $`(\mathcal M,g,\mu)`$ is the base manifold, metric, and reference measure;

3.  $`r=(r_i)`$ is one fixed normalized reserve record;

4.  $`v`$ is a supplied transport velocity when used;

5.  $`K=(K_i)`$ is a supplied diffusion or mobility record when used;

6.  $`s=(s_i)`$ contains consumption, repair, exchange, and reclassification terms;

7.  $`\mathcal B`$ contains initial and boundary data;

8.  $`\mathcal S`$ specifies regularity and the classical, weak, renormalized, or entropy solution concept; and

9.  $`\pi`$ records derivation, units, uncertainty, and provenance.

</div>

The record is deliberately larger than a single PDE. Without its base measure, a quantity cannot be classified as a density. Without boundary data, an integral conservation statement is incomplete. Without a solution concept, a discontinuous transport law can be ambiguous.

## Three meanings of transport

<div class="center">

<div class="tabularx">

@L0.22Y Y@ Object & Representative equation & Meaning
Material scalar & $`\partial_t r+v\cdot\nabla r=s`$ & A label or reserve carried along trajectories.
Additive density & $`\partial_t\rho+\operatorname{div}(\rho v)=s`$ & An extensive amount per unit reference volume.
Diffusive/reactive field & $`\partial_t r+v\cdot\nabla r
   =\operatorname{div}(K\nabla r)+s`$ & A constitutive smoothing and source model.

</div>

</div>

Calling all three a “capacity current” would conceal their different transformation laws. In particular, the normalized bottleneck need not be additive over disjoint regions, so it is not automatically a conserved density.

# Pathwise reserve dynamics

The weakest dynamical statement follows the actual state trajectory and does not require a spacetime current.

<div id="ass:path" class="assumption">

**Assumption 2** (Continuous rowwise budget). Let $`x:[0,T]\to\mathcal X`$ be an absolutely continuous trajectory. Suppose each reserve
``` math
R_i(t)=r_i(t,x(t))
```
is absolutely continuous and, for almost every $`t`$,
``` math
\dot R_i(t)\ge-a_i(t),
 \qquad
 a_i(t)\ge0,
```
with $`a_i\in L^1(0,T)`$.

</div>

<div id="thm:pathbudget" class="theorem">

**Theorem 3** (Continuous cumulative budget). *Under Assumption <a href="#ass:path" data-reference-type="ref" data-reference="ass:path">2</a>,
``` math
R_i(t)
 \ge
 R_i(0)-\int_0^t a_i(\sigma)\,\mathrm d\sigma
 \qquad(i\in\mathcal I).
```
Consequently,
``` math
D(t,x(t))
 \ge
 D(0,x(0))
 -
 \int_0^t
 \max_{i\in\mathcal I}a_i(\sigma)\,\mathrm d\sigma.
```
The trajectory remains admissible whenever the right-hand side is positive.*

</div>

<div class="proof">

*Proof.* The first inequality is the fundamental theorem of calculus for absolutely continuous functions. For every row,
``` math
R_i(t)
 \ge
 R_i(0)-\int_0^t\max_j a_j(\sigma)\,\mathrm d\sigma
 \ge
 D(0,x(0))-\int_0^t\max_j a_j(\sigma)\,\mathrm d\sigma.
```
Taking the minimum over $`i`$ proves the second inequality. ◻

</div>

<div id="cor:exit" class="corollary">

**Corollary 4** (Certified first-exit lower bound). *Define
``` math
\tau_{\rm exit}
 =
 \inf\{t\in[0,T]:D(t,x(t))\le0\}.
```
If $`\max_i a_i(t)\le A`$ almost everywhere for a constant $`A>0`$, then
``` math
\tau_{\rm exit}\ge\frac{D(0,x(0))}{A}
```
whenever the quotient lies in $`[0,T]`$.*

</div>

The bound is one-sided. It is not an exact lifetime unless a row is known to consume its full allowance and actually reaches its boundary.

## Switching of the active row

<div class="definition">

**Definition 5** (Active set). At a point $`(t,x)`$, define
``` math
\mathcal I_{\rm act}(t,x)
 =
 \{i:r_i(t,x)=D(t,x)\}.
```

</div>

<div id="prop:min" class="proposition">

**Proposition 6** (One-sided derivative of the bottleneck). *Let the finite family $`R_i(t)`$ be differentiable at $`t_0`$. Then the right directional derivative of
``` math
D(t)=\min_iR_i(t)
```
exists and satisfies
``` math
D'_+(t_0)
 =
 \min_{i\in\mathcal I_{\rm act}(t_0)}\dot R_i(t_0).
```*

</div>

<div class="proof">

*Proof.* Rows outside the active set have a strictly positive separation from the minimum at $`t_0`$ and cannot become minimizing for all sufficiently small positive increments. Expanding the finitely many active rows to first order and taking their minimum gives the formula. ◻

</div>

Thus $`D`$ can have a kink even when every row is smooth. A scalar PDE written directly for $`D`$ must account for active-row switching; it is not generally obtained by applying the same PDE to the minimum.

# Balance laws require additional structure

## Local and integral balance

Suppose a model promotes a quantity $`\rho`$ to an additive density with flux $`J`$ and source $`s`$:
``` math
\partial_t\rho+\operatorname{div}J=s.
```
For a material flux $`J=\rho v`$, this is the continuity equation
``` math
\partial_t\rho+\operatorname{div}(\rho v)=s.
```
Balance laws of this form are standard in continuum physics . Their use here is conditional on the promotion of a particular capacity-related object to a density.

<div id="thm:integral" class="theorem">

**Theorem 7** (Integral balance on a fixed region). *Let $`\Omega\subset\mathcal M`$ be a compact region with smooth boundary and outward normal $`n`$. For a classical solution of
``` math
\partial_t\rho+\operatorname{div}J=s,
```
``` math
\frac{\mathrm d}{\mathrm dt}\int_\Omega\rho\,\mathrm d\mu
 =
 -\int_{\partial\Omega}J\cdot n\,\mathrm dA
 +\int_\Omega s\,\mathrm d\mu.
```
Hence total $`\rho`$ is conserved only when the net boundary flux and integrated source vanish.*

</div>

<div class="proof">

*Proof.* Differentiate under the integral, substitute the field equation, and use the divergence theorem. ◻

</div>

This theorem does not derive the local balance law. It states what follows after that law and its regularity have been supplied. On a moving region, the Reynolds transport term must also be included.

## Normalization rigidity

The capacity representative must be fixed before a density law is used. An arbitrary same-zero-set reparameterization changes the law.

<div id="thm:reparam" class="theorem">

**Theorem 8** (Reparameterization identity). *Let $`C>0`$ satisfy
``` math
\partial_tC+\operatorname{div}(Cv)=s
```
classically, and let $`f\in C^1((0,\infty))`$. Then
``` math
\partial_t f(C)+\operatorname{div}(f(C)v)
 =
 f'(C)s+
 \bigl[f(C)-Cf'(C)\bigr]\operatorname{div}v.
```
For arbitrary compressible velocities, a source-free density law is preserved under $`C\mapsto f(C)`$ only for
``` math
f(C)=aC
```
with constant $`a`$.*

</div>

<div class="proof">

*Proof.* The original equation gives
``` math
\partial_tC+v\cdot\nabla C=s-C\operatorname{div}v.
```
The chain and product rules yield
``` math
\partial_t f(C)+\operatorname{div}(f(C)v)
 =
 f'(C)\bigl(\partial_tC+v\cdot\nabla C\bigr)+f(C)\operatorname{div}v,
```
which is the stated identity. In the source-free case, invariance for arbitrary $`\operatorname{div}v`$ requires $`f(C)-Cf'(C)=0`$. Solving this ordinary differential equation gives $`f(C)=aC`$. ◻

</div>

The functions $`C`$, $`C^2`$, and $`\sqrt C`$ can have the same positive region and zero set, yet they do not represent the same conserved density. This is why the normalization and reference measure are part of Definition <a href="#def:record" data-reference-type="ref" data-reference="def:record">1</a>.

# Constitutive PDE classes

## Passive scalar transport

A reserve label carried by a supplied velocity satisfies
``` math
\partial_t r_i+v\cdot\nabla r_i=s_i.
```
Along a characteristic $`X(t)`$ solving
``` math
\dot X(t)=v(t,X(t)),
```
the row obeys
``` math
\frac{\mathrm d}{\mathrm dt}r_i(t,X(t))
=s_i(t,X(t)).
```
This form is appropriate when $`r_i`$ is a local diagnostic rather than an additive amount.

## Advection–diffusion–reaction

A model can instead supply
``` math
\partial_t r_i+v\cdot\nabla r_i
=
\operatorname{div}(K_i\nabla r_i)+s_i(t,x,r).
```
The diffusion tensor $`K_i`$, reaction law $`s_i`$, and boundary conditions are new physical or algorithmic inputs. A positive-semidefinite $`K_i`$ can smooth spatial variation; it does not specify what is being conserved.

## Weak and rough transport

Classical characteristic formulas require regular velocity fields. For Sobolev or bounded-variation velocities, existence, uniqueness, and renormalization require the hypotheses of the appropriate transport theory. DiPerna–Lions theory treats Sobolev vector fields , and Ambrosio extends the framework to bounded variation under declared divergence control . Nonlinear scalar conservation laws require an entropy condition; the Kruzhkov theory is a standard reference . General elliptic, parabolic, and hyperbolic solution concepts are reviewed in .

These references matter because a formal current is not enough. A paper claiming transport must state whether it has a classical, weak, renormalized, or entropy solution and which theorem supplies well-posedness.

# What source-free transport cannot do

## Passive transport preserves positive reserve

<div id="thm:passive" class="theorem">

**Theorem 9** (No exhaustion from source-free passive transport). *Let $`r`$ solve
``` math
\partial_t r+v\cdot\nabla r=0
```
on a domain where the characteristic flow $`X(t;x_0)`$ exists. Then
``` math
r(t,X(t;x_0))=r(0,x_0).
```
In particular, a strictly positive reserve cannot reach zero along a characteristic by passive transport alone.*

</div>

<div class="proof">

*Proof.* The chain rule gives
``` math
\frac{\mathrm d}{\mathrm dt}r(t,X(t;x_0))
=
\partial_t r+v\cdot\nabla r=0.
```
 ◻

</div>

## A positive density stays positive under smooth continuity flow

<div id="thm:densitypositive" class="theorem">

**Theorem 10** (No finite-time zero from regular source-free continuity). *Let $`v`$ generate a classical flow $`X(t;x_0)`$, and let $`\rho`$ solve
``` math
\partial_t\rho+\operatorname{div}(\rho v)=0.
```
Then
``` math
\rho(t,X(t;x_0))
 =
 \rho_0(x_0)
 \exp\left(
 -\int_0^t\operatorname{div}v(\sigma,X(\sigma;x_0))\,\mathrm d\sigma
 \right).
```
If $`\rho_0(x_0)>0`$ and the divergence integral is finite, then $`\rho(t,X(t;x_0))>0`$.*

</div>

<div class="proof">

*Proof.* Along the flow,
``` math
\frac{\mathrm d}{\mathrm dt}\rho(t,X(t))
=
-\rho(t,X(t))\operatorname{div}v(t,X(t)).
```
Solving this scalar linear equation gives the formula. ◻

</div>

<div class="corollary">

**Corollary 11** (Compression raises a conserved density). *If $`\operatorname{div}v<0`$ along a trajectory, then a positive source-free density increases along that trajectory.*

</div>

This is the opposite of the former claim that generic focusing exhausts a conserved capacity. A reserve can still decrease under compression, but only if the model supplies a separate relation between the carrier density and the reserve.

## Continuity does not imply a focusing equation

<div id="prop:nofocus" class="proposition">

**Proposition 12** (No universal Raychaudhuri-type inequality). *The continuity equation alone does not imply
``` math
\dot\theta\le-\kappa\theta^2
```
for $`\theta=\operatorname{div}v`$ and any fixed $`\kappa>0`$.*

</div>

<div class="proof">

*Proof.* On $`\mathbb R`$, take
``` math
v(x)=ax,
 \qquad
 \rho(t,x)=\rho_0e^{-at},
```
where $`\rho_0>0`$ and $`a<0`$. Then
``` math
\partial_t\rho+\partial_x(\rho v)=0,
\qquad
 \theta=\partial_xv=a,
\qquad
 \dot\theta=0.
```
The proposed inequality would require
``` math
0\le-\kappa a^2,
```
which is false. ◻

</div>

A Raychaudhuri equation follows from geometric and dynamical equations for a congruence, not from a scalar continuity law. Capacity dynamics would need an independently derived equation for $`v`$, its acceleration, curvature coupling, and any shear or vorticity terms.

## The actual routes to first exit

A positive reserve can reach zero if at least one of the following is present:

1.  a negative source or consumption term;

2.  outward boundary loss;

3.  a time-dependent admissible set, tolerance, or normalization;

4.  a constitutive relation to another concentrating field;

5.  singular or nonunique flow behavior outside the regular theorem;

6.  a change of chart or model that reclassifies the active rows; or

7.  initial data already touching the boundary.

Each mechanism has different mathematics and must be recorded separately.

# First-exit geometry

## When is the boundary a hypersurface?

<div id="thm:regularboundary" class="theorem">

**Theorem 13** (Regular active-row boundary). *Fix a time $`t_0`$. Suppose $`r_j(t_0,\cdot)`$ is $`C^1`$ near $`x_0`$,
``` math
r_j(t_0,x_0)=0,
\qquad
 \nabla r_j(t_0,x_0)\ne0,
```
and $`j`$ is the unique active row near $`x_0`$. Then the local first-exit boundary
``` math
\{x:D(t_0,x)=0\}
```
is a $`C^1`$ codimension-one hypersurface near $`x_0`$.*

</div>

<div class="proof">

*Proof.* Uniqueness of the active row gives $`D=r_j`$ locally. The conclusion is the regular-value theorem applied to $`r_j(t_0,\cdot)`$. ◻

</div>

Without the nonzero-gradient condition, the zero set can be singular or have codimension greater than one. It can also contain an open region. Without a unique active row, several hypersurfaces can meet and the bottleneck can be nonsmooth. Codimension one is therefore a theorem under hypotheses, not a generic consequence of capacity language.

## Normal velocity of a regular boundary

<div id="thm:normalvelocity" class="theorem">

**Theorem 14** (Level-set motion law). *Let $`r_j(t,x)=0`$ define a regular moving boundary and set
``` math
n=\frac{\nabla r_j}{|\nabla r_j|}.
```
Its normal velocity is
``` math
V_n=-\frac{\partial_t r_j}{|\nabla r_j|}.
```
If the row satisfies
``` math
\partial_t r_j+v\cdot\nabla r_j=s_j,
```
then
``` math
V_n=v\cdot n-\frac{s_j}{|\nabla r_j|}.
```*

</div>

<div class="proof">

*Proof.* For a boundary trajectory $`x_b(t)`$,
``` math
0=\frac{\mathrm d}{\mathrm dt}r_j(t,x_b(t))
 =\partial_t r_j+\dot x_b\cdot\nabla r_j.
```
Taking the normal component gives the first formula. Substitution of the transport equation gives the second. ◻

</div>

This is the standard level-set logic used for moving fronts . It tracks a boundary after its PDE has been supplied; it does not choose the PDE.

## Exit is not a reset

At $`D=0`$, one declared description has reached its boundary. The model must still choose among:
``` math
\begin{aligned}
 &\text{stop},\qquad
 \text{continue in another chart},\\
 &\text{apply a deterministic reset},\qquad
 \text{apply a stochastic kernel}.
 \end{aligned}
```
Those choices define different hybrid systems. A first-exit surface alone does not define an outcome, a probability law, or an irreversible update.

# Concentration and reserve are different objects

Concentration describes how an additive measure or density occupies a region. Reserve describes distance from a declared failure condition. They can be related, but the relation is constitutive.

<div class="center">

<div class="tabularx">

@L0.23Y Y@ Question & Density $`\rho`$ & Reserve $`r`$
Additive over regions? & Yes, when promoted as a density & Generally no
Compression under continuity? & Raises $`\rho`$ & Undetermined without a relation to $`\rho`$
Zero means? & Absence of represented amount & Failure boundary of a declared condition
Conservation source? & Continuity law or symmetry & Not supplied by its definition

</div>

</div>

<div id="prop:constitutive" class="proposition">

**Proposition 15** (Conditional compression-to-depletion law). *Suppose a positive density obeys
``` math
\partial_t\rho+\operatorname{div}(\rho v)=0
```
and a reserve is defined by a fixed $`C^1`$ constitutive map
``` math
r=h(\rho).
```
Along characteristics,
``` math
\frac{\mathrm dr}{\mathrm dt}
=
-h'(\rho)\rho\,\operatorname{div}v.
```
If $`h'(\rho)<0`$ and $`\operatorname{div}v<0`$, then the reserve decreases.*

</div>

<div class="proof">

*Proof.* The continuity equation gives
``` math
\frac{\mathrm d\rho}{\mathrm dt}=-\rho\operatorname{div}v.
```
Apply the chain rule to $`r=h(\rho)`$. ◻

</div>

This proposition is a valid route from concentration to reserve loss, but the decreasing function $`h`$ is part of the model. It cannot be inferred from projection alone.

# Two explicit conditional models

## Advected consumption on a circle

Let $`x\in S^1`$, let $`u`$ be constant, and consider
``` math
\partial_t r+u\,\partial_xr=-\sigma(t,x),
\qquad
 \sigma\ge0.
```
Along $`X(t)=x_0+ut`$,
``` math
r(t,X(t))
=
r_0(x_0)-\int_0^t\sigma(\tau,X(\tau))\,\mathrm d\tau.
```
The first exit occurs when accumulated consumption reaches the initial reserve. If $`\sigma\le A`$, Corollary <a href="#cor:exit" data-reference-type="ref" data-reference="cor:exit">4</a> gives
``` math
\tau_{\rm exit}\ge\frac{\min_x r_0(x)}{A}.
```

This example has a genuine transport velocity and a genuine sink. The sink is not produced by the word “capacity”; it must be calculated from the underlying operator or control model.

## Compression with a supplied constitutive reserve

On $`\mathbb R`$, choose
``` math
v(x)=-kx,
\qquad
 k>0,
```
and a spatially uniform carrier density
``` math
\rho(t)=\rho_0e^{kt}.
```
It solves the source-free continuity equation. Now supply the decreasing constitutive relation
``` math
r(t)=R-\alpha\rho(t),
\qquad
 R>0,\quad\alpha>0.
```
If $`R>\alpha\rho_0`$, the reserve is initially positive and reaches zero at
``` math
t_*=\frac1k\log\left(\frac{R}{\alpha\rho_0}\right).
```

The model cleanly separates the steps:

1.  continuity transport concentrates $`\rho`$;

2.  the chosen map $`r=R-\alpha\rho`$ turns concentration into reserve consumption; and

3.  the zero of $`r`$ is a first exit.

No gravity, entropy, or horizon follows from these equations.

# Role within Modal Triplet Theory

<div class="center">

<div class="tabularx">

@L0.28Y@ Source & Canonical responsibility
MTT Foundation & Complete admissibility ledger and the stop/continue/reset alternatives .
Normalized capacity paper & Signed slacks, normalization, reserve vector, bottleneck, metric clearance, and active rows .
Control-budget paper & Allowed perturbations, exit cost, cumulative discrete consumption, composition, and resource-completion contract .
This paper & Conditional continuous-time row budgets, scalar-versus-density transport, balance identities, no-go results, regular first-exit geometry, and model-level examples.
Future source dynamics & A selected action, velocity, diffusion, source, repair, exchange, constitutive relation, boundary law, and reset kernel.

</div>

</div>

The corrected order is:
``` math
\begin{aligned}
 \text{operator control rows}
 &\longrightarrow
 \text{normalized capacity record}\\
 &\longrightarrow
 \text{selected or postulated dynamics}
 \longrightarrow
 \text{first-exit analysis}.
 \end{aligned}
```
The dynamics cannot be read backward from the existence of the scalar.

# What is not derived

## No automatic conservation

Conservation requires a balance law plus boundary and source conditions. In a fundamental field theory it can be derived from an action and symmetry; in a reduced model it can be a constitutive postulate. The capacity definition supplies neither.

## No force or gravity

A flux velocity is not a force law. A gradient is not a force until an action, Hamiltonian, or constitutive equation assigns it that role. Einstein gravity requires Lorentzian geometry, a gravitational action or field equations, and a sourced normalization. None is contained in a capacity transport template.

## No entropy or thermalization

Mixing a scalar field does not by itself define entropy. Thermalization requires a state, dynamics, coarse-graining, equilibrium notion, and thermodynamic limit or statistical theorem.

## No horizon or area law

A regular zero-level set is only a failure boundary for the declared certificate. A horizon requires a causal metric and trapped or event-horizon definition. An area law requires state counting and a coefficient.

## No probability, collapse, or arrow of time

A deterministic PDE supplies no outcome probabilities unless a random initial state, noise law, or stochastic kernel is added. A first exit does not choose a reset. An arrow of time requires asymmetric dynamics, boundary conditions, stable records, or thermodynamic structure.

# Completion and falsifiability contract

A physical capacity-dynamics claim must publish at least the following rows.

<div class="center">

<div class="tabularx">

@L0.25Y@ Row & Required content
Base and ordering & Manifold or configuration space, metric, measure, and ordering variable.
Capacity source & Full normalized reserve vector, scales, tolerances, provenance, and active-row convention.
Transport type & Material scalar, additive density, diffusive field, or another explicit type.
Dynamical source & Action, operator evolution, constitutive postulate, or reduction that yields the PDE.
Coefficients & Velocity, flux, diffusion, reaction, consumption, repair, and exchange terms with units.
Initial and boundary data & Domains, inflow/outflow, no-flux, periodic, interface, and compatibility conditions.
Solution concept & Classical, weak, renormalized, entropy, stochastic, or hybrid, with a well-posedness theorem.
Conservation claim & Exact source and boundary conditions or the symmetry that proves it.
First-exit claim & Active row, regularity, transversality, time bound, and error control.
Post-exit rule & Stop, chart change, deterministic reset, or stochastic kernel.
Physical promotion & Separate theorem connecting the model to force, gravity, entropy, measurement, or another observable.
Provenance & Independent inputs, fitted inputs, held-out outputs, code, commit, uncertainty, and hashes for numerical work.

</div>

</div>

The framework is falsifiable. A claimed conservation law fails if its source or boundary flux is nonzero. A pathwise budget fails if an allowed trajectory consumes more than the certified row bounds. A hypersurface claim fails at a zero where transversality or active-row uniqueness fails. A constitutive concentration mechanism fails if the supplied relation does not match the underlying operator evolution. A physical promotion fails if its held-out observable does not agree.

# Conclusion

Coherence capacity can have dynamics, but only after dynamics are supplied. The mathematically clean starting point is the full normalized reserve vector. Along trajectories it supports cumulative consumption and first-exit bounds. On a base manifold it can be placed in a scalar transport, density balance, or advection–diffusion–reaction model, each with different meaning.

The main correction is constructive. Source-free regular transport does not generically exhaust positive capacity, and continuity does not produce a focusing equation. Genuine exhaustion needs a sink, boundary loss, changing admissible set, singular regime, or explicit constitutive link to another field. Once one of those mechanisms is derived, the regular-value and level-set results provide a precise way to analyze the resulting first-exit boundary.

# Reproducibility statement

This paper reports structural definitions, identities, counterexamples, and conditional PDE theorems. It contains no fitted parameter or numerical physical prediction. The source TeX, bibliography, revision audit, and generated PDF are versioned in the MTT papers repository. A future numerical dynamics result must additionally archive its capacity record, PDE coefficients, initial and boundary data, solver, convergence study, error bounds, code commit, and verification hashes.
