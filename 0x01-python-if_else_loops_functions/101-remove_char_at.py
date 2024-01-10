def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        return input_str 
    # Return the original string if the index is out of bounds

    # Using string slicing to create a copy without the character at position n
    result_str = input_str[:n] + input_str[n+1:]
    return result_str
