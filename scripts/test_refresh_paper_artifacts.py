from pathlib import Path
import tempfile
import unittest

from refresh_paper_artifacts import restore_managed_markdown_markers


class ManagedEvidenceHeadingTest(unittest.TestCase):
    def test_both_existing_headings_are_preserved_idempotently(self):
        for heading in ("Computational Evidence and Reproducibility", "Reproducibility and Result Ownership"):
            with self.subTest(heading=heading), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                tex = root / "main.tex"
                tex.write_text("% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE\n", encoding="utf-8")
                markdown = root / "paper.md"
                markdown.write_text(f"# Introduction\n\nContext.\n\n# {heading}\n\nEvidence.\n\n# Conclusion\n\nEnd.\n", encoding="utf-8")
                restore_managed_markdown_markers(root, tex)
                first = markdown.read_text(encoding="utf-8")
                self.assertIn(f"# {heading}", first)
                self.assertEqual(first.count("<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->"), 1)
                self.assertLess(first.index("<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->"), first.index("# Conclusion"))
                restore_managed_markdown_markers(root, tex)
                self.assertEqual(markdown.read_text(encoding="utf-8"), first)

    def test_missing_heading_is_not_silently_accepted(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            tex = root / "main.tex"
            tex.write_text("% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE\n", encoding="utf-8")
            (root / "paper.md").write_text("# Unrelated section\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                restore_managed_markdown_markers(root, tex)


if __name__ == "__main__":
    unittest.main()
