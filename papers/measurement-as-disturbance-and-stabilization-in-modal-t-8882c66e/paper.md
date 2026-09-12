---
abstract: |
  Measurement is an ordinary physical interaction, but an adequate mathematical description must distinguish three stages: apparatus coupling, completion into an outcome-resolved transition, and stabilization of the resulting record. This paper formulates that distinction for Modal Triplet Theory (MTT). A localized coupling may displace a state from a quiet coherent regime, and contractive dynamics inside a selected record basin may then stabilize a repeatable record. Neither fact chooses a basin. We therefore introduce the missing transition-completion object: a normalized kernel, or in quantum language an instrument, that assigns both an outcome probability and a post-outcome state. We prove that one global contraction cannot support multiple stable outcomes, derive the exact normalization and conditional-state laws of a completion kernel, and distinguish failure of unique decoding from the possible existence of a representative section. Decoherence suppresses interference within an outcome algebra but does not select one instrument element. The Born rule requires a selected preparation law and a basin–trace or instrument–trace equality. The current q79 binary one-anchor recorder supplies such an exact stopped-output law on its declared domain; arbitrary apparatus contexts and objective one-history selection remain open. An Ornstein–Uhlenbeck variance is retained only as a conditional linear-response model and is not identified with the Heisenberg uncertainty principle.
author:
- Peter Nero
current_version: v7
date: 12 September 2026, Version 7
generated_from_main_tex_sha256: c9379807cef8584ef8330f5fef8c4682a7677da928d81dc11d1e4608078ab5b8
paper_id: measurement-as-disturbance-and-stabilization-in-modal-t-8882c66e
release_state: current_revised_tex
released_version: v6
title: |
  Measurement as Physical Disturbance, Outcome Completion,
  and Record Stabilization in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.21665982
zenodo_record_id: 21665982
zenodo_url: "https://zenodo.org/records/21665982"
---

# Measurement as Physical Disturbance, Outcome Completion, and Record Stabilization in Modal Triplet Theory

Peter Nero. 12 September 2026, Version 7

## Abstract

Measurement is an ordinary physical interaction, but an adequate mathematical description must distinguish three stages: apparatus coupling, completion into an outcome-resolved transition, and stabilization of the resulting record. This paper formulates that distinction for Modal Triplet Theory (MTT). A localized coupling may displace a state from a quiet coherent regime, and contractive dynamics inside a selected record basin may then stabilize a repeatable record. Neither fact chooses a basin. We therefore introduce the missing transition-completion object: a normalized kernel, or in quantum language an instrument, that assigns both an outcome probability and a post-outcome state. We prove that one global contraction cannot support multiple stable outcomes, derive the exact normalization and conditional-state laws of a completion kernel, and distinguish failure of unique decoding from the possible existence of a representative section. Decoherence suppresses interference within an outcome algebra but does not select one instrument element. The Born rule requires a selected preparation law and a basin–trace or instrument–trace equality. The current q79 binary one-anchor recorder supplies such an exact stopped-output law on its declared domain; arbitrary apparatus contexts and objective one-history selection remain open. An Ornstein–Uhlenbeck variance is retained only as a conditional linear-response model and is not identified with the Heisenberg uncertainty principle.

# Version 7 Revision Note

**Supersedes** Version 6 as the current manuscript; its released identity and revision note are retained.

**Reason** The continuum-recorder and ontology refinements need explicit consumer references in the coupling/completion/stabilization account.

**Resolution** A concise source interface states the compiler hypotheses and operational non-entailment result with their contextual owners.

**Retained** The local kernel and contraction theorems, ordinary physical measurement, and exact canonical binary recorder remain unchanged.

**Open boundary** Physical continuum source selection, universal apparatus control, and objective actualization remain separate research obligations.

# Version 6 Revision Note

**Supersedes** *Measurement as Disturbance and Stabilization in Modal Triplet Theory*, version 5.

**Reason** The earlier paper combined localized disturbance, global contractivity, multiple outcome basins, decoherence, Born probabilities, uncertainty, Bell correlations, and neutrino mass in one mechanism. A global contraction has only one fixed point, basin volume does not by itself produce Born weights, and noninjective projection does not imply that no right inverse or representative section can exist.

**Resolution** This version separates coupling, transition completion, outcome-conditioned stabilization, decoherence, probability source, and one-history actualization. It adds the missing completion kernel, corrects the inverse terminology, and states the current q79 recorder result at its exact restricted tier.

**Retained result** A measuring apparatus can be treated as a localized physical coupling followed by basin-local stabilization. Contractive dynamics can explain record persistence and repeatability after an outcome has been resolved.

**Remaining boundary** MTT has not yet derived the completion instrument and Born-compatible source law for every apparatus context, nor an objective rule selecting one ontic history. The physical upper geometry must be supplied by the selected branch rather than assumed to be a generic ten-dimensional product.

# The measurement chain

A measurement is not important because a conscious observer notices it. It is important because a physical interaction produces a durable, communicable record. A complete model must answer several different questions:

1.  How does the apparatus couple to the system?

2.  Which record alternatives are physically available?

3.  What assigns a probability to each alternative?

4.  What state is available after each recorded outcome?

5.  Why does a completed record remain stable?

6.  If an ontic account is intended, what selects one individual history?

The corrected MTT decomposition is
``` math
\boxed{
\text{coupling/disturbance}
\longrightarrow
\text{outcome completion}
\longrightarrow
\text{record stabilization}.
}
```
The middle arrow cannot be omitted. A disturbance may move a state toward a boundary, and a contraction may stabilize a state once it lies in a basin. Neither statement determines which basin receives the state.

# Standard operational target

Let $`\mathcal{H}`$ be a complex Hilbert space and $`\rho`$ a density operator.

<div class="definition">

**Definition 1** (Quantum instrument). A finite quantum instrument $`\mathcal{I}=\{\mathcal{I}_i\}_{i\in I}`$ is a family of completely positive, trace-nonincreasing maps on trace-class operators such that $`\sum_i\mathcal{I}_i`$ is trace preserving. Its effects are
``` math
E_i=\mathcal{I}_i^*(\mathbf{1}),\qquad
E_i\geq0,\qquad
\sum_iE_i=\mathbf{1}.
```

</div>

The outcome probability and conditional state are <a id="eq:instrument"></a>
``` math
\begin{equation}
p_i=\operatorname{Tr}[\mathcal{I}_i(\rho)]=\operatorname{Tr}(\rho E_i),
\qquad
\rho_i'=\frac{\mathcal{I}_i(\rho)}{p_i}
\quad(p_i>0).

\end{equation}
```
An instrument therefore includes both the classical record $`i`$ and the state passed to later physical interactions \[[1](#ref-DaviesLewis1970)\].

The nonselective channel
``` math
\mathcal{I}_{\mathrm{ns}}=\sum_i\mathcal{I}_i
```
describes what remains if the outcome label is ignored. It is not an outcome-selection law. Keeping $`\mathcal{I}_{\mathrm{ns}}`$ while deleting the individual $`\mathcal{I}_i`$ removes precisely the information needed to say which record occurred.

# An upper transition-completion kernel

MTT seeks an upper physical account of equation [(1)](#eq:instrument). The minimal classical-measure analogue is an outcome-resolved kernel.

<div class="definition">

**Definition 2** (Transition-completion kernel). Let $`E`$ be a measurable pre-completion exit space, let $`I`$ be a finite record set, and let $`D_i`$ be the post-completion state space associated with record $`i`$. A transition-completion kernel is a family
``` math
\mathcal{K}_i:E\times\mathfrak{B}(D_i)\longrightarrow[0,1]
```
such that:

1.  for fixed $`x\in E`$, $`\mathcal{K}_i(x,\cdot)`$ is a finite measure on $`D_i`$;

2.  for fixed measurable $`A\subseteq D_i`$, $`\mathcal{K}_i(\cdot,A)`$ is measurable; and

3.  for every $`x\in E`$,
    ``` math
    \sum_{i\in I}\mathcal{K}_i(x,D_i)=1.
    ```

</div>

The kernel can encode unresolved upper degrees of freedom, an effective stochastic closure, or a genuinely probabilistic law. Those interpretations are not equivalent. The definition only states the data required at the effective level.

<div id="thm:completion" class="theorem">

**Theorem 3** (Completion law). *Let $`\nu`$ be a probability measure on $`E`$ and $`\{\mathcal{K}_i\}_{i\in I}`$ a transition-completion kernel. Define <a id="eq:completion-prob"></a>
``` math
\begin{equation}
p_i=\int_E\mathcal{K}_i(x,D_i)\,d\nu(x).

\end{equation}
```
Then $`p_i\geq0`$ and $`\sum_i p_i=1`$. If $`p_i>0`$, the conditional post-completion law <a id="eq:completion-state"></a>
``` math
\begin{equation}
\nu_i'(A)
=\frac{1}{p_i}\int_E\mathcal{K}_i(x,A)\,d\nu(x),
\qquad A\in\mathfrak{B}(D_i),

\end{equation}
```
is a probability measure on $`D_i`$.*

</div>

<div class="proof">

*Proof.* Nonnegativity follows from positivity of each kernel measure. Finite additivity and normalization give
``` math
\sum_i p_i
=\int_E\sum_i\mathcal{K}_i(x,D_i)\,d\nu(x)
=\int_E1\,d\nu(x)=1.
```
For $`p_i>0`$, equation [(3)](#eq:completion-state) inherits countable additivity from $`\mathcal{K}_i(x,\cdot)`$, is nonnegative, and satisfies $`\nu_i'(D_i)=1`$. ◻

</div>

<div class="remark">

*Remark 4*. Theorem [3.2](#thm:completion) is a normalization theorem, not a source theorem. It says what follows once $`\nu`$ and $`\mathcal{K}`$ have been physically selected. It does not determine either object and does not imply Born weights.

</div>

A deterministic completion is the special case in which a map $`c:E\to\bigsqcup_iD_i`$ sends every exit state to one outcome-conditioned state:
``` math
\mathcal{K}_i(x,A)
=\mathbf{1}_{\{c(x)\in D_i\cap A\}}.
```
An ensemble of hidden upper states can then yield nontrivial effective probabilities through $`\nu`$, even though $`c`$ is deterministic. This is an ordinary pushforward mechanism. It must not be described as probability created by projection.

# Basin-local stabilization

Once completion has produced a state in $`D_i`$, an outcome-conditioned map may stabilize the corresponding record.

<div id="thm:basin-contraction" class="theorem">

**Theorem 5** (Record-basin contraction). *Let $`(D_i,d_i)`$ be nonempty and complete, and let $`T_i:D_i\to D_i`$ satisfy
``` math
d_i(T_i x,T_i y)\leq q_i d_i(x,y),
\qquad 0\leq q_i<1.
```
Then $`T_i`$ has a unique fixed record $`r_i\in D_i`$, and
``` math
d_i(T_i^n x,r_i)\leq q_i^n d_i(x,r_i)
```
for every $`x\in D_i`$.*

</div>

<div class="proof">

*Proof.* This is the Banach contraction theorem applied on the explicitly declared complete invariant basin $`D_i`$. ◻

</div>

The hypotheses matter. Completeness, nonemptiness, invariance $`T_i(D_i)\subseteq D_i`$, and the strict contraction constant are all proof obligations. A local linear estimate near a candidate record does not establish a global invariant basin.

<div id="prop:no-global-contraction" class="proposition">

**Proposition 6** (A global contraction cannot encode several outcomes). *If a map $`T:D\to D`$ is a contraction on one nonempty complete space $`D`$, then it cannot have two distinct fixed records.*

</div>

<div class="proof">

*Proof.* The Banach theorem gives a unique fixed point. Equivalently, if $`Tx=x`$ and $`Ty=y`$, then
``` math
d(x,y)=d(Tx,Ty)\leq qd(x,y)
```
with $`q<1`$, hence $`d(x,y)=0`$. ◻

</div>

This corrects a central tension in version 5. Multiple outcomes require separate invariant basins $`D_i`$, a noncontractive transition region, a context-dependent map, an outcome kernel, or some combination of these. A single global Fundamental Contractivity Condition cannot simultaneously select several stable records.

## Repeatability

Repeatability is a statement about what happens after record $`i`$ is completed. If the later apparatus interaction preserves $`D_i`$ and its readout identifies the same record throughout a neighborhood of $`r_i`$, then Theorem [4.1](#thm:basin-contraction) supplies asymptotic stabilization. Immediate exact repeatability requires a stronger nondemolition or idempotence condition on the instrument. It does not follow from attraction alone.

# Projection, decoding, and irreversibility

Let $`P:\mathcal{U}\to\mathcal{X}`$ be an effective projection from upper configurations to records. If $`P`$ is noninjective, two upper states $`u_1\neq u_2`$ may have the same record $`P(u_1)=P(u_2)`$.

<div id="prop:decoder" class="proposition">

**Proposition 7** (Unique decoding versus representative selection). *If $`P:\mathcal{U}\to\mathcal{X}`$ is noninjective, there is no decoder $`D:\mathcal{X}\to\mathcal{U}`$ satisfying
``` math
D\circ P=\operatorname{id}_{\mathcal{U}}.
```
A right inverse or section $`s:\mathcal{X}\to\mathcal{U}`$ satisfying
``` math
P\circ s=\operatorname{id}_{\mathcal{X}}
```
may nevertheless exist. Such a section chooses one representative and does not recover the actual upper state in a nontrivial fiber.*

</div>

<div class="proof">

*Proof.* If $`P(u_1)=P(u_2)`$, a decoder would imply
``` math
u_1=D(P(u_1))=D(P(u_2))=u_2,
```
contradicting noninjectivity. The second statement has no such contradiction: a section chooses one element of each represented fiber. ◻

</div>

Irreversibility must therefore be stated operationally. Possible precise claims include:

- failure of unique decoding of the actual upper history;

- merger of distinct effective histories under the record map;

- absence of a physically admissible recovery channel;

- hysteresis or entropy production in a declared open-system model;

- or failure of upper dynamics to descend to a reversible lower map.

Bare noninjectivity does not prove all of them.

# Decoherence and outcome completion

Suppose a pointer decomposition defines a dephasing channel
``` math
\mathcal{D}(\rho)=\sum_iP_i\rho P_i.
```
Decoherence controls the off-diagonal blocks of the reduced state and explains why interference between record alternatives can become negligible \[[2](#ref-Zurek2003)\]. It does not, by itself, choose an index $`i`$.

The distinction is visible algebraically:
``` math
\rho
\longmapsto
\mathcal{D}(\rho)
=\sum_iP_i\rho P_i
```
is a nonselective channel. An outcome-resolved instrument retains the individual maps
``` math
\mathcal{I}_i(\rho)=P_i\rho P_i
```
and associates each with a record. Even then, the instrument gives an ensemble law and conditional states. If the theory promises one objective ontic history, another source or selection statement is required.

In MTT language, decoherence may occur inside or between approximate record sectors, while basin completion says which record label is emitted. Record stabilization then keeps that label robust. These are adjacent physical processes, not one theorem.

# The Born source obligation

Given an instrument, standard quantum mechanics predicts
``` math
p_i^{\mathrm{QM}}=\operatorname{Tr}(\rho E_i).
```
Given an upper completion package, Theorem [3.2](#thm:completion) predicts
``` math
p_i^{\mathrm{upper}}
=\int_E\mathcal{K}_i(x,D_i)\,d\nu_\rho(x).
```
The required MTT equality is <a id="eq:born-source"></a>
``` math
\begin{equation}
\boxed{
\int_E\mathcal{K}_i(x,D_i)\,d\nu_\rho(x)
=\operatorname{Tr}(\rho E_i)
\quad\text{for every allowed }\rho,\mathcal{I},i.
}

\end{equation}
```

Equation [(4)](#eq:born-source) displays all the missing data:

- the preparation-dependent upper law $`\nu_\rho`$;

- the selected apparatus completion kernel $`\mathcal{K}`$;

- the quantum effect $`E_i`$;

- and the equality on a declared preparation and apparatus domain.

Relative basin volume
``` math
\frac{\mu(B_i)}{\sum_j\mu(B_j)}
```
is merely a normalized probability model until the measure, preparation dependence, and equality [(4)](#eq:born-source) are proved. Contractivity does not determine those weights. The version 5 “Born rule from basin measures” proved only that a random initial point lands in a basin with the measure assigned to that basin; it did not prove equality to quantum trace weights.

# Current q79 measurement status

## Exact canonical domain

The q79 program now supplies a selected operational realization on one restricted domain. For the canonical binary one-anchor nondemolition Fock recorder:

- the finite state, observable, and output-algebra data are fixed;

- the commuting output algebra defines the record events;

- the selected normal state emits the stopped output measure;

- second-moment capture descent is exact; and

- no separate Born axiom, stochastic primitive, observed probability, or fit is inserted on that domain.

Thus the analogue of equation [(4)](#eq:born-source) is closed for that canonical binary apparatus. This is stronger than the conditional basin-volume story in version 5.

<a id="sec:recorder-source-interface"></a>

## Open quantifiers

The Born/record companion explains the selected Fock law and its conditional continuum compiler \[[3](#ref-NeroBornClassical2026),[6](#ref-FrozenFock),[7](#ref-FrozenContinuum)\]. The compiler requires a supplied positive self-adjoint Hessian, an invariant rank-three sector with kernel/support ranks one and two, and an isometry intertwining its projector pair with the finite pair. With the same clock, minimal Luders coupling, and no added Hamiltonian, it transports both the stopped probabilities and conditional states. Approximate intertwining gives finite-horizon error bounds; normalized rare-event states require a positive weight floor. This is how a selected geometric source could supply this paper’s completion instrument. It does not select the physical continuum endpoint, finite comparison map and tails, or clock by itself.

The ontology source has a different consumer role \[[9](#ref-LocalityCompanion),[8](#ref-FrozenOntology)\]. Its 448-atom canonical checkpoint admits one record per atom with the same probabilities and conditional states as the operational instrument; a coactual completion can preserve those data as well. Thus the completed operational instrument does not entail either ontology. This context-specific countermodel is not an apparatus-independent hidden-variable model, a physical one-history selector, or an additional stabilization law. In particular, stabilization after a record cannot choose between completions that already agree on every retained operational datum.

The exact result does not yet establish:

- the completion instrument for every allowed preparation and apparatus;

- finite-bandwidth and non-Markov detector corrections;

- a contextual family of overlapping measurements;

- a universal basin geometry for all quantum observables;

- or objective selection of one ontic history.

The correct ledger is
``` math
\begin{array}{ll}
\text{canonical q79 binary recorder:}&\text{exact on its domain},\\
\text{general MTT apparatus family:}&\text{open},\\
\text{universal Born source theorem:}&\text{open},\\
\text{objective one-history selector:}&\text{open}.
\end{array}
```

# A guarded Ornstein–Uhlenbeck model

Version 5 used Ornstein–Uhlenbeck (OU) widths as an explanation of quantum uncertainty. The OU calculation is valid as a conditional linear-response model, but the identification with Heisenberg uncertainty is not derived.

Let $`W_t`$ be standard Brownian motion and let a square-integrable $`a_0`$ be independent of its future increments. Suppose a reduced disturbance coordinate satisfies <a id="eq:ou"></a>
``` math
\begin{equation}
da_t=-\gamma a_t\,dt+\sigma\,dW_t,
\qquad \gamma>0.

\end{equation}
```

<div id="lem:ou" class="lemma">

**Lemma 8** (OU stationary variance). *Equation [(5)](#eq:ou) has the solution
``` math
a_t=e^{-\gamma t}a_0
+\sigma\int_0^t e^{-\gamma(t-s)}\,dW_s,
```
and
``` math
\operatorname{Var}(a_t)
=e^{-2\gamma t}\operatorname{Var}(a_0)
+\frac{\sigma^2}{2\gamma}
\left(1-e^{-2\gamma t}\right).
```
Consequently its stationary variance is
``` math
\operatorname{Var}_{\mathrm{stat}}(a)=\frac{\sigma^2}{2\gamma}.
```*

</div>

<div class="proof">

*Proof.* The variation-of-constants formula gives the displayed solution. Ito isometry gives
``` math
\sigma^2\int_0^t e^{-2\gamma(t-s)}\,ds
=\frac{\sigma^2}{2\gamma}(1-e^{-2\gamma t}),
```
which proves the variance formula and its limit. ◻

</div>

If instead
``` math
\dot a=-\gamma a+\eta(t),
\qquad
\|\eta\|_\infty\leq M,
```
then variation of constants gives
``` math
\limsup_{t\to\infty}|a(t)|\leq\frac{M}{\gamma}.
```
The stochastic variance and deterministic amplitude bound have different meanings and should not be identified.

To turn Lemma [9.1](#lem:ou) into a quantum-uncertainty theorem, MTT would need to derive:

1.  the reduced coordinate $`a`$ from selected observables;

2.  the noise or unresolved-state law and its strength $`\sigma`$;

3.  the damping $`\gamma`$ from the same source;

4.  the canonical commutator or symplectic form; and

5.  the Robertson–Schrodinger lower bound with the correct $`\hbar`$ normalization.

Without those steps, the OU floor is an effective fluctuation model, not the origin of quantum uncertainty.

# A concrete apparatus example

Consider a Stern–Gerlach-type spin readout. The corrected stages are:

1.  A magnetic-field gradient couples spin and position, producing spatially distinguishable wave packets.

2.  Environmental coupling and detector amplification suppress interference between macroscopic record sectors.

3.  An outcome-resolved instrument assigns the two detector records and their conditional post-measurement states.

4.  Record-sector dynamics stabilizes the fired detector state.

The field gradient is the physical coupling. Decoherence helps make the records robust. The instrument supplies the outcome-resolved law. Stabilization explains persistence. Calling the first step a disturbance does not calculate the third step, and calling the fourth step a contraction does not select between the two detector channels.

The same decomposition applies to interferometry, weak measurements, and multi-stage protocols. Bell experiments additionally require a bipartite state, local instrument algebras, setting assumptions, and a locality analysis. They cannot be derived from stabilization alone.

# Relation to interpretations

The framework is compatible with several ontological readings unless stronger MTT data are added:

- As an operational theory, the instrument and output law suffice for record statistics.

- As an epistemic upper-state model, probabilities may reflect a preparation law over unresolved upper configurations.

- As a stochastic completion, the kernel may be primitive or derived from a limit theorem.

- As a deterministic ontic completion, a selected upper state and deterministic completion map must explain the observed statistics.

No observer-dependent collapse is required to formulate any of these options. But the options are physically different. A claim that MTT selects one of them must identify the relevant source theorem.

# Completion program

The next measurement theorem should be built in this order:

1.  Select an upper carrier, preparation map, and apparatus coupling from the physical q79 branch.

2.  Identify finite record algebras and outcome spaces.

3.  Derive every instrument element or transition-completion kernel from the same coupling.

4.  Prove equation [(4)](#eq:born-source) for a nontrivial family of preparations and apparatus contexts.

5.  Prove basin-local stabilization or nondemolition repeatability after completion.

6.  Derive controlled detector bandwidth, memory, and environmental corrections.

7.  State whether one-history actualization is outside the theory or supply its selected mechanism.

This order prevents three familiar substitutions:
``` math
\begin{gathered}
\text{decoherence}\neq\text{outcome selection},\\
\text{basin stability}\neq\text{Born weight},\\
\text{projection}\neq\text{probability source}.
\end{gathered}
```

# Conclusion

The disturbance-and-stabilization intuition survives, but only as two parts of a three-stage measurement process. A physical coupling can displace a state. An outcome-resolved kernel or instrument completes that interaction into a record and post-record state. Basin-local contraction can then stabilize the record. A global contraction cannot perform all three jobs because it has only one fixed point.

The corrected inverse language also matters. Noninjective projection forbids unique decoding of the actual upper state, but it does not forbid every right inverse or representative section. Irreversibility requires a specified physical decoder, channel, or dynamical criterion.

MTT has one substantial exact foothold: the canonical q79 binary one-anchor recorder emits its stopped-output law and exact capture descent on the declared domain without a fitted probability. The general apparatus and one-history problems remain open. The transition-completion kernel introduced here makes their missing content explicit and gives the measurement program a testable, noncircular next step.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The distinction among coupling, outcome completion, and record stabilization is established from instruments and transition kernels. The open strict-upgrade ledger does not select an outcome law and is cited only to mark the stronger unresolved source boundary.

The referenced rows are frozen to the curated results repository state identified below. Hashes are grouped in eight-character blocks for line breaking.

> **Repository:** <https://github.com/PeterNero/mtt-results-repro>
> **Commit:** `31247ebb 5c22f3fb b5443024 365433c6 ee0bff4a`
> **Manifest:**
> **Manifest SHA-256:**
> `fb399689 60b00584 631dbf53 1a708e18`
> `ef928d6b 6d935119 c185d7f6 32b1e7cd`

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper’s local theorems; and an open row is evidence of an unresolved obligation, never of closure.

= by -
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

#### Open boundary (not evidence of closure).

- (*open*).

  Historical 2/9 strict no-knob ledger snapshot, not a current global completion count.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

# References

<a id="ref-DaviesLewis1970"></a>

\[1\] E. B. Davies and J. T. Lewis, *An Operational Approach to Quantum Probability*, Communications in Mathematical Physics **17** (1970) 239–260, doi:10.1007/BF01647093.

<a id="ref-Zurek2003"></a>

\[2\] W. H. Zurek, *Decoherence, Einselection, and the Quantum Origins of the Classical*, Reviews of Modern Physics **75** (2003) 715–775, doi:10.1103/RevModPhys.75.715, arXiv:quant-ph/0105127.

<a id="ref-NeroBornClassical2026"></a>

\[3\] P. Nero, *Born-Compatible Record Measures and the Classical Concentration Limit: Separate Theorems and Their MTT Interface*, version 3, MTT research manuscript, September 2026, Section 4.

<a id="ref-NeroContextOrder2026"></a>

\[4\] P. Nero, *Contextuality and Sequential Measurement Order: Distinct Obstructions with a Shared MTT Interface*, version 2, MTT research manuscript, July 2026.

<a id="ref-MTTResults"></a>

\[5\] P. Nero, *MTT Results Reproducibility Repository*, <https://github.com/PeterNero/mtt-results-repro>.

<a id="ref-FrozenFock"></a>

\[6\] P. Nero, *Canonical q79 Fock output measure and second-moment capture descent*, frozen source (2026). <https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_fock_output_measure/artifact.json>.

<a id="ref-FrozenContinuum"></a>

\[7\] P. Nero, *Continuum Hessian-to-recorder compiler*, frozen source (2026). <https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_continuum_recorder_compiler/artifact.json>.

<a id="ref-FrozenOntology"></a>

\[8\] P. Nero, *q79 operational ontology non-entailment*, frozen source (2026). <https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_ontology_nonentailment/artifact.json>.

<a id="ref-LocalityCompanion"></a>

\[9\] P. Nero, *Locality, Coherent Alternatives, and Physical Records: An Interpretive Account of Quantum Experiments in Modal Triplet Theory*, unpublished version 2 (September 2026), subsection *Operational data do not force many actual worlds*.
