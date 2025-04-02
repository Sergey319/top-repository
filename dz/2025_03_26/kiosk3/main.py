from controllers import *

hr = "\u2015" * 50
budget = 10000
reserve = Reserve(budget)
#controller_purchase = PurchaseController()
view_reserve = ReserveView()


bread = Ingredient("булка", 50, 30)
sausage = Ingredient("колбаска", 150, 70)

ketchup = Ingredient("кетчуп", 20, 5)
mustard = Ingredient("горчица", 20, 5)
mayonnaise = Ingredient("майонез", 20, 5)

onion = Ingredient("сладкий лук", 30, 10)
jalapeno = Ingredient("халапеньо", 40, 15)
chili = Ingredient("чили", 40, 15)
cucumber = Ingredient("солёный огурец", 50, 20)


def purchase_of_ingredients():
    while True:
        print(f"Бюджет киоска {reserve.budget} руб.\n" + hr)
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
            case "1": ingredient = bread; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "2": ingredient = sausage; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "3": ingredient = ketchup; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "4": ingredient = mustard; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "5": ingredient = mayonnaise; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "6": ingredient = onion; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "7": ingredient = jalapeno; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "8": ingredient = chili; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "9": ingredient = cucumber; count = count_ingredients(); purchase(reserve, ingredient, count)
            case "10": auto_purchase(); break
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

def auto_purchase():
    ingredients = [bread, sausage, ketchup, mustard, mayonnaise, onion, jalapeno, chili, cucumber]
    while True:
        if reserve.budget > 0:
            for ingredient in ingredients:
                if reserve.budget >= ingredient.purchase_price:
                    reserve.budget -= ingredient.purchase_price
                    reserve.add_ingredient(ingredient)
        else:
            break

def main():
    pass

if __name__ == "__main__":
    purchase_of_ingredients()
    main()
