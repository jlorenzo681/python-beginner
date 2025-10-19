# Exercise 8: Solution

## Code
```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

## Alternative Solution (more compact)
```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

## Explanation
- The `for` loop iterates over a sequence of numbers
- `range(1, 11)` generates numbers from 1 to 10 (11 is exclusive)
- The loop variable `i` takes each value in the range, one at a time
- On each iteration, we calculate `number * i` and print the result
- The loop automatically repeats until all values are processed

## Key Concepts
- **for loop**: Repeats code for each item in a sequence
- **range() function**: Generates a sequence of numbers
  - `range(stop)`: 0 to stop-1
  - `range(start, stop)`: start to stop-1
  - `range(start, stop, step)`: start to stop-1, incrementing by step
- **Loop variable**: Temporarily holds each value during iteration
- **Iteration**: Repeating a process multiple times

## range() Examples
- `range(5)` → 0, 1, 2, 3, 4
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8
