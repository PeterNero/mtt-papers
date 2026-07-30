---
abstract: |
  Topology-only obstructions are separated from representation checks and from physical source theorems. Chiral multiplicity is an index on the compact internal six-manifold $`X_6`$, not on physical spacetime. For an $`SU(r)`$ bundle $`E\to X_6`$, the spin-Dirac index is $`\operatorname{ind}D_E^+=\frac12\int_{X_6}c_3(E)`$. The current q79 branch constructs smooth non-pullback bundles with $`\int c_3=\pm6`$, and therefore index $`\pm3`$, but its holomorphic gerbe lift, balanced Hermitian–Yang–Mills connection, and differential Bianchi representative remain open. Abelian charges are integer characters: a field of integer charge $`n`$ is valued in $`L^{\otimes n}`$ and its physical convention is $`Y=n/N_0`$. A linear difference-charge construction is only a reconstruction after observed charge differences are inserted. A separate finite-branch theorem is stronger: on the selected chiral carrier, anomaly constraints select the primitive relative-charge vector $`6Y=(1,-4,2,-3,6,0)`$ and the faithful gauge group $`(SU(3)\times SU(2)\times U(1))/\mathbb{Z}_6`$. We prove the resulting anomaly checks, the correct character criterion for a bare Majorana bilinear, the distinction between topological, holomorphic, equivariant, flat, and holonomy trivializations, the conditional common-principal-symbol result for photon and graviton cones, and the correctly normalized one-loop beta coefficients. Peccei–Quinn dynamics, particular baryon/lepton operator exclusions, physical family realization, and neutrino ontology remain conditional or open at the precisely stated gates.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: c86a09f3efdacf32eedeb34cbf979cb0a8e510ca1ebd23838f50c0bf3861562e
paper_id: topology-only-constraints-in-modal-triplet-theory-mtt-i-20d0edb2
release_state: zenodo_released
released_version: v2
title: |
  Topological Consistency Conditions in Modal Triplet Theory:
  Internal Indices, Charge Lattices, and Holonomy
zenodo_doi: 10.5281/zenodo.21666014
zenodo_record_id: 21666014
zenodo_url: "https://zenodo.org/records/21666014"
---

# Version 2 Revision Note

<div class="description">

*Topology–Only Constraints in Modal Triplet Theory (MTT): Indices, Anomalies, and Line–Bundle Triviality*, version 1.

Version 1 placed the family index on physical $`Y_4`$, treated inserted hypercharges as a prediction, confused ordinary line-bundle triviality with gauge-equivariant triviality and trivial holonomy, and promoted several conditional Standard Model checks to topology-only predictions.

Version 2 types the physical and internal bases separately, replaces fractional line-bundle powers by integer characters, corrects the Majorana and renormalization-group formulas, and incorporates the current q79 and finite Standard Model theorem packets at their declared scope.

Index theory, Chern-class obstructions, anomaly sums, tensor-product holonomy, and principal-symbol comparisons remain useful exact tools when their displayed hypotheses hold.

Topology does not by itself select the physical compactification, gauge connection, low-energy representation, coupling values, PQ current, operator coefficients, or Lorentzian action.

</div>

# Logical levels and geometric types

We use three claim levels throughout.

1.  *Mathematical identity or obstruction*: a theorem about declared manifolds, bundles, connections, or representations.

2.  *Selected-branch theorem*: an exact or certified result inside a named current MTT packet, with all of that packet’s premises retained.

3.  *Physical realization*: a theorem that the selected branch supplies the fields, action, state, normalization, and reduction used by observation.

An L1 result is not automatically L2, and an L2 result is not automatically L3. In particular, a topological existence theorem for a bundle does not select a holomorphic structure or a physical gauge vacuum.

Let $`M_4`$ denote physical Lorentzian spacetime and let $`X_6`$ denote a compact internal six-manifold. A ten-dimensional reduction, when used, is based on an appropriate fibration or local product with these two typed factors; no claim below identifies $`M_4`$ with $`X_6`$. Let $`E\to X_6`$ be an internal complex gauge bundle. Its internal Dirac or Dolbeault index can count net four-dimensional chiral zero modes after the reduction hypotheses are supplied.

For an effective $`U(1)`$ factor over $`M_4`$, let $`P_Y\to M_4`$ be the principal bundle and
``` math
L_Y=P_Y\times_{\chi_1}\mathbb{C},
 \qquad \chi_n(e^{i\vartheta})=e^{in\vartheta},\quad n\in\mathbb{Z}.
```
A field with integer character $`n`$ is valued in $`L_Y^{\otimes n}`$, in addition to its spin and nonabelian bundles. Fractional tensor powers are not used.

Pairwise MTT lines $`L_{ij}`$ may live on an internal or effective base, but the base must be stated. The same symbol must not be used to move an index from $`X_6`$ to $`M_4`$.

# The family index belongs to the internal space

<div id="thm:internal-index" class="theorem">

**Theorem 1** (Twisted spin-Dirac index in six dimensions). *Let $`X_6`$ be a closed spin six-manifold and let $`E\to X_6`$ be a complex vector bundle. Then
``` math
\operatorname{ind}D_E^+
 =\left\langle \widehat A(TX_6)\operatorname{ch}(E),[X_6]\right\rangle.
```
If $`c_1(E)=0`$, then
``` math
\begin{equation}
 \operatorname{ind}D_E^+=\frac12\int_{X_6}c_3(E).
 \label{eq:su-index}
\end{equation}
```
The sign assigned to particles rather than conjugate particles is a chirality convention; the magnitude is convention-independent.*

</div>

<div class="proof">

*Proof.* The first formula is the Atiyah–Singer index theorem . In degree six,
``` math
\widehat A=1-\frac1{24}p_1+\cdots,
 \qquad
 \operatorname{ch}_1(E)=c_1(E),
 \qquad
 \operatorname{ch}_3(E)=\frac16
 (c_1^3-3c_1c_2+3c_3).
```
Only $`\operatorname{ch}_3-(p_1/24)\operatorname{ch}_1`$ contributes. When $`c_1(E)=0`$, this is $`c_3(E)/2`$. ◻

</div>

On a compact complex threefold with a holomorphic bundle, the corresponding Dolbeault statement is
``` math
\chi(X_6,E)=\int_{X_6}\operatorname{Td}(TX_6)\operatorname{ch}(E).
```
The analytic zero-mode interpretation additionally requires the relevant complex, connection, and reduction hypotheses. This is the established heterotic logic: net generations are an internal Dirac index, not a Dirac index of physical spacetime .

<div id="cor:q79-index" class="corollary">

**Corollary 2** (Exact q79 smooth index candidate). *On the current q79 rank-one Fu–Yau topology, the shared-circle clutching construction gives smooth non-pullback $`SU(3)`$ bundles $`E_g`$ with
``` math
\int_{X_6}c_3(E_g)=2k,\qquad k=+3\ \hbox{or}\ -3.
```
Whenever the spin-Dirac operator is formed on this smooth data, $`\operatorname{ind}D_{E_g}^+=+3`$ or $`-3`$.*

</div>

<div class="proof">

*Proof.* The q79 clutching theorem computes $`\int c_3(E_g)=2k`$ from the winding of $`g:P_\delta\to SU(3)`$ along the shared circle . Equation <a href="#eq:su-index" data-reference-type="eqref" data-reference="eq:su-index">[eq:su-index]</a> gives the index. ◻

</div>

<div class="remark">

*Remark 3* (What Corollary <a href="#cor:q79-index" data-reference-type="ref" data-reference="cor:q79-index">2</a> does not yet prove). The K3-pullback visible bundle has $`c_3=0`$ and zero net chiral index, even though a K3 cohomology calculation produces three slots and three conjugate slots. The non-pullback smooth construction repairs the topological index but does not yet furnish the selected holomorphic inverse-gerbe transform, balanced Hermitian–Yang–Mills connection, or differential Bianchi identity. The integral gerbe restriction is now proved zero, but a flat holomorphic class $`\beta_C`$ and the subsequent analytic promotion remain open . Thus “index three exists” is established at L1; “the selected q79 physical vacuum has three net families” remains an L3 target.

</div>

The executable current chiral packet $`\mathbb{C}^3_{\rm family}\otimes\mathcal H_{16}`$ is a separate L2 result. It closes the finite representation and anomaly table once that selected family carrier is adopted. It does not replace the analytic promotion just listed.

# Integer charge lattices and the hypercharge question

<div id="prop:charge-lattice" class="proposition">

**Proposition 4** (Characters, line powers, and physical normalization). *The character group of $`U(1)`$ is $`\mathbb{Z}`$. If $`L_Y`$ is the line associated with its primitive character, every associated one-dimensional representation is $`L_Y^{\otimes n}`$ for a unique $`n\in\mathbb{Z}`$. A physical hypercharge convention has the form
``` math
\begin{equation}
 Y=\frac{n}{N_0},
 \label{eq:charge-normalization}
\end{equation}
```
where $`N_0>0`$ specifies the normalization. Topology quantizes $`n`$; it does not by itself determine the gauge coupling or a conventional unit $`N_0`$.*

</div>

<div class="proof">

*Proof.* Continuous homomorphisms $`U(1)\to U(1)`$ are $`e^{i\vartheta}\mapsto e^{in\vartheta}`$ with $`n\in\mathbb{Z}`$. Associated-line tensor products add character integers. ◻

</div>

## The former difference-charge result

Let $`Y_{ij}=y_i-y_j`$ and fix $`y_1+y_2+y_3=0`$. If one inserts
``` math
y_1-y_2=\frac16,\qquad
 y_1-y_3=\frac23,\qquad
 y_3-y_2=-\frac12,
```
then linear algebra gives
``` math
(y_1,y_2,y_3)=\left(\frac5{18},\frac19,-\frac7{18}\right).
```
This is an exact coordinate reconstruction of the three inserted differences. It neither derives those differences nor determines the remaining matter rows without extra identifications. Version 1’s “unique exact SM hypercharges” theorem is therefore withdrawn as a prediction.

## A stronger current finite-branch theorem

The current finite Standard Model packet supplies a different argument that was not available to version 1.

<div id="thm:selected-hypercharge" class="theorem">

**Theorem 5** (Selected relative hypercharge direction). *Assume the selected finite chiral carrier with left-handed rows $`(Q,u^c,d^c,L,e^c,N^c)`$ and the three abelian sheet phases $`(\alpha,\mu,\nu)`$. Assume their integer row charges are
``` math
\begin{align*}
 n_Q&=-\mu,& n_{u^c}&=\mu-\alpha,&
 n_{d^c}&=\alpha+\mu,\\
 n_L&=-\alpha,& n_{e^c}&=2\alpha,&
 n_{N^c}&=\alpha-\nu.
\end{align*}
```
The $`SU(2)^2U(1)`$ and gravitational-$`U(1)`$ anomaly equations are
``` math
\alpha+3\mu=0,\qquad \alpha-\nu=0.
```
Their integer kernel is one-dimensional and has primitive generator $`(\alpha,\mu,\nu)=(3,-1,3)`$. It emits
``` math
\begin{equation}
 (n_Q,n_{u^c},n_{d^c},n_L,n_{e^c},n_{N^c})
 =(1,-4,2,-3,6,0).
 \label{eq:integer-hypercharge}
\end{equation}
```
In the convention $`N_0=6`$, this is the Standard Model relative hypercharge vector
``` math
6Y=(1,-4,2,-3,6,0).
```*

</div>

<div class="proof">

*Proof.* The two displayed equations have rational nullspace generated by $`(3,-1,3)`$. Its entries have greatest common divisor one, so it is the primitive integer generator up to an overall sign. Substitution gives Equation <a href="#eq:integer-hypercharge" data-reference-type="eqref" data-reference="eq:integer-hypercharge">[eq:integer-hypercharge]</a>. The cubic anomaly polynomial on this sheet family factorizes as
``` math
6\alpha^2(\alpha+3\mu)+(\alpha-\nu)^3,
```
and therefore vanishes on the same line. This is the exact calculation in the selected neutral-summand theorem . ◻

</div>

This theorem selects relative integer charges inside the supplied finite edge structure. It is not a topology-only consequence of $`c_1(L)`$, and the choice $`N_0=6`$ states the conventional physical normalization. On the same carrier, the selected native bundle automorphisms give the local group $`SU(3)\times SU(2)\times U(1)`$, and center enumeration gives the faithful form
``` math
\begin{equation}
 G_{\rm SM}=\frac{SU(3)\times SU(2)\times U(1)}{\mathbb{Z}_6}.
 \label{eq:global-sm-group}
\end{equation}
```
This is an exact L2 theorem for the selected carrier, not a consequence of the old difference-potential equations .

# Local and global anomaly checks

Use left-handed Weyl fields throughout. With the integer charges in Equation <a href="#eq:integer-hypercharge" data-reference-type="eqref" data-reference="eq:integer-hypercharge">[eq:integer-hypercharge]</a>, one family has
``` math
Q:(\mathbf{3},\mathbf{2})_1,\quad
 u^c:(\overline{\mathbf{3}},\mathbf{1})_{-4},\quad
 d^c:(\overline{\mathbf{3}},\mathbf{1})_2,\quad
 L:(\mathbf{1},\mathbf{2})_{-3},\quad
 e^c:(\mathbf{1},\mathbf{1})_6,\quad
 N^c:(\mathbf{1},\mathbf{1})_0.
```

<div id="thm:anomaly-table" class="theorem">

**Theorem 6** (Anomaly cancellation on the selected rows). *The perturbative gauge and mixed anomaly coefficients vanish on each supplied family:
``` math
\begin{align*}
 SU(3)^3 &: 2-1-1=0,\\
 SU(3)^2U(1) &: \tfrac12\bigl(2(1)-4+2\bigr)=0,\\
 SU(2)^2U(1) &: \tfrac12\bigl(3(1)-3\bigr)=0,\\
 \mathrm{grav}^2U(1) &: 6(1)+3(-4)+3(2)+2(-3)+6=0,\\
 U(1)^3 &: 6(1)^3+3(-4)^3+3(2)^3+2(-3)^3+6^3=0.
\end{align*}
```
The $`SU(2)^3`$ perturbative anomaly vanishes because the doublet is pseudoreal.*

</div>

<div class="proof">

*Proof.* The equations are the traces of one or three gauge generators over the listed left-handed representation, including color and weak multiplicities. The common Dynkin index $`T(\mathbf3)=T(\mathbf2)=1/2`$ is displayed in the mixed nonabelian sums. ◻

</div>

<div id="thm:witten" class="theorem">

**Theorem 7** (Witten parity check for the selected doublets). *For a spin four-dimensional $`SU(2)`$ theory containing only the Standard Model isospin-$`1/2`$ rows, the original Witten obstruction is absent. There are three colored $`Q`$ doublets and one $`L`$ doublet per family, hence $`4`$ per family and $`12`$ on the selected three-family carrier.*

</div>

<div class="proof">

*Proof.* An odd number of left-handed $`SU(2)`$ doublets has the mod-$`2`$ global anomaly . Both $`4`$ and $`12`$ are even. ◻

</div>

Theorems <a href="#thm:anomaly-table" data-reference-type="ref" data-reference="thm:anomaly-table">6</a> and <a href="#thm:witten" data-reference-type="ref" data-reference="thm:witten">7</a> are exact consistency checks on one supplied representation packet. They do not independently select the representation or the number of families. The current A46 packet performs all these checks on the same $`48`$-dimensional chiral carrier ; that consolidation is a genuine advance over the version 1 bookkeeping.

# Bare Majorana masses require an invariant character

<div id="thm:majorana-character" class="theorem">

**Theorem 8** (One-dimensional gauge-character criterion). *Let a left-handed Weyl field $`\psi`$ transform in a one-dimensional character $`\chi`$ of a gauge group $`G`$. A bare bilinear $`m\psi^T C\psi/2+\mathrm{h.c.}`$ is gauge invariant if and only if
``` math
\begin{equation}
 \chi^2=1
 \label{eq:character-square}
\end{equation}
```
as a character of $`G`$, equivalently the bilinear admits a $`G`$-equivariant trivialization. For a continuous $`U(1)`$ character $`n`$, this requires $`n=0`$. For a $`\mathbb{Z}_N`$ character $`k`$, it requires $`2k=0\pmod N`$.*

</div>

<div class="proof">

*Proof.* Under $`g\in G`$, the bilinear acquires the factor $`\chi(g)^2`$. It is invariant for every $`g`$ exactly when Equation <a href="#eq:character-square" data-reference-type="eqref" data-reference="eq:character-square">[eq:character-square]</a> holds. The two special cases follow from their character groups. ◻

</div>

If $`L_\chi`$ is the associated ordinary line bundle, gauge invariance implies $`L_\chi^{\otimes2}`$ is equivariantly trivial and therefore $`2c_1(L_\chi)=0`$. The converse is false: ordinary topological triviality of a particular background bundle does not erase a nontrivial gauge character. Moreover, a scalar of opposite charge, a Higgs insertion, or a higher dimensional Weinberg operator can make an effective Majorana term invariant even when a bare term is forbidden. Version 1’s topological “if and only if” and its conclusion “otherwise neutrinos are Dirac” are withdrawn.

On the current ambient $`\mathbb{Z}_{1344}`$ packet, the exact self-character solutions are $`k=0`$ and $`k=672`$. The selected CP labels are not such characters. The current source emits a Dirac-neutrino channel, but exclusivity of that channel, the absolute mass scale, and a separately admissible Majorana operator remain open .

# Five distinct notions of triviality

For a complex line bundle with connection, the following notions must not be identified.

<div class="center">

| Notion | Condition and meaning |
|:---|:---|
| Smooth topological triviality | $`c_1(L)=0`$; a smooth nowhere-zero section exists. |
| Holomorphic triviality | $`L\cong\mathcal O`$ in the holomorphic category; $`c_1=0`$ alone can leave a nontrivial class in $`\operatorname{Pic}^0`$. |
| Gauge-equivariant triviality | The relevant tensor representation contains the trivial character or singlet. |
| Flatness | The chosen connection has curvature $`F_\nabla=0`$. |
| Trivial holonomy | $`\operatorname{Hol}_\nabla(\gamma)=1`$ for every closed loop; equivalently a global parallel frame exists. |

</div>

Smooth complex line bundles over the manifolds considered here are classified by $`c_1`$, but a smooth trivialization does not select a flat connection, a parallel frame, or a holomorphic trivialization.

## The pairwise tensor product

Suppose line bundles $`B_i`$ on one declared base obey
``` math
\alpha_i=c_1(B_i),\qquad \alpha_1+\alpha_2+\alpha_3=0,
```
and define $`L_{ij}=B_i\otimes B_j`$.

<div id="lem:top-product" class="lemma">

**Lemma 9** (Topological product identity). *The underlying smooth line bundle $`L_{12}\otimes L_{23}\otimes L_{31}`$ is topologically trivial.*

</div>

<div class="proof">

*Proof.* Its first Chern class is
``` math
(\alpha_1+\alpha_2)+(\alpha_2+\alpha_3)+(\alpha_3+\alpha_1)
 =2(\alpha_1+\alpha_2+\alpha_3)=0.
```
Classification of smooth complex line bundles by $`H^2(-,\mathbb{Z})`$ gives the claim. The trivialization exists but is not canonical from this equation alone. ◻

</div>

## Operator selection

<div id="prop:operator-test" class="proposition">

**Proposition 10** (Conditional global operator test). *Let fields $`\Phi_a`$ transform in representations $`R_a`$ and $`U(1)`$ characters $`n_a`$. With no charged spurion, compensator, or additional field insertion, a constant-coefficient monomial can be gauge invariant only if
``` math
\mathbf{1}\subset\bigotimes_a R_a,\qquad \sum_a n_a=0.
```
For line carriers this gives an equivariant trivialization of the total line. A nonzero total first Chern class is a topological obstruction. Vanishing total $`c_1`$ is only an allowance: nonabelian contraction, statistics, locality, holomorphic structure, and the actual coupling functional remain separate.*

</div>

<div class="proof">

*Proof.* A gauge-invariant scalar is an invariant vector in the tensor product representation. $`U(1)`$ characters multiply, so their integers add. The associated invariant line is topologically trivial, proving the obstruction. ◻

</div>

Consequently, $`3c_1(L_{ij})\ne0`$ obstructs a constant trilinear made only from three fields in that one line sector. Lemma <a href="#lem:top-product" data-reference-type="ref" data-reference="lem:top-product">9</a> removes this particular topological obstruction for a $`(12)(23)(31)`$ trilinear, but it does not generate a Yukawa coupling. Nor does the obstruction by itself identify specific baryon- or lepton-number violating Standard Model operators. Those claims require the complete field-to-bundle dictionary and all allowed scalar insertions.

## Holonomy

Equip the $`L_{ij}`$ with unitary connections $`\nabla_{ij}`$ and let $`\nabla_\otimes`$ be their tensor-product connection.

<div id="thm:holonomy" class="theorem">

**Theorem 11** (Exact tensor-product holonomy statement). *For every closed loop $`\gamma`$,
``` math
\operatorname{Hol}_{\nabla_\otimes}(\gamma)
 =\operatorname{Hol}_{\nabla_{12}}(\gamma)
  \operatorname{Hol}_{\nabla_{23}}(\gamma)
  \operatorname{Hol}_{\nabla_{31}}(\gamma).
```
The product equals one for every loop if a connection-preserving trivialization identifies $`\nabla_\otimes`$ with the trivial connection. Topological triviality from Lemma <a href="#lem:top-product" data-reference-type="ref" data-reference="lem:top-product">9</a> alone does not imply this conclusion.*

</div>

<div class="proof">

*Proof.* Parallel transport on a tensor product is the tensor product of the parallel transports. A connection-preserving trivialization gives a global parallel unit section and therefore unit holonomy. For the failure of the converse, take the trivial line over $`S^1`$ with $`\nabla=d+i a\,d\vartheta`$. It has $`c_1=0`$ and $`F_\nabla=0`$, but its holonomy is $`e^{-2\pi i a}`$, which is nontrivial when $`a\notin\mathbb{Z}`$. ◻

</div>

Thus the phase-sum rule is a valid conditional connection theorem, not a consequence of flux balance alone.

# Strong CP and the conditional PQ mechanism

<div id="thm:pq" class="theorem">

**Theorem 12** (Conditional Peccei–Quinn relaxation). *Assume a compact axion $`a/f_a`$, an approximate global shift symmetry, a nonzero QCD anomaly coefficient $`N`$, adequate suppression of explicit PQ-breaking terms, and a QCD effective potential whose physical minimum is at the CP-conserving point. Then the potential depends on
``` math
\theta_{\rm eff}=\theta_{\rm QCD}+N\frac{a}{f_a}
```
and dynamical minimization relaxes $`\theta_{\rm eff}`$ to zero modulo its periodicity.*

</div>

<div class="proof">

*Proof.* The anomalous shift moves the QCD theta angle into the dynamical axion coordinate. Under the stated potential and quality assumptions, minimization selects the CP-conserving class. This is the Peccei–Quinn mechanism . ◻

</div>

The physical domain-wall number counts inequivalent minima after charge normalization and identifications by any unbroken discrete subgroup. It is not universally equal to an unnormalized anomaly sum. The current MTT audit finds that the complete selected $`E_6`$ $`27`$ has zero central $`Q_\psi`$ color anomaly: three matter $`16_1`$ contributions $`+12`$ are canceled by the colored $`10_{-2}`$ partners $`-12`$. A matter-only threshold diagnostic would instead give $`N_{\rm DW}=3`$, not one. No selected flux/threshold axion-current anomaly matching map currently promotes that diagnostic to a physical result . Strong CP therefore remains open in MTT; the conditional Theorem <a href="#thm:pq" data-reference-type="ref" data-reference="thm:pq">12</a> is not a topology-only solution.

# Equal characteristic cones are an action-level theorem

<div id="thm:principal-cone" class="theorem">

**Theorem 13** (Common principal cone). *Assume a Lorentzian metric $`g`$, the two-derivative Einstein–Hilbert action, minimally coupled Maxwell theory, standard gauge fixing, and no Lorentz-violating constitutive or higher-derivative principal terms. The gauge-fixed linearized Maxwell and Einstein operators have principal symbols proportional to
``` math
g^{\mu\nu}\xi_\mu\xi_\nu
```
on their respective field components. Their local geometric-optics characteristic cones therefore coincide.*

</div>

<div class="proof">

*Proof.* In Lorenz gauge the Maxwell operator has principal part $`\Box_g A_\mu`$. In de Donder gauge the linearized Einstein operator has principal part $`\Box_g h_{\mu\nu}`$. Curvature and mass terms are lower order and do not alter the characteristic set. ◻

</div>

This proves the conditional vacuum statement often denoted $`c_{\rm em}=c_{\rm grav}`$. It does not derive the assumed action from topology, nor does it exclude dispersion from additional principal operators.

# Correct one-loop representation coefficients

Fix
``` math
\beta(g)=\mu\frac{dg}{d\mu}
 =-\frac{g^3}{16\pi^2}b_0+O(g^5).
```

<div id="prop:beta" class="proposition">

**Proposition 14** (Weyl/Dirac and real/complex counting). *For a simple gauge factor,
``` math
\begin{equation}
 b_0=\frac{11}{3}C_2(G)
 -\frac{2}{3}\sum_{\text{Weyl }f}T(R_f)
 -\frac{1}{3}\sum_{\text{complex }s}T(R_s).
 \label{eq:beta-correct}
\end{equation}
```
Equivalently, a Dirac fermion contributes $`4T(R)/3`$ and a real scalar contributes $`T(R)/6`$. With three Standard Model families and one complex Higgs doublet,
``` math
b_0^{SU(3)}=7,\qquad
 b_0^{SU(2)}=\frac{19}{6},\qquad
 b_0^{Y}=-\frac{41}{6}.
```
For $`g_1=\sqrt{5/3}\,g_Y`$, the last value is $`b_0^{1}=-41/10`$.*

</div>

<div class="proof">

*Proof.* Equation <a href="#eq:beta-correct" data-reference-type="eqref" data-reference="eq:beta-correct">[eq:beta-correct]</a> is the standard one-loop general-gauge-theory coefficient . Two Weyl fields make one Dirac field, and two real scalars make one complex scalar. For $`SU(3)`$, the Standard Model Weyl sum gives $`b_0=11-4=7`$. For $`SU(2)`$ it gives $`22/3-4-1/6=19/6`$. For physical hypercharge, $`\sum_f Y_f^2=10`$ and the complex Higgs sum is $`1/2`$, giving $`-(2/3)10-(1/3)(1/2)=-41/6`$. ◻

</div>

These signs and coefficients follow from imported perturbative QFT and supplied representations. They are not topology-only MTT predictions. Version 1 used the Dirac coefficient for Weyl fields and half the complex-scalar coefficient; that formula is corrected here.

# Current result ledger

<div class="center">

| Claim | Current status | Exact boundary |
|:---|:---|:---|
| Internal family index | Established L1 | Index is on $`X_6`$; physical zero-mode realization needs the selected analytic compactification. |
| q79 three-index bundle | Topological L1 established | Smooth $`c_3=\pm6`$ bundles exist; holomorphic gerbe/HYM/Bianchi promotion remains open. |
| Difference charges | Encoding only | The old equations reconstruct inserted observed differences. |
| Relative hypercharge vector | Selected L2 established | A50 selects the primitive vector on the supplied finite chiral edge packet; $`N_0`$ states normalization. |
| Gauge group and $`/\mathbb{Z}_6`$ | Selected L2 established | Exact on the native selected carrier; physical compactification promotion is separate. |
| Local and Witten anomalies | Selected L2 established | Exact consistency checks on the supplied rows, not independent selection of them. |
| Dirac/Majorana criterion | Character theorem established | Current packet emits a Dirac channel; exclusivity, absolute scale, and Majorana completion remain open. |
| Operator forbiddance | Conditional obstruction | Nonzero total $`c_1`$ obstructs a constant term; specific B/L claims need the full dictionary and compensator audit. |
| Holonomy phase sum | Conditional connection theorem | Requires a connection-preserving trivialization, not merely $`c_1=0`$. |
| PQ/strong CP | Open physically | Standard PQ theorem is conditional; selected MTT anomalous current and matching map are missing. |
| Photon/graviton cone | Conditional action theorem | Holds for common standard principal symbols; not selected by topology. |
| One-loop RG signs | Imported QFT check | Correct once the Standard Model representation and perturbative action are supplied. |

</div>

# Conclusion

Topology supplies powerful integer obstructions and indices, but it does not perform every physical selection. The strongest corrected result is a clean composition: internal index theory gives the required family-count target; the q79 branch now realizes that target by smooth non-pullback $`c_3=\pm6`$ bundles; the selected finite carrier independently closes the relative hypercharge, global gauge-group, and anomaly algebra. The remaining work is correspondingly sharp: promote the q79 smooth bundle to the selected holomorphic/HYM/Bianchi vacuum and prove that its reduction realizes the same finite carrier and action. PQ dynamics, neutrino ontology, particular operator exclusions, couplings, and propagation laws retain their independent source gates.

# Version 2 delta

- Moved the family index from physical four-space to internal $`X_6`$ and replaced the K3-spacetime example by the six-dimensional $`c_3`$ formula.

- Added the exact q79 smooth $`c_3=\pm6`$ candidate and its explicit analytic promotion boundary.

- Replaced fractional charge bundles by integer powers $`L_Y^{\otimes n}`$ with $`Y=n/N_0`$.

- Reclassified the old hypercharge equations as an inserted-data encoding and added the newer A50 anomaly-kernel theorem as a separate selected result.

- Added the selected native $`G_{\rm SM}/\mathbb{Z}_6`$ theorem and consolidated anomaly table at their finite-carrier scope.

- Replaced ordinary $`L^{\otimes2}`$ topological triviality by the correct gauge-character criterion for bare Majorana masses.

- Separated smooth, holomorphic, equivariant, flat, and holonomy triviality; corrected the phase-sum proof.

- Narrowed operator forbiddance, PQ relaxation, and equal wave speed to their actual conditional hypotheses.

- Corrected one-loop coefficients for Weyl versus Dirac fermions and real versus complex scalars.

- Replaced the claim that all Tier–1 predictions are fully established by the auditable status ledger above.

#### Rows used directly in this paper.

- (*derived exact*).

  E6 Qpsi matter/exotic QCD anomaly cancellation audit.

- (*derived exact*).

  Executable q=79 exact-branch audit.

- (*derived exact*).

  CRT q=79 theorem on the selected exact branch.

- (*derived exact*).

  Sparse 27x27 qutrit-Weyl left-action realization.

= by -

#### Corpus-state cross-checks.

- (*profile replay*).

  Versioned Yu, Yd, Ye and lambda_H profile packet.

- (*numeric certified*).

  Three selected CKM profile rows and uncertainty comparison.

- (*profile replay*).

  Current non-looping global status and source-certificate map.

- (*derived exact*).

  Promoted direct K_threshold.Omega_H.lambda row.

- (*profile replay*).

  Twelve-obligation embedded renormalized-SM equivalence audit.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*profile replay*).

  Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.

- (*profile replay*).

  Fifteen measured source coordinates, Jacobian and covariance transport.

- (*profile replay*).

  Eight-coordinate SMDR output with positive-definite 8x8 covariance.

- (*derived exact*).

  Promoted P_EW source row at the declared one-shared-primitive standard.

= by -

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The q=79 branch, finite representation, and anomaly packets are used directly as topological or representation consistency examples. Gauge, flavor, precision, HYM, and Higgs rows are not topology-only theorems and are included only as lower-sector cross-checks. The strict source upgrade remains open.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A22/e6_qpsi_qcd_anomaly` (**DERIVED_EXACT**): E6 Qpsi matter/exotic QCD anomaly cancellation audit.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.
- `A01/qutrit_weyl_27_matrix` (**DERIVED_EXACT**): Sparse 27x27 qutrit-Weyl left-action realization.

## Corpus-state cross-checks

- `A01/charged_yukawa_higgs_profile` (**PROFILE_REPLAY**): Versioned Yu, Yd, Ye and lambda_H profile packet.
- `A14/ckm_prediction_profile` (**NUMERIC_CERTIFIED**): Three selected CKM profile rows and uncertainty comparison.
- `A01/current_global_lock` (**PROFILE_REPLAY**): Current non-looping global status and source-certificate map.
- `A01/direct_k_higgs_row` (**DERIVED_EXACT**): Promoted direct K_threshold.Omega_H.lambda row.
- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): Twelve-obligation embedded renormalized-SM equivalence audit.
- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A40/neutral_two_primitive_profile` (**PROFILE_REPLAY**): Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.
- `A02/precision_15_source_transport` (**PROFILE_REPLAY**): Fifteen measured source coordinates, Jacobian and covariance transport.
- `A02/precision_8x8_workspace` (**PROFILE_REPLAY**): Eight-coordinate SMDR output with positive-definite 8x8 covariance.
- `A01/strict_pew_row` (**DERIVED_EXACT**): Promoted P_EW source row at the declared one-shared-primitive standard.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

M. F. Atiyah and I. M. Singer, *The index of elliptic operators: I*, Annals of Mathematics **87** (1968), 484–530. <https://doi.org/10.2307/1970715>

P. Candelas, G. T. Horowitz, A. Strominger, and E. Witten, *Vacuum configurations for superstrings*, Nuclear Physics B **258** (1985), 46–74. <https://doi.org/10.1016/0550-3213(85)90602-9>

E. Witten, *An $`SU(2)`$ anomaly*, Physics Letters B **117** (1982), 324–328. <https://doi.org/10.1016/0370-2693(82)90728-6>

M. E. Machacek and M. T. Vaughn, *Two-loop renormalization group equations in a general quantum field theory. I. Wave function renormalization*, Nuclear Physics B **222** (1983), 83–103. <https://doi.org/10.1016/0550-3213(83)90610-7>

R. D. Peccei and H. R. Quinn, *CP conservation in the presence of pseudoparticles*, Physical Review Letters **38** (1977), 1440–1443. <https://doi.org/10.1103/PhysRevLett.38.1440>

J.-X. Fu and S.-T. Yau, *The theory of superstring with flux on non-Kahler manifolds and the complex Monge–Ampere equation*, Journal of Differential Geometry **78** (2009), 369–428. <https://arxiv.org/abs/hep-th/0604063>

P. Nero, *MTT Selected q79 Non-Pullback Chiral Visible Bundle and Full $`SU(9)`$ Holonomy Selection*, theorem packet (2026). <https://github.com/PeterNero/mtt-sm-parity-closure/blob/2d7465f60a9d2a0333a5c32a94311d048aeb435d/proof_corpus/MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1.md>

P. Nero, *MTT Selected q79 Twisted Spectral Gerbe Lift, HYM and Bianchi Execution*, theorem packet (2026). <https://github.com/PeterNero/mtt-sm-parity-closure/blob/2d7465f60a9d2a0333a5c32a94311d048aeb435d/proof_corpus/MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1.md>

P. Nero, *MTT Selected Typed Family–Gauge Carrier and Diagonal SM Representation Theorem*, theorem packet (2026). <https://github.com/PeterNero/mtt-sm-parity-closure/blob/2d7465f60a9d2a0333a5c32a94311d048aeb435d/proof_corpus/MTT_Selected_TypedFamilyGaugeCarrierAndDiagonalSMRepresentationTheorem_v1.md>

P. Nero, *MTT Selected Native Bundle–Automorphism Gauge Group or Parameter–Assumption Audit*, theorem packet (2026). <https://github.com/PeterNero/mtt-sm-parity-closure/blob/2d7465f60a9d2a0333a5c32a94311d048aeb435d/proof_corpus/MTT_Selected_NativeBundleAutomorphismGaugeGroup_or_ParameterAssumptionAudit_v1.md>

P. Nero, *MTT Selected Neutral Algebra Summand or Equivalent Axiom Revision*, theorem packet (2026). <https://github.com/PeterNero/mtt-sm-parity-closure/blob/2d7465f60a9d2a0333a5c32a94311d048aeb435d/proof_corpus/MTT_Selected_NeutralAlgebraSummandOrEquivalentAxiomRevision_v1.md>

P. Nero, *MTT Selected Neutrino and Strong–CP Strict–Upgrade Attack*, theorem packet (2026). <https://github.com/PeterNero/mtt-sm-parity-closure/blob/2d7465f60a9d2a0333a5c32a94311d048aeb435d/proof_corpus/MTT_Selected_NeutrinoAndStrongCP_StrictUpgradeAttack_v1.md>

P. Nero, *MTT Selected $`E_6`$ Central–Generator QCD Anomaly Audit*, theorem packet (2026). <https://github.com/PeterNero/mtt-sm-parity-closure/blob/2d7465f60a9d2a0333a5c32a94311d048aeb435d/proof_corpus/MTT_Selected_E6CentralGeneratorQCDAnomalyAudit_v1.md>

</div>
