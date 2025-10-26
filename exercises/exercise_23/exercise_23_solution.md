# Exercise 23: Solution

## Solution 1: Complete Implementation
```python
shopping_list = []


def display_menu():
    """Display the main menu."""
    print("\n===== SHOPPING LIST MANAGER =====\n")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Mark item as purchased")
    print("5. Search for item")
    print("6. Show statistics")
    print("7. Clear list")
    print("8. Quit")


def add_item():
    """Add a new item to the shopping list."""
    try:
        name = input("\nItem name: ").strip()
        if not name:
            print("Item name cannot be empty!")
            return

        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0!")
            return

        price = float(input("Price per unit: "))
        if price < 0:
            print("Price cannot be negative!")
            return

        item = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "purchased": False
        }

        shopping_list.append(item)
        total_price = quantity * price
        print(f"Added: {name} ({quantity} @ ${price:.2f} each = ${total_price:.2f})")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


def remove_item():
    """Remove an item from the shopping list."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    name = input("\nEnter item name to remove: ").strip()

    for item in shopping_list:
        if item["name"].lower() == name.lower():
            shopping_list.remove(item)
            print(f"Removed: {item['name']}")
            return

    print(f"Item '{name}' not found!")


def view_list():
    """Display all items in formatted table."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    print("\nShopping List:")
    print("-" * 60)
    print(f"{'#':<3} | {'Item':<15} | {'Qty':<4} | {'Price':<8} | Status")
    print("-" * 60)

    total_cost = 0
    for i, item in enumerate(shopping_list, 1):
        item_total = item["quantity"] * item["price"]
        total_cost += item_total
        status = "[✓]" if item["purchased"] else "[ ]"

        print(f"{i:<3} | {item['name']:<15} | {item['quantity']:<4} | "
              f"${item_total:<7.2f} | {status}")

    print("-" * 60)
    print(f"Total Items: {len(shopping_list)} | Total Cost: ${total_cost:.2f}")


def mark_purchased():
    """Mark an item as purchased or unpurchased."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    name = input("\nEnter item name: ").strip()

    for item in shopping_list:
        if item["name"].lower() == name.lower():
            item["purchased"] = not item["purchased"]
            status = "purchased" if item["purchased"] else "unpurchased"
            print(f"Marked '{item['name']}' as {status}")
            return

    print(f"Item '{name}' not found!")


def search_item():
    """Search for an item in the list."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    search_term = input("\nEnter search term: ").strip().lower()
    found_items = []

    for item in shopping_list:
        if search_term in item["name"].lower():
            found_items.append(item)

    if found_items:
        print(f"\nFound {len(found_items)} item(s):")
        for item in found_items:
            status = "✓" if item["purchased"] else " "
            total = item["quantity"] * item["price"]
            print(f"  [{status}] {item['name']}: {item['quantity']} @ "
                  f"${item['price']:.2f} = ${total:.2f}")
    else:
        print(f"No items found matching '{search_term}'")


def show_statistics():
    """Display statistics about the shopping list."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    total_items = len(shopping_list)
    purchased_items = sum(1 for item in shopping_list if item["purchased"])
    remaining_items = total_items - purchased_items

    total_cost = sum(item["quantity"] * item["price"] for item in shopping_list)
    average_price = total_cost / total_items if total_items > 0 else 0

    print("\nStatistics:")
    print(f"- Total items: {total_items}")
    print(f"- Items purchased: {purchased_items}")
    print(f"- Items remaining: {remaining_items}")
    print(f"- Total cost: ${total_cost:.2f}")
    print(f"- Average cost per item: ${average_price:.2f}")


def clear_list():
    """Clear the entire shopping list."""
    if not shopping_list:
        print("\nShopping list is already empty!")
        return

    confirm = input("\nAre you sure you want to clear the entire list? (yes/no): ")
    if confirm.lower() == 'yes':
        shopping_list.clear()
        print("Shopping list cleared!")
    else:
        print("Clear cancelled.")


# Main program loop
while True:
    display_menu()

    choice = input("\nChoose an option: ").strip()

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_list()
    elif choice == '4':
        mark_purchased()
    elif choice == '5':
        search_item()
    elif choice == '6':
        show_statistics()
    elif choice == '7':
        clear_list()
    elif choice == '8':
        print("\nGoodbye!")
        break
    else:
        print("Invalid option! Please choose 1-8.")
```

## Solution 2: Enhanced with File Persistence
```python
import json

shopping_list = []
FILENAME = "shopping_list.json"


def save_to_file():
    """Save shopping list to a file."""
    try:
        with open(FILENAME, 'w') as f:
            json.dump(shopping_list, f, indent=2)
        print("Shopping list saved!")
    except Exception as e:
        print(f"Error saving file: {e}")


def load_from_file():
    """Load shopping list from a file."""
    global shopping_list
    try:
        with open(FILENAME, 'r') as f:
            shopping_list = json.load(f)
        print(f"Loaded {len(shopping_list)} items from file!")
    except FileNotFoundError:
        print("No saved shopping list found.")
    except Exception as e:
        print(f"Error loading file: {e}")


def display_menu():
    """Display the main menu."""
    print("\n===== SHOPPING LIST MANAGER =====\n")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Mark item as purchased")
    print("5. Search for item")
    print("6. Show statistics")
    print("7. Sort items")
    print("8. Clear list")
    print("9. Save to file")
    print("10. Load from file")
    print("11. Quit")


def add_item():
    """Add a new item to the shopping list."""
    try:
        name = input("\nItem name: ").strip()
        if not name:
            print("Item name cannot be empty!")
            return

        # Check for duplicates
        for item in shopping_list:
            if item["name"].lower() == name.lower():
                print(f"'{name}' already exists in the list!")
                update = input("Update quantity and price? (yes/no): ")
                if update.lower() == 'yes':
                    quantity = int(input("New quantity: "))
                    price = float(input("New price per unit: "))
                    if quantity > 0 and price >= 0:
                        item["quantity"] = quantity
                        item["price"] = price
                        print(f"Updated: {name}")
                return

        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0!")
            return

        price = float(input("Price per unit: "))
        if price < 0:
            print("Price cannot be negative!")
            return

        category = input("Category (optional): ").strip()

        item = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "purchased": False,
            "category": category if category else "Uncategorized"
        }

        shopping_list.append(item)
        total_price = quantity * price
        print(f"Added: {name} ({quantity} @ ${price:.2f} each = ${total_price:.2f})")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


def remove_item():
    """Remove an item from the shopping list."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    name = input("\nEnter item name to remove: ").strip()

    for item in shopping_list:
        if item["name"].lower() == name.lower():
            shopping_list.remove(item)
            print(f"Removed: {item['name']}")
            return

    print(f"Item '{name}' not found!")


def view_list():
    """Display all items in formatted table."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    print("\nShopping List:")
    print("-" * 75)
    print(f"{'#':<3} | {'Item':<15} | {'Qty':<4} | {'Price':<8} | {'Category':<12} | Status")
    print("-" * 75)

    total_cost = 0
    for i, item in enumerate(shopping_list, 1):
        item_total = item["quantity"] * item["price"]
        total_cost += item_total
        status = "[✓]" if item["purchased"] else "[ ]"
        category = item.get("category", "Uncategorized")

        print(f"{i:<3} | {item['name']:<15} | {item['quantity']:<4} | "
              f"${item_total:<7.2f} | {category:<12} | {status}")

    print("-" * 75)
    print(f"Total Items: {len(shopping_list)} | Total Cost: ${total_cost:.2f}")


def mark_purchased():
    """Mark an item as purchased or unpurchased."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    name = input("\nEnter item name: ").strip()

    for item in shopping_list:
        if item["name"].lower() == name.lower():
            item["purchased"] = not item["purchased"]
            status = "purchased" if item["purchased"] else "unpurchased"
            print(f"Marked '{item['name']}' as {status}")
            return

    print(f"Item '{name}' not found!")


def search_item():
    """Search for an item in the list."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    search_term = input("\nEnter search term: ").strip().lower()
    found_items = []

    for item in shopping_list:
        if (search_term in item["name"].lower() or
            search_term in item.get("category", "").lower()):
            found_items.append(item)

    if found_items:
        print(f"\nFound {len(found_items)} item(s):")
        for item in found_items:
            status = "✓" if item["purchased"] else " "
            total = item["quantity"] * item["price"]
            category = item.get("category", "Uncategorized")
            print(f"  [{status}] {item['name']} ({category}): {item['quantity']} @ "
                  f"${item['price']:.2f} = ${total:.2f}")
    else:
        print(f"No items found matching '{search_term}'")


def show_statistics():
    """Display statistics about the shopping list."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    total_items = len(shopping_list)
    purchased_items = sum(1 for item in shopping_list if item["purchased"])
    remaining_items = total_items - purchased_items

    total_cost = sum(item["quantity"] * item["price"] for item in shopping_list)
    average_price = total_cost / total_items if total_items > 0 else 0

    # Category statistics
    categories = {}
    for item in shopping_list:
        cat = item.get("category", "Uncategorized")
        categories[cat] = categories.get(cat, 0) + 1

    print("\nStatistics:")
    print(f"- Total items: {total_items}")
    print(f"- Items purchased: {purchased_items}")
    print(f"- Items remaining: {remaining_items}")
    print(f"- Total cost: ${total_cost:.2f}")
    print(f"- Average cost per item: ${average_price:.2f}")
    print("\nItems by category:")
    for cat, count in sorted(categories.items()):
        print(f"  - {cat}: {count}")


def sort_items():
    """Sort items by different criteria."""
    if not shopping_list:
        print("\nShopping list is empty!")
        return

    print("\nSort by:")
    print("1. Name (A-Z)")
    print("2. Name (Z-A)")
    print("3. Price (Low to High)")
    print("4. Price (High to Low)")
    print("5. Quantity")

    choice = input("\nChoose sorting option: ").strip()

    if choice == '1':
        shopping_list.sort(key=lambda x: x["name"].lower())
        print("Sorted by name (A-Z)")
    elif choice == '2':
        shopping_list.sort(key=lambda x: x["name"].lower(), reverse=True)
        print("Sorted by name (Z-A)")
    elif choice == '3':
        shopping_list.sort(key=lambda x: x["price"])
        print("Sorted by price (Low to High)")
    elif choice == '4':
        shopping_list.sort(key=lambda x: x["price"], reverse=True)
        print("Sorted by price (High to Low)")
    elif choice == '5':
        shopping_list.sort(key=lambda x: x["quantity"], reverse=True)
        print("Sorted by quantity")
    else:
        print("Invalid option!")


def clear_list():
    """Clear the entire shopping list."""
    if not shopping_list:
        print("\nShopping list is already empty!")
        return

    confirm = input("\nAre you sure you want to clear the entire list? (yes/no): ")
    if confirm.lower() == 'yes':
        shopping_list.clear()
        print("Shopping list cleared!")
    else:
        print("Clear cancelled.")


# Main program
print("Welcome to Shopping List Manager!")
load_from_file()

while True:
    display_menu()

    choice = input("\nChoose an option: ").strip()

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_list()
    elif choice == '4':
        mark_purchased()
    elif choice == '5':
        search_item()
    elif choice == '6':
        show_statistics()
    elif choice == '7':
        sort_items()
    elif choice == '8':
        clear_list()
    elif choice == '9':
        save_to_file()
    elif choice == '10':
        load_from_file()
    elif choice == '11':
        print("\nSave before quitting?")
        if input("(yes/no): ").lower() == 'yes':
            save_to_file()
        print("Goodbye!")
        break
    else:
        print("Invalid option! Please choose 1-11.")
```

## Explanation

### Key Concepts

1. **Data Structure**
   ```python
   # Each item is a dictionary
   item = {
       "name": "Apples",
       "quantity": 6,
       "price": 0.50,
       "purchased": False
   }

   # All items stored in a list
   shopping_list = [item1, item2, item3]
   ```

2. **CRUD Operations**
   - **Create**: Add new items to the list
   - **Read**: View and search items
   - **Update**: Mark items as purchased, change quantities
   - **Delete**: Remove items from the list

3. **List Comprehensions for Statistics**
   ```python
   # Count purchased items
   purchased = sum(1 for item in shopping_list if item["purchased"])

   # Calculate total cost
   total = sum(item["quantity"] * item["price"] for item in shopping_list)
   ```

4. **Formatted Output**
   ```python
   # Left-aligned with width 15
   print(f"{item['name']:<15}")

   # Right-aligned with width 8, 2 decimals
   print(f"${price:>8.2f}")
   ```

5. **File Operations (JSON)**
   ```python
   # Save to file
   with open('file.json', 'w') as f:
       json.dump(data, f, indent=2)

   # Load from file
   with open('file.json', 'r') as f:
       data = json.load(f)
   ```

## Common Patterns

1. **Checking if list is empty**
   ```python
   if not shopping_list:
       print("List is empty!")
       return
   ```

2. **Finding an item**
   ```python
   for item in shopping_list:
       if item["name"].lower() == search_name.lower():
           # Found it!
           break
   else:
       # Not found (else clause of for loop)
       print("Not found!")
   ```

3. **Toggle boolean**
   ```python
   item["purchased"] = not item["purchased"]
   ```

## Extensions Ideas

1. **Export to CSV**
   ```python
   import csv
   with open('shopping.csv', 'w', newline='') as f:
       writer = csv.DictWriter(f, fieldnames=["name", "quantity", "price"])
       writer.writeheader()
       writer.writerows(shopping_list)
   ```

2. **Budget tracking**
   ```python
   budget = 100.00
   total_cost = sum(item["quantity"] * item["price"] for item in shopping_list)
   remaining = budget - total_cost
   print(f"Budget: ${budget:.2f}")
   print(f"Remaining: ${remaining:.2f}")
   ```

3. **Shopping history**
   ```python
   # Track when items were purchased
   import datetime
   item["purchased_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
   ```
