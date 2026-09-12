"""Check this manuscript's generated representations, not its physical claims."""

import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicationArtifacts(unittest.TestCase):
    maxDiff = 400
    @classmethod
    def setUpClass(cls):
        cls.tex = (ROOT / "main.tex").read_text(encoding="utf-8")
        cls.md = (ROOT / "paper.md").read_text(encoding="utf-8")
        cls.metadata = json.loads((ROOT / "metadata.json").read_text(encoding="utf-8"))

    def test_citation_markers_and_bibliography_survive(self):
        keys = re.findall(r"\\bibitem\{([^}]+)\}", self.tex)
        self.assertEqual(len(keys), 29)
        cited = [key.strip() for group in re.findall(r"\\cite\{([^}]+)\}", self.tex)
                 for key in group.split(",")]
        for number, key in enumerate(keys, 1):
            self.assertEqual(self.md.count(f'<a id="ref-{key}"></a>'), 1)
            self.assertIn(f"\\[{number}\\]", self.md)
        for key in cited:
            self.assertIn(f"(#ref-{key})", self.md)
        self.assertNotIn('class="thebibliography"', self.md)

    def test_tables_preserved_without_duplicate_headers(self):
        self.assertEqual(self.md.count("| Feature | Electron | Photon |"), 1)
        self.assertEqual(self.md.count("| Expression | Meaning used here |"), 1)
        self.assertNotIn('class="tabularx"', self.md)

    def test_equation_and_section_links_are_resolved(self):
        labels = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", self.tex)
        for label in labels:
            self.assertIn(f'<a id="{label}"></a>', self.md)
            self.assertTrue(f"(#{label})" in self.md, f"Unresolved reference: {label}")
        for key, number in {"eq:nosignal": 4, "eq:interference": 7,
                            "eq:monitor": 10, "eq:448": 22}.items():
            self.assertTrue(f"[({number})](#{key})" in self.md, f"Wrong equation number: {key}")
        self.assertIn("[12](#sec:results)", self.md)
        self.assertNotIn("data-reference=", self.md)

    def test_standalone_abstract_and_scope(self):
        self.assertIn("## Abstract", self.md)
        self.assertIn("# References", self.md)
        self.assertIn("Version 1.0 Revision Note", self.md)
        self.assertIn("Version 2 Revision Note", self.md)
        self.assertIn("<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->", self.md)
        self.assertTrue(re.search(r"(?m)^```\s*text\s*$", self.md), "Reproduction commands lack a fenced block")
        for label in ("Supersedes:", "Reason:", "Resolution:", "Retained content:", "Remaining boundary:"):
            self.assertTrue(f"**{label}**" in self.md, f"Missing version label: {label}")
        self.assertTrue(self.metadata["author_review_required"])
        self.assertIsNone(self.metadata["latest_zenodo_release"])

    def test_no_duplicate_formal_theorems(self):
        self.assertFalse(re.search(r"\\begin\{(?:theorem|lemma|proposition|proof)\}", self.tex))

    def test_hashes_match_canonical_files(self):
        self.assertEqual(self.metadata["result_refs"], sorted(set(self.metadata["result_refs"])))
        canonical = json.dumps(self.metadata["source_files"], sort_keys=True,
                               separators=(",", ":"), ensure_ascii=True).encode()
        self.assertEqual(self.metadata["source_tree_sha256"], hashlib.sha256(canonical).hexdigest())
        for key, filename in (("main_tex_sha256", "main.tex"), ("paper_md_sha256", "paper.md")):
            self.assertEqual(self.metadata[key], hashlib.sha256((ROOT / filename).read_bytes()).hexdigest())
        for row in self.metadata["source_files"]:
            data = (ROOT / row["path"]).read_bytes()
            self.assertEqual(row["bytes"], len(data))
            self.assertEqual(row["sha256"], hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    unittest.main(verbosity=2)
