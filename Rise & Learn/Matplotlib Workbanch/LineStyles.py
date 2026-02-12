# The Line plot can be customized by using the linestyle parameter.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [6, 2, 9, 4]

# Dashed line
plt.plot(x, y, linestyle='--')    # Dashed line

plt.show()