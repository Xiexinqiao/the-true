
from enum import Enum
class PropertyStatus(Enum):
    AVAILABLE = 'Available'
    SOLD = 'Sold'
class Property:
    def __init__(self, property_id, address, price, property_type, status=PropertyStatus.AVAILABLE, owner=None):
        self.property_id = property_id
        self.address = address
        self.price = price
        self.property_type = property_type
        self.status = status
        self.owner = owner

    def __repr__(self):
        return f"Property({self.property_id}, {self.address}, {self.price}, {self.property_type}, {self.status}, {self.owner})"

    def __eq__(self, other):
        return self.property_id == other.property_id

    def __lt__(self, other):
        return self.property_id < other.property_id
