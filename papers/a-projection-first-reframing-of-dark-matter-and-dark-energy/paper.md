---
abstract: |
  Dark matter and dark energy are names for distinct empirical requirements, not merely for missing microscopic descriptions. A projection-first framework may suggest that unresolved source data appear as effective gravitational terms, but this suggestion becomes physical only after it produces covariant field equations and observables. This paper formulates that requirement for Modal Triplet Theory. A dark-matter realization must reproduce gravitational lensing, approximately pressureless clustering, structure growth, cosmic microwave background effects, and cluster dynamics. A dark-energy realization must produce the observed expansion history and perturbation behavior while remaining stable and compatible with local gravity. Both require a selected effective stress tensor or an explicit modified-gravity operator satisfying the Bianchi identity. “Constraint load” and “capacity exhaustion” are therefore retained as hypothesis labels, not established explanations. No current MTT result derives the required dark-sector source, halo solutions, or cosmological likelihoods.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: fb5a45ba3edf3795aa81d5d323a708f9cd546f88fef34d97c14b2e80615cb8da
paper_id: a-projection-first-reframing-of-dark-matter-and-dark-energy
release_state: zenodo_released
released_version: v2
title: |
  Projection-First Dark-Sector Diagnostics:
  Effective Stress, Lensing, and Cosmological Closure
zenodo_doi: 10.5281/zenodo.21665929
zenodo_record_id: 21665929
zenodo_url: "https://zenodo.org/records/21665929"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *A Projection-First Reframing of Dark Matter and Dark Energy*.

The original paper identified failed particle encoding with dark matter and global capacity exhaustion with dark energy without deriving the stress-energy, field equations, perturbations, or observables needed for those identifications.

The two proposals are recast as falsifiable hypotheses. Necessary covariant source equations, cold-matter limits, lensing tests, acceleration conditions, stability gates, and data comparisons are stated explicitly.

Projection-first reasoning can motivate a search for effective gravitational sources that need not be new elementary particles.

MTT has not selected a dark-sector action or effective tensor and has not reproduced halo, lensing, CMB, growth, BAO, or supernova likelihoods.

</div>

# The empirical problem

Dark matter and dark energy are inferred from different classes of observations. Dark-matter phenomenology includes galaxy and cluster dynamics, gravitational lensing, structure formation, and signatures in the cosmic microwave background. Dark-energy phenomenology concerns the late-time expansion history and the behavior of cosmological perturbations. The spatial separation between lensing mass and collisional gas in merging clusters is an especially important constraint on any account of gravitating mass . Precision cosmology is well described by a $`\Lambda`$CDM baseline, although time-dependent dark-energy models remain actively tested .

These observations do not require that dark matter be an elementary particle or that dark energy be a literal fluid. They do require a theory to produce the same gravitational observables. A semantic replacement of “dark component” by “projection strain” is not enough.

# The covariant closure requirement

In an Einstein-form description one may write
``` math
G_{\mu\nu}+\Lambda g_{\mu\nu}
 =8\pi G\left(T^{\rm vis}_{\mu\nu}
              +T^{\rm eff}_{\mu\nu}\right).
```
The Bianchi identity gives
``` math
\nabla^\mu G_{\mu\nu}=0.
```
If visible matter is separately conserved, then consistency requires
``` math
\nabla^\mu T^{\rm eff}_{\mu\nu}=0.
```
An exchange law is possible, but it must be specified:
``` math
\nabla^\mu T^{\rm vis}_{\mu\nu}=Q_\nu,
 \qquad
 \nabla^\mu T^{\rm eff}_{\mu\nu}=-Q_\nu.
```

A modified-gravity description can instead use
``` math
\mathcal E_{\mu\nu}[g,\chi]
 =8\pi G T^{\rm vis}_{\mu\nu},
```
where $`\chi`$ denotes additional geometric or projected variables. Moving terms between the two sides can define an effective tensor, but it does not remove the need for a covariant identity, initial data, stability, and observables.

For MTT, the missing central object is consequently one of:
``` math
S_{\rm selected}[g,\chi]
 \quad\Longrightarrow\quad
 T^{\rm eff}_{\mu\nu}
 =-\frac{2}{\sqrt{-g}}
   \frac{\delta S_{\rm selected}}{\delta g^{\mu\nu}},
```
or a selected covariant operator $`\mathcal E_{\mu\nu}`$ with an equivalent closure identity. A scalar “closure cost” is not a substitute for this tensor.

# Dark matter: required behavior

## Background and perturbations

At homogeneous level, cold dark matter is approximately pressureless:
``` math
p_{\rm dm}\simeq0,
 \qquad
 \rho_{\rm dm}\propto a^{-3}.
```
At perturbative level, a proposed source must supply sufficiently small effective sound speed and controlled anisotropic stress so that it clusters on the observed scales. It must participate in the metric potentials that govern both motion and lensing.

In a scalar-perturbed cosmology,
``` math
ds^2=-(1+2\Psi)dt^2
 +a(t)^2(1-2\Phi)d\mathbf x^2,
```
nonrelativistic motion primarily probes $`\Psi`$, while lensing probes combinations of $`\Phi`$ and $`\Psi`$. Reproducing one rotation curve does not establish the required lensing relation or cosmological growth law.

## Minimum dark-matter test set

An MTT dark-matter candidate must provide:

1.  a covariant background solution and a positive effective density;

2.  linear scalar, vector, and tensor perturbation equations;

3.  galaxy and cluster lensing from the same metric that governs motion;

4.  halo or alternative nonlinear solutions;

5.  a matter power spectrum and CMB transfer functions;

6.  merging-cluster behavior and bounds on dissipation or self-interaction;

7.  compatibility with solar-system and binary-pulsar tests; and

8.  a parameter ledger and likelihood comparison with $`\Lambda`$CDM.

The phrase “constraint load without particle encoding” is compatible with either an effective source or modified gravity. It does not imply that the source is cold, collisionless, stable, or correctly distributed. Those are outputs to be calculated.

# Dark energy: required behavior

## Acceleration

For a spatially homogeneous Einstein cosmology,
``` math
\frac{\ddot a}{a}
 =-\frac{4\pi G}{3}\left(\rho+3p\right).
```
Acceleration requires
``` math
\rho+3p<0
```
for the effective total source in this formulation. A cosmological constant has $`p_\Lambda=-\rho_\Lambda`$. More general dark energy is often described by $`w(a)=p/\rho`$, but a background $`w(a)`$ alone is insufficient. One must also specify perturbations, sound speed, anisotropic stress, and interactions.

The original “capacity exhaustion” language does not determine $`\rho(a)`$, $`p(a)`$, or $`w(a)`$, and therefore does not predict acceleration. It remains a possible interpretation only after a selected MTT action or closure equation yields these quantities.

## Minimum dark-energy test set

A viable construction must supply:

1.  a background $`H(z)`$ and luminosity and angular-diameter distances;

2.  BAO, supernova, CMB, and growth predictions from one parameter set;

3.  stable scalar and tensor perturbations without ghosts or gradient instabilities;

4.  a controlled effective Newton coupling and gravitational slip;

5.  compatibility with local tests and gravitational-wave propagation;

6.  an initial-condition and radiative-stability account; and

7.  evidence that the new description improves prediction or parameter economy.

Current observations motivate testing both a cosmological constant and dynamical alternatives; the paper does not assume that one option has already been selected.

# What projection can and cannot contribute

A projection
``` math
\pi:\mathcal X_{\rm upper}\longrightarrow\mathcal X_{\rm eff}
```
can hide variables that influence the retained sector. Integrating out or conditioning on hidden variables may yield effective forces, memory kernels, noise, or additional source terms. This is a legitimate route to dark-sector phenomenology.

However, the effective term depends on the upper action, state, projection, and approximation. The same projection map can produce no force, a local potential, colored noise, dissipation, or a nonlocal kernel under different upper dynamics. Projection alone does not select the sign, equation of state, clustering scale, or magnitude of a dark source.

The disciplined MTT claim is therefore:

> Selected upper degrees of freedom may descend to an effective gravitational source that is not represented as an elementary particle in the lower description.

Whether that source behaves as dark matter or dark energy is a subsequent calculation.

# Two constructive routes

## Effective-source route

Start with a selected upper action
``` math
S[g,\psi,\chi],
```
where $`\psi`$ denotes visible fields and $`\chi`$ denotes projected or unresolved fields. Define a state and integrate or solve for $`\chi`$ under a controlled approximation:
``` math
e^{iS_{\rm eff}[g,\psi]}
 =\int\mathcal D\chi\;e^{iS[g,\psi,\chi]}.
```
Then derive $`T^{\rm eff}_{\mu\nu}`$, conservation laws, response kernels, and perturbations. This route can yield particle, fluid, stochastic, or nonlocal behavior.

## Modified-geometry route

Derive a selected covariant operator $`\mathcal E_{\mu\nu}`$ from the MTT closure geometry. Prove its differential identity, count propagating degrees of freedom, and establish a well-posed stable initial-value problem. Then compute lensing and cosmology. Writing the result as an effective stress tensor is optional; matching observables is not.

Both routes require the same-source upper data. Importing a fitted halo profile or a fitted $`w(a)`$ would demonstrate compatibility but not derive the dark sector.

# Status and falsifiability

<div class="center">

| Claim | Status | Missing object or test |
|:---|:---|:---|
| Projection can generate effective sources | Standard possibility | Requires upper dynamics, state, and reduction. |
| MTT closure cost is a stress tensor | Not established | Metric variation of a selected covariant action. |
| MTT derives dark matter | Open | Cold clustering, lensing, CMB, halos, and likelihoods. |
| MTT derives dark energy | Open | $`H(z)`$, perturbations, stability, and likelihoods. |
| Dark matter need not be a new particle | Logically possible | Must still match all gravitational and cosmological evidence. |
| Dark energy is capacity exhaustion | Interpretive hypothesis | No selected equation of state or source amplitude yet. |
| One MTT source explains both sectors | Open | Common action and independent predictions required. |

</div>

The hypotheses are falsifiable. A candidate fails if it cannot reproduce lensing and dynamics from one metric, violates stability or local gravity, spoils the CMB or matter spectrum, or needs observational dark-sector profiles inserted as unconstrained functions.

# Discussion

The projection-first perspective contributes a useful warning: the absence of a lower particle encoding does not prove the absence of upper physical influence. Effective theories routinely contain forces and stresses from variables that have been removed. This opens a legitimate nonparticle route.

The same warning applies in reverse. A variable missing from a description does not automatically gravitate, and a bookkeeping deficit does not automatically accelerate the universe. General covariance turns that gap into a concrete demand: produce the tensor or modified operator, prove its identity and stability, and confront the data.

This standard is productive for MTT. It identifies a single mathematical frontier rather than two verbal explanations: derive the selected metric-response functional of the unresolved sector. Its homogeneous part can then be tested as dark energy; its inhomogeneous and clustering part can be tested as dark matter.

# Conclusion

MTT has not yet explained dark matter or dark energy. It has a possible organizing hypothesis: unresolved selected source data may appear in a lower description as effective gravitational response rather than as new elementary particles.

The next result must be covariant and numerical. It should derive $`T^{\rm eff}_{\mu\nu}`$ or $`\mathcal E_{\mu\nu}`$ from a selected MTT action, obtain background and perturbation equations, and compare their lensing, growth, CMB, BAO, and supernova predictions with existing models. Until then, “constraint load” and “capacity exhaustion” name research directions, not dark-sector solutions.

<div class="thebibliography">

9

A. G. Riess et al., *Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant*, Astronomical Journal **116** (1998), 1009–1038.

S. Perlmutter et al., *Measurements of $`\Omega`$ and $`\Lambda`$ from 42 High-Redshift Supernovae*, Astrophysical Journal **517** (1999), 565–586.

D. Clowe et al., *A Direct Empirical Proof of the Existence of Dark Matter*, Astrophysical Journal Letters **648** (2006), L109–L113.

Planck Collaboration, *Planck 2018 Results. VI. Cosmological Parameters*, Astronomy & Astrophysics **641** (2020), A6.

DESI Collaboration, *DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations*, Journal of Cosmology and Astroparticle Physics **02** (2025), 021.

S. Weinberg, *The Cosmological Constant Problem*, Reviews of Modern Physics **61** (1989), 1–23.

</div>
