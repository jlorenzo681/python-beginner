# Exercise 22: Simple Caesar Cipher

## Difficulty: Advanced

## Description
Create a program that encrypts and decrypts messages using the Caesar cipher, a simple encryption technique where each letter is shifted by a fixed number of positions in the alphabet.

## Learning Objectives
- Practice string manipulation with character operations
- Understand ASCII values and character encoding
- Work with the alphabet and modular arithmetic
- Implement encryption and decryption logic
- Create a menu-driven program

## Requirements
- Ask the user to choose: encrypt, decrypt, or quit
- For encryption: get message and shift value, then encrypt it
- For decryption: get encrypted message and shift value, then decrypt it
- Preserve spaces and punctuation (don't encrypt them)
- Handle both uppercase and lowercase letters
- Support shift values from 1 to 25
- Use a menu system with a loop

## Expected Output
```
Caesar Cipher Program
1. Encrypt a message
2. Decrypt a message
3. Quit

Choose an option: 1
Enter message to encrypt: Hello World
Enter shift value (1-25): 3
Encrypted message: Khoor Zruog

Caesar Cipher Program
1. Encrypt a message
2. Decrypt a message
3. Quit

Choose an option: 2
Enter message to decrypt: Khoor Zruog
Enter shift value (1-25): 3
Decrypted message: Hello World

Choose an option: 3
Goodbye!
```

## Hints
- The alphabet has 26 letters
- Use `ord()` to get ASCII value of a character
- Use `chr()` to convert ASCII value back to a character
- For uppercase: 'A' has ASCII value 65, 'Z' is 90
- For lowercase: 'a' has ASCII value 97, 'z' is 122
- Use modulo (%) to wrap around the alphabet: `(position + shift) % 26`
- To decrypt, shift in the opposite direction (subtract instead of add)
- Use `.isalpha()` to check if a character is a letter

## Challenge
Add these advanced features:
1. Auto-detect if input is likely encrypted (frequency analysis hint)
2. Brute force mode that tries all 25 possible shifts
3. Handle punctuation and numbers properly
4. Create a reverse cipher option
