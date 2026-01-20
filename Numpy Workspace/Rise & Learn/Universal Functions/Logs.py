'''
Logarithms are widely used in data science, statistics, and machine learning, especially for scaling data
and handling exponential growth.
NumPy provides fast, vectorized log functions.

All log functions are available as universal functions, so they work element by element.
'''
import numpy as np

'''
1. Natural Log (log)
Base e logarithm.
'''
arr = np.array([1, 2, 10, 20])
np.log(arr)


# 2. Log Base 10 (log10)
np.log10(arr)


# 3. Log Base 2 (log2)
np.log2(arr)


'''
4. Log of (1 + x) → log1p
More accurate for very small values.
'''
arr = np.array([0.0001, 0.01, 0.1])
np.log1p(arr)


'''
5. Handling Zero and Negative Values
Log is not defined for zero or negative numbers.
'''
arr = np.array([1, 0, -2])
np.log(arr)

# Safe approach:
arr = np.where(arr > 0, arr, 1)
np.log(arr)


# 6. Log Transformation (Real Example)
sales = np.array([10, 100, 1000, 10000])
log_sales = np.log10(sales)
print(log_sales)


# 7. Logs Are Vectorized
arr = np.array([1, 4, 16, 64])
np.log2(arr)