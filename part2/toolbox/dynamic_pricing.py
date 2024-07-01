class DynamicPricingModel:
    def __init__(self):
        self.view_counts = {}

    def track_view(self, property_id):
        if property_id not in self.view_counts:
            self.view_counts[property_id] = 0
        self.view_counts[property_id] += 1

    def adjust_price(self, property, base_price):
        views = self.view_counts.get(property.property_id, 0)
        if views > 10:
            property.price = base_price * 1.1
        elif views < 5:
            property.price = base_price * 0.9
        else:
            property.price = base_price
