---
abstract: |
  This paper asks what Modal Triplet Theory (MTT) presently establishes about Kaluza–Klein reduction. A Kaluza–Klein construction begins with a supplied higher-dimensional geometry, action, field content, operator domains, mode normalizations, and reduction ansatz. Compactness then gives discrete internal spectra, but it does not select the internal manifold, its scale, the higher-dimensional action, or a nonlinearly consistent truncation. We package the required inputs as a typed Kaluza–Klein record and define a partial map from an upper MTT state to that record. The main realization theorem is conditional: if one selected MTT state emits every row of the record, the lower consistency and error conditions hold, and MTT evaluation factors through the standard reduction, then MTT realizes that reduced sector at the declared cutoff and order. For a fixed compact fiber we derive the usual tower masses from the eigenvalues of the appropriate internal Laplace-, Dirac-, or Lichnerowicz-type operator. We also distinguish an exact consistent truncation from a spectral projection and give a Lyapunov–Schmidt residual certificate for controlled approximate reduction. The canonical MTT specialization is a ten-dimensional bundle over a four-dimensional Lorentzian base with compact six-dimensional Riemannian fiber. Its constant-time $`9\to3`$ description is the spatial slice of the same $`10\to4`$ fibration, not an independent derivation. The local $`1+3\times3=4+6`$ component identity and the selected finite shared-line carrier motivate this geometry, but they do not yet construct the physical six-manifold or preserve its connection and Hessian. Consequently the paper establishes a reusable and testable reduction contract, not a first-principles selection of extra dimensions, Kaluza–Klein radii, gauge groups, particle masses, or Standard Model parameters.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 3b67d245f3bddee30ff8177512dc63b40d2c299d600c775de08071d361ea6b87
paper_id: modal-triplet-theory-from-mtt-to-kaluza-klein-theory
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and Kaluza–Klein Reduction:
  A Conditional $`4+6`$ Spectral and Truncation Contract
zenodo_doi: 10.5281/zenodo.21708733
zenodo_record_id: 21708733
zenodo_url: "https://zenodo.org/records/21708733"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1 and its claims that MTT had already selected the Kaluza–Klein internal space, radius, zero-mode spectrum, gauge couplings, family number, and a finite fixed-point system equivalent to the full higher-dimensional field equations.

The former paper combined valid Kaluza–Klein formulas with unproved MTT source claims. It treated a finite left-invariant ansatz as automatically complete for a nonlinear PDE, used cohomological completeness as if it were solution-space completeness, and inferred controlled truncation from a gap ratio without bounding the omitted equations. It also described the constant-time $`9\to3`$ slice as an independently proved compactification equivalence and imported obsolete Iwasawa and Lens–Nil selection claims.

This revision defines the full lower record, separates kinematic mode expansion from dynamical truncation, proves a conditional MTT realization theorem, and gives an explicit omitted-mode residual certificate. It uses the canonical $`4+6`$ geometry and states precisely what the $`1+3\times3=4+6`$ identity does and does not imply. Standard Kaluza–Klein formulas retain their literature ownership.

Compact internal operators still organize four-dimensional towers; internal isometries can supply gauge fields; normalized overlap integrals determine effective couplings; and finite invariant ansatzes can exactly encode the equations restricted to those ansatzes. These are valuable lower-level tools once their inputs and domains are supplied.

The current MTT research ledger leaves the continuum geometry-to-operator naturality problem open. Its exit requires a same-source commuting map from the world-in-world/strain carrier to the physical $`q=79`$ vertical Hermitian–Yang–Mills complex that preserves the connection, covariant derivatives, and Hessian. Without that map, the finite carrier does not select the physical Kaluza–Klein fiber or its operators.

</div>

# The corrected question

Kaluza–Klein theory is a method of reduction. One starts with a field theory on a space of dimension $`D=4+d`$, resolves its fields into internal modes, and asks which lower-dimensional fields and interactions survive at the scale of interest. Kaluza’s five-dimensional metric ansatz and Klein’s compact circle gave the original example; modern supergravity and string compactifications use the same architecture with richer fields and internal geometries .

There are two logically different questions:

1.  *Reduction question.* Given the higher-dimensional theory and compactification data, what lower-dimensional theory follows?

2.  *Source question.* Why are that theory, internal geometry, radius, bundle, vacuum, and truncation selected?

Kaluza–Klein analysis answers the first question. It does not by itself answer the second. The corrected MTT question is therefore:

> Does one selected upper MTT state emit a complete higher-dimensional record, and does MTT evaluation factor through a mathematically controlled Kaluza–Klein reduction of that same record?

This formulation makes the burden of proof visible. A metric with six unlabelled internal coordinates is not yet a compactification. Nor is an orthogonal projector a consistent low-energy theory. The action, gauge identifications, operator domains, mode normalization, nonlinear ansatz, source terms, and approximation error all matter.

## Result and non-result

The positive result of this paper is a conditional realization contract. It states exactly what MTT must provide and what follows once it does. The spectral and truncation statements below are ordinary mathematical consequences of a fixed lower record. They are included because they expose the interface that an MTT source theorem must satisfy.

The paper does not prove that MTT already selects a unique compact six-manifold, radius, higher-dimensional action, gauge group, chiral spectrum, or observed mass. In particular, a dimension count is not a geometric construction, and agreement with a profile used to choose a branch is not a held-out prediction.

# The lower Kaluza–Klein object

## Geometry

Let $`M_4`$ be a time-oriented Lorentzian four-manifold and let
``` math
\pi:Y_D\longrightarrow M_4,\qquad D=4+d,
```
be a smooth fiber bundle with compact $`d`$-dimensional fibers $`X_x=\pi^{-1}(x)`$. A horizontal distribution $`\mathcal H\subset TY_D`$ gives
``` math
TY_D=\mathcal H\oplus\mathcal V,\qquad \mathcal V=\operatorname{Ker}\mathrm d\pi .
```
The higher-dimensional metric is Lorentzian on the horizontal directions and Riemannian on the vertical directions. In a local trivialization it may be written schematically as
``` math
\begin{equation}
\label{eq:kkmetric}
\mathrm ds_D^2
 =g_{\mu\nu}(x)\,\mathrm dx^\mu\mathrm dx^\nu
 +h_{mn}(x,y)
   \bigl(\mathrm dy^m+\mathcal A^m{}_\mu(x,y)\mathrm dx^\mu\bigr)
   \bigl(\mathrm dy^n+\mathcal A^n{}_\nu(x,y)\mathrm dx^\nu\bigr).
\end{equation}
```
Equation <a href="#eq:kkmetric" data-reference-type="eqref" data-reference="eq:kkmetric">[eq:kkmetric]</a> is a local decomposition of supplied metric data. It neither proves that $`Y_D`$ exists globally nor selects $`(X,h,\mathcal H)`$.

Warping, boundaries, orbifold strata, monodromy, and varying fibers require additional data. To keep the spectral theorems transparent, the principal calculation below uses a closed compact fiber and a product or adiabatically controlled background. More general cases require the corresponding family, boundary, or singular elliptic theory.

## Fields, action, and operators

A reduction must specify the higher-dimensional fields and the action from which their equations follow. We denote by $`\mathcal F_D`$ the collection of metrics, connections, spinors, differential forms, scalars, source data, and any gauge-fixing or constraint variables. Let
``` math
S_D:\mathcal D(S_D)\subset\mathcal F_D\longrightarrow\mathbb R
```
be the action at a declared derivative and quantum order, with equations $`\mathcal E_D(\Phi)=0`$. Gauge transformations, diffeomorphisms, boundary conditions, and normalizations are part of the record rather than ellipsis.

Each field type has its own vertical operator. Scalar modes may be organized by a Laplace-type operator, spinors by a twisted Dirac operator, one-forms by a gauge-fixed Hodge operator, and metric fluctuations by a Lichnerowicz-type operator. Background flux, curvature, torsion, and potentials may add lower-order terms. A single formula $`-\Delta_XY_n=\lambda_nY_n`$ is therefore illustrative, not universal.

<div id="def:record" class="definition">

**Definition 1** (Complete Kaluza–Klein record). A *complete Kaluza–Klein record* at scope $`\sigma=(D,N,\ell,\partial,\mathrm{obs})`$ is
``` math
\mathcal K_\sigma=
\bigl(
Y_D,\pi,g_D,\mathcal H;\,
\mathcal F_D,S_D,\mathcal G_D;\,
\{L_\alpha,\mathcal D(L_\alpha)\}_\alpha;\,
\{u_{\alpha n}\};\,
P_N,\iota_N,\mathcal E_4;\,
\mathcal C_N,\mathcal N,\mathcal O
\bigr),
```
where:

1.  $`(Y_D,\pi,g_D,\mathcal H)`$ is the global geometric and connection data;

2.  $`(\mathcal F_D,S_D,\mathcal G_D)`$ gives fields, action, symmetries, constraints, sources, and boundary conditions;

3.  every $`L_\alpha`$ is the appropriate closed vertical operator with a specified domain, measure, adjoint convention, and normalization;

4.  $`\{u_{\alpha n}\}`$ is a complete normalized mode system whenever such a system is invoked;

5.  $`P_N`$ is the retained spectral or representation projector and $`\iota_N`$ is the full nonlinear uplift ansatz, not merely a linear inclusion;

6.  $`\mathcal E_4`$ is the claimed lower equation or action;

7.  $`\mathcal C_N`$ records exact consistency or an explicit residual and error certificate;

8.  $`\mathcal N`$ contains coupling, scale, frame, and measure normalizations; and

9.  $`\mathcal O`$ declares the observables and comparison map at which the reduction is asserted.

</div>

The record is deliberately longer than a metric ansatz. Most false compactification arguments omit precisely the rows that decide whether the calculation is physical: the nonlinear uplift, normalization, domain, and error rows.

# The MTT realization contract

Let $`\mathcal U_{\mathrm{MTT}}`$ be the domain of admissible upper MTT states. A candidate source map is a partial typed map
``` math
\mathcal R_{\mathrm{KK}}:
  \mathcal U_{\mathrm{MTT}}\dashrightarrow \mathfrak K_\sigma ,
```
where $`\mathfrak K_\sigma`$ is the class of records in Definition <a href="#def:record" data-reference-type="ref" data-reference="def:record">1</a>. The dashed arrow matters: not every abstract coherent state contains spacetime, action, or reduction data.

Let
``` math
\operatorname{Red}_{\mathrm{KK}}:\mathfrak K_\sigma
 \dashrightarrow \mathfrak L_\sigma
```
be the standard lower-dimensional reduction functional and let $`\operatorname{Ev}_{\mathrm{MTT}}`$ and $`\operatorname{Ev}_4`$ be the upper and lower observable evaluations on their declared common domain.

<div id="def:realization" class="definition">

**Definition 2** (Complete MTT–KK realization). A selected state $`u_\ast\in\mathcal U_{\mathrm{MTT}}`$ realizes a Kaluza–Klein sector at scope $`\sigma`$ when:

1.  $`\mathcal R_{\mathrm{KK}}(u_\ast)`$ is a complete record;

2.  every global, gauge, analytic, and source condition required by that record is satisfied;

3.  the truncation certificate $`\mathcal C_N`$ is exact or gives a stated error bound on the requested domain; and

4.  the observable diagram commutes,
    ``` math
    \begin{CD}
    u_\ast @>{\mathcal R_{\mathrm{KK}}}>>
           \mathcal K_\sigma @>{\operatorname{Red}_{\mathrm{KK}}}>>
           \mathfrak L_\sigma\\
    @V{\operatorname{Ev}_{\mathrm{MTT}}}VV
    && @VV{\operatorname{Ev}_4}V\\
    \mathcal O_\sigma @= \mathcal O_\sigma .
    \end{CD}
    ```

</div>

Equivalently, the commuting condition may be read algebraically as
``` math
\operatorname{Ev}_{\mathrm{MTT}}(u_\ast)
 =
 \operatorname{Ev}_4\!\left(
 \operatorname{Red}_{\mathrm{KK}}
 (\mathcal R_{\mathrm{KK}}(u_\ast))\right).
```

<div id="thm:conditional" class="theorem">

**Theorem 3** (Conditional MTT–Kaluza–Klein realization). *Suppose a selected MTT state $`u_\ast`$ satisfies Definition <a href="#def:realization" data-reference-type="ref" data-reference="def:realization">2</a>. Then MTT realizes the lower Kaluza–Klein sector
``` math
\operatorname{Red}_{\mathrm{KK}}
 \bigl(\mathcal R_{\mathrm{KK}}(u_\ast)\bigr)
```
at scope $`\sigma`$. If $`\mathcal C_N`$ is exact, the assertion is exact on the declared ansatz. If $`\mathcal C_N`$ supplies error $`\epsilon_N`$, every observable in $`\mathcal O_\sigma`$ is realized only to the propagated stated error.*

</div>

<div class="proof">

*Proof.* The source map supplies one lower record rather than a list of mutually unrelated compatible objects. The standard reduction functional is therefore defined on that record. The consistency certificate makes the reduction exact or controlled at the declared scope, while commutation of the evaluation diagram identifies the upper and lower observable values. No conclusion is asserted outside the domains, order, cutoff, sources, or observables recorded in $`\sigma`$. ◻

</div>

<div class="remark">

*Remark 4* (Why the theorem is substantive but conditional). The theorem is not the empty statement that equal models are equal. It fixes the exact source, covariance, normalization, truncation, and evaluation obligations whose omission previously allowed a representation to be remembered as a derivation. Its hypotheses are nevertheless not yet all discharged by current MTT geometry.

</div>

# Canonical $`4+6`$ geometry

## The physical specialization

The canonical physical specialization used in current MTT is
``` math
\pi:M_{10}\longrightarrow M_4,
  \qquad \dim M_4=4,\qquad \dim X_x=6,
```
with a globally hyperbolic Lorentzian base in the physical completion and compact Riemannian fibers. Positive elliptic modal operators act vertically. They organize internal states; they do not add causal time directions .

This $`4+6`$ architecture is a declared physical realization of the dimension-neutral MTT Hilbert-bundle formalism. It is not derived merely from the existence of three modal labels. If a selected physical six-manifold is eventually supplied, it must still come with the geometry, connections, action, operators, and reduction data in Definition <a href="#def:record" data-reference-type="ref" data-reference="def:record">1</a>.

## What the $`3\times3`$ field actually counts

Let $`TP`$ and $`TI`$ be oriented Euclidean rank-three bundles. A local world-in-world comparison field
``` math
Q_{\mathrm{WW}}\in\Gamma(\operatorname{Hom}(TP,TI))
```
has nine components after choosing frames. Around a nonsingular background, polar decomposition gives
``` math
\operatorname{Mat}(3,\mathbb R)
 =
 \mathfrak{so}(3)\oplus\operatorname{Sym}(3,\mathbb R),
 \qquad 9=3+6.
```
Relative to an orthonormal flag,
``` math
\operatorname{Sym}(3,\mathbb R)
 =
 \mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O,
 \qquad \dim(\mathbb RI_3,\mathcal D_0,\mathcal O)=(1,2,3).
```
Thus the component identity
``` math
1+3\times3=(1+3)+(1+2+3)=4+6=10
```
is exact once one ordering scalar is supplied. It is not manifold-dimension multiplication. Nor does it prove that the four components are a Lorentzian tangent space or that the six strain components globalize to the tangent bundle of a compact physical fiber.

The identity is useful because it presents a candidate local interface: orientation directions can be quotiented while the six strain directions carry the $`1+2+3`$ filtration. The missing theorem is global. It must intertwine bundles, connections, covariant derivatives, measures, and operators, not just match ranks.

## The constant-time $`9\to3`$ picture

Suppose the ten-dimensional fibration already has compatible splittings
``` math
M_{10}\simeq\mathbb R_t\times\Sigma_9,
 \qquad
 M_4\simeq\mathbb R_t\times M_3,
```
and $`\pi`$ preserves the time coordinate. Restriction to a time slice then gives
``` math
\pi_t:\Sigma_9\longrightarrow M_3
```
with the same six-dimensional fiber. Reattaching time recovers the original $`10\to4`$ fibration.

<div id="prop:slice" class="proposition">

**Proposition 5** (Spatial-slice identity). *Under the compatible product and time-preservation hypotheses above, the $`9\to3`$ spatial projection and the $`10\to4`$ fibration describe the same fiberwise geometric data after restriction and reattachment of the supplied time factor.*

</div>

<div class="proof">

*Proof.* The restriction of $`\pi`$ to $`\{t\}\times\Sigma_9`$ has base $`\{t\}\times M_3`$ and unchanged vertical bundle. Conversely, taking the product of $`\pi_t`$ with $`\operatorname{Id}_{\mathbb R_t}`$ reconstructs $`\pi`$. The claim is therefore an identity between two descriptions of one already supplied fibration. ◻

</div>

<div class="remark">

*Remark 6*. Proposition <a href="#prop:slice" data-reference-type="ref" data-reference="prop:slice">5</a> is not a derivation of time, three-space, or six compact directions. If the metric is not product-like, the fibration depends on time, or the horizontal distribution mixes causal and vertical directions, additional hypotheses replace this elementary identity.

</div>

## The shared circle

Current MTT finite geometry contains one universal flat cyclic line whose pullbacks agree across several selected finite carriers. This is stronger than noticing several isomorphic copies of $`U(1)`$: it identifies common connection and holonomy data at the proven finite level . It still does not make that line:

-
-
-
-

Any of those identifications requires a source-preserving geometric intertwiner with the relevant metric radius, spin structure, connection, and action. The corrected M-theory paper states the analogous circle boundary for eleven-dimensional reduction .

# Spectral origin of Kaluza–Klein masses

## A fixed compact fiber

Let $`X`$ be a closed compact Riemannian manifold and let $`E\to X`$ be a Hermitian vector bundle. A formally self-adjoint elliptic operator
``` math
L_X:\mathcal D(L_X)\subset L^2(X,E)\longrightarrow L^2(X,E)
```
with its self-adjoint realization has compact resolvent. Its spectrum is discrete with finite multiplicities and an orthonormal eigenbasis $`\{u_n\}`$ . The use of internal momentum and twists to generate lower-dimensional masses is standard Kaluza–Klein machinery .

Consider first a scalar on the unwarped product $`M_4\times X`$ with
``` math
S[\Phi]=-\frac12\int_{M_4\times X}
 \left(
 |\mathrm d_{M_4}\Phi|^2
 +\langle\Phi,L_X\Phi\rangle
 +m_D^2|\Phi|^2
 \right)\mathrm d\mathrm{vol}_{4}\mathrm d\mathrm{vol}_{X}.
```
For
``` math
L_Xu_n=\lambda_nu_n,\qquad
 \int_X\overline{u_m}u_n\,\mathrm d\mathrm{vol}_{X}=\delta_{mn},
\qquad
 \Phi(x,y)=\sum_n\phi_n(x)u_n(y),
```
orthogonality diagonalizes the quadratic action.

<div id="lem:masses" class="lemma">

**Lemma 7** (Fixed-background spectral mass dictionary). *Under the preceding hypotheses, the four-dimensional scalar modes have
``` math
m_n^2=m_D^2+\lambda_n.
```
If $`h=R^2h_0`$ and $`L_X=-\Delta_h`$, then
``` math
\lambda_n(h)=R^{-2}\widehat\lambda_n(h_0),
 \qquad
 m_n^2=m_D^2+\frac{\widehat\lambda_n}{R^2}.
```
The zero modes are $`\operatorname{Ker}L_X`$; a positive first omitted eigenvalue gives a quadratic spectral separation, not by itself a nonlinear truncation.*

</div>

<div class="proof">

*Proof.* Insert the normalized eigenmode expansion into the quadratic action. Self-adjointness and orthogonality remove cross terms, leaving one four-dimensional quadratic action for each $`n`$ with mass squared $`m_D^2+\lambda_n`$. The inverse-square scaling follows from the metric scaling of the scalar Laplacian. ◻

</div>

## Different fields use different operators

For a twisted spinor, the internal Dirac eigenvalue enters the four-dimensional mass matrix, with chirality and zero modes controlled by the spin or spin$`^{c}`$ bundle, twisting connection, and index. For differential forms, the relevant Hodge operator must be combined with gauge constraints and harmonic representatives. Metric fluctuations use a gauge-fixed Lichnerowicz-type operator and can mix with form and scalar fluctuations. Background curvature, torsion, flux, or bundle curvature changes the operator and may produce a matrix-valued eigenproblem.

It is therefore more accurate to write
``` math
M^2_{\alpha,mn}
  =
  M^2_{\alpha,\mathrm{bulk}}\delta_{mn}
  +
  \bigl\langle u_{\alpha m},
  L_{\alpha,X}u_{\alpha n}\bigr\rangle
```
after all constraints and normalizations are fixed. A numerical Kaluza–Klein mass is a conclusion only after $`L_{\alpha,X}`$, its domain, the scale, and the background are selected independently of the target mass.

## Uniform gaps are additional results

Every fixed closed compact elliptic problem has discrete spectrum. A uniform lower bound on the first positive eigenvalue across a varying family does not follow from compactness of each member. Collapse, degeneration, or an eigenvalue crossing zero can destroy such a bound. The corrected Calabi–Yau paper owns the corresponding fixed-background spectral admissibility statement and its uniformity warning . The present paper uses that result rather than duplicating it as an MTT theorem.

# Projection is not truncation

## The nonlinear consistency condition

Let $`P_N`$ project onto retained modes and let $`Q_N=\operatorname{Id}-P_N`$. Writing a field as $`P_N\Phi+Q_N\Phi`$ is a kinematic decomposition. Setting $`Q_N\Phi=0`$ is dynamically valid only if the omitted equations remain satisfied.

<div id="def:consistent" class="definition">

**Definition 8** (Exact consistent truncation). An uplift $`\iota_N:\mathcal F_4\to\mathcal F_D`$ is an exact consistent truncation when there is a lower equation $`\mathcal E_4`$ such that
``` math
\mathcal E_D(\iota_N\varphi)=0
 \quad\Longleftrightarrow\quad
 \mathcal E_4(\varphi)=0
```
on the declared domains. Equivalently, every lower solution uplifts to a higher-dimensional solution, and no omitted equation is sourced by the retained configuration.

</div>

Generic zero-mode truncations are not automatically consistent at nonlinear order. Products of retained harmonics can contain omitted harmonics. Special sphere, group-manifold, and supergravity ansatzes may nevertheless be consistent because symmetry and nonlinear field combinations enforce cancellations . The consistency belongs to the specific uplift ansatz, not to the word “compact.”

## A controlled residual certificate

When exact consistency fails, one can still justify an effective reduction by solving for the omitted modes and bounding their response. The following standard Lyapunov–Schmidt estimate makes the needed information explicit.

<div id="prop:residual" class="proposition">

**Proposition 9** (Omitted-mode correction bound). *Let $`\mathcal E_D:\mathcal X\to\mathcal Y`$ be $`C^1`$ between Banach spaces with compatible splittings $`P_N+Q_N=\operatorname{Id}`$. Fix a retained configuration $`u_0=\iota_N\varphi`$, set
``` math
r_N=Q_N\mathcal E_D(u_0),\qquad
 A_N=Q_ND\mathcal E_D(u_0)\big|_{Q_N\mathcal X},
```
and suppose $`A_N:Q_N\mathcal X\to Q_N\mathcal Y`$ is invertible with $`\|A_N^{-1}\|\le\gamma_N^{-1}`$. On the ball $`\|\eta\|\le\rho`$, suppose
``` math
\left\|
Q_N\!\left[
\mathcal E_D(u_0+\eta)-\mathcal E_D(u_0)-D\mathcal E_D(u_0)\eta
\right]
-
Q_N\!\left[
\mathcal E_D(u_0+\zeta)-\mathcal E_D(u_0)-D\mathcal E_D(u_0)\zeta
\right]
\right\|
\le L_\rho\|\eta-\zeta\|.
```
If
``` math
\frac{L_\rho}{\gamma_N}<1,
 \qquad
 \frac{\|r_N\|}{\gamma_N}
 \le
 \left(1-\frac{L_\rho}{\gamma_N}\right)\rho ,
```
then there is a unique $`\eta_\ast\in Q_N\mathcal X`$ in that ball such that
``` math
Q_N\mathcal E_D(u_0+\eta_\ast)=0,
\qquad
 \|\eta_\ast\|
 \le
 \frac{\|r_N\|}
      {\gamma_N-L_\rho}.
```*

</div>

<div class="proof">

*Proof.* Write the omitted equation as the fixed-point problem
``` math
\eta=
-A_N^{-1}r_N
-A_N^{-1}Q_N\!
\left[
\mathcal E_D(u_0+\eta)-\mathcal E_D(u_0)-D\mathcal E_D(u_0)\eta
\right].
```
The first inequality makes this map a contraction, and the second makes the closed radius-$`\rho`$ ball invariant. Banach’s fixed-point theorem gives existence and uniqueness. Taking norms in the fixed-point equation gives the stated bound. ◻

</div>

<div class="remark">

*Remark 10* (What a gap does). A spectral gap can help bound $`\|A_N^{-1}\|`$, but the other quantities do not disappear. One must still compute the omitted residual $`r_N`$, control the nonlinear Lipschitz constant $`L_\rho`$, and propagate the correction into the retained equation and requested observables. A dimensionless ratio of two named scales is not an error estimate unless these links are proved.

</div>

# Finite invariant ansatzes and the FCC

Version 1 introduced a fixed-point compactification condition (FCC): a finite algebraic system obtained by expanding a higher-dimensional background in a left-invariant basis. That construction has a correct but narrow scope.

Let $`\mathcal A_{\mathrm{inv}}=\{u(a):a\in\mathbb R^k\}`$ be a finite invariant ansatz. Suppose all derivatives, contractions, and nonlinear operations appearing in $`\mathcal E_D`$ send $`\mathcal A_{\mathrm{inv}}`$ into a finite residual space with linearly independent basis $`\{e_j\}_{j=1}^{m}`$. Then
``` math
\mathcal E_D(u(a))=\sum_{j=1}^{m}F_j(a)e_j.
```

<div id="prop:fcc" class="proposition">

**Proposition 11** (Exact scope of an invariant coefficient system). *Under the stated closure and linear-independence hypotheses,
``` math
\mathcal E_D(u(a))=0
 \quad\Longleftrightarrow\quad
 F_1(a)=\cdots=F_m(a)=0
```
for configurations $`u(a)`$ inside the chosen ansatz.*

</div>

<div class="proof">

*Proof.* The forward implication follows by taking coefficients. The converse follows because vanishing of every coefficient makes the residual zero in the finite residual space. ◻

</div>

Proposition <a href="#prop:fcc" data-reference-type="ref" data-reference="prop:fcc">11</a> does not say that every solution of the full PDE is left-invariant, that time-dependent perturbations remain in the ansatz, or that the ansatz gives a consistent truncation. Those are separate statements. Nomizu’s theorem computes de Rham cohomology from invariant forms on compact nilmanifolds ; it does not imply that all metrics, connections, nonlinear field configurations, or PDE solutions are invariant.

Nor does a finite algebraic system automatically select a unique vacuum. It may have no solutions, several isolated solutions, positive-dimensional branches, or singular components. An invertible Jacobian at one solution gives a locally unique branch under specified parameter variation; it does not select the integer data, fix an overall scale, or prove global uniqueness.

Accordingly, “FCC” can be retained as a useful name for the residual coefficient system of a declared invariant ansatz. It must not be described as equivalent to the unrestricted higher-dimensional theory without an independent completeness or consistent-truncation theorem.

# Four-dimensional quantities

## Planck normalization

For an unwarped product with fixed internal metric and Einstein–Hilbert term
``` math
S_D^{\mathrm{EH}}
 =
 \frac{1}{2\kappa_D^2}
 \int_{M_4\times X}\sqrt{-g_D}\,R_D,
```
integration over $`X`$ gives
``` math
\frac{1}{\kappa_4^2}
 =
 \frac{\operatorname{Vol}(X,h)}{\kappa_D^2}
```
before any further convention-dependent rescaling. Warping, a varying dilaton, or moduli replace the ordinary volume by a weighted integral and require an explicit Weyl transformation to four-dimensional Einstein frame. Thus the formula computes $`\kappa_4`$ from supplied $`(\kappa_D,h)`$; it does not select either input.

## Gauge fields and couplings

If $`K_a`$ are Killing vector fields of the internal metric, off-diagonal metric components along them can produce lower-dimensional vector fields. The Lie brackets
``` math
[K_a,K_b]=f_{ab}{}^{c}K_c
```
give the candidate gauge algebra. In a simple unwarped convention, the kinetic matrix contains the internal Gram integral
``` math
\mathcal G_{ab}
 \propto
 \frac{1}{\kappa_D^2}
 \int_X
 h(K_a,K_b)\,\mathrm d\mathrm{vol}_h .
```
The proportionality factor depends on the metric ansatz, generator normalization, radius factors, and Weyl frame. Higher-dimensional gauge connections provide additional gauge sectors by a different mechanism.

An internal isometry therefore makes a gauge interpretation possible, but it does not select the observed gauge group or its normalized couplings. Moreover, retaining all isometry vectors need not define a nonlinearly consistent truncation for an arbitrary compact space .

## Overlap couplings

For normalized internal profiles, effective cubic coefficients have the generic form
``` math
g_{ijk}^{(4)}
 =
 g_D
 \int_X
 \mathcal I\!\left(u_i,u_j,u_k;
 h,\nabla,F,\ldots\right)
 \mathrm d\mathrm{vol}_h ,
```
where $`\mathcal I`$ includes the contractions and background insertions dictated by the higher-dimensional action. Selection rules can follow from representations, parity, index theory, or bundle cohomology. Numerical Yukawa or threshold values require the actual normalized wavefunctions, connections, scales, and renormalization transport. The mere existence of an overlap formula is not a value-source theorem.

# Relation to current MTT geometry

## What is already available

Current MTT work provides several pieces that are relevant to a future Kaluza–Klein source map:

1.  a dimension-neutral Hilbert-bundle architecture with explicit operator domains, coherent spectral projectors, and separate stabilization and truncation gates;

2.  the canonical $`4+6`$ physical specialization;

3.  the local six-dimensional strain decomposition $`\operatorname{Sym}(3)=1\oplus2\oplus3`$;

4.  a selected finite $`q=79`$ carrier with the same rank filtration; and

5.  one universal finite differential line with connection- and holonomy-preserving pullbacks across the proven finite sectors .

These are nontrivial compatibility results. They make the desired global map more structured than a guess.

## What is not yet available

Rank agreement does not identify the local strain carrier with the vertical tangent or field bundle of a physical compactification. The current open step is a same-source continuum intertwiner that preserves:
``` math
\text{bundle transitions},\quad
\text{connection},\quad
\nabla,\quad
\text{measure},\quad
\text{operator domains},\quad
\text{Hessian}.
```
The physical $`q=79`$ program additionally needs the selected visible and hidden holomorphic bundles and their Hermitian–Yang–Mills connections before those vertical operators can be executed. Until then, the finite rank carrier is not a Kaluza–Klein compactification record.

## Calabi–Yau, Fu–Yau, and M-theory branches

The corrected Calabi–Yau paper treats strict Calabi–Yau compactification as a conditional realization map and separates fixed-background spectral facts from vacuum selection . The selected $`q=79`$ Fu–Yau program is instead a torsional non-Kähler heterotic branch; it cannot be substituted for a strict Calabi–Yau result merely because both use six internal dimensions.

The corrected M-theory paper treats the eleven-dimensional low-energy record and its massless type-IIA circle reduction . That circle is not automatically the finite shared MTT phase line. This paper supplies the general Kaluza–Klein reduction interface; it does not re-own either the Calabi–Yau spectral theorem or the M-theory circle dictionary.

## Lens–Nil and recursive topology

Circle, Lens, and Nil language may organize filtrations, bundle towers, or effective local models. Literal $`S^1\times\mathrm{Lens}\times\mathrm{Nil}`$ and literal manifold nesting are not current proof sources for the physical $`q=79`$ compactification. In particular, the old Lens–Nil and Fu–Yau models have different global topological data and must not be identified. A recursive or circle-fibered description becomes physical only when the relevant total space, transition functions, connection, and operator compatibility are specified.

# Claim disposition

| Version 1 claim | Version 2 status | Resolution |
|:---|:---|:---|
| MTT derives Kaluza–Klein compactification from first principles | Withdrawn | MTT currently supplies a conditional source-and-factorization contract. |
| MTT selects $`B_{\rm KK}`$, $`R_{\rm KK}`$, and the zero-mode spectrum | Open | These must be emitted as geometry, scale, and operator data by one selected source. |
| $`9\to3`$ projection independently proves $`10\to4`$ compactification | Narrowed | They are spatial and spacetime descriptions of the same supplied time-compatible $`4+6`$ fibration. |
| The finite FCC is equivalent to the higher-dimensional PDE | Corrected | It is equivalent only to the residual equations restricted to a closed finite ansatz. |
| Invariant cohomology makes the ansatz complete | Withdrawn | Cohomological completeness does not imply field-configuration or PDE completeness. |
| A spectral gap justifies zero-mode truncation | Corrected | A gap helps invert the omitted linear block; residual and nonlinear bounds are also required. |
| Planck, gauge, and KK masses are MTT predictions | Conditional formulas | They are computed from supplied action normalizations, geometry, operators, and radii. |
| Internal isometries select the observed gauge group | Open | Isometries provide candidate gauge vectors; selection and nonlinear consistency require additional data. |
| Iwasawa and Lens–Nil examples prove physical compactification selection | Retired as proof sources | They may remain auxiliary invariant models but do not establish the current physical $`q=79`$ branch. |
| MTT gap data fix families, thresholds, and observed couplings | Removed | Those claims require selected normalized modes, source values, and renormalization transport. |

# Completion contract

A selected MTT Kaluza–Klein realization will be established only when one source supplies and one independent verification checks the following:

1.  a global $`D`$-dimensional Lorentzian fibration with compact internal geometry, transition maps, horizontal connection, spin or spin$`^{c}`$ data, and all required bundles;

2.  the higher-dimensional field content, action, symmetries, sources, normalizations, and declared classical or quantum order;

3.  the vertical operators with domains, measures, adjoints, boundary conditions, normalized modes, and scale conventions;

4.  the selected background and a proof that it solves the supplied equations, rather than only a subset of projected coefficients;

5.  an exact nonlinear uplift or a residual certificate of the form in Proposition <a href="#prop:residual" data-reference-type="ref" data-reference="prop:residual">9</a>, including propagation to the stated observables;

6.  a source-preserving map from the MTT strain and shared-line data to the physical vertical bundles, connections, derivatives, and Hessians;

7.  normalized four-dimensional Planck, gauge, mass, chirality, and interaction data derived from that same source; and

8.  a clear separation between construction inputs, fitted values, profile checks, and held-out predictions.

The first five items would establish a controlled Kaluza–Klein reduction. The sixth would make it an MTT-sourced reduction. The final two would be needed before phenomenological equivalence or prediction could be claimed.

# Discussion

## Why this correction strengthens the program

The corrected paper asks less rhetorically and more mathematically. It no longer treats the existence of familiar lower formulas as evidence that their inputs were derived. Instead, it turns the missing source into a finite list of typed obligations. This is useful even before closure: different candidate compactifications can be compared row by row, and a failure in geometry, action, truncation, or normalization cannot be hidden inside a generic projection symbol.

The distinction between spectrum and truncation is especially important. Compactness gives a tower. It does not say that the light part of the tower is closed under interactions. The residual certificate identifies the quantities that a computation must actually bound. It also gives a natural place for the MTT fixed-point and semigroup machinery: those methods may control $`\gamma_N`$, $`L_\rho`$, and $`r_N`$, but only after the physical operator and its source have been identified.

## What could become distinctive

Traditional Kaluza–Klein theory begins after a higher-dimensional record is chosen. MTT asks one level upstream whether the same upper object sources the internal geometry, shared line, operators, action, and admissible low sector. A connection-preserving intertwiner and upper-action map would not replace Kaluza–Klein theory; they would explain why a particular record is the correct lower image and why its truncation is admissible.

That is the credible advantage of the MTT route. Component counts and replayed four-dimensional values remain insufficient: the upstream source must reduce independent choices, not rename them.

# Conclusion

Kaluza–Klein reduction is exact mathematics once its higher-dimensional record and consistency hypotheses are fixed. On a closed compact fiber, self-adjoint elliptic operators give discrete towers, and the tower masses are internal eigenvalues with the appropriate metric scaling. Internal isometries and normalized overlap integrals can generate gauge fields and effective couplings. Finite invariant ansatzes can turn their restricted equations into exact algebraic systems.

None of those facts selects the internal space, radius, action, gauge group, or nonlinear truncation. Version 2 therefore replaces the former first-principles claim by a conditional MTT realization theorem and an explicit truncation certificate. It reconciles the spatial $`9\to3`$ language with the canonical $`10\to4`$ fibration, keeps the shared circle as common phase/holonomy data at its proven level, and separates local $`1+2+3`$ rank agreement from the still-open physical continuum intertwiner.

The route forward is sharp: select one physical vertical geometry and action, preserve their connection and Hessian under the MTT source map, execute the appropriate internal operators, and certify the retained sector by exact consistency or quantitative residual bounds. That would turn this contract into a selected MTT Kaluza–Klein realization. Until then it proves compatibility and a rigorous proof interface, not extra-dimensional phenomenology.

#### Corpus-state cross-checks.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*derived exact*).

  Literal 81-entry, 729-cocycle finite Cech witness.

- (*derived exact*).

  Executable q=79 exact-branch audit.

- (*derived exact*).

  CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The exact q79 arithmetic, finite rank-two Cech witness, and rank-two Wiener-contraction certificate are contextual evidence for an adjacent selected heterotic branch. They do not directly construct the physical compact six-manifold, higher-dimensional action, nonlinear uplift, normalized vertical mode system, Kaluza-Klein radius, gauge group, consistent truncation, or the connection- and Hessian-preserving MTT-to-Kaluza-Klein realization map.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Corpus-state cross-checks

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A07/literal_cech_witness` (**DERIVED_EXACT**): Literal 81-entry, 729-cocycle finite Cech witness.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
