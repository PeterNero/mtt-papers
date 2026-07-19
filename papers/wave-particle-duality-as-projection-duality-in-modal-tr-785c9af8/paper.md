---
abstract: |
  Wave–particle duality is usually presented as a primitive feature of quantum theory: microscopic systems propagate as extended wave amplitudes, interfere through coherent phase relations, and yet appear as localized particle-like events under measurement. Modal Triplet Theory (MTT) reframes this duality as a projection phenomenon. The apparent opposition between “wave” and “particle” is not fundamental. It arises because one finite coherent-sector excitation admits two downstream shadows: a local delta-like shadow and a spectral phase-coherent shadow.

  In an admissible MTT fixed-point regime, the relevant object is the finite coherent kernel
  ``` math
  B_{\mathrm{adm}}
    =
    P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P,
  ```
  where $`A`$ is the fixed-point stabilization operator, $`P`$ is the coherent-sector projector, $`\chi(A)`$ is the admissible spectral window, and
  ``` math
  \tau_{\mathrm{adm}}
    =
    \lambda_\ast^{-1}\log(C_Q/\epsilon_{\mathrm{adm}})
  ```
  is the damping-selected proper-time/heat-time scale. In the local representation, the kernel
  ``` math
  K_{\mathrm{adm}}(x,y)=\langle x|B_{\mathrm{adm}}|y\rangle
  ```
  defines a finite localization profile and recovers the Dirac delta only in the sharp limit. This is the particle shadow. In the spectral representation,
  ``` math
  K_{\mathrm{adm}}(x,y)
    =
    \sum_{n\in \mathrm{coh}}
    \chi(\lambda_n)^2 e^{-\tau_{\mathrm{adm}}\lambda_n}
    \phi_n(x)\phi_n^\ast(y),
  ```
  the same object appears as a weighted coherent modal structure whose phase evolution produces interference. This is the wave shadow.

  The paper strengthens this statement in three ways. First, the delta limit is stated as a distributional convergence theorem. Second, branch damping is formulated as a Schur product quantum channel, with the positivity condition $`D\succeq0`$ ensuring complete positivity and trace preservation. Third, finite detector effects are treated as normalized POVM kernels, so localized detection is a finite survivor-basin selection process rather than a primitive collapse postulate. The double-slit experiment is then a canonical example: branch coherence gives interference, while which-way selection damps off-diagonal branch terms and leaves localized events.

  The main result is a projection-duality theorem: wave-like interference and particle-like localization are not competing ontologies but complementary effective descriptions induced by different projections of one coherent-sector excitation. Standard quantum mechanics is recovered in the sharp coherent limit; MTT supplies the deeper projection architecture from which the dual shadows arise.
author:
- Peter Nero
current_version: v4
date: April 2026
generated_from_main_tex_sha256: 173e420f48f4f521ad9ab10889df18f9923c5b2321f27f19ee1266e1a8c10885
paper_id: wave-particle-duality-as-projection-duality-in-modal-tr-785c9af8
release_state: not_matched_to_zenodo
title: |
  Wave–Particle Duality as Projection Duality in Modal Triplet Theory  
  Pointlike Delta Shadows and Wavelike Spectral Shadows of a Single Coherent Kernel
---

# Purpose and claim discipline

Wave–particle duality is one of the oldest signs that effective physical description is projection-dependent. In one experimental arrangement a microscopic system is described by a phase-coherent amplitude that propagates, diffracts, and interferes. In another arrangement the same system produces a localized detector record. Standard quantum mechanics encodes both facts successfully, but it normally treats their coexistence as a primitive feature of the formalism: states evolve as amplitudes, while measurements return localized outcomes.

The purpose of this paper is to show that this dual appearance follows naturally from the projection architecture of Modal Triplet Theory (MTT). The preceding delta–projection sequence established that Dirac delta distributions should not be read as primitive physical objects whenever finite coherent support is relevant. Rather, they arise as singular downstream limits of finite admissible kernels. The fixed-point kernel construction then replaced arbitrary smoothing by the canonical admissible operator
``` math
\begin{equation}
  B_{\mathrm{adm}}
  =
  P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P,
  \label{eq:purpose-badm}
\end{equation}
```
where $`A`$ is the fixed-point stabilization operator, $`P`$ is the coherent-sector projector, $`\chi(A)`$ is the admissible spectral window, and $`\tau_{\mathrm{adm}}`$ is the damping-selected proper-time/heat-time scale.

The present paper applies this same object to the wave–particle problem. The claim is not that there are two underlying things, one wave-like and one particle-like. Nor is the claim that an object changes its ontology when a detector is introduced. The claim is that a single finite coherent-sector excitation has two different downstream representations. In a local or source representation, the admissible kernel appears as a finite localization profile whose sharp idealization is a Dirac delta. In a spectral or phase representation, the same kernel appears as a weighted coherent modal structure whose retained phases generate interference.

> *Central claim.* Wave-like interference and particle-like localization are two downstream projection shadows of one finite coherent-sector excitation.

Equivalently,
``` math
\begin{equation}
  \boxed{
  \text{wave--particle duality}
  =
  \text{projection duality}.
  }
  \label{eq:purpose-projection-duality}
\end{equation}
```

The word “shadow” is used in the technical MTT sense. A shadow is not an illusion, nor is it a merely subjective description. It is a stable effective representation obtained after projecting a richer coherent structure into a lower-capacity descriptive context. The same upstream coherent excitation may therefore have inequivalent downstream shadows, depending on which projection context is imposed.

## What is being claimed

This paper proves and organizes the following structural claims.

First, the admissible coherent kernel has both a local representation and a spectral representation. In local notation,
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)=\langle x|B_{\mathrm{adm}}|y\rangle
\end{equation}
```
acts as a finite source, response, or detector-amplitude kernel. In spectral notation, under the assumptions stated below,
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)
  =
  \sum_{n\in\mathrm{coh}}
  \chi(\lambda_n)^2 e^{-\tau_{\mathrm{adm}}\lambda_n}
  \phi_n(x)\phi_n^\ast(y).
  \label{eq:purpose-spectral-kernel}
\end{equation}
```
The local representation is the particle-like side. The spectral representation is the wave-like side.

Second, the point-particle description is recovered only as a limiting representation. In a sharp spectral/proper-time limit,
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)\longrightarrow \delta(x-y)
\end{equation}
```
in the distributional sense. Thus MTT does not postulate literal point particles. It explains why point-particle descriptions are successful when the finite coherent width is below the resolution scale of the probing apparatus.

Third, wave-like behavior is identified operationally with preserved off-diagonal coherence: superposition, retained relative phase, and observable cross terms. If two branches $`a,b`$ remain in the same coherent sector, then interference terms survive. If a measurement arrangement distinguishes the branches strongly enough, those off-diagonal terms are damped.

Fourth, branch damping is not introduced as an arbitrary visibility factor. It must define a valid quantum channel on the branch density matrix. In finite branch bases this means that the damping matrix $`D=(D_{ab})`$ must satisfy
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1,
\end{equation}
```
so that the Schur map
``` math
\begin{equation}
  \rho\mapsto D\circ\rho
\end{equation}
```
is completely positive and trace preserving. This condition is essential: not every proposed interference-damping rule is physically admissible.

Fifth, measurement is treated as finite survivor-basin selection. A detector is represented by a measurement context $`\mathsf M`$, with its own device-sector data
``` math
\begin{equation}
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\}_{i\in I},\mathfrak B_{\mathsf M}).
\end{equation}
```
Here $`\mathfrak B_{\mathsf M}=\{B_i^{(\mathsf M)}\}_{i\in I}`$ denotes the survivor-basin partition. Different devices can therefore disturb the same coherent excitation in different ways, select different branch bases, and induce different damping matrices
``` math
\begin{equation}
  D_{ab}^{(\mathsf M)}
  =
  \exp[-\tau_{\mathsf M}\Lambda_{ab}^{(\mathsf M)}],
\end{equation}
```
when the exponent defines an admissible positive kernel. The exact detector record is not a pre-existing context-free point value revealed without disturbance. It is a stabilized downstream record produced by the device-specific evolve–project–stabilize cycle.

## What is not being claimed

This paper does not claim that standard quantum mechanics is false. It does not deny the usefulness of wavefunctions, Hilbert spaces, amplitudes, density matrices, POVMs, or projection-valued idealizations. Instead, it explains why these structures appear as effective descriptions inside finite admissible regimes.

This paper also does not claim that particles are ordinary extended classical blobs. The MTT claim is more precise. The upstream object is not a little ball, and it is not a classical wave spread through space. It is a stable coherent-sector excitation. That excitation can appear pointlike when probed locally and wavelike when represented spectrally.

Thus
``` math
\begin{equation}
  \text{particle}\neq \text{literal mathematical point},
\end{equation}
```
and
``` math
\begin{equation}
  \text{wave}\neq \text{separate physical substance}.
\end{equation}
```
Rather,
``` math
\begin{equation}
  \text{particle shadow}
  =
  \text{localized delta-limit representation},
\end{equation}
```
while
``` math
\begin{equation}
  \text{wave shadow}
  =
  \text{spectral phase-coherent representation}.
\end{equation}
```
Both are generated by the same admissible MTT structure.

Nor does this paper compute all sector-specific numerical parameters. The quantities $`A`$, $`P`$, $`\chi`$, $`\lambda_\ast`$, $`C_Q`$, $`\epsilon_{\mathrm{adm}}`$, and the relevant detector or branch-separation metric must be supplied by the physical sector under consideration. The present claim is conditional but sharp: once those data are supplied by an admissible fixed-point regime, no independent wave–particle switch and no arbitrary smoothing width remain.

## Relation to probability and the Born rule

A common source of confusion is to conflate two different questions:
``` math
\begin{align}
  &\text{Which outcome is selected?}
  \label{eq:which-outcome}\\
  &\text{How much interference remains before or during selection?}
  \label{eq:how-much-interference}
\end{align}
```
MTT treats these as related but distinct questions.

The first question is answered by basin-measure structure. In the Born-rule shadow-bridge program, outcome probabilities are associated with the relative measures of stabilized selection basins. Schematically,
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i)}{\sum_j\mu(B_j)},
  \label{eq:basin-born}
\end{equation}
```
where $`B_i`$ is the basin of the $`i`$-th stabilized outcome and $`\mu`$ is the relevant admissibility-weighted basin measure. This is the probability side of measurement.

The second question is answered by branch-coherence survival. Before a unique outcome is stabilized, or in arrangements where alternatives are recombined, the off-diagonal terms $`\rho_{ab}`$ determine interference visibility. Device-induced disturbance acts on these terms by an admissible damping channel,
``` math
\begin{equation}
  \rho_{ab}\longmapsto D_{ab}^{(\mathsf M)}\rho_{ab}.
  \label{eq:branch-damping-purpose}
\end{equation}
```
This is the visibility side of measurement.

Thus this paper does not replace Born probabilities with visibility damping. Instead it keeps the two roles separate:
``` math
\begin{equation}
  \boxed{
  \text{basin measure determines stabilized outcome frequencies},
  }
\end{equation}
```
whereas
``` math
\begin{equation}
  \boxed{
  \text{branch coherence determines interference visibility}.
  }
\end{equation}
```
This distinction is crucial for the double-slit experiment. The screen distribution is shaped by coherent interference when $`D_{12}\approx1`$, while individual screen records are still localized detector outcomes whose frequencies are governed by the relevant measurement effects and basin weights.

## Relation to measurement as disturbance and stabilization

The measurement picture used here is the same one used throughout the MTT measurement sequence. A measuring device is not a passive reader of a pre-existing classical value. It is a localized disturbance coupled to a finite-capacity coherent sector. After the disturbance, the system undergoes re-coherence: high-frequency or inadmissible components are damped, the coherent projector selects the retained content, and the resulting state stabilizes into one of the available survivor basins.

In symbolic form, a measurement context induces the sequence
``` math
\begin{equation}
  \text{coherent evolution}
  \longrightarrow
  \text{localized disturbance}
  \longrightarrow
  \text{projection}
  \longrightarrow
  \text{survivor-basin stabilization}.
  \label{eq:evolve-project-stabilize-purpose}
\end{equation}
```
Different devices implement different versions of this sequence. A weak which-way marker, a strong absorbing detector, a Stern–Gerlach magnet, a delayed-choice recombination stage, and a phase-sensitive interferometer do not impose the same disturbance. They define different measurement contexts $`\mathsf M`$, different branch partitions, and different damping kernels.

This is why the device matters in the double-slit experiment. With no which-way device, the two path branches remain mutually coherent and the off-diagonal term survives. With a weak which-way device, the off-diagonal term is partially damped. With a strong which-way device, the path branches are separated into distinct survivor basins and the interference term is suppressed. The outcome is exact within the selected measurement context because the device stabilizes a definite record, but the context itself is created by the device-specific disturbance.

## Why this is not merely decoherence

The formal appearance of a damping factor
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab}
\end{equation}
```
resembles ordinary decoherence. The relation is real but incomplete. Environmental decoherence explains how entanglement with uncontrolled degrees of freedom suppresses off-diagonal terms in a reduced density matrix. MTT includes such suppression as one possible shadow, but the present structure is broader.

In MTT, branch damping is tied to admissibility, coherent projection, detector-sector disturbance, and survivor-basin stabilization. The damping factor is not merely a phenomenological loss of phase coherence. It must be compatible with a finite measurement kernel, a valid quantum channel, and a basin-selection process. Decoherence suppresses interference; MTT also asks which stabilized branch is selected, which basin measure governs its frequency, and which finite coherent kernel underlies the local and spectral shadows in the first place.

## Paper structure

The paper proceeds as follows. The next section fixes the analytic setting and the admissible kernel. We then state the precise delta-limit theorem, giving the mathematical basis for the particle shadow. The following section develops the spectral representation and coherent phase evolution, giving the mathematical basis for the wave shadow. We then formulate finite measurement effects, Schur-channel branch damping, and the operator version of the double-slit experiment. After that we discuss device-dependent disturbance, further experimental modules, recovery of standard quantum mechanics, relation to existing accounts, and the failure modes of the construction.

The intended result is a rigorous structural synthesis:
``` math
\begin{equation}
  \boxed{
  \text{one admissible coherent kernel}
  \quad\Longrightarrow\quad
  \begin{cases}
  \text{delta-like local particle shadow},\\
  \text{spectral phase wave shadow},\\
  \text{finite measurement-selection shadow}.
  \end{cases}
  }
  \label{eq:purpose-summary}
\end{equation}
```

# Analytic setting and admissible coherent kernels

This section fixes the analytic assumptions used in the structural theorems below. The goal is not to introduce a new quantum formalism, but to identify the minimal operator-theoretic data needed for the local and spectral shadows of a coherent MTT excitation to be well-defined.

## Base Hilbert space and fixed-point operator

Let $`X`$ be a compact smooth Riemannian manifold without boundary, or a compact manifold with boundary equipped with a self-adjoint elliptic boundary condition. More generally, $`X`$ may be replaced by a compact admissible chart and scalar functions by sections of a Hermitian vector bundle. We write $`L^2(X)`$ for the Hilbert space of square-integrable sections.

Let
``` math
\begin{equation}
  A\ge 0
\end{equation}
```
be a nonnegative self-adjoint elliptic operator on $`L^2(X)`$, with compact resolvent. The spectral theorem gives an orthonormal basis of smooth eigenfunctions or eigensections
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
  \qquad
  0\le \lambda_0\le\lambda_1\le\cdots,
  \label{eq:A-spectrum}
\end{equation}
```
where eigenvalues are repeated according to multiplicity. In MTT, $`A`$ is interpreted as the linearized fixed-point stabilization, damping, or admissibility operator in the coherent chart under consideration.

The compact setting is used to state the spectral results without unnecessary measure-theoretic technicalities. In flat noncompact charts, such as $`X=\mathbb R^d`$, the corresponding statements are obtained by Fourier transform and convergence on Schwartz test functions. For example, $`A=-\Delta`$ has continuous spectral parameter $`k^2`$, and heat kernels are interpreted as tempered-distribution kernels.

<div id="ass:fixed-point-spectral-data" class="assumption">

**Assumption 1** (Fixed-point spectral data). The fixed-point coherent sector is specified by:

1.  a nonnegative self-adjoint elliptic operator $`A`$ with compact resolvent;

2.  an isolated coherent spectral cluster $`\Omega_{\rm coh}\subset\sigma(A)`$;

3.  the Riesz spectral projector
    ``` math
    \begin{equation}
        P
        =
        \frac{1}{2\pi i}
        \oint_\Gamma (z-A)^{-1}\,\mathrm{d}z,
        \label{eq:riesz-P}
    \end{equation}
    ```
    where $`\Gamma`$ encloses $`\Omega_{\rm coh}`$ and no discarded spectrum;

4.  the complementary projector
    ``` math
    \begin{equation}
        Q=I-P;
    \end{equation}
    ```

5.  a discarded-sector gap
    ``` math
    \begin{equation}
        A|_{\mathrm{Ran}Q}\ge \lambda_\ast I,
        \qquad
        \lambda_\ast>0;
        \label{eq:discarded-gap}
    \end{equation}
    ```

6.  an admissible spectral window $`\chi:[0,\infty)\to[0,1]`$ subordinate to the coherent spectral split.

</div>

Because $`P`$ is a Riesz projector of $`A`$, it commutes with $`A`$ and preserves the smooth spectral domain. This avoids a common ambiguity: a merely bounded projector commuting with $`A`$ is not enough, by itself, to guarantee the smooth kernel properties used below. In the sharp cluster realization, $`\chi(A)=P`$. Smooth windows may be used when a transition layer inside a gap-protected admissible neighborhood is required, but such windows are subordinate to the same spectral split and are not independent phenomenological regulators.

<div id="def:coh-discarded-sectors" class="definition">

**Definition 2** (Coherent and discarded sectors). The retained coherent sector and discarded sector are
``` math
\begin{equation}
  \mathcal{H}_{\rm coh}:=\mathrm{Ran}P,
  \qquad
  \mathcal{H}_{\rm inc}:=\mathrm{Ran}Q.
\end{equation}
```
A vector $`\Psi\in L^2(X)`$ decomposes as
``` math
\begin{equation}
  \Psi=P\Psi+Q\Psi.
\end{equation}
```
The coherent component $`P\Psi`$ is the part represented by the effective physical description. The discarded component $`Q\Psi`$ is not necessarily nonexistent; it is inadmissible for the chosen effective chart.

</div>

## Damping-selected proper-time scale

The admissible kernel contains a heat/proper-time parameter. In ordinary regularization this parameter is often chosen by hand. In the MTT fixed-point setting, it is selected by the damping required to reduce discarded-sector leakage below an admissibility tolerance.

Let $`\Phi_t`$ denote the local linearized or locally controlled damping flow. In the simplest self-adjoint linear case,
``` math
\begin{equation}
  \Phi_t=e^{-tA}.
\end{equation}
```
Assume that the discarded sector satisfies
``` math
\begin{equation}
  \left\lVert Q\Phi_tQ \right\rVert
  \le
  C_Qe^{-\lambda_\ast t},
  \qquad
  t\ge0,
  \label{eq:discarded-sector-bound}
\end{equation}
```
for some $`C_Q\ge1`$. In the canonical self-adjoint spectral case with $`A|_{\mathrm{Ran}Q}\ge\lambda_\ast I`$, one has $`C_Q=1`$.

<div id="def:admissible-residual-leakage" class="definition">

**Definition 3** (Admissible residual leakage). Let $`0<\epsilon_{\mathrm{adm}}<1`$. A stabilization step of heat/proper-time $`t`$ is $`\epsilon_{\mathrm{adm}}`$-admissible if
``` math
\begin{equation}
  \left\lVert Q\Phi_tQ \right\rVert\le \epsilon_{\mathrm{adm}}.
\end{equation}
```
The parameter $`\epsilon_{\mathrm{adm}}`$ is a regime-dependent admissibility tolerance. It may be determined by basin separation, detector resolution, closure strain, or other sector data. It is not a universal constant in this paper.

</div>

<div id="prop:minimal-admissible-time" class="proposition">

**Proposition 4** (Minimal admissible heat/proper-time). *Under the damping estimate <a href="#eq:discarded-sector-bound" data-reference-type="eqref" data-reference="eq:discarded-sector-bound">[eq:discarded-sector-bound]</a>, every
``` math
\begin{equation}
  t\ge
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\mathrm{adm}}}
\end{equation}
```
is $`\epsilon_{\mathrm{adm}}`$-admissible. The minimal time selected by this bound is
``` math
\begin{equation}
  \tau_{\mathrm{adm}}
  :=
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\mathrm{adm}}}.
  \label{eq:tau-adm}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The bound <a href="#eq:discarded-sector-bound" data-reference-type="eqref" data-reference="eq:discarded-sector-bound">[eq:discarded-sector-bound]</a> gives
``` math
\begin{equation}
  \left\lVert Q\Phi_tQ \right\rVert
  \le
  C_Qe^{-\lambda_\ast t}.
\end{equation}
```
Requiring the right-hand side to be at most $`\epsilon_{\mathrm{adm}}`$ gives
``` math
\begin{equation}
  C_Qe^{-\lambda_\ast t}\le\epsilon_{\mathrm{adm}}.
\end{equation}
```
Taking logarithms yields
``` math
\begin{equation}
  t\ge
  \lambda_\ast^{-1}\log(C_Q/\epsilon_{\mathrm{adm}}).
\end{equation}
```
 ◻

</div>

<div id="rem:heat-time" class="remark">

*Remark 5* (Heat-time rather than clock time). The parameter $`\tau_{\mathrm{adm}}`$ is a proper-time/heat-time parameter for the semigroup generated by $`A`$. If $`A`$ is Laplace-type and compared to $`k^2`$, then in units $`\hbar=c=1`$,
``` math
\begin{equation}
  [A]=E^2,
  \qquad
  [\tau_{\mathrm{adm}}]=E^{-2}.
\end{equation}
```
The corresponding coherence length scale is
``` math
\begin{equation}
  \ell_{\rm coh}\sim \sqrt{\tau_{\mathrm{adm}}},
\end{equation}
```
and the effective coherence-energy scale is
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim \tau_{\mathrm{adm}}^{-1/2}.
\end{equation}
```

</div>

## The admissible coherent kernel

<div id="def:admissible-coherent-operator" class="definition">

**Definition 6** (Admissible coherent operator). Given the fixed-point data of Assumption <a href="#ass:fixed-point-spectral-data" data-reference-type="ref" data-reference="ass:fixed-point-spectral-data">1</a> and the damping-selected scale $`\tau_{\mathrm{adm}}`$, define
``` math
\begin{equation}
  B_{\mathrm{adm}}
  :=
  P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P.
  \label{eq:Badm-definition}
\end{equation}
```
When $`B_{\mathrm{adm}}`$ has an integral kernel, we write
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)
  :=
  \langle x|B_{\mathrm{adm}}|y\rangle.
  \label{eq:Kadm-definition}
\end{equation}
```

</div>

Because $`A`$ is self-adjoint and $`P,\chi(A)`$ are defined by functional calculus, the operator $`B_{\mathrm{adm}}`$ is positive and bounded. For $`\tau_{\mathrm{adm}}>0`$, elliptic heat-kernel regularity implies that $`B_{\mathrm{adm}}`$ is smoothing on the retained spectral sector. In a finite-rank coherent cluster, $`B_{\mathrm{adm}}`$ has a smooth kernel even at $`\tau_{\mathrm{adm}}=0`$.

<div id="prop:spectral-form" class="proposition">

**Proposition 7** (Spectral form of the admissible kernel). *Under Assumption <a href="#ass:fixed-point-spectral-data" data-reference-type="ref" data-reference="ass:fixed-point-spectral-data">1</a>, suppose $`A\phi_n=\lambda_n\phi_n`$ is an orthonormal spectral resolution. Then
``` math
\begin{equation}
  B_{\mathrm{adm}}f
  =
  \sum_n
  p_n\chi(\lambda_n)^2 e^{-\tau_{\mathrm{adm}}\lambda_n}
  \langle \phi_n,f\rangle\phi_n,
  \label{eq:Badm-spectral-action}
\end{equation}
```
where $`p_n=1`$ if $`\phi_n\in\mathrm{Ran}P`$ and $`p_n=0`$ otherwise. Consequently,
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)
  =
  \sum_{n\in\mathrm{coh}}
  \chi(\lambda_n)^2 e^{-\tau_{\mathrm{adm}}\lambda_n}
  \phi_n(x)\phi_n^\ast(y).
  \label{eq:Kadm-spectral}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Since $`P`$, $`\chi(A)`$, and $`e^{-\tau_{\mathrm{adm}}A}`$ are all functions of $`A`$ on the spectral decomposition, they are diagonal in the same eigenbasis. Applying the product $`P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P`$ to $`f=\sum_n\langle\phi_n,f\rangle\phi_n`$ gives <a href="#eq:Badm-spectral-action" data-reference-type="eqref" data-reference="eq:Badm-spectral-action">[eq:Badm-spectral-action]</a>. The kernel formula follows by writing the corresponding Schwartz kernel of the spectral expansion. ◻

</div>

<div id="rem:kernel-not-density" class="remark">

*Remark 8* (Amplitude kernel versus probability density). The kernel $`K_{\mathrm{adm}}(x,y)`$ should not be assumed to be a probability density. In general it is a finite source, response, or amplitude kernel and may have oscillatory structure depending on the spectral window. Positive probabilities are obtained from positive effects, for example
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
\end{equation}
```
where $`k_x(y)=K_{\rm det}(y,x)`$, or more generally from a POVM satisfying the normalization conditions stated below. This distinction prevents the pointlike “particle shadow” from being misread as a classical density blob.

</div>

## Local and spectral readings

The same kernel $`K_{\mathrm{adm}}`$ has two readings.

First, fixing $`y=x_0`$, the function
``` math
\begin{equation}
  x\longmapsto K_{\mathrm{adm}}(x,x_0)
\end{equation}
```
is a finite local response to a source centered at $`x_0`$. If the effective kernel width is below the resolving power of a detector, this response is operationally indistinguishable from a point source. This is the local or particle-like shadow.

Second, the expansion <a href="#eq:Kadm-spectral" data-reference-type="eqref" data-reference="eq:Kadm-spectral">[eq:Kadm-spectral]</a> expresses the same kernel as a weighted sum of coherent modes. If a coherent phase generator $`H_{\rm coh}`$ transports these retained modes unitarily, then relative phases between modal or branch components produce interference. This is the spectral or wave-like shadow.

The paper’s central thesis is that these are not two objects. They are two representations of one admissible coherent operator.

## Detector-sector kernels

Measurement introduces device-specific data. A detector is not modeled by an arbitrary external delta function. It is represented by a detector-sector instance of the same admissible kernel construction.

<div id="def:detector-sector-kernel" class="definition">

**Definition 9** (Detector-sector admissible kernel). A measurement context $`\mathsf M`$ supplies detector-sector data
``` math
\begin{equation}
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M}).
\end{equation}
```
The associated detector filter is denoted
``` math
\begin{equation}
  F_{\mathsf M}
  =
  P_{\mathsf M}\chi_{\mathsf M}(A_{\mathsf M})
  e^{-\tau_{\mathsf M}A_{\mathsf M}}
  \chi_{\mathsf M}(A_{\mathsf M})P_{\mathsf M}.
  \label{eq:detector-filter-F}
\end{equation}
```
Its kernel is denoted
``` math
\begin{equation}
  K_{\mathsf M}(y,x)
  =
  \langle y|F_{\mathsf M}|x\rangle.
  \label{eq:detector-kernel-F}
\end{equation}
```
When the context is a position-sensitive detector we also write
``` math
\begin{equation}
  K_{\rm det}(y,x):=K_{\mathsf M}(y,x).
\end{equation}
```

</div>

Thus $`K_{\rm det}`$ is not an extra arbitrary smoothing function. It is the detector-sector realization of the same MTT admissible-kernel architecture. Different devices may have different $`A_{\mathsf M}`$, $`P_{\mathsf M}`$, $`\chi_{\mathsf M}`$, and $`\tau_{\mathsf M}`$, and therefore disturb and select the coherent excitation differently.

## Finite effects and normalized detection

Given a detector kernel $`K_{\rm det}`$, define the rank-one effect density
``` math
\begin{equation}
  E_x(y,z)
  =
  K_{\rm det}(y,x)K_{\rm det}^\ast(z,x).
  \label{eq:finite-effect-kernel}
\end{equation}
```
Equivalently,
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
  \qquad
  k_x(y)=K_{\rm det}(y,x).
\end{equation}
```

For a probability-conserving detector on the retained sector, the effects satisfy the POVM normalization
``` math
\begin{equation}
  \int_X E_x\,\mathrm{d}x
  =
  I_{\rm coh}.
  \label{eq:povm-normalization}
\end{equation}
```
Then a state $`\rho`$ gives detection density
``` math
\begin{equation}
  p(x)=\mathop{\mathrm{tr}}(\rho E_x),
\end{equation}
```
and
``` math
\begin{equation}
  \int_X p(x)\,\mathrm{d}x
  =
  \mathop{\mathrm{tr}}(\rho I_{\rm coh}).
\end{equation}
```
For normalized states on the retained sector, this equals one.

<div id="rem:open-detectors" class="remark">

*Remark 10* (Open detectors and leakage). If the detector has unobserved discarded channels, then one may instead have
``` math
\begin{equation}
  \int_X E_x\,\mathrm{d}x
  \le
  I_{\rm coh}.
\end{equation}
```
The missing probability corresponds to loss into channels not recorded by the chosen detector context. The closed-detector case <a href="#eq:povm-normalization" data-reference-type="eqref" data-reference="eq:povm-normalization">[eq:povm-normalization]</a> is used when discussing ordinary normalized detection statistics.

</div>

## Operational meanings of particle-like and wave-like

The words “particle-like” and “wave-like” are used operationally.

<div id="def:particle-like" class="definition">

**Definition 11** (Particle-like behavior). An excitation is particle-like relative to a detector context $`\mathsf M`$ when:

1.  detector effects $`E_i^{(\mathsf M)}`$ stabilize discrete records;

2.  the relevant detector kernel width is below the resolution scale of the apparatus;

3.  the sharp idealization of those effects is a delta/PVM limit;

4.  repeated trials yield localized records distributed according to the appropriate measurement probabilities.

</div>

<div id="def:wave-like" class="definition">

**Definition 12** (Wave-like behavior). An excitation is wave-like relative to an experimental context when:

1.  it supports coherent superposition of retained branches or modes;

2.  relative phases between those branches or modes are preserved;

3.  observable probabilities contain off-diagonal cross terms;

4.  those cross terms are visible as interference, diffraction, or phase-sensitive modulation.

</div>

These definitions make the main claim precise. MTT does not assert that an entity is “really” a wave or “really” a particle. It asserts that particle-like and wave-like behavior are context-dependent downstream manifestations of a coherent-sector excitation.

# The particle shadow: localization as a delta limit

This section makes precise the sense in which pointlike particle behavior is a limiting description of finite coherent support. The claim is not that MTT replaces particles by classical extended objects. The claim is that the mathematical point source is the sharp idealization of a finite admissible kernel.

## Finite local response

Let $`x_0\in X`$. The local response of the coherent sector to a source centered at $`x_0`$ is represented by the kernel section
``` math
\begin{equation}
  x\longmapsto K_{\mathrm{adm}}(x,x_0).
  \label{eq:local-response-section}
\end{equation}
```
In the ideal point-particle description one instead writes
``` math
\begin{equation}
  x\longmapsto \delta(x-x_0).
\end{equation}
```
MTT reverses the hierarchy. The finite object $`K_{\mathrm{adm}}(x,x_0)`$ is native to a finite admissible regime; the Dirac delta is recovered only after an idealizing limit.

For a source amplitude $`J`$ localized near $`x_0`$, the coherent response is
``` math
\begin{equation}
  (B_{\rm adm}J)(x)
  =
  \int_X K_{\mathrm{adm}}(x,y)J(y)\,\mathrm{d}y.
  \label{eq:kernel-response-source}
\end{equation}
```
If $`J=\delta_{x_0}`$ is used as an ideal test distribution, then
``` math
\begin{equation}
  (B_{\rm adm}\delta_{x_0})(x)
  =
  K_{\mathrm{adm}}(x,x_0).
\end{equation}
```
Thus even a formally point-supported input is represented downstream by a finite coherent response.

<div id="rem:not-classical-density" class="remark">

*Remark 13* (Not a classical matter density). The function $`x\mapsto K_{\mathrm{adm}}(x,x_0)`$ is a response amplitude or kernel section. It should not be read as a positive classical matter density unless additional positivity conditions are present. Detection probabilities are computed from positive effects, such as $`E_x=|k_x\rangle\langle k_x|`$, or from a normalized POVM. This distinction matters: the particle shadow is a localization limit of the coherent kernel, not a claim that particles are small classical blobs.

</div>

## Resolution-dependent pointlikeness

Let $`\ell_{\rm coh}`$ denote the characteristic width of the finite coherent kernel in the local chart. In heat-kernel models on a flat chart,
``` math
\begin{equation}
  \ell_{\rm coh}\sim \sqrt{\tau_{\mathrm{adm}}}.
  \label{eq:ell-coh}
\end{equation}
```
More precisely, for the Euclidean heat kernel
``` math
\begin{equation}
  K_\tau(x,y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(-\frac{|x-y|^2}{4\tau}\right),
  \label{eq:flat-heat-kernel}
\end{equation}
```
the root-mean-square width is of order $`\sqrt{\tau}`$, with convention-dependent numerical factors.

Let $`\ell_{\rm res}`$ be the spatial resolution of the probing apparatus. The coherent excitation is pointlike relative to that apparatus when
``` math
\begin{equation}
  \ell_{\rm coh}\ll \ell_{\rm res}.
  \label{eq:pointlike-resolution}
\end{equation}
```
Equivalently, if the experiment probes momenta up to $`E_{\rm probe}`$, while the coherent scale is
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim \tau_{\mathrm{adm}}^{-1/2},
\end{equation}
```
then the pointlike approximation is valid when
``` math
\begin{equation}
  E_{\rm probe}\ll \Lambda_{\rm eff}.
  \label{eq:pointlike-energy}
\end{equation}
```

<div id="def:effective-point-particle" class="definition">

**Definition 14** (Effective point particle). An excitation is an effective point particle relative to a detector context $`\mathsf M`$ if its detector-sector localization width is below the resolution scale of $`\mathsf M`$, so that the finite effects $`E_x^{(\mathsf M)}`$ are operationally indistinguishable from sharp position effects on the retained sector.

</div>

Thus pointlikeness is not absolute. It is a relation between a coherent support scale and a probing scale.

## Sharp spectral/proper-time limit

We now state the precise delta-limit theorem used throughout the paper. The statement is standard spectral analysis, but its interpretation is central for MTT.

Let $`P_N=\mathbf 1_{[0,\Lambda_N]}(A)`$ be the spectral projector of $`A`$ onto eigenvalues at most $`\Lambda_N`$, with
``` math
\begin{equation}
  \Lambda_N\to\infty.
\end{equation}
```
Let
``` math
\begin{equation}
  B_{N,\tau}
  :=
  P_N e^{-\tau A}P_N.
  \label{eq:BNtau}
\end{equation}
```
When $`B_{N,\tau}`$ has a kernel, denote it by $`K_{N,\tau}(x,y)`$.

<div id="thm:delta-limit" class="theorem">

**Theorem 15** (Delta limit of finite coherent kernels). *Let $`X`$ be compact and $`A\ge0`$ be self-adjoint elliptic with compact resolvent. Let $`\tau_N\downarrow0`$ and $`\Lambda_N\to\infty`$. Then, for every $`f\in C^\infty(X)`$,
``` math
\begin{equation}
  B_{N,\tau_N}f\longrightarrow f
\end{equation}
```
in $`C^\infty(X)`$. Equivalently,
``` math
\begin{equation}
  K_{N,\tau_N}(x,y)
  \longrightarrow
  \delta(x-y)
\end{equation}
```
in the distributional sense on $`X\times X`$.*

</div>

<div class="proof">

*Proof.* Write
``` math
\begin{equation}
  f-B_{N,\tau_N}f
  =
  (I-P_N)f
  +
  P_N(I-e^{-\tau_NA})P_N f.
  \label{eq:delta-proof-split}
\end{equation}
```
The first term tends to zero in all Sobolev norms because spectral projectors converge strongly to the identity on smooth functions, and smooth functions have rapidly decaying spectral coefficients.

For the second term, fix a Sobolev index $`s`$. Choose $`M>s`$. Since $`f\in C^\infty(X)`$,
``` math
\begin{equation}
  \sum_n (1+\lambda_n)^M |\langle\phi_n,f\rangle|^2<\infty.
\end{equation}
```
For each fixed $`n`$,
``` math
\begin{equation}
  1-e^{-\tau_N\lambda_n}\to0.
\end{equation}
```
Moreover, the Sobolev-weighted summands are dominated by a summable multiple of $`(1+\lambda_n)^M|\langle\phi_n,f\rangle|^2`$. Dominated convergence gives convergence to zero in $`H^s`$. Since $`s`$ is arbitrary, Sobolev embedding gives convergence in $`C^\infty(X)`$. The distributional convergence of kernels is the kernel formulation of strong convergence to the identity on test functions. ◻

</div>

<div id="rem:meaning-sharp-limit" class="remark">

*Remark 16* (Meaning of the sharp limit). The theorem does not say that the physical coherent kernel is literally a Dirac delta. It says that the Dirac delta is recovered when:

1.  coherent bandwidth becomes complete;

2.  the proper-time width tends to zero;

3.  no discarded sector remains unresolved.

A finite-capacity coherent regime does not satisfy these idealizations exactly. Its native object is the finite kernel.

</div>

## Finite-width correction estimates

The sharp limit is useful, but finite-width estimates are more physically meaningful. The difference between a sharp retained description and the admissibly filtered description has three conceptually distinct sources:

1.  loss from discarding the noncoherent sector;

2.  loss from the spectral acceptance window $`\chi(A)`$;

3.  smoothing from the finite heat/proper-time factor $`e^{-\tau_{\rm adm}A}`$.

For $`f\in L^2(X)`$, using
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)P,
\end{equation}
```
one has the exact decomposition
``` math
\begin{align}
  f-B_{\rm adm}f
  &=
  (I-P)f
  +
  P\bigl(I-\chi(A)^2\bigr)Pf
  \nonumber\\
  &\quad+
  P\chi(A)\bigl(I-e^{-\tau_{\rm adm}A}\bigr)\chi(A)Pf.
  \label{eq:three-source-error-decomposition}
\end{align}
```
The three terms are respectively:
``` math
\begin{align}
  (I-P)f
  &=
  \text{discarded noncoherent component},
  \\
  P\bigl(I-\chi(A)^2\bigr)Pf
  &=
  \text{spectral-window loss},
  \\
  P\chi(A)\bigl(I-e^{-\tau_{\rm adm}A}\bigr)\chi(A)Pf
  &=
  \text{finite proper-time smoothing}.
\end{align}
```

<div class="proof">

*Proof.* Insert $`I=P+(I-P)`$:
``` math
\begin{equation}
  f-B_{\rm adm}f
  =
  (I-P)f
  +
  P f
  -
  P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)P f.
\end{equation}
```
Since $`P`$, $`\chi(A)`$, and $`e^{-\tau_{\rm adm}A}`$ commute by functional calculus on the spectral sector, write
``` math
\begin{align}
  P f
  -
  P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)P f
  &=
  P f
  -
  P\chi(A)^2P f
  \nonumber\\
  &\quad+
  P\chi(A)^2P f
  -
  P\chi(A)e^{-\tau_{\rm adm}A}\chi(A)P f
  \\
  &=
  P\bigl(I-\chi(A)^2\bigr)P f
  \nonumber\\
  &\quad+
  P\chi(A)\bigl(I-e^{-\tau_{\rm adm}A}\bigr)\chi(A)P f.
\end{align}
```
This gives <a href="#eq:three-source-error-decomposition" data-reference-type="eqref" data-reference="eq:three-source-error-decomposition">[eq:three-source-error-decomposition]</a>. ◻

</div>

In the common sharp-window case where $`f\in\mathrm{Ran}P`$ and $`\chi(A)f=f`$, the first two terms vanish and only finite proper-time smoothing remains. If the relevant spectral support of $`f`$ lies in
``` math
\begin{equation}
  \sigma(A|_{\mathrm{Ran}P})\subset[0,\Lambda_{\rm coh}],
\end{equation}
```
then
``` math
\begin{equation}
  \|f-B_{\rm adm}f\|
  \le
  \bigl(1-e^{-\tau_{\rm adm}\Lambda_{\rm coh}}\bigr)\|f\|.
  \label{eq:finite-width-bound}
\end{equation}
```
For
``` math
\begin{equation}
  \tau_{\rm adm}\Lambda_{\rm coh}\ll1,
\end{equation}
```
this gives
``` math
\begin{equation}
  \|f-B_{\rm adm}f\|
  \le
  \tau_{\rm adm}\Lambda_{\rm coh}\|f\|
  +
  O(\tau_{\rm adm}^2\Lambda_{\rm coh}^2)\|f\|.
  \label{eq:small-tau-bound}
\end{equation}
```

<div id="prop:resolution-criterion" class="proposition">

**Proposition 17** (Resolution criterion from finite-width error). *Let $`O`$ be an observable whose relevant spectral support is bounded by $`\Lambda_{\rm obs}`$. If the state is already in the accepted coherent window and
``` math
\begin{equation}
  \tau_{\rm adm}\Lambda_{\rm obs}\ll \eta,
  \label{eq:resolution-eta}
\end{equation}
```
where $`\eta`$ is the experimental tolerance, then the finite coherent kernel and the sharp delta idealization are indistinguishable for that observable up to tolerance $`\eta`$.*

</div>

<div class="proof">

*Proof.* Under the accepted-window assumptions, apply <a href="#eq:finite-width-bound" data-reference-type="eqref" data-reference="eq:finite-width-bound">[eq:finite-width-bound]</a> on the observable’s retained spectral support and use $`1-e^{-x}\le x`$ for $`x\ge0`$. ◻

</div>

This is the operational content of pointlikeness in MTT. A particle appears pointlike when all accessible observables lie far below the coherent cutoff scale and when projection/window loss is negligible in the sector being probed.

## Point sources, propagators, and contact idealizations

The same local shadow appears in several familiar places.

A point source,
``` math
\begin{equation}
  J(x)=q\delta(x-x_0),
\end{equation}
```
is replaced by the finite coherent source
``` math
\begin{equation}
  J_{\rm adm}(x)
  =
  qK_{\mathrm{adm}}(x,x_0).
\end{equation}
```
A point-source Green equation,
``` math
\begin{equation}
  LG(x,y)=\delta(x-y),
\end{equation}
```
is replaced by
``` math
\begin{equation}
  LG_{\rm adm}(x,y)=K_{\mathrm{adm}}(x,y).
\end{equation}
```
In a flat Euclidean chart with $`A=-\Delta`$, the corresponding filtered scalar propagator has the form
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{e^{-\tau_{\mathrm{adm}}|k|^2}}{|k|^2+m^2}.
  \label{eq:filtered-propagator-particle-section}
\end{equation}
```
A local contact vertex is similarly replaced by a finite coherent overlap. Schematically,
``` math
\begin{equation}
  \int_X \phi(x)^4\,\mathrm{d}x
\end{equation}
```
is replaced by an expression built from products of finite kernels,
``` math
\begin{equation}
  \int_X
  \prod_{j=1}^4 K_{\mathrm{adm}}(x,x_j)
  \,\mathrm{d}x.
\end{equation}
```

These examples show that the pointlike particle shadow, the point-source shadow, and the contact-interaction shadow are manifestations of the same delta-limit structure.

## Interpretive summary

The particle shadow can now be stated precisely.

A finite coherent excitation gives a finite local response:
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,x_0).
\end{equation}
```
When its width is below resolution, the response is operationally pointlike. When the coherent bandwidth is idealized to infinity and the proper-time width to zero, the response becomes the Dirac delta:
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)\to\delta(x-y).
\end{equation}
```
Thus the point particle is not the fundamental object in MTT. It is the local sharp-limit shadow of a finite coherent-sector excitation.

``` math
\begin{equation}
  \boxed{
  \text{particle-like localization}
  =
  \text{delta-limit shadow of finite coherent support}.
  }
\end{equation}
```

# The wave shadow: spectral phase coherence

The preceding section described the local or particle-like shadow of an admissible coherent kernel. This section develops the complementary spectral or wave-like shadow. The same coherent-sector structure that appears locally as a finite source kernel appears spectrally as a retained modal superposition. Wave-like behavior is the preservation and evolution of relative phase among these retained modes or branches.

## Damping operator versus phase generator

Two operators play different roles in the construction.

The operator $`A`$ is the fixed-point stabilization or damping operator. It appears in the proper-time filter
``` math
\begin{equation}
  e^{-\tau_{\mathrm{adm}}A},
\end{equation}
```
and controls coherent support, smoothing, and suppression of discarded modes.

Wave-like behavior, by contrast, requires a phase generator on the retained coherent sector. We therefore introduce a self-adjoint operator
``` math
\begin{equation}
  H_{\rm coh}
\end{equation}
```
on $`\mathcal{H}_{\rm coh}=\mathrm{Ran}P`$, generating unitary coherent evolution
``` math
\begin{equation}
  U_t^{\rm coh}
  =
  e^{-itH_{\rm coh}}.
  \label{eq:coh-unitary}
\end{equation}
```
In applications $`H_{\rm coh}`$ may arise as the effective Hamiltonian, a projected wave operator, or the phase-transport part of a linearized coherent dynamics. The important point is that $`H_{\rm coh}`$ is conceptually distinct from the heat-time damping operator $`A`$.

<div id="ass:coherent-phase-evolution" class="assumption">

**Assumption 18** (Coherent phase evolution). The retained coherent sector $`\mathcal{H}_{\rm coh}`$ carries a self-adjoint phase generator $`H_{\rm coh}`$. The corresponding unitary group $`U_t^{\rm coh}=e^{-itH_{\rm coh}}`$ preserves $`\mathcal{H}_{\rm coh}`$ and transports retained relative phases.

</div>

<div id="rem:no-conflation" class="remark">

*Remark 19* (No conflation of smoothing and phase). The heat kernel $`e^{-\tau_{\mathrm{adm}}A}`$ determines finite coherent support and admissible smoothing. The unitary $`e^{-itH_{\rm coh}}`$ determines phase evolution. The paper does not identify these two operations. Their coexistence is what allows a finite coherent excitation to have both local support and wave-like phase behavior.

</div>

## Coherent modal expansion

Let $`\{\varphi_\alpha\}_{\alpha\in I}`$ be an orthonormal modal basis for the retained coherent sector, chosen so that
``` math
\begin{equation}
  H_{\rm coh}\varphi_\alpha
  =
  E_\alpha\varphi_\alpha
\end{equation}
```
in the simplest diagonal case. A coherent state can be written as
``` math
\begin{equation}
  \psi_{\rm coh}
  =
  \sum_{\alpha\in I}
  c_\alpha\varphi_\alpha,
  \qquad
  \sum_{\alpha\in I}|c_\alpha|^2=1.
  \label{eq:coherent-state-expansion}
\end{equation}
```
Under coherent phase evolution,
``` math
\begin{equation}
  \psi_{\rm coh}(t)
  =
  U_t^{\rm coh}\psi_{\rm coh}
  =
  \sum_{\alpha\in I}
  c_\alpha e^{-iE_\alpha t}\varphi_\alpha.
  \label{eq:coherent-phase-expansion}
\end{equation}
```

The spectral expansion of the admissible kernel,
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)
  =
  \sum_{n\in\mathrm{coh}}
  \chi(\lambda_n)^2e^{-\tau_{\mathrm{adm}}\lambda_n}
  \phi_n(x)\phi_n^\ast(y),
\end{equation}
```
is not itself the time-evolution law. It is the finite coherent support structure. When a phase generator acts on the retained sector, the retained modal components acquire relative phases, and those relative phases produce interference.

<div id="def:spectral-wave-shadow" class="definition">

**Definition 20** (Spectral wave shadow). The spectral wave shadow of a coherent excitation is the representation of $`P\Psi`$ as a retained modal superposition together with its coherent phase evolution under $`U_t^{\rm coh}`$.

</div>

## Interference from off-diagonal coherence

Wave-like behavior is most transparently expressed in density-matrix language. Let $`\rho`$ be a density operator on the retained coherent sector. In a branch or modal basis $`\{|a\rangle\}_{a\in I}`$, write
``` math
\begin{equation}
  \rho_{ab}
  =
  \langle a|\rho|b\rangle.
\end{equation}
```
The diagonal entries $`\rho_{aa}`$ encode branch weights in that basis. The off-diagonal entries $`\rho_{ab}`$ with $`a\neq b`$ encode retained relative phase and coherence.

Let $`E`$ be an effect corresponding to an observable in which the branches can interfere. Then
``` math
\begin{equation}
  \operatorname{tr}(\rho E)
  =
  \sum_a \rho_{aa}E_{aa}
  +
  \sum_{a\neq b}\rho_{ab}E_{ba}.
  \label{eq:prob-diagonal-offdiagonal}
\end{equation}
```
The second term is the interference contribution. It vanishes when the off-diagonal coherences vanish, and it survives when the branch phases remain coherently related.

<div id="prop:interference-criterion" class="proposition">

**Proposition 21** (Interference criterion). *Let $`\rho`$ be a density operator on a finite branch subspace and let $`E`$ be an effect. If $`E_{ba}\neq0`$ for some $`a\neq b`$, then the probability $`\operatorname{tr}(\rho E)`$ depends on the off-diagonal coherence $`\rho_{ab}`$. In particular, interference is present precisely when off-diagonal branch coherence contributes to observable probabilities.*

</div>

<div class="proof">

*Proof.* The identity <a href="#eq:prob-diagonal-offdiagonal" data-reference-type="eqref" data-reference="eq:prob-diagonal-offdiagonal">[eq:prob-diagonal-offdiagonal]</a> follows from expanding the trace in the branch basis:
``` math
\begin{equation}
  \operatorname{tr}(\rho E)
  =
  \sum_{a,b}\rho_{ab}E_{ba}.
\end{equation}
```
Terms with $`a=b`$ are diagonal contributions, while terms with $`a\neq b`$ are off-diagonal contributions. If $`E_{ba}\neq0`$, changing $`\rho_{ab}`$ while holding diagonal entries fixed changes the probability. This is exactly phase-sensitive interference in the chosen context. ◻

</div>

<div id="rem:wave-like-phase-sensitive" class="remark">

*Remark 22* (Wave-like means phase-sensitive, not spatially diffuse). Wave-like behavior does not mean that the excitation is a classical fluid spread through space. It means that the effective description retains phase-sensitive off-diagonal structure whose observable probabilities contain cross terms. Spatial diffraction and interference are common realizations, but the same logic applies to spin, flavor, path, polarization, and other coherent branch spaces.

</div>

## Two-branch superposition

The simplest case is a two-branch coherent state
``` math
\begin{equation}
  |\psi\rangle
  =
  \alpha|1\rangle+\beta|2\rangle,
  \qquad
  |\alpha|^2+|\beta|^2=1.
  \label{eq:two-branch-state}
\end{equation}
```
Its density matrix is
``` math
\begin{equation}
  \rho
  =
  |\alpha|^2|1\rangle\langle1|
  +
  |\beta|^2|2\rangle\langle2|
  +
  \alpha\beta^\ast|1\rangle\langle2|
  +
  \alpha^\ast\beta|2\rangle\langle1|.
  \label{eq:two-branch-density}
\end{equation}
```
The interference-bearing terms are the off-diagonal terms
``` math
\begin{equation}
  \rho_{12}=\alpha\beta^\ast,
  \qquad
  \rho_{21}=\alpha^\ast\beta.
\end{equation}
```

If the two branches acquire a relative phase $`\theta`$, then
``` math
\begin{equation}
  |\psi(\theta)\rangle
  =
  \alpha|1\rangle+\beta e^{i\theta}|2\rangle.
\end{equation}
```
For an effect $`E`$ with $`E_{21}\neq0`$, the probability contains terms of the form
``` math
\begin{equation}
  2\operatorname{Re}
  \left[
    \alpha\beta^\ast e^{-i\theta}E_{21}
  \right].
  \label{eq:two-branch-interference-term}
\end{equation}
```
This is the abstract form of interference fringes.

<div id="cor:loss-coherence-removes-interference" class="corollary">

**Corollary 23** (Loss of off-diagonal coherence removes interference). *If the off-diagonal entries $`\rho_{12}`$ and $`\rho_{21}`$ are set to zero while the diagonal entries are held fixed, then all phase-dependent two-branch interference terms vanish.*

</div>

<div class="proof">

*Proof.* Set $`\rho_{12}=\rho_{21}=0`$ in <a href="#eq:prob-diagonal-offdiagonal" data-reference-type="eqref" data-reference="eq:prob-diagonal-offdiagonal">[eq:prob-diagonal-offdiagonal]</a>. Only diagonal terms remain, and these do not depend on the relative phase. ◻

</div>

## Relation to the admissible kernel

The wave shadow is not independent of the admissible kernel. The finite kernel selects the retained coherent sector and weights its spectral content:
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)
  =
  \sum_{n\in\mathrm{coh}}
  w_n\phi_n(x)\phi_n^\ast(y),
  \qquad
  w_n=\chi(\lambda_n)^2e^{-\tau_{\mathrm{adm}}\lambda_n}.
  \label{eq:kernel-weights-wave}
\end{equation}
```
A coherent state supported in this sector has the modal form
``` math
\begin{equation}
  \psi_{\rm coh}(x,t)
  =
  \sum_{n\in\mathrm{coh}}
  c_n(t)\phi_n(x).
\end{equation}
```
When the phase generator is diagonal in the same basis,
``` math
\begin{equation}
  c_n(t)=c_n(0)e^{-iE_nt}.
\end{equation}
```
When $`H_{\rm coh}`$ is not diagonal in the $`A`$-basis, coherent phase evolution is still unitary on $`\mathrm{Ran}P`$, and interference is described by the density-matrix criterion above.

Thus $`A`$ and $`H_{\rm coh}`$ need not be identical. The role of $`A`$ is to select and weight admissible coherent support. The role of $`H_{\rm coh}`$ is to transport phase within that support. Wave-like behavior requires both:

1.  a retained coherent sector in which off-diagonal relations can exist;

2.  phase evolution preserving those relations until a measurement context damps or selects them.

## Wave packets and unresolved localization

The spectral wave shadow also includes the familiar wave-packet picture. A wave packet is a coherent superposition of modes whose phases are arranged to give localized support over some finite region. In MTT terms, this is not a contradiction between wave and particle pictures. A wave packet is already a mixed local/spectral representation of the same coherent sector.

Let
``` math
\begin{equation}
  \psi(x)
  =
  \sum_{n\in\mathrm{coh}}
  c_n\phi_n(x)
\end{equation}
```
be concentrated near $`x_0`$. It may be spatially localized, yet still wave-like in the sense that its evolution and detection probabilities depend on phase relations among the $`c_n`$. If its support is much smaller than detector resolution, it is operationally particle-like; if phase relations are probed by an interferometer, it is operationally wave-like.

<div id="rem:no-contradiction-local-interference" class="remark">

*Remark 24* (No contradiction between localization and interference). A localized wave packet can still interfere. Conversely, an extended coherent state can still produce localized detection events. The apparent contradiction arises only if “localized” and “wave-like” are treated as mutually exclusive ontologies rather than as different projection contexts.

</div>

## Interpretive summary

The wave shadow can now be stated precisely.

A finite coherent excitation has a retained spectral representation:
``` math
\begin{equation}
  \psi_{\rm coh}
  =
  \sum_{\alpha}c_\alpha\varphi_\alpha.
\end{equation}
```
A coherent phase generator transports the retained modes:
``` math
\begin{equation}
  \psi_{\rm coh}(t)=e^{-itH_{\rm coh}}\psi_{\rm coh}(0).
\end{equation}
```
Observable probabilities contain interference exactly when off-diagonal branch or modal coherences contribute:
``` math
\begin{equation}
  \operatorname{tr}(\rho E)
  =
  \sum_a \rho_{aa}E_{aa}
  +
  \sum_{a\neq b}\rho_{ab}E_{ba}.
\end{equation}
```

Thus the wave is not a separate substance added to a particle. It is the phase-sensitive spectral shadow of the same coherent-sector excitation whose local shadow can appear pointlike.

``` math
\begin{equation}
  \boxed{
  \text{wave-like interference}
  =
  \text{phase-coherent spectral shadow of finite coherent support}.
  }
\end{equation}
```

# Measurement, survivor basins, and admissible branch damping

The previous two sections described the two shadows of a coherent excitation: local delta-like localization and spectral phase coherence. Measurement connects them. A measurement context is a device-dependent disturbance followed by projection and stabilization. It does not convert a wave into a particle. It selects a downstream survivor basin and, depending on the device, may damp the off-diagonal coherences that made interference visible.

This section gives the operator form of that statement.

## Measurement contexts

A measurement is specified not only by an abstract observable but by a physical context. In MTT, a measurement context $`\mathsf M`$ includes:
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\}_{i\in I},\mathfrak B_{\mathsf M}).
  \label{eq:measurement-context-data}
\end{equation}
```
Here:

1.  $`A_{\mathsf M}`$ is the detector-sector stabilization or disturbance-damping operator;

2.  $`P_{\mathsf M}`$ is the detector coherent-sector projector;

3.  $`\chi_{\mathsf M}(A_{\mathsf M})`$ is the detector spectral acceptance window;

4.  $`\tau_{\mathsf M}`$ is the detector-sector proper-time/heat-time scale;

5.  $`\{E_i^{(\mathsf M)}\}_{i\in I}`$ is the finite effect family associated with the possible records;

6.  $`\mathfrak B_{\mathsf M}=\{B_i^{(\mathsf M)}\}_{i\in I}`$ is the corresponding survivor-basin partition.

Different measurement devices can have different data. Thus different devices can disturb the same incoming coherent excitation in different ways. This is not an imperfection added after the fact. It is part of what defines the measurement context.

<div id="def:closed-finite-measurement" class="definition">

**Definition 25** (Closed finite measurement). A finite measurement context $`\mathsf M`$ is closed on the retained coherent sector if its effects satisfy
``` math
\begin{equation}
  E_i^{(\mathsf M)}\ge0,
  \qquad
  \sum_{i\in I}E_i^{(\mathsf M)}=I_{\rm coh}
  \label{eq:closed-discrete-povm}
\end{equation}
```
in the discrete-outcome case, or
``` math
\begin{equation}
  E_x^{(\mathsf M)}\ge0,
  \qquad
  \int E_x^{(\mathsf M)}\,\mathrm{d}x=I_{\rm coh}
  \label{eq:closed-continuous-povm}
\end{equation}
```
in the continuous-outcome case.

</div>

For a normalized retained-sector state $`\rho`$, the probability of a discrete outcome $`i`$ is
``` math
\begin{equation}
  p_i^{(\mathsf M)}
  =
  \mathop{\mathrm{tr}}(\rho E_i^{(\mathsf M)}),
  \label{eq:discrete-outcome-prob}
\end{equation}
```
and closedness gives
``` math
\begin{equation}
  \sum_i p_i^{(\mathsf M)}
  =
  \mathop{\mathrm{tr}}(\rho I_{\rm coh})
  =
  1.
\end{equation}
```

<div id="rem:open-measurement-contexts" class="remark">

*Remark 26* (Open measurement contexts). If the detector has unobserved leakage channels, the effect family may satisfy
``` math
\begin{equation}
  \sum_i E_i^{(\mathsf M)}\le I_{\rm coh}.
\end{equation}
```
The missing probability corresponds to outcomes outside the recorded detector context. The closed case is the appropriate idealization when discussing ordinary normalized measurement statistics.

</div>

## Exact records as stabilized survivor basins

A detector record is exact relative to its measurement context because the device stabilizes one branch of the basin partition. This does not mean the device reveals a context-free pre-existing classical value. It means that, after disturbance and re-coherence, the downstream state lies in one basin $`B_i^{(\mathsf M)}`$.

Schematically,
``` math
\begin{equation}
  \Psi
  \xrightarrow{\text{device disturbance}}
  \Psi'
  \xrightarrow{\text{projection}}
  P_{\mathsf M}\Psi'
  \xrightarrow{\text{stabilization}}
  B_i^{(\mathsf M)}.
  \label{eq:measurement-stabilization-chain}
\end{equation}
```

The stabilized record is discrete even when the pre-measurement coherent excitation was represented by a continuous wave amplitude. In this sense, particle-like detector clicks are not primitive point events. They are stable finite records produced by a detector-context projection.

<div id="def:survivor-basin-record" class="definition">

**Definition 27** (Survivor-basin record). A survivor-basin record for a measurement context $`\mathsf M`$ is an outcome $`i\in I`$ such that the post-disturbance projected state enters and remains in the basin $`B_i^{(\mathsf M)}`$ under the local stabilization dynamics.

</div>

## Outcome probabilities versus coherence visibility

The measurement process has two logically distinct parts.

First, it has an outcome-selection part. In the basin-measure account, outcome probabilities are determined by the relative measures of stabilized basins:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i^{(\mathsf M)})}
  {\sum_j\mu(B_j^{(\mathsf M)})},
  \label{eq:basin-probabilities-measurement}
\end{equation}
```
where $`\mu`$ is the admissibility-weighted measure on the relevant ensemble.

Second, it has a coherence-visibility part. Before or during final selection, branch coherences may survive, partially survive, or be suppressed. These off-diagonal terms determine whether interference is visible.

Thus one must not identify Born probabilities with visibility damping. The former concern which basin is selected. The latter concerns how much off-diagonal coherence remains between branches.

``` math
\begin{equation}
  \boxed{
  \text{basin measure controls outcome frequency},
  }
  \qquad
  \boxed{
  \text{branch damping controls interference visibility}.
  }
\end{equation}
```

This distinction is especially important in the double-slit experiment. Each detection event is localized, but the ensemble distribution can still display interference if branch coherence survives until detection.

## Branch density matrices

Let $`\{|a\rangle\}_{a=1}^N`$ be a finite branch basis selected by a measurement context. A retained-sector density matrix has entries
``` math
\begin{equation}
  \rho_{ab}
  =
  \langle a|\rho|b\rangle.
\end{equation}
```
The diagonal terms $`\rho_{aa}`$ give branch weights in this basis. The off-diagonal terms $`\rho_{ab}`$, $`a\neq b`$, carry branch coherence.

A measurement device that distinguishes branches acts by suppressing the off-diagonal entries. The simplest branch-damping form is
``` math
\begin{equation}
  \rho_{ab}
  \longmapsto
  D_{ab}^{(\mathsf M)}\rho_{ab}.
  \label{eq:branch-damping-map-entry}
\end{equation}
```
In matrix notation,
``` math
\begin{equation}
  \rho
  \longmapsto
  \mathcal E_D(\rho)
  =
  D\circ \rho,
  \label{eq:schur-map}
\end{equation}
```
where $`\circ`$ denotes entrywise, or Schur, multiplication.

Not every matrix $`D`$ gives a physically admissible damping map. The next theorem states the consistency condition.

<div id="thm:schur-channel" class="theorem">

**Theorem 28** (Schur-channel consistency). *Let $`D=(D_{ab})_{a,b=1}^N`$ be a positive semidefinite matrix satisfying
``` math
\begin{equation}
  D_{aa}=1
  \qquad
  \text{for all }a.
  \label{eq:D-diagonal-one}
\end{equation}
```
Then
``` math
\begin{equation}
  \mathcal E_D(\rho)=D\circ\rho
\end{equation}
```
is completely positive and trace preserving on $`N\times N`$ density matrices.*

</div>

<div class="proof">

*Proof.* Since $`D\succeq0`$, there exist vectors $`v_a`$ in an auxiliary Hilbert space such that
``` math
\begin{equation}
  D_{ab}=\langle v_b,v_a\rangle.
\end{equation}
```
Define a Stinespring isometry
``` math
\begin{equation}
  V|a\rangle=|a\rangle\otimes v_a.
\end{equation}
```
The condition $`D_{aa}=1`$ implies $`\|v_a\|=1`$, hence $`V^\ast V=I`$. Then
``` math
\begin{align}
  \bigl(\operatorname{tr}_{\rm aux}(V\rho V^\ast)\bigr)_{ab}
  &=
  \rho_{ab}\langle v_b,v_a\rangle
  \\
  &=
  D_{ab}\rho_{ab}.
\end{align}
```
Thus
``` math
\begin{equation}
  \operatorname{tr}_{\rm aux}(V\rho V^\ast)=D\circ\rho.
\end{equation}
```
The map is therefore completely positive. Since $`D_{aa}=1`$, diagonal entries are unchanged, so
``` math
\begin{equation}
  \mathop{\mathrm{tr}}(D\circ\rho)=\mathop{\mathrm{tr}}(\rho).
\end{equation}
```
Hence the map is trace preserving. ◻

</div>

<div id="rem:admissible-damping-rules" class="remark">

*Remark 29* (Admissibility condition for damping rules). A proposed branch-damping rule is admissible only if it defines such a positive Schur multiplier. This prevents arbitrary insertion of visibility factors. The damping matrix must correspond to a valid reduced dynamics or detector-context projection.

</div>

## Branch-distance damping and Schoenberg positivity

MTT often writes branch damping in the form
``` math
\begin{equation}
  D_{ab}^{(\mathsf M)}
  =
  \exp[-\tau_{\mathsf M}\Lambda_{ab}^{(\mathsf M)}],
  \label{eq:branch-distance-damping}
\end{equation}
```
where $`\Lambda_{ab}^{(\mathsf M)}\ge0`$ measures detector-induced branch separation, basin-splitting, or distinguishability.

For this to define a valid Schur channel, the matrix $`D`$ must be positive semidefinite. A sufficient and widely useful condition is conditional negative definiteness of $`\Lambda=(\Lambda_{ab})`$.

<div id="def:cnd" class="definition">

**Definition 30** (Conditionally negative definite branch separation). A real symmetric matrix $`\Lambda=(\Lambda_{ab})`$ with $`\Lambda_{aa}=0`$ is conditionally negative definite if
``` math
\begin{equation}
  \sum_{a,b}\overline{c_a}c_b\Lambda_{ab}\le0
  \label{eq:cnd-condition}
\end{equation}
```
for all complex coefficients $`c_a`$ satisfying
``` math
\begin{equation}
  \sum_a c_a=0.
\end{equation}
```

</div>

<div id="prop:schoenberg" class="proposition">

**Proposition 31** (Schoenberg-type admissibility criterion). *If $`\Lambda`$ is conditionally negative definite, then for every $`\tau\ge0`$,
``` math
\begin{equation}
  D_{ab}=e^{-\tau\Lambda_{ab}}
\end{equation}
```
is positive semidefinite and satisfies $`D_{aa}=1`$. Hence $`D\circ\rho`$ is a completely positive trace-preserving branch-damping channel.*

</div>

<div class="proof">

*Proof.* This is the finite-dimensional Schoenberg theorem: a real symmetric matrix with zero diagonal is conditionally negative definite if and only if $`e^{-\tau\Lambda}`$ is positive semidefinite for every $`\tau\ge0`$. Since $`\Lambda_{aa}=0`$, one has $`D_{aa}=1`$. The claim then follows from <a href="#thm:schur-channel" data-reference-type="ref+label" data-reference="thm:schur-channel">28</a>. ◻

</div>

A particularly transparent case is squared Hilbert-space distance. If there exist vectors $`r_a`$ in a real Hilbert space such that
``` math
\begin{equation}
  \Lambda_{ab}
  =
  \frac12\left\lVert r_a-r_b \right\rVert^2,
  \label{eq:squared-distance-Lambda}
\end{equation}
```
then $`\Lambda`$ is conditionally negative definite, and
``` math
\begin{equation}
  D_{ab}
  =
  \exp\left[
  -\frac{\tau}{2}\left\lVert r_a-r_b \right\rVert^2
  \right]
  \label{eq:gaussian-branch-damping}
\end{equation}
```
is a valid damping kernel.

<div id="rem:device-dependence-lambda" class="remark">

*Remark 32* (Device dependence of $`\Lambda_{ab}^{(\mathsf M)}`$). The same incoming coherent excitation may yield different branch-separation matrices for different devices. A weak path marker, a strong absorbing detector, a Stern–Gerlach magnet, and a recombining interferometer do not define the same branch metric. This is why the measurement method affects whether the wave-like or particle-like shadow is observed.

</div>

## Visibility as off-diagonal survival

For a two-branch experiment, write
``` math
\begin{equation}
  \rho
  =
  \begin{pmatrix}
  \rho_{11} & \rho_{12}\\
  \rho_{21} & \rho_{22}
  \end{pmatrix}.
\end{equation}
```
A valid two-branch damping channel has
``` math
\begin{equation}
  D=
  \begin{pmatrix}
  1 & d\\
  d^\ast & 1
  \end{pmatrix},
  \qquad
  |d|\le1.
\end{equation}
```
Then
``` math
\begin{equation}
  \mathcal E_D(\rho)
  =
  \begin{pmatrix}
  \rho_{11} & d\rho_{12}\\
  d^\ast\rho_{21} & \rho_{22}
  \end{pmatrix}.
\end{equation}
```

If $`d=1`$, branch coherence is fully retained. If $`d=0`$, the branch state is reduced to the corresponding incoherent mixture. Intermediate values $`0<|d|<1`$ produce partial visibility.

For real nonnegative damping $`d=D_{12}\in[0,1]`$, the interference term is simply multiplied by $`D_{12}`$. This is the operator-theoretic basis of the visibility formula used in the double-slit section.

## Measurement as projection-duality switch

The same coherent excitation can therefore be seen under two limiting measurement regimes.

In a coherence-preserving arrangement,
``` math
\begin{equation}
  D_{ab}^{(\mathsf M)}\approx1
  \qquad
  (a\neq b),
\end{equation}
```
so off-diagonal terms survive. The wave shadow is visible.

In a strongly distinguishing arrangement,
``` math
\begin{equation}
  D_{ab}^{(\mathsf M)}\approx0
  \qquad
  (a\neq b),
\end{equation}
```
so off-diagonal terms are suppressed. The downstream record is particle-like.

This does not mean the object changed from wave to particle. It means the device changed which projection shadow survived in the effective description.

``` math
\begin{equation}
  \boxed{
  \text{measurement context controls the survival of branch coherence}.
  }
\end{equation}
```

# The double-slit experiment

The double-slit experiment is the canonical case in which wave-like and particle-like shadows appear in the same physical setup. A coherent excitation propagates through two available branches and produces an interference pattern when no branch-distinguishing record is stabilized. Yet each detection event on the screen is localized. In MTT this is not a paradox. The interference pattern is the spectral phase shadow of retained branch coherence, while the localized screen event is the survivor-basin record produced by the detector context.

This section derives the double-slit formula from the branch-damping and finite-effect framework of <a href="#sec:measurement-branch-damping" data-reference-type="ref+label" data-reference="sec:measurement-branch-damping">5</a>.

## Branch decomposition

Let $`|1\rangle`$ and $`|2\rangle`$ denote the two path branches associated with the two slits. A coherent outgoing state after the slits has the form
``` math
\begin{equation}
  |\psi\rangle
  =
  \alpha|\psi_1\rangle+\beta|\psi_2\rangle,
  \label{eq:double-slit-state}
\end{equation}
```
where $`|\psi_1\rangle`$ and $`|\psi_2\rangle`$ include the propagation amplitudes from the respective slits to the detection screen. The coefficients $`\alpha,\beta`$ include the relative weights and phases set by the source and slit geometry. We assume normalization
``` math
\begin{equation}
  \langle\psi|\psi\rangle=1.
\end{equation}
```

The corresponding density matrix is
``` math
\begin{align}
  \rho
  &=
  |\alpha|^2|\psi_1\rangle\langle\psi_1|
  +
  |\beta|^2|\psi_2\rangle\langle\psi_2|
  \nonumber\\
  &\quad+
  \alpha\beta^\ast|\psi_1\rangle\langle\psi_2|
  +
  \alpha^\ast\beta|\psi_2\rangle\langle\psi_1|.
  \label{eq:double-slit-density}
\end{align}
```
The first two terms are branch-diagonal. The last two terms are branch off-diagonal and carry the relative phase required for interference.

Let $`E_x`$ be the finite screen effect associated with a detection record at screen coordinate $`x`$. In a sharp idealization one writes $`E_x=|x\rangle\langle x|`$. In MTT $`E_x`$ is a finite detector effect, typically of the form
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
  \qquad
  k_x(y)=K_{\rm det}(y,x),
  \label{eq:screen-effect}
\end{equation}
```
or a more general positive effect satisfying the POVM normalization condition.

The screen detection density is
``` math
\begin{equation}
  I(x)
  =
  \mathop{\mathrm{tr}}(\rho E_x).
  \label{eq:screen-density}
\end{equation}
```

## No which-way device: full branch coherence

When no which-way record is stabilized, the two path branches remain in the same coherent sector until detection. In the branch-damping notation this corresponds to
``` math
\begin{equation}
  D_{12}\approx1.
\end{equation}
```
Substituting <a href="#eq:double-slit-density" data-reference-type="eqref" data-reference="eq:double-slit-density">[eq:double-slit-density]</a> into <a href="#eq:screen-density" data-reference-type="eqref" data-reference="eq:screen-density">[eq:screen-density]</a> gives
``` math
\begin{align}
  I(x)
  &=
  |\alpha|^2\langle\psi_1|E_x|\psi_1\rangle
  +
  |\beta|^2\langle\psi_2|E_x|\psi_2\rangle
  \nonumber\\
  &\quad+
  2\operatorname{Re}
  \left[
    \alpha\beta^\ast
    \langle\psi_2|E_x|\psi_1\rangle
  \right].
  \label{eq:double-slit-full-interference}
\end{align}
```
The last term is the interference term.

In the ideal sharp-position notation, this reduces to the familiar expression
``` math
\begin{equation}
  I(x)
  =
  |\alpha\psi_1(x)+\beta\psi_2(x)|^2.
  \label{eq:double-slit-sharp}
\end{equation}
```
The MTT expression <a href="#eq:double-slit-full-interference" data-reference-type="eqref" data-reference="eq:double-slit-full-interference">[eq:double-slit-full-interference]</a> is the finite-effect version of the same formula.

<div id="rem:localized-events-interference-distribution" class="remark">

*Remark 33* (Localized events with an interference distribution). There is no contradiction between localized screen records and an interference distribution. Each individual detection is a stabilized record of the screen detector context. The ensemble distribution displays interference because the off-diagonal branch coherences survive until the detection effects are applied.

</div>

## Which-way device: device-dependent branch damping

Now introduce a which-way device $`\mathsf M_{\rm ww}`$. The device couples differently to the two path branches. In standard notation one often writes
``` math
\begin{equation}
  |\psi_1\rangle|D_0\rangle
  +
  |\psi_2\rangle|D_0\rangle
  \longmapsto
  |\psi_1\rangle|D_1\rangle
  +
  |\psi_2\rangle|D_2\rangle.
  \label{eq:which-way-standard}
\end{equation}
```
The overlap $`\langle D_2|D_1\rangle`$ then controls the residual interference.

In MTT this overlap is interpreted as the downstream signature of a device-dependent branch-separation process. The device defines a branch-distance scale
``` math
\begin{equation}
  \Lambda_{12}^{(\rm ww)}
\end{equation}
```
and a detector proper-time/heat-time scale $`\tau_{\rm ww}`$. The associated damping factor is
``` math
\begin{equation}
  D_{12}^{(\rm ww)}
  =
  \exp[-\tau_{\rm ww}\Lambda_{12}^{(\rm ww)}],
  \label{eq:which-way-damping}
\end{equation}
```
provided the resulting $`D`$-matrix defines a valid Schur channel.

The post-device branch density matrix is
``` math
\begin{align}
  \rho'
  &=
  |\alpha|^2|\psi_1\rangle\langle\psi_1|
  +
  |\beta|^2|\psi_2\rangle\langle\psi_2|
  \nonumber\\
  &\quad+
  D_{12}^{(\rm ww)}
  \alpha\beta^\ast|\psi_1\rangle\langle\psi_2|
  +
  D_{21}^{(\rm ww)}
  \alpha^\ast\beta|\psi_2\rangle\langle\psi_1|.
  \label{eq:post-which-way-density}
\end{align}
```
For real symmetric damping,
``` math
\begin{equation}
  D_{12}^{(\rm ww)}=D_{21}^{(\rm ww)}\in[0,1].
\end{equation}
```

The resulting screen density is
``` math
\begin{align}
  I_{\rm MTT}(x)
  &=
  |\alpha|^2\langle\psi_1|E_x|\psi_1\rangle
  +
  |\beta|^2\langle\psi_2|E_x|\psi_2\rangle
  \nonumber\\
  &\quad+
  2D_{12}^{(\rm ww)}
  \operatorname{Re}
  \left[
    \alpha\beta^\ast
    \langle\psi_2|E_x|\psi_1\rangle
  \right].
  \label{eq:double-slit-mtt-damped}
\end{align}
```

Thus the device controls the survival of the wave-like shadow:
``` math
\begin{equation}
  D_{12}^{(\rm ww)}\approx1
  \quad\Rightarrow\quad
  \text{interference visible},
\end{equation}
```
whereas
``` math
\begin{equation}
  D_{12}^{(\rm ww)}\approx0
  \quad\Rightarrow\quad
  \text{interference suppressed}.
\end{equation}
```

## Weak, intermediate, and strong which-way regimes

The MTT reading naturally yields three regimes.

#### Weak which-way disturbance.

If the device couples weakly to the path distinction, then
``` math
\begin{equation}
  \tau_{\rm ww}\Lambda_{12}^{(\rm ww)}\ll1,
\end{equation}
```
so
``` math
\begin{equation}
  D_{12}^{(\rm ww)}
  =
  1-\tau_{\rm ww}\Lambda_{12}^{(\rm ww)}
  +O((\tau_{\rm ww}\Lambda_{12}^{(\rm ww)})^2).
\end{equation}
```
The interference pattern survives with only small visibility loss.

#### Intermediate disturbance.

If
``` math
\begin{equation}
  \tau_{\rm ww}\Lambda_{12}^{(\rm ww)}\sim1,
\end{equation}
```
then the interference term is partially suppressed. The ensemble distribution interpolates between the full interference pattern and the incoherent sum.

#### Strong which-way disturbance.

If
``` math
\begin{equation}
  \tau_{\rm ww}\Lambda_{12}^{(\rm ww)}\gg1,
\end{equation}
```
then
``` math
\begin{equation}
  D_{12}^{(\rm ww)}\approx0,
\end{equation}
```
and
``` math
\begin{equation}
  I_{\rm MTT}(x)
  \approx
  |\alpha|^2\langle\psi_1|E_x|\psi_1\rangle
  +
  |\beta|^2\langle\psi_2|E_x|\psi_2\rangle.
  \label{eq:double-slit-incoherent-sum}
\end{equation}
```
The wave-like interference shadow is no longer visible. The downstream description is particle-like in the sense that a definite path-correlated record has been stabilized.

<div id="rem:exact-outcome-device-context" class="remark">

*Remark 34* (Exact outcome within a device context). A strong which-way device gives an exact outcome relative to the branch partition it defines. This does not mean that the particle carried a context-independent classical path value through the apparatus. It means that the device disturbance split the coherent sector into path-distinguishable survivor basins and stabilized one of them.

</div>

## Visibility law

In a symmetric two-slit setup, the intensity can be written in the form
``` math
\begin{equation}
  I_0(x)
  =
  \bar I(x)\left[1+V_0\cos\varphi(x)\right],
  \label{eq:ideal-visibility-form}
\end{equation}
```
where $`V_0`$ is the ideal visibility and $`\varphi(x)`$ is the relative phase. Under MTT branch damping, the interference term is multiplied by $`D_{12}`$, giving
``` math
\begin{equation}
  I_{\rm MTT}(x)
  =
  \bar I(x)\left[1+D_{12}V_0\cos\varphi(x)\right].
  \label{eq:mtt-visibility-form}
\end{equation}
```
Therefore
``` math
\begin{equation}
  V_{\rm MTT}
  =
  D_{12}V_0.
  \label{eq:visibility-law}
\end{equation}
```

<div id="prop:visibility-reduction" class="proposition">

**Proposition 35** (Visibility reduction). *In a symmetric two-branch interference experiment with real branch damping $`D_{12}\in[0,1]`$, the measured visibility is
``` math
\begin{equation}
  V_{\rm MTT}=D_{12}V_0.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The maximum and minimum of <a href="#eq:mtt-visibility-form" data-reference-type="eqref" data-reference="eq:mtt-visibility-form">[eq:mtt-visibility-form]</a> are
``` math
\begin{equation}
  I_{\max}=\bar I(1+D_{12}V_0),
  \qquad
  I_{\min}=\bar I(1-D_{12}V_0).
\end{equation}
```
Thus
``` math
\begin{equation}
  \frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}}
  =
  D_{12}V_0.
\end{equation}
```
 ◻

</div>

This formula is the quantitative form of the projection-duality crossover. As the device becomes more path-distinguishing, $`D_{12}`$ decreases and the wave-like shadow disappears from the ensemble distribution.

## Screen localization and finite detector kernels

The same experiment also displays particle-like localization at the screen. A screen detection at location $`x`$ is represented by a finite effect
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
  \qquad
  k_x(y)=K_{\rm det}(y,x).
\end{equation}
```
If $`K_{\rm det}(y,x)`$ is narrow relative to the detector resolution, the record is effectively pointlike.

In the sharp idealization,
``` math
\begin{equation}
  K_{\rm det}(y,x)\to\delta(y-x),
\end{equation}
```
and
``` math
\begin{equation}
  E_x\to |x\rangle\langle x|.
\end{equation}
```
But the finite kernel is the native MTT object. The delta/PVM form is the singular measurement limit.

Thus the double-slit experiment contains both shadows at once:

1.  the ensemble pattern depends on off-diagonal branch coherence and is wave-like;

2.  each detector record is a finite survivor-basin event and is particle-like.

## Delayed choice and quantum eraser reading

The same formalism also explains delayed-choice and quantum eraser variants. What matters is not whether a particle retroactively chose a path. What matters is which final measurement context is imposed on the branch-marker system.

If the marker basis preserves path distinguishability, then the branch separation remains large and
``` math
\begin{equation}
  D_{12}\approx0.
\end{equation}
```
No unconditional interference appears.

If the marker is measured in a recombining basis that groups the two path alternatives into coherent subensembles, then conditional interference fringes can reappear within those post-selected subensembles. In MTT language, the final measurement context changes the survivor-basin partition. It does not rewrite the past; it changes which downstream shadow is stabilized and which conditional ensemble is being described.

<div id="rem:no-retrocausality" class="remark">

*Remark 36* (No retrocausality required). Delayed-choice and eraser experiments do not require retroactive changes of history in this framework. They require only that the final measurement context determine whether the available branch information is stabilized as distinguishable records or recombined into a coherent conditional basis.

</div>

## Summary of the double-slit result

The double-slit experiment is not evidence that a quantum object switches between being a wave and being a particle. It is evidence that two different projection shadows are available.

With branch coherence preserved,
``` math
\begin{equation}
  D_{12}\approx1,
\end{equation}
```
and the wave-like interference term survives. With path-distinguishing disturbance,
``` math
\begin{equation}
  D_{12}\approx0,
\end{equation}
```
and the ensemble becomes an incoherent sum. With finite screen effects, every individual record is localized.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{interference pattern}
  =
  \text{spectral branch-coherence shadow},
  }
\end{equation}
```
while
``` math
\begin{equation}
  \boxed{
  \text{localized screen click}
  =
  \text{finite survivor-basin record}.
  }
\end{equation}
```

Both arise from the same coherent excitation under different projection aspects.

# Further experimental modules

The double-slit experiment is the cleanest illustration of projection duality, but it is not a special case in the sense of requiring a unique mechanism. The same architecture appears in spin measurements, interferometers, delayed-choice arrangements, matter-wave diffraction, and multi-particle indistinguishability experiments. In each case, MTT separates three questions:

1.  which coherent branches or modes are retained;

2.  how the measurement device disturbs and separates those branches;

3.  which survivor-basin record is stabilized.

This section records several standard modules. They are not new phenomenological fits; they are consistency checks showing that the same projection-duality structure covers familiar wave-particle experiments.

## Stern–Gerlach splitting

A Stern–Gerlach apparatus measures spin by coupling spin branches to spatially separated trajectories. The measurement context is determined by the magnet orientation $`\hat n`$. For spin $`1/2`$, the branch basis is
``` math
\begin{equation}
  \{|\uparrow_{\hat n}\rangle,|\downarrow_{\hat n}\rangle\}.
\end{equation}
```
An incoming spin state can be written
``` math
\begin{equation}
  |\psi\rangle
  =
  \alpha|\uparrow_{\hat n}\rangle
  +
  \beta|\downarrow_{\hat n}\rangle.
  \label{eq:sg-incoming}
\end{equation}
```
The Stern–Gerlach field correlates these spin branches with different spatial wave packets:
``` math
\begin{equation}
  |\psi\rangle|\Phi_0\rangle
  \longmapsto
  \alpha|\uparrow_{\hat n}\rangle|\Phi_+\rangle
  +
  \beta|\downarrow_{\hat n}\rangle|\Phi_-\rangle.
  \label{eq:sg-branch-correlation}
\end{equation}
```

In MTT, the magnet plus downstream detector define a measurement context
``` math
\begin{equation}
  \mathsf M_{\rm SG}(\hat n).
\end{equation}
```
The corresponding branch damping acts on the spin off-diagonal term:
``` math
\begin{equation}
  \rho_{\uparrow\downarrow}
  \longmapsto
  D_{\uparrow\downarrow}^{(\hat n)}\rho_{\uparrow\downarrow}.
  \label{eq:sg-damping}
\end{equation}
```
For a strong Stern–Gerlach measurement,
``` math
\begin{equation}
  D_{\uparrow\downarrow}^{(\hat n)}\approx0,
\end{equation}
```
and the apparatus stabilizes one of two spatially separated survivor basins:
``` math
\begin{equation}
  B_+^{(\hat n)}
  \quad\text{or}\quad
  B_-^{(\hat n)}.
\end{equation}
```

<div id="prop:sg-context-basins" class="proposition">

**Proposition 37** (Stern–Gerlach records as context-selected basins). *In a Stern–Gerlach measurement, the exact up/down record is exact relative to the device orientation $`\hat n`$. Changing $`\hat n`$ changes the branch basis and hence changes the survivor-basin partition selected by the device.*

</div>

<div class="proof">

*Proof.* The branch decomposition <a href="#eq:sg-incoming" data-reference-type="eqref" data-reference="eq:sg-incoming">[eq:sg-incoming]</a> is defined by the eigenbasis of $`\sigma\cdot\hat n`$. A different orientation $`\hat n'`$ defines a different eigenbasis and a different splitting of the incoming coherent spin state. The measurement device correlates the selected basis with spatially separated packets and detector basins. Thus the stabilized record is definite inside the context $`\mathsf M_{\rm SG}(\hat n)`$, not independent of the chosen orientation. ◻

</div>

This illustrates why measurement outcomes are exact without being context-free. The device does not merely read a pre-existing classical spin vector. It imposes a branch basis and stabilizes one branch.

## Mach–Zehnder interferometer

A Mach–Zehnder interferometer is a controlled two-branch experiment. After the first beam splitter, the state is
``` math
\begin{equation}
  |\psi\rangle
  =
  \frac{1}{\sqrt2}
  \left(
  |1\rangle+e^{i\varphi}|2\rangle
  \right),
  \label{eq:mz-state}
\end{equation}
```
where $`\varphi`$ is the relative phase between the two arms.

If the arms are recombined without which-path marking, the output probabilities are phase-sensitive:
``` math
\begin{equation}
  p_\pm
  =
  \frac12(1\pm V_0\cos\varphi),
  \label{eq:mz-ideal}
\end{equation}
```
with ideal visibility $`V_0\le1`$.

A which-path marker or absorber introduces branch separation. In MTT this is represented by a damping factor
``` math
\begin{equation}
  D_{12}^{(\rm MZ)}
  =
  \exp[-\tau_{\rm MZ}\Lambda_{12}^{(\rm MZ)}],
\end{equation}
```
assuming admissibility of the corresponding Schur channel. The output probabilities become
``` math
\begin{equation}
  p_\pm^{\rm MTT}
  =
  \frac12
  \left(
  1\pm D_{12}^{(\rm MZ)}V_0\cos\varphi
  \right).
  \label{eq:mz-mtt}
\end{equation}
```

The Mach–Zehnder setup therefore makes projection duality tunable. Recombination without branch marking displays the wave shadow. Strong branch marking suppresses the interference term and yields path-like records.

## Delayed choice and quantum eraser

Delayed-choice and quantum eraser experiments are often described as paradoxical because the final measurement arrangement appears to decide whether the system behaved like a wave or a particle. In MTT, the issue is not retrospective behavior. The issue is which final survivor-basin partition is imposed on the joint branch-marker system.

Let the path branches be correlated with marker states:
``` math
\begin{equation}
  |\Psi\rangle
  =
  \frac{1}{\sqrt2}
  \left(
  |\psi_1\rangle|M_1\rangle
  +
  e^{i\varphi}|\psi_2\rangle|M_2\rangle
  \right).
  \label{eq:eraser-joint-state}
\end{equation}
```
If the marker is measured in the distinguishable basis
``` math
\begin{equation}
  \{|M_1\rangle,|M_2\rangle\},
\end{equation}
```
then path information is stabilized and the unconditional interference is suppressed.

If instead the marker is measured in a recombining basis such as
``` math
\begin{equation}
  |M_\pm\rangle
  =
  \frac{1}{\sqrt2}
  (|M_1\rangle\pm |M_2\rangle),
  \label{eq:eraser-marker-basis}
\end{equation}
```
then conditional subensembles can recover phase-sensitive fringes. The final measurement context has changed the basin partition:
``` math
\begin{equation}
  \{B_1,B_2\}
  \quad\longrightarrow\quad
  \{B_+,B_-\}.
\end{equation}
```

<div id="prop:no-retrocausal-eraser" class="proposition">

**Proposition 38** (No-retrocausal eraser reading). *In the MTT reading, delayed-choice and eraser phenomena require no retroactive change of a past path. They reflect the fact that different final measurement contexts stabilize different survivor-basin partitions of the joint path-marker state.*

</div>

<div class="proof">

*Proof.* The joint state <a href="#eq:eraser-joint-state" data-reference-type="eqref" data-reference="eq:eraser-joint-state">[eq:eraser-joint-state]</a> contains both path and marker degrees of freedom. Measuring the marker in the path-distinguishing basis stabilizes basins correlated with $`M_1`$ and $`M_2`$, suppressing path interference in the unconditional ensemble. Measuring in the recombining basis <a href="#eq:eraser-marker-basis" data-reference-type="eqref" data-reference="eq:eraser-marker-basis">[eq:eraser-marker-basis]</a> stabilizes different conditional basins $`B_\pm`$, within which relative phase information can reappear as conditional fringes. No past event is changed; the final projection context determines the downstream conditional shadow. ◻

</div>

## Matter-wave diffraction

Electron, neutron, atom, and molecule diffraction experiments show that massive objects produce interference and diffraction patterns while still being detected as localized events. This is a direct example of the distinction between ensemble wave shadow and individual particle shadow.

In a diffraction grating experiment, the grating prepares a coherent superposition of many path or momentum branches:
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_{a} c_a|a\rangle.
\end{equation}
```
Free propagation transports the relative phases among the branches. The detection screen then applies finite effects $`E_x`$, giving
``` math
\begin{equation}
  p(x)
  =
  \sum_{a,b}
  c_a c_b^\ast
  \langle b|E_x|a\rangle.
  \label{eq:diffraction-prob}
\end{equation}
```
The off-diagonal terms $`a\neq b`$ generate diffraction structure.

If a gas, thermal bath, or monitoring field distinguishes the branches, the density matrix is modified by an admissible damping matrix:
``` math
\begin{equation}
  \rho_{ab}
  \mapsto
  D_{ab}\rho_{ab}.
\end{equation}
```
The diffraction pattern loses contrast as the off-diagonal terms are suppressed.

The important point is that increasing mass or complexity does not by itself remove wave-like behavior. What matters is whether the relevant branch coherence remains admissible relative to environmental and detector disturbances. This is why matter-wave experiments can display interference for large molecules when isolation is sufficient.

## Hong–Ou–Mandel-type indistinguishability

The branch-coherence logic is not restricted to single-particle path interference. It also applies to multi-particle alternatives in configuration space. Hong–Ou–Mandel-type experiments are governed by indistinguishability between two-particle alternatives.

At a beam splitter, two alternatives may lead to the same detection pattern. If the alternatives are indistinguishable, their amplitudes interfere. If timing, polarization, frequency, or other markers distinguish them, the off-diagonal coherence between alternatives is damped.

Let $`a,b`$ label the relevant two-particle alternatives. The MTT damping rule has the same form:
``` math
\begin{equation}
  \rho_{ab}
  \mapsto
  D_{ab}^{(\rm HOM)}\rho_{ab},
\end{equation}
```
where $`D_{ab}^{(\rm HOM)}`$ depends on the distinguishability introduced by the device and input preparation. Perfect indistinguishability corresponds to
``` math
\begin{equation}
  D_{ab}^{(\rm HOM)}\approx1,
\end{equation}
```
while strong distinguishing information gives
``` math
\begin{equation}
  D_{ab}^{(\rm HOM)}\approx0.
\end{equation}
```

Thus particle-like coincidence records and wave-like multi-particle interference again arise from the same structure: coherent alternatives plus finite measurement effects.

## Quantum Zeno and anti-Zeno regimes

Repeated measurement provides another illustration of device-dependent disturbance. A rapid sequence of weak or strong projections can inhibit or accelerate transitions depending on how the disturbance interacts with the coherent basin geometry.

Let $`P_B`$ denote the projector or finite effect associated with remaining in a basin $`B`$. Repeated monitoring over intervals $`\Delta t`$ acts schematically as
``` math
\begin{equation}
  \rho
  \longmapsto
  \mathcal M_{\Delta t}
  \bigl(
  U_{\Delta t}\rho U_{\Delta t}^\ast
  \bigr),
\end{equation}
```
where $`\mathcal M_{\Delta t}`$ is the finite measurement channel induced by the device. If repeated disturbance continually projects the state back into the same basin, transitions are suppressed. This is the Zeno regime. If the disturbance injects fluctuations into a nearby transition layer or basin boundary, it can enhance switching. This is the anti-Zeno regime.

In MTT terms, Zeno and anti-Zeno behavior are not separate postulates. They are different regimes of the same disturbance–damping–stabilization balance.

## Ramsey and spin-echo reversibility

Ramsey interferometry and spin-echo experiments probe how coherences dephase and then partially rephase under controlled operations. These experiments are important because they show that not all loss of visible interference is irreversible selection.

In MTT language, dephasing without basin capture corresponds to coherent phase dispersion inside an admissible sector. Echo pulses can reverse or refocus this dispersion. By contrast, true survivor-basin stabilization is noninvertible at the effective level: once the measurement context has stabilized a record and discarded incompatible coherences, the original branch phase information is not recoverable within the same downstream description.

Thus Ramsey and echo experiments help separate two mechanisms:

1.  reversible phase dispersion within the coherent sector;

2.  irreversible basin selection after admissibility-breaking disturbance.

This distinction is important for preventing the MTT measurement account from collapsing ordinary reversible dephasing and genuine record formation into the same category.

## Summary of experimental modules

Across these examples the same structure repeats:
``` math
\begin{equation}
  \text{coherent branches}
  \quad\longrightarrow\quad
  \text{device-dependent disturbance}
  \quad\longrightarrow\quad
  \text{branch damping or survivor-basin selection}
  \quad\longrightarrow\quad
  \text{localized records}.
\end{equation}
```

The wave-like shadow is visible when branch coherence survives:
``` math
\begin{equation}
  D_{ab}\approx1.
\end{equation}
```
The particle-like shadow dominates when the device distinguishes and stabilizes branches:
``` math
\begin{equation}
  D_{ab}\approx0.
\end{equation}
```
Intermediate regimes yield partial visibility, threshold behavior, Zeno-like inhibition, anti-Zeno switching, or conditional recovery of fringes, depending on the measurement context.

Thus the double-slit experiment is not an isolated mystery. It is one instance of a general projection-duality architecture.

# Projection-duality theorem

We now collect the previous constructions into the central theorem of the paper. The theorem is stated in two layers. The first layer is mathematical: a single admissible coherent operator has both a local kernel representation and a spectral modal representation, and its sharp limit recovers the identity kernel. The second layer is physical: under coherent phase evolution and finite measurement selection, these two representations appear respectively as particle-like localization and wave-like interference.

## Mathematical kernel-duality theorem

<div id="thm:kernel-dual-representation" class="theorem">

**Theorem 39** (Kernel dual-representation theorem). *Let $`X`$ be compact and let $`A\ge0`$ be a self-adjoint elliptic operator with compact resolvent. Let $`P`$ be the Riesz spectral projector onto an isolated coherent spectral cluster, let $`\chi(A)`$ be an admissible spectral window subordinate to that cluster, and let $`\tau_{\mathrm{adm}}>0`$. Define
``` math
\begin{equation}
  B_{\mathrm{adm}}
  =
  P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P.
  \label{eq:theorem-badm}
\end{equation}
```
Then:*

1.  *$`B_{\mathrm{adm}}`$ is a bounded positive operator on $`L^2(X)`$.*

2.  *For $`\tau_{\mathrm{adm}}>0`$, $`B_{\mathrm{adm}}`$ is smoothing on the retained spectral sector and has a smooth Schwartz kernel $`K_{\mathrm{adm}}(x,y)`$, under the regularity assumptions of Assumption <a href="#ass:fixed-point-spectral-data" data-reference-type="ref" data-reference="ass:fixed-point-spectral-data">1</a>.*

3.  *In the spectral representation,
    ``` math
    \begin{equation}
        K_{\mathrm{adm}}(x,y)
        =
        \sum_{n\in\mathrm{coh}}
        \chi(\lambda_n)^2 e^{-\tau_{\mathrm{adm}}\lambda_n}
        \phi_n(x)\phi_n^\ast(y).
        \label{eq:theorem-spectral-kernel}
    \end{equation}
    ```*

4.  *In the local representation, $`x\mapsto K_{\mathrm{adm}}(x,x_0)`$ is the finite coherent response to an ideal source at $`x_0`$.*

5.  *Under the joint sharp limit of complete bandwidth and vanishing proper-time width, $`K_{\mathrm{adm}}(x,y)`$ converges to $`\delta(x-y)`$ distributionally in the sense of <a href="#thm:delta-limit" data-reference-type="ref+label" data-reference="thm:delta-limit">15</a>.*

</div>

<div class="proof">

*Proof.* Since $`A`$ is nonnegative self-adjoint, the spectral theorem defines $`e^{-\tau_{\mathrm{adm}}A}`$ and $`\chi(A)`$ by functional calculus. Since $`P`$ is a Riesz spectral projector of $`A`$, it is a bounded orthogonal spectral projector and commutes with both $`\chi(A)`$ and $`e^{-\tau_{\mathrm{adm}}A}`$. Thus $`B_{\mathrm{adm}}`$ is bounded. It is positive because it is diagonal in the spectral representation with nonnegative eigenvalues
``` math
\begin{equation}
  p_n\chi(\lambda_n)^2e^{-\tau_{\mathrm{adm}}\lambda_n}\ge0.
\end{equation}
```

For $`\tau_{\mathrm{adm}}>0`$, elliptic heat-kernel regularity implies that $`e^{-\tau_{\mathrm{adm}}A}`$ is smoothing. Since $`P`$ and $`\chi(A)`$ are spectral multipliers subordinate to the coherent sector, the product preserves the retained smooth spectral domain and has the asserted smooth kernel under the regularity assumptions.

The spectral formula follows directly from applying the product $`P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P`$ to the eigenbasis $`A\phi_n=\lambda_n\phi_n`$. Only retained modes with $`p_n=1`$ contribute, giving <a href="#eq:theorem-spectral-kernel" data-reference-type="eqref" data-reference="eq:theorem-spectral-kernel">[eq:theorem-spectral-kernel]</a>.

The local response statement follows from the definition of the Schwartz kernel:
``` math
\begin{equation}
  (B_{\mathrm{adm}}\delta_{x_0})(x)=K_{\mathrm{adm}}(x,x_0)
\end{equation}
```
in the distributional sense. The sharp delta limit is exactly <a href="#thm:delta-limit" data-reference-type="ref+label" data-reference="thm:delta-limit">15</a>. ◻

</div>

<div id="rem:not-merely-interpretive" class="remark">

*Remark 40* (Why the theorem is not merely interpretive). The theorem does not use the words “wave” or “particle.” It is an operator statement. It says that a single admissible coherent operator has both a local kernel representation and a spectral modal representation. The physical terminology enters only after specifying how experiments read these representations.

</div>

## Physical projection-duality theorem

We now add the physical assumptions needed to interpret the two representations.

<div id="ass:physical-reading" class="assumption">

**Assumption 41** (Physical reading assumptions). In addition to the hypotheses of <a href="#thm:kernel-dual-representation" data-reference-type="ref+label" data-reference="thm:kernel-dual-representation">39</a>, assume:

1.  the retained sector carries a self-adjoint coherent phase generator $`H_{\rm coh}`$, giving unitary phase evolution $`U_t^{\rm coh}=e^{-itH_{\rm coh}}`$;

2.  measurement contexts are represented by finite POVMs or effect densities on the retained sector;

3.  branch damping induced by a measurement context is represented by a valid Schur channel $`\rho\mapsto D\circ\rho`$, with $`D\succeq0`$ and $`D_{aa}=1`$;

4.  stabilized detector records correspond to survivor basins of the measurement context.

</div>

<div id="thm:wave-particle-projection-duality" class="theorem">

**Theorem 42** (Wave–particle projection duality). *Under Assumptions <a href="#ass:fixed-point-spectral-data" data-reference-type="ref" data-reference="ass:fixed-point-spectral-data">1</a>, <a href="#ass:coherent-phase-evolution" data-reference-type="ref" data-reference="ass:coherent-phase-evolution">18</a>, and <a href="#ass:physical-reading" data-reference-type="ref" data-reference="ass:physical-reading">41</a>, a finite coherent-sector excitation has two downstream shadows:*

1.  *a particle-like local shadow, obtained when the finite local response kernel is probed below detector resolution and idealized by the delta limit;*

2.  *a wave-like spectral shadow, obtained when retained modal or branch phases evolve coherently and contribute off-diagonal interference terms to observable probabilities.*

*Measurement contexts interpolate between these shadows by damping or preserving off-diagonal branch coherences and stabilizing survivor-basin records. Therefore wave-like interference and particle-like localization are not distinct ontological primitives; they are different projection shadows of one finite coherent-sector excitation.*

</div>

<div class="proof">

*Proof.* By <a href="#thm:kernel-dual-representation" data-reference-type="ref+label" data-reference="thm:kernel-dual-representation">39</a>, the admissible coherent operator has a local kernel representation and a spectral modal representation.

For the particle-like statement, fix a detector context whose finite effects $`E_x`$ have localization width below the detector resolution. Then the local kernel response $`K_{\mathrm{adm}}(x,x_0)`$, or the corresponding detector effect $`E_x`$, is operationally indistinguishable from a sharp position effect. By <a href="#thm:delta-limit" data-reference-type="ref+label" data-reference="thm:delta-limit">15</a>, the exact sharp position description is obtained as the distributional delta limit. Hence particle-like localization is the local sharp shadow of the finite coherent kernel.

For the wave-like statement, Assumption <a href="#ass:coherent-phase-evolution" data-reference-type="ref" data-reference="ass:coherent-phase-evolution">18</a> gives unitary phase transport on the retained sector. By <a href="#prop:interference-criterion" data-reference-type="ref+label" data-reference="prop:interference-criterion">21</a>, observable probabilities are phase-sensitive exactly when off-diagonal branch or modal coherences contribute. Therefore the spectral representation of the retained coherent sector gives wave-like interference whenever those coherences survive.

For the measurement statement, <a href="#thm:schur-channel" data-reference-type="ref+label" data-reference="thm:schur-channel">28</a> shows that admissible branch damping is a valid quantum channel when $`D\succeq0`$ and $`D_{aa}=1`$. If $`D_{ab}\approx1`$ for relevant branches, off-diagonal coherence survives and the wave-like shadow is visible. If $`D_{ab}\approx0`$, off-diagonal coherence is suppressed and the downstream description is a mixture of branch-stabilized records. The exact record is supplied by survivor-basin stabilization in the measurement context.

Thus the same coherent excitation gives wave-like or particle-like behavior according to which projection context is imposed and which coherences survive. This proves the projection-duality statement. ◻

</div>

``` math
\begin{equation}
  \boxed{
  \text{wave--particle duality}
  =
  \text{projection duality}.
  }
\end{equation}
```

## Corollaries

<div id="cor:ordinary-wave-mechanics" class="corollary">

**Corollary 43** (Recovery of ordinary wave mechanics). *If branch damping is absent or negligible,
``` math
\begin{equation}
  D_{ab}\approx1,
\end{equation}
```
and coherent phase evolution is retained, then the MTT description reduces to ordinary wave-mechanical interference on the coherent sector.*

</div>

<div class="proof">

*Proof.* When $`D_{ab}\approx1`$, the Schur channel leaves off-diagonal coherences approximately unchanged. Probabilities therefore include the usual interference terms. The coherent phase generator $`H_{\rm coh}`$ supplies the standard unitary phase evolution. ◻

</div>

<div id="cor:point-particle-detection" class="corollary">

**Corollary 44** (Recovery of point-particle detection). *If detector kernels are narrow compared with the resolution scale and the sharp effect limit is taken, then finite MTT detector effects reduce to ordinary pointlike detection effects:
``` math
\begin{equation}
  E_x\to |x\rangle\langle x|.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* By the detector-kernel construction, $`E_x=|k_x\rangle\langle k_x|`$. In the sharp detector limit $`k_x(y)\to\delta(y-x)`$, giving $`E_x\to |x\rangle\langle x|`$. ◻

</div>

<div id="cor:incoherent-mixture" class="corollary">

**Corollary 45** (Incoherent mixture from strong branch selection). *If a measurement context strongly distinguishes branches so that
``` math
\begin{equation}
  D_{ab}\approx0
  \qquad
  (a\neq b),
\end{equation}
```
then interference terms vanish and the downstream ensemble is described by the corresponding incoherent branch mixture.*

</div>

<div class="proof">

*Proof.* The Schur map sends $`\rho_{ab}\mapsto D_{ab}\rho_{ab}`$. If $`D_{ab}\approx0`$ for $`a\neq b`$, then all off-diagonal branch terms are suppressed. Observable probabilities therefore contain only diagonal branch contributions. ◻

</div>

<div id="cor:no-primitive-conversion" class="corollary">

**Corollary 46** (No primitive wave-to-particle conversion). *Within the stated assumptions, measurement does not require a primitive conversion of a wave into a particle. It requires only a change in projection context: branch coherences are preserved, damped, or selected according to the measurement-device data.*

</div>

<div class="proof">

*Proof.* The proof of <a href="#thm:wave-particle-projection-duality" data-reference-type="ref+label" data-reference="thm:wave-particle-projection-duality">42</a> shows that wave-like and particle-like descriptions are downstream shadows of the same coherent-sector excitation. Measurement changes the effective description by applying finite effects and admissible branch damping, not by changing the ontological type of the excitation. ◻

</div>

## Relation to complementarity

The projection-duality theorem refines, rather than discards, the traditional complementarity intuition. Complementarity says that wave and particle descriptions are revealed by different experimental arrangements. MTT explains why this is so: different experimental arrangements implement different projection contexts.

An interference setup preserves or recombines branch coherence:
``` math
\begin{equation}
  D_{ab}\approx1.
\end{equation}
```
A which-way setup distinguishes branches and stabilizes path-correlated records:
``` math
\begin{equation}
  D_{ab}\approx0.
\end{equation}
```
Intermediate setups yield partial visibility.

Because projection is generally non-invertible, no single downstream description captures all upstream coherent structure. A wave-like description and a particle-like description can both be accurate in their respective contexts without being jointly reducible to a single classical picture.

## Interpretive conclusion

The theorem gives the formal version of the central claim:
``` math
\begin{equation}
  \boxed{
  \text{one finite coherent-sector excitation}
  \quad\Longrightarrow\quad
  \begin{cases}
    \text{local delta-like particle shadow},\\
    \text{spectral phase-coherent wave shadow},\\
    \text{finite measurement-selection shadow}.
  \end{cases}
  }
\end{equation}
```

The ordinary particle picture is recovered when local finite kernels are idealized by Dirac deltas. The ordinary wave picture is recovered when retained phases evolve coherently and off-diagonal terms survive. The ordinary measurement picture is recovered when finite effects are idealized by sharp projectors and survivor-basin selection has stabilized a record.

Thus wave–particle duality is not an additional mystery placed on top of MTT. It is a direct consequence of coherent projection, finite kernels, phase evolution, and survivor-basin selection.

# Relation to standard quantum mechanics and existing accounts

The projection-duality theorem is not intended to replace the working formalism of quantum mechanics. It is intended to explain why that formalism has both wave-like and particle-like faces. This section clarifies how the MTT account relates to ordinary quantum mechanics, Born probabilities, decoherence, quantum field theory, pilot-wave theory, and extended-object approaches such as string theory.

## Recovery of standard quantum mechanics

Standard quantum mechanics is recovered in the appropriate limiting regimes.

When coherent phase evolution is retained, a state evolves as
``` math
\begin{equation}
  |\psi(t)\rangle
  =
  e^{-itH_{\rm coh}}|\psi(0)\rangle.
  \label{eq:standard-unitary-recovery}
\end{equation}
```
When finite detector effects are idealized as sharp projectors,
``` math
\begin{equation}
  E_i\to \Pi_i,
  \label{eq:sharp-projector-recovery}
\end{equation}
```
one obtains the usual projective-measurement description. When branch damping is absent,
``` math
\begin{equation}
  D_{ab}=1,
\end{equation}
```
the off-diagonal terms of the density matrix remain intact and ordinary interference is recovered. When branch damping is strong,
``` math
\begin{equation}
  D_{ab}=0
  \qquad
  (a\neq b),
\end{equation}
```
the density matrix reduces to the corresponding incoherent mixture in the selected branch basis.

Thus the MTT construction reproduces the standard cases:
``` math
\begin{align}
  D_{ab}=1
  &\quad\Longrightarrow\quad
  \text{coherent wave-like interference},
  \\
  D_{ab}=0
  &\quad\Longrightarrow\quad
  \text{incoherent branch mixture},
  \\
  E_x\to |x\rangle\langle x|
  &\quad\Longrightarrow\quad
  \text{sharp pointlike detection}.
\end{align}
```

The difference is not in the limiting formulas. The difference is in the order of explanation. In standard quantum mechanics, wave evolution and pointlike measurement are part of the formal postulates. In MTT, both are downstream limits of finite coherent projection.

## Born probabilities and basin weights

The projection-duality theorem concerns the coexistence of wave-like interference and particle-like localization. It does not by itself replace the Born rule. In the MTT corpus, Born probabilities are associated with basin-measure structure.

Let $`\{B_i\}_{i\in I}`$ be the survivor-basin partition associated with a measurement context $`\mathsf M`$, and let $`\mu`$ be the relevant admissibility-weighted basin measure. The outcome probability is
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i)}{\sum_j\mu(B_j)}.
  \label{eq:born-basin-probability-existing}
\end{equation}
```
This answers the question:
``` math
\begin{equation}
  \text{Which stabilized record occurs?}
\end{equation}
```

By contrast, branch damping answers the question:
``` math
\begin{equation}
  \text{How much interference remains between alternatives?}
\end{equation}
```
The damping factors $`D_{ab}`$ multiply off-diagonal density-matrix entries. They control visibility, not final outcome frequencies by themselves.

This separation is essential. In the double-slit experiment, individual screen events are distributed according to the screen effects and basin capture. The ensemble pattern contains fringes only if branch coherences survive:
``` math
\begin{equation}
  \rho_{12}\mapsto D_{12}\rho_{12}.
\end{equation}
```
Thus:
``` math
\begin{equation}
  \boxed{
  \text{Born weights govern selection frequency},
  }
  \qquad
  \boxed{
  \text{branch damping governs interference visibility}.
  }
\end{equation}
```

## Decoherence

The MTT branch-damping map resembles decoherence:
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab}.
\end{equation}
```
This resemblance is not accidental. Environmental entanglement is one physical way of suppressing off-diagonal coherences in a reduced density matrix. Standard decoherence therefore captures an important part of the wave-to-classical transition.

The MTT claim is broader and more structured. Decoherence explains how coherence can become inaccessible after tracing out environmental degrees of freedom. MTT additionally requires:

1.  a finite coherent kernel determining admissible support;

2.  a detector or environment sector that supplies a valid measurement context;

3.  a positive branch-damping channel;

4.  a survivor-basin stabilization mechanism;

5.  a basin-measure account of outcome frequencies.

In this sense, decoherence is a shadow of one part of the MTT measurement architecture: coherence suppression. It does not by itself provide the full projection-duality structure, because it does not identify both pointlike localization and wavelike interference as two representations of one admissible coherent kernel, nor does it by itself select a unique stabilized outcome basin.

## Quantum field theory

Quantum field theory already weakens the classical idea of a particle as a tiny billiard ball. Particles are excitations of fields, and local detector events arise from interactions between fields and measuring devices. This is close in spirit to the MTT view that particle-like behavior is not a fundamental point ontology.

The MTT difference is again structural. QFT commonly uses local fields, point insertions, distributions, and propagators as part of its formal machinery. In the delta-projection reading, the pointlike structures
``` math
\begin{equation}
  \delta(x-y),
  \qquad
  \phi(x),
  \qquad
  \int \phi(x)^4\,\mathrm{d}x
\end{equation}
```
are sharp shadows of finite coherent kernels and overlap structures. A filtered propagator such as
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{e^{-\tau_{\mathrm{adm}}|k|^2}}{|k|^2+m^2}
\end{equation}
```
is not introduced merely as a regulator; in the MTT reading it is the propagator-level shadow of finite coherent support.

Thus MTT does not deny QFT. It attempts to explain why QFT’s local distributional structures are so effective: they are idealized limits of finite coherent projection.

## Pilot-wave theory

Pilot-wave theory gives a clear ontology in which particles have definite positions guided by a wave. In a double-slit experiment, the guiding wave passes through both slits, while the particle follows a definite trajectory influenced by that wave. This is a genuine common-source attempt in the sense that it explains interference and localized detection within one theory.

The MTT account differs in ontology. It does not postulate both a point particle and a guiding wave as separate real ingredients. Instead, it treats the particle-like and wave-like descriptions as two downstream shadows of one finite coherent-sector excitation:
``` math
\begin{equation}
  \text{particle shadow}
  =
  \text{local delta-limit representation},
\end{equation}
```
``` math
\begin{equation}
  \text{wave shadow}
  =
  \text{spectral phase-coherent representation}.
\end{equation}
```
Thus pilot-wave theory is dual-ontology at the foundational level, whereas the MTT account is projection-dual at the effective-description level.

## String and extended-object approaches

String theory and other extended-object approaches also reject fundamental point-particle ontology. In perturbative string theory, point particles are replaced by one-dimensional objects whose vibrational modes appear as particle species at scales much larger than the string length. This shares an important intuition with MTT:
``` math
\begin{equation}
  \text{point particle}
  =
  \text{low-resolution limit of a non-pointlike structure}.
\end{equation}
```

The difference is that string theory’s common source is an extended object with vibrational modes, whereas the MTT common source is an admissible coherent projection kernel. MTT’s construction also places measurement and survivor-basin selection at the center of the wave-particle account. The pointlike shadow arises from the local delta limit of a finite kernel; the wave-like shadow arises from retained spectral phase; the measurement record arises from finite survivor-basin stabilization.

Thus string theory is close in the point-particle replacement sense, but it is not primarily a projection-duality account of measurement and interference. MTT’s claim is not that strings are wrong, but that the wave-particle issue can be reframed more generally as a statement about projections of coherent support.

## Complementarity

The traditional complementarity view says that wave and particle descriptions are revealed by mutually exclusive experimental arrangements. MTT preserves this insight while giving it a structural mechanism.

Different experimental arrangements implement different projection contexts:
``` math
\begin{equation}
  \mathsf M_{\rm interference}
  \quad\text{preserves or recombines branch coherence},
\end{equation}
```
whereas
``` math
\begin{equation}
  \mathsf M_{\rm which\text{-}way}
  \quad\text{distinguishes branches and stabilizes records}.
\end{equation}
```
Because projection is generally non-invertible, no single downstream description captures all upstream coherent structure. The wave and particle descriptions are therefore complementary not because nature switches between two substances, but because different projection contexts expose different shadows of the same coherent-sector excitation.

## Novelty claim

The novelty of the present account is not that finite kernels exist, nor that interference comes from phase, nor that measurement devices can decohere systems. All of these are familiar.

The distinctive claim is the unified selection architecture:
``` math
\begin{equation}
  \boxed{
  \text{one finite admissible coherent kernel}
  \quad\Longrightarrow\quad
  \begin{cases}
  \text{local delta-like particle shadow},\\
  \text{spectral phase wave shadow},\\
  \text{finite measurement-selection shadow}.
  \end{cases}
  }
\end{equation}
```
The kernel is not chosen as a phenomenological smoothing function. It is selected by fixed-point coherent data and damping/admissibility. Branch damping is not an arbitrary visibility factor. It must define a valid quantum channel. Outcome probabilities are not identified with damping factors. They are basin-measure weights.

This combination is the specific MTT contribution:
``` math
\begin{equation}
  \boxed{
  \text{wave and particle are not two primitives, but two projection shadows of one
  admissible coherent-sector structure.}
  }
\end{equation}
```

# Compatibility with basin-measure and disturbance-stabilization papers

This section records how the present projection-duality theorem fits with two earlier MTT developments: the basin-measure account of the Born rule and the disturbance-stabilization account of measurement. The purpose is to avoid conflating three related but distinct structures:

1.  basin-measure probabilities;

2.  branch-coherence visibility;

3.  localized survivor-basin records.

## Compatibility with the basin-measure Born-rule bridge

The basin-measure bridge treats quantum probabilities as shadows of basin measures on an admissible coherent sector. In its simplest form, if a measurement context has survivor basins
``` math
\begin{equation}
  \{B_i\}_{i\in I},
\end{equation}
```
and if $`\mu`$ is the admissibility-weighted basin measure, then the outcome probability is
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i)}{\sum_j\mu(B_j)}.
  \label{eq:compat-born-basin}
\end{equation}
```
This answers the outcome-frequency question:
``` math
\begin{equation}
  \text{Which stabilized record occurs, and how often?}
\end{equation}
```

The present paper answers a different question:
``` math
\begin{equation}
  \text{Why can the same excitation produce both interference and localized records?}
\end{equation}
```
The answer is that the excitation has both a spectral phase shadow and a local delta-like shadow, and measurement contexts determine which branch coherences survive.

Thus the Born-rule bridge and the projection-duality theorem are complementary. The Born bridge supplies the basin-measure weights for stabilized outcomes. The duality theorem supplies the representation structure explaining why coherent interference can coexist with localized detection.

<div id="prop:probability-visibility-separation" class="proposition">

**Proposition 47** (Separation of probability and visibility). *Let a measurement context $`\mathsf M`$ have survivor basins $`B_i`$ with basin probabilities $`\mathbb P(i)`$ given by <a href="#eq:compat-born-basin" data-reference-type="eqref" data-reference="eq:compat-born-basin">[eq:compat-born-basin]</a>. Let the same context induce a valid branch-damping channel
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}^{(\mathsf M)}\rho_{ab}.
\end{equation}
```
Then $`\mathbb P(i)`$ and $`D_{ab}^{(\mathsf M)}`$ answer different structural questions:*

1.  *$`\mathbb P(i)`$ determines the frequency of stabilized records;*

2.  *$`D_{ab}^{(\mathsf M)}`$ determines the survival of interference between branches $`a,b`$.*

*Therefore branch damping must not be identified with the Born rule.*

</div>

<div class="proof">

*Proof.* The basin probability $`\mathbb P(i)`$ is defined on the partition of stabilized outcome basins. It assigns weights to final records. The damping factor $`D_{ab}^{(\mathsf M)}`$ acts on off-diagonal density-matrix entries before or during stabilization and determines whether cross terms contribute to observable probabilities. Since diagonal basin weights and off-diagonal coherence survival act on different components of the effective description, they are not the same object. ◻

</div>

## Minimal basin-capture assumptions

The basin-measure formula requires assumptions. In the setting of this paper, the minimal ones are:

1.  a stationary or experimentally reproducible input ensemble $`(\Omega,\mu)`$;

2.  a measurable survivor-basin partition
    ``` math
    \begin{equation}
        \Omega=\bigcup_i B_i,
        \qquad
        B_i\cap B_j=\varnothing\quad(i\neq j),
    \end{equation}
    ```
    up to measure-zero boundaries;

3.  almost-sure finite capture into exactly one basin under the measurement-context stabilization dynamics.

Under these assumptions,
``` math
\begin{equation}
  \mathbb P(i)=\frac{\mu(B_i)}{\mu(\Omega)}
\end{equation}
```
is well-defined. If the partition is not measurable, if capture fails, or if trajectories hover near basin boundaries for experimentally relevant times, then the simple basin-probability formula must be replaced by a metastable or protocol-dependent description.

<div id="rem:basin-capture-duality" class="remark">

*Remark 48* (Why this matters for duality). The double-slit interference pattern concerns ensemble density on a screen. The individual screen click concerns basin capture by the detector. These are compatible only if one keeps the ensemble interference structure distinct from the single-record stabilization process.

</div>

## Compatibility with measurement as disturbance and stabilization

The disturbance-stabilization measurement account states that a device perturbs a coherent mode away from a quiet or balanced submanifold. The system then undergoes local smoothing, global projection, and stabilization into an admissible branch. In schematic form:
``` math
\begin{equation}
  \text{disturbance}
  \longrightarrow
  \text{damping/smoothing}
  \longrightarrow
  \text{projection}
  \longrightarrow
  \text{stabilized outcome}.
  \label{eq:disturbance-stabilization-chain}
\end{equation}
```

The present paper supplies an operator-theoretic version of this chain for wave-particle duality:
``` math
\begin{equation}
  \rho
  \longmapsto
  D^{(\mathsf M)}\circ\rho
  \longmapsto
  \{E_i^{(\mathsf M)}\}
  \longmapsto
  B_i^{(\mathsf M)}.
  \label{eq:operator-disturbance-chain}
\end{equation}
```
Here $`D^{(\mathsf M)}`$ records the survival of branch coherence, the effect family $`\{E_i^{(\mathsf M)}\}`$ records the finite measurement readout, and $`B_i^{(\mathsf M)}`$ records the survivor basin.

This is why different devices matter. A weak which-way marker, a destructive absorber, a Stern–Gerlach magnet, and a phase-recombining interferometer impose different disturbance maps and different survivor-basin partitions.

## Disturbance strength and visibility knees

Let $`\delta\ge0`$ denote a scalar measure of measurement strength, such as marker coupling, environmental distinguishability, detector gain, or branch-separation amplitude. A simple MTT-compatible visibility model is
``` math
\begin{equation}
  D_{12}(\delta)
  =
  \exp[-\tau_{\rm det}\Lambda_{12}^{\rm det}(\delta)].
  \label{eq:visibility-delta-model}
\end{equation}
```
If
``` math
\begin{equation}
  \Lambda_{12}^{\rm det}(\delta)
\end{equation}
```
is small for weak disturbance and grows across a branch-separation threshold, then the visibility
``` math
\begin{equation}
  V(\delta)
  =
  D_{12}(\delta)V_0
\end{equation}
```
falls smoothly at first and then rapidly near the threshold. This produces a knee-like transition between wave-like and particle-like behavior.

<div id="rem:weak-strong-threshold" class="remark">

*Remark 49* (Weak, strong, and threshold regimes). The disturbance-stabilization paper emphasizes that measurement need not be all-or-nothing. The present formula makes that continuous structure explicit. Weak disturbance leaves $`D_{12}\approx1`$, strong disturbance gives $`D_{12}\approx0`$, and threshold regimes can produce rapid visibility loss, switching, or hysteresis depending on basin geometry.

</div>

## OU floors and finite detector width

The disturbance-stabilization account also interprets uncertainty floors as finite balances between disturbance and damping. In the present notation, this appears as the finite width of the detector or coherent kernel. Even after damping, the kernel need not collapse to a delta. Instead, it may approach a finite Ornstein–Uhlenbeck-like floor set by the balance between disturbance injection and stabilization.

This supports the hierarchy used throughout the paper:
``` math
\begin{equation}
  \text{finite POVM/effect}
  \quad\text{is native},
\end{equation}
```
while
``` math
\begin{equation}
  \text{PVM/delta measurement}
  \quad\text{is a singular idealization}.
\end{equation}
```

In double-slit language, this means that the localized screen record is never literally a mathematical point. It is a finite stabilized detector event whose width is below the relevant resolution scale.

## What this paper adds

The earlier measurement papers explain how outcomes stabilize and how probabilities arise from basins. The present paper adds a specific structural synthesis:
``` math
\begin{equation}
  \text{the same finite coherent kernel has both a local delta-like shadow and a spectral
  phase-coherent shadow}.
\end{equation}
```
It also adds a channel-consistency condition for interference damping:
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```
This ensures that the visibility-reduction map is a valid quantum operation, not merely an interpretive multiplier.

Thus the paper should be read as a bridge between three parts of MTT:

1.  the delta-projection sequence, where pointlike objects are sharp limits of finite kernels;

2.  the measurement sequence, where outcomes are disturbance-stabilized survivor basins;

3.  the basin-measure sequence, where Born probabilities are basin weights.

## Compatibility summary

The relationship can be summarized as:
``` math
\begin{align}
  \text{finite coherent kernel}
  &\longrightarrow
  \text{local particle shadow and spectral wave shadow},
  \\
  \text{branch damping}
  &\longrightarrow
  \text{visibility suppression},
  \\
  \text{survivor-basin capture}
  &\longrightarrow
  \text{individual outcome records},
  \\
  \text{basin measure}
  &\longrightarrow
  \text{Born frequencies}.
\end{align}
```

These are not competing explanations. They are different layers of one MTT measurement architecture.

# Phenomenological consequences and testable scalings

The projection-duality theorem is primarily structural. It identifies wave-like and particle-like behavior as two shadows of a finite coherent-sector excitation. Nevertheless, the framework has phenomenological content. Once a sector supplies the relevant operator data, detector kernel, damping scale, and branch-separation metric, the theory gives definite finite-width and visibility corrections.

This section records the leading scaling relations. They should not be read as universal numerical predictions. They are templates: in each physical sector the quantities $`\tau_{\mathrm{adm}}`$, $`\tau_{\mathsf M}`$, $`\Lambda_{\rm eff}`$, $`D_{ab}`$, and $`\Lambda_{ab}^{(\mathsf M)}`$ must be derived or bounded from the corresponding coherent-sector and detector-sector data.

## Pointlikeness bounds

The particle-like approximation is valid when the coherent width is below experimental resolution:
``` math
\begin{equation}
  \ell_{\rm coh}\ll \ell_{\rm res}.
  \label{eq:phen-pointlike-length}
\end{equation}
```
In heat-kernel models,
``` math
\begin{equation}
  \ell_{\rm coh}\sim \sqrt{\tau_{\mathrm{adm}}}.
\end{equation}
```
Equivalently, in energy or momentum terms,
``` math
\begin{equation}
  E_{\rm probe}\ll \Lambda_{\rm eff},
  \qquad
  \Lambda_{\rm eff}\sim\tau_{\mathrm{adm}}^{-1/2}.
  \label{eq:phen-pointlike-energy}
\end{equation}
```

If an experiment observes no deviation from pointlike behavior up to characteristic scale $`E_{\rm max}`$ with tolerance $`\eta`$, the generic scaling bound is
``` math
\begin{equation}
  \tau_{\mathrm{adm}}E_{\rm max}^2\lesssim \eta.
  \label{eq:phen-tau-bound}
\end{equation}
```
Thus
``` math
\begin{equation}
  \Lambda_{\rm eff}
  \gtrsim
  \frac{E_{\rm max}}{\sqrt{\eta}}.
  \label{eq:phen-lambda-bound}
\end{equation}
```

This is the same logic used in effective form-factor constraints. The MTT difference is that $`\tau_{\mathrm{adm}}`$ is not introduced merely as a fitted form-factor scale. It is, in principle, fixed by discarded-sector damping and admissibility:
``` math
\begin{equation}
  \tau_{\mathrm{adm}}
  =
  \lambda_\ast^{-1}\log(C_Q/\epsilon_{\mathrm{adm}}).
  \label{eq:phen-tau-fixed}
\end{equation}
```

<div id="rem:null-results-pointlike" class="remark">

*Remark 50* (Interpretation of null results). A null result in a high-resolution scattering or localization experiment does not prove that particles are literal points. In the MTT reading it implies that the finite coherent width is below the resolution scale tested by the experiment.

</div>

## Finite propagator corrections

In a flat Euclidean coherent chart with $`A=-\Delta`$, the finite coherent kernel gives the filtered scalar propagator
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{e^{-\tau_{\mathrm{adm}}|k|^2}}{|k|^2+m^2}.
  \label{eq:phen-propagator}
\end{equation}
```
At low momentum,
``` math
\begin{equation}
  e^{-\tau_{\mathrm{adm}}|k|^2}
  =
  1-\tau_{\mathrm{adm}}|k|^2+O(\tau_{\mathrm{adm}}^2|k|^4),
\end{equation}
```
so
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{1}{|k|^2+m^2}
  -
  \tau_{\mathrm{adm}}\frac{|k|^2}{|k|^2+m^2}
  +
  O\!\left(
  \frac{\tau_{\mathrm{adm}}^2|k|^4}{|k|^2+m^2}
  \right).
  \label{eq:phen-propagator-expansion}
\end{equation}
```

The leading correction is controlled by
``` math
\begin{equation}
  \tau_{\mathrm{adm}}|k|^2.
\end{equation}
```
Therefore short-distance deviations from pointlike propagation are expected only when
``` math
\begin{equation}
  |k|^2\sim \tau_{\mathrm{adm}}^{-1}.
\end{equation}
```

<div id="rem:gauge-lorentzian-caution-phen" class="remark">

*Remark 51* (Gauge and Lorentzian caution). The scalar Euclidean propagator formula is a clean model of finite coherent support. Gauge theories and Lorentzian scattering require compatibility with gauge identities, positivity, causality, and unitarity. The projection-duality theorem does not by itself prove those sector-specific consistency conditions.

</div>

## Visibility loss

In a two-branch interference experiment, the MTT visibility law is
``` math
\begin{equation}
  V_{\rm MTT}
  =
  D_{12}V_0.
  \label{eq:phen-visibility}
\end{equation}
```
If the damping factor is
``` math
\begin{equation}
  D_{12}
  =
  \exp[-\tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}],
  \label{eq:phen-D}
\end{equation}
```
then for weak disturbance,
``` math
\begin{equation}
  1-D_{12}
  =
  \tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}
  +
  O\!\left((\tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)})^2\right).
  \label{eq:phen-visibility-small}
\end{equation}
```

If an experiment observes no visibility loss above tolerance $`\eta_V`$, then
``` math
\begin{equation}
  \tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}
  \lesssim
  \eta_V.
  \label{eq:phen-visibility-bound}
\end{equation}
```
Thus interference visibility bounds the product of measurement-sector time scale and branch-separation scale.

<div id="rem:visibility-constraints-measure" class="remark">

*Remark 52* (What visibility constraints measure). Visibility constraints do not directly measure the Born probabilities of final records. They measure the survival of off-diagonal coherence between alternatives. This is why a high visibility experiment constrains $`D_{12}`$, whereas repeated record frequencies constrain basin measures.

</div>

## Disturbance-dependent knees

Let $`\delta`$ denote a controllable disturbance strength. Examples include which-way marker coupling, gas pressure in matter-wave interferometry, detector gain, magnetic-field gradient, or timing distinguishability. Suppose
``` math
\begin{equation}
  D_{12}(\delta)
  =
  \exp[-\tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}(\delta)].
  \label{eq:phen-D-delta}
\end{equation}
```
If $`\Lambda_{12}^{(\mathsf M)}(\delta)`$ grows slowly at first and then rapidly near an admissibility threshold, the measured visibility
``` math
\begin{equation}
  V(\delta)
  =
  V_0D_{12}(\delta)
  \label{eq:phen-V-delta}
\end{equation}
```
will display a knee-like transition.

This gives a qualitative experimental signature:
``` math
\begin{equation}
  \text{smooth weak-disturbance visibility loss}
  \quad\longrightarrow\quad
  \text{rapid threshold suppression}.
\end{equation}
```
Such knees are expected when the measurement disturbance pushes the state across a survivor-basin boundary rather than merely adding small reversible phase noise.

## Reversibility versus basin capture

The distinction between reversible dephasing and irreversible basin capture is experimentally important.

If a disturbance only disperses phases inside the coherent sector, then echo or reversal protocols may recover visibility:
``` math
\begin{equation}
  D_{12}^{\rm effective}\to1
\end{equation}
```
after rephasing.

If a disturbance stabilizes a survivor-basin record, the lost branch coherence is not recoverable inside the same downstream description:
``` math
\begin{equation}
  D_{12}\approx0
  \quad\text{after record stabilization}.
\end{equation}
```

Thus MTT predicts a qualitative distinction between:

1.  reversible coherence dispersion;

2.  irreversible measurement-induced selection.

Ramsey and echo experiments probe the first; strong which-way measurement probes the second.

## Device-dependence as a prediction

Because different devices define different measurement contexts,
``` math
\begin{equation}
  \mathsf M_1\neq \mathsf M_2,
\end{equation}
```
they may induce different damping matrices even when aimed at the same nominal observable:
``` math
\begin{equation}
  D_{ab}^{(\mathsf M_1)}
  \neq
  D_{ab}^{(\mathsf M_2)}.
\end{equation}
```
Thus MTT predicts that visibility loss is not determined solely by the abstract observable label. It depends on the device’s disturbance channel, detector kernel, and branch-separation metric.

This is not surprising operationally, but MTT makes it structural. The device is part of the projection context, not an external passive reader.

## Summary of testable scalings

The main phenomenological scalings are:
``` math
\begin{align}
  \ell_{\rm coh}
  &\sim
  \sqrt{\tau_{\mathrm{adm}}},
  \\
  \Lambda_{\rm eff}
  &\sim
  \tau_{\mathrm{adm}}^{-1/2},
  \\
  \tau_{\mathrm{adm}}E_{\rm max}^2
  &\lesssim
  \eta
  \quad
  \text{for unresolved pointlike behavior},
  \\
  V_{\rm MTT}
  &=
  D_{12}V_0,
  \\
  D_{12}
  &=
  \exp[-\tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}],
  \\
  \tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}
  &\lesssim
  \eta_V
  \quad
  \text{when visibility loss is unobserved}.
\end{align}
```

These formulas do not by themselves fix the numerical scales. They become predictions only when the physical sector supplies the fixed-point data, detector kernel, damping gap, basin metric, and admissibility tolerance. Their importance is that they identify where measurable departures from ideal wave or particle shadows should enter.

# Failure modes and domain of validity

The projection-duality theorem is conditional. It does not assert that every physical regime admits a clean coherent-sector description, nor that every proposed damping factor or detector kernel is admissible. This section records the main ways in which the construction can fail. Making these failure modes explicit is important: it prevents the theorem from becoming a catch-all interpretation and clarifies what must be checked in any concrete physical sector.

## Failure of coherent spectral isolation

The construction assumes an isolated coherent spectral cluster and a corresponding Riesz projector
``` math
\begin{equation}
  P
  =
  \frac{1}{2\pi i}
  \oint_\Gamma (z-A)^{-1}\,\mathrm{d}z.
\end{equation}
```
If the coherent cluster is not isolated, then the contour $`\Gamma`$ cannot be chosen without enclosing discarded spectrum. In that case the retained coherent sector is not sharply defined by the spectral data of $`A`$.

This can occur near gap closure, phase transitions, strong coupling, uncontrolled turbulence, horizon-like breakdowns, or measurement thresholds. In such regimes, the effective description may lose stable representability. The failure is not a small correction to the wave-particle duality theorem; it is a failure of the theorem’s hypotheses.

``` math
\begin{equation}
  \lambda_\ast\downarrow0
  \quad\Longrightarrow\quad
  \text{coherent-sector projection may cease to be stable}.
\end{equation}
```

## Divergent or undefined admissible proper time

The damping-selected time is
``` math
\begin{equation}
  \tau_{\mathrm{adm}}
  =
  \lambda_\ast^{-1}\log\frac{C_Q}{\epsilon_{\mathrm{adm}}}.
\end{equation}
```
This formula requires
``` math
\begin{equation}
  \lambda_\ast>0,
  \qquad
  0<\epsilon_{\mathrm{adm}}<1,
  \qquad
  C_Q\ge1.
\end{equation}
```
If $`\lambda_\ast=0`$, the discarded sector is not exponentially damped away from the coherent sector, and the required admissible time may diverge. If no meaningful basin tolerance $`\epsilon_{\mathrm{adm}}`$ exists, then $`\tau_{\mathrm{adm}}`$ is not determined by the damping criterion.

Thus the finite kernel is not guaranteed in every regime. It is selected only when the sector has a stable damping/admissibility structure.

## Failure of projector regularity

The smooth kernel statements require more than a bounded projector. They require $`P`$ to be a spectral/Riesz projector of $`A`$, or otherwise to preserve the relevant smooth domain. If $`P`$ is an arbitrary bounded projection that does not respect the spectral regularity of $`A`$, then
``` math
\begin{equation}
  P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P
\end{equation}
```
may not have the smooth kernel properties assumed in the local and spectral analysis.

This is why the theorem uses spectral projectors rather than arbitrary coherent labels.

## Failure of coherent phase evolution

Wave-like behavior requires a coherent phase generator
``` math
\begin{equation}
  H_{\rm coh}
\end{equation}
```
on the retained sector. If the retained sector does not support approximately unitary phase transport, then modal coherence may not persist long enough to generate interference.

Such failure may occur when:

1.  the retained sector is strongly open;

2.  phase coherence is rapidly lost to uncontrolled discarded modes;

3.  the effective Hamiltonian is not self-adjoint on the retained sector;

4.  the experiment probes beyond the coherent-sector validity regime.

In such cases the particle-like local shadow may remain meaningful while the wave-like interference shadow is suppressed or absent.

## Invalid branch-damping matrices

A proposed branch-damping rule
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab}
\end{equation}
```
is physically admissible only if the Schur map is completely positive and trace preserving. For finite branch bases this requires
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```
If these conditions fail, then the map may send valid density matrices to non-positive operators. Such a rule cannot represent a physical measurement or disturbance channel.

Similarly, a proposed exponential form
``` math
\begin{equation}
  D_{ab}=e^{-\tau\Lambda_{ab}}
\end{equation}
```
is automatically safe for all $`\tau\ge0`$ only under conditions such as conditional negative definiteness of $`\Lambda`$. Otherwise positivity must be checked directly.

## Unnormalized or leaky detector effects

The finite detector effects must satisfy
``` math
\begin{equation}
  \sum_i E_i=I_{\rm coh}
\end{equation}
```
or
``` math
\begin{equation}
  \int E_x\,\mathrm{d}x=I_{\rm coh}
\end{equation}
```
for a closed probability-conserving detector on the retained sector. If instead
``` math
\begin{equation}
  \sum_i E_i<I_{\rm coh},
\end{equation}
```
then the detector is open: probability leaks into unrecorded channels. This is not necessarily a contradiction, but the interpretation changes. One must then include the missing channels or explicitly work with conditional probabilities.

Thus finite detector kernels do not automatically give normalized measurements. Their POVM normalization is part of the measurement-context data.

## Over-resolved coherent width

The particle-like approximation is resolution-dependent. If the experimental probe reaches the coherent scale
``` math
\begin{equation}
  E_{\rm probe}\sim\Lambda_{\rm eff},
\end{equation}
```
or equivalently
``` math
\begin{equation}
  \ell_{\rm res}\sim\ell_{\rm coh},
\end{equation}
```
then the delta approximation can fail. In that regime the finite kernel should produce observable deviations from pointlike behavior, such as:

1.  softened short-distance response;

2.  finite-width detector effects;

3.  modified contact interactions;

4.  reduced ultraviolet sensitivity;

5.  departure from sharp localization assumptions.

This is not a failure of MTT. It is precisely where MTT predicts that the point-particle shadow should no longer be treated as exact.

## Device-context dependence

Different measurement devices define different contexts:
``` math
\begin{equation}
  \mathsf M_1\neq \mathsf M_2.
\end{equation}
```
They may have different branch bases, detector effects, damping matrices, and survivor-basin partitions. Therefore one cannot compare outcomes from different devices as if they were readings of the same context-free classical variable.

This is not a loophole. It is part of the theory’s content. But in applications it requires care: the measurement context must be specified before asking which branch basis is being damped or which basin partition is being sampled.

## Failure of basin capture

The basin-measure account of outcome probabilities assumes that post-disturbance trajectories are captured by survivor basins in finite effective time, at least almost surely relative to the relevant ensemble measure. If trajectories hover near basin boundaries, undergo chaotic switching, or fail to stabilize, then ordinary discrete outcome statistics may not apply without additional coarse-graining.

In such cases one may observe:

1.  metastability;

2.  threshold knees;

3.  switching noise;

4.  hysteresis;

5.  Zeno or anti-Zeno behavior;

6.  protocol dependence.

These are not outside MTT, but they are outside the simplest stable-basin theorem used in this paper.

## Domain of validity

The projection-duality theorem applies in regimes where:

1.  a coherent spectral sector is isolated;

2.  the discarded sector has a positive damping gap;

3.  the admissible proper-time scale is finite;

4.  the retained sector supports coherent phase evolution;

5.  detector effects form a valid POVM or a clearly specified open measurement;

6.  branch damping defines a completely positive trace-preserving channel;

7.  survivor-basin capture is well-defined for the measurement context.

Within this domain, wave-like interference and particle-like localization are not separate postulates. They follow from the same coherent projection architecture.

Outside this domain, the theorem does not apply directly. The failure mode itself then becomes physically meaningful: it indicates loss of coherent representability, gap closure, invalid measurement modeling, or transition into a boundary regime.

## Summary

The projection-duality account is not a universal slogan. It is a conditional structural result. Its strength comes from its explicit hypotheses. If the hypotheses hold, then the wave and particle descriptions are recovered as shadows of one finite coherent-sector excitation. If the hypotheses fail, the theory identifies why the simple wave-particle description breaks down.

``` math
\begin{equation}
  \boxed{
  \text{Projection duality is valid exactly where coherent projection, phase transport,
  and survivor-basin measurement are valid.}
  }
\end{equation}
```

# Conclusion

Wave–particle duality is usually presented as a primitive feature of quantum mechanics: microscopic systems propagate and interfere as waves, yet appear as localized particles when measured. Modal Triplet Theory reframes this duality as a projection phenomenon. The wave-like and particle-like descriptions are not two competing ontologies. They are two downstream shadows of one finite coherent-sector excitation.

The central object is the admissible coherent operator
``` math
\begin{equation}
  B_{\mathrm{adm}}
  =
  P\chi(A)e^{-\tau_{\mathrm{adm}}A}\chi(A)P.
\end{equation}
```
In its local representation,
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)=\langle x|B_{\mathrm{adm}}|y\rangle,
\end{equation}
```
this operator defines a finite source, response, or detector-amplitude kernel. When its width is below the resolution scale of the probing apparatus, it appears pointlike. In the sharp spectral/proper-time limit, it recovers the Dirac delta:
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)\longrightarrow\delta(x-y).
\end{equation}
```
This is the particle shadow.

In its spectral representation,
``` math
\begin{equation}
  K_{\mathrm{adm}}(x,y)
  =
  \sum_{n\in\mathrm{coh}}
  \chi(\lambda_n)^2e^{-\tau_{\mathrm{adm}}\lambda_n}
  \phi_n(x)\phi_n^\ast(y),
\end{equation}
```
the same operator selects retained coherent modes. When those modes are transported by a self-adjoint coherent phase generator $`H_{\rm coh}`$, their relative phases produce interference. This is the wave shadow.

Measurement connects these shadows. A measurement device is not a passive reader of a context-free classical property. It is a device-specific disturbance and stabilization context:
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
\end{equation}
```
Different devices can therefore define different branch bases, different finite detector effects, different damping matrices, and different survivor-basin partitions. The exact detector record is exact inside the measurement context because the device stabilizes one survivor basin.

The interference side is controlled by off-diagonal branch coherence. A measurement-induced damping map has the form
``` math
\begin{equation}
  \rho_{ab}\longmapsto D_{ab}^{(\mathsf M)}\rho_{ab},
\end{equation}
```
or
``` math
\begin{equation}
  \rho\longmapsto D^{(\mathsf M)}\circ\rho.
\end{equation}
```
For this to be physically admissible, $`D`$ must define a valid Schur channel:
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```
When
``` math
\begin{equation}
  D_{ab}\approx1,
\end{equation}
```
branch coherence survives and the wave-like shadow is visible. When
``` math
\begin{equation}
  D_{ab}\approx0,
\end{equation}
```
branch coherence is suppressed and the downstream description becomes particle-like.

The double-slit experiment then becomes transparent. With no which-way record stabilized, the two path branches remain coherent and the screen distribution contains the interference term. With a which-way device, the device introduces branch separation and damps the off-diagonal term. In a symmetric two-slit arrangement,
``` math
\begin{equation}
  V_{\rm MTT}
  =
  D_{12}V_0.
\end{equation}
```
Each individual screen event is localized by a finite detector effect, while the ensemble pattern reflects the survival or loss of branch coherence.

This paper also separates two issues that are often conflated. Basin-measure probabilities answer:
``` math
\begin{equation}
  \text{Which survivor basin is selected?}
\end{equation}
```
Branch damping answers:
``` math
\begin{equation}
  \text{How much interference remains between alternatives?}
\end{equation}
```
Thus Born frequencies and interference visibility are related but distinct layers of the MTT measurement architecture.

The resulting theorem is:
``` math
\begin{equation}
  \boxed{
  \text{wave--particle duality}
  =
  \text{projection duality}.
  }
\end{equation}
```
More explicitly,
``` math
\begin{equation}
  \boxed{
  \text{one finite coherent-sector excitation}
  \quad\Longrightarrow\quad
  \begin{cases}
  \text{local delta-like particle shadow},\\
  \text{spectral phase-coherent wave shadow},\\
  \text{finite measurement-selection shadow}.
  \end{cases}
  }
\end{equation}
```

The ordinary quantum descriptions are recovered in the appropriate limits. Standard wave mechanics is recovered when coherent phases are retained. Pointlike detection is recovered when finite detector effects are idealized by sharp projectors. Incoherent mixtures are recovered when branch coherences are strongly damped. Thus MTT does not reject the standard formalism; it supplies a deeper projection architecture explaining why the standard formalism has both wave-like and particle-like faces.

The remaining execution tasks are sector-specific. To turn the scaling relations into numerical predictions, one must derive or constrain:
``` math
\begin{equation}
  A,\quad P,\quad \chi,\quad \lambda_\ast,\quad C_Q,\quad \epsilon_{\mathrm{adm}},
\end{equation}
```
and, for each measurement context,
``` math
\begin{equation}
  A_{\mathsf M},\quad P_{\mathsf M},\quad \chi_{\mathsf M},\quad \tau_{\mathsf M},\quad
  \Lambda_{ab}^{(\mathsf M)},\quad \{E_i^{(\mathsf M)}\},\quad \mathfrak B_{\mathsf M}.
\end{equation}
```
Only then does the theory produce numerical predictions for finite-width deviations, visibility loss, detector-resolution effects, or threshold knees.

Nevertheless, the structural conclusion is already fixed. The quantum object is not forced to be either a wave or a particle. In MTT, both are downstream shadows of one finite coherent excitation, revealed differently by local probing, spectral phase evolution, and device-specific survivor-basin selection.

<div class="thebibliography">

20

M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press.

E. B. Davies, *Heat Kernels and Spectral Theory*, Cambridge University Press.

J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View*, Springer.

W. H. Zurek, Decoherence, einselection, and the quantum origins of the classical, *Reviews of Modern Physics* 75, 715–775.

M. Schlosshauer, *Decoherence and the Quantum-to-Classical Transition*, Springer.

N. Bohr, The quantum postulate and the recent development of atomic theory, *Nature* 121, 580–590.

D. Bohm, A suggested interpretation of the quantum theory in terms of hidden variables, *Physical Review* 85, 166–193.

R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals*, McGraw–Hill.

P. Nero, *Dirac Delta Functions as Singular Shadows of Admissible Projection*, MTT Delta–Projection sequence.

P. Nero, *Canonical Coherent Kernels from MTT Fixed-Point Data*, MTT Delta–Projection sequence.

P. Nero, *Deriving the MTT Coherence Scale from Fixed-Point Damping*, MTT Delta–Projection sequence.

I. J. Schoenberg, Metric spaces and positive definite functions, *Transactions of the American Mathematical Society* 44, 522–536.

B.-G. Englert, Fringe visibility and which-way information: An inequality, *Physical Review Letters* 77, 2154–2157.

R. A. Horn and C. R. Johnson, *Matrix Analysis*, Cambridge University Press.

V. Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press.

M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press.

J. Polchinski, *String Theory, Volumes 1 and 2*, Cambridge University Press.

P. Nero, *Inflationary Measures and the Born Rule as a Single Shadow–Bridge Problem*, MTT Shadow–Bridge sequence.

P. Nero, *Measurement as Disturbance and Stabilization in Modal Triplet Theory*, MTT Measurement sequence.

P. Nero, *Measurement Effects as Finite Survivor-Basin Kernels*, MTT Delta–Projection sequence.

</div>
