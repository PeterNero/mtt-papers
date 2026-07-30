---
abstract: |
  A tensor of the form $`\langle D_\mu\Psi,D_\nu\Psi\rangle`$ is a positive-semidefinite Gram tensor and cannot have Lorentzian signature. Physical signature must instead come from the principal symbol of a selected local physical evolution law. For a nondegenerate quadratic metric symbol we prove that hyperbolicity with respect to one evolution covector is possible exactly for Lorentzian inertia, with one sign occurring once. This conditionally excludes Euclidean and multi-time signatures from the standard one-parameter Cauchy problem, but it does not select the number of spatial dimensions. The $`3+1`$ Lorentzian base is therefore an assumption of the canonical ten-dimensional MTT/Fixed-Points realization unless a separate dimension-selection theorem is supplied. We prove local stability of Lorentzian inertia under coefficient perturbations, show that continuous signature change crosses degeneracy, and give a principal-symbol descent theorem for fiberwise coherent compression. Control contraction, internal spectral gaps, physical hyperbolicity, and dimension selection remain independent gates.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: d46e5b2dfbdf9cfa255fe1ead3340db2783690469642cc2093ac24c8903d5660
paper_id: lorentzian-base-compatibility-and-signature-stability-i-6ac3fbb9
release_state: zenodo_released
released_version: v2
title: |
  Lorentzian Base Compatibility and Signature Stability
  in the MTT Fixed-Point Realization
zenodo_doi: 10.5281/zenodo.21665981
zenodo_record_id: 21665981
zenodo_url: "https://zenodo.org/records/21665981"
---

# Version 2 Revision Note

Supersedes
*Signature Selection and Exclusion in Modal Triplet Theory*, first edition.

Reason
A positive Hilbert-space Gram tensor was assigned Lorentzian signature, which is mathematically impossible.

Resolution
Version 2 moves causal signature to the principal symbol, proves the conditional one-time hyperbolicity criterion and inertia stability, and separates signature from dimension selection and internal rank counts.

Retained result
Signature stability and coherent principal-symbol descent survive under explicit hyperbolic hypotheses.

Remaining boundary
The $`3+1`$ base and its Lorentzian law are inputs of the canonical physical completion until independently selected.

# Correction and scope

The former paper defined
``` math
K_{\mu\nu}=\langle D_\mu\Psi_\ast,D_\nu\Psi_\ast\rangle_{\rm coh}
```
using a positive Hilbert inner product and then assigned Lorentzian signature to $`K`$. This is impossible.

<div id="prop:gram" class="proposition">

**Proposition 1** (Positive Gram obstruction). *For vectors $`v_0,\ldots,v_{d-1}`$ in a real Hilbert space, the Gram matrix $`G_{\mu\nu}=\langle v_\mu,v_\nu\rangle`$ is positive semidefinite. Hence it has no negative eigenvalues and cannot be a Lorentzian metric.*

</div>

<div class="proof">

*Proof.* For every $`c\in\mathbb R^d`$,
``` math
c^\mu G_{\mu\nu}c^\nu
 =\left\|\sum_\mu c^\mu v_\mu\right\|^2\ge0.
```
 ◻

</div>

The Gram tensor may be a useful positive kinetic or information metric. It is not a causal metric. Inserting an indefinite operator between the vectors can produce an indefinite form, but that operator is then additional signature data and must be selected and justified independently.

This revision studies compatibility and stability of a Lorentzian principal symbol. It does not claim universal signature or dimension selection. The separate world-in-world identity $`1+3\times3=(1+3)+(1+2+3)`$ counts components of an ordering scalar and a rank-three comparison field. It is not a principal-symbol calculation and therefore cannot select either a $`3+1`$ base or Lorentzian inertia.

# Canonical MTT geometry and independent gates

The canonical physical realization is
``` math
\pi:M_{10}\to Y_4,
 \qquad \dim Y_4=4,
 \qquad \dim X_x=6,
```
with globally hyperbolic Lorentzian base $`(Y_4,g)`$ and compact Riemannian fiber $`X_x`$. The base dimension and its Lorentzian signature are part of this canonical realization. Positive vertical operators act on $`X_x`$ and do not determine the causal signature of $`Y_4`$. Matching the six local strain components to a rank-six internal carrier likewise supplies no causal sign.

Four gates must remain separate:

1.  the internal gap and coherent spectral projector;

2.  stability or contraction of the stabilization flow $`R_\tau`$;

3.  hyperbolicity and causal propagation of a physical evolution $`U(t_2,t_1)`$; and

4.  selection of base dimension and topology.

The stabilization parameter $`\tau`$ is not automatically physical time $`t`$. Neither a vertical gap nor Banach contraction supplies a null cone.

# Principal symbols and physical signature

Consider a local second-order physical field equation for a multiplet $`u^A`$,
``` math
\mathcal E_A(u)
 =C_{AB}^{\mu\nu}(x,u,\partial u)\,\partial_\mu\partial_\nu u^B
 +\text{lower-order terms}=0.
```
Its principal symbol at a frozen background is
``` math
\sigma_{\rm pr}(x,\xi)_{AB}
 =C_{AB}^{\mu\nu}(x)\xi_\mu\xi_\nu.
```
Characteristics, hyperbolicity, and causal cones come from this symbol after gauge fixing and constraint reduction. Lower-order damping and internal mass operators can affect stability without changing the characteristic cone.

For a normally hyperbolic metric-type equation,
``` math
\sigma_{\rm pr}(x,\xi)
 =g^{\mu\nu}(x)\xi_\mu\xi_\nu I.
```
The physical signature is the inertia of $`g^{\mu\nu}`$, not the inertia of a positive state-space inner product.

For a first-order system, the appropriate condition is strong or symmetric hyperbolicity of $`A^\mu\partial_\mu u`$. Such a system need not be classified by one effective metric without an additional characteristic-cone theorem.

# Quadratic hyperbolicity and conditional exclusions

Let $`q(\xi)=B(\xi,\xi)`$ be a nondegenerate real quadratic form on a real vector space of dimension $`d\ge2`$. It is hyperbolic with respect to a covector $`n`$ if $`q(n)\ne0`$ and, for every $`\xi`$, all roots $`s\in\mathbb C`$ of
``` math
q(\xi+s n)=0
```
are real.

<div id="thm:quadratic" class="theorem">

**Theorem 2** (Quadratic hyperbolicity criterion). *A nondegenerate quadratic form admits a hyperbolicity covector if and only if its inertia is $`(1,d-1)`$ or $`(d-1,1)`$. For a Lorentzian form, the hyperbolicity covectors are the covectors in the one-sign cone.*

</div>

<div class="proof">

*Proof.* Fix $`n`$ with $`q(n)\ne0`$ and decompose $`\xi=a n+\eta`$ with $`B(n,\eta)=0`$. Then
``` math
q(\xi+s n)=q(n)(s+a)^2+q(\eta).
```
All roots are real for every $`\eta\in n^\perp`$ exactly when $`q(n)q(\eta)\le0`$ for every such $`\eta`$. Nondegeneracy makes the restriction to $`n^\perp`$ definite with sign opposite to $`q(n)`$. Thus the sign of $`q(n)`$ occurs exactly once. Conversely, for a vector in the one-sign cone of a Lorentzian form, its orthogonal complement is definite with the opposite sign, and the displayed roots are real. ◻

</div>

<div class="corollary">

**Corollary 3** (Euclidean metric symbol). *A definite Euclidean quadratic symbol is not hyperbolic with respect to any covector. It defines an elliptic rather than a standard hyperbolic Cauchy problem.*

</div>

This does not exclude Euclidean boundary-value theories, statistical models, or Wick-rotated calculational descriptions. It excludes their interpretation as the same real-time metric principal symbol for the standard local physical Cauchy problem.

<div class="corollary">

**Corollary 4** (Multi-time metric symbols). *A nondegenerate metric symbol of signature $`(p,q)`$ with $`p,q\ge2`$, including $`(2,2)`$, has no hyperbolicity covector. It therefore does not furnish the standard single-parameter metric Cauchy problem assumed in the canonical physical realization.*

</div>

This is a conditional principal-symbol statement, not a universal no-go theorem for every constrained, nonlocal, ultrahyperbolic, or analytically continued model.

<div class="corollary">

**Corollary 5** (No selection of three spatial dimensions). *For every $`n\ge1`$, a metric symbol of inertia $`(1,n)`$ or $`(n,1)`$ admits hyperbolicity covectors. Hyperbolicity alone therefore does not select $`n=3`$.*

</div>

Extra spatial dimensions may be incompatible with a particular spectrum, compactification, observation, or stability requirement, but each such exclusion needs its own theorem. The internal MTT gap does not automatically suppress extra base directions.

# Signature stability

<div id="thm:stability" class="theorem">

**Theorem 6** (Uniform inertia stability). *Let $`H(x)`$ be a continuous field of real symmetric nondegenerate matrices on a compact set $`K`$, all with the same inertia. Define
``` math
\delta_{\rm sig}
 :=\inf_{x\in K}\min_j|\lambda_j(H(x))|>0.
```
If a continuous symmetric perturbation $`E(x)`$ satisfies
``` math
\sup_{x\in K}\|E(x)\|_{\rm op}<\delta_{\rm sig},
```
then $`H(x)+E(x)`$ has the same inertia as $`H(x)`$ for every $`x\in K`$.*

</div>

<div class="proof">

*Proof.* Weyl’s eigenvalue perturbation inequality moves every ordered eigenvalue by at most $`\|E(x)\|_{\rm op}`$. No eigenvalue can cross zero under the strict bound, so the numbers of positive and negative eigenvalues are unchanged. ◻

</div>

<div class="corollary">

**Corollary 7** (Continuous signature change crosses degeneracy). *Along a continuous path of real symmetric matrices, a change of inertia requires at least one zero eigenvalue. Thus a continuous metric signature change leaves the uniformly nondegenerate hyperbolic class at the transition.*

</div>

For a quasilinear system, inertia stability is only one gate. Uniform strong hyperbolicity also requires control of the symmetrizer, characteristic roots, gauge conditions, constraints, and coefficient regularity.

# Coherent compression of a hyperbolic realization

The following theorem states a sufficient bridge from the selected physical completion to the coherent sector.

<div id="thm:descent" class="theorem">

**Theorem 8** (Principal-symbol descent). *Let the upper local operator on $`M_{10}\to Y_4`$ have the form
``` math
\mathcal L_{10}
 =g^{\mu\nu}(x)\nabla_\mu\nabla_\nu\otimes I_{\rm int}
 +\mathcal L_{\rm vert}+\mathcal L_{\rm low},
```
where $`\mathcal L_{\rm vert}`$ has no base derivatives of order two and $`\mathcal L_{\rm low}`$ has base order at most one. Let $`P_x`$ be a smooth fiberwise coherent projector whose action commutes with the scalar base principal coefficient. Then the compressed operator on $`\operatorname{Ran}P`$ has principal symbol
``` math
\sigma_{\rm pr}(P\mathcal L_{10}P)(x,\xi)
 =g^{\mu\nu}(x)\xi_\mu\xi_\nu I_{\operatorname{Ran}P}.
```
Consequently the coherent compression inherits the already selected Lorentzian characteristic cone.*

</div>

<div class="proof">

*Proof.* Only the two-base-derivative term contributes to the base principal symbol. Its internal coefficient is the identity, so compression replaces it by the identity on $`\operatorname{Ran}P`$. Derivatives of a smooth base-dependent $`P_x`$ enter commutators of base order at most one and do not alter the principal symbol. ◻

</div>

This theorem proves descent, not emergence or selection, of Lorentzian signature. If the upper operator is bilocal over the base, contains higher-order mixed base/fiber derivatives, or has matrix-valued principal coefficients that do not preserve $`\operatorname{Ran}P`$, a separate analysis is required.

# Relation to the corrected MTT spine

The corrected Foundation supplies the canonical $`Y_4`$-over-$`X_6`$ realization, the joint coherent projector, and the requirement that physical signature come from a principal symbol. Fixed Points I–VI supply conditional projected fixed points, equilibrium promotion, stability margins, curved-projector control, and admissibility diagnostics.

Those results do not select a base metric. Their proper role here is:

- to ensure that the coherent sector used in Theorem <a href="#thm:descent" data-reference-type="ref" data-reference="thm:descent">8</a> is mathematically controlled;

- to bound leakage and lower-order perturbations that might invalidate a chosen physical completion; and

- to provide independent control-flow stability after hyperbolicity has been established.

The Projection–Admissibility theorem contributes typed continuation and locality descent. An admissibility exit detects failure of a declared hyperbolicity or signature margin but does not select a replacement signature.

# Compatibility ledger

A physical signature claim must record:

1.  the physical field equations and gauge-fixed principal symbol;

2.  the state about which the symbol is frozen;

3.  the hyperbolicity covector or time function;

4.  the characteristic cone and domain-of-dependence theorem;

5.  the uniform nondegeneracy margin $`\delta_{\rm sig}`$;

6.  symmetrizer and constraint-propagation bounds for systems;

7.  the relation, if any, between physical time $`t`$ and stabilization parameter $`\tau`$;

8.  the coherent-compression hypotheses; and

9.  the independent status of the chosen base dimension.

Without this ledger, a positive kinetic form or stable control flow cannot be promoted to a spacetime signature theorem.

# Scoped signature theorem

<div id="thm:scope" class="theorem">

**Theorem 9** (Lorentzian compatibility and stability). *Assume the canonical $`3+1`$ MTT physical realization is equipped with a local metric-type physical equation whose principal symbol is Lorentzian and uniformly nondegenerate. Assume also the coherent-compression hypotheses of Theorem <a href="#thm:descent" data-reference-type="ref" data-reference="thm:descent">8</a>. Then the coherent physical equation inherits the selected Lorentzian cone, and sufficiently small symmetric coefficient perturbations preserve its inertia. Definite Euclidean and multi-time metric symbols are incompatible with the same standard one-parameter quadratic hyperbolicity condition.*

</div>

The theorem does not derive Lorentzian signature or $`3+1`$ dimensions from the MTT Hilbert geometry. It verifies compatibility and perturbative stability after a physical principal symbol and canonical base have been supplied.

# Conclusion

The positive Gram construction cannot select spacetime signature. Replacing it with principal-symbol analysis yields a precise and useful result: a standard metric Cauchy problem requires Lorentzian inertia, that inertia is stable away from degeneracy, and coherent fiberwise compression can preserve an already selected causal cone. The same analysis also establishes the limit of the claim: hyperbolicity permits one time and any number of spatial dimensions, so three spatial dimensions remain part of the canonical MTT realization pending a separate selection theorem.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Foundations*, revised v7, 2026.

P. Nero, *Fixed Points I–VI*, corrected theorem spine, 2026.

M. E. Taylor, *Partial Differential Equations III: Nonlinear Equations*, Springer, 2011.

L. Hörmander, *The Analysis of Linear Partial Differential Operators III*, Springer, 1985.

</div>
