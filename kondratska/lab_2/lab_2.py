# 1. load data from JSON
import json
import random
from uuid import uuid4
from container import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship, ConfigShip

ports_id = [str(uuid4()) for i in range(5)]

# ships
shipsFiller = []
for i in range(10):
    shipDummyArray = {}
    shipDummyArray["ship_id"] = str(uuid4())
    shipDummyArray["port_id"] = random.choice(ports_id)
    shipDummyArray["ports_deliver"] = random.choice([i for i in ports_id if i != shipDummyArray["port_id"]])
    shipDummyArray["fuel"] = 1000
    shipDummyArray["totalWeightCapacity"] = 1000
    shipDummyArray["maxNumberOfAllContainers"] = 20
    shipDummyArray["maxNumberOfHeavyContainers"] = 5
    shipDummyArray["maxNumberOfRefrigeratedContainers"] = 2
    shipDummyArray["maxNumberOfLiquidContainers"] = 5
    shipDummyArray["fuelConsumptionPerKM"] = 20
    shipsFiller.append(shipDummyArray)


# ports
portsFiller = []
for i in range(5):
    portDummyArray = {}
    portDummyArray["port_id"] = ports_id[i]
    portDummyArray["ships"] = [ship for ship in shipsFiller if ship["port_id"] == portDummyArray["port_id"]]
    portDummyArray["containers"] = random.randint(1, 20)
    portDummyArray["basic"] = random.randint(1, 10)
    portDummyArray["heavy"] = random.randint(1, 8)
    portDummyArray["refrigerated"] = random.randint(1, 5)
    portDummyArray["liquid"] = random.randint(1, 5)
    portsFiller.append(portDummyArray)


json_object = json.dumps(portsFiller, indent=2)


# Writing to input.json
with open("input.json", "w") as outfile:
    outfile.write(json_object)


json_object = json.dumps(portsFiller, indent=2)


with open("input.json", "w") as outfile:
    outfile.write(json_object)

# created containers
containers = [BasicContainer(250), BasicContainer(450),
              HeavyContainer(350), RefrigeratedContainer(250.5), LiquidContainer(124)]

# Creating ports
ports_objects = []
for i in range(len(portsFiller)):
    ports_objects.append(Port(
        portsFiller[i]["port_id"],
        round(random.uniform(0, 10 ** 6) / 10 ** 6, 6),
        round(random.uniform(0, 10 ** 6) / 10 ** 6, 6),
        containers
    ))

# Creating ships
ships_objects = []
for i in range(len(shipsFiller)):
    ships_objects.append(Ship(
        shipsFiller[i]["ship_id"],
        ports_objects,
        ConfigShip(
            shipsFiller[i]["totalWeightCapacity"],
            shipsFiller[i]["maxNumberOfAllContainers"],
            shipsFiller[i]["maxNumberOfHeavyContainers"],
            shipsFiller[i]["maxNumberOfRefrigeratedContainers"],
            shipsFiller[i]["maxNumberOfLiquidContainers"],
            shipsFiller[i]["fuelConsumptionPerKM"]
        ),
        containers,
        205 * (i + 1)
    ))

# Loading and unloading containers on ships
for i in range(len(containers)):
    for ship in ships_objects:
        if not isinstance(containers[i], str):
            containerID = containers[i].id
            ship.load(containerID)
            ship.unload(containerID)
            ship.sail_to(ports_objects[i])
