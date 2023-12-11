from items.item import Item
from items.small import Small
from items.heavy import Heavy
from items.refrigerated import Refrigerated
from items.liquid import Liquid

class ItemFactory:
    def create_item(self, item_type, config):
        if item_type == "Small":
            return Small(config)
        elif item_type == "Heavy":
            return Heavy(config)
        elif item_type == "Refrigerated":
            return Refrigerated(config)
        elif item_type == "Liquid":
            return Liquid(config)
        else:
            return Item(config)
