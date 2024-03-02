# Test Plan for HW4
## 1. 'add' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | add - Test with positive numbers | 3, 2 | 5 | 1 | FAILED | a - b is the incorrect operation |
002 | add - Test with positive numbers (bugfix 001) | 3, 2 | 5 | 5 | PASS | N/A |
003 | add - Test with positive numbers | 0, 5 | 5 | -5 | FAILED | a - b is the incorrect operation |
004 | add - Test with positive numbers (bugfix 003) | 0, 5 | 5 | 5 | PASS | N/A |


## 2. 'subtract' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | subtract - Test with positive numbers | 5, 3 | 2 | 8 | FAILED | a + b is the incorrect operation |
002 | subtract - Test with positive numbers (bugfix 001) | 5, 3 | 2 | 2 | PASS | N/A |
003 | subtract - Test with positive numbers | 3, 5 | -2 | 8 | FAILED | a + b is the incorrect operation |
004 | subtract - Test with positive numbers (bugfix 003) | 3, 5 | -2 | -2 | PASS | N/A |


## 3. 'divide' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | divide - Test with positive numbers | 6, 2 | 3.0 | 12 | FAILED | a * b is the incorrect operation |
002 | divide - Test with positive numbers (bugfix 001) | 6, 2 | 3.0 | 3.0 | PASS | N/A |
003 | divide - Test with positive numbers | 1, 0 | ZeroDivisionError | 0 | FAILED | a * b is the incorrect operation |
004 | divide - Test with positive numbers (bugfix 003) | 1, 0 | ZeroDivisionError | ZeroDivisionError | PASS | N/A |


## 4. 'multiply' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | multiply - Test with positive numbers | 4, 3 | 12 | 1.3333333333333333 | FAILED | a / b is the incorrect operation |
002 | multiply - Test with positive numbers (bugfix 001) | 4, 3 | 12 | 12 | PASS | N/A |
003 | multiply - Test with positive numbers | 4, 0 | 0 | ZeroDivisionError | FAILED | a / b is the incorrect operation |
004 | multiply - Test with positive numbers (bugfix 003) | 4, 0 | 0 | 0 | PASS | N/A |


## 5. 'greet' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | greet - Test with strings | "John" | Hello, John! | Heloo, John! | FAILED | "Hello" was spelled incorrectly" |
002 | greet - Test with strings (bugfix 001) | "John" | Hello, John! | Hello, John! | PASS | N/A |
003 | greet - Test with strings | "Doe" | Hello, Doe! | "Heloo, Doe!" | FAILED | "Hello" was spelled incorrectly |
004 | greet - Test with strings | "Doe" | Hello, Doe! | Hello, Doe! | PASS | N/A |


## 6. 'grade_calc' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | grade_calc - Test with float | 95 | A | A | PASS | N/A |
002 | grade_calc - Test with float | 85 | B | B | PASS | N/A |
003 | grade_calc - Test with float | 75 | C | C | PASS | N/A |
004 | grade_calc - Test with float | 79 | C | Invalid Score | FAILED | condition did not include <= |
005 | grade_calc - Test with float (bugfix 004) | 79 | C | C | PASS | N/A |
006 | grade_calc - Test with float | 65 | D | D | PASS | N/A |
007 | grade_calc - Test with float | 50 | F | F | PASS | N/A |
008 | grade_calc - Test with float | 105 | Invalid Score | OutOfRange | FAILED | data input was out of range |
009 | grade_calc - Test with float | 105 | Invalid Score | Invalid Score | PASS | N/A |
0010 | grade_calc - Test with float | -5 | Invalid Score | OutOfRange | FAILED | data input was out of range |
0011 | grade_calc - Test with float | -5 | Invalid Score | Invalid Score | PASS | N/A |


## 7. 'speed_check' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | speed_check - Test with float | 10 | Too slow | Too Slow | PASS | N/A |
002 | speed_check - Test with float | 50 | Within limit | Within limit | PASS | N/A |
003 | speed_check - Test with float | 80 | Over speed limit | Over speed limit | PASS | N/A |
004 | speed_check - Test with float | 65 | Within limit | Unknown | FAILED | condition did not include <= 70 |
005 | speed_check - Test with float | 65 | Within limit | Within limit | PASS | N/A |



## 8. 'is_leap_year' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | is_leap_year - Test with int | 2020 | True | True | PASS | N/A |
002 | is_leap_year - Test with int | 2021 | False | False | PASS | N/A |
003 | is_leap_year - Test with int | 2000 | True | True | PASS | N/A |
004 | is_leap_year - Test with int | 1900 | False | True | FAILED | condition was not placed in correct order |
005 | sis_leap_year - Test with int (bugfix 004) | 1900 | False | False | PASS | N/A |