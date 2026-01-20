'''
Correlation measures how strongly two variables are related to each other.
In data analysis, it helps you understand relationships between numerical columns.

Correlation values range from -1 to +1:
    • +1 → perfect positive relationship
    • -1 → perfect negative relationship
    • 0 → no relationship

Why correlation matters:
    • Identify patterns in data
    • Detect features useful for modeling
    • Understand business relationships
    • Spot redundancy between variables
'''
import pandas as pd

data = {
    "Salary": [50000, 45000, 55000, 60000, 48000],
    "Experience": [2, 1, 3, 5, 2],
    "Age": [22, 21, 24, 28, 23]
}

df = pd.DataFrame(data)


'''
Calculate correlation in Pandas:

df.corr()
Computes pairwise correlation between numerical columns.
'''
# Example:
df.corr()


# Common correlation methods
df.corr(method="pearson")   # Linear relationship
df.corr(method="spearman")  # Rank-based, non-linear
df.corr(method="kendall")   # Ordinal data


# Correlation between two columns
df["Salary"].corr(df["Experience"])


'''
Important notes:
    • Correlation does not mean causation
    • Works only on numerical data
    • Outliers can affect correlation values
'''