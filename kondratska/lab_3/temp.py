import json
from uuid import uuid4
import random
from item import Item


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
        port["latitude"] = random.uniform(-90, 90)
        port["longitude"] = random.uniform(-180, 180)
        port["basic_cont"] = random.randint(1, 10)
        port["heavy_cont"] = random.randint(1, 8)
        port["refrigerated_cont"] = random.randint(1, 5)
        port["liquid_cont"] = random.randint(1, 5)
        ports.append(port)

    return ports


def create_ships_data(ports):
    ships = []
    for i in range(10):
        ship = dict()
        ship["ship_id"] = generate_uuid()
        ship["port_id"] = random.choice([port["id"] for port in ports])
        ship["ports_deliver"] = random.choice([port["id"] for port in ports if port["id"] != ship["port_id"]])
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

def create_containers_data(item_data):
    containers = []
    for i in range(2):
        container = dict()
        container["id"] = generate_uuid()
        container["weight"] = random.uniform(100, 500)
        container["type"] = random.choice(["basic", "heavy", "refrigerated", "liquid"])
        container["items"] = []  # Initialize an empty list for items
        container["remaining_capacity"] = container["weight"]
        containers.append(container)

    assign_items_to_containers(item_data, containers)

    return containers



def create_items():
    items = []
    for i in range(36):
        item_type = random.choice(["Small", "Heavy", "Refrigerated", "Liquid"])
        weight = random.uniform(20, 150)
        count = random.randint(1, 6)
        items.append({
            "item_type": item_type,
            "ID": generate_uuid(),
            "weight": weight,
            "count": count,
            "specific_attribute": random.uniform(10, 50)
        })

    return items



if __name__ == "__main__":
    ports_data = create_ports_data()
    ships_data = create_ships_data(ports_data)
    items_data = create_items()
    containers_data = create_containers_data(items_data)  # Pass items_data

    json_structure = {
        "Ports_data": ports_data,
        "Ships_data": ships_data,
        "Containers_data": containers_data
    }

    json_object = json.dumps(json_structure, indent=2, cls=ItemEncoder)

    # Writing to input_data.json
    with open("input_data.json", "w") as outfile:
        outfile.write(json_object)