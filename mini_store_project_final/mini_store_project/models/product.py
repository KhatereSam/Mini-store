class Product:
    """Represent one product available in the store."""
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self) -> str:
        """Return product information as readable text."""
        return f"{self.name} | Price: ${self.price:.2f} | Stock: {self.stock}"

    def __str__(self) -> str:
        """Return a short product description."""
        return self.display_info()
