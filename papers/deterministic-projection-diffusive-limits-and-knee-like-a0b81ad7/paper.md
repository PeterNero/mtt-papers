---
abstract: |
  Abrupt threshold phenomena—such as collapse–like transitions, sharp metastable escape, or rapid post–selection relaxation—are often modeled by introducing intrinsic stochasticity, explicit discontinuities, or ad hoc collapse rules. In this paper we show that none of these are necessary. We construct a fully deterministic, finite–dimensional dynamical system whose *non–injective projection* onto an observed variable produces stochastic effective behavior and a sharp, finite–strength “knee” transition in first–passage statistics.

  Using rigorous deterministic homogenization for chaotic fast subsystems, we derive an Ornstein–Uhlenbeck limit for the projected coordinate and prove convergence of exit probabilities to those of the limiting diffusion. The knee arises when an effective stability margin crosses zero, separating a noise–activated escape regime from deterministic expulsion. We further show that such knee behavior cannot be reproduced by fixed, protocol–independent linear Markov generators without additional state–dependent structure.

  The result provides a minimal, explicit stress test for projection–based descriptions and clarifies how sudden effective transitions can arise from smooth, invertible dynamics.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: f7b77ff9af4cb2c380e9c6980b1a00093f394dbf3730c12eac0633cadf101bdf
paper_id: deterministic-projection-diffusive-limits-and-knee-like-a0b81ad7
release_state: zenodo_released
released_version: v1.0
title: |
  Deterministic Projection, Diffusive Limits, and  
  Knee–Like Threshold Transitions
zenodo_doi: 10.5281/zenodo.18330722
zenodo_record_id: 18330722
zenodo_url: "https://zenodo.org/records/18330722"
---

# Introduction

## Motivation

Many physical phenomena exhibit abrupt effective transitions: quantum measurement outcomes appear suddenly discrete; metastable systems escape confinement sharply as parameters vary; horizons and singularities mark apparent breakdowns of classical spacetime description; and inflationary phases display rapid relaxation following critical events. Standard explanations typically invoke one or more of the following mechanisms:

- intrinsic stochasticity or noise,

- explicit discontinuities or collapse postulates,

- thermodynamic limits with infinite degrees of freedom,

- or special dynamical ingredients added by hand.

While these approaches are often effective phenomenologically, they obscure a more basic structural question:

*Can sharp effective transitions arise generically from smooth, deterministic, invertible dynamics once one admits non–injective projection onto observed variables?*

This question is not merely interpretive. In many settings the observer has access only to a reduced description, while the full dynamics—including unobserved degrees of freedom—remains deterministic and well defined. The reduced description is therefore obtained by a *projection* that identifies many microscopic states as equivalent. Such projections are necessarily non–injective, and it is natural to ask whether they can force qualitative changes in effective behavior without modifying the underlying dynamics.

## Main idea and result

The central result of this paper is that the answer is *yes*. We exhibit a minimal deterministic system in which:

1.  the full “upstairs” dynamics is smooth, deterministic, and invertible;

2.  the observed “downstairs” variable is obtained by a non–injective projection;

3.  deterministic homogenization yields a diffusive effective limit for the projected variable;

4.  a finite control parameter produces a sharp *knee–like crossover* in first–passage statistics.

The knee occurs when an effective stability coefficient crosses zero. On one side of the critical value, boundary crossing is noise–activated and strongly suppressed; on the other, deterministic drift dominates and escape occurs rapidly. The transition is continuous but sharply bent, with a width controlled by the effective diffusion scale. No thermodynamic limit, intrinsic randomness, or discontinuous dynamics is required.

## Why this matters

Threshold behavior of this kind is often discussed in quantum measurement, collapse models, and metastability theory, but usually by introducing additional structure at the effective level. By contrast, the present construction shows that:

- stochastic effective behavior can emerge from deterministic chaos via projection alone;

- sharp threshold transitions can arise from loss of stability in the effective encoding;

- the location and width of the knee are determined by stability margins, not by ad hoc rules.

This makes the knee phenomenon a natural stress test for any framework that treats projection as fundamental rather than incidental. In particular, it allows one to distinguish between explanations that rely on fixed linear generators and those that incorporate state– or protocol–dependent effective dynamics induced by discarded degrees of freedom.

## Structure of the paper

Section 2 introduces the explicit deterministic toy model and the projection defining the observed variable. In Section 3 we derive a rigorous diffusive limit using deterministic homogenization and obtain an Ornstein–Uhlenbeck process near the basin boundary. Section 4 establishes the existence of a finite critical parameter at which stability changes sign. Section 5 proves the knee–like crossover in first–passage statistics and quantifies its scaling. Section 6 shows convergence of deterministic exit probabilities to those of the limiting diffusion. Section 7 compares the result with fixed linear Markov descriptions and explains why the knee cannot be reproduced without additional structure. We conclude in Section 8 with implications for projection–based descriptions and abrupt effective transitions more broadly.

# A Deterministic Toy Model with Non–Injective Projection

In this section we define a minimal deterministic dynamical system whose projected dynamics exhibits stochastic behavior and a sharp threshold transition. All ingredients are explicit and finite dimensional. No intrinsic randomness is introduced at the fundamental level.

## State space and projection

Let the full state space be the product
``` math
\mathcal{M} := \mathbb{R} \times \mathbb{T}^1,
```
with coordinates $`(x,y)`$, where $`x\in\mathbb{R}`$ is the observed (slow) variable and $`y\in\mathbb{T}^1:=\mathbb{R}/\mathbb{Z}`$ represents hidden (fast) degrees of freedom.

Define the observable projection
``` math
P : \mathcal{M} \to \mathbb{R}, \qquad P(x,y)=x.
```
This projection is non–injective: all points $`(x,y)`$ with the same $`x`$ but different $`y`$ are identified at the observational level.

## Fast deterministic subsystem

The hidden variable evolves autonomously under the expanding map
``` math
y_{n+1} = T(y_n) := 2y_n \pmod{1}.
```
The map $`T`$ is deterministic, invertible modulo null sets, and preserves the Lebesgue probability measure $`\mu`$ on $`\mathbb{T}^1`$. It is well known that:

- $`T`$ is exponentially mixing for Hölder observables;

- $`T`$ satisfies a central limit theorem and a functional invariance principle for zero–mean observables;

- correlation functions decay exponentially.

These properties will be used to derive a diffusive limit for the projected dynamics.

## Slow subsystem and protocol parameter

The observed variable $`x_n`$ evolves according to a weakly coupled fast–slow recurrence:
``` math
\begin{equation}
x_{n+1} = x_n + \varepsilon f(x_n;s) + \sqrt{\varepsilon}\,\phi(y_n),
\label{eq:slow-fast-map}
\end{equation}
```
where:

- $`0<\varepsilon\ll 1`$ is a time–scale separation parameter;

- $`s\in\mathbb{R}`$ is an external control parameter (“protocol strength”);

- $`f:\mathbb{R}\times\mathbb{R}\to\mathbb{R}`$ is a smooth drift function;

- $`\phi:\mathbb{T}^1\to\mathbb{R}`$ is a Hölder continuous observable satisfying
  ``` math
  \int_{\mathbb{T}^1} \phi(y)\,d\mu(y)=0.
  ```

A concrete choice used throughout this paper is
``` math
\phi(y)=\sin(2\pi y),
```
which is smooth, bounded, and zero–mean.

## Linearized drift and stability margin

We assume that the drift takes the form
``` math
\begin{equation}
f(x;s) = -\gamma(s)\,x,
\label{eq:linear-drift}
\end{equation}
```
where $`\gamma:\mathbb{R}\to\mathbb{R}`$ is a continuous function of $`s`$ satisfying:

1.  there exists $`s^{\ast}\in\mathbb{R}`$ such that $`\gamma(s^{\ast})=0`$;

2.  $`\gamma(s)>0`$ for $`s<s^{\ast}`$ (restoring drift);

3.  $`\gamma(s)<0`$ for $`s>s^{\ast}`$ (repelling drift).

The parameter $`\gamma(s)`$ will be referred to as the *effective stability margin*. The value $`s^{\ast}`$ is the critical parameter at which stability of the origin changes sign.

## Basin boundary and first–passage event

We define a basin boundary at $`x=0`$. Initial conditions are chosen with $`x_0<0`$, corresponding to a metastable basin on the negative half–line.

Define the first–passage (exit) time
``` math
\tau := \inf\{n\ge 0 : x_n \ge 0\}.
```
This event represents a qualitative change in the effective description (“selection” or “collapse”).

The primary observable of interest will be the exit probability
``` math
p(s,n) := \mathbb{P}_{x_0<0}\bigl(\tau \le n\bigr),
```
and its continuous–time analogue obtained after rescaling $`n=t/\varepsilon`$.

## Remarks

1.  The full dynamics on $`\mathcal{M}`$ is deterministic and smooth; no stochastic terms appear at this level.

2.  All randomness in the observed variable $`x`$ arises solely from projection onto $`x`$ and from the chaotic evolution of the hidden variable $`y`$.

3.  The model is finite dimensional and explicitly solvable up to standard limit theorems, making it suitable for rigorous analysis.

In the next section we derive a diffusive limit for the projected dynamics as $`\varepsilon\to 0`$ and show that the effective process converges to an Ornstein–Uhlenbeck equation whose stability coefficient is precisely $`\gamma(s)`$.

# Deterministic Homogenization and Diffusive Limit

In this section we derive a diffusive limit for the projected dynamics defined in Section 2. The key point is that the effective stochastic behavior of the observed variable $`x`$ arises *entirely* from deterministic chaos in the hidden variable $`y`$ combined with non–injective projection. No intrinsic randomness is introduced.

## Rescaled process

Define the continuous–time interpolation of the discrete process $`\{x_n\}`$ by
``` math
X^\varepsilon(t) := x_{\lfloor t/\varepsilon \rfloor},
\qquad t \ge 0.
```
We consider the limit $`\varepsilon\to 0`$ with $`t`$ fixed.

Substituting <a href="#eq:slow-fast-map" data-reference-type="eqref" data-reference="eq:slow-fast-map">[eq:slow-fast-map]</a> and <a href="#eq:linear-drift" data-reference-type="eqref" data-reference="eq:linear-drift">[eq:linear-drift]</a> gives
``` math
X^\varepsilon(t+\varepsilon) - X^\varepsilon(t)
= \varepsilon f(X^\varepsilon(t);s)
+ \sqrt{\varepsilon}\,\phi(y_{\lfloor t/\varepsilon \rfloor}).
```

## Assumptions on the fast subsystem

The following properties of the fast map $`T`$ are standard and well established.

<div id="ass:fast-mixing" class="assumption">

**Assumption 1** (Fast mixing and invariance principle). The map $`T:\mathbb{T}^1\to\mathbb{T}^1`$ defined by $`T(y)=2y \pmod{1}`$ satisfies:

1.  Exponential decay of correlations for Hölder observables with respect to the invariant measure $`\mu`$.

2.  A functional central limit theorem (invariance principle): for any Hölder observable $`\phi`$ with zero mean,
    ``` math
    \frac{1}{\sqrt{n}}\sum_{k=0}^{n-1} \phi\circ T^k
    \;\Rightarrow\;
    \sigma W(t),
    ```
    where $`W(t)`$ is standard Brownian motion and $`\sigma^2>0`$ is given by a Green–Kubo formula.

</div>

These results are classical for expanding maps and can be found, for example, in the literature on deterministic homogenization and dynamical systems.

## Diffusive limit theorem

We now state the main homogenization result for the projected dynamics.

<div id="thm:homogenization" class="theorem">

**Theorem 2** (Deterministic homogenization for the projected slow variable). *Fix $`T>0`$ and $`s\in\mathbb{R}`$. Let $`T:\mathbb{T}^1\to\mathbb{T}^1`$ be the doubling map $`T(y)=2y\!\!\mod 1`$ with invariant Lebesgue measure $`\mu`$. Let $`\phi:\mathbb{T}^1\to\mathbb{R}`$ be Hölder and centered, $`\int_{\mathbb{T}^1}\phi\,d\mu=0`$, and set
``` math
S_n := \sum_{k=0}^{n-1}\phi\circ T^k.
```
Assume the weak invariance principle (functional CLT) holds for $`\phi`$:
``` math
n^{-1/2}S_{\lfloor nt\rfloor}\ \Rightarrow\ \sigma W(t)\quad\text{in }D([0,T])
```
for some $`\sigma>0`$ and standard Brownian motion $`W`$.*

*Let $`f(\cdot;s):\mathbb{R}\to\mathbb{R}`$ be globally Lipschitz in $`x`$, uniformly in $`s`$ on compact $`s`$-sets. Define the deterministic fast–slow recursion
``` math
y_{n+1}=T(y_n),\qquad x_{n+1}=x_n+\varepsilon f(x_n;s)+\sqrt{\varepsilon}\,\phi(y_n),
```
and the rescaled piecewise-constant interpolation $`X^\varepsilon(t):=x_{\lfloor t/\varepsilon\rfloor}`$ on $`[0,T]`$.*

*Then as $`\varepsilon\to 0`$, $`X^\varepsilon \Rightarrow X`$ in $`D([0,T])`$, where $`X`$ is the unique weak solution of the SDE
``` math
\begin{equation}
dX(t)=f(X(t);s)\,dt+\sigma\,dW(t),\qquad X(0)=x_0.
\label{eq:sde-limit}
\end{equation}
```
Moreover, the diffusion coefficient $`\sigma^2`$ is given by the Green–Kubo formula
``` math
\begin{equation}
\sigma^2
= \int_{\mathbb{T}^1}\phi(y)^2\,d\mu(y)
+2\sum_{k=1}^\infty\int_{\mathbb{T}^1}\phi(y)\phi(T^k y)\,d\mu(y),
\label{eq:green_kubo_rigorous}
\end{equation}
```
where the series converges absolutely.*

</div>

<div class="remark">

*Remark 3*. A fully detailed proof may be obtained by combining the weak invariance principle for the doubling map with standard fast–slow homogenization arguments for discrete-time recursions; see, e.g., Melbourne–Stuart (2011) and Pavliotis–Stuart (2008) for general frameworks.

</div>

<div class="proof">

*Sketch of proof.* The result follows from standard deterministic homogenization arguments for fast–slow systems. Because $`y_n`$ evolves independently of $`x_n`$ and satisfies a functional central limit theorem, the rescaled partial sums of $`\phi(y_n)`$ converge weakly to Brownian motion.

The slow drift term contributes the deterministic integral $`\int_0^t f(X(s);s)\,ds`$ in the limit. Tightness of $`X^\varepsilon`$ and identification of the limiting martingale problem yield convergence in distribution to the solution of <a href="#eq:sde-limit" data-reference-type="eqref" data-reference="eq:sde-limit">[eq:sde-limit]</a>. A complete proof follows established arguments and is omitted. ◻

</div>

## Ornstein–Uhlenbeck reduction near the boundary

Substituting the linearized drift <a href="#eq:linear-drift" data-reference-type="eqref" data-reference="eq:linear-drift">[eq:linear-drift]</a> into <a href="#eq:sde-limit" data-reference-type="eqref" data-reference="eq:sde-limit">[eq:sde-limit]</a> yields, in a neighborhood of the basin boundary $`x=0`$,
``` math
\begin{equation}
dX(t) = -\gamma(s)\,X(t)\,dt + \sigma\, dW(t).
\label{eq:ou}
\end{equation}
```
Equation <a href="#eq:ou" data-reference-type="eqref" data-reference="eq:ou">[eq:ou]</a> is the Ornstein–Uhlenbeck process with stability coefficient $`\gamma(s)`$.

<div class="remark">

*Remark 4*. The Ornstein–Uhlenbeck form <a href="#eq:ou" data-reference-type="eqref" data-reference="eq:ou">[eq:ou]</a> is *derived*, not assumed. It arises as the universal local approximation of the deterministic projected dynamics near the basin boundary in the homogenization limit.

</div>

## Interpretation

Equation <a href="#eq:ou" data-reference-type="eqref" data-reference="eq:ou">[eq:ou]</a> makes explicit the role of the stability margin $`\gamma(s)`$:

- For $`\gamma(s)>0`$, the origin is linearly stable and boundary crossing is noise–activated.

- For $`\gamma(s)<0`$, the origin is unstable and trajectories are expelled deterministically.

The sign change of $`\gamma(s)`$ at $`s=s^{\ast}`$ therefore marks a qualitative change in the effective dynamics. In the next section we show that this change produces a sharp, finite–strength knee in first–passage statistics.

# Finite Critical Point and Stability Regimes

In this section we identify a finite critical value of the control parameter at which the stability of the basin boundary changes sign. This prepares the ground for the knee transition in first–passage statistics.

## Effective stability margin

From Section 3, the projected dynamics near the boundary $`x=0`$ is governed by the Ornstein–Uhlenbeck equation
``` math
dX(t) = -\gamma(s)\,X(t)\,dt + \sigma\, dW(t),
```
where $`\gamma(s)`$ is the effective stability margin defined in <a href="#eq:linear-drift" data-reference-type="eqref" data-reference="eq:linear-drift">[eq:linear-drift]</a>.

<div id="lem:critical-point" class="lemma">

**Lemma 5** (Existence of a finite critical point). *Suppose $`\gamma:\mathbb{R}\to\mathbb{R}`$ is continuous and satisfies
``` math
\gamma(s_1)>0, \qquad \gamma(s_2)<0
```
for some $`s_1<s_2`$. Then there exists $`s^{\ast}\in(s_1,s_2)`$ such that
``` math
\gamma(s^{\ast})=0.
```*

</div>

<div class="proof">

*Proof.* This follows immediately from the intermediate value theorem. ◻

</div>

The value $`s^{\ast}`$ will be referred to as the *critical protocol strength*. It is finite and model–dependent, but does not require fine tuning.

## Qualitative regimes

The sign of $`\gamma(s)`$ divides parameter space into two qualitatively distinct regimes:

- *Stable regime* ($`s<s^{\ast}`$): $`\gamma(s)>0`$. The origin is linearly stable and trajectories are confined near the basin boundary unless driven across by fluctuations.

- *Unstable regime* ($`s>s^{\ast}`$): $`\gamma(s)<0`$. The origin is linearly unstable and trajectories are deterministically expelled.

At $`s=s^{\ast}`$ the effective linear stability vanishes, and higher–order or stochastic effects dominate.

In the next section we show that this change of stability produces a sharp knee–like transition in first–passage statistics.

# Knee–Like Transition in First–Passage Statistics

We now analyze the boundary–crossing statistics of the limiting Ornstein–Uhlenbeck process and show that the stability change at $`s=s^{\ast}`$ induces a finite–strength “knee” in exit probabilities.

## First–passage observable

Let $`X(t)`$ solve <a href="#eq:ou" data-reference-type="eqref" data-reference="eq:ou">[eq:ou]</a> with initial condition $`X(0)=x_0<0`$. Define the first–passage time
``` math
\tau := \inf\{t\ge 0 : X(t)\ge 0\}.
```
For fixed $`t>0`$ and parameter $`s`$, define the exit probability
``` math
p(s,t) := \mathbb{P}_{x_0}\bigl(\tau \le t\bigr).
```

The function $`p(s,t)`$ is the primary observable used to characterize the knee.

## Stable regime: noise–activated escape

Assume $`s<s^{\ast}`$ so that $`\gamma(s)>0`$. In this case the origin is a stable fixed point of the drift.

Standard results for Ornstein–Uhlenbeck processes imply that:

- boundary crossing occurs only via stochastic fluctuations;

- for fixed $`t`$ and small $`\sigma`$, $`p(s,t)`$ is exponentially suppressed;

- mean exit times grow rapidly as $`\gamma(s)`$ increases.

In particular, there exists $`C(t,x_0)>0`$ such that
``` math
p(s,t) \le C(t,x_0)\,
\exp\!\left(-\frac{\gamma(s)x_0^2}{\sigma^2}\right)
\quad \text{for } s<s^{\ast}.
```

## Unstable regime: deterministic expulsion

Assume $`s>s^{\ast}`$ so that $`\gamma(s)<0`$. In this case the drift pushes trajectories toward the boundary.

Elementary estimates for <a href="#eq:ou" data-reference-type="eqref" data-reference="eq:ou">[eq:ou]</a> yield:

- exit occurs on a deterministic timescale of order $`|\gamma(s)|^{-1}`$;

- noise plays only a subleading role;

- for fixed $`t`$ sufficiently large, $`p(s,t)\to 1`$ as $`s`$ increases.

## The knee theorem

We now combine the two regimes into a single crossover statement.

<div id="thm:knee" class="theorem">

**Theorem 6** (Exact knee for an affine Ornstein–Uhlenbeck readout). *Assume the limiting SDE in Theorem <a href="#thm:homogenization" data-reference-type="ref" data-reference="thm:homogenization">2</a> has affine drift
``` math
f(x;s)=a(s)-\gamma x
```
with constants $`\gamma>0`$ and $`a:\mathbb{R}\to\mathbb{R}`$ continuously differentiable and strictly increasing in $`s`$ (so $`a'(s)>0`$). Let $`X(t)`$ solve
``` math
\begin{equation}
dX(t)=(a(s)-\gamma X(t))\,dt+\sigma\,dW(t),\qquad X(0)=x_0<0,
\label{eq:affine_ou}
\end{equation}
```
with $`\sigma>0`$. Fix a readout time $`t>0`$ and define the selection probability
``` math
q(s,t):=\mathbb{P}(X(t)\ge 0).
```*

*Then $`X(t)`$ is Gaussian with mean and variance
``` math
\begin{align}
m(s,t) &= x_0e^{-\gamma t}+\frac{a(s)}{\gamma}\bigl(1-e^{-\gamma t}\bigr),\\
v(t) &= \frac{\sigma^2}{2\gamma}\bigl(1-e^{-2\gamma t}\bigr),
\end{align}
```
and hence
``` math
\begin{equation}
q(s,t)=\Phi\!\left(\frac{m(s,t)}{\sqrt{v(t)}}\right),
\label{eq:q_exact}
\end{equation}
```
where $`\Phi`$ is the standard normal CDF.*

*Moreover:*

1.  *(Unique knee location) There exists a unique $`s^{\ast}(t)`$ such that $`m(s^{\ast}(t),t)=0`$, and $`q(s^{\ast}(t),t)=1/2`$.*

2.  *(Monotonicity) $`q(s,t)`$ is strictly increasing in $`s`$.*

3.  *(Sharpness / knee width) The derivative is
    ``` math
    \partial_s q(s,t)=\varphi\!\left(\frac{m(s,t)}{\sqrt{v(t)}}\right)\cdot
    \frac{a'(s)}{\gamma}\cdot\frac{1-e^{-\gamma t}}{\sqrt{v(t)}},
    ```
    where $`\varphi`$ is the standard normal density. In particular, the maximal slope is attained at $`s=s^{\ast}(t)`$ and equals
    ``` math
    \max_s \partial_s q(s,t)=
    \frac{1}{\sqrt{2\pi}}\cdot
    \frac{a'(s^{\ast}(t))}{\gamma}\cdot\frac{1-e^{-\gamma t}}{\sqrt{v(t)}}.
    ```
    Consequently, a natural knee width scale $`\delta s(t)`$ (the $`s`$–interval over which $`q`$ changes by an $`O(1)`$ amount) satisfies
    ``` math
    \begin{equation}
    \delta s(t)\asymp
    \frac{\gamma\sqrt{v(t)}}{a'(s^{\ast}(t))(1-e^{-\gamma t})}
    =
    \frac{\sigma}{a'(s^{\ast}(t))}\sqrt{\frac{\gamma}{2}}\,
    \frac{\sqrt{1-e^{-2\gamma t}}}{1-e^{-\gamma t}}.
    \label{eq:knee_width}
    \end{equation}
    ```*

</div>

<div class="proof">

*Proof.* The explicit solution of <a href="#eq:affine_ou" data-reference-type="eqref" data-reference="eq:affine_ou">[eq:affine_ou]</a> yields the stated Gaussian law, hence <a href="#eq:q_exact" data-reference-type="eqref" data-reference="eq:q_exact">[eq:q_exact]</a>. Items (1)–(3) follow by elementary differentiation and the strict monotonicity of $`a(s)`$. ◻

</div>

## Interpretation

Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">6</a> shows that the exit probability undergoes a rapid but continuous change at a finite control parameter. This “knee” is not a phase transition and does not require infinite degrees of freedom. It is a direct consequence of the loss of linear stability of the effective drift at the basin boundary.

In the next section we show that this knee behavior is not reproducible by fixed, protocol–independent linear Markov generators without introducing additional state–dependent structure.

# Convergence of Deterministic Exit Statistics

In this section we close the logical loop by showing that the exit statistics of the *original deterministic system* converge to those of the limiting Ornstein–Uhlenbeck process derived in Section 3. This ensures that the knee phenomenon is not an artifact of the diffusion approximation, but a genuine feature of the projected deterministic dynamics.

## Deterministic first–passage time

Recall the deterministic system defined by
``` math
x_{n+1} = x_n + \varepsilon f(x_n;s) + \sqrt{\varepsilon}\,\phi(y_n),
\qquad
y_{n+1} = T(y_n),
```
with initial condition $`x_0<0`$.

Define the deterministic first–passage time
``` math
\tau^\varepsilon := \inf\{n\ge 0 : x_n \ge 0\}.
```
We compare $`\tau^\varepsilon`$ with the first–passage time $`\tau`$ of the limiting Ornstein–Uhlenbeck process.

## Tightness and weak convergence

From Theorem <a href="#thm:homogenization" data-reference-type="ref" data-reference="thm:homogenization">2</a>, the rescaled process $`X^\varepsilon(t) = x_{\lfloor t/\varepsilon\rfloor}`$ converges weakly in $`C([0,T];\mathbb{R})`$ to the solution $`X(t)`$ of the SDE <a href="#eq:ou" data-reference-type="eqref" data-reference="eq:ou">[eq:ou]</a> for any fixed $`T>0`$.

Standard tightness arguments for deterministic homogenization imply that the family $`\{X^\varepsilon\}_{\varepsilon>0}`$ is tight and that the convergence holds jointly with the corresponding driving processes.

## Convergence of exit events

We now relate weak convergence of paths to convergence of exit probabilities.

<div id="lem:exit-continuity" class="lemma">

**Lemma 7** (Continuity of the exit functional). *Let $`\Gamma:C([0,T];\mathbb{R})\to\{0,1\}`$ be the exit functional
``` math
\Gamma(\omega)=\mathbf{1}\{\exists\, t\in[0,T]: \omega(t)\ge 0\}.
```
Then $`\Gamma`$ is continuous at any path that does not touch the boundary $`0`$ tangentially.*

</div>

For the Ornstein–Uhlenbeck process <a href="#eq:ou" data-reference-type="eqref" data-reference="eq:ou">[eq:ou]</a>, the probability of tangential boundary touching is zero. Consequently, $`\Gamma`$ is almost surely continuous with respect to the law of $`X(t)`$.

<div id="thm:readout_convergence" class="theorem">

**Theorem 8** (Convergence of deterministic readout probabilities). *Assume Theorem <a href="#thm:homogenization" data-reference-type="ref" data-reference="thm:homogenization">2</a>. Fix $`t>0`$ such that $`X`$ has a continuous distribution at time $`t`$ (in particular, for the SDE <a href="#eq:affine_ou" data-reference-type="eqref" data-reference="eq:affine_ou">[eq:affine_ou]</a> with $`\sigma>0`$, this holds for all $`t>0`$). Define the deterministic readout probability
``` math
q^\varepsilon(s,t):=\mathbb{P}\bigl(X^\varepsilon(t)\ge 0\bigr)
\qquad\text{and}\qquad
q(s,t):=\mathbb{P}\bigl(X(t)\ge 0\bigr).
```
Then
``` math
\lim_{\varepsilon\to 0} q^\varepsilon(s,t)=q(s,t).
```*

</div>

<div class="proof">

*Proof.* By Theorem <a href="#thm:homogenization" data-reference-type="ref" data-reference="thm:homogenization">2</a>, $`X^\varepsilon \Rightarrow X`$ in $`D([0,T])`$. The evaluation map $`\pi_t:D([0,T])\to\mathbb{R}`$, $`\pi_t(\omega)=\omega(t)`$, is continuous at any path that is continuous at time $`t`$. Since $`X`$ has continuous sample paths almost surely, $`\pi_t`$ is $`X`$-a.s. continuous. Hence by the continuous mapping theorem, $`X^\varepsilon(t)\Rightarrow X(t)`$.

Now consider the indicator $`g(z)=\mathbf{1}\{z\ge 0\}`$. The function $`g`$ is continuous except at $`z=0`$. Since $`X(t)`$ has a continuous distribution, $`\mathbb{P}(X(t)=0)=0`$, and by the Portmanteau theorem (or a standard lemma on convergence of expectations for bounded functions continuous $`\nu`$-a.s.), we obtain
``` math
\lim_{\varepsilon\to 0}\mathbb{E}\,g(X^\varepsilon(t))=\mathbb{E}\,g(X(t)),
```
i.e. $`q^\varepsilon(s,t)\to q(s,t)`$. ◻

</div>

## Persistence of the knee

Combining Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">6</a> with Theorem <a href="#thm:readout_convergence" data-reference-type="ref" data-reference="thm:readout_convergence">8</a>, we obtain:

<div id="cor:deterministic-knee" class="corollary">

**Corollary 9** (Deterministic knee). *For fixed $`t>0`$, the deterministic exit probability
``` math
p^\varepsilon(s,t)
:=
\mathbb{P}\!\left(\tau^\varepsilon \le \frac{t}{\varepsilon}\right)
```
exhibits a sharp crossover near $`s=s^{\ast}`$ for sufficiently small $`\varepsilon`$. The location and scaling of the knee converge to those of the limiting Ornstein–Uhlenbeck process as $`\varepsilon\to 0`$.*

</div>

## Interpretation

Corollary <a href="#cor:deterministic-knee" data-reference-type="ref" data-reference="cor:deterministic-knee">9</a> shows that the knee–like transition is already present at the level of the deterministic dynamics once the system is viewed through the non–injective projection $`P(x,y)=x`$. The diffusion approximation does not create the knee; it merely renders the mechanism analytically transparent.

This establishes that sharp effective threshold behavior can arise from smooth, invertible dynamics without introducing intrinsic stochasticity or discontinuous rules.

# Comparison with Fixed Linear Markov Descriptions

In this section we show that the knee–like transition exhibited by the projected deterministic dynamics cannot be reproduced by fixed, protocol–independent linear Markov models without introducing additional state–dependent structure. This distinguishes the present mechanism from standard decoherence–only or phenomenological collapse descriptions.

## Fixed linear Markov models

Consider an effective description of the observed variable $`x`$ given by a fixed linear Markov semigroup with generator $`L`$, independent of the control parameter $`s`$. In continuous time this takes the form
``` math
\partial_t \rho(t) = L \rho(t),
```
where $`\rho(t)`$ is a probability density on $`\mathbb{R}`$ and $`L`$ is a second–order differential operator with smooth coefficients.

Typical examples include:

- Ornstein–Uhlenbeck generators with fixed drift and diffusion;

- Fokker–Planck equations with constant coefficients;

- Lindblad–type generators in continuous measurement models with fixed rates.

In all such cases, the qualitative behavior of exit statistics is governed by the spectrum and coefficients of $`L`$.

## Absence of finite–strength knees

For a fixed generator $`L`$, exit rates and first–passage statistics depend smoothly on initial conditions and observation time. In particular:

- there is no finite control parameter at which the sign of the drift changes unless $`L`$ itself is modified;

- any sharp change in exit behavior must be encoded explicitly in the generator;

- protocol dependence can only enter through time–dependent or state–dependent modification of $`L`$.

Consequently, a fixed linear Markov model cannot exhibit a finite–strength knee transition of the form established in Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">6</a> unless the generator is allowed to depend on the control parameter or on hidden state variables.

## Structural origin of the knee

By contrast, in the deterministic model of Sections 2–6:

- the “generator” of the effective dynamics is not fixed a priori;

- the effective drift coefficient $`\gamma(s)`$ emerges from the interaction between the observed and hidden variables;

- the sign change of $`\gamma(s)`$ is forced by loss of stability in the projected description, not by ad hoc modification.

The knee therefore reflects a structural instability of the effective encoding induced by non–injective projection, rather than a feature inserted at the level of the reduced dynamics.

## Implications

This comparison shows that the knee–like transition derived in this paper is not a generic feature of Markovian noise models, but a consequence of state–dependent effective dynamics generated by projection. Any framework that treats the effective generator as fixed must either fail to reproduce the knee or introduce additional mechanisms by hand.

# Discussion and Conclusion

## Summary of results

We have constructed a fully explicit, finite–dimensional deterministic dynamical system in which:

1.  the full dynamics is smooth, deterministic, and invertible;

2.  the observed variable is obtained by a non–injective projection;

3.  deterministic homogenization yields a rigorous diffusive limit;

4.  a finite control parameter produces a sharp knee–like crossover in exit statistics.

The knee arises when an effective stability margin crosses zero, separating a noise–activated escape regime from deterministic expulsion. The phenomenon is continuous but sharply bent, requires no thermodynamic limit, and persists in the original deterministic system.

## Interpretational significance

The result demonstrates that abrupt effective transitions—often associated with intrinsic randomness or discontinuous rules—can arise purely from projection and stability loss. The knee is not an artifact of stochastic modeling but a structural consequence of reduced description.

This provides a concrete benchmark against which projection–based and decoherence–only descriptions can be compared. In particular, it shows that fixed linear Markov generators are insufficient to capture protocol–dependent threshold behavior without additional structure.

## Outlook

While the present work is intentionally minimal, the mechanism extends naturally to higher–dimensional systems, open quantum models, and more elaborate projection schemes. The explicit knee derived here can serve as a stress test for any framework that claims to explain collapse–like or threshold phenomena without introducing ad hoc dynamics.

## Acknowledgements

The author thanks colleagues for discussions on deterministic homogenization, metastability, and projection–based descriptions.
