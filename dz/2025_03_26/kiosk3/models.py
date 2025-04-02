class Reserve:
    def __init__(self, budget):
        self.budget = budget
        self.reserve = []

    def add_ingredient(self, ingredient):
        return self.reserve.append(ingredient)

    def sub_ingredient(self, ingredient):
        return self.reserve.remove(ingredient)

    def get_reserve(self):
        return self.reserve

class Ingredient:
    def __init__(self, name, price, purchase_price):
        self.name = name
        self.price = price
        self.purchase_price = purchase_price

class HotDog:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients =ingredients

