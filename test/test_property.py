import unittest
from part1.toolbox.property import Property
from part1.toolbox.property import PropertyType
from part1.toolbox.property import PropertyStatus

class TestProperty(unittest.TestCase):
    def test_init(self):
        property = Property('P123', '123 Main St', 250000, 'Apartment')
        self.assertEqual(property.property_id, 'P123')
        self.assertEqual(property.address, '123 Main St')
        self.assertEqual(property.price, 250000)
        self.assertEqual(property.property_type, PropertyType.APARTMENT)
        self.assertEqual(property.status, PropertyStatus.AVAILABLE)
        self.assertIsNone(property.owner)

    def test_init_with_status_and_owner(self):
        property = Property('P123', '123 Main St', 250000, 'House', 'Sold', 'John Doe')
        self.assertEqual(property.status, PropertyStatus.SOLD)
        self.assertEqual(property.owner, 'John Doe')

    def test_eq(self):
        property1 = Property('P123', '123 Main St', 250000, 'House')
        property2 = Property('P123', '456 Elm St', 300000, 'Apartment')
        property3 = Property('P456', '789 Oak St', 200000, 'Land')
        self.assertEqual(property1, property2)
        self.assertNotEqual(property1, property3)

    def test_lt(self):
        property1 = Property('P123', '123 Main St', 250000, 'House')
        property2 = Property('P456', '456 Elm St', 300000, 'Apartment')
        self.assertLess(property1, property2)
        self.assertGreater(property2, property1)

if __name__ == '__main__':
    unittest.main()
