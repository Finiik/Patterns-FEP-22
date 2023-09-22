import json
from customer import Customer
from operators import Operator
from bills import Bill


with open('operators.json') as file:
    op_data = json.load(file)

Operators = []
for item in op_data['operators']:
    Operators.append(Operator(
        item['id'],
        item['talking_charge'],
        item['message_charge'],
        item['network_charge'],
        item['discount_rate'],
    ))

with open('customers.json') as file:
    cus_data = json.load(file)

with open("bills.json") as bill_info:
    bill_data = json.load(bill_info)

Bills = []
for item in bill_data['bills']:
    Bills.append(Bill(
        item['limit'],
        item['current_debt']
    ))

Customers = []
for item in cus_data["customers"]:
    Customers.append(Customer(
        item["id"],
        item["name"],
        item["age"],
        Operators[item["id"]],
        Bill(item["bill"])))


# Create prints
print(Customers[0].talk(10, Customers[1]))
print(Customers[1].talk(10, Customers[2]))
Customers[0].connect(traffic=50)
