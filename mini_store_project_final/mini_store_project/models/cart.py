from models.cartitem import CartItem
from models.product import Product

class Cart:
    """Manage cart items and synchronize product stock."""
    def __init__(self) -> None:
        self.items: list[CartItem] = []

    def add_to_cart(self, product: Product, quantity: int) -> None:
        """Add items to the cart and reduce available stock."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > product.stock:
            raise ValueError(f"Not enough stock. Available quantity: {product.stock}")

        existing_item = None
        for item in self.items:
            if item.product is product:
                existing_item = item
                break
        if existing_item is None:
            self.items.append(CartItem(product, quantity))
        else:
            existing_item.quantity += quantity
        product.stock -= quantity

    def remove_from_cart(self, product_name: str) -> None:
        """Remove a product and return its quantity to stock."""
        for item in self.items:
            if item.product.name.lower() == product_name.strip().lower():
                item.product.stock += item.quantity
                self.items.remove(item)
                return
        raise ValueError("That product is not in the cart.")

    def view_cart(self) -> None:
        """Print cart items and the total."""
        if not self.items:
            print("Your cart is empty.")
            return
        print("\n--- Your Cart ---")
        for item in self.items:
            print(item)
        print(f"Total: ${self.total_price():.2f}")

    def total_price(self) -> float:
        """Calculate the total price of the cart."""
        total = 0.0
        for item in self.items:
            total += item.subtotal()
        return total

    def finish_checkout(self) -> None:
        """Clear the cart after checkout without restoring stock."""
        self.items.clear()

    def return_items_to_stock(self) -> None:
        """Restore stock if the customer leaves without checkout."""
        for item in self.items:
            item.product.stock += item.quantity
        self.items.clear()
