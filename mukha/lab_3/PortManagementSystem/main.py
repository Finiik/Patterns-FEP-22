from factories.item_factory import ItemFactory
from factories.ship_factory import ShipFactory
from builders.ship_builder import ShipBuilder
from items.small import Small
from items.heavy import Heavy
from items.refrigerated import Refrigerated
from items.liquid import Liquid
from ships.light_weight_ship import LightWeightShip
from ships.medium_ship import MediumShip
from ships.heavy_ship import HeavyShip
from ports import Port  # Імпортуємо клас Port із файлу ports.py



def main():
    # Створення фабрики для створення предметів
    item_factory = ItemFactory()

    # Створення фабрики для створення кораблів
    ship_factory = ShipFactory()

    # Створення будівельника кораблів
    ship_builder = ShipBuilder()

    # Приклад конфігурації для створення контейнерів
    container_configuration = {
        'ID': 1,
        'weight': 10.0,
        'count': 5,
        'containerID': 101
    }

    # Створення предметів (контейнерів)
    small_container = item_factory.create_item("Small", container_configuration)
    heavy_container = item_factory.create_item("Heavy", container_configuration)
    refrigerated_container = item_factory.create_item("Refrigerated", container_configuration)
    liquid_container = item_factory.create_item("Liquid", container_configuration)

    # Приклад конфігурації для створення кораблів
    ship_configuration = {
        'ID': 1,
        'weight': 100.0,
        'capacity': 500,
        'fuel_capacity': 50
    }

    # Створення кораблів
    light_ship = ship_factory.create_ship("LightWeight", ship_configuration)
    medium_ship = ship_factory.create_ship("Medium", ship_configuration)
    heavy_ship = ship_factory.create_ship("Heavy", ship_configuration)

    # Створення портів
    port1 = Port("Port 1", "Location 1", {"latitude": 12.345, "longitude": 67.890}, 1000)
    port2 = Port("Port 2", "Location 2", {"latitude": 34.567, "longitude": 89.012}, 1500)

    # Завантаження контейнерів на кораблі
    light_ship.load_container(small_container)
    medium_ship.load_container(heavy_container)
    heavy_ship.load_container(refrigerated_container)
    light_ship.load_container(liquid_container)

    # Розрахунок пального для кораблів
    light_ship.calculate_fuel()
    medium_ship.calculate_fuel()
    heavy_ship.calculate_fuel()

    # Виведення результатів у форматі JSON
    result = {
        "LightShip": {
            "ID": light_ship.id,
            "Weight": light_ship.weight,
            "Capacity": light_ship.capacity,
            "Fuel Capacity": light_ship.fuel_capacity,
            "Fuel": light_ship.fuel
        },
        "MediumShip": {
            "ID": medium_ship.id,
            "Weight": medium_ship.weight,
            "Capacity": medium_ship.capacity,
            "Fuel Capacity": medium_ship.fuel_capacity,
            "Fuel": medium_ship.fuel
        },
        "HeavyShip": {
            "ID": heavy_ship.id,
            "Weight": heavy_ship.weight,
            "Capacity": heavy_ship.capacity,
            "Fuel Capacity": heavy_ship.fuel_capacity,
            "Fuel": heavy_ship.fuel
        }
    }

    print("Light Ship:")
    for key, value in result["LightShip"].items():
        print(f"{key}: {value}")

    print("\nMedium Ship:")
    for key, value in result["MediumShip"].items():
        print(f"{key}: {value}")

    print("\nHeavy Ship:")
    for key, value in result["HeavyShip"].items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
