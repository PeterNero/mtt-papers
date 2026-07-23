# Computational Evidence

The canonical public calculation repository for this paper collection is:

<https://github.com/PeterNero/mtt-results-repro>

Papers should cite that repository only when their authority overlays map to
one or more entries in its hash-addressed result manifest. The paper should name
the mapped authority/result identifiers and preserve the result tier
(`DERIVED_EXACT`, `NUMERICAL_CERTIFIED`, `PROFILE_REPLAY`, `CONDITIONAL`, or
`OPEN`). A repository reference does not promote a replay or conditional result
to a derivation.

When a versioned Zenodo calculation capsule is available, cite both the capsule
DOI and the repository. Until then, the repository URL is a valid
reproducibility reference for mapped committed results. Papers without mapped
results may mention the repository as project infrastructure, but should not
claim that it supplies evidence for the paper.

The MTT Research Environment publication panel applies a managed TeX/Markdown
reference block and previews the corresponding Zenodo metadata. It uses the
paper authority overlays and the curated result manifest rather than guessing
links from titles.
