# 8. Python Program to Count the Frequency of Each Word in a String using Dictionary
#    "Train Bus Bus Train Taxi Aeroplane Taxi Bus Apple Mango Orange Mango Guava Guava Mango"

def word_frequency(s):
    words = s.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

result = word_frequency("Train Bus Bus Train Taxi Aeroplane Taxi Bus Apple Mango Orange Mango Guava Guava Mango")
print(result)
