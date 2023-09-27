class Ship:
    def __init__(self, ship_id, port_id, max_weight, max_containers, max_heavy_containers, max_refrigerated, max_liquid, fuel_consumption):
        self.ship_id = ship_id
        self.port_id = port_id
        self.max_weight = max_weight
        self.max_containers = max_containers
        self.max_heavy_containers = max_heavy_containers
        self.max_refrigerated = max_refrigerated
        self.max_liquid = max_liquid
        self.fuel_consumption = fuel_consumption
        self.current_weight = 0
        self.current_containers = 0
        self.current_heavy_containers = 0
        self.current_refrigerated = 0
        self.current_liquid = 0
        self.containers = []