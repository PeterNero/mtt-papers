---
abstract: |
  We isolate the part of the proto-spinor construction that is mathematically forced after its geometric premises are stated. A world-in-world field is a section of $`\operatorname{Hom}(TP,TI)`$ for oriented rank-three bundles; its nine local components do not multiply manifold dimensions. If closure data must retain the nontrivial loop class in $`SO(3)`$, the faithful continuous double-cover carrier is spinorial and is represented through $`\operatorname{Spin}(3)\cong SU(2)`$. This is a conditional lifting theorem, not a derivation of internal dimension three or of physical fermions from admissibility alone. For the selected q79 degree-three spectral cover we record the exact trace split of ranks $`1+2`$, the common $`1+2+3`$ carrier, and the local binary-dihedral lift of signed sheet monodromy. The shared circle is now a specified pullback of one universal flat $`\mathbb Z_{64}`$ differential line, not merely an isomorphic fiber. Its determinant, CLN, root-plane, and finite-Hessian actions intertwine exactly. The BHT and Hori fiber transforms share one orthogonal complex structure $`J_{\rm FM}`$, and the binary sheet group has exactly two conjugate $`\pm i`$ phase-root lifts for which $`(\pm iJ_{\rm FM})^2=I`$. Strict global Spin closure remains equivalent to a branch-relator obstruction calculation; the closed result is SpinC and finite symbolic. Circle, lens, and nil remain typed phase, finite-transport, and anchoring roles. Lorentzian spinors, masses, and particle assignments remain downstream realization problems.
author:
- Peter Nero
current_version: v7
date: July 2026 Version 7
generated_from_main_tex_sha256: 7c68851cd2e7e3e17fccc3865ad0135bcb7d9790960ed66d9f7dae6b7ab69ff9
paper_id: the-proto-spinor-conditional-spinorial-closure-and-the-973217d8
release_state: zenodo_released
released_version: v7
title: |
  The Proto-Spinor:
  Conditional Spinorial Closure and the q79 Interface
zenodo_doi: 10.5281/zenodo.21655396
zenodo_record_id: 21655396
zenodo_url: "https://zenodo.org/records/21655396"
---

# Revision note for version 7

Supersedes.
*The Proto-Spinor: Conditional Spinorial Closure and the q79 Interface*, version 6.

Reason.
Version 6 contains the current finite SpinC and shared-line results, but the relation between loop memory, the double cover, the q79 finite return, and a physical fermion remained too easy to compress into one claim.

Resolution.
Version 7 adds a four-layer reading guide, the explicit $`2\pi/4\pi`$ loop-memory picture, and a one-line derivation of the two conjugate finite returns. It keeps strict global Spin, continuum HYM intertwining, Lorentzian dynamics, and particle interpretation as separate gates and changes no theorem tier.

Retained result.
The conditional double-cover theorem, universal flat shared line, finite Hessian naturality, and binary SpinC–Fourier return are retained unchanged.

Remaining boundary.
Strict global q79 Spin, the nonflat FM/HYM lift, the strain-to-q79 continuum intertwiner, and a physical Lorentzian particle/action completion remain open.

# Revision note for version 6

Supersedes.
*The Proto-Spinor: Conditional Spinorial Closure and the q79 Interface*, version 5.

Reason.
Version 5 stopped at a local $`\operatorname{Dic}_3`$ lift and an untyped shared line. It did not include the later universal differential-line pullback, the common BHT–Hori Clifford operator, or the exact binary SpinC return.

Resolution.
Version 6 retains the conditional double-cover theorem and adds the flat q79 shared-line theorem, finite Hessian naturality, the exact $`J_{\rm FM}^2=-I`$ polarization, and the two conjugate $`\pm i`$ phase-root lifts.

Retained result.
Spinorial lifting is necessary when an oriented rank-three carrier must retain the nontrivial $`SO(3)`$ loop class.

Remaining boundary.
Strict global q79 Spin, the physical nonflat FM/HYM lift, the strain-to-q79 continuum intertwiner, and a Lorentzian particle/action completion remain open gates.

# How to Read the Proto-Spinor

The construction has four layers, and the word “proto” is meant to keep them apart.

1.  A local comparison field is a linear map between two oriented rank-three bundles. Its $`3\times3`$ matrix contains orientation and strain components.

2.  Requiring the state carrier to remember the nontrivial loop in the orientation group replaces $`SO(3)`$ by its double cover $`\operatorname{Spin}(3)\cong SU(2)`$.

3.  The selected q79 finite geometry supplies a separate rank-$`1+2+3`$ carrier, a shared flat differential line, signed sheet monodromy, and an exact finite SpinC–Fourier return.

4.  A physical fermion requires a Lorentzian spinor bundle, Dirac dynamics, statistics, interactions, observables, and a particle interpretation.

The first three layers provide a mathematically controlled precursor to spinorial physics. They do not silently supply the fourth.

## Object picture: why a double cover appears

Consider a continuous path of spatial frames describing one full $`2\pi`$ rotation. Its endpoint in $`SO(3)`$ is the identity, but the path is not contractible. When lifted to $`\operatorname{Spin}(3)`$, that path begins at $`+1`$ and ends at $`-1`$. Repeating the rotation produces a lifted path ending at $`+1`$. An ordinary vector representation sees only the $`SO(3)`$ endpoint and cannot distinguish the two loop classes; a spinorial carrier retains the sign.

This is the exact content of “loop memory” in the theorem below. It does not say that a physical object literally rotates through an extra coordinate, and it does not derive Fermi statistics or a Dirac equation. It says that the smallest connected faithful carrier for this homotopy information is the double cover.

## The finite double return in one line

The q79 Fourier operator satisfies $`J_{\rm FM}^2=-I`$. The two admissible shared-line roots contribute scalar phases $`+i`$ or $`-i`$, whose squares are also $`-1`$. Therefore
``` math
(\pm iJ_{\rm FM})^2=(-1)(-I)=I.
```
This is the finite SpinC–Fourier return. The two signs are complex-conjugate lifts of the same determinant structure. The theorem does not choose one as the observed branch and does not identify the compact phase with time.

## Argument map

Sections 2–4 construct the local comparison carrier and its conditional spin lift. Sections 5–8 build the selected q79 rank flag, shared line, binary sheet lift, and Clifford return. Sections 9–12 then type the CLN roles and state the physical, continuum-intertwiner, and numerical-program boundaries. The conclusion should be read as a ledger of which square is closed at the finite level and which arrows still require continuum or Lorentzian data.

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

The rank-two complex fiber is therefore not a two-component particle model by declaration. It is the smallest representation in which the lifted central sign can act nontrivially. Only after the bundle is connected to Lorentzian geometry and an action can its sections be interpreted as physical spinor fields.

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

The labels $`1`$, $`2`$, and $`3`$ refer to ranks of nested algebraic roles: the central unit line, the trace-zero complement, and the full cover algebra. Their sum gives a six-dimensional fiber carrier. They are not three particle families, three spatial manifolds, or a count of quark colors unless a later source map proves such an identification.

# Universal shared differential line

Let $`\mathcal L_{64}^{\rm univ}\to B_\nabla\mathbb Z_{64}`$ be the universal flat line for the primitive character $`\chi_1(n)=\exp(2\pi\mathrm i n/64)`$. The unique nontrivial homomorphism
``` math
h_{S_3}:S_3\longrightarrow\mathbb Z_{64},
 \qquad h_{S_3}(\sigma)=32\,\epsilon(\sigma),
```
sends even permutations to zero and odd permutations to $`32`$. Pulling $`\mathcal L_{64}^{\rm univ}`$ back along the q79 sheet classifying map gives $`(L_{\rm sh},\nabla_{\rm sh})`$. For both admissible odd roots $`r\in\{1,33\}`$,
``` math
\chi_r\circ h_{S_3}=\operatorname{sgn}.
```
Hence $`L_{\rm sh}`$ and the SpinC determinant sign line are canonically parallel-isomorphic. This equality preserves connection and holonomy; it is stronger than recognizing the same order-two phase pattern.

<div class="theorem">

**Theorem 7** (Shared-line finite naturality). *The line $`L_{\rm sh}`$ tensors the trace/trace-zero/full carrier and acts by scalar holonomy. It therefore commutes with all three lane projectors, the root-plane quarter-turn $`J_{DE}`$, and the normalized finite Hessian
``` math
H_{\rm fin}=\kappa_{\rm fin}(I-P_{\rm Haar}),
 \qquad P_{\rm Haar}=\frac1{6}\sum_{g\in S_3}\rho(g).
```
On the selected two-copy sheet/edge representation,
``` math
\operatorname{rank}P_{\rm Haar}=2,
 \quad
 \operatorname{spec}(H_{\rm fin}/\kappa_{\rm fin})
 =\{0^{\times2},1^{\times4}\},
 \quad H_{\rm TT}=\kappa_{\rm fin}I_2.
```
Thus the determinant, CLN, root-plane, and finite-Hessian occurrences are coherent pullbacks of one differential line, with no new fit parameter.*

</div>

<div class="proof">

*Proof.* The determinant statement is the displayed character identity. Scalar holonomy commutes with every sheet operator. Haar averaging is an orthogonal projector, and direct decomposition of the selected representation gives the rank and spectrum. Tensoring by $`L_{\rm sh}`$ preserves all identities. ◻

</div>

This theorem is flat and finite-symbol exact. The full physical HYM carrier has nonzero characteristic curvature and cannot literally have this flat connection. Its promotion requires a spectral-symbol functor and a parallel continuum Hessian comparison.

# Signed sheet monodromy and its lift

For a permutation $`\sigma\in S_3`$, let $`P_\sigma`$ be its permutation matrix and define
``` math
\rho_+(\sigma)=\operatorname{sgn}(\sigma)P_\sigma.
```
Since $`\det(\operatorname{sgn}(\sigma)P_\sigma)=1`$, this is a representation $`S_3\to SO(3)`$.

<div class="theorem">

**Theorem 8** (Local binary-dihedral lift). *The inverse image of $`\rho_+(S_3)`$ in $`\operatorname{Spin}(3)`$ is the binary-dihedral group $`\operatorname{Dic}_3`$ of order twelve. Lifts $`q_1,q_2`$ of adjacent transpositions may be chosen so that
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

# Clifford polarization and exact SpinC return

On the oriented two-circle exterior algebra with basis $`(1,p,q,pq)`$, the Poincare-kernel transform is the integral operator
``` math
J_{\rm FM}=
 \begin{pmatrix}
 0&0&0&-1\\
 0&0&-1&0\\
 0&1&0&0\\
 1&0&0&0
 \end{pmatrix}.
```
Direct multiplication gives
``` math
J_{\rm FM}^{T}J_{\rm FM}=I,
 \qquad \det J_{\rm FM}=1,
 \qquad J_{\rm FM}^{2}=-I.
```
Thus $`J_{\rm FM}`$ is an orthogonal complex structure, equivalently one $`\mathrm{Cl}_{0,1}`$ generator, and
``` math
P_\pm=\frac12(I\mp\mathrm iJ_{\rm FM})
```
are complementary complex rank-two polarizations. The same derived operator reproduces the selected BHT and two-circle Hori fiber transforms.

The half-turn character of $`S_3`$ cannot itself cancel $`J_{\rm FM}^{2}`$: an involution maps to $`0`$ or $`32`$ in $`\mathbb Z_{64}`$, while the square roots of $`32`$ are $`16`$ and $`48`$. The correct domain is the binary sheet group $`\operatorname{Dic}_3`$ already obtained above.

<div class="theorem">

**Theorem 9** (Binary-sheet SpinC–Fourier return). *There are exactly two homomorphisms
``` math
\widetilde h_\pm:\operatorname{Dic}_3\longrightarrow\mathbb Z_{64}
```
which send the binary central element to $`32`$ and the two braid generators to $`(16,16)`$ or $`(48,48)`$. Under either odd character these phases are $`+i`$ and $`-i`$, respectively. In the Fourier frame the binary transposition lift is $`J_{\rm FM}`$, and therefore
``` math
U_\pm=\pm\mathrm iJ_{\rm FM},
 \qquad U_\pm^2=I.
```
The two lifts are complex conjugates with the same determinant sign line. No continuous or discrete fitted parameter is introduced.*

</div>

<div class="proof">

*Proof.* The binary relations force both generator images to be equal square roots of $`32`$; exhaustive solution in $`\mathbb Z_{64}`$ leaves only $`16`$ and $`48`$. The real spinor representation identifies the binary transposition with $`J_{\rm FM}`$. Multiplication then gives $`(\pm\mathrm iJ_{\rm FM})^2=I`$. ◻

</div>

This closes the double return at representation and flat differential-line tier. It does not identify compact phase with physical time, choose one of the conjugate orientations as the observed universe, or supply the nonflat physical FM/HYM correspondence.

The role of SpinC is precise here. The spin lift contributes a central minus sign and the shared $`U(1)`$ root contributes the compensating phase, so the combined finite operator returns exactly. A strict Spin theorem would have to make the spin part close without that $`U(1)`$ compensation on every global relator. This is why the finite return is a genuine result without resolving the separate $`w_2`$ obstruction.

# Circle, lens, and nil as typed carrier roles

In this revision the three labels have the following nonexhaustive roles:

Circle.
The common line $`L_{\rm shared}`$ stores phase or holonomy data. It is counted once and is not physical time.

Lens.
Finite quotient, signed-sheet, or projective transport data. This does not require the global compactification to contain a literal lens-space factor.

Nil.
Anchoring, upper-triangular transport, or termination data in a selected operator filtration. This does not prove a literal Nil$`_3`$ factor.

Thus circle–lens–nil is a carrier and obstruction taxonomy. The auxiliary model $`L(3,1)\times\mathrm{Nil}_3`$ may realize some roles, but it is not the selected q79 Fu–Yau compactification and the two manifolds are not identified.

Boothby–Wang geometry gives a precise supporting model for this typing. A prequantum circle bundle over $`\mathbb{CP}^1`$ with first Chern number $`k`$ has total space $`L(k,1)`$, while an integral circle bundle over $`T^2`$ has a Heisenberg nilmanifold as total space. Thus $`L(3,1)`$ and Nil$`_3`$ are parallel circle-bundle realizations over different bases and curvature classes, not nested spaces . Their curved connections are not the flat q79 root-stack connection. All three may map to the universal classifier $`BU(1)_\nabla`$, but an MTT identification requires selected classifying maps and coherent comparison data.

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

Until these clauses are proved, the local and q79 objects are related by a dimension-matched conditional bridge, not an identity. The universal-line and finite SpinC/Fourier theorems above close important internal squares on the q79 side; they do not supply this world-in-world-to-continuum map.

# Relation to the numerical SM program

The current calculation repositories close embedded renormalized-Standard- Model equivalence at the declared one-shared-physical-primitive/profile standard, including the finite matrix, charged Yukawa profile, electroweak, threshold, and precision transport packets. Those are valid at their stated certificate tier. They do not prove that the proto-spinor carrier uniquely selects the measured profile, and they do not close the strict no-knob or unique-observed-branch upgrade. This paper therefore uses the calculations as downstream realization evidence, not as a proof of its upstream premises.

# Conclusion

The corrected proto-spinor result is narrower and stronger. Under explicit rank-three orientation and loop-memory premises, the double cover is indeed spinorial. The selected q79 carrier has an exact $`1+2+3`$ trace split and an exact universal flat differential line, an exact $`\operatorname{Dic}_3`$ lift, and an exact SpinC–Fourier return on its finite carrier. What remains is sharply separated: the strict global Spin obstruction calculation, the physical nonflat FM/HYM lift, the same-source local-to-q79 continuum intertwiner, and the Lorentzian action/particle completion.

#### Rows used directly in this paper.

- (*derived exact*).

  E6 Qpsi matter/exotic QCD anomaly cancellation audit.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

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

- (*derived exact*).

  Exact-branch internal TT support certificate; physical normalization remains open.

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

The selected q=79, finite-matrix, anomaly, and HYM rows provide the concrete lower structures used at the proto-spinor interface. They do not prove the supplied Lorentzian, SpinC, worldsheet, or physical-bundle hypotheses. Other Standard Model rows are corpus context, and the strict source upgrade remains open.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A22/e6_qpsi_qcd_anomaly` (**DERIVED_EXACT**): E6 Qpsi matter/exotic QCD anomaly cancellation audit.
- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A11/q79_exact_audit` (**DERIVED_EXACT**): Executable q=79 exact-branch audit.
- `A11/q79_exact_theorem` (**DERIVED_EXACT**): CRT q=79 theorem on the selected exact branch.
- `A01/qutrit_weyl_27_matrix` (**DERIVED_EXACT**): Sparse 27x27 qutrit-Weyl left-action realization.

## Corpus-state cross-checks

- `A01/charged_yukawa_higgs_profile` (**PROFILE_REPLAY**): Versioned Yu, Yd, Ye and lambda_H profile packet.
- `A14/ckm_prediction_profile` (**NUMERIC_CERTIFIED**): Three selected CKM profile rows and uncertainty comparison.
- `A01/current_global_lock` (**PROFILE_REPLAY**): Current non-looping global status and source-certificate map.
- `A01/direct_k_higgs_row` (**DERIVED_EXACT**): Promoted direct K_threshold.Omega_H.lambda row.
- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): Twelve-obligation embedded renormalized-SM equivalence audit.
- `A13/gr_tt_support` (**DERIVED_EXACT**): Exact-branch internal TT support certificate; physical normalization remains open.
- `A40/neutral_two_primitive_profile` (**PROFILE_REPLAY**): Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.
- `A02/precision_15_source_transport` (**PROFILE_REPLAY**): Fifteen measured source coordinates, Jacobian and covariance transport.
- `A02/precision_8x8_workspace` (**PROFILE_REPLAY**): Eight-coordinate SMDR output with positive-definite 8x8 covariance.
- `A01/strict_pew_row` (**DERIVED_EXACT**): Promoted P_EW source row at the declared one-shared-primitive standard.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

9 H. B. Lawson and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press, 1989.

J.-X. Fu and S.-T. Yau, *The theory of superstring with flux on non-Kahler manifolds and the complex Monge–Ampere equation*, J. Differential Geom. 78 (2008).

P. Nero, *Selected q79 Trace-Split CLN Carrier and World-in-World Bridge*, internal theorem packet, 2026.

W. M. Boothby and H. C. Wang, *On contact manifolds*, Ann. Math. 68 (1958), 721–734.

R. Casals, D. M. Pancholi, and F. Presas, *Contact blow-up*, Expo. Math. 33 (2015), 97–123.

P. Nero, *q79 Universal Shared Differential Line and Finite-Operator Intertwiner*, executable theorem packet, 2026.

P. Nero, *q79 Binary-Sheet FM Shared Root and SpinC Return*, executable theorem packet, 2026.

</div>
