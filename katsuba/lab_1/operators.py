from __future__ import annotations
from typing import TYPE_CHECKING

from bill import Bill

if TYPE_CHECKING:
    from customer import Customer


class Operator:
    """Holds operator details"""

    def __init__(self, _id: int, talking_charge: float, message_cost: float, network_charge: float,
                 discount_rate: int) -> None:
        self.ID = _id
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    def create_bill(self) -> Bill:
        bill = Bill(operator_id=self.ID)
        return bill
    def calculate_talking_cost(self, minutes: int, customer: Customer) -> float:
        if customer.age < 18 or customer.age > 65:
            return minutes * self.talking_charge
        return minutes * self.talking_charge

    def calculate_message_cost(self, quantity: int, customer: Customer, other: Customer) -> float:
        if customer.operators[customer.operator_name] == other.operators[other.operator_name]:
            return quantity * self.message_cost * (1 - self.discount_rate / 100)
        return quantity * self.message_cost

    def calculate_network_cost(self, amount: float) -> float:
        return amount * self.network_charge

