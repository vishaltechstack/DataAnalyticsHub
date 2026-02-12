# The Subplot function in Matplotlib allows you to create multiple plots in a single figure.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

# First subplot
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Plot 1")

# Second subplot
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.show()