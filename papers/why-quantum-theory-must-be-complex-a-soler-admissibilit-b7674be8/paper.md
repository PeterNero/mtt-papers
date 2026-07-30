---
abstract: |
  Solèr’s theorem classifies an orthomodular generalized Hilbert space containing an infinite orthonormal sequence as a real, complex, or quaternionic Hilbert space. This classification does not by itself select the complex field. We add a separate finite-composition requirement: a system of dimension $`d`$ over the selected field has the full self-adjoint matrix space as its unnormalized state/effect space; a composite of dimensions $`a`$ and $`b`$ has dimension $`ab`$ over the same field; and independent product effects are tomographically complete. The resulting dimension identity holds for complex Hermitian matrices and fails, by explicit nonzero defects, for real symmetric and quaternionic Hermitian matrices whenever $`a,b>1`$. Complex Hilbert space is therefore rigid within this declared reconstruction class. The conclusion is conditional and representation-sensitive: complex quantum theory can be realified by adjoining an orthogonal complex-structure operator, and alternative composite rules fall outside the theorem. Applied to MTT, the result identifies exact missing premises rather than deriving them. The current q79 finite quantum model and finite complex polarization are compatible with the complex branch, but MTT has not yet sourced the required infinite orthogonality and standard locally tomographic composition from one physical upper construction.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: July 2026, Version 2
generated_from_main_tex_sha256: bfaca00316201382337cb836ee63eda64fa268d7ce8b8a7ad576e7b73c01376f
paper_id: why-quantum-theory-must-be-complex-a-soler-admissibilit-b7674be8
release_state: zenodo_released
released_version: v2
title: |
  Complex-Hilbert Rigidity under Solèr, Local Tomography,
  and Standard Composition
  A Conditional MTT Reconstruction Theorem
zenodo_doi: 10.5281/zenodo.21666024
zenodo_record_id: 21666024
zenodo_url: "https://zenodo.org/records/21666024"
---

# Version 2 Revision Note

Supersedes
*Why Quantum Theory Must Be Complex: A Solèr–Admissibility Rigidity Theorem in Modal Triplet Theory*, version 1.

Reason
The earlier paper treated a Hilbert reconstruction, infinite orthogonality, local tomography, and phase-rich composition as already derived by MTT. It also attributed to projection alone the exclusion of real and quaternionic alternatives and did not state the composite-system convention on which that exclusion depends.

Resolution
This version separates the imported Solèr classification from an explicit finite-dimensional composition theorem. It declares the full state/effect spaces, standard same-field composite dimensions, local independence, and tomographic completeness, then proves the real, complex, and quaternionic dimension identities directly. It also records realification and alternative-composition boundaries.

Retained result
Under the stated orthomodular, infinite-orthogonality, full-matrix, and standard locally tomographic composition assumptions, the effective Hilbert theory is uniquely complex.

Remaining boundary
MTT has not yet derived the infinite orthogonal sequence, the standard composite rule, or local tomography for all physical contexts from the selected q79 source; its present finite complex model shows compatibility, not independent scalar-field selection.

# The question and the corrected answer

Why does ordinary quantum mechanics use complex Hilbert space rather than real or quaternionic Hilbert space? There are two different questions hidden here.

First, one may ask which scalar division rings are compatible with a sufficiently rich orthomodular quantum logic. Solèr’s theorem answers this under a strong infinite-dimensional hypothesis: the possibilities reduce to
``` math
\mathbb{R},\qquad \mathbb{C},\qquad \mathbb{H}.
```
It does not choose among them.

Second, one may ask which of those theories has the familiar tensor-product parameter count: the state of a composite is determined by joint statistics of independent local measurements. Under the full-matrix and standard-composition convention stated below, a short dimension calculation selects $`\mathbb{C}`$.

The word “under” matters. The result is not a theorem that nature is metaphysically made of complex numbers. A complex Hilbert theory can be rewritten on a real Hilbert space with an additional operator $`J`$ satisfying $`J^2=-I`$. Conversely, real or quaternionic theories can be paired with altered composite rules. The theorem identifies a rigid *package*:
``` math
\begin{gathered}
\text{orthomodular representation}
+\text{ infinite orthogonality}\\
+\text{ standard local composition}\\
\Longrightarrow\text{ complex Hilbert theory}
\end{gathered}
```

This corrected formulation fits the current MTT status. The selected finite q79 quantum model already uses complex Hilbert and operator data, and the finite carrier has an exact complex polarization. What remains open is to derive the assumptions that would make the complex structure unique rather than merely present.

# The generalized Hilbert input

## Orthomodular form

Let $`K`$ be a division ring with involution $`z\mapsto z^*`$. Let $`V`$ be a right vector space over $`K`$, equipped with a nondegenerate Hermitian form
``` math
\langle\cdot,\cdot\rangle:V\times V\longrightarrow K.
```
For a subspace $`M\subseteq V`$, define
``` math
M^\perp=\{v\in V:\langle m,v\rangle=0\text{ for every }m\in M\}.
```
The form is called orthomodular when every orthogonally closed subspace $`M=M^{\perp\perp}`$ satisfies
``` math
V=M+M^\perp.
```
The closed subspaces then form an orthomodular lattice under inclusion, orthogonal complement, intersection, and closed span.

This is not automatic from a list of measurement outcomes. To reach this setting from an operational theory, one must construct:

1.  a proposition lattice;

2.  an orthocomplementation compatible with exclusivity;

3.  a coordinatizing vector space over a division ring with involution;

4.  a nondegenerate Hermitian form; and

5.  orthomodularity of the represented closed subspaces.

These are reconstruction assumptions unless proved by an earlier theorem.

## The infinite-orthogonality gate

Solèr’s theorem requires an infinite orthonormal sequence
``` math
e_1,e_2,\ldots,\qquad
\langle e_j,e_k\rangle=\delta_{jk}.
```
Arbitrarily large finite orthogonal families do not automatically give such a sequence in one completed space. An inductive family of finite systems also does not suffice until compatible embeddings and a completed limit have been constructed.

This distinction is decisive for MTT. The canonical q79 quantum carrier is finite. Its exact finite Hilbert structure cannot, by itself, satisfy the infinite-sequence hypothesis.

# What Solèr’s theorem supplies

Solèr’s classification states that an orthomodular form containing an infinite orthonormal sequence is a Hilbert space over $`\mathbb{R}`$, $`\mathbb{C}`$, or $`\mathbb{H}`$, with the standard involution and norm-complete structure . In implication form,
``` math
\begin{equation}
\begin{gathered}
\text{orthomodular generalized Hilbert representation}\\
+\text{ infinite orthonormal sequence}
\end{gathered}
\quad\Longrightarrow\quad
K\in\{\mathbb{R},\mathbb{C},\mathbb{H}\}.
\label{eq:soler}
\end{equation}
```

Two guardrails follow immediately.

1.  Solèr’s theorem is an imported classification theorem; MTT does not own its proof.

2.  Equation <a href="#eq:soler" data-reference-type="eqref" data-reference="eq:soler">[eq:soler]</a> leaves three scalar possibilities. Any claim of unique complex structure needs an additional premise.

The additional premise used here is a precise composite-system rule.

# Standard composition and local tomography

## State/effect dimensions

For a finite $`d`$-dimensional Hilbert space over $`F\in\{\mathbb{R},\mathbb{C},\mathbb{H}\}`$, let
``` math
\operatorname{Herm}_F(d)
```
denote the real vector space of self-adjoint $`d\times d`$ matrices over $`F`$. Its dimension is the number of real coordinates needed for an unnormalized state, or equivalently for an unrestricted self-adjoint effect:
``` math
\begin{align}
K_{\mathbb{R}}(d)&=\frac{d(d+1)}{2},\label{eq:KR}\\
K_{\mathbb{C}}(d)&=d^2,\label{eq:KC}\\
K_{\mathbb{H}}(d)&=d(2d-1).\label{eq:KH}
\end{align}
```

The counts are elementary. A real symmetric matrix has $`d`$ diagonal and $`d(d-1)/2`$ off-diagonal entries. A complex Hermitian matrix has $`d`$ real diagonal entries and two real coordinates for each off-diagonal pair. A quaternionic Hermitian matrix has $`d`$ real diagonal entries and four real coordinates for each off-diagonal pair.

## Declared composite rule

Consider systems $`A`$ and $`B`$ of dimensions $`a,b>1`$ over the same field $`F`$. The theorem below assumes:

Full local spaces
The unnormalized state/effect spaces are $`\operatorname{Herm}_F(a)`$ and $`\operatorname{Herm}_F(b)`$.

Standard global dimension
The composite is represented on a same-field Hilbert space of dimension $`ab`$, with global space $`\operatorname{Herm}_F(ab)`$.

Independent product effects
The bilinear product of local effects has no additional linear identifications, so it spans a space of dimension $`K_F(a)K_F(b)`$.

Tomographic completeness
Those product effects separate all global states.

The last two conditions together give the dimension identity
``` math
\begin{equation}
K_F(ab)=K_F(a)K_F(b).
\label{eq:local-tomography}
\end{equation}
```
This is the standard locally tomographic tensor-product condition used in operational reconstructions . Local tomography without a declared composite rule is not enough: different theories may change the global space or allow redundancy among products.

<div id="lem:defects" class="lemma">

**Lemma 1** (Exact composition defects). *For $`a,b>1`$,
``` math
\begin{align}
K_{\mathbb{R}}(ab)-K_{\mathbb{R}}(a)K_{\mathbb{R}}(b)
&=\frac{ab(a-1)(b-1)}{4}>0,\label{eq:real-defect}\\
K_{\mathbb{C}}(ab)-K_{\mathbb{C}}(a)K_{\mathbb{C}}(b)
&=0,\label{eq:complex-defect}\\
K_{\mathbb{H}}(ab)-K_{\mathbb{H}}(a)K_{\mathbb{H}}(b)
&=-2ab(a-1)(b-1)<0.\label{eq:quat-defect}
\end{align}
```*

</div>

<div class="proof">

*Proof.* Substitute <a href="#eq:KR" data-reference-type="eqref" data-reference="eq:KR">[eq:KR]</a>–<a href="#eq:KH" data-reference-type="eqref" data-reference="eq:KH">[eq:KH]</a> and factor. For example,
``` math
\frac{ab(ab+1)}2
-\frac{a(a+1)b(b+1)}4
=\frac{ab(a-1)(b-1)}4.
```
The complex equality is immediate: $`(ab)^2=a^2b^2`$. The quaternionic expression factors as
``` math
ab(2ab-1)-ab(2a-1)(2b-1)
=-2ab(a-1)(b-1).
```
 ◻

</div>

#### Interpretation.

For real matrices, the global space contains parameters that independent local products do not reach. For quaternionic matrices, the naive product count is larger than the same-field global count, so independence and that global convention cannot both hold. Only the complex full-matrix family has exact multiplicativity.

<div id="thm:rigidity" class="theorem">

**Theorem 2** (Conditional complex-Hilbert rigidity). *Assume:*

1.  *the effective proposition theory has an orthomodular generalized Hilbert representation with an infinite orthonormal sequence;*

2.  *finite $`d`$-level systems use the full self-adjoint matrix spaces over the scalar field selected by that representation; and*

3.  *every pair of nontrivial systems obeys the standard same-field composite rule with independent, tomographically complete product effects.*

*Then the scalar field is $`\mathbb{C}`$.*

</div>

<div class="proof">

*Proof.* By Solèr’s theorem, assumption 1 restricts the field to $`\mathbb{R},\mathbb{C},\mathbb{H}`$. Assumptions 2 and 3 require <a href="#eq:local-tomography" data-reference-type="eqref" data-reference="eq:local-tomography">[eq:local-tomography]</a>. Lemma <a href="#lem:defects" data-reference-type="ref" data-reference="lem:defects">1</a> excludes $`\mathbb{R}`$ and $`\mathbb{H}`$ for every $`a,b>1`$, while $`\mathbb{C}`$ satisfies the identity. ◻

</div>

# What “complex” means here

## Realification

The scalar label is not representation-invariant by itself. Let $`H_{\mathbb{C}}`$ be a complex Hilbert space. Forget complex scalar multiplication and retain the real Hilbert space $`H_{\mathbb{R}}`$ together with
``` math
J:H_{\mathbb{R}}\longrightarrow H_{\mathbb{R}},
\qquad
J^2=-I,
\qquad
J^*=-J.
```
Multiplication by $`a+ib`$ is represented by $`aI+bJ`$. Complex-linear operators are precisely the real-linear operators commuting with $`J`$. Thus the same complex theory may be written over $`\mathbb{R}`$ if the complex-structure operator and its composition law are retained.

<div id="prop:realification" class="proposition">

**Proposition 3** (Representation guard). *Theorem <a href="#thm:rigidity" data-reference-type="ref" data-reference="thm:rigidity">2</a> selects the complex full-matrix theory with its standard composition class. It does not prove that every faithful presentation must display complex scalar entries.*

</div>

<div class="proof">

*Proof.* The realification above is faithful: it preserves vectors, inner products through their real and $`J`$-dependent parts, and all complex-linear observables through the commutant of $`J`$. What changes is the declared real state/effect space and tensor product: they are restricted by the shared complex structure rather than being the unrestricted real-symmetric theory counted by $`K_{\mathbb{R}}`$. ◻

</div>

## Alternative composites

Real quantum theory can be bilocally rather than locally tomographic . Quaternionic and Jordan-algebraic theories require particular care in defining composites, and natural alternatives need not equal the naive same-field full-matrix rule . Such theories are not refuted by Theorem <a href="#thm:rigidity" data-reference-type="ref" data-reference="thm:rigidity">2</a>; they reject one of its composition premises.

The corrected claim is therefore conditional rigidity, not an unconditional impossibility theorem.

# The MTT interface

## What is already available

Current MTT work supplies two relevant finite results:

1.  the canonical q79 binary one-anchor operational model has an exact finite complex Hilbert space, state cone, observable algebra, reduced semigroup, Fock dilation, and output probability law on its declared domain; and

2.  the selected finite carrier has an exact complex polarization with $`+i`$ and $`-i`$ eigenspaces and a compatible shared-line return structure.

These results establish that complex quantum structure is compatible with, and concretely realized in, the current finite MTT branch. They do not establish the hypotheses of Theorem <a href="#thm:rigidity" data-reference-type="ref" data-reference="thm:rigidity">2</a>.

## What must still be derived

<div class="center">

| Required object | Current status |
|:---|:---|
| Finite q79 Hilbert model | Exact complex model on the canonical binary domain |
| Finite complex polarization | Exact on the declared finite carrier |
| Orthomodular reconstruction | Must be proved for the intended full proposition family |
| Infinite orthonormal sequence | Not supplied by the finite q79 carrier |
| Compatible inductive completion | Open |
| Standard physical composites | Not derived from one selected upper source |
| Local independence | Open for arbitrary physical contexts |
| Tomographic completeness | Open for arbitrary physical contexts |
| Shared $`U(1)`$ source of $`J`$ | Candidate finite evidence; global theorem open |

</div>

The most direct MTT completion would use the shared circle line as more than a repeated phase label. One would need to prove that its connection and holonomy induce one compatible operator $`J`$ on states, observables, instruments, and composites, and that the resulting balanced composition is the one used by the q79 operational theory. That would connect the finite complex polarization to the physical quantum reconstruction without pretending that Solèr’s infinite hypothesis follows from a finite carrier.

# Consequences and non-consequences

Under its assumptions, Theorem <a href="#thm:rigidity" data-reference-type="ref" data-reference="thm:rigidity">2</a> has a clean consequence: no separate “phase-rich interference” argument is required to eliminate real full-matrix quantum theory. The same standard-composition condition excludes both real and quaternionic candidates by exact parameter counts.

The theorem does *not* establish:

- that projection alone produces Hilbert space;

- that every MTT basin is a quantum proposition;

- that the q79 finite model has an infinite orthogonal completion;

- that physical composites must obey the standard tensor-product rule;

- that real or quaternionic mathematical formulations are inconsistent;

- that complex notation is ontologically fundamental; or

- that Born probabilities for arbitrary apparatus contexts follow from scalar-field selection.

It instead converts a vague question into three auditable gates:
``` math
\text{Soler gate},\qquad
\text{composition gate},\qquad
\text{MTT source gate}.
```
The first is established mathematics. The second is proved here after explicit assumptions. The third remains a research obligation.

# Conclusion

Complex Hilbert space is uniquely selected within a well-defined reconstruction class. Solèr’s theorem first reduces an infinite orthomodular generalized Hilbert representation to the real, complex, and quaternionic cases. Standard full-matrix composition with independent and tomographically complete local effects then imposes multiplicativity of the self-adjoint parameter count. The complex count is exactly multiplicative; the real and quaternionic counts have nonzero defects.

This is a meaningful rigidity theorem, but it is conditional. Its assumptions include both an infinite-orthogonality completion and a particular physical composition rule. MTT currently realizes the complex branch in a finite q79 operational model and finite polarization, yet still must derive those stronger assumptions from the selected upper geometry. The right next theorem is therefore not another assertion that quantum theory “must” be complex. It is the source theorem connecting the common MTT phase line to one globally compatible complex structure and composite rule.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The conditional complex-Hilbert reconstruction depends on Soler rigidity, local tomography, and the stated composition assumptions. The open strict-upgrade ledger is unrelated to that proof and is cited solely as a boundary on broader MTT source claims.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
