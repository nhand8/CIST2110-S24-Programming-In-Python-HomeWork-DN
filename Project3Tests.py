# Import Statments
import pytest   



#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author: Dylan Nhan
# CIST2110-Project-3 Library Management System (LMS) Test Cases
# This file should be used in conjunction with a test plan that you create. The file can be csv, markdown, or text. The test plan should be submitted with this file and project3.py.
from Project3 import Book

# Test cases for the Book class

def test_book_creation():
    book = Book(1234567890, "Test Book", "Author Name")
    assert book.title == "Test Book"
    assert book.author == "Author Name"
    assert book.isbn == 1234567890
    assert not book.borrowed


def test_book_checkout():
    book = Book("Test Book", "Author Name", 1234567890)
    book.check_out()
    assert book.borrowed


def test_book_return():
    book = Book("Test Book", "Author Name", 1234567890)
    book.check_out()
    book.check_in()
    assert not book.borrowed

from Project3 import User
# Test cases for the User class
def test_user_creation():
    user = User("John Doe", 1)
    assert user.name == "John Doe"
    assert user.member_id == 1
    assert user.borrowed_books == []


def test_user_borrow():
    user = User("John Doe", 1)
    book = Book(1234567890, "Test Book", "Author Name")
    user.borrow_book(book)
    assert book in user.borrowed_books
    assert book.borrowed


from Project3 import Library

# Test cases for the Library class
def test_library_add_book():
    library = Library()
    book = Book(1234567890, "Test Book", "Author Name")
    library.add_book(book)
    assert book in library.books


def test_library_add_user():
    library = Library()
    user = User("John Doe", 1)
    library.add_user(user)
    assert user in library.users


def test_library_find_book():
    library = Library()
    book = Book(1234567890, "Test Book", "Author Name")
    library.add_book(book)
    print(library.books)
    found = library.find_book(1234567890)
    print(library.books)
    assert found in library.books
    assert None == library.find_book(1234567891)


def test_library_find_user():
    library = Library()
    ### Implement this test case ###        

    ### Be sure to include this test case in your test plan ### 
