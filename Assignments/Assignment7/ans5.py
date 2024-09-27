def filter_not_containing_e(lst):
    return [item for item in lst if 'e' not in item]

# Example usage
input_list = ['hello', 'world', 'python', 'code']
print(filter_not_containing_e(input_list))  # Output: ['world', 'python']
