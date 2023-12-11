    class Port:
        def __init__(self, name, location, coordinates, capacity):
            self.name = name
            self.location = location
            self.coordinates = coordinates
            self.capacity = capacity
            self.items = []

        def load_ship(self, ship):
            # Реалізуйте логіку завантаження корабля в порт
            pass

        def unload_ship(self, ship):
            # Реалізуйте логіку вивантаження корабля в порт
            pass

        def sail_to(self, destination_port):
            # Реалізуйте логіку переходу корабля до іншого порту
            pass

        def __str__(self):
            return f"Port: {self.name}, Location: {self.location}, Capacity: {self.capacity}"

        def to_dict(self):
            return {
                "name": self.name,
                "location": self.location,
                "coordinates": self.coordinates,
                "capacity": self.capacity,
                "items": [item.to_dict() for item in self.items]
            }
