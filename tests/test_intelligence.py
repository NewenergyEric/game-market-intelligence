import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('intelligence',ROOT/'scripts/intelligence.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class IntelligenceTests(unittest.TestCase):
    def setUp(self): self.data=json.loads((ROOT/'examples/merge-research.json').read_text(encoding='utf-8'))
    def test_missing_market_numbers_are_preserved(self):
        self.assertEqual(module.validate(self.data),[])
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory)/'report';module.render(self.data,out)
            result=json.loads((out/'report.json').read_text(encoding='utf-8'))
            self.assertIsNone(result['claims'][0]['value'])
            self.assertIn('未知', (out/'report.html').read_text(encoding='utf-8'))
    def test_stated_revenue_needs_specific_evidence(self):
        self.data['claims'][0]['value']=123
        self.assertTrue(module.validate(self.data))
    def test_confirmation_needs_authority(self):
        self.data['recommendation']['status']='confirmed'
        self.assertTrue(module.validate(self.data))
    def test_render_does_not_execute_html(self):
        self.data['title']='<script>alert(1)</script>'
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory)/'report';module.render(self.data,out)
            content=(out/'report.html').read_text(encoding='utf-8')
            self.assertNotIn('<script>',content)
            self.assertIn('&lt;script&gt;',content)
    def test_revenue_routing_excludes_ratings_and_steam_activity(self):
        sources=module.catalog();ids={s['id'] for s in module.select_sources(sources,topic='revenue')}
        self.assertNotIn('metacritic',ids);self.assertNotIn('steamdb',ids)
        self.assertEqual(len(sources),len({s['id'] for s in sources}))
        self.assertFalse(any(s['automated_adapter'] for s in sources))
        self.assertNotIn('data-ai',{s['id'] for s in sources})
        self.assertLessEqual({s['verification'] for s in sources},{'candidate','entry_checked','file_import','limited'})
    def test_public_merge_case_is_valid_and_stays_proposed(self):
        case=json.loads((ROOT/'case-studies/merge-community-public-signals/report.json').read_text(encoding='utf-8'))
        self.assertEqual(module.validate(case),[])
        self.assertEqual(case['recommendation']['status'],'proposed')
        self.assertEqual({c['kind'] for c in case['claims']},{'estimate','observed'})
        self.assertIn('investgame-mobile-landscape-2026',{s['id'] for s in module.catalog()})

if __name__=='__main__': unittest.main()
