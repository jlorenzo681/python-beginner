# Exercise 19: Palindrome Checker

## Difficulty: Advanced

## Description
Create a program that checks if a word or phrase is a palindrome (reads the same forwards and backwards).

## Learning Objectives
- Practice string manipulation
- Understand string cleaning and normalization
- Work with string reversal
- Handle edge cases

## Requirements
- Ask the user for a word or phrase
- Remove spaces and convert to lowercase
- Check if it's a palindrome
- Display whether it is or isn't a palindrome
- Test with: "racecar", "A man a plan a canal Panama", "hello"

## Expected Output
```
Enter a word or phrase: racecar
"racecar" is a palindrome!

Enter a word or phrase: A man a plan a canal Panama
"A man a plan a canal Panama" is a palindrome!

Enter a word or phrase: hello
"hello" is not a palindrome.
```

## Hints
- Remove spaces with `.replace(" ", "")`
- Convert to lowercase with `.lower()`
- Reverse string with slicing `[::-1]`
- Compare cleaned string with its reverse
- Consider removing punctuation for advanced version
