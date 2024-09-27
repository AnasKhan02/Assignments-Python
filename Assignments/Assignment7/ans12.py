import re

def extract_words(text):
    return re.findall(r'(?<=[=:])\s*(\w+)\s*(?=[.:])', text)

# Example usage
ip = 'Poke,on=-=so_good:ink.to/is(vast)ever2-sit'
print(extract_words(ip))  # Output: ['so_good']
