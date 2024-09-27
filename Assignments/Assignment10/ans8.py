import numpy as np

def block_sum(array, block_size):
    return array.reshape(array.shape[0] // block_size, block_size, array.shape[1] // block_size, block_size).sum(axis=(1, 3))

array = np.random.rand(16, 16)
print(block_sum(array, 4))
