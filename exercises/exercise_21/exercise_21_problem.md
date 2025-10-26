# Exercise 21: Number Guessing Game with Statistics

## Difficulty: Advanced

## Description
Create an enhanced number guessing game that tracks player statistics including number of attempts, all guesses made, and provides hints.

## Learning Objectives
- Practice while loops and conditionals
- Work with lists to track data
- Implement game logic with multiple features
- Use random number generation
- Calculate and display statistics

## Requirements
- Generate a random number between 1 and 100
- Allow the player to guess the number
- Provide feedback (too high, too low, correct)
- Track all guesses in a list
- Count the number of attempts
- Show hints after every 3 wrong guesses
- Display statistics when the player wins
- Validate user input (handle non-numeric input)

## Expected Output
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too low! Try again.

Enter your guess: 75
Too high! Try again.

Enter your guess: 60
Too low! Try again.

Hint: The number is between 60 and 75

Enter your guess: 67
Congratulations! You guessed it in 4 attempts!

Game Statistics:
All your guesses: [50, 75, 60, 67]
Number of attempts: 4
Highest guess: 75
Lowest guess: 50
```

## Hints
- Use `import random` and `random.randint(1, 100)` to generate a random number
- Use a while loop that continues until the correct guess
- Use a list to store all guesses: `guesses.append(guess)`
- Use a counter variable to track attempts
- Use try-except to handle invalid input
- Calculate min and max from the guesses list

## Challenge
Add the following features:
1. Allow the player to play multiple rounds
2. Track the best score (fewest attempts)
3. Offer difficulty levels (different number ranges)
