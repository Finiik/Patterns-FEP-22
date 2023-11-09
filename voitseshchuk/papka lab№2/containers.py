class Container:
    def __init__(self, weight):
        self.weight = weight
        self.ID = None

class BasicContainer(Container):
    def __init__(self, weight):
        super().__init__(weight)
        self.ID = None

class HeavyContainer(Container):
    def __init__(self, weight, special_type):
        super().__init__(weight)
        self.special_type = special_type
        self.ID = None
