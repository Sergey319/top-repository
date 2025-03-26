

def hd_view(hd):
    return f"{hd.name} ({ingredient_view(hd)})" + "_" * (69 - len(hd.name) - len(ingredient_view(hd)) - len(str(price_hd_view(hd)))) + f"{price_hd_view(hd)} руб."

def ingredient_view(hd):
    return ', '.join(i.name for i in hd.ingredients)

def price_hd_view(hd):
    price = 0
    for i in hd.ingredients:
        price += i.price
    return price

def order_view(orders):
    hr = "\u2015" * 50
    price = 0
    print(hr + "\n" + " " * 35 + f"З А К А З :")
    for order in orders:
        print(f"Хот-Дог: {order.name}\nИнгредиенты:")
        price += order.price
        for ingredient in order.ingredients:
            print(f"{ingredient.name}" + "_" * (75 - len(ingredient.name) - len(str(ingredient.price))) + f"{ingredient.price} руб.")
    print(f"\nИ Т О Г О :" + "_" * (64 - len(str(price))) + f"{price} руб.\n" + hr)

def warehouse_view(warehouse, ingredient):
    print(f"{ingredient.name} осталось {warehouse.count(ingredient)}")

def message_error_ingredient(ingredient):
    message = f"   Ингредиент {ingredient} закончился   "
    print("!" * ((80 - len(message)) // 2) + message + "!" * ((80 - len(message)) // 2 + len(message) % 2))

def message_error_warehouse():
    print("СКЛАД СОВЕРШЕННО ПУСТ!!!")
    print("ДО СВИДАНИЯ!!!")
