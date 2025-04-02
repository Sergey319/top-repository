from controllers import *

from views import *

hr = "\u2015" * 50
budget = 1000
reserve = Reserve(budget)

#view_reserve = ReserveView()


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
hd = HotDog("Собственный", [bread, sausage])

ingredients = [bread, sausage, ketchup, mustard, mayonnaise, onion, jalapeno, chili, cucumber]


def purchase_of_ingredients():
    while True:
        print(hr + f"\nБюджет киоска {reserve.budget} руб.\n" + hr)
        print(f"Выберите ингредиент для закупки:\n"
              f"1. {bread.name} - {bread.purchase_price} руб.\n"
              f"2. {sausage.name} - {sausage.purchase_price} руб.\n"
              f"3. {ketchup.name} - {ketchup.purchase_price} руб.\n"
              f"4. {mustard.name} - {mustard.purchase_price} руб.\n"
              f"5. {mayonnaise.name} - {mayonnaise.purchase_price} руб.\n"
              f"6. {onion.name} - {onion.purchase_price} руб.\n"
              f"7. {jalapeno.name} - {jalapeno.purchase_price} руб.\n"
              f"8. {chili.name} - {chili.purchase_price} руб.\n"
              f"9. {cucumber.name} - {cucumber.purchase_price} руб.\n"
              f"10. Автоматическая закупка\n"
              f"11. Продолжить")
        choice = input("-> ")
        match choice:
            case "1": ReserveControllers(reserve, bread, count_ingredients()).purchase()
            case "2": ReserveControllers(reserve, sausage, count_ingredients()).purchase()
            case "3": ReserveControllers(reserve, ketchup, count_ingredients()).purchase()
            case "4": ReserveControllers(reserve, mustard, count_ingredients()).purchase()
            case "5": ReserveControllers(reserve, mayonnaise, count_ingredients()).purchase()
            case "6": ReserveControllers(reserve, onion, count_ingredients()).purchase()
            case "7": ReserveControllers(reserve, jalapeno, count_ingredients()).purchase()
            case "8": ReserveControllers(reserve, chili, count_ingredients()).purchase()
            case "9": ReserveControllers(reserve, cucumber, count_ingredients()).purchase()
            case "10": ReserveControllers(reserve, ingredients=ingredients).auto_purchase()
            case "11": break
            case _: pass

def count_ingredients():
    count = ""
    while type(count) != int:
        try:
            count = int(input("Укажите количество -> "))
        except ValueError:
            pass
        else:
            return count



def display_reserve():
    print("Список закупленных ингредиентов:")
    for ingredient in ingredients:
        print(f"{ingredient.name} - {reserve.reserve.count(ingredient)}")

def main():
    purchase_of_ingredients()
    print(hr)
    display_reserve()

if __name__ == "__main__":
    main()
