from model import *
from view import *

class OrdersController:
    def add_hd_in_order(self, orders, hd, reserve):
        orders.add_orders(hd)
        for ingredient in hd.ingredients:
            reserve.sub_reserve(ingredient)
        OrderView.display_order(orders)