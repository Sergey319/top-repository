from models.model import *
from controllers.controller import *
from views.view import *

def add_hd_order(order, hd):
    order.hd.append(hd)
    order.sum += hd.price
    order_view(order)
    return order

def add_sauce_order(order, sauce):
    order.sauce.append(sauce)
    order.sum += sauce.price
    order_view(order)
    return order

def add_topping_order(order, topping):
    order.topping.append(topping)
    order.sum += topping.price
    order_view(order)
    return order