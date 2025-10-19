# Exercise 6: Solution

## Code
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```

## Explanation
- We get a number from the user and convert it to an integer
- The condition `number % 2 == 0` checks if the remainder when dividing by 2 is 0
- If the condition is True, the number is even
- If the condition is False, we go to the `else` block and the number is odd
- The `==` operator checks for equality (different from `=` which assigns values)

## Key Concepts
- **if/else statements**: Execute different code based on conditions
- **Comparison operators**: `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`
- **Modulus operator**: Returns the remainder of division
- **Boolean values**: Conditions evaluate to True or False
- **Indentation**: Python uses indentation to define code blocks

## Visual Flow
```
number % 2 == 0?
    ├── True → Print "even"
    └── False → Print "odd"
```
