import re

def count_vowel_starting_words(text):
    return len(re.findall(r'\b[aeiouAEIOU]\w*', text))

# Example usage
text = "apple orange banana umbrella egg"
print(count_vowel_starting_words(text))  # Output: 4
