class Containers:
    def __init__(self, ID, weight, count, containerID):
        self.ID = ID
        self.weight = weight
        self.count = count
        self.containerID = containerID

    def getTotalWeight(self):
        return self.weight * self.count

class ItemDecorator(Containers):
    def __init__(self, item, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item = item

    def getTotalWeight(self):
        return self.weight * self.count + self.item.getTotalWeight()

class Small(Containers):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Small"

class Heavy(Containers):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Heavy"

class Refrigerated(Containers):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Refrigerated"

class Liquid(Containers):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Liquid"
