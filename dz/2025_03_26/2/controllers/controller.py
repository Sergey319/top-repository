def add_hd_order(order, hd):
    order.hd.append(hd)
    order.sum += hd.price
    return order

def add_sauce_order(order, sauce):
    order.sauce.append(sauce)
    order.sum += sauce.price
    return order