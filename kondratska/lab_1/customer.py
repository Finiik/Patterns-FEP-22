"""Implements Customer class

class Customer
"""
from operators import Operator
from bills import Bill


class Customer:
    """Holds Customer details"""

    def __init__(self, id: int, name: str, age: int, operator: Operator, bill: Bill) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.bill = bill
        self.operator = operator

    def talk(self, minutes: int, customer):
        self.bill.add(self.operator.calculate_talking_cost(minutes, self))
        return f"Customer {self.name} talked to {customer.name} {minutes}"

    def message(self, quantity: int, customer):
        self.bill.add(self.operator.calculate_message_cost(quantity, self, customer))
        return f"Customer {self.name} sent {quantity} messages to {customer.name}"

    def connect(self, traffic: float):
        self.bill.add(self.operator.calculate_network_cost(traffic))
        return f"Customer {self.name} used {traffic} MB during their conversation"
