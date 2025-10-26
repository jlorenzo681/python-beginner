# Exercise 21: Solution

## Solution 1: Basic Version
```python
import random

# Game setup
target_number = random.randint(1, 100)
attempts = 0
guesses = []
game_over = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

# Main game loop
while not game_over:
    try:
        guess = int(input("Enter your guess: "))

        # Add to tracking
        attempts += 1
        guesses.append(guess)

        # Check the guess
        if guess == target_number:
            print(f"Congratulations! You guessed it in {attempts} attempts!\n")
            game_over = True
        elif guess < target_number:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")

        # Provide hint every 3 guesses
        if attempts % 3 == 0 and not game_over:
            min_val = max(1, target_number - 10)
            max_val = min(100, target_number + 10)
            print(f"Hint: The number is between {min_val} and {max_val}\n")

    except ValueError:
        print("Invalid input! Please enter a number.\n")

# Display statistics
print("Game Statistics:")
print(f"All your guesses: {guesses}")
print(f"Number of attempts: {attempts}")
print(f"Highest guess: {max(guesses)}")
print(f"Lowest guess: {min(guesses)}")
```

## Solution 2: Enhanced Version with Better Hints
```python
import random

def play_game():
    """Play one round of the guessing game."""
    target_number = random.randint(1, 100)
    attempts = 0
    guesses = []
    low_bound = 1
    high_bound = 100

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            # Validate guess range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue

            attempts += 1
            guesses.append(guess)

            if guess == target_number:
                print(f"Congratulations! You guessed it in {attempts} attempts!\n")
                break
            elif guess < target_number:
                print("Too low! Try again.\n")
                low_bound = max(low_bound, guess)
            else:
                print("Too high! Try again.\n")
                high_bound = min(high_bound, guess)

            # Provide hint after every 3 wrong guesses
            if attempts % 3 == 0:
                print(f"Hint: The number is between {low_bound} and {high_bound}\n")

        except ValueError:
            print("Invalid input! Please enter a number.\n")

    # Display statistics
    print("Game Statistics:")
    print(f"All your guesses: {guesses}")
    print(f"Number of attempts: {attempts}")
    print(f"Highest guess: {max(guesses)}")
    print(f"Lowest guess: {min(guesses)}")

    return attempts

# Play the game
play_game()
```

## Solution 3: Multi-Round with Difficulty Levels
```python
import random

def play_game(min_num, max_num):
    """Play one round of the guessing game with custom range."""
    target_number = random.randint(min_num, max_num)
    attempts = 0
    guesses = []
    low_bound = min_num
    high_bound = max_num

    print(f"\nI'm thinking of a number between {min_num} and {max_num}.\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < min_num or guess > max_num:
                print(f"Please enter a number between {min_num} and {max_num}.\n")
                continue

            attempts += 1
            guesses.append(guess)

            if guess == target_number:
                print(f"Congratulations! You guessed it in {attempts} attempts!\n")
                break
            elif guess < target_number:
                print("Too low! Try again.\n")
                low_bound = max(low_bound, guess)
            else:
                print("Too high! Try again.\n")
                high_bound = min(high_bound, guess)

            # Hint every 3 guesses
            if attempts % 3 == 0:
                print(f"Hint: The number is between {low_bound} and {high_bound}\n")

        except ValueError:
            print("Invalid input! Please enter a number.\n")

    # Display statistics
    print("Game Statistics:")
    print(f"All your guesses: {guesses}")
    print(f"Number of attempts: {attempts}")
    if guesses:
        print(f"Highest guess: {max(guesses)}")
        print(f"Lowest guess: {min(guesses)}")

    return attempts

# Main game loop
print("Welcome to the Number Guessing Game!")
print("\nDifficulty Levels:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

best_score = None
rounds_played = 0

while True:
    # Select difficulty
    difficulty = input("\nChoose difficulty (1-3) or 'q' to quit: ")

    if difficulty.lower() == 'q':
        break

    if difficulty == '1':
        score = play_game(1, 50)
    elif difficulty == '2':
        score = play_game(1, 100)
    elif difficulty == '3':
        score = play_game(1, 500)
    else:
        print("Invalid choice!")
        continue

    rounds_played += 1

    # Track best score
    if best_score is None or score < best_score:
        best_score = score
        print(f"New best score! {best_score} attempts")

    # Ask to play again
    play_again = input("\nPlay another round? (y/n): ")
    if play_again.lower() != 'y':
        break

# Final statistics
if rounds_played > 0:
    print(f"\nTotal rounds played: {rounds_played}")
    print(f"Best score: {best_score} attempts")
    print("Thanks for playing!")
```

## Explanation

### Key Concepts

1. **Random Number Generation**
   - `random.randint(a, b)` generates a random integer between a and b (inclusive)
   - The random module must be imported

2. **List Operations**
   - `guesses.append(guess)` adds each guess to the list
   - `max(guesses)` and `min(guesses)` find highest and lowest values
   - Lists maintain order, so we can see the guess history

3. **Input Validation**
   - `try-except` catches `ValueError` when user enters non-numeric input
   - Additional range validation ensures guess is within bounds

4. **Game Logic**
   - While loop continues until correct guess
   - Bounds tracking improves hints over time
   - Counter tracks attempts

5. **User Experience**
   - Clear feedback for each guess
   - Helpful hints at regular intervals
   - Comprehensive statistics at the end

## Common Pitfalls

1. **Forgetting to import random**
   ```python
   # Wrong
   target = randint(1, 100)  # NameError

   # Correct
   import random
   target = random.randint(1, 100)
   ```

2. **Not handling invalid input**
   ```python
   # Risky
   guess = int(input("Guess: "))  # Crashes on non-numeric input

   # Better
   try:
       guess = int(input("Guess: "))
   except ValueError:
       print("Please enter a number!")
   ```

3. **Forgetting to update bounds**
   - Without updating low_bound and high_bound, hints aren't useful

## Testing Checklist

- [ ] Game generates different numbers each time
- [ ] Correct guess ends the game
- [ ] "Too high" and "too low" messages work correctly
- [ ] Hints appear every 3 guesses
- [ ] Invalid input doesn't crash the program
- [ ] Statistics display correctly
- [ ] Handles edge cases (1, 100, first guess correct)

## Extensions

1. **Add a scoring system based on number of attempts**
   ```python
   if attempts <= 5:
       print("Perfect! Score: A+")
   elif attempts <= 10:
       print("Great! Score: A")
   elif attempts <= 15:
       print("Good! Score: B")
   else:
       print("Score: C")
   ```

2. **Save high scores to a file**
   ```python
   with open('highscores.txt', 'a') as f:
       f.write(f"{attempts}\n")
   ```

3. **Add a time limit**
   ```python
   import time
   start_time = time.time()
   # ... game logic ...
   elapsed = time.time() - start_time
   print(f"Time taken: {elapsed:.1f} seconds")
   ```
