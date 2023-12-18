import json
from port import Port
from ship import Ship, ConfigShip
from containers import *
import random


def find_object_by_id(object_list, target_id):
    for obj in object_list:
        if obj.id == target_id:
            return obj
    return None


def load_containers(ship_instance, container_type, max_count):
    count = 0
    while max_count >= count and len(getattr(ship_instance.port, container_type)) > 0:
        container = getattr(ship_instance.port, container_type).pop(0)
        ship_instance.load(container)
        count += 1


def main():
    with open("input_2.json") as input_file:
        data = json.load(input_file)

    ports_list = []
    ships_list = []

    for port_data in data["ports"]:
        port = Port(port_data["port_id"], random.uniform(30.0, 32.0), random.uniform(20.0, 22.0))
        ports_list.append(port)

        for ship_data in port_data["ships"]:
            ship_id = ship_data["ship_id"]
            port_deliver_id = ship_data["ports_deliver"]
            fuel = random.uniform(1800.0, 2200.0)
            port = ports_list[-1]
            configs = ConfigShip(ship_data["totalWeightCapacity"], ship_data["maxNumberOfAllContainers"],
                                 ship_data["maxNumberOfHeavyContainers"],
                                 ship_data["maxNumberOfRefrigeratedContainers"],
                                 ship_data["maxNumberOfLiquidContainers"], ship_data["maxNumberOfBasicContainers"],
                                 ship_data["fuelConsumptionPerKM"])
            ships_list.append(Ship(ship_id, port, port_deliver_id, configs, fuel))

        for container_type in ["basic", "heavy", "refrigerated", "liquid"]:
            container_count = port_data[container_type]
            container_class = globals()[container_type.capitalize() + "Container"]
            getattr(ports_list[-1], container_type).extend(
                [container_class(random.uniform(10.0, 5.0)) for _ in range(container_count)]
            )

    for ship_instance in ships_list:
        load_containers(ship_instance, "heavy", ship_instance.configs.maxNumberOfHeavyContainers)
        load_containers(ship_instance, "basic", ship_instance.configs.maxNumberOfBasicContainers)
        load_containers(ship_instance, "liquid", ship_instance.configs.maxNumberOfLiquidContainers)
        load_containers(ship_instance, "refrigerated", ship_instance.configs.maxNumberOfRefrigeratedContainers)

        port_deliver = find_object_by_id(ports_list, ship_instance.port_deliver)
        if not ship_instance.sail_to(port_deliver):
            ship_instance.refuel(1000)
            ship_instance.sail_to(port_deliver)

        while len(ship_instance.containers) > 0:
            container = ship_instance.containers[0]
            ship_instance.unload(container)
            destination_port = port_deliver
            if isinstance(container, BasicContainer):
                destination_port.basic.append(container)
            # Add other container types to their respective ports

    file_name = "output.json"
    with open(file_name, "w") as json_file:
        data = {"Ports": []}
        for port_instance in ports_list:
            heavy_cont = [str(h.id) for h in port_instance.heavy]
            basic_cont = [str(b.id) for b in port_instance.basic]
            refrigerated_cont = [str(r.id) for r in port_instance.refrigerated]
            liquid_cont = [str(l.id) for l in port_instance.liquid]
            ships_cont = [str(s.id) for s in port_instance.current_ships]

            data["Ports"].append({
                "port": port_instance.id,
                "latitude": port_instance.latitude,
                "longitude": port_instance.longitude,
                "heavy_containers": heavy_cont,
                "basic_containers": basic_cont,
                "refrigerated_containers": refrigerated_cont,
                "liquid_containers": liquid_cont,
                "ships": ships_cont
            })

        json.dump(data, json_file, indent=4)


main()
