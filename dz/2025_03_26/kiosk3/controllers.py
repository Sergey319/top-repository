from views import *
from models import *

def purchase(reserve, ingredient, count):
    price = 0
    for _ in range(count):
        price += ingredient.purchase_price
    if reserve.budget >= price:
        reserve.budget -= price
        for _ in range(count):
            reserve.add_ingredient(ingredient)
        return reserve
    else:
        print("!!!!! НЕ ХВАТАЕТ СРЕДСТВ !!!!!")


