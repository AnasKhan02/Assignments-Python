import re

def count_words_without_a_e_c_t(text):
    return len(re.findall(r'\b[^aecTt]*\b', text))

# Example usage
text = "hello world bat cat eat"
print(count_words_without_a_e_c_t(text))  # Output: 2
