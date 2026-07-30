# Program B1 revision audit

## Selected revision

- Paper: `The Modal Triplet Theory Program B1`
- Superseded source: version 1.0
- Superseded source SHA-256: `b84404efbfe82ed0545cfe699795e7b70173f0e705ba6a0621ee61d963ad2d3d`
- Selected successor: version 2
- Controlling correction authority: `A10`
- A10 SHA-256: `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`

## Context audit

Version 1 was checked against the selected revisions of Program A0, Program
A1, Program B0, Coherent Kinematics, Fixed Points VI, and Lorentzian Base
Compatibility and Signature Stability. The correction is structural rather
than cosmetic. The earlier paper moved directly from a coarse circle profile
to gravity, curvature, causal cones, horizons, and universality. Those objects
live at different mathematical levels and require separate source data.

## Required corrections

### 1. Gravity is not the unique response to every circle profile

**Prior claim:** Every loop-dependent return mismatch forces one unique
kinematic-consistency encoding, identified with gravity.

**Finding:** A circle profile only says that some declared return transport is
nonidentity. Internal gauge transport, a flat local system, Berry transport,
and frame transport can all have this property. The coarse predicate does not
select a carrier, group, bundle, representation, or connection.

**Resolution:** Version 2 proves the holonomy-fixed descent theorem and the
endpoint-only trivialization criterion. Gravity is a canonical realization
only after a tangent/frame/coframe/spin carrier and Lorentzian metric are
supplied.

**Status:** Resolved.

### 2. Kinematic compatibility, Lorentzian geometry, and Einstein dynamics
must be separate

**Prior claim:** Loop bookkeeping stabilizes physical causal structure and
thereby identifies gravity.

**Finding:** A transport functor compares carrier values. It does not select a
metric or a causal principal symbol. A connection can be flat, internal, or
non-gravitational. Einstein dynamics additionally requires an action or field
equation.

**Resolution:** Version 2 uses four explicit levels: encoding transport,
smooth bundle/connection realization, physical principal-symbol geometry, and
local gravitational action.

**Status:** Resolved.

### 3. Physical causal geometry must use the corrected fixed-point
principal-symbol/local-action construction

**Prior claim:** Causal cones, null boundaries, and horizons become stable
once the circle compensator is present.

**Finding:** A causal cone is determined by the principal symbol of a selected
local hyperbolic equation after gauge and constraint treatment. An admissible
encoding boundary is not automatically a characteristic boundary or a
spacetime horizon. A spatially nonlocal kernel may preserve a formal
differential symbol while violating local domain of dependence.

**Resolution:** Version 2 proves conditional coherent principal-symbol descent
for a smooth fiberwise projector and a local normally hyperbolic operator with
scalar internal principal coefficient. It requires a local parent action or a
separately controlled retarded operator for causal dynamics.

**Status:** Resolved.

### 4. Einstein equations cannot be inferred from obstruction taxonomy

**Prior claim:** Gravity is structurally complete before any dynamical
realization, and later actions merely express the already forced encoding.

**Finding:** The same coarse return-memory predicate is compatible with a flat
internal connection, Einstein-Hilbert gravity, higher-curvature gravity, or no
metric dynamics. The obstruction predicate therefore underdetermines the
action.

**Resolution:** Version 2 derives Einstein's equation only from a supplied
Einstein-Hilbert-matter action with a well-posed variational problem. It proves
an explicit underdetermination theorem using flat U(1) holonomy and a family of
higher-curvature actions.

**Status:** Resolved.

## Additional mathematical corrections

- A nontrivial principal bundle can satisfy its cocycle exactly even when no
  nonzero global parallel section exists.
- Nontrivial holonomy is not itself inconsistency; the exact descending sector
  is the holonomy-fixed subspace.
- A path-dependent inverse does not provide an endpoint-only global
  trivialization.
- Flat connections can have nontrivial global holonomy.
- Levi-Civita uniqueness is conditional on a supplied metric plus torsion-free
  metric compatibility.
- Common transport on associated bundles is conditional on one supplied
  principal bundle and connection; it does not by itself prove the equivalence
  principle or universal numerical coupling.
- Encoding boundaries, characteristic boundaries, and gravitational horizons
  are separately typed.
- The shared compact phase circle is not identified with noncompact physical
  time.

## Retained theorem content

The revision retains the useful core of Program B1:

1. loop-dependent comparison requires explicit transport data;
2. smooth local transport is naturally represented by a connection;
3. a common principal connection induces compatible transport on associated
   carriers; and
4. frame transport supplies a genuine gravity realization after the physical
   metric and carrier are selected.

## Resulting scope

Program B1 v2 is a conditional reconstruction theorem. It proves that
path-independent carrier values are exactly the holonomy-fixed values, that an
endpoint-only trivialization requires trivial holonomy, and that smooth local
transport corresponds to a connection only on a supplied bundle. Gravity
becomes canonical only after a Lorentzian metric and physical frame carrier
are supplied; causal cones and Einstein dynamics additionally require a local
principal symbol and a selected action.

The resulting mathematical bridge is

```text
typed loop transport
  -> holonomy and its fixed sector
  -> smooth connection, given a bundle
  -> Levi-Civita transport, given a Lorentzian metric and frame carrier
  -> causal cone, given a local physical principal symbol
  -> Einstein equation, given an Einstein-Hilbert-matter action.
```

It does not select the physical base, Lorentzian signature, frame bundle,
metric, action, coupling constants, or Einstein dynamics from the circle
profile alone.

## Expository revision

The current paper now opens with a paper-specific guide following the idea
through abstract transport, smooth connection geometry, causal geometry, and
gravitational dynamics. A one-dimensional phase example explains
holonomy-fixed descent and the lawful responses to nontrivial return memory.
The argument map makes clear where the bundle, metric, principal symbol, and
action enter, so Levi--Civita and Einstein results cannot be mistaken for
consequences of the circle profile alone.

## Verification

- The current source compiles with `pdflatex` to a 13-page PDF.
- The final log has no undefined references, underfull boxes, overfull boxes,
  or LaTeX/package warnings.
