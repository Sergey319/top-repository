from models.recipe import Recipe
from controllers.recipe_controller import RecipeController
from views.recipe_view import RecipeView

def main():

    controller = RecipeController()
    view = RecipeView()

    recipe1 = Recipe("Паста карбоната",
                     "Итальянский шеф",
                     "Основное блюдо",
                     "Классическая паста карбоната с беконом и сыром",
                     "https://example.com/video1",
                     ["паста", "яйцо", "бекон", "сыр пармезан", "перец"],
                     "Итальянская"
                     )

    recipe2 = Recipe("Борщ",
                     "Русский шеф",
                     "Первое блюдо",
                     "Традиционный Русский борщ с мясом и свёклой",
                     "https://example.com/video2",
                     ["свёкла", "капуста", "картофель", "мясо", "чеснок"],
                     "Русская"
                     )

    controller.add_recipe(recipe1)
    controller.add_recipe(recipe2)

    view.display_recipe_info(controller.get_recipe_info())

    controller.update_recipe_video(0, "https://example.com/new_video1")
    print("\nПосле обновления ссылки на видео:\n")

    view.display_recipe_info(controller.get_recipe_info())

if __name__ == "__main__":
    main()