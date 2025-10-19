# Exercise 16: List Comprehensions

## Difficulty: Intermediate+

## Description
Learn and practice list comprehensions to create lists in a concise and elegant way.

## Learning Objectives
- Understand list comprehension syntax
- Replace traditional loops with comprehensions
- Practice filtering and transforming data

## Requirements
Create the following using list comprehensions:
1. A list of squares of numbers from 1 to 10
2. A list of even numbers from 1 to 20
3. A list of lengths of words in a given sentence
4. A list of uppercase words from a sentence (only words longer than 3 characters)

## Expected Output
```
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Enter a sentence: The quick brown fox jumps
Word lengths: [3, 5, 5, 3, 5]
Long words (uppercase): ['QUICK', 'BROWN', 'JUMPS']
```

## Hints
- List comprehension syntax: `[expression for item in iterable]`
- With condition: `[expression for item in iterable if condition]`
- Squares: `[x**2 for x in range(1, 11)]`
- Even: `[x for x in range(1, 21) if x % 2 == 0]`
