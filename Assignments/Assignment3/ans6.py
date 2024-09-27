# 6. Python Program to Find the Sum of All the Items in a Dictionary

def sum_dictionary_items(dictionary):
    return sum(dictionary.values())

# Example usage
result = sum_dictionary_items({'a': 1, 'b': 2, 'c': 3})
print(result)  # Output: 6
