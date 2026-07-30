# Program A2 v2 Revision Audit

## Selected source

- Paper: `The Modal Triplet Theory Program A2: Computation and Predictive Limits`
- Selected predecessor: v1.0
- Predecessor SHA-256: `4b72d576a13c75e79f613ce8c74eaefc8f37ee216397389ad622ac931ca82fb4`
- Controlling authority: A10
- Authority SHA-256: `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`
- Durable handoff: `744b6861-5267-45f2-90ef-1e67231b85ac`

## Required actions

1. **Conditionalize undecidability.** Resolved by
   Definition 7 and Theorem 8. Selection reachability is undecidable only if
   one selected MTT realization satisfies the six-clause robust uniform
   embedding contract for a universal two-counter machine.
2. **Do not infer computational irreducibility from non-Markovianity or finite
   capacity.** Resolved in Section 9. Non-Markovianity, undecidability,
   decision complexity, and stepwise simulation cost are separated.
3. **Reconcile unbounded counters with finite admissibility.** Resolved by the
   unbounded admissible-persistence clause (E3), Theorem 9, and its capacity
   obstruction corollary. A fixed finite carrier has decidable reachability.
4. **Separate undecidability, lower bounds, and full simulation.** Resolved in
   Sections 1 and 9 and in the scoped theorem.

## Additional contextual repairs

- Replaced the false no-global-predictive-map theorem by a typed reachability
  language.
- Restricted finite prediction depth to certified barriers along the declared
  continuations.
- Made refinement monotonicity conditional on a stepwise projection contract.
- Classified branching as underdetermination and chart termination as partial
  semantics rather than algorithmic undecidability.
- Narrowed the control no-go to a universal intervention-verifier consequence
  of the same reduction.
- Removed claimed derivations of quantization, probability, physical horizons,
  physical time, and irreversibility.
- Explicitly states that the earlier basin/record counter construction does not
  establish clauses (E1)--(E6) for a selected MTT realization.

## Resulting theorem chain

1. A computable admissible presentation defines a precise selection
   reachability language.
2. Recognizable termination or finite-state recurrence makes deterministic
   reachability decidable.
3. Certified barriers bound protocol-relative prediction depth.
4. Finite-depth branching remains algorithmically decidable.
5. A robust uniform universal two-counter embedding transfers halting
   undecidability to MTT selection reachability.
6. A fixed finite-capacity carrier cannot satisfy that embedding contract.

## Resulting scope

Program A2 v2 establishes finite prediction-depth diagnostics and an exact
conditional undecidability transfer theorem. It does not establish that a
selected physical MTT realization is computationally universal, that all MTT
trajectories are computationally irreducible, or that prediction limits derive
probability, quantization, physical time, horizons, irreversibility, or a
universal control obstruction.

## Expository revision

The current paper now opens with a paper-specific guide separating finite
prediction depth, branching, undefined continuation, undecidability,
complexity, and simulation cost in plain language. A bounded-counter toy
system gives a concrete case with finite depth and fully decidable
reachability. The argument map then shows why the six-clause robust
two-counter embedding is the decisive missing construction and why the
finite-capacity theorem is the complementary result.

## Verification

- The current source compiles with `pdflatex` to a 10-page PDF.
- The final log has no undefined references, underfull boxes, overfull boxes,
  or LaTeX/package warnings.
