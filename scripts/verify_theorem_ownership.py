from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
DECISIONS = ROOT / "catalog" / "expository-review-decisions.json"
READY_STATES = {"reviewed", "reference_ready"}

ENVIRONMENT_RE = re.compile(
    r"\\begin\{(theorem|proposition|lemma|corollary)\}"
    r"(?:\[([^\]]*)\])?"
    r"(.*?)"
    r"\\end\{\1\}",
    re.DOTALL,
)
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")


@dataclass(frozen=True)
class Result:
    paper_id: str
    kind: str
    title: str
    label: str
    body: str


def normalize(value: str) -> str:
    value = re.sub(r"%[^\n]*", "", value)
    value = LABEL_RE.sub("", value)
    return re.sub(r"\s+", " ", value).strip().lower()


def results_for(paper_id: str) -> list[Result]:
    path = PAPERS / paper_id / "main.tex"
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    rows: list[Result] = []
    for match in ENVIRONMENT_RE.finditer(text):
        raw_body = match.group(3)
        label_match = LABEL_RE.search(raw_body)
        rows.append(
            Result(
                paper_id=paper_id,
                kind=match.group(1),
                title=normalize(match.group(2) or ""),
                label=label_match.group(1) if label_match else "",
                body=normalize(raw_body),
            )
        )
    return rows


BOOK = "the-book-on-modal-triplet-theory-a-typed-interpretive-o-4d11c793"
BELL = "temporal-bell-inequalities-and-global-consistency-in-mo-b0f2bdeb"
A0 = "the-modal-triplet-theory-program-a0-a-structural-theory-bebae240"
A1 = "the-modal-triplet-theory-program-a1-coherent-kinematics"
PROJECTION = "the-projection-admissibility-principle-descent-recovery-b0fd6e59"
KINEMATICS = "coherent-kinematics-in-modal-triplet-theory-chart-persi-359fefe8"
FOUNDATION = "modal-triplet-theory-foundations"
FP1 = "fixed-points-i-fixed-points-over-multi-bundle-manifolds-725f9fce"
FP2 = "fixed-points-ii-projected-fixed-points-and-equilibria-i-e079d534"
FP3 = "fixed-points-iii-disturbance-damping-balance-and-stability"
FP4 = "fixed-points-iv-curvature-centroid-motion-and-structura-47f7cbce"
FP5 = "fixed-points-v-curvature-coupling-multi-structure-dynam-e0cf3ba8"
FP6 = "fixed-points-vi-formal-synthesis-and-physical-interpretations"

RELEASE_SCOPE = [
    BOOK,
    BELL,
    A0,
    A1,
    PROJECTION,
    KINEMATICS,
    FOUNDATION,
    FP1,
    FP2,
    FP3,
    FP4,
    FP5,
    FP6,
]


def reviewed_release_scope() -> list[str]:
    document = json.loads(DECISIONS.read_text(encoding="utf-8-sig"))
    decisions = document.get("papers") or {}
    return sorted(
        paper_id
        for paper_id, decision in decisions.items()
        if str((decision or {}).get("status") or "") in READY_STATES
    )


def cross_paper_duplicates(
    rows: list[Result], attribute: str
) -> list[list[Result]]:
    grouped: dict[str, list[Result]] = defaultdict(list)
    for row in rows:
        key = getattr(row, attribute)
        if key:
            grouped[key].append(row)
    return [
        values
        for values in grouped.values()
        if len({value.paper_id for value in values}) > 1
    ]


def verify() -> tuple[int, int]:
    active_scope = sorted(set(RELEASE_SCOPE) | set(reviewed_release_scope()))
    scoped = {paper_id: results_for(paper_id) for paper_id in active_scope}

    assert not scoped[BOOK], "The Book must own no formal results"
    assert {row.label for row in scoped[BELL]} == {
        "thm:lgi",
        "prop:nrs",
    }, "Temporal Bell must contain exactly its LGI and no-retro results"
    assert not scoped[A1], "Program A1 must import, not duplicate, its theorem chain"

    prohibited = {
        A0: {
            "projection--descent and recovery",
            "finite-diameter contraction obstruction",
            "measure-dependent reduced kernel",
        },
        FOUNDATION: {
            "projected time-step existence",
            "strict-lyapunov equilibrium promotion",
            "banach gate",
            "autonomous descent criterion",
        },
        FP5: {"exact scalar ou variance"},
    }
    for paper_id, titles in prohibited.items():
        present = {row.title for row in scoped[paper_id]}
        overlap = present & titles
        assert not overlap, f"{paper_id} repeats owned titles: {sorted(overlap)}"

    assert {row.label for row in scoped[FP6]} == {
        "prop:bilocal",
        "prop:mediator",
    }, "FP VI must own only its bilocal and mediator propositions"

    all_scoped = [row for values in scoped.values() for row in values]
    duplicate_bodies = cross_paper_duplicates(all_scoped, "body")
    assert not duplicate_bodies, (
        "exact formal-result bodies are duplicated in release scope: "
        + "; ".join(
            ", ".join(sorted({row.paper_id for row in group}))
            for group in duplicate_bodies
        )
    )

    all_rows: list[Result] = []
    for tex_path in sorted(PAPERS.glob("*/main.tex")):
        all_rows.extend(results_for(tex_path.parent.name))
    global_duplicates = cross_paper_duplicates(all_rows, "body")
    return len(all_scoped), len(global_duplicates)


def main() -> int:
    try:
        scoped_count, global_duplicate_groups = verify()
    except Exception as error:
        print(f"theorem ownership verification failed: {error}", file=sys.stderr)
        return 1
    print(
        "theorem ownership verified: "
        f"{scoped_count} scoped formal results, "
        f"{global_duplicate_groups} known global duplicate-body groups"
    )
    if global_duplicate_groups:
        print(
            "note: global duplicates remain a release blocker outside the "
            "verified scope; see THEOREM_OWNERSHIP_AND_STANDALONE_POLICY.md"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
