---
abstract: |
  We isolate the part of the proto-spinor construction that is mathematically forced after its geometric premises are stated. A world-in-world field is a section of $`\operatorname{Hom}(TP,TI)`$ for oriented rank-three bundles; its nine local components do not multiply manifold dimensions. If closure data must retain the nontrivial loop class in $`SO(3)`$, the faithful continuous double-cover carrier is spinorial and is represented through $`\operatorname{Spin}(3)\cong SU(2)`$. This is a conditional lifting theorem, not a derivation of internal dimension three or of physical fermions from admissibility alone. For the selected q79 degree-three spectral cover we record the exact trace split of ranks $`1+2`$, the common $`1+2+3`$ carrier, and the local binary-dihedral lift of signed sheet monodromy. Strict global Spin closure remains equivalent to a branch-relator sign or obstruction-class calculation. Circle, lens, and nil are retained as phase, finite-transport, and anchoring roles, rather than asserted to be an exhaustive literal product topology. Lorentzian spinors, masses, Higgs modes, and particle assignments are downstream realization problems with explicit gates.
author:
- Peter Nero
current_version: v5
date: July 2026
generated_from_main_tex_sha256: 1641742a6db9de7132741b4553e8cbb439f2d6ca71ea06774c9668798ac3bb6a
paper_id: the-proto-spinor-conditional-spinorial-closure-and-the-973217d8
release_state: zenodo_released
released_version: v4.0
title: |
  The Proto-Spinor:  
  Conditional Spinorial Closure and the q79 Interface  
  Corrected fifth edition
zenodo_doi: 10.5281/zenodo.19534666
zenodo_record_id: 19534666
zenodo_url: "https://zenodo.org/records/19534666"
---

# Revision note for this edition

Supersedes.  
*The Proto-Spinor: Triadic Closure from Pointwise Internal Embedding*, version 4.

Reason.  
Rank three, the Spin$`(3)`$ lift, exhaustive circle–lens–nil support, and downstream physical spinor regimes were presented as universally forced rather than conditional on explicit orientation and topology data.

Resolution.  
Version 5 types $`Q_{\rm WW}`$, proves the conditional double-cover theorem, imports the exact q79 trace split and local $`\operatorname{Dic}_3`$ lift, and separates strict Spin from SpinC closure.

Retained result.  
Spinorial lifting is necessary when an oriented rank-three carrier must retain the nontrivial $`SO(3)`$ loop class.

Remaining boundary.  
Strict global q79 Spin, the strain-to-q79 intertwiner, and a Lorentzian particle/action completion remain open gates.

# Status and dependencies

This paper is a conditional carrier theorem. Its conclusions depend on the following data, none of which follows from a bare projection map:

1.  oriented Euclidean rank-three bundles $`TP`$ and $`TI`$ over a declared base $`B`$;

2.  a comparison field $`Q_{\rm WW}\in
    \Gamma(\operatorname{Hom}(TP,TI))`$;

3.  an $`SO(3)`$ frame or holonomy bundle whose nontrivial loop class is to be retained by the state description;

4.  for the q79 specialization, the selected degree-three spectral cover, its trace map, and its sheet monodromy; and

5.  for a physical fermion interpretation, a separate Lorentzian spin or $`\operatorname{Spin}^c`$ completion, action, observable map, and normalization.

The terms “forced” and “necessary” below always mean necessary relative to these premises. They do not mean that MTT has selected the premises uniquely.

# World-in-world comparison data

<div class="definition">

**Definition 1** (Comparison field). Let $`TP,TI\to B`$ be oriented Euclidean vector bundles of rank three. A world-in-world comparison field is
``` math
Q_{\rm WW}\in\Gamma\!\left(\operatorname{Hom}(TP,TI)\right).
```
At $`b\in B`$, choices of oriented orthonormal frames represent $`Q_{\rm WW}(b)`$ by a matrix in $`\operatorname{Mat}(3,\mathbb R)`$.

</div>

<div class="proposition">

**Proposition 2** (Dimension and component bookkeeping). *The total space of $`TI\to B`$ has dimension $`\dim B+3`$. If $`\dim B=3`$, its dimension is six. The number nine is instead the fiber dimension of $`\operatorname{Hom}(TP,TI)`$.*

</div>

<div class="proof">

*Proof.* A rank-$`r`$ vector bundle over a $`d`$-dimensional base is locally $`U\times\mathbb R^r`$ and therefore has total dimension $`d+r`$. Furthermore, $`\operatorname{Hom}(\mathbb R^3,\mathbb R^3)`$ has dimension nine. ◻

</div>

At an invertible, orientation-preserving background, polar decomposition gives $`Q_{\rm WW}=RU`$ with $`R\in SO(3)`$ and $`U`$ symmetric positive definite. Its linearized carrier has the orthogonal Frobenius decomposition
``` math
\operatorname{Mat}(3,\mathbb R)
 =\mathfrak{so}(3)\oplus\operatorname{Sym}(3,\mathbb R),
 \qquad 9=3+6.
```
After a flag is selected, the symmetric part further decomposes as
``` math
\operatorname{Sym}(3,\mathbb R)
 =\mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O,
 \qquad 6=1+2+3,
```
where $`\mathcal D_0`$ is traceless diagonal and $`\mathcal O`$ is symmetric off-diagonal. The latter split depends on the selected flag; only the $`1+5`$ trace/traceless split is invariant under the full orthogonal group.

Consequently
``` math
1+3\times3=(1+3)+(1+2+3)=4+6=10
```
is an exact component identity once an ordering scalar is added. It is not a proof of a ten-dimensional manifold, a $`3+1`$ spacetime, or Lorentzian signature.

# Conditional spinorial lifting theorem

Let $`F^+(TI)\to B`$ be the oriented orthonormal frame bundle. Its structure group is $`SO(3)`$ and
``` math
\pi_1(SO(3))\cong\mathbb Z_2,
 \qquad
 1\longrightarrow\{\pm1\}\longrightarrow
 \operatorname{Spin}(3)\longrightarrow SO(3)\longrightarrow1.
```

<div class="definition">

**Definition 3** (Neutrality with loop memory). A carrier has neutrality with loop memory when its projected $`SO(3)`$ frame returns after a closed orientation loop while its state representation still distinguishes the two homotopy classes of such loops.

</div>

<div class="theorem">

**Theorem 4** (Conditional double-cover necessity). *Suppose a continuous state carrier over the $`SO(3)`$ frame data is required to distinguish the generator of $`\pi_1(SO(3))`$ and to compose consistently under concatenation of lifted paths. Then an ordinary vector representation of $`SO(3)`$ is insufficient. The minimal connected covering group on which the nontrivial class remains visible is the universal double cover $`\operatorname{Spin}(3)\cong SU(2)`$.*

</div>

<div class="proof">

*Proof.* Every $`SO(3)`$ representation identifies a loop with its endpoint group element, so both homotopy classes of loops ending at the identity act as the identity. Path lifting to the universal cover assigns the two classes the endpoints $`+1`$ and $`-1`$. Since $`\pi_1(SO(3))=\mathbb Z_2`$, the universal connected cover is two-sheeted and no smaller connected cover can retain that class. The universal cover is $`\operatorname{Spin}(3)\cong SU(2)`$. ◻

</div>

<div class="definition">

**Definition 5** (Proto-spinor). Relative to the preceding hypotheses, a proto-spinor is a section of an associated complex rank-two bundle
``` math
S_I=P_{\rm Spin}\times_{SU(2)}\mathbb C^2,
```
where $`P_{\rm Spin}`$ is a chosen lift of the relevant oriented frame or holonomy data. The word “proto” records that no Lorentzian Dirac operator, statistics law, or particle ontology has yet been supplied.

</div>

The theorem does not prove that an internal world must be three-dimensional. For example, $`SO(2)`$ already has nontrivial winding, while higher-dimensional orientation groups also possess spin covers. Rank three is a selected realization premise supported here by the comparison carrier and the q79 degree-three data, not a universal dimensional-minimality theorem.

# Selected q79 trace-split carrier

Let $`\pi:C\to B`$ be the selected degree-three spectral cover and set
``` math
\mathcal A=\pi_*\mathcal O_C.
```
The unit and trace define
``` math
p_{\rm cen}=\frac13\,\mathbf1\circ\operatorname{Tr},
 \qquad
 \mathcal A_0=\ker\operatorname{Tr}.
```

<div class="theorem">

**Theorem 6** (Trace-split rank flag). *If $`\mathcal A`$ is finite locally free of rank three and the ground field has characteristic different from three, then
``` math
\mathcal A\cong\mathcal O\oplus\mathcal A_0,
 \qquad
 \operatorname{rank}(\mathcal O,\mathcal A_0,\mathcal A)=(1,2,3).
```
Consequently the shared-line carrier
``` math
\mathcal H_{\rm CLN}
 =L_{\rm shared}\otimes
 (\mathcal O\oplus\mathcal A_0\oplus\mathcal A)
```
has rank six.*

</div>

<div class="proof">

*Proof.* The normalized trace projector is idempotent, has image the unit line, and has kernel $`\mathcal A_0`$. Rank additivity gives $`3=1+2`$, and the displayed direct sum has rank $`1+2+3=6`$. ◻

</div>

This theorem selects a direct trace/trace-zero/full carrier. On a connected cover with transitive monodromy it does not produce a global ordering of three individual sheets.

# Signed sheet monodromy and its lift

For a permutation $`\sigma\in S_3`$, let $`P_\sigma`$ be its permutation matrix and define
``` math
\rho_+(\sigma)=\operatorname{sgn}(\sigma)P_\sigma.
```
Since $`\det(\operatorname{sgn}(\sigma)P_\sigma)=1`$, this is a representation $`S_3\to SO(3)`$.

<div class="theorem">

**Theorem 7** (Local binary-dihedral lift). *The inverse image of $`\rho_+(S_3)`$ in $`\operatorname{Spin}(3)`$ is the binary-dihedral group $`\operatorname{Dic}_3`$ of order twelve. Lifts $`q_1,q_2`$ of adjacent transpositions may be chosen so that
``` math
q_1^2=q_2^2=-1,
 \qquad q_1q_2q_1=q_2q_1q_2,
 \qquad (q_1q_2)^3=-1.
```*

</div>

<div class="proof">

*Proof.* The signed permutation image is the rotational symmetry group of an oriented triangular frame, isomorphic to the dihedral rotation group of order six. The inverse image of a finite rotation group under the two-to-one map $`SU(2)\to SO(3)`$ has twice its order and is its binary counterpart. Standard half-angle quaternion lifts of the two generating rotations satisfy the displayed relations, identifying the inverse image with $`\operatorname{Dic}_3`$. ◻

</div>

## Global obstruction

The preceding theorem is not yet a strict global q79 Spin theorem. Let $`B^\circ`$ be the branch complement and let $`\rho:\pi_1(B^\circ)\to SO(3)`$ be the signed sheet monodromy. A strict lift is a homomorphism $`\widetilde\rho`$ making
``` math
\begin{array}{ccc}
 &\operatorname{Spin}(3)&\\[-2mm]
 &\downarrow&\\[-1mm]
 \pi_1(B^\circ)&\xrightarrow{\rho}&SO(3)
\end{array}
```
commute. It exists exactly when the pulled-back central extension is trivial, equivalently when the relevant $`w_2`$ obstruction vanishes. Computationally, one must lift a presentation of $`\pi_1(B^\circ)`$ and verify that every relator closes with central sign $`+1`$. Local braid relations alone do not decide all global relators.

A shared $`U(1)`$ line can instead participate in a $`\operatorname{Spin}^c`$ cancellation of the mod-two obstruction. That is a distinct theorem and must not be reported as a strict Spin lift.

# Circle, lens, and nil as typed carrier roles

In this revision the three labels have the following nonexhaustive roles:

Circle.  
The common line $`L_{\rm shared}`$ stores phase or holonomy data. It is counted once and is not physical time.

Lens.  
Finite quotient, signed-sheet, or projective transport data. This does not require the global compactification to contain a literal lens-space factor.

Nil.  
Anchoring, upper-triangular transport, or termination data in a selected operator filtration. This does not prove a literal Nil$`_3`$ factor.

Thus circle–lens–nil is a carrier and obstruction taxonomy. The auxiliary model $`L(3,1)\times\mathrm{Nil}_3`$ may realize some roles, but it is not the selected q79 Fu–Yau compactification and the two manifolds are not identified.

# Downstream physical gates

1.  A Lorentzian spinor requires a globally hyperbolic base, a spin or $`\operatorname{Spin}^c`$ structure, a tetrad, a compatible connection, and a hyperbolic Dirac operator.

2.  A particle interpretation requires a physical state space, statistics, observables, interactions, and an asymptotic or local excitation criterion.

3.  A mass is read from a canonically normalized quadratic action or a propagator pole. A positive closure cost alone is not a mass.

4.  A Higgs identification requires a selected scalar representation and couplings. A positive Hessian does not imply a unique scalar mode.

5.  A discrete spectrum requires a self-adjoint operator with compact resolvent, confining boundary conditions, or another explicit spectral compactness theorem. Nil language alone does not quantize a theory.

Weyl, Dirac, Majorana, and twistor descriptions may be built as conditional encodings once their respective chirality, pairing, real-structure, and conformal hypotheses are supplied. They are not consequences of the rank-three comparison field alone.

# The same-source interface theorem still required

The local strain carrier and the q79 trace-split carrier both have dimensions $`1+2+3`$. Rank equality supplies only a fiberwise linear isomorphism. The needed physical theorem must construct
``` math
\mathfrak I_{\rm WW\to q79}:
 \mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O
 \longrightarrow
 L_{\rm shared}\otimes
 (\mathcal O\oplus\mathcal A_0\oplus\mathcal A)
```
on the selected base and prove:

1.  compatibility with transition functions and the selected flag;

2.  isometry for the declared strain and HYM inner products;

3.  covariant compatibility $`\mathfrak I\nabla^{\rm WW}=\nabla^{q79}\mathfrak I`$; and

4.  intertwining of the Hessian, retarded, and overlap operators used by the numerical source packets.

Until these clauses are proved, the local and q79 objects are related by a dimension-matched conditional bridge, not an identity.

# Relation to the numerical SM program

The current calculation repositories close embedded renormalized-Standard- Model equivalence at the declared one-shared-physical-primitive/profile standard, including the finite matrix, charged Yukawa profile, electroweak, threshold, and precision transport packets. Those are valid at their stated certificate tier. They do not prove that the proto-spinor carrier uniquely selects the measured profile, and they do not close the strict no-knob or unique-observed-branch upgrade. This paper therefore uses the calculations as downstream realization evidence, not as a proof of its upstream premises.

# Conclusion

The corrected proto-spinor result is narrower and stronger. Under explicit rank-three orientation and loop-memory premises, the double cover is indeed spinorial. The selected q79 carrier has an exact $`1+2+3`$ trace split and an exact local $`\operatorname{Dic}_3`$ lift. What remains is sharply separated: the global q79 obstruction calculation, the same-source local-to-q79 intertwiner, and the physical Lorentzian/action completion.

<div class="thebibliography">

9 H. B. Lawson and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press, 1989.

J.-X. Fu and S.-T. Yau, *The theory of superstring with flux on non-Kahler manifolds and the complex Monge–Ampere equation*, J. Differential Geom. 78 (2008).

P. Nero, *Selected q79 Trace-Split CLN Carrier and World-in-World Bridge*, internal theorem packet, 2026.

</div>
