from PyQt6 import QtWidgets
import sys
from coffee_shop_menu import Ui_Menu
from order_summary import Ui_orderSummary
from shopping_cart import ShoppingCart


class CoffeeShopMenu(QtWidgets.QWidget, Ui_Menu):
    def __init__(self, cart: ShoppingCart) -> None:
        """
        Initialize the coffee shop menu with a given shopping cart.

        Args:
            cart (ShoppingCart): The shopping cart instance to be used with the menu.
        """
        super().__init__()
        self.setupUi(self)
        self.cart = cart
        self.addToCartButton.clicked.connect(self.add_to_cart)
        self.update_spin_boxes()

    def add_to_cart(self) -> None:
        """Adds items to the cart based on the SpinBox values and updates the order summary window."""
        self.cart.add_item("Espresso", self.espressoSpinBox.value())
        self.cart.add_item("Americano", self.americanoSpinBox.value())
        self.cart.add_item("Cappuccino", self.cappuccinoSpinBox.value())
        self.cart.add_item("Mocha", self.mochaSpinBox.value())
        self.cart.add_item("Cafe Latte", self.cafeLatteSpinBox.value())

        # Check if an OrderSummary window already exists
        if hasattr(self, 'summary_window') and self.summary_window.isVisible():
            self.summary_window.update_order_summary()
        else:
            self.summary_window = OrderSummary(self.cart, self)
            self.summary_window.show()
        self.hide()

    def update_spin_boxes(self) -> None:
        """Updates the SpinBoxes to reflect the current quantities in the shopping cart."""
        self.espressoSpinBox.setValue(self.cart.get_quantity("Espresso"))
        self.americanoSpinBox.setValue(self.cart.get_quantity("Americano"))
        self.cappuccinoSpinBox.setValue(self.cart.get_quantity("Cappuccino"))
        self.mochaSpinBox.setValue(self.cart.get_quantity("Mocha"))
        self.cafeLatteSpinBox.setValue(self.cart.get_quantity("Cafe Latte"))


class OrderSummary(QtWidgets.QWidget, Ui_orderSummary):
    def __init__(self, cart: ShoppingCart, menu_window: CoffeeShopMenu) -> None:
        """
        Initialize the order summary window with a shopping cart and a reference to the menu window.

        Args:
            cart (ShoppingCart): The shopping cart instance containing the order items.
            menu_window (CoffeeShopMenu): The menu window instance to return to from the order summary.
        """
        super().__init__()
        self.setupUi(self)
        self.cart = cart
        self.menu_window = menu_window
        self.populate_order_summary()
        self.confirmationLabel.setVisible(False)
        self.confirmOrderButton.clicked.connect(self.confirm_order)
        self.backToMenuButton.clicked.connect(self.back_to_menu)

    def update_order_summary(self) -> None:
        """Updates the order summary label with the current items in the cart."""
        self.orderSummaryLabel.clear()
        self.populate_order_summary()

    def populate_order_summary(self) -> None:
        """Populates the order summary label with the items and total amount from the shopping cart."""
        summary_text = self.generate_summary_text()
        self.orderSummaryLabel.setText(summary_text)

    def generate_summary_text(self) -> str:
        """
        Generates a summary text of the current items in the shopping cart.

        Returns:
            str: A formatted string of the order summary.
        """
        summary_text = ""
        total_amount = 0
        for item, quantity in self.cart.get_items().items():
            if quantity > 0:
                price = self.find_item_price(item)
                total_amount += price * quantity
                summary_text += f"{item} x{quantity} @ ${price:.2f} each\n"
        summary_text += f"\nTotal: ${total_amount:.2f}"
        return summary_text

    def find_item_price(self, item_name: str) -> int:
        """
        Finds the price of a given item.

        Args:
            item_name (str): The name of the item.

        Returns:
            int: The price of the item.
        """
        item_prices = {"Espresso": 3, "Americano": 5, "Cappuccino": 6, "Mocha": 7, "Cafe Latte": 7}
        return item_prices.get(item_name, 0)

    def back_to_menu(self) -> None:
        """Hides the order summary and shows the coffee shop menu."""
        self.hide()
        self.menu_window.update_spin_boxes()
        self.menu_window.show()

    def confirm_order(self) -> None:
        """Confirms the order and displays a confirmation message."""
        self.confirmationLabel.setText("Order confirmed, it will be ready shortly. Thank you for shopping with us!")
        self.confirmationLabel.setVisible(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cart = ShoppingCart()
    mainWindow = CoffeeShopMenu(cart)
    mainWindow.show()
    sys.exit(app.exec())
