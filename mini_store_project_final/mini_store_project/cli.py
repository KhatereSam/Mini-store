from store import Store
from models.cart import Cart

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def read_number(prompt: str) -> float:
    """Keep asking until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def read_integer(prompt: str) -> int:
    """Keep asking until a whole number is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def manager_menu(store: Store) -> None:
    """Log in and manage store products."""
    username = input("Username: ").strip()
    password = input("Password: ")
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        print("Login failed. Incorrect username or password.")
        return
    print("Login successful!")
    while True:
        print("\n--- Store Manager ---")
        print("1. Add product")
        print("2. List products")
        print("3. Return to main menu")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            name = input("Product name (or 'done' to cancel): ").strip()
            if name.lower() == "done":
                continue
            price = read_number("Product price: $")
            stock = read_integer("Product stock: ")
            try:
                store.add_product(name, price, stock)
                print("Product added successfully.")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            store.list_products()
        elif choice == "3":
            return
        else:
            print("Invalid menu choice. Please choose 1, 2, or 3.")

def customer_menu(store: Store) -> None:
    """Let a customer use a cart and check out."""
    cart = Cart()
    while True:
        print("\n--- Customer Menu ---")
        print("1. View products")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Return to main menu")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            store.list_products()
        elif choice == "2":
            product = store.find_product(input("Product name: ").strip())
            if product is None:
                print("Product not found.")
                continue
            quantity = read_integer("Quantity: ")
            try:
                cart.add_to_cart(product, quantity)
                print("Item added to cart.")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "3":
            try:
                cart.remove_from_cart(input("Product name to remove: ").strip())
                print("Item removed. Its stock has been returned.")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "4":
            cart.view_cart()
        elif choice == "5":
            if not cart.items:
                print("Your cart is empty. Add an item before checkout.")
                continue
            cart.view_cart()
            confirmation = input("Confirm checkout? (yes/no): ").strip().lower()
            if confirmation == "yes":
                total = cart.total_price()
                cart.finish_checkout()
                print(f"Checkout complete. Total paid: ${total:.2f}")
                print("Thank you for shopping!")
                return
            print("Checkout cancelled. Your cart has not changed.")
        elif choice == "6":
            cart.return_items_to_stock()
            return
        else:
            print("Invalid menu choice. Please choose a number from 1 to 6.")

def run_cli() -> None:
    """Run the main menu until the user exits."""
    store = Store()
    while True:
        print("\n====== MINI STORE ======")
        print("1. Store Manager")
        print("2. Customer")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            manager_menu(store)
        elif choice == "2":
            customer_menu(store)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Please choose 1, 2, or 3.")
