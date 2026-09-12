"""Guard the reviewed FP citation direction; this is not a proof checker."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

from verify_theorem_ownership import FP1, FP2, FP3, FP4, FP5, FP6

ROOT = Path(__file__).resolve().parents[1]
FP_ORDER = (FP1, FP2, FP3, FP4, FP5, FP6)
POLICY = ROOT / "catalog/fp-foundational-dependencies.json"
CITATION = re.compile(
    r"\\[a-zA-Z]*[Cc]ite[a-zA-Z]*\*?"
    r"(?:\s*\[[^\]]*\])*\s*\{([^{}]*)\}"
)
EXTERNAL_INPUT = re.compile(r"\\(?:input|include|externaldocument|addbibresource)\b")
RESEARCH_SOURCE = re.compile(
    r"NeroQMSP2026|NeroFiniteMode2026|mtt-qm-source-proof|"
    r"github\.com/PeterNero/(?:mtt-results|mtt-papers|mtt-.*proof)|"
    r"\.packet\.json|Independent downstream q79 status", re.I
)


def without_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", tex)


def bibliography_snapshot(tex: str, directory: Path) -> tuple[str, set[str]]:
    """Fingerprint the supported literal BibTeX/inline sources, without parsing fields."""
    parts = []
    keys = set()
    for names in re.findall(r"\\bibliography\s*\{([^{}]+)\}", tex):
        for name in names.split(","):
            path = Path(name.strip())
            if path.suffix != ".bib":
                path = path.with_suffix(".bib")
            assert not path.is_absolute() and len(path.parts) == 1, "nonlocal bibliography"
            content = (directory / path).read_text(encoding="utf-8-sig")
            parts.append(path.name + "\n" + content)
            keys.update(re.findall(r"@\w+\s*\{\s*([^,{}\s]+)\s*,", content))
    for content in re.findall(
        r"\\begin\{thebibliography\}\{[^}]*\}(.*?)\\end\{thebibliography\}", tex, re.S
    ):
        parts.append("inline\n" + content)
        keys.update(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", content))
    assert parts, "no recognized bibliography"
    digest = hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()
    return digest, keys


def check_paper(tex: str, directory: Path, order: int, row: dict) -> dict:
    source = without_comments(tex)
    assert not EXTERNAL_INPUT.search(source), "unreviewed external TeX source mechanism"
    assert not RESEARCH_SOURCE.search(source), "downstream MTT source in foundation"
    assert not re.search(r"\\(?:def|let)\s*\\(?:cite|nocite)", source), "citation alias"
    standard = set(row["standard_reference_keys"])
    earlier = row["earlier_fp_reference_keys"]
    assert not standard.intersection(earlier), "ambiguous reference type"
    for key, number in earlier.items():
        assert isinstance(number, int) and 1 <= number < order, f"non-earlier FP input: {key}"
    digest, bibliography = bibliography_snapshot(source, directory)
    assert digest == row["reviewed_bibliography_sha256"], "bibliography changed: contextual review required"
    assert bibliography == standard | set(earlier), "unclassified bibliography entry"
    cited = {key.strip() for group in CITATION.findall(source) for key in group.split(",")}
    assert cited <= bibliography, f"unreviewed citation: {sorted(cited - bibliography)}"
    return {"paper": order, "earlier_fp_inputs": sorted(set(earlier.values())),
            "cited_keys": sorted(cited), "bibliography_reviewed": True}


def verify(root: Path = ROOT) -> list[dict]:
    policy = json.loads((root / "catalog/fp-foundational-dependencies.json").read_text())
    assert policy["schema"] == "mtt.fp-foundational-dependencies.v1"
    assert set(policy["papers"]) == set(FP_ORDER), "all six foundations must be reviewed"
    result = []
    for number, pid in enumerate(FP_ORDER, 1):
        directory = root / "papers" / pid
        tex = (directory / "main.tex").read_text(encoding="utf-8-sig")
        style = without_comments((directory / "series.sty").read_text(encoding="utf-8-sig"))
        assert not EXTERNAL_INPUT.search(style) and not CITATION.search(style), f"{pid}: style imports"
        try:
            result.append(check_paper(tex, directory, number, policy["papers"][pid]))
        except AssertionError as exc:
            raise AssertionError(f"{pid}: {exc}") from exc
    return result


if __name__ == "__main__":
    print(json.dumps({"foundational_dependencies": verify()}, indent=2))
