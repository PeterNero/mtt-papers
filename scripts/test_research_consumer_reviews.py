from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from research_consumer_reviews import reviewed_consumers


class ConsumerReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/'catalog').mkdir()
        text = 'Context: exact owner theorem, conditional physical bridge.\n'
        sha = hashlib.sha256(text.encode()).hexdigest()
        for name in ('owner','consumer'):
            path = self.root/'papers'/name
            path.mkdir(parents=True)
            (path/'main.tex').write_text(text, encoding='utf-8')
            (path/'metadata.json').write_text('{}', encoding='utf-8')
        self.ownership = {'results':[{'result_id':'source','sha256':'a'*64,
            'integration_owner':'owner','contextual_review':{
                'state':'integrated','stale_reasons':[], 'main_tex_lf_sha256':sha}}]}
        self.row = {'id':'review1','paper_id':'consumer','reviewer':'test',
            'reviewed_at':'2026-09-12','state':'integrated',
            'assessment':'Contextual import of the exact owner theorem with its physical bridge remaining conditional.',
            'anchors':['conditional physical bridge'], 'main_tex_lf_sha256':sha,
            'result_ids':['R.SOURCE'],'curated_result_ids':['source'],
            'result_hashes':{'source':'a'*64}}

    def run_document(self, rows):
        (self.root/'catalog/research-consumer-reviews.json').write_text(json.dumps({
            'schema':'mtt.research-consumer-reviews.v1',
            'result_source_map': {'R.SOURCE': ['source']},
            'reviews':rows}), encoding='utf-8')
        return reviewed_consumers(self.root,self.ownership)

    def test_consumer_does_not_change_owner(self):
        before = deepcopy(self.ownership)
        result = self.run_document([self.row])
        self.assertEqual(self.ownership,before)
        self.assertEqual(result[0]['canonical_owner_papers'], {'source':'owner'})
        self.assertEqual(result[0]['locations'][0]['line_start'],1)

    def test_stale_manuscript_fails(self):
        self.row['main_tex_lf_sha256']='b'*64
        with self.assertRaisesRegex(ValueError,'stale consumer manuscript'):
            self.run_document([self.row])

    def test_wrong_source_hash_fails(self):
        self.row['result_hashes']['source']='b'*64
        with self.assertRaisesRegex(ValueError,'stale consumer source'):
            self.run_document([self.row])

    def test_owner_not_reviewed_fails(self):
        self.ownership['results'][0]['contextual_review']['state']='unreviewed'
        with self.assertRaisesRegex(ValueError,'unreviewed consumer source owner'):
            self.run_document([self.row])

    def test_owner_changed_fails(self):
        (self.root/'papers/owner/main.tex').write_text('changed',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'stale canonical owner'):
            self.run_document([self.row])

    def test_missing_anchor_fails(self):
        self.row['anchors']=['never written']
        with self.assertRaisesRegex(ValueError,'missing consumer evidence anchor'):
            self.run_document([self.row])

    def test_duplicate_pair_fails(self):
        other = dict(self.row,id='review2')
        with self.assertRaisesRegex(ValueError,'duplicate consumer placement'):
            self.run_document([self.row,other])

    def test_not_applicable_is_explicit_review_not_proof(self):
        self.row['state']='not_applicable'
        self.assertEqual(self.run_document([self.row])[0]['state'],'not_applicable')

    def test_noncanonical_path_fails(self):
        self.row['paper_id']='../../outside'
        with self.assertRaisesRegex(ValueError,'invalid consumer paper path'):
            self.run_document([self.row])

    def test_windows_newlines_have_portable_hash_and_line_number(self):
        text = 'First line.\nContext: exact owner theorem, conditional physical bridge.\n'
        sha = hashlib.sha256(text.encode()).hexdigest()
        for name in ('owner', 'consumer'):
            (self.root/'papers'/name/'main.tex').write_bytes(text.replace('\n','\r\n').encode())
        self.row['main_tex_lf_sha256'] = sha
        self.ownership['results'][0]['contextual_review']['main_tex_lf_sha256'] = sha
        self.assertEqual(self.run_document([self.row])[0]['locations'][0]['line_start'],2)

    def test_unregistered_kernel_result_cannot_be_cleared(self):
        self.row['result_ids'] = ['R.UNRELATED']
        with self.assertRaisesRegex(ValueError,'unregistered Kernel source mapping'):
            self.run_document([self.row])

    def test_per_review_binding_cannot_escape_registered_family(self):
        self.row['kernel_result_sources'] = {'R.SOURCE': ['unrelated']}
        with self.assertRaisesRegex(ValueError, 'unregistered per-review source binding'):
            self.run_document([self.row])

    def test_exact_per_review_binding_is_accepted(self):
        self.row['kernel_result_sources'] = {'R.SOURCE': ['source']}
        self.assertEqual(len(self.run_document([self.row])), 1)


if __name__=='__main__':
    unittest.main()
