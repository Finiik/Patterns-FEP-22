class Ship:
    def __init__(self, ship_id, port, max_weight, max_containers, max_heavy_containers,
                 max_refrigerated, max_liquid, fuel_consumption):
        self.ship_id = ship_id
        self.port = port
        self.max_weight = max_weight
        self.max_containers = max_containers
        self.max_heavy_containers = max_heavy_containers
        self.max_refrigerated = max_refrigerated
        self.max_liquid = max_liquid
        self.fuel_consumption = fuel_consumption
        self.fuel = 0
        self.containers = []

    def get_current_containers(self):
        return sorted(self.containers, key=lambda container: container.container_id)

    def load_container(self, container):
        if len(self.containers) < self.max_containers:
            self.containers.append(container)
            return True
        return False

    def unload_container(self, container_id):
        container = next((c for c in self.containers if c.container_id == container_id), None)
        if container:
            self.containers.remove(container)
            return True
        return False

    def sail_to(self, destination_port):
        # Implement sailing logic
        if self.has_enough_fuel(destination_port):
            self.port.outgoing_ship(self)
            self.port = destination_port
            destination_port.incoming_ship(self)
            self.consume_fuel(destination_port)
            return True
        else:
            return False

    def refuel(self):
        self.fuel = 100

    def consume_fuel(self, destination_port):
        distance = self.port.get_distance(destination_port)
        fuel_consumed = self.fuel_consumption * distance
        self.fuel -= fuel_consumed

    def has_enough_fuel(self, destination_port):
        distance = self.port.get_distance(destination_port)
        required_fuel = self.fuel_consumption * distance
        return self.fuel >= required_fuel
