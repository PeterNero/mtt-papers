# Temporal Bell paper v3 revision audit

## Current publication and exposition repair

- Superseded released edition: version 2, Zenodo record `21650911`.
- Reason for version 3: the published version 2 PDF predates the final
  theorem-ownership cleanup and did not contain a reader map or a sufficiently
  explicit plain-language connection between pair protocols, disturbance,
  and the qubit benchmark.
- Resolution: version 3 adds the protocol map, interpretive bridges around
  the two owned results, and a measurement-as-physical-process conclusion.
- Retained result: the common-joint-distribution Leggett--Garg theorem and
  conditional no-retro-signaling proposition are unchanged.
- Open boundary: no selected MTT source currently emits the generic physical
  clock, state, instrument family, and probability law for arbitrary temporal
  Bell experiments.

The release-currency audit found that the published version 2 PDF and the
reviewed local source differed under the same version label.  Version 3 makes
that content delta explicit and prevents the stale release from being treated
as current.

## Version 2 selected revision

- Paper: `Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory`
- Superseded source: version 1.0
- Superseded source SHA-256:
  `fbf9cb11f14918c433eb9a8ea778e4e27ff908ab7e99d3002bf9dbddd06f12ea`
- Selected successor: version 2
- Controlling correction authority: `A10`
- A10 SHA-256:
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`
- Durable research handoff:
  `354864cc-6255-465c-bfcf-85996c6ce37c`

## Version 2 verdict retained

The original algebraic Leggett-Garg result survives: a single
context-independent joint distribution for three dichotomic variables implies
`-3 <= K <= 1`. The explicit qubit calculation also survives as a standard
quantum operational benchmark.

The former MTT promotion did not survive. Projection, fixed-point selection,
or the assertion of global consistency does not by itself select a probability
measure, sequential measurement instruments, a physical clock, causal
channels, no-retro-signaling, or an LGI violation. Version 2 is therefore a
conditional sequential-instrument analysis and completion contract.

## Version 2 required corrections

### 1. Separate physical and stabilization time

**Prior state:** Physical measurement times and fixed-point/global-history
language were used without a type boundary.

**Resolution:** Version 2 defines physical clock times `t_i` on a supplied
causal spacetime and an independent auxiliary stabilization parameter `tau`.
No identification is made with stabilization flow or shared-circle phase.

**Status:** Resolved.

### 2. Correct the source of LGI violation

**Prior claim:** MTT generically violates temporal factorization because of
projection and global coherence.

**Finding:** Failure of one sufficient classical factorization model does not
imply `K > 1`. The same projection data support both satisfying and violating
operational realizations.

**Resolution:** Version 2 gives a projection/global-history non-selection
check in prose. A violation is attributed only to an executed state-channel-
instrument packet whose three pair contexts give `K > 1`. Global consistency
is retained as a possible contextual mechanism, not a prediction.

**Status:** Resolved.

### 3. State instruments and updates explicitly

**Prior state:** Measurements were represented by outcomes and conditioning,
without instrument maps or a sourced update law.

**Resolution:** Version 2 defines completely positive trace-nonincreasing
outcome maps, their trace-preserving nonselective sum, conditional states,
propagation channels, pair probabilities, and pair correlators. It separately
defines no-retro-signaling and no-signaling in time.

**Status:** Resolved.

## Additional contextual repairs

- The no-retro-signaling claim is now conditional on causal preparation,
  channel, and future-instrument independence.
- The common-joint-distribution contract is stated directly, avoiding the
  stronger-than-needed deterministic hidden-variable definition.
- Pair correlators are recognized as potentially coming from distinct
  laboratory contexts.
- Measurement invasiveness and the clumsiness loophole are explicit.
- The standard qubit/Lueders calculation is labeled an imported quantum
  benchmark.
- The former generic temporal-network claim is withdrawn.
- Spatial Bell and temporal LGI scenarios are no longer declared one theorem:
  temporal experiments permit forward disturbance.
- The assumed fixed-point-ensemble probability measure is removed.
- The duplicate placeholder bibliography is removed.

## Exact theorem content retained in version 3

Version 2 has exactly two formal results:

1. the three-time Leggett-Garg bound from a common joint distribution;
2. conditional operational no-retro-signaling for causal sequential
   instruments.

The projection/global-history comparison is a scope check, the MTT
temporal-correlation bridge is a completion contract, and the qubit/Lueders
value `K = 3/2` is an imported operational benchmark. None is presented as a
new Bell-paper theorem.

## Theorem ownership

The paper owns only the algebraic LGI theorem and its conditional
no-retro-signaling proposition. It does not own projection/descent,
fixed-point, Born-source, or general MTT completion theorems. This keeps the
paper close to the lighter theorem profile intended for the Bell discussion.

## Frontier preserved

The paper does not claim:

- a general MTT Born source theorem;
- a selected physical clock from stabilization order;
- a selected measurement instrument from projection;
- generic temporal Bell violation;
- ontic no-retrocausality from operational marginals;
- a theorem identifying spatial and temporal Bell phenomena;
- arbitrary-apparatus completion beyond selected finite recorder contracts.

## Version 3 publication delta

Version 3 is an explanatory and theorem-ownership successor to the published
version 2. It should be uploaded as a new Zenodo version with the generated
PDF, canonical TeX, Markdown conversion, and this revision audit.
