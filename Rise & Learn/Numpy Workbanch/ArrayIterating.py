'''
Array iterating means going through elements one by one.
NumPy gives multiple ways to iterate, depending on the array’s dimension and what you want to do.
'''

import numpy as np

# 1. Iterating Over a 1D Array
arr = np.array([10, 20, 30, 40])

for x in arr:
    print(x)


# 2. Iterating Over a 2D Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

for row in arr:
    print(row)


# Access individual elements
for row in arr:
    for value in row:
        print(value)


# 3. Iterating Over a 3D Array
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

for block in arr:
    for row in block:
        for value in row:
            print(value)


'''
4. Using nditer() (Recommended)
nditer() works for any dimension and is more efficient.
'''
arr = np.array([[1, 2], [3, 4]])

for x in np.nditer(arr):
    print(x)


'''
5. Iterating with Index (ndenumerate())
Gives both index and value.
'''
arr = np.array([[10, 20],
                [30, 40]])

for index, value in np.ndenumerate(arr):
    print(index, value)


# 6. Iterating with Different Data Types
arr = np.array([1.1, 2.2, 3.3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['int']):
    print(x)



'''
Important Tip
Avoid loops when possible. NumPy works best with vectorized operations.
'''

# Slow
for i in range(len(arr)):
    arr[i] = arr[i] * 2

# Fast
arr = arr * 2