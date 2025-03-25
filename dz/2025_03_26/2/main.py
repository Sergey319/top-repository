from models.hot_dog import HotDog, Sauce, Order
from views.hot_dog_view import HotDogView

view = HotDogView()

def main_menu():
    min_hd = HotDog("Маленький", 100)
    normal_hd = HotDog("Средний", 150)
    max_hd = HotDog("Большой", 200)
    print("Добро пожаловать!\n" + hr)
    while True:
        print("Выберите хот-дог:")
        print(f"1. {min_hd}\n2. {normal_hd}\n3. {max_hd}\n0. Выход\n" + hr)
        choice = input("-> ")
        print(hr)
        match choice:
            case "0": break
            case "1": sauce_menu(min_hd)
            case "2": Order(normal_hd); sauce_menu(normal_hd)
            case "3": Order(max_hd); sauce_menu(max_hd)
            case _ : pass

def sauce_menu(hot_dog):
    view.display_hot_dog_info(hot_dog)
    mustard = Sauce("горчица", 20)
    ketchup = Sauce("кетчуп", 30)
    mayonnaise = Sauce("майонез", 40)
    while True:
        print(hr + f"\nВыберите соус:\n1. {mustard}\n2. {ketchup}\n3. {mayonnaise}\n4. Без соуса\n0. Назад\n" + hr)
        choice = input("-> ")
        match choice:
            case "0": break



if __name__ == "__main__":
    hr = "\u2015" * 20
    main_menu()
