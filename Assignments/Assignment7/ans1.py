import re

def find_lowercase_sequences(text):
    return re.findall(r'[a-z]+(?:_[a-z]+)+', text)

# Example usage
text = "this_is_a_test string example hello_world"
print(find_lowercase_sequences(text))  # Output: ['this_is_a_test', 'hello_world']
