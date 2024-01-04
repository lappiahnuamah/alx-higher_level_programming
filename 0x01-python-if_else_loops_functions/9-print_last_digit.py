#!/usr/bin/python3
def print_last_digit(number):
    # Ensure the number is positive (absolute value)
    number = abs(number)

    # Extract the last digit using the remainder operator (%)
    last_digit = number % 10

    # Print the last digit
    print(last_digit, end='')

    # Return the last digit if needed
    return last_digit
