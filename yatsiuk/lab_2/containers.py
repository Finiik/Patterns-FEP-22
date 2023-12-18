class Container:
    def __init__(self, container_id, weight):
        self.container_id = container_id
        self.weight = weight

    def consumption(self):
        pass

    def equals(self, other):
        return self.__class__.__name__ == other.__class__.__name__  \
            and self.container_id == other.container_id and self.weight == other.weight

class BasicContainer(Container):
    def consumption(self):
        return 2.50 * self.weight

class HeavyContainer(Container):
    def consumption(self):
        return 3.00 * self.weight

class RefrigeratedContainer(HeavyContainer):
    def consumption(self):
        return 5.00 * self.weight

class LiquidContainer(HeavyContainer):
    def consumption(self):
        return 4.00 * self.weight
