class HotDog:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        price = 0
        for ingredient in ingredients:
            price += ingredient.price
        self.price = price

    def __str__(self):
        hd = f"{self.name} - {self.price} руб."
        return hd

class Ingredient:
    def __init__(self, name, price, purchase_price):
        self.name = name
        self.price = price
        self.purchase_price = purchase_price

class Orders:
    def __init__(self):
        self.orders = []

    def add_order(self, hd):
        self.orders.append(hd)

    def get_orders(self):
        return self.orders

class Reserve:
    def __init__(self):
        self.reserve = []

    def get_reserve(self):
        return self.reserve

    def add_reserve(self, ingredients):
        self.reserve.append(ingredients)

    def sub_reserve(self, ingredients):
        self.reserve.remove(ingredients)