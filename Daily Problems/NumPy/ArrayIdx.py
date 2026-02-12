# Find indices where values > 75 in a random array.
import numpy as np

def find_threshold(arr, threshold=75):
    indices = np.where(arr > threshold)[0]
    return indices

if __name__ == "__main__":
    # Create a random array of integers between 0 and 100
    random_array = np.random.randint(0, 100, size=50)
    print("Random array: ", random_array)
    threshold_indices = find_threshold(random_array)
    print(f"Indices where values > 75: {threshold_indices}")