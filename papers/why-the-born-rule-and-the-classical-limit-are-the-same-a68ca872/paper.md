---
abstract: |
  The Born rule and the emergence of classical behavior are related, but they are not the same mathematical problem. The first fixes outcome probabilities for a declared quantum preparation and instrument. The second asks when retained records and observables are well approximated by one stable classical alternative. We formulate their interface without identifying them. Standard Gleason-type results recover trace probabilities only after additive or effect-noncontextual probability assumptions are supplied; they do not select an MTT source measure. The current q79 program now provides a stronger, domain-specific result: its canonical binary one-anchor Fock recorder emits an exact stopped-output measure and second-moment capture descent from the selected normal state, without an added Born axiom, stochastic primitive, fit, or observed probability on that domain. General apparatus contexts and objective single-history actualization remain open. Separately, we prove exact concentration and persistence bounds. If one record has probability at least $`1-\varepsilon`$, the law is within $`\varepsilon`$ in total variation of a deterministic record, bounded observables differ by at most $`\varepsilon`$ times their oscillation, and a record with per-step escape probability at most $`\eta`$ survives $`n`$ steps with probability at least $`1-\varepsilon-n\eta`$. These statements define a controlled classical limit. They do not derive the outcome weights or select one realized history.
author:
- Peter Nero
current_version: v2
date: July 2026, Version 2
generated_from_main_tex_sha256: dcedc23f54f0a2c6faacd995b733e28ea5a39bd5d6cfbff2bdf470bcfe0d0526
paper_id: why-the-born-rule-and-the-classical-limit-are-the-same-a68ca872
release_state: zenodo_released
released_version: v2
title: |
  Born-Compatible Record Measures and the Classical Concentration Limit:
  Separate Theorems and Their MTT Interface
zenodo_doi: 10.5281/zenodo.21666025
zenodo_record_id: 21666025
zenodo_url: "https://zenodo.org/records/21666025"
---

# Version 2 Revision Note

Supersedes
*Why the Born Rule and the Classical Limit Are the Same Problem: A Projection-Based Shadow Bridge in Modal Triplet Theory*, version 1.

Reason
The earlier paper inferred squared-norm basin weights from projection, identified probability generation with classical concentration, and described both as a unified resolution. It did not state the measure and noncontextuality assumptions behind Gleason-style trace representation, and it did not distinguish record stability from selection of one outcome.

Resolution
This version separates the quantum probability source, ordinary instrument dynamics, decoherence, concentration, record persistence, and one-history actualization. It imports Gleason-type representation at its proper conditional tier, records the exact current q79 binary-recorder result, and proves finite concentration and persistence bounds independently.

Retained result
Born-compatible record weights and the classical limit can use the same outcome algebra and basin labels. Once a valid record law is known, concentration into one robust record gives a controlled deterministic approximation.

Remaining boundary
MTT has not yet derived the required outcome law for every allowed apparatus context, a universal concentration regime, or an objective rule selecting one ontic history. Projection alone supplies none of these three results.

# The corrected relation

There are at least four distinct questions in a measurement process.

1.  Which alternatives can become physical records?

2.  What probabilities are assigned to those records?

3.  When are interference terms between records operationally negligible?

4.  When is one record so dominant and stable that a deterministic classical description is accurate?

A fifth question may be asked: why is one individual record actual rather than another? Standard operational quantum mechanics need not answer that question in order to predict recorded frequencies. Any ontic completion must answer it without confusing the answer with the probability law.

The old title compressed questions 2 and 4 into one problem. The corrected claim is narrower and more useful:
``` math
\boxed{
\begin{gathered}
\text{Born-compatible record law}
+\text{ concentration and stability}\\
\Longrightarrow
\text{ controlled classical predictions}
\end{gathered}
}
```
Each input has its own hypotheses and can fail independently.

# Measurement as an ordinary physical instrument

Let $`\mathcal{H}`$ be a complex Hilbert space and $`\rho`$ a density operator. A finite quantum instrument is a family
``` math
\{\mathcal{I}_i\}_{i\in I}
```
of completely positive, trace-nonincreasing maps such that $`\sum_i\mathcal{I}_i`$ is trace preserving. Its effects are
``` math
E_i=\mathcal{I}_i^*(\mathbf{1}),\qquad
E_i\geq0,\qquad
\sum_iE_i=\mathbf{1}.
```
The operational outcome law and conditional post-measurement state are
``` math
\begin{equation}
p_i=\operatorname{Tr}(\rho E_i),\qquad
\rho_i'=\frac{\mathcal{I}_i(\rho)}{p_i}
\quad(p_i>0).
\label{eq:instrument}
\end{equation}
```

Nothing in <a href="#eq:instrument" data-reference-type="eqref" data-reference="eq:instrument">[eq:instrument]</a> makes measurement metaphysically privileged. An apparatus is a physical interaction that amplifies alternatives into records. The instrument formalism records the input-output statistics and state update of that interaction.

Suppose an upper model has measurable record regions $`B_i`$ and an upper probability law $`\mu_{\rho,\mathcal{I}}`$ for the preparation and apparatus context. The exact compatibility equation is
``` math
\begin{equation}
\mu_{\rho,\mathcal{I}}(B_i)=\operatorname{Tr}(\rho E_i)
\qquad\text{for every }i.
\label{eq:basin-trace}
\end{equation}
```
Writing down normalized basin weights does not prove <a href="#eq:basin-trace" data-reference-type="eqref" data-reference="eq:basin-trace">[eq:basin-trace]</a>. The source law, the record regions, and the equality to the trace weights all require independent construction.

# What Gleason-type theorems establish

Gleason’s theorem starts with a probability measure on the closed subspaces, or equivalently projections, of a real or complex Hilbert space of dimension greater than two. Countable additivity on mutually orthogonal subspaces implies that the measure has the trace form
``` math
\mu(P)=\operatorname{Tr}(\rho P)
```
for a positive trace-class operator $`\rho`$ . Extensions using positive-operator-valued measurements recover the trace form for generalized effects and can include two-dimensional systems .

These are representation theorems. Their assumptions already include a probability assignment satisfying strong consistency conditions. They show the form that such an assignment must take; they do not derive an upper physical measure from non-injective projection.

For an MTT application, the logical order is therefore:
``` math
\begin{gathered}
\text{selected preparation and record measure}\\
+\text{additivity or effect noncontextuality}
\end{gathered}
\Longrightarrow
\text{trace representation},
```
followed by a separate proof of the basin–trace equality <a href="#eq:basin-trace" data-reference-type="eqref" data-reference="eq:basin-trace">[eq:basin-trace]</a>. This separation prevents a conditional reconstruction from being reported as a source theorem.

# Current q79 Born status

## The exact canonical domain

The current q79 program closes a specific operational domain. For the canonical binary one-anchor recorder:

- the finite Hilbert/state/observable data and reduced dynamics are fixed;

- the commuting nondemolition Fock output algebra supplies the record events;

- the selected normal state emits the stopped output measure;

- second-moment capture descent is exact; and

- no separate Born axiom, stochastic primitive, observed probability, or numerical fit is added on that domain.

Thus equation <a href="#eq:basin-trace" data-reference-type="eqref" data-reference="eq:basin-trace">[eq:basin-trace]</a> has a selected operational realization for that binary apparatus context. This is stronger than the conditional Gleason-only status of the earlier paper.

## The quantifier boundary

The canonical result does not yet prove:

- the same descent for every allowed apparatus and preparation context;

- controlled corrections for finite-bandwidth or non-Markov detectors;

- a pre-quantum probability semantics, if one is demanded;

- or objective selection of one ontic history.

The correct status is therefore tiered:
``` math
\begin{array}{ll}
\text{canonical q79 binary one-anchor output law:}&\text{exact},\\
\text{universal physical apparatus family:}&\text{open},\\
\text{objective single-history actualization:}&\text{open}.
\end{array}
```

# Decoherence is not concentration

Let $`\mathcal{D}`$ be dephasing in a pointer decomposition. If
``` math
\frac12\|\rho-\mathcal{D}(\rho)\|_1\leq\delta,
```
then every effect $`0\leq E\leq\mathbf{1}`$ satisfies
``` math
\begin{equation}
\left|
\operatorname{Tr}(\rho E)-\operatorname{Tr}(\mathcal{D}(\rho)E)
\right|
\leq\delta.
\label{eq:decoherence-bound}
\end{equation}
```
This is the operational meaning of approximate decoherence for the declared effect family: coherences alter probabilities by at most $`\delta`$.

Equation <a href="#eq:decoherence-bound" data-reference-type="eqref" data-reference="eq:decoherence-bound">[eq:decoherence-bound]</a> does not imply that one diagonal weight is near one. The state
``` math
\frac12|0\rangle\langle0|
+\frac12|1\rangle\langle1|
```
is exactly decohered and maximally nonconcentrated on its two pointer records. Decoherence helps explain stable alternatives and suppression of interference ; a separate concentration estimate is needed for an approximately deterministic record.

# The finite classical concentration theorem

Let $`I`$ be a finite record set and let
``` math
p=(p_i)_{i\in I}
```
be a probability law. For a function $`f:I\to\mathbb{R}`$, define
``` math
\operatorname{osc}(f)=\max_{i\in I}f(i)-\min_{i\in I}f(i).
```

<div class="theorem">

**Theorem 1** (Classical concentration). *Suppose a record $`i_\star`$ satisfies
``` math
p_{i_\star}\geq1-\varepsilon
\qquad(0\leq\varepsilon\leq1).
```
Then
``` math
\begin{align}
d_{\mathrm{TV}}(p,\delta_{i_\star})
&=1-p_{i_\star}\leq\varepsilon,
\label{eq:tv}\\
\left|
\sum_{i\in I}p_i f(i)-f(i_\star)
\right|
&\leq\varepsilon\,\operatorname{osc}(f)
\label{eq:observable}
\end{align}
```
for every real function $`f`$ on $`I`$.*

</div>

<div class="proof">

*Proof.* Using the convention $`d_{\mathrm{TV}}(p,q)=\frac12\sum_i|p_i-q_i|`$,
``` math
d_{\mathrm{TV}}(p,\delta_{i_\star})
=\frac12\left(
1-p_{i_\star}+\sum_{i\neq i_\star}p_i
\right)
=1-p_{i_\star}.
```
Also,
``` math
\sum_i p_i f(i)-f(i_\star)
=\sum_{i\neq i_\star}
p_i\bigl(f(i)-f(i_\star)\bigr).
```
Taking absolute values and using $`|f(i)-f(i_\star)|\leq\operatorname{osc}(f)`$ gives <a href="#eq:observable" data-reference-type="eqref" data-reference="eq:observable">[eq:observable]</a>. ◻

</div>

This theorem gives an exact error budget for replacing the record law by the deterministic prediction $`i_\star`$. It does not say why $`p_{i_\star}`$ is large. That must follow from the preparation, dynamics, environment, control regime, or an MTT source theorem.

# Record persistence

Concentration at one time is not enough. A classical record should persist. Let $`X_0,X_1,\ldots`$ be a discrete-time record process on $`I`$. No Markov assumption is needed for the following conditional escape bound.

<div class="theorem">

**Theorem 2** (Finite-horizon persistence). *Assume
``` math
\Pr(X_0=i_\star)\geq1-\varepsilon
```
and, for every $`k<n`$,
``` math
\Pr\!\left(
X_{k+1}\neq i_\star
\mid X_0=\cdots=X_k=i_\star
\right)
\leq\eta.
```
Then
``` math
\begin{equation}
\Pr(X_0=\cdots=X_n=i_\star)
\geq(1-\varepsilon)(1-\eta)^n
\geq1-\varepsilon-n\eta.
\label{eq:persistence}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The chain rule for conditional probabilities gives the first inequality. Bernoulli’s inequality gives $`(1-\eta)^n\geq1-n\eta`$. Finally,
``` math
(1-\varepsilon)(1-n\eta)
\geq1-\varepsilon-n\eta.
```
 ◻

</div>

Equation <a href="#eq:persistence" data-reference-type="eqref" data-reference="eq:persistence">[eq:persistence]</a> separates two classicality controls:
``` math
\varepsilon
=\text{initial nonconcentration},
\qquad
\eta
=\text{per-step record escape}.
```
A useful classical regime requires both to be small over the physical observation horizon.

# How the two theorems fit together

<div class="center">

| Layer | Required object | What it establishes |
|:---|:---|:---|
| Alternatives | instrument effects and record algebra | available records |
| Probability source | selected state/measure and capture map | the values $`p_i`$ |
| Trace representation | additivity or effect noncontextuality | $`p_i=\operatorname{Tr}(\rho E_i)`$ |
| Decoherence | suppression of off-diagonal influence | classical mixture approximation |
| Concentration | $`p_{i_\star}\geq1-\varepsilon`$ | deterministic prediction with error $`\varepsilon`$ |
| Persistence | escape control $`\eta`$ | stable record over a finite horizon |
| Actualization | interpretation or additional dynamics | why one history is individually actual |

</div>

The same record labels and effects can appear in every row. That shared interface is the legitimate connection between the Born law and the classical limit. The logical arrows are not reversible. Concentration cannot derive the general Born weights, and a Born law need not be concentrated.

# A precise MTT completion target

To extend the canonical q79 result into a general Born-and-classical theorem, MTT must supply a family indexed by physical contexts $`c`$ and a classical regime parameter $`L`$:
``` math
\bigl(
\rho_{c,L},
\{\mathcal{I}_{i,c,L}\},
\mu_{c,L},
\{B_{i,c,L}\}
\bigr).
```
The required statements are:

1.  **Source equality.**
    ``` math
    \mu_{c,L}(B_{i,c,L})
    =\operatorname{Tr}(\rho_{c,L}E_{i,c,L})
    ```
    for every allowed context and outcome, with stated errors for nonideal detectors.

2.  **Concentration regime.** There is a selected $`i_\star(c,L)`$ and an explicit $`\varepsilon(c,L)\to0`$ such that
    ``` math
    \mu_{c,L}(B_{i_\star,c,L})\geq1-\varepsilon(c,L).
    ```

3.  **Persistence regime.** A derived escape bound $`\eta(c,L)`$ obeys
    ``` math
    n(L)\eta(c,L)\to0
    ```
    on the intended observation horizon.

4.  **Domain and interpretation.** The theorem states whether it is an operational record theorem only or also claims an ontic one-history law.

When these four rows are proved from the same selected source, the previous informal slogan can be replaced by a valid implication:
``` math
\begin{gathered}
\text{Born-compatible source law}\\
+\text{decoherence}\\
+\text{concentration}\\
+\text{persistence}
\end{gathered}
\Longrightarrow
\text{controlled classical record theory}.
```

# Consequences and non-consequences

The corrected separation yields several firm conclusions.

- Measurement can remain an ordinary physical interaction; no special conscious observer is needed in the mathematics.

- The current q79 binary recorder is a real advance over a purely conditional Gleason reconstruction.

- Classical behavior is quantitative: it comes with the three errors $`\delta`$, $`\varepsilon`$, and $`n\eta`$ for decoherence, concentration, and persistence.

- Exact decoherence does not imply a deterministic outcome.

- A sharply concentrated law does not explain the general Born rule.

- Operational probabilities do not, by themselves, select one ontic history.

- Projection can define record equivalence classes, but it does not create their measure.

The phrase “same problem” should therefore be retired. The two problems are adjacent stages of one physical workflow and can be tested on one common instrument, but their proof obligations remain distinct.

# Conclusion

Born probabilities and the classical limit share an outcome algebra, not a single theorem. A Born source theorem fixes the weights of records. Decoherence controls interference. Concentration makes one record approximately deterministic, and persistence keeps it stable. One-history actualization, if required, is another question.

MTT now closes more of this chain than version 1 reported correctly. The canonical q79 binary one-anchor Fock recorder has an exact stopped-output law and exact second-moment capture descent on its declared domain, without a fitted probability. The general apparatus family remains open. The classical concentration and persistence theorems proved here then state exactly what must be shown, after a valid record law exists, to obtain a controlled classical regime.

This separation is not a retreat from unification. It is the structure needed for a rigorous one: one source may eventually discharge several adjacent proof obligations, but none is counted as solved merely because the same record labels appear in all of them.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The concentration and persistence bounds are proved in this paper, while the general Born-source theorem remains open. The strict-upgrade ledger is included only as a current source-level boundary; it does not provide the missing outcome weights or select one realized history.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

A. M. Gleason, *Measures on the Closed Subspaces of a Hilbert Space*, Journal of Mathematics and Mechanics **6** (1957) 885–893, doi:10.1512/iumj.1957.6.56050.

C. M. Caves, C. A. Fuchs, K. Manne, and J. M. Renes, *Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements*, Foundations of Physics **34** (2004) 193–209, doi:10.1023/B:FOOP.0000019581.00318.a5, arXiv:quant-ph/0306179.

W. H. Zurek, *Decoherence and the Transition from Quantum to Classical—Revisited*, arXiv:quant-ph/0306072.

</div>
