# The Pareto distribution is a power-law probability distribution used in various fields to model phenomena such as wealth distribution, natural phenomena, and social dynamics. It is characterized by a shape parameter (a) that determines the distribution's tail behavior. The Pareto distribution is often associated with the 80-20 rule, which states that a small percentage of the population controls a large portion of the wealth or resources. In this example, we will generate random numbers from a Pareto distribution using NumPy.
import numpy as np

# a = shape parameter
data = np.random.pareto(a=2.0, size=10)
print(data)

# 📌 80–20 rule (wealth distribution).