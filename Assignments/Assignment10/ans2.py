import numpy as np

Z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
R = np.array([Z[i:i+4] for i in range(len(Z) - 3)])
print(R)
