# The Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, given a constant average rate of occurrence.
import numpy as np

# lam = average rate
data = np.random.poisson(lam=5, size=10)
print(data)

# 📌 Models event occurrence over time.