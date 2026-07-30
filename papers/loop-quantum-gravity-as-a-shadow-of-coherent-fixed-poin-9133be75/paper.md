---
abstract: |
  This paper develops an interpretive comparison between loop quantum gravity (LQG) and the coherent fixed-point sector of Modal Triplet Theory (MTT). The comparison is useful, but it is not a derivation of LQG from projection. Fixed-point stability, finite survivor sectors, compact reuse channels, and noninvertible projection suggest why graph-based states and discrete labels can be effective descriptions of coherent geometry. They do not by themselves construct the Ashtekar–Barbero phase space, the holonomy–flux algebra, the Ashtekar–Lewandowski state, area and volume operators, quantum constraints, or spin-foam amplitudes. Those objects require the explicit canonical and representation data stated in the companion technical paper. In particular, the Barbero–Immirzi parameter is selected by MTT only if the same four-dimensional source that fixes the parity-even gravitational action also emits a normalized parity-odd Holst coefficient. That coefficient is currently open. The result is a disciplined shadow dictionary: it identifies a plausible overlap regime, explains what fixed-point geometry contributes, and gives concrete conditions under which the analogy would become a mathematical embedding.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 8bc6c9f52c7eb7f975585c17f6d9b6c2fab1faf786ac975d9ab090b468ab8670
paper_id: loop-quantum-gravity-as-a-shadow-of-coherent-fixed-poin-9133be75
release_state: zenodo_released
released_version: v2
title: |
  Loop Quantum Gravity as a Possible Shadow of Coherent Fixed-Point Geometry:
  An Interpretive Dictionary and Its Missing Bridges
zenodo_doi: 10.5281/zenodo.21665980
zenodo_record_id: 21665980
zenodo_url: "https://zenodo.org/records/21665980"
---

# Version 2 Revision Note

Supersedes:
The first release under the coherent fixed-point shadow title.

Reason:
A broad graph analogy had been promoted into derivations of $`\mathrm{SU}(2)`$, spin networks, geometric spectra, and the Immirzi parameter.

Resolution:
The paper is now an interpretive dictionary that imports the canonical theorem from its technical owner and lists each missing bridge.

Retained result:
Fixed-point survivors and relational projection give a coherent interpretation of finite graph-labelled encodings.

Remaining boundary:
The Holst source, holonomy–flux algebra, state, operators, constraints, and spin-foam dynamics remain external or open.

# Why compare fixed points with loops?

LQG and MTT begin with different questions. LQG asks how the canonical phase space of general relativity can be quantized using connection variables. MTT asks which upper configurations remain coherent under a many-to-one projection and how stable lower descriptions arise from those survivor classes.

The two viewpoints meet because both organize geometry through relational rather than pointwise data. A holonomy remembers how a connection transports information around a path. A fixed-point survivor class remembers which upper differences remain invisible or stable after projection. Both can be encoded by networks, labels, and local compatibility relations.

That resemblance motivates the word *shadow*. It does not yet establish identity. Many different continuum systems admit graph discretizations, and many different graph systems use compact representation labels. To show that an MTT shadow is specifically LQG, one must recover LQG’s symplectic, algebraic, and representation structures, not just a graph-shaped picture.

## The plain-language picture

Imagine a coherent geometric configuration observed only through a finite family of admissible comparisons. Regions become nodes, admissible transport channels become edges, and compact internal transformations label how the descriptions match. This can look like a spin network. The graph is then an encoding of what the projection can distinguish, rather than a declaration that spacetime is fundamentally a lattice.

The distinction is important. A useful encoding can have discrete labels while the underlying geometry remains continuous. Conversely, a finite projector can select finitely many modes without producing the particular flux algebra from which LQG area and volume spectra follow.

# The disciplined shadow dictionary

<div class="center">

| MTT language | Possible LQG reading | What must still be proved |
|:---|:---|:---|
| Coherent fixed-point sector | Effective geometric phase-space sector | Lorentzian tetrad and symplectic reduction |
| Compact reuse channel | Internal rotational data | Exact time-gauge $`\mathrm{SU}(2)`$ connection |
| Admissible transport | Edge holonomy | Connection, path category, and composition law |
| Projected comparison data | Flux-like surface data | Densitized triad and holonomy–flux brackets |
| Finite survivor encoding | Graph or spin-network truncation | Cylindrical consistency and representation state |
| Closure cost or response | Constraint or dynamics candidate | Regularized constraint operators and anomaly control |
| Shared source coefficients | Immirzi and Newton normalizations | Complete normalized first-order action |

</div>

The third column is not a list of minor technicalities. It separates a broad analogy from an embedding. Each row introduces a mathematical object with its own domain and compatibility conditions.

# What fixed-point geometry can genuinely contribute

## A reason for finite effective descriptions

If an MTT branch has a spectral gap and a controlled finite projector, then a bounded observational window may be described by finitely many surviving modes. This gives a principled reason to use finite graphs or finite label sets as approximations. It is stronger than choosing a lattice solely for numerical convenience because the truncation is tied to a specified coherence criterion.

It is nevertheless a truncation statement. It does not imply that the continuum limit is already defined, that all refinements are equivalent, or that the selected finite data carry the LQG holonomy–flux algebra.

## A reason for relational labels

The current MTT corpus treats physical lower data as relations among surviving structures rather than as a list of independent point values. Edges and intertwiners are natural bookkeeping devices for such relations. If the relevant reuse symmetry is exactly $`\mathrm{SU}(2)`$, its irreducible representations provide discrete labels of those channels.

But the phrase “if the symmetry is exactly $`\mathrm{SU}(2)`$” carries real content. Compactness alone does not select $`\mathrm{SU}(2)`$. The group must arise from the Lorentzian tetrad theory after the standard internal time gauge, or be selected independently with an explicit action on the physical variables.

## A reason to distinguish fundamental and effective discreteness

MTT naturally separates upper configurations from their lower encodings. That separation offers a clean interpretation of LQG discreteness: discrete geometric eigenvalues may characterize the chosen quantum representation without requiring a literal granular manifold in the upper description. This is an interpretive advantage, not a new proof of the spectra.

# The canonical bridge imported from the technical paper

The technical companion, *Modal Triplet Theory and Loop Quantum Gravity: A Conditional Holst/Canonical Embedding*, owns the relevant theorem. In its fixed convention, suppose the selected four-dimensional action is
``` math
S=
 \frac{1}{16\pi G}\int
 \left[
  \frac12\epsilon_{IJKL}e^I\wedge e^J\wedge F^{KL}
  +r_H e_I\wedge e_J\wedge F^{IJ}
 \right]+S_{\partial M}.
```
After a controlled $`3+1`$ split, time gauge, treatment of torsion, and the required boundary data, the standard Holst reduction gives
``` math
A^i_a=\Gamma^i_a+\gamma K^i_a,
 \qquad
 \{A^i_a(x),E^b_j(y)\}
 =8\pi G\gamma\,\delta^i_j\delta^b_a\delta^{(3)}(x,y),
```
with $`\gamma=-1/r_H`$.

This is the precise point at which the shadow can become a canonical embedding. The result is conditional because current MTT results do not emit the selected coefficient $`r_H`$, the foliation, or the time gauge. This paper does not repeat the proof; it explains its meaning.

## What happened to the predicted Immirzi parameter?

The first edition said that a bottleneck vector $`\Theta`$ fixed $`\gamma`$ through unnamed overlap ratios. That statement skipped the essential source calculation. A genuine prediction needs:

1.  a selected four-dimensional parity-even coefficient;

2.  a selected parity-odd Holst coefficient from the same source;

3.  a complete normalization and sign convention; and

4.  an evaluated ratio with an error or exactness certificate.

The conversion from the ratio to $`\gamma`$ is known. The selected ratio is not. Black-hole entropy matching may test a supplied value in a chosen LQG counting framework, but it cannot serve as the missing MTT derivation without turning the observed entropy normalization into an input.

# Why projection alone does not give spin networks

A spin network is not merely a finite graph with group labels. It is a cylindrical function of a connection, with edges labelled by group representations and vertices by intertwiners, living in a specified kinematical Hilbert space. To reach that object from MTT one needs:

1.  an $`\mathrm{SU}(2)`$ connection on a spatial slice;

2.  holonomies and fluxes with their correct Poisson brackets;

3.  a consistent family of graph refinements;

4.  a positive state on the resulting algebra; and

5.  the representation and measure selected by that state.

The LOST uniqueness result becomes relevant only after its exact algebraic, regularity, covariance, and state hypotheses are met. Saying that an MTT projector respects a symmetry is not the same as constructing the required state. Once the Ashtekar–Lewandowski representation is supplied, standard spin networks and area/volume operators are inherited. Before that point, they remain candidate shadow encodings.

# Constraints and dynamics

The graph-shaped kinematical picture is only the beginning of LQG. Physical dynamics requires implementation of the Gauss, spatial-diffeomorphism, and Hamiltonian constraints. Their quantum versions involve choices of regularization, operator domains, graph changes, anomaly control, and physical inner products.

Fixed-point closure may inspire a constraint interpretation: an admissible state is one that survives all required compatibility tests. Yet a closure cost is not automatically the LQG Hamiltonian constraint, and the kernel of one is not automatically the physical Hilbert space of the other. An operator equality or controlled limiting theorem is required.

The same caution applies to spin foams. A covariant history of projected graphs resembles a two-complex, but EPRL/FK amplitudes require a BF/Plebanski formulation, simplicity constraints, representation maps, amplitude weights, and a refinement prescription. Those are separate construction data.

# The overlap regime with MTT fixed points

The shadow interpretation is strongest in a restricted regime:

1.  the q79 branch has already reduced to a controlled four-dimensional Lorentzian gravitational sector;

2.  the effective fields admit a nondegenerate tetrad formulation;

3.  a $`3+1`$ description and time gauge are valid on the region studied;

4.  the same selected source emits the Holst ratio;

5.  a finite coherent projector defines a controlled approximation to the resulting canonical theory; and

6.  the LQG algebra, state, and operators are supplied without conflict with that approximation.

In that overlap regime, MTT can provide an upper-world interpretation of why only some relational geometric data remain visible, while LQG provides a precise canonical language for those visible data. Outside it, the two frameworks may still share motifs without describing the same mathematical object.

# Relation to the q79 Fu–Yau branch

The current strongest MTT compactification candidate is the q79 Fu–Yau heterotic branch. It is not the same object as an LQG spatial graph. The Fu–Yau geometry belongs to the internal compactification and ultraviolet completion route; the LQG variables belong to an effective four-dimensional canonical description.

The hoped-for chain is therefore
``` math
\begin{aligned}
 \text{q79 internal geometry}
 &\longrightarrow \text{normalized four-dimensional action}\\
 &\longrightarrow \text{Holst canonical variables}\\
 &\longrightarrow \text{LQG kinematics and, separately, dynamics}.
\end{aligned}
```
Each arrow must preserve its fields, normalizations, and domains. A shared circle or common bundle may help define the first reduction, but it does not replace the later canonical and representation maps.

# What would count as success or failure?

The proposal becomes substantially stronger if all of the following are constructed from one selected branch:

1.  a nonzero normalized $`r_H`$ and hence a definite $`\gamma`$;

2.  a controlled finite projector on the canonical variables that intertwines holonomies, fluxes, and refinement;

3.  a positive diffeomorphism-compatible state satisfying the relevant uniqueness theorem;

4.  constraint operators whose lower action agrees with the chosen LQG construction; and

5.  a semiclassical sector recovering the same Einstein observables already certified in the MTT gravity branch.

The proposal fails in its strong form if the selected action has no compatible Holst bridge, if the finite projector cannot preserve the canonical algebra, if the required state does not exist, or if the physical constraint sector disagrees with the Einstein limit. These are useful failure conditions: the shadow language is not allowed to move the target after a calculation.

# Version 2 revision note

The first edition described $`\mathrm{SU}(2)`$, spin networks, geometric spectra, the Immirzi parameter, and horizon entropy as consequences of coherent projection. Version 2 reclassifies those statements. It retains the fixed-point interpretation of finite relational encodings, but imports the canonical theorem from its technical owner and lists every missing bridge. It also removes claims that entropy fixes an already selected MTT parameter or that the MTT ultraviolet filter automatically acts on spin-foam amplitudes.

# Conclusion

LQG can plausibly be a shadow language for a controlled MTT coherent sector, but the present result is an interpretive dictionary plus a precise interface, not a derivation. Fixed-point geometry explains why finite, relational, graph-like encodings may be natural. The Holst action explains when those encodings become the Ashtekar–Barbero phase space. The holonomy–flux representation and quantum dynamics require further explicit data.

That layered conclusion is more informative than the older automatic emergence claim. It says exactly what MTT contributes, exactly what LQG contributes, and which calculation – the same-source normalized Holst coefficient – is the first unresolved bridge between them.

<div class="thebibliography">

9 S. Holst, *Barbero’s Hamiltonian derived from a generalized Hilbert–Palatini action*, Physical Review D **53** (1996), 5966–5969.

J. Lewandowski, A. Okolow, H. Sahlmann, and T. Thiemann, *Uniqueness of diffeomorphism invariant states on holonomy–flux algebras*, Communications in Mathematical Physics **267** (2006), 703–733.

C. Rovelli, *Quantum Gravity*, Cambridge University Press, 2004.

</div>
