import re

def count_consecutive_repeated_words(text):
    return len(re.findall(r'\b\w*(\w)\1\w*(\w)\2\w*\b', text))

# Example usage
ip = '''oppressed abandon accommodation bloodless
carelessness committed apparition innkeeper
occasionally afforded embarrassment foolishness
depended successfully succeeded
possession cleanliness suppress'''
print(count_consecutive_repeated_words(ip))  # Output: 8
