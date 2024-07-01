import unittest
from part2.toolbox.property_matcher import PropertyMatcher
class TestPropertyMatcher(unittest.TestCase):
    def setUp(self):
        self.matcher = PropertyMatcher()
        self.client = {'budget': 300000}

        self.properties = [
            {'price': 100000},
            {'price': 200000},
            {'price': 400000},
            {'price': 500000}
        ]

    def test_normal_case(self):
        matched = self.matcher.match_properties(self.client, self.properties)
        self.assertEqual(len(matched), 2)
        self.assertTrue(all(prop['price'] <= self.client['budget'] for prop in matched))

    def test_no_match(self):
        self.client['budget'] = 0
        matched = self.matcher.match_properties(self.client, self.properties)
        self.assertEqual(len(matched), 0)

    def test_all_match(self):
        self.client['budget'] = 500000
        matched = self.matcher.match_properties(self.client, self.properties)
        self.assertEqual(len(matched), 4)

    def test_budget_just_enough(self):
        self.client['budget'] = 100000
        matched = self.matcher.match_properties(self.client, self.properties)
        self.assertEqual(len(matched), 1)
        self.assertEqual(matched[0]['price'], 100000)

    def test_empty_list(self):
        matched = self.matcher.match_properties(self.client, [])
        self.assertEqual(len(matched), 0)

    def test_negative_price_property(self):
        self.properties.append({'price': -50000})
        matched = self.matcher.match_properties(self.client, self.properties)
        self.assertTrue(all(prop['price'] > 0 for prop in matched))

    def test_invalid_budget(self):
        with self.assertRaises(TypeError):
            self.client['budget'] = 'not a number'
            self.matcher.match_properties(self.client, self.properties)

        with self.assertRaises(TypeError):
            self.client['budget'] = None
            self.matcher.match_properties(self.client, self.properties)

if __name__ == '__main__':
    unittest.main()
