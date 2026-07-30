from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
JSON_REPORT = ROOT / "catalog" / "expository-readability.json"
MARKDOWN_REPORT = ROOT / "EXPOSITORY_READABILITY_AUDIT.md"
REVIEW_DECISIONS = ROOT / "catalog" / "expository-review-decisions.json"

FORMAL_NAMES = (
    "theorem",
    "proposition",
    "lemma",
    "corollary",
    "definition",
    "assumption",
    "conjecture",
)
FORMAL_BLOCK_RE = re.compile(
    rf"\\begin\{{({'|'.join(FORMAL_NAMES)})\}}.*?\\end\{{\1\}}",
    re.DOTALL,
)
PROOF_BLOCK_RE = re.compile(r"\\begin\{proof\}.*?\\end\{proof\}", re.DOTALL)
DISPLAY_MATH_RE = re.compile(
    r"\\\[.*?\\\]|"
    r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}"
    r".*?"
    r"\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}",
    re.DOTALL,
)
HEADING_RE = re.compile(
    r"\\(?:part|chapter|section|subsection|subsubsection)\*?\{([^{}]*)\}"
)
WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z-]*\b")

FORBIDDEN_SERIES_PHRASES = (
    "As both the cornerstone of the Modal Triplet Theory",
    "the series is intended to function simultaneously as a basis",
    "Each paper in the series builds upon its predecessors",
)

REFERENCE_PAPERS = {
    "modal-triplet-theory-foundations",
    "the-book-on-modal-triplet-theory-a-typed-interpretive-o-4d11c793",
}


@dataclass
class PaperReadability:
    paper_id: str
    title: str
    total_words: int
    narrative_words: int
    formal_results: int
    proofs: int
    narrative_words_per_result: float
    orientation: bool
    object_intuition: bool
    argument_flow: bool
    result_interpretation: bool
    concrete_foothold: bool
    limitations: bool
    conclusion: bool
    coverage_dimensions: int
    audit_priority: str
    heuristic_priority: str
    review_status: str
    reviewed_on: str
    review_note: str
    missing_dimensions: list[str]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def strip_comments(text: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def searchable_text(text: str) -> str:
    value = strip_comments(text)
    value = re.sub(r"\\[A-Za-z@]+(?:\[[^\]]*\])?", " ", value)
    value = re.sub(r"[{}$%^_&#~]", " ", value)
    return re.sub(r"\s+", " ", value).lower()


def has_any(value: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, value, flags=re.IGNORECASE) for pattern in patterns)


def classify_priority(
    paper_id: str,
    formal_results: int,
    words_per_result: float,
    coverage: int,
) -> str:
    if paper_id in REFERENCE_PAPERS:
        return "reference_ready"
    if formal_results >= 12 and (words_per_result < 150 or coverage <= 2):
        return "critical"
    if (formal_results >= 8 and words_per_result < 250) or (
        formal_results >= 5 and coverage <= 2
    ):
        return "major"
    if (formal_results >= 3 and words_per_result < 400) or coverage <= 3:
        return "moderate"
    if coverage < 7:
        return "light"
    return "low"


def audit_paper(directory: Path, decisions: dict[str, dict]) -> PaperReadability:
    tex = (directory / "main.tex").read_text(
        encoding="utf-8-sig", errors="replace"
    )
    metadata = read_json(directory / "metadata.json")
    clean = strip_comments(tex)
    formal_blocks = list(FORMAL_BLOCK_RE.finditer(clean))
    proof_blocks = list(PROOF_BLOCK_RE.finditer(clean))

    narrative = FORMAL_BLOCK_RE.sub(" ", clean)
    narrative = PROOF_BLOCK_RE.sub(" ", narrative)
    narrative = DISPLAY_MATH_RE.sub(" ", narrative)
    narrative_plain = searchable_text(narrative)
    full_plain = searchable_text(clean)
    headings = " ".join(HEADING_RE.findall(clean)).lower()

    orientation = has_any(
        headings,
        (
            r"\bintroduction\b",
            r"\boverview\b",
            r"\bmotivation\b",
            r"\bpurpose\b",
            r"how to read",
            r"reader",
            r"\broadmap\b",
            r"status.*scope|scope.*status",
        ),
    )
    object_intuition = has_any(
        full_plain,
        (
            r"in plain language",
            r"in plain terms",
            r"\bintuition\b",
            r"geometric meaning",
            r"physical meaning",
            r"can be understood as",
            r"the central picture",
            r"the idea is",
        ),
    )
    argument_flow = has_any(
        full_plain,
        (
            r"how to read",
            r"dependency",
            r"canonical theorem source",
            r"the next section",
            r"the preceding",
            r"the following .* (?:steps|gates|stages|questions)",
            r"first.*second",
        ),
    )
    result_interpretation = has_any(
        headings + " " + full_plain,
        (
            r"\bdiscussion\b",
            r"\binterpretation\b",
            r"\bconsequence",
            r"what this means",
            r"the practical content",
            r"the .* content of the theorem",
            r"this result (?:means|shows|establishes)",
        ),
    )
    concrete_foothold = bool(re.search(r"\\begin\{example\}", clean)) or has_any(
        headings + " " + full_plain,
        (
            r"\bexample\b",
            r"for example",
            r"as an example",
            r"toy model",
            r"worked case",
            r"finite-dimensional",
        ),
    )
    limitations = has_any(
        headings + " " + full_plain,
        (
            r"\blimitation",
            r"\bboundar",
            r"\bopen (?:problem|question|target|frontier)",
            r"does not",
            r"remain(?:s)? open",
            r"failure mode",
            r"nonpromotion",
            r"\bscope\b",
        ),
    )
    conclusion = has_any(
        headings,
        (
            r"\bconclusion\b",
            r"\bsummary\b",
            r"\boutlook\b",
            r"\bafterword\b",
            r"what .* achieved",
        ),
    )

    dimensions = {
        "orientation": orientation,
        "object_intuition": object_intuition,
        "argument_flow": argument_flow,
        "result_interpretation": result_interpretation,
        "concrete_foothold": concrete_foothold,
        "limitations": limitations,
        "conclusion": conclusion,
    }
    formal_results = len(formal_blocks)
    narrative_words = words(narrative_plain)
    words_per_result = (
        narrative_words / formal_results if formal_results else float(narrative_words)
    )
    coverage = sum(dimensions.values())

    heuristic_priority = classify_priority(
        directory.name, formal_results, words_per_result, coverage
    )
    decision = decisions.get(directory.name, {})
    review_status = str(decision.get("status") or "")
    audit_priority = (
        review_status
        if review_status in {"reviewed", "reference_ready"}
        else heuristic_priority
    )

    return PaperReadability(
        paper_id=directory.name,
        title=str(metadata.get("title") or directory.name),
        total_words=words(searchable_text(clean)),
        narrative_words=narrative_words,
        formal_results=formal_results,
        proofs=len(proof_blocks),
        narrative_words_per_result=round(words_per_result, 1),
        orientation=orientation,
        object_intuition=object_intuition,
        argument_flow=argument_flow,
        result_interpretation=result_interpretation,
        concrete_foothold=concrete_foothold,
        limitations=limitations,
        conclusion=conclusion,
        coverage_dimensions=coverage,
        audit_priority=audit_priority,
        heuristic_priority=heuristic_priority,
        review_status=review_status,
        reviewed_on=str(decision.get("reviewed_on") or ""),
        review_note=str(decision.get("note") or ""),
        missing_dimensions=[
            name for name, present in dimensions.items() if not present
        ],
    )


def find_forbidden_boilerplate() -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for directory in sorted(path for path in PAPERS.iterdir() if path.is_dir()):
        for name in ("main.tex", "series.sty", "paper.md"):
            path = directory / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8-sig", errors="replace")
            for phrase in FORBIDDEN_SERIES_PHRASES:
                if phrase in text:
                    hits.append(
                        {
                            "paper_id": directory.name,
                            "path": path.relative_to(ROOT).as_posix(),
                            "phrase": phrase,
                        }
                    )
    return hits


def audit() -> tuple[list[PaperReadability], list[dict[str, str]]]:
    decisions_payload = (
        read_json(REVIEW_DECISIONS) if REVIEW_DECISIONS.is_file() else {}
    )
    decisions = decisions_payload.get("papers", {})
    rows = [
        audit_paper(directory, decisions)
        for directory in sorted(path for path in PAPERS.iterdir() if path.is_dir())
        if (directory / "main.tex").is_file()
    ]
    return rows, find_forbidden_boilerplate()


def report_payload(
    rows: list[PaperReadability], boilerplate: list[dict[str, str]]
) -> dict:
    priorities = Counter(row.audit_priority for row in rows)
    missing = Counter(
        dimension for row in rows for dimension in row.missing_dimensions
    )
    return {
        "schema": "mtt.expository-readability-audit.v1",
        "generated_on": date.today().isoformat(),
        "papers": len(rows),
        "priority_counts": dict(sorted(priorities.items())),
        "missing_dimension_counts": dict(sorted(missing.items())),
        "forbidden_boilerplate_hits": boilerplate,
        "rows": [asdict(row) for row in rows],
    }


def markdown_report(payload: dict) -> str:
    rows = payload["rows"]
    priority_order = {
        "critical": 0,
        "major": 1,
        "moderate": 2,
        "light": 3,
        "low": 4,
        "reviewed": 5,
        "reference_ready": 6,
    }
    ordered = sorted(
        rows,
        key=lambda row: (
            priority_order[row["audit_priority"]],
            -row["formal_results"],
            row["paper_id"],
        ),
    )
    lines = [
        "# MTT Expository Readability Audit",
        "",
        f"Generated: {payload['generated_on']}",
        "",
        "This is a triage instrument, not a prose-quality certificate. "
        "The heuristic score is preserved in the JSON, while an effective "
        "`reviewed` or `reference_ready` state is assigned only through the "
        "explicit human-review decision file.",
        "",
        f"Canonical papers audited: **{payload['papers']}**.",
        "",
        "## Priority Summary",
        "",
        "| Priority | Papers |",
        "| --- | ---: |",
    ]
    for priority, count in sorted(
        payload["priority_counts"].items(), key=lambda item: priority_order[item[0]]
    ):
        lines.append(f"| {priority} | {count} |")

    lines.extend(
        [
            "",
            "## Missing-Dimension Summary",
            "",
            "| Dimension | Papers flagged |",
            "| --- | ---: |",
        ]
    )
    for dimension, count in payload["missing_dimension_counts"].items():
        lines.append(f"| {dimension} | {count} |")

    lines.extend(
        [
            "",
            "## Revision Queue",
            "",
            "| Effective priority | Heuristic | Paper | Formal results | "
            "Narrative words/result | Coverage | Missing |",
            "| --- | --- | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in ordered:
        missing = ", ".join(row["missing_dimensions"]) or "-"
        lines.append(
            f"| {row['audit_priority']} | {row['heuristic_priority']} | "
            f"`{row['paper_id']}` | "
            f"{row['formal_results']} | {row['narrative_words_per_result']:.1f} | "
            f"{row['coverage_dimensions']}/7 | {missing} |"
        )

    lines.extend(
        [
            "",
            "## Forbidden Boilerplate",
            "",
        ]
    )
    if payload["forbidden_boilerplate_hits"]:
        lines.append(
            f"Found **{len(payload['forbidden_boilerplate_hits'])}** occurrences:"
        )
        lines.append("")
        for hit in payload["forbidden_boilerplate_hits"]:
            lines.append(f"- `{hit['path']}`")
    else:
        lines.append("No forbidden generic series prose remains.")

    lines.extend(
        [
            "",
            "## Use",
            "",
            "Revise papers in coherent dependency batches. For each paper, inspect "
            "the actual formal chain and add paper-specific motivation, object "
            "intuition, examples, result interpretation, limitations, and "
            "downstream role. Re-run this audit after every batch, then compile "
            "and visually inspect each revised PDF.",
            "",
        ]
    )
    return "\n".join(lines)


def write_reports(payload: dict) -> None:
    JSON_REPORT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    MARKDOWN_REPORT.write_text(
        markdown_report(payload), encoding="utf-8", newline="\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--strict-boilerplate", action="store_true")
    args = parser.parse_args()

    rows, boilerplate = audit()
    payload = report_payload(rows, boilerplate)
    if args.write:
        write_reports(payload)

    print(
        json.dumps(
            {
                "papers": payload["papers"],
                "priority_counts": payload["priority_counts"],
                "missing_dimension_counts": payload["missing_dimension_counts"],
                "forbidden_boilerplate_hits": len(boilerplate),
            },
            indent=2,
            sort_keys=True,
        )
    )
    if args.strict_boilerplate and boilerplate:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
