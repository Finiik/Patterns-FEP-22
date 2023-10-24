import json

# Abstract Item class
class Item:
    def __init__(self, ID, weight, count, containerID):
        self.ID = ID
        self.weight = weight
        self.count = count
        self.containerID = containerID

    def get_total_weight(self):
        return self.weight * self.count

# Concrete item classes
class Small(Item):
    pass

class Heavy(Item):
    pass

class Refrigerated(Item):
    pass

class Liquid(Item):
    pass

# Container class to hold items
class Container:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

# Abstract Ship class
class Ship:
    def __init__(self, ID, capacity, fuel_capacity):
        self.ID = ID
        self.capacity = capacity
        self.fuel_capacity = fuel_capacity
        self.containers = []

    def load_container(self, container):
        self.containers.append(container)

# Concrete ship classes
class LightWeightShip(Ship):
    pass

class MediumShip(Ship):
    def __init__(self, ID, capacity, fuel_capacity, refrigerator):
        super().__init__(ID, capacity, fuel_capacity)
        self.refrigerator = refrigerator

class HeavyShip(Ship):
    def __init__(self, ID, capacity, fuel_capacity, refrigerator, fuel_bank):
        super().__init__(ID, capacity, fuel_capacity)
        self.refrigerator = refrigerator
        self.fuel_bank = fuel_bank

# Port class
class Port:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

# Simulation class to manage ports and ships
class PortManagementSystem:
    def __init__(self):
        self.ports = []
        self.ships = []

    def add_port(self, port):
        self.ports.append(port)

    def add_ship(self, ship):
        self.ships.append(ship)

    def sail_ship(self, ship, destination_port):
        # Implement logic to sail the ship from one port to another
        pass

    def load_items(self, ship, items):
        for item in items:
            # Check if there is a container for this item
            container = None
            for existing_container in ship.containers:
                if existing_container.item.__class__ == item.__class__:
                    container = existing_container
                    break

            if container is None:
                container = Container(item, item.count)
                ship.load_container(container)
            else:
                container.quantity += item.count

    def unload_items(self, ship, items):
        # Implement logic to unload items from a ship
        pass

    def to_json(self):
        ships_data = []
        for ship in self.ships:
            containers_data = [{"item": container.item.__class__.__name__, "quantity": container.quantity, "containerID": container.item.containerID} for container in ship.containers]
            ships_data.append({
                "ID": ship.ID,
                "capacity": ship.capacity,
                "fuel_capacity": ship.fuel_capacity,
                "containers": containers_data
            })

        return {
            "ports": [{"name": port.name, "coordinates": port.coordinates} for port in self.ports],
            "ships": ships_data
        }

# Example usage
if __name__ == '__main__':
    port1 = Port("Port A", (0.0, 0.0))
    port2 = Port("Port B", (10.0, 10.0))

    ship1 = LightWeightShip(1, 100, 1000.0)
    ship2 = MediumShip(2, 200, 2000.0, True)

    system = PortManagementSystem()
    system.add_port(port1)
    system.add_port(port2)
    system.add_ship(ship1)
    system.add_ship(ship2)

    items1 = [Small(1, 5.0, 10, 1), Heavy(2, 20.0, 5, 2), Refrigerated(3, 10.0, 3, 3)]
    items2 = [Liquid(4, 15.0, 7, 4), Small(5, 5.0, 5, 5), Heavy(6, 20.0, 7, 6)]

    system.load_items(ship1, items1)
    system.load_items(ship1, items2)  # Add items to the second container of ship1

    # Serialize the state to JSON
    json_data = system.to_json()
    print(json.dumps(json_data, indent=2))