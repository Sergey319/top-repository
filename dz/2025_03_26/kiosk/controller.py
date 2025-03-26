

from view import *

def add_order(orders, order, warehouse):
    mess = False
    if not warehouse:
        message_error_warehouse()
        exit()
    for ingredient in order.ingredients:
        if ingredient not in warehouse:
            message_error_ingredient(ingredient)
            mess = True
    if mess:
        return orders
    for ingredient in order.ingredients:
        sub_warehouse(warehouse, ingredient)
    orders.append(order)
    order_view(orders)


def add_warehouse(warehouse, ingredient):
    warehouse.append(ingredient)
    warehouse_view(warehouse, ingredient)
    return warehouse

def sub_warehouse(warehouse, ingredient):
    warehouse.remove(ingredient)
    warehouse_view(warehouse, ingredient)
    return warehouse