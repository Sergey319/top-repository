from views import *
from models import *
from main import *


class ReserveControllers:
    def __init__(self, reserve, ingredient=None, count=1, ingredients=None):
        self.reserve = reserve
        self.ingredient = ingredient
        self.count = count
        self.ingredients = ingredients

    def purchase(self):
        price = 0
        for _ in range(self.count):
            price += self.ingredient.purchase_price
        if self.reserve.budget >= price:
            self.reserve.budget -= price
            for _ in range(self.count):
                self.reserve.add_ingredient(self.ingredient)
            return self.reserve
        else:
            print("!!!!! НЕ ХВАТАЕТ СРЕДСТВ !!!!!")

    def auto_purchase(self):
        while True:
            if self.reserve.budget > 0:
                for ingredient in self.ingredients:
                    ReserveControllers(self.reserve, ingredient).purchase()
            else:
                return self.reserve

class OrdersControllers:
    def controller_add_order(self, orders, hd):
        return orders.add_order(hd)






