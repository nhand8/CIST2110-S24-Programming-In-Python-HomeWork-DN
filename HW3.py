# HW3.py
# Author: Dylan Nhan

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.
# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
def number_squared(num: int) -> int:
    """Input number and reutrn the number squared

    Args:
        num (int): the number to square

    Returns:
        int: the number squared
    """
    return num**2
user_input = int(input("Please enter a number: "))
input_squared = number_squared(user_input)
print("The number you entered squared is: " + str(input_squared))

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
def replace_letter_index(input_string: str, letter: str, index: int):
    if index < 0 or index >= len(input_string):
        print("Cannot do that")
        return input_string
    else:
        return input_string[:index] + letter + input_string[index + 1:]
user_string = input("Enter a string: ")
user_letter = input("Enter a letter: ")
user_index = int(input("Enter an index: "))

result = replace_letter_index(user_string, user_letter, user_index)
print(result)

# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
def num_within_bounds(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

user_number = int(input("Please enter a number: "))
user_lower_bound = int(input("Please enter the lower bound: "))
user_upper_bound = int(input("Please enter the upper bound: "))

result = num_within_bounds(user_number, user_lower_bound, user_upper_bound)
print("Are the numbers entered within the bounds?: ", result)

# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
def user_info(name: str, age: int, color: str) -> str:
    """Take in a string and an int and return the name, age and favorite color

    Args:
        name (str): name of user
        age (int): age of user
        color (str): favorite color

    Returns:
        str: "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
    """

    return f"Hello, my name is {user_name}. I am {user_age} years old. My favorite color is {user_color}."

# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4
def get_user_info() -> None:
    """asks the user for their name, age, and favorite color and then calls the user_info function
    """

user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))
user_color = input("Please enter your favorite color: ")

information = user_info(user_name, user_age, user_color)

print(information)

get_user_info()

# Question 6:
# import the random module and use it to generate a random number between 1 and 100
import random
def random_number():
    """returns a random number between 1 and 100
    
    Returns:
        int: random number between 1 and 100
    """
    return random.randint(1, 100)

print(random_number())

# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
from math import sqrt

def sqrt_root_num(num: int) -> int:
    """takes in an int and returns the square root of the number(16)

    Args:
        num (int): the number to square root
    
    Returns:
        int: square root of the number
    """
    return sqrt(num)

print(sqrt_root_num(16))

# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys 

print("Python version:", sys.version)

# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
from os import getcwd

current_directory = getcwd()
print("Current working directory:", current_directory)