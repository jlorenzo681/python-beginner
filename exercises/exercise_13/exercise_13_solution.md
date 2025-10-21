# Exercise 13: Solution

## Code
```python
sentence = input("Enter a sentence: ")

print(f"Length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Number of words: {len(sentence.split())}")
print(f"Reversed: {sentence[::-1]}")
print(f"First 3 characters: {sentence[:3]}")

if "python" in sentence.lower():
    print("Contains 'python': Yes")
else:
    print("Contains 'python': No")
```

## Explanation
- `len(string)` returns the number of characters
- `.upper()` converts all characters to uppercase
- `.lower()` converts all characters to lowercase
- `.split()` splits a string into a list of words (by whitespace)
- String slicing `[start:end:step]` extracts portions of a string
  - `[::-1]` means start to end with step -1 (reverses the string)
  - `[:3]` means from start to index 3 (first 3 characters)
- The `in` operator checks if a substring exists in a string

## Key Concepts
- **String methods**: Built-in functions that operate on strings
- **String slicing**: Extracting parts of strings using `[start:end:step]`
- **String immutability**: Strings cannot be changed; methods return new strings
- **Membership testing**: Using `in` to check if substring exists

## Common String Methods
- `.upper()`: Convert to uppercase
- `.lower()`: Convert to lowercase
- `.title()`: Capitalize first letter of each word
- `.strip()`: Remove leading/trailing whitespace
- `.split(separator)`: Split string into list
- `.join(list)`: Join list items into string
- `.replace(old, new)`: Replace occurrences
- `.find(substring)`: Find index of substring
- `.count(substring)`: Count occurrences
- `.startswith(prefix)`: Check if starts with prefix
- `.endswith(suffix)`: Check if ends with suffix

## String Slicing Examples
```python
text = "Python"
text[0]      # 'P' (first character)
text[-1]     # 'n' (last character)
text[0:3]    # 'Pyt' (indices 0, 1, 2)
text[2:]     # 'thon' (from index 2 to end)
text[:4]     # 'Pyth' (from start to index 4)
text[::2]    # 'Pto' (every 2nd character)
text[::-1]   # 'nohtyP' (reversed)
```
