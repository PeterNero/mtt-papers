from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BOOK = (
    ROOT
    / "papers"
    / "the-book-on-modal-triplet-theory-a-typed-interpretive-o-4d11c793"
    / "main.tex"
)

FORMAL_ENVIRONMENT_RE = re.compile(
    r"\\begin\{(?:theorem|proposition|lemma|corollary|definition|proof)\}"
)
WORD_RE = re.compile(r"\b[A-Za-z0-9_-]+\b")
DISPLAY_MATH_RE = re.compile(r"(?m)^\s*\\\[\s*$")


def verify() -> dict[str, int]:
    text = BOOK.read_text(encoding="utf-8-sig")
    words = len(WORD_RE.findall(text))
    display_math = len(DISPLAY_MATH_RE.findall(text))
    formal_results = len(FORMAL_ENVIRONMENT_RE.findall(text))
    chapters = len(re.findall(r"\\chapter(?:\*)?\{", text))
    longtables = text.count(r"\begin{longtable}")

    assert text.isascii(), "Book source must remain ASCII"
    assert words >= 8_000, "Book has collapsed back into a short status summary"
    assert chapters >= 24, "Book no longer has broad interpretive coverage"
    assert formal_results == 0, "Book must own no formal result or proof"
    assert display_math <= 4, "Book has become too display-math-heavy"
    assert longtables <= 1, "Book must not become a technical ledger"

    required = (
        r"\Large An Interpretive Guide",
        "This is the plain-language book about Modal Triplet Theory",
        r"\part{The Guiding Picture}",
        r"\chapter{One World, Several Descriptions}",
        r"\chapter{Particles as Persistent Patterns}",
        r"\chapter{Measurement Is an Ordinary Physical Process}",
        r"\chapter{Gravity as Closure Strain}",
        r"\chapter{Memory, Entropy, and Cosmology}",
        "one-shared-physical-primitive/profile tier",
        "q79/Fu--Yau",
        "The shared circle is not physical time",
        "The literal products",
        "The old few-TeV chain",
        "The Born rule",
        r"\chapter{Where to Find the Mathematics}",
    )
    for token in required:
        assert token in text, f"required interpretive/current-corpus token missing: {token}"

    forbidden = (
        "A Typed Interpretive Overview of the Current Program",
        r"\part{The Rigorous Internal Spine}",
        r"\chapter{Hilbert Bundles, Vertical Operators, and Coherence}",
        r"\chapter{Current Claim Ledger}",
        r"\chapter{Notation and Guardrails}",
        "One field. One arena. Three filters. One inequality. One coherent world.",
        "Born weights are basin volumes",
        "completed UV-finite and unitary quantum gravity",
    )
    for token in forbidden:
        assert token not in text, f"retired or ledger-style Book token present: {token}"

    current_note_match = re.search(
        r"\\chapter\*\{Version 11 Revision Note\}(.*?)"
        r"\\chapter\*\{Version 10 Revision Note\}",
        text,
        re.DOTALL,
    )
    assert current_note_match, "Book current revision note is missing or misplaced"
    current_note = current_note_match.group(1)
    required_fields = {
        "Supersedes.": ("Supersedes.",),
        "Reason.": ("Reason.",),
        "Resolution.": ("Resolution.",),
        "Retained result/content.": ("Retained result.", "Retained content."),
        "Remaining boundary.": ("Remaining boundary.", "Open boundary."),
    }
    for field, labels in required_fields.items():
        count = sum(current_note.count(rf"\item[{label}]") for label in labels)
        assert count == 1, (
            f"Book revision note must contain exactly one {field} field"
        )

    return {
        "words": words,
        "chapters": chapters,
        "display_math": display_math,
        "formal_results": formal_results,
        "longtables": longtables,
    }


def main() -> int:
    result = verify()
    print(
        "book interpretive role verified: "
        f"{result['words']} words, {result['chapters']} chapters, "
        f"{result['display_math']} display equations, "
        f"{result['formal_results']} formal results"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
