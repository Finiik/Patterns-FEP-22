
import json
import sys

import item
from port import Port
from ship import *
# from containers import BasicContainer, LiquidContainer, HeavyContainer, RefrigeratedContainer
from containers import *
from item import *
import random


def find_object_by_id(object_list, target_id):
    for obj in object_list:
        if obj.id == target_id:
            return obj  # Found the object
    return None  # Obje


def main():

    # Зчитуємо JSON з файлу
    with open("input_2.json") as input_file:
        data = json.load(input_file)

    ports_list = []
    ships_list = []

    ship_factory = ShipFactory()

    ####        append ports         ####
    print(f"\nappend ports and ships\n")

    i = 0
    for port_data in data["ports"]:
        port_id = port_data["port_id"]
        latitude = random.uniform(30.0, 32.0)
        longitude = random.uniform(20.0, 22.0)
        ports_list.append(Port(port_id, latitude, longitude))
        ships = port_data["ships"]
        print(f"ports {ports_list[i]}")
        # print(f"ships {ships}")

        ####        append ships         ####
        for j in range(0, len(ships)):
            ship_data = ships[j]
            ship_id = ship_data["ship_id"]
            port_deliver_id = ship_data["ports_deliver"]
            fuel = random.uniform(1800.0, 2200.0)
            port = ports_list[i]
            totalWeightCapacity = ship_data["totalWeightCapacity"]
            maxNumberOfAllContainers = ship_data["maxNumberOfAllContainers"]
            maxNumberOfHeavyContainers = ship_data["maxNumberOfHeavyContainers"]
            maxNumberOfRefrigeratedContainers = ship_data["maxNumberOfRefrigeratedContainers"]
            maxNumberOfLiquidContainers = ship_data["maxNumberOfLiquidContainers"]
            maxNumberOfBasicContainers = ship_data["maxNumberOfBasicContainers"]
            fuelConsumptionPerKM = ship_data["fuelConsumptionPerKM"]
            configs = ConfigShip(totalWeightCapacity, maxNumberOfAllContainers, maxNumberOfHeavyContainers,
                                 maxNumberOfRefrigeratedContainers, maxNumberOfLiquidContainers,
                                 maxNumberOfBasicContainers,
                                 fuelConsumptionPerKM)
            ship_type = ship_data["ship_type"]

            ships_list.append(ship_factory.create_ship(ship_type, ship_id, port, port_deliver_id, configs, fuel))

            #ships_list.append(Ship(ship_id, port, port_deliver_id, configs, fuel))
            print(f" - ships {ships_list[j]}")

        ####        append containers         ####
        basic = port_data["basic"]
        heavy = port_data["heavy"]
        refrigerated = port_data["refrigerated"]
        liquid = port_data["liquid"]
        for count in range(0, basic):
            real_basic = BasicContainer(random.uniform(10.0, 5.0))
            item_builder = ItemBuilder().weight(10).count(2).containerID(int(real_basic.id))
            real_basic.items.append(item_builder.build('Small'))
            ports_list[i].basic.append(real_basic)

            #print(f"Item {real_basic.items} created")

        for count in range(0, heavy):
            real_heavy = HeavyContainer(random.uniform(20.0, 10.0))
            item_builder = ItemBuilder().weight(20).count(2).containerID(int(real_heavy.id))
            real_heavy.items.append(item_builder.build('Heavy'))
            ports_list[i].basic.append(real_heavy)

            #print(f"Item {real_heavy.items} created")


        for count in range(0, refrigerated):
            real_refrigerated = RefrigeratedContainer(random.uniform(10.0, 8.0))
            item_builder = ItemBuilder().weight(15).count(3).containerID(int(real_refrigerated.id))
            real_refrigerated.items.append(item_builder.build('Refrigerated'))
            ports_list[i].basic.append(real_refrigerated)

            #print(f"Item {real_refrigerated.items} created")

        for count in range(0, liquid):
            real_liquid = LiquidContainer(random.uniform(10.0, 15.0))
            item_builder = ItemBuilder().weight(11).count(4).containerID(int(real_liquid.id))
            real_liquid.items.append(item_builder.build('Liquid'))
            ports_list[i].basic.append(real_liquid)

            #print(f"Item {real_liquid.items} created")

        i = i + 1




    for ship_instance in ships_list:

        # 4. Ships can load() containers
        print(f"\nShips load containers\n")

        cont_count = 0
        while ((ship_instance.configs.maxNumberOfHeavyContainers >= cont_count) &
               (len(ship_instance.port.heavy) > 0)):
            cont = ship_instance.port.heavy[0]
            ship_instance.load(cont)
            ship_instance.port.heavy.remove(cont)
            cont_count = cont_count + 1
        print(f"load {cont_count} heavy cont, in port exist {len(ship_instance.port.heavy)}")

        cont_count = 0
        while ((ship_instance.configs.maxNumberOfBasicContainers >= cont_count) &
               (len(ship_instance.port.basic) > 0)):
            cont = ship_instance.port.basic[0]
            ship_instance.load(cont)
            ship_instance.port.basic.remove(cont)
            cont_count = cont_count + 1
        print(f"load {cont_count} basic cont, in port exist {len(ship_instance.port.basic)}")

        cont_count = 0
        while ((ship_instance.configs.maxNumberOfLiquidContainers >= cont_count) &
               (len(ship_instance.port.liquid) > 0)):
            cont = ship_instance.port.liquid[0]
            ship_instance.load(cont)
            ship_instance.port.liquid.remove(cont)
            cont_count = cont_count + 1
        print(f"load {cont_count} liquid cont, in port exist {len(ship_instance.port.liquid)}")

        cont_count = 0
        while ((ship_instance.configs.maxNumberOfRefrigeratedContainers >= cont_count) &
               (len(ship_instance.port.refrigerated) > 0)):
            cont = ship_instance.port.refrigerated[0]
            ship_instance.load(cont)
            ship_instance.port.refrigerated.remove(cont)
            cont_count = cont_count + 1
        print(f"load {cont_count} refrigerated cont, in port exist {len(ship_instance.port.refrigerated)}")

        # 5. Ships sail to ports()
        print(f"\nShips sail to ports\n")

        port_deliver = find_object_by_id(ports_list, ship_instance.port_deliver)
        if not ship_instance.sail_to(port_deliver):
            ship_instance.refuel(1000)
            ship_instance.sail_to(port_deliver)

        # 4. Ships unload containers
        print(f"\nShips unload containers\n")

        while len(ship_instance.containers) > 0:
            cont = ship_instance.containers[0]
            ship_instance.unload(cont)
            if isinstance(cont, BasicContainer):
                port_deliver.basic.append(cont)
            if isinstance(cont, HeavyContainer):
                port_deliver.heavy.append(cont)
            if isinstance(cont, LiquidContainer):
                port_deliver.liquid.append(cont)
            if isinstance(cont, RefrigeratedContainer):
                port_deliver.refrigerated.append(cont)

        cont_count = len(port_deliver.basic) + len(port_deliver.heavy) + len(port_deliver.liquid) + len(port_deliver.refrigerated)
        print(f"now {cont_count} containers in port")

    # 8. Output to JSON
    print(f"\nOutput to JSON\n")

    file_name = "output.json"

    # Step 3: Open the file in write mode
    with open(file_name, "w") as json_file:
        # Step 4: Use json.dump() to write data to the file


        data = {
            "Ports": []
        }

        for port_instance in ports_list:
            heavy_cont = []
            for h in port_instance.heavy:
                heavy_cont.append(str(h.id))

            basic_cont = []
            for b in port_instance.basic:
                basic_cont.append(str(b.id))

            refrigerated_cont = []
            for r in port_instance.refrigerated:
                refrigerated_cont.append(str(r.id))

            liquid_cont = []
            for l in port_instance.liquid:
                liquid_cont.append(str(l.id))

            ships_cont = []
            for s in port_instance.current_ships:
                ships_cont.append(str(s.id))


            data["Ports"].append({
                "port": port_instance.id,
                "latitutde": port_instance.latitude,
                "longetude": port_instance.longitude,
                "heavy_containers": heavy_cont,
                "basic_containers": basic_cont,
                "refrigerated_containers": refrigerated_cont,
                "liquid_containers": liquid_cont,
                "ships": ships_cont


            })
        json.dump(data, json_file, indent=4)

main()



# 1. load data from JSON
# 2. Generate Ships based on JSON
# 3. Generate ports based on JSON
# 4. Generate containers
# Loop operations
# 4. Ships can load(), unload() containers
# 5. Ships sail to ports()
# 6. Ships can refuel in the ports;
# 7. Ships must check if they can reach the port
# end loop
# 8. Output to JSON
# 9* (optional). Unit tests all classes.
