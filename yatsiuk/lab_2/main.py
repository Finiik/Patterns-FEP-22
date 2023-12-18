import json
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from ships import Ship
from ports import Port

def load_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def create_container(container_info):
    container_id = container_info["container_id"]
    weight = container_info["weight"]
    container_type = container_info["container_type"]

    if container_type == "BasicContainer":
        return BasicContainer(container_id, weight)
    elif container_type == "HeavyContainer":
        return HeavyContainer(container_id, weight)
    elif container_type == "RefrigeratedContainer":
        return RefrigeratedContainer(container_id, weight)
    elif container_type == "LiquidContainer":
        return LiquidContainer(container_id, weight)
    else:
        print(f"Unknown container type: {container_type}")
        return None

def create_ship(ship_info, ports):
    ship_id = ship_info["ship_id"]
    port_id = ship_info["port_id"]
    port = next((p for p in ports if p.port_id == port_id), None)

    if port is None:
        print(f"Port with ID {port_id} not found.")
        return None

    max_weight = ship_info["max_weight"]
    max_containers = ship_info["max_containers"]
    max_heavy_containers = ship_info["max_heavy_containers"]
    max_refrigerated = ship_info.get("max_refrigerated", 0)
    max_liquid = ship_info.get("max_liquid", 0)
    fuel_consumption = ship_info["fuel_consumption"]

    return Ship(ship_id, port, max_weight, max_containers, max_heavy_containers, max_refrigerated, max_liquid, fuel_consumption)

def process_events(events_data, ships, containers, ports):
    for event_info in events_data["events"]:
        event_type = event_info["event_type"]
        ship_id = event_info["ship_id"]
        ship = next((s for s in ships if s.ship_id == ship_id), None)

        if ship is None:
            print(f"Ship with ID {ship_id} not found.")
            continue

        if event_type == "load_container":
            container_id = event_info["container_id"]
            container = next((c for c in containers if c.container_id == container_id), None)

            if container is None:
                print(f"Container with ID {container_id} not found.")
                continue

            if ship.load_container(container):
                ship.port.unload(container)
            else:
                print(f"Ship {ship_id} cannot load more containers.")

        elif event_type == "unload_container":
            container_id = event_info["container_id"]
            if not ship.unload_container(container_id):
                print(f"Container with ID {container_id} not found on ship {ship_id}.")

        elif event_type == "sail_to_port":
            destination_port_id = event_info["destination_port"]
            destination_port = next((p for p in ports if p.port_id == destination_port_id), None)

            if destination_port is None:
                print(f"Destination port with ID {destination_port_id} not found.")
                continue

            if ship.sail_to(destination_port):
                print(f"Ship {ship.ship_id} sailed to Port {destination_port_id}.")
            else:
                print(f"Ship {ship.ship_id} does not have enough fuel to reach Port {destination_port_id}.")

        elif event_type == "refuel_ship":
            ship.refuel()
            print(f"Ship {ship.ship_id} has been refueled.")

def main():
    containers_data = load_json_file("containers.json")
    ships_data = load_json_file("ships.json")
    ports_data = load_json_file("ports.json")
    events_data = load_json_file("events.json")

    if containers_data is None or ships_data is None or ports_data is None or events_data is None:
        return

    containers = [create_container(container_info) for container_info in containers_data["containers"]]
    ports = [Port(port_info["port_id"], port_info["latitude"], port_info["longitude"]) for port_info in ports_data["ports"]]
    ships = [create_ship(ship_info, ports) for ship_info in ships_data["ships"]]

    process_events(events_data, ships, containers, ports)

if __name__ == "__main__":
    main()
