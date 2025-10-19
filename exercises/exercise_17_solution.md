# Exercise 17: Solution

## Code
```python
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()

        if notes:
            print("\nYour notes:")
            for index, note in enumerate(notes, 1):
                print(f"{index}. {note.strip()}")
        else:
            print("No notes yet.")

    except FileNotFoundError:
        print("No notes yet.")

# Main program
while True:
    print("\nSimple Note Taker")
    print("1. Add note")
    print("2. View notes")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
```

## Explanation
- `with open(filename, mode) as file:` is the context manager syntax
- The `with` statement automatically closes the file when done
- Mode 'a' (append) adds to the end without erasing existing content
- Mode 'r' (read) opens the file for reading
- `readlines()` returns a list of all lines (each line includes `\n`)
- `.strip()` removes the newline character when displaying
- `try/except` catches the error when file doesn't exist

## Key Concepts
- **File I/O**: Reading from and writing to files
- **Context managers**: Using `with` for automatic resource management
- **File modes**: 'r' (read), 'w' (write/overwrite), 'a' (append)
- **Exception handling**: try/except for error handling
- **Persistence**: Data survives after program ends

## File Modes
- `'r'`: Read (default) - file must exist
- `'w'`: Write - creates new file or overwrites existing
- `'a'`: Append - creates new file or adds to existing
- `'r+'`: Read and write
- `'rb'`: Read binary
- `'wb'`: Write binary

## File Operations
```python
# Writing
with open("file.txt", "w") as f:
    f.write("text\n")
    f.writelines(["line1\n", "line2\n"])

# Reading
with open("file.txt", "r") as f:
    content = f.read()           # Entire file as string
    lines = f.readlines()        # List of lines
    line = f.readline()          # One line at a time

# Appending
with open("file.txt", "a") as f:
    f.write("more text\n")
```

## Why use `with`?
```python
# Without with (not recommended)
file = open("file.txt", "r")
content = file.read()
file.close()  # Easy to forget!

# With 'with' (recommended)
with open("file.txt", "r") as file:
    content = file.read()
# File automatically closed
```

## Enhanced Version with Error Handling
```python
def add_note():
    note = input("Enter your note: ")
    try:
        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("Note saved!")
    except IOError as e:
        print(f"Error saving note: {e}")
```
