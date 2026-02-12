# The Histogram is a graphical representation of the distribution of numerical data. It is created by dividing the data into intervals (bins) and counting the number of data points that fall into each bin. The height of each bar in the histogram represents the frequency of data points within that bin. Histograms are useful for understanding the shape, central tendency, and variability of a dataset.
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]     # Sample data for the histogram

# Histogram
plt.hist(data, bins=5)

plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()