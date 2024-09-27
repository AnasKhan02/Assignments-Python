import re

def filter_surrounded_by_word_chars(lst):
    return [item for item in lst if re.search(r'\w4\w', item)]

# Example usage
input_list = ['test4example', '4test', 'example', 'foo4bar']
print(filter_surrounded_by_word_chars(input_list))  # Output: ['test4example', 'foo4bar']
