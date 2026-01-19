'''
Summation in NumPy means adding elements of an array.
NumPy provides fast and flexible ways to calculate sums across entire arrays or along specific dimensions.
'''
import numpy as np

# 1. Sum of All Elements
arr = np.array([1, 2, 3, 4])
np.sum(arr)


# 2. Summation in 2D Arrays
arr = np.array([[1, 2, 3],[4, 5, 6]])

# Row-wise Sum
np.sum(arr, axis=1)

# Column-wise Sum
np.sum(arr, axis=0)


# 3. Summation in Higher Dimensions
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
np.sum(arr, axis=0)


'''
4. Using keepdims
Keeps the original dimensions.
'''
np.sum(arr, axis=1, keepdims=True)


# 5. Cumulative Sum (cumsum)
arr = np.array([1, 2, 3, 4])
np.cumsum(arr)


# 6. Handling Missing Values
arr = np.array([1, 2, np.nan, 4])
np.nansum(arr)


# 7. Difference Between sum() and Python sum()
np.sum(arr)     # Faster, supports axis
sum(arr)        # Slower, limited


'''
Real-World Example
Total sales per product:
'''
sales = np.array([[100, 200, 300],
                  [150, 250, 350]])

np.sum(sales, axis=0)