# Bar Plot is used for categorical data to show the distribution of values across different categories.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Bar plot
sns.barplot(
    data=data,
    x="day",
    y="total_bill"
)

plt.show()