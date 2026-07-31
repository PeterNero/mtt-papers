---
abstract: |
  This paper examines a concrete MTT proposal: localized persistent structures may be represented as coherence basins, while their effective motion may be described by capacity-dependent forces. The basin part is viable only after a map from effective state space to spatial observables is supplied; distinct basins need not have distinct spatial densities. The force part requires still more structure. A gradient of a diagnostic admissibility margin is not a force until a selected action, Hamiltonian, stress law, or constitutive equation couples that margin to motion. We derive the exact centroid balance law for a localized density and show how Newtonian and Lorentz equations follow conditionally from a declared effective action. The integrated basin weight equals inertial mass only when the kinetic term is normalized accordingly. Gauge charge conservation requires a symmetry or transported representation label, not basin persistence alone. Confinement follows from a capacity interpretation only after a coercive separation energy is proved; an area law does not follow from qualitative “strain.” The result is a rigorous effective-particle and force-encoding framework. It preserves coherence basins as a useful model proposal while leaving the selected MTT action, constitutive map, physical masses, interaction laws, and gravitational coupling open.
author:
- Peter Nero
current_version: v3
date: July 2026, Version 3
generated_from_main_tex_sha256: 4925b8cfecd02875f040021f3baf7230f5b2243f43b2c8993153a58b3ddeef54
paper_id: particles-and-forces-as-coherence-basins-and-capacity-gradients
release_state: zenodo_released
released_version: v3
title: |
  **Particles and Forces as Conditional Coherence-Basin Encodings:**
  Effective actions, centroid laws, and the limits of capacity gradients
zenodo_doi: 10.5281/zenodo.21719055
zenodo_record_id: 21719055
zenodo_url: "https://zenodo.org/records/21719055"
---

# Version 3 Revision Note

<div class="description">

Version 2.0, released in January 2026.

The previous version identified a diagnostic capacity gradient with force, identified integrated density with mass, and claimed Newtonian, Lorentz, confinement, charge, and gravity results without deriving the action or constitutive laws that generate them.

Version 3 defines a complete effective-particle record, proves the exact centroid balance law, gives a reparameterization no-go for bare capacity gradients, and derives conditional force laws from a declared effective action. It replaces the confinement and conservation claims by their correct conditional statements.

Stable localized basins remain candidate effective particle encodings, and capacity may enter interaction potentials or stress laws when a selected source map assigns it that role.

MTT has not yet selected the upper action, spatial observation map, kinetic normalization, capacity-to-potential map, physical mass spectrum, transition law, or universal gravitational coupling.

</div>

# The proposal and its logical layers

The intuitive proposal is attractive. A physical particle is not observed as an abstract point with no internal structure; it is recognized through persistence, localization, charges, and reproducible responses. A stable region of an effective state space can model persistence. A localized density can model position. An internal representation can model charge. A selected action can model response to fields. Taken together, these ingredients form a credible effective-particle record.

They do not follow from one another automatically. In particular:

1.  a basin in state space is not yet a region of physical space;

2.  a spatial density is not yet a mass density;

3.  a scalar margin is not yet an energy;

4.  a gradient is not yet a force;

5.  a persistent label is not automatically a conserved Noether charge;

6.  a growing diagnostic cost is not yet confinement or a Wilson-loop area law.

The purpose of this revision is to keep these types separate and then prove the bridges that can actually be proved. The final result is conditional, but it is operational: every missing physical statement is attached to a specific source row rather than absorbed into the word “coherence.”

## Status language

<div id="def:status" class="definition">

**Definition 1** (Encoding, dynamics, and selection). An *encoding* is a typed representation of one effective object by another. A *dynamical model* supplies an action, generator, balance law, or constitutive evolution. A *selected MTT derivation* additionally proves that those data descend from one accepted upper source without fitting the target behavior.

</div>

This paper closes several encoding-level and conditional dynamical statements. It does not claim the final selected derivation.

# From an effective basin to a spatial particle

## Invariant basins

Let $`\mathcal{Y}`$ be an effective state space on a declared time slab, with evolution $`\Phi_{t,s}`$ wherever that evolution is defined.

<div id="def:basin" class="definition">

**Definition 2** (Stable coherence basin). A set $`\mathcal{B}_\alpha\subset\mathcal{Y}`$ is a stable coherence basin on $`[t_0,t_1]`$ if:

1.  it is invariant on the slab: $`\Phi_{t,s}(\mathcal{B}_\alpha)\subseteq\mathcal{B}_\alpha`$;

2.  nearby allowed states are attracted or remain controlled according to a specified stability estimate;

3.  the basin remains separated from competing basins by a declared positive margin on the controlled domain.

</div>

This definition captures persistence in state space. It says nothing yet about spatial localization, spin, statistics, energy, or particle detection.

## The observation map

Let $`\Sigma`$ be a physical or effective spatial slice. A spatial representation requires a map
``` math
\mathcal{O}_t:\mathcal{Y}\longrightarrow \mathcal{M}_+(\Sigma)\times\mathcal{J}(\Sigma),
```
where $`\mathcal{M}_+(\Sigma)`$ is a class of positive finite measures or densities and $`\mathcal{J}(\Sigma)`$ is a class of currents. Write
``` math
\mathcal{O}_t(y)=(\rho_y(\,\cdot\,,t),j_y(\,\cdot\,,t)).
```
The map, its regularity, and its physical meaning are additional data.

<div id="prop:noninjective" class="proposition">

**Proposition 3** (Spatial identity does not follow from basin identity). *Distinct invariant basins can have identical spatial density histories.*

</div>

<div class="proof">

*Proof.* Let $`\mathcal{Y}=\mathcal{D}\times\{-1,+1\}`$, let the evolution preserve the second coordinate, and let
``` math
\mathcal{B}_\pm=\mathcal{D}\times\{\pm1\}.
```
Define $`\mathcal{O}_t(\rho,\sigma)=(\rho,j_\rho)`$ independently of $`\sigma`$. Then $`\mathcal{B}_+`$ and $`\mathcal{B}_-`$ are distinct invariant basins but have the same image under $`\mathcal{O}_t`$. Thus the spatial observation map need not be injective. ◻

</div>

The proposition withdraws the earlier claim that an effective density uniquely tracks basin identity. Hidden spin, flavor, gauge, or topological labels may be invisible to a chosen density observable. A complete particle record must carry them separately.

<div id="def:particle-record" class="definition">

**Definition 4** (Effective particle record). An effective particle record on a slab is
``` math
\mathfrak{P}_\alpha
 =
 (\mathcal{B}_\alpha,\mathcal{O},\rho_\alpha,j_\alpha,
  \Pi_\alpha,b_\alpha,S_{\mathrm{eff}},
  \mathcal{R}_\alpha,\varepsilon_\alpha),
```
where:

1.  $`\mathcal{B}_\alpha`$ is a stable basin;

2.  $`(\rho_\alpha,j_\alpha)`$ is its selected spatial image;

3.  $`\Pi_\alpha`$ is a momentum-flux or stress tensor;

4.  $`b_\alpha`$ is a body-force density or source term;

5.  $`S_{\mathrm{eff}}`$ is an effective action, or a declared constitutive replacement sufficient to determine $`\Pi_\alpha`$ and $`b_\alpha`$;

6.  $`\mathcal{R}_\alpha`$ contains internal representation and charge data;

7.  $`\varepsilon_\alpha`$ records approximation and slab errors.

</div>

A basin is therefore the persistence component of a particle model, not the entire particle theorem.

# Exact centroid mechanics

## Balance assumptions

Assume $`\rho\geq0`$, $`j=\rho v`$, and sufficient integrability on a fixed region $`\Omega\subset\Sigma`$. Define
``` math
M(t)=\int_\Omega \rho\,\mathrm{d}x,\qquad
 X^i(t)=\frac{1}{M(t)}\int_\Omega x^i\rho\,\mathrm{d}x,\qquad
 P^i(t)=\int_\Omega \rho v^i\,\mathrm{d}x.
```
Suppose
``` math
\begin{align}
 \partial_t\rho+\partial_j(\rho v^j)&=0,
 \label{eq:continuity}\\
 \partial_t(\rho v^i)+\partial_j\Pi^{ij}&=b^i.
 \label{eq:momentum}
\end{align}
```
These are dynamical or constitutive assumptions. A smooth density representation alone does not imply them.

<div id="thm:centroid" class="theorem">

**Theorem 5** (Exact centroid balance). *If the mass flux through $`\partial\Omega`$ vanishes and $`M>0`$, then $`M`$ is constant and
``` math
\begin{align}
 M\dot X^i&=P^i,\label{eq:first-moment}\\
 M\ddot X^i
 &=\int_\Omega b^i\,\mathrm{d}x
   -\int_{\partial\Omega}\Pi^{ij}n_j\,\mathrm{d}S.
 \label{eq:centroid}
\end{align}
```*

</div>

<div class="proof">

*Proof.* Integrating <a href="#eq:continuity" data-reference-type="ref+label" data-reference="eq:continuity">[eq:continuity]</a> gives $`\dot M=-\int_{\partial\Omega}\rho v\cdot n\,\mathrm{d}S=0`$. Multiplying <a href="#eq:continuity" data-reference-type="ref+label" data-reference="eq:continuity">[eq:continuity]</a> by $`x^i`$, integrating by parts, and using the same boundary condition gives <a href="#eq:first-moment" data-reference-type="ref+label" data-reference="eq:first-moment">[eq:first-moment]</a>. Integrating <a href="#eq:momentum" data-reference-type="ref+label" data-reference="eq:momentum">[eq:momentum]</a> and applying the divergence theorem gives
``` math
\dot P^i
 =\int_\Omega b^i\,\mathrm{d}x
  -\int_{\partial\Omega}\Pi^{ij}n_j\,\mathrm{d}S.
```
Differentiating <a href="#eq:first-moment" data-reference-type="ref+label" data-reference="eq:first-moment">[eq:first-moment]</a> completes the proof. ◻

</div>

This theorem is stronger and clearer than the former narrow-basin argument. It identifies the force on the centroid as the integrated body source plus the boundary traction. The equation does not say where those terms come from.

<div id="cor:narrow" class="corollary">

**Corollary 6** (Controlled point-particle approximation). *Suppose the boundary traction vanishes and $`b^i(x,t)=\rho(x,t)a^i(x,t)`$, with $`a(\,\cdot\,,t)`$ Lipschitz on the basin support with constant $`L_a(t)`$. Then
``` math
\left|
 M\ddot X^i-Ma^i(X,t)
 \right|
 \leq
 L_a(t)\int_\Omega |x-X|\,\rho(x,t)\,\mathrm{d}x.
```*

</div>

<div class="proof">

*Proof.* Subtract $`Ma^i(X,t)`$ from the volume term in <a href="#eq:centroid" data-reference-type="ref+label" data-reference="eq:centroid">[eq:centroid]</a> and apply the Lipschitz bound. ◻

</div>

Newtonian form is therefore a controlled localized limit of an already specified momentum law. It is not generated by localization alone.

# Why a capacity gradient is not yet a force

Let $`C:\Sigma\to\mathbb{R}`$ be a normalized diagnostic margin. Its zero set may mark loss of admissibility, and its sign may rank distance from a chosen boundary. Neither fact supplies dimensions of energy or a coupling to motion.

<div id="prop:reparam" class="proposition">

**Proposition 7** (Reparameterization obstruction). *Let $`\phi`$ be strictly increasing with $`\phi(0)=0`$. Then $`C`$ and $`\widetilde C=\phi\circ C`$ have the same sign and zero set, but
``` math
\nabla\widetilde C=\phi'(C)\nabla C.
```
Consequently a force rule $`F=-\nabla C`$ is not invariant under admissibility- preserving reparameterization of the diagnostic.*

</div>

<div class="proof">

*Proof.* Monotonicity preserves the sign and zero set. The gradient identity is the chain rule. Unless $`\phi'(C)=1`$, the proposed force changes. ◻

</div>

The obstruction is decisive because capacity diagnostics often admit equivalent monotone normalizations. A physical force can still depend on capacity, but the theory must select both a representative and a coupling law.

<div id="def:promotion" class="definition">

**Definition 8** (Capacity-to-dynamics promotion). A capacity-to-dynamics promotion consists of:

1.  a fixed normalized capacity representative $`C`$;

2.  an effective action, Hamiltonian, stress law, or mobility law;

3.  a dimensionful constitutive map, for example $`V_C=G(C)`$;

4.  boundary conditions and a solution concept;

5.  a source theorem or calibration rule for every coefficient;

6.  an error budget and declared domain of validity.

</div>

With $`V_C=G(C)`$ selected, the conservative capacity contribution becomes
``` math
F_C=-\nabla V_C=-G'(C)\nabla C.
```
Under $`C\mapsto\phi(C)`$, the same physical potential is preserved only if the constitutive function transforms to $`G\circ\phi^{-1}`$. The invariant object is the selected potential, not the bare diagnostic gradient.

# Conditional Newton and Lorentz equations

## A declared effective action

Consider one localized basin with centroid $`X(t)`$ on a Riemannian spatial chart, inertial coefficient $`m_I>0`$, scalar potential $`\Phi`$, connection $`A_i`$, representation label $`q`$, and capacity potential $`V_C`$. Take
``` math
\begin{equation}
\label{eq:lagrangian}
 L_{\mathrm{eff}}
 =
 \frac12m_I g_{ij}(X)\dot X^i\dot X^j
 +qA_i(X,t)\dot X^i
 -q\Phi(X,t)-V_C(X,t).
\end{equation}
```

<div id="thm:force" class="theorem">

**Theorem 9** (Conditional force law). *The Euler–Lagrange equations of <a href="#eq:lagrangian" data-reference-type="ref+label" data-reference="eq:lagrangian">[eq:lagrangian]</a> give
``` math
m_I\frac{D\dot X^i}{\mathrm{d}t}
 =
 q\bigl(E^i+F^i{}_j\dot X^j\bigr)
 -\nabla^iV_C,
```
where
``` math
F_{ij}=\partial_iA_j-\partial_jA_i,
 \qquad
 E_i=-\partial_i\Phi-\partial_tA_i.
```*

</div>

<div class="proof">

*Proof.* Differentiate $`\partial L/\partial\dot X^i`$, subtract $`\partial L/\partial X^i`$, and collect the Levi–Civita terms into the covariant acceleration. The antisymmetric derivative of $`A`$ gives $`F_{ij}`$, the time derivative gives $`E_i`$, and the remaining scalar term is $`-\nabla_iV_C`$. ◻

</div>

The theorem shows exactly what survives from the earlier argument. The Lorentz force follows from gauge-covariant minimal coupling in the effective action. If MTT derives that action and its $`U(1)`$ connection from the same source, the result becomes an MTT force law. Phase coherence by itself does not select the kinetic term, charge, connection, or mass.

## Three distinct notions of mass

The previous paper used
``` math
M_\rho=\int\rho\,\mathrm{d}x
```
as both normalization and mass. Three quantities must instead be separated:

1.  $`M_\rho`$, the conserved weight of the chosen density;

2.  $`m_I`$, the coefficient of the kinetic term and hence inertial response;

3.  $`m_{\mathrm{spec}}`$, a rest-energy or spectral mass extracted from a physical operator.

<div id="prop:mass" class="proposition">

**Proposition 10** (Mass-identification condition). *The equality $`M_\rho=m_I`$ is a convention or a constitutive theorem, not a consequence of the continuity equation.*

</div>

<div class="proof">

*Proof.* For any constant $`c>0`$, replacing $`\rho`$ by $`c\rho`$ leaves the normalized centroid $`X`$ unchanged and preserves the homogeneous continuity equation, but changes $`M_\rho`$ by $`c`$. The kinetic coefficient $`m_I`$ in <a href="#eq:lagrangian" data-reference-type="ref+label" data-reference="eq:lagrangian">[eq:lagrangian]</a> is unchanged unless a separate rule ties it to $`\rho`$. ◻

</div>

A selected theory may prove $`M_\rho=m_I=m_{\mathrm{spec}}`$ after fixing normalization. Until then, “mass is integrated coherence weight” is only a model ansatz.

# Charge and particle number

## Charge conservation

A representation label can remain constant under parallel transport, but that statement requires a fixed representation bundle and compatible connection. In an action formulation, continuous charge conservation is normally tied to a symmetry and a current identity.

<div id="thm:charge" class="theorem">

**Theorem 11** (Conditional charge conservation). *Assume an effective action invariant under a $`U(1)`$ gauge symmetry, a well-defined gauge current $`J^\mu`$, and equations of motion for which the Noether identity is valid. Then
``` math
\nabla_\mu J^\mu=0.
```
If boundary flux vanishes, the total charge on a spatial slice is conserved.*

</div>

<div class="proof">

*Proof.* This is the standard Noether identity for the declared gauge symmetry, followed by integration of the continuity equation. ◻

</div>

Basin persistence alone is insufficient. A persistent basin may contain a nonconserved internal coordinate, while a conserved charge may be shared across several changing quasiparticle basins.

## Particle number

Basin merge, split, creation, or dissolution are possible descriptions of particle-number change, but possibility is not dynamics. A physical claim requires a transition kernel, field equation, interaction vertex, or singular-limit rule that determines rates and preserves the required charges. Version 3 therefore retains basin recombination as an interpretation and withdraws automatic particle creation or annihilation from barrier crossing.

# Confinement requires a coercive energy law

Qualitative non-Abelian “strain” does not prove confinement. A useful capacity model must produce a gauge-invariant energy or action whose cost grows with separation.

<div id="thm:confinement" class="theorem">

**Theorem 12** (Conditional separation bound). *Let $`R\geq0`$ be a gauge-invariant separation coordinate for a nonsinglet configuration. If a selected effective energy satisfies
``` math
V_{\mathrm{sep}}(R)\geq\sigma R-c,
 \qquad \sigma>0,
```
then every configuration in the energy sublevel $`V_{\mathrm{sep}}\leq E`$ obeys
``` math
R\leq\frac{E+c}{\sigma}.
```*

</div>

<div class="proof">

*Proof.* Combine the lower bound with $`V_{\mathrm{sep}}(R)\leq E`$ and solve for $`R`$. ◻

</div>

This is a genuine confinement-type statement for finite-energy sublevels. To connect it to Yang–Mills confinement one still needs the physical gauge field, Hilbert space or path-integral measure, static-source limit, renormalization, and a Wilson-loop or equivalent observable. A Wilson-loop area law cannot be inferred merely from a capacity bottleneck. Capacity may help generate $`V_{\mathrm{sep}}`$, but the coercive estimate is the theorem that must be derived.

# Gravity and universality

The universality of gravity does not follow from the fact that every basin has a capacity record. A gravitational model needs Lorentzian geometry, a stress-energy source, field equations or an action, and a rule connecting the particle record to geodesic or forced motion.

At the effective level one may append
``` math
S_{\mathrm{grav}}[g]
 +S_{\mathrm{matter}}[g,\Psi]
```
and derive both the gravitational field equation and covariant matter response. Equality of inertial and gravitational mass, universal free fall, and backreaction then become testable properties of the common action. They are not consequences of a scalar capacity gradient.

The basin proposal remains compatible with gravity: a localized solution of a matter theory may define a quasiparticle whose centroid follows a controlled worldline limit. The missing step is the same-source action and limit theorem.

# The MTT source contract

<div id="def:source" class="definition">

**Definition 13** (Selected basin-particle source contract). A selected MTT basin-particle derivation must provide:

1.  one upper state complex and selected action or generator;

2.  a coherent projector and a proved stable-basin sector;

3.  a spatial observation map with localization and approximation bounds;

4.  a momentum or stress balance derived from the same action;

5.  kinetic normalization and a source-derived mass observable;

6.  gauge representation, connection, current, and charge identity;

7.  any capacity-to-potential or capacity-to-stress constitutive map;

8.  transition dynamics for merge, split, creation, and annihilation;

9.  for confinement, a gauge-invariant coercive energy or area-law theorem;

10. for gravity, a common metric coupling and controlled worldline limit.

</div>

<div id="thm:encoding" class="theorem">

**Theorem 14** (Conditional basin-particle encoding). *If the rows of Definition <a href="#def:source" data-reference-type="ref" data-reference="def:source">13</a> are supplied by one selected upper MTT object and commute with projection to the effective record, then each stable localized basin defines a controlled effective particle model. Its centroid obeys <a href="#thm:centroid" data-reference-type="ref+label" data-reference="thm:centroid">5</a>; its force law is determined by the projected action or constitutive stress; and its masses and charges have the status proved by their source rows.*

</div>

<div class="proof">

*Proof.* The basin and observation rows construct Definition <a href="#def:particle-record" data-reference-type="ref" data-reference="def:particle-record">4</a>. The common action supplies the balance law and internal symmetry. The centroid theorem transfers the distributed dynamics to a worldline equation with an explicit localization error. Because the remaining quantities are carried by the same commuting source maps, no force, mass, or charge is introduced by relabeling a diagnostic. ◻

</div>

Current MTT work has not instantiated the full contract. In particular, the live upper-action blocker remains open. The theorem is therefore a precise conditional target, not a claim that MTT has already replaced quantum field theory’s particle and interaction structure.

# What the basin picture achieves

The corrected proposal still has real value.

1.  It gives a common effective vocabulary for persistence, localization, internal labels, and transition events.

2.  It replaces an ideal point particle by a controlled localized record, which is often the natural object in soliton, quasiparticle, and wave-packet limits.

3.  It supplies an exact route from distributed balance laws to centroid mechanics.

4.  It identifies how a capacity diagnostic may enter physics without confusing admissibility with energy: through a selected potential, action, or stress law.

5.  It turns broad claims about mass, charge, confinement, and gravity into separate falsifiable source obligations.

The proposal is not a proof that all elementary particles are classical attractors. Fermionic statistics, spin, relativistic localization, quantum superselection, scattering, and particle creation require the appropriate quantum field-theoretic carrier. A basin may encode a sector or stable excitation in that carrier; it need not be a literal classical region in three-space.

# Falsifiability and next steps

A concrete basin-particle model should publish:

1.  the state space, evolution, basin, and stability estimate;

2.  the spatial observation map and localization error;

3.  the action or constitutive laws producing $`\Pi`$ and $`b`$;

4.  independent definitions of density weight, inertial mass, spectral mass, and gravitational coupling;

5.  the gauge bundle, current, and conservation proof;

6.  the capacity normalization and selected coupling function;

7.  held-out predictions for motion, scattering, spectra, or transitions.

The immediate MTT frontier is to derive one nontrivial entry of this list from the selected upper action. A useful first target would be a localized mode of the selected operator whose effective kinetic term, mass coefficient, and one gauge coupling are all obtained by the same projection. That would establish more than a visual resemblance to a particle: it would connect persistence, inertia, and interaction in one source-preserving calculation.

# Conclusion

Stable coherence basins remain plausible effective encodings of persistent localized excitations. The mathematical content begins only after the basin is connected to spatial observables and dynamics. Under declared continuity and momentum balances, the exact centroid equation follows. Under a declared gauge-covariant action, Newtonian and Lorentz force laws follow. Under a coercive separation energy, a confinement-type finite-energy bound follows.

None of these laws follows from a diagnostic capacity gradient alone. Version 3 therefore replaces the claim that particles and forces have already been derived with a more useful result: a complete typed particle record, exact centroid mechanics, conditional force theorems, no-go results for untyped identifications, and a sharply stated same-source action target.

<div class="thebibliography">

99

P. Nero, *Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion*, Version 3, July 2026.

P. Nero, *Coherence Capacity as the Invariant Admissibility Margin*, revised 2026.

P. Nero, *Projection-Limited Coherence: A Structural Theory of Effective Description*, Version 2, July 2026.

P. Nero, *Modal Triplet Theory: Foundation*, revised July 2026. <https://doi.org/10.5281/zenodo.16949762>

</div>
