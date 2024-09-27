import numpy as np

class SymmetricArray(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            self.view(np.ndarray)[key] = value
            self.view(np.ndarray)[key[::-1]] = value
        else:
            super().__setitem__(key, value)

arr = SymmetricArray(np.zeros((3, 3)))
arr[0, 1] = 5
print(arr)
