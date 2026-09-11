class Product:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_product_info(self, amount):
        if self.quantity + amount < 0:
            self.quantity += amount
            print("Stock is empty")
        else:
            print(self.quantity)

    def total_value(self):
        return self.price * self.quantity

produkti = Product("Banana", 1.50, 50)
print(produkti.update_product_info(10))
print(produkti.total_value())
