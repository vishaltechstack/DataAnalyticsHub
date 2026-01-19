'''
A view shares the same data as the original array.
If you change the view, the original array also changes.
'''

import numpy as np

# Example: View
arr = np.array([10, 20, 30, 40])
view_arr = arr.view()    # Create a view of the original array

view_arr[0] = 99         # Modify the vieww

print(arr)
print(view_arr)


'''
A copy creates a new array with its own data.
Changes in the copy do not affect the original array.
'''

# Example: Copy
arr = np.array([10, 20, 30, 40])
copy_arr = arr.copy()      # Create a copy of the original array
  
copy_arr[0] = 99           # Modify the copy

print(arr)
print(copy_arr)


'''
Slicing: View or Copy?
By default, slicing returns a view
'''
arr = np.array([1, 2, 3, 4])
slice_arr = arr[1:3]

slice_arr[0] = 88
print(arr)