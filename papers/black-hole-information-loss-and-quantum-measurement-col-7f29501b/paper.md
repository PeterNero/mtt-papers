---
abstract: |
  This paper develops a rigorous Modal Triplet Theory language for projected information, effective dynamics, and restricted recovery. An autonomous projected map exists exactly when the upper evolution preserves projection fibers; it is invertible exactly when the fiber equivalence is preserved in both time directions. Fiber splitting, effective merger, and restricted recovery are therefore distinct mechanisms. Quantum measurement is treated as an ordinary physical instrument followed by retention or loss of a record. Black-hole exterior restriction is a separate physical channel whose identification with an MTT admissibility boundary remains a model assumption. Island and entanglement-wedge results are represented by recovery on a code subspace or observable algebra, not by a partial right inverse between different state spaces. No common origin for Born and Hawking weights is claimed without an explicit measure and both pushforwards. The surviving MTT result is a rigorous language for projected information and recovery, together with a falsifiable source contract; it is not yet a solution of either the measurement problem or the black-hole information problem.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 6e5d29deb56f49389363232615d6288d1ff0f402d22c84d9313cc3e92495345d
paper_id: black-hole-information-loss-and-quantum-measurement-col-7f29501b
release_state: zenodo_released
released_version: v2
title: |
  Projected Information Loss in Modal Triplet Theory:
  Fiber Dynamics, Measurement Channels, and the Black-Hole Recovery Boundary
zenodo_doi: 10.5281/zenodo.21665948
zenodo_record_id: 21665948
zenodo_url: "https://zenodo.org/records/21665948"
---

# Version 2 Revision Note

Supersedes:
The first release under the former equivalence title.

Reason:
The former right-inverse bridge conflated quotient dynamics, fiber overlap, and code-restricted recovery.

Resolution:
The paper now proves the exact fiber-factorization and invertibility criteria and treats measurement, exterior restriction, and island recovery as distinct physical channels.

Retained result:
MTT supplies a rigorous language for projected information and recovery once the projection and dynamics are specified.

Remaining boundary:
A selected black-hole channel, code/algebra recovery map, and common source for any Born/Hawking comparison remain open.

# Correction, purpose, and reader map

The useful idea behind the first version was that invertible microscopic dynamics can look irreversible after information is discarded. That statement is true, but the old theorem did not prove it. It confused four different questions:

1.  whether an observable state determines its own future;

2.  whether two observable states later merge;

3.  whether a microscopic state can be recovered from a restricted record; and

4.  whether a recovery channel exists on a protected code.

Sections 2 and 3 separate those questions in elementary quotient language. Section 4 translates the result into quantum channels and treats measurement as an ordinary interaction with an apparatus and record. Section 5 states what the island literature actually supports. Sections 6 and 7 explain why the two applications are an analogy, not one proved physical process. Section 8 gives the MTT exit contract. The following steps therefore move from exact set-level dynamics, to physical channel typing, and only then to the two proposed applications.

## The central picture in plain language

A projection groups many upper states into one observable state. Those groups are its *fibers*. If upper evolution carries every fiber into a single later fiber, the observable state has an autonomous future. If one old fiber splits across several later fibers, the observable state lacks enough memory to determine that future. If distinct observable fibers merge, an autonomous future may exist but cannot be inverted. A larger record can sometimes undo the apparent loss.

This picture applies to many physical processes, including ordinary coarse-graining. It does not make measurement metaphysically special. Nor does it identify a detector interaction with an evaporating black hole. Physical equivalence requires the actual channels, states, observables, and probabilities to be constructed in both cases.

# Projected dynamics: the exact theorem

Let $`\mathcal X`$ and $`\mathcal Y`$ be sets, let $`P:\mathcal X\to\mathcal Y`$ be a surjective observation map, and let $`\Phi:\mathcal X\to\mathcal X`$ be a bijective microscopic time step. Define the fiber equivalence relation
``` math
x\sim_P x'
 \quad\Longleftrightarrow\quad
 P(x)=P(x').
```
The observable question is whether there is a map $`F:\mathcal Y\to\mathcal Y`$ satisfying
``` math
\begin{equation}
 F\circ P=P\circ\Phi.
 \label{eq:factor}
\end{equation}
```

<div id="thm:factor" class="theorem">

**Theorem 1** (Projected-dynamics factorization). *There is a unique $`F:\mathcal Y\to\mathcal Y`$ satisfying <a href="#eq:factor" data-reference-type="eqref" data-reference="eq:factor">[eq:factor]</a> if and only if
``` math
x\sim_P x'
 \quad\Longrightarrow\quad
 \Phi(x)\sim_P\Phi(x').
 \tag{2.2}
```
When it exists, $`F`$ is bijective if and only if
``` math
x\sim_P x'
 \quad\Longleftrightarrow\quad
 \Phi(x)\sim_P\Phi(x').
 \tag{2.3}
```*

</div>

<div class="proof">

*Proof.* If $`F`$ exists and $`P(x)=P(x')`$, then $`P\Phi(x)=FP(x)=FP(x')=P\Phi(x')`$. Conversely, if (2.2) holds, define $`F(y)=P\Phi(x)`$ for any $`x`$ with $`P(x)=y`$. The condition makes this definition independent of the representative, and surjectivity of $`P`$ gives uniqueness.

Assume now that $`F`$ exists. It is injective exactly when $`P\Phi(x)=P\Phi(x')`$ implies $`P(x)=P(x')`$, which is the reverse implication in (2.3). It is surjective because for any $`y=P(x)`$, bijectivity of $`\Phi`$ gives $`x=\Phi(z)`$ and hence $`y=P\Phi(z)=F(Pz)`$. Thus (2.3) is equivalent to bijectivity. ◻

</div>

#### What this means.

Noninjectivity of $`P`$ is not enough to produce irreversible observable dynamics. The decisive issue is how $`\Phi`$ acts on the fiber partition. This is the exact replacement for the old barrier theorem.

<div id="cor:counter" class="corollary">

**Corollary 2** (Noninjective projection can have reversible shadows). *Let $`\mathcal X=\mathcal Y\times Z`$, let $`P(y,z)=y`$, and let $`\Phi(y,z)=(f(y),g(z))`$ for bijections $`f`$ and $`g`$. Then $`P`$ is noninjective when $`Z`$ has more than one point, yet the projected dynamics exists and equals the bijection $`F=f`$.*

</div>

<div class="proof">

*Proof.* Equation <a href="#eq:factor" data-reference-type="eqref" data-reference="eq:factor">[eq:factor]</a> is immediate. ◻

</div>

For example, take $`\mathcal Y=Z=\{0,1\}`$, let $`f`$ flip the first bit and let $`g`$ flip the second. The four upper states project to two observable states. Although each observable state hides one bit, its observed evolution is the perfectly reversible flip $`0\leftrightarrow1`$. This finite example shows why information hidden inside a fiber is not the same as information destroyed by the effective time step.

# Three mechanisms that must not be conflated

## Fiber splitting: no autonomous shadow

Fiber splitting occurs when $`P(x)=P(x')`$ but $`P\Phi(x)\neq P\Phi(x')`$. By Theorem <a href="#thm:factor" data-reference-type="ref" data-reference="thm:factor">1</a>, no deterministic $`F:\mathcal Y\to\mathcal Y`$ can represent the next observable state. This is not yet fundamental stochasticity. It says that $`\mathcal Y`$ omitted a variable on which the future depends. Enlarging the observable state to include a memory record may restore closure.

## Effective merger: autonomous but noninvertible

Suppose fiber preservation holds, so $`F`$ exists, but two distinct observable states $`y\neq y'`$ satisfy $`F(y)=F(y')`$. Then the shadow is autonomous and noninvertible. This is an effective merger. The microscopic map $`\Phi`$ can remain bijective because the distinguishing information survives elsewhere inside $`\mathcal X`$.

## Restricted recovery: information in a larger record

Recovery is a third question. For a map $`T:\mathcal X\to\mathcal Y`$, a right inverse $`S:\mathcal Y\to\mathcal X`$ satisfying $`T\circ S=\mathrm{Id}_\mathcal Y`$ merely chooses one representative from each observed fiber. It does not satisfy $`S(Tx)=x`$ for every microscopic state. Exact microscopic recovery would require a left inverse on the states of interest.

<div id="prop:disjoint" class="proposition">

**Proposition 3** (Invertible flow preserves disjointness). *If $`\Phi:\mathcal X\to\mathcal X`$ is injective and $`U_+\cap U_-=\varnothing`$, then
``` math
\Phi(U_+)\cap\Phi(U_-)=\varnothing.
```*

</div>

<div class="proof">

*Proof.* An element in the intersection would equal both $`\Phi(x_+)`$ and $`\Phi(x_-)`$. Injectivity would imply $`x_+=x_-`$, contradicting disjointness. ◻

</div>

The condition $`\Phi(U_+)\cap\Phi(U_-)\neq\varnothing`$ used in the first edition was therefore incompatible with its own assumption that $`\Phi`$ was invertible.

# Quantum channels and ordinary physical measurement

The correct quantum language is a channel or instrument, not a set-theoretic right inverse. Let $`\{\mathcal I_a\}_a`$ be a completely positive instrument. For an input state $`\rho`$,
``` math
p(a|\rho)=\operatorname{Tr}\mathcal I_a(\rho),
 \qquad
 \rho_a=\frac{\mathcal I_a(\rho)}{p(a|\rho)}
```
when $`p(a|\rho)>0`$. The outcome-forgetting process is the channel
``` math
\mathcal E(\rho)=\sum_a\mathcal I_a(\rho).
```
This is the standard operational description of a physical system interacting with an apparatus and leaving a classical or quantum record .

Nothing in this formalism gives measurement a privileged role in fundamental dynamics. Conditioning on the record and discarding the record are different physical data flows. The normalized update $`\rho\mapsto\rho_a`$ is outcome-conditioned, while the unconditioned system-plus-apparatus evolution may be represented unitarily before a subsystem is ignored.

<div class="definition">

**Definition 4** (Exact recovery on a code). A channel $`\mathcal E`$ is exactly recoverable on a set of states $`\mathcal C`$ if a channel $`\mathcal R`$ exists such that
``` math
\mathcal R\!\circ\mathcal E(\rho)=\rho
 \qquad\text{for every }\rho\in\mathcal C.
```

</div>

<div class="proposition">

**Proposition 5** (Collision obstruction to recovery). *If $`\rho,\sigma\in\mathcal C`$ are distinct and $`\mathcal E(\rho)=\mathcal E(\sigma)`$, then no exact recovery channel exists on $`\mathcal C`$.*

</div>

<div class="proof">

*Proof.* Applying a putative $`\mathcal R`$ to the common output would have to return both $`\rho`$ and $`\sigma`$. ◻

</div>

This is the correct sense in which discarded measurement records can obstruct recovery. It is also the right type for comparing restricted black-hole reconstruction, provided the physical channel and code are specified.

## Born weights are not basin weights by declaration

The probabilities of an instrument are fixed by $`p(a|\rho)=\operatorname{Tr}\mathcal I_a(\rho)`$. An MTT basin measure would derive these weights only if it supplied an upper probability measure $`\mu_\rho`$, an outcome map $`M`$, and a theorem
``` math
(M_*\mu_\rho)(a)
 =\operatorname{Tr}\mathcal I_a(\rho)
```
for the declared class of states and apparatuses. No such universal source theorem is established by the projection formalism alone.

# Black-hole exterior channels and islands

## The horizon identification is an additional model

Semiclassical Hawking radiation follows from quantum fields on a black-hole background and has a thermal late-time spectrum in the appropriate approximation . To represent exterior restriction as an MTT projection, one must construct:

1.  the selected black-hole geometry and quantum state;

2.  the interior, exterior, and radiation observable algebras;

3.  a restriction or noise channel $`\mathcal E_{\mathrm{ext}}`$;

4.  the MTT upper state space and map that realize that channel; and

5.  the evaporation-time evolution and its domain.

Calling a horizon an “admissibility barrier” does not supply these objects. It remains a physical modeling hypothesis.

## What island results support

In controlled holographic and semiclassical models, quantum extremal surfaces and island formulas reproduce a Page curve and place part of the interior in the entanglement wedge of the radiation . Entanglement-wedge reconstruction is naturally expressed in quantum-error-correction or operator-algebra language .

The corresponding typed statement is:
``` math
\mathcal R_{\mathrm{rad}}\circ\mathcal E_{\mathrm{rad}}
 \simeq \mathrm{Id}
 \quad\text{on a declared code or observable algebra}.
```
It is not a partial right inverse from the radiation state space to the full microscopic black-hole state space. The code, accuracy, state dependence, observable algebra, and semiclassical regime matter.

The Page curve is powerful entropy evidence for information-preserving evaporation in the models where the island prescription is derived. It does not by itself construct the complete microscopic dynamics of a general four-dimensional evaporating black hole, and it does not select an MTT projection.

# The surviving analogy and its limit

Measurement and black-hole restriction can share an abstract pattern:
``` math
\text{larger state}
 \longrightarrow
 \text{restricted record}
 \longrightarrow
 \text{possible recovery on a code}.
```
That is a channel-theoretic analogy. The physical mechanisms differ:

- measurement uses a specified system–apparatus interaction and an outcome instrument;

- black-hole radiation uses quantum fields, dynamical geometry, horizon or asymptotic algebras, and gravitational entropy prescriptions;

- their state spaces, observables, time scales, and recovery criteria are not the same; and

- neither process needs fundamental microscopic nonunitarity.

The revised claim is therefore narrower and stronger: MTT offers a common fiber/channel language in which both problems can be posed, but it has not proved that they instantiate one selected transition.

# Born and Hawking probabilities: the source boundary

A claim that two probability laws come from one upper measure has mathematical content only after one supplies a single measurable probability space $`(\mathcal X,\mu)`$ and two declared maps
``` math
M:\mathcal X\to\mathcal A,
 \qquad
 H:\mathcal X\to\mathcal R,
```
such that
``` math
M_*\mu=p_{\mathrm{Born}},
 \qquad
 H_*\mu=p_{\mathrm{Hawking}}
```
for nontrivial families of preparations and backgrounds. Merely observing that every probability distribution can be written as some pushforward does not relate the two laws.

Moreover, Born probabilities depend on the prepared quantum state and instrument, while Hawking weights depend on geometry, field content, quantum state, and observer/asymptotic mode definitions. A common MTT source would have to emit all these dependencies and their normalization. The current corpus does not yet do so.

# Selected MTT exit contract

To promote the surviving analogy into a physical MTT theorem, one compatible source chain must supply:

1.  an upper state space, dynamics, and observable projection with the fiber conditions of Theorem <a href="#thm:factor" data-reference-type="ref" data-reference="thm:factor">1</a>;

2.  a derived quantum instrument for a concrete measurement apparatus, including its Born probabilities;

3.  a selected black-hole geometry, exterior/radiation channel, and semiclassical limit;

4.  a declared code subspace or observable algebra for recovery;

5.  an explicit recovery channel with an exactness or error certificate;

6.  a common probability source only if both Born and Hawking pushforwards are actually computed; and

7.  at least one prediction not inserted through the target instrument, geometry, or radiation law.

Current MTT fixed-point and projection results help organize item 1. The corrected quantum-gravity program has not yet completed items 2–6 for this pair of applications.

# Version delta

Relative to version 1, this successor:

- deletes the invalid right-inverse bridge proof;

- proves the exact fiber-factorization and invertibility theorem;

- proves that an invertible flow preserves disjointness;

- separates fiber splitting, effective merger, and restricted recovery;

- treats measurement as an ordinary physical quantum instrument;

- treats the horizon/admissibility identification as a model assumption;

- replaces “islands as partial inverses” by recovery on a code or observable algebra;

- withdraws the measurement–island equivalence theorem; and

- withdraws a common origin for Born and Hawking weights until both pushforwards are constructed.

# Conclusion

The first edition reached for a deep connection but promoted an analogy into a theorem too early. The correction leaves a useful and exact result. Projected dynamics is autonomous precisely when upper evolution preserves projection fibers, and it is reversible precisely when that equivalence is preserved in both directions. Apparent loss can then arise through missing memory, effective merger, or restriction to a smaller record, while recovery must be stated on a declared code.

This framework cleanly accommodates ordinary physical measurement and the modern channel interpretation of black-hole reconstruction without declaring them identical. The next scientific step is not another verbal bridge. It is to emit one concrete MTT measurement instrument or one concrete black-hole exterior/recovery channel, with provenance and numerical or operator-level checks. Only then can the proposed common architecture become a physical result.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The channel, recovery, and information-loss statements in this paper are operator-theoretic. The mapped strict-upgrade ledger supplies no black-hole recovery theorem and is cited only to prevent later Standard Model closure claims from being read into this analysis.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

E. B. Davies and J. T. Lewis, *An operational approach to quantum probability*, Commun. Math. Phys. **17** (1970), 239–260, doi:10.1007/BF01647093.

M. Ozawa, *Quantum measuring processes of continuous observables*, J. Math. Phys. **25** (1984), 79–87, doi:10.1063/1.526000.

S. W. Hawking, *Particle creation by black holes*, Commun. Math. Phys. **43** (1975), 199–220, doi:10.1007/BF02345020.

G. Penington, *Entanglement wedge reconstruction and the information paradox*, JHEP **09** (2020), 002, doi:10.1007/JHEP09(2020)002, arXiv:1905.08255.

A. Almheiri, R. Mahajan, J. Maldacena, and Y. Zhao, *The Page curve of Hawking radiation from semiclassical geometry*, JHEP **03** (2020), 149, doi:10.1007/JHEP03(2020)149, arXiv:1908.10996.

A. Almheiri, X. Dong, and D. Harlow, *Bulk locality and quantum error correction in AdS/CFT*, JHEP **04** (2015), 163, doi:10.1007/JHEP04(2015)163, arXiv:1411.7041.

X. Dong, D. Harlow, and A. C. Wall, *Reconstruction of bulk operators within the entanglement wedge in gauge-gravity duality*, Phys. Rev. Lett. **117** (2016), 021601, doi:10.1103/PhysRevLett.117.021601, arXiv:1601.05416.

</div>
