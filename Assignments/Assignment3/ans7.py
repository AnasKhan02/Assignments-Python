# 7. Python Program to Map Two Lists into a Dictionary

def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example usage
result = map_lists_to_dict(['a', 'b', 'c'], [1, 2, 3])
print(result)  # Output: {'a': 1, 'b': 2, 'c': 3}
