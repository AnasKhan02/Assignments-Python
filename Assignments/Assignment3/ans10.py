# 10.Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def distinct_elements(lst):
    return list(set(lst))

result = distinct_elements([1, 2, 2, 3, 4, 4])
print(result)  # Output: [1, 2, 3, 4]
