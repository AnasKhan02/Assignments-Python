# 4. Python Program to Check whether two Strings are Anagrams

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
