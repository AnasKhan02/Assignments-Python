def lines_not_containing_start(text):
    return [line for line in text.splitlines() if 'start' not in line.lower()]

# Example usage
input_text = """Start the process
This line does not contain the word
Another start here"""
print(lines_not_containing_start(input_text))
