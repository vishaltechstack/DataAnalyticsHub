'''
Searching in NumPy means finding the index or position of elements that match a condition.
This is very common in data analysis and interviews.
'''

import numpy as np

'''
1. Searching with where()
np.where() returns the index where the condition is true.
'''
arr = np.array([10, 20, 30, 40, 50])

index = np.where(arr == 30)
print(index)


# 2. Search with Condition
arr = np.array([5, 12, 18, 25, 30])

result = np.where(arr > 15)
print(result)


# 3. Getting Actual Values
arr[np.where(arr > 15)]


# 4. Searching in 2D Array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print(np.where(arr == 50))


'''
5. Using searchsorted()
Used only on sorted arrays.
'''
arr = np.array([10, 20, 30, 40])
print(np.searchsorted(arr, 25))


# 6. Left vs Right Search
arr = np.array([10, 20, 20, 30])

print(np.searchsorted(arr, 20, side='left'))           # First occurrence
print(np.searchsorted(arr, 20, side='right'))          # Last occurrence


# 7. Boolean Mask Searching
arr = np.array([10, 25, 30, 45])

mask = arr > 20
print(mask)
print(arr[mask])