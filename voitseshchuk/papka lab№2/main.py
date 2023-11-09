import json
from port import Port
from ship import Ship

with open('input.json', 'r') as file:
    data = json.load(file)

ports = [Port(port['ID'], port['latitude'], port['longitude']) for port in data['ports']]

ships = [Ship(ship['ID'], next(port for port in ports if port.ID == ship['port_ID']), ship['max_weight'],
              ship['max_num_containers'], ship['max_num_heavy_containers'], ship['max_num_refrigerated'],
              ship['max_num_liquid'], ship['fuel_consumption']) for ship in data['ships']]
