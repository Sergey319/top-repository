from main import *

def view(list):
    for i in list:
        print(f"{i.name} - {i.price}")

warehouse = []
for _ in range(20):
    warehouse.append(bun)
    warehouse.append(sausage)
    warehouse.append(mustard)
    warehouse.append(ketchup)
    warehouse.append(mayonnaise)
    warehouse.append(onion)
    warehouse.append(jalapeno)
    warehouse.append(chile)
    warehouse.append(cucumber)
view(warehouse)
print(warehouse.count(bun))
print(warehouse.count(sausage))
print(warehouse.count(mustard))
print(warehouse.count(ketchup))
print(warehouse.count(mayonnaise))
print(warehouse.count(onion))
print(warehouse.count(jalapeno))
print(warehouse.count(chile))
print(warehouse.count(cucumber))
warehouse.remove(bun)
print(warehouse.count(bun))
print(warehouse.count(sausage))
print(warehouse.count(mustard))
print(warehouse.count(ketchup))
print(warehouse.count(mayonnaise))
print(warehouse.count(onion))
print(warehouse.count(jalapeno))
print(warehouse.count(chile))
print(warehouse.count(cucumber))