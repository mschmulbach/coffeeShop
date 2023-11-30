class ShoppingCart:
    def __init__(self) -> None:
        """Initializes the ShoppingCart with an empty dictionary to store items."""
        self.items: dict[str, int] = {}

    def add_item(self, item: str, quantity: int) -> None:
        """
        Adds an item to the cart or updates its quantity.

        Args:
            item (str): The name of the item to add or update.
            quantity (int): The quantity of the item. If zero or negative, the item is removed.
        """
        if quantity > 0:
            self.items[item] = quantity
        elif item in self.items:
            del self.items[item]

    def get_items(self) -> dict[str, int]:
        """
        Returns a dictionary of all items in the cart.

        Returns:
            dict[str, int]: A dictionary where keys are item names and values are quantities.
        """
        return self.items

    def clear_cart(self) -> None:
        """Clears all items from the shopping cart."""
        self.items.clear()

    def update_item(self, item: str, quantity: int) -> None:
        """
        Updates the quantity of a specific item or removes it if the quantity is zero or negative.

        Args:
            item (str): The name of the item to update.
            quantity (int): The new quantity of the item.
        """
        if quantity > 0:
            self.items[item] = quantity
        elif item in self.items:
            del self.items[item]

    def get_quantity(self, item: str) -> int:
        """
        Returns the quantity of a specific item in the cart.

        Args:
            item (str): The name of the item to check.

        Returns:
            int: The quantity of the item. Returns 0 if the item is not in the cart.
        """
        return self.items.get(item, 0)