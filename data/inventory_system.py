from custom_exceptions import InventoryFullError, ItemNotFoundError


class Inventory:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = []

    def add_item(self, item):
        if len(self.items) >= self.max_size:
            raise InventoryFullError("Inventory is full.")
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            raise ItemNotFoundError(f"Item '{item}' not found.")
        self.items.remove(item)

    def list_items(self):
        return self.items
