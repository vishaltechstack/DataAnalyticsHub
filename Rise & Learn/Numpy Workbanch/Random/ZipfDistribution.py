# The Zipf distribution is a discrete probability distribution that describes the frequency of events in a dataset. It is often used to model the distribution of word frequencies in natural language and the distribution of web traffic.
import numpy as np

# a = distribution parameter
data = np.random.zipf(a=2.0, size=10)
print(data)

# 📌 Used in natural language & web traffic.