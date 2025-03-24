# core/models.py
class HotDog:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        return f"{self.name} ({', '.join(i.name for i in self.ingredients)}) - ${self.price}"

class Ingredient:
    def __init__(self, name, category, unit, stock=0):
        self.name = name
        self.category = category
        self.unit = unit
        self.stock = stock

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.stock} {self.unit}"

class Order:
    def __init__(self, hot_dogs, payment_method, total_amount, discount=0):
        self.hot_dogs = hot_dogs
        self.payment_method = payment_method
        self.total_amount = total_amount
        self.discount = discount

    def __str__(self):
        return f"Order: {len(self.hot_dogs)} hot dogs, Total: ${self.total_amount}, Payment: {self.payment_method}, Discount: {self.discount}"

class Discount:
    def __init__(self, quantity_threshold, discount_percentage):
        self.quantity_threshold = quantity_threshold
        self.discount_percentage = discount_percentage

# core/services.py
class HotDogService:
    def __init__(self, ingredient_repository):
        self.ingredient_repository = ingredient_repository

    def create_hot_dog(self, name, ingredient_ids):
        ingredients = [self.ingredient_repository.get_by_id(id) for id in ingredient_ids]
        price = sum(i.price for i in ingredients)  # Simplified price calculation
        return HotDog(name, ingredients, price)

    def get_default_hot_dogs(self):
        # Implement fetching from a config or predefined list
        pass

class InventoryService:
    def __init__(self, ingredient_repository):
        self.ingredient_repository = ingredient_repository

    def check_ingredient_availability(self, ingredient, quantity):
        return ingredient.stock >= quantity

    def consume_ingredient(self, ingredient, quantity):
        ingredient.stock -= quantity
        self.ingredient_repository.update_stock(ingredient.id, ingredient.stock)

    def get_low_stock_ingredients(self, threshold=5):
        return [i for i in self.ingredient_repository.get_all() if i.stock <= threshold]

class PricingService:
    def __init__(self, discount_rules):
        self.discount_rules = discount_rules

    def apply_discount(self, order):
        for rule in self.discount_rules:
            if len(order.hot_dogs) >= rule.quantity_threshold:
                order.discount = rule.discount_percentage
                order.total_amount *= (1 - rule.discount_percentage / 100)
                break

class OrderService:
    def __init__(self, hot_dog_service, inventory_service, pricing_service, order_repository):
        self.hot_dog_service = hot_dog_service
        self.inventory_service = inventory_service
        self.pricing_service = pricing_service
        self.order_repository = order_repository

    def create_order(self, hot_dog_names, payment_method):  # hot_dog_names is a list of hot dog names/IDs
        hot_dogs = []
        for hot_dog_name in hot_dog_names:
            # Assuming hot_dog_name is the name of the hot dog, find it and add it
            hot_dog = self.hot_dog_service.get_default_hot_dog(hot_dog_name) # Implement this in HotDogService
            if not hot_dog:
                raise ValueError(f"Hot dog '{hot_dog_name}' not found.")

            for ingredient in hot_dog.ingredients:
                if not self.inventory_service.check_ingredient_availability(ingredient, 1): # Assuming 1 unit of each ingredient per hot dog
                    raise Exception(f"Ingredient {ingredient.name} is out of stock.")
                self.inventory_service.consume_ingredient(ingredient, 1)
            hot_dogs.append(hot_dog)

        total_amount = sum(hd.price for hd in hot_dogs)
        order = Order(hot_dogs, payment_method, total_amount)
        self.pricing_service.apply_discount(order)
        self.order_repository.save(order)
        return order


hotdog = HotDog("Классический", ["булка", "сосиска"], 300)
print(hotdog)