# Exercise 18: Solution

## Code
```python
import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break

# Main program
print("Welcome to the Number Guessing Game!")

while True:
    play_game()

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
```

## Explanation
- `import random` brings in the random module
- `random.randint(a, b)` generates a random integer between a and b (inclusive)
- We use a function to organize the game logic
- The inner while loop continues until the guess is correct
- We track attempts with a counter that increments each guess
- `break` exits the loop when the correct number is guessed
- The outer loop allows playing multiple games
- `.lower()` makes the input case-insensitive

## Key Concepts
- **Modules**: Importing and using external code
- **random module**: Generating random numbers
- **Nested loops**: Loop within a loop
- **Game logic**: Implementing rules and feedback
- **Input validation**: Could add error handling for non-numeric input

## Common random Module Functions
```python
import random

random.randint(1, 10)      # Random integer from 1 to 10
random.random()            # Random float from 0.0 to 1.0
random.uniform(1, 10)      # Random float from 1.0 to 10.0
random.choice([1, 2, 3])   # Random item from list
random.shuffle(my_list)    # Shuffle list in place
random.sample([1,2,3], 2)  # Random sample of 2 items
```

## Enhanced Version with Input Validation
```python
import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

print("Welcome to the Number Guessing Game!")

while True:
    play_game()

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing!")
        break
```

## Difficulty Levels Enhancement
```python
def get_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter choice: ")

    if choice == "1":
        return 50
    elif choice == "2":
        return 100
    else:
        return 200

max_num = get_difficulty()
secret_number = random.randint(1, max_num)
```
