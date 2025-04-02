from models import *

class ReserveView:
    def display_reserve(self, reserve):
        for ingredient in reserve.get_reserve():
            print(f"{ingredient.name}")
        print(reserve.budget)