# HW4.py
# Author: Dylan Nhan

### README
# This file contains buggy functions that you need to fix.
# There are 10 buggy functions in total.
# run test.py to see which functions are buggy and what the expected output is.
# remember you can run test.py with the -v flag to see more details about the tests.
# also remember that you can run a specific test by specifying the test name after the -k flag.
# you should not change the test.py file.

# Each function has a comment above it that describes what the function should do.
# Answer each question asking where the bug is in the buggy function.
# Provide your answer as what line the bug is on and what the bug is.
# For example, if the bug is on line 5 and the bug is that the function is missing a colon, you would write:
# 5: Missing colon
# After you fix the function, you should run test.py to make sure that the function is fixed.


def add(a: float, b: float) -> float:
    """Add two numbers together

    Args:
        a (float): number to add
        b (float): number to add

    Returns:
        float: the sum of a and b
    """
    return a + b
print(add(3, 2))
print(add(0, 5))

# Where is the bug in the buggy function?
# A: 30: The function was returning a - b instead of a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers

    Args:
        a (float): number to subtract from
        b (float): number to subtract

    Returns:
        float: the difference of a and b
    """
    return a - b
print(subtract(5, 3))  
print(subtract(3, 5)) 


# Where is the bug in the buggy function?
# A: 47: The function was returning a + b instead of a - b


def divide(a, b):
    """Divide two numbers

    Args:
        a (float): number to divide
        b (float): number to divide by

    Returns:
        float: the quotient of a and b
    """
    return a / b
print(divide(6, 2))
#print(divide(1, 0))

# Where is the bug in the buggy function?
# A: 65: The function was returning a * b instead of a / b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers

    Args:
        a (float): number to multiply
        b (float): number to multiply by

    Returns:
        float: the product of a and b
    """
    return a * b
print(multiply(4, 3))
print(multiply(4, 0))

# Where is the bug in the buggy function?
# A: 82: The function was returning a / b instead of a * b


def greet(name: str) -> str:
    """Greet a person

    Args:
        name (str): name of the person to greet

    Returns:
        _type_: the greeting message
    """
    return "Hello, " + name + "!"
print(greet("John")) 
print(greet("Doe"))  


# Where is the bug in the buggy function?
# A: 102: The function was returning "Heloo, " + name instead of "Hello, " + name + "!"


def square(num: int) -> int:
    """Square a number

    Args:
        num (int): number to square

    Returns:
        int: the square of the number
    """
    return num * num
print(square(4))
print(square(0))


# Where is the bug in the buggy function?
# A: 120: The function was returning num + num instead of num * num


def is_even(num: int) -> bool:
    """Check if a number is even

    Args:
        num (int): number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return num % 2 == 0
print(is_even(4))
print(is_even(3))


# Where is the bug in the buggy function?
# A: 138: The function was returning num % 2 == 1 instead of num % 2 == 0


def grade_calculator(score: float) -> str:
    """Calculate the grade based on the score

    Args:
        score (float): score to calculate the grade for

    Returns:
        str: the grade for the score
    """
    if score > 100 or score < 0:
        return "Invalid Score"
    elif 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid Score"
print(grade_calculator(95))
print(grade_calculator(85)) 
print(grade_calculator(75)) 
print(grade_calculator(79)) 
print(grade_calculator(65)) 
print(grade_calculator(50)) 
print(grade_calculator(105))    
print(grade_calculator(-5))

# Where is the bug in the buggy function?
# A: 160: The function was returning "C" for score < 79 instead of score <= 79 (missing = sign), and missing condition for score < 0 and score > 100

def speed_check(speed: float) -> str:
    """Check if the speed is within the speed limit

    Args:
        speed (float): speed to check

    Returns:
        str: the speed check result
    """
    # Assuming general speed limits: min: 20, max: 70 (in mph)
    if speed < 20:
        return "Too slow"
    elif 20 <= speed <= 70:
        return "Within limit"
    elif speed > 70:
        return "Over speed limit"
    else:
        return "Unknown"
print(speed_check(10))
print(speed_check(50))
print(speed_check(80))
print(speed_check(65))


# Where is the bug in the buggy function?
# A: 194: The function was returning "Within limit" for speed <= 60 instead of speed <= 70


def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year

    Args:
        year (int): year to check

    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False
        else:    
            return True
    else:
        return False
print(is_leap_year(2020))
print(is_leap_year(2021))
print(is_leap_year(2000))
print(is_leap_year(1900))

# Where is the bug in the buggy function?
# A: 220 - 225: The function was incorrectly ordered and needed to be placed right after each condition to check for leap years. 


def main():
    print("You are running me directly!")


if __name__ == "__main__":
    main()
