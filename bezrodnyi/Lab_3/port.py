class Port:
    def __init__(self, Name, Coordinates):
        self.Name = Name
        self.Coordinates = Coordinates
        self.containers = []

    def loadContainers(self, containers):
        self.containers.extend(containers)

    def unloadContainers(self, ship):
        unloaded_containers = []
        for item in ship.items:
            if item.containerID in [container.ID for container in self.containers]:
                unloaded_containers.append(item)
        self.containers = [container for container in self.containers if container.ID not in [item.containerID for item in unloaded_containers]]
        return unloaded_containers
