import numpy as np
from scipy import stats


def most_frequent(array):
    mode_result = stats.mode(array)

    return mode_result.mode[0]  # This should now work correctly


array = [1, 2, 3, 1, 2, 1]
print(most_frequent(array))  # Output: 1