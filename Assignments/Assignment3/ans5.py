# 5. Python Program to Check if a Key Exists in a Dictionary or Not

def key_exists(dictionary, key):
    return key in dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter a key to check: ")
if key_exists(my_dict, key):
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")
