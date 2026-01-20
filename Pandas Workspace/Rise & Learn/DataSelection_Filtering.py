'''
Selecting the right subset of data is a core part of working with Pandas.
Pandas provides different ways to access data depending on whether you want to use labels, positions, or column names.

loc[] – Label-based selection
loc is used when you want to select data using row and column labels.

Key points:
    • Works with index names and column names
    • End label is included in slicing

Quick comparison:
    • loc[] → label-based selection
    • iloc[] → position-based selection
    • [] → column selection and simple filtering
'''
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "John", "Neha", "Rahul"],
    "Age": [22, 24, 23, 25],
    "Marks": [80, 75, 87, 90]
})

# Examples:
df.loc["Amit"]
df.loc["Amit", "Marks"]
df.loc[["Amit", "Neha"], ["Age", "Marks"]]
df.loc["Amit":"Rahul"]


'''
iloc[] – Integer position-based selection
iloc works with numerical positions, starting from 0.

Key points:
    • Uses row and column positions
    • End index is excluded in slicing
'''
# Examples:

df.iloc[0]
df.iloc[0, 1]
df.iloc[0:2]
df.iloc[:, 1]


'''
[] – Basic indexing operator
The square brackets are mainly used to select columns.
'''
# Examples:

df["Marks"]
df[["Age", "Marks"]]