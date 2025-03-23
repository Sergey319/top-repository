class RecipeController:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self, recipe):
        self.recipe_list.append(recipe)

    def get_recipe_info(self):
        return [recipe.get_info() for recipe in self.recipe_list]

    def update_recipe_video(self, index, new_link):
        if 0 <= index < len(self.recipe_list):
            self.recipe_list[index].update_video_link(new_link)
        else:
            print("Рецепт с таким индексом не найден.")