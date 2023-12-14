# negotiator.py

class Negotiator:
    def check_resources(self):
        self.connect_inventory_db()
        return ("got negotiation req")

    def connect_inventory_db(self):
        pass