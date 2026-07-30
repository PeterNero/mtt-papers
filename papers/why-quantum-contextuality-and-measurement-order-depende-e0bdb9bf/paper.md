---
abstract: |
  Quantum contextuality and sequential measurement order effects are related, but they are not the same mathematical phenomenon. Kochen–Specker contextuality is a static obstruction to gluing locally compatible value assignments into one global noncontextual assignment. An order effect is a dynamical statement about the noncommuting composition of quantum instruments, including their state-update maps. We formulate both structures explicitly and prove two separation results. First, projective qubit measurements exhibit an exact order effect even though the original projective Kochen–Specker obstruction does not apply in dimension two. Second, two instruments can have the same effects and identical one-step outcome probabilities while producing different sequential statistics. Effect or valuation data therefore cannot determine order dependence. A common MTT carrier may nevertheless source both structures. We state the required context-indexed source, instrument, measure, and naturality data for such a unification and identify the missing comparison theorem. The current q79 binary one-anchor recorder supplies an exact stopped-output law for one restricted apparatus domain; it does not yet provide the family of contexts needed for a contextuality theorem or a general contextuality–order equivalence.
author:
- Peter Nero
current_version: v2
date: July 2026, Version 2
generated_from_main_tex_sha256: e0afb48e4fddfc7039632afed8e5af33550cf19919ea3cd6b0c0d3f4008e2c0f
paper_id: why-quantum-contextuality-and-measurement-order-depende-e0bdb9bf
release_state: zenodo_released
released_version: v2
title: |
  Contextuality and Sequential Measurement Order:
  Distinct Obstructions with a Shared MTT Interface
zenodo_doi: 10.5281/zenodo.21666021
zenodo_record_id: 21666021
zenodo_url: "https://zenodo.org/records/21666021"
---

# Version 2 Revision Note

Supersedes
*Why Quantum Contextuality and Measurement Order Dependence Are the Same Phenomenon: A Projection-Based Shadow Bridge in Modal Triplet Theory*, version 1.

Reason
The earlier central theorem identified failure of a common basin refinement with sequential order dependence. Its proof did not establish either implication. It also treated Kochen–Specker contextuality, generalized operational contextuality, incompatible observables, and instrument disturbance as interchangeable notions.

Resolution
This version states the instrument algebra explicitly, separates static valuation/gluing obstructions from dynamic composition, and gives exact counterexamples to the claimed equivalence. It replaces the old bridge theorem with a typed MTT construction contract.

Retained result
Contextuality and order effects can be invariants of one richer context-indexed physical model. Projection, admissibility, stable records, and a shared upper carrier remain plausible ingredients of that model.

Remaining boundary
MTT has not yet constructed a selected family of physical apparatus instruments together with a contextuality scenario and a theorem relating its global-section obstruction to instrument composition. The canonical q79 binary recorder is exact only on its declared one-context domain.

# The corrected relation

Four notions were compressed in the earlier paper:

1.  incompatibility of observables;

2.  Kochen–Specker failure of a noncontextual global valuation;

3.  generalized contextuality of preparations, transformations, or effects;

4.  dependence of sequential statistics on instrument order.

They can interact, but they use different data and answer different questions. The corrected relation is
``` math
\boxed{
\begin{gathered}
\text{one context-indexed physical carrier}\\
\Downarrow\\
\text{static contextuality data}
\qquad\text{and}\qquad
\text{dynamic instrument data}.
\end{gathered}}
```
The two lower structures may share a source without being equal. A theorem identifying them would need a map between their mathematical categories and proof that the relevant obstructions correspond.

Basic data.
Contextuality uses contexts, compatible outcomes, and empirical distributions. Sequential order uses completely positive instrument maps.

Question.
Contextuality asks whether local assignments can be glued globally. Sequential order asks whether physical composition depends on order.

Typical obstruction.
The former is the absence of a global section or noncontextual model. The latter is noncommuting state update.

Role of effects.
Effects are central to many contextuality scenarios, but they are insufficient to determine a sequential order effect.

# Measurement as an ordinary physical instrument

Measurement is a physical interaction. It does not acquire a special logical status because an observer reads the record. The appropriate operational object includes both outcome probabilities and the state made available to later interactions.

<div class="definition">

**Definition 1** (Finite quantum instrument). Let $`\mathcal{H}`$ be a complex Hilbert space. A finite quantum instrument $`\mathcal{I}^A=\{\mathcal{I}_i^A\}_{i\in I_A}`$ is a family of completely positive, trace-nonincreasing maps on trace-class operators such that
``` math
\sum_{i\in I_A}\mathcal{I}_i^A
```
is trace preserving. Its effects are
``` math
E_i^A=\mathcal{I}_i^{A*}(\mathbf{1}),\qquad
E_i^A\geq0,\qquad
\sum_i E_i^A=\mathbf{1}.
```

</div>

For an input density operator $`\rho`$, the probability and conditional post-measurement state are
``` math
\begin{equation}
p(i|A,\rho)=\operatorname{Tr}\!\left[\mathcal{I}_i^A(\rho)\right]
            =\operatorname{Tr}(\rho E_i^A),
\qquad
\rho_{i|A}=
\frac{\mathcal{I}_i^A(\rho)}{p(i|A,\rho)}
\label{eq:instrument}
\end{equation}
```
when the denominator is nonzero. This is the standard instrument distinction: the effects determine one-step probabilities, while the maps $`\mathcal{I}_i^A`$ also determine what can happen next .

For instruments $`A`$ and $`B`$, the sequential joint laws are
``` math
\begin{align}
p_{A\rightarrow B}(i,j|\rho)
 &=\operatorname{Tr}\!\left[\mathcal{I}_j^B\!\left(\mathcal{I}_i^A(\rho)\right)\right],
\label{eq:forward}\\
p_{B\rightarrow A}(j,i|\rho)
 &=\operatorname{Tr}\!\left[\mathcal{I}_i^A\!\left(\mathcal{I}_j^B(\rho)\right)\right].
\label{eq:reverse}
\end{align}
```

<div class="definition">

**Definition 2** (Sequential order effect). The pair $`A,B`$ has a sequential order effect on $`\rho`$ if a declared comparison of the operational laws in <a href="#eq:forward" data-reference-type="eqref" data-reference="eq:forward">[eq:forward]</a>–<a href="#eq:reverse" data-reference-type="eqref" data-reference="eq:reverse">[eq:reverse]</a> differs. For example, one may compare the probability of obtaining the labelled result $`+`$ in both positions.

</div>

An order effect is therefore not merely the statement that two operators fail to commute. It is a statement about an input state, two fully specified instruments, and a chosen comparison of their sequential records.

# Contextuality is a gluing obstruction

A sharp contextuality scenario starts with a set $`X`$ of measurements and a cover $`\mathcal{C}`$ whose elements are jointly measurable contexts. If every measurement has outcome set $`O`$, a local assignment on $`C\in\mathcal{C}`$ is an element of $`O^C`$. An empirical model gives a compatible probability distribution on the assignments in every context.

A deterministic noncontextual assignment is one global element of $`O^X`$ whose restriction to each context is allowed. More general noncontextual models are convex mixtures of such assignments. Contextuality is the failure of the relevant global model to exist. The sheaf formulation makes this local-to-global obstruction explicit .

For projective quantum measurements, the Kochen–Specker theorem rules out a global value assignment satisfying the functional relations among commuting observables in Hilbert-space dimension at least three . This is a theorem about compatible valuations. It does not specify a state-update map for any physical apparatus.

Generalized operational contextuality is broader. It asks whether operationally equivalent preparations, transformations, or measurement events must have identical representations in an ontological model . That framework can include transformation contextuality and can apply to qubits. It remains important to name which notion is being used; “contextuality” alone does not turn a static Kochen–Specker scenario into a theorem about sequential instruments.

# Exact separation results

## Order dependence without projective Kochen–Specker contextuality

Let
``` math
|0\rangle=
\begin{pmatrix}1\\0\end{pmatrix},
\qquad
|+\rangle=\frac{1}{\sqrt2}
\begin{pmatrix}1\\1\end{pmatrix},
\qquad
P_z=|0\rangle\langle0|,
\qquad
P_x=|+\rangle\langle+|.
```
Take the initial state $`\rho=P_z`$. Let $`Z`$ and $`X`$ be the binary projective measurements in the $`z`$- and $`x`$-bases, with their Lueders instruments
``` math
\mathcal{I}_i^Z(\rho)=P_i^Z\rho P_i^Z,
\qquad
\mathcal{I}_j^X(\rho)=P_j^X\rho P_j^X .
```

<div id="prop:qubit-order" class="proposition">

**Proposition 3** (Exact qubit order effect). *For the events $`z+`$ and $`x+`$,
``` math
p_{Z\rightarrow X}(z+,x+|\rho)=\frac12,
\qquad
p_{X\rightarrow Z}(x+,z+|\rho)=\frac14.
```
Thus a two-dimensional projective system can exhibit a sequential order effect even though the original projective Kochen–Specker theorem does not apply in dimension two.*

</div>

<div class="proof">

*Proof.* The $`z+`$ outcome occurs first with probability one and leaves the state $`P_z`$. Hence
``` math
p_{Z\rightarrow X}(z+,x+|\rho)
=\operatorname{Tr}(P_xP_zP_x)=|\langle+|0\rangle|^2=\frac12.
```
In the reverse order, the $`x+`$ outcome occurs with probability $`1/2`$, leaves the state $`P_x`$, and the later $`z+`$ outcome has conditional probability $`1/2`$. Therefore
``` math
p_{X\rightarrow Z}(x+,z+|\rho)=\frac12\cdot\frac12=\frac14.
```
 ◻

</div>

<div class="remark">

*Remark 4*. Proposition <a href="#prop:qubit-order" data-reference-type="ref" data-reference="prop:qubit-order">3</a> does not say that every generalized notion of contextuality is absent for qubits. Spekkens contextuality can occur in dimension two. The proposition addresses the specific equivalence claimed in version 1: ordinary sequential order dependence does not imply the original Kochen–Specker global-valuation obstruction.

</div>

## The same effects can have different sequential laws

The second separation is more basic. A POVM records only effects, whereas an instrument also records state updates.

<div id="thm:instrument-underdetermination" class="theorem">

**Theorem 5** (Instrument underdetermination). *There exist two instruments with identical effects and identical one-step outcome probabilities for every input state, but with different statistics under the same subsequent measurement.*

</div>

<div class="proof">

*Proof.* On a qubit let $`P_0=|0\rangle\langle0|`$ and $`P_1=|1\rangle\langle1|`$. Define the Lueders instrument
``` math
\mathcal{L}_i(\rho)=P_i\rho P_i
```
and a measure-and-prepare instrument
``` math
\mathcal{M}_i(\rho)=\operatorname{Tr}(P_i\rho)\sigma_i,
\qquad
\sigma_0=|+\rangle\langle+|,
\quad
\sigma_1=|-\rangle\langle-|.
```
Both families are completely positive, their sums are trace preserving, and both have effects $`P_i`$. Therefore
``` math
\operatorname{Tr}[\mathcal{L}_i(\rho)]=\operatorname{Tr}[\mathcal{M}_i(\rho)]=\operatorname{Tr}(P_i\rho)
```
for every $`\rho`$.

Now take $`\rho=P_0`$, retain the first outcome $`0`$, and then measure $`\{P_0,P_1\}`$ again. The Lueders instrument gives
``` math
\operatorname{Tr}[P_0\mathcal{L}_0(P_0)]=1,
```
whereas the measure-and-prepare instrument gives
``` math
\operatorname{Tr}[P_0\mathcal{M}_0(P_0)]
=\operatorname{Tr}(P_0|+\rangle\langle+|)=\frac12.
```
Thus the same effects and one-step probabilities do not determine the sequential law. ◻

</div>

<div id="cor:no-bare-bridge" class="corollary">

**Corollary 6** (No bare contextuality–order equivalence). *No theorem formulated only in terms of effects, compatibility contexts, or global valuations can determine general sequential order effects. Instrument update maps or equivalent dynamical data are indispensable.*

</div>

<div class="proof">

*Proof.* The data listed in the corollary cannot distinguish the two instruments in Theorem <a href="#thm:instrument-underdetermination" data-reference-type="ref" data-reference="thm:instrument-underdetermination">5</a>, while a subsequent measurement does distinguish them. ◻

</div>

This corollary identifies the exact flaw in the old basin-atlas bridge. Failure of a common invariant refinement was used simultaneously as a valuation obstruction and as a dynamical noncommutation statement. Those properties belong to different structures unless a comparison map has been supplied and proved faithful to both.

# A shared MTT interface

The failure of equivalence does not make a common-source program empty. It specifies what that program must construct.

<div class="definition">

**Definition 7** (Context-indexed MTT measurement package). A context-indexed MTT measurement package consists of:

1.  an upper physical state space $`\Omega`$ with selected preparation laws $`\mu_\rho`$;

2.  a compatibility cover $`(X,\mathcal{C})`$ and a presheaf of record assignments;

3.  for every apparatus context $`C`$, a physical coupling and record map $`r_C:\Omega\to O^C`$;

4.  for every sequential apparatus $`A`$, a quantum instrument $`\mathcal{I}^A=\{\mathcal{I}_i^A\}`$;

5.  a context-indexed projection or intertwiner that derives each $`\mathcal{I}_i^A`$ from the same upper dynamics;

6.  pushforward identities
    ``` math
    (r_C)_*\mu_\rho=e_C
    ```
    for the contextual empirical distributions; and

7.  composition identities showing that upper sequential evolution descends to $`\mathcal{I}_j^B\circ\mathcal{I}_i^A`$.

</div>

The static and dynamic questions can then be asked on one package:
``` math
\begin{align*}
\mathfrak{o}_{\mathrm{ctx}}
&=\text{obstruction to a compatible global section},\\
\mathfrak{o}_{\mathrm{ord}}(A,B,\rho)
&=\text{difference between declared sequential laws}.
\end{align*}
```
They are two invariants of one object. They are not automatically the same invariant.

## What a genuine bridge theorem would require

A nontrivial contextuality–order bridge must add a rule
``` math
\Phi:
\{\text{global-section obstructions}\}
\longrightarrow
\{\text{instrument-composition obstructions}\}
```
or a functor between the underlying categories, and prove at least:

1.  *typing*: $`\Phi`$ is defined for the selected physical context family, not for an analogy between labels;

2.  *naturality*: restrictions of contexts commute with the MTT projection and with instrument composition;

3.  *measure preservation*: empirical supports and probabilities are the pushforwards of one selected source law;

4.  *soundness*: a static obstruction mapped by $`\Phi`$ produces the declared dynamic obstruction;

5.  *completeness*, if equivalence is claimed: every such dynamic obstruction comes from the static one.

Proposition <a href="#prop:qubit-order" data-reference-type="ref" data-reference="prop:qubit-order">3</a> shows that completeness fails for the broad class of all sequential instruments. Theorem <a href="#thm:instrument-underdetermination" data-reference-type="ref" data-reference="thm:instrument-underdetermination">5</a> shows that soundness cannot be obtained from effects alone. A future bridge must therefore use a restricted, geometry-selected instrument family and state its domain.

# What projection and fixed points may contribute

The useful MTT intuition can now be stated without overclaim.

## Projection can expose different lower structures

One upper evolution may be read through several context-indexed projections. Its one-step record supports may define a compatibility scenario, while its conditioned evolution may define an instrument. If the projections are derived from one carrier, both lower descriptions have a common physical origin.

Common origin is already valuable. It can explain why the same apparatus labels occur in contextuality tests and sequential protocols. It may also constrain which instruments are physically realizable. It does not prove that the global-section obstruction equals noncommutativity of those instruments.

## Fixed points can support records

Stable fixed points or attracting regions can model persistent apparatus records after a coupling. For a context $`C`$, an MTT construction could assign record regions $`B_i^C\subset\Omega`$ and require
``` math
\mu_\rho(B_i^C)=\operatorname{Tr}(\rho E_i^C).
```
This is a meaningful source equation. The regions, measure, and equality must all be derived; normalized labels or noninvertible projection alone do not produce the probability law.

Nor does a family of record basins automatically instantiate a Kochen–Specker scenario. One must prove which basins represent the same event when it appears in overlapping compatible contexts. That overlap or gluing map is exactly where contextuality lives.

## Order belongs to the coupling, not only the partition

For sequential experiments the physical maps must retain the conditioned post-record state. A partition of state space can say where a record lies but not, by itself, how a subsequent apparatus acts. The required MTT object is therefore a context-indexed transition kernel or CP instrument, not merely a basin atlas.

# Current MTT status

## The exact restricted result

The current q79 program has an exact result on a declared canonical domain. For its binary one-anchor nondemolition Fock recorder, the selected normal state emits the stopped output measure, and second-moment capture descent is exact. No separate Born axiom, fitted probability, observed probability, or stochastic primitive is added on that domain.

This closes a real instrument-and-measure statement for one binary apparatus. It improves the old paper’s unsupported claim that projection alone supplies Born basin measures.

## What the restricted result does not establish

One binary context cannot display a Kochen–Specker gluing obstruction. The current result does not yet construct:

- a family of overlapping compatible apparatus contexts;

- context-independent identification of shared measurement events;

- every corresponding physical instrument from one selected geometry;

- arbitrary-context Born descent;

- controlled finite-bandwidth or non-Markov corrections;

- or an objective rule selecting one ontic history.

The current status is therefore
``` math
\begin{array}{ll}
\text{canonical binary q79 record law:}&\text{exact on its domain},\\
\text{general selected apparatus family:}&\text{open},\\
\text{MTT contextuality realization:}&\text{open},\\
\text{contextuality--order equivalence:}&\text{not established}.
\end{array}
```

# Interpretive consequences

## Contextuality does not force anti-realism

Kochen–Specker excludes a particular kind of global noncontextual value assignment. It does not prove that physical records are unreal, that observers create reality, or that every realist theory is impossible. Generalized contextuality similarly constrains ontological representations under explicit operational-equivalence assumptions. MTT may seek a realist upper carrier, but it must reproduce those no-go results rather than dissolve them by renaming context-dependent variables.

## Disturbance is not a dismissive explanation

Calling an order effect “disturbance” is not an explanation until the instrument is specified. Equations <a href="#eq:forward" data-reference-type="eqref" data-reference="eq:forward">[eq:forward]</a>–<a href="#eq:reverse" data-reference-type="eqref" data-reference="eq:reverse">[eq:reverse]</a> make the mechanism testable. Two apparatus implementations of the same POVM can disturb differently, as Theorem <a href="#thm:instrument-underdetermination" data-reference-type="ref" data-reference="thm:instrument-underdetermination">5</a> shows.

## No privileged measurement event is required

The formalism treats preparation, coupling, record formation, and later coupling as ordinary dynamics. “Measurement” names a physical process with a classical record interface. The distinction between contextuality and order does not add an observer postulate; it simply keeps the static and dynamic parts of that process typed correctly.

# Completion program

The strongest next theorem is not another verbal shadow bridge. It is the construction of one finite, selected test case:

1.  choose a contextuality scenario with overlapping contexts and an experimentally meaningful inequality or logical support obstruction;

2.  construct each apparatus coupling and instrument from the same q79 source rather than importing arbitrary CP maps;

3.  prove the source-measure pushforwards for all contexts;

4.  compute both the contextuality witness and every relevant sequential law from that package; and

5.  test whether a restricted natural transformation relates the two obstructions, recording counterexamples if it does not.

A qutrit Kochen–Specker or KCBS-type context family would test the static side. A matched set of sequential instruments would test the dynamic side. The output should be a table distinguishing:
``` math
\text{same source},\quad
\text{correlated invariants},\quad
\text{one-way implication},\quad
\text{equivalence}.
```
Only the last entry would justify the original title.

# Conclusion

Quantum contextuality and sequential measurement order are not one theorem in two guises. Contextuality concerns the impossibility of a noncontextual global model for locally compatible data. Order dependence concerns the composition of physical instruments. Qubit Lueders measurements already refute the broad equivalence, and instruments with identical effects show why effect or valuation data cannot recover the missing dynamics.

The MTT common-source idea survives in a sharper form. A selected upper carrier may generate both a contextual empirical model and a family of sequential instruments. Fixed points may provide stable records, and projection may relate upper dynamics to lower apparatus maps. The required source, intertwining, pushforward, and gluing theorems are now explicit. The current q79 binary recorder closes one important local part of that construction, but the multi-context bridge remains open.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The contextuality and sequential-order obstructions are established from their respective operational data. The open strict-upgrade ledger proves neither obstruction and is included only to delimit stronger claims of complete physical reconstruction.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

S. Kochen and E. P. Specker, *The Problem of Hidden Variables in Quantum Mechanics*, Journal of Mathematics and Mechanics **17** (1967) 59–87, doi:10.1512/iumj.1968.17.17004.

E. B. Davies and J. T. Lewis, *An Operational Approach to Quantum Probability*, Communications in Mathematical Physics **17** (1970) 239–260, doi:10.1007/BF01647093.

R. W. Spekkens, *Contextuality for Preparations, Transformations, and Unsharp Measurements*, Physical Review A **71** (2005) 052108, doi:10.1103/PhysRevA.71.052108, arXiv:quant-ph/0406166.

S. Abramsky and A. Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*, New Journal of Physics **13** (2011) 113036, doi:10.1088/1367-2630/13/11/113036, arXiv:1102.0264.

P. Nero, *Born-Compatible Record Measures and the Classical Concentration Limit: Separate Theorems and Their MTT Interface*, version 2, MTT research manuscript, July 2026.

P. Nero, *MTT Results Reproducibility Repository*, <https://github.com/PeterNero/mtt-results-repro>.

</div>
