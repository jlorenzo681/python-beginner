# Exercise 15: Solution

## Code
```python
sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Count word frequencies
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display frequencies
print("\nWord frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Find most common word
most_common = max(word_count, key=word_count.get)
max_count = word_count[most_common]
print(f'\nMost common word: "{most_common}" (appears {max_count} times)')
```

## Alternative Solution (using .get())
```python
sentence = input("Enter a sentence: ")
words = sentence.lower().split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

most_common = max(word_count, key=word_count.get)
print(f'\nMost common word: "{most_common}" (appears {word_count[most_common]} times)')
```

## Explanation
- We convert to lowercase so "The" and "the" are counted as the same word
- `.split()` breaks the sentence into a list of individual words
- We use a dictionary to track counts (word: count)
- For each word, we check if it exists and increment its count
- The `.get(word, 0)` method returns the current count or 0 if word doesn't exist
- `max(dict, key=dict.get)` finds the key with the highest value

## Key Concepts
- **Frequency counting**: Common pattern for counting occurrences
- **Dictionary accumulation**: Building up data in a dictionary
- **String processing**: Cleaning and splitting text
- **Method chaining**: `.lower().split()` applies multiple methods

## Common Patterns

### Frequency Counting Pattern
```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```

### Finding Min/Max by Value
```python
max_key = max(dictionary, key=dictionary.get)
min_key = min(dictionary, key=dictionary.get)
```

## Using Counter (Advanced)
```python
from collections import Counter

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

word_count = Counter(words)
print(dict(word_count))

most_common = word_count.most_common(1)[0]
print(f'Most common: "{most_common[0]}" ({most_common[1]} times)')
```
