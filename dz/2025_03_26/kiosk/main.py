from models.model import *
from controller import *
from views.view import *

# хот-дог
bun = Ingredient("булка", 50)
sausage = Ingredient("колбаска", 150)

# соус
mustard = Ingredient("горчица", 10)
ketchup = Ingredient("кетчуп", 15)
mayonnaise = Ingredient("майонез", 20)

# топпинг
onion = Ingredient("сладкий лук", 30)
jalapeno = Ingredient("халапеньо", 25)
chile = Ingredient("чили", 30)
cucumber = Ingredient("солёный огурец", 35)

# рецепт хот-дога
standard_hd = HotDog("Стандарт", [bun, sausage, ketchup])
spicy_hd = HotDog("Острый", [bun, sausage, mustard, chile])
special_hd = HotDog("Особый", [bun, sausage, mayonnaise, jalapeno, onion])

warehouse = []

hr = "\u2015" * 50

def main():
    print("_" * 80)
    print(hr + "\n" + " " * 20 + "Д О Б Р О   П О Ж А Л О В А Т Ь ! ! !\n" + hr)
    orders = []
    main_menu(orders)

def main_menu(orders):
    while True:
        print(f"Выберите Хот-Дог или создайте свой рецепт:")
        print(f"1. {hd_view(standard_hd)}\n"
              f"2. {hd_view(spicy_hd)}\n"
              f"3. {hd_view(special_hd)}\n"
              f"4. Создать свой рецепт\n"
              f"0. Выход\n" + hr)
        choice = input("-> ")
        match choice:
            case "1": add_order(orders, standard_hd)
            case "2": add_order(orders, spicy_hd)
            case "3": add_order(orders, special_hd)
            case "4": pass
            case "0": break
            case _: pass


if __name__ == "__main__":
    main()