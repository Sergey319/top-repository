class HotDog:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Sauce:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Order:
    def __init__(self, hd, sauce, topping, sum):
        self.hd = hd
        self.sauce = sauce
        self.topping = topping
        self.sum = sum