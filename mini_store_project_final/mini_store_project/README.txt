MINI STORE MANAGEMENT SYSTEM

How to run:
1. Extract mini_store_project.zip.
2. Open the extracted mini_store_project folder in VS Code.
3. Open main.py and run it in the Terminal.

Manager login:
Username: admin
Password: 1234

Files:
- main.py: starts the program
- cli.py: menus and user input
- store.py: manages products
- models/product.py: Product class
- models/cartitem.py: CartItem class
- models/cart.py: Cart class

Stock decreases when items are added to the cart.
Removing items or leaving without checkout restores stock.
Successful checkout keeps the stock reduction.
