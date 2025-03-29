from model import *
from view import *


def update_order(orders, hd):
    Orders.add_order(orders, hd)
    display_order(orders)