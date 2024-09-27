def filter_den_ly(lst):
    return [item for item in lst if item.startswith('den') or item.endswith('ly')]

# Example usage
input_list = ['deny', 'dependency', 'friendly', 'endlessly']
print(filter_den_ly(input_list))  # Output: ['deny', 'friendly', 'endlessly']
