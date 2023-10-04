import json
import random


def generate_random_coordinates():
    # генеруємо випадкові значення координат
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude


with open('input.json', 'r') as f:
    data = json.load(f)

# ініціалізація портів з даних input.json
ports_data = {}
for port_data in data:
    port_id = "Port" + str(data.index(port_data))
    ports_data[port_id] = {
        "lat": generate_random_coordinates()[0],
        "lon": generate_random_coordinates()[1],
        "basic_container": [i+1 for i in range(port_data['basic'])],
        "heavy_container": [i+1 for i in range(port_data['heavy'])],
        "refrigerated_container": [i+1 for i in range(port_data['refrigerated'])],
        "liquid_container": [i+1 for i in range(port_data['liquid'])]
    }

    # додавання інформації про кораблі
    for i, ship in enumerate(port_data['ships']):
        ship_id = "ship_" + str(i)
        ports_data[port_id][ship_id] = {
            "fuel_left": ship['fuel_consumption_per_km'] * 1000,
            "basic_container": [i+1 for i in range(ship['max_number_of_all_containers'])],
            "heavy_container": [i+1 for i in range(ship['max_number_of_heavy_containers'])],
            "refrigerated_container": [i+1 for i in range(ship['max_number_of_refrigerated_containers'])],
            "liquid_container": [i+1 for i in range(ship['max_number_of_liquid_containers'])],
        }

# запис даних у output.json
with open('output.json', 'w') as f:
    json.dump(ports_data, f, indent=2)
