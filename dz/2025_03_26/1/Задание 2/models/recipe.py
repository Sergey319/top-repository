class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def get_info(self):
        ingredients_list = ', '.join(self.ingredients)
        return (f"Название: {self.name}\n"
                f"Автор: {self.author}\n"
                f"Тип: {self.recipe_type}\n"
                f"Описание: {self.description}\n"
                f"Ссылка на видео: {self.video_link}\n"
                f"Ингредиенты: {ingredients_list}\n"
                f"Кухня: {self.cuisine}\n")

    def update_video_link(self, new_link):
        self.video_link = new_link

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)