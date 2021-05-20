
class product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def print_info(self):
        print("Name:", self.name, "Price:", self.price, "Category:", self.category)
        return self
    def update_price(self, new_price):
        self.price = new_price
        return self



