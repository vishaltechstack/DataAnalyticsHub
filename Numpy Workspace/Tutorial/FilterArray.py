'''
Filtering arrays means selecting elements based on a condition.
In NumPy, this is usually done using boolean indexing, and it is one of the most powerful features.
'''

import numpy as np

# 1. Filtering with Conditions (Boolean Indexing)
arr = np.array([10, 20, 30, 40, 50])

filtered = arr[arr > 25]
print(filtered)


'''
2. Multiple Conditions
Use logical operators:

    • & for AND
    • | for OR
    • ~ for NOT
'''
arr = np.array([10, 20, 30, 40, 50])

filtered = arr[(arr > 20) & (arr < 50)]
print(filtered)


# 3. Filtering 2D Arrays
arr = np.array([[5, 15, 25],
                [35, 45, 55]])

filtered = arr[arr > 30]
print(filtered)


# 4. Using where()
arr = np.array([10, 20, 30, 40])

result = np.where(arr > 25, arr, 0)
print(result)


# 5. Filtering with Custom Boolean Array
arr = np.array([100, 200, 300, 400])
mask = np.array([True, False, True, False])

print(arr[mask])


# 6. Filtering with isin()
arr = np.array([1, 2, 3, 4, 5])
print(arr[np.isin(arr, [2, 4])])


# 7. Common Mistake to Avoid
# Wrong:
arr[arr > 10 and arr < 40]   # error

# Correct:
arr[(arr > 10) & (arr < 40)]