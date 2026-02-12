# Kde plot used for visualizing the distribution of a continuous variable. It estimates the probability density function of the variable, providing a smooth curve that represents the distribution of the data. This can be useful for identifying patterns, such as skewness or multimodality, in the data.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# KDE plot
sns.kdeplot(
    data=data,
    x="total_bill",
    fill=True
)

plt.show()