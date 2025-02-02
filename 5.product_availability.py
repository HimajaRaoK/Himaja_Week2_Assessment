'''5. Create a `Product` class with attributes `name`, `price`, and `stock`. 
Write a method `check_availability(quantity)` that returns whether the requested quantity is available.'''

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def check_availability(self, quantity):
        if quantity <= self.stock:
            print(f"{quantity} {self.name} are available.")
        else:
            print("Not available")

product1 = Product("Pen", 10, 100)

quantity = int(input(f"Enter the quantity of {product1.name} to check availability: "))

product1.check_availability(quantity)
