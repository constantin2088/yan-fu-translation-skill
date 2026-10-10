import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from glossary import conflicts
class DomainTests(unittest.TestCase):
 def test_different_contexts_allowed(self):self.assertEqual(conflicts([dict(source='accountability',context='职位',target='责任'),dict(source='accountability',context='审查',target='问责')]),[])
 def test_same_context_conflict(self):self.assertEqual(len(conflicts([dict(source='x',context='a',target='甲'),dict(source='x',context='a',target='乙')])),1)
 def test_duplicate_consistent(self):self.assertEqual(conflicts([dict(source='x',context='a',target='甲')]*2),[])
 def test_missing_context(self):
  with self.assertRaises(ValueError):conflicts([dict(source='x',target='甲')])
 def test_stable_order(self):self.assertEqual(conflicts([dict(source='x',context='a',target='b'),dict(source='x',context='a',target='a')])[0]['targets'],['a','b'])
