# The difference between shuffle and permutation in NumPy is that shuffle modifies the original array in place, while permutation returns a new array with the elements permuted.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Shuffle changes original array
np.random.shuffle(arr)
print("Shuffled:", arr)

# Permutation returns new array
print("Permutation:", np.random.permutation(arr))