# Exercise 5: Temperature Converter

## Difficulty: Beginner

## Description
Create a program that converts temperatures between Celsius and Fahrenheit.

## Learning Objectives
- Work with formulas and calculations
- Get numeric input from users
- Format output with decimal places

## Requirements
- Ask the user for a temperature in Celsius
- Convert it to Fahrenheit using the formula: F = (C × 9/5) + 32
- Convert it to Kelvin using the formula: K = C + 273.15
- Display both conversions with 2 decimal places

## Expected Output
```
Enter temperature in Celsius: 25
25.0°C is equal to:
  77.00°F (Fahrenheit)
  298.15 K (Kelvin)
```

## Hints
- Use `float()` to convert input to a decimal number
- Use `:.2f` in f-strings to format to 2 decimal places: `f"{value:.2f}"`
- Remember the order of operations in the Fahrenheit formula
