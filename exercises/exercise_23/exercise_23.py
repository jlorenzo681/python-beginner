# Exercise 23: Shopping List Manager
# Objective: Create a comprehensive shopping list manager with multiple features

# Hint: Use a list to store items
# Hint: Each item is a dictionary with keys: name, quantity, price, purchased
# Hint: Create separate functions for each operation
# Hint: Use while True loop for menu
# Hint: Format output with f-strings and proper alignment

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
    # Get item name, quantity, and price from user
    # Validate input (quantity > 0, price >= 0)
    # Create dictionary with name, quantity, price, purchased=False
    # Append to shopping_list
    # Display confirmation
    pass


def remove_item():
    """Remove an item from the shopping list."""
    # Get item name from user
    # Search for item in list
    # If found, remove it
    # Display confirmation or error message
    pass


def view_list():
    """Display all items in formatted table."""
    # Check if list is empty
    # Display header
    # Loop through items and display with formatting
    # Show total items and total cost
    pass


def mark_purchased():
    """Mark an item as purchased or unpurchased."""
    # Get item name from user
    # Search for item
    # Toggle purchased status
    # Display confirmation
    pass


def search_item():
    """Search for an item in the list."""
    # Get search term from user
    # Search through list (case-insensitive)
    # Display matching items or "not found" message
    pass


def show_statistics():
    """Display statistics about the shopping list."""
    # Calculate total items, purchased items, remaining items
    # Calculate total cost and average price
    # Display all statistics
    pass


def clear_list():
    """Clear the entire shopping list."""
    # Ask for confirmation
    # Clear the list
    # Display confirmation
    pass


# Main program loop
while True:
    display_menu()

    # Get user choice


    # Call appropriate function based on choice


    # Handle invalid choice
