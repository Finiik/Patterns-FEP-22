import json
import random
from uuid import uuid4
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship, ConfigShip

containers = [
    BasicContainer(weight=250, id=uuid4()),
    BasicContainer(weight=450, id=uuid4()),
    HeavyContainer(weight=350, id=uuid4()),
    RefrigeratedContainer(weight=250.5, id=uuid4()),
    LiquidContainer(weight=124, id=uuid4())
]


def generate_random_ship_data(ports_id):
    ships_filler_ = []
    for _ in range(10):
        ship_data_ = {
            "ship_id": str(uuid4()),
            "port_id": random.choice(ports_id),
            "fuel": 1000,
            "totalWeightCapacity": 1000,
            "maxNumberOfAllContainers": 20,
            "maxNumberOfHeavyContainers": 5,
            "maxNumberOfRefrigeratedContainers": 2,
            "maxNumberOfLiquidContainers": 5,
            "fuelConsumptionPerKM": 20,
            "ship_type": random.choice(['LightWeightShip', 'MediumShip', 'HeavyShip']),
            "items": [
                {
                    "item_type": random.choice(['Small', 'Heavy', 'Refrigerated', 'Liquid']),
                    "ID": str(uuid4()),
                    "weight": random.uniform(100, 500),
                    "count": random.randint(1, 5),
                    "containerID": str(uuid4()),
                    "specific_attribute": random.uniform(10, 50),
                }
                for _ in range(random.randint(1, 5))
            ]
        }
        ship_data_["ports_deliver"] = random.choice([i for i in ports_id if i != ship_data_["port_id"]])
        ships_filler_.append(ship_data_)
    return ships_filler_


def load_items_onto_ship(ship, containers, item_data):
    container_id_ = item_data["containerID"]
    loaded_container = next((c for c in containers if str(c.id) == container_id_), None)
    if loaded_container:
        print(f"Loading item into Container {loaded_container.id}")
        loaded_container.load_item(
            item_data["item_type"],
            item_data["ID"],
            item_data["weight"],
            item_data["count"],
            item_data["specific_attribute"]
        )
        print(f"Item loaded into Container {loaded_container.id} successfully.")
    else:
        print(f"Container with ID {container_id_} not found.")


if __name__ == "__main__":
    ports_id = [str(uuid4()) for _ in range(5)]

    ships_filler = generate_random_ship_data(ports_id)

    # Writing to input.json
    json_object = json.dumps(ships_filler, indent=2)
    with open("input.json", "w") as outfile:
        outfile.write(json_object)

    # Creating ports
    ports_objects = []
    for i in range(len(ports_id)):
        ports_objects.append(Port(
            str(uuid4()),
            round(random.uniform(0, 10 ** 6) / 10 ** 6, 6),
            round(random.uniform(0, 10 ** 6) / 10 ** 6, 6),
            containers
        ))

    ship_data = []

    ships_objects = []
    for i in range(len(ships_filler)):
        ship_data = ships_filler[i]
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
            205 * (i + 1)
        )
        ships_objects.append(ship)

        # Load items onto the ship
        for item_data in ship_data["items"]:
            load_items_onto_ship(ship, containers, item_data)

    # Unload items from the containers
    for ship_data in ships_filler:
        for item_data in ship_data["items"]:
            container_id = item_data['containerID']
            for container in containers:
                if container.id == container_id:
                    container.unload_item(item_data['ID'])
                    break

    # Perform sail_to operation
    for i in range(len(containers)):
        for ship in ships_objects:
            if not isinstance(containers[i].id, str):
                container_id = containers[i].id
                ship.load(container_id)
                ship.unload(container_id)
                ship.sail_to(ports_objects[i])
