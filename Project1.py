# Project1.py
# Author: Dylan Nhan

# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions
# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.
# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome_message():
    print("Welcome to Dylan's Quiz Game!!!")
    print("You will be asked a series of questions and will be given 4 options to choose from.")
    print("You will be given a score at the end of the game based on how many questions you answered correctly.")
    print("Good luck!!!\n")
welcome_message()   
# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
def ask_question(question:str, option_1:str, option_2:str, option_3:str, option_4:str, correct_answer:str)->bool:
    """Ask a question and check the answer

    Args:
        question (str): the question
        option_1 (str): the first option
        option_2 (str): the second option
        option_3 (str): the third option
        option_4 (str): the fourth option
        correct_answer (str): the correct answer

    Returns:
        bool: whether the user was correct
    """
    print(question)
    print("a) " + option_1)
    print("b) " + option_2)
    print("c) " + option_3)
    print("d) " + option_4)
    while True:
        user_answer = input("Please enter your answer: ").lower()
        if user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
            if user_answer == correct_answer:
                print("Correct!") 
                return True
            else:
                print("Incorrect! The correct answer is: " + correct_answer)
                return False 
                break
        elif user_answer not in ["a", "b", "c", "d"]:
            print("Invalid input. Please enter a, b, c, or d only! Try again.")
        else:
            print("Incorrect! The correct answer is: " + correct_answer)
        
 
question_1 = ask_question("What products did Amazon originally only sell?", "Books", "Technology", "Gift Cards", "Cooking Appliances", "a")

question_2 = ask_question("Who painted the Mona Lisa?", "Leonardo da Pizza", "Leonardo da Vinci", "Leonardo da Caprio", "Leonardo da Quincy", "b")

question_3 = ask_question("Who was Walt Disney's favorite princess?", "Mulan", "Moana", "Cinderella", "Ariel", "c")

question_4 = ask_question("How many hearts does an Octopus have?", "Five", "Three", "Nine", "Seventeen", "b")

question_5 = ask_question("What color is a giraffe's tongue?", "Blue", "Purple", "Pink", "Black", "d")

score = 0

for question in [question_1, question_2, question_3, question_4, question_5]:
    if question:
        score += 1

# Score Tracking:
# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
print("The Quiz is Done! Your score is: " + str(score))
print("Thank you for playing!")

# Function Utilization:
# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, the correct answer, and return whether the user was correct.
# an example would be def ask_question(question:str, option_1:str, option_2:str, option_3,:str option_4:str, correct_answer:str)->bool:
# the return value should be a boolean (True or False) for whether the user was correct
# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).