## Items should be a list of products objects of the type product class
class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.price = price
        self.amount = amount
