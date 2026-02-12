# Pair plot used for visualizing the relationships between multiple variables in a dataset. It creates a grid of scatter plots for each pair of variables, along with histograms or density plots on the diagonal to show the distribution of each variable.
import seaborn as sns

data = sns.load_dataset("iris")

# Pair plot
sns.pairplot(data)