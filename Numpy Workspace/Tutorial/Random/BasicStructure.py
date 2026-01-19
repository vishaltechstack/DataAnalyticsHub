import numpy as np

# 1. Random Float Values (0 to 1)
np.random.rand(4)
np.random.rand(1, 10)


# 2. Random Integers
np.random.randint(1, 10)

# Array of random integers:
np.random.randint(1, 10, size=(2, 3))


# 3. Random Values from Normal Distribution
np.random.randn(5)


# 4. Random Choice
np.random.choice([10, 20, 30, 40])


'''
Reproducibility with Seed
Using a seed ensures you get the same random values every time.
'''
np.random.seed(42)
print(np.random.rand(3))


# Random Arrays Example
arr = np.random.randint(0, 100, size=(3, 3))
print(arr)