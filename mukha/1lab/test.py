import json

class Operator:
    def __init__(self, ID, talking_charge, message_cost, network_charge, discount_rate):
        self.ID = ID
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    def calculate_talking_cost(self, minutes, customer):
        cost = minutes * self.talking_charge
        if 18 <= customer.get_age() < 65:
            cost -= cost * (self.discount_rate / 100.0)
        return cost

    def calculate_message_cost(self, quantity, sender, receiver):
        cost = quantity * self.message_cost
        if sender.get_operator().ID == receiver.get_operator().ID:
            cost -= cost * (self.discount_rate / 100.0)
        return cost

    def calculate_network_cost(self, amount):
        return amount * self.network_charge

class Bill:
    def __init__(self, limiting_amount):
        self.limiting_amount = limiting_amount
        self.current_debt = 0.0

    def check(self, amount):
        return self.current_debt + amount <= self.limiting_amount

    def add(self, amount):
        self.current_debt += amount

    def pay(self, amount):
        self.current_debt -= amount

    def change_the_limit(self, amount):
        self.limiting_amount = amount

class Customer:
    def __init__(self, id, name, age, limiting_amount):
        self.ID = id
        self.name = name
        self.age = age
        self.operator_ptr = None
        self.bill = Bill(limiting_amount)
        self.limiting_amount = limiting_amount

    def talk(self, minutes, other):
        cost = self.operator_ptr.calculate_talking_cost(minutes, other)
        if self.bill.check(cost):
            self.bill.add(cost)
            cost = round(cost, 2)  # Округлення до двох знаків після коми
            print(f"{self.name} talking with {other.name} during {minutes} minutes for {cost} units.")
        else:
            print("The call could not be made: there are not enough funds in the account.")

    def message(self, quantity, other):
        cost = self.operator_ptr.calculate_message_cost(quantity, self, other)
        if self.bill.check(cost):
            self.bill.add(cost)
            cost = round(cost, 2)  # Округлення до двох знаків після коми
            print(f"{self.name} sends {quantity} messages to {other.name} for {cost} units.")
        else:
            print("Failed to send messages: insufficient funds in account.")

    def connection(self, amount):
        cost = self.operator_ptr.calculate_network_cost(amount)
        if self.bill.check(cost):
            self.bill.add(cost)
            cost = round(cost, 2)  # Округлення до двох знаків після коми
            print(f"{self.name} uses the Internet for {amount} MB for {cost} units.")
        else:
            print("Could not connect to the Internet: insufficient funds in the account.")

    def pay_bill(self, amount):
        if amount >= 0:
            self.bill.pay(amount)
            print(f"{self.name} paid {amount} units towards the bill.")
        else:
            print("Invalid payment amount: must be non-negative.")

    def change_operator(self, new_operator):
        self.operator_ptr = new_operator
        print(f"{self.name} changed operator to {new_operator.ID}.")

    def change_limit(self, amount):
        if amount >= 0:
            self.bill.change_the_limit(amount)
            print(f"{self.name} changed bill limit to {amount} units.")
        else:
            print("Invalid bill limit: must be non-negative.")

    def get_age(self):
        return self.age

    def get_operator(self):
        return self.operator_ptr

    def get_bill(self):
        return self.bill

    def get_limiting_amount(self):
        return self.limiting_amount

    def set_limiting_amount(self, amount):
        self.limiting_amount = amount

def main():
    # Зчитуємо JSON з файлу
    with open("info.json") as input_file:
        data = json.load(input_file)

    # Отримуємо клієнтів та операторів з JSON
    customers = []  # Список клієнтів
    operators = []  # Список операторів

    # Зчитуємо клієнтів з JSON і додаємо їх до списку customers
    for customer_data in data["customers"]:
        id = customer_data["id"]
        name = customer_data["name"]
        age = customer_data["age"]
        limit = customer_data["limit"]
        customers.append(Customer(id, name, age, limit))

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
def main():
    # Зчитуємо JSON з файлу
    with open("info.json") as input_file:
        data = json.load(input_file)

    # Отримуємо клієнтів та операторів з JSON
    customers = []  # Список клієнтів
    operators = []  # Список операторів

    # Зчитуємо клієнтів з JSON і додаємо їх до списку customers
    for customer_data in data["customers"]:
        id = customer_data["id"]
        name = customer_data["name"]
        age = customer_data["age"]
        limit = customer_data["limit"]
        customers.append(Customer(id, name, age, limit))

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


