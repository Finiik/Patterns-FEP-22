from __future__ import annotations  # дозволяє використовувати типи об'єктів заздалегідь визначеними в анотаціях
from typing import Dict  # імпортується тип Dict з модуля typing для використання його в анотаціях типів
from operators import Operator  # імпорт класу Operator з модуля operators
from bill import Bill  # імпорт класу Bill з модуля bill


class Customer:  # оголошення класу Customer, який представляє клієнта в системі
    """Holds Customer details"""
    def __init__(self, _id: int, first_name: str, second_name: str, age: int,  # Конструктор класу Customer, який
                 operators: Dict[str, Operator], bills: Dict[str, Bill], limiting_amount: float) -> None:
        # ініціалізує об'єкт класу з певними параметрами
        self.id = _id  # встановлення атрибуту id для об'єкта класу на основі переданого _id
        self._first_name = first_name
        self.second_name = second_name
        self.age = age
        self.operators = operators
        self.bills = self._generate_bill()
        self.limiting_amount = limiting_amount
        self.operator_name = None  # ініціалізація атрибуту operator_name об'єкта класу значенням None

    @property  # цей декоратор вказує, що метод first_name є властивістю (property) об'єкта класу
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:  # метод first_name є setter (встановлювачем) для атрибуту _first_name
        if not isinstance(value, str):  # перевірка, чи переданий value є рядком
            # помилка ValueError(користувач надає функції не дійсне число), якщо переданий value не є рядком
            raise ValueError(f"Provided name {value} is not of string type")
        self._first_name = value  # встановлення значення атрибуту _first_name на основі переданого value

    def _generate_bill(self):
        bills = {}
        for operator_id, operator in self.operators.items():
            bills[operator_id] = operator.create_bill()
        return bills

    # метод talk приймає наступні параметри:
    # self: спеціальний параметр, що вказує на поточний об'єкт класу Customer
    # minutes: ціле число, кількість хвилин, протягом яких клієнт буде розмовляти
    # other: інший об'єкт класу Customer, з яким клієнт буде розмовляти
    def talk(self, minutes: int, other: Customer) -> None:
        # рядок отримує оператора (об'єкт класу Operator), який обслуговує поточного клієнта
        # self.operator_name вказує на ім'я оператора, який обслуговує клієнта
        # потім це ім'я використовується для отримання відповідного оператора зі словника self.operators
        operator = self.operators[self.operator_name]
        cost = operator.calculate_talking_cost(minutes, self)  # обчислює вартість розмови для поточного клієнтa
        if self.check_limit(cost):  # перевіряє, чи поточний клієнт має достатньо коштів на своєму рахунку
            # якщо умова if вище поверне True, то ця стрічка додає вартість розмови до рахунку клієнта
            # тут використовується метод add об'єкта self.bills[self.operator_name], який визначений в класі Bill
            self.bills[self.operator_name].add(cost)
            # f спосіб форматує рядок, для кращої читабельності і швидкості виконання
        print(f"{self.first_name} talked to {other.first_name} for {minutes} minutes.")

    def message(self, quantity: int, other: Customer) -> None:  # quantity - кількість повідомлень
        # перевіряє, чи обидва користувачі використовують одного і того ж оператора
        if self.operators[self.operator_name] == other.operators[other.operator_name]:
            operator_discount_rate = self.operators[self.operator_name].discount_rate  # отримує розмір знижки
            # обчислює вартість повідомлень. Вона дорівнює кількість повідомлень,
            # помножену на вартість одного повідомлення, з урахуванням знижки оператора.
            cost = quantity * self.operators[self.operator_name].message_cost * (1 - operator_discount_rate / 100)
        else:  # якщо користувачі використовують різних операторів
            cost = quantity * self.operators[self.operator_name].message_cost  # вартість повідомлення без знижки

        if self.check_limit(cost):  # чи користувач має достатньо коштів на рахунку
            self.bills[self.operator_name].add(cost)  # додає вартість повідомлень до рахунку користувача
        print(f"{self.first_name} sent {quantity} messages to {other.first_name}.")

    def connection(self, amount: float) -> None:  # self - обєкт класу , amount - кількість мегабайтів
        # вартість розраховується, помножуючи кількість мегабайтів на вартість (network_charge),
        # яка визначена для поточного користувача
        cost = amount * self.operators[self.operator_name].network_charge
        # self.check_limit(cost) - виклик методу check_limit з поточного об'єкта Customer,
        # який приймає вартість (cost) і повертає True, якщо ліміт не буде перевищений,
        # або False, якщо ліміт перевищиться.
        if self.check_limit(cost):  # чи користувач може виконати цю дію, не перевищуючи ліміт рахунку
            self.bills[self.operator_name].add(cost)  # додає вартість cost до рахунку користувача
            print(f"{self.first_name} used {amount} MB of data.")

    def pay_bills(self, operator_name: str, amount: float) -> None:
        # self.bills[operator_name] вказує на об'єкт рахунку, який належить оператору з іменем operator_name
        # метод .pay(amount) викликається на цьому об'єкті рахунку з переданою сумою amount, щоб здійснити оплату
        self.bills[operator_name].pay(amount)
        print(f"{self.first_name} paid {amount} for the {operator_name} bill.")

    def change_operator(self, new_operator_name: str) -> None:
        # присвоює значення параметра new_operator_name атрибуту operator_name
        self.operator_name = new_operator_name
        print(f"{self.first_name} changed the operator to {new_operator_name}.")

    def change_limit(self, new_limit: float, operator_name: str) -> None:
        # рядок звертається до рахунку користувача, який належить конкретному оператору (operator_name),
        # і викликає метод change_limit цього рахунку, передаючи новий ліміт new_limit як аргумент
        self.bills[operator_name].change_limit(new_limit)
        print(f"{self.first_name} changed the {operator_name} bill limit to {new_limit}.")

    def check_limit(self, cost: float) -> bool:  # параметр cost приймає вартість
        return self.bills[self.operator_name].check(cost)
        # функція обирає рахунок користувача, який вказаний у змінній self.operator_name, із словника self.bills
        # потім функція викликає метод check рахунку користувача, передаючи йому cost як аргумент
        # метод check рахунку перевіряє, чи може користувач оплатити вартість cost без перевищення ліміту на рахунку
        # результат - булеве значення True(користувач може оплатити cost без перев лім),
        # і False, якщо ліміт буде перевищений
