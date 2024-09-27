import numpy as np

def extract_blocks(matrix):
    return np.lib.stride_tricks.as_strided(matrix, shape=(matrix.shape[0]-2, matrix.shape[1]-2, 3, 3), strides=matrix.strides * 2)

matrix = np.random.rand(10, 10)
blocks = extract_blocks(matrix)
print(blocks)
