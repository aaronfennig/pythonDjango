import uuid
class store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, product_name):
        self.products.remove(product_name)
        saleID = uuid.uuid4()
        print("The ID for this sale is:", saleID)
        return self
    def printProductList(self):
        for each in self.products:
            print("Name:", each.name, "Price:", each.price,"Category:", each.category)
        return self
    def inflationAdjustment(self, inflationRate = 1.02):
        for each in self.products:
            each.price *= inflationRate
            print(each.name, each.price)
        return self
    def setClearance(self, clearanceRate = .75):
        for each in self.products:
            each.price *= clearanceRate
            print(each.name, each.price)
        return self

