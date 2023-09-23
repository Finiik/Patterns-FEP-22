from operators import Operator
from bill import Bill
from customer import Customer

operators = {  # створюємо словник operators, де ключами є імена операторів(operator1 і operator2), вводимо параметри
    "lifecell": Operator(0, 0.1, 0.01, 0.001, 10),
    "kyivstar": Operator(1, 0.2, 0.02, 0.002, 15)
}
# створюємо словник bills де ключами є імена операторів, вводимо параметри(ліміти)
bills = {
    "lifecell": Bill(100),
    "kyivstar": Bill(150)
}
# створюємо об'єкт класу Customer з ініціалізованими параметрами
customer1 = Customer(0, "Kiara", "Johnson", 25, operators, bills, 1000)
customer1.operator_name = "lifecell"  # встановлюємо ім'я оператора для customer1
# аналогічно ...
customer2 = Customer(1, "Henry", "Mikaelson", 20, operators, bills, 1200)
customer2.operator_name = "kyivstar"

# встановлюємо час розмови, к-сть повідомлень, к-сть використаних МВ, сплачуємо рахунок, змінюємо оператора і ліміт
customer1.talk(30, customer2)
customer2.message(10, customer1)
customer1.connection(1769)
customer1.pay_bills("lifecell", 150)
customer1.change_operator("kyivstar")
customer1.change_limit(200, "lifecell")
