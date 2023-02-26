class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) == self.__capacity:
            return "not enough room in the inventory"

        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items = ', '.join(self.items)
        left_capacity = self.__capacity - len(self.items)
        return f"Items: {items}.\nCapacity left: {left_capacity}"
