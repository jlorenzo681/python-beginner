# Exercise 17: File Operations - Simple Note Taker

## Difficulty: Advanced

## Description
Create a simple note-taking program that can save notes to a file and read them back.

## Learning Objectives
- Learn to write to files
- Learn to read from files
- Practice file handling with context managers
- Understand persistence of data

## Requirements
- Create a menu with options: Add note, View notes, Quit
- When adding a note, append it to a file called `notes.txt`
- When viewing notes, read and display all notes from the file
- Use proper file handling (with statement)
- Handle the case when the file doesn't exist yet

## Expected Output
```
Simple Note Taker
1. Add note
2. View notes
3. Quit
Choose an option: 1
Enter your note: Buy groceries
Note saved!

Choose an option: 1
Enter your note: Call dentist
Note saved!

Choose an option: 2
Your notes:
1. Buy groceries
2. Call dentist

Choose an option: 3
Goodbye!
```

## Hints
- Use `with open(filename, mode) as file:` for file operations
- Mode 'a' appends to file, 'r' reads from file
- Use `file.write()` to write to file
- Use `file.readlines()` to read all lines
- Handle `FileNotFoundError` exception when reading
