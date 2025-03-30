class OrderView:
    def __init__(self, orders):
        self.orders = orders

    def display_order(self):
        print("З А К А З :")
        price = 0
        for order in self.orders:
            print(f"Хот-дог: {order.name} - {order.price} руб.")
            price += order.price
        print(f"ИТОГО: {price} руб.")
