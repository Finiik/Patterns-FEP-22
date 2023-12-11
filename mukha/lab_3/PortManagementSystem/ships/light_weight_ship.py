from ships.ship import Ship

class LightWeightShip(Ship):
    def calculate_fuel(self):
        # Логіка розрахунку пального для легкого корабля
        self.fuel = self.capacity * 0.1  # Приклад логіки розрахунку пального

    def load_container(self, container):
        # Логіка завантаження контейнера на корабель
        pass
