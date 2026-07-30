---
abstract: |
  We separate the geometry-light statements of MTT into exact algebraic identities, consequences of explicit symmetry or positivity assumptions, and phenomenological estimates requiring additional dynamics. Modal democracy implies $`\sin^2\theta_W=3/8`$, but democracy is an assumption and is not selected by the current gauge profile. Holonomy phase sums require a specified trivial tensor product and compatible connection. Equal propagation speeds require equality of principal symbols and do not follow from topology alone. Curvature–mass drift is an identity conditional on a chosen mass–curvature ansatz, while the PPN statement requires an explicit response-norm estimate. No internal spectral gap is identified with an external cutoff. These typed statements provide safe interfaces for later numerical tiers without overstating their physical content.
author:
- Peter Nero
current_version: v3
date: July 2026 Version 3
generated_from_main_tex_sha256: c49eddc050691fb2225c219e5772bf165cce4617c2908b469d55ed9c559b608c
paper_id: geometry-light-relations-in-modal-triplet-theory-exact-1a5eeb7e
release_state: zenodo_released
released_version: v3
title: |
  Geometry–Light Relations in Modal Triplet Theory:
  Exact Identities, Conditional Bounds, and Principal Symbols
zenodo_doi: 10.5281/zenodo.21665977
zenodo_record_id: 21665977
zenodo_url: "https://zenodo.org/records/21665977"
---

# Version 3 Revision Note

Supersedes
*Geometry–Light Relations in Modal Triplet Theory*, version 2.

Reason
Algebraic identities, symmetry assumptions, topology, spectral gaps, propagation speeds, and phenomenological bounds were not consistently separated by logical strength.

Resolution
Version 3 types each statement as exact, conditional, or phenomenological, moves causal speed to principal symbols, and separates internal gaps from external cutoffs.

Retained result
Modal-democracy, holonomy, curvature–mass, and PPN relations remain valid in precisely the displayed conditional forms.

Remaining boundary
Physical light propagation and quantitative bounds require a selected hyperbolic action, response map, and normalization.

# Classification rule

A relation is called *exact* only when it follows algebraically from its displayed definitions. A *conditional theorem* additionally lists every symmetry, bundle, principal-symbol, positivity, or response assumption. A *phenomenological bound* also requires a selected physical normalization and comparison scheme. Geometry-light does not mean assumption-free.

# Gauge-weight identity and modal democracy

At one common scale and in one scheme, write
``` math
\alpha_r^{-1}=K\zeta_r,
\qquad \zeta_r>0,
```
and use $`g_Y^2=(3/5)g_1^2`$. Then the exact algebraic identity is
``` math
\begin{equation}
\boxed{\sin^2\theta_W
=\frac{1}{1+(5/3)(\zeta_1/\zeta_2)}.}
\label{eq:weak-general}
\end{equation}
```

<div class="definition">

**Definition 1** (Modal democracy). Modal democracy at the chosen scale means $`\zeta_1=\zeta_2`$.

</div>

<div class="corollary">

**Corollary 2** (Conditional democracy value). *If modal democracy holds, Equation <a href="#eq:weak-general" data-reference-type="eqref" data-reference="eq:weak-general">[eq:weak-general]</a> gives $`\sin^2\theta_W=3/8`$.*

</div>

This is exact given democracy, but democracy is not derived by this paper and is not satisfied by the selected low-scale SMDR profile. The value $`3/8`$ is therefore neither a current MTT weak-angle prediction nor evidence for a physical matching scale. For $`\zeta_1/\zeta_2=1+\varepsilon`$, the Taylor identity is
``` math
\sin^2\theta_W=\frac38\left(1-\frac58\varepsilon
+\frac{25}{64}\varepsilon^2+O(\varepsilon^3)\right).
```

# Conditional holonomy phase sum

<div class="theorem">

**Theorem 3** (Holonomy product under compatible trivialization). *Let $`L_{12},L_{23},L_{31}`$ be line bundles equipped with unitary connections. Assume a specified connection-preserving trivialization
``` math
L_{12}\otimes L_{23}\otimes L_{31}\cong\underline{\mathbb C}.
```
Then for every closed loop $`\gamma`$,
``` math
U_{12}(\gamma)U_{23}(\gamma)U_{31}(\gamma)=1,
```
and the three phases sum to an integer multiple of $`2\pi`$.*

</div>

<div class="proof">

*Proof.* The tensor-product connection is trivial by assumption, so its holonomy is unity. Holonomy on a tensor product is the product of the three line-bundle holonomies. ◻

</div>

Topological triviality alone does not force an arbitrary chosen product connection to have zero holonomy. The compatible trivialization is an essential hypothesis. The theorem constrains phase sums but does not select CKM or PMNS phases individually.

# Principal-symbol condition for propagation speeds

For a linearized field component $`\phi_a`$, let the second-order operator have principal symbol
``` math
\sigma_2(P_a)(x,\xi)=G_a^{\mu\nu}(x)\xi_\mu\xi_\nu.
```

<div class="theorem">

**Theorem 4** (Common characteristic cone). *Two canonically normalized sectors have the same local high-frequency propagation cone if and only if their nondegenerate principal symbols define the same null cone. In dimension at least three this means $`G_b^{\mu\nu}=\Omega^2G_a^{\mu\nu}`$ for a positive conformal factor, subject to the usual regularity assumptions.*

</div>

Lower-order masses, potentials, projectors, or internal overlap coefficients do not determine the characteristic cone. Equal wave speeds therefore require a common principal-symbol theorem; they cannot be inferred solely from bundle topology, modal counting, or an internal spectral gap.

# Representation-only RG signs

Conditional on importing the Standard Model field content and perturbative quantization, the one-loop coefficient, written as sums over Dirac fermions and real scalars, is
``` math
b_0=\frac{11}{3}C_A-\frac{4}{3}\sum_{\rm Dirac}T(R_f)
-\frac{1}{6}\sum_{\rm real}T(R_s).
```
Equivalently, without pairing fields,
``` math
b_0=\frac{11}{3}C_A-\frac{2}{3}\sum_{\rm Weyl}T(R_f)
-\frac{1}{3}\sum_{\rm complex}T(R_s).
```
These conventions give the same coefficient and fix the qualitative signs of the gauge beta functions. This is a standard QFT consequence of representation content, not a new geometric prediction of MTT. Quantitative running uses the selected multi-loop transport rather than this sign-level approximation.

# Conditional curvature–mass drift

Assume, rather than derive, the local ansatz
``` math
m(x)=\sqrt{\kappa(\lambda^{(0)}+\beta R(x))},
\qquad \lambda^{(0)}+\beta R(x)>0.
```
Then differentiation gives the exact identity
``` math
\nabla_\mu\log m
=\frac{\beta\nabla_\mu R}{2(\lambda^{(0)}+\beta R)}.
```
If the denominator is bounded below by $`\lambda_{\min}>0`$, then
``` math
|\nabla_\mu\log m|
\leq\frac{|\beta|}{2\lambda_{\min}}|\nabla_\mu R|.
```
The calculus is exact, but the mass ansatz, $`\beta`$, and physical-unit bridge are independent inputs. This is not a prediction of cosmological mass drift.

# Conditional PPN estimate

Suppose a linearized gravitational equation can be written
``` math
\square\bar h_{\mu\nu}=-16\pi G_NT_{\mu\nu}+S_{\mu\nu}
```
and a specified solution norm obeys
``` math
\|S\|\leq C\Delta_{\mathrm{curv}}\|T\|.
```
Only under a stable inverse estimate for the gauge-fixed operator does this imply a bound of the form
``` math
|\gamma-1|\leq C_{\mathrm{PPN}}\Delta_{\mathrm{curv}}.
```
The constants and norm must be computed for the selected background and source. Writing merely $`\gamma=1+O(\Delta_{\mathrm{curv}})`$ is an asymptotic template, not a numerical solar-system prediction.

# No internal-gap cutoff inference

An internal Laplacian gap controls suppression of omitted internal modes in a specified reduction. It does not by itself define a four-dimensional UV, coherence, inflationary, or cosmological cutoff. Any such identification needs a dimensionful bridge, an action-level decoupling theorem, and an error bound. The common SMDR point $`Q=M_t`$ is likewise a matching convention rather than a physical cutoff.

# Discussion and proper use

These relations are best used as interface tests. A selected gauge construction may be checked against Equation <a href="#eq:weak-general" data-reference-type="eqref" data-reference="eq:weak-general">[eq:weak-general]</a>, but agreement does not select modal democracy. A selected bundle connection may be checked against the holonomy product, but topological triviality does not supply the required parallel trivialization. A selected gravitational action may be checked for a common photon/graviton cone, but internal rank or spectral data do not supply its principal symbol.

The same distinction controls numerical interpretation. Substituting a measured scale or fitted response coefficient demonstrates compatibility. It becomes a prediction only when the scale, coefficient, and branch were selected without the target observable. Geometry-light formulas are therefore valuable consistency checks and error-detection tools even when they are not source theorems.

# Conclusion

The geometry-light tier contains useful exact relations, but their scope is now explicit. The weak-angle and curvature formulas are algebraic identities conditional on stated ansatz data; holonomy phases require a compatible trivialization; wave-speed equality is a principal-symbol question; RG signs are imported Standard Model QFT; and PPN control needs a quantitative response estimate. These statements can constrain later constructions without being misreported as source-derived numerical predictions.

#### Rows used directly in this paper.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*profile replay*).

  Fifteen measured source coordinates, Jacobian and covariance transport.

- (*profile replay*).

  Eight-coordinate SMDR output with positive-definite 8x8 covariance.

- (*derived exact*).

  Sparse 27x27 qutrit-Weyl left-action realization.

- (*derived exact*).

  Promoted P_EW source row at the declared one-shared-primitive standard.

= by -

#### Corpus-state cross-checks.

- (*profile replay*).

  Versioned Yu, Yd, Ye and lambda_H profile packet.

- (*numeric certified*).

  Three selected CKM profile rows and uncertainty comparison.

- (*profile replay*).

  Current non-looping global status and source-certificate map.

- (*derived exact*).

  Promoted direct K_threshold.Omega_H.lambda row.

- (*derived exact*).

  E6 Qpsi matter/exotic QCD anomaly cancellation audit.

- (*profile replay*).

  Twelve-obligation embedded renormalized-SM equivalence audit.

- (*profile replay*).

  Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.

= by -

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The paper's exact geometry-light identities are proved locally. The HYM, precision, finite-matrix, and electroweak rows instantiate selected computational examples; the remaining flavor and global-closure rows are cross-checks and do not strengthen the local theorem tier. The zero-knob upgrade remains open.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A02/precision_15_source_transport` (**PROFILE_REPLAY**): Fifteen measured source coordinates, Jacobian and covariance transport.
- `A02/precision_8x8_workspace` (**PROFILE_REPLAY**): Eight-coordinate SMDR output with positive-definite 8x8 covariance.
- `A01/qutrit_weyl_27_matrix` (**DERIVED_EXACT**): Sparse 27x27 qutrit-Weyl left-action realization.
- `A01/strict_pew_row` (**DERIVED_EXACT**): Promoted P_EW source row at the declared one-shared-primitive standard.

## Corpus-state cross-checks

- `A01/charged_yukawa_higgs_profile` (**PROFILE_REPLAY**): Versioned Yu, Yd, Ye and lambda_H profile packet.
- `A14/ckm_prediction_profile` (**NUMERIC_CERTIFIED**): Three selected CKM profile rows and uncertainty comparison.
- `A01/current_global_lock` (**PROFILE_REPLAY**): Current non-looping global status and source-certificate map.
- `A01/direct_k_higgs_row` (**DERIVED_EXACT**): Promoted direct K_threshold.Omega_H.lambda row.
- `A22/e6_qpsi_qcd_anomaly` (**DERIVED_EXACT**): E6 Qpsi matter/exotic QCD anomaly cancellation audit.
- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): Twelve-obligation embedded renormalized-SM equivalence audit.
- `A40/neutral_two_primitive_profile` (**PROFILE_REPLAY**): Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255621>

P. Nero, *Modal Triplet Theory: Foundation*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.16949762>

P. Nero, *Fixed Points I–VI: Complete Coherence Spine*, Zenodo preprints, August 2025. <https://doi.org/10.5281/zenodo.16948748>

P. Nero, *The Projection–Admissibility Principle: Structural Constraints on Effective Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255838>

P. Nero, *Closure and Inevitability in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255510>

P. Nero, *Coherence Capacity as the Fundamental Resource of Effective Physics*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255905>

P. Nero, *Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256048>

P. Nero, *Modal Triplet Theory: From MTT to Quantum Mechanics*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.17074246>

P. Nero, *From MTT to Quantum Field Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17068816>

P. Nero, *Modal Triplet Theory: From MTT to General Relativity*, Zenodo preprint, October 2025. <https://doi.org/10.5281/zenodo.16950597>

P. Nero, *Modal Triplet Theory: From MTT to a UV-Finite, Unitary Quantum Gravity*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17077671>

P. Nero, *Measurement as Disturbance and Stabilization in Modal Triplet Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17177404>

P. Nero, *Projection, Probability, and Irreversibility: Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256408>

P. Nero, *Modal Fixed Points, Bell’s Beables, and the Limits of Factorization*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17076300>

P. Nero, *Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory*, Zenodo preprint, August 2025. <https://doi.org/10.5281/zenodo.18208884>

P. Nero, *From Modal Triplet Theory to Indivisible Stochastic Processes: A First-Principles, Fully Rigorous Derivation*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18254862>

</div>
