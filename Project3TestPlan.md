# Test Plan for Project 3
## 1

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_book_creation|"Test Book", "Author Name", 1234567890|New Book Object Created|AssertionError|Fail|The Book Class was expecting the isbn as the first argument|
|002|test_book_creation|1234567890, "Test Book", "Author Name"|New Book Object Created|New Book Object Created|Pass|N/A|

## 2

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_book_checkout|Test Book", "Author Name", 1234567890|New Book Object Created|New Book Object Created|Pass|N/A|

## 3

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_book_return|"Test Book", "Author Name", 1234567890|New Book Object Created|New Book Object Created|Pass|N/A|

## 4

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_user_creation|"John Doe", 1|New User Object Created|InsertionError|Fail|Import User was not indented correctly|
|002|test_user_creation|"John Doe", 1|New User Object Created|New User Object Created|Pass|N/A|

## 5

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_user_borrow|"Test Book", "Author Name", 1234567890, "John Doe", 1|New User and Book Object Created|AssertionError|Fail|The Book Class was expecting the isbn as the first argument|
|002|test_user_borrow|"Test Book", "Author Name", 1234567890, "John Doe", 1|New User and Book Object Created|New User and Book Object Created|Pass|N/A|

## 6

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_library_add_book|"Test Book", "Author Name", 1234567890|New User and Book Object Created|AssertionError|Fail|The Book Class was expecting the isbn as the first argument|
|002|test_library_add_book|1234567890, "Test Book", "Author Name"|New User and Book Object Created|New User and Book Object Created|Pass|N/A|

## 7

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_library_add_user|"John Doe", 1|New Library Object Created|New Library Object Created|Pass|N/A|

## 8

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_library_find_book|"Test Book", "Author Name", 1234567890|New Library Object Created|AssertionError|Fail|The Book Class was expecting the isbn as the first argument|
|002|test_library_find_book|1234567890, "Test Book", "Author Name"|New Library Object Created|New Library Object Created|Pass|N/A

## 9

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
|001|test_library_find_user|||IndentationError|Pass|Missing an indentation|
|002|test_library_find_user||||Pass|N/A|