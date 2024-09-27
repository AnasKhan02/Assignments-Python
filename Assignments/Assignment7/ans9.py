def replace_matching_elements(items, strings):
    for item in items:
        strings = [s.replace(item, 'X') for s in strings]
    return strings

# Example usage
items = ['hello', 'world']
input_strings = ['hello there', 'world of python', 'goodbye']
print(replace_matching_elements(items, input_strings))  # Output: ['X there', 'X of python', 'goodbye']
