---
abstract: |
  We develop curvature coupling and structural transitions on the canonical FP–I–III spine. A Laplace-type operator is normalized as $`L=\nabla^\ast\nabla+\mathcal R`$. Curvature can shift the spectral cluster, mix coherent and noncoherent sectors, and create a leakage floor. If $`\|\mathcal R\|<\lambda_\ast/2`$, the full curved operator retains a separated low cluster and defines a new Riesz projector; if one retains the unperturbed projector, the term $`Q\mathcal RP`$ must appear explicitly. Centroids are defined intrinsically by a Karcher mean inside a convex normal ball. A first-order gradient parent flow yields a first-order modulation law; a Newtonian law requires a separately specified inertial parent equation. Absolute interaction bounds give $`|E_{\rm int}|\le C\mathcal O`$, while attraction or repulsion needs a sign hypothesis. Structural transitions are controlled by a Lyapunov mountain- pass/work theorem, and exit detection is separated from selection of the post-transition basin. We also state the exact projective-module transport and finite-reduction boundary: a supplied connection and its Hessian transport naturally, bare compression is exact only on an invariant subspace, and otherwise the Feshbach or reduced-Green operator is required.
author:
- Peter Nero
current_version: v7
date: September 2026 Version 7
generated_from_main_tex_sha256: 208df8b55e21a91c5e19043af446fb01a5de4a05509f7cab7473c43c873c9b30
paper_id: fixed-points-iv-curvature-centroid-motion-and-structura-47f7cbce
release_state: current_revised_tex
released_version: v6
title: "Fixed Points IV: Curvature, Centroid Motion, and Structural Transitions"
zenodo_doi: 10.5281/zenodo.21655378
zenodo_record_id: 21655378
zenodo_url: "https://zenodo.org/records/21655378"
---

# Revision note for version 7

Supersedes.
Version 6, retained as the released edition.

Reason.
The finite-representation discussion imported a later MTT research source into a foundational paper.

Resolution.
Universal connections are attributed to their standard mathematical source. Transport is derived on the image module, and local proofs of block elimination and constrained minimization replace reliance on research packets. Application-specific compiler and status claims are removed.

Retained result.
Curved clusters, leakage, finite reduction, centroid modulation and transition criteria retain their analytic roles. The reduction statements now specify the operator domains and coercivity they use.

Remaining boundary.
Each application must supply the bundle, connection, energy, finite subspace and dynamical interpretation.

# Revision note for version 6

Supersedes.
*Fixed Points IV: Curvature, Centroid Motion, and Structural Transitions*, version 5.

Reason.
Version 5 states the corrected curvature and finite-reduction theorems, but it did not sufficiently explain the difference between a finite projective module, a finite Galerkin truncation, and an exact invariant reduction.

Resolution.
Version 6 adds a three-way finite-data guide, separates diagonal curvature shifts from off-diagonal leakage, and gives a clearer route from curved spectral clusters to centroid and transition statements. The theorem statements and their canonical ownership are unchanged.

Retained result.
Curved-cluster persistence, leakage bounds, intrinsic first-order modulation, barrier exclusion, and the Feshbach/reduced-Green boundary remain as in version 5.

Remaining boundary.
The physical HYM source, continuum Hessian, selected finite subspace, inertial parent law, interaction sign, and post-transition selection remain open.

# Revision note for version 5

Supersedes.
*Fixed Points IV: Curvature, Centroid Motion, and Structural Transitions*, version 4.

Reason.
Version 4 corrected curvature leakage and transition claims but did not state when a curved continuum Hessian is represented exactly by finite projective-module data or when a compressed matrix is the physical effective operator.

Resolution.
Version 5 retains the curved Riesz-projector analysis and adds exact connection/Hessian transport, the invariant-subspace versus Feshbach–Schur criterion, and the reduced-Green shorted Hessian for nonlinear strain coordinates. It also distinguishes a finite matrix-valued smooth projector from a Fourier or Galerkin truncation.

Retained result.
Curved-cluster persistence, leakage bounds, intrinsic first-order modulation, and barrier exclusion survive conditionally.

Remaining boundary.
The selected q79 HYM endpoints, action, physical Hessian and finite subspace remain open, as do attraction, inertia, and post-transition selection without a specified physical parent law.

# How to read this paper

The earlier Fixed Points papers use a coherent projector defined by an unperturbed vertical operator. FP–IV asks what remains true when curvature changes that operator and when one tries to represent the resulting continuum problem by finite data. The paper also follows localized solutions through centroid motion, interaction, and possible exit from one admissible basin.

#### The central picture in plain language.

Curvature has two effects that must not be collapsed into one number. Its diagonal $`Q\mathcal RQ`$ block changes damping inside the old noncoherent sector, while its off-diagonal $`Q\mathcal RP`$ block pushes an old coherent state out of that sector. One can either keep the old projector and account for this leakage, or prove that the full curved operator has a separated low cluster and use its rotated projector $`P_{\mathcal R}`$.

#### Three meanings of finite.

A finite-rank vector bundle can be embedded exactly into a finite matrix algebra whose entries are still smooth functions. That is not the same as retaining finitely many Fourier or Galerkin modes. A finite Galerkin compression is, in turn, an exact dynamical reduction only when the selected subspace is invariant. Otherwise the omitted fields return through the Feshbach self-energy. Keeping these three statements separate is essential for deciding what a finite calculation can represent.

#### Argument map.

Sections 1–3 define the curved operator, prove persistence of a low spectral cluster, and distinguish the old from the curved coherent projector. Section 4 then states exact projective transport and the two correct effective operators: Feshbach reduction for a linear finite subspace and reduced-Green shorting for nonlinear strain coordinates. Section 5 quantifies leakage when the old projector is retained. Sections 6–8 discuss intrinsic centroid motion and signed interactions. Sections 9–10 return to fixed-point existence and separate energy-barrier exclusion, exit detection, and post-exit selection.

#### Scope boundary.

These are universal operator and control statements. They do not supply the physical bundle, energy-derived Hessian, invariant finite subspace, inertial parent dynamics, interaction sign, or basin-selection law. A physical application must provide those inputs before invoking the corresponding theorem.

# Inherited control framework

We use the FP–I/II Riemannian control geometry , joint internal operators, and projected stabilization flow. The projector $`P`$ below is the unperturbed joint harmonic projector and $`Q=I-P`$. FP–III supplies separate deterministic and stochastic disturbance bounds. No statement here identifies the stabilization parameter with physical Lorentzian time.

Existence of a projected step fixed point requires the corrected invariant-set conditions and the stated Schauder or Darbo hypotheses. Promotion to a full equilibrium uses the strict Lyapunov identity of FP–II.

# Curved Laplace-type operator

Let $`E\to B`$ be a Hermitian bundle with compatible connection $`\nabla`$. A Laplace-type operator is written
``` math
\begin{equation}
L=\nabla^\ast\nabla+\mathcal R,
\label{eq:weitzenbock}
\end{equation}
```
where $`\nabla^\ast\nabla\ge0`$ is the rough/connection Laplacian and $`\mathcal R=\mathcal R^\ast`$ is the curvature endomorphism. We identify the unperturbed vertical operator with $`A_0=\nabla^\ast\nabla`$ in the selected sector and assume
``` math
\operatorname{spec}(A_0)\subset\{0\}\cup[\lambda_\ast,\infty),
\qquad \lambda_\ast>0.
```

Relative to $`P\oplus Q`$, curvature has four blocks
``` math
\mathcal R=
\begin{pmatrix}
P\mathcal RP&P\mathcal RQ\\
Q\mathcal RP&Q\mathcal RQ
\end{pmatrix}.
```
Define the noncoherent negative-part and leakage bounds
``` math
\begin{align}
\operatorname{Re}\langle q,Q\mathcal RQq\rangle
&\ge-\rho_Q\|q\|^2,\\
\ell_{QP}&:=\|Q\mathcal RP\|.
\end{align}
```
The scalar lower bound $`\rho_Q`$ does not control the off-diagonal block $`Q\mathcal RP`$.

# Gap persistence and the curved projector

<div id="thm:gap" class="theorem">

**Theorem 1** (Bounded-curvature cluster persistence). *Assume $`\mathcal R`$ is bounded and self-adjoint with $`r:=\|\mathcal R\|<\lambda_\ast/2`$. Then the spectrum of $`L=A_0+\mathcal R`$ lies in the $`r`$-neighborhood of $`\operatorname{spec}(A_0)`$. The low cluster and the remaining spectrum are separated by at least
``` math
\lambda_{\rm gap}^{\mathcal R}\ge\lambda_\ast-2r>0.
```
A contour in this separation defines the full curved Riesz projector
``` math
P_{\mathcal R}=\frac{1}{2\pi i}\int_\Gamma(z-L)^{-1}\,dz,
```
which has the same finite rank as $`P`$ along the norm-continuous perturbation $`A_0+s\mathcal R`$, $`0\le s\le1`$.*

</div>

#### What cluster persistence changes.

The theorem does not say that curvature leaves the old harmonic states fixed. It says that a low-dimensional spectral cluster survives and can be followed continuously. Its range may rotate inside the full Hilbert space. Therefore $`P_{\mathcal R}`$ is the natural exact coherent projector for the curved operator, whereas retaining $`P`$ is an approximation whose leakage must be measured.

Using $`P_{\mathcal R}`$ eliminates linear leakage because $`[L,P_{\mathcal R}]=0`$, but changes the coherent subspace. If the bounded- perturbation condition is unavailable, gap persistence and the Riesz projector must be proved directly for the full curved operator; the unperturbed gap may not simply be reused.

For base-dependent curvature and projectors, modulation and locality estimates also require bounds on $`\nabla\mathcal R`$, $`\nabla P_{\mathcal R}`$, and any commutator with the base control operator. These gradient terms are not contained in the scalar loss $`\rho_Q`$.

# Exact projective transport and finite reduction

This section answers two different representation questions. First, can a supplied bundle and connection be represented exactly by finite matrix-valued functions? Second, can an infinite-dimensional Hessian be replaced by a finite operator without losing the effect of discarded modes? The universal connection answers the first. Invariance or Feshbach–Schur reduction answers the second.

The curved spectral projector above should not be confused with a finite projective-module presentation of a supplied bundle. Let $`X`$ be compact and let $`(E,h,\nabla)`$ be a supplied finite-rank Hermitian bundle with unitary connection. The universal-connection theorem of Narasimhan and Ramanan gives a finite $`N`$, a fiberwise isometry
``` math
U:E\longrightarrow X\times\mathbb C^N,
\qquad p_{\rm mod}=UU^\ast\in M_N(C^\infty(X)),
```
such that
``` math
p_{\rm mod}\,d(Us)=U\nabla s,
\qquad
p_{\rm mod}(dp_{\rm mod})\wedge(dp_{\rm mod})p_{\rm mod}
=UF_\nabla U^\ast.
```
These identities concern the image bundle $`p_{\rm mod}\mathbb C^N`$, not the entire trivial bundle. On its sections define $`\nabla'=U\nabla U^\ast`$. Then $`(\nabla')^2=UF_\nabla U^\ast`$ by composition. The induced map on $`L^2`$ sections is unitary onto its image when both spaces use the same base measure. It therefore transports adjoints and closed quadratic forms, with their domains. In particular, if a twice differentiable energy is transported by $`C'(v)=C(U^\ast v)`$ on that image, then
``` math
d^2C'(Uu)[U\xi,U\eta]=d^2C(u)[\xi,\eta].
```
The corresponding Hessian is $`H'=UHU^\ast`$ on the transported domain. Any gauge slice must also be transported, not chosen independently. No claim is made about an extension of $`H'`$ outside the image module. This preserves the supplied curvature; it does not flatten the connection.

Here “finite” refers only to the ambient matrix size $`N`$. The entries of $`p_{\rm mod}(x)`$ are smooth functions and can contain infinitely many base modes. Thus $`p_{\rm mod}`$ is not, by itself, a finite Fourier, Toeplitz, or Galerkin cutoff. An arbitrary smooth embedding of the same bundle need not represent the supplied connection by $`p_{\rm mod}d`$. In such a presentation, the difference between the transported connection and $`p_{\rm mod}d`$ is an endomorphism-valued one-form and must be retained. A bundle projector alone does not determine a previously specified connection.

<div id="thm:finite-reduction" class="theorem">

**Theorem 2** (Exact finite-reduction criterion). *Let $`H=H^\ast`$ be a densely defined Hessian on a Hilbert space, let $`P_f`$ be a finite-rank orthogonal projector with $`\operatorname{Ran}P_f\subset D(H)`$, and put $`Q_f=I-P_f`$. Use the domain decomposition $`D(H)=\operatorname{Ran}P_f\oplus(D(H)\cap\operatorname{Ran}Q_f)`$. Then the bare compression $`P_fHP_f`$ is the exact restriction of $`H`$ to $`\operatorname{Ran}P_f`$ if and only if
``` math
Q_fHP_f=0.
```
If this residual is nonzero and the complementary block $`Q_f(H-z)Q_f`$ has a bounded inverse into its operator domain, the exact finite operator at spectral parameter $`z`$ is the Feshbach–Schur map
``` math
F_{P_f}(H-z)
=P_f(H-z)P_f
-P_fHQ_f\,[Q_f(H-z)Q_f]^{-1}Q_fHP_f.
```
The second term is determined by the same Hessian, not an independent fit parameter. This map is an exact reduced spectral equation; a spectral-parameter-dependent map is not automatically an autonomous evolution generator on the finite subspace.*

</div>

<div class="proof">

*Proof.* For $`u\in\operatorname{Ran}P_f`$, the decomposition $`Hu=P_fHu+Q_fHu`$ shows that invariance is equivalent to $`Q_fHP_f=0`$. Self-adjointness then gives a reducing decomposition on the stated domain. For the general case write a vector as $`u+v`$ in the two summands. The $`Q_f`$ row of $`(H-z)(u+v)=0`$ is
``` math
Q_fHP_fu+Q_f(H-z)Q_fv=0.
```
Its unique solution is $`v=-[Q_f(H-z)Q_f]^{-1}Q_fHP_fu`$. Substitution into the $`P_f`$ row gives $`F_{P_f}(H-z)u=0`$, and the substitution also reconstructs every full solution. The domain assumptions make all displayed products well defined. ◻

</div>

<div id="thm:shorted-hessian" class="theorem">

**Theorem 3** (Reduced-Green strain Hessian). *Let $`H_Q\ge cI`$, $`c>0`$, be a self-adjoint Hessian on the retained Hilbert space after removal of its declared kernel, let $`G_Q=H_Q^{-1}`$, and let $`J=d\Phi_{\rm strain}`$ be a bounded surjection from that Hilbert space to a finite-dimensional target at the point in question. If $`JG_QJ^\ast>0`$, then the exact effective Hessian on strain variations is
``` math
H_{\rm strain}=(JG_QJ^\ast)^{-1}.
```
Indeed, for every target variation $`y`$,
``` math
\min_{\substack{x\in D(H_Q^{1/2})\\Jx=y}}
\frac12\|H_Q^{1/2}x\|^2
=\frac12\langle y,(JG_QJ^\ast)^{-1}y\rangle.
```
Thus the effective operator minimizes over the directions forgotten by $`J`$. It is the Hessian of the tangent quadratic minimization problem, not a claim about the complete nonlinear energy away from the reference point. It is a quotient or shorted Hessian, not a bare restriction to a selected subspace.*

</div>

<div class="proof">

*Proof.* Put $`B=JG_QJ^\ast`$ and $`x_\ast=G_QJ^\ast B^{-1}y`$. Then $`x_\ast\in D(H_Q)`$ and $`Jx_\ast=y`$. Every admissible $`x`$ has the form $`x_\ast+z`$ with $`Jz=0`$. In the quadratic form,
``` math
\langle H_Qx_\ast,z\rangle
=\langle J^\ast B^{-1}y,z\rangle=0.
```
Consequently its energy is the energy of $`x_\ast`$ plus $`\frac12\|H_Q^{1/2}z\|^2`$. The latter is nonnegative and vanishes only for $`z=0`$. Substituting $`x_\ast`$ gives the asserted minimum and uniqueness. ◻

</div>

These are operator identities for supplied data. To apply them, construct the Hessian and its domain, verify the regularity and coercivity required by the chosen reduction, and evaluate either the invariance residual or the complementary inverse. No physical model is selected by these identities.

#### Interpretation of the two effective operators.

The Feshbach map keeps a chosen linear subspace and feeds back propagation through its orthogonal complement. The reduced-Green formula instead asks for the least quadratic energy needed to realize a prescribed tangent strain variation. Both integrate out omitted directions from the same source Hessian. Neither licenses inserting an independently fitted finite matrix, and neither determines which subspace or quotient an application realizes.

#### A two-dimensional check.

For $`H=\left(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\right)`$ and $`J(x_1,x_2)=x_1`$, bare compression gives $`2`$. Eliminating $`x_2`$ gives $`2-1/3=5/3`$. Since $`(H^{-1})_{11}=3/5`$, the constrained formula also gives $`(JH^{-1}J^\ast)^{-1}=5/3`$. Thus both derivations agree, while simple compression misses the adjustment in the discarded variable.

# Curvature leakage and stability floor

Consider
``` math
\partial_t\Psi=-(A_0+\mathcal R)\Psi-N(\Psi)+F,
\qquad p=P\Psi,\quad q=Q\Psi.
```
Assume unperturbed coherence invariance $`QN(p)=0`$ and the one-sided estimate
``` math
\operatorname{Re}\langle q,Q(N(p+q)-N(p))\rangle
\ge-L_Q\|q\|^2.
```

<div id="thm:leakage" class="theorem">

**Theorem 4** (Noncoherent leakage bound). *Let
``` math
\gamma_Q:=\lambda_\ast-L_Q-\rho_Q>0.
```
Then
``` math
\begin{equation}
D^+\|q(t)\|
\le-\gamma_Q\|q(t)\|+\ell_{QP}\|p(t)\|+\|QF(t)\|.
\label{eq:leakage-dini}
\end{equation}
```
Consequently,
``` math
\begin{align}
\|q(t)\|
&\le e^{-\gamma_Qt}\|q(0)\|\\
&\quad+\int_0^t e^{-\gamma_Q(t-s)}
\bigl(\ell_{QP}\|p(s)\|+\|QF(s)\|\bigr)\,ds.
\end{align}
```
If $`p`$ and $`QF`$ are uniformly bounded, then
``` math
\limsup_{t\to\infty}\|q(t)\|
\le\frac{\ell_{QP}\sup_t\|p(t)\|+\sup_t\|QF(t)\|}{\gamma_Q}.
```*

</div>

Thus positive damping need not drive the old $`Q`$ component to zero. Exact decay to the old coherent sector requires $`Q\mathcal RP=0`$ and vanishing noncoherent forcing, or replacement of $`P`$ by a verified curved projector.

#### What the leakage floor means.

Even with $`\gamma_Q>0`$, a persistent coherent profile can continually source the old $`Q`$ sector through curvature. The resulting nonzero floor is not an instability; it records that the old coherent/noncoherent split is no longer aligned with the curved operator. Recomputing the projector can remove this linear leakage, but only after cluster persistence for the full operator has been proved.

# Intrinsic centroid and modulation

Once a localized profile is available, its location must be defined without averaging coordinates from unrelated charts. The Karcher mean gives an intrinsic centroid inside a convex normal ball. Projecting a first-order gradient flow onto the tangent directions of the profile manifold then yields a first-order law for that centroid; a Newtonian acceleration law would require genuinely second-order parent dynamics.

Let
``` math
d\nu_t(y)=\frac{\rho(y,t)\,d\operatorname{vol}_Y(y)}
{\int_Y\rho(\cdot,t)\,d\operatorname{vol}_Y}
```
be the normalized density measure. Assume its support lies in a geodesically convex normal ball on which the squared-distance functional is strictly convex.

<div class="definition">

**Definition 5** (Karcher centroid). The centroid is the unique minimizer
``` math
X(t)=\operatorname*{argmin}_{z\in Y}
\frac12\int_Y d_Y(z,y)^2\,d\nu_t(y).
```

</div>

This definition is coordinate invariant. A coordinate average is used only after choosing a normal chart and estimating its curvature-dependent error.

Let $`\{\Psi_X:X\in\mathcal M\}`$ be a smooth localized profile manifold and write
``` math
\Psi(t)=\Psi_{X(t)}+r(t),
\qquad
\langle r,\partial_{X^i}\Psi_X\rangle=0.
```
Define the positive tangent Gram matrix $`G_{ij}(X)=\langle\partial_{X^i}\Psi_X,
\partial_{X^j}\Psi_X\rangle`$ and $`V_{\rm eff}(X)=C[\Psi_X]`$.

<div id="thm:modulation" class="theorem">

**Theorem 6** (First-order modulation law). *For the first-order gradient flow $`\partial_t\Psi=-\nabla C(\Psi)`$, assume the profile decomposition is unique, $`G(X)`$ is uniformly invertible, and the remainder and curvature-gradient terms are controlled. Projection onto the tangent space gives
``` math
G_{ij}(X)\dot X^j=-\partial_iV_{\rm eff}(X)+\varepsilon_i(t),
```
where $`\varepsilon_i`$ is bounded by the modulation remainder, localization width, $`\nabla\mathcal R`$, and projector-variation errors specified by the model.*

</div>

A second-order law $`M_{ij}(X)\ddot X^j+\cdots=-\partial_iV_{\rm eff}`$ is retained only when the parent field equation contains an explicit inertial/kinetic second-order term. It does not follow from the FP first-order gradient flow.

# Overlap and interaction sign

For two profiles define
``` math
E_{\rm int}:=C[\Psi_1+\Psi_2]-C[\Psi_1]-C[\Psi_2].
```
Let $`\mathcal O(\Psi_1,\Psi_2)\ge0`$ be a declared overlap functional.

<div id="ass:cross" class="assumption">

**Assumption 7** (Absolute cross-term control). All quadratic and nonlinear cross terms obey
``` math
|E_{\rm int}|\le C_{\rm int}\mathcal O(\Psi_1,\Psi_2).
```

</div>

This assumption yields exactly the displayed absolute estimate. It does not yield positive constants $`c_1,c_2`$ with $`c_1\mathcal O\le E_{\rm int}\le c_2\mathcal O`$.

<div id="thm:sign" class="theorem">

**Theorem 8** (Signed interaction criterion). *If a model additionally proves $`E_{\rm int}\le-c\mathcal O`$ with $`c>0`$, overlap lowers the energy and is energetically attractive. If it proves $`E_{\rm int}\ge c\mathcal O`$, overlap raises the energy and is energetically repulsive. Neither sign follows from overlap magnitude alone.*

</div>

Energetic attraction still does not prove dynamical merger. The flow must have access to the merged basin and avoid intervening conserved quantities or barriers.

# Existence and equilibrium status

The corrected FP–I/II theorems apply to the curved flow only after the full operator supplies the required sectoriality, smoothing, invariant set, compactness/confinement, and projector hypotheses. A Schauder or Darbo result first gives a projected step fixed point. It becomes an equilibrium only when the strict Lyapunov identity is verified. Curvature does not preserve the old fixed-point structure automatically.

# Structural transitions

The final distinction is between preventing a transition, noticing that a trajectory has left an admissible region, and determining where it goes next. An energy barrier can establish the first. An exit time records the second. The third needs accessibility and convergence information that neither of the first two contains.

Let $`\mathcal B_-`$ and $`\mathcal B_+`$ be two basins for a continuous gradient flow with Lyapunov energy $`C`$. Define the mountain-pass level
``` math
c_{-+}:=\inf_{\gamma\in\Gamma_{-+}}\max_{s\in[0,1]}C(\gamma(s)),
```
where $`\Gamma_{-+}`$ is the set of continuous paths joining the two basins.

<div id="thm:barrier" class="theorem">

**Theorem 9** (Energy-barrier exclusion with work). *Assume trajectories are continuous in the energy topology and satisfy
``` math
C[\Psi(t)]\le C[\Psi(0)]+W_{\rm ext}(t),
\qquad W_{\rm ext}(t)\le W_\ast.
```
If $`C[\Psi(0)]+W_\ast<c_{-+}`$, the trajectory cannot pass from $`\mathcal B_-`$ to $`\mathcal B_+`$. For an unforced gradient flow, $`W_\ast=0`$.*

</div>

Noise-driven transitions require probabilistic exit estimates and are not covered by this deterministic theorem.

<div id="thm:exit" class="theorem">

**Theorem 10** (Exit does not determine selection). *Let $`\mathcal A`$ be an admissible region and $`\tau_{\rm exit}=\inf\{t:\Psi(t)\notin\mathcal A\}`$. Finite $`\tau_{\rm exit}`$ detects loss of admissibility only. Identification of the post-exit basin requires a separate basin-accessibility and convergence or selection theorem.*

</div>

# Conclusion

Curvature is not merely a scalar subtraction from a damping margin. It can shift the spectral cluster, rotate the coherent projector, and leak coherent amplitude into the old noncoherent sector. This paper makes those effects explicit and adds the exact boundary between natural projective transport, bare compression, Feshbach reduction, and nonlinear shorting. Centroid motion is intrinsic and first order for a gradient parent flow; interaction signs and dynamic merger require additional hypotheses; and barrier crossing is controlled by total energy plus work. These corrected statements preserve the useful curvature and transition program without claiming that a finite projector, overlap, or positive damping alone selects a physical basin.

The reusable achievement is a typed decision tree. Use the curved Riesz projector when a separated full-operator cluster is known; otherwise retain the old projector together with an explicit leakage floor. Use bare finite compression only on an invariant subspace; otherwise use the full-operator Feshbach map. Use reduced-Green shorting for nonlinear quotient coordinates, not as an unexplained linear restriction. Finally, distinguish first-order centroid motion, energetic interaction sign, barrier exclusion, exit, and basin selection. An application must instantiate this decision tree with its connection, Hessian, quotient and finite execution data. The foundation is independent of which application eventually supplies them.

<div class="thebibliography">

99

H. B. Lawson and M.-L. Michelsohn, *Spin Geometry*, Princeton Mathematical Series, Vol. 38, Princeton University Press, Princeton, 1989.

P. Petersen, *Riemannian Geometry*, 3rd edition, Graduate Texts in Mathematics, Vol. 171, Springer, New York, 2016.

R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, Applied Mathematical Sciences, Vol. 68, Springer-Verlag, New York, 1997.

D. Henry, *Geometric Theory of Semilinear Parabolic Equations*, Lecture Notes in Mathematics, Vol. 840, Springer-Verlag, Berlin, 1981.

E. Hebey, *Nonlinear Analysis on Manifolds: Sobolev Spaces and Inequalities*, Courant Lecture Notes, Vol. 5, American Mathematical Society, Providence, 2000.

P. Nero, *Fixed Points I: Fixed Points over Multi–Bundle Manifolds*, version 7, 2026.

P. Nero, *Fixed Points II: Projected Fixed Points and Equilibria in a 10D Modal Model*, version 6, 2026.

P. Nero, *Fixed Points III: Disturbance–Damping Balance and Stability*, version 8, 2026.

M. S. Narasimhan and S. Ramanan, *Existence of universal connections*, American Journal of Mathematics **83** (1961), 563–572. [doi:10.2307/2372896](https://doi.org/10.2307/2372896).

</div>

# Dependency and reproducibility statement

The inputs are the preceding FP papers and standard mathematical literature. Block elimination and constrained minimization are derived here. No MTT research packet, numerical endpoint or later paper supplies a proof premise.
