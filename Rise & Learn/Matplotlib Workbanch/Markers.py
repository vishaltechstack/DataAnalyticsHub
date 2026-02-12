#  Markers in Matplotlib are used to highlight specific data points on a plot. They can be customized in terms of shape, size, color, and more. In this example, I will show you how to use markers in a simple line plot.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [3, 8, 1, 10]

# Plot with markers
plt.plot(x, y, marker='o')   # 'o' is the marker style for circles. You can choose from various marker styles such as 's' for squares, '^' for triangles, etc.

plt.show()