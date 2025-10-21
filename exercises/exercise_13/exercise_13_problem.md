# Exercise 13: String Manipulation

## Difficulty: Intermediate

## Description
Write a program that demonstrates various string manipulation techniques.

## Learning Objectives
- Learn string methods and operations
- Understand string slicing
- Practice text processing

## Requirements
- Ask the user for a sentence
- Display the following:
  - Length of the sentence
  - Sentence in uppercase
  - Sentence in lowercase
  - Number of words in the sentence
  - Reversed sentence
  - First 3 characters
  - Whether it contains the word "python" (case-insensitive)

## Expected Output
```
Enter a sentence: Python is awesome!
Length: 18
Uppercase: PYTHON IS AWESOME!
Lowercase: python is awesome!
Number of words: 3
Reversed: !emosewa si nohtyP
First 3 characters: Pyt
Contains 'python': Yes
```

## Hints
- Use `len()` for length
- Use `.upper()` and `.lower()` for case conversion
- Use `.split()` to split into words
- Use slicing `[::-1]` to reverse
- Use slicing `[:3]` for first 3 characters
- Use `in` operator with `.lower()` to check for word
