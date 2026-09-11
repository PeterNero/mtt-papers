# Locality, Coherent Alternatives, and Physical Records

An Interpretive Account of Quantum Experiments in Modal Triplet Theory

Author: Peter Nero. Version 1.0, 6 September 2026.

Status: unpublished interpretive manuscript for author review and later release.

## Contents

- [TeX source](main.tex)
- [PDF](main.pdf)
- [Generated Markdown](paper.md)
- [Version rationale and contextual review](REVISION_AUDIT.md)
- [Source and result provenance](evidence-manifest.json)
- [Build and review record](build-review.json)

This paper is distinct from the earlier philosophical interpretation of causal-base constraint realism. It focuses on definitions, photon/electron experiments, temporal and multipartite distinctions, actual records, and a local-first single-world reading of Wigner's friend.

## Reproduce

From this directory:

~~~text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
python -B examples/check_explanatory_examples_v2.py
python -B examples/check_ontology_examples_v1.py
python -B examples/check_publication_artifacts.py
~~~

The references are embedded in the TeX bibliography; no BibTeX pass is required. Standard TeX Live or MiKTeX packages and Python's standard library suffice for these commands. A third TeX pass may be needed after changes to the table of contents.

The explanatory checks are copied unchanged from the independent analysis workspace so they are self-contained and do not rely on that workspace or a running Kernel. Their source hashes are recorded in the evidence manifest.

Generated Markdown follows the repository's paper artifact refresh workflow. Use the stable paper ID locality-coherent-alternatives-and-records-in-mtt. Its opt-in paper-markdown.lua filter preserves the embedded bibliography, citations, equation links, tables, and standalone abstract. The six publication checks are separate from the 31 explanatory model checks.

## Scope

The paper imports research results at their declared domains. The supplementary ideal quantum calculations are not new MTT source certificates. No ontology primitive has been adopted and no numerical research blocker has been promoted.
