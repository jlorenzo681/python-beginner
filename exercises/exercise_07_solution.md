# Exercise 7: Solution

## Code
```python
grade = int(input("Enter your grade: "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your letter grade is: {letter}")
```

## Alternative Solution (more verbose)
```python
grade = int(input("Enter your grade: "))

if grade >= 90 and grade <= 100:
    print("Your letter grade is: A")
elif grade >= 80 and grade < 90:
    print("Your letter grade is: B")
elif grade >= 70 and grade < 80:
    print("Your letter grade is: C")
elif grade >= 60 and grade < 70:
    print("Your letter grade is: D")
elif grade >= 0 and grade < 60:
    print("Your letter grade is: F")
else:
    print("Invalid grade")
```

## Explanation
- We use `elif` (else if) to check multiple conditions in sequence
- Python evaluates conditions from top to bottom
- Once a condition is True, that block executes and the rest are skipped
- We check from highest to lowest, so we only need `>=` comparisons
- The `else` catches all remaining cases (grades below 60)

## Key Concepts
- **elif statement**: Chain multiple conditions together
- **Logical operators**: `and`, `or`, `not` for complex conditions
- **Range checking**: Determining if a value falls within a range
- **Control flow**: Only one block of code executes

## Why Check Highest to Lowest?
If we check `grade >= 60` first, a grade of 85 would match and return "D" incorrectly!
