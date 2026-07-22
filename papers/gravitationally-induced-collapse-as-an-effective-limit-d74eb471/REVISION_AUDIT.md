# Revision Audit: Gravitationally Induced Collapse v3

## Verdict

The original paper did not derive Diósi--Penrose (DP) collapse from MTT. Version 2
repaired the open-system typing and isolated the missing correlation source. Version
3 closes a different, previously unproved layer: the selected Einstein/TEGR
weak-field constraint gives the Penrose Newton self-energy, that energy is a squared
Hilbert distance, and the exact Penrose rate matrix has a unique completely positive
pure-dephasing Markov completion whose generator is the DP double commutator.

This is a real completion theorem, not a source-selection theorem. Penrose's argument
motivates a lifetime of order hbar / E_G; it does not prove that MTT selects the exact
rate, the smearing scale, Markovianity, or objective outcomes.

## Version-3 changes resolved

| Required correction | Resolution |
|---|---|
| Use the selected gravitational law rather than postulate the spatial kernel | Derives the regulated Newton quadratic form from the static Einstein/TEGR Poisson constraint |
| Prove that Penrose pair rates define valid quantum dynamics | Shows E_ab is one half of a squared Green-Hilbert distance and is conditionally negative definite |
| Prove complete positivity for every finite branch set | Applies Schoenberg and constructs the CPTP Schur semigroup exp(-t E_ab / hbar) |
| Identify the generator exactly | Proves equality with the regulated DP double commutator on every branch matrix unit |
| Avoid claiming more than Penrose proves | Treats the exact rate equality as the remaining MTT source theorem |
| Separate decoherence from objective outcomes | Gives a random-unitary Gaussian unravelling and proves the master equation alone cannot select single outcomes |
| Preserve the open-system route | Shows a Davies source with Newton Kossakowski kernel yields the same generator |

## New exact results

1. Newton-constraint energy theorem in the static weak-field regime.
2. Green-Hilbert squared-distance representation of E_G.
3. Exact conditional-negative-definiteness identity for all finite branch sets.
4. Penrose--Schoenberg CPTP semigroup theorem.
5. Exact equality of its generator with the regulated DP double commutator.
6. Uniqueness in the time-homogeneous, population-preserving, no-extra-phase Schur class.
7. Random-unitary Gaussian realization and objective-outcome obstruction.
8. Direct-rate and Davies-correlation routes shown to converge to the same effective law.

The executable companion `verify_penrose_schoenberg_completion.py` checks the exact
finite Poisson field/source identity, the CND identity, the DP generator equality,
and numerical positivity of representative Schur kernels. The paper proof is general;
the script is a regression certificate, not evidence for physical source selection.

## Version-2 results retained

- CPTP reduction/lifting projection theorem;
- conditional normalization of trace-decreasing filters;
- exact finite-cutoff Nakajima--Zwanzig equation;
- conditional Davies--GKSL interface;
- internal-to-external scale-typing obstruction;
- analytic finite-time response theorem;
- finite-noise OU first-passage smoothness result.

These results are not reopened by version 3.

## Promotion data still absent

- selected numerical G_eff or an independently accepted gravitational scale anchor;
- selected external mass-density smearing map and length in physical units;
- MTT proof of the exact rate identity
  `-d/dt log|A_ab(t)| at t=0 = E_ab / hbar`, or an equivalent selected
  mass-density correlation function;
- controlled Markov/weak-coupling/secular errors, if the environmental route is used;
- selected stochastic instrument or nonlinear state process for objective outcomes;
- proof of the associated probability rule and realized-branch selection.

## Context checked

- current q79 finite TT and same-source Einstein/TEGR action status;
- the corpus's existing general Schoenberg branch-damping theorems;
- the corrected projection/probability paper's instrument and outcome separation;
- Nakajima--Zwanzig, Davies, GKSL and Diósi primary results;
- Penrose's 1996 free-fall incompatibility and provisional lifetime argument;
- Schoenberg's 1938 positive-definite-kernel theorem.
