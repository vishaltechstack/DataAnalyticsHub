# Scatter plot used to show the relationship between two variables. It is a type of plot that uses Cartesian coordinates to display values for two variables for a set of data. Each point on the plot represents an observation in the dataset, with the position of the point determined by the values of the two variables being plotted.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Scatter plot
sns.scatterplot(
    data=data,
    x="total_bill",
    y="tip"
)

plt.show()