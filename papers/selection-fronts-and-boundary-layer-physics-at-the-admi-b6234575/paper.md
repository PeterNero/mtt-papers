---
abstract: |
  An admissibility boundary is the place where at least one declared control condition loses positive reserve. That static fact does not by itself produce a boundary layer, metastability, a large-deviation law, a measurement outcome, or a new physical phase. Those conclusions require a specified dynamical model.

  This paper gives a precise conditional meaning to the term *selection front*. The input is a finite vector of normalized signed reserve rows, including the rows needed for spectral separation, projector control, well-posedness, descent, coherent stability, truncation, and numerical certification. The exact boundary is distinguished from a conservative numerical event guard. At one regular active row the boundary is a smooth facet; at transverse row ties it is locally an orthant corner. A dynamical front additionally requires a drift, diffusion, initial law, stopping rule, interior return set, observables, and a post-exit stop, chart-transition, reset map, or reset kernel.

  The central calculation is an exactly solvable normal diffusion on an interval. Its guard-hitting committor and mean exit time are derived in closed form. Drift away from the guard gives an exponential boundary layer of thickness proportional to noise divided by drift; zero drift gives a linear committor and inverse-noise exit time; drift toward the guard gives neither behavior. Thus no universal sigmoid, metastable law, or first-passage scaling follows from admissibility alone. Eyring–Kramers and Freidlin–Wentzell asymptotics remain available when a small-noise family, attracting basin, quasipotential barrier, and regularity hypotheses are independently supplied.

  The result is a reproducible local theory of first exit and a strict application contract. It does not derive vacuum selection, black-hole dynamics, cosmological measures, quantum collapse, or limits on scalable coherence.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 583fd0ce8b87b0ba74250755c01add519d39405f6f4752007bab1f5e50317223
paper_id: selection-fronts-and-boundary-layer-physics-at-the-admi-b6234575
release_state: zenodo_released
released_version: v2
title: |
  Selection Fronts at an Admissibility Boundary:
  Local Exit Geometry, Conditional Boundary Layers, and Reset Semantics
zenodo_doi: 10.5281/zenodo.21710105
zenodo_record_id: 21710105
zenodo_url: "https://zenodo.org/records/21710105"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1.0, DOI [10.5281/zenodo.18262389](https://doi.org/10.5281/zenodo.18262389).

Version 1 used one unspecified scalar as a universal distance to failure and then asserted necessary boundary layers, metastability, large deviations, abrupt effective-theory failure, measurement collapse, black-hole information loss, cosmological measure failure, and coherence limits. It supplied neither a complete reserve ledger nor the generator, small-noise family, guard, reset law, asymptotic regime, or error certificate needed for those deductions.

The revision starts from the normalized multirow admissibility record developed in the corrected capacity papers. It defines local front geometry, separates exact and numerical guards, specifies the additional data required for a diffusion or hybrid process, derives an exact one-dimensional exit model, and states the precise extra assumptions under which large-deviation or Eyring–Kramers results may be imported.

The useful idea survives: when a selected reduced model approaches the first failure of one of its own control rows, committors, exit times, active-row statistics, and exit-location laws can reveal a sharply localized transition layer.

Modal Triplet Theory does not currently select a universal drift, diffusion, noise scale, potential, observation protocol, or post-exit reset for all physical applications. The phrase “selection front” names a conditional first-exit construction, not an additional fundamental interaction.

</div>

# The question in its corrected form

The original paper asked whether the edge of an admissible region has distinctive dynamics. The corrected answer is:

> It can, after both the admissible region and the dynamics approaching it have been specified. The static boundary determines where a selected description first fails. The generator determines how trajectories approach that boundary. A reset rule determines what, if anything, follows the exit.

These are three different mathematical objects. Confusing them was the source of most of the earlier overclaims.

The paper therefore separates:

1.  the *static ledger*: which inequalities define admissibility;

2.  the *local geometry*: whether their common boundary is a facet, a corner, or a singular set;

3.  the *within-chart process*: drift, diffusion, forcing, and observation horizon before first exit;

4.  the *exit statistics*: committors, stopping times, active rows, and exit locations;

5.  the *continuation semantics*: stop, change chart, reset deterministically, or sample a reset kernel; and

6.  the *physical interpretation*: a separate map from these mathematical objects to an experiment or fundamental theory.

The static ledger and its normalized bottleneck are inherited from the capacity papers . The explicit stop/chart/reset alternatives are inherited from the capacity-gated hybrid model . This paper owns the local selection-front record, the transverse-corner description, the exact normal-diffusion calculation, and the resulting diagnostic and application contracts.

## What is not claimed

No theorem below says that every admissibility boundary is physically reachable, that every first exit is irreversible, or that an inadmissible point is absent from reality. It says only that a declared description no longer has all of its certified positive reserves there. Another chart, theory, or scale may remain available.

Likewise, the word *selection* does not mean that the boundary chooses one successor. It refers to the study of a stopping or transition layer. Outcome selection begins only after a continuation law has been supplied.

# The complete static input

## A vector of signed normalized reserves

Let $`U`$ be a state-and-control region and let $`\mathcal I`$ be a finite set of required rows. Each row has:
``` math
s_i:\mathcal D_i\longrightarrow\mathbb R,
 \qquad
 \sigma_i>0,
 \qquad
 r_i=\frac{s_i}{\sigma_i},
 \qquad i\in\mathcal I.
```
Here $`s_i>0`$ means that row $`i`$ passes, $`\sigma_i`$ is a declared reference scale, and the common domain is $`\mathcal D=\bigcap_{i\in\mathcal I}\mathcal D_i`$. Every row also carries provenance: its norm, tolerance, source theorem or assumption, uncertainty, and evaluation method.

The primary object is the vector
``` math
r(x)=\bigl(r_i(x)\bigr)_{i\in\mathcal I}.
```
The signed bottleneck and admissible set are
``` math
\begin{equation}
 D(x)=\min_{i\in\mathcal I}r_i(x),
 \qquad
 \mathcal A=\{x\in\mathcal D:D(x)>0\}.
\label{eq:bottleneck}
\end{equation}
```
The clipped visualization $`C=\min\{1,\max\{0,D\}\}`$ may be useful, but it must not replace the signed rows in an exit calculation.

For a physical application, a single spectral gap is not a complete margin. At minimum, every condition actually used by the reduced description must appear as its own row. Typical families are:

<div class="center">

<div class="tabularx">

@L0.22Y Y@ Row family & Question answered & Example signed reserve
Gap & Is the selected spectral sector separated? & $`(\gamma-\gamma_{\min})/\sigma_{\rm gap}`$.
Projector or resolvent & Is the selected projection bounded and controlled? & $`(K_{\max}-K)/\sigma_{\rm proj}`$.
Well-posedness & Are the operator domain, evolution, or solution hypotheses valid? & A normalized lower bound for the relevant estimate.
Descent or leakage & Does the selected sector remain closed to the declared tolerance? & $`(\ell_{\max}-\ell)/\sigma_{\rm desc}`$.
Coherent stability & Is the complementary or transverse mode stable? & $`(\omega_Q-\omega_{\min})/\sigma_{\rm coh}`$.
Truncation & Is the omitted remainder below the accepted error? & $`(E_{\max}-E)/\sigma_{\rm tr}`$.
Numerical certificate & Does the interval, residual, or majorant test pass strictly? & A normalized certified inclusion radius.

</div>

</div>

The table is a schema, not a claim that every problem uses exactly these seven rows. Omitting a row that the downstream argument needs makes the front incomplete.

## Exact boundary, front layer, and active rows

<div id="def:frontlayer" class="definition">

**Definition 1** (Static selection-front layer). For a fixed normalized record and $`\delta>0`$, define
``` math
\mathcal F_\delta
 =
 \{x\in\mathcal D:0<D(x)\le\delta\}.
```
The exact admissibility boundary is
``` math
\partial_{\mathcal D}\mathcal A
 =
 \{x\in\mathcal D:D(x)=0\}
```
when no domain boundary intervenes. The active-row set is
``` math
I_{\rm act}(x)
 =
 \{i\in\mathcal I:r_i(x)=D(x)\}.
```

</div>

The layer thickness $`\delta`$ is a declared diagnostic resolution in the chosen normalized record. It is not a universal length, energy, or time. A controlled change of row normalization changes its numerical value.

## Exact and numerical guards are not the same

Suppose a computation returns $`\widehat r_i(x)`$ with certified errors
``` math
|r_i(x)-\widehat r_i(x)|\le e_i(x).
```
Then
``` math
D^-(x)=\min_i\bigl(\widehat r_i(x)-e_i(x)\bigr)>0
```
certifies exact admissibility. A numerical event guard may be chosen as
``` math
\mathcal G_{\rm num}
 =
 \{x:D^-(x)\le\delta_{\rm evt}\},
```
where $`\delta_{\rm evt}\ge0`$ includes event-location tolerance and any declared safety reserve.

Reaching $`\mathcal G_{\rm num}`$ need not mean that $`D=0`$. It may be an early, conservative stop. Conversely, stepping across the exact boundary between two discrete time samples is possible unless event detection is included. Every numerical selection-front claim must record which guard was used.

# Local geometry: facets, corners, and singular points

The corrected capacity-dynamics paper proves that one uniquely active $`C^1`$ row with nonzero gradient defines a local codimension-one hypersurface . The next question is what happens when several rows become active together.

<div id="prop:corner" class="proposition">

**Proposition 2** (Transverse active rows give an orthant corner). *Let $`U\subset\mathbb R^n`$ be open and let $`x_0\in U`$. Suppose a set $`J\subset\mathcal I`$ of $`k\le n`$ rows satisfies
``` math
r_j(x_0)=0\quad(j\in J),
 \qquad
 r_i(x_0)>0\quad(i\notin J),
```
and the covectors $`\{\mathrm dr_j(x_0):j\in J\}`$ are linearly independent. Then there is a local $`C^1`$ coordinate chart
``` math
x\longmapsto
 \bigl((r_j(x))_{j\in J},y(x)\bigr)
 \in\mathbb R^k\times\mathbb R^{n-k}
```
in which the admissible set is locally
``` math
(0,\infty)^k\times\mathbb R^{n-k}.
```
The common active stratum $`\{r_j=0:j\in J\}`$ has codimension $`k`$, and the local boundary is the union of its coordinate faces.*

</div>

<div class="proof">

*Proof.* The map $`r_J=(r_j)_{j\in J}`$ has rank $`k`$ at $`x_0`$. The constant rank theorem completes its components to local coordinates $`(r_J,y)`$. Continuity keeps every inactive row positive after the neighborhood is reduced. The sign conditions for membership in $`\mathcal A`$ are therefore exactly $`r_j>0`$ for $`j\in J`$, giving the stated orthant. ◻

</div>

<div class="remark">

*Remark 3*. At a row tie, the scalar minimum $`D=\min_i r_i`$ is generally nondifferentiable even though every row is smooth. A force, normal coordinate, or boundary velocity should therefore be computed rowwise or within a declared stratum. Differentiating the bottleneck as though it were globally smooth is not justified.

</div>

If the active gradients lose rank, the boundary can have cusps, self-contact, higher-order tangency, or an open zero set. “A front is a smooth surface” is consequently a local theorem under regularity and transversality hypotheses, not part of the definition.

# The additional dynamical data

## A typed front record

<div id="def:dynamicrecord" class="definition">

**Definition 4** (Dynamical selection-front record). A dynamical selection-front record consists of:
``` math
\mathcal S_{\rm front}
 =
 \bigl(
 \mathcal R_{\rm adm},
 \{\mathcal L_\eta\}_{\eta\in E},
 \mu_0,
 \mathcal G,
 \mathcal B,
 \mathcal K,
 \mathcal O,
 T_{\rm obs}
 \bigr),
```
where:

1.  $`\mathcal R_{\rm adm}`$ is the complete normalized row record;

2.  $`\eta\in E`$ is a declared model or noise parameter, and $`\mathcal L_\eta`$ is the within-chart generator;

3.  $`\mu_0`$ is the initial law;

4.  $`\mathcal G`$ is the exact or numerical guard;

5.  $`\mathcal B\Subset\mathcal A`$ is an optional interior return or comparison set;

6.  $`\mathcal K`$ is absent for stopping, a chart-transition map, a deterministic reset, or a Markov reset kernel;

7.  $`\mathcal O`$ is the declared observable family; and

8.  $`T_{\rm obs}`$ is the observation horizon.

</div>

For an Ito diffusion in local coordinates,
``` math
\begin{equation}
 \mathrm dX_t
 =
 b_\eta(X_t)\,\mathrm dt
 +
 \sqrt{2\eta}\,\Sigma_\eta(X_t)\,\mathrm dW_t,
\label{eq:diffusion}
\end{equation}
```
the generator is
``` math
\mathcal L_\eta f
 =
 b_\eta\cdot\nabla f
 +
 \eta\,\operatorname{tr}
 \bigl(a_\eta\nabla^2f\bigr),
 \qquad
 a_\eta=\Sigma_\eta\Sigma_\eta^\top.
```
Regularity, nonexplosion, degeneracy, and boundary accessibility hypotheses must be stated for the chosen model. A jump process, delay equation, deterministic flow, or stochastic partial differential equation requires its own solution concept rather than being hidden in $`\mathcal L_\eta`$.

## Committors and stopping times

Let
``` math
\tau_{\mathcal G}=\inf\{t\ge0:X_t\in\mathcal G\},
 \qquad
 \tau_{\mathcal B}=\inf\{t\ge0:X_t\in\mathcal B\}.
```
The guard committor is
``` math
q_\eta(x)
 =
 \mathbb P_x(\tau_{\mathcal G}<\tau_{\mathcal B}).
```
Under standard regularity assumptions it solves the boundary-value problem
``` math
\mathcal L_\eta q_\eta=0,
 \qquad
 q_\eta|_{\mathcal G}=1,
 \qquad
 q_\eta|_{\mathcal B}=0.
```
This function is often a better operational definition of a dynamical front than the raw strip $`\mathcal F_\delta`$: its level sets report the actual competition between drift, diffusion, geometry, and the selected comparison sets.

The equation is not determined by $`D`$. Two models with the same admissible set and different generators can have entirely different committors and exit-time laws.

## A diagnostic barrier becomes a force only when inserted

On a positive-row domain one may define
``` math
U_{\rm bar}(x)
 =
 -\sum_{i\in\mathcal I}\alpha_i\log r_i(x),
 \qquad
 \alpha_i>0.
```
As a plotted scalar, $`U_{\rm bar}`$ is only a diagnostic. If the drift is changed to
``` math
b_\eta=b_\eta^{(0)}-M\nabla U_{\rm bar},
```
then $`-M\nabla U_{\rm bar}`$ is a genuine feedback force or penalty in that reduced model. The coefficients $`\alpha_i`$ and mobility $`M`$ are additional constitutive inputs. The barrier does not become non-dynamical merely because its intended interpretation is “admissibility repair.”

This barrier should also not be confused with the potential in a metastable Eyring–Kramers model. They coincide only if that identification is explicitly made and the resulting drift and basin structure are verified.

## Exit is not continuation

The stopped path and its exit location are determined by the within-chart process. A successor state is not. At the guard the model must choose:
``` math
\text{stop},\qquad
 \text{change chart},\qquad
 \text{apply a reset map},\qquad
 \text{sample a reset kernel}.
```
These choices produce different path laws. In particular, an exit distribution on $`\mathcal G`$ is not a distribution of post-exit outcomes unless a map or kernel from guard states to restart states has been supplied. Stochastic hybrid systems with boundary-hitting resets provide the appropriate established framework .

# An exactly solvable normal front

The simplest calculation already shows why no universal boundary-layer law can follow from the static margin.

## Model

Let $`R_t\in(0,L)`$ be a signed inward normal coordinate, with $`R=0`$ the guard and $`R=L`$ an interior comparison surface. Consider
``` math
\begin{equation}
 \mathrm dR_t=b\,\mathrm dt+\sqrt{2\eta}\,\mathrm dW_t,
 \qquad
 \eta>0,
\label{eq:normalSDE}
\end{equation}
```
stopped at
``` math
\tau=\tau_0\wedge\tau_L,
 \qquad
 \tau_a=\inf\{t\ge0:R_t=a\}.
```
Positive $`b`$ points away from the guard, negative $`b`$ points toward it, and $`b=0`$ is unbiased diffusion.

<div id="thm:normal" class="theorem">

**Theorem 5** (Exact committor and mean exit time). *For the stopped diffusion <a href="#eq:normalSDE" data-reference-type="eqref" data-reference="eq:normalSDE">[eq:normalSDE]</a>, define
``` math
p_\eta(x)=\mathbb P_x(\tau_0<\tau_L),
 \qquad
 T_\eta(x)=\mathbb E_x[\tau],
 \qquad 0<x<L.
```
If $`b\ne0`$, then
``` math
\begin{align}
 p_\eta(x)
 &=
 \frac{e^{-bx/\eta}-e^{-bL/\eta}}
      {1-e^{-bL/\eta}},
\label{eq:pnonzero}\\
 T_\eta(x)
 &=
 \frac{L}{b}
 \frac{1-e^{-bx/\eta}}{1-e^{-bL/\eta}}
 -
 \frac{x}{b}.
\label{eq:Tnonzero}
\end{align}
```
If $`b=0`$, then
``` math
\begin{equation}
 p_\eta(x)=1-\frac{x}{L},
 \qquad
 T_\eta(x)=\frac{x(L-x)}{2\eta}.
\label{eq:zero}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The generator is
``` math
\mathcal L_\eta=b\frac{\mathrm d}{\mathrm dx}
 +\eta\frac{\mathrm d^2}{\mathrm dx^2}.
```
The committor solves
``` math
\mathcal L_\eta p_\eta=0,
 \qquad p_\eta(0)=1,\quad p_\eta(L)=0.
```
For $`b\ne0`$, its general form is $`A+Be^{-bx/\eta}`$; imposing the boundary values gives <a href="#eq:pnonzero" data-reference-type="eqref" data-reference="eq:pnonzero">[eq:pnonzero]</a>. For $`b=0`$, the solution is affine.

Dynkin’s formula gives
``` math
\mathcal L_\eta T_\eta=-1,
 \qquad T_\eta(0)=T_\eta(L)=0.
```
For $`b\ne0`$, integrating the ordinary differential equation twice gives
``` math
T_\eta(x)=-\frac{x}{b}+A+Be^{-bx/\eta}.
```
The two boundary values yield <a href="#eq:Tnonzero" data-reference-type="eqref" data-reference="eq:Tnonzero">[eq:Tnonzero]</a>. When $`b=0`$, solving $`\eta T_\eta''=-1`$ gives <a href="#eq:zero" data-reference-type="eqref" data-reference="eq:zero">[eq:zero]</a>. ◻

</div>

## A genuine boundary layer, under one sign of drift

<div id="cor:thickness" class="corollary">

**Corollary 6** (Exact committor-layer thickness). *Assume $`b>0`$. For any fixed $`q\in(0,1)`$, the unique point $`x_q\in(0,L)`$ satisfying $`p_\eta(x_q)=q`$ is
``` math
x_q
 =
 -\frac{\eta}{b}
 \log\!\left(q+(1-q)e^{-bL/\eta}\right).
```
Consequently,
``` math
x_q
 =
 \frac{\eta}{b}\log\frac1q
 +
 O\!\left(\eta e^{-bL/\eta}\right)
 \qquad(\eta\downarrow0).
```*

</div>

<div class="proof">

*Proof.* Solving <a href="#eq:pnonzero" data-reference-type="eqref" data-reference="eq:pnonzero">[eq:pnonzero]</a> for $`x`$ gives the exact expression. For fixed $`q>0`$, expand the logarithm around $`q`$ as $`e^{-bL/\eta}\to0`$. ◻

</div>

Thus a thin exponential committor layer is real in this model, and its scale is $`\eta/b`$. But it is not universal:

- If $`b>0`$, $`p_\eta(x)`$ is exponentially small away from the guard, while $`T_\eta(x)\to(L-x)/b`$.

- If $`b=0`$, the committor is linear throughout the interval and $`T_\eta(x)`$ scales as $`\eta^{-1}`$.

- If $`b<0`$, the process follows the deterministic drift toward the guard and $`T_\eta(x)\to x/|b|`$; on compact subsets away from $`L`$, $`p_\eta(x)\to1`$.

The same static interval therefore supports a thin exponential layer, a domain-wide linear profile, or almost-certain guard hitting. It supports no universal sigmoid and no automatic exponentially long metastable time.

## What this model does and does not establish

The normal model is a local reduced calculation. It becomes an approximation to a higher-dimensional front only after:

1.  a regular active row provides a normal coordinate;

2.  tangential motion and curvature terms are bounded or retained;

3.  the projected drift and diffusion are derived with an error bound;

4.  the approximation remains valid over the stopping-time scale of interest; and

5.  the comparison surface $`R=L`$ is chosen independently of the desired result.

Without those items, fitting $`b`$ and $`\eta`$ to observed exit data is a phenomenological model, not a derivation from MTT geometry.

# When large deviations and metastability are valid

## Large deviations require a family

Large-deviation theory concerns a declared family such as
``` math
\mathrm dX_t^\eta
 =
 f(X_t^\eta)\,\mathrm dt
 +
 \sqrt{2\eta}\,\Sigma(X_t^\eta)\,\mathrm dW_t,
 \qquad \eta\downarrow0.
```
Under suitable regularity and nondegeneracy assumptions, paths have an action functional. With $`a=\Sigma\Sigma^\top`$ invertible, one common normalization is
``` math
I_{0T}(\phi)
 =
 \frac14\int_0^T
 \bigl(\dot\phi-f(\phi)\bigr)^\top
 a(\phi)^{-1}
 \bigl(\dot\phi-f(\phi)\bigr)\,\mathrm dt.
```
Path probabilities then have logarithmic asymptotics governed by $`\inf I_{0T}/\eta`$, subject to the standard open/closed set qualifications .

One simulation at one noise amplitude does not establish a large-deviation principle. Neither does a small reserve $`D`$. The small-noise parameter, topology on path space, action, and limiting family must all be supplied.

## Metastability requires a trap

Metastability is stronger than proximity to a guard. It requires a long-lived region, a shorter local relaxation scale, and a much longer escape scale. For the standard reversible gradient diffusion
``` math
\begin{equation}
 \mathrm dX_t
 =
 -\nabla V(X_t)\,\mathrm dt
 +
 \sqrt{2\eta}\,\mathrm dW_t,
\label{eq:kramers}
\end{equation}
```
suppose $`m`$ is a nondegenerate local minimum and $`z`$ is the relevant nondegenerate index-one saddle. In the standard ordered-well setting, the Eyring–Kramers transition law has the form
``` math
\begin{equation}
 \mathbb E_m\tau
 \sim
 \frac{2\pi}{|\lambda_-(z)|}
 \sqrt{
 \frac{|\det\nabla^2V(z)|}
      {\det\nabla^2V(m)}
 }
 \exp\!\left(\frac{V(z)-V(m)}{\eta}\right),
 \qquad \eta\downarrow0,
\label{eq:kramerslaw}
\end{equation}
```
where $`\lambda_-(z)`$ is the unique negative Hessian eigenvalue. Rigorous versions require precise basin, saddle, regularity, and ordering hypotheses .

Equation <a href="#eq:kramerslaw" data-reference-type="eqref" data-reference="eq:kramerslaw">[eq:kramerslaw]</a> is powerful precisely because its hypotheses are restrictive. Degenerate saddles, non-gradient drift, multiple equal escape routes, state-dependent or degenerate noise, non-Markov memory, moving guards, and hybrid resets can alter the prefactor, the exponent, or the whole asymptotic form.

## A strict promotion test

A selection-front study may use the words *metastable* or *Kramers* only after it records:

1.  the process family and small parameter;

2.  an attracting set or local equilibrium;

3.  a basin and exit set;

4.  a quasipotential or actual potential barrier;

5.  the relevant regularity and nondegeneracy conditions;

6.  the initial or quasistationary law;

7.  the asymptotic observable and error term; and

8.  whether a reset changes the stopped process.

The v1 paper supplied none of these as a common cross-domain record. Its universal metastability claim is therefore withdrawn, not merely renamed.

# Multiple rows and moving fronts

If one row $`r_j(t,x)`$ is uniquely active and regular, its zero set has normal velocity
``` math
V_n=-\frac{\partial_t r_j}{|\nabla r_j|}.
```
If it obeys
``` math
\partial_t r_j+v\cdot\nabla r_j=s_j,
```
then
``` math
V_n=v\cdot n-\frac{s_j}{|\nabla r_j|}.
```
These are standard level-set identities, already derived in the corrected capacity-dynamics paper and situated in the level-set literature . They track a front after its row evolution has been supplied; they do not select that evolution.

At a transverse corner, several normal coordinates compete. The appropriate local object is the vector
``` math
R_J(X_t)=\bigl(r_j(X_t)\bigr)_{j\in J},
```
not one differentiable scalar minimum. Ito’s formula gives each row its own projected drift, quadratic variation, and cross-variation. The probability of first reaching a particular face then depends on the full covariance matrix and tangential dynamics. Even the identity of the first failing row is generator-dependent.

If the rows themselves depend on time, the admissible set moves. The stopping problem must then be posed in space-time, and a row can reach zero because the state moves, the tolerance changes, or both. These mechanisms should not be merged into a single claim that “capacity was consumed.”

# Observable diagnostics

A front claim should be attached to observables that can be computed, bounded, or measured. Useful examples are:
``` math
\begin{aligned}
 \tau_{\mathcal G}
 &=\inf\{t:X_t\in\mathcal G\},\\
 q(x)
 &=\mathbb P_x(\tau_{\mathcal G}<\tau_{\mathcal B}),\\
 \Theta_\delta(T)
 &=\frac1T\int_0^T
   \mathbf1_{\{0<D(X_t)\le\delta\}}\,\mathrm dt,\\
 \nu_{\rm exit}(A)
 &=\mathbb P_{\mu_0}(X_{\tau_{\mathcal G}}\in A),\\
 \pi_i
 &=\mathbb P_{\mu_0}\bigl(i\in I_{\rm act}(X_{\tau_{\mathcal G}})\bigr).
\end{aligned}
```

<div class="center">

<div class="tabularx">

@L0.23Y Y@ Proposed label & Minimum operational test & What it does not prove
Thin boundary layer & Committor level-set widths shrink under a declared asymptotic family. & A new phase or force.
Metastability & Separation between local relaxation and exit times, with a quasistationary or basin analysis. & Universal Kramers scaling.
Protocol sensitivity & Exit laws change under predeclared variations of initial law, forcing, guard, or reset. & Fundamental indeterminism.
Active-row switching & The identity or multiplicity of limiting rows changes along paths. & Nonsmooth physical motion.
Abrupt transition & A stated observable develops a controlled sharp asymptotic or discontinuity. & Breakdown of every alternative chart.
Irreversibility & Forward and reversed path measures, records, or semigroups fail a declared reversibility criterion. & Irreversibility from noninjectivity alone.

</div>

</div>

Words such as *hesitation*, *channeling*, or *selection* can remain useful descriptive labels, but the archival claim should name the observable, parameter family, comparison baseline, confidence or error bound, and acceptance criterion.

# Numerical execution and exactness

## Boundary events need special treatment

A fixed-step Euler scheme can move from $`D>0`$ to $`D<0`$ without recording the crossing. For killed diffusions, boundary hitting can reduce the weak convergence order of a naive discrete scheme . A credible numerical front calculation should:

1.  retain every signed row rather than only the clipped bottleneck;

2.  bracket the first row crossing within a step;

3.  refine or interpolate the event using a stated method;

4.  distinguish the exact guard from a numerical safety guard;

5.  stop before applying a separately declared reset;

6.  record random seeds and all constitutive parameters;

7.  repeat across time-step and guard tolerances; and

8.  report sampling error separately from discretization and model error.

## What an exactness certificate would contain

For a theorem-level computational claim, the archival packet should contain:

1.  source hashes for the row functions and generator;

2.  interval or otherwise certified row-evaluation errors;

3.  a verified positive reserve before each accepted step;

4.  a certified event bracket or analytic exit solution;

5.  convergence bounds for the chosen stopped-process observable;

6.  the post-exit semantics and reset-support check, if any; and

7.  a verifier independent enough to reject altered rows, parameters, or outputs.

The present paper contains an analytic calculation, not a numerical result packet. No empirical or physical prediction is promoted.

# Contracts for physical applications

The earlier paper moved directly from a formal boundary to cosmology, black holes, measurement, and limits on coherence. The corrected route is to state what each application would have to add.

<div class="center">

<div class="tabularx">

@L0.20Y Y@ Application & Required source data & Status here
Vacuum or compactification selection & A selected configuration space, complete geometric and operator rows, a branch dynamics, noise or control law, and a map from exit/reset states to four-dimensional observables. & Not derived.
EFT or RG validity & A rigorous truncation/error row, well-posed flow, regulator and scheme map, and a comparison to an overlapping description. & A front can mark first certificate failure only.
Cosmological initial data & A state space, measure or deterministic law, constraint surface, observation map, and a justified extrapolation domain. & No global measure conclusion.
Black-hole dynamics & Semiclassical validity rows, a spacetime and quantum-state model, horizon observables, and a continuation law past first failure. & No horizon, information-loss, or evaporation theorem.
Quantum measurement & A system–apparatus algebra, state, interaction, instrument or detector law, outcome record, and probability theorem. & No collapse or Born-rule derivation.
Scalable coherence & An operational coherence measure, noise and control model, device geometry, and asymptotic scaling family. & No universal coherence or entanglement-depth bound.

</div>

</div>

These are not rhetorical disclaimers. They are the missing maps that would turn a conditional first-exit model into a claim about nature.

# Relation to established mathematics

The mathematical neighbors are direct:

- first-exit probabilities and singularly perturbed boundary-value problems ;

- Freidlin–Wentzell large deviations for small random perturbations ;

- potential-theoretic metastability and rigorous Eyring–Kramers laws ;

- hybrid systems and boundary-hitting resets ;

- level-set motion for supplied moving-front equations ; and

- numerical approximation of killed diffusions .

The MTT-specific contribution is not the invention of exit theory. It is the insistence that the exit domain be built from a complete, provenance-bearing vector of normalized admissibility rows, and that static failure, within-chart motion, numerical stopping, and post-exit selection remain separate typed layers.

# Claim status and theorem ownership

<div class="center">

<div class="tabularx">

@L0.27L0.20Y@ Statement & Status & Reason
A complete row record defines an exact first-failure set & Inherited exact fact & Owned by the normalized capacity paper.
A unique regular row defines a local hypersurface & Inherited conditional theorem & Owned by the capacity-dynamics paper.
Transverse simultaneous rows form a local orthant corner & Proved here & Proposition <a href="#prop:corner" data-reference-type="ref" data-reference="prop:corner">2</a>.
The normal constant-drift diffusion has the stated committor and exit time & Proved here & Theorem <a href="#thm:normal" data-reference-type="ref" data-reference="thm:normal">5</a>.
Its outward-drift committor has scale $`\eta/b`$ & Proved here & Corollary <a href="#cor:thickness" data-reference-type="ref" data-reference="cor:thickness">6</a>.
Every admissibility boundary has a thin layer & False without dynamics & The exact model gives three different regimes.
Every front is metastable or obeys Kramers law & Withdrawn & Requires an attracting basin, barrier, small-noise family, and regular saddle data.
Exit selects a unique successor & Withdrawn & A reset map or kernel is independent data.
Selection fronts explain collapse, horizons, or cosmological measures & Open application proposals & The physical source maps listed in <a href="#sec:applications" data-reference-type="ref+label" data-reference="sec:applications">10</a> are absent.

</div>

</div>

This paper is therefore a conditional mathematical reconstruction at the level of a reduced first-exit model. It is not a selected-source theorem for a specific MTT compactification, Standard Model sector, quantum measurement apparatus, or quantum-gravity observable.

# Completion and falsifiability contract

A proposed physical selection front is complete only if another researcher can answer all of the following from the archive:

1.  What is the state-and-control space?

2.  What are all required signed rows, scales, norms, and provenances?

3.  Which boundary point or stratum is under study?

4.  Is the geometry regular, transverse, or singular?

5.  What is the within-chart generator or deterministic evolution?

6.  What parameter tends to zero, infinity, or a threshold?

7.  What are the initial law, guard, comparison set, and observation horizon?

8.  Which committor, exit time, exit law, or active-row statistic is claimed?

9.  What are the analytic, numerical, and sampling errors?

10. Does the process stop, change chart, or reset after exit?

11. Which physical observable does the mathematical output represent?

12. Which held-out data could contradict the construction?

The selection-front interpretation fails for a proposed application if:

- no complete common row record can be formed;

- the claimed front disappears under allowed normalization or certification refinement;

- the observed exit law disagrees with the supplied generator outside the declared error;

- a purported universal scaling changes when an unrecorded drift, covariance, guard, or reset is exposed;

- the physical observable map is nonunique and no source selects one; or

- an overlapping effective description remains controlled across the alleged terminal boundary.

# Conclusion

An admissibility boundary is a precise and useful object: it is the first place where one or more declared control rows lose positive reserve. A selection front becomes dynamical only after a process is supplied.

The exact normal calculation makes the central lesson unavoidable. The same static interval exhibits an exponential committor layer, a linear profile, or almost-certain guard hitting depending only on the drift. Metastability and Eyring–Kramers scaling are valid and important in their own basin-and-barrier regime, but they are not consequences of a small bottleneck reserve.

The corrected concept is therefore narrower than Version 1 and more useful. It provides a disciplined bridge from MTT admissibility records to first-exit analysis while keeping geometry, dynamics, numerics, reset, and physical interpretation separate. That separation is what makes future applications testable.

# Reproducibility statement

All formulas in <a href="#sec:normal" data-reference-type="ref+label" data-reference="sec:normal">5</a> follow from the two elementary boundary value problems
``` math
bp'+\eta p''=0,
 \qquad
 bT'+\eta T''=-1
```
with the displayed boundary conditions. The paper contains no fitted parameter, simulation output, or mapped numerical-result packet. The canonical source, generated Markdown, bibliography, revision audit, and release PDF are maintained in the MTT papers repository. The public repository identifiers are included in the release metadata.
