'''
Create a 5×5 matrix with random integers (1–100).
    • Find mean, median, standard deviation.
'''
import numpy as np

# Create a 5x5 matrix with random integers from 1 to 100
matrix = np.random.randint(1, 101, size=(5, 5))

# Calculate mean
mean = np.mean(matrix)

# Calculate median
median = np.median(matrix)

# Calculate standard deviation
std_dev = np.std(matrix)

print("Matrix: ", matrix)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")