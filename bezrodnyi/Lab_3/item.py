class Item:
    def __init__(self, ID, weight, count, containerID):
        self.ID = ID
        self.weight = weight
        self.count = count
        self.containerID = containerID

    def getTotalWeight(self):
        return self.weight * self.count

class Small(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Small"

class Heavy(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Heavy"

class Refrigerated(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Refrigerated"

class Liquid(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)
        self.item_type = "Liquid"
