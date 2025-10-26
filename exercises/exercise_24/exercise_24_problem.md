# Exercise 24: Simple Grade Book

## Difficulty: Advanced+

## Description
Create a grade book system that manages student records, calculates grades, provides statistical analysis, and handles multiple subjects with grade point averages.

## Learning Objectives
- Work with nested data structures (dictionaries containing lists/dictionaries)
- Implement mathematical calculations and statistics
- Practice data validation and error handling
- Format complex output with tables
- Use functions to organize code effectively

## Requirements
- Store students with multiple grades per subject
- Add new students with name and ID
- Add grades for different subjects (Math, English, Science, etc.)
- Calculate average grade for each student
- Calculate class average for each subject
- Display student report cards
- Find top performing students
- Display letter grades (A, B, C, D, F)
- Show class statistics (highest, lowest, median)
- Validate all inputs (grades 0-100, unique student IDs)

## Expected Output
```
===== GRADE BOOK SYSTEM =====

1. Add student
2. Add grade
3. View student report
4. View all students
5. Class statistics
6. Top performers
7. Quit

Choose option: 1
Student name: Alice Johnson
Student ID: S001
Student added successfully!

Choose option: 2
Student ID: S001
Subject: Math
Grade (0-100): 95
Grade added!

Choose option: 3
Student ID: S001

===== REPORT CARD =====
Student: Alice Johnson (S001)
-----------------------------------
Subject          | Grade | Letter
-----------------------------------
Math             | 95.0  | A
English          | 88.0  | B
Science          | 92.0  | A
-----------------------------------
Average:         | 91.7  | A
GPA:             | 3.83  |
-----------------------------------

Choose option: 5

===== CLASS STATISTICS =====
Total Students: 3

Math:
  Average: 87.3
  Highest: 95.0 (Alice Johnson)
  Lowest: 78.0 (Bob Smith)

English:
  Average: 85.7
  Highest: 92.0 (Carol White)
  Lowest: 78.0 (Bob Smith)

Overall Class Average: 86.5
```

## Hints
- Use a dictionary to store students: `students = {"S001": {...}, "S002": {...}}`
- Each student is a dictionary: `{"name": "Alice", "grades": {"Math": [95, 88], "English": [90]}}`
- Calculate average: `sum(grades) / len(grades)`
- Letter grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
- GPA: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
- Use `.get()` for safe dictionary access
- Use max() and min() with key parameter for finding top students

## Challenge
Add these advanced features:
1. Weight grades differently (tests 60%, homework 40%)
2. Track attendance and factor into final grade
3. Generate grade distribution histogram
4. Save and load grade book from file
5. Calculate class rank for each student
6. Support grade curves and extra credit
