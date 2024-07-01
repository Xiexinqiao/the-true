
from enum import Enum

class PropertyType(Enum):
    APARTMENT = 'Apartment'
    HOUSE = 'House'
    COMMERCIAL = 'Commercial'
    LAND = 'Land'

class PropertyStatus(Enum):
    AVAILABLE = 'Available'
    SOLD = 'Sold'
class Property:
    def __init__(self, property_id, address, price, property_type, status='Available', owner=None):
        self.property_id = property_id
        self.address = address
        self.price = price
        self.property_type = PropertyType[property_type.upper()]
        self.status = PropertyStatus[status.upper()]
        self.owner = owner
    
    def __repr__(self):
        return f"Property({self.property_id}, {self.address}, {self.price}, {self.property_type}, {self.status}, {self.owner})"

    def __eq__(self, other):
        return self.property_id == other.property_id

    def __lt__(self, other):
        return self.property_id < other.property_id
