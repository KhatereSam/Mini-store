from models.product import Product

class CartItem:
    """Represent a product and its quantity in a cart."""
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def subtotal(self) -> float:
        """Calculate this item's total price."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Return a readable cart item description."""
        return f"{self.product.name} x {self.quantity} = ${self.subtotal():.2f}"
