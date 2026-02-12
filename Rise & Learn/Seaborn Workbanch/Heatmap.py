# Heatmap is used for visualizing data in a matrix format where individual values are represented as colors.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("flights")

# Pivot table for heatmap
pivot = data.pivot("month", "year", "passengers")

# Heatmap
sns.heatmap(pivot, annot=True, fmt="d")

plt.show()