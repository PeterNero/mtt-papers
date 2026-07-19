---
abstract: |
  Dirac delta distributions appear throughout physics as identity kernels, point sources, constraint enforcers, measurement idealizations, gauge-fixing devices, and conservation laws at interaction vertices. Their ubiquity is usually treated as a technical feature of continuum mathematics. This paper isolates a structural explanation compatible with Modal Triplet Theory (MTT): a Dirac delta is the singular downstream limit of an admissible projection when finite-width selection, coherent-sector truncation, or representative choice is idealized to zero width.

  The mathematical core is deliberately narrow. We prove that spectral projection kernels on a compact elliptic setting converge to the Dirac delta in the distributional sense, and we record the corresponding heat-kernel approximate identity. These standard analytic facts provide the rigorous anchor for the MTT interpretation: the native object in a finite-capacity coherent regime is not the exact identity kernel $`\delta(x-y)`$, but a bounded coherent kernel $`K_{\mathrm{coh}}(x,y)`$ induced by a coherent projector $`\Pi_{\mathrm{coh}}`$. The delta is recovered only after an infinite-resolution or zero-width limit.

  We then apply this projection reading to Green kernels, canonical commutators, contact interactions, path-integral constraints, measurement, fixed-point basin selection, and gauge fixing. Gauge theory displays the same architecture explicitly: gauge freedom is uncollapsed projection redundancy, gauge fixing is local representative selection, the gauge-fixing delta is a singular section-selection kernel, and the Faddeev–Popov determinant is the projection Jacobian. The paper does not replace distribution theory, QFT, or gauge theory. It supplies a diagnostic principle: wherever a physical theory writes a Dirac delta, one should ask which finite admissible projection, filter, basin, or quotient operation has been idealized as exact.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: b4c52174f6664e90bbce3da9468e75aa629df11c2c912665a928a214afcb1606
paper_id: dirac-delta-functions-as-singular-shadows-of-admissible-6e0ddf3f
release_state: not_matched_to_zenodo
title: |
  Dirac Delta Functions as Singular Shadows of Admissible Projection  
  A Fixed-Point and Gauge-Theoretic Formulation in Modal Triplet Theory
---

*Part I of I in the Admissible Projection series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

# Purpose and claim discipline

The purpose of this paper is to isolate a recurring mathematical pattern in physical theories and reinterpret it through the projection-first architecture of MTT.

The recurring pattern is the Dirac delta. It appears as:

1.  the identity kernel $`\delta(x-y)`$;

2.  a point source $`\delta(x-x_0)`$;

3.  a hard constraint $`\delta(C[x])`$;

4.  a sharp measurement outcome;

5.  a gauge-fixing slice selector;

6.  a conservation law at interaction vertices;

7.  a spectral selector $`\delta(E-E_n)`$;

8.  a contact interaction or coincidence-limit singularity.

The central claim is structural:

<div class="center">

</div>

## Non-claims

This paper does not claim:

1.  that distribution theory is mathematically invalid;

2.  that ordinary QFT must be reformulated from scratch;

3.  that the coherent-kernel replacement is numerically evaluated here for all physical sectors;

4.  that every delta function has the same microscopic realization;

5.  that the proposed reading alone solves renormalization, measurement, or quantum gravity.

The narrower claim is:

> In any MTT-compatible effective description, a Dirac delta should be read as a singular encoding of a bounded projection, admissibility filter, survivor-basin selection, or representative-choice operation whenever that effective description arises by coherent truncation or quotienting.

## Working dictionary

The following dictionary states the intended use of the paper before the analytic details are introduced. The left column records a standard distributional device; the right column gives the corresponding projection-theoretic reading.

<div class="center">

| **Standard delta usage** | **Projection/admissibility reading** |
|:---|:---|
| $`\delta(x-y)`$ | Exact identity kernel; singular limit of a coherent identity kernel. |
| $`\delta(x-x_0)`$ | Point localization; zero-width limit of a finite survivor basin or source profile. |
| $`\delta(C[\phi])`$ | Hard constraint; zero-width limit of an admissibility filter. |
| $`\delta(G[A])`$ | Gauge-slice selector; singular representative choice in a quotient. |
| $`\delta(\sum_i p_i)`$ | Exact bookkeeping closure at a vertex; sharp limit of finite overlap conservation. |
| $`|x\rangle\langle x|`$ | Ideal measurement effect; zero-width limit of finite detector/coherence support. |

</div>

This table is not a proof. It is a map of the examples to which the proved kernel theorem will later be applied.

# Fixed-point backbone: projection before delta

The fixed-point framework supplies the analytic backbone for the present proposal. The basic structure is
``` math
\begin{equation}
T_t=\Pi_{\mathrm{coh}}\circ \Phi_t,
\end{equation}
```
where $`\Phi_t`$ is a smoothing or dissipative flow on the underlying modal configuration space and $`\Pi_{\mathrm{coh}}`$ is a bounded coherent projector onto the joint harmonic or coherent sector. The map $`T_t`$ is the projected evolution whose fixed points define stable coherent regimes.

If $`\Pi_{\mathrm{coh}}`$ admits an integral kernel $`K_{\mathrm{coh}}`$, then
``` math
\begin{equation}
(\Pi_{\mathrm{coh}}f)(x)=\int_X K_{\mathrm{coh}}(x,y)f(y)\,\mathrm{d}y.
\end{equation}
```
Standard continuum physics often uses instead
``` math
\begin{equation}
f(x)=\int_X \delta(x-y)f(y)\,\mathrm{d}y.
\end{equation}
```
The difference is the difference between a finite admissible identity and an ideal exact identity. The MTT replacement principle is therefore
``` math
\begin{equation}
\boxed{\delta(x-y)\quad\leadsto\quad K_{\mathrm{coh}}(x,y).}
\end{equation}
```

<div class="definition">

**Definition 1** (Finite coherent identity kernel). Let $`\Pi_{\mathrm{coh}}`$ be a bounded projection on a Hilbert space of fields over a domain $`X`$. If $`\Pi_{\mathrm{coh}}`$ is represented by a distributional or smooth kernel $`K_{\mathrm{coh}}(x,y)`$, then $`K_{\mathrm{coh}}`$ is called the finite coherent identity kernel of that effective regime. It acts as an identity only on $`\mathrm{Ran}(\Pi_{\mathrm{coh}})`$.

</div>

<div class="remark">

*Remark 2*. The phrase “identity kernel” is sector-relative. A finite coherent kernel need not be the identity on the full upstream function space. It is the identity on the retained admissible sector and a filter on everything else.

</div>

# Spectral gaps and finite width

The fixed-point framework assumes a positive spectral separation between coherent and incoherent sectors. In a standard elliptic model,
``` math
\begin{equation}
A|_{\mathrm{Ran}(Q)}\geq \lambda^\ast>0,\qquad Q=\mathrm{Id}-\Pi_{\mathrm{coh}}.
\end{equation}
```
This yields damping estimates of the form
``` math
\begin{equation}
\left\lVert A^{1/2}e^{-tA}Q \right\rVert\lesssim t^{-1/2}e^{-\lambda^\ast t}.
\end{equation}
```

The interpretation used below is:
``` math
\boxed{\text{finite spectral gap and finite damping margin imply finite projection width.}}
```
The delta limit corresponds to an idealization in which coherent projection becomes infinitely sharp. MTT does not begin with this sharpness. It begins with bounded projection, finite spectral separation, and controlled truncation.

A canonical model for the replacement is the heat kernel
``` math
\begin{equation}
H_\tau(x,y)\sim (4\pi \tau)^{-d/2}\exp\left(-\frac{\mathop{\mathrm{dist}}(x,y)^2}{4\tau}\right),
\end{equation}
```
with
``` math
\begin{equation}
\delta(x-y)=\lim_{\tau\downarrow 0}H_\tau(x,y)
\end{equation}
```
in the distributional sense.

# Spectral projection kernels and the Dirac delta

This section supplies the narrow mathematical anchor. The aim is not to prove that every occurrence of a Dirac delta in physics has the same origin. The aim is to prove the precise analytic statement that a Dirac delta arises as the distributional limit of increasingly complete projection kernels.

<div id="ass:compact-elliptic" class="assumption">

**Assumption 3** (Compact elliptic setting). Let $`(X,g)`$ be a compact smooth Riemannian manifold without boundary, or a compact domain with boundary equipped with a self-adjoint elliptic boundary condition. Let $`\Delta\geq 0`$ be a nonnegative Laplace-type operator on $`L^2(X)`$. Let
``` math
0\leq \lambda_0\leq \lambda_1\leq \lambda_2\leq \cdots
```
be its eigenvalues, repeated with multiplicity, and let $`\{\phi_n\}_{n=0}^\infty`$ be an orthonormal eigenbasis satisfying
``` math
\begin{equation}
\Delta \phi_n=\lambda_n\phi_n .
\end{equation}
```

</div>

For $`\Lambda>0`$, define the spectral projector
``` math
\begin{equation}
\Pi_\Lambda f=\sum_{\lambda_n\leq \Lambda}\left\langle \phi_n,\,f \right\rangle\phi_n .
\end{equation}
```
Its Schwartz kernel is
``` math
\begin{equation}
K_\Lambda(x,y)=\sum_{\lambda_n\leq \Lambda}\phi_n(x)\overline{\phi_n(y)} .
\end{equation}
```
Then
``` math
\begin{equation}
(\Pi_\Lambda f)(x)=\int_X K_\Lambda(x,y)f(y)\,\mathrm{d}\mathrm{vol}_g(y).
\end{equation}
```

<div id="thm:spectral-delta" class="theorem">

**Theorem 4** (Spectral projection kernels converge to the Dirac delta). *Under <a href="#ass:compact-elliptic" data-reference-type="ref+label" data-reference="ass:compact-elliptic">3</a>, for every $`f\in C^\infty(X)`$,
``` math
\begin{equation}
\lim_{\Lambda\to\infty}\int_X K_\Lambda(x,y)f(y)\,\mathrm{d}\mathrm{vol}_g(y)=f(x),
\end{equation}
```
with convergence in $`C^\infty(X)`$. Equivalently,
``` math
\begin{equation}
K_\Lambda(x,y)\longrightarrow \delta(x-y)
\end{equation}
```
in the sense of distributions on $`X\times X`$, where $`\delta(x-y)`$ denotes the kernel of the identity operator with respect to the Riemannian volume measure.*

</div>

<div class="proof">

*Proof.* By the spectral theorem, $`\{\phi_n\}`$ is a complete orthonormal basis of $`L^2(X)`$. Hence every $`f\in L^2(X)`$ has the expansion
``` math
f=\sum_{n=0}^{\infty} f_n\phi_n,\qquad f_n=\left\langle \phi_n,\,f \right\rangle,
```
with convergence in $`L^2`$. For $`f\in C^\infty(X)`$, elliptic regularity gives rapid decay of spectral coefficients: for every integer $`m\geq 0`$,
``` math
\begin{equation}
\sum_{n=0}^{\infty}(1+\lambda_n)^m|f_n|^2<\infty .
\end{equation}
```

The truncated projection is
``` math
\Pi_\Lambda f=\sum_{\lambda_n\leq \Lambda}f_n\phi_n,
```
so
``` math
f-\Pi_\Lambda f=\sum_{\lambda_n>\Lambda}f_n\phi_n.
```
For every Sobolev index $`s\geq 0`$,
``` math
\begin{equation}
\left\lVert f-\Pi_\Lambda f \right\rVert_{H^s}^2
=\sum_{\lambda_n>\Lambda}(1+\lambda_n)^s|f_n|^2 .
\end{equation}
```
The right-hand side tends to zero as $`\Lambda\to\infty`$, because $`f`$ is smooth and therefore has finite $`H^s`$-norm for every $`s`$. Hence $`\Pi_\Lambda f\to f`$ in all Sobolev norms. By Sobolev embedding, the convergence is in $`C^k`$ for every finite $`k`$. Therefore
``` math
\lim_{\Lambda\to\infty}(\Pi_\Lambda f)(x)=f(x)
```
smoothly in $`x`$.

Since
``` math
(\Pi_\Lambda f)(x)=\int_X K_\Lambda(x,y)f(y)\,\mathrm{d}\mathrm{vol}_g(y),
```
we obtain the stated convergence. This is precisely the distributional defining property of the Dirac delta kernel. Therefore $`K_\Lambda\to\delta`$ distributionally on $`X\times X`$. ◻

</div>

<div id="cor:finite-proj" class="corollary">

**Corollary 5** (Finite projection kernels are regularized deltas). *For finite $`\Lambda`$, $`K_\Lambda(x,y)`$ is a finite-rank smooth kernel. It acts as the identity on $`\mathrm{Ran}(\Pi_\Lambda)`$ and as a truncation on the full space. Thus $`K_\Lambda`$ is a finite-resolution identity kernel, while $`\delta(x-y)`$ is the infinite-bandwidth identity kernel.*

</div>

<div class="proof">

*Proof.* Finite-rank smoothness follows from the finite sum defining $`K_\Lambda`$. The identity property on $`\mathrm{Ran}(\Pi_\Lambda)`$ follows from idempotence: $`\Pi_\Lambda^2=\Pi_\Lambda`$. The limiting statement is <a href="#thm:spectral-delta" data-reference-type="ref+label" data-reference="thm:spectral-delta">4</a>. ◻

</div>

<div id="cor:mtt-reading" class="corollary">

**Corollary 6** (MTT reading). *If the coherent sector of an MTT fixed-point regime is represented by a bounded spectral projector $`\Pi_{\mathrm{coh}}`$, then its kernel
``` math
\begin{equation}
K_{\mathrm{coh}}(x,y)=\langle x|\Pi_{\mathrm{coh}}|y\rangle
\end{equation}
```
is the MTT-native replacement for the exact identity kernel $`\delta(x-y)`$ on that regime. The Dirac delta is recovered only when the coherent projection is idealized as complete, infinitely sharp, and free of finite-capacity remainder.*

</div>

<div class="remark">

*Remark 7*. <a href="#cor:mtt-reading" data-reference-type="ref+Label" data-reference="cor:mtt-reading">6</a> is interpretive rather than an additional analytic theorem. The analytic theorem is the distributional convergence of spectral projection kernels. The MTT claim is that physical deltas should be read through this projection structure whenever the relevant effective theory arises from coherent truncation.

</div>

<div class="center">

</div>

# Heat kernels as admissibility kernels

Spectral cutoffs are not the only regularized identity kernels. Heat kernels provide the smoothest and most physically useful model.

Let $`H_\tau(x,y)`$ be the heat kernel of $`\Delta`$:
``` math
\begin{equation}
e^{-\tau\Delta}f(x)=\int_X H_\tau(x,y)f(y)\,\mathrm{d}\mathrm{vol}_g(y).
\end{equation}
```
Spectrally,
``` math
\begin{equation}
H_\tau(x,y)=\sum_{n=0}^{\infty}e^{-\tau\lambda_n}\phi_n(x)\overline{\phi_n(y)}.
\end{equation}
```

<div id="thm:heat" class="theorem">

**Theorem 8** (Heat-kernel approximate identity). *For every $`f\in C^\infty(X)`$,
``` math
\begin{equation}
\lim_{\tau\downarrow 0}\int_X H_\tau(x,y)f(y)\,\mathrm{d}\mathrm{vol}_g(y)=f(x)
\end{equation}
```
in $`C^\infty(X)`$. Equivalently,
``` math
\begin{equation}
H_\tau(x,y)\to \delta(x-y)
\end{equation}
```
distributionally as $`\tau\downarrow 0`$.*

</div>

<div class="proof">

*Proof.* The heat semigroup $`e^{-\tau\Delta}`$ converges strongly to the identity on every Sobolev space $`H^s(X)`$. For smooth $`f`$, this convergence holds in all Sobolev norms and hence, by Sobolev embedding, in $`C^k`$ for every $`k`$. The kernel formulation gives the stated distributional convergence. ◻

</div>

<div class="remark">

*Remark 9* (Projection versus heat smoothing). A sharp spectral projector $`\Pi_\Lambda`$ gives a band-limited coherent identity. A heat kernel $`H_\tau`$ gives a soft coherent identity with exponential high-frequency suppression. Both converge to $`\delta`$ in singular limits. In MTT applications, heat/proper-time kernels are often more natural because finite damping and finite coherence capacity are represented by exponential suppression rather than a hard spectral wall.

</div>

# Inverse principle: delta as diagnostic

<div id="def:delta-diagnostic" class="definition">

**Definition 10** (Delta diagnostic). The delta diagnostic is the following rule: whenever a physical theory contains a Dirac delta, ask which finite projection, admissibility filter, survivor-basin selection, representative choice, or coherent identity kernel has been idealized to zero width.

</div>

This principle does not deny standard calculations. It identifies where the calculation has hidden a projection step.

<div class="example">

**Example 11** (Green kernel). The equation
``` math
\begin{equation}
LG(x,y)=\delta(x-y)
\end{equation}
```
states that $`G`$ is the response to a perfectly localized source. The coherent replacement is
``` math
\begin{equation}
LG_{\mathrm{coh}}(x,y)=K_{\mathrm{coh}}(x,y).
\end{equation}
```
Thus the point source is replaced by an admissibly localized source.

</div>

<div class="example">

**Example 12** (Canonical commutator). The standard equal-time relation
``` math
\begin{equation}
[\phi(t,x),\pi(t,y)]=i\hbar\delta(x-y)
\end{equation}
```
is replaced, in a projected coherent sector, by
``` math
\begin{equation}
[\phi_{\mathrm{coh}}(t,x),\pi_{\mathrm{coh}}(t,y)]
=i\hbar K_{\mathrm{coh}}(x,y).
\end{equation}
```
Locality is not destroyed. It becomes coherent-sector-local rather than infinitely sharp.

</div>

# Fixed points and delta concentration

In ordinary dynamical systems, convergence to a stable fixed point is often represented distributionally as
``` math
\begin{equation}
\rho_t\to \delta_{x_\ast}.
\end{equation}
```
In MTT this should be refined. A fixed point $`\Psi_\ast`$ of
``` math
\begin{equation}
T_t=\Pi_{\mathrm{coh}}\circ\Phi_t
\end{equation}
```
is the center of a stabilized coherent basin, not necessarily a literal zero-width state of the full upstream dynamics.

The MTT-native statement is
``` math
\begin{equation}
\rho_t\to \rho_{\mathrm{basin},\Psi_\ast},
\end{equation}
```
where $`\rho_{\mathrm{basin},\Psi_\ast}`$ has finite width determined by projection resolution, damping margins, disturbance floors, and the size of the basin of attraction. The delta appears only in the singular limit:
``` math
\begin{equation}
\rho_{\mathrm{basin},\Psi_\ast}\to\delta_{\Psi_\ast}.
\end{equation}
```

<div id="prop:fixed-delta" class="proposition">

**Proposition 13** (Projected fixed-point delta). *Suppose an admissible projected dynamics $`T_t`$ has an attracting fixed point $`\Psi_\ast`$ with a basin whose effective distribution at time $`t`$ is $`\rho_t`$. If $`\rho_t`$ converges weakly to a probability measure $`\rho_\ast`$ supported in a finite coherent basin $`B_\ast`$, then the notation $`\rho_t\to\delta_{\Psi_\ast}`$ is valid only after the further idealization that $`B_\ast`$ has zero effective width.*

</div>

<div class="proof">

*Proof.* Weak convergence to $`\delta_{\Psi_\ast}`$ means that all continuous test observables take the value associated with the single point $`\Psi_\ast`$. If the limiting measure is supported on a finite basin $`B_\ast`$, then observables that vary across $`B_\ast`$ distinguish $`\rho_\ast`$ from $`\delta_{\Psi_\ast}`$. The delta notation is therefore justified only when the retained observable algebra cannot resolve the basin width, or in the additional zero-width limit. ◻

</div>

# Disturbance–damping balance and nonzero width

The fixed-point disturbance analysis supports the finite-width replacement. For a non-harmonic mode with damping margin $`\gamma_{n,k}>0`$ and disturbance strength $`\delta_{n,k}`$, the Ornstein–Uhlenbeck regime gives
``` math
\begin{equation}
\sigma^2_{n,k}=\frac{\delta_{n,k}}{2\gamma_{n,k}}.
\end{equation}
```
Thus exact delta collapse requires either
``` math
\begin{equation}
\delta_{n,k}\to 0
\end{equation}
```
or
``` math
\begin{equation}
\gamma_{n,k}\to\infty.
\end{equation}
```
Neither is generic in finite-capacity MTT. A Gaussian model for the finite stabilized kernel is
``` math
\begin{equation}
K_{\gamma,\delta}(x,x_0)\sim
\exp\left[-\frac{(x-x_0)^2}{2\sigma^2}\right],
\qquad
\sigma^2=\frac{\delta}{2\gamma}.
\end{equation}
```

# Gauge as uncollapsed projection; delta as collapsed projection

Gauge theory provides the clearest standard example of the same architecture.

Let $`\mathcal A`$ be a space of gauge fields and $`\mathcal G`$ the gauge group. The physical configuration space is the quotient
``` math
\begin{equation}
\mathcal A/\mathcal G.
\end{equation}
```
The projection
``` math
\begin{equation}
\mathcal A\to\mathcal A/\mathcal G
\end{equation}
```
is many-to-one. Gauge freedom is the visible persistence of that non-injectivity:
``` math
\boxed{\text{gauge freedom}=\text{uncollapsed projection redundancy}.}
```
In MTT language, this is lens structure.

Gauge fixing imposes a condition
``` math
\begin{equation}
G[A]=0.
\end{equation}
```
This selects a representative slice through each gauge orbit. The Faddeev–Popov identity has the formal form
``` math
\begin{equation}
1=\Delta_{\mathrm{FP}}[A]\int \mathcal D\alpha\,
\delta(G[A^\alpha]).
\end{equation}
```
Here $`A^\alpha`$ parameterizes a gauge orbit, $`\delta(G[A^\alpha])`$ selects the slice, and $`\Delta_{\mathrm{FP}}`$ corrects the quotient measure.

<div id="prop:fp" class="proposition">

**Proposition 14** (Faddeev–Popov determinant as projection Jacobian). *Assume a local gauge slice $`G[A]=0`$ intersects gauge orbits transversely near $`A`$. Then the Faddeev–Popov factor
``` math
\begin{equation}
\Delta_{\mathrm{FP}}[A]
=\left|\det D_\alpha(G[A^\alpha])\right|
\end{equation}
```
is the Jacobian of the projection from orbit coordinates to the chosen local slice.*

</div>

<div class="proof">

*Proof.* Locally decompose a neighborhood of $`A`$ into coordinates $`(s,\alpha)`$, where $`s`$ parametrizes the gauge slice and $`\alpha`$ parametrizes the gauge orbit. The gauge condition maps orbit coordinates to the constraint value $`G[A^\alpha]`$. If the intersection is transverse, $`D_\alpha G[A^\alpha]`$ is invertible in the orbit directions. The standard change-of-variables formula then contributes the absolute determinant $`\left|\det D_\alpha(G[A^\alpha])\right|`$, which is precisely the Faddeev–Popov factor. ◻

</div>

Thus:
``` math
\boxed{\delta(G[A])=\text{singular shadow of representative selection},}
```
and
``` math
\boxed{\Delta_{\mathrm{FP}}[A]=\text{projection Jacobian}.}
```

## Ghosts as quotient bookkeeping

The determinant may be represented by ghost fields:
``` math
\begin{equation}
\Delta_{\mathrm{FP}}[A]=
\int \mathcal D\bar c\,\mathcal Dc\,e^{iS_{\mathrm{ghost}}[\bar c,c,A]}.
\end{equation}
```
In MTT terms:
``` math
\boxed{\text{ghosts encode the local measure cost of quotienting lens redundancy}.}
```
They are not physical particles in the ordinary sense. They are bookkeeping fields for the projection Jacobian.

## Gribov copies

Gauge fixing may fail globally. A gauge slice may intersect one orbit multiple times. These are Gribov copies. In MTT language:
``` math
\boxed{\text{Gribov copies}=\text{failure of global admissible section}.}
```
This matches the MTT principle that reduced descriptions are local encodings, not globally valid ontologies.

## BRST

BRST symmetry algebraically controls the quotient:
``` math
\begin{equation}
Q_{\mathrm{BRST}}^2=0,\qquad
\mathcal H_{\mathrm{phys}}=\ker Q_{\mathrm{BRST}}/\mathop{\mathrm{im}}Q_{\mathrm{BRST}}.
\end{equation}
```
MTT reading:
``` math
\boxed{\text{physical states}=\text{admissible quotient classes modulo null redundancy}.}
```

# Path integrals and admissibility filters

Path integrals often impose constraints using hard deltas:
``` math
\begin{equation}
Z=\int \mathcal D\phi\,\delta(C[\phi])e^{iS[\phi]/\hbar}.
\end{equation}
```
MTT replaces this with a finite admissibility kernel:
``` math
\begin{equation}
\delta(C[\phi])\quad\leadsto\quad \mathcal K_{\mathrm{adm}}[C[\phi]].
\end{equation}
```
A standard Gaussian model is
``` math
\begin{equation}
\mathcal K_{\mathrm{adm}}[C]
=\exp\left(-\frac{1}{2\epsilon_{\mathrm{adm}}^2}\left\lVert C \right\rVert^2\right).
\end{equation}
```
Thus
``` math
\begin{equation}
Z_{\mathrm{MTT}}=
\int \mathcal D\phi\,
\exp\left(\frac{i}{\hbar}S[\phi]
-\frac{1}{2\epsilon_{\mathrm{adm}}^2}\left\lVert C[\phi] \right\rVert^2\right).
\end{equation}
```
The hard delta is recovered as
``` math
\begin{equation}
\delta(C)=\lim_{\epsilon_{\mathrm{adm}}\to 0}\mathcal K_{\mathrm{adm}}[C].
\end{equation}
```

# Measurement as finite survivor-basin selection

An ideal position measurement uses projectors
``` math
\begin{equation}
P_x=|x\rangle\langle x|,
\end{equation}
```
with distributional kernel
``` math
\begin{equation}
\langle y|P_x|z\rangle=\delta(y-x)\delta(z-x).
\end{equation}
```
MTT replaces this with a finite coherent effect:
``` math
\begin{equation}
E_x^{\mathrm{coh}}(y,z)
=K_{\mathrm{coh}}(y,x)\overline{K_{\mathrm{coh}}(z,x)}.
\end{equation}
```
The probability becomes
``` math
\begin{equation}
p(x)=\langle \psi|E_x^{\mathrm{coh}}|\psi\rangle.
\end{equation}
```
The post-measurement state is not a point delta but a stabilized survivor basin:
``` math
\begin{equation}
\psi\mapsto \frac{M_x^{\mathrm{coh}}\psi}{\left\lVert M_x^{\mathrm{coh}}\psi \right\rVert}.
\end{equation}
```
Thus:
``` math
\boxed{\text{measurement collapse}=\text{finite basin selection idealized as delta collapse}.}
```

# QFT applications

## Green functions

Standard:
``` math
\begin{equation}
LG(x,y)=\delta(x-y).
\end{equation}
```
MTT-coherent:
``` math
\begin{equation}
LG_{\mathrm{coh}}(x,y)=K_{\mathrm{coh}}(x,y).
\end{equation}
```

## Contact interactions

A local interaction such as $`\lambda\phi^4(x)`$ can be written as a zero-width overlap. The coherent replacement is
``` math
\begin{equation}
\lambda\int dx_1\cdots dx_4\,
V_{\mathrm{coh}}(x_1,x_2,x_3,x_4)
\phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4),
\end{equation}
```
where
``` math
\begin{equation}
V_{\mathrm{coh}}\sim
\int dx\,K_{\mathrm{coh}}(x,x_1)K_{\mathrm{coh}}(x,x_2)
K_{\mathrm{coh}}(x,x_3)K_{\mathrm{coh}}(x,x_4).
\end{equation}
```
Point-local interaction is the zero-width limit of coherent overlap.

## Momentum conservation deltas

At a standard vertex,
``` math
\begin{equation}
(2\pi)^4\delta^{(4)}\left(\sum_i p_i\right)
\end{equation}
```
enforces exact bookkeeping closure. MTT reads this as the sharp limit of an overlap-conservation kernel:
``` math
\begin{equation}
\delta^{(4)}\left(\sum_i p_i\right)
\quad\leadsto\quad
K_{\mathrm{book}}\left(\sum_i p_i\right),
\end{equation}
```
where $`K_{\mathrm{book}}`$ has width determined by coherent-sector resolution and finite interaction support.

# Renormalization as repair of over-sharp projection

Many ultraviolet divergences arise from products or limits of distributions at coincident points:
``` math
\begin{equation}
\delta(x-x),\qquad G(x,x),\qquad \phi^n(x)\text{ at one point}.
\end{equation}
```
The MTT interpretation is:

<div class="center">

</div>

Renormalization then becomes, at least in part, the downstream repair mechanism required after over-sharp projection. This does not eliminate renormalization. It explains why renormalization appears exactly where the idealized continuum theory compresses admissible overlap structure into pointlike coincidence.

# Triadic placement: circle, lens, nil

The proto-spinor carrier
``` math
\begin{equation}
\Xi=(\Psi,C,L,N)
\end{equation}
```
provides a useful classification.

<div class="center">

| Carrier role | Delta/gauge interpretation |
|:---|:---|
| $`C`$: circle bookkeeping | phase, return, conservation kernels |
| $`L`$: lens redundancy | gauge freedom, equivalence classes, quotienting |
| $`N`$: nil survivorship | selection, thresholds, collapse, discrete outcomes |

</div>

Thus:
``` math
\begin{equation}
\text{gauge}\subset L,\qquad
\delta\text{-selection}\subset N,\qquad
\text{conservation deltas}\subset C.
\end{equation}
```
More carefully, delta functions can appear as singular shadows in all three sectors: circle deltas enforce exact return/bookkeeping closure; lens deltas enforce representative selection in a redundancy class; nil deltas enforce survivor selection at a threshold.

# Diagnostics and possible finite-width effects

The preceding sections do not by themselves compute new numerical predictions. They identify where finite-width corrections would enter if a delta idealization is replaced by an admissible kernel. The following are the most concrete diagnostic directions.

1.  **UV-softened contact interactions.** A point interaction or local monomial such as $`\lambda\phi^4(x)`$ can be replaced by a finite overlap vertex. The leading diagnostic is suppression of coincident-point divergences or a controlled modification of high-momentum behavior.

2.  **Coherent Green functions.** The equation $`LG=\delta`$ is replaced by $`LG_{\mathrm{coh}}=K_{\mathrm{coh}}`$. This gives a direct worked sequel: compute how a finite coherent source changes the near-source behavior of a Green function while preserving the ordinary solution outside the kernel width.

3.  **Finite detector-resolution collapse.** Ideal projectors $`|x\rangle\langle x|`$ are replaced by positive finite effects $`E_x^{\mathrm{coh}}`$. The diagnostic is a nonzero stabilization width rather than exact delta collapse, with the width controlled by damping and disturbance scales.

4.  **Gauge-fixing tubes instead of exact slices.** The hard factor $`\delta(G[A])`$ can be softened to a tube around the gauge slice. The diagnostic is sensitivity to the width of representative selection, especially near Gribov horizons where the projection Jacobian degenerates.

5.  **Spectral peaks as finite basins.** A spectral line written as $`\delta(E-E_n)`$ is the infinite-lifetime limit of a finite-width stable mode. MTT suggests reading linewidths as basin-width or disturbance–damping data rather than merely as external broadening.

These diagnostics provide the transition from the present foundation paper to concrete worked examples. The first technically clean target is the coherent Green-function problem: replace a point source by a bounded projection kernel and compare the resulting solution to the ordinary distributional Green function.

# Research program

The practical method is:

1.  Locate every Dirac delta in a physical formulation.

2.  Classify its role: identity, source, constraint, representative selection, conservation, measurement, or spectral selection.

3.  Identify the corresponding MTT structure: coherent kernel, admissibility filter, basin kernel, lens quotient, circle bookkeeping, or nil selection.

4.  Replace the delta with a bounded kernel.

5.  Study the corrections induced by finite width.

The highest-priority targets are:

1.  canonical commutators;

2.  propagators;

3.  gauge fixing and Faddeev–Popov determinants;

4.  measurement projectors;

5.  path-integral constraints;

6.  point-particle sources in GR and QFT;

7.  contact interactions and UV divergences;

8.  spectral delta peaks and finite-lifetime resonances.

# Conclusion

The Dirac delta is one of the most ubiquitous mathematical objects in physics. In standard usage it implements identity, localization, constraint, conservation, or selection. In MTT these roles share a common structural origin: each is a downstream idealization of projection under finite admissibility.

The fixed-point framework supplies the analytic core. Coherent projection is bounded; smoothing suppresses incoherent modes; spectral gaps control resolution; disturbance–damping balance leaves finite width; projected fixed points represent stabilized coherent basins. The literal Dirac delta appears only when this finite structure is idealized to zero width.

Gauge theory confirms the same pattern from another direction. Gauge freedom records uncollapsed projection redundancy; gauge fixing imposes representative selection; the Faddeev–Popov determinant is the projection Jacobian; ghosts encode quotient-measure bookkeeping; Gribov ambiguities mark global section failure.

The central principle is:
``` math
\boxed{\text{Every Dirac delta is a diagnostic of hidden projection.}}
```
Where standard physics writes $`\delta`$, MTT asks what bounded coherent kernel, admissibility filter, survivor basin, or gauge-section selection has been collapsed into singular notation.
