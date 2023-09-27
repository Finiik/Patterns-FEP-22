class Port:
    def __init__(self, port_id, latitude, longitude):
        self.port_id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = {
            'BasicContainer': [],
            'HeavyContainer': [],
            'RefrigeratedContainer': [],
            'LiquidContainer': []
        }
        self.ships = []