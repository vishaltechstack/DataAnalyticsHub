# The chi-square distribution is a continuous probability distribution that arises in statistics when estimating the variance of a normally distributed population from a sample. It is defined by the degrees of freedom (df) parameter, which determines the shape of the distribution. The chi-square distribution is commonly used in hypothesis testing, particularly in tests of independence and goodness-of-fit tests.
import numpy as np

# df = degrees of freedom
data = np.random.chisquare(df=2, size=10)
print(data)

# 📌 Used in hypothesis testing.