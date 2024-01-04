#!/usr/bin/python3
output = ""
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit == 8:
            output += "{:02d} ".format(tens_digit * 10 + ones_digit)
        else:
            output += "{:02d}, ".format(tens_digit * 10 + ones_digit)
output = output.rstrip(', ')
print(output)
