'''
NumPy makes arithmetic operations simple, fast, and clean.
You can perform calculations directly on arrays without writing loops.
Every operation works element-wise.
'''
import numpy as np

# 1. Basic Arithmetic Operations
a = np.array([10, 20, 30])
b = np.array([2, 4, 6])

# • Addition
a + b

# • Subtraction
a - b

# • Multiplication
a * b

# • Division
a / b


# 2. Arithmetic with Scalars (Vectorization)
arr = np.array([1, 2, 3, 4])

arr + 10
arr * 2
arr / 5


# 3. Using NumPy Functions (ufuncs)
np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
np.divide(a, b)


# 4. Power and Modulus
arr = np.array([2, 3, 4])

arr ** 2        # square
np.power(arr, 3)
arr % 2         # modulus


# 5. Arithmetic in 2D Arrays
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

a + b
a * b


# 6. Broadcasting Example
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr + 10


'''
7. Common Mistake
This is not matrix multiplication:
'''
a * b

# Matrix multiplication:
a @ b

# or
np.dot(a, b)