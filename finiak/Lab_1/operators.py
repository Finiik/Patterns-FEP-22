from __future__ import annotations #дозволяє використовувати типи об'єктів заздалегідь визначеними в анотаціях
from typing import TYPE_CHECKING #імпортує модуль TYPE_CHECKING з бібліотеки typing,яка використовується для перевірки 
#типів під час анотації, і далі буде використана для створення зациклених імпортів(циклічних залежностей) між модулями
from bill import Bill
if TYPE_CHECKING:
    from customers import Customer
    
class Operator:
    def __init__(self, oper_id: int, talk_charge: float, mess_cost: float, net_charge: float, discount_rate: int) -> None:
        self.ID = oper_id
        self.talk_charge = talk_charge
        self.mess_cost = mess_cost
        self.net_charge = net_charge
        self.discount_rate = discount_rate
        
    def create_bill(self) -> Bill: #створення об'єктів рахунків
        bill = Bill(op_id=self.ID)
        return bill
    
    def calct_talk(self, minutes: int, customer: Customer) -> float: #перевірка віку для знижки
        if customer.age < 18 or customer.age > 65:
            operator_discount_rate = self.discount_rate
        else:
            operator_discount_rate = 0
            
        cost = minutes * (self.talk_charge * (1 - operator_discount_rate/100)) 
        return cost
    
    def calc_mess(self, quantity: int, customer: Customer, other: Customer) -> float: #перевірка чи мають одинакового оператора
        if customer.operators[customer.op_name] == other.operators[other.op_name]:
            return quantity * self.mess_cost * (1 - self.discount_rate / 100)
        return quantity * self.mess_cost
    
    def calc_net(self, amount: float) -> float: #нічо особливого
        return amount * self.net_charge