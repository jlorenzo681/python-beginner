# Exercise 23: Shopping List Manager

## Difficulty: Advanced+

## Description
Create a comprehensive shopping list manager that allows users to add items with quantities, remove items, view the list, mark items as purchased, and calculate total items.

## Learning Objectives
- Work with lists of dictionaries
- Implement CRUD operations (Create, Read, Update, Delete)
- Build a menu-driven application
- Practice data validation and error handling
- Format output in a user-friendly way

## Requirements
- Display a menu with multiple options
- Add items with name, quantity, and price
- Remove items by name
- View all items in a formatted table
- Mark items as purchased/unpurchased
- Show total number of items and total cost
- Search for items
- Clear the entire list
- Validate all user input
- Use a loop to keep the program running until user quits

## Expected Output
```
===== SHOPPING LIST MANAGER =====

1. Add item
2. Remove item
3. View shopping list
4. Mark item as purchased
5. Search for item
6. Show statistics
7. Clear list
8. Quit

Choose an option: 1
Item name: Apples
Quantity: 6
Price per unit: 0.50
Added: Apples (6 @ $0.50 each)

Choose an option: 3
Shopping List:
----------------------------------------
#  | Item      | Qty | Price   | Status
----------------------------------------
1  | Apples    | 6   | $3.00   | [ ]
2  | Bread     | 2   | $5.00   | [✓]
3  | Milk      | 1   | $3.50   | [ ]
----------------------------------------
Total Items: 3 | Total Cost: $11.50

Choose an option: 6
Statistics:
- Total items: 3
- Items purchased: 1
- Items remaining: 2
- Total cost: $11.50
- Average price: $3.83

Choose an option: 8
Goodbye!
```

## Hints
- Use a list to store items: `shopping_list = []`
- Each item is a dictionary: `{"name": "Apples", "quantity": 6, "price": 0.50, "purchased": False}`
- Use a while loop for the main menu
- Use functions for each operation (add_item, remove_item, etc.)
- Use f-strings for formatted output
- Use enumerate() when displaying numbered lists

## Challenge
Add these advanced features:
1. Save shopping list to a file
2. Load shopping list from a file
3. Sort items by name, price, or quantity
4. Export to CSV format
5. Add categories to items
