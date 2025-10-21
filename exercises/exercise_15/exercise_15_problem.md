# Exercise 15: Word Frequency Counter

## Difficulty: Intermediate+

## Description
Create a program that counts the frequency of each word in a sentence.

## Learning Objectives
- Combine string manipulation with dictionaries
- Practice text processing
- Understand frequency counting patterns

## Requirements
- Ask the user for a sentence
- Convert the sentence to lowercase
- Split the sentence into words
- Count how many times each word appears
- Display each word with its count
- Display the most common word

## Expected Output
```
Enter a sentence: The quick brown fox jumps over the lazy dog and the fox ran away
Word frequencies:
the: 3
quick: 1
brown: 1
fox: 2
jumps: 1
over: 1
lazy: 1
dog: 1
and: 1
ran: 1
away: 1

Most common word: "the" (appears 3 times)
```

## Hints
- Convert to lowercase with `.lower()`
- Split into words with `.split()`
- Use a dictionary to store word counts
- Use `.get(word, 0)` to safely get current count
- Iterate through words and increment counts
- Use `max()` with key parameter to find most common
