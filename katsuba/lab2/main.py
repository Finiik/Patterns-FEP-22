import json
import random
from port import Port
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from ship import Ship, ConfigShip


def generate_random_coordinates():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude


with open('input.json', 'r') as f:
    data = json.load(f)

ports_data = {}
for port_data in data:
    port_id = str(port_data['port_id'])
    port_coordinates = generate_random_coordinates()
    ports_data[port_id] = Port(latitude=port_coordinates[0], longitude=port_coordinates[1])

    # Create containers
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

# Create ships
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

        # Вибір випадкового порту для прибуття корабля
        destination_port_id = random.choice(list(ports_data.keys()))
        destination_port = ports_data[destination_port_id]

        arrived_port = ship.sail_to(destination_port)

        ship.refuel(100)  # Припустимо, що ви хочете заправити корабель на 100 одиниць палива
        # Вибір випадкового контейнера для завантаження та розвантаження
        container = random.choice(ports_data[port_id].containers)
        ship.load(container)  # Припустимо, що container вибирається випадково
        ship.unload(container)

# Write data to output.json
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
