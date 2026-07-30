# MTT Expository Readability Policy

Date: 2026-07-28

## Purpose

Every MTT paper must be understandable as an argument, not merely inspectable
as a list of definitions, theorems, and proofs. Formal rigor and explanatory
depth are complementary requirements.

This policy applies to all canonical papers, including Foundation, the Fixed
Points series, program papers, encoding papers, calculation papers, and
interpretive papers.

## Required Reader Experience

Each paper must provide, in language specific to its own subject:

1. **Orientation.** State the problem, why it matters, the paper's main
   contribution, its claim tier, and the prerequisite results it imports.
2. **Object intuition.** Explain what the central spaces, maps, operators, or
   numerical objects represent and why they are introduced.
3. **Argument flow.** Tell the reader how the major formal results depend on
   one another and which question each result answers.
4. **Result interpretation.** After each major theorem cluster, explain what
   has been established, what has not, and how the result is used downstream.
5. **Concrete foothold.** Include a worked example, finite-dimensional toy
   model, geometric picture, limiting case, or explicit schematic whenever
   the subject permits one.
6. **Context.** Relate the paper to its actual MTT dependencies and to
   relevant established mathematics or physics without claiming containment
   that has not been proved.
7. **Limitations and frontier.** Identify assumptions, failure modes, open
   promotions, and the strongest legitimate current conclusion.
8. **Standalone readability.** Define local notation and restate imported
   contracts clearly enough to follow the argument, while citing the
   canonical theorem owner and not duplicating its proof.

Section titles need not follow a template. The requirement concerns the
reader's understanding, not the presence of stock headings.

## Prohibited Substitute

Generic series prose is not an explanation. In particular, the following
paragraph is forbidden in TeX, styles, generated Markdown, and release PDFs:

> Part ... of ... in the ... series. As both the cornerstone of the Modal
> Triplet Theory (MTT) collection and a stand-alone development, the series is
> intended to function simultaneously as a basis and as a self-contained
> study. Each paper in the series builds upon its predecessors, extending the
> fixed-point framework step by step.

The shared `\seriestagline` macro is intentionally empty by default. A paper
may include a short series note only when the note is factually correct and
helps the reader understand that paper's exact dependency position.

## Abstract and Revision History

The abstract is scholarly content, not a change log. It states the paper's
problem, method, result, claim tier, and scope boundary. Words such as
`corrected edition`, `supersedes`, and `revision note` belong in the separate
revision note or release metadata and must not be mixed into the abstract.

Likewise, the scholarly title does not carry an edition announcement. The
edition belongs in the version field or title-page date block.

The complete release contract, including the five-field revision note and
Zenodo draft gate, is `PAPER_RELEASE_REQUIREMENTS.md`.

## Relationship to Theorem Ownership

Theorem ownership prevents duplicated formal results. Expository readability
prevents the opposite failure: a technically correct paper whose logic is
opaque to a reader.

A later paper may explain an imported theorem in its own physical or
computational context. It should state the hypotheses, conclusion, and role,
cite the owner, and discuss the new consequence. It should not copy the
owner's theorem/proof block.

## Human Review and Automated Audit

`scripts/audit_expository_readability.py` records quantitative indicators:

- formal-result and proof counts;
- narrative word count outside formal blocks;
- presence of reader orientation, examples, interpretation, limitations, and
  conclusion material;
- theorem-density warnings; and
- forbidden-boilerplate occurrences.

These indicators prioritize human review; they do not certify prose quality.
A paper is marked expository-ready only after contextual review, compilation,
and rendered-page inspection.

## Reference Standard

The July 28 revision of *Modal Triplet Theory: Foundations* is the first
reference implementation. It adds a reader route, object-level intuition,
finite examples, explanations around each theorem cluster, a dependency
ledger, limitations, and a concrete downstream frontier without adding or
duplicating formal results.

*The Book on Modal Triplet Theory* has a different role: it is a
low-mathematics interpretive guide and therefore carries still less formal
detail. Technical papers should be explanatory, but they remain technical
papers rather than copies of the Book.
