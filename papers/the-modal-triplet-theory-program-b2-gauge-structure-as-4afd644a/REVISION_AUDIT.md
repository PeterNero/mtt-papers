# Program B2 revision audit

## Selected revision

- Paper: `The Modal Triplet Theory Program B2`
- Superseded source: version 1.0
- Superseded source SHA-256: `72d198f4e94ee37ec4e5339ee001451746a4deb9305994285f071b04df1dd7ba`
- Selected successor: version 2
- Controlling correction authority: `A10`
- A10 SHA-256: `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`

## Context audit

Version 1 was checked against the selected Program A0, B0, and B1 revisions
and against standard principal-bundle and gauge-orbit mathematics. The old
paper correctly recognized gauge freedom as redundancy bookkeeping, but it
treated every nonunique representation as a global obstruction and moved too
quickly from that redundancy to a unique connection and gauge theory.

## Required corrections

### 1. Gauge redundancy is a canonical lens-type realization, not the unique
response to every lens profile

**Prior claim:** Every persistent lens obstruction forces one unique gauge
encoding.

**Finding:** A lens profile is only nonfaithfulness or redundancy of a declared
reduction. Gauge redundancy requires additional data: a group, an action, a
configuration object, a quotient category, and boundary conditions.

**Resolution:** Version 2 defines a gauge lens-type realization as a
noninjective orbit map for a declared group action. It retains the exact
universal factorization of invariant set-valued diagnostics through the orbit
space, without interpreting that universal property as uniqueness of a
physical gauge theory.

**Status:** Resolved.

### 2. Nonunique representatives do not imply failure of global description

**Prior claim:** Multiple admissible local lifts mean that a global
description or global lift cannot exist.

**Finding:** A principal bundle is globally defined by its transition cocycle
even when it has no global section. Trivial bundles also have many
gauge-related representatives. Redundancy and nonexistence of a section are
different predicates.

**Resolution:** Version 2 proves that a principal bundle admits a global
section exactly when it is trivial, while emphasizing that the bundle itself
is global independently of such a section.

**Status:** Resolved.

### 3. The category and section obstruction must be explicit

**Prior claim:** A lens obstruction generically forbids global gauge fixing.

**Finding:** The old paper conflated a section of `P -> Y` with a section of
the field-space orbit map. A global gauge fixing depends on function spaces,
the gauge group and its boundary behavior, the orbit stratum, stabilizers, and
the required regularity. Noninjectivity alone does not decide existence of a
section.

**Resolution:** Version 2 distinguishes bundle sections, associated-field
sections, and orbit-map sections. A genuine gauge-fixing obstruction is exactly
nonexistence of a right inverse of the orbit map in the declared category.
Gribov-Singer phenomena are retained as important realization-specific
examples rather than as universal consequences.

**Status:** Resolved.

### 4. Yang-Mills uniqueness requires a classification theorem

**Prior claim:** Smooth redundancy bookkeeping is uniquely implemented by a
gauge connection and determines the gauge-theory realization.

**Finding:** The lens profile does not select the base, group, bundle,
connection, invariant bilinear form, coupling, matter representation, boundary
conditions, or action. Gauge-invariant theta and higher-derivative terms can
coexist with the same orbit redundancy.

**Resolution:** Version 2 derives the Yang-Mills equation only from a supplied
Yang-Mills action and proves an underdetermination theorem for the group and
dynamics.

**Status:** Resolved.

## Additional mathematical corrections

- The quotient stack and coarse orbit space retain different information;
  stabilizers can make the coarse quotient singular.
- Gauge invariance of an observable does not imply that a chosen family of
  observables separates gauge orbits.
- Local slice theorems do not automatically provide a global slice.
- The allowed gauge group must include boundary and asymptotic conditions;
  large or boundary transformations may carry physical charges.
- Local gauge potentials are representatives of one global connection when
  they obey the correct overlap law.
- Lens-type orbit redundancy and circle-type connection holonomy may coexist
  in one gauge realization.
- Internal gauge and gravitational frame connections remain separately typed.
- Gauge quotienting does not derive quantization, BRST/BV completion, Born
  probability, or the Standard Model representation content.

## Retained theorem content

The revision retains the useful core of Program B2:

1. gauge transformations organize redundant representatives;
2. invariant diagnostics factor through gauge orbits;
3. principal-bundle transition functions organize local representatives;
4. a connection compares local gauges without selecting a preferred gauge;
   and
5. Yang-Mills theory is a valid realization after its geometric and dynamical
   inputs are supplied.

## Resulting scope

Program B2 v2 is a typed gauge-redundancy and conditional Yang-Mills
reconstruction theorem. It proves the orbit-quotient factorization, separates
the two global-section problems, and makes global gauge fixing a
category-specific right-inverse question. It does not select a gauge group,
principal bundle, connection, coupling, matter sector, anomaly cancellation,
or Yang-Mills action from the lens profile alone.

## Expository revision

The current paper now opens with a paper-specific guide following redundancy
through group action, quotient, principal bundle, connection, gauge fixing,
and action. It explains the two genuinely different section problems, gives a
simple `U(1)` potential example, maps the argument, and states which gauge and
Standard Model data remain unselected. The quotient universal property is
therefore presented as an organizer of representatives rather than as a
uniqueness theorem for physics.

## Verification

- The current source compiles with `pdflatex` to a 12-page PDF.
- The final log has no undefined references, underfull boxes, overfull boxes,
  or LaTeX/package warnings.
