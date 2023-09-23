from operators import Operator
from bill import Bill
from customer import Customer

operators = {
    "operator1": Operator(0, 0.1, 0.01, 0.001, 10),
    "operator2": Operator(1, 0.2, 0.02, 0.002, 15)
}

bills = {
    "operator1": Bill(100),
    "operator2": Bill(150)
}

customer1 = Customer(0, "Customer1", "SecondName1", 17, operators, bills, 1000)
customer1.operator_name = "operator1"
customer2 = Customer(1, "Customer2", "SecondName1", 20, operators, bills, 1200)
customer2.operator_name = "operator2"

customer1.talk(30, customer2)
customer2.message(10, customer1)
customer1.connection(500)
customer1.pay_bills("operator1", 50)
customer1.change_operator("operator2")
customer1.change_limit(200, "operator1")
