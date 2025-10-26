# Exercise 25: Solution

## Complete Adventure Game Implementation

```python
import time

# Game data structures
rooms = {
    "entrance": {
        "name": "Entrance Hall",
        "description": "A grand entrance with stone pillars. Torches light the dusty room.",
        "exits": {"north": "puzzle", "east": "treasure"},
        "items": ["torch", "rusty key"],
        "visited": False,
        "enemy": None,
        "detail": "Ancient carvings on the walls depict a sun god."
    },
    "puzzle": {
        "name": "Puzzle Room",
        "description": "A dark room with strange symbols on the floor.",
        "exits": {"south": "entrance", "east": "armory"},
        "items": [],
        "visited": False,
        "enemy": None,
        "puzzle_solved": False,
        "detail": "You need light to see the symbols clearly."
    },
    "armory": {
        "name": "Ancient Armory",
        "description": "Weapon racks line the walls. Most are empty.",
        "exits": {"west": "puzzle", "south": "treasure"},
        "items": ["sword"],
        "visited": False,
        "enemy": None,
        "detail": "A single sword remains on the rack, still sharp."
    },
    "treasure": {
        "name": "Treasure Chamber",
        "description": "A magnificent chamber with a pedestal in the center. The Golden Idol sits atop it!",
        "exits": {"west": "entrance", "north": "armory"},
        "items": ["golden idol"],
        "visited": False,
        "enemy": {"name": "Temple Guardian", "health": 50, "attack": 15},
        "detail": "Gold coins are scattered on the floor, but the idol is the real prize."
    }
}

# Item descriptions and effects
items = {
    "torch": {
        "description": "A wooden torch that provides light",
        "usable": True,
        "use_location": "puzzle"
    },
    "rusty key": {
        "description": "An old rusty key, might open something",
        "usable": False
    },
    "golden key": {
        "description": "A shiny golden key",
        "usable": False
    },
    "sword": {
        "description": "A sharp ancient sword that increases attack power",
        "usable": True,
        "use_location": None
    },
    "golden idol": {
        "description": "The legendary Golden Idol!",
        "usable": False
    }
}

# Player state
player = {
    "location": "entrance",
    "inventory": [],
    "health": 100,
    "max_health": 100,
    "score": 0,
    "attack_power": 20,
    "rooms_explored": set(),
    "enemies_defeated": 0
}

# Game state
game_over = False
has_won = False


def print_slow(text, delay=0.03):
    """Print text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def display_intro():
    """Display the game introduction."""
    print("=" * 60)
    print("         ADVENTURE GAME: The Lost Temple")
    print("=" * 60)
    print()
    print("You wake up at the entrance of an ancient temple.")
    print("Your goal: Find the legendary Golden Idol and escape!")
    print()
    print("Commands:")
    print("  go [direction] - Move in a direction (north, south, east, west)")
    print("  take [item]    - Pick up an item")
    print("  use [item]     - Use an item from your inventory")
    print("  look           - Examine your surroundings")
    print("  inventory      - View your items")
    print("  status         - Check your status")
    print("  fight          - Attack an enemy")
    print("  help           - Show this help message")
    print("  quit           - Exit the game")
    print()


def display_room():
    """Display current room information."""
    current_room = rooms[player["location"]]

    print("\n" + "-" * 60)
    print(current_room["name"].upper())
    print("-" * 60)
    print(current_room["description"])

    # Show exits
    exits = ", ".join(current_room["exits"].keys())
    print(f"Exits: {exits}")

    # Show items
    if current_room["items"]:
        items_list = ", ".join(current_room["items"])
        print(f"Items: {items_list}")

    # Show enemy
    if current_room["enemy"]:
        enemy = current_room["enemy"]
        print(f"⚔️  {enemy['name']} (Health: {enemy['health']}) blocks your path!")

    print("-" * 60)


def move(direction):
    """Move player to a new room."""
    current_room = rooms[player["location"]]

    # Check for enemy blocking
    if current_room["enemy"]:
        print(f"The {current_room['enemy']['name']} blocks your path!")
        print("You must defeat it first or flee!")
        return

    # Check if direction is valid
    if direction not in current_room["exits"]:
        print(f"You can't go {direction} from here.")
        return

    # Move to new room
    new_location = current_room["exits"][direction]
    player["location"] = new_location

    # Mark room as visited and add score
    if not rooms[new_location]["visited"]:
        rooms[new_location]["visited"] = True
        player["score"] += 50
        player["rooms_explored"].add(new_location)
        print(f"+50 score for discovering {rooms[new_location]['name']}!")

    # Display new room
    display_room()


def take_item(item_name):
    """Pick up an item from the current room."""
    current_room = rooms[player["location"]]

    # Check if item is in the room
    if item_name not in current_room["items"]:
        print(f"There is no {item_name} here.")
        return

    # Special case for golden idol - need to defeat guardian first
    if item_name == "golden idol" and current_room["enemy"]:
        print("The guardian blocks your path! Defeat it first!")
        return

    # Add to inventory
    player["inventory"].append(item_name)
    current_room["items"].remove(item_name)
    player["score"] += 25
    print(f"You picked up: {item_name}")
    print(f"+25 score!")


def use_item(item_name):
    """Use an item from inventory."""
    # Check if player has the item
    if item_name not in player["inventory"]:
        print(f"You don't have a {item_name}.")
        return

    # Check if item is usable
    if item_name not in items or not items[item_name]["usable"]:
        print(f"You can't use the {item_name} here.")
        return

    current_room = rooms[player["location"]]

    # Torch in puzzle room
    if item_name == "torch" and player["location"] == "puzzle":
        if not current_room.get("puzzle_solved", False):
            print("The torch illuminates the room!")
            print("You can now see a pattern on the floor forming a sun symbol.")
            print("A secret compartment opens, revealing a golden key!")
            current_room["items"].append("golden key")
            current_room["puzzle_solved"] = True
            player["score"] += 100
            print("+100 score for solving the puzzle!")
        else:
            print("You already solved this puzzle.")

    # Sword - permanently increases attack
    elif item_name == "sword":
        if player["attack_power"] == 20:
            player["attack_power"] = 35
            player["inventory"].remove("sword")
            print("You equip the ancient sword!")
            print("Your attack power increased to 35!")
        else:
            print("You're already wielding the sword.")

    else:
        print(f"You can't use the {item_name} here.")


def show_inventory():
    """Display player's inventory."""
    if not player["inventory"]:
        print("\nYour inventory is empty.")
        return

    print("\nYour inventory:")
    for item in player["inventory"]:
        desc = items.get(item, {}).get("description", "No description")
        print(f"  - {item}: {desc}")


def show_status():
    """Display player's current status."""
    print("\n=== Player Status ===")
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Attack Power: {player['attack_power']}")
    print(f"Score: {player['score']}")
    print(f"Items: {len(player['inventory'])}/10")
    print(f"Location: {rooms[player['location']]['name']}")
    print(f"Rooms Explored: {len(player['rooms_explored'])}")
    print(f"Enemies Defeated: {player['enemies_defeated']}")


def combat():
    """Handle combat with an enemy."""
    current_room = rooms[player["location"]]

    if not current_room["enemy"]:
        print("There's nothing to fight here.")
        return

    enemy = current_room["enemy"]

    # Player attacks
    print(f"\nYou attack the {enemy['name']} for {player['attack_power']} damage!")
    enemy["health"] -= player["attack_power"]

    # Check if enemy defeated
    if enemy["health"] <= 0:
        print(f"You defeated the {enemy['name']}!")
        player["score"] += 150
        player["enemies_defeated"] += 1
        current_room["enemy"] = None
        print(f"+150 score!")
        return

    # Enemy attacks back
    print(f"The {enemy['name']} attacks you for {enemy['attack']} damage!")
    player["health"] -= enemy["attack"]
    print(f"Your health: {player['health']}/{player['max_health']}")

    # Check if player died
    if player["health"] <= 0:
        global game_over
        game_over = True
        print("\nYou have been defeated!")


def look():
    """Look around the current room for details."""
    current_room = rooms[player["location"]]

    if "detail" in current_room:
        print(f"\n{current_room['detail']}")

    # Show item descriptions
    if current_room["items"]:
        print("\nYou see:")
        for item in current_room["items"]:
            desc = items.get(item, {}).get("description", "An item")
            print(f"  - {item}: {desc}")


def show_help():
    """Display available commands."""
    print("\nAvailable Commands:")
    print("  go [direction] - Move (north, south, east, west)")
    print("  take [item]    - Pick up an item")
    print("  use [item]     - Use an item")
    print("  look           - Examine surroundings")
    print("  inventory      - View your items")
    print("  status         - Check your status")
    print("  fight          - Attack an enemy")
    print("  help           - Show this message")
    print("  quit           - Exit game")


def process_command(command):
    """Process player's command."""
    # Parse command
    parts = command.lower().strip().split()

    if not parts:
        return

    action = parts[0]

    # One-word commands
    if action == "quit":
        global game_over
        game_over = True
        print("\nThanks for playing!")
        return

    elif action == "help":
        show_help()

    elif action == "look":
        look()

    elif action == "inventory" or action == "inv":
        show_inventory()

    elif action == "status":
        show_status()

    elif action == "fight" or action == "attack":
        combat()

    # Two-word commands
    elif action == "go" or action == "move":
        if len(parts) < 2:
            print("Go where? (north, south, east, west)")
            return
        move(parts[1])

    elif action == "take" or action == "get" or action == "pickup":
        if len(parts) < 2:
            print("Take what?")
            return
        take_item(" ".join(parts[1:]))

    elif action == "use":
        if len(parts) < 2:
            print("Use what?")
            return
        use_item(" ".join(parts[1:]))

    else:
        print("I don't understand that command. Type 'help' for commands.")


def check_win_condition():
    """Check if player has won the game."""
    global has_won, game_over

    # Win if player has golden idol and returns to entrance
    if "golden idol" in player["inventory"] and player["location"] == "entrance":
        has_won = True
        game_over = True


def check_lose_condition():
    """Check if player has lost the game."""
    global game_over

    if player["health"] <= 0:
        game_over = True


def display_end_game():
    """Display end game statistics."""
    print("\n" + "=" * 60)

    if has_won:
        print("           🏆 CONGRATULATIONS! 🏆")
        print("    You escaped with the Golden Idol!")
    else:
        print("              GAME OVER")
        if player["health"] <= 0:
            print("         You have been defeated...")

    print("=" * 60)
    print(f"\nFinal Score: {player['score']}")
    print(f"Items Collected: {len(player['inventory'])}")
    print(f"Rooms Explored: {len(player['rooms_explored'])}")
    print(f"Enemies Defeated: {player['enemies_defeated']}")
    print("\nThanks for playing The Lost Temple!")
    print("=" * 60)


# Main game loop
def main():
    """Main game function."""
    display_intro()

    # Mark starting room as visited
    rooms[player["location"]]["visited"] = True
    player["rooms_explored"].add(player["location"])

    # Display first room
    display_room()

    while not game_over:
        # Get player command
        command = input("\n> ").strip()

        # Process command
        process_command(command)

        # Check win/lose conditions
        check_win_condition()
        check_lose_condition()

    # Display end game statistics
    display_end_game()


# Run the game
if __name__ == "__main__":
    main()
```

## Enhanced Version with Save/Load

```python
import time
import json
import os

# ... (include all the code from above, then add:)

def save_game():
    """Save the current game state to a file."""
    save_data = {
        "player": player,
        "rooms": rooms,
        "game_over": game_over,
        "has_won": has_won
    }

    try:
        with open("savegame.json", "w") as f:
            json.dump(save_data, f, indent=2)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")


def load_game():
    """Load a saved game state."""
    global player, rooms, game_over, has_won

    if not os.path.exists("savegame.json"):
        print("No saved game found.")
        return False

    try:
        with open("savegame.json", "r") as f:
            save_data = json.load(f)

        player = save_data["player"]
        rooms = save_data["rooms"]
        game_over = save_data["game_over"]
        has_won = save_data["has_won"]

        # Convert rooms_explored back to set
        player["rooms_explored"] = set(player["rooms_explored"])

        print("Game loaded successfully!")
        return True
    except Exception as e:
        print(f"Error loading game: {e}")
        return False


# Add to process_command function:
    elif action == "save":
        save_game()

    elif action == "load":
        if load_game():
            display_room()
```

## Key Concepts Explained

### 1. Game State Management
```python
# Player state tracks everything about the player
player = {
    "location": "entrance",
    "inventory": [],
    "health": 100,
    "score": 0
}

# Room state tracks room information
rooms = {
    "entrance": {
        "items": [],
        "exits": {"north": "puzzle"},
        "enemy": None
    }
}
```

### 2. Command Parsing
```python
# Split "go north" into ["go", "north"]
parts = command.split()
action = parts[0]
target = parts[1] if len(parts) > 1 else None
```

### 3. Game Loop Pattern
```python
while not game_over:
    get_input()
    process_input()
    update_game_state()
    check_win_lose_conditions()
```

### 4. State Checking
```python
# Check if item is in room
if item_name in current_room["items"]:
    # Player can take it

# Check if enemy is defeated
if enemy["health"] <= 0:
    # Remove enemy
```

## Design Patterns

### 1. Command Pattern
Each command has its own function:
- `move()` - handles movement
- `take_item()` - handles item pickup
- `combat()` - handles fighting

### 2. State Pattern
Game state determines available actions:
- Can't take idol if enemy present
- Can't use torch except in puzzle room
- Can't leave room if enemy blocks

### 3. Data-Driven Design
Game content in dictionaries, not hard-coded:
```python
rooms = {...}  # Easy to add new rooms
items = {...}  # Easy to add new items
```

## Extension Ideas

### 1. Random Encounters
```python
import random

def check_random_encounter():
    if random.random() < 0.3:  # 30% chance
        print("A goblin appears!")
        return {"name": "Goblin", "health": 30, "attack": 10}
    return None
```

### 2. Dialogue System
```python
npcs = {
    "wizard": {
        "dialogue": [
            "Greetings, adventurer!",
            "Beware the guardian!",
            "May fortune favor you."
        ],
        "current_line": 0
    }
}

def talk_to_npc(npc_name):
    npc = npcs[npc_name]
    print(npc["dialogue"][npc["current_line"]])
    npc["current_line"] = (npc["current_line"] + 1) % len(npc["dialogue"])
```

### 3. Item Crafting
```python
recipes = {
    "magic_sword": {
        "requires": ["sword", "magic_gem"],
        "creates": "magic_sword",
        "description": "A sword imbued with magic!"
    }
}

def craft_item(recipe_name):
    recipe = recipes[recipe_name]
    if all(item in player["inventory"] for item in recipe["requires"]):
        for item in recipe["requires"]:
            player["inventory"].remove(item)
        player["inventory"].append(recipe["creates"])
        print(f"You crafted a {recipe['creates']}!")
```

### 4. Experience and Leveling
```python
player["exp"] = 0
player["level"] = 1

def gain_exp(amount):
    player["exp"] += amount
    exp_needed = player["level"] * 100

    if player["exp"] >= exp_needed:
        player["level"] += 1
        player["max_health"] += 20
        player["health"] = player["max_health"]
        player["attack_power"] += 5
        print(f"Level up! You are now level {player['level']}!")
```

## Testing Checklist

- [ ] All rooms are accessible
- [ ] All items can be collected
- [ ] Combat system works correctly
- [ ] Win condition works
- [ ] Lose condition works
- [ ] Commands are parsed correctly
- [ ] Invalid commands don't crash
- [ ] Game state updates properly
- [ ] Score calculates correctly

## Common Mistakes to Avoid

1. **Not checking if item exists before using**
   ```python
   # Wrong
   item_desc = items[item_name]["description"]  # KeyError if not exists

   # Right
   item_desc = items.get(item_name, {}).get("description", "Unknown")
   ```

2. **Forgetting to update game state**
   ```python
   # Remember to:
   current_room["enemy"] = None  # After defeat
   current_room["items"].remove(item)  # After taking
   player["location"] = new_room  # After moving
   ```

3. **Not handling edge cases**
   ```python
   # Check for empty inventory
   if not player["inventory"]:
       print("Inventory empty")
       return

   # Check for valid direction
   if direction not in room["exits"]:
       print("Can't go that way")
       return
   ```

This project demonstrates mastery of:
- Data structures (dictionaries, lists, sets)
- Functions and code organization
- Control flow (loops, conditionals)
- String manipulation
- Game logic and state management
- User input handling
- Error handling

It's a perfect capstone project for Python beginners!
