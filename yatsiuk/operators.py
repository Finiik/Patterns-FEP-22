""""""
from __future__ import annotations
from typing import TYPE_CHECKING

from bill import Bill

if TYPE_CHECKING:
    from customer import Customer


class Operator:
    """Holds operator details"""

    def __init__(self, id_: int, name: str, talking_charge: float,
                 message_cost: float, network_charge: float) -> None:
        self.id = id_
        self.name = name
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        

    @staticmethod
    def create_bill(customer_id: int) -> Bill:
        bill = Bill(customer_id=customer_id)
        return bill

    def calc_talking_charge(self, duration: float) -> float:
        return self.talking_charge * duration

    def calc_message_cost(self, quantity: int) -> float:
        return self.message_cost * quantity
    
    def calc_network_charge(self, data_size: int) -> float:
        return self.network_charge * data_size
