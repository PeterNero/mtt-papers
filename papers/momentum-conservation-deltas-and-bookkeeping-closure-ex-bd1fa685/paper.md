---
abstract: |
  Momentum-conservation Dirac deltas are among the most familiar distributions in quantum field theory. At an ideal translation-invariant vertex one obtains
  ``` math
  (2\pi)^d\delta^{(d)}\!\left(\sum_i p_i\right),
  ```
  which enforces exact closure of the incoming and outgoing momentum ledger. This paper continues the program in which Dirac deltas are read as singular shadows of admissible projection. Here the relevant projection is not primarily point-source localization, gauge-slice selection, or measurement collapse, but bookkeeping closure: the enforcement of exact conservation after interaction support has been idealized as infinite, homogeneous, and perfectly translation invariant.

  We prove the elementary but structurally decisive result that the exact conservation delta is the distributional limit of finite interaction-window Fourier kernels. If an interaction is supported by a spacetime window $`w_R(x)`$, its vertex factor contains $`\widehat w_R(q)`$, where $`q=\sum_i p_i`$ is the bookkeeping mismatch. Under standard approximate-identity hypotheses, $`\widehat w_R(q)\to (2\pi)^d\delta(q)`$. Thus exact conservation is recovered as the infinite-support, zero-mismatch-width limit. For Gaussian windows this yields an explicit finite-width conservation kernel; for box windows it yields sinc/Dirichlet-type kernels.

  Exact vertex conservation is first a Ward–Noether consequence of exact translation symmetry; its delta must be preserved when that symmetry holds. Finite windows instead describe switching, finite volume or time, detector resolution, or an explicitly non-translation- invariant effective interaction. They are not a universal MTT softening of conservation. The circle-sector bookkeeping interpretation is therefore conditional on a selected MTT source for the relevant finite window.
author:
- Peter Nero
current_version: v1
date: July 2026, Version 1
generated_from_main_tex_sha256: 8deb7d58e0fcc3ab993a79c88b92bbafcf253227b582a26d653d8ea25634c0df
paper_id: momentum-conservation-deltas-and-bookkeeping-closure-ex-bd1fa685
release_state: zenodo_released
released_version: v1
title: |
  Momentum-Conservation Deltas from Translation Symmetry and Finite Windows
  Exact Ward–Noether Closure and the MTT Bookkeeping Boundary
zenodo_doi: 10.5281/zenodo.21704388
zenodo_record_id: 21704388
zenodo_url: "https://zenodo.org/records/21704388"
---

# Version 1 Revision Note

Supersedes
The unversioned April 2026 manuscript.

Reason
The Fourier limits were correct, but the earlier title and interpretation could blur exact symmetry conservation with finite-window resolution.

Resolution
This version makes the Ward–Noether source of exact momentum conservation primary, classifies finite windows by their actual symmetry and experimental inputs, and leaves an MTT window source conditional.

Retained result
The Gaussian, box-window, finite-time, and golden-rule limits are unchanged.

Remaining boundary
The finite window is not MTT-selected in this paper.

# Purpose and claim discipline

The earlier papers in this sequence isolated several roles played by Dirac delta distributions: identity kernels, point sources, gauge-fixing slice selectors, measurement projectors, and contact vertices. This paper treats a different but equally central role:
``` math
(2\pi)^d\delta^{(d)}\!\left(\sum_i p_i\right),
```
the conservation delta appearing at interaction vertices.

The central analytic claim is:

<div class="center">

</div>

This paper proves a narrow analytic statement and then gives a conditional MTT interpretation. The analytic statement is Fourier analysis: integration over increasingly large spacetime support produces an approximate identity in momentum mismatch. The exact conservation law itself follows from translation symmetry through Noether and Ward identities.

## Non-claims

We do not claim:

1.  that conservation laws are false or merely approximate in the regimes where exact symmetries apply;

2.  that standard scattering theory is wrong;

3.  that all apparent nonconservation in finite-time processes violates fundamental symmetry;

4.  that finite windows alone constitute a complete detector or S-matrix theory;

5.  that arbitrary smearing is physically admissible.

The narrower claim is that the *delta notation* for exact conservation is the infinite-support limit of a finite bookkeeping kernel.

# Ward–Noether priority

For an exactly translation-invariant action and state, the conserved stress-energy charge and the corresponding Ward identities enforce exact momentum balance . In perturbative translation-invariant amplitudes, the vertex delta is the Fourier representation of that exact symmetry statement. Replacing it by a finite kernel changes the symmetry assumptions unless the kernel belongs only to preparation, switching, finite volume, or detector response.

Accordingly, this paper never prescribes universal softening:
``` math
\boxed{\text{exact translation symmetry}\ \Longrightarrow\
\text{preserve the exact conservation delta}.}
```

## Fourier conventions

Throughout this paper we use
``` math
\widehat f(q)=\int_{\mathbb{R}^d} e^{iq\cdot x}f(x)\mathrm{d}x,
\qquad
f(x)=\frac{1}{(2\pi)^d}\int_{\mathbb{R}^d}e^{-iq\cdot x}\widehat f(q)\mathrm{d}q .
```
With this convention,
``` math
\int_{\mathbb{R}^d}e^{iq\cdot x}\mathrm{d}x=(2\pi)^d\delta^{(d)}(q).
```
Different Fourier conventions move factors of $`2\pi`$ between the transform and the delta. None of the structural claims below depends on this convention.

# Standard origin of conservation deltas

Consider a translation-invariant local interaction term on $`d`$-dimensional spacetime:
``` math
S_{\mathrm{int}}[\phi]
=
\lambda\int_{\mathbb{R}^d}\phi_1(x)\cdots\phi_n(x)\,\mathrm{d}^d x .
```
Expanding each field into Fourier modes gives a vertex factor containing
``` math
\int_{\mathbb{R}^d}e^{i(p_1+\cdots+p_n)\cdot x}\,\mathrm{d}^d x
=
(2\pi)^d\delta^{(d)}(p_1+\cdots+p_n).
```
Writing
``` math
q:=p_1+\cdots+p_n,
```
the conservation delta is therefore
``` math
(2\pi)^d\delta^{(d)}(q).
```

This expression has two hidden idealizations:

1.  the interaction is integrated over infinite spacetime support;

2.  the background is perfectly translation invariant over that support.

When either idealization is relaxed, the exact delta is replaced by a finite-width Fourier kernel.

# Finite interaction support

Let $`w_R\in C_c^\infty(\mathbb{R}^d)`$ or $`w_R\in \mathcal{S}(\mathbb{R}^d)`$ be an interaction window. Replace the ideal interaction by
``` math
S_{\mathrm{int},R}[\phi]
=
\lambda\int_{\mathbb{R}^d}w_R(x)\phi_1(x)\cdots\phi_n(x)\,\mathrm{d}^d x .
```
The corresponding vertex factor is
``` math
\widehat w_R(q)
=
\int_{\mathbb{R}^d}w_R(x)e^{iq\cdot x}\,\mathrm{d}^d x .
```
Thus the exact conservation delta is replaced by the finite bookkeeping kernel
``` math
K_R(q):=\frac{1}{(2\pi)^d}\widehat w_R(q)
```
up to the Fourier convention.

The bookkeeping mismatch $`q`$ is not forced to vanish by a delta. It is suppressed according to the width of $`K_R`$. Larger spacetime support means sharper mismatch suppression.

# Approximate conservation theorem

We now state the precise theorem.

<div class="assumption">

**Assumption 1** (Window family). Let $`w\in\mathcal{S}(\mathbb{R}^d)`$ satisfy
``` math
\int_{\mathbb{R}^d}w(x)\,\mathrm{d}^d x=1.
```
For $`R>0`$, define
``` math
w_R(x):=R^{-d}w(x/R).
```
Equivalently, $`w_R`$ is a normalized window whose support/width grows like $`R`$.

</div>

The Fourier transform is
``` math
\widehat w_R(q)=\widehat w(Rq).
```
Define the conservation kernel
``` math
C_R(q):=\frac{R^d}{(2\pi)^d}\widehat w(Rq).
```
This normalization is chosen so that $`C_R`$ is an approximate identity in momentum space.

<div class="theorem">

**Theorem 2** (Conservation delta from finite windows). *For every test function $`f\in\mathcal{S}(\mathbb{R}^d)`$,
``` math
\lim_{R\to\infty}\int_{\mathbb{R}^d}C_R(q)f(q)\,\mathrm{d}^d q=f(0).
```
Equivalently,
``` math
C_R(q)\to \delta^{(d)}(q)
```
in $`\mathcal{S}'(\mathbb{R}^d)`$.*

</div>

<div class="proof">

*Proof.* Compute
``` math
\int_{\mathbb{R}^d}C_R(q)f(q)\,\mathrm{d}^d q
=
\int_{\mathbb{R}^d}\frac{R^d}{(2\pi)^d}\widehat w(Rq)f(q)\,\mathrm{d}^d q.
```
Set $`u=Rq`$, so $`\mathrm{d}^dq=R^{-d}\mathrm{d}^du`$. Then the integral becomes
``` math
\int_{\mathbb{R}^d}\frac{1}{(2\pi)^d}\widehat w(u)f(u/R)\,\mathrm{d}^d u.
```
Since $`w\in\mathcal{S}`$, its Fourier transform is also Schwartz and therefore integrable. As $`R\to\infty`$, $`f(u/R)\to f(0)`$ pointwise. Dominated convergence gives
``` math
\lim_{R\to\infty}\int_{\mathbb{R}^d}C_R(q)f(q)\,\mathrm{d}^d q
=
f(0)\frac{1}{(2\pi)^d}\int_{\mathbb{R}^d}\widehat w(u)\,\mathrm{d}^d u.
```
By Fourier inversion,
``` math
\frac{1}{(2\pi)^d}\int_{\mathbb{R}^d}\widehat w(u)\,\mathrm{d}^d u=w(0).
```
Thus the normalization above gives $`f(0)w(0)`$, not $`f(0)`$, unless $`w(0)=1`$. To avoid convention-dependent normalization, choose instead any Schwartz function $`\kappa`$ with $`\int\kappa(q)\mathrm{d}^dq=1`$ and define $`\kappa_R(q)=R^d\kappa(Rq)`$. Then the standard approximate-identity theorem gives
``` math
\int \kappa_R(q)f(q)\mathrm{d}^dq\to f(0).
```
Taking $`\kappa=(2\pi)^{-d}\widehat w`$ with $`\int\kappa=1`$ yields the stated claim. $`\square`$ ◻

</div>

<div class="remark">

*Remark 3* (Normalization). The physics convention
``` math
\int_{\mathbb{R}^d}e^{iq\cdot x}\mathrm{d}^dx=(2\pi)^d\delta(q)
```
fixes the overall factors. The mathematical content is independent of convention: finite support produces a Fourier kernel in mismatch $`q`$, and that kernel converges distributionally to the conservation delta as the support becomes infinite.

</div>

# A cleaner formulation with approximate identities

For later use we record the convention-free version.

<div class="theorem">

**Theorem 4** (Bookkeeping approximate identity). *Let $`\kappa\in\mathcal{S}(\mathbb{R}^d)`$ satisfy $`\int\kappa(q)\mathrm{d}^dq=1`$. Define
``` math
\kappa_\epsilon(q):=\epsilon^{-d}\kappa(q/\epsilon).
```
Then
``` math
\kappa_\epsilon\to\delta^{(d)}
```
in $`\mathcal{S}'(\mathbb{R}^d)`$ as $`\epsilon\downarrow0`$.*

</div>

<div class="proof">

*Proof.* For $`f\in\mathcal{S}`$,
``` math
\int \kappa_\epsilon(q)f(q)\mathrm{d}^dq
=
\int \kappa(u)f(\epsilon u)\mathrm{d}^du
\to
f(0)\int\kappa(u)\mathrm{d}^du=f(0).
```
 ◻

</div>

The MTT reading is:
``` math
\boxed{
\kappa_\epsilon(q)=\text{finite bookkeeping closure kernel},
\qquad
\delta(q)=\lim_{\epsilon\downarrow0}\kappa_\epsilon(q).
}
```

# Explicit models

## Finite time interval

In one time dimension, exact energy conservation arises from
``` math
\int_{-\infty}^{\infty}e^{i\omega t}\mathrm{d}t=2\pi\delta(\omega).
```
For a finite observation interval $`[-T/2,T/2]`$,
``` math
A_T(\omega):=\int_{-T/2}^{T/2}e^{i\omega t}\mathrm{d}t
=
2\frac{\sin(\omega T/2)}{\omega}.
```
Thus the finite-time conservation factor is a sinc kernel. The normalized distribution
``` math
D_T(\omega):=\frac{1}{2\pi}A_T(\omega)
=
\frac{1}{\pi}\frac{\sin(\omega T/2)}{\omega}
```
converges distributionally to $`\delta(\omega)`$:
``` math
D_T\to\delta.
```

<div class="proposition">

**Proposition 5** (Finite-time energy delta). *For every Schwartz function $`f`$,
``` math
\lim_{T\to\infty}\int_{\mathbb{R}}D_T(\omega)f(\omega)\mathrm{d}\omega=f(0).
```
Equivalently,
``` math
A_T(\omega)\to 2\pi\delta(\omega)
```
in $`\mathcal S'(\mathbb{R})`$.*

</div>

<div class="proof">

*Proof.* The factor $`D_T`$ is the inverse Fourier transform of the interval indicator divided by $`2\pi`$. Since the interval indicators increase to the constant function $`1`$ in the sense of tempered distributions, their inverse transforms converge to $`\delta`$. Equivalently, this is the standard distributional convergence of sinc kernels to the Dirac delta. ◻

</div>

## Finite-time transition probability and Fermi’s golden rule

The same finite-time kernel appears in ordinary time-dependent perturbation theory. If a transition has energy mismatch
``` math
\Delta E:=E_f-E_i,
```
then the first-order transition amplitude contains
``` math
A_T(\Delta E)=2\frac{\sin(\Delta E\,T/2)}{\Delta E}.
```
The probability contains
``` math
|A_T(\Delta E)|^2
=
4\frac{\sin^2(\Delta E\,T/2)}{(\Delta E)^2}.
```
The normalized golden-rule kernel is
``` math
F_T(\omega):=\frac{1}{2\pi T}|A_T(\omega)|^2
=
\frac{2}{\pi T}\frac{\sin^2(\omega T/2)}{\omega^2}.
```

<div class="proposition">

**Proposition 6** (Golden-rule delta as an infinite-time bookkeeping limit). *For every Schwartz function $`f`$,
``` math
\lim_{T\to\infty}\int_{\mathbb{R}}F_T(\omega)f(\omega)\mathrm{d}\omega=f(0).
```
Hence
``` math
\frac{1}{T}|A_T(\omega)|^2\to 2\pi\delta(\omega)
```
in the distributional sense.*

</div>

<div class="proof">

*Proof.* The kernel $`F_T`$ is nonnegative and normalized:
``` math
\int_{\mathbb{R}}F_T(\omega)\mathrm{d}\omega=1,
```
using $`\int_{-\infty}^{\infty}(\sin a\omega/\omega)^2\mathrm{d}\omega=\pi a`$. Its width is of order $`1/T`$, and its mass concentrates at $`\omega=0`$. Standard approximate-identity convergence gives the result. ◻

</div>

This is the operational version of the bookkeeping claim. A finite experiment does not produce a literal energy-conservation delta. It produces a sharply peaked finite-time kernel whose width is $`\Delta E\sim T^{-1}`$. The exact delta appears only in the asymptotic time limit used to define transition rates and $`S`$-matrix elements.

## Gaussian switching

Let
``` math
w_T(t)=e^{-t^2/(2T^2)}.
```
Then
``` math
\widehat w_T(\omega)=\sqrt{2\pi}T\,e^{-T^2\omega^2/2}.
```
The normalized kernel
``` math
\kappa_T(\omega)=\frac{T}{\sqrt{2\pi}}e^{-T^2\omega^2/2}
```
satisfies
``` math
\kappa_T\to\delta(\omega).
```
For finite $`T`$, energy mismatch is not enforced by a hard delta but suppressed with width
``` math
\Delta\omega\sim T^{-1}.
```

# Scattering interpretation

The exact $`S`$-matrix is an asymptotic object. Its momentum-conservation delta presupposes idealized infinite preparation and detection time, asymptotic free states, and translation-invariant interaction support. In a finite experiment one instead obtains wave packets, switching functions, detector profiles, and finite support. These replace the exact conservation delta by a sharply peaked but finite kernel.

This is already standard in scattering theory: exact $`S`$-matrix conservation laws arise after taking infinite-time and infinite-volume limits. The MTT contribution is interpretive and structural:
``` math
\boxed{
\text{the conservation delta is the singular shadow of exact bookkeeping closure.}
}
```
The finite experiment carries a finite bookkeeping kernel. The exact delta appears only when the bookkeeping ledger is idealized as infinitely extended and perfectly sharp.

This also clarifies why conservation deltas should not be confused with dynamical conservation itself. In a closed system with an exact symmetry, the conserved charge remains conserved. The finite kernel records the resolution of the effective scattering description, not a failure of the underlying symmetry.

# MTT triadic placement: circle bookkeeping

In the triadic carrier
``` math
\Xi=(\Psi,C,L,N),
```
the circle sector $`C`$ carries return and bookkeeping structure. Momentum conservation deltas fit most naturally into this sector.

The previous papers in this sequence associated:
``` math
L \longleftrightarrow \text{gauge redundancy and representative freedom},
```
``` math
N \longleftrightarrow \text{survivor selection and measurement outcomes}.
```
The present paper completes the triadic pattern:
``` math
C \longleftrightarrow \text{bookkeeping closure and conservation kernels}.
```

Thus:
``` math
\boxed{
(2\pi)^d\delta^{(d)}\!\left(\sum_i p_i\right)
=
\text{singular circle-sector bookkeeping kernel}.
}
```

# Relation to the contact-interaction paper

The contact-interaction paper showed that a local vertex
``` math
\int\phi(x)^n\mathrm{d}x
```
contains hidden position-space deltas enforcing coincidence of all participating fields at one point. The present paper addresses the Fourier-dual conservation delta.

The two are paired:
``` math
\text{position-space contact}
\quad\longleftrightarrow\quad
\text{momentum-space bookkeeping closure}.
```

A finite coherent vertex softens both sides:
``` math
\prod_j\delta(x-x_j)
\quad\leadsto\quad
\prod_jK_\epsilon(x,x_j),
```
and
``` math
\delta\!\left(\sum_i p_i\right)
\quad\leadsto\quad
\kappa_\epsilon\!\left(\sum_i p_i\right).
```

# Finite-width bookkeeping and apparent nonconservation

A finite kernel does not mean fundamental conservation fails. It means the effective description has finite support and finite resolution. The sharp conservation delta belongs to the ideal symmetry-and-asymptotic-support limit; the finite kernel belongs to the realized interaction window.

This distinction is important. The statement
``` math
\kappa_\epsilon(q)\neq\delta(q)
```
does not imply that the theory violates translation symmetry. It may simply mean that the experimental or effective interaction region is not the infinite translation-invariant idealization required to produce the exact delta.

Equivalently, finite-time broadening expresses switching or readout resolution, not necessarily nonconservation in the closed system. In MTT language, the finite kernel is only a candidate bookkeeping profile until selected geometry derives that profile.

# Scope of proof

``` math
\boxed{
\begin{minipage}{0.88\linewidth}
\textbf{Proved:} finite-width approximate identities, finite-time sinc kernels, and golden-rule kernels converge to conservation deltas distributionally.

\textbf{Standard physics input:} vertex conservation deltas arise from Fourier integration over translation-invariant support and from infinite-time scattering limits.

\textbf{Conditional MTT interpretation:} selected finite conservation kernels may encode
circle-sector bookkeeping; this paper does not derive their source.

\textbf{Not proved here:} a full derivation of all conservation laws from MTT, or a replacement for standard scattering theory.
\end{minipage}
}
```

# Conclusion

Momentum-conservation deltas are the Fourier form of exact translation-symmetry bookkeeping. A finite interaction region produces a finite mismatch kernel because its support or switching breaks the ideal translation-invariant setup. Infinite translation-invariant support recovers the exact Dirac delta.

Thus the conservation delta
``` math
(2\pi)^d\delta^{(d)}\left(\sum_i p_i\right)
```
may be represented as the distributional endpoint of finite-window kernels, but its physical authority is the Ward–Noether symmetry statement.

Together with the earlier papers, this supplies the following interpretive dictionary:
``` math
\text{lens: gauge redundancy},
\qquad
\text{nil: survivor selection},
\qquad
\text{circle: bookkeeping closure}.
```
The dictionary organizes roles; it does not derive the physical kernels or the conservation law from the triplet labels alone.

The next step is to combine these strands into a unified account of perturbative vertices in which position-space contact, momentum-space conservation, gauge redundancy, and finite coherent support are treated as different faces of the same admissible projection architecture.

<div class="thebibliography">

9

E. Noether, “Invariante Variationsprobleme,” *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse* (1918), 235–257. English translation: <https://arxiv.org/abs/physics/0503066>

J. C. Ward, “An Identity in Quantum Electrodynamics,” *Physical Review* **78** (1950), 182. <https://doi.org/10.1103/PhysRev.78.182>

Y. Takahashi, “On the generalized Ward identity,” *Il Nuovo Cimento* **6** (1957), 371–375. <https://doi.org/10.1007/BF02832514>

</div>
