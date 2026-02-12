'''
In NumPy, differences usually mean finding the difference between consecutive elements in an array.
This is done using the np.diff() function.
It is commonly used in data analysis, time series, and signal processing.
'''
import numpy as np

'''
What is np.diff()?
np.diff() calculates the difference between adjacent elements.

Formula:
diff[i] = arr[i+1] − arr[i]
'''

# 1. Difference in 1D Array
arr = np.array([10, 15, 25, 40])
result = np.diff(arr)

print(result)


'''
2. Difference in 2D Array
By default, difference is calculated row-wise (axis = -1).
'''
arr = np.array([[1, 4, 7],
                [2, 5, 9]])

print(np.diff(arr))


'''
3. Using axis
Column-wise difference
'''
np.diff(arr, axis=0)


'''
4. Higher Order Differences
You can calculate differences multiple times using n.
'''
arr = np.array([1, 4, 9, 16, 25])
np.diff(arr, n=2)


'''
5. Difference with Custom Step
To compare non-adjacent elements:
'''
arr[2:] - arr[:-2]


'''
Real-World Example
Daily Sales Change
'''
sales = np.array([100, 120, 115, 140])
daily_change = np.diff(sales)

print(daily_change)
