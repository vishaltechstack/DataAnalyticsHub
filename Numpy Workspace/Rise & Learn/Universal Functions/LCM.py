'''
The Lowest Common Multiple (LCM) of two numbers is the smallest positive number that is divisible by both numbers.
NumPy provides built-in functions to calculate LCM easily for numbers and arrays.

Real-World Example

LCM is useful in:
    • Scheduling tasks
    • Repeating cycles
    • Time synchronization problems
'''
import numpy as np

# 1. LCM of Two Numbers
result = np.lcm(4, 6)
print(result)


# 2. LCM of Arrays (Element-wise)
a = np.array([2, 4, 6])
b = np.array([3, 5, 9])
print(np.lcm(a, b))


'''
3. LCM of Multiple Numbers
Use reduce() with np.lcm.
'''
arr = np.array([4, 6, 8])

result = np.lcm.reduce(arr)
print(result)


# 4. LCM with Range of Numbers
result = np.lcm.reduce(np.arange(1, 11))
print(result)


# 5. Broadcasting with LCM
arr = np.array([2, 3, 4])
print(np.lcm(arr, 6))