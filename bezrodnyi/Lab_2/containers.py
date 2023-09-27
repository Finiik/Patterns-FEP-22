# У класі BasicContainer додайте атрибут container_type та присвойте йому відповідне значення
class BasicContainer:
    def __init__(self, container_id, weight):
        self.container_id = container_id
        self.weight = weight
        self.container_type = "Basic"  # Додайте цей атрибут та присвойте йому значення "Basic"

# У класі HeavyContainer також додайте атрибут container_type
class HeavyContainer:
    def __init__(self, container_id, weight, container_type):
        self.container_id = container_id
        self.weight = weight
        self.container_type = container_type  # Присвойте значення container_type при створенні об'єкту