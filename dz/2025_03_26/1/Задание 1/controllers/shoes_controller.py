class ShoesController:
    def __init__(self):
        self.shoes_list = []

    def add_shoes(self, shoes):
        self.shoes_list.append(shoes)

    def get_shoes_info(self):
        return [shoes.get_info() for shoes in self.shoes_list]

    def update_shoes_price(self, index, new_price):
        if 0 <= index < len(self.shoes_list):
            self.shoes_list[index].set_price(new_price)
        else:
            print("Обувь с таким индексом не найдена.")