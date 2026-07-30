---
abstract: |
  A delta-correlated covariance is the distributional limit of many finite-memory kernels, but covariance convergence alone does not imply convergence of stochastic processes, Gaussianity, or the Markov property. We separate these statements and prove an exact process-level model. Nonnegative approximate-identity kernels with total mass $`2D`$ converge to $`2D\delta_0`$ as distributions. A valid stationary covariance must additionally be of positive type. For the explicit stationary colored Ornstein–Uhlenbeck source
  ``` math
  d\xi_\tau=-\tau^{-1}\xi_\tau\,dt
   +\sqrt{2D}\,\tau^{-1}dW_t,
  ```
  the integrated disturbance $`B_\tau(t)=\int_0^t\xi_\tau(s)\,ds`$ converges weakly in $`C([0,T])`$ to $`\sqrt{2D}\,W`$. The damped response therefore converges to the white-noise Ornstein–Uhlenbeck equation. Its exact finite-memory stationary variance is
  ``` math
  \operatorname{Var}(a_\tau)=\frac{D}{\gamma(1+\gamma\tau)},
  ```
  which tends to $`D/\gamma`$. This supplies a rigorous effective Markov limit, not a derivation of fundamental randomness. A general MTT source theorem would still need a selected preparation measure or invariant state, positivity of the covariance, mixing or a functional limit theorem, closure of the resolved variables, and a derivation of the finite-memory coefficients from the physical carrier.
author:
- Peter Nero
current_version: v1
date: July 2026, Version 1
generated_from_main_tex_sha256: 1d38d1f8f8c4c4af18459c4d2464d9fa6583fe3d28625f099ebf375a915e2180
paper_id: white-noise-and-markov-limits-as-delta-correlation-idea-854be499
release_state: zenodo_released
released_version: v1
title: |
  Finite-Memory Noise and the White-Noise/Markov Limit
  Exact Colored-OU Convergence and Its MTT Scope
zenodo_doi: 10.5281/zenodo.21666016
zenodo_record_id: 21666016
zenodo_url: "https://zenodo.org/records/21666016"
---

# Version 1 Revision Note

Supersedes
The unversioned April 2026 manuscript *White Noise and Markov Limits as Delta-Correlation Idealizations: Finite Memory, Colored Disturbances, and OU Floors in Modal Triplet Theory*.

Reason
The earlier paper proved distributional covariance convergence but described an OU process and a Markov limit as if they followed automatically. It did not require positive-definiteness of a covariance, Gaussianity or mixing for process convergence, or closure of the resolved state.

Resolution
This version distinguishes kernel, covariance, finite- dimensional, path-space, and Markov convergence. It proves an explicit colored-OU functional limit and the exact finite-memory response variance, then states the additional assumptions needed for a general MTT realization.

Retained result
White-noise covariance is a controlled zero-memory idealization of normalized finite-memory kernels, and the exponential colored-OU model converges to the standard white-noise OU model.

Remaining boundary
No selected MTT geometry currently emits the finite-memory source, its invariant law, mixing estimates, or coefficients for all physical sectors. The exact model in this paper is an effective construction, not evidence that noise is ontically fundamental or universally Markovian.

# Five different limits

The notation
``` math
\mathbb{E}[\xi(t)\xi(t')]=2D\,\delta(t-t')
```
is compact, but it can conceal several independent claims:

1.  a family of ordinary kernels converges to a Dirac distribution;

2.  those kernels are valid covariances of actual processes;

3.  the finite-dimensional laws of those processes converge;

4.  the full paths converge in a specified topology; and

5.  the limiting resolved dynamics is Markov.

Only the first statement follows from the approximate-identity calculation. The other four require extra hypotheses. This paper proves all five for one explicit Gaussian colored-OU model and keeps the general case conditional.

<div class="center">

| Object | Required control |
|:---|:---|
| Kernel | positivity as a measure, normalization, concentration |
| Covariance | positive type or nonnegative spectral measure |
| Finite-dimensional law | distributional information beyond second moments, unless Gaussian |
| Path law | tightness plus finite-dimensional convergence |
| Markov limit | closure of the limiting state and transition law |

</div>

# Approximate identities

Let $`C_\tau\in L^1(\mathbb{R})`$, with $`\tau>0`$, model a memory kernel.

<div id="thm:delta" class="theorem">

**Theorem 1** (Delta-correlation limit). *Suppose:*

1.  *$`C_\tau(t)\geq0`$;*

2.  *$`\int_{\mathbb R}C_\tau(t)\,dt=2D`$; and*

3.  *for every $`\varepsilon>0`$,
    ``` math
    \int_{|t|>\varepsilon}C_\tau(t)\,dt\longrightarrow0
    \quad\text{as }\tau\downarrow0.
    ```*

*Then $`C_\tau\to2D\delta_0`$ in the sense of distributions. Equivalently, for every $`f\in C_c^\infty(\mathbb{R})`$,
``` math
\int_{\mathbb R}C_\tau(t)f(t)\,dt\longrightarrow2Df(0).
```*

</div>

<div class="proof">

*Proof.* Write
``` math
\int C_\tau(t)f(t)\,dt-2Df(0)
=\int C_\tau(t)\bigl(f(t)-f(0)\bigr)\,dt.
```
For a fixed $`\varepsilon>0`$, the contribution from $`|t|<\varepsilon`$ is bounded by
``` math
2D\sup_{|t|<\varepsilon}|f(t)-f(0)|.
```
The complementary contribution is bounded by
``` math
2\|f\|_\infty
\int_{|t|>\varepsilon}C_\tau(t)\,dt.
```
First take $`\tau\downarrow0`$, then $`\varepsilon\downarrow0`$. ◻

</div>

Two standard examples are
``` math
\begin{align}
C_\tau^{\mathrm{exp}}(t)
&=\frac{D}{\tau}e^{-|t|/\tau},
\label{eq:exp-cov}\\
C_\tau^{\mathrm{gau}}(t)
&=\frac{2D}{\sqrt{2\pi}\tau}
\exp\!\left(-\frac{t^2}{2\tau^2}\right).
\label{eq:gauss-cov}
\end{align}
```
Both have total mass $`2D`$, and both concentrate at the origin.

# A kernel is not automatically a covariance

Pointwise nonnegativity is enough for Theorem <a href="#thm:delta" data-reference-type="ref" data-reference="thm:delta">1</a>, but not enough for a stationary covariance.

<div class="definition">

**Definition 2** (Positive-type covariance). An even function $`C:\mathbb{R}\to\mathbb{R}`$ is of positive type if, for every finite set $`t_1,\ldots,t_n`$ and $`z_1,\ldots,z_n\in\mathbb{C}`$,
``` math
\sum_{j,k=1}^n
z_j\overline{z_k}\,C(t_j-t_k)\geq0.
```

</div>

Every covariance of a second-order stationary process has this property, because the displayed sum equals
``` math
\mathbb{E}\left|
\sum_j z_j\xi(t_j)
\right|^2.
```
Conversely, under the usual continuity assumptions, Bochner’s theorem represents a positive-type function as the Fourier transform of a finite nonnegative spectral measure.

The two kernels <a href="#eq:exp-cov" data-reference-type="eqref" data-reference="eq:exp-cov">[eq:exp-cov]</a>–<a href="#eq:gauss-cov" data-reference-type="eqref" data-reference="eq:gauss-cov">[eq:gauss-cov]</a> are valid:
``` math
\widehat C_\tau^{\mathrm{exp}}(\omega)
=\frac{2D}{1+\omega^2\tau^2}\geq0,
\qquad
\widehat C_\tau^{\mathrm{gau}}(\omega)
=2D e^{-\omega^2\tau^2/2}\geq0.
```

<div id="prop:covariance" class="proposition">

**Proposition 3** (Covariance does not determine process law). *Two processes can have identical means and covariances but different laws. Consequently, covariance convergence alone does not imply process convergence or Gaussian white noise.*

</div>

<div class="proof">

*Proof.* Let $`Z\sim N(0,1)`$ and let $`R`$ be Rademacher, with values $`\pm1`$ of equal probability. The constant processes $`X_t=Z`$ and $`Y_t=R`$ both have mean zero and covariance one at every pair of times. Their one-time distributions are different. ◻

</div>

Gaussianity removes this particular ambiguity because a Gaussian process is determined by its mean and covariance. The exact model below uses that fact and separately proves path tightness.

# An exact finite-memory source

Fix $`D>0`$. For every $`\tau>0`$, let $`\xi_\tau`$ be the stationary solution of
``` math
\begin{equation}
d\xi_\tau(t)
=-\frac{1}{\tau}\xi_\tau(t)\,dt
+\frac{\sqrt{2D}}{\tau}\,dW_t,
\label{eq:colored-ou}
\end{equation}
```
initialized with $`\xi_\tau(0)\sim N(0,D/\tau)`$, independent of the future Wiener increments. Then
``` math
\begin{equation}
\mathbb{E}[\xi_\tau(t)\xi_\tau(s)]
=\frac{D}{\tau}e^{-|t-s|/\tau}.
\label{eq:colored-cov}
\end{equation}
```
The source is Markov and Gaussian on the augmented variable $`\xi_\tau`$, has finite memory time $`\tau`$, and has diverging pointwise variance $`D/\tau`$. Its integrated power remains finite.

Define
``` math
B_\tau(t)=\int_0^t\xi_\tau(u)\,du.
```

<div id="thm:functional" class="theorem">

**Theorem 4** (Colored noise converges to Brownian forcing). *For every finite $`T>0`$,
``` math
B_\tau\Rightarrow\sqrt{2D}\,W
\quad\text{in }C([0,T])
```
as $`\tau\downarrow0`$.*

</div>

<div class="proof">

*Proof.* Each $`B_\tau`$ is a centered continuous Gaussian process. For $`0\leq s\leq t`$, direct integration of <a href="#eq:colored-cov" data-reference-type="eqref" data-reference="eq:colored-cov">[eq:colored-cov]</a> gives
``` math
\begin{align}
\operatorname{Cov}(B_\tau(t),B_\tau(s))
={}&2Ds
-D\tau(1-e^{-s/\tau})\notag\\
&-D\tau
\left(e^{-(t-s)/\tau}-e^{-t/\tau}\right).
\label{eq:integrated-cov}
\end{align}
```
This converges to $`2D\min(s,t)`$, the covariance of $`\sqrt{2D}\,W`$. Gaussianity therefore gives convergence of every finite-dimensional distribution.

For $`0\leq s\leq t\leq T`$,
``` math
\mathbb{E}|B_\tau(t)-B_\tau(s)|^2
=2D(t-s)-2D\tau(1-e^{-(t-s)/\tau})
\leq2D|t-s|.
```
The increment is Gaussian, so
``` math
\mathbb{E}|B_\tau(t)-B_\tau(s)|^4
=3\left(\mathbb{E}|B_\tau(t)-B_\tau(s)|^2\right)^2
\leq12D^2|t-s|^2.
```
The Kolmogorov tightness criterion gives tightness in $`C([0,T])`$. Together with finite-dimensional convergence, this proves the claim. ◻

</div>

This theorem is stronger than
``` math
C_\tau\to2D\delta_0.
```
It establishes convergence of complete continuous paths for an explicit finite-memory process.

# The damped response and its exact floor

Let $`a_\tau`$ solve the ordinary random differential equation
``` math
\begin{equation}
\dot a_\tau(t)
=-\gamma a_\tau(t)+\xi_\tau(t),
\qquad \gamma>0.
\label{eq:colored-response}
\end{equation}
```
Equivalently,
``` math
a_\tau(t)
=a_0-\gamma\int_0^t a_\tau(s)\,ds+B_\tau(t).
```

<div id="cor:ou-limit" class="corollary">

**Corollary 5** (White-noise OU limit). *On every finite interval,
``` math
a_\tau\Rightarrow a
\quad\text{in }C([0,T]),
```
where
``` math
\begin{equation}
da(t)=-\gamma a(t)\,dt+\sqrt{2D}\,dW_t.
\label{eq:white-ou}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* For a continuous driver $`b`$, the integral equation
``` math
x(t)=a_0-\gamma\int_0^t x(s)\,ds+b(t)
```
has a unique solution, and the solution map is continuous in the uniform norm by Gronwall’s inequality. Apply the continuous mapping theorem to Theorem <a href="#thm:functional" data-reference-type="ref" data-reference="thm:functional">4</a>. ◻

</div>

The finite-memory stationary variance can also be computed exactly without taking the limit.

<div id="thm:finite-floor" class="theorem">

**Theorem 6** (Exact colored-OU response variance). *For the stationary joint system <a href="#eq:colored-ou" data-reference-type="eqref" data-reference="eq:colored-ou">[eq:colored-ou]</a>–<a href="#eq:colored-response" data-reference-type="eqref" data-reference="eq:colored-response">[eq:colored-response]</a>,
``` math
\operatorname{Var}(\xi_\tau)=\frac{D}{\tau},
\qquad
\operatorname{Cov}(a_\tau,\xi_\tau)=\frac{D}{1+\gamma\tau},
```
and
``` math
\begin{equation}
\operatorname{Var}(a_\tau)
=\frac{D}{\gamma(1+\gamma\tau)}.
\label{eq:finite-variance}
\end{equation}
```
Hence
``` math
\operatorname{Var}(a_\tau)\longrightarrow\frac{D}{\gamma},
```
the stationary variance of equation <a href="#eq:white-ou" data-reference-type="eqref" data-reference="eq:white-ou">[eq:white-ou]</a>.*

</div>

<div class="proof">

*Proof.* Stationarity of $`\xi_\tau`$ gives $`\operatorname{Var}(\xi_\tau)=D/\tau`$. Differentiating the stationary second moments, or equivalently solving the $`2\times2`$ Lyapunov equation, gives
``` math
0=-(\gamma+\tau^{-1})\operatorname{Cov}(a_\tau,\xi_\tau)
+\frac{D}{\tau},
```
and
``` math
0=-2\gamma\operatorname{Var}(a_\tau)
+2\operatorname{Cov}(a_\tau,\xi_\tau).
```
Solving these equations yields the result. ◻

</div>

The quantity in <a href="#eq:finite-variance" data-reference-type="eqref" data-reference="eq:finite-variance">[eq:finite-variance]</a> is an effective response width. It is not, without further operator and normalization theorems, the Heisenberg uncertainty relation.

# What is genuinely Markov

At finite $`\tau`$, the augmented pair
``` math
(a_\tau,\xi_\tau)
```
is Markov. The resolved coordinate $`a_\tau`$ alone is not closed: its instantaneous derivative depends on the hidden memory coordinate $`\xi_\tau`$. In the limit, Corollary <a href="#cor:ou-limit" data-reference-type="ref" data-reference="cor:ou-limit">5</a> yields the closed Markov diffusion $`a`$.

Thus a correct statement for this model is
``` math
\boxed{
\text{finite Markov augmentation}
\longrightarrow
\text{nonclosed resolved memory}
\longrightarrow
\text{closed Markov limit}.
}
```

For a general colored disturbance, none of these arrows is automatic. One needs:

- a normalized invariant law or preparation ensemble;

- a valid covariance or transition kernel;

- mixing, martingale, or other functional-limit hypotheses;

- tightness in a declared path topology;

- and closure of the limiting resolved variables.

A deterministic upstream flow can satisfy a functional central limit theorem under suitable invariant-measure and mixing assumptions. That is a deterministic source of effective Brownian behavior, but the invariant measure and hypotheses remain part of the theorem. Determinism alone does not imply a diffusive limit.

# Nonlinear limits and stochastic calculus

For the additive equation <a href="#eq:white-ou" data-reference-type="eqref" data-reference="eq:white-ou">[eq:white-ou]</a>, Ito and Stratonovich forms coincide. For nonlinear multiplicative noise, the limiting calculus can depend on how the finite-memory or smooth forcing is taken to zero memory. Classical Wong–Zakai results show why smooth-noise approximations often produce a Stratonovich correction under their stated hypotheses .

Therefore a bare covariance
``` math
2D\delta(t-t')
```
does not encode the eliminated approximation scheme. An MTT derivation would have to retain enough source geometry to decide the limiting drift correction, not choose Ito or Stratonovich by convention after the fact.

# MTT interpretation and status

Projection can hide distinctions among upper configurations. If an ensemble or invariant state is supplied, those hidden distinctions can induce an effective stochastic kernel on the reduced variables. Three cautions are essential:

1.  Noninjective projection does not create a probability measure.

2.  A deterministic upper state with fully known initial data remains deterministic unless an ensemble, coarse-graining, or limit theorem is added.

3.  Finite memory can survive projection; white noise is a further scaling limit, not the definition of projected stochasticity.

The exact results in this paper establish a mathematically complete effective model:
``` math
\text{colored OU source}
\longrightarrow
\text{Brownian path limit}
\longrightarrow
\text{white-noise OU response}.
```
They do not yet establish that the selected q79 or other physical MTT carrier emits equation <a href="#eq:colored-ou" data-reference-type="eqref" data-reference="eq:colored-ou">[eq:colored-ou]</a>.

<div class="center">

| Status      | Result                                                        |
|:------------|:--------------------------------------------------------------|
| Exact       | Approximate-identity convergence to $`2D\delta_0`$            |
| Exact       | Positive-type guard for physical covariance data              |
| Exact       | Colored-OU convergence in $`C([0,T])`$                        |
| Exact       | Damped-response convergence to white-noise OU                 |
| Exact       | Finite-memory variance $`D/[\gamma(1+\gamma\tau)]`$           |
| Conditional | General mixing or deterministic upstream realization          |
| Open        | Selected physical MTT source and sector-specific coefficients |

</div>

# Completion program

To promote the effective construction into an MTT source theorem:

1.  select an upper state or preparation measure from the physical branch;

2.  derive a centered finite-memory observable $`\xi_\tau`$;

3.  prove positivity and normalization of its covariance;

4.  prove quantitative mixing or a martingale approximation;

5.  establish a functional limit with a computable error bound;

6.  prove closure of the intended resolved state;

7.  derive $`D`$, $`\tau`$, and $`\gamma`$ from the same source; and

8.  compare finite-memory corrections against an observable protocol.

This route can falsify the white-noise approximation. If the selected source has long memory, heavy tails, anomalous scaling, or no closed resolved state, the correct effective theory will not be the Markov OU model.

# Conclusion

White noise can be a rigorous zero-memory limit, but three levels must be kept apart. Normalized kernels may converge to a Dirac distribution. Valid covariances require positive type. Process and Markov convergence require law-level and path-level control.

The stationary colored-OU source supplies all of that control in one exact example. Its integrated forcing converges to Brownian motion in $`C([0,T])`$; its damped response converges to the standard OU diffusion; and its finite-memory variance tends monotonically to the white-noise floor. This shows precisely how finite memory can be compressed into delta correlation.

For MTT, the result is a reusable target, not a completed ontology. Projection may motivate unresolved effective forcing, but the source measure, memory kernel, mixing theorem, Markov closure, and coefficients still have to be selected from geometry. The credible claim is therefore not that randomness has been eliminated. It is that one exact route from finite-memory physics to an effective white-noise model has been constructed, with every additional MTT obligation visible.

<div class="thebibliography">

99

G. E. Uhlenbeck and L. S. Ornstein, *On the Theory of the Brownian Motion*, Physical Review **36** (1930) 823–841, doi:10.1103/PhysRev.36.823.

E. Wong and M. Zakai, *On the Relation Between Ordinary and Stochastic Differential Equations*, International Journal of Engineering Science **3** (1965) 213–229, doi:10.1016/0020-7225(65)90045-5.

</div>
