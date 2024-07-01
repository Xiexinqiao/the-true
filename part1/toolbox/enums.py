from enum import Enum

class PropertyType(Enum):
    APARTMENT = 'Apartment'
    HOUSE = 'House'
    COMMERCIAL = 'Commercial'
    LAND = 'Land'

class PropertyStatus(Enum):
    AVAILABLE = 'Available'
    SOLD = 'Sold'
