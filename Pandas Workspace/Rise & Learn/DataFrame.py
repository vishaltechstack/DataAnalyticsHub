'''
A DataFrame is a two-dimensional data structure in Pandas.
It looks like an Excel sheet or a SQL table with rows and columns.
    • Rows are identified by an index
    • Columns have names
    • Each column is a Series
Think of it as structured, labeled data that is easy to analyze and modify.


Named Indexes:

By default, Pandas gives row indexes as numbers: 0, 1, 2...
A named index means you explicitly give meaningful labels to rows.

Why named indexes matter:
    • Data becomes easier to read
    • Row selection becomes clearer
    • Useful when rows represent real entities (students, products, dates)

Example idea:
Index (Name) → Student Name
Columns → Marks, Age
'''

'''
Locate Row by Index (loc)
loc is used to access rows by label (name).

Rule to remember:
    • loc works with index labels, not positions
'''
import pandas as pd

# Example 1: Create a DataFrame with named indexes
data = {
    "Age": [20, 21, 22],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data, index=["Amit", "Neha", "Rahul"])
print(df)


# Example 2: Locate a single row using loc
print(df.loc["Neha"])


# Example 3: Locate multiple rows using loc
print(df.loc[["Amit", "Rahul"]])


# Example 4: Locate specific row and column
print(df.loc["Rahul", "Marks"])


# Example 5: Slice rows using named indexes
print(df.loc["Amit":"Rahul"])


'''
Key differences to remember:
    • loc → label-based selection
    • Index names must exist, otherwise error occurs
    • Named indexes improve readability and control

Quick summary:
    • DataFrame → table of labeled data
    • Named Index → meaningful row labels
    • loc → select rows using index names
'''