'''
Create two random arrays and perform:
    • Element-wise addition
    • Dot product
'''
import numpy as np

arr1 = np.random.randint(1, 10, size=(3, 3))
arr2 = np.random.randint(1, 10, size=(3, 3))

print("Array 1:")
print(arr1)
print("Array 2:")
print(arr2)

# Element-wise addition
addition = arr1 + arr2
print("Element-wise addition:")
print(addition)

# Dot product
dot_product = np.dot(arr1, arr2)
print("Dot product:")
print(dot_product)