# Categorical plot used for visualizing categorical data
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Categorical plot
sns.catplot(
    data=data,
    x="day",
    y="total_bill",
    kind="bar"
)

plt.show()