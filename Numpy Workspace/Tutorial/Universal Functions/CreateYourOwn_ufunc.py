'''
NumPy lets you create custom universal functions so your own logic works like built-in NumPy functions.
These custom ufuncs operate element-wise on arrays and support vectorization.

Difference Between frompyfunc and vectorize:
Feature	           frompyfunc	       vectorize

Creates ufunc	   Yes	               No (wrapper)
Speed	           Faster	           Slower
Output dtype	   object	           inferred
Broadcasting	   Yes	               Yes
'''

import numpy as np

'''
1. Using np.frompyfunc (True ufunc behavior)
This converts a normal Python function into a NumPy ufunc.
'''
# np.frompyfunc(function, inputs, outputs)

# Example:
def add_square(x, y):
    return x*x + y*y

ufunc = np.frompyfunc(add_square, 2, 1)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(ufunc(a, b))


'''
2. Using np.vectorize (Convenience wrapper)
This makes your function look vectorized, but internally it still uses a loop.
It is easier to use, but not as fast as real ufuncs.
'''
def cube(x):
    return x ** 3

vec_func = np.vectorize(cube)

arr = np.array([1, 2, 3, 4])
print(vec_func(arr))


# Custom Comparison ufunc
def greater_than_10(x):
    return x > 10

ufunc = np.frompyfunc(greater_than_10, 1, 1)

arr = np.array([5, 15, 25])
print(ufunc(arr))