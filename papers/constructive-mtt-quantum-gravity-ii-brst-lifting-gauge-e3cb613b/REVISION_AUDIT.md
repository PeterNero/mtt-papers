# Constructive MTT Quantum Gravity II v2 Revision Audit

## Source lineage

- Superseded title: `Constructive MTT Quantum Gravity II: BRST Lifting,
  Gauge-Invariant Observables, and the Physical Hilbert Space under SPT
  Damping`
- Superseded source: `12 Quantum Gravity/_work/Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping`
- Public v1 record: Zenodo `10.5281/zenodo.18209697`
- Stable paper ID:
  `constructive-mtt-quantum-gravity-ii-brst-lifting-gauge-e3cb613b`
- Selected successor:
  `mtt-papers/papers/constructive-mtt-quantum-gravity-ii-brst-lifting-gauge-e3cb613b/main.tex`
- Successor title: `Constructive MTT Quantum Gravity II: A Conditional
  BRST/BV Compatibility and Physical-State Reconstruction Contract for
  SPT-Filtered Models`
- Successor version: `v2`
- Governing authorities: A10 master corrigendum, A18 strict quantization/QFT
  audit, the 2026 quantum-gravity status audit, the SPT
  Gaussian/Stieltjes correction, and the mathematical-language BRST packet.

Version 2 retains the stable paper identity and public-release lineage while
superseding the theorem-level claims of v1.

## Overall disposition

The v1 headline is withdrawn. It did not prove a nonperturbatively defined,
unitary MTT quantum-gravity sector. Four logical promotions were unsupported:

1. separately filtered graviton and ghost covariances were treated as an
   invariant BRST/BV regulator;
2. termwise formal BRST identities were treated as exact identities of an
   already constructed Borel sum;
3. TT-sector reflection positivity was treated as positivity of the complete
   BRST cohomology; and
4. a finite slab was treated as sufficient for a global unitary Lorentzian
   time-translation group.

The corrected paper replaces that chain by a five-gate conditional theorem and
proves the valid interface theorems. This is a major mathematical rewrite, not
a prefatory caveat.

## A10 requirements and resolution

| Required correction | v2 resolution |
| --- | --- |
| Do not infer positivity on BRST cohomology from TT positivity | A two-dimensional counterexample proves the inference false. The physical theorem now assumes positivity on the full BRST-closed positive-time algebra and requires exact vectors to lie in the reflection null radical. |
| Prove Borel-summed Ward/QME identities with uniform bounds | V2 proves a precise Borel-inheritance theorem for continuous linear Ward operators under a common analytic continuation, uniform exponential Borel bounds, and uniqueness. It explicitly leaves the constructive estimates and nonlinear QME convolution bounds open. |
| Verify SPT preservation of BRST/BV and boundaries | V2 proves a shared functional-calculus chain theorem from exact spectral-projector intertwining and compatible boundary domains. A one-dimensional counterexample proves that independent filters are insufficient. |
| Construct a physical Hilbert space only after physical OS positivity | The cohomological OS theorem is conditional on positivity of the physical observable algebra, exact-null descent, support preservation, and translation compatibility. Global unitarity additionally requires the full OS reconstruction and removal limits. |
| Label the current result conditional | The title, abstract, main theorem, ledger, and conclusion all identify the result as a conditional compatibility contract. |

## Additional corrections found in contextual review

### Quantum measure versus classical nilpotency

V1 used the standard classical BRST transformation and a formal boson/ghost
Jacobian cancellation as if they established a quantum measure. V2 separates:

- classical nilpotency and the classical master equation;
- a regulator-dependent BV Laplacian and quantum master equation;
- anomaly counterterms, integration cycle, boundary behavior, and removal
  limits.

The finite-cutoff Ward theorem is now proved by super-Stokes only after the
weighted quantum measure is explicitly assumed invariant.

### Gauge-parameter independence

V1 differentiated a normalized functional integral while allowing the gauge
parameter to enter the kinetic split, but did not account for the corresponding
measure and covariance variation. V2 states gauge-fixing independence for a
fixed exact quantum BRST measure and an `s`-exact gauge-fixing homotopy. The BV
formulation is cited as the framework in which that condition must be
constructed.

### Finite-volume Borel theorem

V1 said a mixed boson/ghost loop-vertex expansion followed from
Hilbert-Schmidt covariance, local factorial derivative bounds, and a lower
bound. It did not construct that expansion or prove the needed sectorial
stability. V2 no longer repeats the claim. It records that QG-II cannot inherit
the still-unproved constructive conclusion of QG-I.

### Finite slab reconstruction

V1 promoted the Euclidean slab translation semigroup to a unitary
one-parameter group. V2 distinguishes a descended local contraction semigroup
from a global positive-energy Lorentzian group. The latter requires the full OS
axioms, analytic continuation, and suitable all-time or infinite-volume
completion.

### Permanent Gaussian damping and standard positivity

The later QG audit found a stronger obstruction not present in the compact A10
entry. V2 proves it directly. If

```text
D(x) = integral rho(ds)/(x+s)
```

has a nonzero positive spectral measure, then `D(x) >= m/(x+R)` for suitable
`m,R > 0`. It cannot also obey a permanent Gaussian upper bound in the same
spectral variable. Consequently, the original SPT Stieltjes/OS argument is
withdrawn. This no-go does not classify every nonlocal theory; it invalidates
the specific standard-positivity proof used by the old program.

## New exact theorems in v2

### Shared-filter chain theorem

For a Hilbert complex whose spectral projections and boundary domains
intertwine the differential, a common bounded functional calculus satisfies

```text
Q_r f(Delta_r) = f(Delta_{r+1}) Q_r.
```

The filtered covariance and common spectral cutoff are therefore chain maps.
The result is exact at the linearized level and does not promote nonlinear
vertices or the measure.

### Independent-filter no-go

On the one-dimensional complex `C --1--> C`, two filters acting by different
constants fail the chain-map equation. Thus separate use of similarly shaped
filters is not a BRST theorem.

### Finite-cutoff quantum Ward theorem

For a finite graded field space with an invariant weighted measure, nilpotent
quantum BRST vector field, invariant integration cycle, exact gauge-fixing
homotopy, and controlled integrals, super-Stokes proves:

```text
integral sG exp(-S/hbar) dmu = 0,
d_alpha E[O] = 0 for sO = 0.
```

This identifies the precise finite object a future MTT BV packet must emit.

### Uniform Borel inheritance theorem

A continuous linear Ward identity satisfied by every perturbative coefficient
passes to the Borel sum only when the Borel transform has a common analytic
continuation, uniform exponential bound, and a unique Laplace sum. This closes
the logical implication while leaving the actual mixed gravity/ghost estimates
open.

### Conditional cohomological OS theorem

Reflection positivity on the full closed observable algebra, exact-null
descent, and translation compatibility yield a physical pre-Hilbert quotient
and its completion. A full Lorentzian unitary theory still requires the
remaining OS and continuum hypotheses.

## Current-corpus results incorporated

| Current result | Use in v2 | Boundary preserved |
| --- | --- | --- |
| Finite q79 TT Hessian and positive free two-helicity sector | Listed as useful gravity input | Does not select an interacting quantum measure or UV completion |
| Two-derivative TEGR/Einstein action shape on the explicitly selected branch | Supplies a possible classical action before a standard diffeomorphism BRST lift | Newton normalization, cosmological term, quantum source, and higher-order data remain separate |
| Fixed-order quantum-GR EFT observable functor | Identifies the current imported-parity benchmark | Standard BRST/BV quantization is imported, not derived from MTT |
| Exact finite SM quotient gauge algebra and classical BRST complex | Demonstrates that MTT now has a real classical gauge-stack BRST result | It is not the gravitational BV measure or QME |
| Corrected Fixed Points VI | Prevents classical damping/covariance from being retyped as quantum input | Quantum covariance and quantization remain downstream |
| Hodge-index BV effective-state proposal | Motivates the needed preprojection field complex, contraction, determinant, and provenance packet | The physical q79 action, QME, and pushforward are still open |

## Primary-source checks

The correction was checked against primary literature:

- Batalin and Vilkovisky for classical and quantum master-equation structure;
- Schwarz for BV gauge-fixing independence as integration over Lagrangian
  submanifolds;
- Costello for regulator-aware renormalized BV quantization;
- Barnich, Brandt, and Henneaux for local BRST cohomology;
- Sokal for the uniqueness and bounds required by Borel summation;
- Osterwalder and Schrader for the actual Euclidean reconstruction hypotheses;
- Kugo and Ojima, and Kalau and van Holten, for the nonautomatic positivity
  conditions on BRST physical state space; and
- Asorey, Rachwal, and Shapiro for the independent unitarity difficulties of
  higher-derivative/nonlocal damping models.

## Claims explicitly not made by v2

Version 2 does not claim that MTT currently has:

- a selected chain-compatible SPT regulator for the complete gravitational BV
  complex;
- a gravitational quantum measure or anomaly-free QME;
- a proved mixed gravity/ghost loop-vertex expansion;
- uniform cutoff and volume Borel-sum limits;
- physical reflection positivity for all BRST-closed observables;
- a global physical Hilbert space reconstructed from the SPT model;
- a massless soft-graviton scattering theory; or
- a nonperturbative, UV-complete, unitary theory of quantum gravity.

## Exit certificate

The corrected paper reduces promotion to five concrete objects:

1. a selected graded gravitational field/antifield complex and action;
2. a common filter packet proving spectral and boundary intertwining;
3. a finite-cutoff BV measure packet proving the QME and anomaly rows;
4. a constructive packet proving common Borel domains, uniform remainders, and
   removal limits; and
5. a physical OS packet for the complete declared BRST-closed observable
   algebra.

The paper becomes a constructed quantum-gravity theorem only when all five are
supplied from the same selected source chain.

## Validation record

- Every theorem and proof in v1 was re-evaluated in context.
- A10 and A18 requirements were mapped individually.
- The 2026 QG, fixed-point, and mathematical-language packets were read
  directly.
- The exact filter, independent-filter, TT-positivity, and spectral/Gaussian
  counterexamples were proved in the successor text.
- Primary citations and publication identifiers were checked against original
  journal or arXiv records.
- TeX compilation, Markdown regeneration, visual inspection, migration, and
  kernel verification are handled by the canonical repository workflow.
