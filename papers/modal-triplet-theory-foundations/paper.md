---
abstract: |
  We give a corrected functional-analytic foundation for Modal Triplet Theory (MTT). The abstract architecture is a Hilbert bundle with three compatible vertical structures, a joint coherent spectral projector, a stabilization flow, and explicitly separate hypotheses for gap, invariance, existence, contraction, truncation, and admissibility. The canonical physical realization is a ten-dimensional bundle $`M_{10}\to Y_4`$ with compact Riemannian fiber $`X_6`$; the central circle is bundle data and is not counted as an additional product dimension. Strong commutation or a single total internal operator is assumed rather than inferred from notation. Complementary-mode stability uses a stable-semigroup estimate that remains valid for nonnormal generators. Projected time-step fixed points are distinguished from equilibria, and Banach, Schur–Feshbach, projector-stability, and basin-robustness statements are given with their required domains. Stabilization time, physical time, and renormalization scale are separated. Selection by reset is identified as a hybrid law unless derived from continuous upper dynamics. Lorentzian signature belongs to a hyperbolic principal symbol in a physical completion, not to a positive Hilbert-space Gram form. A complete admissibility ledger records the independent obligations inherited by every downstream MTT realization. A rank-three world-in-world comparison field and the selected q79 trace-split carrier are included as a typed geometry interface: their matching component counts do not by themselves derive a ten-dimensional manifold, Lorentzian spacetime, or a global intertwiner.
author:
- Peter Nero
current_version: v7
date: July 2026
generated_from_main_tex_sha256: 7b7ea991bf6a669385b4cec959641f79c9088b76d1444b581b7aef230f7ab3ab
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
*Modal Triplet Theory: Foundation*, version 6.

Reason.  
The previous foundation did not keep joint spectral compatibility, semigroup stability, fixed-point type, reduction domains, physical time, signature, and internal geometry as independent hypotheses.

Resolution.  
Version 7 rebuilds the functional-analytic spine, corrects the fixed-point and Schur–Feshbach gates, separates all scales and evolution parameters, and adds the typed world-in-world/q79 geometry interface.

Retained result.  
The coherent-projector and basin-local fixed-point architecture survives as a conditional control-and-reduction framework.

Remaining boundary.  
Physical field equations, probability, particle content, numerical selection, and the same-source strain-to-q79 intertwiner remain downstream obligations.

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

Let $`Y`$ be a smooth base and let $`\mathscr H\to Y`$ be a real or complex separable Hilbert bundle. A state belongs to a declared Sobolev space
``` math
\mathcal H=H^s(Y;\mathscr H),
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

**Assumption 1** (Joint spectral structure). For each base point, the $`A_i`$ are nonnegative self-adjoint operators whose spectral measures strongly commute. Their quadratic forms have a common dense domain. Equivalently, a realization may provide one nonnegative self-adjoint total internal operator $`A_{\rm int}`$ directly.

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

**Assumption 2** (Internal gap and Sobolev boundedness). There is $`\lambda_{\rm int}>0`$ such that, in quadratic-form sense,
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

**Proposition 3** (Gap-to-decay under a bounded perturbation). *Suppose $`Q\mathcal H`$ is invariant and
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

**Theorem 4** (Projected time-step existence). *Assume $`T_\tau(K)\subset K`$ and either:*

1.  *$`T_\tau:K\to K`$ is continuous and compact; or*

2.  *$`T_\tau`$ is continuous and condensing for a declared measure of noncompactness.*

*Then there is $`u_\ast\in K`$ with $`T_\tau u_\ast=u_\ast`$.*

</div>

<div class="proof">

*Proof.* Apply Schauder in the first case and Darbo–Sadovskii in the second. ◻

</div>

The conclusion is a *projected time-step fixed point*. It is not named an equilibrium merely because $`P R_\tau u_\ast=u_\ast`$.

<div id="thm:promotion" class="theorem">

**Theorem 5** (Strict-Lyapunov equilibrium promotion). *Suppose $`P\mathcal H`$ is invariant, so that $`P R_\tau u_\ast=R_\tau u_\ast=u_\ast`$, and along the orbit
``` math
\mathcal C(R_\tau u)-\mathcal C(u)
 =-\int_0^\tau\mathcal D(R_su)\,ds,
 \qquad\mathcal D\ge0,
```
where $`\mathcal D(v)=0`$ exactly when $`F(v)=0`$. Then the fixed point from Theorem <a href="#thm:existence" data-reference-type="ref" data-reference="thm:existence">4</a> is an equilibrium.*

</div>

<div class="proof">

*Proof.* Endpoint recurrence makes the left side zero. Nonnegativity and continuity force $`\mathcal D=0`$ along the orbit; strictness gives $`F(u_\ast)=0`$. ◻

</div>

<div id="thm:banach" class="theorem">

**Theorem 6** (Banach gate). *If $`K`$ is complete, $`T_\tau(K)\subset K`$, and
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

**Theorem 7** (Schur–Feshbach equation). *Under these hypotheses, solving $`L(p,q)=(f_P,f_Q)`$ is equivalent to
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

**Proposition 8** (Riesz-projector stability). *Let $`A(\epsilon)`$ be a norm-resolvent-continuous family and let a contour $`\Gamma`$ remain in the resolvent set while enclosing one isolated cluster. Then
``` math
P(\epsilon)=\frac{1}{2\pi i}\oint_\Gamma(z-A(\epsilon))^{-1}\,dz
```
is norm continuous and has constant finite rank. This proves projector stability, not dynamical stability of a fixed point.*

</div>

<div id="thm:robust" class="theorem">

**Theorem 9** (Basin-local fixed-point robustness). *Let $`T,\widetilde T:K\to K`$ be contractions on the same complete invariant domain with contraction constant at most $`q<1`$. If
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

**Theorem 10** (Autonomous descent criterion). *There exists a unique reduced map $`\overline\Phi:Y_{\rm eff}\to Y_{\rm eff}`$ satisfying
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

14. **Scale separation:** internal gap $`\lambda_{\rm int}`$, coherent contraction scale, external four-dimensional cutoff $`\Lambda_{4D}`$, curvature scale, and RG scale $`\mu`$.

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

**Theorem 11** (Scoped MTT foundation). *Assume the dimension-neutral Hilbert-bundle architecture, joint spectral structure, internal gap, stable complementary semigroup, and the separately listed hypotheses for a chosen fixed-point theorem. Then the model possesses a bounded coherent decomposition and a projected time-step fixed point. Under strict Lyapunov and invariance hypotheses that point is an equilibrium. Under the Banach gate it is unique in the declared basin. Under the Schur–Feshbach hypotheses the local linear complementary sector can be eliminated with the displayed error bound. Under contraction and map-closeness hypotheses the fixed point is basin-locally robust. Autonomous reduced dynamics exists exactly under the descent criterion.*

</div>

None of these conclusions supplies a physical probability law, Lorentzian field equation, quantum representation, particle spectrum, Standard Model matching, cosmology, or numerical prediction. Those are downstream obligations governed by the admissibility ledger. Nor does equality of the local $`1+2+3`$ strain dimensions and the q79 $`1+2+3`$ trace-split ranks prove the same-source intertwiner needed to identify their metrics, connections, and vertical operators.

# Conclusion

The corrected Foundation provides a typed and noncircular spine for the MTT corpus. It identifies what the triplet and projector mean, how complementary stability is proved, which fixed-point conclusion is available, how reduction is typed, and where physical assumptions enter. Its value is precisely this separation: later realizations can now be tested against explicit gates rather than inheriting conclusions from an undifferentiated appeal to coherence.

<div class="thebibliography">

99

P. Nero, *Fixed Points I–VI*, corrected theorem spine, revised editions, 2026.

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

K.-J. Engel and R. Nagel, *One-Parameter Semigroups for Linear Evolution Equations*, Springer, 2000.

K. Deimling, *Nonlinear Functional Analysis*, Springer, 1985.

</div>
