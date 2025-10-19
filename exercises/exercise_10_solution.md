# Exercise 10: Solution

## Code
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = None
    print("Invalid operation!")

# Display result
if result is not None:
    print(f"Result: {num1} {operation} {num2} = {result}")
```

## Explanation
- Each function is defined with `def`, takes two parameters, and returns a result
- Parameters `a` and `b` are placeholders that receive values when the function is called
- The `return` statement sends the calculated value back to where the function was called
- We store the returned value in the `result` variable
- We check which operation was entered and call the corresponding function

## Key Concepts
- **Function definition**: Creating reusable blocks of code
- **Parameters**: Inputs that functions receive
- **Return values**: Outputs that functions send back
- **Function call**: Using the function by passing arguments
- **Scope**: Variables inside functions are local to that function
- **Code reusability**: Functions can be called multiple times

## Function Anatomy
```python
def function_name(parameter1, parameter2):  # Definition
    result = parameter1 + parameter2        # Function body
    return result                           # Return value

output = function_name(5, 3)                # Function call
```

## Enhanced Version (with error handling)
```python
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
```
