# Exercise 5: Solution

## Code
```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C is equal to:")
print(f"  {fahrenheit:.2f}°F (Fahrenheit)")
print(f"  {kelvin:.2f} K (Kelvin)")
```

## Explanation
- We use `float()` instead of `int()` because temperatures can have decimal values
- The Fahrenheit formula multiplies by 9/5 (or 1.8) and adds 32
- The Kelvin formula simply adds 273.15 to the Celsius value
- The `:.2f` format specifier rounds the number to 2 decimal places
- The special character `°` represents the degree symbol

## Key Concepts
- **float() function**: Converts input to decimal numbers
- **String formatting**: Using `:.2f` to control decimal places
- **Mathematical formulas**: Implementing real-world calculations
- **Multiple outputs**: Displaying related information together

## Temperature Conversion Formulas
- **Celsius to Fahrenheit**: F = (C × 9/5) + 32
- **Celsius to Kelvin**: K = C + 273.15
- **Fahrenheit to Celsius**: C = (F - 32) × 5/9
