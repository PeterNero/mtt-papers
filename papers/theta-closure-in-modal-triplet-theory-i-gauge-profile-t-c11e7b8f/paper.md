---
abstract: |
  We present a conditional $`\Theta`$–closure realization relating Standard Model gauge couplings to internal geometric overlap integrals. Measured source data are transported with SMDR v1.3 into the full-Standard-Model $`\overline{\mathrm{MS}}`$ scheme at $`Q=M_t`$. In the normalization used here, the resulting profile targets are
  ``` math
  I_2/I_1=0.5110273\pm0.0001231,\qquad
   I_3/I_1=0.158335\pm0.001098.
  ```
  They are calibrated profile coordinates, not first-principles predictions of the gauge couplings. We formulate the admissibility and spectral-gap conditions under which an internal realization may reproduce these targets. To address the normalization of nonabelian harmonics, we introduce a high–coherence (twistor) corner with declared period and gauge-kinetic normalizations. An $`O(\lambda_Q^{-1})`$ overlap estimate is conditional on explicit projector and representative perturbation bounds. The old $`4.2`$–$`5~\mathrm{TeV}`$ crossing and its identification with a physical coherence, gap, or quantum-gravity scale are withdrawn. The scale $`Q=M_t`$ is a renormalization and matching convention only. Explicit geometric realization must therefore be re-executed against the new target pair.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 4a742c599fb249c90287a61eb6fd49a623d95e5893324de51b700e1937717eba
paper_id: theta-closure-in-modal-triplet-theory-i-gauge-profile-t-c11e7b8f
release_state: zenodo_released
released_version: v1.0
title: "Theta Closure in Modal Triplet Theory I: Gauge-Profile Targets from Multi-Loop Common-Scheme Transport"
zenodo_doi: 10.5281/zenodo.18255245
zenodo_record_id: 18255245
zenodo_url: "https://zenodo.org/records/18255245"
---

# Revision note for this edition

Supersedes.  
*Theta Closure in Modal Triplet Theory I: Gauge Couplings from Internal Geometry*, first edition.

Reason.  
The former target used an obsolete one-loop few-TeV crossing, treated calibrated ratios as predictions, and combined unit-$`L^2`$ normalization with overlap definitions that would force trivial unit values.

Resolution.  
Version 2 uses weighted gauge-kinetic coefficients and SMDR v1.3 common-scheme targets at $`Q=M_t`$, with explicit provenance and conditional projector-error assumptions.

Retained result.  
Gauge-coupling ratios can still be posed as geometric overlap targets in a normalized high-coherence realization.

Remaining boundary.  
MTT must independently select and execute the internal geometry before these calibrated targets become predictions.

# Purpose and scope

This paper presents a conditional map from a common-scheme Standard Model gauge profile to internal overlap targets in Modal Triplet Theory (MTT).

The goals are deliberately narrow:

1.  Derive gauge–coupling expressions from internal overlap integrals.

2.  Extract numerical $`\Theta`$–profile targets from measured couplings.

3.  Test whether a nonempty admissible $`\Theta`$–region satisfies the MTT gap conditions.

4.  State all assumptions and calibration choices explicitly.

No claim of uniqueness, zero-knob gauge-coupling prediction, or full unification is made. The coupling data enter upstream of the profile targets; agreement of a fitted geometry with those same targets is a realization or round-trip test, not a held-out prediction.

# Standing assumptions of Modal Triplet Theory

We collect here the assumptions used throughout. They are standard within the MTT corpus and are not re-derived.

<div class="assumption">

**Assumption 1** (Bounded internal geometry). The internal bundles $`B_n`$ possess bounded geometry and admit commuting vertical Laplacians.

</div>

<div class="assumption">

**Assumption 2** (Uniform spectral gap). There exists a strictly positive lower bound
``` math
\lambda_{\ast} > 0
```
separating coherent from noncoherent internal modes.

</div>

<div class="assumption">

**Assumption 3** (Bounded coherent projection). The joint Riesz projector
``` math
\Pi = \Pi_{B_1}\Pi_{B_2}\Pi_{B_3}
```
is bounded on $`H^1`$.

</div>

<div class="assumption">

**Assumption 4** (Fundamental Contractivity Condition (FCC)). The projected flow $`F=\Pi\circ\Phi_\tau`$ is contractive on the coherent sector.

</div>

<div class="remark">

*Remark 5*. If these assumptions fail, this paper loses controlled access to the stated coherent effective encoding. No claim is made that the underlying mathematical configuration, probabilities, records, or observers cease to exist in every description.

</div>

## Spectral gap as a controlled-description gate

A uniform spectral gap is assumed throughout this work as a sufficient condition for a stable finite coherent sector. If the selected cluster loses separation, the corresponding Riesz projector and truncation estimates may lose regularity, so this paper no longer controls the stated effective encoding. This does not imply that amplitudes, probabilities, records, or an underlying mathematical description cease to exist in every formulation.

The present work does not derive the gap dynamically or prove that every physical theory must possess this particular finite-cluster description. It tests consequences conditional on the declared gap and projector hypotheses.

# Internal operator structure

The physical dimensional-reduction formula is posed on one compact six-manifold $`X_6`$ with three compatible vertical sectors. A single Hermitian line bundle or principal $`U(1)`$ bundle $`L_{\mathrm{shared}}\to X_6`$ supplies the common phase/holonomy datum. It acts in every sector and is counted once.

For the calibrated Route–A computation only, write $`B_n`$ for the effective support and measure used by sector $`n`$. Locally these supports may be modeled using:

- a shared-circle phase normalization for the abelian lane,

- a round two-dimensional lens-base representative for the weak lane,

- a compact Heisenberg nilmanifold representative for the color lane.

The three $`B_n`$ are not asserted to be simultaneous Cartesian factors of $`X_6`$, and no literal $`S^1_{\mathrm{shared}}\times L(3,1)\times\mathrm{Nil}_3`$ compactification is used. The Lens–Nil data form an auxiliary calibrated operator model; the current global physical candidate is the distinct q79/Fu–Yau branch.

# Gauge couplings from internal overlaps

## Definition of gauge-kinetic overlaps

<div class="definition">

**Definition 6** (Sector gauge-kinetic coefficient). For each gauge factor $`a=1,2,3`$, fix a sector representative $`\omega_a`$ by a declared pointwise, period, or cohomological normalization and define
``` math
I_a := \int_{B_a}
 w_a\,\langle \omega_a,\omega_a\rangle\,d\mu_{B_a}.
```
Here $`w_a>0`$ contains the induced gauge-kinetic density, including any integrated spectator directions and trace factors. The representative is not simultaneously normalized to unit $`L^2(B_a,w_a\,d\mu)`$; doing so would make $`I_a=1`$ by definition and erase the coupling information.

</div>

## Reduction of the Yang–Mills action

<div class="proposition">

**Proposition 7** (Conditional coupling–overlap relation). *Assume a ten-dimensional Yang–Mills sector with common coefficient $`g_{10}`$, a consistent truncation to mutually orthogonal four-dimensional gauge zero modes, and the gauge-kinetic weights and normalizations in the preceding definition. Then
``` math
\frac{1}{g_a^2} = \frac{1}{g_{10}^2}\, I_a.
```*

</div>

<div class="proof">

*Proof.* Start from the ten-dimensional Yang–Mills action
``` math
S_{10} = \frac{1}{2g_{10}^2}\int \mathrm{Tr}(F_{AB}F^{AB})\, d\mathrm{vol}_{10}.
```

Expand the gauge field along the declared internal sector modes
``` math
A_\mu(x,u) = A_\mu^{(a)}(x)\,\omega_a(u),
```

Integrating the weighted internal gauge-kinetic density and using orthogonality of the retained modes yields
``` math
S_4 = \frac{1}{4g_a^2}\int F_{\mu\nu}^{(a)}F^{(a)\mu\nu}\, d\mathrm{vol}_4,
```
with
``` math
\frac{1}{g_a^2}
=\frac{1}{g_{10}^2}
\int_{B_a}w_a\langle\omega_a,\omega_a\rangle d\mu_{B_a}.
```
 ◻

</div>

## Normalization conventions

We adopt the following conventions:

1.  **Generator normalization:**
    ``` math
    \mathrm{Tr}(T^a T^b)=\frac{1}{2}\delta^{ab}.
    ```

2.  **Hypercharge normalization (GUT-normalized):**
    ``` math
    g_1=\sqrt{\frac{5}{3}}\, g',
    \qquad
    \alpha_1=\frac{5}{3}\alpha_Y.
    ```

With these conventions, the normalization constants satisfy
``` math
N_1=N_2=N_3=1,
```
and all group-theoretic factors are absorbed into the definition of $`g_1`$.

# Summary of this section

At this point we have established:

- Gauge couplings descend from weighted internal gauge-kinetic coefficients under the stated higher-dimensional action and truncation assumptions.

- The relation $`1/g_a^2=I_a/g_{10}^2`$ is exact within that declared reduction ansatz.

- Ratios of couplings are ratios of those coefficients only when the same $`g_{10}`$ and compatible generator conventions apply to all three sectors.

In the next part we will:

1.  Compute $`g_1,g_2,g_3`$ explicitly from experimental inputs.

2.  Run them to a common matching scale.

3.  Extract numerical $`\Theta`$–constraints.

# Experimental inputs and gauge couplings at $`M_Z`$

In this section we compute the Standard Model gauge couplings explicitly from experimental inputs at the $`Z`$-pole and prepare them for comparison with the internal overlap formulation.

## Electroweak inputs

We use the following $`\overline{\mathrm{MS}}`$-scheme inputs at $`\mu=M_Z`$:
``` math
\begin{equation}
\alpha(M_Z)^{-1} = 127.95,
\qquad
\sin^2\theta_W(M_Z) = 0.23122,
\qquad
\alpha_s(M_Z) = 0.1179.
\label{eq:EWinputs}
\end{equation}
```

These values are representative of current PDG averages and are sufficient for the present analysis.

## Definition of gauge couplings

Define the electromagnetic coupling
``` math
\begin{equation}
e := \sqrt{4\pi \alpha(M_Z)}.
\end{equation}
```

Then the electroweak couplings are
``` math
\begin{equation}
g_2 = \frac{e}{\sin\theta_W},
\qquad
g' = \frac{e}{\cos\theta_W},
\end{equation}
```
and the GUT-normalized hypercharge coupling is
``` math
\begin{equation}
g_1 = \sqrt{\frac{5}{3}}\, g'.
\end{equation}
```

The strong coupling is
``` math
\begin{equation}
g_3 = \sqrt{4\pi \alpha_s(M_Z)}.
\end{equation}
```

## Explicit numerical evaluation

From <a href="#eq:EWinputs" data-reference-type="eqref" data-reference="eq:EWinputs">[eq:EWinputs]</a>:
``` math
\alpha(M_Z) \approx 0.007816,
\qquad
e = \sqrt{4\pi\alpha} \approx 0.3135.
```

Also,
``` math
\sin\theta_W = \sqrt{0.23122} \approx 0.4809,
\qquad
\cos\theta_W \approx 0.8768.
```

Thus,
``` math
g_2(M_Z) = \frac{0.3135}{0.4809} \approx 0.6517,
```
``` math
g'(M_Z) = \frac{0.3135}{0.8768} \approx 0.3576,
```
``` math
g_1(M_Z) = \sqrt{\frac{5}{3}}\times 0.3576 \approx 0.4614.
```

For QCD,
``` math
g_3(M_Z) = \sqrt{4\pi\times 0.1179} \approx 1.2172.
```

| Scale   | $`g_1`$ (GUT) |  $`g_2`$   |  $`g_3`$   |
|:--------|:-------------:|:----------:|:----------:|
| $`M_Z`$ |  $`0.4614`$   | $`0.6517`$ | $`1.2172`$ |

Gauge couplings at $`\mu=M_Z`$ computed from <a href="#eq:EWinputs" data-reference-type="eqref" data-reference="eq:EWinputs">[eq:EWinputs]</a>.

# Selected multi-loop common-scheme transport

The former one-loop evolution to $`5~\mathrm{TeV}`$ is not used in this revision. In particular, the Standard Model equations do not place the $`g_1=g_2`$ crossing there. We instead use the selected SMDR v1.3 transport, which maps fifteen measured source coordinates to the full non-decoupled Standard Model in the tadpole-free pure $`\overline{\mathrm{MS}}`$ scheme at
``` math
Q=M_t=172.5590883453979~\mathrm{GeV}.
```
This is a scheme and comparison scale, not an MTT coherence scale.

The accepted gauge rows are
``` math
\begin{align}
 g_Y(Q)&=0.3585945042\pm0.0000307251,\\
 g_2(Q)&=0.6475986708\pm0.0000287665,\\
 g_3(Q)&=1.163427409\pm0.004036156.
\end{align}
```
With the paper’s GUT normalization,
``` math
g_1(Q)=\sqrt{\frac53}\,g_Y(Q)
       =0.4629435143\pm0.0000396660.
```
These rows are outputs of a common multi-loop matching/running map. Their covariance is propagated from the declared diagonal measured-input profile; an official joint likelihood spanning all fifteen source coordinates is not claimed.

# Numerical $`\Theta`$–profile targets from gauge data

Under the coupling–overlap relation already proved conditionally above,
``` math
\frac{I_b}{I_a}=\left(\frac{g_a}{g_b}\right)^2.
```
Consequently the selected common-scheme profile gives
``` math
\begin{equation}
\boxed{
 \frac{I_2}{I_1}=0.5110273\pm0.0001231,
 \qquad
 \frac{I_3}{I_1}=0.158335\pm0.001098.
}
\label{eq:targets}
\end{equation}
```
The propagated covariance of the two ratios is $`-6.1892\times10^{-9}`$, corresponding to correlation $`-0.04578`$.

These are experimentally anchored profile targets. A geometry adjusted to reproduce them is a calibrated realization. A held-out prediction would require fixing that geometry without these gauge rows and then computing an observable not used in source, branch, scale, or model selection.

# Transition to the geometric $`\Theta`$-problem

The next step is to determine whether the internal geometry of MTT admits overlap integrals $`I_1,I_2,I_3`$ satisfying the above ratios while maintaining the baseline spectral gap $`\lambda_{\ast}=0.25`$.

This problem is addressed in the next section.

# Baseline internal geometry and spectral gap bounds

We now specify the auxiliary operator models used for the Route–A gap check and collect their assumed spectral inequalities.

## Auxiliary metric supports

The three vertical operators are tested on effective supports $`\Sigma_n`$:

- $`\Sigma_1`$ is an auxiliary circle,

- $`\Sigma_2`$ is a two-dimensional lens-base model,

- $`\Sigma_3`$ is a compact nilmanifold model.

The common $`U(1)`$ phase/holonomy line acts across all three supports and is counted once. The notation does not assert three products $`S^1_{\mathrm{cen}}\times\Sigma_n`$ or identify these supports with coordinate factors of the selected q79 compactification.

The auxiliary metric ansatz has parameters:

- $`R_1`$ – radius of $`\Sigma_1`$,

- $`R_{\mathrm{lens}}`$ – effective lens-base radius,

- $`f_2`$ – lens-base scale factor,

- $`h_0`$ – Cheeger lower-bound parameter for the nil model.

## Spectral gap bounds

The following are model-specific lower bounds on the smallest nonzero eigenvalues of the auxiliary vertical Laplacians.

#### Circle factor $`\Sigma_1`$.

For a circle of radius $`R_1`$,
``` math
\begin{equation}
\lambda_{\Sigma_1} \sim \frac{1}{R_1^2}.
\label{eq:gapSigma1}
\end{equation}
```

#### Lens factor $`\Sigma_2`$.

For the lens sheet with effective radius $`f_2R_{\mathrm{lens}}`$,
``` math
\begin{equation}
\lambda_{\mathrm{lens}} \ge \frac{2}{(f_2R_{\mathrm{lens}})^2}.
\label{eq:gapLens}
\end{equation}
```

#### Nil factor $`\Sigma_3`$.

For the nil leaf, the spectral gap is controlled by the Cheeger constant:
``` math
\begin{equation}
h \ge h_0 > 0
\quad\Rightarrow\quad
\lambda_{\mathrm{nil}} \ge \frac{h_0^2}{4}.
\label{eq:gapNil}
\end{equation}
```

## Baseline numerical values

In the worked numerical baseline of the Foundation,
``` math
\begin{equation}
h_0 = 1
\quad\Rightarrow\quad
\lambda_{\mathrm{nil}} = \frac{1}{4} = 0.25.
\end{equation}
```

We enforce the *baseline lower bound* $`\lambda_{\ast}\ge 0.25`$ using $`h_0=1`$. This sets a conservative admissibility floor; explicit realizations of the nil sector may exceed this bound and need not saturate it.

# Geometric overlap model

We now introduce a minimal, computable auxiliary coefficient model. It is not obtained by multiplying three sector supports or by appending the shared circle to each support. Instead, all spectator integrations, mode normalizations, and gauge-kinetic weights are absorbed into three positive coefficients.

## Auxiliary coefficient ansatz

At the Route–A calibration tier, parameterize the coefficients as
``` math
\begin{align}
I_1 &= 2\pi R_1,
\label{eq:I1}\\
I_2 &= \kappa_\ell (f_2R_{\mathrm{lens}})^2,
\label{eq:I2}\\
I_3 &= \kappa_n\,\mathcal{S}_n,
\label{eq:I3}
\end{align}
```
This is an ansatz for the weighted coefficients defined above, not a theorem equating the norm of an $`L^2`$-normalized mode with a geometric volume. A selected compactification must emit the corresponding weights and representatives on one $`X_6`$ before these coefficients become source-derived. where:

- $`\kappa_\ell`$ is the unit-area normalization of the lens sheet,

- $`\kappa_n\,\mathcal{S}_n`$ is the effective nil overlap weight,

- $`\mathcal{S}_n`$ is not assumed equal to a simple metric area.

This separation is required because the nil spectral gap <a href="#eq:gapNil" data-reference-type="eqref" data-reference="eq:gapNil">[eq:gapNil]</a> is controlled by $`h_0`$, not directly by metric scale.

# Solving the $`\Theta`$–system

We now solve the overlap constraints from Section 4 of Part II together with the spectral gap bounds.

## Overlap constraints

From <a href="#eq:targets" data-reference-type="eqref" data-reference="eq:targets">[eq:targets]</a> and <a href="#eq:I1" data-reference-type="eqref" data-reference="eq:I1">[eq:I1]</a>–<a href="#eq:I3" data-reference-type="eqref" data-reference="eq:I3">[eq:I3]</a>:
``` math
\begin{align}
\frac{I_2}{I_1}
&=
\frac{\kappa_\ell (f_2R_{\mathrm{lens}})^2}{2\pi R_1}
= 0.5110273,
\label{eq:Theta1}\\
\frac{I_3}{I_1}
&=
\frac{\kappa_n\mathcal{S}_n}{2\pi R_1}
= 0.158335.
\label{eq:Theta2}
\end{align}
```

Solving <a href="#eq:Theta1" data-reference-type="eqref" data-reference="eq:Theta1">[eq:Theta1]</a> gives
``` math
\begin{equation}
(f_2R_{\mathrm{lens}})^2
=
\frac{0.5110273\cdot 2\pi}{\kappa_\ell}\,R_1
=
\frac{3.210879}{\kappa_\ell}\,R_1,
\label{eq:RlSolve}
\end{equation}
```
hence
``` math
\begin{equation}
R_{\mathrm{lens}}
=
\frac{\sqrt{(3.210879/\kappa_\ell)\,R_1}}{f_2}.
\label{eq:RlFinal}
\end{equation}
```

From <a href="#eq:Theta2" data-reference-type="eqref" data-reference="eq:Theta2">[eq:Theta2]</a>:
``` math
\begin{equation}
\kappa_n\mathcal{S}_n
=
0.158335\cdot 2\pi\,R_1
=
0.994849\,R_1.
\label{eq:SnSolve}
\end{equation}
```

## Imposing gap inequalities

We require:
``` math
\begin{align}
\lambda_{\Sigma_1} &\ge 0.25,
\label{eq:gap1}\\
\lambda_{\mathrm{lens}} &\ge 0.25,
\label{eq:gap2}\\
\lambda_{\mathrm{nil}} &\ge 0.25.
\label{eq:gap3}
\end{align}
```

#### Nil.

Set $`h_0=1`$, so <a href="#eq:gapNil" data-reference-type="eqref" data-reference="eq:gapNil">[eq:gapNil]</a> gives $`\lambda_{\mathrm{nil}}=0.25`$.

#### Circle.

From <a href="#eq:gapSigma1" data-reference-type="eqref" data-reference="eq:gapSigma1">[eq:gapSigma1]</a> and <a href="#eq:gap1" data-reference-type="eqref" data-reference="eq:gap1">[eq:gap1]</a>,
``` math
\frac{1}{R_1^2}\ge 0.25
\quad\Rightarrow\quad
R_1\le 2.
```

#### Lens.

From <a href="#eq:gapLens" data-reference-type="eqref" data-reference="eq:gapLens">[eq:gapLens]</a> and <a href="#eq:gap2" data-reference-type="eqref" data-reference="eq:gap2">[eq:gap2]</a>,
``` math
\frac{2}{(f_2R_{\mathrm{lens}})^2}\ge 0.25
\quad\Rightarrow\quad
(f_2R_{\mathrm{lens}})^2\le 8.
```

Substitute <a href="#eq:RlSolve" data-reference-type="eqref" data-reference="eq:RlSolve">[eq:RlSolve]</a>:
``` math
\frac{3.210879}{\kappa_\ell}\,R_1 \le 8
\quad\Rightarrow\quad
R_1 \le \frac{8\kappa_\ell}{3.210879}\approx 2.492\,\kappa_\ell.
```

## Existence theorem

<div class="theorem">

**Theorem 8** (Existence of an auxiliary calibrated $`\Theta`$–region). *At the selected common-scheme profile point $`Q=M_t`$, choose
``` math
h_0=1,\qquad \kappa_\ell=1,\qquad f_2\ge 1.
```
Then for every $`R_1\in(0,2]`$ there exists a choice of $`R_{\mathrm{lens}}`$ and $`\mathcal{S}_n`$ given by <a href="#eq:RlFinal" data-reference-type="eqref" data-reference="eq:RlFinal">[eq:RlFinal]</a> and <a href="#eq:SnSolve" data-reference-type="eqref" data-reference="eq:SnSolve">[eq:SnSolve]</a> such that:*

1.  *the gauge overlap constraints $`\frac{I_2}{I_1}=0.5110273`$ and $`\frac{I_3}{I_1}=0.158335`$ are satisfied;*

2.  *the spectral gap inequalities $`\lambda_{\Sigma_1},\lambda_{\mathrm{lens}},\lambda_{\mathrm{nil}}\ge 0.25`$ hold;*

3.  *the minimal spectral gap remains $`\lambda_{\ast}=0.25`$.*

</div>

<div class="proof">

*Proof.* Let $`R_1\in(0,2]`$. Then $`\lambda_{\Sigma_1}\ge 0.25`$. With $`\kappa_\ell=1`$ and $`f_2\ge 1`$, <a href="#eq:RlFinal" data-reference-type="eqref" data-reference="eq:RlFinal">[eq:RlFinal]</a> implies $`(f_2R_{\mathrm{lens}})^2=3.210879R_1\le 6.421758<8`$, hence $`\lambda_{\mathrm{lens}}>0.25`$. With $`h_0=1`$, $`\lambda_{\mathrm{nil}}=0.25`$. The overlap constraints are satisfied by construction. ◻

</div>

# Interpretation

The existence theorem shows only that the measured Standard Model gauge profile can be represented inside this auxiliary coefficient ansatz without violating its assumed dimensionless gap inequalities. The choice $`h_0=1`$ saturates the declared nil lower bound in this ansatz; it does not prove that the selected q79 geometry has this value or that the nil lane physically controls the onset of noncoherent behavior.

<div class="remark">

*Remark 9*. The quantities $`\kappa_n`$ and $`\mathcal{S}_n`$ encode nontrivial nilmanifold structure and are not free once explicit harmonic representatives are specified.

</div>

<div class="remark">

*Remark 10* (Coherent sector stability). All results in this work are conditional on the stability of the coherent sector. If the coherent sector were dynamically unstable, the theory would not merely predict different numerical values; rather, it would fail to support persistent observables, reproducible measurements, or probabilistic interpretation. Accordingly, coherent sector stability is treated here as a prerequisite for physics rather than a phenomenological assumption.

</div>

# Massless gauge-sector normalization via the twistor corner

The remaining technical ambiguity in the $`\Theta`$–closure analysis concerns the explicit definition and normalization of the nonabelian gauge-kinetic coefficients $`I_2`$ and $`I_3`$ associated with the $`SU(2)`$ and $`SU(3)`$ sectors. In this section we state a well-typed conditional definition in the high–coherence (twistor) corner of Modal Triplet Theory.

<div class="remark">

*Remark 11* (Twistor corner as a computational device). In this paper the twistor corner is used solely as a *computational normalization regime* for the massless coherent gauge sector, providing canonical harmonic representatives and gap-controlled error bounds. No claim is made that Nature resides exactly in this corner, nor that twistor space is fundamental.

</div>

## High–coherence regime and admissible truncation

The twistor formulation of MTT establishes the existence of a high–coherence regime in which:

1.  the spectral gap $`\lambda_Q`$ separating coherent and noncoherent modes is parametrically large;

2.  the effective generator admits a Schur–Feshbach reduction onto a finite–dimensional coherent subspace;

3.  truncation errors are bounded by explicit operator–norm estimates of order $`O(\lambda_Q^{-1})`$.

<div class="assumption">

**Assumption 12** (Twistor-corner admissibility). We assume that the $`\Theta`$–matching scale $`\mu_\Theta`$ lies within the high–coherence regime for the massless gauge sector, so that the Schur–Feshbach reduction is valid with remainder bounded by $`O(\lambda_Q^{-1})`$.

</div>

<div class="remark">

*Remark 13*. This assumption invokes no ultraviolet completion and no string-theoretic structure; it relies only on the coherence and gap hypotheses already stated in Sections 2 and 10.

</div>

## Canonical definition of the massless gauge subspace

Let $`\mathcal H`$ denote the full internal Hilbert space of modal fields. Define $`\mathcal H_0\subset\mathcal H`$ as the coherent massless gauge subspace selected by the twistor corner, characterized by:

1.  self–duality of the Yang–Mills curvature;

2.  vanishing effective mass under the reduced generator;

3.  holomorphic encoding via the Ward correspondence.

<div class="definition">

**Definition 14** (Twistor-corner massless sector). $`\mathcal H_0`$ is defined as the image of the coherent projector $`P_0`$ associated with the self–dual Yang–Mills corner of the MTT configuration space.

</div>

This definition is canonical within the admissible slab and does not depend on additional choices.

## Schur–Feshbach reduction and error control

Let $`L`$ be the full internal generator and write
``` math
L =
\begin{pmatrix}
P_0 L P_0 & P_0 L Q \\
Q L P_0 & Q L Q
\end{pmatrix},
\qquad Q=1-P_0.
```

The effective generator on $`\mathcal H_0`$ is given by the Schur–Feshbach map
``` math
L_{\mathrm{eff}}
=
P_0 L P_0
-
P_0 L Q (Q L Q)^{-1} Q L P_0.
```

The twistor analysis proves the operator bound
``` math
\|P_0 L Q (Q L Q)^{-1} Q L P_0\|
\;\le\;
C\,\lambda_Q^{-1},
```
for some constant $`C`$ independent of infrared data.

## Harmonic representatives and normalization

<div class="definition">

**Definition 15** (Twistor-corner harmonic representatives). For $`a=2,3`$, fix a cohomology class together with its period normalization, the internal metric, and a gauge condition. Let $`\omega_a^{(0)}`$ denote its harmonic representative in $`\mathcal H_0`$. Hodge theory fixes the harmonic representative of the fixed class; the period condition, rather than unit $`L^2`$ normalization, fixes its scale.

</div>

<div class="remark">

*Remark 16*. The abelian overlap $`I_1`$ remains fixed by the explicit $`S^1_{\mathrm{cen}}`$ normalization of Appendix G and is not modified by the twistor construction.

</div>

## Leading–order overlap integrals

<div class="definition">

**Definition 17** (Leading–order overlaps). The leading–order nonabelian overlap integrals are defined by
``` math
I_a^{(0)} := \int_{B_a}
w_a^{(0)}
\langle \omega_a^{(0)}, \omega_a^{(0)} \rangle \, d\mu_{B_a},
\qquad a=2,3.
```

</div>

These depend on the massless coherent geometry, the fixed periods, and the gauge-kinetic weights. The twistor representation alone does not select those normalization data.

## Control of overlap deviations

Let $`I_a`$ denote the full overlap integrals defined in Section 4.

<div class="lemma">

**Lemma 18** (Conditional overlap stability under coherent truncation). *Assume the full and leading projectors, period-normalized representatives, weights, and measures obey uniform perturbation estimates of order $`\lambda_Q^{-1}`$ in norms controlling the displayed integrals. Then there exist constants $`C_a>0`$ such that
``` math
|I_a - I_a^{(0)}| \;\le\; C_a\,\lambda_Q^{-1},
\qquad a=2,3.
```*

</div>

<div class="proof">

*Proof.* Expand the difference of the two weighted quadratic integrals into the representative, weight, and measure perturbations. Cauchy–Schwarz and the assumed uniform bounds control each term by its corresponding $`O(\lambda_Q^{-1})`$ estimate. Their finite sum gives the stated constant $`C_a`$. The Schur–Feshbach bound alone would not supply all of these coefficient estimates. ◻

</div>

## Twistor-corner $`\Theta`$–closure at leading order

Combining the above with the experimentally extracted targets at the selected common-scheme point $`Q=M_t`$:
``` math
\frac{I_2}{I_1} = 0.5110273,
\qquad
\frac{I_3}{I_1} = 0.158335,
```
we obtain:

<div class="theorem">

**Theorem 19** (Twistor-corner $`\Theta`$–closure condition). *If the twistor-corner admissibility assumption holds at $`\mu_\Theta`$, then $`\Theta`$–closure at leading order reduces to the computable conditions
``` math
\frac{I_2^{(0)}}{I_1} = 0.5110273,
\qquad
\frac{I_3^{(0)}}{I_1} = 0.158335,
```
with controlled corrections of order $`O(\lambda_Q^{-1})`$.*

</div>

<div class="remark">

*Remark 20*. Failure of these relations falsifies either the baseline internal geometry or the twistor-corner admissibility hypothesis.

</div>

## Scope

This section does not claim that the twistor corner describes the full physical gauge sector. It provides a conditional computational corner in which $`I_2`$ and $`I_3`$ are well defined after the metric, periods, weights, and perturbation bounds have been supplied.

# Scale separation and withdrawn legacy calibration

The scale $`Q=M_t`$ used above is a renormalization/matching coordinate. It does not determine the physical internal gap, compactification radius, proper-time filter, Planck scale, Hubble scale, or primordial tensor amplitude. The former identifications
``` math
Q\sim E_{\mathrm{gap,min}}\sim\tau_0^{-1/2}
```
were additional calibrations tied to the invalid $`4.2`$–$`5~\mathrm{TeV}`$ crossing and are withdrawn.

The dimensionless spectral inequalities in the preceding sections remain conditional geometric statements. Converting them to SI or external energy units requires an independently selected action normalization and a theorem relating the internal operator spectrum to physical propagator poles or response scales. No cosmological or quantum-gravity bound is inferred in this paper.

# Falsifiability and status

At the profile tier, the direct test is whether a specified internal geometry, with its measure and harmonic normalization fixed independently of the gauge targets, emits the two ratios in <a href="#eq:targets" data-reference-type="eqref" data-reference="eq:targets">[eq:targets]</a> within the propagated covariance. If the geometry is fitted to those ratios, the result is instead a realization and round-trip consistency check.

The old cosmological and Gaussian quantum-gravity discriminators are removed because their physical scale identification is not derived here. The current broader MTT repository closes embedded renormalized-Standard-Model equivalence at the adopted one-shared-physical-primitive/profile standard. That successor does not turn the present overlap targets into zero-knob predictions and does not derive standard perturbative quantization from MTT.

# Conclusion

The coupling–overlap formula survives as a conditional dimensional-reduction identity. Its numerical implementation is now placed in one selected multi-loop common scheme at $`Q=M_t`$, yielding
``` math
I_2/I_1=0.5110273\pm0.0001231,\qquad
 I_3/I_1=0.158335\pm0.001098.
```
The full covariance provenance is retained, and the absence of a public joint fifteen-coordinate likelihood is stated explicitly.

The former $`5~\mathrm{TeV}`$ crossing, the geometry calibrated to its ratios, and the identification of that scale with an internal gap, proper-time cutoff, or cosmological scale are not results of this revision. Papers II–V must be re-executed or reclassified accordingly. This paper therefore supplies a reproducible profile target and a precise geometric test, not a unique first-principles prediction of gauge couplings or internal geometry.

# References

1.  Particle Data Group (PDG), Review of Particle Physics (for $`M_Z`$, $`\alpha(M_Z)`$, $`\sin^2\theta_W(M_Z)`$, $`\alpha_s(M_Z)`$).

2.  M. E. Machacek and M. T. Vaughn, “Two-loop renormalization group equations in a general quantum field theory,” Nucl. Phys. B222 (1983) 83–103.

3.  T. Kato, *Perturbation Theory for Linear Operators*, Springer (1995).

4.  Peter Nero, *Modal Triplet Theory: Foundation* (MTT corpus).

5.  Peter Nero, *Modal Triplet Theory: Quantum Amplitudes from Modal Geometry* (MTT corpus).

6.  Peter Nero, *Twistor Encodings as High-Coherence Limits of Modal Triplet Theory* (MTT corpus).
