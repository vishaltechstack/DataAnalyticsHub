'''
Joining arrays means combining multiple NumPy arrays into one.
NumPy provides several clear ways to do this, depending on how you want the data arranged.

When to Use What:
Method	             Use Case

concatenate()	     General purpose
stack()	             Add new dimension
hstack()	         Join columns
vstack()	         Join rows
append()	         Small tasks only


Variants of stack():

np.hstack((a, b)) - horizontal (column-wise)
np.vstack((a, b)) - vertical (row-wise)
np.dstack((a, b)) - depth-wise (3D)
'''

import numpy as np

'''
1. concatenate()
The most basic and commonly used method.
'''

# 1D Arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))
print(result)


# 2D Arrays (Row-wise)
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

result = np.concatenate((a, b), axis=0)
print(result)


# 2D Arrays (Column-wise)
result = np.concatenate((a, b), axis=1)
print(result)



'''
2. stack()
Stacks arrays along a new axis.
'''
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.stack((a, b))
print(result)


'''
3. append()
Adds elements at the end. Not recommended for large arrays.
'''
np.append(a, b)


'''
4. Joining with Different Shapes
Arrays must be compatible.
'''
a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])

np.vstack((a, b))   # works
np.hstack((a, b))   # works