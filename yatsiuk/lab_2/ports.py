class Port:
    def __init__(self, port_id, latitude, longitude):
        self.port_id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.ships = []

    def get_distance(self, other_port):
        # Calculate and return the distance using geospatial calculations
        pass

    def sail_to(self, destination_port):
        # Implement the sailing logic
        pass

    def refuel(self, ship):
        # Implement refueling logic
        pass

    def load(self, container):
        self.containers.append(container)

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
        else:
            print(f"Container {container.container_id} does not exist")

    def incoming_ship(self, ship):
        self.ships.append(ship)

    def outgoing_ship(self, ship):
        self.ships.remove(ship)

    def __str__(self):
        return f"Port ID: ({self.latitude}, {self.longitude})"
