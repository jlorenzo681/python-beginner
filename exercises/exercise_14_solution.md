# Exercise 14: Solution

## Code
```python
# Create grade book
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Display all students and grades
print("Grade Book:")
for name, grade in grades.items():
    print(f"{name}: {grade}")

# Calculate average
average = sum(grades.values()) / len(grades)
print(f"\nAverage grade: {average}")

# Find top student
top_student = max(grades, key=grades.get)
top_grade = grades[top_student]
print(f"\nTop student: {top_student} with grade {top_grade}")

# Look up a student
student_name = input("\nEnter student name to look up: ")
if student_name in grades:
    print(f"{student_name}'s grade: {grades[student_name]}")
else:
    print(f"{student_name} not found in grade book.")
```

## Explanation
- Dictionaries store key-value pairs (name: grade)
- `.items()` returns both keys and values for iteration
- `.values()` returns just the values
- `sum()` adds up all values
- `max(dict, key=dict.get)` finds the key with the maximum value
- `in` operator checks if a key exists in the dictionary
- Square brackets `[]` access values by key

## Key Concepts
- **Dictionaries**: Unordered collections of key-value pairs
- **Dictionary methods**: .items(), .keys(), .values(), .get()
- **Key lookup**: Fast access to values using keys
- **Dictionary iteration**: Looping through keys, values, or both

## Common Dictionary Operations
```python
# Creating dictionaries
my_dict = {"key": "value"}
my_dict = dict(key="value")

# Adding/updating
my_dict["new_key"] = "new_value"

# Accessing
value = my_dict["key"]
value = my_dict.get("key", "default")  # Safer

# Removing
del my_dict["key"]
value = my_dict.pop("key")

# Checking existence
if "key" in my_dict:
    ...

# Iterating
for key in my_dict:              # Keys only
for value in my_dict.values():   # Values only
for key, value in my_dict.items():  # Both
```

## Alternative: Using get() for safer lookup
```python
student_name = input("\nEnter student name to look up: ")
grade = grades.get(student_name)
if grade is not None:
    print(f"{student_name}'s grade: {grade}")
else:
    print(f"{student_name} not found in grade book.")
```
