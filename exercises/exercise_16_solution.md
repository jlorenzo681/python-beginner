# Exercise 16: Solution

## Code
```python
# 1. Squares of numbers 1-10
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# 2. Even numbers 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers: {evens}")

# 3. Lengths of words in a sentence
sentence = input("\nEnter a sentence: ")
words = sentence.split()
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")

# 4. Uppercase words longer than 3 characters
long_words = [word.upper() for word in words if len(word) > 3]
print(f"Long words (uppercase): {long_words}")
```

## Traditional Loop Equivalents

### Squares
```python
# List comprehension
squares = [x**2 for x in range(1, 11)]

# Traditional loop
squares = []
for x in range(1, 11):
    squares.append(x**2)
```

### Even numbers
```python
# List comprehension
evens = [x for x in range(1, 21) if x % 2 == 0]

# Traditional loop
evens = []
for x in range(1, 21):
    if x % 2 == 0:
        evens.append(x)
```

## Explanation
- List comprehensions create lists in a single line
- Basic syntax: `[expression for item in iterable]`
- With filter: `[expression for item in iterable if condition]`
- The expression can be any valid Python expression
- Conditions filter which items are included

## Key Concepts
- **List comprehensions**: Concise way to create lists
- **Expression**: What to put in the new list
- **Iterable**: What to loop over
- **Condition**: Optional filter for items
- **Readability vs Conciseness**: Use comprehensions for simple cases

## Advanced Examples

### Nested comprehensions
```python
# Create a 3x3 matrix
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### Multiple conditions
```python
# Numbers divisible by both 2 and 3
numbers = [x for x in range(1, 31) if x % 2 == 0 if x % 3 == 0]
# [6, 12, 18, 24, 30]
```

### With if-else
```python
# "even" or "odd" labels
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
# ['odd', 'even', 'odd', 'even', 'odd']
```

## When to Use List Comprehensions
✅ Simple transformations and filters
✅ Creating lists from iterables
✅ When readability isn't sacrificed

❌ Complex logic (use regular loops)
❌ Side effects (printing, file writing)
❌ When it becomes hard to read
