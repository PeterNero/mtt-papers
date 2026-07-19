---
abstract: |
  Delta functions appear in stochastic physics most visibly through white-noise correlations,
  ``` math
  \langle \xi(t)\xi(t')\rangle = 2D\,\delta(t-t'),
  ```
  and through Markov transition kernels that collapse memory into instantaneous updates. This paper develops the stochastic sequel to the delta-projection program in Modal Triplet Theory (MTT). The main mathematical point is simple but structurally important: white noise is the zero-correlation-time limit of finite-memory colored disturbances. Thus temporal delta correlations are not primitive randomness; they are singular limits of bounded correlation kernels.

  We prove that standard families of finite-memory covariance kernels converge distributionally to Dirac deltas, derive the Ornstein–Uhlenbeck white-noise model as a Markov limit of colored disturbance models, and separate three notions that are often conflated: deterministic upstream evolution, stochastic projected description, and white-noise idealization. In the MTT interpretation, finite disturbances are filtered through the evolve–project cycle; damping suppresses noncoherent modes, while persistent disturbance produces a finite OU floor. The delta-correlated noise model is recovered only when the disturbance correlation time is idealized to zero relative to the coherent timescale.

  The conclusion is that white noise is the stochastic analogue of the point source, gauge-fixing delta, projective measurement, contact vertex, conservation delta, and spectral peak studied earlier in this series. It is the singular shadow of a finite admissible process: here, finite-memory disturbance compressed into instantaneous correlation.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: c79f18f7635efde97728c2da7899ff76ed9e4e35987cc1407bfbe34aa5f7dd47
paper_id: white-noise-and-markov-limits-as-delta-correlation-idea-854be499
release_state: not_matched_to_zenodo
title: |
  White Noise and Markov Limits as Delta-Correlation Idealizations  
  Finite Memory, Colored Disturbances, and OU Floors in Modal Triplet Theory
---

# Purpose and Claim Discipline

The purpose of this paper is to extend the delta-projection program to stochastic descriptions. In many effective theories, unresolved degrees of freedom are represented by noise terms. The most common idealization is white noise:
``` math
\mathbb E[\xi(t)\xi(t')] = 2D\,\delta(t-t').
```
This expression is mathematically useful, but it is not an ordinary function. It represents a singular process with zero correlation time and unbounded pointwise variance.

The central claim of this paper is:
``` math
\boxed{\text{white noise is the zero-memory limit of finite-correlation disturbance}.}
```

In MTT language:
``` math
\boxed{\delta(t-t')=\text{singular shadow of finite-memory projected disturbance}.}
```

## Non-claims

We do not claim:

1.  that stochastic differential equations are invalid;

2.  that white noise is never useful;

3.  that all effective randomness has the same microscopic origin;

4.  that this paper derives the Born rule or all projected stochasticity from MTT;

5.  that the finite-memory kernel is computed here from a specific carrier geometry.

The narrower claim is that delta-correlated noise should be read as an idealization: the finite correlation structure of unresolved disturbances has been collapsed to zero temporal width.

<div class="center">

| Layer | Role in this paper |
|:---|:---|
| Mathematical core | Approximate-identity covariance kernels converge to temporal Dirac deltas. |
| Standard stochastic model | White-noise OU dynamics is obtained as a zero-memory limit of colored disturbance. |
| MTT interpretation | Projection can erase retained memory, and the white-noise delta is the sharp notation for that erasure. |
| Non-claim | Not every stochastic process is derived here from MTT, and not every colored kernel is physically admissible. |

</div>

# Finite-Memory Covariance Kernels

Let $`C_\tau(t)`$ be a family of even, nonnegative covariance kernels on $`\mathbb R`$, with correlation time $`\tau>0`$, normalized by
``` math
\int_{-\infty}^{\infty} C_\tau(t)\,dt = 2D .
```
A standard example is the exponential kernel
``` math
C_\tau(t)=\frac{D}{\tau}e^{-|t|/\tau}.
```
Another is the Gaussian kernel
``` math
C_\tau(t)=\frac{2D}{\sqrt{2\pi}\tau}\exp\!\left(-\frac{t^2}{2\tau^2}\right).
```
Both have total integrated covariance $`2D`$. The parameter $`\tau`$ is the finite memory scale. White noise is obtained only when $`\tau\downarrow 0`$.

# The Delta-Correlation Limit

<div class="theorem">

**Theorem 1** (Finite-memory kernels converge to a temporal delta). *Let $`C_\tau(t)`$ be an approximate-identity family satisfying:*

1.  *$`C_\tau(t)\ge 0`$;*

2.  *$`\int_{\mathbb R} C_\tau(t)\,dt=2D`$;*

3.  *for every $`\epsilon>0`$,
    ``` math
    \int_{|t|>\epsilon} C_\tau(t)\,dt\to 0
    \qquad\text{as }\tau\downarrow 0 .
    ```*

*Then
``` math
C_\tau(t)\to 2D\,\delta(t)
```
in the sense of distributions. Equivalently, for every test function $`f\in C_c^\infty(\mathbb R)`$,
``` math
\lim_{\tau\downarrow 0}\int_{\mathbb R} C_\tau(t)f(t)\,dt=2D f(0).
```*

</div>

<div class="proof">

*Proof.* Write
``` math
\int C_\tau(t)f(t)\,dt-2Df(0)
=
\int C_\tau(t)(f(t)-f(0))\,dt.
```
Fix $`\epsilon>0`$. Since $`f`$ is continuous, choose $`\epsilon`$ so that $`|f(t)-f(0)|<\eta`$ for $`|t|<\epsilon`$. Then
``` math
\left|\int_{|t|<\epsilon} C_\tau(t)(f(t)-f(0))\,dt\right|
\le 2D\eta .
```
On the complement, $`|f(t)-f(0)|\le 2\|f\|_\infty`$, hence
``` math
\left|\int_{|t|>\epsilon} C_\tau(t)(f(t)-f(0))\,dt\right|
\le 2\|f\|_\infty\int_{|t|>\epsilon}C_\tau(t)\,dt,
```
which tends to zero by assumption. Since $`\eta`$ is arbitrary, the result follows. ◻

</div>

<div class="corollary">

**Corollary 2** (Exponential covariance gives white noise in the zero-memory limit). *For
``` math
C_\tau(t)=\frac{D}{\tau}e^{-|t|/\tau},
```
one has
``` math
C_\tau(t)\to 2D\,\delta(t)
```
distributionally as $`\tau\downarrow 0`$.*

</div>

<div class="proof">

*Proof.* The kernel is nonnegative, has total integral $`2D`$, and its mass outside any fixed neighborhood of the origin decays exponentially:
``` math
\int_{|t|>\epsilon}\frac{D}{\tau}e^{-|t|/\tau}\,dt
=2D e^{-\epsilon/\tau}\to0.
```
 ◻

</div>

# Colored Noise Before White Noise

A finite-memory disturbance $`\xi_\tau(t)`$ is modeled by
``` math
\mathbb E[\xi_\tau(t)]=0,
\qquad
\mathbb E[\xi_\tau(t)\xi_\tau(t')]=C_\tau(t-t').
```
For finite $`\tau`$, this process is colored: nearby times are correlated. The white-noise model is the singular limit
``` math
\mathbb E[\xi(t)\xi(t')]=2D\,\delta(t-t').
```

Thus the delta correlation does not mean the physical disturbance has no structure. It means the effective description has discarded the structure because the correlation time is treated as negligible compared with the resolved timescale.

``` math
\boxed{
\text{white noise}=
\text{finite-memory disturbance viewed below its memory scale}.
}
```

## Explicit exponential colored-noise model

A standard finite-memory covariance is
``` math
C_\tau(t)=\frac{D}{\tau}e^{-|t|/\tau}.
```
It has total weight
``` math
\int_{-\infty}^{\infty}C_\tau(t)\,dt=2D
```
and therefore converges, in the sense of distributions, to
``` math
C_\tau(t)\longrightarrow 2D\,\delta(t)
```
as $`\tau\downarrow0`$. Its Fourier transform is
``` math
\widehat C_\tau(\omega)=\frac{2D}{1+\omega^2\tau^2},
```
which tends pointwise to the flat white-noise spectrum $`2D`$. This model makes explicit that white noise is not a separate primitive object; it is the limit in which a finite correlation time is collapsed.

<div class="remark">

*Remark 3* (Normalization). Some authors write the white-noise covariance as $`D\delta(t-t')`$ instead of $`2D\delta(t-t')`$. The factor of $`2`$ is a convention tied to the standard OU normalization. Nothing in the argument depends on this convention.

</div>

# OU Dynamics and the Disturbance–Damping Floor

The fixed-point disturbance analysis in MTT uses precisely the structure that makes this paper natural: noncoherent modes are damped, but persistent disturbances can maintain a finite residual width.

Consider the scalar mode equation
``` math
\dot a(t)=-\gamma a(t)+\xi(t),
\qquad \gamma>0,
```
with white noise covariance
``` math
\mathbb E[\xi(t)\xi(t')]=2D\,\delta(t-t').
```
This is the Ornstein–Uhlenbeck model. Its stationary variance is
``` math
\operatorname{Var}(a)=\frac{D}{\gamma}.
```

If instead the disturbance has finite correlation time,
``` math
\mathbb E[\xi_\tau(t)\xi_\tau(t')]=C_\tau(t-t'),
```
then the stationary variance is
``` math
\operatorname{Var}_\tau(a)
=
\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}
\frac{\widehat C_\tau(\omega)}{\gamma^2+\omega^2}.
```
For the exponential covariance above,
``` math
C_\tau(t)=\frac{D}{\tau}e^{-|t|/\tau},
\qquad
\widehat C_\tau(\omega)=\frac{2D}{1+\omega^2\tau^2}.
```
Hence
``` math
\operatorname{Var}_\tau(a)
=
\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}
\frac{2D}{(1+\omega^2\tau^2)(\gamma^2+\omega^2)}.
```
Evaluating the elementary contour integral gives
``` math
\operatorname{Var}_\tau(a)
=
\frac{D}{\gamma(1+\gamma\tau)}.
```
Therefore
``` math
\operatorname{Var}_\tau(a)\to \frac{D}{\gamma}
```
as $`\tau\downarrow0`$. Finite memory lowers the effective variance in this particular model because high-frequency disturbance power is not yet flat.

<div class="remark">

*Remark 4*. The exact finite-$`\tau`$ value depends on the colored-noise model. The robust structural point is the limit: finite-memory disturbance converges to the OU white-noise floor when the memory time is collapsed relative to the damping timescale.

</div>

## Connection to finite survivor-basin width

In the fixed-point interpretation, damping does not by itself imply a point outcome. Persistent disturbance leaves a residual width. For a single damped mode, the white-noise idealization gives
``` math
\sigma^2=\frac{D}{\gamma},
```
while the exponential colored model gives
``` math
\sigma_\tau^2=\frac{D}{\gamma(1+\gamma\tau)}.
```
Thus finite memory, finite damping, and finite disturbance power together define a nonzero basin width. The delta limit appears only when the memory kernel is collapsed and the remaining width is then further idealized away.

# Markov Limits

White noise is closely tied to Markovian effective dynamics, but the implication is not automatic. A delta covariance is one ingredient in a Markov idealization; one also needs compatible drift, closure of the resolved variables, and no retained hidden memory variables. A process with memory is generally non-Markovian when viewed only through the resolved variable. Markovianity emerges only when the relevant memory kernel collapses and the reduced state is closed under the effective dynamics.

A schematic generalized Langevin equation is
``` math
\dot x(t)
=
-\int_0^t M_\tau(t-s)x(s)\,ds+\eta_\tau(t),
```
where $`M_\tau`$ is a finite-memory friction kernel and $`\eta_\tau`$ is a correlated disturbance. If
``` math
M_\tau(t)\to 2\gamma\delta(t),
```
then formally
``` math
\dot x(t)=-\gamma x(t)+\eta(t),
```
with instantaneous damping and white-noise forcing.

Thus:
``` math
\boxed{
\text{Markov dynamics}=
\text{zero-memory limit of finite-memory projected dynamics}.
}
```

This is the stochastic analogue of earlier results in the series:
``` math
\text{point source} \leftrightarrow \text{zero spatial width},
```
``` math
\text{S-matrix delta} \leftrightarrow \text{infinite time support},
```
``` math
\text{white noise} \leftrightarrow \text{zero memory width}.
```

# MTT Interpretation

In MTT, effective stochasticity arises because projection is generally non-invertible. Distinct upstream configurations can share the same coherent projection while differing in discarded noncoherent content. When the projected description does not retain those distinctions, their residual influence may appear as stochastic disturbance.

The delta-correlation idealization is a further step. It says not only that the unresolved content has been projected away, but that its temporal correlations are neglected.

``` math
\boxed{
\text{projection-induced stochasticity}
\neq
\text{white-noise idealization}.
}
```

Projection-induced stochasticity can be structured, biased, finite-memory, and constrained by admissibility. White noise is the special limit in which the residual memory scale is sent to zero.

## Relation to the fixed-point series

The fixed-point framework supplies three ingredients:

1.  coherent projection $`\Pi_{\mathrm{coh}}`$;

2.  damping of noncoherent modes through spectral gaps;

3.  finite disturbance–damping balance producing OU-type floors.

Therefore the MTT-native object is not necessarily a white-noise process. It is a finite-memory disturbance filtered by damping and projection. White noise appears only after idealizing the disturbance memory as negligible.

``` math
\boxed{
\delta(t-t')=
\text{zero-memory shadow of finite admissible disturbance}.
}
```

# Itô, Stratonovich, and Model Dependence

When colored noise is replaced by white noise in nonlinear equations, different limiting procedures can yield different stochastic calculi, most famously Itô or Stratonovich. This matters because the white-noise limit is singular.

The present paper does not choose a universal calculus. Instead it states a structural warning:

``` math
\boxed{
\text{the finite-memory model matters before the white-noise limit is taken}.
}
```

In MTT terms, the admissible kernel and projection mechanism determine the correct limiting rule. A bare delta correlation does not contain enough information to reconstruct the eliminated finite-memory structure.

# Fluctuation–Dissipation Caveat

In thermal equilibrium, noise and damping are not independent: they are related by fluctuation–dissipation conditions. In such cases a covariance kernel $`C_\tau`$ cannot be chosen arbitrarily. It must be paired with a compatible dissipation kernel. For a generalized Langevin equation, the same bath structure that produces colored disturbance also produces memory-dependent friction.

This caveat strengthens rather than weakens the projection interpretation. It means admissible disturbance kernels must respect the bookkeeping of the effective sector. A finite kernel is not merely a regulator; it is part of a constrained effective description.

The present paper therefore does not claim that one may replace white noise by any convenient colored kernel while preserving the same physics. The admissible replacement must preserve the relevant equilibrium, positivity, causality, and fluctuation–dissipation data of the regime under study.

# Examples of Delta-Correlation Idealization

<div class="center">

| Standard delta object | Finite-memory replacement | Interpretation |
|:---|:---|:---|
| $`\langle\xi(t)\xi(t')\rangle=2D\delta(t-t')`$ | $`C_\tau(t-t')`$ | colored disturbance |
| Markov update | memory kernel | unresolved history retained finitely |
| OU white-noise floor | colored-noise floor | finite disturbance timescale |
| Brownian motion | correlated random walk | zero-step-time limit |
| white thermal bath | finite-band bath | bath memory neglected |

</div>

# Scope of Proof

<div class="center">

| Status | Statement |
|:---|:---|
| Proved | Approximate-identity covariance kernels converge distributionally to temporal deltas. |
| Proved | Exponential and Gaussian finite-memory kernels yield white-noise covariance in the zero-memory limit. |
| Computed | The exponential colored-noise OU model gives $`\sigma_\tau^2=D/[\gamma(1+\gamma\tau)]`$, tending to $`D/\gamma`$. |
| Standard model result | OU stationary variance arises from balancing damping against disturbance power. |
| Caveat | White noise alone does not guarantee a Markov process; closure of the reduced variables is also required. |
| Interpreted | In MTT, white noise is the zero-memory shadow of finite admissible disturbance. |
| Not proved here | A derivation of every effective stochastic kernel from the full MTT carrier dynamics. |

</div>

# Conclusion

White noise is one of the most common uses of the Dirac delta in physics. It says that unresolved disturbances are correlated only at exactly equal times:
``` math
\mathbb E[\xi(t)\xi(t')]=2D\delta(t-t').
```
The analysis here shows that this is the singular limit of a finite-memory covariance kernel.

In the delta-projection program, this completes another major class of delta functions. A point source is a zero-width spatial source. A gauge-fixing delta is a zero-width representative selector. A projective measurement is a zero-width outcome effect. A contact vertex is a zero-width overlap. A conservation delta is an infinite-support bookkeeping limit. A spectral delta peak is an infinite-lifetime mode. White noise is the zero-memory limit of finite disturbance.

The MTT lesson is therefore:
``` math
\boxed{
\text{delta-correlated randomness is not primitive randomness;}
}
```
it is the singular notation used when finite-memory projected disturbance is compressed into instantaneous correlation.
