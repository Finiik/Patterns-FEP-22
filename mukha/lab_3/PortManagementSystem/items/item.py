class Item:
    def __init__(self, config):
        self.id = config['ID']
        self.weight = config['weight']
        self.count = config['count']
        self.container_id = config['containerID']

    def to_dict(self):
        return {
            'ID': self.id,
            'weight': self.weight,
            'count': self.count,
            'containerID': self.container_id
        }
