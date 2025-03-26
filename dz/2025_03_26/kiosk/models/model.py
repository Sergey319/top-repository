class HotDog:
    def __init__(self, name, ingredients):
        price = 0
        for i in ingredients:
            price += i.price
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        return f"{self.name}"

class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"


