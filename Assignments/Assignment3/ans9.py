# 9. Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number


def create_tuples_list(n):
    return [(i, i ** 2) for i in range(n + 1)]

result = create_tuples_list(5)
print(result)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
