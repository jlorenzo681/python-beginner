# Exercise 12: Shopping List Manager

## Difficulty: Intermediate

## Description
Create an interactive shopping list program that allows users to add, view, and remove items.

## Learning Objectives
- Work with lists dynamically
- Use loops with lists
- Practice user interaction patterns

## Requirements
- Create a menu with options: Add item, View list, Remove item, Quit
- Use a while loop to keep the program running
- Store items in a list
- Display the list with numbered items

## Expected Output
```
Shopping List Manager
1. Add item
2. View list
3. Remove item
4. Quit
Choose an option: 1
Enter item to add: milk
milk added to the list.

Choose an option: 1
Enter item to add: bread
bread added to the list.

Choose an option: 2
Your shopping list:
1. milk
2. bread

Choose an option: 4
Goodbye!
```

## Hints
- Use a while loop with a condition like `while True:` and `break` to exit
- Use a list to store items
- Use `enumerate()` to get index and value when displaying
- Check if list is empty before displaying or removing
