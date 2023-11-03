import json
from uuid import uuid4
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship, ConfigShip

containers = [
    BasicContainer(weight=250, id="3"),
    BasicContainer(weight=450, id="5"),
    HeavyContainer(weight=350, id="7"),
    RefrigeratedContainer(weight=250.5, id="10"),
    LiquidContainer(weight=124, id="14")
]


# решта коду

def load_data_from_json(file_path):
    with open(file_path, "r") as infile:
        data = json.load(infile)
    return data


def load_items_onto_ship(ship, containers, item_data):
    container_id_ = item_data["containerID"]
    loaded_container = next((c for c in containers if str(c.id) == container_id_), None)
    if loaded_container:
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
    else:
        print(f"Container with ID {container_id_} not found.")

if __name__ == "__main__":
    ships_filler = load_data_from_json("input.json")

    # Creating ports
    ports_objects = []
    for port_data in ships_filler:
        port_id = str(uuid4())
        port_latitude = port_data["latitude"]
        port_longitude = port_data["longitude"]
        port_containers = containers
        ports_objects.append(Port(port_id, port_latitude, port_longitude, port_containers))

    ships_objects = []
    for i, ship_data in enumerate(ships_filler):
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

        # Load specific containers onto ships
        for j in range(i, len(containers), len(ships_filler)):
            ship.load(containers[j].id)
            ship.unload(containers[j].id)
            ship.sail_to(ports_objects[i])

        # Loading items onto the ship
        for item_data in ship_data["items"]:
            load_items_onto_ship(ship, containers, item_data)
