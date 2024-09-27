def clean_csv_fields(csv_string):
    return [field.strip() for field in csv_string.split(',')]

# Example usage
csv1 = ' comma  ,separated ,values \t\r '
csv2 = 'good bad,nice  ice  , 42 , ,   stall   small'
print(clean_csv_fields(csv1))  # Output: ['comma', 'separated', 'values']
print(clean_csv_fields(csv2))  # Output: ['good bad', 'nice  ice', '42', '', 'stall', 'small']
