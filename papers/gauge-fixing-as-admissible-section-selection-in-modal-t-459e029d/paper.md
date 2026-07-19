---
abstract: |
  Gauge theory contains an explicit version of the projection architecture developed in Modal Triplet Theory (MTT). The full field space $`\mathcal A`$ contains redundant representatives related by a gauge group $`\mathcal G`$, while the physical configuration space is the quotient $`\mathcal A/\mathcal G`$. A gauge condition $`G[A]=0`$ is therefore not a physical law imposed on the quotient itself, but a local representative section of the quotient map. This paper develops the MTT interpretation of gauge fixing as admissible section selection. The gauge-fixing delta $`\delta(G[A])`$ is identified as the singular zero-width limit of a representative-selection kernel, the Faddeev–Popov determinant is the Jacobian of the projection from gauge-orbit coordinates to slice coordinates, ghost fields are quotient-measure bookkeeping variables, BRST cohomology is the algebraic implementation of admissible quotienting, and Gribov ambiguity is the failure of a global admissible section.

  The mathematical core is deliberately modest. We first prove a finite-dimensional slice formula showing that the Faddeev–Popov determinant is exactly the transverse projection Jacobian for a local quotient. We then state the corresponding regularized infinite-dimensional functional identity under the usual formal assumptions of gauge-fixed path integration. Finally, we reinterpret these standard structures through the MTT triad: lens structure carries gauge redundancy, nil structure appears in sharp representative selection, and circle structure carries return/conservation bookkeeping. The result is a worked sequel to the delta-projection paper: gauge fixing becomes the cleanest example of a Dirac delta functioning as the singular shadow of admissible projection.
author:
- Peter Nero
current_version: unversioned
date: April 2026
generated_from_main_tex_sha256: b0f05a0f5c023e0c7b332b337a39615a8e1220d78faa36bff956b5d6c9d283ca
paper_id: gauge-fixing-as-admissible-section-selection-in-modal-t-459e029d
release_state: not_matched_to_zenodo
title: |
  **Gauge Fixing as Admissible Section Selection in Modal Triplet Theory**  
  Faddeev–Popov Determinants, Ghosts, BRST, and Gribov Ambiguity as Projection Geometry
---

*Part VI of VI in the Fixed Points series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

# Purpose and claim discipline

The previous paper in this sequence argued that Dirac delta functions should be read, in MTT-compatible effective descriptions, as singular shadows of finite admissible projection kernels. The present paper applies that principle to the most transparent standard case: gauge fixing.

The guiding slogan is:
``` math
\boxed{\text{Gauge is uncollapsed projection; gauge fixing is collapsed representative selection.}}
```

More explicitly, gauge freedom records that the map from a richer description to a physical quotient is many-to-one. Gauge fixing chooses a representative section. The Faddeev–Popov determinant corrects the measure induced by that choice. The gauge-fixing delta is the zero-width limit of a finite representative-selection kernel.

## What is proved

This paper proves a finite-dimensional local slice formula. In a finite-dimensional free gauge action with a transverse gauge condition, the Faddeev–Popov determinant is exactly the Jacobian by which orbit coordinates project onto the gauge-fixing condition. This is a rigorous local theorem.

## What is not proved

This paper does not provide a new rigorous construction of nonperturbative Yang–Mills theory. It does not solve the Gribov problem. It does not replace the BV–BRST formalism. It does not claim that every gauge theory has a global smooth gauge section. In fact, one of the central claims is that global section failure is structurally expected.

The infinite-dimensional functional-integral statements are used in the standard physicists’ sense: as formal identities that become rigorous only after choosing a regulator, a measure construction, and a renormalization scheme. The finite-dimensional theorem is the analytic anchor; the functional gauge-theory interpretation is the physical extension.

<div class="center">

</div>

# Projection structure of gauge theory

Let $`\mathcal A`$ be a field configuration space and let $`\mathcal G`$ be a gauge group acting on it:
``` math
\mathcal A\times\mathcal G\to\mathcal A,\qquad (A,g)\mapsto A^g.
```
The physical configuration associated with $`A`$ is not $`A`$ itself but its orbit:
``` math
[A]=\{A^g:g\in\mathcal G\}.
```
The physical configuration space is the quotient
``` math
\mathcal M:=\mathcal A/\mathcal G.
```
Thus there is a quotient projection
``` math
\pi:\mathcal A\to\mathcal M,\qquad A\mapsto [A].
```

<div class="definition">

**Definition 1** (Gauge orbit). The gauge orbit through $`A\in\mathcal A`$ is
``` math
\mathcal O_A:=\pi^{-1}([A])=\{A^g:g\in\mathcal G\}.
```

</div>

<div class="definition">

**Definition 2** (Local gauge section). A local gauge section over $`U\subset\mathcal M`$ is a map
``` math
s:U\to\mathcal A
```
such that
``` math
\pi\circ s=\mathrm{id}_U.
```
Equivalently, $`s`$ chooses one representative $`A=s([A])`$ from each orbit in $`U`$.

</div>

<div class="remark">

*Remark 3* (MTT reading). The quotient projection $`\pi:\mathcal A\to\mathcal A/\mathcal G`$ is a lens-type projection. Its fibers are equivalence classes of redundant representatives. Gauge freedom is not additional physical content; it is the visible non-injectivity of the representation map.

</div>

The central structural point is:
``` math
\boxed{\text{Gauge freedom}=\text{visible persistence of projection non-injectivity}.}
```

# Gauge conditions as local sections

A gauge condition is a functional
``` math
G:\mathcal A\to V
```
into some vector space $`V`$, with the intended gauge slice
``` math
\Sigma_G:=\{A\in\mathcal A:G[A]=0\}.
```

If $`\Sigma_G`$ intersects each nearby gauge orbit exactly once and transversely, then it defines a local section of the quotient map.

<div class="definition">

**Definition 4** (Admissible local gauge condition). A gauge condition $`G[A]=0`$ is locally admissible at $`A`$ if:

1.  the orbit through $`A`$ intersects $`\Sigma_G`$;

2.  the intersection is locally unique;

3.  the intersection is transverse, i.e. the linearized map from infinitesimal gauge directions to $`V`$ is invertible.

</div>

The linearized gauge variation is
``` math
\delta_\epsilon A := R_A\epsilon,
```
where $`R_A:\mathfrak g\to T_A\mathcal A`$ is the infinitesimal gauge-action map. The gauge-fixing operator is
``` math
M_G(A):=D_A G\circ R_A:\mathfrak g\to V.
```
The transverse condition is:
``` math
\det M_G(A)\ne0.
```

<div class="remark">

*Remark 5*. In ordinary gauge theory $`M_G(A)`$ is the Faddeev–Popov operator. For example, in Yang–Mills theory with Lorenz gauge $`G[A]=\partial^\mu A_\mu`$, the infinitesimal variation gives an operator of the schematic form
``` math
M_G(A)=\partial^\mu D_\mu[A].
```

</div>

# Finite-dimensional slice theorem

We now state the rigorous finite-dimensional model behind the Faddeev–Popov identity.

<div class="assumption">

**Assumption 6** (Finite-dimensional local quotient model). Let $`X`$ be a smooth oriented $`n`$-dimensional manifold, and let a $`k`$-dimensional Lie group $`G`$ act freely and properly on $`X`$. Let $`G_0:X\to\mathbb R^k`$ be a smooth gauge condition. Fix $`x_0\in X`$ such that:

1.  $`G_0(x_0)=0`$;

2.  the differential $`D_{x_0}G_0`$ restricted to the tangent space of the orbit $`T_{x_0}\mathcal O_{x_0}`$ is an isomorphism onto $`\mathbb R^k`$.

</div>

Let $`R_{x_0}:\mathfrak g\to T_{x_0}X`$ be the infinitesimal action map. Define
``` math
M_{G_0}(x_0):=D_{x_0}G_0\circ R_{x_0}:\mathfrak g\to\mathbb R^k.
```

<div class="theorem">

**Theorem 7** (Local slice and projection Jacobian). *Under the finite-dimensional local quotient assumptions, there is a neighborhood $`U`$ of $`x_0`$ such that $`G_0^{-1}(0)\cap U`$ is a local slice through the $`G`$-orbits. Moreover, in local coordinates $`(u,\alpha)`$, where $`u`$ parameterizes the slice and $`\alpha\in\mathfrak g`$ parameterizes the orbit, the volume form factorizes as
``` math
d\mathrm{vol}_X = J(u,\alpha)\,du\,d\alpha,
```
and the distributional identity
``` math
1
=
\left|\det M_{G_0}(x)\right|
\int_{\mathfrak g} d\alpha\,\delta(G_0(x^\alpha))
```
holds locally, up to the conventional normalization of Haar measure.*

</div>

<div class="proof">

*Proof.* By the transversality assumption, $`D_{x_0}G_0`$ restricted to the orbit tangent space is an isomorphism. The implicit function theorem implies that $`G_0^{-1}(0)`$ is a codimension-$`k`$ submanifold through $`x_0`$, transverse to the orbit. Since the action is free and proper, the orbit map is locally an embedding, and the map
``` math
(u,\alpha)\mapsto u^\alpha
```
from slice coordinates and group coordinates is a local diffeomorphism onto a neighborhood of $`x_0`$.

For fixed $`u`$, define
``` math
F_u(\alpha):=G_0(u^\alpha).
```
At the selected representative $`\alpha=0`$, the derivative is
``` math
D_\alpha F_u(0)=D_uG_0\circ R_u=M_{G_0}(u).
```
By invertibility, the ordinary multidimensional delta-change-of-variables formula gives
``` math
\delta(F_u(\alpha))
=
\frac{\delta(\alpha)}{|\det M_{G_0}(u)|}
```
locally. Therefore
``` math
\int d\alpha\,\delta(G_0(u^\alpha))
=
\frac{1}{|\det M_{G_0}(u)|}.
```
Multiplying by $`|\det M_{G_0}(u)|`$ gives the stated identity. Extending from $`u`$ to $`x`$ in the local neighborhood gives the same expression for $`x`$ near the slice. ◻

</div>

<div class="corollary">

**Corollary 8** (Faddeev–Popov determinant as projection Jacobian). *In a local gauge slice, the Faddeev–Popov determinant is the Jacobian measuring how gauge-orbit coordinates project onto the gauge-fixing condition:
``` math
\Delta_{\mathrm{FP}}(x)=|\det(DG_0\circ R_x)|.
```*

</div>

<div class="remark">

*Remark 9* (MTT interpretation). The determinant is not mysterious. It is the measure cost of reducing a redundant fiber to a chosen local representative. In MTT language, it is the Jacobian of lens-quotient projection.

</div>

# Soft representative selection

The delta function in the Faddeev–Popov identity imposes a perfectly sharp gauge slice:
``` math
\delta(G[A]).
```
The delta-projection principle replaces such a sharp condition with a finite admissibility kernel. For a scale $`\epsilon>0`$, define
``` math
\mathcal K_\epsilon(G[A])
:=
(2\pi\epsilon^2)^{-k/2}
\exp\left(-\frac{\|G[A]\|^2}{2\epsilon^2}\right)
```
in finite dimension, or the corresponding Gaussian functional weight in field theory.

Then
``` math
\mathcal K_\epsilon(G[A])\to \delta(G[A])
```
distributionally as $`\epsilon\downarrow0`$.

<div class="definition">

**Definition 10** (Gauge tube). For $`\epsilon>0`$, the $`\epsilon`$-gauge tube around the slice $`G[A]=0`$ is the finite-width representative-selection region weighted by $`\mathcal K_\epsilon(G[A])`$.

</div>

<div class="proposition">

**Proposition 11** (Soft slice identity). *In the finite-dimensional local quotient model,
``` math
\Delta_{\mathrm{FP}}(x)\int d\alpha\,\mathcal K_\epsilon(G(x^\alpha))
\to 1
```
as $`\epsilon\downarrow0`$, locally near a transverse slice.*

</div>

<div class="proof">

*Proof.* This follows directly from the distributional convergence $`\mathcal K_\epsilon\to\delta`$ and the local slice theorem. ◻

</div>

<div class="remark">

*Remark 12* (MTT reading). A hard gauge slice is an idealized zero-width representative choice. A finite gauge tube is the MTT-native version: representative selection with finite admissibility width.

</div>

# Functional Faddeev–Popov identity

In field theory one writes the formal identity
``` math
1=\Delta_{\mathrm{FP}}[A]\int\mathcal D\alpha\,\delta(G[A^\alpha]),
```
where
``` math
\Delta_{\mathrm{FP}}[A]=\det\left(\frac{\delta G[A^\alpha]}{\delta\alpha}\right)_{\alpha=0}.
```

In infinite dimension this determinant is formal until a regulator, boundary condition, and renormalization prescription are specified. In what follows it is used in the standard perturbative sense. The rigorous content imported from the previous section is the finite-dimensional local slice formula; the field-theoretic expression is its regulated formal analogue.

Gauge-fixed path integration then takes the form
``` math
Z
=
\int \mathcal DA\,\Delta_{\mathrm{FP}}[A]\,\delta(G[A])\,e^{iS[A]/\hbar}.
```

The MTT-consistent soft form is
``` math
Z_{\mathrm{adm},\epsilon}
=
\int \mathcal DA\,\Delta_{\mathrm{FP}}[A]\,
\mathcal K_\epsilon(G[A])\,
e^{iS[A]/\hbar}.
```

For a quadratic Gaussian gauge-tube kernel,
``` math
\mathcal K_\epsilon(G[A])
=
\exp\left(-\frac{1}{2\epsilon^2}\|G[A]\|^2\right),
```
the familiar covariant gauge-fixing term appears as the finite-width representative-selection penalty.

<div class="remark">

*Remark 13*. This is not a new gauge theory. It is a reinterpretation of the standard gauge-fixing term: the gauge parameter controls the width of the representative-selection tube. The exact delta gauge is recovered as the singular zero-width limit.

</div>

# Worked examples: Abelian and non-Abelian Lorenz gauge

The abstract projection-Jacobian statement becomes especially transparent in the standard Lorenz gauge.

## Abelian $`U(1)`$

Let $`A_\mu`$ be an Abelian gauge potential and let
``` math
A_\mu^\alpha=A_\mu+\partial_\mu\alpha .
```
Choose the Lorenz gauge condition
``` math
G[A]=\partial^\mu A_\mu .
```
Then
``` math
G[A^\alpha]
=
\partial^\mu A_\mu+\Box\alpha .
```
Therefore the Faddeev–Popov operator is
``` math
M_G=\Box .
```
Hence
``` math
\Delta_{\mathrm{FP}}[A]=\det \Box ,
```
which is independent of $`A`$. In the Abelian case the ghost determinant is therefore field-independent and decouples from the interacting dynamics.

<div class="remark">

*Remark 14* (MTT reading). For $`U(1)`$, the local projection Jacobian is constant along the physical field directions. The quotient still exists, and the gauge-fixing delta still selects a representative slice, but the measure cost does not introduce interacting quotient-bookkeeping fields.

</div>

The soft MTT gauge tube gives the familiar covariant gauge penalty
``` math
\exp\left[-\frac{1}{2\epsilon^2}\int(\partial^\mu A_\mu)^2\right],
```
in Euclidean signature, or the corresponding phase-weighted term in Lorentzian signature. Thus the usual gauge parameter can be read as controlling the width of admissible representative selection around the Lorenz slice.

## Non-Abelian Yang–Mills

For a non-Abelian gauge field $`A_\mu=A_\mu^aT_a`$, the infinitesimal gauge variation is
``` math
\delta_\alpha A_\mu = D_\mu[A]\alpha ,
```
where
``` math
D_\mu[A]\alpha=\partial_\mu\alpha+[A_\mu,\alpha].
```
With the same Lorenz gauge condition,
``` math
G[A]=\partial^\mu A_\mu,
```
one obtains
``` math
G[A^\alpha]=G[A]+\partial^\mu D_\mu[A]\alpha+O(\alpha^2).
```
Therefore
``` math
M_G[A]=\partial^\mu D_\mu[A].
```
The Faddeev–Popov determinant is now
``` math
\Delta_{\mathrm{FP}}[A]=\det(\partial^\mu D_\mu[A]),
```
which depends on the gauge field. Consequently the ghost representation produces interacting ghost terms.

<div class="remark">

*Remark 15* (Why ghosts interact). Ghosts interact in the non-Abelian case because the projection Jacobian depends on the point of the gauge orbit. Equivalently, the redundancy fiber is curved or twisted relative to the chosen representative slice. Ghost interactions therefore encode the field-dependent geometry of quotienting, not additional physical matter.

</div>

<div class="center">

| Case | Faddeev–Popov operator | Interpretation |
|:---|:---|:---|
| Abelian $`U(1)`$ | $`\Box`$ | constant projection Jacobian; ghosts decouple |
| Non-Abelian Yang–Mills | $`\partial^\mu D_\mu[A]`$ | field-dependent projection Jacobian; ghosts interact |

</div>

# Ghosts as quotient bookkeeping

For non-Abelian gauge theory the Faddeev–Popov determinant is field-dependent. One introduces anticommuting ghost fields $`c,\bar c`$ to represent it:
``` math
\Delta_{\mathrm{FP}}[A]
=
\int \mathcal D\bar c\,\mathcal Dc\,
\exp\left(iS_{\mathrm{ghost}}[\bar c,c,A]\right).
```

In the present interpretation:
``` math
\boxed{\text{ghost fields are local bookkeeping variables for the quotient-measure Jacobian.}}
```

They are not physical excitations in the same sense as gauge-invariant particles. They encode how the redundant lens directions distort the measure after representative selection.

<div class="proposition">

**Proposition 16** (Ghosts encode the determinant). *Formally, for a linearized Faddeev–Popov operator $`M_G[A]`$,
``` math
\det M_G[A]
=
\int \mathcal D\bar c\,\mathcal Dc\,
\exp\left(-\int \bar c\,M_G[A]\,c\right)
```
in Euclidean signature, up to normalization.*

</div>

<div class="remark">

*Remark 17*. The sign and factor of $`i`$ depend on signature and convention. The structural point is invariant: ghost integration represents the determinant induced by quotienting the gauge orbit.

</div>

# BRST as algebraic admissible quotienting

BRST symmetry packages gauge redundancy, gauge fixing, and ghosts into a cohomological structure. The BRST operator $`Q_{\mathrm{BRST}}`$ satisfies
``` math
Q_{\mathrm{BRST}}^2=0.
```
Physical states are represented by cohomology:
``` math
\mathcal H_{\mathrm{phys}}
=
\ker Q_{\mathrm{BRST}}/\operatorname{im}Q_{\mathrm{BRST}}.
```

In MTT language:
``` math
\boxed{
\text{physical states}=
\text{admissible quotient classes modulo null redundancy}.
}
```

Exact BRST states are invisible redundancy; closed BRST states are compatible with the quotient constraint.

<div class="remark">

*Remark 18* (Nilpotency and projection). The nilpotency $`Q_{\mathrm{BRST}}^2=0`$ says that gauge redundancy has already been identified as a null direction of physical distinction. Acting twice remains within redundancy. This is the algebraic counterpart of a projection quotient.

</div>

# Gribov ambiguity as global section failure

The local slice theorem does not imply global gauge fixing. A gauge condition may intersect a single orbit more than once:
``` math
A_1,A_2\in\Sigma_G,\qquad A_2=A_1^g,\qquad A_1\ne A_2.
```
These are Gribov copies.

In the present language:
``` math
\boxed{
\text{Gribov ambiguity}=
\text{failure of a global admissible representative section}.
}
```

This is not an accidental technical nuisance. It is a structural warning: the quotient projection may have nontrivial global topology, and no single downstream chart can cover it without ambiguity.

<div class="remark">

*Remark 19* (MTT alignment). MTT expects reduced descriptions to be local encoding regimes with controlled overlap, not global primitive ontologies. The Gribov problem is therefore a standard gauge-theoretic example of a general MTT principle: representative choice can be locally admissible while globally obstructed.

</div>

# Triadic placement

The MTT proto-spinorial carrier is written schematically as
``` math
\Xi=(\Psi,C,L,N),
```
where $`C`$ carries return/bookkeeping, $`L`$ carries lens redundancy transport, and $`N`$ carries nil termination or survivor selection.

Gauge theory maps naturally into this structure:

<div class="center">

| Gauge-theory object | MTT role | Interpretation |
|:---|:---|:---|
| Gauge orbit | $`L`$ | lens redundancy fiber |
| Gauge fixing | $`L`$-selection interface | representative selection |
| $`\delta(G[A])`$ | selection idealization | sharp slice selection |
| Faddeev–Popov determinant | lens Jacobian | quotient-measure cost |
| Ghosts | lens bookkeeping | determinant variables |
| BRST cohomology | quotient algebra | admissible physical classes |
| Gribov copies | section obstruction | local charts only |
| Ward identities | $`C/L`$ bookkeeping | return/consistency constraints |

</div>

The key point is that gauge freedom is primarily lens structure, while gauge fixing introduces a representative-selection operation with the same formal profile as nil-sector selection. The delta function appears at precisely this interface:
``` math
\boxed{
\text{gauge delta}=\text{singular representative-selection kernel on a lens quotient}.
}
```

# Diagnostic consequences

The present paper gives a practical diagnostic:

1.  Find the gauge redundancy.

2.  Identify the quotient projection.

3.  Identify the local gauge section.

4.  Compute the projection Jacobian.

5.  Replace sharp $`\delta(G[A])`$ by a finite admissibility kernel if one wants the MTT-native description.

6.  Check whether the local section extends globally; if not, Gribov-type obstruction is expected.

This suggests several later developments:

1.  soft gauge fixing as finite admissible section selection;

2.  BRST/BV as the algebra of admissible quotienting;

3.  Gribov regions as admissible chart domains;

4.  gauge-parameter dependence as tube-width dependence;

5.  anomalies as failures of quotient-measure consistency.

# Conclusion

Gauge theory provides the cleanest standard example of the delta-projection principle. The full field space contains redundant representatives; the physical space is a quotient; gauge freedom is uncollapsed projection non-injectivity; gauge fixing chooses a local representative; the gauge-fixing delta is the singular zero-width selection kernel; the Faddeev–Popov determinant is the projection Jacobian; ghosts are quotient-measure bookkeeping variables; BRST cohomology implements admissible quotienting algebraically; and Gribov ambiguity marks the failure of global section choice.

Thus the central conclusion is:
``` math
\boxed{
\begin{minipage}{0.86\textwidth}
\centering
Gauge fixing is admissible section selection, and Faddeev--Popov is its projection Jacobian.
\end{minipage}
}
```

This result strengthens the broader MTT research program. It shows that the delta-projection idea is not merely a metaphor about point sources. It is already present in one of the most mature parts of modern field theory: the mathematics of gauge redundancy and its quotient.
