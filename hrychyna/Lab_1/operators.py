from __future__ import annotations  # дозволяє використовувати типи об'єктів заздалегідь визначеними в анотаціях
from typing import TYPE_CHECKING  # імпортує модуль TYPE_CHECKING з бібліотеки typing,яка використовується для перевірки
# типів під час анотації, і далі буде використана для створення зациклених імпортів(циклічних залежностей) між модулями

from bill import Bill  # імпорт класу Bill з модуля bill

if TYPE_CHECKING:  # якщо імпортовано модуль TYPE_CHECKING
    from customer import Customer  # імпортує клас Customer з модуля customer


class Operator:
    """Holds operator details"""

    def __init__(self, _id: int, talking_charge: float, message_cost: float, network_charge: float,
                 discount_rate: int) -> None:  # ініціалізує конструктор класу Operator, який приймає певні параметри
        # і не повертає значення
        self.ID = _id
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    def create_bill(self) -> Bill:  # створюються обєкти рахунків для кожного оператора з однаковими обмеженнями
        bill = Bill(operator_id=self.ID)
        return bill

    def calculate_talking_cost(self, minutes: int, customer: Customer) -> float:
        # визначаємо, чи вік клієнта відповідає умовам для знижки
        if customer.age < 18 or customer.age > 65:
            # якщо вік клієнта менше 18 або більше 65, то застосовуємо знижку
            operator_discount_rate = self.discount_rate
        else:
            # якщо вік клієнта не підпадає під умови для знижки, то знижка 0%
            operator_discount_rate = 0
        # розраховуємо вартість розмови, використовуючи врахування знижки
        cost = minutes * (self.talking_charge * (1 - operator_discount_rate / 100))
        return cost

    def calculate_message_cost(self, quantity: int, customer: Customer, other: Customer) -> float:
        # перевірка чи користувачі викроистовують однакового оператора
        if customer.operators[customer.operator_name] == other.operators[other.operator_name]:
            # якщо так, то вартість повідомлення обчислюється зі знижкою
            return quantity * self.message_cost * (1 - self.discount_rate / 100)
        return quantity * self.message_cost  # якщо ні, то вартість повідомлення без знижки

    def calculate_network_cost(self, amount: float) -> float:  # обрахунок рахунку за інтернет
        return amount * self.network_charge
