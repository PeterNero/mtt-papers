---
abstract: |
  Comparing coherent sectors across different geometries is not the same problem as proving that one projector is stable inside one Hilbert space. The models may have different domains, spectra, retained spaces, observables, clocks, and physical interpretations. A claim of “universality” is therefore meaningful only after those differences are transported into a common comparison record.

  This paper defines that record. Each model supplies a typed coherent-sector reduction certificate, a nonempty common spectral region, and an explicit unitary or quasi-unitary identification of its retained space with a reference space. The compressed resolvent is then transported to the reference space. We prove a local comparison theorem, a chainwise error-accumulation bound, and an observable-transfer estimate. We also separate projector stability, norm-resolvent robustness, domain or form convergence, finite-time dynamics, observable agreement, and physical equivalence.

  Two counterexamples mark the boundary of the result. A continuum of microscopically distinct operators can have the same retained resolvent and uniform gap, so local robustness does not make a landscape finite or select one vacuum. Conversely, identical reduced spectral data can be paired with different observable maps and therefore different predictions. The current Modal Triplet Theory applications to Calabi–Yau geometry, heterotic flux backgrounds, perturbative strings, M-theory, and quantum gravity are consequently recorded as conditional realization or compatibility programs, not as members of one proved global physical equivalence class. The result is a rigorous local comparison framework and a concrete completion contract for future cross-model claims.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 1db283114f7c49319421b69075c3069e4c782160fdfed5b0abf99ef7a1058fb4
paper_id: universality-and-robustness-of-the-coherent-sector-in-m-a64842b3
release_state: zenodo_released
released_version: v2
title: |
  Local Coherent-Sector Robustness Across Model Families:
  Transported Resolvents, Accumulated Error, and the Limits of Universality in MTT
zenodo_doi: 10.5281/zenodo.21710653
zenodo_record_id: 21710653
zenodo_url: "https://zenodo.org/records/21710653"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1.0, DOI [10.5281/zenodo.18260834](https://doi.org/10.5281/zenodo.18260834).

Version 1 defined a broad coherent universality class from generic gap, bounded-geometry, and projector language, then treated Calabi–Yau, heterotic, string, M-theory, and quantum-gravity constructions as members. Its projector theorem did not declare the operator family, contour, or perturbation norm. Its curvature and RG statements did not define an evolution or error topology. It also promoted local spectral control to full quantum robustness, physical equivalence, and landscape reduction.

This revision imports the domain-explicit Feshbach and projector theorem from the companion reduction paper rather than duplicating it. It builds the missing cross-model layer: explicit comparison spaces, transported compressed resolvents, accumulated errors, state and observable maps, and separate dynamical and physical-equivalence gates.

The useful intuition survives locally. Families of models can share a controlled effective sector when each model has a valid reduction certificate and the resulting bounded objects are close after a declared identification.

No current theorem places all viable compactifications, string limits, M-theory backgrounds, quantum-gravity constructions, or Standard Model realizations in one physical equivalence class. Nor does a local robustness certificate count, select, or empirically identify vacua.

</div>

# The corrected question

The original paper asked whether microscopic geometric changes leave one coherent sector physically unchanged. That sentence contains three different mathematical questions:

1.  Does a selected spectral subspace persist under a perturbation?

2.  Can effective operators from different models be compared after their retained spaces are identified?

3.  Does agreement of those effective operators imply agreement of states, observables, dynamics, and physical interpretation?

The first question belongs to spectral perturbation theory. The second requires a transported comparison framework, especially when Hilbert spaces or domains vary. The third requires additional physical maps. A proof of one is not a proof of the next.

## Why a common gap is not enough

Suppose two self-adjoint operators each have an isolated low spectral cluster. Even then:

- their low spaces need not come with a canonical identification;

- their operators may have different domains;

- operator-norm, graph-norm, form, strong-resolvent, and semigroup convergence are inequivalent hypotheses;

- their clocks and observable algebras may be different; and

- the same reduced spectrum can carry different physical labels.

The comparison object must therefore include more than a projector and a gap.

## What this paper does not claim

This paper does not prove that:

- one coherent projector exists across every Modal Triplet Theory encoding;

- all compactifications lie in one connected or controlled family;

- local spectral robustness gives uniform long-time dynamics;

- a finite or Galerkin comparison converges to a continuum theory;

- reduced operator agreement implies physical equivalence;

- an admissibility filter makes a candidate landscape finite; or

- one selected vacuum follows from the existence of a nonempty admissible set.

# The imported single-model reduction

The companion paper owns the single-model reduction theorem. Its essential distinction is worth stating before any cross-model comparison.

Let
``` math
\mathcal H_a=\mathcal H_{P,a}\oplus\mathcal H_{Q,a}
```
and let
``` math
T_a=
 \begin{pmatrix}
 A_a&B_a\\ C_a&D_a
 \end{pmatrix},
 \qquad
 \mathcal D(T_a)=\mathcal D(A_a)\oplus\mathcal D(D_a),
```
where $`A_a`$ and $`D_a`$ are self-adjoint, $`B_a`$ and $`C_a`$ are bounded, and $`C_a=B_a^*`$. For $`z\in\rho(D_a)`$, define
``` math
F_a(z)=A_a-z-B_a(D_a-z)^{-1}C_a.
```
If $`z\in\rho(T_a)`$ as well, then
``` math
R_a^P(z)
 :=
 P_a(T_a-z)^{-1}P_a\big|_{\mathcal H_{P,a}}
 =
 F_a(z)^{-1}.
```

The bounded correction is
``` math
\Sigma_a(z)=B_a(D_a-z)^{-1}C_a
```
and obeys
``` math
\|\Sigma_a(z)\|
 \leq
 \|B_a\|\,\|(D_a-z)^{-1}\|\,\|C_a\|.
```
Every factor is typed and every spectral parameter is declared.

<div class="remark">

*Remark 1* (Exact spectral projectors). If $`P_a`$ is the exact spectral projector of the same self-adjoint operator $`T_a`$, then it reduces $`T_a`$, so
``` math
P_aT_aQ_a=Q_aT_aP_a=0.
```
A nonzero eliminated-sector correction requires a projector selected from a reference operator, symmetry, Galerkin space, localization rule, or approximate criterion. Cross-model comparison must record which case is being used.

</div>

This paper begins only after each model has supplied such an individual certificate. It does not weaken or silently fill a missing single-model domain, resolvent, or source row.

# The transported comparison record

<div id="def:modelrecord" class="definition">

**Definition 2** (Controlled model record). A controlled model record indexed by $`a`$ is
``` math
\mathcal M_a=
\bigl(
\mathcal H_a,G_a,T_a,P_a,Q_a,
A_a,B_a,C_a,D_a,
\Omega,
\varepsilon_a,
U_a,
\mathcal S_a,\mathcal O_a,\iota_a,
\pi_a
\bigr),
```
with the following data:

1.  $`G_a`$ is the reference operator or rule selecting $`P_a`$;

2.  $`T_a`$ and its four blocks satisfy the domain assumptions in <a href="#sec:imported" data-reference-type="ref+label" data-reference="sec:imported">2</a>;

3.  $`\Omega`$ is a nonempty compact set contained in
    ``` math
    \rho(T_a)\cap\rho(D_a);
    ```

4.  the compressed resolvent $`R_a^P(z)`$ is uniformly bounded on $`\Omega`$;

5.  $`U_a:\mathcal H_{P,a}\to\mathcal K`$ is a declared unitary identification with one reference Hilbert space $`\mathcal K`$;

6.  $`\varepsilon_a`$ is the individual reduction or numerical error;

7.  $`\mathcal S_a`$, $`\mathcal O_a`$, and $`\iota_a`$ record states, observables, and physical interpretation maps; and

8.  $`\pi_a`$ records provenance, theorem status, and source hashes.

</div>

The common $`\Omega`$ is part of the comparison. Two reductions evaluated at unrelated spectral parameters or on disjoint resolvent regions have not yet been compared.

<div class="definition">

**Definition 3** (Transported compressed resolvent). For a controlled model record, define
``` math
\widehat R_a(z)
 =
 U_a R_a^P(z)U_a^*
 \in\mathcal B(\mathcal K),
 \qquad z\in\Omega.
```
For two records define
``` math
d_\Omega(a,b)
 =
 \sup_{z\in\Omega}
 \|\widehat R_a(z)-\widehat R_b(z)\|.
```

</div>

Because the identifications $`U_a`$ are part of the records, this functional compares bounded operators on one fixed space. Changing $`U_a`$ changes the question and must be reported as a different comparison convention.

# Local comparison and accumulated error

<div id="thm:transported" class="theorem">

**Theorem 4** (Transported local comparison). *Let $`a,b`$ be controlled model records on a common compact region $`\Omega`$. Then $`d_\Omega(a,b)<\infty`$. It is symmetric and obeys the triangle inequality. More generally, suppose
``` math
E_a,E_b:\Omega\to\mathcal B(\mathcal K)
```
are declared approximate reduced-resolvent fields satisfying
``` math
\sup_{z\in\Omega}\|\widehat R_a(z)-E_a(z)\|
 \leq\varepsilon_a,
 \qquad
 \sup_{z\in\Omega}\|\widehat R_b(z)-E_b(z)\|
 \leq\varepsilon_b.
```
Then
``` math
d_\Omega(a,b)
 \leq
 \varepsilon_a
 +
 \sup_{z\in\Omega}\|E_a(z)-E_b(z)\|
 +
 \varepsilon_b.
```*

</div>

<div class="proof">

*Proof.* Uniform boundedness follows from compactness of $`\Omega`$, continuity of each resolvent, and the unitary invariance of the operator norm. Symmetry is immediate. For any third record $`c`$,
``` math
\begin{aligned}
\|\widehat R_a(z)-\widehat R_c(z)\|
&\leq
\|\widehat R_a(z)-\widehat R_b(z)\|\\
&\quad+
\|\widehat R_b(z)-\widehat R_c(z)\|.
\end{aligned}
```
Taking the supremum gives the triangle inequality. Inserting and subtracting $`E_a(z)`$ and $`E_b(z)`$ gives the final estimate. ◻

</div>

<div id="cor:chain" class="corollary">

**Corollary 5** (Error accumulation along a comparison chain). *For controlled records $`a_0,\ldots,a_N`$ on the same $`\Omega`$,
``` math
d_\Omega(a_0,a_N)
 \leq
 \sum_{j=0}^{N-1}d_\Omega(a_j,a_{j+1}).
```
Consequently, a chain of $`N`$ comparisons each certified only to $`\varepsilon`$ gives at best an $`N\varepsilon`$ endpoint bound unless a stronger cancellation theorem is supplied.*

</div>

<div class="proof">

*Proof.* Iterate the triangle inequality in <a href="#thm:transported" data-reference-type="ref+label" data-reference="thm:transported">4</a>. ◻

</div>

This simple bound matters in a large corpus. A sequence
``` math
\text{upper geometry}
 \longrightarrow
 \text{finite operator}
 \longrightarrow
 \text{four-dimensional action}
 \longrightarrow
 \text{observable}
```
cannot reuse the same tolerance at every arrow and report it once at the end. Each arrow contributes its own error and provenance row.

## Local class, not global equivalence

<div class="definition">

**Definition 6** (Local coherent comparison class). Fix a reference record $`a_0`$, a common region $`\Omega`$, fixed identification conventions, and a tolerance $`\varepsilon>0`$. The local comparison class is
``` math
\mathfrak U_\varepsilon(a_0;\Omega)
 =
 \{a:\ d_\Omega(a,a_0)\leq\varepsilon\}.
```

</div>

This is a useful neighborhood, not a theorem that all viable models lie in it. Finite-tolerance membership is also not automatically transitive at the same tolerance: two members can be as far as $`2\varepsilon`$ apart.

# Projector stability is one separate layer

The retained spaces themselves may vary. To compare their projectors, one needs full-space identifications, not only the retained unitaries in <a href="#def:modelrecord" data-reference-type="ref+label" data-reference="def:modelrecord">2</a>.

<div id="prop:riesz" class="proposition">

**Proposition 7** (Transported Riesz-projector bound). *Let $`W_a:\mathcal H_a\to\mathcal H_*`$ be unitary and set
``` math
\widetilde G_a=W_aG_aW_a^*.
```
Suppose $`G_*`$ and $`\widetilde G_a`$ are self-adjoint on the same dense domain,
``` math
V_a=\widetilde G_a-G_*
```
is bounded and self-adjoint, and a positively oriented contour $`\Gamma\subset\rho(G_*)`$ encloses the selected reference cluster. Define
``` math
M_*=\sup_{z\in\Gamma}\|(G_*-z)^{-1}\|.
```
If $`M_*\|V_a\|<1`$, then $`\Gamma\subset\rho(\widetilde G_a)`$, and the corresponding spectral projectors satisfy
``` math
\|W_aP_aW_a^*-P_*\|
 \leq
 \frac{\operatorname{length}(\Gamma)}{2\pi}
 \frac{M_*^2\|V_a\|}
      {1-M_*\|V_a\|}.
```
If the right-hand side is below one and $`P_*`$ has finite rank, the retained ranks agree.*

</div>

<div class="proof">

*Proof.* This is the standard Riesz-projector perturbation estimate in the transported Hilbert space. The resolvent identity and Neumann series give
``` math
\|(\widetilde G_a-z)^{-1}\|
 \leq
 \frac{M_*}{1-M_*\|V_a\|}.
```
Integrating the second resolvent identity around $`\Gamma`$ yields the bound. Orthogonal projectors at distance below one have isomorphic ranges. See Kato and Davis–Kahan ; the domain-explicit Modal Triplet Theory specialization is recorded in . ◻

</div>

<div class="remark">

*Remark 8*. <a href="#prop:riesz" data-reference-type="ref+Label" data-reference="prop:riesz">7</a> proves projector and finite-rank stability. It does not prove closeness of the full operators, their Feshbach maps, semigroups, states, observables, or physical interpretations.

</div>

# When the Hilbert spaces genuinely vary

A unitary $`W_a:\mathcal H_a\to\mathcal H_*`$ always exists for Hilbert spaces of the same Hilbert dimension, but it may not represent the geometry or preserve the operators. Singular limits can also change effective spaces. The appropriate literature then uses identification maps and explicit defect bounds rather than pretending the operators already act on one space .

<div class="definition">

**Definition 9** (Quasi-unitary comparison data). A quasi-unitary comparison from $`\mathcal H_{P,a}`$ to $`\mathcal K`$ consists of
``` math
J_a:\mathcal H_{P,a}\to\mathcal K,
 \qquad
 J_a':\mathcal K\to\mathcal H_{P,a},
```
and a defect $`\eta_a\geq0`$ such that
``` math
\|J_a\|,\|J_a'\|\leq1+\eta_a,
```
``` math
\|J_a'J_a-\mathbf 1_{\mathcal H_{P,a}}\|\leq\eta_a,
 \qquad
 \|J_aJ_a'-\mathbf 1_{\mathcal K}\|\leq\eta_a.
```
One then transports the compressed resolvent as
``` math
\widetilde R_a(z)=J_aR_a^P(z)J_a'.
```

</div>

The defect must enter the error budget. For example, if $`\|R_a^P(z)\|\leq r_a`$ on $`\Omega`$, then
``` math
\|\widetilde R_a(z)\|
 \leq
 (1+\eta_a)^2r_a.
```
More substantive convergence statements require compatibility of the forms, domains, or resolvents with $`J_a,J_a'`$. Mosco-type convergence and varying-space norm-resolvent convergence are established frameworks for such problems . The phrase “same coherent sector” is not a replacement for those hypotheses.

# Seven robustness layers

<div class="tabularx">

L0.20L0.28Y Layer & Typical certificate & What it does not imply
Selected rank & Riesz contour, perturbation norm, rank bound & Close reduced operator
Projector & Operator-norm or angle estimate after full-space transport & Stable domains or dynamics
Reduced resolvent & Common $`\Omega`$, retained identification, norm bound & Uniform long-time evolution
Domain or form & Graph-gap, relative-bound, or Mosco hypotheses & Observable agreement
Finite-time dynamics & Generator or semigroup estimate on a declared interval & Arbitrary-time equivalence
States and observables & State channel, observable transport, expectation error & Same microscopic theory
Physical equivalence & Algebra, states, dynamics, symmetries, clocks, and comparison functor & Follows from no single spectral row

</div>

## Finite-time dynamics

<div id="prop:duhamel" class="proposition">

**Proposition 10** (Bounded-generator finite-time comparison). *Let $`H_a,H_b`$ be bounded self-adjoint operators on $`\mathcal K`$ and suppose
``` math
\|H_a-H_b\|\leq\delta.
```
Then for every $`t\in\mathbb R`$,
``` math
\|e^{-itH_a}-e^{-itH_b}\|
 \leq |t|\delta.
```*

</div>

<div class="proof">

*Proof.* Duhamel’s formula gives
``` math
e^{-itH_a}-e^{-itH_b}
 =
 -i\int_0^t
 e^{-i(t-s)H_a}(H_a-H_b)e^{-isH_b}\,\mathrm ds.
```
The unitary factors have norm one. ◻

</div>

This is a standard functional-analytic estimate, not a new Modal Triplet Theory law. It also displays the time horizon explicitly. A local spectral or generator error can accumulate into an order-one phase error at sufficiently long times.

## States and observables

<div id="prop:observable" class="proposition">

**Proposition 11** (Expectation-transfer bound). *Let $`\rho_a,\rho_b`$ be density operators on $`\mathcal K`$, and let $`O_a,O_b\in\mathcal B(\mathcal K)`$ be bounded observables. Then
``` math
\left|
\operatorname{Tr}(\rho_aO_a)-\operatorname{Tr}(\rho_bO_b)
\right|
\leq
\|\rho_a-\rho_b\|_1\,\|O_a\|
+
\|O_a-O_b\|.
```*

</div>

<div class="proof">

*Proof.* Insert and subtract $`\operatorname{Tr}(\rho_bO_a)`$. Trace duality bounds the first difference by $`\|\rho_a-\rho_b\|_1\|O_a\|`$. Since $`\|\rho_b\|_1=1`$, the second is bounded by $`\|O_a-O_b\|`$. ◻

</div>

The proposition shows why reduced-resolvent agreement is not yet empirical agreement. One must also transport states and observables and bound their errors.

# Three boundary counterexamples

<div id="ex:continuum" class="example">

**Example 12** (A robust continuum need not be a small landscape). For each $`\lambda\in[0,1]`$, let
``` math
\mathcal H_\lambda=\mathbb C^3,
 \qquad
 T_\lambda=
 \begin{pmatrix}
 0&0&0\\
 0&2&0\\
 0&0&3+\lambda
 \end{pmatrix},
 \qquad
 P_\lambda=
 \begin{pmatrix}
 1&0&0\\
 0&0&0\\
 0&0&0
 \end{pmatrix}.
```
The selected eigenvalue is isolated by a uniform gap of at least two. All retained spaces are the same line, and for every common $`z\neq0`$,
``` math
R_\lambda^P(z)=-z^{-1}.
```
Thus
``` math
d_\Omega(\lambda,\mu)=0
```
for all $`\lambda,\mu`$, while the eliminated spectrum varies continuously. Local coherent-sector robustness is therefore compatible with a continuum of microscopically distinct models.

</div>

<div id="ex:observable" class="example">

**Example 13** (The same reduced spectrum can give different observables). Take two records with the same one-dimensional retained Hilbert space and the same compressed resolvent. Give the first record the observable $`O_0=0`$ and the second $`O_1=\mathbf 1`$. Their unique normalized state gives
``` math
\operatorname{Tr}(\rho O_0)=0,
 \qquad
 \operatorname{Tr}(\rho O_1)=1.
```
The spectral comparison error is zero, but the predictions differ. An observable identification is indispensable.

</div>

<div id="ex:time" class="example">

**Example 14** (Projector stability is not arbitrary-time stability). On $`\mathbb C`$, take $`H_0=0`$ and $`H_\varepsilon=\varepsilon`$. The projector is identical and the resolvents converge away from their poles. At
``` math
t=\frac{\pi}{\varepsilon},
```
however,
``` math
\|e^{-itH_\varepsilon}-e^{-itH_0}\|=2.
```
Finite-time bounds do not become uniform-in-time equivalence merely because $`\varepsilon`$ is small.

</div>

# What landscape reduction would require

Let $`\mathfrak V`$ be a declared candidate set and let
``` math
C:\mathfrak V\to\{0,1\}
```
be a certified admissibility predicate. The surviving set is
``` math
\mathfrak V_{\rm adm}
 =
 \{v\in\mathfrak V:C(v)=1\}.
```
This is a filter. It becomes a landscape-reduction result only after additional questions are answered:

1.  How is $`\mathfrak V`$ defined or enumerated?

2.  Is $`C`$ decidable or certifiable on every candidate in scope?

3.  What measure, index, or counting convention defines “most”?

4.  Is the surviving set finite, discrete, compact, or merely nonempty?

5.  What dynamics or selection rule chooses among multiple survivors?

6.  Which survivor is empirically identified with our universe?

Flux-vacuum counts in string theory illustrate why these inputs matter: they start from a specified ensemble, charge cutoff, and index or distribution . A local operator gap by itself provides none of that counting data.

<div id="prop:nonselection" class="proposition">

**Proposition 15** (An admissibility predicate does not imply uniqueness). *If $`|\mathfrak V_{\rm adm}|>1`$, then the predicate $`C`$ alone does not select a unique element of $`\mathfrak V_{\rm adm}`$.*

</div>

<div class="proof">

*Proof.* Every survivor has the same predicate value $`1`$. No rule using only that value distinguishes two different survivors. ◻

</div>

The logical separation among mathematical existence, chart validity, admissibility, realization, and empirical identification is developed in . Local robustness belongs between admissibility and controlled realization; it is not a substitute for the later layers.

# Current MTT application map

The present paper does not use older papers as proof sources merely because they contain the word “universality.” It reads the selected current revisions at their declared tiers.

<div class="tabularx">

L0.20L0.25Y Target family & Current established role & Missing comparison or selection rows
Fixed-point framework & Conditional analytic existence and stability under stated hypotheses & Physical carrier, source map, and realization theorem
Calabi–Yau & Conditional lower realization target; fixed compact elliptic problems have standard spectral control & Uniformity over moduli, stable visible–hidden bundle, worldsheet, stabilization, and unique selection
Heterotic/Fu–Yau & Exact local and finite ingredients; Lens–Nil is auxiliary; selected $`q=79`$ is a completion program & Physical rank-three visible–hidden endpoint and common comparison operator
Perturbative string & Conditional typed encoding at declared order and genus & Complete physical worldsheet record, exact infrared SCFT, GSO/modular data, and quantum completion
M-theory low-energy limit & Conditional eleven-dimensional target record & Selected spin geometry, differential C-field, action, branes, and action-preserving upper map
Quantum gravity & Exact finite TT support and conditional/fixed-order low-energy parity & Physical normalization, complete state and measure, selected higher-derivative values, and nonperturbative UV completion

</div>

This table does not say the programs are incompatible. It says that a common comparison class must be earned by constructing the same typed rows for each member and transporting them through explicit maps.

# A complete cross-model certificate

<div class="definition">

**Definition 16** (Cross-model robustness certificate). A cross-model certificate for records $`a,b`$ contains
``` math
\mathfrak C_{a\leftrightarrow b}
=
\bigl(
\mathfrak C_a,\mathfrak C_b,
\Omega,
U_a,U_b,
d_\Omega,
\varepsilon_{\rm chain},
\mathfrak T,
\mathfrak O,
\mathfrak I,
\pi
\bigr),
```
where:

- $`\mathfrak C_a,\mathfrak C_b`$ are complete single-model reduction certificates;

- $`\Omega`$ is the common full and eliminated-sector resolvent region;

- $`U_a,U_b`$, or their quasi-unitary replacements, are the identification maps;

- $`d_\Omega`$ is the transported compressed-resolvent error;

- $`\varepsilon_{\rm chain}`$ is the accumulated error across all intermediate arrows;

- $`\mathfrak T`$ records any finite-time, semigroup, graph, or form comparison;

- $`\mathfrak O`$ records state, observable, and expectation transport;

- $`\mathfrak I`$ records clocks, units, symmetries, and physical interpretation; and

- $`\pi`$ records provenance and theorem status.

</div>

## Numerical execution

For a finite or Galerkin comparison, an executable packet should report:

1.  basis dimensions and immutable basis hashes;

2.  Hermiticity and projector residuals;

3.  source and rank of every projector;

4.  interval enclosures for the common spectral region;

5.  certified norms of the eliminated resolvents and couplings;

6.  the retained identification matrices and their unitary defects;

7.  interval bounds for $`d_\Omega`$;

8.  every discretization, reduction, transport, and roundoff error separately;

9.  state and observable comparison rows when empirical claims are made; and

10. a continuum-transfer theorem when the physical target is not the finite object itself.

An exact finite calculation is exact for the finite object. It is not a continuum, string, gravitational, or physical-equivalence theorem until the corresponding transfer rows are supplied.

# Ownership of the mathematics

Spectral projections, resolvent perturbation, closed-operator stability, and semigroup estimates belong to established operator theory . Frameworks for convergence across varying Hilbert spaces and spectral structures are likewise established .

The Modal Triplet Theory Foundation owns the general admissibility and status semantics . The companion coherent-sector paper owns the domain-explicit Feshbach reduction, exact-projector correction, and single-model robustness estimate . The current Calabi–Yau, heterotic, string, M-theory, and quantum-gravity papers own their individual realization records and boundaries.

This paper owns only the integration layer:

- the transported cross-model record;

- the common-region compressed-resolvent comparison;

- chainwise accumulation of reduction and comparison errors;

- the state-observable transfer requirement;

- the explicit seven-layer robustness hierarchy; and

- the counterexamples separating local robustness from landscape reduction and physical equivalence.

# Claim status and limitations

<div class="tabularx">

L0.31L0.18Y Statement & Status here & Boundary
Single-model Feshbach reduction & Imported & Domain-explicit companion theorem
Transported resolvent comparison & Proved & Common $`\Omega`$, declared identifications
Chainwise error accumulation & Proved & Sum bound; no assumed cancellation
Riesz-projector stability & Imported and specialized & Fixed transported domain, bounded perturbation
Finite-time bounded dynamics & Standard and proved & Bounded generators, declared time interval
Expectation transfer & Proved & Density operators and bounded observables
Varying-space convergence & Contract only & Requires quasi-unitary, Mosco, form, or resolvent theorem
One global MTT universality class & Not established & No common source and full comparison record
Landscape reduction & Not established & Requires candidate set, count/measure, filter execution, and selection
Physical equivalence & Not established & Requires states, observables, dynamics, symmetries, clocks, and units

</div>

# Completion and falsifiability contract

A claimed cross-model class is complete only if it supplies:

1.  one exact list of models or a precisely quantified family;

2.  one valid single-model reduction certificate for every member;

3.  explicit full-space or retained-space identification maps;

4.  a nonempty common spectral region;

5.  fixed-domain, graph, form, or varying-space hypotheses appropriate to the claimed topology;

6.  a certified transported error and an accumulated chain budget;

7.  finite-time or semigroup control if dynamics is claimed;

8.  state and observable maps if predictions are compared;

9.  clock, unit, symmetry, and interpretation maps if physical equivalence is claimed; and

10. an enumeration, measure, decision procedure, and selector if landscape reduction or unique-vacuum selection is claimed.

The claim fails in its declared regime if the contour meets the spectrum, the retained rank changes, the common resolvent region becomes empty, an identification defect exceeds its tolerance, accumulated error exceeds the observable budget, the domain topology changes without control, or a held-out observable violates the expectation bound.

# Conclusion

Coherent-sector robustness is a meaningful and useful local statement. It says that after each model has supplied a valid reduction and after the retained spaces have been explicitly identified, their bounded compressed resolvents can be compared with a certified error.

That statement does not become global universality by changing its name. Projectors, domains, resolvents, finite-time dynamics, states, observables, and physical interpretation are different layers. Their errors accumulate through a chain. A continuum of microscopic models can share exactly the same retained resolvent, and equal spectral data can still support different observables.

The corrected role of this paper is therefore precise. It supplies the mathematical language by which future Modal Triplet Theory branches can prove that they belong to one controlled local comparison class. The current Calabi–Yau, heterotic, string, M-theory, and quantum-gravity branches are valuable conditional targets and partial constructions, but their common physical equivalence and any resulting landscape reduction remain theorem obligations rather than established conclusions.

# Reproducibility statement

No numerical result is claimed in this paper. Every displayed estimate is analytic and can be checked directly from the stated assumptions. Application-level computations must publish the single-model certificates, identification maps, interval or exact norm bounds, source hashes, and accumulated error ledger described in <a href="#sec:certificate" data-reference-type="ref+label" data-reference="sec:certificate">11</a>.
