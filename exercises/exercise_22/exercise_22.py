# Exercise 22: Simple Caesar Cipher
# Objective: Encrypt and decrypt messages using Caesar cipher

# Hint: ord() gets ASCII value, chr() converts back to character
# Hint: 'A' = 65, 'Z' = 90, 'a' = 97, 'z' = 122
# Hint: Use modulo % 26 to wrap around the alphabet
# Hint: To decrypt, shift in opposite direction
# Hint: Use .isalpha() to check if character is a letter

def encrypt(message, shift):
    """Encrypt a message using Caesar cipher."""
    encrypted = ""

    # Loop through each character in message


    # If character is a letter, shift it


    # If uppercase


    # If lowercase


    # If not a letter (space, punctuation), keep it unchanged


    return encrypted


def decrypt(message, shift):
    """Decrypt a message using Caesar cipher."""
    # Decryption is just encryption with negative shift


    pass


# Main program
while True:
    print("\nCaesar Cipher Program")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Quit")

    # Get user choice


    # Handle encrypt option


    # Handle decrypt option


    # Handle quit option


    # Handle invalid option
