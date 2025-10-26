# Exercise 22: Solution

## Solution 1: Basic Version
```python
def encrypt(message, shift):
    """Encrypt a message using Caesar cipher."""
    encrypted = ""

    for char in message:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                # Shift within uppercase range (A-Z)
                shifted = ord(char) - ord('A')
                shifted = (shifted + shift) % 26
                encrypted += chr(shifted + ord('A'))
            # Handle lowercase letters
            else:
                # Shift within lowercase range (a-z)
                shifted = ord(char) - ord('a')
                shifted = (shifted + shift) % 26
                encrypted += chr(shifted + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            encrypted += char

    return encrypted


def decrypt(message, shift):
    """Decrypt a message using Caesar cipher."""
    # Decryption is encryption with negative shift
    return encrypt(message, -shift)


# Main program
while True:
    print("\nCaesar Cipher Program")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Quit")

    choice = input("\nChoose an option: ")

    if choice == '1':
        message = input("Enter message to encrypt: ")
        shift = int(input("Enter shift value (1-25): "))
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")

    elif choice == '2':
        message = input("Enter message to decrypt: ")
        shift = int(input("Enter shift value (1-25): "))
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1, 2, or 3.")
```

## Solution 2: Enhanced with Input Validation
```python
def encrypt(message, shift):
    """Encrypt a message using Caesar cipher."""
    encrypted = ""
    shift = shift % 26  # Handle shifts larger than 26

    for char in message:
        if char.isalpha():
            if char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26
                encrypted += chr(shifted + ord('A'))
            else:
                shifted = (ord(char) - ord('a') + shift) % 26
                encrypted += chr(shifted + ord('a'))
        else:
            encrypted += char

    return encrypted


def decrypt(message, shift):
    """Decrypt a message using Caesar cipher."""
    return encrypt(message, -shift)


def get_shift_value():
    """Get a valid shift value from user."""
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a value between 1 and 25.")
        except ValueError:
            print("Invalid input! Please enter a number.")


# Main program
print("=" * 40)
print("     CAESAR CIPHER PROGRAM")
print("=" * 40)

while True:
    print("\nOptions:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Quit")

    choice = input("\nChoose an option (1-3): ")

    if choice == '1':
        message = input("Enter message to encrypt: ")
        if not message:
            print("Message cannot be empty!")
            continue
        shift = get_shift_value()
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")

    elif choice == '2':
        message = input("Enter message to decrypt: ")
        if not message:
            print("Message cannot be empty!")
            continue
        shift = get_shift_value()
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")

    elif choice == '3':
        print("\nThanks for using Caesar Cipher!")
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1, 2, or 3.")
```

## Solution 3: Advanced with Brute Force
```python
def encrypt(message, shift):
    """Encrypt a message using Caesar cipher."""
    encrypted = ""
    shift = shift % 26

    for char in message:
        if char.isalpha():
            if char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26
                encrypted += chr(shifted + ord('A'))
            else:
                shifted = (ord(char) - ord('a') + shift) % 26
                encrypted += chr(shifted + ord('a'))
        else:
            encrypted += char

    return encrypted


def decrypt(message, shift):
    """Decrypt a message using Caesar cipher."""
    return encrypt(message, -shift)


def brute_force(message):
    """Try all possible shifts and display results."""
    print("\nTrying all possible shifts:\n")
    print("Shift | Decrypted Message")
    print("-" * 50)

    for shift in range(1, 26):
        decrypted = decrypt(message, shift)
        print(f"{shift:2d}    | {decrypted}")


def get_shift_value():
    """Get a valid shift value from user."""
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a value between 1 and 25.")
        except ValueError:
            print("Invalid input! Please enter a number.")


# Main program
print("=" * 50)
print("        CAESAR CIPHER PROGRAM")
print("=" * 50)

while True:
    print("\nOptions:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute force decrypt (try all shifts)")
    print("4. Quit")

    choice = input("\nChoose an option (1-4): ")

    if choice == '1':
        message = input("Enter message to encrypt: ")
        if not message.strip():
            print("Message cannot be empty!")
            continue
        shift = get_shift_value()
        result = encrypt(message, shift)
        print(f"\nOriginal:  {message}")
        print(f"Encrypted: {result}")
        print(f"Shift used: {shift}")

    elif choice == '2':
        message = input("Enter message to decrypt: ")
        if not message.strip():
            print("Message cannot be empty!")
            continue
        shift = get_shift_value()
        result = decrypt(message, shift)
        print(f"\nEncrypted: {message}")
        print(f"Decrypted: {result}")
        print(f"Shift used: {shift}")

    elif choice == '3':
        message = input("Enter encrypted message: ")
        if not message.strip():
            print("Message cannot be empty!")
            continue
        brute_force(message)
        print("\nLook for the message that makes sense!")

    elif choice == '4':
        print("\nThanks for using Caesar Cipher!")
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1-4.")
```

## Explanation

### How Caesar Cipher Works

The Caesar cipher shifts each letter by a fixed number of positions in the alphabet:
- A shift of 3 means: A→D, B→E, C→F, ..., X→A, Y→B, Z→C
- Example: "HELLO" with shift 3 becomes "KHOOR"

### Key Concepts

1. **Character Encoding (ASCII)**
   - Each character has a numeric value (ASCII code)
   - `ord('A')` returns 65, `ord('a')` returns 97
   - `chr(65)` returns 'A'

2. **Modular Arithmetic**
   ```python
   # Without modulo - goes beyond Z
   shifted = ord('Z') - ord('A') + 3  # 25 + 3 = 28 (invalid!)

   # With modulo - wraps around
   shifted = (ord('Z') - ord('A') + 3) % 26  # (25 + 3) % 26 = 2 → 'C'
   ```

3. **The Algorithm**
   ```python
   # For uppercase letter with shift 3:
   char = 'X'
   # 1. Get position in alphabet (0-25)
   position = ord(char) - ord('A')  # 23

   # 2. Shift and wrap around
   new_position = (position + 3) % 26  # 26 % 26 = 0

   # 3. Convert back to character
   new_char = chr(new_position + ord('A'))  # chr(0 + 65) = 'A'
   # X + 3 = A
   ```

4. **Decryption**
   - Decryption is just encryption with negative shift
   - If encrypted with +3, decrypt with -3
   - `encrypt(message, -shift)` is the same as decrypt

### Step-by-Step Example

Encrypting "Hi!" with shift 5:

```python
message = "Hi!"
shift = 5

# Character 1: 'H'
'H'.isalpha()  # True
'H'.isupper()  # True
ord('H') - ord('A')  # 72 - 65 = 7 (position in alphabet)
(7 + 5) % 26  # 12
chr(12 + ord('A'))  # chr(12 + 65) = chr(77) = 'M'

# Character 2: 'i'
'i'.isalpha()  # True
'i'.isupper()  # False
ord('i') - ord('a')  # 105 - 97 = 8
(8 + 5) % 26  # 13
chr(13 + ord('a'))  # chr(13 + 97) = chr(110) = 'n'

# Character 3: '!'
'!'.isalpha()  # False
# Keep unchanged: '!'

# Result: "Mn!"
```

## Common Mistakes

1. **Forgetting to wrap around**
   ```python
   # Wrong - will create invalid characters
   new_char = chr(ord(char) + shift)

   # Right - wraps Z back to A
   position = (ord(char) - ord('A') + shift) % 26
   new_char = chr(position + ord('A'))
   ```

2. **Not handling uppercase and lowercase separately**
   ```python
   # Wrong - mixes cases
   shifted = (ord(char) + shift) % 26

   # Right - separate handling
   if char.isupper():
       shifted = (ord(char) - ord('A') + shift) % 26
       result = chr(shifted + ord('A'))
   else:
       shifted = (ord(char) - ord('a') + shift) % 26
       result = chr(shifted + ord('a'))
   ```

3. **Encrypting spaces and punctuation**
   ```python
   # Wrong - encrypts everything
   encrypted = chr((ord(char) + shift) % 26)

   # Right - check if letter first
   if char.isalpha():
       # encrypt
   else:
       encrypted += char  # keep unchanged
   ```

## Testing

Test with these cases:
- "ABC" with shift 1 → "BCD"
- "XYZ" with shift 3 → "ABC" (wrapping)
- "Hello, World!" with shift 13 → "Uryyb, Jbeyq!" (spaces/punctuation preserved)
- Encrypt then decrypt should return original message

## Historical Note

The Caesar cipher is named after Julius Caesar, who used it to protect military messages. It's one of the simplest encryption techniques but is easily broken today. It's a great learning tool for understanding:
- Basic encryption concepts
- Character manipulation
- Algorithm implementation

## Extensions

1. **ROT13** (special case where shift = 13)
   ```python
   def rot13(message):
       return encrypt(message, 13)
   ```

2. **Reverse the alphabet**
   ```python
   def reverse_cipher(message):
       result = ""
       for char in message:
           if char.isalpha():
               if char.isupper():
                   result += chr(ord('Z') - (ord(char) - ord('A')))
               else:
                   result += chr(ord('z') - (ord(char) - ord('a')))
           else:
               result += char
       return result
   ```

3. **Frequency analysis hint**
   ```python
   def analyze_frequency(text):
       """Count letter frequencies to detect encryption."""
       freq = {}
       for char in text.upper():
           if char.isalpha():
               freq[char] = freq.get(char, 0) + 1
       # Most common letter in English is 'E'
       if freq:
           most_common = max(freq, key=freq.get)
           print(f"Most common letter: {most_common}")
   ```
