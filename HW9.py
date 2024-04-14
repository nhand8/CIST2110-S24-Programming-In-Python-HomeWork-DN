# HW9.py
# Author:

# This homework will expand upon the code for Lab12.py. If you did not complete Lab12.py, you should do so before attempting this homework.

# Copy the code from Lab12.py into this file 1-13. I'll add some comments to help you out.


### INSERT CODE FROM LAB12.PY HERE 1-13###

### END CODE FROM LAB12.PY ###

# START OF HOMEWORK Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.


# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.


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
    pass  # remove this line when you start working on the main function


if __name__ == "__main__":
    """
    Leave this code at the bottom of the file. It will call the main function when you run the file.
    """

    main()
