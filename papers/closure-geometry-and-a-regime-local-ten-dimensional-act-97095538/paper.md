---
abstract: |
  We formulate a ten-dimensional effective action compatible with closure-strain and q79 carrier data. The metric, bundle $`M_{10}\to Y_4`$, compact fiber, field representations, and derivative expansion are declared realization inputs. The action is an ansatz on a specified regime, not the most general action and not a derivation of gravity from projection. We give the conditions under which a closure Hessian contributes to canonically normalized pole masses, a rank-four real alignment projector yields one Higgs doublet, an internal operator has discrete spectrum, and a four-dimensional mode truncation is consistent. Curvature is defined through explicit connections rather than inferred from nonuniform strain. The selected q79 Fu–Yau branch is the compactification candidate, while Lens–Nil remains auxiliary. Existing finite-matrix and Standard-Model profile calculations are incorporated at their declared embedded-renormalized-SM tier; their profile inputs and imported BRST quantization are not reclassified as no-knob consequences of this action. Finite residual, cyclic-action, and cotangent constructions explain which action data follow from a supplied source and which physical identifications remain additional assumptions.
author:
- Peter Nero
current_version: v5
date: Version 5 September 2026
generated_from_main_tex_sha256: fba3db2514715a045a6194f19cc75ed6088c96975a34d4926976dfa33bf706a4
paper_id: closure-geometry-and-a-regime-local-ten-dimensional-act-97095538
release_state: current_revised_tex
released_version: v4
title: |
  Closure Geometry and a Regime-Local
  Ten-Dimensional Action Ansatz
zenodo_doi: 10.5281/zenodo.21654885
zenodo_record_id: 21654885
zenodo_url: "https://zenodo.org/records/21654885"
---

# Closure Geometry and a Regime-Local Ten-Dimensional Action Ansatz

Peter Nero. Version 5 September 2026

## Abstract

We formulate a ten-dimensional effective action compatible with closure-strain and q79 carrier data. The metric, bundle $`M_{10}\to Y_4`$, compact fiber, field representations, and derivative expansion are declared realization inputs. The action is an ansatz on a specified regime, not the most general action and not a derivation of gravity from projection. We give the conditions under which a closure Hessian contributes to canonically normalized pole masses, a rank-four real alignment projector yields one Higgs doublet, an internal operator has discrete spectrum, and a four-dimensional mode truncation is consistent. Curvature is defined through explicit connections rather than inferred from nonuniform strain. The selected q79 Fu–Yau branch is the compactification candidate, while Lens–Nil remains auxiliary. Existing finite-matrix and Standard-Model profile calculations are incorporated at their declared embedded-renormalized-SM tier; their profile inputs and imported BRST quantization are not reclassified as no-knob consequences of this action. Finite residual, cyclic-action, and cotangent constructions explain which action data follow from a supplied source and which physical identifications remain additional assumptions.

# Version 5 revision note

Supersedes.
Version 4; its release identity and revision note are retained.

Reason.
The ansatz needs the subsequent residual-to-action results in context, and its reduction statement did not distinguish a Schur kernel from a local derivative expansion.

Resolution.
Explain curved repair germs, variational anchors, cyclic Maurer–Cartan descent, and the full-string cotangent boundary. State the additional nonlinear and locality estimates needed in dimensional reduction.

Retained result.
The regime-local ansatz and finite-SM/profile inputs, pole normalization, alignment, and compact-resolvent gates are retained.

Open boundary.
The physical signed action, trace normalization, real slice, same-source visible endpoint, and Lorentzian/BV compactification map remain distinct from the exact finite constructions.

# Version 4 revision note

Supersedes.
*Closure Geometry and Unified Dynamics: A Ten-Dimensional Action for Mass, Scalar Relaxation, Quantization, and Curvature*, version 3.

Reason.
The metric and Einstein–Hilbert term were imported while the action was described as derived and most general; closure cost, Hessian positivity, nil language, and nonuniform strain were also promoted directly to mass, one Higgs, quantization, and curvature.

Resolution.
Version 4 declares a regime-local EFT ansatz, lists omitted operators, and supplies separate pole-mass, alignment-projector, compact-resolvent, curvature, and consistent-truncation gates. This edition also adds a reader map and a worked compactification example so that the role of each gate can be followed without treating the action as a theorem list.

Retained result.
The action remains a useful conditional synthesis and can host the currently certified finite-SM profile branch.

Remaining boundary.
A same-source q79 action, normalized zero modes, gauge-fixed Hessians, reduction error, and strict value selection remain to be constructed.

# Status and regime

Fix an energy interval $`E\ll\Lambda_{10}`$ and an admissible field neighborhood $`\mathcal U`$ on which a local derivative expansion is valid. The word “minimal” below means that only a displayed subset of operators is retained for a stated calculation. It does not mean uniqueness under all symmetries.

The action requires as input:

1.  a ten-dimensional smooth bundle $`\pi:M_{10}\to Y_4`$ with compact six-dimensional fiber $`X_x`$;

2.  a slab-local Lorentzian metric $`g_{10}`$ with one time direction and a globally hyperbolic four-dimensional physical base;

3.  gauge and spin/$`\operatorname{Spin}^c`$ bundles with compatible connections;

4.  the selected q79 Fu–Yau geometry and HYM data, or another explicitly declared compactification;

5.  a field content and symmetry group; and

6.  a power-counting rule and cutoff controlling omitted operators.

The component identity $`1+3\times3=4+6`$ motivates a local comparison carrier but supplies none of these global inputs.

#### How the argument should be read.

There are four logically different stages:
``` math
\begin{gathered}
\boxed{\text{declared geometry and fields}}
\longrightarrow
\boxed{\text{action ansatz}}\\
\Downarrow\\[-1mm]
\boxed{\text{equations and mode reduction}}
\longrightarrow
\boxed{\text{renormalized observables}} .
\end{gathered}
```
An implication within this chain can be derived once the object on its left has been fixed. The chain as a whole is not thereby selected by MTT. In particular, varying an assumed ten-dimensional action rigorously derives its field equations, but it does not prove that this is the unique action chosen by closure geometry. The separate gates below answer four practical questions: which quadratic coefficients are masses, which scalar modes form a Higgs doublet, why the internal spectrum is discrete, and when discarding heavy modes is legitimate.

# Fields and typed geometry

Let $`Q_{\rm WW}\in\Gamma(\operatorname{Hom}(TP,TI))`$ be the rank-three comparison field and let
``` math
S=\frac12\log(Q_{\rm WW}^TQ_{\rm WW})
```
be its local strain. A selected flag gives the strain projectors $`P_{\rm sc},P_{\rm sh},P_{\rm nil}`$ of ranks $`1,2,3`$.

For the q79 degree-three cover, the selected internal carrier is
``` math
\mathcal H_{\rm q79}
 =L_{\rm shared}\otimes
 (\mathcal O\oplus\mathcal A_0\oplus\mathcal A),
 \qquad \operatorname{rank}=1+2+3.
```
An action using $`S`$ as the source of q79 fields must include or cite a global intertwiner $`\mathfrak I_{\rm WW\to q79}`$ preserving metrics, connections, and the selected operators. This paper does not infer it from rank equality.

Let $`\phi^A`$ denote real scalar coordinates on the retained field manifold, $`A_M^a`$ a gauge connection, $`\Psi`$ a spinor in a declared representation, and $`H`$ a selected complex scalar module when present.

# Regime-local action ansatz

One two-derivative ansatz is <a id="eq:action"></a>
``` math
\begin{align}
S_{10}=\int_{M_{10}}\!\sqrt{|g_{10}|}\,\mathrm{d}^{10}x\,
\Big[&\frac{1}{2\kappa_{10}^2}R_{10}
-\frac14 k_{ab}(\phi)F^a_{MN}F^{b\,MN}
-\frac12G_{AB}(\phi)D_M\phi^A D^M\phi^B\nonumber\\
&-V(\phi)
+i\overline\Psi\Gamma^M D_M\Psi
-\overline\Psi\,\mathcal M(\phi)\Psi
+\mathcal L_{H,B,\Phi}
\Big]
+S_{\rm gf}+S_{\rm gh}+S_{\rm bdy}.

\end{align}
```
Here $`k_{ab}`$ and $`G_{AB}`$ must be positive on physical directions, $`\mathcal L_{H,B,\Phi}`$ records the selected flux/torsion/dilaton sector, and the gauge-fixing, ghost, and boundary terms are part of the definition of a quantized perturbative calculation.

Equation [(3.1)](#eq:action) imports the Einstein–Hilbert term and a Lorentzian metric. It therefore realizes gravity; it does not derive gravity from strain or projection.

Each displayed term has a distinct job. The $`R_{10}`$ term determines the metric response, $`F^2`$ supplies gauge propagation, $`G_{AB}D\phi^A D\phi^B`$ defines the scalar normalization, $`V`$ and $`\mathcal M`$ supply quadratic and interaction coefficients, and $`\mathcal L_{H,B,\Phi}`$ carries the flux–torsion sector. Varying these fields gives, schematically,
``` math
\frac{\delta S_{10}}{\delta g_{10}}=0,\qquad
\frac{\delta S_{10}}{\delta A}=0,\qquad
\frac{\delta S_{10}}{\delta\phi}=0,\qquad
\frac{\delta S_{10}}{\delta\overline\Psi}=0.
```
These equations are consequences of the ansatz. Their coefficients remain inputs unless an upstream source theorem derives them from the selected q79 geometry. This distinction is important: an internally consistent solution of the field equations tests the assumed model, whereas source selection explains why that model and those coefficients apply.

## Omitted operators

Unless forbidden by a stated symmetry, the effective action can also contain
``` math
\begin{gathered}
 R^2,\quad R_{MN}R^{MN},\quad R_{MNPQ}R^{MNPQ},\quad
 RF^2,\quad F^3,\quad F^4,\\
 (D\phi)^4,\quad R(D\phi)^2,\quad \phi^n,\quad
 \overline\Psi\Gamma\Psi D\phi ,
\end{gathered}
```
torsion and Chern–Simons terms, higher fermion operators, and higher derivatives. A truncation must bound their contribution by powers of $`E/\Lambda_{10}`$ and the relevant curvature or field amplitudes.

Higher-curvature or higher-time-derivative terms can introduce extra degrees of freedom or ghosts if treated nonperturbatively. In an EFT treatment they are perturbative operators below the cutoff; any claimed fundamental completion requires a separate constraint/propagator analysis.

<a id="sec:repair-action"></a>

# From a repair residual to an action

## Curvature is not detected faithfully by every representation

The curved-repair germ of R1-T1 starts with a graded associative algebra, an odd charge $`Q`$, and a declared trace and real slice. Its curvature and adjoint differential are $`F=Q^2`$ and $`d_Q X=QX-(-1)^{|X|}XQ`$. The identities
``` math
d_Q^2X=[F,X],\qquad d_QF=0
```
separate three regimes: $`F=0`$; nonzero central $`F`$; and noncentral $`F`$. Only the last necessarily curves the adjoint differential \[[1](#ref-FrozenGerm)\]. For example, the odd matrix $`Q=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)`$ has $`Q^2=I`$. Its adjoint differential squares to zero, but its defect is nonzero and the Jordan response $`FX+XF=2X`$ survives. Nilpotence in an adjoint representation is therefore not a test for exact physical closure. An algebraic differential also needs a positive metric and suitable domains before Hodge or dissipative language applies.

For a smooth residual $`\Phi:E\to F_{\rm res}`$ with a positive residual metric $`W(a)`$, the repair cost is $`S_{\rm rep}(a)=\frac12\langle\Phi(a),W(a)\Phi(a)\rangle`$. At $`\Phi(a_*)=0`$ its Hessian is $`J^\dagger W(a_*)J`$, where $`J=D\Phi(a_*)`$. This measures sensitivity to defects. It is not yet the Euler–Lagrange operator of [(3.1)](#eq:action).

<a id="sec:anchor"></a>

## Variational anchors and the information lost by squaring

H4-T9 supplies a direct test \[[2](#ref-FrozenAnchor)\]. A chosen anchor $`A:F_{\rm res}\to E^*`$ turns the residual into a field-space one-form $`\alpha_a(v)=(A\Phi(a))(v)`$. On a star-shaped finite-dimensional domain, $`dS_{\rm var}=\alpha`$ exists exactly when $`d\alpha=0`$, or equivalently when $`D(A\Phi)`$ is symmetric. The reconstructed action is
``` math
S_{\rm var}(a)-S_{\rm var}(0)=\int_0^1\alpha_{ta}(a)\,dt.
```
For fields, this becomes a graded formal-adjoint Helmholtz condition with boundary terms and operator domains. It is not implied by positivity of $`W`$. Indeed $`(x,y)`$ and $`(-y,x)`$ have identical repair cost $`(x^2+y^2)/2`$, but the latter is not a gradient for the standard anchor: its Jacobian has antisymmetric part $`\left(\begin{smallmatrix}0&-2\\2&0\end{smallmatrix}\right)`$.

Every residual nevertheless has a multiplier action $`S_{\rm mult}(a,\lambda)=\langle\lambda,\Phi(a)\rangle`$. Its equations are $`\Phi(a)=0`$ and $`D\Phi(a)^\dagger\lambda=0`$. At $`(a_*,0)`$ the Hessian and its square are
``` math
D_J=\begin{pmatrix}0&J^\dagger\\J&0\end{pmatrix},\qquad
 D_J^2=\begin{pmatrix}J^\dagger J&0\\0&JJ^\dagger\end{pmatrix}.
```
Thus the repair operator is one normal block. The added multiplier is not automatically a particle or BV antifield, nor is $`D_J`$ automatically a Lorentzian Dirac operator.

The distinction is visible without a large calculation. For $`S_{\rm var}(x)=mx^2/2+gx^3/6`$, squaring its derivative gives
``` math
S_{\rm rep}(x)=m^2x^2/2+mgx^3/2+g^2x^4/8.
```
At zero, the quadratic, cubic, and quartic derivatives are $`(m,g,0)`$ for the action and $`(m^2,3mg,3g^2)`$ for the repair cost. At the second root $`x=-2m/g`$, with $`g\ne0`$, the signed Hessian is $`-m`$ but the repair Hessian is $`m^2`$. Repair stability has erased the sign and changed the vertices. A physical propagator or pole mass must use the correctly identified signed, gauge-fixed operator.

<a id="sec:cyclic-action"></a>

## A cyclic integrability lane really does have an action

H4-T10 is a positive construction, not just a warning \[[3](#ref-FrozenMC)\]. Let $`\mathcal A`$ be a characteristic-zero dg algebra with a degree-three trace $`\tau`$ satisfying graded cyclicity and $`\tau(dx)=0`$. For $`a\in\mathcal A^1`$, define
``` math
F(a)=da+a^2,\qquad
 S_{\rm MC}(a)=\tfrac12\tau(a\,da)+\tfrac13\tau(a^3).
```
Then $`DS_{\rm MC}(a)[u]=\tau(uF(a))`$. Nondegeneracy of the pairing between degrees one and two is required to identify the critical locus with the full Maurer–Cartan zero set; otherwise only a weak variational identity follows. Stokes and the Bianchi identity give infinitesimal gauge invariance, not an automatic large-gauge quantization of the coefficient.

For projective overlaps $`G_{ij}G_{jk}G_{ki}=\alpha_{ijk}I`$, scalar twists cancel in endomorphism conjugation. If the differentials and traces intertwine, the action descends through that same atlas. This does not assert that an arbitrary Fourier–Mukai equivalence preserves the trace. On a compact boundaryless complex threefold the candidate trace is $`\tau(x)=\int_X\Omega_{\rm hol}\wedge\operatorname{Str}(x)`$. The holomorphic volume form and its physical normalization are separate from a unit-normalized volume form used by a Hermitian metric.

At an exact solution the signed Hessian is $`C_\tau J`$, with $`C_\tau`$ the cyclic anchor, whereas the positive repair Hessian is $`J^\dagger WJ`$. The frozen rational exterior-algebra witness explicitly has a negative signed direction absent from the repair square. It supplies the integrability action, not the full ten-dimensional ansatz.

<a id="sec:string-cotangent"></a>

## Why the full string complex needs more than that trace

The full q79 string deformation complex also has form/anomaly lanes. H4-T14 identifies a precise obstruction \[[4](#ref-FrozenCotangent)\]: using only wedge product, top-form integration, the invariant gauge pairing, and $`\Omega_{\rm hol}`$, those lanes lie in the pairing radical. Their degree-one types $`(3,0),(2,1)`$ and degree-two types $`(3,1),(2,2)`$ have wedges of holomorphic degree at least four on a threefold. Cross terms would require an invariant linear functional on $`\mathfrak{sl}_3\oplus\mathfrak{sl}_3\oplus\mathfrak{sl}_9`$, which vanishes because the algebra equals its commutator algebra. This excludes that local trace grammar, not every possible action.

For a locally perfect dg Lie algebra $`L`$, its density-valued local dual $`L^!`$ gives the canonical cyclic completion
``` math
\widehat L=L\ltimes L^![-3],\qquad
 S_{\rm cot}(a,p)=\langle p,da+\tfrac12[a,a]\rangle.
```
The shift uses $`(V[s])^k=V^{k+s}`$; the familiar shifted-cotangent notation on a suspended field stack uses a different grading. Dual variation recovers the full residual, and every original solution lifts to $`(a,0)`$. The algebraic pairing is canonical, but its physical coefficient, real slice, charged fields, and identification with the accepted BV action are not supplied by this construction.

The central shared line acts trivially on product-adjoint and ordinary-form lanes and hence on their cotangent duals. Relative charged $`\operatorname{Hom}`$ lanes are outside this neutrality claim. The fuller string-algebroid and Calabi moment-map reductions are explained by the companion Cohesive paper \[[5](#ref-Cohesive14)\]: anomaly is part of integrability, and HYM/balance can be combined under their stated source hypotheses. They do not require a new independent action ansatz for every residual row. The remaining comparison is one physical source, trace, moment map, and BV-compatible compactification, with the Lorentzian coframe sector still separate.

# Closure Hessian and physical masses

Let $`\varphi=0`$ be a stationary background for retained real fields and write the quadratic four-dimensional action after integrating the internal fiber as
``` math
S_4^{(2)}
 =\frac12\int_{Y_4}\sqrt{|g_4|}\,\mathrm{d}^4x
 \left(
 Z_{AB}\,\partial_\mu\varphi^A\partial^\mu\varphi^B
 -M^2_{AB}\varphi^A\varphi^B
 \right).
```

<div class="theorem">

**Theorem 1** (Pole-mass promotion). *Assume $`Z`$ is positive definite, the quadratic operator is self-adjoint on its declared domain, and interactions admit the stated perturbative pole definition. At tree level the squared masses are the eigenvalues of
``` math
Z^{-1/2}M^2Z^{-1/2}.
```
A closure Hessian $`H_{\mathcal J}`$ contributes to physical mass only after a source theorem identifies $`M^2=C^*H_{\mathcal J}C`$ for a normalized field map $`C`$.*

</div>

<div class="proof">

*Proof.* The field redefinition $`\widehat\varphi=Z^{1/2}\varphi`$ canonically normalizes the kinetic term. The inverse propagator is then $`p^2I-Z^{-1/2}M^2Z^{-1/2}`$, whose zeros give the tree-level poles. The final statement follows because an unnormalized dimensionless cost is not the quadratic coefficient in the physical action until $`C`$ and units are fixed. ◻

</div>

Loop-corrected pole masses require the renormalized self-energy and a declared mass scheme. Eigenvalues of an internal Hessian are not automatically pole masses.

# Scalar alignment and the Higgs gate

A positive Hessian on the six-dimensional strain sector proves local stability, not one scalar. Suppose instead that the selected finite fluctuation space $`V_{\rm scal}`$ carries the required gauge representation and there is a source-selected orthogonal projector
``` math
P_H:V_{\rm scal}\to V_H,
 \qquad \operatorname{rank}_{\mathbb R}V_H=4,
```
onto one complex weak doublet.

<div class="proposition">

**Proposition 2** (Conditional one-doublet reduction). *If $`P_H`$ commutes with the quadratic gauge-fixed operator, the orthogonal complement is massive above the truncation gap or consistently removed, and the potential restricted to $`V_H`$ has the Standard-Model symmetry-breaking form, then the retained scalar sector contains one Higgs doublet at that scale.*

</div>

The selected finite-algebra packet executes such a rank-four alignment projector on a raw rank-twelve real fluctuation space and removes eight real scalar directions at the declared profile tier. That is the relevant selection result. It must not be replaced by “the Hessian has a unique radial direction,” which is false without the projector and representation data.

# Discrete spectra and quantization

Let $`D_X`$ be a self-adjoint internal Dirac-type or Laplace-type operator on the compact fiber with elliptic boundary conditions when a boundary is present.

<div class="theorem">

**Theorem 3** (Internal spectral discreteness). *If $`(D_X-i)^{-1}`$ is compact, then the spectrum of $`D_X`$ is discrete with finite-multiplicity eigenvalues accumulating only at infinity.*

</div>

This theorem justifies a Kaluza–Klein or finite spectral expansion. A nil group, nil boundary, or divergent cost does not by itself imply compact resolvent or isolated minima. Moreover, spectral discreteness is not a derivation of quantum probabilities. Quantization still requires a state space, observable algebra, dynamics, constraints, and probability rule.

# A concrete compactification foothold

The simplest model showing what the spectral and reduction statements do is not the selected q79 geometry but a product $`M_{10}=Y_4\times T^6`$ with circle radii $`R_i`$. For a real scalar of ten-dimensional mass $`\mu`$, normalized Fourier modes give
``` math
\Phi(x,y)=
\sum_{\mathbf n\in\mathbb Z^6}
\phi_{\mathbf n}(x)
\prod_{i=1}^{6}
\frac{\exp(i n_i y_i/R_i)}{\sqrt{2\pi R_i}},
\qquad
m_{\mathbf n}^2
=\mu^2+\sum_{i=1}^{6}\frac{n_i^2}{R_i^2}.
```
Compactness has turned the internal differential operator into a discrete mass tower. The zero mode has mass $`\mu`$, while the first discarded mode is separated by a gap of at least $`\min_i R_i^{-2}`$ in squared mass. This is the elementary mechanism abstracted by the compact-resolvent theorem.

For translation-invariant polynomial interactions, a field that is constant on $`T^6`$ remains constant under multiplication. The zero-mode sector then closes on itself and setting every nonzero mode to zero is an exact consistent truncation. If the background coefficients depend on $`y`$, or if retained nonzero modes multiply to source discarded momenta, that closure fails and the Schur–Feshbach estimate below is needed. Thus “the heavy modes have a large mass” and “the heavy modes are not sourced” are different claims. The example explains the logic only; it neither identifies the q79 fiber with $`T^6`$ nor supplies the missing q79 overlap kernels.

# Curvature and integrability

Let $`P_H`$ now denote a projector defining a horizontal distribution in a declared bundle, and let $`\nabla`$ be a connection. Its curvature is
``` math
F_\nabla=\nabla^2,
```
or locally $`F=\mathrm{d}A+A\wedge A`$. Frobenius failure of a distribution is tested by the vertical part of $`[X,Y]`$ for horizontal vector fields $`X,Y`$.

The condition $`\nabla S\ne0`$ says only that strain is nonparallel. It does not by itself imply nonintegrability, Riemann curvature, or the Einstein equations. Any curvature–strain coupling in [(3.1)](#eq:action) must be written with an explicit connection and varied to obtain its field equations.

# q79 Fu–Yau specialization

The current selected global compactification candidate is the q79 Fu–Yau branch with its declared complex, flux, spectral-cover, and HYM data. Known Hull–Strominger/Fu–Yau mathematics supplies a legitimate class of heterotic backgrounds once anomaly cancellation and the relevant bundle conditions are satisfied.

The auxiliary geometry $`L(3,1)\times\mathrm{Nil}_3`$ can support model calculations but is not the same manifold: its cohomology already differs from the q79 branch. The action must choose one background and integrate over that background. Literal $`S^1\times\mathrm{Lens}\times\mathrm{Nil}`$ and literal nesting are not used to define $`X_6`$.

The shared circle is encoded by $`L_{\rm shared}`$ and its connection. It is counted once and is not a time coordinate.

# Four-dimensional reduction

Let $`\{\chi_n(y)\}`$ be normalized internal modes and expand a field as
``` math
\Phi(x,y)=\sum_{n\in I_{\rm keep}}\phi_n(x)\chi_n(y)
 +\sum_{r\in I_{\rm disc}}\eta_r(x)\chi_r(y).
```
Setting all $`\eta_r`$ to zero is a consistent truncation only if their exact Euler–Lagrange equations vanish on the retained ansatz:
``` math
\left.\frac{\delta S_{10}}{\delta\eta_r}\right|_{\eta=0}=0
 \quad\text{for every }r\in I_{\rm disc}.
```

<div class="theorem">

**Theorem 4** (Conditional coherent reduction). *At a fixed truncation order, assume that the discarded linear operator is invertible on its declared domain with $`\|L_{\rm disc}^{-1}\|\le C/\lambda_{\rm gap}`$, and the source into discarded modes obeys $`\|J_{\rm disc}\|\le\epsilon`$. Then the leading linearized eliminated field obeys
``` math
\|\eta\|\le
 \|L_{\rm disc}^{-1}\|\,\epsilon
 \le \frac{C\epsilon}{\lambda_{\rm gap}},
```
and substitution gives the quadratic Schur–Feshbach correction. For the nonlinear equation $`L_{\rm disc}\eta+J_{\rm disc}+N(\eta)=0`$, also require that $`-L_{\rm disc}^{-1}(J_{\rm disc}+N(\eta))`$ preserves a specified ball and has Lipschitz constant $`q<1`$ there, with $`N(0)=0`$. The solution then satisfies $`\|\eta\|\le C\epsilon/((1-q)\lambda_{\rm gap})`$. A local effective action additionally requires a controlled low-energy derivative expansion of the resulting generally nonlocal kernel.*

</div>

<div class="proof">

*Proof.* Apply the inverse bound for the leading term and the contraction estimate for the nonlinear equation. The Schur complement follows by substitution; its locality does not follow from invertibility. Exact consistency is the case in which the discarded equations vanish identically on the retained ansatz, so $`J_{\rm disc}=0`$ and $`\eta=0`$ solves them. ◻

</div>

A spectral gap alone does not prove nonlinear invariance or exact truncation.

# Gauge fixing, anomalies, and observables

A perturbative gauge theory built from [(3.1)](#eq:action) must include a common gauge-fixing, ghost, zero-mode, regulator, scale, and renormalization-scheme policy. BRST nilpotency and anomaly cancellation are equations to verify. Physical predictions require a functor from action parameters to renormalized local or scattering observables.

The current embedded-renormalized-SM closure imports standard BRST/Faddeev–Popov quantization at its declared profile tier. This is a valid reconstruction standard, but it is not a derivation of the BRST/path-integral or Born-record rules from MTT.

# Relation to the current numerical closure

At the adopted one-shared-physical-primitive/profile standard, the calculation repositories lock the finite $`27\times27`$ matrix, the physical finite Dirac operator at profile tier, charged Yukawa magnitudes, CKM rows, electroweak and threshold rows, multi-loop precision transport, and the renormalized observable functor. The final audit reports embedded renormalized-SM equivalence at that stated standard.

This action paper neither demotes nor strengthens those certificates. It records what would be needed to derive the same data from one ten-dimensional source action:

1.  the world-in-world/q79 bundle-and-connection intertwiner;

2.  the selected normalized internal zero modes and overlap kernels;

3.  one common gauge-fixed Hessian and transport policy;

4.  the consistent-truncation or error theorem; and

5.  independent source selection if strict no-knob closure is claimed.

# Scoped action theorem

<div class="theorem">

**Theorem 5** (Regime-local action statement). *Given the geometric, representation, metric, gauge-fixing, and EFT inputs of this paper, action [(3.1)](#eq:action) defines a local covariant realization on the declared domain. Under compact-resolvent, alignment-projector, pole-normalization, and consistent-reduction hypotheses, it yields a discrete internal mode expansion, a selected one-doublet scalar sector, canonically defined tree-level masses, and a controlled four-dimensional effective action.*

</div>

The theorem is conditional. It does not establish uniqueness of the action, derive the metric or dimension, select the q79 vacuum, or prove the full Standard Model without the listed source and observable maps.

# Conclusion

The action is a useful synthesis ansatz, not a universal derivation. Its value is that every physical promotion now has a recognizable mathematical gate: global geometry, connection, compact resolvent, scalar projector, canonical pole normalization, gauge consistency, and controlled reduction. The next decisive construction is the same-source q79 intertwiner followed by evaluation of the action’s normalized internal rows.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The action written here remains a regime-local ansatz. The exact q=79, finite-action, anomaly, HYM, and internal TT packets constrain or instantiate ingredients used by the ansatz, but they do not derive its continuum action, physical normalization, or ultraviolet completion. Profile rows are retained only as cross-checks on the lower effective target.

The referenced rows are frozen to the curated results repository state identified below. Hashes are grouped in eight-character blocks for line breaking.

> **Repository:** <https://github.com/PeterNero/mtt-results-repro>
> **Commit:** `31247ebb 5c22f3fb b5443024 365433c6 ee0bff4a`
> **Manifest:**
> **Manifest SHA-256:**
> `fb399689 60b00584 631dbf53 1a708e18`
> `ef928d6b 6d935119 c185d7f6 32b1e7cd`

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper’s local theorems; and an open row is evidence of an unresolved obligation, never of closure.

= by -
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

#### Rows used directly in this paper.

- (*derived exact*).

  Promoted direct K_threshold.Omega_H.lambda row.

- (*derived exact*).

  E6 Qpsi matter/exotic QCD anomaly cancellation audit.

- (*derived exact*).

  Exact-branch internal TT support certificate; physical normalization remains open.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*derived exact*).

  Executable q=79 exact-branch audit.

- (*derived exact*).

  CRT q=79 theorem on the selected exact branch.

- (*derived exact*).

  Sparse 27x27 qutrit-Weyl left-action realization.

= by -

#### Corpus-state cross-checks.

- (*profile replay*).

  Versioned Yu, Yd, Ye and lambda_H profile packet.

- (*numeric certified*).

  Three selected CKM profile rows and uncertainty comparison.

- (*profile replay*).

  Current non-looping global status and source-certificate map.

- (*profile replay*).

  Twelve-obligation embedded renormalized-SM equivalence audit.

- (*profile replay*).

  Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.

- (*profile replay*).

  Fifteen measured source coordinates, Jacobian and covariance transport.

- (*profile replay*).

  Eight-coordinate SMDR output with positive-definite 8x8 covariance.

- (*derived exact*).

  Promoted P_EW source row at the declared one-shared-primitive standard.

= by -

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

# References

<a id="ref-FrozenGerm"></a>

\[1\] P. Nero, *Curved cyclic repair germ*, R1-T1, frozen result , 2026. <https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/preprojection_curved_cyclic_repair_germ/artifact.json>.

<a id="ref-FrozenAnchor"></a>

\[2\] P. Nero, *Variational anchor, multiplier lift, and normal square*, H4-T9, 2026. <https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/preprojection_h4_variational_anchor_multiplier_lift/artifact.json>.

<a id="ref-FrozenMC"></a>

\[3\] P. Nero, *Cyclic Maurer–Cartan action and twisted descent*, H4-T10, 2026. <https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/preprojection_h4_cyclic_mc_action_descent/artifact.json>.

<a id="ref-FrozenCotangent"></a>

\[4\] P. Nero, *q79 shared-line neutrality and cyclic cotangent completion*, H4-T14, 2026. <https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/preprojection_h4_q79_string_cyclic_cotangent/artifact.json>.

<a id="ref-Cohesive14"></a>

\[5\] P. Nero, *Cohesive Closure Repair and Its Hodge, Kernel, and Projection Shadows: From Nonlinear Defects to Tangent Semigroups, with the Physical-Action Boundary*, version 14, string-algebroid and BV sections, MTT papers repository, 2026.

<a id="ref-WeinbergEFT"></a>

\[6\] S. Weinberg, *The Quantum Theory of Fields, Vol. II*, Cambridge University Press, 1996.

<a id="ref-FuYau"></a>

\[7\] J.-X. Fu and S.-T. Yau, *The theory of superstring with flux on non-Kahler manifolds and the complex Monge–Ampere equation*, J. Differential Geom. 78 (2008).

<a id="ref-MTTSM"></a>

\[8\] P. Nero, *MTT Current True SM Closure Consolidated Ledger*, internal theorem and verification packet, 2026.
