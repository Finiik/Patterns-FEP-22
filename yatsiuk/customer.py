"""Implements Customer class

class Customer
"""

from __future__ import annotations
from typing import Dict, Optional
import uuid

from operators import Operator
from bill import Bill


class Customer:
    """Holds Customer details"""

    def __init__(self, operators: Dict[Operator] = None, bills: Dict[Bill] = None,
                 first_name: str = "test", second_name: str = "test",
                 age: int = 0,discount_rate: float  = 0 ) -> None:
        self.id = uuid.uuid4()
        self._first_name = first_name
        self.second_name = second_name
        self.age = age
        self.operators = operators
        self.bills = self._generate_bills()
        self.discount_rate = discount_rate

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

    def talk(self, minutes: int, customer: Customer, operator_id: int) -> None:
        operator = self.operators[operator_id]
        cost = operator.calc_talking_charge(minutes)
        
        if self.discount_rate > 0:
            cost -= cost * self.discount_rate

        bill = self.bills[operator_id]
        bill.add(debt=cost)
        print(f"Customer {self.first_name} talked to {customer.first_name} for {minutes} minute(s)")

    def message(self,  quantity: float, customer: Customer, operator_id: int ):
        operator = self.operators[operator_id]
        cost = operator.calc_message_cost(quantity) 
        
        if self.discount_rate > 0:
            cost -= cost * self.discount_rate

        bill = self.bills[operator_id]
        bill.add(cost)
        print(f"Customer {self.first_name} sent to {customer.first_name} {quantity} message(s)")

    def connect(self, traffic: float,  customer: Customer, operator_id: int):
        operator = self.operators[operator_id]
        cost = operator.calc_network_charge(traffic)
        
        if self.discount_rate > 0:
            cost -= cost * self.discount_rate

        bill = self.bills[operator_id]
        bill.add(cost)
        print(f"Customer {self.first_name} talked to customer {customer.first_name} spending {traffic} MB")
        pass

    def change_limit(self, value: float, operator_id: int) -> None:
        bill = self.bills[operator_id]
        bill.change_limit(value)
