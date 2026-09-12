"""Small regression witnesses for the September editorial corrections."""
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SM = "modal-triplet-theory-from-mtt-to-standard-model-a-rigor-923ad6b1"
COH = "cohesive-closure-repair-and-its-hodge-kernel-and-projection-shadows"


class EditorialImportTests(unittest.TestCase):
    def test_metadata_abstract_is_plain_text_and_release_unchanged(self):
        meta = json.loads((ROOT / "papers" / SM / "metadata.json").read_text())
        self.assertNotIn("\\", meta["abstract"])
        self.assertEqual(meta["current_version"], "v4")
        self.assertEqual(meta["latest_zenodo_release"]["version"], "v3")
        self.assertEqual(meta["latest_zenodo_release"]["doi"],
                         "10.5281/zenodo.21720135")

    def test_explicit_incidence_correction(self):
        ranks = [3, 8, 8, 80, 3]
        incidence = [[1, 1, 0, 0, 1], [1, 0, 1, 0, 1],
                     [1, 0, 0, 1, 1], [1, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]]

        def count(rows):
            blocks = [(i, j) for i in range(5) for j in range(5)
                      if any(row[i] and row[j] for row in rows)]
            return len(blocks), sum(ranks[i] * ranks[j] for i, j in blocks)

        self.assertEqual(count(incidence), (25, 10404))
        self.assertEqual(count(incidence[:4] + incidence[5:]), (19, 7716))
        self.assertEqual(10404 - 7716, 2688)
        self.assertEqual(30**2 + 8 * 9**2, 1548)

    def test_isometric_pullback_does_not_imply_reduction(self):
        # J'=(1,1), T=(1,0)^t, U=1 and J=1: the chain row holds.
        Jprime = (1, 1)
        T = (1, 0)
        self.assertEqual(sum(a * b for a, b in zip(Jprime, T)), 1)
        Hprime = [[a * b for b in Jprime] for a in Jprime]
        HprimeT = tuple(sum(row[j] * T[j] for j in range(2))
                       for row in Hprime)
        self.assertEqual(sum(T[i] * HprimeT[i] for i in range(2)), 1)
        self.assertNotEqual(HprimeT, T)
        tex = (ROOT / "papers" / COH / "main.tex").read_text()
        self.assertIn(r"J'^\dagger U=TJ^\dagger", tex)
        self.assertIn("rather than an onto equivalence", tex)


if __name__ == "__main__":
    unittest.main()
