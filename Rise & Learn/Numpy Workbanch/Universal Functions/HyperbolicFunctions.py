'''
Hyperbolic functions are mathematical functions similar to trigonometric functions,
but they are based on hyperbolas instead of circles.
In NumPy, these functions are available as universal functions (ufuncs),
so they work element-wise on arrays and are fully vectorized.
'''
import numpy as np

'''
Common Hyperbolic Functions in NumPy
1. sinh() – Hyperbolic Sine
'''
arr = np.array([0, 1, 2])
np.sinh(arr)


# 2. cosh() – Hyperbolic Cosine
np.cosh(arr)


# 3. tanh() – Hyperbolic Tangent
np.tanh(arr)


'''
Inverse Hyperbolic Functions
NumPy also provides inverse versions.
'''
# 4. arcsinh()
np.arcsinh(arr)


# 5. arccosh()
np.arccosh(arr)


# Working with Arrays
values = np.linspace(-2, 2, 5)
print(np.sinh(values))
print(np.tanh(values))


'''
Real-World Use Cases
Hyperbolic functions are used in:
    • Neural networks (activation functions like tanh)
    • Physics and engineering equations
    • Signal processing
    • Differential equations

Important Points to Remember
    • Hyperbolic functions are ufuncs
    • Operate element-wise
    • Accept scalars or arrays
    • Output is always float

Quick Summary:
Function	  Description

sinh()	      Hyperbolic sine
cosh()	      Hyperbolic cosine
tanh()	      Hyperbolic tangent
arcsinh()	  Inverse sinh
arccosh()	  Inverse cosh
arctanh()	  Inverse tanh
'''