import numpy as np

def compute_rank(matrix):
    return np.linalg.matrix_rank(matrix)

matrix = np.array([[1, 2], [2, 4]])
print(compute_rank(matrix))  # Output: 1
