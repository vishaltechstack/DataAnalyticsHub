'''
Array indexing means accessing specific elements from a NumPy array.
NumPy indexing is fast, flexible, and works for all dimensions.
'''

import numpy as np

# 1. Indexing in 1D Array
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])    # first element
print(arr[2])    # third element
print(arr[-1])   # last element


# 2. Indexing in 2D Array
arr = np.array([[1, 2, 3],[4, 5, 6]])
print(arr[0, 0])   # first row, first column
print(arr[0, 2])   # first row, third column
print(arr[1, 1])   # second row, second column


# 3. Indexing in 3D Array
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(arr[0, 1, 2])    # first block, second row, third column


# 4. Boolean Indexing
arr = np.array([10, 20, 30, 40])
print(arr[arr > 20])    # elements greater than 20


# 5. Fancy Indexing
arr = np.array([10, 20, 30, 40])
print(arr[[0, 2]])      # elements at index 0 and 2


# 6. Modifying Elements Using Indexing
arr = np.array([1, 2, 3, 4])
arr[1] = 20     # modify second element
print(arr)