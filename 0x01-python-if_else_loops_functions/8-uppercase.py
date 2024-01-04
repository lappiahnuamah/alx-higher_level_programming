#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert the character to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - 3i2)
            print('{}'.format(uppercase_char), end='')
        else:
            print('{}'.format(char), end='')
