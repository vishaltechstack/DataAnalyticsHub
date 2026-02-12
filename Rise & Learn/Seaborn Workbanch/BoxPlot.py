# Box plot is used to display the distribution of data based on five summary statistics:
# minimum, first quartile (Q1), median, third quartile (Q3), and maximum.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Box plot
sns.boxplot(
    data=data,
    x="day",
    y="total_bill"
)

plt.show()