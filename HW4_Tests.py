# HW4_Tests.py
# Author:

import pytest


from HW4 import (
    add,
    subtract,
    divide,
    multiply,
    greet,
    square,
    is_even,
    grade_calculator,
    speed_check,
    is_leap_year,
)


def test_add():
    assert add(3, 2) == 5, "Addition failed"
    assert add(0, 5) == 5, "Addition failed with 0"


def test_subtract():
    assert subtract(5, 3) == 2, "Subtraction failed"
    assert subtract(3, 5) == -2, "Subtraction failed with negative result"


def test_divide():
    assert divide(6, 2) == 3, "Division failed"
    with pytest.raises(ZeroDivisionError):  # Expected error for dividing by zero
        divide(1, 0)


def test_multiply():
    assert multiply(4, 3) == 12, "Multiplication failed"
    assert multiply(4, 0) == 0, "Multiplication failed with 0"


def test_greet():
    assert greet("John") == "Hello, John!", "Greeting failed"
    assert greet("Doe") == "Hello, Doe!", "Greeting failed with different name"


def test_square():
    assert square(4) == 16, "Squaring failed"
    assert square(0) == 0, "Squaring failed with 0"


def test_is_even():
    assert is_even(4) == True, "Even check failed for even number"
    assert is_even(3) == False, "Even check failed for odd number"


def test_grade_calculator():
    assert grade_calculator(95) == "A", "Grade calculation failed for A"
    assert grade_calculator(85) == "B", "Grade calculation failed for B"
    assert grade_calculator(75) == "C", "Grade calculation failed for C"
    assert grade_calculator(79) == "C", "Grade calculation failed for C"
    assert grade_calculator(65) == "D", "Grade calculation failed for D"
    assert grade_calculator(50) == "F", "Grade calculation failed for F"
    assert (
        grade_calculator(105) == "Invalid Score"
    ), "Grade calculation failed for out-of-range score"
    assert (
        grade_calculator(-5) == "Invalid Score"
    ), "Grade calculation failed for negative score"


def test_speed_check():
    assert speed_check(10) == "Too slow", "Speed check failed for too slow"
    assert speed_check(50) == "Within limit", "Speed check failed for within limit"
    assert (
        speed_check(80) == "Over speed limit"
    ), "Speed check failed for over speed limit"
    assert (
        speed_check(65) == "Within limit"
    ), "Speed check failed for upper end of within limit"


def test_is_leap_year():
    assert is_leap_year(2020) == True, "Leap year check failed for leap year"
    assert is_leap_year(2021) == False, "Leap year check failed for non-leap year"
    assert is_leap_year(2000) == True, "Leap year check failed for century leap year"
    assert (
        is_leap_year(1900) == False
    ), "Leap year check failed for century non-leap year"
