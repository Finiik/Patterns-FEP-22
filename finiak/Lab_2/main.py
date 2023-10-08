import json
import random
from uuid import uuid4
portsID = [str(uuid4()) for i in range(5)]

Ships = []
for i in range(10):
    fillerShipList = {}
    fillerShipList["ship_id"] = str(uuid4())
    fillerShipList["port_id"] = random.choice(portsID)
    fillerShipList["ports_deliver"] = random.choice([i for i in portsID if i != fillerShipList["ship_id"]])
    fillerShipList["totalWeightCapacity"] = 1000
    fillerShipList["maxNumberOfAllContainers"] = 20
    fillerShipList["maxNumberOfHeavyContainers"] = 5
    fillerShipList["maxNumberOfRefrigeratedContainers"] = 2
    fillerShipList["maxNumberOfLiquidContainers"] = 5
    fillerShipList["fuelConsumptionPerKM"] = 20
    Ships.append(fillerShipList)
    
Ports = []
for i in range(5):
    fillerPortList = {}
    fillerPortList["port_id"] = portsID[i]
    fillerPortList["ships"] = [ship for ship in Ships if ship["port_id"] == fillerPortList["port_id"]]
    fillerPortList["basic"] = random.randint(1, 10)
    fillerPortList["heavy"] = random.randint(1, 8)
    fillerPortList["refrigerated"] = random.randint(1, 5)
    fillerPortList["liquid"] = random.randint(1, 5)
    Ports.append(fillerPortList)
    
json_obj = json(Ports, indent = 2)

from containers import *
from port import IPort, Port
from ship import ConfigShip, IShip, Ship

with open("C:\Users\Олег\Desktop\Потрібне шось\Patterns\Lab_2\input.json", "w") as outfile:
    outfile.write(json_obj)
    
containers = [BasicContainer(200), BasicContainer(400), HeavyContainer(300), RefrigeratedContainer(300), LiquidContainer(136)]

ports = [Port(
    Ports[i]["port_id"],
    round(random.uniform(0, 10**6)/10**6, 6),
    round(random.uniform(0, 10**6)/10**6, 6),
    containers
) for i in range(len(Ports))]

ships = [Ship(
    Ships[i]["ship_id"],
    ports,
    ConfigShip(
        Ships[i]["totalWeightCapacity"],
        Ships[i]["maxNumberOfAllContainers"],
        Ships[i]["maxNumberOfHeavyContainers"],
        Ships[i]["maxNumberOfRefrigeratedContainers"],
        Ships[i]["maxNumberOfLiquidContainers"],
        Ships[i]["fuelConsumptionPerKM"]
    ),
    containers,
    205 * (i+1)
    ) for i in range(len(Ships))]
for i in range(len(containers)-1):
    for ship in ships:
        if type(containers[i]) == str:
            break
        containerID = containers[i].id
        ship.load(containerID)
        ship.unload(containerID)
        ship.sailTo(ports[i])
    i+=1