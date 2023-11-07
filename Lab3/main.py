import json
from icecream import ic
from Items import CreateItem
import Containers
from Port import Port, ConfigPort
import Ship
from Containers import Container
with open("input.json", "r") as f:
    data = json.load(f)
confdata = []
ports = []
ships = []
items = []




confdata.append(data)

#placing all ports fom json into ports list
for i in confdata:
    for j in i:
      ports.append(Port(ConfigPort(**j)))

items.append(CreateItem.Create_Item(10, 3, 'B'))
items.append(CreateItem.Create_Item(10, 3, 'B'))
items.append(CreateItem.Create_Item(10, 3, 'B'))
items.append(CreateItem.Create_Item(200, 6, 'H'))
items.append(CreateItem.Create_Item(2000, 4, 'L'))
ports[0].create_container('H', 4000)
ports[0].create_container('R', 4000)
ports[0].create_container('L', 4000)
ports[0].create_container('B', 100)
ports[0].basic_containers[0].add_item(items[0])
ports[0].basic_containers[0].add_item(items[1])
ports[0].liquid_containers[0].add_item(items[4])
for item in ports[0].basic_containers[0].items:
    ic(item)
#__________________________
#ERROR
#__________________________
#placing all ships from json into ships list
    for i in ports:
        ic(i)
        for j in i.config_port.ships:
            ship = Ship.Ship(Ship.ConfigShip(*list(j.values())))
            ic(ship)
            if ship.get_weight()<=1000:
                i.ships.append(Ship.LightWeightSHipFactory.create_ship(ship.ship_config))
            elif ship.get_weight()<=10000 and ship.get_weight()>1000:
                i.ships.append(Ship.MediumShipFactory.create_ship(ship.ship_config))
            elif ship.get_weight()<=100000 and ship.get_weight()>10000:
                i.ships.append(Ship.HeavyShipFactory.create_ship(ship.ship_config))


    ports[2].get_ships()
    ports[1].get_ships()
    ports[2].ships[2].sail_to(ports[0], ports[1])
    ports[2].get_ships()
    ports[1].get_ships()
    container = ports[0].create_container('B', 100)


    ports[0].ships[0].load(ports[0].basic_containers[0], ports[0])



x=[]
y=[]
for port in ports:
  for i in port.ships:
    y.append({
      "ship": f"{i.get_id()}",
      "fuel": f"{i.fuel}",
      "Basic_containers": f"{i.get_current_container()}",

    })
  x.append({
      "Port": f"{port.port_id}",
      "Longitude": f"{port.config_port.longitude}",
      "Latitude": f"{port.config_port.latitude}",
      "Basic_containers": f"{port.basic_containers}",
      "Heavy_containers": f"{port.heavy_containers}",
      "liquid_containers": f"{port.liquid_containers}",
      "Refgirigerated_containers": f"{port.refrigirator_containers}",
      "Ships": y
        })

j_object = json.dumps(x)

with open("data.json", "w") as outfile:
    outfile.write(j_object)
