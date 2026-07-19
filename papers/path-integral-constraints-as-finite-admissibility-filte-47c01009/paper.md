---
abstract: |
  Delta functionals occur throughout path-integral physics: as hard constraints, gauge-fixing conditions, phase-space reductions, Lagrange-multiplier insertions, and exact selection of histories. In standard formalism they are usually treated as distributional devices. This paper continues the delta/projection program by showing that a delta functional may be understood as the zero-width limit of a finite admissibility filter over histories. The rigorous core is finite-dimensional: for a smooth constraint map $`C:M\to\mathbb R^m`$ with $`0`$ a regular value, normalized Gaussian filters
  ``` math
  \mathcal K_\varepsilon(C(x))=(2\pi\varepsilon^2)^{-m/2}\exp(-|C(x)|^2/2\varepsilon^2)
  ```
  converge, as measures, to the surface delta $`\delta(C(x))\,dx`$, including the standard Jacobian factor from the coarea formula. The infinite-dimensional path-integral statement is then treated as a formal extension requiring regularization. In MTT language, the hard delta $`\delta[C]`$ is the singular limit of a finite admissibility weight $`\exp[-J_{\mathrm{adm}}/\epsilon^2]`$. This also clarifies the relation between multiplier representations, large-penalty localization, and finite admissibility tubes, and unifies the interpretation of classical constraint shells, gauge-fixing deltas, and path-integral restrictions: exact constraint enforcement is the zero-width idealization of finite admissibility selection.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: 9c9b073f278d04d4f5f3963fdc3fcd829e1bbe4374860ba64b726b5b6b218e92
paper_id: path-integral-constraints-as-finite-admissibility-filte-47c01009
release_state: not_matched_to_zenodo
title: |
  Path Integral Constraints as Finite Admissibility Filters  
  Delta Functionals, Soft Constraints, and Projection in Modal Triplet Theory
---

# Purpose and claim discipline

The previous papers in this sequence reinterpreted several recurring delta functions: identity kernels, point sources, gauge slices, measurement projectors, contact vertices, conservation deltas, spectral peaks, white noise, and microcanonical shells. The present paper treats the path-integral version:
``` math
\delta[C[\phi]] .
```

The guiding claim is:
``` math
\boxed{\delta[C]=\text{zero-width limit of a finite admissibility filter over histories}.}
```

This paper has two layers.

<div class="center">

| Layer | Status |
|:---|:---|
| Finite-dimensional constraint theorem | rigorous, proved using the coarea formula |
| Functional-integral extension | formal; requires regulator, measure choice, and anomaly control |
| MTT interpretation | structural; finite admissibility weights replace hard delta constraints |

</div>

The paper does not claim to define all path integrals nonperturbatively. It isolates one mathematical pattern: hard functional deltas are singular limits of finite-width constraint filters.

# From hard constraints to finite filters

A standard constrained path integral has the schematic form
``` math
Z=\int \mathcal D\phi\; \delta[C[\phi]]\,e^{iS[\phi]/\hbar}.
```
The delta functional enforces exact membership in the constraint surface $`C[\phi]=0`$.

The finite-filter replacement is
``` math
\delta[C[\phi]]
\quad\leadsto\quad
\mathcal K_\varepsilon[C[\phi]]
=
\exp\!\left(-\frac{1}{2\varepsilon^2}\|C[\phi]\|^2\right),
```
possibly with normalization and with the norm chosen by an admissibility metric. The finite-filter path integral is then
``` math
Z_\varepsilon
=
\int \mathcal D\phi\;
\mathcal K_\varepsilon[C[\phi]]\,
e^{iS[\phi]/\hbar}.
```

In Euclidean signature one may instead write
``` math
Z_\varepsilon^{E}
=
\int \mathcal D\phi\;
\exp\!\left(
-S_E[\phi]
-\frac{1}{2\varepsilon^2}\|C[\phi]\|^2
\right).
```
This is a soft-constraint or penalty formulation. The hard constraint is recovered only in the $`\varepsilon\downarrow0`$ limit.

# Finite-dimensional theorem

Let $`M`$ be an $`n`$-dimensional smooth Riemannian manifold with volume measure $`d\mu`$. Let
``` math
C:M\to\mathbb R^m,\qquad m\le n,
```
be a smooth constraint map, and assume $`0`$ is a regular value. Then
``` math
\Sigma:=C^{-1}(0)
```
is a smooth submanifold of codimension $`m`$.

Define the constraint Jacobian
``` math
J_C(x):=\sqrt{\det\bigl(DC_x\,DC_x^{\ast}\bigr)},
```
where $`DC_x:T_xM\to\mathbb R^m`$ and the adjoint is taken with respect to the Riemannian metric on $`M`$ and the Euclidean metric on $`\mathbb R^m`$.

The surface delta is defined by
``` math
\int_M f(x)\,\delta(C(x))\,d\mu(x)
=
\int_{\Sigma}\frac{f(x)}{J_C(x)}\,d\sigma(x),
```
for test functions $`f`$, where $`d\sigma`$ is the induced hypersurface measure.

## Gaussian constraint filters

Let
``` math
k_\varepsilon(u):=(2\pi\varepsilon^2)^{-m/2}\exp(-|u|^2/2\varepsilon^2).
```

<div class="theorem">

**Theorem 1** (Gaussian constraint filters converge to surface deltas). *Let $`f\in C_c^\infty(M)`$. Under the regular-value assumption above,
``` math
\lim_{\varepsilon\downarrow0}
\int_M f(x) k_\varepsilon(C(x))\,d\mu(x)
=
\int_{\Sigma}\frac{f(x)}{J_C(x)}\,d\sigma(x).
```
Equivalently,
``` math
k_\varepsilon(C(x))\,d\mu(x)\;\longrightarrow\;\delta(C(x))\,d\mu(x)
```
weakly as measures.*

</div>

<div class="proof">

*Proof.* By the coarea formula, for any integrable $`h`$,
``` math
\int_M h(x)J_C(x)\,d\mu(x)
=
\int_{\mathbb R^m}
\left(\int_{C^{-1}(u)} h(x)\,d\sigma_u(x)\right)\,du .
```
Apply this with
``` math
h(x)=\frac{f(x)k_\varepsilon(C(x))}{J_C(x)} ,
```
which is well-defined on a neighborhood of $`\Sigma`$ because $`0`$ is a regular value and $`f`$ has compact support. Then
``` math
\int_M f(x)k_\varepsilon(C(x))\,d\mu(x)
=
\int_{\mathbb R^m} k_\varepsilon(u)
\left[
\int_{C^{-1}(u)}
\frac{f(x)}{J_C(x)}\,d\sigma_u(x)
\right]du .
```
For $`u`$ near $`0`$, the bracketed expression is smooth by the regular-level-set theorem and compact support of $`f`$. Denote it by $`F(u)`$. Since $`k_\varepsilon`$ is an approximate identity on $`\mathbb R^m`$,
``` math
\int_{\mathbb R^m} k_\varepsilon(u)F(u)\,du\to F(0).
```
But
``` math
F(0)=\int_{\Sigma}\frac{f(x)}{J_C(x)}\,d\sigma(x).
```
This proves the claim. ◻

</div>

# General admissibility kernels

Gaussian filters are convenient but not essential. Let
``` math
k_\varepsilon(u)=\varepsilon^{-m}k(u/\varepsilon),
```
where $`k\in C_c^\infty(\mathbb R^m)`$, $`k\ge0`$, and $`\int k(u)\,du=1`$. The same proof gives:
``` math
k_\varepsilon(C(x))\,d\mu(x)\to \delta(C(x))\,d\mu(x).
```

Thus the hard delta does not depend on the detailed shape of the finite filter. The detailed shape controls finite-$`\varepsilon`$ corrections. In MTT language, those corrections encode finite admissibility width.

# Path integrals: formal functional extension

The formal field-theoretic analogue is obtained by replacing $`x\in M`$ with a field configuration $`\phi\in\mathcal F`$ and $`C(x)`$ with a functional constraint
``` math
C[\phi]\in \mathcal Y .
```
A hard constrained functional integral has the schematic form
``` math
Z=
\int_{\mathcal F}\mathcal D\phi\;
\delta(C[\phi])\,e^{iS[\phi]/\hbar}.
```

The finite-filter version is
``` math
Z_\varepsilon=
\int_{\mathcal F}\mathcal D\phi\;
\mathcal K_\varepsilon(C[\phi])\,e^{iS[\phi]/\hbar},
```
where
``` math
\mathcal K_\varepsilon(C)
=
\mathcal N_\varepsilon
\exp\!\left(-\frac{1}{2\varepsilon^2}\|C\|_{\mathcal Y}^{2}\right).
```

In Euclidean form:
``` math
Z_\varepsilon^E
=
\int_{\mathcal F}\mathcal D\phi\;
\exp\!\left(
-S_E[\phi]
-\frac{1}{2\varepsilon^2}\|C[\phi]\|_{\mathcal Y}^{2}
\right).
```

## Scope warning

In infinite dimensions, the symbols
``` math
\mathcal D\phi,\qquad \delta(C[\phi]),\qquad \det(DC\,DC^\ast)
```
are formal unless a regulator, Gaussian measure, lattice approximation, pAQFT construction, or other definition is supplied. The rigorous theorem of this paper is finite-dimensional. The functional-integral formulas are structural extensions of the same mechanism.

# Relation to Lagrange multipliers

A delta constraint may also be represented by a Fourier integral:
``` math
\delta(C)=\int \frac{d\lambda}{2\pi}\,e^{i\lambda C}.
```
For multiple constraints:
``` math
\delta^{(m)}(C)=\int \frac{d^m\lambda}{(2\pi)^m}\,e^{i\lambda\cdot C}.
```

This expresses hard constraint enforcement by an auxiliary multiplier field. The finite-filter version corresponds to adding a damping envelope in multiplier space:
``` math
k_\varepsilon(C)
=
\int \frac{d^m\lambda}{(2\pi)^m}
e^{i\lambda\cdot C}\,
e^{-\varepsilon^2|\lambda|^2/2}.
```

Thus finite admissibility width in constraint space is equivalent to suppressing arbitrarily large Lagrange-multiplier modes.

# Large-penalty localization

The same limit may be expressed dynamically as a large-penalty limit. In Euclidean signature, replace the constrained integral
``` math
\int \delta(C(x))\,e^{-S(x)}\,d\mu(x)
```
by
``` math
\int
\exp\!\left[-S(x)-\frac{|C(x)|^2}{2\varepsilon^2}\right]\,d\mu(x).
```
As $`\varepsilon\downarrow0`$, the penalty term suppresses all configurations outside an $`O(\varepsilon)`$-tube around the constraint surface $`C^{-1}(0)`$. In local coordinates $`(u,v)`$, where $`u=C(x)\in\mathbb R^m`$ and $`v`$ parametrizes the constraint surface, the integral has the schematic form
``` math
\int e^{-|u|^2/2\varepsilon^2}\,F(u,v)\,du\,dv .
```
After multiplication by the normalizing factor $`(2\pi\varepsilon^2)^{-m/2}`$, the Gaussian integral localizes to $`u=0`$, giving
``` math
\int_{C^{-1}(0)}
\frac{e^{-S(x)}}{J_C(x)}\,d\sigma(x),
```
with $`J_C=(\det DC\,DC^\ast)^{1/2}`$. Thus the finite admissibility filter is not merely a visual analogy for a delta; it has the same localizing asymptotics as the hard constrained measure.

In Lorentzian signature the corresponding statement is more delicate because the path integral is oscillatory. The penalty term may be introduced after Wick rotation, by $`i0`$-type damping, or inside a regulator-defined construction. The structural point remains the same: the hard functional delta is the zero-width limit of a filter that increasingly localizes histories near $`C=0`$.

# Admissible filters versus arbitrary penalties

A finite-width constraint filter changes the theory at finite $`\varepsilon`$. Therefore the replacement
``` math
\delta[C]\leadsto \mathcal K_\varepsilon[C]
```
is not automatically legitimate as physics. It is legitimate only if the filter is either:

1.  a regulator that is removed in the end;

2.  an effective model for finite experimental or coarse-graining resolution; or

3.  an admissibility kernel derived from the underlying MTT projection and closure-cost structure.

This distinction is important. A generic penalty may violate a symmetry, distort the measure, or select the wrong sector. In gauge theory, for example, finite gauge-tube filters must be compatible with the Faddeev–Popov/BV–BRST quotient structure if they are to define the same physical quotient in the sharp limit. In MTT terms, the filter must be an admissible projection weight, not an arbitrary smearing inserted by hand.

# Relation to gauge fixing

Gauge fixing is a special case of constraint filtering. A gauge condition
``` math
G[A]=0
```
inserts
``` math
\delta(G[A])
```
together with the Faddeev–Popov determinant.

The finite admissibility version is
``` math
\delta(G[A])
\quad\leadsto\quad
\mathcal K_\varepsilon(G[A])
=
\exp\!\left(-\frac{1}{2\varepsilon^2}\|G[A]\|^2\right).
```

This replaces a hard gauge slice by a finite gauge tube. The Faddeev–Popov determinant remains the Jacobian of projection from gauge-orbit coordinates to the chosen slice, while the filter width controls how sharply the representative section is enforced.

This paper therefore generalizes the gauge paper:
``` math
\text{gauge-fixing delta}
\subset
\text{path-integral constraint delta}
\subset
\text{finite admissibility filter limit}.
```

# MTT interpretation

In Modal Triplet Theory, admissible descriptions are not arbitrary configurations. They are configurations that survive projection, stabilization, and coherence constraints. Therefore a hard functional delta
``` math
\delta(C[\phi])
```
should not be treated as primitive. It is the zero-width limit of an admissibility filter:
``` math
\mathcal K_{\epsilon}[C[\phi]]
=
\exp\!\left(-\frac{1}{\epsilon^2}J_{\mathrm{adm}}[\phi]\right),
```
where $`J_{\mathrm{adm}}`$ measures the degree of constraint violation, closure strain, gauge-slice distance, or failure of coherent continuation.

The hard limit is
``` math
\delta(C[\phi])
=
\lim_{\epsilon\downarrow0}\mathcal K_\epsilon[C[\phi]]
```
in the same structural sense that finite-dimensional Gaussian filters converge to surface deltas.

## Triadic reading

The same delta may involve different MTT carrier roles.

<div class="center">

| Carrier role | Constraint-filter interpretation |
|:---|:---|
| Circle $`C`$ | exact bookkeeping closure, return consistency, conservation shells |
| Lens $`L`$ | representative selection inside redundancy classes, gauge slices |
| Nil $`N`$ | survivor-basin thresholds, admissibility boundaries, collapse-like selection |

</div>

A path-integral delta functional is therefore not a single primitive object in MTT. It is a downstream singular notation for whichever admissibility condition is being enforced.

# Soft constraints versus hard constraints

The finite filter
``` math
\exp(-\|C\|^2/2\varepsilon^2)
```
does not merely approximate a mathematical delta. For finite $`\varepsilon`$, it defines a different effective theory: one in which constraint violation is penalized rather than forbidden.

This distinction matters.

<div class="center">

| Regime | Mathematical form | MTT reading |
|:---|:---|:---|
| Hard constraint | $`\delta(C)`$ | zero-width admissibility limit |
| Soft constraint | $`e^{-\|C\|^2/2\varepsilon^2}`$ | finite admissibility tolerance |
| Penalty action | $`S+\|C\|^2/2\varepsilon^2`$ | closure-cost deformation |
| Unconstrained | no filter | no enforced admissibility shell |

</div>

The hard limit may be useful and often correct. But MTT treats it as a limit, not as the primitive description.

# Diagnostics and finite-width effects

Replacing $`\delta[C]`$ by $`\mathcal K_\varepsilon[C]`$ suggests concrete finite-width diagnostics:

1.  constraint surfaces become finite admissibility tubes;

2.  gauge slices become finite gauge tubes;

3.  hard classical shells become soft shells;

4.  path histories with small closure violation contribute with controlled suppression;

5.  infinitely sharp Lagrange-multiplier modes are damped;

6.  exact constraint enforcement is recovered only as $`\varepsilon\downarrow0`$.

The physical relevance of these corrections depends on the sector. In ordinary effective field theory they may be only regulator artifacts. In MTT they may encode finite coherence capacity.

# Scope of proof

<div class="center">

| Statement | Status |
|:---|:---|
| Gaussian filters on regular finite-dimensional constraint surfaces converge to surface deltas | proved |
| General approximate-identity filters give the same surface delta | proved by same coarea argument |
| Large-penalty filters localize to the constraint surface in the sharp limit | proved locally by the same coarea/Gaussian argument |
| Functional delta filters behave analogously in path integrals | formal, regulator-dependent |
| Gauge-fixing deltas are a special case of constraint filtering | structural and standard |
| Finite penalties preserve physics only when regulator-removable or admissibility-derived | caveat, not automatic |
| MTT admissibility costs generate all physical constraint filters | interpretive target, not proved here |

</div>

# Conclusion

Path-integral delta functionals are usually written as hard constraints:
``` math
\delta[C[\phi]].
```
This paper shows that, at the rigorous finite-dimensional level, such deltas arise as zero-width limits of finite constraint filters. The same pattern extends formally to functional integrals, where a hard delta can be replaced by a finite admissibility weight
``` math
\exp[-\|C[\phi]\|^2/2\varepsilon^2].
```

The MTT reading is direct:
``` math
\boxed{
\delta[C]=\text{singular shadow of finite admissibility filtering}.
}
```
This unifies classical constraint shells, gauge-fixing deltas, soft penalty actions, and path-integral restrictions under one projection-first interpretation.
