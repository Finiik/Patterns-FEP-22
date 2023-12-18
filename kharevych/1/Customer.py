
from Bill import Bill
import uuid


class Customer:
    def __init__(self, name, age, limiting_amount):
        self.ID = uuid.uuid4()
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