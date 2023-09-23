from operators import Operator
from customer import Customer
from uuid import uuid4


operators_ = {i: Operator(id_=i, name=f"oper_{i}", talking_charge=10,
                       message_cost=20, network_charge=5)
    for i in range(2)
}

customers_ = [Customer(first_name=f"test_name{i}",
                       age=i+20, second_name=f"second_name{i}",
                       operators=operators_)
    for i in range(2)
]

if __name__ == '__main__':
    customer =  customers_[0]
    companion =  customers_[1]
    operator =  operators_[0]

    customer.talk(1,companion,0)
    customer.message(1,companion,0)
    customer.connect(1,companion,0)
    # all done