class Ship:
    def __init__(self, config):
        self.id = config['ID']
        self.weight = config['weight']
        self.capacity = config['capacity']
        self.fuel_capacity = config['fuel_capacity']
        self.fuel = 0

    def load_container(self, container):
        # Логіка завантаження контейнера на корабель
        pass

    def calculate_fuel(self):
        # Логіка розрахунку пального для корабля
        pass

    def to_dict(self):
        return {
            'ID': self.id,
            'weight': self.weight,
            'capacity': self.capacity,
            'fuel_capacity': self.fuel_capacity,
            'fuel': self.fuel
        }
