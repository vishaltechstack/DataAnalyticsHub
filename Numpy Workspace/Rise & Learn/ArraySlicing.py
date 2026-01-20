'''
Array slicing means extracting a part of an array.
NumPy slicing is simple, fast, and works the same way across dimensions.

Basic rule:
[start : stop : step]


start → included

stop → excluded

step → optional
'''

import numpy as np

# 1. Slicing in 1D Array
arr = np.array([10, 20, 30, 40, 50])
arr[1:4]     # [20 30 40]
arr[:3]      # [10 20 30]
arr[2:]      # [30 40 50]
arr[::2]     # [10 30 50]
arr[::-1]    # reverse array


# 2. Slicing in 2D Array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
arr[0:2, 1:3]   # rows 0–1, columns 1–2
arr[:, 0]       # all rows, first column
arr[1, :]       # second row
arr[:, :]       # full array


# 3. Slicing in 3D Array
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
arr[0, :, 1:]   # first block, all rows, columns from index 1


# 4. Using Step in Slicing
arr = np.array([1, 2, 3, 4, 5, 6])
arr[::2]     # every second element
arr[1::2]    # every second element starting from index 1


'''
5. Slicing Returns a View (Important)
In NumPy, slicing usually returns a view, not a copy.
'''
arr = np.array([10, 20, 30, 40])
slice_arr = arr[1:3]   # slice_arr is a view of arr

slice_arr[0] = 99      # Modifying the slice
print(arr)