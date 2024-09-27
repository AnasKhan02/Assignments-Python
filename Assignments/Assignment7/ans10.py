import re

def extract_hex_sequences(text):
    return re.findall(r'\b(0x)?[0-9a-fA-F]+\b', text)

# Example usage
text = "Here are some hex values: 0x1A, 0x2b, 3F, 4f and 5G"
print(extract_hex_sequences(text))  # Output: ['0x1A', '0x2b', '3F', '4f']
