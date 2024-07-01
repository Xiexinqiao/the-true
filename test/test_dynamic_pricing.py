import unittest
from part2.toolbox.dynamic_pricing import DynamicPricingModel
class Property:
    def __init__(self, property_id):
        self.property_id = property_id
        self.price = 0

class TestDynamicPricingModel(unittest.TestCase):
    def setUp(self):
        self.pricing_model = DynamicPricingModel()
        self.property = Property('123')

    def test_track_view(self):
        self.pricing_model.track_view(self.property.property_id)
        self.assertEqual(self.pricing_model.view_counts[self.property.property_id], 1)

    def test_adjust_price_increases_for_many_views(self):
        for _ in range(11):  # 触发价格上涨的阈值
            self.pricing_model.track_view(self.property.property_id)
        base_price = 100
        self.pricing_model.adjust_price(self.property, base_price)
        self.assertEqual(self.property.price, base_price * 1.1)

    def test_adjust_price_decreases_for_few_views(self):
        for _ in range(4):  # 触发价格下降的阈值
            self.pricing_model.track_view(self.property.property_id)
        base_price = 100
        self.pricing_model.adjust_price(self.property, base_price)
        self.assertEqual(self.property.price, base_price * 0.9)

    def test_adjust_price_unchanged_for_average_views(self):
        for _ in range(7):  # 触发价格不变的阈值
            self.pricing_model.track_view(self.property.property_id)
        base_price = 100
        self.pricing_model.adjust_price(self.property, base_price)
        self.assertEqual(self.property.price, base_price)



if __name__ == '__main__':
    unittest.main()
