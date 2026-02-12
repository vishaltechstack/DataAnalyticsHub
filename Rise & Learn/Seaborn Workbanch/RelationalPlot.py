# Relational plot used for visualizing the relationship between two variables. It can be used to show how one variable changes with respect to another variable. In this example, we will use the "tips" dataset from seaborn to create a relational plot that shows the relationship between total bill and tip.
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

# Relational plot
sns.relplot(
    data=data,
    x="total_bill",
    y="tip"
)

plt.show()