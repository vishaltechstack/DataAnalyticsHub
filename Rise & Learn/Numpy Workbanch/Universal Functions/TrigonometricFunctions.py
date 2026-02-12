'''
NumPy provides built-in trigonometric functions to work with angles and waves.
These functions are widely used in engineering, physics, graphics, and data analysis.

Important point: NumPy trigonometric functions use radians, not degrees.
'''
import numpy as np

# 1. Basic Trigonometric Functions
angles = np.array([0, np.pi/2, np.pi])

np.sin(angles)
np.cos(angles)
np.tan(angles)


'''
2. Degrees to Radians
Since inputs must be in radians:
'''
degrees = np.array([0, 30, 45, 90])
radians = np.deg2rad(degrees)

print(np.sin(radians))


# 3. Radians to Degrees
angles = np.array([0, np.pi/2, np.pi])
degrees = np.rad2deg(angles)

print(degrees)


'''
4. Inverse Trigonometric Functions
These return values in radians.
'''
values = np.array([0, 0.5, 1])

np.arcsin(values)
np.arccos(values)
np.arctan(values)


'''
5. Using Trigonometry on Arrays
All trigonometric functions are vectorized.
'''
x = np.linspace(0, 2*np.pi, 5)
y = np.sin(x)

print(y)


# 6. Common Mistake:

# Wrong:
np.sin(90)   # assumes radians, not degrees

# Correct:
np.sin(np.deg2rad(90))


'''
Real-World Example
Wave simulation:
'''
x = np.linspace(0, 360, 10)
y = np.sin(np.deg2rad(x))