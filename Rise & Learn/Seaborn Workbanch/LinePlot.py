# Line plot used for visualizing the relationship between two continuous variables. It is useful for showing trends over time or across different categories. In this example, I will create a line plot using the seaborn library to visualize the relationship between time and signal in an fmri dataset.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("fmri")

# Line plot
sns.lineplot(
    data=data,
    x="timepoint",
    y="signal"
)

plt.show()