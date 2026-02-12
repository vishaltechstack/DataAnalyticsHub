# The Normal Distribution, also known as the Gaussian distribution, is a continuous probability distribution characterized by its bell-shaped curve. It is defined by two parameters: the mean (μ) and the standard deviation (σ). The mean determines the center of the distribution, while the standard deviation controls the spread of the data.
import numpy as np

# Mean = 0, Std Dev = 1
data = np.random.normal(loc=0, scale=1, size=10)
print(data)

# 📌 Bell-shaped curve, widely used in ML.