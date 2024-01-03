#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the character to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end='')
        else:
            print(char, end='')

    # Add a new line after printing the uppercase string
    print()
