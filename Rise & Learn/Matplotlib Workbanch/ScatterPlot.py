# The Scatter Plot is a type of data visualization that uses Cartesian coordinates to display values for two variables. Each point on the plot represents an observation, with its position determined by the values of the two variables. Scatter plots are useful for identifying relationships, trends, and patterns between the variables, such as correlations or clusters.
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 6, 9]
y = [99, 86, 87, 88, 100, 90]

# Scatter plot
plt.scatter(x, y)

plt.title("Scatter Plot Example")
plt.xlabel("Age")
plt.ylabel("Score")

plt.show()