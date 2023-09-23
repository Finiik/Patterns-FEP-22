class Operator:
    """Holds operator details"""

    def __init__(self, id_: int, talking_charge: float,
                 message_cost: float, network_charge: float,
                 discount_rate: int) -> None:
        self.id = id_
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    def calculate_talking_cost(self, minute: float, customer):
        # calculates talking cost including discounts
        talking_cost = minute * self.talking_charge
        if 18 > customer.age < 65:
            talking_cost -= talking_cost * self.discount_rate
        return talking_cost

    def calculate_message_cost(self, quantity: int, customer, other_customer):
        # calculates talking cost including discounts
        total_message_cost = quantity * self.message_cost
        if customer.operators == other_customer.operators:
            total_message_cost -= total_message_cost * self.discount_rate
        return total_message_cost

    def calculate_network_cost(self, amount: float):
        # calculates networking cost
        return amount * self.network_charge
