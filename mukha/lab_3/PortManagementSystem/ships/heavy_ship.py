from ships.ship import Ship

class HeavyShip(Ship):
    def calculate_fuel(self):
        # Логіка розрахунку пального для важкого корабля
        self.fuel = self.capacity * 0.3  # Приклад логіки розрахунку пального

    def load_container(self, container):
        # Логіка завантаження контейнера на корабель
        pass
