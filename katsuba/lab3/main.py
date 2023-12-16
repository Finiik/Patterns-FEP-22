import json
import random
from port import Port
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from ship import Ship, ConfigShip


def generate_input():
    ports = []

    lat1 = 46.48526390187893  # Одеський морський торговельний порт
    lon1 = 30.748038281602632

    lat2 = 37.94498875617777  # Пірейський порт
    lon2 = 23.640635655709

    lat3 = 54.40094300509025  # Гданський морський порт
    lon3 = 18.664403864157627

    lat4 = 44.402778  # Генуезький порт
    lon4 = 8.916667

    lat5 = 51.94926  # порт Філікстоу
    lon5 = 1.312394

    ports.append({
        "id": "08f032a0-074c-4bbb-b859-98bc924ded22",
        "lat": lat1,
        "lon": lon1,
    })

    ports.append({
        "id": "5b0ff1f4-1ffa-405d-8bf9-bc6a4d663e79",
        "lat": lat2,
        "lon": lon2,
    })

    ports.append({
        "id": "f5a1f58d-2af9-4b31-b543-62953913d654",
        "lat": lat3,
        "lon": lon3,
    })

    ports.append({
        "id": "c2e68204-2e11-464f-abcf-6603585761db",
        "lat": lat4,
        "lon": lon4,
    })

    ports.append({
        "id": "67f03c04-3b5c-4c5f-a0c5-d7613c1f046b",
        "lat": lat5,
        "lon": lon5,
    })

    return ports


with open('input.json', 'r') as f:
    data = json.load(f)

ports_data = {}
for port_data in data:
    port_id = str(port_data['port_id'])

    port_coordinates = (0, 0)

    # використання generate_input() для отримання координат для порта
    for port in generate_input():
        if port['id'] == port_id:
            port_coordinates = (port['lat'], port['lon'])
            break

    ports_data[port_id] = Port(latitude=port_coordinates[0], longitude=port_coordinates[1])

    # створення контейнерів
    for i in range(port_data['basic']):  # цикл, який виконується
        container = BasicContainer(random.uniform(0, 3000))  # генерує випадкову вагу від 0 до 3000
        ports_data[port_id].containers.append(container)

    for i in range(port_data['heavy']):
        container = HeavyContainer(random.uniform(3001, 10000))  # генерує випадкову вагу від 3000 до 10000
        ports_data[port_id].containers.append(container)

    for i in range(port_data['refrigerated']):
        container = RefrigeratedContainer(random.uniform(3001, 10000))  # генерує випадкову вагу від 3000 до 10000
        ports_data[port_id].containers.append(container)

    for i in range(port_data['liquid']):
        container = LiquidContainer(random.uniform(3001, 10000))   # генерує випадкову вагу від 3000 до 10000
        ports_data[port_id].containers.append(container)

# створення кораблів
for port_data in data:
    port_id = str(port_data['port_id'])

    for ship_data in port_data['ships']:
        ship_id = str(ship_data['ship_id'])
        ship_config = ConfigShip(
            ship_data['total_weight_capacity'],
            ship_data['max_number_of_all_containers'],
            ship_data['max_number_of_heavy_containers'],
            ship_data['max_number_of_refrigerated_containers'],
            ship_data['max_number_of_liquid_containers'],
            ship_data['fuel_consumption_per_km']
        )
        ship = Ship(ports_data[port_id], ship_config, fuel=ship_data['fuel_consumption_per_km'])
        ports_data[port_id].current_ships.append(ship)

        # вибір випадкового порту для прибуття корабля
        destination_port_id = random.choice(list(ports_data.keys()))
        destination_port = ports_data[destination_port_id]

        arrived_port = ship.sail_to(destination_port)

        ship.refuel(100)  # припустимо, що ви хочете заправити корабель на 100 одиниць палива
        # вибір випадкового контейнера для завантаження та розвантаження
        container = random.choice(ports_data[port_id].containers)
        ship.load(container)  # припустимо, що container вибирається випадково
        ship.unload(container)

# запис даних в output.json
output_data = {port_id: {} for port_id in ports_data.keys()}
for port_id, port in ports_data.items():
    output_data[port_id]["lat"] = port.latitude
    output_data[port_id]["lon"] = port.longitude
    output_data[port_id]["containers"] = [c.weight for c in port.containers]
    output_data[port_id]["ships"] = {}
    for ship in port.current_ships:
        output_data[port_id]["ships"][str(ship.id)] = {
            "fuel_left": ship.fuel,
            "containers": [c.weight for c in ship.containers]
        }

with open('output.json', 'w') as f:
    json.dump(output_data, f, indent=4)
