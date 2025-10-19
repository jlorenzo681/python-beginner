# Exercise 4: Solution

## Code
```python
name = input("What is your name? ")
age = int(input("How old are you? "))

birth_year = 2025 - age

print(f"Hello {name}! You are {age} years old and were born around {birth_year}.")
```

## Explanation
- `input()` function displays a prompt and waits for user input
- The `input()` function always returns a string, even if the user enters numbers
- We use `int()` to convert the age string to an integer so we can do math with it
- We calculate the birth year by subtracting the age from the current year (2025)
- The final message uses an f-string to combine all the variables

## Key Concepts
- **input() function**: Gets user input from the console
- **Type conversion**: Using `int()` to convert strings to integers
- **Variables**: Storing user data for later use
- **Calculations**: Performing arithmetic with user-provided data

## Common Mistakes
- Forgetting to convert age to int (you can't subtract strings from numbers)
- Not including the space after the prompt in `input()`
