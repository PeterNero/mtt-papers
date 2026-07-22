---
abstract: |
  We give a corrected functional-analytic foundation for Modal Triplet Theory (MTT). The abstract architecture is a Hilbert bundle with three compatible vertical structures, a joint coherent spectral projector, a stabilization flow, and explicitly separate hypotheses for gap, invariance, existence, contraction, truncation, and admissibility. The canonical physical realization is a ten-dimensional bundle $`M_{10}\to Y_4`$ with compact Riemannian fiber $`X_6`$; the central circle is bundle data and is not counted as an additional product dimension. Strong commutation or a single total internal operator is assumed rather than inferred from notation. Complementary-mode stability uses a stable-semigroup estimate that remains valid for nonnormal generators. Projected time-step fixed points are distinguished from equilibria, and Banach, Schur–Feshbach, projector-stability, and basin-robustness statements are given with their required domains. Stabilization time, physical time, and renormalization scale are separated. Selection by reset is identified as a hybrid law unless derived from continuous upper dynamics. Lorentzian signature belongs to a hyperbolic principal symbol in a physical completion, not to a positive Hilbert-space Gram form. A complete admissibility ledger records the independent obligations inherited by every downstream MTT realization. A rank-three world-in-world comparison field and the selected q79 trace-split carrier are included as a typed geometry interface: their matching component counts do not by themselves derive a ten-dimensional manifold, Lorentzian spacetime, or a global intertwiner. The shared-circle claim is upgraded from fiberwise analogy to an exact finite differential-line theorem: one universal flat $`\mathbb Z_{64}`$ line pulls back coherently to the q79 SpinC determinant, the $`1+2+3`$ carrier, the root-plane complex structure, and the finite Reynolds Hessian. Boothby–Wang geometry independently identifies lens and Heisenberg nil manifolds as parallel curved prequantum circle bundles over different bases. These results are compatible but not identical, and neither compact circle flow is physical Lorentzian time.
author:
- Peter Nero
current_version: v8
date: July 2026
generated_from_main_tex_sha256: 67b2cd3bb94fe446e2dbde09e93350fd6cc7500fb3dacd6619da134197b450c9
paper_id: modal-triplet-theory-foundations
release_state: zenodo_released
released_version: v6.0
title: "Modal Triplet Theory: Foundations"
zenodo_doi: 10.5281/zenodo.18268125
zenodo_record_id: 18268125
zenodo_url: "https://zenodo.org/records/18268125"
---

*Part VI of VI in the Fixed Points series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

# Revision note for this edition

Supersedes.  
*Modal Triplet Theory: Foundations*, version 7.

Reason.  
Version 7 correctly typed the shared circle as line-bundle data, but it did not yet distinguish the curved Boothby–Wang Lens/Nil realizations from the later exact flat q79 differential-line theorem, nor did it record the resulting finite connection, holonomy, and Hessian identities.

Resolution.  
Version 8 retains the functional-analytic spine and adds the universal q79 flat differential line, its SpinC/CLN/root-plane/finite- Hessian pullbacks, the parallel Boothby–Wang realization theorem, and the conditional polarized-section readout.

Retained result.  
The coherent-projector and basin-local fixed-point architecture survives as a conditional control-and-reduction framework.

Remaining boundary.  
The flat finite theorem does not identify the nonzero-Chern physical HYM connection, prove the local strain-to-q79 continuum intertwiner, select a physical Hilbert space, or identify compact Reeb flow with time.

# Status, scope, and logical vocabulary

This paper defines an abstract control and reduction architecture. It does not derive a particular quantum theory, gauge group, particle spectrum, spacetime equation, probability law, or numerical constant. Downstream claims must use one of the following statuses:

Axiom or assumption.  
Input structure of a realization.

Conditional theorem.  
A consequence proved from listed hypotheses.

Characterization.  
A necessary form for objects satisfying the premises.

Reconstruction or embedding.  
Recovery or representation of a known framework after compatible data are supplied.

Calibration or postdiction.  
Numerical agreement using target-related input or model selection.

Held-out prediction.  
A quantity not used in construction, calibration, scale choice, or branch selection.

Interpretation.  
A conceptual reading without theorem status.

The word “physical” is reserved for a realization equipped with a selected state space, local evolution law, observable map, and empirical interpretation.

# Dimension-neutral architecture and physical realization

## Abstract Hilbert-bundle form

Let $`Y`$ be a smooth base and let $`\mathcal E\to Y`$ be a real or complex separable Hilbert bundle. A state belongs to a declared Sobolev space
``` math
\mathcal H=H^s(Y;\mathcal E),
```
with $`s`$ chosen so that every nonlinear map and operator domain used below is well defined. The abstract results are dimension neutral.

The modal triplet is represented by three compatible vertical structures
``` math
(\mathcal E_i,A_i,P_i),\qquad i=1,2,3,
```
on the same internal Hilbert fiber. Here $`A_i`$ is a nonnegative self-adjoint vertical operator and $`P_i`$ is its selected low spectral projector. The triplet is not automatically a product of three coordinate manifolds.

## Canonical physical realization

The canonical physical specialization is
``` math
\pi:M_{10}\longrightarrow Y_4,
 \qquad X_x=\pi^{-1}(x),qquad\dim X_x=6,
```
where $`Y_4`$ is a four-dimensional globally hyperbolic Lorentzian base in the physical completion and each compact fiber $`X_x`$ is Riemannian. In a local trivialization, $`M_{10}\simeq Y_4\times X_6`$. Positive elliptic modal operators act vertically on $`X_6`$ and do not create additional causal directions.

If $`X_6`$ is explicitly factorized as $`F_1\times F_2\times F_3`$, then $`\sum_i\dim F_i=6`$. A shared phase circle is represented by a principal $`U(1)`$ bundle or Hermitian line bundle $`L_{\rm cen}\to X_6`$. It is not appended as a seventh independent product coordinate. Recursive nil/lens/circle descriptions may be used as bundle or filtration data, but their dimensions must not be added unless an actual product decomposition is proved.

## Local comparison carrier and selected q79 interface

Let $`TP`$ and $`TI`$ be oriented Euclidean rank-three bundles over a common base. A world-in-world comparison field is a typed section
``` math
Q_{\rm WW}\in\Gamma\!\left(\operatorname{Hom}(TP,TI)\right).
```
After choosing local frames, $`Q_{\rm WW}`$ has nine matrix components. This is not dimension multiplication: the total space of a rank-three vector bundle over a three-dimensional base has dimension $`3+3=6`$.

At a nonsingular comparison background, polar decomposition separates the infinitesimal orientation and strain directions,
``` math
\operatorname{Mat}(3,\mathbb R)
 =\mathfrak{so}(3)\oplus\operatorname{Sym}(3,\mathbb R),
 \qquad 9=3+6.
```
Relative to a selected orthonormal flag, the strain space has the orthogonal decomposition
``` math
\operatorname{Sym}(3,\mathbb R)
 =\mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O,
 \qquad \dim(\mathbb RI_3,\mathcal D_0,\mathcal O)=(1,2,3),
```
where $`\mathcal D_0`$ is traceless diagonal and $`\mathcal O`$ is symmetric off-diagonal. Thus
``` math
1+3\times3=(1+3)+(1+2+3)=4+6=10
```
is an exact component identity once one additional ordering scalar is supplied. It is not a tangent-space decomposition of $`M_{10}`$, does not select a $`3+1`$ Lorentzian base, and does not globalize without transition data.

For the selected degree-three q79 spectral cover, let
``` math
\mathcal A=\pi_*\mathcal O_C,
 \qquad \mathcal A=\mathcal O\oplus\mathcal A_0,
 \qquad \operatorname{rank}(\mathcal O,\mathcal A_0,\mathcal A)=(1,2,3),
```
where $`\mathcal A_0=\ker\operatorname{Tr}`$. The corresponding common carrier is
``` math
\mathcal H_{\rm CLN}
 =L_{\rm shared}\otimes(\mathcal O\oplus\mathcal A_0\oplus\mathcal A),
 \qquad \operatorname{rank}\mathcal H_{\rm CLN}=6.
```
This proves the selected rank filtration, not its identification with the local strain decomposition. Such an identification requires a same-source bundle-and-connection intertwiner. The line bundle $`L_{\rm shared}`$ carries common $`U(1)`$ phase or holonomy data; it is neither an extra product dimension nor physical Lorentzian time.

## Universal q79 differential line and finite operator square

The phrase “one shared circle” has a global meaning only after its classifying maps and connection are retained. Let $`\mathcal L_{64}^{\rm univ}\to B_\nabla\mathbb Z_{64}`$ be the universal flat Hermitian line associated to the primitive character
``` math
\chi_1(n)=\exp(2\pi\mathrm i n/64).
```
On the unbranched q79 sheet stack, let $`c_{\rm sheet}:B^\circ\to BS_3`$ classify the sheet local system. Since $`S_3^{\rm ab}\cong\mathbb Z_2`$, there is exactly one nontrivial homomorphism to $`\mathbb Z_{64}`$,
``` math
h_{S_3}(\sigma)=32\,\epsilon(\sigma),
 \qquad \epsilon(\sigma)=
 \begin{cases}0,&\sigma\text{ even},\\1,&\sigma\text{ odd}.
 \end{cases}
```
Put
``` math
c_{\rm sh}=B(h_{S_3})\circ c_{\rm sheet},
 \qquad
 (L_{\rm sh},\nabla_{\rm sh})
 =c_{\rm sh}^{*}(\mathcal L_{64}^{\rm univ},\nabla_{64}).
```
For both admissible odd roots $`r\in\{1,33\}`$,
``` math
\chi_r\circ h_{S_3}=\operatorname{sgn}.
```
Thus the associated determinant sign line and $`L_{\rm sh}`$ are canonically parallel-isomorphic: their connections and every loop holonomy agree, not merely their fiber dimensions.

<div id="thm:shared-line" class="theorem">

**Theorem 1** (Finite shared-line and Hessian intertwiner). *On the selected q79 flat root-stack symbol, the same pullback $`L_{\rm sh}`$ tensors all three trace lanes
``` math
\mathcal H_{\rm CLN}
 =L_{\rm sh}\otimes(\mathcal O\oplus\mathcal A_0\oplus\mathcal A).
```
Its scalar holonomy commutes with the trace, trace-zero, and full projectors, with the root-plane quarter-turn $`J_{DE}`$, and with the normalized finite Reynolds operators
``` math
P_{\rm Haar}=\frac1{6}\sum_{g\in S_3}\rho(g),
 \qquad
 H_{\rm fin}=\kappa_{\rm fin}(I-P_{\rm Haar}).
```
For the selected two-copy sheet/edge representation,
``` math
\operatorname{rank}P_{\rm Haar}=2,
 \qquad
 \operatorname{spec}(H_{\rm fin}/\kappa_{\rm fin})
 =\{0^{\times2},1^{\times4}\},
 \qquad H_{\rm TT}=\kappa_{\rm fin}I_2.
```
The lifted Hessian is exactly $`I_{L_{\rm sh}}\otimes H_{\rm fin}`$ and introduces no dimensionless fit.*

</div>

<div class="proof">

*Proof.* The character identity gives the parallel determinant-line isomorphism. Scalar line holonomy commutes with every finite sheet operator. Haar averaging is an orthogonal projector, so $`I-P_{\rm Haar}`$ is the complementary projector. Direct decomposition of the selected two-copy permutation representation gives the displayed ranks and spectrum. Tensoring by the same line preserves these identities and proves the intertwining statement. ◻

</div>

The theorem is exact at flat differential-character and finite-symbol tier. It does not identify $`\nabla_{\rm sh}`$ with a nonflat physical HYM connection: a flat trace-free carrier has vanishing real characteristic curvature, whereas the active physical bundle has nonzero $`c_2`$. The continuum target is a spectral-symbol functor and a unitary parallel Hessian comparison, not literal equality of those connections.

## Boothby–Wang Lens and Nil realizations

Let $`(B,\omega)`$ be an integral symplectic manifold. The Boothby–Wang construction produces a principal circle bundle
``` math
U(1)\longrightarrow P_k\xrightarrow{\pi}B,
 \qquad c_1(P_k)=k[\omega],
```
with connection/contact form $`\alpha_k`$ satisfying, in the chosen normalization,
``` math
d\alpha_k=2\pi k\,\pi^*\omega.
```
For $`B=\mathbb{CP}^1`$ this total space is the lens space $`L(k,1)`$; hence $`k=3`$ gives $`L(3,1)`$ exactly at bundle-topology level. For an integral area form on $`T^2`$, the total space is a quotient of the Heisenberg group by a lattice and is a three-dimensional contact nilmanifold .

Consequently Lens and Nil are parallel realizations of one prequantization schema over different bases and curvature classes. They are not literally nested manifolds. Nor are they one literal line bundle: the rigorous common target is the differential classifier $`BU(1)_\nabla`$ with separate maps
``` math
c_{\rm Lens}:\mathbb{CP}^1\to BU(1)_\nabla,
 \qquad
 c_{\rm Nil}:T^2\to BU(1)_\nabla.
```
The flat q79 classifying map factors through $`B_\nabla\mathbb Z_{64}\to BU(1)_\nabla`$. Because the Boothby–Wang connections above have nonzero curvature while the q79 root-stack line is flat on $`B^\circ`$, the constructions cannot be identified connection by connection. A stronger MTT “same circle” theorem would have to select the three classifying maps and coherent comparison $`2`$-cells on a declared correspondence space.

After a polarization, weight-$`m`$ equivariant functions on $`P_k`$ correspond to sections of the associated line $`L^m`$. In a positive holomorphic polarization this gives the familiar readout
``` math
\mathcal H_m=H^0(B,L^m).
```
This is a conditional geometric-quantization Hilbert space, not a Hilbert space selected by the abstract MTT axioms. The periodic Reeb flow is the vertical phase action and must not be identified with noncompact physical time .

# Three independent evolution parameters

The foundation distinguishes:

1.  a stabilization flow $`R_\tau`$ with control parameter $`\tau\ge0`$;

2.  a physical propagator $`U(t_2,t_1)`$, supplied only by a selected physical completion; and

3.  a renormalization or coarse-graining scale $`\mu`$.

No equality among $`\tau`$, $`t`$, and $`\log\mu`$ is assumed. A theorem relating any two of them must specify the map, units, domain, and approximation error.

We write the stabilization equation as
``` math
\partial_\tau\Psi=F(\Psi),\qquad R_\tau(\Psi_0)=\Psi(\tau).
```
Well-posedness is imposed on a declared interval and invariant domain; global well-posedness is not part of the abstract foundation unless proved in a specific realization.

# Joint vertical operator and coherent projector

<div id="ass:joint" class="assumption">

**Assumption 2** (Joint spectral structure). For each base point, the $`A_i`$ are nonnegative self-adjoint operators whose spectral measures strongly commute. Their quadratic forms have a common dense domain. Equivalently, a realization may provide one nonnegative self-adjoint total internal operator $`A_{\rm int}`$ directly.

</div>

Under strong commutation define
``` math
P=\prod_{i=1}^3\mathbf1_{I_i}(A_i),\qquad Q=I-P,
```
for declared isolated low spectral sets $`I_i`$. The product is then an orthogonal projector independent of ordering. Base-only coefficients or separate variable names do not, by themselves, prove strong commutation.

For harmonic selection one may instead use the form sum $`A_{\rm int}=A_1+A_2+A_3`$. Nonnegativity gives
``` math
\ker A_{\rm int}=\bigcap_i\ker A_i,
```
provided the form sum is well defined. The coherent projector is then the spectral projector of $`A_{\rm int}`$ at zero.

<div id="ass:gap" class="assumption">

**Assumption 3** (Internal gap and Sobolev boundedness). There is $`\lambda_{\rm int}>0`$ such that, in quadratic-form sense,
``` math
A_{\rm int}\succeq\lambda_{\rm int}Q,
```
and $`P,Q`$ extend boundedly to every Sobolev space used by the dynamics.

</div>

The internal gap separates the selected fiber cluster from complementary fiber modes. It does not by itself imply invariance under $`R_\tau`$, existence of a fixed point, coherent contraction, suppression of arbitrarily high four-dimensional energy, or selection of a physical state.

# Stable complementary dynamics

Let $`\Psi_\ast`$ be a reference state at which the stabilization vector field is Fréchet differentiable, and set $`L=DF(\Psi_\ast)`$. The stable sign convention is that $`L_{QQ}=QLQ`$ generates decay:
``` math
\|e^{\tau L_{QQ}}\|\le M_Qe^{-\omega_Q\tau},
 \qquad M_Q\ge1,quad\omega_Q>0.
 \label{eq:q-semigroup}
```
This estimate, rather than spectral abscissa alone, is authoritative for a nonnormal generator.

<div class="proposition">

**Proposition 4** (Gap-to-decay under a bounded perturbation). *Suppose $`Q\mathcal H`$ is invariant and
``` math
L_{QQ}=-\kappa A_{\rm int}|_{Q\mathcal H}+B_Q,
 \qquad \kappa>0,quad B_Q\in\mathcal B(Q\mathcal H).
```
If $`\omega_Q:=\kappa\lambda_{\rm int}-\|B_Q\|>0`$, then
``` math
\|e^{\tau L_{QQ}}\|\le e^{-\omega_Q\tau}.
```*

</div>

<div class="proof">

*Proof.* The self-adjoint semigroup generated by $`-\kappa A_{\rm int}|_{Q\mathcal H}`$ has norm at most $`e^{-\kappa\lambda_{\rm int}\tau}`$. The bounded perturbation estimate gives the additional factor $`e^{\|B_Q\|\tau}`$. ◻

</div>

For a general sectorial or nonnormal $`L_{QQ}`$, the constants $`M_Q`$ and $`\omega_Q`$ must be proved directly. A positive vertical operator cannot be identified with the stabilization generator without the minus sign and the lower-order terms.

# Independent logical gates

The following gates are independent and must not be collapsed:

Gap.  
Spectral separation for $`A_{\rm int}`$.

Projector stability.  
Persistence and regularity of $`P`$ under parameter or curvature variation.

Invariance.  
$`R_\tau(P\mathcal H)\subseteq P\mathcal H`$, equivalently $`QF(Pu)=0`$ in a differentiable autonomous realization.

Existence.  
A fixed-point theorem applies on a declared invariant domain.

Equilibrium identification.  
A projected time-step fixed point is shown to be stationary.

Contraction.  
The coherent reduced map is strictly contractive.

Truncation.  
The influence of $`Q`$ on $`P`$ is quantitatively bounded.

Selection.  
A continuation or reset rule is supplied at admissibility exit.

No gate in this list follows solely from the gate preceding it.

# Projected fixed points and equilibria

Let $`K\subset P\mathcal H`$ be nonempty, closed, bounded, and convex and define
``` math
T_\tau=P R_\tau|_K.
```

<div id="thm:existence" class="theorem">

**Theorem 5** (Projected time-step existence). *Assume $`T_\tau(K)\subset K`$ and either:*

1.  *$`T_\tau:K\to K`$ is continuous and compact; or*

2.  *$`T_\tau`$ is continuous and condensing for a declared measure of noncompactness.*

*Then there is $`u_\ast\in K`$ with $`T_\tau u_\ast=u_\ast`$.*

</div>

<div class="proof">

*Proof.* Apply Schauder in the first case and Darbo–Sadovskii in the second. ◻

</div>

The conclusion is a *projected time-step fixed point*. It is not named an equilibrium merely because $`P R_\tau u_\ast=u_\ast`$.

<div id="thm:promotion" class="theorem">

**Theorem 6** (Strict-Lyapunov equilibrium promotion). *Suppose $`P\mathcal H`$ is invariant, so that $`P R_\tau u_\ast=R_\tau u_\ast=u_\ast`$, and along the orbit
``` math
\mathcal C(R_\tau u)-\mathcal C(u)
 =-\int_0^\tau\mathcal D(R_su)\,ds,
 \qquad\mathcal D\ge0,
```
where $`\mathcal D(v)=0`$ exactly when $`F(v)=0`$. Then the fixed point from Theorem <a href="#thm:existence" data-reference-type="ref" data-reference="thm:existence">5</a> is an equilibrium.*

</div>

<div class="proof">

*Proof.* Endpoint recurrence makes the left side zero. Nonnegativity and continuity force $`\mathcal D=0`$ along the orbit; strictness gives $`F(u_\ast)=0`$. ◻

</div>

<div id="thm:banach" class="theorem">

**Theorem 7** (Banach gate). *If $`K`$ is complete, $`T_\tau(K)\subset K`$, and
``` math
\|T_\tau u-T_\tau v\|\le q\|u-v\|,
 \qquad0\le q<1,
```
then $`T_\tau`$ has a unique fixed point in $`K`$, and its iterates converge to that point. The theorem does not apply without the invariant complete domain.*

</div>

# Schur–Feshbach reduction with domains

Let $`\mathcal H=P\mathcal H\oplus Q\mathcal H`$. Consider a closed block operator
``` math
L=\begin{pmatrix}L_{PP}&L_{PQ}\\L_{QP}&L_{QQ}\end{pmatrix}
```
with domain $`P\mathcal H\oplus\mathcal D(L_{QQ})`$. Assume:

1.  $`0\in\rho(L_{QQ})`$ and $`L_{QQ}^{-1}:Q\mathcal H\to\mathcal D(L_{QQ})`$ is bounded in the graph norm;

2.  $`L_{PP}`$ and $`L_{QP}:P\mathcal H\to Q\mathcal H`$ are bounded; and

3.  $`L_{PQ}:\mathcal D(L_{QQ})\to P\mathcal H`$ is graph-norm bounded, so $`L_{PQ}L_{QQ}^{-1}`$ is bounded.

<div id="thm:feshbach" class="theorem">

**Theorem 8** (Schur–Feshbach equation). *Under these hypotheses, solving $`L(p,q)=(f_P,f_Q)`$ is equivalent to
``` math
S p=f_P-L_{PQ}L_{QQ}^{-1}f_Q,
 \qquad
 q=L_{QQ}^{-1}(f_Q-L_{QP}p),
```
where
``` math
S=L_{PP}-L_{PQ}L_{QQ}^{-1}L_{QP}.
```
If $`\|L_{QQ}^{-1}\|\le C_Q/\omega_Q`$, then
``` math
\|S-L_{PP}\|
 \le\|L_{PQ}L_{QQ}^{-1}\|\,\|L_{QP}\|
 \le\frac{C_Q\|L_{PQ}\|_{\rm gr}\|L_{QP}\|}{\omega_Q}.
```*

</div>

<div class="proof">

*Proof.* The $`Q`$ block equation gives the displayed formula for $`q`$. Substitution in the $`P`$ block equation gives $`S`$. The bound follows from the declared graph norm and inverse estimates. ◻

</div>

This is a local linear reduction near the reference state. Nonlinear truncation additionally requires control of nonlinear remainders and of the time interval on which the eliminated sector remains small.

# Projector stability and basin-local robustness

<div class="proposition">

**Proposition 9** (Riesz-projector stability). *Let $`A(\epsilon)`$ be a norm-resolvent-continuous family and let a contour $`\Gamma`$ remain in the resolvent set while enclosing one isolated cluster. Then
``` math
P(\epsilon)=\frac{1}{2\pi i}\oint_\Gamma(z-A(\epsilon))^{-1}\,dz
```
is norm continuous and has constant finite rank. This proves projector stability, not dynamical stability of a fixed point.*

</div>

<div id="thm:robust" class="theorem">

**Theorem 10** (Basin-local fixed-point robustness). *Let $`T,\widetilde T:K\to K`$ be contractions on the same complete invariant domain with contraction constant at most $`q<1`$. If
``` math
\sup_{u\in K}\|T(u)-\widetilde T(u)\|\le\varepsilon,
```
then their fixed points satisfy
``` math
\|u_\ast-\widetilde u_\ast\|\le\frac{\varepsilon}{1-q}.
```*

</div>

<div class="proof">

*Proof.* Insert and subtract $`T(\widetilde u_\ast)`$ and absorb the resulting $`q\|u_\ast-\widetilde u_\ast\|`$ term. ◻

</div>

This is the justified foundation for a local robustness or universality claim. It is not global universality across arbitrary microscopic models.

# Projection, descent, and recovery types

Let $`r:X\to Y_{\rm eff}`$ be a surjective reduction map on a microscopic state space $`X`$, and let $`\Phi:X\to X`$ be a microscopic step.

<div id="thm:descent" class="theorem">

**Theorem 11** (Autonomous descent criterion). *There exists a unique reduced map $`\overline\Phi:Y_{\rm eff}\to Y_{\rm eff}`$ satisfying
``` math
\overline\Phi\circ r=r\circ\Phi
```
if and only if
``` math
r(x)=r(x')\quad\Longrightarrow\quad r(\Phi x)=r(\Phi x').
```*

</div>

<div class="proof">

*Proof.* Necessity follows by applying $`\overline\Phi`$. For sufficiency define $`\overline\Phi(r(x))=r(\Phi x)`$; the implication makes this independent of the representative, and surjectivity gives uniqueness. ◻

</div>

A section $`s:Y_{\rm eff}\to X`$ obeys $`r\circ s=\operatorname{id}`$ and chooses one representative. It does not recover every microscopic state. Exact microscopic recovery would require $`s\circ r=\operatorname{id}_X`$, which is possible only when $`r`$ is injective. An effective merger combines reduced descriptions and is neither kind of inverse unless separately typed and proved.

If $`r`$ is fiberwise over the base and the microscopic generator is local in base variables, a reduced local generator may descend when the invariance criterion holds and all coefficients depend locally and smoothly on the base jet. A projection nonlocal in base variables does not inherit locality merely from being a projector.

# Admissibility and hybrid selection

Let $`m_j(u)`$ be declared continuous margins and define
``` math
\mathcal A_\varepsilon
 =\{u:m_j(u)\ge\varepsilon\text{ for all }j\},
 \qquad
 \mathfrak B(u)=\max_j[-m_j(u)].
```
Then $`u\in\mathcal A_0`$ exactly when $`\mathfrak B(u)\le0`$. This is a diagnostic encoding of declared constraints, not automatically an energy or force.

At a first exit from $`\mathcal A_0`$, three logically different constructions are possible:

1.  stop the reduced description;

2.  continue the upper dynamics and derive a new reduced chart; or

3.  impose a reset $`S:\partial\mathcal A_0\to\mathcal A_0`$.

The third option defines a hybrid dynamical system. It changes the continuation law and must separately prove existence, measurability, conservation, and any probability assigned to alternative reset outcomes. Calling the reset “selection” does not make it part of the original flow.

# Complete admissibility-margin ledger

Every realization must record the following entries independently:

1.  **Geometry/domain:** base, fiber, dimensions, bundle regularity, operator domains, and boundary conditions.

2.  **Joint spectral structure:** strong commutation or a selected total operator, the spectral contour, rank, and Sobolev boundedness of $`P`$.

3.  **Internal gap:** $`\lambda_{\rm int}`$ and its uniformity domain.

4.  **Complementary stability:** $`M_Q,\omega_Q`$ and the generator sign.

5.  **Leakage/invariance:** $`QF(Pu)`$ or a quantitative leakage bound.

6.  **Existence gate:** the invariant set $`K`$ and the compact, condensing, or contraction theorem actually used.

7.  **Equilibrium gate:** stationarity equation or strict Lyapunov promotion.

8.  **Coherent contraction:** norm, basin, and factor $`q<1`$.

9.  **Truncation:** mixing blocks, inverse/domain bounds, nonlinear remainder, and error interval.

10. **Projector robustness:** perturbation topology and resolvent contour.

11. **Admissibility:** each margin $`m_j`$, its units, and its source.

12. **Continuation/selection:** stop, upper continuation, or hybrid reset, including conservation and probability data.

13. **Physical hyperbolicity:** principal symbol, constraints, causal domain, and relation between $`t`$ and $`\tau`$.

14. **Scale separation:** record the internal gap $`\lambda_{\rm int}`$, coherent contraction scale, four-dimensional cutoff, curvature scale, and RG scale $`\mu`$.

15. **Numerical provenance:** source-independent inputs, fitted inputs, branch selection, uncertainty, and held-out outputs.

No single scalar “coherence scale” may replace this ledger unless a theorem derives all identifications with dimensions and errors.

# Lorentzian physical completion

The Hilbert inner product and every Gram tensor constructed from it are positive semidefinite. They cannot acquire Lorentzian signature. In a local physical completion, causal signature is instead read from the principal symbol. For a second-order field equation this has the schematic form
``` math
\sigma_{\rm pr}(x,\xi)=g^{\mu\nu}(x)\xi_\mu\xi_\nu I+\text{gauge blocks}.
```
Lorentzian hyperbolicity, constraint propagation, and a domain-of-dependence theorem must be verified for the selected equations. The canonical base dimension $`3+1`$ is part of the canonical FP physical realization; it is not derived by the abstract Hilbert-bundle theory. In particular, the component identity $`1+3\times3=4+6`$ neither selects a four-dimensional causal base nor determines its signature.

# Foundation synthesis theorem

<div id="thm:foundation" class="theorem">

**Theorem 12** (Scoped MTT foundation). *Assume the dimension-neutral Hilbert-bundle architecture, joint spectral structure, internal gap, stable complementary semigroup, and the separately listed hypotheses for a chosen fixed-point theorem. Then the model possesses a bounded coherent decomposition and a projected time-step fixed point. Under strict Lyapunov and invariance hypotheses that point is an equilibrium. Under the Banach gate it is unique in the declared basin. Under the Schur–Feshbach hypotheses the local linear complementary sector can be eliminated with the displayed error bound. Under contraction and map-closeness hypotheses the fixed point is basin-locally robust. Autonomous reduced dynamics exists exactly under the descent criterion.*

</div>

None of these conclusions supplies a physical probability law, Lorentzian field equation, quantum representation, particle spectrum, Standard Model matching, cosmology, or numerical prediction. Those are downstream obligations governed by the admissibility ledger. Nor does equality of the local $`1+2+3`$ strain dimensions and the q79 $`1+2+3`$ trace-split ranks prove the same-source intertwiner needed to identify their metrics, connections, and vertical operators. Theorem <a href="#thm:shared-line" data-reference-type="ref" data-reference="thm:shared-line">1</a> closes the common flat line and finite Hessian square inside the q79 carrier; it does not close that local-to-continuum identification.

# Conclusion

The corrected Foundation provides a typed and noncircular spine for the MTT corpus. It identifies what the triplet and projector mean, how complementary stability is proved, which fixed-point conclusion is available, how reduction is typed, and where physical assumptions enter. Its value is precisely this separation: later realizations can now be tested against explicit gates rather than inheriting conclusions from an undifferentiated appeal to coherence. The shared-circle sector now illustrates the intended discipline particularly well: a curved Boothby–Wang schema, an exact flat q79 differential line, and a conditional polarized Hilbert readout coexist without being conflated.

<div class="thebibliography">

99

P. Nero, *Fixed Points I–VI*, corrected theorem spine, revised editions, 2026.

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

K.-J. Engel and R. Nagel, *One-Parameter Semigroups for Linear Evolution Equations*, Springer, 2000.

K. Deimling, *Nonlinear Functional Analysis*, Springer, 1985.

W. M. Boothby and H. C. Wang, On contact manifolds, *Annals of Mathematics* 68 (1958), 721–734.

R. Casals, D. M. Pancholi, and F. Presas, Contact blow-up, *Expositiones Mathematicae* 33 (2015), 97–123.

N. M. J. Woodhouse, *Geometric Quantization*, second edition, Oxford University Press, 1992.

P. Nero, *q79 Universal Shared Differential Line and Finite-Operator Intertwiner*, executable theorem packet, 2026.

</div>
