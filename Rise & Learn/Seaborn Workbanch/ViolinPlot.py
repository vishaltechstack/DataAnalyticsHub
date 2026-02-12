# violin plot used to visualize the distribution of a dataset across different categories. It combines aspects of a box plot and a kernel density plot, providing insights into the central tendency, variability, and distribution shape of the data.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Violin plot
sns.violinplot(
    data=data,
    x="day",
    y="total_bill"
)

plt.show()