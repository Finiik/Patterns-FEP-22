from __future__ import annotations
from typing import Dict
from operators import Operator
from bill import Bill


class Customer:
    """Holds Customer details"""
    def __init__(self, _id: int, first_name: str, second_name: str, age: int,
                 operators: Dict[str, Operator], bills: Dict[str, Bill], limiting_amount: float) -> None:
        self.id = _id
        self._first_name = first_name
        self.second_name = second_name
        self.age = age
        self.operators = operators
        self.bills = self._generate_bill()
        self.limiting_amount = limiting_amount
        self.operator_name = None

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"Provided name {value} is not of string type")
        self._first_name = value

    def _generate_bill(self):
        bills = {}
        for operator_id, operator in self.operators.items():
            bills[operator_id] = operator.create_bill()
        return bills
    def talk(self, minutes: int, other: Customer) -> None:
        operator = self.operators[self.operator_name]
        cost = operator.calculate_talking_cost(minutes, self)
        if self.check_limit(cost):
            self.bills[self.operator_name].add(cost)
        print(f"{self.first_name} talked to {other.first_name} for {minutes} minutes.")

    def message(self, quantity: int, other: Customer) -> None:
        if self.operators[self.operator_name] == other.operators[other.operator_name]:
            operator_discount_rate = self.operators[self.operator_name].discount_rate
            cost = quantity * self.operators[self.operator_name].message_cost * (1 - operator_discount_rate / 100)
        else:
            cost = quantity * self.operators[self.operator_name].message_cost

        if self.check_limit(cost):
            self.bills[self.operator_name].add(cost)
        print(f"{self.first_name} sent {quantity} messages to {other.first_name}.")

    def connection(self, amount: float) -> None:
        cost = amount * self.operators[self.operator_name].network_charge
        if self.check_limit(cost):
            self.bills[self.operator_name].add(cost)
            print(f"{self.first_name} used {amount} MB of data.")

    def pay_bills(self, operator_name: str, amount: float) -> None:
        self.bills[operator_name].pay(amount)
        print(f"{self.first_name} paid {amount} for the {operator_name} bill.")

    def change_operator(self, new_operator_name: str) -> None:
        self.operator_name = new_operator_name
        print(f"{self.first_name} changed the operator to {new_operator_name}.")

    def change_limit(self, new_limit: float, operator_name: str) -> None:
        self.bills[operator_name].change_limit(new_limit)
        print(f"{self.first_name} changed the {operator_name} bill limit to {new_limit}.")

    def check_limit(self, cost: float) -> bool:
        return self.bills[self.operator_name].check(cost)

