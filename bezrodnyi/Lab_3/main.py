import json
from factory import ItemFactory, ShipFactory
from factory import ItemFactory
from item import ItemDecorator
from port import Port


def simulate_port_management():
    # Створення порту
    port_coordinates = (100.32, 47.87)  # Приклад координат порту
    port = Port("Port of Los Angeles", port_coordinates)

    # Створення корабля
    ship = ShipFactory.createLightWeightShip("Вантажний", 5000, 2000)

    # Створення предметів
    small_item = ItemFactory.createSmallItem(6, 16, 5, 2254)

    # Створення декоратора для предмета в контейнері
    small_item_in_container = ItemDecorator(small_item, 6, 16, 5, 2254)

    # Завантаження контейнера на корабель та розвантаження
    port.loadContainers([small_item_in_container])
    ship.loadItems(port.unloadContainers(ship))

    # Виведення результатів у JSON, включаючи інформацію про контейнери та предмети
    result = {
        "Назва порта": port.Name,
        "Координати порту": port.Coordinates,
        "Тип корабля": ship.Type,
        "Вага коробля": ship.weight,
        "Ємність паливного баку": ship.fuel_capacity,
        "Контейнер інфо": [
            {
                "Тип": small_item_in_container.item.item_type,
                "ID": small_item_in_container.item.ID,
                "Вага контейнера": small_item_in_container.item.weight,
                "Кількість предметів в контейнері": small_item_in_container.item.count,
                "ID контейнера": small_item_in_container.item.containerID,
            }
        ],
    }

    # Серіалізація в JSON і виведення у консоль
    json_result = json.dumps(result, ensure_ascii=False, indent=4)
    return json_result

if __name__ == "__main__":
    output_json = simulate_port_management()

    # Print the JSON result to the console
    print(output_json)

    # You can also save it to a file if needed
    with open('output.json', 'w', encoding='utf-8') as file:
        file.write(output_json)