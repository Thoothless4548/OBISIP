#random Password generator
import string
import random

def passgen(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine selected character sets
    all_characters = f'{letters}{numbers}{symbols}'

    # Check if at least one character set is selected
    if not all_characters:
        print("Error: Please select at least one character set.")
        return None

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def get_user_input():
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter password length: "))
            break
        except ValueError:
            print("Error: Please enter a valid number.")

    # Get user input for character sets
    use_letters = input("Include letters (y/n)? ").lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    return length, use_letters, use_numbers, use_symbols

def main():
    # Get user input
    length, use_letters, use_numbers, use_symbols = get_user_input()

    # Generate and print password
    password = passgen(length, use_letters, use_numbers, use_symbols)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
