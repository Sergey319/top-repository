class HotDog:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}"

class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"

class Order:
    def __init__(self, hd):
        self.hd = hd

    def __str__(self):
        return f"{self.hd}"