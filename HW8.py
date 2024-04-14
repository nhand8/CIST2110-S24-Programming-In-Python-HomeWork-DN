# HW8.py
# Author:

# This homework will exapnd upon the code for Lab10.py. If you did not complete Lab10.py, you should do so before attempting this homework.

# Copy the code from Lab10.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)
import streamlit as st
import datetime as dt

# Streamlit title, subtitle, date, and button


# The calculate_days function from Lab10.py


# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.


# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)

# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE.
# new_years = dt.date(2025, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")


# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.

# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date.
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# app function from Lab10.py


if __name__ == "__main__":
    app()
