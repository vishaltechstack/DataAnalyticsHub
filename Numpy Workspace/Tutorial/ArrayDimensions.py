'''
In Numpy, dimension means how many levels an array has. It tells you how data is organized.
'''
import numpy as np

# 1. 0-Dimensional Array (Scalar)
arr = np.array(40)
print("0-Dimensional array: ", arr)
print("Number of dimensions: ", arr.ndim)    


# 2. 1-Dimensional Array
arr1 = np.array([1, 2, 3, 4, 5])
print("\n1-Dimensional array: ", arr1)
print("Number of dimensions: ", arr1.ndim)


# 3. 2-Dimensional Array
arr2 = np.array([[1, 2, 3], [9, 8, 7]])
print("\n2-Dimensional array: ", arr2)
print("Number of dimensions: ", arr2.ndim)


# 4. 3-Dimensional Array
arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("\n3-Dimensional array: ", arr3)
print("Number of dimensions: ", arr3.ndim)


# 5. 4-Dimensional Array
arr4 = np.array([[[[1, 2], [3, 4], [5, 6], [7, 8]]]])
print("\n4-Dimensional array: ", arr4)
print("Number of dimensions: ", arr4.ndim)


'''
Higher Dimensional Arrays:

An array can have any number of dimensions.
When the array is created, you can define the number of dimensions by using the ndmin argument.
'''
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print('number of dimensions :', arr5.ndim)