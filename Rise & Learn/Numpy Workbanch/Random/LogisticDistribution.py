# The logistic distribution is a continuous probability distribution used in statistics and machine learning. It is similar to the normal distribution but has heavier tails, making it useful for modeling data with outliers. The logistic distribution is defined by its location parameter (mean) and scale parameter (standard deviation).
import numpy as np

# loc = mean, scale = standard deviation
data = np.random.logistic(loc=0, scale=1, size=10)
print(data)

# 📌 Used in logistic regression.