class Shoes:
    def __init__(self, m_w, type, color, price, manufacturer, size):
        self.m_w = m_w      # мужская или женская
        self.type = type    # кроссовки, сапоги, сандали, туфли, и т.д.
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def get_info(self):
        return f"Тип: {self.m_w}, Вид: {self.type}, Цвет: {self.color}, Цена: {self.price}, Производитель: {self.manufacturer}, Размер: {self.size}"

    def set_price(self, new_price):
        self.price = new_price

    def set_color(self, new_color):
        self.color = new_color


