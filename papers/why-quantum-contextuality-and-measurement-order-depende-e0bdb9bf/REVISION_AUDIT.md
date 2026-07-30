# Revision Audit: Contextuality and Sequential Measurement Order

## Release Decision

- Current source: Version 2, July 2026.
- Supersedes: Version 1, January 2026.
- Review class: central-theorem withdrawal and exact separation.
- Intended tier: standard instrument formalism, exact finite-dimensional counterexamples, and a conditional MTT construction contract.
- Not a proof that contextuality and order dependence are equivalent.

## Defects Corrected

1. Version 1 identified Kochen-Specker contextuality and sequential order dependence as the same phenomenon.
2. Its `Contextuality--Order Shadow Bridge` did not prove either implication.
3. It used failure of a common basin refinement both as a static valuation obstruction and as dynamic noncommutation without a typed map between those structures.
4. It did not state the instrument algebra needed to compute sequential probabilities.
5. It treated projective contextuality, generalized operational contextuality, observable incompatibility, weak measurement, and disturbance as interchangeable.
6. It imported a general basin-measure Born theorem that is not established by current MTT results.
7. It described the construction as fully formal despite the missing selected apparatus family and naturality theorem.

## Imported Quantum Framework

For an instrument `{I_i^A}` with effects `E_i^A = I_i^{A*}(1)`,

```text
p(i | A, rho) = Tr[I_i^A(rho)] = Tr[rho E_i^A].
```

Sequential joint probabilities require the maps, not only the effects:

```text
p_A->B(i,j | rho) = Tr[I_j^B(I_i^A(rho))].
```

Primary references checked:

- S. Kochen and E. P. Specker, *The Problem of Hidden Variables in Quantum Mechanics*, Journal of Mathematics and Mechanics 17 (1967), 59-87, DOI 10.1512/iumj.1968.17.17004.
- E. B. Davies and J. T. Lewis, *An Operational Approach to Quantum Probability*, Communications in Mathematical Physics 17 (1970), 239-260, DOI 10.1007/BF01647093.
- R. W. Spekkens, *Contextuality for Preparations, Transformations, and Unsharp Measurements*, Physical Review A 71 (2005), 052108, DOI 10.1103/PhysRevA.71.052108.
- S. Abramsky and A. Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*, New Journal of Physics 13 (2011), 113036, DOI 10.1088/1367-2630/13/11/113036.

## Exact Results Owned by Version 2

### Qubit order-effect counterexample

For `rho = |0><0|`, the Lueders instruments for the `z` and `x` projective measurements give

```text
p(z+ then x+) = 1/2,
p(x+ then z+) = 1/4.
```

This is an exact order effect in dimension two. It does not imply that generalized Spekkens contextuality is absent for qubits. It shows that ordinary sequential order dependence does not imply the original projective Kochen-Specker obstruction.

### Same effects, different sequential behavior

The Lueders instrument

```text
L_i(rho) = P_i rho P_i
```

and the measure-and-prepare instrument

```text
M_i(rho) = Tr(P_i rho) sigma_i
```

have the same effects `P_i` and the same one-step probabilities for every input. With `rho = P_0`, `sigma_0 = |+><+|`, and a later `P_0` test, their probabilities are respectively `1` and `1/2`.

Therefore compatibility, effect, or valuation data alone cannot determine a sequential order law.

## Current MTT Status Used

The current q79 result closes the stopped-output law and exact second-moment capture descent for the canonical binary one-anchor nondemolition Fock recorder on its declared domain. It adds no separate Born axiom, fitted probability, observed probability, or stochastic primitive there.

This result supplies one selected instrument-and-measure domain. It does not provide:

- a Kochen-Specker family of overlapping compatible contexts;
- a context-independent identification of shared events;
- all corresponding apparatus instruments from one source;
- arbitrary-context Born descent;
- or a contextuality--order comparison theorem.

Controlling current objects:

- `B.QM.01`: exact canonical recorder result, open for arbitrary apparatus contexts and stronger source/actualization demands.
- `ENC.QM.BORN`: mixed L3 status, exact only on the declared canonical domain.
- paper audit overlays `A03`, `A05`, `A10`, and `A18`, used only within their stated scopes.

## MTT Construction Contract

A genuine common-source theorem must construct:

1. one selected upper state space and source law;
2. a cover of compatible measurement contexts;
3. context-indexed physical record maps;
4. fully specified context-indexed CP instruments;
5. intertwiners deriving those instruments from the upper dynamics;
6. pushforward identities for every context;
7. sequential composition identities; and
8. a sound, typed map from the global-section obstruction to an instrument-composition obstruction.

Equivalence additionally requires completeness. The qubit counterexample shows that completeness cannot hold for all sequential instruments, so any future theorem must restrict the selected instrument family.

## Claims Explicitly Not Made

- Contextuality and order dependence are not declared equivalent.
- Noncommuting observables are not identified with contextuality.
- Instrument disturbance is not identified with Kochen-Specker contextuality.
- A basin partition does not determine a state-update map.
- Projection alone does not supply a Born measure.
- One binary apparatus does not establish contextuality.
- Contextuality does not imply observer-created reality or the failure of every realist theory.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 2 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- External primary references checked.
- The old central equivalence theorem is withdrawn, not duplicated.
- Current q79 results are reported by tier and not reproduced as theorem bodies.
- LaTeX compiles without unresolved references, overfull boxes, or underfull boxes.
- PDF must be visually inspected page by page before freezing.
