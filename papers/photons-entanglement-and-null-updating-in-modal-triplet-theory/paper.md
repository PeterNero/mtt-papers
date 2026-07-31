---
abstract: |
  This paper gives a typed account of photons in Modal Triplet Theory (MTT). The effective spacetime is a four-dimensional Lorentzian manifold $`Y_4`$, while the candidate upper carrier is written $`Y_4\times X_6`$. The internal factor does not by itself select electromagnetism. A photon analysis additionally requires a $`U(1)`$ gauge sector, its Maxwell action or equations, a physical state, and an upper-to-lower encoding map.

  Once the Maxwell sector is supplied, two central statements are exact. The principal symbol of the gauge-reduced Maxwell operator has nonzero physical characteristics only on the metric null cone. For each nonzero null covector in four dimensions, the transverse polarization space modulo gauge is two-dimensional and decomposes into helicities $`+1`$ and $`-1`$. “Null updating” is therefore a useful MTT name for Maxwell characteristic propagation; it is not an independent derivation obtained merely by excluding static or superluminal motion.

  We then separate global quantum structure from local propagation. A state on a local algebra net may be nonfactorizing across regions while spacelike observables commute. Entanglement is consequently compatible with local dynamics and no signaling. Localization and discrete photon records arise through ordinary local couplings and quantum instruments, not through a metaphysically special act of measurement. Gravitational lensing and redshift remain consequences of Maxwell theory on curved spacetime and admit an MTT encoding interpretation only downstream of those equations.

  For horizons, the relevant question is code-relative: can one exterior description recover a declared class of global states and correlations while respecting the dynamics and observable algebra? Hawking thermality is treated as an imported result of quantum field theory on curved spacetime, not derived from projection language alone. The result is a rigorous conditional photon interface and a sharply stated frontier: MTT still needs a same-source upper action that selects the bosonic $`U(1)`$ sector, its state, and its interacting and horizon completions.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: d999dc775645cf2fc04a32bc894b61eb3848aaa1ecaef995547d8b976c684ce7
paper_id: photons-entanglement-and-null-updating-in-modal-triplet-theory
release_state: zenodo_released
released_version: v2
title: |
  **Photons, Entanglement, and Null Updating in Modal Triplet Theory:**
  A Conditional Maxwell-to-Encoding Analysis
zenodo_doi: 10.5281/zenodo.21715791
zenodo_record_id: 21715791
zenodo_url: "https://zenodo.org/records/21715791"
---

# Version 2 revision note

#### Supersedes.

Version 1.0, DOI [10.5281/zenodo.18262340](https://doi.org/10.5281/zenodo.18262340).

#### Reason.

The earlier version used $`Y^4\times B_1\times B_2\times B_3`$, inferred null propagation by excluding static and superluminal updates, treated the two photon helicities as an informal consequence of cost-free rebalancing, and identified a horizon with loss of a global right inverse. Those arguments did not establish the stated conclusions. Noninjective maps can have sections, masslessness alone does not select Maxwell dynamics, and global entanglement must be distinguished from nonlocal propagation.

#### Resolution.

Version 2 uses $`Y_4\times X_6`$, starts from a typed Maxwell input, derives the null characteristic cone and the two-dimensional physical polarization quotient, proves compatibility of nonfactorizing states with local commutativity, and replaces the right-inverse language by code-relative exterior recovery. Lensing, redshift, and Hawking thermality are explicitly downstream of standard local equations.

#### Retained result.

The useful interpretive idea survives: a photon can be represented globally at the state level while its observables and interactions propagate locally. MTT may describe localization, polarization, gravity, and detector records as different lower encodings of one admissible upper configuration, provided the required maps are selected.

#### Remaining boundary.

The selected q79 construction currently supplies a free even CAR net for a twisted-Dirac sector, not a selected bosonic Maxwell/CCR net. A same-source upper action, $`U(1)`$ sector, physical state, interacting completion, detector instrument for general contexts, and horizon recovery or information theorem remain open.

# What is being explained

A photon participates in several mathematical descriptions:

- a classical electromagnetic wave is a solution of Maxwell’s equations;

- a one-photon state is a vector or state in a quantized electromagnetic theory in a regime where a particle interpretation is available;

- a detector click is a local apparatus record;

- polarization labels a two-dimensional physical degree of freedom;

- in curved spacetime, geometric optics follows null rays and quantum field theory may produce observer- or horizon-dependent particle descriptions.

These are related, but they are not interchangeable definitions.

MTT adds another distinction. It separates an upper coherent configuration from the lower encoding accessible in a particular physical context. That separation can organize the preceding descriptions, but it does not remove their mathematical input. In particular, the words “coherence”, “massless”, or “admissible” do not by themselves imply the Maxwell equations.

The objective of this paper is therefore conditional:
``` math
\boxed{
\begin{gathered}
\text{upper carrier and encoding}\\
+\ \text{Maxwell/quantum input}\\
\Downarrow\\
\text{null characteristics, two helicities, local observables}\\
\Downarrow\\
\text{MTT interpretation of global states, records, and restricted views}.
\end{gathered}}
```
The first downward implication contains exact mathematics. The second is an interpretation theorem only where the required encoding maps intertwine the standard structures.

# The typed photon record

## Upper and lower spaces

Write the candidate MTT carrier as
``` math
\begin{equation}
\mathfrak M=Y_4\times X_6,
\label{eq:carrier}
\end{equation}
```
where $`Y_4`$ is oriented and time-oriented Lorentzian spacetime and $`X_6`$ is the selected or candidate internal geometry. The notation does not multiply manifold dimensions through a $`3\times3`$ argument, nor does it identify compact circle phase with physical time.

Let $`\Pi_{\mathrm{adm}}`$ denote an admissible-sector map on a declared domain and let
``` math
P:\Pi_{\mathrm{adm}}\mathcal U\longrightarrow\mathcal A
```
be an upper-to-lower encoding into an effective observable theory. Neither map is assumed invertible. In a concrete photon construction, $`P`$ must preserve gauge equivalence, local support, dynamics, and the state or correlation function being discussed.

## Data that cannot be hidden

<div class="definition">

**Definition 1** (Photon interface record). A photon interface record is a tuple
``` math
\mathfrak R_\gamma=
(Y_4,g,\mathcal U,\Pi_{\mathrm{adm}},P,
\mathcal A_{\mathrm{em}},S_{\mathrm{Max}},\omega,\mathfrak I)
```
with:

1.  a globally hyperbolic effective spacetime $`(Y_4,g)`$, or a declared local/asymptotic substitute;

2.  an upper configuration space $`\mathcal U`$, admissible domain, and encoding $`P`$;

3.  a $`U(1)`$ gauge field or gauge-invariant Maxwell algebra $`\mathcal A_{\mathrm{em}}`$;

4.  the source-free Maxwell action
    ``` math
    S_{\mathrm{Max}}[A]=-\frac14\int_{Y_4}
    F_{\mu\nu}F^{\mu\nu}\,\mathrm{vol}_g,
    \qquad F=\mathrm{d}A,
    ```
    or an equivalent equation-of-motion record;

5.  a quantum state $`\omega`$, when quantum claims are made; and

6.  a local coupling or instrument $`\mathfrak I`$, when detector records are discussed.

</div>

This definition prevents three common shortcuts. A field equation does not select a state. A state does not select a detector. An internal geometry does not select a $`U(1)`$ action unless an explicit source map is proved.

<div class="proposition">

**Proposition 2** (Intertwining requirement). *Suppose an upper linearized mode $`u\in\mathcal U`$ is called a photon because $`P u=A`$. The name is dynamically justified on a domain only if
``` math
P\,D_{\mathcal U}u=D_{\mathrm{Max}}\,Pu,
\label{eq:intertwine}
```
modulo gauge, and if $`P`$ preserves the relevant local support and state pairings. Equality of dimensions or a resemblance between internal orientations and polarization does not imply <a href="#eq:intertwine" data-reference-type="eqref" data-reference="eq:intertwine">[eq:intertwine]</a>.*

</div>

<div class="proof">

*Proof.* Without the intertwining identity, an upper solution need not map to a Maxwell solution. Without gauge compatibility, two equivalent lower potentials may be assigned inequivalent upper data. Without support and state compatibility, the map does not preserve local observables or correlations. These are necessary typing conditions, independent of any interpretation. ◻

</div>

# Why Maxwell photons propagate on the null cone

## Field strength and potential

In vacuum the gauge-invariant field strength obeys
``` math
\begin{equation}
\mathrm{d}F=0,\qquad \delta_g F=0.
\label{eq:maxwell}
\end{equation}
```
Locally $`F=\mathrm{d}A`$, with gauge equivalence
``` math
A\sim A+\mathrm{d}\lambda.
```
For the potential, the equation is $`\delta_g\mathrm{d}A=0`$. In Lorenz gauge $`\delta_g A=0`$, its principal part is the normally hyperbolic wave operator. Quantization on globally hyperbolic manifolds and the topological qualifications of the Maxwell field are standard subjects in curved-spacetime QFT .

## The characteristic calculation

Let $`x\in Y_4`$ and let $`0\ne k\in T_x^*Y_4`$. For a covector amplitude $`a\in T_x^*Y_4\otimes\mathbb C`$, the principal symbol of $`\delta_g\mathrm{d}`$, up to an irrelevant overall sign, is
``` math
\begin{equation}
\sigma_{\delta\mathrm{d}}(k)a
=g^{-1}(k,k)a-k\,g^{-1}(k,a).
\label{eq:symbol}
\end{equation}
```
Gauge amplitudes are multiples of $`k`$.

<div id="thm:maxwell-characteristic" class="theorem">

**Theorem 3** (Maxwell characteristic and polarization theorem). *For the source-free Maxwell potential on a four-dimensional Lorentzian spacetime:*

1.  *nonzero physical characteristic amplitudes occur only when $`g^{-1}(k,k)=0`$;*

2.  *for a nonzero null covector $`k`$, the physical polarization space is
    ``` math
    \mathcal P_k=
    \frac{\{a\in T_x^*Y_4\otimes\mathbb C:
    g^{-1}(k,a)=0\}}{\mathbb Ck};
    \label{eq:polarization}
    ```*

3.  *$`\dim_{\mathbb C}\mathcal P_k=2`$; after choosing orientation, the transverse rotation group decomposes $`\mathcal P_k`$ into weights $`+1`$ and $`-1`$, the two photon helicities.*

</div>

<div class="proof">

*Proof.* Use gauge freedom to impose $`g^{-1}(k,a)=0`$. Equation <a href="#eq:symbol" data-reference-type="eqref" data-reference="eq:symbol">[eq:symbol]</a> then reduces to
``` math
g^{-1}(k,k)a=0.
```
If $`k`$ is nonnull, the only transverse characteristic amplitude is zero. Thus a nonzero physical characteristic requires $`k`$ null.

For null $`k`$, its orthogonal complement $`k^\perp`$ in the complexified four-dimensional cotangent space has dimension three and contains $`\mathbb Ck`$. Quotienting by this gauge line gives $`\dim_\mathbb C\mathcal P_k=3-1=2`$. The little-group rotation on the transverse plane is $`SO(2)`$. Complexifying its real two-dimensional representation gives one-dimensional weight spaces with weights $`+1`$ and $`-1`$. These are the helicity representations. ◻

</div>

The representation-theoretic part is the familiar massless spin-one content of Wigner’s classification . The theorem does not say that every massless mode is a photon. It says that a supplied Maxwell gauge mode has null characteristics and two physical polarizations.

<div class="corollary">

**Corollary 4** (Correct meaning of null updating). *On a domain where <a href="#eq:intertwine" data-reference-type="eqref" data-reference="eq:intertwine">[eq:intertwine]</a> holds, an upper MTT mode mapped to the Maxwell sector has lower characteristic covectors on the null cone and exactly the Maxwell physical polarization quotient. “Null updating” may name this transported characteristic structure, but it does not replace the Maxwell input.*

</div>

## Geometric optics

For a rapidly varying field with phase $`S`$, let $`k_\mu=\nabla_\mu S`$. The leading Maxwell equation gives
``` math
g^{\mu\nu}k_\mu k_\nu=0.
```
Because $`k`$ is a gradient,
``` math
k^\nu\nabla_\nu k_\mu
=k^\nu\nabla_\mu k_\nu
=\frac12\nabla_\mu(k^\nu k_\nu)=0.
```
Thus the rays are affinely parametrized null geodesics at leading geometric-optics order. Finite-wavelength and polarization corrections may require additional analysis; the leading null-ray statement should not be inflated into an exact point-particle ontology.

# Global quantum states and local propagation

## Two different uses of the word global

A classical Maxwell solution can have extended support. A quantum state can also fail to factor across spatial regions. Neither statement means that a signal or causal influence propagates instantaneously.

Let $`O\mapsto\mathcal A(O)`$ be a net of observable algebras. Locality requires
``` math
\begin{equation}
[\mathcal A(O_1),\mathcal A(O_2)]=0
\quad\text{when }O_1\text{ and }O_2\text{ are spacelike separated}.
\label{eq:locality}
\end{equation}
```
A state $`\omega`$ is a positive normalized functional on the global algebra. It may be entangled or nonfactorizing across $`\mathcal A(O_1)`$ and $`\mathcal A(O_2)`$. This coexistence is ordinary AQFT, not a new form of superluminal dynamics .

<div id="prop:no-signaling" class="proposition">

**Proposition 5** (Nonfactorization is compatible with no signaling). *Let $`O_1`$ and $`O_2`$ be spacelike separated and let $`U\in\mathcal A(O_1)`$ be unitary. For every $`B\in\mathcal A(O_2)`$ and every state $`\omega`$,
``` math
\omega(U^*BU)=\omega(B).
```
The conclusion does not require $`\omega`$ to factor across the two regions.*

</div>

<div class="proof">

*Proof.* Locality gives $`UB=BU`$. Hence $`U^*BU=B`$, and applying the state gives the identity. ◻

</div>

This is the precise reconciliation needed by the MTT language. The upper or global encoding may carry correlations across the whole preparation. The lower observable net still has local commutativity and causal propagation.

## What a one-photon state means

In Minkowski space or an asymptotically stationary regime, a one-photon state is built from the one-particle subspace of the quantized Maxwell field. Its wave packet may be spread over many positions, momenta, and polarizations. In a general curved or time-dependent spacetime there may be no preferred global particle decomposition. The local algebra and state remain meaningful even when “the photon number” does not.

MTT may represent such a state by one admissible upper configuration whose projections into different local contexts are not independent. This is a structural encoding proposal. To become a theorem, the upper state, lower Maxwell algebra, and correlation-preserving map must be constructed from the same source.

## Virtual photons

Internal photon lines in perturbation theory are propagator terms, not on-shell one-photon states. They need not satisfy the on-shell characteristic relation individually. Calling them “temporary violations” or literal particles moving off the light cone is misleading. In the MTT interface they belong to the chosen gauge-fixed perturbative presentation and inherit its regime and renormalization dependencies.

# Localization, detection, and wave–particle language

## Measurement is a physical interaction

No conscious observer is needed to localize a photon record. A detector couples locally to the electromagnetic field and produces a stable macroscopic output. Operationally, an outcome-resolved quantum instrument is a family of completely positive maps $`\{\mathcal I_i\}`$ such that $`\sum_i\mathcal I_i`$ is trace preserving. For a state $`\rho`$,
``` math
p_i=\operatorname{Tr}\mathcal I_i(\rho),\qquad
\rho_i'=\frac{\mathcal I_i(\rho)}{p_i}
\quad(p_i>0).
```
The coupling, probability law, conditional state, and record stability are distinct parts of the physical process .

An extended state can therefore produce a localized detector record without having been a tiny localized object before the interaction. This is not unique to MTT. MTT’s additional task is to derive the instrument or transition-completion kernel from its upper dynamics. At present that general source theorem remains open.

## Wave and particle are output descriptions

The wave description concerns field amplitudes, correlations, and interference. The particle description concerns quantized excitations, energy-momentum transfer, and discrete records. A single experiment can require both descriptions at different stages:
``` math
\text{preparation and propagation}
\longrightarrow
\text{local coupling}
\longrightarrow
\text{outcome record}.
```
MTT can encode this as one upper history with several valid lower descriptions. It should not claim that a change of vocabulary alone derives the Born probabilities or selects one individual outcome.

# Polarization and the shared-circle proposal

The two helicities were derived in <a href="#thm:maxwell-characteristic" data-reference-type="ref+Label" data-reference="thm:maxwell-characteristic">3</a> from four-dimensional Maxwell gauge structure. They must not be counted a second time as independent internal dimensions.

The MTT shared-circle proposal may nevertheless be relevant. A common line bundle $`L_{\mathrm{shared}}`$ with connection can carry phase or holonomy information through several upper sectors. To identify this phase with photon helicity, one needs a connection-preserving intertwiner
``` math
\begin{CD}
\text{upper shared-line/helicity carrier}
@>{D_{\mathcal U}}>>
\text{upper carrier}\\
@V{P}VV @VV{P}V\\
\mathcal P_k @>{D_{\mathrm{Max}}}>>
\mathcal P_k
\end{CD}
```
that maps the circle action to the transverse $`SO(2)`$ action with weights $`\pm1`$. Isomorphic circles are not enough; their connections, holonomies, domains, and dynamics must agree.

This observation gives the shared circle a testable role without identifying it with compact physical time. The decisive calculation is not another dimension count. It is the construction of the commuting map and the demonstration that no extra longitudinal mode survives.

# Lensing and redshift

## What the standard equations already imply

At geometric-optics order, the wave covector $`k`$ follows a null geodesic. Gravitational lensing is the comparison of these null curves between source, lens, and observer in the curved metric. For an observer with four-velocity $`u`$, the measured frequency is
``` math
\begin{equation}
\omega_{\mathrm{obs}}=-g(u,k).
\label{eq:frequency}
\end{equation}
```
If emitter and receiver have four-velocities $`u_e,u_r`$, then
``` math
1+z=\frac{\omega_e}{\omega_r}
=\frac{-g(u_e,k_e)}{-g(u_r,k_r)}.
```
This formula includes gravitational, Doppler, and cosmological contributions according to the spacetime and observers. No statement that the photon “loses intrinsic energy” is required.

## The legitimate MTT reading

MTT may say that the same upper coherence class is encoded relative to different local frames and metric regions. Lensing then reads as transport of the lower null direction, while redshift reads as a change in the observer-dependent pairing <a href="#eq:frequency" data-reference-type="eqref" data-reference="eq:frequency">[eq:frequency]</a>. This is a useful unification of descriptions, but it is downstream of Maxwell and Einstein geometry. It does not independently derive the metric, the null geodesic equation, or the redshift law.

The current MTT gravity program contains controlled and conditional Einstein-sector bridges at declared tiers. Until the selected upper action and physical continuum intertwiner are complete, the photon paper must use a supplied $`g`$, not claim to generate it.

# Horizons, exterior encodings, and thermality

## Restriction is not recovery

Let $`\mathcal A_{\mathrm{glob}}`$ be a global observable algebra and $`\mathcal A_{\mathrm{ext}}\subset\mathcal A_{\mathrm{glob}}`$ the algebra accessible to an exterior observer. Restriction sends a global state $`\omega`$ to
``` math
r(\omega)=\omega|_{\mathcal A_{\mathrm{ext}}}.
```
Fix a declared code $`\mathcal C`$ of global states. An exact exterior decoder on $`\mathcal C`$ would be a physically allowed map $`D`$ satisfying
``` math
D(r(\omega))=\omega
\qquad(\omega\in\mathcal C).
\label{eq:decoder}
```
Such a decoder requires $`r`$ to be injective on $`\mathcal C`$, as well as positivity, algebraic compatibility, and whatever causal or dynamical conditions the physical problem imposes.

The earlier statement that noninjectivity forbids a right inverse was too coarse. A surjection may have a section that chooses one representative. What fails after two code states acquire the same exterior restriction is recovery of both original states. This code-relative criterion is developed in the corrected MTT shadow-bridge paper .

## What a horizon may mean in MTT

An MTT horizon interpretation can therefore be stated carefully:

> A horizon-like encoding boundary occurs on a declared state code when no single lower exterior representation preserves and recovers all of the global correlations required by that code while remaining compatible with the local dynamics.

This is not yet a theorem identifying every geometric event horizon with an MTT projector failure. Local physics can remain regular across a horizon, and different observer algebras can be valid on different domains.

## Hawking radiation remains an imported result

Quantum field theory on black-hole spacetimes yields Hawking particle creation and, under stationary horizon hypotheses, thermal or KMS properties tied to the surface gravity . In units $`c=\hbar=k_B=1`$, the idealized temperature is
``` math
T_H=\frac{\kappa}{2\pi},
```
with greybody factors and field-spin effects entering the flux observed at infinity.

Restriction to an exterior algebra is compatible with an interpretation in terms of lost access to correlations. It does not, by itself, derive the KMS state, Bogoliubov coefficients, greybody factors, or temperature. Nor does it solve the black-hole information problem. A full MTT claim would need one upper state and dynamics whose exterior restriction reproduces the Hawking state and whose global evolution has a proved information and recovery property.

# Time and the photon

A null curve has zero proper-time interval:
``` math
\mathrm{d}\tau^2=-g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu=0.
```
This geometrical fact does not mean that a photon “experiences no time” in a mathematically defined subjective sense. Quantum states and fields are still related by spacetime translations, local dynamics, or algebraic automorphisms, and detectors have timelike clocks.

MTT may reserve “closure time” or “rebalancing time” for an upper ordering variable, but it must then define that variable and its map to physical time. The shared compact circle may encode phase or holonomy; physical Lorentzian time is noncompact unless an explicit lift and quotient theorem says otherwise. Keeping these notions distinct avoids turning a useful phase structure into a false spacetime identification.

# Current MTT status

<div class="center">

| Object | Status | Meaning for this paper |
|:---|:---|:---|
| $`Y_4\times X_6`$ notation | Adopted carrier form | Separates effective spacetime from the six-dimensional internal candidate; does not select photon dynamics. |
| Maxwell characteristic cone | Exact, standard | Null propagation follows once the Maxwell sector and Lorentzian metric are supplied. |
| Two photon helicities | Exact, standard | They are the two-dimensional transverse quotient modulo gauge. |
| Global state/local net compatibility | Exact, standard | Entanglement or nonfactorization does not violate local commutativity. |
| Selected q79 free even CAR net | Closed at its tier | This is a fermionic twisted-Dirac construction, not the missing bosonic Maxwell/CCR source. |
| MTT Maxwell/CCR source | Open | Requires a same-source $`U(1)`$ action, gauge quotient, state, and continuum/local-net construction. |
| General detector completion | Open | The physical instrument and Born-compatible source are not selected for every apparatus context. |
| Hawking thermality | Imported | Standard QFT on curved spacetime supplies the result; MTT currently gives an interpretation and recovery contract, not a derivation. |

</div>

This table matters because the fermionic CAR success cannot silently stand in for a bosonic photon theorem. It is evidence that the broader source-to-local-net strategy can work, but the Maxwell branch needs its own selected construction. The selected CAR theorem and the distinction between commutative output measures and a noncommutative field algebra are documented in the companion QFT papers .

# What the corrected paper proves

The logical output can be summarized as follows.

<div id="thm:conditional-photon" class="theorem">

**Theorem 6** (Conditional MTT photon-encoding theorem). *Assume a photon interface record $`\mathfrak R_\gamma`$ for which:*

1.  *the lower field obeys source-free Maxwell dynamics on $`Y_4`$;*

2.  *the upper-to-lower map intertwines dynamics and gauge equivalence;*

3.  *the local observable net satisfies spacelike commutativity; and*

4.  *any claimed detector or exterior record is supplied by its declared instrument or restriction map.*

*Then:*

1.  *lower physical characteristics are null and have two helicities;*

2.  *global nonfactorizing states remain compatible with local propagation and no signaling;*

3.  *localized photon records are outputs of local physical instruments, not evidence for a pre-existing sharply localized photon;*

4.  *lensing and redshift can be read as context-dependent encodings of standard Maxwell transport; and*

5.  *a horizon claim reduces to a declared exterior recovery problem, while Hawking thermality still requires the standard curved-spacetime quantum input or a new same-source derivation.*

</div>

<div class="proof">

*Proof.* Part (a) is <a href="#thm:maxwell-characteristic" data-reference-type="ref+Label" data-reference="thm:maxwell-characteristic">3</a>. Part (b) is <a href="#prop:no-signaling" data-reference-type="ref+Label" data-reference="prop:no-signaling">5</a>. Part (c) follows from the definition of the instrument and the separation between premeasurement state and record. Part (d) follows from the eikonal and frequency formulas. Part (e) follows from the code-relative decoder condition <a href="#eq:decoder" data-reference-type="eqref" data-reference="eq:decoder">[eq:decoder]</a> and the independent hypotheses of the Hawking/KMS construction. ◻

</div>

<div class="remark">

*Remark 7* (What is conditional). The theorem organizes and transports supplied structures. It does not select the Maxwell action, the upper photon mode, the state, the instrument, or the black-hole quantum state. Those are precisely the objects that a stronger MTT source theorem must emit.

</div>

# Research program

The corrected frontier has a natural order.

1.  **Select the bosonic source.** Construct a $`U(1)`$ connection and Maxwell quadratic action from the same q79 upper geometry used by the accepted lower carrier.

2.  **Prove the continuum intertwiner.** Show that the upper linearized Hessian descends to the Maxwell operator with its gauge complex, local support, and two-dimensional physical quotient.

3.  **Build the CCR/Weyl net.** Quantize the selected symplectic space and prove locality, covariance, and time-slice properties, including topological sectors.

4.  **Select a state.** Provide a Hadamard state or declared state class from the same source. Dynamics alone does not choose it.

5.  **Connect the shared circle.** Prove that $`L_{\mathrm{shared}}`$, with connection and holonomy, maps to the helicity action rather than merely having an isomorphic $`U(1)`$.

6.  **Derive records.** Construct the detector coupling and outcome-resolved instrument, retaining the existing distinction among disturbance, outcome completion, and stabilization.

7.  **Test horizons separately.** State the global code, exterior algebra, restriction channel, recovery criterion, state, and error bounds; then compare with Hawking/KMS observables.

These steps would turn the present conditional interface into a selected photon theorem. Repeating the words “global coherence” or fitting a known photon formula would not.

# Discussion

## What remains distinctive

The corrected paper does not compete with Maxwell theory by proposing a different speed of light or a third polarization. Its distinctive idea is architectural: local particle, wave, detector, and exterior descriptions may be projections of one upper coherent object, and the validity of each description is controlled by an explicit map and domain.

This is useful because it makes several conceptual confusions visible. An extended quantum state is not a superluminal signal. A detector click is not proof that the incoming excitation was sharply localized. A section of a projection is not recovery of the original state. A thermal exterior description is not yet a derivation of Hawking radiation. A compact phase circle is not automatically time.

## What would count as a major advance

The major advance would be one commuting same-source diagram:
``` math
\begin{gathered}
\text{q79 upper line/bundle and action}\\
\downarrow\\
\text{Maxwell gauge complex and symplectic space on }Y_4\\
\downarrow\\
\text{CCR/Weyl local net and selected state}\\
\downarrow\\
\text{detector and horizon restrictions}.
\end{gathered}
```
If its connections, Hessians, holonomies, local supports, and states were preserved, <a href="#thm:conditional-photon" data-reference-type="ref+Label" data-reference="thm:conditional-photon">6</a> would promote from a conditional interface to a selected MTT result.

# Conclusion

The photon is not derived by declaring a massless coherence mode and discarding every propagation speed except $`c`$. The rigorous route is more informative. Maxwell gauge dynamics has a null principal characteristic set. Its physical transverse quotient has dimension two and carries helicities $`+1`$ and $`-1`$. Quantization permits global nonfactorizing states while the local observable net remains causal. Local interactions and instruments create detector records. Curved spacetime Maxwell theory supplies lensing and redshift, and curved-spacetime QFT supplies Hawking thermality under its own hypotheses.

MTT can unify these descriptions through an upper-to-lower encoding language, but only where the relevant maps are constructed. The present paper proves the conditional interface and removes several false shortcuts. The remaining scientific target is now precise: select the bosonic $`U(1)`$ action, Maxwell complex, CCR/Weyl net, state, and apparatus or horizon maps from one upper q79 source.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The Maxwell characteristic, polarization, locality, and recovery statements in this paper are analytic and do not depend on numerical fitting. The curated [MTT Results Reproduction repository](https://github.com/PeterNero/mtt-results-repro) supplies current MTT status context. The mapped `A04/final_12_of_12_audit` row is profile-replay evidence for the embedded renormalized Standard Model, while `A05/strict_upgrade_ledger` records stronger source obligations that remain open. Neither row proves a selected Maxwell/CCR photon source. Exact tier labels, artifacts, and source hashes are retained in the repository.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
