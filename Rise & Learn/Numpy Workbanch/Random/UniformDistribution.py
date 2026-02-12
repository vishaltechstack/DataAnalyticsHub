# The uniform distribution is a continuous probability distribution where all outcomes are equally likely within a specified range. It is defined by two parameters: the minimum value (a) and the maximum value (b). The probability density function (PDF) of a uniform distribution is constant between a and b, and zero elsewhere.
import numpy as np

# Values between 0 and 1
data = np.random.uniform(0, 1, size=10)
print(data)

# 📌 All values have equal probability.