# The multinomial distribution is a generalization of the binomial distribution. It models the probabilities of counts for each outcome in a fixed number of trials, where each trial can result in one of several outcomes.
import numpy as np

# n trials, probabilities
data = np.random.multinomial(n=10, pvals=[0.2, 0.5, 0.3])
print(data)

# 📌 Extension of binomial for multiple outcomes.