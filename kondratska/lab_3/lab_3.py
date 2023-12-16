import json
from uuid import uuid4
from random import choice, randint, uniform
from item import Item
from container import Container
from ship import ShipBuilder, ConfigShip
from port import Port


def load_data_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data


def save_data_to_json(data, file_path):
    with open(file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)


def generate_unique_id():
    return str(uuid4())


def process_containers_data(data_entry):
    for cont_entry in data_entry.get('Containers_data', []):
        cont_entry["id"] = generate_unique_id()


def process_ports_data(data_entry):
    for port_entry in data_entry.get("Ports_data", []):
        port_entry["id"] = generate_unique_id()


def process_ships_data(data_entry):
    for ship_entry in data_entry.get("Ships_data", []):
        ship_entry["id"] = generate_unique_id()


class ItemEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Item):
            return obj.__dict__
        return super().default(obj)


def generate_uuid():
    return str(uuid4())


def create_ports_data():
    ports_id = [generate_uuid() for _ in range(5)]

    ports = []
    for i in range(5):
        port = dict()
        port["id"] = ports_id[i]
        port["latitude"] = uniform(-90, 90)
        port["longitude"] = uniform(-180, 180)
        port["basic_cont"] = randint(1, 10)
        port["heavy_cont"] = randint(1, 8)
        port["refrigerated_cont"] = randint(1, 5)
        port["liquid_cont"] = randint(1, 5)
        ports.append(port)

    return ports


def create_ships_data(ports):
    ships = []
    for i in range(10):
        ship = dict()
        ship["ship_id"] = generate_uuid()
        ship["port_id"] = choice([port["id"] for port in ports])
        ship["ports_deliver"] = choice([port["id"] for port in ports if port["id"] != ship["port_id"]])
        ship["fuel"] = 1000
        ship["total_weight_capacity"] = 1000
        ship["max_number_of_all_containers"] = 20
        ship["max_number_of_basic_containers"] = 5
        ship["max_number_of_heavy_containers"] = 5
        ship["max_number_of_refrigerated_containers"] = 2
        ship["max_number_of_liquid_containers"] = 5
        ship["fuel_consumption_per_km"] = 20
        ships.append(ship)

    return ships


def create_containers_data(item_data):
    containers = []
    for i in range(2):
        container = dict()
        container["id"] = generate_uuid()
        container["weight"] = uniform(100, 500)
        container["type"] = choice(["basic", "heavy", "refrigerated", "liquid"])
        container["items"] = []  # Initialize an empty list for items
        container["remaining_capacity"] = container["weight"]
        containers.append(container)

    assign_items_to_containers(item_data, containers)

    return containers


def create_items():
    items = []
    for i in range(36):
        item_type = choice(["Small", "Heavy", "Refrigerated", "Liquid"])
        weight = uniform(20, 150)
        count = randint(1, 6)
        items.append({
            "item_type": item_type,
            "ID": generate_uuid(),
            "weight": weight,
            "count": count,
            "specific_attribute": uniform(10, 50)
        })

    return items


def assign_items_to_containers(items_data, containers_data):

    for item_data in items_data:
        print(f"Processing item_data: {item_data}")
        item_type = item_data["item_type"]
        ID = item_data["ID"]
        weight = item_data["weight"]
        count = item_data["count"]
        specific_attribute = item_data["specific_attribute"]

        item = Item.check_type(ID, weight, count, item_type, specific_attribute)
        if item:
            container_assigned = False
            for cont in containers_data:
                if cont["remaining_capacity"] >= item.get_total_weight():
                    cont["items"].append(item)
                    cont["remaining_capacity"] -= item.get_total_weight()
                    container_assigned = True
                    break
            if not container_assigned:
                print(f"Failed to assign item with ID {item.ID} to any container.")
                print(f"Item Weight: {item.weight}, Item Type: {item.item_type}")


def generate_ports(data):
    ports = []
    for data_entry_list in data:
        for data_entry in data_entry_list:
            ports_data = data_entry.get("Ports_data", [])
            for port_entry in ports_data:
                port = Port(
                    port_id=port_entry.get("id"),
                    latitude=port_entry.get("latitude"),
                    longitude=port_entry.get("longitude"),
                    basic_containers=port_entry.get("basic_cont"),
                    heavy_containers=port_entry.get("heavy_cont"),
                    refrigerated_containers=port_entry.get("refrigerated_cont"),
                    liquid_containers=port_entry.get("liquid_cont"),
                )
                ports.append(port)
    return ports


def create_ships(data_entries, ports):
    ships = []
    port_count = len(ports)

    for data_entry in data_entries:
        for i, ship in enumerate(data_entry.get("Ships_data", [])):
            port = ports[i % port_count]
            ship_data = ConfigShip(
                ship["total_weight_capacity"],
                ship["maxNumberOfAllContainers"],
                ship["maxNumberOfBasicContainers"],
                ship["maxNumberOfHeavyContainers"],
                ship["maxNumberOfRefrigeratedContainers"],
                ship["maxNumberOfLiquidContainers"],
                ship["fuelConsumptionPerKM"]
            )

            # Use ShipBuilder to create ships
            ship_builder = ShipBuilder(ship["type"], port, ship["id"], ship["fuel"])
            ship_builder.set_configs(ship_data.total_weight_capacity,
                                     ship_data.max_number_of_all_containers,
                                     ship_data.max_number_of_basic_containers,
                                     ship_data.max_number_of_heavy_containers,
                                     ship_data.max_number_of_refrigerated_containers,
                                     ship_data.max_number_of_liquid_containers,
                                     ship_data.fuel_consumption_per_km)

            # Add containers to the ship
            for container_id in ship["containers"]:
                container = next((cont for data_entry in data_entries
                                  for cont in data_entry.get("Containers_data", []) if cont["id"] == container_id),
                                 None)
                if container:
                    container_type = None
                    if "type" in container:
                        container_type = container["type"]
                    ship_builder.add_container(Container.create_container(container["id"],
                                                                          container['weight'], container_type))
            new_ship = ship_builder.build()
            ships.append(new_ship)
            port.ship_current.append(new_ship)

    return ships


def generate_items():
    return [Item.check_type(str(uuid4()), randint(1, 30) * 20, randint(1, 6), choice(["R", "L", None, None])) for _
            in range(36)]


def generate_output_data(ports):
    output_data = []
    for port in ports:
        port_data_info = {
            "id": port.id,
            "latitude": port.latitude,
            "longitude": port.longitude,
            "basic_cont": port.basic_cont,
            "heavy_cont": port.heavy_cont,
            "refrigerated_cont": port.refrigerated_cont,
            "liquid_cont": port.liquid_cont
        }
        output_data.append(port_data_info)
    return output_data


def generate_input_data():
    ports_data = create_ports_data()
    ships_data = create_ships_data(ports_data)
    items_data = create_items()
    containers_data = create_containers_data(items_data)  # Pass items_data

    json_structure = {
        "Ports_data": ports_data,
        "Ships_data": ships_data,
        "Containers_data": containers_data
    }

    json_object = json.dumps([json_structure], indent=2, cls=ItemEncoder)

    # Writing to input_data.json
    with open("input_data.json", "w") as outfile:
        outfile.write(json_object)


def main():
    # Uncomment the line below if you want to generate the input_data.json file
    # generate_input_data()

    id_data = load_data_from_json('input_data.json')

    print("Loaded data:", id_data)

    # Check if the loaded data has the expected structure
    if isinstance(id_data, dict) and any(key in id_data for key in ['Ports_data', 'Ships_data', 'Containers_data']):
        # Process each type of data
        for cont_entry in id_data.get('Containers_data', []):
            container_id = cont_entry.get('id')
            # Process container data here
            process_containers_data(cont_entry)

        for port_entry in id_data.get('Ports_data', []):
            port_id = port_entry.get('id')
            process_ports_data(port_entry)

        for ship_entry in id_data.get('Ships_data', []):
            ship_id = ship_entry.get('ship_id')
            # Process ship data here
            process_ships_data(ship_entry)

        # Save the updated data
        save_data_to_json(id_data, 'input_data.json')

        project_data = [entry for key, entry
                        in id_data.items() if key in ['Ports_data', 'Ships_data', 'Containers_data']]

        print("Project data:", project_data)

        if project_data:
            # Rest of the code remains the same
            ports = generate_ports(project_data)

            # Updated part for creating containers
            containers = [
                Container.create_container(container("id"), container.get('weight', 0), container.get('type'))
                for data_entry in project_data
                for container in data_entry
            ]

            items = generate_items()
            assign_items_to_containers(items, containers)

            ships = create_ships(project_data, ports)

            output_data = {
                "Ports_data": generate_output_data(ports),
                "Ships_data": [
                    {
                        "ship_id": ship.id,
                        "port_id": ship.port.id,
                        "fuel": ship.fuel,
                        "total_weight_capacity": ship.total_weight_capacity,
                        "max_number_of_all_containers": ship.max_number_of_all_containers,
                        "max_number_of_basic_containers": ship.max_number_of_basic_containers,
                        "max_number_of_heavy_containers": ship.max_number_of_heavy_containers,
                        "max_number_of_refrigerated_containers": ship.max_number_of_refrigerated_containers,
                        "max_number_of_liquid_containers": ship.max_number_of_liquid_containers,
                        "fuel_consumption_per_km": ship.fuel_consumption_per_km,
                        "ship_type": ship.type,
                        "containers": [cont.id for cont in ship.containers],
                        "items": [
                            {
                                "item_type": item.item_type,
                                "ID": item.ID,
                                "weight": item.weight,
                                "count": item.count,
                                "containerID": item.containerID,
                                "specific_attribute": item.specific_attribute
                            }
                            for cont in ship.containers
                            for item in cont.items
                        ],
                        "ports_deliver": ship.port_deliver.id if ship.port_deliver else None
                    }
                    for ship in ships
                ],
                "Containers_data": [
                    {
                        "id": cont.id,
                        "weight": cont.weight,
                        "type": cont.type
                    }
                    for cont in containers
                ]
            }

            save_data_to_json([output_data], 'output_data.json')
        else:
            print("No data entries found in the input data.")
    else:
        print("Unexpected data structure in the input data. Please check the input_data.json file.")


if __name__ == "__main__":
    main()
