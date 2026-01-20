'''
Splitting an array means dividing it into multiple smaller arrays.
NumPy provides simple functions to split arrays based on rows, columns, or positions.

Quick Summary:
Function	         Use Case

split()	             Equal parts only
array_split()	     Unequal parts allowed
hsplit()	         Split columns
vsplit()	         Split rows
'''

import numpy as np

'''
1. np.split() – Equal Splitting
Use this when the array can be divided into equal parts.
'''
# Example:
arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = np.split(arr, 3)
print(new_arr)


'''
2. np.array_split() – Unequal Splitting
Works even if the parts are not equal.
'''
arr = np.array([1, 2, 3, 4, 5])

new_arr = np.array_split(arr, 3)
print(new_arr)


'''
3. Splitting 2D Arrays
Split by rows
'''
arr = np.array([[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]])

row_split = np.split(arr, 2)
print(row_split)


# Split by Columns
col_split = np.split(arr, 2, axis=1)
print(col_split)


'''
4. hsplit() and vsplit():
Horizontal Split (Columns)
'''
np.hsplit(arr, 2)


# Vertical Split (Rows)
np.vsplit(arr, 2)


# 5. Splitting Using Index Positions
arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = np.split(arr, [2, 4])
print(new_arr)