---
abstract: |
  Topology can constrain a four-dimensional effective theory, but only after the global gauge group, field representations, internal bundles, zero-mode spaces, coefficient bundles, and contraction maps have been specified. This paper replaces an earlier topology-only argument by that typed statement. For a fixed global gauge group, characters of its $`U(1)`$ factor form an integer lattice; rational hypercharges arise after a normalization choice and quotient compatibility conditions. This lattice does not by itself select the observed matter representations. Gauge anomalies are encoded by the determinant or Pfaffian line of a family of chiral Dirac operators over background-field space, rather than by the determinant of the matter bundle on spacetime. Local anomaly is detected by curvature and global anomaly by holonomy; cancellation requires a compatible local equivariant trivialization. For effective operators, we give the exact tensor-product line classes of the Yukawa, Weinberg, $`QQQL`$, $`u^cu^cd^ce^c`$, and singlet-Majorana monomials. The two baryon-number violating examples are Standard Model gauge singlets and, in nonsupersymmetric SMEFT, have mass dimension six. They are excluded only if a declared realization supplies an additional bundle, symmetry, cohomology, or overlap obstruction. We prove a sufficient bundle-selection theorem and explain why passing its tests does not guarantee a nonzero coupling. Current Modal Triplet Theory (MTT) has exact finite results for a selected chiral representation, its anomaly table, the faithful $`(SU(3)\times SU(2)\times U(1))/\mathbb{Z}_6`$ group, and a unique anomaly-free shared hypercharge direction within the chosen finite completion. Those results do not yet select the physical compactification endpoint or prove that every dangerous operator is absent. The result is a rigorous realization-by-realization selection framework, not a universal topology-only derivation of the Standard Model.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 02ba3c274b8b0eacf86b79e26a278706bc335a881780a3f04db60be22f5f0c24
paper_id: topology-only-constraints-and-forbidden-operators-in-mo-90db2212
release_state: zenodo_released
released_version: v2
title: |
  **Bundle Selection Rules, Anomaly Lines, and Charge Lattices**
  A Conditional Topological Layer for Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.21713543
zenodo_record_id: 21713543
zenodo_url: "https://zenodo.org/records/21713543"
---

# Version 2 revision note

<div class="description">

Version 1, DOI [`10.5281/zenodo.18261774`](https://doi.org/10.5281/zenodo.18261774).

Version 1 used rational tensor powers of a line bundle without first choosing a root, placed the anomaly line on the wrong base, treated existence of a global section as equivalent to bundle triviality, and suggested that Standard Model gauge topology removes operators that are already Standard Model gauge singlets.

Version 2 separates character lattices, global gauge-group descent, determinant-line anomalies, internal Picard classes, coefficient spaces, and actual overlap pairings. Every displayed operator now has an explicit class and a stated decision rule.

The useful core survives: topology can provide exact, pre-dynamical obstructions inside a fixed realization, and those obstructions are valuable early consistency and falsifiability tests.

MTT has not yet selected the physical bundle endpoint and coefficient functional that would decide all proton-decay and lepton-number-violating operators. Its current exact finite gauge and anomaly results are recorded without promoting them to a no-knob compactification theorem.

</div>

# What a topology-only claim must contain

The phrase “forbidden by topology” sounds stronger than it usually is. It can mean at least four different things:

1.  a proposed field is not a representation of the global gauge group;

2.  a family of chiral fermions has an uncancelled local or global anomaly;

3.  an internal bundle product has no allowed coefficient or invariant pairing;

4.  a particular overlap integral vanishes.

These statements live on different spaces and require different proofs. A charge is a representation label. An anomaly is a property of a quantum fermion theory over its background-field space. An internal selection rule is a statement about bundles and mode spaces on a compactification or overlap base. A vanishing coefficient is a statement about a specific multilinear functional. Conflating them makes an argument look shorter, but also makes its conclusion undecidable.

## The typed realization record

Let $`X`$ denote the internal or overlap space relevant to a proposed four-dimensional realization. It need not be physical space and it is not identified with a spatial slice. Let
``` math
G=\frac{SU(3)\times SU(2)\times U(1)}{\Gamma}
```
be the declared global gauge group, where $`\Gamma`$ is a specified central subgroup. For every four-dimensional field label $`f`$, a usable record contains:
``` math
\bigl(R_f,n_f,\mathcal{L}_f,V_f,\nabla_f\bigr).
```
Here $`R_f`$ is the nonabelian representation, $`n_f\in\mathbb{Z}`$ is the normalized $`U(1)`$ character, $`\mathcal{L}_f\to X`$ is the internal line or more general bundle factor, $`V_f`$ is the selected zero-mode space, and $`\nabla_f`$ is the connection when holonomy or parallel transport matters.

For a monomial
``` math
\mathcal{O}=\prod_{a=1}^{r} f_a,
```
define
``` math
\begin{align}
R_{\mathcal{O}}&=\bigotimes_{a=1}^{r}R_{f_a},&
n_{\mathcal{O}}&=\sum_{a=1}^{r}n_{f_a},&
\mathcal{L}_{\mathcal{O}}&=\bigotimes_{a=1}^{r}\mathcal{L}_{f_a}.
\label{eq:operator-data}
\end{align}
```
Dual or conjugate fields contribute the dual representation, opposite character, and dual line bundle.

<div id="def:completion" class="definition">

**Definition 1** (Operator completion record). An operator completion record consists of the data in <a href="#eq:operator-data" data-reference-type="eqref" data-reference="eq:operator-data">[eq:operator-data]</a>, an allowed coefficient space
``` math
\mathcal{C}_{\mathcal{O}}\subseteq
\Gamma\!\left(X,\mathcal{L}_{\mathcal{O}}^{*}\right),
```
a $`G`$-invariant contraction of the nonabelian representations, and a multilinear functional
``` math
\mu_{\mathcal{O}}:
\mathcal{C}_{\mathcal{O}}\otimes V_{f_1}\otimes\cdots\otimes V_{f_r}
\longrightarrow \mathbb{C}.
```
The four-dimensional coefficient is the value of $`\mu_{\mathcal{O}}`$ on the selected coefficient and zero modes.

</div>

This definition accommodates several familiar cases. A constant scalar coefficient corresponds to a chosen trivialization of $`\mathcal{L}_{\mathcal{O}}`$. A holomorphic compactification may instead use a section of $`\mathcal{L}_{\mathcal{O}}^{*}`$ and a cohomological cup product. A Kaluza–Klein reduction may use an integral of mode representatives. A discrete symmetry can set $`\mathcal{C}_{\mathcal{O}}=0`$. The final scalar cannot be inferred from the symbol $`\mathcal{L}_{\mathcal{O}}`$ alone.

## Four distinctions that prevent false selection rules

<div id="prop:distinctions" class="proposition">

**Proposition 2** (Section, trivialization, and connection). *Let $`\mathcal{L}\to X`$ be a complex line bundle.*

1.  *A nowhere-zero global section trivializes $`\mathcal{L}`$, but an arbitrary global section may have zeros and need not trivialize it.*

2.  *If $`c_1(\mathcal{L})\ne0`$, then $`\mathcal{L}`$ is not topologically trivial. The converse can fail when torsion or flat Picard data are present.*

3.  *A flat connection can have nontrivial holonomy.*

4.  *A trivial line bundle can carry a connection with nonzero curvature.*

*A nonzero global parallel section exists exactly when the connection has trivial holonomy; such a section supplies a connection-preserving trivialization.*

</div>

<div class="proof">

*Proof.* The first statement follows by using a nowhere-zero section as a global frame. The Chern class obstructs a topological trivialization, but does not classify every line bundle on every space. Flatness sets the curvature to zero but leaves a representation of $`\pi_1(X)`$ as holonomy. Conversely, on the trivial line, $`d+iA`$ has curvature $`i\,dA`$, which need not vanish. Parallel transport of a nonzero vector produces a path-independent global parallel section exactly when all holonomies fix it; for a line this means trivial holonomy. ◻

</div>

<div class="remark">

*Remark 3*. Version 1 repeatedly moved between these notions. In the revised argument, “topologically trivial,” “flat,” “trivial holonomy,” and “equipped with a selected trivialization” are never synonyms.

</div>

# Charge lattices and what they do not select

## Integer characters come first

The continuous characters of $`U(1)`$ are
``` math
\chi_n(z)=z^n,\qquad n\in\mathbb{Z}.
```
Thus a principal $`U(1)`$ bundle $`P_Y`$ and its weight-one associated line $`K`$ generate the charged lines
``` math
K_n=P_Y\times_{\chi_n}\mathbb{C}\cong K^{\otimes n},
\qquad
c_1(K_n)=n\,c_1(K).
```
There is no canonical rational tensor power $`K^{\otimes q}`$. Writing a rational physical hypercharge $`Y=n/N`$ presupposes a normalization $`N`$, or equivalently a primitive line whose integer weight is $`n`$. If one starts from a nonprimitive line and wants an $`N`$-th root, existence of that root is additional global data.

<div id="thm:charge-lattice" class="theorem">

**Theorem 4** (Fixed-group charge lattice). *Fix a compact global gauge group
``` math
G=(G_{\mathrm{ss}}\times U(1))/\Gamma
```
with finite central $`\Gamma`$. Every finite-dimensional representation of $`G`$ pulls back to a representation of $`G_{\mathrm{ss}}\times U(1)`$ with integer $`U(1)`$ character $`n`$. It descends to $`G`$ exactly when the combined action of every element of $`\Gamma`$ is trivial. Consequently the allowed labels form an integer lattice with congruence conditions. After a normalization $`Y=n/N`$, they form a rational lattice. This determines allowed representation labels, not which labels occur in nature.*

</div>

<div class="proof">

*Proof.* Every continuous character of $`U(1)`$ is $`\chi_n`$ for a unique $`n\in\mathbb{Z}`$. A representation of the quotient is precisely a representation of the covering product on which the quotient subgroup $`\Gamma`$ acts trivially. The descent condition is therefore a finite set of congruences relating $`n`$ to the central characters of $`G_{\mathrm{ss}}`$. Selecting a matter spectrum is extra data: the representation ring contains many allowed elements. ◻

</div>

For the conventional left-handed Standard Model labels, the useful integer normalization is $`n=6Y`$:

<div id="tab:sm-labels">

| field | $`Q`$ | $`u^c`$ | $`d^c`$ | $`L`$ | $`e^c`$ | $`N^c`$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $`SU(3)\times SU(2)`$ | $`(\mathbf3,\mathbf2)`$ | $`(\bar{\mathbf3},\mathbf1)`$ | $`(\bar{\mathbf3},\mathbf1)`$ | $`(\mathbf1,\mathbf2)`$ | $`(\mathbf1,\mathbf1)`$ | $`(\mathbf1,\mathbf1)`$ |
| $`6Y`$ | $`1`$ | $`-4`$ | $`2`$ | $`-3`$ | $`6`$ | $`0`$ |

Conventional one-family labels. These are an example to be reproduced, not a consequence of the abstract lattice theorem.

</div>

The global form of the gauge group matters. Different quotients of groups with the same Lie algebra can impose different descent conditions . This is why “integral cohomology quantizes hypercharge” is incomplete: one must name the primitive character, the global group, its quotient, and the field representations.

# Anomalies live over background-field space

## The determinant line has a different base

Let $`\mathcal{B}`$ be a space of gauge and metric backgrounds and let $`\mathcal{G}`$ be the relevant gauge group. A chiral fermion representation defines a family of chiral Dirac operators
``` math
D_b^+:\Gamma(S^+\otimes E_b)\longrightarrow
\Gamma(S^-\otimes E_b),
\qquad b\in\mathcal{B}.
```
Its determinant line is the family-index line
``` math
\operatorname{Det}D^+\longrightarrow \mathcal{B}
\quad\text{or, equivariantly, over }\mathcal{B}/\mathcal{G}.
```
It is not the ordinary top exterior power $`\det E_b`$ of the matter bundle over spacetime. The Bismut–Freed connection on this family line has a curvature determined by the local index density, while its holonomy detects global anomaly information .

<div id="thm:anomaly" class="theorem">

**Theorem 5** (Scoped anomaly criterion). *For a declared family of chiral Dirac operators, a nonzero equivariant curvature of the determinant or Pfaffian line is a local anomaly obstruction, and nontrivial equivariant holonomy of a flat anomaly line is a global anomaly obstruction. Anomaly cancellation on that domain requires a local, gauge-compatible trivialization of the anomaly theory; in the determinant-line model this includes vanishing curvature and holonomy after all allowed counterterms and inflow contributions are included.*

</div>

<div class="proof">

*Proof.* The fermionic functional integral is naturally a section of the determinant or Pfaffian line. A gauge-compatible scalar partition function requires a compatible trivialization. Curvature obstructs local flatness and encodes the perturbative anomaly. If curvature vanishes, nontrivial holonomy still prevents a single-valued gauge-compatible section around loops in background-field space. Conversely, a compatible local equivariant trivialization converts the section into a scalar functional on the stated domain. The locality qualifier is essential: an arbitrary nonlocal trivialization is not an admissible counterterm. ◻

</div>

## The conventional one-family arithmetic

The representation labels in <a href="#tab:sm-labels" data-reference-type="ref+label" data-reference="tab:sm-labels">1</a> satisfy the familiar four-dimensional anomaly equations. Omitting common positive normalization factors,
``` math
\begin{align}
\mathcal A_{SU(3)^2Y}
 &=2Y_Q+Y_{u^c}+Y_{d^c}=0,\\
\mathcal A_{SU(2)^2Y}
 &=3Y_Q+Y_L=0,\\
\mathcal A_{\mathrm{grav}^2Y}
 &=6Y_Q+3Y_{u^c}+3Y_{d^c}+2Y_L+Y_{e^c}=0,\\
\mathcal A_{Y^3}
 &=6Y_Q^3+3Y_{u^c}^3+3Y_{d^c}^3+2Y_L^3+Y_{e^c}^3=0.
\end{align}
```
The color cubic anomaly cancels between two triplet components of $`Q`$ and the two antitriplets $`u^c,d^c`$. The number of weak doublets per family, counting color, is $`3+1=4`$, so the Witten $`SU(2)`$ global anomaly also cancels. These equations verify a chosen representation. They do not by themselves derive that representation or its multiplicity.

# Exact operator classes and selection rules

## Field lines

Attach internal line bundles
``` math
\mathcal{L}_Q,\ \mathcal{L}_u,\ \mathcal{L}_d,\ \mathcal{L}_L,\ \mathcal{L}_e,\
\mathcal{L}_N,\ \mathcal{L}_H
\quad\text{in }\operatorname{Pic}(X)
```
to the left-handed fields in <a href="#tab:sm-labels" data-reference-type="ref+label" data-reference="tab:sm-labels">1</a> and to a Higgs doublet $`H`$ with $`6Y_H=3`$. Write
``` math
\ell_f=[\mathcal{L}_f]\in\operatorname{Pic}(X)
```
additively. Complex conjugation contributes $`-\ell_f`$. The following table now makes every claim checkable.

<div class="tabularx">

@lcccY@ monomial & 4D dimension & $`6Y`$ sum & internal Picard class & exact additional test
$`QHu^c`$ & $`4`$ & $`1+3-4=0`$ & $`\ell_Q+\ell_H+\ell_u`$ & An $`SU(3)\times SU(2)`$ singlet exists. A constant Yukawa needs a selected trivialization; a geometric Yukawa needs a nonzero allowed overlap functional.
$`QH^\dagger d^c`$ & $`4`$ & $`1-3+2=0`$ & $`\ell_Q-\ell_H+\ell_d`$ & Same distinction between a trivial line and a nonzero overlap coefficient.
$`LH^\dagger e^c`$ & $`4`$ & $`-3-3+6=0`$ & $`\ell_L-\ell_H+\ell_e`$ & Gauge neutrality does not determine the charged-lepton Yukawa matrix.
$`(LH)(LH)`$ & $`5`$ & $`2(-3+3)=0`$ & $`2\ell_L+2\ell_H`$ & The Weinberg coefficient lies in the dual line and a symmetric flavor pairing; it is not decided by a bare “real structure” statement.
$`QQQL`$ & $`6`$ & $`3(1)-3=0`$ & $`3\ell_Q+\ell_L`$ & It is already an SM gauge singlet. Exclusion requires this extra class, an additional symmetry, a vanishing cohomology group, or a zero overlap functional.
$`u^cu^cd^ce^c`$ & $`6`$ & $`2(-4)+2+6=0`$ & $`2\ell_u+\ell_d+\ell_e`$ & It is also an SM gauge singlet. The same realization-specific certificate is required.
$`N^cN^c`$ & $`3`$ & $`0`$ & $`2\ell_N`$ & A bare Majorana mass needs an allowed invariant symmetric bilinear or a coefficient section of $`\mathcal{L}_N^{-2}`$.

</div>

In nonsupersymmetric SMEFT, $`QQQL`$ and $`u^cu^cd^ce^c`$ are four-fermion operators of mass dimension six . In supersymmetric language, analogous four-chiral-superfield superpotential monomials are often called dimension-five proton-decay operators after the superspace measure and effective suppression are accounted for. The framework must state which convention it uses.

## The selection theorem

<div id="thm:selection" class="theorem">

**Theorem 6** (Typed bundle-selection rule). *Fix an operator completion record as in <a href="#def:completion" data-reference-type="ref+label" data-reference="def:completion">1</a>. The operator $`\mathcal{O}`$ is absent on the declared realization if any one of the following holds:*

1.  *$`\operatorname{Inv}_G(R_{\mathcal{O}})=0`$;*

2.  *the allowed coefficient space $`\mathcal{C}_{\mathcal{O}}`$ is zero;*

3.  *every allowed invariant multilinear functional $`\mu_{\mathcal{O}}`$ vanishes on the selected zero-mode spaces.*

*If coefficients are restricted to constants, nontriviality of $`\mathcal{L}_{\mathcal{O}}`$ is a sufficient obstruction. In particular, $`c_1(\mathcal{L}_{\mathcal{O}})\ne0`$ is a sufficient certificate in that restricted constant-coefficient setting. Passing all of these tests is necessary for a nonzero coupling but does not guarantee one.*

</div>

<div class="proof">

*Proof.* Without a $`G`$-invariant contraction, the monomial cannot be a gauge scalar. Without an allowed dual coefficient, its internal bundle factor cannot be paired into a scalar. If every allowed multilinear functional vanishes, dimensional reduction emits zero coefficient. For a constant coefficient, pairing requires a selected trivialization of $`\mathcal{L}_{\mathcal{O}}`$; a nontrivial line has none. A nonzero first Chern class certifies nontriviality. Conversely, a gauge singlet with a trivial total line can still have zero coefficient because its zero-mode product, symmetry selection rule, or overlap integral vanishes. ◻

</div>

<div id="cor:proton" class="corollary">

**Corollary 7** (What must be shown for the two proton-decay examples). *Topology removes $`QQQL`$ or $`u^cu^cd^ce^c`$ from a chosen realization only after that realization proves, respectively,
``` math
3\ell_Q+\ell_L\ne0,
\qquad
2\ell_u+\ell_d+\ell_e\ne0,
```
in the relevant Picard or differential-cohomology group under a constant-coefficient rule, or supplies an equivalent vanishing certificate for the allowed coefficient space or overlap functional.*

</div>

<div class="remark">

*Remark 8*. This is weaker than Version 1 rhetorically and stronger mathematically. It does not announce proton stability from generic overlap language. It tells a calculation exactly what class or functional must be emitted before that claim can be made. Concrete heterotic line-bundle models illustrate this model-by-model logic: additional $`U(1)`$ symmetries can forbid particular operators, but the allowed spectrum is explicitly computed for each bundle choice .

</div>

# Majorana terms: the precise condition

A “real structure” is one sufficient route to a Majorana pairing, but it is not the most precise universal criterion. Let $`E`$ be the gauge and internal bundle carried by a left-handed Weyl field. A bare mass requires a gauge-invariant symmetric bilinear in the internal/flavor labels compatible with the antisymmetric spinor contraction. Equivalently, the relevant singlet must occur in the correct symmetry component of $`E\otimes E`$, and its coefficient bundle must be allowed. A real representation often provides such a bilinear; a pseudoreal representation may require multiple flavors. A complex charged representation generally does not allow a bare Majorana term without symmetry breaking or an additional field.

For a sterile $`N^c`$, the internal line condition is the last row of <a href="#tab:operators" data-reference-type="ref+label" data-reference="tab:operators">[tab:operators]</a>. For active Standard Model neutrinos, the leading gauge-invariant route is the dimension-five Weinberg operator $`(LH)(LH)`$ . The exact internal class is
``` math
2\ell_L+2\ell_H.
```
If the operator is absent at one level, higher-dimensional operators, symmetry-breaking insertions, or a different completion can still generate a Majorana mass. Therefore failure of a bare real structure does not imply that every neutrino mass must be Dirac.

# What current MTT has actually established

The current corpus is stronger than the abstract Version 1 picture in some finite directions and weaker in the physical compactification direction. The distinction is important enough to state row by row.

<div class="tabularx">

@P0.19P0.18Y@ object & current tier & statement
Typed family carrier (A46) & derived exact; vacuum selector open & A 48-state family-diagonal chiral representation emits the $`Q,u^c,d^c,
L,e^c,N^c`$ rows and exactly verifies the local and global anomaly table.
Native gauge group (A47) & derived exact & The selected rank-$`1,2,3`$ finite carriers have native $`U(1),SU(2),SU(3)`$ automorphisms, and the diagonal center kernel is $`\mathbb{Z}_6`$. The faithful group is $`(SU(3)\times SU(2)\times U(1))/\mathbb{Z}_6`$.
Shared hypercharge line (A50) & derived exact; profile tier & Within the chosen finite completion, the abelian anomaly equations have the unique primitive null vector that yields $`6Y=(1,-4,2,-3,6,0)`$. This adds no continuous knob, but it is a low-energy finite-profile theorem.
$`E_6`$ $`Q_\psi`$ color anomaly (A22) & derived exact; strong-CP map open & Three matter families contribute $`+12`$, complete-$`\mathbf{27}`$ exotics contribute $`-12`$, and the selected trace cancels. The axion-current threshold map remains a separate obligation.
Embedded renormalized-SM equivalence (A04) & closed at declared profile standard & The twelve-obligation baseline is closed at one shared physical primitive and measured-profile standard. This is not zero-knob prediction.
Strict no-knob upgrade (A05) & open, $`2/9`$ closed & Physical source selection, remaining values, and stronger prediction claims are not supplied by the topology-only layer.

</div>

The exact finite results are reproducible in the curated MTT calculation repository and summarized in the current typed Standard Model compatibility and noncommutative-geometry papers . They improve the charge and anomaly part of the old paper substantially. They do not yet provide the operator-specific internal classes in <a href="#tab:operators" data-reference-type="ref+label" data-reference="tab:operators">[tab:operators]</a> on a selected physical visible–hidden compactification. In particular, no current theorem may replace the two conditions in <a href="#cor:proton" data-reference-type="ref+label" data-reference="cor:proton">7</a> by the word “generic.”

# Falsifiability after the correction

The revised framework produces sharp tests, but each test is conditional on a declared realization.

1.  **Global-group descent.** If a claimed field representation fails the $`\Gamma`$-descent condition, the realization is inconsistent.

2.  **Anomaly line.** If the complete fermion and inflow content leaves nonzero anomaly curvature or holonomy, the quantum gauge theory is inconsistent on that domain.

3.  **Operator certificate.** If a paper claims that an operator is absent, it must publish $`R_{\mathcal{O}},n_{\mathcal{O}},\mathcal{L}_{\mathcal{O}},\mathcal{C}_{\mathcal{O}},V_f,\mu_{\mathcal{O}}`$ or an equivalent complete certificate. A nonzero observed coefficient contradicts that declared certificate.

4.  **Charge selection.** An allowed charge lattice is not a prediction of the observed assignment. A predictive claim must also identify the selection theorem that chooses the observed primitive vector and matter multiplicities.

5.  **Held-out consequence.** Selection data used to construct a model cannot count again as a prediction. A physical claim requires an observable not used to choose the bundles, representations, or coefficient functional.

An observed proton-decay channel would therefore falsify an MTT realization that had already certified the corresponding operator as absent. It would not, by itself, falsify the abstract idea that some other overlap realizations possess topological selection rules. This distinction turns a broad slogan into a testable scientific statement.

# Version 2 changes and reasons

<div class="tabularx">

@P0.28YY@ Version 1 statement & Version 2 decision & Reason
Rational charges use $`L_Y^{\otimes q}`$. & Replace by integer characters $`K^{\otimes n}`$, quotient descent, and an explicit normalization $`Y=n/N`$. & Rational tensor powers are not defined without root data.
Integral cohomology selects hypercharge. & Narrow to an allowed charge lattice; record the separate A50 finite selection theorem. & A lattice does not select a spectrum or normalization by itself.
The anomaly line is $`\det\mathcal E\to\Sigma`$. & Replace by $`\operatorname{Det}D^+\to\mathcal{B}/\mathcal{G}`$ with curvature, holonomy, locality, counterterm, and inflow data. & The fermionic anomaly is a family-index object over background-field space.
An operator is allowed iff its bundle has a global section. & Replace by the completion record and <a href="#thm:selection" data-reference-type="ref+label" data-reference="thm:selection">6</a>. & A section may vanish; nontrivial bundles may have sections; a coupling requires an invariant scalar functional.
$`QQQL`$ and $`u^cu^cd^ce^c`$ are leading dimension-five operators forbidden by overlap topology. & Correct to nonsupersymmetric dimension six, show both are SM gauge singlets, and state their exact extra Picard classes. & Their exclusion is realization-specific, not a consequence of SM hypercharge.
Majorana mass requires a real structure. & Use the invariant symmetric bilinear and coefficient-space criterion; keep real structure as one sufficient route. & Representation type, flavor multiplicity, Higgs insertions, and higher operators all matter.
Topology-only results explain proton stability universally. & Withdraw. & Current MTT has not emitted the two physical operator-class certificates.

</div>

# Conclusion

Topology is most useful here as a compiler of exact obstructions. Once a global gauge group and a physical bundle realization are fixed, it can say that a representation does not descend, an anomaly line cannot be trivialized, or an operator has no allowed coefficient or overlap functional. Those are strong, pre-dynamical conclusions.

Topology cannot, without additional source data, choose the observed matter spectrum, make every dangerous Standard Model gauge singlet disappear, or turn a vanishing first Chern class into a nonzero coupling. Version 2 makes that boundary explicit. The present MTT finite carrier already supplies an exact $`\mathbb{Z}_6`$ global group, a chiral anomaly table, and a unique anomaly-free normalized hypercharge vector inside its chosen completion. The next physical theorem is now concrete: emit the selected internal classes and coefficient functionals for the operator rows in <a href="#tab:operators" data-reference-type="ref+label" data-reference="tab:operators">[tab:operators]</a> on the same compactification branch. Until then, the paper provides a rigorous conditional selection language and an auditable completion contract.
