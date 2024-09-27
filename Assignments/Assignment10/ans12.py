import numpy as np

def create_record_array(arr):
    return np.array(arr, dtype=[('col1', 'i4'), ('col2', 'i4')])

data = [[1, 2], [3, 4]]
record_array = create_record_array(data)
print(record_array)
