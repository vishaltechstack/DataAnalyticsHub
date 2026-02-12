# The Rayleigh distribution is a continuous probability distribution for positive-valued random variables. It is often used to model the magnitude of a two-dimensional vector whose components are independent and identically distributed Gaussion random variables. The probability density function (PDF) of the Rayleigh distribution is given by:
import numpy as np

# scale parameter
data = np.random.rayleigh(scale=2.0, size=10)
print(data)

# 📌 Used in signal processing.