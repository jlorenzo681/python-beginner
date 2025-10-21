# Exercise 18: Number Guessing Game

## Difficulty: Advanced

## Description
Create a number guessing game where the computer picks a random number and the user tries to guess it.

## Learning Objectives
- Learn to use the random module
- Practice while loops with conditions
- Implement game logic
- Track attempts and provide feedback

## Requirements
- Generate a random number between 1 and 100
- Allow the user to guess the number
- Provide hints ("Too high" or "Too low")
- Count the number of attempts
- Congratulate when correct
- Ask if they want to play again

## Expected Output
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Too high! Try again.

Enter your guess: 31
Congratulations! You guessed it in 4 attempts!

Play again? (yes/no): no
Thanks for playing!
```

## Hints
- Use `import random` and `random.randint(1, 100)`
- Use a while loop to keep asking for guesses
- Compare guess to the secret number
- Use a counter variable to track attempts
- Use another loop to handle "play again"
