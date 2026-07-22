---
abstract: |
  This paper corrects the first edition’s claim that a full nonperturbative, unitary gravity sector follows from separately filtered graviton and ghost covariances, termwise BRST identities, and reflection positivity of the transverse-traceless sector. Those implications are not valid. We replace them by a typed compatibility contract. First, a common bounded functional calculus preserves a linear BRST complex when the kinetic Laplacians, spectral projections, domains, and boundary conditions intertwine the differential; independently chosen filters do not ensure this. Second, an exact finite-cutoff quantum BRST measure gives Ward identities and gauge-fixing independence by super-Stokes, while Borel summation preserves a linear Ward identity only under a common analytic domain and uniform Gevrey-one remainder bounds. Third, BRST cohomology yields a physical pre-Hilbert space only when reflection positivity is proved on the full BRST-closed positive-time observable algebra and exact classes lie in the reflection null radical. Positivity on the TT subspace alone is insufficient. We also prove that a nonzero positive Kallen–Lehmann measure cannot have permanent Gaussian decay in the same Euclidean spectral variable, so the old SPT positivity argument cannot be used. The result is a rigorous conditional theorem and an explicit exit certificate. Current MTT data provide useful finite classical and free-field inputs, but not yet the selected gravitational quantum measure, quantum master equation, constructive Borel theorem, or physical reflection-positivity theorem required by that certificate.
author:
- Peter Nero
current_version: v2
date: Corrected second edition, July 2026
generated_from_main_tex_sha256: bc2d5cadb02e3c99e96998df4d0eacb8e94f5fe35b8be6983e92ded41f3c1381
paper_id: constructive-mtt-quantum-gravity-ii-brst-lifting-gauge-e3cb613b
release_state: zenodo_released
released_version: v1.0
title: |
  Constructive MTT Quantum Gravity II:  
  A Conditional BRST/BV Compatibility and Physical-State Reconstruction Contract for SPT-Filtered Models
zenodo_doi: 10.5281/zenodo.18209697
zenodo_record_id: 18209697
zenodo_url: "https://zenodo.org/records/18209697"
---

# Scope and revision statement

The first edition attempted to lift a conditional SPT-filtered Euclidean TT model to a complete gauge theory. Its central chain was
``` math
\text{filtered covariances}
 \Longrightarrow \text{Borel-summed BRST identities}
 \Longrightarrow \text{TT positivity}
 \Longrightarrow \mathcal H_{\mathrm{phys}}.
```
Each arrow needs an additional theorem. In particular:

1.  a regulator must be a chain map for the BRST/BV complex, including its domains and boundary conditions;

2.  the regularized measure must satisfy the quantum master equation, or an equivalent anomaly-free quantum BRST invariance statement;

3.  the constructive expansion must exist for a precisely specified stable interaction and have uniform bounds strong enough to pass the identity to its Borel sum; and

4.  reflection positivity must hold for the physical gauge-invariant Schwinger functional, not merely for a selected free TT block.

Version 2 withdraws the claim that these four steps have been completed for MTT quantum gravity. It proves the implications that are valid once their hypotheses are supplied and identifies which hypotheses remain open. This is a theorem-level correction, not a change of notation or a boundary disclaimer.

## Typed claim levels

We use three levels throughout:

Classical algebraic level.  
A nilpotent BRST differential and a classical master action are defined after a gauge symmetry and action are supplied.

Regularized quantum level.  
A regulator, measure, integration cycle, and renormalized action satisfy a quantum master equation with controlled boundaries and anomalies.

Physical reconstruction level.  
Gauge-invariant Euclidean correlators satisfy the relevant OS axioms and reconstruct a positive Lorentzian theory.

The first level does not imply the second, and the second does not imply the third.

# Current MTT input and its boundary

The current quantum-gravity audit records exact finite representation data, a finite q79 TT Hessian proportional to the identity, a two-derivative TEGR/Einstein action shape on the explicitly selected branch, and a positive two-helicity free graviton sector. At fixed low-energy order, standard background-field BRST/BV quantum-GR effective-field-theory machinery can be composed with that action. This is an imported parity construction, not an MTT derivation of the quantum measure or UV completion .

There is also an exact classical BRST result for the selected finite Standard Model carrier: the quotient gauge algebra, its Chevalley–Eilenberg ghost differential, and its sixteen-state matter representation close exactly. That result is a classical gauge-stack theorem. It does not construct the gravitational BV measure or prove a quantum master equation .

The revised fixed-point series is deliberately classical. Its damping, covariance, and equilibrium results do not select a quantum covariance or a BRST regulator . Consequently, neither fixed-point damping nor the finite TT Hessian can silently supply the missing quantum hypotheses below.

# Classical gravitational BRST data

Let $`g`$ be a background metric on a bounded Euclidean domain $`\Omega`$ and let $`\gamma=g+h`$ be the total metric. The standard gauge-fixed multiplet is
``` math
\Phi=(h_{\mu\nu},c^\mu,\bar c_\mu,b_\mu),
```
with ghost, antighost, and Nakanishi–Lautrup field. In a consistent graded sign convention, the diffeomorphism BRST differential has the schematic form
``` math
s\gamma=\mathcal L_c\gamma,
 \qquad
 sc=\tfrac12[c,c]_{\mathrm{gr}},
 \qquad
 s\bar c=b,
 \qquad
 sb=0.
```
The graded Jacobi identity and the representation of vector fields by Lie derivatives give $`s^2=0`$. A gauge-fixing fermion $`\Psi`$ adds an $`s`$-exact gauge-fixing and ghost term to a diffeomorphism-invariant classical action. The BV extension adds antifields and packages these relations in the classical master equation
``` math
(S_{\mathrm{BV}},S_{\mathrm{BV}})=0.
```
These are standard consequences of a supplied diffeomorphism-invariant action .

<div class="proposition">

**Proposition 1** (Classical lift does not select a quantum theory). *A nilpotent classical differential and a solution of the classical master equation do not determine a regularized measure, a BV Laplacian, a quantum master action, an integration cycle, or a physical positive inner product.*

</div>

<div class="proof">

*Proof.* The classical data depend only on the gauge orbits and the classical action. Different regularizations can have different Jacobians and anomaly counterterms, and an indefinite gauge-fixed state space can admit inequivalent or nonexistent positive physical completions. These objects are additional data in the BV and OS formalisms. The quantum master equation explicitly contains the measure-dependent BV Laplacian, which is absent from the classical master equation . ◻

</div>

# When an SPT filter preserves a BRST complex

The first edition applied separate scalar functions to the graviton and ghost kinetic operators. The correct requirement is an intertwining theorem.

## A shared functional-calculus theorem

Let
``` math
\cdots\longrightarrow E^r
 \mathop{\longrightarrow}^{Q_r} E^{r+1}
 \mathop{\longrightarrow}^{Q_{r+1}} E^{r+2}
 \longrightarrow\cdots,
 \qquad Q_{r+1}Q_r=0,
```
be a Hilbert complex. Let $`\Delta_r\ge0`$ be self-adjoint kinetic Laplacians on $`E^r`$, with spectral measures $`P_r(B)`$ for Borel sets $`B\subset[0,\infty)`$. Boundary conditions are part of the domains of $`Q_r`$ and $`\Delta_r`$.

<div id="ass:chain" class="assumption">

**Assumption 2** (Spectral chain compatibility). For every Borel set $`B`$ and every $`u`$ in the domain of $`Q_r`$,
``` math
Q_rP_r(B)u=P_{r+1}(B)Q_ru.
```
In addition, the selected boundary domains are mapped by $`Q_r`$ and no boundary term appears in the corresponding Green identity.

</div>

<div id="thm:filter" class="theorem">

**Theorem 3** (Shared-filter chain theorem). *Under Assumption <a href="#ass:chain" data-reference-type="ref" data-reference="ass:chain">2</a>, every bounded Borel function $`f`$ satisfies
``` math
Q_rf(\Delta_r)=f(\Delta_{r+1})Q_r
```
on the domain of $`Q_r`$. Hence, for $`\lambda>0`$, the common filtered covariance
``` math
C_r=f(\Delta_r)(\Delta_r+\lambda)^{-1}
```
is a chain map. The same statement holds for common spectral cutoffs $`P_r([0,\Lambda])`$.*

</div>

<div class="proof">

*Proof.* The spectral theorem gives
``` math
f(\Delta_r)=\int_{[0,\infty)}f(x)\,dP_r(x).
```
Assumption <a href="#ass:chain" data-reference-type="ref" data-reference="ass:chain">2</a> permits $`Q_r`$ to pass through the spectral integral, which gives the displayed identity. The resolvent factor is another bounded Borel function of the same spectral variable. Taking $`f=\mathbf 1_{[0,\Lambda]}`$ gives the cutoff statement. ◻

</div>

<div id="prop:independent" class="proposition">

**Proposition 4** (Independent filters are insufficient). *Even when the unfiltered kinetic operators form a complex, independently chosen filters need not preserve it.*

</div>

<div class="proof">

*Proof.* Take $`E^0=E^1=\mathbb C`$, $`Q_0=1`$, and $`\Delta_0=\Delta_1=0`$. If the two filters act by constants $`a`$ and $`b`$, then chain compatibility requires $`aQ_0=bQ_0`$, hence $`a=b`$. Independent choices with $`a\ne b`$ violate BRST compatibility in this one-dimensional example. ◻

</div>

Theorem <a href="#thm:filter" data-reference-type="ref" data-reference="thm:filter">3</a> is useful but limited. It controls the linearized complex and its Gaussian covariance. Nonlinear BRST transformations, interaction vertices, antifields, counterterms, and the measure Jacobian must still satisfy the quantum master equation. A smoothing operator can be an excellent regulator while breaking the unmodified Slavnov–Taylor identity; then one needs a modified identity and a proved restoration limit, not an assertion of exact invariance .

## Boundary conditions are structural data

Support of observables away from $`\partial\Omega`$ does not by itself make the integration domain BRST invariant. One must select relative, absolute, or other elliptic boundary conditions for the full complex and prove that $`Q_r`$ maps each domain to the next. Boundary ghosts and possible edge modes must be included whenever gauge transformations act nontrivially at the boundary.

# The finite-cutoff quantum Ward theorem

The clean finite-dimensional statement is a super-Stokes theorem. It shows exactly which premise the first edition assumed rather than proved.

Let $`\mathcal M_N`$ be a finite-dimensional graded field space with Berezin measure $`d\mu_N`$, integration cycle $`\Gamma_N`$, odd vector field $`s_N`$, and Euclidean action $`S_{N,\alpha}`$. The parameter $`\alpha`$ labels a family of gauge-fixing choices.

<div id="ass:qmeasure" class="assumption">

**Assumption 5** (Quantum BRST measure). The following hold:

1.  $`s_N^2=0`$ and $`\Gamma_N`$ is invariant or has vanishing super-boundary;

2.  the weighted measure is invariant,
    ``` math
    \operatorname{div}_{\mu_N}\!\left(s_Ne^{-S_{N,\alpha}/\hbar}\right)=0;
    ```

3.  the gauge variation is exact, $`\partial_\alpha S_{N,\alpha}=s_NK_{N,\alpha}`$; and

4.  all displayed integrals and differentiations are absolutely controlled.

In BV language, item (b) is the finite-cutoff quantum master equation with the chosen measure and anomaly counterterms.

</div>

<div id="thm:ward" class="theorem">

**Theorem 6** (Finite-cutoff Ward and gauge-fixing theorem). *Under Assumption <a href="#ass:qmeasure" data-reference-type="ref" data-reference="ass:qmeasure">5</a>,
``` math
\int_{\Gamma_N}s_NG\,e^{-S_{N,\alpha}/\hbar}d\mu_N=0.
```
If $`s_NO=0`$ and $`O`$ has no explicit $`\alpha`$ dependence, then its normalized expectation is gauge-fixing independent:
``` math
\partial_\alpha\mathbb E_{N,\alpha}[O]=0.
```
Expectations therefore depend only on the $`s_N`$-cohomology class of $`O`$.*

</div>

<div class="proof">

*Proof.* The first identity is super-Stokes applied to $`G e^{-S_{N,\alpha}/\hbar}d\mu_N`$. For a closed $`O`$, the graded Leibniz rule turns $`O\,s_NK_{N,\alpha}`$ into an $`s_N`$-exact insertion. Differentiating the numerator and denominator of the normalized expectation therefore gives zero for each derivative term. Replacing $`O`$ by $`O+s_NH`$ changes no expectation. ◻

</div>

This theorem is nonperturbative at a fixed finite cutoff, but only after the quantum measure premise has been constructed. Classical nilpotency does not prove item (b). Neither does formal cancellation of bosonic and ghost Jacobians, because a regulator, boundary, chiral matter content, or global gauge orbit can change the Jacobian. BV gauge independence is precisely a consequence of the quantum master and integration-cycle hypotheses .

# What Borel summation can and cannot preserve

Suppose a constructive model has already produced Banach-valued correlators $`F(g)`$ with formal series
``` math
F(g)\sim\sum_{n\ge0}F_ng^n.
```
Let $`W`$ be a continuous linear Ward operator on the correlator space.

<div class="theorem">

**Theorem 7** (Uniform Borel inheritance of a linear Ward identity). *Assume:*

1.  *$`WF_n=0`$ for every $`n`$;*

2.  *the Borel transform $`\widehat F(t)=\sum_{n\ge0}F_nt^n/n!`$ has a common analytic continuation along the summation ray;*

3.  *$`\widehat F`$ has a uniform exponential bound that permits the Laplace integral and permits $`W`$ to pass through it; and*

4.  *the resulting Laplace integral is the unique Borel sum of $`F`$ in the declared Nevanlinna–Sokal domain.*

*Then $`WF(g)=0`$ throughout that domain.*

</div>

<div class="proof">

*Proof.* Continuity and item (i) give $`W\widehat F(t)=\sum_n(WF_n)t^n/n!=0`$ near the origin. Analytic continuation keeps it zero along the summation ray. By item (iii), $`W`$ commutes with the Laplace integral, so the Borel sum is also annihilated by $`W`$. Uniqueness prevents a second analytic function with the same controlled asymptotic series from being substituted . ◻

</div>

The theorem is an inheritance result, not a constructive existence theorem. It does not derive the loop-vertex expansion, stability, the common analytic domain, cutoff-uniform constants, or convergence as $`N\to\infty`$. A nonlinear QME additionally requires a Banach algebra in which products and Borel convolutions are controlled. The first edition supplied none of these uniform estimates for the full gravity/ghost interaction. The corresponding claim is therefore conditional.

The antecedent QG-I paper also requires its own repair: Hilbert–Schmidt control alone is not a construction of a countably additive Gaussian measure on the same Hilbert space, and generic local analyticity plus a lower bound is not a complete mixed boson–ghost Borel theorem. QG-II cannot inherit a conclusion that its antecedent has not established.

# Physical cohomology and reflection positivity

Let $`\mathcal A`$ be a Euclidean observable algebra, $`\mathcal A_{+}`$ its positive-time subalgebra, $`\Theta`$ the antilinear time reflection, and $`\mathcal S`$ the Euclidean expectation functional. Let $`s`$ be an odd derivation preserving support and compatible with reflection. Set
``` math
Z_+=\ker(s|_{\mathcal A_{+}}),\qquad B_+=\operatorname{im}(s|_{\mathcal A_{+}})\cap Z_+.
```

<div id="ass:physicalOS" class="assumption">

**Assumption 8** (Physical reflection package). For all $`F,G\in Z_+`$:

1.  the form $`(F,G)_{\mathrm{OS}}=\mathcal S(\Theta F\,G)`$ is Hermitian and positive semidefinite;

2.  BRST-exact vectors are in its radical, $`\mathcal S(\Theta F\,sH)=\mathcal S(\Theta(sH)\,F)=0`$; and

3.  positive Euclidean-time translations preserve $`Z_+`$, $`B_+`$, and the null space of the form.

</div>

<div id="thm:os" class="theorem">

**Theorem 9** (Conditional cohomological OS reconstruction). *Under Assumption <a href="#ass:physicalOS" data-reference-type="ref" data-reference="ass:physicalOS">8</a>, the quotient
``` math
\mathcal H_{0}=
 \frac{Z_+}{B_++\mathcal N_{\mathrm{OS}}}
```
has a positive definite inner product. Its completion is a Hilbert space $`\mathcal H_{\mathrm{phys}}`$. The Euclidean translation maps descend to contractions whenever the usual OS semigroup hypotheses hold. A global positive-energy Lorentzian unitary group follows only after the full OS reconstruction hypotheses, including a suitable all-time or infinite-volume completion, are proved.*

</div>

<div class="proof">

*Proof.* Item (b) makes the form independent of the representative of a BRST cohomology class. Item (a) makes the descended form positive semidefinite, and quotienting by its null space makes it positive definite. Completion gives $`\mathcal H_{\mathrm{phys}}`$. Item (c) permits the OS semigroup construction. The final Lorentzian statement is exactly the additional content of the OS reconstruction theorem, not a consequence of a bounded slab alone . ◻

</div>

<div class="proposition">

**Proposition 10** (TT positivity does not imply physical positivity). *Positivity of the OS form on a TT subspace $`T\subset Z_+`$ does not imply Assumption <a href="#ass:physicalOS" data-reference-type="ref" data-reference="ass:physicalOS">8</a>(a) unless every physical cohomology class has a TT representative and the representative map preserves the OS form.*

</div>

<div class="proof">

*Proof.* Take $`Z_+=\mathbb C^2`$, $`s=0`$, and the Hermitian form $`\operatorname{diag}(1,-1)`$. Its restriction to $`T=\operatorname{span}\{(1,0)\}`$ is positive, but the full cohomology contains the negative vector $`(0,1)`$. Thus positivity on a subspace has no such logical consequence. The missing representative theorem is exactly what would rule out this counterexample. ◻

</div>

Kugo–Ojima positivity similarly requires a representation of the BRST charge, the quartet mechanism, and spectral/asymptotic assumptions; it is not a formal consequence of writing $`\ker Q/\operatorname{im}Q`$ .

# Why permanent Gaussian damping cannot prove standard positivity

The earlier SPT program tried to combine a positive spectral representation with permanent Gaussian ultraviolet damping. The following elementary no-go is independent of the BRST issue.

<div class="theorem">

**Theorem 11** (Positive spectral measure versus Gaussian decay). *Let
``` math
D(x)=\int_0^\infty\frac{\rho(ds)}{x+s},\qquad x>0,
```
where $`\rho`$ is a nonzero positive measure and $`D(x)`$ is finite. Then there are $`R,m>0`$ such that
``` math
D(x)\ge\frac{m}{x+R}.
```
Consequently, for no $`C,\tau,\lambda>0`$ can
``` math
D(x)\le \frac{C e^{-\tau x}}{x+\lambda}
```
hold for all sufficiently large $`x`$.*

</div>

<div class="proof">

*Proof.* Because $`\rho`$ is nonzero, some bounded interval $`[0,R]`$ has mass $`m=\rho([0,R])>0`$. Restricting the integral to that interval gives the lower bound. Combining both inequalities would imply
``` math
\frac{m}{C}\le e^{-\tau x}\frac{x+R}{x+\lambda},
```
whose right-hand side tends to zero. ◻

</div>

Thus a nontrivial standard positive Kallen–Lehmann measure and permanent Gaussian decay cannot hold in the same Euclidean spectral variable. This does not prove that every nonlocal model is nonunitary; it proves that the old Stieltjes/OS argument cannot establish the desired result. Nonlocal theories require a separate, internally consistent spectral and positivity framework .

# The corrected conditional theorem

We can now state the strongest result supported by the present paper.

<div id="thm:main" class="theorem">

**Theorem 12** (Conditional SPT–BRST reconstruction contract). *Consider an SPT-filtered Euclidean gravity model. Suppose all of the following are supplied independently:*

F1.  
*A selected gauge-invariant classical action and a closed BRST/BV complex with compatible boundary domains.*

F2.  
*A shared spectral filter satisfying Assumption <a href="#ass:chain" data-reference-type="ref" data-reference="ass:chain">2</a>, together with a controlled finite-cutoff measure space.*

F3.  
*An anomaly-free quantum measure satisfying Assumption <a href="#ass:qmeasure" data-reference-type="ref" data-reference="ass:qmeasure">5</a> at every cutoff, with a proved removal limit.*

F4.  
*A constructive existence and Borel theorem with a common analytic domain, uniform Gevrey-one remainders, and convergence of the Borel sums as the cutoff and volume are removed.*

F5.  
*The physical gauge-invariant Schwinger functional satisfies Assumption <a href="#ass:physicalOS" data-reference-type="ref" data-reference="ass:physicalOS">8</a> and the remaining OS reconstruction axioms.*

*Then BRST-exact insertions vanish, BRST-closed expectations are independent of the admitted gauge-fixing homotopy, the linear Ward identities survive Borel summation, and the BRST cohomology reconstructs a positive physical Hilbert space. If the global OS, continuation, and time-translation hypotheses are also met, the reconstructed Lorentzian time evolution is unitary.*

</div>

<div class="proof">

*Proof.* F1 and F2 give Theorem <a href="#thm:filter" data-reference-type="ref" data-reference="thm:filter">3</a>. F3 gives Theorem <a href="#thm:ward" data-reference-type="ref" data-reference="thm:ward">6</a> at finite cutoff. F4 permits the uniform Borel inheritance theorem and the declared removal limits. F5 gives Theorem <a href="#thm:os" data-reference-type="ref" data-reference="thm:os">9</a> and, with the remaining OS axioms, Lorentzian reconstruction. No step uses TT positivity as a substitute for physical positivity or classical nilpotency as a substitute for the QME. ◻

</div>

The theorem is rigorous as an implication. It is not a proof that current MTT satisfies F2–F5.

# MTT readiness ledger and exit certificate

<div class="center">

| Object | Current status | Exact boundary |
|:---|:---|:---|
| Finite q79 TT operator and free helicity sector | Available at declared tier | Does not select a quantum measure or interacting UV theory. |
| Two-derivative gravity action shape | Conditional on the selected branch | Standard diffeomorphism BRST can be attached classically; normalization and quantum source remain separate. |
| Finite SM gauge BRST complex | Closed classically | Applies to the selected quotient gauge carrier, not to the gravitational QME. |
| SPT chain-compatible regulator | Open for the selected gravity complex | Must verify Theorem <a href="#thm:filter" data-reference-type="ref" data-reference="thm:filter">3</a>, including boundaries and antifields. |
| Quantum BRST/BV measure | Open | Must construct the regulator-dependent BV Laplacian, counterterms, anomaly cancellation, and QME. |
| Full mixed constructive theorem | Open | Requires stable interaction, measure support, uniform Borel bounds, and cutoff/volume convergence. |
| Physical reflection positivity | Open | Must hold on BRST-closed gauge-invariant correlators; TT positivity is insufficient. |
| Global physical Hilbert space and unitarity | Open | Requires the preceding gates plus complete OS/Lorentzian and infrared control. |

</div>

The minimal executable exit packet is therefore:

1.  one explicitly selected graded gravity field/antifield complex and gauge-invariant action;

2.  one common SPT spectral calculus with exact chain and boundary intertwining checks;

3.  one finite-cutoff BV measure packet verifying the QME and its anomaly rows;

4.  one constructive estimate packet proving common Borel domains and uniform remainder and removal bounds; and

5.  one physical OS packet evaluating every generator of the declared BRST-closed positive-time observable algebra and proving the completion hypotheses.

This packet would turn Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">12</a> from a compatibility theorem into a constructed quantum-gravity result.

# Conclusion

SPT filtering, BRST cohomology, Borel summation, and OS reconstruction are compatible only after their interfaces are proved. The shared-filter theorem gives the correct linear interface; the finite quantum-measure theorem gives the correct Ward interface; the uniform Borel theorem gives the correct summation interface; and the cohomological OS theorem gives the correct physical-state interface. The previous edition assumed these interfaces and therefore overstated its conclusion.

The present MTT program has meaningful ingredients on both sides of this contract: finite q79 gravity data, a classical gravitational action at a declared branch tier, a free helicity sector, and exact classical finite gauge BRST data. What remains is sharply localized in F2–F5. Until those objects are constructed, this paper establishes a rigorous dependency theorem and research target, not a nonperturbative unitary theory of quantum gravity.

<div class="thebibliography">

99

L. D. Faddeev and V. N. Popov, Feynman diagrams for the Yang–Mills field, *Phys. Lett. B* **25** (1967), 29–30, doi:10.1016/0370-2693(67)90067-6.

C. Becchi, A. Rouet, and R. Stora, Renormalization of gauge theories, *Ann. Phys.* **98** (1976), 287–321, doi:10.1016/0003-4916(76)90156-1.

I. A. Batalin and G. A. Vilkovisky, Gauge algebra and quantization, *Phys. Lett. B* **102** (1981), 27–31, doi:10.1016/0370-2693(81)90205-7.

M. Henneaux and C. Teitelboim, *Quantization of Gauge Systems*, Princeton University Press, 1992.

G. Barnich, F. Brandt, and M. Henneaux, Local BRST cohomology in gauge theories, *Phys. Rept.* **338** (2000), 439–569, doi:10.1016/S0370-1573(00)00049-1.

A. Schwarz, Geometry of Batalin–Vilkovisky quantization, *Commun. Math. Phys.* **155** (1993), 249–260, doi:10.1007/BF02097392.

K. Costello, Renormalisation and the Batalin–Vilkovisky formalism, arXiv:0706.1533, 2007.

P. M. Lavrov, BRST, Ward identities, gauge dependence, and a functional renormalization group, arXiv:2002.05997, 2020.

A. D. Sokal, An improvement of Watson’s theorem on Borel summability, *J. Math. Phys.* **21** (1980), 261–263, doi:10.1063/1.524408.

K. Osterwalder and R. Schrader, Axioms for Euclidean Green’s functions, *Commun. Math. Phys.* **31** (1973), 83–112, doi:10.1007/BF01645738.

K. Osterwalder and R. Schrader, Axioms for Euclidean Green’s functions II, *Commun. Math. Phys.* **42** (1975), 281–305, doi:10.1007/BF01608978.

T. Kugo and I. Ojima, Local covariant operator formalism of non-Abelian gauge theories and quark confinement problem, *Prog. Theor. Phys. Suppl.* **66** (1979), 1–130, doi:10.1143/PTPS.66.1.

W. Kalau and J. W. van Holten, BRST cohomology and BRST gauge fixing, *Nucl. Phys. B* **361** (1991), 233–252, doi:10.1016/0550-3213(91)90623-6.

M. Asorey, L. Rachwal, and I. Shapiro, Unitarity issues in higher derivative field theories, arXiv:1802.01036, 2018.

J. F. Donoghue, The effective field theory treatment of quantum gravity, arXiv:1209.3511, 2012.

P. Nero, *Fixed Points VI: Formal Synthesis and Physical Interpretations*, corrected v4, 2026.

P. Nero, *MTT Quantum-Gravity Research and Paper Status Audit*, research ledger, 2026.

P. Nero, *MTT SPT Gaussian, Stieltjes, and Graph-Rank Correction*, executable research note, 2026.

P. Nero, *Globally Hyperbolic SM Gauge-Stack Obstruction and BRST Theorem*, executable theorem packet, 2026.

</div>
