# Normalize a NumPy array (min-max scaling).
import numpy as np

def min_max_normalize(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    if max_val - min_val == 0:
        return np.zeros_like(arr) # Avoid division by zero if all values are the same
    
    normalized_arr = (arr - min_val) / (max_val - min_val)
    return normalized_arr

# Example usage:
if __name__ == "__main__":
    data = np.array([10, 20, 30, 40, 50])
    normalized_data = min_max_normalize(data)
    print("Original data: ", data)
    print("Normalized data: ", normalized_data)