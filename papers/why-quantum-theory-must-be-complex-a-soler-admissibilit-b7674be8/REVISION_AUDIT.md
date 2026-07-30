# Revision Audit: Complex-Hilbert Rigidity

## Release Decision

- Current source: Version 2, July 2026.
- Supersedes: Version 1, January 2026.
- Review class: substantive theorem correction.
- Intended tier: conditional reconstruction theorem with an imported Soler classification.
- Not an unconditional MTT derivation of the complex scalar field.

## Defects Corrected

1. Version 1 treated the Hilbert reconstruction, an infinite orthogonal sequence, and local tomography as already derived by MTT.
2. Soler's theorem was described as though it selected the complex field; it only reduces the possibilities to the real, complex, and quaternionic division rings.
3. Quaternionic exclusion was attributed to predictive stability without a precise composite-system axiom.
4. Real exclusion was attributed to "phase-rich coherence," although complex quantum theory can be represented on a real Hilbert space equipped with a complex-structure operator.
5. The finite q79 carrier was allowed to stand in for Soler's infinite-sequence hypothesis.
6. The representation-sensitive and composition-sensitive scope of the conclusion was not stated.

## Version 2 Theorem Package

The corrected argument has two independent stages.

1. An orthomodular generalized Hilbert space containing an infinite orthonormal sequence is classified, by Soler's imported theorem, over `R`, `C`, or `H`.
2. Within a declared finite-composition class, each `d`-dimensional system has the full self-adjoint matrix space as its unnormalized state/effect space, the standard same-field composite has dimension `ab`, independent product effects have no extra linear identifications, and those product effects are tomographically complete.

For that class, the real dimensions are

```text
K_R(d) = d(d+1)/2,
K_C(d) = d^2,
K_H(d) = d(2d-1).
```

For `a,b > 1`, the composition defects are

```text
K_R(ab) - K_R(a)K_R(b) = ab(a-1)(b-1)/4 > 0,
K_C(ab) - K_C(a)K_C(b) = 0,
K_H(ab) - K_H(a)K_H(b) = -2ab(a-1)(b-1) < 0.
```

Thus only the complex full-matrix theory satisfies the declared product-tomography identity.

## Imported Results

- Soler's classification theorem is imported from:
  - Maria Pia Soler, *Characterization of Hilbert Spaces by Orthomodular Spaces*, Communications in Algebra 23 (1995), 219-243.
  - Samuel S. Holland Jr., *Orthomodularity in Infinite Dimensions; a Theorem of M. Soler*, Bulletin of the American Mathematical Society 32 (1995), 205-234.
- The operational-composition context is compared with:
  - Lucien Hardy and William K. Wootters, *Limited Holism and Real-Vector-Space Quantum Theory*, Foundations of Physics 42 (2012), 454-473.
  - Howard Barnum and Alexander Wilce, *Local Tomography and the Jordan Structure of Quantum Theory*, Foundations of Physics 44 (2014), 192-212.

The paper owns the explicit dimension-defect calculation and the resulting conditional theorem, not the imported classification.

## Representation and Composition Guardrails

- Complex quantum theory can be realified by adjoining an orthogonal operator `J` with `J^2 = -I`; therefore the theorem selects an operational package, not a unique notation for the underlying real vector space.
- Alternative real or quaternionic composite rules can evade the displayed dimension identity by changing the standard same-field/full-matrix composition package. They are outside, not refuted by, the theorem.
- Local tomography is an additional physical assumption and is not inferred from locality alone.

## MTT Interface

Current MTT results are compatible with the theorem's complex branch:

- the canonical q79 quantum model is an exact finite complex model on its declared binary domain;
- the finite carrier supports a complex polarization with the selected `+i/-i` orientation pair.

The following source gates remain open:

1. construct one infinite orthogonal sequence, or a compatible completed limit, from selected MTT geometry;
2. derive the standard same-field composite rule from the shared upper construction;
3. prove independent local effects and local tomography on the intended physical domain;
4. derive the global complex-structure operator from the shared circle connection, rather than inserting it at the finite representation layer.

## Claims Explicitly Not Made

- No unconditional proof that every quantum theory must use complex numbers.
- No derivation of Soler's infinite-sequence hypothesis from the finite q79 model.
- No inference of local tomography from Bell locality or no-signaling.
- No exclusion of all real or quaternionic reformulations.
- No claim that the compact phase circle is physical time.
- No ownership of Soler's theorem.

## Release Checks

- Science-only title and abstract.
- Revision history appears only in the unnumbered Version 2 Revision Note.
- Required fields included: Supersedes, Reason, Resolution, Retained result, Remaining boundary.
- External references checked against primary publication records.
- No duplicated MTT theorem body.
- PDF compiled with BibTeX and visually inspected page by page before freezing.
