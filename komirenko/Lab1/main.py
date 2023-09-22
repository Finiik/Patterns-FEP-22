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
        if customer.get_age() < 18:
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

    def change_limit(self, amount):
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
            cost = round(cost, 2)
            print(f"{self.name} was talking with {other.name} for {minutes} minutes, which costs {cost} hrn.")
        else:
            print("Call unsuccessful: insufficient funds.")

    def message(self, quantity, other):
        cost = self.operator_ptr.calculate_message_cost(quantity, self, other)
        if self.bill.check(cost):
            self.bill.add(cost)
            cost = round(cost, 2)
            print(f"{self.name} sent {quantity} messages to {other.name}, which costs {cost} hrn.")
        else:
            print("Failed to send messages: insufficient funds.")

    def connect(self, amount):
        cost = self.operator_ptr.calculate_network_cost(amount)
        if self.bill.check(cost):
            self.bill.add(cost)
            cost = round(cost, 2)
            print(f"{self.name} used {amount} MB of internet, which costs {cost} hrn.")
        else:
            print("Could not connect to the internet: insufficient funds.")

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def get_operator(self):
        return self.operator_ptr

    def get_bill(self):
        return self.bill

    def get_limiting_amount(self):
        return self.limiting_amount

    def set_limiting_amount(self, amount):
        self.limiting_amount = amount

def main():
    with open("info.json") as input_file:
        data = json.load(input_file)

    customers = []
    operators = []

    for customer_data in data["customers"]:
        id = customer_data["id"]
        name = customer_data["name"]
        age = customer_data["age"]
        limit = customer_data["limit"]
        customers.append(Customer(id, name, age, limit))

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

    if len(customers) >= 2:
        customer1 = customers[0]
        customer2 = customers[1]

        customer1.operator_ptr = operators[0]
        customer2.operator_ptr = operators[1]

        customer1.talk(153, customer2)
        customer1.message(269, customer2)
        customer1.connect(750)
        customer1.bill.pay(50)
        customer1.operator_ptr.talking_charge = 0.15
        customer1.limiting_amount = 200

        customer2.talk(254, customer1)
        customer2.message(294, customer1)
        customer2.connect(600)
        customer2.bill.pay(30)
        customer2.operator_ptr.talking_charge = 0.18
        customer2.limiting_amount = 300
    else:
        print("Error: There should be at least two customers in the JSON data.")

if __name__ == "__main__":
    main()
