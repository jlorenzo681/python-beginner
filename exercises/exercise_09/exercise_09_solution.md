# Exercise 9: Solution

## Code
```python
n = int(input("Enter a positive number: "))

counter = 1
total = 0

while counter <= n:
    total += counter
    counter += 1

print(f"The sum of numbers from 1 to {n} is: {total}")
```

## Alternative Solution (using for loop)
```python
n = int(input("Enter a positive number: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"The sum of numbers from 1 to {n} is: {total}")
```

## Mathematical Solution
```python
n = int(input("Enter a positive number: "))

# Formula: sum = n * (n + 1) / 2
total = n * (n + 1) // 2

print(f"The sum of numbers from 1 to {n} is: {total}")
```

## Explanation
- We initialize a `counter` at 1 and `total` at 0
- The while loop continues as long as `counter <= n`
- In each iteration, we add the current counter value to the total
- We increment the counter using `counter += 1` (shorthand for `counter = counter + 1`)
- The loop stops when counter exceeds n
- The `+=` operator adds to the existing value

## Key Concepts
- **while loop**: Repeats code while a condition is True
- **Accumulator pattern**: Building up a result over multiple iterations
- **Loop counter**: Variable that tracks iterations
- **Compound operators**: `+=`, `-=`, `*=`, `/=` modify and assign in one step
- **Loop termination**: Ensuring the loop eventually stops

## Trace Example (n=5)
| Iteration | counter | total | Condition |
|-----------|---------|-------|-----------|
| Start     | 1       | 0     | 1 <= 5 ✓  |
| 1         | 2       | 1     | 2 <= 5 ✓  |
| 2         | 3       | 3     | 3 <= 5 ✓  |
| 3         | 4       | 6     | 4 <= 5 ✓  |
| 4         | 5       | 10    | 5 <= 5 ✓  |
| 5         | 6       | 15    | 6 <= 5 ✗  |
