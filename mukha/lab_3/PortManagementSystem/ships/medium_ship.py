from ships.ship import Ship

class MediumShip(Ship):
    def calculate_fuel(self):
        # Логіка розрахунку пального для середнього корабля
        self.fuel = self.capacity * 0.2  # Приклад логіки розрахунку пального

    def load_container(self, container):
        # Логіка завантаження контейнера на корабель
        pass
