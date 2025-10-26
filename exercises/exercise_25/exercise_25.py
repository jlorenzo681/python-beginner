# Exercise 25: Text-Based Adventure Game
# Objective: Create a comprehensive adventure game combining multiple Python concepts

# Hint: Use a dictionary for rooms with description, exits, items, enemies
# Hint: Use a list for inventory
# Hint: Create helper functions for each action (move, take, use, fight, etc.)
# Hint: Use a main loop that processes commands
# Hint: Track game state with variables (current location, health, score)
# Hint: Use .split() to parse commands like "go north" into ["go", "north"]

# Game data structures
rooms = {
    "entrance": {
        "name": "Entrance Hall",
        "description": "A grand entrance with stone pillars. Torches light the dusty room.",
        "exits": {"north": "puzzle", "east": "treasure"},
        "items": ["torch", "rusty key"],
        "visited": False,
        "enemy": None
    },
    # Add more rooms here
}

# Item descriptions
items = {
    "torch": "A wooden torch that provides light",
    "rusty key": "An old rusty key, might open something",
    "golden key": "A shiny golden key",
    "golden idol": "The legendary Golden Idol!"
}

# Player state
player = {
    "location": "entrance",
    "inventory": [],
    "health": 100,
    "max_health": 100,
    "score": 0,
    "attack_power": 20
}

# Game state
game_over = False
has_won = False


def display_intro():
    """Display the game introduction."""
    # Print game title and story
    # Explain objective
    # List available commands
    pass


def display_room():
    """Display current room information."""
    # Get current room
    # Print room name and description
    # Print available exits
    # Print items in room
    # Print enemy if present
    pass


def move(direction):
    """Move player to a new room."""
    # Check if direction is valid
    # Update player location
    # Mark room as visited
    # Add score if first visit
    # Display new room
    pass


def take_item(item_name):
    """Pick up an item from the current room."""
    # Check if item is in room
    # Add to inventory
    # Remove from room
    # Update score
    pass


def use_item(item_name):
    """Use an item from inventory."""
    # Check if item is in inventory
    # Implement item-specific effects
    # Some items unlock areas or solve puzzles
    pass


def show_inventory():
    """Display player's inventory."""
    # List all items in inventory with descriptions
    pass


def show_status():
    """Display player's current status."""
    # Show health, score, location, item count
    pass


def combat(enemy):
    """Handle combat with an enemy."""
    # Player attacks enemy
    # Enemy attacks player
    # Check if enemy or player defeated
    # Update score if enemy defeated
    pass


def look():
    """Look around the current room for details."""
    # Provide additional room details
    # Show hidden information
    pass


def show_help():
    """Display available commands."""
    # List all commands and what they do
    pass


def process_command(command):
    """Process player's command."""
    # Parse command
    # Call appropriate function
    # Handle invalid commands
    pass


def check_win_condition():
    """Check if player has won the game."""
    # Check if player has golden idol and is at entrance
    pass


def check_lose_condition():
    """Check if player has lost the game."""
    # Check if player health <= 0
    pass


# Main game loop
def main():
    """Main game function."""
    display_intro()

    global game_over, has_won

    while not game_over:
        # Display current room


        # Get player command


        # Process command


        # Check win/lose conditions


    # Display end game message and statistics


# Run the game
if __name__ == "__main__":
    main()
