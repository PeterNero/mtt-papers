---
abstract: |
  We develop disturbance–damping stability on the joint spectral decomposition of the FP–II internal operators. For each noncoherent joint mode $`\alpha`$, the one-sided nonlinear damping margin is $`\gamma_\alpha=d_\alpha-L_\alpha`$. Deterministic force amplitude $`f_\alpha`$ and stochastic noise power $`q_\alpha`$ are distinct quantities. We prove the deterministic input-to-state floor $`\limsup|a_\alpha|\le f_\alpha/\gamma_\alpha`$ and the stochastic second-moment floor $`\limsup\mathbb E|a_\alpha|^2\le q_\alpha/(2\gamma_\alpha)`$ when $`\gamma_\alpha>0`$. Gaussian invariant laws and necessity of the sign condition are asserted only for exact Ornstein–Uhlenbeck dynamics or robust worst-case stability. Bundlewise results apply to $`Q\Psi`$ and use separate stochastic trace and deterministic weighted-series conditions. Finally, deterministic homogenization is made conditional on an enhanced functional central-limit theorem, tightness, and rough-path convergence; the symmetrized Green–Kubo tensor is $`D=\int_0^\infty(R+R^\ast)\,ds`$.
author:
- Peter Nero
bibliography:
- refs.bib
current_version: v7
date: September 2026, Version 7
generated_from_main_tex_sha256: 63582488d784052c7cdb8461833c411533f658dd2ac796e6779b601a1cd47fac
paper_id: fixed-points-iii-disturbance-damping-balance-and-stability
release_state: current_revised_tex
released_version: v5
title: "Fixed Points III: Disturbance–Damping Balance and Stability"
zenodo_doi: 10.5281/zenodo.21655371
zenodo_record_id: 21655371
zenodo_url: "https://zenodo.org/records/21655371"
---

# Version 7 Revision Note

**Supersedes.** Version 6, the previous authoring revision; version 5 remains the released edition. **Reason.** The finite-mode calculations now have a separate manuscript owner and must not be mistaken for a realization of the mixing hypothesis. **Resolution.** Adds a scoped companion citation and distinguishes recurrence, finite-time transition control, and the stochastic-driver limit. **Retained result.** The deterministic, stochastic, and conditional homogenization theorems and their proofs are unchanged. **Remaining boundary.** A selected physical noise source and controlled reduced-dynamics limit are still required.

# Version 6 Revision Note

**Supersedes.** Version 5, which remains the released edition. **Reason and resolution.** Separates the standalone analytic theorems from the physical source-selection problem. **Retained results.** The previous mathematical results and proofs are unchanged. **Boundary.** This is a contextual clarification in an unreleased revision, not a new physical-source theorem.

# Revision note for version 5

Supersedes.
*Fixed Points III: Disturbance–Damping Balance and Stability*, version 4.

Reason.
The corrected deterministic and stochastic estimates in version 4 were sound, but their parallel notation could still obscure that force amplitude, noise power, invariant law, and homogenized noise are different objects.

Resolution.
Version 5 adds an explicit argument map and worked interpretive discussion of the two disturbance lanes, their summability requirements, and the separate homogenization gate. It preserves theorem ownership and separates the public abstract from revision history and reproducibility metadata.

Retained result.
The deterministic input-to-state floor, stochastic second-moment floor, OU restrictions, and enhanced invariance-principle conditions are unchanged.

Remaining boundary.
Coherent-sector disturbances, general nonlinear invariant measures, and a physical stochastic source law remain unproved.

# Revision note for version 4

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

# How to read this paper

FP–II separates the coherent sector $`P\Psi`$ from its damped complement $`Q\Psi`$. This paper asks what happens to the complement when it is continually disturbed. The answer depends on what kind of disturbance is meant, so the paper deliberately develops deterministic forcing and stochastic forcing in parallel without identifying their parameters.

#### The central picture in plain language.

For each joint internal mode, damping removes amplitude at a rate $`d_\alpha`$, while nonlinear feedback can return at most $`L_\alpha`$ in the one-sided energy estimate. Their difference $`\gamma_\alpha=d_\alpha-L_\alpha`$ is the available margin. A bounded deterministic push produces an amplitude floor proportional to $`f_\alpha/\gamma_\alpha`$. Brownian forcing deposits variance rather than a fixed amplitude and produces a second-moment floor proportional to $`q_\alpha/(2\gamma_\alpha)`$. The similar-looking denominators do not make $`f_\alpha`$ and $`q_\alpha`$ the same quantity.

#### Argument map.

Sections 1–2 inherit the joint projector and build a non-double-counted spectral index for the overlapping vertical operators. Sections 3–4 derive the deterministic and stochastic modewise bounds. Section 5 identifies the limited settings in which positivity of the margin is also necessary and a Gaussian invariant law follows. Section 6 lifts individual mode bounds to the bundle by summability or covariance-trace conditions. Section 7 explains when rapidly mixing deterministic complement modes can instead appear as effective stochastic forcing of coherent variables. Sections 8–9 separate invariant measures from deterministic fixed points and turn the hypotheses into an execution checklist.

#### Scope boundary.

Every modal result in the main stability chain concerns $`Q\Psi`$. It neither contracts coherent modes nor proves that a physical environment supplies Brownian noise. The homogenized diffusion is an emergent limit only after the enhanced functional-CLT, tightness, and rough-path hypotheses have been verified for the selected dynamics.

A physical q79 application must independently select the damping generator, coherent projector, invariant domain, gap data, and forcing or noise law. The analytic estimates below consume those typed inputs; they do not emit them from MTT geometry.

# Scope and inherited framework

We use the corrected FP–I/II control framework. The compact internal space carries strongly commuting nonnegative self-adjoint operators $`A_1,A_2,A_3`$ on one common Hilbert space. Their joint harmonic projector is $`P`$, with $`Q=I-P`$. All stability results below concern $`Q\Psi`$ unless coherent forcing is explicitly introduced. The stabilization parameter is not physical Lorentzian time.

Deterministic fixed points of a time-step map and stochastic invariant measures are different objects. Existence of the former is inherited from FP–I/II under their invariant-set and compactness/condensing hypotheses. Existence of the latter requires a Markov/Feller and tightness argument stated separately below. For analytic-semigroup and dissipative-flow background, see ; for stochastic evolution and exact Ornstein–Uhlenbeck processes, see . The companion analytic framework is .

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

#### What the two floors mean.

Both estimates say that positive damping prevents indefinite accumulation in one mode, but they answer different questions. The deterministic theorem bounds every trajectory against a worst-case input amplitude. The stochastic theorem bounds an expectation after quadratic variation has injected power. Neither floor is automatically attained, and neither is a prediction until the mode, margin, and disturbance data have been obtained from the concrete operator model.

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

This section addresses a different route to stochastic behavior. The underlying system can remain deterministic while rapidly mixing noncoherent modes drive slow coherent variables. Under a sufficiently strong limit theorem, the accumulated fast forcing converges to Brownian transport. Ordinary mixing is not enough: the second iterated integrals determine whether the limiting equation is the stated Stratonovich equation or carries an additional bracket drift.

#### A concrete candidate and its limit.

The calculation companion constructs a supplied radial quantum Hamiltonian with finitely many spatial modes but no occupation cutoff. It has compact resolvent and recurrent state orbits. Its all-occupation equilibrium bounds and certified nonzero channel transition are genuine results at that model’s declared boundary, normalization, sector, and preparation. They do not make its nonconstant Gibbs correlations mixing. Thus increasing the occupation cutoff alone does not supply the enhanced invariance principle below. A suitable system–bath or spatial/volume limit, and its reduced path law, must be established separately. The detailed domain construction and calculations belong to that companion; the present paper retains the analytic disturbance and homogenization statements.

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

The paper therefore contributes a translation layer between FP–II spectral damping and later statistical descriptions. Its robust content is the pair of modewise inequalities and their bundlewise summability conditions. Exact Gaussianity belongs only to the OU specialization, while emergent diffusion belongs only to the verified homogenization limit. Coherent disturbances, nonlinear invariant-law uniqueness, and a physical identification of the noise source remain separate model-specific tasks.

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

*Proof.* The first positive eigenvalue varies continuously on this compact metric family and is positive for every compact connected fiber, so it attains a positive minimum; compare the spectral-geometric background in . ◻

</div>

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The analytic disturbance and homogenization statements are proved or explicitly conditioned in this paper. The finite-mode calculation discussed in Section 7 has its own manuscript and reproduction references ; its four frozen records are held in the [curated MTT results repository](https://github.com/PeterNero/mtt-results-repro). They concern the supplied radial model, cubic heat-trace bound, L11 pure channel, and historical frontier map. This citation does not replace the enhanced invariance principle or identify the calculated transition with a selected physical noise law.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
