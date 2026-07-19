---
abstract: |
  We rebuild disturbance–damping stability on the joint spectral decomposition of the corrected FP–II internal operators. For each noncoherent joint mode $`\alpha`$, the one-sided nonlinear damping margin is $`\gamma_\alpha=d_\alpha-L_\alpha`$. Deterministic force amplitude $`f_\alpha`$ and stochastic noise power $`q_\alpha`$ are distinct quantities. We prove the deterministic input-to-state floor $`\limsup|a_\alpha|\le f_\alpha/\gamma_\alpha`$ and the stochastic second-moment floor $`\limsup\mathbb E|a_\alpha|^2\le q_\alpha/(2\gamma_\alpha)`$ when $`\gamma_\alpha>0`$. Gaussian invariant laws and necessity of the sign condition are asserted only for exact Ornstein–Uhlenbeck dynamics or robust worst-case stability. Bundlewise results apply to $`Q\Psi`$ and use separate stochastic trace and deterministic weighted-series conditions. Finally, deterministic homogenization is made conditional on an enhanced functional central-limit theorem, tightness, and rough-path convergence; the corrected Green–Kubo tensor is $`D=\int_0^\infty(R+R^\ast)\,ds`$.
author:
- Peter Nero
bibliography:
- refs.bib
current_version: v4
date: July 2026
generated_from_main_tex_sha256: bf98d12988915667364c8dd5f3a8b44466202b89fc8d94dc400c1238b22ab5eb
paper_id: fixed-points-iii-disturbance-damping-balance-and-stability
release_state: zenodo_released
released_version: v2.0
title: "Fixed Points III: Disturbance–Damping Balance and Stability"
zenodo_doi: 10.5281/zenodo.18202941
zenodo_record_id: 18202941
zenodo_url: "https://zenodo.org/records/18202941"
---

*Part III of VI in the Fixed Point series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

# Revision note for this edition

Supersedes.  
*Fixed Points III: Disturbance–Damping Balance and Stability*, version 3.

Reason.  
Deterministic amplitudes and stochastic powers were conflated, nonlinear systems were assigned Gaussian/OU conclusions, and the Green–Kubo normalization and homogenization hypotheses were incomplete.

Resolution.  
Version 4 derives separate deterministic and stochastic floors on the joint modal spectrum, restricts Gaussian claims to exact OU dynamics, and states the enhanced invariance-principle and rough-path gates.

Retained result.  
Positive net modal damping still gives quantitative noncoherent stability and disturbance floors.

Remaining boundary.  
Coherent disturbances, nonlinear invariant laws, and physical stochastic interpretation require additional assumptions.

# Scope and inherited framework

We use the corrected FP–I/II control framework. The compact internal space carries strongly commuting nonnegative self-adjoint operators $`A_1,A_2,A_3`$ on one common Hilbert space. Their joint harmonic projector is $`P`$, with $`Q=I-P`$. All stability results below concern $`Q\Psi`$ unless coherent forcing is explicitly introduced. The stabilization parameter is not physical Lorentzian time.

Deterministic fixed points of a time-step map and stochastic invariant measures are different objects. Existence of the former is inherited from FP–I/II under their invariant-set and compactness/condensing hypotheses. Existence of the latter requires a Markov/Feller and tightness argument stated separately below.

# Joint modal decomposition

Strong commutation supplies a joint spectral calculus. In the compact pure- point case, choose a joint orthonormal basis $`\{e_\alpha\}`$ such that
``` math
A_ne_\alpha=\lambda_\alpha^{(n)}e_\alpha,
\qquad n=1,2,3.
```
The multi-index $`\alpha`$ includes all three spectral labels and any multiplicity label. Define
``` math
d_\alpha:=\sum_{n=1}^3\kappa_n\lambda_\alpha^{(n)},
\qquad
\Lambda_\alpha:=\sum_{n=1}^3\lambda_\alpha^{(n)}.
```
Let $`\mathcal I_Q`$ contain the indices for which at least one $`\lambda_\alpha^{(n)}`$ is positive. Then
``` math
Q\Psi(t)=\sum_{\alpha\in\mathcal I_Q}a_\alpha(t)e_\alpha.
```
This joint index prevents multiple counting when the vertical structures overlap. It also applies to a genuinely nested realization after its inclusion maps have been supplied; rank labels alone do not establish nesting.

<div id="ass:one-sided" class="assumption">

**Assumption 1** (One-sided modal remainder bound). On the invariant set, the nonlinear modal remainder satisfies
``` math
\operatorname{Re}(\overline{a_\alpha}R_\alpha(a))
\le L_\alpha|a_\alpha|^2,
\qquad
\gamma_\alpha:=d_\alpha-L_\alpha.
```
The remainder may couple modes; the displayed one-sided estimate, rather than an entrywise linearization identity, is the hypothesis used in the energy inequalities.

</div>

# Two distinct disturbance classes

## Deterministic forcing

For deterministic input $`b_\alpha(t)`$ assume
``` math
\|b_\alpha\|_{L^\infty(0,\infty)}\le f_\alpha,
```
where $`f_\alpha`$ has units of amplitude per stabilization time. The mode equation is
``` math
\begin{equation}
\dot a_\alpha=-d_\alpha a_\alpha+R_\alpha(a)+b_\alpha(t).
\label{eq:det-mode}
\end{equation}
```

## Stochastic forcing

For the scalar real stochastic theorem let $`W_\alpha`$ be standard Brownian motions and let $`q_\alpha\ge0`$ be noise powers. The mode equation is
``` math
\begin{equation}
da_\alpha=(-d_\alpha a_\alpha+R_\alpha(a))\,dt
+\sqrt{q_\alpha}\,dW_\alpha(t).
\label{eq:stoch-mode}
\end{equation}
```
Correlated or infinite-dimensional noise is described by a positive covariance operator $`Q_\xi`$; then the scalar $`q_\alpha`$ are replaced by its matrix entries and the bundlewise criterion is a weighted trace condition.

The deterministic amplitude $`f_\alpha`$ and stochastic power $`q_\alpha`$ are not interchangeable and are not represented by one common parameter.

# Modewise stability

<div id="thm:det-iss" class="theorem">

**Theorem 2** (Deterministic input-to-state bound). *Assume Assumption <a href="#ass:one-sided" data-reference-type="ref" data-reference="ass:one-sided">1</a> and $`\gamma_\alpha>0`$. Every solution of Equation <a href="#eq:det-mode" data-reference-type="eqref" data-reference="eq:det-mode">[eq:det-mode]</a> obeys
``` math
|a_\alpha(t)|
\le e^{-\gamma_\alpha t}|a_\alpha(0)|
+\frac{f_\alpha}{\gamma_\alpha}
(1-e^{-\gamma_\alpha t}),
```
and hence
``` math
\limsup_{t\to\infty}|a_\alpha(t)|
\le\frac{f_\alpha}{\gamma_\alpha}.
```*

</div>

<div class="proof">

*Proof.* The upper Dini derivative satisfies $`D^+|a_\alpha|\le-\gamma_\alpha|a_\alpha|+f_\alpha`$. Comparison with the scalar affine equation gives the result. ◻

</div>

<div id="thm:stoch-moment" class="theorem">

**Theorem 3** (Stochastic second-moment bound). *Assume Assumption <a href="#ass:one-sided" data-reference-type="ref" data-reference="ass:one-sided">1</a> and $`\gamma_\alpha>0`$. Every solution of Equation <a href="#eq:stoch-mode" data-reference-type="eqref" data-reference="eq:stoch-mode">[eq:stoch-mode]</a> satisfies
``` math
\frac{d}{dt}\mathbb E|a_\alpha|^2
\le-2\gamma_\alpha\mathbb E|a_\alpha|^2+q_\alpha,
```
and therefore
``` math
\mathbb E|a_\alpha(t)|^2
\le e^{-2\gamma_\alpha t}\mathbb E|a_\alpha(0)|^2
+\frac{q_\alpha}{2\gamma_\alpha}(1-e^{-2\gamma_\alpha t}).
```*

</div>

<div class="proof">

*Proof.* Apply Itô’s formula to $`|a_\alpha|^2`$, use the one-sided remainder bound, and take expectations. The martingale term has zero expectation and the quadratic variation contributes $`q_\alpha dt`$. ◻

</div>

These two theorems are sufficient stability bounds for nonlinear dynamics. They do not assert that a nonlinear invariant law is Gaussian or that $`\gamma_\alpha>0`$ is necessary for every particular forcing history.

# Exact OU theorem and robust necessity

<div id="thm:OU" class="theorem">

**Theorem 4** (Exact scalar OU classification). *For
``` math
da=-\gamma a\,dt+\sqrt q\,dW_t,
\qquad q>0,
```
there is a unique invariant probability law with finite variance if and only if $`\gamma>0`$. It is Gaussian with mean zero and variance
``` math
\operatorname{Var}(a)=\frac{q}{2\gamma}.
```
For $`\gamma=0`$ the variance grows linearly, and for $`\gamma<0`$ it grows exponentially.*

</div>

<div id="thm:robust" class="theorem">

**Theorem 5** (Worst-case deterministic sign criterion). *The scalar family $`\dot a=-da+R(a)+b(t)`$ with $`\operatorname{Re}(\bar aR(a))\le L|a|^2`$ is uniformly input-to-state stable for every bounded input and every admissible remainder only if $`\gamma=d-L>0`$. For a specified forcing/remainder pair, $`\gamma\le0`$ does not by itself prove divergence because cancellation or a vanishing input may occur.*

</div>

Thus “if and only if” belongs to exact OU dynamics or a declared robust worst-case class, not to arbitrary nonlinear stochastic equations.

# Bundlewise noncoherent stability

Under bounded geometry and the joint spectral calculus, assume
``` math
\begin{equation}
c_1\sum_{\alpha\in\mathcal I_Q}(1+\Lambda_\alpha)|a_\alpha|^2
\le\|Q\Psi\|_{H_F^1}^2
\le c_2\sum_{\alpha\in\mathcal I_Q}(1+\Lambda_\alpha)|a_\alpha|^2.
\label{eq:joint-sobolev}
\end{equation}
```

## Stochastic trace condition

For independent exact OU modes define
``` math
\Sigma_q:=\sum_{\alpha\in\mathcal I_Q}
(1+\Lambda_\alpha)\frac{q_\alpha}{2\gamma_\alpha}.
```
If every $`\gamma_\alpha>0`$ and $`\Sigma_q<\infty`$, then
``` math
\limsup_{t\to\infty}\mathbb E\|Q\Psi(t)\|_{H_F^1}^2
\le c_2\Sigma_q.
```
For the independent exact OU product this condition is also necessary for a finite-$`H_F^1`$ second moment. For nonlinear dynamics it remains a sufficient bound unless additional lower estimates establish necessity. With correlated noise the correct replacement is the corresponding weighted covariance trace.

## Deterministic weighted-series condition

Define
``` math
\Sigma_f:=\sum_{\alpha\in\mathcal I_Q}
(1+\Lambda_\alpha)\frac{f_\alpha^2}{\gamma_\alpha^2}.
```
If every $`\gamma_\alpha>0`$ and $`\Sigma_f<\infty`$, then
``` math
\limsup_{t\to\infty}\|Q\Psi(t)\|_{H_F^1}^2
\le c_2\Sigma_f.
```
This is an amplitude-series condition, not a stochastic trace.

## Weyl-law check

If the joint counting function satisfies $`N(\Lambda)\lesssim\Lambda^{d_{\rm eff}/2}`$ and $`\gamma_\alpha\gtrsim1+\Lambda_\alpha`$, then $`q_\alpha\lesssim(1+\Lambda_\alpha)^{-p}`$ with $`p>d_{\rm eff}/2`$ is sufficient for $`\Sigma_q<\infty`$. The exact exponent must be recomputed if the damping growth or joint multiplicities differ.

No statement in this section controls a disturbance acting directly in $`P\Psi`$. Such coherent forcing needs a separate base/coherent stability theorem.

# Deterministic homogenization of coherent dynamics

Write $`\Psi=X+Y`$ with $`X=P\Psi`$ and $`Y=Q\Psi`$. For frozen $`x`$, let the fast flow for $`Y`$ have invariant measure $`\mu_x`$, and decompose
``` math
g(x,y)=\bar g(x)+G(x,y),
\qquad
\bar g(x)=\int g(x,y)\,d\mu_x(y).
```
The correctly scaled slow–fast system is
``` math
\begin{align}
\dot X_\varepsilon
&=f(X_\varepsilon)+\bar g(X_\varepsilon)
+\varepsilon^{-1/2}G(X_\varepsilon,Y_\varepsilon),\\
\dot Y_\varepsilon
&=\varepsilon^{-1}L_{X_\varepsilon}(Y_\varepsilon).
\label{eq:fastslow}
\end{align}
```

For fixed $`x`$ define the stationary covariance
``` math
R_x(s)=\int G(x,Y_s)\otimes G(x,Y_0)\,d\mu_x(Y_0).
```

<div id="ass:efclt" class="assumption">

**Assumption 6** (Enhanced invariance principle). On the selected compact slow domain:

1.  the frozen fast flow has a unique invariant measure and sufficient mixing for an integrable covariance;

2.  the centered additive functionals satisfy a functional CLT uniformly in $`x`$, and their laws are tight in the required path topology;

3.  the lifted first and second iterated integrals converge to a geometric Brownian rough path, with zero area anomaly for the canonical Stratonovich statement below;

4.  the Poisson equation/corrector and its $`x`$-derivatives have the bounds needed to control slow dependence; and

5.  initial layers and exits from the compact slow domain are controlled on $`[0,T]`$.

For infinite-dimensional coherent spaces, the corresponding Hilbert-space tightness, trace, and rough-path assumptions must be supplied separately.

</div>

<div id="thm:homogen" class="theorem">

**Theorem 7** (Conditional homogenized limit). *Under Assumption <a href="#ass:efclt" data-reference-type="ref" data-reference="ass:efclt">6</a>, $`X_\varepsilon`$ converges in law on $`C([0,T])`$ to
``` math
dX_t=(f(X_t)+\bar g(X_t))\,dt+\sigma(X_t)\circ dW_t,
```
where
``` math
\begin{equation}
D(x):=\sigma(x)\sigma(x)^\ast
=\int_0^\infty\bigl(R_x(s)+R_x(s)^\ast\bigr)\,ds.
\label{eq:green-kubo}
\end{equation}
```
If the enhanced limit has a nonzero area anomaly, an additional deterministic bracket drift must be included; if only an ordinary functional CLT is known, the Stratonovich conclusion is not established.*

</div>

# Fixed points versus invariant measures

For autonomous or $`\tau`$-periodic deterministic forcing, the corrected FP–I/II Schauder or Darbo theorem applies after a deterministic invariant set is proved; the result is respectively a step-fixed or periodic point, with equilibrium promotion only under the FP–II Lyapunov condition.

For stochastic forcing, the solution defines a Markov semigroup. An invariant probability measure requires, for example, the Feller property, a Lyapunov moment bound, and tight Krylov–Bogoliubov averages. Uniqueness requires an additional irreducibility/coupling or contractivity argument. A stochastic invariant measure is not called a deterministic fixed point.

# Examples and execution checklist

For a circle operator with eigenvalues $`m^2`$ and linear damping $`\gamma_m=m^2-L`$, exact OU noise gives $`\operatorname{Var}(a_m)=q_m/[2(m^2-L)]`$, whereas bounded deterministic forcing gives $`\limsup|a_m|\le f_m/(m^2-L)`$. These are different floors.

For a compact Heisenberg nilmanifold in a noncollapsing left-invariant metric class, the first positive eigenvalue has a uniform lower bound. This supplies one ingredient in $`d_\alpha`$ but does not replace the joint-mode or summability checks.

For every concrete geometry:

1.  construct the joint spectral index and multiplicities;

2.  compute $`d_\alpha`$ and prove the one-sided constants $`L_\alpha`$;

3.  list deterministic amplitudes $`f_\alpha`$ and stochastic covariance data $`q_\alpha`$ or $`Q_\xi`$ separately;

4.  check $`\gamma_\alpha>0`$ and the appropriate $`\Sigma_f`$ or covariance trace;

5.  control coherent forcing independently; and

6.  for homogenization, verify the enhanced invariance principle rather than only quoting mixing.

# Conclusion

The damping-margin principle survives, but with precise scope. Positive $`\gamma_\alpha`$ gives deterministic input-to-state and stochastic second-moment bounds. Exact Gaussian invariant laws and sign necessity belong to exact OU or robust worst-case formulations. Bundlewise results concern $`Q\Psi`$ and require either a stochastic trace or deterministic weighted series. The homogenized Stratonovich equation is conditional on enhanced functional-CLT/rough-path data and uses the corrected Green–Kubo normalization. These distinctions prevent stochastic invariant measures from being conflated with deterministic fixed points.

# Exact OU variance computation

For $`da=-\gamma a\,dt+\sqrt q\,dW_t`$,
``` math
a(t)=e^{-\gamma t}a(0)+\sqrt q\int_0^t e^{-\gamma(t-s)}\,dW_s.
```
Itô isometry gives
``` math
\mathbb E\left|\sqrt q\int_0^t e^{-\gamma(t-s)}\,dW_s\right|^2
=\frac{q}{2\gamma}(1-e^{-2\gamma t})
```
when $`\gamma>0`$.

# Uniform spectral gap for noncollapsing nil fibers

<div class="proposition">

**Proposition 8**. *Let $`F=\Gamma\backslash\mathrm{Nil}_3`$ be fixed and let $`\mathcal G_\epsilon`$ be a compact class of left-invariant metrics satisfying $`\epsilon I\le G\le\epsilon^{-1}I`$. Then
``` math
\inf_{g\in\mathcal G_\epsilon}\lambda_1(F,g)>0.
```
The same bound is uniform for a smoothly base-dependent family remaining in $`\mathcal G_\epsilon`$.*

</div>

<div class="proof">

*Proof.* The first positive eigenvalue varies continuously on this compact metric family and is positive for every compact connected fiber, so it attains a positive minimum. ◻

</div>
