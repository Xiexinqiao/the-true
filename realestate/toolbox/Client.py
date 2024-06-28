


class Client:
    def __init__(self, client_id, name, contact_info, budget,price):
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info
        self.budget = budget
        self.price = price
    def __repr__(self):
        return f"Client({self.client_id}, {self.name}, {self.contact_info}, {self.budget}, {self.price})"