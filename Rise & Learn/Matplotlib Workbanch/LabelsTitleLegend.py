# The code demonstrates how to add labels, title, and legend to a plot using Matplotlib. It creates two lines representing sales and profit over four years, adds appropriate labels for the axes and a title for the plot and includes a legend to differentiate between the two lines. Finally, it displays the plot.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

# Plot lines
plt.plot(x, y1, label="Sales")     # Add label for the first line
plt.plot(x, y2, label="Profit")    # Add label for the second line

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Amount")
plt.title("Company Performance")

# Show legend
plt.legend()     # Display the legend to differentiate between the lines

plt.show()