---
abstract: |
  This paper audits the strongest currently reproducible connection between Modal Triplet Theory (MTT) and the Standard Model (SM). The result is substantial but tiered. At the exact finite-structure tier, released calculations provide a 27-dimensional qutrit–Weyl carrier, the faithful gauge action $`(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6`$, a three-family chiral representation with all local and global gauge anomalies cancelled, a completed finite real-even geometry, and a rank-four one-Higgs projection inside its rank-twelve raw scalar fluctuation space. At the profile tier, an explicit $`96\times96`$ finite Dirac operator contains the accepted charged and neutral Yukawa matrices; CKM, Higgs, threshold, and precision packets have executable provenance and pass their declared audits. At the embedded-equivalence tier, the selected branch reproduces the same renormalized SM action, parameter point, scheme, and perturbative observable functor, with twelve of twelve declared obligations verified.

  This is not a zero-parameter derivation of the measured SM. The adopted closure standard allows one shared electroweak primitive and measured renormalized profile coordinates downstream. In particular, the finite carrier and gauge representation do not by themselves select Yukawa singular values, mixing matrices, absolute neutrino data, the strong-CP mechanism, or a unique observed branch. We state the exact reconstruction theorem, prove a family-intertwiner nonselection result, explain the distinct roles of the $`27\times27`$ and $`96\times96`$ matrices, give a parameter and provenance ledger, and isolate the remaining source theorems needed for strict no-knob Standard-Model closure.
author:
- Peter Nero
current_version: v3
date: July 2026, Version 3
generated_from_main_tex_sha256: 33abbcc3f7e3364a7f6ac870a0b4fb42e366a461c0813c6abfce0932dc749536
paper_id: modal-triplet-theory-from-mtt-to-standard-model-a-rigor-923ad6b1
release_state: zenodo_released
released_version: v3
title: |
  From Modal Triplet Theory to a Standard-Model Sector
  Exact Finite Structure, Profile-Level Equivalence, and the No-Knob Boundary
zenodo_doi: 10.5281/zenodo.21720135
zenodo_record_id: 21720135
zenodo_url: "https://zenodo.org/records/21720135"
---

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

The current neutral execution uses a normal-ordering Dirac profile with lightest mass set to zero. Two measured mass-squared splittings calibrate two neutral coordinates and emit the corresponding mass, Yukawa, and mixing rows. Absolute mass, ordering, Dirac-versus-Majorana ontology, and the source of those calibration coordinates are separate questions. The finite operator is complete at this declared profile, while strict neutral source selection remains open.

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
Neutrino sector & Two-splitting profile & Two measured splittings plus declared normal-ordering, Dirac, and lightest-mass assumptions; absolute source and ontology remain open.
Precision outputs & Multi-loop profile transport & Fifteen declared source coordinates are transported to eight outputs; source correlations and held-out prediction are separate tests.
Strong CP and branch choice & Open/partial & No selected suppression mechanism or unique global observed-branch measure is established.

</div>

</div>

The rows overlap and must not be arithmetically summed as independent knobs. The defensible global statement is simpler: at the adopted equivalence tier, measured renormalized SM coordinates remain admissible inputs. Therefore the current result does not establish fewer empirical parameters than the SM. “One shared primitive” means one upstream electroweak primitive within this architecture; it does not mean one free parameter for all observed particle physics.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Reproducibility and Result Ownership

The calculations cited here are curated at commit `31247ebb5c22` of the public [MTT results repository](https://github.com/PeterNero/mtt-results-repro/tree/31247ebb5c22f3fbb5443024365433c6ee0bff4a). The repository binds each result identifier to an authority row, source artifact, hash, and verification tier. The most relevant entries are:

- **Discrete carrier.** `qutrit_weyl_27_matrix` is the exact sparse $`27\times27`$ Weyl left action.

- **Gauge and matter.** `typed_family_representation` and `native_gauge_group` are the exact chiral, anomaly, native-group, and $`\mathbb{Z}_6`$-kernel packets.

- **Finite geometry.** `physical_df_96`, `neutral_summand_hypercharge`, and `finite_inner_fluctuation` contain the profile $`D_F`$, the exact native no-go and minimal completion, the shared hypercharge line, the full one-form execution, and the selected one-Higgs projector.

- **Flavor and Higgs profiles.** `charged_yukawa_higgs_profile` is the charged/Higgs replay;
  `neutral_two_primitive_profile` is the neutral replay; and `ckm_prediction_profile` is the numerical prediction-profile certificate.

- **Electroweak rows.** `strict_pew_row` and `direct_k_higgs_row` are exact at the adopted shared primitive tier.

- **Precision transport.** `precision_15_source_transport` is the SMDR source packet;
  `precision_8x8_workspace` is the corresponding output profile packet.

- **Global scope.** `final_12_of_12_audit` closes declared-standard embedded equivalence; `strict_upgrade_ledger` records the stronger open no-knob and foundational program.

Reproduction should start from those released artifacts, not from historical status sentences in the development corpus. The current authority ledger is deliberately stronger than search order: an old file containing “open” or “closed” does not override the selected row and hash.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

# Relation to Standard Approaches

The ordinary renormalized SM specifies the field representations and treats its masses, mixings, couplings, Higgs parameters, and CP data as measured renormalized coordinates. The present MTT program adds an explicit finite carrier and a selected structural route to the same representation. That is a meaningful reduction of structural arbitrariness, especially for the anomaly-free shared circle, finite-algebra completion, and one-Higgs submodule. It is not yet a reduction of all empirical parameter freedom.

Almost-commutative spectral geometry is the closest established mathematical comparison. It also encodes the SM representation and Higgs field through a finite algebra and Dirac operator, and the spectral action produces the corresponding bosonic operator content . The MTT calculation differs by adding the $`27`$-dimensional Weyl carrier, q79/proto-spinor source constraints, and a tiered same-source program. At present it shares the familiar limitation that finite Dirac entries and absolute action normalization require additional input or selection.

The SMDR calculation is not an alternative fundamental theory. It is the precision engine used to transport a declared renormalized SM point. Its inclusion greatly improves consistency and reproducibility, but does not convert an input point into a prediction.

# Remaining Theorems and Falsifiers

The remaining frontier is short enough to state without reopening solved finite rows.

1.  **Zero-primitive electroweak source (B.SM.01).** Emit $`P_{\mathrm{EW}}`$ from the selected source geometry and action normalization without using its observed target.

2.  **No-knob SM values and precision (B.SM.02).** Emit the gauge, charged-flavor, CKM/PMNS, Higgs, and threshold values from that same source; transport them with a complete uncertainty and covariance record; and compare held-out observables.

3.  **Selected upper action (B.ACTION.01).** Construct one upper differential/action whose automorphisms, zero modes, and transferred products reproduce the accepted lower operators.

4.  **Interacting quantum completion (B.QFT.02).** Supply the geometry-selected nonperturbative gauge–BRST completion or controlled regulator limit and its physical state.

5.  **Neutrino, strong-CP, and branch selection.** Select the absolute neutrino data and ontology, a suppression or relaxation mechanism for $`\bar\theta`$, and the global observed branch.

The program is falsifiable at several levels. A failed exact replay of the released finite packets would invalidate the corresponding structural claim. A proof that the selected projector is not compatible with the full upper action would invalidate the one-Higgs source interpretation. A future source emitter that uses measured targets in its construction would remain a replay, not a prediction. Finally, a held-out parameter or observable outside the certified uncertainty region would refute that proposed no-knob source law without undoing the exact representation theory.

# Conclusion

The current MTT-to-SM result is neither the old speculative bundle dictionary nor a completed parameter-free theory. It is a reproducible, layered construction. The discrete $`27`$-carrier, native gauge group, three-family anomaly-free representation, finite-algebra completion, and one-Higgs projector are genuine finite structural results. The $`96\times96`$ Dirac operator, Yukawa and neutrino entries, CKM profile, and precision transport are executable at explicitly declared profile tiers. Together they establish embedded renormalized-SM equivalence at the one-shared-physical-primitive/profile standard.

The remaining scientific leap is not to recompute those matrices again. It is to construct the same-source value functional and upper action that select the admitted profile before empirical comparison. That boundary is now explicit, testable, and narrow enough to guide the next work.

<div class="thebibliography">

10

A. H. Chamseddine and A. Connes, “The Spectral Action Principle,” *Commun. Math. Phys.* **186** (1997) 731–750, [arXiv:hep-th/9606001](https://arxiv.org/abs/hep-th/9606001).

C. A. Stephan, “Almost-Commutative Geometry, Massive Neutrinos and the Orientability Axiom in KO-Dimension 6,” *J. Phys. A* **40** (2007) 9941–9956, [arXiv:hep-th/0610097](https://arxiv.org/abs/hep-th/0610097).

D. Tong, “Line Operators in the Standard Model,” *JHEP* **07** (2017) 104, [arXiv:1705.01853](https://arxiv.org/abs/1705.01853).

E. Witten, “An $`SU(2)`$ Anomaly,” *Phys. Lett. B* **117** (1982) 324–328.

S. P. Martin and D. G. Robertson, “Standard Model Parameters in the Tadpole-Free Pure $`\overline{\mathrm{MS}}`$ Scheme,” *Phys. Rev. D* **100** (2019) 073004, [arXiv:1907.02500](https://arxiv.org/abs/1907.02500).

P. Nero, “MTT Results Reproducibility Capsule,” commit `31247ebb5c22`, <https://github.com/PeterNero/mtt-results-repro>.

</div>
