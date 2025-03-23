from controllers.shoes_controller import ShoesController
from views.shoes_view import ShoesView
from models.shoes import Shoes

def main():
    controller = ShoesController()
    view = ShoesView()

    shoes1 = Shoes("мужская",
                   "кросовки",
                   "чёрный",
                   3000,
                   "Nike",
                   42)
    shoes2 = Shoes("женская",
                   "туфли",
                   "красный",
                   5000,
                   "Adidas",
                   37)

    controller.add_shoes(shoes1)
    controller.add_shoes(shoes2)

    view.display_shoes_info(controller.get_shoes_info())

    controller.update_shoes_price(0, 3500)
    print("\nПосле обновления цены:\n")

    view.display_shoes_info(controller.get_shoes_info())

if __name__ == "__main__":
    main()