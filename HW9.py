# HW9.py
# Author: Dylan Nhan

# This homework will expand upon the code for Lab12.py. If you did not complete Lab12.py, you should do so before attempting this homework.

# Copy the code from Lab12.py into this file 1-13. I'll add some comments to help you out.


### INSERT CODE FROM LAB12.PY HERE 1-13###
class Product:
    """
    Product class that has a name, price, and product_id.
    """

    def __init__(self, name: str, price: float, product_id: int) -> None:
        self.name = name
        self.price = price
        self.product_id = product_id

def __str__(self) -> str:
        return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}"

class Customer:
    def __init__(self, name: str, customer_id: int) -> None:
        self.name = name
        self.customer_id = customer_id
        self.cart = []

    def __str__(self) -> str:
        return f"Customer: {self.name}, ID: {self.customer_id}"

def add_to_cart(self, product: Product) -> None:
        """"Add a product to the cart list.

        Args:
            product (Product): Product to add
        """
        self.cart.append(product)
        print(f"{product.name} was added to {self.name}'s cart.")

def remove_from_cart(self, product: Product) -> None:
        """Remove a product from the cart list.

        Args:
            product (Product): Product to remove
        """
        self.cart.remove(product)
        print(f"{product.name} was removed from {self.name}'s cart.")

def checkout(self) -> None:
        """Calculate the total price of all the products in the cart and print out the total. Empty the cart after printing out the total.
        """
        total = 0
        for product in self.cart:
            total += product.price
        print(f"{self.name}'s total is: {total}")
        self.cart = []

def display_products(self) -> None:
        """Print out all the products in the cart list.
        """
        for product in self.cart:
            print(product)

def print_products_pretty(self):
        """Print out all the products in the cart list using tabulate.
        """
        from tabulate import tabulate
        
        print(f"{self.name}'s Cart:")
        print(tabulate(
              [
                    {
                          "Name": product.name,
                          "Price": product.price,
                          "ID": product.product_id
                    }
                    for product in self.cart
                ],
                headers="keys",
                tablefmt="fancy_grid"
             )
        )

class Store:
      """Store class that has products and cutomers."""
      def __init__(self) -> None:
          self.products = []
          self.customers = []

def add_product(self, product: Product) -> None:
        """Add a product to the products list.

        Args:
            product (Product): Product to add
        """
        self.products.append(product)
        print(f"{product.name} was added to the store.")

def add_customer(self, customer: Customer) -> None:
        """Add a customer to the customers list.

        Args:
            customer (Customer): Customer to add
        """
        self.customers.append(customer)
        print(f"{customer} was added to the store.")

def display_products(self) -> None:
        """Print out all the products in the products list.
        """
        for product in self.products:
            print(product)

def display_customers(self) -> None:
        """Print out all the customers in the customers list.
        """
        for customer in self.customers:
            print(customer)
### END CODE FROM LAB12.PY ###

# START OF HOMEWORK Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def add_product_to_customer_cart(customer: Customer, product: Product) -> None:
    """Add a product to a customer's cart.

    Args:
        customer (Customer): Customer to add product to
        product (Product): Product to add
    """
    customer.add_to_cart(product)
    print(f"{product.name} was added to {customer.name}'s cart.")

# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def remove_product_from_customer_cart(customer: Customer, product: Product) -> None:
    """Remove a product from a customer's cart.

    Args:
        customer (Customer): Customer to remove product from
        product (Product): Product to remove
    """
    customer.remove_from_cart(product)
    print(f"{product.name} was removed from {customer.name}'s cart.")

# 3. Create a menu function that will display the following menu:
# 1. Add Product
# 2. Add Customer
# 3. Add Product to Customer's Cart
# 4. Remove Product from Customer's Cart
# 5. Display Products
# 6. Display Customers
# 7. Display Customer's Cart
# 8. Checkout
# 9. Exit
def menu() -> int: 
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Add Product to Customer's Cart")
    print("4. Remove Product from Customer's Cart")
    print("5. Display Products")
    print("6. Display Customers")
    print("7. Display Customer's Cart")
    print("8. Checkout")
    print("9. Exit")

    choice = int(input("Enter your choice: "))
    return choice
# The menu function should return the user's choice as an integer.
# Hint: Print out the menu and then use the input() function to get the user's choice.

# 4. Create a main function that will call the menu function and then call the appropriate methods based on the user's choice. The main function should be in a while loop that will continue to call the menu function until the user enters 0 to exit the program.
# IMPORTANT: The main function should create a Store object and then call the appropriate methods on the Store object. Without the Store object, you will not be able to add products or customers.
# IE main function should look something like this:
# def main():
#     store = Store()
#     while True:
#         choice = menu()
#         if choice == 1:
#             # call add_product method
#         elif choice == 2:
#             # call add_customer method
#         elif choice == 3:
#             # call add_product_to_customer_cart method
# ETC...

# Hint 1: If you need informtation from the user about a product or customer, you can ask for it in the main function and then pass it to the appropriate method. Don't be afraid to use input() in the main function.
# Hint 2: Some of the methods take in a Product object or a Customer object. You will need to create a Product object or a Customer object before calling the method. You can create a Product object or a Customer object in the main function and then pass it to the appropriate method.
# Hint 3: You can use the display_products and display_customers methods to help you out.
# Hint 4: Some Methods take in parameters. You will need to pass in the correct parameters to the method. For example, the add_product method takes in a Product object. You will need to pass in a Product object to the method. You can pass in a Product as a parameter.
# IE. store.add_product(product) where product is a Product object.
# store.add_product(Product(name, price, product_id))
# You can either ask the user for the name, price, and product_id or you can hard code it in the main function.
def main():
    store = Store()
    while True:
        choice = menu()
        if choice == 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            product_id = int(input("Enter product ID: "))
            product = Product(name, price, product_id)
            store.add_product(product)
        elif choice == 2:
            name = input("Enter customer name: ")
            customer_id = int(input("Enter customer ID: "))
            customer = Customer(name, customer_id)
            store.add_customer(customer)
        elif choice == 3:
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            customer = store.customers[customer_id]
            product = store.products[product_id]
            add_product_to_customer_cart(customer, product)
        elif choice == 4:
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            customer = store.customers[customer_id]
            product = store.products[product_id]
            remove_product_from_customer_cart(customer, product)
        elif choice == 5:
            store.display_products()
        elif choice == 6:
            store.display_customers()
        elif choice == 7:
            customer_id = int(input("Enter customer ID: "))
            customer = store.customers[customer_id]
            customer.display_products()
        elif choice == 8:
            customer_id = int(input("Enter customer ID: "))
            customer = store.customers[customer_id]
            customer.checkout()
        elif choice == 9:
            break

if __name__ == "__main__":
    """
    Leave this code at the bottom of the file. It will call the main function when you run the file.
    """

    main()