from models.product import Product

class Store:
    """Manage the store's product list."""
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, name: str, price: float, stock: int) -> Product:
        """Validate and add a new product."""
        name = name.strip()
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        if self.find_product(name) is not None:
            raise ValueError("A product with that name already exists.")
        product = Product(name, price, stock)
        self.products.append(product)
        return product

    def list_products(self) -> None:
        """Print all products."""
        if not self.products:
            print("There are no products in the store yet.")
            return
        print("\n--- Store Products ---")
        for product in self.products:
            print(product.display_info())

    def find_product(self, name: str) -> Product | None:
        """Find a product by name, ignoring letter case."""
        for product in self.products:
            if product.name.lower() == name.strip().lower():
                return product
        return None
