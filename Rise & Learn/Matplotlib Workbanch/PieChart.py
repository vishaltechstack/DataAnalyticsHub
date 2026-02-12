# The Pie Chart is a circular statistical graphic that is divided into slices to illustrate numerical proportions. Each slice represents a category's contribution to the whole, making it easy to visualize the relative sizes of different categories.
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 25, 20, 15]

# Pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')   # autopct='%1.1f%%' is used to display the percentage value on each slice of the pie chart, formatted to one decimal place.

plt.title("Programming Language Usage")

plt.show()