---
abstract: |
  A projection can identify source states that an effective description no longer distinguishes. This observation is useful, but it is not by itself a theory of information, computation, complexity, or undecidability. Information quantities require a state or probability law and a specified channel; computation requires an encoding, evolution rule, readout, and resource model; undecidability requires an unbounded problem family and an explicit reduction from a known undecidable problem. This paper gives a projection-first account of these layers. Classical and quantum data-processing inequalities formalize loss of distinguishability under channels, while recovery maps state when the loss can be reversed on a selected family of states. Noninvertibility alone does not imply entropy production, an arrow of time, computational hardness, or undecidability. For Modal Triplet Theory, finite selected operators supply concrete descriptive channels, but a physical undecidability theorem remains open until a uniform computational embedding is constructed.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 2c36ed8c18f7fd80df5f3d8611e3ded36fa0b7c36981e2a1cc5027c5f1b00f3e
paper_id: a-projection-first-reframing-of-information-computation-dab93645
release_state: zenodo_released
released_version: v2
title: |
  A Projection-First Reframing of Information and Computation:
  Distinguishability, Channels, and Conditional Undecidability
zenodo_doi: 10.5281/zenodo.21665930
zenodo_record_id: 21665930
zenodo_url: "https://zenodo.org/records/21665930"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *A Projection-First Reframing of Information, Computation, and Undecidability*.

The original paper inferred information loss, complexity, and generic undecidability directly from projection and finite admissibility. Those implications do not hold without further probabilistic, dynamical, and computational structures.

Projection is now typed as a channel only after a state space is supplied. Information loss is formulated through data processing and recovery. Computation and undecidability are made conditional on explicit encodings, resource models, and reductions.

Projection-first language remains useful for separating source distinctions from distinctions available to an effective observer.

MTT still needs a selected uniform computational embedding, together with a proved reduction, before it can claim a new physical undecidability result.

</div>

# Scope

Let
``` math
\pi:X\longrightarrow Y
```
map a richer source description to an effective one. If $`\pi(x)=\pi(x')`$, the effective variable does not distinguish $`x`$ from $`x'`$. This is a statement about an equivalence relation induced by $`\pi`$. It is not yet a statement about entropy, information flow, memory, or computation.

Those notions belong to different mathematical categories. A probability distribution is required before Shannon entropy is defined. A density operator and observable algebra are required before quantum information is defined. An input language and an algorithmic model are required before computability or complexity is defined. The purpose of this paper is to retain the useful projection-first intuition while making those additional structures explicit.

# From a map to an information channel

## Classical distinguishability

Suppose $`X`$ is a random variable with distribution $`p`$, and let $`Y=\pi(X)`$. The deterministic map induces a stochastic channel
``` math
K(y\mid x)=
 \begin{cases}
 1,&y=\pi(x),\\
 0,&\text{otherwise}.
 \end{cases}
```
Only now are Shannon entropy and mutual information defined. For a deterministic channel on finite alphabets,
``` math
H(Y)\leq H(X).
```
The inequality describes the chosen random variables and their law. It is not a property of the bare set map independent of $`p`$.

A more robust statement compares two candidate source laws $`p`$ and $`q`$. For any stochastic channel $`K`$, the classical data-processing inequality gives
``` math
D(Kp\Vert Kq)\leq D(p\Vert q),
```
where $`D`$ is relative entropy. Operationally, processing cannot improve the ability to distinguish $`p`$ from $`q`$. A projection therefore supports an information-loss interpretation only relative to specified states and an observation channel.

## Quantum distinguishability

In quantum theory the corresponding object is a completely positive, trace-preserving map
``` math
\mathcal E:\mathcal T(\mathcal H_X)\longrightarrow
 \mathcal T(\mathcal H_Y).
```
Quantum relative entropy obeys
``` math
D(\mathcal E(\rho)\Vert\mathcal E(\sigma))
 \leq D(\rho\Vert\sigma).
```
A finite projector $`P`$ does not by itself define this channel on all states. One must specify, for example, whether the operation is a selected outcome, the nonselective instrument
``` math
\rho\longmapsto P\rho P+(I-P)\rho(I-P),
```
or a compression followed by normalization. These operations have different physical meanings.

# Loss, recovery, and irreversibility

Information being unavailable in $`Y`$ does not imply that it was destroyed in $`X`$. A section $`s:Y\to X`$ satisfying $`\pi s=I_Y`$ merely chooses one representative from each fiber. It does not recover the original $`x`$ from $`\pi(x)`$.

For a channel $`\mathcal E`$, recovery on a selected state family $`\mathcal S`$ requires another channel $`\mathcal R`$ such that
``` math
\mathcal R\mathcal E(\rho)=\rho
 \qquad(\rho\in\mathcal S),
```
or an explicit norm or fidelity error bound. Equality in suitable data-processing inequalities is tied to such sufficient or recoverable families; approximate equality motivates quantitative recovery estimates .

This distinction prevents three common overclaims.

1.  A many-to-one description can coexist with reversible lower dynamics.

2.  Entropy need not increase along a trajectory unless a state, coarse-graining rule, and dynamical law make it do so.

3.  Memory effects require a history-dependent reduced law, hidden variables, or a non-Markovian channel; they do not follow from noninjectivity alone.

Physical irreversibility therefore needs a semigroup, dissipative generator, boundary condition, growing recovery error, or another time-directed structure. Projection can explain which distinctions are discarded, but not by itself why their loss is dynamically irreversible.

# What makes a physical process a computation?

A computational interpretation needs at least a tuple
``` math
(\mathcal I,E,\Phi_t,R,\mathcal O),
```
where $`\mathcal I`$ is an input language, $`E`$ encodes inputs into physical states, $`\Phi_t`$ evolves those states, $`R`$ reads an output, and $`\mathcal O`$ specifies the output convention. Complexity additionally requires an input-size function, an error tolerance, and a resource cost such as time, memory, energy, or circuit depth.

Projection may enter this tuple in several useful ways. It can define a readout, compress inaccessible variables, or identify physically equivalent encodings. It can also make a chosen decoding problem ill posed. None of these facts alone establishes that the underlying task is algorithmically hard. A constant map is maximally noninjective but trivial to compute. Conversely, an injective map may be expensive to evaluate.

The phrase “the universe computes” is therefore optional interpretation, not a mathematical consequence. The precise question is whether a physical family implements a named input-output problem with controlled errors and resources.

# Undecidability requires a reduction

Undecidability is stronger than practical unpredictability, chaos, or an expensive numerical calculation. A decision problem is undecidable when no algorithm halts with the correct answer for every input in a specified unbounded family.

A physical undecidability proof consequently needs:

1.  a recursively describable family of physical instances $`M_w`$;

2.  a decision predicate $`Q(M_w)`$;

3.  an effective map from instances $`w`$ of a known undecidable problem;

4.  a proof that $`Q(M_w)`$ answers that problem; and

5.  robustness conditions showing that the encoding belongs to the claimed physical class.

This is the pattern used in genuine many-body undecidability results: a Hamiltonian family is constructed so that its spectral-gap behavior encodes the halting problem .

By contrast, the following do not prove undecidability:

- a projection being many-to-one;

- a finite stability margin;

- sensitivity to initial data;

- a simulation taking a long time;

- not knowing in advance whether a numerical solver will converge; or

- one fixed finite matrix having a complicated spectrum.

A fixed finite exact model is, in principle, exhaustively decidable for finite predicates. Undecidability can enter only through a uniform unbounded family, an infinite-volume limit, an exact real-number oracle, or another explicitly stated source of unbounded computation.

# Consequences for Modal Triplet Theory

MTT currently supplies several concrete finite descriptive structures: selected projectors, finite Hessian blocks, a $`27\times27`$ finite carrier at its declared Standard-Model profile tier, and selected free-field operator data. These can be studied as channels once states and instruments are specified. Their finite nature is an advantage for reproducibility, but it does not support a new undecidability claim.

A serious MTT computational program has two distinct branches.

#### Finite branch.

Specify the state, selected instrument, readout, and error metric for each finite operator. Then compute distinguishability loss, recovery fidelity, spectral conditioning, and algorithmic cost. This can produce exact or certified numerical results without invoking undecidability.

#### Uniform branch.

Construct a family indexed by words, lattice size, cutoff, bundle data, or another recursive parameter. Prove that the family preserves the selected MTT constraints and embeds a universal computation. Only then should a halting, reachability, spectral, or admissibility predicate be tested for an undecidability reduction.

The second branch is open. It may succeed, but projection and admissibility do not replace the construction.

# Claim ledger

<div class="center">

| Claim | Status | Required structure or qualification |
|:---|:---|:---|
| $`\pi`$ identifies source states | Exact | A defined map $`X\to Y`$. |
| Projection reduces distinguishability | Conditional | State family and classical or quantum channel. |
| Data processing gives monotonicity | Standard result | Relative entropy and an admissible stochastic or CPTP map. |
| Projection destroys information | Not implied | Must exclude source access and recovery on the selected family. |
| Projection creates irreversibility | False in general | Needs directed dynamics, boundary data, or recovery-error growth. |
| Projection creates computational hardness | False in general | Needs a problem encoding and resource model. |
| Finite MTT operators are undecidable | Not established | A fixed finite instance is not an undecidable family. |
| MTT admits physical undecidability | Open | Uniform selected family and an explicit reduction. |

</div>

# Discussion

The corrected projection-first view is narrower than the original one, but more useful. Projection says which distinctions survive a change of description. Information theory quantifies those distinctions after a state and channel are supplied. Recovery theory tests whether the loss is reversible on a chosen family. Computation theory asks whether a controlled encoding and readout implement a problem. Undecidability appears only when an unbounded family carries a proved reduction.

This hierarchy also clarifies black-hole and measurement language. Tracing out a region, conditioning on an outcome, recording an apparatus state, and losing access to a source are different channels. Calling all of them “projection” can hide the very mechanism under study. MTT should therefore name the channel and recovery criterion in each application.

# Conclusion

Projection-first reasoning does not make information, computation, or undecidability inevitable. It gives a disciplined starting point: identify the source states, the effective states, and the distinctions that the map forgets. The next layers must then be built explicitly.

For MTT, the immediate rigorous opportunity is finite and quantitative: turn selected projectors and operators into specified channels and compute their distinguishability and recovery properties. A new undecidability result would be a later theorem, requiring a recursive physical family and a genuine computational reduction.

<div class="thebibliography">

9

C. E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal **27** (1948), 379–423, 623–656.

A. M. Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society **42** (1936), 230–265.

D. Petz, *Sufficient Subalgebras and the Relative Entropy of States of a von Neumann Algebra*, Communications in Mathematical Physics **105** (1986), 123–131.

D. Sutter, M. Tomamichel, and A. W. Harrow, *Strengthened Monotonicity of Relative Entropy via Pinched Petz Recovery Map*, IEEE Transactions on Information Theory **62** (2016), 2907–2913.

T. S. Cubitt, D. Pérez-García, and M. M. Wolf, *Undecidability of the Spectral Gap*, Nature **528** (2015), 207–211.

J. Bausch, T. S. Cubitt, A. Lucia, and D. Pérez-García, *Undecidability of the Spectral Gap in One Dimension*, Physical Review X **10** (2020), 031038.

</div>
