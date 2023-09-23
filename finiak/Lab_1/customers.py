from __future__ import annotations
from typing import Dict
from operators import Operator
from bill import Bill


class Customer:
    def __init__(self, cust_id: int, first_name: str, second_name: str, age: int, operators: Dict[str, Operator], bills: Dict[str, Bill], limit: float) -> None:
        self.cust_id = cust_id
        self._first_name = first_name
        self.second_name = second_name
        self.age = age
        self.operators = operators
        self.bills = self.generate_bill()
        self.limit = limit
        self.op_name = None
        
    @property #цей декоратор вказує, що метод first_name є властивістю (property) об'єкта класу
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"Provided name {value} is not of string type") #f спосіб форматує рядок, для кращої читабельності і швидкості виконання
        self._first_name = value
        
    def generate_bill(self):
        bills = {}
        for oper_id, operator in self.operators.items():
            bills[oper_id] = operator.create_bill()
        return bills
    
    def talk(self, minutes: int, other: Customer) -> None:
        operator = self.operators[self.op_name]
        cost = operator.calct_talk(minutes, self)
        if self.check_limit(cost):
            self.bills[self.op_name].add(cost)
        print(f"{self._first_name} talked to {other.first_name} for {minutes} minutes.")
        
    def message(self, quantity: int, other: Customer) -> None:
        if self.operators[self.op_name] == other.operators[other.op_name]:
            operator_discount_rate = self.operators[self.op_name].discount_rate
            cost = quantity * self.operators[self.op_name].mess_cost
        else:
            cost = quantity * self.operators[self.op_name].mess_cost
            
        if self.check_limit(cost):
            self.bills[self.op_name].add(cost)
        print(f"{self.first_name} sent {quantity} messages to {other.first_name}.")
        
    def connect(self, traffic: float) -> None:
        cost = traffic * self.operators[self.op_name].net_charge
        if self.check_limit(cost):
            self.bills[self.op_name].addDebt(cost)
            print(f"{self.first_name} used {traffic} MB of data.")
            
    def pay_bills(self, op_name: str, amount: float) -> None:
        self.bills[op_name].payDebt(amount)
        print(f"{self.first_name} paid {amount} for the {op_name} bill.")
        
    def change_operator(self, new_op_name: str) -> None:
        self.op_name = new_op_name
        print(f"{self.first_name} changed the operator to {new_op_name}.")
        
    def change_limit(self, new_lim: float, op_name: str) -> None:
        self.bills[op_name].change_lim(new_lim)
        print(f"{self.first_name} changed the {op_name} bill limit to {new_lim}.")
        
    def check_limit(self, cost: float) -> bool:
        return self.bills[self.op_name].checkDebt(cost)