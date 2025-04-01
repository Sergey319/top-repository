from model import *
from view import *

class OrdersController:
    def add_hd_in_order(self, orders, hd, reserve):
        for ingredient in hd.ingredients:
            if 0 < reserve.get_count_ingredient_in_reserve(ingredient) <= 3:
                print(f"!!!!! Ингредиент: {ingredient.name} осталось {reserve.get_count_ingredient_in_reserve(ingredient)} штук !!!!!")
        orders.add_orders(hd)
        for ingredient in hd.ingredients:
            reserve.sub_reserve(ingredient)
        OrderView.display_order(orders)