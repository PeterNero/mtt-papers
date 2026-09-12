---
abstract: |
  This paper audits the strongest currently reproducible connection between Modal Triplet Theory (MTT) and the Standard Model (SM). The result is substantial but tiered. At the exact finite-structure tier, released calculations provide a 27-dimensional qutrit–Weyl carrier, the faithful gauge action $`(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6`$, a three-family chiral representation with all local and global gauge anomalies cancelled, a completed finite real-even geometry, and a rank-four one-Higgs projection inside its rank-twelve raw scalar fluctuation space. At the profile tier, an explicit $`96\times96`$ finite Dirac operator contains the accepted charged and neutral Yukawa matrices; CKM, Higgs, threshold, and precision packets have executable provenance and pass their declared audits. At the embedded-equivalence tier, the selected branch reproduces the same renormalized SM action, parameter point, scheme, and perturbative observable functor, with twelve of twelve declared obligations verified.

  This is not a zero-parameter derivation of the measured SM. The adopted closure standard allows one shared electroweak primitive and measured renormalized profile coordinates downstream. In particular, the finite carrier and gauge representation do not by themselves select Yukawa singular values, mixing matrices, absolute neutrino data, the strong-CP mechanism, or a unique observed branch. We state the exact reconstruction theorem, prove a family-intertwiner nonselection result, explain the distinct roles of the $`27\times27`$ and $`96\times96`$ matrices, give a parameter and provenance ledger, and isolate the remaining source theorems needed for strict no-knob Standard-Model closure. Later same-source imports reduce the effective non-neutrino profile to thirteen coordinates, excluding QCD theta, and the minimal neutral extension to nineteen. These counts include empirical inputs and are not prospectively validated parameter predictions. Conditional neutral-holonomy, branch-measure and axion-quality results specify more precisely which selections are still required.
author:
- Peter Nero
current_version: v5
date: September 2026, Version 5
generated_from_main_tex_sha256: 4b66c1482bfe0657ac45807d8beef051cd19c90e46162b187bf5ad9d9ce241af
paper_id: modal-triplet-theory-from-mtt-to-standard-model-a-rigor-923ad6b1
release_state: current_revised_tex
released_version: v3
title: |
  From Modal Triplet Theory to a Standard-Model Sector
  Exact Finite Structure, Profile-Level Equivalence, and the No-Knob Boundary
zenodo_doi: 10.5281/zenodo.21720135
zenodo_record_id: 21720135
zenodo_url: "https://zenodo.org/records/21720135"
---

# Version 5 Revision Note

Supersedes.
Local version 4; published editions remain unchanged.

Reason.
The interacting-QFT frontier did not distinguish the completed conditional analytic-family construction from selection of its physical source.

Resolution.
Import that distinction from the quantum-mechanics owner paper and its frozen family-source certificate, with no repeated proof.

Retained result.
All finite structures, profile values, parameter counts, and the declared embedded-equivalence theorem remain unchanged.

Open boundary.
The common source, full-domain measure, gluing and uniform continuum control remain open; finite matrices and determinant lines do not supply them.

# Version 4 Revision Note

Supersedes.
Version 3 of this paper; the earlier released PDF remains a separate edition.

Reason.
The reconstruction was already in place, but its normalization, parameter, neutral and strong-CP discussions did not include the later accepted source results.

Resolution.
Add scoped imports of the finite gauge spectra and common-scale obstruction, positive gauge density, one-anchor coupling map, thirteen/nineteen-coordinate ledger, neutral holonomy and conditional branch measure, and the Green–Schwarz axion and quality criteria. Explain the finite Cech and rank-two HYM witnesses without transferring them to the physical visible rank-three bundle.

Retained result.
The finite-carrier, anomaly, Higgs, reconstruction and family-intertwiner results are unchanged. No source proof is duplicated and no numerical artifact is refitted.

Open boundary.
Independent physical value selection, a common visible–hidden endpoint, global branch uniqueness, the nonperturbative axion payload and interacting QFT completion remain separate from the adopted profile closures.

# Version 3 Revision Note

Supersedes.
Version 2, *Modal Triplet Theory: From MTT to Standard Model*.

Reason.
Version 2 identified a useful proposed bridge, but described bundle-to-group assignments, family number, electroweak breaking, Yukawa values, and a one-loop benchmark as a complete first-principles derivation. The present calculation repositories now contain much stronger finite results and, equally importantly, exact tier and parameter audits that rule out that wording.

Resolution.
Version 3 replaces the old argument by a hash-addressed reconstruction. It separates exact structural theorems, profile-dependent executions, measured-parameter equivalence, and open source selection. It also incorporates the native gauge-group theorem, the finite-triple no-go and minimal completion, the one-Higgs projector, the current CKM and SMDR precision results, and the strict-upgrade ledger.

Retained content.
The chiral field dictionary, explicit anomaly checks, Higgs and Yukawa interpretation, and the goal of connecting MTT finite geometry to the SM remain, but only at their justified tiers.

Open boundary.
Zero-primitive electroweak normalization, no-knob flavor and precision values, absolute neutrino ontology, strong CP, the selected upper action, nonperturbative four-dimensional QFT, and unique observed-branch selection remain open.

# What Question Is Actually Answered?

There are several inequivalent meanings of “derive the Standard Model.” A construction may recover the SM gauge representation but not its couplings. It may reproduce a measured parameter point without predicting that point. It may build a finite Dirac operator but still borrow the quantum field theory used to interpret it. Confusing these tasks makes a calculation look stronger than it is and also hides genuine progress.

The current MTT result answers the following precise question:

> Can one selected finite MTT branch carry the exact SM representation and finite-geometric operator structure, and can that branch be mapped to the renormalized SM at a declared measured parameter point with executable precision transport?

At the adopted standard the answer is yes. The stronger question—whether MTT selects all measured values from prior geometry with no continuous empirical input—has not yet been answered. This paper is organized around that distinction.

## Four status tiers

<div class="definition">

**Definition 1** (Structural, profile, equivalence, and prediction tiers). For this paper the following terms have fixed meanings.

1.  A *structural exact* result uses discrete or symbolic source data and verifies the stated algebraic identity without observed SM values.

2.  A *profile* result executes a mathematically definite operator after a declared set of measured or calibrated entries has been supplied.

3.  *Embedded renormalized-SM equivalence* means that the selected branch is identified with the same renormalized SM action, parameter point, scheme, and observable functor. It is an existence and consistency statement at that point.

4.  A *strict no-knob prediction* requires the numerical values to be emitted by a selected upstream MTT source before comparison with the observations used to test them.

</div>

The status words are part of the mathematics. A profile theorem does not become a prediction because its matrix calculation is exact after the entries are inserted. Conversely, use of a profile does not invalidate an exact theorem about the representation, anomaly lattice, or operator identities surrounding it.

# The Two Finite Matrices Have Different Jobs

Two matrix sizes recur in the calculation program. They should not be conflated.

## The $`27\times27`$ qutrit–Weyl realization

Let $`X,Z\in\operatorname{End}(\mathbb{C}^3)`$ be the qutrit shift and clock operators,
``` math
\begin{equation}
ZX=\omega XZ,\qquad X^3=Z^3=I,\qquad
\omega=\exp(2\pi i/3).
\end{equation}
```
The nine Weyl operators $`W_{ab}=Z^aX^b`$, $`a,b\in\mathbb{Z}_3`$, form an orthogonal basis of $`\operatorname{HS}(\mathbb{C}^3)`$. The selected finite carrier is
``` math
\begin{equation}
\mathcal{H}_Q=\mathbb{C}^3_{\mathrm{class}}\otimes\operatorname{HS}(\mathbb{C}^3_{\mathrm{qutrit}}),
\qquad \dim_{\mathbb{C}}\mathcal{H}_Q=3\cdot9=27,
\end{equation}
```
with ordered basis $`|c,a,b\rangle`$. Left multiplication by $`X`$ and $`Z`$ gives two sparse $`27\times27`$ matrices. The released packet verifies rank $`27`$ for each, $`27`$ nonzero entries in each matrix, full rank $`27`$ for the represented algebra basis, and residuals below $`3\times10^{-15}`$ for the left-action Weyl relation. No observed SM value is used.

This is an exact finite algebraic carrier. It is not a $`27`$-particle list, not the SM mass matrix, and not the SM Lagrangian written as one matrix. Its role is to make the discrete class/phase/shift algebra and its projectors executable. Gauge, chirality, flavor magnitudes, and the action require additional typed objects.

## The $`96\times96`$ finite Dirac operator

The second matrix acts on the completed finite fermion Hilbert space. There are sixteen left-handed Weyl slots per family when a neutral singlet is included, forty-eight slots for three families, and the real finite geometry includes the conjugate sector, giving dimension $`96`$. The finite Dirac operator $`D_F`$ connects left and right representation slots and carries the Yukawa and neutral-mass blocks.

Thus the dimensions answer different questions:

<div class="center">

<div class="tabularx">

0.94@L0.17Y Y@ Object & What indexes its basis & What it establishes
$`27\times27`$ & Three discrete classes times nine qutrit–Weyl operators & A faithful finite left-action realization of the selected Weyl carrier
$`96\times96`$ & Three-family particle and conjugate finite-fermion slots & The finite Dirac, grading, reality, order-zero, and order-one calculations at the declared profile

</div>

</div>

Neither dimension is the dimension of spacetime, and neither is a conventional SM requirement. They are dimensions of two MTT finite carriers.

# Exact Gauge and Chiral Structure

## Native bundle automorphisms

The selected rank-one, rank-two, and determinant-trivial rank-three carrier tensors have native automorphism groups
``` math
\begin{equation}
\mathrm{U}(1),\qquad \operatorname{USp}(2)=\mathrm{SU}(2),\qquad \mathrm{SU}(3),
\end{equation}
```
respectively. On the selected chiral representation, the central element
``` math
\begin{equation}
(\omega_3,-1,e^{i\pi/3})
\end{equation}
```
acts trivially and generates a six-element kernel. The faithful image of this particular field representation is therefore
``` math
\begin{equation}
G_{\mathrm{SM}}=\frac{\mathrm{SU}(3)_C\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y}{\mathbb{Z}_6}.
\end{equation}
```
This is an exact statement about the selected representation. It should not be confused with an experimental determination of the complete global line-operator spectrum: local SM fields alone can be compatible with several quotients, as emphasized in the standard analysis of global SM gauge structure .

## Three-family chiral carrier

Using left-handed Weyl notation, one family is
``` math
\begin{equation}
\mathcal{H}_{16}=Q\oplus u^c\oplus d^c\oplus L\oplus e^c\oplus N^c,
\qquad
\mathcal{H}_{\mathrm{ch}}=\mathbb{C}^3_{\mathrm{family}}\otimes\mathcal{H}_{16}.
\end{equation}
```
The gauge action is family diagonal,
``` math
\begin{equation}
\rho_{\mathrm{ch}}(g)=I_3\otimes\rho_{16}(g),
\end{equation}
```
and the six rows are
``` math
\begin{equation}
\begin{aligned}
Q&:(\mathbf3,\mathbf2)_{1/6},&
u^c&:(\bar{\mathbf3},\mathbf1)_{-2/3},&
d^c&:(\bar{\mathbf3},\mathbf1)_{1/3},\\
L&:(\mathbf1,\mathbf2)_{-1/2},&
e^c&:(\mathbf1,\mathbf1)_{1},&
N^c&:(\mathbf1,\mathbf1)_{0}.
\end{aligned}
\end{equation}
```
The Higgs row $`(\mathbf1,\mathbf2)_{1/2}`$ is scalar and contributes no chiral gauge anomaly.

## Anomaly audit

The cancellation can be seen without a numerical fit. Per family,
``` math
\begin{align}
\mathrm{SU}(3)^3 &: 2-1-1=0,\\
\mathrm{SU}(3)^2\mathrm{U}(1)_Y &: 2\left(\frac12\right)\frac16
 +\left(\frac12\right)\left(-\frac23\right)
 +\left(\frac12\right)\frac13=0,\\
\mathrm{SU}(2)^2\mathrm{U}(1)_Y &: 3\left(\frac12\right)\frac16
 +\left(\frac12\right)\left(-\frac12\right)=0,\\
\mathrm{grav}^2\mathrm{U}(1)_Y &: 6\frac16+3\left(-\frac23\right)
 +3\frac13+2\left(-\frac12\right)+1=0,\\
\mathrm{U}(1)_Y^3 &: 6\left(\frac16\right)^3+3\left(-\frac23\right)^3
 +3\left(\frac13\right)^3+2\left(-\frac12\right)^3+1=0.
\end{align}
```
There are four $`\mathrm{SU}(2)`$ doublets per family after color multiplicity and hence twelve for three families, so the global Witten anomaly is absent . The released representation packet evaluates the same coefficients on the same forty-eight-state carrier, rather than combining anomaly statements from unrelated conventions.

<div class="proposition">

**Proposition 2** (Exact finite gauge-content result). *The selected native carrier and chiral packet define an anomaly-free representation of $`G_{\mathrm{SM}}`$ on three identical families, with no continuous parameter used to select the group, hypercharge lattice, or anomaly cancellations.*

</div>

<div class="proof">

*Proof.* The native automorphism groups give the three local factors. Exhaustive center action gives the $`\mathbb{Z}_6`$ kernel. The displayed representation and anomaly sums prove the local conditions, and the even number of weak doublets proves the global condition. These operations use only integer charges, representation multiplicities, and finite matrices. ◻

</div>

## What the finite gauge spectra add

Representation content and a kinetic operator answer different questions. The released gauge-spectrum packets supply the latter on the nine-state finite base $`\mathbb F_3^2`$, with eigenvalues $`0,g,2g`$ of multiplicities $`1,4,4`$ and $`g\simeq4.386490844928604`$ in the packet’s selected units. Tensoring the base operator with the adjoint, and using the selected unitary transport $`U`$ for the weak sector, gives
``` math
\begin{equation}
\Delta_2^{\rm fin}=U(\Delta_{\mathbb F_3^2}\otimes I_3)U^{-1},\qquad
\Delta_3^{\rm fin}=\Delta_{\mathbb F_3^2}\otimes I_8.
\end{equation}
```
The weak multiplicities are $`(3,12,12)`$ and the color multiplicities are $`(8,32,32)`$. For color the admitted background is central and hence acts trivially in the adjoint. These are finite-dimensional exactness statements, not zero-error truncations of an arbitrary continuum HYM operator. In particular, $`U`$ is an operator in the transport-closed quotient; raw multiplication in a twenty-seven-mode Fourier truncation is not its substitute.

The two packets close the ten-row finite spectral family. Their common base spectrum also proves an obstruction: this family alone produces a common renormalization-scale shift, not an independent nonuniversal threshold shape. The combined gauge/ghost indices are $`-22/3`$ and $`-11`$; multiplying an additional continuum ghost determinant into those already combined indices would double count without a new factorization theorem. The later positive-density construction below adds genuinely different operator information rather than reopening these spectral rows .

# Finite Geometry and the Higgs Module

## A no-go result and its minimal completion

For a KO-dimension-six finite geometry, the original three-summand algebra $`\mathbb{C}\oplus\mathbb H\oplus M_3(\mathbb{C})`$ has two problems when the selected neutral singlet is included. The $`N_R:\mathbb{C}\!\to\!\mathbb{C}`$ self-edge obstructs orientability, in agreement with the known right-handed-neutrino issue , and the one-family intersection form
``` math
\begin{equation}
\begin{pmatrix}
0&2&2\\[-1mm]
-2&0&-2\\[-1mm]
-2&2&0
\end{pmatrix}
\end{equation}
```
is antisymmetric of odd rank and has determinant zero.

The selected neutral line $`1_M=N^c`$ canonically supplies
``` math
\begin{equation}
\mathbb{C}_N=\operatorname{End}_{\mathbb{C}}(1_M),\qquad
\mathcal{A}_F'=\mathbb{C}\oplus\mathbb H\oplus M_3(\mathbb{C})\oplus\mathbb{C}_N.
\end{equation}
```
With the neutral edge moved to the distinct $`\mathbb{C}_N`$ sheet, an explicit Hochschild zero-cycle represents the grading with zero stored residual, and the four-summand intersection form has determinant $`4`$ per family. This completion adds a primitive central idempotent but no particle slot and no continuous coefficient.

The distinct complex sheets do not create a second physical circle. If their Abelian phases are $`(\alpha,\mu,\nu)`$, the independent linear anomaly equations are
``` math
\begin{equation}
\alpha+3\mu=0,\qquad \alpha-\nu=0.
\end{equation}
```
Their primitive integer null vector is $`(3,-1,3)`$, which yields
``` math
\begin{equation}
6Y=(1,-4,2,-3,6,0)
\end{equation}
```
on $`(Q,u^c,d^c,L,e^c,N^c)`$. The cubic anomaly vanishes on the same line; an independent neutral phase is anomalous. This is the finite-geometric realization of one shared anomaly-free hypercharge circle.

## The one-Higgs projection

The complete one-form calculation executes all $`26^2=676`$ real-algebra basis pairs in
``` math
\begin{equation}
\Omega^1_{D_F}(\mathcal{A}_F')=\operatorname{span}\{\rho(a)[D_F,\rho(b)]\},
\qquad A_{\mathrm{real}}=A+J_FAJ_F^{-1}.
\end{equation}
```
The unrestricted real fluctuation space has rank twelve. It is therefore a three-doublet scalar space, not automatically the one-Higgs SM. The selected q79/proto-spinor alignment rule is
``` math
\begin{equation}
H_{\mathrm{up}}=H_{\nu}=H,\qquad
H_{\mathrm{down}}=H_e=-\varepsilon\overline H.
\end{equation}
```
When executed on the actual one-form space, its image has real rank four and removes eight real scalar directions. The stored inclusion residual is $`6.15\times10^{-15}`$. The survivor is one complex weak doublet of hypercharge $`1/2`$.

The finite gauge traces are
``` math
\begin{equation}
k_Y:k_2:k_3=10:6:6,
\end{equation}
```
which become $`6:6:6`$ after the conventional $`5/3`$ hypercharge normalization. This supplies a finite normalization relation. It does not determine the observed gauge couplings without a four-dimensional Dirac geometry, cutoff moments, canonical field normalization, a matching scale, and renormalization-group transport. Those distinctions are standard in the spectral action framework .

## Selected density, relative shape and the remaining amplitude

The later Route-A source supplies response operators $`I+Z`$ and $`I+X`$. Their Gram map $`G(M)=MM^\dagger`$ gives positive, basis-covariant densities
``` math
\begin{equation}
\begin{aligned}
\Phi_u=\Phi_e&=G(I+Z),&\Phi_d=\Phi_N&=G(I+X),\\
\Phi_Q=\Phi_L&=G(I+Z)+G(I+X).
\end{aligned}
\end{equation}
```
Both right-hand densities have spectrum $`(1,1,4)`$ and trace six; the left trace is twelve. Together with the admitted heat-shadow and finite-action rules, this yields the relative gauge-action shape
``` math
\begin{equation}
\widehat K=K/K_2=(1.9568437044693519,\ 1,\ 0.3098373950028702).
\end{equation}
```
This is a source-owned result at the declared corpus-action tier. It is not a derivation of the proper-time/action premise from primitive MTT. Nor should these density-weighted coefficients be confused with the unweighted traces $`10:6:6`$ above.

In the normalized convention the coupling map is
``` math
\begin{equation}
g_i^{-2}=c\widehat K_i,\qquad c=6f_0,
\qquad g_1=\sqrt{5/3}\,g_Y.
\end{equation}
```
Here $`f_0`$ denotes the common spectral-action amplitude in that convention. Supplying only $`g_2=0.6475986707537685`$ fixes $`c=2.3844493555491852`$ and gives
``` math
\begin{equation}
g_1=0.46294338085858994,\qquad g_3=1.1634267159672989.
\end{equation}
```
At the frozen SMDR scheme and scale, the correlated two-coordinate statistic is $`\chi^2=5.725295700053512\times10^{-6}`$. This is a close compatibility check, not held-out evidence: the comparison profile was known while the shape construction was developed. A frozen no-retuning ratio test is available for future independent data.

The unresolved amplitude is exactly one dimensional within this map. Replacing $`c`$ by $`a c`$, $`a>0`$, sends every $`g_i`$ to $`a^{-1/2}g_i`$ and leaves all ratios unchanged. Normalizing a Born probability or a filter measure does not select this action amplitude. In particular, $`P_{\rm EW}=0.0685013467625`$ is a different typed quantity and cannot replace $`c`$ in the kinetic term. A zero-anchor extension must supply a common-convention modal action, twistor-action amplitude, or spectral-action measure that fixes $`c`$ independently. The three normalization packets establish these imports and the scope of the scale obstruction .

# Where the Numerical Values Enter

The renormalized SM action can be written schematically as
``` math
\begin{equation}
S_{\mathrm{SM}}[\mathbf p(\mu);\mathfrak s]
=\int \!d^4x\,\bigl(\mathcal{L}_{\mathrm{gauge}}+\mathcal{L}_{\mathrm{fermion}}
+\mathcal{L}_{\mathrm{Higgs}}+\mathcal{L}_{\mathrm{Yukawa}}+\mathcal{L}_{\theta}\bigr),
\end{equation}
```
where $`\mathbf p(\mu)`$ is the renormalized parameter vector and $`\mathfrak s`$ records the scheme, scale, loop order, and matching conventions. Structural reconstruction fixes which terms and representations are allowed. Numerical equivalence additionally needs $`\mathbf p(\mu)`$ and $`\mathfrak s`$.

## Charged flavor and the finite Dirac operator

The released profile packet supplies $`Y_u,Y_d,Y_e`$ and $`\lambda_H`$ at a common declared scale. Inserted into $`D_F`$, these matrices pass self-adjointness, grading, reality, order-zero, and order-one checks. The profile traces are
``` math
\begin{equation}
a=\operatorname{Tr}(Y^\dagger Y)=3.15667873398489,
\qquad
b=\operatorname{Tr}[(Y^\dagger Y)^2]=3.31696406124945,
\end{equation}
```
with color multiplicities included. These are exact evaluations of the supplied profile, not predictions of its entries.

The CKM packet contains three selected profile rows and a declared uncertainty comparison. Its largest displacement from the comparison profile is $`2.36\times10^{-4}`$ standard deviations. The obsolete requirement of exact equality to a moving experimental central estimator has been retired. This is a numerically certified profile result; it does not turn all flavor values into upstream algebraic constants.

## Neutral profile

The original neutral execution used two measured mass-squared splittings and a declared zero lightest mass. The later U5 import reparameterizes those two coordinates as one central holonomy $`\phi`$ and one atmospheric mass-squared scale. It is a structural refinement, not a reduction from two empirical inputs to one .

For $`\zeta_3=e^{2\pi i/3}`$, the retained holonomy is
``` math
\begin{equation}
H_\nu(\phi)=e^{i\phi}\operatorname{diag}(1,\zeta_3,\zeta_3^2).
\end{equation}
```
If the neutral action preserves this holonomy, a Majorana entry can survive $`H_\nu^T M_MH_\nu=M_M`$ only when the corresponding eigenvalue product is one. Thus all Majorana entries vanish away from the self-conjugate values $`\phi=0,\pi/3`$ modulo the shape period. The accepted profile $`\phi=0.02619638630300379`$ avoids those values and lies in the normal-ordering chamber $`0<|\phi|<\pi/6`$ of the selected neutral spectrum. Its conjugate $`-\phi`$ has the same sorted masses, with the low-family labels exchanged.

Consequently Dirac character and normal ordering are fixed *within this admitted holonomy-preserving profile*. They are no longer additional arbitrary ontology choices inside that profile. The nil minimal-trace boundary $`m_{\rm lightest}=0`$, the holonomy value, the absolute scale and the right-handed basis convention remain declared inputs or source conditions. The resulting thirty-six mass, Yukawa and matrix rows are closed at the one-holonomy/one-scale tier. Selecting those inputs from the physical source remains open.

## Electroweak normalization and Higgs row

The adopted baseline counts one shared physical primitive, denoted $`P_{\mathrm{EW}}`$. Given that primitive, the strict electroweak source row and the direct $`K_{\mathrm{threshold}}.\Omega_H.\lambda`$ row are exact in the released ledger. No separate Higgs-specific continuous parameter is added by that construction. Deriving $`P_{\mathrm{EW}}`$ itself from selected source geometry is the stronger zero-primitive problem.

## Multi-loop precision transport

The precision workspace transports fifteen declared source coordinates through SMDR v1.3 to an eight-coordinate output with a positive-definite $`8\times8`$ covariance. SMDR is an established multi-loop implementation of the $`\overline{\mathrm{MS}}`$ SM, including running and threshold matching . In MTT the result proves that the selected profile can be carried consistently through a modern common scheme. It is not an independent prediction when the same measured source coordinates are used to construct the input point. The current accepted workspace uses a declared diagonal source covariance; a complete official joint input likelihood is a stricter upgrade.

# The Reconstruction Theorem

<div class="definition">

**Definition 3** (Selected SM reconstruction record). A selected reconstruction record is
``` math
\begin{equation}
\mathfrak R_{\mathrm{SM}}=
(\mathcal{H}_Q,L_X,L_Z;G_{\mathrm{SM}},\mathcal{H}_{\mathrm{ch}};
\mathcal{A}_F',\mathcal{H}_F,D_F,J_F,\Gamma_F;P_H;
\mathbf p,\mathfrak s,\mathcal{O}_{\mathrm{ren}}),
\end{equation}
```
where the semicolon-separated blocks are, respectively, the discrete finite carrier, gauge and chiral data, finite real-even geometry, one-Higgs projector, and renormalized profile plus observable functor.

</div>

<div class="definition">

**Definition 4** (Embedded renormalized-SM equivalence). An MTT branch has embedded renormalized-SM equivalence when there is a typed identification from its selected coherent sector to a standard SM presentation that intertwines the gauge action and finite fermion operator, sends the selected action to $`S_{\mathrm{SM}}[\mathbf p(\mu);\mathfrak s]`$, and gives the same declared perturbative observable functor $`\mathcal{O}_{\mathrm{ren}}`$ with the same input provenance and uncertainties.

</div>

<div class="theorem">

**Theorem 5** (Current released reconstruction). *For the hash-addressed result packets listed in <a href="#sec:repro" data-reference-type="ref+label" data-reference="sec:repro">8</a>, the selected MTT record has:*

1.  *exact qutrit–Weyl, gauge-group, chiral-representation, anomaly, hypercharge, finite-algebra, and one-Higgs structural rows;*

2.  *an explicit profile-level $`96\times96`$ finite Dirac operator and accepted charged, neutral, Higgs, CKM, threshold, and precision rows;*

3.  *embedded renormalized-SM equivalence at the one-shared-physical-primitive/profile standard, with all twelve declared audit obligations satisfied.*

*The theorem does not imply strict no-knob value selection, unique branch selection, or a nonperturbative construction of the interacting four-dimensional quantum field theory.*

</div>

<div class="proof">

*Proof.* Part (a) is the composition of the independently replayed exact packets for the $`27`$-carrier, native gauge action, typed family representation and anomalies, neutral algebra completion, and rank-four Higgs projection. Their shared convention map identifies the six left-Weyl rows and the unique anomaly-free hypercharge line. Part (b) uses the same representation to assemble $`D_F`$ and then applies the declared profile and SMDR transport packets. The final global audit checks the compatibility interfaces, parameter provenance, scheme, observable functor, and recovery rows and reports twelve accepted obligations out of twelve. The final sentence follows because the same audit explicitly admits measured profile coordinates, imports perturbative SM quantization, and retains the stronger source and nonperturbative-QFT rows as open. ◻

</div>

This theorem is best read as a reproducible existence and consistency result. It is stronger than saying that some matrices can be fitted to SM data, because much of the representation and finite geometry is fixed and exactly checked. It is weaker than a parameter prediction, because the observed profile is still part of the input record.

# Why the Structural Data Do Not Yet Select All Values

<div class="theorem">

**Theorem 6** (Family-intertwiner nonselection). *The family-diagonal gauge representation $`\rho_{\mathrm{ch}}=I_3\otimes\rho_{16}`$ does not uniquely determine the charged Yukawa matrices or their singular values and mixings.*

</div>

<div class="proof">

*Proof.* The gauge action is trivial on the family factor. Consequently, every family transformation $`U\in\mathrm{U}(3)`$ commutes with it. Gauge-invariant Yukawa maps between the allowed left and right representation slots may therefore carry arbitrary family matrices $`Y_u,Y_d,Y_e\in M_3(\mathbb{C})`$, subject only to the chosen reality and Higgs-conjugation conventions. Changing their singular values changes masses while preserving the gauge representation and anomaly equations. Changing their relative left singular vectors changes CKM mixing while preserving the same structural data. Hence a further selected source functional is necessary. ◻

</div>

The theorem pinpoints the remaining task. More algebraic execution of the same representation cannot, by itself, determine the missing numbers. One needs a map from selected geometry and action data to the family coefficients, together with an exactness or uncertainty certificate and a held-out comparison.

## Parameter ledger

<div class="center">

<div class="tabularx">

0.96@L0.23L0.18Y@ Layer & Current status & Parameter meaning
Finite carrier, gauge group, anomalies, algebra completion, Higgs projector & Structural exact & Zero continuous fit parameters are introduced by these finite executions.
Shared $`P_{\mathrm{EW}}`$ & One admitted physical primitive & Counted once across electroweak and direct Higgs/threshold rows; its zero-primitive source remains open.
Charged Yukawa and Higgs values & Profile replay & Measured/common-scale coordinates are accepted downstream; their exact matrix evaluation is not source prediction.
CKM & Certified prediction profile & Three selected rows with uncertainty comparison; a complete no-knob flavor source theorem is stronger.
Neutrino sector & One-holonomy/one-scale profile & Dirac character and normal ordering follow within the retained profile; its holonomy, scale and nil boundary remain source conditions.
Precision outputs & Multi-loop profile transport & Fifteen declared source coordinates are transported to eight outputs; source correlations and held-out prediction are separate tests.
Strong CP and branch choice & Conditional imports & The two-point conditional measure is fixed; global uniqueness and the selected nonperturbative axion-quality payload remain open.

</div>

</div>

The rows overlap and must not be arithmetically summed as independent knobs. The later deduplicated ledger does give an effective count at the adopted standard :
``` math
\begin{equation}
\underbrace{1}_{\text{gauge anchor}}+
\underbrace{9}_{\text{charged magnitudes}}+
\underbrace{1}_{\text{CKM phase}}+
\underbrace{1}_{\text{EW scale}}+
\underbrace{1}_{P_{\rm EW}}=13.
\end{equation}
```
QCD theta is excluded from this count. Relative to the previous eighteen-coordinate non-neutrino profile, the common gauge shape replaces two relative coupling coordinates and the three accepted CKM-angle prediction profiles replace three more. The CKM phase is *not* removed: the q79 phase comparison has a $`2.213743629348511`$ degree residual and remains a contact/postcheck, separate from the much closer three-angle comparison above.

The minimal neutral extension adds three mixing angles, one Dirac CP phase, one holonomy shape and one mass scale, giving nineteen coordinates in total. This is an effective model-coordinate reduction at a specified profile standard, not five independently confirmed predictions and not a no-input parameter count. The SMDR fifteen-source vector is a transport input chart, not another fifteen independent fundamental parameters to add to this ledger. “One shared primitive” refers to the upstream electroweak/Higgs object, not to the total freedom of observed particle physics.

## The conditional branch measure

The U9 import considers the selected two-point antiunitary orbit $`\{q79/F/m1,q369/F^*/m2\}`$. Antiunitary invariance and normalization force equal weights $`1/2`$. Conditioning on the independently specified retarded singleton then gives probability one for q79; the advanced condition gives its conjugate . This introduces no new continuous parameter. The shared compact phase circle is not identified with Lorentzian time by that conditioning.

This small probability space must not be substituted for the space of every admissible MTT carrier. The full carrier domain, quotient, measurable structure, selected measure or coercive action, and existence/support result remain to be constructed. U5 and U9 are therefore closed at their adopted profile/conditional-orbit tiers while remaining open as strict source/global statements. The later adopted upgrade tally is four closed, four partial and one dependency-blocked; the stricter tally remains two, six and one.

## Strong CP: the current and the quality question

The $`E_6`$ branching $`27=16_1\oplus10_{-2}\oplus1_4`$ gives a useful negative check. With $`\mathcal A_3=\sum 2T(R)Q_\psi`$ including multiplicities, three light matter families contribute $`+12`$, while the colored partners contribute $`-12`$. The complete representation has zero anomaly. Discarding the partners does not by itself select a surviving anomalous Peccei–Quinn current; threshold anomaly matching must be accounted for .

The independent candidate is the model-independent Green–Schwarz axion, the periodic scalar dual of the spacetime two-form. In the source normalization it is $`\theta_{\rm MI}=2\pi\int_{X_6}B_6`$, with period $`2\pi`$, and $`a_{\rm MI}=f_{\rm MI}\theta_{\rm MI}`$. It is not the flat order-three internal gerbe. The conditional reduction gives the primitive color term $`-\theta_{\rm MI}k_3c_2(F_c)`$ with $`k_3=1`$, and hence domain-wall number one for this primitive single-axion coupling. Its kinetic normalization still depends on the ten-dimensional action, volume and coupling. Neither the anomaly index nor the reduction formula selects a physical axion scale by itself.

There is now a nonlinear sufficient quality test, not just an appeal to a small extra potential. Write
``` math
\begin{equation}
V(\theta)=\chi_{\rm QCD}[1-\cos(\theta+\bar\theta)]
-\sum_j\Lambda_j^4\cos(n_j\theta+\delta_j).
\end{equation}
```
Set $`M_0=\sum_j\Lambda_j^4`$ and $`M_k=\sum_j|n_j|^k\Lambda_j^4`$ for $`k=1,2`$. Assume the periodic perturbation is twice differentiable, the displayed sums converge, $`\chi_{\rm QCD}>0`$ and $`0<\epsilon<\pi/2`$. The imported criterion is
``` math
\begin{equation}
\begin{aligned}
M_1&<\chi_{\rm QCD}\sin\epsilon,&
M_2&<\chi_{\rm QCD}\cos\epsilon,\\
2M_0&<\chi_{\rm QCD}(1+\cos\epsilon).
\end{aligned}
\end{equation}
```
It places the unique global minimum modulo $`2\pi`$ within $`\epsilon`$ of the CP-conserving point. The bounds control the derivative, curvature and competing far minimum respectively; they do not assume a linearized small-angle solution. The missing physical input is the same-source non-QCD harmonic/amplitude table, including hidden-gauge and wrapped-brane contributions. A topological anomaly calculation cannot bound those amplitudes.

The multi-axion import supplies a complementary route. For the admitted principal $`T^2`$ bundle over K3 with real Chern-class span of rank $`r=1`$ or $`2`$, the pre-lifting count is $`b_2(X_6)=22-r`$, so there are at least twenty model-dependent candidates in addition to the universal mode. This is not a count of light physical axions. For $`N`$ surviving real directions, non-QCD charge matrix $`K_{\rm nq}`$ and QCD row $`k_{\rm QCD}`$, a direction blind to the former but not the latter exists precisely when
``` math
\begin{equation}
\operatorname{rank}K_{\rm nq}<N,\qquad
\operatorname{rank}\begin{pmatrix}K_{\rm nq}\\ k_{\rm QCD}\end{pmatrix}
>\operatorname{rank}K_{\rm nq}.
\end{equation}
```
The illustrative hidden-flat case cannot be silently imposed on the selected nonflat hidden HYM bundle. The actual coupling lattice, gauged/lifted quotient and instanton zero modes still have to be emitted together. These results make the strong-CP target precise, but do not close it .

## What the geometric support witnesses do establish

The reconstruction also uses scoped tests of the mathematical machinery. The finite $`\mathbb F_3^2`$ Cech witness gives eighty-one cocycle entries with vanishing curvature and the selected central phase. Separately, the rank-two scalar HYM calculation is a contraction in a zero-mean Wiener ball on $`T^4`$: at radius $`r=0.01`$, $`Y=0.005476265398865539`$ and $`Z(r)=0.3850761192575742`$ satisfy $`Y+Z(r)r=0.00932702659144128<r`$ and $`Z(r)<1`$. Gaussian Fourier tails and an explicit roundoff envelope are included. The result gives existence and uniqueness in that ball, with the stated transition-law patching .

These are genuine finite-cocycle and rank-two analytic witnesses. They do not evaluate the full analytic Deligne obstruction of a varying q79 spectral cover, prove global uniqueness outside the Wiener ball, or supply the physical rank-three visible bundle and its same-source rank-nine partner. Their construction details belong to the geometry/Flux source; here they explain why a successful support calculation and an open physical endpoint can coexist without contradiction.

## From finite matrices to an analytic physical family

There is a positive result between the finite reconstruction and the remaining interacting-QFT problem. Given a smooth physical elliptic family on a common Sobolev domain, a self-adjoint Hessian realization, and an isolated spectral window on a regular chart, the Dirac/Hessian family, its Riesz projector, Kato transport and analytic determinant line are canonical constructions. They add no further physical parameter once those data have been selected. The conditional construction and its finite nonselection witness are treated in the quantum-mechanics owner paper ; the frozen certificate is `q79_family_source_cutset` in Ref. . This is a useful dependency reduction, not a new assumption that every finite matrix has a unique physical continuum realization.

The reason for the distinction is simple. A finite projection forgets directions of a smooth connection. Changing a forgotten direction can change the full Dirac operator without changing any retained source row. HYM, Bianchi, action and naturality conditions must therefore select the common lift; they cannot be recovered from the $`27`$- or $`96`$-dimensional matrices alone. The later hidden-bundle existence results remain valid at their own tier, but do not by themselves supply this whole common family. Once it is supplied, three separate full-domain tasks still remain: a local chiral-measure current, gluing across crossings and disconnected sectors, and cutoff-uniform locality and fixed-coupling control. A determinant line is not that measure, and a gapped-chart projector is not an extension through a spectral crossing. Thus the analytic construction need not be reinvented, while the physical source and interacting-continuum obligations must not be silently discarded.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Reproducibility and Result Ownership

The calculations cited here are curated at commit `f141a20ea23c` of the public [MTT results repository](https://github.com/PeterNero/mtt-results-repro/tree/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7). The repository binds each result identifier to an authority row, source artifact, hash, and verification tier. The most relevant entries are:

- **Discrete carrier.** `qutrit_weyl_27_matrix` is the exact sparse $`27\times27`$ Weyl left action.

- **Gauge and matter.** `typed_family_representation` and `native_gauge_group` are the exact chiral, anomaly, native-group, and $`\mathbb{Z}_6`$-kernel packets.

- **Finite geometry.** `physical_df_96`, `neutral_summand_hypercharge`, and `finite_inner_fluctuation` contain the profile $`D_F`$, the exact native no-go and minimal completion, the shared hypercharge line, the full one-form execution, and the selected one-Higgs projector.

- **Flavor and Higgs profiles.** `charged_yukawa_higgs_profile` is the charged/Higgs replay;
  `neutral_two_primitive_profile` is the neutral replay; and `ckm_prediction_profile` is the numerical prediction-profile certificate.

- **Electroweak rows.** `strict_pew_row` and `direct_k_higgs_row` are exact at the adopted shared primitive tier.

- **Precision transport.** `precision_15_source_transport` is the SMDR source packet;
  `precision_8x8_workspace` is the corresponding output profile packet.

- **Global scope.** `final_12_of_12_audit` closes declared-standard embedded equivalence; `strict_upgrade_ledger` records the stronger open no-knob and foundational program.

- **Gauge spectra and action.**
  `su2_finite_gauge_spectrum`, `su3_finite_gauge_spectrum`,
  `sm_gauge_density_source_promotion`, `sm_gauge_common_scheme_map`, and `sm_gauge_scale_orbit_nogo` separate finite spectra, density-weighted shape and the common kinetic anchor.

- **Refined bookkeeping.**
  `sm_minimal_parameter_ledger`, `sm_neutral_u5_tier_decision`, and `sm_branch_u9_conditional_measure` state the effective counts and adopted neutral/branch closures; the historical strict ledger is not relabeled by them.

- **Strong-CP reductions.** `e6_qpsi_qcd_anomaly`, `sm_axion_gs_reduction`, `sm_axion_quality_bound`, and `sm_multiaxion_superset` supply the current, coupling and quality criteria, not the missing physical instanton amplitudes.

- **Geometric support.** `literal_cech_witness` and `hym_wiener_contraction` are the finite-cocycle and certified rank-two witnesses, not the visible rank-three endpoint.

Reproduction should start from those released artifacts, not from historical status sentences in the development corpus. The current authority ledger is deliberately stronger than search order: an old file containing “open” or “closed” does not override the selected row and hash.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

# Relation to Standard Approaches

The ordinary renormalized SM specifies the field representations and treats its masses, mixings, couplings, Higgs parameters, and CP data as measured renormalized coordinates. The present MTT program adds an explicit finite carrier and a selected structural route to the same representation. That is a meaningful reduction of structural arbitrariness, especially for the anomaly-free shared circle, finite-algebra completion, and one-Higgs submodule. The effective thirteen/nineteen coordinate ledger additionally records a declared profile reduction. Independent prospective validation of those reductions, and selection of the remaining empirical values, are stronger questions.

Almost-commutative spectral geometry is the closest established mathematical comparison. It also encodes the SM representation and Higgs field through a finite algebra and Dirac operator, and the spectral action produces the corresponding bosonic operator content . The MTT calculation differs by adding the $`27`$-dimensional Weyl carrier, q79/proto-spinor source constraints, and a tiered same-source program. At present it shares the familiar limitation that finite Dirac entries and absolute action normalization require additional input or selection.

The SMDR calculation is not an alternative fundamental theory. It is the precision engine used to transport a declared renormalized SM point. Its inclusion greatly improves consistency and reproducibility, but does not convert an input point into a prediction.

# Remaining Theorems and Falsifiers

The remaining frontier is short enough to state without reopening solved finite rows.

1.  **Zero-primitive electroweak source (B.SM.01).** Emit $`P_{\mathrm{EW}}`$ from the selected source geometry and action normalization without using its observed target.

2.  **No-knob SM values and precision (B.SM.02).** Emit the gauge, charged-flavor, CKM/PMNS, Higgs, and threshold values from that same source; transport them with a complete uncertainty and covariance record; and compare held-out observables.

3.  **Selected upper action (B.ACTION.01).** Construct one upper differential/action whose automorphisms, zero modes, and transferred products reproduce the accepted lower operators.

4.  **Interacting quantum completion (B.QFT.02).** Supply the geometry-selected nonperturbative gauge–BRST completion or controlled regulator limit and its physical state.

5.  **Strict neutral, strong-CP, and global branch sources.** Select the neutral holonomy, scale and nil boundary independently; fill the nonperturbative axion-quality and coupling-lattice payload; and define the global carrier space and selection measure. Do not reopen the holonomy-preserving Dirac/ordering result or the finite conditional branch measure.

The program is falsifiable at several levels. A failed exact replay of the released finite packets would invalidate the corresponding structural claim. A proof that the selected projector is not compatible with the full upper action would invalidate the one-Higgs source interpretation. A future source emitter that uses measured targets in its construction would remain a replay, not a prediction. Finally, a held-out parameter or observable outside the certified uncertainty region would refute that proposed no-knob source law without undoing the exact representation theory.

# Conclusion

The current MTT-to-SM result is neither the old speculative bundle dictionary nor a completed parameter-free theory. It is a reproducible, layered construction. The discrete $`27`$-carrier, native gauge group, three-family anomaly-free representation, finite-algebra completion, and one-Higgs projector are genuine finite structural results. The $`96\times96`$ Dirac operator, Yukawa and neutrino entries, CKM profile, and precision transport are executable at explicitly declared profile tiers. Together they establish embedded renormalized-SM equivalence at the one-shared-physical-primitive/profile standard.

The later imports replace a generic parameter warning by an explicit thirteen-coordinate non-neutrino and nineteen-coordinate minimal-neutral ledger, excluding QCD theta. They also close the declared neutral and two-branch conditional problems and identify exact tests for the strong-CP mechanism. Their assumptions explain both the progress and why a selected universe with independently predicted values is still a stronger target.

The remaining scientific leap is not to recompute those matrices again. It is to construct the same-source value functional and upper action that select the admitted profile before empirical comparison. That boundary is now explicit, testable, and narrow enough to guide the next work.

<div class="thebibliography">

10

A. H. Chamseddine and A. Connes, “The Spectral Action Principle,” *Commun. Math. Phys.* **186** (1997) 731–750, [arXiv:hep-th/9606001](https://arxiv.org/abs/hep-th/9606001).

C. A. Stephan, “Almost-Commutative Geometry, Massive Neutrinos and the Orientability Axiom in KO-Dimension 6,” *J. Phys. A* **40** (2007) 9941–9956, [arXiv:hep-th/0610097](https://arxiv.org/abs/hep-th/0610097).

D. Tong, “Line Operators in the Standard Model,” *JHEP* **07** (2017) 104, [arXiv:1705.01853](https://arxiv.org/abs/1705.01853).

E. Witten, “An $`SU(2)`$ Anomaly,” *Phys. Lett. B* **117** (1982) 324–328.

S. P. Martin and D. G. Robertson, “Standard Model Parameters in the Tadpole-Free Pure $`\overline{\mathrm{MS}}`$ Scheme,” *Phys. Rev. D* **100** (2019) 073004, [arXiv:1907.02500](https://arxiv.org/abs/1907.02500).

P. Nero, “MTT Results Reproducibility Capsule,” commit `f141a20ea23c`, <https://github.com/PeterNero/mtt-results-repro>.

P. Nero, selected finite weak/color gauge-spectrum certificates, frozen in Ref. , entries `su2_finite_gauge_spectrum` and `su3_finite_gauge_spectrum`.

P. Nero, selected positive-density promotion, common-scheme coupling map and scale-orbit obstruction, frozen in Ref. , entries `sm_gauge_density_source_promotion`, `sm_gauge_common_scheme_map`, `sm_gauge_scale_orbit_nogo`.

P. Nero, post-A89 minimal parameter ledger, frozen in Ref. , entry `sm_minimal_parameter_ledger`.

P. Nero, neutral U5 tier decision and conditional U9 measure, frozen in Ref. , entries `sm_neutral_u5_tier_decision` and `sm_branch_u9_conditional_measure`.

P. Nero, $`E_6`$ current audit and conditional Green–Schwarz axion/quality reductions, frozen in Ref. , entries `e6_qpsi_qcd_anomaly`, `sm_axion_gs_reduction`, `sm_axion_quality_bound`, and `sm_multiaxion_superset`.

P. Nero, finite Cech witness and certified rank-two HYM contraction, frozen in Ref. , entries `literal_cech_witness` and `hym_wiener_contraction`; interpreted in the Flux compactification audit.

P. Nero, *Modal Triplet Theory and Nonrelativistic Quantum Mechanics: A Coherent-Sector Reconstruction and the Born-Source Boundary*, current canonical manuscript, [MTT papers repository](https://github.com/PeterNero/mtt-papers/tree/main/papers/modal-triplet-theory-from-mtt-to-quantum-mechanics); release family [doi:10.5281/zenodo.17074246](https://doi.org/10.5281/zenodo.17074246).

</div>
