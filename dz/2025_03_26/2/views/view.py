def hd_view(hd):
    print(f"Название хот-дога: {hd.name}\n"
          f"Цена:              {hd.price} руб.")

def sauce_view(sauce):
    print(f"Название соуса:    {sauce.name}\n"
          f"Цена:              {sauce.price} руб.")

def topping_view(topping):
    print(f"Топпинг:           {topping.name}\n"
          f"Цена:              {topping.price} руб.")

def order_view(order):
    for hd in order.hd:
        hd_view(hd)
    if order.sauce:
        for sauce in order.sauce:
            sauce_view(sauce)
    print(f"ИТОГО:             {order.sum} руб.")
    if order.topping:
        for topping in order.topping:
            topping_view(topping)

    print(f"ИТОГО:             {order.sum} руб.")