class HotDog:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Sauce:
    def __init__(self, name, price):
        self.name =name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Order:
    def __init__(self, hot_dog, sauce=None, topping=None):
        self.hot_dog = hot_dog
        self.sauce = sauce
        self.topping = topping
