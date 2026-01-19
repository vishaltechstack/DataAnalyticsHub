'''
Docstring for Universal Functions.SetOperations
'''
import numpy as np

# 1. unique() – Find Unique Elements
arr = np.array([1, 2, 2, 3, 4, 4, 5])
print(np.unique(arr))


'''
2. union1d() – Union of Two Arrays
Returns all unique elements from both arrays.
'''
a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
print(np.union1d(a, b))


'''
3. intersect1d() – Intersection
Returns common elements.
'''
print(np.intersect1d(a, b))


'''
4. setdiff1d() – Difference
Elements in first array but not in second.
'''
print(np.setdiff1d(a, b))


'''
5. setxor1d() – Symmetric Difference
Elements in either array but not in both.
'''
print(np.setxor1d(a, b))


'''
6. isin() – Membership Test
Checks whether elements exist in another array.
'''
arr = np.array([10, 20, 30, 40])
print(np.isin(arr, [20, 40]))


'''
Important Notes
    • Works only on 1D arrays
    • Output is always sorted
    • Duplicate values are removed
    • Data type is preserved
'''
# Real-World Example
old_users = np.array([101, 102, 103, 104])
new_users = np.array([103, 104, 105])

inactive_users = np.setdiff1d(old_users, new_users)
print(inactive_users)


'''
Quick Summary:
Function	       Purpose

unique	           Remove duplicates
union1d	           Combine unique values
intersect1d	       Common elements
setdiff1d	       Difference
setxor1d	       Exclusive elements
isin	           Membership check
'''