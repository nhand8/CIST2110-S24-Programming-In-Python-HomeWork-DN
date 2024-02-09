# HW2.py
# Author: Dylan Nhan

# Question 1:
# Write some code that prompts the user for their age. Depending on the input:
# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."
user_age = int(input("What is your age?: "))
if user_age < 13:
    print("You are a child. ")
elif user_age >= 13 and user_age <= 19:
    print("You are a teenager. ")
elif user_age >= 20:
    print("You are an adult. ")

# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    for i in range(1, i+1):
        print(i, end="")
    print()
    
# Question 3:
# Write some code that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:
# The highest number.
# The lowest number.
# The average of all the numbers.
# Hint 1: You will need to use a for loop and a counter variable to keep track of the total sum of the numbers.
# Hint 2: You will need to use an if statement to keep track of the highest and lowest numbers.
highest_num = 0
lowest_num = 99999999
total = 0

for i in range(1,11):
    user_number = int(input("Please enter a number: "))
    total += user_number
    if user_number > highest_num:
        highest_num = user_number
    if user_number < lowest_num:
        lowest_num = user_number 
average = total/10         
print("The Highest Number is: " + str(highest_num))
print("The Lowest Number is: " + str(lowest_num))
print("The Average of All the Numbers is: " + str(average))

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement
string = input("Please enter a string: ")
string = string.lower()
vowel_counter = 0
for char in string:
    if char in 'aeiou':
        vowel_counter += 1
print("Number of vowels in the string: ", vowel_counter)