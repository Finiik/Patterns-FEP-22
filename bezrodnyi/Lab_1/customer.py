"""Implements Customer class

class Customer
"""

from __future__ import annotations
from typing import Dict, Optional
import uuid

from pydantic import BaseModel

from operators import Operator
from bill import Bill


class Customer:
    """Holds Customer details"""

    def __init__(self, operators: Dict[Operator] = None, bills: Dict[Bill] = None,
                 first_name: str = "test", second_name: str = "test",
                 age: int = 0) -> None:
        self.id = uuid.uuid4()
        self._first_name = first_name
        self.second_name = second_name
        self.age = age
        # operators = {"operators_id": operator_object, ...}
        self.operators = operators
        # bills = {"operators_id": bill_object, ...}
        self.bills = self._generate_bills()

    def _generate_bills(self) -> dict:
        bills = {}
        for operator_id, operator in self.operators.items():
            bills[operator_id] = operator.create_bill(customer_id=self.id)
        return bills

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"Provided name {value} is not of string type")
        self._first_name = value

    def talk(self, minutes: int, customer: Customer, operator_name: str) -> None:
        # TODO: using operator, calculate talk rate
        # operator = self.operators[operator_name]
        # cost = operator.calc_talking_cost(duration=minutes, customer_1: self, customer: Customer)
        # bill = self.bills[operator_name]
        # bill.add(debt=cost)
        print(f"Customer {self.first_name} talked to {customer.first_name} {minutes}")

    def message(self, quantity: float, customer: Customer, operator_name):
        # TODO: using operator, calculate message cost
        # operator = self.operators[operator_name]
        # cost = operator.calc_talking_cost(duration=minutes, customer_1: Self, customer_2: Self)
        # bill = self.bills["operator_name"]
        # bill.add(debt: cost)
        print(f"Customer {self.first_name} chats to {customer.first_name} with cost")

    def connect(self, traffic: float, operator_name):
        # TODO: using operator, calculate network cost
        # operator = self.operators["operator_name"]
        # cost = operator.calc_talking_cost(duration=minutes, customer_1: Self, customer_2: Self)
        # bill = self.bills["operator_name"]
        # bill.add(debt: cost)
        # print(f"Customer {self.first_name} talked to {customer.first_name} {minutes}")
        pass

    def change_limit(self, value: float, operator_name: str) -> None:
        bill = self.bills[operator_name]
        bill.change_limit(value)


c = Customer()
print(c.id)
