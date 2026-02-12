# The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent trials, where each trial has the same probability of success.
import numpy as np

# n = number of trials, p = probability
data = np.random.binomial(n=10, p=0.5, size=10)
print(data)

# 📌 Used for yes/no experiments.