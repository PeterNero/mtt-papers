---
abstract: |
  We reassess whether the weak mixing angle provides a redundant test of the selected MTT gauge profile. Let $`r_{21}=I_2/I_1=g_1^2/g_2^2`$, with $`g_1=\sqrt{5/3}\,g_Y`$. Then $`\sin^2\theta_W=3r_{21}/(5+3r_{21})`$ at the same scale and in the same scheme. For the selected SMDR profile at $`Q=M_t`$, this gives $`\sin^2\theta_W=0.2346644\pm0.0000433`$. Because $`r_{21}`$ was itself obtained from the measured $`(g_Y,g_2)`$ profile, this equality is an exact algebraic round trip, not a held-out prediction. Supplying an absolute $`g_2`$ from $`(G_F,m_W)`$ does not remove that circularity. A genuine redundancy test requires an MTT source theorem selecting $`r_{21}`$ without electroweak gauge data, followed by independent common-scheme transport. The obsolete one-loop $`5~\mathrm{TeV}`$ calculation and its precision-prediction claim are withdrawn.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 733bd0c5287818b91a87c6c965ced61b540a04f54f9dcf7f381d72d0681c641c
paper_id: theta-closure-in-modal-triplet-theory-v-weak-angle-roun-a4083c1c
release_state: zenodo_released
released_version: v1.0
title: "Theta Closure in Modal Triplet Theory V: Weak-Angle Round Trip and the Non-Circularity Criterion"
zenodo_doi: 10.5281/zenodo.18262146
zenodo_record_id: 18262146
zenodo_url: "https://zenodo.org/records/18262146"
---

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

# Why the $`(G_F,m_W)`$ construction remains circular

An electroweak input such as $`(G_F,m_W)`$ can set an absolute $`SU(2)`$ normalization, subject to radiative matching. It cannot make the weak-angle test independent when the ratio $`r_{21}`$ still comes from the measured hypercharge-to-$`SU(2)`$ profile. Indeed, once $`g_2`$ and $`r_{21}`$ are supplied, Equation <a href="#eq:r21" data-reference-type="eqref" data-reference="eq:r21">[eq:r21]</a> defines $`g_1`$ and hence the weak angle. The information being tested is already present in $`r_{21}`$.

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

# References

1.  Particle Data Group (PDG), *Review of Particle Physics*, Prog. Theor. Exp. Phys. 2024, 083C01 (for $`G_F`$, $`m_W`$, $`M_Z`$, and electroweak input values).

2.  M. E. Machacek and M. T. Vaughn, “Two-loop renormalization group equations in a general quantum field theory,” Nucl. Phys. B222 (1983) 83–103.

3.  T. Kato, *Perturbation Theory for Linear Operators*, Springer (1995).

4.  P. Nero, *Modal Triplet Theory: Foundation*, MTT corpus.

5.  P. Nero, *Modal Triplet Theory: Quantum Amplitudes from Modal Geometry*, MTT corpus.

6.  P. Nero, *Gauge Couplings, Internal Geometry, and $`\Theta`$–Closure in Modal Triplet Theory*, Paper I.

7.  P. Nero, *Direct Geometric Evaluation of Nonabelian Overlaps in Modal Triplet Theory*, Paper II.

8.  P. Nero, *Twistor–Action Matching of Gauge Overlaps in Modal Triplet Theory*, Paper III.

9.  P. Nero, *Extending $`\Theta`$–Closure to Gravity and Cosmology in Modal Triplet Theory*, Paper IV.

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
