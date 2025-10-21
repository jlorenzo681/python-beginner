# Exercise 14: Student Grade Book

## Difficulty: Intermediate+

## Description
Create a grade book program using dictionaries to store student names and their grades.

## Learning Objectives
- Learn to create and use dictionaries
- Understand key-value pairs
- Practice dictionary methods and operations

## Requirements
- Create a dictionary to store at least 3 students with their grades
- Display all students and their grades
- Calculate and display the average grade
- Find and display the student with the highest grade
- Allow user to look up a grade by student name

## Expected Output
```
Grade Book:
Alice: 85
Bob: 92
Charlie: 78

Average grade: 85.0

Top student: Bob with grade 92

Enter student name to look up: Alice
Alice's grade: 85
```

## Hints
- Create dictionary with curly braces: `grades = {"name": score}`
- Use `.items()` to iterate over keys and values
- Use `.values()` to get all values
- Use `max()` to find maximum value
- Access values with `dictionary[key]`
