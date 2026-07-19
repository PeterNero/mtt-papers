---
abstract: |
  We present a first-principles derivation of interacting quantum field theory (QFT) on curved spacetimes from Modal Triplet Theory (MTT). Extending the projection operator formalism $`\Pi_{\mathrm{QM}}`$ of the MTT $`\to`$ quantum mechanics correspondence, we construct $`\Pi_{\mathrm{QFT}}`$ as a map from modal-coherent sectors of the 10D MTT configuration space to the algebra of quantum fields on a globally hyperbolic 4D spacetime $`(Y_4,g_{\mu\nu})`$. Our formulation employs the algebraic QFT framework, ensuring the Hadamard property of physical states, and incorporates running couplings from the covariant functional renormalisation group (FRG). We derive the semiclassical Einstein equation with FRG-improved $`\langle T_{\mu\nu} \rangle_{\mathrm{ren}}`$, discuss unitarity and implementability conditions (Shale–Stinespring), and give a worked example: scalar field particle production in a spatially flat FRW universe with scale-dependent mass and curvature coupling. This work completes the triad MTT $`\to`$ (QM, GR, QFT) and provides a mathematically rigorous bridge between modal dynamics and the standard formalism of quantum fields in curved backgrounds.
author:
- Peter Nero
current_version: v3
date: January, 2026
generated_from_main_tex_sha256: bebfbc5d5a847c2e1dc92af32d4e1cdf4d573b5c90a2c096be2f51218142ac8f
paper_id: modal-triplet-theory-from-mtt-to-quantum-field-theory-o-fd17e8ba
release_state: zenodo_released
released_version: v3.0
title: "**Modal Triplet Theory: From MTT to Quantum Field Theory on Curved Spacetime**"
zenodo_doi: 10.5281/zenodo.18321814
zenodo_record_id: 18321814
zenodo_url: "https://zenodo.org/records/18321814"
---

# Introduction

Modal Triplet Theory (MTT) provides a 10-dimensional, fixed-point and gap-structured field-theoretic framework unifying gravity, gauge fields, matter sectors, and a modal phase degree of freedom. Previous work has established explicit projections $`\Pi_{\mathrm{QM}}`$ and $`\Pi_{\mathrm{GR}}`$ realising the derivations MTT $`\to`$ quantum mechanics and MTT $`\to`$ general relativity, respectively. Here we extend this program to the third pillar: the derivation of interacting quantum field theory (QFT) on curved spacetimes from MTT.

Our goals in this paper are:

1.  To define the projection operator $`\Pi_{\mathrm{QFT}}`$ from modal configuration space to the \*algebra\* of quantum fields on $`(Y_4,g_{\mu\nu})`$, not just finite-mode truncations.

2.  To ensure the projected states satisfy the Hadamard condition, enabling covariant renormalisation of observables such as $`\langle T_{\mu\nu} \rangle`$.

3.  To incorporate running couplings via the covariant functional renormalisation group (FRG) in a manner consistent with diffeomorphism invariance.

4.  To analyse unitarity of the projected dynamics via the Shale–Stinespring criterion.

5.  To demonstrate the formalism in a concrete example with cosmological relevance.

The structure of the paper is as follows. In Sec. <a href="#sec:proj" data-reference-type="ref" data-reference="sec:proj">2</a>, we recall the modal field content of MTT and define the algebraic QFT projection $`\Pi_{\mathrm{QFT}}`$. Sec. <a href="#sec:algqft" data-reference-type="ref" data-reference="sec:algqft">3</a> reviews the field-algebra and Hadamard-state framework, and explains how modal coherence data selects a physical state. Sec. <a href="#sec:dyn" data-reference-type="ref" data-reference="sec:dyn">4</a> develops the dynamical evolution, including unitary implementability and Bogoliubov transformations. In Sec. <a href="#sec:renTmunu" data-reference-type="ref" data-reference="sec:renTmunu">5</a> we construct the renormalised stress–energy tensor and its conservation, then couple it to the semiclassical Einstein equation with FRG-improved couplings. Sec. <a href="#sec:frg" data-reference-type="ref" data-reference="sec:frg">6</a> describes the covariant FRG machinery and the projection of the Wetterich flow onto relevant operators. Sec. <a href="#sec:frw-example" data-reference-type="ref" data-reference="sec:frw-example">8</a> presents the FRW scalar example with running parameters. We conclude in Sec. <a href="#sec:summary" data-reference-type="ref" data-reference="sec:summary">9</a> with a summary and outlook.

All statements in this paper are local in time and are formulated on finite time slabs; global-in-time existence or completeness is not claimed.

# Modal Field Content and Definition of $`\Pi_{\mathrm{QFT}}`$

## Modal Triplet Theory configuration space

The classical configuration space of MTT consists of the following fields on a ten-dimensional manifold
``` math
M^{10} \;=\; Y_4 \times B_1 \times B_2 \times B_3,
```
where $`Y_4`$ is a globally hyperbolic Lorentzian spacetime and the $`B_n`$ are compact internal modal manifolds associated with each triplet leg:

- Gravity sector: tetrad $`e^a{}_\mu`$ or metric $`g_{\mu\nu}`$ on $`Y_4`$ extended trivially over the $`B_n`$; internal warp factors and moduli are encoded in the ten-dimensional metric $`g_{AB}`$.

- Gauge sectors: connections $`A^{(n)}_\mu`$ for gauge factors $`G_n`$, plus their higher-dimensional components along the $`B_n`$.

- Fermions: two-of-three fermionic fields $`\Psi_{ij}`$, valued in spin bundles over $`Y_4`$ tensored with appropriate representations of $`G_n`$ and harmonic modes on the $`B_n`$.

- Scalars: coherent scalar fields $`\phi_n`$ and the family-phase scalar $`\vartheta`$.

The fixed-point and gap structure of MTT is encoded in:

1.  The *coherent-sector projection*, selecting modal field configurations lying on a stable fixed point with finite excitation gaps $`\lambda_*^{-1}`$ to other modal sectors.

2.  A set of *superselection integers* $`(Q_{12},Q_{13},Q_{23}; k_2,k_3; g)`$ labelling disconnected components of the configuration space; these protect fermion family number and internal topological structure.

## From finite-mode truncations to the full field algebra

In the MTT $`\to`$ QM derivation, the projection $`\Pi_{\mathrm{QM}}`$ restricted modal configurations to a finite set of normal modes, producing a Hilbert space and Hamiltonian dynamics for a finite number of degrees of freedom. Here, we lift this restriction and instead map to the *algebra of quantum fields* on $`(Y_4,g_{\mu\nu})`$.

Let $`\mathcal{C}_{\mathrm{MTT}}`$ denote the coherent-sector configuration space of MTT in a fixed superselection sector. Let $`(M,g)`$ denote the effective 4D spacetime $`(Y_4,g_{\mu\nu})`$ obtained by the $`\Pi_{\mathrm{GR}}`$ projection and integration over the $`B_n`$. We denote by $`\mathcal{A}(M,g)`$ the *CCR* (bosons) and *CAR* (fermions) $`*`$-algebra of quantum fields on $`(M,g)`$.

<div class="definition">

**Definition 1** (QFT projection). The projection operator
``` math
\Pi_{\mathrm{QFT}}: \mathcal{C}_{\mathrm{MTT}} \longrightarrow \{(\mathcal{A}(M,g),\omega)\}
```
maps a coherent-sector MTT configuration to:

1.  the field algebra $`\mathcal{A}(M,g)`$ generated by smeared quantum fields $`\Phi(f)`$ for each matter and gauge species (and the metric, if quantised perturbatively), with canonical commutation or anticommutation relations,

2.  a *state* $`\omega`$ on $`\mathcal{A}`$ that is of Hadamard form.

</div>

Physically, $`\Pi_{\mathrm{QFT}}`$ encodes two operations:

Modal pushforward:  
restriction of the ten-dimensional fields to $`Y_4`$ and decomposition into harmonics on $`B_n`$, producing field species and their bare parameters $`(m_0, g_0, \xi_0, \dots)`$ on $`(M,g)`$.

State selection:  
mapping the modal coherence data to a state $`\omega`$ whose two-point function $`W_\omega`$ has the universal Hadamard short-distance structure required for local covariant renormalisation.

## Properties of $`\Pi_{\mathrm{QFT}}`$

#### Functoriality.

$`\Pi_{\mathrm{QFT}}`$ is covariant under isometries of $`(M,g)`$ induced from automorphisms of the coherent-sector $`M^{10}`$.

#### Gauge/diffeomorphism invariance.

The construction is invariant under the residual gauge symmetries and diffeomorphisms preserved by $`\Pi_{\mathrm{GR}}`$.

#### Gap stability.

The fixed-point gap ensures that integrating out heavy internal modes leaves a well-defined low-energy effective field theory on $`(M,g)`$ with local operators up to suppressed higher-derivative terms.

<div class="remark">

*Remark 2*. The algebraic construction depends only on the coherent-sector projector $`\Pi_{\mathrm{coh}}`$ and the induced effective operator on the base spacetime. Higher noncoherent spectral data and microscopic fibre details do not enter the definition of the observable algebra.

</div>

# Algebraic QFT Framework and State Selection

## Field algebras on curved spacetimes

Let $`(M,g)`$ be a globally hyperbolic Lorentzian spacetime. For each bosonic field species $`\phi`$ obeying a linear equation of motion $`P\phi = 0`$ (e.g. Klein–Gordon, Maxwell, Yang–Mills in a fixed background), one defines the *canonical commutation relations* (CCR) $`*`$-algebra $`\mathcal{A}_{\phi}(M,g)`$ generated by smeared fields $`\phi(f)`$, $`f \in C_0^\infty(M)`$, modulo the relations:
``` math
\begin{align}
[\phi(f),\phi(h)] &= i \Delta(f,h) \mathbf{1}, \\
\phi(Pf) &= 0,
\end{align}
```
where $`\Delta`$ is the causal propagator $`E_{\mathrm{ret}} - E_{\mathrm{adv}}`$ of $`P`$.

For Dirac fields $`\psi`$ satisfying $`D\psi=0`$, the CAR $`C^*`$-algebra is generated by symbols $`\psi(f)`$, $`f\in C^\infty_0(M,S)`$, modulo
``` math
\begin{equation}
\{\psi(f),\psi(h)\}=0,\qquad
\{\psi(f),\psi(h)^{\!*}\}= S(f,h)\, \mathbf{1},
\label{eq:CAR}
\end{equation}
```
where $`S`$ is the causal fundamental solution of $`D`$ (skew-adjoint), and $`{}^{\!*}`$ is the $`*`$-operation in the algebra.

The full field algebra $`\mathcal{A}(M,g)`$ is the tensor product (in the $`*`$-algebra sense) of $`\mathcal{A}_{\phi}`$ and $`\mathcal{A}_{\psi}`$ factors for all species, including ghosts and gauge-fixing sectors if quantising gauge fields.

## Hadamard states and local covariance

A *state* on $`\mathcal{A}(M,g)`$ is a positive, normalised linear functional $`\omega: \mathcal{A} \to \mathbb{C}`$. Physically, $`\omega(A)`$ gives the expectation value of the observable $`A`$ in the state $`\omega`$. For free fields, a state is fully characterised by its two-point function $`W_\omega`$; higher $`n`$-point functions follow by Wick’s theorem in quasifree cases.

A state $`\omega`$ is of *Hadamard form* if, in a neighbourhood of any point $`x\in M`$, the singular part of $`W_\omega(x,x')`$ matches the universal Hadamard parametrix:
``` math
\begin{equation}
W_\omega(x,x') \;\sim\; \frac{U(x,x')}{\sigma_\epsilon(x,x')} \;+\; V(x,x') \ln \sigma_\epsilon(x,x') \;+\; W_{\mathrm{smooth}}(x,x'),
\end{equation}
```
where $`\sigma_\epsilon`$ is Synge’s world function with Feynman $`i\epsilon`$ prescription, and $`U`$, $`V`$ are smooth biscalars determined by the geometry and field equation. Hadamard states ensure that local, covariant renormalisation of composite operators (e.g. $`T_{\mu\nu}`$) is possible.

## State selection from modal data

In MTT, the modal fields $`\Psi^*`$ in a coherent sector carry:

1.  *Geometric data*: the induced 4D metric $`g_{\mu\nu}`$ from $`\Pi_{\mathrm{GR}}`$ and its curvature tensors.

2.  *Mode structure*: harmonic decomposition coefficients on $`B_n`$ determining field masses $`m`$, couplings $`g`$, curvature couplings $`\xi`$, etc.

3.  *Coherence phases*: internal modal time phases and correlation data encoding relative alignment of field components.

We define $`\Pi_{\mathrm{QFT}}`$ to map $`(\Psi^*, g_{\mu\nu})`$ to $`(\mathcal{A}(M,g), \omega)`$ as follows:

Step 1:  
Construct the field algebra $`\mathcal{A}(M,g)`$ for the set of species arising in the $`\Pi_{\mathrm{GR}}`$ reduction of $`\Psi^*`$, with parameters $`(m,\xi,g,\dots)`$ fixed by the modal harmonic decomposition.

Step 2:  
From the modal coherence phases, build the two-point function $`W_\omega`$ in a neighbourhood of the observer’s worldline by matching the short-distance structure to the Minkowski vacuum in local normal coordinates, and extending globally by parallel transport along the modal minimal paths $`\gamma^*(x^\mu)`$. This yields a *quasifree Hadamard state* $`\omega`$.

In spacetimes with high symmetry (e.g. FRW), this procedure picks out the *adiabatic vacuum* of some order, modified by the running couplings inherited from MTT via the functional RG flow.

#### Explicit Hadamard selection.

Locally, choose Riemann normal coordinates at $`x\in M`$ and set the two-point function to match the Minkowski parametrix up to smooth remainders; transport along modal minimal curves $`\gamma_\ast`$ to extend globally. Equivalently, in spatially homogeneous cases (e.g. FRW) choose an adiabatic vacuum of order $`N\ge 2`$ (bosons) or the standard fermionic analogue. Both constructions yield quasifree Hadamard states and are compatible with the smooth running couplings inherited from the FRG, provided these are $`C^\infty`$ with bounded derivatives on the observational domain.

#### Remark.

This construction is *locally covariant*: under an embedding $`\chi: (M,g) \hookrightarrow (M',g')`$, the corresponding algebras and states satisfy
``` math
\Pi_{\mathrm{QFT}}(\Psi^*|_M) \;=\; (\mathcal{A}(\chi),\chi^*\omega'),
```
with $`\mathcal{A}(\chi)`$ the induced $`*`$-homomorphism.

## Local nets and the time-slice property

To make the propagation content explicit in algebraic form, we package the field algebra on $`(M,g)`$ as a Haag–Kastler net of local algebras.

Let $`(M,g)`$ be globally hyperbolic and let $`P`$ be a normally hyperbolic operator (or Dirac-type operator in the fermionic case) defining the free field equation. Let $`\mathcal{A}(M,g)`$ denote the corresponding CCR (or CAR) $`*`$–algebra generated by smeared fields $`\Phi(f)`$ (or $`\Psi(f)`$), modulo the field equation ideal and the canonical (anti)commutation relations determined by the causal propagator.

For each open region $`\mathcal{O}\subset M`$, define the *local algebra* $`\mathcal{A}(\mathcal{O})`$ to be the unital $`*`$–subalgebra of $`\mathcal{A}(M,g)`$ generated by all smeared fields with support in $`\mathcal{O}`$:
``` math
\mathcal{A}(\mathcal{O}) := \big\langle \Phi(f)\ :\ f\in C^\infty_0(M),\ \mathrm{supp}(f)\subset \mathcal{O}\big\rangle_{*}.
```
(For fermions, replace $`\Phi`$ by $`\Psi`$ and CCR by CAR, with the same support restriction.)

#### Isotony.

If $`\mathcal{O}_1\subset \mathcal{O}_2`$, then $`\mathcal{A}(\mathcal{O}_1)\subset \mathcal{A}(\mathcal{O}_2)`$.

#### Microcausality (locality).

If $`\mathcal{O}_1`$ and $`\mathcal{O}_2`$ are causally disjoint, then the corresponding local algebras commute (bosons) or graded-commute (fermions):
``` math
[\mathcal{A}(\mathcal{O}_1),\mathcal{A}(\mathcal{O}_2)] = 0,
\qquad
\text{(or graded commutator }=0\text{ in the fermionic case).}
```
This follows from support properties of the causal propagator $`\Delta = E_{\mathrm{ret}}-E_{\mathrm{adv}}`$, which vanishes for spacelike separation.

#### Time-slice property (algebraic propagation).

Let $`\mathcal{O}\subset M`$ be an open region containing a Cauchy surface for $`(M,g)`$ (or for the relevant subspacetime under consideration). Then the inclusion
``` math
\mathcal{A}(\mathcal{O}) \hookrightarrow \mathcal{A}(M,g)
```
is an isomorphism onto the algebra of the domain of dependence $`D(\mathcal{O})`$; equivalently, the algebra generated in an arbitrarily small neighborhood of a Cauchy surface determines the algebra in its causal development. This is the algebraic expression of hyperbolic propagation and will be the primary notion of “field propagation” used throughout.

#### Scope.

All statements above are to be understood slab-locally in the MTT sense: they hold precisely on those effective domains where the QFT encoding and the associated normally hyperbolic operator $`P`$ are available under admissibility control.

# Dynamics, Bogoliubov Transformations, and Unitary Implementability

In this section we specify the time evolution of the projected field algebra and state, and give precise conditions for unitarily implementable dynamics on a chosen Fock representation. The curved background $`(M,g)`$ and the running parameters inherited from MTT via the FRG (Sec. <a href="#sec:frg" data-reference-type="ref" data-reference="sec:frg">6</a>) generally render the evolution *time-dependent*. We treat bosons (CCR) and fermions (CAR) in parallel.

## Classical evolution and symplectic/inner-product structures

Let $`(\mathcal{S},E)`$ denote the real vector space of smooth, compactly supported solutions of a linear hyperbolic equation $`P\phi=0`$ (e.g. Klein–Gordon with possibly time-dependent parameters) with causal propagator $`\Delta=E_{\mathrm{ret}}-E_{\mathrm{adv}}`$. The *symplectic form* on $`\mathcal{S}`$ is
``` math
\begin{equation}
\sigma(\phi_1,\phi_2) \;=\; \int_\Sigma \!\left(\phi_1\,\pi_2-\phi_2\,\pi_1\right)\, d\Sigma,
\qquad \pi:=n^\mu \sqrt{h}\,\partial_\mu \phi,
\label{eq:symplectic}
\end{equation}
```
with $`\Sigma`$ a Cauchy surface and $`n^\mu`$ its unit normal (the expression is Cauchy-surface invariant). For Dirac fields, the classical space $`\mathcal{S}_{\mathrm{D}}`$ carries a *Hermitian* inner product
``` math
\begin{equation}
\langle \psi_1,\psi_2\rangle_{\mathrm{D}}
= \int_\Sigma \!\bar\psi_1 \gamma^\mu n_\mu \psi_2\, d\Sigma,
\end{equation}
```
which is conserved under the Dirac evolution. Time evolution defines a family of real-linear maps $`U_{t,t_0}:\mathcal{S}\to\mathcal{S}`$ (bosons, symplectic) and unitary maps $`V_{t,t_0}:\mathcal{S}_{\mathrm{D}}\to\mathcal{S}_{\mathrm{D}}`$ (fermions, CAR).

## Quantisation, complex structures, and quasifree states

For CCR, a *complex structure* $`J:\mathcal{S}\to\mathcal{S}`$ ($`J^2=-\mathbf{1}`$, $`\sigma(J\cdot,J\cdot)=\sigma`$, $`\mu(\cdot,\cdot):=\sigma(\cdot,J\cdot)`$ positive) determines a quasifree state $`\omega_J`$ with two-point function $`W_J=\frac12(\mu - i\sigma)`$. The corresponding one-particle Hilbert space $`(\mathcal{H}_J,\langle\cdot,\cdot\rangle)`$ yields a Fock representation $`\mathcal{F}_J`$ of the Weyl algebra. For CAR, a projection $`S`$ on $`\mathcal{S}_{\mathrm{D}}\otimes\mathbb{C}`$ with $`0\le S\le \mathbf{1}`$ defines a quasifree state; $`S`$ is the *covariance* (two-point function) obeying the Dirac equation in both arguments.

In the MTT projection, $`\Pi_{\mathrm{QFT}}`$ (Sec. <a href="#sec:algqft" data-reference-type="ref" data-reference="sec:algqft">3</a>) selects a *Hadamard* quasifree state $`\omega`$ (hence a $`J`$ or $`S`$) by matching the universal short-distance structure and the modal coherence phases. Running couplings $`m(t),\xi(t),Z(t),\ldots`$ enter only through $`P`$ (or $`\mathcal{D}`$) and do not spoil Hadamardness provided they are smooth with bounded derivatives on the observational domain.

## Bogoliubov transformations for time-dependent dynamics

Let $`U_{t,t_0}`$ be the classical symplectic evolution for the bosonic system (the fermionic case is analogous with unitary $`V_{t,t_0}`$). Relative to a fixed complex structure $`J`$ (equivalently a splitting $`\mathcal{S}\otimes\mathbb{C}=\mathcal{H}_J\oplus \overline{\mathcal{H}}_J`$), the map $`U_{t,t_0}`$ admits a block form
``` math
\begin{equation}
U_{t,t_0}
= \begin{pmatrix}
\alpha_{t,t_0} & \beta_{t,t_0} \\
\overline{\beta}_{t,t_0} & \overline{\alpha}_{t,t_0}
\end{pmatrix},
\qquad \alpha_{t,t_0}:\mathcal{H}_J\to\mathcal{H}_J,\ \beta_{t,t_0}:\overline{\mathcal{H}}_J\to\mathcal{H}_J,
\label{eq:Bogo}
\end{equation}
```
with $`\alpha^\dagger\alpha - \beta^\dagger\beta=\mathbf{1}`$ and $`\alpha\beta^{\mathsf{T}}=\beta\alpha^{\mathsf{T}}`$. These are the *Bogoliubov coefficients* determined by $`(M,g)`$ and the time dependence of $`P`$ (thus of $`m,\xi,Z,\ldots`$).

<div id="thm:Shale" class="theorem">

**Theorem 3** (Shale–Stinespring criterion (CCR)). *Let $`\omega_J`$ be a quasifree state with complex structure $`J`$ and Fock space $`\mathcal{F}_J`$. The symplectic evolution $`U_{t,t_0}`$ is unitarily implementable on $`\mathcal{F}_J`$ iff $`\beta_{t,t_0}`$ is Hilbert–Schmidt on $`\mathcal{H}_J`$:
``` math
\begin{equation}
\|\beta_{t,t_0}\|_{\mathrm{HS}}^2 \;=\; \mathrm{Tr}\,(\beta_{t,t_0}^\dagger \beta_{t,t_0}) \;<\; \infty.
\end{equation}
```*

</div>

<div id="thm:ShaleCAR" class="theorem">

**Theorem 4** (Shale–Stinespring criterion (CAR)). *Let $`\omega_S`$ be a quasifree CAR state with covariance $`S`$ and Fock space $`\mathcal{F}_S`$. The unitary evolution $`V_{t,t_0}`$ is implementable on $`\mathcal{F}_S`$ iff $`[S, V_{t,t_0}]`$ is Hilbert–Schmidt.*

</div>

<div class="proof">

*Idea of proof.* Standard arguments: for CCR, use the Segal–Shale–Weil representation of the restricted symplectic group and the fact that $`\beta\in \mathfrak{S}_2`$ (Hilbert–Schmidt) is necessary and sufficient for lifting to the metaplectic implementer. For CAR, use Araki’s criterion for Bogoliubov automorphisms of the CAR algebra. ◻

</div>

## Adiabatic/Hadamard initial data and implementability

In spatially homogeneous backgrounds (e.g. FRW) with smooth time dependence, adiabatic Hadamard states of order $`N\ge 2`$ (bosons) or the analogous fermionic constructions ensure
``` math
\begin{equation}
\sum_{k} |\beta_k(t,t_0)|^2 < \infty \quad \text{(compact Cauchy surfaces)},\qquad
\int_{\mathbb{R}^3}\!\! d^3\mathbf{k}\, |\beta_{\mathbf{k}}(t,t_0)|^2 < \infty \quad \text{(non-compact, with UV decay)} ,
\end{equation}
```
hence unitary implementability by the Shale–Stinespring criteria in Sec. <a href="#sec:dynamics" data-reference-type="ref" data-reference="sec:dynamics">[sec:dynamics]</a>. In our MTT setting, the smooth running couplings entering $`P`$ or $`D`$ preserve the adiabatic structure and do not spoil the Hadamard/microlocal spectrum conditions.

## KMS and stationary cases

If $`(M,g)`$ admits a timelike Killing vector $`K^\mu`$ and the couplings are stationary, the dynamics are implemented by a one-parameter group of $`*`$-automorphisms $`\alpha_t`$ of $`\mathcal{A}(M,g)`$. A state $`\omega`$ is *KMS* at inverse temperature $`\beta`$ if $`\omega(A\alpha_{i\beta}(B))=\omega(BA)`$ for a suitable dense set of $`A,B\in\mathcal{A}`$. In this case, $`\alpha_t`$ admits a unitary implementer in the GNS representation of $`\omega`$, and the modular flow is geometric. This covers static spacetimes and (locally) Rindler wedges, relevant for Unruh and Hawking effects.

## Gauge fields, constraints, and BRST in the projection

For Abelian gauge fields on a fixed background, the Gupta–Bleuler construction or BRST quantisation yields a physical Hilbert space $`\mathcal{H}_{\mathrm{phys}}=\ker Q_{\mathrm{BRST}}/\mathrm{Im}\,Q_{\mathrm{BRST}}`$. The evolution is implemented on the Krein space before reduction; compatibility with $`\Pi_{\mathrm{QFT}}`$ requires that the regulator and state selection respect Ward identities (see Sec. <a href="#sec:frg" data-reference-type="ref" data-reference="sec:frg">6</a>). For non-Abelian backgrounds linearised around a coherent MTT sector, the same structure applies perturbatively.

#### Ward/BRST identities with regulator.

Background-covariant regulators $`R_k(-\bar\nabla^2)`$ induce modified Ward (and BRST) identities holding at each $`k`$ and recovering the exact identities as $`k\to 0`$. Our state selection and renormalisation respect these identities; observables are taken at fixed $`k`$ (or after integrating the flow to $`k=0`$), ensuring gauge/diffeomorphism covariance.

## Interacting fields: perturbative algebraic QFT and causal factorisation

To incorporate interactions while preserving locality and covariance, we adopt the perturbative algebraic QFT (pAQFT) framework. Given a local interaction $`V(\phi)`$ (e.g. $`\lambda \phi^4`$) with running couplings from MTT/FRG, one constructs the *time-ordered* product $`\mathcal{T}`$ via Epstein–Glaser renormalisation and defines the interacting algebra $`\mathcal{A}_V`$ as a formal deformation of $`\mathcal{A}`$. The causal factorisation property ensures locality; the renormalisation freedom is fixed by Hadamard subtraction and microlocal spectrum condition. The in-in (Schwinger–Keldysh) construction used in Sec. <a href="#sec:renTmunu" data-reference-type="ref" data-reference="sec:renTmunu">5</a> then yields real-time, causal dynamics for expectation values and $`n`$-point functions.

#### Summary.

Given a Hadamard quasifree state selected by $`\Pi_{\mathrm{QFT}}`$, the time-dependent background and running couplings induce Bogoliubov transformations whose implementability is guaranteed under adiabatic/Hadamard conditions. This provides a unitary (or algebraically well-defined) evolution of the QFT observables on $`(M,g)`$, setting the stage for renormalised $`\langle T_{\mu\nu}\rangle`$ and semiclassical backreaction in the next section.

# Renormalised Stress–Energy Tensor and Semiclassical Backreaction

## Classical definition

For a classical matter field $`\phi`$ on $`(M,g)`$ with Lagrangian density $`\mathcal{L}(\phi,g)`$, the stress–energy tensor is
``` math
\begin{equation}
T_{\mu\nu}[\phi,g] \;=\; -\frac{2}{\sqrt{-g}} \frac{\delta S[\phi,g]}{\delta g^{\mu\nu}}.
\end{equation}
```
For example, a scalar field with curvature coupling $`\xi`$ and potential $`V(\phi)`$ has
``` math
\begin{align}
T_{\mu\nu} &= (1-2\xi)\,\nabla_\mu \phi \nabla_\nu \phi + \left(2\xi-\frac{1}{2}\right)g_{\mu\nu} (\nabla\phi)^2
- 2\xi\,\phi \nabla_\mu \nabla_\nu \phi
+ 2\xi\,g_{\mu\nu}\,\phi \Box \phi \nonumber\\
&\quad - \xi G_{\mu\nu}\,\phi^2 - g_{\mu\nu} V(\phi).
\end{align}
```

In gauge and fermion sectors, analogous expressions follow from varying the corresponding actions.

## Point-splitting renormalisation

Given a Hadamard state $`\omega`$ selected by $`\Pi_{\mathrm{QFT}}`$, the formal expectation value $`\langle T_{\mu\nu}(x) \rangle_\omega`$ contains ultraviolet divergences from the coincidence limit $`x'\to x`$ of products of fields. The *point-splitting* prescription replaces $`\phi(x)^2`$ by $`\phi(x)\phi(x')`$ and subtracts the *Hadamard parametrix* $`H(x,x')`$ before taking the limit:
``` math
\begin{equation}
\langle T_{\mu\nu}(x) \rangle_{\mathrm{ren}} =
\lim_{x'\to x} D_{\mu\nu}(x,x') \left[ W_\omega(x,x') - H(x,x') \right],
\label{eq:Tmunu-ren}
\end{equation}
```
where $`D_{\mu\nu}`$ is a bi-differential operator implementing the metric variation. The subtraction removes the universal singularities while preserving local covariance.

## Conservation and renormalisation freedom

By construction,
``` math
\begin{equation}
\nabla^\mu \langle T_{\mu\nu} \rangle_{\mathrm{ren}} = 0
\end{equation}
```
in any Hadamard state, reflecting the Ward identity for diffeomorphism invariance. There is a finite renormalisation freedom:
``` math
\begin{equation}
\langle T_{\mu\nu} \rangle_{\mathrm{ren}} \;\mapsto\;
\langle T_{\mu\nu} \rangle_{\mathrm{ren}} + \alpha_1 g_{\mu\nu} + \alpha_2 G_{\mu\nu}
+ \alpha_3 I_{\mu\nu} + \alpha_4 J_{\mu\nu},
\end{equation}
```
where $`I_{\mu\nu}`$ and $`J_{\mu\nu}`$ are local conserved curvature tensors from varying $`R^2`$ and $`R_{\rho\sigma}R^{\rho\sigma}`$, and the $`\alpha_i`$ are state-independent constants. In the MTT context, these constants become *scale-dependent* through the FRG flow (§<a href="#sec:frg" data-reference-type="ref" data-reference="sec:frg">6</a>).

#### Conservation at fixed coarse-graining scale.

The variation defining $`\langle T_{\mu\nu}\rangle_{\rm ren}`$ is taken at fixed $`k`$; thus $`\nabla^\mu\langle T_{\mu\nu}\rangle_{\rm ren}=0`$ holds exactly. If $`k`$ is promoted to a background-dependent profile, one must include the flow of the effective action along that profile to maintain diffeomorphism Ward identities; in this work we keep $`k`$ fixed when varying $`g`$.

## Trace anomaly

For classically conformal matter (e.g. $`\xi=1/6`$, $`m=0`$ scalar; Maxwell; massless Dirac), the classical $`T^\mu{}_\mu=0`$ is broken in the quantum theory:
``` math
\begin{equation}
\langle T^\mu{}_\mu \rangle_{\mathrm{ren}}
= \frac{1}{(4\pi)^2} \left[ c\,C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}
+ a\,E_4 + b\,\Box R \right],
\label{eq:trace-anomaly}
\end{equation}
```
where $`C_{\mu\nu\rho\sigma}`$ is the Weyl tensor, $`E_4`$ the Euler density, and $`a,b,c`$ are theory-dependent constants. In MTT, these coefficients acquire a mild scale dependence $`a_k,b_k,c_k`$ inherited from the running couplings of the matter content.

## Semiclassical Einstein equation

The *semiclassical Einstein equation* (SEE) couples the renormalised $`\langle T_{\mu\nu}\rangle`$ to the spacetime metric:
``` math
\begin{equation}
G_{\mu\nu} + \Lambda_{\mathrm{eff}}(k) g_{\mu\nu}
= 8\pi G_{\mathrm{eff}}(k) \langle T_{\mu\nu} \rangle_{\mathrm{ren}} + \text{(higher curvature terms)},
\label{eq:SEE}
\end{equation}
```
where $`G_{\mathrm{eff}}(k)`$ and $`\Lambda_{\mathrm{eff}}(k)`$ are the scale-dependent couplings from the MTT FRG analysis. Higher curvature terms, such as $`\alpha_3 I_{\mu\nu} + \alpha_4 J_{\mu\nu}`$, appear if the FRG truncation includes $`R^2`$ and $`R_{\mu\nu}R^{\mu\nu}`$ operators.

#### Backreaction in the MTT framework.

The SEE <a href="#eq:SEE" data-reference-type="eqref" data-reference="eq:SEE">[eq:SEE]</a> is solved *self-consistently* with the QFT state $`\omega`$ selected by $`\Pi_{\mathrm{QFT}}`$, so that the geometry $`g_{\mu\nu}`$ and the matter state co-determine each other. Running couplings encode the integrated-out heavy modal modes and the RG dressing of both gravitational and matter sectors.

## In-in formalism for causal evolution

For time-dependent backgrounds, causal evolution of $`\langle T_{\mu\nu} \rangle`$ is formulated in the *in-in* (Schwinger–Keldysh) formalism. Let $`S_{\mathrm{tot}}[g,\Phi]`$ be the classical matter action; double the fields $`\Phi\to(\Phi_+,\Phi_-)`$ and evolve along a closed time contour $`\mathcal{C}`$. The generating functional is
``` math
\begin{equation}
Z[J_+,J_-] = \int \mathcal{D}\Phi_+\,\mathcal{D}\Phi_- \;
e^{i S_{\mathrm{tot}}[g,\Phi_+] - i S_{\mathrm{tot}}[g,\Phi_-] + i\int_\mathcal{C} J \Phi}.
\end{equation}
```
Functional differentiation with respect to $`J_\pm`$ yields time-ordered and anti-time-ordered correlators, from which one builds causal expectation values like $`\langle T_{\mu\nu}(x) \rangle`$ that depend only on the past of $`x`$. This formalism is essential for nonequilibrium phenomena such as particle production in an expanding universe.

#### Summary.

In the MTT→QFT projection, the renormalised $`\langle T_{\mu\nu} \rangle_{\mathrm{ren}}`$ is constructed via point-splitting in Hadamard states, ensuring local covariance, conservation, and correct anomalies. The semiclassical Einstein equation with RG-improved couplings from MTT yields a unified backreaction framework linking modal dynamics, quantum field theory, and effective gravity.

# Covariant Functional Renormalization Group on Curved Spacetime

In this section we formulate the functional renormalization group (FRG) for the effective quantum field theory obtained from the coherent sector of Modal Triplet Theory. The purpose of the FRG here is not to introduce new dynamics, but to provide a covariant and controlled description of scale dependence, compatible with the fixed–point and admissibility framework developed in the preceding sections.

## Euclidean continuation and conventions

The FRG is formulated in Euclidean signature. Accordingly, throughout this section we work with the Wick–rotated metric $`g_E`$ of signature $`(+,+,+,+)`$, the Euclidean action $`S_E`$, and the Euclidean effective average action $`\Gamma_k^E`$. Lorentzian quantities $`(g,S,\Gamma)`$ used elsewhere in the paper are related to their Euclidean counterparts by standard Wick rotation and analytic continuation. No physical statement in this section depends on a nonstandard choice of continuation.

## Effective average action and flow equation

Let $`\Phi`$ collectively denote the fields of the projected effective theory (scalar, spinor, and gauge fields as appropriate). The Euclidean effective average action $`\Gamma_k^E[\Phi]`$ is defined by adding an infrared regulator term
``` math
\Delta S_k^E[\Phi] = \frac{1}{2} \langle \Phi, R_k \Phi \rangle_{g_E},
```
where $`R_k`$ is a positive, covariant regulator suppressing modes with eigenvalues $`\lambda \lesssim k^2`$ of the Euclidean Laplace–type operators.

The scale dependence of $`\Gamma_k^E`$ is governed by the Wetterich equation
``` math
\begin{equation}
\partial_k \Gamma_k^E[\Phi]
=
\frac{1}{2}
\operatorname{Tr}
\left[
\left(
\Gamma_k^{E\,(2)}[\Phi] + R_k
\right)^{-1}
\partial_k R_k
\right],
\end{equation}
```
where $`\Gamma_k^{E\,(2)}`$ denotes the second functional derivative of $`\Gamma_k^E`$ with respect to the fields, and the trace is taken over all field components as well as spacetime indices, using the Euclidean metric $`g_E`$.

The regulator $`R_k`$ is chosen to be a function of the Euclidean Laplace–Beltrami operator $`\Delta_E`$ associated with $`g_E`$, so that the flow preserves covariance on curved backgrounds.

## Locality, admissibility, and truncations

The FRG flow is evaluated only on finite, bounded–geometry regions where the coherent sector is well defined and the admissibility conditions hold. Within such regions, the flow equation preserves locality in the effective field theory sense: $`\Gamma_k^E`$ admits a derivative expansion whose coefficients depend smoothly on $`k`$.

Truncations of $`\Gamma_k^E`$ are understood as controlled approximations within an admissible universality class. In particular, the presence of a spectral gap separating coherent and noncoherent modes ensures that contributions from discarded sectors are suppressed and do not destabilize the flow. This is consistent with the Fundamental Contractivity Condition and the fixed–point analysis developed in Fixed Points I–V.

## Infrared limit and return to Lorentzian physics

Physical couplings and correlation functions are obtained by integrating the flow to $`k \to 0`$, yielding the full Euclidean effective action $`\Gamma_{k=0}^E`$. Lorentzian observables are then recovered by analytic continuation back to Lorentzian signature. In this sense, the FRG provides a technically convenient but conceptually auxiliary tool for organizing scale dependence, without altering the underlying deterministic dynamics or the admissibility structure of Modal Triplet Theory.

# Universality Class of the Coherent Effective Field Theory

A central question for any effective field theory derived from a microscopic construction is whether its low-energy predictions depend sensitively on microscopic details, or only on a small set of macroscopic invariants. In this section we show that the coherent-sector quantum field theory obtained from MTT belongs to a well-defined *universality class* in the Wilsonian sense.

Within a coherent universality class, admissibility thresholds and selection barriers are universal up to renormalization of relevant couplings, and do not depend on microscopic modal details.

## Definition of the universality class

We consider two microscopic modal geometries
``` math
\mathcal{M}_1 = (Y,g;\{B_n\},\Delta_{B_n}),\qquad
\mathcal{M}_2 = (Y,g;\{B_n'\},\Delta_{B_n'}),
```
both satisfying the standing assumptions SA.1–SA.4 of the MTT Foundation (bounded geometry on time slabs, uniform spectral gap, bounded coherent projector, and well-posed coherent evolution).

<div class="definition">

**Definition 5** (Coherent universality class). Two microscopic modal geometries $`\mathcal{M}_1`$ and $`\mathcal{M}_2`$ belong to the same *coherent universality class* if they share:

1.  the same base spacetime $`(Y,g)`$ up to bounded-geometry equivalence,

2.  the same number of coherent bundles and symmetry representations,

3.  a common positivity window $`\lambda_a(x)\ge\lambda_{\min}>0`$ on the coherent domain,

4.  the same coherent-sector projector $`\Pi_{\mathrm{coh}}`$ up to bounded $`H^1`$ perturbations,

5.  stability margins satisfying the RG–FCC hypotheses in the MTT Foundation.

</div>

The microscopic fibre metrics, higher eigenvalues, and detailed noncoherent spectral structure are allowed to differ.

## RG flow and loss of microscopic information

Let $`k`$ denote a coarse-graining scale and let $`\Gamma_k[\phi]`$ be the scale-dependent effective action obtained from the coherent-sector projection followed by covariant renormalization group flow.

By construction:

- integrating out noncoherent modes modifies only irrelevant operators,

- relevant operators are controlled by symmetry and gap data,

- RG flow preserves the admissibility window as long as the RG–FCC margin remains positive.

In particular, the running couplings $`\{g_i(k)\}`$ depend on microscopic details only through their initial values at $`k_0`$, while their infrared scaling is governed by the same beta functions within a universality class.

## Universality of the coherent EFT

<div id="thm:universality" class="theorem">

**Theorem 6** (Universality of the coherent EFT). *Let $`\mathcal{M}_1`$ and $`\mathcal{M}_2`$ be two microscopic modal geometries in the same coherent universality class. Assume the RG–FCC holds uniformly on $`k\in[k_{\mathrm{IR}},k_0]`$. Then the corresponding coherent effective field theories $`\Gamma^{(1)}_{k_{\mathrm{IR}}}`$ and $`\Gamma^{(2)}_{k_{\mathrm{IR}}}`$ agree up to:*

1.  *finite renormalizations of relevant couplings,*

2.  *irrelevant operators suppressed by powers of $`k_{\mathrm{IR}}/\lambda_{\min}`$,*

3.  *field redefinitions compatible with the coherent projector.*

*In particular, scattering amplitudes, anomaly structure, and low-energy observables coincide within the expected EFT accuracy.*

</div>

Universality here does not imply uniqueness of the Standard Model or of any specific parameter values; it asserts equivalence of low-energy effective theories up to the expected EFT freedom within a given universality class.

<div class="proof">

*Proof.* The proof follows standard Wilsonian reasoning. By the RG–FCC theorem, the coherent sector remains well-defined and contractive under RG flow on $`[k_{\mathrm{IR}},k_0]`$. Differences in microscopic structure generate only irrelevant operators, which are suppressed in the infrared. Relevant operators are fixed by symmetry, representation content, and the positivity window, which coincide by assumption. ◻

</div>

## Implications

Theorem <a href="#thm:universality" data-reference-type="ref" data-reference="thm:universality">6</a> shows that the coherent QFT derived from MTT is robust: its low-energy content depends only on a small set of macroscopic geometric and spectral data, not on microscopic details. This explains why distinct microscopic modal geometries can lead to the same effective quantum field theory, and why predictions derived from the coherent sector are stable under perturbations of the underlying structure.

# Worked example: scalar field in FRW with running parameters

Consider spatially flat FRW $`ds^2=-dt^2+a(t)^2 d\mathbf{x}^2`$ and a real scalar with curvature coupling $`\xi_k`$ and running mass $`m_k`$ at fixed RG scale $`k`$. The Klein–Gordon equation reads
``` math
\begin{equation}
\ddot{\phi}+3H\dot{\phi}-\frac{1}{a^2}\Delta_{\mathbb{R}^3}\phi + m_k^2\,\phi + \xi_k R\,\phi =0,\qquad H:=\dot a/a,\quad R=6(\dot H + 2H^2).
\end{equation}
```
Mode functions $`\phi_{\mathbf{k}}(t)`$ obey
``` math
\begin{equation}
\ddot{\phi}_{\mathbf{k}} + 3H\dot{\phi}_{\mathbf{k}} + \Big(\frac{k^2}{a^2}+ m_k^2 + \xi_k R\Big)\phi_{\mathbf{k}}=0.
\end{equation}
```
Define the adiabatic initial data at $`t_0`$ by $`\phi_{\mathbf{k}}(t_0)=\big(2\omega_{\mathbf{k}}(t_0)\big)^{-1/2}`$, $`\dot\phi_{\mathbf{k}}(t_0)=\big(-\frac{3}{2}H(t_0) - \frac{\dot\omega_{\mathbf{k}}(t_0)}{2\omega_{\mathbf{k}}(t_0)}\big)\phi_{\mathbf{k}}(t_0)`$, with $`\omega_{\mathbf{k}}^2(t):=k^2/a^2+m_k^2+\xi_k R`$; this yields a quasifree Hadamard state of adiabatic order $`N\ge 2`$. As usual, write the Bogoliubov transform at time $`t`$ as
``` math
\begin{equation}
\phi_{\mathbf{k}}(t)=\alpha_{\mathbf{k}}(t,t_0)\,u_{\mathbf{k}}(t)+\beta_{\mathbf{k}}(t,t_0)\,u_{\mathbf{k}}^\ast(t),\qquad |\alpha_{\mathbf{k}}|^2-|\beta_{\mathbf{k}}|^2=1.
\end{equation}
```
For $`a,\ m_k,\ \xi_k`$ smooth with bounded derivatives on $`[t_0,T]`$, standard adiabatic estimates give $`|\beta_{\mathbf{k}}(t,t_0)|=\mathcal{O}(|\mathbf{k}|^{-2})`$ as $`|\mathbf{k}|\to\infty`$, hence $`\int d^3\mathbf{k}\,|\beta_{\mathbf{k}}|^2<\infty`$ and unitary implementability. Point-splitting with the FRW Hadamard parametrix yields $`\langle T_{\mu\nu}\rangle_{\rm ren}`$; conservation $`\nabla^\mu\langle T_{\mu\nu}\rangle_{\rm ren}=0`$ holds at fixed $`k`$

# Summary, Conclusions, and Outlook

## Summary of the MTT$`\to`$QFT construction

In this work we have extended the Modal Triplet Theory (MTT) framework to the full setting of *interacting quantum field theory on curved spacetimes*. The central steps are:

1.  Starting from a coherent modal fixed point $`\Psi^*`$, the projection $`\Pi_{\mathrm{GR}}`$ yields a 4D effective spacetime $`(M,g)`$ with emergent Einstein–Hilbert dynamics and scale-dependent couplings $`G_{\mathrm{eff}}(k)`$, $`\Lambda_{\mathrm{eff}}(k)`$, and matter parameters.

2.  The projection $`\Pi_{\mathrm{QFT}}`$ maps $`(\Psi^*,g)`$ to an algebraic QFT $`(\mathcal{A}(M,g),\omega)`$, where $`\mathcal{A}`$ is the covariant field algebra of the species arising in the $`\Pi_{\mathrm{GR}}`$ reduction, and $`\omega`$ is a Hadamard state determined by the modal coherence phases.

3.  The dynamical evolution of states is implemented by Bogoliubov transformations, unitary on the Fock space whenever the Shale–Stinespring condition is satisfied. In cosmological and stationary backgrounds, this reproduces standard particle interpretation and scattering theory.

4.  Expectation values of the stress–energy tensor are defined by locally covariant point-splitting, ensuring conservation, correct anomaly structure, and renormalisation freedom restricted to geometric tensors. The semiclassical Einstein equation with RG-improved couplings realises the backreaction of quantum matter on the emergent geometry.

5.  The covariant functional RG flow of the effective average action $`\Gamma_k`$ governs the running of both gravitational and matter couplings, embedding the effects of integrating out higher modal excitations at each scale. This provides a unified treatment of low-energy QFT and its UV completion within the MTT paradigm.

## Conceptual implications

The MTT$`\to`$QFT derivation shows that the entire framework of locally covariant quantum field theory, including state selection, renormalisation, and backreaction, can be obtained from modal first principles without additional postulates. In particular:

- The Hadamard condition, essential for renormalisation, emerges from the short-distance modal coherence structure.

- The probabilistic interpretation and particle concept are recovered as limiting descriptions of the unitary modal evolution projected to $`\mathcal{A}(M,g)`$.

- Scale dependence of couplings, usually introduced as an external ingredient, is intrinsic to the MTT projection as a result of integrating out modal scales.

## Observational and experimental prospects

Several avenues exist for testing the predictions of the MTT$`\to`$QFT framework:

1.  **Running couplings in curved backgrounds.** Deviations from constant $`G`$, $`\Lambda`$, or matter couplings in strong curvature environments (early universe, black holes) could reveal the RG imprint of the modal sector.

2.  **Anomaly coefficients.** The scale dependence of trace anomaly coefficients $`a_k`$, $`b_k`$, $`c_k`$ may be probed indirectly through cosmological perturbations or high-energy astrophysical phenomena.

3.  **Vacuum state selection.** The $`\Pi_{\mathrm{QFT}}`$ prescription predicts specific preferred states (e.g. adiabatic vacua) in cosmology; deviations from the Bunch–Davies state might leave imprints in the cosmic microwave background.

4.  **Particle production rates.** In time-dependent backgrounds, the particle creation spectra predicted by the modal-determined Bogoliubov coefficients could be compared to those in standard QFT to constrain the coherence structure.

## Future work

Extensions of the present construction include:

- Full inclusion of nonperturbative matter interactions within the $`\Pi_{\mathrm{QFT}}`$ projection, beyond polynomial truncations.

- Exploration of the asymptotic safety scenario in the joint MTT–QFT RG flow, including the effect of modal topology on fixed point structure.

- Coupling to the MTT$`\to`$GR derivation for a unified quantum gravity framework where both geometry and quantum fields arise from modal dynamics without external inputs.

#### Conclusion.

We have shown that interacting quantum field theory on curved spacetime, with full renormalisation and backreaction, emerges naturally from the modal geometry of MTT through a well-defined projection procedure. This strengthens the case for MTT as a viable unifying framework for fundamental physics, with concrete observational predictions and a clear mathematical path from modal structure to all known low-energy physics.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Foundations*, Zenodo, 2025.

R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*, University of Chicago Press, Chicago, 1994.

M. J. Radzikowski, Micro-local approach to the Hadamard condition in quantum field theory on curved space-time, *Commun. Math. Phys.* **179** (1996), 529–553.

R. Brunetti, K. Fredenhagen, and R. Verch, The generally covariant locality principle: A new paradigm for local quantum physics, *Commun. Math. Phys.* **237** (2003), 31–68.

S. Hollands and R. M. Wald, Local Wick polynomials and time ordered products of quantum fields in curved spacetime, *Commun. Math. Phys.* **223** (2001), 289–326.

S. Hollands and R. M. Wald, Existence of local covariant time ordered products of quantum fields in curved spacetime, *Commun. Math. Phys.* **231** (2002), 309–345.

K. Rejzner, *Perturbative Algebraic Quantum Field Theory*, Mathematical Physics Studies, Springer, Cham, 2016.

D. Shale, Linear symmetries of free boson fields, *Trans. Amer. Math. Soc.* **103** (1962), 149–167.

H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, *Publ. RIMS Kyoto Univ.* **6** (1970), 385–442.

C. Wetterich, Exact evolution equation for the effective potential, *Phys. Lett. B* **301** (1993), 90–94.

J. M. Pawlowski, Aspects of the functional renormalisation group, *Annals Phys.* **322** (2007), 2831–2915.

N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space*, Cambridge Monographs on Mathematical Physics, Cambridge University Press, Cambridge, 1982.

</div>
