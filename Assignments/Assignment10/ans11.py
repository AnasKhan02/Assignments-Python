import numpy as np
import itertools

def cartesian_product(*vectors):
    return np.array(list(itertools.product(*vectors)))

A = [1, 2]
B = ['a', 'b']
print(cartesian_product(A, B))
