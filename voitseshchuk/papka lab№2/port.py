class Port:
    def __init__(self, ID, latitude, longitude):
        self.ID = ID
        self.coordinates = (latitude, longitude)
        self.storage = []

    def load_container(self, container):
        # Додати логіку для завантаження контейнера в порт
        pass

    def unload_container(self, container):
        # Додати логіку для розвантаження контейнера з порту
        pass

    def find_closest_refueling_port(self):
        # Додати логіку для пошуку найближчого порту для підйому палива
        pass
