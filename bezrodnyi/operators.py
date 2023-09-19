""""""
from __future__ import annotations
from typing import TYPE_CHECKING

from bill import Bill

if TYPE_CHECKING:
    from customer import Customer


class Operator:
    """Holds operator details"""

    def __init__(self, id_: int, name: str, talking_charge: float,
                 message_cost: float, network_charge: float,
                 discount_rate: int) -> None:
        self.id = id_
        self.name = name
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    @staticmethod
    def create_bill(limit: float, customer_id: int) -> Bill:
        bill = Bill(limit=limit, customer_id=customer_id)
        return bill

    def calc_talking_charge(self, duration: float,
                            customer_1: Customer,
                            customer_2: Customer) -> float:
        pass

    def calc_message_cost(self):
        pass
