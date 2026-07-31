# Spectral Action Paper v2 Release Audit

## Selected revision

- Paper: `The Spectral Action as a Conditional Shadow of Coherent Fixed-Point Geometry`
- Superseded version: v1.0
- Prior release DOI: `10.5281/zenodo.18261750`
- Selected successor: v2
- Controlling correction authority: A10
- Live blocker: B.ACTION.01, upper action and automorphism transfer

## Context audit

Version 1 was checked against the revised MTT-to-NCG paper and the current
finite Standard Model authorities A46, A47, A49, A50, and A51. Its central
proposal remains useful: the almost-commutative spectral action is a natural
candidate lower-dimensional action language for selected MTT data. The
original proof did not establish that descent.

The revision distinguishes three logical layers:

1. standard spectral-action mathematics after a product triple and cutoff are
   supplied;
2. executed finite MTT representation and operator packets;
3. the still-open same-source upper action and descent theorem.

## Required corrections and resolutions

### 1. Canonical finite algebra from overlap channels

**Prior claim:** Finitely many stable overlap channels canonically select the
finite Standard Model algebra up to Morita equivalence.

**Finding:** Finite closure under composition and involution does not select a
unique real algebra, representation, KO-dimension, or finite-axiom solution.
The current execution instead finds a no-go for the native three-summand
neutral sector and requires a specific fourth summand.

**Resolution:** The claimed proposition and proof are withdrawn. Version 2
reports the actual no-go and minimal completion.

### 2. Unique Dirac operator from compatibility

**Prior claim:** Bounded commutators, grading, and reality select a canonical
Dirac operator, unique up to bounded perturbations and inner fluctuations.

**Finding:** Those conditions admit many Dirac operators. In the current finite
packet the physical entries of the 96-by-96 operator are profile coordinates.

**Resolution:** Version 2 treats the finite Dirac operator as an explicit
profile-tier construction and states the source-value theorem that would be
needed to predict its entries.

### 3. Cutoff fixed by the spectral gap

**Prior claim:** The coherent gap and lower proper-time support fix the cutoff
function and scale up to reparametrization.

**Finding:** A support bound fixes neither the measure nor its Laplace
transform. Measures with the same lower support point give different cutoff
functions and moments.

**Resolution:** Version 2 proves the correct proper-time statement and gives an
explicit two-measure counterexample. A selected measure and normalization are
now listed as open inputs.

### 4. Standard Model parameters fixed by one bottleneck vector

**Prior claim:** Gauge couplings, Yukawa matrices, Higgs coefficients, and
several unrelated sectors are fixed functions of one vector Theta.

**Finding:** The finite packet fixes exact representation data and evaluates
some traces, while finite Dirac entries remain profile data and absolute
normalization, cutoff moments, threshold transport, and RG transport remain
open.

**Resolution:** The one-vector closure theorem is withdrawn. Version 2 states
the exact/profile/open tier for each sector.

### 5. Spectral action as an established MTT shadow

**Prior claim:** The spectral action is already derived as a truncation shadow
of coherent fixed-point dynamics.

**Finding:** No selected upper differential/action and connection-preserving
intertwiner currently reproduces the lower product triple and action. This is
the live B.ACTION.01 exit.

**Resolution:** Version 2 defines the selected spectral-action source contract
and proves a conditional descent theorem. It explicitly records that the
contract is not yet instantiated.

### 6. Cross-sector closure

**Prior claim:** Collapse, events, UV completion, canonical geometry, and all
Standard Model parameters are governed by the same finite bottleneck vector.

**Finding:** Shared terminology does not supply typed common source maps.

**Resolution:** The cross-sector theorem is withdrawn. Same-source,
commuting-map closure is retained as a falsifiable future target.

## Current computational inputs

The revision directly uses these curated result objects at results commit
`31247ebb5c22f3fbb5443024365433c6ee0bff4a`:

- `typed_family_representation` (A46): exact three-family representation and
  anomaly checks;
- `native_gauge_group` (A47): exact native gauge group and Z6 quotient;
- `physical_df_96` (A49): profile finite Dirac operator and the native-triple
  no-go;
- `neutral_summand_hypercharge` (A50): exact neutral completion and
  anomaly-free hypercharge line;
- `finite_inner_fluctuation` (A51): exact one-form enumeration and selected
  one-Higgs submodule, with profile finite traces;
- `su3_finite_gauge_spectrum` (A62): finite gauge-spectrum cross-check.

The repository reference does not promote profile replay to source-derived
prediction.

## Frontier after revision

The paper-level correctness blocker is resolved: the revised paper no longer
claims that MTT has derived the full spectral action or Standard Model
parameters. The research blocker B.ACTION.01 remains open. Its exit requires
one selected upper differential/action whose automorphisms, zero modes,
products, finite operators, trace data, and continuum action descend through
certified commuting maps.
