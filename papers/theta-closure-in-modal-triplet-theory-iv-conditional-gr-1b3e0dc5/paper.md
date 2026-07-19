---
abstract: |
  We re-evaluate the propagation of the gauge-profile geometry into gravity and cosmology. Within the auxiliary six-dimensional $`S^1\times S^2\times\mathrm{Nil}_3`$ product ansatz of Papers I–III, the updated dimensionless internal-volume coefficient is $`\widehat V_{\mathrm{int}}=20.07064R_1^3`$. Restoring the common internal length $`\ell_{\mathrm{int}}`$ gives $`G_N^{-1}=20.07064\ell_{\mathrm{int}}^6R_1^3/G_{10}`$ if that auxiliary manifold is adopted as the compactification. It is not the selected q79/Fu–Yau space, so the coefficient is an ansatz diagnostic rather than the current MTT internal volume. Even within the ansatz, the gauge profile does not determine Newton’s constant without an absolute scale and fundamental gravity normalization. The former identification $`\Lambda_\Theta\sim5~\mathrm{TeV}`$ is withdrawn with the obsolete gauge crossing, so its numerical primordial-tensor bound is also withdrawn. We retain the correctly normalized conditional relation $`r\leq 2\epsilon^2(\Lambda_\Theta/M_{\mathrm{Pl}})^2/(\pi^2A_s)`$ when $`H\leq\epsilon\Lambda_\Theta`$. The paper therefore supplies conditional scaling laws and an assumption audit, not cross-sector numerical closure.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: b32468bf9b6f804e661cc9fe79fdba912c304d8d17c5335aa276d38692fbbbb7
paper_id: theta-closure-in-modal-triplet-theory-iv-conditional-gr-1b3e0dc5
release_state: zenodo_released
released_version: v1.0
title: "Theta Closure in Modal Triplet Theory IV: Conditional Gravity Scaling and Cosmological Cutoff Audit"
zenodo_doi: 10.5281/zenodo.18262122
zenodo_record_id: 18262122
zenodo_url: "https://zenodo.org/records/18262122"
---

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

# Propagation of $`\Theta`$ to Newton’s constant

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

Equation <a href="#eq:GN_reduction" data-reference-type="eqref" data-reference="eq:GN_reduction">[eq:GN_reduction]</a> is the standard dimensional-reduction form assumed here. Its applicability to MTT requires the product metric, Einstein-frame convention, and absence or control of warp/dilaton corrections.

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
For vacuum tensor fluctuations in standard slow-roll normalization,
``` math
\begin{equation}
P_t=\frac{2H^2}{\pi^2M_{\mathrm{Pl}}^2},
\qquad r=\frac{P_t}{A_s}.
\end{equation}
```
Consequently,
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

# References

1.  Particle Data Group (PDG), *Review of Particle Physics*, for Standard Model input parameters and cosmological conventions.

2.  M. E. Machacek and M. T. Vaughn, “Two-loop renormalization group equations in a general quantum field theory,” Nucl. Phys. B222 (1983) 83–103.

3.  T. Kato, *Perturbation Theory for Linear Operators*, Springer (1995).

4.  P. Nero, *Modal Triplet Theory: Foundation*, MTT corpus.

5.  P. Nero, *Modal Triplet Theory: Quantum Amplitudes from Modal Geometry*, MTT corpus.

6.  P. Nero, *Direct Geometric Evaluation of Nonabelian Overlaps in Modal Triplet Theory*, Paper II.

7.  P. Nero, *Twistor–Action Matching of Gauge Overlaps in Modal Triplet Theory*, Paper III.

8.  R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 2, Cambridge University Press (for twistor geometry background).

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
