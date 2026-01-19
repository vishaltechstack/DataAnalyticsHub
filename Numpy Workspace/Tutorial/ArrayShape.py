'''
The shape of a NumPy array tells you how many elements are in each dimension.
It is one of the most used properties in NumPy.
'''

import numpy as np

# Shape in Different Dimensions:

# 1D Array
arr = np.array([10, 20, 30, 40])
print(arr.shape)


# 2D Array
arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])
print(arr.shape)


# 3D Array
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr.shape)