# Distribution plot used for visualizing the distribution of a dataset
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Distribution plot
sns.displot(
    data=data,
    x="total_bill"
)

plt.show()