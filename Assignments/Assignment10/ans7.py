import numpy as np

def sum_matrix_products(matrices, vectors):
    return sum(np.dot(mat, vec) for mat, vec in zip(matrices, vectors))

matrices = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
vectors = [np.array([[1], [2]]), np.array([[3], [4]])]
print(sum_matrix_products(matrices, vectors))
