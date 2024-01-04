#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert the character to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
    print("{}".format(result))
