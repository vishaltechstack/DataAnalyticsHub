# The Grid is a set of horizontal and vertical lines that can be added to a plot to improve readability and make it easier to interpret the data. Grids help to visually align data points with the corresponding values on the axes, making it easier to compare and analyze the data.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]        # X-axis values
y = [10, 15, 25, 30]    # Y-axis values

plt.plot(x, y)

# Add grid
plt.grid(True)          # Enable grid

plt.show()