


class Operator:
    def __init__(self, ID, talking_charge, message_cost, network_charge, discount_rate):
        self.ID = ID
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    def calculate_talking_cost(self, minute, customer):
        cost = minute * self.talking_charge
        if customer.get_age() < 18:
            cost -= cost * (self.discount_rate / 100.0)
        return cost

    def calculate_message_cost(self, quantity, sender, receiver):
        cost = quantity * self.message_cost
        if sender.get_operator().ID == receiver.get_operator().ID:
            cost -= cost * (self.discount_rate / 100.0)
        return cost

    def calculate_network_cost(self, amount):
        return amount * self.network_charge