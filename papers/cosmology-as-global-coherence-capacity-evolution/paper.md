---
abstract: |
  This paper replaces an earlier heuristic cosmology with a covariant effective-model interface. Coherence capacity in Modal Triplet Theory (MTT) is an admissibility margin; by itself it does not determine a spacetime metric, expansion, acceleration, a causal horizon, a cosmological singularity, or an arrow of time. To ask those questions we declare a Jordan-frame scalar–tensor action in which a scalar $`\mathcal C`$ is proposed as the large-scale image of capacity data. We derive the metric equation, scalar equation, homogeneous Friedmann equations, and the exact condition for accelerated expansion. We also prove a reconstruction-degeneracy result: freely chosen coupling functions can reproduce a broad class of expansion histories, so agreement with $`H(z)`$ is not a prediction until MTT selects those functions and their initial data independently of the observations. Capacity-zero level sets are separated from Lorentzian particle, event, and apparent horizons; positive capacity is shown not to imply past completeness; and time orientation is kept distinct from irreversible entropy production. The result is a conditional effective realization, not a derivation of cosmology from the present MTT axioms. It supplies the equations and data products that a future same-source theorem must determine.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: Version 3, July 2026
generated_from_main_tex_sha256: b61f3a68e7547f87ac157c4308a444c0c5066bd62d7f9cf364db861bbccfc3a3
paper_id: cosmology-as-global-coherence-capacity-evolution
release_state: zenodo_released
released_version: v3
title: |
  **A Covariant Effective Model for Coherence-Capacity Cosmology**
  Equations, Degeneracies, and Observational Tests
zenodo_doi: 10.5281/zenodo.21716823
zenodo_record_id: 21716823
zenodo_url: "https://zenodo.org/records/21716823"
---

# Version 3 Revision Note

Supersedes.
Version 2, *Cosmology as Global Coherence Capacity Evolution*.

Reason.
The earlier paper inferred expansion, acceleration, horizons, nonsingularity, and a time arrow from capacity language without a covariant metric equation or a selected irreversible dynamics.

Resolution.
Version 3 declares and varies a covariant effective action, derives its homogeneous equations and exact acceleration criterion, proves the reconstruction degeneracy and the relevant separation counterexamples, and supplies an observational test contract.

Retained content.
The proposal that an MTT admissibility margin may have a useful large-scale cosmological image is retained as a conditional interpretation.

Open boundary.
MTT has not yet selected the source map, coupling functions, initial state, perturbation branch, or a held-out observationally viable solution from one accepted upper source.

# Introduction and orientation

In plain language, the motivating picture is that a cosmological solution may carry, in addition to its metric and matter fields, a slowly varying record of how far the projected description lies from loss of admissibility. It is tempting to call that record “spare capacity” and then to read expansion, acceleration, or horizons directly from it. That temptation must be resisted. A positive scalar says that a margin is positive. It does not say how the metric evolves.

This revision therefore reverses the order of inference. We first state a covariant effective action. Its Euler–Lagrange equations determine which cosmological histories are allowed. Only afterward do we ask whether the scalar in that action can be sourced by the independently defined MTT coherence capacity. This places the proposal in the same mathematical class as familiar scalar–tensor models , while leaving the MTT source problem visible.

The paper has three aims:

1.  give a mathematically complete covariant realization that can be reduced to homogeneous cosmology;

2.  identify exactly which attractive conclusions do *not* follow from capacity language alone; and

3.  specify the observables and independent tests required before the realization can be promoted from a model to an MTT prediction.

# Claim tier and interface with MTT

## Three logically separate layers

The construction uses three layers that must not be collapsed.

<div class="center">

| Layer | Supplied object | What is not supplied |
|:---|:---|:---|
| MTT admissibility | A normalized coherence-capacity margin and, where available, a constitutive transport law | A Lorentzian metric equation, a cosmological scalar, or an equation of state |
| Covariant realization | An action for $`g_{\mu\nu}`$, $`\mathcal C`$, and matter | A theorem selecting its free functions from upper geometry |
| Observational comparison | Distances, expansion rates, perturbations, and likelihoods | Predictive force unless parameters and functions were fixed before using the compared data |

</div>

The current result is at the second layer. The capacity papers define and transport an admissibility margin . They do not prove that the resulting quantity is a fundamental scalar field, a varying Planck mass, or a stress-energy component. Those identifications are hypotheses of the present effective model.

## What “capacity cosmology” means here

<div class="definition">

**Definition 1** (Capacity-cosmology realization). A capacity-cosmology realization is a tuple
``` math
\mathfrak C_{\mathrm{cos}}
 =
 (M,g,\mathcal C,F,K,U,S_{\mathrm m},\mathfrak s)
```
where $`(M,g)`$ is a time-oriented Lorentzian spacetime, $`\mathcal C`$ is a real scalar, $`F,K,U`$ are coupling functions, $`S_{\mathrm m}`$ is a matter action, and $`\mathfrak s`$ is a proposed source map from declared MTT capacity data to $`\mathcal C`$. The realization is *selected* only if $`\mathfrak s`$, $`F`$, $`K`$, $`U`$, and the relevant initial state are derived from one accepted MTT source without fitting the target cosmological observables.

</div>

This definition makes room for the physical idea without pretending that the source map has already been proved.

# A covariant effective action

We use metric signature $`(-,+,+,+)`$ and units $`c=1`$. Matter is minimally coupled to the Jordan-frame metric $`g_{\mu\nu}`$, which therefore defines redshift, rods, clocks, and the observational distances in this paper. Consider
``` math
\begin{equation}
 S_{\mathrm{eff}}
 =
 \int_M \mathrm{d}^4x\,\sqrt{-g}\,
 \left[
 \frac{1}{2}F(\mathcal C)R
 -\frac{1}{2}K(\mathcal C)
    g^{\mu\nu}\nabla_\mu\mathcal C\nabla_\nu\mathcal C
 -U(\mathcal C)
 \right]
 +S_{\mathrm m}[g,\Psi].
 \label{eq:action}
\end{equation}
```
We assume $`F(\mathcal C)>0`$. A sufficient simple stability choice is $`K(\mathcal C)\geq 0`$; more generally the Einstein-frame scalar kinetic coefficient must satisfy
``` math
\frac{K}{F}+\frac{3}{2}\left(\frac{F'}{F}\right)^2>0.
```
The functions $`F`$, $`K`$, and $`U`$ are part of the model data, not results of covariance.

<div id="thm:field-equations" class="theorem">

**Theorem 2** (Field equations of the declared realization). *The stationary points of <a href="#eq:action" data-reference-type="ref+label" data-reference="eq:action">[eq:action]</a> satisfy
``` math
\begin{align}
 F G_{\mu\nu}
 &=
 T^{\mathrm m}_{\mu\nu}
 +K\left(
     \nabla_\mu\mathcal C\nabla_\nu\mathcal C
     -\frac{1}{2}g_{\mu\nu}(\nabla\mathcal C)^2
   \right)
 -Ug_{\mu\nu}
 +\nabla_\mu\nabla_\nu F
 -g_{\mu\nu}\Box F,
 \label{eq:metric-field}\\
 0
 &=
 K\Box\mathcal C
 +\frac{1}{2}K'(\nabla\mathcal C)^2
 +\frac{1}{2}F'R
 -U'.
 \label{eq:capacity-field}
\end{align}
```*

*If the matter equations hold, minimal coupling gives $`\nabla^\mu T^{\mathrm m}_{\mu\nu}=0`$.*

</div>

<div class="proof">

*Proof.* Metric variation of $`\sqrt{-g}F R/2`$ gives $`F G_{\mu\nu}/2+(g_{\mu\nu}\Box F-\nabla_\mu\nabla_\nu F)/2`$ before the conventional factor of two is restored. Variation of the kinetic and potential terms gives the scalar stress tensor in <a href="#eq:metric-field" data-reference-type="ref+label" data-reference="eq:metric-field">[eq:metric-field]</a>. Varying $`\mathcal C`$, integrating its kinetic term by parts, and collecting the $`F'R`$ and $`U'`$ terms gives <a href="#eq:capacity-field" data-reference-type="ref+label" data-reference="eq:capacity-field">[eq:capacity-field]</a>. Diffeomorphism invariance and the matter equations yield the matter conservation law. ◻

</div>

#### Interpretation.

$`F(\mathcal C)`$ is an effective squared Planck mass, $`K`$ controls the kinetic response, and $`U`$ is an effective potential. Calling $`\mathcal C`$ a capacity variable does not remove these ingredients. If $`\mathcal C`$ is instead a nonlocal functional of more fundamental fields, varying <a href="#eq:action" data-reference-type="ref+label" data-reference="eq:action">[eq:action]</a> as though it were independent would be incorrect; the source map must then be inserted before variation. That is one of the open upstream choices.

# Homogeneous reduction and the acceleration test

Take a spatially flat FLRW metric
``` math
\mathrm{d}s^2=-\mathrm{d}t^2+a(t)^2\mathrm{d}\mathbf x^2,
 \qquad H=\frac{\dot a}{a},
```
a homogeneous scalar $`\mathcal C(t)`$, and a perfect fluid with density $`\rho_{\mathrm m}`$ and pressure $`p_{\mathrm m}`$. The field equations reduce to
``` math
\begin{align}
 3F H^2
 &=
 \rho_{\mathrm m}
 +\frac{1}{2}K\dot{\mathcal C}^{\,2}
 +U
 -3H\dot F,
 \label{eq:friedmann-one}\\
 -2F\dot H
 &=
 \rho_{\mathrm m}+p_{\mathrm m}
 +K\dot{\mathcal C}^{\,2}
 +\ddot F-H\dot F,
 \label{eq:friedmann-two}\\
 0
 &=
 K(\ddot{\mathcal C}+3H\dot{\mathcal C})
 +\frac{1}{2}K'\dot{\mathcal C}^{\,2}
 +U'
 -3F'(\dot H+2H^2),
 \label{eq:scalar-flrw}\\
 0
 &=
 \dot\rho_{\mathrm m}
 +3H(\rho_{\mathrm m}+p_{\mathrm m}).
 \label{eq:matter-continuity}
\end{align}
```

These are genuine Friedmann-type equations because they are reductions of a covariant action. Dimensional consistency and isotropy alone would not determine them.

<div id="thm:acceleration" class="theorem">

**Theorem 3** (Exact acceleration criterion). *For every solution of <a href="#eq:friedmann-one,eq:friedmann-two" data-reference-type="ref+label" data-reference="eq:friedmann-one,eq:friedmann-two">[eq:friedmann-one,eq:friedmann-two]</a>, accelerated expansion occurs at a time $`t`$ if and only if
``` math
\begin{equation}
 2U
 >
 \rho_{\mathrm m}+3p_{\mathrm m}
 +2K\dot{\mathcal C}^{\,2}
 +3\ddot F+3H\dot F.
 \label{eq:acceleration-condition}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Multiply $`\ddot a/a=H^2+\dot H`$ by $`6F`$, then substitute twice <a href="#eq:friedmann-one" data-reference-type="ref+label" data-reference="eq:friedmann-one">[eq:friedmann-one]</a> and three times <a href="#eq:friedmann-two" data-reference-type="ref+label" data-reference="eq:friedmann-two">[eq:friedmann-two]</a>. The result is
``` math
6F\frac{\ddot a}{a}
 =
 -\rho_{\mathrm m}-3p_{\mathrm m}
 -2K\dot{\mathcal C}^{\,2}
 +2U-3\ddot F-3H\dot F.
```
Since $`F>0`$, positivity of $`\ddot a`$ is equivalent to <a href="#eq:acceleration-condition" data-reference-type="ref+label" data-reference="eq:acceleration-condition">[eq:acceleration-condition]</a>. ◻

</div>

The theorem identifies the error in the earlier heuristic. An outward capacity current, increasing $`\mathcal C`$, or decreasing $`1/\mathcal C`$ does not by itself determine the signs of $`\dot F`$, $`\ddot F`$, $`U`$, or $`\dot H`$. Acceleration follows only after the action and a solution fix all terms in <a href="#eq:acceleration-condition" data-reference-type="ref+label" data-reference="eq:acceleration-condition">[eq:acceleration-condition]</a>.

<div class="corollary">

**Corollary 4** (Minimal-coupling limit). *If $`F=M_{\mathrm{Pl}}^2`$ is constant, then
``` math
\frac{\ddot a}{a}>0
 \quad\Longleftrightarrow\quad
 2U>\rho_{\mathrm m}+3p_{\mathrm m}
       +2K\dot{\mathcal C}^{\,2}.
```
Thus a canonical kinetic term resists acceleration, while a sufficiently large positive potential can support it.*

</div>

<div id="prop:no-expansion" class="proposition">

**Proposition 5** (Capacity positivity does not imply expansion). *Without a declared dynamical relation between $`\mathcal C`$ and $`g`$, the condition $`\mathcal C>0`$ implies neither $`H>0`$ nor $`\ddot a>0`$.*

</div>

<div class="proof">

*Proof.* The same constant positive function $`\mathcal C=\mathcal C_0`$ can be placed on a static FLRW metric, an expanding de Sitter metric, or a contracting FLRW metric at the purely kinematic level. Capacity positivity distinguishes none of them. Within <a href="#eq:action" data-reference-type="ref+label" data-reference="eq:action">[eq:action]</a>, their admissibility is decided by $`F,K,U`$, matter, and initial data rather than by the sign of $`\mathcal C`$ alone. ◻

</div>

# Why a fitted expansion history is not yet a prediction

A flexible scalar–tensor action can reconstruct a chosen background history. This is useful for model building and dangerous for claims of derivation.

<div id="thm:reconstruction" class="theorem">

**Theorem 6** (Background reconstruction degeneracy). *Let $`H(t)`$, $`\rho_{\mathrm m}(t)`$, and $`p_{\mathrm m}(t)`$ be smooth and satisfy <a href="#eq:matter-continuity" data-reference-type="ref+label" data-reference="eq:matter-continuity">[eq:matter-continuity]</a>. Choose a monotone clock $`\mathcal C(t)`$ and a smooth positive function $`F(t)`$. Define
``` math
\begin{align}
 \mathcal K(t)
 &:=
 -2F\dot H-(\rho_{\mathrm m}+p_{\mathrm m})
 -\ddot F+H\dot F,
 \label{eq:reconstructed-kinetic}\\
 \mathcal U(t)
 &:=
 3F H^2-\rho_{\mathrm m}
 -\frac{1}{2}\mathcal K(t)+3H\dot F.
 \label{eq:reconstructed-potential}
\end{align}
```
If $`\mathcal K(t)\geq0`$, then along the selected trajectory the choices
``` math
K(\mathcal C(t))=\frac{\mathcal K(t)}{\dot{\mathcal C}(t)^2},
 \qquad
 U(\mathcal C(t))=\mathcal U(t)
```
reproduce that background. Where $`\dot{\mathcal C}\neq0`$, the scalar equation follows from the metric equations, matter conservation, and the Bianchi identity.*

</div>

<div class="proof">

*Proof.* Substitution of <a href="#eq:reconstructed-kinetic" data-reference-type="ref+label" data-reference="eq:reconstructed-kinetic">[eq:reconstructed-kinetic]</a> into <a href="#eq:friedmann-two" data-reference-type="ref+label" data-reference="eq:friedmann-two">[eq:friedmann-two]</a> makes the second Friedmann equation an identity. Substitution of both reconstructed quantities into <a href="#eq:friedmann-one" data-reference-type="ref+label" data-reference="eq:friedmann-one">[eq:friedmann-one]</a> makes the first equation an identity. The contracted Bianchi identity relates the divergence of the metric equation to the scalar equation. With conserved matter and $`\dot{\mathcal C}\neq0`$, the remaining scalar factor must vanish. ◻

</div>

#### Consequence.

An observed $`H(z)`$ can be replayed by many choices of $`F,K,U`$. Such a reconstruction is not evidence that MTT selected the expansion history. A prediction requires $`F,K,U`$, the source map, and initial data to be fixed independently and then compared with held-out observations.

## A concrete example: the nested standard cosmology

<div id="prop:lcdm" class="proposition">

**Proposition 7** ($`\Lambda`$CDM is a nested limit). *For $`F=M_{\mathrm{Pl}}^2`$, constant $`\mathcal C`$, and $`U=M_{\mathrm{Pl}}^2\Lambda`$, <a href="#eq:action" data-reference-type="ref+label" data-reference="eq:action">[eq:action]</a> reduces at the background level to general relativity with a cosmological constant:
``` math
3M_{\mathrm{Pl}}^2H^2=\rho_{\mathrm m}+M_{\mathrm{Pl}}^2\Lambda,
 \qquad
 -2M_{\mathrm{Pl}}^2\dot H=\rho_{\mathrm m}+p_{\mathrm m}.
```*

</div>

This limit is an important consistency check, but it is not a capacity-based explanation of $`\Lambda`$. A nonconstant alternative must outperform or distinguish itself from this baseline after accounting for all added functions and parameters.

# Transport data are not a metric equation

The MTT transport program may supply an effective current $`J^\mu_{\mathcal C}`$ and a balance law
``` math
\begin{equation}
 \nabla_\mu J^\mu_{\mathcal C}=\sigma_{\mathcal C}.
 \label{eq:capacity-balance}
\end{equation}
```
For a homogeneous current $`J^\mu_{\mathcal C}=q_{\mathcal C}u^\mu`$, <a href="#eq:capacity-balance" data-reference-type="ref+label" data-reference="eq:capacity-balance">[eq:capacity-balance]</a> becomes
``` math
\dot q_{\mathcal C}+3Hq_{\mathcal C}=\sigma_{\mathcal C}.
```
This equation describes dilution, production, or loss of the declared charge density *on a given cosmological geometry*. It does not replace <a href="#eq:friedmann-one,eq:friedmann-two" data-reference-type="ref+label" data-reference="eq:friedmann-one,eq:friedmann-two">[eq:friedmann-one,eq:friedmann-two]</a>. In particular, the $`3Hq_{\mathcal C}`$ term already contains the expansion one might otherwise try to derive from the balance law.

A future source theorem must specify whether $`q_{\mathcal C}`$ equals $`\mathcal C`$, is a function of $`\mathcal C`$, or is an independent transported density. It must also show how its stress tensor or its modification of $`F,K,U`$ follows from the same action. Treating a bookkeeping current as stress-energy without that map would violate the type boundary.

# Horizons and singularities

## Causal horizons

Cosmological horizons are properties of Lorentzian causal structure. In an FLRW spacetime a particle-horizon radius and an event-horizon radius, when the relevant integrals exist, are
``` math
\begin{align}
 R_{\mathrm p}(t)
 &=a(t)\int_{t_{\mathrm i}}^t\frac{\mathrm{d}t'}{a(t')},\\
 R_{\mathrm e}(t)
 &=a(t)\int_t^{t_{\mathrm f}}\frac{\mathrm{d}t'}{a(t')}.
\end{align}
```
For nonzero spatial curvature the apparent-horizon areal radius is
``` math
R_{\mathrm A}=\frac{1}{\sqrt{H^2+k/a^2}}.
```
These notions are not interchangeable; event horizons are global, while apparent horizons depend on a foliation.

<div id="prop:horizon-separation" class="proposition">

**Proposition 8** (A capacity-zero surface is not a causal horizon). *A regular level set $`\mathcal C^{-1}(0)`$ is not, from that fact alone, a particle, event, or apparent horizon. Conversely, a cosmological horizon need not be a zero of $`\mathcal C`$.*

</div>

<div class="proof">

*Proof.* On de Sitter spacetime, a constant positive scalar $`\mathcal C=\mathcal C_0`$ coexists with a cosmological event horizon ; hence capacity zero is not necessary. On Minkowski spacetime, the scalar $`\mathcal C=t`$ has the regular zero set $`t=0`$, which is a spacelike Cauchy surface rather than a causal horizon; hence capacity zero is not sufficient. ◻

</div>

Capacity level sets may still be useful diagnostics of model breakdown. Their geometric relation to a causal horizon requires an additional theorem involving $`g`$, null expansions, or causal accessibility. Area and entropy statements then require the separately typed hypotheses given in the horizon paper .

## Past completeness

<div id="prop:singularity-separation" class="proposition">

**Proposition 9** (Positive capacity does not remove a singularity). *The condition $`\mathcal C>0`$ does not imply bounded curvature or geodesic completeness.*

</div>

<div class="proof">

*Proof.* Take a constant positive scalar on the spatially flat dust solution $`a(t)\propto t^{2/3}`$ for $`t>0`$. Its Ricci scalar diverges as $`t^{-2}`$ toward $`t=0`$, while $`\mathcal C`$ remains positive. The capacity condition does not control the curvature. ◻

</div>

A nonsingular or past-complete model must instead prove the relevant extension and completeness conditions for a solution of <a href="#thm:field-equations" data-reference-type="ref+label" data-reference="thm:field-equations">2</a>. Bounded capacity, bounded $`H`$, or the absence of a capacity-zero surface is not by itself such a proof. Standard geodesic-incompleteness results also show why accelerated expansion does not automatically provide a past completion .

# Time orientation and irreversible evolution

The action <a href="#eq:action" data-reference-type="ref+label" data-reference="eq:action">[eq:action]</a> is time-reversal invariant under the usual transformation of a homogeneous solution. It therefore does not select an arrow of time. A time orientation is part of the Lorentzian background, whereas an entropy arrow requires an irreversible state, boundary condition, coarse graining, or open-system dynamics.

If an entropy current $`s^\mu`$ is supplied and satisfies
``` math
\nabla_\mu s^\mu\geq0,
```
then its integral can orient a thermodynamic arrow on the domain where the inequality holds. Likewise, a declared irreversible capacity law could orient a capacity arrow. Neither inequality follows from the sign of $`\mathcal C`$ or from the covariant action alone. The phrase “capacity exhaustion” is therefore a physical input until its generator and entropy-production theorem are specified.

# Observable map and comparison contract

## Background observables

Given a solution and the normalization $`a(t_0)=1`$, redshift is $`1+z=1/a`$. In the spatially flat case the comoving and luminosity distances are
``` math
\begin{equation}
 \chi(z)=\int_0^z\frac{\mathrm{d}z'}{H(z')},
 \qquad
 d_L(z)=(1+z)\chi(z).
 \label{eq:distance-map}
\end{equation}
```
Useful derived quantities include
``` math
q(z)=-\frac{\ddot a}{aH^2},
 \qquad
 w_{\mathrm{eff}}(z)
 =-1-\frac{2\dot H}{3H^2}.
```
Equations <a href="#eq:friedmann-one,eq:friedmann-two,eq:scalar-flrw" data-reference-type="ref+label" data-reference="eq:friedmann-one,eq:friedmann-two,eq:scalar-flrw">[eq:friedmann-one,eq:friedmann-two,eq:scalar-flrw]</a> and <a href="#eq:distance-map" data-reference-type="ref+label" data-reference="eq:distance-map">[eq:distance-map]</a> are sufficient to produce predictions for background expansion, supernova distances, and baryon-acoustic-oscillation distance combinations after the matter and radiation sectors are fixed.

The standard cosmological data set is already restrictive. CMB anisotropies constrain the early background and perturbations ; supernovae constrain relative luminosity distances ; and BAO constrain radial and transverse distance scales. A capacity model must be compared with the full covariance information rather than with a few plotted central values.

## Perturbations are indispensable

Background agreement is not enough. Perturbing <a href="#eq:metric-field,eq:capacity-field" data-reference-type="ref+label" data-reference="eq:metric-field,eq:capacity-field">[eq:metric-field,eq:capacity-field]</a> determines gravitational slip, the effective clustering strength, scalar propagation, and the growth of matter perturbations. The effective Planck-mass running
``` math
\alpha_M=\frac{\dot F}{HF}
```
is one useful diagnostic, but it is not a complete perturbation theory. The same selected functions used for $`H(z)`$ must also be used for CMB, lensing, structure growth, local-gravity constraints, and gravitational wave propagation. Scalar–tensor effective parameterizations provide a standard comparison language .

## Minimum reproducible comparison packet

A claim of observational viability requires one versioned packet containing:

1.  explicit $`F(\mathcal C)`$, $`K(\mathcal C)`$, $`U(\mathcal C)`$ and source-map formulas;

2.  all dimensional normalizations, initial data, priors, and the Jordan-frame convention;

3.  a background and perturbation solver with numerical tolerances;

4.  named data releases and complete likelihood definitions, including covariances, nuisance parameters, and train/hold-out separation;

5.  posterior or certified parameter intervals and residuals;

6.  comparison with $`\Lambda`$CDM using the true parameter and function count; and

7.  hashes linking the source, solver, inputs, and output tables.

No such fit is claimed in this paper. The nested <a href="#prop:lcdm" data-reference-type="ref+label" data-reference="prop:lcdm">7</a> shows that the action has a standard baseline. It does not show that a nontrivial capacity branch fits the data or predicts a departure.

# Parameter accounting and falsifiability

At its present tier the realization contains three functions $`F,K,U`$, a source map $`\mathfrak s`$, and initial data. A monotone field redefinition can remove one functional redundancy locally, but at least two independent functional degrees of freedom generally remain. This is more freedom than the six-parameter base $`\Lambda`$CDM background and primordial model used in standard fits . The comparison is therefore not won by renaming functions as geometry.

The model becomes sharply falsifiable after upstream selection. Given fixed source data and no target fitting, any of the following is an exit:

- $`F\leq0`$ or a negative Einstein-frame kinetic coefficient;

- failure of the background equations or loss of a regular solution;

- disagreement with distance, CMB, growth, lensing, local-gravity, or gravitational-wave constraints outside the declared uncertainty budget;

- a purported capacity horizon that fails the relevant causal or null-expansion criterion; or

- an arrow-of-time claim without a positive entropy-production law.

The decisive MTT theorem would derive
``` math
\mathfrak s,\quad F,\quad K,\quad U,\quad
 \text{initial state}
```
from the same upper geometry that supplies the accepted capacity operator, while preserving covariance and the current fixed-point and operator interfaces. Until then, <a href="#eq:action" data-reference-type="ref+label" data-reference="eq:action">[eq:action]</a> is a candidate realization and not an inevitable consequence of MTT.

# Relation to established cosmology

The equations in this paper are not a new class of gravitational theory. They are a scalar–tensor effective action, a well-studied extension of general relativity . What is specific to MTT is the proposed interpretation and the stronger demand that the functions be selected by an independently defined admissibility geometry.

This distinction provides a useful benchmark:

- If $`F`$ and $`\mathcal C`$ are constant and $`U=M_{\mathrm{Pl}}^2\Lambda`$, the model is the standard $`\Lambda`$CDM background.

- If $`F`$ varies, the model belongs to the constrained scalar–tensor/modified-gravity landscape.

- If an MTT theorem fixes $`F,K,U`$ before looking at cosmological data, the model acquires genuinely new predictive content.

- If the functions are reconstructed from the observed $`H(z)`$, the result is a profile or fit, not a derivation.

Capacity language may still prove useful by organizing which branch is admissible and when an effective description exits its domain. It does not exempt the model from the Einstein equations, causal definitions, or observational likelihoods appropriate to its declared action.

# Conclusion

The corrected result is narrower and more useful. A coherence-capacity interpretation can be embedded in a covariant cosmological model, and that model has explicit field equations, an exact acceleration test, causal-horizon criteria, and an observational map. None of these structures follows from capacity positivity alone.

The principal mathematical lesson is the reconstruction degeneracy: with freely chosen $`F,K,U`$, many expansion histories can be replayed. The scientific frontier is therefore not to invent another capacity-shaped Friedmann equation. It is to derive the source map and coupling functions from accepted MTT geometry before using cosmological measurements, then run the same branch through background, perturbation, causal, and statistical tests. That would turn the present conditional realization into a predictive cosmology.
