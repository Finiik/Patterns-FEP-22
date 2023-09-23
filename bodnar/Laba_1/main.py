from operators import Operator
from bill import Bill
from customer import Customer

operators = {
    "lifecell": Operator(0, 0.1, 0.01, 0.001, 10),
    "kyivstar": Operator(1, 0.2, 0.02, 0.002, 15)
}
bills = {
    "lifecell": Bill(100),
    "kyivstar": Bill(150)
}
customer1 = Customer(0, "Kiara", "Johnson", 25, operators, bills, 1000)
customer1.operator_name = "lifecell"
customer2 = Customer(1, "Henry", "Mikaelson", 20, operators, bills, 1200)
customer2.operator_name = "kyivstar"

customer1.talk(30, customer2)
customer2.message(10, customer1)
customer1.connection(1769)
customer1.pay_bills("lifecell", 150)
customer1.change_operator("kyivstar")
customer1.change_limit(200, "lifecell")
