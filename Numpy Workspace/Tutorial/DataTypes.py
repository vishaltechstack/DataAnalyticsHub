'''
NumPy data types define what kind of data an array can store.
Using the right data type makes operations faster and saves memory.
'''

import numpy as np

# 1. Checking Data Type
arr = np.array([1, 2, 3])
print(arr.dtype)


'''
2. Common NumPy Data Types:

• Integer Types
    np.int8    # very small integers
    np.int16
    np.int32
    np.int64

• Floating Types
    np.float16
    np.float32
    np.float64

• Complex Numbers
    np.complex64
    np.complex128

• Boolean
    np.bool_

• String
    np.str_
'''

# 3. Setting Data Type While Creating Array
arr = np.array([1, 2, 3], dtype=np.float32)
print(arr.dtype)


# 4. Changing Data Type (Type Casting)
arr = np.array([1.5, 2.6, 3.7])
new_arr = arr.astype(int)
print(new_arr)


'''
5. Why Data Types Matter
    • Faster calculations
    • Less memory usage
    • Better control over data
    • Important for ML and large datasets
'''


# 6. Memory Usage Example
arr1 = np.array([1, 2, 3], dtype=np.int32)
arr2 = np.array([1, 2, 3], dtype=np.int64)
print(arr1.itemsize)  # 4 bytes
print(arr2.itemsize)  # 8 bytes


'''
7. Mixed Data Types
NumPy arrays must have one data type.
'''
arr = np.array([1, 2.5, 3])
print(arr.dtype)