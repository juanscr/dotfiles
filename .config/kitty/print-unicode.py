#!/usr/bin/env python3

# Hexadecimal to correspondent unicode character
def get_num(x):
    num = x.split("x")[1]
    if len(num) < 3:
        num = "0" * (3 - len(num)) + num

    return "U+E" + num.upper()

# Number of characters in icons-in-terminal font
num_of_char = 3730

# Unicode characters
initial_char = get_num(hex(0))
last_char = get_num(hex(num_of_char))
chars = [initial_char, last_char]

# Print symbol map
print("symbol_map", "-".join(chars), "icons-in-terminal")
