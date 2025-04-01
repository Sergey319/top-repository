
from view import *

class OrdersController:
    def add_hd_in_order(self, orders, hd, reserve):
        order = True
        for ingredient in hd.ingredients:
            if reserve.get_count_ingredient_in_reserve(ingredient) > 3:
                reserve.sub_reserve(ingredient)
            elif 0 < reserve.get_count_ingredient_in_reserve(ingredient) <= 3:
                print(f"!!!!! Ингредиент: {ingredient.name} осталось {reserve.get_count_ingredient_in_reserve(ingredient)} штук !!!!!")
                reserve.sub_reserve(ingredient)
            elif reserve.get_count_ingredient_in_reserve(ingredient) == 0:
                print(f"!!!!!!!!!!! Ингредиента {ingredient.name} нет !!!!!!!!!!!")
                order = False
        if order == True:
            orders.add_orders(hd)
        OrderView.display_order(orders)