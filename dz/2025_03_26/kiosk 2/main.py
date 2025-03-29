from model import *
from controller import *


def main():
    bread = Ingredient("булка", 50, 30)
    sausage = Ingredient("колбаска", 150, 70)

    ketchup = Ingredient("кетчуп", 20, 5)
    mustard = Ingredient("горчица", 20, 5)
    mayonnaise = Ingredient("майонез", 20, 5)

    onion = Ingredient("сладкий лук", 30, 10)
    jalapeno = Ingredient("халапеньо", 40, 15)
    chili = Ingredient("чили", 40, 15)
    cucumber = Ingredient("солёный огурец", 50, 20)

    standard_hd = HotDog("Стандарт", [bread, sausage, ketchup])
    spicy_hd = HotDog("Острый", [bread, sausage, mustard, chili])
    special_hd = HotDog("Особый", [bread, sausage, mayonnaise, cucumber])

    orders = Orders()

    hr = "\u2015" * 50

    print(hr)
    print(" " * 21 + "Д О Б Р О   П О Ж А Л О В А Т Ь ! ! !")
    while True:
        print(hr)
        print("Выберите хот-дог или создайте свой рецепт:")
        print(f"1. {standard_hd}\n"
              f"2. {spicy_hd}\n"
              f"3. {special_hd}\n"
              f"4. Создать свой\n"
              f"5. Перейти к оплате\n"
              f"0. Выход\n" + hr)
        choice = input("-> ")
        match choice:
            case "1": update_order(orders, standard_hd)
            case "2": pass
            case "3": pass
            case "4": pass
            case "5": pass
            case "0": break



if __name__ == "__main__":
    main()