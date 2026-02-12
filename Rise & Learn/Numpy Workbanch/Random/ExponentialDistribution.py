# The exponential distribution is a continuous probability distribution that describes the time between events in a Poisson process. It is often used to model the time until on event occurs, such as the time between arrivals of customers at a store or the time until a radioactive particle decays. The exponential distribution is defined by a single parameter, lamda (λ), which is the rate parameter. The mean of the distribution is given by 1/λ, and the variance is given by 1/λ^2.
import numpy as np

# scale = 1 / lambda
data = np.random.exponential(scale=1.0, size=10)
print(data)

# 📌 Time between events.