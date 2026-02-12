'''
Sorting in NumPy means arranging elements in a specific order, usually ascending.
NumPy gives fast and flexible ways to sort arrays, even in multiple dimensions.
'''

import numpy as np

# 1. Sorting a 1D Array
arr = np.array([5, 2, 9, 1, 3])
sorted_arr = np.sort(arr)

print(sorted_arr)


'''
2. Sorting in Descending Order
NumPy does not have a direct descending option, but this works:
'''
arr = np.array([5, 2, 9, 1, 3])
print(np.sort(arr)[::-1])


'''
3. Sorting a 2D Array
By default, sorting happens row-wise.
'''
arr = np.array([[3, 1, 2],
                [6, 4, 5]])

print(np.sort(arr))


'''
4. Sorting Along an Axis
Sort each column
'''
print(np.sort(arr, axis=0))


# Sort each row
print(np.sort(arr, axis=1))


# 5. In-Place Sorting with sort()
arr = np.array([5, 2, 9, 1])
arr.sort()
print(arr)


'''
6. Getting Sorted Indexes using argsort()
Useful when you want positions instead of values.
'''
arr = np.array([40, 10, 30, 20])
indexes = np.argsort(arr)

print(indexes)
print(arr[indexes])


# 7. Sorting Based on Another Array
names = np.array(['A', 'B', 'C'])
scores = np.array([88, 72, 95])

order = np.argsort(scores)
print(names[order])
print(scores[order])