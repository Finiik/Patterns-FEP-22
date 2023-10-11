import json  # імпортуємо бібліотеку для роботи з JSON
from uuid import uuid4  # імпортуємо функцію для генерації UUID
import random  # мпортуємо бібліотеку для генерації випадкових значень

# створюємо список унікальних ідентифікаторів портів (5 штук)
ports_id = [str(uuid4()) for i in range(5)]

# ініціалізуємо список для збереження інформації про кораблі
ships = []
for i in range(10):
    ship = {}  # створюємо пустий словник для інформації про корабель
    ship["ship_id"] = str(uuid4())  # генеруємо унікальний ідентифікатор корабля
    ship["port_id"] = random.choice(ports_id)  # вибираємо випадковий порт для корабля зі списку портів
    ship["ports_deliver"] = random.choice([i for i in ports_id if i != ship["ship_id"]])
    # вибираємо випадковий порт для доставки, існуючий окрім поточного порту корабля
    ship["total_weight_capacity"] = 1000  # задаємо загальну вагову місткість корабля
    ship["max_number_of_all_containers"] = 20  # задаємо макс к-сть усіх контейнерів, яку може вмістити корабель
    ship["max_number_of_heavy_containers"] = 5  # задаємо макс к-сть важких контейнерів, яку може вмістити корабель
    ship["max_number_of_refrigerated_containers"] = 2  # Задаємо макс к-сть refrigerated конт,яку може вмістити корабель
    ship["max_number_of_liquid_containers"] = 5  # задаємо макс к-сть рідких контейнерів, яку може вмістити корабель
    ship["fuel_consumption_per_km"] = 20  # задаємо витрати пального на 1 кілометр плавання корабля.
    ships.append(ship)  # додаємо інформацію про корабель до списку кораблів

# ініціалізуємо список для збереження інформації про порти
ports = []
for i in range(5):
    port = {}  # створюємо пустий словник для інформації про порт
    port["port_id"] = ports_id[i]  # задаємо ідентифікатор порту
    port["ships"] = [ship for ship in ships if ship["port_id"] == port["port_id"]]
    # вибираємо кораблі, які призначені для цього порту
    port["basic"] = random.randint(1, 10)  # генеруємо випадкову к-сть базових контейнерів у порту
    port["heavy"] = random.randint(1, 8)  # генеруємо випадкову к-сть важких контейнерів у порту
    port["refrigerated"] = random.randint(1, 5)  # генеруємо випадкову к-сть холодильних контейнерів у порту
    port["liquid"] = random.randint(1, 5)  # генеруємо випадкову к-сть рідких контейнерів у порту
    ports.append(port)  # додаємо інформацію про порт до списку портів

# перетворюємо список портів у JSON обєкт з відступами
json_object = json.dumps(ports, indent=2)

# записуємо JSON обєкт у файл input.json
with open('input.json', 'w') as outfile:
    outfile.write(json_object)
