# Revision Audit: Theta Closure II

Date: 2026-07-29

## Supersedes

This source supersedes the first edition, *Theta Closure in Modal Triplet
Theory II: Direct Geometric Realization of Nonabelian Overlaps*.

## Reason

The first edition used the retired few-TeV gauge crossing and could be read as
identifying an auxiliary Lens--Nil model with the selected q79/Fu--Yau
compactification. The v2 source already corrected that scientific scope, but
its two spectral-margin calculations contained arithmetic errors and its
nilmanifold appendix ended with a placeholder literature reference.

## Resolution

- Retained the selected SMDR gauge-profile targets at `Q = M_t`.
- Kept the shared circle as common phase/holonomy data counted once.
- Kept the round `S2` and compact Heisenberg nilmanifold as an auxiliary
  calibrated ansatz, not the selected physical compactification.
- Corrected the worst-case lens lower bound from `3.57` to `3.9137`.
- Corrected the worst-case nil lower bound from `11.05` to `16.2553`; the old
  calculation evaluated `4*pi^2/(1.989699)^2` incorrectly.
- Added a fully worked `R1 = 1` example exposing all three overlap
  coefficients and both spectral branches.
- Replaced the placeholder nilmanifold-spectrum citation with Andriot and
  Tsimpis, JHEP 09 (2018) 096.
- Added an explanatory roadmap and interpretation section.

## Retained Result

Within the paper's declared dimensionless auxiliary ansatz, two scale
parameters can be chosen to reproduce the two Paper I overlap ratios, and the
resulting representative remains well above the assumed spectral floor.

## Remaining Boundary

The paper does not prove uniqueness, a full lens-space reduction, selection of
the auxiliary geometry by MTT, identification with the q79/Fu--Yau branch, or
a held-out prediction of the gauge couplings.
