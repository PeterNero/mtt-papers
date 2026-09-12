---
abstract: |
  We determine which parts of two proposed heterotic flux constructions survive the full Hull–Strominger proof obligations. The diagonal invariant Hermitian structure on the Iwasawa manifold is balanced, and its torsion and $`\mathrm{d}H`$ are computed exactly. The proposed bundle, however, does not exist as claimed. One of its alleged first-Chern forms is not closed; the monad maps were not constructed as global sections; the printed Dolbeault operator is not integrable; and a connection on the stated trivial smooth rank-three carrier cannot have third Chern number six. Within the declared one-entry repair ansatz, the Maurer–Cartan equation has a unique signed repair, but the repaired family is a single complex-gauge orbit with a non-scalar holomorphic commutant, so it cannot supply the claimed stable bundle. The old anomaly, three-generation, and normalized-Yukawa conclusions therefore do not follow. The printed Lens–Nil forms fail balancedness and positivity of the associated metric, and their almost-complex structure is non-integrable. We finish by separating the exact $`q=79`$ finite and rank-two Hermitian–Yang–Mills evidence, and the existential projective rank-nine hidden connection, from the still-open common visible–hidden problem, and state a typed completion contract for a future Fu–Yau endpoint. The selected eta9 source, integral comparison, localized residue construction, and certified local response are explained without identifying them with an unevaluated global Deligne obstruction.
author:
- Peter Nero
bibliography:
- references.bib
current_version: v7
date: September 2026, Version 7
generated_from_main_tex_sha256: fbbdd6d99251d02dd737df8008fd340b1f20e604dd53d8e34b9cea0c348b27f4
paper_id: flux-compactifications-in-heterotic-string-theory-expli-08b38155
release_state: current_revised_tex
released_version: v4
title: |
  Auditing Heterotic Flux Compactifications on Iwasawa and Lens–Nil Geometries:
  Bundle Obstructions and a $`q=79`$ Fu–Yau Completion Contract
zenodo_doi: 10.5281/zenodo.21705964
zenodo_record_id: 21705964
zenodo_url: "https://zenodo.org/records/21705964"
---

# Version 7 Revision Note

**Supersedes.** Unreleased Version 6; Version 4 remains the released edition. **Reason.** The frozen q79 source sequence required contextual integration, and rereading the invariant forms exposed local sign and prerequisite errors. **Resolution.** Adds the arithmetic, integral-lattice, Koszul–Cech, finite-action and local-response dependency chain; includes all three Maurer–Cartan conditions, corrects the sign of $`\mathrm{d}H`$, and evaluates the printed Lens–Nil forms directly. **Retained results.** Iwasawa balancedness, the failed-bundle audit, the signed repair obstruction, finite q79 and rank-two HYM results, hidden rank-nine existence, and the T69–T73 local/global distinctions survive. **Open boundary.** The selected visible bundle, global period-class decision, common HYM chamber and pointwise Bianchi data remain unsupplied.

# Version 6 Revision Note

**Supersedes.** The unreleased Version 5; Version 4 remains the released edition. **Reason.** The baseline table understated the later hidden-sector existence results. **Resolution.** Distinguishes the constructed projective rank-nine hidden carrier and existential HYM connection from the unevaluated numerical chamber and common physical pair. **Retained results.** The Iwasawa audit and the local/global q79 reconciliation are unchanged. **Remaining boundary.** Visible-source selection, explicit common connections and pointwise Bianchi cancellation are not supplied by the hidden existence theorem.

# Version 5 Revision Note

**Supersedes.** Version 4, which remains the released edition. **Reason and resolution.** Incorporates the new local q79 response certificates and the correction separating a fixed-fiber Picard test from the global BHT obstruction. **Retained results.** The Iwasawa audit and typed compactification contract are unchanged. **Boundary.** The new certificates do not construct the selected common physical endpoint.

# Introduction

The Hull–Strominger system is attractive because geometry, gauge data, torsion, and anomaly cancellation must all hold on the same compact complex threefold. That coupling also makes proposed solutions unusually easy to overstate. A balanced metric is not yet a heterotic vacuum; a formal matrix of $`(0,1)`$-forms is not yet a holomorphic bundle; a cohomological Chern-class identity is not yet the differential Bianchi identity; and a topological index is not yet a computed four-dimensional Yukawa coupling.

An earlier version of this paper presented explicit solutions on the Iwasawa manifold and on a Lens–Nil geometry. The present version re-executes those claims against the mathematical type of every object. The result is mixed but useful:

1.  the local Iwasawa $`SU(3)`$-structure and torsion calculation survives;

2.  the proposed Iwasawa rank-three bundle, anomaly match, generation count, and Yukawa normalization do not survive;

3.  Lens and Nil remain auxiliary geometric labels, but the printed differential forms do not define the claimed balanced compactification;

4.  the selected $`q=79`$ branch remains a plausible Fu–Yau-oriented research direction, with exact finite and separate rank-two HYM results, but its physical visible–hidden bundle endpoint is still open.

This is not a no-go theorem for all heterotic solutions on the Iwasawa manifold. Invariant solutions on complex Lie groups and nilmanifolds are known under carefully specified choices of tangent and gauge connections . The result here is narrower: the particular bundle and coefficient chain printed in the earlier paper does not establish such a solution.

## What is proved and what is not

<div class="center">

| Object | Status here | Meaning |
|:---|:---|:---|
| Iwasawa diagonal $`SU(3)`$ structure | proved | Complex, balanced, non-Kähler; $`H`$ and $`\mathrm{d}H`$ are explicit. |
| Old Iwasawa monad | withdrawn | Its Chern data and global maps were not defined. |
| Old Dolbeault matrix | disproved | Its Maurer–Cartan residual is nonzero. |
| Minimal signed repair | proved but rejected | Integrable, yet gauge-redundant and non-simple; not a stable visible bundle. |
| Old Bianchi and Yukawa chain | withdrawn | It depends on the invalid bundle and on further unproved inputs. |
| Lens–Nil forms | rejected as printed | Not balanced or positive Hermitian; the displayed complex coframe is non-integrable. |
| $`q=79`$ Fu–Yau endpoint | open | Finite, rank-two and hidden rank-nine results exist; the common physical visible–hidden Hull–Strominger tuple is not yet constructed. |

</div>

# The proof obligations for a heterotic solution

Let $`X`$ be a compact complex threefold with a nowhere-vanishing holomorphic $`(3,0)`$-form $`\Omega`$, Hermitian form $`\omega`$, dilaton $`\Phi`$, gauge bundle $`V`$, and unitary connections $`A`$ on $`V`$ and $`\nabla`$ on $`TX`$. In one standard first-order convention, the Hull–Strominger equations include
``` math
\begin{align}
\mathrm{d}\!\left(\|\Omega\|_\omega\omega^2\right)&=0,
\label{eq:balanced}\\
F_A^{0,2}=0,\qquad F_A\wedge\omega^2&=0,
\label{eq:hym}\\
H=\mathrm{i}(\bar\partial-\partial)\omega,\qquad
\mathrm{d}H&=\frac{\alpha'}{4}
\left(\mathrm{tr}R_\nabla\wedge R_\nabla-\mathrm{tr}F_A\wedge F_A\right).
\label{eq:bianchi}
\end{align}
```
Trace normalization and the choice of $`\nabla`$ must be fixed consistently. If the supersymmetry equations are also required to imply the first-order equations of motion, the tangent connection must obey the corresponding instanton condition. These choices cannot be changed midway through a coefficient comparison .

In the mathematical normalization one identifies $`\|\Omega\|_\omega`$ with the dilaton factor up to convention. For constant dilaton and constant $`\|\Omega\|_\omega`$, Equation <a href="#eq:balanced" data-reference-type="eqref" data-reference="eq:balanced">[eq:balanced]</a> reduces to $`\mathrm{d}(\omega^2)=0`$. This balanced condition is one row of the system, not a replacement for the other rows.

<div class="definition">

**Definition 1** (Complete first-order certificate). A complete certificate for a background in the convention above contains:

1.  an integrable complex threefold and global $`\Omega`$;

2.  a positive Hermitian form satisfying the conformally balanced equation;

3.  actual holomorphic gauge bundles and HYM connections;

4.  a specified tangent connection and its curvature;

5.  equality of the differential four-forms in Equation <a href="#eq:bianchi" data-reference-type="eqref" data-reference="eq:bianchi">[eq:bianchi]</a>;

6.  the required integral or differential-cohomological flux data.

</div>

Topological equality $`c_2(TX)=c_2(V)`$ can be necessary, but it does not determine the chosen curvature representatives. Likewise, the Li–Yau theorem supplies an HYM connection after the relevant stability hypotheses are proved; it does not turn a partial search for invariant sections into a stability proof . Established constructions make these dependencies explicit, for example the Fu–Yau solutions and stable-bundle perturbative constructions .

# The surviving Iwasawa geometry

Let $`X=\Gamma\backslash H_3(\mathbb{C})`$ be an Iwasawa manifold with global left-invariant $`(1,0)`$-forms
``` math
\begin{equation}
\mathrm{d}\omega^1=\mathrm{d}\omega^2=0,\qquad
\mathrm{d}\omega^3=\omega^1\wedge\omega^2.
\label{eq:iwasawa}
\end{equation}
```
For $`r_j>0`$, set
``` math
\begin{equation}
\omega=\frac{\mathrm{i}}{2}\sum_{j=1}^3 r_j^2
\omega^j\wedge\bar\omega^j,\qquad
\Omega=\omega^1\wedge\omega^2\wedge\omega^3.
\label{eq:su3}
\end{equation}
```

<div id="prop:geometry" class="proposition">

**Proposition 2** (Exact invariant geometry). *The structure in Equation <a href="#eq:su3" data-reference-type="eqref" data-reference="eq:su3">[eq:su3]</a> is complex, balanced, and non-Kähler. With $`H=\mathrm{i}(\bar\partial-\partial)\omega`$,
``` math
\begin{align}
H={}&\frac{r_3^2}{2}\left(
\omega^3\wedge\bar\omega^1\wedge\bar\omega^2
+\omega^1\wedge\omega^2\wedge\bar\omega^3\right),
\label{eq:H}\\
\mathrm{d}H={}&-r_3^2\,
\omega^1\wedge\bar\omega^1\wedge
\omega^2\wedge\bar\omega^2.
\label{eq:dH}
\end{align}
```*

</div>

<div class="proof">

*Proof.* The structure equations have no $`(0,2)`$ component, so the declared almost-complex structure is integrable. Also $`\mathrm{d}\Omega=0`$, because the only possible term contains $`\omega^1\wedge\omega^2\wedge\omega^1\wedge\omega^2`$. The only nonclosed summand of $`\omega`$ is the $`j=3`$ summand. When $`\mathrm{d}\omega`$ is wedged with either of the remaining diagonal summands, a repeated $`\omega^1`$ or $`\omega^2`$ occurs. Hence $`\mathrm{d}(\omega^2)=2\mathrm{d}\omega\wedge\omega=0`$. Since $`\mathrm{d}\omega\neq0`$, the metric is not Kähler. Splitting Equation <a href="#eq:iwasawa" data-reference-type="eqref" data-reference="eq:iwasawa">[eq:iwasawa]</a> into types gives
``` math
\partial\omega=\frac{\mathrm{i}r_3^2}{2}
\omega^1\wedge\omega^2\wedge\bar\omega^3,\qquad
\bar\partial\omega=-\frac{\mathrm{i}r_3^2}{2}
\omega^3\wedge\bar\omega^1\wedge\bar\omega^2,
```
which yields Equations <a href="#eq:H" data-reference-type="eqref" data-reference="eq:H">[eq:H]</a> and <a href="#eq:dH" data-reference-type="eqref" data-reference="eq:dH">[eq:dH]</a>. ◻

</div>

Define the invariant diagonal $`(1,1)`$-forms
``` math
\begin{equation}
a=\frac{\mathrm{i}}{2}\omega^1\wedge\bar\omega^1,\qquad
b=\frac{\mathrm{i}}{2}\omega^2\wedge\bar\omega^2,\qquad
c=\frac{\mathrm{i}}{2}\omega^3\wedge\bar\omega^3.
\label{eq:abc}
\end{equation}
```
Then Equation <a href="#eq:dH" data-reference-type="eqref" data-reference="eq:dH">[eq:dH]</a> is equivalently
``` math
\begin{equation}
\mathrm{d}H=4r_3^2\,a\wedge b.
\label{eq:dHab}
\end{equation}
```
The earlier construction treated all three forms in Equation <a href="#eq:abc" data-reference-type="eqref" data-reference="eq:abc">[eq:abc]</a> as first-Chern representatives. That is the first decisive type error.

<div id="prop:closed" class="proposition">

**Proposition 3** (Closed-form obstruction). *Within the span of $`a,b,c`$, a form $`x a+y b+z c`$ is closed if and only if $`z=0`$. In particular, $`c`$ cannot represent the first Chern class of a line bundle.*

</div>

<div class="proof">

*Proof.* The first two forms are closed, while
``` math
\begin{equation}
\mathrm{d}c=\frac{\mathrm{i}}{2}\left(
\omega^1\wedge\omega^2\wedge\bar\omega^3
-\omega^3\wedge\bar\omega^1\wedge\bar\omega^2\right)\neq0.
\label{eq:dc}
\end{equation}
```
The $`(2,1)`$ and $`(1,2)`$ summands in Equation <a href="#eq:dc" data-reference-type="eqref" data-reference="eq:dc">[eq:dc]</a> are linearly independent, so $`z\,\mathrm{d}c=0`$ exactly when $`z=0`$. A Chern–Weil representative of $`c_1`$ is closed; therefore $`c`$ is ineligible. Closedness is only the first gate: integrality must still be checked by periods on the chosen lattice. ◻

</div>

# Why the proposed rank-three bundle fails

## The monad data were not global bundle data

For a genuine monad
``` math
0\longrightarrow K_1\stackrel{f}{\longrightarrow}
\bigoplus_i L_i\stackrel{g}{\longrightarrow}K_2
\longrightarrow0,
```
the $`L_i,K_j`$ must first exist as line bundles. Every entry of $`f`$ and $`g`$ must then be a global holomorphic section of the appropriate Hom bundle, for example
``` math
g_i\in H^0\!\left(X,\mathrm{Hom}(L_i,K_2)\right)
=H^0\!\left(X,K_2\otimes L_i^{-1}\right).
```
A “constant matrix in a left-invariant frame” is not automatically such a section when its source and target line bundles are nonisomorphic.

The former monad used combinations containing $`c`$ as first-Chern data. Proposition <a href="#prop:closed" data-reference-type="ref" data-reference="prop:closed">3</a> prevents those line bundles from being defined with the advertised curvature. No global Hom sections, exactness loci, or locally free cohomology sheaf were supplied independently. Consequently the formal Chern-character arithmetic did not compute the Chern classes of an actual rank-three bundle.

The old stability argument had a second logical gap. The statement $`H^0(X,E)=0`$, even if proved, excludes a map $`\mathcal{O}_X\to E`$; it does not exclude every line bundle $`L`$ of nonnegative slope from mapping into $`E`$. Nor does checking invariant candidates exhaust all coherent subsheaves. Slope stability requires every proper torsion-free subsheaf to have smaller slope. The Li–Yau theorem becomes applicable only after that global condition is established.

## The printed Dolbeault operator is not integrable

Write a left-invariant candidate as
``` math
\begin{equation}
\bar\partial_E=\bar\partial+A,\qquad
A=B_1\bar\omega^1+B_2\bar\omega^2+B_3\bar\omega^3.
\label{eq:A}
\end{equation}
```
Because $`\bar\partial\bar\omega^3=\bar\omega^1\wedge\bar\omega^2`$, the Maurer–Cartan equation is
``` math
\begin{equation}
\bar\partial_E^2=0
\quad\Longleftrightarrow\quad
B_3+[B_1,B_2]=0,\qquad [B_1,B_3]=[B_2,B_3]=0.
\label{eq:MC}
\end{equation}
```

The earlier paper used
``` math
\begin{equation}
B_1=\sqrt{\mu}\,E_{13},\qquad
B_2=-\sqrt{\mu}\,E_{31},\qquad
B_3=\mu E_{12},\qquad \mu>0.
\label{eq:oldB}
\end{equation}
```
Substitution gives
``` math
B_3+[B_1,B_2]
=\mu(E_{12}-E_{11}+E_{33})\neq0.
```
Thus the printed operator does not define a holomorphic structure.

<div id="thm:repair" class="theorem">

**Theorem 4** (Minimal signed repair and its obstruction). *Within the declared one-entry signed repair in which the $`B_2`$ arrow is moved to the composable Heisenberg arrow, Equation <a href="#eq:MC" data-reference-type="eqref" data-reference="eq:MC">[eq:MC]</a> forces
``` math
\begin{equation}
B_1=\sqrt{\mu}\,E_{13},\qquad
B_2=-\sqrt{\mu}\,E_{32},\qquad
B_3=\mu E_{12}.
\label{eq:repair}
\end{equation}
```
This family is one $`SL(3,\mathbb{C})`$ complex-gauge orbit. Its holomorphic commutant has complex dimension two, so it is not simple and cannot be the claimed stable rank-three bundle.*

</div>

<div class="proof">

*Proof.* Since $`E_{13}E_{32}=E_{12}`$ and $`E_{32}E_{13}=0`$, $`[B_1,B_2]=-\mu E_{12}`$. Also $`E_{12}`$ commutes with both $`E_{13}`$ and $`E_{32}`$, so all three curvature components vanish. This proves integrability, not just cancellation in the $`\bar\omega^1\wedge\bar\omega^2`$ component. For
``` math
G_\mu=\operatorname{diag}(\sqrt{\mu},\mu^{-1/2},1)
\in SL(3,\mathbb{C}),
```
one has $`B_j(\mu)=G_\mu B_j(1)G_\mu^{-1}`$ for all three matrices. Hence $`\mu`$ labels complex gauge, not distinct holomorphic data. The matrices commuting with $`E_{13}`$, $`E_{32}`$, and $`E_{12}`$ are exactly
``` math
\{\,\lambda I+\nu E_{12}:\lambda,\nu\in\mathbb{C}\,\}.
```
The non-scalar element $`E_{12}`$ is therefore a holomorphic endomorphism. A slope-stable holomorphic vector bundle is simple, so the repaired object cannot satisfy the claimed stability conclusion. ◻

</div>

<div id="cor:trivial" class="corollary">

**Corollary 5** (Topological obstruction on the stated carrier). *If Equation <a href="#eq:A" data-reference-type="eqref" data-reference="eq:A">[eq:A]</a> is a connection on the stated smooth carrier $`E_{\mathrm{sm}}=X\times\mathbb{C}^3`$, then
``` math
c_1(E_{\mathrm{sm}})=c_2(E_{\mathrm{sm}})
=c_3(E_{\mathrm{sm}})=0.
```
In particular, it cannot have $`\int_Xc_3=6`$.*

</div>

<div class="proof">

*Proof.* The total Chern class of a trivial smooth bundle is one. Changing a connection changes a Chern–Weil representative by an exact transgression form, not the underlying characteristic class. A nonzero local six-form expression cannot override this topological fact. ◻

</div>

# Consequences for anomaly cancellation and Yukawa claims

The preceding obstruction propagates to every downstream claim that used the old bundle.

## The Bianchi identity

Complex parallelizability makes the holomorphic tangent bundle of the Iwasawa manifold trivial, so $`c_2(TX)=0`$. This gives a cohomological simplification, not the differential identity in Equation <a href="#eq:bianchi" data-reference-type="eqref" data-reference="eq:bianchi">[eq:bianchi]</a>. That identity still requires specified connections and their actual curvature four-forms.

The old hidden abelian flux also does not pass the stated HYM check. Its nonzero component was proportional to $`a+2b`$. For the positive diagonal metric,
``` math
\Lambda_\omega(a+2b)>0,
```
so it is not primitive. Placing the negative of the same form along an independent Cartan generator does not cancel a Lie-algebra-valued primitivity condition; each independent component must vanish. In addition, integer coefficients in an invariant coframe do not prove flux quantization until the period lattice is computed.

Because the visible connection is invalid, the hidden flux is not HYM as written, and the tangent-curvature convention was not independently certified, the former coefficient equation for $`r_3`$ is withdrawn. A rebuilt solution must recompute all three curvature terms from one declared set of connections.

## Generation number and Yukawa coupling

For a genuine special-unitary bundle on a compact complex threefold, an index formula can relate net chirality to $`\frac12\int_Xc_3(V)`$ under the standard hypotheses. Corollary <a href="#cor:trivial" data-reference-type="ref" data-reference="cor:trivial">5</a> shows that the old carrier does not provide the advertised value. The three-generation conclusion therefore does not follow from this Iwasawa construction.

A Yukawa coupling requires considerably more data:

1.  a valid holomorphic bundle and its relevant cohomology groups;

2.  normalized harmonic representatives for the matter modes;

3.  the bundle contraction or invariant tensor;

4.  evaluation of the corresponding overlap integral.

Orthonormality of three representatives does not imply that their wedge product equals $`\bar\Omega`$, even up to phase. The old assertion $`\lambda_{123}=1`$ and its rank-one mass interpretation are therefore withdrawn. This does not conflict with separate MTT finite/profile Yukawa results; it says only that this compactification did not derive them.

# Why Lens–Nil is not a Hull–Strominger solution

A real six-manifold can carry an $`SU(3)`$ structure $`(\omega,\Omega)`$ even when its induced almost-complex structure is not integrable. Conditions such as $`\mathrm{d}(\omega^2)=0`$ still make sense in that setting. The Hull–Strominger system, however, uses a complex threefold, holomorphic bundles, and the Dolbeault operators $`\partial,\bar\partial`$ with $`\bar\partial^2=0`$.

Nonclosedness of a chosen smooth $`(3,0)`$-form alone does not prove non-integrability. For the printed ansatz the failure can instead be checked directly. Write $`e^1,e^2,e^3=\eta^1,\eta^2,\eta^3`$ and $`e^4,e^5,e^6=\sigma^4,\sigma^5,\sigma^6`$, with
``` math
\mathrm{d}e^1=e^{23},\quad \mathrm{d}e^2=e^{31},\quad \mathrm{d}e^3=e^{12},
 \quad \mathrm{d}e^4=\mathrm{d}e^5=0,\quad \mathrm{d}e^6=e^{45}.
```
Here $`e^{ij}=e^i\wedge e^j`$. The earlier forms were
``` math
\omega_{\rm old}=a_L e^{12}+b_L e^{36}+c_L e^{45},\qquad
 \Omega_{\rm old}=(e^1+\mathrm{i}e^2)\wedge(e^3+\mathrm{i}e^4)
                     \wedge(e^6+\mathrm{i}e^5),
```
where $`a_L=R_1^2,b_L=R_2^2,c_L=R_3^2>0`$.

<div class="proposition">

**Proposition 6** (Correct status of the Lens–Nil construction). *The printed Lens–Nil pair is not balanced or positive Hermitian. The almost-complex structure defined by $`\Omega_{\rm old}`$ is non-integrable. Thus this pair is neither the claimed compatible $`SU(3)`$ structure nor a Hull–Strominger solution.*

</div>

<div class="proof">

*Proof.* The structure equations give
``` math
\mathrm{d}(\omega_{\rm old}^2)
   =2b_Lc_L e^{12456}-2a_Lb_L e^{12345}\neq0.
```
The two independent five-forms cannot cancel when $`R_2=R_3`$. Moreover,
``` math
\omega_{\rm old}\wedge\Omega_{\rm old}
 =(c_L-b_L)(e^{13456}+\mathrm{i}e^{23456}).
```
The algebraic wedge condition does hold when $`b_L=c_L`$, but the associated bilinear form is not positive: if $`E_j`$ denotes the dual frame, then $`I E_3=E_4`$ and $`\omega_{\rm old}(E_3,I E_3)=0`$. Thus this condition cannot supply a positive Hermitian metric. For $`\theta^2=e^3+\mathrm{i}e^4`$, $`\theta^3=e^6+\mathrm{i}e^5`$,
``` math
(\mathrm{d}\theta^3)^{0,2}=-\tfrac14\bar\theta^2\wedge\bar\theta^3\neq0.
```
This is the direct Dolbeault obstruction. ◻

</div>

This conclusion does not say that Lens or Nil geometry is useless in MTT. It can remain an auxiliary spectral, transport, or rank-filter model. What must be retired is the inference from that auxiliary role to a literal physical Hull–Strominger compactification. The literal $`L(3,1)\times\mathrm{Nil}_3`$ model is also not the selected $`q=79`$ Fu–Yau candidate; distinct topology cannot be erased by assigning the same interpretive labels.

# Baseline q79 evidence and its exact scope

The failure of the old Iwasawa bundle does not return the broader MTT program to zero. It changes which results may be composed.

## Available ingredients

The current research ledger contains the following separate results:

1.  an exact finite arithmetic selection of the $`q=79`$ branch;

2.  smooth non-pullback rank-three topological candidates with $`\int c_3=\pm6`$, giving index $`\pm3`$ at the topological tier;

3.  an exact finite rank-two Cech witness with 81 transition entries and 729 triple-overlap checks;

4.  a certified finite HYM approximation with residual $`8.208\times10^{-13}`$, coercivity lower bound $`26.0187`$, and residual-to-gap indicator $`3.155\times10^{-14}`$;

5.  a Wiener-algebra contraction certificate for that selected rank-two problem, with contraction constant $`Z=0.38508<1`$ and verified ball bound $`Y+Zr=0.00932703<0.01`$, yielding existence and local uniqueness in the declared neighborhood.

The machine-readable packets and verifiers are curated in the MTT Results Reproduction repository . The topological rank-three/index statement is also discussed separately in Ref. .

These are meaningful results, but their ranks and domains matter. The rank-two Cech/HYM witness is not the missing rank-three visible bundle. The smooth rank-three $`c_3=\pm6`$ candidate is not yet a holomorphic stable bundle with an HYM connection. Neither result by itself supplies a common visible–hidden pair, the differential Bianchi representative, or a worldsheet theory.

## Geometry imports and their physical input boundary

Two structural imports from *Cohesive Closure Repair and Its Hodge, Kernel, and Projection Shadows*, subsections on global support and the rank-zero large-gauge kernel, sharpen the comparison. First, the selected real K3 certificate gives an injective immersion $`b_{K3}:\mathbb R^2\to\mathbb T^{20}`$ with dense nonclosed image . Rank zero refers to the lattice of large-gauge identifications, not to the dimension of the source, the repair kernel, or a parameter-free physical theory. Numerical periods are unnecessary for that kernel decision, but the result does not supply kinetic normalization or the unrelated eta9 affine lift.

Second, Fitting ideals of the twisted Hartshorne–Serre benchmark descend as ordinary ideal sheaves: local line twists multiply minor generators by units without changing their ideals . Its determinant divisor has class $`3H+3D_0`$, not the physical eta9 class $`9H+3D_0`$. Generic corank three does not produce a spectral line. Support descent neither trivializes the gerbe nor executes literal connection overlaps. The older packet’s open hidden-HYM labels are superseded by the retained hidden existence theorem discussed below; the common physical pair remains a separate obligation.

The operator interface is owned by *Modal Triplet Theory: From MTT to Quantum Mechanics*, “From a geometric source to a retained operator.” For a supplied unitary connection, projective naturality preserves its curvature, differential and Hessian on the transported metric and domain . A smooth finite-matrix projector over the base is not a finite Fourier truncation. The lane flag acts on a separate factor, not inside an irreducible stable HYM gauge bundle. Its explicit Cech compiler uses the supplied transitions and metric to construct $`p=UU^*`$ and the correction
``` math
A_0=U^*dU,\qquad \Gamma=U(A-A_0)U^*,\qquad D_p=p\,d+\Gamma
```
so that the compiled connection, rather than the bare Grassmann connection, is the supplied one . The hidden central twist cancels in its rank-80 adjoint, giving the ordinary rank-102 deformation complex, not an ordinary hidden fundamental or a 27-mode continuum theorem. The intrinsic finite subspace must also be transported. Exact restriction requires $`(1-P)HP=0`$; otherwise the complementary resolvent contributes the Feshbach term. These are exact implications after inputs are supplied, not physical endpoint selection or a new fit. Thus the finite arithmetic, topological and compiler results can coexist with an unfinished common visible/hidden connection and Bianchi calculation.

## Why the Fu–Yau direction is different

Fu–Yau geometry belongs to an established class of complex non-Kähler heterotic constructions: torus bundles over a K3-type base can support balanced metrics and solutions of the anomaly equation under explicit topological and analytic hypotheses . This makes it a mathematically appropriate target for the selected MTT branch. It does not make every $`q=79`$ topological carrier a Fu–Yau solution automatically.

The current branch must still produce the following objects on one and the same complex threefold $`X_{79}`$:

<div class="center">

| Gate | Required object | Current state |
|:---|:---|:---|
| G1 | Global complex $`X_{79}`$, holomorphic volume form, balanced Fu–Yau metric | candidate/partial |
| V1 | Physical rank-three visible holomorphic bundle with $`\int c_3=\pm6`$ | open |
| V2 | Projective rank-nine hidden carrier on its declared q79 orbit | constructed; pair open |
| H1 | Visible, hidden, and tangent instantons in one metric chamber | hidden existence; pair open |
| A1 | Differential Green–Schwarz identity with fixed traces and connections | open |
| Q1 | Global gerbe/flux quantization and patching | open |
| Y1 | Matter cohomology, normalized overlaps, and physical Yukawa map | open |
| W1 | Exact heterotic worldsheet and modular/factorization data | open downstream |

</div>

## Hidden existence is not a missing theorem

The later unified-source construction supplies a locally free, holomorphic projective rank-nine hidden object. Its balanced qutrit orbit consists of three rank-three factors; the corrected determinant and relative polystability are part of that construction. This is not the earlier rank-two numerical witness and it should not be relabelled as an unconstructed hidden carrier.

The subsequent hidden HYM theorem is existential. For the fixed compact Gauduchon reference geometry, a finite common upper bound $`M`$ for the factor slopes exists. The direct stable-factor argument gives
``` math
\deg_t(G)\leq 2M-\frac{2}{3}(t-1)
```
for the relevant proper subobjects. Consequently $`t>1+3M`$ makes the three factors stable and the rank-nine orbit polystable; twisted Kobayashi–Hitchin then supplies a qutrit-equivariant projective HYM connection. The calculation has not emitted a numerical $`M`$, a selected $`t`$, or executable connection coefficients. Those are reproduction and source-selection tasks, not reasons to reopen the existence conclusion.

These are imported results, whose original statements and proofs remain in the frozen [balanced holomorphic projective-carrier record](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/unified_source_balanced_holomorphic_p39/artifact.json) and [existential hidden HYM record](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/unified_source_hidden_projective_hym/artifact.json). The latter explicitly leaves the same-source visible $`V_3`$, a numerical common visible–hidden chamber, and pointwise Bianchi cancellation open. Thus it advances rows V2 and H1 without closing the full Hull–Strominger assembly contract or determining physical Yukawa values.

## September update: local observability and the global obstruction

The baseline above is not an exhaustive inventory of the later q79 research. There is now a full selected $`164\times164`$ local Gauss–Manin coefficient source with a certified correlated lift on $`0\leq u\leq2^{-96}`$. Separately, the completed same-source affine Deligne test proves $`\beta_C(B89)\neq0`$. Thus B89 is rejected from the zero locus; neither the small local interval nor that rejection determines the global answer for every other cover. These results narrow an actual construction problem without changing the ranks or carriers of the baseline HYM theorems.

One correction is particularly important for subsequent searches. The non-torsion calculation at an initial Picard point on one genus-82 fiber does not compute the full global BHT obstruction. CBF T69 retracts the attempted global exclusion of ranks $`1`$ through $`1449`$. The fixed-fiber calculation survives, while the global rank-one and rank-two alternatives remain undecided. The valid implication that an actual rank-$`r`$ twisted spectral object requires $`r\beta_C=0`$ must be applied to that global class, not to a substitute evaluated at one fiber.

The newer response certificates explain why comparing several fibers is useful. CBF T70 finds rank $`70`$ for one coefficient evaluation of a $`122`$-dimensional projective tangent space, leaving a $`52`$-dimensional kernel. CBF T71–T72 instead recover rank $`122`$ from three evaluations. T72 proves the characteristic-zero statement at the three physical midpoints and preserves the coefficient rank on independent boxes $`|s_i-1/2|\leq2^{-32}`$, with certified Neumann defect below $`0.199`$.

CBF T73 supplies the canonical-dual response at those midpoints. K3 adjunction identifies the quotient $`H^0(\mathcal O(9H))/\langle F\rangle`$ with an $`82`$-dimensional canonical space. The three bilinear blocks are invertible and have total rank $`246`$; postcomposition preserves the coefficient rank $`122`$. This last bilinear invertibility is a midpoint result, not yet a certificate over the whole three-panel boxes. In particular, none of these coefficient ranks is silently identified with the derivative of the nonlinear global Picard/BHT restriction map.

All statements in this update are imported from the frozen [curated result manifest at commit f141a20e](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/result_manifest.json), including the records [CBF T69 (corrected global-rank scope)](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_eta9_framed_member_spectral_rank_exclusion/artifact.json), [CBF T72 (three-evaluation frame)](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_eta9_physical_midpoint_three_evaluation_frame/artifact.json), and [CBF T73 (canonical-dual response)](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_eta9_physical_canonical_dual_response_observability/artifact.json). The certificates and their original proofs remain the theorem owners. The next bridge is to certify the finite-trace bilinear over all three panels, complete global transport and the integral readout, and evaluate the actual global obstruction. The common HYM/Hull–Strominger endpoint and its physical overlaps still require the remaining rows below.

# The selected source and the integral comparison

The source sequence is best read as a construction with several different outputs. Arithmetic fixes a branch. A smooth spectral surface carries an analytic twist. Integral topology identifies the lattice on which its normal function lives. Residue calculations provide coordinates and local transport. The final period-class test, followed by a common HYM solution, is a further step. These are imported constructions, not new existence proofs in this paper; the frozen bibliography identifies their owners.

## What the number 79 selects

The exact A11 theorem assumes the retained carrier $`K_{64}\simeq\mathbb{C}[\mathbb{Z}/64]`$, its primitive shift $`S`$, block-circulant operators in $`\mathbb{C}[S]`$, exact commutation with the coherent projector, and the selected nil-survivor kernel. The primitive lag $`16\mapsto15`$ gives $`q_{64}=15`$; the separately fixed Mukai charge sector gives $`q_7=2`$. Hence
``` math
q\equiv15\pmod{64},\qquad q\equiv2\pmod7
 \quad\Longrightarrow\quad q\equiv79\pmod{448}.
```
Exact block commutation makes the off-block Schur correction zero in this regime. These assumptions matter: the conclusion is not an extraction theorem for every mixed continuum Hessian. Nor is a Mukai charge-sector identity already a single locally free visible HYM bundle. The companion audit checks the small CRT and primitive-lag arithmetic and the presence of specified source statements; its text-presence gates do not independently prove those statements. The established exact branch is retained without reopening its finite physics conclusions .

## Theta incidence and two different twists

On $`J=S\times E^*`$, with $`S`$ the selected K3 surface and $`H^2=2`$, the physical eta9 linear system is
``` math
\mathcal L_{\eta9}=\mathcal{O}_S(9H)\boxtimes\mathcal{O}_{E^*}(3[0]),
 \qquad h^0(\mathcal L_{\eta9})=83\cdot3=249.
```
Its projectivization has dimension 248. This is not the auxiliary $`3H+3D_0`$ pencil: changing 9 to 3 changes the geometry and the relevant cohomology. In UST.G3AB the selected theta matrices obey $`XZ=\zeta_3ZX`$. Values transform by $`U_g`$, coefficients by $`U_g^{-T}`$, so their contraction is invariant. The inverse multipliers cancel in the universal incidence equation. The rank-three coefficient minor and projective faithfulness give the selected nine-member smooth orbit .

This cancellation is finite equivariant descent, not analytic untwisting. The theta multiplier in $`H^2(E[3],U(1))`$ and the BHT universal-kernel obstruction in $`H^2(J,\mathcal{O}_J^*)`$ occupy different slots. Here BHT denotes the relative twisted Fourier–Mukai construction used by the source, and $`\beta_C`$ denotes the normalized analytic obstruction on a spectral member $`C`$. A smooth orbit and an honest incidence equation do not evaluate $`\beta_C`$, choose its zero locus, or produce a nonflat common visible–hidden connection. This is why the hidden existence result above can coexist with an open visible endpoint.

## A pairing-one class is not yet its transported coordinates

The Gate-1 campaign closes all 30 original-Jacobian groups and their 225 support columns. They provide polynomial identities with which to reduce the selected residue source, not an independently selected physical embedding. The older execution frontier begins with incomplete counts but continues through substantive filling and surgery results. Its remaining-Gate-1 instruction is superseded by the completed campaign; its mathematical distinctions must not be discarded with that instruction. In particular, an apparent chart pole need not be a critical value of the geometric pencil, and homological boundary cancellation is not itself a chain-level ordered-root lift .

The later gamma promotion fixes the orientation of $`h_Z=\delta\otimes u_A`$ and $`z_Z=\gamma\otimes u_B`$, where $`u_A,u_B`$ are the selected elliptic cycles. The four-thimble representative $`-T_{17}+T_{26}-T_{27}+T_{28}`$ has pairing one. The ordinary divisor-avoidance argument preserves its integral homology class. The frontier also explains how equal-label opposite-sign crossings can be removed by tubes, and why admitted filling repairs have the same twisted homology and closed-cocycle pairings. This removes an artificial choice of fourteen local physical parameters. It does not supply the missing selected transport or the integral residue coordinates. Existence of a representative, a particular executed representative, and its period image are three different assertions .

## Integral gluing cannot be replaced by rational rank

For a primitive nondegenerate ambient sublattice $`A`$ in a unimodular surface lattice $`L`$, put $`V=A^\perp`$. The integral quotient is $`L/A\simeq V^\vee`$, not automatically $`V`$. The pairing embeds $`V`$ in its dual with discriminant quotient $`D(V)=V^\vee/V`$. In the physical eta9 surface the ranks of $`L,A,V`$ are respectively $`1532,23,1509`$, and
``` math
D(V)\simeq(\mathbb{Z}/3)^{22}\oplus\mathbb{Z}/54.
```
Rationalizing erases precisely this finite gluing information. Thus a rank-1510 affine extension retains its rank when the integral coefficient module is corrected, but identifying its integral translation lattice requires an explicit marking; a rank match cannot identify the physical normal function with a finite compiler .

H4-T30 gives the integral comparison test. For an integrally generating presentation it retains the selected primitive, infinite-order topological affine extension, not merely an unconstructed candidate. When the physical coefficient module is the ambient quotient, use $`V^\vee`$ for that module; applying a theorem stated for $`V`$ requires the corresponding integral comparison. For the abstract meridian map $`E:\mathbb{Z}^N\to V`$, with $`K=\ker E`$, H4-T31 separates the pairing-map obstruction as
``` math
0\longrightarrow D(V)\longrightarrow\operatorname{coker}(E^*Q)
   \longrightarrow K^*\longrightarrow0.
```
Zero relation defects remove the free obstruction; zero discriminant residues remove the finite obstruction. Both are needed. For example, in negative $`A_2`$, the roots $`e_1,e_2,e_1+e_2`$ have relation $`(1,1,-1)`$. The translation difference $`(1,0,1)`$ kills this relation but requires the fractional gauge $`(-2/3,-1/3)`$; it is not an integral coboundary. This small example explains the need for the integral test without reproducing the owning proof.

H4-T32 computes the discriminant class from an integral lift in $`L`$: pair with the 23 ambient generators, apply the fixed left Smith transform, and reduce by the displayed invariant factors. It also supplies a finite generation criterion: after one nonzero maximal minor $`\Delta`$ is known, full rank modulo every prime dividing $`\Delta`$ certifies integral surjectivity. The physical pairing vector and its residues are not supplied by this recipe. Filtered Deligne comparison additionally needs compatible connection, transversality and normalization data. Nor does a degree-two gerbe obstruction automatically belong to an ordinary Neron model: such a comparison requires its own admissibility and integral specialization map.

H4-T33 allows a smaller first decision than constructing the entire marking. If $`h`$ is a primitive integer pairing and $`R`$ an additive readout modulo the periods of $`\ker h`$, then $`[R(z)]=h(z)\beta_C`$. A pairing-four root with nonzero quotient readout proves $`\beta_C\neq0`$; zero proves only $`4\beta_C=0`$. An odd accessible pairing, for example 7, yields a pairing-one combination $`2\cdot4-7=1`$. This is a decision strategy, not an emitted physical readout. Equality in the period quotient also does not authorize applying an arbitrary normal operator: that operator must preserve the period subgroup .

# From a root cycle to a residue source

## Why the failed scalar representation is not a failed cycle

H4-T34 factors the selected root curve $`R^-\times[1:-1:0]`$ using $`Q_2,w+G_3,t_0+t_1,t_2`$: a conic, a selected double-cover sheet, and two equations fixing the elliptic projective point. Here the $`t_i`$ are its homogeneous coordinates and the degree triples record Cox characters. The resulting Cayley determinant numerator has degree $`(10,2,1)`$, but the defining degrees are split nef, not ample. Therefore the ample-cycle closed formula cannot be imported without a comparison. Literal division by $`xt_0`$ fails. H4-T35 instead solves the equation modulo the Jacobian ideal in a specified 927-coordinate gauge; a nonzero good-reduction minor proves existence over $`\mathbb Q(\gamma)`$, not yet a geometric cycle-class identification .

H4-T36 retains the regular embedding and the three-chart cover, and H4-T37 emits all three chart numerators. The next test matters: H4-T38A finds coefficient rank 85 and augmented rank 86 in the common-scalar correction system over $`\mathbb F_{11}`$. Its stacked multiplier has rank 1012, not 1013. Thus no single ordinary-Jacobian scalar realizes these three numerators at that place. Neither the root curve nor its Gysin class has been disproved. The rank-16 Koszul matrix factorization of H4-T39, $`D^2=\Phi I`$, retains the full degree-eight determinant form with 45 components before scalar projection. Its line-valued curvature is not a nilpotent differential that can be treated as an ordinary complex.

H4-T40 checks a different possible shortcut: the full ten-derivative character is a nonzero polynomial but has zero ordinary $`H^{0,2}`$ Jacobian image at the locked finite place. That zero does not erase the degree-eight localized source. Indeed H4-T41 proves that the fractions $`N_x/(xt_0),N_y/(yt_0),N_z/(zt_0)`$ agree after localization: the cross-differences first vanish at denominator power four. All tested relative finite-field rescalings still fail the original global-scalar demand. Localization removes denominator torsion; it does not retroactively solve the unsaturated equations. The affine nonzero witness lies outside the toric semistable locus, so semistable descent remains a separate step.

## Descent, orientation and the surviving edge class

H4-T42 types the Koszul construction as two rank-eight Cox-equivariant bundles with a potential valued in $`\mathcal{O}(0,0,1)`$. H4-T43 enumerates the semistable strata and contracts the two nonidentity $`\mu_3`$ inertia sectors by an explicit $`w^{-1}`$ homotopy; this removes those sectors, not the identity-sector character. On its support, H4-T44 supplies 27 unimodular charts, integral monomial frames, their transition cocycles, and the logarithmic-differential Atiyah input. These are actual descent data rather than a guess from matching dimensions .

To apply a function-valued character formula, H4-T45A passes to the potential-trivializing torsor. The potential becomes a function on the eight-dimensional quotient, but its residual $`R`$-charge must be kept. H4-T45B contracts by that Euler field and the Gale top form, forcing the $`(9,1,1)`$ character of the desired $`H^{1,1}`$ residue. It also fixes the chart signs $`(+,-,+)`$. H4-T45C shows that oriented and unsigned fractions can both agree on affine overlaps because the sign-sensitive restrictions there vanish. Agreement on those overlaps cannot select the orientation; the Gale form does.

H4-T45D identifies the saturated, oriented finite-fiber section with the 1013-coordinate $`H^{1,1}`$ vector and its compulsory factor $`1/6`$. H4-T45E then uses the nonnegative Cech filtration of the total character: its zero-Cech component fixes the edge image. Positive-Cech terms complete the cocycle but do not change that edge image. This does not assert that the total cocycle has been explicitly expanded. H4-T45F defines the nonzero characteristic-zero class compactly as $`[N_{\rm root}/6]`$. The failure to reconstruct large coordinates in one frozen gauge is not nonexistence of this exact quotient class.

## The action is normalized before it is transported

H4-T46 identifies the root, the moving graph and the four-normal source, including the sign $`R^- - H=-\delta`$, and supplies the fixed elliptic period $`\Omega_B`$. The start source is $`\Omega_B[N_{\rm root}/6]`$, not a freely rescaled state. H4-T47 explains when the connection acts on this quotient: it must preserve the relation subbundle. A new quotient frame then has the usual inhomogeneous gauge law, including its derivative. A frozen quotient matrix alone is not the complete Gauss–Manin connection .

H4-T48 executes the full $`H^{0,2}`$-to-$`H^{1,1}`$-to-$`H^{2,0}`$ recursive action at six roots of the split prime 21817, retaining the original-Jacobian preimages for the successive $`1/4`$ and $`1/3`$ divergences. H4-T49 repeats the action at sixteen split primes and proves the $`H^{2,0}`$ endpoint determinant over $`\mathbb Q(\gamma)`$. The full action is not thereby reconstructed over that field. Crucially, H4-T50 corrects the normalization of the stored T47–T49 arrays: they used the raw numerator. Every source, preimage, right-hand side and output must be divided by six before it represents the canonical class. Linearity preserves the zero-residual identities. Over $`\mathbb F_{11}`$ this means multiplying by 2. The raw arrays remain valid unnormalized witnesses, not canonical physical source values.

## What computational reduction and precision establish

The characteristic-zero reduction of the earlier Gate-2 chart separates the exact $`H^{2,0}`$ inverse, $`H^{1,1}`$ kernels of dimensions 934 and 398, and an $`H^{0,2}`$ Woodbury kernel of dimension 15158. Integral anchors with nonzero determinant modulo 11 justify the exact reduction. They do not select one of the six Archimedean embeddings or provide interval inverse values .

For the canonical selected source, H4-T51 constructs the 6022-coordinate Woodbury adapter $`z=S^{-1}Wx`$, with 34 balanced blocks. H4-T52 evaluates $`Pz`$ by one base solve rather than materializing $`P=A_0^{-1}U`$; the endpoint and reduced equations replay at all 96 selected roots. Their reconstruction tests produce no stable nonzero coordinate in the tested window. Those conclusions concern a finite adapter and a bounded reconstruction attempt, not the nonexistence of a characteristic-zero solution .

H4-T53 provides an exact sparse coefficient compiler and high-precision midpoint refinement at all independent embeddings. Its binary64 factor is only a preconditioner; a small correction computed at Arb midpoints is still not a directed enclosure. H4-T54 and H4-T55 instead certify exact split $`p`$-adic actions, first through $`21817^{512}`$, then through $`21817^{2048}`$, with specified rational-reconstruction exclusion windows. T55’s 7746-dimensional core is minimal among fourteen tested admissible gauges, not globally optimal among every gauge. None of these precision or height statements is an Archimedean path theorem. The later local source tube below is a genuine additional result, so the earlier “source enclosure open” wording is not current in that local scope.

# Completed local tests and the global endpoint

## A complete three-cycle calculation can be non-detecting

The full-coverage packet retains the earlier seven-eighths base as provenance. Its later frontier merge adds the three missing faces, using 81 source records and exact prefix-free dyadic partitions. The readiness packet binds three complete eight-face covers to one mathematical source. The endpoint projection then supplies ten real component intervals for each of 4251 transported cells. Coverage, projection and intersection are separate assertions: projection alone proves no pairing .

The common-fiber separation packet exhaustively separates the cross-cycle box unions. Thus the off-diagonal intersections vanish. Together with the retained self-intersections, the B96 Gram matrix is $`-2I_3`$, with determinant $`-8`$. The three cycles are independent, and their affine coefficients are rational coboundaries on this subsystem. The completed calculation is therefore non-detecting at the rational relation-defect tier. It neither proves integral coboundary membership nor trivializes the full global affine class. This source should not be rerun as though its cover were incomplete; a detecting subsystem must contain different information. In the converse direction, a singular Gram matrix alone would not prove an actual relation in the ambient lattice.

## A positive-width source with correlated errors

The positive-width packet reconstructs the complete $`164\times164`$ algebraic connection on the normalized marked interval $`0\leq u\leq2^{-96}`$, with a source inverse defect less than $`0.000149`$ and local lift contraction less than $`0.006231`$. The coordinate $`u`$ is dimensionless and is not physical time. This is a same-source correlated family, not a statement about arbitrary independent choices of every interval entry .

For clarity, let $`\mathcal J`$ be the local real-structure matrix, $`S=\mathcal J_{21}^{-1}`$, and $`R=-\mathcal J_{11}S`$, with subscript 0 denoting the initial value. The correlated-increment certificate uses
``` math
\Delta S=-S_0\Delta\mathcal J_{21}S,\qquad
 \Delta R=-(\Delta\mathcal J_{11}+R_0\Delta\mathcal J_{21})S.
```
Keeping the common initial data in these identities sharply improves the increment bound without a new source solve. It does not improve the precision of $`R_0`$ itself. The consolidation record indexes these two certificates; it is not an additional numerical acceptance theorem. Useful-width continuation, the normalized-to-global frame with its gauge derivative, ordered-path completion and integral readout remain separate.

## A local scalar does not select a compactification

CBF T65 is a useful warning about precision. Its three frozen-binary row gauges refine to tiny residuals but disagree on the proposed scale. The test rejects promotion from those binary coefficients, not the characteristic-zero geometric functional. T67 subsequently uses a certified characteristic-zero inverse and correlated adjoint readouts. For $`A^Tz=g`$, the error in a scalar can be bounded through the adjoint residual and the common source rather than by treating every solved coordinate independently. The certified denominator excludes zero, so the stated $`585/(2D)`$ scale and its derivative are defined at the declared edge-2 midpoint .

This is a method-chart scalar on the already declared B89 source, not an observed physical coupling or a replacement for $`\beta_C`$. The same-source B89 affine replay has a mod-two cokernel detector annihilating $`M-I`$ and pairing one with the translation. It therefore rejects B89 from the zero locus, without proving that the integral class has exact order two .

CBF T68 explains the rank consequence. Taking determinants in $`g_{ij}g_{jk}g_{ki}=\alpha_{ijk}I_r`$ gives the necessary condition $`r[\alpha]=0`$; for a twisted line it is the trivialization condition itself. In the declared degree-three transform, spectral rank $`r`$ would give inverse rank $`3r`$, subject to the transform’s local-freeness and cohomological hypotheses. Raising spectral rank to two therefore does not preserve the intended rank-three visible bundle. B89’s genuine mod-two detector excludes odd ranks but does not construct an even-rank object. A local component sieve on another candidate is usable only after its map from the actual global twist has been established; an ordinary Neron-model interpretation cannot be assumed. In particular, the T69 fixed-fiber calculation still does not decide the framed member’s global rank-one or rank-two alternatives.

## What the three coefficient evaluations resolve

The T70 and T71 residue calculations explain the later T72–T73 response result already summarized above. The graph-incidence kernel has affine dimension 123 and contains the radial member, leaving projective tangent dimension 122. One selected fiber sees only 70 directions, with kernel 52 and cokernel 12. The earlier principal 33-dimensional slice sees only 11. In T71 every tested pair sees 111 directions; a dependent triple adds none, while a deterministic independent triple reaches 122. Thus “three evaluations” means independent coefficient rows, not any three observations .

T72 supplies the characteristic-zero midpoint minor and its positive-width coefficient-rank certificate. T73 uses K3 adjunction and the three invertible midpoint canonical bilinears to postcompose this map without changing its kernel. Its later source also supplies all three local branch carriers, refining T72’s earlier carrier inventory. None of that extends the canonical-bilinear nondegeneracy automatically over the whole product of panels. Nor does coefficient injectivity compute the nonlinear divisor-to-Picard derivative or the global BHT integral. It supplies an informative local readout, not a physical-source selector.

# A typed completion theorem

The useful way forward is to make completion compositional without allowing objects from different carriers or ranks to be silently merged.

<div id="thm:contract" class="theorem">

**Theorem 7** (Hull–Strominger assembly contract). *Fix one compact complex threefold $`X`$, one Hermitian metric $`\omega`$, one holomorphic volume form $`\Omega`$, one dilaton $`\Phi`$, holomorphic bundles $`V_{\mathrm{vis}},V_{\mathrm{hid}}`$, unitary connections $`A_{\mathrm{vis}},A_{\mathrm{hid}}`$, and a specified unitary tangent connection $`\nabla`$. Suppose:*

1.  *$`\Omega`$ is nowhere vanishing and $`\mathrm{d}(\|\Omega\|_\omega\omega^2)=0`$;*

2.  *both gauge curvatures have type $`(1,1)`$ and are primitive;*

3.  *$`R_\nabla`$ obeys the tangent-instanton condition required by the chosen first-order convention;*

4.  *with $`H=\mathrm{i}(\bar\partial-\partial)\omega`$, the differential identity
    ``` math
    \mathrm{d}H=\frac{\alpha'}4\left(
    \mathrm{tr}R_\nabla^2-\mathrm{tr}F_{\mathrm{vis}}^2-\mathrm{tr}F_{\mathrm{hid}}^2\right)
    ```
    holds with one fixed trace normalization;*

5.  *the resulting $`H`$ and Chern–Simons data define the required global differential-cohomological flux class.*

*Then these data form a first-order heterotic Hull–Strominger background in the declared convention.*

</div>

<div class="proof">

*Proof.* Each hypothesis is exactly one typed equation or global patching requirement from Section <a href="#sec:obligations" data-reference-type="ref" data-reference="sec:obligations">2</a>. Because every term is defined on the same carrier with fixed connections and traces, the equations can be assembled without changing representatives or importing a result from a different rank. The conclusion is therefore the conjunction of the verified rows. ◻

</div>

<div class="remark">

*Remark 8* (What the theorem does not add). Theorem <a href="#thm:contract" data-reference-type="ref" data-reference="thm:contract">7</a> is an assembly theorem, not an existence theorem. It prevents a common logical error: satisfying each row somewhere is not the same as satisfying all rows on one selected object. The open MTT task is to construct the tuple satisfying its hypotheses on $`X_{79}`$.

</div>

Three-family physics requires an additional layer. One must prove the relevant index on $`V_{\mathrm{vis}}`$, identify the massless cohomology groups, choose the physical embedding and normalization, and compute the overlap map. None of those conclusions is supplied merely by Theorem <a href="#thm:contract" data-reference-type="ref" data-reference="thm:contract">7</a>.

# Interpretation inside MTT

The MTT language of selection and admissibility remains useful if it is kept typed. It can organize a search over candidate complex manifolds, bundles, connections, and finite operators. It cannot convert a failed Maurer–Cartan equation into a holomorphic bundle or replace an analytic existence theorem.

The corrected relation among the recurring geometric labels is:
``` math
\text{local Circle--Lens--Nil filtration}
\;\not\equiv\;
L(3,1)\times\mathrm{Nil}_3
\;\not\equiv\;
X_{79}.
```
Circle, lens, and nil may label phase/holonomy, finite transport, and anchoring or shear sectors after projection. The shared circle is common line-bundle phase data counted once; it is not automatically a compact time coordinate. A connection-preserving intertwiner is required before the local filtration can be identified with vertical operators on the global $`q=79`$ geometry.

This distinction explains why the rank-two HYM theorem is valuable but not decisive for the physical compactification. It demonstrates that the selected analytic machinery can close a nontrivial HYM problem. It does not change the bundle rank, Chern class, or carrier on which that theorem was proved.

# Discussion

The main positive result is methodological as well as algebraic. The Iwasawa calculation supplies a clean example of how far local geometry can progress before the global bundle layer becomes decisive. The exact repair in Theorem <a href="#thm:repair" data-reference-type="ref" data-reference="thm:repair">4</a> is also informative: integrability can be restored without producing the desired physics. Gauge redundancy and simplicity are independent gates.

The negative conclusions are deliberately local to the constructions audited here:

- they do not rule out other invariant Iwasawa solutions with properly chosen instantons;

- they do not rule out generalized or nonsupersymmetric uses of a non-integrable Lens–Nil $`SU(3)`$ structure;

- they do not invalidate the exact $`q=79`$ finite theorem, the topological rank-three candidate, or the separate rank-two HYM theorem;

- they do prevent those separate results from being advertised as one completed physical compactification.

The most direct research target is now the physical visible bundle gate V1. A successful construction should begin with an actual holomorphic rank-three bundle on the selected Fu–Yau carrier, prove its stability in the same balanced chamber used by the geometry, compare the already established hidden connection in that common chamber, and solve the pointwise Bianchi row. Reusing the rank-two Wiener-contraction architecture is reasonable; reusing its conclusion without a rank-three operator is not.

# Reproducibility

The exact finite-dimensional statements behind Theorem <a href="#thm:repair" data-reference-type="ref" data-reference="thm:repair">4</a> are checked by the standard-library script `verify_bundle_audit.py` distributed with this paper. It verifies:

1.  the nonzero Maurer–Cartan residual of the printed matrix;

2.  the vanishing residual of the repaired matrix;

3.  the three $`SL(3,\mathbb{C})`$ conjugation identities as Laurent-polynomial identities;

4.  the two-dimensional commutant by exact rational row reduction.

The wider q79, Cech, finite-HYM, and Wiener-contraction artifacts are provided with provenance hashes and their own verifiers in Ref. . Numerical execution does not alter the scope boundaries stated in Section <a href="#sec:q79" data-reference-type="ref" data-reference="sec:q79">7</a>.

The accompanying `test_contextual_revision.py` performs bounded exact checks of the exterior-form signs, all three Maurer–Cartan components, CRT, the small integral-lattice example, factorial scaling, and the dyadic cover arithmetic. It also parses and hashes every assigned frozen artifact, including every endpoint-component interval. These checks do not rerun the large source calculations or turn packet Boolean fields into independent verification. The contextual review records that distinction and the source-specific qualifications.

# Revision note: Version 4

<div class="description">

Version 4 supersedes Version 3 and its claim of two explicit heterotic compactifications.

The earlier paper combined a correct local Iwasawa calculation with nonclosed Chern data, an unconstructed monad, a nonintegrable Dolbeault operator, an impossible Chern number on a trivial carrier, and a non-integrable Lens–Nil model.

This version proves the closed-form and Maurer–Cartan obstructions, constructs and diagnoses the unique minimal signed repair, withdraws the dependent Bianchi, generation, and Yukawa conclusions, and replaces the claimed solutions by the typed q79 Fu–Yau completion contract.

The verified Iwasawa complex and balanced structure, the corrected torsion and $`\mathrm{d}H`$, the auxiliary role of Lens and Nil filtrations, and Fu–Yau geometry as the strongest current q79 heterotic direction are retained.

The program still needs one common q79 rank-three visible–hidden Hull–Strominger tuple satisfying the holomorphic, HYM, differential Bianchi, flux, and matter-overlap gates of Theorem <a href="#thm:contract" data-reference-type="ref" data-reference="thm:contract">7</a>.

</div>

# Conclusion

The earlier paper did not construct the two claimed heterotic compactifications. What survives is a correct Iwasawa balanced-geometry calculation, an exact diagnosis of the failed bundle, and a sharper route forward. The selected $`q=79`$ program has nontrivial finite, topological, and rank-two analytic evidence, a projective rank-nine hidden existence theorem, and the source and local-response constructions described above. A physical Hull–Strominger compactification still requires one common tuple with a rank-three visible bundle and the compatible hidden connection, satisfying every gate in Theorem <a href="#thm:contract" data-reference-type="ref" data-reference="thm:contract">7</a>. That is the precise frontier.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The q79 arithmetic theorem and audit, literal finite rank-two Cech witness, and rank-two Wiener-contraction certificate are used directly at their declared finite, topological, or rank-two analytic tiers. They do not construct the missing physical rank-three visible-hidden bundle, differential Green-Schwarz representative, flux gerbe, or worldsheet theory. The paper’s SU3 repair obstruction is checked by its own exact local verifier and is not relabeled as a promoted q79 HYM endpoint.

The referenced rows are frozen to the curated results repository state identified below. Hashes are grouped in eight-character blocks for line breaking. This older baseline evidence block retains its own immutable snapshot; the additional contextual imports in Sections <a href="#sec:source-integral" data-reference-type="ref" data-reference="sec:source-integral">8</a>–<a href="#sec:local-global-import" data-reference-type="ref" data-reference="sec:local-global-import">10</a> are cited separately at frozen commit f141a20e. Neither snapshot’s status fields replace the current authority distinctions explained in the text.

> **Repository:** <https://github.com/PeterNero/mtt-results-repro>
> **Commit:** `31247ebb 5c22f3fb b5443024 365433c6 ee0bff4a`
> **Manifest:**
> **Manifest SHA-256:**
> `fb399689 60b00584 631dbf53 1a708e18`
> `ef928d6b 6d935119 c185d7f6 32b1e7cd`

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper’s local theorems; and an open row is evidence of an unresolved obligation, never of closure.

= by -
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

#### Rows used directly in this paper.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*derived exact*).

  Literal 81-entry, 729-cocycle finite Cech witness.

- (*derived exact*).

  Executable q=79 exact-branch audit.

- (*derived exact*).

  CRT q=79 theorem on the selected exact branch.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
