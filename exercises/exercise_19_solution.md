# Exercise 19: Solution

## Basic Solution
```python
text = input("Enter a word or phrase: ")

# Clean the text: remove spaces and convert to lowercase
cleaned = text.replace(" ", "").lower()

# Check if it's a palindrome
if cleaned == cleaned[::-1]:
    print(f'"{text}" is a palindrome!')
else:
    print(f'"{text}" is not a palindrome.')
```

## Advanced Solution (removes punctuation)
```python
def is_palindrome(text):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    # Check if cleaned text equals its reverse
    return cleaned == cleaned[::-1]

# Main program
text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print(f'"{text}" is a palindrome!')
else:
    print(f'"{text}" is not a palindrome.')
```

## Using Regular Expressions
```python
import re

def is_palindrome(text):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print(f'"{text}" is a palindrome!')
else:
    print(f'"{text}" is not a palindrome.')
```

## Explanation
- We first clean the text by removing spaces and converting to lowercase
- String slicing `[::-1]` reverses the string
- We compare the cleaned string with its reverse
- If they're equal, it's a palindrome
- For advanced checking, we also remove punctuation using `.isalnum()`

## Key Concepts
- **String cleaning**: Removing unwanted characters
- **String reversal**: Using slicing with step -1
- **String comparison**: Checking equality
- **Character methods**: `.isalnum()`, `.isalpha()`, `.isdigit()`
- **Edge cases**: Handling spaces, punctuation, and case

## String Character Methods
```python
char.isalnum()   # True if alphanumeric (letter or number)
char.isalpha()   # True if letter
char.isdigit()   # True if digit
char.islower()   # True if lowercase
char.isupper()   # True if uppercase
char.isspace()   # True if whitespace
```

## Alternative: Two-Pointer Approach
```python
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True
```

## Test Cases
```python
test_cases = [
    "racecar",                           # True
    "A man a plan a canal Panama",      # True
    "race a car",                        # False
    "Was it a rat I saw",                # True
    "Madam",                             # True
    "hello",                             # False
    "Never odd or even",                 # True
    ""                                   # True (empty is palindrome)
]

for test in test_cases:
    result = "is" if is_palindrome(test) else "is not"
    print(f'"{test}" {result} a palindrome')
```

## Enhanced Interactive Version
```python
def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]

print("Palindrome Checker")
print("-" * 40)

while True:
    text = input("\nEnter a word or phrase (or 'quit' to exit): ")

    if text.lower() == 'quit':
        break

    if not text.strip():
        print("Please enter some text.")
        continue

    if is_palindrome(text):
        print(f'"{text}" is a palindrome!')
    else:
        print(f'"{text}" is not a palindrome.')

print("Goodbye!")
```
