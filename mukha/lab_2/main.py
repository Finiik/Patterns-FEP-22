import json
from containers import BasicContainer, HeavyContainer
from ships import Ship
from ports import Port
from events import load_container, unload_container, sail_to_port, refuel_ship

# Функція для завантаження JSON-файлу
def load_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

# Функція для обробки подій
def process_events(events_data):
    # Імплементуйте логіку для обробки подій тут
    pass

if __name__ == "__main__":
    # Завантаження JSON-файлів
    containers_data = load_json_file("containers.json")
    ships_data = load_json_file("ships.json")
    ports_data = load_json_file("ports.json")
    events_data = load_json_file("events.json")

    # Імплементуйте логіку для створення контейнерів, кораблів, портів

    # Обробка подій та дій
    process_events(events_data)

    if __name__ == "__main__":
        # Завантаження JSON-файлів
        containers_data = load_json_file("containers.json")
        ships_data = load_json_file("ships.json")
        ports_data = load_json_file("ports.json")
        events_data = load_json_file("events.json")

        # Імплементуйте логіку для створення контейнерів, кораблів, портів

        # Створення контейнерів
        containers = []
        for container_info in containers_data:
            container_id = container_info["container_id"]
            weight = container_info["weight"]
            container_type = container_info["container_type"]

            if container_type == "BasicContainer":
                container = BasicContainer(container_id, weight)
            elif container_type == "HeavyContainer":
                container = HeavyContainer(container_id, weight, container_type)
            else:
                print(f"Невідомий тип контейнера: {container_type}")
                continue

            containers.append(container)

        # Створення портів
        ports = []
        for port_info in ports_data:
            port_id = port_info["port_id"]
            latitude = port_info["latitude"]
            longitude = port_info["longitude"]
            port = Port(port_id, latitude, longitude)
            ports.append(port)

        # Створення кораблів
        ships = []
        for ship_info in ships_data:
            ship_id = ship_info["ship_id"]
            port_id = ship_info["port_id"]
            max_weight = ship_info["max_weight"]
            max_containers = ship_info["max_containers"]
            max_heavy_containers = ship_info["max_heavy_containers"]
            max_refrigerated = ship_info["max_refrigerated"]
            max_liquid = ship_info["max_liquid"]
            fuel_consumption = ship_info["fuel_consumption"]

            port = next((p for p in ports if p.port_id == port_id), None)
            if port is None:
                print(f"Порт з ID {port_id} не знайдено.")
                continue

            ship = Ship(ship_id, port, max_weight, max_containers, max_heavy_containers, max_refrigerated, max_liquid,
                        fuel_consumption)
            ships.append(ship)

        # Обробка подій та дій
        for event_info in events_data:
            event_type = event_info["event_type"]
            ship_id = event_info["ship_id"]
            container_id = event_info.get("container_id")
            destination_port = event_info.get("destination_port")

            ship = next((s for s in ships if s.ship_id == ship_id), None)
            if ship is None:
                print(f"Корабель з ID {ship_id} не знайдено.")
                continue

            if event_type == "load_container":
                container = next((c for c in containers if c.container_id == container_id), None)
                if container is None:
                    print(f"Контейнер з ID {container_id} не знайдено.")
                    continue
                load_container(ship, container)

            elif event_type == "unload_container":
                unload_container(ship, container_id)

            elif event_type == "sail_to_port":
                sail_to_port(ship, destination_port)

            elif event_type == "refuel_ship":
                refuel_ship(ship)

        # Виведення результатів
        # Імплементуйте логіку виведення результатів
        # Виведення інформації про порти
        print("Інформація про порти:")
        for port in ports:
            print(f"Port ID: ({port.latitude}, {port.longitude})")

            # Виведення контейнерів в порту
            container_count = len(port.containers)
            print(f"Кількість контейнерів в порту: {container_count}")
            print("{BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer}: {container_list}")

            # Виведення кораблів в порту
            ship_count = len(port.ships)
            print(f"Кількість кораблів в порту: {ship_count}")
            for ship in port.ships:
                print(f"Ship ID: {ship.ship_id}, FUEL_LEFT: {ship.fuel_left}")

        # Виведення інформації про кораблі
        print("\nІнформація про кораблі:")
        for ship in ships:
            print(f"Ship ID: {ship.ship_id}")
            print(f"Максимальна вага корабля: {ship.max_weight}")
            print(f"Максимальна кількість контейнерів на кораблі: {ship.max_containers}")

            # Перевірка, чи є атрибут 'max_refrigerated' у корабля
            # Виведення інформації про кораблі
            print("\nІнформація про кораблі:")
            for ship in ships:
                print(f"Ship ID: {ship.ship_id}")
                print(f"Максимальна вага корабля: {ship.max_weight}")
                print(f"Максимальна кількість контейнерів на кораблі: {ship.max_containers}")

                # Перевірка, чи є атрибут 'max_refrigerated' у корабля
                if hasattr(ship, 'max_refrigerated'):
                    print(f"Максимальна кількість рефрижераторних контейнерів на кораблі: {ship.max_refrigerated}")
                else:
                    print("Корабель не підтримує рефрижераторні контейнери.")

                print(f"Максимальна кількість важких контейнерів на кораблі: {ship.max_heavy_containers}")

                # Перевірка, чи є атрибут 'max_liquid' у корабля
                if hasattr(ship, 'max_liquid'):
                    print(f"Максимальна кількість рідких контейнерів на кораблі: {ship.max_liquid}")
                else:
                    print("Корабель не підтримує рідкі контейнери.")

                # Переконайтеся, що ви правильно вказали атрибут з залишком пального
                if hasattr(ship, 'fuel'):
                    print(f"Залишок пального: {ship.fuel}")
                else:
                    print("На кораблі відсутній атрибут 'fuel'.")


        # Виведення інформації про контейнери
        print("\nІнформація про контейнери:")
        for container in containers:
            print(f"Container ID: {container.container_id}")
            print(f"Weight: {container.weight}")
            print(f"Type: {container.container_type}")