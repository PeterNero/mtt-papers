import copy
import hashlib
from pathlib import Path
import tempfile
import unittest

from consolidate_research_ownership import reviewed_results, SM, lf_hash, build


class ContextualReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / 'papers' / SM / 'main.tex'
        self.path.parent.mkdir(parents=True)
        self.path.write_bytes(b'Context\nA profile, not a prediction.\n')
        self.results = [{'id': 'sm_test', 'repo_id': 'sm_closure', 'sha256': 'a' * 64}]
        self.review = {'id': 'review', 'state': 'integrated', 'paper_id': SM,
                       'result_ids': ['sm_test'], 'anchors': ['A profile, not a prediction.'],
                       'assessment': 'Read in context.', 'reviewed_at': '2026-09-12',
                       'reviewer': 'Test', 'main_tex_lf_sha256': lf_hash(self.path),
                       'result_hashes': {'sm_test': 'a' * 64}}

    def assess(self):
        return reviewed_results({'reviews': [self.review]}, self.results, self.root)['sm_test']

    def test_context_without_literal_id_is_reviewed(self):
        self.assertEqual(self.assess()['state'], 'integrated')
        self.assertEqual(self.assess()['locations'][0]['line_start'], 2)

    def test_newlines_are_portable(self):
        self.path.write_bytes(self.path.read_bytes().replace(b'\n', b'\r\n'))
        self.assertEqual(self.assess()['state'], 'integrated')

    def test_text_change_invalidates_review(self):
        self.path.write_bytes(self.path.read_bytes() + b'New theorem\n')
        self.assertEqual(self.assess()['state'], 'review_stale')

    def test_artifact_change_invalidates_review(self):
        self.results[0]['sha256'] = 'b' * 64
        self.assertEqual(self.assess()['state'], 'review_stale')

    def test_anchor_removal_is_not_accepted(self):
        self.review['anchors'] = ['Missing location']
        self.assertEqual(self.assess()['state'], 'review_stale')

    def test_duplicate_result_review_rejected(self):
        with self.assertRaises(ValueError):
            reviewed_results({'reviews': [self.review, self.review]}, self.results, self.root)

    def test_unknown_result_rejected(self):
        self.review['result_ids'] = ['not_in_capsule']
        with self.assertRaises(ValueError):
            self.assess()

    def test_foreign_owner_rejected(self):
        self.results[0]['repo_id'] = 'qm_source'
        with self.assertRaises(ValueError):
            self.assess()

    def test_literal_id_does_not_promote_an_unreviewed_result(self):
        self.path.write_text('sm_test\n')
        artifact = self.root / 'artifact.json'
        artifact.write_text('{}')
        row = {**self.results[0], 'sha256': hashlib.sha256(artifact.read_bytes()).hexdigest(),
               'release_path': 'artifact.json', 'tier': 'profile', 'description': 'Supplied values'}
        output = build({'results': [row], 'source_commit': 'a' * 40},
                       {'papers': [{'paper_id': SM}]}, self.root, root=self.root, reviews={})
        self.assertEqual(output['results'][0]['manuscript_integration'], 'unreviewed')
        self.assertTrue(output['results'][0]['reference_scan']['tex'])


if __name__ == '__main__':
    unittest.main()
