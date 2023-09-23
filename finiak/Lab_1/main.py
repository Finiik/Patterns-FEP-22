from operators import Operator
from bill import Bill
from customers import Customer

operators = { #словник операторів з параметрами
    "Kyivstar": Operator(0, 0.5, 0.3, 0.01, 20),
    "Vodafone": Operator(1, 0.3, 0.4, 0.03, 15)
}

bills = { #словник з ключами операторів (імена) та лімітами
    "Kyivstar": Bill(200),
    "Vodafone": Bill(175)
}

cust1 = Customer(0, "Tyler", "Josheph", 37, operators, bills, 1500)
cust1.op_name = "Kyivstar"

cust2 = Customer(1, "Joshua", "Dun", 25, operators, bills, 1300)
cust2.op_name = "Vodafone"

cust3 = Customer(2, "Corey", "Taylor", 70, operators, bills, 1000)
cust3.op_name = "Kyivstar"

cust1.talk(30, cust2)
cust2.message(10, cust3)
cust3.talk(10, cust1)
cust2.connect(378)
cust1.pay_bills("Kyivstar", 140)
cust1.change_operator("Vodafone")
cust3.pay_bills("Kyivstar", 50)
cust2.change_limit(175, "Vodafone")
