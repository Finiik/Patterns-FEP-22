import json
import random
from uuid import uuid4
from containers import *
from port import IPort, PortClass
from ship import IShip, ShipСlass, ConfigShip

input_file_path = "input.json"

# Считування з json
with open(input_file_path, "r") as infile:
    data = json.load(infile)

print(f"All Data on Json")
print()

for port_data in data:
    print(f"Port ID: {port_data['port_id']}")
    print(f"Basic Containers: {port_data['basic']}")
    print(f"Heavy Containers: {port_data['heavy']}")
    print(f"Refrigerated Containers: {port_data['refrigerated']}")
    print(f"Liquid Containers: {port_data['liquid']}")

    print("Ships:")
    for ship_data in port_data['ships']:
        print(f"  Ship ID: {ship_data['ship_id']}")
        print(f"  Total Weight Capacity: {ship_data['totalWeightCapacity']}")
        print(f"  Max Number Of All Containers: {ship_data['maxNumberOfAllContainers']}")
        print(f"  Max Number Of Heavy Containers: {ship_data['maxNumberOfHeavyContainers']}")
        print(f"  Max Number Of Refrigerated Containers: {ship_data['maxNumberOfRefrigeratedContainers']}")
        print(f"  Max Number Of Liquid Containers: {ship_data['maxNumberOfLiquidContainers']}")
        print(f"  Fuel Consumption Per KM: {ship_data['fuelConsumptionPerKM']}")

        print()

    print()

portsID = [port["port_id"] for port in data]

#Стягування
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
for port_data in data:
    fillerPortList = {}
    fillerPortList["port_id"] = port_data["port_id"]
    fillerPortList["ships"] = [ship for ship in Ships if ship["port_id"] == fillerPortList["port_id"]]
    fillerPortList["basic"] = port_data["basic"]
    fillerPortList["heavy"] = port_data["heavy"]
    fillerPortList["refrigerated"] = port_data["refrigerated"]
    fillerPortList["liquid"] = port_data["liquid"]
    Ports.append(fillerPortList)

json_object = json.dumps(Ports, indent=2)
output_file_path = "output.json"

with open(output_file_path, "w") as outfile:
    outfile.write(json_object)

# створення обєктів з випадковими координатами з завкругленням
containers = [BasicContainer(250), BasicContainer(450), HeavyContainer(350), RefrigeratedContainer(250.5), LiquidContainer(124)]
ports = [PortClass(
  Ports[i]["port_id"],
  round(random.uniform(0, 10**4)/10**4, 4),
  round(random.uniform(0, 10**4)/10**4, 4),
  containers
)
# Пальне
for i in range(len(Ports))]
ships = [ShipСlass(
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
404*(i+1)
  )
for i in range(len(Ships))]
for i in range(len(containers)-1):
  for ship in ships:
    if type(containers[i]) == str:
      break
    containerID = containers[i].id
    ship.load(containerID)
    ship.unload(containerID)
    ship.sailTo(ports[i])
  i+=1
