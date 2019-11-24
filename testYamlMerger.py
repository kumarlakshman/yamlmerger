import unittest
import yamlMerger

class TestYamlMerges(unittest.TestCase):

    def test_merge(self):
        parent_set = {'size': 12, 'color': 'blue','actual':'3.6'}
        child_set = {'size': 8,'count': 2,'actual':'3.2'}
        result_set = {'size': 8, 'color': 'blue','count': 2,'actual':'3.2'}
        output = yamlMerger.yaml_merger(child_set,parent_set)
        self.assertEqual(output, result_set)
        print("UnitTest for String,Int and Float Merge is success")

    def test_list_merge(self):
        parent_set = {'wishlist': ["car","pony"]}
        child_set = {'wishlist': ["worldpeace"]}
        result_set = {'wishlist': ["worldpeace","car", "pony"]}
        output = yamlMerger.yaml_merger(child_set,parent_set)
        self.assertEqual(output, result_set)
        print("UnitTest for List Merge is success")

    def test_dict_merge(self):
        parent_set = {'todo': {'laundry': {'priority': 'low'}, 'dishes': {'priority': 'high'}}}
        child_set = {'todo': {'dishes': {'priority': 'low'}, 'vacuum': {'priority': 'high'}}}
        result_set = {'todo': {'dishes': {'priority': 'low'}, 'vacuum': {'priority': 'high'},'laundry': {'priority': 'low'}}}
        output = yamlMerger.yaml_merger(child_set,parent_set)
        self.assertEqual(output, result_set)
        print("UnitTest for Dictnary Merge is success")

if __name__ == '__main__':
    unittest.main()
