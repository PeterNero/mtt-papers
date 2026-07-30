---
abstract: |
  A projection-first viewpoint asks which physical structures belong to an effective description and which belong to a richer source from which that description descends. This paper develops the viewpoint as a conceptual tool, not an inevitability theorem. A many-to-one map can identify microscopic states, but it does not by itself define lower dynamics, probabilities, entropy, locality, an arrow of time, quantum theory, or gravity. Those conclusions require additional structures: an intertwining dynamics, a state or measure, observable algebras, stability estimates, and sector-specific source maps. Modal Triplet Theory provides exact examples of finite projectors, a shared phase line, fixed-point constructions, and selected free field and finite Standard-Model carriers at declared tiers. Its broader physical reconstructions remain conditional where the required maps are incomplete. The projection-first framework is therefore most useful as a discipline for typing levels of description and exposing missing bridges.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 2226db74b148e01d3928bb1eab6dc3b834b073f6abdc04e4aad45615aa888277
paper_id: a-projection-first-reframing-of-physics
release_state: zenodo_released
released_version: v2
title: |
  A Projection-First Reframing of Physics:
  Descent, Effective Description, and the Limits of the Analogy
zenodo_doi: 10.5281/zenodo.21665933
zenodo_record_id: 21665933
zenodo_url: "https://zenodo.org/records/21665933"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *A Projection-First Reframing of Physics*.

The original overview treated noninvertibility as sufficient for irreversibility and sometimes presented projection-based explanations as theorem-level necessities.

Projection, quotient dynamics, recovery, probability, locality, and physical time are now separated. Counterexamples show why a many-to-one map alone does not create an arrow of time.

Projection-first reasoning remains a useful way to organize effective descriptions and to demand explicit descent and recovery maps.

Each physical application must still construct its dynamics, state, observables, and same-source intertwiners; no universal physics follows from projection alone.

</div>

# The basic question

Physics often relates descriptions by forgetting detail:
``` math
\pi:X\longrightarrow Y.
```
The source space $`X`$ may contain microscopic, gauge, internal, or preprojection data. The effective space $`Y`$ contains the variables used by an observer or lower theory.

The projection-first question is:
``` math
\text{Which puzzles arise because properties of }Y
\text{ are incorrectly demanded of }X,\text{ or conversely?}
```
This can be illuminating. Gauge redundancy, coarse-graining, reduced density operators, effective field theories, and quotient spaces all depend on maps between descriptive levels. Yet the notation $`\pi`$ is not a physical theory. The domain, codomain, dynamics, states, and observables must be named.

# Projection and quotient dynamics

Let $`\Phi_t:X\to X`$ be upper evolution. A deterministic lower evolution $`\psi_t:Y\to Y`$ exists only if upper evolution respects projection fibers:
``` math
\pi(x)=\pi(x')
 \quad\Longrightarrow\quad
 \pi(\Phi_t x)=\pi(\Phi_t x')
```
for every relevant $`t`$. Equivalently,
``` math
\pi\Phi_t=\psi_t\pi.
```
Without this condition, the present lower state does not determine its own future. One may still obtain stochastic, memory-dependent, or set-valued lower dynamics, but those require additional constructions.

This distinction is central in MTT. A finite projector can select a carrier or sector. It does not automatically produce the effective equations acting on that sector.

# Why noninvertibility is not an arrow of time

If $`\pi`$ is many-to-one, the original upper state cannot generally be recovered from $`\pi(x)`$. That is loss of distinguishability relative to the lower description. It is not yet dynamical irreversibility.

Consider
``` math
X=Y\times F,\qquad
 \pi(y,f)=y,
```
and an invertible lower flow $`\psi_t`$. Define
``` math
\Phi_t(y,f)=(\psi_t(y),f).
```
The projection is many-to-one whenever $`F`$ has more than one point, but the lower dynamics remains exactly reversible. Thus:
``` math
\text{many-to-one description}
\not\Rightarrow
\text{irreversible lower evolution}.
```

An arrow of time can arise when the induced lower evolution is a proper semigroup, when recovery error grows, when entropy increases relative to a specified state, or when a physical record process has asymmetric boundary conditions. Each route needs its own theorem.

## Physical time and compact phase

A periodic phase variable can function as a clock in a specified dynamical model. It is not identical to noncompact Lorentzian time. Likewise, a branch choice can orient a history without proving that the unobserved branch is well behaved or physically realized.

# Recovery maps

For a surjection $`\pi:X\to Y`$, a section $`s:Y\to X`$ satisfies
``` math
\pi s=I_Y.
```
It is a right inverse of $`\pi`$. It chooses one representative from each fiber but does not recover an arbitrary original state, because generally
``` math
s\pi\neq I_X.
```

Approximate recovery should be measured by a declared norm, fidelity, or observable error. In quantum information, a recovery channel has complete positivity and trace conditions. In geometry, a lift must preserve the relevant connections or tensors. The word “reconstruction” is incomplete until those structures are stated.

# Probability and quantization are additional

A set map carries no probability by itself. Probabilities require a measure, state, or stochastic law. Quantum probabilities additionally require an operator algebra and positive normalized state, or an equivalent operational structure.

Finite projectors and effects can be used inside quantum theory:
``` math
p(E|\rho)=\operatorname{tr}(\rho E).
```
But this equation imports the trace-state pairing. It is not derived from idempotence of $`E`$. The current MTT Born-source program has exact results on a restricted selected recorder, while the general apparatus and objective-history problem remains open.

Similarly, a Gaussian expansion or a finite spectral decomposition does not derive CCR/CAR quantization. The revised curved-spacetime QFT paper obtains a selected free CAR net by composing an MTT Dirac source with independent AQFT theorems.

# Locality and effective nonlocality

An upper theory can be local in its own variables while a reduced description is nonlocal. This happens when eliminated variables mediate memory or when observables do not factor across the projection.

The converse warning is equally important. Calling an upper description local does not evade Bell’s theorem if the resulting model is also assumed to satisfy measurement independence and conditional-factorization locality. The revised Bell paper instead distinguishes upper-local equations, microcausal observable algebras, operational no-signaling, and globally nonfactorizing states.

For spacetime propagation, a nonlocal spatial filter need not preserve strict support even if it leaves the hyperbolic principal symbol unchanged. Causal claims require a retarded kernel or support estimate.

# What projection does organize well

Projection-first language is especially useful for:

<div class="description">

separating redundant representatives from physical observables, provided constraints or BRST descent are respected;

identifying retained variables and quantifying discarded-sector errors;

distinguishing effects, channels, instruments, and records;

distinguishing local frames, quotient data, and global bundles;

distinguishing an upper fixed state from its lower encoding and proving any intertwiner between them;

asking whether an explicit computational dynamics embeds before invoking undecidability.

</div>

# Current MTT examples

The present corpus contains several concrete projection structures:

- the $`1+2+3`$ finite rank filtration;

- the q79 finite Haar projector and complementary finite Hessian sector;

- the shared flat phase line on the finite root-stack symbol;

- selected finite Standard-Model carrier and profile-level transport;

- a selected free twisted-Dirac CAR net on a globally hyperbolic representative;

- fixed-point and conditional-recovery theorems under explicit analytic hypotheses.

The important open bridges include the physical nonzero-Chern HYM endpoint, continuum geometry-to-operator naturality, selected upper action, general Born source, nonperturbative interacting QFT, and zero-primitive Standard-Model values.

# Claim ledger

<div class="center">

| Claim | Status | Required addition |
|:---|:---|:---|
| Projection identifies lower-equivalent states | Exact | Defined equivalence relation or map. |
| Compatible upper dynamics descends | Exact conditional | Fiber-respecting intertwining equation. |
| Many-to-one projection creates an arrow of time | False in general | Irreversible dynamics, entropy, or record theorem. |
| A section recovers the original upper state | False in general | Section chooses a representative only. |
| Projection supplies probabilities | False in general | Measure, state, or stochastic law. |
| Projection organizes MTT encodings | Supported | Several exact finite examples exist. |
| All physics is inevitable from projection | Not established | Sector-specific source maps and dynamics. |

</div>

# Discussion

The strongest use of a projection-first framework is methodological. It prevents a familiar category error: transferring a property across a map without proving that the relevant structure is preserved. It also suggests new constructions, because a failed transfer tells us what the missing intertwiner must carry.

For MTT, this discipline supports the proposed preprojection language. If one upper object is to generate Dirac, Weyl, twistor, QFT, Standard-Model, and gravitational encodings, the claim should be expressed as a family of commuting diagrams preserving connections, actions, states, and observables. Similarity of dimensions or terminology is not enough.

# Conclusion

A projection-first reframing remains a valuable way to think about physics, provided projection is not asked to do more than it can. It identifies descriptive equivalence and can organize descent. Dynamics, probability, locality, irreversibility, quantization, and gravity require additional objects.

The current MTT program has enough exact finite structure to make this more than a metaphor. Its next advances depend on constructing the missing same-source intertwiners. That is a sharper and more credible program than claiming that projection alone makes the rest inevitable.

<div class="thebibliography">

99

M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2010.

H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press, 2002.

R. Haag, *Local Quantum Physics*, Springer, 1996.

P. Nero, *Modal Triplet Theory: Foundations*, current revised MTT paper corpus, 2026.

P. Nero, *Fixed Points I–VI*, current revised MTT paper corpus, 2026.

</div>
