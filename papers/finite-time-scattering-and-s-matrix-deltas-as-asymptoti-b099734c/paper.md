---
abstract: |
  The exact energy–momentum conserving delta functions of the scattering matrix,
  ``` math
  (2\pi)^4\delta^{(4)}(p_f-p_i),
  ```
  are usually introduced as consequences of translation invariance and asymptotic scattering theory. This paper continues the sequence interpreting Dirac deltas as singular shadows of admissible projection. The previous bookkeeping paper showed that momentum-conservation deltas arise as infinite-support limits of finite interaction-window Fourier kernels. Here we focus on scattering itself: finite-time transition amplitudes do not produce exact energy deltas, but finite-width sinc or window kernels. The exact S-matrix delta appears only after the asymptotic idealization of infinite observation time, infinite spatial support, and stable in/out sectors.

  We prove a standard finite-time transition theorem: for a constant perturbation acting during a time window of length $`T`$, the first-order transition amplitude contains
  ``` math
  W_T(\Delta E)=\int_{-T/2}^{T/2}e^{i\Delta E t}\,dt
  =2\frac{\sin(\Delta E T/2)}{\Delta E},
  ```
  and the normalized squared kernel converges distributionally to $`2\pi\delta(\Delta E)`$. More generally, smooth time windows yield approximate energy-conservation kernels through their Fourier transforms, with normalization fixed by Plancherel. The transition-rate limit reproduces the usual Fermi-golden-rule factor, and wave-packet scattering shows how plane-wave deltas are always integrated against finite profiles in physical amplitudes. We then combine finite time and finite spatial support to obtain finite energy–momentum bookkeeping kernels replacing the exact S-matrix conservation delta.

  The MTT interpretation is that exact scattering deltas are not primitive conservation objects inside finite processes. They are asymptotic bookkeeping limits of admissible transition windows once the interaction is idealized as infinitely extended and the in/out sectors are stable enough to support an S-matrix description. Finite-time scattering therefore provides a concrete bridge between coherent admissible dynamics and the distributional conservation structure of perturbative QFT.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: c8dfdbb72fa2ed82eda536f08eee70461e7cf5d444484e4fcff0b63ee10c265d
paper_id: finite-time-scattering-and-s-matrix-deltas-as-asymptoti-b099734c
release_state: not_matched_to_zenodo
title: |
  Finite-Time Scattering and S-Matrix Deltas as Asymptotic Bookkeeping Limits  
  Energy–Momentum Conservation Deltas from Admissible Transition Windows
---

# Purpose and claim discipline

This paper is the scattering sequel to the delta/projection series. Its purpose is narrow.

We do not claim to reconstruct full scattering theory from first principles in this paper. We also do not claim that energy or momentum conservation is merely approximate in a closed system. Rather, we prove and interpret a standard fact:

> Exact S-matrix delta functions arise only after idealizing finite transition windows into infinite asymptotic support.

The mathematical statement is elementary Fourier analysis. The MTT interpretation is structural: finite admissible interactions carry finite bookkeeping kernels; exact conservation deltas are the singular limit of those kernels.

<div class="center">

</div>

# Fourier conventions

We use the following convention on time:
``` math
\widehat w(\omega)=\int_{\mathbb R} w(t)e^{i\omega t}\,dt.
```
With this convention,
``` math
\lim_{T\to\infty}\int_{-T/2}^{T/2}e^{i\omega t}\,dt
=2\pi\delta(\omega)
```
in the sense of distributions.

In spacetime dimension $`d+1`$, for a window $`w(x)`$ with $`x=(t,\mathbf x)`$, we write
``` math
\widehat w(q)=\int w(x)e^{iq\cdot x}\,d^{d+1}x,
```
with the corresponding limiting convention
``` math
\widehat w_R(q)\longrightarrow (2\pi)^{d+1}\delta^{(d+1)}(q)
```
for approximate-identity windows whose support scale tends to infinity.

# Finite-time transition amplitudes

Let $`H=H_0+V`$ and suppose $`|i\rangle,|f\rangle`$ are eigenstates of $`H_0`$ with
``` math
H_0|i\rangle=E_i|i\rangle,\qquad H_0|f\rangle=E_f|f\rangle.
```
In first-order time-dependent perturbation theory, with perturbation $`V`$ active only through a time window $`w_T(t)`$, the transition amplitude is
``` math
\mathcal A_{fi}^{(1)}(T)
=
-i\,V_{fi}\int_{\mathbb R} w_T(t)e^{i(E_f-E_i)t}\,dt.
```
Writing
``` math
\Delta E:=E_f-E_i,
```
we have
``` math
\mathcal A_{fi}^{(1)}(T)
=
-i\,V_{fi}\,\widehat w_T(\Delta E).
```

Thus the finite-time transition does not contain $`\delta(\Delta E)`$. It contains the finite bookkeeping kernel $`\widehat w_T(\Delta E)`$.

# Box window and the sinc kernel

For the sharp observation window
``` math
w_T(t)=\mathbf 1_{[-T/2,T/2]}(t),
```
the kernel is
``` math
W_T(\omega)=\widehat w_T(\omega)
=
\int_{-T/2}^{T/2}e^{i\omega t}\,dt
=
2\frac{\sin(\omega T/2)}{\omega}.
```

This is a sinc-type energy bookkeeping kernel. It is sharply peaked near $`\omega=0`$, but for finite $`T`$ it is not a delta.

<div class="theorem">

**Theorem 1** (Finite-time energy kernel). *Let
``` math
D_T(\omega):=\frac{1}{2\pi T}|W_T(\omega)|^2
=
\frac{1}{2\pi T}\left(\frac{2\sin(\omega T/2)}{\omega}\right)^2.
```
Then
``` math
D_T(\omega)\to \delta(\omega)
```
in the sense of distributions as $`T\to\infty`$.*

</div>

<div class="proof">

*Proof.* Let $`f`$ be a Schwartz test function. With $`u=\omega T/2`$, one obtains
``` math
\int_{\mathbb R}D_T(\omega)f(\omega)\,d\omega
=
\int_{\mathbb R}\frac{1}{\pi}\left(\frac{\sin u}{u}\right)^2
f\!\left(\frac{2u}{T}\right)\,du.
```
Since
``` math
\int_{\mathbb R}\frac{1}{\pi}\left(\frac{\sin u}{u}\right)^2du=1,
```
and $`f(2u/T)\to f(0)`$ pointwise, dominated-convergence/standard approximate-identity arguments give
``` math
\int_{\mathbb R}D_T(\omega)f(\omega)\,d\omega\to f(0).
```
Thus $`D_T\to\delta`$ distributionally. ◻

</div>

The unsquared amplitude kernel itself satisfies
``` math
W_T(\omega)\to 2\pi\delta(\omega)
```
distributionally. The squared, normalized kernel $`D_T`$ is the probability-rate version.

<div class="center">

| Object | Finite-time expression | Asymptotic limit |
|:---|:---|:---|
| Amplitude kernel | $`W_T(\omega)`$ | $`2\pi\delta(\omega)`$ |
| Rate kernel | $`\frac{1}{T}|W_T(\omega)|^2`$ | $`2\pi\delta(\omega)`$ |
| Normalized rate kernel | $`\frac{1}{2\pi T}|W_T(\omega)|^2`$ | $`\delta(\omega)`$ |

</div>

The distinction is important. Amplitudes contain a distributional delta in the infinite-time limit. Probabilities contain squared kernels, and the meaningful object is the rate-normalized approximate identity.

# Fermi’s golden rule as the rate limit

The first-order transition probability is
``` math
P_{fi}(T)=|V_{fi}|^2 |W_T(\Delta E)|^2.
```
For transitions into a continuum of final states with density $`\rho(E_f)`$, the total probability is
``` math
P_i(T)=\int |V_{fi}|^2 |W_T(E_f-E_i)|^2\rho(E_f)\,dE_f.
```
Using the distributional limit
``` math
\frac{1}{T}|W_T(\omega)|^2\to 2\pi\delta(\omega),
```
one obtains the transition rate
``` math
\Gamma_i
=
\lim_{T\to\infty}\frac{P_i(T)}{T}
=
2\pi |V_{fi}|^2\rho(E_i),
```
in the usual idealized form.

Thus Fermi’s golden rule already displays the core pattern of this paper:

``` math
\boxed{\text{finite-time transition kernel}\quad\longrightarrow\quad\text{asymptotic energy delta}.}
```

# Smooth time windows

The box window is useful because it gives the familiar sinc kernel, but the conclusion does not depend on the discontinuity of the box. Let
``` math
w_T(t)=w(t/T),
```
with $`w\in C_c^\infty(\mathbb R)`$ nonzero. Then
``` math
\widehat w_T(\omega)=T\widehat w(T\omega).
```
With our Fourier convention, Plancherel gives
``` math
\|\widehat w\|_{L^2(\omega)}^2=2\pi\|w\|_{L^2(t)}^2.
```
Hence the correctly normalized smooth-window rate kernel is
``` math
D_T^w(\omega)
=
\frac{|\widehat w_T(\omega)|^2}{2\pi T\|w\|_{L^2}^2}
=
\frac{T|\widehat w(T\omega)|^2}{2\pi \|w\|_{L^2}^2}.
```
It has unit integral and forms an approximate identity:
``` math
D_T^w(\omega)\to \delta(\omega)
```
distributionally.

Indeed, for a Schwartz test function $`f`$,
``` math
\int_{\mathbb R}D_T^w(\omega)f(\omega)\,d\omega
=
\int_{\mathbb R}
\frac{|\widehat w(u)|^2}{2\pi\|w\|_{L^2}^2}
f(u/T)\,du
\to f(0).
```
The constants change if one uses a different Fourier convention, but the structural result is invariant: finite time windows give finite-width energy kernels, and exact deltas appear only in the infinite-time limit.

This shows that the exact energy delta is not tied to a discontinuous box window. It is the universal infinite-time limit of finite admissible time windows.

# Wave-packet scattering

Plane-wave scattering states are themselves idealizations: they are infinitely extended and exactly sharp in momentum. A finite incoming packet has the form
``` math
|\psi_i\rangle=\int dp\, f_i(p)|p\rangle,
\qquad
|\psi_f\rangle=\int dp\, f_f(p)|p\rangle,
```
with normalized packet profiles $`f_i,f_f`$. When the plane-wave S-matrix contains a conservation factor,
``` math
(2\pi)^{d+1}\delta^{(d+1)}(p_f-p_i),
```
the packet amplitude contains this distribution only under integration against the packet profiles:
``` math
\mathcal A_{\psi_f\psi_i}
=
\int dp_f\,dp_i\,
f_f^\ast(p_f)f_i(p_i)
(2\pi)^{d+1}\delta^{(d+1)}(p_f-p_i)\mathcal M(p_f,p_i).
```
For finite packets and finite interaction windows, the delta is replaced by a finite overlap kernel,
``` math
\delta^{(d+1)}(p_f-p_i)
\quad\leadsto\quad
K_{T,R}(p_f-p_i),
```
where $`K_{T,R}`$ is the Fourier transform of the spacetime transition window. The physically observed amplitude is therefore a packet-weighted overlap, not a naked delta. The exact delta belongs to the plane-wave, infinite-support idealization.

In MTT terms, wave packets are closer to admissible finite bookkeeping than plane waves. Plane waves expose the singular limit cleanly, but finite packets better represent the finite-resolution transition structure.

# LSZ, asymptotic regimes, and admissible scattering

The exact S-matrix is not available in arbitrary dynamical regimes. It requires stable asymptotic sectors in which in/out states can be defined and compared. In ordinary QFT this is the role of Haag–Ruelle/LSZ-type scattering theory in regimes with appropriate mass gaps, stability, and asymptotic separation.

The present paper does not derive LSZ or Haag–Ruelle theory. It uses their standard lesson as a domain condition:

> S-matrix deltas are meaningful only when the theory admits stable asymptotic in/out sectors.

In MTT language, this means that an S-matrix description is an admissible scattering encoding, not a universal description of all processes. In time-dependent backgrounds, finite systems, measurement contexts, or strongly interacting non-asymptotic regimes, local observables or in-in quantities may be the correct objects, and exact conservation deltas should be replaced by finite bookkeeping kernels.

# Finite spatial support and full energy–momentum kernels

Let an interaction be supported by a spacetime window
``` math
w_{T,R}(t,\mathbf x)
=
w_T(t)v_R(\mathbf x).
```
For an interaction with total energy–momentum mismatch
``` math
q=(\Delta E,\Delta \mathbf p),
```
the vertex factor contains
``` math
\widehat w_{T,R}(q)
=
\widehat w_T(\Delta E)\widehat v_R(\Delta \mathbf p).
```
For finite $`T,R`$, this is a finite-width energy–momentum bookkeeping kernel. In the asymptotic limit,
``` math
\widehat w_{T,R}(q)
\to
(2\pi)^{d+1}\delta(\Delta E)\delta^{(d)}(\Delta\mathbf p).
```

Hence the exact S-matrix conservation factor is the infinite-time, infinite-volume limit of finite transition support:
``` math
(2\pi)^{d+1}\delta^{(d+1)}(q)
=
\lim_{T,R\to\infty}\widehat w_{T,R}(q).
```

# S-matrix deltas and asymptotic idealization

In standard scattering theory, one writes
``` math
\langle f|S|i\rangle
=
\delta_{fi}
+
i(2\pi)^4\delta^{(4)}(p_f-p_i)\mathcal M_{fi}.
```
The delta is not produced by a finite laboratory process. It belongs to the asymptotic idealization in which:

1.  in/out states are stable and well separated;

2.  the interaction region is effectively isolated;

3.  time support has been idealized to infinity;

4.  spatial support has been idealized to exact translation invariance;

5.  bookkeeping mismatch has been forced to zero width.

This is not a criticism of the S-matrix. It is a clarification of its domain. The S-matrix is the correct object when admissible scattering regimes exist. In finite-time or time-dependent regimes, local or in-in observables are usually more appropriate, and conservation deltas are replaced by finite kernels.

# MTT interpretation

The MTT reading is that exact scattering deltas belong to the circle/bookkeeping side of the triadic carrier. They express exact closure of the energy–momentum ledger after the finite transition window has been idealized away.

The finite kernel
``` math
\widehat w_{T,R}(q)
```
is the native object. It measures how strongly a process with mismatch $`q`$ is supported by the finite admissible transition region. The delta arises only when the bookkeeping window becomes infinitely extended and the mismatch width collapses to zero.

``` math
\boxed{
\text{S-matrix delta}
=
\text{singular asymptotic shadow of finite bookkeeping closure}.
}
```

This completes the circle-sector counterpart to the previous papers:

<div class="center">

| Paper               | Delta role               | MTT sector emphasis |
|:--------------------|:-------------------------|:--------------------|
| Gauge fixing        | Representative selection | Lens redundancy     |
| Measurement         | Survivor-basin selection | Nil stabilization   |
| Momentum/scattering | Conservation bookkeeping | Circle closure      |

</div>

# Conservation is not merely approximate

A possible misunderstanding should be avoided. Finite-width energy–momentum kernels do not mean that closed systems violate conservation laws. Rather, the finite kernel reflects that a finite effective transition description does not implement the asymptotic S-matrix idealization.

Exact conservation belongs to the full closed-system symmetry or to the asymptotic scattering limit. Finite broadening belongs to finite observation, finite support, finite coherence, and finite admissible transition windows.

Thus the claim is:

``` math
\text{finite window} \neq \text{fundamental nonconservation}.
```

It is instead:

``` math
\text{finite window} = \text{finite bookkeeping resolution}.
```

# Scope of proof

<div class="center">

</div>

# Conclusion

Finite-time scattering exposes the same projection structure that appeared in point sources, gauge fixing, measurement, and contact interactions. A finite process produces a finite kernel. The exact Dirac delta appears only after an asymptotic idealization.

The central result is:
``` math
\boxed{
2\pi\delta(\Delta E)
=
\lim_{T\to\infty}
\int_{-T/2}^{T/2}e^{i\Delta E t}\,dt
}
```
in the distributional amplitude sense, and
``` math
\boxed{
\delta(\Delta E)
=
\lim_{T\to\infty}
\frac{1}{2\pi T}\left|
\int_{-T/2}^{T/2}e^{i\Delta E t}\,dt
\right|^2
}
```
in the normalized transition-rate sense.

Thus S-matrix deltas are not mysterious primitive conservation objects inside finite dynamics. They are the distributional endpoints of finite admissible transition kernels. In MTT language, they are singular asymptotic shadows of bookkeeping closure.
