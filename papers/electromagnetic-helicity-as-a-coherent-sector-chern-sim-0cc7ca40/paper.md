---
abstract: |
  A smooth rank-one orthogonal projector on a Hermitian bundle defines a line subbundle and an induced unitary connection. This elementary construction provides a precise setting in which Berry curvature, Abelian Chern–Simons functionals, magnetic helicity, and Hopf invariants can be compared. We derive the induced curvature, including its projector term, and formulate helicity only after specifying a global trivialization or a relative-helicity protocol. The exact slice balance is the usual electric–magnetic pairing plus an explicit boundary flux. There is no additional projector remainder when the electric and magnetic fields are those of the full induced connection: projector variation is already part of those fields. A quantitative comparison theorem bounds the error made when the Berry curvature is omitted and only the ambient Abelian field is retained. We also give a correctly scaled Riesz-projector derivative estimate and state the Hopf normalization with all conventions visible. Modal Triplet Theory (MTT) can use this construction as a conditional encoding once a selected source emits the Hermitian bundle, connection, rank-one projector, physical field identification, and boundary data. Current MTT results do not yet establish that source theorem for the physical electromagnetic sector. The paper therefore proves an exact geometric dictionary and a controlled comparison result, not a universal electromagnetic prediction.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: Version 3, July 2026
generated_from_main_tex_sha256: e3d50561bc0fef5cb045401b572be80c5700106d999868c2c905f09894a54d53
paper_id: electromagnetic-helicity-as-a-coherent-sector-chern-sim-0cc7ca40
release_state: zenodo_released
released_version: v3
title: |
  **Electromagnetic Helicity from an Induced Line Connection
  Exact Chern–Simons Identities and a Conditional MTT Encoding**
zenodo_doi: 10.5281/zenodo.21713347
zenodo_record_id: 21713347
zenodo_url: "https://zenodo.org/records/21713347"
---

# Revision note for Version 3

<div class="description">

Version 2, DOI [10.5281/zenodo.18261452](https://doi.org/10.5281/zenodo.18261452).

Version 2 correctly retained the Berry term in the induced curvature, but it then counted projector variation a second time as a remainder in the exact helicity balance. It also contracted a spatial two-form to define the electric field, mixed two Hopf normalizations, and treated a candidate rank-one coherent line as the selected physical electromagnetic sector.

Version 3 distinguishes the full spacetime curvature from its spatial and electric parts, proves the boundary-aware balance for the full induced field, and uses projector control only for the error made by an ambient-field surrogate. It declares the global gauge and topology domain, fixes the Hopf and Riesz constants, and makes physical MTT sourcing a six-row conditional contract.

The projected-connection construction and the fact that its curvature contains a Berry/Grassmann term remain valid. The revision changes the balance-law bookkeeping and physical claim status, not that underlying geometry.

Current MTT results do not yet select the physical photon line, identify the induced curvature with the physical electromagnetic field, or transport the required dynamics. Those source rows remain explicit conditions rather than results of this paper.

</div>

# Purpose and corrected scope

Magnetic helicity is often written as
``` math
H=\int_\Sigma \bm A\cdot\bm B\,d^3x
  =\int_\Sigma a\wedge da.
```
The compact formula hides three separate questions. First, does a global potential $`a`$ exist? Second, which gauge transformations and boundary conditions leave the integral unchanged? Third, if a projector defines a moving coherent line, is the relevant field the ambient Abelian field or the curvature of the induced line connection?

The needed ingredients are standard but belong to different literatures: Chern–Simons transgression , magnetic and relative helicity , and Berry holonomy . Keeping their domains distinct is what makes the combined statement reliable.

The purpose of this paper is to answer those questions in a typed order. The answer to the third is especially important. The projector contribution is not an extra force added after a Chern–Simons balance has been written. It is a part of the induced curvature itself. Consequently, the exact balance law for the total induced field has no separate “projector remainder.” Such a term appears only when one compares the total induced field with a surrogate that has deliberately omitted the Berry contribution.

This distinction also fixes the relation to MTT. Projection and spectral gaps can control a supplied coherent line. They do not, by themselves, prove that this line is the physical photon sector or that its curvature obeys Maxwell, magnetohydrodynamic, or other chosen dynamics. Those identifications belong to a source contract stated in <a href="#sec:mtt" data-reference-type="ref+label" data-reference="sec:mtt">9</a>.

# The typed geometric contract

Let $`I=[t_0,t_1]`$, let $`\Sigma`$ be an oriented Riemannian three-manifold, and set $`\mathcal U=I\times\Sigma`$. Write $`\iota_t:\Sigma\hookrightarrow\mathcal U`$ for the slice inclusion. The basic objects are listed in <a href="#tab:contract" data-reference-type="ref+label" data-reference="tab:contract">1</a>.

<div id="tab:contract">

| Object | Type | Role |
|:---|:---|:---|
| $`\mathcal E\to\mathcal U`$ | Hermitian vector bundle | Ambient carrier |
| $`D`$ | Unitary connection on $`\mathcal E`$ | Ambient parallel transport |
| $`P`$ | $`C^2`$ rank-one orthogonal projection | Defines $`\mathcal L=\operatorname{Ran}P`$ |
| $`\nabla^\mathcal L=P D`$ | Unitary connection on $`\mathcal L`$ | Total induced connection |
| $`f=-iF_{\nabla^\mathcal L}`$ | Real two-form on $`\mathcal U`$ | Total induced field strength |
| $`b_t=\iota_t^*f`$ | Spatial two-form | Magnetic part |
| $`e_t=-\iota_t^*(\iota_{\partial_t}f)`$ | Spatial one-form | Electric part |
| Boundary protocol | Closed slice, decay, or relative data | Makes helicity typed |

The minimal geometric data. No physical interpretation is inferred from these types alone.

</div>

The sign in the definition of $`e_t`$ is chosen so that, in a global gauge $`\mathcal A=\phi\,dt+a_t`$,
``` math
f=d\mathcal A
  =dt\wedge(\dot a_t-d_\Sigma\phi)+d_\Sigma a_t,
\qquad
e_t=d_\Sigma\phi-\dot a_t.
```
Other sign conventions are equivalent after changing all balance formulas consistently.

# The induced line connection

<div id="def:projected-connection" class="definition">

**Definition 1** (Projected connection). For a section $`s`$ of $`\mathcal L=\operatorname{Ran}P`$, define
``` math
\nabla^\mathcal Ls:=P(Ds).
```

</div>

Because $`P`$ is orthogonal and $`D`$ is unitary, $`\nabla^\mathcal L`$ is a unitary connection. It depends on both the ambient connection and the way the range of $`P`$ turns inside $`\mathcal E`$.

<div id="thm:projected-curvature" class="theorem">

**Theorem 2** (Curvature of the projected connection). *Let $`F_D=D^2`$ and let $`DP=[D,P]`$. The curvature of $`\nabla^\mathcal L`$ is
``` math
F_{\nabla^\mathcal L}
 =P F_D P+P(DP)\wedge(DP)P
```
as an endomorphism-valued two-form restricted to $`\mathcal L`$.*

</div>

<div class="proof">

*Proof.* For $`s=Ps`$,
``` math
(P D)^2s=P D(PDs)
       =P(DP)\wedge Ds+P D^2s.
```
Differentiate $`P^2=P`$ to obtain $`P(DP)P=0`$. Splitting $`Ds=P Ds+(1-P)Ds`$ and using $`(1-P)Ds=(DP)s`$ gives the stated Grassmann-curvature term. ◻

</div>

The most transparent specialization is an ambient scalar $`U(1)`$ connection. Suppose that, in a local frame,
``` math
D=d+iA\,\mathrm{Id}_{\mathcal E},
```
where $`A`$ is a real one-form. Then $`DP=dP`$, $`F_D=i\,dA`$, and the real curvature of the induced line is
``` math
\begin{equation}
f=dA+q_P,
\qquad
q_P:=-i\,\mathop{\mathrm{Tr}}\!\bigl(P\,dP\wedge dP\bigr).
\label{eq:curvature-split}
\end{equation}
```
The second term is the Berry or Grassmann curvature. In a local unit section $`u`$ with $`P=|u\rangle\langle u|`$, the induced real connection form is
``` math
\mathcal A=A-i\langle u,du\rangle,
\qquad
f=d\mathcal A.
```
Under $`u\mapsto e^{i\chi}u`$, this local form changes by $`\mathcal A\mapsto\mathcal A+d\chi`$, while $`f`$ is unchanged.

# When helicity is a real-valued functional

The local formula for $`\mathcal A`$ does not guarantee a global real one-form on a slice. A nontrivial line bundle has no global unit frame, and even a trivial bundle requires a boundary and gauge convention before $`\int a\wedge da`$ is an invariant real number.

<div id="ass:absolute-domain" class="assumption">

**Assumption 3** (Absolute-helicity domain). For each time under consideration, $`\mathcal L|_{\Sigma_t}`$ is supplied with a global unitary trivialization. In that trivialization, $`a_t=\iota_t^*\mathcal A`$ and $`b_t=d_\Sigma a_t`$. In addition, one of the following holds:

1.  $`\Sigma`$ is closed and allowed gauge transformations lift to single-valued real functions $`\chi`$;

2.  $`\Sigma=\mathbb R^3`$ and all fields and gauge functions decay enough to remove the boundary term; or

3.  a boundary gauge is fixed so that the flux terms displayed below are part of the data.

</div>

<div id="def:helicity" class="definition">

**Definition 4** (Induced helicity). On the domain of Assumption <a href="#ass:absolute-domain" data-reference-type="ref" data-reference="ass:absolute-domain">3</a>, define
``` math
H_\mathcal L(t):=\int_\Sigma a_t\wedge b_t.
```

</div>

<div id="prop:gauge-change" class="proposition">

**Proposition 5** (Gauge change). *Under $`a_t\mapsto a_t+d_\Sigma\chi_t`$,
``` math
H_\mathcal L\mapsto H_\mathcal L+\int_{\partial\Sigma}\chi_t b_t.
```
Thus $`H_\mathcal L`$ is invariant for closed slices and for the decay or fixed boundary protocols in Assumption <a href="#ass:absolute-domain" data-reference-type="ref" data-reference="ass:absolute-domain">3</a>. On a general open or multiply connected domain, one must instead supply a reference field and use relative helicity, or retain the boundary term explicitly.*

</div>

<div class="proof">

*Proof.* Since $`d_\Sigma b_t=0`$,
``` math
\int_\Sigma d_\Sigma\chi_t\wedge b_t
 =\int_\Sigma d_\Sigma(\chi_t b_t)
 =\int_{\partial\Sigma}\chi_t b_t.
```
 ◻

</div>

For a nontrivial line bundle, Abelian Chern–Simons data can still be formulated relative to a reference connection or as a differential character, generally with a value defined modulo a period lattice. That construction is not the same object as the real-valued absolute helicity in Definition <a href="#def:helicity" data-reference-type="ref" data-reference="def:helicity">4</a>. This paper uses the latter only on its declared domain.

# Exact balance and boundary flux

<div id="thm:balance" class="theorem">

**Theorem 6** (Exact induced-helicity balance). *Assume Assumption <a href="#ass:absolute-domain" data-reference-type="ref" data-reference="ass:absolute-domain">3</a> and write the full induced connection as $`\mathcal A=\phi\,dt+a_t`$. Then
``` math
\begin{equation}
\frac{d}{dt}H_\mathcal L(t)
=-2\int_\Sigma e_t\wedge b_t
 \int_{\partial\Sigma}\bigl(\phi b_t+a_t\wedge e_t\bigr).
\label{eq:balance}
\end{equation}
```
In particular, on a closed slice or under a protocol that removes the displayed boundary flux,
``` math
\frac{d}{dt}H_\mathcal L(t)=-2\int_\Sigma e_t\wedge b_t.
```
The formula contains no additional projector remainder.*

</div>

<div class="proof">

*Proof.* Differentiate $`H_\mathcal L=\int_\Sigma a_t\wedge d_\Sigma a_t`$. Stokes’ theorem gives
``` math
\frac{dH_\mathcal L}{dt}
=2\int_\Sigma \dot a_t\wedge b_t
-\int_{\partial\Sigma}a_t\wedge\dot a_t.
```
Substitute $`\dot a_t=d_\Sigma\phi-e_t`$, use $`d_\Sigma b_t=0`$, and integrate the exact boundary two-form $`d_\Sigma(\phi a_t)`$ over $`\partial\Sigma`$. This yields <a href="#eq:balance" data-reference-type="ref+label" data-reference="eq:balance">[eq:balance]</a>. ◻

</div>

<div id="cor:conservation" class="corollary">

**Corollary 7** (Conservation criterion). *Under vanishing boundary flux, $`H_\mathcal L`$ is conserved whenever $`\int_\Sigma e_t\wedge b_t=0`$. Pointwise ideal evolution $`e_t\wedge b_t=0`$ is sufficient but not necessary.*

</div>

Small projector derivatives alone do not imply helicity conservation. They control only the Berry part of the field. The ambient contribution to $`e_t\wedge b_t`$ may remain nonzero.

# What projector control actually bounds

Let
``` math
f_0=dA,\qquad f=f_0+q_P
```
be the ambient and induced real curvatures from <a href="#eq:curvature-split" data-reference-type="ref+label" data-reference="eq:curvature-split">[eq:curvature-split]</a>. Decompose them on a slice as
``` math
b=b_0+\Delta b,\qquad e=e_0+\Delta e,
```
where
``` math
\Delta b=\iota_t^*q_P,
\qquad
\Delta e=-\iota_t^*(\iota_{\partial_t}q_P).
```

<div id="prop:berry-bounds" class="proposition">

**Proposition 8** (Berry-curvature component bounds). *For tangent vectors $`X,Y`$,
``` math
|q_P(X,Y)|
\le 2\,\|d_XP\|_{\mathrm{op}}\,\|d_YP\|_{\mathrm{op}}.
```
Consequently, up to fixed norm-equivalence constants determined by the metric on $`\Sigma`$,
``` math
|\Delta b|\le 2|d_\Sigma P|^2,
\qquad
|\Delta e|\le 2|\partial_tP|\,|d_\Sigma P|.
```*

</div>

<div class="proof">

*Proof.* Expand the wedge product:
``` math
q_P(X,Y)
=-i\,\mathop{\mathrm{Tr}}\!\left(P(d_XP\,d_YP-d_YP\,d_XP)\right).
```
Because $`P`$ has rank one, the trace of $`PT`$ is bounded by $`\|T\|_{\mathrm{op}}`$. Apply submultiplicativity to the two terms. ◻

</div>

The next result places the old “remainder” in its correct role. It measures the error in using the ambient field instead of the induced field; it is not an extra term in <a href="#thm:balance" data-reference-type="ref+label" data-reference="thm:balance">6</a>.

<div id="thm:surrogate-error" class="theorem">

**Theorem 9** (Ambient-surrogate rate error). *Assume the boundary flux vanishes and all displayed fields are in $`L^2`$. Let
``` math
\dot H_{\rm ind}:=-2\int_\Sigma e\wedge b,
\qquad
\dot H_{\rm amb}:=-2\int_\Sigma e_0\wedge b_0.
```
Then
``` math
\begin{align}
|\dot H_{\rm ind}-\dot H_{\rm amb}|
\le 2\bigl(&\|\Delta e\|_{L^2}\|b_0\|_{L^2}
 \|e_0\|_{L^2}\|\Delta b\|_{L^2}\notag\\
&+\|\Delta e\|_{L^2}\|\Delta b\|_{L^2}\bigr).
\label{eq:surrogate-bound}
\end{align}
```*

</div>

<div class="proof">

*Proof.* Expand $`(e_0+\Delta e)\wedge(b_0+\Delta b)-e_0\wedge b_0`$ and apply Cauchy–Schwarz to each of the three remaining pairings. ◻

</div>

Combining Proposition <a href="#prop:berry-bounds" data-reference-type="ref" data-reference="prop:berry-bounds">8</a> and Theorem <a href="#thm:surrogate-error" data-reference-type="ref" data-reference="thm:surrogate-error">9</a> gives a quantitative adiabatic comparison whenever $`\partial_tP`$ and $`d_\Sigma P`$ are controlled. The estimate does not erase the Berry term and does not turn a nonconserved ambient field into a conserved induced one.

# Hopf specialization and normalization

Let $`\Omega_{S^2}`$ be the standard oriented area form on the unit two-sphere, normalized by
``` math
\int_{S^2}\Omega_{S^2}=4\pi.
```

<div id="thm:hopf" class="theorem">

**Theorem 10** (Whitehead integral formula in the chosen normalization). *Let $`n:S^3\to S^2`$ be smooth. Since $`H^2_{\mathrm{dR}}(S^3)=0`$, choose a real one-form $`a`$ satisfying
``` math
da=n^*\Omega_{S^2}.
```
Then
``` math
\operatorname{Hopf}(n)
=\frac{1}{16\pi^2}\int_{S^3}a\wedge da
\in\mathbb Z.
```
The value is independent of the choice of $`a`$.*

</div>

<div class="proof">

*Proof.* This is Whitehead’s integral formula with the area form of total area $`4\pi`$. If $`a'`$ is another primitive, then $`a'-a`$ is closed and hence exact on $`S^3`$. The resulting change of the integral is the integral of an exact three-form and vanishes. ◻

</div>

If instead one uses $`\omega_{S^2}=\Omega_{S^2}/(4\pi)`$, whose integral is one, and $`d\alpha=n^*\omega_{S^2}`$, the same statement reads $`\operatorname{Hopf}(n)=\int_{S^3}\alpha\wedge d\alpha`$. Mixing these two normalizations is a common source of an erroneous factor of $`16\pi^2`$; the integral construction is due to Whitehead .

For an induced MTT line connection, integer Hopf quantization follows only if its spatial curvature is actually of the form $`n^*\Omega_{S^2}`$ for a specified map $`n`$. Rank one, coherence, or a spectral gap does not imply that pullback condition.

# Riesz projectors and correctly scaled derivative bounds

Projector control can be obtained from a gapped operator family, but the operator domain and the gap scaling must be explicit.

<div id="thm:riesz" class="theorem">

**Theorem 11** (Bounded-family Riesz estimate). *Let $`y\mapsto L(y)`$ be a $`C^1`$ family of bounded self-adjoint operators on a fixed Hilbert space. Suppose
``` math
\sigma(L(y))\subset\{0\}\cup[\lambda_*,\infty),
\qquad \lambda_*>0,
```
and the multiplicity of the zero eigenspace is constant. Let $`P(y)`$ be the orthogonal projection onto $`\ker L(y)`$. For the positively oriented circle $`\Gamma=\{z:|z|=\lambda_*/2\}`$,
``` math
P(y)=\frac{1}{2\pi i}\oint_\Gamma (z-L(y))^{-1}\,dz
```
and, for every parameter direction $`v`$,
``` math
\partial_vP
=\frac{1}{2\pi i}\oint_\Gamma
(z-L)^{-1}(\partial_vL)(z-L)^{-1}\,dz.
```
Moreover,
``` math
\begin{equation}
\|\partial_vP\|_{\mathrm{op}}
\le \frac{2}{\lambda_*}\,
\|\partial_vL\|_{\mathrm{op}}.
\label{eq:riesz-bound}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Differentiate the resolvent identity under the contour integral. On $`\Gamma`$, self-adjointness and the spectral assumption give $`\|(z-L)^{-1}\|\le2/\lambda_*`$. Since $`\operatorname{len}(\Gamma)=\pi\lambda_*`$, the contour estimate is
``` math
\frac{\pi\lambda_*}{2\pi}
\left(\frac{2}{\lambda_*}\right)^2
\|\partial_vL\|
=\frac{2}{\lambda_*}\|\partial_vL\|.
```
 ◻

</div>

For unbounded Laplace-type families, norm differentiability in $`\mathcal B(\mathcal{H})`$ is generally the wrong hypothesis. One instead fixes a common domain or uses graph-norm and relative-resolvent bounds, as in Kato perturbation theory. The same contour identity remains available after those domain hypotheses are supplied. This paper does not silently replace that unbounded problem by the bounded theorem above. The relevant perturbation framework is developed systematically by Kato .

# Conditional MTT encoding

The preceding results are ordinary differential geometry and functional analysis. MTT enters only through a proposed source for the typed data. The current scope is aligned with the revised Foundation, fixed-point, and topological-encoding papers .

<div id="def:source-contract" class="definition">

**Definition 12** (Electromagnetic source contract). An MTT electromagnetic source packet on $`\mathcal U`$ must provide:

1.  a Hermitian carrier $`(\mathcal E,D)`$;

2.  a $`C^2`$, constant-rank, rank-one projector $`P`$;

3.  a theorem identifying $`\operatorname{Ran}P`$, rather than merely an isomorphic line, with the physical electromagnetic sector;

4.  an intertwiner identifying $`-iF_{PD}`$ with the physical electromagnetic field strength and preserving its dynamics;

5.  a trivialization, relative connection, or differential-character protocol that types the claimed helicity observable;

6.  when Hopf quantization is claimed, a selected map $`n:S^3\to S^2`$ and the equality $`\iota_t^*(-iF_{PD})=n^*\Omega_{S^2}`$.

</div>

<div id="thm:conditional-pullback" class="theorem">

**Theorem 13** (Conditional pullback of helicity statements). *If an MTT source packet satisfies S1–S5, then Theorem <a href="#thm:projected-curvature" data-reference-type="ref" data-reference="thm:projected-curvature">2</a>, Proposition <a href="#prop:gauge-change" data-reference-type="ref" data-reference="prop:gauge-change">5</a>, Theorem <a href="#thm:balance" data-reference-type="ref" data-reference="thm:balance">6</a>, Proposition <a href="#prop:berry-bounds" data-reference-type="ref" data-reference="prop:berry-bounds">8</a>, and Theorem <a href="#thm:surrogate-error" data-reference-type="ref" data-reference="thm:surrogate-error">9</a> apply to the emitted physical electromagnetic sector. If S6 also holds, <a href="#thm:hopf" data-reference-type="ref+label" data-reference="thm:hopf">10</a> supplies the integer Hopf invariant. If $`P`$ is emitted as the kernel projector of a bounded family satisfying <a href="#thm:riesz" data-reference-type="ref+label" data-reference="thm:riesz">11</a>, then <a href="#eq:riesz-bound" data-reference-type="ref+label" data-reference="eq:riesz-bound">[eq:riesz-bound]</a> controls its parameter derivatives.*

</div>

<div class="proof">

*Proof.* Each source row identifies an emitted object with the corresponding typed hypothesis of the cited result. Composition with the stated intertwiners therefore transports those identities without changing their domains. ◻

</div>

<div id="tab:mtt-status">

| Rows | Status here | Meaning |
|:---|:---|:---|
| S1–S2 | Conditional representation data | Standard projected-connection mathematics applies once supplied |
| S3–S4 | Open source identification | No current theorem in this paper selects the physical photon line and its dynamics |
| S5 | Case-dependent | Closed, decaying, relative, and differential-character domains are distinct |
| S6 | Specialization only | Hopf quantization requires the explicit pullback condition |

Claim status of the MTT bridge.

</div>

The conditional theorem is useful because it states exactly what remains to be constructed. It is not evidence that S3–S4 already hold.

# What the paper establishes

The durable mathematical conclusions are:

1.  a rank-one projector and ambient unitary connection define an induced line connection with the exact curvature in <a href="#thm:projected-curvature" data-reference-type="ref+label" data-reference="thm:projected-curvature">2</a>;

2.  absolute helicity is a typed observable only after trivialization, gauge, and boundary data are fixed;

3.  the exact balance law is <a href="#eq:balance" data-reference-type="ref+label" data-reference="eq:balance">[eq:balance]</a>;

4.  omission of the Berry curvature has the controlled comparison error in <a href="#eq:surrogate-bound" data-reference-type="ref+label" data-reference="eq:surrogate-bound">[eq:surrogate-bound]</a>;

5.  Hopf quantization is valid under the explicit pullback and normalization in <a href="#thm:hopf" data-reference-type="ref+label" data-reference="thm:hopf">10</a>; and

6.  a spectral gap controls a bounded-family Riesz projector with scaling $`1/\lambda_*`$, not an unexplained $`1/\lambda_*^2`$ factor.

The paper does not derive Maxwell’s equations, ideal magnetohydrodynamics, a physical photon sector, a universal helicity conservation law, or a universal topological classification from MTT. Those claims require the source and dynamical rows in Definition <a href="#def:source-contract" data-reference-type="ref" data-reference="def:source-contract">12</a>.

# Version 3 changes and reasons

<div class="center">

| Change | Earlier issue | Reason |
|:---|:---|:---|
| Retitled and reclassified as a conditional encoding | The previous title implied that MTT had selected the physical coherent electromagnetic line | The selected physical source remains open |
| Replaced the projector-remainder balance | Projector variation was counted once in the induced field and again as a remainder | The exact balance must use the full connection; comparison error is a separate question |
| Separated spacetime and slice forms | The electric field was defined by contracting a spatial two-form | The contraction must be taken before pullback to the slice |
| Added gauge, topology, and boundary domains | A local connection form was treated as a global helicity potential | Nontrivial bundles and open domains require relative or differential data |
| Fixed the Hopf convention | The normalized area form and the factor $`1/(16\pi^2)`$ were mixed | The coefficient depends on whether the sphere area is $`4\pi`$ or $`1`$ |
| Corrected the Riesz estimate | The contour constant obscured the gap dimension and unbounded-domain issue | The bounded theorem gives $`2\|\partial L\|/\lambda_*`$; Laplace-type families need graph-domain hypotheses |

</div>

# Discussion

The main conceptual lesson is modest but useful. A varying projector can produce a genuine geometric contribution to an Abelian field strength. That contribution is neither optional nor mysterious: it is the curvature of the projected connection. Once it is included, the usual Chern–Simons calculus works without modification. The new quantitative question is how far the induced field lies from an ambient-field approximation, and <a href="#thm:surrogate-error" data-reference-type="ref+label" data-reference="thm:surrogate-error">9</a> answers that question on its stated domain.

For MTT, this yields a clean research target. A future source theorem should not merely point to a rank-one coherent subspace. It must identify the same line and connection with the physical electromagnetic sector, transport the dynamics, and specify the global observable domain. If that target is met, the geometric results in this paper apply immediately. Until then, they are a rigorous compatibility and completion contract.
