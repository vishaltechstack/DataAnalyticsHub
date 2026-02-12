'''
In NumPy, products refer to different ways of multiplying numbers or arrays.
NumPy supports element-wise multiplication, dot products, matrix multiplication, and cumulative products.

Operation	           Function

Element-wise	       *, np.multiply()
Dot product	           np.dot()
Matrix multiply	       @, np.matmul()
Total product	       np.prod()
Cumulative	           np.cumprod()
'''
import numpy as np

'''
1. Element-Wise Product
Each element is multiplied with the corresponding element.
'''
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a * b


'''
2. Using np.multiply()
Same as element-wise *, but more explicit.
'''
np.multiply(a, b)


'''
3. Dot Product
Used in linear algebra.
'''
# 1D Dot Product
np.dot(a, b)


# Calculation:
(1*4) + (2*5) + (3*6) 


# 2D Dot Product (Matrix Multiplication)
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

np.dot(A, B)


'''
4. Matrix Multiplication (@ or matmul)
Preferred method for matrices.
'''
A @ B

# or
np.matmul(A, B)


# 5. Product of All Elements
arr = np.array([1, 2, 3, 4])
np.prod(arr)


# 6. Product Along an Axis
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

np.prod(arr, axis=0)   # column-wise
np.prod(arr, axis=1)   # row-wise


# 7. Cumulative Product
arr = np.array([1, 2, 3, 4])
np.cumprod(arr)