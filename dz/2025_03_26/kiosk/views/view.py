def hd_view(hd):
    return f"{hd.name} ({ingredient_view(hd)}) - {price_hd_view(hd)} руб."

def ingredient_view(hd):
    return ', '.join(i.name for i in hd.ingredients)

def price_hd_view(hd):
    price = 0
    for i in hd.ingredients:
        price += i.price
    return price

def order_view(order):
    print(f"Хот-дог: {order.name}\n"
            f"Состав: {'\n        '.join(i.name for i in order.ingredients)} - {'\n'.join(str(i.price) for i in order.ingredients)}")