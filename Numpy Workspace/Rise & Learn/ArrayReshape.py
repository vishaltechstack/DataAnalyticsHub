'''
reshape() is used to change the shape of an array without changing its data.
It is very common in data analysis, machine learning, and image processing.

Basic Rule of Reshape:
The total number of elements must remain the same.

rows × columns = total elements
'''

import numpy as np

# 1. Simple Reshape
arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)
print(new_arr)


# 2. Reshape to 3D Array
arr = np.arange(12)

new_arr = arr.reshape(2, 2, 3)
print(new_arr)


'''
3. Using -1 in Reshape (Very Important)
NumPy automatically calculates the missing dimension.
'''
arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(-1, 3)
print(new_arr)


'''
4. Reshape vs Resize

reshape()
    • Does not change original array
    • Returns a new view or array
'''
new_arr = arr.reshape(3, 2)


'''
resize()
    • Changes original array
    • Can repeat or remove data
'''
arr.resize(3, 2)
print(arr)


'''
5. Flattening an Array
Convert multi-dimensional array to 1D.
'''
arr = np.array([[1, 2], [3, 4]])

arr.flatten()   # returns copy
arr.ravel()     # returns view (mostly)


# 6. Common Error
arr = np.array([1, 2, 3, 4, 5])
arr.reshape(2, 3)     # Error: total elements do not match