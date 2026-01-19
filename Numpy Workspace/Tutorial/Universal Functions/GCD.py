'''
The Greatest Common Divisor (GCD) of two numbers is the largest positive integer
that divides both numbers without leaving a remainder.
NumPy provides a direct and efficient way to compute GCD for numbers and arrays.

GCD vs LCM (Quick Comparison):
Feature	      GCD	                       LCM

Meaning	      Largest common divisor	   Smallest common multiple
Function	  np.gcd()	                   np.lcm()
Use case	  Simplifying ratios	       Scheduling cycles


Real-World Use

GCD is useful for:
    • Simplifying fractions
    • Dividing tasks evenly
    • Optimizing resource allocation
'''
import numpy as np

# 1. GCD of Two Numbers
result = np.gcd(18, 24)
print(result)


# 2. GCD of Arrays (Element-wise)
a = np.array([12, 15, 21])
b = np.array([18, 25, 14])

print(np.gcd(a, b))


'''
3. GCD of Multiple Numbers
Use reduce().
'''
arr = np.array([24, 36, 60])

result = np.gcd.reduce(arr)
print(result)


# 4. GCD with a Single Number (Broadcasting)
arr = np.array([10, 20, 30])
print(np.gcd(arr, 10))


# 5. GCD of a Range of Numbers
result = np.gcd.reduce(np.arange(1, 11))
print(result)