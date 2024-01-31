# HW1.py
# Author: Dylan Nhan

# Question 1:
# Print Hello World like we did in class
print("Hello World")
# Question 2:
# Print the following:
# Your name
name = "Dylan Nhan"
print(name)
# Your age
age = 20
print(age)
# Your favorite color
fav_color = "Blue"
print(fav_color)
# Your favorite animal
fav_animal = "Crocodile"
print(fav_animal)
# Question 3:
# Create a variable called "myName" and set it equal to your name
myName = "Dylan Nhan"
# Create a variable called "myAge" and set it equal to your age
myAge = 20
# Create a variable called "myColor" and set it equal to your favorite color
myColor = "Blue"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "Crocodile"
# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>
print("Hello, my name is " + myName)
print("I am " + str(myAge) + " years old")
print("My favorite color is " + myColor)
print("My favorite animal is a " + myAnimal)
# Question 4:
# Calculate the following and print the result:
# 2 + 2
print(2 + 2)
# 3 * 4
print(3 * 4)
# 5 - 6
print(5 - 6)
# 8 / 2
print(8 / 2)
# Question 5:
# Create a variable called "num1" and set it equal to 2
num1 = 2
# Create a variable called "num2" and set it equal to 3
num2 = 3
# Create a variable called "num3" and set it equal to 4
num3 = 4
# Create a variable called "num4" and set it equal to 5
num4 = 5
# Calculate the following and print the result:
# num1 + num2
print(num1 + num2)
# num3 * num4
print(num3 * num4)
# num4 - num1
print(num4 - num1)
# num2 / num1
print(num2 / num1)
# Question 6: Write a program that asks the user for their name and then prints the following:
name = input("What is your name? ")
# Hello, <name>. Please enter three numbers.
# The program should then ask the user for three numbers (floats) and print the following:
number1 = float(input("Hello, " + name + ". Can you enter three numbers. Please enter the first number: "))
number2 = float(input("Please enter a second number: "))
number3 = float(input("Please enter a third number: "))
# 1. The sum of the three numbers is <sum>
sum = (number1 + number2 + number3)
print("1. The sum of the three numbers is " + str(sum))
# 2. The product of the three numbers is <product>
product = (number1 * number2 * number3)
print("2. The product of the three numbers is " + str(product))
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3
round(number1)
round(number2)
round(number3)
sum_rounded = round(sum / 3)
print("3. Round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3: " + str(sum_rounded))
# 4. The average of the three numbers is <average>
avg = sum / 3
print("4. The average of the three numbers is " + str(avg))
# Question 7: Ask the user for an input of a symbol (in the example its *)
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character.
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.
#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
symbol = str(input("Please enter a symbol: "))
print("| " + "\t   " + symbol +   "\t      |")
print("| " + "\t  " + symbol * 3 +   "\t      |")
print("| " + "\t " + symbol * 5 +   "\t      |")
print("| " + "\t" + symbol * 7 +   "\t      |")
print("| " + "\t " + symbol * 5 +   "\t      |")
print("| " + "\t  " + symbol * 3 +   "\t      |")
print("| " + "\t   " + symbol +   "\t      |")