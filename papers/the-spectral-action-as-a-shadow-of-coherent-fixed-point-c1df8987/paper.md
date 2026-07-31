---
abstract: |
  This paper asks when the Connes–Chamseddine spectral action may be interpreted as a lower-dimensional encoding of Modal Triplet Theory (MTT). The answer is conditional and can be stated precisely. Given a real even finite spectral triple, a compact four-dimensional Euclidean spin triple, cutoff data, and an intertwining source map from a selected MTT upper complex, the almost-commutative product and its spectral action follow by standard noncommutative geometry. Current MTT calculations supply substantial finite data: a three-family chiral representation with exact anomaly cancellation, the faithful Standard Model gauge group, a necessary neutral algebra summand, an explicit finite Dirac operator at profile tier, and a selected rank-four one-form sector representing one complex Higgs doublet. They do not yet derive the physical entries of the finite Dirac operator, the continuum Euclidean triple, the cutoff function and scale, absolute field normalization, or the renormalization-group transport from one selected upper action. In particular, a spectral gap alone does not determine a cutoff function, and the Standard Model couplings are not presently fixed by one bottleneck vector. The result is therefore a rigorous spectral-action encoding theorem and an explicit source-obligation theorem, not a derivation of the full Standard Model action.
author:
- Peter Nero
current_version: v2
date: July 2026, Version 2
generated_from_main_tex_sha256: 55b231ec665734cffeca194165e41646d642988f7ce5fdc8cae10234932b9287
paper_id: the-spectral-action-as-a-shadow-of-coherent-fixed-point-c1df8987
release_state: zenodo_released
released_version: v2
title: |
  **The Spectral Action as a Conditional Shadow of Coherent Fixed-Point Geometry**
  A source contract between Modal Triplet Theory and almost-commutative geometry
zenodo_doi: 10.5281/zenodo.21718806
zenodo_record_id: 21718806
zenodo_url: "https://zenodo.org/records/21718806"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, released in January 2026.

The original paper promoted assumed overlap and proper-time data to a canonical spectral triple, a unique cutoff, and source-derived Standard Model parameters. Those conclusions did not follow from the stated hypotheses.

This version separates standard spectral-action mathematics, executed finite MTT results, and the open source/descent problem. It proves a conditional descent theorem, gives a counterexample to cutoff uniqueness from a gap, and reports the exact and profile tiers of the current finite calculations.

The spectral action remains a natural candidate for a four-dimensional encoding of coherent fixed-point data, and inner fluctuations remain the correct language for the gauge and scalar sectors once the spectral triple is supplied.

A selected upper differential/action, continuum Euclidean-to-Lorentzian bridge, source-derived finite Dirac entries, cutoff measure, absolute normalization, and quantum/RG transport remain open.

</div>

# Question, answer, and scope

The spectral action packages geometry and matter into operator data. For a spectral triple $`(\mathcal{A},\mathcal{H},D)`$, the bosonic term is a trace of a function of the Dirac operator, while the fermionic term pairs fermions with the fluctuated Dirac operator. In the almost-commutative Standard Model, the continuous spin geometry and a finite noncommutative geometry are combined in one product triple . This economy makes the construction an attractive possible endpoint for an MTT projection.

The important word is *endpoint*. A lower spectral triple does not by itself explain which upper dynamics selected its algebra, representation, Dirac operator, or cutoff data. Conversely, a coherent projector or a spectral gap is not automatically a spectral triple. The purpose of this paper is to identify the exact bridge that would make the “shadow” language mathematical and to report how much of that bridge has actually been built.

Three layers must be kept separate.

1.  **Imported spectral geometry.** Once an almost-commutative real even spectral triple and cutoff data are given, standard spectral-action mathematics produces a bosonic action and fermionic couplings.

2.  **Executed finite MTT encoding.** Current calculations construct and test a particular finite representation, algebra completion, finite Dirac operator at profile tier, and finite one-form sector.

3.  **Open MTT source theorem.** One selected upper action must still emit those lower objects through commuting, connection-preserving maps and must supply their physical numerical values.

This distinction is not a retreat from the original proposal. It turns a broad analogy into a testable research program. The finite calculations tell us that a noncommutative-geometric encoding is compatible with the selected MTT branch. The source theorem would explain why that encoding, with those values, is physically selected.

## Status vocabulary

<div id="def:tiers" class="definition">

**Definition 1** (Claim tiers). In this paper:

1.  *derived exact* means an algebraic or finite computational statement proved from the declared packet without measured Standard Model values;

2.  *profile replay* means that accepted physical parameter values are inserted into a typed operator and the resulting identities or spectra are then checked;

3.  *conditional* means a theorem whose hypotheses include mathematical objects not yet selected by MTT;

4.  *open* means that no accepted source theorem currently emits the required object or value.

</div>

Profile replay is useful: it tests whether the proposed carrier can hold the known theory without contradiction. It is not numerical prediction. Likewise, a conditional theorem can close the logic of a bridge while leaving the existence or selection of its input data open.

# The standard spectral-action contract

## Finite and continuous triples

<div id="def:finite" class="definition">

**Definition 2** (Finite real even spectral data). A finite real even spectral datum is a tuple
``` math
(\mathcal{A}_F,\mathcal{H}_F,D_F,J_F,\gamma_F)
```
where $`\mathcal{A}_F`$ is a finite-dimensional involutive algebra represented on the finite-dimensional Hilbert space $`\mathcal{H}_F`$, $`D_F=D_F^\ast`$, $`J_F`$ is an antilinear real structure, and $`\gamma_F`$ is a grading. The tuple becomes a finite real even spectral triple only after the relevant reality, grading, order-zero, order-one, orientability, and Poincare-duality conditions are verified in the chosen convention.

</div>

<div id="def:base" class="definition">

**Definition 3** (Euclidean base triple). Let $`Y_E`$ be a compact four-dimensional Riemannian spin manifold. Its canonical Euclidean spin triple is
``` math
\bigl(\mathcal{A}_E,\mathcal{H}_E,D_E\bigr)
  =
  \bigl(C^\infty(Y_E),L^2(Y_E,S),\not{D}_{Y_E}\bigr).
```
The compactness, spin structure, Riemannian signature, and domain of $`\not{D}_{Y_E}`$ are part of the input. They are not consequences of a finite internal triple.

</div>

Given Definitions <a href="#def:finite" data-reference-type="ref" data-reference="def:finite">2</a> and <a href="#def:base" data-reference-type="ref" data-reference="def:base">3</a>, the almost-commutative product uses
``` math
\mathcal{A}=\mathcal{A}_E\otimes\mathcal{A}_F,\qquad
 \mathcal{H}=\mathcal{H}_E\otimes\mathcal{H}_F,\qquad
 D=D_E\otimes 1+\gamma_E\otimes D_F.
```
The exact signs and KO-dimension conventions must be fixed consistently. Inner fluctuations of $`D`$ then generate gauge and scalar fields. This is standard noncommutative geometry; it should not be counted as a new MTT derivation.

## Bosonic and fermionic actions

For a suitable positive cutoff profile $`f`$ and scale $`\Lambda>0`$, write
``` math
\begin{equation}
\label{eq:spectral-action}
 S_{\mathrm{bos}}[D_A]
   =\mathop{\mathrm{Tr}}f(D_A^2/\Lambda^2),
\end{equation}
```

where $`D_A`$ is the fluctuated Dirac operator. The fermionic part is represented schematically by
``` math
\begin{equation}
\label{eq:fermionic-action}
 S_{\mathrm{ferm}}[\Psi,D_A]
   =\frac12\langle J\Psi,D_A\Psi\rangle ,
\end{equation}
```

with the physical fermion space and doubling prescription stated separately.

Under the usual ellipticity and regularity assumptions, the large-$`\Lambda`$ expansion of <a href="#eq:spectral-action" data-reference-type="ref+label" data-reference="eq:spectral-action">[eq:spectral-action]</a> has the form
``` math
\begin{equation}
\label{eq:heat}
 \mathop{\mathrm{Tr}}f(D_A^2/\Lambda^2)
 \sim
 \sum_{k\geq 0} F_{4-k}\,\Lambda^{4-k}\,a_k(D_A^2),
\end{equation}
```

where the $`a_k`$ are heat-kernel coefficients and the $`F_j`$ are moments or derivatives of $`f`$, according to convention. The Einstein–Hilbert, cosmological, gauge, scalar kinetic, and scalar potential terms arise from this expansion when the chosen product triple has the required content.

<div id="thm:standard" class="theorem">

**Theorem 4** (Conditional spectral-action output). *Assume the Euclidean base triple, a finite real even spectral triple, a valid almost-commutative product, a fluctuated self-adjoint Dirac operator with the required elliptic regularity, and cutoff data $`(f,\Lambda)`$. Then <a href="#eq:spectral-action,eq:heat" data-reference-type="ref+label" data-reference="eq:spectral-action,eq:heat">[eq:spectral-action,eq:heat]</a> define the bosonic spectral action and its asymptotic local expansion. If the finite representation and finite Dirac operator are those of the Standard Model encoding, the expansion has the corresponding gauge, Higgs, and Yukawa operator content.*

</div>

<div class="proof">

*Proof.* This is the standard heat-kernel consequence of the spectral-action principle applied to the declared product triple . The theorem is conditional because the triple and cutoff data occur among its hypotheses. ◻

</div>

The theorem explains what the spectral action does after its inputs are known. It does not select those inputs, prove that they descend from MTT, or determine the physical renormalized parameters.

# Proper time, spectral gaps, and cutoff nonuniqueness

Version 1 proposed that a coherent proper-time kernel and a spectral gap fix the cutoff function. There is a correct mathematical statement nearby, but the selection claim was too strong.

<div id="prop:proper" class="proposition">

**Proposition 5** (Proper-time representation). *Let $`\mu`$ be a finite positive Borel measure on $`[0,\infty)`$. Then
``` math
f_\mu(x)=\int_0^\infty e^{-\tau x}\,\mathrm{d}\mu(\tau),
  \qquad x\geq 0,
```
is completely monotone. For a positive self-adjoint operator $`D^2`$, whenever the traces and interchange of integrals are justified,
``` math
\mathop{\mathrm{Tr}}f_\mu(D^2/\Lambda^2)
  =
  \int_0^\infty
  \mathop{\mathrm{Tr}}\!\left(e^{-\tau D^2/\Lambda^2}\right)\mathrm{d}\mu(\tau).
```*

</div>

<div class="proof">

*Proof.* Differentiation under the integral gives $`(-1)^n f_\mu^{(n)}(x)=\int \tau^n e^{-\tau x}\mathrm{d}\mu(\tau)\geq0`$. The trace identity follows from the functional calculus and Tonelli’s theorem under the stated finiteness assumptions. ◻

</div>

<div id="prop:no-gap" class="proposition">

**Proposition 6** (A gap does not select the cutoff). *Knowledge of a positive spectral gap or of a lower proper-time support bound $`\tau_0>0`$ does not determine the cutoff profile.*

</div>

<div class="proof">

*Proof.* The two positive measures
``` math
\mu_1=\delta_{\tau_0},
  \qquad
  \mu_2=\tfrac12\delta_{\tau_0}+\tfrac12\delta_{2\tau_0}
```
have the same lower support point $`\tau_0`$, but give
``` math
f_1(x)=e^{-\tau_0x},
 \qquad
 f_2(x)=\tfrac12e^{-\tau_0x}+\tfrac12e^{-2\tau_0x}.
```
They are different cutoff functions and have different moments. A relation such as $`\Lambda\sim\tau_0^{-1/2}`$ therefore sets at most a characteristic scale after a convention is chosen; it does not select $`f`$. ◻

</div>

This no-go result identifies the missing datum cleanly. MTT needs a selected proper-time measure, or an equivalent source functional, together with a normalization convention. A family of admissible damping functions is not the same as one predicted cutoff profile.

# The finite MTT execution

The current finite results are stronger than the assumptions used in Version 1, but their status is more differentiated. They should be presented directly rather than summarized as one undefined bottleneck vector.

## Representation and gauge group

The selected finite carrier has a three-family chiral sector
``` math
\mathcal{H}_{\mathrm{chiral}}
   =\mathbb{C}^3_{\mathrm{family}}\otimes\mathcal{H}_{16},
  \qquad \dim_\mathbb{C}\mathcal{H}_{\mathrm{chiral}}=48.
```
Its rows reproduce the $`Q,u^c,d^c,L,e^c,N^c`$ representation pattern. On that same packet the local cubic, mixed, gravitational, and global $`SU(2)`$ anomaly checks cancel exactly. This is an exact finite representation result, not yet a theorem selecting a physical compactification vacuum.

The native bundle automorphisms produce
``` math
U(1)\times SU(2)\times SU(3)
```
on the selected carriers. Their central action has diagonal kernel $`\mathbb{Z}_6`$, giving the faithful group
``` math
G_{\mathrm{SM}}
   =\frac{SU(3)\times SU(2)\times U(1)_Y}{\mathbb{Z}_6}.
```
This exact result establishes the lower finite gauge group. It does not by itself provide its kinetic action or running couplings.

## Why the finite algebra requires completion

The native three-summand candidate
``` math
\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})
```
supports the familiar Standard Model representation, but the executed finite-axiom test finds a genuine obstruction in the neutral sector: the $`N^c`$ self-edge obstructs orientability and the associated antisymmetric intersection form is singular. Thus the uncompleted native triple is not a full finite real-even triple.

The minimal four-summand completion
``` math
\mathcal{A}_F=
 \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})\oplus\mathbb{C}_N
```
moves the neutral right-handed state to a distinct central sheet. The completed packet has an explicit orienting cycle and a nondegenerate intersection form. The anomaly equations then select one primitive anomaly-free abelian direction, reproducing hypercharge while excluding a second independent physical $`U(1)`$.

This is an important correction to the idea that “coherent overlap” alone canonically gives the standard finite algebra. The algebra was selected only after a no-go theorem and a specific minimal completion.

## Finite Dirac operator and Higgs one-forms

On the completed finite Hilbert space, the current execution constructs an explicit $`96\times96`$ finite Dirac operator. Self-adjointness, oddness, KO-dimension-six reality, and the order-zero and order-one conditions are checked on the accepted profile. The word *profile* matters: the charged, neutral, and Majorana entries are accepted physical coordinates, not yet values emitted by an MTT source theorem.

The one-form calculation evaluates all $`26\times26=676`$ real-algebra basis pairs. The unrestricted real fluctuation space has rank $`12`$, consisting of three rank-four scalar-doublet modules. It therefore does not automatically give the one-Higgs Standard Model. A selected q79/proto-spinor alignment projector has rank $`4`$ and removes eight unwanted real scalar directions, leaving one complex Higgs doublet.

The finite gauge traces are $`10:6:6`$ before the conventional $`5/3`$ hypercharge normalization and $`6:6:6`$ afterward. The profile finite Dirac operator also emits finite Yukawa invariants. These are exact calculations *of the selected/profile packet*; they are not yet high-scale physical predictions or an absolute normalization theorem.

<div id="tab:status">

| Object | Current tier | What remains |
|:---|:---|:---|
| Three-family representation and anomaly cancellation | Derived exact | Physical vacuum/source selector |
| Faithful $`G_{\mathrm{SM}}/\mathbb{Z}_6`$ structure | Derived exact | Upper automorphism and action transfer |
| Four-summand finite algebra | Derived exact after no-go | Same-source continuum realization |
| $`96\times96`$ finite Dirac operator | Profile replay | Source-derived masses, mixings, and phases |
| Rank-four one-Higgs submodule | Derived exact for selected projector | Upstream derivation of the projector |
| Gauge and Yukawa finite traces | Exact evaluation of profile data | Cutoff moments, absolute normalization, and RG transport |

The finite spectral-action status. “Exact” describes the declared packet and must not be read as source selection of its profile entries.

</div>

# The missing source/descent contract

To call the spectral action an MTT shadow in more than an interpretive sense, one must specify how upper coherent data descend to the lower product triple. The following contract makes that obligation explicit.

<div id="def:source" class="definition">

**Definition 7** (Selected spectral-action source contract). A selected spectral-action source contract consists of:

1.  an upper Hilbert complex $`(\mathcal{H}_U,D_U)`$ with a specified dense domain, upper involutive algebra $`\mathcal{A}_U`$, real/grading data where required, and one selected action $`S_U`$;

2.  a selected orthogonal projector $`P_U`$ whose range reduces $`D_U`$ and the relevant upper algebra action;

3.  a unitary
    ``` math
    U:\mathrm{Ran}P_U\longrightarrow \mathcal{H}_E\otimes\mathcal{H}_F
    ```
    and a representation homomorphism $`\iota:\mathcal{A}_E\otimes\mathcal{A}_F\to P_U\mathcal{A}_UP_U`$;

4.  the intertwining identities
    ``` math
    U(P_UD_UP_U)U^{-1}
     =D_E\otimes1+\gamma_E\otimes D_F
     \quad\text{and}\quad
     U\,\iota(a)\,U^{-1}=\pi(a);
    ```

5.  compatible transfer of the real structure, grading, domains, connections, inner fluctuations, and trace or measure entering the action;

6.  a selected rule sending the upper action to the lower bosonic and fermionic functionals, including $`(f,\Lambda)`$, field normalization, Wick dictionary, and RG/mass-scheme convention.

</div>

The reducing condition is essential. A generic compression $`PDP`$ need not inherit the bounded-commutator, first-order, reality, or domain properties of a spectral triple. Nor does equality of finite dimensions produce a canonical unitary intertwiner.

<div id="thm:descent" class="theorem">

**Theorem 8** (Conditional MTT spectral-action encoding). *If a selected MTT upper object satisfies Definition <a href="#def:source" data-reference-type="ref" data-reference="def:source">7</a>, then the lower almost-commutative triple and its spectral action are certified encodings of that upper object. Every lower operator, inner fluctuation, and action term is then the image of declared upper data under the same commuting source map.*

</div>

<div class="proof">

*Proof.* The first four clauses identify the reduced upper algebra, Hilbert space, and differential with the lower product triple. Compatibility with the real structure, grading, domains, and connections transfers the finite and product axioms. The final clause identifies the upper action functional and trace data with <a href="#eq:spectral-action,eq:fermionic-action" data-reference-type="ref+label" data-reference="eq:spectral-action,eq:fermionic-action">[eq:spectral-action,eq:fermionic-action]</a>. The standard output theorem <a href="#thm:standard" data-reference-type="ref" data-reference="thm:standard">4</a> then supplies the lower spectral-action expansion. Because all maps belong to one contract, the result is a source-preserving descent rather than an after-the-fact isomorphism. ◻

</div>

<div id="cor:open" class="corollary">

**Corollary 9** (What remains open). *The current finite carrier and spectral calculations do not prove <a href="#thm:descent" data-reference-type="ref+label" data-reference="thm:descent">8</a>. They establish lower representation compatibility and finite operator content, but they do not supply the selected upper differential/action, continuum base triple, full intertwiner, cutoff measure, or physical source values required by Definition <a href="#def:source" data-reference-type="ref" data-reference="def:source">7</a>.*

</div>

This is the precise frontier denoted by the live upper-action blocker. Adding another compatible lower matrix cannot close it. Closure requires one upper object whose automorphisms, zero modes, products, finite operators, and action all commute with the same descent maps.

# Which parameter claims survive

## Gauge sector

The finite representation fixes the gauge generators and their trace ratios on the selected packet. Once a cutoff moment and field normalization are supplied, these traces constrain relative kinetic coefficients. They do not select the absolute coupling scale, the matching scale, threshold corrections, or the RG trajectory. Therefore the exact finite trace ratio is a structural result; measured low-energy gauge couplings are not derived by this paper.

## Yukawa and mass sector

In almost-commutative geometry the entries of $`D_F`$ carry the Yukawa and neutral mass information. The current $`96\times96`$ construction shows that the accepted profile can be placed in a finite Dirac operator satisfying the tested axioms. This closes an encoding problem. A strict MTT prediction would instead require the upper source to emit the entries of $`D_F`$ before observed masses, mixings, or phases are inserted. That source-value theorem remains open.

## Higgs sector

The executed one-form calculation and the rank-four alignment projector explain how one complex Higgs doublet can be isolated inside the completed finite geometry. The coefficients of its effective potential depend on finite Dirac invariants, spectral moments, normalization, matching conditions, and RG transport. Since several of these inputs are still profile or open, the Higgs mass parameter and quartic coupling are not presently fixed functions of a single MTT vector.

## Cutoff and gravitational terms

The cosmological and gravitational coefficients in the heat-kernel expansion depend on different moments of $`f`$ and on the continuum geometry. The gap no-go in Proposition <a href="#prop:no-gap" data-reference-type="ref" data-reference="prop:no-gap">6</a> prevents these moments from being inferred from one spectral scale. A physical Lorentzian interpretation additionally requires a Wick or real-time contract; a Euclidean heat-kernel calculation alone does not provide unitary Lorentzian dynamics.

# A concrete reading of the shadow proposal

It is useful to see what the current result does accomplish. Begin with the selected finite family and gauge representation. Complete its algebra only after the neutral-sector no-go forces a distinct central sheet. Insert the accepted finite Dirac profile and verify the finite axioms. Enumerate the finite one-forms, observe that the raw scalar space is too large, and apply the selected rank-four alignment projector. The result is a typed finite noncommutative geometry with the Standard Model gauge representation and one complex Higgs doublet.

At this stage the word “shadow” has an operational but limited meaning: the finite MTT packet can be represented by the lower noncommutative data, and the spectral action is the standard action language for that data after the continuum and cutoff inputs are appended. What is not yet known is whether the same selected upper geometry generates every appended datum.

The distinction resembles the difference between fitting coordinates to a known solution and deriving the evolution equation that selects it. The finite execution has made the coordinates and consistency checks explicit. The source/descent contract asks for the evolution and selection law.

# Relation to the broader MTT program

This paper is deliberately downstream of the MTT fixed-point, projection, and typed-realization papers. Fixed points can identify stable or invariant subspaces. Projection can define a reduced carrier. Neither operation alone constructs a self-adjoint Dirac operator, a real structure, a cutoff measure, or an action. Those objects require the additional clauses in Definition <a href="#def:source" data-reference-type="ref" data-reference="def:source">7</a>.

The paper is also narrower than the dedicated MTT-to-NCG analysis. That work audits the complete finite spectral-triple axioms, the Euclidean product, the Wick contract, moment identifiability, and the finite gauge-fixed complex in detail. The present contribution is the action-level synthesis: it states exactly when the spectral action may be called an MTT encoding and why the upper action remains the decisive missing object.

Claims about collapse, event density, asymptotic safety, loop variables, or other shadows cannot be bundled into a single parameter vector merely because similar words such as gap, coherence, or projection occur in each construction. Cross-sector closure requires typed maps and common source data. It is a future theorem, not a premise of the spectral-action bridge.

# Falsifiability and next theorem

The revised bridge has concrete failure modes.

1.  If no upper differential has a reducing sector unitarily equivalent to the selected product Dirac operator, the proposed MTT source fails.

2.  If the upper automorphism action does not descend to the finite gauge action, representation compatibility is accidental rather than generative.

3.  If no selected upper trace or measure yields the required cutoff moments, the spectral action remains an appended effective functional.

4.  If source-derived $`D_F`$ entries fail to reproduce masses, mixings, and phases after declared transport, the numerical branch is falsified.

5.  If the continuum or Wick contract fails, the Euclidean spectral action cannot be promoted to a physical Lorentzian theory.

The next decisive theorem is therefore not another finite spectral identity. It is an *upper action and automorphism transfer theorem*: construct one selected q79 upper complex and action, identify its zero modes, transfer its products and automorphisms, and prove that the finite and continuum operators used here arise by commuting maps. Success would promote the current conditional encoding into a derivation. Failure would localize exactly which part of the spectral-action interpretation must be abandoned.

# Conclusion

The spectral action remains one of the clearest mathematical languages in which MTT could encode a four-dimensional matter-and-geometry sector. The current finite work has moved beyond analogy: it contains an exact chiral representation and gauge group, a proved algebraic obstruction and minimal completion, a profile-tier finite Dirac operator, and an exact selected one-Higgs submodule.

What has not been proved is equally clear. MTT has not yet selected the continuum product triple, generated the physical finite Dirac entries, fixed the cutoff profile or absolute normalization, or transferred a single upper action to all lower sectors. Version 2 therefore replaces the claim that the spectral action has already emerged with the stronger scientific object we actually possess: a conditional descent theorem, an executed finite encoding, and a sharply stated source obligation.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The finite calculations used by this paper are archived in the [curated MTT results repository at commit `31247ebb5c22`](https://github.com/PeterNero/mtt-results-repro/tree/31247ebb5c22f3fbb5443024365433c6ee0bff4a). The mapped authority/result identifiers are:

- `A46/typed_family_representation`;

- `A47/native_gauge_group`;

- `A49/physical_df_96`;

- `A50/neutral_summand_hypercharge`;

- `A51/finite_inner_fluctuation`;

- `A62/su3_finite_gauge_spectrum`.

Their manifests distinguish exact finite derivations from profile replay. Repository linkage does not promote profile values to source-derived predictions.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

A. H. Chamseddine and A. Connes, *The Spectral Action Principle*, Communications in Mathematical Physics **186** (1997), 731–750. <https://arxiv.org/abs/hep-th/9606001>

A. H. Chamseddine, A. Connes, and M. Marcolli, *Gravity and the Standard Model with Neutrino Mixing*, Advances in Theoretical and Mathematical Physics **11** (2007), 991–1089. <https://arxiv.org/abs/hep-th/0610241>

P. Nero, *From Modal Triplet Theory to Noncommutative Geometry: Spectral Triples, Finite Geometry, and the Exact Status of the Standard Model Encoding*, Zenodo preprint, July 2026.

P. Nero, *Modal Triplet Theory: Foundation*, Zenodo preprint, revised July 2026. <https://doi.org/10.5281/zenodo.16949762>

P. Nero, *Fixed Points I–VI*, Zenodo preprints, revised July 2026. <https://doi.org/10.5281/zenodo.16948748>

P. Nero, *The Modal Triplet Theory Program C: A Typed Dictionary for Geometric, Bundle, and Operator Realizations*, Version 4, July 2026. <https://doi.org/10.5281/zenodo.21718498>

P. Nero, *MTT Curated Results and Reproducibility Repository*, commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`, 2026. <https://github.com/PeterNero/mtt-results-repro/tree/31247ebb5c22f3fbb5443024365433c6ee0bff4a>

</div>
