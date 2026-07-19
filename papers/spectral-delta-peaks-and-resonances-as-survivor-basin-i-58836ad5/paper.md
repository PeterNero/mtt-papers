---
abstract: |
  Dirac delta functions appear in spectral physics as sharp energy levels, stable-particle poles, density-of-states atoms, spectral functions, and exact normal-mode decompositions. In ordinary notation one writes terms such as
  ``` math
  \rho(E)=\sum_n \delta(E-E_n),
  \qquad
  A(\omega)=2\pi Z\,\delta(\omega-\omega_0)+\cdots .
  ```
  This paper develops the spectral sequel to the delta-projection program in Modal Triplet Theory (MTT). The core mathematical statement is standard but structurally decisive: Lorentzian/Breit–Wigner kernels form approximate identities, and delta peaks are recovered only in the zero-width or infinite-lifetime limit. A stable spectral delta is therefore the singular idealization of a finite-width survivor mode.

  We prove the weak convergence of Lorentzian kernels to the Dirac delta, derive the same kernel from exponential decay in time, and state the corresponding spectral-measure smearing theorem. We then interpret sharp spectral atoms, resonances, finite lifetimes, LSZ poles, and density-of-states peaks through the MTT lens: a delta peak is the downstream encoding of a survivor basin whose lifetime and coherence width have been idealized as infinite stability and zero spectral width. This does not deny exact bound-state eigenvalues in self-adjoint spectral theory. Rather, it separates exact mathematical spectral atoms from the physical idealization involved when finite-resolution, finite-lifetime effective descriptions are written as exact deltas.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: da4a2852063dd59a2384cf5ebafb503e1f0908dc53039e156bb2a06fa64eef04
paper_id: spectral-delta-peaks-and-resonances-as-survivor-basin-i-58836ad5
release_state: not_matched_to_zenodo
title: |
  Spectral Delta Peaks and Resonances as Survivor-Basin Idealizations  
  Finite Lifetime, Lorentzian Kernels, and the Delta Limit in Modal Triplet Theory
---

*Part VIII of VIII in the Delta Projection series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

# Purpose and claim discipline

The preceding papers in this sequence treated Dirac deltas as singular shadows of admissible projection in several settings: identity kernels, Green functions, gauge fixing, measurement, contact interactions, and scattering support. The present paper treats the spectral case.

The target object is the familiar spectral delta:
``` math
\delta(E-E_0).
```
It appears in:

- density of states;

- spectral functions;

- stable-particle poles;

- normal-mode decompositions;

- Fermi’s golden rule;

- Kallen–Lehmann-type spectral representations;

- condensed-matter quasiparticle peaks;

- resonance approximations.

The central claim is:
``` math
\boxed{\text{A spectral delta peak is the zero-width limit of a finite-lifetime or finite-resolution survivor mode.}}
```

## Non-claims

We do not claim:

1.  that self-adjoint operators cannot have genuine pure point spectrum;

2.  that bound-state eigenvalues are artifacts;

3.  that resonance theory is replaced by MTT language;

4.  that all spectral broadening has one microscopic cause;

5.  that finite lifetime is the only source of spectral width.

The narrower statement is that whenever an effective physical description writes a stable spectral contribution as a Dirac delta, MTT should ask which admissible survivor basin, lifetime scale, coherence width, detector resolution, or projection kernel has been idealized away.

# Sharp spectral atoms and finite-width peaks

A normalized exact spectral atom at energy $`E_0`$ is written
``` math
\rho(E)=\delta(E-E_0).
```
If the mode has finite lifetime or finite resolution, the sharp atom is replaced by a broadened peak. The most common model is the Lorentzian or Breit–Wigner kernel
``` math
L_\Gamma(E-E_0)
=
\frac{1}{\pi}\frac{\Gamma/2}{(E-E_0)^2+(\Gamma/2)^2},
\qquad \Gamma>0.
```
It is normalized:
``` math
\int_{\mathbb{R}}L_\Gamma(E-E_0)\,\mathrm{d}E=1.
```
As $`\Gamma\downarrow0`$, it converges to $`\delta(E-E_0)`$ in the sense of distributions.

The MTT interpretation is:
``` math
\Gamma>0
\quad\leftrightarrow\quad
\text{finite survivor-basin width or finite lifetime},
```
while
``` math
\Gamma=0
\quad\leftrightarrow\quad
\text{idealized infinitely stable survivor mode}.
```

# Lorentzian approximate identity theorem

<div class="definition">

**Definition 1** (Lorentzian kernel). For $`\Gamma>0`$, define
``` math
L_\Gamma(x)=\frac{1}{\pi}\frac{\Gamma/2}{x^2+(\Gamma/2)^2}.
```

</div>

<div class="theorem">

**Theorem 2** (Lorentzian kernels converge to the Dirac delta). *For every test function $`f\in C_c^\infty(\mathbb{R})`$,
``` math
\lim_{\Gamma\downarrow0}\int_{\mathbb{R}}L_\Gamma(E-E_0)f(E)\,\mathrm{d}E=f(E_0).
```
Equivalently,
``` math
L_\Gamma(E-E_0)\to \delta(E-E_0)
```
in the sense of distributions.*

</div>

<div class="proof">

*Proof.* Let $`a=\Gamma/2`$. Then
``` math
L_\Gamma(x)=\frac{1}{\pi}\frac{a}{x^2+a^2}.
```
The functions $`L_\Gamma`$ are nonnegative and normalized. Fix $`\epsilon>0`$. Since $`f`$ is continuous at $`E_0`$, choose $`\eta>0`$ so that
``` math
|f(E)-f(E_0)|<\epsilon
```
whenever $`|E-E_0|<\eta`$.

Then
``` math
\left|\int L_\Gamma(E-E_0)f(E)\,\mathrm{d}E-f(E_0)\right|
\le I_1+I_2,
```
where
``` math
I_1=
\int_{|E-E_0|<\eta}L_\Gamma(E-E_0)|f(E)-f(E_0)|\,\mathrm{d}E
\le \epsilon,
```
and
``` math
I_2=
\int_{|E-E_0|\ge \eta}L_\Gamma(E-E_0)|f(E)-f(E_0)|\,\mathrm{d}E.
```
Since $`f`$ is compactly supported and bounded, $`|f(E)-f(E_0)|\le C_f`$. Moreover the Lorentzian mass outside any fixed neighborhood tends to zero:
``` math
\int_{|x|\ge \eta}L_\Gamma(x)\,\mathrm{d}x\to0
\qquad(\Gamma\downarrow0).
```
Hence $`I_2\to0`$. Since $`\epsilon`$ was arbitrary, the result follows. ◻

</div>

<div class="corollary">

**Corollary 3** (Breit–Wigner peak as regularized spectral delta). *A Breit–Wigner spectral contribution
``` math
\rho_\Gamma(E)=ZL_\Gamma(E-E_0)
```
converges weakly to
``` math
Z\delta(E-E_0)
```
as $`\Gamma\downarrow0`$.*

</div>

# Finite lifetime produces Lorentzian width

The Lorentzian is not merely a convenient regularization. It is the Fourier-domain signature of exponential decay.

Let a mode have time dependence
``` math
a(t)=\Theta(t)e^{-iE_0t}e^{-\Gamma t/2}.
```
Its Fourier transform is, up to convention factors,
``` math
\widehat a(E)
=
\int_0^\infty e^{iEt}e^{-iE_0t}e^{-\Gamma t/2}\,\mathrm{d}t
=
\frac{1}{\Gamma/2-i(E-E_0)}.
```
Therefore
``` math
|\widehat a(E)|^2
=
\frac{1}{(E-E_0)^2+(\Gamma/2)^2}.
```
After normalization, this is the Lorentzian $`L_\Gamma(E-E_0)`$.

Thus:
``` math
\boxed{
\text{finite lifetime } \tau\sim \Gamma^{-1}
\quad\Longleftrightarrow\quad
\text{finite spectral width } \Gamma.
}
```
The spectral delta is recovered only when $`\tau\to\infty`$.

# Spectral-measure smearing theorem

Let $`H`$ be a self-adjoint operator on a Hilbert space $`\mathcal{H}`$, with spectral measure $`P_H(\mathrm{d}E)`$. For a normalized vector $`\psi\in\mathcal{H}`$, define the scalar spectral measure
``` math
\mu_\psi(B)=\left\langle \psi,\,P_H(B)\psi \right\rangle.
```
A sharp spectral density is formal unless $`\mu_\psi`$ is absolutely continuous. But one can always form a Lorentzian-smeared spectral density:
``` math
\rho_{\psi,\Gamma}(E)
=
\int_{\mathbb{R}}L_\Gamma(E-E')\,\mu_\psi(\mathrm{d}E').
```

<div class="theorem">

**Theorem 4** (Smeared spectral measures converge weakly). *For every bounded continuous test function $`f`$,
``` math
\lim_{\Gamma\downarrow0}
\int_{\mathbb{R}} f(E)\rho_{\psi,\Gamma}(E)\,\mathrm{d}E
=
\int_{\mathbb{R}} f(E)\,\mu_\psi(\mathrm{d}E).
```*

</div>

<div class="proof">

*Proof.* By Fubini,
``` math
\int f(E)\rho_{\psi,\Gamma}(E)\,\mathrm{d}E
=
\int \left(\int f(E)L_\Gamma(E-E')\,\mathrm{d}E\right)\mu_\psi(\mathrm{d}E').
```
The inner integral is $`(L_\Gamma*f)(E')`$, which converges to $`f(E')`$ pointwise as $`\Gamma\downarrow0`$. Since $`f`$ is bounded and $`L_\Gamma`$ is normalized,
``` math
|(L_\Gamma*f)(E')|\le \|f\|_\infty.
```
Dominated convergence with respect to the finite measure $`\mu_\psi`$ gives the result. ◻

</div>

<div class="remark">

*Remark 5*. This theorem includes pure point, absolutely continuous, and singular continuous spectral measures. It does not say all spectra are physically broadened. It says Lorentzian broadening is a controlled approximation to any spectral measure and that delta atoms are recovered in the zero-width limit.

</div>

# Resolvent representation

The Lorentzian also appears as the imaginary part of a resolvent:
``` math
L_\Gamma(E-E_0)
=
-\frac{1}{\pi}\operatorname{Im}\frac{1}{E-E_0+i\Gamma/2}.
```
More generally, for a self-adjoint $`H`$,
``` math
\rho_{\psi,\Gamma}(E)
=
-\frac{1}{\pi}\operatorname{Im}\left\langle \psi,\,(E-H+i\Gamma/2)^{-1}\psi \right\rangle.
```
Thus finite spectral width is equivalent to evaluating the resolvent off the real axis. The sharp spectral measure is recovered as the boundary value $`\Gamma\downarrow0`$.

In physical language, $`\Gamma`$ may encode finite lifetime, detector resolution, environment coupling, damping, or coherent-sector width. In MTT language, it is the spectral width of the survivor-basin encoding.

# Lifetime, width, and complex poles

A finite resonance width is conventionally related to a finite lifetime by
``` math
\tau_{\mathrm{life}}\sim \Gamma^{-1},
```
up to convention-dependent factors. The simplest way to see this is the exponentially decaying amplitude
``` math
a(t)=e^{-iE_0t}e^{-\Gamma t/2}\mathbf 1_{t\ge0}.
```
Its Fourier transform has denominator
``` math
\widehat a(E)\propto \frac{1}{E-E_0+i\Gamma/2}.
```
Thus the resonance is represented by a pole displaced from the real axis:
``` math
E_{\mathrm{pole}}=E_0-i\Gamma/2.
```
The spectral peak on the real energy axis is the imaginary part of this off-axis pole contribution. A true spectral delta corresponds to the limiting case in which the pole approaches the real axis:
``` math
\Gamma\downarrow0,
\qquad
E_{\mathrm{pole}}\to E_0.
```

<div class="remark">

*Remark 6*. This pole language is especially useful for separating three notions that are often blurred: an exact eigenvalue of a self-adjoint finite-volume operator, a stable infinite-volume particle pole, and an unstable resonance pole. All three may produce sharp or nearly sharp spectral features, but their mathematical status is different.

</div>

# Stable particles, LSZ poles, and resonance peaks

In scattering theory, a stable one-particle state appears as a pole on the real mass shell or as a delta contribution to the spectral measure. A schematic spectral function has the form
``` math
A(\omega,\mathbf p)
=
2\pi Z\,\delta(\omega-E_{\mathbf p})
+
A_{\mathrm{cont}}(\omega,\mathbf p).
```
For an unstable particle or quasiparticle, the sharp contribution is replaced by
``` math
A_\Gamma(\omega,\mathbf p)
\approx
2\pi Z\,L_\Gamma(\omega-E_{\mathbf p})
+
A_{\mathrm{cont}}(\omega,\mathbf p).
```

The delta peak is therefore the infinite-lifetime limit:
``` math
\Gamma\downarrow0
\quad\Longrightarrow\quad
A_\Gamma\to A.
```

<div class="center">

| Object                | Finite-width form         | Sharp limit               |
|:----------------------|:--------------------------|:--------------------------|
| Stable bound state    | narrow spectral atom      | $`\delta(E-E_n)`$         |
| Unstable particle     | Breit–Wigner peak         | pole approaches real axis |
| Quasiparticle         | Lorentzian-like peak      | infinite lifetime mode    |
| Detector-limited line | resolution-broadened peak | ideal line spectrum       |
| MTT survivor basin    | finite basin width        | zero-width survivor label |

</div>

# Kallen–Lehmann spectral representation

The same distinction appears in relativistic quantum field theory through the Kallen–Lehmann representation. For a scalar field, the two-point function can be written schematically as
``` math
\langle 0|\phi(x)\phi(0)|0\rangle
=
\int_0^\infty d\mu^2\,\rho(\mu^2)\,\Delta_+(x;\mu^2).
```
When the theory contains a stable one-particle state of mass $`m`$, the spectral density contains an atom:
``` math
\rho(\mu^2)
=
Z\,\delta(\mu^2-m^2)
+
\rho_{\mathrm{cont}}(\mu^2).
```
The coefficient $`Z`$ is the pole residue or wave-function weight of the stable sector. If the would-be particle is unstable, the exact delta contribution is replaced by a broadened resonance contribution inside the continuum.

In the present terminology,
``` math
Z\,\delta(\mu^2-m^2)
```
is the sharp idealization of an exactly stable survivor sector. A finite-width resonance is the corresponding finite-persistence version.

<div class="remark">

*Remark 7*. This section does not derive the Kallen–Lehmann representation. Its role is classificatory: it identifies one of the most important places where spectral delta functions enter QFT and shows that it fits the same delta-as-ideal-survivor pattern.

</div>

# Finite-volume spectral atoms versus physical lifetime

A self-adjoint operator on a compact domain may have exact discrete eigenvalues. Its spectral measure may therefore contain genuine atoms even before any physical infinite-lifetime claim is made. These atoms are mathematical consequences of compactness, boundary conditions, or finite-volume quantization.

This paper distinguishes three cases:

<div class="center">

| Case | Meaning of the delta-like feature |
|:---|:---|
| Finite-volume eigenvalue | Exact atom of a compact/self-adjoint spectral problem. |
| Stable infinite-volume particle | Real-axis mass-shell pole with exact asymptotic persistence. |
| Unstable resonance | Finite-width peak from a pole off the real axis. |

</div>

The MTT survivor-basin reading applies most directly to the second and third cases: the delta peak represents idealized exact persistence, while the resonance represents finite leakage or finite basin width. In finite volume, a delta may also reflect mathematical discreteness rather than physical infinite lifetime.

# MTT interpretation: survivor-basin idealization

The triadic MTT carrier distinguishes bookkeeping, redundancy transport, and survivorship. Spectral peaks are naturally tied to survivorship: a mode that persists long enough to be tracked as a stable excitation appears as a spectral object.

A finite-width resonance corresponds to a basin that is coherent but not infinitely stable. It has:

- a central energy or mass label;

- a finite damping or leakage rate;

- finite measurement resolution;

- finite admissibility width;

- possible coupling to continuum sectors.

A spectral delta idealizes all of this into an exact survivor:
``` math
\boxed{
\delta(E-E_0)
=
\text{zero-width encoding of an infinitely persistent survivor mode}.
}
```

This aligns with the fixed-point and measurement papers in the sequence. A fixed point may be represented by a delta only after its basin width is ignored. A measurement outcome may be represented by a sharp projector only after finite detector width is ignored. A stable particle may be represented by a spectral delta only after finite lifetime and resolution are ignored.

# Relation to the OU floor

In the MTT measurement and fixed-point stability papers, persistent disturbance balanced against damping produces an Ornstein–Uhlenbeck-type variance
``` math
\sigma^2=\frac{\delta}{2\gamma}.
```
The spectral analogue is:
``` math
\Gamma \sim \text{leakage/damping rate}.
```
If damping and disturbance leave a nonzero effective width, the spectral line does not become a true delta. Thus the exact delta limit requires not merely a central label, but removal of all effective broadening:
``` math
\Gamma\to0,
\qquad
\sigma\to0,
\qquad
\text{or resolution}\to0.
```

This gives the MTT diagnostic:
``` math
\boxed{
\text{When a spectral delta appears, ask which finite lifetime, basin width, or resolution scale has been suppressed.}
}
```

# Scope of proof and physical claim

<div class="center">

| Level | Status |
|:---|:---|
| Lorentzian approximate identity | Proved rigorously. |
| Finite lifetime to Lorentzian line shape | Standard Fourier calculation. |
| Smeared spectral measures | Proved as weak convergence. |
| Complex pole interpretation | Standard resonance-theory classification. |
| Kallen–Lehmann delta atom | Standard QFT spectral structure, used here classificatorily. |
| Stable particle delta as infinite-lifetime limit | Standard physical interpretation. |
| Finite-volume spectral atoms | A distinct mathematical case, explicitly separated from lifetime claims. |
| MTT survivor-basin reading | Structural interpretation, not a new spectral theorem. |
| Exact derivation of widths from MTT carrier data | Not done here; belongs to execution-level work. |

</div>

# Consequences for the delta-projection program

This paper adds a new domain to the growing dictionary:
``` math
\delta(E-E_0)
\quad\leadsto\quad
L_\Gamma(E-E_0)
\quad\leadsto\quad
\text{finite survivor-basin spectral kernel}.
```

It shows that spectral deltas fit the same pattern as earlier cases:

- point-source deltas are zero-width source kernels;

- gauge-fixing deltas are zero-width section-selection kernels;

- measurement deltas are zero-width detector effects;

- contact deltas are zero-width overlap vertices;

- scattering deltas are infinite-time bookkeeping limits;

- spectral deltas are infinite-lifetime survivor limits;

- Kallen–Lehmann mass deltas are sharp stable-sector atoms.

# Conclusion

Spectral delta peaks are among the most familiar idealizations in physics. They mark exact energy levels, stable-particle contributions, and perfectly sharp normal modes. The mathematical theory of self-adjoint operators allows genuine spectral atoms, and this paper does not deny that fact. Its point is different: in effective physical descriptions, a sharp spectral delta often encodes an idealization of infinite lifetime, zero width, perfect resolution, or exact survivor stability.

The Lorentzian/Breit–Wigner kernel makes this precise. It converges to the Dirac delta as its width tends to zero, and it arises directly from exponential decay in time. Smeared spectral measures converge weakly to the underlying spectral measure. Thus the delta peak is the singular endpoint of a controlled finite-width family.

In MTT language, a spectral delta is the zero-width shadow of a survivor basin whose persistence has been idealized as exact. The question prompted by every spectral delta is therefore:

``` math
\boxed{
\text{What finite lifetime, admissibility width, or survivor-basin structure has been collapsed into this sharp peak?}
}
```
