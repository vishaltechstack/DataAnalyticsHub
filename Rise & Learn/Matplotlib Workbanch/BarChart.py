# The Bar Chart is a graphical representation of data using rectangular bars. Each bar's length is proportional to the value it represents. Bar charts are commonly used to compare different categories or groups of data.
import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]    # Categories for the bars
values = [5, 7, 3, 8]                # Corresponding values for each category

# Bar chart
plt.bar(categories, values)

plt.title("Bar Chart Example")       # Ttile of the chart
plt.xlabel("Category")               # Label for the x-axis
plt.ylabel("Values")                 # Label for the y-axis

plt.show()