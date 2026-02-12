import numpy as np

arr = np.array([10, 20, 30, 20, 40])

x = np.where(arr == 20)    # Returns the indices where the condition is true
print(x)

# Search sorted
sorted_arr = np.array([1,2,3,4,5])
print(np.searchsorted(sorted_arr, 4))    # Returns the index where the value 4 should be inserted to maintain order