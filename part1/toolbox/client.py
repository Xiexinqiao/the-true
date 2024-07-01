class Client:
    def __init__(self, client_id, name, contact_info, budget):
        if not name:
            raise ValueError("Name cannot be empty")
        if budget < 0:
            raise ValueError("Budget cannot be negative")
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info
        self.budget = budget

    def __repr__(self):
        return f"Client({self.client_id}, '{self.name}', '{self.contact_info}', {self.budget})"

