'''
Rounding decimals is common when cleaning data, formatting results, or preparing outputs.
NumPy provides multiple functions to handle different rounding needs.
'''
import numpy as np

'''
1. round() / around()
Rounds values to a given number of decimals.
'''
arr = np.array([1.234, 5.678, 9.876])
np.round(arr, 2)


'''
2. floor()
Rounds down to the nearest integer.
'''
arr = np.array([1.9, 2.1, 3.7])
np.floor(arr)


'''
3. ceil()
Rounds up to the nearest integer.
'''
np.ceil(arr)


'''
4. trunc()
Removes the decimal part without rounding.
'''
np.trunc(arr)


# 5. Rounding to Integers
arr = np.array([1.2, 2.5, 3.8])
arr.astype(int)


'''
6. Difference Between Common Methods
Function	   Behavior

round	       Nearest value
floor	       Always down
ceil	       Always up
trunc	       Remove decimals
'''
# Real Example
prices = np.array([99.999, 149.456, 200.123])
final_prices = np.round(prices, 2)
print(final_prices)