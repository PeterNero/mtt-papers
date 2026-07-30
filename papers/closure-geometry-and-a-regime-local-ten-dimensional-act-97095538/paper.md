---
abstract: |
  We formulate a ten-dimensional effective action compatible with closure-strain and q79 carrier data. The metric, bundle $`M_{10}\to Y_4`$, compact fiber, field representations, and derivative expansion are declared realization inputs. The action is an ansatz on a specified regime, not the most general action and not a derivation of gravity from projection. We give the conditions under which a closure Hessian contributes to canonically normalized pole masses, a rank-one alignment projector yields one Higgs doublet, an internal operator has discrete spectrum, and a four-dimensional mode truncation is consistent. Curvature is defined through explicit connections rather than inferred from nonuniform strain. The selected q79 Fu–Yau branch is the compactification candidate, while Lens–Nil remains auxiliary. Existing finite-matrix and Standard-Model profile calculations are incorporated at their declared embedded-renormalized-SM tier; their profile inputs and imported BRST quantization are not reclassified as no-knob consequences of this action.
author:
- Peter Nero
current_version: v4
date: Corrected fourth edition July 2026
generated_from_main_tex_sha256: 691de4188702b9f5ffda4a517d5200e23a2c89832b63b67992cf68d04ba1507d
paper_id: closure-geometry-and-a-regime-local-ten-dimensional-act-97095538
release_state: zenodo_released
released_version: v4
title: |
  Closure Geometry and a Regime-Local
  Ten-Dimensional Action Ansatz
zenodo_doi: 10.5281/zenodo.21654885
zenodo_record_id: 21654885
zenodo_url: "https://zenodo.org/records/21654885"
---

# Revision note for this edition

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

One two-derivative ansatz is
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
\label{eq:action}
\end{align}
```
Here $`k_{ab}`$ and $`G_{AB}`$ must be positive on physical directions, $`\mathcal L_{H,B,\Phi}`$ records the selected flux/torsion/dilaton sector, and the gauge-fixing, ghost, and boundary terms are part of the definition of a quantized perturbative calculation.

Equation <a href="#eq:action" data-reference-type="eqref" data-reference="eq:action">[eq:action]</a> imports the Einstein–Hilbert term and a Lorentzian metric. It therefore realizes gravity; it does not derive gravity from strain or projection.

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

# Closure Hessian and physical masses

Let $`\varphi=0`$ be a stationary background for retained real fields and write the quadratic four-dimensional action after integrating the internal fiber as
``` math
S_4^{(2)}
 =\frac12\int_{Y_4}\sqrt{|g_4|}\,dd^4x
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

The condition $`\nabla S\ne0`$ says only that strain is nonparallel. It does not by itself imply nonintegrability, Riemann curvature, or the Einstein equations. Any curvature–strain coupling in <a href="#eq:action" data-reference-type="eqref" data-reference="eq:action">[eq:action]</a> must be written with an explicit connection and varied to obtain its field equations.

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

**Theorem 4** (Conditional coherent reduction). *Assume the retained mode space is invariant under all nonlinear terms to the order considered, the discarded equations vanish on the retained ansatz, the discarded linear operator has gap $`\lambda_{\rm gap}>0`$, and the nonlinear source into discarded modes obeys $`\|J_{\rm disc}\|\le\epsilon`$. Then the leading eliminated field obeys
``` math
\|\eta\|\le
 \|L_{\rm disc}^{-1}\|\,\epsilon
 \le \frac{C\epsilon}{\lambda_{\rm gap}},
```
and substituting it gives a controlled local four-dimensional effective action with the corresponding Schur–Feshbach correction.*

</div>

<div class="proof">

*Proof.* Solve the discarded equation by the inverse on the gapped complement and use the stated resolvent bound. The effective correction follows by substitution or the Schur complement. Exact consistency is the special case $`J_{\rm disc}=0`$. ◻

</div>

A spectral gap alone does not prove nonlinear invariance or exact truncation.

# Gauge fixing, anomalies, and observables

A perturbative gauge theory built from <a href="#eq:action" data-reference-type="eqref" data-reference="eq:action">[eq:action]</a> must include a common gauge-fixing, ghost, zero-mode, regulator, scale, and renormalization-scheme policy. BRST nilpotency and anomaly cancellation are equations to verify. Physical predictions require a functor from action parameters to renormalized local or scattering observables.

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

**Theorem 5** (Regime-local action statement). *Given the geometric, representation, metric, gauge-fixing, and EFT inputs of this paper, action <a href="#eq:action" data-reference-type="eqref" data-reference="eq:action">[eq:action]</a> defines a local covariant realization on the declared domain. Under compact-resolvent, alignment-projector, pole-normalization, and consistent-reduction hypotheses, it yields a discrete internal mode expansion, a selected one-doublet scalar sector, canonically defined tree-level masses, and a controlled four-dimensional effective action.*

</div>

The theorem is conditional. It does not establish uniqueness of the action, derive the metric or dimension, select the q79 vacuum, or prove the full Standard Model without the listed source and observable maps.

# Conclusion

The corrected action is a useful synthesis ansatz, not a universal derivation. Its value is that every physical promotion now has a recognizable mathematical gate: global geometry, connection, compact resolvent, scalar projector, canonical pole normalization, gauge consistency, and controlled reduction. The next decisive construction is the same-source q79 intertwiner followed by evaluation of the action’s normalized internal rows.

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

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The action written here remains a regime-local ansatz. The exact q=79, finite-action, anomaly, HYM, and internal TT packets constrain or instantiate ingredients used by the ansatz, but they do not derive its continuum action, physical normalization, or ultraviolet completion. Profile rows are retained only as cross-checks on the lower effective target.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A01/direct_k_higgs_row` (**DERIVED_EXACT**): Promoted direct K_threshold.Omega_H.lambda row.
- `A22/e6_qpsi_qcd_anomaly` (**DERIVED_EXACT**): E6 Qpsi matter/exotic QCD anomaly cancellation audit.
- `A13/gr_tt_support` (**DERIVED_EXACT**): Exact-branch internal TT support certificate; physical normalization remains open.
- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.
- `A01/qutrit_weyl_27_matrix` (**DERIVED_EXACT**): Sparse 27x27 qutrit-Weyl left-action realization.

## Corpus-state cross-checks

- `A01/charged_yukawa_higgs_profile` (**PROFILE_REPLAY**): Versioned Yu, Yd, Ye and lambda_H profile packet.
- `A14/ckm_prediction_profile` (**NUMERIC_CERTIFIED**): Three selected CKM profile rows and uncertainty comparison.
- `A01/current_global_lock` (**PROFILE_REPLAY**): Current non-looping global status and source-certificate map.
- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): Twelve-obligation embedded renormalized-SM equivalence audit.
- `A40/neutral_two_primitive_profile` (**PROFILE_REPLAY**): Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.
- `A02/precision_15_source_transport` (**PROFILE_REPLAY**): Fifteen measured source coordinates, Jacobian and covariance transport.
- `A02/precision_8x8_workspace` (**PROFILE_REPLAY**): Eight-coordinate SMDR output with positive-definite 8x8 covariance.
- `A01/strict_pew_row` (**DERIVED_EXACT**): Promoted P_EW source row at the declared one-shared-primitive standard.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

9 S. Weinberg, *The Quantum Theory of Fields, Vol. II*, Cambridge University Press, 1996.

J.-X. Fu and S.-T. Yau, *The theory of superstring with flux on non-Kahler manifolds and the complex Monge–Ampere equation*, J. Differential Geom. 78 (2008).

P. Nero, *MTT Current True SM Closure Consolidated Ledger*, internal theorem and verification packet, 2026.

</div>
