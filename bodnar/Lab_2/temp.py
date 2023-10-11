import json
from uuid import uuid4
import random

ports_id = [str(uuid4()) for i in range(5)]

ships = []
for i in range(10):
    ship = {}
    ship["ship_id"] = str(uuid4())
    ship["port_id"] = random.choice(ports_id)
    ship["ports_deliver"] = random.choice([i for i in ports_id if i != ship["ship_id"]])
    ship["max_number_of_all_containers"] = 20
    ship["max_number_of_heavy_containers"] = 5
    ship["max_number_of_refrigerated_containers"] = 2
    ship["max_number_of_liquid_containers"] = 5
    ship["fuel_consumption_per_km"] = 20
    ships.append(ship)

ports = []
for i in range(5):
    port = {}
    port["port_id"] = ports_id[i]
    port["ships"] = [ship for ship in ships if ship["port_id"] == port["port_id"]]
    port["basic"] = random.randint(1, 10)
    port["heavy"] = random.randint(1, 8)
    port["refrigerated"] = random.randint(1, 5)
    port["liquid"] = random.randint(1, 5)
    ports.append(port)

json_object = json.dumps(ports, indent=2)

with open('input.json', 'w') as outfile:
    outfile.write(json_object)
