---
abstract: |
  Many of the central structures of modern physics appear in distinct formalisms: Dirac delta localization, spectral wave propagation, finite measurement records, gauge redundancy, scattering amplitudes, quantized spectra, entangled correlations, and geometric curvature. Modal Triplet Theory (MTT) suggests that these are not unrelated phenomena. They are downstream projection shadows of finite coherent admissibility.

  The central analytic object is the admissible coherent projection operator
  ``` math
  \begin{equation}
    B_{\rm adm}
    =
    P\chi(A)\mathrm e^{-\tau A}\chi(A)P,
  \end{equation}
  ```
  where $`A`$ is a sectoral stabilization or admissibility operator, $`P`$ is the coherent-sector projector, $`\chi(A)`$ is an admissible spectral window, and $`\tau`$ is the damping-selected proper-time/heat-time scale. In a local representation, the kernel
  ``` math
  \begin{equation}
    K_{\rm adm}(x,y)=\langle x|B_{\rm adm}|y\rangle
  \end{equation}
  ```
  is a finite source, response, or detector-amplitude kernel whose sharp limit recovers the Dirac delta. In a spectral representation, the same object is a weighted coherent modal structure,
  ``` math
  \begin{equation}
    K_{\rm adm}(x,y)
    =
    \sum_{n\in\mathrm{coh}}
    \chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}
    \phi_n(x)\phi_n^\ast(y),
  \end{equation}
  ```
  whose retained phases generate interference.

  This paper proposes that the same finite projection architecture also organizes scattering, gauge, electromagnetism, gravity, quantization, superposition, entanglement, and measurement. In flat spectral charts, $`e^{-\tau A}`$ produces Gaussian high-mode damping and finite propagator corrections. In gauge sectors, $`P`$ must be quotient-compatible, so finite filtering acts only on gauge-admissible physical content or through gauge-covariant operators. In gravity, the corresponding projector must be diffeomorphism-compatible, because geometry itself is the object whose local representatives must glue globally. In quantization, admissible spectra arise from Circle phase closure, Lens quotient consistency, and Nil survivor selection. In entanglement, joint coherent sectors need not factor into independent local sectors. In measurement, finite effects and survivor-basin stabilization replace primitive collapse by context-dependent projection and selection.

  The result is a structural unification theorem: local deltas, spectral waves, finite records, gauge representatives, geometric gluing, quantized survivor spectra, and entangled joint coherences are distinct shadows of one finite coherent projection architecture. The claim is not that all numerical sector data are already derived. Rather, the claim is that MTT identifies the common operator-theoretic mechanism by which these structures arise and specifies the sector-by-sector execution tasks needed for empirical closure.
author:
- Peter Nero
current_version: v2
date: April 2026
generated_from_main_tex_sha256: 2cda12ec30370284ca3ace1940298e95897058fbe2efae85ae6aca1275ced03b
paper_id: finite-coherent-projection-in-modal-triplet-theory-a-co-064c2edb
release_state: not_matched_to_zenodo
title: |
  Finite Coherent Projection in Modal Triplet Theory  
  A Common Architecture for Duality, Gauge, Gravity, Quantization, Entanglement, and Measurement
---

# Introduction

Wave–particle duality is usually presented as a foundational quantum puzzle. In one experimental context a system appears localized, producing discrete detector records. In another context the same system produces interference, phase coherence, and wave-like propagation. The standard lesson is that neither classical particles nor classical waves are adequate primitives.

This paper develops a sharper formulation of that lesson in Modal Triplet Theory (MTT). The central claim is not that a quantum object is sometimes a particle and sometimes a wave. The claim is that both particle-like localization and wave-like interference are downstream projection shadows of one finite coherent admissibility structure.

The analytic object is
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  \label{eq:intro-Badm}
\end{equation}
```
In earlier drafts this object was sometimes called a projection operator. We will use more precise language here. The map $`P`$ is the projector. The full operator $`B_{\rm adm}`$ is generally not idempotent and therefore will be called the finite coherent admissibility operator, or equivalently the admissible coherent filter.

The local kernel of $`B_{\rm adm}`$,
``` math
\begin{equation}
  K_{\rm adm}(x,y)=\langle x|B_{\rm adm}|y\rangle,
\end{equation}
```
gives a finite coherent response kernel. In the sharp limit this kernel becomes a Dirac delta:
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
\end{equation}
```
This is the particle shadow.

The spectral representation of the same operator,
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y),
  \qquad
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n},
  \label{eq:intro-spectral-kernel}
\end{equation}
```
gives retained coherent modes, phases, and interference. This is the wave shadow.

Thus the first guiding thesis is:
``` math
\begin{equation}
  \boxed{
  \text{particle and wave are local and spectral shadows of the same finite coherent kernel.}
  }
  \label{eq:intro-wave-particle-thesis}
\end{equation}
```

The rest of the paper shows that this duality is not isolated. Measurement records, scattering form factors, gauge quotienting, electromagnetic holonomy, gravitational gluing, quantized survivor labels, superposition, and entanglement all fit into the same finite coherent admissibility architecture.

## From abstract filter to geometric realization

The operator $`B_{\rm adm}`$ can be stated abstractly on a Hilbert space. However, the physically important realization used in this paper is geometric. In the fixed-point realization of MTT, the total space is modeled as a fibered ten-dimensional structure
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
  \label{eq:intro-M10}
\end{equation}
```
or, more generally, as an internal fiber product over a four-dimensional base.

Here $`Y^4`$ is the observed four-dimensional Lorentzian base, while $`X^6`$ is a compact Riemannian internal space. The internal sector carries bundle directions
``` math
\begin{equation}
  B_n\to Y^4,
  \qquad
  n=1,2,3,
\end{equation}
```
with compact fibers and nonnegative fiber Laplacians
``` math
\begin{equation}
  \Delta_{B_n(y)}\ge0.
\end{equation}
```
The default internal admissibility operator is
``` math
\begin{equation}
  A_{\rm int}(y)
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n(y)},
  \qquad
  \kappa_n>0.
  \label{eq:intro-Aint}
\end{equation}
```
This operator is positive and elliptic along the internal fibers.

The coherent projector is the joint fiber-harmonic projector
``` math
\begin{equation}
  P_{\rm coh}(y)
  =
  \Pi_{B_1}(y)\Pi_{B_2}(y)\Pi_{B_3}(y),
  \label{eq:intro-Pcoh}
\end{equation}
```
where
``` math
\begin{equation}
  \Pi_{B_n}(y):L^2(B_n|_y)\to\ker\Delta_{B_n(y)}
\end{equation}
```
is the fiberwise harmonic projector. Thus
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}(y)
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n(y)}.
  \label{eq:intro-joint-harmonic}
\end{equation}
```

In this realization, the finite coherent admissibility operator becomes
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
  \label{eq:intro-FP-Badm}
\end{equation}
```

Thus the abstract operator <a href="#eq:intro-Badm" data-reference-type="eqref" data-reference="eq:intro-Badm">[eq:intro-Badm]</a> has a concrete geometric meaning:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}
  =
  \text{finite coherent filtering over a compact internal fiber geometry}.
  }
\end{equation}
```

The coherent sector is therefore not a vague retained subspace. In the fixed-point realization, it is the joint fiber-harmonic sector.

## Why the Dirac delta is still central

The geometric formulation does not weaken the wave–particle result. It strengthens it.

In ordinary point-particle descriptions one often begins with a Dirac delta source,
``` math
\begin{equation}
  J(x)=q\delta(x-x_0).
\end{equation}
```
MTT reverses the explanatory order. The finite coherent kernel is the native object; the delta is the singular sharp limit:
``` math
\begin{equation}
  \delta(x-y)
  =
  \lim_{\rm sharp}K_{\rm adm}(x,y).
\end{equation}
```

In the FP realization, this finite kernel is not arbitrary smearing. It is generated by the positive internal admissibility operator $`A_{\rm int}`$, the joint harmonic projector $`P_{\rm coh}`$, the spectral window $`\chi(A_{\rm int})`$, and the finite damping scale $`\tau`$. Therefore:
``` math
\begin{equation}
  \boxed{
  \text{Dirac localization is the zero-width local shadow of finite coherent fiber support.}
  }
  \label{eq:intro-delta-shadow}
\end{equation}
```

This is the first major physical shadow of finite coherent admissibility.

## Why the wave shadow is equally central

The same finite kernel also has a spectral expansion. If
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
\end{equation}
```
then, in the commuting spectral case,
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```
The retained modes carry phase, recurrence, interference, and coherent transport.

In the FP realization, the eigenvalues $`\lambda_n`$ are tied to internal fiber spectra or their sectoral analogues. The zero modes define the coherent low-energy sector, while nonzero internal modes are damped by
``` math
\begin{equation}
  \mathrm e^{-\tau\lambda_n}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{wave behavior is the spectral phase-coherent shadow of the same finite kernel.}
  }
  \label{eq:intro-wave-shadow}
\end{equation}
```

The central duality may therefore be written as
``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility}
  \quad\longrightarrow\quad
  \begin{cases}
    \text{Dirac delta shadow},\\
    \text{spectral wave shadow}.
  \end{cases}
  }
  \label{eq:intro-duality-map}
\end{equation}
```

This is the physical entry point of the paper.

## The Lorentzian admissibility principle

A major source of confusion in finite-kernel theories is the temptation to write a Lorentzian damping factor of the form
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}.
\end{equation}
```
MTT does not take this as its fundamental Lorentzian construction.

The d’Alembertian $`\Box`$ is not a positive elliptic operator. A naive exponential of $`\Box`$ can introduce acausal behavior, ghost-like pathologies, or uncontrolled analytic continuation problems. The MTT admissibility principle is therefore:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  \quad
  \text{as the fundamental Lorentzian damping operator.}
  }
  \label{eq:intro-A-not-box}
\end{equation}
```

Instead, $`A`$ must be positive in the relevant admissibility sector. In the FP realization,
``` math
\begin{equation}
  A=A_{\rm int}
\end{equation}
```
is a positive fiber elliptic operator. In Cauchy-slice formulations, $`A`$ may be a positive spatial or Hamiltonian operator acting on a fixed time-slab or on constrained physical data. In gauge and gravitational sectors, $`A`$ must act only after quotienting or in a constraint-compatible way.

Thus the second guiding thesis is:
``` math
\begin{equation}
  \boxed{
  \text{MTT damping is positive fiber/spatial/Cauchy-slice damping, not naive Lorentzian }
  \mathrm e^{-\tau\Box}\text{ damping.}
  }
  \label{eq:intro-positive-damping}
\end{equation}
```

This is not a technical footnote. It is part of the physical architecture.

## Dimensional reduction and the KK-style reading

The FP realization has an honest Kaluza–Klein-style backbone. Compact internal fiber spectra produce zero modes and massive internal excitations. If
``` math
\begin{equation}
  A_{\rm int}\phi_n=\mu_n^2\phi_n,
\end{equation}
```
then the admissibility filter assigns internal weight
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_n^2}.
\end{equation}
```

After dimensional reduction, a schematic four-dimensional propagator has the form
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{n\ge0}
  \frac{Z_n\mathrm e^{-\tau\mu_n^2}}
  {p^2-m_n^2+\mathrm i\epsilon},
  \label{eq:intro-4D-propagator}
\end{equation}
```
where $`Z_n\ge0`$ in ghost-free positive-norm sectors.

The zero mode satisfies
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
so
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Therefore ordinary low-energy four-dimensional propagation is recovered at the zero-mode level. Finite coherent corrections enter through nonzero internal modes, threshold effects, loop corrections, detector profiles, or sector-specific form factors.

This point is important:
``` math
\begin{equation}
  \boxed{
  \text{the default FP/MTT damping acts on internal fiber momentum, not on the physical
  Lorentzian four-momentum of a zero mode.}
  }
  \label{eq:intro-fiber-not-base}
\end{equation}
```

Thus MTT is not a random nonlocal modification of four-dimensional quantum field theory. It is a projection-and-filter architecture over a fibered geometric structure.

The connection to Kaluza–Klein theory is therefore not a weakness. It is the geometric backbone that makes the framework concrete. The distinction is that MTT does not stop at the existence of extra modes. It organizes finite kernels, measurement records, damping, gauge quotienting, gravitational gluing, quantization, and entanglement under one projection architecture.

## Locality in total space and nonlocality as shadow

The geometric interpretation also clarifies the status of nonlocality.

MTT does not begin with arbitrary nonlocal influence in $`Y^4`$. It begins with finite coherent structure in the total fibered setting. When this structure is projected to the observed four-dimensional base, it may appear as a finite-width source, finite detector profile, form factor, or nonlocal-looking effective kernel.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional nonlocality is a projection shadow of controlled finite structure
  in the total/fibered space.}
  }
  \label{eq:intro-nonlocality-shadow}
\end{equation}
```

In Cauchy-slice formulations, finite kernels may be evaluated on equal-time spatial slices. When such kernels enter as lower-order bounded terms and do not change the principal hyperbolic symbol, the finite speed of propagation and domains of dependence remain those of the underlying local hyperbolic system. This gives the Lorentzian implementation a causal interpretation without invoking $`\mathrm e^{-\tau\Box}`$.

Thus MTT separates two notions that are often confused:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent support}
  \neq
  \text{acausal signal propagation}.
  }
\end{equation}
```

Finite support or finite overlap in an admissible projection context can produce non-pointlike effective shadows without violating relativistic causal propagation.

## Circle–Lens–Nil grammar

The interpretive grammar of MTT is the Modal Triplet:
``` math
\begin{equation}
  \mathsf C,\qquad \mathsf L,\qquad \mathsf N.
\end{equation}
```

Circle denotes phase, return, recurrence, spectral closure, and holonomy:
``` math
\begin{equation}
  \mathsf C:
  \quad
  \text{phase, loop, recurrence, spectral mode, coherent return}.
\end{equation}
```

Lens denotes projection, representation, quotienting, gauge choice, coordinate choice, and measurement context:
``` math
\begin{equation}
  \mathsf L:
  \quad
  \text{projection, representative, quotient, gauge, context}.
\end{equation}
```

Nil denotes damping, termination, branch selection, survivor basins, and discrete records:
``` math
\begin{equation}
  \mathsf N:
  \quad
  \text{damping, threshold, basin, record, survivor}.
\end{equation}
```

The finite coherent admissibility operator has the corresponding reading:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}
  =
  \mathsf C\text{-compatible}
  \;\mathsf L\text{-consistent}
  \;\mathsf N\text{-surviving}
  \text{ finite identity}.
  }
  \label{eq:intro-CLN-Badm}
\end{equation}
```

This grammar does not replace the mathematics. It explains why the same mathematical architecture appears in wave mechanics, measurement, gauge theory, gravity, quantization, and entanglement.

## What is unified

The unification proposed here is structural and conditional. It does not claim that all Standard Model parameters, masses, coupling constants, detector basin measures, or quantum-gravity sectors have already been derived. It claims that once a physical sector supplies admissible data
``` math
\begin{equation}
  A,\qquad P,\qquad \chi,\qquad \tau,
\end{equation}
```
and the relevant quotient, positivity, and measurement conditions are satisfied, the same finite coherent admissibility architecture produces multiple physical shadows.

The main shadows are:
``` math
\begin{align}
  \text{particle}
  &:=
  \text{local delta-limit shadow},
  \\
  \text{wave}
  &:=
  \text{spectral phase-coherent shadow},
  \\
  \text{measurement record}
  &:=
  \text{finite survivor-basin shadow},
  \\
  \text{scattering form factor}
  &:=
  \text{finite overlap or damped internal-mode shadow},
  \\
  \text{gauge}
  &:=
  \text{Lens quotient consistency},
  \\
  \text{electromagnetism}
  &:=
  \text{gauge Lens plus phase holonomy plus photon records},
  \\
  \text{gravity}
  &:=
  \text{diffeomorphism-compatible geometric gluing},
  \\
  \text{quantization}
  &:=
  \text{admissible survivor labels},
  \\
  \text{superposition}
  &:=
  \text{coherent branch coexistence before selection},
  \\
  \text{entanglement}
  &:=
  \text{non-factorizable coherent support in a joint sector}.
\end{align}
```

The central claim is therefore:
``` math
\begin{equation}
  \boxed{
  \text{many familiar physical structures are distinct projection shadows of finite coherent
  admissibility.}
  }
  \label{eq:intro-central-claim}
\end{equation}
```

## What the paper does not claim

The paper does not claim that every sector has already been numerically closed. In particular, it does not yet derive:

1.  the full Standard Model gauge group and matter representations from first principles;

2.  all particle masses and coupling constants;

3.  a complete nonperturbative quantum-gravity theory;

4.  exact collider bounds for every internal excitation;

5.  all detector basin measures;

6.  a full derivation of Born weights in every measurement context.

Those are execution tasks.

The result established here is more modest and more precise:
``` math
\begin{equation}
  \boxed{
  \text{MTT supplies a common finite admissibility architecture that sectoral theories must
  instantiate and test.}
  }
  \label{eq:intro-modest-claim}
\end{equation}
```

This distinction is important. The unification is structural; prediction requires sectoral execution.

## Outline of the paper

Section <a href="#sec:geometric-setup" data-reference-type="ref" data-reference="sec:geometric-setup">2</a> states the geometric setup, including the FP realization on $`M_{10}=Y^4\times X^6`$, compact internal fibers, nonnegative fiber Laplacians, and the joint fiber-harmonic coherent projector.

Section <a href="#sec:operator-setup" data-reference-type="ref" data-reference="sec:operator-setup">3</a> defines the finite coherent admissibility operator
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
and distinguishes the commuting spectral case from noncommuting sectoral projections.

Section <a href="#sec:cln-kernel" data-reference-type="ref" data-reference="sec:cln-kernel">4</a> gives the Circle–Lens–Nil interpretation of the operator.

Section <a href="#sec:delta-wave-measurement" data-reference-type="ref" data-reference="sec:delta-wave-measurement">5</a> develops the central wave–particle result: Dirac delta localization and spectral wave behavior are two shadows of the same finite coherent kernel.

Section <a href="#sec:scattering" data-reference-type="ref" data-reference="sec:scattering">6</a> treats scattering, finite propagators, Euclidean scalar kernels, fiber damping, and the distinction between internal-mode damping and naive Lorentzian damping.

Section <a href="#sec:cauchy-locality" data-reference-type="ref" data-reference="sec:cauchy-locality">7</a> explains the Lorentzian admissibility principle, Cauchy-slice finite kernels, and locality in total space versus nonlocality as a four-dimensional projection shadow.

Section <a href="#sec:gauge-em" data-reference-type="ref" data-reference="sec:gauge-em">8</a> applies the architecture to gauge theory and electromagnetism.

Section <a href="#sec:gravity" data-reference-type="ref" data-reference="sec:gravity">9</a> treats gravity as diffeomorphism-compatible geometric gluing and relates the admissibility operator to spatial/geometric data rather than to an indefinite spacetime d’Alembertian.

Section <a href="#sec:quantization" data-reference-type="ref" data-reference="sec:quantization">10</a> reframes quantization as the emergence of admissible survivor labels.

Section <a href="#sec:superposition-entanglement" data-reference-type="ref" data-reference="sec:superposition-entanglement">11</a> treats superposition and entanglement as coherent-sector and joint-sector structure.

Section <a href="#sec:unification-theorem" data-reference-type="ref" data-reference="sec:unification-theorem">12</a> separates the analytic filter theorem, the branch-channel theorem, the scalar benchmark theorem, and the structural unification corollary.

Section <a href="#sec:relation-existing" data-reference-type="ref" data-reference="sec:relation-existing">13</a> compares the framework to complementarity, decoherence, consistent histories, relational quantum mechanics, quantum field theory, gauge theory, Kaluza–Klein theory, string theory, loop/holonomy approaches, holography, and other structural programs.

Section <a href="#sec:phenomenology" data-reference-type="ref" data-reference="sec:phenomenology">14</a> states the phenomenological execution program, including the geometric origin of the coherence scale
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
and the relation
``` math
\begin{equation}
  \sqrt{\tau}
  \sim
  R\sqrt{\log(C_Q/\epsilon_{\rm adm})}
\end{equation}
```
when the internal spectral gap scales as $`\lambda_\ast\sim R^{-2}`$.

Section <a href="#sec:failure-modes" data-reference-type="ref" data-reference="sec:failure-modes">15</a> records the domain of validity and failure modes, including noncommuting projectors, invalid damping channels, gauge violation, diffeomorphism violation, and inadmissible Lorentzian operators.

Section <a href="#sec:conclusion" data-reference-type="ref" data-reference="sec:conclusion">16</a> summarizes the result:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility}
  \longrightarrow
  \text{projection shadows}
  \longrightarrow
  \text{effective physics}.
  }
\end{equation}
```

# Geometric setup and fixed-point realization

The introduction stated the finite coherent admissibility operator in abstract form,
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
This section gives the geometric realization that will be used as the default model throughout the paper.

The key point is that $`A`$ should not be thought of first as an arbitrary smoothing operator on four-dimensional spacetime. In the fixed-point realization of MTT, $`A`$ is naturally a positive internal or fiberwise operator. This turns the finite kernel from an ad hoc regulator into a geometric admissibility filter.

The geometric picture is:
``` math
\begin{equation}
  \boxed{
  M_{10}=Y^4\times X^6,
  }
\end{equation}
```
or, more generally, a compact internal fiber geometry over a four-dimensional Lorentzian base. The observed four-dimensional physics is a projection shadow of coherent admissible structure on the total/fibered space.

## The total space

Let
``` math
\begin{equation}
  M_{10}=Y^4\times X^6.
  \label{eq:M10-section2}
\end{equation}
```
Here $`Y^4`$ is the observed four-dimensional base and $`X^6`$ is a compact internal Riemannian space.

The base $`Y^4`$ is Lorentzian. It carries the macroscopic causal structure, time evolution, and the effective four-dimensional field description. The internal space $`X^6`$ is compact and Riemannian. It carries the fiber spectra, internal harmonics, and coherent admissibility structure.

Thus:
``` math
\begin{equation}
  \boxed{
  Y^4:
  \text{Lorentzian base},
  \qquad
  X^6:
  \text{compact Riemannian internal space}.
  }
\end{equation}
```

The product notation is a clean model. More generally, one may allow a fiber bundle
``` math
\begin{equation}
  \pi:M_{10}\to Y^4,
\end{equation}
```
with compact internal fiber
``` math
\begin{equation}
  X_y^6=\pi^{-1}(y)
\end{equation}
```
over each base point $`y\in Y^4`$. The product case is recovered when all fibers are canonically identified with one fixed compact space $`X^6`$.

The essential requirement is not strict product geometry. The essential requirement is that the internal directions carry positive elliptic operators with controlled spectra.

## Internal bundle directions

In the fixed-point realization, the internal space is organized into three compact bundle directions
``` math
\begin{equation}
  B_n\to Y^4,
  \qquad
  n=1,2,3.
  \label{eq:Bn-section2}
\end{equation}
```
Each $`B_n`$ has compact Riemannian fibers over the base. Let
``` math
\begin{equation}
  \Delta_{B_n(y)}
\end{equation}
```
denote the corresponding nonnegative fiber Laplacian over $`y\in Y^4`$.

The nonnegativity condition is
``` math
\begin{equation}
  \Delta_{B_n(y)}\ge0.
\end{equation}
```
This is crucial. The admissibility damping
``` math
\begin{equation}
  \mathrm e^{-\tau A}
\end{equation}
```
is well-defined as damping only when $`A`$ is positive in the relevant sector.

The internal admissibility operator is then modeled as
``` math
\begin{equation}
  A_{\rm int}(y)
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n(y)},
  \qquad
  \kappa_n>0.
  \label{eq:Aint-section2}
\end{equation}
```
Since each $`\Delta_{B_n(y)}`$ is nonnegative and each $`\kappa_n`$ is positive, one has
``` math
\begin{equation}
  A_{\rm int}(y)\ge0.
\end{equation}
```

Thus the default MTT damping operator is:
``` math
\begin{equation}
  \boxed{
  A=A_{\rm int},
  \qquad
  A_{\rm int}\ge0.
  }
\end{equation}
```

## The Hilbert bundle

At each base point $`y\in Y^4`$, let
``` math
\begin{equation}
  \mathcal H_{\rm int}(y)
\end{equation}
```
be the internal Hilbert space of square-integrable sections over the compact internal fiber. In the simplest product case,
``` math
\begin{equation}
  \mathcal H_{\rm int}(y)\cong L^2(X^6,E),
\end{equation}
```
where $`E`$ is the relevant internal bundle or representation space.

The full state space may be written schematically as
``` math
\begin{equation}
  \mathcal H
  =
  L^2\!\left(Y^4;\mathcal H_{\rm int}(y)\right),
  \label{eq:Hilbert-bundle-section2}
\end{equation}
```
with the understanding that Lorentzian time evolution on $`Y^4`$ must be treated by a Hamiltonian, Cauchy-slice, or covariant field-theoretic formulation rather than by an indefinite heat operator on spacetime.

For local Cauchy-slice discussions, one may instead write
``` math
\begin{equation}
  \mathcal H_\Sigma
  =
  L^2\!\left(\Sigma;\mathcal H_{\rm int}(x)\right),
\end{equation}
```
where $`\Sigma\subset Y^4`$ is a spacelike Cauchy slice.

Thus the internal Hilbert structure is fibered over the observed base:
``` math
\begin{equation}
  \boxed{
  \text{state}
  =
  \text{base dependence}
  +
  \text{internal coherent fiber data}.
  }
\end{equation}
```

## Fiber spectra

Because the internal fibers are compact Riemannian spaces, the fiber Laplacians have discrete nonnegative spectra. For each $`n`$,
``` math
\begin{equation}
  \Delta_{B_n(y)}\psi_{n,j}(y)
  =
  \lambda_{n,j}(y)\psi_{n,j}(y),
\end{equation}
```
with
``` math
\begin{equation}
  0=\lambda_{n,0}(y)
  \le
  \lambda_{n,1}(y)
  \le
  \lambda_{n,2}(y)
  \le
  \cdots.
\end{equation}
```

The zero eigenspace
``` math
\begin{equation}
  \ker\Delta_{B_n(y)}
\end{equation}
```
is the harmonic sector of the $`n`$-th fiber direction.

The first positive eigenvalue controls the gap between harmonic and non-harmonic internal content:
``` math
\begin{equation}
  \lambda_{n,1}(y)>0.
\end{equation}
```
A uniform spectral gap means there exists
``` math
\begin{equation}
  \lambda_\ast>0
\end{equation}
```
such that
``` math
\begin{equation}
  \lambda_{n,1}(y)\ge\lambda_\ast
\end{equation}
```
for all relevant $`n`$ and $`y`$.

This gap is the analytic source of finite admissibility damping.

## The coherent projector

Let
``` math
\begin{equation}
  \Pi_{B_n}(y):
  \mathcal H_{\rm int}(y)\to\ker\Delta_{B_n(y)}
\end{equation}
```
be the fiberwise harmonic projector. The joint coherent projector is
``` math
\begin{equation}
  P_{\rm coh}(y)
  =
  \Pi_{B_1}(y)\Pi_{B_2}(y)\Pi_{B_3}(y).
  \label{eq:Pcoh-section2}
\end{equation}
```
When the fiber projectors commute, this is itself an orthogonal projector.

Its range is the joint fiber-harmonic sector:
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}(y)
  =
  \bigcap_{n=1}^3
  \ker\Delta_{B_n(y)}.
  \label{eq:joint-harmonic-section2}
\end{equation}
```

This is the precise fixed-point meaning of the coherent sector:
``` math
\begin{equation}
  \boxed{
  \mathcal H_{\rm coh}
  =
  \operatorname{Ran}P_{\rm coh}
  =
  \text{joint fiber-harmonic sector}.
  }
  \label{eq:Hcoh-joint-harmonic}
\end{equation}
```

Thus the phrase “retained coherent content” is not merely interpretive. In the fixed-point realization it is a concrete spectral subspace: the joint kernel of the internal fiber Laplacians.

## The finite coherent admissibility operator

With
``` math
\begin{equation}
  A=A_{\rm int}
\end{equation}
```
and
``` math
\begin{equation}
  P=P_{\rm coh},
\end{equation}
```
the fixed-point realization of the MTT admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
  \label{eq:Badm-FP-section2}
\end{equation}
```

The factors have the following roles:
``` math
\begin{align}
  P_{\rm coh}
  &: \text{projection to the joint fiber-harmonic sector},\\
  \chi(A_{\rm int})
  &: \text{admissible spectral window},\\
  \mathrm e^{-\tau A_{\rm int}}
  &: \text{damping of noncoherent internal modes},\\
  \chi(A_{\rm int})
  &: \text{readmission to the admissible spectral band},\\
  P_{\rm coh}
  &: \text{return to the coherent sector}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  \text{finite coherent filtering over the internal fiber spectrum}.
  }
\end{equation}
```

The operator $`B_{\rm adm}^{\rm FP}`$ should not be called a projector unless it is idempotent in a particular limiting case. It is a positive admissibility filter built from a genuine projector $`P_{\rm coh}`$, a spectral window, and a finite damping factor.

## Commuting spectral case

The cleanest case occurs when
``` math
\begin{equation}
  [P_{\rm coh},A_{\rm int}]=0.
\end{equation}
```
This is the natural situation when $`P_{\rm coh}`$ is built from the spectral calculus of the same fiber operators that define $`A_{\rm int}`$.

Let
``` math
\begin{equation}
  A_{\rm int}\phi_j=\lambda_j\phi_j
\end{equation}
```
and
``` math
\begin{equation}
  P_{\rm coh}\phi_j=p_j\phi_j,
  \qquad
  p_j\in\{0,1\}.
\end{equation}
```
Then
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}\phi_j
  =
  p_j\chi(\lambda_j)^2\mathrm e^{-\tau\lambda_j}\phi_j.
  \label{eq:Badm-modal-action-section2}
\end{equation}
```
The admissible modal weight is
``` math
\begin{equation}
  w_j
  =
  p_j\chi(\lambda_j)^2\mathrm e^{-\tau\lambda_j}.
  \label{eq:modal-weight-section2}
\end{equation}
```

This is the spectral formula used repeatedly in the paper:
``` math
\begin{equation}
  \boxed{
  \text{mode survives}
  \quad\Longleftrightarrow\quad
  w_j
  \text{ remains nonzero or above threshold}.
  }
\end{equation}
```

## Noncommuting sectoral projectors

Not every physical sector has a projector that commutes with the chosen stabilization operator. In measurement contexts, gauge-fixed sectors, approximate effective descriptions, and gravitational projections, one may have
``` math
\begin{equation}
  [P,A]\neq0.
\end{equation}
```

In such cases the expression
``` math
\begin{equation}
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
may still be meaningful, but the diagonal modal formula
``` math
\begin{equation}
  w_j=p_j\chi(\lambda_j)^2\mathrm e^{-\tau\lambda_j}
\end{equation}
```
does not automatically apply.

Therefore the paper distinguishes two levels:

1.  the commuting spectral case, where the mode weights are diagonal and explicit;

2.  the noncommuting sectoral case, where admissibility must be checked by operator estimates, positivity, constraint preservation, and domain control.

This distinction is essential. It prevents the finite coherent admissibility operator from being mistaken for an arbitrary formal smoothing map.

## The damping scale

The finite damping time $`\tau`$ is selected by a leakage tolerance. Let
``` math
\begin{equation}
  Q=I-P_{\rm coh}
\end{equation}
```
be the discarded-sector projector. Suppose the discarded-sector flow satisfies an estimate
``` math
\begin{equation}
  \|Q\Phi_tQ\|
  \le
  C_Q\mathrm e^{-\lambda_\ast t},
  \label{eq:discarded-damping-section2}
\end{equation}
```
where
``` math
\begin{equation}
  \lambda_\ast>0
\end{equation}
```
is the uniform spectral gap. Given an admissibility tolerance
``` math
\begin{equation}
  0<\epsilon_{\rm adm}<1,
\end{equation}
```
one chooses $`\tau`$ so that
``` math
\begin{equation}
  C_Q\mathrm e^{-\lambda_\ast\tau}
  =
  \epsilon_{\rm adm}.
\end{equation}
```
Thus
``` math
\begin{equation}
  \boxed{
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
  }
  \label{eq:tau-gap-section2}
\end{equation}
```

This is the geometric origin of the coherence scale.

If the typical internal radius is $`R`$, then for Laplace-type fibers
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2}.
\end{equation}
```
Therefore
``` math
\begin{equation}
  \tau
  \sim
  R^2\log\frac{C_Q}{\epsilon_{\rm adm}},
  \label{eq:tau-R-section2}
\end{equation}
```
and
``` math
\begin{equation}
  \sqrt{\tau}
  \sim
  R
  \sqrt{\log\frac{C_Q}{\epsilon_{\rm adm}}}.
  \label{eq:sqrttau-R-section2}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \sqrt{\tau}
  =
  \text{internal coherent length scale}.
  }
\end{equation}
```

The paper will later use
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim\tau^{-1/2}
\end{equation}
```
as the corresponding effective energy scale.

## Zero modes and massive internal modes

The internal operator has zero modes and positive modes. If
``` math
\begin{equation}
  A_{\rm int}\phi_0=0,
\end{equation}
```
then
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_0=\phi_0.
\end{equation}
```
Thus zero modes are not damped by internal admissibility.

If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
  \qquad
  \mu_j^2>0,
\end{equation}
```
then
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
\end{equation}
```
Thus nonzero internal modes are suppressed.

After dimensional reduction, this gives the schematic four-dimensional tower
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
  \label{eq:4D-KK-tower-section2}
\end{equation}
```
The zero mode satisfies
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
so its admissibility weight is
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{ordinary low-energy four-dimensional fields are recovered as undamped zero-mode
  shadows.}
  }
\end{equation}
```

Finite coherent corrections enter through nonzero internal modes, finite detector kernels, threshold effects, or sector-specific form factors.

## Fiber damping versus Lorentzian damping

The distinction between internal damping and Lorentzian damping is central.

The FP/MTT default is
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}},
\end{equation}
```
where
``` math
\begin{equation}
  A_{\rm int}\ge0.
\end{equation}
```

It is not the naive Lorentzian expression
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}.
\end{equation}
```
The d’Alembertian $`\Box`$ is indefinite and is not a positive elliptic damping operator on Lorentzian spacetime.

Thus the fundamental Lorentzian admissibility principle is:
``` math
\begin{equation}
  \boxed{
  \text{MTT damping acts through positive fiber, positive spatial, or constraint-compatible
  operators, not through naive } \mathrm e^{-\tau\Box}.
  }
  \label{eq:no-naive-box-section2}
\end{equation}
```

This principle will be used later in the scattering, gauge, and gravity sections.

## Locality in the total space

The finite kernel should not be read as arbitrary four-dimensional nonlocality. In the geometric realization, finite coherent width arises from internal fiber structure.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional nonlocal-looking behavior can be a projection shadow of finite
  coherent structure in the total/fibered space.}
  }
\end{equation}
```

At the level of the observed base $`Y^4`$, one may see finite source profiles, finite detector effects, or form factors. At the level of the full fibered geometry, these are shadows of internal coherent admissibility.

This gives the conceptual rule:
``` math
\begin{equation}
  \boxed{
  \text{locality in the total admissible structure}
  \quad\longrightarrow\quad
  \text{finite non-pointlike shadows in four dimensions}.
  }
\end{equation}
```

This is why Dirac deltas are not taken as primitive. They are sharp limits of finite coherent kernels.

## Relation to Kaluza–Klein structure

The fixed-point realization has a Kaluza–Klein-style geometric backbone. Compact internal directions produce zero modes and massive internal excitations. This connection should be acknowledged directly.

However, MTT is not merely ordinary Kaluza–Klein theory with different terminology. The distinctive MTT structure is the combination of:

1.  finite coherent admissibility filtering;

2.  joint fiber-harmonic projection;

3.  damping-selected survivor sectors;

4.  Circle–Lens–Nil interpretation;

5.  measurement as finite effects plus survivor basins;

6.  gauge as quotient-compatible Lens projection;

7.  gravity as diffeomorphism-compatible geometric projection;

8.  quantization as admissible survivor labels;

9.  entanglement as non-factorizable coherent support.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is KK-compatible, but its central contribution is the finite coherent projection
  architecture across physical sectors.}
  }
\end{equation}
```

## Abstract sectoral generalization

Although the FP realization is the default geometric model, the formal architecture can be stated sectorally. A sector supplies:

1.  a Hilbert space or effective state space $`\mathcal H`$;

2.  a positive or sector-compatible admissibility operator $`A`$;

3.  an idempotent projector $`P`$ onto retained coherent or physical content;

4.  a spectral window $`\chi(A)`$;

5.  a damping scale $`\tau>0`$;

6.  additional quotient, measurement, or constraint data if required.

Then
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
is the finite coherent admissibility operator of that sector.

In scalar Euclidean benchmark cases,
``` math
\begin{equation}
  A=-\Delta.
\end{equation}
```
In the fixed-point internal realization,
``` math
\begin{equation}
  A=A_{\rm int}.
\end{equation}
```
In gauge sectors,
``` math
\begin{equation}
  A=A_{\rm gauge}
\end{equation}
```
must be quotient-compatible. In gravitational sectors,
``` math
\begin{equation}
  A=A_{\rm grav}
\end{equation}
```
must be diffeomorphism-compatible or constraint-compatible. In measurement sectors,
``` math
\begin{equation}
  A=A_{\mathsf M}
\end{equation}
```
is a detector-context stabilization operator.

Thus the abstract architecture is common, but the operator data are sectoral.

## What is not assumed

The geometric setup does not assume that all physics has already been derived from $`M_{10}=Y^4\times X^6`$. It does not by itself determine:

1.  the complete Standard Model representation content;

2.  all particle masses;

3.  all coupling constants;

4.  the exact internal geometry;

5.  the exact collider spectrum of internal modes;

6.  all measurement basin measures;

7.  a complete nonperturbative quantum-gravity sector.

Those are execution tasks.

What is assumed for this paper is more precise:
``` math
\begin{equation}
  \boxed{
  \text{there exists a sectoral positive admissibility operator and coherent projector from
  which finite projection shadows can be studied.}
  }
\end{equation}
```

The FP realization supplies a concrete and mathematically controlled version of that assumption.

## Summary

The default geometric realization of MTT is:
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
with $`Y^4`$ Lorentzian and $`X^6`$ compact Riemannian.

The internal admissibility operator is:
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```

The coherent projector is:
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
with
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
\end{equation}
```

The finite coherent admissibility operator is:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
  }
\end{equation}
```

The damping scale is set by the internal spectral gap:
``` math
\begin{equation}
  \boxed{
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
  }
\end{equation}
```

This geometric setup preserves the central duality:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent fiber kernel}
  \longrightarrow
  \begin{cases}
    \text{Dirac delta local shadow},\\
    \text{spectral wave shadow}.
  \end{cases}
  }
\end{equation}
```

It also fixes the Lorentzian interpretation:
``` math
\begin{equation}
  \boxed{
  \text{MTT damping is positive fiber/spatial/Cauchy-slice damping, not naive }
  \mathrm e^{-\tau\Box}\text{ damping}.
  }
\end{equation}
```

# The finite coherent admissibility operator

The previous section introduced the geometric setting in which MTT is realized as finite coherent admissibility over a compact internal fiber geometry. We now define the central operator in its general form and record the analytic assumptions under which it is used.

The basic object is
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  \label{eq:Badm-section3}
\end{equation}
```
This operator is not generally a projector. The map $`P`$ is the projector. The full operator $`B_{\rm adm}`$ is a finite coherent admissibility operator, or admissible coherent filter.

The purpose of $`B_{\rm adm}`$ is to retain the coherent sector, apply an admissible spectral window, damp inadmissible high or noncoherent modes, and return the result to the retained sector. It is the analytic engine behind the paper’s projection-shadow claims.

## Basic sectoral data

A sectoral MTT construction begins with the following data:
``` math
\begin{equation}
  (\mathcal H,A,P,\chi,\tau).
\end{equation}
```
Here $`\mathcal H`$ is a Hilbert space or effective state space,
``` math
\begin{equation}
  A:\mathcal D(A)\subset\mathcal H\to\mathcal H
\end{equation}
```
is a nonnegative self-adjoint or sector-compatible positive stabilization operator,
``` math
\begin{equation}
  P=P^\ast=P^2
\end{equation}
```
is an idempotent projector onto coherent or physical content,
``` math
\begin{equation}
  \chi(A)
\end{equation}
```
is a bounded spectral window, and
``` math
\begin{equation}
  \tau>0
\end{equation}
```
is the damping-selected admissibility scale.

The clean self-adjoint case assumes
``` math
\begin{equation}
  A\ge0,
\end{equation}
```
so that
``` math
\begin{equation}
  \mathrm e^{-\tau A}
\end{equation}
```
is a contraction:
``` math
\begin{equation}
  0\le \mathrm e^{-\tau A}\le I.
\end{equation}
```
If the spectral window satisfies
``` math
\begin{equation}
  0\le\chi(A)\le I,
\end{equation}
```
then
``` math
\begin{equation}
  \chi(A)\mathrm e^{-\tau A}\chi(A)
\end{equation}
```
is positive and bounded.

The finite coherent admissibility operator is then
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  }
\end{equation}
```

In the fixed-point realization,
``` math
\begin{equation}
  A=A_{\rm int},
  \qquad
  P=P_{\rm coh},
\end{equation}
```
where
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3\kappa_n\Delta_{B_n}
\end{equation}
```
is the positive internal fiber operator and
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3}
\end{equation}
```
is the joint fiber-harmonic projector.

## Why $`B_{\rm adm}`$ is not called a projector

A projector $`Q`$ satisfies
``` math
\begin{equation}
  Q^2=Q.
\end{equation}
```
Although $`P`$ is a projector, the full operator
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
does not generally satisfy
``` math
\begin{equation}
  B_{\rm adm}^2=B_{\rm adm}.
\end{equation}
```

Indeed, in a diagonal spectral basis one obtains eigenvalues
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```
Unless each $`w_n`$ is exactly $`0`$ or $`1`$, the corresponding operator is not idempotent.

Thus the precise terminology is:
``` math
\begin{equation}
  \boxed{
  P
  =
  \text{coherent projector},
  }
\end{equation}
```
while
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}
  =
  \text{finite coherent admissibility operator}.
  }
\end{equation}
```

This distinction matters because the physical claim is not that $`B_{\rm adm}`$ sharply projects once and for all. The physical claim is that $`B_{\rm adm}`$ filters finite coherent admissibility.

## Spectral calculus

Assume for the moment that $`A`$ is nonnegative and self-adjoint. By the spectral theorem,
``` math
\begin{equation}
  A
  =
  \int_0^\infty
  \lambda\,\,\mathrm dE_A(\lambda),
\end{equation}
```
where $`E_A`$ is the projection-valued spectral measure of $`A`$. For a bounded Borel function $`f`$,
``` math
\begin{equation}
  f(A)
  =
  \int_0^\infty
  f(\lambda)\,\,\mathrm dE_A(\lambda).
\end{equation}
```

Therefore
``` math
\begin{equation}
  \chi(A)
  =
  \int_0^\infty
  \chi(\lambda)\,\,\mathrm dE_A(\lambda),
\end{equation}
```
and
``` math
\begin{equation}
  \mathrm e^{-\tau A}
  =
  \int_0^\infty
  \mathrm e^{-\tau\lambda}\,\,\mathrm dE_A(\lambda).
\end{equation}
```

If $`P`$ is a spectral projector of $`A`$, or if $`P`$ commutes with $`A`$, then $`P`$ also commutes with $`\chi(A)`$ and $`\mathrm e^{-\tau A}`$. In that case the operator $`B_{\rm adm}`$ is a spectral multiplier on the retained sector.

This commuting spectral case is the cleanest analytic setting and is the default in the fiber-harmonic FP realization.

## Commuting case

Suppose
``` math
\begin{equation}
  [P,A]=0.
  \label{eq:P-commutes-A-section3}
\end{equation}
```
Let
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n
\end{equation}
```
and
``` math
\begin{equation}
  P\phi_n=p_n\phi_n,
  \qquad
  p_n\in\{0,1\}.
\end{equation}
```
Then
``` math
\begin{equation}
  \chi(A)\phi_n=\chi(\lambda_n)\phi_n,
\end{equation}
```
and
``` math
\begin{equation}
  \mathrm e^{-\tau A}\phi_n=\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```
Therefore
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
  \label{eq:Badm-action-section3}
\end{equation}
```

Define the admissible modal weight
``` math
\begin{equation}
  w_n
  :=
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
  \label{eq:weight-section3}
\end{equation}
```
Then
``` math
\begin{equation}
  B_{\rm adm}
  =
  \sum_n
  w_n|\phi_n\rangle\langle\phi_n|
  \label{eq:Badm-spectral-sum-section3}
\end{equation}
```
in the discrete spectral case.

The interpretation is direct:
``` math
\begin{align}
  p_n&=0
  &&\Rightarrow
  \text{mode outside coherent sector},\\
  \chi(\lambda_n)=0
  &&\Rightarrow
  \text{mode outside admissible spectral window},\\
  \mathrm e^{-\tau\lambda_n}\ll1
  &&\Rightarrow
  \text{mode strongly damped},\\
  w_n\approx1
  &&\Rightarrow
  \text{mode retained as coherent admissible content}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{coherent survivor mode}
  =
  \text{mode with nonzero or threshold-surviving admissible weight}.
  }
\end{equation}
```

## Noncommuting case

In more general sectors, the projector $`P`$ need not commute with $`A`$:
``` math
\begin{equation}
  [P,A]\neq0.
\end{equation}
```
This may occur for detector projections, approximate effective sectors, constrained gauge systems, or gravitational reductions.

Then the diagonal expression
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}
\end{equation}
```
is not generally valid. The operator
``` math
\begin{equation}
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
may still be bounded and physically meaningful, but its admissibility must be justified by operator estimates rather than by scalar spectral weights.

In the noncommuting case, one must check:

1.  domain preservation;

2.  positivity or complete positivity where relevant;

3.  boundedness on the intended Sobolev or Hilbert scale;

4.  compatibility with constraints;

5.  preservation of gauge or diffeomorphism equivalence;

6.  stability of the retained sector under the effective dynamics.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{commuting case}
  =
  \text{spectral multiplier};
  }
\end{equation}
```
whereas
``` math
\begin{equation}
  \boxed{
  \text{noncommuting case}
  =
  \text{sectoral admissibility problem}.
  }
\end{equation}
```

This distinction will be important in the gauge, gravity, and measurement sections.

## Positivity and boundedness

In the commuting self-adjoint setting, $`B_{\rm adm}`$ is positive. Indeed, if $`P`$ commutes with $`A`$, then
``` math
\begin{align}
  \langle f,B_{\rm adm}f\rangle
  &=
  \langle f,P\chi(A)\mathrm e^{-\tau A}\chi(A)P f\rangle\\
  &=
  \left\|
  \mathrm e^{-\tau A/2}\chi(A)Pf
  \right\|^2\\
  &\ge0.
\end{align}
```

If
``` math
\begin{equation}
  0\le\chi(A)\le I,
\end{equation}
```
and $`P`$ is an orthogonal projector, then
``` math
\begin{equation}
  \|B_{\rm adm}\|\le1.
\end{equation}
```

Therefore, in the clean spectral case,
``` math
\begin{equation}
  \boxed{
  0\le B_{\rm adm}\le I.
  }
\end{equation}
```

This inequality gives a precise sense in which $`B_{\rm adm}`$ is an admissibility filter: it does not amplify retained modes beyond the identity; it preserves, windows, and damps.

## Kernel representation

When $`B_{\rm adm}`$ admits an integral kernel, write
``` math
\begin{equation}
  K_{\rm adm}(x,y)=\langle x|B_{\rm adm}|y\rangle.
  \label{eq:Kadm-section3}
\end{equation}
```
Then
``` math
\begin{equation}
  (B_{\rm adm}f)(x)
  =
  \int
  K_{\rm adm}(x,y)f(y)\,\,\mathrm d\mu(y),
  \label{eq:kernel-action-section3}
\end{equation}
```
where $`\,\mathrm d\mu`$ is the relevant measure.

In a discrete spectral expansion,
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
  \label{eq:Kadm-spectral-section3}
\end{equation}
```

This equation is the source of both primary shadows.

The local reading fixes one argument:
``` math
\begin{equation}
  x\mapsto K_{\rm adm}(x,x_0).
\end{equation}
```
This is the finite coherent response to a localized source at $`x_0`$. In the sharp limit it becomes a delta response:
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
\end{equation}
```

The spectral reading uses the expansion
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y),
\end{equation}
```
which displays retained coherent modes and their phase relations.

Therefore:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}
  =
  \text{one finite kernel with a local delta shadow and a spectral wave shadow}.
  }
\end{equation}
```

## Sharp limit

The Dirac delta is recovered only in a controlled sharp limit. In the simplest case this means:
``` math
\begin{equation}
  P\to I,
  \qquad
  \chi(A)\to I,
  \qquad
  \tau\downarrow0.
  \label{eq:sharp-limit-section3}
\end{equation}
```
Then
``` math
\begin{equation}
  B_{\rm adm}\to I
\end{equation}
```
in the relevant strong or distributional sense, and the kernel of the identity is
``` math
\begin{equation}
  \delta(x-y).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \delta(x-y)
  =
  \text{identity-kernel shadow of the sharp admissibility limit}.
  }
\end{equation}
```

This is why MTT does not treat point particles or point sources as native primitive objects. They are idealized sharp shadows of finite coherent kernels.

## Finite-width regime

The physically important regime is usually not the exact sharp limit but the finite-width regime. The coherent width is
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau}.
  \label{eq:lcoh-section3}
\end{equation}
```
The corresponding energy scale is
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
  \label{eq:Lambdaeff-section3}
\end{equation}
```

If a probe has resolution length $`\ell_{\rm res}`$, then the finite kernel appears pointlike when
``` math
\begin{equation}
  \ell_{\rm coh}\ll\ell_{\rm res}.
\end{equation}
```
Equivalently, if the probe energy is $`E_{\rm probe}`$, the pointlike approximation holds when
``` math
\begin{equation}
  E_{\rm probe}\ll\Lambda_{\rm eff}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{pointlike}
  =
  \text{finite coherent support below experimental resolution}.
  }
\end{equation}
```

In the FP realization, $`\ell_{\rm coh}`$ is tied to the internal fiber scale through
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
and, for typical internal radius $`R`$,
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \sim
  R
  \sqrt{\log\frac{C_Q}{\epsilon_{\rm adm}}}.
\end{equation}
```

## Finite filter versus arbitrary regulator

It is important to distinguish the finite coherent admissibility operator from an arbitrary regulator.

An arbitrary regulator is imposed externally to tame divergences. By contrast, $`B_{\rm adm}`$ is intended to arise from sectoral admissibility data:
``` math
\begin{equation}
  A,\qquad P,\qquad \chi,\qquad \tau.
\end{equation}
```
In the FP realization, these data have geometric meaning:
``` math
\begin{equation}
  A=A_{\rm int},
  \qquad
  P=P_{\rm coh},
  \qquad
  \tau=\lambda_\ast^{-1}\log(C_Q/\epsilon_{\rm adm}).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent damping is not arbitrary smoothing;}
  }
\end{equation}
```
it is:
``` math
\begin{equation}
  \boxed{
  \text{damping generated by a positive admissibility operator and a coherent-sector
  projector}.
  }
\end{equation}
```

This distinction becomes essential in gauge and gravity sectors. A Gaussian-looking factor is not automatically admissible. It must preserve quotient consistency, constraints, positivity, and causal structure.

## Lorentzian admissibility

The operator $`A`$ in
``` math
\begin{equation}
  \mathrm e^{-\tau A}
\end{equation}
```
is required to be positive in the relevant admissibility sector.

Therefore, in Lorentzian field theory, MTT does not take
``` math
\begin{equation}
  A=\Box
\end{equation}
```
as the fundamental damping choice. The d’Alembertian is indefinite and does not generate a positive heat kernel in Lorentzian signature.

The admissible alternatives are:

1.  positive internal fiber operators such as $`A_{\rm int}`$;

2.  positive spatial elliptic operators on Cauchy slices;

3.  positive Hamiltonian or constraint-compatible operators;

4.  gauge-quotiented physical operators;

5.  diffeomorphism-compatible geometric operators;

6.  detector-context stabilization operators.

Thus the Lorentzian rule is:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  \quad
  \text{unless a positive physical-sector replacement has been defined.}
  }
\end{equation}
```

This principle is not optional. It is what prevents the finite kernel from becoming an uncontrolled nonlocal Lorentzian modification.

## Sectoral examples

The same formal architecture appears in several sectors.

#### FP internal sector.

``` math
\begin{equation}
  A=A_{\rm int},
  \qquad
  P=P_{\rm coh}.
\end{equation}
```
Here $`B_{\rm adm}`$ filters compact internal fiber modes.

#### Scalar Euclidean benchmark.

``` math
\begin{equation}
  A=-\Delta,
  \qquad
  P=I,
  \qquad
  \chi=1.
\end{equation}
```
Then $`B_{\rm adm}=e^{\tau\Delta}`$ and the kernel is Gaussian.

#### Gauge sector.

``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
\end{equation}
```
Here $`P_{\rm phys}`$ projects to gauge-admissible content.

#### Gravity sector.

``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
\end{equation}
```
Here $`P_{\rm diff}`$ projects to diffeomorphism-compatible geometric content.

#### Measurement sector.

``` math
\begin{equation}
  B_{\rm adm}^{\mathsf M}
  =
  P_{\mathsf M}\chi(A_{\mathsf M})
  \mathrm e^{-\tau_{\mathsf M}A_{\mathsf M}}
  \chi(A_{\mathsf M})P_{\mathsf M}.
\end{equation}
```
Here $`A_{\mathsf M}`$ and $`P_{\mathsf M}`$ are detector-context data.

The formal shape is common. The sectoral content differs.

## Projection shadows

A projection shadow is an effective physical structure obtained by reading $`B_{\rm adm}`$ through a particular representation, limit, quotient, or measurement context.

The most important shadows are:
``` math
\begin{align}
  \text{local kernel}
  &\Rightarrow
  \text{particle/delta shadow},
  \\
  \text{spectral expansion}
  &\Rightarrow
  \text{wave/interference shadow},
  \\
  \text{finite detector effects}
  &\Rightarrow
  \text{measurement-record shadow},
  \\
  \text{fiber-mode damping}
  &\Rightarrow
  \text{finite internal excitation shadow},
  \\
  \text{quotient-compatible projection}
  &\Rightarrow
  \text{gauge or diffeomorphism shadow},
  \\
  \text{joint coherent sector}
  &\Rightarrow
  \text{entanglement shadow}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{effective physics}
  =
  \text{finite coherent admissibility read through a projection context}.
  }
\end{equation}
```

## Summary

The central operator is
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  }
\end{equation}
```
It is not generally a projector. It is a finite coherent admissibility operator.

In the commuting spectral case,
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```
The modal weight is
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```

When a kernel exists,
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
\end{equation}
```
The same kernel has two primary shadows:
``` math
\begin{equation}
  \boxed{
  \text{local reading}
  \Rightarrow
  \text{Dirac delta / particle shadow},
  }
\end{equation}
```
and
``` math
\begin{equation}
  \boxed{
  \text{spectral reading}
  \Rightarrow
  \text{wave / interference shadow}.
  }
\end{equation}
```

In the FP realization,
``` math
\begin{equation}
  A=A_{\rm int},
  \qquad
  P=P_{\rm coh},
\end{equation}
```
so the finite admissibility operator is grounded in compact internal fiber geometry rather than arbitrary four-dimensional smearing.

The Lorentzian rule is:
``` math
\begin{equation}
  \boxed{
  \text{MTT damping uses positive fiber/spatial/constraint-compatible operators, not naive }
  \mathrm e^{-\tau\Box}.
  }
\end{equation}
```

# Circle–Lens–Nil reading of finite coherent kernels

The previous sections defined the geometric setting and the finite coherent admissibility operator
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
This section records the Modal Triplet interpretation of that operator. The purpose is not to replace the analytic construction with metaphor, but to identify the three structural roles played by the factors of $`B_{\rm adm}`$.

The triplet is
``` math
\begin{equation}
  \mathsf C,\qquad \mathsf L,\qquad \mathsf N.
\end{equation}
```
Circle denotes phase, recurrence, closure, spectral coherence, and holonomy. Lens denotes projection, representation, quotienting, context, gauge choice, and coordinate choice. Nil denotes damping, loss, thresholding, basin selection, and survivor records.

In this language,
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}
  =
  \mathsf C\text{-compatible}
  \;\mathsf L\text{-consistent}
  \;\mathsf N\text{-surviving}
  \text{ finite admissibility operator}.
  }
  \label{eq:cln-Badm-reading}
\end{equation}
```

This is the structural grammar that will later organize wave–particle duality, measurement, scattering, gauge theory, electromagnetism, gravity, quantization, superposition, and entanglement.

## Circle

Circle is the phase and return component of the theory. It appears whenever physical content is organized by coherent modes, periodicity, recurrence, spectral phase, holonomy, or closure conditions.

In a spectral representation,
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
\end{equation}
```
the retained modes
``` math
\begin{equation}
  \phi_n
\end{equation}
```
carry coherent phase structure. In ordinary wave mechanics this appears as
``` math
\begin{equation}
  \mathrm e^{\mathrm ik\cdot x},
\end{equation}
```
or, under time evolution,
``` math
\begin{equation}
  \mathrm e^{-\mathrm iE_nt}.
\end{equation}
```
In gauge theory it appears as electromagnetic phase and holonomy:
``` math
\begin{equation}
  \exp\left(\mathrm iq\oint_\gamma A\right).
\end{equation}
```
In gravity it appears as frame holonomy and curvature:
``` math
\begin{equation}
  [\nabla_\mu,\nabla_\nu]v^\rho
  =
  R^\rho{}_{\sigma\mu\nu}v^\sigma.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \mathsf C
  =
  \text{phase, recurrence, closure, spectral coherence, holonomy}.
  }
\end{equation}
```

In the finite coherent admissibility operator, Circle is represented by the spectral modes of $`A`$, together with the phase relations among retained modes. The modal expansion
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y)
  \label{eq:cln-spectral-kernel}
\end{equation}
```
is therefore the Circle-readable form of the kernel.

The wave shadow of MTT is a Circle shadow:
``` math
\begin{equation}
  \boxed{
  \text{wave}
  =
  \mathsf C\text{-coherent spectral shadow}.
  }
\end{equation}
```

## Lens

Lens is the projection and representation component of the theory. It appears whenever the same physical content can be read through different coordinate systems, bases, gauges, measurement contexts, or quotient representatives.

In the finite coherent admissibility operator, Lens appears first as the projector
``` math
\begin{equation}
  P.
\end{equation}
```
The projector selects the retained coherent or physical sector:
``` math
\begin{equation}
  P:\mathcal H\to\mathcal H_{\rm coh}.
\end{equation}
```

In the fixed-point realization,
``` math
\begin{equation}
  P=P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
and the retained sector is the joint fiber-harmonic sector:
``` math
\begin{equation}
  \mathcal H_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
\end{equation}
```

In gauge theory, Lens appears as quotienting:
``` math
\begin{equation}
  A_\mu\sim A_\mu+\partial_\mu\alpha.
\end{equation}
```
The local potential is a representative; the physical content is gauge-equivalence data.

In gravity, Lens appears as diffeomorphism redundancy:
``` math
\begin{equation}
  g_{\mu\nu}\sim\varphi^\ast g_{\mu\nu}.
\end{equation}
```
Coordinates are representatives; the physical content is diffeomorphism-compatible geometry.

In measurement, Lens appears as the chosen observable basis or detector context:
``` math
\begin{equation}
  \mathsf M=
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \mathsf L
  =
  \text{projection, representation, quotient, gauge, coordinate, context}.
  }
\end{equation}
```

The particle shadow also has a Lens aspect. The same finite kernel can be read locally, spectrally, through a detector, through a gauge quotient, or through a geometric projection. The observed physical shadow depends on the projection context.

## Nil

Nil is the damping, loss, threshold, and survivor component of the theory. It appears whenever some formal possibilities are suppressed, excluded, terminated, or stabilized into records.

In the finite coherent admissibility operator, Nil appears in the factor
``` math
\begin{equation}
  \mathrm e^{-\tau A}.
\end{equation}
```
If
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
\end{equation}
```
then
``` math
\begin{equation}
  \mathrm e^{-\tau A}\phi_n
  =
  \mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```
Modes with large $`\lambda_n`$ are suppressed. Modes in the coherent zero or low sector survive.

In the FP realization,
``` math
\begin{equation}
  A=A_{\rm int},
\end{equation}
```
so Nil damping acts on internal fiber excitations:
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_n
  =
  \mathrm e^{-\tau\mu_n^2}\phi_n.
\end{equation}
```
The zero mode is undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Nonzero internal modes are suppressed:
``` math
\begin{equation}
  \mu_n^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_n^2}<1.
\end{equation}
```

In measurement theory, Nil appears as branch damping:
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab},
\end{equation}
```
and as survivor-basin capture:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

In gravity, Nil appears as horizons, singularities, boundary conditions, topology selection, and survivor geometries.

Thus:
``` math
\begin{equation}
  \boxed{
  \mathsf N
  =
  \text{damping, threshold, termination, basin, survivor, record}.
  }
\end{equation}
```

## The triplet in $`B_{\rm adm}`$

The finite coherent admissibility operator has the form
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
Each factor has a triplet interpretation.

The projectors $`P`$ are Lens factors:
``` math
\begin{equation}
  P:
  \quad
  \mathsf L\text{-selection of coherent or physical content}.
\end{equation}
```

The spectral windows $`\chi(A)`$ are Lens–Nil factors:
``` math
\begin{equation}
  \chi(A):
  \quad
  \mathsf L\text{-selected admissible band}
  +
  \mathsf N\text{-exclusion of inadmissible modes}.
\end{equation}
```

The heat factor $`\mathrm e^{-\tau A}`$ is Nil damping:
``` math
\begin{equation}
  \mathrm e^{-\tau A}:
  \quad
  \mathsf N\text{-suppression of noncoherent spectral content}.
\end{equation}
```

The retained spectral modes and their phases are Circle:
``` math
\begin{equation}
  \phi_n,\quad \mathrm e^{\mathrm i\theta_n}:
  \quad
  \mathsf C\text{-coherent modal content}.
\end{equation}
```

Thus the whole operator can be read as:
``` math
\begin{equation}
  \boxed{
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
  =
  \mathsf L\text{-project}
  \to
  \mathsf L/\mathsf N\text{-window}
  \to
  \mathsf N\text{-damp}
  \to
  \mathsf L/\mathsf N\text{-readmit}
  \to
  \mathsf L\text{-return}.
  }
\end{equation}
```

Circle is carried by the coherent spectral content that survives this sequence.

## Circle–Lens–Nil in the fixed-point realization

In the fixed-point realization,
``` math
\begin{equation}
  A=A_{\rm int}
  =
  \sum_{n=1}^3\kappa_n\Delta_{B_n}.
\end{equation}
```
The triplet interpretation becomes concrete.

Circle is the harmonic and spectral coherence of the compact internal fibers:
``` math
\begin{equation}
  \mathsf C_{\rm FP}
  =
  \text{fiber-harmonic phases, internal spectral closure, coherent zero modes}.
\end{equation}
```

Lens is the projection onto the joint fiber-harmonic sector:
``` math
\begin{equation}
  \mathsf L_{\rm FP}
  =
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3}.
\end{equation}
```

Nil is the damping of nonzero internal modes:
``` math
\begin{equation}
  \mathsf N_{\rm FP}
  =
  \mathrm e^{-\tau A_{\rm int}}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  \text{fiber-Circle coherence}
  +
  \text{joint-harmonic Lens projection}
  +
  \text{internal-mode Nil damping}.
  }
\end{equation}
```

This gives the MTT triplet a concrete geometric backbone.

## The local shadow

When $`B_{\rm adm}`$ has a kernel,
``` math
\begin{equation}
  K_{\rm adm}(x,y)=\langle x|B_{\rm adm}|y\rangle,
\end{equation}
```
one may read it locally. Fixing a source point $`y=x_0`$, the section
``` math
\begin{equation}
  x\mapsto K_{\rm adm}(x,x_0)
\end{equation}
```
is a finite coherent response to a localized input.

In the sharp limit,
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
\end{equation}
```
Therefore:
``` math
\begin{equation}
  \boxed{
  \text{Dirac delta}
  =
  \text{sharp local Lens shadow of finite coherent admissibility}.
  }
\end{equation}
```

The point particle is not a primitive object in this reading. It is the result of taking a finite coherent kernel below resolution:
``` math
\begin{equation}
  \ell_{\rm coh}\ll\ell_{\rm res}.
\end{equation}
```

Thus particle-like localization is a Nil/Lens shadow:
``` math
\begin{equation}
  \boxed{
  \text{particle shadow}
  =
  \mathsf L\text{-localized}
  \;\mathsf N\text{-surviving}
  \text{ finite kernel event}.
  }
\end{equation}
```

## The spectral shadow

The same kernel also has a spectral reading:
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
\end{equation}
```
This expression displays retained modes and their coherent phase relations. When those relative phases contribute to probabilities, interference appears.

For a density matrix $`\rho`$ and effect $`E`$,
``` math
\begin{equation}
  \operatorname{tr}(\rho E)
  =
  \sum_a\rho_{aa}E_{aa}
  +
  \sum_{a\neq b}\rho_{ab}E_{ba}.
\end{equation}
```
The off-diagonal terms are Circle-coherent interference terms.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{wave shadow}
  =
  \mathsf C\text{-coherent spectral reading of the same finite kernel}.
  }
\end{equation}
```

Thus wave and particle are not separate substances. They are two projection shadows:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}
  \quad
  \begin{cases}
  \text{local Lens/Nil reading}
  &\Rightarrow
  \text{particle shadow},\\
  \text{spectral Circle reading}
  &\Rightarrow
  \text{wave shadow}.
  \end{cases}
  }
\end{equation}
```

## Measurement as triplet interaction

Measurement uses all three triplet components.

A measurement context
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\}_{i\in I},\mathfrak B_{\mathsf M})
\end{equation}
```
chooses a Lens decomposition:
``` math
\begin{equation}
  P_{\mathsf M},\quad \{E_i^{(\mathsf M)}\}.
\end{equation}
```

It may preserve or suppress Circle coherence:
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}^{(\mathsf M)}\rho_{ab}.
\end{equation}
```

It stabilizes a Nil survivor record:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{measurement}
  =
  \mathsf L\text{-context}
  +
  \mathsf C\text{-coherence preservation or loss}
  +
  \mathsf N\text{-survivor record}.
  }
\end{equation}
```

This reading will be developed in the next section.

## Gauge as Lens with Circle holonomy

Gauge theory is mainly Lens structure. A gauge potential is a local representative:
``` math
\begin{equation}
  A_\mu\sim A_\mu+\partial_\mu\alpha.
\end{equation}
```
The physical content is obtained after quotienting.

However, gauge theory also contains Circle structure. A charged system transported around a loop may acquire the holonomy
``` math
\begin{equation}
  \exp\left(\mathrm iq\oint_\gamma A\right).
\end{equation}
```

Nil appears through admissible charge sectors, photon records, detector events, and damping of nonphysical or noncoherent modes.

Thus:
``` math
\begin{align}
  \mathsf L_{\rm gauge}
  &: \text{gauge quotient},\\
  \mathsf C_{\rm gauge}
  &: \text{phase and holonomy},\\
  \mathsf N_{\rm gauge}
  &: \text{charge sectors and photon records}.
\end{align}
```

This will later require a gauge-compatible admissibility operator:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
\end{equation}
```

## Gravity as Lens-on-locality

Gravity is the deepest Lens sector because the redundancy acts on the representation of locality itself:
``` math
\begin{equation}
  g_{\mu\nu}\sim\varphi^\ast g_{\mu\nu}.
\end{equation}
```

Circle appears as curvature and frame holonomy:
``` math
\begin{equation}
  [\nabla_\mu,\nabla_\nu]v^\rho
  =
  R^\rho{}_{\sigma\mu\nu}v^\sigma.
\end{equation}
```

Nil appears as horizons, singularities, boundaries, and survivor geometries.

Thus:
``` math
\begin{align}
  \mathsf L_{\rm grav}
  &: \text{diffeomorphism quotient and chart gluing},\\
  \mathsf C_{\rm grav}
  &: \text{curvature and frame holonomy},\\
  \mathsf N_{\rm grav}
  &: \text{boundary, horizon, singularity, survivor geometry}.
\end{align}
```

A gravitational admissibility operator must therefore have the schematic form
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff},
\end{equation}
```
where $`A_{\rm grav}`$ is positive or constraint-compatible on geometric data and is not the naive Lorentzian d’Alembertian.

## Quantization as triplet closure

Quantization also has a triplet reading.

Circle gives phase closure:
``` math
\begin{equation}
  \psi(\theta+2\pi)=\psi(\theta)
  \quad\Rightarrow\quad
  n\in\mathbb Z.
\end{equation}
```

Lens gives quotient and representation consistency:
``` math
\begin{equation}
  \frac{1}{2\pi}\int_\Sigma F\in\mathbb Z.
\end{equation}
```

Nil gives survivor labels:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{quantization}
  =
  \mathsf C\text{-closure}
  +
  \mathsf L\text{-quotient consistency}
  +
  \mathsf N\text{-survivor selection}.
  }
\end{equation}
```

In the FP realization, compact internal spectra provide an additional geometric source of discrete labels:
``` math
\begin{equation}
  A_{\rm int}\phi_n=\mu_n^2\phi_n.
\end{equation}
```

## Entanglement as non-factorizing triplet structure

For a composite system,
``` math
\begin{equation}
  \mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B
\end{equation}
```
may be only a kinematic starting point. The admissible coherent sector may fail to factor:
``` math
\begin{equation}
  P_{AB}\neq P_A\otimes P_B,
\end{equation}
```
or
``` math
\begin{equation}
  B_{AB}\neq B_A\otimes B_B.
\end{equation}
```

In triplet terms:
``` math
\begin{align}
  \mathsf C&: \text{joint phase coherence},\\
  \mathsf L&: \text{subsystem decomposition and projection context},\\
  \mathsf N&: \text{joint or correlated survivor records}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{entanglement}
  =
  \text{non-factorizable coherent admissibility across a joint Lens decomposition}.
  }
\end{equation}
```

## Manifest covariance as Lens

The Lorentzian implementation of MTT often requires a Cauchy-slice or Hamiltonian description. Such descriptions may not be manifestly Lorentz covariant at every intermediate step. This should be understood as a Lens feature, not as a physical violation of relativity.

Gauge theory provides the analogy. Coulomb gauge is not manifestly Lorentz covariant, yet it can isolate physical transverse degrees of freedom. The loss of manifest covariance in the representative does not by itself imply a loss of physical covariance.

Similarly, a Cauchy-slice finite kernel may select a Lens representation adapted to a time foliation. The physical requirement is not manifest covariance of every intermediate formula. The physical requirements are:

1.  preservation of the hyperbolic principal symbol;

2.  finite propagation speed;

3.  compatibility with constraints;

4.  foliation-independent or consistently transformed observable content.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{manifest covariance is a representation property;}
  }
\end{equation}
```
whereas
``` math
\begin{equation}
  \boxed{
  \text{physical covariance is an observable and constraint-level requirement}.
  }
\end{equation}
```

This distinction is part of the Lens grammar.

## Triplet failure modes

The Circle–Lens–Nil reading also identifies failure modes.

Circle failure occurs when the claimed coherent phase structure is not actually preserved:
``` math
\begin{equation}
  \rho_{ab}\to0
  \qquad
  (a\neq b).
\end{equation}
```

Lens failure occurs when the projection context is invalid:
``` math
\begin{equation}
  P
  \text{ does not select a physical or admissible sector}.
\end{equation}
```
In gauge theory this means quotient failure. In gravity it means diffeomorphism or constraint failure.

Nil failure occurs when damping is not physically admissible:
``` math
\begin{equation}
  \rho\mapsto D\circ\rho
\end{equation}
```
but
``` math
\begin{equation}
  D\nsucceq0.
\end{equation}
```
It also occurs when no survivor basin stabilizes.

Thus the triplet grammar is not decorative. It tells us what must be checked:
``` math
\begin{equation}
  \boxed{
  \mathsf C:
  \text{coherence},
  \qquad
  \mathsf L:
  \text{valid projection},
  \qquad
  \mathsf N:
  \text{admissible damping and survivor selection}.
  }
\end{equation}
```

## Summary

The finite coherent admissibility operator
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
has a natural Circle–Lens–Nil reading.

Circle is the coherent spectral and phase content:
``` math
\begin{equation}
  \mathsf C
  =
  \text{phase, return, closure, holonomy, spectral coherence}.
\end{equation}
```

Lens is the projection and representation structure:
``` math
\begin{equation}
  \mathsf L
  =
  \text{projector, quotient, gauge, coordinate, measurement context}.
\end{equation}
```

Nil is the damping and survivor structure:
``` math
\begin{equation}
  \mathsf N
  =
  \text{damping, threshold, basin, record, survivor}.
\end{equation}
```

In the fixed-point realization:
``` math
\begin{equation}
  \mathsf C
  =
  \text{fiber spectral coherence},
\end{equation}
```
``` math
\begin{equation}
  \mathsf L
  =
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
and
``` math
\begin{equation}
  \mathsf N
  =
  \mathrm e^{-\tau A_{\rm int}}.
\end{equation}
```

The first and most important physical application is wave–particle projection duality:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}
  \quad
  \begin{cases}
  \text{local Lens/Nil reading}
  &\Rightarrow
  \text{Dirac delta / particle shadow},\\
  \text{spectral Circle reading}
  &\Rightarrow
  \text{wave / interference shadow}.
  \end{cases}
  }
\end{equation}
```

The next section develops this result in detail.

# Delta, wave, and measurement shadows

The previous section gave the Circle–Lens–Nil reading of the finite coherent admissibility operator
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
This section develops the first physical consequence in detail: particle-like localization, wave-like interference, and measurement records are three downstream shadows of the same finite coherent kernel.

The result is not that a quantum object is sometimes literally a point particle and sometimes literally a wave. The result is:
``` math
\begin{equation}
  \boxed{
  \text{particle, wave, and measurement record are three projection shadows of finite coherent admissibility.}
  }
  \label{eq:delta-wave-measurement-thesis}
\end{equation}
```

The particle shadow comes from the local kernel and its sharp Dirac-delta limit. The wave shadow comes from the spectral expansion and its retained phase coherence. The measurement shadow comes from finite effects, branch damping, and survivor-basin stabilization.

In the fixed-point realization, these shadows are grounded in the internal/fiber geometry. The native object is not an ideal point in four-dimensional spacetime. The native object is finite coherent admissibility over a compact internal/fiber structure, projected into the observed four-dimensional base.

## The finite coherent kernel

Assume first that $`B_{\rm adm}`$ admits a kernel:
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \langle x|B_{\rm adm}|y\rangle.
  \label{eq:Kadm-section5}
\end{equation}
```
Here $`x,y`$ denote the variables of the representation being used. In a purely four-dimensional effective reading, $`x,y\in Y^4`$ or on a Cauchy slice $`\Sigma\subset Y^4`$. In the full fibered reading, the variables may include internal/fiber coordinates or may represent a fiber-projected effective kernel on the base.

The kernel acts by
``` math
\begin{equation}
  (B_{\rm adm}f)(x)
  =
  \int
  K_{\rm adm}(x,y)f(y)\,\,\mathrm d\mu(y).
  \label{eq:kernel-action-section5}
\end{equation}
```

The two primary readings are:
``` math
\begin{align}
  \text{local reading}
  &: \quad
  x\mapsto K_{\rm adm}(x,x_0),
  \\
  \text{spectral reading}
  &: \quad
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
\end{align}
```

The local reading gives the particle/delta shadow. The spectral reading gives the wave shadow.

In the fixed-point realization,
``` math
\begin{equation}
  B_{\rm adm}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
\end{equation}
```
Thus the finite kernel is generated by:

1.  the joint fiber-harmonic coherent projector $`P_{\rm coh}`$;

2.  the positive internal admissibility operator $`A_{\rm int}`$;

3.  the spectral window $`\chi(A_{\rm int})`$;

4.  the finite damping scale $`\tau`$.

Therefore:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}
  =
  \text{finite coherent response kernel generated by internal/fiber admissibility}.
  }
  \label{eq:finite-kernel-generated-by-fiber}
\end{equation}
```

## Particle shadow

A point particle in ordinary idealized language is represented by a Dirac delta:
``` math
\begin{equation}
  x\longmapsto \delta(x-x_0).
\end{equation}
```
This is a zero-width object. It is not square-integrable and is not a finite physical profile.

MTT reverses the explanatory order. The finite coherent kernel section
``` math
\begin{equation}
  x\longmapsto K_{\rm adm}(x,x_0)
  \label{eq:finite-kernel-section}
\end{equation}
```
is the native admissible object. The Dirac delta is recovered only as a sharp limit:
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
  \label{eq:delta-limit-section5}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{particle}
  =
  \text{local Dirac-delta shadow of finite coherent support}.
  }
  \label{eq:particle-shadow-box-section5}
\end{equation}
```

This does not mean that a particle is a tiny classical ball. The kernel section $`K_{\rm adm}(x,x_0)`$ is a finite coherent response profile. Depending on the sector, it may be a source kernel, amplitude kernel, detector kernel, or effective local response.

A positive detection probability requires a positive effect. For example, a finite position-sensitive detector may use
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
  \qquad
  k_x(y)=K_{\rm det}(y,x).
  \label{eq:finite-position-effect-section5}
\end{equation}
```
The detector event is then localized by the finite width of $`k_x`$, not by a primitive mathematical point.

## Resolution-relative pointlikeness

Pointlikeness is resolution-relative. Let
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau}
\end{equation}
```
be the coherent width of the finite kernel, and let
``` math
\begin{equation}
  \ell_{\rm res}
\end{equation}
```
be the detector or probe resolution.

The system appears pointlike when
``` math
\begin{equation}
  \ell_{\rm coh}\ll\ell_{\rm res}.
  \label{eq:pointlike-resolution-section5}
\end{equation}
```
Equivalently, with
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim\tau^{-1/2},
\end{equation}
```
the pointlike approximation holds when
``` math
\begin{equation}
  E_{\rm probe}\ll\Lambda_{\rm eff}.
  \label{eq:pointlike-energy-section5}
\end{equation}
```

In the fixed-point realization, the coherent width is tied to the internal spectral gap:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
  \label{eq:tau-section5}
\end{equation}
```
If the typical internal radius is $`R`$, then
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2},
\end{equation}
```
so
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \sim
  R
  \sqrt{\log\frac{C_Q}{\epsilon_{\rm adm}}}.
  \label{eq:lcoh-R-section5}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{pointlike behavior in four dimensions is the below-resolution shadow of finite internal coherent width}.
  }
  \label{eq:pointlike-fiber-shadow}
\end{equation}
```

This is why high-resolution scattering may probe finite coherent structure, while low-energy experiments see ordinary pointlike behavior.

## The Dirac delta as a sharp shadow

The sharp delta limit requires a controlled limiting procedure. In the simplest spectral form, one takes
``` math
\begin{equation}
  P\to I,
  \qquad
  \chi(A)\to I,
  \qquad
  \tau\downarrow0.
  \label{eq:sharp-limit-section5}
\end{equation}
```
Then
``` math
\begin{equation}
  B_{\rm adm}\to I,
\end{equation}
```
and the kernel of the identity is the Dirac delta:
``` math
\begin{equation}
  I(x,y)=\delta(x-y).
\end{equation}
```

In flat Euclidean space, the benchmark example is
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(-\frac{|x-y|^2}{4\tau}\right).
  \label{eq:flat-heat-kernel-section5}
\end{equation}
```
As $`\tau\downarrow0`$,
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  \to
  \delta^{(d)}(x-y)
\end{equation}
```
distributionally.

But in the FP realization the primary damping is not a naive four-dimensional Lorentzian smearing. The clean physical interpretation is internal/fiber damping:
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}},
\end{equation}
```
with the four-dimensional pointlike shadow emerging after projection and dimensional reduction.

Therefore:
``` math
\begin{equation}
  \boxed{
  \delta
  =
  \text{sharp local shadow, not the native object}.
  }
  \label{eq:delta-shadow-not-native-section5}
\end{equation}
```

## Wave shadow

The same kernel has a spectral representation. In the commuting spectral case,
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
\end{equation}
```
and
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  w_n\phi_n,
  \qquad
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```
Then
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
  \label{eq:wave-shadow-spectral-section5}
\end{equation}
```

This expansion is the wave side of the same finite object. It displays:

1.  which modes survive;

2.  which modes are windowed out;

3.  which modes are damped;

4.  which phase relations remain coherent.

In the FP realization, if
``` math
\begin{equation}
  A_{\rm int}\phi_n=\mu_n^2\phi_n,
\end{equation}
```
then the internal modal weights include
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_n^2}.
\end{equation}
```
The zero mode satisfies
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
and is undamped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Nonzero internal modes are suppressed:
``` math
\begin{equation}
  \mu_n^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_n^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{wave}
  =
  \text{spectral phase-coherent shadow of finite coherent admissibility}.
  }
  \label{eq:wave-shadow-box-section5}
\end{equation}
```

## Off-diagonal coherence

Wave-like behavior is operationally visible through off-diagonal coherence. Let
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_a c_a|a\rangle
\end{equation}
```
be a coherent branch state in a chosen Lens context. Its density matrix is
``` math
\begin{equation}
  \rho
  =
  |\psi\rangle\langle\psi|
  =
  \sum_{a,b}
  c_a c_b^\ast
  |a\rangle\langle b|.
\end{equation}
```

The diagonal terms
``` math
\begin{equation}
  \rho_{aa}=|c_a|^2
\end{equation}
```
are branch weights. The off-diagonal terms
``` math
\begin{equation}
  \rho_{ab}=c_a c_b^\ast,
  \qquad
  a\neq b,
\end{equation}
```
carry relative phase coherence.

For an effect $`E`$,
``` math
\begin{equation}
  \operatorname{tr}(\rho E)
  =
  \sum_a\rho_{aa}E_{aa}
  +
  \sum_{a\neq b}\rho_{ab}E_{ba}.
  \label{eq:trace-interference-section5}
\end{equation}
```
The second term is the interference contribution.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{interference}
  =
  \text{observable contribution of off-diagonal coherent-sector terms}.
  }
  \label{eq:interference-offdiagonal-section5}
\end{equation}
```

When the off-diagonal terms survive, the wave shadow is visible. When they are damped, the downstream description becomes particle-like or mixture-like relative to the measurement context.

## The common-source duality

The particle and wave readings are not two different underlying objects. They are two representations of the same finite coherent kernel:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}(x,y)
  \quad
  \begin{cases}
    \text{local reading}
    &\Rightarrow
    \text{Dirac delta / particle shadow},
    \\
    \text{spectral reading}
    &\Rightarrow
    \text{phase-coherent wave shadow}.
  \end{cases}
  }
  \label{eq:common-source-duality-section5}
\end{equation}
```

This is the core wave–particle projection-duality claim.

In the FP realization, the common source is not merely formal. It is the finite coherent admissibility structure generated by the internal/fiber operator:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{wave--particle duality}
  =
  \text{two shadows of one finite coherent fiber-generated admissibility kernel}.
  }
  \label{eq:wave-particle-FP-section5}
\end{equation}
```

This is the central physical result of the paper.

## Measurement shadow

Measurement introduces a detector context. In MTT a measurement is not merely the selection of an abstract observable. It is a finite physical projection context:
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\}_{i\in I},\mathfrak B_{\mathsf M}).
  \label{eq:measurement-context-section5}
\end{equation}
```

Here:
``` math
\begin{align}
  A_{\mathsf M}
  &: \text{detector-sector stabilization operator},\\
  P_{\mathsf M}
  &: \text{detector-context projector},\\
  \chi_{\mathsf M}
  &: \text{detector spectral window},\\
  \tau_{\mathsf M}
  &: \text{measurement damping or stabilization scale},\\
  E_i^{(\mathsf M)}
  &: \text{positive detector effects},\\
  \mathfrak B_{\mathsf M}
  &: \text{survivor-basin partition}.
\end{align}
```

The measurement-sector finite admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}^{\mathsf M}
  =
  P_{\mathsf M}\chi_{\mathsf M}(A_{\mathsf M})
  \mathrm e^{-\tau_{\mathsf M}A_{\mathsf M}}
  \chi_{\mathsf M}(A_{\mathsf M})P_{\mathsf M}.
  \label{eq:measurement-filter-section5}
\end{equation}
```

A measurement record is then a downstream survivor-basin event:
``` math
\begin{equation}
  \Psi
  \to
  B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{measurement record}
  =
  \text{finite Nil survivor-basin shadow of a detector context}.
  }
  \label{eq:measurement-record-shadow-section5}
\end{equation}
```

## Finite detector effects

Detector outcomes are represented by positive effects:
``` math
\begin{equation}
  E_i^{(\mathsf M)}\succeq0.
\end{equation}
```
For a closed discrete detector,
``` math
\begin{equation}
  \sum_i E_i^{(\mathsf M)}=I_{\rm coh}.
  \label{eq:POVM-normalization-section5}
\end{equation}
```
For a continuous position-sensitive detector,
``` math
\begin{equation}
  \int E_x\,\,\mathrm dx=I_{\rm coh}.
\end{equation}
```

A finite position-sensitive effect may be written as
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
  \qquad
  k_x(y)=K_{\rm det}(y,x).
  \label{eq:finite-effect-section5}
\end{equation}
```
Then
``` math
\begin{equation}
  p(x)=\operatorname{tr}(\rho E_x)
\end{equation}
```
is the detection density.

This shows that localized detection does not require an infinitely sharp position projector as a primitive. The detector has finite resolution. The sharp PVM limit is recovered only when the detector kernel becomes infinitely narrow.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{localized detector click}
  =
  \text{finite detector effect captured below resolution}.
  }
  \label{eq:localized-click-section5}
\end{equation}
```

## Branch damping

A measurement context may preserve or destroy coherence between branches. In a finite branch basis, branch damping is represented by a Schur channel:
``` math
\begin{equation}
  \rho\mapsto D^{(\mathsf M)}\circ\rho,
  \label{eq:schur-damping-section5}
\end{equation}
```
or entrywise,
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}^{(\mathsf M)}\rho_{ab}.
\end{equation}
```

For this to be a valid quantum channel, the damping matrix must satisfy
``` math
\begin{equation}
  D^{(\mathsf M)}\succeq0,
  \qquad
  D_{aa}^{(\mathsf M)}=1.
  \label{eq:D-positive-section5}
\end{equation}
```
Then $`\rho\mapsto D^{(\mathsf M)}\circ\rho`$ is completely positive and trace preserving.

In a two-branch experiment,
``` math
\begin{equation}
  D
  =
  \begin{pmatrix}
    1 & d\\
    d^\ast & 1
  \end{pmatrix},
  \qquad
  |d|\le1.
\end{equation}
```
The channel acts as
``` math
\begin{equation}
  \begin{pmatrix}
    \rho_{11} & \rho_{12}\\
    \rho_{21} & \rho_{22}
  \end{pmatrix}
  \mapsto
  \begin{pmatrix}
    \rho_{11} & d\rho_{12}\\
    d^\ast\rho_{21} & \rho_{22}
  \end{pmatrix}.
\end{equation}
```

For real $`d\in[0,1]`$, the visibility law is
``` math
\begin{equation}
  V_{\rm MTT}=dV_0.
  \label{eq:visibility-law-section5}
\end{equation}
```

More generally, one may use an exponential form
``` math
\begin{equation}
  D_{ab}^{(\mathsf M)}
  =
  \mathrm e^{-\tau_{\mathsf M}\Lambda_{ab}^{(\mathsf M)}},
  \label{eq:exponential-damping-section5}
\end{equation}
```
provided $`\Lambda^{(\mathsf M)}`$ satisfies the appropriate conditional negative-definiteness condition that makes $`D^{(\mathsf M)}`$ positive semidefinite.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{visibility loss}
  =
  \text{Nil damping of off-diagonal Circle coherence}.
  }
  \label{eq:visibility-loss-section5}
\end{equation}
```

## Survivor-basin records

Branch damping is not the same as a definite record. A record requires survivor-basin stabilization.

The measurement chain is:
``` math
\begin{equation}
  \Psi
  \xrightarrow{\text{device coupling}}
  \Psi'
  \xrightarrow{\text{finite effects}}
  \rho'
  \xrightarrow{\text{branch damping}}
  D^{(\mathsf M)}\circ\rho'
  \xrightarrow{\text{basin capture}}
  B_i^{(\mathsf M)}.
  \label{eq:measurement-chain-section5}
\end{equation}
```

The survivor-basin partition is
``` math
\begin{equation}
  \mathfrak B_{\mathsf M}
  =
  \{B_i^{(\mathsf M)}\}_{i\in I}.
\end{equation}
```
An outcome is exact relative to the measurement context when the downstream state is captured by one basin:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{collapse shadow}
  =
  \text{branch damping plus survivor-basin selection}.
  }
  \label{eq:collapse-shadow-section5}
\end{equation}
```

This avoids treating collapse as a primitive conversion of a wave into a particle. It is a finite downstream transition from coherent branch structure to stabilized record.

## Born weights versus visibility damping

MTT separates outcome probabilities from interference visibility.

Visibility damping answers:
``` math
\begin{equation}
  \text{How much off-diagonal coherence remains?}
\end{equation}
```
It is controlled by
``` math
\begin{equation}
  D_{ab}^{(\mathsf M)}.
\end{equation}
```

Outcome probability answers:
``` math
\begin{equation}
  \text{Which record occurs, and how often?}
\end{equation}
```
In the basin-measure account, if $`\mu`$ is the admissibility-weighted measure on the measurement ensemble, then
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i^{(\mathsf M)})}
  {\sum_j\mu(B_j^{(\mathsf M)})}.
  \label{eq:basin-probability-section5}
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{branch damping controls visibility;}
  }
\end{equation}
```
whereas
``` math
\begin{equation}
  \boxed{
  \text{basin measure controls outcome frequency.}
  }
\end{equation}
```

This distinction is essential. A detector may completely suppress interference while leaving the diagonal branch weights unchanged. The eventual frequencies require the basin-measure layer.

## Double slit

The double-slit experiment is the canonical example. Let the two path branches be
``` math
\begin{equation}
  |1\rangle,\qquad |2\rangle.
\end{equation}
```
After the slits, a coherent state has the form
``` math
\begin{equation}
  |\psi\rangle
  =
  \alpha|\psi_1\rangle+\beta|\psi_2\rangle.
  \label{eq:double-slit-state-section5}
\end{equation}
```
The density matrix contains the off-diagonal terms
``` math
\begin{equation}
  \alpha\beta^\ast|\psi_1\rangle\langle\psi_2|
  +
  \alpha^\ast\beta|\psi_2\rangle\langle\psi_1|.
\end{equation}
```

A finite screen effect $`E_x`$ gives detection density
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
  \label{eq:double-slit-intensity-section5}
\end{align}
```
The final term is interference.

If a which-way detector damps the off-diagonal branch coherence, then
``` math
\begin{align}
  I_{\mathsf M}(x)
  &=
  |\alpha|^2\langle\psi_1|E_x|\psi_1\rangle
  +
  |\beta|^2\langle\psi_2|E_x|\psi_2\rangle
  \nonumber\\
  &\quad+
  2D_{12}^{(\mathsf M)}
  \operatorname{Re}
  \left[
    \alpha\beta^\ast
    \langle\psi_2|E_x|\psi_1\rangle
  \right].
  \label{eq:double-slit-damped-section5}
\end{align}
```

Thus:
``` math
\begin{align}
  D_{12}^{(\mathsf M)}\approx1
  &\quad\Rightarrow\quad
  \text{interference visible},
  \\
  D_{12}^{(\mathsf M)}\approx0
  &\quad\Rightarrow\quad
  \text{which-way record dominates}.
\end{align}
```

Each screen event is localized by a finite detector effect. Across many trials, the ensemble distribution shows or loses interference depending on branch coherence.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{double-slit behavior}
  =
  \text{finite detector records plus retained or damped branch coherence}.
  }
  \label{eq:double-slit-summary-section5}
\end{equation}
```

## Measurement devices disturb differently

Different measurement methods disturb different branch structures. This is not an experimental loophole. It is part of the MTT architecture.

A measurement context is not only an observable label. It contains concrete device data:
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
\end{equation}
```
Two devices that nominally measure the same branch alternative may still have different damping matrices:
``` math
\begin{equation}
  D_{ab}^{(\mathsf M_1)}
  \neq
  D_{ab}^{(\mathsf M_2)}.
\end{equation}
```
They may also have different detector effects:
``` math
\begin{equation}
  E_i^{(\mathsf M_1)}
  \neq
  E_i^{(\mathsf M_2)},
\end{equation}
```
and different survivor-basin partitions:
``` math
\begin{equation}
  \mathfrak B_{\mathsf M_1}
  \neq
  \mathfrak B_{\mathsf M_2}.
\end{equation}
```

Thus a weak, reversible marker may reduce visibility only partially, while a strong macroscopic detector may stabilize a durable which-way record:
``` math
\begin{align}
  \text{weak marker}
  &: \quad
  0<D_{12}<1,
  \\
  \text{strong which-way detector}
  &: \quad
  D_{12}\approx0.
\end{align}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{the measurement device is part of the projection context}.
  }
  \label{eq:device-context-section5}
\end{equation}
```

## Other benchmark experiments

The same pattern appears beyond the double slit.

#### Mach–Zehnder interferometer.

The two arms form a branch basis. If path coherence survives recombination, interference appears at the output ports. If which-path information is marked, the off-diagonal terms are damped:
``` math
\begin{equation}
  V_{\rm MZ}=D_{12}^{(\rm MZ)}V_0.
\end{equation}
```

#### Stern–Gerlach experiment.

The magnet orientation $`\hat n`$ defines a Lens context:
``` math
\begin{equation}
  \{|\uparrow_{\hat n}\rangle,|\downarrow_{\hat n}\rangle\}.
\end{equation}
```
The apparatus couples these branches to spatially separated detector basins. The outcome is exact relative to $`\hat n`$, not a context-free pre-existing classical spin value.

#### Delayed-choice and quantum eraser arrangements.

The final measurement context determines which branch decomposition is stabilized. Conditional interference may reappear when marker degrees of freedom are projected into a recombining basis. This does not require retroactive alteration of a past path. It reflects a change in Lens decomposition and Nil survivor partition.

#### Matter-wave diffraction.

Massive particles produce interference when coherent branch structure survives. Individual detections remain localized finite records. Increasing mass or complexity suppresses interference only when environmental or detector coupling damps off-diagonal coherence.

#### Hong–Ou–Mandel interference.

The relevant branches are multi-particle alternatives. Indistinguishable alternatives retain joint coherence; distinguishability damps the off-diagonal terms responsible for the interference dip.

All these experiments follow:
``` math
\begin{equation}
  \boxed{
  \text{coherent branches}
  \to
  \text{measurement context}
  \to
  \text{branch damping or recombination}
  \to
  \text{survivor records}.
  }
  \label{eq:benchmark-pattern-section5}
\end{equation}
```

## Connection to internal/fiber geometry

The wave–particle result can be stated abstractly, but the FP realization gives it a geometric source.

The finite coherent kernel is generated by internal admissibility:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
\end{equation}
```
The observed four-dimensional shadows arise after projecting this finite coherent structure onto the base $`Y^4`$, detector contexts, and effective sectoral descriptions.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional pointlike events are local projection shadows of finite fiber-coherent
  admissibility}.
  }
\end{equation}
```
And:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional wave interference is the spectral phase shadow of the same admissible
  coherent sector}.
  }
\end{equation}
```

This is the common-source claim in its strongest form:
``` math
\begin{equation}
  \boxed{
  \text{Dirac delta and wave behavior have one finite geometric source.}
  }
  \label{eq:delta-wave-one-source-section5}
\end{equation}
```

## Summary

The finite coherent admissibility operator
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
has three immediate physical shadows.

First, the local kernel gives the particle shadow:
``` math
\begin{equation}
  \boxed{
  \text{particle}
  =
  \text{local Dirac-delta shadow of finite coherent support}.
  }
\end{equation}
```

Second, the spectral expansion gives the wave shadow:
``` math
\begin{equation}
  \boxed{
  \text{wave}
  =
  \text{spectral phase-coherent shadow of finite coherent support}.
  }
\end{equation}
```

Third, finite detector effects, branch damping, and survivor basins give the measurement shadow:
``` math
\begin{equation}
  \boxed{
  \text{measurement record}
  =
  \text{finite survivor-basin shadow}.
  }
\end{equation}
```

Together:
``` math
\begin{equation}
  \boxed{
  \text{wave, particle, and measurement are three projection shadows of finite coherent
  admissibility}.
  }
\end{equation}
```

In the fixed-point realization, this finite coherent admissibility is generated by compact internal/fiber geometry:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
  }
\end{equation}
```

Therefore the Dirac delta and the wave are not rival primitives. They are the first two observable shadows of the same finite coherent fiber-generated kernel.

# Scattering, finite propagators, and fiber damping

The previous section established the first three projection shadows of finite coherent admissibility: the local Dirac-delta shadow, the spectral wave shadow, and the measurement record shadow. This section applies the same structure to propagation and scattering.

The main point is subtle but important. In a flat Euclidean benchmark, the finite coherent operator produces the familiar Gaussian momentum factor
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}.
\end{equation}
```
However, in the fixed-point realization of MTT this should not be confused with a fundamental Lorentzian damping factor
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}.
\end{equation}
```
The default physical interpretation is instead fiber damping:
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}},
\end{equation}
```
where $`A_{\rm int}`$ is a positive internal elliptic operator. After dimensional reduction, this gives ordinary four-dimensional zero-mode propagation plus damped massive internal or Kaluza–Klein-like excitations.

Thus the central message of this section is:
``` math
\begin{equation}
  \boxed{
  \text{finite scattering corrections arise from admissible finite kernels, internal-mode
  damping, and finite overlaps, not from naive Lorentzian } \mathrm e^{-\tau\Box}.
  }
  \label{eq:scattering-main-message}
\end{equation}
```

## Euclidean scalar benchmark

The cleanest worked example is the Euclidean scalar heat-kernel model. Let
``` math
\begin{equation}
  A=-\Delta
\end{equation}
```
on $`\mathbb R^d`$, with
``` math
\begin{equation}
  P=I,
  \qquad
  \chi=1.
\end{equation}
```
Then
``` math
\begin{equation}
  B_{\rm adm}
  =
  \mathrm e^{-\tau A}
  =
  \mathrm e^{\tau\Delta}.
\end{equation}
```

The Fourier modes obey
``` math
\begin{equation}
  -\Delta \mathrm e^{\mathrm ik\cdot x}
  =
  k^2\mathrm e^{\mathrm ik\cdot x}.
\end{equation}
```
Therefore
``` math
\begin{equation}
  \mathrm e^{-\tau A}\mathrm e^{\mathrm ik\cdot x}
  =
  \mathrm e^{-\tau k^2}\mathrm e^{\mathrm ik\cdot x}.
  \label{eq:euclidean-momentum-damping-section6}
\end{equation}
```

The heat kernel is
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  \int_{\mathbb R^d}
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \mathrm e^{-\tau k^2}
  \mathrm e^{\mathrm ik\cdot(x-y)}.
  \label{eq:euclidean-heat-fourier-section6}
\end{equation}
```
Evaluating the Gaussian integral gives
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
  \label{eq:euclidean-heat-kernel-section6}
\end{equation}
```

As $`\tau\downarrow0`$,
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  \to
  \delta^{(d)}(x-y)
\end{equation}
```
distributionally.

Thus the Euclidean scalar benchmark gives:
``` math
\begin{equation}
  \boxed{
  \delta^{(d)}(x-y)
  \rightsquigarrow
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right),
  }
  \label{eq:delta-to-gaussian-section6}
\end{equation}
```
and, in momentum space,
``` math
\begin{equation}
  \boxed{
  1
  \rightsquigarrow
  \mathrm e^{-\tau k^2}.
  }
  \label{eq:one-to-gaussian-momentum-section6}
\end{equation}
```

This benchmark is mathematically useful because it gives a closed model of finite coherent width, delta recovery, and high-mode damping.

## Finite scalar propagator shadow

The ordinary Euclidean scalar propagator is
``` math
\begin{equation}
  \Delta(k)
  =
  \frac{1}{k^2+m^2}.
  \label{eq:ordinary-euclidean-propagator-section6}
\end{equation}
```
Inserting one finite coherent heat-kernel factor gives the finite propagator shadow
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
  \label{eq:finite-euclidean-propagator-section6}
\end{equation}
```

In position space,
``` math
\begin{equation}
  \Delta_{\rm adm}(x-y)
  =
  \int_{\mathbb R^d}
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}
  \mathrm e^{\mathrm ik\cdot(x-y)}.
  \label{eq:finite-position-propagator-section6}
\end{equation}
```
Equivalently,
``` math
\begin{equation}
  \Delta_{\rm adm}
  =
  K_\tau^{(d)}\ast\Delta
\end{equation}
```
in the distributional sense.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite propagator shadow}
  =
  \text{ordinary propagator convolved with finite coherent kernel}.
  }
  \label{eq:finite-propagator-convolution-section6}
\end{equation}
```

For small $`\tau k^2`$,
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
  =
  1-\tau k^2+\frac12\tau^2k^4+O(\tau^3k^6).
  \label{eq:gaussian-expansion-section6}
\end{equation}
```
Therefore the leading correction to the propagator is controlled by
``` math
\begin{equation}
  \tau k^2.
\end{equation}
```
At low momentum,
``` math
\begin{equation}
  \tau k^2\ll1,
\end{equation}
```
ordinary pointlike propagation is recovered.

At high momentum,
``` math
\begin{equation}
  \tau k^2\gtrsim1,
\end{equation}
```
the finite coherent structure becomes resolvable.

## Dimensional scale

For a Laplace-type operator,
``` math
\begin{equation}
  [A]=L^{-2}=E^2.
\end{equation}
```
The damping factor
``` math
\begin{equation}
  \mathrm e^{-\tau A}
\end{equation}
```
is dimensionless only if
``` math
\begin{equation}
  [\tau]=L^2=E^{-2}.
\end{equation}
```

The coherent length scale is
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau},
  \label{eq:scattering-lcoh-section6}
\end{equation}
```
and the corresponding effective energy scale is
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
  \label{eq:scattering-Lambda-section6}
\end{equation}
```

The finite-width expansion parameter is
``` math
\begin{equation}
  \tau E_{\rm probe}^2
  =
  \left(
    \frac{E_{\rm probe}}{\Lambda_{\rm eff}}
  \right)^2.
  \label{eq:scattering-expansion-parameter-section6}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  E_{\rm probe}\ll\Lambda_{\rm eff}
  \quad\Rightarrow\quad
  \text{pointlike effective behavior}.
  }
\end{equation}
```
and
``` math
\begin{equation}
  \boxed{
  E_{\rm probe}\sim\Lambda_{\rm eff}
  \quad\Rightarrow\quad
  \text{finite coherent structure may become observable}.
  }
\end{equation}
```

## Flat four-dimensional Euclidean case

For $`d=4`$, the Euclidean heat kernel becomes
``` math
\begin{equation}
  K_\tau^{(4)}(x-y)
  =
  (4\pi\tau)^{-2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
  \label{eq:4d-heat-kernel-section6}
\end{equation}
```
Its Fourier transform is
``` math
\begin{equation}
  \widehat K_\tau^{(4)}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```

The finite Euclidean scalar propagator shadow is
``` math
\begin{equation}
  \Delta_{\rm adm}^{(4)}(k)
  =
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
  \label{eq:4d-finite-propagator-section6}
\end{equation}
```

This expression is useful as a benchmark because all pieces can be computed explicitly. It will be elevated to a complete benchmark theorem later in the paper.

However, it must be interpreted carefully. Equation <a href="#eq:4d-finite-propagator-section6" data-reference-type="eqref" data-reference="eq:4d-finite-propagator-section6">[eq:4d-finite-propagator-section6]</a> is a Euclidean scalar model. It is not the default Lorentzian MTT prescription.

<div id="rem:euclidean-benchmark-lorentzian" class="remark">

*Remark 1* (Euclidean benchmark versus Lorentzian physics). The factor $`\mathrm e^{-\tau k^2}`$ is clean when $`k^2\ge0`$, as in Euclidean signature or positive spectral charts. In Lorentzian signature, replacing $`k^2`$ by the indefinite invariant associated with $`\Box`$ is not automatically causal, unitary, or admissible. The physical MTT implementation uses positive fiber, spatial, Hamiltonian, or constraint-compatible operators.

</div>

## Why $`e^{-\tau\Box}`$ is not the fundamental object

The Lorentzian d’Alembertian is indefinite. In flat spacetime, depending on sign convention,
``` math
\begin{equation}
  \Box
  =
  -\partial_t^2+\nabla^2
\end{equation}
```
or the opposite sign. Its Fourier symbol is not nonnegative. Therefore
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
is not a heat-kernel damping factor in the same sense as
``` math
\begin{equation}
  \mathrm e^{\tau\Delta}
\end{equation}
```
on Euclidean space.

Naively inserting
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
can threaten:

1.  causality;

2.  unitarity;

3.  pole structure;

4.  reflection positivity;

5.  gauge identities;

6.  constraint preservation.

MTT therefore imposes the Lorentzian admissibility principle:
``` math
\begin{equation}
  \boxed{
  \text{the damping operator must be positive in the admissible physical sector}.
  }
  \label{eq:lorentzian-admissibility-principle-section6}
\end{equation}
```

In the fixed-point realization this means:
``` math
\begin{equation}
  A=A_{\rm int},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```

In Cauchy-slice formulations this means:
``` math
\begin{equation}
  A=A_\Sigma,
  \qquad
  A_\Sigma\ge0
\end{equation}
```
on a spatial slice or constrained physical data.

In gauge theory this means:
``` math
\begin{equation}
  A=A_{\rm gauge}
\end{equation}
```
after quotienting or in a gauge-covariant physical sector.

In gravity this means:
``` math
\begin{equation}
  A=A_{\rm grav}
\end{equation}
```
on diffeomorphism-compatible or constraint-compatible geometric data.

Thus:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  \quad
  \text{unless a positive physical-sector replacement has been constructed}.
  }
  \label{eq:A-not-box-section6}
\end{equation}
```

## Fiber damping in the fixed-point realization

In the fixed-point realization, the admissibility operator is the positive internal operator
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```
Let
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j.
\end{equation}
```
Then
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
  \label{eq:fiber-damping-eigenmode-section6}
\end{equation}
```

The zero mode satisfies
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
and is undamped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

A nonzero internal mode satisfies
``` math
\begin{equation}
  \mu_j^2>0,
\end{equation}
```
and is damped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT damping suppresses internal nonzero modes while leaving coherent zero modes
  undamped.}
  }
  \label{eq:fiber-damping-summary-section6}
\end{equation}
```

This is the clean physical replacement for naive Lorentzian smoothing.

## Dimensional reduction and effective four-dimensional propagation

After dimensional reduction, internal eigenmodes appear as effective four-dimensional fields. Schematically, a field on the total space may be expanded as
``` math
\begin{equation}
  \Phi(x,z)
  =
  \sum_j
  \varphi_j(x)\phi_j(z),
  \label{eq:KK-expansion-section6}
\end{equation}
```
where
``` math
\begin{equation}
  x\in Y^4,
  \qquad
  z\in X^6.
\end{equation}
```

If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
then the internal eigenvalue contributes to the effective four-dimensional mass scale:
``` math
\begin{equation}
  m_j^2
  =
  m_0^2+\mu_j^2
\end{equation}
```
in the simplest scalar model.

The finite admissibility factor assigns weight
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
to the $`j`$-th internal mode. Thus the effective four-dimensional propagator has schematic Källén–Lehmann-like form
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
  \label{eq:4D-effective-propagator-section6}
\end{equation}
```
Here the residues $`Z_j`$ depend on the internal geometry, wavefunction overlap, and sectoral normalization.

If
``` math
\begin{equation}
  Z_j\ge0
\end{equation}
```
and the internal sector is ghost-free, then the spectral representation is positive. Positivity is therefore not automatic for every formal sector; it is a consistency requirement of the sectoral realization.

The zero mode has
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
so its finite admissibility weight is
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Therefore:
``` math
\begin{equation}
  \boxed{
  \text{ordinary four-dimensional low-energy propagation is recovered from undamped zero modes.}
  }
  \label{eq:zero-mode-recovery-section6}
\end{equation}
```

The massive internal modes are suppressed by
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```
Therefore finite coherent corrections appear as suppressed internal-tower contributions, threshold effects, loop effects, finite overlaps, or detector-dependent form factors.

## Fiber damping versus base damping

One may formally decompose a total Euclidean momentum as
``` math
\begin{equation}
  k^2=k_{\rm base}^2+k_{\rm fiber}^2.
\end{equation}
```
A total Euclidean Gaussian factor would then split as
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
  =
  \mathrm e^{-\tau k_{\rm base}^2}
  \mathrm e^{-\tau k_{\rm fiber}^2}.
\end{equation}
```

However, this is not the default Lorentzian FP/MTT interpretation. The clean fixed-point choice is fiber damping:
``` math
\begin{equation}
  \mathrm e^{-\tau k_{\rm fiber}^2}
  \quad
  \text{or spectrally}
  \quad
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

The base dynamics remain Lorentzian and are treated by standard hyperbolic or Hamiltonian evolution. There is no fundamental base factor
``` math
\begin{equation}
  \mathrm e^{-\tau k_{\rm base}^2}
\end{equation}
```
unless a positive spatial/Cauchy-slice operator is explicitly introduced and justified.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the default MTT finite filter is internal/fiber damping, not four-dimensional Lorentzian
  momentum damping.}
  }
  \label{eq:fiber-not-base-section6}
\end{equation}
```

## Contact interactions as finite overlaps

Pointlike quantum field theory often uses local contact interactions. For example, a scalar quartic interaction is written as
``` math
\begin{equation}
  S_{\rm int}
  =
  \frac{\lambda}{4!}
  \int
  \phi(x)^4\,\,\mathrm d^dx.
  \label{eq:local-contact-section6}
\end{equation}
```
This expression assumes exact coincidence at one spacetime point.

In finite coherent admissibility, exact coincidence is replaced by finite coherent overlap. A schematic finite version is
``` math
\begin{equation}
  S_{\rm int}^{\rm adm}
  =
  \frac{\lambda}{4!}
  \int
  \prod_{i=1}^4\,\mathrm d^dx_i\,
  K_\tau(x_1,x_2,x_3,x_4)
  \phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4),
  \label{eq:finite-contact-section6}
\end{equation}
```
where $`K_\tau`$ is sharply peaked near coincidence but finite.

In the sharp limit,
``` math
\begin{equation}
  K_\tau(x_1,x_2,x_3,x_4)
  \to
  \delta(x_1-x_2)\delta(x_1-x_3)\delta(x_1-x_4),
\end{equation}
```
and the local contact interaction is recovered.

In the FP/fiber realization, the finite overlap may arise from internal wavefunction overlap:
``` math
\begin{equation}
  \lambda_{ijkl}^{\rm eff}
  =
  \lambda_{10D}
  \int_{X^6}
  \phi_i(z)\phi_j(z)\phi_k(z)\phi_l(z)\,\,\mathrm dz
\end{equation}
```
together with admissibility weights
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_i^2},
  \quad
  \mathrm e^{-\tau\mu_j^2},
  \quad
  \mathrm e^{-\tau\mu_k^2},
  \quad
  \mathrm e^{-\tau\mu_l^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{local contact}
  =
  \text{sharp shadow of finite coherent overlap}.
  }
  \label{eq:contact-sharp-shadow-section6}
\end{equation}
```

## Scattering amplitudes

In a scalar Euclidean benchmark, a tree-level exchange amplitude may contain
``` math
\begin{equation}
  \frac{1}{k^2+m^2}.
\end{equation}
```
A finite coherent insertion gives
``` math
\begin{equation}
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
\end{equation}
```
At low momentum,
``` math
\begin{equation}
  \tau k^2\ll1,
\end{equation}
```
the standard amplitude is recovered.

In the FP/fiber realization, the four-dimensional amplitude instead receives a tower of internal-mode contributions:
``` math
\begin{equation}
  \mathcal A_{4D}(p)
  \sim
  \sum_{j\ge0}
  g_j^2
  \frac{\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
  \label{eq:fiber-scattering-amplitude-section6}
\end{equation}
```
Here $`g_j`$ is an effective coupling determined by internal wavefunction overlap.

The zero mode contributes with no internal damping:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
The higher internal modes contribute with suppressed weights:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent scattering corrections are suppressed internal-mode, overlap, or
  threshold effects.}
  }
  \label{eq:finite-scattering-corrections-section6}
\end{equation}
```

This is the physically safe way to connect MTT damping to observed four-dimensional scattering.

## Amplitude weights and cross-section caution

If the first nonzero internal eigenvalue is
``` math
\begin{equation}
  \mu_1^2\sim\lambda_\ast,
\end{equation}
```
and
``` math
\begin{equation}
  \tau=\lambda_\ast^{-1}\log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
then its admissibility weight is
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_1^2}
  \sim
  \mathrm e^{-\log(C_Q/\epsilon_{\rm adm})}
  =
  \frac{\epsilon_{\rm adm}}{C_Q}.
  \label{eq:first-mode-weight-section6}
\end{equation}
```
This gives a clean relationship between the first internal-mode amplitude weight and the admissibility tolerance.

However, an observable cross section depends on more than this single factor. It depends on:

1.  production couplings;

2.  decay couplings;

3.  resonance widths;

4.  phase space;

5.  internal wavefunction overlaps;

6.  gauge and representation factors;

7.  interference with Standard Model backgrounds.

Therefore the paper does not assert a universal numerical cross-section suppression such as $`\epsilon_{\rm adm}`$ or $`\epsilon_{\rm adm}^2`$. The safe claim is:
``` math
\begin{equation}
  \boxed{
  \text{the \(j\)-th internal excitation carries an amplitude-level admissibility weight }
  \mathrm e^{-\tau\mu_j^2}.
  }
  \label{eq:amplitude-level-weight-section6}
\end{equation}
```

The observable collider prediction must be computed from the derived four-dimensional effective action.

## Bounds from pointlike scattering

In the Euclidean scalar benchmark, if no deviation from a pointlike amplitude is observed up to energy $`E_{\max}`$ with tolerance $`\eta`$, the leading estimate is
``` math
\begin{equation}
  \tau E_{\max}^2\lesssim\eta.
  \label{eq:scalar-scattering-bound-section6}
\end{equation}
```
Equivalently,
``` math
\begin{equation}
  \Lambda_{\rm eff}
  \gtrsim
  \frac{E_{\max}}{\sqrt{\eta}}.
  \label{eq:Lambda-bound-section6}
\end{equation}
```

In the FP/fiber realization, the corresponding bound is on the internal scale:
``` math
\begin{equation}
  \mu_1\gtrsim E_{\rm threshold},
\end{equation}
```
up to coupling, representation, and damping effects. Since
``` math
\begin{equation}
  \mu_1\sim R^{-1},
\end{equation}
```
this translates into
``` math
\begin{equation}
  R\lesssim E_{\rm threshold}^{-1}.
\end{equation}
```

The coherence scale is then
``` math
\begin{equation}
  \sqrt{\tau}
  \sim
  R
  \sqrt{\log\frac{C_Q}{\epsilon_{\rm adm}}}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{scattering constrains the finite coherent internal length scale.}
  }
  \label{eq:scattering-constrains-length-section6}
\end{equation}
```

Precise numerical bounds require specifying the internal geometry, gauge embedding, matter representations, and effective couplings.

## Loop regularization and open tasks

The damping factor
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
suppresses high internal modes. This suggests a natural finite-mode control mechanism in loop sums over internal excitations:
``` math
\begin{equation}
  \sum_j
  F_j
  \quad
  \rightsquigarrow
  \quad
  \sum_j
  \mathrm e^{-\tau\mu_j^2}F_j.
  \label{eq:loop-sum-damping-section6}
\end{equation}
```

However, this does not automatically complete renormalization. One must still prove:

1.  compatibility with gauge identities;

2.  unitarity of the reduced theory;

3.  positivity of the spectral representation;

4.  stability under radiative corrections;

5.  correct low-energy effective matching;

6.  anomaly cancellation in chiral sectors;

7.  preservation of Lorentzian causal propagation.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{internal damping is a candidate ultraviolet-control mechanism, not a completed
  renormalization theorem by itself.}
  }
  \label{eq:not-renormalization-theorem-section6}
\end{equation}
```

This is an execution task for sector-specific MTT field theory.

## Gauge-sector caution

Gauge scattering cannot be modified by inserting damping factors arbitrarily. A gauge-sector finite propagator must be constructed from physical or quotient-compatible data:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
  \label{eq:gauge-Badm-preview-section6}
\end{equation}
```

For Abelian conserved-current exchange, a schematic transverse form may be
``` math
\begin{equation}
  \mathcal A_{\rm adm}(k)
  \sim
  e^2J_\mu(k)
  \frac{\mathrm e^{-\tau k^2}}{k^2}
  P_T^{\mu\nu}(k)
  J'_\nu(-k),
\end{equation}
```
but this is safe only in a positive Euclidean or physical transverse chart. In the FP/fiber realization, the safer statement is that internal gauge excitations carry weights
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
after gauge quotienting.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{filter after quotienting, or filter covariantly before quotienting}.
  }
  \label{eq:gauge-safe-rule-preview-section6}
\end{equation}
```

This rule will be developed in the gauge section.

## Gravity-sector caution

Gravity requires even more care. A gravitational finite filter cannot simply damp all metric components. Metric components include diffeomorphism redundancy.

The schematic form is
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
  \label{eq:grav-Badm-preview-section6}
\end{equation}
```
Here $`A_{\rm grav}`$ must be positive or constraint-compatible on geometric data, and $`P_{\rm diff}`$ must respect diffeomorphism equivalence or the gravitational constraint surface.

In weak-field settings, $`A_{\rm grav}`$ may be a positive spatial or transverse-traceless operator on Cauchy-slice data. In full gravity, this is a much harder nonperturbative construction.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravitational damping must act on diffeomorphism-compatible geometry, not coordinate
  components.}
  }
  \label{eq:gravity-safe-rule-preview-section6}
\end{equation}
```

## Scattering as a projection shadow

The finite coherent interpretation of scattering can now be summarized.

In the Euclidean scalar benchmark:
``` math
\begin{equation}
  \frac{1}{k^2+m^2}
  \quad
  \rightsquigarrow
  \quad
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
\end{equation}
```

In the FP/fiber realization:
``` math
\begin{equation}
  \frac{1}{p^2-m_0^2+\mathrm i\epsilon}
  \quad
  \rightsquigarrow
  \quad
  \sum_j
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```

In contact interactions:
``` math
\begin{equation}
  \delta\text{-coincidence}
  \quad
  \rightsquigarrow
  \quad
  \text{finite coherent overlap}.
\end{equation}
```

In all cases:
``` math
\begin{equation}
  \boxed{
  \text{pointlike scattering}
  =
  \text{sharp or low-resolution shadow of finite coherent admissibility}.
  }
  \label{eq:pointlike-scattering-shadow-section6}
\end{equation}
```

## Summary

This section separated three different ideas that must not be conflated.

First, the Euclidean scalar benchmark gives the clean Gaussian formula:
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right),
\end{equation}
```
and
``` math
\begin{equation}
  \widehat K_\tau(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```

Second, the FP realization uses positive internal fiber damping:
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
\end{equation}
```
The zero mode is undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Massive internal modes are damped:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Third, Lorentzian MTT does not use naive
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
as its fundamental damping operator. The admissibility operator must be positive in the physical sector:
``` math
\begin{equation}
  \boxed{
  A=A_{\rm int},
  \quad
  A=A_\Sigma,
  \quad
  A=A_{\rm gauge},
  \quad
  A=A_{\rm grav},
  \quad
  \text{or another positive constraint-compatible operator}.
  }
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{finite scattering corrections are projection shadows of positive coherent
  admissibility, not arbitrary Lorentzian nonlocality}.
  }
\end{equation}
```

# Cauchy-slice kernels and Lorentzian admissibility

The previous section separated the Euclidean scalar benchmark from the physical Lorentzian implementation of MTT. The distinction is essential. The factor
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
\end{equation}
```
is mathematically clean in Euclidean or positive spectral settings, but the naive Lorentzian expression
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
is not the fundamental MTT prescription.

This section gives the Lorentzian replacement. In Lorentzian sectors, finite coherent admissibility is implemented through positive internal operators, positive spatial operators on Cauchy slices, Hamiltonian or constraint-compatible operators, or equal-time kernels that enter as lower-order bounded terms without changing the hyperbolic principal symbol.

The guiding principle is:
``` math
\begin{equation}
  \boxed{
  \text{Lorentzian MTT uses positive admissibility data on physical sectors, not indefinite
  spacetime heat flow.}
  }
  \label{eq:lorentzian-principle-section7}
\end{equation}
```

This preserves the central finite-kernel logic while avoiding the usual pathologies of nonlocal Lorentzian exponential operators.

## The Lorentzian divide

Euclidean heat flow is generated by a positive elliptic operator:
``` math
\begin{equation}
  A=-\Delta\ge0.
\end{equation}
```
The heat operator
``` math
\begin{equation}
  \mathrm e^{-\tau A}=\mathrm e^{\tau\Delta}
\end{equation}
```
is smoothing, bounded, and contractive on suitable spaces.

Lorentzian wave propagation is different. The d’Alembertian
``` math
\begin{equation}
  \Box
\end{equation}
```
is hyperbolic and indefinite. It is not a positive elliptic operator. Therefore
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
is not a heat operator in the same sense.

A naive Lorentzian exponential can introduce:

1.  acausal tails;

2.  uncontrolled infinite time derivatives;

3.  ghost-like poles or extra degrees of freedom;

4.  loss of unitarity;

5.  ambiguity in analytic continuation;

6.  violation of gauge or gravitational constraints.

MTT therefore rejects the naive identification
``` math
\begin{equation}
  A=\Box
\end{equation}
```
as the fundamental damping rule.

Instead:
``` math
\begin{equation}
  \boxed{
  A
  \text{ must be positive or constraint-compatible in the admissible sector.}
  }
  \label{eq:A-positive-sector-section7}
\end{equation}
```

## Positive admissibility operators

The allowed Lorentzian implementations include the following.

#### Internal/fiber operators.

In the fixed-point realization,
``` math
\begin{equation}
  A=A_{\rm int}
  =
  \sum_{n=1}^3\kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```
This is the cleanest case. Damping acts on compact internal fiber modes:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
  \qquad
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
\end{equation}
```

#### Spatial Cauchy-slice operators.

On a globally hyperbolic spacetime, choose a Cauchy slice $`\Sigma_t`$. A positive spatial elliptic operator
``` math
\begin{equation}
  A_\Sigma\ge0
\end{equation}
```
may act on data on $`\Sigma_t`$. For example, in a flat spatial chart,
``` math
\begin{equation}
  A_\Sigma=-\Delta_\Sigma.
\end{equation}
```

#### Hamiltonian or energy operators.

In a canonical formulation, one may use a positive Hamiltonian, positive energy operator, or constraint-compatible quadratic form where such an object is available.

#### Gauge-quotiented operators.

In gauge theory, the operator must act on gauge-admissible physical content:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
\end{equation}
```

#### Diffeomorphism-compatible operators.

In gravity, the operator must act on geometric or constraint-compatible data:
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
\end{equation}
```

Thus the Lorentzian admissibility rule is:
``` math
\begin{equation}
  \boxed{
  \text{damp only positive admissible directions, not arbitrary Lorentzian spacetime
  directions.}
  }
  \label{eq:damp-positive-directions-section7}
\end{equation}
```

## Global hyperbolicity and Cauchy slices

Let $`Y^4`$ be globally hyperbolic. Then it admits a foliation by Cauchy slices
``` math
\begin{equation}
  \Sigma_t,
\end{equation}
```
so that
``` math
\begin{equation}
  Y^4
  \cong
  \mathbb R\times\Sigma.
\end{equation}
```
A field $`\phi`$ can be represented by Cauchy data
``` math
\begin{equation}
  \left(\phi|_{\Sigma_t},\,n^\mu\nabla_\mu\phi|_{\Sigma_t}\right),
\end{equation}
```
where $`n^\mu`$ is the future-directed unit normal to the slice.

A hyperbolic equation has finite propagation speed when its principal symbol defines a causal cone and lower-order terms do not alter the characteristic structure.

A typical scalar hyperbolic equation has the schematic form
``` math
\begin{equation}
  \Box_g\phi
  +
  m^2\phi
  =
  F(\phi,\nabla\phi).
  \label{eq:hyperbolic-scalar-section7}
\end{equation}
```
The causal domain of dependence is determined by the principal part
``` math
\begin{equation}
  \Box_g.
\end{equation}
```

MTT finite kernels are Lorentzian-admissible when they do not change this principal hyperbolic structure.

## Equal-time finite kernels

A Cauchy-slice finite kernel acts on fields at equal time:
``` math
\begin{equation}
  (\mathcal K_t f)(x)
  =
  \int_{\Sigma_t}
  K_t(x,y)f(y)\,\,\mathrm d\mu_{\Sigma_t}(y),
  \qquad
  x,y\in\Sigma_t.
  \label{eq:equal-time-kernel-section7}
\end{equation}
```
Here $`K_t(x,y)`$ is a spatial kernel on the slice $`\Sigma_t`$.

The kernel is finite and admissible if it is bounded in the relevant Sobolev scale. A simple sufficient condition is that $`K_t`$ is integrable in each variable:
``` math
\begin{equation}
  \sup_x
  \int_{\Sigma_t}
  |K_t(x,y)|\,\,\mathrm d\mu_{\Sigma_t}(y)
  <
  \infty,
  \label{eq:kernel-L1-x-section7}
\end{equation}
```
and
``` math
\begin{equation}
  \sup_y
  \int_{\Sigma_t}
  |K_t(x,y)|\,\,\mathrm d\mu_{\Sigma_t}(x)
  <
  \infty.
  \label{eq:kernel-L1-y-section7}
\end{equation}
```
Then $`\mathcal K_t`$ is bounded on $`L^2(\Sigma_t)`$ by Schur-type estimates.

More generally, if $`K_t`$ is smooth enough and has controlled spatial decay or compact support, it defines a bounded lower-order operator on Sobolev spaces:
``` math
\begin{equation}
  \mathcal K_t:H^s(\Sigma_t)\to H^s(\Sigma_t)
\end{equation}
```
for the relevant range of $`s`$.

Such a kernel can represent finite detector resolution, finite spatial overlap, finite source profile, or finite coherent internal projection read on a Cauchy slice.

## Lower-order nonlocality

Consider a hyperbolic equation modified by an equal-time finite kernel:
``` math
\begin{equation}
  \Box_g\phi
  +
  m^2\phi
  +
  \mathcal K_t\phi
  =
  J.
  \label{eq:kernel-modified-hyperbolic-section7}
\end{equation}
```
The operator $`\mathcal K_t`$ acts only on spatial variables at fixed time and is bounded on the relevant energy space.

The principal part remains
``` math
\begin{equation}
  \Box_g.
\end{equation}
```
Therefore the characteristic cone is unchanged.

The finite kernel modifies the lower-order dynamics, dispersion, or effective source response, but it does not replace the hyperbolic principal symbol. Hence:
``` math
\begin{equation}
  \boxed{
  \text{equal-time bounded kernels do not by themselves change the causal characteristic
  cone.}
  }
  \label{eq:principal-symbol-unchanged-section7}
\end{equation}
```

This is the key Lorentzian distinction. MTT finite kernels are admissible when they behave as bounded lower-order terms relative to the hyperbolic equation.

## Domain of dependence

For a local hyperbolic system, the solution in a region depends only on initial data inside the causal past determined by the principal symbol. If a finite kernel enters as a bounded lower-order equal-time term, the principal causal cone remains the same.

Let $`D(\mathcal O)`$ denote the domain of dependence of a region $`\mathcal O\subset\Sigma_0`$ under the original hyperbolic operator. If the finite kernel is lower-order and compatible with the energy estimates, then the modified equation has the same characteristic propagation speed.

The energy estimate has the schematic form
``` math
\begin{equation}
  E(t)
  \le
  C
  \left[
    E(0)
    +
    \int_0^t
    \|J(s)\|^2\,\,\mathrm ds
  \right]
  \exp(C_Kt),
  \label{eq:energy-estimate-kernel-section7}
\end{equation}
```
where $`C_K`$ depends on the operator norm of $`\mathcal K_t`$, but not on new superluminal principal characteristics.

Thus the finite kernel may alter growth rates, mode mixing, or finite-width responses, but it does not create a new principal propagation cone.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent Cauchy kernels can preserve relativistic finite propagation speed.}
  }
  \label{eq:finite-propagation-preserved-section7}
\end{equation}
```

## Causality versus finite overlap

Finite overlap should not be confused with acausal signaling.

A spatial kernel may correlate or average data over a finite region of a Cauchy slice:
``` math
\begin{equation}
  (\mathcal K_t f)(x)
  =
  \int_{\Sigma_t}
  K_t(x,y)f(y)\,\,\mathrm dy.
\end{equation}
```
This means that the effective state at $`x`$ includes a finite spatial profile. But if the kernel is part of the initial data, detector response, internal projection, or lower-order source term, it does not imply that a signal is propagating outside the causal cone.

The distinction is:
``` math
\begin{equation}
  \boxed{
  \text{finite spatial support or overlap}
  \neq
  \text{superluminal signal propagation}.
  }
  \label{eq:finite-support-not-superluminal-section7}
\end{equation}
```

A detector with finite spatial resolution samples a finite region. That is not acausal. A finite internal wavefunction projects to an effective finite profile. That is not acausal. A bounded equal-time kernel may enter the equations without changing the characteristic cone. That is not acausal.

Acausality would arise only if the construction allowed controllable influence outside the domain of dependence or changed the principal hyperbolic structure in a way that creates superluminal characteristics.

## Manifest covariance as Lens

A Cauchy-slice construction is not always manifestly Lorentz covariant. It singles out a foliation
``` math
\begin{equation}
  \{\Sigma_t\}_{t\in\mathbb R}.
\end{equation}
```
In MTT this is a Lens choice: a representation used to define positive admissibility data.

This is analogous to gauge fixing. Coulomb gauge is not manifestly Lorentz covariant, but it can isolate physical transverse modes. The loss of manifest covariance in the representative does not by itself imply loss of physical covariance.

Similarly, a Cauchy-slice kernel may be a non-manifestly covariant representative of a physically admissible finite projection. The physical requirements are:

1.  the principal causal structure is preserved;

2.  constraints are preserved;

3.  observable predictions are independent of unphysical representative choices or transform consistently under changes of foliation;

4.  no controllable superluminal signaling is introduced.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{manifest covariance is a Lens property;}
  }
\end{equation}
```
whereas
``` math
\begin{equation}
  \boxed{
  \text{physical covariance is a constraint and observable-level requirement.}
  }
\end{equation}
```

This distinction allows MTT to use positive Cauchy-slice operators without confusing a non-manifest representation with a physical violation of relativity.

## Internal damping and Lorentzian base dynamics

The fixed-point realization gives the cleanest version of Lorentzian admissibility. The base $`Y^4`$ is Lorentzian and carries hyperbolic dynamics. The internal space $`X^6`$ is compact Riemannian and carries the positive damping operator:
``` math
\begin{equation}
  A_{\rm int}\ge0.
\end{equation}
```

Thus the finite filter is
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}},
\end{equation}
```
not
``` math
\begin{equation}
  \mathrm e^{-\tau\Box_Y}.
\end{equation}
```

The four-dimensional base dynamics remain governed by Lorentzian equations. The internal modes appear after dimensional reduction as effective mass towers:
``` math
\begin{equation}
  m_j^2=m_0^2+\mu_j^2,
\end{equation}
```
with admissibility weights
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{the Lorentzian base remains hyperbolic while internal modes are finitely filtered.}
  }
  \label{eq:base-hyperbolic-internal-filtered-section7}
\end{equation}
```

This is the clean FP/MTT answer to the Lorentzian divide.

## The role of $`\varepsilon`$-base regularization

Some fixed-point constructions introduce a regularized operator of the schematic form
``` math
\begin{equation}
  A_\varepsilon
  =
  A_{\rm int}
  +
  \varepsilon A_{\rm base},
  \qquad
  \varepsilon\ge0.
  \label{eq:Aepsilon-section7}
\end{equation}
```
Here $`A_{\rm base}`$ may be a positive spatial or Euclideanized base operator used for analytic control.

The physical Lorentzian interpretation must distinguish two cases.

If
``` math
\begin{equation}
  \varepsilon=0,
\end{equation}
```
then the finite damping is purely internal:
``` math
\begin{equation}
  A_\varepsilon=A_{\rm int}.
\end{equation}
```
This is the clean fiber-damping reading.

If
``` math
\begin{equation}
  \varepsilon>0,
\end{equation}
```
then base regularization has been introduced. This may be a useful analytic device, but it is not automatically a physical Lorentzian damping mechanism. One must show that the base operator is positive on a Cauchy slice or otherwise physically admissible.

Thus:
``` math
\begin{equation}
  \boxed{
  \varepsilon>0
  \text{ requires a separate Lorentzian admissibility justification.}
  }
  \label{eq:epsilon-requires-justification-section7}
\end{equation}
```

The safest physical default is:
``` math
\begin{equation}
  \boxed{
  \varepsilon=0
  \quad
  \text{for fundamental fiber damping.}
  }
  \label{eq:epsilon-zero-section7}
\end{equation}
```

## Spatial filters and Hamiltonian evolution

A second Lorentzian-admissible route uses spatial filters on Hamiltonian data. Let
``` math
\begin{equation}
  (\phi,\pi)
\end{equation}
```
be canonical data on $`\Sigma_t`$. A positive spatial operator
``` math
\begin{equation}
  A_\Sigma\ge0
\end{equation}
```
may define a finite filter
``` math
\begin{equation}
  B_\Sigma
  =
  P_\Sigma\chi(A_\Sigma)
  \mathrm e^{-\tau A_\Sigma}
  \chi(A_\Sigma)P_\Sigma.
  \label{eq:spatial-filter-section7}
\end{equation}
```

The filtered data are
``` math
\begin{equation}
  (\phi,\pi)
  \mapsto
  (B_\Sigma\phi,B_\Sigma\pi),
\end{equation}
```
or a sector-specific variant.

The subsequent time evolution remains hyperbolic:
``` math
\begin{equation}
  \partial_t
  \begin{pmatrix}
    \phi\\
    \pi
  \end{pmatrix}
  =
  \mathcal H
  \begin{pmatrix}
    \phi\\
    \pi
  \end{pmatrix}.
\end{equation}
```

In this picture, finite coherent projection prepares or constrains admissible data, while the base dynamics remain Lorentzian.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{spatial filtering of Cauchy data is admissible when it preserves the physical constraint
  and energy spaces.}
  }
\end{equation}
```

## Gauge constraints on Cauchy slices

Gauge fields have constraints on Cauchy data. For electromagnetism, Gauss law is
``` math
\begin{equation}
  \nabla\cdot\mathbf E=\rho.
\end{equation}
```
A finite spatial or internal filter must preserve this constraint or act after projection to the physical transverse sector.

Thus a gauge-safe Cauchy-slice filter has the schematic form
``` math
\begin{equation}
  B_{\Sigma}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_\Sigma^{\rm gauge})
  \mathrm e^{-\tau A_\Sigma^{\rm gauge}}
  \chi(A_\Sigma^{\rm gauge})P_{\rm phys}.
  \label{eq:gauge-cauchy-filter-section7}
\end{equation}
```

Here $`P_{\rm phys}`$ may be a transverse projector, BRST cohomology projection, or another quotient-compatible physical-sector map.

The rule is:
``` math
\begin{equation}
  \boxed{
  \text{Cauchy-slice filtering must not turn constraint-violating gauge data into physical data.}
  }
  \label{eq:gauge-cauchy-rule-section7}
\end{equation}
```

## Gravity constraints on Cauchy slices

In gravity, Cauchy data consist of spatial geometry and extrinsic curvature:
``` math
\begin{equation}
  (h_{ij},K_{ij})
\end{equation}
```
on a spatial slice $`\Sigma_t`$. These data must satisfy the Hamiltonian and momentum constraints:
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
\end{equation}
```

A gravitational finite filter must preserve the constraint surface or act after reduction to physical/diffeomorphism-compatible data:
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}
  =
  P_{\rm diff}\chi(A_\Sigma^{\rm grav})
  \mathrm e^{-\tau A_\Sigma^{\rm grav}}
  \chi(A_\Sigma^{\rm grav})P_{\rm diff}.
  \label{eq:gravity-cauchy-filter-section7}
\end{equation}
```

In weak-field settings, $`P_{\rm diff}`$ may reduce to a transverse-traceless projector. In full gravity, it must encode diffeomorphism and Hamiltonian constraint compatibility.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravitational finite filtering must act on admissible spatial geometry, not arbitrary
  metric components.}
  }
  \label{eq:gravity-cauchy-rule-section7}
\end{equation}
```

## Locality in total space

The fixed-point realization gives a geometric reading of effective nonlocality.

In the total space
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
finite coherent structure may be local or controlled in the internal/fiber directions. When projected to the observed base $`Y^4`$, it may appear as:

1.  finite source profiles;

2.  finite detector response;

3.  form factors;

4.  suppressed internal-mode towers;

5.  non-pointlike local shadows;

6.  effective finite overlaps.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional nonlocality can be the shadow of locality or finite controlled support
  in the total/fibered space.}
  }
  \label{eq:nonlocality-shadow-section7}
\end{equation}
```

This is not arbitrary action at a distance. It is projection-induced finite support.

## Finite coherent width

The coherent width is
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau}.
\end{equation}
```
In the fixed-point realization,
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
and if
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2},
\end{equation}
```
then
``` math
\begin{equation}
  \ell_{\rm coh}
  \sim
  R
  \sqrt{\log\frac{C_Q}{\epsilon_{\rm adm}}}.
\end{equation}
```

Thus the finite coherent width is an internal geometric length scale. The four-dimensional delta approximation is valid when this internal width is below observational resolution:
``` math
\begin{equation}
  \ell_{\rm coh}\ll\ell_{\rm res}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{Dirac deltas are low-resolution shadows of finite internal coherent width.}
  }
  \label{eq:deltas-low-resolution-section7}
\end{equation}
```

## Lorentzian admissibility checklist

A Lorentzian finite-kernel construction is admissible only if the following checks pass:

1.  The damping operator is positive in the relevant sector.

2.  No naive indefinite $`\mathrm e^{-\tau\Box}`$ is used as a fundamental filter.

3.  Equal-time kernels are bounded on the relevant energy or Sobolev spaces.

4.  The hyperbolic principal symbol is unchanged.

5.  The finite propagation cone is preserved.

6.  Gauge constraints are preserved in gauge sectors.

7.  Diffeomorphism and Hamiltonian constraints are preserved in gravity.

8.  The construction does not allow controllable superluminal signaling.

9.  Observable predictions are independent of unphysical Lens choices or transform consistently under changes of representative.

This checklist is part of the theory, not an afterthought.

## Failure modes

Lorentzian admissibility fails if:

1.  $`A=\Box`$ is used without a positive physical-sector replacement;

2.  a finite kernel modifies the principal hyperbolic symbol in an uncontrolled way;

3.  an equal-time kernel is unbounded on the energy space;

4.  gauge or gravitational constraints are broken;

5.  base diffusion is treated as physical without a Lorentzian justification;

6.  foliation dependence enters observable predictions without compensation;

7.  finite overlap is used to transmit controllable signals outside the causal cone.

In these cases, the finite kernel is not an admissible MTT object. It is an invalid Lorentzian nonlocal modification.

## Summary

MTT resolves the Lorentzian divide by refusing to identify finite coherent damping with naive spacetime heat flow:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  }
\end{equation}
```
as the fundamental Lorentzian damping operator.

Instead, admissible Lorentzian MTT uses:
``` math
\begin{equation}
  \boxed{
  \text{positive internal fiber operators, positive spatial Cauchy-slice operators, Hamiltonian
  or constraint-compatible operators, and bounded equal-time kernels.}
  }
\end{equation}
```

In the fixed-point realization:
``` math
\begin{equation}
  A=A_{\rm int}\ge0,
\end{equation}
```
so damping acts on internal fiber modes:
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
\end{equation}
```

Equal-time Cauchy kernels are admissible when they are bounded lower-order operators that do not change the hyperbolic principal symbol. Therefore they can preserve finite propagation speed and the usual domains of dependence.

The conceptual result is:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional finite nonlocality is a projection shadow of controlled finite
  coherent structure, not a license for acausal propagation.}
  }
\end{equation}
```

This Lorentzian admissibility principle will be used in the gauge and gravity sections that follow.

# Gauge and electromagnetism as quotient-compatible projection shadows

The previous sections established the finite coherent admissibility operator, its Circle–Lens–Nil reading, the delta/wave/measurement shadows, the scattering interpretation, and the Lorentzian admissibility principle. We now apply the same architecture to gauge theory and electromagnetism.

Gauge theory is the paradigmatic Lens sector. Its defining feature is that the variables used locally are not themselves unique physical objects. They are representatives of equivalence classes. Therefore an MTT finite filter is admissible in a gauge sector only if it respects the gauge quotient.

The central rule is:
``` math
\begin{equation}
  \boxed{
  \text{filter after quotienting, or filter covariantly before quotienting}.
  }
  \label{eq:gauge-safe-rule-section8}
\end{equation}
```

Equivalently, the gauge-sector finite coherent admissibility operator must have the schematic form
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
  \label{eq:gauge-Badm-section8}
\end{equation}
```
Here $`P_{\rm phys}`$ projects to gauge-admissible physical content, and $`A_{\rm gauge}`$ is a positive or gauge-compatible admissibility operator on that physical content.

This section develops this rule and explains electromagnetism as a combined Lens–Circle–Nil projection shadow.

## Gauge redundancy as Lens structure

In Abelian gauge theory, the gauge potential transforms as
``` math
\begin{equation}
  A_\mu
  \mapsto
  A_\mu+\partial_\mu\alpha.
  \label{eq:U1-gauge-transform-section8}
\end{equation}
```
The field strength is
``` math
\begin{equation}
  F_{\mu\nu}
  =
  \partial_\mu A_\nu-\partial_\nu A_\mu.
\end{equation}
```
It is invariant under <a href="#eq:U1-gauge-transform-section8" data-reference-type="eqref" data-reference="eq:U1-gauge-transform-section8">[eq:U1-gauge-transform-section8]</a>:
``` math
\begin{equation}
  F_{\mu\nu}
  \mapsto
  F_{\mu\nu}.
\end{equation}
```

Thus $`A_\mu`$ is not itself a unique physical object. It is a local representative. The physical content is encoded in gauge-invariant or gauge-covariant structures such as:

1.  field strengths;

2.  Wilson loops and holonomies;

3.  conserved-current amplitudes;

4.  physical transverse modes;

5.  BRST cohomology classes;

6.  gauge-invariant composite observables.

In MTT language:
``` math
\begin{equation}
  \boxed{
  \mathsf L_{\rm gauge}
  =
  \text{local representative modulo gauge equivalence}.
  }
\end{equation}
```

Therefore, a finite coherent filter cannot treat all components of $`A_\mu`$ as physical degrees of freedom. Pure-gauge directions are Lens redundancy, not physical modes to be damped or retained.

## Physical-sector projection

The gauge-sector projector
``` math
\begin{equation}
  P_{\rm phys}
\end{equation}
```
selects physical, gauge-admissible content. In a simple Abelian flat-space setting this may be represented by projection to transverse modes. In momentum space, define
``` math
\begin{equation}
  P_T^{\mu\nu}(k)
  =
  \eta^{\mu\nu}
  -
  \frac{k^\mu k^\nu}{k^2},
  \qquad
  k^2\neq0,
  \label{eq:transverse-projector-section8}
\end{equation}
```
with the appropriate Euclidean or physical transverse interpretation.

It satisfies
``` math
\begin{equation}
  k_\mu P_T^{\mu\nu}(k)=0,
\end{equation}
```
and
``` math
\begin{equation}
  P_T^2=P_T.
\end{equation}
```

The transverse projector removes longitudinal representative components. Thus a simple gauge-safe Abelian finite filter may be written schematically as
``` math
\begin{equation}
  B_{\rm adm}^{\rm Abelian}
  =
  P_T\chi(A_T)\mathrm e^{-\tau A_T}\chi(A_T)P_T,
  \label{eq:abelian-transverse-filter-section8}
\end{equation}
```
where $`A_T`$ is positive on the transverse physical sector.

This is the gauge analogue of the coherent projector $`P_{\rm coh}`$ in the FP internal realization. In both cases, $`P`$ removes inadmissible directions before finite damping is interpreted physically.

## Conserved currents

Electromagnetic amplitudes couple to conserved currents:
``` math
\begin{equation}
  \partial_\mu J^\mu=0,
\end{equation}
```
or in momentum space,
``` math
\begin{equation}
  k_\mu J^\mu(k)=0.
  \label{eq:current-conservation-section8}
\end{equation}
```
Because of <a href="#eq:current-conservation-section8" data-reference-type="eqref" data-reference="eq:current-conservation-section8">[eq:current-conservation-section8]</a>, longitudinal components do not contribute to physical conserved-current amplitudes:
``` math
\begin{equation}
  J_\mu k^\mu=0.
\end{equation}
```

A gauge-safe finite current-exchange amplitude may therefore be written schematically as
``` math
\begin{equation}
  \mathcal A_{\rm adm}(k)
  \sim
  e^2
  J_\mu(k)
  \frac{F_{\rm adm}(k)}{k^2}
  P_T^{\mu\nu}(k)
  J'_\nu(-k),
  \label{eq:gauge-safe-current-amplitude-section8}
\end{equation}
```
where $`F_{\rm adm}`$ is an admissible finite factor.

In a Euclidean scalar-like benchmark,
``` math
\begin{equation}
  F_{\rm adm}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```
In the FP/fiber realization, the safer physical interpretation is instead an internal-mode sum:
``` math
\begin{equation}
  F_{\rm adm}
  \quad
  \leadsto
  \quad
  \sum_j Z_j\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge-safe amplitudes damp physical or quotient-compatible content, not pure
  representative directions.}
  }
  \label{eq:gauge-safe-amplitudes-section8}
\end{equation}
```

## Fiber realization of gauge sectors

In the FP realization, gauge degrees of freedom may arise from internal geometry, internal harmonics, bundle connections, representation data, or fiber-mode sectors. The finite coherent filter acts on internal spectral data:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
with weight
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

A four-dimensional gauge boson zero mode corresponds to an undamped internal zero mode:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Massive internal gauge excitations carry weights
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2},
  \qquad
  \mu_j^2>0.
\end{equation}
```

Thus the effective four-dimensional gauge propagator may take the schematic form
``` math
\begin{equation}
  D_{\mu\nu}^{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}
  P_{\mu\nu}^{(j)}(p),
  \label{eq:gauge-KK-effective-propagator-section8}
\end{equation}
```
where $`P_{\mu\nu}^{(j)}`$ denotes the appropriate physical polarization or quotient-compatible projector for the $`j`$-th effective mode.

The zero mode recovers ordinary low-energy gauge propagation. The nonzero internal modes are admissibility-suppressed.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional gauge fields are undamped zero-mode shadows plus suppressed
  internal gauge excitations.}
  }
  \label{eq:gauge-zero-mode-shadow-section8}
\end{equation}
```

## Gauge covariance before quotienting

Sometimes it is useful to filter before explicitly projecting to the physical Hilbert space. In that case the filter must be gauge-covariant.

For a non-Abelian gauge theory with connection
``` math
\begin{equation}
  A_\mu=A_\mu^aT_a,
\end{equation}
```
the covariant derivative is
``` math
\begin{equation}
  D_\mu=\partial_\mu+[A_\mu,\cdot].
\end{equation}
```
A natural gauge-covariant positive operator is a covariant Laplacian of the schematic form
``` math
\begin{equation}
  A_{\rm YM}
  =
  -D_iD^i
  \label{eq:YM-spatial-covariant-laplacian-section8}
\end{equation}
```
on a Cauchy slice, or a positive elliptic operator on internal/gauge-covariant fiber data.

A covariant filter
``` math
\begin{equation}
  \chi(A_{\rm YM})\mathrm e^{-\tau A_{\rm YM}}\chi(A_{\rm YM})
\end{equation}
```
can be meaningful before quotienting only if it transforms compatibly under gauge transformations. The resulting physical content must then be projected or evaluated through gauge-invariant observables.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{before quotienting, the filter must be gauge-covariant;}
  }
\end{equation}
```
and:
``` math
\begin{equation}
  \boxed{
  \text{after quotienting, the filter must act on physical gauge content.}
  }
\end{equation}
```

## BRST-compatible formulation

In covariant quantization, gauge redundancy is often handled by BRST symmetry. Let
``` math
\begin{equation}
  Q_{\rm BRST}^2=0.
\end{equation}
```
The physical Hilbert space is represented by cohomology:
``` math
\begin{equation}
  \mathcal H_{\rm phys}
  =
  \ker Q_{\rm BRST}/\operatorname{im}Q_{\rm BRST}.
  \label{eq:BRST-cohomology-section8}
\end{equation}
```

A finite coherent filter is BRST-compatible if it preserves physical cohomology. A sufficient schematic condition is
``` math
\begin{equation}
  [A_{\rm gauge},Q_{\rm BRST}]=0,
  \qquad
  [P_{\rm phys},Q_{\rm BRST}]=0,
  \label{eq:BRST-compatibility-section8}
\end{equation}
```
with domain and gauge-fixing details handled in the specific theory.

If a finite filter maps BRST-closed states to non-closed states, or turns BRST-exact redundancy into physical content, it is not gauge-admissible.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{BRST-compatible MTT filtering preserves physical cohomology.}
  }
  \label{eq:BRST-compatible-filtering-section8}
\end{equation}
```

## Ward and Slavnov–Taylor constraints

Gauge theory is constrained by identities that express gauge consistency. In Abelian theory, Ward identities encode current conservation and gauge invariance. In non-Abelian theory, Slavnov–Taylor identities encode the corresponding BRST/gauge constraints.

A finite coherent filter must preserve these identities. Therefore $`A_{\rm gauge}`$, $`P_{\rm
phys}`$, $`\chi`$, and $`\tau`$ cannot be chosen arbitrarily.

A filter that damps physical transverse modes while preserving Ward identities may be admissible. A filter that treats longitudinal pure-gauge modes as physical, or breaks current conservation, is not.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge admissibility requires identity preservation, not merely high-mode damping.}
  }
  \label{eq:gauge-identity-preservation-section8}
\end{equation}
```

This is one of the central ways in which MTT finite filtering differs from arbitrary regularization.

## Electromagnetism as Lens–Circle–Nil structure

Electromagnetism realizes all three MTT modes.

Lens is gauge redundancy:
``` math
\begin{equation}
  A_\mu\sim A_\mu+\partial_\mu\alpha.
\end{equation}
```
The potential is a local representative. The physical content is gauge-compatible.

Circle is electromagnetic phase and holonomy:
``` math
\begin{equation}
  \exp\left(\mathrm iq\oint_\gamma A\right).
  \label{eq:EM-holonomy-section8}
\end{equation}
```
This phase can be physically observable even when the local field strength vanishes along the path, as in holonomy-type effects.

Nil is charge-sector selection, photon-number records, detector clicks, and damping of inadmissible or noncoherent gauge modes:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{align}
  \mathsf L_{\rm EM}
  &: \text{gauge representative and quotient},\\
  \mathsf C_{\rm EM}
  &: \text{phase, flux, holonomy},\\
  \mathsf N_{\rm EM}
  &: \text{charge sectors, photon records, detector outcomes}.
\end{align}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{electromagnetism}
  =
  \mathsf L\text{-gauge}
  +
  \mathsf C\text{-phase/holonomy}
  +
  \mathsf N\text{-charge and photon records}.
  }
  \label{eq:EM-CLN-box-section8}
\end{equation}
```

## Aharonov–Bohm-type phase as Circle shadow

The phase
``` math
\begin{equation}
  \exp\left(\mathrm iq\oint_\gamma A\right)
\end{equation}
```
is gauge-compatible because under
``` math
\begin{equation}
  A\mapsto A+\,\mathrm d\alpha
\end{equation}
```
one has
``` math
\begin{equation}
  \oint_\gamma \,\mathrm d\alpha=0
\end{equation}
```
for a closed loop with single-valued gauge function.

Thus the loop phase is not merely a local representative artifact. It is a Circle holonomy shadow of gauge structure:
``` math
\begin{equation}
  \boxed{
  \text{electromagnetic phase}
  =
  \mathsf C\text{-holonomy read through }\mathsf L\text{-gauge representatives}.
  }
\end{equation}
```

This is why gauge potentials cannot simply be dismissed as unphysical. They are representatives, but their global holonomy can encode physical phase information.

## Flux quantization and charge sectors

Gauge theory also exhibits quantized global labels. For suitable closed two-surfaces $`\Sigma`$, flux quantization has the schematic form
``` math
\begin{equation}
  \frac{1}{2\pi}\int_\Sigma F\in\mathbb Z.
  \label{eq:flux-quantization-section8}
\end{equation}
```
For a magnetic monopole, Dirac quantization gives
``` math
\begin{equation}
  eg=2\pi n,
  \qquad
  n\in\mathbb Z,
  \label{eq:dirac-monopole-section8}
\end{equation}
```
in units where $`\hbar=c=1`$.

In MTT language, these integers are Lens–Circle consistency labels. They arise because local gauge representatives must glue globally in a phase-consistent way.

Charge-sector records and photon-number detections add the Nil component:
``` math
\begin{equation}
  \text{charge or photon record}
  =
  \text{survivor label in a detector or sectoral basin}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge quantization}
  =
  \mathsf C\text{-phase closure}
  +
  \mathsf L\text{-bundle consistency}
  +
  \mathsf N\text{-sector survival}.
  }
  \label{eq:gauge-quantization-section8}
\end{equation}
```

## Finite charge sources

A point charge is usually written as
``` math
\begin{equation}
  \rho(\mathbf r)=q\delta^{(3)}(\mathbf r).
\end{equation}
```
MTT treats this as a sharp shadow of a finite coherent charge profile. A simple Euclidean finite-source model is
``` math
\begin{equation}
  \rho_\tau(\mathbf r)
  =
  q(4\pi\tau)^{-3/2}
  \exp\left(-\frac{r^2}{4\tau}\right).
  \label{eq:finite-charge-profile-section8}
\end{equation}
```
It preserves total charge:
``` math
\begin{equation}
  \int_{\mathbb R^3}\rho_\tau(\mathbf r)\,\,\mathrm d^3r=q.
\end{equation}
```

The corresponding Coulomb-like potential is
``` math
\begin{equation}
  \Phi_\tau(r)
  =
  \frac{q}{4\pi r}
  \operatorname{erf}
  \left(
    \frac{r}{2\sqrt{\tau}}
  \right).
  \label{eq:finite-coulomb-section8}
\end{equation}
```
At large radius,
``` math
\begin{equation}
  r\gg\sqrt{\tau},
\end{equation}
```
one recovers the usual Coulomb potential:
``` math
\begin{equation}
  \Phi_\tau(r)\sim\frac{q}{4\pi r}.
\end{equation}
```
At small radius, the singularity is softened.

However, in the FP/fiber realization this formula should be read as a benchmark finite-source model, not automatically as a universal four-dimensional Coulomb correction. If the finite width is primarily internal, then four-dimensional Coulomb corrections arise through internal mode exchange and finite overlap, not by direct spatial smearing of $`\mathbf r`$ unless a physical four-dimensional finite source is derived.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite Coulomb smearing is a benchmark; FP-realized electromagnetic corrections are
  internal-mode and overlap effects unless a 4D source profile is derived.}
  }
  \label{eq:finite-coulomb-caution-section8}
\end{equation}
```

## Photon records

A photon detection event is not merely the presence of a mode. It is a measurement record. In MTT terms, photon detection involves:

1.  a gauge-compatible electromagnetic field sector;

2.  a finite detector effect $`E_i^{(\mathsf M)}`$;

3.  branch or mode damping due to the detector/environment;

4.  survivor-basin stabilization into a record.

The measurement chain is
``` math
\begin{equation}
  \rho_{\rm EM}
  \to
  D^{(\mathsf M)}\circ\rho_{\rm EM}
  \to
  B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{photon}
  =
  \text{gauge-compatible excitation shadow plus detector survivor record}.
  }
  \label{eq:photon-record-section8}
\end{equation}
```

The wave aspect of light is the Circle-coherent spectral field. The particle aspect is the Nil-stabilized detector record. Gauge structure is the Lens quotient behind both.

## Non-Abelian gauge sectors

For non-Abelian gauge theory, the gauge potential is Lie-algebra-valued:
``` math
\begin{equation}
  A_\mu=A_\mu^aT_a.
\end{equation}
```
Gauge transformations are nonlinear, and the field strength is
``` math
\begin{equation}
  F_{\mu\nu}
  =
  \partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu].
\end{equation}
```

The finite admissibility operator must respect the non-Abelian quotient structure:
``` math
\begin{equation}
  B_{\rm adm}^{\rm YM}
  =
  P_{\rm phys}\chi(A_{\rm YM})
  \mathrm e^{-\tau A_{\rm YM}}
  \chi(A_{\rm YM})P_{\rm phys}.
  \label{eq:YM-Badm-section8}
\end{equation}
```

Compared with Abelian theory, several new issues appear:

1.  field-dependent gauge orbits;

2.  ghost sectors;

3.  Gribov ambiguity;

4.  BRST cohomology;

5.  Slavnov–Taylor identities;

6.  anomaly cancellation in chiral sectors;

7.  confinement or nonperturbative sector structure.

Thus non-Abelian MTT filtering is not obtained by simply multiplying propagators by a Gaussian factor. It must be derived in a gauge-compatible physical sector.

## Standard Model gauge execution

A full Standard Model gauge implementation must recover
``` math
\begin{equation}
  SU(3)\times SU(2)\times U(1),
\end{equation}
```
matter representations, chirality, anomaly cancellation, electroweak symmetry breaking, mixing, confinement, and precision scattering data.

In MTT terms, this requires deriving or specifying:
``` math
\begin{equation}
  A_{\rm SM},
  \qquad
  P_{\rm phys}^{\rm SM},
  \qquad
  \chi_{\rm SM},
  \qquad
  \tau_{\rm SM}.
\end{equation}
```

The fixed-point/fiber realization may provide a geometric source of representation and mode data, but the present paper does not claim to complete the Standard Model derivation. It identifies the form such a derivation must take.

The minimum requirements are:

1.  correct gauge group;

2.  correct representations;

3.  anomaly cancellation;

4.  gauge-identity preservation;

5.  correct low-energy zero-mode physics;

6.  admissibly suppressed nonzero internal modes;

7.  compatibility with collider and precision constraints.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{Standard Model closure is an execution task, not assumed by the structural theorem.}
  }
  \label{eq:SM-execution-task-section8}
\end{equation}
```

## Gauge-sector failure modes

The MTT gauge construction fails if:

1.  pure-gauge modes are treated as physical;

2.  $`P_{\rm phys}`$ is not quotient-compatible;

3.  $`A_{\rm gauge}`$ breaks gauge covariance or gauge constraints;

4.  the spectral window $`\chi(A_{\rm gauge})`$ breaks gauge identities;

5.  Ward or Slavnov–Taylor identities fail;

6.  current conservation is violated;

7.  BRST cohomology is not preserved;

8.  anomaly cancellation is broken;

9.  Lorentzian damping is implemented by an inadmissible $`\mathrm e^{-\tau\Box}`$ factor.

In such cases, the finite filter is not an MTT gauge object. It is an inadmissible regulator.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{gauge-sector admissibility is a quotient and identity-preservation condition.}
  }
  \label{eq:gauge-admissibility-summary-section8}
\end{equation}
```

## Summary

Gauge theory is the paradigmatic Lens sector of MTT. The local variables are representatives, not unique physical objects:
``` math
\begin{equation}
  A_\mu\sim A_\mu+\partial_\mu\alpha.
\end{equation}
```

Therefore the finite coherent admissibility operator must be gauge-compatible:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
  }
\end{equation}
```

The safe rule is:
``` math
\begin{equation}
  \boxed{
  \text{filter after quotienting, or filter covariantly before quotienting}.
  }
\end{equation}
```

Electromagnetism combines all three MTT components:
``` math
\begin{align}
  \mathsf L_{\rm EM}
  &: \text{gauge representatives and quotienting},\\
  \mathsf C_{\rm EM}
  &: \text{phase, flux, and holonomy},\\
  \mathsf N_{\rm EM}
  &: \text{charge sectors, photon records, and detector outcomes}.
\end{align}
```

In the fixed-point/fiber realization, ordinary four-dimensional gauge fields arise as undamped zero-mode shadows, while nonzero internal gauge excitations are admissibility suppressed:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{electromagnetism is gauge-compatible finite coherent admissibility read through
  Lens quotienting, Circle phase, and Nil records.}
  }
\end{equation}
```

# Gravity as diffeomorphism-compatible geometric projection

Gauge theory is Lens structure over fields on spacetime. Gravity is deeper: it is Lens structure acting on spacetime geometry itself. In general relativity, the metric is not a field living on a fixed physical stage in the same way as an ordinary matter field. The metric helps define the stage. Coordinate-related metric descriptions represent the same physical geometry:
``` math
\begin{equation}
  g_{\mu\nu}\sim\varphi^\ast g_{\mu\nu}.
  \label{eq:diff-equivalence-section9}
\end{equation}
```

Therefore, a finite coherent admissibility operator in gravity cannot act on arbitrary metric components as if they were all physical. It must act on diffeomorphism-compatible geometric content.

The schematic gravitational operator is
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
  \label{eq:grav-Badm-section9}
\end{equation}
```
Here $`P_{\rm diff}`$ is a diffeomorphism-compatible projector or reduction map, and $`A_{\rm grav}`$ is a positive or constraint-compatible geometric admissibility operator.

The central rule is:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent filtering in gravity must preserve diffeomorphism-compatible
  geometric content.}
  }
  \label{eq:gravity-safe-rule-section9}
\end{equation}
```

## Diffeomorphism redundancy as Lens structure

A diffeomorphism
``` math
\begin{equation}
  \varphi:M\to M
\end{equation}
```
acts on the metric by pullback:
``` math
\begin{equation}
  g_{\mu\nu}\mapsto\varphi^\ast g_{\mu\nu}.
\end{equation}
```
The two metric representatives describe the same geometry if they are related by an allowed diffeomorphism.

Thus coordinates are not physical labels by themselves. They are Lens representatives.

In MTT language:
``` math
\begin{equation}
  \boxed{
  \mathsf L_{\rm grav}
  =
  \text{coordinate representation modulo diffeomorphism equivalence}.
  }
\end{equation}
```

This makes gravity the most radical Lens sector. Gauge theory has redundancy over a fixed base. Gravity has redundancy in the representation of the base geometry itself.

Therefore the gravitational finite filter cannot be:
``` math
\begin{equation}
  \text{``smooth each metric component in coordinates.''}
\end{equation}
```
That would be coordinate-dependent and generally inadmissible. The admissible operation must be geometric:
``` math
\begin{equation}
  \boxed{
  \text{filter geometric content, not coordinate artifacts.}
  }
  \label{eq:filter-geometric-content-section9}
\end{equation}
```

## Why $`A_{\rm grav}\neq\Box_g`$ as a naive heat operator

The Lorentzian d’Alembertian
``` math
\begin{equation}
  \Box_g
\end{equation}
```
is hyperbolic and indefinite. A naive expression
``` math
\begin{equation}
  \mathrm e^{-\tau\Box_g}
\end{equation}
```
is not a positive heat-kernel damping operator. In gravity this is even more dangerous than in ordinary field theory, because the operator itself depends on the dynamical metric.

Thus MTT does not define gravitational finite admissibility by naive spacetime heat flow:
``` math
\begin{equation}
  \boxed{
  A_{\rm grav}\neq\Box_g
  \quad
  \text{as a fundamental Lorentzian damping operator.}
  }
  \label{eq:Agrav-not-box-section9}
\end{equation}
```

Instead, $`A_{\rm grav}`$ must be one of the following:

1.  a positive spatial operator on Cauchy-slice geometric data;

2.  a positive operator on transverse-traceless perturbative modes;

3.  a constraint-compatible operator on canonical data;

4.  a geometric elliptic operator in a Euclidean or positive spectral chart;

5.  an internal/fiber geometric operator that contributes to effective gravitational sectors;

6.  a reduced operator acting after diffeomorphism quotienting.

The safe gravitational rule is:
``` math
\begin{equation}
  \boxed{
  \text{use positive geometric admissibility data after constraints or quotienting, not indefinite
  Lorentzian damping.}
  }
  \label{eq:positive-grav-data-section9}
\end{equation}
```

## ADM/Cauchy-slice formulation

On a globally hyperbolic spacetime, one may foliate the geometry by spacelike Cauchy slices:
``` math
\begin{equation}
  Y^4\cong\mathbb R\times\Sigma.
\end{equation}
```
The gravitational data on a slice $`\Sigma_t`$ are the spatial metric and extrinsic curvature:
``` math
\begin{equation}
  (h_{ij},K_{ij}).
\end{equation}
```

Equivalently, in Hamiltonian variables, one uses
``` math
\begin{equation}
  (h_{ij},\pi^{ij}),
\end{equation}
```
where $`\pi^{ij}`$ is the momentum conjugate to $`h_{ij}`$.

The data cannot be arbitrary. They must satisfy the gravitational constraints:
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
  \label{eq:ADM-constraints-section9}
\end{equation}
```
The Hamiltonian constraint $`\mathcal H=0`$ and momentum constraints $`\mathcal H_i=0`$ encode the diffeomorphism structure of general relativity.

Thus a gravitational finite filter must act on:
``` math
\begin{equation}
  \text{constraint-compatible Cauchy data}
\end{equation}
```
rather than arbitrary metric components.

The Cauchy-slice gravitational filter has the schematic form
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\Sigma}^{\rm grav})
  \mathrm e^{-\tau A_{\Sigma}^{\rm grav}}
  \chi(A_{\Sigma}^{\rm grav})P_{\rm diff}.
  \label{eq:grav-cauchy-filter-section9}
\end{equation}
```

Here:
``` math
\begin{align}
  P_{\rm diff}
  &: \text{projects to diffeomorphism- or constraint-compatible content},\\
  A_{\Sigma}^{\rm grav}
  &: \text{positive spatial/geometric admissibility operator},\\
  \chi(A_{\Sigma}^{\rm grav})
  &: \text{admissible spectral window},\\
  \mathrm e^{-\tau A_{\Sigma}^{\rm grav}}
  &: \text{finite damping of inadmissible geometric modes}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravity-sector MTT filtering is naturally ADM/Cauchy-slice compatible.}
  }
  \label{eq:ADM-compatible-filtering-section9}
\end{equation}
```

## Constraint preservation

The constraint surface is not optional. Let
``` math
\begin{equation}
  \mathcal C_{\rm grav}
  =
  \{(h_{ij},\pi^{ij}):\mathcal H=0,\mathcal H_i=0\}.
\end{equation}
```
A gravitational finite filter is admissible only if it preserves this surface or acts on a reduced physical quotient:
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}:
  \mathcal C_{\rm grav}\to\mathcal C_{\rm grav},
  \label{eq:constraint-preservation-section9}
\end{equation}
```
or, more generally,
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}:
  \mathcal C_{\rm grav}/\mathrm{Diff}
  \to
  \mathcal C_{\rm grav}/\mathrm{Diff}.
\end{equation}
```

In an operator language, one expects compatibility conditions of the schematic form
``` math
\begin{equation}
  [A_{\Sigma}^{\rm grav},\widehat{\mathcal H}]\approx0,
  \qquad
  [A_{\Sigma}^{\rm grav},\widehat{\mathcal H}_i]\approx0,
  \label{eq:constraint-commutators-section9}
\end{equation}
```
or a weaker condition that the full projected operator preserves physical equivalence classes.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{a gravitational finite filter is admissible only if it preserves the constraint structure.}
  }
  \label{eq:constraint-structure-box-section9}
\end{equation}
```

This is the gravitational analogue of preserving Ward or Slavnov–Taylor identities in gauge theory.

## Linearized gravity and transverse-traceless projection

In weak-field gravity, one expands around a background metric:
``` math
\begin{equation}
  g_{\mu\nu}
  =
  \bar g_{\mu\nu}+h_{\mu\nu}.
\end{equation}
```
For a flat background,
``` math
\begin{equation}
  \bar g_{\mu\nu}=\eta_{\mu\nu}.
\end{equation}
```

At linear order, infinitesimal diffeomorphisms act as
``` math
\begin{equation}
  h_{\mu\nu}
  \mapsto
  h_{\mu\nu}
  +
  \partial_\mu\xi_\nu
  +
  \partial_\nu\xi_\mu.
  \label{eq:linearized-diff-section9}
\end{equation}
```
Thus not all components of $`h_{\mu\nu}`$ are physical.

In a flat perturbative setting, the physical graviton degrees of freedom are represented by transverse-traceless data:
``` math
\begin{equation}
  h_{ij}^{\rm TT}.
\end{equation}
```
They satisfy
``` math
\begin{equation}
  \partial^i h_{ij}^{\rm TT}=0,
  \qquad
  \delta^{ij}h_{ij}^{\rm TT}=0.
\end{equation}
```

A weak-field gravitational finite filter can therefore be written schematically as
``` math
\begin{equation}
  B_{\rm grav}^{\rm lin}
  =
  P_{\rm TT}\chi(A_{\rm TT})
  \mathrm e^{-\tau A_{\rm TT}}
  \chi(A_{\rm TT})P_{\rm TT},
  \label{eq:linearized-grav-filter-section9}
\end{equation}
```
where $`P_{\rm TT}`$ is the transverse-traceless projector and $`A_{\rm TT}\ge0`$ is a positive operator on the TT sector.

For example, on a spatial Cauchy slice one may use
``` math
\begin{equation}
  A_{\rm TT}=-\Delta_\Sigma
\end{equation}
```
restricted to TT data, or a Lichnerowicz-type operator in a curved background.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{weak-field gravitational filtering acts on physical spin-2 data, not pure
  diffeomorphism modes.}
  }
  \label{eq:weak-field-spin2-filtering-section9}
\end{equation}
```

## Lichnerowicz-type geometric operators

On a curved background $`(M,\bar g)`$, a natural elliptic operator on symmetric two-tensors is a Lichnerowicz-type operator. In one common convention,
``` math
\begin{equation}
  (\Delta_L h)_{\mu\nu}
  =
  -\nabla^2 h_{\mu\nu}
  -
  2R_{\mu\rho\nu\sigma}h^{\rho\sigma}
  +
  R_\mu{}^\rho h_{\rho\nu}
  +
  R_\nu{}^\rho h_{\mu\rho}.
  \label{eq:Lichnerowicz-section9}
\end{equation}
```
The exact form depends on sign conventions and on the chosen gauge-fixed gravitational sector.

The important point is not this particular formula. The important point is that $`A_{\rm grav}`$ must be:

1.  geometric;

2.  positive or controlled on the relevant sector;

3.  compatible with constraints;

4.  compatible with diffeomorphism quotienting;

5.  compatible with the Lorentzian admissibility principle.

Thus:
``` math
\begin{equation}
  \boxed{
  A_{\rm grav}
  =
  \text{positive or constraint-compatible geometric stabilization operator}.
  }
  \label{eq:Agrav-geometric-section9}
\end{equation}
```

## Finite graviton propagator shadow

In a weak-field positive spectral chart, one may write a schematic finite graviton propagator shadow:
``` math
\begin{equation}
  D_{\mu\nu\rho\sigma}^{\rm adm}(k)
  \sim
  \frac{F_{\rm adm}(k)}{k^2}
  P_{\mu\nu\rho\sigma}^{\rm TT}(k),
  \label{eq:finite-graviton-propagator-section9}
\end{equation}
```
where $`P^{\rm TT}`$ is the physical spin-2 projector and $`F_{\rm adm}`$ is an admissible finite factor.

In a Euclidean or positive spatial benchmark,
``` math
\begin{equation}
  F_{\rm adm}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```
In the FP/fiber realization, the safer interpretation is internal-mode damping:
``` math
\begin{equation}
  F_{\rm adm}
  \leadsto
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
for gravitational or geometry-coupled internal modes.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite graviton propagation is meaningful only after physical spin-2 or geometric
  projection.}
  }
  \label{eq:finite-graviton-after-projection-section9}
\end{equation}
```

A damping factor applied directly to all metric components is not admissible.

## Geometry-dependent heat kernels

For a fixed Riemannian geometry and a positive geometric operator $`A_g`$, the finite heat kernel has the form
``` math
\begin{equation}
  K_g(x,y;\tau)
  =
  \langle x|
  \mathrm e^{-\tau A_g}
  |y\rangle.
\end{equation}
```
For small $`\tau`$, the local heat-kernel expansion has the schematic structure
``` math
\begin{equation}
  K_g(x,y;\tau)
  \sim
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{\sigma_g(x,y)}{2\tau}
  \right)
  \Delta_g^{1/2}(x,y)
  \left[
    1+\tau a_1(x,y)+\tau^2a_2(x,y)+\cdots
  \right],
  \label{eq:geometry-heat-kernel-section9}
\end{equation}
```
where $`\sigma_g(x,y)`$ is Synge’s world function and $`\Delta_g(x,y)`$ is the Van Vleck determinant.

This expression shows that finite kernels in gravity are shaped by geometry. They depend on:

1.  geodesic distance;

2.  curvature;

3.  volume measure;

4.  parallel transport;

5.  boundary conditions;

6.  topology.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{a gravitational finite kernel is a geometry-dependent coherent response, not a flat
  Gaussian pasted onto spacetime.}
  }
  \label{eq:geometry-dependent-response-section9}
\end{equation}
```

## Curvature as Circle holonomy

Gravity has a natural Circle component: curvature is holonomy.

Parallel transport around a loop $`\gamma`$ acts as
``` math
\begin{equation}
  v^\mu
  \mapsto
  \mathcal P
  \exp\left(
    \oint_\gamma \Gamma
  \right)
  v^\mu.
\end{equation}
```
Infinitesimally,
``` math
\begin{equation}
  [\nabla_\mu,\nabla_\nu]v^\rho
  =
  R^\rho{}_{\sigma\mu\nu}v^\sigma.
  \label{eq:curvature-commutator-section9}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  R^\rho{}_{\sigma\mu\nu}
  =
  \text{infinitesimal Circle holonomy of local frame transport}.
  }
  \label{eq:curvature-circle-box-section9}
\end{equation}
```

The gravitational triplet becomes:
``` math
\begin{align}
  \mathsf L_{\rm grav}
  &: \text{diffeomorphism quotient and coordinate representation},\\
  \mathsf C_{\rm grav}
  &: \text{curvature and frame holonomy},\\
  \mathsf N_{\rm grav}
  &: \text{boundary, horizon, singularity, survivor geometry}.
\end{align}
```

## Nil boundaries and survivor geometries

Nil appears in gravity whenever geometric continuation, admissibility, or observation reaches a boundary or survivor condition.

Examples include:

1.  event horizons;

2.  apparent horizons;

3.  trapped surfaces;

4.  singularity formation;

5.  cosmological boundaries;

6.  asymptotic boundary conditions;

7.  topology-change restrictions;

8.  black-hole endpoint sectors.

In MTT language, a gravitational solution is a survivor geometry:
``` math
\begin{equation}
  \boxed{
  \text{gravitational solution}
  =
  \text{constraint-compatible survivor geometry}.
  }
  \label{eq:survivor-geometry-section9}
\end{equation}
```

A finite gravitational filter must therefore preserve or select admissible geometric survivors. It cannot arbitrarily smooth away a singularity, horizon, or boundary and claim success unless the resulting geometry satisfies the constraints and boundary conditions.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{singularity smoothing is meaningful only when it produces an admissible survivor
  geometry.}
  }
  \label{eq:singularity-smoothing-caution-section9}
\end{equation}
```

## Stress-energy compatibility

Finite coherent matter sources coupled to gravity must respect stress-energy conservation:
``` math
\begin{equation}
  \nabla_\mu T^{\mu\nu}=0.
  \label{eq:stress-energy-conservation-section9}
\end{equation}
```
A point-mass source idealization may be written schematically as
``` math
\begin{equation}
  T_{\mu\nu}
  \sim
  m u_\mu u_\nu \delta^{(3)}(\mathbf x-\mathbf x_0).
\end{equation}
```
MTT may replace this with a finite coherent profile:
``` math
\begin{equation}
  T_{\mu\nu}^{\rm adm}
  \sim
  m u_\mu u_\nu K_{\rm adm}(x,x_0).
\end{equation}
```

But this replacement is admissible only if the resulting source satisfies the gravitational constraints and conservation equations. Finite smearing is not arbitrary:
``` math
\begin{equation}
  \boxed{
  \text{finite stress-energy must be geometrically and dynamically consistent.}
  }
  \label{eq:finite-stress-energy-section9}
\end{equation}
```

This is the gravitational analogue of charge conservation in electromagnetism.

## Gravity and the FP internal realization

In the fixed-point realization, the internal compact geometry contributes coherent zero modes and damped nonzero internal excitations. Gravity may couple to this structure in two ways.

First, the four-dimensional gravitational sector may arise as a zero-mode geometric shadow:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Second, nonzero internal geometric or matter excitations may affect effective gravity through suppressed tower contributions:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2},
  \qquad
  \mu_j^2>0.
\end{equation}
```

Thus, in a schematic effective gravitational sector,
``` math
\begin{equation}
  G_{\rm grav}^{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j^{\rm grav}\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}
  P_j^{\rm phys}(p),
  \label{eq:grav-effective-tower-section9}
\end{equation}
```
where $`P_j^{\rm phys}`$ is the appropriate physical spin/geometric projector.

This should be read as an execution template, not as a completed quantum-gravity derivation.

The important principle is:
``` math
\begin{equation}
  \boxed{
  \text{the observed gravitational sector is the diffeomorphism-compatible zero-mode and
  survivor-geometric shadow of finite internal admissibility.}
  }
  \label{eq:gravity-zero-mode-shadow-section9}
\end{equation}
```

## Emergent locality and geometric projection

Because gravity defines geometry, locality itself is projection-sensitive. In ordinary field theory one asks whether a field is local on a fixed spacetime. In gravity, the meaning of “local” depends on the geometric sector.

MTT therefore treats gravitational locality as a Lens outcome:
``` math
\begin{equation}
  \boxed{
  \text{locality in gravity is defined after diffeomorphism-compatible geometric projection.}
  }
  \label{eq:locality-after-projection-section9}
\end{equation}
```

This matters for:

1.  horizons;

2.  entanglement across regions;

3.  black-hole interiors;

4.  bulk/boundary reconstruction;

5.  singularity resolution;

6.  spatial subregion factorization.

Thus, in gravity, the Lens component acts not only on field representation but on the representation of spacetime regions themselves.

## Entanglement and gravitational factorization

In non-gravitational quantum mechanics one often begins with
``` math
\begin{equation}
  \mathcal H_{AB}
  =
  \mathcal H_A\otimes\mathcal H_B.
\end{equation}
```
In gravity, this factorization can be subtle or fail. The decomposition into subregions depends on geometry, boundary data, constraints, and diffeomorphism-invariant definitions of location.

Thus a gravitational coherent sector may not factor:
``` math
\begin{equation}
  \mathcal H_{\rm grav}^{AB}
  \neq
  \mathcal H_{\rm grav}^{A}
  \otimes
  \mathcal H_{\rm grav}^{B}.
\end{equation}
```
Similarly,
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  \neq
  B_{\rm adm}^{A}
  \otimes
  B_{\rm adm}^{B}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{gravitational entanglement must be defined after geometric Lens projection.}
  }
  \label{eq:gravitational-entanglement-lens-section9}
\end{equation}
```

This will be revisited in the section on superposition and entanglement.

## Weak-field phenomenological template

A near-term benchmark for gravitational MTT is weak-field linearized gravity. The execution program is:

1.  choose a background $`\bar g_{\mu\nu}`$;

2.  decompose perturbations $`h_{\mu\nu}`$;

3.  project to physical transverse-traceless or constraint-compatible data;

4.  choose a positive operator $`A_{\rm TT}`$ on that sector;

5.  construct
    ``` math
    \begin{equation}
        B_{\rm grav}^{\rm lin}
        =
        P_{\rm TT}\chi(A_{\rm TT})
        \mathrm e^{-\tau A_{\rm TT}}
        \chi(A_{\rm TT})P_{\rm TT};
    \end{equation}
    ```

6.  compute finite corrections to propagation or source coupling;

7.  compare with gravitational-wave and weak-field constraints.

This is a controlled benchmark. It does not claim to solve full quantum gravity.

The leading correction scale is again
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau},
  \qquad
  \Lambda_{\rm eff}\sim\tau^{-1/2},
\end{equation}
```
with $`\tau`$ determined by the relevant sectoral gap or admissibility scale.

## Full nonperturbative execution task

Full gravity is harder. A nonperturbative gravitational MTT sector must supply:
``` math
\begin{equation}
  A_{\rm grav},
  \qquad
  P_{\rm diff},
  \qquad
  \chi,
  \qquad
  \tau.
\end{equation}
```
It must also satisfy:

1.  diffeomorphism compatibility;

2.  Hamiltonian and momentum constraint preservation;

3.  recovery of classical general relativity at large scales;

4.  controlled Lorentzian causal structure;

5.  admissible boundary conditions;

6.  stress-energy compatibility;

7.  a physical Hilbert or state-space interpretation;

8.  no unphysical coordinate-dependent smoothing.

This paper does not complete that task. It states the form such a construction must take.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravity-sector MTT is a geometric projection program, not a completed quantum-gravity
  calculation by itself.}
  }
  \label{eq:gravity-execution-task-section9}
\end{equation}
```

## Gravity-sector failure modes

The gravitational MTT construction fails if:

1.  $`A_{\rm grav}`$ is taken to be an indefinite Lorentzian $`\Box_g`$ heat operator;

2.  metric components are damped as coordinate components rather than geometric data;

3.  pure diffeomorphism modes are treated as physical;

4.  the Hamiltonian or momentum constraints are violated;

5.  the constraint algebra is broken;

6.  stress-energy conservation fails;

7.  a weak-field projector is used outside its perturbative regime;

8.  singularities or horizons are smoothed without producing admissible survivor geometries;

9.  observable predictions depend on arbitrary coordinate or foliation choices.

In such cases, the finite filter is not an admissible gravitational MTT object.

## Summary

Gravity is the deepest Lens sector because it acts on the representation of locality and geometry itself:
``` math
\begin{equation}
  g_{\mu\nu}\sim\varphi^\ast g_{\mu\nu}.
\end{equation}
```

The gravitational finite coherent admissibility operator must therefore be diffeomorphism-compatible:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
  }
\end{equation}
```

The Lorentzian rule is:
``` math
\begin{equation}
  \boxed{
  A_{\rm grav}\neq\Box_g
  \quad
  \text{as a naive fundamental heat operator}.
  }
\end{equation}
```
Instead, $`A_{\rm grav}`$ must be a positive or constraint-compatible geometric operator.

In ADM/Cauchy form:
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\Sigma}^{\rm grav})
  \mathrm e^{-\tau A_{\Sigma}^{\rm grav}}
  \chi(A_{\Sigma}^{\rm grav})P_{\rm diff},
\end{equation}
```
with preservation of the Hamiltonian and momentum constraints.

The Circle–Lens–Nil reading is:
``` math
\begin{align}
  \mathsf L_{\rm grav}
  &: \text{diffeomorphism quotient and geometric representation},\\
  \mathsf C_{\rm grav}
  &: \text{curvature and frame holonomy},\\
  \mathsf N_{\rm grav}
  &: \text{boundary, horizon, singularity, survivor geometry}.
\end{align}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{gravity is diffeomorphism-compatible finite coherent admissibility read as geometric
  projection.}
  }
\end{equation}
```

# Quantization as admissible survivor-label structure

The previous sections treated particles, waves, measurement records, scattering, gauge structure, electromagnetism, and gravity as projection shadows of finite coherent admissibility. We now turn to quantization.

In ordinary presentations, quantization often appears as a separate mystery: why do some physical quantities come in discrete units? In MTT, quantization is not treated as a primitive postulate. It is treated as the emergence of stable admissible labels from the combined action of Circle closure, Lens quotient consistency, and Nil survivor selection.

The guiding thesis is:
``` math
\begin{equation}
  \boxed{
  \text{quantization}
  =
  \mathsf C\text{-closure}
  +
  \mathsf L\text{-quotient consistency}
  +
  \mathsf N\text{-survivor selection}.
  }
  \label{eq:quantization-thesis-section10}
\end{equation}
```

In the fixed-point realization, compact internal fiber geometry adds a concrete source of discrete labels: the spectrum of positive fiber operators and the joint harmonic coherent sector.

## Quantization as survivor-label discreteness

A quantized label is a stable label that survives admissibility constraints. Such labels may come from:

1.  eigenvalues of a self-adjoint operator;

2.  compact-fiber spectra;

3.  phase closure conditions;

4.  topological winding numbers;

5.  gauge flux sectors;

6.  representation labels;

7.  particle-number records;

8.  measurement survivor basins;

9.  boundary or horizon sectors.

In MTT, these are not all identical mechanisms. They are different ways in which admissible structure becomes discretely labeled.

The common form is:
``` math
\begin{equation}
  \boxed{
  \text{continuous formal possibility}
  \longrightarrow
  \text{admissibility constraint}
  \longrightarrow
  \text{stable discrete survivor labels}.
  }
  \label{eq:formal-to-discrete-section10}
\end{equation}
```

A quantized label is therefore not merely a number. It is a Nil-surviving label compatible with Circle closure and Lens representation consistency.

## Spectral quantization

The simplest form of quantization is spectral. Let $`A`$ be a self-adjoint operator with eigenvalue equation
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n.
  \label{eq:spectral-eigenvalue-section10}
\end{equation}
```
If the spectrum is discrete, then admissible modes are labeled by $`n`$.

The finite coherent admissibility operator acts by
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n
  \label{eq:Badm-spectral-quantization-section10}
\end{equation}
```
in the commuting spectral case.

The label $`n`$ survives when
``` math
\begin{equation}
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}
\end{equation}
```
is nonzero or above the relevant admissibility threshold.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{spectral quantization}
  =
  \text{discrete eigenlabels surviving finite admissibility filtering}.
  }
  \label{eq:spectral-quantization-box-section10}
\end{equation}
```

This is the analytic prototype for MTT quantization.

## Compact fiber spectra

In the fixed-point realization, quantization has a geometric source. The internal fibers are compact Riemannian spaces. Their Laplace-type operators have discrete nonnegative spectra:
``` math
\begin{equation}
  \Delta_{B_n(y)}\psi_{n,j}(y)
  =
  \lambda_{n,j}(y)\psi_{n,j}(y),
\end{equation}
```
with
``` math
\begin{equation}
  0=\lambda_{n,0}(y)
  \le
  \lambda_{n,1}(y)
  \le
  \lambda_{n,2}(y)
  \le
  \cdots.
\end{equation}
```

The internal admissibility operator is
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3\kappa_n\Delta_{B_n}.
\end{equation}
```
If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
then the internal labels $`j`$ are discrete in compact sectors.

The zero-mode sector is
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
and is undamped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
The nonzero internal modes satisfy
``` math
\begin{equation}
  \mu_j^2>0,
\end{equation}
```
and are damped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus the fixed-point realization gives:
``` math
\begin{equation}
  \boxed{
  \text{compact fiber geometry}
  \longrightarrow
  \text{discrete internal labels}
  \longrightarrow
  \text{zero-mode shadows and damped excitation towers}.
  }
  \label{eq:fiber-quantization-box-section10}
\end{equation}
```

This is the Kaluza–Klein-compatible source of one class of MTT quantized labels.

## The joint harmonic coherent sector

The coherent projector in the FP realization is
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
with
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3
  \ker\Delta_{B_n}.
\end{equation}
```

This means that the coherent low-energy sector is not arbitrary. It is the joint fiber-harmonic sector. The zero-mode labels are selected by simultaneous harmonicity across internal bundle directions.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{coherent zero-mode quantization}
  =
  \text{joint survival in the fiber-harmonic kernel}.
  }
  \label{eq:joint-harmonic-quantization-box-section10}
\end{equation}
```

The nonzero internal modes are not absent in principle. They are present as possible excitations, but admissibility suppresses them by
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Therefore, the FP realization separates:
``` math
\begin{align}
  \text{zero modes}
  &: \text{coherent low-energy survivor labels},\\
  \text{nonzero internal modes}
  &: \text{damped excitation labels}.
\end{align}
```

## Phase closure and integer labels

Circle closure gives another basic route to quantization. If a phase variable lives on a circle, then single-valuedness requires
``` math
\begin{equation}
  \psi(\theta+2\pi)=\psi(\theta).
\end{equation}
```
The eigenfunctions are
``` math
\begin{equation}
  \psi_n(\theta)=\mathrm e^{\mathrm in\theta},
\end{equation}
```
with
``` math
\begin{equation}
  n\in\mathbb Z.
\end{equation}
```

Thus integer labels arise from phase closure:
``` math
\begin{equation}
  \boxed{
  \mathsf C\text{-closure}
  \quad\Rightarrow\quad
  n\in\mathbb Z.
  }
  \label{eq:circle-integer-section10}
\end{equation}
```

This is not merely a formal fact. It is the simplest example of quantization as admissible return. A phase that fails to return consistently is not a valid global state.

In this sense:
``` math
\begin{equation}
  \boxed{
  \text{integer quantization}
  =
  \text{stable Circle return label}.
  }
\end{equation}
```

## Gauge quantization

Gauge theory adds Lens quotient consistency. Local representatives must glue globally in a way that preserves phase and bundle structure.

For a $`U(1)`$ gauge field, flux quantization may take the schematic form
``` math
\begin{equation}
  \frac{1}{2\pi}\int_\Sigma F\in\mathbb Z.
  \label{eq:flux-quantization-section10}
\end{equation}
```
For electric and magnetic charges, Dirac quantization gives
``` math
\begin{equation}
  eg=2\pi n,
  \qquad
  n\in\mathbb Z,
  \label{eq:Dirac-quantization-section10}
\end{equation}
```
in units where $`\hbar=c=1`$.

In MTT language:
``` math
\begin{align}
  \mathsf C&: \text{phase closure around loops},\\
  \mathsf L&: \text{bundle patching and gauge quotient consistency},\\
  \mathsf N&: \text{stable charge or flux sector}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge quantization}
  =
  \mathsf C\text{-phase closure}
  +
  \mathsf L\text{-bundle consistency}
  +
  \mathsf N\text{-sector survival}.
  }
  \label{eq:gauge-quantization-box-section10}
\end{equation}
```

Gauge quantized labels are therefore not arbitrary labels attached to fields. They are global consistency labels of the gauge Lens structure.

## Representation labels

Quantum systems often carry representation labels. A particle may transform under a representation of a symmetry group:
``` math
\begin{equation}
  \rho:G\to\mathrm{Aut}(V).
\end{equation}
```
For compact groups, irreducible representation labels are discrete.

In MTT terms, representation labels are Lens-compatible survivor labels. They specify how states transform under symmetry while remaining admissible under quotient and phase constraints.

For a gauge group $`G`$, a matter sector must choose representation data:
``` math
\begin{equation}
  V_R.
\end{equation}
```
The representation label $`R`$ survives only if it is compatible with:

1.  gauge quotienting;

2.  anomaly cancellation;

3.  physical positivity;

4.  observed low-energy sectors;

5.  admissible coupling to measurement records.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{representation quantization}
  =
  \text{symmetry-compatible Lens survivor labeling}.
  }
  \label{eq:representation-quantization-section10}
\end{equation}
```

The present paper does not derive the full Standard Model representation content. It states the MTT form such a derivation must have.

## Particle number

Particle number is another quantized label, but it is not always fundamental. In quantum field theory, particle number is often a Fock-space label associated with excitations relative to a chosen vacuum or asymptotic context.

In MTT, particle number is a survivor label in a sector where:

1.  a coherent mode decomposition is available;

2.  excitations can be counted;

3.  the measurement context stabilizes number records;

4.  interactions do not destroy the relevant asymptotic interpretation.

For a mode $`a^\dagger`$, Fock labels are
``` math
\begin{equation}
  |n\rangle
  =
  \frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle,
  \qquad
  n=0,1,2,\dots.
\end{equation}
```

In MTT language:
``` math
\begin{equation}
  \boxed{
  \text{particle number}
  =
  \text{Nil-stable count of excitations in a chosen Circle/Lens mode context}.
  }
  \label{eq:particle-number-section10}
\end{equation}
```

This is why particle number can be exact in one regime and ambiguous in another. It depends on the admissible sector and the measurement context.

## Measurement outcomes as quantized records

Measurement outcomes are discrete when the detector survivor basins are discrete:
``` math
\begin{equation}
  \mathfrak B_{\mathsf M}
  =
  \{B_i^{(\mathsf M)}\}_{i\in I}.
\end{equation}
```
An individual record is
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

The outcome label $`i`$ is a Nil survivor label. It is exact relative to the measurement context when the detector dynamics stabilize the basin.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{measurement quantization}
  =
  \text{discrete survivor-basin labeling}.
  }
  \label{eq:measurement-quantization-section10}
\end{equation}
```

This clarifies the difference between a continuous underlying amplitude and a discrete record. The detector context may map continuous or coherent input structure into a discrete basin partition.

The basin probabilities are not supplied merely by the label set. They require a measure:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i^{(\mathsf M)})}
  {\sum_j\mu(B_j^{(\mathsf M)})}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{quantized outcomes require survivor labels; probabilities require basin measure.}
  }
\end{equation}
```

## Energy quantization

Energy quantization depends on boundary conditions, potentials, geometry, and the relevant Hamiltonian. For a bound system with Hamiltonian $`H`$,
``` math
\begin{equation}
  H\psi_n=E_n\psi_n.
\end{equation}
```
If the resolvent is compact or the bound-state spectrum is discrete, then
``` math
\begin{equation}
  E_n
\end{equation}
```
are discrete labels.

In MTT terms, the discrete energies are Circle/Lens/Nil-compatible survivor labels:
``` math
\begin{align}
  \mathsf C&: \text{standing-wave phase closure},\\
  \mathsf L&: \text{boundary conditions and representation choice},\\
  \mathsf N&: \text{normalizable bound-state survival}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{bound-state energy quantization}
  =
  \text{phase-closed normalizable survivor modes}.
  }
  \label{eq:energy-quantization-box-section10}
\end{equation}
```

The same logic applies to compact internal fiber spectra, where compactness and ellipticity produce discrete internal energies or mass contributions.

## Topological quantization

Topological sectors provide robust quantized labels. Examples include winding number, Chern number, instanton number, monopole charge, and flux sectors.

A typical topological integer has the schematic form
``` math
\begin{equation}
  Q_{\rm top}
  =
  \int_M \omega
  \in\mathbb Z,
\end{equation}
```
where $`\omega`$ is a characteristic density normalized so that the integral is integer-valued on admissible configurations.

In MTT language:
``` math
\begin{align}
  \mathsf C&: \text{closed cycles and return},\\
  \mathsf L&: \text{global patching and quotient consistency},\\
  \mathsf N&: \text{topological sector survival}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{topological quantization}
  =
  \text{integer-valued survivor labels of global admissibility}.
  }
  \label{eq:topological-quantization-section10}
\end{equation}
```

These labels are often stable under continuous deformation because changing them requires leaving the admissible sector or crossing a singular configuration.

## Gravity and geometric quantization labels

Gravity introduces geometric labels. In canonical or holonomy-based approaches, such labels may include:

1.  spin-network labels;

2.  holonomy representations;

3.  flux labels;

4.  area and volume spectra;

5.  boundary charges;

6.  horizon microstate labels.

MTT does not assume a specific quantum-gravity realization. Instead, it states the structural condition:
``` math
\begin{equation}
  \boxed{
  \text{gravitational quantized labels must be diffeomorphism-compatible survivor labels of
  geometric admissibility.}
  }
  \label{eq:gravity-quantization-section10}
\end{equation}
```

Thus a gravitational label is not physical merely because it is discrete in a coordinate description. It must survive the Lens quotient:
``` math
\begin{equation}
  g_{\mu\nu}\sim\varphi^\ast g_{\mu\nu},
\end{equation}
```
and must preserve the gravitational constraints.

## Quantization and the Born layer

Quantized labels are not the same as probabilities. A theory may identify possible discrete outcomes
``` math
\begin{equation}
  i\in I,
\end{equation}
```
but still need to assign outcome weights.

In MTT, survivor labels are supplied by Nil basin structure:
``` math
\begin{equation}
  \mathfrak B_{\mathsf M}
  =
  \{B_i^{(\mathsf M)}\}_{i\in I}.
\end{equation}
```
Probabilities require a basin measure:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i^{(\mathsf M)})}
  {\sum_j\mu(B_j^{(\mathsf M)})}.
  \label{eq:born-basin-section10}
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{quantization gives possible labels;}
  }
\end{equation}
```
while:
``` math
\begin{equation}
  \boxed{
  \text{the Born layer gives frequencies over labels.}
  }
\end{equation}
```

This distinction prevents the common mistake of treating discreteness itself as a probability law.

## Quantization and finite admissibility

Finite coherent admissibility modifies quantization by distinguishing possible formal labels from surviving admissible labels.

In the commuting spectral case:
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  w_n\phi_n,
\end{equation}
```
with
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```
A formal eigenlabel $`n`$ is strongly suppressed if
``` math
\begin{equation}
  w_n\ll1.
\end{equation}
```
It survives as part of the effective coherent sector if
``` math
\begin{equation}
  w_n
\end{equation}
```
is nonzero or above the relevant admissibility threshold.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite admissibility turns a formal spectrum into an effective survivor spectrum.}
  }
  \label{eq:effective-survivor-spectrum-section10}
\end{equation}
```

In the FP realization:
``` math
\begin{equation}
  w_j
  =
  p_j\chi(\mu_j^2)^2\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```
The zero modes survive undamped. The nonzero modes are suppressed according to their internal eigenvalues.

## Continuous spectra and approximate quantization

Not every sector has a purely discrete spectrum. Scattering states often form continuous spectra. In such cases, quantization may appear only after:

1.  imposing boundary conditions;

2.  compactifying a region;

3.  selecting resonances;

4.  measuring discrete detector records;

5.  projecting onto finite-resolution bins;

6.  restricting to bound states or stable sectors.

Thus MTT distinguishes:
``` math
\begin{equation}
  \text{spectral discreteness}
\end{equation}
```
from
``` math
\begin{equation}
  \text{record discreteness}.
\end{equation}
```

A continuous scattering spectrum can still produce discrete detector clicks because the detector has survivor basins:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{continuous wave spectra can produce discrete records through Nil basin selection.}
  }
  \label{eq:continuous-to-discrete-records-section10}
\end{equation}
```

This is another way in which MTT unifies wave-like and particle-like behavior.

## Classical discreteness versus quantum discreteness

Not all discreteness is quantum. A classical system can have discrete stable states due to nonlinear attractors, thresholds, or boundary conditions. Quantum discreteness is distinguished by its relation to coherent phase structure, Hilbert-space representation, and measurement statistics.

In MTT, quantum discreteness requires:

1.  coherent spectral or phase structure;

2.  admissible Lens representation;

3.  Nil survivor stability;

4.  a compatible probability or basin-measure layer.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{quantum labels are not merely discrete states;}
  }
\end{equation}
```
they are:
``` math
\begin{equation}
  \boxed{
  \text{coherence-compatible survivor labels in an admissible projection architecture}.
  }
\end{equation}
```

## Relation to wave–particle duality

The delta/wave duality remains central. Quantization adds a third aspect to the same kernel.

The local reading gives:
``` math
\begin{equation}
  \text{particle/delta shadow}.
\end{equation}
```

The spectral reading gives:
``` math
\begin{equation}
  \text{wave/interference shadow}.
\end{equation}
```

The survivor-label reading gives:
``` math
\begin{equation}
  \text{quantized label shadow}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}
  \quad
  \begin{cases}
    \text{local reading}
    &\Rightarrow
    \text{particle shadow},\\
    \text{spectral reading}
    &\Rightarrow
    \text{wave shadow},\\
    \text{survivor-label reading}
    &\Rightarrow
    \text{quantization shadow}.
  \end{cases}
  }
  \label{eq:particle-wave-quantization-section10}
\end{equation}
```

This is why quantization belongs in the same paper. It is not an unrelated add-on. It is another projection shadow of finite coherent admissibility.

## What is not yet derived

The paper does not claim to derive all observed quantum numbers from the present structural argument. In particular, it does not yet derive:

1.  all Standard Model representations;

2.  all fermion generations;

3.  all masses;

4.  all coupling constants;

5.  all anomaly cancellations;

6.  all quantum-gravity labels;

7.  all detector basin measures.

Those are sectoral execution tasks.

The claim established here is:
``` math
\begin{equation}
  \boxed{
  \text{quantization fits the finite coherent admissibility architecture as survivor-label
  structure.}
  }
  \label{eq:quantization-structural-claim-section10}
\end{equation}
```

## Summary

MTT interprets quantization as admissible survivor-label structure:
``` math
\begin{equation}
  \boxed{
  \text{quantization}
  =
  \mathsf C\text{-closure}
  +
  \mathsf L\text{-quotient consistency}
  +
  \mathsf N\text{-survivor selection}.
  }
\end{equation}
```

In spectral sectors:
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n
\end{equation}
```
gives discrete modal labels, and finite admissibility weights them by
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```

In the fixed-point realization:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j
\end{equation}
```
gives compact-fiber labels. Zero modes survive undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1,
\end{equation}
```
while nonzero internal modes are suppressed:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Measurement outcomes are quantized when detector survivor basins are discrete:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Gauge and topological labels arise from global phase closure and quotient consistency:
``` math
\begin{equation}
  \frac{1}{2\pi}\int_\Sigma F\in\mathbb Z.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{quantized labels are finite coherent admissibility labels that survive Circle closure,
  Lens consistency, and Nil selection.}
  }
\end{equation}
```

# Superposition and entanglement as coherent-sector structure

The previous section treated quantization as admissible survivor-label structure. We now turn to superposition and entanglement. These are often treated as uniquely quantum mysteries: how can a system be in several states at once, and how can separated systems share nonclassical correlations?

In MTT, superposition and entanglement are not separate primitives. They are coherent-sector structures before Nil survivor selection. Superposition is coherent coexistence of admissible branches in a given Lens context. Entanglement is non-factorizable coherent support across a joint admissible sector.

The guiding thesis is:
``` math
\begin{equation}
  \boxed{
  \text{superposition}
  =
  \text{coherent branch coexistence before Nil selection},
  }
  \label{eq:superposition-thesis-section11}
\end{equation}
```
and
``` math
\begin{equation}
  \boxed{
  \text{entanglement}
  =
  \text{non-factorizable coherent admissibility in a joint sector}.
  }
  \label{eq:entanglement-thesis-section11}
\end{equation}
```

Both are naturally expressed through the finite coherent admissibility operator:
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```

## Superposition as coherent branch coexistence

Let a measurement or representation context select a branch basis:
``` math
\begin{equation}
  \{|a\rangle\}_{a\in I}.
\end{equation}
```
A superposed state has the form
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_{a\in I}c_a|a\rangle.
  \label{eq:superposition-state-section11}
\end{equation}
```
The density matrix is
``` math
\begin{equation}
  \rho
  =
  |\psi\rangle\langle\psi|
  =
  \sum_{a,b}
  c_a c_b^\ast
  |a\rangle\langle b|.
  \label{eq:superposition-density-section11}
\end{equation}
```

The diagonal terms
``` math
\begin{equation}
  |c_a|^2|a\rangle\langle a|
\end{equation}
```
are branch weights. The off-diagonal terms
``` math
\begin{equation}
  c_a c_b^\ast|a\rangle\langle b|,
  \qquad
  a\neq b,
\end{equation}
```
are branch coherences.

In MTT, the state <a href="#eq:superposition-state-section11" data-reference-type="eqref" data-reference="eq:superposition-state-section11">[eq:superposition-state-section11]</a> is not read as a classical object being in many classical states simultaneously. It is read as a coherent admissible state whose branch decomposition depends on the Lens context.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{superposition is basis-relative coherent admissibility, not classical multiplicity.}
  }
  \label{eq:superposition-basis-relative-section11}
\end{equation}
```

## Circle, Lens, and Nil in superposition

Superposition involves all three components of the Modal Triplet.

Circle carries relative phase:
``` math
\begin{equation}
  c_a c_b^\ast
  =
  |c_a||c_b|\mathrm e^{\mathrm i(\theta_a-\theta_b)}.
\end{equation}
```
These relative phases are what allow interference.

Lens supplies the branch decomposition:
``` math
\begin{equation}
  \{|a\rangle\}_{a\in I}.
\end{equation}
```
A different measurement basis produces a different branch expansion.

Nil selects or stabilizes one record downstream:
``` math
\begin{equation}
  |\psi\rangle
  \to
  B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{superposition}
  =
  \mathsf C\text{-relative phase}
  +
  \mathsf L\text{-branch decomposition}
  \quad
  \text{before}
  \quad
  \mathsf N\text{-record selection}.
  }
  \label{eq:superposition-CLN-section11}
\end{equation}
```

This is why superposition and measurement are inseparable in interpretation. The state is coherent relative to one Lens decomposition, and the record is stabilized relative to a measurement context.

## Superposition and finite admissibility

Not every formal branch decomposition is physically admissible. The finite coherent admissibility operator determines which components survive the sectoral filtering:
``` math
\begin{equation}
  B_{\rm adm}|\psi\rangle
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P|\psi\rangle.
\end{equation}
```

In a commuting spectral basis,
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_n c_n|\phi_n\rangle,
\end{equation}
```
with
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
\end{equation}
```
one obtains
``` math
\begin{equation}
  B_{\rm adm}|\psi\rangle
  =
  \sum_n
  c_n
  p_n\chi(\lambda_n)^2
  \mathrm e^{-\tau\lambda_n}
  |\phi_n\rangle.
  \label{eq:filtered-superposition-section11}
\end{equation}
```

The mode weights are
``` math
\begin{equation}
  w_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```
Thus the admissible superposition is:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}|\psi\rangle
  =
  \sum_n c_n w_n|\phi_n\rangle.
  }
\end{equation}
```

This shows that superposition in MTT is not unconstrained formal addition. It is finite coherent addition inside an admissible sector.

## Decoherence and branch damping

When a system couples to a detector or environment, off-diagonal coherence may be damped. In a finite branch basis this is described by
``` math
\begin{equation}
  \rho\mapsto D\circ\rho,
  \label{eq:branch-damping-section11}
\end{equation}
```
where
``` math
\begin{equation}
  (D\circ\rho)_{ab}=D_{ab}\rho_{ab}.
\end{equation}
```

Physical admissibility requires
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```
Then the Schur map is completely positive and trace preserving.

If
``` math
\begin{equation}
  D_{ab}\approx1,
  \qquad
  a\neq b,
\end{equation}
```
then branch coherence survives. If
``` math
\begin{equation}
  D_{ab}\approx0,
  \qquad
  a\neq b,
\end{equation}
```
then the branches are effectively decohered in that Lens context.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{decoherence}
  =
  \mathsf N\text{-damping of off-diagonal Circle coherence in a Lens-selected branch basis}.
  }
  \label{eq:decoherence-CLN-section11}
\end{equation}
```

This is not yet a definite outcome. A definite outcome also requires survivor-basin selection:
``` math
\begin{equation}
  D\circ\rho
  \to
  B_i^{(\mathsf M)}.
\end{equation}
```

## Superposition versus mixture

A coherent superposition
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_a c_a|a\rangle
\end{equation}
```
has density matrix
``` math
\begin{equation}
  \rho_{\rm sup}
  =
  \sum_{a,b}
  c_a c_b^\ast
  |a\rangle\langle b|.
\end{equation}
```
An incoherent mixture with the same branch weights has density matrix
``` math
\begin{equation}
  \rho_{\rm mix}
  =
  \sum_a
  |c_a|^2
  |a\rangle\langle a|.
\end{equation}
```

The difference is the off-diagonal part:
``` math
\begin{equation}
  \rho_{\rm sup}-\rho_{\rm mix}
  =
  \sum_{a\neq b}
  c_a c_b^\ast
  |a\rangle\langle b|.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{superposition}
  -
  \text{mixture}
  =
  \text{off-diagonal coherent structure}.
  }
  \label{eq:superposition-mixture-difference-section11}
\end{equation}
```

Measurement devices that erase or preserve these off-diagonal terms produce different experimental shadows.

## Entanglement as non-factorizable coherence

Let a joint system have Hilbert space
``` math
\begin{equation}
  \mathcal H_{AB}
  =
  \mathcal H_A\otimes\mathcal H_B
\end{equation}
```
in a regime where such a tensor product decomposition is valid. A general pure state is
``` math
\begin{equation}
  |\Psi\rangle
  =
  \sum_{a,b}
  c_{ab}
  |a\rangle_A\otimes|b\rangle_B.
\end{equation}
```

The state is separable if
``` math
\begin{equation}
  c_{ab}=\alpha_a\beta_b,
\end{equation}
```
so that
``` math
\begin{equation}
  |\Psi\rangle=|\psi\rangle_A\otimes|\varphi\rangle_B.
\end{equation}
```
It is entangled if it cannot be written in this factorized form.

In MTT language:
``` math
\begin{equation}
  \boxed{
  \text{entanglement}
  =
  \text{joint coherent admissibility that does not factor into local coherent sectors}.
  }
  \label{eq:entanglement-nonfactor-box-section11}
\end{equation}
```

At the operator level, this means that the joint admissibility structure may fail to factor:
``` math
\begin{equation}
  P_{AB}\neq P_A\otimes P_B,
  \label{eq:PAB-nonfactor-section11}
\end{equation}
```
or
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  \neq
  B_{\rm adm}^{A}\otimes B_{\rm adm}^{B}.
  \label{eq:Badm-nonfactor-section11}
\end{equation}
```

Thus entanglement is not merely a surprising correlation after measurement. It is a structure of the joint coherent sector before measurement.

## Joint finite admissibility

For a joint system, the finite coherent admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  =
  P_{AB}\chi(A_{AB})
  \mathrm e^{-\tau A_{AB}}
  \chi(A_{AB})P_{AB}.
  \label{eq:joint-Badm-section11}
\end{equation}
```

If the system factorizes cleanly, then one may have
``` math
\begin{equation}
  A_{AB}=A_A\otimes I_B+I_A\otimes A_B,
\end{equation}
```
and
``` math
\begin{equation}
  P_{AB}=P_A\otimes P_B.
\end{equation}
```
In that case, under compatible windows and scales, the finite filter may factor.

But in interacting, constrained, gauge, gravitational, or globally coherent sectors, one may have
``` math
\begin{equation}
  A_{AB}
  \neq
  A_A\otimes I_B+I_A\otimes A_B,
\end{equation}
```
or
``` math
\begin{equation}
  P_{AB}\neq P_A\otimes P_B.
\end{equation}
```

Then the joint finite admissibility operator is genuinely non-factorizing.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{entanglement can arise from non-factorizing admissibility data }(A_{AB},P_{AB}).
  }
  \label{eq:entanglement-admissibility-data-section11}
\end{equation}
```

## Entangled records

Entanglement becomes operationally visible through correlated measurement records. Let Alice and Bob measure settings $`x`$ and $`y`$, producing outcomes $`a`$ and $`b`$. The joint effects are
``` math
\begin{equation}
  E_{a|x}^{A},
  \qquad
  E_{b|y}^{B}.
\end{equation}
```
The joint probability is
``` math
\begin{equation}
  p(a,b|x,y)
  =
  \operatorname{tr}\left[
    \rho_{AB}
    \left(
      E_{a|x}^{A}\otimes E_{b|y}^{B}
    \right)
  \right],
  \label{eq:joint-probability-section11}
\end{equation}
```
when a tensor factorization is valid.

In MTT, the measurement process also includes branch damping and survivor-basin selection:
``` math
\begin{equation}
  \rho_{AB}
  \to
  D^{(x,y)}\circ\rho_{AB}
  \to
  B_{ab}^{(x,y)}.
\end{equation}
```

Thus an entangled experiment has:

1.  a joint coherent sector;

2.  local Lens settings $`x,y`$;

3.  possible non-factorizing phase structure;

4.  local detector effects;

5.  correlated survivor records.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{entangled correlations}
  =
  \text{joint coherent-sector structure read through local measurement Lenses}.
  }
  \label{eq:entangled-correlations-section11}
\end{equation}
```

## Bell-type correlations

Bell-type experiments show that quantum correlations cannot be reproduced by local hidden variables satisfying the usual factorization assumptions. MTT does not evade this by adding classical hidden variables. The nonclassical feature is the non-factorizing joint coherent sector.

The key MTT statement is:
``` math
\begin{equation}
  \boxed{
  \text{joint admissible coherence need not factor into pre-existing local survivor labels.}
  }
  \label{eq:bell-MTT-statement-section11}
\end{equation}
```

Before measurement, the joint state can be coherent in a way that is not equivalent to a probability distribution over local classical records. Measurement settings select Lens decompositions, and Nil survivor basins stabilize outcomes.

The local outcome records are definite only after measurement:
``` math
\begin{equation}
  \Psi_{AB}
  \to
  B_{ab}^{(x,y)}.
\end{equation}
```

Thus Bell-type violation is not surprising in MTT. It reflects the failure of the assumption:
``` math
\begin{equation}
  \text{joint coherent admissibility}
  =
  \text{pre-existing distribution over local survivor labels}.
\end{equation}
```

MTT instead says:
``` math
\begin{equation}
  \boxed{
  \text{local records are Nil shadows of a joint coherent structure, not pre-existing classical
  variables.}
  }
  \label{eq:local-records-nil-shadows-section11}
\end{equation}
```

## No-signaling constraint

Entanglement must not permit controllable superluminal signaling. Therefore the local marginals must not depend on the remote measurement setting.

For Alice,
``` math
\begin{equation}
  p(a|x,y)
  =
  \sum_b p(a,b|x,y)
\end{equation}
```
must satisfy
``` math
\begin{equation}
  p(a|x,y)=p(a|x,y')
  \label{eq:no-signaling-Alice-section11}
\end{equation}
```
for all Bob settings $`y,y'`$. Similarly,
``` math
\begin{equation}
  p(b|x,y)=p(b|x',y)
  \label{eq:no-signaling-Bob-section11}
\end{equation}
```
for all Alice settings $`x,x'`$.

In MTT terms:
``` math
\begin{equation}
  \boxed{
  \text{joint coherence may be non-factorizing, but local survivor statistics must satisfy
  no-signaling.}
  }
  \label{eq:no-signaling-MTT-section11}
\end{equation}
```

This is a required admissibility condition on any MTT entanglement model.

The presence of joint coherent structure does not by itself transmit a signal. A signal would require controllable modulation of local marginals by a remote choice. MTT forbids this in admissible physical sectors.

## Gauge and gravitational factorization subtleties

The tensor product
``` math
\begin{equation}
  \mathcal H_{AB}
  =
  \mathcal H_A\otimes\mathcal H_B
\end{equation}
```
is not always fundamental.

In gauge theory, Gauss constraints can obstruct naive factorization across spatial regions. Boundary or edge modes may be required. The physical Hilbert space may not factor without including shared boundary data.

In gravity, the issue is deeper. Spatial regions themselves are defined only after geometric Lens projection. Diffeomorphism constraints and gravitational boundary charges can obstruct simple factorization.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{subsystem factorization is itself a Lens-dependent structure.}
  }
  \label{eq:factorization-lens-dependent-section11}
\end{equation}
```

Therefore, entanglement claims in gauge or gravity sectors must first justify the subsystem decomposition:
``` math
\begin{equation}
  \mathcal H_{AB}\stackrel{?}{=}\mathcal H_A\otimes\mathcal H_B.
\end{equation}
```

If this decomposition is invalid, then apparent entanglement or separability may be an artifact of a bad Lens choice.

## Internal/fiber entanglement

In the fixed-point realization, the internal fiber structure may also contribute to entanglement. A total state may involve both base and internal variables:
``` math
\begin{equation}
  \Psi(x,z),
  \qquad
  x\in Y^4,
  \quad
  z\in X^6.
\end{equation}
```
Expanding in internal modes:
``` math
\begin{equation}
  \Psi(x,z)
  =
  \sum_j
  \psi_j(x)\phi_j(z).
  \label{eq:base-fiber-expansion-section11}
\end{equation}
```

If this expansion cannot be written as a product
``` math
\begin{equation}
  \Psi(x,z)\neq \psi(x)\phi(z),
\end{equation}
```
then base and internal degrees of freedom are entangled.

After projection to the four-dimensional base, such internal coherence may appear as:

1.  effective mixed states;

2.  suppressed internal towers;

3.  finite form factors;

4.  correlated sector labels;

5.  apparent nonlocal finite-width shadows.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{some four-dimensional effective mixedness or finite structure can be a shadow of
  base--fiber entanglement.}
  }
  \label{eq:base-fiber-entanglement-section11}
\end{equation}
```

## Superposition in the FP zero-mode sector

In the FP realization, the coherent low-energy sector is the joint fiber-harmonic sector:
``` math
\begin{equation}
  \mathcal H_{\rm coh}
  =
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
\end{equation}
```

A low-energy superposition is therefore a coherent combination inside this zero-mode sector:
``` math
\begin{equation}
  |\psi_{\rm coh}\rangle
  =
  \sum_\alpha c_\alpha|\alpha\rangle_{\rm coh},
  \label{eq:coherent-zero-mode-superposition-section11}
\end{equation}
```
where
``` math
\begin{equation}
  P_{\rm coh}|\alpha\rangle_{\rm coh}
  =
  |\alpha\rangle_{\rm coh}.
\end{equation}
```

Nonzero internal modes may also appear formally:
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_\alpha c_\alpha|\alpha\rangle_{\rm coh}
  +
  \sum_j d_j|\phi_j\rangle_{\rm nonzero}.
\end{equation}
```
The finite admissibility operator suppresses them:
``` math
\begin{equation}
  d_j
  \mapsto
  d_j\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{effective low-energy superposition lives primarily in the joint fiber-harmonic
  coherent sector.}
  }
  \label{eq:FP-superposition-box-section11}
\end{equation}
```

## Measurement of entangled systems

For an entangled system, measurement must be described jointly. A measurement context includes local or joint settings:
``` math
\begin{equation}
  \mathsf M_{AB}
  =
  (x,y,A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_{ab}^{(x,y)}\},\mathfrak B_{AB}^{(x,y)}).
\end{equation}
```

The survivor basins are joint:
``` math
\begin{equation}
  \mathfrak B_{AB}^{(x,y)}
  =
  \{B_{ab}^{(x,y)}\}_{a,b}.
\end{equation}
```
The basin probability is
``` math
\begin{equation}
  \mathbb P(a,b|x,y)
  =
  \frac{
    \mu(B_{ab}^{(x,y)})
  }{
    \sum_{a',b'}\mu(B_{a'b'}^{(x,y)})
  }.
  \label{eq:joint-basin-probability-section11}
\end{equation}
```

If the basin measure agrees with the quantum trace rule, then
``` math
\begin{equation}
  \mathbb P(a,b|x,y)
  =
  \operatorname{tr}\left[
    \rho_{AB}
    E_{ab}^{(x,y)}
  \right].
\end{equation}
```

The important distinction remains:
``` math
\begin{equation}
  \boxed{
  \text{joint coherence determines possible correlations;}
  }
\end{equation}
```
whereas
``` math
\begin{equation}
  \boxed{
  \text{joint basin measure determines observed frequencies.}
  }
\end{equation}
```

## Reversibility and erasure

Some apparent loss of coherence is reversible. If branch information is stored in a marker system but not irreversibly amplified into a stable survivor record, then a later measurement may erase or recombine the marker basis.

Let the system-marker state be
``` math
\begin{equation}
  |\Psi\rangle
  =
  \alpha|\psi_1\rangle|m_1\rangle
  +
  \beta|\psi_2\rangle|m_2\rangle.
\end{equation}
```
The branch coherence visible in the system alone is controlled by the marker overlap:
``` math
\begin{equation}
  \langle m_2|m_1\rangle.
\end{equation}
```
If
``` math
\begin{equation}
  \langle m_2|m_1\rangle=0,
\end{equation}
```
the system alone shows no interference in that basis. But if the marker is later measured in a recombining basis, conditional interference can reappear.

In MTT language:
``` math
\begin{equation}
  \boxed{
  \text{reversible marker entanglement}
  \neq
  \text{irreversible Nil survivor-basin capture}.
  }
  \label{eq:reversibility-vs-capture-section11}
\end{equation}
```

This explains quantum eraser behavior without retrocausal alteration. The Lens context and Nil basin partition are changed before a final survivor record is stabilized.

## Classical correlations versus entanglement

A classically correlated state has the form
``` math
\begin{equation}
  \rho_{\rm class}
  =
  \sum_\lambda
  p(\lambda)
  \rho_A^\lambda\otimes\rho_B^\lambda.
\end{equation}
```
It represents a probability distribution over local states.

An entangled state cannot be written in this form. It contains joint coherent structure that does not reduce to pre-existing local alternatives.

In MTT:
``` math
\begin{equation}
  \boxed{
  \text{classical correlation}
  =
  \text{shared Nil label distribution};
  }
\end{equation}
```
whereas
``` math
\begin{equation}
  \boxed{
  \text{entanglement}
  =
  \text{joint Circle coherence before local Nil labels exist}.
  }
\end{equation}
```

This distinction is central to Bell-type experiments. Classical correlation assumes local survivor labels already exist. Entanglement says the joint coherent sector precedes the local record decomposition.

## Entanglement and the delta/wave duality

The delta/wave duality extends naturally to entanglement.

For a single system:
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  \quad
  \begin{cases}
    \text{local reading}
    &\Rightarrow
    \text{particle/delta shadow},\\
    \text{spectral reading}
    &\Rightarrow
    \text{wave shadow}.
  \end{cases}
\end{equation}
```

For a joint system:
``` math
\begin{equation}
  K_{AB}(x_A,x_B;y_A,y_B)
\end{equation}
```
may fail to factor:
``` math
\begin{equation}
  K_{AB}
  \neq
  K_AK_B.
\end{equation}
```
Then local readings produce correlated records, while spectral readings show joint coherent modes.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{entanglement}
  =
  \text{non-factorizing extension of the same finite kernel logic behind delta/wave duality}.
  }
  \label{eq:entanglement-delta-wave-section11}
\end{equation}
```

This is why entanglement belongs naturally in the same finite coherent projection framework.

## Execution tasks

A complete MTT account of entanglement must supply:

1.  the joint Hilbert or physical state space;

2.  the admissible joint operator $`A_{AB}`$;

3.  the joint coherent projector $`P_{AB}`$;

4.  proof or disproof of factorization $`P_{AB}=P_A\otimes P_B`$;

5.  local measurement effects $`E_{a|x}^{A}`$, $`E_{b|y}^{B}`$;

6.  joint survivor basins $`B_{ab}^{(x,y)}`$;

7.  the basin measure $`\mu`$;

8.  no-signaling of local marginals;

9.  agreement with Bell-type quantum correlations in benchmark cases.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT identifies the structure of entanglement; sectoral execution must derive the
  quantitative correlations.}
  }
  \label{eq:entanglement-execution-section11}
\end{equation}
```

## Summary

Superposition is coherent branch coexistence:
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_a c_a|a\rangle.
\end{equation}
```
It depends on a Lens branch decomposition and carries Circle phase coherence.

Decoherence is Nil damping of off-diagonal terms:
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab}.
\end{equation}
```
A definite outcome requires survivor-basin capture:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Entanglement is non-factorizable joint coherent admissibility:
``` math
\begin{equation}
  P_{AB}\neq P_A\otimes P_B,
\end{equation}
```
or
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  \neq
  B_{\rm adm}^{A}\otimes B_{\rm adm}^{B}.
\end{equation}
```

Bell-type correlations reflect the fact that joint coherent admissibility need not be a pre-existing distribution over local survivor labels. Admissible MTT entanglement must still satisfy no-signaling:
``` math
\begin{equation}
  \sum_b p(a,b|x,y)
  =
  \sum_b p(a,b|x,y')
\end{equation}
```
and similarly for Bob.

In the fixed-point realization, effective low-energy superpositions live primarily in the joint fiber-harmonic sector:
``` math
\begin{equation}
  \mathcal H_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n},
\end{equation}
```
while nonzero internal modes are suppressed by
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{superposition and entanglement are coherent-sector shadows of the same finite
  admissibility structure that produces delta and wave shadows.}
  }
\end{equation}
```

# Analytic theorems and structural unification corollary

The preceding sections developed the physical shadows of finite coherent admissibility: Dirac-delta localization, spectral wave behavior, measurement records, scattering form factors, gauge quotienting, electromagnetic holonomy, gravitational projection, quantization, superposition, and entanglement. We now separate the rigorous analytic claims from the broader structural unification claim.

This separation is important. The paper does not assert one vague theorem that proves all physics at once. It establishes a hierarchy:

1.  an analytic finite-filter theorem;

2.  a branch-channel theorem for admissible damping;

3.  a scalar heat-kernel benchmark theorem;

4.  a fixed-point/fiber realization statement;

5.  a structural unification corollary.

The first three are mathematical statements. The fourth identifies the geometric realization. The fifth is the interpretive MTT conclusion.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{analytic control}
  \quad\Rightarrow\quad
  \text{sectoral admissibility}
  \quad\Rightarrow\quad
  \text{projection-shadow unification}.
  }
  \label{eq:theorem-hierarchy-section12}
\end{equation}
```

## The finite-filter theorem

Let $`\mathcal H`$ be a Hilbert space. Let
``` math
\begin{equation}
  A:\mathcal D(A)\subset\mathcal H\to\mathcal H
\end{equation}
```
be a nonnegative self-adjoint operator:
``` math
\begin{equation}
  A\ge0.
\end{equation}
```
Let
``` math
\begin{equation}
  P=P^\ast=P^2
\end{equation}
```
be an orthogonal projector. Let $`\chi`$ be a bounded Borel function satisfying
``` math
\begin{equation}
  0\le\chi(\lambda)\le1.
\end{equation}
```
Assume the commuting spectral condition:
``` math
\begin{equation}
  [P,A]=0.
  \label{eq:commuting-condition-section12}
\end{equation}
```
For $`\tau>0`$, define
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  \label{eq:Badm-theorem-section12}
\end{equation}
```

<div id="thm:finite-filter" class="theorem">

**Theorem 2** (Finite coherent admissibility filter). *Under the assumptions above, $`B_{\rm adm}`$ is a bounded positive contraction:
``` math
\begin{equation}
  0\le B_{\rm adm}\le I.
\end{equation}
```
If $`A\phi_n=\lambda_n\phi_n`$ and $`P\phi_n=p_n\phi_n`$ with $`p_n\in\{0,1\}`$, then
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
  \label{eq:finite-filter-modal-action-section12}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Since $`A\ge0`$, the spectral theorem gives
``` math
\begin{equation}
  0\le \mathrm e^{-\tau A}\le I.
\end{equation}
```
Since $`0\le\chi\le1`$,
``` math
\begin{equation}
  0\le\chi(A)\le I.
\end{equation}
```
Because $`[P,A]=0`$, $`P`$ commutes with $`\chi(A)`$ and $`\mathrm e^{-\tau A}`$. Therefore, for any $`f\in\mathcal H`$,
``` math
\begin{align}
  \langle f,B_{\rm adm}f\rangle
  &=
  \langle f,P\chi(A)\mathrm e^{-\tau A}\chi(A)P f\rangle\\
  &=
  \left\|
    \mathrm e^{-\tau A/2}\chi(A)P f
  \right\|^2\\
  &\ge0.
\end{align}
```
Thus $`B_{\rm adm}\ge0`$.

Moreover,
``` math
\begin{equation}
  \|\chi(A)\|\le1,
  \qquad
  \|\mathrm e^{-\tau A}\|\le1,
  \qquad
  \|P\|\le1.
\end{equation}
```
Hence
``` math
\begin{equation}
  \|B_{\rm adm}\|\le1.
\end{equation}
```
Since $`B_{\rm adm}\ge0`$, this implies
``` math
\begin{equation}
  0\le B_{\rm adm}\le I.
\end{equation}
```

If $`A\phi_n=\lambda_n\phi_n`$, then
``` math
\begin{equation}
  \chi(A)\phi_n=\chi(\lambda_n)\phi_n,
\end{equation}
```
and
``` math
\begin{equation}
  \mathrm e^{-\tau A}\phi_n=\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```
If $`P\phi_n=p_n\phi_n`$, then
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```
 ◻

</div>

<div class="remark">

*Remark 3*. The theorem is stated in the commuting spectral case. If $`[P,A]\neq0`$, the formula <a href="#eq:finite-filter-modal-action-section12" data-reference-type="eqref" data-reference="eq:finite-filter-modal-action-section12">[eq:finite-filter-modal-action-section12]</a> need not hold. The expression $`P\chi(A)\mathrm e^{-\tau A}\chi(A)P`$ may still be meaningful, but admissibility must then be checked by domain, positivity, constraint, and boundedness estimates.

</div>

## Kernel-shadow corollary

Assume now that $`B_{\rm adm}`$ has an integral kernel
``` math
\begin{equation}
  K_{\rm adm}(x,y)=\langle x|B_{\rm adm}|y\rangle.
\end{equation}
```
In the commuting discrete spectral case,
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}
  \phi_n(x)\phi_n^\ast(y).
  \label{eq:kernel-shadow-formula-section12}
\end{equation}
```

<div id="cor:local-spectral-shadows" class="corollary">

**Corollary 4** (Local and spectral shadows). *When a kernel representation exists, the same finite coherent admissibility operator has two primary readings:
``` math
\begin{align}
  \text{local reading}
  &: \quad
  x\mapsto K_{\rm adm}(x,x_0),
  \\
  \text{spectral reading}
  &: \quad
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
\end{align}
```
The local reading gives the finite source or particle-shadow profile. The spectral reading gives the wave-shadow profile.*

</div>

Thus:
``` math
\begin{equation}
  \boxed{
  \text{one finite kernel}
  \quad\Rightarrow\quad
  \begin{cases}
    \text{Dirac-delta/local shadow},\\
    \text{spectral/wave shadow}.
  \end{cases}
  }
  \label{eq:one-kernel-two-shadows-section12}
\end{equation}
```

## Sharp delta corollary

The Dirac delta is recovered when the finite coherent admissibility operator approaches the identity.

<div id="cor:sharp-delta-limit" class="corollary">

**Corollary 5** (Sharp delta limit). *Suppose a family
``` math
\begin{equation}
  B_{\rm adm}^{(N)}
  =
  P_N\chi_N(A)\mathrm e^{-\tau_N A}\chi_N(A)P_N
\end{equation}
```
satisfies
``` math
\begin{equation}
  P_N\to I,
  \qquad
  \chi_N(A)\to I,
  \qquad
  \tau_N\downarrow0
\end{equation}
```
strongly on the relevant test-function domain. Then
``` math
\begin{equation}
  B_{\rm adm}^{(N)}f\to f.
\end{equation}
```
If $`B_{\rm adm}^{(N)}`$ has kernels $`K_N(x,y)`$, then
``` math
\begin{equation}
  K_N(x,y)\to\delta(x-y)
\end{equation}
```
distributionally.*

</div>

This establishes the precise MTT reading:
``` math
\begin{equation}
  \boxed{
  \delta(x-y)
  =
  \text{sharp identity-kernel shadow of finite coherent admissibility}.
  }
  \label{eq:delta-sharp-shadow-section12}
\end{equation}
```

The Dirac delta is therefore not primitive in the theory. It is the zero-width limit of an admissible finite kernel.

## Schur branch-channel theorem

Measurement and decoherence require a separate theorem. Branch damping is not described by the same operator $`B_{\rm adm}`$ acting on wavefunctions. It is described by a channel acting on density matrices.

Let $`D`$ be an $`N\times N`$ matrix and define the Schur product map
``` math
\begin{equation}
  \Phi_D(\rho)=D\circ\rho,
  \qquad
  (\Phi_D(\rho))_{ab}=D_{ab}\rho_{ab}.
  \label{eq:Schur-map-section12}
\end{equation}
```

<div id="thm:schur-damping-channel-section12" class="theorem">

**Theorem 6** (Schur damping channel). *If
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1
\end{equation}
```
for all $`a`$, then
``` math
\begin{equation}
  \rho\mapsto D\circ\rho
\end{equation}
```
is completely positive and trace preserving.*

</div>

<div class="proof">

*Proof.* Since $`D\succeq0`$, there exist vectors $`v_a`$ in an auxiliary Hilbert space $`\mathcal K`$ such that
``` math
\begin{equation}
  D_{ab}=\langle v_b,v_a\rangle.
\end{equation}
```
The condition $`D_{aa}=1`$ implies
``` math
\begin{equation}
  \|v_a\|=1.
\end{equation}
```
Define an isometry
``` math
\begin{equation}
  V:\mathbb C^N\to\mathbb C^N\otimes\mathcal K
\end{equation}
```
by
``` math
\begin{equation}
  V|a\rangle=|a\rangle\otimes v_a.
\end{equation}
```
Then
``` math
\begin{equation}
  V^\ast V=I.
\end{equation}
```
The reduced channel
``` math
\begin{equation}
  \Phi_D(\rho)
  =
  \operatorname{tr}_{\mathcal K}(V\rho V^\ast)
\end{equation}
```
has matrix elements
``` math
\begin{align}
  \langle a|\Phi_D(\rho)|b\rangle
  &=
  \rho_{ab}\langle v_b,v_a\rangle\\
  &=
  D_{ab}\rho_{ab}.
\end{align}
```
Therefore
``` math
\begin{equation}
  \Phi_D(\rho)=D\circ\rho.
\end{equation}
```
Because $`\Phi_D`$ has a Stinespring representation, it is completely positive. Because $`V`$ is an isometry, it is trace preserving. ◻

</div>

Thus:
``` math
\begin{equation}
  \boxed{
  D\succeq0,\quad D_{aa}=1
  \quad\Rightarrow\quad
  \text{branch damping is a valid quantum channel}.
  }
  \label{eq:branch-channel-box-section12}
\end{equation}
```

This theorem is why MTT does not permit arbitrary visibility factors.

## Exponential damping and Schoenberg admissibility

A common measurement damping model is
``` math
\begin{equation}
  D_{ab}(\tau)
  =
  \mathrm e^{-\tau\Lambda_{ab}}.
  \label{eq:exponential-damping-section12}
\end{equation}
```
For this to define a valid Schur channel for all $`\tau\ge0`$, one needs
``` math
\begin{equation}
  D(\tau)\succeq0
\end{equation}
```
for all $`\tau\ge0`$, together with
``` math
\begin{equation}
  D_{aa}(\tau)=1.
\end{equation}
```

A standard sufficient condition is that $`\Lambda`$ is conditionally negative definite and has zero diagonal:
``` math
\begin{equation}
  \Lambda_{aa}=0,
\end{equation}
```
and
``` math
\begin{equation}
  \sum_{a,b}\overline{c_a}c_b\Lambda_{ab}\le0
  \qquad
  \text{whenever}
  \qquad
  \sum_a c_a=0.
  \label{eq:CND-section12}
\end{equation}
```

Then Schoenberg’s theorem implies
``` math
\begin{equation}
  \mathrm e^{-\tau\Lambda}\succeq0
\end{equation}
```
for all $`\tau\ge0`$.

Thus:
``` math
\begin{equation}
  \boxed{
  \Lambda\text{ conditionally negative definite}
  \quad\Rightarrow\quad
  D_{ab}=\mathrm e^{-\tau\Lambda_{ab}}
  \text{ is admissible branch damping}.
  }
  \label{eq:Schoenberg-box-section12}
\end{equation}
```

In MTT language, $`\Lambda_{ab}`$ measures branch distinguishability, while $`D_{ab}`$ measures surviving coherence.

## Scalar heat-kernel benchmark theorem

The scalar Euclidean heat kernel provides a complete closed benchmark. Let
``` math
\begin{equation}
  A=-\Delta
\end{equation}
```
on $`\mathbb R^d`$, with
``` math
\begin{equation}
  P=I,
  \qquad
  \chi=1.
\end{equation}
```
Then
``` math
\begin{equation}
  B_{\rm adm}=\mathrm e^{\tau\Delta}.
\end{equation}
```

<div id="thm:scalar-heat-benchmark" class="theorem">

**Theorem 7** (Flat scalar heat-kernel benchmark). *For $`A=-\Delta`$ on $`\mathbb R^d`$, $`P=I`$, and $`\chi=1`$, the finite coherent kernel is
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
  \label{eq:scalar-heat-kernel-theorem-section12}
\end{equation}
```
Its Fourier transform is
``` math
\begin{equation}
  \widehat K_\tau^{(d)}(k)=\mathrm e^{-\tau k^2}.
  \label{eq:scalar-heat-transform-section12}
\end{equation}
```
It converges distributionally to the Dirac delta:
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)\to\delta^{(d)}(x-y)
  \qquad
  \text{as}
  \qquad
  \tau\downarrow0.
  \label{eq:scalar-delta-limit-section12}
\end{equation}
```
The coherent length and effective energy scale are
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau},
  \qquad
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
  \label{eq:scalar-scales-section12}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The Fourier representation is
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  \int_{\mathbb R^d}
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \mathrm e^{-\tau k^2}
  \mathrm e^{\mathrm ik\cdot(x-y)}.
\end{equation}
```
The $`d`$-dimensional Gaussian integral gives
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
\end{equation}
```
By construction its Fourier transform is
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}.
\end{equation}
```
For every test function $`f\in C_c^\infty(\mathbb R^d)`$,
``` math
\begin{equation}
  \lim_{\tau\downarrow0}
  \int_{\mathbb R^d}
  K_\tau^{(d)}(x-y)f(y)\,\,\mathrm d^dy
  =
  f(x),
\end{equation}
```
so $`K_\tau^{(d)}\to\delta^{(d)}`$ distributionally. Since $`[\tau]=L^2`$, the coherent length is $`\sqrt{\tau}`$, and the inverse energy scale is $`\tau^{-1/2}`$. ◻

</div>

This benchmark proves explicitly how a finite kernel yields both:
``` math
\begin{equation}
  \delta^{(d)}(x-y)
\end{equation}
```
as a sharp local shadow and
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
\end{equation}
```
as a spectral damping shadow.

## Finite propagator benchmark

In the Euclidean scalar benchmark, the ordinary propagator is
``` math
\begin{equation}
  \Delta(k)
  =
  \frac{1}{k^2+m^2}.
\end{equation}
```
A finite coherent insertion gives
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
  \label{eq:finite-propagator-benchmark-section12}
\end{equation}
```

This has the position-space form
``` math
\begin{equation}
  \Delta_{\rm adm}
  =
  K_\tau^{(d)}\ast\Delta.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite propagator}
  =
  \text{ordinary propagator convolved with finite coherent kernel}.
  }
  \label{eq:finite-propagator-box-section12}
\end{equation}
```

However, as emphasized earlier, this is a Euclidean scalar benchmark. It is not the fundamental Lorentzian prescription. Lorentzian MTT uses positive internal, spatial, Hamiltonian, or constraint-compatible operators.

## Fixed-point/fiber realization statement

In the fixed-point realization, the total geometric model is
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
or a compact internal fiber geometry over a Lorentzian base $`Y^4`$. The internal admissibility operator is
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3\kappa_n\Delta_{B_n},
  \qquad
  \kappa_n>0,
  \label{eq:Aint-theorem-section12}
\end{equation}
```
with
``` math
\begin{equation}
  A_{\rm int}\ge0.
\end{equation}
```

The coherent projector is
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
  \label{eq:Pcoh-theorem-section12}
\end{equation}
```
with range
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
  \label{eq:joint-harmonic-theorem-section12}
\end{equation}
```

The fixed-point coherent admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
  \label{eq:FP-Badm-theorem-section12}
\end{equation}
```

If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
then
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}\phi_j
  =
  p_j\chi(\mu_j^2)^2
  \mathrm e^{-\tau\mu_j^2}\phi_j.
  \label{eq:FP-modal-action-section12}
\end{equation}
```

The zero modes satisfy
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
and are undamped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
The nonzero internal modes satisfy
``` math
\begin{equation}
  \mu_j^2>0,
\end{equation}
```
and are damped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{FP/MTT finite admissibility}
  =
  \text{joint harmonic zero-mode survival plus damped internal excitations}.
  }
  \label{eq:FP-admissibility-box-section12}
\end{equation}
```

## Gap-selected damping scale

Assume the discarded sector has a uniform gap:
``` math
\begin{equation}
  \lambda_\ast>0.
\end{equation}
```
Let
``` math
\begin{equation}
  Q=I-P
\end{equation}
```
be the discarded-sector projector. Suppose the discarded-sector flow satisfies
``` math
\begin{equation}
  \|Q\Phi_tQ\|
  \le
  C_Q\mathrm e^{-\lambda_\ast t}.
\end{equation}
```
Given admissibility tolerance
``` math
\begin{equation}
  0<\epsilon_{\rm adm}<1,
\end{equation}
```
choose $`\tau`$ by
``` math
\begin{equation}
  C_Q\mathrm e^{-\lambda_\ast\tau}=\epsilon_{\rm adm}.
\end{equation}
```
Then
``` math
\begin{equation}
  \boxed{
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
  }
  \label{eq:gap-selected-tau-section12}
\end{equation}
```

If the typical internal radius is $`R`$, then for Laplace-type fibers
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2}.
\end{equation}
```
Therefore
``` math
\begin{equation}
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
  \label{eq:gap-radius-scale-section12}
\end{equation}
```

Thus the finite coherent width has a geometric origin:
``` math
\begin{equation}
  \boxed{
  \ell_{\rm coh}
  \sim
  \sqrt{\tau}
  \sim
  R\sqrt{\log(C_Q/\epsilon_{\rm adm})}.
  }
  \label{eq:coherent-width-geometric-section12}
\end{equation}
```

## Lorentzian admissibility theorem schema

The Lorentzian result is not a heat-kernel theorem for $`\Box`$. It is an admissibility schema.

A Lorentzian finite-kernel construction is admissible when:

1.  the damping operator is positive in the relevant physical sector;

2.  no naive indefinite $`e^{-\tau\Box}`$ is used as a fundamental heat operator;

3.  equal-time kernels are bounded on the relevant energy/Sobolev spaces;

4.  the hyperbolic principal symbol is unchanged;

5.  gauge and gravitational constraints are preserved where relevant;

6.  no controllable superluminal signaling is introduced.

For an equation of the schematic form
``` math
\begin{equation}
  \Box_g\phi+m^2\phi+\mathcal K_t\phi=J,
  \label{eq:kernel-hyperbolic-schema-section12}
\end{equation}
```
where $`\mathcal K_t`$ is a bounded equal-time spatial operator, the principal part remains
``` math
\begin{equation}
  \Box_g.
\end{equation}
```
Therefore the characteristic cone is unchanged.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{bounded equal-time finite kernels can preserve Lorentzian finite propagation speed
  because they do not change the principal symbol.}
  }
  \label{eq:lorentzian-schema-box-section12}
\end{equation}
```

This is the Lorentzian replacement for naive $`e^{-\tau\Box}`$.

## Gauge and gravity admissibility schemas

Gauge admissibility requires
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
  \label{eq:gauge-schema-section12}
\end{equation}
```
The operator must preserve gauge quotienting, Ward identities, BRST cohomology, and current conservation.

Gravity admissibility requires
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
  \label{eq:gravity-schema-section12}
\end{equation}
```
The operator must preserve diffeomorphism-compatible geometric content and the gravitational constraint structure.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite filtering is physical only after the relevant quotient and constraint structure
  has been respected.}
  }
  \label{eq:quotient-constraint-box-section12}
\end{equation}
```

## Structural unification corollary

We can now state the structural MTT conclusion.

<div id="cor:structural-unification" class="corollary">

**Corollary 8** (Structural projection-shadow unification). *Suppose a physical sector supplies admissible data
``` math
\begin{equation}
  (\mathcal H,A,P,\chi,\tau),
\end{equation}
```
with $`A`$ positive or sector-compatible, $`P`$ a valid coherent/physical projector, $`\chi(A)`$ an admissible spectral window, and $`\tau`$ a finite damping scale. Suppose further that gauge, gravitational, measurement, and Lorentzian constraints are respected where relevant. Then the finite coherent admissibility operator
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
generates sectoral projection shadows. These include:
``` math
\begin{align}
  \text{local kernel shadow}
  &\Rightarrow
  \text{particle/delta behavior},\\
  \text{spectral kernel shadow}
  &\Rightarrow
  \text{wave/interference behavior},\\
  \text{finite detector shadow}
  &\Rightarrow
  \text{measurement records},\\
  \text{branch-channel shadow}
  &\Rightarrow
  \text{visibility damping},\\
  \text{internal-mode shadow}
  &\Rightarrow
  \text{suppressed excitation towers},\\
  \text{quotient-compatible shadow}
  &\Rightarrow
  \text{gauge structure},\\
  \text{geometric quotient shadow}
  &\Rightarrow
  \text{gravity},\\
  \text{survivor-label shadow}
  &\Rightarrow
  \text{quantization},\\
  \text{joint-sector shadow}
  &\Rightarrow
  \text{entanglement}.
\end{align}
```*

</div>

In compact form:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility}
  \longrightarrow
  \text{projection shadows}
  \longrightarrow
  \text{effective physics}.
  }
  \label{eq:structural-unification-box-section12}
\end{equation}
```

## Why this is not a trivial theorem

The result is not merely the observation that physics uses Hilbert spaces, operators, or spectra. Those are already standard. The nontrivial content is the assembly.

The same finite coherent architecture accounts for:

1.  the Dirac-delta limit of local particle-like behavior;

2.  the spectral representation of wave-like behavior;

3.  detector records through finite effects and survivor basins;

4.  decoherence through admissible Schur channels;

5.  scattering form factors through finite kernels or internal-mode damping;

6.  gauge theory through quotient-compatible projection;

7.  electromagnetism through gauge Lens, Circle holonomy, and Nil records;

8.  gravity through diffeomorphism-compatible geometric projection;

9.  quantization through survivor-label discreteness;

10. entanglement through non-factorizing joint coherent sectors.

The individual pieces are familiar. The contribution is that they are organized by a single projection architecture:
``` math
\begin{equation}
  \boxed{
  \text{coherent sector}
  \xrightarrow{\;\text{finite admissibility}\;}
  \text{physical shadow}.
  }
  \label{eq:coherent-sector-to-shadow-section12}
\end{equation}
```

## What the theorem does not prove

The structural corollary does not prove all sectoral physics automatically. It does not by itself derive:

1.  all Standard Model particles and representations;

2.  all masses and couplings;

3.  the full nonperturbative quantum-gravity state space;

4.  exact collider phenomenology of internal excitations;

5.  all measurement basin measures;

6.  the Born rule in every detector context;

7.  all cosmological or black-hole predictions.

Those require sectoral execution.

The theorem gives the admissibility architecture:
``` math
\begin{equation}
  \boxed{
  \text{derive }A,\;P,\;\chi,\;\tau
  \quad
  \text{then compute the sectoral shadows}.
  }
  \label{eq:execution-architecture-section12}
\end{equation}
```

## Summary

This section separated the paper’s claims into precise layers.

The finite-filter theorem states that, under clean spectral assumptions,
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
is a positive bounded admissibility filter with modal weights
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```

The Schur-channel theorem states that
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1
\end{equation}
```
makes
``` math
\begin{equation}
  \rho\mapsto D\circ\rho
\end{equation}
```
a valid completely positive trace-preserving branch-damping channel.

The scalar benchmark theorem proves explicitly that
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(-\frac{|x-y|^2}{4\tau}\right)
\end{equation}
```
has Fourier transform
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
\end{equation}
```
and sharp limit
``` math
\begin{equation}
  \delta^{(d)}(x-y).
\end{equation}
```

The fixed-point realization grounds the abstract operator in compact internal geometry:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
\end{equation}
```

The structural corollary is:
``` math
\begin{equation}
  \boxed{
  \text{wave, particle, measurement, scattering, gauge, gravity, quantization, and
  entanglement are projection shadows of finite coherent admissibility.}
  }
\end{equation}
```

# Relation to existing programs

The previous section separated the analytic theorems from the structural unification corollary. We now locate the framework relative to existing physical programs.

The purpose of this section is not to claim that MTT replaces all existing approaches. Many ingredients used here are familiar: spectral theory, heat kernels, decoherence, gauge quotienting, Kaluza–Klein reduction, constrained Hamiltonian dynamics, and geometric projection all have long histories. The contribution of MTT is the assembly:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility}
  \longrightarrow
  \text{projection shadows}
  \longrightarrow
  \text{effective physics}.
  }
\end{equation}
```

The central novelty is that particle localization, wave interference, measurement records, gauge structure, gravity, quantization, and entanglement are treated as different shadows of one finite coherent admissibility architecture.

## Complementarity

Bohr complementarity states that wave-like and particle-like descriptions are mutually exclusive experimental descriptions. One experimental arrangement reveals interference; another reveals localized path or detector information.

MTT agrees with the operational lesson but changes the explanatory order.

Complementarity says:
``` math
\begin{equation}
  \boxed{
  \text{wave and particle are complementary descriptions.}
  }
\end{equation}
```

MTT says:
``` math
\begin{equation}
  \boxed{
  \text{wave and particle are two projection shadows of one finite coherent kernel.}
  }
\end{equation}
```

The common source is
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
The local reading gives the particle shadow:
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
\end{equation}
```
The spectral reading gives the wave shadow:
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
\end{equation}
```

Thus MTT does not deny complementarity. It refines complementarity into projection duality:
``` math
\begin{equation}
  \boxed{
  \text{complementary appearances arise from different Lens readings of the same finite
  coherent admissibility structure.}
  }
\end{equation}
```

## Decoherence

Decoherence explains the suppression of interference through entanglement with environmental degrees of freedom. MTT incorporates this mechanism but distinguishes it from record selection.

In MTT, branch damping is represented by
``` math
\begin{equation}
  \rho\mapsto D\circ\rho,
\end{equation}
```
with physical admissibility condition
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```
This is precisely the Schur-channel layer.

However, MTT separates:
``` math
\begin{equation}
  \text{coherence loss}
\end{equation}
```
from
``` math
\begin{equation}
  \text{record stabilization}.
\end{equation}
```
The first is described by
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab}.
\end{equation}
```
The second is described by survivor-basin capture:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{decoherence explains visibility loss;}
  }
\end{equation}
```
whereas:
``` math
\begin{equation}
  \boxed{
  \text{MTT measurement requires visibility loss plus Nil survivor-basin stabilization.}
  }
\end{equation}
```

In this sense, MTT is compatible with decoherence but does not identify decoherence alone with a completed measurement theory.

## Consistent histories

Consistent-histories approaches assign probabilities to sets of histories when interference between histories is sufficiently suppressed. The key condition is that a set of histories must satisfy a consistency or decoherence condition before classical probabilities can be assigned.

MTT has a closely related structure. A measurement or history context supplies a Lens decomposition, branch damping suppresses off-diagonal interference, and Nil survivor basins stabilize records.

In MTT notation:
``` math
\begin{equation}
  \text{history branches}
  \quad\leadsto\quad
  \rho_{ab}
  \quad\leadsto\quad
  D_{ab}\rho_{ab}
  \quad\leadsto\quad
  B_i^{(\mathsf M)}.
\end{equation}
```

The distinction is that MTT embeds this logic in the broader finite admissibility operator
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
Thus histories are not the only context in which projection matters. They are one instance of the more general Circle–Lens–Nil grammar.

## Relational quantum mechanics

Relational quantum mechanics emphasizes that quantum states and facts are relative to systems or interactions. MTT agrees that measurement context matters. In MTT language, this context-dependence is Lens structure.

A measurement record is not an absolute context-free primitive. It is a finite survivor record relative to a measurement context:
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{facts are Lens-relative and Nil-stabilized.}
  }
\end{equation}
```

The difference is that MTT gives an explicit finite-kernel architecture for this contextuality:
``` math
\begin{equation}
  B_{\rm adm}^{\mathsf M}
  =
  P_{\mathsf M}\chi(A_{\mathsf M})
  \mathrm e^{-\tau_{\mathsf M}A_{\mathsf M}}
  \chi(A_{\mathsf M})P_{\mathsf M}.
\end{equation}
```

Therefore MTT can be read as a finite coherent projection realization of a relational idea.

## Quantum field theory

Quantum field theory already treats particles as excitations of fields rather than classical point objects. MTT is compatible with this. The MTT contribution is not to reintroduce classical particles but to reinterpret pointlike field-theoretic objects as sharp projection shadows.

In ordinary QFT, one often uses:
``` math
\begin{equation}
  \delta(x-y),
\end{equation}
```
local fields,
``` math
\begin{equation}
  \phi(x),
\end{equation}
```
and pointlike vertices,
``` math
\begin{equation}
  \int \phi(x)^4\,\,\mathrm d^dx.
\end{equation}
```

MTT reads these as limiting structures:
``` math
\begin{equation}
  \delta(x-y)
  =
  \text{sharp local shadow},
\end{equation}
```
``` math
\begin{equation}
  \phi(x)
  =
  \text{local field representative},
\end{equation}
```
and
``` math
\begin{equation}
  \text{point vertex}
  =
  \text{sharp limit of finite coherent overlap}.
\end{equation}
```

In the Euclidean scalar benchmark, this replacement is explicit:
``` math
\begin{equation}
  \delta^{(d)}(x-y)
  \rightsquigarrow
  (4\pi\tau)^{-d/2}
  \exp\left(-\frac{|x-y|^2}{4\tau}\right).
\end{equation}
```

In the FP/fiber realization, the more physical statement is:
``` math
\begin{equation}
  \text{4D local QFT}
  =
  \text{zero-mode low-resolution shadow of fiber-coherent admissibility}.
\end{equation}
```

Thus MTT does not reject QFT. It reframes the ideal local objects of QFT as effective shadows of finite coherent structure.

## Renormalization group and effective field theory

The renormalization group already teaches that physics depends on scale. Effective field theory organizes low-energy descriptions without requiring the same variables to remain valid at arbitrarily high energy.

MTT agrees with this scale-dependent view. The finite coherent scale
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau},
\end{equation}
```
or
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim\tau^{-1/2},
\end{equation}
```
marks the scale at which finite admissibility becomes resolvable.

At energies
``` math
\begin{equation}
  E\ll\Lambda_{\rm eff},
\end{equation}
```
the pointlike effective description is valid. At energies
``` math
\begin{equation}
  E\sim\Lambda_{\rm eff},
\end{equation}
```
finite coherent structure may become visible.

The difference from ordinary EFT is that $`\tau`$ is not merely an arbitrary cutoff. In the FP realization,
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
so the coherent scale is tied to the internal spectral gap:
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is compatible with EFT, but gives the finite scale a geometric admissibility
  interpretation.}
  }
\end{equation}
```

## Kaluza–Klein theory

The fixed-point realization of MTT has an explicit Kaluza–Klein-style backbone. The total space is
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
or a compact internal fiber geometry over a four-dimensional Lorentzian base. Internal spectra produce zero modes and massive internal excitations:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j.
\end{equation}
```

After dimensional reduction, the schematic four-dimensional propagator is
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```

The zero mode satisfies
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
and is undamped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Nonzero internal modes are damped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}<1,
  \qquad
  \mu_j^2>0.
\end{equation}
```

Thus MTT should be honest about the KK connection:
``` math
\begin{equation}
  \boxed{
  \text{FP-realized MTT is KK-compatible and uses a compact internal spectral backbone.}
  }
\end{equation}
```

The distinction is:
``` math
\begin{equation}
  \boxed{
  \text{ordinary KK: compact dimensions produce mode towers;}
  }
\end{equation}
```
whereas:
``` math
\begin{equation}
  \boxed{
  \text{MTT/FP: compact dimensions plus finite coherent admissibility produce projection
  shadows across sectors.}
  }
\end{equation}
```

MTT is therefore not “unrelated to KK.” It is a projection-theoretic extension of a KK-compatible geometric structure.

## String theory

String theory also replaces point particles with extended objects and uses extra dimensions, compactification, worldsheet conformal structure, and dualities. It provides one of the most developed frameworks in which pointlike particles emerge as effective low-energy shadows.

MTT shares several broad themes:

1.  pointlike objects are not fundamental primitives;

2.  compact internal geometry matters;

3.  observed four-dimensional physics may be a lower-dimensional shadow;

4.  dualities can relate apparently different descriptions;

5.  gauge and gravity are deeply geometric.

However, MTT does not assume that the fundamental object is a string or brane. Its central object is the finite coherent admissibility operator:
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```

Thus the comparison is:
``` math
\begin{equation}
  \boxed{
  \text{string theory: extended fundamental objects and worldsheet consistency;}
  }
\end{equation}
```
while:
``` math
\begin{equation}
  \boxed{
  \text{MTT: finite coherent admissibility and projection shadows.}
  }
\end{equation}
```

The two are not necessarily incompatible. A string compactification could, in principle, supply sectoral data $`A,P,\chi,\tau`$ for an MTT-style finite admissibility analysis. But MTT does not require the full string-theoretic machinery in order to state its structural claim.

## Holography

Holography teaches that bulk gravitational physics may be encoded in lower-dimensional boundary data. It emphasizes that locality and spacetime geometry can be emergent or representation-dependent.

MTT is compatible with this lesson. In MTT language, holography is a powerful Lens principle:
``` math
\begin{equation}
  \text{bulk geometry}
  \quad
  \leftrightarrow
  \quad
  \text{boundary representation}.
\end{equation}
```

The MTT contribution is to place this among a broader class of projection shadows. The same logic that makes geometry representation-dependent also appears in:

1.  wave/particle duality;

2.  gauge quotienting;

3.  measurement context;

4.  entanglement factorization;

5.  finite internal-mode projection.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{holography is a deep geometric Lens duality;}
  }
\end{equation}
```
whereas:
``` math
\begin{equation}
  \boxed{
  \text{MTT treats Lens projection as a general structural principle across sectors.}
  }
\end{equation}
```

## Loop and holonomy approaches

Loop quantum gravity and related holonomy approaches emphasize connections, holonomies, spin networks, fluxes, and diffeomorphism-compatible geometric labels.

MTT shares the importance of:

1.  holonomy as Circle structure;

2.  diffeomorphism quotienting as Lens structure;

3.  discrete geometric labels as Nil survivor labels;

4.  constraint compatibility in gravity.

The gravitational MTT operator has the schematic form
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
\end{equation}
```

This is not a replacement for a full loop quantization. Rather, it states what any MTT-compatible gravitational sector must supply:
``` math
\begin{equation}
  A_{\rm grav},
  \qquad
  P_{\rm diff},
  \qquad
  \chi,
  \qquad
  \tau.
\end{equation}
```

A loop or holonomy theory could potentially provide these data. MTT then supplies the finite coherent projection grammar.

## Causal set and discrete spacetime approaches

Discrete spacetime approaches posit that spacetime may be fundamentally discrete or partially ordered. MTT does not begin by assuming spacetime discreteness. Instead, it treats discrete labels as admissible survivor labels.

Thus MTT distinguishes:
``` math
\begin{equation}
  \text{discrete substrate}
\end{equation}
```
from
``` math
\begin{equation}
  \text{discrete survivor shadow}.
\end{equation}
```

A finite detector record is discrete, but this does not automatically imply that spacetime is a lattice. A compact fiber spectrum is discrete, but this does not automatically imply that the base is discrete.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{MTT allows discrete effective labels without requiring spacetime to be fundamentally
  discrete.}
  }
\end{equation}
```

If a discrete spacetime model supplies a sectoral admissibility operator and coherent projector, it may be expressible in MTT terms. But discreteness is not the starting axiom of MTT.

## Nonlocal field theories

Many nonlocal field theories introduce form factors such as
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
or other functions of the d’Alembertian. These theories often face difficulties with causality, unitarity, analyticity, and extra degrees of freedom.

MTT differs sharply from naive Lorentzian nonlocal field theory. The fundamental Lorentzian principle is:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  \quad
  \text{as a naive indefinite heat operator}.
  }
\end{equation}
```

Instead, MTT uses:

1.  positive internal/fiber operators;

2.  positive spatial Cauchy-slice operators;

3.  Hamiltonian or constraint-compatible operators;

4.  gauge-quotiented physical operators;

5.  diffeomorphism-compatible geometric operators;

6.  bounded equal-time kernels that preserve the principal hyperbolic symbol.

Thus MTT finite kernels are not arbitrary acausal nonlocal modifications. They are admissible projection kernels constrained by positivity, quotienting, and causal structure.

## Open quantum systems

Open quantum systems provide the mathematical language of channels, decoherence, reduced states, and environment-induced dynamics. MTT uses this language in the measurement and branch-damping layer.

The Schur damping theorem is an open-system result:
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1
  \quad
  \Rightarrow
  \quad
  \rho\mapsto D\circ\rho
  \text{ is CPTP}.
\end{equation}
```

MTT adds the survivor-basin layer:
``` math
\begin{equation}
  D\circ\rho
  \to
  B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{open-system channels describe admissible damping;}
  }
\end{equation}
```
while:
``` math
\begin{equation}
  \boxed{
  \text{MTT adds record stabilization as Nil basin selection.}
  }
\end{equation}
```

## Hidden-variable and collapse theories

Hidden-variable theories attempt to restore definite underlying variables. Collapse theories modify the dynamics to produce definite outcomes.

MTT is different from both.

It does not introduce pre-existing local classical variables for every possible measurement context. In Bell-type situations, MTT treats local records as Nil shadows of a joint coherent sector, not as pre-existing classical values.

It also does not postulate a universal stochastic collapse law as the primitive dynamics. Instead, it treats record formation as survivor-basin stabilization in a finite measurement context:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is not a local hidden-variable theory and not a primitive collapse theory.}
  }
\end{equation}
```

It is a finite coherent projection theory with contextual survivor records.

## Relation to ordinary quantum mechanics

Ordinary quantum mechanics is recovered when:

1.  the coherent sector is fixed;

2.  the relevant finite width is below experimental resolution;

3.  the zero modes dominate;

4.  measurement effects reproduce the usual POVM or PVM predictions;

5.  basin measures reproduce Born probabilities.

Then MTT reduces operationally to the usual formalism:
``` math
\begin{equation}
  p(i)=\operatorname{tr}(\rho E_i).
\end{equation}
```

The difference is interpretive and structural. Ordinary quantum mechanics begins with states, observables, and Born probabilities. MTT asks what finite admissibility structure produces:

1.  local particle records;

2.  wave interference;

3.  detector effects;

4.  branch damping;

5.  survivor records;

6.  quantized labels;

7.  entangled joint sectors.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{ordinary quantum mechanics is the effective operational shadow of MTT in sectors
  where the standard POVM/Born structure is recovered.}
  }
\end{equation}
```

## What MTT adds

MTT adds the following structural claims:

1.  Point particles are Dirac-delta shadows of finite coherent kernels.

2.  Waves are spectral phase shadows of the same kernels.

3.  Measurement records are survivor-basin shadows.

4.  Visibility loss is admissible Schur damping.

5.  Gauge theory is Lens quotient structure.

6.  Electromagnetism combines gauge Lens, Circle holonomy, and Nil records.

7.  Gravity is diffeomorphism-compatible geometric projection.

8.  Quantization is admissible survivor-label structure.

9.  Entanglement is non-factorizing joint coherent admissibility.

10. The fixed-point realization gives a KK-compatible compact-fiber source for the finite coherent scale.

The core addition is:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
  }
\end{equation}
```
as a common finite admissibility engine, together with:
``` math
\begin{equation}
  \boxed{
  \mathsf C/\mathsf L/\mathsf N
  }
\end{equation}
```
as the structural grammar of its physical shadows.

## What MTT does not add

MTT does not claim that every existing theory is wrong. It does not claim to have already computed every sectoral observable. It does not claim to replace:

1.  quantum field theory as a computational framework;

2.  gauge theory as the structure of known interactions;

3.  general relativity as the classical theory of gravity;

4.  effective field theory as the low-energy expansion method;

5.  decoherence as the mechanism of visibility loss;

6.  KK or compactification methods where internal geometry is relevant.

Instead, MTT reframes these as sectoral shadows of finite coherent admissibility where the operator data can be supplied:
``` math
\begin{equation}
  A,\qquad P,\qquad \chi,\qquad \tau.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is an organizing and execution framework, not a declaration that existing
  machinery is obsolete.}
  }
\end{equation}
```

## Summary

MTT is compatible with many existing insights but assembles them differently.

It refines complementarity by giving wave and particle a common finite kernel source.

It incorporates decoherence but distinguishes coherence loss from survivor-record selection.

It is compatible with QFT and EFT but treats pointlike local objects as sharp shadows.

It honestly acknowledges its KK-compatible FP backbone:
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
with internal-mode damping:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

It avoids naive Lorentzian nonlocality by rejecting $`e^{-\tau\Box}`$ as the fundamental damping rule.

It aligns with gauge and gravitational quotient structures by requiring:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys},
\end{equation}
```
and
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
\end{equation}
```

The unifying statement is:
``` math
\begin{equation}
  \boxed{
  \text{MTT is a finite coherent admissibility architecture whose physical content appears as
  projection shadows across quantum, gauge, geometric, and measurement sectors.}
  }
\end{equation}
```

# Phenomenology and execution tasks

The preceding sections established the structural claim: finite coherent admissibility gives rise to local delta shadows, spectral wave shadows, measurement records, scattering form factors, gauge quotienting, gravitational projection, quantized survivor labels, and entanglement structure. This section turns to the execution question:

``` math
\begin{equation}
  \boxed{
  \text{What would the framework predict, constrain, or require quantitatively?}
  }
\end{equation}
```

The answer depends on the sectoral data:
``` math
\begin{equation}
  A,\qquad P,\qquad \chi,\qquad \tau,
\end{equation}
```
and, in the fixed-point realization, on the internal geometry:
``` math
\begin{equation}
  M_{10}=Y^4\times X^6.
\end{equation}
```

The main phenomenological message is:

``` math
\begin{equation}
  \boxed{
  \text{ordinary four-dimensional low-energy physics is recovered by undamped zero modes,
  while finite coherent corrections enter through suppressed internal modes, finite overlaps,
  detector profiles, and threshold effects.}
  }
  \label{eq:phenomenology-main-message}
\end{equation}
```

## Geometric origin of the coherence scale

In the fixed-point realization, the admissibility operator is the positive internal operator
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```
The internal fibers are compact, so the nonzero fiber spectrum has a positive gap. Let
``` math
\begin{equation}
  \lambda_\ast>0
\end{equation}
```
denote the relevant uniform spectral gap.

The damping-selected admissibility time is
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
  \label{eq:tau-phenomenology}
\end{equation}
```
where $`C_Q`$ is the discarded-sector constant and $`\epsilon_{\rm adm}`$ is the admissibility tolerance.

If the typical internal radius is $`R`$, then for Laplace-type internal operators,
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2}.
\end{equation}
```
Therefore
``` math
\begin{equation}
  \tau
  \sim
  R^2
  \log\frac{C_Q}{\epsilon_{\rm adm}},
  \label{eq:tau-R-phenomenology}
\end{equation}
```
and
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
  \label{eq:lcoh-R-phenomenology}
\end{equation}
```

The effective energy scale is
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \tau^{-1/2}
  \sim
  \frac{1}{R}
  \left(
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  \right)^{-1/2}.
  \label{eq:Lambdaeff-R-phenomenology}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the finite coherent scale is not arbitrary; it is tied to the internal spectral gap.}
  }
  \label{eq:coherence-scale-geometric-box}
\end{equation}
```

## Zero-mode recovery

Let
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j.
\end{equation}
```
The admissibility weight is
``` math
\begin{equation}
  W_j
  =
  \mathrm e^{-\tau\mu_j^2}.
  \label{eq:mode-weight-phenomenology}
\end{equation}
```

The zero mode satisfies
``` math
\begin{equation}
  \mu_0=0.
\end{equation}
```
Therefore
``` math
\begin{equation}
  W_0=\mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

This gives the central low-energy recovery statement:
``` math
\begin{equation}
  \boxed{
  \text{zero modes are not suppressed by internal finite admissibility.}
  }
  \label{eq:zero-mode-not-suppressed}
\end{equation}
```

Hence ordinary four-dimensional low-energy propagation is recovered from zero-mode sectors. In a scalar benchmark, the effective four-dimensional propagator has the schematic form
``` math
\begin{equation}
  G_{4D}(p)
  =
  \frac{Z_0}{p^2-m_0^2+\mathrm i\epsilon}
  +
  \sum_{j\ge1}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
  \label{eq:4D-propagator-phenomenology}
\end{equation}
```

The first term is the ordinary zero-mode contribution. The remaining terms are suppressed internal excitations.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT corrections are not generic low-energy distortions of the zero mode; they are
  suppressed excitation, overlap, and threshold effects.}
  }
  \label{eq:not-low-energy-distortion}
\end{equation}
```

## Internal excitation scale

The first nonzero internal eigenvalue defines a mass scale
``` math
\begin{equation}
  \mu_1^2\sim\lambda_\ast.
\end{equation}
```
The corresponding internal excitation mass is
``` math
\begin{equation}
  M_{\rm int}\sim\mu_1\sim R^{-1}.
  \label{eq:Mint-R}
\end{equation}
```

The admissibility weight of the first internal excitation is
``` math
\begin{equation}
  W_1
  =
  \mathrm e^{-\tau\mu_1^2}.
\end{equation}
```
If
``` math
\begin{equation}
  \mu_1^2\simeq\lambda_\ast,
\end{equation}
```
then using <a href="#eq:tau-phenomenology" data-reference-type="eqref" data-reference="eq:tau-phenomenology">[eq:tau-phenomenology]</a>,
``` math
\begin{equation}
  W_1
  \simeq
  \exp\left(
    -
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  \right)
  =
  \frac{\epsilon_{\rm adm}}{C_Q}.
  \label{eq:first-mode-weight-phenomenology}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the first internal excitation carries amplitude-level admissibility weight }
  W_1\simeq\epsilon_{\rm adm}/C_Q
  \text{ when } \mu_1^2\simeq\lambda_\ast.
  }
  \label{eq:first-mode-weight-box}
\end{equation}
```

This is a clean structural prediction. However, an observed cross section depends on more than $`W_1`$. It also depends on effective couplings, widths, internal wavefunction overlaps, phase space, spin, gauge representation, background interference, and detector efficiencies.

Therefore:
``` math
\begin{equation}
  \boxed{
  W_j=\mathrm e^{-\tau\mu_j^2}
  \text{ is an amplitude-level admissibility weight, not by itself a universal cross-section
  prediction.}
  }
  \label{eq:weight-not-cross-section}
\end{equation}
```

## Effective four-dimensional tower

The reduced four-dimensional theory contains zero modes and nonzero internal excitations. A generic propagator or response function has the schematic tower form
``` math
\begin{equation}
  G_{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j
    \chi(\mu_j^2)^2
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}.
  \label{eq:generic-effective-tower}
\end{equation}
```

The residues $`Z_j`$ encode internal overlap and normalization. The window
``` math
\begin{equation}
  \chi(\mu_j^2)
\end{equation}
```
selects the admissible spectral band. The damping
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
suppresses nonzero internal modes.

For $`j=0`$,
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
and therefore
``` math
\begin{equation}
  \chi(\mu_0^2)^2\mathrm e^{-\tau\mu_0^2}
  =
  \chi(0)^2.
\end{equation}
```
If
``` math
\begin{equation}
  \chi(0)=1,
\end{equation}
```
then the zero mode is fully retained.

Thus the low-energy consistency condition is:
``` math
\begin{equation}
  \boxed{
  \chi(0)=1,
  \qquad
  Z_0>0,
  \qquad
  \mu_0=0.
  }
  \label{eq:zero-mode-consistency}
\end{equation}
```

## Phenomenological bound template

Suppose an experiment excludes internal excitations below a scale
``` math
\begin{equation}
  M_{\rm exp}.
\end{equation}
```
Then one obtains the template bound
``` math
\begin{equation}
  \mu_1\gtrsim M_{\rm exp}.
\end{equation}
```
Since
``` math
\begin{equation}
  \mu_1\sim R^{-1},
\end{equation}
```
this gives
``` math
\begin{equation}
  R\lesssim M_{\rm exp}^{-1}.
  \label{eq:R-bound-template}
\end{equation}
```

The coherence length then satisfies
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \lesssim
  M_{\rm exp}^{-1}
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
  \label{eq:lcoh-bound-template}
\end{equation}
```

Equivalently,
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \tau^{-1/2}
  \gtrsim
  M_{\rm exp}
  \left(
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  \right)^{-1/2}.
  \label{eq:Lambda-bound-template}
\end{equation}
```

This is the general translation from experimental non-observation to MTT internal scale:
``` math
\begin{equation}
  \boxed{
  \text{bounds on internal excitations}
  \Rightarrow
  \text{bounds on }R,\sqrt{\tau},\Lambda_{\rm eff}.
  }
  \label{eq:bound-translation-box}
\end{equation}
```

Precise numerical values require a specified internal geometry, gauge embedding, coupling normalization, and detector channel.

## Illustrative tolerance benchmark

As an illustrative benchmark, suppose
``` math
\begin{equation}
  C_Q\simeq1
\end{equation}
```
and
``` math
\begin{equation}
  \epsilon_{\rm adm}=10^{-3}.
\end{equation}
```
Then
``` math
\begin{equation}
  \log\frac{C_Q}{\epsilon_{\rm adm}}
  =
  \log(10^3)
  \simeq
  6.9.
\end{equation}
```
Therefore
``` math
\begin{equation}
  \sqrt{\tau}
  \simeq
  2.6R.
  \label{eq:illustrative-sqrttau}
\end{equation}
```
The first-mode admissibility weight, if $`\mu_1^2\simeq\lambda_\ast`$, is
``` math
\begin{equation}
  W_1\simeq10^{-3}.
  \label{eq:illustrative-W1}
\end{equation}
```

This benchmark is useful for scale intuition, but it is not a universal prediction. A different $`\epsilon_{\rm adm}`$, $`C_Q`$, or internal spectrum changes the numerical coefficient.

Thus:
``` math
\begin{equation}
  \boxed{
  \epsilon_{\rm adm}
  \text{ must ultimately be fixed by sectoral admissibility, not chosen by hand.}
  }
  \label{eq:epsadm-execution-task}
\end{equation}
```

## Collider template

Collider signatures arise if internal excitations couple to visible four-dimensional fields. The generic amplitude contribution from an internal excitation $`j`$ is
``` math
\begin{equation}
  \mathcal A_j(p)
  \sim
  g_j^{\rm in}g_j^{\rm out}
  \frac{
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm im_j\Gamma_j},
  \label{eq:collider-amplitude-template}
\end{equation}
```
where
``` math
\begin{equation}
  g_j^{\rm in},\quad g_j^{\rm out}
\end{equation}
```
are effective production and decay couplings, and $`\Gamma_j`$ is the width.

The corresponding observable cross section depends on
``` math
\begin{equation}
  |\mathcal A_{\rm SM}+\sum_j\mathcal A_j|^2.
\end{equation}
```
Therefore, even if the amplitude-level MTT weight is
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2},
\end{equation}
```
the cross-section effect may scale differently depending on interference, widths, and coupling suppression.

The execution tasks for collider phenomenology are:

1.  specify the internal geometry $`X^6`$;

2.  compute $`\mu_j^2`$;

3.  compute internal wavefunction overlaps;

4.  derive effective couplings $`g_j`$;

5.  impose gauge and representation constraints;

6.  compute widths $`\Gamma_j`$;

7.  calculate observable cross sections;

8.  compare with collider exclusions.

Thus the robust MTT collider statement is:
``` math
\begin{equation}
  \boxed{
  \text{internal excitations appear, if at all, as tower-like states with admissibility weights }
  \mathrm e^{-\tau\mu_j^2}.
  }
  \label{eq:collider-robust-statement}
\end{equation}
```

## Precision-electroweak and QED templates

Low-energy precision observables receive corrections only if internal excitations couple to the relevant sector. A generic heavy-mode correction to a low-energy observable $`\mathcal O`$ has the form
``` math
\begin{equation}
  \delta\mathcal O
  \sim
  \sum_{j\ge1}
  C_j
  \mathrm e^{-\tau\mu_j^2}
  \left(
    \frac{E_{\rm obs}}{\mu_j}
  \right)^{d_j},
  \label{eq:precision-correction-template}
\end{equation}
```
where:
``` math
\begin{align}
  C_j &: \text{effective coupling/overlap coefficient},\\
  E_{\rm obs} &: \text{observable energy scale},\\
  d_j &: \text{operator-dimension or decoupling power}.
\end{align}
```

When
``` math
\begin{equation}
  E_{\rm obs}\ll\mu_1,
\end{equation}
```
such corrections are suppressed both by heavy-mode decoupling and by the admissibility factor
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{precision low-energy tests constrain MTT primarily through suppressed virtual internal
  modes and effective operators.}
  }
  \label{eq:precision-tests-box}
\end{equation}
```

A complete analysis must derive the coefficients $`C_j`$ from the internal geometry and gauge embedding.

## Coulomb-law and finite-source tests

The Euclidean finite-source benchmark replaces a point charge by
``` math
\begin{equation}
  \rho_\tau(\mathbf r)
  =
  q(4\pi\tau)^{-3/2}
  \exp\left(
    -\frac{r^2}{4\tau}
  \right),
\end{equation}
```
with potential
``` math
\begin{equation}
  \Phi_\tau(r)
  =
  \frac{q}{4\pi r}
  \operatorname{erf}
  \left(
    \frac{r}{2\sqrt{\tau}}
  \right).
  \label{eq:finite-Coulomb-template}
\end{equation}
```

This benchmark shows how a finite four-dimensional source profile would soften a Coulomb singularity.

However, in the FP/fiber realization, the finite width is primarily internal unless a physical four-dimensional finite source is derived. Therefore four-dimensional Coulomb deviations should be described by internal-mode exchange:
``` math
\begin{equation}
  \Phi(r)
  =
  \frac{q}{4\pi r}
  \left[
    1+
    \sum_{j\ge1}
    c_j
    \mathrm e^{-\tau\mu_j^2}
    \mathrm e^{-\mu_j r}
  \right],
  \label{eq:Coulomb-internal-mode-template}
\end{equation}
```
where $`c_j`$ depends on the internal gauge-sector overlap.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{direct Gaussian Coulomb smearing is a benchmark; FP-realized Coulomb corrections are
  internal-mode Yukawa-type corrections unless a 4D finite source is derived.}
  }
  \label{eq:Coulomb-caution-box}
\end{equation}
```

## Gravitational short-distance template

A gravitational analogue involves finite stress-energy profiles or internal-mode corrections. A point-mass source may be replaced schematically by
``` math
\begin{equation}
  T_{\mu\nu}^{\rm adm}(x)
  \sim
  m u_\mu u_\nu K_{\rm adm}(x,x_0),
\end{equation}
```
but only if the resulting source satisfies
``` math
\begin{equation}
  \nabla_\mu T^{\mu\nu}=0
\end{equation}
```
and the gravitational constraints.

In the FP/fiber realization, gravitational corrections may instead appear through suppressed internal modes:
``` math
\begin{equation}
  V_{\rm grav}(r)
  =
  -\frac{Gm_1m_2}{r}
  \left[
    1+
    \sum_{j\ge1}
    a_j
    \mathrm e^{-\tau\mu_j^2}
    \mathrm e^{-\mu_j r}
  \right].
  \label{eq:gravity-yukawa-template}
\end{equation}
```

The coefficients $`a_j`$ depend on the gravitational sector, internal geometry, boundary data, and physical spin/geometric projection.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{short-distance gravity constrains internal geometric modes only after the
  diffeomorphism-compatible sector is derived.}
  }
  \label{eq:gravity-phenomenology-box}
\end{equation}
```

## Measurement phenomenology

Measurement experiments constrain the branch-damping and survivor-basin layer.

For a two-branch interferometer, the visibility law is
``` math
\begin{equation}
  V_{\rm obs}
  =
  |D_{12}|V_0.
  \label{eq:visibility-phenomenology}
\end{equation}
```
If
``` math
\begin{equation}
  D_{12}
  =
  \mathrm e^{-\tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}},
\end{equation}
```
then
``` math
\begin{equation}
  \log\frac{V_0}{V_{\rm obs}}
  =
  \tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}.
  \label{eq:visibility-log-law}
\end{equation}
```

Thus interferometry can constrain:

1.  detector-induced branch distinguishability $`\Lambda_{12}^{(\mathsf M)}`$;

2.  measurement damping scale $`\tau_{\mathsf M}`$;

3.  whether damping is reversible;

4.  whether survivor-basin capture has occurred.

The key distinction is:
``` math
\begin{equation}
  \boxed{
  \text{visibility loss measures branch damping, not directly outcome probability.}
  }
\end{equation}
```

Outcome frequencies require basin measures:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{
    \mu(B_i^{(\mathsf M)})
  }{
    \sum_j\mu(B_j^{(\mathsf M)})
  }.
\end{equation}
```

Thus a measurement execution program must separately fit:
``` math
\begin{equation}
  D_{ab}^{(\mathsf M)}
\end{equation}
```
and
``` math
\begin{equation}
  \mu(B_i^{(\mathsf M)}).
\end{equation}
```

## Quantum eraser and weak-measurement tests

Weak measurement and quantum eraser experiments are useful because they separate branch marking from irreversible record formation.

Let marker states be
``` math
\begin{equation}
  |m_1\rangle,
  \qquad
  |m_2\rangle.
\end{equation}
```
The surviving coherence is controlled by
``` math
\begin{equation}
  D_{12}
  =
  \langle m_2|m_1\rangle.
  \label{eq:marker-overlap-phenomenology}
\end{equation}
```

If
``` math
\begin{equation}
  |D_{12}|<1,
\end{equation}
```
visibility is reduced. If the marker degrees of freedom are later measured in a recombining basis, conditional interference may reappear.

MTT predicts the distinction:
``` math
\begin{equation}
  \boxed{
  \text{reversible branch marking}
  \neq
  \text{irreversible survivor-basin capture}.
  }
  \label{eq:weak-eraser-distinction}
\end{equation}
```

Thus the relevant experimental observables are:

1.  raw visibility;

2.  conditional visibility after erasure;

3.  marker overlap;

4.  record stability;

5.  environmental irreversibility;

6.  basin capture probability.

## Entanglement and no-signaling tests

Entanglement phenomenology constrains the joint coherent-sector and measurement-basin structure.

For local settings $`x,y`$, outcomes $`a,b`$, and joint probabilities $`p(a,b|x,y)`$, MTT must reproduce:
``` math
\begin{equation}
  p(a,b|x,y)
  =
  \operatorname{tr}\left[
    \rho_{AB}
    E_{ab}^{(x,y)}
  \right]
\end{equation}
```
in standard quantum benchmark sectors.

It must also satisfy no-signaling:
``` math
\begin{equation}
  \sum_b p(a,b|x,y)
  =
  \sum_b p(a,b|x,y')
  \label{eq:no-signaling-phenomenology-A}
\end{equation}
```
and
``` math
\begin{equation}
  \sum_a p(a,b|x,y)
  =
  \sum_a p(a,b|x',y).
  \label{eq:no-signaling-phenomenology-B}
\end{equation}
```

The MTT execution task is to identify:
``` math
\begin{equation}
  A_{AB},
  \qquad
  P_{AB},
  \qquad
  \chi_{AB},
  \qquad
  \tau_{AB},
\end{equation}
```
and the joint survivor basins
``` math
\begin{equation}
  B_{ab}^{(x,y)}
\end{equation}
```
such that the basin measure reproduces quantum correlations without enabling signaling.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{entanglement tests constrain non-factorizing admissibility and joint basin measure.}
  }
  \label{eq:entanglement-tests-box}
\end{equation}
```

## Gauge-sector execution tasks

A phenomenologically viable gauge sector must supply:
``` math
\begin{equation}
  A_{\rm gauge},
  \qquad
  P_{\rm phys},
  \qquad
  \chi_{\rm gauge},
  \qquad
  \tau_{\rm gauge}.
\end{equation}
```
It must also satisfy:

1.  correct gauge group;

2.  correct representation content;

3.  anomaly cancellation;

4.  Ward or Slavnov–Taylor identity preservation;

5.  current conservation;

6.  positive physical-state space;

7.  undamped observed zero modes;

8.  admissibly suppressed internal excitations;

9.  agreement with precision and collider data.

The effective gauge-sector tower has the schematic form
``` math
\begin{equation}
  D_{\mu\nu}^{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}
  P_{\mu\nu}^{(j)}(p).
\end{equation}
```

The zero-mode consistency condition is:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  \mathrm e^{-\tau\mu_0^2}=1,
\end{equation}
```
with the correct observed gauge boson sector after symmetry breaking.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge phenomenology requires quotient-compatible towers, not arbitrary damped
  propagators.}
  }
  \label{eq:gauge-phenomenology-box}
\end{equation}
```

## Gravity-sector execution tasks

A phenomenologically viable gravity sector must supply:
``` math
\begin{equation}
  A_{\rm grav},
  \qquad
  P_{\rm diff},
  \qquad
  \chi_{\rm grav},
  \qquad
  \tau_{\rm grav}.
\end{equation}
```
It must also satisfy:

1.  diffeomorphism compatibility;

2.  Hamiltonian and momentum constraint preservation;

3.  recovery of classical general relativity;

4.  positive physical graviton sector in perturbative regimes;

5.  stress-energy conservation;

6.  causal propagation;

7.  consistency with weak-field and gravitational-wave observations;

8.  admissible treatment of horizons and boundaries.

The weak-field benchmark is:
``` math
\begin{equation}
  B_{\rm grav}^{\rm lin}
  =
  P_{\rm TT}\chi(A_{\rm TT})
  \mathrm e^{-\tau A_{\rm TT}}
  \chi(A_{\rm TT})P_{\rm TT}.
  \label{eq:weak-gravity-execution}
\end{equation}
```

The full nonperturbative task is much harder and requires a genuine diffeomorphism-compatible state space.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravity phenomenology must be computed after geometric projection and constraint
  preservation.}
  }
  \label{eq:gravity-execution-box}
\end{equation}
```

## Standard Model embedding tasks

A complete Standard Model embedding requires the internal geometry to generate or support:
``` math
\begin{equation}
  SU(3)\times SU(2)\times U(1),
\end{equation}
```
fermion representations, chirality, generations, Yukawa structure, anomaly cancellation, symmetry breaking, and observed low-energy couplings.

In MTT terms, the execution problem is to derive:
``` math
\begin{equation}
  A_{\rm SM},
  \qquad
  P_{\rm SM},
  \qquad
  \chi_{\rm SM},
  \qquad
  \tau_{\rm SM},
\end{equation}
```
from the internal/fiber geometry and quotient structure.

The minimal checklist is:

1.  recover the correct gauge group;

2.  recover the correct chiral matter;

3.  cancel anomalies;

4.  produce three observed generations or explain their effective emergence;

5.  derive Yukawa and mixing structures;

6.  recover observed gauge couplings at low energy;

7.  suppress unobserved internal excitations;

8.  preserve Lorentzian and gauge admissibility.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{Standard Model closure is a concrete execution program, not an assumption of the
  structural theorem.}
  }
  \label{eq:SM-closure-box}
\end{equation}
```

## Predictions versus templates

It is useful to distinguish three levels of phenomenological statement.

#### Level 1: structural predictions.

These follow from the architecture:

1.  zero modes are undamped by internal admissibility;

2.  nonzero internal modes carry weights $`\mathrm e^{-\tau\mu_j^2}`$;

3.  $`\tau`$ is tied to the spectral gap;

4.  pointlike behavior is recovered below resolution;

5.  branch visibility is controlled by admissible damping matrices;

6.  gauge and gravity filters must preserve quotient/constraint structure.

#### Level 2: model templates.

These require a chosen internal geometry and sectoral operators:

1.  effective tower propagators;

2.  Yukawa corrections;

3.  collider resonance templates;

4.  precision observable corrections;

5.  weak-field gravity corrections.

#### Level 3: numerical predictions.

These require full sectoral execution:

1.  internal spectrum;

2.  wavefunction overlaps;

3.  gauge representation content;

4.  couplings;

5.  widths;

6.  detector acceptances;

7.  renormalization and matching.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{this paper establishes Level 1 and supplies Level 2 templates; Level 3 is future
  sectoral computation.}
  }
  \label{eq:levels-box}
\end{equation}
```

## A compact execution table

The core phenomenological quantities are:

<div class="center">

| Quantity | Symbol | MTT/FP meaning |
|:--:|:--:|:--:|
| Internal radius | $`R`$ | compact fiber size |
| Fiber spectral gap | $`\lambda_\ast`$ | first nonzero admissibility gap |
| Coherent time | $`\tau`$ | damping-selected admissibility scale |
| Coherent length | $`\ell_{\rm coh}`$ | $`\sqrt{\tau}`$ |
| Effective scale | $`\Lambda_{\rm eff}`$ | $`\tau^{-1/2}`$ |
| First excitation | $`\mu_1`$ | first nonzero internal mass scale |
| Mode weight | $`W_j`$ | $`\mathrm e^{-\tau\mu_j^2}`$ |
| Visibility factor | $`D_{ab}`$ | branch coherence survival |
| Basin measure | $`\mu(B_i)`$ | outcome-frequency weight |

</div>

The key relations are:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2},
\end{equation}
```
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau},
\end{equation}
```
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \tau^{-1/2},
\end{equation}
```
and
``` math
\begin{equation}
  W_j
  =
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

## What would falsify or constrain the framework

The framework can be constrained or falsified at several levels.

#### Analytic falsification.

If a proposed sectoral $`A`$, $`P`$, $`\chi`$, $`\tau`$ fails positivity, boundedness, quotient compatibility, or causal admissibility, that sectoral implementation fails.

#### Gauge falsification.

If the finite filter violates Ward identities, Slavnov–Taylor identities, BRST cohomology, or anomaly cancellation, the gauge implementation fails.

#### Gravity falsification.

If the gravitational filter violates constraints, stress-energy conservation, or diffeomorphism compatibility, the gravitational implementation fails.

#### Phenomenological falsification.

If a specified internal geometry predicts unsuppressed excitations, deviations, or new couplings already excluded by experiment, that model is ruled out or constrained.

#### Measurement falsification.

If a proposed damping matrix is not positive semidefinite, or if its visibility predictions fail controlled interferometry, that measurement model fails.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is not immune to falsification; each sectoral realization must satisfy analytic,
  quotient, causal, and observational tests.}
  }
  \label{eq:falsification-box}
\end{equation}
```

## Summary

The phenomenological content of the fixed-point realization is organized by the internal spectral gap:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
\end{equation}
```
For an internal scale $`R`$,
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2},
\end{equation}
```
so
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
\end{equation}
```

Zero modes are undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
Nonzero internal modes are suppressed:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

The generic effective tower is:
``` math
\begin{equation}
  G_{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j\chi(\mu_j^2)^2\mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```

The robust phenomenological predictions are structural:

1.  low-energy zero-mode recovery;

2.  suppressed internal excitations;

3.  finite coherent scale tied to the internal spectral gap;

4.  visibility damping controlled by positive Schur channels;

5.  gauge and gravity corrections constrained by quotient compatibility;

6.  pointlike behavior recovered below resolution.

Precise numerical predictions require a completed sectoral model.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT becomes predictive when the internal geometry, sectoral projectors, admissibility
  windows, and basin measures are explicitly computed.}
  }
\end{equation}
```

# Domain of validity and failure modes

The previous section described the phenomenological execution program. This section records the domain of validity of the framework and the main ways in which a proposed MTT realization can fail.

This is necessary because the finite coherent admissibility operator
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
is not automatically physical for arbitrary choices of $`A`$, $`P`$, $`\chi`$, and $`\tau`$. The operator is meaningful only when the data are admissible in the relevant sector.

The central rule is:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent filtering is physical only when positivity, quotient consistency,
  Lorentzian admissibility, and sectoral constraints are preserved.}
  }
  \label{eq:failure-central-rule}
\end{equation}
```

Thus this section is not merely defensive. It identifies what must be proven in any serious sectoral realization.

## General admissibility requirements

A sectoral MTT construction begins with
``` math
\begin{equation}
  (\mathcal H,A,P,\chi,\tau).
\end{equation}
```
The basic admissibility requirements are:

1.  $`A`$ must be positive, or positive after projection to the physical sector:
    ``` math
    \begin{equation}
        A\ge0.
    \end{equation}
    ```

2.  $`P`$ must be a genuine projector:
    ``` math
    \begin{equation}
        P=P^\ast=P^2.
    \end{equation}
    ```

3.  $`\chi(A)`$ must be a bounded admissible spectral window:
    ``` math
    \begin{equation}
        0\le\chi(A)\le I
    \end{equation}
    ```
    in the clean spectral case.

4.  $`\tau`$ must have the correct dimension and physical origin:
    ``` math
    \begin{equation}
        [\tau]=L^2=E^{-2}.
    \end{equation}
    ```

5.  The finite operator
    ``` math
    \begin{equation}
        B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
    \end{equation}
    ```
    must be bounded on the intended Hilbert or Sobolev scale.

6.  Gauge, diffeomorphism, and measurement constraints must be preserved where relevant.

7.  The Lorentzian implementation must not use a naive indefinite heat operator
    ``` math
    \begin{equation}
        \mathrm e^{-\tau\Box}
    \end{equation}
    ```
    as its fundamental damping rule.

If any of these fail, the proposed construction is not an admissible MTT sector.

## Failure mode I: calling $`B_{\rm adm}`$ a projector

The first failure is conceptual but important. The full operator
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
is not generally a projector. A projector must satisfy
``` math
\begin{equation}
  Q^2=Q.
\end{equation}
```
In a diagonal spectral case, $`B_{\rm adm}`$ has weights
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```
Unless
``` math
\begin{equation}
  w_n\in\{0,1\}
\end{equation}
```
for every mode, one has
``` math
\begin{equation}
  B_{\rm adm}^2\neq B_{\rm adm}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  P\text{ is the projector; }B_{\rm adm}\text{ is the finite coherent admissibility operator.}
  }
  \label{eq:Badm-not-projector-failure}
\end{equation}
```

Calling $`B_{\rm adm}`$ a projector obscures the finite filtering role of $`\chi(A)\mathrm e^{-\tau A}\chi(A)`$.

## Failure mode II: nonpositive admissibility operator

The damping factor
``` math
\begin{equation}
  \mathrm e^{-\tau A}
\end{equation}
```
is a genuine damping factor only when $`A`$ is positive in the relevant sector.

If $`A`$ has negative spectrum, then modes with
``` math
\begin{equation}
  \lambda<0
\end{equation}
```
are amplified:
``` math
\begin{equation}
  \mathrm e^{-\tau\lambda}>1.
\end{equation}
```
This is not Nil damping. It is instability.

Thus:
``` math
\begin{equation}
  \boxed{
  A\ge0
  \text{ is not optional in the clean finite-filter theorem.}
  }
  \label{eq:positive-A-required-failure}
\end{equation}
```

In gauge and gravity sectors, positivity may only hold after physical projection or constraint reduction. In those cases, the reduced or projected operator must be positive on the physical sector.

## Failure mode III: naive Lorentzian heat flow

The most serious failure is to set
``` math
\begin{equation}
  A=\Box
\end{equation}
```
in Lorentzian signature and write
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
as if it were an ordinary heat operator.

The d’Alembertian is hyperbolic and indefinite. Therefore $`\mathrm e^{-\tau\Box}`$ is not the Lorentzian analogue of Euclidean heat flow. A naive expression of this type may introduce:

1.  acausal tails;

2.  infinite time-derivative instabilities;

3.  ghost-like poles;

4.  loss of unitarity;

5.  analytic continuation ambiguity;

6.  violation of gauge or gravitational constraints.

The Lorentzian admissibility principle is:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  \quad
  \text{as a fundamental damping operator.}
  }
  \label{eq:A-not-box-failure}
\end{equation}
```

The admissible alternatives are positive internal/fiber operators, positive spatial Cauchy-slice operators, Hamiltonian or constraint-compatible operators, gauge-quotiented operators, and diffeomorphism-compatible geometric operators.

## Failure mode IV: uncontrolled base diffusion

Some fixed-point constructions may introduce a regularized operator
``` math
\begin{equation}
  A_\varepsilon
  =
  A_{\rm int}
  +
  \varepsilon A_{\rm base},
  \qquad
  \varepsilon\ge0.
\end{equation}
```
This can be useful analytically. However, if $`A_{\rm base}`$ represents base diffusion in a Lorentzian direction, then it cannot automatically be interpreted as physical damping.

The clean physical FP/MTT reading is:
``` math
\begin{equation}
  \varepsilon=0,
\end{equation}
```
so that
``` math
\begin{equation}
  A_\varepsilon=A_{\rm int}.
\end{equation}
```
If
``` math
\begin{equation}
  \varepsilon>0,
\end{equation}
```
then the base term must be justified as:

1.  a positive spatial Cauchy-slice operator;

2.  a Euclidean analytic regulator later removed;

3.  a Hamiltonian or constraint-compatible positive operator;

4.  or a physically derived detector/source profile.

Thus:
``` math
\begin{equation}
  \boxed{
  \varepsilon>0
  \text{ is not automatically physical Lorentzian damping.}
  }
  \label{eq:epsilon-failure}
\end{equation}
```

## Failure mode V: invalid sharp-limit reasoning

The Dirac delta appears as a sharp limit:
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
\end{equation}
```
This does not mean that every finite kernel may be replaced by a delta in every calculation.

The delta approximation is valid only when the coherent width is below the relevant resolution:
``` math
\begin{equation}
  \ell_{\rm coh}\ll\ell_{\rm res},
\end{equation}
```
or equivalently,
``` math
\begin{equation}
  E_{\rm probe}\ll\Lambda_{\rm eff}.
\end{equation}
```

If
``` math
\begin{equation}
  E_{\rm probe}\sim\Lambda_{\rm eff},
\end{equation}
```
then finite-width corrections may matter.

Thus:
``` math
\begin{equation}
  \boxed{
  \delta\text{-locality is a low-resolution approximation, not an exact physical primitive.}
  }
  \label{eq:delta-approximation-failure}
\end{equation}
```

A proposed MTT calculation fails if it uses the delta limit outside its resolution domain.

## Failure mode VI: arbitrary spectral windows

The spectral window
``` math
\begin{equation}
  \chi(A)
\end{equation}
```
cannot be chosen arbitrarily if the goal is physical prediction. It must reflect sectoral admissibility.

In the clean bounded case one requires
``` math
\begin{equation}
  0\le\chi(A)\le I.
\end{equation}
```
If $`\chi`$ amplifies modes, breaks gauge identities, violates constraints, or excludes required zero modes, the construction fails.

In particular, low-energy recovery usually requires
``` math
\begin{equation}
  \chi(0)=1.
\end{equation}
```
If
``` math
\begin{equation}
  \chi(0)=0,
\end{equation}
```
then the zero mode is removed and ordinary low-energy physics is not recovered.

Thus:
``` math
\begin{equation}
  \boxed{
  \chi(A)
  \text{ must be an admissibility window, not an arbitrary regulator.}
  }
  \label{eq:window-failure}
\end{equation}
```

## Failure mode VII: noncommuting projectors treated as diagonal

The modal formula
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}
\end{equation}
```
is valid only when
``` math
\begin{equation}
  [P,A]=0.
\end{equation}
```

If
``` math
\begin{equation}
  [P,A]\neq0,
\end{equation}
```
then $`P`$ and $`A`$ cannot generally be diagonalized together. The operator
``` math
\begin{equation}
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
may still be meaningful, but its behavior must be checked by operator estimates.

A calculation fails if it assumes diagonal weights in a noncommuting sector without proof.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{noncommuting sectoral projections require operator-level admissibility checks.}
  }
  \label{eq:noncommuting-failure}
\end{equation}
```

This matters especially in measurement, gauge, and gravity sectors.

## Failure mode VIII: invalid branch damping

Branch damping is represented by
``` math
\begin{equation}
  \rho\mapsto D\circ\rho.
\end{equation}
```
This map is physically valid only if
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```
If $`D`$ is not positive semidefinite, then the map may fail to be completely positive. If $`D_{aa}\neq1`$, then trace preservation may fail unless additional loss channels are included.

For exponential damping
``` math
\begin{equation}
  D_{ab}=\mathrm e^{-\tau\Lambda_{ab}},
\end{equation}
```
one cannot choose $`\Lambda_{ab}`$ arbitrarily. A sufficient condition is that $`\Lambda`$ is conditionally negative definite with zero diagonal.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{not every visibility law is a valid quantum damping law.}
  }
  \label{eq:visibility-law-failure}
\end{equation}
```

A proposed measurement model fails if its damping matrix does not define a completely positive trace-preserving channel.

## Failure mode IX: confusing decoherence with outcome selection

Decoherence suppresses off-diagonal terms:
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab}.
\end{equation}
```
It does not by itself specify which detector record occurs.

MTT separates:
``` math
\begin{equation}
  \text{branch damping}
\end{equation}
```
from
``` math
\begin{equation}
  \text{survivor-basin capture}.
\end{equation}
```

A measurement record requires:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```
Outcome probabilities require a basin measure:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i^{(\mathsf M)})}
  {\sum_j\mu(B_j^{(\mathsf M)})}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{visibility damping is not the same thing as outcome probability.}
  }
  \label{eq:decoherence-not-outcome-failure}
\end{equation}
```

A proposed measurement account fails if it treats decoherence alone as a complete record selection mechanism.

## Failure mode X: ignoring device dependence

Different measurement devices disturb different branch structures. A detector context includes:
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
\end{equation}
```

Two devices may have different effects:
``` math
\begin{equation}
  E_i^{(\mathsf M_1)}\neq E_i^{(\mathsf M_2)},
\end{equation}
```
different damping matrices:
``` math
\begin{equation}
  D_{ab}^{(\mathsf M_1)}
  \neq
  D_{ab}^{(\mathsf M_2)},
\end{equation}
```
and different survivor basins:
``` math
\begin{equation}
  \mathfrak B_{\mathsf M_1}\neq\mathfrak B_{\mathsf M_2}.
\end{equation}
```

Thus a measurement model fails if it treats “measuring the same observable” as sufficient to determine the same disturbance, visibility loss, or basin structure.

The rule is:
``` math
\begin{equation}
  \boxed{
  \text{the measurement device is part of the Lens context.}
  }
  \label{eq:device-context-failure}
\end{equation}
```

## Failure mode XI: gauge quotient violation

Gauge theory requires quotient compatibility. The gauge-sector operator must have the form
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys},
\end{equation}
```
or an equivalent gauge-covariant construction before quotienting.

A gauge-sector realization fails if:

1.  pure-gauge modes are treated as physical;

2.  $`P_{\rm phys}`$ is not quotient-compatible;

3.  Ward identities are violated;

4.  Slavnov–Taylor identities are violated;

5.  BRST cohomology is not preserved;

6.  current conservation is broken;

7.  anomaly cancellation fails.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge filtering must preserve gauge quotient structure and gauge identities.}
  }
  \label{eq:gauge-failure-box}
\end{equation}
```

A Gaussian factor inserted into a gauge propagator is not automatically gauge-admissible.

## Failure mode XII: gravitational diffeomorphism violation

Gravity requires diffeomorphism compatibility. The gravitational operator must have the form
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
\end{equation}
```

A gravity-sector realization fails if:

1.  metric components are damped as coordinate components;

2.  pure diffeomorphism modes are treated as physical;

3.  the Hamiltonian constraint is violated;

4.  the momentum constraints are violated;

5.  the constraint algebra is broken;

6.  stress-energy conservation fails;

7.  a weak-field projector is used outside its domain;

8.  singularities or horizons are smoothed without an admissible survivor-geometry principle.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravitational filtering must act on geometric content, not coordinate artifacts.}
  }
  \label{eq:gravity-failure-box}
\end{equation}
```

## Failure mode XIII: invalid subsystem factorization

Entanglement claims require a valid subsystem decomposition. In ordinary quantum mechanics, one often writes
``` math
\begin{equation}
  \mathcal H_{AB}
  =
  \mathcal H_A\otimes\mathcal H_B.
\end{equation}
```
But in gauge and gravity sectors this factorization may fail or require boundary/edge data.

A proposed entanglement analysis fails if it assumes
``` math
\begin{equation}
  \mathcal H_{AB}
  =
  \mathcal H_A\otimes\mathcal H_B
\end{equation}
```
without checking constraints, gauge redundancy, diffeomorphism equivalence, or boundary structure.

The rule is:
``` math
\begin{equation}
  \boxed{
  \text{subsystem factorization is a Lens structure and must be justified.}
  }
  \label{eq:factorization-failure-box}
\end{equation}
```

This is especially important in gravitational entanglement.

## Failure mode XIV: no-signaling violation

Entanglement may produce nonclassical correlations, but it must not enable controllable superluminal signaling. Therefore local marginals must be independent of remote settings:
``` math
\begin{equation}
  \sum_b p(a,b|x,y)
  =
  \sum_b p(a,b|x,y')
\end{equation}
```
and
``` math
\begin{equation}
  \sum_a p(a,b|x,y)
  =
  \sum_a p(a,b|x',y).
\end{equation}
```

A proposed MTT entanglement model fails if joint basin measures or detector contexts allow remote settings to change local outcome statistics in a controllable way.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{joint coherent admissibility must satisfy no-signaling at the record-statistics level.}
  }
  \label{eq:no-signaling-failure-box}
\end{equation}
```

## Failure mode XV: overclaiming Standard Model closure

The structural framework does not by itself derive:

1.  the Standard Model gauge group;

2.  chiral matter representations;

3.  three generations;

4.  Yukawa couplings;

5.  mixing matrices;

6.  anomaly cancellation;

7.  symmetry breaking;

8.  observed masses and coupling constants.

A paper or model overclaims if it suggests that the finite admissibility architecture alone has already produced these details.

The correct statement is:
``` math
\begin{equation}
  \boxed{
  \text{Standard Model closure is an execution task.}
  }
  \label{eq:SM-overclaim-failure}
\end{equation}
```

MTT supplies the form of the required data:
``` math
\begin{equation}
  A_{\rm SM},
  \qquad
  P_{\rm SM},
  \qquad
  \chi_{\rm SM},
  \qquad
  \tau_{\rm SM},
\end{equation}
```
but the data must still be derived or specified.

## Failure mode XVI: overclaiming quantum gravity

Similarly, the structural gravity section does not complete quantum gravity. It states that a gravitational MTT sector must supply:
``` math
\begin{equation}
  A_{\rm grav},
  \qquad
  P_{\rm diff},
  \qquad
  \chi_{\rm grav},
  \qquad
  \tau_{\rm grav}.
\end{equation}
```
It must preserve diffeomorphism equivalence, constraints, causal structure, and stress-energy compatibility.

A model overclaims if it treats the schematic operator
``` math
\begin{equation}
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}
\end{equation}
```
as a completed nonperturbative quantum-gravity theory without constructing the physical state space and constraints.

The correct statement is:
``` math
\begin{equation}
  \boxed{
  \text{MTT gives a gravitational projection architecture, not a completed nonperturbative
  quantum-gravity calculation by itself.}
  }
  \label{eq:QG-overclaim-failure}
\end{equation}
```

## Failure mode XVII: arbitrary phenomenological numbers

The relations
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
and
``` math
\begin{equation}
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }
\end{equation}
```
give a geometric scale relation. But precise numerical predictions require:

1.  internal geometry;

2.  spectrum $`\mu_j^2`$;

3.  wavefunction overlaps;

4.  gauge representations;

5.  couplings;

6.  widths;

7.  detector acceptances;

8.  renormalization and matching.

Thus a model fails if it asserts exact collider cross-section suppressions, precision-test deviations, or mass spectra without deriving the effective four-dimensional action.

The safe universal statement is:
``` math
\begin{equation}
  \boxed{
  W_j=\mathrm e^{-\tau\mu_j^2}
  }
\end{equation}
```
is an amplitude-level admissibility weight. Observable cross sections require further calculation.

## Failure mode XVIII: treating benchmarks as universal predictions

The flat Euclidean Gaussian kernel
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right)
\end{equation}
```
is a benchmark theorem. It is not automatically the universal physical kernel in every sector.

Similarly, the finite Coulomb potential
``` math
\begin{equation}
  \Phi_\tau(r)
  =
  \frac{q}{4\pi r}
  \operatorname{erf}
  \left(
    \frac{r}{2\sqrt{\tau}}
  \right)
\end{equation}
```
is a useful benchmark for a finite four-dimensional charge profile. But in the FP/fiber realization, electromagnetic corrections may instead appear through internal-mode exchange:
``` math
\begin{equation}
  \Phi(r)
  =
  \frac{q}{4\pi r}
  \left[
    1+
    \sum_{j\ge1}
    c_j\mathrm e^{-\tau\mu_j^2}\mathrm e^{-\mu_j r}
  \right].
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{benchmark kernels are examples, not universal sectoral predictions.}
  }
  \label{eq:benchmark-failure-box}
\end{equation}
```

## Failure mode XIX: loss of low-energy recovery

A viable MTT sector must recover ordinary low-energy physics. In the FP realization this requires undamped zero modes:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
It also requires:
``` math
\begin{equation}
  \chi(0)=1.
\end{equation}
```

If the zero mode is removed, over-damped, or assigned the wrong representation, the low-energy sector fails.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{zero-mode recovery is a mandatory consistency condition.}
  }
  \label{eq:low-energy-recovery-failure}
\end{equation}
```

## Failure mode XX: unbounded equal-time kernels

Equal-time Cauchy kernels are Lorentzian-admissible only if they are bounded on the relevant energy or Sobolev spaces. A kernel
``` math
\begin{equation}
  (\mathcal K_t f)(x)
  =
  \int_{\Sigma_t}K_t(x,y)f(y)\,\,\mathrm dy
\end{equation}
```
is not automatically safe.

A sufficient boundedness condition is a Schur-type condition:
``` math
\begin{equation}
  \sup_x
  \int_{\Sigma_t}|K_t(x,y)|\,\,\mathrm dy<\infty,
\end{equation}
```
and
``` math
\begin{equation}
  \sup_y
  \int_{\Sigma_t}|K_t(x,y)|\,\,\mathrm dx<\infty.
\end{equation}
```

If the kernel is unbounded or changes the hyperbolic principal symbol, it may spoil well-posedness or causality.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{Cauchy-slice kernels must be bounded lower-order operators.}
  }
  \label{eq:unbounded-kernel-failure}
\end{equation}
```

## Failure mode XXI: changing the hyperbolic principal symbol

A Lorentzian finite kernel may be admissible when it enters as a lower-order bounded term:
``` math
\begin{equation}
  \Box_g\phi+m^2\phi+\mathcal K_t\phi=J.
\end{equation}
```
The principal part remains
``` math
\begin{equation}
  \Box_g.
\end{equation}
```

But if the finite modification changes the highest-derivative hyperbolic structure, the causal cone may change. This can introduce superluminal characteristics or ill-posedness.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{Lorentzian finite kernels must not alter the principal causal structure unless a new
  causal theory is explicitly derived.}
  }
  \label{eq:principal-symbol-failure}
\end{equation}
```

## Failure mode XXII: treating finite overlap as signaling

Finite spatial support or overlap is not the same as signal propagation. A finite detector samples a finite region. A finite source has a finite profile. An internal fiber state may project to a finite effective base profile.

These facts do not by themselves imply superluminal signaling.

A failure occurs if the theory allows controllable influence outside the causal domain of dependence. That is a stronger condition than finite support.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite overlap is admissible; controllable acausal signaling is not.}
  }
  \label{eq:overlap-signaling-failure}
\end{equation}
```

## Failure mode XXIII: ignoring positivity of spectral representation

After dimensional reduction, a schematic propagator may be written
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```
A positive Källén–Lehmann-type interpretation requires
``` math
\begin{equation}
  Z_j\ge0
\end{equation}
```
in the relevant physical sector.

If negative-norm states or ghost residues appear, the sector is not physical unless a consistent constraint or gauge mechanism removes them.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{spectral damping does not repair negative-norm sectors.}
  }
  \label{eq:spectral-positivity-failure}
\end{equation}
```

## Failure mode XXIV: topology or boundary inconsistency

Topological and boundary data can carry physical labels. A finite coherent filter must respect global consistency.

Failure occurs if:

1.  flux quantization is broken;

2.  bundle patching is inconsistent;

3.  boundary charges are not preserved;

4.  horizon or asymptotic boundary conditions are violated;

5.  topological sectors are mixed without an admissible transition rule.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite admissibility must preserve global topological and boundary data unless a
  lawful transition is derived.}
  }
  \label{eq:topology-boundary-failure}
\end{equation}
```

## Failure mode XXV: confusing structural unification with completed prediction

The structural corollary says:
``` math
\begin{equation}
  \text{finite coherent admissibility}
  \longrightarrow
  \text{projection shadows}.
\end{equation}
```
It does not say:
``` math
\begin{equation}
  \text{all predictions are already computed}.
\end{equation}
```

A correct use of MTT must distinguish:

1.  structural architecture;

2.  sectoral operator data;

3.  analytic admissibility;

4.  numerical prediction;

5.  experimental test.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is meaningful when it guides sectoral execution, not when it replaces it.}
  }
  \label{eq:structure-vs-prediction-failure}
\end{equation}
```

## Summary

A finite coherent admissibility operator is physical only when its data are admissible:
``` math
\begin{equation}
  B_{\rm adm}=P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```

The most important failure modes are:

1.  treating $`B_{\rm adm}`$ as a projector;

2.  using a nonpositive $`A`$;

3.  using naive $`\mathrm e^{-\tau\Box}`$ in Lorentzian signature;

4.  interpreting base diffusion as physical without justification;

5.  using the delta limit outside its resolution regime;

6.  choosing arbitrary spectral windows;

7.  assuming diagonal weights when $`[P,A]\neq0`$;

8.  using non-CPTP branch damping;

9.  confusing decoherence with outcome selection;

10. ignoring detector-context dependence;

11. violating gauge quotienting;

12. violating diffeomorphism constraints;

13. assuming invalid subsystem factorization;

14. violating no-signaling;

15. overclaiming Standard Model or quantum-gravity closure;

16. treating benchmark kernels as universal predictions.

The central domain-of-validity statement is:
``` math
\begin{equation}
  \boxed{
  \text{MTT is valid only where finite coherent filtering preserves positivity, quotient
  consistency, Lorentzian causality, sectoral constraints, and empirical low-energy recovery.}
  }
\end{equation}
```

# Conclusion

This paper developed finite coherent admissibility as a structural architecture for Modal Triplet Theory. The central operator is
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
The projector is $`P`$. The full operator $`B_{\rm adm}`$ is not generally a projector; it is a finite coherent admissibility operator, or admissible coherent filter.

The main result is that many familiar physical structures can be read as projection shadows of this finite coherent operator:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility}
  \longrightarrow
  \text{projection shadows}
  \longrightarrow
  \text{effective physics}.
  }
  \label{eq:conclusion-main-map}
\end{equation}
```

The first and most important shadows are the Dirac-delta particle shadow and the spectral wave shadow:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}(x,y)
  \quad
  \begin{cases}
    \text{local reading}
    &\Rightarrow
    \text{Dirac delta / particle shadow},\\
    \text{spectral reading}
    &\Rightarrow
    \text{wave / interference shadow}.
  \end{cases}
  }
  \label{eq:conclusion-delta-wave}
\end{equation}
```

Thus wave–particle duality is not treated as a primitive paradox. It is treated as projection duality: two readings of one finite coherent kernel.

## The geometric backbone

The paper also clarified the geometric realization used as the default physical model. In the fixed-point realization, the total space is
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
or more generally a compact internal fiber geometry over a four-dimensional Lorentzian base.

The base $`Y^4`$ carries the observed Lorentzian dynamics. The internal space $`X^6`$, or the internal bundle fibers, carry positive elliptic operators. The internal admissibility operator is
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```

The coherent projector is
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
with
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
\end{equation}
```

Therefore the fixed-point version of the finite coherent admissibility operator is
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
  }
  \label{eq:conclusion-FP-Badm}
\end{equation}
```

This gives the abstract MTT operator a concrete geometric source. The coherent sector is not a vague retained subspace. It is the joint fiber-harmonic sector.

## The Lorentzian resolution

A central correction made in this paper is the rejection of naive Lorentzian heat flow. MTT does not use
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
as its fundamental physical damping operator.

The Lorentzian d’Alembertian is indefinite. Therefore the expression
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
does not play the same role as Euclidean heat flow generated by a positive operator.

The Lorentzian admissibility principle is:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  \quad
  \text{as a naive fundamental damping operator.}
  }
  \label{eq:conclusion-A-not-box}
\end{equation}
```

Instead, admissible Lorentzian implementations use:

1.  positive internal/fiber operators;

2.  positive spatial Cauchy-slice operators;

3.  Hamiltonian or constraint-compatible operators;

4.  gauge-quotiented physical operators;

5.  diffeomorphism-compatible geometric operators;

6.  bounded equal-time kernels that preserve the hyperbolic principal symbol.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT finite kernels are not arbitrary Lorentzian nonlocality.}
  }
\end{equation}
```

They are admissible only when positivity, constraints, quotient structure, and causal propagation are preserved.

## Locality and projection

The finite-kernel structure does not imply uncontrolled action at a distance. In the fixed-point realization, finite coherent width is tied to internal geometry:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
and, for internal radius $`R`$,
``` math
\begin{equation}
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
\end{equation}
```

Thus four-dimensional nonlocal-looking behavior may be a projection shadow of controlled finite support in the total/fibered structure:
``` math
\begin{equation}
  \boxed{
  \text{locality in total/fibered space}
  \longrightarrow
  \text{finite non-pointlike shadows in four dimensions}.
  }
  \label{eq:conclusion-locality-shadow}
\end{equation}
```

Point particles are recovered when the finite coherent width is below resolution:
``` math
\begin{equation}
  \ell_{\rm coh}\ll\ell_{\rm res}.
\end{equation}
```

Equivalently:
``` math
\begin{equation}
  E_{\rm probe}\ll\Lambda_{\rm eff},
  \qquad
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{pointlike behavior is a low-resolution shadow of finite coherent support.}
  }
\end{equation}
```

## Scattering and internal-mode damping

In the Euclidean scalar benchmark, the finite kernel is
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right),
\end{equation}
```
with Fourier transform
``` math
\begin{equation}
  \widehat K_\tau^{(d)}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```
This gives the benchmark finite propagator
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
\end{equation}
```

But in the physical fixed-point realization, the default damping is internal:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
so
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
\end{equation}
```

After dimensional reduction, a typical four-dimensional effective propagator has the schematic form
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j\mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```

The zero mode is undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

Nonzero internal modes are suppressed:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{ordinary low-energy four-dimensional physics is recovered by undamped zero modes.}
  }
\end{equation}
```

Finite coherent corrections enter through suppressed internal excitations, finite overlaps, threshold effects, detector profiles, and sector-specific form factors.

## Gauge and electromagnetism

Gauge theory was identified as the paradigmatic Lens sector. Gauge potentials are local representatives:
``` math
\begin{equation}
  A_\mu\sim A_\mu+\partial_\mu\alpha.
\end{equation}
```

Therefore a finite coherent filter is admissible in a gauge theory only if it respects the gauge quotient:
``` math
\begin{equation}
  \boxed{
  \text{filter after quotienting, or filter covariantly before quotienting}.
  }
\end{equation}
```

The gauge-sector operator must have the schematic form
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
  }
\end{equation}
```

Electromagnetism then has a natural Circle–Lens–Nil reading:
``` math
\begin{align}
  \mathsf L_{\rm EM}
  &: \text{gauge representatives and quotienting},\\
  \mathsf C_{\rm EM}
  &: \text{phase, flux, and holonomy},\\
  \mathsf N_{\rm EM}
  &: \text{charge sectors, photon records, and detector outcomes}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{electromagnetism is gauge-compatible finite coherent admissibility read through
  Lens quotienting, Circle phase, and Nil records.}
  }
\end{equation}
```

## Gravity

Gravity is the deepest Lens sector because it acts on the representation of geometry itself:
``` math
\begin{equation}
  g_{\mu\nu}\sim\varphi^\ast g_{\mu\nu}.
\end{equation}
```

Therefore a gravitational finite filter cannot act on arbitrary coordinate components of the metric. It must act on diffeomorphism-compatible geometric content:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
  }
\end{equation}
```

In ADM/Cauchy form, the relevant data are spatial geometry and momentum:
``` math
\begin{equation}
  (h_{ij},\pi^{ij}),
\end{equation}
```
subject to the Hamiltonian and momentum constraints:
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
\end{equation}
```

Thus gravitational MTT filtering must preserve the constraint surface or act on a reduced physical quotient.

The gravitational triplet is:
``` math
\begin{align}
  \mathsf L_{\rm grav}
  &: \text{diffeomorphism quotient and geometric representation},\\
  \mathsf C_{\rm grav}
  &: \text{curvature and frame holonomy},\\
  \mathsf N_{\rm grav}
  &: \text{boundary, horizon, singularity, survivor geometry}.
\end{align}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{gravity is diffeomorphism-compatible finite coherent admissibility read as geometric
  projection.}
  }
\end{equation}
```

## Quantization, superposition, and entanglement

Quantization was interpreted as admissible survivor-label structure:
``` math
\begin{equation}
  \boxed{
  \text{quantization}
  =
  \mathsf C\text{-closure}
  +
  \mathsf L\text{-quotient consistency}
  +
  \mathsf N\text{-survivor selection}.
  }
\end{equation}
```

In spectral sectors:
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n
\end{equation}
```
gives possible labels, and finite admissibility weights them by
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```

In the fixed-point realization:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j
\end{equation}
```
gives compact-fiber labels. Zero modes survive undamped, while nonzero modes are suppressed.

Superposition was interpreted as coherent branch coexistence before Nil selection:
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_a c_a|a\rangle.
\end{equation}
```

Entanglement was interpreted as non-factorizable coherent admissibility in a joint sector:
``` math
\begin{equation}
  P_{AB}\neq P_A\otimes P_B
\end{equation}
```
or
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  \neq
  B_{\rm adm}^{A}\otimes B_{\rm adm}^{B}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{superposition and entanglement are coherent-sector shadows of finite admissibility.}
  }
\end{equation}
```

## Measurement and records

Measurement was described by finite detector effects, branch damping, and survivor-basin capture. A measurement context is
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
\end{equation}
```

Branch damping is represented by a Schur channel:
``` math
\begin{equation}
  \rho\mapsto D\circ\rho.
\end{equation}
```
Physical admissibility requires
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```

A definite measurement record requires survivor-basin stabilization:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{visibility damping}
  \neq
  \text{outcome selection}.
  }
\end{equation}
```

Visibility is controlled by off-diagonal damping:
``` math
\begin{equation}
  \rho_{ab}\mapsto D_{ab}\rho_{ab}.
\end{equation}
```

Outcome frequencies require a basin measure:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{
    \mu(B_i^{(\mathsf M)})
  }{
    \sum_j\mu(B_j^{(\mathsf M)})
  }.
\end{equation}
```

This distinction is essential to the MTT measurement account.

## What has been achieved

The paper achieved the following structural synthesis.

First, it gave a common-source account of wave–particle duality:
``` math
\begin{equation}
  \boxed{
  \text{Dirac delta and wave behavior are two shadows of one finite coherent kernel.}
  }
\end{equation}
```

Second, it grounded the finite kernel in a concrete fixed-point/fiber geometry:
``` math
\begin{equation}
  M_{10}=Y^4\times X^6.
\end{equation}
```

Third, it resolved the Lorentzian ambiguity by rejecting naive
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
as a fundamental damping rule and replacing it with positive fiber, spatial, Hamiltonian, or constraint-compatible admissibility operators.

Fourth, it showed that scattering corrections should be interpreted as finite overlap, Euclidean benchmark damping, or internal-mode suppression, depending on the sector.

Fifth, it showed that gauge theory and gravity require quotient-compatible finite filtering:
``` math
\begin{equation}
  P_{\rm phys}
  \quad
  \text{for gauge sectors},
\end{equation}
```
and
``` math
\begin{equation}
  P_{\rm diff}
  \quad
  \text{for gravitational sectors}.
\end{equation}
```

Sixth, it placed quantization, superposition, and entanglement inside the same finite coherent architecture.

Seventh, it separated rigorous analytic theorems from structural claims and from future phenomenological execution.

The resulting framework is:
``` math
\begin{equation}
  \boxed{
  \text{not a completed calculation of all sectoral physics, but a unified admissibility
  architecture for deriving and testing sectoral physics.}
  }
  \label{eq:conclusion-achievement-box}
\end{equation}
```

## What remains open

Several tasks remain open.

A complete Standard Model execution must derive or specify:
``` math
\begin{equation}
  A_{\rm SM},
  \qquad
  P_{\rm SM},
  \qquad
  \chi_{\rm SM},
  \qquad
  \tau_{\rm SM},
\end{equation}
```
together with the observed gauge group, matter representations, chirality, anomaly cancellation, masses, couplings, and mixing data.

A complete gravitational execution must derive or specify:
``` math
\begin{equation}
  A_{\rm grav},
  \qquad
  P_{\rm diff},
  \qquad
  \chi_{\rm grav},
  \qquad
  \tau_{\rm grav},
\end{equation}
```
on a physical diffeomorphism-compatible state space.

A complete measurement execution must derive detector basin measures:
``` math
\begin{equation}
  \mu(B_i^{(\mathsf M)}),
\end{equation}
```
and show when they reproduce Born weights.

A complete phenomenological execution must compute internal spectra:
``` math
\begin{equation}
  \mu_j^2,
\end{equation}
```
effective couplings:
``` math
\begin{equation}
  Z_j,\quad g_j,
\end{equation}
```
and observable cross sections or precision corrections.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the next stage is sectoral execution.}
  }
  \label{eq:conclusion-next-stage}
\end{equation}
```

## Final statement

The framework developed here can be summarized in one sentence:

``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility is the common source from which particle, wave,
  measurement, gauge, gravity, quantization, and entanglement appear as projection shadows.}
  }
  \label{eq:conclusion-final-statement}
\end{equation}
```

The Dirac delta is not fundamental. It is the sharp local shadow.

The wave is not a rival substance. It is the spectral phase shadow.

The measurement record is not primitive collapse. It is Nil survivor-basin stabilization.

Gauge is not optional redundancy. It is Lens quotient structure.

Electromagnetism is gauge Lens plus Circle holonomy plus Nil records.

Gravity is the Lens structure of geometry itself.

Quantization is admissible survivor-label discreteness.

Entanglement is non-factorizable coherent admissibility.

All of these are organized by:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  }
\end{equation}
```

In the fixed-point realization:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
  }
\end{equation}
```

Thus the paper’s final claim is:
``` math
\begin{equation}
  \boxed{
  \text{effective physics is the shadow structure of finite coherent admissibility.}
  }
\end{equation}
```

# Spectral calculus for finite coherent admissibility

This appendix records the analytic background for the finite coherent admissibility operator used throughout the paper:
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  \label{eq:appA-Badm}
\end{equation}
```
The main purpose is to clarify when the simple modal weight formula is valid and when it is not.

The clean case is the commuting spectral case:
``` math
\begin{equation}
  A\ge0,
  \qquad
  P=P^\ast=P^2,
  \qquad
  [P,A]=0.
\end{equation}
```
In this case, $`B_{\rm adm}`$ is a positive bounded contraction and acts diagonally on common eigenmodes of $`A`$ and $`P`$.

## Nonnegative self-adjoint operators

Let $`\mathcal H`$ be a Hilbert space and let
``` math
\begin{equation}
  A:\mathcal D(A)\subset\mathcal H\to\mathcal H
\end{equation}
```
be a nonnegative self-adjoint operator:
``` math
\begin{equation}
  A=A^\ast,
  \qquad
  A\ge0.
\end{equation}
```
Nonnegativity means
``` math
\begin{equation}
  \langle f,Af\rangle\ge0
\end{equation}
```
for all $`f\in\mathcal D(A)`$.

By the spectral theorem, there is a projection-valued spectral measure $`E_A(\lambda)`$ such that
``` math
\begin{equation}
  A
  =
  \int_0^\infty
  \lambda\,\,\mathrm dE_A(\lambda).
  \label{eq:appA-spectral-resolution}
\end{equation}
```
For every bounded Borel function $`f`$, one defines
``` math
\begin{equation}
  f(A)
  =
  \int_0^\infty
  f(\lambda)\,\,\mathrm dE_A(\lambda).
  \label{eq:appA-functional-calculus}
\end{equation}
```

In particular,
``` math
\begin{equation}
  \chi(A)
  =
  \int_0^\infty
  \chi(\lambda)\,\,\mathrm dE_A(\lambda),
\end{equation}
```
and
``` math
\begin{equation}
  \mathrm e^{-\tau A}
  =
  \int_0^\infty
  \mathrm e^{-\tau\lambda}\,\,\mathrm dE_A(\lambda).
\end{equation}
```

Since
``` math
\begin{equation}
  0\le\mathrm e^{-\tau\lambda}\le1
\end{equation}
```
for $`\lambda\ge0`$, one has
``` math
\begin{equation}
  0\le\mathrm e^{-\tau A}\le I.
\end{equation}
```

If also
``` math
\begin{equation}
  0\le\chi(\lambda)\le1,
\end{equation}
```
then
``` math
\begin{equation}
  0\le\chi(A)\le I.
\end{equation}
```

## The finite coherent admissibility operator

Let
``` math
\begin{equation}
  P=P^\ast=P^2
\end{equation}
```
be an orthogonal projector. Define
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
The operator $`P`$ is idempotent. The full operator $`B_{\rm adm}`$ is generally not idempotent:
``` math
\begin{equation}
  B_{\rm adm}^2\neq B_{\rm adm}.
\end{equation}
```
Therefore $`B_{\rm adm}`$ is called a finite coherent admissibility operator, not a projector.

If
``` math
\begin{equation}
  [P,A]=0,
\end{equation}
```
then $`P`$ also commutes with $`\chi(A)`$ and $`\mathrm e^{-\tau A}`$. In that case,
``` math
\begin{align}
  \langle f,B_{\rm adm}f\rangle
  &=
  \langle f,P\chi(A)\mathrm e^{-\tau A}\chi(A)P f\rangle\\
  &=
  \left\|
    \mathrm e^{-\tau A/2}\chi(A)Pf
  \right\|^2\\
  &\ge0.
\end{align}
```
Thus
``` math
\begin{equation}
  B_{\rm adm}\ge0.
\end{equation}
```
Moreover,
``` math
\begin{equation}
  \|B_{\rm adm}\|\le1.
\end{equation}
```
Hence
``` math
\begin{equation}
  \boxed{
  0\le B_{\rm adm}\le I.
  }
  \label{eq:appA-positive-contraction}
\end{equation}
```

## Discrete spectral case

Suppose $`A`$ has a discrete orthonormal eigenbasis
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
  \qquad
  \lambda_n\ge0.
\end{equation}
```
Assume also that $`P`$ commutes with $`A`$, so that the eigenbasis can be chosen to diagonalize $`P`$:
``` math
\begin{equation}
  P\phi_n=p_n\phi_n,
  \qquad
  p_n\in\{0,1\}.
\end{equation}
```

Then
``` math
\begin{equation}
  \chi(A)\phi_n=\chi(\lambda_n)\phi_n,
\end{equation}
```
and
``` math
\begin{equation}
  \mathrm e^{-\tau A}\phi_n
  =
  \mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```
Therefore
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
  \label{eq:appA-modal-action}
\end{equation}
```

Define
``` math
\begin{equation}
  w_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
  \label{eq:appA-modal-weight}
\end{equation}
```
Then
``` math
\begin{equation}
  B_{\rm adm}
  =
  \sum_n
  w_n|\phi_n\rangle\langle\phi_n|.
  \label{eq:appA-spectral-Badm}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the commuting spectral case gives explicit admissibility weights }w_n.
  }
\end{equation}
```

## Why $`B_{\rm adm}`$ is usually not idempotent

Using the spectral expression,
``` math
\begin{equation}
  B_{\rm adm}^2\phi_n=w_n^2\phi_n.
\end{equation}
```
Meanwhile,
``` math
\begin{equation}
  B_{\rm adm}\phi_n=w_n\phi_n.
\end{equation}
```
Therefore
``` math
\begin{equation}
  B_{\rm adm}^2=B_{\rm adm}
\end{equation}
```
only if
``` math
\begin{equation}
  w_n^2=w_n
\end{equation}
```
for every $`n`$, i.e.
``` math
\begin{equation}
  w_n\in\{0,1\}.
\end{equation}
```

But generally
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}
\end{equation}
```
takes values strictly between $`0`$ and $`1`$. Hence $`B_{\rm adm}`$ is generally not a projector.

Thus:
``` math
\begin{equation}
  \boxed{
  P\text{ is a projector; }B_{\rm adm}\text{ is a finite filter.}
  }
\end{equation}
```

## Kernel representation

If $`B_{\rm adm}`$ admits an integral kernel, write
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \langle x|B_{\rm adm}|y\rangle.
\end{equation}
```
In the discrete spectral case,
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
  \label{eq:appA-kernel-spectral}
\end{equation}
```

The same kernel has two primary readings:
``` math
\begin{align}
  x\mapsto K_{\rm adm}(x,x_0)
  &: \text{local finite response profile},\\
  \sum_n w_n\phi_n(x)\phi_n^\ast(y)
  &: \text{spectral coherent-mode expansion}.
\end{align}
```

Thus:
``` math
\begin{equation}
  \boxed{
  K_{\rm adm}
  =
  \text{one kernel with local and spectral shadows}.
  }
\end{equation}
```

## Sharp identity limit

Suppose
``` math
\begin{equation}
  P\to I,
  \qquad
  \chi(A)\to I,
  \qquad
  \tau\downarrow0.
\end{equation}
```
Then formally
``` math
\begin{equation}
  B_{\rm adm}\to I.
\end{equation}
```
If the convergence holds strongly on a suitable test-function space, then
``` math
\begin{equation}
  B_{\rm adm}f\to f.
\end{equation}
```
At the kernel level, this means
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y)
\end{equation}
```
distributionally.

Thus:
``` math
\begin{equation}
  \boxed{
  \delta(x-y)
  =
  \text{kernel of the identity reached in the sharp admissibility limit}.
  }
\end{equation}
```

## Noncommuting case

If
``` math
\begin{equation}
  [P,A]\neq0,
\end{equation}
```
then $`P`$, $`\chi(A)`$, and $`\mathrm e^{-\tau A}`$ cannot generally be diagonalized together. The formula
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}
\end{equation}
```
is then not valid.

The operator
``` math
\begin{equation}
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
may still be meaningful. However, its admissibility must be checked by:

1.  boundedness on the intended Hilbert or Sobolev scale;

2.  positivity or complete positivity where relevant;

3.  preservation of constraints;

4.  preservation of gauge or diffeomorphism equivalence;

5.  domain stability;

6.  compatibility with the physical measurement context.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{noncommuting projections require operator estimates, not scalar modal weights.}
  }
\end{equation}
```

## FP commuting case

In the fixed-point realization,
``` math
\begin{equation}
  A=A_{\rm int}
  =
  \sum_{n=1}^3\kappa_n\Delta_{B_n},
\end{equation}
```
and
``` math
\begin{equation}
  P=P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3}.
\end{equation}
```
The coherent projector is built from the fiber-harmonic projectors. In the clean fiber-spectral setting, this gives the commuting relation
``` math
\begin{equation}
  [P_{\rm coh},A_{\rm int}]=0.
\end{equation}
```

Therefore the modal formula applies:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}\phi_j
  =
  p_j\chi(\mu_j^2)^2\mathrm e^{-\tau\mu_j^2}\phi_j,
\end{equation}
```
where
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j.
\end{equation}
```

The zero modes satisfy
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
and are undamped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
The nonzero internal modes satisfy
``` math
\begin{equation}
  \mu_j^2>0,
\end{equation}
```
and are damped:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the FP realization is the clean commuting spectral model of MTT admissibility.}
  }
\end{equation}
```

## Summary

The finite coherent admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
In the clean commuting case,
``` math
\begin{equation}
  A\ge0,
  \qquad
  [P,A]=0,
\end{equation}
```
one has
``` math
\begin{equation}
  0\le B_{\rm adm}\le I.
\end{equation}
```

If
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
  \qquad
  P\phi_n=p_n\phi_n,
\end{equation}
```
then
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```

The modal weight is
``` math
\begin{equation}
  w_n=p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```

The operator $`B_{\rm adm}`$ is generally not idempotent and therefore is not generally a projector.

When a kernel exists,
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
\end{equation}
```
Its sharp identity limit gives the Dirac delta:
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
\end{equation}
```

This is the analytic foundation for the paper’s central claim:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent kernels have both local particle shadows and spectral wave shadows.}
  }
\end{equation}
```

# Dirac delta limits and finite coherent kernels

This appendix records the distributional meaning of the Dirac delta limit used throughout the paper. The central point is that the Dirac delta is not treated as a primitive physical object. It is the sharp local shadow of a family of finite coherent kernels.

The guiding relation is
``` math
\begin{equation}
  K_\tau(x,y)\to\delta(x-y)
  \qquad
  \text{as}
  \qquad
  \tau\downarrow0,
  \label{eq:appB-delta-limit}
\end{equation}
```
where the convergence is distributional or weak, not pointwise.

This appendix makes precise what that means.

## The delta distribution

Let $`M`$ be a smooth manifold with measure $`\,\mathrm d\mu`$. The Dirac delta distribution
``` math
\begin{equation}
  \delta_x(y)
\end{equation}
```
is defined by its action on test functions:
``` math
\begin{equation}
  \int_M \delta_x(y)f(y)\,\,\mathrm d\mu(y)
  =
  f(x).
  \label{eq:appB-delta-def}
\end{equation}
```

Equivalently, the identity operator has kernel
``` math
\begin{equation}
  I(x,y)=\delta(x-y),
\end{equation}
```
because
``` math
\begin{equation}
  (If)(x)
  =
  \int_M \delta(x-y)f(y)\,\,\mathrm d\mu(y)
  =
  f(x).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \delta(x-y)
  =
  \text{kernel of the identity operator}.
  }
  \label{eq:appB-delta-identity}
\end{equation}
```

In MTT, this identity kernel appears only as the sharp limit of finite coherent admissibility.

## Approximate identities

A family of kernels
``` math
\begin{equation}
  K_\tau(x,y),
  \qquad
  \tau>0,
\end{equation}
```
is an approximate identity if
``` math
\begin{equation}
  \lim_{\tau\downarrow0}
  \int_M K_\tau(x,y)f(y)\,\,\mathrm d\mu(y)
  =
  f(x)
  \label{eq:appB-approx-identity}
\end{equation}
```
for all test functions $`f`$ in the relevant class.

This is equivalent to saying
``` math
\begin{equation}
  K_\tau(x,y)\to\delta(x-y)
\end{equation}
```
distributionally.

A typical approximate identity satisfies:

1.  normalization:
    ``` math
    \begin{equation}
        \int_M K_\tau(x,y)\,\,\mathrm d\mu(y)=1;
    \end{equation}
    ```

2.  concentration near $`x=y`$ as $`\tau\downarrow0`$;

3.  decay away from the diagonal;

4.  boundedness or positivity sufficient for convergence on the chosen function space.

The physical meaning is:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent response becomes pointlike only in the sharp limit.}
  }
\end{equation}
```

## Flat Gaussian approximate identity

On $`\mathbb R^d`$, the standard heat kernel is
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
  \label{eq:appB-flat-gaussian}
\end{equation}
```

It is normalized:
``` math
\begin{equation}
  \int_{\mathbb R^d}
  K_\tau^{(d)}(x-y)\,\,\mathrm d^dy
  =
  1.
\end{equation}
```

For every test function $`f\in C_c^\infty(\mathbb R^d)`$,
``` math
\begin{equation}
  \lim_{\tau\downarrow0}
  \int_{\mathbb R^d}
  K_\tau^{(d)}(x-y)f(y)\,\,\mathrm d^dy
  =
  f(x).
  \label{eq:appB-gaussian-convergence}
\end{equation}
```

Therefore
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  \to
  \delta^{(d)}(x-y)
\end{equation}
```
distributionally.

This is the simplest mathematical model of the MTT particle shadow:
``` math
\begin{equation}
  \boxed{
  \text{finite Gaussian kernel}
  \longrightarrow
  \text{Dirac delta shadow}.
  }
\end{equation}
```

## Fourier representation

The same kernel has Fourier representation
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  \int_{\mathbb R^d}
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \mathrm e^{-\tau k^2}
  \mathrm e^{\mathrm ik\cdot(x-y)}.
  \label{eq:appB-fourier-gaussian}
\end{equation}
```

As $`\tau\downarrow0`$,
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}\to1.
\end{equation}
```
Formally,
``` math
\begin{equation}
  \lim_{\tau\downarrow0}
  K_\tau^{(d)}(x-y)
  =
  \int_{\mathbb R^d}
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \mathrm e^{\mathrm ik\cdot(x-y)}
  =
  \delta^{(d)}(x-y).
\end{equation}
```

Thus the same object has two readings:
``` math
\begin{equation}
  \boxed{
  K_\tau^{(d)}(x-y)
  =
  \text{finite local kernel},
  }
\end{equation}
```
and
``` math
\begin{equation}
  \boxed{
  \widehat K_\tau^{(d)}(k)
  =
  \mathrm e^{-\tau k^2}
  =
  \text{spectral damping factor}.
  }
\end{equation}
```

This is the mathematical prototype of wave–particle projection duality.

## Finite width

The Gaussian kernel
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
\end{equation}
```
has characteristic width
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau}.
\end{equation}
```
The corresponding effective energy scale is
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
\end{equation}
```

The delta approximation is valid only when the finite width is below experimental resolution:
``` math
\begin{equation}
  \ell_{\rm coh}\ll\ell_{\rm res}.
\end{equation}
```
Equivalently,
``` math
\begin{equation}
  E_{\rm probe}\ll\Lambda_{\rm eff}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \delta\text{-locality is a resolution-dependent approximation.}
  }
  \label{eq:appB-resolution-delta}
\end{equation}
```

## Sharp limit of $`B_{\rm adm}`$

The finite coherent admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
A sharp identity limit is obtained when
``` math
\begin{equation}
  P\to I,
  \qquad
  \chi(A)\to I,
  \qquad
  \tau\downarrow0.
\end{equation}
```

Under suitable convergence assumptions,
``` math
\begin{equation}
  B_{\rm adm}f\to f.
\end{equation}
```
If $`B_{\rm adm}`$ has a kernel $`K_{\rm adm}(x,y)`$, this implies
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y)
\end{equation}
```
distributionally.

Thus the Dirac delta is the kernel of the limiting identity:
``` math
\begin{equation}
  \boxed{
  \delta(x-y)
  =
  \lim_{\rm sharp}
  \langle x|B_{\rm adm}|y\rangle.
  }
  \label{eq:appB-delta-Badm-limit}
\end{equation}
```

## Spectral sharp limit

In the commuting discrete spectral case,
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y),
\end{equation}
```
where
``` math
\begin{equation}
  w_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
\end{equation}
```

The sharp identity limit corresponds to
``` math
\begin{equation}
  w_n\to1
\end{equation}
```
for all modes in the test-function domain. Then
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  \to
  \sum_n
  \phi_n(x)\phi_n^\ast(y).
\end{equation}
```
By completeness,
``` math
\begin{equation}
  \sum_n
  \phi_n(x)\phi_n^\ast(y)
  =
  \delta(x-y).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \delta(x-y)
  =
  \text{complete spectral reconstruction in the sharp admissibility limit}.
  }
  \label{eq:appB-spectral-delta}
\end{equation}
```

## Finite kernels on manifolds

On a Riemannian manifold $`(M,g)`$, a positive elliptic operator $`A_g`$ defines a heat kernel
``` math
\begin{equation}
  K_g(x,y;\tau)
  =
  \langle x|\mathrm e^{-\tau A_g}|y\rangle.
\end{equation}
```
For small $`\tau`$, the heat kernel has an asymptotic expansion of the schematic form
``` math
\begin{equation}
  K_g(x,y;\tau)
  \sim
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{\sigma_g(x,y)}{2\tau}
  \right)
  \Delta_g^{1/2}(x,y)
  \left[
    1+\tau a_1(x,y)+\tau^2a_2(x,y)+\cdots
  \right],
  \label{eq:appB-manifold-heat}
\end{equation}
```
where $`\sigma_g(x,y)`$ is Synge’s world function and $`\Delta_g(x,y)`$ is the Van Vleck determinant.

As $`\tau\downarrow0`$,
``` math
\begin{equation}
  K_g(x,y;\tau)\to\delta_g(x,y),
\end{equation}
```
where $`\delta_g`$ is the delta distribution with respect to the Riemannian volume measure.

Thus the delta limit persists on curved spaces, but the finite kernel is shaped by:

1.  geodesic distance;

2.  curvature;

3.  measure;

4.  topology;

5.  boundary conditions;

6.  bundle structure.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent kernels are geometry-dependent before they become delta shadows.}
  }
\end{equation}
```

## Internal/fiber delta shadows

In the fixed-point realization, the natural finite kernel lives on compact internal/fiber geometry. The positive internal operator is
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n}.
\end{equation}
```
A corresponding internal heat kernel has spectral form
``` math
\begin{equation}
  K_{\rm int}(z,z';\tau)
  =
  \sum_j
  \mathrm e^{-\tau\mu_j^2}
  \phi_j(z)\phi_j^\ast(z'),
  \label{eq:appB-internal-kernel}
\end{equation}
```
where
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j.
\end{equation}
```

The internal sharp limit is
``` math
\begin{equation}
  K_{\rm int}(z,z';\tau)\to\delta_{X^6}(z,z')
\end{equation}
```
as $`\tau\downarrow0`$, subject to the relevant projector and window limits.

After dimensional reduction, this finite internal structure appears as four-dimensional effective data:

1.  zero-mode fields;

2.  damped internal excitations;

3.  finite overlap coefficients;

4.  form factors;

5.  detector or source profiles;

6.  non-pointlike projection shadows.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional delta behavior may be a low-resolution shadow of finite internal
  coherent structure.}
  }
  \label{eq:appB-fiber-delta-shadow}
\end{equation}
```

## Delta sources and finite sources

A point source is often written as
``` math
\begin{equation}
  J(x)=q\delta(x-x_0).
\end{equation}
```
MTT replaces this, when finite structure is relevant, by
``` math
\begin{equation}
  J_\tau(x)=qK_\tau(x,x_0).
\end{equation}
```
The total charge or weight is preserved if
``` math
\begin{equation}
  \int_M K_\tau(x,x_0)\,\,\mathrm d\mu(x)=1.
\end{equation}
```

In the sharp limit,
``` math
\begin{equation}
  J_\tau(x)\to q\delta(x-x_0).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{point source}
  =
  \text{sharp limit of finite coherent source}.
  }
\end{equation}
```

This is the source-side version of the particle shadow.

## Delta detectors and finite effects

Similarly, an idealized position measurement may be represented by a sharp projector:
``` math
\begin{equation}
  |x\rangle\langle x|.
\end{equation}
```
A finite detector instead uses a positive effect
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
\end{equation}
```
where
``` math
\begin{equation}
  k_x(y)=K_{\rm det}(y,x).
\end{equation}
```

The probability density is
``` math
\begin{equation}
  p(x)=\operatorname{tr}(\rho E_x).
\end{equation}
```

The sharp position measurement is recovered only when the detector profile becomes delta-like:
``` math
\begin{equation}
  K_{\rm det}(y,x)\to\delta(y-x).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{localized detector clicks are finite-effect records, not primitive delta events.}
  }
\end{equation}
```

## Distributional convergence versus pointwise convergence

It is important that
``` math
\begin{equation}
  K_\tau(x,y)\to\delta(x-y)
\end{equation}
```
does not mean ordinary pointwise convergence. The delta distribution is not a function.

For fixed $`x\neq y`$, the Gaussian kernel satisfies
``` math
\begin{equation}
  K_\tau(x-y)\to0
\end{equation}
```
as $`\tau\downarrow0`$. At $`x=y`$, it diverges:
``` math
\begin{equation}
  K_\tau(0)\to\infty.
\end{equation}
```
The meaningful statement is the integrated one:
``` math
\begin{equation}
  \int K_\tau(x-y)f(y)\,\,\mathrm dy\to f(x).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the delta limit is a distributional limit, not a pointwise physical profile.}
  }
\end{equation}
```

## Resolution and operational indistinguishability

A finite kernel and a delta source are operationally indistinguishable to a probe if the probe cannot resolve the finite width. Let the probe resolution be
``` math
\begin{equation}
  \ell_{\rm res}.
\end{equation}
```
If
``` math
\begin{equation}
  \sqrt{\tau}\ll\ell_{\rm res},
\end{equation}
```
then
``` math
\begin{equation}
  K_\tau(x,y)
\end{equation}
```
is effectively indistinguishable from
``` math
\begin{equation}
  \delta(x-y)
\end{equation}
```
for that probe.

The first finite-width correction in a derivative expansion is often controlled by
``` math
\begin{equation}
  \tau\partial^2
\end{equation}
```
or, in momentum space,
``` math
\begin{equation}
  \tau k^2.
\end{equation}
```

Thus the expansion parameter is
``` math
\begin{equation}
  \tau E_{\rm probe}^2.
\end{equation}
```

If
``` math
\begin{equation}
  \tau E_{\rm probe}^2\ll1,
\end{equation}
```
the delta approximation is reliable. If
``` math
\begin{equation}
  \tau E_{\rm probe}^2\sim1,
\end{equation}
```
finite coherent structure may become observable.

## Summary

The Dirac delta is defined by
``` math
\begin{equation}
  \int\delta(x-y)f(y)\,\,\mathrm d\mu(y)=f(x).
\end{equation}
```
It is the kernel of the identity operator:
``` math
\begin{equation}
  I(x,y)=\delta(x-y).
\end{equation}
```

A family of finite kernels $`K_\tau(x,y)`$ converges to the delta distribution when
``` math
\begin{equation}
  \int K_\tau(x,y)f(y)\,\,\mathrm d\mu(y)\to f(x)
\end{equation}
```
for suitable test functions.

The Gaussian heat kernel provides the benchmark:
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right),
\end{equation}
```
with
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)\to\delta^{(d)}(x-y).
\end{equation}
```

In MTT,
``` math
\begin{equation}
  \delta(x-y)
  =
  \lim_{\rm sharp}
  \langle x|B_{\rm adm}|y\rangle.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{the Dirac delta is the sharp local shadow of finite coherent admissibility.}
  }
\end{equation}
```

# Schur damping, branch channels, and visibility

This appendix records the channel-theoretic details behind the MTT branch-damping layer. The central object is a Schur product map
``` math
\begin{equation}
  \Phi_D(\rho)
  =
  D\circ\rho,
  \label{eq:appC-Schur-map}
\end{equation}
```
where
``` math
\begin{equation}
  (D\circ\rho)_{ab}
  =
  D_{ab}\rho_{ab}.
\end{equation}
```

This map describes loss of branch coherence in a chosen Lens context. It is used for decoherence, visibility loss, partial which-way marking, weak measurement, and measurement disturbance.

The key admissibility condition is:
``` math
\begin{equation}
  \boxed{
  D\succeq0,
  \qquad
  D_{aa}=1.
  }
  \label{eq:appC-D-condition}
\end{equation}
```
Under this condition, the Schur map is completely positive and trace preserving.

## Branch basis and density matrices

Let
``` math
\begin{equation}
  \{|a\rangle\}_{a=1}^N
\end{equation}
```
be a finite branch basis selected by a measurement or representation context. A density matrix has entries
``` math
\begin{equation}
  \rho_{ab}
  =
  \langle a|\rho|b\rangle.
\end{equation}
```

The diagonal entries
``` math
\begin{equation}
  \rho_{aa}
\end{equation}
```
are branch weights. The off-diagonal entries
``` math
\begin{equation}
  \rho_{ab},
  \qquad
  a\neq b,
\end{equation}
```
carry branch coherence.

A branch-damping map acts as
``` math
\begin{equation}
  \rho_{ab}
  \mapsto
  D_{ab}\rho_{ab}.
  \label{eq:appC-branch-damping}
\end{equation}
```

If
``` math
\begin{equation}
  D_{aa}=1,
\end{equation}
```
the diagonal branch weights are unchanged. If
``` math
\begin{equation}
  |D_{ab}|<1,
  \qquad
  a\neq b,
\end{equation}
```
the corresponding branch coherence is reduced.

Thus:
``` math
\begin{equation}
  \boxed{
  D_{ab}
  =
  \text{surviving coherence between branches }a\text{ and }b.
  }
  \label{eq:appC-D-meaning}
\end{equation}
```

## The Schur product theorem

The Schur product theorem states that if
``` math
\begin{equation}
  D\succeq0
\end{equation}
```
and
``` math
\begin{equation}
  \rho\succeq0,
\end{equation}
```
then
``` math
\begin{equation}
  D\circ\rho\succeq0.
\end{equation}
```

This ensures positivity of the output state. However, quantum channels require complete positivity, not only positivity. For Schur maps, positive semidefiniteness of $`D`$ is also sufficient for complete positivity.

<div id="thm:appC-Schur-channel" class="theorem">

**Theorem 9** (Schur damping channel). *Let $`D\in M_N(\mathbb C)`$. The map
``` math
\begin{equation}
  \Phi_D(\rho)=D\circ\rho
\end{equation}
```
is completely positive if and only if
``` math
\begin{equation}
  D\succeq0.
\end{equation}
```
It is trace preserving if and only if
``` math
\begin{equation}
  D_{aa}=1
\end{equation}
```
for all $`a`$. Therefore, if
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1,
\end{equation}
```
then $`\Phi_D`$ is CPTP.*

</div>

<div class="proof">

*Proof.* If $`D\succeq0`$, then there exist vectors $`v_a`$ in an auxiliary Hilbert space $`\mathcal K`$ such that
``` math
\begin{equation}
  D_{ab}
  =
  \langle v_b,v_a\rangle.
\end{equation}
```
Define
``` math
\begin{equation}
  V:\mathbb C^N\to\mathbb C^N\otimes\mathcal K
\end{equation}
```
by
``` math
\begin{equation}
  V|a\rangle
  =
  |a\rangle\otimes v_a.
\end{equation}
```
If
``` math
\begin{equation}
  D_{aa}=1,
\end{equation}
```
then
``` math
\begin{equation}
  \|v_a\|^2=D_{aa}=1,
\end{equation}
```
and hence
``` math
\begin{equation}
  V^\ast V=I.
\end{equation}
```

Now define
``` math
\begin{equation}
  \Phi_D(\rho)
  =
  \operatorname{tr}_{\mathcal K}(V\rho V^\ast).
\end{equation}
```
Then
``` math
\begin{align}
  \langle a|\Phi_D(\rho)|b\rangle
  &=
  \rho_{ab}\langle v_b,v_a\rangle\\
  &=
  D_{ab}\rho_{ab}.
\end{align}
```
Thus
``` math
\begin{equation}
  \Phi_D(\rho)=D\circ\rho.
\end{equation}
```
Because $`\Phi_D`$ has a Stinespring representation, it is completely positive. Because $`V^\ast V=I`$, it is trace preserving.

Conversely, if $`\Phi_D`$ is completely positive, applying it to the maximally entangled Choi state shows that its Choi matrix is positive. The Choi matrix of $`\Phi_D`$ is supported on the span of $`|aa\rangle`$ and has entries $`D_{ab}`$, so $`D\succeq0`$. Trace preservation requires
``` math
\begin{equation}
  \operatorname{tr}(D\circ\rho)=\operatorname{tr}\rho
\end{equation}
```
for all $`\rho`$, which is equivalent to $`D_{aa}=1`$ for every $`a`$. ◻

</div>

Thus arbitrary branch damping is not allowed. The damping matrix must define a valid quantum channel.

## Two-branch damping

For two branches,
``` math
\begin{equation}
  D
  =
  \begin{pmatrix}
    1 & d\\
    d^\ast & 1
  \end{pmatrix}.
  \label{eq:appC-two-branch-D}
\end{equation}
```
The condition
``` math
\begin{equation}
  D\succeq0
\end{equation}
```
is equivalent to
``` math
\begin{equation}
  |d|\le1.
\end{equation}
```

The Schur map acts as
``` math
\begin{equation}
  \begin{pmatrix}
    \rho_{11} & \rho_{12}\\
    \rho_{21} & \rho_{22}
  \end{pmatrix}
  \mapsto
  \begin{pmatrix}
    \rho_{11} & d\rho_{12}\\
    d^\ast\rho_{21} & \rho_{22}
  \end{pmatrix}.
  \label{eq:appC-two-branch-map}
\end{equation}
```

If
``` math
\begin{equation}
  d=1,
\end{equation}
```
coherence is preserved. If
``` math
\begin{equation}
  d=0,
\end{equation}
```
the off-diagonal terms vanish in the branch basis. If
``` math
\begin{equation}
  0<|d|<1,
\end{equation}
```
coherence is partially preserved.

Thus:
``` math
\begin{equation}
  \boxed{
  |d|
  =
  \text{two-branch coherence survival factor}.
  }
\end{equation}
```

## Visibility law

Consider a two-branch interferometer with state
``` math
\begin{equation}
  |\psi\rangle
  =
  \alpha|\psi_1\rangle+\beta|\psi_2\rangle.
\end{equation}
```
A detector effect $`E_x`$ gives intensity
``` math
\begin{align}
  I(x)
  &=
  |\alpha|^2
  \langle\psi_1|E_x|\psi_1\rangle
  +
  |\beta|^2
  \langle\psi_2|E_x|\psi_2\rangle
  \nonumber\\
  &\quad+
  2\operatorname{Re}
  \left[
    \alpha\beta^\ast
    \langle\psi_2|E_x|\psi_1\rangle
  \right].
  \label{eq:appC-undamped-intensity}
\end{align}
```

After branch damping with two-branch factor $`d`$, the intensity becomes
``` math
\begin{align}
  I_D(x)
  &=
  |\alpha|^2
  \langle\psi_1|E_x|\psi_1\rangle
  +
  |\beta|^2
  \langle\psi_2|E_x|\psi_2\rangle
  \nonumber\\
  &\quad+
  2\operatorname{Re}
  \left[
    d\alpha\beta^\ast
    \langle\psi_2|E_x|\psi_1\rangle
  \right].
  \label{eq:appC-damped-intensity}
\end{align}
```

If $`d`$ is real and nonnegative, the fringe visibility obeys
``` math
\begin{equation}
  V_D=dV_0.
  \label{eq:appC-visibility-law}
\end{equation}
```
If $`d`$ is complex, $`|d|`$ controls the visibility reduction and $`\arg(d)`$ shifts the phase.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{visibility loss}
  =
  \text{off-diagonal branch damping}.
  }
  \label{eq:appC-visibility-box}
\end{equation}
```

## Marker-state model

A physical origin for Schur damping is entanglement with marker states. Suppose
``` math
\begin{equation}
  |\psi\rangle
  =
  \sum_a c_a|a\rangle
\end{equation}
```
becomes
``` math
\begin{equation}
  |\Psi\rangle
  =
  \sum_a c_a|a\rangle|m_a\rangle,
  \label{eq:appC-marker-entangled}
\end{equation}
```
where $`|m_a\rangle`$ are marker or environment states.

Tracing out the marker system gives
``` math
\begin{equation}
  \rho_{ab}
  \mapsto
  \langle m_b|m_a\rangle\rho_{ab}.
\end{equation}
```
Thus
``` math
\begin{equation}
  D_{ab}
  =
  \langle m_b|m_a\rangle.
  \label{eq:appC-marker-D}
\end{equation}
```

Because $`D`$ is a Gram matrix, it is positive semidefinite:
``` math
\begin{equation}
  D\succeq0.
\end{equation}
```
If the marker states are normalized,
``` math
\begin{equation}
  \langle m_a|m_a\rangle=1,
\end{equation}
```
then
``` math
\begin{equation}
  D_{aa}=1.
\end{equation}
```

Thus marker entanglement automatically produces an admissible Schur damping channel.

For two branches:
``` math
\begin{equation}
  d=\langle m_2|m_1\rangle.
\end{equation}
```
If
``` math
\begin{equation}
  \langle m_2|m_1\rangle=1,
\end{equation}
```
no which-way information is stored. If
``` math
\begin{equation}
  \langle m_2|m_1\rangle=0,
\end{equation}
```
the marker states are perfectly distinguishable and branch coherence vanishes in the reduced system.

## Weak marking and partial distinguishability

Weak measurement corresponds to partial branch distinguishability:
``` math
\begin{equation}
  0<|\langle m_b|m_a\rangle|<1.
\end{equation}
```
The coherence is reduced but not eliminated:
``` math
\begin{equation}
  \rho_{ab}\mapsto
  \langle m_b|m_a\rangle\rho_{ab}.
\end{equation}
```

Thus weak measurement naturally gives:
``` math
\begin{equation}
  0<|D_{ab}|<1.
\end{equation}
```

This explains why different devices disturb the same nominal observable differently. They produce different marker states and therefore different damping matrices:
``` math
\begin{equation}
  D_{ab}^{(\mathsf M_1)}
  \neq
  D_{ab}^{(\mathsf M_2)}.
\end{equation}
```

In MTT language:
``` math
\begin{equation}
  \boxed{
  \text{device disturbance is encoded in the measurement-context damping matrix }D^{(\mathsf M)}.
  }
\end{equation}
```

## Quantum eraser

If marker information is stored reversibly, later measurement of the marker in a different basis may conditionally restore interference.

For two branches,
``` math
\begin{equation}
  |\Psi\rangle
  =
  \alpha|\psi_1\rangle|m_1\rangle
  +
  \beta|\psi_2\rangle|m_2\rangle.
\end{equation}
```
If $`|m_1\rangle`$ and $`|m_2\rangle`$ are orthogonal, the system alone has no interference in the branch basis. But define marker superposition states
``` math
\begin{equation}
  |m_\pm\rangle
  =
  \frac{1}{\sqrt2}
  \left(
    |m_1\rangle\pm |m_2\rangle
  \right)
\end{equation}
```
when the marker states are orthonormal. Conditional on detecting $`m_+`$ or $`m_-`$, the system state becomes proportional to
``` math
\begin{equation}
  \alpha|\psi_1\rangle\pm\beta|\psi_2\rangle.
\end{equation}
```
Interference reappears conditionally.

MTT reads this as a change of Lens context before irreversible Nil survivor-basin capture:
``` math
\begin{equation}
  \boxed{
  \text{quantum erasure changes the marker Lens before final record stabilization.}
  }
\end{equation}
```

It does not require retroactive alteration of a past event.

## Exponential branch damping

A useful damping model is
``` math
\begin{equation}
  D_{ab}(\tau)
  =
  \mathrm e^{-\tau\Lambda_{ab}},
  \label{eq:appC-exponential-D}
\end{equation}
```
where
``` math
\begin{equation}
  \Lambda_{aa}=0.
\end{equation}
```
To ensure that $`D(\tau)`$ is positive semidefinite for all $`\tau\ge0`$, $`\Lambda`$ should be conditionally negative definite:
``` math
\begin{equation}
  \sum_{a,b}
  \overline{c_a}c_b\Lambda_{ab}
  \le0
  \qquad
  \text{whenever}
  \qquad
  \sum_a c_a=0.
  \label{eq:appC-CND}
\end{equation}
```

Under this condition, Schoenberg’s theorem implies
``` math
\begin{equation}
  \left(
  \mathrm e^{-\tau\Lambda_{ab}}
  \right)_{ab}
  \succeq0
\end{equation}
```
for all $`\tau\ge0`$.

Thus:
``` math
\begin{equation}
  \boxed{
  \Lambda\text{ conditionally negative definite}
  \quad
  \Rightarrow
  \quad
  D_{ab}=\mathrm e^{-\tau\Lambda_{ab}}
  \text{ is admissible branch damping}.
  }
  \label{eq:appC-Schoenberg-box}
\end{equation}
```

This condition prevents arbitrary phenomenological visibility laws from being inserted without channel consistency.

## Distance-induced damping

A common way to obtain conditionally negative definite $`\Lambda`$ is through squared distances. Suppose each branch $`a`$ is assigned a vector $`r_a`$ in a real Hilbert space. Define
``` math
\begin{equation}
  \Lambda_{ab}
  =
  \|r_a-r_b\|^2.
  \label{eq:appC-squared-distance}
\end{equation}
```
Then $`\Lambda`$ is conditionally negative definite.

Therefore
``` math
\begin{equation}
  D_{ab}
  =
  \exp\left(
    -\tau\|r_a-r_b\|^2
  \right)
\end{equation}
```
is positive semidefinite for all $`\tau\ge0`$.

Physically, $`r_a`$ may represent the detector/environment imprint associated with branch $`a`$. Branches with more separated imprints have smaller coherence:
``` math
\begin{equation}
  \|r_a-r_b\|\text{ large}
  \quad\Rightarrow\quad
  |D_{ab}|\text{ small}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{branch distinguishability can generate admissible exponential coherence damping.}
  }
\end{equation}
```

## Relation to measurement contexts

In MTT, a measurement context is
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
\end{equation}
```
The damping matrix
``` math
\begin{equation}
  D^{(\mathsf M)}
\end{equation}
```
is part of this context. It records how the device/environment suppresses coherence in the chosen branch basis.

Two devices may measure the same nominal branch alternative but have different damping:
``` math
\begin{equation}
  D^{(\mathsf M_1)}
  \neq
  D^{(\mathsf M_2)}.
\end{equation}
```

They may also have different finite effects:
``` math
\begin{equation}
  E_i^{(\mathsf M_1)}
  \neq
  E_i^{(\mathsf M_2)},
\end{equation}
```
and different survivor basins:
``` math
\begin{equation}
  \mathfrak B_{\mathsf M_1}
  \neq
  \mathfrak B_{\mathsf M_2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{measurement disturbance is device-specific finite admissibility data.}
  }
\end{equation}
```

## Visibility versus probability

The damping matrix $`D`$ controls visibility, not final outcome frequency by itself.

Visibility asks:
``` math
\begin{equation}
  \text{How much off-diagonal coherence survives?}
\end{equation}
```
This is determined by
``` math
\begin{equation}
  D_{ab}.
\end{equation}
```

Outcome frequency asks:
``` math
\begin{equation}
  \text{Which record occurs, and how often?}
\end{equation}
```
In MTT, this requires basin measures:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{
    \mu(B_i^{(\mathsf M)})
  }{
    \sum_j\mu(B_j^{(\mathsf M)})
  }.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  D_{ab}
  \text{ controls coherence survival;}
  \qquad
  \mu(B_i)
  \text{ controls outcome frequency.}
  }
  \label{eq:appC-visibility-probability-box}
\end{equation}
```

Confusing these two layers is a failure mode.

## Relation to decoherence

Environmental decoherence is a physical mechanism that often produces Schur damping in an approximately preferred basis. MTT incorporates this mechanism but separates it from final record selection.

The sequence is:
``` math
\begin{equation}
  \rho
  \xrightarrow{\text{branch coupling}}
  \rho'
  \xrightarrow{\text{Schur damping}}
  D\circ\rho'
  \xrightarrow{\text{basin capture}}
  B_i^{(\mathsf M)}.
  \label{eq:appC-measurement-chain}
\end{equation}
```

Decoherence corresponds to the middle step. Measurement record formation requires the final Nil step.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{decoherence is branch damping; measurement record is survivor-basin capture.}
  }
  \label{eq:appC-decoherence-record-box}
\end{equation}
```

## No-signaling compatibility

For entangled systems, local branch damping must not allow controllable superluminal signaling. If the damping is a local CPTP channel on Alice’s subsystem,
``` math
\begin{equation}
  \Phi_A\otimes I_B,
\end{equation}
```
then Bob’s marginal remains unaffected by Alice’s local choice when averaged over Alice’s outcomes:
``` math
\begin{equation}
  \rho_B'
  =
  \operatorname{tr}_A[(\Phi_A\otimes I_B)(\rho_{AB})]
  =
  \operatorname{tr}_A(\rho_{AB})
  =
  \rho_B.
\end{equation}
```

Thus CPTP locality is a sufficient condition for no-signaling at the channel level.

However, full measurement models must also check basin probabilities:
``` math
\begin{equation}
  p(a,b|x,y)
\end{equation}
```
must satisfy
``` math
\begin{equation}
  \sum_b p(a,b|x,y)
  =
  \sum_b p(a,b|x,y')
\end{equation}
```
and similarly for Bob.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{admissible branch damping must be CPTP and compatible with no-signaling record
  statistics.}
  }
\end{equation}
```

## Summary

Branch damping in MTT is represented by the Schur map
``` math
\begin{equation}
  \rho\mapsto D\circ\rho.
\end{equation}
```
It is a valid quantum channel when
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```

For two branches,
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
The visibility law is
``` math
\begin{equation}
  V_D=|d|V_0.
\end{equation}
```

Marker states generate damping by
``` math
\begin{equation}
  D_{ab}=\langle m_b|m_a\rangle.
\end{equation}
```

Exponential damping
``` math
\begin{equation}
  D_{ab}=\mathrm e^{-\tau\Lambda_{ab}}
\end{equation}
```
is admissible for all $`\tau\ge0`$ when $`\Lambda`$ is conditionally negative definite.

The main physical distinction is:
``` math
\begin{equation}
  \boxed{
  \text{Schur damping controls visibility; survivor basins control records.}
  }
\end{equation}
```

# Scalar heat-kernel benchmark

This appendix gives the complete scalar Euclidean benchmark used throughout the paper. It is the simplest fully closed example of finite coherent admissibility.

The benchmark data are:
``` math
\begin{equation}
  A=-\Delta,
  \qquad
  P=I,
  \qquad
  \chi=1,
\end{equation}
```
on $`\mathbb R^d`$, with Euclidean metric.

Then the finite coherent admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}
  =
  \mathrm e^{-\tau A}
  =
  \mathrm e^{\tau\Delta}.
  \label{eq:appD-Badm-scalar}
\end{equation}
```

This appendix proves:

1.  the heat kernel formula;

2.  the Dirac delta limit;

3.  the momentum damping factor;

4.  the finite propagator shadow;

5.  the coherent length scale $`\ell_{\rm coh}\sim\sqrt{\tau}`$;

6.  the effective energy scale $`\Lambda_{\rm eff}\sim\tau^{-1/2}`$.

This example is Euclidean. It is not the fundamental Lorentzian prescription of MTT. Its role is to provide a transparent benchmark in which all formulas can be computed explicitly.

## The Euclidean scalar operator

Let
``` math
\begin{equation}
  A=-\Delta
\end{equation}
```
on $`\mathbb R^d`$, where
``` math
\begin{equation}
  \Delta
  =
  \sum_{j=1}^d
  \frac{\partial^2}{\partial x_j^2}.
\end{equation}
```
The operator $`A=-\Delta`$ is nonnegative:
``` math
\begin{equation}
  \langle f,Af\rangle
  =
  \int_{\mathbb R^d}
  |\nabla f(x)|^2\,\,\mathrm d^dx
  \ge0
\end{equation}
```
for suitable $`f`$.

The plane waves
``` math
\begin{equation}
  \mathrm e^{\mathrm ik\cdot x}
\end{equation}
```
are generalized eigenfunctions:
``` math
\begin{equation}
  -\Delta \mathrm e^{\mathrm ik\cdot x}
  =
  k^2\mathrm e^{\mathrm ik\cdot x},
\end{equation}
```
where
``` math
\begin{equation}
  k^2=|k|^2.
\end{equation}
```

Therefore
``` math
\begin{equation}
  \mathrm e^{-\tau A}\mathrm e^{\mathrm ik\cdot x}
  =
  \mathrm e^{-\tau k^2}\mathrm e^{\mathrm ik\cdot x}.
  \label{eq:appD-plane-wave-damping}
\end{equation}
```

Thus the scalar Euclidean benchmark gives the clean spectral damping factor:
``` math
\begin{equation}
  \boxed{
  \widehat K_\tau(k)=\mathrm e^{-\tau k^2}.
  }
  \label{eq:appD-momentum-damping-box}
\end{equation}
```

## Heat kernel from Fourier transform

The heat kernel is defined by
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  \langle x|\mathrm e^{\tau\Delta}|y\rangle.
\end{equation}
```
Using the Fourier representation, one has
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  \int_{\mathbb R^d}
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \mathrm e^{-\tau k^2}
  \mathrm e^{\mathrm ik\cdot(x-y)}.
  \label{eq:appD-heat-fourier}
\end{equation}
```

The integral factorizes into $`d`$ one-dimensional Gaussian integrals:
``` math
\begin{equation}
  \int_{-\infty}^{\infty}
  \frac{\,\mathrm dk}{2\pi}
  \mathrm e^{-\tau k^2}
  \mathrm e^{\mathrm ik a}
  =
  (4\pi\tau)^{-1/2}
  \exp\left(
    -\frac{a^2}{4\tau}
  \right).
\end{equation}
```

Therefore
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
  \label{eq:appD-heat-kernel}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
  }
  \label{eq:appD-heat-kernel-box}
\end{equation}
```

## Normalization

The kernel is normalized:
``` math
\begin{equation}
  \int_{\mathbb R^d}
  K_\tau^{(d)}(x-y)\,\,\mathrm d^dy
  =
  1.
  \label{eq:appD-normalization}
\end{equation}
```
Indeed,
``` math
\begin{align}
  \int_{\mathbb R^d}
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right)
  \,\mathrm d^dy
  &=
  (4\pi\tau)^{-d/2}
  (4\pi\tau)^{d/2}\\
  &=
  1.
\end{align}
```

Thus $`K_\tau^{(d)}`$ preserves total weight.

This is important for physical interpretation. A finite source profile built from $`K_\tau^{(d)}`$ preserves total charge, mass, or probability weight if normalized in this way.

## Delta limit

Let $`f\in C_c^\infty(\mathbb R^d)`$. Then
``` math
\begin{equation}
  (K_\tau^{(d)}\ast f)(x)
  =
  \int_{\mathbb R^d}
  K_\tau^{(d)}(x-y)f(y)\,\,\mathrm d^dy.
\end{equation}
```
As $`\tau\downarrow0`$,
``` math
\begin{equation}
  K_\tau^{(d)}\ast f
  \to
  f
\end{equation}
```
smoothly on compact sets.

Equivalently,
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  \to
  \delta^{(d)}(x-y)
\end{equation}
```
distributionally.

Thus:
``` math
\begin{equation}
  \boxed{
  \lim_{\tau\downarrow0}
  K_\tau^{(d)}(x-y)
  =
  \delta^{(d)}(x-y)
  }
  \label{eq:appD-delta-limit-box}
\end{equation}
```
in the sense of distributions.

This proves the particle-shadow limit in the scalar benchmark.

## The finite kernel as delta replacement

The benchmark replacement is:
``` math
\begin{equation}
  \delta^{(d)}(x-y)
  \quad
  \rightsquigarrow
  \quad
  K_\tau^{(d)}(x-y).
  \label{eq:appD-delta-replacement}
\end{equation}
```

Explicitly:
``` math
\begin{equation}
  \delta^{(d)}(x-y)
  \quad
  \rightsquigarrow
  \quad
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
\end{equation}
```

The right-hand side is finite for every $`\tau>0`$, normalized, and concentrated near $`x=y`$ with width $`\sqrt{\tau}`$.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{point support}
  \quad
  \rightsquigarrow
  \quad
  \text{finite coherent support}.
  }
  \label{eq:appD-point-to-finite}
\end{equation}
```

## Momentum damping

Taking the Fourier transform of the heat kernel gives
``` math
\begin{equation}
  \widehat K_\tau^{(d)}(k)
  =
  \mathrm e^{-\tau k^2}.
  \label{eq:appD-fourier-damping}
\end{equation}
```

Thus the same finite kernel that appears as a Gaussian in position space appears as a damping factor in momentum space.

The high-momentum modes are suppressed:
``` math
\begin{equation}
  k^2\gg\tau^{-1}
  \quad
  \Rightarrow
  \quad
  \mathrm e^{-\tau k^2}\ll1.
\end{equation}
```

The low-momentum modes are retained:
``` math
\begin{equation}
  k^2\ll\tau^{-1}
  \quad
  \Rightarrow
  \quad
  \mathrm e^{-\tau k^2}\approx1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent width in position space}
  =
  \text{high-mode damping in spectral space}.
  }
  \label{eq:appD-position-spectral-duality}
\end{equation}
```

This is the scalar benchmark version of the MTT delta/wave duality.

## Coherence length and effective scale

The Gaussian exponent is
``` math
\begin{equation}
  -\frac{|x-y|^2}{4\tau}.
\end{equation}
```
Therefore the characteristic spatial width is
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau}.
  \label{eq:appD-lcoh}
\end{equation}
```

Since
``` math
\begin{equation}
  [\tau]=L^2=E^{-2},
\end{equation}
```
the corresponding energy scale is
``` math
\begin{equation}
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
  \label{eq:appD-Lambdaeff}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \ell_{\rm coh}\sim\sqrt{\tau},
  \qquad
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
  }
  \label{eq:appD-scales-box}
\end{equation}
```

The finite-kernel correction parameter is
``` math
\begin{equation}
  \tau k^2
  =
  \left(
    \frac{k}{\Lambda_{\rm eff}}
  \right)^2.
\end{equation}
```

At low momentum:
``` math
\begin{equation}
  k\ll\Lambda_{\rm eff},
\end{equation}
```
the pointlike approximation is valid.

At high momentum:
``` math
\begin{equation}
  k\sim\Lambda_{\rm eff},
\end{equation}
```
finite coherent structure becomes resolvable.

## Finite propagator shadow

The ordinary Euclidean scalar propagator is
``` math
\begin{equation}
  \Delta(k)
  =
  \frac{1}{k^2+m^2}.
  \label{eq:appD-ordinary-propagator}
\end{equation}
```

Inserting the finite coherent heat-kernel factor gives
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
  \label{eq:appD-finite-propagator}
\end{equation}
```

In position space:
``` math
\begin{equation}
  \Delta_{\rm adm}(x-y)
  =
  \int_{\mathbb R^d}
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}
  \mathrm e^{\mathrm ik\cdot(x-y)}.
  \label{eq:appD-finite-propagator-position}
\end{equation}
```

Equivalently:
``` math
\begin{equation}
  \Delta_{\rm adm}
  =
  K_\tau^{(d)}\ast\Delta.
  \label{eq:appD-propagator-convolution}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite propagator}
  =
  \text{ordinary propagator convolved with finite coherent kernel}.
  }
  \label{eq:appD-finite-propagator-box}
\end{equation}
```

This is the cleanest scalar model of finite coherent scattering.

## Low-momentum expansion

For
``` math
\begin{equation}
  \tau k^2\ll1,
\end{equation}
```
one has
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
  =
  1-\tau k^2+\frac12\tau^2k^4+O(\tau^3k^6).
  \label{eq:appD-exponential-expansion}
\end{equation}
```

Therefore
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{1}{k^2+m^2}
  -
  \tau
  \frac{k^2}{k^2+m^2}
  +
  \frac12\tau^2
  \frac{k^4}{k^2+m^2}
  +\cdots.
  \label{eq:appD-low-momentum-propagator}
\end{equation}
```

The first correction is controlled by
``` math
\begin{equation}
  \tau k^2.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite-kernel corrections are small when }\tau k^2\ll1.
  }
  \label{eq:appD-low-momentum-box}
\end{equation}
```

## High-momentum behavior

For
``` math
\begin{equation}
  k^2\gg\tau^{-1},
\end{equation}
```
the factor
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
\end{equation}
```
strongly suppresses high-momentum contributions.

In loop-type integrals, a scalar benchmark expression may take the schematic form
``` math
\begin{equation}
  \int
  \frac{\,\mathrm d^dk}{(2\pi)^d}
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
\end{equation}
```
The exponential factor improves ultraviolet convergence in the Euclidean benchmark.

However, this does not by itself prove a complete renormalization theorem for Lorentzian quantum field theory. Gauge identities, unitarity, positivity, and analytic continuation must be checked separately in each sector.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{Euclidean high-mode damping is a benchmark for UV control, not by itself a full
  Lorentzian QFT proof.}
  }
  \label{eq:appD-UV-caution}
\end{equation}
```

## Four-dimensional Euclidean case

For $`d=4`$, the kernel is
``` math
\begin{equation}
  K_\tau^{(4)}(x-y)
  =
  (4\pi\tau)^{-2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
  \label{eq:appD-4D-kernel}
\end{equation}
```

The finite propagator is
``` math
\begin{equation}
  \Delta_{\rm adm}^{(4)}(k)
  =
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
  \label{eq:appD-4D-propagator}
\end{equation}
```

The coherent length and effective scale are:
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau},
  \qquad
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
\end{equation}
```

The low-energy condition is:
``` math
\begin{equation}
  k^2\ll\tau^{-1}.
\end{equation}
```

This is the formula often useful for intuition, but it should not be confused with the physical Lorentzian FP/MTT prescription.

## Why this is not the Lorentzian rule

The Euclidean benchmark uses
``` math
\begin{equation}
  A=-\Delta\ge0.
\end{equation}
```
The operator is positive, so
``` math
\begin{equation}
  \mathrm e^{-\tau A}
\end{equation}
```
is a true damping operator.

In Lorentzian spacetime, the d’Alembertian
``` math
\begin{equation}
  \Box
\end{equation}
```
is indefinite. Therefore the expression
``` math
\begin{equation}
  \mathrm e^{-\tau\Box}
\end{equation}
```
is not the direct analogue of Euclidean heat flow.

MTT therefore imposes:
``` math
\begin{equation}
  \boxed{
  A\neq\Box
  \quad
  \text{as a naive fundamental Lorentzian damping operator}.
  }
  \label{eq:appD-not-box}
\end{equation}
```

The physical Lorentzian choices are instead:

1.  positive internal/fiber operators;

2.  positive spatial Cauchy-slice operators;

3.  Hamiltonian or constraint-compatible positive operators;

4.  gauge-quotiented physical operators;

5.  diffeomorphism-compatible geometric operators.

Thus the scalar benchmark is a mathematical model of finite coherent damping, not the universal physical prescription.

## Relation to FP/fiber damping

In the fixed-point realization, the natural positive operator is
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n}.
\end{equation}
```
If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
then
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
\end{equation}
```

This is the internal/fiber analogue of
``` math
\begin{equation}
  \mathrm e^{-\tau k^2}
\end{equation}
```
in the Euclidean scalar benchmark.

The key difference is:
``` math
\begin{equation}
  k^2
  =
  \text{Euclidean base momentum squared}
\end{equation}
```
in the scalar benchmark, while
``` math
\begin{equation}
  \mu_j^2
  =
  \text{internal fiber eigenvalue}
\end{equation}
```
in the FP realization.

Thus:
``` math
\begin{equation}
  \boxed{
  \mathrm e^{-\tau k^2}
  \text{ is the Euclidean benchmark;}
  \qquad
  \mathrm e^{-\tau\mu_j^2}
  \text{ is the FP/fiber physical analogue.}
  }
  \label{eq:appD-benchmark-vs-FP}
\end{equation}
```

## Finite source benchmark

A point source in $`\mathbb R^d`$ is
``` math
\begin{equation}
  J(x)=q\delta^{(d)}(x-x_0).
\end{equation}
```
The finite scalar benchmark replaces it by
``` math
\begin{equation}
  J_\tau(x)
  =
  qK_\tau^{(d)}(x-x_0).
  \label{eq:appD-finite-source}
\end{equation}
```

This source has total charge or weight:
``` math
\begin{equation}
  \int_{\mathbb R^d}
  J_\tau(x)\,\,\mathrm d^dx
  =
  q.
\end{equation}
```

As $`\tau\downarrow0`$,
``` math
\begin{equation}
  J_\tau(x)
  \to
  q\delta^{(d)}(x-x_0).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{point source}
  =
  \text{sharp limit of finite coherent source}.
  }
  \label{eq:appD-source-box}
\end{equation}
```

## Finite contact benchmark

A local contact interaction has the schematic form
``` math
\begin{equation}
  S_{\rm int}
  =
  \frac{\lambda}{4!}
  \int_{\mathbb R^d}
  \phi(x)^4\,\,\mathrm d^dx.
  \label{eq:appD-local-contact}
\end{equation}
```

A finite coherent benchmark replaces exact coincidence by a finite overlap kernel:
``` math
\begin{equation}
  S_{\rm int}^{\rm adm}
  =
  \frac{\lambda}{4!}
  \int
  \prod_{i=1}^4\,\mathrm d^dx_i\,
  K_\tau(x_1,x_2,x_3,x_4)
  \phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4).
  \label{eq:appD-finite-contact}
\end{equation}
```

In the sharp limit:
``` math
\begin{equation}
  K_\tau(x_1,x_2,x_3,x_4)
  \to
  \delta(x_1-x_2)\delta(x_1-x_3)\delta(x_1-x_4),
\end{equation}
```
and the local contact interaction is recovered.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{local contact}
  =
  \text{sharp shadow of finite coherent overlap}.
  }
\end{equation}
```

## Summary

The scalar heat-kernel benchmark is defined by:
``` math
\begin{equation}
  A=-\Delta,
  \qquad
  P=I,
  \qquad
  \chi=1.
\end{equation}
```

The finite coherent admissibility operator is:
``` math
\begin{equation}
  B_{\rm adm}=\mathrm e^{\tau\Delta}.
\end{equation}
```

Its kernel is:
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right).
\end{equation}
```

Its Fourier transform is:
``` math
\begin{equation}
  \widehat K_\tau^{(d)}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```

Its sharp limit is:
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)\to\delta^{(d)}(x-y).
\end{equation}
```

The coherent length and energy scale are:
``` math
\begin{equation}
  \ell_{\rm coh}\sim\sqrt{\tau},
  \qquad
  \Lambda_{\rm eff}\sim\tau^{-1/2}.
\end{equation}
```

The finite propagator shadow is:
``` math
\begin{equation}
  \Delta_{\rm adm}(k)
  =
  \frac{\mathrm e^{-\tau k^2}}{k^2+m^2}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{the scalar benchmark proves explicitly how finite coherent kernels produce both
  Dirac-delta localization and spectral damping.}
  }
\end{equation}
```

# Lorentzian admissibility, Cauchy-slice kernels, and causality

This appendix records the Lorentzian admissibility logic used in the main text. The purpose is to separate three ideas that are often conflated:

1.  Euclidean heat-kernel damping generated by a positive elliptic operator;

2.  Lorentzian hyperbolic propagation generated by a principal wave operator;

3.  finite Cauchy-slice kernels used as preparation, detector, source, internal projection, or lower-order effective terms.

The central point is that MTT does not define Lorentzian finite coherent admissibility by
``` math
\begin{equation}
  \mathrm e^{-\tau\Box_g}.
\end{equation}
```
Instead, the damping operator must be positive in the relevant physical sector:
``` math
\begin{equation}
  A\ge0,
\end{equation}
```
or positive after projection, quotienting, or constraint reduction.

Thus the Lorentzian admissibility principle is:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent damping must act through positive internal, spatial, Hamiltonian,
  gauge-physical, or diffeomorphism-compatible operators, not through naive }
  \mathrm e^{-\tau\Box_g}.
  }
  \label{eq:appE-lorentzian-principle}
\end{equation}
```

## Euclidean heat flow versus Lorentzian wave flow

In Euclidean signature, a positive elliptic operator such as
``` math
\begin{equation}
  A=-\Delta\ge0
\end{equation}
```
generates a heat semigroup:
``` math
\begin{equation}
  \mathrm e^{-\tau A}=\mathrm e^{\tau\Delta}.
\end{equation}
```
This operator is smoothing and damping.

In Lorentzian signature, the d’Alembertian
``` math
\begin{equation}
  \Box_g
\end{equation}
```
is hyperbolic and indefinite. It is not a positive elliptic operator. Therefore
``` math
\begin{equation}
  \mathrm e^{-\tau\Box_g}
\end{equation}
```
is not a heat kernel in the same sense.

A naive Lorentzian exponential can introduce:

1.  acausal tails;

2.  infinite time-derivative instabilities;

3.  ghost-like poles;

4.  analytic continuation ambiguity;

5.  loss of unitarity;

6.  violation of gauge or gravitational constraints.

Therefore MTT imposes:
``` math
\begin{equation}
  \boxed{
  A\neq\Box_g
  \quad
  \text{as a naive fundamental damping operator.}
  }
  \label{eq:appE-A-not-box}
\end{equation}
```

## Globally hyperbolic setup

Let $`Y^4`$ be globally hyperbolic. Then
``` math
\begin{equation}
  Y^4\cong\mathbb R\times\Sigma,
\end{equation}
```
with Cauchy slices
``` math
\begin{equation}
  \Sigma_t.
\end{equation}
```
A scalar field is specified by Cauchy data
``` math
\begin{equation}
  \left(
  \phi|_{\Sigma_t},
  n^\mu\nabla_\mu\phi|_{\Sigma_t}
  \right),
\end{equation}
```
where $`n^\mu`$ is the future-directed unit normal to $`\Sigma_t`$.

A standard hyperbolic equation has schematic form
``` math
\begin{equation}
  \Box_g\phi+m^2\phi=J.
  \label{eq:appE-standard-hyperbolic}
\end{equation}
```
Its finite propagation speed is determined by the principal symbol of
``` math
\begin{equation}
  \Box_g.
\end{equation}
```

Thus the causal cone is controlled by the highest-derivative hyperbolic part of the equation.

## Positive Cauchy-slice operators

On each spatial slice $`\Sigma_t`$, one may define positive spatial operators. A basic example is
``` math
\begin{equation}
  A_\Sigma=-\Delta_{\Sigma_t}\ge0
\end{equation}
```
on a Riemannian slice, subject to appropriate boundary conditions.

Then one may define a finite Cauchy-slice filter
``` math
\begin{equation}
  B_\Sigma
  =
  P_\Sigma\chi(A_\Sigma)
  \mathrm e^{-\tau A_\Sigma}
  \chi(A_\Sigma)P_\Sigma.
  \label{eq:appE-cauchy-filter}
\end{equation}
```

This filter acts on spatial data, not on Lorentzian spacetime by an indefinite heat flow. It may be used to:

1.  prepare admissible initial data;

2.  define finite detector effects;

3.  define finite source profiles;

4.  project to physical spatial modes;

5.  filter internal/fiber data read on a Cauchy slice.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{spatial filtering of Cauchy data is Lorentzian-admissible when it preserves the
  physical energy and constraint spaces.}
  }
  \label{eq:appE-spatial-filtering-box}
\end{equation}
```

## Equal-time kernels

A finite equal-time kernel acts on spatial data by
``` math
\begin{equation}
  (\mathcal K_t f)(x)
  =
  \int_{\Sigma_t}
  K_t(x,y)f(y)\,\,\mathrm d\mu_{\Sigma_t}(y).
  \label{eq:appE-equal-time-kernel}
\end{equation}
```
A sufficient boundedness condition is a Schur estimate:
``` math
\begin{equation}
  \sup_x
  \int_{\Sigma_t}
  |K_t(x,y)|\,\,\mathrm d\mu_{\Sigma_t}(y)
  <\infty,
  \label{eq:appE-Schur-x}
\end{equation}
```
and
``` math
\begin{equation}
  \sup_y
  \int_{\Sigma_t}
  |K_t(x,y)|\,\,\mathrm d\mu_{\Sigma_t}(x)
  <\infty.
  \label{eq:appE-Schur-y}
\end{equation}
```
Then
``` math
\begin{equation}
  \mathcal K_t:L^2(\Sigma_t)\to L^2(\Sigma_t)
\end{equation}
```
is bounded.

More generally, one may require boundedness on the relevant Sobolev or energy space:
``` math
\begin{equation}
  \mathcal K_t:H^s(\Sigma_t)\to H^s(\Sigma_t).
\end{equation}
```

This is the minimal analytic requirement for using such a kernel as a lower-order finite admissibility term.

## Principal-symbol preservation

Consider a modified hyperbolic equation of the schematic form
``` math
\begin{equation}
  \Box_g\phi+m^2\phi+\mathcal K_t\phi=J.
  \label{eq:appE-kernel-modified-equation}
\end{equation}
```
Assume $`\mathcal K_t`$ is bounded on the relevant energy space and contains no additional time derivatives.

The principal part is still
``` math
\begin{equation}
  \Box_g.
\end{equation}
```
Therefore the principal symbol is unchanged.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{bounded equal-time finite kernels do not change the hyperbolic principal symbol.}
  }
  \label{eq:appE-principal-symbol-box}
\end{equation}
```

This is the precise sense in which such kernels do not alter the local characteristic cone.

## Energy estimate

Let $`E(t)`$ be the standard hyperbolic energy associated with Cauchy data on $`\Sigma_t`$. For the equation
``` math
\begin{equation}
  \Box_g\phi+m^2\phi+\mathcal K_t\phi=J,
\end{equation}
```
a schematic energy estimate has the form
``` math
\begin{equation}
  E(t)
  \le
  C
  \left[
    E(0)
    +
    \int_0^t
    \|J(s)\|^2\,\,\mathrm ds
  \right]
  \exp(C_Kt),
  \label{eq:appE-energy-estimate}
\end{equation}
```
where $`C_K`$ depends on a bound for $`\mathcal K_t`$.

The finite kernel may change the energy growth constant, but it does not change the highest-derivative hyperbolic operator.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{bounded lower-order kernels can preserve hyperbolic well-posedness while modifying
  finite response or mode mixing.}
  }
  \label{eq:appE-energy-box}
\end{equation}
```

## Important distinction: principal cone versus strict support

There is a subtle but important distinction.

Preserving the principal symbol means preserving the local characteristic cone. It does not automatically mean that an arbitrary spatially nonlocal integral kernel preserves strict compact support of solutions.

If $`K_t(x,y)`$ has global spatial support and appears dynamically in the equation
``` math
\begin{equation}
  \Box_g\phi+m^2\phi+\mathcal K_t\phi=J,
\end{equation}
```
then the value of $`\mathcal K_t\phi`$ at $`x`$ may depend on $`\phi(y)`$ at distant points on the same slice. This can spoil strict support-domain statements even though the principal symbol is unchanged.

Therefore MTT distinguishes three cases.

#### Case 1: preparation, source, detector, or readout kernels.

If the finite kernel is used to prepare initial data, define a finite source, describe detector resolution, or read out an internal projection, then it does not alter the Lorentzian evolution law. The subsequent propagation is governed by the underlying hyperbolic system.

#### Case 2: local or support-controlled lower-order kernels.

If the kernel has controlled spatial support compatible with the physical finite resolution, then the effective domain of dependence may be enlarged only by the finite support radius, or may be handled as part of the finite preparation/readout apparatus.

#### Case 3: globally supported dynamical kernels.

If the kernel has unrestricted global spatial support and is inserted dynamically, then strict support-domain preservation is not automatic. One must prove that no controllable acausal signaling or physical domain-of-dependence violation results.

Thus the safe statement is:
``` math
\begin{equation}
  \boxed{
  \text{principal-symbol preservation is automatic for bounded lower-order equal-time kernels;
  strict support-domain preservation requires support control or a preparation/readout
  interpretation.}
  }
  \label{eq:appE-support-caution-box}
\end{equation}
```

This distinction prevents MTT from overclaiming causality.

## Finite overlap versus acausal signaling

Finite spatial overlap is not the same thing as acausal signaling.

A finite detector effect may sample a spatial region:
``` math
\begin{equation}
  E_x=|k_x\rangle\langle k_x|,
  \qquad
  k_x(y)=K_{\rm det}(y,x).
\end{equation}
```
This does not imply superluminal signal propagation. It means the detector has finite spatial resolution.

Similarly, a finite source profile
``` math
\begin{equation}
  J_\tau(x)=qK_\tau(x,x_0)
\end{equation}
```
does not imply that information propagates outside the light cone. It means the source is not a mathematical point.

Acausality would require controllable influence outside the domain allowed by the Lorentzian dynamics.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent support}
  \neq
  \text{controllable acausal signaling}.
  }
  \label{eq:appE-finite-support-not-signaling}
\end{equation}
```

## Internal/fiber damping as the clean Lorentzian route

The fixed-point realization gives the cleanest Lorentzian implementation. The total space is
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
with $`Y^4`$ Lorentzian and $`X^6`$ compact Riemannian.

The finite damping operator is internal:
``` math
\begin{equation}
  A=A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```
If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
then
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
\end{equation}
```

The Lorentzian base dynamics remain hyperbolic. The internal modes appear in four dimensions as zero modes and massive excitations:
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```

The zero mode is undamped:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{fiber damping avoids Lorentzian heat-flow pathology by damping compact internal
  spectra rather than the indefinite spacetime d'Alembertian.}
  }
  \label{eq:appE-fiber-damping-box}
\end{equation}
```

## Base regularization and the $`\varepsilon`$ parameter

Some analytic constructions introduce
``` math
\begin{equation}
  A_\varepsilon
  =
  A_{\rm int}
  +
  \varepsilon A_{\rm base},
  \qquad
  \varepsilon\ge0.
\end{equation}
```
This can be useful as a regulator or approximation. However, it must not be interpreted automatically as physical Lorentzian damping.

The clean FP/MTT physical choice is
``` math
\begin{equation}
  \varepsilon=0,
\end{equation}
```
so that
``` math
\begin{equation}
  A_\varepsilon=A_{\rm int}.
\end{equation}
```

If
``` math
\begin{equation}
  \varepsilon>0,
\end{equation}
```
then $`A_{\rm base}`$ must be justified as one of:

1.  a positive spatial Cauchy-slice operator;

2.  a Euclidean analytic regulator to be removed;

3.  a Hamiltonian or energy operator on physical data;

4.  a detector or source profile;

5.  a constraint-compatible positive operator.

Thus:
``` math
\begin{equation}
  \boxed{
  \varepsilon>0
  \text{ requires separate Lorentzian admissibility justification.}
  }
  \label{eq:appE-epsilon-box}
\end{equation}
```

## Gauge constraints

Gauge fields have constraints on Cauchy data. For electromagnetism, Gauss law is
``` math
\begin{equation}
  \nabla\cdot\mathbf E=\rho.
\end{equation}
```
A finite Cauchy-slice filter must preserve this constraint or act after projection to physical transverse data.

A gauge-admissible filter has schematic form
``` math
\begin{equation}
  B_{\Sigma}^{\rm gauge}
  =
  P_{\rm phys}
  \chi(A_\Sigma^{\rm gauge})
  \mathrm e^{-\tau A_\Sigma^{\rm gauge}}
  \chi(A_\Sigma^{\rm gauge})
  P_{\rm phys}.
  \label{eq:appE-gauge-cauchy}
\end{equation}
```

The requirement is:
``` math
\begin{equation}
  \boxed{
  B_{\Sigma}^{\rm gauge}
  \text{ must preserve gauge constraints and physical gauge equivalence.}
  }
  \label{eq:appE-gauge-constraint-box}
\end{equation}
```

Thus one may filter physical transverse data, BRST cohomology, or gauge-covariant internal data. One may not arbitrarily damp gauge representatives.

## Gravity constraints

In ADM gravity, Cauchy data are
``` math
\begin{equation}
  (h_{ij},\pi^{ij}),
\end{equation}
```
subject to constraints
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
\end{equation}
```

A gravitational finite filter must preserve the constraint surface or act on reduced diffeomorphism-compatible data:
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}
  =
  P_{\rm diff}
  \chi(A_\Sigma^{\rm grav})
  \mathrm e^{-\tau A_\Sigma^{\rm grav}}
  \chi(A_\Sigma^{\rm grav})
  P_{\rm diff}.
  \label{eq:appE-grav-cauchy}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  B_{\Sigma}^{\rm grav}
  \text{ must preserve gravitational constraints and diffeomorphism-compatible geometry.}
  }
  \label{eq:appE-gravity-constraint-box}
\end{equation}
```

A coordinate-component smoothing of the metric is not an admissible gravitational MTT filter.

## Manifest covariance as Lens

A Cauchy-slice construction selects a foliation
``` math
\begin{equation}
  \{\Sigma_t\}.
\end{equation}
```
This may obscure manifest Lorentz covariance. In MTT, this is interpreted as a Lens feature: a representation chosen to define positive admissibility data.

The analogy is gauge fixing. A gauge-fixed description may not display all symmetries manifestly, but it can still describe the correct physical content if gauge-invariant observables and constraints are preserved.

Thus the relevant distinction is:
``` math
\begin{equation}
  \boxed{
  \text{manifest covariance is a property of the representative;}
  }
\end{equation}
```
whereas:
``` math
\begin{equation}
  \boxed{
  \text{physical covariance is a property of observables, constraints, and transformation
  consistency.}
  }
\end{equation}
```

A Cauchy-slice MTT construction is admissible only if observable predictions do not depend on arbitrary foliation choices, or if their foliation dependence is physically specified and constraint-compatible.

## Causality checklist

A Lorentzian finite-kernel construction must pass the following checks:

1.  The damping operator is positive in the relevant physical sector.

2.  The construction does not use naive $`\mathrm e^{-\tau\Box_g}`$ as a fundamental heat flow.

3.  Cauchy-slice kernels are bounded on the intended energy/Sobolev space.

4.  The hyperbolic principal symbol is unchanged, unless a new causal theory is explicitly derived.

5.  Strict support-domain claims are justified by support control, locality, or a preparation/readout interpretation.

6.  Gauge constraints are preserved in gauge sectors.

7.  Diffeomorphism and Hamiltonian constraints are preserved in gravity.

8.  No controllable acausal signaling is introduced.

9.  Observable predictions are independent of unphysical Lens choices or transform consistently under changes of representative.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{Lorentzian admissibility is a positivity, constraint, and causal-consistency condition.}
  }
  \label{eq:appE-causality-checklist-box}
\end{equation}
```

## Summary

The Lorentzian d’Alembertian is not a positive damping operator:
``` math
\begin{equation}
  A\neq\Box_g
\end{equation}
```
as a naive fundamental MTT filter.

The admissible Lorentzian replacements are:
``` math
\begin{equation}
  A_{\rm int}\ge0,
  \qquad
  A_\Sigma\ge0,
  \qquad
  A_{\rm gauge}\ge0
  \text{ on physical gauge data},
  \qquad
  A_{\rm grav}
  \text{ constraint-compatible}.
\end{equation}
```

A bounded equal-time kernel may preserve the hyperbolic principal symbol:
``` math
\begin{equation}
  \Box_g\phi+m^2\phi+\mathcal K_t\phi=J
  \quad
  \Rightarrow
  \quad
  \text{principal part remains }\Box_g.
\end{equation}
```

However, strict support-domain preservation requires additional support or interpretation conditions. Arbitrary globally supported dynamical kernels are not automatically causal.

The safest physical realization is internal/fiber damping:
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}},
\end{equation}
```
with the Lorentzian base remaining hyperbolic.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{MTT finite kernels are Lorentzian-admissible only when positivity, constraints,
  principal causal structure, and no-signaling are preserved.}
  }
\end{equation}
```

# Gauge-compatible finite filters

This appendix records the gauge-sector admissibility conditions used in the main text. The central point is that a finite coherent filter is not gauge-admissible merely because it damps high modes. It must respect gauge redundancy, physical-state projection, current conservation, and the relevant Ward, Slavnov–Taylor, or BRST identities.

The gauge-sector version of the finite coherent admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}
  \chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})
  P_{\rm phys}.
  \label{eq:appF-gauge-Badm}
\end{equation}
```

The safe rule is:
``` math
\begin{equation}
  \boxed{
  \text{filter after quotienting, or filter covariantly before quotienting.}
  }
  \label{eq:appF-safe-rule}
\end{equation}
```

This appendix explains what that means.

## Gauge equivalence

For Abelian gauge theory, the local gauge potential transforms as
``` math
\begin{equation}
  A_\mu
  \mapsto
  A_\mu+\partial_\mu\alpha.
  \label{eq:appF-U1-transform}
\end{equation}
```
The field strength is
``` math
\begin{equation}
  F_{\mu\nu}
  =
  \partial_\mu A_\nu-\partial_\nu A_\mu,
\end{equation}
```
and is invariant under <a href="#eq:appF-U1-transform" data-reference-type="eqref" data-reference="eq:appF-U1-transform">[eq:appF-U1-transform]</a>:
``` math
\begin{equation}
  F_{\mu\nu}\mapsto F_{\mu\nu}.
\end{equation}
```

Thus $`A_\mu`$ is a Lens representative, not a unique physical object. The physical content is represented by gauge-invariant or gauge-covariant data such as:

1.  field strengths;

2.  Wilson loops;

3.  holonomies;

4.  conserved-current amplitudes;

5.  transverse photon modes;

6.  BRST cohomology classes;

7.  gauge-invariant composite observables.

Therefore, a finite coherent filter cannot act on gauge representatives as if every component were physical. Pure-gauge directions must be removed, quotiented, or handled covariantly.

## Physical projection

Let
``` math
\begin{equation}
  P_{\rm phys}
\end{equation}
```
denote the projection to physical gauge-admissible content. The precise form depends on the formalism.

In a simple Abelian transverse-mode setting, one may use a transverse projector:
``` math
\begin{equation}
  P_T^{ij}(k)
  =
  \delta^{ij}
  -
  \frac{k^ik^j}{|\mathbf k|^2},
  \qquad
  \mathbf k\neq0.
  \label{eq:appF-spatial-transverse-projector}
\end{equation}
```
It satisfies
``` math
\begin{equation}
  k_iP_T^{ij}(k)=0
\end{equation}
```
and
``` math
\begin{equation}
  P_T^2=P_T.
\end{equation}
```

A transverse finite filter on a spatial Cauchy slice may then have the form
``` math
\begin{equation}
  B_{\Sigma}^{\rm EM}
  =
  P_T
  \chi(A_T)
  \mathrm e^{-\tau A_T}
  \chi(A_T)
  P_T,
  \label{eq:appF-transverse-filter}
\end{equation}
```
where $`A_T\ge0`$ acts on transverse physical modes.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the finite filter must act on physical transverse data, not on arbitrary gauge
  representatives.}
  }
  \label{eq:appF-transverse-box}
\end{equation}
```

## Conserved-current amplitudes

Physical electromagnetic exchange amplitudes couple to conserved currents:
``` math
\begin{equation}
  \partial_\mu J^\mu=0.
\end{equation}
```
In momentum space,
``` math
\begin{equation}
  k_\mu J^\mu(k)=0.
  \label{eq:appF-current-conservation}
\end{equation}
```

Because of <a href="#eq:appF-current-conservation" data-reference-type="eqref" data-reference="eq:appF-current-conservation">[eq:appF-current-conservation]</a>, longitudinal components of the gauge propagator do not contribute to physical conserved-current amplitudes. A gauge-compatible finite exchange amplitude may be written schematically as
``` math
\begin{equation}
  \mathcal A_{\rm adm}(k)
  =
  e^2
  J_\mu(k)
  \frac{F_{\rm adm}(k)}{k^2+\mathrm i\epsilon}
  P_{\rm phys}^{\mu\nu}(k)
  J'_\nu(-k),
  \label{eq:appF-current-amplitude}
\end{equation}
```
where $`P_{\rm phys}^{\mu\nu}`$ represents the appropriate physical projector and $`F_{\rm adm}`$ is an admissible finite factor.

In a Euclidean benchmark,
``` math
\begin{equation}
  F_{\rm adm}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```
In the FP/fiber realization, the safer physical statement is an internal-mode expansion:
``` math
\begin{equation}
  F_{\rm adm}
  \leadsto
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
for the $`j`$-th internal gauge excitation.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge-compatible finite factors must multiply physical amplitudes, not unphysical
  gauge components.}
  }
\end{equation}
```

## Filter after quotienting

The cleanest gauge procedure is:
``` math
\begin{equation}
  \text{gauge fields}
  \longrightarrow
  \text{physical quotient}
  \longrightarrow
  \text{finite admissibility filter}.
\end{equation}
```

At the Hilbert-space level this means:
``` math
\begin{equation}
  \mathcal H_{\rm gauge}
  \longrightarrow
  \mathcal H_{\rm phys},
\end{equation}
```
then
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}:
  \mathcal H_{\rm phys}\to\mathcal H_{\rm phys}.
\end{equation}
```

The operator has the schematic form:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}
  \chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})
  P_{\rm phys}.
\end{equation}
```

In this case, the role of $`P_{\rm phys}`$ is to ensure that pure-gauge directions are removed before the finite filter is interpreted physically.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{after quotienting, finite damping acts only on physical gauge content.}
  }
  \label{eq:appF-after-quotient-box}
\end{equation}
```

## Filter covariantly before quotienting

Sometimes it is useful to filter before explicitly passing to the physical quotient. In that case, the filter must transform covariantly under gauge transformations.

For a non-Abelian connection
``` math
\begin{equation}
  A_\mu=A_\mu^aT_a,
\end{equation}
```
the covariant derivative is
``` math
\begin{equation}
  D_\mu=\partial_\mu+[A_\mu,\cdot].
\end{equation}
```
A positive spatial covariant operator may be
``` math
\begin{equation}
  A_{\rm cov}
  =
  -D_iD^i
  \label{eq:appF-covariant-spatial-laplacian}
\end{equation}
```
on a Cauchy slice, with appropriate gauge-covariant boundary conditions.

Under a gauge transformation $`g`$, the operator transforms as
``` math
\begin{equation}
  A_{\rm cov}
  \mapsto
  gA_{\rm cov}g^{-1}.
\end{equation}
```
Therefore
``` math
\begin{equation}
  \chi(A_{\rm cov})\mathrm e^{-\tau A_{\rm cov}}\chi(A_{\rm cov})
\end{equation}
```
also transforms covariantly.

This is admissible only if final observables are gauge-invariant or if the result is subsequently projected to the physical quotient.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{before quotienting, the filter must be gauge-covariant and must not create
  gauge-artifact observables.}
  }
  \label{eq:appF-before-quotient-box}
\end{equation}
```

## BRST formulation

In covariant quantization, physical states are often represented by BRST cohomology. Let
``` math
\begin{equation}
  Q_{\rm BRST}^2=0.
\end{equation}
```
The physical state space is
``` math
\begin{equation}
  \mathcal H_{\rm phys}
  =
  \ker Q_{\rm BRST}/\operatorname{im}Q_{\rm BRST}.
  \label{eq:appF-BRST-cohomology}
\end{equation}
```

A finite coherent filter is BRST-compatible if it maps BRST-closed states to BRST-closed states and does not turn BRST-exact redundancy into physical content.

A strong sufficient condition is
``` math
\begin{equation}
  [A_{\rm gauge},Q_{\rm BRST}]=0,
  \label{eq:appF-A-BRST-commute}
\end{equation}
```
and
``` math
\begin{equation}
  [P_{\rm phys},Q_{\rm BRST}]=0,
  \label{eq:appF-P-BRST-commute}
\end{equation}
```
on the relevant domains.

Then
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}
\end{equation}
```
preserves the physical cohomology class.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{BRST-compatible finite filtering preserves physical cohomology.}
  }
  \label{eq:appF-BRST-box}
\end{equation}
```

## Ward identity condition

In Abelian gauge theory, Ward identities encode gauge invariance and current conservation. A finite modification is gauge-admissible only if it preserves these identities.

For a current-exchange amplitude, this means longitudinal components must decouple:
``` math
\begin{equation}
  k_\mu\mathcal A^\mu=0
\end{equation}
```
where appropriate. Equivalently, current conservation
``` math
\begin{equation}
  k_\mu J^\mu=0
\end{equation}
```
must remain valid.

If a finite damping factor modifies transverse and longitudinal sectors differently in a way that makes longitudinal components physical, the construction fails.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{Abelian finite filtering must preserve Ward identities and current conservation.}
  }
  \label{eq:appF-Ward-box}
\end{equation}
```

This is why a Gaussian-looking factor is not enough. It must be inserted in a gauge-safe way.

## Slavnov–Taylor condition

In non-Abelian gauge theory, Slavnov–Taylor identities encode the interacting gauge constraints. A finite filter must preserve these identities or be derived from a gauge-invariant or BRST-invariant regularized action.

A non-Abelian finite filter is inadmissible if it:

1.  breaks BRST symmetry;

2.  changes ghost cancellations inconsistently;

3.  spoils Slavnov–Taylor identities;

4.  violates unitarity of the physical sector;

5.  changes anomaly cancellation;

6.  turns gauge artifacts into physical poles.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{non-Abelian finite filtering must be identity-preserving, not merely high-mode
  damping.}
  }
  \label{eq:appF-ST-box}
\end{equation}
```

## Gauge-sector spectral weights

In a clean physical gauge sector, suppose
``` math
\begin{equation}
  A_{\rm gauge}\psi_j=\lambda_j\psi_j,
\end{equation}
```
and
``` math
\begin{equation}
  P_{\rm phys}\psi_j=p_j\psi_j.
\end{equation}
```
Then, if
``` math
\begin{equation}
  [P_{\rm phys},A_{\rm gauge}]=0,
\end{equation}
```
one has
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}\psi_j
  =
  p_j\chi(\lambda_j)^2\mathrm e^{-\tau\lambda_j}\psi_j.
  \label{eq:appF-gauge-modal-weight}
\end{equation}
```

This formula is valid only in the commuting physical-sector case. If
``` math
\begin{equation}
  [P_{\rm phys},A_{\rm gauge}]\neq0,
\end{equation}
```
the scalar weight formula is not valid without further analysis.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge-sector mode weights require physical projection and commuting spectral data.}
  }
  \label{eq:appF-gauge-weight-box}
\end{equation}
```

## FP/fiber gauge tower

In the fixed-point realization, gauge fields may arise as zero-mode shadows of internal geometric or bundle data. Let
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j.
\end{equation}
```
The internal admissibility weight is
``` math
\begin{equation}
  W_j=\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

A schematic four-dimensional gauge propagator after dimensional reduction may take the form
``` math
\begin{equation}
  D_{\mu\nu}^{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}
  P_{\mu\nu}^{(j)}(p).
  \label{eq:appF-gauge-effective-propagator}
\end{equation}
```
Here $`P_{\mu\nu}^{(j)}`$ is the appropriate physical polarization or quotient-compatible projector for the $`j`$-th mode.

The zero mode satisfies
``` math
\begin{equation}
  \mu_0=0,
\end{equation}
```
so
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```
This recovers the undamped low-energy gauge field.

Nonzero internal gauge excitations satisfy
``` math
\begin{equation}
  \mu_j^2>0,
\end{equation}
```
and are suppressed by
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{observed gauge fields are undamped zero-mode shadows; nonzero internal gauge
  excitations are admissibility-suppressed.}
  }
  \label{eq:appF-gauge-zero-mode-box}
\end{equation}
```

## Finite electromagnetic source benchmark

A point charge is represented by
``` math
\begin{equation}
  \rho(\mathbf r)=q\delta^{(3)}(\mathbf r).
\end{equation}
```
A Euclidean finite-source benchmark replaces it by
``` math
\begin{equation}
  \rho_\tau(\mathbf r)
  =
  q(4\pi\tau)^{-3/2}
  \exp\left(
    -\frac{r^2}{4\tau}
  \right).
  \label{eq:appF-finite-charge}
\end{equation}
```
This preserves total charge:
``` math
\begin{equation}
  \int_{\mathbb R^3}\rho_\tau(\mathbf r)\,\,\mathrm d^3r=q.
\end{equation}
```

The corresponding potential is
``` math
\begin{equation}
  \Phi_\tau(r)
  =
  \frac{q}{4\pi r}
  \operatorname{erf}
  \left(
    \frac{r}{2\sqrt{\tau}}
  \right).
  \label{eq:appF-finite-Coulomb}
\end{equation}
```

This benchmark is useful for understanding finite source profiles. However, in the FP/fiber realization, direct four-dimensional Gaussian smearing is not automatic. If the finite width is internal, then electromagnetic corrections instead appear through internal-mode exchange:
``` math
\begin{equation}
  \Phi(r)
  =
  \frac{q}{4\pi r}
  \left[
    1+
    \sum_{j\ge1}
    c_j\mathrm e^{-\tau\mu_j^2}\mathrm e^{-\mu_j r}
  \right],
  \label{eq:appF-Coulomb-Yukawa}
\end{equation}
```
where $`c_j`$ depends on the internal gauge-sector overlap.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite Coulomb smearing is a benchmark; FP-realized electromagnetic corrections
  require internal-mode derivation.}
  }
  \label{eq:appF-Coulomb-caution-box}
\end{equation}
```

## Holonomy and global gauge data

Gauge physics is not exhausted by local field strengths. A charged system transported around a closed loop $`\gamma`$ can acquire the phase
``` math
\begin{equation}
  \exp\left(
    \mathrm iq\oint_\gamma A
  \right).
  \label{eq:appF-holonomy}
\end{equation}
```

Under
``` math
\begin{equation}
  A\mapsto A+\,\mathrm d\alpha,
\end{equation}
```
one has
``` math
\begin{equation}
  \oint_\gamma\,\mathrm d\alpha=0
\end{equation}
```
for a single-valued gauge function on a closed loop. Therefore the holonomy is gauge-compatible.

In MTT language:
``` math
\begin{equation}
  \boxed{
  \text{gauge holonomy is Circle phase read through Lens gauge representatives.}
  }
  \label{eq:appF-holonomy-box}
\end{equation}
```

A finite gauge filter must preserve such global gauge data. It must not erase holonomies, flux sectors, or bundle patching conditions unless a lawful transition is derived.

## Flux quantization

For suitable closed two-surfaces $`\Sigma`$, flux quantization has the schematic form
``` math
\begin{equation}
  \frac{1}{2\pi}
  \int_\Sigma F
  \in
  \mathbb Z.
  \label{eq:appF-flux-quantization}
\end{equation}
```
For magnetic monopoles, Dirac quantization gives
``` math
\begin{equation}
  eg=2\pi n,
  \qquad
  n\in\mathbb Z.
  \label{eq:appF-Dirac-quantization}
\end{equation}
```

These are global Lens–Circle consistency conditions. A finite filter that breaks flux quantization or bundle patching is not gauge-admissible.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge finite filtering must preserve global topological consistency.}
  }
  \label{eq:appF-global-consistency-box}
\end{equation}
```

## Anomaly constraints

A chiral gauge theory is consistent only if its gauge anomalies cancel. A finite coherent filter must not spoil this cancellation.

Therefore, any Standard Model or chiral gauge-sector MTT realization must preserve:

1.  gauge anomaly cancellation;

2.  mixed gauge-gravity anomaly cancellation where relevant;

3.  global anomaly constraints;

4.  the correct chiral representation content.

If the filter changes representation weights, removes required states, or introduces anomalous unpaired modes, the gauge sector fails.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{anomaly cancellation is a mandatory gauge-sector admissibility condition.}
  }
  \label{eq:appF-anomaly-box}
\end{equation}
```

## Gauge failure modes

A gauge-sector finite filter fails if:

1.  pure-gauge modes are treated as physical;

2.  $`P_{\rm phys}`$ is not a valid quotient-compatible projector;

3.  the filter breaks Ward identities;

4.  the filter breaks Slavnov–Taylor identities;

5.  BRST cohomology is not preserved;

6.  current conservation is violated;

7.  anomaly cancellation is spoiled;

8.  flux quantization or bundle patching is broken;

9.  longitudinal components acquire unphysical poles;

10. the Lorentzian filter is implemented as naive $`\mathrm e^{-\tau\Box}`$.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge-sector admissibility is quotient compatibility plus identity preservation.}
  }
  \label{eq:appF-failure-box}
\end{equation}
```

## Summary

The gauge-sector finite coherent admissibility operator is
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}
  \chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})
  P_{\rm phys}.
\end{equation}
```

The safe rule is:
``` math
\begin{equation}
  \boxed{
  \text{filter after quotienting, or filter covariantly before quotienting.}
  }
\end{equation}
```

Gauge admissibility requires:

1.  physical projection or gauge covariance;

2.  Ward or Slavnov–Taylor identity preservation;

3.  BRST compatibility where relevant;

4.  current conservation;

5.  anomaly cancellation;

6.  global bundle and flux consistency;

7.  Lorentzian positivity and causal admissibility.

In the FP/fiber realization, the zero-mode gauge sector is undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1,
\end{equation}
```
while nonzero internal gauge excitations are suppressed:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{gauge theory is finite coherent admissibility constrained by Lens quotient structure.}
  }
\end{equation}
```

# Diffeomorphism-compatible gravitational filters

This appendix records the gravitational admissibility conditions used in the main text. The central point is that a finite coherent filter in gravity cannot act on arbitrary coordinate components of the metric. It must act on diffeomorphism-compatible geometric content.

The gravitational finite coherent admissibility operator has the schematic form
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}
  \chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})
  P_{\rm diff}.
  \label{eq:appG-grav-Badm}
\end{equation}
```
Here $`P_{\rm diff}`$ is a diffeomorphism-compatible projection or reduction map, and $`A_{\rm grav}`$ is a positive or constraint-compatible geometric admissibility operator.

The gravitational safe rule is:
``` math
\begin{equation}
  \boxed{
  \text{filter geometric content, not coordinate artifacts.}
  }
  \label{eq:appG-safe-rule}
\end{equation}
```

## Diffeomorphism equivalence

In general relativity, metrics related by diffeomorphism represent the same physical geometry:
``` math
\begin{equation}
  g_{\mu\nu}
  \sim
  \varphi^\ast g_{\mu\nu}.
  \label{eq:appG-diff-equivalence}
\end{equation}
```
Coordinates are therefore Lens representatives. They are not themselves physical labels.

This means that the components
``` math
\begin{equation}
  g_{\mu\nu}(x)
\end{equation}
```
are not independently physical in a coordinate-free sense. A finite filter that smooths or damps metric components in a chosen coordinate chart may fail to be geometrically meaningful.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{a gravitational finite filter must respect diffeomorphism equivalence.}
  }
  \label{eq:appG-diff-box}
\end{equation}
```

## Why naive metric-component smoothing fails

A coordinate-dependent smoothing operation may have the form
``` math
\begin{equation}
  g_{\mu\nu}(x)
  \mapsto
  \int K(x,y)g_{\mu\nu}(y)\,\,\mathrm dy.
\end{equation}
```
This expression is generally not tensorial, not diffeomorphism-compatible, and not tied to the constraint structure of general relativity.

Such an operation can:

1.  depend on the coordinate chart;

2.  fail to preserve the Hamiltonian and momentum constraints;

3.  smooth pure gauge directions as if they were physical;

4.  break stress-energy compatibility;

5.  produce a tensor field that no longer solves the gravitational equations;

6.  alter boundary or horizon data without an admissible geometric rule.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{coordinate-component smoothing is not an admissible gravitational MTT filter.}
  }
  \label{eq:appG-no-component-smoothing}
\end{equation}
```

## ADM data and constraints

On a globally hyperbolic spacetime, one may use an ADM decomposition:
``` math
\begin{equation}
  Y^4\cong\mathbb R\times\Sigma.
\end{equation}
```
The gravitational Cauchy data on a slice $`\Sigma_t`$ are
``` math
\begin{equation}
  (h_{ij},K_{ij}),
\end{equation}
```
or equivalently
``` math
\begin{equation}
  (h_{ij},\pi^{ij}),
\end{equation}
```
where $`h_{ij}`$ is the spatial metric and $`\pi^{ij}`$ is its conjugate momentum.

These data must satisfy the constraints:
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
  \label{eq:appG-ADM-constraints}
\end{equation}
```

Let
``` math
\begin{equation}
  \mathcal C_{\rm grav}
  =
  \{(h_{ij},\pi^{ij}):\mathcal H=0,\ \mathcal H_i=0\}
\end{equation}
```
denote the constraint surface.

A gravitational finite filter is admissible only if it preserves the constraint surface:
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}:
  \mathcal C_{\rm grav}\to\mathcal C_{\rm grav},
  \label{eq:appG-constraint-surface-preservation}
\end{equation}
```
or acts on the reduced quotient:
``` math
\begin{equation}
  \mathcal C_{\rm grav}/\mathrm{Diff}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravitational filtering must preserve the constraint surface or act after reduction.}
  }
  \label{eq:appG-constraint-box}
\end{equation}
```

## Cauchy-slice gravitational filter

A Cauchy-slice gravitational filter has schematic form
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}
  =
  P_{\rm diff}
  \chi(A_{\Sigma}^{\rm grav})
  \mathrm e^{-\tau A_{\Sigma}^{\rm grav}}
  \chi(A_{\Sigma}^{\rm grav})
  P_{\rm diff}.
  \label{eq:appG-cauchy-grav-filter}
\end{equation}
```

Here:
``` math
\begin{align}
  P_{\rm diff}
  &: \text{projection to diffeomorphism- or constraint-compatible content},\\
  A_{\Sigma}^{\rm grav}
  &: \text{positive spatial/geometric admissibility operator},\\
  \chi(A_{\Sigma}^{\rm grav})
  &: \text{admissible spectral window},\\
  \mathrm e^{-\tau A_{\Sigma}^{\rm grav}}
  &: \text{finite damping of inadmissible geometric modes}.
\end{align}
```

This is the gravitational analogue of:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}
  \chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})
  P_{\rm phys}
\end{equation}
```
in gauge theory.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravity requires diffeomorphism-compatible projection just as gauge theory requires
  gauge-compatible projection.}
  }
  \label{eq:appG-gauge-gravity-analogy}
\end{equation}
```

## Constraint-compatibility conditions

In an operator formulation, a strong schematic compatibility condition is:
``` math
\begin{equation}
  [A_{\Sigma}^{\rm grav},\widehat{\mathcal H}]\approx0,
  \qquad
  [A_{\Sigma}^{\rm grav},\widehat{\mathcal H}_i]\approx0,
  \label{eq:appG-constraint-commutators}
\end{equation}
```
where $`\approx0`$ means equality on the constraint surface or modulo constraints.

Similarly, the projector must satisfy:
``` math
\begin{equation}
  P_{\rm diff}
  \mathcal C_{\rm grav}
  \subseteq
  \mathcal C_{\rm grav}.
\end{equation}
```

More generally, one may require only that the full composed filter preserve equivalence classes:
``` math
\begin{equation}
  B_{\Sigma}^{\rm grav}:
  \mathcal C_{\rm grav}/\mathrm{Diff}
  \to
  \mathcal C_{\rm grav}/\mathrm{Diff}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the gravitational admissibility condition is preservation of physical geometric
  equivalence classes.}
  }
  \label{eq:appG-equivalence-class-box}
\end{equation}
```

## Linearized gravity

In weak-field gravity, one expands around a background:
``` math
\begin{equation}
  g_{\mu\nu}
  =
  \bar g_{\mu\nu}+h_{\mu\nu}.
\end{equation}
```
For a flat background,
``` math
\begin{equation}
  \bar g_{\mu\nu}=\eta_{\mu\nu}.
\end{equation}
```

At linear order, infinitesimal diffeomorphisms act by
``` math
\begin{equation}
  h_{\mu\nu}
  \mapsto
  h_{\mu\nu}
  +
  \partial_\mu\xi_\nu
  +
  \partial_\nu\xi_\mu.
  \label{eq:appG-linearized-diff}
\end{equation}
```

The physical graviton modes are transverse-traceless. On a spatial slice, one represents them by
``` math
\begin{equation}
  h_{ij}^{\rm TT},
\end{equation}
```
with
``` math
\begin{equation}
  \partial^i h_{ij}^{\rm TT}=0,
  \qquad
  \delta^{ij}h_{ij}^{\rm TT}=0.
\end{equation}
```

A weak-field admissible gravitational filter is therefore:
``` math
\begin{equation}
  B_{\rm grav}^{\rm lin}
  =
  P_{\rm TT}
  \chi(A_{\rm TT})
  \mathrm e^{-\tau A_{\rm TT}}
  \chi(A_{\rm TT})
  P_{\rm TT},
  \label{eq:appG-linear-filter}
\end{equation}
```
where $`P_{\rm TT}`$ projects to transverse-traceless data and $`A_{\rm TT}\ge0`$ acts on that sector.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{linearized gravitational filtering must act on physical spin-2 data.}
  }
  \label{eq:appG-TT-box}
\end{equation}
```

## Transverse-traceless propagator shadow

In a positive spectral or Euclidean benchmark, a finite graviton propagator shadow may be written schematically as
``` math
\begin{equation}
  D_{\mu\nu\rho\sigma}^{\rm adm}(k)
  \sim
  \frac{F_{\rm adm}(k)}
  {k^2}
  P_{\mu\nu\rho\sigma}^{\rm TT}(k).
  \label{eq:appG-TT-propagator}
\end{equation}
```

In the Euclidean benchmark,
``` math
\begin{equation}
  F_{\rm adm}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```

In the FP/fiber realization, the safer physical analogue is:
``` math
\begin{equation}
  F_{\rm adm}
  \leadsto
  \mathrm e^{-\tau\mu_j^2},
\end{equation}
```
where $`\mu_j^2`$ is an internal geometric or matter-coupled eigenvalue.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite gravitational propagator shadows are meaningful only after physical spin-2 or
  geometric projection.}
  }
  \label{eq:appG-TT-propagator-box}
\end{equation}
```

## Lichnerowicz-type operators

On a curved Riemannian or spatial background, natural geometric operators on symmetric two-tensors include Lichnerowicz-type operators. A representative form is:
``` math
\begin{equation}
  (\Delta_L h)_{\mu\nu}
  =
  -\nabla^2 h_{\mu\nu}
  -
  2R_{\mu\rho\nu\sigma}h^{\rho\sigma}
  +
  R_\mu{}^\rho h_{\rho\nu}
  +
  R_\nu{}^\rho h_{\mu\rho}.
  \label{eq:appG-Lichnerowicz}
\end{equation}
```

The exact sign convention and curvature terms depend on the background, the gauge-fixing choice, and the field space.

In MTT, such an operator is admissible only if it is:

1.  geometric;

2.  positive or controlled on the intended sector;

3.  compatible with constraints;

4.  compatible with diffeomorphism quotienting;

5.  compatible with Lorentzian causality when used in a physical Lorentzian sector.

Thus:
``` math
\begin{equation}
  \boxed{
  A_{\rm grav}
  =
  \text{positive or constraint-compatible geometric stabilization operator}.
  }
  \label{eq:appG-Agrav-box}
\end{equation}
```

## Geometry-dependent heat kernels

For a positive geometric operator $`A_g`$ on a fixed Riemannian geometry, the heat kernel is
``` math
\begin{equation}
  K_g(x,y;\tau)
  =
  \langle x|
  \mathrm e^{-\tau A_g}
  |y\rangle.
\end{equation}
```
For small $`\tau`$, one has a local asymptotic expansion of the schematic form:
``` math
\begin{equation}
  K_g(x,y;\tau)
  \sim
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{\sigma_g(x,y)}{2\tau}
  \right)
  \Delta_g^{1/2}(x,y)
  \left[
    1+\tau a_1(x,y)+\tau^2a_2(x,y)+\cdots
  \right].
  \label{eq:appG-heat-expansion}
\end{equation}
```

This shows that a gravitational finite kernel is shaped by:

1.  geodesic distance;

2.  curvature;

3.  parallel transport;

4.  volume measure;

5.  topology;

6.  boundary conditions.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravitational finite kernels are geometry-dependent coherent responses, not flat
  Gaussians pasted onto spacetime.}
  }
  \label{eq:appG-geometry-dependent-box}
\end{equation}
```

## Stress-energy compatibility

Matter sources coupled to gravity must satisfy
``` math
\begin{equation}
  \nabla_\mu T^{\mu\nu}=0.
  \label{eq:appG-stress-conservation}
\end{equation}
```
A finite coherent matter source may replace a point idealization:
``` math
\begin{equation}
  T_{\mu\nu}(x)
  \sim
  m u_\mu u_\nu\delta(x-x_0)
\end{equation}
```
by
``` math
\begin{equation}
  T_{\mu\nu}^{\rm adm}(x)
  \sim
  m u_\mu u_\nu K_{\rm adm}(x,x_0).
\end{equation}
```

This replacement is admissible only if the resulting stress-energy tensor satisfies conservation and the gravitational constraints.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite stress-energy profiles must be dynamically and geometrically consistent.}
  }
  \label{eq:appG-stress-box}
\end{equation}
```

Finite smoothing of matter sources is not automatically gravitationally admissible.

## Horizons, boundaries, and Nil structure

Gravity contains Nil structures in the form of:

1.  event horizons;

2.  apparent horizons;

3.  trapped surfaces;

4.  singularity boundaries;

5.  asymptotic boundaries;

6.  cosmological boundaries;

7.  black-hole endpoint sectors.

A finite gravitational filter must respect boundary and horizon data. It may not arbitrarily remove, smooth, or mix such structures unless the resulting geometry is an admissible survivor geometry satisfying the constraints.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravitational Nil structures require admissible survivor-geometry rules.}
  }
  \label{eq:appG-nil-boundary-box}
\end{equation}
```

## Curvature as Circle holonomy

Curvature is the infinitesimal holonomy of parallel transport. For a vector $`v^\rho`$,
``` math
\begin{equation}
  [\nabla_\mu,\nabla_\nu]v^\rho
  =
  R^\rho{}_{\sigma\mu\nu}v^\sigma.
  \label{eq:appG-curvature-commutator}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  R^\rho{}_{\sigma\mu\nu}
  =
  \text{Circle holonomy of gravitational frame transport}.
  }
  \label{eq:appG-curvature-circle-box}
\end{equation}
```

The gravitational triplet is therefore:
``` math
\begin{align}
  \mathsf L_{\rm grav}
  &: \text{diffeomorphism quotient and geometric representation},\\
  \mathsf C_{\rm grav}
  &: \text{curvature and frame holonomy},\\
  \mathsf N_{\rm grav}
  &: \text{boundary, horizon, singularity, survivor geometry}.
\end{align}
```

## FP/fiber gravitational tower

In the fixed-point realization, gravitational or geometry-coupled internal excitations may contribute to effective four-dimensional gravity. If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
then internal admissibility gives weight
``` math
\begin{equation}
  W_j=\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

A schematic effective gravitational propagator or response may have the form:
``` math
\begin{equation}
  G_{\rm grav}^{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j^{\rm grav}
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}
  P_j^{\rm phys}(p),
  \label{eq:appG-grav-effective-tower}
\end{equation}
```
where $`P_j^{\rm phys}`$ is the appropriate physical spin/geometric projector.

The zero mode is undamped:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

Nonzero internal modes are suppressed:
``` math
\begin{equation}
  \mu_j^2>0,
  \qquad
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{observed low-energy gravity is the diffeomorphism-compatible zero-mode shadow;
  nonzero internal gravitational excitations are admissibility-suppressed.}
  }
  \label{eq:appG-gravity-zero-mode-box}
\end{equation}
```

## Weak-field phenomenological template

A controlled weak-field execution program is:

1.  choose a background $`\bar g_{\mu\nu}`$;

2.  expand
    ``` math
    \begin{equation}
        g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu};
    \end{equation}
    ```

3.  identify physical perturbations, e.g. transverse-traceless modes;

4.  choose a positive operator $`A_{\rm TT}`$ on that sector;

5.  construct
    ``` math
    \begin{equation}
        B_{\rm grav}^{\rm lin}
        =
        P_{\rm TT}
        \chi(A_{\rm TT})
        \mathrm e^{-\tau A_{\rm TT}}
        \chi(A_{\rm TT})
        P_{\rm TT};
    \end{equation}
    ```

6.  compute finite corrections to propagation or source coupling;

7.  compare with weak-field and gravitational-wave constraints.

This program is perturbative. It does not solve nonperturbative quantum gravity.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{weak-field MTT gravity is an execution benchmark, not the full theory.}
  }
  \label{eq:appG-weak-field-box}
\end{equation}
```

## Nonperturbative execution requirements

A full nonperturbative gravitational MTT sector must supply:
``` math
\begin{equation}
  A_{\rm grav},
  \qquad
  P_{\rm diff},
  \qquad
  \chi_{\rm grav},
  \qquad
  \tau_{\rm grav}.
\end{equation}
```

It must also satisfy:

1.  diffeomorphism compatibility;

2.  Hamiltonian and momentum constraint preservation;

3.  physical state-space construction;

4.  positive or controlled inner product;

5.  recovery of classical general relativity;

6.  Lorentzian causal admissibility;

7.  stress-energy compatibility;

8.  boundary and horizon consistency;

9.  no coordinate-dependent smoothing artifacts.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the schematic gravitational filter is an architecture; full quantum gravity requires
  sectoral construction.}
  }
  \label{eq:appG-nonperturbative-box}
\end{equation}
```

## Gravity failure modes

A gravitational finite filter fails if:

1.  $`A_{\rm grav}`$ is taken to be naive $`\Box_g`$ heat flow;

2.  metric components are damped as coordinate components;

3.  pure diffeomorphism modes are treated as physical;

4.  the Hamiltonian constraint is violated;

5.  the momentum constraints are violated;

6.  the constraint algebra is broken;

7.  stress-energy conservation fails;

8.  boundary or horizon data are erased without an admissible rule;

9.  a perturbative projector is used outside its regime;

10. observable predictions depend on arbitrary coordinate or foliation choices.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravitational admissibility is diffeomorphism compatibility plus constraint
  preservation.}
  }
  \label{eq:appG-failure-box}
\end{equation}
```

## Summary

The gravitational finite coherent admissibility operator is:
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}
  \chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})
  P_{\rm diff}.
\end{equation}
```

It is admissible only when it acts on diffeomorphism-compatible geometric content.

In ADM form, it must preserve:
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
\end{equation}
```

In weak-field form, it should act on physical transverse-traceless data:
``` math
\begin{equation}
  B_{\rm grav}^{\rm lin}
  =
  P_{\rm TT}
  \chi(A_{\rm TT})
  \mathrm e^{-\tau A_{\rm TT}}
  \chi(A_{\rm TT})
  P_{\rm TT}.
\end{equation}
```

In the FP/fiber realization, zero-mode gravity is undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1,
\end{equation}
```
while nonzero internal geometric excitations are suppressed:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{gravity is finite coherent admissibility constrained by diffeomorphism-compatible
  geometry.}
  }
\end{equation}
```

# Fixed-point fiber realization and dimensional reduction

This appendix records the fixed-point/fiber realization that gives the finite coherent admissibility operator its geometric backbone. The purpose is to make explicit how the abstract operator
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
\end{equation}
```
is realized in the compact internal/fiber setting and how its four-dimensional shadows arise after dimensional reduction.

The central fixed-point realization is:
``` math
\begin{equation}
  \boxed{
  M_{10}=Y^4\times X^6,
  }
  \label{eq:appH-M10}
\end{equation}
```
where $`Y^4`$ is the observed Lorentzian base and $`X^6`$ is a compact Riemannian internal space or compact internal fiber geometry.

The finite coherent admissibility operator acts primarily on internal/fiber spectral data:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}
  \chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})
  P_{\rm coh}.
  }
  \label{eq:appH-FP-Badm}
\end{equation}
```

## Total space and sectoral Hilbert data

Let
``` math
\begin{equation}
  M_{10}=Y^4\times X^6.
\end{equation}
```
The base $`Y^4`$ carries Lorentzian dynamics. The internal space $`X^6`$ is compact and Riemannian. A simple scalar Hilbert space model is
``` math
\begin{equation}
  \mathcal H_{10}
  =
  L^2(Y^4)\otimes L^2(X^6),
\end{equation}
```
or, more carefully in Lorentzian settings, a Cauchy-space Hilbert structure of the form
``` math
\begin{equation}
  \mathcal H_{\Sigma}
  =
  L^2(\Sigma)\otimes L^2(X^6),
\end{equation}
```
where $`\Sigma\subset Y^4`$ is a Cauchy slice.

For fields with spin, gauge, or bundle content, one replaces $`L^2(X^6)`$ by sections of the appropriate internal bundle:
``` math
\begin{equation}
  L^2(X^6,E).
\end{equation}
```

Thus the generic sectoral Hilbert data have the form
``` math
\begin{equation}
  \mathcal H_{\rm sector}
  =
  \mathcal H_{Y,\rm sector}
  \otimes
  \mathcal H_{X,\rm sector},
  \label{eq:appH-sector-Hilbert}
\end{equation}
```
subject to gauge, gravitational, and constraint reductions when relevant.

## Internal admissibility operator

The fixed-point internal admissibility operator is
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  \kappa_n>0.
  \label{eq:appH-Aint}
\end{equation}
```
Here $`\Delta_{B_n}`$ are positive fiber Laplacians or sectoral positive elliptic operators on compact internal directions.

Since each $`\Delta_{B_n}`$ is nonnegative and $`\kappa_n>0`$,
``` math
\begin{equation}
  A_{\rm int}\ge0.
\end{equation}
```

This positivity is the key analytic reason the FP realization avoids the Lorentzian $`\mathrm e^{-\tau\Box}`$ problem. The damping factor is:
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}},
\end{equation}
```
not
``` math
\begin{equation}
  \mathrm e^{-\tau\Box_Y}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{FP damping acts on compact positive internal spectra, not on the indefinite
  Lorentzian d'Alembertian.}
  }
  \label{eq:appH-internal-not-box}
\end{equation}
```

## Internal spectrum

Because $`X^6`$ is compact and $`A_{\rm int}`$ is elliptic in the internal directions, the spectrum is discrete in the clean compact case:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
  \label{eq:appH-internal-spectrum}
\end{equation}
```
with
``` math
\begin{equation}
  0=\mu_0^2
  \le
  \mu_1^2
  \le
  \mu_2^2
  \le
  \cdots.
\end{equation}
```

The finite damping factor acts as
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}\phi_j
  =
  \mathrm e^{-\tau\mu_j^2}\phi_j.
  \label{eq:appH-internal-damping}
\end{equation}
```

The zero mode is undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_0^2}=1.
  \label{eq:appH-zero-mode-undamped}
\end{equation}
```

The nonzero modes are suppressed:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_j^2}<1.
  \label{eq:appH-nonzero-suppressed}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{zero modes survive; nonzero internal modes are admissibility-damped.}
  }
  \label{eq:appH-zero-nonzero-box}
\end{equation}
```

## The coherent projector

The fixed-point coherent projector is
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
  \label{eq:appH-Pcoh}
\end{equation}
```
where $`\Pi_{B_n}`$ projects to the harmonic sector of the $`n`$-th internal/fiber operator.

Its range is
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3
  \ker\Delta_{B_n}.
  \label{eq:appH-joint-kernel}
\end{equation}
```

Thus the coherent sector is not a vague retained sector. It is the joint fiber-harmonic sector:
``` math
\begin{equation}
  \boxed{
  \mathcal H_{\rm coh}
  =
  \bigcap_{n=1}^3
  \ker\Delta_{B_n}.
  }
  \label{eq:appH-coherent-sector-box}
\end{equation}
```

In the clean spectral setting,
``` math
\begin{equation}
  [P_{\rm coh},A_{\rm int}]=0.
\end{equation}
```
Therefore the commuting modal formula applies:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}\phi_j
  =
  p_j
  \chi(\mu_j^2)^2
  \mathrm e^{-\tau\mu_j^2}
  \phi_j,
  \label{eq:appH-FP-modal-action}
\end{equation}
```
where
``` math
\begin{equation}
  P_{\rm coh}\phi_j=p_j\phi_j,
  \qquad
  p_j\in\{0,1\}.
\end{equation}
```

## The gap-selected damping scale

Let $`\lambda_\ast>0`$ be the relevant uniform spectral gap in the discarded internal sector. Assume the discarded-sector flow satisfies
``` math
\begin{equation}
  \|Q\Phi_tQ\|
  \le
  C_Q\mathrm e^{-\lambda_\ast t},
  \label{eq:appH-gap-flow}
\end{equation}
```
where
``` math
\begin{equation}
  Q=I-P_{\rm coh}.
\end{equation}
```

Given an admissibility tolerance
``` math
\begin{equation}
  0<\epsilon_{\rm adm}<1,
\end{equation}
```
the damping-selected time is defined by
``` math
\begin{equation}
  C_Q\mathrm e^{-\lambda_\ast\tau}=\epsilon_{\rm adm}.
\end{equation}
```
Solving gives
``` math
\begin{equation}
  \boxed{
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
  }
  \label{eq:appH-tau-gap}
\end{equation}
```

If the characteristic internal radius is $`R`$, then for Laplace-type operators,
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2}.
\end{equation}
```
Therefore
``` math
\begin{equation}
  \tau
  \sim
  R^2
  \log\frac{C_Q}{\epsilon_{\rm adm}},
  \label{eq:appH-tau-R}
\end{equation}
```
and
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
  \label{eq:appH-lcoh-R}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the finite coherent width is geometrically tied to the internal spectral gap.}
  }
  \label{eq:appH-geometric-width-box}
\end{equation}
```

## Dimensional reduction

A field on the total space may be expanded in internal eigenmodes:
``` math
\begin{equation}
  \Phi(x,z)
  =
  \sum_{j\ge0}
  \varphi_j(x)\phi_j(z),
  \qquad
  x\in Y^4,
  \quad
  z\in X^6.
  \label{eq:appH-KK-expansion}
\end{equation}
```

If
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
then $`\mu_j^2`$ appears in the four-dimensional effective theory as an internal mass contribution. In the simplest scalar model:
``` math
\begin{equation}
  m_j^2=m_0^2+\mu_j^2.
  \label{eq:appH-effective-mass}
\end{equation}
```

The finite admissibility factor contributes:
``` math
\begin{equation}
  W_j
  =
  \mathrm e^{-\tau\mu_j^2}.
  \label{eq:appH-Wj}
\end{equation}
```

Thus the schematic four-dimensional effective propagator is:
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j\chi(\mu_j^2)^2
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}.
  \label{eq:appH-effective-propagator}
\end{equation}
```

Here $`Z_j`$ depends on normalization, internal wavefunction overlap, sectoral projection, and physical-state positivity.

The zero-mode term is:
``` math
\begin{equation}
  \frac{Z_0\chi(0)^2}{p^2-m_0^2+\mathrm i\epsilon}.
\end{equation}
```
If
``` math
\begin{equation}
  \chi(0)=1,
\end{equation}
```
the zero-mode propagation is undamped.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{ordinary four-dimensional low-energy physics is recovered from undamped zero modes.}
  }
  \label{eq:appH-zero-mode-recovery-box}
\end{equation}
```

## Källén–Lehmann positivity

A four-dimensional spectral representation is physically acceptable only if the residues in the physical sector are nonnegative:
``` math
\begin{equation}
  Z_j\ge0.
\end{equation}
```

The damping factor
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
is positive, so it does not by itself introduce negative residues. However, it also does not repair a sector that already contains ghosts, negative-norm states, or constraint violations.

Thus the effective propagator
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j\mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}
\end{equation}
```
is Källén–Lehmann positive only when
``` math
\begin{equation}
  Z_j\ge0
\end{equation}
```
in the physical sector.

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{internal damping preserves positive residues but does not cure nonphysical sectors.}
  }
  \label{eq:appH-KL-box}
\end{equation}
```

## Gauge-sector dimensional reduction

For gauge fields, dimensional reduction must respect the gauge quotient. A schematic gauge-sector tower has the form:
``` math
\begin{equation}
  D_{\mu\nu}^{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j^{\rm gauge}
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}
  P_{\mu\nu}^{(j)}(p).
  \label{eq:appH-gauge-tower}
\end{equation}
```

Here $`P_{\mu\nu}^{(j)}`$ is the physical polarization or quotient-compatible projector for the $`j`$-th mode.

The gauge-sector zero mode must reproduce the observed low-energy gauge field:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

Nonzero internal gauge excitations are suppressed:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gauge dimensional reduction must produce undamped physical zero modes and
  quotient-compatible damped excitations.}
  }
  \label{eq:appH-gauge-reduction-box}
\end{equation}
```

## Gravity-sector dimensional reduction

For gravity, dimensional reduction must respect diffeomorphism compatibility and constraints. A schematic gravitational tower has the form:
``` math
\begin{equation}
  G_{\rm grav}^{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j^{\rm grav}
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}
  P_j^{\rm phys}(p),
  \label{eq:appH-gravity-tower}
\end{equation}
```
where $`P_j^{\rm phys}`$ is the appropriate spin/geometric physical projector.

The zero-mode gravitational sector must reproduce the observed low-energy gravitational field:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  \mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

Nonzero internal geometric excitations are suppressed:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{gravity dimensional reduction must be diffeomorphism-compatible and constraint
  preserving.}
  }
  \label{eq:appH-gravity-reduction-box}
\end{equation}
```

## Internal overlaps and effective couplings

Effective four-dimensional couplings are determined by internal overlap integrals. For example, a schematic quartic scalar coupling may reduce as:
``` math
\begin{equation}
  \lambda_{ijkl}^{\rm eff}
  =
  \lambda_{10D}
  \int_{X^6}
  \phi_i(z)\phi_j(z)\phi_k(z)\phi_l(z)
  \,\,\mathrm d\mu_X(z).
  \label{eq:appH-overlap-coupling}
\end{equation}
```

With finite admissibility, the corresponding contribution carries mode weights:
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_i^2},
  \qquad
  \mathrm e^{-\tau\mu_j^2},
  \qquad
  \mathrm e^{-\tau\mu_k^2},
  \qquad
  \mathrm e^{-\tau\mu_l^2},
\end{equation}
```
depending on how the finite filter enters the vertex.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{effective couplings are internal overlap integrals dressed by admissibility weights.}
  }
  \label{eq:appH-overlap-box}
\end{equation}
```

This is why numerical predictions require explicit internal geometry.

## Locality in total space and shadows on the base

In the total space $`M_{10}`$, dynamics or support may be local or controlled in the internal directions. After projection to $`Y^4`$, the same structure can appear as:

1.  finite source profiles;

2.  finite detector effects;

3.  non-pointlike form factors;

4.  suppressed internal-mode towers;

5.  apparent finite nonlocality;

6.  effective mixed states from unobserved internal variables.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{four-dimensional finite nonlocality can be a projection shadow of controlled
  total-space or fiber structure.}
  }
  \label{eq:appH-locality-shadow-box}
\end{equation}
```

This does not license arbitrary nonlocality. The Lorentzian base must still satisfy causal admissibility.

## Base–fiber entanglement

A total state may fail to factor between base and internal variables:
``` math
\begin{equation}
  \Psi(x,z)
  \neq
  \psi(x)\phi(z).
\end{equation}
```
In an internal eigenbasis:
``` math
\begin{equation}
  \Psi(x,z)
  =
  \sum_j
  \psi_j(x)\phi_j(z).
  \label{eq:appH-base-fiber-expansion}
\end{equation}
```

If more than one internal mode contributes coherently, the base and fiber sectors may be entangled.

After internal projection or tracing over inaccessible internal data, the four-dimensional effective state may appear mixed:
``` math
\begin{equation}
  \rho_Y
  =
  \operatorname{tr}_X|\Psi\rangle\langle\Psi|.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{some effective four-dimensional mixedness may be the shadow of base--fiber
  entanglement.}
  }
  \label{eq:appH-base-fiber-entanglement-box}
\end{equation}
```

## Internal coherence and Circle–Lens–Nil

The FP/fiber realization has a direct Circle–Lens–Nil reading.

Circle is internal spectral coherence:
``` math
\begin{equation}
  \mathsf C_{\rm FP}
  =
  \text{fiber phase, harmonicity, internal spectral closure}.
\end{equation}
```

Lens is projection to the coherent joint harmonic sector:
``` math
\begin{equation}
  \mathsf L_{\rm FP}
  =
  P_{\rm coh}.
\end{equation}
```

Nil is damping of nonzero internal modes:
``` math
\begin{equation}
  \mathsf N_{\rm FP}
  =
  \mathrm e^{-\tau A_{\rm int}}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  \text{Circle-coherent internal modes}
  \xrightarrow{\mathsf L}
  \text{joint harmonic sector}
  \xrightarrow{\mathsf N}
  \text{suppressed nonzero excitations}.
  }
  \label{eq:appH-CLN-box}
\end{equation}
```

## Relation to Kaluza–Klein theory

The FP/fiber realization is explicitly Kaluza–Klein-compatible. The compact internal space produces a tower of four-dimensional modes:
``` math
\begin{equation}
  \mu_j^2
  \quad
  \longrightarrow
  \quad
  m_j^2=m_0^2+\mu_j^2.
\end{equation}
```

The MTT-specific addition is the finite coherent admissibility weight:
``` math
\begin{equation}
  W_j=\mathrm e^{-\tau\mu_j^2},
\end{equation}
```
together with the projection architecture:
``` math
\begin{equation}
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{ordinary KK gives internal towers; FP/MTT gives internal towers filtered by finite
  coherent admissibility.}
  }
  \label{eq:appH-KK-MTT-box}
\end{equation}
```

This is a strength, not a weakness. It gives the MTT finite scale a concrete geometric origin.

## Phenomenological scale translation

If experiments constrain the first internal excitation by
``` math
\begin{equation}
  \mu_1\gtrsim M_{\rm exp},
\end{equation}
```
then
``` math
\begin{equation}
  R\lesssim M_{\rm exp}^{-1}.
\end{equation}
```

Using
``` math
\begin{equation}
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  },
\end{equation}
```
one obtains
``` math
\begin{equation}
  \sqrt{\tau}
  \lesssim
  M_{\rm exp}^{-1}
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
  \label{eq:appH-scale-bound}
\end{equation}
```

Equivalently:
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \tau^{-1/2}
  \gtrsim
  M_{\rm exp}
  \left(
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  \right)^{-1/2}.
  \label{eq:appH-Lambda-bound}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{bounds on internal excitations translate into bounds on }R,\sqrt{\tau},\Lambda_{\rm eff}.
  }
  \label{eq:appH-bound-box}
\end{equation}
```

Precise numbers require explicit internal geometry, representation data, and couplings.

## Failure modes

The FP/fiber realization fails if:

1.  $`A_{\rm int}`$ is not positive;

2.  $`P_{\rm coh}`$ does not project to the joint harmonic sector;

3.  $`[P_{\rm coh},A_{\rm int}]\neq0`$ but diagonal modal weights are assumed anyway;

4.  the zero mode is removed or damped;

5.  $`\chi(0)\neq1`$ when low-energy recovery requires $`\chi(0)=1`$;

6.  internal excitations violate experimental bounds;

7.  gauge quotienting is not preserved;

8.  gravitational constraints are not preserved;

9.  Källén–Lehmann positivity fails;

10. the KK-style structure is hidden rather than stated honestly.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{FP/MTT is physically meaningful only when internal spectral damping, zero-mode
  recovery, quotient compatibility, and positivity all hold.}
  }
  \label{eq:appH-failure-box}
\end{equation}
```

## Summary

The fixed-point/fiber realization places MTT on:
``` math
\begin{equation}
  M_{10}=Y^4\times X^6,
\end{equation}
```
with Lorentzian base $`Y^4`$ and compact Riemannian internal space $`X^6`$.

The internal admissibility operator is:
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```

The coherent projector is:
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
with:
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3
  \ker\Delta_{B_n}.
\end{equation}
```

The fixed-point finite coherent admissibility operator is:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}
  \chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})
  P_{\rm coh}.
\end{equation}
```

Internal eigenmodes satisfy:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j,
\end{equation}
```
with weights:
``` math
\begin{equation}
  W_j=\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Zero modes are undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  W_0=1.
\end{equation}
```

Nonzero modes are suppressed:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  W_j<1.
\end{equation}
```

The damping scale is:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the FP realization gives finite coherent admissibility a concrete compact-fiber,
  KK-compatible, positive-spectral foundation.}
  }
\end{equation}
```

# Phenomenological scale relations and execution templates

This appendix collects the scale relations used in the phenomenology section. The purpose is to make explicit how the internal spectral gap, the damping time $`\tau`$, the coherent length $`\ell_{\rm coh}`$, and the effective four-dimensional excitation scale are related.

The central chain is:
``` math
\begin{equation}
  \boxed{
  \lambda_\ast
  \sim
  R^{-2}
  \quad\Longrightarrow\quad
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}
  \quad\Longrightarrow\quad
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \sim
  R\sqrt{\log(C_Q/\epsilon_{\rm adm})}.
  }
  \label{eq:appI-main-chain}
\end{equation}
```

Equivalently:
``` math
\begin{equation}
  \boxed{
  \Lambda_{\rm eff}
  =
  \tau^{-1/2}
  \sim
  R^{-1}
  \left(
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  \right)^{-1/2}.
  }
  \label{eq:appI-Lambda-chain}
\end{equation}
```

These relations are structural. Precise numerical predictions require a completed sectoral model.

## Dimensions

A Laplace-type internal operator has dimension
``` math
\begin{equation}
  [A_{\rm int}]
  =
  L^{-2}
  =
  E^2
\end{equation}
```
in units where $`\hbar=c=1`$.

The damping factor
``` math
\begin{equation}
  \mathrm e^{-\tau A_{\rm int}}
\end{equation}
```
is dimensionless, so
``` math
\begin{equation}
  [\tau]=L^2=E^{-2}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
\end{equation}
```
has dimensions of length, and
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \tau^{-1/2}
\end{equation}
```
has dimensions of energy.

Thus:
``` math
\begin{equation}
  \boxed{
  \tau
  \text{ is a length-squared or inverse-energy-squared scale.}
  }
  \label{eq:appI-tau-dimension-box}
\end{equation}
```

## Internal radius and spectral gap

Let $`R`$ denote a characteristic internal length scale. For a compact internal Laplace-type operator, the first nonzero eigenvalue is typically of order
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2}.
  \label{eq:appI-gap-radius}
\end{equation}
```

More precisely, the coefficient depends on the internal geometry, boundary conditions, bundle structure, curvature, and normalization of the operator. Thus one may write
``` math
\begin{equation}
  \lambda_\ast
  =
  c_X R^{-2},
  \label{eq:appI-gap-cX}
\end{equation}
```
where $`c_X`$ is a dimensionless geometry-dependent constant.

Then
``` math
\begin{equation}
  \tau
  =
  \frac{1}{c_X}R^2
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
  \label{eq:appI-tau-cX}
\end{equation}
```

Hence
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  =
  \frac{R}{\sqrt{c_X}}
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
  \label{eq:appI-lcoh-cX}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \ell_{\rm coh}
  \text{ is generically of order the internal radius, up to gap and tolerance factors.}
  }
  \label{eq:appI-lcoh-order-box}
\end{equation}
```

## Damping-selected time

The damping-selected time is defined by the discarded-sector condition
``` math
\begin{equation}
  C_Q\mathrm e^{-\lambda_\ast\tau}
  =
  \epsilon_{\rm adm}.
\end{equation}
```
Solving gives
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
  \label{eq:appI-tau-selected}
\end{equation}
```

This means that $`\tau`$ is not an arbitrary ultraviolet cutoff. It is selected by:

1.  the discarded-sector gap $`\lambda_\ast`$;

2.  the discarded-sector constant $`C_Q`$;

3.  the admissibility tolerance $`\epsilon_{\rm adm}`$.

Thus:
``` math
\begin{equation}
  \boxed{
  \tau
  \text{ measures how long the positive internal damping must act to suppress the discarded
  sector below tolerance.}
  }
  \label{eq:appI-tau-meaning-box}
\end{equation}
```

## First-mode admissibility weight

Let the first nonzero internal eigenvalue be
``` math
\begin{equation}
  \mu_1^2.
\end{equation}
```
The corresponding amplitude-level admissibility weight is
``` math
\begin{equation}
  W_1
  =
  \mathrm e^{-\tau\mu_1^2}.
  \label{eq:appI-W1}
\end{equation}
```

If
``` math
\begin{equation}
  \mu_1^2\simeq\lambda_\ast,
\end{equation}
```
then using <a href="#eq:appI-tau-selected" data-reference-type="eqref" data-reference="eq:appI-tau-selected">[eq:appI-tau-selected]</a> gives
``` math
\begin{equation}
  W_1
  \simeq
  \mathrm e^{-\log(C_Q/\epsilon_{\rm adm})}
  =
  \frac{\epsilon_{\rm adm}}{C_Q}.
  \label{eq:appI-W1-eps}
\end{equation}
```

More generally, define
``` math
\begin{equation}
  r_1
  =
  \frac{\mu_1^2}{\lambda_\ast}.
\end{equation}
```
Then
``` math
\begin{equation}
  W_1
  =
  \left(
    \frac{\epsilon_{\rm adm}}{C_Q}
  \right)^{r_1}.
  \label{eq:appI-W1-r}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  W_j
  =
  \mathrm e^{-\tau\mu_j^2}
  }
\end{equation}
```
is the universal amplitude-level internal-mode weight, while its numerical value depends on the internal spectrum and tolerance choice.

## Illustrative tolerance benchmark

As an illustrative benchmark, take
``` math
\begin{equation}
  C_Q=1,
  \qquad
  \epsilon_{\rm adm}=10^{-3}.
\end{equation}
```
Then
``` math
\begin{equation}
  \log\frac{C_Q}{\epsilon_{\rm adm}}
  =
  \log(10^3)
  \simeq
  6.9.
\end{equation}
```

If
``` math
\begin{equation}
  c_X=1,
\end{equation}
```
then
``` math
\begin{equation}
  \ell_{\rm coh}
  \simeq
  \sqrt{6.9}\,R
  \simeq
  2.6R.
  \label{eq:appI-illustrative-lcoh}
\end{equation}
```

If also
``` math
\begin{equation}
  \mu_1^2\simeq\lambda_\ast,
\end{equation}
```
then
``` math
\begin{equation}
  W_1\simeq10^{-3}.
  \label{eq:appI-illustrative-W1}
\end{equation}
```

This benchmark is not a universal prediction. It is a scale example. A different $`C_Q`$, $`\epsilon_{\rm adm}`$, geometry factor $`c_X`$, or internal spectrum changes the coefficient.

Thus:
``` math
\begin{equation}
  \boxed{
  \epsilon_{\rm adm}
  \text{ must ultimately be derived or fixed by sectoral admissibility, not chosen freely.}
  }
  \label{eq:appI-epsadm-warning-box}
\end{equation}
```

## Energy-length conversion

In natural units,
``` math
\begin{equation}
  \hbar c
  \simeq
  1.97\times10^{-16}\,{\rm GeV\,m}.
\end{equation}
```
Therefore an energy scale $`M`$ corresponds to a length
``` math
\begin{equation}
  M^{-1}
  \simeq
  \frac{1.97\times10^{-16}\,{\rm m}}{M/{\rm GeV}}.
  \label{eq:appI-energy-length}
\end{equation}
```

For example, if
``` math
\begin{equation}
  M=1\,{\rm TeV}=10^3\,{\rm GeV},
\end{equation}
```
then
``` math
\begin{equation}
  M^{-1}
  \simeq
  2.0\times10^{-19}\,{\rm m}.
  \label{eq:appI-TeV-length}
\end{equation}
```

Thus an internal excitation scale
``` math
\begin{equation}
  \mu_1\sim M
\end{equation}
```
corresponds to
``` math
\begin{equation}
  R\sim M^{-1}.
\end{equation}
```

This conversion is useful for translating collider or scattering bounds into internal length bounds.

## Bound translation

Suppose an experiment constrains the first visible internal excitation to satisfy
``` math
\begin{equation}
  \mu_1\gtrsim M_{\rm exp}.
  \label{eq:appI-mu-bound}
\end{equation}
```
Then
``` math
\begin{equation}
  R\lesssim M_{\rm exp}^{-1}.
  \label{eq:appI-R-bound}
\end{equation}
```

Using
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \frac{R}{\sqrt{c_X}}
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  },
\end{equation}
```
one obtains
``` math
\begin{equation}
  \ell_{\rm coh}
  \lesssim
  \frac{1}{M_{\rm exp}\sqrt{c_X}}
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
  \label{eq:appI-lcoh-bound}
\end{equation}
```

Equivalently,
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \ell_{\rm coh}^{-1}
  \gtrsim
  M_{\rm exp}\sqrt{c_X}
  \left(
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  \right)^{-1/2}.
  \label{eq:appI-Lambda-bound}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \mu_1\gtrsim M_{\rm exp}
  \quad
  \Rightarrow
  \quad
  R\lesssim M_{\rm exp}^{-1},
  \quad
  \ell_{\rm coh}\lesssim M_{\rm exp}^{-1}\sqrt{\log(C_Q/\epsilon_{\rm adm})/c_X}.
  }
  \label{eq:appI-bound-box}
\end{equation}
```

## Effective tower response

After dimensional reduction, the generic four-dimensional response has the schematic form
``` math
\begin{equation}
  G_{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j
    \chi(\mu_j^2)^2
    \mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}.
  \label{eq:appI-effective-tower}
\end{equation}
```

The zero-mode term has
``` math
\begin{equation}
  \mu_0=0.
\end{equation}
```
If
``` math
\begin{equation}
  \chi(0)=1,
\end{equation}
```
then the zero-mode weight is
``` math
\begin{equation}
  \chi(0)^2\mathrm e^{-\tau\mu_0^2}=1.
\end{equation}
```

The nonzero-mode terms have
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}<1.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  G_{\rm eff}
  =
  G_{\rm zero}
  +
  G_{\rm damped\ tower}.
  }
  \label{eq:appI-zero-plus-tower}
\end{equation}
```

This is the basic phenomenological form of the FP/MTT reduction.

## Low-energy expansion

At energies much smaller than the first internal excitation,
``` math
\begin{equation}
  E\ll\mu_1,
\end{equation}
```
the nonzero internal modes can be integrated out. Their effects appear as higher-dimensional operators suppressed by powers of
``` math
\begin{equation}
  \frac{E}{\mu_j},
\end{equation}
```
and by admissibility weights
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

A generic correction has the form
``` math
\begin{equation}
  \delta\mathcal O
  \sim
  \sum_{j\ge1}
  C_j
  \mathrm e^{-\tau\mu_j^2}
  \left(
    \frac{E}{\mu_j}
  \right)^{d_j}.
  \label{eq:appI-low-energy-correction}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{low-energy corrections are suppressed both by heavy-mode decoupling and by finite
  admissibility.}
  }
  \label{eq:appI-low-energy-box}
\end{equation}
```

## Collider amplitude template

If an internal excitation $`j`$ can be produced in a collider process, its schematic amplitude contribution is
``` math
\begin{equation}
  \mathcal A_j(s)
  \sim
  g_j^{\rm in}g_j^{\rm out}
  \frac{
    \mathrm e^{-\tau\mu_j^2}
  }
  {s-m_j^2+\mathrm im_j\Gamma_j}.
  \label{eq:appI-collider-amplitude}
\end{equation}
```

Here:
``` math
\begin{align}
  g_j^{\rm in}
  &: \text{effective production coupling},\\
  g_j^{\rm out}
  &: \text{effective decay coupling},\\
  \Gamma_j
  &: \text{width},\\
  m_j^2
  &: \text{effective four-dimensional mass}.
\end{align}
```

The observable cross section depends on
``` math
\begin{equation}
  |\mathcal A_{\rm SM}+\sum_j\mathcal A_j|^2.
\end{equation}
```

Therefore the amplitude weight
``` math
\begin{equation}
  \mathrm e^{-\tau\mu_j^2}
\end{equation}
```
does not by itself determine a universal cross-section suppression. Interference, width, phase space, spin, gauge representation, internal overlap, and detector acceptance all matter.

Thus:
``` math
\begin{equation}
  \boxed{
  W_j=\mathrm e^{-\tau\mu_j^2}
  \text{ is an amplitude-level admissibility weight, not a complete collider prediction.}
  }
  \label{eq:appI-cross-section-caution}
\end{equation}
```

## Yukawa correction template

A massive internal mode exchanged between four-dimensional sources produces a Yukawa-type correction. A generic static potential has the schematic form
``` math
\begin{equation}
  V(r)
  =
  V_0(r)
  \left[
    1+
    \sum_{j\ge1}
    a_j
    \mathrm e^{-\tau\mu_j^2}
    \mathrm e^{-\mu_j r}
  \right],
  \label{eq:appI-Yukawa-template}
\end{equation}
```
where $`a_j`$ depends on couplings, overlaps, and representations.

For electromagnetism:
``` math
\begin{equation}
  V_0(r)=\frac{q_1q_2}{4\pi r}.
\end{equation}
```

For Newtonian gravity:
``` math
\begin{equation}
  V_0(r)=-\frac{Gm_1m_2}{r}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{FP-realized short-distance corrections are typically Yukawa tower corrections dressed
  by admissibility weights.}
  }
  \label{eq:appI-Yukawa-box}
\end{equation}
```

Direct four-dimensional Gaussian smearing is a useful benchmark only when a four-dimensional finite source profile has been derived.

## Finite source benchmark

A finite four-dimensional source benchmark replaces
``` math
\begin{equation}
  \delta^{(3)}(\mathbf r)
\end{equation}
```
by
``` math
\begin{equation}
  K_\tau^{(3)}(\mathbf r)
  =
  (4\pi\tau)^{-3/2}
  \exp\left(
    -\frac{r^2}{4\tau}
  \right).
\end{equation}
```

For electromagnetism, this gives the finite Coulomb benchmark:
``` math
\begin{equation}
  \Phi_\tau(r)
  =
  \frac{q}{4\pi r}
  \operatorname{erf}
  \left(
    \frac{r}{2\sqrt{\tau}}
  \right).
  \label{eq:appI-finite-Coulomb}
\end{equation}
```

But this benchmark should not be automatically identified with the FP/fiber prediction. In the FP realization, the finite width is primarily internal unless a physical four-dimensional source kernel is derived.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite Coulomb smearing is a source-profile benchmark; internal-mode exchange is the
  default FP correction mechanism.}
  }
  \label{eq:appI-finite-source-caution}
\end{equation}
```

## Measurement visibility template

For a two-branch interference experiment, branch damping gives
``` math
\begin{equation}
  V_{\rm obs}
  =
  |D_{12}|V_0.
  \label{eq:appI-visibility-template}
\end{equation}
```

If
``` math
\begin{equation}
  D_{12}
  =
  \mathrm e^{-\tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}},
\end{equation}
```
then
``` math
\begin{equation}
  \log\frac{V_0}{V_{\rm obs}}
  =
  \tau_{\mathsf M}\Lambda_{12}^{(\mathsf M)}.
  \label{eq:appI-visibility-log}
\end{equation}
```

This gives a direct way to fit measurement-context damping:
``` math
\begin{equation}
  \boxed{
  \text{visibility loss measures off-diagonal branch damping.}
  }
\end{equation}
```

It does not by itself determine outcome probabilities. Those require basin measures:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{
    \mu(B_i^{(\mathsf M)})
  }{
    \sum_j\mu(B_j^{(\mathsf M)})
  }.
\end{equation}
```

## Entanglement and no-signaling template

A joint measurement model supplies probabilities
``` math
\begin{equation}
  p(a,b|x,y),
\end{equation}
```
where $`x,y`$ are local settings and $`a,b`$ are outcomes.

Admissibility requires no-signaling:
``` math
\begin{equation}
  \sum_b p(a,b|x,y)
  =
  \sum_b p(a,b|x,y')
  \label{eq:appI-no-signaling-A}
\end{equation}
```
and
``` math
\begin{equation}
  \sum_a p(a,b|x,y)
  =
  \sum_a p(a,b|x',y).
  \label{eq:appI-no-signaling-B}
\end{equation}
```

In MTT terms, this constrains:

1.  the joint coherent sector $`P_{AB}`$;

2.  the joint admissibility operator $`A_{AB}`$;

3.  the measurement effects $`E_{ab}^{(x,y)}`$;

4.  the branch damping channel;

5.  the survivor-basin measure.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{joint coherent admissibility may be non-factorizing, but local record statistics must
  obey no-signaling.}
  }
  \label{eq:appI-no-signaling-box}
\end{equation}
```

## Execution table

The following table summarizes the main quantities.

<div class="center">

| Quantity | Symbol | Meaning |
|:--:|:--:|:--:|
| Internal radius | $`R`$ | characteristic compact-fiber size |
| Geometry factor | $`c_X`$ | $`\lambda_\ast=c_XR^{-2}`$ |
| Spectral gap | $`\lambda_\ast`$ | first relevant nonzero internal gap |
| Tolerance | $`\epsilon_{\rm adm}`$ | admissibility threshold |
| Discarded-sector constant | $`C_Q`$ | gap estimate prefactor |
| Damping time | $`\tau`$ | $`\lambda_\ast^{-1}\log(C_Q/\epsilon_{\rm adm})`$ |
| Coherent length | $`\ell_{\rm coh}`$ | $`\sqrt{\tau}`$ |
| Effective energy | $`\Lambda_{\rm eff}`$ | $`\tau^{-1/2}`$ |
| Internal eigenvalue | $`\mu_j^2`$ | $`A_{\rm int}\phi_j=\mu_j^2\phi_j`$ |
| Mode weight | $`W_j`$ | $`\mathrm e^{-\tau\mu_j^2}`$ |
| Tower residue | $`Z_j`$ | physical overlap/normalization |
| Visibility factor | $`D_{ab}`$ | surviving branch coherence |
| Basin measure | $`\mu(B_i)`$ | outcome-frequency weight |

</div>

The core relations are:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
``` math
\begin{equation}
  \lambda_\ast=c_XR^{-2},
\end{equation}
```
``` math
\begin{equation}
  \ell_{\rm coh}=\sqrt{\tau},
\end{equation}
```
``` math
\begin{equation}
  \Lambda_{\rm eff}=\tau^{-1/2},
\end{equation}
```
and
``` math
\begin{equation}
  W_j=\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

## What must be computed for numerical predictions

To turn the structural templates into numerical predictions, one must compute:

1.  the internal geometry $`X^6`$;

2.  the internal spectrum $`\mu_j^2`$;

3.  the coherent projector $`P_{\rm coh}`$;

4.  the admissibility window $`\chi`$;

5.  the gap $`\lambda_\ast`$;

6.  the tolerance $`\epsilon_{\rm adm}`$;

7.  wavefunction overlaps $`Z_j`$;

8.  effective gauge and matter couplings;

9.  resonance widths $`\Gamma_j`$;

10. gauge and gravitational quotient projectors;

11. anomaly and constraint consistency;

12. detector effects and basin measures.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT becomes numerically predictive only after the sectoral data are explicitly
  computed.}
  }
  \label{eq:appI-predictive-box}
\end{equation}
```

## Summary

The FP/MTT scale relations are:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
\end{equation}
```
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2},
\end{equation}
```
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  },
\end{equation}
```
and
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \tau^{-1/2}.
\end{equation}
```

Internal modes carry weights:
``` math
\begin{equation}
  W_j=\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

Zero modes are undamped:
``` math
\begin{equation}
  \mu_0=0
  \quad\Rightarrow\quad
  W_0=1.
\end{equation}
```

Nonzero modes are suppressed:
``` math
\begin{equation}
  \mu_j^2>0
  \quad\Rightarrow\quad
  W_j<1.
\end{equation}
```

The generic four-dimensional effective response is:
``` math
\begin{equation}
  G_{\rm eff}(p)
  =
  \sum_{j\ge0}
  \frac{
    Z_j\chi(\mu_j^2)^2\mathrm e^{-\tau\mu_j^2}
  }
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```

Therefore:
``` math
\begin{equation}
  \boxed{
  \text{the phenomenology of MTT is controlled by zero-mode recovery, admissibility-weighted
  internal excitations, finite measurement damping, and sectoral quotient constraints.}
  }
\end{equation}
```

# Notation, glossary, and execution checklist

This appendix collects the central notation used throughout the paper and gives a compact execution checklist for applying the MTT finite coherent admissibility architecture to a specific physical sector.

The central object is:
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
  \label{eq:appJ-Badm}
\end{equation}
```

The main interpretive rule is:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility}
  \longrightarrow
  \text{projection shadows}
  \longrightarrow
  \text{effective physics}.
  }
  \label{eq:appJ-main-rule}
\end{equation}
```

## Core operator notation

The basic analytic data are:

<div class="center">

| Symbol | Meaning |
|:--:|:---|
| $`\mathcal H`$ | sectoral Hilbert space or physical state space |
| $`A`$ | nonnegative admissibility/stabilization operator |
| $`P`$ | coherent, physical, or constraint-compatible projector |
| $`\chi(A)`$ | bounded admissible spectral window |
| $`\tau`$ | finite damping time or coherence scale parameter |
| $`B_{\rm adm}`$ | finite coherent admissibility operator |
| $`K_{\rm adm}(x,y)`$ | integral kernel of $`B_{\rm adm}`$, when it exists |

</div>

The clean spectral assumptions are:
``` math
\begin{equation}
  A\ge0,
  \qquad
  P=P^\ast=P^2,
  \qquad
  [P,A]=0,
  \qquad
  0\le\chi(A)\le I.
\end{equation}
```

Under these assumptions:
``` math
\begin{equation}
  0\le B_{\rm adm}\le I.
\end{equation}
```

If
``` math
\begin{equation}
  A\phi_n=\lambda_n\phi_n,
  \qquad
  P\phi_n=p_n\phi_n,
  \qquad
  p_n\in\{0,1\},
\end{equation}
```
then
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```

The modal weight is:
``` math
\begin{equation}
  w_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}.
  \label{eq:appJ-modal-weight}
\end{equation}
```

The full operator $`B_{\rm adm}`$ is generally not a projector:
``` math
\begin{equation}
  B_{\rm adm}^2\neq B_{\rm adm}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  P\text{ is the projector; }B_{\rm adm}\text{ is the finite coherent admissibility filter.}
  }
  \label{eq:appJ-projector-distinction}
\end{equation}
```

## Circle–Lens–Nil notation

The Modal Triplet notation is:
``` math
\begin{align}
  \mathsf C&: \text{phase, coherence, return, holonomy, spectral closure},\\
  \mathsf L&: \text{representation, quotient, projection, contextual reading},\\
  \mathsf N&: \text{damping, boundary, record, survivor selection}.
\end{align}
```

The main structural reading is:
``` math
\begin{equation}
  \boxed{
  \text{physical phenomena appear as }\mathsf C/\mathsf L/\mathsf N\text{ shadows of finite coherent
  admissibility.}
  }
\end{equation}
```

Examples:

<div class="center">

| Sector | $`\mathsf C`$ | $`\mathsf L`$ | $`\mathsf N`$ |
|:--:|:--:|:--:|:--:|
| Wave/particle | phase coherence | local/spectral reading | delta limit/record |
| Measurement | branch phase | detector basis/context | survivor basin |
| Gauge | holonomy/flux | gauge quotient | charge/photon record |
| Gravity | curvature holonomy | diffeomorphism quotient | boundary/horizon geometry |
| Quantization | phase closure | representation consistency | stable label |
| Entanglement | joint coherence | subsystem split | correlated record |

</div>

## Geometry notation

The fixed-point/fiber realization uses:
``` math
\begin{equation}
  M_{10}=Y^4\times X^6.
\end{equation}
```

Here:

<div class="center">

|      Symbol      | Meaning                                    |
|:----------------:|:-------------------------------------------|
|     $`Y^4`$      | four-dimensional Lorentzian base           |
|     $`X^6`$      | compact Riemannian internal space or fiber |
|   $`\Sigma_t`$   | Cauchy slice in $`Y^4`$                    |
|   $`z\in X^6`$   | internal coordinate                        |
|   $`x\in Y^4`$   | base coordinate                            |
|      $`R`$       | characteristic internal radius             |
| $`\lambda_\ast`$ | relevant internal spectral gap             |
|   $`\mu_j^2`$    | internal eigenvalue of $`A_{\rm int}`$     |

</div>

The internal admissibility operator is:
``` math
\begin{equation}
  A_{\rm int}
  =
  \sum_{n=1}^3
  \kappa_n\Delta_{B_n},
  \qquad
  A_{\rm int}\ge0.
\end{equation}
```

The coherent projector is:
``` math
\begin{equation}
  P_{\rm coh}
  =
  \Pi_{B_1}\Pi_{B_2}\Pi_{B_3},
\end{equation}
```
with:
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
\end{equation}
```

The FP finite coherent admissibility operator is:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}
  \chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})
  P_{\rm coh}.
  \label{eq:appJ-FP-Badm}
\end{equation}
```

## Scale notation

The main scale relations are:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}},
  \label{eq:appJ-tau}
\end{equation}
```
``` math
\begin{equation}
  \lambda_\ast\sim R^{-2},
  \label{eq:appJ-gap-radius}
\end{equation}
```
``` math
\begin{equation}
  \ell_{\rm coh}
  =
  \sqrt{\tau},
  \label{eq:appJ-lcoh}
\end{equation}
```
and
``` math
\begin{equation}
  \Lambda_{\rm eff}
  =
  \tau^{-1/2}.
  \label{eq:appJ-Lambda}
\end{equation}
```

Thus:
``` math
\begin{equation}
  \ell_{\rm coh}
  \sim
  R
  \sqrt{
    \log\frac{C_Q}{\epsilon_{\rm adm}}
  }.
\end{equation}
```

The internal-mode admissibility weight is:
``` math
\begin{equation}
  W_j
  =
  \mathrm e^{-\tau\mu_j^2}.
  \label{eq:appJ-Wj}
\end{equation}
```

Zero modes satisfy:
``` math
\begin{equation}
  \mu_0=0,
  \qquad
  W_0=1.
\end{equation}
```

Nonzero internal modes satisfy:
``` math
\begin{equation}
  \mu_j^2>0,
  \qquad
  W_j<1.
\end{equation}
```

## Kernel-shadow notation

When $`B_{\rm adm}`$ has a kernel,
``` math
\begin{equation}
  K_{\rm adm}(x,y)=\langle x|B_{\rm adm}|y\rangle.
\end{equation}
```

The two primary kernel shadows are:
``` math
\begin{align}
  \text{local reading}
  &: \quad
  x\mapsto K_{\rm adm}(x,x_0),
  \\
  \text{spectral reading}
  &: \quad
  K_{\rm adm}(x,y)
  =
  \sum_n
  w_n\phi_n(x)\phi_n^\ast(y).
\end{align}
```

The sharp limit is:
``` math
\begin{equation}
  K_{\rm adm}(x,y)\to\delta(x-y).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \delta(x-y)
  =
  \text{sharp local shadow of finite coherent admissibility}.
  }
\end{equation}
```

In the scalar Euclidean benchmark:
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right),
\end{equation}
```
with:
``` math
\begin{equation}
  \widehat K_\tau^{(d)}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```

## Measurement notation

A measurement context is:
``` math
\begin{equation}
  \mathsf M
  =
  (A_{\mathsf M},P_{\mathsf M},\chi_{\mathsf M},\tau_{\mathsf M},
  \{E_i^{(\mathsf M)}\},\mathfrak B_{\mathsf M}).
  \label{eq:appJ-measurement-context}
\end{equation}
```

Here:

<div class="center">

|           Symbol            | Meaning                              |
|:---------------------------:|:-------------------------------------|
|    $`E_i^{(\mathsf M)}`$    | finite detector effect               |
| $`\mathfrak B_{\mathsf M}`$ | measurement survivor-basin partition |
|    $`B_i^{(\mathsf M)}`$    | survivor basin for record $`i`$      |
|  $`D_{ab}^{(\mathsf M)}`$   | branch damping matrix                |
| $`\mu(B_i^{(\mathsf M)})`$  | basin measure of outcome $`i`$       |

</div>

Branch damping is:
``` math
\begin{equation}
  \rho\mapsto D\circ\rho,
\end{equation}
```
with:
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1.
\end{equation}
```

Outcome probabilities are:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{
    \mu(B_i^{(\mathsf M)})
  }{
    \sum_j\mu(B_j^{(\mathsf M)})
  }.
\end{equation}
```

The key distinction is:
``` math
\begin{equation}
  \boxed{
  D_{ab}
  \text{ controls visibility; }
  \mu(B_i)
  \text{ controls outcome frequencies.}
  }
\end{equation}
```

## Gauge notation

Gauge equivalence is:
``` math
\begin{equation}
  A_\mu\sim A_\mu+\partial_\mu\alpha.
\end{equation}
```

The gauge-sector finite coherent admissibility operator is:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}
  \chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})
  P_{\rm phys}.
  \label{eq:appJ-gauge-Badm}
\end{equation}
```

Here:

<div class="center">

|       Symbol       | Meaning                                         |
|:------------------:|:------------------------------------------------|
|  $`P_{\rm phys}`$  | projection to physical gauge content            |
| $`A_{\rm gauge}`$  | positive or gauge-compatible operator           |
|  $`Q_{\rm BRST}`$  | BRST operator                                   |
|      $`P_T`$       | transverse projector in simple Abelian settings |
|   $`F_{\mu\nu}`$   | gauge-invariant field strength                  |
| $`\oint_\gamma A`$ | gauge holonomy around loop $`\gamma`$           |

</div>

The safe rule is:
``` math
\begin{equation}
  \boxed{
  \text{filter after quotienting, or filter covariantly before quotienting.}
  }
\end{equation}
```

## Gravity notation

Diffeomorphism equivalence is:
``` math
\begin{equation}
  g_{\mu\nu}\sim\varphi^\ast g_{\mu\nu}.
\end{equation}
```

The gravitational finite coherent admissibility operator is:
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}
  \chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})
  P_{\rm diff}.
  \label{eq:appJ-gravity-Badm}
\end{equation}
```

In ADM notation, the Cauchy data are:
``` math
\begin{equation}
  (h_{ij},\pi^{ij}),
\end{equation}
```
subject to:
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
\end{equation}
```

Here:

<div class="center">

| Symbol | Meaning |
|:--:|:---|
| $`P_{\rm diff}`$ | diffeomorphism-compatible projection/reduction |
| $`A_{\rm grav}`$ | positive or constraint-compatible geometric operator |
| $`P_{\rm TT}`$ | transverse-traceless projector in weak-field gravity |
| $`\mathcal H`$ | Hamiltonian constraint |
| $`\mathcal H_i`$ | momentum constraints |
| $`R^\rho{}_{\sigma\mu\nu}`$ | curvature tensor / infinitesimal holonomy |

</div>

The safe rule is:
``` math
\begin{equation}
  \boxed{
  \text{filter geometric content, not coordinate artifacts.}
  }
\end{equation}
```

## Entanglement notation

For a joint sector:
``` math
\begin{equation}
  \mathcal H_{AB}
  =
  \mathcal H_A\otimes\mathcal H_B
\end{equation}
```
when the tensor product factorization is valid.

The joint finite coherent admissibility operator is:
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  =
  P_{AB}
  \chi(A_{AB})
  \mathrm e^{-\tau A_{AB}}
  \chi(A_{AB})
  P_{AB}.
  \label{eq:appJ-joint-Badm}
\end{equation}
```

Entanglement is signaled structurally by:
``` math
\begin{equation}
  P_{AB}\neq P_A\otimes P_B,
\end{equation}
```
or:
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  \neq
  B_{\rm adm}^{A}\otimes B_{\rm adm}^{B}.
\end{equation}
```

No-signaling requires:
``` math
\begin{equation}
  \sum_b p(a,b|x,y)
  =
  \sum_b p(a,b|x,y')
\end{equation}
```
and:
``` math
\begin{equation}
  \sum_a p(a,b|x,y)
  =
  \sum_a p(a,b|x',y).
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{joint coherence may be non-factorizing, but local record statistics must obey
  no-signaling.}
  }
\end{equation}
```

## Core theorem dependency map

The paper’s mathematical dependencies are:

1.  spectral theorem for nonnegative self-adjoint $`A`$;

2.  positivity and boundedness of $`\mathrm e^{-\tau A}`$;

3.  finite-filter theorem for $`B_{\rm adm}`$;

4.  distributional delta limit for approximate identities;

5.  scalar heat-kernel benchmark;

6.  Schur product theorem for branch damping;

7.  Schoenberg admissibility for exponential damping;

8.  Cauchy-slice boundedness and principal-symbol preservation;

9.  gauge quotient compatibility;

10. gravitational constraint compatibility;

11. compact-fiber spectral discreteness;

12. dimensional reduction into zero modes and damped internal towers.

In compact form:
``` math
\begin{equation}
  \boxed{
  \text{spectral positivity}
  +
  \text{finite kernels}
  +
  \text{quotient compatibility}
  +
  \text{Lorentzian admissibility}
  =
  \text{MTT structural unification}.
  }
\end{equation}
```

## Sectoral execution checklist

To apply MTT to a concrete sector, one must provide the following data.

#### Step 1: Choose the state space.

Specify:
``` math
\begin{equation}
  \mathcal H_{\rm sector}.
\end{equation}
```
For gauge and gravity sectors, specify the physical quotient or constraint-compatible state space.

#### Step 2: Choose the admissibility operator.

Specify:
``` math
\begin{equation}
  A_{\rm sector}.
\end{equation}
```
Check:
``` math
\begin{equation}
  A_{\rm sector}\ge0
\end{equation}
```
or positivity after projection/reduction.

#### Step 3: Choose the projector.

Specify:
``` math
\begin{equation}
  P_{\rm sector}.
\end{equation}
```
Check:
``` math
\begin{equation}
  P_{\rm sector}=P_{\rm sector}^\ast=P_{\rm sector}^2.
\end{equation}
```

#### Step 4: Check commutation.

Determine whether:
``` math
\begin{equation}
  [P_{\rm sector},A_{\rm sector}]=0.
\end{equation}
```
If yes, modal weights may be used. If no, operator-level estimates are required.

#### Step 5: Choose the window.

Specify:
``` math
\begin{equation}
  \chi(A_{\rm sector}).
\end{equation}
```
Check:
``` math
\begin{equation}
  0\le\chi(A_{\rm sector})\le I
\end{equation}
```
in the clean bounded case, and verify that required zero modes are retained.

#### Step 6: Choose or derive $`\tau`$.

Specify:
``` math
\begin{equation}
  \tau.
\end{equation}
```
In the FP realization:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
\end{equation}
```

#### Step 7: Construct the finite filter.

Build:
``` math
\begin{equation}
  B_{\rm adm}^{\rm sector}
  =
  P_{\rm sector}
  \chi(A_{\rm sector})
  \mathrm e^{-\tau A_{\rm sector}}
  \chi(A_{\rm sector})
  P_{\rm sector}.
\end{equation}
```

#### Step 8: Compute shadows.

Compute the relevant physical shadows:

1.  local kernel;

2.  spectral weights;

3.  effective propagator;

4.  finite source profile;

5.  detector effects;

6.  branch damping;

7.  gauge quotient response;

8.  geometric projection;

9.  measurement basins;

10. entanglement correlations.

#### Step 9: Check physical constraints.

Verify:

1.  positivity;

2.  unitarity or channel complete positivity;

3.  Lorentzian causal admissibility;

4.  gauge identities;

5.  gravitational constraints;

6.  no-signaling;

7.  low-energy recovery;

8.  experimental bounds.

#### Step 10: Extract predictions.

Only after Steps 1–9 are complete should one compute numerical predictions such as:

1.  masses;

2.  couplings;

3.  cross sections;

4.  precision corrections;

5.  visibility curves;

6.  basin probabilities;

7.  gravitational deviations;

8.  internal excitation bounds.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT prediction requires sectoral execution, not merely the formal presence of }
  B_{\rm adm}.
  }
  \label{eq:appJ-execution-box}
\end{equation}
```

## Minimal admissibility checklist

A proposed sectoral realization must satisfy:

1.  $`A\ge0`$ in the physical sector.

2.  $`P`$ is a valid projector.

3.  $`\chi(A)`$ is bounded and does not remove required zero modes.

4.  $`\tau`$ has a sectoral origin.

5.  $`B_{\rm adm}`$ is not mislabeled as a projector.

6.  If $`[P,A]\neq0`$, diagonal modal weights are not assumed without proof.

7.  Lorentzian damping is not implemented as naive $`\mathrm e^{-\tau\Box}`$.

8.  Gauge quotienting is preserved in gauge sectors.

9.  Diffeomorphism constraints are preserved in gravity.

10. Branch damping is CPTP in measurement sectors.

11. No-signaling is preserved in joint sectors.

12. Low-energy zero-mode recovery is maintained.

Failure of any required item invalidates that sectoral implementation.

## Claim-status checklist

The paper makes claims at three levels.

#### Analytic theorem.

These claims are mathematically proven under explicit assumptions:

1.  positivity and boundedness of $`B_{\rm adm}`$;

2.  scalar heat-kernel delta limit;

3.  Fourier damping in the scalar benchmark;

4.  Schur damping channel admissibility.

#### Structural corollary.

These claims organize known physical structures through MTT:

1.  wave and particle as kernel shadows;

2.  measurement as finite effects plus survivor basins;

3.  gauge as Lens quotient structure;

4.  gravity as diffeomorphism-compatible projection;

5.  quantization as survivor-label structure;

6.  entanglement as non-factorizing coherent admissibility.

#### Execution task.

These are not yet derived by the structural theorem alone:

1.  Standard Model representations;

2.  fermion generations;

3.  masses and couplings;

4.  full quantum gravity;

5.  exact collider signatures;

6.  complete Born-rule basin measure;

7.  numerical phenomenology.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{analytic theorem}
  \neq
  \text{structural unification}
  \neq
  \text{completed sectoral prediction}.
  }
  \label{eq:appJ-claim-status-box}
\end{equation}
```

## Recommended terminology

Use the following terminology consistently:

<div class="center">

| Preferred term | Avoid or qualify |
|:--:|:--:|
| finite coherent admissibility operator | projector for $`B_{\rm adm}`$ |
| admissible coherent filter | projection operator for $`B_{\rm adm}`$ |
| coherent projector $`P`$ | full filter $`B_{\rm adm}`$ as projector |
| fiber damping | Lorentzian $`\mathrm e^{-\tau\Box}`$ damping |
| Euclidean scalar benchmark | universal physical propagator |
| internal-mode weight | universal cross-section suppression |
| gauge-compatible filter | arbitrary damped gauge propagator |
| diffeomorphism-compatible filter | coordinate metric smoothing |
| survivor-basin selection | decoherence alone |
| structural unification | completed numerical prediction |

</div>

The most important terminology rule is:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}
  \text{ is a finite coherent admissibility operator, not generally a projector.}
  }
\end{equation}
```

## Summary

The paper is organized around:
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```

In the fixed-point/fiber realization:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}
  \chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})
  P_{\rm coh}.
\end{equation}
```

The coherent sector is:
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
\end{equation}
```

The scale is:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
\end{equation}
```

The internal-mode weight is:
``` math
\begin{equation}
  W_j=\mathrm e^{-\tau\mu_j^2}.
\end{equation}
```

The physical shadows are:
``` math
\begin{align}
  \text{local kernel} &\Rightarrow \text{particle/delta shadow},\\
  \text{spectral kernel} &\Rightarrow \text{wave shadow},\\
  \text{finite detector effect} &\Rightarrow \text{measurement shadow},\\
  \text{Schur damping} &\Rightarrow \text{visibility shadow},\\
  \text{gauge quotient} &\Rightarrow \text{electromagnetic/gauge shadow},\\
  \text{diffeomorphism quotient} &\Rightarrow \text{gravitational shadow},\\
  \text{survivor labels} &\Rightarrow \text{quantization shadow},\\
  \text{non-factorizing joint sector} &\Rightarrow \text{entanglement shadow}.
\end{align}
```

The final operational rule is:
``` math
\begin{equation}
  \boxed{
  \text{derive }A,\;P,\;\chi,\;\tau
  \text{ in the sector, prove admissibility, then compute the shadows.}
  }
\end{equation}
```

# Claim audit and reviewer-response map

This appendix states, in compact form, what the paper claims, what it does not claim, and how the main possible objections are addressed. Its purpose is to prevent overreading of the structural unification result.

The central distinction is:
``` math
\begin{equation}
  \boxed{
  \text{analytic theorem}
  \neq
  \text{structural unification}
  \neq
  \text{completed sectoral prediction}.
  }
  \label{eq:appK-three-levels}
\end{equation}
```

The paper proves finite-filter, kernel, heat-kernel, and branch-channel statements under explicit assumptions. It then uses these statements to organize quantum, gauge, gravitational, measurement, and entanglement structures as projection shadows. It does not claim that every Standard Model parameter, gravitational observable, or detector probability has already been computed.

## Primary claim

The primary claim of the paper is:
``` math
\begin{equation}
  \boxed{
  \text{finite coherent admissibility is a common projection architecture behind particle,
  wave, measurement, gauge, gravity, quantization, and entanglement shadows.}
  }
  \label{eq:appK-primary-claim}
\end{equation}
```

The operator expressing this architecture is:
``` math
\begin{equation}
  B_{\rm adm}
  =
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```

In the fixed-point/fiber realization:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}
  \chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})
  P_{\rm coh}.
\end{equation}
```

The coherent sector is:
``` math
\begin{equation}
  \operatorname{Ran}P_{\rm coh}
  =
  \bigcap_{n=1}^3\ker\Delta_{B_n}.
\end{equation}
```

Thus the coherent sector has a concrete meaning: it is the joint fiber-harmonic sector.

## What is mathematically proven

The following claims are analytic claims proven under stated hypotheses.

#### Finite-filter theorem.

If $`A\ge0`$, $`P=P^\ast=P^2`$, $`[P,A]=0`$, and $`0\le\chi(A)\le I`$, then
``` math
\begin{equation}
  0\le
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P
  \le I.
\end{equation}
```

In a common eigenbasis:
``` math
\begin{equation}
  B_{\rm adm}\phi_n
  =
  p_n\chi(\lambda_n)^2\mathrm e^{-\tau\lambda_n}\phi_n.
\end{equation}
```

#### Delta-limit theorem.

For an approximate identity $`K_\tau(x,y)`$,
``` math
\begin{equation}
  K_\tau(x,y)\to\delta(x-y)
\end{equation}
```
distributionally as $`\tau\downarrow0`$.

#### Scalar benchmark theorem.

For $`A=-\Delta`$, $`P=I`$, and $`\chi=1`$ on $`\mathbb R^d`$,
``` math
\begin{equation}
  K_\tau^{(d)}(x-y)
  =
  (4\pi\tau)^{-d/2}
  \exp\left(
    -\frac{|x-y|^2}{4\tau}
  \right),
\end{equation}
```
with Fourier transform
``` math
\begin{equation}
  \widehat K_\tau^{(d)}(k)=\mathrm e^{-\tau k^2}.
\end{equation}
```

#### Schur-channel theorem.

If
``` math
\begin{equation}
  D\succeq0,
  \qquad
  D_{aa}=1,
\end{equation}
```
then
``` math
\begin{equation}
  \rho\mapsto D\circ\rho
\end{equation}
```
is a completely positive trace-preserving channel.

#### Lorentzian admissibility schema.

A bounded equal-time Cauchy-slice kernel that enters as a lower-order term does not change the hyperbolic principal symbol. Strict support-domain preservation, however, requires additional support control or a preparation/readout interpretation.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the paper's hard analytic claims are conditional and explicitly scoped.}
  }
  \label{eq:appK-analytic-scoped}
\end{equation}
```

## What is structurally argued

The following are structural interpretations supported by the analytic architecture.

#### Wave–particle duality.

The same kernel has a local and spectral reading:
``` math
\begin{equation}
  K_{\rm adm}(x,y)
  \quad
  \begin{cases}
    \text{local reading}
    &\Rightarrow
    \text{particle/delta shadow},\\
    \text{spectral reading}
    &\Rightarrow
    \text{wave/interference shadow}.
  \end{cases}
\end{equation}
```

#### Measurement.

Finite detector effects, branch damping, and survivor basins together produce measurement records:
``` math
\begin{equation}
  \rho
  \to
  D\circ\rho
  \to
  B_i^{(\mathsf M)}.
\end{equation}
```

#### Gauge theory.

Gauge theory is Lens quotient structure. Therefore:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
\end{equation}
```

#### Gravity.

Gravity is diffeomorphism-compatible geometric projection:
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
\end{equation}
```

#### Quantization.

Quantization is survivor-label discreteness generated by Circle closure, Lens consistency, and Nil selection:
``` math
\begin{equation}
  \text{quantization}
  =
  \mathsf C\text{-closure}
  +
  \mathsf L\text{-quotient consistency}
  +
  \mathsf N\text{-survivor selection}.
\end{equation}
```

#### Entanglement.

Entanglement is non-factorizing joint coherent admissibility:
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  \neq
  B_{\rm adm}^{A}\otimes B_{\rm adm}^{B}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{the structural claim is unification by projection architecture, not derivation of all
  numerical physics.}
  }
  \label{eq:appK-structural-scoped}
\end{equation}
```

## What is not yet claimed

The paper does not claim to have already derived:

1.  the full Standard Model gauge group from first principles;

2.  all Standard Model representations;

3.  three fermion generations;

4.  all masses and Yukawa couplings;

5.  CKM or PMNS mixing data;

6.  anomaly cancellation from the MTT operator alone;

7.  a full nonperturbative quantum-gravity Hilbert space;

8.  exact black-hole microphysics;

9.  all Born-rule basin measures;

10. exact collider cross sections;

11. exact numerical deviations in precision tests.

These are execution tasks.

The correct claim is:
``` math
\begin{equation}
  \boxed{
  \text{MTT specifies the admissibility architecture within which such sectoral derivations
  must be carried out.}
  }
  \label{eq:appK-execution-not-complete}
\end{equation}
```

## Response to the “just a regulator” objection

A possible objection is that
``` math
\begin{equation}
  \mathrm e^{-\tau A}
\end{equation}
```
looks like an ordinary regulator.

The response is that MTT does not use the exponential merely as a computational cutoff. The finite damping appears inside a larger architecture:
``` math
\begin{equation}
  P\chi(A)\mathrm e^{-\tau A}\chi(A)P.
\end{equation}
```
The projector $`P`$, the spectral window $`\chi`$, the gap-selected $`\tau`$, and the sectoral quotient constraints are all part of the physical content.

In the FP realization, $`\tau`$ is tied to the internal spectral gap:
``` math
\begin{equation}
  \tau
  =
  \lambda_\ast^{-1}
  \log\frac{C_Q}{\epsilon_{\rm adm}}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is not merely ``put in a regulator''; it is a finite admissibility architecture with
  projector, window, gap scale, and physical quotient constraints.}
  }
  \label{eq:appK-regulator-response}
\end{equation}
```

## Response to the “just Kaluza–Klein” objection

A possible objection is that the FP realization is just Kaluza–Klein theory.

The answer is that the FP realization is intentionally KK-compatible. The compact internal geometry supplies the positive spectrum:
``` math
\begin{equation}
  A_{\rm int}\phi_j=\mu_j^2\phi_j.
\end{equation}
```
Dimensional reduction gives a tower:
``` math
\begin{equation}
  G_{4D}(p)
  =
  \sum_{j\ge0}
  \frac{Z_j\mathrm e^{-\tau\mu_j^2}}
  {p^2-m_j^2+\mathrm i\epsilon}.
\end{equation}
```

The MTT addition is that the tower is embedded in a finite coherent projection architecture:
``` math
\begin{equation}
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{ordinary KK gives compactification towers; FP/MTT gives compactification towers
  filtered through finite coherent admissibility and interpreted as projection shadows.}
  }
  \label{eq:appK-KK-response}
\end{equation}
```

The KK backbone is not hidden. It is the geometric support of the framework.

## Response to the Lorentzian nonlocality objection

A possible objection is that exponential finite operators in Lorentzian field theory are often acausal or unstable.

MTT addresses this by rejecting the naive rule:
``` math
\begin{equation}
  A=\Box_g.
\end{equation}
```

The paper’s Lorentzian rule is:
``` math
\begin{equation}
  \boxed{
  A\neq\Box_g
  \quad
  \text{as a naive fundamental damping operator.}
  }
\end{equation}
```

Instead, admissible $`A`$’s are:

1.  positive internal/fiber operators;

2.  positive spatial Cauchy-slice operators;

3.  Hamiltonian or constraint-compatible operators;

4.  gauge-quotiented physical operators;

5.  diffeomorphism-compatible geometric operators.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is not a naive Lorentzian nonlocal theory based on }\mathrm e^{-\tau\Box_g}.
  }
  \label{eq:appK-Lorentzian-response}
\end{equation}
```

## Response to the causality objection

A possible objection is that finite kernels imply action at a distance.

The response is that finite support, finite detector resolution, or finite source width is not the same as controllable acausal signaling. A finite detector samples a region. A finite source has extent. A finite internal mode may project to a finite effective profile.

The strict causal requirements are:

1.  the Lorentzian principal symbol is not modified in an inadmissible way;

2.  no controllable signal can be transmitted outside the causal domain;

3.  globally supported dynamical kernels require additional support or no-signaling proof;

4.  preparation/readout kernels are distinguished from dynamical propagation kernels.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{finite overlap is not acausal signaling; controllable domain-of-dependence violation
  would be inadmissible.}
  }
  \label{eq:appK-causality-response}
\end{equation}
```

## Response to the gauge objection

A possible objection is that finite filters can break gauge invariance.

MTT agrees and makes this a failure mode. The gauge-sector filter must be:
``` math
\begin{equation}
  B_{\rm adm}^{\rm gauge}
  =
  P_{\rm phys}\chi(A_{\rm gauge})
  \mathrm e^{-\tau A_{\rm gauge}}
  \chi(A_{\rm gauge})P_{\rm phys}.
\end{equation}
```

The safe rule is:
``` math
\begin{equation}
  \text{filter after quotienting, or filter covariantly before quotienting}.
\end{equation}
```

The filter must preserve:

1.  gauge quotienting;

2.  Ward identities;

3.  Slavnov–Taylor identities;

4.  BRST cohomology where relevant;

5.  current conservation;

6.  anomaly cancellation;

7.  global bundle and flux consistency.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{a gauge-breaking finite filter is not an admissible MTT gauge object.}
  }
  \label{eq:appK-gauge-response}
\end{equation}
```

## Response to the gravity objection

A possible objection is that finite filtering of the metric is coordinate-dependent and violates diffeomorphism invariance.

MTT agrees that coordinate-component smoothing is invalid. The gravitational filter must be:
``` math
\begin{equation}
  B_{\rm adm}^{\rm grav}
  =
  P_{\rm diff}\chi(A_{\rm grav})
  \mathrm e^{-\tau A_{\rm grav}}
  \chi(A_{\rm grav})P_{\rm diff}.
\end{equation}
```

It must act on diffeomorphism-compatible geometric content, not arbitrary metric components.

In ADM language, it must preserve:
``` math
\begin{equation}
  \mathcal H=0,
  \qquad
  \mathcal H_i=0.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{coordinate smoothing of }g_{\mu\nu}\text{ is not MTT gravity; constraint-compatible
  geometric projection is.}
  }
  \label{eq:appK-gravity-response}
\end{equation}
```

## Response to the measurement objection

A possible objection is that decoherence does not solve the measurement problem.

MTT agrees. The paper distinguishes:
``` math
\begin{equation}
  \text{branch damping}
\end{equation}
```
from
``` math
\begin{equation}
  \text{survivor-basin record selection}.
\end{equation}
```

Branch damping is:
``` math
\begin{equation}
  \rho\mapsto D\circ\rho.
\end{equation}
```

Record formation is:
``` math
\begin{equation}
  \Psi\to B_i^{(\mathsf M)}.
\end{equation}
```

Outcome frequencies require a basin measure:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \frac{\mu(B_i^{(\mathsf M)})}
  {\sum_j\mu(B_j^{(\mathsf M)})}.
\end{equation}
```

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT does not identify decoherence alone with outcome selection.}
  }
  \label{eq:appK-measurement-response}
\end{equation}
```

## Response to the Born-rule objection

A possible objection is that the paper has not derived the Born rule.

The correct response is that the paper identifies where the Born rule must enter in the MTT architecture: it must be a statement about basin measures:
``` math
\begin{equation}
  \mu(B_i^{(\mathsf M)}).
\end{equation}
```

The Born-form recovery condition is:
``` math
\begin{equation}
  \mathbb P(i)
  =
  \operatorname{tr}(\rho E_i).
\end{equation}
```

Thus the open task is:
``` math
\begin{equation}
  \boxed{
  \text{derive conditions under which survivor-basin measures reproduce the quantum trace
  rule.}
  }
  \label{eq:appK-Born-response}
\end{equation}
```

The paper does not overclaim that this has been completed in all detector contexts.

## Response to the entanglement objection

A possible objection is that MTT might be a hidden-variable theory and conflict with Bell experiments.

MTT is not a local hidden-variable theory. It does not assume pre-existing local survivor labels for all possible measurement settings.

The MTT statement is:
``` math
\begin{equation}
  \text{joint coherent admissibility}
  \neq
  \text{pre-existing distribution over local records}.
\end{equation}
```

Entanglement is:
``` math
\begin{equation}
  B_{\rm adm}^{AB}
  \neq
  B_{\rm adm}^{A}\otimes B_{\rm adm}^{B}.
\end{equation}
```

Admissibility still requires no-signaling:
``` math
\begin{equation}
  \sum_b p(a,b|x,y)
  =
  \sum_b p(a,b|x,y'),
\end{equation}
```
and similarly for Bob.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT permits non-factorizing joint coherence but requires no-signaling record
  statistics.}
  }
  \label{eq:appK-entanglement-response}
\end{equation}
```

## Response to the predictivity objection

A possible objection is that the framework is structural but not yet fully predictive.

The response is that the paper distinguishes three levels:

1.  structural predictions;

2.  model templates;

3.  numerical predictions.

The structural predictions include:

1.  zero modes are undamped by internal admissibility;

2.  nonzero internal modes are suppressed by $`\mathrm e^{-\tau\mu_j^2}`$;

3.  $`\tau`$ is tied to the internal spectral gap;

4.  gauge filters must preserve quotient identities;

5.  gravity filters must preserve diffeomorphism constraints;

6.  branch damping must be CPTP.

Numerical predictions require:

1.  internal geometry;

2.  spectra;

3.  overlap integrals;

4.  couplings;

5.  widths;

6.  detector acceptances;

7.  basin measures.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT is predictive only after sectoral execution; this paper supplies the execution
  architecture and structural constraints.}
  }
  \label{eq:appK-predictivity-response}
\end{equation}
```

## Response to the over-unification objection

A possible objection is that claiming to unify wave, particle, gauge, gravity, quantization, and entanglement sounds too broad.

The correct interpretation is not that all equations of physics have been derived from one line. The claim is that these phenomena can be organized as different projection shadows of one finite coherent admissibility architecture.

The unification is structural:
``` math
\begin{equation}
  \boxed{
  \text{different physical phenomena share the same projection grammar.}
  }
  \label{eq:appK-structural-unification}
\end{equation}
```

It is not yet a complete numerical reduction of all phenomena to one computed model.

Thus:
``` math
\begin{equation}
  \boxed{
  \text{MTT unifies the architecture of admissibility and projection, while sectoral physics
  still requires execution.}
  }
  \label{eq:appK-over-unification-response}
\end{equation}
```

## Reviewer-facing summary

A concise reviewer-facing summary is:

> MTT does not postulate a naive Lorentzian nonlocal operator. Its finite coherent filter is defined through positive or physically reduced sectoral operators. In the fixed-point realization, the damping is internal/fiber elliptic, not Lorentzian $`\Box`$-damping. The framework is KK-compatible: compact internal spectra generate zero modes and excitation towers. The MTT contribution is the finite coherent projection architecture that interprets delta localization, wave interference, measurement records, gauge quotienting, gravity, quantization, and entanglement as projection shadows. The analytic theorems are conditional and explicit; Standard Model closure, quantum gravity, Born-rule basin measures, and numerical phenomenology remain sectoral execution tasks.

In formula form:
``` math
\begin{equation}
  \boxed{
  B_{\rm adm}^{\rm FP}
  =
  P_{\rm coh}\chi(A_{\rm int})
  \mathrm e^{-\tau A_{\rm int}}
  \chi(A_{\rm int})P_{\rm coh},
  \qquad
  A_{\rm int}\ge0,
  \qquad
  A\neq\Box_g.
  }
  \label{eq:appK-reviewer-formula}
\end{equation}
```

## Final claim-audit table

<div class="center">

| Topic | Claimed | Not claimed |
|:---|:---|:---|
| Finite filter | Positive contraction under stated assumptions | Projector for arbitrary data |
| Dirac delta | Sharp limit of finite kernels | Fundamental physical point object |
| Wave behavior | Spectral shadow of same kernel | Separate wave substance |
| Lorentzian physics | Positive sectoral damping, not $`\Box`$-heat flow | Naive $`\mathrm e^{-\tau\Box}`$ theory |
| KK structure | Explicitly acknowledged FP backbone | Denial of compactification role |
| Gauge | Quotient-compatible filtering | Arbitrary damped gauge propagator |
| Gravity | Constraint-compatible geometric projection | Completed nonperturbative QG |
| Measurement | Damping plus survivor basins | Decoherence alone solves outcomes |
| Born rule | Basin-measure execution target | Fully derived in all contexts |
| Entanglement | Non-factorizing joint coherence with no-signaling | Local hidden-variable model |
| Phenomenology | Structural templates and scale relations | Complete numerical predictions |

</div>

## Summary

The paper’s safe final claim is:
``` math
\begin{equation}
  \boxed{
  \text{MTT provides a finite coherent admissibility architecture whose projection shadows
  organize particle, wave, measurement, gauge, gravity, quantization, and entanglement
  structures.}
  }
\end{equation}
```

The paper’s safe limitation is:
``` math
\begin{equation}
  \boxed{
  \text{the architecture becomes numerically predictive only after sectoral execution of }
  A,\;P,\;\chi,\;\tau,\text{ quotient data, and basin measures.}
  }
\end{equation}
```

This is the intended level of the synthesis paper.

<div class="thebibliography">

99 <span id="sec:bibliography" label="sec:bibliography"></span>

<span class="smallcaps">Author</span>, *Modal Triplet Theory: Core and Encodings*, manuscript.

<span class="smallcaps">Author</span>, *Fixed Points and Coherent Projection in Modal Triplet Theory*, manuscript series.

<span class="smallcaps">Author</span>, *Fixed-Point Fiber Geometry and Internal Coherent Modes*, manuscript.

<span class="smallcaps">Author</span>, *Lorentzian Admissibility, Cauchy Kernels, and Finite Coherent Projection*, manuscript.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators*, Academic Press, 1978.

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

N. Dunford and J. T. Schwartz, *Linear Operators, Part II: Spectral Theory*, Wiley, 1988.

J. B. Conway, *A Course in Functional Analysis*, Springer, 1990.

R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, American Mathematical Society, 1997.

R. A. Horn and C. R. Johnson, *Matrix Analysis*, Cambridge University Press, 2012.

E. B. Davies, *Heat Kernels and Spectral Theory*, Cambridge University Press, 1989.

P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, CRC Press, 1995.

N. Berline, E. Getzler, and M. Vergne, *Heat Kernels and Dirac Operators*, Springer, 2004.

A. Grigor’yan, *Heat Kernel and Analysis on Manifolds*, American Mathematical Society, 2009.

I. Chavel, *Eigenvalues in Riemannian Geometry*, Academic Press, 1984.

S. Rosenberg, *The Laplacian on a Riemannian Manifold*, Cambridge University Press, 1997.

R. T. Seeley, “Complex powers of an elliptic operator,” *Proceedings of Symposia in Pure Mathematics* **10** (1967), 288–307.

B. S. DeWitt, *Dynamical Theory of Groups and Fields*, Gordon and Breach, 1965.

S. Minakshisundaram and Å. Pleijel, “Some properties of the eigenfunctions of the Laplace-operator on Riemannian manifolds,” *Canadian Journal of Mathematics* **1** (1949), 242–256.

L. C. Evans, *Partial Differential Equations*, American Mathematical Society, 2010.

L. Hörmander, *The Analysis of Linear Partial Differential Operators III*, Springer, 1985.

M. E. Taylor, *Partial Differential Equations II: Qualitative Studies of Linear Equations*, Springer, 2011.

H. Ringström, *The Cauchy Problem in General Relativity*, European Mathematical Society, 2009.

C. Bär, N. Ginoux, and F. Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007.

F. G. Friedlander, *The Wave Equation on a Curved Space-Time*, Cambridge University Press, 1975.

J. von Neumann, *Mathematical Foundations of Quantum Mechanics*, Princeton University Press, 1955.

P. A. M. Dirac, *The Principles of Quantum Mechanics*, Oxford University Press, 1958.

J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, Cambridge University Press, 2020.

M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2010.

A. S. Holevo, *Probabilistic and Statistical Aspects of Quantum Theory*, North-Holland, 1982.

E. B. Davies, *Quantum Theory of Open Systems*, Academic Press, 1976.

K. Kraus, *States, Effects, and Operations*, Springer, 1983.

M.-D. Choi, “Completely positive linear maps on complex matrices,” *Linear Algebra and its Applications* **10** (1975), 285–290.

G. Lindblad, “On the generators of quantum dynamical semigroups,” *Communications in Mathematical Physics* **48** (1976), 119–130.

V. Gorini, A. Kossakowski, and E. C. G. Sudarshan, “Completely positive dynamical semigroups of N-level systems,” *Journal of Mathematical Physics* **17** (1976), 821–825.

H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press, 2002.

M. Schlosshauer, *Decoherence and the Quantum-to-Classical Transition*, Springer, 2007.

W. H. Zurek, “Decoherence, einselection, and the quantum origins of the classical,” *Reviews of Modern Physics* **75** (2003), 715–775.

E. Joos and H. D. Zeh, “The emergence of classical properties through interaction with the environment,” *Zeitschrift für Physik B* **59** (1985), 223–243.

R. B. Griffiths, *Consistent Quantum Theory*, Cambridge University Press, 2002.

R. Omnès, *The Interpretation of Quantum Mechanics*, Princeton University Press, 1994.

I. J. Schoenberg, “Metric spaces and positive definite functions,” *Transactions of the American Mathematical Society* **44** (1938), 522–536.

J. S. Bell, “On the Einstein Podolsky Rosen paradox,” *Physics Physique Fizika* **1** (1964), 195–200.

J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, “Proposed experiment to test local hidden-variable theories,” *Physical Review Letters* **23** (1969), 880–884.

A. Aspect, P. Grangier, and G. Roger, “Experimental realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment: A new violation of Bell’s inequalities,” *Physical Review Letters* **49** (1982), 91–94.

R. Horodecki, P. Horodecki, M. Horodecki, and K. Horodecki, “Quantum entanglement,” *Reviews of Modern Physics* **81** (2009), 865–942.

S. Weinberg, *The Quantum Theory of Fields, Volume I: Foundations*, Cambridge University Press, 1995.

S. Weinberg, *The Quantum Theory of Fields, Volume II: Modern Applications*, Cambridge University Press, 1996.

M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press, 1995.

M. Srednicki, *Quantum Field Theory*, Cambridge University Press, 2007.

R. Haag, *Local Quantum Physics*, Springer, 1996.

R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That*, Princeton University Press, 2000.

G. Källén, “On the definition of the renormalization constants in quantum electrodynamics,” *Helvetica Physica Acta* **25** (1952), 417–434.

H. Lehmann, “Über Eigenschaften von Ausbreitungsfunktionen und Renormierungskonstanten quantisierter Felder,” *Il Nuovo Cimento* **11** (1954), 342–357.

N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields*, Wiley, 1980.

J. Polchinski, “Renormalization and effective Lagrangians,” *Nuclear Physics B* **231** (1984), 269–295.

K. G. Wilson and J. Kogut, “The renormalization group and the epsilon expansion,” *Physics Reports* **12** (1974), 75–199.

C. N. Yang and R. L. Mills, “Conservation of isotopic spin and isotopic gauge invariance,” *Physical Review* **96** (1954), 191–195.

L. D. Faddeev and V. N. Popov, “Feynman diagrams for the Yang–Mills field,” *Physics Letters B* **25** (1967), 29–30.

C. Becchi, A. Rouet, and R. Stora, “Renormalization of gauge theories,” *Annals of Physics* **98** (1976), 287–321.

I. V. Tyutin, “Gauge invariance in field theory and statistical physics in operator formalism,” Lebedev Institute preprint, 1975.

M. Henneaux and C. Teitelboim, *Quantization of Gauge Systems*, Princeton University Press, 1992.

A. A. Slavnov, “Ward identities in gauge theories,” *Theoretical and Mathematical Physics* **10** (1972), 99–104.

J. C. Taylor, “Ward identities and charge renormalization of the Yang–Mills field,” *Nuclear Physics B* **33** (1971), 436–444.

J. C. Ward, “An identity in quantum electrodynamics,” *Physical Review* **78** (1950), 182.

Y. Takahashi, “On the generalized Ward identity,” *Il Nuovo Cimento* **6** (1957), 371–375.

S. L. Adler, “Axial-vector vertex in spinor electrodynamics,” *Physical Review* **177** (1969), 2426–2438.

J. S. Bell and R. Jackiw, “A PCAC puzzle: $`\pi^0\to\gamma\gamma`$ in the sigma model,” *Il Nuovo Cimento A* **60** (1969), 47–61.

M. Nakahara, *Geometry, Topology and Physics*, CRC Press, 2003.

D. Bleecker, *Gauge Theory and Variational Principles*, Dover, 2005.

R. M. Wald, *General Relativity*, University of Chicago Press, 1984.

S. W. Hawking and G. F. R. Ellis, *The Large Scale Structure of Space-Time*, Cambridge University Press, 1973.

C. W. Misner, K. S. Thorne, and J. A. Wheeler, *Gravitation*, W. H. Freeman, 1973.

Y. Choquet-Bruhat, *General Relativity and the Einstein Equations*, Oxford University Press, 2009.

R. Arnowitt, S. Deser, and C. W. Misner, “The dynamics of general relativity,” in L. Witten, ed., *Gravitation: An Introduction to Current Research*, Wiley, 1962.

P. A. M. Dirac, *Lectures on Quantum Mechanics*, Yeshiva University, 1964.

B. S. DeWitt, “Quantum theory of gravity. I. The canonical theory,” *Physical Review* **160** (1967), 1113–1148.

R. Geroch, “Domain of dependence,” *Journal of Mathematical Physics* **11** (1970), 437–449.

R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*, University of Chicago Press, 1994.

T. Kaluza, “Zum Unitätsproblem der Physik,” *Sitzungsberichte der Preussischen Akademie der Wissenschaften* (1921), 966–972.

O. Klein, “Quantum theory and five-dimensional theory of relativity,” *Zeitschrift für Physik* **37** (1926), 895–906.

T. Appelquist, A. Chodos, and P. G. O. Freund, eds., *Modern Kaluza–Klein Theories*, Addison-Wesley, 1987.

J. M. Overduin and P. S. Wesson, “Kaluza–Klein gravity,” *Physics Reports* **283** (1997), 303–378.

M. J. Duff, B. E. W. Nilsson, and C. N. Pope, “Kaluza–Klein supergravity,” *Physics Reports* **130** (1986), 1–142.

L. Randall and R. Sundrum, “A large mass hierarchy from a small extra dimension,” *Physical Review Letters* **83** (1999), 3370–3373.

L. Randall and R. Sundrum, “An alternative to compactification,” *Physical Review Letters* **83** (1999), 4690–4693.

N. Arkani-Hamed, S. Dimopoulos, and G. Dvali, “The hierarchy problem and new dimensions at a millimeter,” *Physics Letters B* **429** (1998), 263–272.

J. Polchinski, *String Theory, Volume I: An Introduction to the Bosonic String*, Cambridge University Press, 1998.

J. Polchinski, *String Theory, Volume II: Superstring Theory and Beyond*, Cambridge University Press, 1998.

M. B. Green, J. H. Schwarz, and E. Witten, *Superstring Theory, Volume I*, Cambridge University Press, 1987.

M. B. Green, J. H. Schwarz, and E. Witten, *Superstring Theory, Volume II*, Cambridge University Press, 1987.

K. Becker, M. Becker, and J. H. Schwarz, *String Theory and M-Theory: A Modern Introduction*, Cambridge University Press, 2007.

J. M. Maldacena, “The large $`N`$ limit of superconformal field theories and supergravity,” *Advances in Theoretical and Mathematical Physics* **2** (1998), 231–252.

S. S. Gubser, I. R. Klebanov, and A. M. Polyakov, “Gauge theory correlators from non-critical string theory,” *Physics Letters B* **428** (1998), 105–114.

E. Witten, “Anti de Sitter space and holography,” *Advances in Theoretical and Mathematical Physics* **2** (1998), 253–291.

A. Ashtekar, “New variables for classical and quantum gravity,” *Physical Review Letters* **57** (1986), 2244–2247.

C. Rovelli, *Quantum Gravity*, Cambridge University Press, 2004.

T. Thiemann, *Modern Canonical Quantum General Relativity*, Cambridge University Press, 2007.

A. Ashtekar and J. Lewandowski, “Background independent quantum gravity: A status report,” *Classical and Quantum Gravity* **21** (2004), R53–R152.

A. Perez, “The spin-foam approach to quantum gravity,” *Living Reviews in Relativity* **16** (2013), 3.

R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.

J. Milnor and J. D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974.

A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.

T. Frankel, *The Geometry of Physics*, Cambridge University Press, 2011.

T. Eguchi, P. B. Gilkey, and A. J. Hanson, “Gravitation, gauge theories and differential geometry,” *Physics Reports* **66** (1980), 213–393.

</div>
