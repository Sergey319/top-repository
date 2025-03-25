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
            case "1": add_hd_order(order, min_hd); sauce_menu(order)
            case "2": add_hd_order(order, normal_hd); sauce_menu(order)
            case "3": add_hd_order(order, max_hd); sauce_menu(order)
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
            case "1": add_sauce_order(order, mustard); topping_menu(order)
            case "2": add_sauce_order(order, ketchup); topping_menu(order)
            case "3": add_sauce_order(order, mayonnaise); topping_menu(order)
            case "0": break
            case _: pass

def topping_menu(order):
    onion = Topping("Сладкий лук", 20)
    jalapeno = Topping("Халапеьо", 25)
    chile = Topping("Чили", 30)
    cucumber = Topping("Солёный огурец", 35)
    while True:
        print(hr + f"\nВыберите топпинг:\n1. {onion}\n2. {jalapeno}\n3. {chile}\n4. {cucumber}\n0. Назад\n" +hr)
        choice = input("-> ")
        match choice:
            case "1": add_topping_order(order, onion)
            case "2": add_topping_order(order, jalapeno)
            case "3": add_topping_order(order, chile)
            case "4": add_topping_order(order, cucumber)
            case "0": break
            case _: pass

def main():
    main_menu()

if __name__ == "__main__":
    main()