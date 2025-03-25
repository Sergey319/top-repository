from models.model import *
from controllers.controller import *
from views.view import *
hr = "\u2015" * 17

def main_menu():
    min_hd = HotDog("Маленький", 100)
    normal_hd = HotDog("Средний", 150)
    max_hd = HotDog("Большой", 200)
    print(hr + "\nДОБРО ПОЖАЛОВАТЬ!")
    order = Order([], [], [], 0)
    while True:
        print(hr + f"\nВыберите хот-дог:\n1. {min_hd}\n2. {normal_hd}\n3. {max_hd}\n0. Выход\n" + hr)
        choice = input("-> ")
        match choice:
            case "1": add_hd_order(order, min_hd); order_view(order); sauce_menu(order)
            case "2": add_hd_order(order, normal_hd); order_view(order); sauce_menu(order)
            case "3": add_hd_order(order, max_hd); order_view(order); sauce_menu(order)
            case "0": break
            case _: pass

def sauce_menu(order):
    mustard = Sauce("Горчица", 10)
    ketchup = Sauce("Кетчуп", 20)
    mayonnaise = Sauce("Майонез", 30)
    while True:
        print(hr + f"\nВыберите соус:\n1. {mustard}\n2. {ketchup}\n3. {mayonnaise}\n0. Назад\n" + hr)
        choice = input("-> ")
        match choice:
            case "1": add_sauce_order(order, mustard); order_view(order)
            case "2": add_sauce_order(order, ketchup); order_view(order)
            case "3": add_sauce_order(order, mayonnaise); order_view(order)
            case "0": break
            case _: pass

def main():
    main_menu()

if __name__ == "__main__":
    main()