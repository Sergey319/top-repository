from views.view import *

def add_order(orders, order):
    if len(orders) < 3:
        orders.append(order)
        order_view(orders)
        return orders
