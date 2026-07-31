---
abstract: |
  Topological phases cannot be identified from generic overlap structure alone. A valid cocycle glues local frames into a bundle; it does not make that bundle trivial. Nontriviality is carried by the cocycle class, or by the corresponding projector, symmetry-protected, many-body, or operator-algebraic invariant. This paper corrects an earlier formulation that treated failure of the cocycle condition as the source of topology and then inferred robustness and bulk–boundary correspondence without the needed Hamiltonian and index hypotheses.

  We give a typed phase record containing the physical algebra or Hamiltonian, Fermi or ground-state projector, symmetry class, gap condition, invariant, allowed deformations, and interface construction. For a smooth gapped two-dimensional class-A family, the occupied projector defines a vector bundle whose first Chern number is constant along every uniform gap-preserving homotopy. A quantitative norm bound gives an explicit stability certificate. We then separate the free-fermion tenfold-way setting from mobility-gap, interacting, symmetry-protected, and intrinsic topological-order settings. Bulk–boundary correspondence is stated in its proper conditional form: a Toeplitz or interface index theorem maps a difference of bulk classes to protected boundary spectral flow or transport.

  Modal Triplet Theory (MTT) supplies useful language for projection, admissibility, coherent projectors, and local spectral stability, but those objects are not automatically Fermi projectors or condensed-matter phase invariants. We prove an exact and an error-controlled pullback theorem: once a selected MTT source emits the complete typed phase record and intertwines its allowed deformations, the standard topological invariant becomes a stable label of that encoding. Current MTT has not yet supplied such a selected source for all topological phases. The result is therefore a rigorous conditional bridge and completion contract, not a new universal classification.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: cb16cd6d384633e46ae9df5ea4dc9c6a4cb807a13f1f5591c8993eb1b6751f6f
paper_id: topological-phases-of-matter-as-admissible-overlap-stru-837dec46
release_state: zenodo_released
released_version: v2
title: |
  **Topological Phases as Bundle and Index Data:**
  A Conditional Projection-Admissible Encoding in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.21711367
zenodo_record_id: 21711367
zenodo_url: "https://zenodo.org/records/21711367"
---

# Revision note for Version 2

<div class="description">

Version 1, DOI [10.5281/zenodo.18261859](https://doi.org/10.5281/zenodo.18261859).

Version 1 defined global admissibility by the cocycle condition and then called a phase topological when that same condition failed. This is mathematically reversed: a cocycle is precisely the datum that constructs a bundle, including a nontrivial bundle. The paper also inferred phase basins, quantization, disorder and interaction robustness, and universal boundary modes from assumptions too weak to imply them.

Version 2 distinguishes gluing from trivialization, supplies the missing Hamiltonian, projector, symmetry, gap, invariant, deformation, and boundary data, and separates free, disordered, interacting, symmetry-protected, and intrinsically ordered systems. Robustness and bulk–boundary statements are proved or imported only on their declared domains.

Local descriptions and their overlap maps remain an effective language for vector bundles, projective modules, and related global data. Projection-admissibility can organize a topological phase once a physical source supplies the complete phase record.

Current MTT does not select a condensed-matter Hamiltonian, protecting symmetry, invariant, and boundary index construction for every phase. The bridge remains conditional on the certificate in <a href="#sec:mtt" data-reference-type="ref+label" data-reference="sec:mtt">9</a>.

</div>

# The corrected question

Topological phases combine several ideas that must not be collapsed into one word:

1.  local frames or local effective descriptions can be glued;

2.  the resulting global bundle or projective module can be nontrivial;

3.  a gapped Hamiltonian or ground-state family selects the relevant projector;

4.  a symmetry class restricts the allowed deformations;

5.  an invariant is constant along those allowed deformations; and

6.  a separate index or anomaly theorem can connect bulk and boundary.

The first item is not the negation of the second. Nor do the first two identify a physical phase without the remaining data.

The corrected question is therefore:

> When does a selected MTT projection encode a complete topological-phase record, so that established homotopy and index theorems can be transferred without changing their hypotheses?

This paper answers that structural question. It does not replace the classification of topological insulators and superconductors , the noncommutative treatment of disorder , or many-body constructions .

# What a phase claim must specify

<div id="def:record" class="definition">

**Definition 1** (Typed topological-phase record). A topological-phase record is a tuple
``` math
\mathfrak P
 =
 (\mathcal A,\mathcal H,H,\mu,P,\mathsf S,g,\mathcal D,
   \mathcal I,\mathcal B,\varepsilon,\mathfrak p)
```
with the following declared meanings:

1.  $`\mathcal A`$ is the observable or bulk algebra and $`\mathcal H`$ its representation space;

2.  $`H`$ is the Hamiltonian or specified many-body generator and $`\mu`$ is the Fermi energy or other reference level;

3.  $`P`$ is the Fermi projector, ground-state projector, or other explicitly typed phase-defining object;

4.  $`\mathsf S`$ contains the protecting symmetries and their representations;

5.  $`g`$ states a spectral-gap, mobility-gap, or many-body-gap hypothesis;

6.  $`\mathcal D`$ is the class of allowed deformations;

7.  $`\mathcal I`$ is the invariant and its target group;

8.  $`\mathcal B`$ is the boundary or interface construction, if one is claimed;

9.  $`\varepsilon`$ is an analytic or numerical error budget; and

10. $`\mathfrak p`$ records provenance, conventions, and source hashes.

</div>

Different physical settings populate this record differently. For a periodic free fermion, $`H=H(k)`$ is a Bloch Hamiltonian and $`P(k)`$ is its occupied-band projector. For a disordered covariant system, $`\mathcal A`$ is typically a crossed-product algebra and the invariant uses a trace per unit volume. For an interacting Hall system, $`P`$ can be a ground-state projector over a torus of inserted fluxes. Intrinsic topological order requires still richer superselection, fusion, braiding, or ground-state degeneracy data.

<div class="remark">

*Remark 2* (Why the tuple is not bureaucracy). Without $`\mathsf S`$, one does not know which perturbations are allowed. Without $`g`$, one does not know whether the projector varies continuously. Without $`\mathcal I`$, the phrase “topologically distinct” has no declared mathematical target. Without $`\mathcal B`$, bulk topology alone does not specify which edge operator is being indexed.

</div>

# Cocycles glue bundles; coboundaries trivialize them

Let $`X`$ be a compact base with open cover $`\{U_\alpha\}`$. A rank-$`r`$ complex vector bundle can be described by transition maps
``` math
g_{\alpha\beta}:U_\alpha\cap U_\beta\longrightarrow GL(r,\mathbb{C})
```
obeying
``` math
g_{\alpha\alpha}=I,\qquad
 g_{\alpha\beta}=g_{\beta\alpha}^{-1},\qquad
 g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=I.
```
The final identity is the cocycle condition. It is the consistency condition for gluing, not a criterion for trivial topology .

<div id="prop:cocycle" class="proposition">

**Proposition 3** (Gluing is not trivialization). *A transition cocycle $`\{g_{\alpha\beta}\}`$ defines a vector bundle. That bundle is trivial precisely when there are local maps $`h_\alpha:U_\alpha\to GL(r,\mathbb{C})`$ such that
``` math
g_{\alpha\beta}=h_\alpha h_\beta^{-1}
```
on every overlap. Thus a valid cocycle may represent either a trivial or a nontrivial bundle; triviality asks whether its class is a coboundary.*

</div>

<div class="proof">

*Proof.* The quotient of the disjoint union $`\coprod_\alpha U_\alpha\times\mathbb{C}^r`$ by $`(x,v)_\beta\sim(x,g_{\alpha\beta}(x)v)_\alpha`$ is transitive exactly because of the cocycle condition, and therefore defines a bundle. If the displayed $`h_\alpha`$ exist, the local maps $`(x,v)_\alpha\mapsto(x,h_\alpha(x)^{-1}v)`$ agree on overlaps and provide a global trivialization. Conversely, comparing any global frame with the local frames produces such $`h_\alpha`$. ◻

</div>

<div id="ex:clutching" class="example">

**Example 4** (A valid cocycle with nonzero Chern class). Cover $`S^2`$ by neighborhoods of the northern and southern hemispheres. Their overlap retracts to the equator $`S^1`$. The clutching map
``` math
g_{NS}(e^{i\varphi})=e^{i\varphi}
```
obeys all overlap consistency conditions and has winding number one. It defines the degree-one complex line bundle, with $`c_1=1`$, and cannot be a coboundary. This directly disproves the Version 1 identification of a valid global completion with topological triviality.

</div>

The correct overlap statement is consequently:

> Topological information may be represented by the equivalence class of valid gluing data. It is not produced by a failure to glue.

Gerbes, anomalies, defects, and higher categorical structures can involve genuine higher obstruction classes, but each must be typed separately. One cannot infer them from the word “overlap.”

# The class-A Chern phase

The simplest complete example is a periodic, charge-conserving, two-dimensional free-fermion system. Let
``` math
H:\mathbb{T}^2\longrightarrow \operatorname{Herm}(N)
```
be smooth, place the Fermi level at zero, and assume the uniform gap
``` math
g=\inf_{k\in\mathbb{T}^2}\operatorname{dist}(0,\sigma(H(k)))>0.
```
Functional calculus then gives a smooth occupied projector
``` math
P(k)=\mathbf 1_{(-\infty,0)}(H(k)).
```
Its ranges form the occupied vector bundle
``` math
E=\bigsqcup_{k\in\mathbb{T}^2}\operatorname{Ran}P(k)\longrightarrow\mathbb{T}^2.
```
The first Chern number is
``` math
\begin{equation}
 C_1(P)
 =
 \frac{1}{2\pi i}
 \int_{\mathbb{T}^2}\operatorname{Tr}\!\left(P\,dP\wedge dP\right)
 \in\mathbb{Z}.
\label{eq:chern}
\end{equation}
```
This is the bundle invariant entering the integer Hall setting .

<div id="thm:homotopy" class="theorem">

**Theorem 5** (Uniform-gap homotopy invariance). *Let $`H_t(k)`$, $`t\in[0,1]`$, be a smooth family of finite-dimensional Hermitian Bloch Hamiltonians satisfying
``` math
\inf_{(k,t)\in\mathbb{T}^2\times[0,1]}
 \operatorname{dist}(0,\sigma(H_t(k)))>0.
```
Then the occupied bundles at $`t=0`$ and $`t=1`$ are isomorphic in $`K^0(\mathbb{T}^2)`$, and
``` math
C_1(P_0)=C_1(P_1).
```*

</div>

<div class="proof">

*Proof.* The uniform gap permits one contour in the resolvent set of every $`H_t(k)`$. The Riesz formula therefore defines a smooth projector
``` math
P(k,t)=\frac{1}{2\pi i}\oint_\Gamma
          (z-H_t(k))^{-1}\,dz
```
on $`\mathbb{T}^2\times[0,1]`$. Its range is a vector bundle over that product. The two endpoint bundles are its pullbacks along homotopic inclusions $`\mathbb{T}^2\hookrightarrow\mathbb{T}^2\times[0,1]`$, so they have the same $`K`$-class and the same first Chern class. ◻

</div>

<div id="prop:norm" class="proposition">

**Proposition 6** (An explicit norm-stability certificate). *Suppose $`H(k)`$ has gap $`g>0`$ at zero and $`V(k)`$ is a continuous Hermitian perturbation satisfying
``` math
\sup_{k\in\mathbb{T}^2}\|V(k)\|<g.
```
Then $`H_t=H+tV`$ remains gapped for every $`t\in[0,1]`$, and its Chern number equals that of $`H`$.*

</div>

<div class="proof">

*Proof.* For self-adjoint matrices, spectral stability gives
``` math
\operatorname{dist}(0,\sigma(H(k)+tV(k)))
 \geq
 \operatorname{dist}(0,\sigma(H(k)))-t\|V(k)\|.
```
The right-hand side is uniformly positive. Apply <a href="#thm:homotopy" data-reference-type="ref+label" data-reference="thm:homotopy">5</a>. ◻

</div>

This is the precise sense in which a Chern phase is robust here. The claim does not cover arbitrary perturbations: the perturbation must remain in the declared class and preserve the relevant gap. The same logic applies to other invariants only after their symmetries and domains are specified.

# Symmetry changes the classification

For gapped free fermions, time-reversal, particle-hole, and chiral symmetry lead to the ten Altland–Zirnbauer classes. Stable classification depends on both the class and spatial dimension . A few representative entries are shown in <a href="#tab:classes" data-reference-type="ref+label" data-reference="tab:classes">[tab:classes]</a>.

<div class="center">

<span id="tab:classes" label="tab:classes"></span>

<div class="tabularx">

@l c c Y Y@ Class & Dimension & Stable group & Representative invariant & Protection retained in the deformation
$`\mathsf{AIII}`$ & $`1`$ & $`\mathbb{Z}`$ & chiral winding number & chiral symmetry and bulk gap
$`\mathsf{D}`$ & $`1`$ & $`\mathbb{Z}_2`$ & Majorana-chain parity & particle-hole structure and bulk gap
$`\mathsf{A}`$ & $`2`$ & $`\mathbb{Z}`$ & first Chern number & charge-conserving class-A structure and bulk gap
$`\mathsf{D}`$ & $`2`$ & $`\mathbb{Z}`$ & superconducting Chern number & Bogoliubov–de Gennes particle-hole structure and bulk gap
$`\mathsf{AII}`$ & $`2`$ & $`\mathbb{Z}_2`$ & Kane–Mele invariant & time reversal with $`T^2=-1`$ and bulk gap
$`\mathsf{AII}`$ & $`3`$ & $`\mathbb{Z}_2`$ & strong topological-insulator index & time reversal with $`T^2=-1`$ and bulk gap
$`\mathsf{DIII}`$ & $`3`$ & $`\mathbb{Z}`$ & winding number & time reversal, particle-hole structure, and bulk gap

</div>

<div class="minipage">

**Table .** Representative strong stable free-fermion classifications. A Brillouin torus can carry additional weak indices tied to translation structure. The table is not an interacting classification.

</div>

</div>

The two-dimensional class-$`\mathsf{AII}`$ invariant distinguishes the quantum spin Hall phase from an ordinary time-reversal invariant insulator . If time reversal is broken, that $`\mathbb{Z}_2`$ protection need not survive. Conversely, two projectors that are homotopic as complex bundles may remain inequivalent inside a narrower symmetry class. This is why “the overlap class” is not a complete physical invariant until its symmetry constraints are included.

Interactions can also change the classification. In the one-dimensional BDI Majorana chain, an integer free-fermion classification reduces to $`\mathbb{Z}_8`$ when suitable interactions are allowed . Generic overlap language cannot decide this reduction; the many-body deformation class does.

# Disorder and mobility gaps

Translation symmetry is not required for every topological invariant, but removing it changes the mathematical object. For a covariant disordered class-A system, the Fermi projection belongs to a noncommutative bulk algebra. Under suitable localization or mobility-gap hypotheses, the Hall invariant can be expressed schematically as
``` math
\operatorname{Ch}_2(P)
 =
 2\pi i\,\mathcal T\!\left(
 P[\nabla_1P,\nabla_2P]\right),
```
where $`\mathcal T`$ is a trace per unit volume and the derivations encode position directions. Bellissard, van Elst, and Schulz-Baldes prove quantization and plateaux in the localized regime .

Three cautions matter:

1.  a mobility gap is not literally an empty spectral interval;

2.  the smooth Bloch-bundle formula <a href="#eq:chern" data-reference-type="ref+label" data-reference="eq:chern">[eq:chern]</a> cannot simply be reused after translation symmetry is removed; and

3.  stability requires the analytic localization/Sobolev hypotheses of the noncommutative construction, not merely the statement that disorder is local.

MTT’s finite noncommutative-geometry encoding can supply compatible algebra and projector language , but it does not by itself select the covariant disorder algebra, trace, localization domain, or physical Fermi projection.

# Interacting systems are not one-particle bundles

For an interacting two-dimensional system on a torus, one standard construction inserts boundary-condition fluxes $`\theta=(\theta_1,\theta_2)\in\mathbb{T}^2`$. If a unique ground state stays uniformly separated from the rest of the spectrum, its projector $`\Pi(\theta)`$ defines a line bundle over the flux torus. More generally, a gapped ground-state multiplet defines a vector bundle. Its many-body Chern number has the same projector form
``` math
C_{\mathrm{MB}}
 =
 \frac{1}{2\pi i}\int_{\mathbb{T}^2}
 \operatorname{Tr}\!\left(\Pi\,d\Pi\wedge d\Pi\right).
```
Niu, Thouless, and Wu use this kind of parameter-space topology to formulate Hall conductance in the presence of interactions and disorder . Hastings and Michalakis prove integer quantization, up to finite-size corrections, for a local interacting system with a unique gapped ground state and conserved charge under their stated hypotheses .

This does not classify every interacting phase. Two broad notions must be distinguished:

<div class="description">

A short-range-entangled gapped phase can be nontrivial only while a protecting symmetry is retained. Interacting bosonic examples require data beyond the free-fermion periodic table .

Long-range-entangled phases can carry topological ground-state degeneracy, superselection sectors, quantum dimensions, fusion, and braiding. Topological entanglement entropy probes part of this data .

</div>

Consequently, replacing one-particle transition maps by unspecified “operator-algebra overlaps” does not prove a classification. The algebra, state sector, deformation relation, and invariant must be supplied. In particular, an occupied-band projector cannot encode intrinsic anyon data without an additional theorem.

# Bulk–boundary correspondence is an index theorem

The intuitive statement that a boundary must “compensate” a bulk obstruction is useful only after the compensation is represented by a specified index or anomaly. In the integer quantum Hall setting, the bulk Chern number and edge winding or edge-current index are related by bulk–edge theorems .

<div id="thm:bulkedge" class="theorem">

**Theorem 7** (Conditional bulk–interface consequence). *Let $`\mathcal A`$ be a declared bulk algebra and
``` math
0\longrightarrow\mathcal E
 \longrightarrow\mathcal T
 \longrightarrow\mathcal A
 \longrightarrow0
```
a boundary or interface Toeplitz extension for the chosen physical model. Let two bulk phases define classes $`[P_+],[P_-]\in K_0(\mathcal A)`$. Assume:*

1.  *locality and the bulk gap or mobility-gap hypotheses needed for the extension and pairings;*

2.  *any protecting symmetry required by the class;*

3.  *a Fredholm boundary construction representing the connecting class $`\partial([P_+]-[P_-])`$; and*

4.  *the applicable bulk–edge pairing theorem for this extension.*

*Then
``` math
\operatorname{Ind}_{\mathrm{edge}}
 =
 \left\langle \operatorname{Ch}_{\mathrm{bulk}},
 [P_+]-[P_-]\right\rangle .
```
If the right-hand side is nonzero, the boundary index cannot be removed by a perturbation that preserves the hypotheses and Fredholmness.*

</div>

<div class="proof">

*Proof.* The extension supplies the connecting map from the bulk $`K`$-class to the edge class. By the assumed bulk–edge theorem, naturality of the index pairing identifies the edge Fredholm index with the bulk pairing. Fredholm index is invariant under norm-continuous Fredholm perturbations, so a nonzero value cannot become zero while the hypotheses remain valid. ◻

</div>

The conclusion may appear physically as chiral edge transport, protected spectral flow, or symmetry-protected boundary degrees of freedom. It does not say that every boundary has an isolated zero-energy eigenstate at every momentum. It also does not say that a trivial bulk forbids accidental boundary states. For interacting SPT phases, a boundary may be gapped by breaking the protecting symmetry or, in some dimensions, by developing appropriate boundary topological order. Those possibilities were absent from Version 1.

# The conditional MTT encoding

MTT distinguishes retained coherent data from complementary unresolved data. This resembles the use of projectors in topology, but the projectors have different types:

- $`P_{\mathrm{coh}}`$ is an MTT coherent or low-mode projector selected from an internal operator problem;

- $`P_F=\mathbf 1_{(-\infty,\mu)}(H)`$ is a Fermi projector selected by a condensed-matter Hamiltonian and reference energy; and

- $`\Pi`$ can be a many-body ground-state projector over a parameter space.

Equal ranks or similar matrices do not identify them.

<div id="def:certificate" class="definition">

**Definition 8** (MTT topological-phase encoding certificate). For a selected MTT source $`s`$, a certificate consists of:

1.  a source-hashed MTT algebra, state space, operator, and coherent projector;

2.  a map $`E_s`$ into every row of a phase record $`\mathfrak P_s`$ from Definition <a href="#def:record" data-reference-type="ref" data-reference="def:record">1</a>;

3.  an intertwiner identifying the relevant MTT subspace with the Fermi or ground-state range, rather than merely matching dimensions;

4.  a map from allowed MTT continuations to symmetry- and gap-preserving physical deformations;

5.  an exactness statement or error bound below a declared gap margin;

6.  an invariant evaluator and, if claimed, a boundary/interface index construction; and

7.  provenance and independent verification for all selected inputs.

</div>

<div id="thm:pullback" class="theorem">

**Theorem 9** (Exact and controlled pullback). *Let $`s_t`$, $`t\in[0,1]`$, be an allowed MTT continuation equipped with a certificate from Definition <a href="#def:certificate" data-reference-type="ref" data-reference="def:certificate">8</a>.*

**Exact case.* If its encoded Hamiltonians $`H_t=E_{s_t}(H)`$ form a continuous symmetry-preserving path with a uniform gap and the encoded projectors are their actual Fermi or ground-state projectors, then every homotopy invariant declared in the phase record is constant along $`s_t`$. In particular, different invariant values obstruct such a certified continuation.*

**Controlled case.* Suppose instead that the certificate emits approximate Hamiltonians $`\widetilde H_t`$ with uniform reference gap $`g>0`$ and verified errors
``` math
\sup_t\|H_t-\widetilde H_t\|\leq\varepsilon<g,
```
with the same protecting symmetries. Then $`H_t`$ and $`\widetilde H_t`$ are connected by a symmetry- and gap-preserving straight line, and they carry the same declared stable invariant.*

</div>

<div class="proof">

*Proof.* In the exact case, composition of the MTT continuation with the certificate is an allowed physical homotopy, so homotopy invariance applies. In the controlled case, spectral stability bounds the gap of $`(1-u)\widetilde H_t+uH_t`$ from below by $`g-\varepsilon>0`$ for $`u\in[0,1]`$. The symmetry-preserving interpolation therefore leaves the invariant unchanged. ◻

</div>

<div class="remark">

*Remark 10* (What this theorem does and does not derive). The theorem transfers an established invariant after the physical phase record has been selected. It does not derive a Hamiltonian, a symmetry class, or the numerical invariant from projection alone. Those are source rows of the certificate, not conclusions hidden in the word “admissibility.”

</div>

## Current MTT status

The current MTT corpus supplies relevant ingredients:

1.  Foundations specifies the coherent projector, local spectral stability, and the distinction between structural support and selected physical realization .

2.  Projection–Admissibility types descent, recovery, and the limits of a generic projection argument .

3.  Coherent-Sector Robustness gives transported-resolvent and projector-stability conditions across declared model families .

4.  The noncommutative-geometry paper supplies a typed finite almost-commutative encoding, while explicitly retaining the nonzero-Chern continuum source as an open boundary .

5.  Topological Consistency Conditions separates Chern-class and index constraints from holomorphic, equivariant, and selected physical source claims .

These results support the syntax of Definition <a href="#def:certificate" data-reference-type="ref" data-reference="def:certificate">8</a>. They do not currently emit a selected condensed-matter Hamiltonian and complete phase record for every row of <a href="#tab:classes" data-reference-type="ref+label" data-reference="tab:classes">[tab:classes]</a>, every mobility-gap model, or every interacting topological order. No new material prediction or universal phase classification is claimed here.

# Comparison with established results

<div class="center">

<span id="tab:comparison" label="tab:comparison"></span>

<div class="tabularx">

@\>

p0.23Y Y@

Framework & Supplied physical data & Correct MTT relation
TKNN / class A & Bloch Hamiltonian, Fermi gap, occupied bundle, first Chern number & Exact example of a complete phase record; MTT must select and intertwine these rows
Tenfold way & Discrete symmetries, spatial dimension, stable $`K`$-theory group & Shows why generic overlap data are insufficient without symmetry
Noncommutative Hall geometry & Covariant bulk algebra, trace per volume, derivations, localization domain & Compatible with MTT’s algebraic language, but requires a selected disorder representation and mobility-gap certificate
Many-body flux torus & Local interacting Hamiltonian, conserved charge, ground-state gap and flux-family projector & Replaces one-particle bundle data; cannot be inferred from the coherent projector alone
Bulk–edge index theory & Bulk class, boundary extension, Fredholm operator, pairing hypotheses & Gives a precise meaning to boundary compensation after the interface object is supplied
Intrinsic topological order & Ground-state degeneracy and superselection, fusion, braiding, or entanglement data & Requires a richer selected encoding than vector-bundle overlaps

</div>

<div class="minipage">

**Table .** The external theories are not special cases of generic MTT overlap syntax. They become conditional MTT encodings only through a complete certificate.

</div>

</div>

# Completion and falsifiability

The proposed bridge fails for a claimed model if any of the following occurs:

1.  the transition data do not define the stated bundle or module;

2.  the claimed cocycle class is actually a coboundary, or the computed invariant is zero;

3.  the chosen projector is not the Fermi or ground-state projector of the declared Hamiltonian;

4.  the spectral or mobility gap fails on the claimed deformation;

5.  a perturbation breaks the protecting symmetry while the old invariant is still asserted;

6.  a free-fermion invariant is applied to an interacting phase without a many-body stability theorem;

7.  a disordered invariant is evaluated without the required covariance, trace, or localization hypotheses;

8.  a boundary claim lacks a Toeplitz, Fredholm, anomaly, or equivalent interface theorem;

9.  the MTT and physical projectors merely have equal rank rather than a verified intertwiner;

10. the approximation error reaches the protective gap margin; or

11. selected source values or provenance cannot be independently replayed.

A future computational realization should therefore publish the entire record $`\mathfrak P`$, source hashes, symmetry checks, gap lower bounds, projector residuals, invariant computation, error intervals, and the boundary-index map. A visually suggestive edge spectrum or an integer obtained after fitting is not by itself a certificate.

# Conclusion

Topological phases are not failures of consistent gluing. Valid cocycles construct bundles, and nontrivial cocycle classes distinguish some of those bundles from trivial ones. A physical phase additionally requires a Hamiltonian or many-body source, a protecting symmetry class, a gap condition, an allowed deformation category, and an invariant. Robustness is homotopy invariance on that domain. Bulk–boundary correspondence is an index or anomaly theorem for a declared interface, not an automatic consequence of local overlap language.

MTT remains useful at the correct level. Its projection and admissibility framework can organize the source, retained sector, continuation, and error data. Once a selected source emits the complete phase record and the intertwining certificate, <a href="#thm:pullback" data-reference-type="ref+label" data-reference="thm:pullback">9</a> transfers the standard topological invariant to the MTT encoding. Until then, generic overlap structure is a representation language rather than a derivation of all topological phases. That distinction both corrects the earlier paper and turns its central intuition into a testable research program.
