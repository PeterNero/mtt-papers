import json
from pathlib import Path
import tempfile
import unittest

from verify_fp_foundational_dependencies import bibliography_snapshot, check_paper, verify


class FoundationDependencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.tex = (r"\cite{Earlier,Standard}" + "\n"
                    r"\begin{thebibliography}{9}" + "\n"
                    r"\bibitem{Earlier} Fixed Points I, version 7." + "\n"
                    r"\bibitem{Standard} Standard mathematics." + "\n"
                    r"\end{thebibliography}")
        digest, _ = bibliography_snapshot(self.tex, self.directory)
        self.row = {"earlier_fp_reference_keys": {"Earlier": 1},
                    "standard_reference_keys": ["Standard"],
                    "reviewed_bibliography_sha256": digest}

    def test_earlier_reference_is_allowed(self):
        self.assertEqual(check_paper(self.tex, self.directory, 2, self.row)["earlier_fp_inputs"], [1])

    def test_later_or_self_reference_is_rejected(self):
        for target in (2, 6):
            self.row["earlier_fp_reference_keys"]["Earlier"] = target
            with self.assertRaisesRegex(AssertionError, "non-earlier"):
                check_paper(self.tex, self.directory, 2, self.row)

    def test_unknown_and_wildcard_citations_are_rejected(self):
        for citation in (r"\cite{NewMTT}", r"\nocite{*}", r"\textcite[note]{NewMTT}"):
            with self.assertRaisesRegex(AssertionError, "unreviewed citation"):
                check_paper(self.tex + citation, self.directory, 2, self.row)

    def test_reused_key_cannot_hide_changed_reference(self):
        with self.assertRaisesRegex(AssertionError, "bibliography changed"):
            check_paper(self.tex.replace("Standard mathematics", "Later MTT theorem"),
                        self.directory, 2, self.row)

    def test_external_sources_and_downstream_packets_are_rejected(self):
        for addition in (r"\input{later}", " mtt-qm-source-proof", " result.packet.json"):
            with self.assertRaises(AssertionError):
                check_paper(self.tex + addition, self.directory, 2, self.row)

    def test_all_six_current_manuscripts(self):
        self.assertEqual(len(verify()), 6)

    def test_fp4_constrained_example(self):
        from fractions import Fraction
        schur = 2 - Fraction(1, 3)
        inverse_11 = Fraction(3, 5)
        self.assertEqual(schur, 1 / inverse_11)
        self.assertNotEqual(schur, 2)


if __name__ == "__main__":
    unittest.main()
