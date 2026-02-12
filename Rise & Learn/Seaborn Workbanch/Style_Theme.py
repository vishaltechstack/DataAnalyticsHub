# Style Theme used to set the overall aesthetic of the plots. It can be set using the sns.set_style() function, which accepts various style options such as "darkgrid", "whitegrid", "dark", "white", and "ticks". Each style option provides a different look and feel to the plots, allowing you to customize the appearance according to your preferences.
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set_style("darkgrid")

data = sns.load_dataset("tips")

# Plot with style
sns.scatterplot(
    data=data,
    x="total_bill",
    y="tip"
)

plt.show()