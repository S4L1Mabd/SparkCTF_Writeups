def xor_and_convert_to_text(decimal_list):
    result = ""
    for num in decimal_list:
        xor_result = num ^ 28  # XOR operation with 28
        character = chr(xor_result)  # Convert decimal value to character
        result += character
    return result

# Example usage:
decimal_values = [79,108, 125, 110, 119 ,103, 88, 80 ,80 ,79, 67 ,40, 78 ,89, 67 ,82, 83 ,72, 67, 79, 83, 67, 90 ,73, 82, 82 ,69, 97]  # Example list of decimal numbers
result_text = xor_and_convert_to_text(decimal_values)
print("Resulting text:", result_text)
