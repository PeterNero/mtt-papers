# Program B3 revision audit

## Selected revision

- Paper: `The Modal Triplet Theory Program B3`
- Superseded source: version 1.0
- Superseded source SHA-256: `2023954f859998ed1d26b2b5db66d7b899af95444994ae21344c661d3e7f3412`
- Selected successor: version 2
- Controlling correction authority: `A10`
- A10 SHA-256: `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`

## Context audit

Version 1 was checked against the selected Program A0 and B0-B2 revisions,
the current typed quantum-reconstruction boundary, and standard differential
topology, spectral theory, and operator-algebraic quantum mechanics. The old
paper correctly observed that discrete constraints can survive where one
continuous description fails and correctly denied that discreteness alone
assigns probabilities. It nevertheless inferred discreteness directly from a
nil boundary and identified that broad phenomenon too closely with
quantization.

## Required corrections

### 1. Nil termination does not by itself collapse continuous families

**Prior claim:** If a continuation encounters a nil obstruction, all
continuous descriptive families collapse and only isolated survivors can
remain.

**Finding:** Failure of one chart or decoder to extend is compatible with a
continuous upper domain and continuous neighboring descriptions. Discreteness
requires a separate constraint, quotient, transversality, compactness, or
spectral hypothesis.

**Resolution:** Version 2 gives an explicit continuous counterexample, defines
a typed nil profile relative to a map, domain, category, and extension class,
and introduces a separate survivor datum.

**Status:** Resolved.

### 2. Discrete survivors require an actual dimension/rank theorem

**Prior claim:** Refinement stability forces isolated discrete survivors.

**Finding:** Informal refinement does not determine dimension or isolation. A
regular zero set of `r` constraints on an `n`-manifold has dimension `n-r`.
It is discrete only in the zero-dimensional case, and compactness is needed to
make it finite.

**Resolution:** Version 2 proves the regular-value survivor theorem and the
compact transverse finite-survivor corollary. Local robustness is stated with
the implicit-function theorem and an invertible derivative.

**Status:** Resolved.

### 3. Discrete structure is not unique to quantum mechanics

**Prior claim:** The discrete constraint encoding is the unique response to nil
and is what quantization is.

**Finding:** Finite deterministic systems, Morse critical sets, symbolic
labels, and topological winding sectors all generate discrete survivors or
labels without complex quantum mechanics. Topological sectors can also retain
continuous moduli inside each discrete class.

**Resolution:** Version 2 presents these classical countermodels and
reclassifies the MTT construction as a broad discrete survivor filter rather
than a unique quantum theorem.

**Status:** Resolved.

### 4. Spectral discreteness is independent of topological discreteness

**Prior claim:** Discrete spectra, charges, and topological quantum numbers are
all direct realizations of the same nil-forced discreteness.

**Finding:** A discrete spectrum is a theorem about a declared operator and its
domain. A topological sector is a homotopy or component label. Neither implies
the other.

**Resolution:** Version 2 states the self-adjoint compact-resolvent theorem and
lists all of its imported hypotheses. It also warns that a finite matrix or
Galerkin truncation has a discrete spectrum without proving compact resolvent
or the continuum spectrum.

**Status:** Resolved.

### 5. Quantum structures must be reconstructed separately

**Prior claim:** Discrete survivors constitute the structural content of
quantization, with operator and measurement formalisms appearing as
realizations.

**Finding:** A survivor set does not select a complex vector space,
noncommutative involutive algebra, representation, CCR/CAR, dynamics, state,
effect, instrument, or Born functional.

**Resolution:** Version 2 separates seven logical layers. It proves the
finite-dimensional exact CCR no-go and distinguishes that result from
finite-mode CAR. It then gives a conditional C*-algebraic reconstruction using
a supplied algebra and state, the GNS theorem, supplied unitary dynamics and
Stone's theorem, and supplied effects for Born probabilities.

**Status:** Resolved.

### 6. Probability evaluation is not probability selection

**Prior claim:** Measurement is selection at a nil boundary and invariant
measures can provide Born-type rules.

**Finding:** A discrete set has no canonical measure. Even after a state and
effect are supplied, `omega(E)` evaluates a probability but does not derive
the state, effect, detector, update map, capture process, or realized outcome.

**Resolution:** Version 2 removes the nil-collapse measurement claim and
states a conditional effect-probability proposition. Instruments, records, and
outcome selection remain explicit source obligations.

**Status:** Resolved.

## Additional mathematical corrections

- A nil profile is relative to a declared chart, decoder, domain, and extension
  category.
- Reduced discreteness can result from quotienting a continuous raw survivor
  set.
- Equal equation and variable counts are insufficient without a rank theorem.
- Compactness and local isolation have distinct roles.
- A finite alphabet does not make a bi-infinite symbolic trajectory space
  discrete.
- A finite matrix has finite spectrum but cannot satisfy exact bosonic CCR.
- A shared `U(1)` circle can carry phase only after a line bundle, action, and
  connection are supplied; it does not derive complex Hilbert space.
- GNS reconstructs a representation from a supplied C*-algebra and state; it
  does not select those inputs.
- Stone's theorem reconstructs a generator from supplied strongly continuous
  unitary dynamics.
- The circle, lens, and nil profiles may coexist, but no exhaustive
  one-profile/one-physical-theory correspondence is asserted.

## Retained theorem content

The revision retains the useful core of Program B3:

1. nil-type termination can motivate a search for robust survivor data;
2. transverse compact constraints can produce finite survivor sets;
3. topological and combinatorial invariants can provide stable discrete labels;
4. compact-resolvent operators provide a rigorous route to spectral
   discreteness; and
5. discreteness by itself carries no intrinsic probability distribution.

## Resulting scope

Program B3 v2 is a rigorous discrete-survivor and conditional quantum-
reconstruction paper. It proves exact conditional routes to finite constraint
sets and discrete spectra, supplies classical countermodels, and records the
operator-algebraic inputs needed for quantum mechanics. It does not derive
complex quantum mechanics, CCR/CAR, the Born rule, measurement dynamics, or
physical outcome selection from a nil profile alone.

## Expository revision, 2026-07-28

The theorem inventory and ownership are unchanged. The paper now begins with a
paper-specific reading guide that separates four logically distinct layers:
nil termination, constrained survival, operator spectrum, and quantum
reconstruction. An explicit object picture explains why failure of one chart
does not discretize the underlying state space, and a theorem-by-theorem guide
states what each formal result contributes.

Interpretive paragraphs were also added after the classical countermodels and
the GNS theorem. They clarify that the survivor result is a reusable geometric
tool, while GNS is a translator from supplied algebraic expectation data rather
than a source theorem for those data. No new quantum claim or duplicated
canonical theorem was introduced.
