---
abstract: |
  We reassess whether the weak mixing angle provides a redundant test of the selected MTT gauge profile. Let $`r_{21}=I_2/I_1=g_1^2/g_2^2`$, with $`g_1=\sqrt{5/3}\,g_Y`$. Then $`\sin^2\theta_W=3r_{21}/(5+3r_{21})`$ at the same scale and in the same scheme. For the selected SMDR profile at $`Q=M_t`$, this gives $`\sin^2\theta_W=0.2346644\pm0.0000433`$. Because $`r_{21}`$ was itself obtained from the measured $`(g_Y,g_2)`$ profile, this equality is an exact algebraic round trip, not a held-out prediction. Supplying an absolute $`g_2`$ from $`(G_F,m_W)`$ does not remove that circularity. A genuine redundancy test requires an MTT source theorem selecting $`r_{21}`$ without electroweak gauge data, followed by independent common-scheme transport.
author:
- Peter Nero
current_version: v3
date: September 2026 (Version 3)
generated_from_main_tex_sha256: df72c2521ec994ed56fffbfac4bc6e9055a0dfeaafb498b330db5ced110b796d
paper_id: theta-closure-in-modal-triplet-theory-v-weak-angle-roun-a4083c1c
release_state: current_revised_tex
released_version: v2
title: "Theta Closure in Modal Triplet Theory V: Weak-Angle Round Trip and the Non-Circularity Criterion"
zenodo_doi: 10.5281/zenodo.21666013
zenodo_record_id: 21666013
zenodo_url: "https://zenodo.org/records/21666013"
---

# Version 3 Revision Note

Supersedes.
Version 2 of this paper; released identifiers are retained.

Reason.
The calibration boundary was present, but the selected-source owner results and their distinct scopes were not explicitly connected to it.

Resolution.
Version 3 imports the exact Gate 1, three-cycle and large-gauge-kernel conclusions through their owners, and retains the distinction between a gauge-profile round trip and a held-out test.

Retained.
The existing calibrated or conditional result, its numerical inputs and all earlier revision notes are retained.

Open boundary.
A selected physical source, its action normalization and the paper-specific execution inputs remain necessary for a held-out prediction.

# Revision note for this edition

Supersedes.
*Theta Closure in Modal Triplet Theory V: Redundant Determination from Gauge Couplings and the Weak Mixing Angle*, first edition.

Reason.
The weak angle was presented as an independent precision test even though it was algebraically reconstructed from the same measured gauge profile, and the scale used the retired few-TeV crossing.

Resolution.
Version 2 derives the same-scheme round-trip formula, propagates its uncertainty at $`Q=M_t`$, and states an explicit non-circularity criterion for any future test.

Retained result.
The weak angle remains an exact consistency identity for a supplied gauge-ratio profile.

Remaining boundary.
A held-out test requires MTT to select $`r_{21}`$ without electroweak gauge data and then transport it independently.

# Central picture and roadmap

The central picture is that the weak mixing angle describes how the neutral electroweak gauge fields are rotated into the photon and $`Z`$ directions. In a fixed renormalization scheme and at one scale, that angle is determined by the same pair of couplings $`(g_Y,g_2)`$. It is therefore not a new datum when the ratio of those couplings has already been used.

The argument has three steps:
``` math
(g_Y,g_2)
\longrightarrow
r_{21}=\frac{5g_Y^2}{3g_2^2}
\longrightarrow
s_W^2=\frac{3r_{21}}{5+3r_{21}}.
```
Section 3 proves that the composition returns $`g_Y^2/(g_Y^2+g_2^2)`$ identically. Section 4 explains why adding an absolute $`SU(2)`$ normalization does not create a second ratio. Section 5 states the data-separation conditions required for a genuine held-out test.

# Selected inputs and scope

Paper I adopts the full-Standard-Model $`\overline{\mathrm{MS}}`$ profile transported by SMDR v1.3 to
``` math
Q=M_t=172.5590883453979~\mathrm{GeV}.
```
Its relevant entries are
``` math
g_Y=0.3585945042\pm0.0000307251,
\qquad
g_2=0.6475986708\pm0.0000287665,
```
or $`g_1=\sqrt{5/3}\,g_Y`$ in GUT normalization. The associated overlap ratio is
``` math
r_{21}:=\frac{I_2}{I_1}=0.5110273\pm0.0001231.
```
Paper II realizes this ratio by calibrating its effective geometry. Paper III checks conditional compatibility of the quadratic norm. Neither paper currently supplies a value-source theorem selecting $`r_{21}`$ independently of the gauge profile.

# Same-scale weak-angle identity

The overlap convention is
``` math
\frac{1}{g_a^2}=\frac{I_a}{g_{10}^2}.
```
Therefore
``` math
\begin{equation}
r_{21}=\frac{I_2}{I_1}=\frac{g_1^2}{g_2^2}.
\label{eq:r21}
\end{equation}
```
Using $`g_Y^2=(3/5)g_1^2`$ and the $`\overline{\mathrm{MS}}`$ definition
``` math
s_W^2(Q):=\frac{g_Y^2(Q)}{g_Y^2(Q)+g_2^2(Q)},
```
gives the exact identity
``` math
\begin{equation}
\boxed{s_W^2(Q)=\frac{3r_{21}(Q)}{5+3r_{21}(Q)}.}
\label{eq:weak_identity}
\end{equation}
```

<div class="theorem">

**Theorem 1** (Gauge-profile round-trip theorem). *If $`r_{21}(Q)`$ is constructed from the same measured common-scheme pair $`(g_Y(Q),g_2(Q))`$ through Equation <a href="#eq:r21" data-reference-type="eqref" data-reference="eq:r21">[eq:r21]</a>, then evaluating Equation <a href="#eq:weak_identity" data-reference-type="eqref" data-reference="eq:weak_identity">[eq:weak_identity]</a> returns the weak angle encoded in that pair. The equality is algebraic and cannot constitute an independent prediction.*

</div>

<div class="proof">

*Proof.* Substitution of $`r_{21}=(5/3)g_Y^2/g_2^2`$ into Equation <a href="#eq:weak_identity" data-reference-type="eqref" data-reference="eq:weak_identity">[eq:weak_identity]</a> gives $`g_Y^2/(g_Y^2+g_2^2)`$ identically. ◻

</div>

For the selected ratio,
``` math
\begin{equation}
s_W^2(M_t)=0.2346644\pm0.0000433,
\end{equation}
```
where the uncertainty is propagated from the selected $`r_{21}`$ row. Direct substitution of the selected $`g_Y`$ and $`g_2`$ gives the same central value. This is a useful convention and arithmetic check, but it has no held-out status.

## Worked example and uncertainty check

As a normalization check, suppose $`g_Y=g_2`$. Then $`r_{21}=5/3`$, and Equation <a href="#eq:weak_identity" data-reference-type="eqref" data-reference="eq:weak_identity">[eq:weak_identity]</a> gives
``` math
s_W^2=\frac{3(5/3)}{5+3(5/3)}=\frac12,
```
exactly as the defining coupling formula does.

For the selected profile, inserting $`r_{21}=0.5110273`$ gives $`s_W^2=0.2346644`$. The derivative
``` math
\frac{d s_W^2}{d r_{21}}
=\frac{15}{(5+3r_{21})^2}
```
is approximately $`0.351443`$ at that point, so multiplying by the supplied ratio uncertainty $`0.0001231`$ gives $`0.0000433`$. This verifies both the central value and its one-row linear uncertainty propagation.

The interpretation is simple: the numerical agreement confirms the normalization convention and arithmetic transport. It does not create an independent electroweak datum because the same coupling ratio appears on both sides of the calculation.

# Why the $`(G_F,m_W)`$ construction remains circular

An electroweak input such as $`(G_F,m_W)`$ can set an absolute $`SU(2)`$ normalization, subject to radiative matching. It cannot make the weak-angle test independent when the ratio $`r_{21}`$ still comes from the measured hypercharge-to-$`SU(2)`$ profile. Indeed, once $`g_2`$ and $`r_{21}`$ are supplied, Equation <a href="#eq:r21" data-reference-type="eqref" data-reference="eq:r21">[eq:r21]</a> defines $`g_1`$ and hence the weak angle. The information being tested is already present in $`r_{21}`$.

At tree level the usual relation is
``` math
g_2^2=4\sqrt{2}\,G_Fm_W^2,
```
with radiative corrections required for a precision common-scheme value. This can supply the overall $`SU(2)`$ scale, but it supplies no independent value of $`g_Y/g_2`$. The latter is precisely the information already stored in $`r_{21}`$.

The earlier tree-level value near $`0.2312`$ used the obsolete $`5~\mathrm{TeV}`$ profile and a one-loop return to $`M_Z`$. It is withdrawn as a prediction. Its threshold scan also showed that the apparent precision was not stable under the stated electroweak matching variation.

# Criterion for a genuine redundant determination

A non-circular weak-angle test requires all of the following:

1.  MTT geometry selects $`r_{21}`$ without using $`g_Y`$, $`g_1`$, $`g_2`$, or $`\sin^2\theta_W`$ as value inputs;

2.  an absolute gauge normalization and matching scale are selected without using the held-out weak angle;

3.  the boundary data are transported with a declared multi-loop scheme and threshold prescription; and

4.  the resulting $`s_W^2`$ is compared with a measurement not used anywhere in selection, calibration, or branch choice.

Only then is Equation <a href="#eq:weak_identity" data-reference-type="eqref" data-reference="eq:weak_identity">[eq:weak_identity]</a> a prediction map rather than a round-trip map. Current Papers I–III satisfy the algebraic and realization parts but not the first value-source condition.

# Conclusion

The weak mixing angle is exactly consistent with the selected gauge profile, as it must be. The precise same-scale result is $`s_W^2(M_t)=0.2346644\pm0.0000433`$. This validates the hypercharge normalization and overlap-ratio bookkeeping.

It does not add an independent Standard Model observable to MTT closure. The former non-circularity claim fails because the overlap ratio already contains the measured weak-angle information. The next theorem target is sharply defined: select $`r_{21}`$ from MTT source geometry before consulting the electroweak gauge profile, then execute a held-out common-scheme comparison.

# Selected-source results and this paper’s boundary

The eta9 imports are owned contextually by *Flux Compactifications in Heterotic String Theory*, in the sections on the selected source and the integral comparison, and completed local tests and the global endpoint. Gate 1 closes the original-Jacobian campaign at all 30 groups and 225 selected columns . This is an exact finite source calculation, not the global integral meridian, the 248-coordinate readout or the analytic Deligne class $`\beta_{\mathbb C}`$.

The completed three-cycle transport has independent cycles with Gram matrix $`-2I_3`$ and zero detected affine pairings . Its scope is a non-detecting subsystem: it does not prove global triviality of the twist, and rerunning that same subsystem is not the missing detection theorem. Neither this conclusion nor the finite gate identifies an auxiliary Circle–Lens–Nil model with the physical q79 topology.

The large-gauge result is owned by *Cohesive Closure Repair and Its Hodge, Kernel, and Projection Shadows*, in its subsection on the rank-zero large-gauge kernel. It gives an injective immersion $`b_{K3}:\mathbb R^2\to\mathbb T^{20}`$ with dense nonclosed image . Rank zero counts periodic gauge identifications, not source coordinates or physical modes. It removes a kernel ambiguity without requiring numerical periods, but does not provide kinetic normalization, the selected shared-circle action or the unrelated eta9 affine lift.

For Paper V, a completed finite Jacobian calculation is not a value source for $`r_{21}`$, and the independent but non-detecting three-cycle subsystem cannot become such a source by repeating it. A dense two-parameter gauge image also does not select that ratio. The non-circularity criterion therefore still requires a source fixed before consulting the electroweak profile, including its branch, scale and normalization. This does not reopen the achieved one-shared-primitive electroweak/profile result.

The managed evidence block below retains its earlier frozen profile snapshot. Its historical source-status labels do not supersede the current exact, local and open boundaries just stated or reopen the retained hidden-HYM existence and shared-primitive Standard Model results.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The weak-angle round trip uses the electroweak source row and common-scheme precision workspaces directly, with the global profile audit fixing the comparison convention. Flavor, neutral, HYM, and finite-matrix rows are neighboring context. The non-circular zero-knob source upgrade remains open.

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

- (*profile replay*).

  Current non-looping global status and source-certificate map.

- (*profile replay*).

  Twelve-obligation embedded renormalized-SM equivalence audit.

- (*profile replay*).

  Fifteen measured source coordinates, Jacobian and covariance transport.

- (*profile replay*).

  Eight-coordinate SMDR output with positive-definite 8x8 covariance.

- (*derived exact*).

  Promoted P_EW source row at the declared one-shared-primitive standard.

= by -

#### Corpus-state cross-checks.

- (*profile replay*).

  Versioned Yu, Yd, Ye and lambda_H profile packet.

- (*numeric certified*).

  Three selected CKM profile rows and uncertainty comparison.

- (*derived exact*).

  Promoted direct K_threshold.Omega_H.lambda row.

- (*derived exact*).

  E6 Qpsi matter/exotic QCD anomaly cancellation audit.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*profile replay*).

  Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.

- (*derived exact*).

  Sparse 27x27 qutrit-Weyl left-action realization.

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

S. Navas et al. (Particle Data Group), *Review of Particle Physics*, Phys. Rev. D **110** (2024) 030001. <https://doi.org/10.1103/PhysRevD.110.030001>

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
