---
abstract: |
  The preceding delta-projection papers established a structural dictionary: Dirac delta functions arise as singular limits of finite kernels, filters, shells, or selection operations. A natural objection is that this does not yet select a physical finite kernel. This paper addresses the first execution-level selection problem in the fixed-point regime of Modal Triplet Theory (MTT). We prove that if the incoherent sector of an evolve–project system decays with a quantified semigroup bound
  ``` math
  \|Q\Phi_t Q\| \le C_Q e^{-\lambda_\ast t},
  ```
  and if admissibility requires residual incoherent leakage below a tolerance $`\varepsilon_{\rm adm}`$, then the minimal admissible proper-time/heat-time is not a free regulator but is fixed by
  ``` math
  \tau_{\rm adm}=\frac{1}{\lambda_\ast}\log\frac{C_Q}{\varepsilon_{\rm adm}} .
  ```
  The corresponding canonical MTT kernel is
  ``` math
  K_{\rm adm}(x,y)
  =
  \big\langle x\big|P\,\chi(A)\,e^{-\tau_{\rm adm}A}\,\chi(A)\,P\big|y\big\rangle,
  ```
  where $`A`$ is the fixed-point linearized stabilization operator, $`P`$ is the coherent-sector projector, and $`\chi(A)`$ is the admissible spectral acceptance window. We then derive explicit error decompositions, show how the effective scale $`\Lambda_{\rm eff}\sim \tau_{\rm adm}^{-1/2}`$ follows from fixed-point data, and give a fully worked circle model in which $`(A,P,\chi,\tau_{\rm adm})`$ are all fixed once the geometry, spectral gap, damping constant, and admissibility tolerance are specified. The result is an execution bridge: the finite kernel used in downstream propagators, Green functions, contact loops, measurements, and constraint filters is selected by fixed-point damping data rather than chosen ad hoc.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: a1d96753b36d9ac55f9fa45ad99d103f1be61fcd0e746994b2d0999f5c849f84
paper_id: deriving-the-mtt-coherence-scale-from-fixed-point-dampi-55ce23b3
release_state: not_matched_to_zenodo
title: |
  Deriving the MTT Coherence Scale from Fixed–Point Damping  
  Canonical Proper-Time Kernels from Admissibility Thresholds
---

# Purpose and Claim Discipline

Earlier papers in the delta-projection program established the forward singular-limit dictionary
``` math
K_\epsilon \longrightarrow \delta .
```
That result is mathematically legitimate but, by itself, does not constitute new physical prediction. The decisive reverse problem is:
``` math
\text{MTT fixed-point data}
\Longrightarrow
(A,P,\chi,\tau)
\Longrightarrow
K_{\rm coh}
\Longrightarrow
\text{finite correction}.
```

This paper solves the first part of that reverse problem in the fixed-point regime. It proves that once a coherent fixed-point sector has quantified damping and an admissibility tolerance, the proper-time scale $`\tau`$ is fixed by the damping requirement. The kernel is then selected by functional calculus from the same operator data that generates stabilization.

## What is proved

We prove the following statements in a Hilbert-space fixed-point setting:

1.  A residual incoherent leakage bound determines a minimal admissible proper-time/heat-time $`\tau_{\rm adm}`$.

2.  This time scale canonically determines the proper-time filter $`e^{-\tau_{\rm adm}A}`$.

3.  Together with a coherent projector $`P`$ and spectral window $`\chi(A)`$, this fixes the kernel $`K_{\rm adm}`$.

4.  Error terms split into damping leakage, spectral-window truncation, and proper-time smoothing.

## What is not yet proved

This paper does not derive the Standard Model, the numerical physical value of $`\varepsilon_{\rm adm}`$, or a unique universal $`\tau`$ for all regimes. The result is regime-relative: given a fixed-point sector and its damping/admissibility data, the kernel is no longer arbitrary.

# Fixed-Point Data

Let $`\mathcal H`$ be a Hilbert space of modal perturbations around a coherent fixed point $`\Psi_\ast`$. Let
``` math
\mathcal H=\mathcal H_{\rm coh}\oplus \mathcal H_{\rm inc}
```
with orthogonal projectors
``` math
P:\mathcal H\to\mathcal H_{\rm coh},
\qquad
Q=I-P.
```

Let $`A\ge0`$ be a self-adjoint nonnegative operator representing the linearized stabilization operator around the fixed point. In the simplest gradient-flow case, $`A`$ is the Hessian or linearized dissipative generator of the closure/admissibility functional. We assume the incoherent sector has a positive gap:
``` math
A|_{\operatorname{Ran}Q}\ge \lambda_\ast I,
\qquad \lambda_\ast>0.
```

We also assume the coherent projection is compatible with the linearized operator:
``` math
[P,A]=0
```
on the relevant domain. This assumption is automatic when $`P`$ is a spectral/Riesz projector of $`A`$. If $`P`$ is only an admissible sector projector not exactly spectral for $`A`$, the results below apply after replacing commutation by the corresponding bounded commutator estimates; that perturbative extension is not needed for the core theorem.

Let $`\Phi_t`$ denote the linearized or locally linearized damping flow. In the linear model,
``` math
\Phi_t=e^{-tA}.
```
In the nonlinear local fixed-point model, the same estimates hold on an admissible slab after replacing $`C_Q`$ and $`\lambda_\ast`$ by the constants in the local semigroup/contractivity estimate.

# Admissibility Tolerance and Minimal Projection Time

The key new input is not a regulator. It is an admissibility threshold. Throughout this section, $`t`$ and $`\tau`$ denote heat/proper-time parameters for the semigroup $`e^{-tA}`$, not ordinary Lorentzian clock time. If $`A`$ is Laplace-type, then its eigenvalues have dimensions of energy squared in units $`\hbar=c=1`$, and $`t`$ or $`\tau`$ has dimensions of inverse energy squared.

<div class="definition">

**Definition 1** (Admissible residual leakage). Let $`\varepsilon_{\rm adm}\in(0,1)`$ be a fixed tolerance for incoherent leakage. We say that the projected stabilization step of duration $`t`$ is $`\varepsilon_{\rm adm}`$-admissible if
``` math
\|Q\Phi_t Q\|_{\mathcal H\to\mathcal H}
\le \varepsilon_{\rm adm}.
```

</div>

The tolerance $`\varepsilon_{\rm adm}`$ encodes the maximum residual noncoherent contribution allowed inside the effective description. It is not a universal constant in this paper; it is regime data. In an execution-level sector paper, it must be derived from closure-strain, detector resolution, observed error tolerance, or basin-separation data.

<div class="assumption">

**Assumption 2** (Incoherent damping bound). There exist constants $`C_Q\ge1`$ and $`\lambda_\ast>0`$ such that
``` math
\|Q\Phi_tQ\|\le C_Qe^{-\lambda_\ast t}
\qquad (t\ge0).
```

</div>

<div class="theorem">

**Theorem 3** (Minimal admissible proper-time). *Under the incoherent damping bound, any time $`t`$ satisfying
``` math
t\ge \frac{1}{\lambda_\ast}\log\frac{C_Q}{\varepsilon_{\rm adm}}
```
is $`\varepsilon_{\rm adm}`$-admissible. The minimal admissible proper-time determined by this bound is therefore
``` math
\boxed{
\tau_{\rm adm}
=
\frac{1}{\lambda_\ast}\log\frac{C_Q}{\varepsilon_{\rm adm}} .
}
```*

</div>

<div class="proof">

*Proof.* The damping estimate gives
``` math
\|Q\Phi_tQ\|\le C_Qe^{-\lambda_\ast t}.
```
Requiring the right-hand side to be at most $`\varepsilon_{\rm adm}`$ gives
``` math
C_Qe^{-\lambda_\ast t}\le \varepsilon_{\rm adm}.
```
Taking logarithms yields
``` math
-\lambda_\ast t\le \log \varepsilon_{\rm adm}-\log C_Q
```
and hence
``` math
t\ge \lambda_\ast^{-1}\log(C_Q/\varepsilon_{\rm adm}).
```
This is the claimed expression. $`\square`$ ◻

</div>

<div class="remark">

*Remark 4* (Why this is not a regulator choice). A heat-kernel regulator normally chooses $`\tau`$ as a computational cutoff. Here $`\tau_{\rm adm}`$ is fixed by a damping inequality and an admissibility threshold. The scale appears before any divergent integral is considered. It is selected by the fixed-point stabilization mechanism.

</div>

#### What has and has not been fixed.

This result fixes the proper-time scale once the damping data and admissibility tolerance are specified:
``` math
(C_Q,\lambda_\ast,\varepsilon_{\rm adm})\quad\Longrightarrow\quad \tau_{\rm adm}.
```
Thus $`\tau`$ is no longer an arbitrary Gaussian width. The remaining execution-level task is sharper: in each physical sector one must derive or constrain $`\varepsilon_{\rm adm}`$, together with $`A`$, $`P`$, $`\chi`$, $`C_Q`$, and $`\lambda_\ast`$, from closure strain, basin separation, detector resolution, measured error tolerance, or other sector data. This moves the freedom from an arbitrary regulator scale to physically interpretable admissibility data.

# Canonical Admissible Kernel

Let $`\chi:[0,\infty)\to[0,1]`$ be a bounded Borel spectral acceptance window. We assume $`\chi(A)`$ commutes with $`P`$, which follows if $`[P,A]=0`$. The window $`\chi`$ encodes retained coherent bandwidth. Typical choices are:

``` math
\chi(\lambda)=\mathbf 1_{\lambda\le\Lambda_{\rm coh}^2}
```
for a sharp spectral window, or a smooth cutoff satisfying
``` math
\chi(\lambda)\approx1 \quad (\lambda\le\Lambda_{\rm coh}^2),
\qquad
\chi(\lambda)\approx0 \quad (\lambda\ge\Lambda_{\rm inc}^2).
```

<div class="definition">

**Definition 5** (Canonical admissible MTT filter). The admissible fixed-point filter is
``` math
B_{\rm adm}
=
P\,\chi(A)\,e^{-\tau_{\rm adm}A}\,\chi(A)\,P .
```
When the corresponding operator has an integral kernel, we define
``` math
\boxed{
K_{\rm adm}(x,y)
=
\langle x|B_{\rm adm}|y\rangle .
}
```

</div>

This is the central execution object. It replaces the arbitrary $`K_\epsilon`$ of the dictionary papers.

<div class="theorem">

**Theorem 6** (Canonical kernel selection). *For fixed regime data
``` math
(A,P,\chi,C_Q,\lambda_\ast,\varepsilon_{\rm adm}),
```
the admissible kernel $`K_{\rm adm}`$ is uniquely determined by functional calculus. It is not freely adjustable.*

</div>

<div class="proof">

*Proof.* The data determine
``` math
\tau_{\rm adm}=\lambda_\ast^{-1}\log(C_Q/\varepsilon_{\rm adm}).
```
Given $`A`$, the spectral theorem uniquely defines $`\chi(A)`$ and $`e^{-\tau_{\rm adm}A}`$. Given $`P`$, the product
``` math
B_{\rm adm}=P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)P
```
is therefore uniquely determined as a bounded operator. If an integral kernel representation exists in the chosen function space, that kernel is the Schwartz kernel of $`B_{\rm adm}`$, hence is uniquely determined as a distribution and, under smoothing hypotheses, as a function. $`\square`$ ◻

</div>

# Error Decomposition

The full identity $`I`$ is not generally the correct target. In MTT, $`P`$ is a sector identity: it is the identity on the retained coherent sector, not on the full upstream space.

Let
``` math
B_{\rm adm}=P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)P.
```
For $`f\in\mathcal H`$,
``` math
f-B_{\rm adm}f
=
(I-P)f
+
P(I-\chi(A)^2)Pf
+
P\chi(A)\big(I-e^{-\tau_{\rm adm}A}\big)\chi(A)Pf .
```
This is the key execution decomposition.

<div class="theorem">

**Theorem 7** (Three-source correction bound). *Assume $`[P,A]=0`$ and $`0\le\chi\le1`$. Then
``` math
\|f-B_{\rm adm}f\|
\le
\|(I-P)f\|
+
\|(I-\chi(A)^2)Pf\|
+
\|\chi(A)(I-e^{-\tau_{\rm adm}A})\chi(A)Pf\|.
```
If $`f\in\operatorname{Ran}P`$ and $`\chi(A)f=f`$, then
``` math
\|f-B_{\rm adm}f\|
\le
\|(I-e^{-\tau_{\rm adm}A})f\|.
```
If additionally the retained spectral support of $`f`$ lies in $`[0,\Lambda^2]`$, then
``` math
\|f-B_{\rm adm}f\|
\le
\left(1-e^{-\tau_{\rm adm}\Lambda^2}\right)\|f\|.
```
For $`\tau_{\rm adm}\Lambda^2\ll1`$,
``` math
\|f-B_{\rm adm}f\|
\le
\tau_{\rm adm}\Lambda^2\|f\|+O(\tau_{\rm adm}^2\Lambda^4)\|f\|.
```*

</div>

<div class="proof">

*Proof.* The algebraic decomposition follows by adding and subtracting $`Pf`$, $`P\chi(A)^2Pf`$, and $`P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)Pf`$, using $`P^2=P`$ and commutation. The norm bound follows by the triangle inequality. If $`f\in\operatorname{Ran}P`$ and $`\chi(A)f=f`$, the first two terms vanish. On spectral support $`[0,\Lambda^2]`$, functional calculus gives
``` math
\|(I-e^{-\tau_{\rm adm}A})f\|
\le
\sup_{0\le\lambda\le\Lambda^2}|1-e^{-\tau_{\rm adm}\lambda}|\|f\|
=
(1-e^{-\tau_{\rm adm}\Lambda^2})\|f\|.
```
The small-$`\tau`$ expansion follows from $`1-e^{-x}=x+O(x^2)`$. $`\square`$ ◻

</div>

<div class="center">

| Term | Formula | Meaning |
|:---|:---|:---|
| Projection loss | $`(I-P)f`$ | discarded noncoherent sector |
| Window loss | $`(I-\chi(A)^2)Pf`$ | modes outside acceptance band |
| Proper-time smoothing | $`(I-e^{-\tau A})\chi(A)Pf`$ | finite coherence scale |

</div>

# Effective Scale

In flat or locally flat sectors where $`A\sim -\Delta`$, spectral values scale like $`\lambda\sim k^2`$. The damping factor becomes
``` math
e^{-\tau_{\rm adm}k^2}.
```
The characteristic scale at which damping becomes order one is
``` math
\tau_{\rm adm} k^2\sim1.
```
Thus
``` math
\boxed{
\Lambda_{\rm eff}\sim \tau_{\rm adm}^{-1/2}.
}
```
Using the fixed-point expression for $`\tau_{\rm adm}`$,
``` math
\boxed{
\Lambda_{\rm eff}
\sim
\left(
\frac{\lambda_\ast}{\log(C_Q/\varepsilon_{\rm adm})}
\right)^{1/2}.
}
```
This is the first explicit route from fixed-point damping data to a finite-width physical correction scale.

# Worked Model: Circle Sector

Let
``` math
X=S^1_R
```
be the circle of radius $`R`$, with coordinate $`\theta\in[0,2\pi)`$. Take
``` math
A=-\frac{1}{R^2}\partial_\theta^2.
```
The eigenfunctions are
``` math
\phi_n(\theta)=\frac{1}{\sqrt{2\pi R}}e^{in\theta},
\qquad
\lambda_n=\frac{n^2}{R^2},
\qquad n\in\mathbb Z.
```

Assume the coherent regime retains a symmetric band $`|n|\le N_{\rm coh}`$. Then
``` math
P=P_{N_{\rm coh}}
=
\sum_{|n|\le N_{\rm coh}}|\phi_n\rangle\langle\phi_n|.
```
For simplicity take $`\chi=1`$ on the retained band. Let the first discarded mode have
``` math
\lambda_\ast=\frac{(N_{\rm coh}+1)^2}{R^2}.
```
Assume $`C_Q=1`$. Then
``` math
\tau_{\rm adm}
=
\frac{R^2}{(N_{\rm coh}+1)^2}
\log\frac{1}{\varepsilon_{\rm adm}}.
```

The canonical kernel is
``` math
K_{\rm adm}(\theta,\theta')
=
\frac{1}{2\pi R}
\sum_{|n|\le N_{\rm coh}}
\exp\left[
-\frac{\tau_{\rm adm}n^2}{R^2}
\right]
e^{in(\theta-\theta')}.
```
Substituting $`\tau_{\rm adm}`$,
``` math
K_{\rm adm}(\theta,\theta')
=
\frac{1}{2\pi R}
\sum_{|n|\le N_{\rm coh}}
\exp\left[
-\frac{n^2}{(N_{\rm coh}+1)^2}
\log\frac{1}{\varepsilon_{\rm adm}}
\right]
e^{in(\theta-\theta')}.
```

The effective mode scale is determined by
``` math
\exp\left(-\tau_{\rm adm}\frac{n^2}{R^2}\right)\sim e^{-1}
\quad\Longleftrightarrow\quad
|n|_{\rm eff}\sim R\,\tau_{\rm adm}^{-1/2}
=\frac{R}{\sqrt{\tau_{\rm adm}}}.
```
Substituting
``` math
\tau_{\rm adm}=\frac{R^2}{(N_{\rm coh}+1)^2}\log\frac{1}{\varepsilon_{\rm adm}},
```
gives the dimensionless retained-mode scale
``` math
|n|_{\rm eff}
\sim
\frac{N_{\rm coh}+1}{\sqrt{\log(1/\varepsilon_{\rm adm})}}.
```

This example shows the selection mechanism explicitly. Once $`R`$, $`N_{\rm coh}`$, and $`\varepsilon_{\rm adm}`$ are fixed, the kernel is fixed. No Gaussian width is chosen by hand.

# Application to Propagator Corrections

The immediate link to the MTT-corrected propagator paper is:
``` math
\boxed{
\Delta_{\rm adm}(k)
=
\frac{e^{-\tau_{\rm adm}k^2}}{k^2+m^2},
\qquad
\tau_{\rm adm}
=
\lambda_\ast^{-1}\log\frac{C_Q}{\varepsilon_{\rm adm}}.
}
```
Thus the exponential factor is not chosen at the propagator stage. It is inherited from the minimal fixed-point damping time required by admissibility.

For a scalar Euclidean sector with ordinary propagator
``` math
\Delta_0(k)=\frac{1}{k^2+m^2},
```
the admissible MTT-corrected propagator becomes
``` math
\boxed{
\Delta_{\rm adm}(k)
=
\frac{e^{-\tau_{\rm adm}k^2}}{k^2+m^2}
}
```
in the flat-sector model.

The leading low-momentum correction is
``` math
\Delta_{\rm adm}(k)
=
\frac{1}{k^2+m^2}
-
\tau_{\rm adm}\frac{k^2}{k^2+m^2}
+
O(\tau_{\rm adm}^2k^4).
```
Thus an observable probing momentum scale $`E`$ is insensitive to the correction when
``` math
\tau_{\rm adm}E^2\ll1.
```
Equivalently,
``` math
E\ll \Lambda_{\rm eff}\sim\tau_{\rm adm}^{-1/2}.
```

# Phenomenological Reading

In natural units $`\hbar=c=1`$, $`\tau_{\rm adm}`$ has units of inverse mass squared in flat momentum-space sectors:
``` math
[\tau_{\rm adm}]=E^{-2}.
```
The length scale associated with the kernel is
``` math
\ell_{\rm coh}\sim \sqrt{\tau_{\rm adm}}.
```
If an experiment tests locality or propagator behavior up to energy $`E_{\rm max}`$ with fractional tolerance $`\eta_{\rm exp}`$, then a rough necessary condition is
``` math
\tau_{\rm adm}E_{\rm max}^2\lesssim \eta_{\rm exp}.
```
Hence
``` math
\Lambda_{\rm eff}
=
\tau_{\rm adm}^{-1/2}
\gtrsim
\frac{E_{\rm max}}{\sqrt{\eta_{\rm exp}}}.
```
A real bound requires matching the filtered propagator into the relevant scattering amplitude and observable. The inequality above is only the universal scaling estimate.

# Why This Solves the Kernel-Choice Objection

The criticism of the earlier dictionary papers was correct: showing
``` math
K_\epsilon\to\delta
```
does not identify which $`K_\epsilon`$ nature selects.

The present paper supplies the missing fixed-point selection rule:
``` math
(A,P,\chi,C_Q,\lambda_\ast,\varepsilon_{\rm adm})
\Longrightarrow
\tau_{\rm adm}
\Longrightarrow
K_{\rm adm}.
```
Thus the kernel is canonical inside a regime. It is not a universal constant and not an arbitrary regulator. It is selected by fixed-point damping and admissibility.

# Next Execution Targets

The next tasks are sector-specific:

1.  derive $`A`$, $`P`$, $`\chi`$, $`\lambda_\ast`$, and $`\varepsilon_{\rm adm}`$ for a concrete MTT sector;

2.  compute $`\tau_{\rm adm}`$;

3.  insert the resulting kernel into propagators, loops, measurement effects, or spectral widths;

4.  compare the correction scale to measured data.

The most plausible first physical sector is the neutrino soft sector, because the existing corpus already contains local nil-basin structure, soft-mode Hessians, ordering branches, and measured mass-splitting inputs.

# Conclusion

This paper converts the delta-projection program from a structural dictionary into an execution rule. In the fixed-point regime, the finite kernel is not chosen by hand. It is determined by damping data, spectral gap, admissibility tolerance, coherent projection, and spectral acceptance.

The central formula is
``` math
\boxed{
\tau_{\rm adm}
=
\frac{1}{\lambda_\ast}\log\frac{C_Q}{\varepsilon_{\rm adm}}
}
```
and the corresponding kernel is
``` math
\boxed{
K_{\rm adm}(x,y)
=
\big\langle x\big|P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)P\big|y\big\rangle.
}
```
This gives the first rigorous answer to the reverse problem:
``` math
\boxed{
\text{MTT fixed-point data}
\Rightarrow
K_{\rm adm}
\Rightarrow
\text{finite correction}.
}
```
