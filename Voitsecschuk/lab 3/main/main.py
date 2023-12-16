import json
from uuid import uuid4
from port import Port
from ship import Ship, ConfigShip
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer


def load_data_from_json(file_path):
    with open(file_path, "r") as infile:
        data = json.load(infile)
    return data


def load_containers_from_data(data):
    if "container" not in data:
        return []

    containers = []
    print("ALL informathion about the container in port:\n")
    for container_data in data["container"]:
        container_type = globals()[container_data["type"]]
        containers.append(container_type(weight=container_data["weight"], id=str(container_data["ID"])))
    return containers

print('\n')
def load_items_onto_ship(ship, containers, item_data, ports_objects):
    container_id_ = item_data["containerID"]
    loaded_container = next((c for c in containers if str(c.id) == container_id_), None)
    if loaded_container:
        print('\n')
        print(f"Loading item into container {loaded_container.id}")
        loaded_container.load_item(
            item_data["item_type"],
            item_data["ID"],
            item_data["weight"],
            item_data["count"],
            item_data["containerID"],
            item_data["specific_attribute"]
        )
        print(f"Item successfully loaded into container {loaded_container.id}.")
        ship.load(loaded_container.id)
        ship.sail_to(ports_objects[i])
        ship.unload(loaded_container.id)
        # Отримання ID порту для контейнера
        port_id = next((port.id for port in ports_objects if loaded_container in port.current_containers), None)
    else:
        print(f"Container with ID {container_id_} not found.")
        print("Available containers:")
        for c in containers:
            print(f"Container {c.id}")



if __name__ == "__main__":
    ships_filler = load_data_from_json("input.json")

    print('\n')

    # Creating ports
    ports_objects = []
    for port_data in ships_filler:
        port_id = str(uuid4())
        port_latitude = port_data["latitude"]
        port_longitude = port_data["longitude"]
        port_containers = load_containers_from_data(port_data)
        print(f"Port {port_id}: {port_containers}")  # Друк кількості контейнерів у порту
        ports_objects.append(Port(port_id, port_latitude, port_longitude, port_containers))

    ships_objects = []
    for i, ship_data in enumerate(ships_filler):
        containers = load_containers_from_data(ship_data)
        ship = Ship(
            ship_data["ship_id"],
            ports_objects,
            ConfigShip(
                ship_data["totalWeightCapacity"],
                ship_data["maxNumberOfAllContainers"],
                ship_data["maxNumberOfHeavyContainers"],
                ship_data["maxNumberOfRefrigeratedContainers"],
                ship_data["maxNumberOfLiquidContainers"],
                ship_data["fuelConsumptionPerKM"]
            ),
            containers,
            ship_data["fuel"]
        )
        ships_objects.append(ship)

        # Loading items onto the ship
        for item_data in ship_data["items"]:
            load_items_onto_ship(ship, containers, item_data, ports_objects)
