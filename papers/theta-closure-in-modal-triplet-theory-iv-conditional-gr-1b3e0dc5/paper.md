---
abstract: |
  We re-evaluate the propagation of the gauge-profile geometry into gravity and cosmology. Within the auxiliary six-dimensional $`S^1\times S^2\times\mathrm{Nil}_3`$ product ansatz introduced here from the auxiliary supports of Papers I–III, the updated dimensionless internal-volume coefficient is $`\widehat V_{\mathrm{int}}=20.07064R_1^3`$. Restoring the common internal length $`\ell_{\mathrm{int}}`$ gives $`G_N^{-1}=20.07064\ell_{\mathrm{int}}^6R_1^3/G_{10}`$ if that auxiliary manifold is adopted as the compactification. It is not the selected q79/Fu–Yau space, so the coefficient is an ansatz diagnostic rather than the current MTT internal volume. Even within the ansatz, the gauge profile does not determine Newton’s constant without an absolute scale and fundamental gravity normalization. A gauge matching point does not by itself select the physical cutoff $`\Lambda_\Theta`$. The correctly normalized conditional relation is $`r\leq 2\epsilon^2(\Lambda_\Theta/M_{\mathrm{Pl}})^2/(\pi^2A_s)`$ when $`H\leq\epsilon\Lambda_\Theta`$. The paper therefore supplies conditional scaling laws and an assumption audit, not cross-sector numerical closure.
author:
- Peter Nero
current_version: v3
date: September 2026 (Version 3)
generated_from_main_tex_sha256: 9b3936b512fb7a65f28744618dda412191b19c3b841c7376eff437f07937b9d6
paper_id: theta-closure-in-modal-triplet-theory-iv-conditional-gr-1b3e0dc5
release_state: current_revised_tex
released_version: v2
title: "Theta Closure in Modal Triplet Theory IV: Conditional Gravity Scaling and Cosmological Cutoff Audit"
zenodo_doi: 10.5281/zenodo.21666012
zenodo_record_id: 21666012
zenodo_url: "https://zenodo.org/records/21666012"
---

# Version 3 Revision Note

Supersedes.
Version 2 of this paper; released identifiers are retained.

Reason.
The calibration boundary was present, but the selected-source owner results and their distinct scopes were not explicitly connected to it.

Resolution.
Version 3 imports the exact Gate 1, three-cycle and large-gauge-kernel conclusions through their owners, and retains the independent absolute-scale and cosmological inputs.

Retained.
The existing calibrated or conditional result, its numerical inputs and all earlier revision notes are retained.

Open boundary.
A selected physical source, its action normalization and the paper-specific execution inputs remain necessary for a held-out prediction.

# Revision note for this edition

Supersedes.
*Theta Closure in Modal Triplet Theory IV: Gravity and Cosmology from the Closure Scale*, first edition.

Reason.
A dimensionless auxiliary volume and the obsolete few-TeV gauge crossing were promoted into Newton and primordial-tensor estimates without an absolute length, $`G_{10}`$, or selected physical compactification.

Resolution.
Version 2 restores dimensions, confines the coefficient $`20.07064R_1^3`$ to the auxiliary $`S^1\times S^2\times\mathrm{Nil}_3`$ ansatz, and withdraws the numerical tensor claim.

Retained result.
The dimensional-reduction and cutoff inequalities survive as conditional scaling relations.

Remaining boundary.
A q79/Fu–Yau volume, absolute scale, gravity normalization, and cosmological solution must be selected independently.

# Introduction

Papers I–III now establish a selected common-scheme gauge profile, a calibrated leading geometric realization, and a conditional twistor representation check. They do not select an absolute internal length, a fundamental ten-dimensional gravitational coupling, or a cosmological coherence cutoff. This distinction controls what can be transported into the gravity and cosmology sectors.

This paper asks two scoped questions. First, what dimensionless auxiliary volume coefficient follows if the effective round-$`S^2`$/nilmanifold product ansatz is used? Second, what tensor inequality follows if a separately selected coherence cutoff bounds the Hubble scale? The answers are conditional scaling relations. They must not be promoted into predictions of $`G_N`$ or $`r`$ until the missing absolute-scale and cutoff source theorems are supplied.

# Central picture and dependency flow

The central picture is dimensional analysis with two independent exits. Gauge ratios can constrain dimensionless shape data, but Newton’s constant also depends on an absolute internal length and the higher-dimensional gravitational normalization. Likewise, a renormalization scale used to quote gauge couplings is not a physical ultraviolet or coherence cutoff.

The two calculations therefore have the form
``` math
\begin{gathered}
\text{calibrated auxiliary shape}
\longrightarrow
\widehat V_{\mathrm{aux}}
\quad+\quad
\{\ell_{\mathrm{int}},G_{10}\}
\longrightarrow G_N,\\
\{\Lambda_\Theta,\epsilon,\text{cosmological state}\}
\longrightarrow r\text{ bound}.
\end{gathered}
```
The first line is evaluated in Section 3 and the second in Section 4. In both lines the braces contain inputs that the gauge-profile calculation does not select.

# Auxiliary volume and conditional Newton scaling

We compute the gravity scaling implied by the auxiliary effective product ansatz. The calculation introduces no retuning of the dimensionless profile, but it retains the independent absolute length $`\ell_{\mathrm{int}}`$ and fundamental coupling $`G_{10}`$.

## Gravitational coupling in Modal Triplet Theory

In Modal Triplet Theory, the effective four–dimensional gravitational coupling arises from dimensional reduction of the higher–dimensional coherent sector. At leading order this takes the form
``` math
\begin{equation}
\frac{1}{G_N}
=
\frac{\mathrm{Vol}(X_{\mathrm{int}})}{G_{10}},
\label{eq:GN_reduction}
\end{equation}
```
where:

- $`G_{10}`$ is the fundamental gravitational coupling of the modal theory,

- $`X_{\mathrm{int}}`$ is the internal coherent space.

Equation <a href="#eq:GN_reduction" data-reference-type="eqref" data-reference="eq:GN_reduction">[eq:GN_reduction]</a> is the standard unwarped dimensional-reduction form assumed here . Its applicability to MTT requires the product metric, Einstein-frame convention, and absence or control of warp/dilaton corrections.

## Internal volume in terms of $`\Theta`$

Define the auxiliary six-dimensional product
``` math
\begin{equation}
X_{\mathrm{aux}}
=
S^1_{\mathrm{cen}} \times \Sigma_2 \times \Sigma_3,
\end{equation}
```
where:

- $`S^1_{\mathrm{cen}}`$ is the central circle of radius $`R_1`$,

- $`\Sigma_2`$ is the lens layer,

- $`\Sigma_3`$ is the color layer $`\Gamma\backslash\mathrm{Nil}_3`$.

Here $`\Sigma_2`$ is the two-dimensional effective lens base, not the three-dimensional lens space. Thus the dimension is $`1+2+3=6`$. This is a declared auxiliary coordinate model. In the general MTT carrier the shared circle is common $`U(1)`$ phase/holonomy data and need not be an independent product coordinate; the current q79/Fu–Yau compactification is a different global manifold.

After factoring out a common physical length $`\ell_{\mathrm{int}}`$, write the remaining radii and metric parameters as dimensionless quantities. Under the unwarped product ansatz the auxiliary volume factorizes as
``` math
\begin{equation}
\mathrm{Vol}(X_{\mathrm{aux}})
=
\ell_{\mathrm{int}}^6(2\pi R_1)\;
\widehat{\mathrm{Area}}(\Sigma_2)\;
\widehat{\mathrm{Vol}}(\Sigma_3).
\label{eq:internal_volume_factorized}
\end{equation}
```

## Insertion of the calibrated gauge-profile geometry

Paper II’s calibrated leading ansatz gives the dimensionless relations
``` math
\begin{align}
\widehat{\mathrm{Area}}(\Sigma_2)
&=4\pi(f_2R_{\mathrm{lens}})^2
=4\pi(0.2555137R_1),\\
\widehat{\mathrm{Vol}}(\Sigma_3)&=c=0.9948493R_1,
\qquad (a=b=1).
\end{align}
```
These are profile-realization data, not an independent gravity-sector selection. Substitution gives
``` math
\begin{align}
\widehat V_{\mathrm{int}}
&=(2\pi R_1)\,[4\pi(0.2555137R_1)]\,(0.9948493R_1)\\
&=20.0706400R_1^3,
\end{align}
```
and therefore
``` math
\begin{equation}
\boxed{\mathrm{Vol}(X_{\mathrm{aux}})
=20.0706400\,\ell_{\mathrm{int}}^6R_1^3.}
\label{eq:volume_result}
\end{equation}
```

## Conditional expression for $`G_N`$

If, in addition to the dimensional-reduction assumptions, one identifies the physical internal space with $`X_{\mathrm{aux}}`$, then
``` math
\begin{equation}
\boxed{\frac{1}{G_N}
=\frac{20.0706400\,\ell_{\mathrm{int}}^6R_1^3}{G_{10}}.}
\label{eq:GN_theta}
\end{equation}
```
The gauge profile fixes only the displayed dimensionless shape coefficient within the chosen ansatz. It does not fix $`\ell_{\mathrm{int}}^6/G_{10}`$, this paper does not derive the reduction formula from a selected MTT action, and the required identification $`X_{\mathrm{int}}=X_{\mathrm{aux}}`$ is not established. Thus no numerical prediction of Newton’s constant follows.

## Worked example and interpretation: one shape, an unresolved scale family

Set $`R_1=1`$ inside the auxiliary model. The gauge-profile calibration then fixes only
``` math
\widehat V_{\mathrm{aux}}=20.0706400,
\qquad
\frac{1}{G_N}
=20.0706400\,\frac{\ell_{\mathrm{int}}^6}{G_{10}}.
```
For any $`s>0`$, the simultaneous change
``` math
\ell_{\mathrm{int}}\longmapsto s\ell_{\mathrm{int}},
\qquad
G_{10}\longmapsto s^6G_{10}
```
leaves $`G_N`$ unchanged. Conversely, holding $`G_{10}`$ fixed while changing $`\ell_{\mathrm{int}}`$ changes the predicted Newton constant by the sixth power. This explicit degeneracy is why a dimensionless overlap fit cannot determine four-dimensional gravity without an absolute-scale theorem.

# Conditional cosmological cutoff relation

The old gauge crossing did not select a physical coherence cutoff. In particular, the former assignment $`\Lambda_\Theta\sim5~\mathrm{TeV}`$ and the scan $`[3,10]~\mathrm{TeV}`$ are withdrawn. The current gauge matching point $`Q=M_t`$ is a renormalization convention and must not be identified with $`\Lambda_\Theta`$.

Let a future source theorem select a physical cutoff $`\Lambda_\Theta`$, and suppose the relevant cosmological solution satisfies the quantitative admissibility condition
``` math
\begin{equation}
H\leq\epsilon\Lambda_\Theta,
\qquad 0<\epsilon<1.
\label{eq:admissibility_H}
\end{equation}
```
For vacuum tensor fluctuations in standard slow-roll normalization ,
``` math
\begin{equation}
P_t=\frac{2H^2}{\pi^2M_{\mathrm{Pl}}^2},
\qquad r=\frac{P_t}{A_s}.
\end{equation}
```
Here $`M_{\mathrm{Pl}}=(8\pi G_N)^{-1/2}`$ is the reduced Planck mass and $`A_s`$ is the scalar curvature-perturbation amplitude in the same convention. Consequently,
``` math
\begin{equation}
\boxed{r\leq
\frac{2\epsilon^2}{\pi^2A_s}
\left(\frac{\Lambda_\Theta}{M_{\mathrm{Pl}}}\right)^2.}
\label{eq:r_bound_general}
\end{equation}
```
This corrects the legacy formula, which omitted the factor $`2/(\pi^2A_s)`$. Equation <a href="#eq:r_bound_general" data-reference-type="eqref" data-reference="eq:r_bound_general">[eq:r_bound_general]</a> remains conditional on the tensor-production model as well as on independently selected values of $`\Lambda_\Theta`$ and $`\epsilon`$. It supplies no current numerical bound.

# Status and falsifiability

The conditional relation <a href="#eq:r_bound_general" data-reference-type="eqref" data-reference="eq:r_bound_general">[eq:r_bound_general]</a> can become falsifiable only after MTT independently selects a cutoff, an admissibility margin, and a cosmological production law. A measured tensor amplitude could then test that joint hypothesis. Without those selections, neither detection nor non-detection of primordial tensors presently falsifies the gauge-profile closure program. The withdrawn $`10^{-30}`$–$`10^{-29}`$ interval must not be quoted as an MTT prediction.

# Conclusion

Within the auxiliary product ansatz, the updated gauge profile fixes the dimensionless ansatz-volume coefficient to $`20.0706400R_1^3`$. Restoring dimensions shows explicitly why this is not yet a prediction of Newton’s constant: the independent combination $`\ell_{\mathrm{int}}^6/G_{10}`$ remains, and no theorem identifies $`X_{\mathrm{aux}}`$ with the selected q79/Fu–Yau compactification.

The cosmological result is likewise a conditional scaling law. The obsolete few-TeV gauge crossing cannot serve as a physical coherence cutoff, and the legacy numerical tensor bound is withdrawn. A future closure theorem must select $`\Lambda_\Theta`$, the quantitative margin $`\epsilon`$, and the applicable cosmological state before Equation <a href="#eq:r_bound_general" data-reference-type="eqref" data-reference="eq:r_bound_general">[eq:r_bound_general]</a> becomes a numerical prediction. Paper IV therefore documents cross-sector dependencies and correct formulas; it does not establish gravity or cosmology closure.

# Selected-source results and this paper’s boundary

The eta9 imports are owned contextually by *Flux Compactifications in Heterotic String Theory*, in the sections on the selected source and the integral comparison, and completed local tests and the global endpoint. Gate 1 closes the original-Jacobian campaign at all 30 groups and 225 selected columns . This is an exact finite source calculation, not the global integral meridian, the 248-coordinate readout or the analytic Deligne class $`\beta_{\mathbb C}`$.

The completed three-cycle transport has independent cycles with Gram matrix $`-2I_3`$ and zero detected affine pairings . Its scope is a non-detecting subsystem: it does not prove global triviality of the twist, and rerunning that same subsystem is not the missing detection theorem. Neither this conclusion nor the finite gate identifies an auxiliary Circle–Lens–Nil model with the physical q79 topology.

The large-gauge result is owned by *Cohesive Closure Repair and Its Hodge, Kernel, and Projection Shadows*, in its subsection on the rank-zero large-gauge kernel. It gives an injective immersion $`b_{K3}:\mathbb R^2\to\mathbb T^{20}`$ with dense nonclosed image . Rank zero counts periodic gauge identifications, not source coordinates or physical modes. It removes a kernel ambiguity without requiring numerical periods, but does not provide kinetic normalization, the selected shared-circle action or the unrelated eta9 affine lift.

For Paper IV, these theorems neither supply the q79 volume nor determine $`\ell_{\mathrm{int}}`$, $`G_{10}`$ or a cosmological state. The auxiliary product used here is an additional diagnostic ansatz, not a consequence of the operator supports in Papers I–III. No rank, kernel or transport certificate turns the matching convention $`Q=M_t`$ into a physical cutoff. The conditional Newton scaling and tensor inequality keep their stated independent inputs.

The managed evidence block below retains its earlier frozen profile snapshot. Its historical source-status labels do not supersede the current exact, local and open boundaries just stated or reopen the retained hidden-HYM existence and shared-primitive Standard Model results.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

This paper audits possible gravity and cosmology scaling from gauge-profile geometry. None of the mapped Standard Model packets derives a physical gravitational normalization or cosmological cutoff, so all closed rows below are corpus-state cross-checks rather than direct proof. The strict upgrade remains open.

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

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*profile replay*).

  Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.

- (*profile replay*).

  Fifteen measured source coordinates, Jacobian and covariance transport.

- (*profile replay*).

  Eight-coordinate SMDR output with positive-definite 8x8 covariance.

- (*derived exact*).

  Sparse 27x27 qutrit-Weyl left-action realization.

- (*derived exact*).

  Promoted P_EW source row at the declared one-shared-primitive standard.

= by -

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<div class="thebibliography">

99

P. Nero, *Selected eta9 original-Jacobian Gate 1 campaign* (2026). Frozen source at curated manifest commit `f141a20e a23c5c3f f19cc216 1c0e226e 29ade8a7`: [source artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/eta9_gate1_campaign/artifact.json).

P. Nero, *Complete selected three-cycle non-detection decision* (2026). Frozen source at curated manifest commit `f141a20e a23c5c3f f19cc216 1c0e226e 29ade8a7`: [source artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/eta9_three_cycle_b96_nondetection/artifact.json).

P. Nero, *Selected K3 rank-zero large-gauge kernel* (2026). Frozen source at curated manifest commit `f141a20e a23c5c3f f19cc216 1c0e226e 29ade8a7`: [source artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_bk3_rank_zero_kernel/artifact.json).

M. J. Duff, B. E. W. Nilsson, and C. N. Pope, *Kaluza–Klein supergravity*, Physics Reports **130** (1986) 1–142. <https://doi.org/10.1016/0370-1573(86)90163-8>

D. Baumann, *TASI lectures on inflation*, <https://arxiv.org/abs/0907.5424>

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

P. Nero, *Modal Triplet Theory and History-Dependent Stochastic Processes: Fixed-State Indivisibility, Markov Order, and the Quantum Boundary*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18254862>

</div>
