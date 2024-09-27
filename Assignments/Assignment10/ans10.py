import numpy as np

def n_largest(array, n):
    return np.partition(array, -n)[-n:]

array = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(n_largest(array, 3))
