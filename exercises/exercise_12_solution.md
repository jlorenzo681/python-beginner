# Exercise 12: Solution

## Code
```python
shopping_list = []

while True:
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for index, item in enumerate(shopping_list, 1):
                print(f"{index}. {item}")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for index, item in enumerate(shopping_list, 1):
                print(f"{index}. {item}")

            item_num = int(input("Enter item number to remove: "))
            if 1 <= item_num <= len(shopping_list):
                removed = shopping_list.pop(item_num - 1)
                print(f"{removed} removed from the list.")
            else:
                print("Invalid item number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-4.")
```

## Explanation
- We use `while True:` to create an infinite loop
- The `break` statement exits the loop when user chooses to quit
- `enumerate(list, start)` gives us both index and value in a loop
- We check if the list is empty before trying to display or remove items
- `pop(index)` removes and returns the item at the specified index
- List indices start at 0, but we display starting from 1 for users

## Key Concepts
- **while True loop**: Runs indefinitely until break is called
- **break statement**: Exits the current loop
- **enumerate()**: Iterates with both index and value
- **List indexing**: Accessing items by position (0-based)
- **Input validation**: Checking if user input is valid

## Common Patterns
```python
# Check if list is empty
if len(my_list) == 0:
    # or: if not my_list:

# Iterate with index
for index, value in enumerate(my_list):
    print(f"{index}: {value}")

# Infinite loop with exit condition
while True:
    if some_condition:
        break
```

## Alternative: Remove by name
```python
elif choice == "3":
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed.")
    else:
        print(f"{item} not found in list.")
```
