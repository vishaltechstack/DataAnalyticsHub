# Histogram used for visualizing the distribution of a single numerical variable
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Histogram
sns.histplot(
    data=data,
    x="total_bill",
    bins=20
)

plt.show()