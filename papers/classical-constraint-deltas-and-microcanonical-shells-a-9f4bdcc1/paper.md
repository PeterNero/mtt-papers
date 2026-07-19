---
abstract: |
  Dirac delta functions enter classical and statistical mechanics most prominently as constraint distributions, for example in microcanonical measures
  ``` math
  \rho_E(z)\propto \delta(H(z)-E)
  ```
  and in phase-space integrals restricted to a constraint surface. In the delta/projection program of Modal Triplet Theory (MTT), such deltas are not treated as primitive objects. They are re-read as singular limits of finite admissibility shells: finite-thickness neighborhoods around constraint surfaces that become exact only when the allowed tolerance is sent to zero.

  This paper develops the classical/statistical-mechanical member of that program. We prove a coarea-based shell theorem: for a regular value $`E`$ of a smooth Hamiltonian $`H:M\to\mathbb R`$, normalized approximate identities
  ``` math
  \eta_\varepsilon(H(z)-E)
  ```
  converge distributionally to the surface delta $`\delta(H-E)`$, with the standard coarea measure $`d\Sigma/\left\lvert \nabla H \right\rvert`$. We then formulate finite-thickness microcanonical shells, show their convergence to the sharp microcanonical measure, and interpret the result in MTT language: $`\delta(H-E)`$ is the zero-thickness limit of an admissibility shell around a bookkeeping constraint.

  The paper also distinguishes three layers often conflated in formal notation: exact constraint surfaces, finite experimental/thermodynamic tolerance shells, and singular delta notation. The result is a concrete extension of the delta/projection program from QFT and measurement to classical and statistical mechanics.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: 8ce883c7bbdaf736a51ebbf1b04a0722785727258a329765ebc628e2d74b4049
paper_id: classical-constraint-deltas-and-microcanonical-shells-a-9f4bdcc1
release_state: not_matched_to_zenodo
title: |
  Classical Constraint Deltas and Microcanonical Shells  
  Admissibility-Shell Limits in Modal Triplet Theory
---

*Part VI of VI in the Fixed Points series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

# Purpose and claim discipline

The preceding papers in this sequence treated Dirac deltas as singular shadows of projection in several settings: coherent projection kernels, point-source Green functions, gauge fixing, measurement effects, contact interactions, scattering bookkeeping, spectral peaks, and white-noise correlations. This paper treats the classical and statistical-mechanical case.

The guiding example is the microcanonical expression
``` math
\Omega(E)=\int_M \delta(H(z)-E)\,dz,
```
where $`M`$ is phase space and $`H`$ is the Hamiltonian. Standard notation says this integral is restricted to the energy surface $`H=E`$. The MTT interpretation asks: what finite admissible process has been idealized by the delta?

The answer developed here is:
``` math
\boxed{\delta(H-E)=\text{zero-thickness limit of an admissibility shell around }H=E.}
```

## Non-claims

This paper does not claim that classical mechanics is wrong, that the microcanonical ensemble is invalid, or that distributional constraints should be abandoned. It proves a standard coarea/approximate-identity result and then gives its MTT interpretation.

The proved mathematical statement is narrow: finite-thickness shell densities converge to the surface delta under regularity hypotheses. The MTT claim is interpretive: the sharp delta is the singular encoding obtained when finite admissibility tolerance is idealized away.

# Constraint deltas in phase space

Let $`M`$ be an $`n`$-dimensional smooth Riemannian manifold, interpreted as a configuration or phase space, with volume measure $`d\mu`$. Let
``` math
C:M\to\mathbb{R}
```
be a smooth constraint function. The formal expression
``` math
\delta(C(z))
```
restricts integrals to the constraint surface $`C^{-1}(0)`$. More generally,
``` math
\delta(H(z)-E)
```
restricts to the energy surface $`H^{-1}(E)`$.

When $`0`$ is a regular value of $`C`$, the coarea formula gives the rigorous meaning:
``` math
\int_M f(z)\delta(C(z))\,d\mu(z)
  =
  \int_{C^{-1}(0)} \frac{f(z)}{\left\lvert \nabla C(z) \right\rvert}\,d\Sigma(z).
```
Likewise, if $`E`$ is a regular value of $`H`$,
``` math
\int_M f(z)\delta(H(z)-E)\,d\mu(z)
  =
  \int_{H^{-1}(E)} \frac{f(z)}{\left\lvert \nabla H(z) \right\rvert}\,d\Sigma_E(z).
```

The present paper replaces the sharp delta by a finite shell kernel.

<div class="remark">

*Remark 1* (Regular-value caveat). The clean surface-delta formula requires the target value to be regular. For $`\delta(H-E)`$, this means
``` math
\nabla H(z)\neq 0 \qquad \text{for all } z\in H^{-1}(E).
```
At critical energies the coarea density may become singular, the topology of the level set can change, and the finite-shell limit may require separate analysis. All theorem-level statements below are made in the regular-value regime.

</div>

<div class="definition">

**Definition 2** (Approximate identity on the constraint variable). Let $`\eta\in C_c^\infty(\mathbb{R})`$, $`\eta\ge0`$, and
``` math
\int_{\mathbb{R}}\eta(u)\,du=1.
```
For $`\varepsilon>0`$, define
``` math
\eta_\varepsilon(u):=\frac1\varepsilon\eta\!\left(\frac{u}{\varepsilon}\right).
```
Then $`\eta_\varepsilon\to\delta_0`$ in distributions on $`\mathbb{R}`$.

</div>

<div class="definition">

**Definition 3** (Finite admissibility shell). For a constraint $`C:M\to\mathbb{R}`$, the finite admissibility shell of width $`\varepsilon`$ around $`C=0`$ is the weighted density
``` math
\eta_\varepsilon(C(z))\,d\mu(z).
```
For an energy function $`H`$, the shell around energy $`E`$ is
``` math
\eta_\varepsilon(H(z)-E)\,d\mu(z).
```

</div>

# Gaussian admissibility shells

A useful non-compact approximate identity is the Gaussian shell
``` math
\eta_\varepsilon(u)
  =
  \frac{1}{\sqrt{2\pi}\varepsilon}
  \exp\!\left(-\frac{u^2}{2\varepsilon^2}\right).
```
For an energy constraint this gives
``` math
\eta_\varepsilon(H(z)-E)
  =
  \frac{1}{\sqrt{2\pi}\varepsilon}
  \exp\!\left(-\frac{(H(z)-E)^2}{2\varepsilon^2}\right).
```
This is often the most natural finite-admissibility model: configurations are not discarded abruptly outside a hard band, but are penalized according to squared constraint mismatch. In the limit $`\varepsilon\downarrow0`$, the Gaussian shell converges to the sharp surface delta in the same distributional sense as the compactly supported approximate identities used in the theorem below.

More generally, any family $`\eta_\varepsilon`$ forming an approximate identity in the constraint variable gives the same limiting surface measure. The choice of kernel therefore describes the finite-tolerance profile, not the sharp limiting constraint.

# Coarea shell theorem

<div id="thm:shell" class="theorem">

**Theorem 4** (Constraint shell convergence). *Let $`M`$ be a smooth Riemannian manifold and let $`C:M\to\mathbb{R}`$ be smooth. Let $`0`$ be a regular value of $`C`$. Suppose $`f\in C_c^\infty(M)`$, and suppose the support of $`f`$ meets only a compact region on which $`\nabla C\neq0`$ in a neighborhood of $`C^{-1}(0)`$. Then
``` math
\lim_{\varepsilon\downarrow0}
  \int_M f(z)\eta_\varepsilon(C(z))\,d\mu(z)
  =
  \int_{C^{-1}(0)} \frac{f(z)}{\left\lvert \nabla C(z) \right\rvert}\,d\Sigma(z).
```
Equivalently,
``` math
\eta_\varepsilon(C)\to \delta(C)
```
as distributions on the tested region.*

</div>

<div class="proof">

*Proof.* By the coarea formula, for sufficiently small $`\varepsilon`$,
``` math
\int_M f(z)\eta_\varepsilon(C(z))\,d\mu(z)
  =
  \int_{\mathbb{R}}\eta_\varepsilon(c)
  \left(
    \int_{C^{-1}(c)}\frac{f(z)}{\left\lvert \nabla C(z) \right\rvert}\,d\Sigma_c(z)
  \right)dc.
```
Define
``` math
F(c):=\int_{C^{-1}(c)}\frac{f(z)}{\left\lvert \nabla C(z) \right\rvert}\,d\Sigma_c(z).
```
Because $`0`$ is a regular value and $`f`$ has compact support in a region where $`\nabla C\neq0`$, the regular level sets form a smooth local family and $`F(c)`$ is continuous near $`c=0`$. Therefore
``` math
\int_{\mathbb{R}}\eta_\varepsilon(c)F(c)\,dc\to F(0)
```
by the approximate-identity property of $`\eta_\varepsilon`$. This gives
``` math
F(0)=\int_{C^{-1}(0)}\frac{f(z)}{\left\lvert \nabla C(z) \right\rvert}\,d\Sigma(z).
```
 ◻

</div>

<div id="cor:energy" class="corollary">

**Corollary 5** (Energy-shell convergence). *Let $`H:M\to\mathbb{R}`$ be smooth and let $`E`$ be a regular value. Then, for $`f\in C_c^\infty(M)`$,
``` math
\lim_{\varepsilon\downarrow0}
  \int_M f(z)\eta_\varepsilon(H(z)-E)\,d\mu(z)
  =
  \int_{H^{-1}(E)}\frac{f(z)}{\left\lvert \nabla H(z) \right\rvert}\,d\Sigma_E(z).
```
Thus
``` math
\eta_\varepsilon(H-E)\to\delta(H-E)
```
distributionally.*

</div>

# Microcanonical shells

The standard microcanonical density is often written
``` math
\rho_E(z)=\frac{\delta(H(z)-E)}{\Omega(E)},
  \qquad
  \Omega(E)=\int_M\delta(H(z)-E)\,d\mu(z).
```
This is a surface measure on the energy shell.

The finite-shell version is
``` math
\rho_{E,\varepsilon}(z)
  =
  \frac{\eta_\varepsilon(H(z)-E)}{\Omega_\varepsilon(E)},
  \qquad
  \Omega_\varepsilon(E)
  =
  \int_M \eta_\varepsilon(H(z)-E)\,d\mu(z).
```

<div class="proposition">

**Proposition 6** (Microcanonical shell convergence). *Assume $`E`$ is a regular value of $`H`$ and that the relevant shells are contained in a compact region, or that the integrals are finite by confinement. If
``` math
\Omega(E):=\int_{H^{-1}(E)}\frac{1}{\left\lvert \nabla H \right\rvert}\,d\Sigma_E
```
is finite and nonzero, then for every test function $`f`$,
``` math
\int_M f(z)\rho_{E,\varepsilon}(z)\,d\mu(z)
  \to
  \frac{1}{\Omega(E)}
  \int_{H^{-1}(E)}\frac{f(z)}{\left\lvert \nabla H(z) \right\rvert}\,d\Sigma_E(z).
```*

</div>

<div class="proof">

*Proof.* Apply <a href="#cor:energy" data-reference-type="ref+Label" data-reference="cor:energy">5</a> to $`f`$ and to $`1`$. The denominator $`\Omega_\varepsilon(E)`$ converges to $`\Omega(E)`$, which is finite and nonzero. Taking the quotient gives the result. ◻

</div>

Thus the sharp microcanonical ensemble is the zero-thickness limit of ordinary finite-width energy shells.

# Worked example: one-dimensional energy shell

Consider the one-dimensional phase space variable $`p\in\mathbb{R}`$ with
``` math
H(p)=\frac{p^2}{2m}.
```
For $`E>0`$, the energy shell consists of two points
``` math
p_\pm=\pm\sqrt{2mE}.
```
For a test function $`f`$,
``` math
\int_{\mathbb{R}} f(p)\delta\!\left(\frac{p^2}{2m}-E\right)\,dp
  =
  \sum_{\sigma=\pm}
  \frac{f(p_\sigma)}{\left\lvert H'(p_\sigma) \right\rvert}.
```
Since
``` math
H'(p)=\frac{p}{m},
```
we get
``` math
\int_{\mathbb{R}} f(p)\delta\!\left(\frac{p^2}{2m}-E\right)\,dp
  =
  \frac{m}{\sqrt{2mE}}
  \left[f(\sqrt{2mE})+f(-\sqrt{2mE})\right].
```
A finite shell replaces this by
``` math
\int_{\mathbb{R}} f(p)\eta_\varepsilon\!\left(\frac{p^2}{2m}-E\right)\,dp,
```
which samples a finite neighborhood of both energy-shell points. The exact delta result is recovered as $`\varepsilon\downarrow0`$.

This example makes the interpretation visible: the delta does not describe a new object on phase space. It is the zero-thickness limit of a finite energy tolerance.

# Multiple constraints and admissibility

The same structure appears for several simultaneous constraints
``` math
C_a(z)=0,\qquad a=1,\dots,r.
```
Let
``` math
C=(C_1,\dots,C_r):M\to\mathbb{R}^r.
```
If $`0`$ is a regular value of $`C`$, then the constraint surface $`C^{-1}(0)`$ is a smooth submanifold of codimension $`r`$. The sharp formal density is
``` math
\delta^{(r)}(C(z)).
```
A finite admissibility tube is obtained from an approximate identity
``` math
\eta_\varepsilon^{(r)}(u)
  =
  \varepsilon^{-r}\eta^{(r)}(u/\varepsilon),
  \qquad
  \int_{\mathbb{R}^r}\eta^{(r)}(u)\,du=1,
```
by writing
``` math
\eta_\varepsilon^{(r)}(C(z))\,d\mu(z).
```

<div id="thm:multi-shell" class="theorem">

**Theorem 7** (Multiple-constraint shell convergence). *Let $`C:M\to\mathbb{R}^r`$ be smooth and let $`0`$ be a regular value. Let $`f\in C_c^\infty(M)`$ be supported in a region where $`DC`$ has full rank $`r`$ near $`C^{-1}(0)`$. Then
``` math
\lim_{\varepsilon\downarrow0}
  \int_M f(z)\eta_\varepsilon^{(r)}(C(z))\,d\mu(z)
  =
  \int_{C^{-1}(0)}
  \frac{f(z)}{J_C(z)}\,d\Sigma(z),
```
where
``` math
J_C(z)
  =
  \sqrt{\det\!\left(DC(z)DC(z)^\ast\right)}
```
is the normal Jacobian appearing in the multidimensional coarea formula. Equivalently,
``` math
\eta_\varepsilon^{(r)}(C)\to\delta^{(r)}(C)
```
distributionally on the tested regular region.*

</div>

<div class="proof">

*Proof.* The multidimensional coarea formula gives
``` math
\int_M f(z)\eta_\varepsilon^{(r)}(C(z))\,d\mu(z)
  =
  \int_{\mathbb{R}^r}\eta_\varepsilon^{(r)}(u)
  \left(
    \int_{C^{-1}(u)}\frac{f(z)}{J_C(z)}\,d\Sigma_u(z)
  \right)du .
```
The inner expression is continuous near $`u=0`$ under the stated regularity and compact support assumptions. The approximate-identity property on $`\mathbb{R}^r`$ then gives the claimed limit. ◻

</div>

This multiconstraint version is the bridge to Hamiltonian constraints, gauge constraints, and path-integral constraint factors. It is also the precise classical counterpart of replacing a hard constraint surface by a finite admissibility tube.

# MTT interpretation

In MTT terms, a classical constraint delta is a bookkeeping/admissibility object. It does not merely localize in ordinary space; it restricts the effective description to a surface of allowed states.

The triadic placement is:

<div class="center">

| Standard object | MTT reading |
|:---|:---|
| $`\delta(H-E)`$ | zero-thickness energy admissibility shell |
| $`\delta(C)`$ | sharp constraint-surface selection |
| $`\eta_\varepsilon(H-E)`$ | finite tolerance around bookkeeping constraint |
| microcanonical ensemble | normalized admissibility shell measure |
| coarea factor $`1/\left\lvert \nabla H \right\rvert`$ | projection Jacobian from phase volume to constraint surface |

</div>

Thus the classical constraint delta belongs primarily to the bookkeeping side of the program. It is closest to the circle role: exact return or conservation closure. However, when constraint enforcement selects a reduced representative surface, it also has the same formal profile as the selection deltas studied in the gauge and measurement papers.

# Canonical weighting as soft admissibility

The canonical ensemble
``` math
\rho_\beta(z)=\frac{e^{-\beta H(z)}}{Z(\beta)}
```
is not a delta shell and should not be confused with a microcanonical constraint. It does not restrict the system to one energy surface. Instead, it weights many energy surfaces with a Boltzmann factor.

Nevertheless, from the present perspective it is useful as a contrasting example:
``` math
\delta(H-E)
  \quad\text{is hard shell selection,}
```
whereas
``` math
e^{-\beta H}
  \quad\text{is soft energetic weighting.}
```
Thus the canonical ensemble belongs to the broader family of finite weighting procedures, while the microcanonical delta is the zero-thickness limit of a finite constraint shell. The MTT reading should therefore distinguish hard admissibility selection from soft statistical weighting.

# Constraint deltas versus physical conservation

Finite shell width does not necessarily mean that the underlying closed system violates the constraint. It may mean only that the effective description carries finite tolerance, finite resolution, or finite observational access.

For example, a microcanonical shell of width $`\varepsilon`$ can represent:

1.  experimental energy resolution;

2.  thermodynamic coarse graining;

3.  finite admissibility tolerance in the effective description;

4.  deliberate smoothing of an otherwise singular surface measure.

The sharp delta is the idealization in which this tolerance is sent to zero.

# Relation to the delta/projection program

The present paper adds the classical/statistical entry:

<div class="center">

| Delta occurrence                     | Finite object                    |
|:-------------------------------------|:---------------------------------|
| $`\delta(x-y)`$                      | coherent projection kernel       |
| $`LG=\delta`$                        | coherent finite source           |
| $`\delta(G[A])`$                     | finite gauge-section tube        |
| $`|x\rangle\langle x|`$              | finite measurement effect        |
| $`\phi(x)^n`$ contact vertex         | finite coherent overlap vertex   |
| $`\delta(\sum p_i)`$                 | finite bookkeeping window        |
| $`\delta(E_f-E_i)`$                  | finite-time transition kernel    |
| $`\delta(E-E_0)`$ spectral peak      | finite-lifetime resonance        |
| $`\delta(t-s)`$ noise correlation    | finite-memory disturbance kernel |
| $`\delta(H-E)`$ microcanonical shell | finite admissibility shell       |

</div>

The unifying rule is unchanged:

``` math
\boxed{\text{A delta marks where a finite admissible process has been idealized as exact.}}
```

# Scope of proof

<div class="center">

| Layer | Status |
|:---|:---|
| Coarea shell convergence | proved under regular-value and compactness/finite-integral hypotheses |
| Microcanonical shell convergence | proved as normalized consequence of coarea convergence |
| Multiple-constraint shell convergence | proved under regular-value/full-rank hypotheses |
| MTT admissibility-shell reading | interpretive classification |
| Derivation of classical constraints from MTT | not claimed here |

</div>

# Conclusion

Classical and statistical mechanics use Dirac deltas to restrict phase-space integrals to constraint surfaces. The microcanonical density $`\delta(H-E)`$ is the most familiar example. This paper showed that such deltas arise as zero-thickness limits of finite admissibility shells.

The rigorous mathematical content is the coarea shell theorem:
``` math
\eta_\varepsilon(H-E)\to\delta(H-E)
```
distributionally, with the correct surface measure $`d\Sigma_E/\left\lvert \nabla H \right\rvert`$. The MTT interpretation is that sharp classical constraints are not primitive delta objects; they are singular encodings of finite tolerance shells around admissible bookkeeping surfaces.

Thus the delta/projection program extends naturally into classical and statistical mechanics. The same pattern repeats: finite admissible structure first, singular delta notation only as an ideal limit.
