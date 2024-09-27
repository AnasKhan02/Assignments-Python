import numpy as np

def extract_subpart(array, center, shape, fill_value=0):
    padded_array = np.pad(array, pad_width=((shape[0]//2, shape[0]//2), (shape[1]//2, shape[1]//2)), mode='constant', constant_values=fill_value)
    center_x, center_y = center
    return padded_array[center_x:center_x + shape[0], center_y:center_y + shape[1]]

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(extract_subpart(array, (1, 1), (3, 3), fill_value=0))
