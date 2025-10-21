# Exercise 11: Solution

## Code
```python
# Create initial list
fruits = ['apple', 'banana', 'orange', 'mango', 'grape']
print(f"Original fruits: {fruits}")

# Add two more fruits
fruits.append('kiwi')
fruits.append('pear')
print(f"After adding: {fruits}")

# Remove a fruit
fruits.remove('banana')
print(f"After removing banana: {fruits}")

# Sort the list
fruits.sort()
print(f"Sorted fruits: {fruits}")

# Display length
print(f"Total fruits: {len(fruits)}")
```

## Explanation
- Lists are ordered collections that can hold multiple items
- Square brackets `[]` create a list
- `.append(item)` adds an item to the end of the list
- `.remove(item)` removes the first occurrence of that item
- `.sort()` sorts the list in place (modifies the original list)
- `len(list)` returns the number of items in the list

## Key Concepts
- **Lists**: Mutable, ordered collections of items
- **List methods**: Built-in functions that modify or query lists
- **Indexing**: Access items by position (starting at 0)
- **Mutability**: Lists can be changed after creation

## Common List Methods
- `append(item)`: Add item to end
- `insert(index, item)`: Add item at specific position
- `remove(item)`: Remove first occurrence of item
- `pop()`: Remove and return last item
- `pop(index)`: Remove and return item at index
- `sort()`: Sort list in place
- `reverse()`: Reverse list in place
- `clear()`: Remove all items
- `count(item)`: Count occurrences of item
- `index(item)`: Find index of first occurrence

## List vs sorted()
```python
fruits.sort()        # Modifies the original list
new_list = sorted(fruits)  # Returns a new sorted list
```
