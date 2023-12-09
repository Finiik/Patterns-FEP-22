import json

from Operator import Operator
from Bill import Bill
from Customer import Customer


def main():
    # Зчитуємо JSON з файлу
    with open("info.json") as input_file:
        data = json.load(input_file)

    # Отримуємо клієнтів та операторів з JSON
    customers = []  # Список клієнтів
    operators = []  # Список операторів

    # Зчитуємо клієнтів з JSON і додаємо їх до списку customers
    for customer_data in data["customers"]:
        #id = customer_data["id"]
        name = customer_data["name"]
        age = customer_data["age"]
        limit = customer_data["limit"]
        customers.append(Customer( name, age, limit))

    # Зчитуємо операторів з JSON і додаємо їх до списку operators
    for operator_data in data["operators"]:
        id = operator_data["id"]
        talking_charge = operator_data["talkingCharge"]
        message_cost = operator_data["messageCost"]
        network_charge = operator_data["networkCharge"]
        discount_rate = operator_data["discountRate"]
        operators.append(Operator(id, talking_charge, message_cost, network_charge, discount_rate))

    print("Customers:")
    for customer in customers:
        print(f"ID: {customer.ID}, Name: {customer.name}, Age: {customer.age}, Limit: {customer.limiting_amount}")

    print("Operators:")
    for oper in operators:
        print(f"ID: {oper.ID}, Talking Charge: {oper.talking_charge}, Message Cost: {oper.message_cost}, Network Charge: {oper.network_charge}, Discount Rate: {oper.discount_rate}")

    print("\n")

    # Перевіряємо, чи є щонайменше два клієнта у списку customers
    if len(customers) >= 2:
        customer1 = customers[0]
        customer2 = customers[1]

        # Встановлюємо вказівники на операторів для клієнтів
        customer1.operator_ptr = operators[0]
        customer2.operator_ptr = operators[1]

        # Виконуємо операції між двома клієнтами в обидва боки
        customer1.talk(10, customer2)
        customer1.message(5, customer2)
        customer1.connection(200)
        customer1.bill.pay(50)
        customer1.operator_ptr.talking_charge = 0.15
        customer1.limiting_amount = 200

        customer2.talk(5, customer1)
        customer2.message(3, customer1)
        customer2.connection(100)
        customer2.bill.pay(30)
        customer2.operator_ptr.talking_charge = 0.18
        customer2.limiting_amount = 300
    else:
        print("Error: There should be at least two customers in the JSON data.")

if __name__ == "__main__":
    main()
